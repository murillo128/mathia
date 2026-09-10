# PF-268 — the lowest finite-seam pole forbids bare supercritical separated weighting

**Status:** `EXACT-DERIVED + POSITIVE-LOWEST-POLE-OBSTRUCTION + SUPERCRITICAL-WEIGHT-NO-GO + DECISIVE-NEGATIVE/ROUTE-REDIRECTION`.

[[research/prime_flute/findings/PF-261-finite-seam-crossover-is-a-bounded-positive-mixture-of-massive-axis-resolvents|PF-261]] reduces the fixed-axis finite seam to a positive odd-mass resolvent ladder, while [[research/prime_flute/findings/PF-267-path-green-correlations-multiply-and-recover-uniform-amplitude-decay|PF-267]] proves that every massive Green kernel has the right joint amplitude/decay estimate. The accepted finite-seam clue therefore asked whether summing the complete odd ladder could retain a strict endpoint-weighted exponent `R>1` before the normalized Robin and separated-Poisson stages.

It cannot. The obstruction is simpler than a difficult coupled mass regime: **the first pole alone already prevents every bare supercritical separated weight at each fixed finite seam scale**.

Fix `r>0` and `s>0`. In either parity block, let

\[
a_0=\frac{\pi}{2rs},
\qquad
\mu_0=\sqrt{1+a_0^2}>1.
\]

PF-264 gives, for the fixed mass `a_0` and parity-chain indices `i\le j` tending to infinity,

\[
G_{ij}(a_0)
=\frac{1}{2\mu_0}
 i^{-1/2+\mu_0}j^{-1/2-\mu_0}
 \bigl(1+O_{r,s}(i^{-1})+O_{r,s}(j^{-1})\bigr).
\]

PF-261 inserts the quarter-order endpoint factors and, off the diagonal, sums all massive Green terms with the **same sign**. Hence for all sufficiently large `i\le j` in one parity block,

\[
\boxed{
|\langle e_{2i+\varepsilon},\mathcal R_{s,r}^0e_{2j+\varepsilon}\rangle|
\ge
c_{r,s,\varepsilon}\,
 i^{\mu_0-1}j^{-\mu_0-1},
}
\tag{1}
\]

with `c_{r,s,\varepsilon}>0`. On proportional separated blocks, for example

\[
i\in[N,5N/4],
\qquad
j\in[4N,5N],
\]

the ratio factor is only a positive constant depending on `r,s`; therefore

\[
\boxed{
|\langle e_{2i+\varepsilon},\mathcal R_{s,r}^0e_{2j+\varepsilon}\rangle|
\ge c'_{r,s,\varepsilon}N^{-2}.
}
\tag{2}
\]

This `N^{-2}` floor is enough to kill every strict `R>1` separated input weight. If `\mathsf S` denotes the matrix restriction to the standard separated cone `j\ge2i+2` and `N_\varepsilon e_{2j+\varepsilon}=(j+1)e_{2j+\varepsilon}`, then for every `R>1`,

\[
\boxed{
\mathsf S\mathcal R_{s,r}^0N_\varepsilon^R
\text{ has no bounded extension on }\ell^2.
}
\tag{3}
\]

The same conclusion holds with the actual fixed-axis corridor weight `K_s^0=sA^{1/2}` and with any fixed high-mode cutoff:

\[
\boxed{
\mathsf S\mathcal R_{s,r}^0(K_s^0)^R
\mathbf 1_{(Z,\infty)}(K_s^0)
\text{ is unbounded for every }R>1,
}
\tag{4}
\]

for every finite `Z`.

Thus the PF-261 odd-mass sum does not merely fail to *prove* a supercritical margin; the proposed bare finite-seam margin is false. The fixed-axis route must use additional structure **before** demanding `R>1`: the combined normalized Robin transform from PF-257 and/or the spatially separated Robin--Poisson propagation in PF-243. This result does not rule out either mechanism.

