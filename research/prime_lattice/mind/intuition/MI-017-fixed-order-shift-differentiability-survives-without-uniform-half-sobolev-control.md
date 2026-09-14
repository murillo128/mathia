# MI-017 — Fixed-order stress is automatic; the small-order endpoint lives on an exponential boundary layer

**Evidence level:** supported by PL-297--PL-305, sharpened by PL-306--PL-308 and the explicit small-order boundary-layer obstruction in [PL-309](../../findings/PL-309-small-order-green-trace-boundary-layer.md). Fixed-`s` Pohozaev admissibility and weak virial stress are exact; uniform `s->0` control for the actual completed-Weil branch, identification with the zero-order aperture derivative, and the rational-prime sign theorem remain open.

PL-297 separates renormalized boundary stress from the critical Fourier first moment. PL-298--PL-304 show that generic spectral stability and ordinary forcing norms do not make the logarithmic resolvent a `BV` smoother. PL-305 removes the kernel-side concern: once a fixed state lies in `C_0 cap BV_0`, every prime-power activation and the completed remainder are first-order differentiable in the aperture.

PL-306--PL-308 then remove fixed-order moving-boundary and high-regularity obligations. The completed-Weil lower operator preserves enough supported Sobolev regularity for a finite `mu`-transmission bootstrap at every fixed `s>0`, yielding the exact weak stress law

`Gamma(1+s)^2/(2s) (|tau_+|^2+|tau_-|^2) = E_s(w)+a^(2s)[b_a(w)+V_a(w)]`.

The translated source fronts are therefore not a fixed-`s` obstruction; transmission space is the right setting. The unresolved analytic currency is the singular limit.

PL-309 identifies the scale consumed by that limit. In the one-dimensional fractional Poisson model, the exact Green trace can be written in the stretched variable `r=-s log((1-x)/2)`. Fixed `r` samples forcing at physical distance `exp(-Theta(1/s))` from the boundary, and the positive trace kernel retains total mass tending to one there. Consequently one can choose smooth forcings with `||f_s||_infty=O(sqrt(s))->0` while prescribing an arbitrary finite limit of `tau_(s,+)/sqrt(s)`.

Thus ordinary bulk `C_0`, `L^infty`, norm-resolvent or generic forcing convergence is too weak for the renormalized boundary observable. **The small-order endpoint is a stretched-boundary problem, not merely a bulk compactness problem.** For the actual completed-Weil eigenbranch, either its eigen-equation must control this exponential layer, or the weak-virial/BV route must bypass pointwise trace recovery with uniform estimates strong enough to identify the same scalar limit.

Only after that analytic gate is closed does the rational-prime sign/first-crossing theorem become available. Reproving fixed-order Hölder regularity, or proving bulk convergence that does not see the stretched coordinate, cannot advance this endpoint.

**Boundary.** PL-309 is an externally forced fractional Poisson counterexample, not a counterexample to the completed-Weil eigenbranch. It rules out only generic inferences from bulk convergence to `s^(-1/2)`-renormalized trace. Source-structured cancellation may still control the stretched profile, and the weak virial may converge without pointwise trace convergence.