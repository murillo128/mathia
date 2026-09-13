# MC-276 — Distributional witness normalization collapses to Christoffel energy

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the witness-normalization problem of `MC-275` and the Christoffel endpoint detector of `MC-268`. On the Boolean cube write

\[
x=(x_1,\ldots,x_k)\in\{-1,+1\}^k,
\qquad
b(x)=\#\{i:x_i=-1\},
\]

and let

\[
\operatorname{NB}(x)=\mathbf 1_{\{b(x)>0\}}
\]

be the nonblind indicator. The blind point is

\[
x_*= (1,\ldots,1).
\]

`MC-275` showed that uniformly approximating `NB` on the full cube has the classical OR approximate-degree barrier. That worst-case obstruction leaves open a seemingly much cheaper escape: approximate `NB` only in distribution, either under the independent-sign/binomial comparator or under the actual arithmetic shell distribution.

For quadratic/L2 approximation this escape can be resolved exactly. Let `\mathcal V_m` be the real Walsh polynomials of degree at most `m`, and let `Q\in\mathcal V_m` satisfy the natural exact blind constraint

\[
Q(x_*)=0.
\tag{1}
\]

Put

\[
P=1-Q,
\qquad P(x_*)=1.
\tag{2}
\]

Under the uniform measure `\mu_k` on the Boolean cube,

\[
\boxed{
\|Q-\operatorname{NB}\|_{L^2(\mu_k)}^2
=
\|P\|_{L^2(\mu_k)}^2-2^{-k}.
}
\tag{3}
\]

The degree-`m` reproducing kernel at `x_*` is

\[
g_m(x)=\sum_{|S|\le m}x_S,
\qquad
Z_m(k)=\sum_{s=0}^m\binom ks,
\tag{4}
\]

with diagonal value `g_m(x_*)=Z_m(k)`. Therefore the Christoffel extremal theorem used in `MC-268` gives

\[
\min_{\substack{P\in\mathcal V_m\\P(x_*)=1}}
\|P\|_2^2
=
\frac1{Z_m(k)},
\tag{5}
\]

and hence

\[
\boxed{
\min_{\substack{Q\in\mathcal V_m\\Q(x_*)=0}}
\|Q-\operatorname{NB}\|_2^2
=
\frac1{Z_m(k)}-2^{-k}.
}
\tag{6}
\]

The unique minimum-norm residual is exactly the existing Christoffel polynomial

\[
P_m(x)=\frac{g_m(x)}{Z_m(k)},
\qquad
Q_m(x)=1-P_m(x).
\tag{7}
\]

Thus generic **distributional L2 normalization is cheap**: unlike the pointwise OR approximation in `MC-275`, it is already solved at degree `m` by the same Christoffel kernel that generated the current endpoint-energy route.

This does not open a new blind-support proof. It collapses back to the existing positive energy. For an arbitrary probability measure `\rho` on the cube with blind mass

\[
a=\rho(\{x_*\}),
\]

every `Q` satisfying `(1)` obeys the exact identity

\[
\boxed{
\|Q-\operatorname{NB}\|_{L^2(\rho)}^2
=
\|1-Q\|_{L^2(\rho)}^2-a.
}
\tag{8}
\]

Apply this to the empirical measure on the actual arithmetic shell

\[
\mathcal T_t=\binom{\mathcal R_y}{t},
\qquad
C=|\mathcal T_t|,
\]

where `A_y(t)` is the number of blind rows. With `Q=Q_m` and the Christoffel energy from `MC-268`,

\[
\mathcal E_{m,y}(t)
=\sum_{T\in\mathcal T_t}P_m(T)^2,
\]

we get

\[
\boxed{
\frac1C\sum_{T\in\mathcal T_t}
\bigl(Q_m(T)-\operatorname{NB}(T)\bigr)^2
=
\frac{\mathcal E_{m,y}(t)-A_y(t)}{C}.
}
\tag{9}
\]

So an empirical L2 theorem saying that `Q_m` approximates nonblindness well controls only the **nonblind part** of the Christoffel energy. The blind mass cancels identically from the approximation error. In the extreme case where every arithmetic row is blind, `Q_m=\operatorname{NB}=0` on every row and the empirical approximation error is exactly zero. Distributional accuracy by itself therefore cannot upper-bound `A_y(t)`.

The surviving phase-sensitive quantity is the signed residual. Summing rather than squaring gives

\[
\boxed{
A_y(t)-L_{m,y}(t)
=
\sum_{T\in\mathcal T_t}
\bigl(Q_m(T)-\operatorname{NB}(T)\bigr),
}
\tag{10}
\]

where

\[
L_{m,y}(t)
:=\sum_{T\in\mathcal T_t}P_m(T)
=
\frac1{Z_m(k_y)}
\sum_{|S|\le m}
\sum_{|T|=t}\chi_T(q_S).
\tag{11}
\]

