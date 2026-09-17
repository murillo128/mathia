# NB-177 — Square-summable Euler spectrum caps the canonical complexity certificate

**Date:** 2026-09-17  
**Status:** `DERIVED + SOURCE-SPECIFIC + METHOD-BOUNDARY + EULER-FOURIER + NUCLEAR-CERTIFICATE + CAPPED-TRANSPORT + NB-176-STRESS-TEST`.

`NB-176` removes the arbitrary-probe step from the dual complexity certificate of `NB-175`: the actual Euler amplitudes of `zeta'/zeta` define a canonical Hilbert feature map, and the corresponding response Gram gives a directly computable lower certificate for the approximate source complexity `mathfrak L_T(epsilon)`. Its frontier asks whether one can realize arbitrarily many Euler-fingerprint singular directions above the source resolution.

There is a structural obstruction to using that particular witness at arbitrarily high rank. After the capped-transport Fourier estimate is inserted, the squared Euler amplitudes have a **uniformly summable spectral tail**, even as the exterior line approaches `Re s=1`. Finite spectral truncations therefore approximate every bounded-transport fingerprint uniformly. This forces the normalized nuclear response of any `N` templates to decay at least like `N^(-1/4)` up to a square-root logarithm.

The consequence is deliberately a boundary on the **certificate**, not on the underlying sampler family. In the high-ordinate regime, if the capped-transport amplitude is `o(sqrt(log T))`, then the canonical Euler fingerprint certificate of `NB-176` is necessarily `o((log T)^2)` at the `NB-174` source resolution. Thus it cannot by itself certify the amount of approximate source complexity that positive-density logarithmic rescue would require. A stronger argument must retain coherent prime-phase information or use a different jointly contractive witness.

## Claim

Fix one `T` and abbreviate

\[
a:=a_T,\qquad q:=q_T,\qquad 0<a\le1.
\]

Let `nu_1,...,nu_N` be zero-mass finite real signed measures and suppose

\[
\mathsf D_a(\nu_i)\le qX
\qquad(1\le i\le N),
\tag{1}
\]

where `mathsf D_a` is the capped Jordan transport of `NB-167`. Let `G^Eul` be the Euler response Gram of `NB-176`, namely

\[
G^{\mathrm{Eul}}_{ij}
=
\frac1{q^2Z_a^2}
\sum_{n\ge2}
\frac{\Lambda(n)^2}{n^{2+2a}}
\Re\!\left(
\widehat\nu_i(\log n)
\overline{\widehat\nu_j(\log n)}
\right),
\tag{2}
\]

with the order-one normalizer `Z_a` from that finding. Then there is an absolute constant `C` such that

\[
\boxed{
\operatorname{tr}\sqrt{G^{\mathrm{Eul}}}
\le
C X N^{3/4}\sqrt{\log(2N)}.
}
\tag{3}
\]

Equivalently, if `s_1,...,s_N` are the singular values of the infinite Euler response matrix, then

\[
\boxed{
\frac1N\sum_{j=1}^N s_j
\le
C X\frac{\sqrt{\log(2N)}}{N^{1/4}}.
}
\tag{4}
\]

In particular, the spectral sufficient condition from `NB-176`,

\[
G^{\mathrm{Eul}}\succeq \alpha^2 I_N,
\]

can hold only if

\[
\boxed{
\alpha
\le
C X\frac{\sqrt{\log(2N)}}{N^{1/4}}.
}
\tag{5}
\]

So bounded capped amplitude cannot support arbitrarily many Euler-fingerprint directions whose singular scale stays a fixed positive fraction of that amplitude.

There is also a ceiling on the complete canonical certificate. Let `mathfrak C_T^Eul(epsilon)` be the supremum defined in `NB-176`, and let

\[
X_T:=
\sup_{\nu\in\mathcal R_T}
\frac{\mathsf D_{a_T}(\nu)}{q_T}
\]

be the realized-range amplitude from `NB-174`. For `0<epsilon<X_T`,

\[
\boxed{
\mathfrak C_T^{\mathrm{Eul}}(\epsilon)
\ll
\frac{X_T^4}{\epsilon^2}
\log^2\!\left(2+\frac{X_T}{\epsilon}\right).
}
\tag{6}
\]

If `epsilon>=X_T`, then

