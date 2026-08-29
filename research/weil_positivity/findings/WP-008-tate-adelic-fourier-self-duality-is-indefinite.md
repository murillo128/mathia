# WP-008 — Tate adelic Fourier self-duality is an involution with both signs, not a positivity theorem

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the direct Tate-self-duality route.

## Claim

`PL-014` identifies the Prime-Lattice valuation skeleton with the finite-idelic quotient and shows that Tate's adelic Fourier--Mellin theory supplies something the bare lattice lacks: the archimedean place, product formula, additive Fourier structure, Poisson summation, analytic continuation, and the canonical self-dual axis `Re(s)=1/2`.

A tempting next step for the Weil-positivity line is therefore:

```text
Prime-Lattice valuation skeleton
    -> full Tate adelic completion
    -> self-dual Fourier involution
    -> positive Hermitian form
    -> Weil positivity.
```

The third arrow fails already on the exact global Schwartz--Bruhat space. With the standard additive character of `A_Q/Q` and self-dual Haar measure, the adelic Fourier transform `F_A` is unitary and satisfies

\[
F_A^2 f(x)=f(-x).
\tag{1}
\]

Hence on the even subspace it is a self-adjoint involution. But it has **both** eigenvalues `+1` and `-1` there. In fact, with

\[
\phi_f=\mathbf 1_{\widehat{\mathbf Z}}
      =\bigotimes_p \mathbf 1_{\mathbf Z_p},
\tag{2}
\]

and

\[
g_0(x)=e^{-\pi x^2},
\qquad
g_2(x)=\left(x^2-\frac{1}{4\pi}\right)e^{-\pi x^2},
\tag{3}
\]

both global factorizable Schwartz--Bruhat functions

\[
\Phi_+=g_0\otimes\phi_f,
\qquad
\Phi_-=g_2\otimes\phi_f
\tag{4}
\]

are even, have **identical finite-place data**, and satisfy

\[
F_A\Phi_+=+\Phi_+,
\qquad
F_A\Phi_-=-\Phi_-.
\tag{5}
\]

Consequently the most direct Hermitian form furnished by Fourier self-duality,

\[
Q_F(f)=\langle f,F_A f\rangle,
\tag{6}
\]

obeys

\[
Q_F(\Phi_+)=\|\Phi_+\|_2^2>0,
\qquad
Q_F(\Phi_-)=-\|\Phi_-\|_2^2<0.
\tag{7}
\]

Thus **Tate self-duality explains the symmetry axis and the functional equation, but it does not supply a positive form.** The sign obstruction survives after the exact global adelic completion and occurs while the complete finite local factor is held fixed.

This rules out the natural branch in which the missing Weil positivity is expected to follow directly from the unitary/self-dual nature of Tate's Fourier transform. Any successful adelic continuation must introduce an additional operation -- for example a nontrivial compression, quotient, relative/cohomological pairing, intersection form, or boundary construction -- whose positivity is a theorem not already equivalent to Weil positivity.

## 1. The exact Tate setting

For `Q`, choose the standard global additive character on `A_Q/Q` and the corresponding self-dual Haar measure. Tate Fourier theory gives a unitary operator

\[
F_A:L^2(\mathbf A_\mathbf Q)\to L^2(\mathbf A_\mathbf Q)
\]

preserving the Schwartz--Bruhat space and satisfying Fourier inversion (1).

At every finite prime, the standard character has conductor `Z_p`, and the self-dual measure is normalized by

\[
\operatorname{vol}(\mathbf Z_p)=1.
\]

Therefore

\[
F_p\mathbf 1_{\mathbf Z_p}=\mathbf 1_{\mathbf Z_p}.
\tag{8}
\]

It follows that the finite basic vector (2) is self-dual:

\[
F_f\phi_f=\phi_f.
\tag{9}
\]

This is exactly the unramified finite test vector used in the standard Tate factorization of the completed Riemann zeta integral.

At the real place, under the normalization

\[
(F_\infty f)(\xi)=\int_{\mathbf R} f(x)e^{-2\pi i x\xi}\,dx,
\tag{10}
\]

the Gaussian is self-dual:

\[
F_\infty g_0=g_0.
\tag{11}
\]

The second even Hermite mode has the opposite eigenvalue. This can be checked directly without invoking Hermite theory. Since

\[
F_\infty[x^2e^{-\pi x^2}]
=\left(-\xi^2+\frac{1}{2\pi}\right)e^{-\pi\xi^2},
\tag{12}
\]

