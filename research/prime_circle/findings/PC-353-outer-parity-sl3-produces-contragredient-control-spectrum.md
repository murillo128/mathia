# PC-353 — outer-parity SL3 developments produce contragredient matched-control spectra

- **Finding ID:** `PC-353`
- **Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `NUMERICAL-SANITY`
- **Status detail:** `DECISIVE-BOUNDARY` for the outer-parity escape left open by PC-352; `DECISIVE-NEGATIVE` for treating outer parity alone as an RH mechanism
- **Workflow:** `DERIVED + PRIOR-ART AUDIT + ADVERSARIAL CONTROL`
- **Research line:** `prime_circle`
- **Result type:** exact structural classification with one numerical source sanity check
- **Prime dependence:** the exact target-space theorem is kinematic and applies equally to the cyclotomic centered profiles and to matched reciprocal controls
- **RH relevance:** high as a boundary result: moving from inner parity to an outer automorphism can make the ordinary conjugacy-class spectrum control-sensitive, but the only forced change is classical contragredient/reciprocal duality, so outer parity by itself supplies no arithmetic or zero-selecting discriminator

## Claim

PC-352 proves that a non-solvable target is still useless for conjugacy-invariant spectral readouts whenever the reciprocal sign flip `W_j -> -W_j` is implemented by one fixed **inner** target automorphism. The most direct remaining repair is to use a semisimple target on which the same parity is genuinely **outer**.

That repair can indeed evade the exact conjugacy obstruction, but its spectral content is sharply constrained. In `SL_d(C)`, `d >= 3`, take the standard outer involution

\[
\Theta(g)=(g^{-1})^{\mathsf T},
\qquad
\theta(X)=-X^{\mathsf T}.
\]

Place the canonical calibration direction in the skew-symmetric subspace and every centered shell direction in the symmetric traceless subspace:

\[
A^{\mathsf T}=-A,
\qquad
B_j^{\mathsf T}=B_j,
\qquad
\operatorname{tr}A=\operatorname{tr}B_j=0.
\]

Then `theta(A)=A` and `theta(B_j)=-B_j`. For the PC-350 centered radial connection

\[
\Omega=A\,dX_2+\sum_j B_j\,dW_j
\]

and its matched reciprocal control

\[
\widetilde\Omega=A\,dX_2-\sum_j B_j\,dW_j,
\]

the regularized developments satisfy the exact identity

\[
\boxed{
\widetilde D_R=\Theta(D_R)=D_R^{-\mathsf T}
}
\]

at every finite cutoff, and therefore in every convergent regularized limit.

Thus the source and control characteristic polynomials are not arbitrary independent spectra. They are exact reciprocals:

\[
\boxed{
\chi_{\widetilde D}(z)
=(-1)^d z^d\chi_D(z^{-1}).
}
\]

For `SL_3`, writing

\[
\chi_D(z)=z^3-tz^2+sz-1,
\]

with

\[
t=\operatorname{tr}D,
\qquad
s=\operatorname{tr}D^{-1},
\]

the matched control simply swaps the two coefficients:

\[
\boxed{
(t,s)\longmapsto(s,t).
}
\]

The reciprocal asymmetry

\[
\Delta(D):=\operatorname{tr}D-\operatorname{tr}D^{-1}
\]

is therefore odd under the control, whereas every reciprocal-symmetric function of the characteristic polynomial is exactly control-blind.

This shows that PC-352's inner-parity obstruction is sharp: an outer target involution can escape equality of conjugacy classes. But it also gives a new no-go boundary. **Outer parity alone does not turn the prime-circle source into an RH spectrum.** The same contragredient relation holds for every admissible non-arithmetic reciprocal profile. A nonzero `Delta` records only an orientation between a source and its sign-flipped twin unless an additional source-forced construction turns that odd coordinate into an independently zero-sensitive invariant.

## 1. Exact transport of the reciprocal control by negative transpose

