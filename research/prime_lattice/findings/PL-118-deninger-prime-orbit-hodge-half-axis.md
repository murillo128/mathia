# PL-118 — Deninger already supplies prime-orbit log geometry and a Hodge half-axis mechanism; the arithmetic polarization remains missing

## Claim

A global dynamical completion of the prime-exponent energy map

`log n = sum_p v_p(n) log p`

with primes represented by primitive periodic orbits of length `log p`, prime powers represented by repetitions of those orbits, zeta represented by a regularized cohomological determinant, and the line `Re(s)=1/2` forced by a positive Hodge-type structure is already classical prior art in Deninger's program.

For the Riemann zeta function, Deninger's conjectural cohomological formalism asks for a real cohomology `H^i("Spec Z",R)` with flow generator `Theta` such that the completed zeta function is an alternating regularized determinant of `s-Theta`. In the expected degree-one cohomology the spectrum of `Theta` is the nontrivial zeta-zero divisor. If, in addition, degree one carries a positive Hodge-star pairing compatible with the flow and cup product, then one obtains the exact identity

`<Theta f,g> + <f,Theta g> = <f,g>`,

hence

`Theta = (1/2) I + A`

with `A` skew-symmetric/skew-adjoint in the appropriate Hilbert completion. Every degree-one eigenvalue then has real part `1/2`. This is a genuine structural localization mechanism: the half-axis is forced by positivity plus the weight-one scaling of top-degree cohomology, not merely inserted as a reparametrization of the functional equation.

The decisive limitation is existence. For `Spec Z`, the cohomology/determinant/Hodge package required to identify the global degree-one spectrum with the Riemann zeros and then force `Theta-(1/2)I` to be skew-adjoint is not known. Deninger's modern arithmetic dynamical system does realize a substantial part of the prime geometry — closed points occur as compact packets of periodic orbits of length `log N(x)`, hence length `log p` for `Spec Z` — but the construction is explicitly an approximation to the expected system, is infinite-dimensional, has packets rather than one orbit per prime, and does not establish the required global Hodge-polarized cohomology or zeta determinant.

**Evidence/status:** `LITERATURE + EXACT-DERIVED + PRIOR-ART-REDIRECT + OPEN-MECHANISM`.

The periodic-orbit/cohomological program and the Hodge argument are Deninger prior art. The exact operator identity below is rederived from the stated hypotheses to make the load-bearing assumption visible. The line-specific conclusion is a novelty obstruction: a proposal of the form `prime orbit lengths log p + cohomological flow + Hodge star => critical line` is not new. What remains genuinely open is constructing or proving the required arithmetic cohomology, trace/determinant correspondence, and positive polarization for an actual global arithmetic dynamical system.

## Exact determinant and half-axis mechanism

Deninger's 1998 formalism starts locally. For a finite prime `p`, let `R_p` be the real finite Fourier series on

`R / (log p) Z`

with translation flow and infinitesimal generator

`Theta = d/dy`.

The eigenvalues of the complexified generator are the poles of the local Euler factor

`zeta_p(s) = (1-p^(-s))^(-1)`,

and Deninger gives the regularized-determinant identity

`zeta_p(s) = det_infty((s-Theta)/(2 pi) | R_p)^(-1)`.

The global analogy with a projective curve then suggests

`hat zeta(s) = product_(i=0)^2 det_infty((s-Theta)/(2 pi) | H^i("Spec Z",R))^((-1)^(i+1)).`

Under the expected separation of the degree spectra, this forces

- `H^0` to carry eigenvalue `0`,
- `H^1` to have the nontrivial zeros `rho` of zeta as the spectrum of `Theta`, with multiplicity,
- `H^2` to carry eigenvalue `1`.

The determinant formula by itself does not prove RH. The localization enters through a second, genuinely geometric hypothesis. Assume a Hodge operator on degree one and a trace on degree two define a positive scalar product

`<f,g> = tr(f cup (*g))`,

assume the flow acts compatibly with cup product so that `Theta` is a derivation, and assume `Theta` commutes with `*`. Since `Theta=I` on top degree, for degree-one classes one has

`Theta(f cup *g) = f cup *g`.

Using the derivation rule and commuting `Theta` through `*` gives

`f cup *g = (Theta f) cup *g + f cup *(Theta g)`.

Applying `tr` yields exactly

`<Theta f,g> + <f,Theta g> = <f,g>`.

Equivalently, on the common invariant domain,

`A := Theta - (1/2) I`

satisfies

