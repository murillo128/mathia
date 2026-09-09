# WI-218 — a logarithmic stack of multiplicative slabs forces positive-density screen complexity

**Status:** `EXACT-DERIVED + STRUCTURAL-RIGIDITY + DECISIVE-NEGATIVE + CLASSICAL-IDENTITY + LITERATURE-CONTEXT`.

WI-217 shows that one fixed-multiplicative Gallagher slab forces only `Omega(M/log T)` exponential screen complexity for an arithmetic bow of population `M=T^{vartheta+o(1)}`. That cost is still zero density relative to `M`. The missing question is whether this logarithmic loss is intrinsic to the bow/source geometry or only to observing one fixed-multiplicative slab at a time.

It is the latter. Keep one reciprocal harmonic `k`, the WI-214--WI-217 bow normalization, and the **same** exponential screen across a small fixed power-scale band around `X_k=T^{k/d}`. There is a fixed `sigma=sigma(h,k,d)>0` such that the following holds. Let the screen have effective exponential-channel rank `n=n(T)`. If

\[
n\le \frac{\sigma}{2}M,
\]

then among `O(log T)` adjacent fixed-multiplicative Gallagher slabs covering

\[
T^{(k-\sigma)/d+o(1)}
\le x\le
T^{(k+\sigma)/d+o(1)},
\]

at least one slab has selected bow-plus-screen energy at least a fixed positive fraction of its matching raw-prime Gallagher diagonal. Consequently, a single screen whose selected residue is `o` of the local raw-prime diagonal on **every** fixed-multiplicative slab in that band must have

\[
\boxed{n(T)\gg M.}
\]

Since one off-line functional-equation pair contributes at most two complex exponential channels in the WI-214--WI-217 screen model, uniform subdiagonal screening across the band costs `Omega(M)` such pairs as well. This is a positive-density **screen-complexity** charge relative to the bow population.

The result does **not** exclude an actual zeta bow and does not give a positive-density lower bound for off-line zeta zeros. The full explicit formula can still cancel the selected residue, and the screening pairs counted here need not lie in the bow's short vertical interval. What is closed is the structural escape left by WI-217: the factor `log T` is not needed once one asks the same screen to survive a logarithmic stack of adjacent multiplicative source observations.

## 1. Remove the outer Gallagher tilt before taking translates

Use the notation of WI-216--WI-217:

\[
L=\log T,
\qquad
M=T^{\vartheta+o(1)},
\qquad
\eta_M=\frac{L}{2dM},
\]

and, at one fixed reciprocal harmonic `k`,

\[
H_M(s)
=K_1\!\left[e^{\eta_M\cdot}(f_{M,k}+g_M)\right](s),
\qquad
(K_1r)(s)=\int_s^{s+1}r(v)\,dv.
\tag{1}
\]

Here `g_M` is an arbitrary sum of at most `n` complex exponential channels and, for odd `M`, the exact normalized bow is

\[
f_{M,k}(u)
=C_k\operatorname{sinc}(u)\rho_M(u),
\qquad
C_k=2\cosh(hk),
\tag{2}
\]

with

\[
\rho_M(u)
=
\frac{\cosh(h(k+u/M))}{\cosh(hk)}
\frac{\pi u/M}{\sin(\pi u/M)}.
\tag{3}
\]

The restriction `q=O(M/L)` in WI-217 comes from keeping the outer factor `e^{eta_M s}` bounded while translating `H_M`. For a stack of physical slabs that factor should instead be absorbed into the local physical normalization. Define

\[
(K_{\eta}r)(s):=\int_0^1e^{\eta v}r(s+v)\,dv
\]

and

\[
\boxed{
\widetilde H_M(s)
:=e^{-\eta_Ms}H_M(s)
=K_{\eta_M}(f_{M,k}+g_M)(s).
}
\tag{4}
\]

This is an exact identity. It is also rank-neutral: if

\[
g_M(u)=\sum_{\ell=1}^{n}c_{\ell,M}e^{z_{\ell,M}u},
\]

then `K_{eta_M}g_M` is still a sum of at most the same `n` exponential channels. Thus the translating-nullspace argument can now be run on `\widetilde H_M` without exponentially reweighting its translate coefficients.

