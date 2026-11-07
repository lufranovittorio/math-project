#!/usr/bin/env python3
"""Build and consistency tool for the Math Project.

    python make.py check    check labels, references and tags
    python make.py tags     give a permanent tag to every label that has none
    python make.py status   show the status of every chapter
    python make.py pdf      build output/pdf/book.pdf
    python make.py html     build the website in output/html
    python make.py pdf-parts  one PDF per part in output/pdf/parts (after pdf)
    python make.py preview <chapter>...  website pages of these chapters only (after html)
    python make.py all      tags, check, pdf, pdf-parts and html
    python make.py serve    serve the website at http://localhost:8000
    python make.py pages    commit output/html to the gh-pages branch (GitHub Pages)
    python make.py lean     check the Mathlib names in web/mathlib.txt online
"""

import argparse
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata
import urllib.parse
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BOOK = ROOT / "book.tex"
CHAPTER_DIR = ROOT / "chapters"
BIBLIOGRAPHY = ROOT / "math-project.bib"
TAGS_FILE = ROOT / "tags" / "tags"
MATHLIB_FILE = ROOT / "web" / "mathlib.txt"
MATHLIB_DOCS = "https://leanprover-community.github.io/mathlib4_docs/"
REPOSITORY = "https://github.com/lufranovittorio/math-project"
SITE_URL = "https://lufranovittorio.github.io/math-project/"
OUTPUT = ROOT / "output"
PDF_DIR = OUTPUT / "pdf"
HTML_DIR = OUTPUT / "html"
GENERATED_MARKER = ".generated-by-make"

# MathJax 2.7.9 with HTML-CSS output renders formulas as real text, so they
# can be selected; MathJax 3 does not.
MATHJAX_URL = ("https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/"
               "MathJax.js?config=TeX-AMS-MML_HTMLorMML")

# Numbered environments (see preamble.tex). The label of each one must be
# <chapter>:<environment>-<name>.
THEOREM_ENVS = {"theorem", "proposition", "lemma", "corollary", "conjecture",
                "definition", "example", "counterexample", "exercise",
                "notation", "remark"}
EQUATION_ENVS = {"equation", "align", "gather", "multline", "alignat", "flalign"}
PROOF_ENVS = {"proof", "solution"}
SECTIONING = {"section", "subsection", "subsubsection"}

STATUSES = {
    "planned": "Only an outline of this chapter exists.",
    "draft": "This chapter is being written; its proofs have not been checked.",
    "complete": "This chapter is written; its proofs await independent checking.",
    "checked": "Every proof in this chapter has been checked.",
}

# Chapters that may refer forward (see the introduction).
FORWARD_REFERENCE_CHAPTERS = {"introduction"}

NAME = r"[a-z0-9]+(?:-[a-z0-9]+)*"
TAG_RE = re.compile(r"[0-9A-Z]{4}")
TAG_DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

TOKEN_RE = re.compile(
    r"\\(?P<beginend>begin|end)\{(?P<env>[^}]+)\}"
    r"|\\label\{(?P<label>[^}]+)\}"
    r"|\\(?:ref|eqref|pageref|autoref)\{(?P<ref>[^}]+)\}"
    r"|\\cite\*?(?:\[[^\]]*\])?\{(?P<cite>[^}]+)\}"
    r"|\\(?P<sectioning>part|chapter|section|subsection|subsubsection)\*?(?=[\[{])"
    r"|\\chapterstatus\{(?P<status>[^}]*)\}"
)


@dataclass
class Chapter:
    slug: str
    number: int
    part: str
    title: str = ""
    status: str = ""


@dataclass
class Label:
    name: str
    chapter: str
    where: str
    position: int


@dataclass
class Reference:
    target: str
    chapter: str
    where: str
    position: int
    context: str  # "proof", "prerequisites" or "text"
    owner: str = None  # the numbered statement whose statement or proof contains it


@dataclass
class Project:
    chapters: list = field(default_factory=list)
    labels: dict = field(default_factory=dict)
    references: list = field(default_factory=list)
    citations: list = field(default_factory=list)  # (key, where)
    equation_owner: dict = field(default_factory=dict)  # equation label -> statement
    errors: list = field(default_factory=list)
    warnings: list = field(default_factory=list)
    position: int = 0

    def next_position(self):
        self.position += 1
        return self.position


def strip_comment(line):
    return re.sub(r"(?<!\\)%.*", "", line)


def latex_to_text(s):
    """Rough plain-text rendering of a title, for terminal output only."""
    accents = {'"': "\u0308", "'": "\u0301", "`": "\u0300", "v": "\u030c", "^": "\u0302"}
    s = re.sub(r"\\([\"'`^])\{?([A-Za-z])\}?", lambda m: m.group(2) + accents[m.group(1)], s)
    s = re.sub(r"\\v\{([A-Za-z])\}", lambda m: m.group(1) + accents["v"], s)
    s = s.replace("--", "\u2013").replace("$", "")
    return unicodedata.normalize("NFC", s)


# ---------------------------------------------------------------------------
# Scanning the sources
# ---------------------------------------------------------------------------

def scan_project():
    project = Project()
    part = ""
    for lineno, raw in enumerate(BOOK.read_text(encoding="utf-8").splitlines(), 1):
        line = strip_comment(raw)
        where = f"book.tex:{lineno}"
        m = re.search(r"\\part\{([^}]*)\}", line)
        if m:
            part = m.group(1)
        for m in re.finditer(r"\\label\{([^}]+)\}", line):
            name = m.group(1)
            if not re.fullmatch(f"part-{NAME}", name):
                project.errors.append(f"{where}: part label '{name}' must have the form part-<name>")
            add_label(project, Label(name, "book", where, project.next_position()))
        for m in re.finditer(r"\\include\{chapters/([^}]+)\}", line):
            chapter = Chapter(m.group(1), len(project.chapters) + 1, part)
            project.chapters.append(chapter)
            scan_chapter(project, chapter)
    check_references(project)
    return project


def add_label(project, label):
    if label.name in project.labels:
        other = project.labels[label.name]
        project.errors.append(f"{label.where}: label '{label.name}' already defined at {other.where}")
        return
    project.labels[label.name] = label


