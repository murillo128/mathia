# PL-120 — Suzuki’s unconditional screw Hilbert space leaves an RH-equivalent metric-identification gap

## Claim

Masatoshi Suzuki’s whole-line Weil/screw-function construction closes a natural escape left by the recent prime-lattice operator funnel. It is possible to construct a **positive Hilbert norm from the completed zeta data unconditionally**, before assuming the Riemann hypothesis. What is not automatic is that this positive norm is the Weil Hermitian form whose positivity localizes the Riemann zeros.

For `psi in C_c^infinity(R)`, Suzuki defines an unconditional transform `P_hat_D` from a zeta screw line and the norm

`||psi||_0 := pi^(-1/2) || P_hat_(D psi) ||_(L^2(R))`.

He proves that this is a genuine norm and lets `H_0` be the corresponding Hilbert completion. His Theorem 1.4 / Theorem 4.5 then gives the exact equivalence

`RH <=> ||psi||_0^2 = <psi,psi>_W  for every psi in C_c^infinity(R)`, 

where `<.,.>_W` is the Weil Hermitian form. Under RH, `H_0` agrees with the Hilbert completion `H_W` of the Weil form, and `H_W` is isomorphic to a de Branges/model space in which a self-adjoint extension of multiplication has the Riemann-zero ordinates as eigenvalues.

Thus an unconditional positive Hilbert space can already be manufactured from the exact zeta/explicit-formula machinery. **The RH-level content is the arithmetic identification of that positive metric with the Weil metric**, not the existence of a positive metric by itself. This is a decisive negative for any route of the form “construct a positive `L^2`/pullback norm from the prime-power explicit formula, then infer critical-line localization from positivity” unless the construction independently proves the norm-identification theorem.

**Evidence/status:** `LITERATURE + EXACT-DERIVED + PRIOR-ART-REDIRECT + DECISIVE-NEGATIVE` for auxiliary-positive-Hilbertization as a localization mechanism. No novelty is claimed for Suzuki’s Hilbert spaces, screw transform, de Branges model, or RH-equivalent norm identity. The line-specific contribution is the collision with `PL-043`, `PL-044`, `PL-118`, and `PL-119`: even after the completed arithmetic data have produced an unconditional positive Hilbert norm, the missing positive polarization is still exactly the theorem identifying that norm with the zero-sensitive Weil form.

## The unconditional positive norm

Suzuki starts from the completed xi-function and the zeta screw line. With

`E_xi(z)=xi(1/2-i z)+xi'(1/2-i z)`

and `Theta_xi=E_xi^sharp/E_xi`, he defines a family `S_t(z)` built from `Theta_xi` and a function `P_t(z)`. The important point for the present audit is that this family is defined and belongs to `L^2(R)` without assuming RH.

For nonnegative `t`, the explicit formula for `P_t` contains pole terms, an archimedean gamma/Hurwitz--Lerch sector, a `zeta'/zeta(1/2-i z)` term, and the finite non-archimedean sum

`sum_(n<=exp t) Lambda(n)/sqrt(n) * (exp(-i z(t-log n))-1)/(i z)`.

Suzuki explains that this expression is the version rewritten without inserting the zero set, using Weil’s explicit formula. The apparent singularities at zeta zeros are cancelled in the full screw-line expression, and for fixed `t` the resulting `S_t` lies in `L^2(R)`.

For a test function `phi`, he defines

`P_hat_phi(z) = integral_R S_t^sharp(z) phi(t) dt`,

and takes `D psi=i psi'`. Then

`||psi||_0 = pi^(-1/2) ||P_hat_(D psi)||_2`.

Suzuki proves unconditionally that this is a norm on `C_c^infinity(R)`. Its completion is the Hilbert space `H_0`. Hence positivity of this metric is not conjectural and does not use RH.

This is more than the generic observation that every injective map into a Hilbert space defines a pullback norm. Here the map is canonically built from the completed zeta screw line and Weil-explicit-formula data. It therefore passes the weak test “does exact zeta arithmetic enter the construction?” while still demonstrating that **positive Hilbertization alone is not the needed rigidity**.

## The metric equality is exactly RH

Let

`<psi_1,psi_2>_W = W(psi_1 * tilde(psi_2))`

be the Weil Hermitian form. Weil’s criterion gives

`RH <=> <psi,psi>_W >= 0  for all psi in C_c^infinity(R)`.

Suzuki’s stronger norm formulation identifies the precise missing bridge. Theorem 1.4 states

`RH <=> ||P_hat_(D psi)||_2^2 = pi <psi,psi>_W  for every psi`,

or equivalently, by the definition of `||.||_0`,

