# Plan of The Math Project

The goal: all of mathematics, at a good level, with complete proofs, written
slowly (motivation, examples, counterexamples, exercises with solutions), in
one strict logical order. The starting material is the 77 chapters copied
from The Hodge Project on 2026-11-05 (about 1.5k PDF pages); the expected size
is about ten times that. Work through the phases in order, but new parts can
be started as soon as phase 0 is done. Tick items off (`[x]`) and move them to
Done with a short summary.

## Phase 0: infrastructure (first)

- [ ] **Identity.** Rewrite `chapters/introduction.tex` for the new scope:
  what the project is, how it is organised, and a reading guide with several
  reading paths (the Hodge conjecture is one of them; add probability, PDE,
  numerical analysis, ... as their parts appear). Check the site header, home
  page, README and PDF title page.
- [ ] **GitHub repository.** Ask the user for the name (suggestion:
  `math-project`) and visibility, then create it and push `main`.
- [ ] **Build in the cloud.** A GitHub Actions workflow that, on every push to
  `main`, installs TeX Live (with `latexmk`, `dvisvgm`, `tikz-cd`) and plasTeX,
  runs `python make.py check` and `python make.py all`, and deploys
  `output/html` to GitHub Pages. Then publishing is just `git push`. Ask the
  user before enabling it.
- [ ] **Fast preview.** `python make.py preview <chapter>`: build the HTML of
  one chapter only, resolving references to other chapters from the last full
  build, so that writing does not need a 25-minute build.
- [ ] **PDFs per part** in addition to the full book (the full PDF will become
  very large).
- [ ] **Report an error.** A link on every tag page that opens a GitHub issue
  prefilled with the tag, and the chapter status shown clearly on every page.
- [ ] **Organisation of `book.tex`.** Insert the new parts below at the place
  their prerequisites require.

## Phase 1: new parts (one at a time, each chapter complete before the next)

Each new chapter: Prerequisites line, introduction, slow sections, examples,
counterexamples, exercises with solutions, citations for quoted results.

- [ ] **Discrete mathematics** (after Algebra): `combinatorics` (counting,
  binomial identities, inclusion–exclusion, pigeonhole, double counting,
  partitions), `generating-functions` (formal power series, recurrences,
  Catalan numbers, exponential generating functions, Lagrange inversion),
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
