# WI-195 — multiplicative Gallagher bridge exposes the bow L2 gate

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`.

WI-193--WI-194 show that the count-saturating bow cannot be closed by fixed-shift modulus bounds plus absolute assembly, nor by a bare two-dimensional stationary transform of the logarithmic phase. There is, however, an exact way to keep the whole shift family coupled before any B-process: choose a triangular Fourier localizer in the height variable. The resulting localized Montgomery square is exactly a multiplicative short-interval mean square of the prime Dirichlet polynomial.

This exact bridge brings a recent theorem much closer to the live source object than the stationary-cell application tested in WI-190. Matomäki--Radziwiłł--Shao--Tao--Teräväinen, *Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*, Invent. Math. 244 (2026), Theorem 3.1(i), controls precisely the Archimedean twist

\[
(\Lambda(n)-\Lambda^\sharp(n))n^{-i\tau}
\]

on almost all additive intervals of length at least `X^(1/3+eta)`, uniformly for `|tau|<=X^C`. At the difficult bow scale `epsilon<1/4`, the multiplicative interval length is

\[
K=X/H_{\rm bow}=X^{1-2\epsilon+o(1)},
\]

so both its interval-length threshold and its polynomial-twist range are comfortably satisfied when `tau=U\asymp X^(2+o(1))`.

The obstruction is not resolution and, even if one removes the exceptional set entirely, it is not the almost-all quantifier. It is **norm strength**. The bow square requires a diagonal-scale `L^2` estimate of order `X K log X` for the raw short sums. Theorem 3.1 gives only the linear-amplitude bound `K log^{-A} X`. Squaring and integrating even that stronger hypothetical all-interval bound gives `X K^2 log^{-2A}X`, larger than the required scale by

\[
\boxed{\frac{K}{\log^{2A+1}X}=X^{1-2\epsilon+o(1)}\log^{-2A-1}X\to\infty}
\]

for every fixed `A`. Its permitted exceptional set is an additional loss, not the fundamental one. Thus the current published major-arc theorem cannot be inserted as a black-box transference from `\Lambda` to `\Lambda^\sharp` in the bow covariance, despite matching the exact twist and interval exponents.

This is a different obstruction from WI-190. WI-190 applies the same 2026 almost-all technology separately to natural B-process stationary cells and finds a length/exceptional-locus dichotomy. Here no B-process is taken: the original joint covariance is represented exactly as a short-interval `L^2` norm, its intervals are already longer than the `1/3` threshold throughout the hard `epsilon<1/4` regime, and the gap survives even under an all-interval strengthening with the same pointwise amplitude.

The resulting source target is sharper than “find joint cancellation across shifts.” A viable major-arc route must prove **square-root-scale variance**, schematically

\[
\int_X^{2X}
\left|\sum_{x<n\le x+K}(\Lambda(n)-\Lambda^\sharp(n))n^{-iU}\right|^2dx
=o(XK\log X),
\]

with the actual smooth source weights restored, and must then control the structured `\Lambda^\sharp` contribution in the same Fejér/Gallagher norm. No unconditional zeta-zero proportion changes here.

## 1. Exact multiplicative triangular identity

Let `b_n` be any square-summable sequence and let `delta>0`. Directly opening the square gives

\[
\begin{aligned}
\int_{\mathbb R}
\left|\sum_{e^y<n\le e^{y+\delta}}b_n\right|^2dy
&=\sum_{m,n}b_n\overline{b_m}\,
\left|[\log n-\delta,\log n)\cap[\log m-\delta,\log m)\right|\\
&=\boxed{\sum_{m,n}b_n\overline{b_m}
\left(\delta-|\log(n/m)|\right)_+.}
\end{aligned}
\tag{1}
\]

The identity is just overlap measure in logarithmic coordinates; no asymptotic, pair-correlation hypothesis, or arithmetic input enters.

Use the Fourier convention of WI-188,

\[
\widehat W(\xi)=\int_{\mathbb R}W(u)e^{iu\xi}\,du,
\]

and choose

\[
\widehat W(\xi)=(1-|\xi|)_+.
\tag{2}
\]

Its inverse Fourier transform is the nonnegative even integrable localizer

\[
W(u)=\frac{1-\cos u}{\pi u^2}
\]

with the continuous value at `u=0`. Put `delta=1/H` in (1). Then

\[
\boxed{
H^2\int_{\mathbb R}
\left|\sum_{e^y<n\le e^{y+1/H}}b_n\right|^2dy
=
H\sum_{m,n}b_n\overline{b_m}
\widehat W\!\left(H\log\frac nm\right).
}
\tag{3}
\]

Now take the BGSTB/WI-188 source coefficients

\[
a_X(n)=\frac{\Lambda(n)}{\sqrt n}q_X(n)
\]

(with a harmless smooth dyadic cutoff when isolating the central block) and set

\[
b_n=a_X(n)n^{iU}.
\tag{4}
\]

The right side of (3) is exactly the triangular-localizer version of the height-localized source square in WI-188, up to the immaterial orientation obtained by exchanging `m,n`. Thus the physical-shift family `|n-m|\lesssim X/H` is not merely analogous to a short-interval problem: for this admissible localizer it is an exact positive `L^2` norm.

On `n\asymp X`, the multiplicative interval in (3) has additive length

\[
J_x=x(e^{1/H}-1)=\frac{x}{H}\left(1+O(H^{-1})\right).
\tag{5}
\]

Writing

\[
K:=\frac XH,
\tag{6}
\]

all central-block intervals therefore have length `asymp K`.

## 2. The bow scale lies well inside the 2026 major-arc range

Retain the count-saturating notation of WI-188--WI-194:

\[
X=T^{1/2+o(1)},
\qquad
U\asymp T,
\qquad
H=H_{\rm bow}=\frac{T^\epsilon}{\log T},
\qquad 0<\epsilon<\frac12.
\tag{7}
\]

Then

\[
\boxed{
K=\frac XH=X^{1-2\epsilon+o(1)}.
}
\tag{8}
\]

Theorem 3.1(i) of Matomäki--Radziwiłł--Shao--Tao--Teräväinen states that if a short interval length `J` satisfies

\[
X^{1/3+\eta}\le J\le X
\tag{9}
\]

for fixed positive `eta`, and if `|tau|<=X^C`, then for every fixed `A>0`, outside a set of starting points of measure `O_{A,eta,C}(X log^{-A}X)`,

\[
\boxed{
\left|\sum_{x<n\le x+J}
(\Lambda(n)-\Lambda^\sharp(n))n^{-i\tau}
\right|^*
\le J\log^{-A}X.
}
\tag{10}
\]

Here

\[
\Lambda^\sharp(n)=\frac{P(R)}{\varphi(P(R))}
1_{(n,P(R))=1},
\qquad
R=\exp((\log X)^{1/10}),
\tag{11}
\]

in the source normalization.

For every fixed `epsilon<1/4`, equation (8) gives

\[
K\ge X^{1/2+o(1)},
\tag{12}
\]

so (9) holds with a fixed exponent margin. Also `U=X^{2+o(1)}`, hence `|U|<=X^C` for any fixed `C>2` once `X` is large. Therefore this primary theorem genuinely matches the **interval and Archimedean-twist ranges** of the difficult bow regime. This is stronger alignment than the generic nilsequence comparison alone suggests.

The small variation of the multiplicative interval length in (5), the factors `q_X(n)/sqrt n`, and a smooth dyadic cutoff can only make the attempted black-box application more technical. For the negative norm comparison below, grant a lossless transfer of (10) to those weights and even grant the estimate on **every** interval rather than almost all intervals. The theorem is still too weak.

## 3. The bow square needs diagonal-scale variance

Define the raw major-arc error short sum

\[
E_x(U;K)
:=\sum_{x<n\le x+K}
(\Lambda(n)-\Lambda^\sharp(n))n^{iU}.
\tag{13}
\]

On `n\asymp X`, the `1/sqrt n` source normalization and `dy=dx/x` in (3) contribute two powers of `X^{-1/2}`. Consequently the source contribution associated to (13) has scale

\[
\frac{H^2}{X^2}
\int_X^{2X}|E_x(U;K)|^2dx
\tag{14}
\]

up to fixed dyadic/source-weight constants.

The full `\Lambda` diagonal satisfies

\[
\sum_{n\asymp X}\Lambda(n)^2\asymp X\log X,
\tag{15}
\]

so the raw triangular short-interval diagonal is

\[
\asymp XK\log X.
\tag{16}
\]

Indeed, substituting `K=X/H` into (14) turns (16) into

\[
\frac{H^2}{X^2}(XK\log X)
=H\log X,
\tag{17}
\]

which is exactly the diagonal scale of the localized BGSTB prime square.

Thus a clean transference that discards the `\Lambda-\Lambda^\sharp` part at the source-square level needs, at least schematically,

\[
\boxed{
\int_X^{2X}|E_x(U;K)|^2dx
=o(XK\log X).
}
\tag{18}
\]

The natural typical amplitude encoded by (18) is

\[
|E_x|\ll o\!\left(\sqrt{K\log X}\right)
\]

in quadratic mean. This is the norm scale required by the bow, not merely a logarithmic saving from the trivial linear scale `K`.

## 4. The published major-arc bound misses this scale by a polynomial factor

Now strengthen Theorem 3.1 dramatically for the sake of testing its information content: suppose (10), with `J=K` and `tau=U`, held for **every** `x`, with no exceptional set and no cost for the smooth source weights. Then it would give only

\[
\int_X^{2X}|E_x(U;K)|^2dx
\le
\frac{XK^2}{\log^{2A}X}.
\tag{19}
\]

Comparing (19) with the target (18),

\[
\boxed{
\frac{XK^2\log^{-2A}X}{XK\log X}
=
\frac{K}{\log^{2A+1}X}.
}
\tag{20}
\]

At the bow scale (8), for every fixed `A`,

\[
\frac{K}{\log^{2A+1}X}
=X^{1-2\epsilon+o(1)}\log^{-2A-1}X
\longrightarrow\infty.
\tag{21}
\]

The theorem allows `A` to be any fixed constant, with constants depending on `A`; it does not provide uniformity for `A=A(X)` growing rapidly enough to convert a polynomial `K` into a logarithmic loss. Therefore its stated amplitude control, even upgraded from almost-all to all intervals, cannot certify (18) by squaring and integrating.

The actual exceptional set makes the interface still weaker. Its permitted measure is `O(X log^{-A}X)`. Even a crude pointwise bound `|E_x|\ll K\log X` there permits a contribution

\[
\ll X K^2\log^{2-A}X,
\tag{22}
\]

whose ratio to (16) is `K log^{1-A}X`, again polynomially large for each fixed `A`. But (20)--(21) show that this is not merely another version of the exceptional-set obstruction in WI-190: the good-set amplitude itself is above the required quadratic scale.

The proof architecture in the primary source is consistent with this diagnosis. Its Lemma 3.3 explicitly converts short-interval variance to Dirichlet-polynomial mean squares, while the Type-II major-arc estimates feeding Theorem 3.1 prove variance bounds of the form `J^2` times a logarithmic saving. In the `\Lambda` case the large-`|tau|` proof invokes its Type-II lemma with a polylogarithmic parameter `W`, producing the arbitrary logarithmic saving needed for (10), not a `J`-scale variance. Thus the gap is present in the published variance input and is not created only by the final Chebyshev step.

## 5. Relation to WI-190 and current prior art

WI-190 audits the same 2026 paper on a **different representation** of the source problem. After a one-dimensional B-process, the natural stationary cells have length `L_top=X^(epsilon+o(1))`. There the almost-all theorem has a dichotomy: for `epsilon<=1/3` the cells are below its `X^(1/3+eta)` length threshold, while for `epsilon>1/3` the entire deterministic alias locus can fit inside the permitted exceptional set.

The present bridge does not pass to those cells. It keeps the original `(m,h)` family coupled and uses the exact positive identity (3). In the hard range singled out by WI-193, `epsilon<1/4`, its physical prime intervals have length

\[
K=X^{1-2\epsilon+o(1)}>X^{1/2+o(1)},
\]

so the `1/3` threshold is no obstacle at all. The obstruction moves from **where** the theorem holds to **how strong a norm** it controls.

The primary source is:

Kaisa Matomäki, Maksym Radziwiłł, Xuancheng Shao, Terence Tao and Joni Teräväinen, **Higher uniformity of arithmetic functions in short intervals II. Almost all intervals**, *Inventiones Mathematicae* 244 (2026), 967--1091, DOI `10.1007/s00222-026-01408-6`, arXiv:2411.05770. The paper was published 26 January 2026. Theorem 3.1(i) is the exact Archimedean major-arc estimate used above; Lemma 3.3 is its Parseval-type variance bridge, and the Type-II estimates in Section 3 are part of the proof mechanism.

The multiplicative overlap identity (1)--(3) is elementary Fourier/Fejer/Gallagher-type algebra and is not claimed as new. A bounded audit located classical short-interval prime exponential-sum and Selberg-integral machinery, including polynomial-phase prime discorrelation, but no published theorem supplying the uniform diagonal-scale variance (18) for the specific high Archimedean twist `U\asymp X^2` together with the `\Lambda-\Lambda^\sharp` decomposition. Absence from this search is not evidence of priority.

## 6. Research consequence

The post-WI-194 source problem can now be stated in a norm-matched way. It is not enough to prove that a typical short prime sum is `o(K)`, even with an arbitrary fixed power of `log X` saved. The bow square asks for a factor of essentially `sqrt K` beyond that scale in quadratic mean.

A viable major-arc program has two separate tasks:

1. strengthen the Archimedean `\Lambda-\Lambda^\sharp` estimate at `U\asymp X^2` from logarithmic linear discorrelation to the diagonal-scale variance (18), with the source weights and multiplicative interval geometry retained; and
2. evaluate or bound the structured `\Lambda^\sharp` contribution in the same positive Fejer/Gallagher norm strongly enough to recover the localized Montgomery diagonal.

The first task is where the existing 2026 Type-I/Type-II machinery is closest but quantitatively underpowered; the second is the major-arc arithmetic that its approximant intentionally leaves behind. A proposal that cites Theorem 3.1 only through `K log^{-A}X` control has not crossed the bow gate, even though its exponent ranges look ideal.

No conclusion about the true size of the twisted covariance follows from this information barrier, and no unconditional simple-critical-zero percentage changes. The exact advance is the positive representation (3), the identification of a primary theorem matched to its twist/interval range, and the proof that the published theorem surface misses the required `L^2` scale by a polynomial factor.