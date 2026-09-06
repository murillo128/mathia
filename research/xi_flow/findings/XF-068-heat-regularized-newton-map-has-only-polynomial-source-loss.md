# XF-068 — heat-regularized Newton map has only polynomial source loss

**Status:** `EXACT-DERIVED` + `QUANTITATIVE-VIETA-BRIDGE` + `COLLISION-SAFE` + `STRUCTURAL/REPAIR`. XF-067 diagonalizes the full periodic zero heat flow in Vieta coordinates and identifies the remaining algebraic concern: when the controlled harmonic index grows to `K\asymp q\log\log T`, could the triangular Newton map amplify small source-controlled power sums by a combinatorial factor large enough to overwhelm the Cauchy heat clock?

It cannot. There is a dimension-free majorant for the forward Newton map, and after any fixed positive heat time the inverse Newton map loses only a polynomial factor in the reciprocal Cauchy rate. In particular, if the raw periodic power sums on the source cone are uniformly `o(1)`, then every corresponding low Vieta coefficient is uniformly `o(1)` **independently of how large `K` is**. If those raw power sums have the arbitrary fixed logarithmic decay available for the localized Xi selectors in XF-059, then after fixed positive periodic heat time the reconstructed power sums retain arbitrary fixed logarithmic decay as well.

The missing bridge is therefore not combinatorial conditioning of Newton identities. It is the geometric/localization step that converts the actual localized Xi selector into the raw power sums of a periodic carrier, together with the separate transition-state input needed downstream.

## 1. Uniformly small power sums give uniformly small Vieta coefficients

Let

\[
u_1,\ldots,u_N\in\mathbb C,
\qquad
P_m:=\sum_{j=1}^N u_j^m,
\qquad
E_k:=e_k(u_1,\ldots,u_N),
\tag{1}
\]

and fix `1\le K\le N`. Put

\[
\varepsilon_K:=\max_{1\le m\le K}|P_m|.
\tag{2}
\]

The elementary-symmetric generating series is the formal identity

\[
\sum_{k=0}^N E_k z^k
=
\prod_{j=1}^N(1+u_jz)
=
\exp\!\left(
\sum_{m\ge1}(-1)^{m-1}\frac{P_m}{m}z^m
\right).
\tag{3}
\]

For the coefficient of `z^k`, only `P_1,\ldots,P_k` matter. Taking coefficientwise absolute values in the exponential therefore gives, for every `1\le k\le K`,

\[
|E_k|
\le
[z^k]\exp\!\left(
\varepsilon_K\sum_{m\ge1}\frac{z^m}{m}
\right)
=
[z^k](1-z)^{-\varepsilon_K}.
\tag{4}
\]

Hence

\[
\boxed{
|E_k|
\le
\frac{(\varepsilon_K)_k}{k!},
\qquad 1\le k\le K,
}
\tag{5}
\]

where `(a)_k=a(a+1)\cdots(a+k-1)` is the rising factorial. In the source-small regime `0\le\varepsilon_K\le1`, each factor after the first satisfies `\varepsilon_K+j\le j+1`, so

\[
\boxed{
\max_{1\le k\le K}|E_k|
\le \varepsilon_K.
}
\tag{6}
\]

There is no dependence on `N`, `K`, a root-separation parameter, or root reality. Thus the feared binomial estimate `|E_k|\le {N\choose k}` from XF-067 is irrelevant once the **power sums themselves** are uniformly source-small. The triangular map does not turn an `o(1)` cone of raw power sums into large low Vieta coordinates.

Equation (5) is also stronger than a recursive Gronwall estimate. It keeps the exact partition combinatorics of Newton's identities and shows that all nonlinear products of small power sums sum to the generalized-binomial coefficient rather than to a combinatorial factor depending on `N`.

## 2. Periodic heat makes the inverse map quantitatively tame