def scan_chapter(project, chapter):
    path = CHAPTER_DIR / f"{chapter.slug}.tex"
    rel = f"chapters/{chapter.slug}.tex"
    if not path.exists():
        project.errors.append(f"book.tex includes {rel}, which does not exist")
        return
    if not re.fullmatch(NAME, chapter.slug):
        project.errors.append(f"{rel}: file name must be lower case words separated by hyphens")

    stack = []  # entries [environment, line, labelled]
    in_section = False
    has_chapter_label = False
    # The last labelled numbered environment: references inside it or inside
    # the proof that follows it are dependencies of that statement.
    last_item = None

    # A shell or a script can turn "\r", "\t", "\b", "\f" in "\ref", "\theta",
    # "\beta", "\frac" into control characters; report any that are left.
    source = path.read_bytes().replace(b"\r\n", b"\n")
    for m in re.finditer(rb"[\x00-\x08\x0b-\x1f\x7f]", source):
        lineno = source.count(b"\n", 0, m.start()) + 1
        project.errors.append(f"{rel}:{lineno}: control character {m.group(0)!r} (a backslash lost to escaping?)")

    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = strip_comment(raw)
        where = f"{rel}:{lineno}"
        sectioning = None
        for m in accent_macro_re().finditer(line):
            project.errors.append(f"{where}: write \\{m.group(1)}{{\\{m.group(2)}}}: plasTeX expands the macro "
                                  f"before MathJax sees it, and MathJax then misreads \\{m.group(0)[1:]}")
        for m in TOKEN_RE.finditer(line):
            if m.group("beginend") == "begin":
                env = m.group("env")
                if env in THEOREM_ENVS and not in_section:
                    project.warnings.append(f"{where}: {env} outside of any section")
                stack.append([env, lineno, False])
            elif m.group("beginend") == "end":
                env = m.group("env")
                if not stack or stack[-1][0] != env:
                    project.errors.append(f"{where}: \\end{{{env}}} does not match the open environment")
                    while stack and stack[-1][0] != env:
                        stack.pop()
                    if not stack:
                        continue
                opened, start, labelled = stack.pop()
                if opened in THEOREM_ENVS and not labelled:
                    project.warnings.append(f"{rel}:{start}: {opened} has no label")
            elif m.group("sectioning"):
                sectioning = m.group("sectioning")
                if sectioning == "part":
                    project.errors.append(f"{where}: \\part belongs in book.tex, not in a chapter")
                elif sectioning == "chapter":
                    t = re.search(r"\\chapter\*?\{(.*?)\}\\label", line) or re.search(r"\\chapter\*?\{(.*)\}", line)
                    chapter.title = latex_to_text(t.group(1)) if t else chapter.slug
                else:
                    in_section = True
            elif m.group("label"):
                name = m.group("label")
                check_label(project, chapter, name, where, stack, sectioning)
                if name == chapter.slug:
                    has_chapter_label = True
                add_label(project, Label(name, chapter.slug, where, project.next_position()))
                innermost = stack[-1][0] if stack else None
                if innermost in THEOREM_ENVS:
                    last_item = name
                elif innermost in EQUATION_ENVS and in_statement(stack) and last_item:
                    project.equation_owner[name] = last_item
            elif m.group("ref"):
                if any(entry[0] in PROOF_ENVS for entry in stack):
                    context = "proof"
                elif "Prerequisites" in line:
                    context = "prerequisites"
                else:
                    context = "text"
                owner = last_item if in_statement(stack) else None
                for target in m.group("ref").split(","):
                    project.references.append(Reference(
                        target.strip(), chapter.slug, where, project.next_position(), context, owner))
            elif m.group("cite"):
                for key in m.group("cite").split(","):
                    project.citations.append((key.strip(), where))
            elif m.group("status") is not None:
                status = m.group("status").strip()
                if status not in STATUSES:
                    project.errors.append(f"{where}: unknown status '{status}' (use {', '.join(STATUSES)})")
                chapter.status = status

    for env, start, _ in stack:
        project.errors.append(f"{rel}:{start}: \\begin{{{env}}} is never closed")
    if not has_chapter_label:
        project.errors.append(f"{rel}: the chapter must be labelled \\label{{{chapter.slug}}}")
    if not chapter.status:
        project.errors.append(f"{rel}: missing \\chapterstatus{{...}}")


def in_statement(stack):
    """Whether the current position is inside a numbered environment or a proof."""
    return any(entry[0] in THEOREM_ENVS or entry[0] in PROOF_ENVS for entry in stack)


def dependency_graph(project):
    """Map each numbered statement to the numbered statements it refers to.

    A statement depends on what its statement and its proof refer to; a
    reference to an equation counts as one to the statement containing it."""
    uses = {}
    for ref in project.references:
        target = project.equation_owner.get(ref.target, ref.target)
        if not ref.owner or target == ref.owner or target not in project.labels:
            continue
        kind = target.partition(":")[2].split("-")[0]
        if kind in THEOREM_ENVS:
            uses.setdefault(ref.owner, set()).add(target)
    return uses


_ACCENT_MACRO_RE = None


def accent_macro_re():
    """Matches an accent applied to a macro of macros.tex without braces, e.g. \\bar\\QQ."""
    global _ACCENT_MACRO_RE
    if _ACCENT_MACRO_RE is None:
        names = re.findall(r"\\newcommand\{\\([A-Za-z]+)\}(?!\[)", (ROOT / "macros.tex").read_text(encoding="utf-8"))
        accents = ("bar", "hat", "tilde", "check", "vec", "dot", "ddot", "breve", "acute", "grave",
                   "overline", "underline", "widehat", "widetilde", "mathring")
        _ACCENT_MACRO_RE = re.compile(r"\\(" + "|".join(accents) + r")\\("
                                      + "|".join(sorted(names, key=len, reverse=True)) + r")(?![A-Za-z])")
    return _ACCENT_MACRO_RE


def check_label(project, chapter, name, where, stack, sectioning):
    innermost = stack[-1] if stack else None
    if innermost and (innermost[0] in THEOREM_ENVS or innermost[0] in EQUATION_ENVS):
        kind = "equation" if innermost[0] in EQUATION_ENVS else innermost[0]
        innermost[2] = True
    elif sectioning == "chapter":
        if name != chapter.slug:
            project.errors.append(f"{where}: the chapter label must be '{chapter.slug}', not '{name}'")
        return
    elif sectioning in SECTIONING:
        kind = sectioning
    else:
        project.errors.append(
            f"{where}: label '{name}' is not attached to a numbered environment, an equation or a sectioning command")
        return
    if not re.fullmatch(f"{re.escape(chapter.slug)}:{kind}-{NAME}", name):
        project.errors.append(f"{where}: label '{name}' should have the form {chapter.slug}:{kind}-<name>")


def bibliography_keys():
    if not BIBLIOGRAPHY.exists():
        return set()
    text = BIBLIOGRAPHY.read_text(encoding="utf-8")
    return set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", text))


def bibliography_years():
    """Year of each bibliography entry, from math-project.bib."""
    if not BIBLIOGRAPHY.exists():
        return {}
    text = BIBLIOGRAPHY.read_text(encoding="utf-8")
    years = {}
    for m in re.finditer(r"@\w+\s*\{\s*([^,\s]+)\s*,(.*?)(?=\n@|\Z)", text, re.S):
        y = re.search(r"\byear\s*=\s*[{\"]?\s*(\d{4})", m.group(2))
        if y:
            years[m.group(1)] = y.group(1)
    return years


def check_references(project):
    keys = bibliography_keys()
    for key, where in project.citations:
        if key not in keys:
            project.errors.append(f"{where}: citation '{key}' is not in {BIBLIOGRAPHY.name}")
    for ref in project.references:
        label = project.labels.get(ref.target)
        if label is None:
            project.errors.append(f"{ref.where}: reference to undefined label '{ref.target}'")
            continue
        if label.position < ref.position or ref.chapter in FORWARD_REFERENCE_CHAPTERS:
            continue
        if ref.context == "proof":
            project.errors.append(f"{ref.where}: forward reference to '{ref.target}' inside a proof")
        elif ref.context == "prerequisites":
            project.errors.append(f"{ref.where}: prerequisite '{ref.target}' comes later in book.tex")
        elif ":" in ref.target and label.chapter != ref.chapter:
            # Outside proofs, forward references within a chapter and to whole
            # chapters or parts are fine; forward references to results of
            # later chapters are discouraged.
            project.warnings.append(f"{ref.where}: forward reference to '{ref.target}'")


# ---------------------------------------------------------------------------
# Tags
# ---------------------------------------------------------------------------

