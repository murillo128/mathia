# MC-506 — Anti-diagonal pushforward reduces varying-profile bias to excess collisions

**Finding ID:** `MC-506`

**Status:** `EXACT-DERIVED` · `FRONTIER-ADVANCE` · `CLASSICAL-FOURIER+CHI-SQUARE` · `PRIOR-ART-AUDITED` · `NO-GENERAL-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-505` identifies the matched Fourier diagonal of the physical start/profile matrix as the only Fourier slice visible to the centered conductor kernel. That slice has an even smaller exact representation: the kernel depends on the matrix only through its pushforward under the sum coordinate

\[
(x,j)\longmapsto t=x+j\pmod p.
\]

Let \(p\) be an odd prime, let

\[
F:\mathbf F_p\to\mathbf C,
\qquad
\sum_{t\in\mathbf F_p}F(t)=0,
\]

and let \(B=(B_{x,j})_{x,j\in\mathbf F_p}\) be a nonnegative coefficient matrix with total mass

\[
W=\sum_{x,j}B_{x,j}>0.
\]

Define the anti-diagonal pushforward

\[
c_t:=\sum_{x\in\mathbf F_p}B_{x,t-x},
\qquad
\nu(t):=\frac{c_t}{W}.
\tag{1}
\]

Then the varying-profile correlation of `MC-505` satisfies the exact quotient identity

\[
\boxed{
\mathcal C_F(B)
:=\sum_{x,j}B_{x,j}F(x+j)
=\sum_t c_tF(t)
=W\,\mathbf E_{t\sim\nu}F(t).
}
\tag{2}
\]

Thus every feature of \(B\) not retained by the one-dimensional pushforward \(c\) is invisible to this conductor phase. In particular, two physically different start/profile matrices with the same \(c_t\) have exactly the same bias.

Let \(u\) denote the uniform distribution on \(\mathbf F_p\), and define the excess-collision statistic

\[
\Delta(B)
:=\chi^2(\nu\|u)
=p\sum_t\left(\nu(t)-\frac1p\right)^2
=p\sum_t\nu(t)^2-1.
\tag{3}
\]

Also write

\[
\sigma_F^2:=\frac1p\sum_t|F(t)|^2.
\tag{4}
\]

Since \(F\) has uniform mean zero, Cauchy--Schwarz gives the exact source-collision certificate

\[
\boxed{
\frac{|\mathcal C_F(B)|}{W}
\le
\sigma_F\sqrt{\Delta(B)}.
}
\tag{5}
\]

For the centered quadratic relative phase \(F_c\) of `MC-497`, one has the exact energy

\[
\sigma_{F_c}^2
=1-\frac3p-rac{(1+\chi(-1))^2}{p^2}
<1.
\tag{6}
\]

Hence

\[
\boxed{
\frac{|\mathcal C_{F_c}(B)|}{W}
\le
\sqrt{\Delta(B)}.
}
\tag{7}
\]

Consequently, fixed normalized bias at level \(\eta>0\) requires

\[
\boxed{
\Delta(B)\ge\frac{\eta^2}{\sigma_{F_c}^2}\ge\eta^2,
}
\tag{8}
\]

or equivalently

\[
\boxed{
\sum_t c_t^2
\ge
\frac{W^2}{p}
\left(1+\frac{\eta^2}{\sigma_{F_c}^2}\right).
}
\tag{9}
\]

The remaining hard-mask alignment route therefore has a necessary arithmetic signature that is lower-dimensional than the nuclear interaction norm of `MC-505`: the exact first-exit source must create a positive excess of weighted collisions in the physical conductor argument \(t=x+j\) above the uniform baseline \(W^2/p\).

This is only a necessary condition for large bias, not a sufficient one. Excess collisions may occur in residues whose signed correlation with \(F_c\) cancels.

## Derivation

Equation `(2)` follows by collecting matrix cells on the fibres of the sum map:

\[
\begin{aligned}
\mathcal C_F(B)
&=\sum_{x,j}B_{x,j}F(x+j)\\
&=\sum_tF(t)\sum_xB_{x,t-x}\\
&=\sum_tc_tF(t).
\end{aligned}
\tag{10}
\]

Because \(\sum_tF(t)=0\),

\[
\frac{\mathcal C_F(B)}W
=\sum_t\left(\nu(t)-\frac1p\right)F(t).
\tag{11}
\]

Applying Cauchy--Schwarz and using `(3)`--`(4)`,

