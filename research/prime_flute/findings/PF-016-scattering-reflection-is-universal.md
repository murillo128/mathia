# PF-016 — scattering reflection is universal, and physical relative scattering cannot carry RH zeros as critical-line determinant zeros

**Status:** `DECISIVE-NEGATIVE / LITERATURE+DERIVED`. The classical universality statement is strengthened by an exact operator-theoretic no-go for the relative physical-scattering determinant contemplated by PF-087.

## Claim

For any finite-area hyperbolic surface with finitely many cusps, the Eisenstein/scattering system already has the functional equation

```text
E(z,s) = Phi(s) E(z,1-s),
Phi(s) Phi(1-s) = I,
```

and therefore its scattering determinant satisfies

```text
phi(s) phi(1-s) = 1.
```

On the physical line

\[
s=\frac12+it,
\]

the scattering matrix is unitary. These identities are standard consequences of hyperbolic cusp scattering and do not depend on prime vertices, prime gaps, the exact `cot(pi/p)` embedding, or the interior/exterior reflection of the prime-circle construction.

There is a stronger consequence for the prime-flute program. Suppose the exact prime-flute and the prime-indexed projective reference of PF-087 admit full physical scattering operators on a common cusp-channel Hilbert space,

\[
\Phi_E\!\left(\frac12+it\right),
\qquad
\Phi_0\!\left(\frac12+it\right),
\]

with the standard physical properties:

1. both operators are bounded and unitary at the real energy `t` under consideration; and
2. their difference is trace class,
   \[
   \Phi_E\!\left(\frac12+it\right)
   -
   \Phi_0\!\left(\frac12+it\right)
   \in\mathcal S_1.
   \]

Then the genuine relative physical scattering operator

\[
S_{\rm rel}(t)
:=
\Phi_E\!\left(\frac12+it\right)
\Phi_0\!\left(\frac12+it\right)^{-1}
\]

is unitary and differs from the identity by a trace-class operator. Hence its ordinary Fredholm determinant exists and satisfies

\[
\boxed{
\left|\det_F S_{\rm rel}(t)\right|=1.
}
\]

In particular,

\[
\boxed{
\det_F S_{\rm rel}(t)\neq0
}
\]

at every regular physical energy where the assumptions hold.

Thus a successful completion of PF-087 from its direct channel to a genuine relative **physical** scattering determinant cannot have Riemann zeros as determinant zeros on `Re s=1/2`. If the required full scattering/Fredholm object does not exist, that route fails by nonexistence; if it does exist with the standard self-adjoint scattering properties, it is zero-free on the physical line. This is a no-go dichotomy for the most direct `relative scattering determinant = RH zero carrier` interpretation.

## Exact operator proof

On the physical line unitarity gives

\[
\Phi_0^{-1}=\Phi_0^*.
\]

Therefore

\[
S_{\rm rel}-I
=
(\Phi_E-\Phi_0)\Phi_0^*
\in\mathcal S_1,
\]

because the trace class is a two-sided ideal in the bounded operators. Hence `det_F S_rel` is defined.

The product of two unitary operators is unitary, so

\[
S_{\rm rel}^*S_{\rm rel}=I.
\]

For Fredholm determinants of identity-plus-trace-class operators,

\[
\det_F(AB)=\det_F(A)\det_F(B),
\qquad
\det_F(A^*)=\overline{\det_F(A)}.
\]

Consequently

\[
\begin{aligned}
\left|\det_F S_{\rm rel}\right|^2
&=
\det_F(S_{\rm rel}^*)\det_F(S_{\rm rel})\\
&=
\det_F(S_{\rm rel}^*S_{\rm rel})\\
&=1.
\end{aligned}
\]

No finite-dimensional cusp assumption is used in this last step. Once a countable-channel prime-flute scattering theory produces bounded unitaries with trace-class relative difference, the conclusion is purely Hilbert-space/Fredholm theory.

## Consequence for PF-087

PF-087 proves that the exact/projective **direct-channel** difference

\[
D(s)_{ij}
=
(C_{ij}^E)^{-2s}-(C_{ij}^0)^{-2s}
\]

is trace class for `Re s>1/4`, and therefore defines

\[
\mathfrak D_{\rm dir}(s)=\det(I+D(s)).
\]

But PF-087 explicitly leaves the non-direct double-coset/scattering remainder unresolved. The present no-go explains why that distinction is essential: `I+D(s)` is not known to be a physical unitary scattering operator, so its determinant is not constrained to the unit circle.

If the missing remainder can be supplied so that the resulting operator really is the relative physical scattering operator, then on `Re s=1/2` the completed determinant must satisfy

