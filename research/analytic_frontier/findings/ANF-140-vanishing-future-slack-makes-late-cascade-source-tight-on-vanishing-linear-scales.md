# ANF-140 — vanishing future slack makes the late cascade source-tight on vanishing linear scales

**Status:** `EXACT-DERIVED + POSITIVE-TRANSLATION-CASCADE + SOURCE-HILBERT-TRIANGLE + RESTRICTED-SLACK-TAIL + SOURCE-WEIGHTED-LARGE-DEVIATION + POSITIVE-RESIDUAL-SLACK + ARBITRARILY-SMALL-LINEAR-TAIL + SLOW-DIAGONAL-SUBLINEAR-TRIMMING`. `ANF-139` shows that positive residual copy-rate slack concentrates the **coefficient mass** of the complete annihilator cloud on the `sqrt(A)` scale, but leaves open whether an exponentially thin coefficient tail can recover macroscopic Montgomery--Taylor source through coherent amplification. For the complete cloud that question remains nontrivial, because its unsigned copy mass is itself exponentially large. For the **late tail of the cascade**, however, the remaining copy-rate budget tends to zero with the cut depth. That vanishing entropy budget is enough to convert the coefficient concentration into a genuine source estimate.

Cut the infinite `ANF-133` cascade after a fixed stage `k`, and let stages `k+1,...,D` act on the stage-`k` packet. Write

\[
T_{k,D}:=\delta_k-\delta_D,
\qquad
T_k^\infty:=\delta_k-\delta_\infty.
\tag{1}
\]

If the late translation increment is sampled according to normalized positive expansion coefficients, let `bar omega_{k,D,A}` be its barycenter. For `epsilon>0`, retain only those late copies whose increment lies outside

\[
|\omega-\bar\omega_{k,D,A}|<\varepsilon A.
\tag{2}
\]

Call the resulting physical submultiset `X_{k,D,A}^{out}(epsilon)`. Then, whenever `T_{k,D}>0`,

\[
\boxed{
\frac{E_0(X_{k,D,A}^{\rm out}(\varepsilon))^{1/2}}
{E_0(X_A^{(k)})^{1/2}}
\le
2\exp\!\left[
-A\left(
\frac{16\log2\,\varepsilon^2\delta_k\delta_D}{T_{k,D}}
-\frac{T_{k,D}}2
\right)
\right].
}
\tag{3}
\]

The first term is the `ANF-139` Bernoulli large-deviation cost; the second is the **largest possible coherent amplification**, namely the full unsigned copy-rate of the late multiplier. Thus coefficient concentration becomes source concentration exactly when the large-deviation rate beats the remaining copy entropy.

The corresponding critical radius is

\[
\boxed{
\varepsilon_{k,D}^{\rm src}
:=
\frac{T_{k,D}}
{\sqrt{32\log2\,\delta_k\delta_D}}.
}
\tag{4}
\]

For every `eta>0`, choosing `epsilon=(1+eta) epsilon_{k,D}^{src}` gives the explicit bound

\[
\boxed{
\frac{E_0(X_{k,D,A}^{\rm out})^{1/2}}
{E_0(X_A^{(k)})^{1/2}}
\le
2\exp\!\left[-\left(\eta+\frac{\eta^2}{2}\right)T_{k,D}A\right].
}
\tag{5}
\]

Now assume the positive-residual-slack branch

\[
\delta_\infty>0.
\tag{6}
\]

Define one radius using the **entire future tail** rather than a chosen terminal depth,

\[
\boxed{
\varepsilon_{k,\eta}^{\infty}
:=
\frac{(1+\eta)T_k^\infty}
{\sqrt{32\log2\,\delta_k\delta_\infty}}.
}
\tag{7}
\]

Then for every finite `D>k`, uniformly in `D`,

\[
\boxed{
\frac{E_0(X_{k,D,A}^{\rm out}(\varepsilon_{k,\eta}^{\infty}))^{1/2}}
{E_0(X_A^{(k)})^{1/2}}
\le
2\exp\!\left[-\left(\eta+\frac{\eta^2}{2}\right)T_k^\infty A\right].
}
\tag{8}
\]

Since `delta_k downarrow delta_infinity`,

\[
\boxed{\varepsilon_{k,\eta}^{\infty}\longrightarrow0.}
\tag{9}
\]

Therefore, after cutting sufficiently deep, **all still-later layers are source-negligible outside an arbitrarily small fixed linear neighborhood of their common barycenter**, uniformly over how many additional finite layers are applied. Combining this with the slow-diagonal principle of `ANF-138` gives a further diagonal on which the late multiplier can be trimmed, in Montgomery--Taylor source norm, to a window `r_A=o(A)` around its barycenter while both the cut depth and the terminal depth tend to infinity.