Unlike the positive energy, `(11)` uses source depth only `m`, not `2m`, and retains cancellation among source supports and target rows. But `(10)` also makes the missing theorem explicit: controlling the low-degree linear form `L_{m,y}` alone does not determine `A_y(t)` unless one also prevents the nonblind signed residual from cancelling an integer blind contribution.

At the live choice `m=t+1`, the independent-sign comparator is nevertheless correctly calibrated for such a signed route. Under `\mu_k`,

\[
\mathbb E P_m=\frac1{Z_m(k)},
\qquad
\mathbb E P_m^2=\frac1{Z_m(k)},
\tag{12}
\]

and `MC-268` gives

\[
\frac{C}{Z_m(k_y)}
=(1+o(1))\frac{m}{k_y}\longrightarrow0.
\tag{13}
\]

Thus an abstract model of independent uniform row signs would have total signed bias of order `C/Z=o(1)` and root-mean-square fluctuation of order `\sqrt{C/Z}=o(1)`. This is only a matched-control benchmark, not arithmetic evidence. It identifies exactly what an arithmetic theorem would have to preserve: **signed cancellation on the nonblind rows**, rather than another pointwise or L2 approximation of the OR endpoint.

Finally, even the requirement that witness weights vanish unless the corresponding coordinate is negative does not obstruct the L2 optimizer. Since `Q_m` is radial, `Q_m(b)` is an ordinary polynomial of degree at most `m` with `Q_m(0)=0`. Hence

\[
h_m(b):=\frac{Q_m(b)}{b}
\tag{14}
\]

is a polynomial of degree at most `m-1`. With

\[
n_i(x)=\frac{1-x_i}{2},
\qquad
\phi_i(x)=n_i(x)h_m(b(x)),
\tag{15}
\]

we have exactly

\[
\boxed{
\phi_i(x)=0\ \text{when }x_i=+1,
\qquad
\sum_{i=1}^k\phi_i(x)=Q_m(x),
\qquad
\deg_{\mathrm W}\phi_i\le m.
}
\tag{16}
\]

The weights `\phi_i` are generally signed; `(16)` is not a positive partition of unity. It shows that **support-respecting signed witness allocation itself is not the missing complexity**. The unresolved information is the arithmetic phase needed to make the aggregate error in `(10)` small without first recovering the full endpoint projector.

No blind relation is excluded, no estimate for `M(X)` follows, and no random-sign independence is asserted for the Legendre shell.

## 1. The L2 identity subtracts the target atom exactly

At the blind point `x_*`, both `Q(x_*)` and `NB(x_*)` vanish. At every nonblind point, `NB=1`, so by `(2)`

\[
Q-\operatorname{NB}=-P.
\]

Therefore for any probability measure `\rho`,

\[
\int (Q-\operatorname{NB})^2\,d\rho
=
\int_{x\ne x_*}P(x)^2\,d\rho(x).
\]

Since `P(x_*)=1`, adding and subtracting the blind atom gives `(8)` immediately. Equation `(3)` is the uniform specialization with `a=2^{-k}`.

This identity is the reason empirical L2 approximation cannot certify nonblindness. The target atom is precisely the part removed from the loss function by imposing the correct value there.

## 2. Christoffel extremality solves the uniform distributional problem

Under uniform measure the Walsh characters `x_S` are an orthonormal basis. The degree-`m` reproducing kernel is

\[
K_m(x,y)=\sum_{|S|\le m}x_Sy_S.
\tag{17}
\]

At `y=x_*`, every `y_S=1`, so

\[
K_m(x,x_*)=g_m(x),
\qquad
K_m(x_*,x_*)=Z_m(k).
\]

For any `P\in\mathcal V_m`, the reproducing property and Cauchy--Schwarz give

\[
|P(x_*)|^2
\le
\|P\|_2^2 Z_m(k).
\tag{18}
\]

When `P(x_*)=1`, this is exactly `(5)`, with equality only for the normalized kernel `P_m=g_m/Z_m`. Substitution into `(3)` proves `(6)`.

This argument is over the entire degree-`m` Walsh space, not merely radial polynomials. The optimizer is radial because the endpoint and uniform product measure are permutation invariant. Therefore allowing a nonradial low-degree distributional selector cannot beat `(6)`.

## 3. The arithmetic empirical loss is the old energy with the answer removed

For the arithmetic shell, every blind row has `P_m(T)=1`. Splitting the energy into blind and nonblind rows gives

\[
\mathcal E_{m,y}(t)
=A_y(t)
+
\sum_{\substack{|T|=t\\T\text{ nonblind}}}P_m(T)^2.
\tag{19}
\]

But the second term in `(19)` is exactly the numerator of the empirical L2 error in `(9)`. Thus replacing the positive endpoint-energy problem by empirical least-squares classification does not create a weaker sufficient target: it simply deletes the very blind contribution that `MC-268` was designed to detect.

