# Sources

## AF-001 — Fiberwise recoverability and unconstrained lifts

- David Blackwell, **“Equivalent Comparisons of Experiments,”** *The Annals of Mathematical Statistics* 24(2), 265–272 (1953). DOI: `10.1214/aoms/1177729032`. Role: classical comparison-of-experiments / garbling background for the principle that deterministic or stochastic post-processing cannot increase available decision information.
- William W. Armstrong, **“Dependency Structures of Data Base Relationships,”** *Information Processing 74*, 580–583 (1974). Role: classical functional-dependency language; equality of determinant values forcing equality of dependent values is the relational-data analogue of a discriminator being constant on compression fibers.
- H. S. Witsenhausen, **“The Zero-Error Side Information Problem and Chromatic Numbers,”** *IEEE Transactions on Information Theory* 22(5), 592–593 (1976). DOI: `10.1109/TIT.1976.1055607`. Role: zero-error side-information prior art; when side information is also known at the transmitter, the alphabet-minimization problem becomes trivial, closely paralleling the unrestricted fiberwise lift construction in AF-001.
- Alon Orlitsky and James R. Roche, **“Coding for Computing,”** *IEEE Transactions on Information Theory* 47(3), 903–917 (2001). DOI: `10.1109/18.915643`. Role: function-computation with side information; shows that nontrivial compression questions arise once the admissible coding/observation model is constrained rather than allowing an arbitrary target-carrying mark.

The elementary set-theoretic factorization statements in AF-001 are derived directly. These sources locate their closest established languages and prevent treating the basic fiber criterion or unconstrained side-information phenomenon as novel.

## AF-002 — Fixed-observable lifts are decision-relative discernibility reducts

- Zdzisław Pawlak, **“Rough Sets,”** *International Journal of Computer & Information Sciences* 11(5), 341–356 (1982). DOI: `10.1007/BF01001956`. Role: foundational rough-set / information-system framework in which retained attributes induce indiscernibility relations and exact definability depends on the resulting equivalence classes.
- Andrzej Skowron and Cecylia Rauszer, **“The Discernibility Matrices and Functions in Information Systems,”** in *Intelligent Decision Support: Handbook of Applications and Advances of the Rough Sets Theory*, 331–362 (1992). DOI: `10.1007/978-94-015-7975-9_21`. Role: direct prior art for pairwise discernibility sets, discernibility functions, and reducts; the decision-relative form matches AF-002 after conditioning on the already-retained map `T`.

AF-002 derives the conditional hitting-set statement directly from AF-001, but the finite fixed-library mechanism is classical rough-set reduct/discernibility mathematics. The source bridge is used to prevent a false novelty claim and to redirect future Arithmetic Fidelity work toward intrinsically constrained observable families and non-table-like settings.

## AF-003 — Invariant-observable quotients and orbit-closure fidelity

- David Mumford, John Fogarty, and Frances Kirwan, ***Geometric Invariant Theory***, 3rd ed., Ergebnisse der Mathematik und ihrer Grenzgebiete, vol. 34, Springer (1994), ISBN `978-3-540-56963-3`. Role: standard source for reductive-group invariant theory, affine categorical quotients, orbit separation by invariants, and the distinction between quotient points and arbitrary group orbits.
- T. A. Springer, ***Invariant Theory***, Lecture Notes in Mathematics 585, Springer (1977). DOI: `10.1007/BFb0095644`. Role: classical invariant-ring background and finite-generation/separation context for algebraic group actions.
- **“Invariants, theory of,”** *Encyclopedia of Mathematics*. Role: concise authoritative summary of the affine reductive quotient statement used here: the invariant ring defines a quotient whose fibers contain exactly one closed orbit, and invariant functions alone do not generally retain complete information about nonclosed orbits.

AF-003 derives the maximal-observable joint-evaluation criterion and the `\mathbb G_m` weight-`(1,-1)` example directly. The orbit-closure description of the full invariant algebra is classical GIT; the Arithmetic Fidelity contribution is to use that quotient as a no-go test for every lift constrained to the same invariant-observable class.
