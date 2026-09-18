# MI-054 — One smooth full-Euler barycenter already reaches the log-squared Vinogradov--Korobov corridor

**Evidence level:** exact synthesis from [NB-212](../../findings/NB-212-smooth-euler-barycenter-saturates-the-log-squared-vinogradov-korobov-corridor.md), refining the representation used in [NB-211](../../findings/NB-211-vinogradov-korobov-prime-halasz-reaches-a-log-squared-diagonal-corridor.md).

NB-211 reaches an order-one positive-return gap by converting a small Euler defect into a phase-pinned plateau of large prime Dirichlet values and then applying a prime-supported Halász inequality. NB-212 shows that the same quantitative corridor is already visible before that reduction.

Choose one fixed nonzero `0<=f<=1` supported smoothly inside the Euler shell and form the full von-Mangoldt barycenter

`M_(a,f)(t)=sum_n Lambda(n)n^(-1-a-it) f(n/x_a)`.

A small positive Euler defect forces `M_(a,f)(t)` to stay close to its zero-frequency mass. At the same time, the Vinogradov--Korobov contour estimate writes it as the Fourier transform of the fixed shell window plus an error of the form

`Q^2 exp(-c X/(Q^(2/3)(log Q)^(1/3)))`,

with `Q=log(10+|t|)` and `X=X_a`. The fixed smooth window has a strict nonzero-frequency contraction, so the two statements are incompatible as long as that contour error tends to zero. Solving the error inequality gives the same corridor

`Q <= kappa X^(3/2)/(log X)^2`.

The important representation lesson is that the harmonic plateau and prime-only large-value machinery are **not load-bearing for this scale** once the source-faithful contour estimate is exposed. One positive full-Euler scalar already carries enough information. This matters because it localizes the remaining quantitative loss to the contour error itself rather than to prime selection or harmonic multiplicity.

NB-212 also identifies the prefactor phase transition. For an error

`L(Q) exp(-c X/(Q^(2/3)(log Q)^(1/3)))`,

any fixed positive polynomial growth `L(Q)=Q^(A+o(1))` forces the same log-squared threshold. A polylogarithmic prefactor would reach every `X^(3/2)/(log X)^(1/2+epsilon)` corridor, while a bounded prefactor would permit the Ford scale `X^(3/2)/sqrt(log X)` in principle. Reducing `Q^2` to another positive power changes constants but not the exponent of `log X`.

The next source theorem should therefore target the **growth class of the contour prefactor**, not merely the harmonic count or a smaller polynomial exponent. A useful improvement must explain how the smoothed logarithmic-derivative correlation avoids the polynomial `Q` loss uniformly in the coupled regime.

**Boundary.** The phase diagram is conditional on the displayed contour-error form and does not assert that polylogarithmic or bounded prefactors are currently available. The positive-return condition is still only a source-side obstruction; a separate Nyman destination argument must show that a successful approximant is forced into this positive source regime.