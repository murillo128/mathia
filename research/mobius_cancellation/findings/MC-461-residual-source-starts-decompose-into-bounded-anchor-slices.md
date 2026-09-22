# MC-461 — Residual source starts decompose into bounded anchor slices

**Status:** `EXACT-DERIVED` · `CLASSICAL-IDENTITY` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the one-sided staged family of `MC-460`. The apparent two-parameter source variation

\[
s\longmapsto (U_s,D_s)
\]

does **not** automatically restore the full two-dimensional source-frame tariff of `MC-446`. After fixing the outer pair and one gcd sector, the start coordinate `U_s` factors through a much smaller residue quotient, and for prime source conductor each fixed-start slice has an exact complete-shift second moment of size at most `pH`.

Write, as in `MC-460`,

\[
r=g r_1,
\qquad
r'=g r_2,
\qquad
h=g h_0,
\qquad
(r_1,r_2)=1,
\]

fix a residual divisor sector

\[
d=(s,r_2),
\qquad
s=d s_0,
\qquad
r_2=d t,
\qquad
h_0=d h_1,
\qquad
(s_0,t)=1,
\]

and let `m_s (mod t)` be the unique solution of

\[
r_1s_0m_s\equiv h_1\pmod t.
\tag{1}
\]

Put

\[
g_0=(h_1,t),
\qquad
t_0=t/g_0.
\tag{2}
\]

Then

