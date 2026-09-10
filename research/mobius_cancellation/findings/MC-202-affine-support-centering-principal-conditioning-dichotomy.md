# MC-202 — Affine support centering has an exact principal/transverse conditioning dichotomy

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `DECISIVE-NEGATIVE`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-200` and `MC-201` reduce the logarithmic-primorial sign/support route to one hard uncentered mixed source statistic. At a complete block `X=Nq`, with `q=q_y=prod_{p<=y}p`, write the `N` source values in each reduced residue class `a mod q` as

\[
x_{a,i}\in\{-1,0,1\},\qquad 1\le i\le N,
\]

and put

\[
A_a=\sum_i x_{a,i},\qquad B_a=\sum_i x_{a,i}^2,
\qquad S=\sum_a A_a,\qquad Q=\sum_a B_a,
\]

with `phi=phi(q)` and

\[
u_a=A_a-\frac S\phi,\qquad v_a=B_a-\frac Q\phi.
\]

The live temptation after `MC-201` is to remove the principal contamination in the mixed source aggregate by centering the square-free-support factor before summation. The whole affine family can be classified exactly.

For arbitrary class weights `rho_a`, define

\[
T_\rho:=
\sum_a\sum_{i\ne j}
 x_{a,i}\bigl(x_{a,j}^2-\rho_a\bigr).
\tag{1}
\]

Set

\[
kappa_a:=B_a-1-(N-1)\rho_a,
\qquad
\bar\kappa:=\frac1\phi\sum_a\kappa_a.
\tag{2}
\]

Then

\[
\boxed{
T_\rho
=\bar\kappa S
+\sum_a u_a(\kappa_a-\bar\kappa).
}
\tag{3}
\]

Thus every affine support-centering of this source statistic splits into exactly two channels:

1. a principal channel with coefficient `bar(kappa)` multiplying the rough Möbius mode `S`; and
2. a transverse centered channel involving only the zero-sum signed residue field `u`.

For the most natural scalar family `rho_a=rho`, equation `(3)` becomes

\[
\boxed{
T_\rho
=\alpha_\rho S+C_{1,2},
\qquad
\alpha_\rho=rac Q\phi-1-(N-1)\rho,
}
\tag{4}
\]

where `C_{1,2}=sum_a u_av_a` is exactly the centered sign/support covariance of `MC-200`--`MC-201`.

This gives a sharp dichotomy. If `alpha_rho=0`, the principal contamination is canceled exactly but the decoder disappears at the same instant: `T_rho=C_{1,2}` contains only the already-controlled transverse covariance. If `alpha_rho!=0`, the principal mode survives and

\[
\boxed{
S=\frac{T_\rho-C_{1,2}}{\alpha_\rho}.
}
\tag{5}
\]

so any suppression of the principal coefficient is paid back as inverse-conditioning loss unless an additional arithmetic theorem controls the numerator jointly.

Consequently, **constant affine centering of the square-free-support factor cannot by itself produce an intermediate carrier that both cancels the target principal term and retains a well-conditioned route back to that target.** Exact cancellation loses the target coordinate; approximate cancellation weakens the decoder by exactly the same residual coefficient.

No improved estimate for `M(X)`, `G_y(X)`, or the Riemann zero set is claimed.

## 1. Exact affine decomposition

For one residue class, abbreviate `x_i=x_{a,i}`, `A=A_a`, and `B=B_a`. Since `x_i^3=x_i`,

\[
\sum_{i\ne j}x_ix_j^2
=\left(\sum_i x_i\right)\left(\sum_jx_j^2\right)-\sum_i x_i^3
=A(B-1).
\tag{6}
\]

Also

\[
\sum_{i\ne j}\rho_a x_i
=\rho_a(N-1)A.
\tag{7}
\]

Therefore the contribution of class `a` to `(1)` is exactly `A_a kappa_a`, and

\[
T_\rho=\sum_aA_a\kappa_a.
\tag{8}
\]

Decompose

\[
A_a=\frac S\phi+u_a,
\qquad
\kappa_a=\bar\kappa+(\kappa_a-\bar\kappa),
\]

with both centered fields summing to zero. Expanding `(8)` proves `(3)`.

For scalar `rho`,

\[
\bar\kappa=\frac Q\phi-1-(N-1)\rho=\alpha_\rho,
\]

while

\[
\kappa_a-\bar\kappa=B_a-\frac Q\phi=v_a.
\]

This proves `(4)`. At `rho=0`, `(4)` is precisely the `MC-200` identity

\[
E_{1,2}=\left(\frac Q\phi-1\right)S+C_{1,2}.
\]

Thus `MC-200` is the uncentered endpoint of the full affine family rather than one isolated formula.

## 2. Exact centering removes exactly the recoverable principal coefficient

There is a unique scalar value

\[
\rho_*:=\frac{Q/\phi-1}{N-1}
\tag{9}
\]

for which `alpha_{rho_*}=0`. It depends only on the unsigned support total `Q` and the block geometry, not on `S`. At this value,

\[
\boxed{T_{\rho_*}=C_{1,2}.}
\tag{10}
\]

So the obvious source-level operation “center the support factor so that the principal contamination cancels” succeeds algebraically, but succeeds by projecting the statistic onto the same centered covariance that `MC-201` already showed is RH-scale harmless for sufficiently small logarithmic primorial exponent `c`.

This is consistent with the quotient obstruction `MC-199`. A centered signed profile together with the full support profile does not universally determine `S` on matched ternary sources. Equation `(10)` therefore cannot be turned into a source-free decoder after the principal coefficient has been set to zero. Any recovery would require an additional Möbius-specific relation not contained in affine support centering itself.

The even stronger classwise choice

\[
\rho_a=\frac{B_a-1}{N-1}
\tag{11}
\]

makes every `kappa_a` vanish and hence gives `T_rho=0` identically. More aggressive local centering does not expose a hidden signed invariant; it deletes the whole affine statistic.

## 3. Global support-density centering nearly reaches the singular point

A second canonical-looking choice is the exact global supported-site density

\[
\rho_0:=\frac{Q}{N\phi}.
\tag{12}
\]

For this choice the principal coefficient collapses from order `N` at `rho=0` to

\[
\boxed{
\alpha_{\rho_0}=\rho_0-1.
}
\tag{13}
\]

At the logarithmic primorial, `MC-201` gives uniformly at complete blocks

\[
\frac Q\phi=N P_y+O(\sqrt X),
\qquad
P_y=\prod_{p>y}\left(1-\frac1{p^2}\right),
\]

and, for fixed `c<1/2`,

\[
1-P_y\sim\frac1{y\log y},
\qquad y=c\log X.
\tag{14}
\]

Since `sqrt(X)/N=X^{c-1/2+o(1)}`, equation `(12)` yields

\[
\rho_0=P_y+o\left(\frac1{y\log y}\right),
\]

and therefore

\[
\boxed{
\alpha_{\rho_0}
\sim-\frac1{y\log y}.
}
\tag{15}
\]

Thus global mean-centering of square-free support almost reaches the singular centering `(9)`: it destroys the polynomially large `~N` decoder coefficient and leaves only an inverse-polylogarithmic principal coefficient. The statistic may look more “fluctuation-like”, but that normalization does not create a cheaper route to `S`; it sharply worsens the inverse problem.

## 4. Quantitative conditioning ledger at the RH scale

`MC-201` proves, for sufficiently small fixed `c`,

\[
|C_{1,2}|\ll \phi N\sqrt X,
\tag{16}
\]

because `X/q=N` at a complete block. Suppose a scalar centering is chosen so that for some `delta>=0`

\[
|\alpha_\rho|\asymp N X^{-\delta}.
\tag{17}
\]

Using only the independently available support control `(16)`, the covariance contribution in the decoder `(5)` costs

\[
\frac{|C_{1,2}|}{|\alpha_\rho|}
\ll \phi X^{1/2+\delta}
\le qX^{1/2+\delta}
=X^{1/2+c+\delta+o(1)}.
\tag{18}
\]

Hence suppressing the principal coefficient by a factor `X^{-delta}` spends `delta` of the available power margin. For a target `X^{1/2+epsilon}`, this elementary route needs, up to the usual `o(1)` slack,

\[
c+\delta<\epsilon.
\tag{19}
\]

At `delta=0`, `(18)` recovers the `MC-201` covariance budget. As `alpha_rho` approaches zero, the decoder becomes correspondingly ill-conditioned; at exact zero it ceases to exist.

Equation `(18)` is deliberately conditional on using the existing separate bound for `C_{1,2}`. It is not a universal lower bound on every possible proof. A genuinely new arithmetic theorem could estimate `T_rho-C_{1,2}` jointly, exploit cancellation unavailable to separate absolute bounds, or replace this affine family entirely. Such a theorem would be new source information; affine centering alone does not provide it.

## 5. Matched controls and the remaining escape routes

The principal/transverse split is not an artifact of Möbius. If the support counts are constant across residue classes, `B_a=B`, then `v_a=0` and hence `C_{1,2}=0`. For scalar `rho`, equation `(4)` reduces exactly to

\[
T_\rho=\alpha_\rho S.
\tag{20}
\]

So on a matched ternary array with perfectly uniform support, every scalar affine-centered mixed statistic is either a rescaled copy of the principal sum or identically blind to it. There is no third affine channel hidden by support irregularity.

This control is intentionally source-generic. It does not rule out a theorem using Möbius multiplicativity, divisor structure, growing-shift cancellation, or another exact arithmetic constraint. It rules out attributing an independent gain to the affine centering operation itself.

Equation `(3)` also identifies what remains outside this no-go. A genuinely class-dependent `rho_a` produces a nonconstant coefficient field `kappa_a-bar(kappa)` and can couple signed transverse structure to support geometry differently from `C_{1,2}`. Non-affine inter-site statistics, ordered divisor relations, multi-scale conservation identities, and source-coupled cancellations are likewise not covered. Any such continuation must still show that its retained uncentered information is quantitatively cheaper than the Mertens target rather than merely another exact encoding.

## 6. Prior-art and novelty audit

The algebra in `(3)` is finite-dimensional centering: a vector is split into its constant component and zero-sum component, and a bilinear statistic splits into mean and covariance terms. This is classical projection/centering machinery, closely analogous to the elementary decomposition underlying centered moments and Hoeffding-type kernel decompositions. No novelty is claimed for that general mechanism.

The mixed Möbius/square-free correlation surface is also established prior art. `MC-200` already audits the relevant fixed-shift/logarithmically averaged correlation results and shows why they do not pay the polynomially sparse growing-shift bill. A targeted audit for centered/U-statistic formulations and mixed Möbius–square-free correlations found neighboring classical centering machinery and known correlation results, but no external theorem is needed for `(3)`--`(20)` and no literature-absence claim is used as evidence.

The durable Mathia contribution is therefore narrower: the exact classification of the **specific affine source-centering escape suggested by the live `MC-200`--`MC-201` decoder**, together with its conditioning ledger at the logarithmic primorial. It is a frontier restriction, not a new theorem about U-statistics or multiplicative functions in general.

## Boundaries and falsification tests

- The exact identities `(3)`--`(13)` are complete-block finite algebra and require no analytic continuation, zero-free region, or cancellation hypothesis.
- The asymptotics `(14)`--`(15)` and budget `(16)`--`(19)` use the logarithmic-primorial regime and the support estimates already established in `MC-201`; they are not asserted for arbitrary moduli or for `c>=1/2`.
- The no-go concerns **affine centering of the support factor inside the same-residue mixed statistic**. It does not classify nonlinear source functions, class-dependent arithmetic weights, or different source relations.
- `rho_*` and `rho_0` depend only on unsigned support totals and block geometry. Their use does not assume a Mertens estimate, but recovering `S` after exact centering would require extra source information by `MC-199`.
- A special theorem for actual Möbius could beat the separate-bound conditioning ledger if it proves cancellation in `T_rho-C_{1,2}` directly. Such a theorem would be a substantive new arithmetic input and is not ruled out here.
- The constant-support matched control is not multiplicative and is not presented as a counterexample to Möbius-specific statements. It tests only whether the affine transformation itself creates an independent universal cancellation channel.

The core claim is falsified by any finite ternary complete-block array for which direct evaluation of `(1)` disagrees with `(3)`. The scalar specialization is falsified if `(4)` fails after substituting `u_a`, `v_a`, `S`, and `Q`. The conditioning claim is falsified if the `MC-201` bound `(16)` combined with `(17)` does not imply `(18)`.

## Consequence for the active frontier

`MC-201` left open the possibility of “a different source relation whose principal contamination cancels before the target Mertens mode is inserted.” The most immediate realization of that idea—subtracting a constant from the square-free-support factor in the mixed source statistic—is now closed as an independent escape.

Exact affine centering cancels the target coefficient and the target information together. Approximate affine centering retains a decoder, but every reduction in its principal coefficient appears inversely in the conditioning ledger. The next viable source relation must therefore do something structurally stronger: preserve a different uncentered/source-sensitive degree of freedom, exploit a genuinely nonconstant arithmetic coupling before centering, or obtain a joint signed estimate whose saving exceeds the decoder loss without assuming the desired Mertens bound.