# AF-290 — Boundary-zero distance is the exact local gate from quotient recovery to Dirichlet zero-count fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `ZERO-COUNT`, `TARGET-RELATIVE`, `GAUGE-QUOTIENT`, `CONDITIONING`, `NO-NOVELTY-CLAIM`

## Claim

AF-289 leaves a precise target-level question open: a small coefficient error modulo common-clock gauge does not by itself imply that a zero-sensitive downstream target is stable. For finite Dirichlet polynomials, the missing target resource can be identified exactly.

For

\[
P_b(s)=\sum_{n=1}^N b_n n^{-s},
\qquad b=(b_1,\ldots,b_N)\in\mathbb C^N,
\]

let `Gamma` be a compact rectifiable Jordan curve bounding a domain `Omega`, and define the boundary-zero discriminant

\[
\Delta_\Gamma
:=
\{c\in\mathbb C^N:\exists z\in\Gamma\text{ with }P_c(z)=0\}.
\]

Write

\[
H_N(x)
:=
\left(\sum_{n=1}^N n^{-2x}\right)^{1/2}.
\]

Then the exact Euclidean distance from `b` to a coefficient vector for which a zero reaches the boundary is

\[
\boxed{
\operatorname{dist}_2(b,\Delta_\Gamma)
=
\min_{z\in\Gamma}
\frac{|P_b(z)|}{H_N(\operatorname{Re}z)}.
}
\]

Consequently, if `P_b` is nonzero on `Gamma` and

\[
\|c-b\|_2
<
\operatorname{dist}_2(b,\Delta_\Gamma),
\]

then `P_c` and `P_b` have exactly the same number of zeros in `Omega`, counted with multiplicity. The threshold is not merely a convenient Rouché bound: it is the **exact coefficient-space distance to the target discontinuity set** where zero count can cease to be locally constant.

Normalize this target margin by

\[
\delta_\Gamma(b)
:=
\frac{\operatorname{dist}_2(b,\Delta_\Gamma)}{\|b\|_2},
\qquad b\ne0.
\]

For AF-289's common-clock quotient, if the nominal decoder satisfies

\[
\frac{\|\widehat b-G_{\sigma_*}b\|_2}{\|b\|_2}
\le
K\left(e^{r(\tau)\log N}-1\right),
\]

then the zero count in the correspondingly translated domain is guaranteed to survive whenever

\[
\boxed{
K\left(e^{r(\tau)\log N}-1\right)
<
\delta_\Gamma(b).
}
\]

Thus source-level timing fidelity and zero-level fidelity are separated by a second, independent resource: **distance of the analytic target to its boundary-zero discriminant**. There is no uniform coefficient-to-zero-count recovery theorem over classes on which this normalized margin can approach zero.

## Exact distance to the boundary-zero discriminant

For fixed `z`, evaluation is the complex-linear functional

\[
L_z(b)=P_b(z)=\sum_{n=1}^N b_n n^{-z}.
\]

Its operator norm on coefficient `ell^2` is

\[
\|L_z\|
=
\left(\sum_{n=1}^N |n^{-z}|^2\right)^{1/2}
=
H_N(\operatorname{Re}z).
\]

The coefficients whose Dirichlet polynomial vanishes at that particular point form the hyperplane `ker L_z`. Standard Hilbert-space projection gives

\[
\operatorname{dist}_2(b,\ker L_z)
=
\frac{|L_z(b)|}{\|L_z\|}
=
\frac{|P_b(z)|}{H_N(\operatorname{Re}z)}.
\]

The minimizing perturbation can be written explicitly. With

\[
v_n(z)=n^{-z},
\]

set

\[
e_n
=-P_b(z)\,
\frac{\overline{v_n(z)}}{\sum_{m=1}^N|v_m(z)|^2}.
\]

Then `P_{b+e}(z)=0` and

\[
\|e\|_2
=
\frac{|P_b(z)|}{H_N(\operatorname{Re}z)}.
\]

Since

\[
\Delta_\Gamma=\bigcup_{z\in\Gamma}\ker L_z,
\]

taking the infimum over `z` gives the displayed distance formula. Compactness of `Gamma` makes the infimum a minimum. If `P_b` has no boundary zero, continuity makes this minimum strictly positive.

This is an exact backward-error statement: the target becomes ill posed precisely when the coefficient vector reaches `Delta_Gamma`.

## Zero count is constant inside the exact distance ball

Let

\[
d_\Gamma(b)
:=
\operatorname{dist}_2(b,\Delta_\Gamma).
\]

For any perturbation `e` with `||e||_2<d_Gamma(b)` and any `z in Gamma`, Cauchy-Schwarz gives

\[
|P_e(z)|
\le
\|e\|_2 H_N(\operatorname{Re}z)
<
d_\Gamma(b)H_N(\operatorname{Re}z)
\le
|P_b(z)|.
\]

Rouché's theorem therefore gives identical zero counts for `P_b` and `P_{b+e}` inside `Omega`, with multiplicity.

