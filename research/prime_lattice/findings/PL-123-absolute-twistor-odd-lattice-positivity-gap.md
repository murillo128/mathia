# PL-123 — The absolute twistor compactification canonically selects the odd exponent face without changing the nontrivial zeta divisor; positivity remains missing

## Claim

Connes and Consani's new 2026 construction of the absolute twistor line and the compactified absolute curve `overline{Spec Z}` adds a mathematically nontrivial archimedean geometry to the arithmetic-site program. The global object is defined inside the **odd arithmetic topos**, dual to the multiplicative monoid of odd positive integers, and the paper states that the restriction of the absolute Frobenius action to odd integers is forced by extension of scalars from `F_1` to the signed base `F_{1^2}`. On complex points the archimedean component carries the canonical fixed-point-free twistor real structure, while the Frobenius dynamics generates Adams operations together with complex conjugation on real Hodge structures.

For `prime_lattice`, the new Frobenius monoid has an exact exponent-vector interpretation:

\[
\mathbf N_{\mathrm{odd}}^\times
\cong
\{\alpha\in \mathbf N_0^{(\mathcal P)}:\alpha_2=0\}
=
\bigoplus_{p\ne2}\mathbf N_0 e_p.
\]

Thus the canonical Frobenius semigroup of the new absolute geometry is not the full positive exponent cone but its codimension-one coordinate face obtained by deleting the `2`-direction. This does **not** mean that the geometric prime `2` is absent from `Spec Z`; it identifies only the global Frobenius-action monoid specified by the `F_{1^2}` structure.

That deletion is harmless for the nontrivial Riemann zero divisor. In `Re(s)>1`,

\[
\zeta^{(2)}(s)
:=\prod_{p\ne2}(1-p^{-s})^{-1}
=(1-2^{-s})\zeta(s).
\]

After using the established meromorphic continuation of `zeta`, this identity extends meromorphically to the plane. Since

\[
1-2^{-s}=0
\quad\Longrightarrow\quad
\Re s=0,
\]

`zeta^(2)` and `zeta` have exactly the same zeros, with multiplicity, in the open critical strip `0<Re(s)<1`. Hence a canonical global geometry whose Frobenius semigroup only sees odd exponent directions can in principle retain the entire nontrivial zeta divisor; the missing `2`-axis is not itself an RH obstruction.

The important limitation is different. The new absolute-twistor construction supplies a canonical real/inversion symmetry and a genuine archimedean completion, but the current paper does not establish a cohomological generator whose spectrum is the Riemann zero divisor, a regularized determinant/trace identity giving the completed zeta function, or a positive polarization/Weil form forcing that spectrum onto the self-dual axis. `PL-118` and `PL-119` show why that distinction is load-bearing: Deninger's Hodge mechanism localizes eigenvalues only after a positive pairing gives `Theta-(1/2)I` skew-adjoint, while Meyer's exact adelic zero-spectrum/explicit-formula realization still permits hypothetical off-axis zeros until positivity/unitarity is imposed.

Accordingly, the fresh absolute-twistor geometry is a **prior-art redirect and structural enrichment**, not an RH mechanism by itself. It makes the archimedean/sign geometry and the odd Frobenius face canonical, but the remaining research target is still an arithmetic positivity/determinant theorem linking that geometry to the completed zeta divisor.

**Evidence/status:** `LITERATURE + EXACT-DERIVED + CURRENT-PRIOR-ART-REDIRECT + OPEN-MECHANISM`. No novelty is claimed for the absolute-twistor construction, the arithmetic site, removal of one Euler factor, or the elementary zero-divisor calculation. The durable line-specific point is the exact exponent-lattice dictionary and the resulting clarification of what the new geometry does and does not add to the current RH frontier.

## 1. The new global Frobenius action is an exact face of the exponent lattice

Let

\[
n=\prod_p p^{\alpha_p},\qquad \alpha=v(n)\in\mathbf N_0^{(\mathcal P)}.
\]

Then `n` is odd exactly when `v_2(n)=0`. Unique factorization therefore gives the canonical monoid isomorphism

\[
\mathbf N_{\mathrm{odd}}^\times
\longleftrightarrow
\bigoplus_{p\ne2}\mathbf N_0 e_p.
\]

Multiplication on odd integers is addition on this face, and the logarithmic energy remains

\[
\log n
=
\sum_{p\ne2}\alpha_p\log p.
\]