\[
\boxed{
\mathfrak C_T^{\mathrm{Eul}}(\epsilon)=0.
}
\tag{7}
\]

Consequently, in the high-ordinate regime

\[
H_T=\frac{\log T}{\log\log T},
\qquad
\epsilon_T\asymp \frac{\log T}{H_T}\asymp\log\log T,
\tag{8}
\]

one has

\[
\boxed{
X_T=o(\sqrt{\log T})
\quad\Longrightarrow\quad
\mathfrak C_T^{\mathrm{Eul}}(\epsilon_T)
=o((\log T)^2).
}
\tag{9}
\]

Under `Ta_T^2 -> infinity`, `NB-174` says that positive-density `q_T log T` rescue requires

\[
\mathfrak L_T(\epsilon_T)\gg (\log T)^2.
\]

Equation (9) therefore identifies a broad regime in which the actual approximate complexity may still be large, but the canonical Euler-Gram witness of `NB-176` is provably too compact to certify the required scale.

## Derivation

### Capped transport makes the Euler feature tail uniformly square summable

Write, as in `NB-176`,

\[
c_{n,a}:=\frac{\Lambda(n)}{n^{1+a}},
\qquad
w_{n,a}:=\frac{c_{n,a}}{Z_a}.
\]

The `n=2` term alone gives a uniform lower bound

\[
Z_a\ge 2\frac{\log2}{2^{1+a}}
\ge\frac{\log2}{2}
\qquad(0<a\le1).
\tag{10}
\]

The capped Fourier estimate of `NB-168`, applied to (1), gives

\[
\frac{|\widehat\nu_i(\log n)|}{q}
\le
2X(1+a\log n).
\tag{11}
\]

For `x=a\log n>=0`,

\[
e^{-2x}(1+x)^2\le1,
\tag{12}
\]

because its logarithmic derivative is `-2x/(1+x)<=0`. Combining (10)--(12), the squared norm contributed by the cosine/sine pair at the Euler frequency `log n` is bounded by

\[
\frac{c_{n,a}^2}{q^2Z_a^2}
|\widehat\nu_i(\log n)|^2
\ll
X^2\frac{\Lambda(n)^2}{n^2}.
\tag{13}
\]

This is the key uniform compactness estimate: the factor that seemed capable of growing like `1+a log n` is exactly absorbed by the exterior damping `n^{-a}`.

Since `Lambda(n)<=log n`, for every integer `M>=2`,

\[
\sum_{n>M}\frac{\Lambda(n)^2}{n^2}
\le
\sum_{n>M}\frac{(\log n)^2}{n^2}
\ll
\frac{\log^2(2M)}{M}.
\tag{14}
\]

Thus the Euler fingerprint of every template in the normalized capped-transport ball has a uniform Hilbert tail

\[
\boxed{
\|R_{>M}(\nu_i)\|_2
\ll
X\frac{\log(2M)}{\sqrt M}.
}
\tag{15}
\]

No prime number theorem is used here. The crude inequality `Lambda(n)<=log n` already gives the required uniform spectral compression.

### Finite spectral truncation caps the nuclear response

Let `A` be the infinite real response matrix from `NB-176`, with two columns for each nonzero von Mangoldt coordinate, so that

\[
AA^{\mathsf T}=G^{\mathrm{Eul}},
\qquad
\|A\|_*=\operatorname{tr}\sqrt{G^{\mathrm{Eul}}}.
\tag{16}
\]

Split

\[
A=A_{\le M}+A_{>M}
\]

according to `n<=M` and `n>M`. Because the full Euler feature map is jointly contractive, every row of `A` has Euclidean norm at most `X`. Hence

\[
\|A_{\le M}\|_F\le X\sqrt N,
\qquad
\operatorname{rank}(A_{\le M})\le2M,
\]

and therefore

\[
\|A_{\le M}\|_*
\le
\sqrt{2M}\,\|A_{\le M}\|_F
\ll
X\sqrt{MN}.
\tag{17}
\]

For the tail, (15) gives

\[
\|A_{>M}\|_F
\ll
X\sqrt N\frac{\log(2M)}{\sqrt M}.
\]

Since its rank is at most `N`,

\[
\|A_{>M}\|_*
\le
\sqrt N\,\|A_{>M}\|_F
\ll
XN\frac{\log(2M)}{\sqrt M}.
\tag{18}
\]