def read_tags(project=None):
    """Return the list of (tag, label) pairs in tags/tags."""
    pairs = []
    if not TAGS_FILE.exists():
        return pairs
    for lineno, raw in enumerate(TAGS_FILE.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        tag, sep, label = line.partition(",")
        if not sep or not TAG_RE.fullmatch(tag):
            if project:
                project.errors.append(f"tags/tags:{lineno}: malformed line '{line}'")
            continue
        pairs.append((tag, label))
    return pairs


def check_tags(project):
    pairs = read_tags(project)
    seen_tags, seen_labels = {}, {}
    for tag, label in pairs:
        if tag in seen_tags:
            project.errors.append(f"tags/tags: tag {tag} is used twice")
        if label in seen_labels:
            project.errors.append(f"tags/tags: label '{label}' has two tags ({seen_labels[label]} and {tag})")
        seen_tags[tag] = label
        seen_labels[label] = tag
    for label in project.labels:
        if label not in seen_labels:
            project.warnings.append(f"label '{label}' has no tag yet (run: python make.py tags)")
    for tag, label in pairs:
        # "alias:<label>": the tag of an item that was merged into another
        # one (for instance the introduction of a chapter merged into an
        # earlier chapter); its page leads to <label>.
        if label.startswith("alias:"):
            if label[len("alias:"):] not in project.labels:
                project.warnings.append(f"tag {tag} is an alias of '{label[6:]}', which does not exist")
            continue
        if label not in project.labels:
            project.warnings.append(
                f"tag {tag} points to '{label}', which no longer exists "
                "(if the label was renamed, edit tags/tags; never reuse or delete a tag)")


# ---------------------------------------------------------------------------
# Links to Mathlib
# ---------------------------------------------------------------------------

LEAN_NAME_RE = re.compile(r"[^\s#]+")


def read_mathlib(project=None):
    """Return the dict label -> Mathlib declaration of web/mathlib.txt."""
    links = {}
    if not MATHLIB_FILE.exists():
        return links
    for lineno, raw in enumerate(MATHLIB_FILE.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        where = f"web/mathlib.txt:{lineno}"
        if len(parts) != 2 or not LEAN_NAME_RE.fullmatch(parts[1]):
            if project:
                project.errors.append(f"{where}: expected '<label> <Mathlib declaration>'")
            continue
        label, name = parts
        if project:
            if label in links:
                project.errors.append(f"{where}: label '{label}' is listed twice")
            elif label not in project.labels:
                project.errors.append(f"{where}: unknown label '{label}'")
        links[label] = name
    return links


def command_lean(args):
    """Check that every declaration in web/mathlib.txt exists in the current Mathlib."""
    import urllib.request
    links = read_mathlib()
    url = MATHLIB_DOCS + "declarations/declaration-data.bmp"
    print(f"lean: downloading the list of Mathlib declarations ({url})")
    with urllib.request.urlopen(url) as response:
        declarations = json.loads(response.read().decode("utf-8"))["declarations"]
    missing = [(label, name) for label, name in links.items() if name not in declarations]
    for label, name in missing:
        print(f"lean: {name} (for {label}) is not in Mathlib any more")
    print(f"lean: {len(links) - len(missing)} of {len(links)} declarations found")
    return not missing


def tag_to_int(tag):
    return int(tag, 36)


def int_to_tag(n):
    digits = ""
    while n:
        n, r = divmod(n, 36)
        digits = TAG_DIGITS[r] + digits
    return digits.rjust(4, "0")


def assign_tags(project):
    pairs = read_tags()
    tagged = {label for _, label in pairs}
    next_number = max((tag_to_int(tag) for tag, _ in pairs), default=0) + 1
    new_lines = []
    for label in sorted(project.labels.values(), key=lambda l: l.position):
        if label.name in tagged:
            continue
        new_lines.append(f"{int_to_tag(next_number)},{label.name}")
        next_number += 1
    if new_lines:
        TAGS_FILE.parent.mkdir(exist_ok=True)
        header = "" if TAGS_FILE.exists() else (
            "# Permanent tags: one line TAG,label per item.\n"
            "# Never delete or reuse a tag. If a label is renamed, edit its line here.\n")
        with TAGS_FILE.open("a", encoding="utf-8", newline="\n") as f:
            f.write(header + "".join(line + "\n" for line in new_lines))
    print(f"tags: {len(new_lines)} new tag(s), {len(pairs) + len(new_lines)} in total")


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def report(project):
    for w in project.warnings:
        print(f"warning: {w}")
    for e in project.errors:
        print(f"error: {e}")
    print(f"check: {len(project.chapters)} chapters, {len(project.labels)} labels, "
          f"{len(project.references)} references, "
          f"{len(project.errors)} error(s), {len(project.warnings)} warning(s)")
    return not project.errors


def command_check(args):
    project = scan_project()
    check_tags(project)
    read_mathlib(project)
    return report(project)


def command_tags(args):
    project = scan_project()
    if project.errors:
        report(project)
        print("tags: fix the errors above before assigning tags")
        return False
    assign_tags(project)
    return True


def command_status(args):
    project = scan_project()
    part = None
    counts = {s: 0 for s in STATUSES}
    for chapter in project.chapters:
        if chapter.part != part:
            part = chapter.part
            print(f"\n{part or '(no part)'}")
        counts[chapter.status] = counts.get(chapter.status, 0) + 1
        print(f"  {chapter.number:3d}  {chapter.status:9s} {chapter.title}")
    print("\n" + ", ".join(f"{n} {s}" for s, n in counts.items()))
    return True


def prepare(args):
    """Assign tags and check the project before a build."""
    project = scan_project()
    if not project.errors:
        assign_tags(project)
    check_tags(project)
    read_mathlib(project)
    ok = report(project)
    if not ok and not args.force:
        print("build stopped because of errors (use --force to build anyway)")
    return project, ok or args.force


def run_logged(cmd, log_path, env=None):
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("w", encoding="utf-8", errors="replace") as log:
        result = subprocess.run(cmd, cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, env=env)
    return result.returncode


def command_pdf(args, project=None):
    if project is None:
        project, ok = prepare(args)
        if not ok:
            return False
    latexmk = shutil.which("latexmk")
    if not latexmk:
        print("pdf: latexmk not found")
        return False
    (PDF_DIR / "chapters").mkdir(parents=True, exist_ok=True)
    cmd = [latexmk, "-pdf", "-interaction=nonstopmode", "-halt-on-error",
           "-file-line-error", "-outdir=output/pdf", "book.tex"]
    # latexmk runs BibTeX inside output/pdf, so tell it where the .bib file is.
    env = dict(os.environ, BIBINPUTS=str(ROOT) + os.pathsep)
    print("pdf: running latexmk (log: output/latexmk.log)")
    code = run_logged(cmd, OUTPUT / "latexmk.log", env)
    if code != 0:
        log = PDF_DIR / "book.log"
        if log.exists():
            lines = log.read_text(encoding="utf-8", errors="replace").splitlines()
            for i, line in enumerate(lines):
                if line.startswith("!") or re.match(r"^\S+\.tex:\d+:", line):
                    print("  " + "\n  ".join(lines[i:i + 3]))
        print("pdf: FAILED")
        return False
    print(f"pdf: wrote {(PDF_DIR / 'book.pdf').relative_to(ROOT)}")
    return True


PARTS_DIR = PDF_DIR / "parts"


def book_parts():
    """The parts of book.tex: (label, title, number, chapters)."""
    project = scan_project()
    parts, number = [], 0
    for raw in BOOK.read_text(encoding="utf-8").splitlines():
        line = strip_comment(raw)
        m = re.search(r"\\part\{([^}]*)\}\\label\{([^}]+)\}", line)
        if m:
            number += 1
            parts.append((m.group(2), m.group(1), number, []))
    by_title = {title: chapters for _, title, _, chapters in parts}
    for chapter in project.chapters:
        if chapter.part in by_title:
            by_title[chapter.part].append(chapter)
    return [p for p in parts if p[3]]


def external_labels(exclude):
    """\\newlabel lines of the full book for the labels not in exclude, without links.

    A part PDF contains only some chapters; the references to the other chapters
    must still print their numbers, which the full build wrote to the .aux files.
    The anchor is left empty, so that hyperref prints the number without a link
    to a place that is not in the file."""
    lines = []
    for aux in [PDF_DIR / "book.aux", *sorted((PDF_DIR / "chapters").glob("*.aux"))]:
        for line in aux.read_text(encoding="utf-8", errors="replace").splitlines():
            if not line.startswith("\\newlabel{"):
                continue
            groups = brace_groups(line[len("\\newlabel"):])
            if len(groups) != 2 or groups[0] in exclude:
                continue
            fields = brace_groups(groups[1])
            if len(fields) < 3:
                continue
            number, page, title = fields[0], fields[1], fields[2]
            lines.append(f"\\newlabel{{{groups[0]}}}{{{{{number}}}{{{page}}}{{{title}}}{{}}{{}}}}")
    return lines


def brace_groups(text):
    """The top-level {...} groups of text, without their braces."""
    groups, depth, start, i = [], 0, 0, 0
    while i < len(text):
        c = text[i]
        if c == "\\":
            i += 2
            continue
        if c == "{":
            if depth == 0:
                start = i + 1
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                groups.append(text[start:i])
        i += 1
    return groups


PART_TEMPLATE = r"""%% Generated by make.py pdf-parts; do not edit.
\documentclass[11pt,openany]{book}
\input{preamble}
\input{macros}
\title{The Math Project\\[3ex]\Large Part @NUMBER@: @TITLE@}
\author{}
\date{}
\makeatletter
\AtBeginDocument{\input{@LABELS@}}
\makeatother
\begin{document}
\maketitle
\tableofcontents
\setcounter{part}{@PREVIOUS@}
\part{@TITLE@}\label{@LABEL@}
@CHAPTERS@
\cleardoublepage
\phantomsection
\addcontentsline{toc}{chapter}{Bibliography}
\bibliographystyle{amsalpha}
\bibliography{math-project}
\end{document}
"""


def command_pdf_parts(args, project=None):
    """One PDF per part, with the numbers of the full book.

    Needs the .aux files of a full PDF build (python make.py pdf)."""
    if project is None:
        project, ok = prepare(args)
        if not ok:
            return False
    if not (PDF_DIR / "book.aux").exists():
        print("pdf-parts: build the full PDF first (python make.py pdf)")
        return False
    latexmk = shutil.which("latexmk")
    if not latexmk:
        print("pdf-parts: latexmk not found")
        return False
    PARTS_DIR.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, BIBINPUTS=str(ROOT) + os.pathsep)
    wanted = set(getattr(args, "parts", None) or [])
    failed = []
    for label, title, number, chapters in book_parts():
        if wanted and label not in wanted and label.removeprefix("part-") not in wanted:
            continue
        slugs = {c.slug for c in chapters}
        exclude = {label} | {name for name, info in project.labels.items() if info.chapter in slugs}
        labels_file = PARTS_DIR / f"{label}-labels.tex"
        labels_file.write_text("\\makeatletter\n" + "\n".join(external_labels(exclude)) + "\n\\makeatother\n",
                               encoding="utf-8")
        body = "\n".join(f"\\setcounter{{chapter}}{{{c.number - 1}}}\n\\input{{chapters/{c.slug}}}"
                         for c in chapters)
        tex = (PART_TEMPLATE.replace("@NUMBER@", roman(number)).replace("@TITLE@", title)
               .replace("@PREVIOUS@", str(number - 1)).replace("@LABEL@", label)
               .replace("@LABELS@", labels_file.relative_to(ROOT).as_posix()).replace("@CHAPTERS@", body))
        source = PARTS_DIR / f"{label}.tex"
        source.write_text(tex, encoding="utf-8")
        cmd = [latexmk, "-pdf", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error",
               f"-outdir={PARTS_DIR.relative_to(ROOT).as_posix()}", source.relative_to(ROOT).as_posix()]
        print(f"pdf-parts: Part {roman(number)}, {title} ({len(chapters)} chapters)")
        if run_logged(cmd, OUTPUT / f"latexmk-{label}.log", env) != 0:
            failed.append(label)
    if failed:
        print("pdf-parts: FAILED for " + ", ".join(failed) + " (logs: output/latexmk-<part>.log)")
        return False
    print(f"pdf-parts: wrote {PARTS_DIR.relative_to(ROOT)}/part-*.pdf")
    return True


def roman(n):
    out = ""
    for value, letters in [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
                           (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]:
        while n >= value:
            out, n = out + letters, n - value
    return out


BYSAME_RULE = r"\providecommand{\bysame}{\leavevmode\hbox to3em{\hrulefill}\thinspace}"
BYSAME_DASHES = r"\providecommand{\bysame}{\textemdash\textemdash\textemdash}"


def command_html(args, project=None):
    if project is None:
        project, ok = prepare(args)
        if not ok:
            return False
    plastex = shutil.which("plastex")
    if not plastex:
        print("html: plastex not found")
        return False
    if HTML_DIR.exists():
        if not (HTML_DIR / GENERATED_MARKER).exists():
            print(f"html: {HTML_DIR} was not created by make.py; remove it by hand first")
            return False
        shutil.rmtree(HTML_DIR)
    HTML_DIR.mkdir(parents=True)
    for stray in ROOT.glob("*.paux"):
        if stray.name != "book.paux":
            stray.unlink()
    # plasTeX reads the bibliography from book.bbl, which BibTeX produces
    # during the PDF build.
    bbl = PDF_DIR / "book.bbl"
    if bbl.exists():
        # amsalpha writes a repeated author list as \bysame, a rule built with
        # \hbox to3em{\hrulefill}, which plasTeX prints as "to3em"; use dashes.
        text = bbl.read_text(encoding="utf-8")
        text = text.replace(BYSAME_RULE, BYSAME_DASHES)
        (ROOT / "book.bbl").write_text(text, encoding="utf-8")
    else:
        print("html: output/pdf/book.bbl is missing; run 'python make.py pdf' first "
              "or the bibliography will be empty")
    # The theme path must be absolute: plasTeX looks for the theme's scripts
    # after changing into the output directory.
    cmd = [plastex, "--renderer", "HTML5",
           "--extra-templates", str(ROOT / "web"), "--theme", "math", "--theme-css", "math",
           "--split-level", "1",
           "--filename", "index [$id, $title(4), $num(4)]",
           "--imager", "pdftoppm", "--vector-imager", "dvisvgm",
           "--mathjax-url", MATHJAX_URL,
           "--dir", "output/html", "book.tex"]
    print("html: running plasTeX (log: output/plastex.log)")
    code = run_logged(cmd, OUTPUT / "plastex.log")
    (HTML_DIR / GENERATED_MARKER).write_text("Created by make.py; safe to delete.\n", encoding="utf-8")
    log_lines = (OUTPUT / "plastex.log").read_text(encoding="utf-8", errors="replace").splitlines()
    problems = sorted({l.strip() for l in log_lines if l.startswith(("WARNING", "ERROR"))})
    for line in problems[:40]:
        print(f"  plasTeX {line}")
    if code != 0 or not (HTML_DIR / "index.html").exists():
        print("html: FAILED")
        return False
    pdf = PDF_DIR / "book.pdf"
    if pdf.exists():
        shutil.copy2(pdf, HTML_DIR / "book.pdf")
    # Before the post-processing, which links the part PDFs that exist.
    part_pdfs = sorted(PARTS_DIR.glob("part-*.pdf")) if PARTS_DIR.exists() else []
    if part_pdfs:
        (HTML_DIR / "pdf").mkdir(exist_ok=True)
        for part_pdf in part_pdfs:
            shutil.copy2(part_pdf, HTML_DIR / "pdf" / part_pdf.name)
    postprocess_html(project)
    print(f"html: wrote {HTML_DIR.relative_to(ROOT)}/index.html")
    return True


PREVIEW_DIR = HTML_DIR / "preview"
LINK_RE = re.compile(r'\b(href|src)="(?![a-z]+:|/|#|\.\./)([^"#?]+)([^"]*)"')

PREVIEW_TEMPLATE = r"""%% Generated by make.py preview; do not edit.
\documentclass[11pt,openany]{book}
\input{preamble}
\input{macros}
\title{The Math Project (preview)}
\author{}
\date{}
\begin{document}
@CHAPTERS@
\bibliographystyle{amsalpha}
\bibliography{math-project}
\end{document}
"""


def command_preview(args):
    """Build the website pages of some chapters only, in output/html/preview.

    References to other chapters are resolved with book.paux, which plasTeX
    writes during a full website build, and the links to them point to the
    pages of that build."""
    project, ok = prepare(args)
    if not ok:
        return False
    chapters = {c.slug: c for c in project.chapters}
    unknown = [s for s in args.chapters if s not in chapters]
    if unknown:
        print("preview: unknown chapter(s): " + ", ".join(unknown))
        return False
    if not (ROOT / "book.paux").exists() or not (HTML_DIR / "index.html").exists():
        print("preview: needs a full website build first (python make.py html)")
        return False
    plastex = shutil.which("plastex")
    if not plastex:
        print("preview: plastex not found")
        return False
    if PREVIEW_DIR.exists():
        shutil.rmtree(PREVIEW_DIR)
    body = "\n".join(f"\\setcounter{{chapter}}{{{chapters[s].number - 1}}}\n\\input{{chapters/{s}}}"
                     for s in sorted(args.chapters, key=lambda s: chapters[s].number))
    source = ROOT / "preview.tex"
    source.write_text(PREVIEW_TEMPLATE.replace("@CHAPTERS@", body), encoding="utf-8")
    # The whole bibliography, so that entries added since the last full
    # build are found too; failing BibTeX, that of the full build.
    (ROOT / "preview.aux").write_text("\\citation{*}\n\\bibstyle{amsalpha}\n\\bibdata{math-project}\n",
                                      encoding="utf-8")
    bibtex = shutil.which("bibtex")
    if bibtex:
        subprocess.run([bibtex, "preview"], cwd=ROOT, capture_output=True)
    if (ROOT / "preview.bbl").exists():
        bbl = (ROOT / "preview.bbl").read_text(encoding="utf-8")
        (ROOT / "preview.bbl").write_text(bbl.replace(BYSAME_RULE, BYSAME_DASHES), encoding="utf-8")
    elif (ROOT / "book.bbl").exists():
        shutil.copy2(ROOT / "book.bbl", ROOT / "preview.bbl")
    cmd = [plastex, "--renderer", "HTML5",
           "--extra-templates", str(ROOT / "web"), "--theme", "math", "--theme-css", "math",
           "--split-level", "1",
           "--filename", "index [$id, $title(4), $num(4)]",
           "--imager", "pdftoppm", "--vector-imager", "dvisvgm",
           "--mathjax-url", MATHJAX_URL,
           "--dir", PREVIEW_DIR.relative_to(ROOT).as_posix(), "preview.tex"]
    print("preview: running plasTeX (log: output/plastex-preview.log)")
    try:
        code = run_logged(cmd, OUTPUT / "plastex-preview.log")
    finally:
        # A stray preview.paux would be loaded by the next full build.
        for leftover in [source] + [ROOT / f"preview.{ext}" for ext in ("paux", "bbl", "aux", "blg")]:
            if leftover.exists():
                leftover.unlink()
    if code != 0 or not (PREVIEW_DIR / "index.html").exists():
        print("preview: FAILED")
        return False
    decorator = PageDecorator(project, PREVIEW_DIR)

    def relink(m):
        # Pages, tags and assets that the preview does not contain are those
        # of the full build, one directory up.
        if (PREVIEW_DIR / m.group(2)).exists():
            return m.group(0)
        return f'{m.group(1)}="../{m.group(2)}{m.group(3)}"'

    for path in PREVIEW_DIR.glob("*.html"):
        text = decorator.decorate(path.read_text(encoding="utf-8"), path.name)
        path.write_text(LINK_RE.sub(relink, text), encoding="utf-8")
    version_assets(PREVIEW_DIR)
    log_lines = (OUTPUT / "plastex-preview.log").read_text(encoding="utf-8", errors="replace").splitlines()
    for line in sorted({l.strip() for l in log_lines if l.startswith(("WARNING", "ERROR"))})[:40]:
        print(f"  plasTeX {line}")
    for slug in args.chapters:
        print(f"preview: http://localhost:8000/preview/{slug}.html (python make.py serve)")
    return True


def command_all(args):
    project, ok = prepare(args)
    if not ok:
        return False
    return (command_pdf(args, project) and command_pdf_parts(args, project)
            and command_html(args, project))


def command_serve(args):
    if not (HTML_DIR / "index.html").exists():
        print("serve: build the website first (python make.py html)")
        return False
    print(f"Serving {HTML_DIR} at http://localhost:{args.port} (Ctrl+C to stop)")
    try:
        subprocess.run([sys.executable, "-m", "http.server", str(args.port),
                        "--directory", str(HTML_DIR)])
    except KeyboardInterrupt:
        pass
    return True


# ---------------------------------------------------------------------------
# Website post-processing: tags, status banners, tag pages
# ---------------------------------------------------------------------------

THM_HEADING_RE = re.compile(r'<div class="(\w+)_thmwrapper[^"]*" id="([^"]+)">\s*<div class="\1_thmheading">')
HEADING_RE = re.compile(r'<h(\d) id="([^"]+)">(.*?)</h\1>', re.S)
CITE_RE = re.compile(r'<span class="cite">.*?</span>', re.S)
# A citation link as plasTeX writes it, and a bibliography entry heading;
# neither matches again once decorated.
BIB_CITE_RE = re.compile(r'<a href="Bibliography\.html#([^"]+)"\s*>')
BIB_DT_RE = re.compile(r'<dt><a name="([^"]+)">')
TOC_LINK_RE = re.compile(r'(<a [^>]*data-label="([^"]+)"[^>]*>.*?</a>)', re.S)
ID_RE = re.compile(r'\bid="([^"]+)"')
EQ_LABEL_RE = re.compile(r'(?<=\\begin\{equation\})\s*\\label\{[^}]*\}')


def tag_badge(tag):
    return f'<a class="tag" href="tag/{tag}.html" title="Permanent link: tag {tag}">{tag}</a>'


def graph_badge(tag):
    return (f'<a class="graph-link" href="graph.html?tag={tag}" title="Dependencies of tag {tag}: what it uses and '
            f'what uses it" aria-label="Dependency graph of tag {tag}"><svg viewBox="0 0 16 16" width="13" height="13" '
            f'aria-hidden="true"><circle cx="3" cy="8" r="2" fill="currentColor"/><circle cx="13" cy="3.5" r="2" '
            f'fill="currentColor"/><circle cx="13" cy="12.5" r="2" fill="currentColor"/><path d="M4.8 7.2 11.2 4.3M4.8 '
            f'8.8l6.4 2.9" stroke="currentColor" stroke-width="1.3"/></svg></a>')


def lean_badge(name):
    url = MATHLIB_DOCS + "find/?pattern=" + urllib.parse.quote(name, safe="") + "#doc"
    return (f'<a class="lean-link" href="{html.escape(url)}" title="Formalised in Lean&#39;s Mathlib, possibly in a '
            f'different generality: {html.escape(name)}">Lean</a>')


def issue_url(title, body):
    query = urllib.parse.urlencode({"title": title, "body": body})
    return f"{REPOSITORY}/issues/new?{query}"


def report_footer(page, title):
    """A link that opens a GitHub issue about the page, prefilled with its address."""
    body = (f"Page: {page}\n\nTag of the item (if any): \n\nWhat is wrong, and what should it say?\n")
    url = issue_url(f"Error in {title}", body)
    return (f'<p class="report-error"><a href="{html.escape(url)}" rel="nofollow">Report an error on this page</a>'
            f' (opens a GitHub issue; the tag of an item is the four-character code next to it).</p>\n')


def page_chapter(text, chapters):
    """The chapter of a page: the chapter part of the first labelled heading."""
    m = re.search(r'<h[1-6] id="([^"]+)">', text)
    return chapters.get(m.group(1).split(":")[0]) if m else None


class PageDecorator:
    """Adds tags, dependency and Lean badges, status banners and report links to a page."""

    def __init__(self, project, html_dir=None):
        self.label_tag = {label: tag for tag, label in read_tags()}
        self.mathlib = read_mathlib()
        self.chapters = {c.slug: c for c in project.chapters}
        self.uses = dependency_graph(project)
        self.in_graph = set(self.uses).union(*self.uses.values()) if self.uses else set()
        self.html_dir = html_dir or HTML_DIR
        # Bibliography numbers (position in the alphabetical order of the
        # Bibliography page) and years, used by the site's display options.
        bib_page = self.html_dir / "Bibliography.html"
        if not bib_page.exists():
            bib_page = HTML_DIR / "Bibliography.html"
        keys = re.findall(r'<dt[^>]*><a name="([^"]+)"', bib_page.read_text(encoding="utf-8")) if bib_page.exists() else []
        self.bib_num = {key: str(i + 1) for i, key in enumerate(keys)}
        self.bib_year = bibliography_years()

    def bib_cite(self, m):
        num = self.bib_num.get(m.group(1))
        return f'<a href="Bibliography.html#{m.group(1)}" data-num="{num}">' if num else m.group(0)

    def bib_entry(self, m):
        key = m.group(1)
        year = self.bib_year.get(key, "")
        return f'<dt data-year="{year}"><a name="{key}" data-num="{self.bib_num.get(key, "")}">'

    def thm(self, m):
        tag = self.label_tag.get(m.group(2))
        if not tag:
            return m.group(0)
        return (m.group(0) + tag_badge(tag) + (graph_badge(tag) if m.group(2) in self.in_graph else "")
                + (lean_badge(self.mathlib[m.group(2)]) if m.group(2) in self.mathlib else ""))

    def heading(self, m):
        level, label, content = m.group(1), m.group(2), m.group(3)
        tag = self.label_tag.get(label)
        out = f'<h{level} id="{label}">{content}{tag_badge(tag) if tag else ""}</h{level}>'
        chapter = self.chapters.get(label.split(":")[0])
        if level == "1" and chapter and chapter.status != "checked":
            out += (f'\n<p class="status-banner status-{chapter.status}">'
                    f'<strong>{chapter.status.capitalize()}.</strong> {STATUSES[chapter.status]}</p>')
        return out

    def toc_link(self, m):
        chapter = self.chapters.get(m.group(2))
        if m.group(2).startswith("part-") and (self.html_dir / "pdf" / f"{m.group(2)}.pdf").exists():
            return (m.group(1) + f' <a class="part-pdf" href="pdf/{m.group(2)}.pdf" '
                    f'title="PDF of this part, with the numbering of the full book">PDF</a>')
        if not chapter:
            return m.group(1)
        return m.group(1) + f'<span class="status-chip status-{chapter.status}">{chapter.status}</span>'

    def decorate(self, text, name):
        # MathJax does not need the \label inside a numbered equation (plasTeX
        # numbers it), and a copy of the equation in a preview box would
        # define the label twice.
        text = EQ_LABEL_RE.sub("", text)
        text = THM_HEADING_RE.sub(self.thm, text)
        text = HEADING_RE.sub(self.heading, text)
        text = CITE_RE.sub(lambda m: re.sub(r"\s*([\[\],])\s*", r"\1 ", m.group(0))
                           .replace("[ ", "[").replace(" ]", "]").replace("] ", "]"), text)
        text = BIB_CITE_RE.sub(self.bib_cite, text)
        if name == "Bibliography.html":
            text = BIB_DT_RE.sub(self.bib_entry, text)
        if name == "index.html":
            return TOC_LINK_RE.sub(self.toc_link, text)
        chapter = page_chapter(text, self.chapters)
        # Chapter pages show the status under the title; section pages
        # show it above the text.
        if chapter and chapter.status != "checked" and not re.search(r'<h1 id=', text):
            text = text.replace('<article class="main-text">',
                                f'<p class="status-banner status-compact status-{chapter.status}">'
                                f'Chapter {chapter.number}: <strong>{chapter.status}</strong>. '
                                f'{STATUSES[chapter.status]}</p>\n<article class="main-text">', 1)
        title = re.search(r"<title>(.*?)</title>", text, re.S)
        title = html.unescape(re.sub(r"<[^>]+>", "", title.group(1))).strip() if title else name
        return text.replace('<nav class="page-nav"',
                            report_footer(f"{SITE_URL}{name}", title.removesuffix(" - The Math Project"))
                            + '<nav class="page-nav"', 1)


def postprocess_html(project):
    decorator = PageDecorator(project)
    label_tag, uses = decorator.label_tag, decorator.uses
    locations = {}
    search_entries = []

    for path in sorted(HTML_DIR.glob("*.html")):
        text = path.read_text(encoding="utf-8")
        collect_search_entries(project, text, path.name, search_entries)
        text = decorator.decorate(text, path.name)
        path.write_text(text, encoding="utf-8")

        for m in ID_RE.finditer(text):
            if m.group(1) in label_tag:
                locations.setdefault(m.group(1), path.name)

    tag_dir = HTML_DIR / "tag"
    tag_dir.mkdir(exist_ok=True)
    rows = []
    for tag, label in read_tags():
        label = label.removeprefix("alias:")
        page = locations.get(label)
        if page is None:
            continue
        url = f"{page}#{label}"
        (tag_dir / f"{tag}.html").write_text(TAG_PAGE.format(
            tag=tag, url=html.escape("../" + url), label=html.escape(label)), encoding="utf-8")
        rows.append(f'<tr><td><a class="tag" href="tag/{tag}.html">{tag}</a></td>'
                    f'<td><a href="{html.escape(url)}"><code>{html.escape(label)}</code></a></td></tr>')
    (HTML_DIR / "tags.html").write_text(TAGS_PAGE.format(rows="\n".join(rows), count=len(rows)),
                                        encoding="utf-8")
    missing = [label for label in label_tag if label in project.labels and label not in locations]
    if missing:
        print(f"html: {len(missing)} tagged label(s) not found in the website, e.g. {missing[0]}")
    count = write_search_index(project, search_entries, label_tag)
    print(f"html: search index with {count} entries")
    edges = write_dependency_data(project, search_entries, label_tag, uses)
    print(f"html: dependency graph with {edges} edges")
    sections = sorted(p.name for p in HTML_DIR.glob("*-section-*.html")
                      if not p.name.startswith("introduction-")
                      and not p.name.endswith(("-section-introduction.html", "-section-exercises.html")))
    (HTML_DIR / "sections.json").write_text(json.dumps(sections), encoding="utf-8")
    print(f"html: {len(sections)} sections for the random section button")
    version_assets()


ASSET_RE = re.compile(r'"((?:styles|js)/[\w.-]+\.(?:css|js))(?:\?v=\w+)?"')


def version_assets(html_dir=None):
    """Add ?v=<hash of the stylesheets and scripts> to their links in the pages.

    Browsers keep a stylesheet or script with an unchanged URL in their cache, so
    after an update a page could be shown with the old styles; a new version
    string forces them to be fetched again."""
    html_dir = html_dir or HTML_DIR
    digest = hashlib.sha1()
    for path in sorted(list((html_dir / "styles").glob("*.css")) + list((html_dir / "js").glob("*.js"))):
        digest.update(path.read_bytes())
    version = digest.hexdigest()[:10]
    for path in html_dir.glob("*.html"):
        text = path.read_text(encoding="utf-8")
        new = ASSET_RE.sub(lambda m: f'"{m.group(1)}?v={version}"', text)
        if new != text:
            path.write_text(new, encoding="utf-8")


# ---------------------------------------------------------------------------
# Website search index
# ---------------------------------------------------------------------------

SEARCH_KINDS = ["chapter", "section"] + sorted(THEOREM_ENVS)
SEARCH_TEXT_LIMIT = 600
HTML_TAG_RE = re.compile(r"<[^>]+>")
BLOCK_TAG_RE = re.compile(r"</?(?:p|div|li|ol|ul|br|table|tr|td|th|h[1-6])\b[^>]*>")
DIV_RE = re.compile(r"<div\b|</div>")
THM_WRAPPER_RE = re.compile(r'<div class="(\w+)_thmwrapper[^"]*" id="([^"]+)">')
ANY_HEADING_RE = re.compile(r'<h[1-6] id="([^"]+)">(.*?)</h[1-6]>', re.S)
SPAN_RE = r'<span class="{env}_{part}">(.*?)</span>'


def html_to_text(fragment):
    """Plain text of an HTML fragment, keeping formulas as \\( ... \\)."""
    fragment = re.sub(r'<a class="tag"[^>]*>.*?</a>', " ", fragment, flags=re.S)
    fragment = BLOCK_TAG_RE.sub(" ", fragment)
    text = html.unescape(HTML_TAG_RE.sub("", fragment))
    text = text.replace("\\[", "\\(").replace("\\]", "\\)")
    text = re.sub(r"\s+", " ", text)
    return re.sub(r" ([,.;:)])", r"\1", text).strip()


def element_end(text, start):
    """End of the <div> element that starts at position start."""
    depth = 0
    for m in DIV_RE.finditer(text, start):
        depth += -1 if m.group(0) == "</div>" else 1
        if depth == 0:
            return m.end()
    return len(text)


def cut_text(text, limit):
    """Cut text after about limit characters, at a space outside formulas."""
    if len(text) <= limit:
        return text
    depth, i = 0, 0
    while i < len(text):
        two = text[i:i + 2]
        if two == "\\(":
            depth, i = depth + 1, i + 2
            continue
        if two == "\\)":
            depth, i = max(0, depth - 1), i + 2
            continue
        if depth == 0 and i >= limit and text[i] == " ":
            return text[:i]
        i += 1
    return text


def collect_search_entries(project, text, page, entries):
    """Record the chapters, sections and numbered environments of one page.

    Each entry is (position, kind, label, number, name, section label, url, text);
    the section is the closest preceding section heading on the same page."""
    events = []
    for m in ANY_HEADING_RE.finditer(text):
        label = m.group(1)
        info = project.labels.get(label)
        if info is None or not (label == info.chapter or ":section-" in label or ":subsection-" in label):
            continue
        title = html_to_text(m.group(2))
        number, _, name = title.partition(" ")
        kind = "chapter" if label == info.chapter else "section"
        events.append((m.start(), kind, label, number, name, ""))
    for m in THM_WRAPPER_RE.finditer(text):
        env, label = m.group(1), m.group(2)
        if env not in THEOREM_ENVS or label not in project.labels:
            continue
        end = element_end(text, m.start())
        block = text[m.start():end]
        number = re.search(SPAN_RE.format(env=env, part="thmlabel"), block, re.S)
        name = re.search(SPAN_RE.format(env=env, part="thmtitle"), block, re.S)
        content = block.find(f'<div class="{env}_thmcontent">')
        body = block[content:element_end(block, content)] if content != -1 else ""
        events.append((m.start(), env, label,
                       html_to_text(number.group(1)) if number else "",
                       html_to_text(name.group(1)) if name else "",
                       cut_text(html_to_text(body), SEARCH_TEXT_LIMIT)))
    section = None
    for _, kind, label, number, name, body in sorted(events):
        if kind == "section":
            section = label
        entries.append((project.labels[label].position, kind, label, number, name,
                        section if kind != "section" else None, f"{page}#{label}", body))


def write_search_index(project, entries, label_tag):
    """Write search-index.js, the data used by search.html."""
    entries.sort()
    places, place_index = [], {}
    for _, kind, label, number, name, _, url, _ in entries:
        if kind in ("chapter", "section"):
            place_index[label] = len(places)
            places.append([number, name, url])
    items = []
    for _, kind, label, number, name, section, url, body in entries:
        chapter = project.labels[label].chapter
        items.append([SEARCH_KINDS.index(kind), label_tag.get(label, ""), label, number, name,
                      place_index.get(chapter, -1), place_index.get(section, -1), url, body])
    data = {"kinds": SEARCH_KINDS, "places": places, "items": items}
    (HTML_DIR / "search-index.js").write_text(
        "window.MATH_SEARCH_INDEX = " + json.dumps(data, ensure_ascii=False, separators=(",", ":"))
        .replace("\u2028", "\\u2028").replace("\u2029", "\\u2029") + ";\n",
        encoding="utf-8")
    (HTML_DIR / "js").mkdir(exist_ok=True)
    shutil.copy2(ROOT / "web" / "search.js", HTML_DIR / "js" / "search.js")
    (HTML_DIR / "search.html").write_text(SEARCH_PAGE.replace("@MATHJAX_URL@", MATHJAX_URL), encoding="utf-8")
    shutil.copy2(ROOT / "web" / "print.js", HTML_DIR / "js" / "print.js")
    (HTML_DIR / "print.html").write_text(PRINT_PAGE.replace("@MATHJAX_URL@", MATHJAX_URL), encoding="utf-8")
    return len(items)


def write_dependency_data(project, entries, label_tag, uses):
    """Write deps.js, the data used by graph.html, and the page itself."""
    chapter_index = {c.slug: i for i, c in enumerate(project.chapters)}
    kinds = sorted(THEOREM_ENVS)
    pages, page_index = [], {}
    items, item_index = [], {}
    for _, kind, label, number, name, _, url, _ in sorted(entries):
        if kind not in THEOREM_ENVS or label in item_index:
            continue
        page = url.partition("#")[0]
        if page not in page_index:
            page_index[page] = len(pages)
            pages.append(page)
        item_index[label] = len(items)
        items.append([label, label_tag.get(label, ""), kinds.index(kind), number, name,
                      chapter_index.get(project.labels[label].chapter, -1), page_index[page]])
    edges = [[] for _ in items]
    count = 0
    for owner, targets in uses.items():
        if owner not in item_index:
            continue
        edges[item_index[owner]] = sorted(item_index[t] for t in targets if t in item_index)
        count += len(edges[item_index[owner]])
    data = {"kinds": kinds,
            "chapters": [[c.number, c.title, c.slug] for c in project.chapters],
            "pages": pages, "items": items, "uses": edges}
    (HTML_DIR / "deps.js").write_text(
        "window.MATH_DEPS = " + json.dumps(data, ensure_ascii=False, separators=(",", ":"))
        .replace("\u2028", "\\u2028").replace("\u2029", "\\u2029") + ";\n",
        encoding="utf-8")
    shutil.copy2(ROOT / "web" / "graph.js", HTML_DIR / "js" / "graph.js")
    (HTML_DIR / "graph.html").write_text(GRAPH_PAGE.replace("@MATHJAX_URL@", MATHJAX_URL), encoding="utf-8")
    return count


GRAPH_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Dependencies - The Math Project</title>
<script>
  try { var r = document.documentElement, t = localStorage.getItem("math-theme"); if (t === "light" || t === "dark" || t === "auto") r.setAttribute("data-theme-mode", t); if (t === "auto") { var h = new Date().getHours(); t = h >= 20 || h < 7 ? "dark" : "light"; } if (t === "light" || t === "dark") r.setAttribute("data-theme", t); } catch (e) {}
</script>
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  tex2jax: { inlineMath: [["\\\\(", "\\\\)"]], displayMath: [["\\\\[", "\\\\]"]], processEscapes: true, processEnvironments: true },
  TeX: { extensions: ["AMSmath.js", "AMSsymbols.js"], equationNumbers: { autoNumber: "none" } },
  "HTML-CSS": { availableFonts: ["TeX"], imageFont: null },
  skipStartupTypeset: true,
  messageStyle: "none"
});
</script>
<script src="@MATHJAX_URL@"></script>
<link rel="stylesheet" href="styles/theme-math.css" />
</head>
<body class="graph-page">
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <a class="site-title" href="index.html">The Math Project</a>
  <form class="site-search" id="graph-form" action="graph.html" method="get">
    <label class="visually-hidden" for="graph-input">Show the dependencies of a tag</label>
    <input id="graph-input" name="tag" type="search" placeholder="Tag, e.g. 02WM" autocomplete="off" spellcheck="false" />
    <button type="submit">Show</button>
  </form>
  <a class="header-link" href="search.html">Search</a>
  <a class="header-link" href="tags.html">Tags</a>