`<Af,g> + <f,Ag> = 0`.

Thus `A` is skew-symmetric, and if the Hilbert completion/domain theory promotes it to the required skew-adjoint operator, its spectrum lies on `iR`. Even at the eigenvector level, if `Theta v=rho v` in the complexified domain then the same identity gives

`2 Re(rho) ||v||^2 = ||v||^2`,

so

`Re(rho)=1/2`.

This isolates the exact source of the critical line. The number `1/2` is half the weight `1` by which the generator acts on top degree. It is not produced by the free prime lattice or by the local circles alone; it comes from a global positive duality structure tying degree one to degree two.

## Relation to the prime-exponent lattice

The bridge to the present line is unusually exact at the prime-power skeleton. Deninger's cohomological reading of the explicit formula has non-archimedean contribution

`sum_p (log p) sum_(k>=1) delta_(k log p)`.

In prime-exponent coordinates, the support point `k log p` is precisely the energy of the axis vector

`k e_p`,

because

`<k e_p,(log q)_q> = k log p = log(p^k)`.

A primitive periodic orbit of length `log p` and its `k`-fold repetition therefore reproduce exactly the prime-power rays that support `-zeta'/zeta` and the non-archimedean side of Weil's explicit formula. This is not merely a verbal prime/orbit analogy: the orbit periods have the same additive energy and the same repetition structure as the exponent-lattice axis rays.

At the same time, this comparison marks an important boundary. The dynamical trace formula is organized by **primitive primes and their repetitions**, not by arbitrary interior lattice points `v(n)` with several nonzero coordinates. Composite multiplication is already generated indirectly by the Euler/Ruelle product. Hence Deninger's mechanism is not a new geometry of the full free commutative lattice. Its extra force comes from global foliation/cohomology, duality, and positivity added to the prime-power skeleton.

This fits the obstruction accumulated in this line. `PL-011` shows that the bare prime Kronecker flow only has the rational-log pure-point spectrum. `PL-033` shows that automorphic scattering can already make the Riemann zeros genuine operator eigenvalues but does not force them onto the symmetry axis. `PL-117` shows that even compatible local Frobenius purity does not localize the global Riemann divisor. Deninger's formalism supplies exactly the kind of missing **global** structure those findings point toward: one cohomological flow generator whose spectrum is the global divisor, plus a positive polarization forcing its centered part to be skew.

## The mechanism is mathematically real in foliated models

The Hodge ingredient is not empty geometric terminology. Deninger and Singhof construct real polarizable Hodge structures on reduced leafwise cohomology for Kähler-Riemann foliations and establish hard Lefschetz and a Kählerian analogue of the Weil-conjecture formalism. Thus positivity/polarization on reduced leafwise cohomology is an established mathematical structure in a substantial class of foliated systems.

Leichtnam's laminated-space model makes the spectral consequence explicit. For a class of foliated laminated spaces with `p`-adic transversal and a scaling flow, under the stated harmonic-form hypotheses he proves a Lefschetz trace formula on leafwise Hodge cohomology and proves that the eigenvalues of the infinitesimal generator on degree one have real part `1/2`. This supplies a matched positive control: conformal/Hodge scaling really can force the half-axis in an honest dynamical cohomology theory.

But this control is not the Riemann-zeta theorem. The model is motivated by Deninger's arithmetic program and function-field examples; it does not construct the required `Spec Z` system whose cohomological determinant is the completed Riemann zeta function. The lesson for this line is therefore structural rather than evidentiary for RH: the Hodge/skew mechanism is coherent and non-vacuous, while the arithmetic realization remains the hard step.

## What Deninger's modern arithmetic system actually realizes

Deninger's current construction, published as *Dynamical systems for arithmetic schemes*, substantially closes the easiest part of the old analogy. For an integral normal arithmetic scheme `X_0` flat and of finite type over `Spec Z`, he constructs an infinite-dimensional continuous-time system `X_0` built from rational Witt-vector spaces and a `Q_{>0}`/Frobenius action. Closed points `x_0` correspond bijectively to compact packets `Gamma_(x_0)` of periodic orbits of length

`log N(x_0)`.

For `X_0=Spec Z`, this gives the desired rational-prime scale `log p`. Each periodic orbit lies in a unique packet. The construction therefore supplies a canonical global arithmetic setting in which the same `log p` values that appear as exponent-lattice coordinate weights are literally return periods of a continuous flow.

