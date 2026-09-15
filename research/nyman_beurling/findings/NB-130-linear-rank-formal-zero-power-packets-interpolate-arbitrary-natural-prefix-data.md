# NB-130 — linear-rank formal zero-power packets interpolate arbitrary natural-prefix data

**Status:** `EXACT-DERIVED + UNIVERSAL-NATURAL-PREFIX-INTERPOLATION + HIGH-STRIP-ZERO-POWER-CONTROL + LINEAR-RANK-NO-GO + NB-129-RECURRENCE-BOUNDARY + NEGATIVE/ROUTE-NARROWING + PRIOR-ART-AUDITED`.

`NB-129` isolates the next source-specific obstruction after natural-grid phase de-aliasing: its sharp block-erasing matched control is an arbitrary endpoint-matched sequence, not a genuine zero-power primitive. The live escape was therefore to use structure absent from that control, with finite recurrence and analyticity among the most immediate candidates.

Those properties by themselves do **not** exclude the control once packet rank is allowed to grow linearly with the visible prefix. At every finite cutoff, the simple zero-power class is already universal on the natural grid: **any prescribed values on `1,...,R` can be interpolated exactly by `R` distinct right-half zero powers whose real parts are identical and whose ordinates lie in an arbitrarily short interval at an arbitrarily high height.**

Precisely, let `R>=2`, fix

\[
\frac12<\beta<1,
\qquad
T\in\mathbb R,
\qquad
W>0,
\tag{1}
\]

and choose

\[
0<\delta<
\min\!\left\{
\frac{2\pi}{\log R},
\frac{W}{R-1}
\right\}.
\tag{2}
\]

For `0<=j<R` put

\[
\rho_j:=\beta+i(T+j\delta).
\tag{3}
\]

Then for every vector

\[
y=(y_1,\ldots,y_R)\in\mathbb C^R
\tag{4}
\]

there are unique coefficients `c_0,...,c_(R-1)` such that the simple zero-power sum

\[
\boxed{
P_y(n)
:=
\sum_{j=0}^{R-1}c_j n^{-\overline{\rho_j}}
=y_n,
\qquad 1\le n\le R.
}
\tag{5}
\]

All exponents in `(3)` satisfy

\[
\Re\rho_j=\beta\in(1/2,1),
\qquad
T\le\Im\rho_j<T+W.
\tag{6}
\]

Thus the width `W` can be made arbitrarily small independently of the interpolation data. If `T>=G`, the entire interpolating family lies above height `G`.

Applied to the sharp ambient control of `NB-129`, this gives a formal high-strip zero-power primitive with **exactly the same finite target angle, the same weighted Dirichlet energy, and the same completely erased phase-sensitive block**. Consequently, finite recurrence, finite exponential-polynomial analyticity, right-half strip location, high ordinate, and even arbitrarily narrow ordinate support do not by themselves cross the reciprocal-height defect barrier. What remains source-specific must use information that this freely placed formal family does not possess: actual zeta-zero locations/counting, a rank restriction relative to the natural prefix, or quantitative coefficient/model-space geometry.

The word **formal** is essential. The points `(3)` are not asserted to be zeta zeros. This finding therefore does not construct an actual off-critical packet and does not weaken the actual-zero conclusions of `NB-123`--`NB-125`. It identifies exactly which proposed extra structures are still too weak when detached from the arithmetic zero set.

## 1. Natural-prefix evaluation is an ordinary Vandermonde map

For `1<=n<=R` define

\[
z_n:=n^{i\delta}=e^{i\delta\log n}.
\tag{7}
\]

Using `(3)`, the evaluation matrix of the zero powers is

\[
M_{n,j}
:=n^{-\overline{\rho_j}}
=n^{-\beta+iT}z_n^j,
\qquad
1\le n\le R,
\quad
0\le j<R.
\tag{8}
\]

The only possible obstruction is collision of the nodes `z_n`. If `z_n=z_k`, then

\[
\delta\log(n/k)\in2\pi\mathbb Z.
\tag{9}
\]

For distinct `n,k in {1,...,R}`,

\[
0<|\log(n/k)|\le\log R,
\tag{10}
\]

and `(2)` gives

\[
0<|\delta\log(n/k)|<2\pi.
\tag{11}
\]

Hence `(9)` is impossible unless `n=k`. Therefore the `z_n` are pairwise distinct.

Factoring the nonzero row multipliers in `(8)` leaves the ordinary monomial Vandermonde matrix, so

\[
\boxed{
\det M
=
\left(\prod_{n=1}^{R} n^{-\beta+iT}\right)
\prod_{1\le n<k\le R}(z_k-z_n)
\ne0.
}
\tag{12}
\]

