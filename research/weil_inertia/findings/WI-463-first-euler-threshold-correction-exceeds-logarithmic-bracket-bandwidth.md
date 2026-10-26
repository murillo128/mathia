# WI-463 — first Euler threshold correction exceeds logarithmic bracket bandwidth

**Status:** EXACT-DERIVED + LITERATURE-REDUCTION + CERTIFICATE-OBSTRUCTION + NO-NOVELTY-CLAIM + NON-RH.

**Local dependencies:** [WI-461](WI-461-fixed-scale-euler-peaks-have-positive-density-at-zeta-zero-ordinates.md), for the coherent tone Gram matrix and leading sampling law; [WI-462](WI-462-prime-power-coherence-lowers-the-zero-sampled-euler-response-mean.md), for the normalization and rational-frequency arithmetic interface.

## Claim and scope

Already the first nonconstant initial truncation of the Euler–Hankel
response, retaining only prime powers at most three, turns its first hard
threshold correction into a classical interval-discrepancy question. Its
signed torus coefficient is **zero at every threshold**, but that fact does
not prove an actual zero-sampling correction of zero.

For every fixed interior threshold, any pointwise finite Fourier brackets
with Haar gap `o(1/log T)` must have physical logarithmic bandwidth
`B_T/log T -> infinity`. This holds even for brackets using both prime
coordinates, with unrestricted coefficients and amplitudes. Consequently
neither the source range used in WI-462 nor the broader `B_T <= log T/8`
comparison in WI-461 can complete this bracket certificate. The obstruction
persists even if all sampling errors inside the permitted band are granted
to be zero.

This is a restriction on a specified certificate, not a counterexample to
an arithmetic threshold asymptotic. It does not preclude cancellation
arguments, control of the high-frequency remainder in a different norm,
or a separate interval-counting theorem.

## The smallest nonconstant initial truncation

Fix `epsilon,r>0` throughout. Put

\[
 A_\varepsilon=-\zeta'(1+\varepsilon)/\zeta(1+\varepsilon),\qquad
 a_n=\frac{\Lambda(n)}{A_\varepsilon n^{1+\varepsilon}},\qquad
 G_r(n,m)=e^{-r|\log(n/m)|}-(nm)^{-r}.
\]

Keep the original normalization; do not renormalize the retained series.
For the negative-Hardy tones `h_omega=P_-(e^{-i omega t}k_(r,0))`,
`<h_(log n),h_(log m)>=G_r(n,m)`. On the two-prime torus set

\[
 \mathscr Q_3(z)=\|a_2z_2h_{\log2}+a_3z_3h_{\log3}\|_2^2
 =c+b\cos v,\qquad v=\arg z_2-\arg z_3,
 \tag{1}
\]
\[
 c=a_2^2(1-2^{-2r})+a_3^2(1-3^{-2r}),\qquad
 b=2a_2a_3[(2/3)^r-6^{-r}]>0.
 \tag{2}
\]

The cutoff at two is constant, so (1) is indeed the first nonconstant
initial cutoff. Gram positivity gives `c>=b`. The relative phase is Haar
uniform. For a fixed `x in (c-b,c+b)`, write

\[
 \alpha=\arccos((x-c)/b)\in(0,\pi),\qquad
 E_x=\{\mathscr Q_3\le x\}=\{v\in[\alpha,2\pi-\alpha]\}.
\]

Thus

\[
 m(E_x)=1-\alpha/\pi,\qquad
 (\mathscr Q_3)_*m(dx)=
 \frac{\mathbf1_{(c-b,c+b)}(x)}{\pi\sqrt{b^2-(x-c)^2}}\,dx.
 \tag{3}
\]

Every interior level is regular; no endpoint singularity or atom is being
used. At the actual prime phases `z_p(t)=e^{-it log p}`, the relative
phase is `v=lambda t`, where `lambda=log(3/2)>0`.

For the finite prime panel define the classical signed coefficient density

\[
 h(z)=-\sum_{p=2,3}\log p\,[K_{p^{-1/2}}(\arg z_p)-1],\qquad
 K_u(\theta)=\frac{1-u^2}{1-2u\cos\theta+u^2}.
 \tag{4}
\]

Common rotation `(z_2,z_3) -> (e^{is}z_2,e^{is}z_3)` preserves (1) and
averages each term of (4) to zero. Therefore, for every bounded measurable
function `f`,

\[
 \int f(\mathscr Q_3)h\,dm=0,\qquad C_3(x):=\int_{E_x}h\,dm=0.
 \tag{5}
\]

This is a Haar identity for an explicitly defined signed density. It is not
an indicator transport theorem. For every fixed smooth `f`, the classical
smooth-test arithmetic formula does give
`log T [sigma_T(f(Q_3))-m(f(Q_3))] -> 0`: all nonconstant frequencies are
integer multiples of `log(3/2)`, and no positive power of `3/2` is an
integer prime power. Here `sigma_T` samples all zeta zeros in `(T,2T]`,
with multiplicity as in WI-462, and `D_T=N(2T)-N(T)`.