</header>
<main class="content graph-content" id="main">
<h1 id="graph-title">Dependencies</h1>
<p class="graph-status" id="graph-status" aria-live="polite">Loading the dependency data&hellip;</p>
<div id="graph-body"></div>
<noscript><p>This page needs JavaScript. The <a href="tags.html">list of tags</a> works without it.</p></noscript>
</main>
<script src="deps.js"></script>
<script src="js/graph.js"></script>
</body>
</html>
"""


PRINT_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Chapter - The Math Project</title>
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  tex2jax: { inlineMath: [["\\\\(", "\\\\)"]], displayMath: [["\\\\[", "\\\\]"]], processEscapes: true, processEnvironments: true },
  TeX: { extensions: ["AMSmath.js", "AMSsymbols.js"], equationNumbers: { autoNumber: "none" } },
  "HTML-CSS": { availableFonts: ["TeX"], imageFont: null },
  skipStartupTypeset: true,
  messageStyle: "none"
});
</script>
<script src="@MATHJAX_URL@"></script>
<link rel="stylesheet" href="styles/theme-math.css" />
</head>
<body class="print-page" data-theme="light">
<div class="print-toolbar">
  <a href="index.html">The Math Project</a>
  <span id="print-status" aria-live="polite">Loading the chapter&hellip;</span>
  <button id="print-button" type="button" hidden>Print or save as PDF</button>
</div>
<main class="content print-content">
<article class="main-text" id="print-body"></article>
</main>
<noscript><p>This page needs JavaScript. The PDF of the whole book is <a href="book.pdf">here</a>.</p></noscript>
<script src="js/print.js"></script>
</body>
</html>
"""


