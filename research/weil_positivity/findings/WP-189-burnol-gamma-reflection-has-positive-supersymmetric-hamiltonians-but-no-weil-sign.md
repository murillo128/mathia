# WP-189 — Burnol's Gamma reflection has nonnegative supersymmetric Hamiltonians, but their positivity does not orient the Weil phase

**Status:** `LITERATURE+DERIVED + EXACT-ARCHIMEDEAN-CARRIER + POSITIVE-SUSY-HAMILTONIAN + CATEGORY-EXIT + PHASE-SIGN-DECOUPLING + PRIOR-ART-CLASSICALIZATION + DECISIVE-NARROWING + MATCHED-CONTROL + NOT-WEIL-POSITIVITY`.

`WP-188` proves that the exact archimedean phase

\[
R_\infty(t)
=\pi^{it}
\frac{\Gamma(\tfrac14-\tfrac{it}{2})}
     {\Gamma(\tfrac14+\tfrac{it}{2})}
\tag{1}
\]

cannot be an ordinary trace-class Birman--Krein scattering determinant. That does **not** mean that the Gamma phase cannot be the reflection phase of a positive differential system. A targeted prior-art audit finds an exact classical category exit: Burnol's Fourier-scattering construction produces Dirac systems whose scalar Schrödinger partners are supersymmetric nonnegative operators, while their reflection phases realize the Fourier-cosine Gamma multiplier and hence (up to the incoming/outgoing convention) exactly `R_infty`.

The decisive point for this research line is negative:

\[
\boxed{
\text{nonnegative scattering Hamiltonian}
\not\Rightarrow
\text{one-signed Gamma/Weil phase velocity}.
}
\tag{2}
\]

Indeed the same exact Gamma phase has the sign-changing velocity already derived in `WP-170`. Thus an independently positive Hamiltonian can carry the exact real-place scattering factor while its positivity is mathematically **decoupled** from the signed observable that enters the explicit formula. This supplies a concrete matched control against a tempting category-exit route left open by `WP-188`: finding a positive singular/domain-changing scattering Hamiltonian for `R_infty` is not enough. The required theorem must order the particular quadratic/relative observable that reduces to the Weil form, not merely the generator whose waves scatter.

This does not solve the finite--archimedean problem. Burnol's construction is classical, purely archimedean, and does not produce the finite Mangoldt selector or the polar/global counterterms. Its value here is to separate two notions of positivity that can otherwise be conflated.

## 1. Burnol's Fourier scattering leaves the ordinary trace-class category

For the cosine and sine transforms, Burnol introduces Fredholm determinants `d_+(u)` and `d_-(u)` of compressed Dirichlet kernels and the real functions

\[
\mu_\pm(u)
=
\sqrt{-\frac{d^2}{du^2}\log d_\pm(u)}.
\tag{3}
\]

The associated first-order system at spectral parameter `t` is

\[
\alpha'
=-\mu_\pm\alpha-t\beta,
\qquad
\beta'
=+\mu_\pm\beta+t\alpha.
\tag{4}
\]

Each component satisfies a Schrödinger equation

\[
L_{\pm,-}\alpha=t^2\alpha,
\qquad
L_{\pm,+}\beta=t^2\beta,
\tag{5}
\]

with

\[
L_{\pm,-}
=-\frac{d^2}{du^2}+\mu_\pm^2-\mu_\pm',
\qquad
L_{\pm,+}
=-\frac{d^2}{du^2}+\mu_\pm^2+\mu_\pm'.
\tag{6}
\]

Burnol proves that the corresponding reflection phase shifts realize the Fourier cosine and sine transforms as scattering matrices. Crucially for comparison with `WP-188`, these are not ordinary short-range two-sided trace-class perturbations of a free full-line Hamiltonian: Burnol records that the potentials vanish exponentially as `u -> -infinity` but grow exponentially as `u -> +infinity`. Waves come from the asymptotically free end and are reflected by the growing end. The construction therefore changes the scattering category exactly where the `L^1` spectral-shift obstruction of `WP-188` says a successful carrier must change it.

There is consequently no contradiction between the existence of Burnol's reflection model and `WP-188`. The latter excludes an ordinary trace-class Birman--Krein determinant on a full scattering tail; the former is an absolute/one-sided reflection problem with a confining end.

## 2. The scalar Hamiltonians are nonnegative by exact factorization

Define on `C_c^\infty(R)`

\[
A_\pm=\frac{d}{du}+\mu_\pm(u),
\qquad
A_\pm^*=-\frac{d}{du}+\mu_\pm(u).
\tag{7}
\]

Then the two scalar operators in (6) factor exactly as

\[
\boxed{
L_{\pm,-}=A_\pm^*A_\pm,
\qquad
L_{\pm,+}=A_\pm A_\pm^*.
}
\tag{8}
\]

Therefore their quadratic forms satisfy

\[
\langle f,L_{\pm,-}f\rangle
=\|A_\pm f\|_2^2\ge0,
\qquad
\langle f,L_{\pm,+}f\rangle
=\|A_\pm^*f\|_2^2\ge0.
\tag{9}
\]

