# Plan of The Math Project

The goal: all of mathematics, at a good level, with complete proofs, written
slowly (motivation, examples, counterexamples, exercises with solutions), in
one strict logical order. The starting material is the 77 chapters copied
from [The Hodge Project](https://lufranovittorio.github.io/Appunti_Matematica/) on 2026-11-05 (about 1.5k PDF pages); the expected size
is about ten times that. Work through the phases in order, but new parts can
be started as soon as phase 0 is done. Tick items off (`[x]`) and move them to
Done with a short summary.

## Roadmap: the whole book, part by part (2026-11-07)

The structure has three levels (user, 2026-11-07: "one must see the macro-argument, the region"):
**part** = a large area, **chapter** = a region of it (a course), **section** = a topic. A new
chapter only for a genuinely new region; everything else becomes sections of an existing chapter.
Below, for every chapter: status and lines at 2026-11-07, then the sections to add or rebuild.
Topics in *italics* belong in that chapter even though one might look for them elsewhere (no
notion is developed twice). This list supersedes the chapter lists of Phase 1 below.

### I. Foundations
- `logic` (complete, 1300): natural deduction and sequent calculus with cut elimination (Gentzen);
  Gödel's incompleteness theorems with full proofs (arithmetisation, diagonal lemma, Löb, Tarski's
  undefinability); Peano and Presburger arithmetic; intuitionistic logic and Kripke models;
  modal logic (survey).