However, the paper explicitly separates this from the conjectural zeta machine. The constructed system is described as an **approximation** to the expected analytic space. The prime/closed-point correspondence is packet-valued rather than one-to-one at the orbit level. The system is infinite-dimensional rather than the expected finite dimensionality suggested by arithmetic topology. The paper proves a one-dimensional zeroth foliation cohomology, while noting that the broader cohomological problem persists and that the first foliation cohomology might be the relevant object. It also has no fixed points in the constructed flow, whereas archimedean completion is an essential part of the completed-zeta formalism.

Consequently, it would be incorrect to combine the 1998 desired properties with the modern construction and announce a proof. The following implications remain unestablished for `Spec Z`:

`constructed prime-periodic system`

`-> cohomology with the required determinant/trace formula for hat zeta`

`-> degree-one spectrum exactly equal to the nontrivial zeta zeros`

`-> positive Hodge star/polarization with weight-one flow scaling`

`-> skew-adjointness of Theta-(1/2)I`.

The last arrow is the easy structural calculation; the preceding arithmetic-geometric arrows contain the unresolved content.

## Analytic-continuation boundary

This route correctly diagnoses why a bare Euler-product dynamical picture is insufficient. The identity

`product_p (1-p^(-s))^(-1)`

is initially valid only for `Re(s)>1`. A periodic-orbit Euler/Ruelle product with periods `log p` has the same convergence issue unless a global dynamical/cohomological theorem supplies continuation.

Deninger's conjectural determinant is precisely such a proposed continuation mechanism: the completed zeta function would be defined/represented through the regularized spectrum of a global cohomological generator, while a Lefschetz trace formula would identify its geometric side with prime-orbit repetitions. The continuation is therefore not supposed to arise by evaluating the local Euler product formally in the critical strip.

The current arithmetic dynamical system does not yet establish this determinant identity, so it does not currently cross the analytic-continuation barrier for Riemann zeta. This distinction must be retained in any use of the prime-orbit picture.

## Prior art and novelty audit

The core mechanism is classical and should be treated as a prior-art redirect, not as a Mathia discovery.

- **Christopher Deninger**, “Some analogies between number theory and dynamical systems on foliated spaces,” *Documenta Mathematica*, Extra Volume ICM 1998, Vol. I, 163–186, DOI `10.4171/DMS/1-1/2`. This is the primary source for the local prime circles of circumference `log p`, the regularized determinant formalism, the conjectural global cohomology with degree-one zero spectrum, the explicit-formula trace distribution, and the Hodge-star calculation `Theta=1/2+A` implying RH.
- **Christopher Deninger, Wilhelm Singhof**, “Real polarizable Hodge structures arising from foliations,” *Annals of Global Analysis and Geometry* **21** (2002), 377–399, arXiv `math/0204111`. This constructs real polarizable Hodge structures on reduced leafwise cohomology for Kähler-Riemann foliations and supplies the rigorous Hodge-theoretic background for the proposed mechanism.
- **Eric Leichtnam**, “Scaling group flow and Lefschetz trace formula for laminated spaces with p-adic transversal,” *Bulletin des Sciences Mathématiques* **131**(7) (2007), 638–669, DOI `10.1016/j.bulsci.2006.11.001`, arXiv `math/0603576`. This proves, in a precise laminated-flow model, a Lefschetz trace formula and the degree-one `Re(rho)=1/2` spectral localization under its hypotheses.
- **Christopher Deninger**, “Dynamical systems for arithmetic schemes,” *Indagationes Mathematicae* **37**(1) (2026), 25–136, DOI `10.1016/j.indag.2024.05.007`, arXiv `1807.06400`. This is the current construction anchor: arithmetic closed points produce compact packets of periodic orbits of length `log N(x)`, while the paper explicitly distinguishes the constructed infinite-dimensional approximation from the still-expected cohomological zeta formalism.

A targeted novelty search around Deninger dynamical cohomology, arithmetic flows, leafwise Hodge theory, Lefschetz trace formulas, periodic prime orbits, and modern rational-Witt arithmetic dynamical systems found the full conceptual chain to be established prior art at the conjectural-program level. No novelty is claimed for representing primes by closed orbits of length `log p`, using repeated orbits for prime powers, expressing zeta through a cohomological determinant, or using Hodge positivity to derive the critical half-axis.

The durable line-specific result is the **collision** with the current prime-lattice frontier. After `PL-117`, it is tempting to seek a global cohomological object that turns local prime/Frobenius data into one polarized spectrum. Deninger's program is already almost exactly that proposal. Any new contribution must therefore construct or prove a missing arithmetic piece, not merely restate the architecture in exponent-vector language.