Retain the canonical shell-`2` clock and centered profiles of PC-350/PC-352,

\[
X_2(r)=\log(1+r),
\qquad
W_j(r)=X_j(r)-\varphi(j)X_2(r).
\]

The matched reciprocal control fixes `X_2` and sends every centered coordinate to its negative. Let

\[
\Omega=A\,dX_2+\sum_jB_j\,dW_j
\]

with `A` skew-symmetric and the `B_j` symmetric traceless. Since

\[
\theta(X)=-X^{\mathsf T},
\]

one has

\[
\theta(A)=A,
\qquad
\theta(B_j)=-B_j,
\]

and hence pointwise

\[
\boxed{
\widetilde\Omega=\theta(\Omega).
}
\]

Let `U_R` solve the same right-ordered matrix ODE convention used in PC-350--PC-352,

\[
U'=U\Omega,
\qquad U(0)=I.
\]

Because `Theta` is a Lie-group automorphism with differential `theta`, naturality of the development gives

\[
\widetilde U_R=\Theta(U_R)=U_R^{-\mathsf T}.
\]

The reciprocity closing factor is

\[
C_R=\exp[-(\log R)A].
\]

Since `theta(A)=A`, it is fixed by `Theta`. Therefore

\[
\widetilde D_R
=\widetilde U_R C_R
=\Theta(U_R)\Theta(C_R)
=\Theta(U_RC_R)
=\boxed{D_R^{-\mathsf T}}.
\]

This identity is finite-cutoff and exact. It does not depend on a delicate limiting interchange. If the regularized limit exists, the same relation passes to it.

All coefficient matrices are traceless, so `D_R` and its limit lie in `SL_d`. The characteristic-polynomial identity follows directly:

\[
\begin{aligned}
\chi_{D^{-\mathsf T}}(z)
&=\det(zI-D^{-1})\\
&=\det(zD-I)\\
&=(-1)^d z^d\det(z^{-1}I-D)\\
&=(-1)^d z^d\chi_D(z^{-1}).
\end{aligned}
\]

Thus the outer-parity control acts on ordinary spectrum by inversion of all eigenvalues, including multiplicities.

## 2. In SL3 the conjugacy-class quotient has exactly one basic odd direction

For `D in SL_3(C)`, the characteristic polynomial is

\[
\chi_D(z)
=z^3-(\operatorname{tr}D)z^2
 +(\operatorname{tr}D^{-1})z-1.
\]

Consequently negative-transpose duality exchanges

\[
\operatorname{tr}D
\longleftrightarrow
\operatorname{tr}D^{-1}.
\]

Equivalently define

\[
\Sigma(D)=\operatorname{tr}D+\operatorname{tr}D^{-1},
\qquad
\Delta(D)=\operatorname{tr}D-\operatorname{tr}D^{-1}.
\]

Then

\[
\boxed{
\Sigma(\widetilde D)=\Sigma(D),
\qquad
\Delta(\widetilde D)=-\Delta(D).
}
\]

So going from inner parity to outer parity does not produce an unconstrained new spectral family. It introduces the familiar dual/contragredient involution on the `SL_3` adjoint quotient. Every class function that is symmetric under duality remains exactly control-blind. A class function can distinguish the two only by retaining a duality orientation, of which `Delta` is the simplest polynomial example.

The same statement extends to higher `d`: the coefficients of the characteristic polynomial are exchanged with their complementary elementary symmetric coefficients under `D -> D^{-T}`. The outer involution therefore supplies reciprocal duality, not a new functional equation tied to the Riemann zeta function.

## 3. The outer involution can coexist with full sl3 generation

The escape from PC-352 is not merely another solvable or triangular artifact. Let

\[
A=(E_{12}-E_{21})+(E_{23}-E_{32})
\]

and

\[
B=\operatorname{diag}(1,2,-3).
\]

Then `A^T=-A`, `B^T=B`, and both are traceless, so the required outer parity holds.

