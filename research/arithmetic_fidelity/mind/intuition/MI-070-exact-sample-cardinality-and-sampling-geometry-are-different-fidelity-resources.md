# MI-070 — Exact sample cardinality and sampling geometry are different fidelity resources

**Evidence level:** exact source-fidelity synthesis from [AF-484](../../findings/AF-484-finite-prime-zeta-samples-admit-free-density-matched-beurling-controls.md) and [AF-485](../../findings/AF-485-unbounded-rightward-samples-are-faithful-for-general-dirichlet-sources.md), refining the analytic-layer hierarchy of MI-004 and the exact-versus-quantitative sampling distinction of MI-044.

Finite exact sampling can remain completely nonfaithful even after strong side information is fixed. AF-484 shows that for any prescribed finite real sample set `1<s_1<...<s_m` and arbitrarily small coordinatewise perturbation tolerances, one can deform the rational primes to a nonintegral Beurling-prime sequence `Q={q_n}` with the same prime-counting density, free numerical factorization, and

`P_Q(s_j)=P(s_j)`

at every prescribed sample. The finite sample vector cuts the source space by only finitely many constraints; a positive-dimensional deformation fiber survives, and rational-prime identity is not recovered.

AF-485 shows that the situation changes qualitatively when the sample set itself escapes to `+infinity`. For an absolutely convergent general Dirichlet series with strictly increasing exponents, equality on any sequence `s_k` with `Re(s_k)->+infinity` determines the least surviving exponent and coefficient, then the next one, and so on. Applied to prime-zeta sources, a right-unbounded countable exact sample family is source-faithful. This rigidity is not analytic continuation from an interior accumulation point; it is successive dominance of the smallest unresolved exponent.

The resulting boundary is sharper than “more samples are better.” Every finite exact family admits source deformations of the AF-484 type, while an unbounded sequence in the convergence half-plane can be injective without ever approaching the analytic boundary. What matters is the asymptotic geometry of the sampling set relative to the exponential basis, not only its cardinality.

Exact injectivity still does not imply stable recovery. At large real `t`, the contribution of a deeper source atom is exponentially small, so identifying later exponents from rightward samples requires correspondingly fine absolute accuracy. A sampling family can therefore be mathematically faithful while being catastrophically ill-conditioned for finite-precision or noisy reconstruction. This is the same exact-versus-quantitative separation seen elsewhere in Arithmetic Fidelity, now inside the source-identification problem itself.

The reusable audit is to separate three questions: whether the sample map is exactly injective on the admitted source class, whether finite truncations leave deformation fibers, and what accuracy is required to recover a chosen source depth. AF-484 answers the first two negatively for every finite prime-zeta sample family even with strong matched side information; AF-485 answers exact injectivity positively for right-unbounded samples but leaves the quantitative recovery modulus as the live problem.

**Boundary.** AF-485 uses exact equality and absolute convergence of general Dirichlet series with ordered exponents. It supplies no noise-stable inversion theorem, no efficient reconstruction algorithm, and no finite cutoff for recovering an unbounded source. AF-484 concerns finite real prime-zeta samples and Beurling-prime deformations; it does not match the full analytic prime-zeta function, the Euler product as a function, additive/congruence structure, or other independently imposed arithmetic data. No RH consequence follows from the sampling dichotomy alone.