\[
\begin{aligned}
\left|\frac{\mathcal C_F(B)}W\right|
&\le
\left(\sum_t\left|\nu(t)-\frac1p\right|^2\right)^{1/2}
\left(\sum_t|F(t)|^2\right)^{1/2}\\
&=\sigma_F\sqrt{\Delta(B)},
\end{aligned}
\tag{12}
\]

which proves `(5)`.

For the exact quadratic phase in `MC-497`,

\[
R_c(0)=0,
\qquad
R_c(m)=\chi(m^2-c^2)\quad(m\ne0),
\]

with \(c\ne0\), and

\[
\mu_c=-\frac{1+\chi(-1)}p,
\qquad
F_c=R_c-\mu_c.
\tag{13}
\]

The three residues \(0,c,-c\) contribute zero to \(R_c^2\), while every other residue contributes one. Therefore

\[
\sum_mR_c(m)^2=p-3.
\tag{14}
\]

Centering subtracts the squared mean:

\[
\sum_m|F_c(m)|^2
=\sum_mR_c(m)^2-p\mu_c^2
=p-3-\frac{(1+\chi(-1))^2}{p},
\tag{15}
\]

which after division by \(p\) gives `(6)`.

## Exact collision interpretation

The statistic in `(3)` is directly countable in the physical source. If the entries of \(B\) arise from source items \(\alpha\) with nonnegative weights \(w_\alpha\) and physical sum-coordinate residues

\[
t_\alpha=x_\alpha+j_\alpha\pmod p,
\]

then

\[
c_t=\sum_{\alpha:t_\alpha=t}w_\alpha
\]

and

\[
\boxed{
\sum_tc_t^2
=
\sum_{\alpha,\beta}
 w_\alpha w_\beta
\mathbf1_{t_\alpha=t_\beta}.
}
\tag{16}
\]

Thus the decisive statistic is a weighted pair-collision count for the actual conductor argument after every first-exit, hard-mask, endpoint, and reconstruction restriction has been restored. It does not require choosing profile classes, estimating a matrix rank, or introducing an auxiliary random model.

Define the effective support of this pushforward by

\[
R_t:=\frac{W^2}{\sum_tc_t^2}.
\tag{17}
\]

Then \(R_t\le p\) and

\[
\Delta(B)=\frac p{R_t}-1.
\tag{18}
\]

So `(5)` becomes

\[
\boxed{
\frac{|\mathcal C_F(B)|}{W}
\le
\sigma_F\sqrt{\frac p{R_t}-1}.
}
\tag{19}
\]

This exposes an important limitation of a pure collision certificate. Merely having conductor-scale effective support is not enough to force a small bias. To certify a normalized bias at most \(arepsilon\) through `(19)`, one needs

\[
R_t
\ge
\frac{p}{1+(\varepsilon/\sigma_F)^2},
\tag{20}
\]

which is near-maximal \(L^2\) equidistribution when \(arepsilon\to0\). The source-collision route is therefore sharp as a diagnostic but demanding as a cancellation proof.

## Relation to the matched Fourier diagonal of MC-505

The reduction in `MC-505` is exactly the Fourier transform of the pushforward `(1)`. With its convention

\[
d_k(B)
=\frac1p\sum_{x,j}B_{x,j}e_p(kx)e_p(kj),
\]

one has

\[
\boxed{
d_k(B)=\frac1p\sum_tc_te_p(kt).
}
\tag{21}
\]

For \(k\ne0\), the uniform part of \(c\) vanishes. Parseval therefore gives

\[
\boxed{
\sum_{k\ne0}|d_k(B)|^2
=\frac1p\sum_t\left|c_t-\frac Wp\right|^2
=\frac{W^2}{p^2}\Delta(B).
}
\tag{22}
\]

So the “matched Fourier diagonal” is not merely a special slice of a two-dimensional interaction matrix: it is the complete Fourier representation of a one-dimensional physical pushforward. The nuclear norm \(\|PBP\|_*\) from `MC-505` remains a valid decomposition-free upper-bound certificate, but it is not the minimal sufficient representation for this kernel. Any matrix structure that changes \(PBP\) while leaving the anti-diagonal sums \(c_t\) fixed cannot change the bias.

This distinction can matter in either direction. A complicated first-exit matrix may have a large centered nuclear norm while its anti-diagonal pushforward is nearly uniform, in which case `(5)` proves cancellation that the nuclear certificate may miss. Conversely, broad start and offset marginals do not help when the sum-coordinate pushforward has substantial excess collisions.