Write

\[
K_{ij}=E_{ij}-E_{ji},
\qquad
S_{ij}=E_{ij}+E_{ji}.
\]

Here `A=K_{12}+K_{23}`. Since the diagonal entries of `B` are `(1,2,-3)`,

\[
[B,K_{12}]=-S_{12},
\qquad
[B,K_{23}]=5S_{23},
\]

and therefore

\[
[B,[B,A]]=K_{12}+25K_{23}.
\]

Together with `A`, this separates `K_{12}` and `K_{23}`. Commuting once more with `B` separates `S_{12}` and `S_{23}`. Hence the generated Lie algebra contains `E_{12},E_{21},E_{23},E_{32}`. Their brackets give the `13` root spaces and the two independent Cartan directions, so

\[
\boxed{
\operatorname{Lie}\langle A,B\rangle=\mathfrak{sl}_3(\mathbb C).
}
\]

If there were a fixed matrix `J` with

\[
JAJ^{-1}=A,
\qquad
JBJ^{-1}=-B,
\]

then `Ad_J` and `theta` would agree on generators and therefore on all of `sl_3`. But negative transpose is the nontrivial outer automorphism of type `A_2`; it is not an inner automorphism. Hence the fixed-conjugacy argument of PC-352 genuinely cannot be extended to this pair.

This is the precise sense in which the inner-parity no-go is sharp. Full semisimple generation plus outer parity can move the matched control out of the source conjugacy class.

## 4. Cyclotomic n=3 sanity check: reciprocal spectra need not coincide

The exact theorem above does not require a non-palindromic arithmetic spectrum. To verify that the surviving odd channel is not vacuous on the actual source, use the displayed `A,B` and the genuine shell `n=3` centered profile

\[
W_3(r)=\log(r^2+r+1)-2\log(1+r).
\]

For coupling `epsilon`, numerically integrate

\[
\Omega_\epsilon=A\,dX_2+\epsilon B\,dW_3
\]

and form the canonical regularized defect

\[
D_R(\epsilon)=U_R(\epsilon)\exp[-(\log R)A].
\]

At `R=10^4` the determinant stays at `1` to approximately `2e-10`. For `epsilon=0.3`,

\[
\operatorname{tr}D_R\approx3.0766444013,
\qquad
\operatorname{tr}D_R^{-1}\approx3.0707438147,
\]

so

\[
\Delta(D_R)\approx5.9005866\times10^{-3}.
\]

Increasing the cutoff from `10^3` through `10^5` stabilizes this difference near `5.899e-3`, consistent with a non-self-reciprocal limiting spectrum. This is only a numerical sanity check for non-vacuity, not an exact arithmetic theorem and not evidence of RH selectivity.

The regularized limit is well behaved for this example: `A` is real skew-symmetric, so conjugation by `exp(X_2 A)` remains bounded, while `dW_3` is integrable at both radial ends. The interaction-picture centered development therefore has an absolutely controlled tail.

## 5. Matched controls show why the outer channel is not yet arithmetic

The main falsification test is not whether `Delta` can be nonzero. It is whether nonzero reciprocal asymmetry is specific to the prime-circle source.

It is not. The derivation in section 1 used only the parity law

\[
W_j\longmapsto-W_j
\]

and the target decomposition into skew/even and symmetric/odd directions. It applies unchanged to every sufficiently regular reciprocal control profile admitted by the PC-350 matched-control class. Therefore any such control is sent to its contragredient development by exactly the same outer involution.

A nonzero `Delta` can consequently certify only that a particular developed path is not self-dual. It does **not** by itself certify cyclotomic arithmetic, prime support, zeta zeros, a critical line, or an `s <-> 1-s` functional equation. The source/control distinction is generic orientation under duality.

This gives a sharper quotient test for future candidates:

- if the proposed spectral readout is invariant under contragredient duality, outer parity buys nothing and the matched control remains invisible;
- if it is odd or otherwise oriented under duality, the readout can distinguish source from its sign-flipped twin, but it must still pass a second matched-control test against non-arithmetic reciprocal profiles and connect to an independently zero-sensitive destination theorem.

Merely choosing a larger type-`A` target, observing a non-palindromic characteristic polynomial, or feeding `Delta` into an arbitrary analytic spectral wrapper does not cross that boundary.

## Prior-art audit

No novelty is claimed for the negative-transpose automorphism, contragredient representations, Dynkin-diagram automorphisms, or reciprocal characteristic polynomials. The involution `g -> (g^{-1})^T` is the standard contragredient automorphism; for `SL_d`, `d >= 3`, it represents the nontrivial diagram automorphism of type `A_{d-1}` and is outer in the natural group.

A targeted prior-art search found the standard representation-theoretic picture rather than a prime-circle-specific predecessor. The Encyclopedia of Mathematics entry **Contragredient representation** records the classical dual action `phi*(g)=phi(g^{-1})*`. Standard type-`A` Dynkin-diagram theory identifies inverse transpose as the corresponding outer automorphism for `SL_d`, `d >= 3`; this is textbook Lie theory, not a new mechanism. The line-local delta is only the exact interaction of that classical duality with the PC-350 centered reciprocity control and the resulting quotient boundary after PC-352.

These sources are contextual prior art rather than dependencies of the proof: every identity used in the finding is displayed and verified directly. No new `SOURCES.md` anchor is required for the derivation.

## Falsification / disproof audit

- **Automorphism check:** `Theta(g)=g^{-T}` is a group automorphism and its differential is exactly `theta(X)=-X^T`.
- **Parity check:** skew-symmetric `A` is fixed and symmetric traceless `B_j` is negated, so the matched reciprocal control is exactly `theta(Omega)`.
- **Finite-cutoff check:** `tilde D_R=D_R^{-T}` holds before taking a regularized limit.
- **Determinant check:** all target matrices are traceless, so the developments remain in `SL_d` and the reciprocal characteristic-polynomial formula has no extra determinant factor.
- **Non-inner check:** the explicit `A,B` generate all of `sl_3`; a fixed conjugator implementing their parity would therefore implement negative transpose on all of `sl_3`, contradicting its standard outer character in type `A_2`.
- **Control check:** the theorem is unchanged if the cyclotomic centered profile is replaced by any admissible reciprocal profile. Thus reciprocal spectral asymmetry is not source-specific by construction.
- **Numerical check:** the `n=3` computation demonstrates that the odd class-function channel can be nonzero for the actual cyclotomic source, but the stored exact conclusions do not depend on that numerical value.
- **Destination check:** neither the reciprocal characteristic-polynomial relation nor `Delta` contains an intrinsic spectral parameter, gamma factor, Riemann-zero condition, or critical-line selector.

## Boundary assessment

PC-351 showed that the faithful triangular decoder loses the source on the ordinary spectral quotient. PC-352 showed that merely moving to a full non-solvable `SL_2` target still fails when reciprocal parity is inner. PC-353 closes the next obvious escape: **outer parity can restore control-sensitive conjugacy-class data, but what it restores is only classical contragredient orientation.**

A viable continuation must do more than make the source and its reciprocal twin spectrally unequal. It must explain why a particular outer-parity observable is forced by the original roots/refinement geometry, show that the observable separates the arithmetic source from non-arithmetic reciprocal controls rather than merely choosing an orientation, and connect that reduced observable to a destination theorem with independent zeta-zero or RH sensitivity.

The result does not rule out such a source-forced outer quotient. It rules out crediting outer automorphism, reciprocal spectra, or a nonzero duality-odd trace difference as progress by themselves.

## Artifact status

Single durable finding. No clue status change is made here: the broader signed-radial-flux clue remains accepted, but its surviving representation branch is now narrower than simply “use a non-inner target automorphism.”