Conversely, at distance exactly `d_Gamma(b)` there is a coefficient vector whose polynomial has a zero on `Gamma`. The zero-count target is therefore separated from its ill-posed locus by exactly `d_Gamma(b)`. This is the finite-Dirichlet analogue of the classical condition-number principle that sensitivity is governed by distance to the nearest ill-posed input.

The statement does **not** say every perturbation of norm just above `d_Gamma(b)` changes the zero count. It says that below this radius the count is protected for every perturbation, while at the radius the boundary-collision obstruction is already reachable.

## Common-clock covariance makes the margin a quotient resource

AF-289 uses the unitary coefficient action

\[
G_\sigma b=(b_n n^{-i\sigma})_{n=1}^N.
\]

The associated Dirichlet polynomial obeys the exact identity

\[
P_{G_\sigma b}(s)=P_b(s+i\sigma).
\]

Hence, if `Gamma-i sigma` and `Omega-i sigma` denote vertical translates,

\[
\boxed{
d_{\Gamma-i\sigma}(G_\sigma b)=d_\Gamma(b),
}
\]

and

\[
\#Z(P_{G_\sigma b};\Omega-i\sigma)
=
\#Z(P_b;\Omega).
\]

The first identity follows because vertical translation does not change `Re z`, and therefore does not change the evaluation norm `H_N(Re z)`. The second is just the same analytic function viewed in a translated imaginary coordinate.

Thus zero count in a **vertically tracked window** is equivariant under the common-clock action, while its orbit class is common-clock invariant. This is the concrete target geometry that AF-289's abstract quotient bound requires.

Choose AF-289's minimizing common mode

\[
\sigma_*=\frac{\max_j\tau_j+\min_j\tau_j}{2},
\qquad
r(\tau)=\frac{\max_j\tau_j-\min_j\tau_j}{2}.
\]

Its nominal reconstruction satisfies

\[
\|\widehat b-G_{\sigma_*}b\|_2
\le
K\left(e^{r(\tau)\log N}-1\right)\|b\|_2.
\]

Since

\[
d_{\Gamma-i\sigma_*}(G_{\sigma_*}b)=d_\Gamma(b),
\]

the exact zero-count gate is

\[
K\left(e^{r(\tau)\log N}-1\right)
<
\frac{d_\Gamma(b)}{\|b\|_2}
=
\delta_\Gamma(b).
\]

When it holds, `P_hat` has the same zero count in `Omega-i sigma_*` as `P_b` has in `Omega`.

This is the first concrete completion of AF-289's target-relative timing statement: quotient coefficient accuracy composes with a zero-sensitive analytic target only after paying the target's own distance-to-discriminant margin.

## The evaluation geometry creates an additional breadth dependence

The exact margin weights boundary values by the norm of the evaluation functional. Along a vertical line `Re s=alpha`,

\[
H_N(\alpha)^2=\sum_{n\le N}n^{-2\alpha}.
\]

For fixed `alpha`, the elementary asymptotics are

\[
H_N(\alpha)
\asymp
\begin{cases}
1, & \alpha>1/2,\\
(\log N)^{1/2}, & \alpha=1/2,\\
N^{1/2-\alpha}, & \alpha<1/2.
\end{cases}
\]

Therefore two contours with the same raw minimum value `|P_b|` need not have the same coefficient-space robustness. Evaluation becomes progressively more sensitive as the contour moves left through the `ell^2` critical exponent `1/2`.

This does **not** by itself impose those powers on timing precision, because the actual boundary value `|P_b(z)|` can scale with `N` and with the source. The invariant target resource is the normalized ratio `delta_Gamma(b)`, not `H_N` alone.

## No uniform zero-count modulus exists without a boundary margin

Even at fixed breadth `N=2`, normalized boundary margins can approach zero while zero count changes under arbitrarily small coefficient perturbations.

Take

\[
P_a(s)=1-a2^{-s}
\]

and the fixed disk

\[
\Omega=\{s:|s+1|<1\}.
\]

For `epsilon>0`, let

\[
a_-=2^{-\varepsilon},
\qquad
a_+=2^{\varepsilon}.
\]

The zeros of `P_a` are

\[
s_k=\log_2 a-\frac{2\pi i k}{\log2},
\qquad k\in\mathbb Z.
\]

Thus `P_{a_-}` has exactly one zero in `Omega`, at `s=-epsilon`, while `P_{a_+}` has none there; all `k ne 0` zeros lie far outside the disk. Yet the coefficient vectors

\[
b_-=(1,-2^{-\varepsilon}),
\qquad
b_+=(1,-2^{\varepsilon})
\]

satisfy

\[
\|b_+-b_-\|_2
=2^{\varepsilon}-2^{-\varepsilon}
\longrightarrow0.
\]

Moreover, evaluating at the boundary point `s=0` shows

\[
d_{\partial\Omega}(b_-)
\le
\frac{|1-2^{-\varepsilon}|}{\sqrt2}
\longrightarrow0.
\]