## What changes in the decisive arithmetic test

For the quadratic repeated-residue hard-mask branch, the first source-derived object to compute after reconstructing the exact physical matrix is now

\[
c_t=\sum_xB_{x,t-x}.
\]

The primary pair-count question is whether the exact first-exit arithmetic forces

\[
\sum_{\alpha,\beta}
 w_\alpha w_\beta
\mathbf1_{x_\alpha+j_\alpha\equiv x_\beta+j_\beta\pmod p}
\]

to exceed the uniform baseline \(W^2/p\) by a fixed relative amount on material blocks.

If the excess is \(o(W^2/p)\), equation `(7)` closes the quadratic hard-mask bias on that block. If the excess is a fixed positive proportion, the collision certificate alone cannot close it; the next question is whether those colliding fibres carry the correct signed alignment with \(F_c\), not whether the original two-dimensional matrix has many profile classes.

This replaces a potentially high-dimensional profile-classification problem by a concrete weighted congruence-pair count whenever the kernel remains exactly \(F_c(x+j)\).

## Prior art and novelty boundary

The abstract ingredients are standard. Equation `(2)` is pushforward along a group homomorphism; `(21)` is the finite-group Fourier-slice identity for that pushforward; `(5)` is the usual Cauchy--Schwarz bound expressed through Pearson chi-square divergence from uniformity; and `(16)` is the standard collision/second-moment identity. The targeted literature audit found no reason to claim novelty for any of these harmonic, probabilistic, or additive-combinatorial facts.

The durable Mathia contribution is only their exact specialization to the current first-exit source representation. `MC-505` left the frontier as control of a matched two-dimensional Fourier diagonal or centered nuclear norm. The present finding identifies the exact quotient carrying that diagonal and turns the remaining source dependence into a weighted congruence-collision problem that can be attacked directly in the physical first-exit variables.

No claim is made that this source-specific pair count is absent from all surrounding character-sum or sieve literature; the novelty claim is deliberately limited to the internal reduction and decisive-test refinement.

## Representation audit

The map \(B\mapsto c\) is lossless for the specific observable being studied because the kernel itself factors exactly through \(x+j\). No source cell is discarded before its contribution is aggregated on the fibre that the conductor phase actually sees.

This quotient must be taken only after the exact physical first-exit table has been constructed. Replacing that table by a completed period, smooth envelope, independent mask, uniform start model, or other relaxed representation before forming \(c_t\) can change the weighted collision statistic and is not licensed by `(2)`.

For signed or complex pre-aggregation coefficients, equation `(2)` and the Fourier identities remain exact, but \(
u\) is no longer a probability distribution and the chi-square/collision interpretation in `(3)`, `(8)`, and `(16)` does not apply without a separate signed-measure analysis. That is precisely the distinct escape channel already retained by `MC-503`--`MC-505`.

## Boundaries and failure modes

- **Necessary, not sufficient.** A fixed excess collision rate is required for fixed quadratic bias, but does not force that bias because the excess may be orthogonal to \(F_c\).
- **Near-uniformity is demanding.** Equation `(20)` shows that this certificate yields \(o(1)\) bias only from \(L^2\)-near-uniformity of the sum-coordinate pushforward, not merely from broad support.
- **Nonnegative source coefficients.** The probability/collision formulation uses the nonnegative aggregation of the current `MC-495` branch. Signed or complex coefficients require a different normed-measure statement.
- **Conductor-local.** The result is for one prime conductor and one repeated-residue block. Outer conductor sums, dyadic decompositions, and reconstruction weights must still be charged.
- **Exact physical coordinate.** The congruence in `(16)` is the physical conductor argument produced by the source reconstruction. An affine or completed surrogate can change collisions even when it looks harmonically similar.
- **No global Möbius conclusion.** The result gives no new estimate for \(M(x)\), no zero-free region, and no RH consequence.

## Consequence

The current quadratic hard-mask frontier can now be tested through a single source-derived pair statistic. Before estimating profile diversity, matrix rank, or nuclear interaction complexity, count weighted collisions of the exact physical phase argument \(t=x+j\). Vanishing relative collision excess closes the bias immediately; fixed bias forces a fixed excess above the uniform collision baseline. If such excess survives, its arithmetic origin and its signed placement against \(F_c\) become the next load-bearing questions.