Now use the periodic zero heat flow of XF-067. Let `t_1=t_0+\tau` with fixed `\tau>0`. The normalized Vieta coefficients evolve exactly by

\[
E_k(t_1)
=
E_k(t_0)e^{-\delta_k\tau},
\qquad
\delta_k=
\frac{4\pi^2}{L^2}k(N-k).
\tag{7}
\]

Assume `K\le N/2` and define the per-index damping parameter

\[
\beta
:=
\frac{4\pi^2\tau}{L^2}(N-K).
\tag{8}
\]

Then for `1\le k\le K`,

\[
\delta_k\tau\ge\beta k.
\tag{9}
\]

Suppose the initial raw power sums obey

\[
\max_{1\le m\le K}|P_m(t_0)|\le\varepsilon\le1.
\tag{10}
\]

By (6) and (9),

\[
|E_k(t_1)|\le\varepsilon e^{-\beta k}.
\tag{11}
\]

To return to power sums, set

\[
F_K(z):=1+\sum_{k=1}^K E_k(t_1)z^k.
\tag{12}
\]

For every `m\le K`, the coefficient of `z^m` in `\log F_K` agrees with the coefficient in the full Vieta polynomial, because that coefficient uses only `E_1,\ldots,E_m`. Thus

\[
[z^m]\log F_K(z)
=
(-1)^{m-1}\frac{P_m(t_1)}m.
\tag{13}
\]

Choose

\[
r=e^{\beta/2},
\qquad
\eta:=
\frac{\varepsilon}{e^{\beta/2}-1}.
\tag{14}
\]

On `|z|=r`, equation (11) gives

\[
|F_K(z)-1|
\le
\varepsilon\sum_{k\ge1}e^{-\beta k/2}
=
\eta.
\tag{15}
\]

If `\eta\le1/2`, the logarithm is analytic on and inside that circle and

\[
|\log F_K(z)|
\le -\log(1-\eta)
\le2\eta.
\tag{16}
\]

Cauchy's coefficient estimate applied to (13) yields the explicit inverse bound

\[
\boxed{
|P_m(t_1)|
\le
2m\eta e^{-\beta m/2},
\qquad 1\le m\le K.
}
\tag{17}
\]

In particular, for `0<\beta\le1`, using `e^{\beta/2}-1\ge\beta/2` and `\sup_{x>0}xe^{-\beta x/2}=2/(e\beta)`, one gets

\[
\boxed{
\max_{1\le m\le K}|P_m(t_1)|
\le
\frac{8}{e}\frac{\varepsilon}{\beta^2},
}
\tag{18}
\]

provided `\varepsilon/(e^{\beta/2}-1)\le1/2`.

So the return from diagonal Vieta coordinates to the raw positive-frequency root sums has only a `\beta^{-2}` loss after positive heat time. No exponential or binomial loss in the growing mode index appears.

## 3. On the Xi memory scales the loss is only a fixed power of `log T`

Use the XF-062--XF-067 scales

\[
q\asymp\log^2T,
\qquad
M=q^2,
\qquad
N=2M,
\qquad
s\asymp\frac1{\log T},
\qquad
L=Ns\asymp\log^3T,
\tag{19}
\]

and the full slow cone

\[
K_T\le Cq\log\log T.
\tag{20}
\]

Then `K_T/N\to0`, so `K_T\le N/2` eventually, and for every fixed `\tau>0`,

\[
\boxed{
\beta_T
=
\frac{4\pi^2\tau(N-K_T)}{L^2}
\asymp_\tau \frac1q.
}
\tag{21}
\]

Consequently (18) costs only

\[
\beta_T^{-2}=O_\tau(q^2)=O_\tau((\log T)^4).
\tag{22}
\]

Suppose a future localization theorem converts the source selector into raw periodic power sums with the same type of rapid logarithmic bound proved for the localized Xi statistic in XF-059, namely that for every fixed `B>0`,

\[
\max_{1\le m\le K_T}|P_m(t_0)|
=O_B((\log T)^{-B}).
\tag{23}
\]

