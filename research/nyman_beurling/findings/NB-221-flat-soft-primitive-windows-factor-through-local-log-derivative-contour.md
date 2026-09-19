# NB-221 — Flat soft primitive windows factor through one local logarithmic-derivative contour

**Date:** 2026-09-19  
**Status:** `EXACT-DERIVED + ANALYTIC-TRANSPORT + LOCAL-CONTOUR + ZETA-PRIMITIVE + LOG-DERIVATIVE-REDUCTION + VINOGRADOV-KOROBOV + METHOD-BOUNDARY + NB-220-REFINEMENT`.

`NB-218`--`NB-220` isolated a potentially useful escape from the absolute Mellin-reconstruction tariff: keep the zeta primitive and its matched shell kernel coupled, localize vertically with a flat analytic soft window, and use the resulting entire source-defined continuation rather than bounding the primitive and kernel separately. `NB-220` left one specific analytic question open: can that continued pairing be connected back to local zero-free-region data on the left of `Re(s)=1` without importing remote zeta singularities or paying the old absolute-value tariff?

For every **fixed** primitive depth, the answer is yes, but the result also exposes a method boundary. Repeated integration by parts factors the soft-windowed `j`-fold primitive pairing into one leading convolution with

\[
P_0(s)=-\frac{\zeta'(s)}{\zeta(s)}
\]

plus correction terms in which at least one derivative falls on the flat window. Those corrections are `O(log X V^(-2M-2))` on the safe `1+` line. The leading logarithmic-derivative convolution can then be moved left on the **finite** rectangle `|v|<=|t|/2`: throughout that rectangle the physical height stays comparable to `|t|`, so a Vinogradov--Korobov zero-free strip excludes every zeta zero there, while the zeta pole at height zero lies outside. The omitted vertical tails stay on `Re(s)>1`, where absolute convergence controls them. No global contour and no remote zero-residue sum are needed.

Consequently the source-side continuation problem left by `NB-220` can be closed locally. But after the transport, the leading term is exactly the same local `-zeta'/zeta` object used in `NB-212`. Applying the existing pointwise Vinogradov--Korobov logarithmic-derivative bound therefore gives again

\[
Q^2\exp\!\left[-c\frac{X}{Q^{2/3}(\log Q)^{1/3}}\right],
\qquad Q=\log(10+|t|),
\]

up to arbitrarily small algebraic window errors. Thus finite zeta primitivization plus flat analytic localization solves the **representation/transport** obstruction but does not by itself improve the log-squared diagonal corridor. Any improvement on this route must now exploit cancellation inside the transported carrier-frequency `P_0` integral, rather than relying on primitive depth or entire continuation alone.

## 1. Every fixed primitive depth has the same leading logarithmic-derivative term

Keep the notation of `NB-220`. Fix an integer `j>=1`, constants `r>0`, `Delta>0`, and

\[
\phi\in C_c^\infty((0,\Delta);\mathbb C).
\]

For large `X`, set

\[
\sigma_X:=1+\frac rX,
\qquad
h_X(u):=\phi(u-X),
\]

and introduce the unweighted shell transform

\[
L_X(v)
:=
\int_0^\infty h_X(u)e^{ivu}\,du.
\tag{1}
\]

The `j`-weighted kernel from `NB-218`--`NB-220` is

\[
K_{j,X}(v)
:=
\int_0^\infty u^j h_X(u)e^{ivu}\,du.
\tag{2}
\]

Because differentiation in `v` inserts powers of `iu`,

\[
\boxed{
K_{j,X}(v)=i^{-j}\frac{d^j}{dv^j}L_X(v).
}
\tag{3}
\]

For `k>=1`, define on `Re(s)>1`

\[
P_k(s)
:=
\sum_{n\ge2}
\frac{\Lambda(n)}{(\log n)^k}n^{-s},
\tag{4}
\]

and put

\[
P_0(s):=-\frac{\zeta'(s)}{\zeta(s)}.
\tag{5}
\]

Then

\[
P_k'(s)=-P_{k-1}(s),
\]

so for real `v`

\[
\frac{d^m}{dv^m}P_j(s+iv)
=(-i)^mP_{j-m}(s+iv)
\qquad(0\le m\le j).
\tag{6}
\]

Let the flat Gaussian window be exactly the one in `NB-220`,

\[
W_M(z)
=
e^{-z^2}
\sum_{\ell=0}^{M}\frac{z^{2\ell}}{\ell!},
\qquad
w_V(v):=W_M(v/V),
\tag{7}
\]

with `V>=1`. The localized `j`-primitive pairing is

\[
I_{j,X,V,M}(s)
:=
\frac1{2\pi}
\int_{\mathbb R}
 w_V(v)K_{j,X}(v)P_j(s+iv)\,dv,
\qquad \Re(s)>1.
\tag{8}
\]

The shell transform `L_X` is Schwartz on the real line, uniformly after factoring its carrier, while `w_V` is Gaussian and each `P_k` is bounded on every fixed half-plane to the right of one. Hence all boundary terms vanish when (3) is integrated by parts `j` times. Using Leibniz and (6),

\[
\begin{aligned}
I_{j,X,V,M}(s)
&=
\frac{i^j}{2\pi}
\int_{\mathbb R}
L_X(v)
\frac{d^j}{dv^j}
\bigl(w_V(v)P_j(s+iv)\bigr)\,dv\\
&=
\frac1{2\pi}
\sum_{k=0}^{j}
\binom jk i^k
\int_{\mathbb R}
L_X(v)w_V^{(k)}(v)P_k(s+iv)\,dv.
\end{aligned}
\tag{9}
\]

Therefore

\[
\boxed{
I_{j,X,V,M}(s)
=A_{0,X,V,M}(s)
+
\sum_{k=1}^{j}
\binom jk i^k A_{k,X,V,M}(s),
}
\tag{10}
\]

where

\[
A_{k,X,V,M}(s)
:=
\frac1{2\pi}
\int_{\mathbb R}
L_X(v)w_V^{(k)}(v)P_k(s+iv)\,dv,
\tag{11}
\]

and in particular

\[
\boxed{
A_{0,X,V,M}(s)
=
\frac1{2\pi}
\int_{\mathbb R}
L_X(v)w_V(v)
\left(-\frac{\zeta'}{\zeta}\right)(s+iv)\,dv.
}
\tag{12}
\]

The coefficient of the `k=0` term is exactly one for every `j`. Thus all fixed primitive depths have the **same** leading logarithmic-derivative convolution. Primitive depth survives only in derivatives of the window.

For `j=1`, (10) reduces to the transparent identity

\[
I_{1,X,V,M}(s)
=
A_{0,X,V,M}(s)
+
\frac{i}{2\pi}
\int_{\mathbb R}
L_X(v)w_V'(v)\log\zeta(s+iv)\,dv.
\tag{13}
\]

This also fixes the sign: differentiating `log zeta(s+iv)` in `v` gives `-iP_0(s+iv)`.

## 2. Flatness makes every primitive correction algebraically negligible

The defining Taylor cancellation of `W_M` is

\[
1-W_M(z)=O_M(z^{2M+2})
\qquad(z\to0).
\tag{14}
\]

Hence, for `1<=k<=2M+2`,

\[
w_V^{(k)}(v)
=
V^{-k}W_M^{(k)}(v/V)
=
O_{M,k}\!\left(
V^{-(2M+2)}|v|^{2M+2-k}
\right)
\tag{15}
\]

for `|v|<=V`. For `|v|>V`, Gaussian decay of `W_M` together with arbitrary Schwartz decay of `L_X` gives the same power of `V` after integration. Since

\[
L_X(v)=e^{iXv}\widehat\phi(v),
\tag{16}
\]

with `widehat phi` a fixed Schwartz function under the present Fourier convention, one obtains, for every fixed `j` with `j<=2M+2`,

\[
\boxed{
\int_{\mathbb R}
|L_X(v)w_V^{(k)}(v)|\,dv
\ll_{j,M,\phi}
V^{-(2M+2)}
\qquad(1\le k\le j).
}
\tag{17}
\]

On the natural safe line `sigma_X=1+r/X`, absolute convergence gives for every fixed `k>=1`

\[
|P_k(\sigma_X+i\tau)|
\le
\sum_{n\ge2}
\frac{\Lambda(n)}{(\log n)^k}n^{-\sigma_X}
\ll_k
\log\zeta(\sigma_X)
\ll_r \log X.
\tag{18}
\]

Here the first comparison follows from `log n>=log 2`; for `k=1` it is equality at the level of the positive coefficient sum. Combining (10), (17), and (18) yields

\[
\boxed{
I_{j,X,V,M}(\sigma_X+it)
=
A_{0,X,V,M}(\sigma_X+it)
+
O_{j,M,r,\phi}\!\left(
(\log X)V^{-(2M+2)}
\right)
}
\tag{19}
\]

uniformly in real `t`.

Thus the flat Gaussian window does more than make the source continuation entire. It suppresses the difference between every fixed zeta-primitive level and the same `P_0` convolution. If `V=X^epsilon`, then for any prescribed `B>0` one may choose `M` once, with `2M+2>=j` and `(2M+2)epsilon>B+1`, to make the error in (19) `O_B(X^{-B})`.

The quantifier is important: `j` and `M` are fixed before `X->infinity`. No uniform claim is made for primitive depth growing with `X`.

## 3. A finite-height rectangle removes the remote-zero problem

It remains to transport the leading term (12) to the left of one. This can be done without a global `v`-contour.

Let

\[
s_X(t):=\sigma_X+it,
\qquad
T:=\frac{|t|}{2},
\tag{20}
\]

and assume `|t|` is sufficiently large. Split

\[
A_{0,X,V,M}(s_X(t))
=A_0^{\rm cen}+A_0^{\rm tail},
\tag{21}
\]

where the central integral has `|v|<=T` and the tail has `|v|>T`.

On the tail we remain on `Re(s)=sigma_X>1`. Since

\[
\left|P_0(\sigma_X+i\tau)\right|
\le
\sum_{n\ge2}\Lambda(n)n^{-\sigma_X}
=-\frac{\zeta'(\sigma_X)}{\zeta(\sigma_X)}
\ll_r X,
\tag{22}
\]

and `L_X` is Schwartz after removing its unimodular real-axis carrier, for every `A>0`

\[
\boxed{
A_0^{\rm tail}
\ll_{A,M,r,\phi}
X(1+|t|)^{-A}.
}
\tag{23}
\]

Now fix a horizontal displacement `eta>0` and consider the finite rectangle in the complex `v`-plane

\[
\mathcal R
=
\{z=v+iy:\ |v|\le T,\ 0\le y\le\eta\}.
\tag{24}
\]

For `z=v+iy`,

\[
s_X(t)+iz
=(\sigma_X-y)+i(t+v).
\tag{25}
\]

Throughout the rectangle,

\[
\frac{|t|}{2}
\le
|t+v|
\le
\frac{3|t|}{2}.
\tag{26}
\]

Hence the height never approaches zero. In particular, the pole of zeta at `1` is not inside this rectangle. If `eta` is chosen as a safe fraction of the Vinogradov--Korobov zero-free width at height `|t|`, then no nontrivial zeta zero lies in the image (25) either. Trivial zeros are far to the left and are not encountered for the small displacement considered here.

This is the key localization point. `NB-220` correctly warned that a **global** displacement of the real `v`-axis can encounter zeta zeros at remote ordinates. The finite rectangle (24) never visits those ordinates; the remote part of the integral was already left on the absolutely convergent `1+` line in (23).

Because `W_M` and `L_X` are entire, and `P_0` is holomorphic in the zero-free rectangle, Cauchy's theorem moves only the central piece. Writing the top edge left-to-right gives

\[
\begin{aligned}
A_0^{\rm cen}
&=
\frac1{2\pi}
\int_{-T}^{T}
 w_V(v+i\eta)L_X(v+i\eta)
 P_0(\sigma_X-\eta+i(t+v))\,dv\\
&\quad + E_{\rm side}.
\end{aligned}
\tag{27}
\]

The two vertical side integrals satisfy rapid bounds. Indeed, for fixed `0<=y<=eta<=1`,

\[
L_X(\pm T+iy)
=e^{-Xy}e^{\pm iXT}
\int_0^\Delta
\phi(u)e^{-yu}e^{\pm iTu}\,du,
\tag{28}
\]

and the final integral is `O_A(T^{-A})` uniformly in `y`. The analytic Gaussian window is bounded on such a horizontal strip after its real Gaussian decay is taken into account. Therefore, if

\[
B(t,\eta)
:=
\sup_{\substack{|v|\le T\\0\le y\le\eta}}
\left|
P_0(\sigma_X-y+i(t+v))
\right|,
\tag{29}
\]

then

\[
\boxed{
E_{\rm side}
\ll_{A,M,\phi}
B(t,\eta)(1+|t|)^{-A}
}
\tag{30}
\]

for every `A>0`.

Combining (23), (27), and (30),

\[
\boxed{
\begin{aligned}
A_{0,X,V,M}(s_X(t))
&=
\frac1{2\pi}
\int_{-T}^{T}
 w_V(v+i\eta)L_X(v+i\eta)
 P_0(\sigma_X-\eta+i(t+v))\,dv\\
&\quad +
O_A\!\left(
[X+B(t,\eta)](1+|t|)^{-A}
\right).
\end{aligned}
}
\tag{31}
\]

There is no zero-residue budget in (31), because no zeta singularity is crossed. This is a genuinely local transport formula.

## 4. The carrier produces the VK gain, but the old pointwise tariff returns

Factor the moving logarithmic carrier on the shifted edge:

\[
\begin{aligned}
L_X(v+i\eta)
&=
\int_0^\Delta
\phi(u)e^{i(v+i\eta)(X+u)}\,du\\
&=
e^{-X\eta}e^{iXv}
\Phi_\eta(v),
\end{aligned}
\tag{32}
\]

where

\[
\Phi_\eta(v)
:=
\int_0^\Delta
\phi(u)e^{-\eta u}e^{ivu}\,du.
\tag{33}
\]

For `0<=eta<=1`, the family `Phi_eta` is uniformly Schwartz. Also `W_M((v+i eta)/V)` is uniformly bounded on this strip for `V>=1`. Hence

\[
\int_{-T}^{T}
|w_V(v+i\eta)\Phi_\eta(v)|\,dv
\ll_{M,\phi}1.
\tag{34}
\]

Equation (31) therefore yields the generic local estimate

\[
\boxed{
|A_{0,X,V,M}(s_X(t))|
\ll
 e^{-X\eta} B(t,\eta)
+
O_A\!\left(
[X+B(t,\eta)](1+|t|)^{-A}
\right).
}
\tag{35}
\]

Now use exactly the already-anchored Vinogradov--Korobov input employed in `NB-212`. Put

\[
Q:=\log(10+|t|),
\qquad
R:=Q^{2/3}(\log Q)^{1/3}.
\tag{36}
\]

Bellotti's zero-free region supplies a constant `c_0>0` such that, for large `|t|`, the rectangle (24)--(26) is zero-free when

\[
0<\eta\le \frac{c_0}{R}
\tag{37}
\]

with `c_0` reduced by a fixed safety factor. The same local logarithmic-derivative estimate already used in `NB-212` then gives

\[
B(t,\eta)\ll Q^2
\tag{38}
\]

on a safe fraction of that strip. Choosing

\[
\eta=\frac cR
\tag{39}
\]

for a sufficiently small fixed `c>0`, equations (19) and (35) give

\[
\boxed{
\begin{aligned}
|I_{j,X,V,M}(\sigma_X+it)|
&\ll_{j,M,r,\phi}
Q^2
\exp\!\left[-c\frac{X}{R}\right]\\
&\quad +
(\log X)V^{-(2M+2)}
+
O_A\!\left((X+Q^2)(1+|t|)^{-A}\right).
\end{aligned}
}
\tag{40}
\]

For `V=X^epsilon` and `M` chosen once according to a prescribed algebraic accuracy, the second term is `O_B(X^{-B})`. The final term is negligible at high ordinate. Thus the localized primitive pairing has exactly the same load-bearing Vinogradov--Korobov factor as the direct full-Euler barycenter in `NB-212`:

\[
\boxed{
Q^2
\exp\!\left[-c\frac{X}{Q^{2/3}(\log Q)^{1/3}}\right].
}
\tag{41}
\]

The primitive denominator has disappeared algebraically, as `NB-218` promised, but after rigorous local transport the pointwise `P_0` tariff has reappeared. This is not the reciprocal-support tariff of `NB-217`; it is the distinct cost of estimating the transported logarithmic derivative pointwise.

## 5. Relation to the entire source continuation of NB-220

`NB-220` defines an entire Euler source function `H_(X,V,M)` whose value on the safe line equals the soft-windowed primitive pairing. Equation (10) is first derived on `Re(s)>1`, where every Dirichlet series is absolutely convergent. Each term in (10) also has a source-side representation obtained by inverse Fourier transforming `L_X w_V^(k)` and dividing by `(log n)^k` for `k>=1`; the Gaussian dual tails make those source series entire by the same unit-log-shell argument as `NB-220`.

Consequently (10) may, if desired, be read as an identity among entire source-defined continuations. The quantitative estimate (40), however, does not come from entire-function growth. It comes from evaluating the physical source value on `sigma_X>1`, reducing it there to `P_0`, and moving only the central `v`-window through a zero-free rectangle.

This distinction matters. Entire continuation solved an admissibility problem, not a cancellation problem. The present factorization and finite contour solve the analytic-identification problem left by `NB-220`, but the quantitative strength is exactly that of the existing logarithmic-derivative estimate.

Combining (40) with the source approximation in `NB-220` therefore gives the same bound, up to the chosen algebraic window error, for the original compact smooth Euler shell correlation. No new positive-return corridor follows beyond `NB-212` from these steps alone.

## 6. What the reduction rules out, and what remains live

The result closes one natural interpretation of the primitive escape. For any fixed `j`, **taking more Mellin primitives does not create a new leading transported observable** once the localization window is sufficiently flat. Repeated integration by parts transfers all `j` derivatives back to the product `w_V P_j`; the term in which all derivatives hit the primitive is exactly `w_V P_0`, while every alternative Leibniz term differentiates the window and is suppressed by its finite-order flatness.

This does not say that zeta primitives are useless. Their exact coupled representation was essential for identifying where the absolute Mellin tariff entered, and the soft window gives a clean source-defined entire continuation. What it says is narrower: **finite primitive depth plus pointwise control after contour transport cannot improve the `NB-212` corridor.** The improvement must occur inside the leading signed integral

\[
\int
 e^{iXv}
\Phi_\eta(v)
W_M((v+i\eta)/V)
P_0(\sigma_X-\eta+i(t+v))\,dv,
\tag{42}
\]

before taking absolute values.

A concrete future success criterion is therefore available. One needs a cancellation-sensitive bound for (42) that is materially smaller than

\[
\|\Phi_\eta W_M\|_1
\sup |P_0|,
\]

for example replacing the positive-power `Q^2` prefactor by a polylogarithmic or bounded effective cost on the coupled diagonal. Such a bound would exploit the moving carrier `e^(iXv)` against the actual variation of `zeta'/zeta`; merely increasing `j`, invoking entire continuation, or flattening the window further cannot supply it at fixed primitive depth.

Two other escapes remain outside the theorem. Primitive depth `j=j_X` growing with `X` is not controlled because the constants in the integration-by-parts and flatness estimates have not been made uniform. And a representation not generated by finitely many Mellin primitives may evade the factorization (10). Both would require a new conditioning audit before being treated as genuine improvements.

The destination-side Nyman--Beurling bridge also remains separate: (40) is a source-side Euler cancellation estimate, not a lower bound for the optimal Nyman distance and not a proof that every good Nyman approximant must realize this particular shell observable.

## 7. Prior-art and representation audit

The ingredients used here are classical. Repeated integration by parts, the identities `P_k'=-P_(k-1)`, and local contour displacement of `-zeta'/zeta` are standard complex/Fourier analysis. Test-function contour arguments for the logarithmic derivative are part of the classical explicit-formula tradition; a close historical boundary is A. P. Guinand, *Fourier Reciprocities and the Riemann Zeta-Function*, Proc. London Math. Soc. (2) 51 (1949), 401--414, DOI `10.1112/plms/s2-51.6.401`. No novelty is claimed for contour shifting or for explicit-formula technology.

The project-local mathematical delta is the coupling of three structures already derived in this line: the exact primitive convolution of `NB-218`, the finite-flat Gaussian source localization of `NB-220`, and the local Vinogradov--Korobov logarithmic-derivative bound of `NB-212`. Their combination gives the exact factorization (10), shows that all fixed primitive depths share one `P_0` leading term, and removes the specific remote-singularity ambiguity of `NB-220` by using a finite height rectangle rather than a global contour.

The load-bearing external zero-free and logarithmic-derivative inputs are already anchored in `SOURCES.md` through Bellotti and the `NB-212` chain. Guinand is used only as a prior-art boundary for the general contour/test-function mechanism, not as a theorem needed for the derivation, so no new source dependency is introduced here.

The representation audit also separates generic from arithmetic content. The factorization (10) is a generic derivative/primitive identity for any analytic family with `P_k'=-P_(k-1)`. What is specific to the Euler source is that `P_0=-zeta'/zeta`, that its singularities are precisely controlled by zeta's pole and zeros, and that Vinogradov--Korobov gives a zero-free rectangle at the relevant moving height. The fact that the shell carrier `e^(iXv)` produces `e^(-X eta)` under horizontal displacement is Fourier geometry; the useful displacement width is arithmetic.

## 8. Falsification and boundary checks

**Sign check.** Equation (10) can be tested already at `j=1`. Since `K_1=L_X'/i` and `d_v log zeta(s+iv)=-iP_0(s+iv)`, one integration by parts gives exactly `A_0+iA_1`. A reversed sign here would invalidate the general binomial identity.

**Flatness check.** The error (19) requires `j<=2M+2` with `j,M` fixed. A fixed low-order Gaussian window does not suppress arbitrarily high primitive depth at the stated rate.

**Local-contour check.** Equation (31) shifts only `|v|<=|t|/2`. Extending the top edge to the whole real line and claiming zero-freeness there would reintroduce exactly the remote-zero problem that `NB-220` warned about. The tails in this proof stay on `Re(s)>1`.

**Pole check.** The zeta pole at `s=1` is not crossed because all points in the finite rectangle have imaginary part between `|t|/2` and `3|t|/2` in absolute value. This is why there is no pole main term or residue in (31).

**Quantitative check.** The corridor does not improve unless the estimate of the leading integral improves. Inserting the same `B(t,eta)<<Q^2` as `NB-212` must reproduce the same log-squared Vinogradov--Korobov threshold; any claimed stronger consequence from (40) without a stronger signed estimate would be bookkeeping, not new cancellation.

**Destination check.** Nothing here proves an implication from small Nyman--Beurling distance to the shell correlation under study. Treating (40) as a distance bound would skip the still-missing destination theorem.

The decisive next test is therefore no longer whether the Gaussian source continuation can cross `Re(s)=1`: it can be connected to the left locally. The live question is whether the carrier-frequency integral (42) admits a genuinely cancellation-sensitive estimate for `-zeta'/zeta` that beats its pointwise `Q^2` tariff while preserving the exact source normalization.