The nuclear triangle inequality yields

\[
\frac{\|A\|_*}{N}
\ll
X\left(
\sqrt{\frac MN}
+
\frac{\log(2M)}{\sqrt M}
\right).
\tag{19}
\]

Taking

\[
M\asymp \sqrt N\,\log(2N)
\]

for large `N`, and absorbing the finitely many small values of `N` into the constant, gives

\[
\frac{\|A\|_*}{N}
\ll
X\frac{\sqrt{\log(2N)}}{N^{1/4}},
\]

which proves (3)--(4). If `G^Eul >= alpha^2 I_N`, all `N` singular values are at least `alpha`; hence `N alpha<=||A||_*`, and (5) follows.

### The full NB-176 lower certificate has a finite positive-resolution ceiling

For one `N`-template configuration, the `NB-176` certificate is

\[
\mathfrak C_{T,N}^{\mathrm{Eul}}(\epsilon)
=
\frac{(\|A\|_* - \epsilon N)_+^2}{N}.
\tag{20}
\]

Because every row norm is at most `X_T`,

\[
\|A\|_*
\le
\sqrt N\,\|A\|_F
\le
NX_T.
\tag{21}
\]

This proves (7). Assume now `0<epsilon<X_T`. By (3), positivity of (20) requires

\[
\epsilon
<
C X_T N^{-1/4}\sqrt{\log(2N)}.
\tag{22}
\]

The elementary inversion of (22) gives

\[
N
\ll
\left(\frac{X_T}{\epsilon}\right)^4
\log^2\!\left(2+\frac{X_T}{\epsilon}\right).
\tag{23}
\]

For completeness, this is just the standard bootstrap of `y<=R sqrt(log(2y))`: once `y=N^(1/4)` and `R` is a fixed multiple of `X_T/epsilon`, taking logarithms shows `log(2N)=O(log(2+R))`, which substituted back into (22) gives (23).

Dropping the negative term in (20) and using (3),

\[
\mathfrak C_{T,N}^{\mathrm{Eul}}(\epsilon)
\le
\frac{\|A\|_*^2}{N}
\ll
X_T^2 N^{1/2}\log(2N).
\tag{24}
\]

Substituting (23) into (24) gives (6), uniformly over `N` and the chosen templates. Taking the supremum proves the asserted ceiling for `mathfrak C_T^Eul(epsilon)`.

Finally, under (8), if `X_T=o(sqrt(log T))`, then

\[
\log\!\left(2+\frac{X_T}{\epsilon_T}\right)
=O(\log\log T),
\]

so (6) gives

\[
\mathfrak C_T^{\mathrm{Eul}}(\epsilon_T)
\ll X_T^4
=o((\log T)^2),
\]

proving (9).

## What this says about the adaptive-rescue frontier

There are now three distinct scales in the high-ordinate regime. `NB-167` gives pointwise geometric suppression when

\[
X_TH_T=o(\log T),
\]

which here is roughly `X_T=o(log log T)`. Above that scale an adaptive source is no longer excluded pointwise by capped transport alone. `NB-174` then says that positive-density rescue can survive only if the template family has approximate source complexity of order `(log T)^2` at tolerance `epsilon_T asymp log log T`.

`NB-177` shows that the canonical Hilbert witness introduced in `NB-176` cannot certify that requirement throughout the much larger range

\[
\log\log T\ \lesssim\ X_T\ =o(\sqrt{\log T}).
\tag{25}
\]

The obstruction is not lack of exact Euler frequencies: all prime powers are present. It is the **square-summed representation itself**. The amplitudes `Lambda(n)n^{-1-a}` have enough `ell_2` decay that bounded-transport fingerprints become uniformly finite-dimensional at every fixed positive resolution. Adding more templates eventually adds mostly sub-resolution singular directions, and the nuclear witness saturates.

This does not restore the arithmetic rescue. A small `mathfrak C_T^Eul` does not imply a small `mathfrak L_T`; `NB-175` and `NB-176` are one-sided lower certificates. Equation (9) therefore identifies a methodological gap, not a new impossibility theorem for the sampler. A family could possess genuinely large capped-transport complexity that the Euler Hilbert embedding compresses.

The next useful attack must therefore do one of two things: prove directly that source-natural Nyman template families have small `mathfrak L_T(epsilon_T)`, or build a source-faithful witness that preserves more of the **coherent scalar phase alignment** in

