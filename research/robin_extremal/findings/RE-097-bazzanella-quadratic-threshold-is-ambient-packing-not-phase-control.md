# RE-097 — Bazzanella's quadratic `13/32` threshold is ambient packing, not phase control

**Status:** `EXACT-DERIVED + NEGATIVE/PRIOR-ART-REDIRECT + MIXED-FIRST/SECOND-LAYER-CHAMBERS + DEFORMED-QUADRATIC-SAMPLE + AMBIENT-EXCEPTIONAL-PACKING + BAZZANELLA-METHOD-AUDIT + SOURCE-CONDITIONED-TARGET-SHARPENING + PRIOR-ART-AUDITED`.

`RE-096` reduces the residual mixed first/depth-two problem to the deterministic integer sample

\[
x(n)=\eta_1^{-1}(\eta_2(n)),
\qquad n\asymp X^{1/2},
\]

and shows a useful dichotomy: physically, `x(n)` is displaced from `n^2/2` by `asymp X/log X`, far larger than the target interval length, while the derivatives of `log x(n)` remain quadratically stable. The nearest published sparse-power comparison was Bazzanella's theorem for intervals starting at `n^alpha`, whose displayed quadratic exponent is

\[
c(2)=\frac{13}{32}.
\]

A direct audit of Bazzanella's proof changes the interpretation of that comparison. The published `alpha=2` value `13/32` does **not** come from exploiting the oscillatory phase of the quadratic sample. In the relevant small-`H` regime it comes from packing sparse sample exceptions into the ordinary ambient PNT exceptional set. That mechanism transfers to the CA-deformed sequence using only its square-root spacing, so the large physical drift identified in `RE-096` is not an obstruction to this proof branch. But precisely because the mechanism factors only through ambient exceptional-set measure, it cannot lower the Robin frontier beyond the combination already available from `RE-094` and the `173/200` second-moment bound.

Thus the phase stability in `RE-096` remains potentially useful, but only for a **genuinely direct sparse-sequence argument**—for example an adaptation of the fourth-moment/zero-additive-energy architecture that Bazzanella uses for sufficiently large `alpha`, not a repackaging of the small-`H` quadratic branch that yields `13/32`.

## 1. Ambient exceptional mass controls the deformed sample by spacing alone

Fix

\[
H=X^\vartheta,
\qquad 0<\vartheta<\frac12,
\]

and use the two-sided bad integer-host set `\mathcal Z_\vartheta(X)` from `RE-096`: an integer `n asymp X^(1/2)` is bad if one of the intervals of length `2H` immediately adjacent to `x(n)` is prime-free.

Suppose that, on a harmless bounded-ratio enlargement of the physical shell, the fixed-`delta` PNT exceptional set for intervals of length `H` has measure

\[
|E_\delta(X,H)|
\ll X^{m(\vartheta)+o(1)}.
\tag{1}
\]

Then

\[
\boxed{
\#\mathcal Z_\vartheta(X)
\ll
\min\!\left(
X^{1/2+o(1)},
X^{m(\vartheta)-\vartheta+o(1)}
\right).
}
\tag{2}
\]

The proof uses no special formula for `x(n)` beyond monotonicity, square-root spacing, and its location at physical scale `X`. If the right-hand `2H` interval adjacent to `x(n)` is prime-free, then an `H`-long packet of nearby starts has its complete `H`-interval inside that prime-free region; the left-hand case is identical. Since `vartheta<1/2`, prime powers contribute only `O((log X)^2)=o(H)` to `psi` on any such `H`-interval, so every start in that packet lies in a fixed-`delta` PNT exceptional set for sufficiently large `X`.

On the other hand `RE-096` gives

\[
\frac{d}{dt}\log x(t)=\frac2t+O\!\left(\frac1{t(\log t)^2}\right),
\qquad x(t)\asymp t^2,
\]

hence

\[
x(n+1)-x(n)\asymp X^{1/2}
\tag{3}
\]

uniformly in the shell. Because `H=o(X^(1/2))`, the exceptional-start packets attached to distinct bad integers are disjoint. Their total measure is therefore `gg H #\mathcal Z_\vartheta(X)`, which together with (1) proves the second term of (2); the first is the trivial number of integer hosts.

Equation (2) is the all-integer analogue of the ambient-to-host conversion already isolated for prime hosts in `RE-095`. The mechanism is classical exceptional-set packing; no novelty is claimed for that conversion itself.

## 2. This information class cannot improve the existing Robin envelope

Write

\[
A(\vartheta):=\frac12+\vartheta,
\qquad
F_0:=\frac{173}{200}.
\]

`RE-094` turns the ambient exponent `m(vartheta)` directly into the mixed-cell frontier

\[
F_{\rm amb}(\vartheta)
=
\max\!\left(A(\vartheta),m(\vartheta)\right),
\tag{4}
\]

while `RE-091`--`RE-093` already supply the independent baseline `F_0`. Thus before using the sparse hosts one already has

\[
F_{\rm old}(\vartheta)
=
\min\!\left(F_0,F_{\rm amb}(\vartheta)\right).
\tag{5}
\]

If (2) is inserted into the sampled-host plus Stadlmann splice of `RE-095`, its only possible host exponent is the ambient packing exponent

\[
\kappa_{\rm pack}(\vartheta)
=
\min\!\left(\frac12,\max(0,m(\vartheta)-\vartheta)\right),
\tag{6}
\]

with the convention that `m(vartheta)<vartheta` actually forces eventual emptiness at the power scale and is stronger than `kappa=0`. The resulting sufficient frontier is

\[
F_{\rm pack}(\vartheta)
=
\max\!\left(
A(\vartheta),
\frac{123}{200}+\frac{\kappa_{\rm pack}(\vartheta)}2
\right).
\tag{7}
\]