- `sets` (complete, 1153): ordinal arithmetic and Cantor normal form, cofinality, König's theorem,
  the axiom of choice and its equivalents (Tychonoff, Hamel bases, every vector space has a basis),
  ZFC in full, the cumulative hierarchy, constructible universe and independence of CH (survey),
  large cardinals (survey), descriptive set theory (Borel and analytic sets, Suslin's theorem).
- `number-systems` (complete, 972): surreal numbers (Conway), hyperreals and non-standard analysis
  (via ultrapowers), quaternions and octonions, Frobenius and Hurwitz theorems.
- `model-theory` (complete, 533): types and saturation, quantifier elimination for real closed
  and algebraically closed fields, o-minimality, Morley's categoricity theorem (statement),
  Ax–Grothendieck, ultraproducts and Łoś.
- `categories` (complete, 1315): monads, Kan extensions, ends, abelian and triangulated
  categories (survey here, details in homological algebra), topoi (survey).
- `computability-and-complexity` (planned): Turing machines, Church–Turing, halting problem,
  recursive and r.e. sets, Rice, degrees; P, NP, Cook–Levin, NP-complete problems, space
  complexity, Savitch, hierarchy theorems; randomised classes; Kolmogorov complexity.

### II. Algebra
- `groups` (complete, 1050): free groups and presentations, Nielsen–Schreier, word problem;
  nilpotent and solvable groups, Jordan–Hölder, finite simple groups (survey of the
  classification), Sylow in depth, groups of small order (table up to 32), semidirect products
  and extensions, transfer and Burnside's normal complement, *Coxeter groups and reflection
  groups*, wallpaper and crystallographic groups.
- `rings` (complete, 952): Euclidean, PID, UFD with counterexamples, Gaussian and Eisenstein
  integers, Gröbner bases and Buchberger, noncommutative rings, Wedderburn–Artin, Jacobson radical.
- `fields` (complete, 747): constructible numbers (section, see below), finite fields in depth,
  solvability by radicals, the inverse Galois problem (survey), infinite Galois theory and Krull
  topology, transcendence bases, *Hilbert irreducibility*, real closed fields and Artin–Schreier.
- `number-theory` (complete, 1269): keep elementary; perfect numbers, Carmichael numbers,
  arithmetic functions and Möbius inversion (check against analytic-number-theory), Gauss sums.
- `linear-algebra` (complete, 1439): canonical forms over PIDs, Perron–Frobenius, positive
  definite matrices, matrix inequalities, the polar and singular value decompositions, tensor
  products (if not in multilinear algebra).
- `multilinear-algebra` (complete, 848): symmetric and exterior powers, Pfaffians, Clifford algebras
  (algebraic part; spin-geometry uses them).
- `representation-theory` (complete, 2127): induced representations, Frobenius reciprocity, Mackey,
  characters of S_n and Young tableaux, Schur–Weyl duality; *Lie algebras* in full here
  (nilpotent and solvable, Engel, Lie, Cartan's criteria, Killing form, root systems and Dynkin
  diagrams, classification of simple Lie algebras, Weyl group, highest weights, Weyl character
  formula, Verma modules, PBW); no separate Lie algebra chapter.
- `commutative-algebra` (complete, 703, thin): rebuild to Stacks depth: localisation, Noetherian
  and Artinian rings, primary decomposition, integral extensions, going up/down, Noether
  normalisation, Nullstellensatz, dimension theory, Krull's principal ideal theorem, regular local
  rings, DVRs and Dedekind domains, completion, Hilbert polynomials, flatness, Cohen–Macaulay rings.
- `homological-algebra` (complete, 1290): Ext and Tor in detail, group cohomology, Lie algebra
  cohomology, spectral sequences, derived categories; Koszul complexes.

### III. Discrete Mathematics
- `combinatorics` (complete, 1949) and `generating-functions` (complete, 1849): designs and finite
  geometries, Latin squares, matroids, posets (Dilworth, Möbius functions of posets), symmetric
  functions, *combinatorics on words*.
- `graph-theory` (planned): trees, Euler and Hamilton, matchings and Hall, Menger, flows and
  max-flow min-cut, colourings (Brooks, Vizing), planarity and Euler's formula, the four colour
  theorem (survey), Kuratowski, Ramsey and Turán, extremal graph theory, spectral graph theory,
  expanders, random graphs; draft in `drafts/graph-theory-part1.tex`.
- `probabilistic-method` (planned): first and second moment, Lovász local lemma, martingale
  concentration, random graphs (thresholds), entropy methods.

### III bis. Classical and Discrete Geometry (new part, 2026-11-08)
- `classical-geometry` (planned, new): axiomatics, Euclidean isometries and Platonic solids,
  triangle geometry (Euler line, Feuerbach, Ceva, Menelaus, Ptolemy, Morley), inversion, affine
  and projective geometry (Desargues, Pappus, Pascal, cross-ratio), spherical and hyperbolic
  geometry, constructions.
- `discrete-geometry` (planned, new): Carathéodory/Radon/Helly, polytopes and Euler's formula,
  regular polytopes, Cauchy rigidity, Hilbert's third problem, Brunn–Minkowski and the
  isoperimetric inequality, Ehrhart, Szemerédi–Trotter, packings and tilings.

### IV. Topology
- `general-topology` (complete, 2125): uniform spaces, nets and filters, paracompactness and
  partitions of unity, metrisation theorems, Stone–Čech, Baire and its applications, dimension theory.
- `homotopy` (complete, 781): CW complexes, cellular approximation, higher homotopy groups, the
  long exact sequence of a fibration, Whitehead, Hurewicz, Freudenthal, Eilenberg–MacLane spaces,
  the Hopf fibration, homotopy groups of spheres (survey).
- `topological-manifolds` (complete, 590) and `poincare-duality` (complete, 420): Lefschetz fixed
  point theorem, linking forms, Alexander duality, the Jordan–Brouwer separation theorem.
- `singular-homology` (complete, 1011): cellular homology, Mayer–Vietoris examples, Künneth,
  universal coefficients, cup products and the cohomology rings of projective spaces.
- `cohomology-operations` (complete, 235, thin): Steenrod squares and reduced powers, Adem
  relations, Hopf invariant, the Steenrod algebra; consider merging into `singular-homology`.
- `low-dimensional-topology` (planned, new): surfaces, mapping class groups, knots and their
  invariants, braids, 3-manifolds, survey of 4-manifolds. Knot theory enlarged (user,
  2026-11-08): HOMFLY-PT, Vassiliev invariants, concordance, hyperbolic knots, Khovanov and knot
  Floer homology, quantum invariants (surveys).
- `geometric-group-theory` (planned, new): Cayley graphs, quasi-isometries, Švarc–Milnor, Bass–Serre,
  growth (Gromov, Grigorchuk), hyperbolic groups, ends, amenability and Banach–Tarski.
- `singular-homology`: add *persistent homology* (topological data analysis) as a section.
- `poincare-duality`: the *Jordan curve theorem* is not in the book yet (prove it there, with
  Jordan–Brouwer).
- `sheaves` (complete, 686): rebuild; presheaves, sheafification, étalé spaces, Čech and derived
  functor cohomology, comparison theorems, soft and fine sheaves, de Rham and Dolbeault
  resolutions, Leray spectral sequence, base change.

### V. Real Analysis and Measure Theory
- `real-analysis` (complete, 2391): Fourier series in detail (Fejér, Dirichlet, Gibbs), convex
  functions, inequalities (AM-GM, Jensen, rearrangement), Weierstrass approximation, implicit and
  inverse function theorems, Riemann–Stieltjes integral.
- `measure-theory` (complete, 2102): slower Littlewood principles; change of variables (polar and
  spherical coordinates, Jacobian via elementary matrices, Sard).
- `lebesgue-differentiation`, `signed-measures`, `radon-measures`: Lebesgue points, unify maximal
  inequalities; Riesz–Markov in all forms; Haar measure examples.
- `geometric-measure-theory` (complete, 1764): Steiner symmetrisation, Kakeya sets,
  rectifiability in depth, BV functions and sets of finite perimeter, De Giorgi's structure theorem.

### VI. Complex and Functional Analysis
- `complex-analysis` (complete, 1173, thin): rebuild: Riemann mapping theorem, Schwarz–Christoffel,
  harmonic functions and the Dirichlet problem, Runge, Mittag-Leffler, Weierstrass factorisation,
  Hadamard, Picard's theorems, normal families (Montel), analytic continuation and monodromy,
  Riemann surfaces of algebraic functions (informal; curves chapter does the theory).
- `special-functions` (planned, new): Gamma (moved from analytic-number-theory), asymptotics,
  orthogonal polynomials, Fuchsian equations, hypergeometric, Bessel, elliptic and theta functions.
- `functional-analysis` (complete, 1234): Banach algebras and Gelfand theory, spectral theorem for
  unbounded operators, compact and Fredholm operators, weak topologies, Banach–Alaoglu,
  Krein–Milman, Dunford–Pettis, interpolation (Riesz–Thorin, Marcinkiewicz), locally convex spaces.
- `several-complex-variables` (complete, 314, thin): Hartogs, domains of holomorphy, pseudoconvexity,
  the dbar problem (Hörmander), Cartan's theorems A and B (survey), Weierstrass preparation.
- `functional-analysis`: *integral equations* (Fredholm alternative, Volterra equations).
- `real-analysis`: *summability* (Cesàro, Abel, Tauberian theorems of Hardy–Littlewood), check
  against analytic-number-theory.
- `geometric-measure-theory`: *fractals* (iterated function systems, self-similar sets, the
  Moran equation, box and Hausdorff dimension of the Cantor set and the Sierpiński gasket).
- `distributions` (complete, 496): Schwartz space, tempered distributions, Fourier transform,
  Paley–Wiener, Sobolev embedding (or in sobolev-spaces), fundamental solutions, Malgrange–Ehrenpreis.
- `harmonic-analysis` (planned): Fourier analysis on locally compact abelian groups, Pontryagin
  duality, Calderón–Zygmund theory, Hilbert transform, Littlewood–Paley, H^1 and BMO, wavelets,
  Peter–Weyl and harmonic analysis on compact groups.
- `operator-algebras` (planned): C*-algebras, Gelfand–Naimark, GNS, von Neumann algebras, the
  bicommutant theorem, factors, K-theory of C*-algebras (survey).

### VII. Probability and Statistics
- `probability` (planned): as in its outline; move Borel–Cantelli and independence here from
  measure-theory (or cite).
- `martingales` (planned, with the stochastic-process outlines): Markov chains (recurrence,
  stationary distributions, mixing times), Poisson processes, Brownian motion (construction,
  path properties, strong Markov, reflection), stochastic calculus (Itô integral, Itô's formula,
  Girsanov, SDEs), random walks and potential theory, percolation (survey).
- `statistics` (planned): estimation, sufficiency, Cramér–Rao, maximum likelihood, tests and
  Neyman–Pearson, confidence intervals, linear models, Bayesian inference, nonparametric methods,
  bootstrap.
- `information-theory` (planned): entropy, source and channel coding theorems, Kraft, Huffman,
  error-correcting codes (Hamming, Reed–Solomon, BCH, bounds), rate distortion.

### VIII. Number Theory
- `prime-numbers`, `continued-fractions`, `geometry-of-numbers`, `analytic-number-theory`,
  `p-adic-numbers` (complete): open items listed in their Done entries; *transcendence* goes into
  `continued-fractions` (new sections: Lindemann–Weierstrass, Gelfond–Schneider, Baker's theorem
  (statement), Schanuel's conjecture, Roth and Schmidt's subspace theorem, irrationality of ζ(3)
  (Apéry/Beukers)); the chapter can be renamed "Diophantine Approximation and Transcendence".
- `additive-number-theory` (draft 2026-11-07): to deepen: the circle method for Waring
  (Hardy–Littlewood asymptotic, Vinogradov's three primes), Brun's sieve, Selberg's sieve,
  Freiman/Plünnecke, partitions (Hardy–Ramanujan).
- `diophantine-equations` (draft 2026-11-07): to deepen: Skolem's p-adic method, Thue's theorem
  with proof, number of representations by three squares, Legendre's theorem on ax²+by²+cz²
  with an elementary proof, more Mordell curves, Kummer's regular primes (after cyclotomic fields).
- `cryptography` (planned, new): arithmetic algorithms, primality (Miller–Rabin, AKS with proof),
  factoring, discrete logarithms, RSA/Diffie–Hellman, lattice cryptography, Shor (survey).
- `algebraic-number-theory` (planned): number fields, class groups and units, cyclotomic fields,
  Kummer theory, quadratic fields and binary quadratic forms (link with number-theory), Dedekind
  zeta functions and the class number formula.
- `local-fields` (planned): local fields, ramification groups, local and global class field
  theory, Hilbert class fields, Kronecker–Weber, Chebotarev, adeles and ideles, Tate's thesis;
  Iwasawa theory and p-adic Hodge theory (surveys).
- Arithmetic of curves stays in Part *Algebraic and Arithmetic Geometry* (modular forms, elliptic curves).

### IX. Differential Equations and Dynamical Systems
- `ordinary-differential-equations` (planned): as in its outline; plus Floquet theory, Sturm
  comparison, boundary value problems and Green's functions, Hamiltonian systems (pointer to
  symplectic), bifurcation theory, chaos (Smale horseshoe, Lorenz), circle maps and rotation number.
- `ergodic-theory` (planned): plus the ergodicity of the Gauss map (see continued-fractions),
  Furstenberg's multiple recurrence and Szemerédi, topological dynamics, entropy (Kolmogorov–Sinai).
- `sobolev-spaces` (planned, PDE): plus first-order equations and characteristics, conservation
  laws and shocks, the Navier–Stokes and Euler equations (survey), dispersive equations,
  Schauder estimates, De Giorgi–Nash–Moser.
- `calculus-of-variations` (planned): direct method, Γ-convergence, minimal surfaces, harmonic
  maps, optimal transport (Monge–Kantorovich, Brenier).

### X. Numerical Analysis and Optimisation
- `numerical-analysis` (planned): plus FFT, wavelets numerics, Monte Carlo methods, spectral methods.
- `convex-analysis` (planned): plus semidefinite programming, interior point methods,
  combinatorial optimisation (matchings, network flows, integer programming), stochastic gradient.
- `game-theory` (planned): plus evolutionary game theory, social choice (Arrow's theorem), voting.

### XI. Differential Geometry
- `smooth-manifolds`, `lie-groups`, `vector-bundles`, `differential-forms`, `de-rham`,
  `connections`, `characteristic-classes` (complete): slower rewrite (see Phase 2); Lie groups:
  maximal tori, Weyl group, classification of compact Lie groups, homogeneous spaces.
- `riemannian-geometry` (complete, 4405): extract more lemmas (Hopf–Rinow done); comparison
  geometry, Bishop–Gromov, Cheeger–Gromoll splitting, sphere theorem (survey), Ricci flow (survey).
- `k-theory` (planned): vector bundles to K-groups, Bott periodicity, Adams operations, Hopf invariant one.
- `currents` (draft, 1207): finish.
- `symplectic-geometry` (complete): still to do: toric manifolds and Delzant's theorem,
  Lagrangian neighbourhood theorem with proof, generating functions; *contact geometry* (contact
  structures, Darboux, Reeb flows, Weinstein conjecture survey); Gromov's non-squeezing theorem,
  J-holomorphic curves and Floer homology (Arnold conjecture, survey).
- Classical differential geometry of *curves and surfaces in R³* (Frenet–Serret, curvature and
  torsion, first and second fundamental forms, Gauss–Bonnet for surfaces, minimal surfaces) is
  not in the book as such: add as the first sections of `riemannian-geometry` (or check whether
  it is scattered there and gather it).
- `characteristic-classes` / `k-theory`: cobordism, Pontryagin–Thom, signature theorem, exotic
  spheres (now in the k-theory plan).
- `elliptic-operators`: still cited, not proved: invariance of H^s under diffeomorphisms for
  non-integer s (Proposition sobolev-sections, Warner). Possible: parametrix and
  pseudodifferential operators (survey).
- `de-rham`: still to do: Thom isomorphism and Euler class with forms (Bott–Tu), Leray–Hirsch.
- `spin-geometry` (planned, new): Clifford algebras, spin structures, Dirac operator, index theorem.
- Also: *Riemann surfaces* are covered by `complex-manifolds` and `curves`; *Morse theory* goes as
  sections in `riemannian-geometry` or `smooth-manifolds` (Morse lemma, handle decompositions,
  Morse inequalities, h-cobordism (survey)).

### XII. Complex Geometry
- `complex-manifolds`, `kahler`, `kodaira` (complete): Chern connection, Kähler identities.
- `deformations` (draft): finish.
- `calabi-yau` (complete, 249, thin): Calabi conjecture (Yau's proof sketch), mirror symmetry
  (survey); consider merging into `kahler`. *SYZ* (user, 2026-11-08): special Lagrangian
  fibrations and the Strominger–Yau–Zaslow conjecture go into the new chapter `mirror-symmetry`.

### XIII. Algebraic and Arithmetic Geometry
- `varieties`, `schemes` (complete): rebuild to Stacks depth: morphisms (finite, proper, flat,
  smooth, étale), valuative criteria, differentials, Serre duality, Grothendieck–Riemann–Roch.
- `divisors` (326), `gaga` (266), `curves` (297), `etale-cohomology` (188): thin; rebuild
  (curves: Riemann–Roch with proof, Hurwitz, canonical embedding, hyperelliptic curves, Weierstrass
  points, Jacobians; étale: sites, étale fundamental group, comparison theorems, Weil conjectures).
- `algebraic-groups`, `intersection-theory` (complete): Chow rings, Grassmannians and Schubert
  calculus, enumerative geometry (27 lines, 2875 lines on the quintic, survey).
- `algebraic-surfaces` (planned, new); plus toric varieties and the minimal model programme (survey).
- `moduli-spaces` (planned, new): moduli functors, Hilbert and Quot schemes, GIT, M_g and
  Deligne–Mumford, vector bundles on curves, stacks (survey).
- `schemes`: derived categories of coherent sheaves, Fourier–Mukai, Bondal–Orlov (or in
  `mirror-symmetry`); tropical geometry (survey) somewhere in this part.
- `modular-forms` (planned): modular group, Eisenstein series, q-expansions, Hecke operators,
  L-functions, theta functions and quadratic forms, modular curves.
- `elliptic-curves-arithmetic` (planned): Mordell–Weil, heights, torsion (Nagell–Lutz, Mazur
  statement), reduction, Hasse, BSD (statement), modularity (statement).

### XIV. Hodge Theory
- All complete but thin (363–1016): computed examples, counterexamples, exercises (Phase 2).

### XV. Mathematical Physics (new part)
- Supersymmetry and supermathematics (user, 2026-11-07): super linear algebra is in
  `multilinear-algebra` (section-super: super vector spaces, Koszul rule, superalgebras, supertrace,
  Berezin integral, fermionic Gaussians). Still to do: Lie superalgebras (gl(m|n), osp, Kac's
  classification, survey) in `representation-theory`; supersymmetric QM, Witten index, Morse
  inequalities via Witten deformation in `quantum-mechanics`; supermanifolds, Berezinian, Getzler's
  proof of the index theorem in `spin-geometry`.
- `classical-mechanics`, `quantum-mechanics`, `general-relativity` (planned, new).
- `mirror-symmetry` (planned, new, 2026-11-08): Batyrev, Gromov–Witten invariants and quantum
  cohomology, the quintic prediction, SYZ (special Lagrangian fibrations, T-duality, Gross–Siebert),
  homological mirror symmetry, TQFT (survey).
- Later candidates (only if they become real regions): statistical mechanics (Ising model, phase
  transitions), quantum field theory (survey), gauge theory (Yang–Mills, instantons).

## Coverage audit (user, 2026-11-08: "a lot of math I forget, don't make me tell you")

Check the book against the whole of mathematics on my own initiative, using the MSC 2020 top-level
classes as a checklist, and add missing regions to the plan without being asked. Audit of
2026-11-08 (done: new chapters above; still to place):
- 03 logic: *universal algebra* (Birkhoff's HSP theorem), *Boolean algebras and Stone duality*,
  lattices (06) → sections in `model-theory` or `categories`; homotopy type theory (survey).
- 18 categories: ∞-categories and higher category theory (survey).
- 16/17 algebra: quivers and Gabriel's theorem, quantum groups, Hopf algebras, vertex algebras and
  monstrous moonshine (survey) → `representation-theory`; profinite groups → `groups`.
- 37 dynamics: holomorphic and hyperbolic dynamics now in `ergodic-theory` (consider renaming it
  "Dynamical Systems and Ergodic Theory").
- 60/62: random matrices, large deviations, learning theory now planned; mathematical finance is in
  `martingales`.
- 74/76 continuum and fluid mechanics: survey in `sobolev-spaces` (Navier–Stokes listed);
  statistical mechanics (Ising, phase transitions) and gauge theory remain later candidates.
- 92/93 biology and control: now in the ODE and calculus-of-variations plans.
- 01 history: a timeline in the introduction (optional).
Re-run this audit whenever a part is finished.

## Phase 0: infrastructure (first)

All done (see Done). Possible later improvements:

- [ ] A per-item "report" link (next to each tag badge) in `web/Themes/math/js/site.js`,
  prefilling the issue with the tag; the page footer already does it per page.
- [ ] In the part PDFs, make references to other parts links to the website
  (now they are printed with the right number but are not links).

## Phase 1: new parts (one at a time, each chapter complete before the next)

(Historical list; the slugs have since been merged, see the Roadmap above.)

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

## Organisation and stated lemmas (user, 2026-11-07)

- Chapters are the major areas; prefer new *sections* inside an existing chapter to new
  chapters. Do not add chapters just because a topic was named as an example (varifolds, knot
  theory): coverage must be balanced and comprehensive. To do:
  - ~~merge thin adjacent chapters~~ (done 2026-11-07: 126 → 92 chapters). Each absorbed
    chapter became a run of sections in the chapter before it; labels `guest:x` became
    `host:x`, the chapter label became `host:section-guest`, and the old introduction tags
    are `alias:` lines in `tags/tags`. Merged: spectral sequences and derived categories
    into homological-algebra; singular cohomology into singular-homology; sheaf cohomology
    into sheaves; the stochastic-process outlines into martingales; class groups and
    cyclotomic fields into algebraic-number-theory; class field theory into local-fields;
    dynamical systems into the ODE chapter; elliptic and evolution PDE into sobolev-spaces;
    the numerical outlines into numerical-analysis; LP and nonlinear optimisation into
    convex-analysis; varifolds into currents; holomorphic bundles and Dolbeault into
    complex-manifolds; the Hodge decomposition and the Lefschetz theorems into kahler;
    coherent sheaves and cohomology into schemes; abelian varieties into algebraic-groups;
    cycle class and index theorems into intersection-theory; Mumford–Tate into
    hodge-structures; Lefschetz (1,1) into hodge-conjecture; intermediate Jacobians into
    vhs; failures into known-cases; the Tate and standard conjectures into absolute-hodge.
    Still possible: cohomology-operations, calabi-yau, gaga, the small topology chapters;
  - ~~knot theory~~: part of the new planned chapter `low-dimensional-topology` (surfaces,
    knots, 3-manifolds, 4-manifolds survey).
  - ~~merge small parts~~ (done 2026-11-07: 19 → 15 parts; Sheaves into Topology, Algebraic
    Number Theory into Number Theory, Arithmetic Geometry into Algebraic and Arithmetic Geometry,
    Optimisation into Numerical Analysis and Optimisation; Miscellany replaced by Mathematical
    Physics; old part labels are `alias:` tags). New planned chapters: low-dimensional-topology,
    special-functions, additive-number-theory, algebraic-surfaces, spin-geometry,
    classical-mechanics, quantum-mechanics, general-relativity.
- **State every reusable step as its own result.** Sweep the existing chapters for facts
  proved inside proofs and extract them as lemmas/propositions with labels. First example,
  `riemannian-geometry:theorem-hopf-rinow`:
  - the geodesic-sphere lemma (every curve from p to q leaves the normal ball through the
    geodesic sphere S, and d(p, q) = δ + min_S d(·, q); cf. Gallot–Hulin–Lafontaine 2.104);
  - "exp_p defined on all of T_pM implies every q is joined to p by a minimising geodesic";
  - extension of geodesics in complete manifolds.

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
     ~~`diophantine-equations`~~ (draft 2026-11-07).
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
     *Extension and completion of measures*); ~~rewrite the early sections
     slowly (σ-algebras, measures, measurable functions, image measures and
     the abstract change of variables, Hölder with all cases)~~ (done
     2026-11-07); ~~Bernstein sets, slower *Modes of convergence* and
     *Product measures* with infinite products~~ (done 2026-11-07); still to
     do: a slower *Littlewood's principles* section, and the change of
     variables section (polar and spherical coordinates, the Jacobian of
     linear maps proved via elementary matrices, Sard's lemma);
   - ~~new `signed-measures`~~ (done 2026-11-07; Dunford–Pettis left for
     `functional-analysis`, where weak topologies are);
   - `lebesgue-differentiation`: ~~functions of bounded variation, Banach–Zarecki~~
     (done 2026-11-07); Lebesgue points, unify the doubling maximal inequality
     with Hardy–Littlewood;
   - ~~`radon-measures`: Besicovitch covering theorem with proof, Prokhorov;
     Haar measure~~ (done 2026-11-07);
   - `geometric-measure-theory`: ~~Frostman's lemma, energies, Marstrand~~ (done
     2026-11-07), ~~Brunn–Minkowski and the
     isoperimetric inequality~~ (done 2026-11-07, for the Minkowski content;
     the perimeter version needs BV functions), Steiner symmetrisation,
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

- [x] 2026-11-07: **Drafts** of `additive-number-theory` (circle-method identity, Schnirelmann,
  Legendre sieve, Cauchy–Davenport, Ruzsa) and `diophantine-equations` (Frobenius/Sylvester,
  Pythagorean triples and conics, descent for x⁴±y⁴=z², congruent numbers and y²=x³−n²x,
  Davenport–Cassels and three squares, Gauss's triangular numbers, Markov tree, Mordell
  y²=x³+7 and y²=x³−2, FLT for 3 and 4, Sophie Germain, Mason–Stothers, abc, Hilbert's tenth).

- [x] 2026-11-07: **Elliptic regularity fully proved**: `distributions` gets Peetre's inequality,
  multiplication on H^s (with the sharp sup|φ| bound), interpolation, difference quotients,
  local elliptic estimate (freezing coefficients) and local regularity, Weyl's lemma, the
  counterexample x d/dx; `elliptic-operators` proves the global estimate and regularity from
  them (localisation lemma). Wirtinger stated once (distributions). **Currents no longer
  duplicated**: the de Rham section on currents moved into `currents` as "Currents on
  manifolds" (labels renamed to `currents:`), and the Euclidean definition is now a dimension
  convention. **One Exercises section per chapter** (18 chapters normalised).

- [x] 2026-11-07: **Differential geometry, first round.** `riemannian-geometry`: Hopf–Rinow
  split into lemma-geodesic-sphere, proposition-minimising-from-point,
  lemma-extension-geodesics. `hodge-theorem`: elliptic complexes (Dolbeault, twisted de Rham),
  spectrum and McKean–Singer, heat flow, Lichnerowicz, conformal invariance of * in the middle
  degree and signature via self-dual forms, products. `symplectic-geometry`: Moser's formula
  as a lemma (Darboux and Moser fully proved), compatible almost complex structures (contractible),
  moment maps, Noether, KKS form on coadjoint orbits, symplectic reduction, Liouville–Arnold,
  survey. `de-rham`: compact supports (fibre integration, compact Poincaré lemma,
  Mayer–Vietoris), Poincaré duality proved by induction on good covers, degree theory with forms
  (local formula, homotopy invariance, fundamental theorem of algebra, comparison with the
  homological degree; Brouwer/hairy ball not repeated, only re-proved in a remark).

- [x] 2026-11-07: **Varifolds** (new chapter after *Currents*, draft): Grassmannian as
  projections (compactness, G(2,1) as a circle), varifolds, weight, convergence and
  compactness, averaging lemma and the varifold limit of oscillating graphs (no mass loss),
  push-forward and Jacobians on planes, C^1-rectifiable sets (tangent planes agree a.e.,
  densities of submanifolds), rectifiable/integral varifolds with Θ = θ a.e., first variation
  as derivative of area, first variation formula with mean curvature and conormal, stationary
  ⇔ minimal, cones over rays and triple junctions (120°), space-filling stationary varifolds,
  Plateau's laws and Taylor (cited), generalised mean curvature and boundary, monotonicity
  formula with full proof, densities (usc), lower area bound, tangent cones, Allard compactness
  and regularity (cited), min–max survey; 6 exercises.

- [x] 2026-11-07: **Currents** (new chapter after *Riemannian Geometry*, draft): currents
  as functionals on forms with multivector notation, push-forward, mass and normal
  currents, representation T = ‖T‖∧T⃗, lower semicontinuity of mass (oscillating graphs),
  compactness of currents of bounded mass, homotopy formula and cones, Lipschitz images,
  integer-multiplicity rectifiable and integral currents, boundary rectifiability and
  Federer–Fleming (cited), existence for Plateau's problem, calibrations (flat discs,
  complex curves, minimal graphs), 3 exercises. *Varifolds* added as a planned chapter.

- [x] 2026-11-07: **Frostman, energies, Marstrand** (new last section of *Geometric
  Measure Theory*): mass distribution principle as a lemma, Hausdorff content,
  Frostman's lemma for compact sets (dyadic proof), measure characterisation of
  dimension, Riesz potentials and energies, energy characterisation of dimension,
  capacity, Marstrand's projection theorem (Kaufman's energy proof), examples
  (C×C, four-corner set), 2 exercises (energy of an interval, dimension of products).

- [x] 2026-11-07: **Monotone functions and bounded variation** (new section of
  *Differentiation and Absolute Continuity*): Vitali covering theorem for fine covers,
  total variation, Jordan decomposition with minimality, jumps of monotone functions,
  Dini derivatives, Lebesgue's theorem (covering proof), Fubini's theorem on series,
  decomposition into absolutely continuous + singular continuous + jump parts,
  Luzin's property (N), Banach–Zarecki, variation = ∫|F'|, FTC for functions
  differentiable off a countable set; 4 exercises (integration by parts, composition
  of AC functions, strictly increasing singular function).

- [x] 2026-11-07: **Besicovitch and Prokhorov** (*Radon Measures*): Besicovitch covering
  theorem with full proof (explicit constant), Vitali-type coverings for every Radon
  measure, differentiation of a Radon measure with respect to any Radon measure on R^n
  (Lebesgue decomposition as a limit of ratios), examples (atoms, Cantor measure);
  narrow convergence, tightness, Prokhorov's theorem, moments example.

- [x] 2026-11-07: **Haar measure** (new section of *Radon Measures*): Weil's existence
  proof, uniqueness, modular function, unimodular groups, the affine group,
  Steinhaus' theorem and measurable solutions of Cauchy's equation, 3 exercises;
  Lie groups and p-adic numbers now cite it. **Brunn–Minkowski** (new first
  section of *Geometric Measure Theory*): full proof, multiplicative form,
  isodiametric inequality, outer Minkowski content, Steiner's formula for convex
  polygons, isoperimetric inequality, L² ≥ 4πF. New Vitali covering theorem in
  *Differentiation*; the proof of H^n = λ^n is now complete (it used to refer to
  Evans–Gariepy).

- [x] 2026-11-07: **Measure and Integration**, second round: Cantor–Bendixson
  lemma and Bernstein sets (with Solovay's theorem quoted); *Modes of
  convergence* rewritten (almost uniform convergence, Riesz's theorem on Cauchy
  sequences in measure, the metric of convergence in measure, a.e. convergence
  is not topological, dominated convergence in measure, diagram of
  implications); *Product measures* rewritten in three subsections plus a new
  one on infinite products of probability measures (existence theorem with full
  proof, independent random variables, coin tossing = Lebesgue measure),
  sections lemma, Borel σ-algebra of products, σ-finiteness and continuous
  Fubini counterexamples, Sierpiński's set, layer-cake examples.

- [x] 2026-11-07: **Measure and Integration**: opening rewritten slowly in three
  sections, *σ-algebras* (closure lemma, trace/preimage σ-algebras, generated and
  Borel σ-algebras, Borel generators with proof, increasing unions, ℚ is F_σ but
  not G_δ), *Measures* (full definition, notation, cocountable and infinite
  measures, inclusion–exclusion with derangements) and *Measurable functions*
  (generators lemma, examples, five-part proposition with full proofs,
  counterexamples, image measures); abstract change of variables
  ∫g d(f_*μ) = ∫g∘f dμ; Hölder/Minkowski with all cases, Young's product
  inequality, equality case, interpolation of L^p norms, failure for p < 1.

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