Since `D_T ~ T log T/(2 pi)`, the proposed hard-threshold conclusion

\[
 \log T\,[\sigma_T(E_x)-m(E_x)]\longrightarrow0
 \tag{6}
\]

is exactly the statement

\[
 \#\{T<\gamma\le2T:\{\gamma\lambda/(2\pi)\}
       \in[\alpha/(2\pi),1-\alpha/(2\pi)]\}
 -D_T(1-\alpha/\pi)=o(T).
 \tag{7}
\]

Endpoint inclusion is the same on both sides of this equivalence; no
assumption that no zero lands on an endpoint is needed. Equation (7) is a
fixed symmetric-interval, dyadic instance of the interval assertion in
Ford–Soundararajan–Zaharescu, Conjecture 1. Their cumulative conjecture
would imply (7) by subtraction. We do not claim equivalence to their
full interval-uniform conjecture or that every later development has been
excluded by a literature search.

## A bandwidth obstruction before any arithmetic error is paid

Let `I=[alpha,2 pi-alpha]`, `0<alpha<pi`, on the angle circle with
normalized Haar measure. Suppose real trigonometric polynomials `P^-`
and `P^+`, of degree at most `J`, satisfy
`P^- <= 1_I <= P^+` pointwise. No restrictions to `[0,1]` or uniform
amplitude bounds are imposed. Put `D=P^+-P^-`. Then `D>=0`, and continuity
at either boundary point gives `D(alpha)>=1`: the majorant is at least
one on approach from inside, and the minorant is at most zero on approach
from outside. If `d_j` are the Fourier coefficients of `D`, positivity gives
`|d_j|<=d_0=int D`. Hence

\[
 \boxed{\int(P^+-P^-)\,dm\ge\frac1{2J+1}.}
 \tag{8}
\]

Indeed `1<=D(alpha)<=sum_(|j|<=J)|d_j|<=(2J+1)d_0`.
This elementary lower bound suffices; sharp extremal constants are not
required. In particular, with `L=log T`,

\[
 L\int(P_T^+-P_T^-)\,dm\to0
 \quad\Longrightarrow\quad J_T/L\to\infty.
 \tag{9}
\]

Using the full two-prime torus cannot evade (9). Let `P^±(z_2,z_3)` be
finite Laurent-polynomial brackets for `1_(E_x)`, with every nonzero
Fourier mode `(j,k)` satisfying

\[
 |j\log2+k\log3|\le B_T.
 \tag{10}
\]

Average the brackets over common rotation. The event is unchanged, and
only modes with `j+k=0` remain. The resulting one-variable brackets have
degree at most `floor(B_T/lambda)`, and their Haar gap equals the original
gap. Therefore

\[
 \boxed{m(P_T^+-P_T^-)\ge
 \frac1{2\lfloor B_T/\lambda\rfloor+1}.}
 \tag{11}
\]

Large integer indices with nearly cancelling logarithms do not help:
common rotation removes every mode except the relative-phase harmonics.
For any fixed `C`, the restriction `B_T<=C L` leaves the scaled Haar gap
bounded away from zero. The first moving-bracket condition in the local
threshold clue already fails, independently of the signed-density and
sampling-error conditions.

The same restriction applies to smooth brackets reduced to finite Fourier
ones with uniform errors `eta_T=o(1/L)`. If `q^-<=1_E<=q^+` and
`||q^±-P^±||_infinity<=eta_T`, then `P^--eta_T` and `P^++eta_T` are genuine
polynomial brackets and their Haar gap is at most
`m(q^+-q^-)+4 eta_T`. Thus small uniform truncation tails cannot remove
(11). Smooth brackets with substantial uncontrolled high-frequency tails
remain outside this argument.

## Price the available arithmetic interface

For the ratio harmonics `x_j=(3/2)^j`, `1<=j<=J`, put `X=3^J`.
They are nonresonant, have rational numerator and denominator at most `X`,
and meet the rational separation used in WI-462. For example, their
distance from a distinct integer is at least `1/X`, and their logarithmic
distance from the nearest prime power is at least `1/(2X^2)`.

The same Landau and ordinate/weighted-zero estimates yield, uniformly in
this finite bank,

\[
 \frac1T\sum_{T<\gamma\le2T}e^{ij\lambda\gamma}
 =O\left(\frac{J^2}{L}+L^{-10}
       +\frac{3^J L^2+9^J J}{T}\right)=:O(E_{T,J}),
 \tag{12}
\]

provided, for instance, `J log 3 <= L/(100 log L)` and `T` is sufficiently
large. Negative harmonics follow by conjugation. This range ensures the
hypothesis `x<=exp(log T/(50 log log T))` of Ford–Meng–Zaharescu,
Lemma 2, at both dyadic endpoints. The nonresonant Landau main term is
bounded by the prime-power separation, rather than discarded without a
uniform estimate.

