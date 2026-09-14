# MI-017 — Fixed-order Pohozaev stress is automatic in transmission space; the singular small-order limit is the real analytic gate

**Evidence level:** supported by PL-297--PL-305, sharpened by PL-306--PL-307 and [PL-308](../../findings/PL-308-transmission-pohozaev-weak-virial-stress.md). Fixed-`s` Pohozaev admissibility and weak virial stress are exact; uniform `s->0` compactness, identification with the explicit aperture derivative, and the rational-prime sign theorem remain open.

PL-297 separates renormalized boundary stress from the critical Fourier first moment. PL-298--PL-304 show that generic spectral stability and ordinary forcing norms do not make the logarithmic resolvent a `BV` smoother. PL-305 removes the kernel-side concern: once a fixed state lies in `C_0 cap BV_0`, every prime-power activation and the completed remainder are first-order differentiable in the aperture.

PL-306 showed that squared boundary-stress compactness is not an independent gate if one has Feynman--Hellmann and a mixed moving-domain fractional Hadamard law. PL-307 shortens the route further: a fixed-domain fractional Pohozaev identity already yields the scalar stress once the actual state is admissible.

PL-308 now closes that fixed-order admissibility gate without the high interior Hölder hypotheses that translated boundary cusps can violate. The completed-Weil lower operator preserves the supported Sobolev regularity needed for Grubb's `mu`-transmission bootstrap. For every fixed `s>0`, finitely many bootstrap steps place the eigenstate in `H^{s(sigma)}` for some `sigma>s+1/2`, exactly the range where the low-regularity radial Pohozaev identity applies by Sobolev duality.

The resulting exact weak stress law is

`Gamma(1+s)^2/(2s) (|tau_+|^2+|tau_-|^2) = E_s(w)+a^(2s)[b_a(w)+V_a(w)]`,

where `V_a(w)=2 Re <B_a w,xw'>` is a well-defined transmission-space dual pairing. Whenever classical aperture differentiation is justified, dilation covariance gives `V_a=-b_a-a partial_a b_a` and this reduces to PL-307's explicit derivative formula.

The conceptual shift is important: **translated source fronts are not a fixed-`s` regularity obstruction; they are a reason to work in transmission space.** Reproving high-Hölder regularity or a mixed Hadamard theorem cannot advance the scalar-stress problem. The unresolved analytic currency is uniformity as `s->0`: the number of bootstrap steps grows, the duality indices approach the critical half-order threshold, and neither the transmission constants nor `V_a(w_(s,a))` are shown compact.

The live bridge is therefore to prove source-structured small-`s` convergence of the weak virial pairing, or enough `C_0+BV`/derivative-measure compactness to identify it with PL-305's explicit aperture derivative at `s=0`. Only after that does the arithmetic sign/first-crossing gate become available.

**Boundary.** PL-308 is generic fixed-order elliptic/transmission analysis for the actual finite completed-Weil operator. It does not produce a uniform zero-order limit, signed/pointwise boundary trace, rational-prime rigidity or RH implication. Moving-domain shape calculus can still matter for stronger boundary observables beyond the scalar squared stress.