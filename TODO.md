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
  ~~`analytic-number-theory`~~ (done 2026-11-06), `algebraic-number-theory`, `modular-forms`, `harmonic-analysis`,
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

Update (user, 2026-11-06): after `p-adic-numbers`, first rebuild measure
theory / geometric measure theory and the differential geometry part, then
resume the number theory list below where it was left (`diophantine-equations`).
Everything in order, without repetition, slowly, with notions that belong
together in one place.

1. **Number theory**, in three parts since 2026-11-05 (user: put new chapters
   in an organised part of their own, in the logical order):
   - Part *Number Theory* (after Probability, uses algebra and analysis only):
     ~~`prime-numbers`~~ (done), ~~`continued-fractions`~~ (done),
     ~~`geometry-of-numbers`~~ (done), ~~`analytic-number-theory`~~ (done),
     ~~`p-adic-numbers`~~ (done 2026-11-06),
     `diophantine-equations` (uses all of the part: three squares via
     Hasse–Minkowski, Skolem, Thue).
   - Part *Algebraic Number Theory*: `algebraic-number-theory` (number fields,
     Dedekind domains, decomposition of primes), `class-groups-and-units`
     (new: Minkowski bound, class number, Dirichlet's unit theorem, class
     number formula), `cyclotomic-fields`, `local-fields`, `class-field-theory`.
   - Part *Arithmetic Geometry* (after Algebraic Geometry, needs curves):
     `modular-forms`, `elliptic-curves-arithmetic`.
   Also revisit the elementary `number-theory` chapter (Algebra part; it stays
   there because combinatorics and later algebra use it).