Connes--Consani's paper does not choose this restriction as an external convenience. It states that the completed absolute curve is an internal object of the odd arithmetic topos and that extension of scalars to the signed absolute base `F_{1^2}` forces the Frobenius action

\[
x\longmapsto x^n,
\qquad n\in\mathbf N_{\mathrm{odd}}^\times.
\]

This is a genuine new structural feature relative to the bare Bohr torus. The ordinary prime lattice treats every `e_p` symmetrically unless extra arithmetic data are supplied. Here the archimedean/sign extension itself selects a distinguished coordinate parity: the Frobenius semigroup consists precisely of combinations of all prime directions except `e_2`.

The selection should nevertheless be interpreted carefully. `overline{Spec Z}` still contains the finite prime `2`; the statement concerns which power maps act as absolute Frobenius operations on the `F_{1^2}`-geometry. The correct prime-lattice translation is therefore "the Frobenius-action monoid is the odd face," not "the absolute curve deletes the prime 2."

## 2. Removing the `2`-Euler factor preserves every nontrivial zeta zero

The odd face raises an immediate falsification question: can a global object that omits one prime direction from its Frobenius monoid still carry the Riemann zero divisor?

For `Re(s)>1`, absolute convergence gives

\[
\zeta(s)
=(1-2^{-s})^{-1}
\prod_{p\ne2}(1-p^{-s})^{-1}.
\]

Define in that half-plane

\[
\zeta^{(2)}(s)
:=\prod_{p\ne2}(1-p^{-s})^{-1}.
\]

Then

\[
\zeta^{(2)}(s)=(1-2^{-s})\zeta(s).
\]

The continuation step must be stated correctly. The Euler product on the left is **not** being evaluated term-by-term in the critical strip. Instead, once the classical meromorphic continuation of `zeta(s)` is known, the right-hand side defines the meromorphic continuation of `zeta^(2)`, and the identity follows from uniqueness of analytic continuation.

Now

\[
1-2^{-s}=0
\iff
\exp(-s\log2)=1
\iff
s=\frac{2\pi i k}{\log2},\qquad k\in\mathbf Z.
\]

Every zero of the removed local factor therefore lies on `Re(s)=0`. Consequently, throughout

\[
0<\Re s<1,
\]

multiplication by `1-2^{-s}` neither creates nor cancels zeros. It follows exactly that

\[
\operatorname{div}_0\zeta^{(2)}
=
\operatorname{div}_0\zeta
\quad\text{inside the open critical strip,}
\]

including multiplicities.

This is useful for the research line because it eliminates a superficial objection to the odd arithmetic topos. The missing Frobenius generator `2` does not prevent the resulting arithmetic package from being compatible with the full nontrivial zeta divisor. More generally, deleting finitely many Euler factors produces elementary factors whose zeros lie on `Re(s)=0`; for the Riemann critical strip, finite-place deletion is divisor-neutral. What remains difficult is not retention of the divisor but constructing it globally without importing analytic continuation or zeros by hand.

## 3. The archimedean component adds genuine structure beyond the Bohr torus

The new construction is not merely the prime torus with one coordinate removed. Its local archimedean geometry begins from the absence of a preferred ordering at infinity. The two possible orderings give two affine charts of an absolute projective line; an involution exchanges the charts, and passing from `F_1` to `F_{1^2}` retains the canonical sign `epsilon`. After adjoining the formal imaginary generator, the complex points acquire the standard fixed-point-free twistor real structure.

The paper then amalgamates this archimedean component with the affine absolute curve constructed in the authors' earlier 2026 work. That earlier construction already ties the finite primes to exact arithmetic geometry: at each prime `p`, its complex-point structure yields Weil-group torsors and a Tate-curve description whose real locus recovers the adelic periodic orbit

\[
C_p=\mathbf R_+^\times/p^{\mathbf Z}.
\]

The new paper supplies the missing archimedean chart and a global odd-Frobenius action. This is substantially richer than the standard Bohr transform, a generic infinite torus, or a free primon gas. In particular, it survives the line's demand that any serious mechanism eventually include genuinely global/archimedean information rather than only the independent frequencies `log p`.

But richness of geometry is not yet zero localization. On complex points, generating Adams operations and complex conjugation on real Hodge structures gives a canonical symmetry package. Symmetry can pair spectral parameters or encode a real structure; it does not by itself imply a positive Hermitian form or force all parameters onto the fixed/self-dual axis.