## Claim

Fix `r,s>0` and one parity `\varepsilon\in\{0,1\}`. Let

\[
f_i=e_{2i+\varepsilon},
\qquad
\mathsf N f_i=(i+1)f_i,
\]

and let `\mathsf S` act on matrices by retaining only entries with `j\ge2i+2`. On finitely supported vectors define

\[
T_R:=\mathsf S\mathcal R_{s,r}^0\mathsf N^R.
\]

Then:

1. there are `N_0` and `c_{r,s,\varepsilon}>0` such that (1) holds for all `j\ge i\ge N_0`;
2. on the proportional blocks above, (2) holds uniformly in the block size `N` once `N` is sufficiently large;
3. for every `R>1`, `T_R` is unbounded on `\ell^2`;
4. replacing `\mathsf N` by the physical parity restriction of `A^{1/2}` changes only fixed comparison constants, and replacing it by `K_s^0=sA^{1/2}` introduces only the fixed factor `s^R`, so the same unboundedness holds;
5. inserting `\mathbf1_{(Z,\infty)}(K_s^0)` for any fixed `Z` does not change the conclusion because the witness blocks escape to arbitrarily high modes.

No assertion is made at the endpoint `R=1`, and no upper boundedness result for `R<1` is claimed.

## 1. Positivity makes the first mass pole a permanent lower bound

PF-261 proves for distinct same-parity physical modes

\[
\langle e_m,\mathcal R_{s,r}^0e_n\rangle
=-\frac{2}{rs^2\sqrt{\kappa_m\kappa_n}}
\sum_{k\ge0}a_k^2
\langle e_m,(L+a_k^2)^{-1}e_n\rangle,
\tag{5}
\]

where

\[
a_k=\frac{(2k+1)\pi}{2rs}.
\]

The below-spectrum Green matrices in the PF parity gauge are strictly positive. PF-267 uses exactly this positivity in its path-correlation factorization. Therefore every summand on the right of (5) has the same sign and

\[
|\langle e_m,\mathcal R_{s,r}^0e_n\rangle|
\ge
\frac{2a_0^2}{rs^2\sqrt{\kappa_m\kappa_n}}
\langle e_m,(L+a_0^2)^{-1}e_n\rangle.
\tag{6}
\]

This is the decisive monotonicity. No refinement of the higher-mass tail can cancel a failure already present in the lowest pole.

## 2. PF-264 turns the first pole into a homogeneous order-minus-two floor

Apply PF-264 with fixed `a=a_0` and write the physical modes as `m=2i+\varepsilon`, `n=2j+\varepsilon`. Its two-index law gives

\[
G_{ij}^{(\varepsilon)}(a_0)
=\frac{1}{2\mu_0}
 i^{-1/2+\mu_0}j^{-1/2-\mu_0}
 \left(1+O_{r,s}(i^{-1})+O_{r,s}(j^{-1})\right).
\tag{7}
\]

For fixed `r,s`, choose `N_0` so that the parenthesis is at least `1/2` once both indices exceed `N_0`. Since

\[
\kappa_{2i+\varepsilon}\asymp i+1,
\qquad
\kappa_{2j+\varepsilon}\asymp j+1,
\tag{8}
\]

substitution of (7)--(8) into (6) proves (1).

If `i/N` stays in `[1,5/4]` and `j/N` stays in `[4,5]`, then

\[
i^{\mu_0-1}j^{-\mu_0-1}
=N^{-2}
(i/N)^{\mu_0-1}(j/N)^{-\mu_0-1}.
\tag{9}
\]

The second factor has a strictly positive minimum on this compact rectangle. This proves (2). The constant can be extremely small when `s` is small because `\mu_0\asymp s^{-1}`, but it is nonzero for every fixed `s`; boundedness is an arbitrarily-high-mode question, so a small fixed coefficient cannot repair the power-law divergence.

