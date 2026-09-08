# WI-204 — Karatsuba's almost-all exception budget can absorb an entire count-saturating bow

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`.

WI-198 deliberately used an **every-interval** critical-line-zero theorem to prune long count-saturating Maynard--Pratt bows, because an almost-all theorem need not control a source-selected bow location. There is a natural attempted repair of that objection: a bow has positive vertical length, so perhaps a single count-saturating bow forces not one exceptional starting height but an entire interval of exceptional starts, large enough to contradict Karatsuba's quantitative almost-all theorem.

The exact bookkeeping below shows that this repair fails by a polynomial margin throughout the bow regime `0<theta<1/2`. Karatsuba's metric theorem at micro-window length `Y^a` permits an exceptional set of starting points of measure `O(Y^(1-a/2))`. A count-saturating bow of exponent `theta`, even after thickening it into **all** internal micro-window starts, forces only `asymp Y^theta/log Y` bad starts. Since the micro-window must fit inside the bow, `a<theta<1/2`, and therefore

\[
\frac{Y^\theta/\log Y}{Y^{1-a/2}}
=\frac{Y^{\theta-1+a/2}}{\log Y}
\longrightarrow0
\]

with a fixed polynomial margin. Thus the theorem's permitted exceptional set is large enough to contain the whole bow-thickened bad-start locus.

More generally, an almost-all theorem at window length `Y^a` with the correct-order lower count `\gg Y^a log Y` and bad-start measure `O(Y^(1-delta+o(1)))` can contradict a **single** count-saturating bow of exponent `theta` by this thickening argument only if

\[
\boxed{\delta>1-\theta}
\]

(up to the endpoint logarithms). Karatsuba supplies `delta=a/2`, which can never satisfy this while `a<theta<1/2`. This closes a tempting de-exceptionalization route; it does not weaken WI-198/WI-202's every-interval pruning and does not rule out stronger metric theorems with a sufficiently small exceptional set or a theorem localized to the source-selected interval.

## 1. Primary-source metric theorem and the exact exceptional measure

A. A. Karatsuba, **The distribution of zeros of the function `zeta(1/2+it)`**, *Math. USSR-Izv.* 25:3 (1985), 519--529, DOI `10.1070/IM1985v025n03ABEH001303` (Russian original 1984), proves metric theorems for odd-order critical-line zeros. The exact form needed here is restated by Karatsuba himself in the introduction of his later paper **On the Number of Zeros of the Riemann Zeta-Function Lying in almost all Short Intervals of the Critical Line**, *Russian Acad. Sci. Izv. Math.* 40:2 (1993), 353--376, DOI `10.1070/IM1993v040n02ABEH002168`.

For every fixed arbitrarily small `a>0` (his parameter is denoted `epsilon`) and

\[
H=T^a,
\]

almost all intervals `(T,T+H)` contain at least

\[
\boxed{c_a H\log T}
\tag{1}
\]

odd-order zeros of `zeta(1/2+it)`, with `c_a>0`. More precisely, for `Y<T<2Y`, the measure of starting points for which (1) fails is

\[
\boxed{O_a\!\left(Y^{1-a/2}\right).}
\tag{2}
\]

The 1993 paper states both (1) and the exponent in (2) explicitly while recalling the earlier theorem, and identifies its reference [1] as the 1984/1985 distribution paper above. The later 1993 supershort theorem is not used here; its different count and exceptional-set scale are not stronger for the present bow-thickening argument.

The quantity counted in (1) is the number of odd-order zero locations on the critical line. That is enough for the count-saturation argument: every such location contributes at least one zero label to the ordinary local Riemann--von Mangoldt count.

## 2. Count saturation makes almost every internal micro-window bad

Take a source-compatible mirror-closed Maynard--Pratt bow at dyadic height `Y`, with

\[
m=Y^\theta,
\qquad 0<\theta<\frac12,
\]

and selected ordinate spacing `c_Y/log Y` at bounded positive scale. WI-184 gives the bow length

\[
L_{\rm bow}
=\left(c_Y+o(1)\right)\frac{m}{\log Y}.
\tag{3}
\]

For a count-saturating bow, `c_Y=4pi+o(1)` and the excess local zero-label budget is `E_I=o(m)`. All but `O(1)` selected right-half bow points and their compulsory mirrors are off the critical line. Hence, if `C_I` denotes the total number of odd-order critical-line zero **locations** in the bow interval, then

\[
\boxed{C_I=o(m).}
\tag{4}
\]

Indeed, apart from the `O(1)` selected critical-line endpoints, every such location must belong to the excess population and consumes at least one unit of `E_I`.

Now fix any exponent

\[
0<a<\theta.
\tag{5}
\]

For a starting point `s` inside the bow define

\[
Z(s):=
N_{0,\mathrm{odd}}(s+s^a)-N_{0,\mathrm{odd}}(s).
\tag{6}
\]

Let `J` consist of the starting points for which `(s,s+s^a]` remains wholly inside the bow. Since `s\asymp Y` and `a<theta`,

\[
|J|
=L_{\rm bow}-O(Y^a)
=(1+o(1))L_{\rm bow}.
\tag{7}
\]

Integrate (6) over `J`. A fixed critical-line zero ordinate can be counted only for starts lying in an interval of length `O(Y^a)`, because `s^a\asymp Y^a` on the dyadic block. Fubini therefore gives

\[
\boxed{
\int_J Z(s)\,ds
\ll Y^a C_I.
}
\tag{8}
\]

Let `G\subseteq J` be the starts satisfying Karatsuba's good lower bound

\[
Z(s)\ge c_a s^a\log s.
\]

Uniformly on `J`, the right side is `\gg_a Y^a log Y`. Combining this with (8),

\[
|G|Y^a\log Y
\ll_a Y^a C_I,
\]

so by (4)

\[
\boxed{
|G|
\ll_a\frac{C_I}{\log Y}
=o\!\left(\frac{m}{\log Y}\right)
=o(L_{\rm bow}).
}
\tag{9}
\]

Thus the strongest possible thickening conclusion is already quite rigid:

\[
\boxed{
|J\setminus G|
=(1-o(1))L_{\rm bow}
\asymp\frac{Y^\theta}{\log Y}.
}
\tag{10}
\]

A count-saturating bow forces **almost every admissible internal micro-window start** to belong to Karatsuba's exceptional set. The remaining question is whether this forced exceptional block is too large for the theorem's global exception budget.

## 3. Karatsuba's exception budget is polynomially larger

Equation (2) allows the global bad-start set inside `(Y,2Y)` to have measure

\[
O_a\!\left(Y^{1-a/2}\right).
\tag{11}
\]

The bow forces only the block (10). Their ratio is

\[
\frac{Y^\theta/\log Y}{Y^{1-a/2}}
=
\frac{Y^{\theta-1+a/2}}{\log Y}.
\tag{12}
\]

But (5) and `theta<1/2` imply

\[
\theta-1+\frac a2
<\frac{3\theta}{2}-1
<-\frac14.
\tag{13}
\]

Consequently

\[
\boxed{
\frac{|J\setminus G|}{Y^{1-a/2}}
\longrightarrow0
}
\tag{14}
\]

by at least a fixed power of `Y`. Karatsuba's almost-all theorem is therefore logically compatible with **the entire bow-thickened start interval being exceptional**. No placement argument is needed: the permitted global bad set is much larger than the one contiguous bad block forced by a single bow.

This is stronger than the generic observation that “almost all does not control a prescribed point.” We have granted the de-exceptionalization attempt its full natural thickening, used every interior start, and still found that the theorem's quantitative exceptional measure leaves polynomial room for the complete source-selected obstruction.

## 4. General de-exceptionalization criterion

The calculation isolates the exact theorem strength a metric zero-reservoir route would need. Suppose an unconditional theorem at window length `Y^a`, with `a<theta`, says that outside a set of starting points of measure

\[
O\!\left(Y^{1-\delta+o(1)}\right),
\tag{15}
\]

every micro-window contains

\[
\gg Y^a\log Y
\tag{16}
\]

odd-order critical-line zero locations. The Fubini argument (8)--(10) is unchanged and forces a count-saturating bow to contribute a bad-start block of measure

\[
Y^{\theta+o(1)}/\log Y.
\tag{17}
\]

For the global metric theorem alone to make one such block impossible, its allowed bad set must be `o` of (17). At the power level this requires

\[
1-\delta<\theta,
\]

or

\[
\boxed{\delta>1-\theta.}
\tag{18}
\]

The equality case is logarithm-sensitive and is not claimed. Karatsuba has `delta=a/2`; because `a<theta<1/2`,

\[
\delta=\frac a2<\frac14
<1-\theta,
\]

so (18) is impossible throughout the Maynard--Pratt fixed-power bow range under consideration.

Criterion (18) is an **interface requirement**, not a universal barrier on metric zeta theorems. A future theorem with a much thinner exceptional set, a theorem whose exceptional set is locally sparse in every interval of bow length, or a source-coupled statement that forbids the bow-selected center can evade it. Likewise, if some independent argument forced a sufficiently dense family of disjoint bows, their bad-start blocks could accumulate beyond a global exceptional budget; no such density-of-bows theorem is assumed here.

## 5. Prior-art boundary and relation to the current frontier

Karatsuba's metric theorem and its exceptional-measure exponent are literature inputs. The bow geometry is Maynard--Pratt prior art, and the mirror/count-saturation bookkeeping is already line-local in WI-184 and WI-198. Equations (8)--(18) are the new line-local deduction: they test whether the quantitative metric theorem can de-exceptionalize a **single source-selected count-saturating bow** after maximal natural thickening.

A bounded novelty audit around Karatsuba's metric theorem, Maynard--Pratt bows, source-selected short intervals, and exceptional-set measure found no published statement of this combined bow-thickening comparison. Absence of a search hit is not evidence of priority, and no priority claim is made.

The result is complementary to WI-190 and WI-196. WI-190 shows that an almost-all **prime/nilsequence** theorem can hide the deterministic stationary alias locus in the prime-side covariance problem; WI-196 shows that a macroscopic twist average cannot force a pointwise lower bound at a distinguished source height. The present finding acts one level earlier, on the **zero-reservoir** side: even when one bow forces a whole interval of bad zero-count starts rather than a single bad center, the classical quantitative almost-all exception budget can still absorb that interval.

WI-198--WI-203's every-interval pruning remains untouched. In particular, improving an every-interval zero theorem can still shrink the bow exponent range, subject to the quarter barrier of WI-203 for the current ordinary exponent-pair architecture. What is closed here is the tempting alternative of replacing the missing every-interval theorem below that frontier by Karatsuba's much shorter almost-all result plus bow thickening.

## 6. Research consequence

For the surviving short-bow regime, an almost-all critical-line reservoir is useful only if it carries a **de-exceptionalization mechanism strong enough to see the source-selected bow**. Merely shortening the micro-window is not sufficient: one must simultaneously shrink the exceptional set to the scale (18), obtain local control of that exceptional set inside every possible bow interval, or couple the zero-reservoir theorem to another source observable.

This redirects the line back to the same structural target exposed independently on the prime side: the remaining obstruction is not ordinary average density but **source-fixed coercivity**. A successful RH-facing mechanism must prevent the geometry from choosing an exceptional location, rather than only proving that exceptional locations are globally sparse.