2. **Differential geometry** (rebuild the part, thinnest chapters first).
3. **Measure theory**. Step 1 done 2026-11-06: split into its own part *Real
   Analysis and Measure Theory* (`measure-theory`, `lebesgue-differentiation`,
   `radon-measures`, `geometric-measure-theory`). Step 2, next (user,
   2026-11-06: "not just split, everything must be comprehensive, a nice
   reading of basically everything", as many chapters and sections as the
   Stacks project): grow the part into a complete treatise, slowly, e.g.
   - `measure-theory`: ~~π-λ (Dynkin), Carathéodory–Hahn extension,
     Lebesgue–Stieltjes measures, completion~~ (done 2026-11-07, new section
     *Extension and completion of measures*); still to do: rewrite the
     compressed early sections slowly (σ-algebras with more examples, the
     proof of Hölder with all cases, measurable functions), Bernstein sets,
     image measures and the abstract change of variables;
   - ~~new `signed-measures`~~ (done 2026-11-07; Dunford–Pettis left for
     `functional-analysis`, where weak topologies are);
   - `lebesgue-differentiation`: functions of bounded variation, Banach–Zarecki,
     Lebesgue points, unify the doubling maximal inequality with Hardy–Littlewood;
   - `radon-measures`: Besicovitch covering theorem with proof, Prokhorov,
     Haar measure (existence and uniqueness);
   - `geometric-measure-theory`: Frostman's lemma, Brunn–Minkowski and the
     isoperimetric inequality, Steiner symmetrisation, Marstrand projection,
     Kakeya/Besicovitch sets, rectifiability in depth; perhaps split into
     `hausdorff-measures`, `fractals`, `area-coarea`, `rectifiability`;
   - move Borel–Cantelli/independence into `probability` when it is written.
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
- [x] 2026-11-05: `continued-fractions` (complete, about 1700 lines, 131 tags):
  finite and infinite continued fractions, matrices, Lamé; the expansions of
  $\varphi$, $\sqrt2$, $\pi$ and $e$ (Cohn's proof); best approximations
  (Lagrange, Legendre, Vahlen, Hurwitz with the optimal $\sqrt5$), Markov
  spectrum (remark), Serret's theorem on equivalent numbers, badly
  approximable numbers; Farey sequences and Ford circles; quadratic
  irrationals (Euler, Lagrange, Galois, the palindrome of $\sqrt d$, the
  integer algorithm); Pell's equation with the group of units, $x^2 - dy^2 = N$
  for $|N| < \sqrt d$; Liouville, Liouville numbers (Baire, measure zero),
  symmetric polynomials, transcendence of $e$ and $\pi$ with full proofs,
  irrationality exponent ($\mu(e) = 2$), Roth (statement); Gauss map and Gauss
  measure, a.e. unbounded partial quotients, Khinchin's convergence theorem;
  Weyl's criterion, Weyl's theorem for $n\alpha$ and for polynomials (van der
  Corput), Benford for $2^n$, the three-gap theorem with proof; 14 exercises.
  When `ergodic-theory` is written, it should prove the ergodicity of the Gauss
  map and the results of `continued-fractions:remark-metric-results`, and can
  refer back to Weyl's criterion here.
- [x] 2026-11-05: **Number theory reorganised into three parts** (Number Theory
  after Probability; Algebraic Number Theory; Arithmetic Geometry after
  Algebraic Geometry), new planned chapter `class-groups-and-units`; the
  introduction's list of parts and reading path updated.
- [x] 2026-11-05: `geometry-of-numbers` (complete, about 1470 lines, 124 tags):
  lattices (bases, covolume, discrete subgroups, fundamental domains and
  Voronoi cells, index, congruence lattices, primitive vectors and adapted
  bases, projections, dual lattice); Blichfeldt, Minkowski's convex body
  theorem with counterexamples, linear forms, simultaneous approximation,
  Siegel's lemma; two and four squares and Legendre's theorem on
  $ax^2+by^2=cz^2$ via lattices; successive minima, Minkowski's second
  theorem (lower bound and ellipsoids proved, general upper bound cited);
  Hermite's constant and inequality, Lagrange–Gauss reduction and algorithm,
  hexagonal packing, $D_n$ and $E_8$, the LLL algorithm with proof of
  termination; lattice point counting, Gauss circle, Leibniz's series from
  $r_2$, Pick's theorem, Reeve tetrahedra, Ehrhart (cited); Minkowski–Hlawka
  with proof, bounds for $\gamma_n$; covering radius and the norm-Euclidean
  imaginary quadratic rings ($m = 1, 2, 3, 7, 11$); 14 exercises. Open: a
  full proof of the general upper bound of Minkowski's second theorem.
- [x] 2026-11-06: `analytic-number-theory` (complete, about 1640 lines, 131
  tags): Dirichlet series (half-planes, abscissae, uniqueness, Euler products,
  table of classical series, Landau's theorem); averages (Euler summation and
  $\gamma$, hyperbola method, $\sum\sigma$, $\sum\varphi$, coprime pairs,
  squarefree numbers, $\tau(n) \ll n^\varepsilon$, Turán and Hardy–Ramanujan,
  Erdős–Kac cited); the Gamma function from scratch (holomorphic parameter
  integrals, Beta, Euler limit, infinite products, Weierstrass product,
  cotangent by Herglotz, sine product, Wallis, reflection, duplication);
  zeta (continuation, bounds near $\sigma = 1$, 3-4-1, theta and the
  functional equation, trivial zeros, $\zeta(2k)$ and $\zeta(1-2k)$ via
  Bernoulli); Newman–Zagier analytic theorem, PNT, $M(x) = o(x)$ and
  $\sum\mu(n)/n = 0$, Wigert; PNT with error term $x e^{-c(\log x)^{1/10}}$ via
  a zero-free region proved from the 3-4-1 inequality, $\pi = \mathrm{li} +
  \ldots$; RH, easy directions of two equivalences, explicit formula, Robin,
  Selberg (cited); characters of finite abelian groups, Dirichlet
  characters, $L(1,\chi) \neq 0$ (Landau for real $\chi$), Dirichlet's theorem,
  PNT in progressions, Chebyshev bias, class number formula (statement);
  13 exercises. Open (optional): the classical zero-free region
  $1 - c/\log t$ via the Hadamard product, the explicit formula with proof,
  Gauss sums and the functional equation of $L(s,\chi)$, Pólya–Vinogradov,
  and van der Corput's $O(x^{1/3})$ for the circle and divisor problems.
- [x] 2026-11-06: `p-adic-numbers` (complete, about 1450 lines, 134 tags):
  absolute values, ultrametric geometry, equivalence, Ostrowski with proof,
  product formula, completion of a valued field; $\QQ_p$, $\ZZ_p$ (DVR,
  density of $\ZZ$), series, summable families, $p$-adic expansions
  (rationals = eventually periodic), inverse limit, compactness, total
  disconnectedness; Hensel's lemma ($|f(a)| < |f'(a)|^2$) with
  counterexamples, squares and square classes, Teichmüller representatives,
  roots of unity, $\QQ_p^\times \cong \ZZ \times \mu_{p-1} \times \ZZ_p$ (and
  $p = 2$), the $\QQ_p$ pairwise non-isomorphic; power series, substitution
  lemma, $\exp$/$\log$ (domains, isometric inverse isomorphisms), Mahler's
  theorem, Strassmann, Skolem–Mahler–Lech with proof (Berstel's example),
  Kummer congruences (remark); Hilbert symbol (norms, explicit formulas with
  full proofs, bilinearity, nondegeneracy), Hilbert reciprocity $\iff$ QR;
  quadratic forms over a field and over $\QQ_p$ (rank $\geq 5$ isotropic for
  $p$ odd, anisotropic rank-4 examples), approximation lemma, rationals with
  prescribed Hilbert symbols (Dirichlet), Hasse–Minkowski (n = 3 via
  Legendre), one place redundant for ternary forms, sums of three rational
  squares; 13 exercises. Open (optional): rank $\geq 5$ isotropic over
  $\QQ_2$ and the local classification with proofs (now cited), Meyer's
  theorem with proof.
- [x] 2026-11-06: **no repetition** (user): the characters of finite abelian
  groups were developed both in `representation-theory` and in
  `analytic-number-theory`; moved into
  `representation-theory:subsection-abelian-characters` (labels renamed,
  tags kept), enlarged with the double dual, the finite Fourier transform,
  Plancherel and convolution. Rule for the rewrite: before developing a
  notion, grep the earlier chapters; merge duplicates into the earliest
  natural chapter and cite it.
- [x] 2026-11-05: removed the paragraphs "On the way to the Hodge conjecture"
  from all chapters (the route stays in the introduction); The Hodge Project
  is linked wherever it is mentioned.

## Carried over from The Hodge Project (still open)

- [ ] `number-theory`: Bertrand's postulate (Erdős's proof via central
  binomial coefficients) and estimates of Chebyshev type (done in
  `prime-numbers`); continued fractions and Pell's equation (done in
  `continued-fractions`); $p$-adic numbers, Dirichlet characters.
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