SEARCH_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Search - The Math Project</title>
<script>
  try { var r = document.documentElement, t = localStorage.getItem("math-theme"); if (t === "light" || t === "dark" || t === "auto") r.setAttribute("data-theme-mode", t); if (t === "auto") { var h = new Date().getHours(); t = h >= 20 || h < 7 ? "dark" : "light"; } if (t === "light" || t === "dark") r.setAttribute("data-theme", t); } catch (e) {}
</script>
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  tex2jax: { inlineMath: [["\\\\(", "\\\\)"]], displayMath: [["\\\\[", "\\\\]"]], processEscapes: true },
  TeX: { extensions: ["AMSmath.js", "AMSsymbols.js"] },
  "HTML-CSS": { availableFonts: ["TeX"], imageFont: null },
  skipStartupTypeset: true,
  messageStyle: "none"
});
</script>
<script src="@MATHJAX_URL@"></script>
<link rel="stylesheet" href="styles/theme-math.css" />
</head>
<body class="search-page">
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <a class="site-title" href="index.html">The Math Project</a>
  <a class="header-link" href="tags.html">Tags</a>
  <a class="header-link" href="book.pdf">PDF</a>
</header>
<main class="content search-content" id="main">
<h1>Search</h1>
<form class="search-form" id="search-page-form" action="search.html" method="get" role="search">
  <label class="visually-hidden" for="search-page-input">Search the statements of the project</label>
  <input id="search-page-input" name="q" type="search" autocomplete="off" spellcheck="false"
         placeholder="For example: Hodge decomposition, central limit theorem, 02B9" />
  <button type="submit">Search</button>
