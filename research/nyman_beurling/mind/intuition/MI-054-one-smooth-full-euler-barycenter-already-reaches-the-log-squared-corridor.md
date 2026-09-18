# MI-054 — One smooth full-Euler barycenter reaches the log-squared corridor, and ordinary primitivization does not improve its growth class

**Evidence level:** exact synthesis from [NB-212](../../findings/NB-212-smooth-euler-barycenter-saturates-the-log-squared-vinogradov-korobov-corridor.md) and [NB-213](../../findings/NB-213-absolute-mellin-primitivization-preserves-a-positive-power-vk-tariff.md), refining the representation used in [NB-211](../../findings/NB-211-vinogradov-korobov-prime-halasz-reaches-a-log-squared-diagonal-corridor.md).

NB-211 reaches an order-one positive-return gap by converting a small Euler defect into a phase-pinned plateau of large prime Dirichlet values and then applying a prime-supported Halász inequality. NB-212 shows that the same quantitative corridor is already visible before that reduction.

Choose one fixed nonzero `0<=f<=1` supported smoothly inside the Euler shell and form the full von-Mangoldt barycenter

`M_(a,f)(t)=sum_n Lambda(n)n^(-1-a-it) f(n/x_a)`.

A small positive Euler defect forces `M_(a,f)(t)` to stay close to its zero-frequency mass. At the same time, the Vinogradov--Korobov contour estimate writes it as the Fourier transform of the fixed shell window plus an error of the form

`Q^2 exp(-c X/(Q^(2/3)(log Q)^(1/3)))`,

with `Q=log(10+|t|)` and `X=X_a`. The fixed smooth window has a strict nonzero-frequency contraction, so the two statements are incompatible while that contour error tends to zero. Solving the error inequality gives the same corridor

`Q <= kappa X^(3/2)/(log X)^2`.

The important representation lesson is that the harmonic plateau and prime-only large-value machinery are **not load-bearing for this scale** once the source-faithful contour estimate is exposed. One positive full-Euler scalar already carries enough information. This localizes the remaining quantitative loss to the contour interface rather than to prime selection or harmonic multiplicity.

NB-212 identifies the prefactor phase transition. For an error

`L(Q) exp(-c X/(Q^(2/3)(log Q)^(1/3)))`,

any fixed positive polynomial growth `L(Q)=Q^(A+o(1))` forces the same log-squared threshold. A polylogarithmic prefactor would reach every `X^(3/2)/(log X)^(1/2+epsilon)` corridor, while a bounded prefactor would permit the Ford scale `X^(3/2)/sqrt(log X)` in principle.

NB-213 shows that **ordinary Mellin primitivization does not change that growth class** when followed by absolute values. Replacing `-zeta'/zeta` by `log zeta` divides the Euler coefficient by `log n`, but integration by parts differentiates the shell carrier `e^(iXv)` and restores a factor `X`. On the coupled diagonal,

`X=Q^(2/3+o(1))`,

so even a hypothetical `Q^(o(1))` pointwise envelope for `log zeta` yields a reconstructed prefactor `Q^(2/3+o(1))`. Any fixed number of ordinary primitive transfers similarly pays powers of `X` and remains in the positive-power class.

The next source theorem must therefore improve the **final reconstructed contour bound**, not merely replace the arithmetic transform by a smoother-looking primitive. A real escape must exploit cancellation between the primitive and `e^(iXv)` before taking absolute values, or change the observable so that source reconstruction does not repay the primitive gain through the carrier.

**Boundary.** NB-213 is a method boundary, not a lower bound for the true oscillatory contour integral. Joint cancellation could still make the integral substantially smaller. The positive-return condition also remains only a source-side obstruction; a separate Nyman destination theorem must show that a successful approximant is forced into this positive source regime.