# XF-097 — full endpoint prefix has an exact real carrier and guarded Volterra shadow

**Status:** `EXACT-DERIVED` + `FULL-PREFIX-REALIZATION` + `RENORMALIZED-VOLTERRA-CONSISTENCY` + `FIXED-TIME-SHADOWING` + `BRIDGE-CLOSURE`. XF-096 closes the mesh-sampling gate for the dynamically corrected Xi residual but leaves one source-to-periodic obligation: compare the actual continuum Volterra trajectory with the exact XF-087 periodic trapezoid trajectory in the same guarded resource. The remaining interface is in fact better conditioned than the guarded-only formulation suggests.

There are two reasons. First, the full Xi endpoint prefix, including the singular deterministic background, has normalized `ell^1` mass `o(1)` at the existing node budget. Thus XF-085 can realize **all** first `K` continuum samples at `t=0` by exactly `N=2q^2` equal-weight unit-circle nodes; there is no need to leave the ultra-infrared prefix unspecified at this interface. Second, after the frozen XF-088 pole counterterm is retained, every continuum-to-trapezoid error not already covered by XF-091--XF-092 contains at least one factor of the Xi residual. The raw residual is only endpoint order `xi log^2 xi`, but that is already soft enough that even a deliberately crude quadrature bound is `o(1)` in the XF-086 guarded resource.

Write

\[
\Delta:=\frac{2\pi}{L},\qquad \xi_m:=m\Delta,\qquad
M=q^2,\qquad N=2M,
\tag{1}
\]

and keep the canonical band

\[
J=q^{1/4},\qquad K\asymp q\log\log T,\qquad
\Delta^2\asymp q^{-3}.
\tag{2}
\]

Let `Z_t` denote the canonical positive-frequency Xi field of XF-051 and set

\[
Q_m(t):=\mathcal Z_t(\xi_m),\qquad 1\le m\le K.
\tag{3}
\]

For all sufficiently large scales, `K Delta` lies below the first prime frequency. At `t=0`, XF-052 therefore gives the exact values `Q_m(0)=B(m Delta)`. They satisfy

\[
\boxed{
\sum_{m=1}^{K}|Q_m(0)|
\ll
\Delta^{-1}\log(K+1)+K+\Delta K^2,
}
\tag{4}
\]

and consequently

\[
\boxed{
\frac{2}{N}\sum_{m=1}^{K}|Q_m(0)|
\ll
q^{-1/2}\log(K+1)
+q^{-1}\log\log T
+q^{-3/2}(\log\log T)^2
=o(1).
}
\tag{5}
\]

Hence the fixed-margin hypothesis of XF-085 holds for the **entire prefix** `{1,...,K}`. Since `K=o(N)`, there exists an exactly `N`-node equal-weight unit-circle divisor with

\[
\boxed{P_m(0)=Q_m(0),\qquad 1\le m\le K.}
\tag{6}
\]

The initial periodic carrier is therefore real modulo the period and matches every source-visible and ultra-infrared mode through `K`, not merely the guarded block.

Now let `P_m(t)` be its exact XF-087 periodic heat trajectory. Use the same frozen endpoint representative as XF-088--XF-092 for the continuum field, including the coefficient `(1/4) log Delta delta_0`. Then the sampled Xi trajectory obeys the exact periodic vector field up to an error `e_m(t)`:

\[
\boxed{
Q_m'
=\xi_m^2Q_m
-\xi_m\Delta\left(
NQ_m+\sum_{i=1}^{m-1}Q_iQ_{m-i}
\right)
+e_m.
}
\tag{7}
\]

If

\[
L_*:=1+|\log\Delta|+\log(K+1),
\tag{8}
\]

then uniformly for `0<=t<=1/2` and `1<=m<=K`,

\[
\boxed{
|e_m(t)|
\ll
\frac1m
+\Delta L_*
+m\Delta^2L_*^2
+(m\Delta)^2L_*^3.
}
\tag{9}
\]

