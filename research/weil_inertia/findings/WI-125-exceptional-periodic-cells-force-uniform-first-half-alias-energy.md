# WI-125 — exceptional mirror-symmetric periodic cells force a uniform first-half alias packet

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + PRIOR-ART-REDIRECT`. WI-124 proves qualitatively that any finite-period density-one cell with genuine off-line mirror mass has a nonzero reciprocal alias at some `alpha<=1/2`, but leaves open whether the first-half aliases can all become quantitatively negligible as the period grows. A classical coefficient theorem for self-inversive polynomials, combined with the first-half Newton structure already isolated in WI-124, gives a period-uniform aggregate answer.

For a mirror-symmetric period-`P` cell, put

\[
q=\left\lfloor\frac P2\right\rfloor,
\qquad
p_m=C(m/P).
\]

Then the weighted first-half alias mass

\[
W_P:=\sum_{m=1}^{q}\frac{|p_m|}{m}
\]

satisfies the exact certificate

\[
\boxed{
W_P\le \log 2
\Longrightarrow
\text{every reciprocal-cell root lies on the unit circle},
}
\tag{1}
\]

and the strict version

\[
\boxed{
W_P<\log 2
\Longrightarrow
\text{all reciprocal-cell roots are on the unit circle and simple}.
}
\tag{2}
\]

Consequently any off-line label forces `W_P>log 2`, while a repeated critical-line root forces `W_P>=log 2`. In either exceptional case the first-half aliases carry a **period-uniform squared-energy floor**

\[
\boxed{
\sum_{m=1}^{q}|C(m/P)|^2
>
\frac{6(\log 2)^2}{\pi^2}.
}
\tag{3}
\]

Thus the growing-period escape left open by WI-124 cannot make the entire lower-half reciprocal spectrum disappear in aggregate. The remaining obstruction is no longer existence or amplitude of the selected-cell alias packet; it is extraction against the complementary zeta amplitude in the complete unconditional form-factor square.

## 1. The same self-inversive root polynomial

Use exactly the cell variables of WI-124. A density-one period-`P` cell has labels

\[
(a_j,b_j),\qquad 1\le j\le P,
\]

with the same-ordinate zeta mirror symmetry `(a,b) -> (a,-b)`. Define

\[
z_j=\exp\!\left(\frac{b_j+2\pi i a_j}{P}\right),
\qquad
p_m=\sum_{j=1}^Pz_j^m=C(m/P).
\tag{4}
\]

The mirror map sends `z` to `1/\bar z`, so the multiset of roots is invariant under reciprocal conjugation. If

\[
Q(z)=\prod_{j=1}^P(z-z_j)
=\sum_{k=0}^P(-1)^k e_k z^{P-k},
\qquad e_0=1,
\tag{5}
\]

then, exactly as in WI-124,

\[
\boxed{e_{P-k}=e_P\overline{e_k}},
\qquad |e_P|=1.
\tag{6}
\]

Hence `Q` is monic self-inversive and

\[
|e_{P-k}|=|e_k|.
\tag{7}
\]

The new point is quantitative: instead of requiring the first-half power sums to vanish, control their total weighted size and propagate that control through the Newton exponential.

## 2. Classical coefficient criterion for self-inversive polynomials

Lakatos and Losonczi prove the following sufficient condition. If

\[
P(z)=\sum_{k=0}^{P}A_kz^k
\]

is self-inversive and

\[
|A_P|\ge\frac12\sum_{k=1}^{P-1}|A_k|,
\tag{8}
\]

then every zero of `P` lies on the unit circle. If the inequality is strict, all of those zeros are simple.

For the monic polynomial (5), `|A_P|=1` and the interior coefficient magnitudes are precisely `|e_1|,...,|e_{P-1}|`. Therefore

\[
\sum_{k=1}^{P-1}|e_k|\le2
\Longrightarrow
|z_j|=1\quad\text{for all }j,
\tag{9}
\]

while

\[
\sum_{k=1}^{P-1}|e_k|<2
\Longrightarrow
|z_j|=1\quad\text{for all }j
\quad\text{and the }z_j\text{ are distinct}.
\tag{10}
\]

This coefficient theorem is classical prior art. The line-specific work is to show that the **first half only** of the reciprocal-cell structure factors quantitatively enforces (9)--(10).

## 3. First-half power sums control the first-half coefficients

The standard symmetric-function generating identity is

\[
\sum_{k=0}^{P}e_k t^k
=\prod_{j=1}^P(1+z_jt)
=\exp\!\left(
\sum_{m\ge1}\frac{(-1)^{m-1}}{m}p_m t^m
\right)
\tag{11}
\]

as a formal power series at `t=0`. For `k<=q`, the coefficient `e_k` depends only on `p_1,...,p_k`; terms of degree `m>q` in the exponent cannot contribute.

Define the positive-coefficient majorant

\[
H(t):=
\exp\!\left(
\sum_{m=1}^{q}\frac{|p_m|}{m}t^m
\right)
=\sum_{k\ge0}h_kt^k,
\qquad h_k\ge0.
\tag{12}
\]

Expanding the exponential in (11) and applying the triangle inequality coefficientwise gives

\[
\boxed{|e_k|\le h_k\qquad(0\le k\le q).}
\tag{13}
\]

Therefore, with

\[
L_q:=\sum_{k=1}^{q}|e_k|,
\qquad
W_P:=\sum_{m=1}^{q}\frac{|p_m|}{m},
\]

we obtain

\[
L_q
\le\sum_{k=1}^{q}h_k
\le H(1)-1
=e^{W_P}-1.
\tag{14}
\]

No asymptotic or numerical approximation enters this step. It is simply the coefficientwise majorization of the Newton/symmetric-function exponential.

## 4. Mirror symmetry turns half-coefficient control into full control

Equation (7) converts `L_q` into a bound for every interior coefficient. If `P=2q+1` is odd, then

\[
\sum_{k=1}^{P-1}|e_k|=2L_q.
\tag{15}
\]

If `P=2q` is even, the middle coefficient is counted only once and

\[
\sum_{k=1}^{P-1}|e_k|
=2L_q-|e_q|
\le2L_q.
\tag{16}
\]

Thus in every parity

\[
\boxed{
\sum_{k=1}^{P-1}|e_k|
\le2L_q
\le2(e^{W_P}-1).
}
\tag{17}
\]

If `W_P<=log 2`, then the right side of (17) is at most `2`, so the Lakatos--Losonczi criterion (9) puts every root on the unit circle. Since

\[
|z_j|=e^{b_j/P},
\]

this forces

\[
\boxed{b_j=0\qquad(1\le j\le P).}
\tag{18}
\]

If `W_P<log 2`, then (17) is strict and (10) additionally makes the reciprocal-cell roots simple. This proves (1)--(2).

The contrapositives separate the two exceptional mechanisms relevant to this research line:

\[
\boxed{
\exists j:\ b_j\ne0
\Longrightarrow
W_P>\log2,
}
\tag{19}
\]

and, for an all-critical cell,

\[
\boxed{
\text{a repeated reciprocal-cell root}
\Longrightarrow
W_P\ge\log2.
}
\tag{20}
\]

In a half-open fundamental period, a critical-line multiple zero at one ordinate gives exactly such a repeated root. Thus the same lower-half alias packet responds to **both** off-line mirror mass and critical-line multiplicity, rather than interpreting the uncertified complement as one homogeneous population.

## 5. Uniform `l2` alias energy and an individual-line corollary

Let

\[
H_q^{(1)}=\sum_{m=1}^{q}\frac1m,
\qquad
H_q^{(2)}=\sum_{m=1}^{q}\frac1{m^2}.
\]

Cauchy--Schwarz gives

\[
W_P^2
\le
\left(\sum_{m=1}^{q}|p_m|^2\right)H_q^{(2)}.
\tag{21}
\]

For either an off-line label or a repeated critical-line root, (19)--(20) therefore imply

\[
\sum_{m=1}^{q}|p_m|^2
\ge
\frac{(\log2)^2}{H_q^{(2)}}.
\tag{22}
\]

Since every finite `H_q^{(2)}` is strictly smaller than `pi^2/6`,

\[
\boxed{
\sum_{m=1}^{q}|C(m/P)|^2
>
\frac{6(\log2)^2}{\pi^2}.
}
\tag{23}
\]

This lower bound is independent of `P`. It is therefore substantially stronger than WI-124's qualitative statement that at least one first-half alias is merely nonzero.

The same weighted `l1` estimate also gives an explicit single-line consequence:

\[
\boxed{
\max_{1\le m\le q}|C(m/P)|
\ge
\frac{\log2}{H_q^{(1)}}
}
\tag{24}
\]

for the exceptional class, with strict inequality in the genuinely off-line case. Thus even if the period grows, all first-half aliases cannot simultaneously shrink faster than the reciprocal harmonic number `1/H_q^{(1)}`.

## 6. Repeated cells carry a coherent alias packet, not just one Bragg line

Repeat the cell over `N` periods. At every reciprocal frequency `alpha=m/P`, translation by one period contributes phase one, so

\[
A_N(m/P)=N p_m.
\tag{25}
\]

Summing the selected-block spectral mass across the entire first-half reciprocal packet gives

\[
\sum_{m=1}^{q}|A_N(m/P)|^2
=N^2\sum_{m=1}^{q}|p_m|^2
>
\boxed{
\frac{6(\log2)^2}{\pi^2}N^2
}.
\tag{26}
\]

If the repeated block contains `M=PN` zero labels, this is a lower bound of order `M^2/P^2` on the **aggregate selected-block** Bragg energy. Equation (24) also supplies at least one individual reciprocal line of amplitude at least `N log(2)/H_q^{(1)}`.

All these frequencies lie in `0<alpha<=1/2`, so the support-one arithmetic interface of Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh is already available for fixed `P`. For a growing `P=P(T)`, the separate diagonal-spike restriction corrected in WI-124 still applies at the smallest frequencies: using `L=log T`, the term `L e^{-2L/P}` is negligible exactly when `2L/P-log L -> +infinity` (for example, `P=o(L/log L)`).

The load-bearing global gap is unchanged. Equations (25)--(26) concern a **selected periodic block**. The unconditional BGSTB quantity is the square of the complete zeta amplitude, and the complementary zero population may in principle cancel the selected amplitude before the square is formed. WI-125 therefore does not yet convert (23) into a larger unconditional simple-critical proportion.

What has changed is the burden on such a cancellation model. A growing-period compensator can no longer evade the second observable merely by making each deterministic first-half structure factor arbitrarily tiny with no aggregate cost: it must neutralize a packet whose discrete `l2` energy is bounded below uniformly in the period.

## 7. Stress tests and boundaries

The proof uses only the exact same-ordinate mirror symmetry from WI-124, the classical self-inversive coefficient theorem, and standard symmetric-function identities. It does not assume RH, simplicity, pair-correlation conjectures, a wider Fourier support, or any new prime-side moment.

The `log 2` threshold is a **certified sufficient threshold, not claimed sharp**. Lakatos--Losonczi give a sufficient coefficient condition for unimodularity; their condition is not being asserted to characterize every self-inversive polynomial. Stronger coefficient/root-location criteria, or a direct optimization over the mirror-constrained roots, could improve the constant in (1)--(3).

The bound is deliberately insensitive to horizontal depth. As an off-line pair approaches the critical line, its reciprocal roots approach a repeated unit-circle root, and the exceptional alias packet need not vanish: the limiting object is a critical-line multiple zero, which is itself outside the simple-critical population being certified. Thus the nonzero floor does not contradict continuity; it reflects the fact that the relevant exceptional class includes both off-line mirror pairs and multiplicity.

Conversely, a large first-half alias packet does **not** prove that a cell is exceptional. Irregular simple all-critical cells may also have large reciprocal structure factors. The useful implication is one-way: sufficiently small weighted first-half aliases certify the simple-on-line cell class, while exceptional cells necessarily pay the quantitative packet cost.

Finally, (23) is not itself a localization theorem. It says nothing about whether packets from many embedded cells align, overlap, or are canceled by the rest of the actual zero set. Any global defect-to-zero bootstrap must still control that extraction problem without double-counting or silently replacing the complete BGSTB square by a selected sub-sum.

## 8. Prior-art audit and provenance

The decisive coefficient input is Piroska Lakatos and László Losonczi, **Self-inversive polynomials whose zeros are on the unit circle**, *Publicationes Mathematicae Debrecen* 65 (2004), 409--420, DOI `10.5486/PMD.2004.3250`. Their Theorem 1 proves (8) and the simplicity conclusion under strict inequality. The broader self-inversive root-location literature includes Cohn's classical criterion and M. N. Lalin and C. J. Smyth, **Unimodularity of zeros of self-inversive polynomials**, *Acta Mathematica Hungarica* 138 (2013), 85--101, DOI `10.1007/s10474-012-0225-4`, which generalizes Cohn and subsumes several sufficient coefficient criteria. No novelty is claimed for these polynomial theorems.

The exponential identity (11), Newton--Girard relations, and the harmonic-series/Cauchy--Schwarz steps are classical. WI-124 already established the line-specific self-inversive dictionary from exact zeta mirror symmetry and proved that the first half of the power sums is the correct reciprocal range.

A targeted search around self-inversive polynomials, power sums, Newton identities, coefficient unimodularity criteria, and first-half moment conditions located the classical coefficient literature above but not the specific implication (1)--(3) for zeta reciprocal cells. Absence from that search is not evidence of priority, and no priority claim is made. The durable contribution here is the **combination**: first-half zeta structure factors majorize the first-half elementary symmetric coefficients; mirror symmetry reflects that control across the full coefficient vector; a classical unimodularity criterion then yields an explicit `log 2` certificate and a period-uniform alias-energy floor.

The zeta-side spectral input remains S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya and C. L. Turnage-Butterbaugh, **An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function**, *Acta Arithmetica* 214 (2024), 357--376, arXiv:2306.04799. WI-125 uses that theorem only to identify the eventual arithmetic interface; the algebraic packet bounds (1)--(26) do not depend on it.

## 9. Research implication

WI-122 showed that count regularity alone cannot expose a compensated screen. WI-123 and WI-124 then forced a subcritical, eventually lower-half, reciprocal alias but left a growing-period amplitude loophole. WI-125 closes that **amplitude-only** loophole at the cell level: an exceptional mirror-symmetric cell has at least `log 2` of weighted first-half alias mass and more than `6(log 2)^2/pi^2` of discrete first-half squared energy, uniformly in the period.

The next live question is therefore sharper. A successful global countermodel must arrange **external cancellation of a uniformly energetic lower-half alias packet**, not merely push one tiny Bragg line around inside support one. Conversely, a coercive localization or large-sieve-type inequality that prevents the complementary zeta population from canceling too many such packets could turn WI-121's count control plus WI-125's spectral packet into the defect-to-zero bootstrap sought by this line. Any such inequality must be tested against overlapping cells and the full complete-square representation before it can be used as evidence.