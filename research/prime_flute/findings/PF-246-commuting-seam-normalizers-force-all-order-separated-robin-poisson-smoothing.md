# PF-246 — commuting seam normalizers force all-order separated Robin-Poisson smoothing

**Status:** `EXACT-DERIVED + COMMUTING-CALIBRATION + ALL-ORDER-SEPARATED-SMOOTHING + POSITIVE/ROUTE-NARROWING`. PF-243 reduces the remaining high-high shear gate to one-sided separated Robin-Poisson smoothing for the **actual fixed seam**. PF-244 shows that positivity, energy contraction, spatial separation, and one-sided seam domination do not imply that smoothing abstractly, because a noncommuting seam square root can convert arbitrarily high transverse input into a cheap low mode before interior propagation. PF-245 then rules out one tempting repair: the bare actual seam square root has branch points approaching the critical strip boundary, so it has no uniform supercritical analytic strip.

There is nevertheless an exact positive calibration that sharply identifies what is missing. On any product corridor whose two seam normalizers are nonnegative **functions of the same transverse operator** `K`, the normalized Robin source maps are smoothing of *every* order across any fixed positive longitudinal separation, with constants independent of the size, softness, spectral growth, or inverse compactness of the seam forms. The proof is modewise and uses only the two Robin reflection coefficients and the scalar inequality

\[
\frac{\sqrt q}{k+q}\le \frac1{2\sqrt k}.
\]

Thus neither a lower seam coercivity bound nor complex analyticity of `Q^{1/2}` is required in the commuting calibration. [[research/prime_flute/findings/PF-236-operator-matched-seam-normalizer-preserves-dressed-variable-corridor-transfer|PF-236]]'s operator-matched seams satisfy this hypothesis exactly, so the [[research/prime_flute/findings/PF-243-fixed-seam-robin-homotopy-reduces-high-high-shear-to-one-sided-separated-poisson-smoothing|PF-243]] separated smoothing estimate holds there for arbitrary order `R`. The actual PF seam does not commute with PF-233's `K_a` after the fixed boundary compactification, so this does **not** close PF-243. It localizes the live theorem much more tightly: the missing structure is quantitative control of **spectral conversion by the normalized actual Robin coupling relative to `K_a`**, not additional scalar seam coercivity and not a supercritical analytic strip for the bare seam square root.

## Claim

Let `H` be a Hilbert space, let `K>=0` be self-adjoint, and let

\[
Q_i=q_i(K),\qquad i=0,1,
\tag{1}
\]

for nonnegative Borel functions `q_i`. Consider the product form on `L^2((0,1);H)`

\[
\mathfrak a[u]
=
\int_0^1\left(\|u_X\|^2+\|Ku\|^2\right)dX
+\|Q_0^{1/2}u(0)\|^2
+\|Q_1^{1/2}u(1)\|^2.
\tag{2}
\]

For normalized forcing from the right boundary, define the Poisson source map `P_1` weakly by

\[
\mathfrak a[P_1f,v]
=\langle f,Q_1^{1/2}v(1)\rangle.
\tag{3}
\]

Let

\[
P_Z=\mathbf 1_{[Z,\infty)}(K),\qquad Z>0,
\tag{4}
\]

and let `0<=chi<=1` be supported in

\[
0\le X\le 1-d,
\qquad 0<d<1.
\tag{5}
\]

Then for every `R>=0`, on the natural spectral/form core and hence by closure,

\[
\boxed{
\max\left\{
\|\chi^{1/2}\partial_XP_1K^RP_Z\|,
\|\chi^{1/2}KP_1K^RP_Z\|
\right\}
\le C_{R,d,Z},
}
\tag{6}
\]

where one may take

\[
\boxed{
C_{R,d,Z}
=
\frac1{\sqrt2\,(1-e^{-2Z})}
\sup_{k\ge Z} k^R e^{-dk}<\infty.
}
\tag{7}
\]

The constant is completely independent of `q_0,q_1`. The reflected statement for normalized forcing from the left boundary and a cutoff supported in `d<=X<=1` is identical.

In particular, any first-order tangential component `T` satisfying

\[
\|Tu\|\le\|Ku\|
\tag{8}
\]

at the product-form level obeys the same separated estimate with `K P_1` replaced by `T P_1`. Hence the exactly separated diagonal calibration of PF-243 has the required all-order far-leg smoothing whenever its seam forms are functions of the product transverse operator.

## 1. Joint functional calculus reduces the Robin problem to one scalar channel

Because `Q_0` and `Q_1` are functions of `K`, the entire variational problem decomposes under the spectral theorem. It is enough to fix one spectral value `k>=Z`, put

\[
q_i=q_i(k)\ge0,
\tag{9}
\]

and solve

\[
-u''+k^2u=0
\quad\text{on }0<X<1
\tag{10}
\]

with

\[
-u'(0)+q_0u(0)=0,
\qquad
u'(1)+q_1u(1)=\sqrt{q_1}\,f.
\tag{11}
\]