In particular the natural nonnegative self-adjoint realizations obtained from these closed/Friedrichs forms have spectrum bounded below by zero. This positivity is not inferred from RH, zeta zeros, or the desired explicit-formula sign. It is the ordinary supersymmetric factorization theorem of the differential system.

Thus the proposed control is genuinely strong: the exact real-place scattering carrier can coexist with an independent operator-positive theorem.

## 3. Its reflection phase is the same Gamma carrier as `WP-169`

The Mellin spectral multiplier of the scale-invariant Fourier cosine transform is the functional-equation factor

\[
\chi_0(s)
=
\pi^{s-1/2}
\frac{\Gamma((1-s)/2)}{\Gamma(s/2)}.
\tag{10}
\]

On the critical line `s=1/2+it`,

\[
\chi_0\!\left(\frac12+it\right)
=
\pi^{it}
\frac{\Gamma(\tfrac14-\tfrac{it}{2})}
     {\Gamma(\tfrac14+\tfrac{it}{2})}
=R_\infty(t).
\tag{11}
\]

Depending on whether incoming versus outgoing waves, or the inverse scale action, is chosen as the scattering convention, the reflection coefficient is written as (11), its inverse, or differs by a constant unitary factor. None of these convention changes matters below: inversion negates the phase velocity and a constant phase leaves it unchanged.

Burnol's construction therefore supplies an explicit differential-scattering realization of precisely the classical phase identified internally in `WP-169`. This is stronger than merely observing that a Gamma function occurs in a potential: the scattering multiplier itself is the real-place functional-equation phase.

## 4. Positive Hamiltonian does not give positive phase velocity

Write

\[
R_\infty(t)=e^{i\phi(t)}.
\tag{12}
\]

`WP-170` derives exactly

\[
\phi'(t)
=
\log\pi
-
\operatorname{Re}\psi\!\left(\frac14+\frac{it}{2}\right)
=-A_\infty(t),
\tag{13}
\]

where `A_infty` is the nonconstant archimedean Weil symbol. Moreover `A_infty(t)` is strictly increasing for `t>0`, satisfies `A_infty(0)<0`, tends to `+infinity`, and has a unique zero

\[
t_0\approx6.2898359888.
\tag{14}
\]

Hence

\[
\phi'(t)>0\quad(0<t<t_0),
\qquad
\phi'(t)<0\quad(t>t_0).
\tag{15}
\]

If the inverse reflection convention is used, every sign in (15) reverses, but the sign change remains. Therefore neither orientation converts the supersymmetric positivity (9) into a one-sided scattering-phase density.

This is a direct falsification, not a heuristic about time delay. Equations (8)--(9) give a positive operator theorem, while (13)--(15) give the exact response entering the archimedean explicit formula. They coexist in the same scattering construction and have different sign content.

The distinction is structural. `L >= 0` says that the energy spectral parameter is `t^2 >= 0`; it does not order the derivative of the reflection phase with respect to `t`. A scattering phase is a relative boundary observable, not the expectation value of the Hamiltonian itself.

## 5. Why this does not evade the earlier passivity obstructions

At first sight the result may look inconsistent with `WP-170`, which proves that `R_infty` is not an ordinary scalar Schur/inner passive boundary response. There is no inconsistency. Burnol's construction is precisely outside that analytic category.

The Gamma factor has a non-Blaschke zero divisor in either causal half-plane orientation, and its boundary phase velocity changes sign. The Fourier-scattering model realizes it instead through a one-sided confining reflection geometry whose coefficients grow at one end. It is not a bounded analytic characteristic function of the ordinary Herglotz/Schur type.

Likewise `WP-188` rules out ordinary trace-class spectral shift, not all singular reflection geometries. Burnol supplies a concrete surviving carrier of the latter kind. What the present finding adds is that **this successful carrier does not carry the desired positivity through to the explicit-formula observable**.

The resulting classification is therefore:

\[
\boxed{
\begin{array}{c}
\text{ordinary passive/trace-class carrier}\;\longrightarrow\;\text{exact Gamma phase obstructed},\\[2mm]
\text{Burnol singular reflection carrier}\;\longrightarrow\;\text{exact Gamma phase realized,}\;L\ge0,\\[1mm]
\hfill\text{but phase/Weil sign not ordered.}
\end{array}
}
\tag{16}
\]

## 6. Matched controls and failure modes

Several controls prevent overinterpreting (8).

**Scattering orientation.** Replacing `R_infty` by `R_infty^{-1}` only changes `phi'` to `-phi'`; a function that changes sign remains sign-changing. A fixed phase normalization does not affect `phi'` at all.

**Supersymmetric partner.** Passing from `A^*A` to `AA^*` preserves nonnegativity. Darboux/supersymmetric partner changes therefore do not turn Hamiltonian positivity into a sign theorem for the Gamma phase.

**All-degree / non-arithmetic control.** The Fourier-cosine system is an archimedean harmonic-analysis construction. It exists without a prime specialization, Mangoldt support, zeta zero data, or the Mathia finite selector. Thus its positivity cannot by itself distinguish the arithmetic target from matched non-prime controls.