This is a source-weighted answer to one half of the gate in `ANF-139`: exponentially thin coefficient tails cannot remain source-relevant arbitrarily far into the physical support once the **remaining** slack spend is small. It does not yet close the cascade. The central late cloud, although `o(A)` wide on a suitable diagonal, can still create violent phase cancellation at `alpha=Theta(1)`, and the fixed prefix before the cut can retain `Theta(A)` physical span. The remaining positive-residual-slack problem is therefore no longer whether arbitrarily remote late coefficient tails can hide the source. It is whether an increasingly narrow late positive cloud can keep annihilating the finite-prefix source skeleton without becoming source-excisable.

## 1. The late multiplier has both a vanishing copy budget and a restricted variance budget

Use the nested cascade notation of `ANF-133`--`ANF-139`. At physical scale `A`, write the tail multiplier from stages `k+1` through `D` as

\[
\mathcal P_{k:D,A}(\alpha)
=
\prod_{d=k+1}^{D}
\prod_{j=1}^{J_{d-1}}
\left(1+e^{-2\pi i\tau_{j,d-1}\alpha}\right)^{m_{d,A}},
\qquad
m_{d,A}:=\lfloor\theta_dA\rfloor.
\tag{10}
\]

Expand with positive multiplicity,

\[
\mathcal P_{k:D,A}(\alpha)
=
\sum_\omega c_{\omega;k,D,A}e^{-2\pi i\omega\alpha},
\qquad
c_{\omega;k,D,A}\ge0,
\tag{11}
\]

and put

\[
V_{k,D,A}:=\sum_\omega c_{\omega;k,D,A}.
\tag{12}
\]

The exact slack spend identity

\[
s_d=2\theta_dJ_{d-1}\log2
\tag{13}
\]

and the floor inequality `m_{d,A}<=theta_d A` give

\[
\begin{aligned}
\log V_{k,D,A}
&=(\log2)\sum_{d=k+1}^{D}m_{d,A}J_{d-1}\\
&\le
A(\log2)\sum_{d=k+1}^{D}\theta_dJ_{d-1}\\
&=\frac A2\sum_{d=k+1}^{D}s_d
=\frac A2T_{k,D}.
\end{aligned}
\tag{14}
\]

Thus the maximum coherent amplitude available to the whole late multiplier has exponential rate at most `T_{k,D}/2`.

Normalize the coefficients in (11) to a probability law and let `W_{k,D,A}` be the corresponding random translation. The Bernoulli representation of `ANF-139` applies verbatim after deleting the first `k` layers. Its centered variance proxy is

\[
\Sigma_{k,D,A}
:=
\sum_{d=k+1}^{D}m_{d,A}
\sum_{j=1}^{J_{d-1}}\tau_{j,d-1}^2.
\tag{15}
\]

The `p=2` slack-moment telescope of `ANF-139`, restricted to the same stages, gives

\[
\boxed{
\Sigma_{k,D,A}
\le
\frac{A}{8\log2}
\left(\frac1{\delta_D}-\frac1{\delta_k}\right)
=
\frac{AT_{k,D}}
{8\log2\,\delta_k\delta_D}.
}
\tag{16}
\]

If

\[
\bar\omega_{k,D,A}:=\mathbb E W_{k,D,A},
\]

then the elementary Hoeffding estimate already proved inside `ANF-139` yields

\[
\begin{aligned}
\mu_{k,D,A}\left(
|W_{k,D,A}-\bar\omega_{k,D,A}|
\ge\varepsilon A
\right)
&\le
2\exp\!\left(-\frac{2\varepsilon^2A^2}{\Sigma_{k,D,A}}\right)\\
&\le
2\exp\!\left(
-\frac{16\log2\,\varepsilon^2\delta_k\delta_D}{T_{k,D}}A
\right).
\end{aligned}
\tag{17}
\]

This is the coefficient-tail rate. The only remaining question is how much source norm that coefficient tail can recover coherently.

## 2. Montgomery--Taylor source turns unsigned coefficient mass into a universal coherence ceiling

Introduce the source seminorm

\[
\|Y\|_0
:=E_0(Y)^{1/2}
=
\left(
\int_{-1}^{1}J_0(\alpha)|S_Y(\alpha)|^2\,d\alpha
\right)^{1/2}.
\tag{18}
\]

A real horizontal translation by `omega` multiplies the spectral sum by a unit-modulus phase,

\[
S_{T_\omega Y}(\alpha)
=e^{-2\pi i\omega\alpha}S_Y(\alpha),
\tag{19}
\]

and therefore