\[
|\mathfrak D_{\rm phys}(1/2+it)|=1.
\]

Therefore any critical-line zeros of the direct determinant, should they exist, cannot survive as zeros of a physically correct relative-scattering completion. The remainder would have to restore unitarity.

This closes the specific route

\[
\boxed{
\text{exact/projective prime-flute}
\to
\text{full relative physical scattering}
\to
\det_F S_{\rm rel}
\to
\text{Riemann zeros as critical-line determinant zeros}.
}
\]

## What is not ruled out

The result does **not** say that scattering is spectrally empty. A unit-modulus determinant can have a nontrivial phase, and in standard self-adjoint scattering the Birman--Krein formula identifies the relative scattering determinant with the exponential of a real spectral-shift/scattering-phase function, up to sign convention:

\[
\det S_{\rm rel}(\lambda)
=
\exp(\mp 2\pi i\,\xi(\lambda)).
\]

Prime-gap information could therefore in principle enter a scattering **phase**, its derivative/time-delay analogue, or poles and zeros of a meromorphic continuation away from the physical line. Those are different mechanisms and require separate evidence. The present finding rules out only the natural but stronger claim that the ordinary physical Fredholm determinant itself has the RH zeros as zeros on its unitary line.

Nor does the result assert existence of full countable-cusp scattering for the infinite prime-flute. Existing findings already show serious global obstructions. The point is that nonexistence does not rescue the determinant-zero route: the branch fails on either side of the existence dichotomy.

## Interior/exterior duality

The original interior/exterior orthogonal-circle realizations are related by ambient Möbius conjugacy. Physical scattering is invariant under the corresponding unitary conjugation/relabeling of channels, and Fredholm determinants are invariant under bounded similarity in the trace-class setting.

Hence the no-go is duality-preserving. Choosing the exterior rather than the interior realization cannot evade physical-line unitarity or create determinant zeros.

## Relation to the earlier universality negative

The earlier PF-016 conclusion remains valid:

```text
interior/exterior sides
        -> reflection
        -> s <-> 1-s
        -> critical line
```

is not spectrally discriminating, because the same reflection and unitarity arise for ordinary cusped hyperbolic surfaces.

The strengthened conclusion is sharper. Even after replacing absolute scattering by the much more prime-sensitive exact/projective relative construction of PF-087, **physical unitarity still prevents the resulting Fredholm determinant from being an RH zero set on the critical line**.

Thus the mere appearance of

```text
s <-> 1-s,
Re(s)=1/2,
unitarity on the critical line,
```

cannot be evidence that the prime-flute explains the Riemann functional equation or its zeros. Moduli-sensitive pole positions, resonances, scattering eigenphases, residues, and channel couplings remain mathematically meaningful, but a physical-line scattering determinant is intrinsically a phase rather than a vanishing spectral characteristic.

## Prior-art and novelty audit

No novelty is claimed for any operator-theoretic ingredient.

- For finite-area cusped hyperbolic surfaces, standard Eisenstein theory gives meromorphic `Phi(s)`, the functional equation, and unitarity on `Re s=1/2`. A modern explicit reference is Le Masson--Sahlsten, *Quantum ergodicity for Eisenstein series on hyperbolic surfaces of large genus* (Mathematische Annalen; arXiv:2006.14935), §2.6.
- J. Behrndt, M. M. Malamud and H. Neidhardt, *Scattering matrices and Weyl functions*, Proc. London Math. Soc. 97 (2008), 568--598, DOI `10.1112/plms/pdn016`, gives self-adjoint scattering matrices and the Birman--Krein relation in an abstract operator framework.
- Standard relative scattering theory states explicitly that a relative scattering operator which is unitary and differs from the identity by trace class has a determinant of modulus one; this is the usual scattering-phase construction. The same principle is used throughout geometric relative scattering and in Borthwick's *Spectral Theory of Infinite-Area Hyperbolic Surfaces* in the relative-scattering setting.
- The Fredholm determinant identities used above are classical trace-ideal theory.

A directed search found the modulus-one statement explicitly in the general relative-scattering literature; therefore it would be incorrect to claim a new scattering theorem here. The durable project-specific content is the **negative composition with PF-087**:

\[
\boxed{
\text{the very condition needed to promote the prime direct kernel to genuine physical scattering}
\Longrightarrow
\text{zero-freeness of its relative determinant on the RH critical line}.
}
\]

That is a decisive boundary condition on the prime-flute program, not new general scattering theory.

## Evidence level

`proved` conditional on the standard physical-scattering hypotheses (bounded unitarity and trace-class relative difference); `decisive-negative` for using zeros of a genuine relative physical scattering Fredholm determinant as the Riemann zero set on `Re s=1/2`.