The outer tilt has not been discarded. Section 5 below puts it back exactly through the physical Jacobian; that is what lets different slabs be compared with their own local raw-prime diagonal.

## 2. The sinc translate frame remains uniformly coercive after `K_eta`

Put

\[
f_k(u):=C_k\operatorname{sinc}(u),
\qquad
F_{k,\eta}:=K_\eta f_k.
\tag{5}
\]

The classical bandlimited identity

\[
\operatorname{sinc}(u)
=\int_{-1/2}^{1/2}e^{2\pi i\xi u}\,d\xi
\]

shows that the Fourier multiplier of `K_eta` on this band is

\[
m_\eta(\xi)=\int_0^1e^{\eta v}e^{2\pi i\xi v}\,dv.
\tag{6}
\]

At `eta=0`,

\[
|m_0(\xi)|
=\left|\frac{\sin(\pi\xi)}{\pi\xi}\right|
\ge\frac2\pi
\qquad(|\xi|\le1/2).
\]

Moreover

\[
\sup_{|\xi|\le1/2}|m_\eta(\xi)-m_0(\xi)|
\le\int_0^1(e^{\eta v}-1)\,dv
=O(\eta).
\]

Since `eta_M->0`, for all sufficiently large `T` there is a fixed `c_0=c_0(h,k)>0` such that every finite coefficient vector `a` satisfies

\[
\boxed{
\left\|
\sum_j a_jF_{k,\eta_M}(\cdot+j)
\right\|_2^2
\ge c_0\sum_j|a_j|^2.
}
\tag{7}
\]

This is the same integer-translate Fourier-frame mechanism used in WI-216--WI-217, now with the small box tilt carried exactly in the multiplier.

There is also a uniform tail bound. Since `eta_M=o(1)` and `|sinc(u)|<=1/(pi|u|)` away from the origin,

\[
\int_{|s|>R}|F_{k,\eta_M}(s)|^2ds
\ll_{h,k}\frac1R,
\qquad R\ge2,
\tag{8}
\]

with the implied constant independent of large `T`.

## 3. A positive fractional rank deficit leaves order-`M` aggregate target energy

Fix once and for all

\[
\delta:=\frac12.
\tag{9}
\]

Choose a small fixed `sigma>0`, to be specified in Section 4, and set

\[
q:=\lfloor\sigma M\rfloor.
\tag{10}
\]

Let

\[
S_M:=K_{\eta_M}g_M.
\]

The `q` translates `S_M(s+j)`, `0<=j<q`, span dimension at most `n`. Hence if

\[
n\le(1-\delta)q=\frac q2,
\tag{11}
\]

then the exact translating nullspace

\[
U_M
:=
\left\{a\in\mathbb C^q:
\sum_{j=0}^{q-1}a_jS_M(s+j)\equiv0
\right\}
\tag{12}
\]

has dimension

\[
r:=\dim U_M\ge q-n\ge\delta q.
\tag{13}
\]

Choose an orthonormal basis `a^(1),...,a^(r)` of `U_M`. Summing (7) over this basis gives

\[
\sum_{\alpha=1}^{r}
\left\|
\sum_{j=0}^{q-1}a_j^{(\alpha)}F_{k,\eta_M}(\cdot+j)
\right\|_2^2
\ge c_0r.
\tag{14}
\]

This aggregate use of the whole nullspace is the codimension mechanism from WI-217. The point is that after (4) it remains available all the way to `q` proportional to `M`.

Localize (14) exactly as in WI-217. For a constant `R>=2` put

\[
I_{q,R}:=[-q-R,R].
\tag{15}
\]

At each `s`, orthonormality gives the Bessel estimate

\[
\sum_{\alpha=1}^{r}
\left|
\sum_ja_j^{(\alpha)}F_{k,\eta_M}(s+j)
\right|^2
\le
\sum_{j=0}^{q-1}|F_{k,\eta_M}(s+j)|^2.
\tag{16}
\]

Outside `I_{q,R}` every shifted argument lies outside a fixed `R`-neighborhood of the origin. Using (8) and summing over `j`,

