# The Math Project

A Stacks-project-style reference, written in LaTeX, that develops mathematics
with complete proofs, slowly and in a strict logical order, aiming to cover
*all* of it at a good level: foundations, algebra, topology, analysis,
geometry, number theory, discrete mathematics, probability and statistics,
differential equations and dynamics, numerical analysis, optimisation, game
theory, and research-level topics (Hodge theory, algebraic geometry, ...).
One source produces a PDF (pdflatex) and a website (plasTeX).
Book language: English. The user writes in Italian; answer in Italian.

The project was started on 2026-11-05 as a copy of "The Hodge Project"
(`C:\Users\Vittorio\Desktop\gerby-notes`, published at
https://lufranovittorio.github.io/Appunti_Matematica/). That project goes on
separately: never modify it from here. The 77 copied chapters are starting
material, free to be reorganised, split, merged and expanded. The plan is in
`TODO.md`; work through it and keep it updated (move finished items to Done).

## How the user wants the book written

- **Slowly.** Expand as much as possible, but never rush definitions or
  steps: motivate every definition, give examples right after it, name the
  steps of proofs, add counterexamples showing why each hypothesis is needed,
  and exercises with solutions. Prefer fewer topics treated fully over many
  compressed ones.
- **Add on own initiative.** Sections should contain the well-known results a
  curious reader would look for around a topic (e.g. number theory: Gaussian
  primes, Heegner numbers, Euler's n²+n+41), not only the core. Say in the
  reply what was added beyond the request.
- **Explicit notation.** When a definition introduces a structure, name the
  operation symbols in the definition and add a Notation item saying which
  conventions are used (multiplicative vs additive, when symbols are omitted).
- **Questions go into the book.** When the user asks a mathematical question,
  answer it in chat and also add the answer (remark, example, proposition) in
  the right place.
- **The user does not want to do things manually**: run the checks, builds
  and publication yourself. Ask first only for outward-facing steps the user
  has not approved yet (creating the GitHub repository, the first push,
  changing the publication setup).

## Layout

- `book.tex` — master file. The order of `\part` / `\include` lines is the
  logical order of the whole project.
- `preamble.tex` — packages and numbered environments. `macros.tex` — math macros.
- `chapters/<slug>.tex` — one file per chapter. The slug is permanent.
- `tags/tags` — permanent tags, one `TAG,label` per line. Append-only.
- `make.py` — checker and build tool (see README.md).
- `math-project.bib` — bibliography (style amsalpha).
- `web/Themes/math/` — plasTeX theme: layouts, `styles/theme-math.css`, `js/site.js`.
  Every `.js` file in the theme is loaded on every page, so page-specific
  scripts live elsewhere: `web/search.js` drives `search.html`, which
  `make.py html` writes together with the index `search-index.js`; likewise
  `web/graph.js` drives `graph.html`, the dependency graph built from the
  `\ref`s inside statements and proofs (data in `deps.js`).
  `web/mathlib.txt` lists the site-only "Lean" badges (only Mathlib names
  verified in the Mathlib documentation; `python make.py lean` checks them).
- `output/` — generated; never edit by hand.

## Rules for writing chapters

- **No forward references.** A proof may only use material that appears
  earlier in `book.tex`. Outside proofs, text may point forward within the same
  chapter (e.g. an introduction announcing the main theorem) and to later
  chapters as a whole, but not to results of later chapters. Examples,
  counterexamples, remarks and exercises may *mention* later notions
  informally. Only `chapters/introduction.tex` may refer forward freely.
  `make.py check` enforces this (errors inside proofs and in Prerequisites
  lines, warnings otherwise). Solutions of exercises count as proofs.
- **Citations**: `\cite{key}` / `\cite[Theorem 2.3]{key}` with keys from
  `math-project.bib`. Only add entries whose details are certain. Results
  quoted without proof must cite a source.
- **Every result is proved.** Use `\begin{proof}` for complete proofs,
  `\begin{proof}[Sketch of proof]` when verifications are omitted (name them),
  and no proof only for results quoted from the literature (give the reference).
- **Numbered environments**: definition, theorem, proposition, lemma,
  corollary, conjecture, example, counterexample, exercise, notation, remark.
  Exercises may be followed by `\begin{solution}`. All share one counter within
  the section, so every numbered environment must be inside a `\section`.
- **Labels**: chapter `\label{<slug>}`; everything else
  `\label{<slug>:<type>-<name>}` where `<type>` is the environment name,
  `section`/`subsection`, or `equation`; `<name>` is lower-case words joined by
  hyphens. Put section labels on the same line as `\section{...}` and
  environment labels right after `\begin{...}`. Every numbered environment
  gets a label (so it gets a tag).
- **Tags** are assigned by `make.py` in label order and never change. If a label
  is renamed, edit its line in `tags/tags`; never delete or reuse a tag.
- **Chapter status**: `\chapterstatus{planned|draft|complete|checked}` right
  after `\chapter`. Planned chapters contain a summary, a Prerequisites line
  (`\noindent\textbf{Prerequisites.} Chapter~\ref{slug} (Title), ...`) and a
  Planned contents list. Only a human reader may set a chapter to `checked`.
- **Reading paths** are described only in the introduction's reading guide
  (the Hodge conjecture is one path among several); describe every new path
  (probability, PDE, ...) there. Chapters have no per-chapter path paragraph
  (the old "On the way to the Hodge conjecture" paragraphs were removed on
  2026-11-05 at the user's request; do not add them back).
- **The Hodge Project**: whenever the book, README or site mentions it, link
  it: `\href{https://lufranovittorio.github.io/Appunti_Matematica/}{The Hodge Project}`
  (source: https://github.com/lufranovittorio/Appunti_Matematica).
- **Comprehensive.** Chapters marked complete are not finished for good: when
  a subject deserves it, rebuild or split an existing chapter to make it
  bigger, or reorganise chapters, rather than only adding new ones.
- **Math that works on both outputs**: plasTeX expands macros from
  `macros.tex` itself, and MathJax 2.7.9 renders the result. Stick to amsmath /
  amssymb commands that MathJax supports; do not add packages without testing
  the HTML build. `mathtools` and `amscd` are not supported.
  Because plasTeX expands the macros first, an accent needs braces around a
  macro argument: write `\bar{\QQ}`, not `\bar\QQ` (MathJax would see
  `\bar\mathbb {Q}`); `make.py check` reports this. Do not use `align*`:
  plasTeX treats its body as text and turns `''` into a curly quote. Write
  `\[\begin{aligned} ... \end{aligned}\]` instead, and write primes as
  `^{\prime}` (plasTeX converts `'` inside `aligned`; `^{\prime}` is safe
  everywhere).
- **Numbered equations**: when a formula is referred to later, write
  `\begin{equation}\label{<slug>:equation-<name>} ... \end{equation}` and refer
  to it with `\eqref{...}`; equations are numbered within chapters, (5.1), and
  the website previews them on hover. Never put `\label` or `\tag` inside
  `\[ \]`: plasTeX attaches such a label to the wrong object.
- **Diagrams**: use `tikz-cd`, *outside* math mode, wrapped in `center`:
  `\begin{center}\begin{tikzcd} ... \end{tikzcd}\end{center}`. plasTeX turns it
  into an SVG image. A `tikzcd` inside `\[ \]` is not rendered on the website.
- New chapters: add the file, add `\include{chapters/<slug>}` in the right
  place in `book.tex`, and run `python make.py check`.

## Working method

- `python make.py check` before and after any change to the sources, then
  `python make.py tags` for new labels, then `check` again.
- `python make.py html` / `pdf` / `all`; `python make.py serve` to view the
  site (`.claude/launch.json` has the server `math-site`, port 8000). A full
  build takes about 25 minutes: run it in the background, never edit the
  sources while it runs, and wait with a loop on the log (delete the old log
  first, so that a stale "exit=" line is not matched).
- While writing a chapter, use `python make.py preview <slug>` (about 20
  seconds; pages in `output/html/preview/`, served at
  http://localhost:8000/preview/<slug>.html) instead of a full build; it needs
  `book.paux` from a full `html` build. `python make.py pdf-parts [part-...]`
  rebuilds part PDFs after a full `pdf` build.
- Publishing is `git push` to `main`: the GitHub Actions workflow builds and
  deploys to https://lufranovittorio.github.io/math-project/ (about 15
  minutes; check with `gh run list`). No local full build is needed to publish.
- After a build or preview, check the changed pages in the browser: zero MathJax errors
  (`.MathJax_Error`, `merror`), no `??` from unresolved references, and no
  display wider than the text column (736 px). Find the
  page of a label with `grep -l 'id="<label>"' output/html/*-section-*.html`.
- The website must use MathJax **2.7.9** (HTML-CSS output), because the user
  wants formulas to be selectable text. Do not upgrade to MathJax 3/4.
- Write `.tex` files with the file-writing tools (Write/Edit), or with Python
  scripts that are themselves written with Write (read bytes, normalise CRLF,
  assert that each anchor occurs once, splice, restore the newline style).
  Never use shell heredocs for LaTeX: the shell can silently turn `\\` into
  `\`, and `\r`, `\b`, `\n` in `\ref`, `\bar`, `\notin` become control
  characters.
- When reordering existing text, verify that nothing was lost by comparing
  the sorted lines of the old and new file.
- Never put private API keys, tokens or passwords in the repository.
