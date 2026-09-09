# PF-243 — fixed-seam Robin homotopy reduces high-high shear to one-sided separated Poisson smoothing

**Status:** `EXACT-DERIVED + VARIATIONAL-IDENTITY + LOCALIZED-POISSON-FACTORIZATION + CONDITIONAL-TRACE-REDUCTION + POSITIVE/ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-240-total-one-scaled-boundary-derivative-is-the-sharp-high-high-shear-trace-threshold|PF-240]] reduces the last local hypercycle-shear obstruction to more than one total scaled boundary derivative for the high-high actual-seam-normalized Schur difference. [[research/prime_flute/findings/PF-241-scaled-tangential-blowup-turns-the-shear-interior-into-a-uniform-long-strip-family|PF-241]] removes shrinking-width ellipticity loss by passing to a uniform unit-width long strip, and [[research/prime_flute/findings/PF-242-hypercycle-shear-is-exponentially-local-in-poschl-teller-mode-index|PF-242]] proves that the direct shear coefficient itself is exponentially local in the exact Pöschl--Teller mode index. A remaining difficulty is that asking directly for weighted regularity of the **full Schur difference** still mixes the perturbation, the Robin seam, and propagation from both boundaries.

With the actual [[research/prime_flute/findings/PF-238-one-sided-seam-domination-closes-complete-lift-dressed-diagonal-transfer|PF-238]] seam held fixed, that difficulty can be separated exactly. The Robin-normalized Schur family is norm differentiable along the shear homotopy, and its derivative is an Alessandrini-type interior pairing in which the reciprocal-prime factor appears **before** any operator inversion:

\[
\boxed{
\langle g,\dot D_t f\rangle
=-\dot q_t[P_t f,P_t g].
}
\tag{1}
\]

In PF-241's scaled coordinates this derivative factors through the two bulk energy components of the seam-normalized Robin Poisson solutions. Splitting the interior in the transverse crossing variable `X` then gives two exact pieces. On the left piece, the solution sourced from boundary 2 is observed a fixed positive `X`-distance from its forcing boundary; on the right piece, the solution sourced from boundary 1 is observed a fixed positive distance from its forcing boundary.

This yields a sharper sufficient target than regularizing the whole Schur map at once. For any fixed high cutoff `Z`, it is enough to prove **one-sided separated-Poisson smoothing of order `R>1`** on those two pieces. PF-233's one-dimensional scaled mode count then makes each piece trace class with norm `O(beta/s)`, and [[research/prime_flute/findings/PF-239-reciprocal-prime-shear-makes-critical-band-leakage-absolutely-trace-summable|PF-239]]'s reciprocal-prime weight makes the family absolutely trace summable.

The separated-Poisson estimate itself is not proved here. In particular, the Hardy ends and the actual nonlocal complete-lift seam remain genuine uniformity gates. The result is an exact reduction showing that no regularity of the near-forcing-boundary leg is needed: all required derivatives may be charged to the boundary leg that is spatially separated from its forcing boundary.

## Claim

Work in the fixed boundary coordinates used by PF-238--PF-240. Let `Q=diag(Q_1,Q_2)>0` be the **same actual complete-lift seam form for every `t`**. Let `q_t`, `0<=t<=1`, be PF-241's long-strip shear homotopy on

\[
\Omega_s=(0,1)_X\times(0,\pi/s)_Y,
\]

written as

\[
q_t[u]
=\int_{\Omega_s}
\left(
|u_X|^2+|\mathcal E_tu|^2+V_s|u|^2
\right)dX\,dY,
\qquad
\mathcal E_tu:=\mathcal T_su-t\mathsf b_su_X,
\tag{2}
\]

where

\[
\mathcal T_s=A_s(\partial_Y+C_s),
\qquad
\|\mathsf b_s\|_\infty\le\beta.
\tag{3}
\]

All boundary mass/unitary transports are fixed in `t`; in particular no square root of a `t`-dependent congruent seam is introduced.

Let `gamma` be the two-boundary trace and set

\[
a_t[u,v]
:=q_t[u,v]
+\langle Q^{1/2}\gamma u,Q^{1/2}\gamma v\rangle.
\tag{4}
\]

For normalized boundary data `f`, define the Robin Poisson solution `P_tf` variationally by

\[
\boxed{
a_t[P_tf,v]
=\langle f,Q^{1/2}\gamma v\rangle
\quad\text{for every form-domain test }v.
}
\tag{5}
\]

Then

\[
Q^{1/2}\gamma P_tf
=Q^{1/2}(\Lambda_t+Q)^{-1}Q^{1/2}f
=:D_tf,
\tag{6}
\]

so `D_t` is exactly PF-240's normalized Schur family. Moreover:

1. `t -> D_t` is norm differentiable on the normalized boundary Hilbert space;
2. for all boundary data `f,g`, equation (1) holds, where
   \[
   \boxed{
   \dot q_t[u,v]
   =-\langle M_{\mathsf b_s}u_X,\mathcal E_tv\rangle_{L^2(\Omega_s)}
    -\langle \mathcal E_tu,M_{\mathsf b_s}v_X\rangle_{L^2(\Omega_s)};
   }
   \tag{7}
   \]
3. the normalized Poisson solutions satisfy
   \[
   q_t[P_tf]\le a_t[P_tf]\le\|f\|^2,
   \tag{8}
   \]
   and hence
   \[
   |\langle g,\dot D_tf\rangle|
   \le2\beta\,\|f\|\,\|g\|;
   \tag{9}
   \]
4. equation (7) admits an exact `X`-localized factorization described below;
5. that factorization reduces PF-240's high-high trace estimate to one-sided separated-Poisson estimates of any fixed order `R>1`.

## 1. The fixed-seam variational derivative is exact

The form domain of `q_t` is independent of `t`: the shear enters only through the bounded multiplier `\mathsf b_s` in `\mathcal E_t`. PF-232/PF-241 give uniform form equivalence for `beta<1`, and directly from (2),

\[
|\dot q_t[u,v]|
\le2\beta\,q_t[u]^{1/2}q_t[v]^{1/2}.
\tag{10}
\]

The boundary term in (4) is independent of `t`. Subtracting the variational equations for `P_{t+h}f` and `P_tf`, using (10) and the polynomial dependence of `q_t` on `t`, gives

\[
\|P_{t+h}f-P_tf\|_{a_t}=O(|h|\beta)\|f\|.
\tag{11}
\]

The same difference-quotient equation converges in the energy norm to the unique `\dot P_tf` satisfying

\[
a_t[\dot P_tf,v]
=-\dot q_t[P_tf,v].
\tag{12}
\]

The estimate is uniform for `\|f\|<=1`, so the induced boundary derivative is an operator-norm derivative.

Equation (8) follows without any inverse estimate for `Q`. Indeed (5) with `v=P_tf` gives

\[
a_t[P_tf]=\langle f,D_tf\rangle,
\]

while the boundary term in `a_t` is `\|D_tf\|^2`; Cauchy--Schwarz first gives `\|D_tf\|<=\|f\|` and then (8).

Differentiate

\[
\langle g,D_tf\rangle
=a_t[P_tf,P_tg]
\]

and use (12) for both differentiated solution terms. The two solution derivatives cancel the corresponding `a_t` terms, leaving exactly (1). Thus no formal derivative of an unbounded inverse and no derivative of `Q^{1/2}` is required.

## 2. The derivative factors through two contractive bulk energy maps

Let `J_1,J_2` inject one-boundary data into the two-boundary normalized space. For a bounded cutoff `0<=chi<=1` depending only on `X`, define

\[
X_{t,j}^{\chi}f
:=\chi^{1/2}\partial_XP_tJ_jf,
\qquad
Y_{t,j}^{\chi}f
:=\chi^{1/2}\mathcal E_tP_tJ_jf.
\tag{13}
\]

By (8),

\[
\|X_{t,j}^{\chi}\|\le1,
\qquad
\|Y_{t,j}^{\chi}\|\le1.
\tag{14}
\]

Let `\dot D_{t,21}^{\chi}` denote the contribution to the `2<-1` block obtained by inserting `chi` in the integral (7). Then the sesquilinear identity (7) is exactly the bounded-operator factorization

\[
\boxed{
\dot D_{t,21}^{\chi}
=-(X_{t,2}^{\chi})^*M_{\mathsf b_s}Y_{t,1}^{\chi}
 -(Y_{t,2}^{\chi})^*M_{\mathsf b_s}X_{t,1}^{\chi}.
}
\tag{15}
\]

In particular

\[
\|\dot D_{t,21}^{\chi}\|\le2\beta.
\tag{16}
\]

PF-239's `O(beta)` normalized-resolvent stability is therefore reproduced here by a more informative identity: the small parameter sits in one explicit interior multiplier, while every other factor is an energy contraction. The gain of (15) is not a better unweighted norm; it is that boundary regularity can now be sought on individual Poisson legs before the two legs are paired.

## 3. A fixed `X` partition makes one leg separated on every term

Choose smooth nonnegative `chi_L,chi_R` with

\[
\chi_L+\chi_R=1,
\qquad
\operatorname{supp}\chi_L\subset\{X<2/3\},
\qquad
\operatorname{supp}\chi_R\subset\{X>1/3\}.
\tag{17}
\]

Then

\[
\dot D_{t,21}
=\dot D_{t,21}^{L}+\dot D_{t,21}^{R}
\tag{18}
\]

exactly, with no IMS or cutoff-derivative error because the partition is inserted only in the bilinear integral (7).

On the `L` contribution, the `j=2` Poisson solution is sampled at distance at least `1/3` from boundary `X=1`, where its external source is applied. On the `R` contribution, the `j=1` solution is sampled at distance at least `1/3` from boundary `X=0`.

This statement is only geometric separation of the **source location**. It does not yet assert smoothing: the Robin solution remains globally coupled and the actual seam may feed nonlocal boundary information back into the corridor. The point of the partition is to identify exactly which source-to-bulk maps need a uniform theorem.

## 4. One-sided separated smoothing of order greater than one closes the high-high shear block

Let

\[
K=K_a,
\qquad
P_Z=\mathbf1_{(Z,\infty)}(K),
\qquad Z>0,
\tag{19}
\]

as in PF-240. Fix any `R>1`. Suppose the following **separated Robin-Poisson estimates** hold uniformly for `0<=t<=1` and on the canonical tail:

\[
\boxed{
\|X_{t,2}^{L}K^RP_Z\|
+\|Y_{t,2}^{L}K^RP_Z\|
\le C_{R,Z},
}
\tag{20}
\]

and

\[
\boxed{
\|X_{t,1}^{R}K^RP_Z\|
+\|Y_{t,1}^{R}K^RP_Z\|
\le C_{R,Z}.
}
\tag{21}
\]

No weighted estimate is assumed for the near-forcing-boundary maps `j=1` on `L` or `j=2` on `R`; their unweighted contraction bounds (14) are enough.

Integrating (15) in `t` and using (20) gives, for

\[
T_L:=\int_0^1\dot D_{t,21}^{L}\,dt,
\qquad
T_R:=\int_0^1\dot D_{t,21}^{R}\,dt,
\tag{22}
\]

\[
\|K^RP_ZT_LP_Z\|\le C\beta,
\qquad
\|P_ZT_RP_ZK^R\|\le C\beta.
\tag{23}
\]

Since

\[
D_{1,21}-D_{0,21}=T_L+T_R,
\tag{24}
\]

the high-high correction is a sum of one output-smoothed and one input-smoothed operator.

PF-233's scaled spectral law implies for every `R>1`

\[
\boxed{
\|P_ZK^{-R}\|_1
=\sum_{k_m>Z}k_m^{-R}
\le C_{R,Z}s^{-1}.
}
\tag{25}
\]

Therefore Schatten ideality can be charged entirely to the separated leg:

\[
\begin{aligned}
\|P_ZT_LP_Z\|_1
&\le
\|P_ZK^{-R}\|_1\,
\|K^RP_ZT_LP_Z\|,\\
\|P_ZT_RP_Z\|_1
&\le
\|P_ZT_RP_ZK^R\|\,
\|K^{-R}P_Z\|_1.
\end{aligned}
\tag{26}
\]

Combining (23)--(26),

\[
\boxed{
\left\|P_Z(D_{1,21}-D_{0,21})P_Z\right\|_1
\le C_{R,Z}\frac{\beta}{s}.
}
\tag{27}
\]

Thus (20)--(21) are sufficient to close PF-240's entire high-high shear gate. PF-239 then supplies the arithmetic reassembly:

\[
\sum_n\delta_n
\left\|P_Z(D_{n,1}-D_{n,0})_{21}P_Z\right\|_1
<\infty,
\tag{28}
\]

because `\delta_n\beta_n/s_n` is bounded by a constant multiple of `1/(P_nP_{n+1})`.

The numerical threshold has moved in a useful way. PF-240 asks for total boundary smoothing `r_1+r_2>1` on the full high-high Schur difference. PF-243 instead permits all Schatten regularity to sit on **one spatially separated leg at a time**, at the cost of asking for order `R>1` there. A fixed positive propagation distance is precisely where arbitrarily high tangential smoothing is plausible; no corresponding claim is needed at the forcing boundary itself.

## 5. Relation to PF-242 and prior art

PF-242 supplies additional structure but is not used to prove (20)--(21). Its exact Jacobi calculation shows that the direct multiplier `\mathsf b_s` cannot couple modes across a fixed scaled-frequency gap except at super-algebraically small cost. In (15), however, the multiplier sits between full Robin Poisson maps. The actual missing theorem is therefore now even more localized: prove that the **separated source-to-bulk energy maps** retain enough `K_a` smoothing uniformly through the long-strip/Hardy/seam geometry.

The variational identity itself is classical in spirit. Isaev and Novikov, *Stability estimates for determination of potential from the impedance boundary map*, arXiv:1112.3728, extend the Alessandrini identity to impedance/Robin-to-Robin boundary data. Uniform Robin regularity on bounded-geometry manifolds is also classical under appropriate strong ellipticity/Shapiro--Lopatinski hypotheses; see Große and Nistor, *Uniform Shapiro-Lopatinski conditions and boundary value problems on manifolds with bounded geometry*, Potential Analysis 53 (2020), 407--447, DOI `10.1007/s11118-019-09774-y`, arXiv:1703.07228.

Neither source supplies (20)--(21) for the PF family. The PF strip length grows like `pi/s`, the tangential operator carries inverse-square Hardy endpoints, and `Q` is the actual complete-lift nonlocal seam whose inverse compactness properties differ sharply from the matched confining model. The fixed-domain off-diagonal DtN smoothing literature already audited in PF-240 likewise does not provide this scaled uniform statement.

No novelty is claimed for Alessandrini identities, form differentiation, spatial partitions, or the elementary Schatten factorization in isolation. The project-specific delta is the exact combination of the **fixed actual seam**, PF-241 shear form, `X`-localized Robin-Poisson factorization, and PF-233 one-dimensional mode count to replace a global two-sided Schur regularity problem by two one-sided separated-source estimates.

## 6. Falsification and boundary checks

1. **The seam must stay fixed along the homotopy.** If `Q=Q_t` varies, (1) acquires an additional boundary-form derivative. PF-243 does not justify dropping such a term.
2. **No commuting of `Q` and `K_a`.** Equations (20)--(21) are statements about the actual seam-normalized Poisson maps. They do not replace `Q` by PF-236's matched seam or move `K_a` through `Q^{1/2}`.
3. **No smoothing is inferred from source separation alone.** The partition only identifies the maps on which smoothing would suffice. A counterexample to (20) or (21) may come from Hardy-end escape or nonlocal seam feedback.
4. **PF-242 is coefficient locality, not Poisson locality.** Its exponential Jacobi decay cannot be substituted for (20)--(21) without proving stability through the full Robin problem.
5. **Order `R>1` is deliberate.** One-sided trace factorization uses `P_ZK^{-R} in S_1`, whose one-dimensional threshold is `R>1`. At `R=1` this particular one-sided route reaches only weak trace class, matching PF-240's critical counting law.
6. **High cutoff remains fixed in scaled frequency.** No physical Fourier cutoff or unscaled rank truncation is substituted for `P_Z`.
7. **No global endpoint theorem follows.** Physical `P/H` recoupling, finite-pant completion, neighboring-cell coupling, the nested PF-222 weak-trace reassembly, wave/scattering theory, determinants/resonances, prime/clone separation, zeta zeros, and RH remain outside the result.

## Consequences for the research line

The local shear frontier is now a **separated Robin-Poisson regularity problem**, not a generic regularity problem for the full Schur difference. A positive proof of (20)--(21) for one `R>1` immediately gives the `O(beta/s)` trace bound needed for the complete high-high shear correction and moves the smooth route to physical `P/H` recoupling and finite-pant completion.

A useful negative result must now be comparably specific: exhibit normalized high-frequency boundary data for which a source-to-bulk energy map observed a fixed positive `X`-distance from its forcing boundary fails every uniform `K_a^R` estimate with `R>1`. Failure of near-boundary regularity, generic mode mixing, or shrinking-width ellipticity no longer addresses the reduced gate.