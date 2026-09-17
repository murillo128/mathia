---
id: WP-346
title: Self-adjoint Robin scattering realizes the CDD control with a positive full truncated norm
branch: weil_positivity
status: supported
kind: self-adjoint-robin-cdd-realization-control
claim_strength: exact free-half-line derivation plus self-adjoint matched control and prior-art audit
created: 2026-09-17
related: [WP-345, WP-171, WP-188]
prior_art:
  - B. Belchev and M. A. Walton, On Robin boundary conditions and the Morse potential in quantum mechanics, J. Phys. A 43 (2010) 085301, arXiv:1002.2139
  - J. Behrndt, M. M. Malamud, and H. Neidhardt, Scattering matrices and Weyl functions, Proc. London Math. Soc. 97 (2008), 568-598, DOI 10.1112/plms/pdn016
  - classical one-dimensional reflection scattering and Wigner phase-delay identities
---

# WP-346 — Self-adjoint Robin scattering realizes the CDD control with a positive full truncated norm

## Claim

The meromorphic CDD factor used as the matched control in `WP-345` is not merely an algebraically admissible unitary-axis modification. It has an elementary realization by an ordinary self-adjoint Hilbert-space scattering geometry whose **full truncated norm is positive for every cutoff** and whose cutoff derivative is an exact boundary square.

Let the free half-line Hamiltonian `H_L=-d^2/dx^2` on `L^2(R_+)` carry the Robin boundary condition

\[
u(0)+L u'(0)=0,
\qquad L>0.
\tag{1}
\]

For continuum momentum `k>0`, the incoming-normalized generalized eigenfunction

\[
\psi_{k,L}(x)=e^{-ikx}+S_L(k)e^{ikx}
\tag{2}
\]

has reflection amplitude

\[
S_L(k)=-\frac{1-ikL}{1+ikL}.
\tag{3}
\]

It satisfies `|S_L(k)|=1` for real `k`, `S_L(-k)=S_L(k)^{-1}`, and `S_L(k)\to1` as `k\to+\infty`. The pole at `k=i/L` is the genuine Robin bound state. With

\[
z=ik,
\qquad a=L^{-1},
\tag{4}
\]

one has exactly

\[
S_L(k)=\frac{z-a}{z+a}.
\tag{5}
\]

Therefore the two-channel direct sum of two identical Robin half-lines has scattering matrix

\[
\mathsf S_L(k)=\operatorname{diag}(S_L(k),S_L(k))
\tag{6}
\]

and determinant

\[
\boxed{
\det\mathsf S_L(k)
=S_L(k)^2
=\left(\frac{z-a}{z+a}\right)^2
=C_a(z),
}
\tag{7}
\]

**exactly the factor of `WP-345`**, including `C_a(0)=1`, `C_a(z)C_a(-z)=1`, unit modulus on `Re z=0`, asymptotic normalization `C_a\to1`, and the double off-unitary zero/pole pair at `z=\pm a`.

Yet each Robin channel has the positive truncated Hilbert norm

\[
N_R(k):=\int_0^R|\psi_{k,L}(x)|^2\,dx\ge0
\tag{8}
\]

for every `R>=0`, and

\[
\boxed{
\partial_R N_R(k)=|\psi_{k,L}(R)|^2\ge0.
}
\tag{9}
\]

More strongly, the exact finite part of `N_R` contains the logarithmic phase derivative carrying the same scattering divisor. Thus **ordinary self-adjoint realizability, positivity of the full truncated norm, and boundary-square monotonicity still do not constrain the scattering divisor to the unitary axis**.

This strengthens `WP-345` but does not claim that an arbitrary CDD modification of an automorphic Eisenstein scattering coefficient is itself automorphically realizable. It closes only the broader escape in which generic self-adjoint Hilbert/scattering realizability was expected to rule out the CDD control. Any surviving source-realizability theorem must use genuinely stronger automorphic/arithmetic structure.

