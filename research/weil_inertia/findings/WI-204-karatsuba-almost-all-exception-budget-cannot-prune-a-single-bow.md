# WI-204 — Karatsuba's almost-all exception budget can absorb an entire count-saturating bow

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`.

WI-198 deliberately used an **every-interval** critical-line-zero theorem to prune long count-saturating Maynard--Pratt bows, because an almost-all theorem need not control a source-selected bow location. There is a natural attempted repair: a bow has positive vertical length, so perhaps a single count-saturating bow forces not one exceptional starting height but a bow-scale set of exceptional starts, large enough to contradict Karatsuba's quantitative almost-all theorem.

The exact bookkeeping below shows that this repair fails by a polynomial margin throughout the bow regime `0<theta<1/2`. Karatsuba's metric theorem at micro-window length `Y^a` permits an exceptional set of starting points of measure `O(Y^(1-a/2))`. A count-saturating bow of exponent `theta`, even after thickening it to **all admissible internal micro-window starts**, forces only `asymp Y^theta/log Y` bad-start measure. Since the micro-window must fit inside the bow, `a<theta<1/2`, and therefore

\[
\frac{Y^\theta/\log Y}{Y^{1-a/2}}
=\frac{Y^{\theta-1+a/2}}{\log Y}
\longrightarrow0
\]

with a fixed polynomial margin. Thus the theorem's permitted exceptional set is large enough to contain the full bad-start mass forced inside one bow interval.

More generally, an almost-all theorem at window length `Y^a` with the correct-order lower count `\gg Y^a\log Y` and bad-start measure `O(Y^(1-delta+o(1)))` can contradict a **single** count-saturating bow of exponent `theta` by this thickening argument only if

\[
\boxed{\delta>1-\theta}
\]

up to endpoint logarithms. Karatsuba supplies `delta=a/2`, which cannot satisfy this while `a<theta<1/2`. This closes a tempting de-exceptionalization route; it does not weaken WI-198/WI-202's every-interval pruning and does not rule out stronger metric theorems with a sufficiently small exceptional set or a theorem localized to the source-selected interval.

## 1. Primary-source metric theorem and exact exceptional measure

A. A. Karatsuba, **The distribution of zeros of the function `zeta(1/2+it)`**, *Math. USSR-Izv.* 25:3 (1985), 519--529, DOI `10.1070/IM1985v025n03ABEH001303` (Russian original: *Izv. Akad. Nauk SSSR Ser. Mat.* 48:6 (1984), 1214--1224), proves two metric theorems for odd-order critical-line zeros. Its Theorem 1 has the following dyadic form. For a fixed admissible arbitrarily small `a>0`, sufficiently large `Y`, and

\[
H=Y^a,
\]

consider starts `s` with `Y<s<2Y`. There is a constant `c_a>0` such that, outside an exceptional set, one has

\[
N_{0,\mathrm{odd}}(s+H)-N_{0,\mathrm{odd}}(s)
\ge c_a H\log s,
\tag{1}
\]

and the measure of the exceptional set is

\[
\boxed{O_a\!\left(Y^{1-a/2}\right).}
\tag{2}
\]

This exact theorem surface was checked against the English version of the 1984 paper. It is also recalled by Karatsuba in the introduction of **On the Number of Zeros of the Riemann Zeta-Function Lying in almost all Short Intervals of the Critical Line**, *Russian Acad. Sci. Izv. Math.* 40:2 (1993), 353--376, DOI `10.1070/IM1993v040n02ABEH002168`, where he states the same correct-order lower count and the `Y^(1-a/2)` exceptional-measure scale before developing the later supershort theory.

The quantity in (1) counts odd-order zero locations on the critical line. That is enough here: every such location contributes at least one zero label to the ordinary local Riemann--von Mangoldt count.

## 2. Count saturation makes almost every internal micro-window start bad

Take a source-compatible mirror-closed Maynard--Pratt bow at dyadic height `Y`, with

\[
m=Y^\theta,
\qquad 0<\theta<\frac12,
\]

and selected ordinate spacing `c_Y/\log Y` at bounded positive scale. WI-184 gives its vertical length

\[
L_{\rm bow}
=\left(c_Y+o(1)\right)\frac{m}{\log Y}.
\tag{3}
\]

For a count-saturating bow, `c_Y=4\pi+o(1)` and the excess local zero-label budget is `E_I=o(m)`. All but `O(1)` selected right-half bow points and their compulsory mirrors are off the critical line. Hence, if `C_I` denotes the total number of odd-order critical-line zero **locations** in the bow interval, then

\[
\boxed{C_I=o(m).}
\tag{4}
\]

Indeed, apart from the `O(1)` selected critical-line endpoints, every such location belongs to the complementary population and consumes at least one unit of the excess label budget.

Now fix any Karatsuba-admissible exponent

\[
0<a<\theta
\tag{5}
\]

and put `H=Y^a`. Let `J` be the set of starts `s` inside the bow for which `(s,s+H]` remains wholly inside it. Since `H=o(L_bow)`,

\[
|J|
=L_{\rm bow}-H
=(1+o(1))L_{\rm bow}.
\tag{6}
\]

Define

\[
Z(s):=N_{0,\mathrm{odd}}(s+H)-N_{0,\mathrm{odd}}(s).
\tag{7}
\]

Integrating over `J`, a fixed critical-line zero ordinate is counted for starts in an interval of length at most `H`. Fubini therefore gives the exact coverage bound

\[
\boxed{
\int_J Z(s)\,ds
\le H C_I.
}
\tag{8}
\]

Let `G\subseteq J` be the starts satisfying Karatsuba's good lower bound (1). Uniformly on the dyadic block, its right side is `\gg_a H\log Y`. Combining with (8),

\[
|G|H\log Y
\ll_a H C_I,
\]

and hence, by (4),

\[
\boxed{
|G|
\ll_a\frac{C_I}{\log Y}
=o\!\left(\frac{m}{\log Y}\right)
=o(L_{\rm bow}).
}
\tag{9}
\]

Thus

\[
\boxed{
|J\setminus G|
=(1-o(1))L_{\rm bow}
\asymp\frac{Y^\theta}{\log Y}.
}
\tag{10}
\]

A count-saturating bow therefore forces **almost every admissible internal micro-window start, in measure**, to be exceptional for Karatsuba's lower bound. No claim is made that the bad subset itself contains one uninterrupted interval; the exact conclusion needed below is the bow-scale measure (10), supported inside a single bow interval.

## 3. Karatsuba's exception budget is polynomially larger

Equation (2) permits the global bad-start set inside `(Y,2Y)` to have measure

\[
O_a\!\left(Y^{1-a/2}\right).
\tag{11}
\]

The bow forces only (10). Their ratio is

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

by a fixed power of `Y`. Karatsuba's almost-all theorem is therefore logically compatible with **every bad start forced by a single count-saturating bow lying inside its permitted exceptional set**. The quantitative theorem leaves much more global exceptional measure than one bow can force.

This is stronger than the generic observation that “almost all does not control a prescribed point.” The de-exceptionalization attempt has been given its full natural thickening: every internal start is used, count saturation forces all but `o(L_bow)` of them to be bad, and the published exceptional-measure allowance still dominates that bad mass polynomially.

## 4. General de-exceptionalization criterion

The same calculation isolates the exact theorem strength a metric zero-reservoir route would need. Suppose an unconditional theorem at window length `Y^a`, with `a<theta`, says that outside a set of starts of measure

\[
O\!\left(Y^{1-\delta+o(1)}\right),
\tag{15}
\]

every micro-window contains

\[
\gg Y^a\log Y
\tag{16}
\]

odd-order critical-line zero locations. The Fubini argument (8)--(10) is unchanged and forces a count-saturating bow to contribute bad-start measure

\[
Y^{\theta+o(1)}/\log Y.
\tag{17}
\]

For the global metric theorem alone to make a single such bow impossible, its allowed bad set must be `o` of (17). At the power level this requires

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
\delta=\frac a2<\frac14<1-\theta,
\]

so (18) is impossible throughout the Maynard--Pratt fixed-power bow range under consideration.

Criterion (18) is an **interface requirement**, not a universal barrier on metric zeta theorems. A future theorem with a much thinner exceptional set, a theorem whose exceptional set is locally sparse inside every interval of bow length, or a source-coupled statement that forbids the bow-selected center can evade it. Likewise, if some independent argument forced a sufficiently dense family of essentially disjoint bows, their bad-start masses could accumulate beyond a global exceptional budget; no such density-of-bows theorem is assumed here.

## 5. Prior-art boundary and relation to the current frontier

Karatsuba's metric theorem and its exceptional-measure exponent are literature inputs. The bow geometry is Maynard--Pratt prior art, and the mirror/count-saturation bookkeeping is already line-local in WI-184 and WI-198. Equations (8)--(18) are the line-local deduction: they test whether the quantitative metric theorem can de-exceptionalize a **single source-selected count-saturating bow** after maximal natural thickening.

A bounded novelty audit around Karatsuba's metric theorem, Maynard--Pratt bows, source-selected short intervals, and exceptional-set measure found no published statement of this combined bow-thickening comparison. Absence of a search hit is not evidence of priority, and no priority claim is made.

The result is complementary to WI-190 and WI-196. WI-190 shows that an almost-all **prime/nilsequence** theorem can hide the deterministic stationary alias locus in the prime-side covariance problem; WI-196 shows that a macroscopic twist average cannot force a pointwise lower bound at a distinguished source height. The present finding acts one level earlier, on the **zero-reservoir** side: even when one bow forces bow-scale bad zero-count measure rather than one bad center, the classical quantitative almost-all exception budget can still absorb it.

WI-198--WI-203's every-interval pruning remains untouched. In particular, improving an every-interval zero theorem can still shrink the bow exponent range, subject to the quarter barrier of WI-203 for the current ordinary exponent-pair architecture. What is closed here is the tempting alternative of replacing the missing every-interval theorem below that frontier by Karatsuba's much shorter almost-all result plus bow thickening.

## 6. Research consequence

For the surviving short-bow regime, an almost-all critical-line reservoir is useful only if it carries a **de-exceptionalization mechanism strong enough to see the source-selected bow**. Merely shortening the micro-window is not sufficient: one must simultaneously shrink the exceptional set to the scale (18), obtain local control of that exceptional set inside every possible bow interval, force enough distinct bows to overrun the global budget, or couple the zero-reservoir theorem to another source observable.

This redirects the line back to the same structural target exposed independently on the prime side: the remaining obstruction is not ordinary average density but **source-fixed coercivity**. A successful RH-facing mechanism must prevent the geometry from choosing an exceptional location, rather than only prove that exceptional locations are globally sparse.