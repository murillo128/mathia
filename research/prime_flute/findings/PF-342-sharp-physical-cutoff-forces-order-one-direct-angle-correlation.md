# PF-342 — adjacent modes across the sharp physical cutoff force order-one direct-angle correlation

**Status:** `EXACT-DERIVED + SHARP-CUTOFF-OBSTRUCTION + NONCOMPACT-DIRECT-ANGLE + DECISIVE-NEGATIVE`.

PF-318/PF-320 leave the direct physical `L/H` channel open through a local Hilbert--Schmidt estimate, while PF-321 shows that any fixed superlinear seam-scale decay of the local reference angle would be more than enough. PF-341 closes a different route: fixed low modes already show that the normalized pant insertion is not asymptotically translation-local. That low/low obstruction does not by itself lower-bound the completed low/high angle.

There is, however, a direct low/high witness already inside the **sharp fixed physical cutoff** used by PF-317/PF-325/PF-326. If a cuff has period `L` and the physical cutoff is `kappa>0`, put

\[
N=\left\lfloor\frac{\kappa L}{2\pi}\right\rfloor,
\qquad
\xi_L=\frac{2\pi N}{L},
\qquad
\xi_H=\frac{2\pi(N+1)}{L}.
\]

Then `xi_L` is retained low and `xi_H` is high, but

\[
\xi_H-\xi_L=\frac{2\pi}{L}\longrightarrow0.
\]

On the collapsing finite--finite corridor of one tail pant, the two corresponding normalized cosine traces are therefore almost the same function. Their sum is nonzero at the unique collapsing corridor and costs order `1/(sL)` in the pant DtN energy, while their difference carries the extra frequency gap `2pi/L` and costs only

\[
O\!\left(1+\frac1{sL^3}\right).
\]

Because `L\to\infty` and PF-341 gives `sL\to0`, polarization forces the low/high pant matrix element itself to have the same leading scale as the two diagonal energies:

\[
\operatorname{Re}\langle c_H,A c_L\rangle
\gtrsim \frac1{sL},
\qquad
\mathcal E_A(c_L)+\mathcal E_A(c_H)
\lesssim \frac1{sL}.
\]

Zero twist gives the same sign on the two pants adjacent to a cuff. In the symmetric seam-parity channel their contributions therefore add rather than cancel. The symmetric seam energy is only `O(w_n)` on this fixed physical band and is negligible compared with the pant scale, which diverges because `s_jL_n\to0`.

Consequently the raw total positive form `Q+Lambda_E` has a low/high **canonical correlation bounded below by a fixed positive constant** on every sufficiently far tail module. Since seam normalization is block diagonal for the physical `L/H` split, the direct angle of

\[
I+K
=Q^{-1/2}(Q+\Lambda_E)Q^{-1/2}
\]

has the same canonical correlations. Choosing modules separated by at least three indices makes these witnesses energy-orthogonal because PF-214's exterior precision is block Jacobi. Arbitrarily large finite sections therefore contain arbitrarily many singular values bounded below by the same constant.

Thus the canonical direct angle `Z_{LH}` is **not compact** on any finite-section-compatible limiting realization. In particular it cannot belong to `\mathcal S_{1,\infty}`. The PF-318 Hilbert--Schmidt route and the PF-321 superlinear-angle route are not merely unproved for the current sharp physical split; they are impossible.

## Claim

Fix the canonical sharp physical cutoff `kappa>0` from PF-317/PF-325. On a tail cuff module `n`, let `L_n` denote its physical period and set

\[
N_n=\left\lfloor\frac{\kappa L_n}{2\pi}\right\rfloor,
\qquad
\alpha_n=\frac{2\pi N_n}{L_n},
\qquad
\beta_n=\frac{2\pi(N_n+1)}{L_n}.
\tag{1}
\]

For all sufficiently large `n`, `N_n\ge1`, and

\[
0<\alpha_n\le\kappa<\beta_n\le\kappa+\frac{2\pi}{L_n}.
\tag{2}
\]

Use the normalized real Fourier traces

