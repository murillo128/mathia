# WI-217 — fixed-multiplicative Gallagher slabs force `M/log T` screen complexity

**Status:** `EXACT-DERIVED + STRUCTURAL-RIGIDITY + DECISIVE-NEGATIVE + CLASSICAL-IDENTITY + LITERATURE-CONTEXT`.

WI-216 proves that an `n`-channel exponential screen cannot make its selected bow-plus-screen residue subdiagonal on a slab widened only to the screen's own scale unless `n/log T -> infinity`. That still leaves a very cheap countermodel: superlogarithmically many channels cost zero density among the `M=T^{vartheta+o(1)}` bow zeros. The next question in the canonical mandate is therefore whether a genuinely macroscopic source observation charges substantially more screen complexity.

It does. The one-null-vector argument of WI-216 leaves most of the finite-dimensional defect unused. If `q` integer translates are observed against an `n`-channel screen, the screen has a translating nullspace of dimension at least `q-n`, not merely one. Summing the sinc-frame energy over that entire nullspace yields a codimension tariff.

Let

\[
L=\log T,
\qquad
M=T^{\vartheta+o(1)},
\qquad
\eta_M=\frac{L}{2dM},
\]

retain one fixed reciprocal harmonic `k`, the odd-`M` bow normalization and `h>0` from WI-209--WI-216, and let

\[
H_M(s)=K_1\!\left[e^{\eta_M\cdot}(f_{M,k}+g_M)\right](s),
\qquad
(K_1r)(s)=\int_s^{s+1}r(v)\,dv,
\]

where `g_M` is an arbitrary sum of at most `n=n(T)` complex exponential channels. Fix constants `c>0` and `delta in (0,1)`. If integers `q=q(T)` satisfy

\[
q\to\infty,
\qquad
q\le c\frac{M}{L},
\qquad
n\le(1-\delta)q,
\tag{1}
\]

then there are constants `A=A(c,delta,h,k,d)>0` and `K=K(c,delta,h,k,d)>0`, independent of `T`, such that for all sufficiently large `T`

\[
\boxed{
\int_{-q-K}^{q+K}|H_M(s)|^2\,ds\ge A.
}
\tag{2}
\]

Consequently the selected physical Gallagher energy on the corresponding `u`-slab is at least a positive constant times `L` times the **full raw-prime Gallagher diagonal**. In particular, if the selected residue is `o` of that global diagonal on a slab of fixed positive multiplicative width in `x`, its effective exponential-channel rank must satisfy

\[
\boxed{n(T)\gg \frac{M}{\log T}.}
\tag{3}
\]

More sharply, for every translate budget `q<=cM/L` whose associated slab is available, subdiagonal selected energy forces

\[
\boxed{
\liminf_{T\to\infty}\frac{n(T)}{q(T)}\ge1,
}
\tag{4}
\]

or equivalently `n(T)>=(1-o(1))q(T)`. Since one off-line functional-equation pair contributes at most two complex exponential channels in the WI-214--WI-216 screen model, the same argument charges `Omega(M/log T)` such pairs up to that fixed factor. This is still `o(M)`, so it does **not** prove a positive-density exceptional-zero cost or RH. It is nevertheless a much stronger rigidity statement than WI-216: a fixed multiplicative source window cannot leave out any fixed fraction of the finite-translation rank budget.

## 1. The limiting sinc target has a uniform `q`-dimensional lower frame bound

Write, as in WI-216,

\[
f_k(u)=C_k\operatorname{sinc}(u),
\qquad
C_k=2\cosh(hk),
\qquad
F_k=K_1f_k.
\]

The Fourier identities

\[
\operatorname{sinc}(u)=\int_{-1/2}^{1/2}e^{2\pi i\xi u}\,d\xi,
\qquad
m(\xi)=\int_0^1e^{2\pi i\xi v}\,dv,
\]

and `|m(xi)|>=2/pi` for `|xi|<=1/2` give, for every `b=(b_0,...,b_{q-1})`,

\[
\boxed{
\left\|\sum_{j=0}^{q-1}b_jF_k(\cdot+j)\right\|_2^2
\ge c_0\|b\|_2^2,
\qquad
c_0:=\frac{4C_k^2}{\pi^2}.
}
\tag{5}
\]

This is just Parseval plus orthogonality of the integer Fourier modes on `[-1/2,1/2]`; no asymptotic spectral theorem is needed.

