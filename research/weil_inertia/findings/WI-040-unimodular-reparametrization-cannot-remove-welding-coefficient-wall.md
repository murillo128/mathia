# WI-040 — unimodular reparameterization cannot remove the Yang welding coefficient wall

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE`. WI-039 showed that the natural affine-linear system in the Yang--Yang one-sided fourth-moment welding layer has reduced dilation coefficients `r,q` that are power-sized on positive, indeed asymptotically dominant, Mertens mass, while the currently published higher-uniformity transference theorems require fixed or at most polylogarithmically growing coefficient complexity. A natural escape is to ask whether the large coefficients are only a bad choice of integer coordinates.

They are not. For the exact four-form system

\[
 m,\qquad m-rk,\qquad n,\qquad n-qk,
\tag{1}
\]

**every lattice-preserving affine change of the three summation variables leaves coefficient norm at least `max(r,q)/2`.** Equivalently, the arithmetic contents `r` and `q` of the two within-pair coefficient differences are invariants of the integer lattice. Thus no unimodular reparameterization can turn the power-sized Yang system into a fixed- or polylog-coefficient system to which MRSTT 2026 Lemma 8.4 or Bienvenu's higher-dimensional Siegel--Walfisz theorem can simply be applied.

This does not rule out an anisotropic theorem, a decomposition into large-index sublattices with genuinely new uniformity, or a source-specific dispersion argument. It rules out the cheaper workaround in which one hopes to remove `r,q` by a clever integral coordinate normalization alone.

## 1. Exact source system and published coefficient interface

The source-side identity is the one audited in WI-039 from

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`, especially `scripts/t2_swaps.py` and the one-sided fourth-moment section of `paper.tex`.

With

\[
g=(b_1,b_2),\qquad r=\frac{b_1}{g},\qquad q=\frac{b_2}{g},
\tag{2}
\]

the equal-lock relation gives

\[
m'=m-rk,\qquad n'=n-qk,
\tag{3}
\]

so the four von Mangoldt factors are evaluated at the forms in (1). The remaining lock/window conditions define a convex strip and block cutoffs; they do not alter the coefficient vectors of the prime arguments.

The recent primary transference input is Kaisa Matomäki, Maksym Radziwiłł, Xuancheng Shao, Terence Tao and Joni Teräväinen, **Higher uniformity of arithmetic functions in short intervals II. Almost all intervals**, *Inventiones mathematicae* 244 (2026), 967--1091, DOI `10.1007/s00222-026-01408-6`. Their Lemma 8.4 fixes `s,d,t,L`, assumes every linear coefficient of every affine form is bounded by `L`, and only then takes the asymptotic scale to infinity. Their Theorem 1.5 correspondingly permits replacement of `0,1,...,ell-1` by other **fixed** distinct integer coefficients.

Pierre-Yves Bienvenu, **A higher-dimensional Siegel--Walfisz theorem**, *Acta Arithmetica* 179 (2017), 79--100, DOI `10.4064/aa8600-10-2016`, enlarges this to coefficients of polylogarithmic size, but not to positive powers of the main scale. WI-039 proved that fixed/polylog reduced coefficients occupy only `o(1)` of the normalized Yang two-base Mertens mass.

The only question addressed here is whether an automorphism of the integer summation lattice can shrink those coefficients before invoking such a theorem.

## 2. Coefficient-difference contents are invariant under `GL_3(Z)`

Write the summation vector as

\[
z=(m,n,k)^T
\]

and the linear coefficient rows of (1) as

\[
a_1=(1,0,0),\qquad
 a_2=(1,0,-r),\qquad
 a_3=(0,1,0),\qquad
 a_4=(0,1,-q).
\tag{4}
\]

Consider the most general lattice-preserving affine reparameterization

\[
z=Uz'+c,
\qquad
U\in GL_3(\mathbb Z),
\qquad
c\in\mathbb Z^3.
\tag{5}
\]

Translations only alter constant terms. The transformed linear rows are

\[
a_i'=a_iU.
\tag{6}
\]

Set

\[
u=e_3^TU,
\tag{7}
\]

the third row of `U`. Since `det U=+-1`, `u` is a primitive integer vector:

\[
\gcd(u_1,u_2,u_3)=1.
\tag{8}
\]

Indeed, if a common integer `d>1` divided the entire third row, it would divide the determinant. Therefore `||u||_infinity>=1`.

Now subtract the transformed forms pairwise. Equations (4)--(7) give exactly

\[
 a_2'-a_1'=-r u,
\qquad
 a_4'-a_3'=-q u.
\tag{9}
\]

Consequently

\[
\boxed{
\gcd_j (a_{2,j}'-a_{1,j}')=r,
\qquad
\gcd_j (a_{4,j}'-a_{3,j}')=q.
}
\tag{10}
\]

These are the one-row Smith/content invariants of the two coefficient differences. No integral automorphism of the domain can change them.

This is stronger than saying that a particular parameterization happens to display large entries: the divisibilities `r` and `q` survive every lattice basis.

## 3. Quantitative lower bound on every transformed coefficient norm

Let

\[
L(U)=\max_{1\le i\le4}\|a_iU\|_\infty
\tag{11}
\]

be the largest modulus of a linear coefficient after the change of variables. From (9),

\[
r\|u\|_\infty
=\|a_2'-a_1'\|_\infty
\le \|a_2'\|_\infty+\|a_1'\|_\infty
\le2L(U),
\tag{12}
\]

and identically

\[
q\|u\|_\infty\le2L(U).
\tag{13}
\]