`RH <=> ||psi||_0^2 = <psi,psi>_W  for every psi`.

The left side of the last equality is positive unconditionally. The right side is the zero-sensitive arithmetic form. Therefore the construction does not prove positivity of the Weil form by merely writing it as an `L^2` norm: **the assertion that it equals that `L^2` norm is itself RH-equivalent**.

Suzuki also obtains a restricted equality criterion on an unconditionally constructed subspace `V^circ(0)`,

`2 ||psi||_(L^2)^2 = <psi,psi>_W`,

again equivalent to RH when required for all vectors in that test family. This reinforces the same boundary: replacing inequalities by a positive norm equality is a useful reformulation, but the equality remains the hard theorem.

## Prime-exponent interpretation

The non-archimedean part of Suzuki’s explicit `P_t` is supported on the von Mangoldt function. Hence only

`n=p^k`

contribute, and in exponent coordinates these are exactly the axis vectors

`v(n)=k e_p`,

with energy

`log n = <k e_p,(log q)_q> = k log p`.

The finite cutoff `n<=exp t` is therefore the energy cutoff `k log p<=t` on the prime-power rays. This is the same axis skeleton isolated in `PL-013` and the threshold geometry used throughout `PL-044`--`PL-066`.

The important conclusion is negative but arithmetic-specific. Even when the exact rational-prime axis data, the completed archimedean sector, and the continued zeta logarithmic derivative are assembled into a canonical whole-line transform, one can obtain an unconditional positive Hilbert norm **without** obtaining the RH positivity statement. What remains is a global identity coupling that norm to the Weil form.

This also shows why an arbitrary Beurling-control objection is not needed for the present no-go. The failure occurs already for the genuine rational-prime completed object: the positive auxiliary space exists, but the zero-localizing metric identification is still equivalent to RH.

## Conditional Hilbert--Polya realization and the precise logical boundary

Assume RH. Then `E_xi` is Hermite--Biehler and `Theta_xi` is meromorphic inner. Suzuki proves that the Weil completion `H_W` is isomorphic, via Fourier/model-space maps, to the de Branges space `H(E_xi)` and the model space `K(Theta_xi)`. He also proves that under RH

`H_0 = H_W`

and the corresponding unconditional model `K_0` agrees with `K(Theta_xi)`.

General de Branges theory then supplies self-adjoint extensions of the multiplication operator. For the distinguished extension used by Suzuki, the zero ordinates `gamma` of `xi(1/2-i z)` form the eigenvalue set. Thus, **conditional on RH**, the Weil Hilbert space is a genuine Hilbert--Polya space.

This must not be read backward. Suzuki explicitly notes that the multiplication-extension formula can still be written without RH, but its operator properties become unclear. Off RH one cannot simply import the de Branges self-adjointness because the Hermite--Biehler/inner structure is precisely what fails to be known. The conditional spectral theorem therefore does not supply an independent proof of the line localization.

There is also a useful technical warning: in Suzuki’s distinguished self-adjoint extension, each `gamma` occurs as an eigenvalue with multiplicity one, even if the corresponding zeta zero has higher multiplicity. The construction realizes the zero locations, not their analytic multiplicities. This does not affect the present no-go but prevents overstating the spectral correspondence.

## Relation to the current prime-lattice frontier

`PL-043` established that ambient de Branges/Sonine geometry is too flexible and that zeta-specific Hermite--Biehler/Hamiltonian positivity is the hard condition. `PL-044` showed that localized self-adjointness and real characteristic zeros can already occur before any prime term is active. `PL-118` recorded Deninger’s global Hodge mechanism, where a positive polarization would force `Theta-(1/2)I` to be skew. `PL-119` then showed via Meyer that one can already have the exact global zero spectrum and the exact Weil trace distribution while positivity/unitarity remains equivalent to RH.

Suzuki’s `H_0` construction closes a remaining loophole between those observations. One might hope that the missing positivity could be obtained by first constructing a canonical positive Hilbert norm from the completed arithmetic data and then identifying the zero representation inside it. But the strongest direct version of that strategy is already present: the positive norm exists unconditionally, and the theorem that it is the **correct** Weil norm is exactly RH.

Thus the surviving target is narrower than “find a positive zeta-derived Hilbert space.” It must prove an **independent arithmetic compatibility theorem** identifying a positive metric/polarization with the Weil/zero-sensitive form, or otherwise force the same sign condition without assuming the zero localization that it is meant to prove.

## Analytic-continuation boundary

No Euler product is formally continued into the critical strip in this finding.