For a moving polynomial `P=sum_(|j|<=J)c_j exp(ijv)`, let
`A_J=sum_(0<|j|<=J)|c_j|`. Equation (12) gives the actual coefficient-mass
budget

\[
 |L[\sigma_T(P)-m(P)]|\ll A_J E_{T,J}.
 \tag{13}
\]

There is no fixed-test constant being treated as uniform. However, already
the source range in (12) is incompatible with (9). Even replacing it by
the broader mirror-paired density comparison `|omega|<=L/8` established
in WI-461 would give only `J<=L/(8 lambda)`, still incompatible. Neither
improving coefficient mass nor removing the displayed arithmetic errors
within that band solves the Haar approximation cost.

The conclusion is specifically about pointwise bracketing at `o(1/L)`
resolution using these bands. It does not assert that the right side of
(12) is a lower bound for actual error, or that no stronger arithmetic
estimate can exist.

## Same-prime control: a positive coefficient still needs transport

Retain instead just `p,p^2` for one prime, again with the original
normalization. This is a selective control, not an initial cutoff. Its
response is `c_p+b_p cos theta`, where
`c_p=a_p^2(1-p^(-2r))+a_(p^2)^2(1-p^(-4r))` and
`b_p=2a_p a_(p^2) G_r(p,p^2)>0`. At the regular level
`x=c_p+b_p cos alpha`, `alpha in (0,pi)`, direct integration of the
one-prime density in (4),
with `u=p^(-1/2)`, gives

\[
 \begin{aligned}
 C_{p,p^2}(x)
 &=\frac{2\log p}{\pi}\sum_{k\ge1}\frac{u^k\sin(k\alpha)}k\\
 &=\frac{2\log p}{\pi}
    \arctan\frac{u\sin\alpha}{1-u\cos\alpha}>0.
 \end{aligned}
 \tag{14}
\]

The series is absolutely convergent; the denominator is positive, so the
principal arctangent has the displayed sign. A single tone, or deletion
of all coherent cross terms, gives a constant response and zero signed
coefficient. The two-distinct-prime control has (5). Thus the candidate
coefficient distinguishes prime-power coherence exactly. Equation (14)
does **not** assert stochastic dominance for the actual zeros, the full
Euler response, or even this selective control. Its threshold transport
would require the corresponding prime-phase interval assertion, with
the same bracket bandwidth cost.

## Prior art, audit, and consequence

Ford–Zaharescu, *On the distribution of imaginary parts of zeros of the
Riemann zeta function*, **J. reine angew. Math. 579** (2005), 145–158,
[Corollary 2 and Lemmas 1–2](https://arxiv.org/abs/math/0405459v2), supply
the fixed smooth-test result and the Landau/density framework.
Ford–Meng–Zaharescu, *Simultaneous distribution of the fractional parts of
Riemann zeta zeros*, **BLMS 49** (2017), 1–9,
[Lemma 2](https://arxiv.org/abs/1511.06814v2), states the uniform
ordinate comparison used in (12). No growing-test consequence of their
fixed-test theorem is presumed.

Ford–Soundararajan–Zaharescu, *On the distribution of imaginary parts of
zeros of the Riemann zeta function, II*, **Math. Ann. 343** (2009),
487–505, [§1, (1.3)–(1.4), Conjecture 1 and Theorem 2](https://arxiv.org/abs/0805.2745),
explicitly separate the smooth correction from interval indicators and
relate the latter to stronger arithmetic hypotheses. Our event is a
special dyadic interval, not a new distribution problem in disguise.

Interval approximation and its inverse-bandwidth cost are classical
Fourier-analysis phenomena. Equations (8)–(11) have been proved directly,
without claiming a new extremal theorem. The substantive local delta is
the exact reduction for the **actual first nonconstant Euler cutoff**
and the incompatible bandwidth requirements of its proposed source
certificate. It strengthens the clue's general smooth-to-hard warning
by identifying where that certificate fails before an infinite Euler
tail or parameter limit enters.

The audit checks the Gram sign, original normalization, dyadic `o(T)`
scale, multiplicity convention, common-rotation projection, positivity
of the bracket gap, and source range. As a supplementary floating-point
check, direct Simpson integration of (14) at five interior angles for
each of `p=2,3,7` agreed with its closed form within `9.3e-14`. This is
not rigorous numerical certification and is not an input to the proof.
No Lean formalization or computation handoff is needed for the elementary
Fourier bound; the missing arithmetic interval estimate remains the
substantive difficulty.

The fixed-parameter leading threshold law of WI-461 and the full-series
first mean correction of WI-462 remain intact. The present result does
not decide the first hard-threshold correction for `Q_3`, higher cutoffs,
or the full Euler response. Those require arithmetic information beyond
this certificate. None of these bulk ordinate statistics, even if their
first corrections were established, excludes an individual off-line zero
or identifies the off-line subpopulation.