\[
c_{n,L}(t)=\sqrt{\frac2{L_n}}\cos(\alpha_nt),
\qquad
c_{n,H}(t)=\sqrt{\frac2{L_n}}\cos(\beta_nt),
\tag{3}
\]

with origin at the finite--finite common-perpendicular foot. By the PF-325/PF-326 cutoff convention, `c_{n,L}` lies in the retained nonconstant physical-low sector and `c_{n,H}` lies in the physical-high sector.

Let `A(s,L)` be the positive shifted self-DtN form of one PF-205 one-cusp pant on a finite boundary of period `L`, with the other finite boundary datum zero, in the geometry used by PF-341. Assume the finite--finite core distance is `s` and `L\to\infty`, `sL\to0`. Then there are constants depending only on the fixed cutoff and the canonical tail geometry such that

\[
\boxed{
\operatorname{Re}\langle c_H,A(s,L)c_L\rangle
\ge \frac{c}{sL},
}
\tag{4}
\]

and

\[
\boxed{
\langle c_L,A(s,L)c_L\rangle
+\langle c_H,A(s,L)c_H\rangle
\le \frac{C}{sL}
}
\tag{5}
\]

for all sufficiently large tail pants.

Let `Lambda_n^(+)` denote PF-340's symmetric seam-parity self response on cuff module `n`, the average of the two adjacent pant self blocks. Put

\[
D_n:=\frac1{L_n}\left(\frac1{s_{n-1}}+\frac1{s_n}\right).
\tag{6}
\]

Then

\[
\boxed{
\operatorname{Re}\langle c_{n,H},\Lambda_n^{(+)}c_{n,L}\rangle
\ge cD_n,
}
\tag{7}
\]

while

\[
\boxed{
\langle c_{n,L},\Lambda_n^{(+)}c_{n,L}\rangle
+
\langle c_{n,H},\Lambda_n^{(+)}c_{n,H}\rangle
\le CD_n.
}
\tag{8}
\]

Moreover `D_n\to\infty`. In the symmetric parity channel the seam form satisfies, uniformly at the two frequencies in (1),

\[
q_+(\xi,w_n)=\sqrt{1+\xi^2}\,
\tanh\!\left(w_n\sqrt{1+\xi^2}\right)
=O_\kappa(w_n),
\tag{9}
\]

so adding `Q_n` to the two diagonal energies does not alter their scale and creates no low/high cross term. Hence there is a fixed `rho_0>0` such that the scalar canonical correlation of the raw total form `Q+Lambda_E` between the symmetric-parity vectors `c_{n,L}` and `c_{n,H}` obeys

\[
\boxed{
\rho_n
:=
\frac{
|\langle c_{n,H},\Lambda_n^{(+)}c_{n,L}\rangle|
}{
\bigl\langle c_{n,L},(Q_n+\Lambda_n^{(+)})c_{n,L}\bigr\rangle^{1/2}
\bigl\langle c_{n,H},(Q_n+\Lambda_n^{(+)})c_{n,H}\bigr\rangle^{1/2}
}
\ge\rho_0.
}
\tag{10}
\]

Finally choose any tail subsequence `n_1<n_2<...` with `n_{j+1}-n_j\ge3`. On every finite canonical section containing the first `M` selected modules, restrict the raw low and high energy spaces to

\[
E_M=\operatorname{span}\{c_{n_j,L}^{(+)}:1\le j\le M\},
\qquad
F_M=\operatorname{span}\{c_{n_j,H}^{(+)}:1\le j\le M\},
\tag{11}
\]

where `(+ )` means the symmetric two-face embedding. PF-214's one-step module support makes the restricted diagonal energies and mixed form block diagonal across `j`. The restricted canonical-correlation operator therefore has `M` singular values at least `rho_0`.

If `T_raw` denotes the full raw canonical correlation of `Q+Lambda_E`, the restricted correlation is

\[
X_M^*T_{\rm raw}Y_M
\tag{12}
\]

for isometric embeddings `X_M,Y_M` obtained from the restricted diagonal energy forms. Hence singular-value monotonicity under two-sided isometric compression gives

\[
\boxed{
s_M(T_{\rm raw})\ge\rho_0}
\tag{13}
\]