\[
\sum_{\alpha=1}^{r}
\int_{\mathbb R\setminus I_{q,R}}
\left|
\sum_ja_j^{(\alpha)}F_{k,\eta_M}(s+j)
\right|^2ds
\ll_{h,k}\frac qR.
\tag{17}
\]

Because `r>=delta q`, choose `R=R(h,k,delta)` once so that the right side of (17) is at most `(c_0/4)r`. Then

\[
\boxed{
\sum_{\alpha=1}^{r}
\left\|
\sum_ja_j^{(\alpha)}F_{k,\eta_M}(\cdot+j)
\right\|_{L^2(I_{q,R})}^2
\ge\frac{3c_0}{4}r.
}
\tag{18}
\]

## 4. The exact finite bow is a small perturbation on a fixed power-scale band

The remaining issue is that `f_{M,k}` is not exactly the limiting sinc when `|u|` is a fixed fraction of `M`. Equation (3) shows precisely what is lost.

Choose `sigma>0` small enough that

\[
2\sigma<\min(k,d-k)
\tag{19}
\]

and `pi sigma<pi/4`. On all arguments used in (15)--(18), namely

\[
|u|\le q+R+1\le\sigma M+O(1),
\]

we have uniformly

\[
\frac{\cosh(h(k+u/M))}{\cosh(hk)}
=1+O_{h,k}(\sigma),
\]

and

\[
\frac{\pi u/M}{\sin(\pi u/M)}
=1+O(\sigma^2).
\]

Thus

\[
\boxed{
\sup_{|u|\le q+R+1}|\rho_M(u)-1|
\le \varepsilon_\sigma+o(1),
\qquad
\varepsilon_\sigma=O_{h,k}(\sigma+\sigma^2).
}
\tag{20}
\]

Let

\[
E_M:=K_{\eta_M}(f_{M,k}-f_k).
\]

On the translated arguments actually entering `I_{q,R}`, (20), Young's inequality for the unit box, and `f_k in L^2(R)` give a uniform local `L^2` bound of size `O_{h,k}(epsilon_sigma^2)` for one error profile. Bessel's inequality in the `alpha` index then gives

\[
\boxed{
\sum_{\alpha=1}^{r}
\int_{I_{q,R}}
\left|
\sum_ja_j^{(\alpha)}E_M(s+j)
\right|^2ds
\ll_{h,k}q\bigl(\varepsilon_\sigma^2+o(1)\bigr).
}
\tag{21}
\]

For completeness, the factor `q` in (21) is the translate multiplicity: pointwise Bessel bounds the sum over `alpha` by `sum_j |E_M(s+j)|^2`, and integration over `I_{q,R}` covers each local error profile at most `q` times. There is no additional `q` loss because `f_k=C_k sinc` has finite total `L^2` mass.

Now choose `sigma` once, depending only on `h,k,d`, so small that the right side of (21) is at most `(c_0/16)r` whenever `r>=delta q`, for all sufficiently large `T`. Applying the triangle inequality in the direct-sum Hilbert space over `alpha` to (18)--(21) gives a constant `c_1=c_1(h,k,d)>0` such that

\[
\boxed{
\sum_{\alpha=1}^{r}
\left\|
\sum_ja_j^{(\alpha)}K_{\eta_M}f_{M,k}(\cdot+j)
\right\|_{L^2(I_{q,R})}^2
\ge c_1r.
}
\tag{22}
\]

The screen term vanishes identically for every `a^(alpha)` by (12). Therefore (22) is equally

\[
\sum_{\alpha=1}^{r}
\left\|
\sum_ja_j^{(\alpha)}\widetilde H_M(\cdot+j)
\right\|_{L^2(I_{q,R})}^2
\ge c_1r.
\tag{23}
\]

A second pointwise Bessel estimate gives

\[
\sum_{\alpha=1}^{r}
\left|
\sum_ja_j^{(\alpha)}\widetilde H_M(s+j)
\right|^2
\le
\sum_{j=0}^{q-1}|\widetilde H_M(s+j)|^2.
\]

After integration and enlargement to

\[
J_{q,R}:=[-q-R,q+R],
\]

we obtain

\[
c_1r
\le q\int_{J_{q,R}}|\widetilde H_M(t)|^2dt.
\]

Using `r>=delta q`,

