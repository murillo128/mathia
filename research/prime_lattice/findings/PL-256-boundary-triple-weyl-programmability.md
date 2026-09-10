# PL-256 — Abstract boundary triples make the Dirac domain escape programmable; zeta-specific Weyl positivity is already RH-equivalent

## Claim and status

`PL-255` leaves one genuine escape from the same-square obstruction: change the first-order self-adjoint domain or boundary coupling so that the squared operator is no longer the already-audited designed pseudo-Laplacian. Abstract boundary-triple theory shows that **the existence of such a domain-changing Weyl/resolvent model is not arithmetic rigidity**. Boundary relations realize a very broad class of Nevanlinna families as Weyl data, so a secular equation produced only by choosing boundary data can be highly programmable.

For zeta there is also a sharp matched control. The completed logarithmic derivative

`Q_xi(z) = i xi'/xi(1/2 - i z)`

belongs to the Nevanlinna/Herglotz class exactly when RH holds (the Lagarias criterion as recorded and developed by Suzuki). Under RH Suzuki further identifies a Krein-string Titchmarsh–Weyl function whose spectral measure is supported at squared ordinates of zeta zeros. Thus a divisor-complete zeta Weyl model is available once the decisive positivity has already been supplied; abstract extension theory does not generate that positivity.

The resulting route restriction is precise: a boundary/domain strategy becomes mathematically substantive only if rational-prime or global arithmetic structure independently forces the boundary maps/Weyl family, proves the required self-adjoint/Herglotz positivity, and proves that the secular divisor contains **all** principal `xi` zeros with multiplicities. Merely changing the domain, obtaining a Krein resolvent formula, or selecting boundary data so that desired zeros solve a secular equation does not advance RH.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE` for the abstract/generic boundary-domain route only. This is not a no-go theorem for a source-forced arithmetic boundary construction.

## Boundary triples are exactly the domain-change formalism left open by PL-255

Let `S` be a closed symmetric operator and let boundary maps `(Gamma_0,Gamma_1)` describe self-adjoint extensions. With a reference extension `A_0`, gamma field `gamma(z)`, Weyl function `M(z)`, and self-adjoint boundary parameter/relation `Theta`, the standard boundary-triple machinery gives, under its usual hypotheses, the spectral selection criterion

`lambda in sigma_p(A_Theta) cap rho(A_0)  <=>  0 in sigma_p(Theta - M(lambda))`

and a Krein-type resolvent formula of the form

`(A_Theta-lambda)^(-1) = (A_0-lambda)^(-1) + gamma(lambda)(Theta-M(lambda))^(-1)gamma(bar(lambda))^*`,

up to the conventional sign/parameter normalization used for the boundary maps.

This is exactly the operator-domain degree of freedom isolated in `PL-255`: two first-order realizations can have the same interior differential expression while their boundary conditions change `Dom(D)` and hence `Dom(D^2)`. The formalism therefore confirms that the escape is real, but it also makes clear where any new information must enter: in the *source* of `Gamma_0`, `Gamma_1`, `Theta`, and `M`, not in the abstract existence of the extension calculus.

No Fredholm determinant is needed for this conclusion. Determinantal secular equations require additional finite-rank, trace-class, or Fredholm hypotheses; the kernel criterion and resolvent identity are the invariant level used here.

## Generic realization theorem: abstract Weyl data are programmable

Derkach, Hassi, Malamud, and de Snoo develop boundary relations precisely to encompass generalized boundary data and prove broad realization theorems: Hilbert-space-valued maximal dissipative/Nevanlinna families can be realized as Weyl families of suitable boundary relations, with unitary uniqueness under the corresponding minimality assumptions. Ordinary/unitary boundary triples give narrower strict subclasses, but the boundary-relation framework is deliberately broad enough to realize the full generalized Nevanlinna-family setting relevant here.

This supplies the matched generic control missing from `PL-255`. If a proposed zeta operator starts by prescribing a Nevanlinna/Weyl function whose poles, zeros, or kernel equation already encode the desired zeta divisor, abstract boundary theory can package that function into a symmetric-operator extension problem. The packaging is mathematically legitimate but does not explain the arithmetic divisor. In particular, “there exists a self-adjoint extension whose Weyl function has these spectral points” is not evidence that the prime-exponent lattice forced those points.

The obstruction is therefore analogous to earlier programmability controls in this line: the construction must survive replacement of the arithmetic input by a generic admissible Weyl family. If the claimed RH mechanism survives that replacement unchanged, it is a boundary-theoretic re-encoding rather than a rational-prime rigidity mechanism.

## Zeta-specific control: Weyl/Herglotz positivity is already RH-equivalent

Suzuki studies the completed Riemann function `xi` without any illegal termwise continuation of the Euler product. A central zeta-specific analytic object is

`Q_xi(z) = i xi'/xi(1/2 - i z)`.

The Lagarias criterion recorded there states that

`RH  <=>  Q_xi is a Nevanlinna/Herglotz function in the upper half-plane`,

with the corresponding positivity also expressible through the zeta screw function and Weil's Hermitian form. Thus the sign condition that would make `Q_xi` legitimate passive/self-adjoint Weyl data is not a free consequence of abstract boundary theory: it already carries the RH content.