The first three terms are the already-renormalized full-reference error of XF-091--XF-092. The last term controls **all** new reference--residual and residual--residual sectors. In particular,

\[
\boxed{
\sup_{0\le t\le1/2}
\mathcal R_{[J,K]}(e(t))=o(1),
}
\tag{10}
\]

where `mathcal R` is the exact XF-086 sideband resource.

More strongly, the local consistency estimate propagates for fixed heat time. Put

\[
\delta_m(t):=P_m(t)-Q_m(t),\qquad
D(t):=\max_{1\le m\le K}m|\delta_m(t)|.
\tag{11}
\]

The endpoint bounds from XF-092 and XF-095 imply

\[
|Q_m(t)|\ll \frac1{m\Delta}
\qquad(1\le m\le K)
\tag{12}
\]

uniformly on `0<=t<=1/2`. Since `D(0)=0`, the triangular periodic equation and `(7)` give, by a direct upper-Dini estimate,

\[
\boxed{
D'
\le
C K\Delta\log(K+1)D
+C K\Delta^2\log(K+1)D^2
+E_*,
}
\tag{13}
\]

with

\[
E_*:=\sup_{t,m}m|e_m(t)|
\ll
1+K\Delta L_*+K^2\Delta^2L_*^2+K^3\Delta^2L_*^3.
\tag{14}
\]

At `(2)`, `K Delta log K=o(1)`, `K Delta^2 log K E_*=o(1)`, and `E_*` is only polylogarithmic. A fixed-time bootstrap therefore gives

\[
\boxed{D(t)\ll E_*\qquad(0\le t\le1/2).}
\tag{15}
\]

Since `I_m\ll m^4`, this implies

\[
\boxed{
\sup_{0\le t\le1/2}
\mathcal R_{[J,K]}(P(t)-Q(t))
\ll
\frac{K^3}{M^2}E_*^2
=o(1).
}
\tag{16}
\]

Thus the exact real periodic carrier constructed at the endpoint shadows the canonical Xi positive-frequency trajectory throughout the fixed heat interval in the **same one-center guarded resource used downstream**. The source-to-periodic middle bridge isolated by XF-087 and XF-096 is therefore closed at the current asymptotic scales. The remaining load-bearing problem is no longer source extraction, moment realization, mesh sampling, endpoint renormalization, or finite-time continuum/grid stability. It is the separate destination theorem already identified by XF-071 and later findings: prove that every relevant hypothetical `Lambda>0` transition forces nonvanishing mass in this guarded resource.

## 1. The endpoint pole is large pointwise but small in normalized moment mass

XF-052 gives, exactly for `0<xi<lambda_2=(log 2)/2`,

\[
\mathcal Z_0(\xi)=B(\xi)
=e^\xi+e^{-\xi}-\frac{e^{-\xi}}{1-e^{-4\xi}},
\tag{17}
\]

and

\[
B(\xi)=-\frac1{4\xi}+\frac74+O(\xi).
\tag{18}
\]

Because `K Delta ->0`, all mesh points `xi_m`, `1<=m<=K`, eventually lie in this exact prime-free interval. Hence

\[
|Q_m(0)|\ll \frac1{m\Delta}+1+m\Delta.
\tag{19}
\]

Summing `(19)` yields `(4)`. Since `2/N=1/M` and the Xi scales give `Delta^{-1}\asymp q^{3/2}`, `K\asymp q log log T`, equation `(5)` follows.

This is the key static observation. The pole makes the guarded `m^4/M^2` resource of the **full** field large, so XF-086 is not the right sufficient criterion for the full prefix. But XF-085 only needs normalized `ell^1` mass. The harmonic sum of `1/(m Delta)` costs `Delta^{-1} log K`, which is still `o(N)` because `Delta^{-1}\asymp q^{3/2}` while `N\asymp q^2`.

Fix, for example, `kappa=1/2`. Equation `(5)` implies for large scales