\[
\boxed{
m_s\equiv m_{s'}\pmod t
\quad\Longleftrightarrow\quad
s_0\equiv s'_0\pmod{t_0}.}
\tag{3}
\]

Consequently, as `s_0` ranges over units modulo `t`, the residue `m_s` takes exactly

\[
\boxed{\varphi(t_0)}
\tag{4}
\]

distinct values. Since

\[
U_s\equiv m_st^{-1}\pmod p
\tag{5}
\]

for a prime conductor `p` with `(p,t)=1`, any source subfamily in this fixed `d` sector occupies at most

\[
\boxed{R_U\le \min\{p,\varphi(t_0)\}}
\tag{6}
\]

distinct start anchors. If `t<p`, reduction modulo `p` is injective on the canonical representatives `0\le m_s<t`, so `U_s` has exactly the same fibre partition as `(3)` on the represented `s_0` classes.

The reciprocal shift remains

\[
D_s\equiv\delta s_0^{-1}\pmod p.
\tag{7}
\]

Thus, when `\delta\ne0`, each fixed-`U` fibre consists of reciprocal shifts indexed by one congruence class

\[
s_0\equiv a\pmod{t_0}.
\tag{8}
\]

When `t<p`, equality of both source coordinates satisfies the sharper CRT condition

\[
(U_s,D_s)=(U_{s'},D_{s'})
\quad\Longleftrightarrow\quad
s_0\equiv s'_0\pmod{pt_0},
\tag{9}
\]

provided `\delta\ne0`. The pair family is therefore a one-integer CRT image, not a set with two independent source coordinates.

There is a matching exact energy statement. Let `chi` be a nonprincipal character modulo the prime `p`, let `J` be any fixed interval of `H<=p` consecutive integers, and define

\[
K_J(U,D)
:=\sum_{j\in J}
\chi(j+U)\overline{\chi(j+U-D)}.
\tag{10}
\]

For each fixed anchor `U`,

\[
\boxed{
\sum_{D\bmod p}|K_J(U,D)|^2
=pA_J(U)-|C_J(U)|^2
\le pH,
}
\tag{11}
\]

where

\[
A_J(U)=\sum_{j\in J}|\chi(j+U)|^2,
\qquad
C_J(U)=\sum_{j\in J}\chi(j+U).
\tag{12}
\]

Hence if a weight `W(U,D)` is supported on source pairs using only an anchor set `\mathcal U`, then

\[
\boxed{
\left|\sum_{U,D}W(U,D)K_J(U,D)\right|
\le
\|W\|_2\sqrt{|\mathcal U|\,pH}.
}
\tag{13}
\]

Compared with the pointwise estimate `H||W||_1`, this fixed-anchor slicing certifies a gain whenever

\[
\boxed{
R_{\rm eff}(W)
:=\frac{\|W\|_1^2}{\|W\|_2^2}
>
|\mathcal U|\frac pH.
}
\tag{14}
\]

For the `MC-460` gcd sector, `|\mathcal U|<=\varphi(t_0)` may therefore replace the ambient `p` start count. In the equal-weight heuristic, `(14)` asks for average occupancy per represented `U` fibre greater than `p/H`; it does **not** ask for `p^2/H` unrelated source points.

This is a real narrowing of the `MC-460` uncertainty. Variable `U_s` can recover the old quadratic ambient tariff only when its anchor diversity itself reaches conductor scale. It is not intrinsically a second free conductor-sized coordinate: the congruence defining `m_s` compresses it to at most `phi(t/(h_1,t))` anchor classes before any analytic estimate is applied.

The result does **not** yet estimate the full staged kernel of `MC-460`. Its surviving factor

\[
\overline{B_\beta(C_s+r_1s_0j)}
\]

depends on `s` and `j`; inserting it destroys the direct reduction to the bare kernel `(10)` unless its dependence is preserved through a stronger weighted dispersion argument. Variable interval lengths `J_s` also require separate control. Thus `(13)` is a source-frame energy classification, not a conductor-power saving for Möbius cancellation.

No new estimate for `M(x)`, no improved twisted-Mertens bound, and no RH consequence follows.

## 1. The congruence defining the start loses a factor `(h_1,t)`

Equation `(1)` gives

\[
m_s\equiv h_1(r_1s_0)^{-1}\pmod t.
\tag{15}
\]

For two admissible reduced divisors `s_0,s'_0`, multiplication by the unit `r_1^{-1}` shows

\[
m_s\equiv m_{s'}\pmod t
\]

if and only if

\[
t\mid h_1(s_0^{-1}-{s'_0}^{-1}).
\tag{16}
\]

Writing `h_1=g_0h_*` and `t=g_0t_0` with `(h_*,t_0)=1`, condition `(16)` is equivalent to

\[
s_0^{-1}\equiv {s'_0}^{-1}\pmod{t_0}.
\tag{17}
\]

Both residues are units modulo `t_0`, so inversion is a bijection and `(17)` is equivalent to `s_0=s'_0 (mod t_0)`. This proves `(3)`.

Multiplication of one fixed residue by all units modulo `t` produces exactly the residues with gcd `g_0` against `t`; equivalently, reduction of the unit variable to modulo `t_0` gives all `phi(t_0)` unit classes. Hence `(4)` follows. The extreme case is informative: if `t|h_1`, then `t_0=1`, `m_s=0 (mod t)` for every admissible `s_0`, and the entire gcd sector has one source anchor.

Because `(p,t)=1` on the nonzero character support, `(5)` is legitimate. It can only identify additional `m_s` values after reduction modulo `p`, which proves `(6)`. If `t<p`, distinct canonical representatives modulo `t` remain distinct modulo `p`, so no additional collision occurs.

## 2. The pair family is a CRT image, not a free box

Assume `delta!=0 (mod p)`. Equation `(7)` gives

\[
D_s=D_{s'}
\quad\Longleftrightarrow\quad
s_0\equiv s'_0\pmod p.
\tag{18}
\]

When `t<p`, equation `(3)` simultaneously gives

\[
U_s=U_{s'}
\quad\Longleftrightarrow\quad
s_0\equiv s'_0\pmod{t_0}.
\tag{19}
\]

Since `(p,t_0)=1`, the two conditions combine by CRT into `(9)`. In particular, on any integer range of `s_0` shorter than `pt_0`, the map to `(U_s,D_s)` has no pair collisions.

This distinction is important. Lack of collisions does **not** mean two-dimensional freedom: the pairs lie on the image of one integer parameter modulo `pt_0`, and their first coordinate occupies at most `phi(t_0)` slices. Conversely, merely calling the family one-dimensional does not yield cancellation. Its analytic usefulness depends on how many reciprocal shifts are populated inside each anchor slice and on how the surviving `B_beta` amplitude correlates with those shifts.

If `delta=0`, all `D_s` are zero and the translated character phase degenerates to a nonoscillatory modulus-square factor. That case does not supply the reciprocal-shift mechanism sought by this branch and must not be counted as favourable low-dimensional structure.

## 3. Exact second moment over reciprocal-shift coordinate

Fix `U`. Expanding `(10)` gives

\[
\sum_D|K_J(U,D)|^2
=
\sum_{j,k\in J}
\chi(j+U)\overline{\chi(k+U)}
\sum_D
\overline{\chi(j+U-D)}\chi(k+U-D).
\tag{20}
\]

For a nonprincipal character modulo the prime `p`, the complete shifted correlation is

\[
\sum_D
\overline{\chi(x-D)}\chi(y-D)
=
\begin{cases}
p-1,&x=y,\\
-1,&x\ne y.
\end{cases}
\tag{21}
\]

This is the prime specialization of the primitive-character/Ramanujan autocorrelation already used in `MC-413` and `MC-446`. Therefore

\[
\begin{aligned}
\sum_D|K_J(U,D)|^2
&=(p-1)A_J(U)
-\sum_{j\ne k}
\chi(j+U)\overline{\chi(k+U)}\\
&=pA_J(U)-|C_J(U)|^2,
\end{aligned}
\tag{22}
\]

which proves `(11)`. No Weil estimate is needed.

Summing `(11)` only over anchors in `\mathcal U`, then applying Cauchy to a weighted aggregate, gives `(13)`. Comparison with `H||W||_1` gives `(14)`.

The contrast with `MC-446` is now exact at the representation level. Full-box Cauchy pays for all `p` start anchors and all `p` shifts. The staged congruence family pays only for the anchors it actually occupies, and the complete shift moment inside each such anchor has energy at most `pH`. The conductor cost is therefore controlled by **anchor diversity times one shift conductor**, rather than by two independent ambient conductors.

## 4. Representation audit

Four exact views of the `MC-460` source family were available before choosing the estimate above.

The raw pair representation `(U_s,D_s)` preserves the source phase directly but makes the family look artificially two-dimensional. The lifted congruence representation `(m_s mod t, s_0^{-1} mod p)` preserves the two arithmetic origins of those coordinates and exposes that `m_s` is not free. The anchor-fibre representation groups by `m_s`, hence by `s_0 mod t_0`, and preserves the exact reciprocal `D_s` variation inside each fibre; it is the strongest representation for the immediate energy question because `(21)` diagonalizes the complete `D` average. Finally, the aligned-amplitude representation from `MC-460`, `C_s=r_1s_0(U_s-D_s) (mod p)`, preserves the surviving `B_beta` coupling and will be necessary for any estimate of the full staged kernel, but by itself does not classify source-pair multiplicity.

Thus the anchor-fibre representation is used only for the source-frame subproblem. The aligned-amplitude representation remains mandatory at the next quantitative step; replacing it permanently by the bare kernel would discard the very factor-specific information that motivated the staging.

## 5. Prior art and novelty boundary

The complete shifted-character correlation `(21)` is classical; for primitive characters it is the prime-conductor specialization of the Ramanujan autocorrelation identity already audited in `MC-413`. The slice moment `(11)` is an immediate finite second-moment consequence of that identity. No novelty is claimed for character orthogonality, complete shifted correlations, Cauchy, or the participation-ratio comparison.

Mean values of incomplete character sums are an established subject. Ayyad, Cochrane and Zheng, *The congruence x1 x2 = x3 x4 (mod p), the equation x1 x2 = x3 x4, and mean values of character sums*, Journal of Number Theory 59 (1996), 398–413, DOI `10.1006/jnth.1996.0105`, is classical neighboring moment literature. Reciprocal-variable bilinear estimates are also established prior art; for example Shparlinski, *On Bilinear Exponential and Character Sums with Reciprocals of Polynomials* (arXiv:1504.03192), treats bilinear exponential and multiplicative-character sums with reciprocal polynomial arguments. The recent Blomer--Pascadi preprint *Bilinear forms with Kloosterman sums via quadratic characters* (arXiv:2607.24311, submitted 27 July 2026) gives new power-saving bilinear Kloosterman estimates through quadratic-character structure.

Those works confirm that moment and reciprocal-variable methods are classical/active analytic languages; none is imported here as an estimate for the specific staged map `(1)`--`(7)` or its surviving divisor-sum amplitude. A targeted audit on 22 September 2026 found no basis for claiming the branch-specific anchor quotient `(3)` or the source-budget consequence `(14)` as a literature theorem. Absence from this bounded audit is not a novelty proof, and no novelty is claimed.

The durable Mathia delta is narrower: once the exact `MC-460` congruence is kept, its varying start coordinate has a finite arithmetic quotient `t_0=t/(h_1,t)`, and the classical complete-shift second moment can be applied **after** that quotient is exposed. This rules out treating `U_s` as an automatically free second conductor-sized coordinate.

## Boundaries and falsification tests

- **Prime conductor is used in `(21)`--`(14)`.** For general primitive composite conductor, the complete shift correlation is the Ramanujan sum `c_q(k-j)` and the slice moment has a different exact kernel. The congruence quotient `(3)`--`(6)` itself does not require prime conductor beyond invertibility.
- **A common interval is used in `(10)`--`(14)`.** The actual `J_s` can vary with `s`. Any application must preserve the anchor classification through a legitimate variable-length or maximal estimate; reindexing unrelated interval starts can create new effective `U` variation.
- **The surviving residual amplitude is not covered.** The full `MC-460` summand contains `B_beta(C_s+r_1s_0j)`. Bounding or expanding it before exploiting `(13)`--`(14)` can destroy the staged alignment and return to the old product-level tariff.
- **Anchor cardinality is not effective occupancy.** The estimate needs weight spread inside anchor fibres. Highly concentrated coefficients can make `R_eff` too small even when many nominal `s` values are present.
- **Small `t_0` is only potential leverage.** If `phi(t_0)` is conductor-sized, the restricted envelope can be as expensive as the full box. If it is small but each anchor fibre contains fewer than about `p/H` effective reciprocal shifts, `(14)` still gives no improvement.
- **The reciprocal map can wrap.** When the integer `s_0` range exceeds `p`, distinct integers can share the same `D`; weights must be aggregated before computing `R_eff`.
- **The degenerate shift `delta=0` is not a positive case.** Low pair dimension then reflects loss of oscillation, not useful cancellation.
- **No later source budget has been paid.** Outer `(r,r')`, gcd-sector summation, residual coefficients, variable lengths, the surviving amplitude, exceptional ranges, and the `MC-415`/`MC-448` source-depth costs remain outside the present estimate.

## Consequence for the research line

`MC-460` left open whether the variable start `U_s` restores the two-dimensional source-frame barrier. The answer is now sharper: **not by dimension alone**. In a fixed gcd sector the start factors through `s_0 mod t_0`, with at most `phi(t_0)` anchors, and each anchor admits an exact complete-`D` second moment of size at most `pH`.

The live question therefore moves one level deeper. The staged branch must determine whether the actual residual-divisor weights populate enough reciprocal shifts per anchor to cross the `p/H` fibre threshold, and whether the aligned unexpanded amplitude can be carried through the same dispersion step without destroying that gain. If not, the new reciprocal source coordinate is structurally real but quantitatively too sparse; if yes, this is the first place in the branch where internal factorization can reduce the source-frame tariff before product collapse.