Now let `S_M=K_1[e^{eta_M\cdot}g_M]`. Its `q` translates span dimension at most `n`. Hence

\[
U_M:=\left\{a\in\mathbb C^q:
\sum_{j=0}^{q-1}a_jS_M(s+j)\equiv0\right\}
\]

has dimension

\[
r:=\dim U_M\ge q-n\ge\delta q.
\tag{6}
\]

Choose an orthonormal basis `a^(1),...,a^(r)` of `U_M`. The key point is to use **all** these null vectors.

## 2. The whole translating nullspace keeps order-`r` target energy on an `O(q)` interval

The exponential tilt is small per unit step but need not be close to one across the whole `q`-window. Treat it exactly by setting

\[
b_j^{(\alpha)}:=e^{\eta_Mj}a_j^{(\alpha)}.
\tag{7}
\]

Because `q<=cM/L`,

\[
1\le e^{\eta_Mj}\le e^{c/(2d)}
\tag{8}
\]

for `0<=j<q`. Applying (5) to each `b^(alpha)` and summing gives

\[
\sum_{\alpha=1}^r
\left\|\sum_jb_j^{(\alpha)}F_k(\cdot+j)\right\|_2^2
\ge c_0r.
\tag{9}
\]

To localize this energy, use the WI-216 tail estimate

\[
\int_{|s|>R}|F_k(s)|^2ds
\le\frac{3C_k^2}{\pi^2R},
\qquad R\ge2.
\tag{10}
\]

At each `s`, orthonormality of the `a^(alpha)` and (8) give the Bessel bound

\[
\sum_{\alpha=1}^r
\left|\sum_jb_j^{(\alpha)}F_k(s+j)\right|^2
\le e^{c/d}\sum_{j=0}^{q-1}|F_k(s+j)|^2.
\tag{11}
\]

Outside

\[
I_{q,R}:=[-q-R,R]
\tag{12}
\]

every shifted argument lies outside `[-R,R]`. Thus (10)--(11) imply

\[
\sum_{\alpha=1}^r
\int_{\mathbb R\setminus I_{q,R}}
\left|\sum_jb_j^{(\alpha)}F_k(s+j)\right|^2ds
\le
q e^{c/d}\frac{3C_k^2}{\pi^2R}.
\tag{13}
\]

Since `r>=delta q`, choose once and for all

\[
R>\frac{18e^{c/d}C_k^2}{\delta\pi^2c_0}.
\tag{14}
\]

Then the right side of (13) is less than `(c_0/2)r`, and therefore

\[
\boxed{
\sum_{\alpha=1}^r
\left\|\sum_jb_j^{(\alpha)}F_k(\cdot+j)\right\|_{L^2(I_{q,R})}^2
\ge\frac{c_0}{2}r.
}
\tag{15}
\]

The important scaling is that `R` depends only on the fixed rank deficit `delta`, not on `q`. A positive fractional codimension therefore leaves order-`q` aggregate target energy on an interval of length `q+O_delta(1)`.

## 3. The finite-`M` bow remains stable all the way to `q=O(M/L)`

WI-216 could replace the tilted finite bow by the limiting sinc because there `q=O(L)`. At the present scale `q=O(M/L)`, the total tilt `eta_M q` is only bounded, not `o(1)`, so the approximation must be reorganized rather than reused verbatim.

For odd `M` and integer `k`, the bow has the exact factorization

\[
f_{M,k}(u)
=C_k\operatorname{sinc}(u)\rho_M(u),
\tag{16}
\]

with

\[
\rho_M(u)=
\frac{\cosh(h(k+u/M))}{\cosh(hk)}
\frac{\pi u/M}{\sin(\pi u/M)}.
\tag{17}
\]

On every interval `|u|<=Cq+O(1)` with `q<=cM/L`, elementary Taylor bounds give

\[
\boxed{
\sup|\rho_M-1|=O_{c,C,h,k}(L^{-1}).
}
\tag{18}
\]

Next factor the tilt on each translate:

\[
K_1[e^{\eta_M\cdot}f_k](s+j)
=e^{\eta_Ms}e^{\eta_Mj}
\bigl(F_k(s+j)+E_{\eta_M}(s+j)\bigr),
\tag{19}
\]

where

\[
E_\eta(s)=\int_0^1(e^{\eta v}-1)f_k(s+v)\,dv.
\]