\[
\boxed{\|T_\omega Y\|_0=\|Y\|_0.}
\tag{20}
\]

This is the key source-side fact. No pointwise sign condition on the physical Montgomery--Taylor kernel is required; the argument stays in its native weighted `L^2` representation.

Let `B` be any subset of the late translation coefficients and form the corresponding physical submultiset

\[
Z_B
:=
\sum_{\omega\in B}
c_{\omega;k,D,A}\,T_\omega X_A^{(k)}.
\tag{21}
\]

The triangle inequality and (20) give the exact universal estimate

\[
\boxed{
\|Z_B\|_0
\le
\left(\sum_{\omega\in B}c_{\omega;k,D,A}\right)
\|X_A^{(k)}\|_0.
}
\tag{22}
\]

Equivalently, if `mu_{k,D,A}(B)` is the normalized coefficient mass of `B`,

\[
\boxed{
\frac{\|Z_B\|_0}{\|X_A^{(k)}\|_0}
\le
V_{k,D,A}\,\mu_{k,D,A}(B).
}
\tag{23}
\]

The right side is deliberately an `ell^1` coherence bound: it allows every retained translate to align perfectly in source space. Hence any decay obtained after (23) cannot be defeated by a more favorable phase arrangement.

Take `B` to be the outer set in (2). Combining (14), (17), and (23) proves (3). The statement is exact at finite `A` up to the displayed one-sided floor inequalities; there is no hidden Laplace prefactor and no chamber-conditioning constant.

## 3. The source threshold is exactly where large-deviation cost beats copy entropy

The exponent in (3) is positive precisely when

\[
\varepsilon
>
\frac{T_{k,D}}
{\sqrt{32\log2\,\delta_k\delta_D}},
\tag{24}
\]

which is (4). Put

\[
\varepsilon
=(1+\eta)
\frac{T_{k,D}}
{\sqrt{32\log2\,\delta_k\delta_D}}.
\tag{25}
\]

Then

\[
\begin{aligned}
\frac{16\log2\,\varepsilon^2\delta_k\delta_D}{T_{k,D}}
-\frac{T_{k,D}}2
&=
\frac{(1+\eta)^2T_{k,D}}2
-\frac{T_{k,D}}2\\
&=
\left(\eta+\frac{\eta^2}{2}\right)T_{k,D},
\end{aligned}
\tag{26}
\]

which proves (5).

This threshold has a useful interpretation. `ANF-139` by itself controls only the **fraction** of coefficients in a remote tail. Equation (14) measures how many unsigned copies exist before that fraction is taken. The product of those two quantities is exactly the strongest possible source amplitude after arbitrary coherence. The source-tail problem therefore has no additional hidden kernel amplification beyond the copy entropy already present in the positive expansion.

For the complete annihilator cloud, `T_{0,D}` may approach a fixed positive constant, so (24) only gives a fixed linear trimming radius. That is why `ANF-139` correctly stopped short of a source-negligible `o(A)` trimming theorem for the whole cloud. The new gain comes from moving the cut `k` deeper, where the unused entropy budget itself tends to zero.

## 4. Positive residual slack makes the source-essential late radius vanish

Assume (6). For a fixed cut `k`, every terminal depth `D>k` obeys

\[
0<T_{k,D}\le T_k^\infty,
\qquad
\delta_D\ge\delta_\infty.
\tag{27}
\]

Use the radius (7) in the exponent of (3). Writing `x=T_{k,D}/T_k^infinity<=1`, one gets

\[
\begin{aligned}
\frac{16\log2\,(\varepsilon_{k,\eta}^{\infty})^2
\delta_k\delta_D}{T_{k,D}}
-\frac{T_{k,D}}2
&\ge
T_k^\infty
\left(
\frac{(1+\eta)^2}{2x}-\frac{x}{2}
\right)\\
&\ge
\left(\eta+\frac{\eta^2}{2}\right)T_k^\infty.
\end{aligned}
\tag{28}
\]

The last expression in parentheses decreases on `0<x<=1`, so its minimum is attained at `x=1`. Equation (28) proves the depth-uniform source estimate (8).

Because the slack sequence decreases to `delta_infinity`,

\[
T_k^\infty=\delta_k-\delta_\infty\longrightarrow0,
\tag{29}
\]

while `delta_k delta_infinity` stays bounded away from zero. Hence (9) follows. In particular, for every prescribed `epsilon>0`, one may first choose a **fixed** cut depth `k` so large that

\[
\varepsilon_{k,\eta}^{\infty}<\varepsilon.
\tag{30}
\]