Here the second equation is exactly the normalized boundary forcing in (3). Write `y=1-X` and

\[
u(y)=a e^{-ky}+b e^{ky}.
\tag{12}
\]

Define the Robin reflection coefficients

\[
r_i=\frac{k-q_i}{k+q_i}.
\tag{13}
\]

Since `k>0` and `q_i>=0`,

\[
|r_i|\le1.
\tag{14}
\]

The left homogeneous Robin condition gives

\[
b=r_0e^{-2k}a,
\tag{15}
\]

while the right source condition gives

\[
\boxed{
a
=
\frac{\sqrt{q_1}}{k+q_1}
\frac1{1-r_0r_1e^{-2k}}\,f.
}
\tag{16}
\]

This is the complete two-boundary reflection series already summed exactly. No lower bound on either seam normalizer has been used.

## 2. Energy normalization cancels arbitrary seam size

Two scalar inequalities contain the whole uniformity. First,

\[
|1-r_0r_1e^{-2k}|
\ge1-e^{-2k}
\ge1-e^{-2Z}.
\tag{17}
\]

Second, arithmetic-geometric mean gives

\[
k+q_1\ge2\sqrt{kq_1},
\]

and therefore

\[
\boxed{
\frac{\sqrt{q_1}}{k+q_1}
\le\frac1{2\sqrt k}.
}
\tag{18}
\]

Combining (16)--(18),

\[
|a|
\le
\frac1{2(1-e^{-2Z})\sqrt k}|f|.
\tag{19}
\]

This bound is uniform in both Robin parameters. It remains valid when a seam is extremely soft, extremely hard, or crosses from second-order to first-order behavior with `k`. The normalized forcing `Q_1^{1/2}` and the Robin inverse `(k+q_1)^{-1}` cancel the seam scale before propagation begins.

This is precisely the mechanism absent from a bare estimate on `Q_1^{1/2}`. It is also why PF-245's complex branch structure of the bare square root is not, by itself, an obstruction to real-axis separated smoothing.

## 3. Positive separation supplies arbitrary transverse powers

On the far region `y>=d`, equation (15) and `|r_0|<=1` give

\[
|b|e^{ky}
\le |a|e^{-k(2-y)}
\le |a|e^{-ky},
\qquad 0\le y\le1.
\tag{20}
\]

Hence

\[
|u(y)|\le2|a|e^{-ky},
\qquad
|u_X(y)|\le2k|a|e^{-ky}.
\tag{21}
\]

Therefore each of the two product-energy legs satisfies

\[
\int_d^1 k^2|u(y)|^2dy
\le2k|a|^2e^{-2dk},
\tag{22}
\]

and

\[
\int_d^1 |u_X(y)|^2dy
\le2k|a|^2e^{-2dk}.
\tag{23}
\]

Using (19),

\[
\max\left\{
\|u_X\|_{L^2(d,1)},
\|ku\|_{L^2(d,1)}
\right\}
\le
\frac{e^{-dk}}{\sqrt2(1-e^{-2Z})}|f|.
\tag{24}
\]

If the boundary datum is first multiplied by `K^RP_Z`, the right side gains only `k^R`. Since

\[
\sup_{k\ge Z}k^Re^{-dk}<\infty
\tag{25}
\]

for every finite `R`, integration against the spectral measure proves (6)--(7). The left-source/right-observation case follows by reflection `X\mapsto1-X`.

The proof uses the positive physical separation `d` in an essential way. At `d=0`, the exponential factor disappears and no arbitrary high-order gain is available.

## 4. PF-236 satisfies the hypothesis exactly

PF-233's exact diagonal corridor becomes a product problem after its boundary-mass conjugation, with effective transverse operator

\[
K=K_a=T_a^{1/2}.
\tag{26}
\]

PF-236 introduces the operator-matched seam branches

\[
q_i^{\rm mat}
=K\tanh(r_iK),
\qquad r_i=\frac{w_i}{s},
\tag{27}
\]

before restoring the common boundary congruence. In the product representation these are exactly nonnegative functions of `K`, so PF-246 applies for **every** `R` and every fixed high-frequency threshold `Z>0`.

The cutoffs in PF-243 were chosen so that one source-to-observation leg is separated by a fixed positive fraction of the unit longitudinal interval. Thus, for the operator-matched calibration, the four far-leg maps required there are uniformly bounded after any power `K^R P_Z`. The first-order tangential factor used by PF-243 is controlled by the product transverse energy, so (8) transfers the estimate from `K u` to that `Y`-leg.

This is stronger than merely recovering PF-236's dressed crossing singular-value envelope. PF-236 controls the fully inverted boundary-to-boundary block; PF-246 shows that the corresponding normalized boundary-to-**interior** Poisson legs have unlimited separated high-mode smoothing before the shear derivative is inserted.

## 5. What this says about PF-244 and PF-245