Thus the evaluation map

\[
(c_0,\ldots,c_{R-1})
\longmapsto
(P(1),\ldots,P(R))
\tag{13}
\]

is an isomorphism from `C^R` to `C^R`, proving `(5)`.

Equivalently, after multiplying the desired data by `n^(beta-iT)`, `(5)` is just polynomial interpolation of degree `<R` at the distinct points `z_1,...,z_R`. No approximation theorem is involved.

For a **fixed** family of `d` zero powers, the evaluation image has dimension at most `d`; hence surjectivity onto every vector of `C^R` requires `d>=R`. The construction is therefore dimension-sharp as a universal fixed-family interpolator. It does not claim that the particular `NB-129` control requires rank `R`; a target-specific representation may use fewer modes.

## 2. The interpolants retain the exact finite-recurrence structure

The construction does not evade the recurrence mechanism of `NB-123`. On a geometric grid `n=q^k`,

\[
P_y(q^k)
=
\sum_{j=0}^{R-1}
 c_j
\left(q^{-\beta+i(T+j\delta)}\right)^k.
\tag{14}
\]

Hence the samples are annihilated by the degree-`R` polynomial

\[
A_q(z)
:=
\prod_{j=0}^{R-1}
\left(z-q^{-\beta+i(T+j\delta)}\right),
\tag{15}
\]

exactly as in `NB-123`. The same is true of their geometric block increments. All characteristic roots have modulus

\[
q^{-\beta}>q^{-1},
\tag{16}
\]

so the harmonic target root `q^{-1}` is still absent.

There is no contradiction with the logarithmic-rank obstruction. `NB-123` becomes effective only when a recurrence window fits inside the available geometric prefix. Here the recurrence order is `R`, while the number of geometric samples below the natural cutoff is only `O(log R)`. The recurrence is perfectly genuine but is too high-rank to constrain arbitrary length-`R` natural-prefix data.

Likewise, the stable annihilator bound of `NB-124` assumes `R>=q^(d+1)`. With `d=R` this hypothesis is deliberately far outside the present regime. The new conclusion is therefore not that recurrence is useless, but that **recurrence without a rank/conditioning law is not a source separator**.

## 3. The sharp NB-129 block-erasing control has an exact formal zero-power realization

Take the matched control from Section 4 of `NB-129`. For `m>=16` and `R>=4m`, it gives a sequence `P_*` on `1,...,R` with the same endpoint-matched harmonic profile as its target, satisfying

\[
P_*(n)=0,
\qquad
m\le n\le2m,
\tag{17}
\]

and

\[
\frac1{2m}
\le
q_R(P_*)^{-1}-1
\le
\frac3m.
\tag{18}
\]

Set `y_n=P_*(n)` in `(5)`. The resulting formal zero-power sum satisfies

\[
P_y(n)=P_*(n)
\qquad
1\le n\le R.
\tag{19}
\]

Every finite natural-grid observable appearing in `NB-117` and `NB-129` is therefore preserved **exactly**, not asymptotically. In particular,

\[
q_R(P_y)=q_R(P_*),
\tag{20}
\]

and for every real phase shift `S`,

\[
\sum_{n=m}^{2m}
|P_y(n)|^2|n^{iS}-1|^2
=0.
\tag{21}
\]

Now choose the base ordinate in `(1)` to be `T=m`. Since `W>0` is arbitrary, all `R` simple exponents can be placed in

\[
\boxed{
\Re\rho=\beta,
\qquad
m\le\Im\rho<m+W,
}
\tag{22}
\]

while still reproducing the entire sharp control through cutoff `R`.

This is stronger than merely producing a formal packet that vanishes on the phase block. It reproduces the **full prefix**, so the endpoint coordinate, every weighted first difference, the exact reciprocal-height excess energy, and every nested finite-prefix statistic derived solely from those samples are unchanged.

The same interpolation can of course reproduce the perfect harmonic profile `C+D/n` itself on `1,...,R`. Thus even absence of the characteristic root `q^(-1)` does not prevent perfect finite-prefix matching when the recurrence order is allowed to exceed the amount of geometric information available.

## 4. Arbitrarily narrow ordinate support comes with a conditioning warning

The theorem is an existence statement, not a uniform stability theorem. As `delta -> 0`, the nodes `(7)` coalesce and the Vandermonde matrix becomes badly conditioned. Indeed, for fixed `R`,

\[
z_k-z_n
=
 i\delta\,\log(k/n)
+O_R(\delta^2),
\tag{23}
\]

up to harmless unit phases, so `(12)` gives

