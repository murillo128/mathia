# MC-471 — Empty-vector base is a two-sided sifted translated-ratio sum

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `FRONTIER-ADVANCE` · `NEGATIVE/OBSTRUCTION` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The empty-vector component isolated in `MC-469` and identified in `MC-470` has an exact representation that removes an apparent degree of freedom from the staged source geometry.

Let `p` be prime, let `chi` be a nonprincipal character modulo `p`, and let

\[
B(y):=B_{\lambda^{(0)}}(y)\ge 0
\]

be the upper-sieve residual from `MC-470`. In the empty-vector cell the two outer factors are

\[
r=r'=1.
\]

Therefore the corresponding shifted quadratic correlation is exactly

\[
\boxed{
C_h^{(0)}(I)
=
\sum_{n\in I}
K_h(n)\,B(n+h)B(n),
}
\tag{1}
\]

where

\[
K_h(n):=\chi(n+h)\overline{\chi(n)}.
\tag{2}
\]

On the nonzero character support, when `h not\equiv0 (mod p)`, this is the fixed rational-character phase

\[
\boxed{
K_h(n)=\chi\!\left(\frac{n+h}{n}\right).
}
\tag{3}
\]

The one-sided staging of `MC-460` does not create an additional phase variable in this base cell. If a residual divisor `s|n+h` is exposed and

\[
n+h=sj,
\]

then the staged phase is

\[
\chi(j)\overline{\chi(j-hs^{-1})}.
\tag{4}
\]

Because a contributing `s` is invertible modulo `p`, multiplication by the constant character factors gives

\[
\chi(j)\overline{\chi(j-hs^{-1})}
=
\chi(sj)\overline{\chi(sj-h)}
=
K_h(n).
\tag{5}
\]

Thus the reciprocal-looking source shift `D_s=h/s (mod p)` is an exact reparametrization of the same fixed translated-ratio phase once `n+h=sj` is restored. In this empty-vector component, treating the residual divisor `s` and the resulting `(U,D,C)` coordinates as an independent source-phase resource would be representation inflation.

There is a second sharpening from `MC-470`. Write

