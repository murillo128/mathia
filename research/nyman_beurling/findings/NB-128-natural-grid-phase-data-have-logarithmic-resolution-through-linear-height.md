# NB-128 — natural-grid phase data have logarithmic resolution through linear height

**Status:** `EXACT-DERIVED + NATURAL-GRID-PHASE-MODULUS + HEIGHT-STABILITY + COMMON-VERTICAL-TRANSLATION + NB-127-ESCAPE-SHARPENING + NB-006-COMPATIBLE + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

`NB-126` shows that one geometric base is exactly periodic in ordinate, and `NB-127` shows that every fixed finite family of bases remains globally unstable: simultaneous Diophantine returns make the labelled multibase roots, annihilator coefficients, margins, and every fixed finite geometric sample window arbitrarily close again at unbounded vertical shifts while the Burnol mass tends to zero. The line therefore left open a qualitatively different escape: retain the primitive on the **full natural grid** rather than on finitely many geometric rays.

That escape has a genuine quantitative effect. For `R>=4`, define the natural-prefix phase map

\[
\Phi_R(T):=(n^{iT})_{2\le n\le R}
\tag{1}
\]

and its sup separation

\[
d_R(S,T)
:=
\max_{2\le n\le R}|n^{iT}-n^{iS}|
=
\max_{2\le n\le R}|n^{i(T-S)}-1|.
\tag{2}
\]

Put

\[
L_R:=\lfloor \log_2R\rfloor,
\qquad
c_*:=\sin\!\left(\frac{\log2}{2}\right),
\qquad
c_1:=\frac{2\log2}{\pi}.
\tag{3}
\]

Then, for every pair of ordinates satisfying

\[
|T-S|\le R-1,
\]

one has the explicit stability modulus

\[
\boxed{
 d_R(S,T)
 \ge
 \min\!\left\{
 c_*,
 c_1L_R|T-S|
 \right\}.
}
\tag{4}
\]

Thus the full natural prefix is not merely injective at infinite precision. It has **logarithmic local height resolution throughout a linear-height window**. In particular, if

\[
d_R(S,T)<c_*,
\tag{5}
\]

then either

\[
\boxed{
|T-S|
<
\frac{c_*}{c_1L_R}
\asymp \frac1{\log R},
}
\tag{6}
\]

or necessarily

\[
\boxed{|T-S|>R-1.}
\tag{7}
\]

Equivalently, inside every ordinate window of diameter `R-1`, natural-prefix phase data determine height to `O(1/log R)` at any fixed accuracy below `c_*`. This is exactly the type of **height-dependent phase modulus** that `NB-127` showed cannot exist for any fixed finite family of bases.

The result applies directly to the formal common vertical translations used in `NB-126`--`NB-127`. If a finite zero-power primitive is written in the `NB-117` normal form

\[
P_F(n)
=
\sum_j\sum_{r<m_j}
 c_{j,r}\,
 n^{-\overline\rho_j}(\log n)^r,
\tag{8}
\]

and every exponent is translated by the same ordinate `T`, then

\[
\boxed{
P_{F_T}(n)=n^{iT}P_F(n)
}
\tag{9}
\]

for every natural `n`; the same factor multiplies every confluent block. Hence the relative natural-grid modulation of two common translates is exactly the phase vector in `(2)`. A common-shift near-alias that is invisible at fixed bases cannot remain uniformly phase-close on the complete natural prefix unless its shift is either `O(1/log R)` or already larger than the section scale `R`.

This does **not** yet give a Burnol-mass or target-angle lower bound. The phase scaffold in `(1)` is observable from labelled root data, but the unlabelled primitive sample in `(9)` can be tiny or zero at a witnessing integer. Turning `(4)` into a source theorem therefore requires one additional amplitude/conditioning statement: a target-bearing zero-power primitive must carry enough nonnegligible mass on natural cells where the phase modulus fires. That is the remaining bridge; the global finite-base recurrence obstruction itself is no longer the issue inside the linear height window.

## 1. Small height differences are amplified by the largest dyadic point

Write

\[
\Delta:=|T-S|.
\tag{10}
\]

The metric `(2)` depends only on `Delta`, so assume `Delta>=0`. First suppose

\[
0\le\Delta\le\frac1{L_R}.
\tag{11}
\]

The dyadic point

\[
n=2^{L_R}
\]

lies in the natural prefix because `2^(L_R)<=R`. At that point

\[
x:=\Delta\log n
=\Delta L_R\log2
\le\log2<\pi.
\tag{12}
\]

Therefore

\[
|n^{i\Delta}-1|
=2\sin\frac x2.
\tag{13}
\]

Using `sin y >= 2y/pi` for `0<=y<=pi/2` gives

\[
|n^{i\Delta}-1|
\ge
\frac{2x}{\pi}
=
\frac{2\log2}{\pi}L_R\Delta
=c_1L_R\Delta.
\tag{14}
\]

Thus the natural phase map has an explicit inverse-Lipschitz scale `1/log R` near every ordinate, not just near the origin. This local statement is translation-invariant because only the difference `T-S` appears.

## 2. Dyadic powers give a constant gap from `1/log R` up to unit height

Now assume

\[
\frac1{L_R}\le\Delta\le1.
\tag{15}
\]

Choose

\[
k:=\left\lceil\frac1\Delta\right\rceil.
\tag{16}
\]

Since `Delta>=1/L_R`, one has `k<=L_R`, so the dyadic integer

\[
n=2^k
\]

again lies in the natural prefix. Moreover

\[
1\le k\Delta\le1+\Delta\le2.
\tag{17}
\]

Hence

\[
\log2
\le
\Delta\log n
\le
2\log2
<\pi.
\tag{18}
\]

The chord length `|e^(ix)-1|=2sin(x/2)` is increasing for `0<=x<=pi`, so

\[
|n^{i\Delta}-1|
\ge
2\sin\!\left(\frac{\log2}{2}\right)
=2c_*.
\tag{19}
\]

In particular

\[
d_R(S,T)\ge2c_*>c_*.
\tag{20}
\]

The transition at scale `1/L_R` is therefore not a Diophantine accident. A dyadic point can always be chosen adaptively so that the accumulated phase lies in a fixed arc separated from `1`.

## 3. Adjacent natural integers give a constant gap through height `R`

It remains to treat

\[
1\le\Delta\le R-1.
\tag{21}
\]

Set

\[
n:=\lfloor\Delta\rfloor,
\qquad
m:=n+1.
\tag{22}
\]

Then `1<=n<m<=R`. Consider the relative phase between these adjacent integers,

\[
e^{ix}
:=
\left(\frac mn\right)^{i\Delta},
\qquad
x=\Delta\log\left(1+\frac1n\right).
\tag{23}
\]

Because `Delta>=n`,

\[
x
\ge
n\log\left(1+\frac1n\right)
\ge\log2.
\tag{24}
\]

The last inequality is elementary: the binomial theorem gives `(1+1/n)^n>=2`. On the other hand, `Delta<n+1` and `log(1+u)<=u`, so

\[
x
<
(n+1)\log\left(1+\frac1n\right)
\le
1+\frac1n
\le2
<\pi.
\tag{25}
\]

Thus again

\[
|e^{ix}-1|
\ge
2\sin\!\left(\frac{\log2}{2}\right)
=2c_*.
\tag{26}
\]

But

\[
e^{ix}
=m^{i\Delta}\overline{n^{i\Delta}},
\]

and therefore

\[
|e^{ix}-1|
=|m^{i\Delta}-n^{i\Delta}|
\le
|m^{i\Delta}-1|+|n^{i\Delta}-1|.
\tag{27}
\]

At least one of the two terms on the right is at least `c_*`. If `n>=2`, both coordinates occur explicitly in `Phi_R`. If `n=1`, the first coordinate is the fixed anchor `1^(iDelta)=1`, so `(26)` actually forces the available coordinate `m=2` to have distance at least `2c_*`. Consequently

\[
\boxed{d_R(S,T)\ge c_*}
\qquad
(1\le|T-S|\le R-1).
\tag{28}
\]

Combining `(14)`, `(20)`, and `(28)` proves `(4)`.

## 4. Common zero-packet translations inherit the same phase modulus

Retain the zero-power representation from `NB-117`. For a simple exponent,

\[
n^{-\overline{(\rho+iT)}}
=
n^{-\bar\rho+iT}
=
n^{iT}n^{-\bar\rho}.
\tag{29}
\]

For a confluent block the polynomial factor `(log n)^r` is unchanged, so the same common scalar `n^(iT)` factors out of the entire block. Holding the zero-power coefficients fixed therefore gives `(9)` exactly.

For two translates `F_S` and `F_T`, every nonzero primitive coordinate obeys

\[
\frac{P_{F_T}(n)}{P_{F_S}(n)}
=n^{i(T-S)}.
\tag{30}
\]

Equivalently,

\[
|P_{F_T}(n)-P_{F_S}(n)|
=|P_F(n)|\,|n^{i(T-S)}-1|.
\tag{31}
\]

Thus `(4)` supplies an exact stability modulus for the **relative phase scaffold** of the natural-grid representation. If one keeps labelled roots across all bases `2,...,R`, as in the strongest data class considered in `NB-127`, no simultaneous near-return of a common vertical translation can occur in the annulus

\[
\frac{c}{\log R}
\lesssim
|T-S|
\le
R-1
\tag{32}
\]

at fixed accuracy below `c_*`.

This is the precise distinction between a fixed multibase family and the growing natural prefix. `NB-127` gives arbitrarily high simultaneous near-aliases for every fixed family. Here the observation family itself grows with `R`, and adjacent natural ratios become available at the same scale as the candidate height difference. They act as an adaptive local frequency ruler.

## 5. This is local height coercivity, not global de-aliasing

Equation `(4)` deliberately stops at height `R-1`. It does not say that the complete natural prefix is globally coercive in ordinate. In fact `NB-006` already supplies the opposite long-range calibration: finitely many natural dilation probes still admit simultaneous Mellin recurrences at sufficiently large frequencies, with a quantitative probe-budget obstruction derived from the independent prime-log directions.

There is no conflict. `NB-006` is a **global recurrence** statement; `(4)` is a **mesoscopic inverse modulus**. The full natural prefix buys a deterministic alias-free window whose height is linear in the largest retained integer, together with local resolution `1/log R`, but recurrence can return again much farther out.

This distinction also prevents an overinterpretation of `(7)`. If two natural-prefix phase vectors are closer than `c_*`, the theorem says that their heights are either locally indistinguishable at the `1/log R` scale or separated by more than `R-1`. It does not locate a far alias, bound the first recurrence time, or improve the global recurrence budget of `NB-006`.

## 6. Representation boundary and the remaining source-facing gate

The phase modulus is exact, but the raw primitive is amplitude-weighted by `(31)`. A zero-power sum can in principle be very small at the dyadic or adjacent integer selected by the proof. Therefore no universal estimate of the form

\[
\max_{n\le R}|P_{F_T}(n)-P_{F_S}(n)|
\ge
c\,\|P_F\|_{\mathrm{natural}}
\tag{33}
\]

follows from `(4)` without an additional nonconcentration statement. Nor does `(4)` by itself lower-bound the target angle `chi_(F,R)`, the compression retention, or Burnol's mass.

This limitation is load-bearing rather than cosmetic. `NB-117` shows that target capture is governed by the weighted first-difference energy of the same natural-grid primitive. `NB-123`--`NB-125` then extract recurrence constraints from geometric subsequences, while `NB-126`--`NB-127` show that fixed-base phase information is altitude-blind. The present result says that the **full natural grid repairs the phase side of that failure on the whole section-scale height window**. What remains is to make the phase witness visible through the target-bearing primitive itself.

A useful next theorem would therefore need to prove one of the following equivalent kinds of source information: near-perfect target capture forces nonnegligible primitive amplitude on enough adjacent natural cells; a weighted natural-grid phase defect is bounded below despite possible isolated cancellations; or the weighted Dirichlet energy from `NB-117` prevents all phase-witness cells from being simultaneously amplitude-invisible. Any of these would splice `(4)` to the compression/Burnol side without requiring a globally stable finite-base height estimator.

The formal translations used here are the same representation-level controls as in `NB-126`--`NB-127`; translating an arbitrary packet of exponents does **not** produce another packet of actual zeta zeros. Accordingly, `(4)` is not a zero-spacing theorem and makes no claim about vertical translation invariance of the zeta zero set.

## 7. Adversarial and prior-art audit

The main failure modes are explicit in the proof. The small-shift argument uses only the largest dyadic point `2^(L_R)` and never crosses the branch of the chord because its phase is at most `log 2`. The intermediate argument chooses `k=ceil(1/Delta)` and is valid precisely because `Delta>=1/L_R` guarantees `k<=L_R`. The large-shift argument uses the adjacent pair `floor(Delta), floor(Delta)+1`; the hypothesis `Delta<=R-1` is exactly what keeps that pair inside the prefix. Negative shifts are handled by complex conjugation. The `n=1` boundary case is harmless because its phase is exactly one and the adjacent coordinate `2` alone carries the whole gap.

The packet statement is also restricted to a **common** vertical translation with the zero-power coefficients fixed. Independent movements of different roots do not factor as `(9)`. Multiplicity causes no additional term because every confluent basis vector acquires the same scalar `n^(iT)`. The theorem concerns relative phase data; it does not silently assume that the unlabelled primitive has a nonzero value at the witnessing coordinate.

A targeted literature search found the expected neighboring themes: Nyman--Beurling Mellin formulations, multiscale `2^j3^k` ladders, and the pretentious-number-theory use of the Archimedean character `n^(it)`. None of those sources is load-bearing here, and the bound `(4)` is proved directly from dyadic points and adjacent integer ratios. No priority claim is made for the elementary phase lemma itself. No new specialized external theorem is required, so `SOURCES.md` remains unchanged.

The durable line-local delta is the quantitative answer to the escape left by `NB-127`: **a growing natural prefix does possess a height-dependent stability modulus**. It resolves common vertical shifts to `O(1/log R)` throughout a height window of size `Theta(R)`. The remaining obstruction is no longer simultaneous finite-base phase recurrence inside that window; it is whether the target-bearing natural-grid primitive exposes enough amplitude for this phase modulus to become a compression/Burnol inequality.