## 3. A positive block witness forces the threshold `R<=1`

Let

\[
I_N=\{i:N\le i\le5N/4\},
\qquad
J_N=\{j:4N\le j\le5N\}.
\tag{10}
\]

For large `N`, every pair `(i,j)\in I_N\times J_N` lies in `j\ge2i+2`. Let

\[
v_N=|J_N|^{-1/2}\sum_{j\in J_N}f_j,
\qquad
\|v_N\|=1.
\tag{11}
\]

All retained matrix entries have the same negative sign. Equations (2), (10), and (11) therefore give, for every `i\in I_N`,

\[
\begin{aligned}
|(T_Rv_N)_i|
&=|J_N|^{-1/2}
\sum_{j\in J_N}
|\langle f_i,\mathcal R_{s,r}^0f_j\rangle|(j+1)^R\\
&\ge c_{r,s,\varepsilon}
N^{-1/2}\cdot N\cdot N^{-2}\cdot N^R\\
&\ge c_{r,s,\varepsilon}N^{R-3/2}.
\end{aligned}
\tag{12}
\]

There are `\asymp N` output indices in `I_N`, hence

\[
\boxed{
\|T_Rv_N\|
\ge c_{r,s,\varepsilon}N^{R-1}.
}
\tag{13}
\]

For every `R>1`, (13) diverges as `N\to\infty`, proving (3).

On this parity block `A^{1/2}` is diagonal with eigenvalue `\kappa_{2j+\varepsilon}\asymp j+1`, so the same witness proves the `A^{R/2}` version. Multiplication by the fixed scalar `s^R` does not change unboundedness, proving the `K_s^0` statement. Any fixed high cutoff contains `J_N` for all sufficiently large `N`, proving (4).

## 4. Why PF-267 cannot rescue the bare seam

PF-267's uniform estimate is fully consistent with this obstruction. At fixed mass and fixed proportional separation `j/i=\lambda>1`, its path exponent satisfies

\[
\Psi_{ij}(\mu_0)\asymp\mu_0\log\lambda,
\tag{14}
\]

which is independent of the absolute scale `i`. It supplies a very small ratio-dependent constant `\lambda^{-c\mu_0}` when `s` is small, but no extra power of `i` along a fixed-ratio ray. PF-264 identifies the corresponding exact leading power as `i^{-2}` after the PF-261 endpoint weights.

The stronger large-mass product in PF-267 also cannot remove the floor: for the fixed first pole, eventually `\mu_0\ll j`, so the witness blocks leave the `\mu\gtrsim j` regime. The problem is therefore not failure to sum the high-mass tail. It is the persistent low-pole asymptotic seen after taking the transverse-mode limit at any fixed finite seam width.

Equivalently, two limits relevant to the route do not commute at the level of supercritical weighted locality:

\[
s\downarrow0\text{ at fixed modes}
\qquad\text{versus}\qquad
(i,j)\to\infty\text{ at fixed }s.
\tag{15}
\]

PF-258--PF-260 control the first regime through the intrinsic-six tangent and retain `1<R<2`. PF-268 shows that the bare finite seam in the second regime has no `R>1` separated weighted bound. Any proof that transfers the tangent margin uniformly through finite `s` without addressing this order-of-limits obstruction is invalid.

## 5. Consequence for the live Robin--Poisson route

The negative result is deliberately narrow. It rules out the strategy

> prove `R>1` weighted locality for the naked positive relative seam `\mathcal R_{s,r}^0`, then pass that margin unchanged through Robin regularization and spatial propagation.

It does **not** rule out the physical combined source map

\[
B_{s,r}^0
=X_{s,r}^0(I+(X_{s,r}^0)^*X_{s,r}^0)^{-1}
\tag{16}
\]

from PF-257/PF-261. The rational recombination in (16) may suppress or reorganize the low-pole tail, and PF-257 already warns that splitting the physical factor into separately estimated amplitude/orientation pieces can lose useful correlation.