Then (5)--(6) give the same bound for all low Vieta coordinates at `t_0`, while (17)--(22) imply that for every fixed `A>0`, after any fixed positive heat time `\tau`,

\[
\boxed{
\max_{1\le m\le K_T}|P_m(t_0+\tau)|
=O_{A,\tau}((\log T)^{-A}).
}
\tag{24}
\]

One simply chooses the source exponent `B>A+4`; the smallness condition in (14) is then automatic because `\beta_T\asymp q^{-1}`.

The same observation covers every fixed polynomially weighted Vieta energy. From (11), for fixed `r\ge0`,

\[
\sum_{k=1}^{K_T}k^r|E_k(t_1)|^2
\le
\varepsilon^2
\sum_{k\ge1}k^r e^{-2\beta_Tk}
\ll_r
\varepsilon^2\beta_T^{-(r+1)}.
\tag{25}
\]

Thus arbitrary fixed logarithmic source decay beats any fixed derivative weight used on the `K_T\asymp q\log\log T` cone. The growing Newton map does not consume the XF-059 source margin.

## 4. Stress tests and boundaries

The conclusion depends on **uniform raw power-sum smallness**, not on bounded root displacement alone. This distinction is essential. A bounded perturbation of the arithmetic lattice gives only the elementary estimate `|P_m|=O(m)` for `m\ll N`, which inserted into Newton's identities does not yield (6). XF-068 therefore does not replace the source selector by a geometric bounded-displacement hypothesis.

Positive heat time is also load-bearing for the quantitative inverse estimate. At `\tau=0`, one starts with the raw power sums themselves and no inverse reconstruction is needed; as `\tau\downarrow0`, the auxiliary radius in (14) collapses to one and the explicit `\beta^{-2}` estimate degenerates. The theorem is tailored to the fixed-positive-time regularization already used in XF-062--XF-066, not to a uniform `\tau\to0` statement.

No assumption of real roots, simple roots, or a zero-separation bound appears. Equations (3), (5), and (13) are symmetric polynomial identities, and the heat evolution (7) is coefficient-level. Hence the estimate remains valid through collisions and through complex-root intervals of the periodic carrier.

## 5. Prior-art and novelty boundary

Newton--Girard identities and the exponential generating relation between elementary symmetric functions and power sums are classical. The prior-art audit found the standard symmetric-function formulation and modern expositions of the same algebraic bridge; no novelty is claimed for (3) itself or for coefficient extraction from it. XF-067 already used Newton identities qualitatively.

The line-specific contribution here is the **quantitative majorization at the Xi scaling**: source-small raw power sums produce low Vieta coordinates with no `K`-dependent amplification, and exact periodic heat regularization makes the inverse map cost only `O(q^2)` on the full `K\lesssim q\log\log T` slow cone. This removes the combinatorial-conditioning concern explicitly left open in XF-067. No new load-bearing external theorem is required, so `SOURCES.md` need not change.

## 6. Consequence for `xi_flow`

XF-067 left two distinct periodic-bridge concerns bundled together: the conditioning of the growing Newton transform and the error in replacing the localized Xi window by a periodic carrier. XF-068 separates them. **The Newton transform is quantitatively benign once the raw power sums inherit the source selector's uniform smallness.** Even the return map after fixed heat time loses only a fixed power of `log T`, which the XF-059 source margin can absorb.

What remains is genuinely geometric/source-local: prove that the localized moving-line measurements of the actual Xi zero field control the raw periodic power sums with sufficiently small error on `m\le Cq\log\log T`, or exhibit a localization/periodization defect that prevents such a conversion. Separately, a positive-`Lambda` transition still has to be connected to a nontrivial post-heat state of the kind detected by XF-064--XF-066. XF-068 proves neither that localization theorem nor the transition implication, and therefore gives no upper bound on `Lambda` and no consequence for RH by itself.