for every `M` on sufficiently large finite sections. Block-diagonal congruence by `Q^{-1/2}` preserves canonical correlations because `Q` reduces the physical `L/H` split. Thus the same statement holds for PF-317's direct angle `Z_{LH}`. No compact finite-section-compatible limit is possible.

## 1. One pant: the cutoff-straddling difference is cheaper by two powers of `L`

Suppress the module index. Write

\[
\delta:=\beta-\alpha=\frac{2\pi}{L}
\tag{14}
\]

and form

\[
g_+=\frac{c_L+c_H}{\sqrt2},
\qquad
g_-=\frac{c_H-c_L}{\sqrt2}.
\tag{15}
\]

PF-341 gives, after the canonical seam cut, a growing finite--finite corridor with ray length `ell(t)` satisfying

\[
c_0s\cosh t\le\ell(t)\le C_0s\cosh t
\tag{16}
\]

on `|t|\le T_s`, together with a uniform logarithmic-derivative bound for `ell` on a slightly shortened corridor. The same geometry is independent of the boundary Fourier index.

Because `alpha,beta` stay in a fixed compact physical-frequency interval, choose a fixed `t_0>0`, depending only on `kappa`, such that both cosines in (3) are positive and bounded away from zero on `|t|\le t_0`. Then

\[
|g_+(t)|^2\ge \frac{c}{L}
\qquad(|t|\le t_0).
\tag{17}
\]

The one-dimensional conductance lower bound along each corridor ray, exactly as in PF-341, gives