\[
\boxed{
\int_{J_{q,R}}|\widetilde H_M(t)|^2dt
\ge c_1\delta.
}
\tag{24}
\]

Thus a screen with a fixed positive fractional rank deficit leaves a fixed amount of normalized residue energy somewhere across a natural-coordinate interval of length `Theta(M)`.

## 5. `O(log T)` multiplicative slabs turn (24) into a positive-density rank charge

Fix any constant `kappa>0` and partition `J_{q,R}` into consecutive blocks `S_b` of natural-coordinate length

\[
Q:=\left\lfloor\kappa\frac{M}{L}\right\rfloor,
\tag{25}
\]

allowing two shorter endpoint blocks. Since `q~sigma M`, the number of blocks is

\[
B=O_{\sigma,\kappa}(L).
\tag{26}
\]

By (24), at least one block satisfies

\[
\boxed{
\int_{S_b}|\widetilde H_M(s)|^2ds
\gg_{h,k,d,\sigma,\kappa}\frac1L.
}
\tag{27}
\]

Each such block is a fixed-multiplicative physical Gallagher slab. Indeed the exact WI-215--WI-217 physical coordinate is

\[
x(s)=X_k e^{sL/(dM)},
\qquad
X_k=T^{k/d},
\tag{28}
\]

so a block of length (25) changes `x` by the fixed factor

\[
\exp\!\left(\frac{QL}{dM}\right)
=e^{\kappa/d+o(1)}.
\tag{29}
\]

Condition (19) keeps every block in the compact support-one power range

\[
\frac{k-\sigma+o(1)}d
\le
\frac{\log x}{\log T}
\le
\frac{k+\sigma+o(1)}d
\subset(0,1).
\tag{30}
\]

Now restore the tilt removed in (4). The exact physical dictionary from WI-215--WI-217 is

\[
Q_M(s)
=-X_k^{1/2}\frac Ld H_M(s),
\qquad
\frac{dx}{ds}
=X_ke^{sL/(dM)}\frac{L}{dM}.
\tag{31}
\]

Since `H_M(s)=e^{eta_Ms}\widetilde H_M(s)` and `2eta_M=L/(dM)`, (31) gives

\[
\boxed{
\int_{x(S_b)}|Q_M(x)|^2dx
=
\frac{X_k^2L^3}{d^3M}
\int_{S_b}e^{4\eta_Ms}|\widetilde H_M(s)|^2ds.
}
\tag{32}
\]

On one block `S_b`, the factor `e^{4eta_Ms}` varies by only a fixed multiplicative constant. If `s_b` is any point of the block and `x_b=x(s_b)`, then the matching unit-box short length is

\[
K_b\asymp x_b\frac L{dM},
\]

and the raw-prime Gallagher diagonal over a fixed-multiplicative `x`-slab has scale

\[
D_b\asymp x_bK_b\log x_b
\asymp_{k,d,\sigma,\kappa}
\frac{x_b^2L^2}{M}.
\tag{33}
\]

Equations (27), (32), and (33) therefore imply for the selected block

\[
\boxed{
\frac{\int_{x(S_b)}|Q_M(x)|^2dx}{D_b}
\gg_{h,k,d,\sigma,\kappa}1.
}
\tag{34}
\]

The key cancellation is the bookkeeping factor `L`: locally the ratio is comparable to

\[
L\int_{S_b}|\widetilde H_M(s)|^2ds,
\]

and the pigeonhole loss across `O(L)` slabs is exactly `1/L`. Hence the logarithmic stack recovers the factor lost by a one-slab observation.

Combining (10)--(11) and (34), if the same screen has selected energy `o(D_b)` on every fixed-multiplicative block in the band, then eventually

\[
n>\frac q2
=\left(\frac\sigma2+o(1)\right)M.
\tag{35}
\]

If `N_scr` is the number of off-line functional-equation pairs used by that screen, then `n<=2N_scr`, so

\[
\boxed{
N_{\rm scr}
\ge\left(\frac\sigma4+o(1)\right)M.
}
\tag{36}
\]

This is the promised positive-density screen-complexity tariff.

## 6. What this closes, and what it does not