A small empirical L2 error can coexist with any blind mass. In particular, the implication

\[
\text{small distributional classification error}
\Longrightarrow
A_y(t)=0
\]

is false without an independent control that reintroduces the uncentered endpoint energy, the blind mass itself, or an equivalent non-cancelling statistic.

This is stronger than saying that generic worst-case OR approximation is expensive. It shows that the most natural weaker replacement is cheap **because its loss is blind to the target atom**.

## 4. Signed aggregation is the only part not absorbed by the positive Christoffel route

Equation `(10)` is the linear counterpart of `(9)`. It follows because on nonblind rows the approximation error is `-P_m(T)` and on blind rows it is zero, while

\[
L_{m,y}(t)
=A_y(t)+
\sum_{T\text{ nonblind}}P_m(T).
\tag{20}
\]

The source expression `(11)` follows from the Walsh formula of `MC-269` before squaring. It uses exactly the flat Hamming-ball source vector, but only once.

This leaves a genuine, narrower frontier. A future theorem could try to show simultaneously that the observable `(11)` is small and that its nonblind contribution has enough signed cancellation that an integer blind count cannot be hidden inside it. Such a theorem would be qualitatively different from:

- a pointwise polynomial approximation to OR, ruled out at low degree by `MC-275`;
- an empirical L2 approximation, which collapses by `(9)`;
- the coefficient-uniform quadratic large-sieve route blocked at the blind-atom threshold by `MC-270`.

The independent-row comparator in `(12)`--`(13)` only confirms that this signed target is calibrated at the right atom scale. The actual Legendre rows share primes, fixed shell weight, reciprocity constraints, and strong algebraic dependence, so comparator cancellation cannot be imported as a theorem.

## 5. Prior art and novelty boundary

The Hilbert-space statement `(5)` is the standard Christoffel/reproducing-kernel extremal principle already used and sourced in `MC-268`. The Krawtchouk/Walsh realization of that kernel is classical Boolean-cube harmonic analysis. Worst-case OR approximate degree is classical and was already audited in `MC-275`.

A targeted literature check through 13 September 2026 found the standard Christoffel point-evaluation extremal framework, Krawtchouk orthogonality, and the established distinction between pointwise approximate degree and distributional/Fourier approximation. No novelty is claimed for those ingredients or for least-squares approximation in a finite-dimensional polynomial space.

The durable Mathia contribution claimed here is only the exact frontier synthesis: once the selector is constrained to be correct on the blind point, its distributional squared error is **Christoffel energy minus blind mass**; the binomial L2 optimum is the same normalized endpoint kernel already present in the research line; and the resulting empirical loss cannot certify the target atom because that atom cancels identically. The support-respecting decomposition `(14)`--`(16)` further shows that signed witness localization does not restore the missing information.

## Boundaries and falsification tests

- **No positive witness partition.** The `\phi_i` in `(15)` may be negative. Positivity or probabilistic allocation would impose additional constraints not analyzed here.
- **No arithmetic-shell L2 lower bound.** Equation `(8)` is exact for every measure, but the minimum over low-degree polynomials for the empirical arithmetic measure is not computed here.
- **No obstruction to signed phase-sensitive theorems.** Equations `(10)`--`(11)` deliberately isolate that route as the surviving alternative.
- **No independence claim.** The comparator calculation after `(12)` is a falsification/calibration control only.
- **No source-degree equivalence to analytic difficulty.** Degree matters here because it is exactly lower-prime support depth in the current Christoffel source hierarchy.
- **No blind-support or RH consequence.** The result only rules out distributional L2 normalization as an independent shortcut.

A direct falsification would be a degree-`m` selector satisfying `(1)` whose uniform L2 error is smaller than `(6)`; by reproducing-kernel extremality this cannot exist. A conceptual falsification would be an empirical-distribution theorem that excludes blind rows while using only the squared classification error in `(9)` and no quantity from which the subtracted blind mass can be recovered; equation `(9)` shows why such a theorem needs additional information.

## Consequence for the research line

The `MC-275` normalization frontier now splits cleanly. Generic pointwise normalization is expensive, but generic distributional L2 normalization is not: the latter is solved by the existing Christoffel kernel and is cheap precisely because the loss discards the blind atom. Therefore moving from worst-case OR approximation to least-squares classification does not evade the endpoint bottleneck.

The useful remaining direction is narrower and phase-sensitive. Either control the original uncentered Christoffel energy strongly enough to preserve the blind atom, or develop a signed low-depth theorem for the linear residual `(10)`--`(11)` that prevents nonblind phase from masking an integer blind contribution. Merely proving that a low-degree witness selector has small empirical L2 error is now an information-losing reformulation rather than progress toward blind exclusion.