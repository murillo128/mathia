# MI-049 — Unitary moving compressions have no Berry-trace escape from one-sign ramification

**Evidence level:** exact operator-theoretic synthesis from [WP-348](../../findings/WP-348-congruence-scattering-has-arithmetic-inner-factors-beyond-zeta.md) through [WP-350](../../findings/WP-350-unitary-pre-differentiation-compressions-are-reducing-restrictions-and-berry-terms-cannot-erase-same-sign-ramification-in-trace.md). The unitary-compression and trace identities are exact; no new positivity theorem is supplied for nonunitary defects.

WP-349 showed that after logarithmic differentiation every bad-prime congruence block has one-sign phase velocity, so a positive moving compression cannot average ramification away. WP-350 closes the apparent pre-differentiation escape when the compressed object is still required to be genuine unitary scattering.

Let `U(t)` be unitary on the critical line, `V(t)` an isometric moving channel embedding and `B(t)=V(t)^*U(t)V(t)`. If `B(t)` is unitary, equality in the compression norm forces the selected subspace to be reducing for `U(t)`: the compression is not a lossy mixture but a unitary restriction. For the phase generators

`Q_U=-i dot(U) U^(-1)`, `Q_B=-i dot(B) B^(-1)`,

the moving-frame connection terms appear only as gauge/commutator contributions and cancel in trace:

`tr Q_B = tr(V^* Q_U V)`.

In squarefree congruence scattering the generator splits into the common unramified scalar plus bad-prime terms `F_p(t)`, and WP-349 gives `F_p(t)<=-c_p I` with `c_p>0`. Therefore every nonzero unitary moving restriction retains a strictly negative ramified trace contribution. A Berry/connection term can change the matrix representative inside the moving frame, but it cannot erase that one-sign trace while preserving unitary scattering.

The structural lesson is that **motion of the representation is not itself a new sign resource when the motion remains inside the unitary category**. Requiring the compressed channel to inherit scattering unitarity turns the moving compression into a reducing restriction, and the gauge part of the motion has no trace leverage against a sign-definite local block.

The surviving escape is categorical rather than kinematic. One may allow a proper contraction/nonunitary defect, or replace the scalar/reducing channel picture by a genuinely noncommuting global construction, but then the ordinary unitary Maaß--Selberg/Wigner--Smith Hermitian structure no longer supplies positivity for free. A new source-forced sign theorem is required.

**Boundary.** WP-350 rules out the unitary pre-differentiation moving-subspace/Berry escape for the explicit congruence scattering setting. It does not rule out nonunitary defect constructions, a different noncommutative global operator mechanism, or another positive form not inherited from unitary scattering. It does not prove Weil positivity or RH.