\[
\mathcal E_A(g_+)
\ge
c\int_{-t_0}^{t_0}\frac{|g_+(t)|^2}{s\cosh t}\,dt
\ge\frac{c'}{sL}.
\tag{18}
\]

For the difference, the mean-value theorem in the frequency variable gives

\[
|g_-(t)|
\le
\frac{C\delta |t|}{\sqrt L},
\tag{19}
\]

and

\[
|g_-'(t)|
\le
\frac{C\delta(1+|t|)}{\sqrt L}
\tag{20}
\]

throughout the corridor. Use PF-341's raywise trial

\[
u(t,r)=g_-(t)\left(1-\frac r{\ell(t)}\right).
\tag{21}
\]

The singular transverse term obeys

\[
\int_{-T_s}^{T_s}
\frac{|g_-(t)|^2}{s\cosh t}\,dt
\le
\frac{C\delta^2}{sL}
\int_{\mathbb R}t^2\operatorname{sech}t\,dt
\le\frac{C}{sL^3}.
\tag{22}
\]

The tangential and positive-shift terms are nonsingular. PF-216/PF-341 give `s\int_{-T_s}^{T_s}\cosh t\,dt=O(1)` and `T_s=O(L)` on the canonical prime tail. Equations (19)--(20), together with the trivial fixed-frequency bounds away from the corridor center, therefore make their total contribution `O(1)`.

Outside a slightly shortened collapsing corridor, the one-cusp pant is covered by `O(L)` unit-scale boundary charts with bounded overlap plus the standard cusp chart, exactly as in PF-341. A normalized fixed-physical-frequency trace has amplitude and tangential derivative `O(L^{-1/2})` there, so the same fixed-cutoff extension argument costs `O(1)`. Thus

\[
\boxed{
\mathcal E_A(g_-)
\le C\left(1+\frac1{sL^3}\right).
}
\tag{23}
\]

Since `sL\to0` and `L\to\infty`,

\[
1+\frac1{sL^3}
=o\!\left(\frac1{sL}\right).
\tag{24}
\]

Polarization now gives

\[
\mathcal E_A(g_+)-\mathcal E_A(g_-)
=2\operatorname{Re}\langle c_H,Ac_L\rangle,
\tag{25}
\]

so (18)--(24) prove (4).

For either individual mode `c=c_L` or `c_H`, use the same raywise linear trial. On the fixed physical band,

\[
|c(t)|^2+|c'(t)|^2\le \frac{C_\kappa}{L}.
\]

The corridor singular term is `O(1/(sL))`, the remaining corridor terms are `O(1)`, and the noncollapsing completion is `O(1)`. Hence

\[
\mathcal E_A(c)\le C\left(1+\frac1{sL}\right)
\le\frac{C'}{sL}
\tag{26}
\]

once `sL<1`. This proves (5).

The mechanism is sharper than a generic statement that the pant DtN map is non-diagonal in Fourier modes. The relevant frequency separation is exactly one lattice step, `2pi/L`, so the high vector lies on the opposite side of the **fixed physical cutoff** while becoming asymptotically indistinguishable from the low vector on every fixed physical corridor window.

## 2. The two adjacent pants have the same sign and the seam energy is negligible

PF-340 identifies the symmetric face-parity self response on module `n` as the average of the two adjacent pant self blocks. Zero twist identifies the same physical Fourier origin at the finite--finite seam foot on both pant faces. Therefore (4) applies on both sides with the **same positive sign**, using `s=s_{n-1}` and `s=s_n`.

This gives (7), while applying (5) twice gives (8), with harmless fixed factors from the symmetric two-face normalization absorbed into the constants.

PF-341 records on the canonical tail

\[
s_j=O(P_j^{-0.475}),
\qquad
L_j=O(\log P_j),
\qquad
s_jL_j\to0.
\tag{27}
\]

Adjacent cuff periods and prime labels are comparable at this coarse scale, hence each term in (6) diverges and

\[
D_n\to\infty.
\tag{28}
\]

The exact symmetric seam-parity eigenvalue from PF-317/PF-326 is (9). The two frequencies (1) remain in a fixed compact set, so `q_+=O_\kappa(w_n)`. In particular

\[
q_+(\alpha_n,w_n)+q_+(\beta_n,w_n)=o(D_n).
\tag{29}
\]

The seam form is Fourier diagonal, so it contributes nothing to the low/high numerator. Equations (7)--(9) and (28)--(29) therefore prove the fixed lower bound (10).

This is exactly where the symmetric parity channel matters. The antisymmetric seam eigenvalue is order `w_n^{-1}` and would require a different comparison. One symmetric channel is enough for the obstruction.

## 3. Separated modules turn the local correlation into a noncompactness theorem

The local lower bound alone already falsifies both proposed modulewise decay targets: the local intrinsic correlation does not tend to zero, let alone satisfy the PF-318 Hilbert--Schmidt budget or a PF-321 superlinear seam power.

For the global conclusion, use PF-214's exact module support. The raw exterior pant form couples only neighboring modules and the seam form is module diagonal. Therefore modules separated by at least three indices have no mutual raw energy or mixed-form terms. On the selected subspaces (11), the restricted positive form is an orthogonal direct sum of scalar `2x2` low/high forms, each with canonical correlation `rho_{n_j}\ge rho_0`.

Let `A,B,C` be the full raw `L/H` blocks of `Q+Lambda_E`, and let `i_E,i_F` be the inclusions of the selected low/high subspaces. Put

\[
A_E=i_E^*Ai_E,
\qquad
C_F=i_F^*Ci_F,
\]

and define

\[
X=A^{1/2}i_EA_E^{-1/2},
\qquad
Y=C^{1/2}i_FC_F^{-1/2}.
\tag{30}
\]

Then `X^*X=Y^*Y=I`, and for

\[
T_{\rm raw}=A^{-1/2}BC^{-1/2}
\]

the restricted canonical correlation is exactly

\[
A_E^{-1/2}i_E^*Bi_FC_F^{-1/2}
=X^*T_{\rm raw}Y.
\tag{31}
\]

Thus its singular values cannot exceed the corresponding singular values of `T_raw`. Because the restricted operator has `M` singular values at least `rho_0`, (13) follows.

Finally, `Q` commutes with the physical `L/H` split. Passing from the raw form `Q+Lambda_E` to PF-317's normalized form

\[
Q^{-1/2}(Q+\Lambda_E)Q^{-1/2}=I+K
\]

is therefore a block-diagonal congruence. The standard canonical-correlation calculation used in PF-329 gives left/right unitary equivalence of the raw and normalized angles. The singular lower bound is consequently a statement about the actual PF-317 direct angle `Z_{LH}`, not an artifact of raw boundary coordinates.

## Prior-art and novelty audit

Nothing novel is claimed about the abstract sharp-projection phenomenon. Off-diagonal corners across Fourier/Hardy projections lead classically to Hankel operators, and Hartman's compactness theorem characterizes compact Hankel operators on the fixed circle through the symbol class; see P. Hartman, *On completely continuous Hankel matrices*, Proc. AMS 9 (1958), 862--866, and F. F. Bonsall--S. C. Power, *A proof of Hartman's theorem on compact Hankel operators*, Math. Proc. Camb. Phil. Soc. 78 (1975), 447--450. Likewise, the fact that a smooth fixed-boundary DtN map is a first-order pseudodifferential operator is classical and already part of the direct-angle prior-art audit.

Those fixed-operator theorems do not state the present degeneration result. Here the Fourier lattice spacing tends to zero because `L_n\to\infty`, while a geometrically localized pant conductance grows like `1/s_n`; the low and high witness modes are chosen on opposite sides of a fixed **physical** cutoff but differ by only one Fourier lattice step. The proof above uses the exact PF-341 corridor geometry, the canonical prime-flute scales, and PF-214's finite-range assembly to obtain a uniform noncompactness witness for the project-specific direct canonical correlation.

A targeted literature search found the classical Hankel compactness framework and general DtN pseudodifferential/commutator theory, but no theorem asserting this sharp-cutoff, degenerating-one-cusp-pant lower bound or its prime-flute noncompactness consequence. No external theorem is imported into the derivation, so `SOURCES.md` acquires no new theorem dependency.

## Boundaries and falsification

1. **The sharp fixed physical split is load-bearing.** The witness uses the adjacent frequencies immediately below and above `kappa`. A smoothed frequency partition, a transition band, or a different reference decomposition is not ruled out by this finding.
2. **The symmetric seam-parity channel is load-bearing.** Its seam energy is `O(w_n)` at fixed physical frequency. No analogous claim is made here for the antisymmetric `O(w_n^{-1})` branch.
3. **Zero twist fixes the common phase origin.** The same-sign two-pant addition uses the canonical zero-twist identification already used by PF-341. A nonzero twist could change the phase relation and requires a separate calculation.
4. **The PF-341 corridor estimates are load-bearing.** The lower and upper variational bounds use the same two-sided `s cosh t` corridor control and the same noncollapsing remainder decomposition.
5. **Finite-section compatibility remains the operator-theoretic setting.** The proof gives a lower singular-value bound uniform in arbitrarily large canonical finite sections. Any proposed infinite-tail realization inconsistent with those compressions is outside the PF-311/PF-317 framework.
6. **This closes the current direct sharp-cutoff channel, not the whole Prime-Flute program.** It does not decide the conditional post-low channel, a different physical decomposition, scattering/determinant constructions, a zeta-zero correspondence, the critical line, or RH.

A falsification must break one of the explicit inputs: the sharp cutoff convention from PF-325/PF-326, the PF-341 corridor variational estimates at fixed physical frequency, the zero-twist two-pant phase alignment, PF-214's finite-range module support, or block-diagonal congruence invariance of the canonical correlation.

## Consequence for the research line

The independent PF-318/PF-320 upper-bound branch left open after PF-341 is now closed for the **current sharp physical `L/H` split**. The obstruction is not the old normalized-insertion translation gate and does not rely on a large unnormalized DtN coefficient. It is already present in the completed energy-normalized low/high correlation: adjacent Fourier modes straddling the fixed physical cutoff retain order-one canonical correlation on infinitely many separated tail modules.

Therefore neither

\[
\|T_{0,n}^{(r)}\|_{\mathcal S_2}^2
\lesssim\frac{1+\log P_n}{P_n^2}
\]

nor

\[
\|T_{0,n}^{(r)}\|=O(s_n^{1+\varepsilon})
\]

can be the missing theorem for this decomposition. Continuing the direct channel requires changing the reference split/endpoint mechanism itself -- for example by introducing a transition/smoothed physical-frequency partition or another decomposition that does not classify two modes separated by `2pi/L_n` as asymptotically orthogonal channels -- rather than sharpening the existing pant estimate.