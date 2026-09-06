# MC-101 — Mesoscopic Hamming bias has an exact degree-two power profile

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `BOUNDARY/CONDITIONAL-GAIN`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Let the source-forced Hamming deformation from `MC-092`--`MC-100` be

\[
\mathcal Q_N(t)
=\sum_{m,n\le N}
\mu(m)^2\mu(n)^2(-t)^{d_\triangle(m,n)}
 z\!\left(\frac{N^2}{mn}\right)
=\sum_{k=0}^{D_N}(-t)^k C_{k,N},
\qquad 0\le t\le1.
\tag{1}
\]

The recent radial analysis isolates three source-level facts:

\[
C_{0,N}=O(N),
\qquad
C_{1,N}=O(N\log\log N),
\qquad
C_{2,N}\sim c_2\frac{N^2}{(\log N)^2},
\tag{2}
\]

where

\[
c_2
=\frac{15}{\pi^2}\left(\gamma+\gamma_1-\frac12\right)>0,
\tag{3}
\]

and `MC-100` gives the direct pair-level bound

\[
\left|
\sum_{k\ge3}(-t)^kC_{k,N}
\right|
\le \frac12N^2t^3
\qquad(0\le t\le1).
\tag{4}
\]

These ingredients determine the whole deformation on a broad shrinking neighborhood of the unbiased endpoint. Let `t_N` be any positive sequence such that

\[
\boxed{
 t_N(\log N)^2\longrightarrow0,
\qquad
\frac{Nt_N^2}{(\log N)^2}\longrightarrow\infty.
}
\tag{5}
\]

Equivalently, this includes every scale strictly inside the mesoscopic window

\[
\frac{\log N}{\sqrt N}\ll t_N\ll\frac1{(\log N)^2},
\tag{6}
\]

with the two inequalities understood with divergent margins. Then

\[
\boxed{
\mathcal Q_N(t_N)
\sim
c_2\frac{N^2t_N^2}{(\log N)^2}.
}
\tag{7}
\]

More strongly, the same asymptotic gives the maximum amplitude on the entire shrinking interval:

\[
\boxed{
\sup_{0\le t\le t_N}|\mathcal Q_N(t)|
\sim
c_2\frac{N^2t_N^2}{(\log N)^2}.
}
\tag{8}
\]

In particular, for every fixed

\[
0<\alpha<\frac12,
\tag{9}
\]

taking `t_N=N^{-\alpha}` yields

\[
\boxed{
\mathcal Q_N(N^{-\alpha})
\sim
c_2\frac{N^{2-2\alpha}}{(\log N)^2},
}
\tag{10}
\]

and

\[
\boxed{
\sup_{0\le t\le N^{-\alpha}}|\mathcal Q_N(t)|
\sim
c_2\frac{N^{2-2\alpha}}{(\log N)^2}.
}
\tag{11}
\]

Thus the near-zero Hamming deformation has an exact deterministic **power profile** throughout this mesoscopic regime. Shrinking the prime-sign bias to `N^{-alpha}` does not produce mysterious regularization: it suppresses the source to the degree-two scale `N^{2-2alpha}` and no further, up to the displayed logarithmic factor.

This closes a substantial part of the moving/shrinking-interval escape left open by `MC-100`. The critical source power `N^{1+o(1)}` would require `alpha>=1/2` in `(10)`. Exactly at that threshold, however, the degree-two contribution is at most `N/(log N)^2`, while the diagonal shell is known only at the `O(N)` scale, so the degree-two-dominance argument ceases to determine the source. The half exponent is therefore an exact **regime boundary for this low-bias mechanism**, not an improved Mertens estimate.

No RH input, zero-free-region estimate, or bound for the hard endpoint `mathcal Q_N(1)` is used in `(7)`--`(11)`.

## 1. The degree-two shell dominates under the mesoscopic hypotheses

Split `(1)` exactly as

\[
\mathcal Q_N(t)
=C_{0,N}-tC_{1,N}+t^2C_{2,N}+\mathcal R_{\ge3,N}(t),
\tag{12}
\]

where

\[
\mathcal R_{\ge3,N}(t)
:=\sum_{k\ge3}(-t)^kC_{k,N}.
\]

At `t=t_N`, use the natural degree-two scale

\[
S_N:=\frac{N^2t_N^2}{(\log N)^2}.
\tag{13}
\]

The second condition in `(5)` is precisely

\[
\frac{N}{S_N}
=\frac{(\log N)^2}{Nt_N^2}
\longrightarrow0,
\tag{14}
\]

so the diagonal shell is negligible:

\[
C_{0,N}=o(S_N).
\tag{15}
\]