Using `||u||_infinity>=1`,

\[
\boxed{
L(U)\ge\frac12\max(r,q)
\qquad
\text{for every }U\in GL_3(\mathbb Z).
}
\tag{14}
\]

Thus a power-sized `r` or `q` remains power-sized, up to the irrelevant factor two, in **every** integer coordinate system that bijects `Z^3` with itself.

The factor `1/2` is not an artifact needed for the conclusion. For a single pair one can center the two coefficient rows around zero by a unimodular shear and make their largest entries about `r/2`, so the simple triangle-inequality constant is of the correct order. What is impossible is changing polynomial coefficient growth into `O(1)` or `(log X)^C` growth.

## 4. Why non-unimodular scaling is not a free escape

One can of course write, for example, `h=rk`, after which the first pair becomes `m,m-h`. But this is not an automorphism of the original integer lattice: `h` is restricted to the sublattice `r Z`, and the second pair becomes

\[
n,\qquad n-\frac qr h,
\tag{15}
\]

which is not an integer-affine system on unrestricted `h`. Because `(r,q)=1`, choosing instead a common scaled shift does not simultaneously make both pairs fixed-coefficient integer forms on the full lattice; the lost arithmetic reappears as a divisibility/congruence restriction of growing modulus.

That observation is not a theorem that all non-unimodular decompositions must fail. A proof may exploit the resulting sparse sublattice, average over its cosets, or develop estimates whose constants are uniform in its index. But such a proof would be **new coefficient/modulus uniformity**, not a coordinate rewrite that brings the problem under the hypotheses already audited in WI-039.

This distinction matters for the proposed anisotropic repair. The matched physical relations

\[
rK\asymp M_m,
\qquad
qK\asymp M_n
\tag{16}
\]

may still permit an estimate whose true complexity is controlled by physical lengths rather than the raw integer coefficients. Equation (14) says only that this cancellation cannot be manufactured by an ordinary `GL_3(Z)` normalization before applying a fixed-`L` theorem.

## 5. Adversarial checks

Several apparent loopholes do not affect (14).

First, affine translations can make the constant terms large or small but leave all four linear rows, hence (9), unchanged. Second, swapping the roles of `m,n,k`, applying shears, or replacing `(m,n,k)` by any other integral basis is already contained in `GL_3(Z)`. Third, using the inverse convention `z'=Uz+c` changes the rows by `U^{-1}` instead of `U`, but `U^{-1}` is again unimodular and the same proof applies.

The argument does **not** permit arbitrary linear combinations of the four output forms. Such row operations would change the arguments on which `Lambda` is evaluated and therefore change the prime-pattern problem itself. Smith reduction of the combined four-row matrix is not a legal way to replace the four prime arguments by different linear combinations.

Finally, the result is deliberately narrower than a no-go for all transference. It does not contradict WI-038's denominator contraction on major arcs: there a dilation acts on a rational phase and genuinely reduces its denominator. Here the invariant belongs to the integer coefficient differences of the prime forms themselves.

## 6. Prior-art and novelty assessment

The lattice fact used in (8)--(10) is classical: unimodular integer transformations preserve the content (gcd of coordinates) of an integer row vector, equivalently the first Smith invariant of a one-row matrix. No novelty is claimed for this algebra.

The literature-backed analytic boundary is the fixed-`L` generalized von Neumann theorem in MRSTT 2026 and Bienvenu's polylogarithmic-coefficient extension. The source-backed input is the exact Yang swap producing (1)--(3). WI-039 supplies the separate Mertens-mass theorem showing that the large-`r,q` regime is not negligible.

The new exact deduction recorded here is the combination of those ingredients: **the coefficient wall identified in WI-039 is invariant under every lattice-preserving reparameterization of the actual Yang summation variables.** A targeted prior-art search located the classical Smith-normal-form invariant and the existing coefficient-uniform prime-pattern literature, but no source that states this Yang-specific obstruction. That absence is not a priority claim.

## 7. Decisive audit tests

This finding should be rejected or narrowed if any of the following fails.

1. Reconstruct (3) from the equal-lock identity `b1(n-n')=b2(m-m')` and verify that `r=b1/g`, `q=b2/g` are the exact reduced coefficients used by the source.
2. For an arbitrary symbolic `U in GL_3(Z)`, verify (9) directly from the coefficient rows (4).
3. Verify that the third row of a unimodular matrix is primitive; equivalently, a common divisor of that row divides `det U`.
4. Check the norm inequality (12)--(14), including the factor two.
5. Do not extend the conclusion from lattice automorphisms to arbitrary sublattice decompositions; those remain a possible route only if their growing index/modulus is controlled analytically.
6. Keep any physical-scale/anisotropic cancellation conjectural until an estimate is proved whose constants are uniform in the actual power-sized `r,q` family.

## 8. Consequence for `weil_inertia`

A cheap repair of WI-039 is now closed. The dominant Yang welding cells cannot be converted to fixed/polylog coefficient complexity merely by choosing better integer coordinates:

\[
\boxed{
\inf_{U\in GL_3(\mathbb Z)} L(U)
\ge \tfrac12\max(r,q).
}
\tag{17}
\]

Combined with WI-039's Mertens-mass calculation, this means that the missing welding step genuinely needs one of the harder ingredients already isolated there: coefficient-uniform or anisotropic transference, a controlled large-index sublattice decomposition, or a source-specific dispersion/maximal estimate. The matched physical scale remains a plausible place to search, but **ordinary reparameterization cannot remove the arithmetic difficulty**.