The comparison with the already available envelope is exact and elementary:

\[
\boxed{
F_{\rm pack}(\vartheta)
\ge
F_{\rm old}(\vartheta).
}
\tag{8}
\]

Indeed, if `m(vartheta)>=A(vartheta)`, then `m(vartheta)-vartheta>=1/2`, so `kappa_pack=1/2` and the second term in (7) is exactly `F_0`; hence `F_pack>=min(F_0,m)=F_old`. If instead `m(vartheta)<A(vartheta)`, then the direct ambient frontier (4) already equals `A(vartheta)`, while (7) is at least that same value. There is no third case.

Therefore an estimate for the deformed sample that is proved **only** by assigning each bad sample an `H`-sized packet inside an ambient exceptional set can never create a new Robin frontier. It may rederive either the ambient `RE-094` gain or the existing `173/200` baseline, but not improve their minimum. To beat `173/200` through `RE-095`, the bad-host saving must contain source information not already encoded by one-variable exceptional-set measure.

## 3. Bazzanella's published `alpha=2` branch is exactly this packing mechanism

Danilo Bazzanella, *Prime Numbers in Intervals Starting at a Fixed Power of the Integers*, Journal of the Australian Mathematical Society **87** (2009), 83--99, DOI `10.1017/S1446788709000020`, studies exceptions among intervals starting at `n^alpha`. The proof contains two materially different regimes.

For `alpha>6/5`, the direct explicit-formula/Kusmin--Landau part of Lemma 5 reaches the sparse sequence only in the range

\[
H(N)
\gg_\alpha
N^{1-1/\alpha}f(N)(\log N)^2,
\tag{9}
\]

with `f(N)->infinity` arbitrarily slowly. At `alpha=2`, (9) is a square-root-scale condition,

\[
H(N)\gg N^{1/2}f(N)(\log N)^2,
\tag{10}
\]

far outside the Robin target `vartheta<73/200<1/2`.

For smaller `H`, Lemma 5(ii) switches mechanisms. It places each sparse exception inside an ordinary ambient exceptional interval and obtains, up to the displayed harmless slowly varying/logarithmic factor,

\[
|A_\delta(N,H,\alpha)|
\ll
\frac{|E_{\delta/2}(N,H)|}{H(N)}
N^{o(1)}
+o(N^{1/\alpha}).
\tag{11}
\]

The paper's later note derives the intermediate-`alpha` values of `c(alpha)` by first estimating the ambient quantity `|E_delta(N,H)|` from zero-density bounds and then explicitly invoking Lemma 5. In the range containing `alpha=2`, it records

\[
c(\alpha)=\frac58-\frac7{16\alpha},
\]

and hence

\[
\boxed{c(2)=\frac{13}{32}=0.40625.}
\tag{12}
\]

So the published quadratic value in (12) belongs to the same information class as (2). The physical identity `x(n)=n^2/2+asymp(X/log X)` prevents a theorem *stated only at exact squares* from transferring by interval inclusion, as `RE-096` correctly notes. But it does **not** prevent the small-`H` proof mechanism from transferring: that branch only needs ambient exceptional-set packets and sufficient spacing of the sample points, both of which the deformed CA sequence has. The real defect for the Robin application is numerical and informational:

\[
\frac{13}{32}-\frac{73}{200}
=
\frac{33}{800}>0,
\tag{13}
\]

and, more fundamentally, any improvement obtained solely by replacing the old ambient exceptional exponent inside the same packing architecture is already covered by (8).

This classification is also consistent with the modern exceptional-set framework of Ayla Gafni and Terence Tao, *On the number of exceptional intervals to the prime number theorem in short intervals*, Essential Number Theory **5** (2026), 221--241, DOI `10.2140/ent.2026.5.221`, arXiv:2505.24017. Their equation (1.6) gives the standard exponent loss `mu(vartheta)-vartheta` when large prime gaps are counted by assigning each gap an `H`-sized packet of ambient exceptional starts. That is the same packing currency appearing in (2), not a source-conditioned phase estimate.

## 4. What remains genuinely open

The prior-art audit therefore narrows, rather than kills, the `RE-096` direction. Bazzanella's paper also contains a genuinely direct sparse-sequence argument for sufficiently large `alpha`: a fourth-moment expansion, zero additive-energy input, and exponent-pair bounds for oscillatory sums over `n^{alpha rho}`. That is the part of the architecture for which the phase derivatives in `RE-096` are relevant. The published proof only converts this branch into its general unconditional `c(alpha)` formula in the large-`alpha` regime (in particular `alpha>=4` in the displayed argument), so it does not already settle the quadratic or CA-deformed target.

The live analytic requirement is therefore sharper than "adapt Bazzanella to `x(n)`". One must prove a **direct below-spacing sparse-sample estimate** for

\[
\Phi_\gamma(n)=\gamma\log x(n)
\]

at some `vartheta<73/200`, with a polynomial saving in the number of bad indices, and the proof must use more than ambient exceptional-set measure. A viable route could adapt a fourth/higher moment or another sparse-sequence phase argument to the slowly deformed quadratic phase; an ambient zero-density theorem followed by packet counting is already noncoercive by (8).

No published theorem located in the targeted audit gives that direct estimate for `x(n)` or for a smooth logarithmic deformation of the quadratic sequence in the required exponent range. This is a prior-art boundary, not a priority claim. The durable correction to the research frontier is that **the `X/log X` physical drift is irrelevant to Bazzanella's small-`H` packing branch, while the phase stability is irrelevant to that same branch; phase stability matters only if one develops a different, genuinely sparse-sequence estimate.**