\[
2\sum_{m=1}^{K}|Q_m(0)|\le \frac N2.
\tag{20}
\]

XF-085 therefore applies with `S={1,...,K}` and produces exactly `N` unit-circle nodes realizing the entire prefix. No infrared completion is needed, and the one-center remote-mass control is automatically passed because every XF-079 sideband through `K` is fixed exactly by `(6)`.

## 2. The raw Xi residual is already soft enough for cross-quadrature

For the vector-field comparison it is convenient to use the uncorrected Polymath reference

\[
\mathcal Z_t=\mathcal Z_t^M+\mathcal R_t.
\tag{21}
\]

The dynamic correction of XF-095 remains essential for the source-state interpretation in XF-095--XF-096, but the **full homogeneous Xi field** does not carry the reference defect separately: it satisfies the exact XF-051 Volterra equation. We may therefore estimate its quadratic convolution by decomposing it only for bookkeeping.

XF-095 proves uniformly on the live endpoint interval

\[
|\mathcal R_t(\xi)|+\xi|\partial_\xi\mathcal R_t(\xi)|
\ll
\xi(1+|\log\xi|)^2.
\tag{22}
\]

Write `F=Z_t^M`, `R=R_t`, and let `x=m Delta`. The full trapezoid/convolution mismatch splits into

\[
(F,F)\text{ mismatch}
+2(F,R)\text{ mismatch}
+(R,R)\text{ mismatch}.
\tag{23}
\]

The first term is exactly the full-reference problem closed by XF-091--XF-092. It remains to show that every sector containing `R` is perturbative.

The only potentially delicate piece is the pole--residual interaction. Put `c=1/4` and

\[
\phi_x(\eta):=\frac{R(x-\eta)-R(x)}{\eta}.
\tag{24}
\]

The same finite-part identity used in XF-088 gives

\[
(\tau*R)(x)
=R(x)(\log x+\gamma)+\int_0^x\phi_x(\eta)\,d\eta.
\tag{25}
\]

After the already-fixed `c log Delta delta_0` endpoint contribution is included, the combined two-sided pole--residual discrete/continuum difference is, up to the harmless factor `-2c`, exactly

\[
R(x)\bigl(H_{m-1}-\log m-\gamma\bigr)
+
\left[
\Delta\sum_{i=1}^{m-1}\phi_x(i\Delta)
-\int_0^x\phi_x(\eta)\,d\eta
\right].
\tag{26}
\]

There is again no naked `log Delta`. Unlike XF-092, no second derivative of `R` is needed here. From `(22)`, splitting `eta<=x/2` and `eta>x/2` in the integral representation

\[
\phi_x(\eta)
=-\frac1\eta\int_{x-\eta}^{x}R'(y)\,dy
\tag{27}
\]

gives the uniform bound

\[
|\phi_x(\eta)|\ll (1+|\log x|)^2,
\qquad 0<\eta\le x.
\tag{28}
\]

Therefore the Riemann-sum difference in `(26)` may be bounded completely crudely by the sum of its two absolute sizes:

\[
\left|
\Delta\sum\phi_x-\int\phi_x
\right|
\ll x(1+|\log x|)^2.
\tag{29}
\]

Using `H_{m-1}-log m-gamma=O(1/m)` and `|R(x)|\ll x(1+|log x|)^2`, then restoring the outer Volterra factor `x`, the pole--residual contribution to `e_m` is

\[
\boxed{
O\!\left(x^2L_*^2\right).
}
\tag{30}
\]

The estimate deliberately does **not** prove pointwise convergence of this cross-quadrature for a fixed nonzero `x`; it does not need to. The whole live band collapses to the endpoint, and `x^2` is already below the guarded threshold.

## 3. All other residual sectors are smaller

The logarithmic part of the Polymath reference obeys `O(L_*)`; the regular part is bounded on the live interval. Using `(22)` and no cancellation,