Suzuki also relates this positivity to Krein strings. Under RH, the associated Titchmarsh–Weyl function belongs to the appropriate string Weyl class and has a partial-fraction/spectral representation supported at the squared ordinates of the nontrivial zeta zeros. Consequently, once RH supplies the Herglotz property, a self-adjoint one-dimensional spectral model can be reconstructed. This is strong prior art for the desired “all zeros in one Weyl function” direction, but it reverses the proof obligation: **one must derive positivity independently rather than obtain it by first assuming the zeros are on the critical line**.

This sharpens `PL-043`. The earlier finding showed that de Branges/canonical-system positivity is the missing zeta-specific condition; the present finding shows that moving the same hope into the exact domain-changing boundary-triple escape from `PL-255` does not avoid that condition because general Weyl realization is itself flexible.

## The spectral-parameter reality test

There is nevertheless a useful exact target. For a nontrivial zero

`s = beta + i gamma`,

use the functional-equation-invariant parameter

`lambda = s(1-s)`.

A direct calculation gives

`lambda = beta(1-beta) + gamma^2 + i gamma(1-2 beta)`,

hence

`Im(lambda) = gamma(1-2 beta)`.

For a nonreal zero (`gamma != 0`), therefore

`lambda in R  <=>  beta = 1/2`.

So a **source-forced, divisor-complete self-adjoint realization** in the spectral parameter `s(1-s)` would imply RH immediately: self-adjointness makes every spectral `lambda` real, and divisor completeness makes every principal `xi` zero participate. This is not itself a proof or construction. It separates the two obligations that previous routes repeatedly conflate: spectral reality and divisor completeness.

The same calculation is also a falsification test. A proposal that proves self-adjointness but captures only a selected sub-divisor has the `PL-254` defect. A proposal that captures the full divisor by prescribing its Weyl function but cannot prove the Herglotz/self-adjoint sign from independent arithmetic structure has the programmability defect isolated here.

## Adversarial audit

The negative claim has deliberately narrow scope.

1. The generic-realization obstruction would fail if the cited boundary-relation theorem did not cover the broad Nevanlinna/maximal-dissipative family being invoked. The Derkach–Hassi–Malamud–de Snoo framework does cover that generalized setting; the finding does not overstate the narrower ordinary-boundary-triple subclass.
2. The zeta control would fail if `Q_xi` being Nevanlinna were merely a consequence of RH rather than an equivalence. Suzuki records the Lagarias equivalence and the equivalent screw/Weil positivity formulations.
3. No determinant identity is asserted without Schatten/Fredholm hypotheses. The argument uses only the standard extension kernel criterion and Krein resolvent formula.
4. No Euler product is continued termwise. The zeta-specific object is the completed, analytically continued `xi` function.
5. The finding does **not** rule out an arithmetic boundary construction. It is escaped by a construction in which prime/global geometry independently determines the boundary data, proves their Nevanlinna positivity, and proves that the resulting secular divisor equals the full principal `xi` divisor with multiplicity.
6. The parameter `s(1-s)` reality calculation is elementary and exact, but by itself only says what a successful full-divisor self-adjoint model would imply; it supplies neither the model nor the missing positivity.

## Prior-art and novelty assessment

The new durable content is a route-closing synthesis, not a claim that boundary triples, Weyl functions, Krein strings, or the zeta Herglotz criterion are new. Derkach–Hassi–Malamud–de Snoo supply the generic realization control; Suzuki supplies the zeta-specific positivity and string/Weyl control. The elementary `s(1-s)` calculation supplies the exact self-adjoint reality test.

Internal duplication was checked against the live line. `PL-208` explicitly left unbounded/domain-changing, boundary-triple, and singular-perturbation actions outside its bounded common-domain resolvent-transport obstruction. `PL-255` then identified a changed first-order domain/boundary coupling as the only genuine way for a Dirac construction to escape same-square spectral inheritance. `PL-043` already warned that zeta-derived canonical-system positivity is essentially RH content, but did not close this later boundary-domain escape using the general Weyl-family realization theorem and the zeta Titchmarsh–Weyl/string prior art. `PL-254` concerns a specific designed pseudo-Laplacian selector rather than generic boundary programmability.

Accordingly, the contribution of `PL-256` is the precise redirect: **abstract domain change is too programmable to be the missing arithmetic mechanism, while zeta-specific Weyl positivity is already the hard condition.**

## Line consequence

The `prime_lattice` frontier should no longer treat “alter the Dirac domain / introduce a boundary triple” as a mechanism by itself. A viable first-order or extension-theoretic route must now exhibit all of the following in one source-forced construction: boundary data derived independently from rational-prime/global structure; self-adjointness or Nevanlinna positivity proved from that structure rather than assumed from RH; and a two-way divisor theorem showing that the secular condition contains **every** principal `xi` zero with multiplicity.

This preserves the current master requirement rather than redefining it. The surviving target remains a nonfactorizing, divisor-complete global relation for the principal zeta factor, now with an additional boundary-theory audit: if admissible Weyl data can be freely substituted without destroying the claimed argument, the construction has not yet used the prime lattice in a restrictive way.

## References

- `SOURCES.md` item 86: Vladimir Derkach, Seppo Hassi, Mark Malamud, Hendrik de Snoo, “Boundary relations and their Weyl families,” *Transactions of the American Mathematical Society* **358**(12) (2006), 5351–5400, DOI `10.1090/S0002-9947-06-04033-5`.
- `SOURCES.md` item 87: Masatoshi Suzuki, “Aspects of the screw function corresponding to the Riemann zeta-function,” *Journal of the London Mathematical Society* **108**(4) (2023), 1448–1487, DOI `10.1112/jlms.12785`.