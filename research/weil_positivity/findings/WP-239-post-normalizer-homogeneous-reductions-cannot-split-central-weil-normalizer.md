# WP-239 — Post-normalizer homogeneous reductions cannot split the central Weil normalizer

**Status:** `EXACT-DERIVED + CENTRAL-SCALAR-HOMOGENEITY-NO-GO + MOVING-COMPRESSION + NONREDUCING-COMPRESSION + ZERO-SHIFT-SCHUR-REDUCTION + MATCHED-CONTROL + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-238` proves that a fixed reducing scattering-channel projection cannot separate the zero, finite-prime, archimedean, and polar pieces hidden inside the scalar global normalizer. It deliberately leaves two nearby escapes open: a moving spectral subbundle, and a non-reducing compression whose effective dynamics might acquire Schur/Feshbach self-energy terms.

There is an exact extension of the centrality obstruction to a substantial part of both escapes. Once the global intertwiner has already factored as

\[
M(s)=m(s)R(s),
\tag{1}
\]

with `m(s)` scalar, **every post-normalizer reduction that is homogeneous under scalar multiplication still carries the same scalar factor as a whole**. In particular, an arbitrary finite-rank moving compression, even when it is non-reducing, satisfies

\[
C(s)=V(s)^*M(s)U(s)=m(s)\,A(s),
\qquad
A(s):=V(s)^*R(s)U(s),
\tag{2}
\]

and a zero-shift Schur complement satisfies

\[
\operatorname{Schur}(mR)=m\,\operatorname{Schur}(R).
\tag{3}
\]

Thus moving-frame connection terms and non-reducing self-energies can change the **normalized-operator remainder**, but they do not by themselves split the prime/Gamma/polar constituents of `m'/m`. Any such split must enter through a genuinely non-homogeneous operation, an `m`-dependent choice of geometry that itself carries arithmetic analytic information, a matrix-valued normalizer, or a construction acting before the scalar normalizer has formed.

This is a narrower claim than saying that every moving/Feshbach construction fails. Shifted resolvents such as `M-zI`, Schur complements of the additive logarithmic generator `(m'/m)I+R^{-1}R'`, Cayley transforms, and other non-homogeneous operations are **not** covered by (3). The result instead closes the canonical idea that merely making the projection move, or merely eliminating non-reducing channels from `M` itself, automatically unlocks the analytic constituents that `WP-238` showed had already been scalarized.

## 1. Moving compression does not require a reducing subspace

Allow the source and target fibers of the intertwiner to be different. Let

\[
U(s):\mathbb C^r\longrightarrow H_{\rm in}(s),
\qquad
V(s):\mathbb C^r\longrightarrow H_{\rm out}(s)
\tag{4}
\]

be `C^1` isometric frames for any rank-`r` moving input and output subbundles. No reducing or invariance condition is imposed. Compress the already-formed global intertwiner by

\[
C(s):=V(s)^*M(s)U(s).
\tag{5}
\]

Because `m(s)` is central and scalar, (1) gives the exact pointwise identity

\[
\boxed{
C(s)=m(s)V(s)^*R(s)U(s)=m(s)A(s).
}
\tag{6}
\]

Suppose `C(s)` is square and invertible on a regular interval. Then

\[
\det C(s)=m(s)^r\det A(s),
\tag{7}
\]

so