So no positive uniform modulus can turn small coefficient-orbit error into zero-count fidelity on an unrestricted coefficient class. A theorem that does so must supply an independent lower bound on the normalized boundary-zero distance, or an equivalent target-conditioning hypothesis.

## Prior art and novelty assessment

The mathematical ingredients are classical and no general novelty is claimed.

- Rouché's theorem gives the standard preservation of zero count under boundary-dominated holomorphic perturbations. The use here is an exact coefficient-space specialization rather than a new complex-analysis theorem.
- James W. Demmel, **“On condition numbers and the distance to the nearest ill-posed problem,”** *Numerische Mathematik* 51(3), 251–289 (1987), DOI `10.1007/BF01400115`, develops the classical condition-number/distance-to-ill-posedness principle and treats polynomial zero sensitivity among its examples.
- Felipe Cucker, Teresa Krick, Gregorio Malajovich, and Mario Wschebor, **“A Numerical Algorithm for Zero Counting. II: Distance to Ill-posedness and Smoothed Analysis,”** *Journal of Fixed Point Theory and Applications* 6(2), 285–294 (2009), DOI `10.1007/s11784-009-0127-4`, proves a condition-number theorem for zero counting of real polynomial systems. It is neighboring prior art for treating zero count through distance to an ill-posed locus, though its setting and discriminant differ from the finite complex Dirichlet boundary problem here.
- The zeros of finite Dirichlet polynomials belong to the classical theory of exponential sums/polynomials. No novelty is claimed for viewing `sum b_n exp(-s log n)` as an exponential polynomial.

The retained Arithmetic Fidelity result is the **exact channel-specific bridge**. For the finite Dirichlet coefficient geometry inherited from AF-287/AF-289, the boundary-zero discriminant has the explicit distance

\[
\min_{z\in\Gamma}|P_b(z)|/H_N(\operatorname{Re}z),
\]

this distance is exactly covariant under the common-clock gauge, and it composes directly with AF-289's differential-jitter bound. That identifies a target resource which is logically independent of acquisition conditioning and timing spread.

## Boundaries and failure modes

- The result concerns finite Dirichlet polynomials with known coefficient breadth `1,...,N`. It does not recover an infinite Dirichlet series, analytic continuation, the zeta zero divisor, or RH from finite samples.
- `Gamma` is a fixed compact contour and the target is a finite zero count in its vertically tracked orbit. Exact zero ordinates, global zero matching, and zero-free regions over unbounded domains require stronger target metrics.
- The coefficient norm is the standard `ell^2` norm used by AF-287/AF-289. Different source norms replace `H_N` by the dual norm of the evaluation vector.
- The formula prices distance to a **boundary zero**, not distance to a multiple zero in the interior. Interior multiplicity can be badly conditioned for zero location while the total zero count inside a protected contour remains stable.
- The AF-289 composition is sufficient because its coefficient estimate is sufficient. AF-290 does not prove AF-289's residual-jitter bound sharp after quotienting.
- A common timing mode is free only because the target window is translated with the analytic carrier. A fixed-height window retains absolute imaginary-origin provenance and does not descend through this quotient.
- A lower bound on `delta_Gamma(b)` is an additional theorem obligation. It must not be assumed merely because coefficient recovery is stable.

## Decisive audit test

Whenever a proposed arithmetic compression claims that stable recovery of coefficients, moments, samples, or another upstream representation automatically stabilizes a zero-based target, identify the target's ill-posed locus first.

For a finite Dirichlet zero count on `Gamma`, compute or bound

\[
\delta_\Gamma(b)
=
\frac1{\|b\|_2}
\min_{z\in\Gamma}
\frac{|P_b(z)|}{H_N(\operatorname{Re}z)}.
\]

An upstream quotient error `eta` transfers uniformly to the zero count only when `eta<delta_Gamma(b)`. If a proposed source class admits `delta_Gamma ->0`, source-level conditioning alone cannot yield a uniform zero-count theorem. The missing proof obligation is then target separation from the boundary-zero discriminant, not another improvement to the upstream decoder.

## Consequence for the research line

AF-289's target-relative frontier now has one exact analytic instantiation. The information bill has two independent terms:

1. **acquisition quotient error**, controlled in the current finite-prefix channel by differential timing radius `r(tau)` and frame condition number `K`; and
2. **target discriminant margin**, measured exactly by `delta_Gamma(b)` for finite zero count.

A common clock offset costs nothing after vertical-translation quotienting, but residual coefficient error is harmless to zero count only while it remains inside the target's exact distance-to-ill-posedness ball.

This rules out a generic inference that `Theta(1/log N)` quotient coefficient stability automatically gives the same timing law for zero-sensitive targets. The next arithmetic question is sharper: identify natural RH-relevant analytic carriers or finite approximants for which a nontrivial lower bound on an appropriate normalized discriminant margin follows from arithmetic structure, or prove that such margins necessarily collapse with breadth.