---
title: "WP-451: Phase-invariant Maharam forms retain the full finite Weil sign defect"
type: research-finding
status: verified
research_question: "Can a positive dilation-covariant Maharam energy repair the finite Weil sign while preserving real-coordinate phase modulation?"
claim_strength: exact_spectral_interval_for_the_critical_defect_in_every_nonzero_dilation_and_modulation_invariant_form_completion
scope: unchanged finite-prime correlation defect in a positive form completion preserving the specified two symmetries; includes unbounded and degenerate forms but not arbitrary global completions
finding_id: WP-451
related_findings:
  - WP-218
  - WP-221
  - WP-225
  - WP-447
  - WP-448
  - WP-449
  - WP-450
related_clues:
  - CLUE-bost-connes-affiliation-conditioning-boundary
created: 2026-10-25
updated: 2026-10-25
tags:
  - weil-positivity
  - maharam-extension
  - positive-form
  - phase-modulation
  - commuting-isometries
  - spectral-obstruction
---

# WP-451: Changing the positive energy does not change the finite sign under both source symmetries

## Claim and evidence boundary

**EXACT-DERIVED; CLASSICAL OPERATOR-THEORETIC INGREDIENTS;
CATEGORY OBSTRUCTION.** The nonconstant positive forms of
WP-447--WP-449 escape various scalar and bounded-operator
classifications. Nevertheless, all of them retain the entire
finite-prime Weil sign defect when the critical prime-power
correlation coefficients are kept unchanged.

Let \(\mathcal D\) be a complex linear subspace of the critical
Maharam space specified below. Let \(Q\) be a nonzero positive
semidefinite sesquilinear form on \(\mathcal D\), conjugate-linear
in its first variable. Write \(Q[f]=Q(f,f)\). Assume
\[
 W_m\mathcal D\subset\mathcal D,\qquad Q[W_m f]=Q[f]
       \quad(m\ge1),                                      \tag{1}
\]
\[
 M_t\mathcal D=\mathcal D,\qquad Q[M_t f]=Q[f]
       \quad(t\in\mathbb R),\qquad (M_tf)(J,s)=e^{its}f(J,s).
                                                               \tag{2}
\]
No boundedness or coercivity of \(Q\) in the original Hilbert norm
is required. Its nullspace may be nontrivial. Form the energy space
\[
 \mathcal H_Q=\overline{\mathcal D/\{f:Q[f]=0\}}^{\,Q}.
\]
For a nonempty finite prime set \(F\), the induced source maps
\(S_p[f]=[W_pf]\) are commuting isometries. Define the bounded
self-adjoint critical correlation defect on this space by
\[
 D_{F,Q}=-\sum_{p\in F}(\log p)
       \sum_{k\ge1}p^{-k/2}(S_p^k+S_p^{*k}).                  \tag{3}
\]
Every series here converges in operator norm. Then
\[
 \boxed{\operatorname{Spec}(D_{F,Q})=
 \left[-2\sum_{p\in F}\frac{(\log p)p^{-1/2}}{1-p^{-1/2}},
        \ 2\sum_{p\in F}\frac{(\log p)p^{-1/2}}{1+p^{-1/2}}
 \right].}                                                 \tag{4}
\]
The closed numerical range is the same interval. Both strict signs
are already witnessed by classes of vectors in \(\mathcal D\).
The whole interval is essential spectrum, so a compact
self-adjoint correction **on the energy space** cannot remove its
negative part.

This closes a sign question rather than classifying the possible
energies: even an unbounded, nonperiodic or degenerate positive
energy cannot repair (3) while (1)--(2) survive. The theorem also
allows excitation off-diagonal couplings if they preserve (2).
It does not identify (3) with the completed Weil functional, supply
an archimedean/polar term, or rule out a construction that changes
these hypotheses before forming its sign. No RH, zero data,
historical novelty, formal verification or independent adversarial
approval is claimed.

## Source normalization and the actual comparison being tested