Since `f_k` is bandlimited to `[-1/2,1/2]`, the Fourier multiplier of this error has sup norm `O(eta)`. Hence its integer-translate synthesis operator has norm `O(eta)`, uniformly in `q`. Summed over the `r` vectors in (7), its squared contribution is `O(eta_M^2 r)=o(r)`.

The remaining finite-bow error from `rho_M-1` need only be controlled on the local interval used in (15). Let `E_M` denote the corresponding box-integrated error after the common factors in (19) are removed. Equations (8) and (18), Bessel's inequality in the `alpha` index, and boundedness of box convolution on `L^2` give

\[
\sum_{\alpha=1}^r
\int_{I_{q,R}}
\left|\sum_jb_j^{(\alpha)}E_M(s+j)\right|^2ds
\le
O_{c,\delta,h,k,d}\!\left(\frac q{L^2}\right)
=o(r).
\tag{20}
\]

The last estimate uses `int_R sinc(u)^2 du=1`: although the observation interval has length `O(q)`, the modulation error is `O(1/L)` times an `L^2` target of bounded total mass, so there is no extra `q` loss inside each shifted profile. This Hilbert--Schmidt/Bessel estimate is the step that prevents the naive `sqrt(q)/L` pointwise accumulation from spoiling the `q~M/L` regime.

Finally, on `I_{q,R}` the common factor `e^{eta_Ms}` is bounded above and below by positive constants depending only on `c,d,R`. Combining (15), (19) and (20), and using the screen annihilation defining `U_M`, yields

\[
\boxed{
\sum_{\alpha=1}^r
\left\|\sum_ja_j^{(\alpha)}H_M(\cdot+j)\right\|_{L^2(I_{q,R})}^2
\ge c_1r
}
\tag{21}
\]

for some fixed `c_1=c_1(c,delta,h,k,d)>0` and all sufficiently large `T`.

Apply Bessel once more to the orthonormal `a^(alpha)`:

\[
\sum_{\alpha=1}^r
\left|\sum_ja_j^{(\alpha)}H_M(s+j)\right|^2
\le\sum_{j=0}^{q-1}|H_M(s+j)|^2.
\]

Integrating (21) and enlarging to

\[
J_{q,R}:=[-q-R,q+R]
\]

gives

\[
c_1r
\le q\int_{J_{q,R}}|H_M(s)|^2ds.
\]

Since `r>=delta q`, this proves (2) with `A=c_1delta` and `K=R`.

## 4. Gallagher conversion turns fixed multiplicative width into an `M/L` rank charge

The exact WI-215/WI-216 physical dictionary is

\[
Q_M(s)=-X_k^{1/2}\frac{L}{d}H_M(s),
\qquad
X_k=T^{k/d},
\]

and

\[
\frac{dx_{k,M}(s)}{ds}
=X_ke^{sL/(dM)}\frac{L}{dM}.
\tag{22}
\]

On `J_{q,R}`, condition `q<=cM/L` keeps the Jacobian multiplier between two fixed positive constants. Therefore (2) implies

\[
\int_{x(J_{q,R})}|Q_M(x)|^2dx
\gg_{c,\delta,h,k,d}
\frac{X_k^2L^3}{d^3M}.
\tag{23}
\]

The full raw-prime Gallagher diagonal at this unit-box short length is, as in WI-216,

\[
X_kK_k\log X_k
\sim k\frac{X_k^2L^2}{d^2M}.
\tag{24}
\]

Hence

\[
\boxed{
\frac{\int_{x(J_{q,R})}|Q_M(x)|^2dx}
{X_kK_k\log X_k}
\gg_{c,\delta,h,k,d}L.
}
\tag{25}
\]

A fixed fractional translation-rank deficit is therefore not merely non-subdiagonal: it is **superdiagonal by a logarithmic factor**.

Now take `q` to be a fixed positive constant times `M/L`, small enough that `J_{q,R}` lies in the prescribed observation slab. Since

\[
t=k+\frac uM,
\qquad
\log x=\frac{L}{d}t,
\]

a normalized width `Delta u = Theta(M/L)` corresponds to `Delta log x=Theta(1)`, i.e. a fixed multiplicative `x`-window. If the selected residue is `o` of the global raw-prime diagonal on that window, (25) rules out `n<=(1-delta)q` for every fixed `delta>0`. This gives (3)--(4).

