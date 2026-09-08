# WI-202 — a current ANTEDB exponent pair lowers the source-safe bow cutoff to 3943/12011

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + PRIOR-ART-REDIRECT + STRUCTURAL-RIGIDITY`.

WI-201 withdrew WI-200's numerical cutoff `1515/4816` because the cited Bourgain--Watt paper does not supply an ordinary exponent pair with that value. The generic theorem surface survived: if `(kappa,lambda)` is a verified ordinary exponent pair, both Khayrulloev's every-interval odd-order-zero theorem and Rakhmonov's every-center narrow-rectangle theorem use

\[
\theta(\kappa,\lambda)=\frac{\kappa+\lambda}{2\kappa+2}.
\]

A fresh audit of the current Analytic Number Theory Exponent Database (ANTEDB) supplies a valid replacement strictly below the source-safe Karatsuba cutoff `27/82`. ANTEDB Theorem 5.22 records

\[
\left(\frac{89}{3478},\frac{15327}{17390}\right)
\]

as an exponent pair, and its standard van der Corput `B`-process gives the exponent pair

\[
\boxed{
(\kappa,\lambda)
=\left(\frac{3316}{8695},\frac{914}{1739}\right).
}
\]

For this pair,

\[
\boxed{
\theta_*
=\frac{\kappa+\lambda}{2\kappa+2}
=\frac{3943}{12011}
=0.3282824077928565\ldots
<\frac{27}{82}=0.3292682926829268\ldots .
}
\]

The exact gap is

\[
\frac{27}{82}-\frac{3943}{12011}
=\frac{971}{984902}>0.
\]

Consequently the WI-198/WI-201 packing argument now unconditionally excludes mirror-closed **count-saturating** fixed-power Maynard--Pratt bows for every fixed exponent

\[
\boxed{\vartheta>\frac{3943}{12011}}.
\]

The same fixed positive spacing-gap conclusion above the `4\pi` mirror-count threshold follows in that range. Using Rakhmonov's generic exponent-pair theorem, the count-saturation-free exclusion of the explicit fixed-physical-depth Maynard--Pratt plateau also extends to every fixed `\vartheta>3943/12011` for the depth range supplied by WI-200's generic algebra. The stronger normalized-depth screening tail of WI-199 is **not** extended: its current source-safe every-center input still starts at `27/82`.

No unconditional simple-critical-zero proportion changes here, and no conclusion about the existence of off-critical zeta zeros follows. The distinguished source-fixed covariance problem remains live for count-saturating fixed-power bows in the smaller range `0<\vartheta\le3943/12011`, with the endpoint unresolved by this packing argument.

## 1. Verified exponent-pair input

The current ANTEDB exponent-pair chapter, maintained by Terence Tao, Tim Trudgian, and Andrew Yang, states in Theorem 5.22 that

\[
(k_9,\ell_9)
=\left(\frac{89}{3478},\frac{15327}{17390}\right)
\tag{1}
\]

is an exponent pair. The same chapter states the standard `B`-process: if `(k,l)` is an exponent pair, then so is

\[
B(k,\ell)=\left(\ell-\frac12,k+\frac12\right).
\tag{2}
\]

Applying (2) to (1) gives, exactly,

\[
\ell_9-\frac12
=\frac{15327}{17390}-\frac12
=\frac{3316}{8695},
\]

and

\[
k_9+\frac12
=\frac{89}{3478}+\frac12
=\frac{914}{1739}.
\]

Thus

\[
(\kappa,\lambda)
=\left(\frac{3316}{8695},\frac{914}{1739}\right)
\tag{3}
\]

is an ordinary exponent pair with no appeal to the invalid Bourgain--Watt specialization corrected in WI-201.

Substitution in the Khayrulloev--Rakhmonov threshold gives

\[
\kappa+\lambda=\frac{7886}{8695},
\qquad
2\kappa+2=\frac{24022}{8695},
\]

hence

\[
\theta(\kappa,\lambda)
=\frac{7886}{24022}
=\boxed{\frac{3943}{12011}}.
\tag{4}
\]

The exact comparison with the last audited source-safe frontier is

\[
\frac{27}{82}-\frac{3943}{12011}
=\frac{971}{984902}>0.
\tag{5}
\]

The theorem containing the new exponent-pair work has also appeared in peer-reviewed form: Terence Tao, Tim Trudgian, and Andrew Yang, **New exponent pairs, zero density estimates, and zero additive energy estimates: A systematic approach**, *Mathematics of Computation* 95 (2026), 2941--2990, DOI `10.1090/mcom/4138`, published electronically 6 November 2025. The exact pair (1) and current convex-hull bookkeeping were checked against the authors' maintained ANTEDB blueprint rather than inferred from the paper's abstract.

## 2. This is the minimum theta on the current ANTEDB exponent-pair hull

ANTEDB currently states that the known exponent pairs form the convex hull of the vertices in its Table 5.2, including the `B`-reflections of the positive-index vertices and the Heath--Brown tail. The objective

\[
\theta(k,\ell)=\frac{k+\ell}{2k+2}
\tag{6}
\]

has affine half-space sublevel and superlevel sets because its denominator is positive throughout the exponent-pair triangle. Therefore its minimum over a convex hull occurs at a vertex; equivalently, if every vertex obeys `theta>=c`, every convex combination obeys the same linear inequality

\[
k+\ell\ge c(2k+2).
\]

Exact rational comparison of the finite vertices shows that the smallest value is attained at the `B`-reflection (3) of Table-5.2 vertex `n=9`. The nearest finite competitors are

\[
\theta(Bk_8)=\frac{630855}{1920826}=0.3284290195\ldots,
\qquad
\theta(Bk_7)=\frac{1533}{4658}=0.3291112065\ldots .
\]

For the infinite Heath--Brown tail

\[
p_m=\frac{2}{(m-1)^2(m+2)},
\qquad
q_m=1-\frac{3m-2}{m(m-1)(m+2)},
\qquad m\ge6,
\]

the potentially competitive reflected values are

\[
\theta(B(p_m,q_m))
=
\frac{m^4-6m^2+9m-2}
{(m-1)(3m^3+3m^2-12m+4)}.
\tag{7}
\]

Their forward difference equals

\[
\frac{2(m+1)(m^2-5m+2)(3m^2+3m-2)}
{m(m-1)(3m^3+3m^2-12m+4)(3m^3+12m^2+3m-2)},
\tag{8}
\]

which is positive for every `m>=6`. Hence that tail is minimized at `m=6`, where

\[
\theta(B(p_6,q_6))=\frac{283}{860}=0.3290697674\ldots>\frac{3943}{12011}.
\]

The unreflected Heath--Brown tail is much larger (its first value is `283/606`). Thus, as of the ANTEDB state audited on 8 September 2026, `3943/12011` is the smallest value of (6) on its recorded convex hull of known exponent pairs. This time-stamped database statement is not a claim that no future exponent pair can improve the threshold.

## 3. Bow consequence from Khayrulloev's generic theorem

WI-201 already primary-source-audited the part of Khayrulloev's 2024 theorem that survives the correction: for an arbitrary ordinary exponent pair `(kappa,lambda)`, fixed `epsilon>0`, and

\[
h=T^{\theta(\kappa,\lambda)+\epsilon},
\]

every sufficiently high interval of length `h` contains

\[
\gg_\epsilon h\log T
\]

odd-order critical-line zeros.

Let a source-compatible mirror-closed bow have

\[
m_T=T^{\vartheta+o(1)}
\]

selected right-half labels and bounded positive unfolded spacing `c_T`, so its vertical span is

\[
L_T=(c_T+o(1))\frac{m_T}{\log T}.
\tag{9}
\]

Fix `vartheta>3943/12011` and choose a fixed `epsilon>0` such that

\[
\frac{3943}{12011}+\epsilon<\vartheta.
\]

Then

\[
\frac{L_T}{T^{3943/12011+\epsilon}}
=T^{\vartheta-3943/12011-\epsilon+o(1)}\frac{c_T}{\log T}
\longrightarrow\infty.
\tag{10}
\]

Packing a `1-o(1)` fraction of the bow interval by disjoint Khayrulloev intervals and summing the every-interval lower bound gives

\[
N_{0,\mathrm{odd}}(I_{\rm bow})
\gg_{\vartheta} L_T\log T
\asymp c_Tm_T.
\tag{11}
\]

As in WI-198, all but `O(1)` selected Maynard--Pratt bow labels are off the line, and their functional-equation mirrors are off the line. Therefore (11) is a compulsory complementary critical-line population of order `m_T`. It contradicts the count-saturating condition `E_I=o(m_T)` and, retaining the factor `c_T`, reproduces WI-198's fixed positive spacing gap above `4\pi`.

Thus the source-safe count-saturation cutoff is now

\[
\boxed{\vartheta>3943/12011.}
\tag{12}
\]

The endpoint is not obtained: at `vartheta=3943/12011`, the bow length has the extra factor `1/log T` and is shorter than every fixed-`epsilon` theorem interval.

## 4. Fixed-depth consequence and the remaining screening distinction

WI-201 also preserved Rakhmonov's **generic** ordinary-exponent-pair theorem. Replacing only the invalid numerical input in WI-200 by (3), its exact downstream calculation applies unchanged. For any fixed

\[
\vartheta>\frac{3943}{12011},
\]

Rakhmonov's every-center narrow-rectangle estimate acts on the whole bow interval. In the first `a=12/5` branch, division by the natural bow population again gives decay for every fixed physical horizontal depth

\[
\delta=\beta-\frac12>\frac1{12}.
\]

Hence the explicit Maynard--Pratt plateau at `beta=3/4` cannot occupy a positive fraction of such a bow even without count saturation.

This does **not** transport WI-199's stronger statement at normalized depth

\[
A=(\beta-\tfrac12)\log T=O(1).
\]

Rakhmonov's near-line exponent leaves a positive power of the interval length after normalization, exactly as already calculated in WI-200. The current source-safe normalized-screening theorem therefore remains restricted to the `vartheta>27/82` range of the Karatsuba--Korolev input. The new cutoff removes count-saturating and fixed-physical-depth bow models in the narrow band

\[
\frac{3943}{12011}<\vartheta\le\frac{27}{82},
\]

but does not create a new source-fixed coercivity statement in the `O(1/log T)` screening layer.

## 5. Prior-art and evidence boundary

**Literature-backed inputs.** The exponent pair `(89/3478,15327/17390)`, the `B`-process, and the current convex-hull table are ANTEDB/Tao--Trudgian--Yang prior art. Khayrulloev's arbitrary-exponent-pair every-interval theorem and Rakhmonov's arbitrary-exponent-pair narrow-rectangle theorem are the generic primary theorem surfaces retained by WI-201. The Maynard--Pratt bow geometry is prior art.

**Exact repository deductions.** Equations (3)--(5), the minimization of `theta` over the current ANTEDB hull, and the transport through the already-audited bow packing are exact rational deductions. They repair WI-200 with an actually verified ordinary exponent pair rather than a numerically similar exponent from another problem.

A bounded novelty search for the exact cutoff `3943/12011` and for the transformed pair `(3316/8695,914/1739)` found no mathematical source applying them to the Khayrulloev/Rakhmonov short-interval zero theorems or to Maynard--Pratt bows. Absence of a search hit is not evidence of priority, and no priority claim is made.

The finding would fail if ANTEDB's Theorem 5.22 pair were not an ordinary exponent pair in the same standard sense used by Khayrulloev/Rakhmonov, if the `B`-process were inapplicable, or if WI-201's audit of the generic theorem surfaces were wrong. The first two points are stated directly in the maintained exponent-pair chapter; the third is unchanged from WI-201. No use is made of the withdrawn Bourgain--Watt `1515/4816` specialization.

## Primary sources and current theorem surfaces

- Terence Tao, Tim Trudgian, and Andrew Yang, **Analytic Number Theory Exponent Database**, exponent-pair chapter, Theorem 5.22, Proposition 5.9, and Table 5.2, https://teorth.github.io/expdb/blueprint/exponent-pairs-chapter.html (audited 8 Sep 2026).
- Terence Tao, Tim Trudgian, and Andrew Yang, **New exponent pairs, zero density estimates, and zero additive energy estimates: A systematic approach**, *Mathematics of Computation* 95 (2026), 2941--2990, DOI `10.1090/mcom/4138`; arXiv:2501.16779.
- Sh. A. Khayrulloev, **On the estimate of the number of odd-order zeros of the Riemann zeta function lying on the critical line**, *Izvestiya of the National Academy of Sciences of Tajikistan*, 2024, No. 4 (197), 51--64, https://journals.anrt.tj/files/News_m/news_m_2024_04.pdf.
- Z. Kh. Rakhmonov, **Density of zeros of the Riemann zeta function in narrow rectangles of the critical strip**, *Chebyshevskii Sbornik* 26:5 (2025), 158--183, DOI `10.22405/2226-8383-2025-26-5-158-183`, https://www.mathnet.ru/eng/cheb1627.
- James Maynard and Kyle Pratt, **Half-Isolated Zeros and Zero-Density Estimates**, *International Mathematics Research Notices* 2024:19 (2024), 12978--13014, DOI `10.1093/imrn/rnae191`, arXiv:2206.11729v2.

## Research consequence

WI-201 correctly killed the unsupported `1515/4816` shortcut, but it should not be read as returning the program permanently to `27/82`. A valid modern exponent pair already lowers the generic every-interval bow threshold to

\[
\boxed{3943/12011=0.3282824077928565\ldots .}
\]

The distinguished source-fixed covariance clue remains unresolved, but the fixed-power count-saturating regime on which it is needed is correspondingly narrower. Future exponent-pair updates can be tested mechanically against the same scalar objective `theta(k,l)`; values imported from zeta mean-square, circle/divisor, or other exponent problems remain inadmissible unless accompanied by an actual ordinary exponent pair.