# Plan of The Math Project

The goal: all of mathematics, at a good level, with complete proofs, written
slowly (motivation, examples, counterexamples, exercises with solutions), in
one strict logical order. The starting material is the 77 chapters copied
from The Hodge Project on 2026-11-05 (about 1.5k PDF pages); the expected size
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
