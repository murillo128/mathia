# PF-237 — complete-lift seam spectral type blocks direct matched-normalizer comparison

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + SPECTRAL-TYPE-OBSTRUCTION + ROUTE-REORDERING`. PF-236 proves that the exact PF-233 variable-width corridor retains the decisive dressed `sqrt(w_1w_2)/s` crossing envelope when its two seam normalizers are built from the same effective transverse operator `K=T_a^{1/2}` as the corridor. The accepted conformal-transfer clue correctly warns that two-sided form comparison of the actual seam with that matched seam is not enough to control the off-diagonal inverse. There is a stronger reason not to pursue that comparison on the **complete lifted seam**: the two normalizers have different spectral type.

For one fixed neighboring-cuff edge, PF-233 gives `K` compact resolvent, while PF-236 defines

\[
Q_i^{\rm mat}
=B^{1/2}K\tanh((w_i/s)K)B^{1/2}.
\]

Its inverse is compact. By contrast, PF-235's complete-axis seam control is form-comparable to

\[
Q_w^{\rm axis}
=M_\tau\tanh(wM_\tau),
\qquad
M_\tau=(1-\partial_\tau^2)^{1/2}
\]

on `L^2(R,d\tau)`. The inverse of this operator is a nonzero Fourier multiplier on a nonatomic line and is not compact. PF-235's exact hypercycle-to-axis transport and the fixed `tau<->theta` compactification, when represented with their canonical boundary-density unitaries, cannot change compactness. Hence the complete lifted actual seam transported into PF-233's `L^2((0,pi),dtheta)` trace realization still has noncompact inverse and cannot be uniformly form-equivalent, or related by a boundedly invertible congruence, to `Q_i^{mat}`.

Equivalently, the mismatch has a canonical boundary-sequence witness. Translate one fixed compactly supported unit vector along the complete intrinsic Fermi seam. Its actual seam energy is unchanged. After exact transport into the compactified `theta` trace space these vectors remain orthonormal and escape toward an ideal endpoint, while their `Q_i^{mat}` energies are necessarily unbounded along a subsequence because `Q_i^{mat}` has compact inverse. Thus the complete-lift mismatch is not an `O(w_i^2)` perturbation hidden inside PF-234/PF-235; the quadratic statements there concern coefficients and seam-dependent coordinate distortion, not the global compactness class created by the corridor's endpoint potential.

This does **not** show that the actual dressed off-diagonal block fails the PF-236 singular-value envelope. It shows that a proof cannot replace the complete lifted actual seam by `Q_i^{mat}` through a global relative-form perturbation before using the rest of the corridor structure. The surviving positive possibilities are more specific: either the joint normalized corridor suppresses the endpoint-escaping seam packets strongly enough that the spectral-type mismatch disappears at the off-diagonal inverse level, or the physical closed-cuff/finite-pant trace realization must be inserted before a matched-normalizer comparison is meaningful.

## Claim

Fix one PF-233 diagonal neighboring-cuff edge with nominal corridor scale `s>0`, seam width `w>0`,

\[
H_\theta=L^2((0,\pi),d\theta),
\qquad
B=M_{a^{-1}},
\qquad
K=T_a^{1/2}.
\tag{1}
\]

Assume the canonical PF-233 bounds

\[
c_0s^2A\le T_a\le C_0s^2A,
\qquad
A=-\partial_\theta^2+\csc^2\theta,
\tag{2}
\]

so `K` has compact resolvent. Put

\[
Q^{\rm mat}
=B^{1/2}K\tanh((w/s)K)B^{1/2}.
\tag{3}
\]

Let `Q_w^{axis}` be PF-235's flat complete-axis seam form on `L^2(R,d\tau)`, and let `Q_w^{lift}` denote the actual complete lifted PF-205 hyperbolic symmetric seam transported to the same axis trace realization as in PF-235. Finally let

\[
\widehat Q_w^{\rm lift}=UQ_w^{\rm lift}U^*
\tag{4}
\]

be its representation on `H_theta` under the exact hypercycle/axis compactification with the canonical boundary-density unitary `U`. Then:

1. `(Q^{mat})^{-1}` is compact on `H_theta`;
2. `(Q_w^{axis})^{-1}` is not compact on `L^2(R,d\tau)`;
3. `(Q_w^{lift})^{-1}` and `(\widehat Q_w^{lift})^{-1}` are not compact;
4. there is no constant `c>0` such that
   \[
   \widehat Q_w^{lift}\ge_{form}cQ^{mat};
   \tag{5}
   \]
   in particular there is no uniform two-sided form equivalence between these complete-lift and matched normalizers, and no boundedly invertible `S` with `\widehat Q_w^{lift}=S^*Q^{mat}S`;
5. there is an orthonormal sequence `y_j in H_theta`, with each `y_j` in the common form core, such that
   \[
   \sup_j\widehat q_w^{lift}[y_j]<\infty
   \tag{6}
   \]
   while, after passing to a subsequence,
   \[
   q^{mat}[y_j]\longrightarrow\infty.
   \tag{7}
   \]

The sequence in (5)--(7) is obtained by translating one compactly supported boundary packet along the complete intrinsic seam and then applying the exact boundary transport. It therefore uses the canonical PF geometry rather than an arbitrary positive form.

## 1. The operator-matched seam has compact inverse

PF-233 proves that `T_a` has compact resolvent and eigenvalues

\[
\lambda_m(T_a)\asymp s^2(m+\alpha)^2,
\qquad m\to\infty.
\tag{8}
\]

Thus the eigenvalues `k_m` of `K` tend to infinity. For `r=w/s>0`, define

\[
q_r(K)=K\tanh(rK).
\tag{9}
\]

Its inverse has eigenvalues

\[
\frac1{k_m\tanh(rk_m)}\longrightarrow0.
\tag{10}
\]

Therefore `q_r(K)^{-1}` is compact. On one fixed edge, `B^{1/2}=M_{a^{-1/2}}` is bounded and boundedly invertible by PF-233's positive upper and lower width bounds. From (3),

\[
(Q^{mat})^{-1}
=B^{-1/2}q_r(K)^{-1}B^{-1/2},
\tag{11}
\]

so `(Q^{mat})^{-1}` is compact as well.

This is not merely high-frequency decay of one cross block. It says that the matched seam form has compact form-domain embedding into `H_theta`: every sequence bounded in its graph/form norm has an `H_theta`-convergent subsequence.

## 2. The complete-axis seam has noncompact inverse

PF-235 uses

\[
Q_w^{axis}=M_\tau\tanh(wM_\tau),
\qquad
M_\tau=(1-\partial_\tau^2)^{1/2}
\tag{12}
\]

on the complete axis. Under the Fourier transform this is multiplication by

\[
q_w(\xi)
=\sqrt{1+\xi^2}\,
\tanh\!\left(w\sqrt{1+\xi^2}\right).
\tag{13}
\]

Hence its bounded inverse is multiplication by

\[
m_w(\xi)=q_w(\xi)^{-1}>0.
\tag{14}
\]

Although `m_w(\xi)->0` as `|xi|->infinity`, multiplication by `m_w` on the nonatomic space `L^2(R,dxi)` is not compact. Indeed choose a bounded interval `I` on which `m_w>=epsilon>0` and split `I` into infinitely many disjoint measurable sets of positive measure. Their normalized indicator functions are orthonormal, while their images under multiplication by `m_w` remain mutually orthogonal with norms at least `epsilon`. No image subsequence can converge.

Equivalently, the noncompactness is visible before Fourier transform: if `phi in C_c^infty(R)` has unit norm and `phi_j(t)=phi(t-jR)` have disjoint supports, translation invariance gives

\[
q_w^{axis}[\phi_j]=q_w^{axis}[\phi]
\tag{15}
\]

for every `j`. The complete-axis seam form therefore has a bounded orthonormal translation sequence, which is impossible for a compact form-domain embedding.

## 3. PF-235's actual lifted seam has the same noncompactness class

PF-235 proves on the complete lifted seam control that

\[
\cosh^{-3}\rho\,Q_w^{axis}
\le_{form}
Q_w^{lift}
\le_{form}
\cosh^3\rho\,Q_w^{axis},
\qquad w=\sinh\rho.
\tag{16}
\]

Thus the two positive form norms are equivalent on the complete axis. The translated sequence from (15) is bounded for `Q_w^{lift}` as well, so the embedding of its form domain into the boundary `L^2` space is not compact. Consequently `(Q_w^{lift})^{-1}` is noncompact.

There is an even more intrinsic witness. In PF-234's complete lifted signed Fermi-area strip, the metric

\[
g=\frac{dx^2}{1+x^2}+(1+x^2)dt^2
\tag{17}
\]

has coefficients independent of the longitudinal seam coordinate `t`. Translating a compactly supported trace packet in `t` leaves the exact actual symmetric seam energy unchanged. PF-235's map `t=T_rho(tau)` and the fixed `tau<->theta` compactification are exact changes of boundary representation. Once their density factors are included, they act unitarily between the natural boundary Hilbert spaces. Unitary transport preserves compactness and orthonormality, so `(\widehat Q_w^{lift})^{-1}` is also noncompact.

The fixed compactification can make an infinite axis look like the finite coordinate interval `(0,pi)`, but it cannot convert continuous translation escape into compact resolvent by coordinate change alone.

## 4. Endpoint-escaping packets rule out direct relative-form replacement

Take one unit trace packet `phi` compactly supported in the intrinsic complete seam coordinate and translate it toward `t=+infinity`. After the exact density-unitary transport of PF-235, write the images as `y_j in H_theta`. For each finite `j`, `y_j` is smooth and supported away from the ideal endpoint, so it lies in the form core of both normalizers. The supports become disjoint after sufficiently separated translations, hence `y_j` are orthonormal, and exact seam translation invariance gives the uniform bound (6).

Suppose, contrary to (5), that

\[
\widehat Q_w^{lift}\ge_{form}cQ^{mat}
\tag{18}
\]

for some `c>0`. Then (6) would make `q^{mat}[y_j]` uniformly bounded. But `(Q^{mat})^{-1}` is compact, so boundedness in the `Q^{mat}` form norm would force an `H_theta`-convergent subsequence. This contradicts orthonormality. Therefore (18) is impossible.

The same argument gives the quantitative qualitative witness (7): if `q^{mat}[y_j]` were bounded along the whole sequence, compactness would again be contradicted; choose a subsequence along which it tends to infinity.

Likewise, a boundedly invertible congruence

\[
\widehat Q_w^{lift}=S^*Q^{mat}S
\tag{19}
\]

would imply

\[
(\widehat Q_w^{lift})^{-1}
=S^{-1}(Q^{mat})^{-1}S^{-*},
\tag{20}
\]

which is compact, contradicting section 3. The obstruction is therefore invariant under bounded changes of boundary coordinates; it is not cured by choosing a more convenient equivalent trace norm.

Geometrically, the packets `y_j` accumulate toward `theta=pi` (or toward `theta=0` for translations in the opposite direction). They are cheap for the complete seam because that seam is longitudinally translation invariant. The matched normalizer instead inherits PF-233's compact-resolvent transverse structure and cannot admit infinitely many orthogonal packets of uniformly bounded energy. This is the exact global representation mismatch left invisible by the `1+O(w^2)` local coefficient comparisons.

## 5. What the obstruction does and does not kill

The result kills one tempting completion of the accepted conformal-transfer clue:

\[
Q_w^{lift}\asymp Q^{mat}
\quad\Longrightarrow\quad
D_{21}^{act}\approx D_{21}^{mat}.
\tag{21}
\]

The premise cannot hold on the complete lifted trace space, even before asking whether form comparison is strong enough to control an off-diagonal inverse. In particular, PF-234's quadratic intrinsic seam comparison and PF-235's quadratic seam-dependent coordinate defect must not be extrapolated into a global relative-form comparison with PF-236's matched normalizer.

The result does **not** prove that

\[
s_j(D_{21}^{act})
\lesssim
\frac{\sqrt{w_1w_2}}s\,\Phi(js)
\tag{22}
\]

is false. The complete corridor has its own endpoint barrier: the same compactification that creates cheap translated seam packets also places them in the large `csc^2(theta)` region of PF-233's transverse energy, where cross-corridor transfer is strongly suppressed. A joint seam-plus-corridor argument can therefore succeed even though the seam forms alone are not relatively comparable.

There are now two honest ways forward, and they must not be conflated. One is to prove the off-diagonal inverse estimate directly by splitting central and endpoint trace sectors, using PF-233/PF-236 functional calculus for the central transfer and the corridor's endpoint suppression against the escaping seam packets. The other is to introduce the actual closed-cuff/finite-pant boundary realization before comparing normalizers; periodic/finite boundary conditions remove the complete-axis translation escape, but then their growing cuff length and the physical trace maps must be controlled quantitatively. Either route still has to face PF-232 shear, physical `P/H` recoupling, finite-pant completion where not already included, and PF-222 global reassembly.

## 6. Prior-art and novelty audit

The functional-analytic ingredients are classical. Compact resolvent is equivalent to compactness of the associated form-domain embedding for a positive self-adjoint operator; bounded invertible left/right factors preserve compactness; and a nonzero multiplication operator on a nonatomic `L^2` space is noncompact. Fourier diagonalization of translation-invariant strip and cylinder boundary operators is likewise standard. The general Dirichlet-to-Neumann and hyperbolic-cylinder literature already cited in PF-234 provides the surrounding context.

A structure-directed literature audit for compact-resolvent/form-comparison criteria, multiplication-operator compactness, and Dirichlet-to-Neumann operators on cylindrical/noncompact boundary models did not identify a theorem whose content is the PF-specific statement here. No novelty is claimed for any of those general ingredients. The project-specific result is their exact application to the **PF-235 complete lifted actual seam versus the PF-236 operator-matched normalizer**, showing that the two cannot be globally relatively comparable and that the order of the remaining transport argument must change. The proof above is self-contained from PF-233--PF-236 and introduces no new external theorem dependency.

## 7. Falsification and boundary checks

1. The obstruction concerns the **complete lifted seam control**. The actual closed decomposition cuff is periodic and has discrete longitudinal spectrum; PF-237 does not claim that its seam inverse is noncompact.
2. Equation (16) is used only at the complete lifted/control stage explicitly identified by PF-235. It is not silently promoted to the finite one-cusp pant.
3. Compactness is asserted after the canonical boundary-density unitaries. An arbitrary unweighted substitution between `tau` and `theta` is not the Hilbert-space identification used here.
4. PF-237 rules out a global lower form bound of the actual complete seam by `Q^{mat}` and hence two-sided equivalence. It does not rule out one-sided estimates in the opposite direction or estimates after spectral/localized projection.
5. The endpoint packet sequence is not by itself a counterexample to the dressed cross block. To refute the PF-236 envelope one would still need to show that the corresponding actual `D_{21}` stays too large after the corridor transfer is included.
6. Conversely, proving that endpoint packets are killed by the corridor is not enough for the physical theorem unless the central sector, shear, `P/H` projections, pant completion, and global nested-cut reassembly are all controlled at their stated scales.
7. Nothing here proves wave-operator equivalence, determinant/resonance control, a prime/clone separator, a zeta-zero statement, or RH.

## Consequences for the research line

The actual-seam gate is narrower but not closed. Do **not** spend the next step trying to upgrade PF-234/PF-235 into `Q_act asymp Q_mat` on the complete lift; spectral type makes that impossible. Instead test the normalized **joint** operator.

The cleanest next local theorem is an endpoint/central decomposition in the common trace realization. It should show either that the endpoint-escaping packet sector contributes a singular-value tail below the PF-236 `sqrt(w_1w_2)/s` envelope because the PF-233 cross-DtN barrier overwhelms the cheap seam energy, leaving a compact central sector where matched-normalizer perturbation is legitimate, or produce an actual normalized packet for which that compensation fails. A finite/periodic physical trace reduction is an alternative only if its constants are tracked strongly enough to replace, rather than hide, the complete-axis obstruction.