For degree one, `(2)` gives

\[
\frac{t_N|C_{1,N}|}{S_N}
\ll
\frac{(\log N)^2\log\log N}{Nt_N}.
\tag{16}
\]

The second condition in `(5)` says

\[
\frac{\sqrt N\,t_N}{\log N}\longrightarrow\infty.
\tag{17}
\]

Consequently

\[
Nt_N
\gg \sqrt N\log N
\]

with a divergent factor, and the right side of `(16)` tends to zero. Hence

\[
t_NC_{1,N}=o(S_N).
\tag{18}
\]

Finally, the source-level cubic estimate `(4)` yields

\[
\frac{|\mathcal R_{\ge3,N}(t_N)|}{S_N}
\le
\frac12t_N(\log N)^2
\longrightarrow0
\tag{19}
\]

by the first condition in `(5)`.

The positive degree-two asymptotic in `(2)` is

\[
t_N^2C_{2,N}
=(c_2+o(1))S_N.
\tag{20}
\]

Substituting `(15)`, `(18)`, `(19)`, and `(20)` into `(12)` proves `(7)`.

The proof is entirely source-local. In particular, unlike `MC-098` and `MC-099`, it does not use the unconditional smallness of the Möbius endpoint to force cancellation elsewhere along the deformation.

## 2. The whole shrinking interval has the same leading amplitude

The endpoint lower bound `(7)` immediately gives

\[
\sup_{0\le t\le t_N}|\mathcal Q_N(t)|
\ge
(c_2+o(1))S_N.
\tag{21}
\]

For the reverse estimate, let `0<=t<=t_N`. From `(12)`, `(2)`, and `(4)`,

\[
|\mathcal Q_N(t)|
\le
O(N)
+O(Nt_N\log\log N)
+(c_2+o(1))\frac{N^2t_N^2}{(\log N)^2}
+\frac12N^2t_N^3.
\tag{22}
\]

The first, second, and fourth terms are `o(S_N)` by exactly `(14)`, `(16)`--`(18)`, and `(19)`. Therefore uniformly for every `t` in the shrinking interval,

\[
|\mathcal Q_N(t)|
\le(c_2+o(1))S_N.
\tag{23}
\]

Combining `(21)` and `(23)` proves `(8)`.

This uniform asymptotic is stronger than the isolated spike in `MC-100`. It says that, throughout the admitted mesoscopic window, the largest amplitude on `[0,t_N]` is asymptotically determined by the complete degree-two shell. No unspecified higher-degree radial cancellation can lower that maximum, because the original pair sum suppresses every degree at least three by one extra factor of `t_N`.

## 3. Fixed power biases expose the half-exponent boundary

Take

\[
t_N=N^{-\alpha}
\]

with fixed `0<alpha<1/2`. Then

\[
t_N(\log N)^2=N^{-\alpha}(\log N)^2\to0,
\]

while

\[
\frac{Nt_N^2}{(\log N)^2}
=
\frac{N^{1-2\alpha}}{(\log N)^2}
\to\infty.
\]

Thus `(5)` holds and `(10)`--`(11)` follow directly from `(7)`--`(8)`.

The power bookkeeping is revealing. At bias `N^{-alpha}`, the degree-two source has exponent

\[
2-2\alpha.
\tag{24}
\]

As `alpha` increases from zero toward one half, this exponent decreases continuously from `2` toward `1`. But the theorem stops exactly before reaching the critical source exponent `1`, because the condition that the degree-two shell dominate the diagonal is

\[
N^{2-2\alpha}(\log N)^{-2}\gg N,
\]

which requires `alpha<1/2` with a power margin.

At `alpha=1/2`, the known sizes are only

\[
t^2C_{2,N}\asymp\frac{N}{(\log N)^2},
\qquad
C_{0,N}=O(N),
\tag{25}
\]

so the diagonal may dominate. For `alpha>1/2`, the degree-two term is strictly below the available diagonal scale. Nothing here determines whether additional cancellation inside `C_{0,N}` makes a smaller-bias regime useful; that is a genuinely different question.

Accordingly, the theorem does **not** prove that square-root bias is impossible or that every shrinking-bias deformation is useless. It identifies the precise point at which the currently forced degree-two obstruction loses control.

## 4. What this changes about the shrinking-geometry escape

`MC-093` proves that any strict power bound on a fixed positive-length bias interval transfers to the hard endpoint with only subpolynomial extrapolation loss. `MC-100` then proves that every such fixed interval already contains almost-square amplitude, while explicitly leaving `N`-dependent shrinking intervals outside its conclusion.