Use the fixed space of WP-447--WP-450:
\[
 \Omega=\prod_p\mathbb N_0,\qquad
 \nu=\bigotimes_p\nu_p,\qquad \nu_p(j)=(1-p^{-1})p^{-j},
 \qquad \mathcal K=L^2(\Omega\times\mathbb R,d\nu\,e^sds).
\]
Set
\[
 (V_pf)(J)=\sqrt p\,1_{J_p\ge1}f(J-e_p),\qquad
 (U_ch)(s)=e^{-c/2}h(s-c),\qquad
 W_p=V_p\otimes U_{\log p},\qquad W_m=\prod_pW_p^{v_p(m)}.
                                                               \tag{5}
\]
These are commuting isometries on \(\mathcal K\). Direct
substitution, with the translation direction in (5), gives
\[
 M_tW_pM_t^*=e^{it\log p}W_p.                                \tag{6}
\]
Positivity and Cauchy--Schwarz make the nullspace of \(Q\)
orthogonal to all of \(\mathcal D\). Equations (1)--(2) preserve
that nullspace, so they induce commuting isometries \(S_p\)
and unitaries \(G_t\) on \(\mathcal H_Q\). Polarization gives
their inner-product identities. Equation (6) becomes
\[
 G_tS_pG_t^*=e^{it\log p}S_p.                               \tag{7}
\]
Thus the symmetry survives the quotient and completion; no
bounded intertwiner from the original Hilbert space is assumed.

The quadratic expression in (3), evaluated on an original vector,
is exactly
\[
 \langle[f],D_{F,Q}[f]\rangle_Q
 =-2\sum_{p\in F}(\log p)\sum_{k\ge1}p^{-k/2}
                     \operatorname{Re}Q(f,W_p^k f).          \tag{8}
\]
Indeed \(|Q(f,W_p^kf)|\le Q[f]\), proving absolute convergence
on \(\mathcal D\). This retains the coefficients
\(-\log p\,p^{-k/2}\) of the finite critical ray. The adjoints
in (3) are the **energy-space adjoints**. We do not silently identify
them with adjoints in \(\mathcal K\), or claim an unbounded
congruence of the original defect has already been defined.

For each excitation-diagonal form in WP-447--WP-449,
\[
 Q[f]=\sum_n\int q_n(s)|h_n(s)|^2e^sds,\qquad
 f=\sum_n\Psi_n\otimes h_n,
                                                               \tag{9}
\]
multiplication of every \(h_n(s)\) by \(e^{its}\) preserves
both its full finite-integral domain and its energy. Those findings
prove (1) on that domain. Consequently every nonzero one of those
forms satisfies the present theorem, including the homogeneous
endpoint with a large nullspace, the coprime-counting form, its
smooth variants, and its coercive norm additions. More generally,
real-coordinate-local positive fibre forms satisfy (2), even when
their valuation coordinates are coupled, provided their domain and
covariance satisfy (1).

## A finite box produces joint approximate eigenvectors

Here is a direct lemma avoiding any assumption of double commutation,
a Hardy representation, a wandering vector, or a unitary dilation.
Let \(S_1,\ldots,S_d\) be commuting isometries on a nonzero Hilbert
space, and fix a unit vector \(x\). For \(z\in\mathbb T^d\), put
\[
 v_N(z)=\sum_{0\le k_1,\ldots,k_d<N}z^{-k}S^kx,
 \quad z^{-k}=\prod_jz_j^{-k_j},\quad S^k=\prod_jS_j^{k_j}.
                                                               \tag{10}
\]
With normalized Haar measure, orthogonality of the distinct
characters gives
\[
 \int\|v_N(z)\|^2\,dz=N^d.                                  \tag{11}
\]
In \((S_j-z_jI)v_N(z)\), all interior terms cancel. The remaining
two faces have distinct Fourier characters, and each vector
coefficient has norm one. Therefore
\[
 \int\|(S_j-z_jI)v_N(z)\|^2\,dz=2N^{d-1}.                   \tag{12}
\]
These equalities use orthogonality in the auxiliary \(z\) variable,
not orthogonality of the orbit vectors \(S^kx\).

Comparing the integrals in (11)--(12) yields some \(z_N\) with
\(v_N(z_N)\ne0\) such that, for
\(x_N=v_N(z_N)/\|v_N(z_N)\|\),
\[
 \sum_{j=1}^d\|(S_j-z_{N,j}I)x_N\|^2\le\frac{2d}{N}.        \tag{13}
\]
In particular this supplies simultaneous approximate eigenvectors
with some unit-modulus phases, including for correlated or
non-doubly-commuting isometries.

Now enumerate \(F=\{p_1,\ldots,p_d\}\). The orbit
\[
 \{(e^{-it\log p_1},\ldots,e^{-it\log p_d}):t\in\mathbb R\}
                                                               \tag{14}
\]
is dense in \(\mathbb T^d\). For completeness, every nontrivial
torus character restricts to \(e^{-it\sum_j a_j\log p_j}\)
with nonzero frequency: unique factorization gives
\(\sum_j a_j\log p_j=0\Rightarrow a_j=0\) for integer \(a_j\).
Its symmetric time average tends to zero. Trigonometric-polynomial
approximation then makes time averages of every continuous function
equal its Haar integral in the limit. A nonnegative continuous bump
inside any nonempty open set has positive Haar integral, proving
that (14) meets that open set.

