# WI-190 — almost-all prime uniformity can hide the entire B-process alias locus

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`. This finding closes the most direct post-WI-189 attempt to control the unresolved count-saturating bow by applying the 2026 almost-all short-interval von-Mangoldt/nilsequence theorem separately on the natural stationary cells produced by a van-der-Corput `B` process. The obstruction is sharper than the generic ambient-normalization warning in WI-053: the exact stationary geometry gives a deterministic union of relevant alias neighborhoods whose total measure is small enough to fit entirely inside the theorem's permitted exceptional set whenever those neighborhoods are long enough for the theorem to apply. When they are shorter, they fall below the theorem's length threshold. Thus, for every fixed bow exponent `0<epsilon<1/2`, the currently published almost-all theorem cannot by itself certify the deterministic alias family required by WI-188--WI-189.

This is a route closure, not a lower bound for the twisted prime covariance. It does not assert that the alias neighborhoods are actually exceptional, nor that the covariance is large. It shows only that the theorem's quantifiers permit exactly that failure, so a proof needs a theorem uniform on this structured alias locus, a joint bilinear/spectral estimate for the shifted-prime covariance, or cancellation across the dual `(h,k)` family itself.

## 1. Exact B-dual of the WI-188 chirp

On a central dyadic prime block `m \asymp X`, write the WI-188 phase in cycles as

\[
f_h(m)=A\log\!\left(1+\frac hm\right),
\qquad A:=\frac{U}{2\pi}.
\tag{1}
\]

A `B`-process mode `-k`, with `k>0`, has a stationary point when

\[
f_h'(m)=-\frac{Ah}{m(m+h)}=-k.
\tag{2}
\]

Put

\[
y:=\frac hm,
\qquad
q:=\frac{kh}{A}=\frac{2\pi kh}{U}.
\tag{3}
\]

Then (2) is exactly

\[
q=\frac{y^2}{1+y},
\qquad
\boxed{y(q)=\frac{q+\sqrt{q^2+4q}}2}.
\tag{4}
\]

At this stationary point, the negative-Legendre phase is

\[
\begin{aligned}
g(h,k)
&:=f_h(m_{h,k})+k m_{h,k}\\
&=A\left[\log(1+y(q))+\frac{y(q)}{1+y(q)}\right].
\end{aligned}
\tag{5}
\]

Hence the dual phase depends on `h` and `k` only through the product `hk/U`. If

\[
G(q):=\log(1+y(q))+\frac{y(q)}{1+y(q)},
\tag{6}
\]

then its small-`q` expansion is

\[
G(q)=2q^{1/2}-\frac q2+\frac{q^{3/2}}{12}+O(q^{5/2}),
\tag{7}
\]

so

\[
\boxed{
g(h,k)=\sqrt{\frac{2Uhk}{\pi}}-\frac{hk}{2}
+O\!\left(\frac{(hk)^{3/2}}{\sqrt U}\right).}
\tag{8}
\]

The term `-hk/2` is only a parity-type phase on the integer lattice; the leading dual geometry is a square-root/hyperbolic product phase. This exact form does not itself give cancellation, but it identifies the structure that a successful second transformation or bilinear estimate would have to exploit.

## 2. Natural stationary-cell scale

The exact curvature is

\[
f_h''(m)=\frac{Ah(2m+h)}{m^2(m+h)^2}.
\tag{9}
\]

At count saturation, WI-184 gives the reciprocal prime scale

\[
X=T^{1/2+o(1)},
\qquad
\rho:=\frac{U}{X^2}=X^{o(1)},
\tag{10}
\]

while a fixed Maynard--Pratt bow exponent `0<epsilon<1/2` gives

\[
H:=H_{\rm bow}=\frac{T^\epsilon}{\log T}\,T^{o(1)}
=X^{2\epsilon+o(1)},
\qquad
K:=\frac XH=X^{1-2\epsilon+o(1)}.
\tag{11}
\]

For `h<=K` and `m\asymp X`, (9) has the power-scale form

\[
f_h''(m)\asymp\frac{\rho h}{X}.
\tag{12}
\]

The natural stationary-phase width around an alias is therefore

\[
\boxed{L_h\asymp\sqrt{\frac{X}{\rho h}}.}
\tag{13}
\]

For a fixed positive fraction of the top shifts `h\asymp K`, this becomes

\[
\boxed{L_{\rm top}=X^{\epsilon+o(1)}.}
\tag{14}
\]

This is genuinely a polynomial-phase cell, not an artifact of using a quadratic approximation too far. Differentiating once more gives `|f_h'''(m)| \ll \rho h/X^2`; hence for `h\asymp K`,

\[
|f_h'''|L_{\rm top}^3
\ll \frac{L_{\rm top}}X
=X^{\epsilon-1+o(1)}=o(1).
\tag{15}
\]