**Classification:** `EXACT-DERIVED + SELF-ADJOINT-ROBIN-SCATTERING + FULL-POSITIVE-TRUNCATED-NORM + EXACT-CDD-REALIZATION + MATCHED-CONTROL + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

## 1. Robin reflection is the elementary CDD factor

Belchev--Walton review the free particle on the positive half-line with (1), noting that these Robin conditions give self-adjoint extensions of the free Hamiltonian and that for `L>0` there is one bound state proportional to `e^{-x/L}` with energy `-1/L^2` in units `\hbar^2/(2m)=1`. They write continuum states as `sin(kx+phi)` with

\[
kL=-\tan\phi.
\tag{10}
\]

Equation (3) follows directly from (1): substituting (2) at `x=0` gives

\[
1+S_L+L(-ik+ikS_L)=0,
\tag{11}
\]

and hence (3). For real `k`, numerator and denominator are conjugates up to the overall sign, so the reflection is lossless. The reciprocal identity follows immediately:

\[
S_L(-k)=S_L(k)^{-1}.
\tag{12}
\]

The denominator of (3) vanishes at `k=i/L`; this is precisely the bound-state pole described by the self-adjoint Robin problem, rather than a non-self-adjoint pathology.

Now use the centered scattering variable `z=ik`. Then

\[
S_L(k)
=-\frac{1-zL}{1+zL}
=\frac{z-L^{-1}}{z+L^{-1}},
\tag{13}
\]

which proves (5). A single channel has `S_L(0)=-1`; taking the direct sum of two identical channels removes only this harmless central sign and gives (7). No divisor fitting is involved: the same positive self-adjoint boundary condition fixes the pole/zero pair and the scattering phase.

The match to `WP-345` is exact after the change of variable (4). In particular, the doubled system realizes the very factor that was introduced there only as a meromorphic inner/CDD matched control.

## 2. The full truncated norm contains the divisor phase derivative

Write on the real continuum

\[
S_L(k)=e^{i\theta_L(k)}
\tag{14}
\]

with the continuous branch

\[
\theta_L(k)=\pi-2\arctan(kL).
\tag{15}
\]

Then

\[
\theta_L'(k)
=-\frac{2L}{1+k^2L^2},
\qquad
\sin\theta_L(k)
=\frac{2kL}{1+k^2L^2},
\tag{16}
\]

so there is the exact endpoint identity

\[
\boxed{
\theta_L'(k)=-\frac{\sin\theta_L(k)}{k}.
}
\tag{17}
\]

Since

\[
|\psi_{k,L}(x)|^2
=2+2\cos(\theta_L(k)+2kx),
\tag{18}
\]

direct integration gives

\[
\begin{aligned}
N_R(k)
&=2R+
\frac{\sin(\theta_L(k)+2kR)-\sin\theta_L(k)}{k}\\
&=\boxed{
2R+
\frac{\sin(\theta_L(k)+2kR)}{k}
+\theta_L'(k)
}.
\end{aligned}
\tag{19}
\]

Thus the same positive Hilbert norm contains three pieces familiar from the Maaß--Selberg pattern: a linear cutoff term, an oscillatory boundary/interference term, and a cutoff-independent scattering phase derivative. The latter is the boundary value of the logarithmic derivative:

\[
-i\frac{S_L'(k)}{S_L(k)}=\theta_L'(k).
\tag{20}
\]

For the doubled system let

\[
D_L(k)=\det\mathsf S_L(k)=e^{i\Theta_L(k)},
\qquad \Theta_L=2\theta_L.
\tag{21}
\]

The sum of the two truncated channel norms is therefore

\[
\boxed{
N_R^{(2)}(k)
=4R+
\frac{2\sin(\theta_L(k)+2kR)}{k}
+\Theta_L'(k)
\ge0.
}
\tag{22}
\]

The logarithmic derivative of the **determinant whose divisor is (7)** is literally the cutoff-independent finite term in (22). Nevertheless it need not be positive: for `L>0`, `\Theta_L'(k)<0`. Positivity belongs to the assembled norm, where the cutoff and interference terms compensate it.

This is exactly the logical point needed for the `WP-345` control. Passing from the full source-defined positive norm to one distinguished logarithmic-derivative summand does not inherit the Hilbert-space sign.

## 3. The cutoff derivative is still a positive boundary square

Differentiating the definition (8), not merely the closed form, gives

\[
\partial_RN_R(k)=|\psi_{k,L}(R)|^2.
\tag{23}
\]

Using (18),

\[
\partial_RN_R(k)
=2+2\cos(\theta_L(k)+2kR)
=|e^{-ikR}+S_L(k)e^{ikR}|^2
\ge0.
\tag{24}
\]

For two channels,

\[
\partial_RN_R^{(2)}(k)
=2|e^{-ikR}+S_L(k)e^{ikR}|^2
\ge0.
\tag{25}
\]

So the strengthened control simultaneously has:

- a genuine self-adjoint Hamiltonian;
- an actual positive `L^2` truncated norm for every cutoff;
- a pointwise positive cutoff derivative given by a boundary square;
- a unitary reciprocal scattering matrix;
- central and high-energy determinant normalization;
- the exact CDD determinant `C_a` with an off-unitary zero/pole pair.

Consequently neither the positivity of the full truncated Hilbert norm nor its monotone boundary growth can, by themselves, imply a restriction on the determinant divisor.

## 4. Aggressive falsification and scope

**This is not an automorphic realization theorem.** The Robin problem proves that the abstract CDD factor is compatible with ordinary self-adjoint scattering geometry and positive truncation. It does not prove that `m(s)C_a(s-1/2)` is the scattering coefficient of an automorphic quotient with the same cusp geometry. A theorem using automorphy, Euler/Gamma normalization, the global functional equation, or another arithmetic constraint could still exclude such factors. The finding narrows what that theorem must use.

**The two-channel duplication is only a matched normalization control.** A single Robin channel already has a self-adjoint positive truncated norm and a simple off-unitary zero/pole pair. Two identical channels are used solely because their determinant has central value `+1` and equals the squared factor chosen in `WP-345`. Since this is a falsification control rather than a proposed arithmetic mechanism, duplicating an already source-defined channel does not insert zero data or tune a kernel.

**The divisor is physical, not an arbitrary meromorphic decoration.** For `L>0`, the pole at `k=i/L` is the bound state of the self-adjoint extension. Reversing the Robin sign reverses the pole/zero orientation. Self-adjointness constrains boundary unitarity but does not force the meromorphic continuation to have no off-continuum divisor.

**There is no conflict with `WP-171`.** That finding shows that a Schur/inner orientation has a semidefinite boundary-delay matrix. The Robin reflection can be placed in the opposite half-plane orientation, and its phase derivative in (16) has the corresponding sign. The present statement is different: whichever orientation is used, the **assembled truncated norm** remains positive while the meromorphic scattering determinant has an off-axis divisor.

**There is no conflict with `WP-188`.** Changing the self-adjoint boundary condition is a domain-changing extension problem, not the ordinary trace-class-difference setting excluded there. Indeed `WP-188` explicitly left generalized/domain-changing scattering as a category boundary. `WP-346` now shows that entering the domain-changing self-adjoint category is not enough by itself: generic Hilbert positivity still permits the exact CDD control.

**The result does not establish Weil positivity.** No zeta zero data are constrained and no global finite-prime/archimedean explicit formula is made nonnegative. This is a negative matched control on one proposed route to such a theorem.

## 5. Prior-art and novelty audit

No theorem-level novelty is claimed for Robin self-adjoint extensions, half-line reflection amplitudes, bound-state poles, or phase/time-delay identities. Belchev and Walton, *On Robin boundary conditions and the Morse potential in quantum mechanics*, J. Phys. A 43 (2010) 085301, arXiv:`1002.2139`, explicitly review the Robin boundary condition `psi(0)+L psi'(0)=0`, its self-adjointness, the continuum phase relation `kL=-tan phi`, the `L>0` bound state, and the corresponding Wigner phase-delay derivative. Behrndt--Malamud--Neidhardt provide a general extension-theoretic scattering framework for self-adjoint extensions and scattering matrices.

The durable Mathia delta is narrower: equations (7) and (22) identify **the exact CDD factor introduced in `WP-345`** with the determinant of a concrete doubled self-adjoint Robin scattering system, while showing in the same calculation that its logarithmic derivative is a summand of an everywhere positive full truncated norm whose cutoff derivative is an exact square. A targeted audit found the classical ingredients separately, not this repository-specific matched-control consequence.

## Consequence for `weil_positivity`

`WP-345` left open the possibility that the CDD control might be excluded once one demands a genuine source realization rather than only boundary unitarity and reciprocal symmetry. The Robin model removes the generic version of that escape:

\[
\boxed{
\text{self-adjoint Hilbert scattering}
+\text{positive full truncation}
+\text{positive boundary square}
\not\Rightarrow
\text{unitary-axis divisor control}.
}
\tag{26}
\]

A viable Maaß--Selberg/trace route therefore needs a **specifically automorphic or arithmetic** restriction that is stronger than ordinary self-adjoint scattering realizability. It must couple the logarithmic-derivative carrier to the positive geometry in a way that the Robin/CDD realization cannot imitate, rather than relying on Hilbert positivity, self-adjointness, boundary unitarity, or truncation monotonicity alone.