</form>
<div class="search-filters" id="search-filters" role="group" aria-label="Kind of result"></div>
<p class="search-status" id="search-status" aria-live="polite">Loading the index&hellip;</p>
<ol class="search-results" id="search-results"></ol>
<button class="search-more" id="search-more" type="button" hidden>Show more results</button>
<p class="search-help">The search looks for all the words you type in the statements, names and labels of the
chapters, sections and numbered items of the project; put several words in quotes to search for them as a phrase.
A four-character tag, such as <code>02B9</code>, or a label, such as <code>lefschetz-11:theorem-kahler</code>, finds
that item directly. Only the beginning of each statement is indexed, and proofs are not.</p>
<noscript><p>The search needs JavaScript. The <a href="tags.html">list of tags</a> and the
<a href="index.html">table of contents</a> work without it.</p></noscript>
</main>
<script src="search-index.js"></script>
<script src="js/search.js"></script>
</body>
</html>
"""


TAG_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>Tag {tag}</title>
<meta http-equiv="refresh" content="0; url={url}" />
<link rel="canonical" href="{url}" />
</head>
<body>
<p>Tag {tag} refers to <a href="{url}">{label}</a>.</p>
</body>
</html>
"""

TAGS_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Tags - The Math Project</title>
<link rel="stylesheet" href="styles/theme-math.css" />
</head>
<body class="tags-page">
<header class="site-header">
  <a class="site-title" href="index.html">The Math Project</a>
  <form class="site-search" action="search.html" method="get" role="search">
    <label class="visually-hidden" for="search-input">Search the project</label>
    <input id="search-input" name="q" type="search" placeholder="Search or tag" autocomplete="off" spellcheck="false" />
    <button type="submit">Search</button>
  </form>