## 5. What this rules out, and what it still cannot rule out

WI-216 left open the possibility that a source bootstrap might simply let the off-line screen grow a little faster than `log T`. WI-217 rules out that cheap route once the source observation reaches fixed multiplicative width: **every fixed fractional deficit in the available translation rank leaves a logarithmically superdiagonal residue**. The screen must spend order `M/log T` independent channels and cannot omit any fixed fraction of the `q` translation degrees of freedom selected inside the slab.

This is a genuine rigidity condition on the uncertified complement, but it is not yet a defect-to-zero theorem. Because

\[
\frac{M/L}{M}=\frac1L\to0,
\]

an `M/log T` exceptional packet still has zero density. The argument also controls only the selected bow-plus-screen source residue. It does not exclude cancellation by complementary zeros, pole/trivial terms, contour terms or structured prime-side contributions in the **full** explicit formula. As in WI-195, WI-209, WI-215 and WI-216, a source-fixed upper bound is still required before converting this rank charge into an impossibility statement for actual zeta.

Nor does the result say that `M/log T` channels are sufficient to screen a fixed multiplicative slab. WI-214 constructs efficient packets only on narrower `u=O(J)` windows in a specific two-harmonic countermodel. WI-217 is a necessary-complexity theorem, not a matching construction at the fixed-multiplicative scale.

## 6. Prior-art audit

The underlying time-frequency dimension phenomenon is classical. Landau and Pollak, *Prolate Spheroidal Wave Functions, Fourier Analysis and Uncertainty—III: The Dimension of the Space of Essentially Time- and Band-Limited Signals*, Bell System Technical Journal 41 (1962), 1295--1336, DOI `10.1002/j.1538-7305.1962.tb03279.x`, identifies the linear time-bandwidth dimension of approximately localized bandlimited signal spaces. Ron and Shen, *Frames and Stable Bases for Shift-Invariant Subspaces of L2(R^d)*, Canadian Journal of Mathematics 47 (1995), 1051--1094, DOI `10.4153/CJM-1995-056-1`, gives the general Fourier-fiber framework for stable translate systems. These are literature context for why a sinc target should carry linearly many independent observations; neither is used as a black box in the proof above.

The actual lower bound here is more elementary and more specialized: exact orthogonality of integer sinc translates gives (5), finite-dimensional rank-nullity gives the `q-n` nullspace, and Bessel aggregation localizes the **entire codimension** rather than one null vector. A targeted search covering time-bandwidth/prolate dimension, shift-invariant frames, sinc translate approximation, Gallagher short-interval norms, off-critical zeta screening, and the recent Alpöge--Furman/Lamzouri simple-critical-zero literature found no published theorem coupling this codimension argument to the WI-209--WI-216 source normalization or deriving the `M/log T` screen tariff on fixed multiplicative slabs. That absence is not a priority claim.

The recent primary theorem remains Alpöge--Furman, arXiv:2608.13637, with Lamzouri arXiv:2609.02882 as an independent Hilbert-space reformulation of the `>2/3` mechanism. Neither source supplies the selected-source screening model used here. The new mathematical content recorded by WI-217 is therefore the exact codimension amplification and its Gallagher scaling consequence inside the already established Mathia countermodel architecture.

## 7. Falsification boundary

The structural claim can be falsified without touching zeta arithmetic. One would need an exponential screen satisfying (1) for which the exact normalized residue violates (2). The load-bearing checks are: the uniform sinc translate lower bound (5), the `q-n` translating nullspace (6), the tail/Bessel localization (11)--(15), the exact finite-bow factorization (16)--(18), and the aggregate perturbation estimate (20). In particular, a failure of the old WI-216 approximation `e^{eta_Mu}f_{M,k}(u)~f_k(u)` at `u~M/L` is **not** a counterexample: WI-217 does not make that approximation and instead carries the bounded exponential tilt through (7)--(8) and (19).

The zeta-level implication can fail even if every displayed analytic estimate is correct, because the selected residue may be canceled in the full explicit formula. No unconditional simple-critical-zero proportion changes here, and no positive-density lower bound on off-line zeros is asserted. The substantive advance is narrower and rigid: **on fixed multiplicative source windows, finite-translation codimension forces an `Omega(M/log T)` exceptional-screen complexity cost, and every admissible `q`-translate observation family forces `n>=(1-o(1))q`.**