## Adversarial boundaries and counterarguments

1. **The modern periodic-orbit construction is not a proof of the determinant formula.** It realizes prime/closed-point periods but does not identify a degree-one generator spectrum with all nontrivial Riemann zeros.

2. **Packets are not single prime orbits.** The current arithmetic system associates a closed point to a compact packet of periodic orbits. Treating it as a literal one-prime/one-orbit Ruelle system would erase a real structural difference that Deninger records explicitly.

3. **The Hodge identity is conditional but non-tautological.** Once positivity, compatibility, and top-degree weight are granted, `Theta-(1/2)I` being skew is an exact consequence. The hard point is proving those hypotheses for the arithmetic cohomology, not algebraically deriving the `1/2` afterward.

4. **The functional equation alone is weaker.** Poincaré duality naturally pairs spectral parameters `rho` and `1-rho`, reproducing the expected symmetry of the divisor. Positive Hodge polarization is the additional ingredient that turns symmetry about `1/2` into localization on `1/2`.

5. **Local purity is not enough.** The trivial compatible `l`-adic system in `PL-117` is already locally pure and still has global L-function `zeta(s)`. Deninger's load-bearing hypothesis is instead a positive global pairing on a cohomology whose single flow generator carries the global zero divisor.

6. **The full exponent lattice is not the primitive dynamical object.** The trace side sees the prime-power rays `k e_p`; it does not attach primitive closed trajectories to general composite vectors. The extra structure is global dynamical cohomology, not a hidden metric of the positive cone itself.

7. **Skew-symmetric versus skew-adjoint must not be blurred.** The formal bilinear identity gives skew-symmetry on a natural domain. A Hilbert–Pólya conclusion for the full spectrum requires the appropriate closedness/domain/self-adjointness theorem. For individual eigenvectors the real-part calculation is immediate, but a complete spectral theorem needs more.

8. **Function-field/foliated controls do not transfer automatically to `Spec Z`.** They show that the mechanism is mathematically coherent, not that the arithmetic realization exists in characteristic zero.

## Decisive falsification tests

This finding should be withdrawn or materially narrowed if any of the following is false:

1. Deninger's 1998 formalism does not place the poles of the local factor at the spectrum of the translation generator on the `log p` circle, or does not state the regularized local determinant formula.
2. The conjectural global determinant does not put the nontrivial zeta zeros in the degree-one spectrum of `Theta` under the stated spectral separation.
3. The positive Hodge-star/cup-product hypotheses fail to imply `<Theta f,g>+<f,Theta g>=<f,g>` and hence the centered skew identity.
4. Deninger's modern arithmetic system does not associate closed points to compact packets of periodic orbits of length `log N(x)`.
5. The modern construction already proves the completed Riemann-zeta determinant plus the required positive Hodge polarization for `Spec Z`; that would convert the present prior-art/open-mechanism classification into something vastly stronger.
6. A current `PL-*` finding already stores this exact Deninger collision — prime-periodic `log p` geometry together with the Hodge localization identity and the status of the modern arithmetic construction — in which case `PL-118` is duplicate evidence and should not survive as an independent claim.

The first four checks are supported directly by the cited primary literature. The fifth is explicitly contrary to the limitations and open cohomological status described in the modern construction. The sixth was checked against the current `prime_lattice` finding inventory and nearest dependencies `PL-033`, `PL-104`–`PL-105`, and `PL-115`–`PL-117`.

## Consequence for the research line

The search frontier should no longer include, as a potentially new idea, the architecture

`prime directions -> periodic orbits of length log p -> cohomological generator -> zeta determinant -> Hodge positivity -> Re(s)=1/2`.

That architecture is Deninger prior art, and its critical-line step is already exact once the required polarization exists. The useful unresolved target is much sharper: **construct or identify a canonical global arithmetic cohomology/flow for the rational-prime norm system whose trace/determinant genuinely gives completed zeta and whose positive polarization forces `Theta-(1/2)I` to be skew-adjoint.**

This also clarifies the division of labor between existing spectral routes. `PL-033` shows that zero-as-spectrum is already achievable through automorphic scattering without localization. Deninger shows how localization would follow from a stronger polarized cohomology, but that cohomology is not yet available for `Spec Z`. `PL-117` shows why assembling locally pure Frobenius classes is insufficient. The missing theorem is therefore neither another encoding of the zero divisor nor another local purity statement; it is a genuinely global positive duality/trace theorem tying the rational-prime orbit data to one completed spectrum.