Thus short-interval polynomial/nilsequence uniformity is the right *type* of modern source input. The obstruction below is instead its interval-length/exceptional-set interface with the deterministic stationary locus.

## 3. The whole robust alias locus can fit inside the permitted exceptional set

Let `nu_h` be the number of `B`-process integer modes for shift `h`. WI-189 gives the derivative-sweep scale `nu_h \ll 1+\rho h` uniformly over the relevant range. Around every stationary center allow an entire interval of possible starting points of length `O(L_h)`. This deliberately strengthens the attempted application: it does not require a theorem at one isolated center, but gives each alias a natural-width neighborhood in which one may move the local cell.

The measure of the union `E_alias` of all such neighborhoods is bounded by the sum of their lengths:

\[
\begin{aligned}
|E_{\rm alias}|
&\ll \sum_{h\le K}\nu_h L_h\\
&\ll \sum_{h\le K}
\left(1+\rho h\right)
\sqrt{\frac{X}{\rho h}}\\
&\ll \sqrt{\frac{XK}{\rho}}
+\sqrt{\rho X}\,K^{3/2}.
\end{aligned}
\tag{16}
\]

Using `K=X/H`,

\[
\boxed{
|E_{\rm alias}|
\ll \frac{X}{\sqrt{\rho H}}
+\frac{\sqrt\rho\,X^2}{H^{3/2}}
=X^{1-\epsilon+o(1)}+X^{2-3\epsilon+o(1)}.
}
\tag{17}
\]

Now compare this exact geometric scale with the published theorem surface. Matomäki--Radziwiłł--Shao--Tao--Teräväinen, *Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*, Invent. Math. 244 (2026), Theorem 1.1, gives von-Mangoldt/nilsequence discorrelation on almost all intervals once the interval length is at least `X^(1/3+delta)` for fixed `delta>0`, with an exceptional set of starting points of size `O_{A,delta}(X log^{-A}X)`.

There is then a complete fixed-`epsilon` dichotomy:

- If `epsilon<=1/3`, the top-shift cells have length `L_top=X^{epsilon+o(1)}`. They do not meet the theorem's `X^(1/3+delta)` threshold for any fixed positive `delta`; at the endpoint `epsilon=1/3` there is still no fixed positive exponent margin.
- If `epsilon>1/3`, the cells are long enough in principle, but both exponents in (17) are strictly below `1`. Hence, for every fixed `A`,

\[
|E_{\rm alias}|=o\!\left(X\log^{-A}X\right).
\tag{18}
\]

The theorem is therefore logically compatible with **every natural alias neighborhood being contained in its allowed exceptional set**.

This is stronger than saying merely that the centers are deterministic. Even after thickening every center by its full stationary-phase width, the complete structured set one needs to control remains too sparse for an almost-all statement to force a single good alias neighborhood when `epsilon>1/3`.

## 4. The all-interval predecessor does not fill the gap

The same 2026 paper records the corresponding previous all-interval von-Mangoldt/nilsequence result from Part I at the substantially longer threshold `H_short >= X^(5/8+delta)`. In the present bow regime the top stationary cells have length only

