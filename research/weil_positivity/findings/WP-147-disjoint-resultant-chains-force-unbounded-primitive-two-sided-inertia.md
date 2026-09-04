# WP-147 — Disjoint resultant chains force unbounded primitive two-sided inertia

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PRIME-CIRCLE + CYCLOTOMIC-RESULTANT + CRITICAL-HALF-DENSITY + UNBOUNDED-PRIMITIVE-INERTIA + BOUNDED-CODIMENSION-OBSTRUCTION + FINITE-RANK-SCHUR-OBSTRUCTION + MATCHED-BLOCKWISE-EQUAL-WEIGHT-CONTROL + PRIOR-ART-AUDITED` for attempts to repair the zero-order Prime-Circle resultant kernel of `WP-146` by a fixed number of global constraints or a fixed finite-dimensional auxiliary/archimedean sector.

`WP-146` exhibited one exact mixed-prime three-chain on which the normalized cyclotomic log-resultant kernel is indefinite after ordinary centering. That finite witness left a natural escape: perhaps a small global/cohomological constraint, or a finite-dimensional real-place sector coupled before the sign theorem, could remove the offending directions.

That escape does not survive arithmetic replication. The same bad three-chain occurs **exactly and with identical weights** on infinitely many mutually resultant-orthogonal triples of Prime-Circle shells. Consequently the centered zero-order resultant kernel has positive and negative primitive indices that are both unbounded. Any fixed bounded-codimension restriction and any fixed-rank Hermitian correction leave both signs once enough disjoint triples are included. In particular, eliminating a fixed finite-dimensional auxiliary sector by Schur complement cannot restore conditional positive or negative definiteness.

This strengthens `WP-146` without changing its boundary in the genuinely global directions: an infinite-dimensional/noncompact auxiliary sector, an unbounded-codimension global constraint, or a nonseparable full-rank modification of the finite resultant block before the sign theorem remains open.

## 1. Replicate the exact `6 -> 12 -> 36` witness without changing its weights

Recall the normalized zero-order resultant kernel from `WP-146`, for distinct `m,n>1`,

\[
J_{m,n}
=
\frac{\log|\operatorname{Res}(\Phi_m,\Phi_n)|}
{\sqrt{\varphi(m)\varphi(n)}},
\qquad J_{m,m}=0.
\tag{1}
\]

For an interior prime-power step `n=mp^k` with `p\mid m`, Apostol's cyclotomic-resultant formula and `\varphi(mp^k)=p^k\varphi(m)` give

\[
J_{m,mp^k}=\frac{\log p}{p^{k/2}}.
\tag{2}
\]

Choose any prime

\[
r>3
\]

and define the exact-order triple

\[
F_r=\{6r,12r,36r\}.
\tag{3}
\]

The first ratio is `2`, the second is `3`, and both are interior because `2\mid6r` and `3\mid12r`. The endpoint ratio is `6`, not a prime power. Hence the restriction of `J` to every `F_r` is **the same matrix**

\[
\boxed{
J_{F_r}=R_{x,y}
=
\begin{pmatrix}
0&x&0\\
x&0&y\\
0&y&0
\end{pmatrix},
}
\tag{4}
\]

with

\[
x=\frac{\log2}{\sqrt2},
\qquad
y=\frac{\log3}{\sqrt3},
\qquad y>x>0.
\tag{5}
\]

The spectator prime `r` changes the shell orders but cancels from the normalized adjacent interactions. Thus (4) is not an asymptotic clone or a rescaled model: it is an exact repeated Prime-Circle resultant block.

## 2. Distinct spectator primes make the copies exactly orthogonal for the resultant kernel

Let `r` and `s` be distinct primes larger than `3`. Every element of `F_r` has the form `ar` and every element of `F_s` has the form `bs`, where

\[
a,b\in\{6,12,36\}.
\]

Neither `ar` divides `bs` nor `bs` divides `ar`. Indeed, if `ar\mid bs`, then the prime `r` would divide `bs`; but `r` divides neither `b` (whose prime factors are only `2,3`) nor the distinct prime `s`. The reverse direction is identical.

For indices greater than one, Apostol's theorem therefore gives

\[
|\operatorname{Res}(\Phi_{ar},\Phi_{bs})|=1,
\]

and hence

\[
\boxed{J_{ar,bs}=0.}
\tag{6}
\]

So if `r_1,\ldots,r_M` are distinct primes greater than `3` and

\[
F_M=\bigcup_{j=1}^M F_{r_j},
\tag{7}
\]

then `J_{F_M}` is an exact block diagonal direct sum of `M` copies of `R_{x,y}`.

This exact decoupling is the key amplification step. It uses only cyclotomic-resultant support; no fitted localization, zero data, cutoff-dependent regularization, or hand-picked cancellation is introduced.

## 3. Every block contributes one positive and one negative primitive direction

Let

\[
U_r=\left\{a\in\mathbb R^{F_r}:\sum_{m\in F_r}a_m=0\right\}.
\tag{8}
\]

In the basis

\[
u=(1,-1,0),
\qquad v=(0,1,-1),
\]

the restriction of the quadratic form of (4) to `U_r` has matrix

\[
\boxed{
H_{x,y}
=
\begin{pmatrix}
-2x&x+y\\
x+y&-2y
\end{pmatrix}.
}
\tag{9}
\]

Its determinant is

\[
\det H_{x,y}
=4xy-(x+y)^2
=-(x-y)^2<0.
\tag{10}
\]

Therefore

\[
\boxed{
\operatorname{inertia}(J_{F_r}|_{U_r})=(1,1,0),
}
\tag{11}
\]

where the first two entries denote positive and negative index. This is the coordinate-free content of the two explicit opposite-sign witnesses in `WP-146`.

Now set

\[
U_M=\bigoplus_{j=1}^M U_{r_j}.
\tag{12}
\]

Every vector in `U_M` has total coordinate sum zero, so

\[
U_M\subset\mathbf1^\perp.
\tag{13}
\]

By the cross-block vanishing (6), the restriction of the quadratic form to `U_M` is the direct sum of the `M` forms in (9). Hence it has exactly `M` positive and `M` negative directions. In particular, on the full centered space,

\[
\boxed{
 n_+\!\left(J_{F_M}|_{\mathbf1^\perp}\right)\ge M,
 \qquad
 n_-\!\left(J_{F_M}|_{\mathbf1^\perp}\right)\ge M.
}
\tag{14}
\]

Thus both primitive inertia indices are unbounded along an explicit arithmetic exhaustion.

## 4. A fixed number of global linear constraints cannot select a sign

Suppose a proposed global/cohomological primitive condition imposes at most `c` additional linear constraints on the ordinary mean-zero space, with `c` independent of the arithmetic cutoff. Let

\[
W_M\subset\mathbf1^\perp,
\qquad
\operatorname{codim}_{\mathbf1^\perp}W_M\le c.
\tag{15}
\]

Inside `U_M`, let `V_M^+` and `V_M^-` be the `M`-dimensional positive and negative subspaces supplied by the direct-sum decomposition above. Elementary dimension counting gives

\[
\dim(V_M^\pm\cap W_M)\ge M-c.
\tag{16}
\]

For `M>c`, both intersections are nonzero. Therefore

\[
\boxed{
J_{F_M}|_{W_M}\text{ is still indefinite for every fixed }c.
}
\tag{17}
\]

So the escape left open in `WP-146` cannot be merely one new degree condition, one pole constraint, or any fixed finite list of globally coupled linear constraints. A sign-selecting admissible space would need codimension growing without bound, or a genuinely different finite block.

## 5. Fixed-rank corrections and finite-dimensional Schur complements also fail

The same direct-sum construction is stable against arbitrary signed finite-rank corrections. Let `R_M=R_M^*` have

\[
\operatorname{rank}R_M\le d
\tag{18}
\]

with `d` independent of `M`. Since `\ker R_M` has codimension at most `d`,

\[
\dim(V_M^\pm\cap W_M\cap\ker R_M)
\ge M-c-d.
\tag{19}
\]

For `M>c+d`, choose nonzero vectors in each intersection. On them `R_M` vanishes exactly, so the corrected form retains one strictly positive and one strictly negative value. Hence

\[
\boxed{
(J_{F_M}+R_M)|_{W_M}
\text{ is neither positive nor negative semidefinite}
}
\tag{20}
\]

for all sufficiently large `M`.

Now let a fixed `d`-dimensional auxiliary/archimedean sector be coupled to the finite resultant coordinates through a Hermitian block form

\[
\mathcal Q_M=
\begin{pmatrix}
J_{F_M}&B_M\\
B_M^*&A_M
\end{pmatrix}.
\tag{21}
\]

If the finite block is retained as a principal restriction, finite-only vectors `(v,0)` already give (17) after any fixed number of admissibility constraints. If instead the auxiliary variables are eliminated through an invertible Schur complement, the effective finite block is

\[
J_{F_M}-B_MA_M^{-1}B_M^*,
\tag{22}
\]

and the correction has rank at most `d`. Equation (20) therefore applies. The same rank bound holds for the corresponding generalized-inverse response whenever such a reduced Hermitian form is well-defined.

Thus a **fixed finite-dimensional** real-place, pole, boundary, or cohomological sector cannot repair the current zero-order resultant kernel merely by finite-rank feedback.

## 6. Additive centering gauges remain irrelevant; arbitrary diagonal completion is not covered

As already noted in `WP-146`, every row-plus-column gauge

\[
G_{mn}=u_m+u_n
\tag{23}
\]

vanishes quadratically on `\mathbf1^\perp`. It therefore vanishes on the whole amplified witness `U_M` and cannot alter any inertia statement above.

This finding deliberately does **not** extend that conclusion to arbitrary diagonal corrections `d_m\delta_{mn}` or other full-rank modifications. Such terms act nontrivially on every block and can change (9); the sparse positive-completion problem for critical arithmetic data is a different route, already constrained elsewhere in this line by `WP-096`--`WP-107`. Nor does (20) cover corrections whose rank grows with the number of arithmetic shells.

## 7. Matched control: equal edge weights remove the replicated blockwise positive directions

The amplification in Section 3 is not caused merely by taking many disconnected three-node paths. Replace the arithmetic weights **within each copy** by a homogeneous control `x=y=w>0`. On the same blockwise mean-zero space `U_r`, equation (9) then has determinant zero and `WP-146` gives

\[
a^TR_{w,w}a=-2w t^2\le0
\qquad(a\in U_r).
\tag{24}
\]

Therefore on the exact comparison subspace used in the amplification proof,

\[
\boxed{
\left(\bigoplus_{j=1}^M R_{w,w}\right)\bigg|_{U_M}\preceq0,
\qquad
n_+\!\left(\left.\bigoplus_{j=1}^M R_{w,w}\right|_{U_M}\right)=0.
}
\tag{25}
\]

Restoring the unequal arithmetic labels `\log2/\sqrt2` and `\log3/\sqrt3` changes each block from seminegative on `U_r` to inertia `(1,1,0)`, producing the `M` independent positive directions used in (14). Thus the replicated positive-index lower bound is genuinely tied to the mixed-prime amplitude mismatch rather than block count alone.

This control is deliberately **blockwise**, not a claim that a disconnected equal-weight kernel is CND on the entire global space `\mathbf1^\perp`. A globally mean-zero vector may have nonzero sum inside individual blocks, and zero cross-block coupling then leaves additional directions that are not tested by (24). The matched statement needed here is only that, on the same `U_M` which certifies (14), equalizing the arithmetic labels removes all of the replicated positive directions.

## 8. Novelty audit and relation to earlier Mathia no-go results

The arithmetic support theorem is classical: T. M. Apostol, *Resultants of cyclotomic polynomials*, Proc. Amer. Math. Soc. **24** (1970), 457--462, determines the cyclotomic resultants used in (2) and (6). Conditional positive/negative type is classical Schoenberg theory. The dimension and rank-perturbation arguments in Sections 4--5 are elementary finite-dimensional inertia facts; no novelty is claimed for them.

A bounded literature audit using combinations of `cyclotomic resultant`, `conditionally negative definite`, `negative type`, `Schoenberg`, `inertia`, and `rank perturbation` did not locate a treatment of the normalized kernel (1) with the exact replicated family (3), nor the unbounded centered-inertia consequence (14). The novelty claim is therefore narrow and project-specific: **Apostol sparsity lets the `WP-146` arithmetic bad block be copied exactly and orthogonally, forcing unbounded two-sided primitive inertia for the Prime-Circle resultant candidate.**

This is not a duplicate of `WP-028`, which proved an infinite negative sector for the finite Weil translation comb and ruled out compact after-the-fact repairs of that different operator. It is also not a duplicate of `WP-035`, which found unbounded positive index in the Prime-Circle boundary-birth Kronecker-sum operator. The present object is the zero-order normalized cyclotomic-resultant kernel left alive by `WP-145`; the new conclusion is that the **conditional-sign failure of `WP-146` has unbounded multiplicity on the primitive space itself**, closing bounded-codimension and finite-rank repairs for this specific candidate.

## 9. Consequence for the Weil-positivity search

The zero-order resultant remains unusually close to the finite arithmetic target: unlike its positive Hessian, it retains exact prime-power support and the critical `\log p/p^{k/2}` amplitudes. But its failure of sign is now known to be extensive rather than local. There is no fixed finite collection of global modes whose removal or feedback converts it into a CPD/CND kernel.

The surviving category is therefore narrower:

\[
\boxed{
\text{exact zero-order resultant data}
\;\not\xrightarrow[\text{fixed finite global sector}]{\text{bounded constraints / finite-rank feedback}}
\;\text{Weil-type geometric positivity}.
}
\tag{26}
\]

A viable continuation must change category before the sign theorem: for example, an intrinsically infinite-dimensional archimedean/cohomological sector, an unbounded-codimension but independently forced global quotient, or a nonseparable full-rank finite--archimedean modification that changes the resultant block itself while preserving its prime-power selector. Such a mechanism would still need to generate the Gamma/polar terms canonically and prove positivity independently of RH or inserted zero data.

## Internal dependencies

- `research/weil_positivity/findings/WP-028-compact-corrections-cannot-remove-finite-prime-comb-negative-index.md`
- `research/weil_positivity/findings/WP-035-prime-circle-local-hodge-signature-does-not-globalize-across-primes.md`
- `research/weil_positivity/findings/WP-145-resultant-hessian-positivity-loses-prime-power-support-and-splits-real-place-curvature.md`
- `research/weil_positivity/findings/WP-146-critical-resultant-kernel-is-conditionally-indefinite-on-mixed-prime-three-chain.md`