Equations `(7)`--`(11)` now calibrate a broad family of those shrinking intervals. For every fixed `alpha<1/2`, the interval `[0,N^{-alpha}]` is indeed easier than a fixed interval at the level of powers, but its gain is completely accounted for by the elementary Hamming damping of the degree-two shell. In particular, one cannot obtain an additional hidden power saving on that entire interval without contradicting the exact source asymptotic `(11)`.

This separates **regularization** from **reconstruction** more cleanly. The source can be regularized to power `N^{2-2alpha}` merely by moving toward `t=0`; that is real but unsurprising information. To use the regularized regime for the Möbius endpoint, a future argument still needs an `N`-dependent recurrence, interpolation, derivative identity, or other signed coupling whose reconstruction cost is strictly smaller than the power `2alpha` gained by shrinking the bias.

The fixed-gap Chebyshev estimate of `MC-093` does not supply such a statement, because the controlled interval itself now degenerates with `N`. Any moving-geometry proposal must therefore keep its stability or condition number explicit and compare that cost directly against the exact gain in `(24)`.

## 5. Prior art and novelty boundary

The arithmetic source is classical Huxley--Watt structure (`MC-S24`). The product-fiber/Hamming reduction is already canonical in `MC-092`, the positive degree-two asymptotic is `MC-097`, and the pair-level cubic tail estimate is proved in `MC-100`. The present result is the exact asymptotic consequence obtained by putting those source terms on a moving bias scale.

Biased random multiplicative functions are established prior art. Marco Aymone and Vladas Sidoravicius, *Partial sums of biased random multiplicative functions*, Journal of Number Theory 172 (2017), 343--382, DOI `10.1016/j.jnt.2016.08.020`, study square-free-supported multiplicative functions built from independent biased prime signs and relate their partial sums to Möbius/RH-scale cancellation. Their setting confirms that varying prime-sign bias is not a new general framework. It does not, in the targeted audit performed for this line, supply the deterministic Huxley--Watt bilinear asymptotic `(7)`--`(11)`.

Likewise, Hamming/noise operators and low-degree damping on product spaces are classical harmonic-analysis mechanisms. A targeted literature search around Möbius/Huxley--Watt sums, biased prime-sign multiplicative functions, Hamming/noise deformations, and shrinking bias did not identify a standard theorem matching the exact source profile above. Search absence is not evidence of novelty, and **no novelty claim is made**.

The durable contribution is narrower: for this already-defined source deformation, the mesoscopic moving-bias regime is no longer an unspecified escape. Its amplitude is forced asymptotically by the degree-two arithmetic shell.

## 6. Boundaries and falsification tests

- The hypotheses `(5)` are sufficient for degree-two dominance, not claimed optimal. In particular, this finding does not classify the transition window where `t_N` is comparable to `log N/sqrt N` or smaller.
- The result depends on the exact source decomposition `(12)`, the positive `C_{2,N}` asymptotic, and the direct cubic pair-level tail bound. Altering the sawtooth kernel, truncating the product fibers, changing the prime-sign coupling, or reweighting radial degrees requires a new audit.
- Equation `(8)` concerns the interval anchored at `t=0`. It does not classify a shrinking interval centered at a moving interior point, nor a sparse moving sample family.
- The theorem does not estimate `mathcal Q_N(1)`, `M(N)`, or `M(N^2)`. It uses no endpoint smallness and therefore supplies no new zero-free region or RH consequence.
- The exact power gain from shrinking bias is not automatically useful. A reconstruction theorem whose norm/condition number costs `N^{2alpha+o(1)}` or more is exponent-neutral.
- Random-multiplicative behavior is not transferred to Möbius. The proof is deterministic and uses the random-bias literature only as a prior-art boundary for the surrounding language.
- A genuine escape remains possible at or below the square-root-bias transition, through a moving interval not anchored at zero, or through a signed recurrence coupling large values across scales. Such a route must be checked against the source terms rather than inferred from the present asymptotic.

## Consequence for the research line

The Hamming branch now has a quantitative two-regime frontier. Fixed positive-length intervals are forced to almost-square amplitude by `MC-100`; shrinking intervals anchored at zero with bias `N^{-alpha}`, `0<alpha<1/2`, have the exact smaller power `N^{2-2alpha}` by `(10)`--`(11)`. The apparent regularization is therefore completely measured before the half exponent.

Any surviving deformation strategy must now do one of three genuinely additional things: enter the transition at or below square-root bias where degree two no longer controls the source, prove a reconstruction/recurrence whose cost is strictly below the known bias gain, or exploit signed relations among deformation values rather than their individual smallness. Merely choosing an `N`-dependent small bias no longer constitutes an unexplained route around the radial-shell obstruction.