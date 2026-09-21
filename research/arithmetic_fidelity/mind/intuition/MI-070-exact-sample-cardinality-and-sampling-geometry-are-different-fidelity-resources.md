# MI-070 — Exact sample cardinality and sampling geometry are different fidelity resources

**Evidence level:** exact source-fidelity synthesis from [AF-484](../../findings/AF-484-finite-prime-zeta-samples-admit-free-density-matched-beurling-controls.md), [AF-485](../../findings/AF-485-unbounded-rightward-samples-are-faithful-for-general-dirichlet-sources.md), and [AF-486](../../findings/AF-486-moving-hankel-determinants-recover-finite-dirichlet-depth-at-sharp-exponential-precision.md), refining the analytic-layer hierarchy of MI-004 and the exact-versus-quantitative sampling distinction of MI-044.

Finite exact sampling can remain completely nonfaithful even after strong side information is fixed. AF-484 shows that for any prescribed finite real sample set `1<s_1<...<s_m` and arbitrarily small coordinatewise perturbation tolerances, one can deform the rational primes to a nonintegral Beurling-prime sequence `Q={q_n}` with the same prime-counting density, free numerical factorization, and

`P_Q(s_j)=P(s_j)`

at every prescribed sample. The finite sample vector cuts the source space by only finitely many constraints; a positive-dimensional deformation fiber survives, and rational-prime identity is not recovered.

AF-485 shows that the situation changes qualitatively when the sample set itself escapes to `+infinity`. For an absolutely convergent general Dirichlet series with strictly increasing exponents, equality on any sequence `s_k` with `Re(s_k)->+infinity` determines the least surviving exponent and coefficient, then the next one, and so on. Applied to prime-zeta sources, a right-unbounded countable exact sample family is source-faithful. This rigidity is not analytic continuation from an interior accumulation point; it is successive dominance of the smallest unresolved exponent.

AF-486 resolves the first quantitative version of that rightward boundary at every fixed finite source depth. For a positive discrete Dirichlet source

`F(s)=sum_n a_n q_n^(-s)`, `a_n>0`, `q_1<q_2<...`,

the moving `J x J` Hankel determinant built from exactly `2J-1` consecutive samples `F(t),F(t+h),...,F(t+(2J-2)h)` satisfies a Vandermonde expansion whose leading term is the first `J` atoms. In particular,

`q_J = lim_(t->infinity) (D_J(t)/D_(J-1)(t))^(-1/t)`.

The determinant ratio performs joint finite-depth recovery rather than recursive atom-by-atom subtraction. If the sample errors are uniformly `O(epsilon q_J^(-t))`, with `epsilon` below a source-dependent separation/weight threshold, the same root-limit still recovers `q_J`. The absolute precision scale `q_J^(-t)` is also sharp in exponential order: deleting the `J`th atom itself produces a perturbation of exactly that size.

The resulting boundary is therefore sharper than either “more samples are better” or “rightward recovery is unstable.” Every fixed finite sample set at fixed locations admits AF-484 deformations, whereas a moving finite window whose base point tends to `+infinity` can stably recover any prescribed fixed depth when its absolute accuracy tracks the deepest retained exponential scale. Sampling cardinality, sampling geometry and measurement precision are distinct resources.

The reusable audit is to separate four questions: whether the sample map is exactly injective on the admitted source class, whether fixed finite sample locations leave deformation fibers, whether a moving sample geometry gives a finite-depth reconstruction formula, and what absolute accuracy that formula requires. AF-486 shows that joint Hankel geometry avoids recursive error compounding at fixed depth, but it does not remove the exponentially shrinking signal itself.

**Boundary.** AF-486 assumes a positive discrete Dirichlet source, fixed finite depth `J`, a fixed positive sample step, ordered separated nodes and source-dependent Vandermonde conditioning. It does not give uniform recovery as `J->infinity`, signed or complex coefficient stability, an efficient global reconstruction algorithm, or rational-prime provenance. Recovering amplitudes requires stronger relative determinant accuracy than recovering the nodes. AF-484 still shows that finitely many fixed real prime-zeta values plus the matched side information do not identify the rational primes. No RH consequence follows from these sampling statements alone.