</header>
<main class="content tags-content">
<h1>Tags</h1>
<p>Every labelled item of the project has a permanent tag. The page
<code>tag/XXXX.html</code> always leads to the item with tag <code>XXXX</code>,
even if chapters are renumbered. There are {count} tags.</p>
<table class="tags-table">
<thead><tr><th>Tag</th><th>Label</th></tr></thead>
<tbody>
{rows}
</tbody>
</table>
</main>
</body>
</html>
"""


def command_pages(args):
    """Record output/html as a new commit on the gh-pages branch, without checking it out.

    GitHub Pages then serves that branch; push it with 'git push origin gh-pages'."""
    if not (HTML_DIR / "index.html").exists():
        print("pages: build the website first (python make.py html)")
        return False
    git_dir = ROOT / ".git"
    index = git_dir / "pages-index"
    env = dict(os.environ, GIT_INDEX_FILE=str(index))

    def git(*arguments, check=True):
        result = subprocess.run(["git", f"--git-dir={git_dir}", f"--work-tree={HTML_DIR}", *arguments],
                                cwd=HTML_DIR, env=env, capture_output=True, text=True)
        if check and result.returncode != 0:
            raise RuntimeError(result.stderr.strip())
        return result.stdout.strip()

    # GitHub Pages must serve the files as they are, without running Jekyll.
    (HTML_DIR / ".nojekyll").write_text("", encoding="utf-8")
    if index.exists():
        index.unlink()
    try:
        git("add", "--all", "--force", ".")
        # plasTeX's image cache and the local marker are not part of the website.
        git("rm", "-r", "--cached", "--quiet", "--ignore-unmatch", ".cache", GENERATED_MARKER)
        tree = git("write-tree")
        parent = git("rev-parse", "--verify", "--quiet", "refs/heads/gh-pages", check=False)
        if parent and git("rev-parse", parent + "^{tree}") == tree:
            print("pages: gh-pages already contains this website")
            return True
        source = git("rev-parse", "--short", "HEAD")
        message = f"Website built from {source}"
        commit = git("commit-tree", tree, *(["-p", parent] if parent else []), "-m", message)
        git("update-ref", "refs/heads/gh-pages", commit)
    except RuntimeError as error:
        print(f"pages: git failed: {error}")
        return False
    finally:
        if index.exists():
            index.unlink()
    print(f"pages: gh-pages is now {commit[:7]}; publish it with 'git push origin gh-pages'")
    return True


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")
    parser = argparse.ArgumentParser(description="Build and consistency tool for the Math Project.")
    sub = parser.add_subparsers(dest="command", required=True)
    for name, func, help_text in [
        ("check", command_check, "check labels, references and tags"),
        ("tags", command_tags, "assign tags to new labels"),
        ("status", command_status, "show the status of every chapter"),
        ("pdf", command_pdf, "build the PDF"),
        ("html", command_html, "build the website"),
        ("preview", command_preview, "build the website pages of some chapters only"),
        ("pdf-parts", command_pdf_parts, "build one PDF per part (after a full PDF build)"),
        ("all", command_all, "build the PDF, the PDFs of the parts and the website"),
        ("serve", command_serve, "serve the website locally"),
        ("pages", command_pages, "commit the built website to the gh-pages branch"),
        ("lean", command_lean, "check the Mathlib names in web/mathlib.txt online"),
    ]:
        p = sub.add_parser(name, help=help_text)
        p.set_defaults(func=func)
        if name == "preview":
            p.add_argument("chapters", nargs="+", help="slugs of the chapters")
        if name == "pdf-parts":
            p.add_argument("parts", nargs="*", help="labels of the parts, e.g. part-algebra (default: all)")
        if name in ("pdf", "pdf-parts", "html", "all", "preview"):
            p.add_argument("--force", action="store_true", help="build even if the check finds errors")
        if name == "serve":
            p.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    sys.exit(0 if args.func(args) else 1)


if __name__ == "__main__":
    main()