Given any target \(\zeta\in\mathbb T^d\), choose \(t_N\) so that
\(e^{-it_N\log p_j}z_{N,j}\) is within \(1/N\) of \(\zeta_j\)
for every \(j\). Equation (7) implies that \(y_N=G_{t_N}x_N\)
satisfies
\[
 \|y_N\|=1,\qquad
 \max_j\|(S_j-\zeta_jI)y_N\|
       \le\sqrt{2d/N}+1/N\longrightarrow0.                 \tag{15}
\]
If \(x\) starts as a class from \(\mathcal D\), all these
vectors remain classes from \(\mathcal D\), since the construction
uses only finite sums, source powers and modulation.

## Exact operator bounds and spectral saturation

For any isometry \(S\) and \(0<r<1\), norm-convergent geometric
series give the operator Poisson identity
\[
 P_r(S):=I+\sum_{k\ge1}r^k(S^k+S^{*k})
 =(1-r^2)(I-rS^*)^{-1}(I-rS)^{-1}.                           \tag{16}
\]
One can verify it by multiplying on the left by \(I-rS^*\)
and on the right by \(I-rS\); the numerator is
\(I-r^2S^*S=(1-r^2)I\). Since
\[
 (1-r)\|u\|\le\|(I-rS)u\|\le(1+r)\|u\|,
\]
equation (16) gives the sharp universal order bounds
\[
 \frac{1-r}{1+r}I\le P_r(S)\le\frac{1+r}{1-r}I.              \tag{17}
\]
Applying (17) term by term proves that the spectrum in (4) is
contained in the displayed interval.

Conversely, if \(\|(S-\zeta I)y\|\le\delta\), \(|\zeta|=1\)
and \(\|y\|=1\), then
\[
 \|(S^*-\overline\zeta I)y\|\le\delta,\qquad
 \|(S^k-\zeta^k I)y\|,\quad
 \|(S^{*k}-\overline\zeta^{\,k}I)y\|\le k\delta.             \tag{18}
\]
The first inequality follows from
\(S^*(S-\zeta I)y=-\zeta(S^*-\overline\zeta I)y\);
the others follow by telescoping and contractivity. Thus for the
vectors (15), with \(\delta_N=\sqrt{2d/N}+1/N\),
\[
 \|(D_{F,Q}-w_F(\zeta)I)y_N\|
 \le 2\delta_N\sum_{p\in F}\frac{(\log p)p^{-1/2}}
                                  {(1-p^{-1/2})^2}\to0,
                                                               \tag{19}
\]
where
\[
 w_F(\zeta)=\sum_{p\in F}(\log p)
       \left(1-\frac{1-p^{-1}}{|1-p^{-1/2}\zeta_p|^2}\right).
                                                               \tag{20}
\]
The continuous function (20) has its minimum at all \(\zeta_p=1\)
and its maximum at all \(\zeta_p=-1\), giving exactly the two
endpoints in (4). The torus is connected, so its image is the whole
interval. Every value is an approximate eigenvalue by (19); this
proves (4). It also proves both strict signs on \(\mathcal D\):
each sufficiently accurate finite packet already has the required
sign. No vector limit in the original Hilbert norm is used.

A bounded self-adjoint operator with this nondegenerate interval
as its spectrum has no isolated spectral point. Its essential
spectrum, in the usual Fredholm sense, is therefore the same
interval. Invariance of essential spectrum under compact
self-adjoint perturbations gives the stated compact-correction
boundary. No claim is made that compactness in the original Hilbert
norm implies compactness in the new energy norm.

## Controls and the remaining mathematical boundary

The two symmetries have different jobs. Dilation invariance makes
the source maps isometries in the new energy. Modulation invariance
then prevents their approximate phases from being confined to a
favorable part of the torus. Neither boundedness of the energy nor
diagonalization in excitation coordinates is used.

Modulation covariance is material. On the one-dimensional Hilbert
space, take \(S_p=-I\) for each \(p\in F\). These commuting
isometries give
\[
 D_F=2\sum_{p\in F}\frac{(\log p)p^{-1/2}}{1+p^{-1/2}}I>0.
\]
They admit no unitaries satisfying (7) for all real \(t\).
This is an abstract control for the necessity of that hypothesis,
not a source-selected Maharam realization.

The proof survives nonarithmetic controls with arbitrary positive
coefficients \(c_j\), radii \(0<r_j<1\), and rationally
independent real frequencies \(\lambda_j\) in place of
\(\log p_j\). Its interval is
\([-2\sum c_jr_j/(1-r_j),2\sum c_jr_j/(1+r_j)]\).
If the frequencies have integer relations, the density argument
only reaches a subtorus and this full-interval proof need not apply.
No arithmetic zero information enters the sign mechanism.

