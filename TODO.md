# Plan of The Math Project

The goal: all of mathematics, at a good level, with complete proofs, written
slowly (motivation, examples, counterexamples, exercises with solutions), in
one strict logical order. The starting material is the 77 chapters copied
from [The Hodge Project](https://lufranovittorio.github.io/Appunti_Matematica/) on 2026-11-05 (about 1.5k PDF pages); the expected size
is about ten times that. Work through the phases in order, but new parts can
be started as soon as phase 0 is done. Tick items off (`[x]`) and move them to
Done with a short summary.

## Phase 0: infrastructure (first)

All done (see Done). Possible later improvements:

- [ ] A per-item "report" link (next to each tag badge) in `web/Themes/math/js/site.js`,
  prefilling the issue with the tag; the page footer already does it per page.
- [ ] In the part PDFs, make references to other parts links to the website
  (now they are printed with the right number but are not links).

## Phase 1: new parts (one at a time, each chapter complete before the next)

Each new chapter: Prerequisites line, introduction, slow sections, examples,
counterexamples, exercises with solutions, citations for quoted results.

- [ ] **Discrete mathematics** (after Algebra): ~~`combinatorics`~~ (done),
  ~~`generating-functions`~~ (done),
  `graph-theory` (trees, Euler and Hamilton, matchings and Hall, Menger,
  colourings, planarity and Euler's formula, Ramsey theory, spectral graph
  theory), later `probabilistic-method`.
- [ ] **Probability and statistics** (after Analysis; builds on
  `measure-theory`): `probability` (probability spaces, random variables,
  independence, Borel–Cantelli, laws of large numbers, characteristic
  functions, weak convergence, central limit theorem, large deviations),
  `martingales` (conditional expectation, martingales, stopping times,
  convergence theorems), `markov-chains`, `brownian-motion`,
  `stochastic-calculus` (Itô integral, Itô's formula, SDEs), `statistics`
  (estimators, sufficiency, Cramér–Rao, maximum likelihood, hypothesis tests,
  linear regression, Bayesian inference).
- [ ] **Differential equations and dynamics** (after Analysis):
  `ordinary-differential-equations` (Picard–Lindelöf, Peano, dependence on
  data, linear systems and the matrix exponential, stability, Lyapunov,
  Sturm–Liouville), `dynamical-systems` (flows, Poincaré–Bendixson, hyperbolic
  fixed points, Hartman–Grobman, stable manifolds, bifurcations, chaos),
  `ergodic-theory` (Poincaré recurrence, Birkhoff and von Neumann ergodic
  theorems, mixing, entropy), `sobolev-spaces`, `elliptic-pde` (Laplace and
  Poisson, maximum principles, Lax–Milgram, regularity), `evolution-equations`
  (heat and wave equations, semigroups, energy methods, hyperbolic systems),
  `calculus-of-variations` (Euler–Lagrange, direct method, Noether).
- [ ] **Numerical analysis** (after Differential equations): `numerical-analysis`
  (floating point and conditioning, interpolation, quadrature, root finding),
  `numerical-linear-algebra` (LU, QR, SVD, iterative methods, eigenvalue
  algorithms), `numerical-ode` (Runge–Kutta, multistep methods, stiffness),
  `numerical-pde` (finite differences, finite elements and Céa's lemma,
  stability and the Lax equivalence theorem).
- [ ] **Optimisation and game theory** (after Topology and Analysis):
  `convex-analysis` (convex sets and functions, separation, duality, Fenchel
  conjugates), `linear-programming` (simplex method, duality, Farkas),
  `nonlinear-optimisation` (Lagrange multipliers, KKT, gradient and Newton
  methods), `game-theory` (games in normal form, von Neumann's minimax
  theorem, Nash equilibria via Brouwer and Kakutani, extensive games and
  backward induction, cooperative games and the Shapley value, auctions and
  mechanism design).
- [ ] **More advanced topics**, extending the existing parts:
  `analytic-number-theory` (Dirichlet series, prime number theorem, Dirichlet's
  theorem), `algebraic-number-theory`, `modular-forms`, `harmonic-analysis`,
  `operator-algebras`, `k-theory`, `information-theory`,
  `computability-and-complexity`, more algebraic geometry in the style of the
  Stacks project.

## Phase 2: deepen the existing chapters

- [ ] The chapters of the Hodge core are much thinner (about 200–400 lines)
  than the foundations (2000–4400 lines): `sheaves`, `sheaf-cohomology`,
  `kahler`, `hodge-theorem`, `hodge-structures`, `lefschetz-11`,
  `cycle-class`, `hodge-conjecture`, `vhs`, `mumford-tate`, `known-cases`,
  `failures`, ... Bring them to the same density: computed examples (curves,
  complex tori, hypersurfaces, projective spaces), counterexamples, exercises.
- [ ] Replace the remaining `Sketch of proof` by complete proofs where
  feasible (`riemannian-geometry` has 5; `schemes`, `smooth-manifolds`,
  `symplectic-geometry`, `mixed-hodge-structures`, `absolute-hodge`,
  `cycle-class`, `tate-conjecture` have 2 each).
- [ ] Finish `deformations` (status `draft`).

## Order of work (user, 2026-11-05)

1. **Number theory** (Part Number Theory, rebuilt into 12 chapters):
   ~~`prime-numbers`~~ (done), `continued-fractions`, `diophantine-equations`,
   `p-adic-numbers`, `analytic-number-theory`, `algebraic-number-theory`
   (number fields, Dedekind domains, decomposition of primes),
   `geometry-of-numbers`, `cyclotomic-fields`, `local-fields`,
   `class-field-theory`, `modular-forms`, `elliptic-curves-arithmetic`; also
   revisit the elementary `number-theory` chapter (Algebra part).
2. **Differential geometry** (rebuild the part, thinnest chapters first).
3. **Measure theory**.
4. **Algebraic geometry**.
5. Then free choice. Discrete mathematics is paused: the first part of
   `graph-theory` is drafted in `drafts/graph-theory-part1.tex` (introduction,
   graphs, degrees, Havel–Hakimi, walks, distance, Moore bound, bipartite
   graphs; fix the Petersen sentence about common neighbours before use);
   the plan is to split graph theory into `graph-theory`, `planar-graphs`,
   `extremal-graph-theory`, `spectral-graph-theory`.

## Comprehensive rebuild of the existing chapters (user request, 2026-11-05)

"Complete" is not final: chapters below the depth of the Stacks project are to
be rebuilt (rewritten slowly, enlarged, split into several chapters, or
merged and reorganised), not only patched. Work on them alternates with the
new parts. Order: the foundations and algebra chapters that the new parts use
first, then the thinnest chapters. Thinnest written chapters (lines, at
2026-11-05): failures 172, etale-cohomology 188, known-cases 194,
lefschetz-11 197, cycle-class 205, intermediate-jacobians 207, vhs 209,
mumford-tate 214, cohomology-operations 235, hodge-conjecture 244,
dolbeault 247, calabi-yau 249, tate-conjecture 260, gaga 266,
abelian-varieties 273, hodge-structures 280, index-theorems 283,
algebraic-groups 285, intersection-theory 293, curves 297,
spectral-sequences 300 (then everything below about 800 lines).

- [ ] For each: list what the Stacks project (or the standard reference) covers,
  plan the new chapter(s), rewrite, keep every existing label (tags are
  permanent; a removed result keeps its tag by staying, possibly as a remark).
- [x] 2026-11-05: `prime-numbers` (complete, 860 lines): proofs of the
  infinitude of primes (Euclid, Goldbach, Euler, Erdős, Fürstenberg), primes in
  progressions (4k+3, 6k+5, 1 mod n via cyclotomic polynomials, all classes
  mod 8), Mersenne and Fermat primes (Lucas–Lehmer, Pépin, Euler's 641),
  Chebyshev's bounds, Bertrand (Erdős), Abel summation and Mertens' three
  theorems, Chebyshev's limit theorem, Korselt, Miller–Rabin with proof of the
  1/2 bound, Lucas, AKS identity, Pollard p−1, open problems; 14 exercises.
- [x] 2026-11-05: removed the paragraphs "On the way to the Hodge conjecture"
  from all chapters (the route stays in the introduction); The Hodge Project
  is linked wherever it is mentioned.

## Carried over from The Hodge Project (still open)

- [ ] `number-theory`: Bertrand's postulate (Erdős's proof via central
  binomial coefficients) and estimates of Chebyshev type; continued fractions
  and Pell's equation, $p$-adic numbers, Dirichlet characters.
- [ ] `fields`: constructible numbers as a section (ruler and compass
  constructions, the field of constructible numbers, Wantzel: doubling the
  cube and trisecting the angle are impossible, Gauss–Wantzel for regular
  polygons, the $17$-gon), expanding `fields:exercise-constructible`.
- [ ] Thin chapters to expand: `sheaves`, `complex-analysis`,
  `commutative-algebra`, second half of `singular-homology`.
- [ ] Lean links (`web/mathlib.txt`): verified names exist for
  `general-topology` and `measure-theory`; extend to other chapters, only with
  names checked in the Mathlib documentation.
- [ ] Slower rewrite, chapter by chapter, of the parts not yet rewritten
  (`characteristic-classes` onwards in differential geometry, then the other
  parts).

## Done

- [x] 2026-11-05: project created as a copy of The Hodge Project (chapters,
  tags, bibliography, `make.py`, website theme), renamed to The Math Project.
- [x] 2026-11-05: **Identity.** New introduction (aim, history, organisation
  with the new parts, three ways to read, reading paths for every subject, the
  Stacks standard of depth); bibliography header renamed.
- [x] 2026-11-05: **GitHub repository** `lufranovittorio/math-project` (public),
  `main` pushed.
- [x] 2026-11-05: **Build in the cloud.** `.github/workflows/build.yml`: on every
  push to `main` it installs TeX Live and plasTeX, runs `make.py check` and
  `make.py all`, and deploys `output/html` to GitHub Pages
  (https://lufranovittorio.github.io/math-project/). Publishing is `git push`.
- [x] 2026-11-05: **Organisation of `book.tex`.** New parts Discrete
  Mathematics, Probability and Statistics, Differential Equations and
  Dynamics, Numerical Analysis, Optimisation and Game Theory, Number Theory,
  and 33 planned chapters (summary, prerequisites, planned contents).
- [x] 2026-11-05: **Fast preview.** `python make.py preview <chapter>...`
  builds the pages of some chapters in about 20 seconds into
  `output/html/preview/`, with references to other chapters resolved from
  `book.paux` of the last full build and the whole bibliography.
- [x] 2026-11-05: **PDFs per part.** `python make.py pdf-parts [part-...]` builds
  one PDF per part with the numbering of the full book (labels of the other
  parts from the aux files of the full build); `make.py all` builds them and the
  table of contents of the website links them.
- [x] 2026-11-05: **Report an error and status.** Every page ends with a link that
  opens a prefilled GitHub issue, and every chapter and section page shows the
  status of its chapter under the title.
- [x] 2026-11-05: `combinatorics` (complete, 1900 lines): basic rules, binomial
  coefficients (also modulo primes: Lucas, Legendre, Kummer), multisets and the
  twelvefold way, inclusion–exclusion, Möbius inversion on posets, pigeonhole
  (Dirichlet, Erdős–Szekeres, R(3,3)), double counting and extremal set theory
  (LYM, Sperner, Erdős–Ko–Rado), Stirling, Bell, Lah and Eulerian numbers,
  partitions, Burnside and Pólya; 18 exercises with solutions.
- [x] 2026-11-05: `generating-functions` (complete, 1800 lines): formal power
  series (summable families, infinite products, composition and compositional
  inverse, derivative, exp/log, Newton's binomial series), rational generating
  functions and linear recurrences (partial fractions, Binet, transfer matrix),
  Catalan numbers (binary trees and other interpretations, parity), partitions
  (Euler, Gaussian binomials and subspaces of F_q^n, pentagonal theorem with
  Franklin's involution, Jacobi triple product), exponential generating
  functions and the exponential formula (set partitions, cycles, involutions,
  connected graphs, Bernoulli numbers and Faulhaber), Lagrange inversion via
  residues, the cycle lemma, Fuss–Catalan, Cayley's formula (two proofs),
  elementary estimates; 16 exercises with solutions.
