# WI-197 — published Type-II module cannot reach the bow L2 scale even with maximal polynomial input

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`.

WI-195 identifies an exact positive Gallagher/Fejer representation of the count-saturating bow source square and shows that the published 2026 major-arc theorem of Matomaki--Radziwill--Shao--Tao--Teravainen (MRSTT) misses the required diagonal-scale `L^2` norm: its actual `Lambda-Lambda^sharp` output gives logarithmic saving from the linear short-interval scale, whereas the bow needs square-root-scale cancellation in quadratic mean. A natural response is to try to improve only the one-variable Dirichlet-polynomial input feeding the MRSTT Type-II argument—replacing the Vinogradov--Korobov logarithmic saving for `Lambda` by a hypothetical polynomial saving—while leaving the published Type-II transference machinery unchanged.

That route is impossible on the theorem surface already published. Even if one **grants** every pointwise Dirichlet-polynomial hypothesis in MRSTT Lemma 3.5 at the largest polynomial parameter `W` permitted by that lemma, its variance conclusion is still polynomially larger than the bow diagonal scale. The obstruction is therefore not only the present Vinogradov--Korobov input isolated in WI-195. The `W^{-3/10}` Type-II variance transfer together with the lemma's admissible `W` range is itself too weak.

For a bow short-interval length

\[
K=X^{\kappa+o(1)},
\qquad \kappa>\frac12
\]

(the hard count-saturating regime corresponding to the fixed Maynard--Pratt height exponent below one quarter), the bow gate requires

\[
\frac1X\int_X^{2X}|E_x(U;K)|^2\,dx=o(K\log X),
\]

while the smallest power-scale upper bound obtainable from the published Lemma 3.5 variance estimate is of shape

\[
K^2 X^{-\frac{3}{10000}(\kappa-1/3)+o(1)}.
\]

Its quotient by `K log X` still grows like

\[
X^{\kappa-\frac{3}{10000}(\kappa-1/3)+o(1)},
\]

whose exponent is positive for every `\kappa>1/3` and is at least about `0.49995` throughout the hard bow range `\kappa>1/2`. Thus strengthening only the pointwise prime-polynomial estimate and plugging it into the existing Type-II module cannot cross WI-195's norm gate.

This is a black-box barrier, not a lower bound for the true twisted-prime variance. A redesigned Type-II estimate, a coupled dispersion/large-value theorem, or another source identity can evade it. No unconditional simple-critical-zero proportion changes here, and no conclusion about the actual existence of bows or off-critical zeros follows.

## 1. The norm that the bow actually requires

Retain the exact source normalization of WI-195. On a central dyadic prime block `n\asymp X`, let

\[
E_x(U;K)
:=\sum_{x<n\le x+K}
(\Lambda(n)-\Lambda^\sharp(n))n^{iU},
\tag{1}
\]

suppressing only the harmless smooth `q_X(n)/\sqrt n` source weight while recording the scale. WI-195's multiplicative triangular identity shows that discarding the `Lambda-Lambda^sharp` part from the localized source square at the required scale needs, schematically,

\[
\boxed{
\frac1X\int_X^{2X}|E_x(U;K)|^2\,dx
=o(K\log X).
}
\tag{2}
\]

The factor `K log X` is the raw diagonal scale per unit `x`-measure: opening the square and retaining `m=n` gives `\asymp K log X` because `\sum_{x<n\le x+K}\Lambda(n)^2` has that order on average. The exact source square then restores the `H^2/X^2` normalization described in WI-195. Equation (2) is therefore not an arbitrary strengthening of an almost-all theorem; it is the norm required by the positive source identity.

For the count-saturating bow,

\[
X=T^{1/2+o(1)},
\qquad
H=T^\epsilon/\log T,
\qquad
K=\frac XH=X^{1-2\epsilon+o(1)}.
\tag{3}
\]

In the unresolved small-bow regime `0<\epsilon<1/4`, write

\[
K=X^{\kappa+o(1)},
\qquad
\kappa=1-2\epsilon>\frac12.
\tag{4}
\]

The argument below is actually stronger than needed: the incompatibility already holds for every fixed `\kappa>1/3`, i.e. throughout the interval-length range in which the relevant MRSTT Type-II part (iii) is available.

## 2. The published Type-II variance surface

The primary source is Kaisa Matomaki, Maksym Radziwill, Xuancheng Shao, Terence Tao and Joni Teravainen, **Higher uniformity of arithmetic functions in short intervals II. Almost all intervals**, *Inventiones Mathematicae* 244 (2026), 967--1091, arXiv:2411.05770v2. The source is already anchored in `research/weil_inertia/SOURCES.md`.

MRSTT Lemma 3.5 is the Type-II major-arc module used in the proof of its Theorem 3.1. In the notation of the paper, let `H_1` be the short-interval length and let `W` be the saving parameter. The lemma begins with the explicit restriction

\[
\boxed{1\le W\le X^{\eta/1000}}
\tag{5}
\]

where `\eta>0` is the small fixed margin parameter (called `\varepsilon` in the paper; a different letter is used here to avoid collision with the bow exponent). In part (iii), the interval-length condition is

\[
H_1\ge X^{1/3+\eta},
\tag{6}
\]

with the Type-II factor range `X^\eta\le M\le X^{1/2}`. The hypotheses ask for two pointwise Dirichlet-polynomial bounds of size at most `W^{-1/3}` on the relevant `t` range. Under those hypotheses the pointwise almost-all conclusion is `H_1/W^{1/10}`.

The load-bearing fact for the present audit is inside the proof of the same lemma. Before Chebyshev, MRSTT prove for parts (iii)--(iv) the variance estimate labelled equation (3.8):

\[
\boxed{
\frac1X\int_X^{2X}
\left|
\sum_{\substack{x<mn\le x+H_1\\m\sim M}}
a(m)b(n)
\right|^2dx
\ll
H_1^2\frac{\log^{O_C(1)}X}{W^{3/10}}.
}
\tag{7}
\]

This is exactly the quantitative transfer that ultimately turns pointwise control of the Dirichlet factors into short-interval Type-II control. The present finding grants the hypotheses feeding (7); it asks how strong (7) can possibly become **without changing Lemma 3.5 itself**.

For comparison, MRSTT Lemma 3.2 supplies for the actual von Mangoldt input only

\[
W_\Lambda=\log^A X,
\tag{8}
\]

through the Vinogradov--Korobov zero-free region, while its divisor-function input receives a polynomial `W_{d_k}=X^{c_k}`. WI-195 already explains why the actual logarithmic `Lambda` output is too weak. The point of the present test is to remove that weakness artificially and see whether the remaining Type-II module would then suffice.

## 3. Even the maximally granted `W` cannot reach diagonal scale

Set

\[
H_1=K=X^{\kappa+o(1)}.
\tag{9}
\]

Suppose, much more strongly than currently known for the relevant von Mangoldt factors, that every pointwise hypothesis in Lemma 3.5(iii) were available for whatever polynomial `W` is most favorable subject only to the lemma's own admissibility conditions. Equation (7) would then give at best

\[
\frac1X\int_X^{2X}|S_x|^2dx
\ll
K^2\frac{\log^{O(1)}X}{W^{3/10}},
\tag{10}
\]

for each Type-II piece `S_x`.

For an estimate of the form (10) to imply a diagonal-scale bound `o(K log X)`, its saving denominator would have to absorb one whole factor of `K`, up to logarithms:

\[
W^{3/10}
\gg K\log^{O(1)}X.
\tag{11}
\]

At power scale this requires

\[
\boxed{
W\ge X^{\frac{10}{3}\kappa-o(1)}
=K^{10/3-o(1)}.
}
\tag{12}
\]

But the interval condition (6) forces

\[
\eta\le \kappa-\frac13+o(1).
\tag{13}
\]

Combining (5) and (13), the largest denominator that the published lemma permits is therefore

\[
W^{3/10}
\le
X^{\frac{3\eta}{10000}}
\le
X^{\frac{3}{10000}(\kappa-1/3)+o(1)}.
\tag{14}
\]

Consequently the **smallest upper-bound scale supplied by (10)**, after dividing by the target `K log X`, is still

\[
X^{\kappa-\frac{3}{10000}(\kappa-1/3)+o(1)}.
\tag{15}
\]

The exponent is

\[
\kappa-\frac{3}{10000}\left(\kappa-\frac13\right)
=
\frac{9997}{10000}\kappa+\frac1{10000}
>0
\tag{16}
\]

for every positive `\kappa`; in particular, at the edge `\kappa=1/2` it equals

\[
\frac{9997}{20000}+\frac1{10000}
=0.49995.
\tag{17}
\]

Thus throughout the actual hard-bow range `\kappa>1/2`, the best bound obtainable from the existing module—even after granting maximal polynomial pointwise input—still misses the diagonal variance target by approximately a square-root power of `X`.

It is important to interpret (15) correctly. It is **not** a lower bound for the true variance. It says that the upper bound certified by this black-box lemma cannot be pushed down to the required scale by tuning or improving only the pointwise `W^{-1/3}` hypotheses. The true Type-II sum could of course be much smaller for arithmetic reasons that (7) does not retain.

There is an even cruder way to see the scale mismatch. If one unrealistically relaxed the published cap (5) all the way to `W\le X` while retaining the same `W^{-3/10}` transfer law, (10) would save at most `X^{3/10}`. But the hard bow needs one factor `K=X^{\kappa+o(1)}` with `\kappa>1/2`. So in that regime the `3/10` transfer exponent itself already shows that merely enlarging the admissible pointwise-saving parameter to an ordinary `X`-scale parameter would not be enough. This last observation is only a diagnostic of the exponent; the rigorous route barrier uses the much stricter actual cap (5).

## 4. The alternative Type-II range does not rescue the route

MRSTT Lemma 3.5(iv) removes the `H_1\ge X^{1/3+\eta}` threshold but assumes

\[
H_1\ge X^{2\eta},
\qquad
X^\eta\le M\le H_1X^{-\eta},
\tag{18}
\]

and uses only the first pointwise Dirichlet-polynomial hypothesis. Its proof is still covered by the same variance equation (7), and the same global parameter restriction `W\le X^{\eta/1000}` remains in force.

With `H_1=K=X^{\kappa+o(1)}`, condition (18) allows at most

\[
\eta\le\frac\kappa2+o(1),
\tag{19}
\]

so

\[
W^{3/10}
\le X^{3\kappa/20000+o(1)}.
\tag{20}
\]

This is again negligible compared with the required `K=X^{\kappa+o(1)}` saving. Part (iv) therefore cannot be used as a hidden short-interval escape from the mismatch.

The conclusion does not require every combinatorial piece of `Lambda-Lambda^sharp` to lie in exactly one of parts (iii) or (iv), nor does it claim that equation (7) is a direct theorem for the undecomposed sum (1). It tests the specific proposed architecture: **improve only the pointwise Dirichlet-polynomial input, then reuse the published Type-II transfer on the Type-II pieces generated by the same decomposition.** Any successful argument that changes the decomposition, couples pieces before Cauchy/Chebyshev, or proves a different second-moment theorem has left the route being closed here.

## 5. Relation to WI-195 and prior art

This result is not a restatement of WI-195. WI-195 compares the bow target with the **actual theorem output** `K log^{-A}X` and notes that squaring even a hypothetical all-interval version gives `XK^2 log^{-2A}X`, polynomially above the desired `XK log X`. It also observes from the source proof that the Type-II machinery produces `K^2`-scale variance with logarithmic saving for the von Mangoldt application.

The present finding asks the next adversarial question: perhaps the only reason for that logarithmic saving is MRSTT Lemma 3.2's Vinogradov--Korobov input for `Lambda`, so could a future polynomial pointwise bound be inserted without otherwise changing the proof? Equations (12)--(17) answer **no**. The admissible `W` range and the `W^{-3/10}` variance transfer in Lemma 3.5 remain polynomially too weak even after the pointwise hypotheses are granted at their maximal legal strength.

The nearby modern prior art includes Larry Guth and James Maynard, **New large value estimates for Dirichlet polynomials**, *Annals of Mathematics* 203 (2026), 623--675, DOI `10.4007/annals.2026.203.2.6`. That work substantially strengthens large-value estimates and, among other applications, improves prime short-interval results. MRSTT itself cites Guth--Maynard for the improved untwisted almost-all prime interval exponent. A bounded audit did not locate in that theorem surface a fixed distinguished high Archimedean twist `U\asymp X^2` estimate giving the diagonal-scale variance (2) for `Lambda-Lambda^sharp`. This absence is **not** evidence of priority and does not say Guth--Maynard techniques cannot be adapted. It says only that citing a stronger large-value theorem as a replacement for Lemma 3.2 is insufficient unless one also proves that the resulting Type-II variance transfer has changed at the norm level quantified above.

The exact published constants used here are source facts, not Mathia claims: MRSTT Lemma 3.5 states `W\le X^{\eta/1000}`, requires pointwise factor bounds `W^{-1/3}`, and its proof establishes the `W^{-3/10}` variance in equation (3.8). The exponent comparison (11)--(17), its specialization to the bow, and the resulting route closure are derived here.

## 6. Research consequence

The accepted bow clue after WI-196 asks for source-specific signed cancellation at the distinguished height, with the structured `Lambda^sharp` component kept in the same norm, or for another source-fixed observable that excludes the common near-null geometry. WI-197 sharpens the first half of that target: **a better one-variable pointwise prime-polynomial estimate is not by itself the missing theorem if the plan is to feed it through the existing MRSTT Type-II module.**

A viable continuation must change at least one load-bearing norm interface. Examples include a Type-II theorem whose quadratic mean is already `O(K log^{O(1)}X)` or better rather than `K^2` times a modest saving; a dispersion or large-sieve argument that preserves cancellation across the factors and/or the physical shift family before absolute-value losses; a source decomposition adapted to the distinguished twist rather than to almost-all major-arc discorrelation; or an exact evaluation/cancellation mechanism for the `Lambda^sharp` structured term that couples to the raw `Lambda` square before the error is separated.

This is a deliberately negative result, but it saves a substantial weak route. The next source-level attempt should be judged first by the **variance exponent it transfers**, not by how strong a pointwise Dirichlet-polynomial saving it advertises. If its final Type-II second moment still has the form `K^2` times a saving smaller than a full factor of `K`, it has not crossed the bow gate identified by WI-195.

No theorem about the actual size of (1), no new simple-zero percentage, and no RH consequence are asserted.