\[
R_z(y):=\mathbf 1_{(y,P(z))=1},
\qquad
E(y):=B(y)-R_z(y)\ge0.
\tag{6}

Then `(1)` splits exactly into four arithmetic channels,

\[
\boxed{
B(n+h)B(n)
=
R_z(n+h)R_z(n)
+R_z(n+h)E(n)
+E(n+h)R_z(n)
+E(n+h)E(n).
}
\tag{7}

The leading rough channel is therefore

\[
\boxed{
C_{RR}(h;I)
=
\sum_{n\in I}
K_h(n)
\mathbf 1_{(n(n+h),P(z))=1}.
}
\tag{8}

For each small prime `q<z`, the local sieve condition in `(8)` excludes the two residue classes

\[
n\equiv0,-h\pmod q
\tag{9}

when `q\nmid h`, and these two classes coalesce when `q|h`. Hence the base problem is not a generic positive residual on an arbitrary affine trajectory: its main piece is a **two-sided shifted sifted sum of the fixed translated-ratio character phase**.

This representation change is analytically consequential because established shifted-character-sum literature already controls either one-sided rough factor in the long prime-conductor range. Gong, Jia and Korolev prove that for any `1`-bounded multiplicative function `f`, prime `p`, nonprincipal character `chi (mod p)`, fixed nonzero shift `a (mod p)`, and

\[
p^{1/2+\varepsilon}\ll N\ll p^A,
\]

one has

\[
\sum_{n\le N}f(n)\chi(n+a)
\ll
N\frac{\log\log p}{\log p}.
\tag{10}

Take

\[
f_z(n):=R_z(n)\overline{\chi(n)}.
\tag{11}

Both factors are multiplicative and `|f_z(n)|\le1`, so `(10)` gives directly

\[
\boxed{
\sum_{n\le N}R_z(n)K_h(n)
\ll
N\frac{\log\log p}{\log p}
}
\tag{12}

for `h not\equiv0 (mod p)` in that range. After the change of variable `m=n+h`, the symmetric one-sided term with `R_z(n+h)` has the same form, with multiplicative coefficient `R_z(m)\chi(m)` and the shifted conjugate character.

Therefore the raw rational phase `K_h`, and even its interaction with **one** roughness condition, are not the missing long-range mechanism. The live base problem begins where multiplicativity is genuinely broken by simultaneous translated constraints: the joint two-sided rough factor in `(8)` and the positive first-exit boundary terms involving `E` in `(7)`.

The Gong--Jia--Korolev theorem provides only a logarithmic saving and only above the square-root conductor scale. It does not give the conductor-power saving required by the current source-depth budget, does not estimate `(8)`, and does not control the boundary channels in `(7)`. No improved bound for `M(x)`, no zero-free region, and no RH consequence follows.

## 1. Exact collapse of the staged base coordinates

Specialize the normalized variables of `MC-463` to the empty-vector outer cell. With

\[
r=r'=1
\]

one has

\[
g=r_1=r_2=G=T=1,
\qquad
H_0=h.
\tag{13}

The congruence defining the anchor representative becomes trivial, so

\[
\ell_s=0,
\qquad
U_s=0,
\qquad
D_s\equiv h s^{-1}\pmod p,
\qquad
C_s=-h.
\tag{14}

The staged residual trajectory is consequently

\[
y=C_s+s j=sj-h=n,
\tag{15}

while the expanded first residual condition is `n+h=sj`. Substitution into the character phase proves `(5)`.

This matters because `MC-460`--`MC-463` correctly found a factor-specific source coordinate in the general staged family, but the empty-vector cell later isolated by `MC-469` is a degenerate outer geometry. In that cell the factor-specific coordinate is not new source information. It is the divisor parametrization of the fixed pair `(n,n+h)`.

The staging can still be useful analytically if it exposes a bilinear or sieve structure that is unavailable in the recombined `n` representation. What is ruled out is crediting the coordinate `D_s=h/s` itself as an additional independent oscillatory resource.

## 2. The positive residual separates into roughness and boundary correction

`MC-470` proves

\[
B(y)=R_z(y)+E(y),
\qquad E(y)\ge0,
\tag{16}

where `E` is supported on non-rough values whose small-prime kernel reaches an odd first-exit boundary of the Rosser--Iwaniec upper support. In particular, the internal Möbius signs of the upper-sieve coefficients have already recombined into a nonnegative integer count.

Substituting `(16)` twice gives `(7)` without loss. This is the most faithful base representation for deciding what information remains:

- `R_z(n)R_z(n+h)` retains simultaneous shifted roughness;
- `R_z(n+h)E(n)` and `E(n+h)R_z(n)` retain one rough leg and one positive boundary leg;
- `E(n+h)E(n)` is the joint first-exit boundary channel.

None of these terms contains sign cancellation internal to the sieve amplitude. Any cancellation must come from `K_h`, from an outer signed decomposition retained before this base cell was isolated, or from interference between signed finite components before positive closure.

For the rough channel, the local residue pattern `(9)` is exact. If `q\nmid h`, exactly two classes modulo `q` are forbidden; if `q|h`, only one is forbidden. Thus any sieve estimate for `(8)` must keep the `q|h` degeneracies instead of replacing the shifted pair by two independent roughness events.

## 3. One-sided roughness is already classical in the long range

Gong--Jia--Korolev's theorem applies to arbitrary multiplicative coefficients bounded by one. The coefficient `(11)` is multiplicative because

\[
R_z(n)=\prod_{q<z}\mathbf 1_{q\nmid n}
\]

is completely multiplicative as a `0/1` function and the Dirichlet character is completely multiplicative after the usual zero extension.

Therefore `(12)` is a direct theorem application, not a new character-sum estimate. The same argument after `m=n+h` controls

\[
\sum_{n\le N}R_z(n+h)K_h(n)
\]

up to the harmless change of interval endpoints caused by the translation.

The theorem cannot be applied directly to `(8)`: as a function of `n`, the coefficient

\[
R_z(n)R_z(n+h)\overline{\chi(n)}
\]

is not multiplicative because of the translated factor `R_z(n+h)`. This is exactly the first point at which the established multiplicative-coefficient theorem stops matching the base component.

This identifies a cleaner prior-art boundary than the staged formulation alone. The hard object is not "a character sum with a rough coefficient"; it is a translated rational-character sum with a **pair-sieve coefficient** coupling `n` and `n+h`.

## 4. Prior art and novelty boundary

K. Gong, C. Jia and M. A. Korolev, *Shifted Character Sums with Multiplicative Coefficients, II*, Journal of Number Theory 178 (2017), 31--39, DOI `10.1016/j.jnt.2017.02.006`, arXiv `1611.06577`, proves `(10)` in the stated prime-conductor long range and also treats products of finitely many shifted character factors. No novelty is claimed for that estimate.

The fixed rational phase `(3)` is likewise classical finite-field character-sum territory. `MC-S55` already anchors Weil/Stepanov estimates for complete mixed rational character sums, and `MC-448` uses the bounded-complexity phase `(x+a)/x` explicitly. No novelty is claimed for viewing `K_h` as a rational multiplicative-character trace.

Classical upper-sieve positivity and first-exit combinatorics are already audited in `MC-470`. The exact local two-residue pattern of `(8)` is the elementary dimension-two shifted-sieve pattern and is not claimed as new sieve theory.

The Mathia-specific delta is the **intersection of these already-known structures with the exact empty-vector cell**: after recombination, the reciprocal staged source coordinate disappears as an independent resource, one-sided roughness falls inside a known shifted-character theorem, and the unresolved base object is sharpened to the joint two-sided rough/boundary coupling `(7)`--`(8)`.

## Boundaries and falsification tests

- **Nonzero shift is essential.** If `h\equiv0 (mod p)`, then `K_h(n)=|\chi(n)|^2` on the character support and there is no translated-character cancellation. The Gong--Jia--Korolev theorem also requires a nonzero shift modulo `p`.
- **Prime conductor is used in the quoted theorem.** The current line also has smooth/composite-conductor machinery (`MC-S46`), but no transfer from that machinery to the exact two-sided sieve product is asserted here.
- **The one-sided theorem gives only logarithmic saving.** It cannot by itself pay a fixed positive conductor power in the `MC-415`/`MC-448` source budget.
- **The range begins above `p^{1/2+epsilon}`.** Nothing here closes the shorter source intervals that are important elsewhere in the staged analysis.
- **The two-sided rough product is not multiplicative.** Applying `(10)` to `(8)` by pretending otherwise would erase the load-bearing translated sieve constraint.
- **The boundary correction is real.** `E` is nonnegative but can have multiplicity greater than one; it cannot be dropped, replaced by a density heuristic, or inferred to be sparse solely from the rank gate of `MC-470`.
- **Staging is not forbidden.** A divisor staging that genuinely produces a bilinear estimate, preserves cross-component signs, or resolves the joint pair-sieve condition remains admissible. What is forbidden is counting the staged divisor coordinate as independent source-phase occupancy when `(5)` shows that it is only a reparametrization in this cell.
- **No full-base estimate is asserted.** Equations `(1)`--`(8)` are exact reductions and `(12)` is only a one-sided prior-art theorem application.

## Consequence for the research line

The accepted staged-sieve clue should be narrowed again. For the unavoidable empty-vector component, the next base calculation should start from `(1)` and `(7)`, not from an abstract four-parameter source frame.

The decisive arithmetic target is now:

\[
\sum_n
\chi\!\left(\frac{n+h}{n}\right)
R_z(n)R_z(n+h)
\tag{17}

and the three analogous terms in which one or both rough indicators are replaced by the positive first-exit boundary correction `E`.

A useful positive result must obtain a strict conductor-power gain for this **joint** shifted sieve/character interaction after the existing endpoint, Fejér, normalization and source-depth costs are charged. A useful negative result may instead prove that this pair-sieve family still obeys the same source tariff. Reapplying generic one-sided multiplicative-coefficient character sums, or treating `D_s=h/s` as new source occupancy, no longer advances the branch.

Nonempty rough-block components and pre-positive cross-component interference remain separate live channels. The present result narrows only the unavoidable empty-vector base.