## 4. Collision with `PL-118` and `PL-119`: symmetry is not the missing positivity theorem

`PL-118` records Deninger's much older global template. If a degree-one arithmetic cohomology carries a flow generator `Theta`, if the completed zeta divisor is its spectrum, and if a positive Hodge pairing satisfies the expected weight-one compatibility, then

\[
\langle\Theta f,g\rangle+\langle f,\Theta g\rangle
=\langle f,g\rangle.
\]

Equivalently,

\[
\Theta=\frac12 I+A,
\qquad A^*=-A,
\]

under the required domain/self-adjointness hypotheses. That is the mechanism that turns a duality symmetry into the critical-line statement.

`PL-119` supplies an independent control. Meyer's adelic representation already realizes the full completed zero divisor as spectrum and its character as the Weil explicit formula. Hypothetical off-line zeros are still admitted. The missing property is precisely positive-definiteness/unitarity, equivalent in that framework to RH.

The absolute twistor paper should therefore be placed between these two gates. It makes a new global real/Hodge-compatible symmetry geometrically canonical, but the inspected theorem/claim set does not establish the additional chain

\[
\text{absolute twistor curve}
\longrightarrow
\text{cohomology/flow with spectrum }Z(\zeta)
\longrightarrow
\text{completed determinant or Weil trace}
\longrightarrow
\text{positive polarization}
\longrightarrow
\Re\rho=\frac12.
\]

The final implication is structurally understood from Deninger's Hodge argument. The new paper advances the left side of the diagram, especially the archimedean/sign geometry, but does not supply the arithmetic spectral and positivity arrows needed to turn that geometry into RH.

This distinction also prevents a false shortcut. A fixed-point-free twistor involution or complex-conjugation action is not a positivity statement. One can have an involution pairing data correctly while an associated form is indefinite, degenerate, or simply absent. Any future claim that the twistor real structure "explains the critical line" must exhibit the actual positive pairing and prove its compatibility with the operator whose spectrum is independently identified with the Riemann zeros.

## 5. Prior-art and novelty audit

The closest current primary sources are:

- **Alain Connes, Caterina Consani**, *The Absolute Twistor Line and the Geometry of `overline{Spec Z}`*, arXiv:`2609.00299` (first posted 31 August 2026). This is the primary source for the archimedean absolute twistor line, the global curve in the odd arithmetic topos, the `F_{1^2}`-forced restriction to odd Frobenius powers, and the Adams/complex-conjugation action on real Hodge structures.
- **Alain Connes, Caterina Consani**, *On the Absolute Geometry of `Spec Z`*, arXiv:`2606.06604` (2026). This constructs the affine absolute arithmetic curve and relates its complex points at each finite prime to Weil torsors, Tate curves, and the adelic periodic orbits `R_+^×/p^Z`.
- **Alain Connes, Caterina Consani**, *On the Jacobian of `overline{Spec Z}`*, arXiv:`2602.15941` (2026; announced for the *Journal of Noncommutative Geometry*). This identifies the Riemann sector of the adele class space with a monoidal extension of the Picard/Jacobian geometry of the arithmetic curve and supplies the immediate geometric background for the compactification program.

Older arithmetic-site/scaling-site work already makes the multiplicative monoid of positive integers and prime periodic orbits part of Connes--Consani prior art. Therefore none of the following is a Mathia novelty claim: encoding multiplication by a monoid action, assigning prime periods `log p`, using the arithmetic/scaling site, constructing the absolute curve, introducing the twistor line, or restricting Frobenius to odd integers.

The exact identification

\[
\mathbf N_{\mathrm{odd}}^\times
\cong
\{v:v_2=0\}
\]

and the critical-strip divisor invariance under multiplication by `1-2^{-s}` are elementary consequences written here to audit the new work against the `prime_lattice` contract. They are not claimed as new number theory. Their value is diagnostic: they show that the new signed/archimedean geometry is compatible with retaining all nontrivial zeta zeros even though its intrinsic Frobenius semigroup is only the odd face.

A targeted current-literature search found the twistor/odd-topos construction itself only in this newly posted Connes--Consani paper and found no separate theorem closing the zero-spectrum-plus-positive-polarization bridge for this object. This negative audit must be read as a statement about the presently inspected literature, not as a proof that no future or unpublished construction can supply the bridge.

