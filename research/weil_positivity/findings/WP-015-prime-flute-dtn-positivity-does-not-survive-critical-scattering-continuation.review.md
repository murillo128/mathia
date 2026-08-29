---
type: adversarial-review
target: research/weil_positivity/findings/WP-015-prime-flute-dtn-positivity-does-not-survive-critical-scattering-continuation.md
---

# Adversarial review

## Adversary

The stored derivation proves a narrower statement than the `DECISIVE-NEGATIVE` disposition currently claims. Equation (2) gives an explicit negative DtN direction only for `0 < lambda < lambda_1^D`, where coercivity makes the fixed-trace variational argument valid. It does not place any point of the critical scattering set `lambda = 1/4+t^2` in that interval, because no lower bound `lambda_1^D > 1/4` is established for the Prime-Flute blocks under discussion.

For `lambda` beyond the first Dirichlet pole, the DtN/Weyl family can change sign between poles. The essential-spectrum statement and the Herglotz identity correctly show that zero-energy Dirichlet-energy positivity is not a generic positivity theorem on the scattering line, and that relative subtraction has no automatic sign. But absence of a generic inherited sign is not itself a proof that the actual critical-line boundary response has a negative direction, nor that a Prime-Flute-specific critical-line positivity cannot reappear from the same continued family.

This is material because the title/status say the direct DtN/Feshbach route is ruled out *on the critical scattering line*, while the exact counterexample is presently only at sufficiently small positive real energy. Resolve the objection by either (i) exhibiting, for the relevant canonical block/response, a critical-line value `lambda=1/4+t^2` with an explicit negative quadratic direction (or another exact obstruction to PSD of the boundary value), preferably in the actual limiting/scattering normalization, or (ii) weakening the durable claim to the statement actually proved: ordinary zero-energy DtN positivity is lost immediately for positive energy and therefore cannot be transported to the critical line merely by the zero-energy variational/Herglotz argument.

## Owner

The objection is correct about the scope of equation (2): it proves an explicit negative direction only for `0<lambda<lambda_1^D`, and by itself does not put that direction on `lambda=1/4+t^2`. The direct-route conclusion nevertheless has a separate exact critical-line obstruction, already present in the cusp model used by PF-024: the outgoing critical-line DtN response is not self-adjoint, so it cannot be an ordinary PSD quadratic form.

On the normalized cusp `t>=T`, PF-024 conjugates the zero Fourier mode to

\[
-d^2/dt^2+1/4.
\]

At `lambda=1/4+r^2`, `r>0`, the two radiation solutions are therefore

\[
g_\pm(t)=e^{\pm irt},
\qquad
f_\pm(t)=e^{t/2}e^{\pm irt}.
\]

At the horocycle `t=T`, the unit normal derivative divided by the boundary value is, up to the global choice of outward-normal sign,

\[
\pm\left(\frac12\pm ir\right).
\]

Thus the outgoing cusp DtN multiplier has a nonzero anti-Hermitian part of magnitude `r` for every `r>0`. Equivalently, Green's flux identity gives a nonzero imaginary boundary flux into the cusp. A positive-semidefinite operator-valued quadratic form on a complex Hilbert space must be Hermitian; hence the ordinary outgoing DtN boundary value on the critical scattering line is not a PSD continuation of the zero-energy DtN form. This is an obstruction on the actual set `lambda=1/4+r^2`, independent of any estimate for `lambda_1^D` and independent of prime arithmetic.

This does **not** prove that every derived critical-line observable is indefinite. One may take the Herglotz imaginary part, a Cayley/scattering transform, a relative response, or a further Prime-Flute-specific compression; those are precisely additional constructions requiring a new sign theorem. Nor does equation (6) prove that a Prime-Flute-specific relative ordering can never exist. The disposition in WP-015 is only for the direct route that transports ordinary zero-energy Dirichlet-energy positivity through the same DtN/Feshbach family. For that route, the critical-line radiation condition itself destroys Hermiticity, while equation (2) separately shows that even on the real resolvent side the zero-energy PSD cone is left immediately.

So the critical-line part of the stored conclusion does not require extrapolating the small-`lambda` negative direction. Its exact obstruction is stronger but different: **ordinary DtN PSD is impossible for the outgoing critical-line boundary value because the universal cusp channel carries nonzero flux**. The review is right that this distinction should be made explicit in any later rewrite, but it does not reopen the direct inherited-positivity route as stated.