\[
|\det M|
=
C_{R,\beta}\,
\delta^{R(R-1)/2}
\left(1+O_R(\delta)\right)
\tag{24}
\]

for an explicit constant `C_(R,beta)>0` independent of the target data.

Hence forcing the exponents into a very thin ordinate band can require enormous interpolation coefficients for some data. The construction supplies **no** useful uniform coefficient norm, continuum model-space norm, or inverse-Vandermonde bound. That limitation is mathematically load-bearing rather than cosmetic: it identifies conditioning/model-space geometry as one of the remaining ways an actual zeta packet could differ from the formal control.

In the confluent limit, the same phenomenon becomes ordinary interpolation by

\[
n^{-\beta+iT}p(\log n),
\qquad
\deg p<R,
\tag{25}
\]

which is exactly the multiplicity block allowed by the `NB-117` zero-power normal form. The distinct-exponent construction above is preferable because it shows that high multiplicity is not required for finite-prefix universality; near-confluence of simple formal exponents already suffices.

## 5. What the result rules out, and what it does not

The direct consequence for the frontier after `NB-129` is negative but sharp. A proposed theorem of the form

> an actual-looking primitive cannot erase the matching natural block because every finite zero-power sum is analytic and obeys a finite recurrence

cannot work without an additional quantitative hypothesis. The counterclass `(3)` is analytic, consists of simple right-half powers, lies arbitrarily high, can be confined to an arbitrarily narrow ordinate band, and has the exact finite recurrence of `NB-123`, yet its finite natural-prefix samples are completely unconstrained at rank `R`.

Several genuinely source-specific exits remain open. An actual packet must use the **actual zeta zero set**, not freely chosen arithmetic-progression ordinates. A useful theorem may also exploit a rank bound relative to the cutoff, zero counting or local spacing, the actual Burnol/model-space Gram geometry, or a quantitative coefficient/annihilator condition that survives high rank. `NB-124`--`NB-125` already show how rank and annihilator margins become effective when a full recurrence window is visible; `NB-130` shows why some such quantitative restriction is indispensable.

Nothing here proves that actual zeta zeros can realize the interpolation. In particular, `(22)` generally violates the arithmetic distribution and local counting constraints of the true zero set. Nor does `(24)` prove that coefficient blow-up itself excludes an actual packet; it only records that the present construction does not control that channel. The finding therefore narrows the next theorem to **actual-zero geometry or stable model-space conditioning**, rather than generic exponential-polynomial structure.

## 6. Adversarial and prior-art audit

The algebraic kill tests are exact. The only invertibility input is the collision criterion `(9)` and the strict arc condition `(2)`. The case `n=1` is harmless because `z_1=1`, while `(2)` keeps every `z_n`, `2<=n<=R`, away from `1` modulo a full turn. Negative or positive `T` merely supplies a common nonzero row phase and has no effect on invertibility. The exponents are distinct because `delta>0`. No generic-position assumption or numerical conditioning claim is used.

The obvious attempted falsification is the recurrence obstruction from `NB-123`. Equations `(14)`--`(16)` show explicitly that the interpolant does satisfy that recurrence and still omits the harmonic root. The escape is exactly rank: a degree-`R` annihilator cannot contradict data observed on only `O(log R)` geometric blocks. The `NB-129` application is also exact because `(19)` preserves every value entering its target-angle and visibility formulas.

The interpolation mechanism is classical Vandermonde theory. Generalized/exponential Vandermonde systems are standard in interpolation theory; for example, the neighboring literature includes R. Abu-Saris and W. Ahmad, *Generalized Exponential Vandermonde Determinant and Hermite Multipoint Discrete Boundary Value Problem*, SIAM J. Matrix Anal. Appl., DOI `10.1137/S0895479803421264`. No novelty is claimed for polynomial or exponential Vandermonde interpolation itself. A targeted search of Nyman--Beurling quantitative approximation, Dirichlet/exponential-polynomial interpolation, and the zero-power recurrence setting did not identify this specific finite-prefix universality splice with the sharp `NB-129` reciprocal-height block-erasing control.

No external theorem is load-bearing: `(5)` follows directly from the determinant `(12)`, and the matched sequence in Section 3 is already canonicalized in `NB-129`. `SOURCES.md` therefore needs no new durable dependency.

The durable conclusion is: **the natural-prefix barrier exposed by `NB-129` cannot be crossed by invoking finite recurrence or zero-power analyticity alone. At linear rank, the formal right-half zero-power class is exactly universal on the finite natural grid, even inside an arbitrarily thin high ordinate band.** The next useful source theorem must quantitatively distinguish the actual zeta-zero packet from this high-rank interpolation class.