Nor does PF-268 rule out PF-243's one-sided separated Robin--Poisson maps. Those maps include a fixed positive **spatial source-to-observation separation before the final weighted estimate**. Such propagation can add a spectral damping factor that is absent from the bare seam matrix in (3)--(4). The correct next test is therefore to place the finite-seam/Robin factor inside the separated Poisson leg first and only then ask whether `K_a^R`, `R>1`, is bounded.

## 6. Prior-art and novelty audit

The ingredients behind (5)--(7) are not new general operator theory. The positive below-spectrum Green representation and left/right solution factorization for Jacobi operators are classical; PF-264 already audits them against Gerald Teschl, *Jacobi Operators and Completely Integrable Nonlinear Lattices*, AMS Mathematical Surveys and Monographs 72 (2000). General boundedness characterizations for weighted Hardy-type operators are also classical; a targeted literature check found, for example, A. L. Bernardis, F. J. Martín-Reyes, and P. Ortega Salvador, *A new proof of the characterization of the weighted Hardy inequality*, Proc. Royal Soc. Edinburgh A 135 (2005), 941--945, DOI `10.1017/S030821050500048X`.

No external Hardy theorem is used in the proof above: the explicit proportional-block vector (11) gives the required unboundedness directly. A targeted search did not locate the Prime-Flute-specific consequence combining the PF-261 odd-pole representation, PF-264's exact massive Jacobi asymptotic, and the quarter-order seam endpoint normalization. No novelty is claimed for the general block-test argument, Jacobi positivity, or weighted Hardy theory. The durable project-specific result is the exact identification of the **first finite-seam pole** as a no-go for the previously proposed `R>1` bare-seam gate.

## 7. Falsification and boundary checks

1. **Fixed finite seam scale.** The proof fixes `s>0` before sending transverse modes to infinity. The constant and the onset index depend on `s`; this dependence is harmless for the unboundedness statement but does not provide a uniform asymptotic in `s`.
2. **Same-parity separated cone.** One parity block is enough to disprove boundedness. Opposite parities vanish and are irrelevant.
3. **Off-diagonal only.** The proof uses PF-261's off-diagonal positive Green sum. No diagonal series splitting is performed.
4. **No cancellation assumption.** The lower bound is valid because every massive Green entry in the chosen gauge is positive and PF-261 places the same minus sign in front of every pole.
5. **PF-264 regime is legitimate.** `a_0` is fixed once `r,s` are fixed. The witness sends both indices to infinity, exactly the two-index regime of PF-264.
6. **No endpoint claim.** The block test diverges only for `R>1`; it does not establish boundedness or unboundedness at `R=1`.
7. **No claim about the combined Robin factor.** A no-go for `\mathcal R_{s,r}^0` does not imply the same no-go for `B_{s,r}^0`, reflection transforms, or spatially separated Poisson maps.
8. **No actual-corridor/global conclusion.** Hypercycle transport, the actual `K_a` corridor, high-high shear reassembly, global weak trace class, scattering/determinant identities, zeta-zero statements, and RH all remain outside this finding.

The result would fail if the PF-261 off-diagonal mass terms had canceling signs, if PF-264's fixed-mass leading coefficient vanished on one parity, or if the quarter-order endpoint normalization changed the proportional-ray degree from `-2`. PF-261, PF-264, and PF-267 exclude all three within the stated fixed-axis model.

## Decisive next test

Do **not** spend further work trying to improve the PF-267 mass sum for the naked relative seam into a strict `R>1` separated weighted estimate; PF-268 proves that target false. Instead insert the finite-seam source factor into the **combined polar-free Robin transform and the spatially separated Poisson leg** isolated by PF-257/PF-243, and test the weighted map there. A viable theorem must show that this extra physical structure changes the fixed-pole proportional-mode `N^{-2}` floor before claiming any supercritical margin.