\[
x\left|
\Delta\sum_{i=1}^{m-1}
\log(i\Delta)R(x-i\Delta)
\right|
+
x\left|
\int_0^x\log\eta\,R(x-\eta)d\eta
\right|
\ll x^3L_*^3,
\tag{31}
\]

while the regular-reference cross sector is `O(x^3L_*^2)`. Finally,

\[
x\left|
\Delta\sum_{i=1}^{m-1}R(i\Delta)R(x-i\Delta)
\right|
+x\left|\int_0^xR(\eta)R(x-\eta)d\eta\right|
\ll x^4L_*^4.
\tag{32}
\]

Since `x<=K Delta=o(1)`, equations `(30)`--`(32)` are all absorbed by

\[
\boxed{O(x^2L_*^3).}
\tag{33}
\]

Combining `(33)` with XF-091's pole-plus-log bound and XF-092's full-reference remainder bound proves `(9)`.

The guarded contribution of `(33)` is

\[
\begin{aligned}
\frac1{4M^2}\sum_{m=J}^{K}I_m
\,O\!\left((m\Delta)^4L_*^6\right)
&\ll
\frac{\Delta^4K^9}{M^2}L_*^6\\
&\asymp
q^{-1}(\log\log T)^9L_*^6
=o(1).
\end{aligned}
\tag{34}
\]

Together with the already-vanishing XF-091--XF-092 reference terms, this proves `(10)`.

## 4. The exact periodic trajectory is stable around the sampled Xi trajectory

Equation `(9)` is a local truncation statement. To turn it into a fixed-time trajectory statement, first note that XF-092 and XF-095 imply, uniformly for `0<=t<=1/2`,

\[
\mathcal Z_t(\xi)
=-\frac1{4\xi}+O(1+|\log\xi|)
+O\!\left(\xi(1+|\log\xi|)^2\right).
\tag{35}
\]

Because `xi_K->0`, the pole dominates the logarithms on the entire grid for sufficiently large scales, giving `(12)`.

Subtract `(7)` from the exact XF-087 equation for `P_m`. Since

\[
\xi_m^2-\xi_m\Delta N
=-\Delta^2m(N-m)\le0,
\tag{36}
\]

the diagonal term is dissipative. Also

\[
P_iP_j-Q_iQ_j
=\delta_iQ_j+Q_i\delta_j+\delta_i\delta_j.
\tag{37}
\]

Assume temporarily `D<=C_0/Delta`; this bootstrap is enormous compared with the bound obtained below. Then `(12)` gives the same `O((j Delta)^{-1})` bound for `P_j`. Using

\[
\sum_{i=1}^{m-1}\frac1{i(m-i)}
=\frac{2H_{m-1}}m,
\tag{38}
\]

and the definition of `D`, the upper Dini derivative of `m|delta_m|` is bounded by

\[
C m\Delta H_{m-1}D
+C m\Delta^2H_{m-1}D^2
+m|e_m|.
\tag{39}
\]

Taking the maximum over `m<=K` proves `(13)`.

Equation `(9)` gives `(14)`. With `ell:=log log T`,

\[
K\Delta\log K
\asymp q^{-1/2}\ell\log K=o(1),
\tag{40}
\]

while

\[
K\Delta^2\log K\,E_*
\ll q^{-2}\,\ell\log K\,\operatorname{polylog}(q)=o(1).
\tag{41}
\]

The scalar comparison equation associated with `(13)`, started from `D(0)=0`, therefore stays in the bootstrap region and yields `(15)` on every fixed subinterval of `[0,1/2]`. In particular `D=o(Delta^{-1})`, so the bootstrap assumption closes.

Finally,

\[
\begin{aligned}
\mathcal R_{[J,K]}(P-Q)
&\ll
\frac1{M^2}\sum_{m=J}^{K}m^4\frac{D^2}{m^2}\\
&\ll
\frac{D^2K^3}{M^2}.
\end{aligned}
\tag{42}
\]