**Finite-place control.** Nothing in (3)--(11) creates the finite-prime term `Lambda(n)/sqrt(n)` or a mixed finite--archimedean incidence relation. The construction is a separated real-place carrier.

**Polar/global control.** The pole/constant terms of the completed explicit formula are not generated by the supersymmetric factorization. Adding them by hand would violate the branch mandate's source-forced-completion gate.

These controls show why the result is a narrowing rather than a candidate solution.

## 7. Prior art and novelty audit

No novelty is claimed for the Fourier Gamma multiplier, Burnol's scattering construction, or supersymmetric factorization of the partner Schrödinger equations.

- Jean-François Burnol, *Des équations de Dirac et de Schrödinger pour la transformation de Fourier*, C. R. Acad. Sci. Paris, Ser. I 336 (2003), 919--924, DOI `10.1016/S1631-073X(03)00223-1`, arXiv `math/0302102`. Burnol constructs the Dirac systems, displays the partner Schrödinger potentials `mu^2 +/- mu'`, records their one-free-end/one-growing-end behavior, and states that their reflection phase shifts realize the cosine and sine Fourier transforms as scattering matrices.
- Jean-François Burnol, *The Explicit Formula and the conductor operator*, arXiv `math/9902080` (1999), together with *Spectral Analysis of the local Conductor Operator*, arXiv `math/9811040` (1998). These works identify the local explicit-formula contribution with the spectral analysis of `log|x|+log|y|` and identify the critical-line logarithmic derivative of the Tate Gamma factor as the conductor spectral function. They are the direct classical boundary against treating a Gamma-phase derivative/conductor operator as a new Mathia positivity mechanism.
- Jean-François Burnol, *On Fourier and Zeta(s)*, Forum Mathematicum 16 (2004), 789--840, DOI `10.1515/form.2004.16.6.789`, already anchors `WP-169`'s identification of the functional-equation factor as the Mellin multiplier of the scale-invariant Fourier transform.

The Mathia-specific durable delta is the **cross-classification** with `WP-170` and `WP-188`: the exact carrier excluded from ordinary passive and trace-class categories has a classical singular reflection realization whose scalar Hamiltonians are independently nonnegative, yet the very same Gamma phase has a sign-changing velocity. This makes Burnol's model a decisive matched counterexample to the inference

\[
\text{positive scattering geometry}\Rightarrow\text{Weil-sign geometry}.
\tag{17}
\]

A targeted audit did not find a theorem in this classical construction converting the supersymmetric Hamiltonian energy into the global Weil quadratic form; Burnol's conductor analysis instead identifies the local explicit-formula observable with the signed Gamma logarithmic derivative itself. Thus the route classicalizes before reaching the research mandate's sign gate.

## 8. Consequence for `weil_positivity`

`WP-188` left singular/domain-changing or generalized scattering as a legitimate carrier category. That category must now be split more sharply.

A candidate does **not** advance the program merely by producing:

\[
\text{positive/self-adjoint Hamiltonian}
\;\longrightarrow\;
\text{exact }R_\infty\text{ reflection phase}.
\tag{18}
\]

Burnol already supplies such a classical control, and its phase velocity still changes sign. To pass the branch mandate, a new construction must instead identify a **specific positive form, quotient, index pairing, relative energy, or other ordered observable** whose own local-to-global reduction yields the finite Mangoldt contribution, the archimedean Gamma term, and the polar/global counterterms together. The sign theorem must apply to that assembled observable itself.

This leaves genuinely stronger category exits open: a source-forced renormalized/relative pairing with its own coercivity theorem, an infinite or noncommutative finite--archimedean incidence structure, or another construction in which positivity acts only after the finite and real places have been coupled. What is closed is the weaker hope that semiboundedness of an archimedean scattering Hamiltonian can serve as the missing Weil positivity theorem.

## Dependencies

- `research/weil_positivity/findings/WP-169-pointed-nyman-relative-phase-is-exact-archimedean-scattering.md`
- `research/weil_positivity/findings/WP-170-archimedean-phase-is-not-a-passive-inner-boundary-response.md`
- `research/weil_positivity/findings/WP-188-exact-gamma-phase-is-not-an-ordinary-trace-class-birman-krein-scattering-determinant.md`
- `research/weil_positivity/SOURCES.md` — Fourier/co-Poisson and scattering controls.

## Bottom line

The exact Gamma phase does admit a positive differential scattering carrier once one leaves ordinary passive/trace-class realization theory: Burnol's Fourier-scattering systems have supersymmetric scalar Hamiltonians `A^*A` and `AA^*`, hence nonnegative quadratic forms, while their reflection phases realize the Fourier-cosine Gamma factor.

That is **not** the missing geometric Weil positivity. The exact reflection phase has a sign-changing derivative, the construction is purely archimedean and classical, and it supplies neither finite-prime incidence nor polar/global completion. The durable lesson is stricter: positivity must belong to the explicit-formula observable after global assembly, not merely to a Hamiltonian that happens to scatter with the correct Gamma phase.