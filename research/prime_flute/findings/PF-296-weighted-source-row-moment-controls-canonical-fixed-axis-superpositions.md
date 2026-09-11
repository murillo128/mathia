# PF-296 — weighted source-row moment controls canonical fixed-axis superpositions

**Status:** `EXACT-DERIVED + UNIFORM-SYNTHESIS-BOUND + NEGATIVE/ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-294-fixed-axis-robin-source-is-uniformly-half-sobolev-for-bounded-seam-ratio|PF-294]] proves a uniform physical-axis `H^{1/2}` bound for every **fixed** normalized Robin source row when `r=w/s` remains bounded, and [[research/prime_flute/findings/PF-295-canonical-seam-ratios-close-the-fixed-axis-parameter-escape|PF-295]] shows that the canonical prime-flute tail lies in exactly that bounded-ratio regime. The remaining caveat in both findings is source-row proliferation: the constants were allowed to depend on the row index.

The proof of PF-294 contains more information than its fixed-row statement. Its conserved positive weight is

\[
q_i=\kappa_i^{1/2}c_i\asymp \kappa_i,
\]

and the argument gives an **explicit linear row bound**. Uniformly over the canonical tail,

\[
\boxed{
\|U^*y_{n,j}^{(i)}\|_{H^{1/2}(\mathbb R)}
\le C q_i,
}
\]

where `y_{n,j}^{(i)}` is the normalized fixed-axis source column on either canonical seam of the `n`th pant and `C` is independent of `n,j,i` after a finite head. By linearity and absolute convergence, the complete fixed-axis synthesis map is therefore uniformly bounded from the weighted source space

\[
\ell^1(q)=\left\{a:\sum_i q_i|a_i|<\infty\right\}
\]

to physical-axis `H^{1/2}`.

This turns the vague possibility “the source-row population grows with the pant index” into a quantitative gate. A superposition of canonical fixed-axis columns cannot realize the [[research/prime_flute/findings/PF-292-fixed-physical-high-pass-forces-diverging-local-frequency-floor|PF-292]] frequency escape while its weighted first source moment `\sum_i q_i|a_i|` stays bounded. If the [[research/prime_flute/findings/PF-290-optimized-local-low-high-correlation-is-an-exact-high-band-shorting-deficit|PF-290]] local deficit has a positive limsup and the complete normalized response factors through these columns followed only by the already-controlled PF-255/PF-256 transports, then either that weighted source moment diverges or there is a genuinely residual mixed/reassembly operator not covered by the fixed-axis synthesis.

This does **not** prove a bound for the complete mixed Riesz response. It isolates the precise source-population currency that must fail before source-row proliferation can remain a viable explanation.

## Claim

Work in one parity sector with PF-294 notation

\[
\varphi_i=e_{2i+\varepsilon},
\qquad
A\varphi_i=\kappa_i^2\varphi_i,
\qquad
q_i=\kappa_i^{1/2}c_i,
\qquad
q_i\asymp\kappa_i.
\tag{1}
\]

For `s,r>0`, let

\[
y_{s,r}^{(i)}:=B_{rs}^*\varphi_i
\tag{2}
\]

be PF-294's normalized fixed-axis source column. Then for every finite `r_*<\infty` there is `C_{r_*}<\infty`, independent of `s`, `r` and `i`, such that

\[
\boxed{
\|U^*y_{s,r}^{(i)}\|_{H^{1/2}(\mathbb R)}
\le C_{r_*}q_i,
\qquad s>0,\ 0<r\le r_*.
}
\tag{3}
\]

Consequently, for every finitely supported scalar sequence `a=(a_i)`,

\[
Y_{s,r}(a):=\sum_i a_i y_{s,r}^{(i)}
\tag{4}
\]

satisfies

\[
\boxed{
\|U^*Y_{s,r}(a)\|_{H^{1/2}(\mathbb R)}
\le C_{r_*}\sum_i q_i|a_i|.
}
\tag{5}
\]

Thus `Y_{s,r}` extends uniquely to a bounded synthesis operator

\[
\boxed{
Y_{s,r}:\ell^1(q)\longrightarrow H^{1/2}(\mathbb R),
\qquad
\sup_{s>0,\,0<r\le r_*}\|Y_{s,r}\|<\infty.
}
\tag{6}
\]

Now take the canonical PF-205/PF-230 pant tail. PF-295 gives one `r_*` and `N` such that both canonical ratios

\[
r_{n,j}=\frac{w_j}{s_n},
\qquad j\in\{n,n+1\},
\tag{7}
\]

lie in `(0,r_*]` for `n\ge N`. Hence, writing

\[
Y_{n,j}(a):=Y_{s_n,r_{n,j}}(a),
\tag{8}
\]

one has

\[
\boxed{
\sup_{n\ge N}\max_{j\in\{n,n+1\}}
\|U^*Y_{n,j}(a_n)\|_{H^{1/2}}
\le C\sup_n\|a_n\|_{\ell^1(q)}.
}
\tag{9}
\]

The same conclusion survives any of the PF-255/PF-256 geometric transports whose relevant positive Sobolev graph norm is already known to be uniformly bounded on the tail.

Finally, let `I` be the fixed PF-226/PF-227 physical window. For every fixed `0<\sigma<1/2`, localization/restriction from `H^{1/2}(\mathbb R)` to the Dirichlet fractional scale on `I` is bounded. Therefore any normalized response family of the form

\[
G_n=\mathcal T_nY_{n,j_n}(a_n)
\tag{10}
\]

with

\[
\sup_n\|a_n\|_{\ell^1(q)}<\infty
\tag{11}
\]

and `\mathcal T_n` uniformly bounded in the already-controlled positive Sobolev scale satisfies

\[
\boxed{
\sup_n\bigl(\|G_n\|_{L^2(I)}+\|K_D^\sigma G_n\|_{L^2(I)}\bigr)<\infty.
}
\tag{12}
\]

By PF-292, its PF-227 physical-high projection tends to zero. In particular, if such a factorization represents the complete PF-290 normalized mixed functional, then

\[
\boxed{\delta_{n,r}\to0.}
\tag{13}
\]

Equivalently, under that factorization a positive limsup of the PF-290 deficit forces

\[
\boxed{
\|a_n\|_{\ell^1(q)}=\sum_i q_i|a_{n,i}|\to\infty
}
\tag{14}
\]

along a subsequence, unless a residual operator outside the controlled synthesis/transport factorization is responsible for the escape.

## 1. PF-294 already gives a row-uniform bound after paying `q_i`

PF-294 uses PF-276's positivity and conserved moment

\[
\sum_j q_j\nu_{s,r,j}=q_i,
\qquad
q_j\ge c\kappa_j,
\tag{15}
\]

with a constant `c>0` independent of all source/seam parameters. Hence

\[
\sum_j\kappa_j\nu_{s,r,j}\le c^{-1}q_i.
\tag{16}
\]

For `z_{s,r}^{(i)}=A^{-1/4}\nu_{s,r}^{(i)}`, the square estimate in PF-294 gives

\[
\|A^{3/4}z_{s,r}^{(i)}\|_2
\le c^{-1}q_i.
\tag{17}
\]

PF-247's exact parity-banded compactification then transfers this to

\[
\|L^{3/4}z_{s,r}^{(i)}\|_2
\le C q_i
\tag{18}
\]

with one constant independent of `i,s,r`. Applying PF-294's finite-seam multiplier estimate at `\sigma=1/2`,

\[
\|L^{1/4}y_{s,r}^{(i)}\|_2^2
\le r\|L^{3/4}z_{s,r}^{(i)}\|_2^2,
\tag{19}
\]

proves (3) for `r\le r_*`. Since

\[
L=U(1-\partial_\tau^2)U^*,
\tag{20}
\]

this is precisely the physical-axis `H^{1/2}` norm.

The only new observation is that none of the constants used in (15)--(19) depends on the source row after the explicit factor `q_i` is retained. PF-294 stated the theorem row by row; its proof already contains the stronger weighted family estimate.

## 2. Absolute source synthesis preserves the positive Sobolev margin

For a finite source vector `a`, linearity of `B_{rs}^*` gives (4). The triangle inequality in `H^{1/2}` and (3) give

\[
\begin{aligned}
\|U^*Y_{s,r}(a)\|_{H^{1/2}}
&\le\sum_i|a_i|\,\|U^*y_{s,r}^{(i)}\|_{H^{1/2}}\\
&\le C_{r_*}\sum_iq_i|a_i|.
\end{aligned}
\tag{21}
\]

This proves (5). Completion of finitely supported sequences in the weighted `\ell^1(q)` norm gives (6); the image series converges absolutely in the Hilbert space `H^{1/2}`.

Because `q_i\asymp\kappa_i` and `\kappa_i` grows linearly with the parity-row index, the relevant currency is a **first spectral moment** of the source population. Merely using more rows is not itself a frequency-escape theorem. What must fail is a uniform bound on their `q`-weighted absolute mass, or else a later operator must destroy the regularity supplied by the synthesis map.

This distinction matters for cancellation. A divergent `\ell^1(q)` bound is only loss of this sufficient estimate; it does not imply that the resulting physical response is rough. Conversely, bounded `\ell^1(q)` is enough to close this entire source-superposition mechanism regardless of cancellation.

## 3. Canonical geometry removes the remaining seam parameter

PF-295 proves that on the actual PF-205 trimmed tail both seam/corridor ratios in (7) are uniformly bounded. Substituting those ratios into (6) gives (9) immediately.

The estimate is therefore uniform simultaneously in the two variables that were previously left vague: shrinking pant scale and source-row superposition. Seam shrinkage is harmless by PF-295, while source proliferation is harmless whenever its first spectral moment remains bounded.

PF-255/PF-256 may then be applied exactly in their persisted scope. They preserve positive graph/Sobolev regularity already present with tail-uniform bounds. They cannot convert a uniformly `\ell^1(q)`-controlled fixed-axis synthesis into the loss of every positive Sobolev norm required by PF-292.

## 4. Consequence for the accepted heavy-angle clue

PF-295 left four qualitatively different local escape routes: mixed/global Schur reassembly, neighboring-cell coupling, source-row proliferation, and support migration/end completion. The present finding sharpens the third.

Suppose the fixed-window part of the complete normalized response can be written as controlled geometry applied to a fixed-axis source synthesis, as in (10). Then PF-292 needs no detailed coefficient asymptotics: bounded `\ell^1(q)` source moment gives a uniform positive Sobolev bound and therefore kills the PF-290 local deficit.

Thus a source-row explanation for a persistent deficit must exhibit a quantitative failure such as

\[
\sum_iq_i|a_{n,i}|\to\infty.
\tag{22}
\]

If the complete response cannot be represented in the form (10), that failure is itself informative: the first missing factor is a genuinely mixed/reassembled operator and should be isolated directly rather than described as source-row proliferation.

The next useful calculation is therefore not merely to count source rows. It is to extract the source coefficient vector of the actual simultaneous one-cusp-pant Riesz response and estimate its `q`-weighted first moment **before** and **after** the unresolved Schur/reassembly step.

## Prior art and novelty audit

No new theorem about weighted sequence spaces, Sobolev spaces, Jacobi operators, or Robin boundary maps is claimed. Once the column estimate (3) is known, the extension from finite sums to `\ell^1(q)` is the elementary absolute-convergence/triangle-inequality synthesis principle for Banach-space-valued series. The fractional-regularity and compactification inputs are exactly the already-audited PF-294/PF-295 ingredients.

A structure-directed literature search for weighted `\ell^1` synthesis and Jacobi/Poisson-source Sobolev estimates returned only the expected general weighted-sequence and orthogonal-polynomial background, with no theorem matching this project-specific normalized Robin family. That is not used as a novelty claim. The mathematical delta here is internal and explicit: PF-294's conserved weight `q_i` is promoted from a hidden row-dependent constant to the quantitative source-population currency for the PF-292 escape test.

## Boundaries and falsification

1. **Sufficient source norm, not a characterization.** Bounded `\ell^1(q)` implies uniform positive Sobolev regularity; divergence of `\ell^1(q)` does not imply roughness or a positive shorting deficit.
2. **Fixed-axis synthesis only.** The theorem does not show that the complete PF-290 Riesz representative has the factorization (10). PF-279-type Schur reservoirs or neighboring-cell terms may create a different response operator.
3. **Absolute coefficients.** The estimate deliberately ignores cancellation. A response with large `\ell^1(q)` may still be regular because of cancellation, so (14) is only a necessary escape condition under the stated factorization.
4. **Canonical bounded ratio.** The tail-uniform form uses PF-295's canonical seam normalization. A different noncanonical normalization would need its own `r` control.
5. **Positive Sobolev margin only.** For the PF-292 application one may use any `0<\sigma<1/2`; no endpoint identification between global `H^{1/2}` and the Dirichlet fractional domain is load-bearing.
6. **Controlled transports only.** PF-255/PF-256 may be included because their persisted theorems preserve the relevant regularity uniformly. No such assertion is made for unresolved global Schur reassembly or end completion.
7. **No weak-trace conclusion.** Killing this local frequency-escape mechanism does not prove compactness of the full heavy angle, weak `\mathcal S_{1,\infty}`, scattering, determinants, a zeta-zero relation, the critical line, or RH.

A direct falsification of (3) would require an error in PF-294's conserved-moment proof or in retaining the explicit `q_i` dependence through its graph and multiplier estimates. A project-level counterexample to the route-narrowing consequence would instead identify a complete normalized response with bounded source `\ell^1(q)` moment and controlled transports but a persistent PF-290 deficit, contradicting PF-292.

## Consequence for the research line

The source-row loophole is now quantitative. **Growing row index or row count matters only insofar as it makes the `q_i\asymp\kappa_i` weighted source mass escape.** The next pass should extract that coefficient moment from the actual simultaneous one-cusp-pant response. If it is uniformly bounded, source-row proliferation joins canonical seam shrinkage on the closed list and the first possible rough factor moves to mixed/neighboring Schur reassembly or support migration. If it diverges, the divergence must then be tested against the exact PF-290 shorting deficit rather than treated as evidence of noncompactness by itself.