WP-221 concerned subspaces of a fixed Hardy norm and did not cover
general unbounded form completions. WP-225 concerned normal positive
maps on a fixed operator algebra with discrete source energies.
Here the Hilbert topology can change, the energy can have a kernel,
and the modulation generator need not have eigenvectors; no bounded
normal channel is supplied. The new conclusion applies directly to
the forms constructed in WP-447--WP-449 and removes their unchanged
finite-defect sign escape without classifying further profiles.

The remaining possibility is an independently source-selected change
to the critical comparison: a domain or form breaking (2), a
nonisometric source relation, a change of the defect itself, or an
active global coupling before the finite and archimedean terms are
read separately. Adding an arbitrary noncompact positive term is
also outside (3), but still needs source selection and an exact
Weil identity. An indefinite finite sector does **not** refute
positivity of a completed global form on a different test class.

## Prior art and validation

Positive invariant metrics inducing isometric representations are
classical. Panja, *Factorization of Toeplitz operators*, Theorem 1.2
and its proof in Section 2, explicitly constructs the isometries
\(R^{1/2}h\mapsto R^{1/2}T_i h\) for bounded positive
\(T\)-Toeplitz operators. The quotient construction here proves
the needed form-level statement directly, without assuming that
\(R\) is bounded. The same paper recalls the classical joint
unitary-extension theorem for commuting isometries before
Theorem 4.5. We instead use (10)--(15), so no dilation theorem or
additional joint-spectrum hypothesis is left implicit.

Gauge symmetry forcing full circular spectral support is likewise
classical: Yamashita's *Toeplitz algebra*, Section 2.2 and the proof
of Proposition 4, exhibit this argument in the Toeplitz quotient.
Poisson resolvents, character orthogonality and the torus density
argument are standard tools. Searches by commuting-isometry
extension, joint approximate spectrum, gauge spectrum and positive
Toeplitz factorization do not establish historical novelty.

The local delta is the exact transfer of those tools to the
Maharam **energy completion**, including unbounded or degenerate
energies, the original-domain witnesses (8), (15), and the full
finite-defect spectrum (4). It closes a concrete sign question left
by the positive examples, rather than counting their existence as
progress toward Weil positivity.

An exact integer-coefficient audit passed 160 checks of (11)--(12),
using \(d=1,2,3\), \(N=1,2,3,5,8\), and an initial vector with
coefficients \(1,2\) on two basis vectors. Controls included
independent coordinate shifts, triangular commuting shifts
\(S_j e_a=e_{a+e_1+\cdots+e_j}\), repeated identical shifts, and
scalar negative unitaries. It expanded the full Fourier/vector
coefficients before integrating, so overlapping orbit vectors and
non-double-commutation were included. The scalar controls check the
finite lemma only; they do not satisfy (7). These checks diagnose
the two-face normalization and phase signs. The domain, density,
infinite-series and spectral assertions are proved above, not
inferred from finite computation.

## References

- [WP-221](WP-221-every-nonzero-jointly-shift-invariant-mixed-prime-hardy-submodule-retains-bost-connes-weil-sign-defect.md), the previous fixed-Hardy-space numerical-range obstruction.
- [WP-225](WP-225-time-covariance-alone-forbids-positive-orientation-of-bost-connes-weil-defect.md), the distinct normal-positive-map obstruction.
- [WP-447](WP-447-homogeneous-maharam-forms-recover-classical-gcd-grams.md), source normalization and homogeneous closed forms.
- [WP-448](WP-448-periodic-maharam-forms-have-a-sharp-zeta-smoothing-threshold.md), periodic closed forms.
- [WP-449](WP-449-nonperiodic-maharam-positive-forms-from-coprime-counting.md), nonperiodic closed forms and their domain/covariance theorem.
- [WP-450](WP-450-bounded-maharam-diagonal-covariance-forces-a-scalar.md), bounded diagonal classification, which is not needed in this proof.
- S. Panja, *Factorization of Toeplitz operators*, New York Journal of Mathematics **29** (2023), 848--873, Theorem 1.2 and Section 4, [journal article](https://nyjm.albany.edu/j/2023/29-33.html), [full text](https://nyjm.albany.edu/j/2023/29-33v.pdf).
- M. Yamashita, *Toeplitz algebra*, guest lecture, University of Warsaw (2012), Section 2.2 and Proposition 4, [author lecture text](https://www.impan.pl/~pmh/teach/intro4/lecture7.pdf).