we obtain

\[
F_\infty\left[\left(x^2-\frac{1}{4\pi}\right)e^{-\pi x^2}\right]
=-\left(\xi^2-\frac{1}{4\pi}\right)e^{-\pi\xi^2}.
\tag{13}
\]

Combining (9), (11), and (13) gives the global eigenvalue identities (5).

No zero of `zeta`, explicit-formula kernel, regularization, or hand-picked prime weight enters this calculation.

## 2. Why the sign obstruction is genuinely global and matched

The counterexample is stronger than observing abstractly that a Fourier transform can have phases.

The two test functions in (4) have the **same finite adelic component**

\[
\bigotimes_p\mathbf 1_{\mathbf Z_p}.
\]

All finite-prime local data are therefore matched exactly. The only change is between two canonical even archimedean Fourier modes. Yet the sign of (6) flips.

So a claim of the form

```text
"the full adelic product, including the infinite place,
 is self-dual; therefore its natural Fourier pairing is positive"
```

is falsified without changing a single finite local factor.

This matters specifically for `WP-004`--`WP-007`. Those findings progressively isolated the missing ingredient as a global operation that must retain the exact finite Mangoldt data while coupling it canonically to the archimedean/polar sector. Tate theory indeed provides such a global coupling at the level of analytic continuation and functional equation. But **the coupling is unitary, not order-positive**.

## 3. The self-dual critical axis is not the same thing as a positive Fourier eigenspace

`PL-014` proves the classical character identity

\[
\chi^\vee=\chi^{-1}|\cdot|,
\]

so for

\[
\chi=\eta|\cdot|^s
\]

with `eta` unitary,

\[
\chi^\vee=\overline\chi
\quad\Longleftrightarrow\quad
\Re(s)=\frac12.
\tag{14}
\]

Equation (14) is a precise and valuable explanation of why the critical line is the Hermitian/unitary self-dual axis of the functional-equation involution. But it is a **duality statement on characters**, not a theorem that `F_A` is a positive operator.

A unitary involution may have both signs. Equations (5)--(7) show that Tate's global Fourier operator does so even on the even Schwartz--Bruhat sector and even with the standard finite basic vector fixed.

Thus the implication

```text
self-dual axis -> positive Hermitian form
```

is not available for free. It is exactly the extra step a successful Weil-positivity geometry must supply.

## 4. Positive functions of the Fourier involution are tautological and too small

One can of course manufacture positive operators from `F_A`. On the even subspace let

\[
P_\pm=\frac{I\pm F_A}{2}.
\tag{15}
\]

Then

\[
\|P_+f\|^2\ge0,
\qquad
\|P_-f\|^2\ge0.
\tag{16}
\]

More generally, any bounded operator depending only on the even Fourier involution by functional calculus has the form

\[
g(F_A)=g(1)P_+ + g(-1)P_-.
\tag{17}
\]

If it is positive, then simply

\[
g(1)\ge0,
\qquad
g(-1)\ge0.
\tag{18}
\]

Such positivity is universal Fourier spectral calculus. It sees at most the two Fourier-parity sectors on the even space. It cannot by itself resolve the infinitely many arithmetic atoms

\[
\frac{\Lambda(p^k)}{p^{k/2}}
\]

or generate the finite-prime plus archimedean decomposition of the Weil functional.

The same objection applies to `F_A^*F_A=I`: the resulting norm positivity is exact but arithmetic-free.

Therefore replacing the indefinite pairing (6) by a positive projector norm does not escape the obstruction. It removes precisely the arithmetic content the research line needs to explain.

## 5. Where nontrivial arithmetic can enter -- and where positivity ceases to be automatic

Tate's proof becomes arithmetically meaningful not because `F_A` is positive, but because it couples additive Fourier transform to multiplicative scaling/Mellin characters, the embedding of `Q`, and Poisson summation.

The explicit formula requires still more: logarithmic scaling/conductor information and a completed trace/distributional comparison. Once one couples Fourier duality to multiplication by `log|x|`, scaling generators, cutoffs, quotients, or trace operations, the resulting operator is no longer merely a positive function of a unitary involution. Its sign has to be established separately.

This is exactly consistent with close prior art:

- Burnol's local conductor/scattering formulations recover explicit-formula terms through additional graded/trace structure rather than from bare Fourier positivity;
- Connes--Consani's archimedean Weil positivity comes from a **compression of the scaling action onto a Sonin-type subspace**, not from `F_A` being positive;
- Connes--Consani--Marcolli's global adele-class cohomological program obtains a Lefschetz/trace organization, while the global positivity analogue remains the missing geometric input.

So Tate theory should be treated as the canonical **global self-dual completion**, not as the independent positivity theorem itself.

## 6. Relation to earlier `weil_positivity` findings

This finding narrows one of the main surviving branches rather than replacing previous obstructions.

- `WP-004` found an exact positive Prime-Lattice operator whose atoms are `Lambda(n)/sqrt(n)` on prime powers.
- `WP-005` showed that positivity is lost under the exact autocorrelation lift needed for the finite Weil quadratic term.
- `WP-006` showed that the most naive Arakelov class completion is too destructive: principal Prime-Lattice vectors become class-trivial.
- `WP-007` showed that the canonical Green/screw completion preserves the full Weil data but makes positivity exactly RH-equivalent.
- `PL-014` identified Tate's full adelic Fourier--Mellin completion as a canonical way to add the missing global and archimedean structure.
- `WP-008` now shows that **the self-duality in that completion is itself sign-indefinite** and therefore cannot be promoted directly to the missing Weil positivity.

The surviving target becomes more specific:

```text
Prime-Lattice finite axis data
    + genuine Q-specific adelic/global completion
    + an additional nontrivial geometric operation
        (compression / relative quotient / cohomology / intersection / boundary law)
    + an independent positivity theorem
    -> completed Weil functional.
```

The third line is essential. Omitting it gives Tate duality but no positivity; choosing it to be the already-completed Weil kernel returns the circularity of `WP-007`.

## 7. Prior art and novelty assessment

No novelty is claimed for adelic Fourier analysis, self-dual Haar measure, Fourier inversion, Hermite eigenfunctions, Tate zeta integrals, or the critical self-dual axis.

- Tate's thesis is the primary classical source for the global Fourier--Poisson mechanism and the functional equation.
- Poonen's notes give an audit-friendly modern treatment of self-dual local/adelic measures, Fourier inversion, the standard unramified vectors, zeta integrals, and the twisted character dual.
- Connes--Consani and Connes--Consani--Marcolli are close prior art showing that serious positivity programs add compression/cohomological structure beyond bare adelic Fourier duality.

The Mathia-specific contribution is the **matched-sign obstruction** (4)--(7) applied to the route opened by `PL-014`: two global even test vectors with exactly the same finite local data already give opposite signs for the direct Fourier Hermitian form. This converts the vague warning "functional equation does not imply RH" into an explicit operator-level no-go for one natural proposed source of positivity.

## 8. Boundary conditions and falsification tests

The obstruction is deliberately narrow.

It does **not** rule out:

- a compression of scaling/Fourier dynamics whose positivity follows from an independent theorem;
- a relative or cohomological quotient in which the relevant form changes signature;
- an arithmetic intersection form on a genuinely larger global object;
- a boundary/scattering construction where the Weil form appears as a Schur complement or response operator;
- any mechanism where `F_A` is one ingredient but positivity comes from additional geometry.

It rules out the direct assertion that Tate Fourier self-duality itself supplies the required positive form.

The finding can be falsified by any failure of the following exact checks:

1. with standard self-dual local data, verify `F_p 1_{Z_p}=1_{Z_p}`;
2. verify `F_infinity e^{-pi x^2}=e^{-pi x^2}` under the `e^{-2pi i x xi}` convention;
3. verify equation (13), hence the even `-1` Fourier eigenfunction;
4. tensor the local identities to obtain (5);
5. evaluate (6) on both eigenvectors to obtain the opposite signs (7).

A future construction **escapes** rather than falsifies `WP-008` only if it identifies the additional geometric operation and proves its positivity independently of RH/Weil positivity.

## Consequence for the research line

The adelic route remains one of the few completions that satisfies an important requirement left open by the Beurling controls: it is genuinely specific to `Q`, includes the infinite place, and produces the correct global functional-equation architecture. But its most obvious candidate source of positivity is now eliminated.

The critical line being a unitary self-dual axis is a symmetry statement. **Symmetry is not positivity.** On the exact Tate Hilbert space the Fourier involution already has positive and negative even directions with identical finite-prime data. Therefore the sought Mathia mechanism, if it exists in the adelic direction, must be an additional geometric sign theorem rather than a consequence of self-duality alone.