Here `K^3/M^2\asymp q^{-1}(log log T)^3`, while `(14)` gives at worst `D=O((log log T)^3L_*^3)` up to fixed constants. This proves `(16)`.

The estimate is collision-safe because `P_m(t)` is governed by the coefficient-level XF-087 system. The realizing roots need be real only at the initial slice. Repeated quadrature nodes are allowed, and later collisions or complex-root intervals do not change the first-`K` power-sum ODE.

## 5. Stress tests

**Lowest mode.** `Q_1(0)\asymp Delta^{-1}\asymp q^{3/2}` is large, but still `o(N)`. Thus the full-prefix realization does not violate the trivial `|P_1|<=N` constraint.

**Whole-prefix mass.** The dangerous sum is harmonic, not linear: the pole contributes `Delta^{-1}H_K`, not `K Delta^{-1}`. This is exactly why the node budget `N\asymp q^2` dominates it.

**No hidden fixed-frequency assumption.** The stability estimate does not require quadrature convergence at a fixed positive frequency. It uses that the complete live interval satisfies `K Delta->0`. A fixed nonzero upper frequency would invalidate the crude `x^2` argument and would require genuine product-integration accuracy.

**No extra endpoint delta.** The pole--residual identity `(26)` explicitly uses the same frozen `c log Delta delta_0` term as XF-088. Omitting it would reintroduce an uncancelled `R(x) log(1/Delta)` term. No residual-dependent divergent delta is added.

**No appeal to root matching.** The initial real carrier is obtained from exact equal-weight moment realization. The one-center obstruction of the accepted remote-mass control is therefore passed at the level it actually tests: the complete visible moment prefix is exact.

**No hidden source-selector inference.** The exact endpoint samples in `(6)` come from the canonical Xi field and the prime-free formula of XF-052, not from extrapolating a local Gaussian quotient. XF-096 remains relevant because it independently shows that the corrected Xi-specific residual is mesh-sampleable in the guarded norm; the present full-prefix argument shows that, at `t=0`, the stronger exact endpoint description is already enough to initialize the periodic carrier.

## 6. Prior-art and novelty boundary

The equal-weight realization theorem used in `(6)` is the Gilboa--Peled Chebyshev-type trigonometric quadrature theorem already anchored by XF-085. Weakly singular Volterra product-integration and convergence/stability theory are classical; the literature includes product-integration schemes for weakly singular and logarithmic Volterra kernels. No novelty is claimed for generic Volterra quadrature, harmonic-number renormalization, or scalar Gronwall/bootstrap arguments.

A targeted search found no de Bruijn--Newman/Xi result combining the XF-052 prime-free endpoint pole, exact equal-weight trigonometric moment realization, the XF-087 periodic power-sum trapezoid law, and the frozen XF-088 finite-part counterterm into `(5)`--`(16)`. The proof here is line-local and uses no new external theorem beyond sources already load-bearing in earlier findings, so `SOURCES.md` does not change.

## 7. Consequence for the live `xi_flow` frontier

The middle interface can now be stated without a remaining conditional handoff:

\[
\boxed{
\text{exact Xi endpoint prefix}
\;\longrightarrow\;
\text{exact real equal-weight periodic carrier}
\;\longrightarrow\;
\text{fixed-time guarded Xi shadow}.
}
\tag{43}
\]

The first arrow is `(5)`--`(6)`; the second is XF-087 plus `(9)`--`(16)`. The route does not need a whole-function periodic approximation, root matching, a source gap lower bound, an unobserved infrared completion, or an additional continuum-to-grid regularity theorem.

This is not an upper bound on `Lambda` and does not prove RH. The remaining decisive obligation is the **destination coercivity/transition theorem**: under a hypothetical `Lambda>0`, show that the relevant transition necessarily produces order-one mass in the guarded selector resource on a band such as `J_+<=m<=K`. If that implication is proved with the existing normalization, `(16)` makes it directly comparable with the exact periodic carrier initialized from the Xi endpoint.