\[
\sum_n
\frac{\Lambda(n)}{n^{1+a_T}}
 n^{-it}\widehat\nu_{T,t}(\log n)
\]

than the squared-amplitude Gram of `NB-176`. The latter points toward a maximal/time-frequency or phase-sensitive certificate rather than another static `ell_2` embedding.

## Stress test and exact boundary

The estimate is uniform as `a->0`; no hidden `1/a` factor enters (15). This is precisely because `e^{-2a log n}(1+a log n)^2<=1`. If that damping were discarded before estimating the Fourier coefficient, the spectral tail would be falsely enlarged and the conclusion would be much weaker.

The result also does not assume a finite total variation bound. The Fourier estimate is paid entirely in capped Jordan transport, so arbitrarily large positive and negative masses may nearly cancel at sub-Poisson distance. What matters is the same normalized amplitude `X_T` already used by `NB-167` and `NB-174`.

The exponent `1/4` in (3) is not claimed optimal. It comes from a deliberately elementary balance between a rank-`O(M)` spectral head and an `O(log M/sqrt M)` Hilbert tail. A prime-number-theorem estimate for the squared von Mangoldt tail could improve logarithmic factors, and more refined approximation-number arguments could sharpen the power-law presentation. Neither would change the qualitative conclusion needed here: at every positive relative resolution the canonical Euler embedding has a finite effective dimension, and in the sub-root-log amplitude regime its `NB-176` certificate is below the `(log T)^2` adaptive-rescue threshold.

Nor does the finding say that the scalar Euler response is compact in height. The coherent phases `n^{-it}` are exactly what were removed when `NB-176` passed to the Hilbert Gram. The present ceiling is therefore evidence that those phases may be the missing information carrier, not evidence that they are harmless.

## Representation and prior-art audit

The generic functional-analytic mechanism is classical. Fourier/RKHS embeddings of finite signed measures and their spectral truncations are standard, and approximation/entropy numbers of compact maps provide an abstract language for the same phenomenon. Sriperumbudur, Gretton, Fukumizu, Schoelkopf and Lanckriet, *Hilbert Space Embeddings and Metrics on Probability Measures*, JMLR 11 (2010), 1517--1561, is representative context for Fourier feature embeddings of measures; R. M. Edmunds, *Inequalities between Entropy and Approximation Numbers of Compact Maps*, Z. Anal. Anwend. 7 (1988), 223--227, is representative context for compact-map approximation-number language.

A focused search over Nyman--Beurling, Euler/logarithmic-derivative Fourier representations, RKHS measure embeddings and compact-operator approximation numbers found the standard ingredients but not this exact source-side consequence. No absence claim is used as evidence of novelty.

No external compact-operator theorem is load-bearing here. Equations (13)--(24) are proved directly from the capped Fourier estimate already persisted in `NB-168`, the Euler feature normalization of `NB-176`, `Lambda(n)<=log n`, and elementary Schatten/rank inequalities. Therefore `research/nyman_beurling/SOURCES.md` is unchanged.

## Evidence ledger

**Internal load-bearing dependencies:** `NB-168` for the capped-transport Fourier coefficient estimate; `NB-174` for `X_T`, `mathfrak L_T(epsilon)` and the source-resolution threshold; `NB-176` for the canonical Euler feature map and Gram certificate.

**External load-bearing dependencies:** none.

**Context-only prior art consulted:** classical RKHS/Fourier embeddings of measures and compact-map approximation-number theory; no theorem from that literature is imported into the proof.

## Frontier moved

`NB-176` asked whether many source-natural templates could realize many Euler-fingerprint singular values above the `NB-174` tolerance. The answer is now constrained before any Nyman-specific parametrization is inspected: **bounded capped amplitude makes the actual Euler Hilbert witness uniformly spectrally compact**. Its average singular scale decays with the number of templates, and at high ordinate it cannot certify the critical `(log T)^2` complexity when `X_T=o(sqrt(log T))`.

This separates geometric source complexity from coherent arithmetic selectivity more sharply than before. If adaptive rescue survives in the newly exposed window, the decisive information cannot be obtained merely by accumulating more square-summed Euler fingerprint directions; it must enter through a stronger description of the template family or through the phase coherence that the canonical Gram deliberately forgets.