\[
\boxed{
\frac{d}{ds}\log\det C(s)
=
r\frac{m'(s)}{m(s)}
+
\frac{d}{ds}\log\det A(s).
}
\tag{8}
\]

All dependence on `U'(s)` and `V'(s)`—the possible Berry/Grassmannian connection terms anticipated in `WP-238`—is contained in the second term through `A'(s)`. The first term remains the entire scalar logarithmic derivative with one common multiplicity `r`.

Equation (8) is purely algebraic and remains true for a non-reducing compression. The moving subbundle may create a new geometric response, but **motion itself does not decompose `m'/m`**. In Wong's zeta specialization, where that scalar logarithmic derivative is what the explicit-formula calculation later resolves into zeros, prime powers, Gamma, and polar terms, all of those constituents inherit the same coefficient `r` from the scalar factor.

There is one important scope condition. If the rule choosing `U(s)` or `V(s)` is itself engineered from the detailed meromorphic scalar `m(s)`, then the second term in (8) can acquire additional `m`-dependence. That is not forbidden algebraically. But then the desired arithmetic separation has been inserted into the **choice of moving geometry** and requires its own source-forced construction and independent sign theorem. It is not inherited from the existence of a moving compression.

For the natural spectral-subbundle version of the proposal, the obstruction is stronger. Multiplication by a nonzero scalar does not change eigenspaces or singular directions of `R(s)`. Hence a subbundle selected from the projective/eigenvector geometry of `M(s)=m(s)R(s)` is the same subbundle selected from `R(s)` (away from degeneracy and from scalar-sensitive threshold conventions). Such a subbundle is insensitive to replacing `m` by another nonzero scalar factor and therefore cannot encode a hidden prime-versus-Gamma separation.

## 2. The matched scalar-normalizer control survives arbitrary moving frames

The clean control is to hold `R`, `U`, and `V` fixed and replace the arithmetic normalizer by

\[
\widetilde m(s)=h(s)m(s),
\qquad h(s)\ne0.
\tag{9}
\]

Then

\[
\widetilde C(s)=h(s)C(s)
\tag{10}
\]

and therefore

\[
\frac{d}{ds}\log\det\widetilde C(s)
-
\frac{d}{ds}\log\det C(s)
=
r\frac{h'(s)}{h(s)}.
\tag{11}
\]

Nothing in the moving-subspace geometry distinguishes whether `h'/h` came from an Euler factor, a Gamma factor, a polar correction, a finite Blaschke factor, or an unrelated scalar scattering phase. Every scalar perturbation passes through the same channel.

This is the relevant falsification of a false geometric success. If one chooses `h` specifically to cancel the Gamma factor or the prime factor, then one has performed the analytic subtraction that the branch mandate excludes unless the cancellation is independently forced by geometry. A successful Mathia mechanism must explain why its geometry reacts differently to the finite and archimedean constituents **before** they are compressed into one central scalar.

## 3. Zero-shift Schur elimination is scalar homogeneous

Now let a possibly moving decomposition split a regular fiber into retained and eliminated coordinates, and write the normalized operator as

\[
R=
\begin{pmatrix}
R_{PP} & R_{PQ}\\
R_{QP} & R_{QQ}
\end{pmatrix}.
\tag{12}
\]

At each `s`, the corresponding blocks of `M=mR` are all multiplied by the same scalar `m`. If `R_{QQ}` is invertible, eliminating the `Q` block from `M` itself gives

\[
\begin{aligned}
S_P(M)
&=M_{PP}-M_{PQ}M_{QQ}^{-1}M_{QP}\\
&=mR_{PP}-(mR_{PQ})(mR_{QQ})^{-1}(mR_{QP})\\
&=m\left(R_{PP}-R_{PQ}R_{QQ}^{-1}R_{QP}\right).
\end{aligned}
\tag{13}
\]

Hence

\[
\boxed{S_P(mR)=mS_P(R).}
\tag{14}
\]

This is precisely the self-energy mechanism that a non-reducing compression introduces at **zero additive shift**, and it still cannot split the scalar normalizer. If the effective block has rank `r` and is invertible,

\[
\frac{d}{ds}\log\det S_P(M)
=
r\frac{m'}m
+
\frac{d}{ds}\log\det S_P(R).
\tag{15}
\]

The same matched control `m\mapsto hm` adds exactly `r h'/h`.

Equation (14) is not special to scattering. It is the elementary homogeneity of the Schur complement. More generally, any post-normalizer operator reduction `\Phi` satisfying

\[
\Phi(\lambda X)=\lambda\Phi(X)
\tag{16}
\]

for nonzero scalars `\lambda` obeys

\[
\Phi(M)=m\Phi(R).
\tag{17}
\]

The project-specific content is not the linear-algebra identity; it is that the identity closes exactly the homogeneous non-reducing escape left open by `WP-238`.

## 4. Positive Gram readouts lose the scalar scattering phase rather than separate it

There is a complementary sign check. From (6),

\[
C(s)^*C(s)=|m(s)|^2A(s)^*A(s)\succeq0.
\tag{18}
\]

On the unitary scattering axis, where the scalar normalizer has modulus one at regular points,

\[
|m(s)|=1,
\tag{19}
\]

so the direct positive Gram form becomes

\[
C(s)^*C(s)=A(s)^*A(s).
\tag{20}
\]

The arithmetic scalar **phase** carrying the logarithmic derivative has disappeared entirely. Thus the most literal way to turn the moving compression into an operator-positive form does not recover a better-signed version of `m'/m`; it erases that scalar phase. Recovering the phase requires differentiating a unitary/scattering response or otherwise using signed generator information, returning to the distinction already exposed by `WP-024` and the phase-positivity audits around `WP-170`--`WP-186`.

This does not say that Maaß–Selberg positivity contains no derivative of the scattering phase. It does. The point is narrower: **pointwise Gram positivity of the compressed intertwiner cannot be the missing mechanism** that selects the Weil zero term from the central normalizer.

## 5. What this does and does not close

The following candidate mechanisms are now ruled out as automatic escapes from `WP-238`:

- replacing a fixed reducing channel by an arbitrary smooth finite-rank compression while keeping the moving geometry independent of the scalar normalizer's internal analytic decomposition;
- allowing the compressed subspace to be non-reducing but reading the compressed intertwiner directly;
- eliminating complementary channels by the zero-shift Schur complement of `M` itself;
- any other post-normalizer degree-one scalar-homogeneous reduction followed by determinant/log-derivative scalarization;
- taking the direct positive Gram of such a compression on the unitary axis and hoping that it retains a selectively positive arithmetic phase.

Several genuinely different mechanisms remain open and are not prejudged here.

**Shifted Schur/Feshbach maps are non-homogeneous.** For fixed `z\ne0`, the operator `M-zI` does not scale as `m` times an `m`-independent operator. Its Schur complement can depend nonlinearly on `m`. The same warning applies to a Schur complement of the additive generator `(m'/m)I+R^{-1}R'`. Such a mechanism would need a canonical source for the shift, a full admissible test-class bridge, and an independent positivity theorem.

**Cayley/resolvent transforms are non-homogeneous.** Objects such as `(I-M)(I+M)^{-1}` can mix the scalar phase nonlinearly with `R`. They evade the algebraic homogeneity lemma, but no sign or Weil bridge follows merely from evasion.

**Scalar-sensitive moving geometry is a new arithmetic input.** A projector defined by thresholds or other rules depending on the value of `m(s)` can change under the matched control. To count as intrinsic geometry rather than target engineering, that rule must be forced independently and must survive replacement/matched controls without having the desired explicit-formula decomposition encoded in its definition.

**Matrix-valued global normalizers remain open.** If the arithmetic normalizer is genuinely operator-valued before scalarization, with noncommuting finite and archimedean structure, the central-factor argument no longer applies. Merely embedding the same scalar `m` into a larger matrix does not help.

**Pre-normalizer local-to-global coupling remains open.** A construction acting before the local finite and archimedean factors collapse to `m(s)` is still the structurally clean escape. This remains aligned with `WP-234`--`WP-236` and with the mixed-prime/nonseparable requirement in the branch mandate.

## 6. Prior-art and novelty audit

No historical novelty is claimed for (6)--(8), for determinant scaling, or for Schur-complement homogeneity. The Schur complement identity is standard linear algebra; a standard monograph reference is Fuzhen Zhang (ed.), *The Schur Complement and Its Applications*, Springer, 2005. The scattering input remains Tian An Wong, *Explicit formulas for the spectral side of the trace formula of SL(2)*, Acta Arith. 195 (2020), 149–175, arXiv:1608.02296, where the continuous spectral contribution is expressed using intertwining operators whose scalar normalizing factors are quotients of completed `L`-functions and are converted to Riemann–Weil explicit-formula terms.

The bounded literature audit found the expected classical ingredients but no basis for claiming a new theorem in automorphic representation theory. This finding should therefore be read as a **Mathia-specific research narrowing**: `WP-238` left moving and non-reducing compression as explicit possible escapes; the elementary central-scalar identities show that a broad canonical homogeneous subclass of those escapes changes only the normalized-operator remainder while retaining the completed arithmetic normalizer intact.

This is also not a repackaging of Hilbert–Pólya, Connes/trace positivity, Sonin/localization, or classical Weil positivity. It produces no new positive criterion and no spectrum from zeros. Its value is negative: it prevents the research program from mistaking extra geometric channel motion or zero-shift self-energy algebra for a mechanism that has actually separated the explicit-formula constituents.

## 7. Consequence for the research line

`WP-237` removes Arthur-height filtering. `WP-238` removes static reducing channel filtering. The present result removes the next homogeneous layer: **moving finite-rank compression and zero-shift non-reducing Schur elimination performed after scalar normalizer formation**.

The surviving frontier is now sharper. If the Maaß–Selberg/scattering route is to yield an intrinsic global Weil-positive form, it must obtain its extra arithmetic selectivity from a mechanism that breaks post-normalizer scalar homogeneity: a source-forced shifted/nonlinear transform with an independent sign theorem, a genuinely matrix-valued arithmetic normalizer, or a finite–archimedean coupling before central scalarization. Anything less continues to transport the same indivisible `m'/m` package that `WP-238` identified.