WI-214 proved that polylogarithmically many off-line pairs can flatten finitely many natural reciprocal windows. WI-216 showed that a linearly widened slab demands superlogarithmic complexity. WI-217 raised the price on one fixed-multiplicative slab to `Omega(M/log T)`, but explicitly left a zero-density screen escape. The present argument closes that particular escape **if one demands simultaneous source suppression across a small fixed exponent band**:

\[
\boxed{
\text{one slab: }\Omega(M/L)
\quad\longrightarrow\quad
O(L)\text{ adjacent slabs: }\Omega(M).
}
\]

The result is deliberately narrower than a zeta theorem.

- It is a statement about the effective exponential-channel rank of the selected bow-plus-screen model. It does not identify those channels with a distinct local zero population.
- The `Omega(M)` screening pairs may be supplied by zeros outside the bow's short vertical span; local Riemann--von Mangoldt counting alone therefore does not contradict (36).
- The full explicit formula can cancel the selected residue. A theorem that controls only one distinguished `X` still faces the WI-217 `M/log T` barrier. To consume (35), the arithmetic source estimate must control a fixed power-scale band, or an equivalent family of `Theta(log T)` independent fixed-multiplicative observations, at the same distinguished bow twist.
- No unconditional simple-critical-zero proportion changes, and no RH implication is claimed.

The structural gain is nevertheless exact: **continuum screening is not cheap across scale**. A zero-density exponential packet can imitate one or finitely many reciprocal profiles, but it cannot keep doing so across a fixed exponent band while retaining a positive fractional rank deficit.

## 7. Novelty audit and provenance

The ingredients are separated by provenance.

- **Existing Mathia geometry:** WI-214 supplies the growing exponential-screen model, WI-216 the tilt/physical Gallagher dictionary and sinc-frame mechanism, and WI-217 the whole-nullspace codimension argument and fixed-multiplicative `M/log T` tariff.
- **Classical identity:** the integer translates of `sinc` form the critical Paley--Wiener/Shannon shift system; (7) is just Parseval on `[-1/2,1/2]` after the nonvanishing unit-box multiplier. Classical Paley--Wiener/Riesz-basis and shift-invariant-space literature is context, not a new arithmetic input.
- **New exact deduction here:** the tilt-normalized identity (4), extension of the nullspace argument to `q=Theta(M)` on a sufficiently small fixed power-scale band, and the `O(log T)` slab pigeonhole that upgrades `Omega(M/log T)` to `Omega(M)` effective screen rank.

A bounded prior-art audit around sinc integer translates, Paley--Wiener/Riesz frames, finite-rank exponential-polynomial approximation, Gallagher short-interval norms, and finite-dimensional exponential screening found the expected classical sampling/frame theory but no direct formulation of the bow-specific logarithmic-stack tariff (35)--(36). That absence is not used as a priority claim. No new external theorem is load-bearing, so `SOURCES.md` is unchanged.

Read-only adjacent Mathia work on the distinguished bow source has continued to sharpen the arithmetic coefficient law, but none of those results is used to prove (35). This finding is therefore a same-line structural deduction rather than an import from another research line.

## 8. Falsification boundary and next gate

The analytic claim can be falsified without touching zeta arithmetic. A counterexample would be an `n<=sigma M/2` exponential screen for which the exact normalized residue violates (24), or for which all blocks in (25) are subdiagonal despite (27)--(34). The load-bearing checks are: exact tilt removal (4), preservation of exponential rank under `K_eta`, the uniform sinc-frame bound (7), the `q-n` nullspace, aggregate tail localization (17)--(18), the fixed-`sigma` bow perturbation estimate (20)--(21), and the local physical renormalization (32)--(33).

The zeta-level implication can still fail even if every analytic step is correct, because selected and complementary source vectors may cancel before the final square. The next meaningful gate is therefore not another refinement of one-slab screen rank. It is either:

1. a source theorem controlling the distinguished bow residual uniformly over a fixed support-one power band, so that (35)--(36) becomes an actual exceptional-zero cost; or
2. a proof that the full zeta complement can realize the required `Omega(M)` scale-varying screen without paying an independent multiplicity, density, or source-energy penalty.

Until one of those is obtained, WI-218 is a structural rigidity theorem for the screen interface, not a defect-to-zero theorem for zeta.