Suzuki’s construction uses the completed `xi` function, the meromorphic continued `zeta'/zeta`, the gamma factor, and a version of the screw line rewritten using Weil’s explicit formula. The finite von-Mangoldt sum records the non-archimedean prime-power sector, while the remaining terms supply the pole and archimedean completion. The identity is therefore a statement about the analytically continued/completed object.

The earlier 2023 screw-function paper likewise derives its one-sided transform from the Euler/Dirichlet expansion only in the valid half-plane and obtains the global zero representation by Fourier inversion/continuation. It explicitly proves that the global screw-kernel positivity is equivalent to RH rather than assuming that the Euler product itself continues as a convergent prime product.

## Prior art and novelty audit

Primary sources:

- **Masatoshi Suzuki**, “On the Hilbert space derived from the Weil distribution,” *Canadian Journal of Mathematics* (published online 3 November 2025), DOI `10.4153/S0008414X25101739`, arXiv:`2301.00421`. Theorem 1.4 gives the RH-equivalent norm identity; Section 3.3 constructs `H_0` unconditionally; Theorem 5.6 identifies `H_0` with `H_W` under RH; Section 6 gives the conditional Hilbert--Polya/self-adjoint-extension realization and explicitly warns that the corresponding unconditional operator properties are unclear.
- **Masatoshi Suzuki**, “Aspects of the screw function corresponding to the Riemann zeta-function,” *Journal of the London Mathematical Society* **108**(4) (2023), 1448--1487, DOI `10.1112/jlms.12785`, arXiv:`2206.03682`. This is the underlying zeta screw-function source: it gives an explicit formula including the von-Mangoldt prime-power contribution, proves several unconditional analytic properties, and proves that the global screw-function positivity property is equivalent to RH.
- **Hiroyuki Yoshida**, “On Hermitian forms attached to zeta functions,” in *Zeta Functions in Geometry* (Tokyo, 1990), Advanced Studies in Pure Mathematics **21** (1992), 281--325. Classical finite-interval Weil-Hermitian predecessor cited by Suzuki. Its finite-window completion method does not extend to the whole line in the way needed for the global Weil Hilbert space.

The exact unconditional `H_0` construction and the RH-equivalent norm identity are Suzuki’s results, not Mathia discoveries. A targeted repository audit found no existing `PL-*` finding centered on this unconditional-positive-space versus Weil-metric-identification split. The nearest stored results are `PL-043`, `PL-044`, `PL-118`, and `PL-119`; the present finding is complementary because it rules out the additional inference that **any** canonical positive Hilbert norm derived from the completed zeta data supplies the missing polarization.

## Adversarial boundaries

1. **`H_0` is genuinely unconditional, but that does not make the Weil metric unconditional.** The completion under `||.||_0` exists without RH. Its identification with the completion under `<.,.>_W` is conditional and, at the test-function level, RH-equivalent.

2. **The construction is not prime-free.** Unlike the small-aperture control in `PL-044`, the whole-line screw transform includes the exact von-Mangoldt prime-power sector and the completed archimedean terms. The negative conclusion therefore cannot be dismissed as a consequence of having omitted arithmetic.

3. **Positivity of an auxiliary pullback norm is tautological at the Hilbert-space level.** The substantive theorem would be the arithmetic equality between this norm and the Weil form. Any future construction must expose where that equality comes from rather than treating positivity of the auxiliary norm as evidence for RH.

4. **The conditional de Branges spectrum is not an unconditional Hilbert--Polya proof.** Self-adjointness and the zero-eigenvalue statement use the RH-dependent Hermite--Biehler/inner identification. Writing the formal multiplication extension off RH is not enough.

5. **The result does not rule out proving the metric identity.** An independent proof of `||psi||_0^2=<psi,psi>_W` from arithmetic structure would prove RH and would be a major substantive mechanism. This finding only records that constructing either side separately is already prior art.

6. **The prime-exponent lattice still enters only through prime-power rays in the explicit-formula channel.** Mixed exponent vectors do not become new primitive geometric data in this construction. Any full-lattice contribution would need an additional theorem coupling interior lattice points to the global metric identity.

## Consequence for the research line

The current funnel can now be sharpened:

`exact prime-power/archimedean completed data -> unconditional positive screw Hilbert space` already exists;

`exact zero spectrum / explicit-formula character` already exists by Meyer;

`positive Weil metric / unitary or Hodge polarization -> critical-line localization` is the remaining hard step.

Therefore the next viable prime-lattice mechanism must not merely produce a positive Hilbert space, a self-adjoint operator after an RH-dependent identification, or another completed explicit-formula transform. It must prove a **non-circular compatibility law** that forces the arithmetic Weil form to coincide with a positive metric (or otherwise forces Weil positivity), and that law must genuinely use structure not already automatic in the screw/de Branges/adelic models.