- [x] 2026-11-07: **Measure and Integration**: new section *Extension and
  completion of measures* (π-systems and Dynkin systems, uniqueness, premeasures,
  Carathéodory–Hahn extension theorem, completion, Lebesgue measurable = Borel
  up to null sets, Lebesgue–Stieltjes measures with atoms/jumps, regularity,
  examples and counterexamples; 3 exercises). The Stieltjes lemma of
  Differentiation and Absolute Continuity now uses it instead of its own
  construction.

- [x] 2026-11-07: **Signed and Complex Measures** chapter (`signed-measures`,
  between differentiation and Radon measures): signed measures, Hahn and
  Jordan decompositions, total variation, complex measures and polar
  decomposition, the Banach space M(X), Lebesgue–Radon–Nikodym for signed and
  complex measures, chain rule, ε–δ absolute continuity, converse Hölder,
  duality (L^p)* = L^q with full proof, Minkowski's integral inequality,
  Hardy's inequality, uniform integrability, de la Vallée Poussin, Vitali
  convergence theorem, Scheffé; 11 exercises. Radon Measures and Functional
  Analysis now cite it instead of restating Hahn/Jordan and L^p duality.

- [x] 2026-11-06: **Measure theory split** into four chapters in a new part
  *Real Analysis and Measure Theory* (labels renamed, tags kept); the
  $5r$-covering lemma moved next to Vitali's lemma; prerequisites updated;
  wide displays split.

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