For that fixed `k`, (8) has a fixed positive exponential rate in `A`, uniformly over all later finite depths. On any `ANF-138` slow diagonal with `D(A)>k` eventually, the fixed stage-`k` source satisfies `E_0(X_A^(k)) asymp E_A`, while the full diagonal source is `e^{o(A)}E_A`. Therefore the outer late tail in (30) is exponentially negligible relative to the **actual** diagonal source as well.

This gives a two-limit statement stronger than coefficient concentration: after a sufficiently deep fixed cut, the source-relevant part of everything still to come lies inside an arbitrarily small prescribed linear fraction of `A` around one barycenter.

One can diagonalize the cut too. Choose fixed pairs

\[
k_1<D_1<k_2<D_2<\cdots
\]

with `k_n->infinity`, and let the scale wait long enough at pair `(k_n,D_n)` that the fixed-depth source comparison constants and the exponential factor in (8) are both dominated. A standard threshold selection, exactly of the type used in `ANF-138`, then produces functions

\[
k(A)<D(A),
\qquad
k(A),D(A)\to\infty,
\tag{31}
\]

and radii

\[
r_A:=\varepsilon_{k(A),\eta}^{\infty}A=o(A)
\tag{32}
\]

such that deleting all late copies with

\[
|\omega-\bar\omega_{k(A),D(A),A}|>r_A
\tag{33}
\]

changes the Montgomery--Taylor source norm by `o(E_0(X_A^(D(A)))^(1/2))`. Thus the positive-residual-slack branch admits an arbitrary-depth diagonal whose **late** source-essential translation cloud has sublinear width modulo a common translation.

## 5. What this removes, and what remains

The coherence escape isolated in `ANF-139` is now sharply constrained. A remote coefficient tail can beat its small probability only by spending unsigned copy entropy. After a deep cut, the entire remaining entropy budget is `T_k^infinity/2`, while the Bernoulli variance budget is proportional to the same vanishing slack tail. Their competition yields the linear threshold (7), which tends to zero. No extra sign or positivity property of the physical source kernel can rescue farther tails, because (22) already grants them perfect Hilbert-space alignment.

This does **not** prove that the cascade is excisable or that `delta_infinity>0`. It also does not turn a sublinear physical late span into a slowly varying spectral multiplier. A translation window `r_A=o(A)` can still satisfy `r_A->infinity`, and at an interior source frequency `alpha=Theta(1)` its phases may oscillate arbitrarily rapidly. In particular, the central late cloud may still annihilate an earlier critical skeleton even though its source-essential physical width is sublinear.

Nor does (32) shrink the entire construction to sublinear width. The stage-`k(A)` prefix is retained as the base object, and it can already have linear physical span. The theorem says something more targeted: **unbounded continuation cannot keep generating source-relevant mass at new macroscopic distances from its own barycenter when positive residual slack survives**. Any remaining obstruction must be encoded in the phase geometry of an increasingly narrow late cloud acting on an earlier prefix, rather than in coherence-amplified remote coefficient tails.

Accordingly `CLUE-near-extremizer-notch-exposure-envelope.md` remains `accepted`, not resolved. The next same-profile gate is to compare this sublinear late-cloud geometry with the exact finite-skeleton annihilation mechanism: determine whether a positive translation multiplier whose source-essential coefficients lie in `o(A)` width can still erase each successive interior critical skeleton without producing a source-negligible/excisable decomposition.

## 6. Prior-art boundary

A directed prior-art audit revisited the classical ingredients around Hoeffding concentration, Bernoulli/Riesz-product coefficient laws, and Hilbert-space norms generated by positive-definite kernels. Those theories contain the separate mechanisms used here: concentration of bounded independent sums and triangle inequalities for coherent sums of translates. The new statement does not require importing either as a black box. `ANF-139` already proves the needed Bernoulli tail estimate from `cosh u<=exp(u^2/2)`, while (18)--(23) are immediate from the defining Montgomery--Taylor weighted `L^2` norm.

The research-specific content is the coupling of those two elementary mechanisms through the exact slack telescope: the late unsigned copy rate is `T_{k,D}/2`, its variance proxy is `T_{k,D}/(8 log 2 delta_k delta_D)`, and positive residual slack forces the **future** spend `T_k^infinity` to vanish. No external theorem is load-bearing, so `SOURCES.md` is unchanged.

**Consequence for `analytic_frontier`.** In the `delta_infinity>0` branch, the weighted-tail ambiguity left by `ANF-139` cannot persist at arbitrarily remote late translations. After a deep enough cut, the remaining cascade is source-tight inside an arbitrarily small linear window; after a further slow diagonalization that window is `o(A)`. The unresolved mechanism has therefore moved inward: the question is now whether **sublinear-width late phase geometry**, rather than macroscopic remote tails, can sustain the infinite saddle-annihilation cascade.