\[
L_{\rm top}=X^{\epsilon+o(1)},
\qquad 0<\epsilon<\frac12.
\tag{19}
\]

Thus the available all-interval theorem is also below the required resolution for every admissible fixed bow exponent. Combining the two published theorem surfaces gives

\[
\boxed{
\begin{array}{ll}
0<\epsilon\le1/3:&
\text{the almost-all theorem is too short-interval restrictive};\\[1mm]
1/3<\epsilon<1/2:&
\text{the full alias locus may fit inside its permitted exceptional set};\\[1mm]
0<\epsilon<1/2:&
\text{the all-interval predecessor requires intervals longer than the alias cells}.
\end{array}}
\tag{20}
\]

So there is no fixed `epsilon` window in the count-saturating bow where the currently published short-interval nilsequence results can simply be applied as a black box to every needed `B`-process cell.

## 5. Prior-art audit and evidence boundary

The relevant prime-correlation and short-interval inputs are already anchored in `research/weil_inertia/SOURCES.md`. Matomäki--Radziwiłł--Tao, *Correlations of the von Mangoldt and higher divisor functions I. Long shift ranges*, Proc. London Math. Soc. 118 (2019), gives the pair-correlation asymptotic for all but `O(H log^{-A}X)` shifts down to `H>=X^(8/33+delta)` and explicitly uses van-der-Corput/negative-Legendre machinery in its exponential-sum analysis. The 2026 Inventiones paper above is the primary source for the almost-all `1/3` short-interval nilsequence threshold and for the statement of the preceding all-interval `5/8` threshold for `Lambda`.

These results do not directly estimate the exact source object of WI-188. After expanding the local mean square, the arithmetic coefficient is a **shifted prime pair** `Lambda(m)Lambda(m+h)`, not a single copy of `Lambda`. Thus even a hypothetical theorem controlling the required interval centers would still need a transference/bilinear step or a joint twisted two-prime theorem before it could close the covariance. The present finding isolates a logically earlier failure: the most obvious single-`Lambda` almost-all theorem cannot even guarantee control on the structured stationary locus where such a reduction would have to operate.

WI-053 already warned, in a different Yang/fiber setting, that almost-all higher-uniformity estimates can lose the sparse arithmetic structure one actually needs. The new delta here is the explicit alias-locus computation (16)--(18), derived from the WI-188/WI-189 `B`-process geometry. It shows quantitatively that the entire robust locus can hide inside the allowed exceptional set exactly on the side of the `epsilon=1/3` threshold where the intervals become long enough. A targeted prior-art search did not locate this exact bow-interface calculation. That absence is **not** a priority claim.

No conclusion about the magnitude or sign of the covariance follows. The exceptional set allowed by a theorem need not be the actual exceptional set for these stationary centers, and cancellation may occur across modes, shifts, or arithmetic decompositions. The result only prevents treating the published almost-all theorem as a completed source-level input.

## 6. Research consequence: the next source theorem should see the hyperbolic alias family itself

WI-189 showed that shortening the prime polynomial does not reduce the aggregate stationary-alias budget. The exact dual formula (5) now shows what survives after passing to those aliases: a phase depending on `h,k` through `q=2pi hk/U`, with leading square-root behavior `sqrt(2Uhk/pi)`. The natural next source target is therefore not another scalar short-interval theorem applied independently to each stationary cell.

A viable input must instead do at least one of the following: control von-Mangoldt (or shifted-prime-pair) sums uniformly on the deterministic alias locus; average over the `(h,k)` hyperbolic family in a way whose exceptional set cannot swallow that family; or exploit bilinear/spectral cancellation in the product phase `G(2pi hk/U)`. A second blind `B` process is not automatically a simplification, since the Legendre transform is involutive at the phase level and the top-mode geometry is self-dual up to the existing `X^{o(1)}` scale uncertainty.

This redirects the canonical defect-elimination program toward a source theorem matched to the actual alias geometry rather than toward another percentage optimization or a generic almost-all short-interval black box.