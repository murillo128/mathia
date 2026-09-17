# WI-330 — a whole surviving bow occupies at most two Riemann--Siegel source cells

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY`.

WI-328 shows that neighboring ordinates inside a surviving Maynard--Pratt bow do not give independent twists on the endpoint cubic source block. WI-329 then shows that moving to the first longer source scale where the bow can genuinely dephase does not split the known almost-all exceptional set, because the matching nilsequence theorem is already uniform over the relevant polynomial phases. A remaining escape in the accepted clue is to hope that the many bow ordinates can be converted into many **distinct source starts** rather than merely many twists at one start.

The natural height-induced source recentering cannot do this. Let

\[
q(U):=\sqrt{\frac{U}{2\pi}},
\qquad
m_{\rm RS}(U):=\lfloor q(U)\rfloor,
\tag{1}
\]

so `m_RS(U)` is the classical Riemann--Siegel truncation index. For a surviving count-saturating fixed-power bow of vertical span

\[
H_{\rm bow}
=\frac{T^{\vartheta+o(1)}}{\log T},
\qquad
0<\vartheta\le
\vartheta_*:=\frac{3943}{12011},
\qquad
U\asymp T,
\tag{2}
\]

the image of the **entire bow** under `q` has diameter

\[
\boxed{
\operatorname{diam} q(\text{bow})
\ll T^{\vartheta-1/2+o(1)}
=o(1).
}
\tag{3}
\]

Equivalently, at the self-dual source scale `T\asymp X^2`,

\[
\boxed{
\operatorname{diam} q(\text{bow})
\ll X^{2\vartheta-1+o(1)}
\le X^{-4125/12011+o(1)}.
}
\tag{4}
\]

Hence, for all sufficiently large `T`, `m_RS(U)` takes **at most two adjacent integer values across the whole bow**. The two-value caveat is only the possibility that the tiny `q`-interval straddles one integer boundary; generically the whole bow lies in one cell.

For the exact endpoint-resonant family of WI-324--WI-325 the statement is stronger. If

\[
U_M=2\pi M\left(M+\frac12\right),
\tag{5}
\]

then

\[
q(U_M)=\sqrt{M\left(M+\frac12\right)}
=M+\frac14+O(M^{-1}),
\tag{6}
\]

so `m_RS(U_M)=M` exactly for every positive integer `M`. WI-325 snaps `U_M` to an actual zero ordinate `\gamma_M\in(U_M,U_M+2]`; this changes `q` by only `O(M^{-1})`. Therefore any surviving bow containing such a snapped ordinate satisfies, uniformly across that bow,

\[
\boxed{m_{\rm RS}(U)=M}
\tag{7}
\]

for all sufficiently large `M`. Thus the explicit resonant source start is not merely close to the natural Riemann--Siegel source cell: the whole admissible vertical bow remains in that same cell.

This closes the straightforward source-diversification route

\[
\text{many bow ordinates}
\;\Longrightarrow\;
\text{many natural Riemann--Siegel source starts}.
\]

Combining WI-328--WI-330, neither keeping the start fixed nor allowing it to follow the standard self-dual height coordinate produces a growing family of independent source samples. Any successful de-exceptionalization must obtain source-start diversity from an **independent arithmetic/source-position parameter**, not from ordinary height recentering.

## 1. Exact contraction of bow height in the Riemann--Siegel coordinate

For `U,V>0`, equation (1) gives the exact identity

\[
|q(U)-q(V)|
=
\frac{|U-V|}
{2\pi\bigl(q(U)+q(V)\bigr)}.
\tag{8}
\]

If `U,V` belong to one bow at height `T`, then `U,V\asymp T`, so

\[
q(U)+q(V)\asymp T^{1/2}.
\tag{9}
\]

Using the bow span (2),

\[
|q(U)-q(V)|
\ll
\frac{H_{\rm bow}}{T^{1/2}}
=
T^{\vartheta-1/2+o(1)}.
\tag{10}
\]

The maximal surviving exponent from WI-202 is strictly below `1/2`:

\[
\vartheta_* -\frac12
=
-\frac{4125}{24022}<0.
\tag{11}
\]

Therefore (10) tends to zero uniformly throughout the full surviving range. At `T\asymp X^2`, equation (10) becomes

\[
|q(U)-q(V)|
\ll
X^{2\vartheta-1+o(1)},
\tag{12}
\]

and at the endpoint

\[
2\vartheta_*-1
=
\frac{7886-12011}{12011}
=
-\frac{4125}{12011},
\tag{13}
\]

which proves (4).

Once the diameter in (3) is less than `1`, an interval of possible `q(U)` values can cross at most one integer boundary. Hence its floors form either one singleton or two adjacent integers. In particular, a bow containing `T^{\vartheta+o(1)}` selected zero labels does not thereby produce more than `O(1)` natural source cells.

This is stronger than a cardinality comparison with an exceptional set: the height-to-source map itself contracts the whole bow to sub-unit diameter before any arithmetic exceptional-set theorem is invoked.

## 2. The endpoint resonant family is frozen in one exact source cell

The carrier heights from WI-324--WI-325 satisfy (5). Their Riemann--Siegel coordinate obeys

\[
M^2
< M\left(M+\frac12\right)
<(M+1)^2,
\tag{14}
\]

so

\[
M<q(U_M)<M+1
\tag{15}
\]

and therefore

\[
m_{\rm RS}(U_M)=M.
\tag{16}
\]

More precisely, rationalizing the difference gives

\[
q(U_M)-M
=
\frac{M/2}{q(U_M)+M}
=\frac14+O(M^{-1}).
\tag{17}
\]

WI-325 chooses an actual nontrivial zero ordinate satisfying

\[
U_M<\gamma_M\le U_M+2.
\tag{18}
\]

By (8),

\[
q(\gamma_M)-q(U_M)
=O(M^{-1}),
\tag{19}
\]

hence

\[
q(\gamma_M)=M+\frac14+O(M^{-1}).
\tag{20}
\]

Now consider any surviving bow containing `\gamma_M`. Since `T\asymp U_M\asymp M^2`, its full vertical span satisfies

\[
H_{\rm bow}
=M^{2\vartheta+o(1)}
=o(M)
\qquad
(\vartheta\le\vartheta_*<1/2),
\tag{21}
\]

with the logarithmic factor absorbed into `M^{o(1)}`. Applying (8) again, every ordinate `U` in that bow satisfies

\[
q(U)-q(\gamma_M)=o(1).
\tag{22}
\]

Combining (20) and (22), uniformly on the bow,

\[
q(U)=M+\frac14+o(1).
\tag{23}
\]

Thus for all sufficiently large `M`, the entire bow lies strictly inside `(M,M+1)`, which proves (7). The conclusion is conditional only in the same sense as the bow program itself: WI-325 supplies the snapped zero ordinate but does not construct an off-critical Maynard--Pratt bow through it.

There is an equivalent exact carrier-spacing formulation. Adjacent resonant centers satisfy

\[
U_{M+1}-U_M
=4\pi M+3\pi
\asymp M.
\tag{24}
\]

The live bow span is `o(M)` by (21). Hence a whole surviving bow can intersect at most one fixed-width neighborhood of the resonant carrier family for sufficiently large `M`. The vertical multiplicity inside the bow cannot be reinterpreted as multiplicity of endpoint carrier centers either.

## 3. A general height-to-source contraction lemma

The preceding argument is not special to the exact square root. Let `s` be any `C^1` height-to-source coordinate on a neighborhood of a surviving bow at height `T` such that

\[
|s'(U)|\le C T^{-1/2}
\tag{25}
\]

throughout that neighborhood, with fixed `C`. Then the mean-value theorem gives

\[
\operatorname{diam}s(\text{bow})
\le
C H_{\rm bow}T^{-1/2}
=
T^{\vartheta-1/2+o(1)}
=o(1).
\tag{26}
\]

Therefore any integer source label obtained by flooring such a coordinate again takes at most two adjacent values. This covers the standard Riemann--Siegel coordinate and the continuous inverse of the exact WI-325 carrier family,

\[
r(U):=
\frac{-1+\sqrt{1+8U/\pi}}4,
\qquad
r(U_M)=M,
\tag{27}
\]

because

\[
r'(U)
=
\frac1{\pi\sqrt{1+8U/\pi}},
\qquad
r'(U_M)=\frac1{\pi(4M+1)}
\asymp M^{-1}.
\tag{28}
\]

Thus the obstruction is a scale fact: a live bow has vertical diameter `T^{\vartheta+o(1)}` with `\vartheta<1/2`, while every smooth self-dual source coordinate changes at speed `O(T^{-1/2})`. Their composition has vanishing diameter.

Equation (26) should not be generalized beyond its hypotheses. A deliberately amplified or arithmetically discontinuous map from heights to source positions need not have derivative `O(T^{-1/2})`; the result does not rule out source diversity supplied by an independent source parameter.

## 4. Relation to WI-328 and WI-329

WI-328 fixes a source start and proves that the whole surviving bow is twist-frozen on the `X^{1/3}` signed endpoint block. It leaves open the idea that the start itself might move with the height. The present result tests the canonical such motion and shows that the standard self-dual source coordinate moves by `o(1)`, not by a growing number of integers.

WI-329 moves to the longer interval `J\asymp X/H_{\rm bow}` where the phase genuinely dephases and proves that the strongest directly matching almost-all theorem still has one common exceptional set for all relevant phases. It therefore leaves open a different possibility: use the bow to force many genuinely distinct source starts and then pigeonhole against that exceptional set. Equations (3)--(7) show that **ordinary Riemann--Siegel recentering supplies only `O(1)` starts**, so it cannot implement that pigeonhole argument.

The combined barrier is now sharper:

\[
\boxed{
\begin{array}{c}
\text{fixed source start: bow phases are not independent at cubic scale (WI-328),}\\
\text{natural dephasing scale: the good/bad start set is already phase-uniform (WI-329),}\\
\text{natural moving source start: the whole bow occupies at most two source cells (WI-330).}
\end{array}
}
\tag{29}
\]

This does not solve the WI-195 variance gate. It rules out one concrete de-exceptionalization mechanism that the current clue still allowed.

## 5. Prior art, novelty audit, and evidence boundary

The Riemann--Siegel truncation in (1) is classical. NIST DLMF §25.10(ii), equation 25.10.3, records `m=floor(sqrt(t/(2*pi)))` in the Riemann--Siegel formula, citing Titchmarsh, *The Theory of the Riemann Zeta-Function*, §4.17. The bow geometry and its vertical spacing come from James Maynard and Kyle Pratt, *Half-Isolated Zeros and Zero-Density Estimates*, IMRN 2024:19 (2024), 12978--13014, DOI `10.1093/imrn/rnae191`; the exact surviving exponent and source-compatible normalization used here are the already-audited Mathia results WI-202 and WI-322.

The endpoint carrier family and its snap to actual zero ordinates are WI-324--WI-325. No statement from those findings is strengthened here beyond the explicit scale consequence (20)--(23).

A bounded prior-art audit of the Riemann--Siegel source and Maynard--Pratt bow literature did not locate a source using the bow span to derive the source-cell contraction (3)--(7). That absence is **not** a priority claim. The new line-local claim recorded here is the elementary exact deduction obtained by combining already attributed ingredients.

The strongest admissible conclusion is negative and specific. A successful continuation may still prove an every-start or distinguished-start cancellation theorem directly, derive an **independent** family of source positions from bow arithmetic or zero geometry, exploit a discontinuous/arithmetic source selector not governed by (25), or bypass start de-exceptionalization and attack the full WI-195 `L^2` variance object. What is closed is the cheaper route in which the many ordinates of one surviving bow are fed through the ordinary self-dual/Riemann--Siegel height coordinate and counted as many source starts.

## Research consequence

Do not use the cardinality of the bow as source-start multiplicity under natural height recentering. In the entire fixed-power range left by WI-202, the Riemann--Siegel coordinate of the full bow has vanishing diameter and supplies at most two adjacent starts; on the explicit WI-325 endpoint-resonant family it supplies exactly one. Any future exceptional-set argument must exhibit source-position diversity from a genuinely independent arithmetic mechanism, or else prove the required source-fixed/every-start estimate directly.