PF-244 constructs a positive seam whose square root sends sparse high modes into a low mode. That mechanism is impossible under (1): a function of `K` preserves every `K`-spectral subspace, so a high-frequency input cannot reach the low-cost propagating channel before the factor `e^{-dK}` acts. PF-246 therefore identifies **mode conversion**, not seam softness, as the load-bearing difference between the positive calibration and the abstract countermodel.

PF-245 proves that the actual intrinsic seam multiplier has square-root branch points at `+-i kappa_w` with `kappa_w->1`. PF-246 never analytically continues `q_i(k)` or `sqrt(q_i(k))`; it only uses positivity on the real spectrum and the normalized scalar factor in (18). Consequently the failure of a uniform supercritical analytic strip for the bare actual seam square root does not threaten the commuting calibration.

The two negative findings and the present positive calibration together sharpen the actual-seam target. A successful proof does not need to show that the actual seam is uniformly comparable from below with the matched seam, nor that its bare square root has a wide holomorphic strip. It needs enough `K_a`-spectral locality of the **normalized Robin source/Poisson coupling** to prevent the PF-244 high-to-low leakage from defeating the real corridor propagation.

## 6. Prior art and novelty audit

Separated Robin boundary conditions, reflection coefficients, and `2x2` boundary data maps on a compact interval are classical. A directly relevant systematic reference is S. Clark, F. Gesztesy, and M. Mitrea, *Boundary Data Maps for Schrödinger Operators on a Compact Interval*, Mathematical Modelling of Natural Phenomena 5 (2010), 73--121, DOI `10.1051/mmnp/20105404`, which studies Dirichlet-to-Neumann and Robin-to-Robin maps for one-dimensional Schrödinger operators with separated boundary conditions.

The scalar ODE solution (12)--(16), spectral decomposition, and AM--GM estimate (18) are not claimed as new general operator theory. A targeted search of Robin boundary-data and interval Green-function literature found the standard surrounding machinery, not a reason to regard this elementary estimate as a new general theorem.

The project-specific contribution is the **PF calibration**: after PF-243--PF-245, the exact two-boundary calculation shows that arbitrary seam magnitude and bare square-root analyticity are irrelevant once the seam is spectrally aligned with the corridor operator, and it identifies the normalized seam-to-corridor spectral-conversion problem as the remaining local obstruction. No RH consequence or general Robin regularity theorem is claimed.

## 7. Falsification and boundary checks

1. **Commutation is essential to this proof.** If `Q_i` do not preserve the `K` spectral resolution, the scalarization leading to (16) is invalid. PF-244 gives an explicit abstract failure mode under the weaker assumptions of positivity, energy contraction, separation, and one-sided form domination.
2. **Positive separation is essential.** The factor `e^{-dk}` is what absorbs arbitrary powers of `k`; at `d=0` the statement is false for `R>0` without additional boundary regularity.
3. **The fixed high-band threshold is essential for the stated uniform reflection constant.** The factor `(1-e^{-2Z})^{-1}` becomes singular as `Z->0`; PF-243 uses the estimate only after a fixed scaled-frequency high projection.
4. **No seam coercivity is hidden.** The proof is uniform for all nonnegative scalar seam symbols `q_i(k)`, including symbols much smaller or larger than `k` on parts of the spectrum.
5. **No complex analyticity is hidden.** Equations (17)--(25) use only real positive spectral values.
6. **This is a calibration, not the actual-seam theorem.** PF-237/PF-238 show that the transported complete-lift actual seam is not the PF-236 matched functional calculus even though a useful one-sided form order survives. PF-246 does not upgrade that order to commutation or spectral locality.
7. **The shear is still absent here.** PF-243 uses this kind of separated Poisson estimate inside the exact Robin homotopy derivative. Establishing the estimate for the actual fixed seam remains necessary before the `O(beta/s)` trace bound can be concluded.
8. **Physical/global gates remain separate.** Even after the local actual-seam smoothing gate closes, the physical `P/H` recoupling, one-cusp-pant completion, neighboring-cell interactions, and PF-222 global weak-trace reassembly remain to be checked.

## Consequence for the live research line

The exactly separated diagonal corridor is now a decisive positive control: **every positive commuting seam normalizer has unlimited separated Robin-Poisson smoothing after energy normalization**. Therefore the next useful theorem should target the actual transported seam at the level where PF-244 can fail, namely spectral conversion relative to `K_a` in the normalized Robin coupling. A sufficient result could be a quantitative high-to-low off-diagonal bound, a commutator/pseudodifferential estimate strong enough to insert the exponential corridor propagator before leakage accumulates, or an equivalent microlocal locality statement for the actual Poisson source map.

This is narrower than seeking a supercritical analytic strip for `Q^{1/2}` and stronger than another one-sided form comparison. It is exactly the missing bridge between PF-238's successful dressed diagonal crossing and PF-243's all-high shear trace estimate.