## 6. Adversarial boundaries

1. **The prime `2` is not deleted from `overline{Spec Z}`.** The codimension-one statement refers to the exponent vectors indexing the canonical Frobenius-action monoid. Conflating that action with the set of finite places would be incorrect.

2. **The odd Euler product is not being continued formally.** The identity with `(1-2^{-s})zeta(s)` is first proved in `Re(s)>1`; the strip statement then uses the already known meromorphic continuation of `zeta`. This finding does not derive analytic continuation from the odd arithmetic topos.

3. **Divisor retention is weaker than a geometric derivation of the divisor.** Knowing that removing the `2`-factor cannot alter nontrivial zeros says only that an odd-prime construction is not disqualified on this ground. It does not show that the absolute curve produces the zeros, their multiplicities, or the explicit formula.

4. **A real/twistor involution is weaker than a positive polarization.** Conjugation and inversion can provide the correct symmetry type while leaving an indefinite or unconstrained spectral problem. The RH-level condition in `PL-118`/`PL-119` is positivity/unitarity tied to the zero-carrying operator.

5. **The critical line is not derived from the odd-face lattice.** The relation `v_2=0` singles out a prime coordinate because of the signed absolute base; it does not numerically produce `1/2`. Any half-axis mechanism still needs completion/duality plus a localization theorem.

6. **Finite Euler-factor deletion is not a route to simplify RH.** Although `zeta` and `zeta^(2)` have the same nontrivial divisor, their Euler products remain absolutely convergent only in `Re(s)>1`. Removing one prime does not move the continuation barrier or prove cancellation in the strip.

7. **The fresh geometry is stronger than generic Beurling/Helson controls, but its spectral consequence remains unproved.** The exact rational scheme, signed base, and archimedean construction cannot be dismissed as a freely assignable prime-frequency model. The appropriate control is instead whether the geometry yields a canonical global positive trace/cohomology statement whose validity would fail for matched generalized-prime systems.

## 7. Decisive continuation tests

A materially stronger `prime_lattice` consequence from this absolute-twistor geometry would require at least one new theorem of the following type.

First, construct a canonical cohomology, operator, or representation attached to the compactified absolute curve whose trace or regularized determinant is proved to equal the **completed** Riemann zeta object after analytic continuation, with the nontrivial zeros appearing spectrally without being inserted as input.

Second, derive from the `F_{1^2}`/twistor/Hodge structure a positive pairing or Hodge-index-type inequality compatible with that same zero-carrying operator. A sufficient version would reproduce an identity of the form

\[
\langle\Theta f,g\rangle+\langle f,\Theta g\rangle
=\langle f,g\rangle
\]

on a positive Hilbert completion, with the required domain theorem making `Theta-(1/2)I` skew-adjoint.

Third, show that the resulting positivity is genuinely arithmetic rather than a generic consequence of having an involution or an odd free monoid. A matched control should replace the exact rational-prime norm data by a Beurling/generalized-prime analogue while retaining the same formal symmetry; if the positivity theorem survives unchanged, it has not yet isolated the Riemann arithmetic.

Finally, the finite place `2` must be handled coherently in any completed trace/determinant theory. The divisor calculation proves that its local Euler factor is irrelevant to zeros in the open strip, but a global geometric explicit formula still has a genuine `p=2` local contribution. The odd Frobenius action cannot simply be used to erase that place from the arithmetic trace side.

## Consequence for `prime_lattice`

This fresh result narrows rather than reopens the geometric route. The line can now treat the following package as current prior art:

\[
\text{exact arithmetic curve}
+\text{prime local geometry}
+\text{archimedean absolute twistor line}
+\text{canonical signed real structure}
+\text{odd Frobenius semigroup}.
\]

In exponent coordinates, the final item is exactly the face `alpha_2=0`, and that face is sufficient to retain the entire nontrivial zeta zero divisor after established analytic continuation. Therefore a proposal does not gain novelty merely by adding an archimedean/twistor completion to the prime lattice or by explaining why only odd Frobenius powers act.

The surviving target is sharper: **derive a completed zero-carrying determinant/trace and a positive polarization from this geometry, rather than merely a symmetry.** That is the missing arrow common to the Deninger and Meyer controls and is the point at which the new absolute geometry would have to produce genuinely new RH-relevant structure.