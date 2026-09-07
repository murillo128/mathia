# PL-207 — Fixed-edge resolvent reparameterization is only affine scalar transport

**Status:** negative result / structural collapse  
**Evidence class:** `EXACT-DERIVED + CLASSICAL-RESOLVENT-IDENTITY + DECISIVE-NEGATIVE` for spectral-parameter-independent bounded left transport with exact reparameterized resolvent covariance  
**Research line:** `prime_lattice`

## Claim

The spectral-parameter-shift escape left open by `PL-206` does not become a richer prime-lattice operator mechanism merely by allowing an arbitrary reparameterization of the resolvent variable while keeping one bounded left edge independent of that variable.

Let `H_0,H_1` be closed densely defined operators on a Hilbert space, with resolvents

\[
R_j(z)=(H_j-z)^{-1}.
\]

Let `U` contain at least two distinct points, let `phi:U -> rho(H_0)` satisfy `U subset rho(H_1)`, and suppose one bounded operator `A`, independent of `z`, obeys

\[
\boxed{R_1(z)=A R_0(\phi(z))}\qquad (z\in U).
\]

Then for every distinct `z,w in U`,

\[
\boxed{A=aI},\qquad
\boxed{a=\frac{\phi(z)-\phi(w)}{z-w}\ne0}.
\]

Consequently, if `U` contains at least three points, or more generally if the relation holds on a nontrivial resolvent domain, all divided differences agree and

\[
\boxed{\phi(z)=az+b}
\]

for constants `a != 0` and `b`. The two operators are then related only by the corresponding affine scalar change

\[
\boxed{H_1=a^{-1}(H_0-bI)}.
\]

Thus exact spectral reparameterization with a fixed bounded left edge has no operator-valued freedom: the edge scalarizes and the parameter map is affine. In particular, the canonical logarithmic prime move

\[
H_1=H_0+(\log p)I
\]

appears as the translation case

\[
A=I,\qquad \phi_p(z)=z-\log p.
\]

Allowing the prime action to move the spectral parameter therefore does not evade the fixed-edge obstruction unless the transfer operator itself depends on the spectral parameter or some other hypothesis of this architecture is abandoned.

## 1. Hilbert's resolvent identity forces the edge to be scalar

For `j=0,1`, Hilbert's first resolvent identity gives

\[
R_j(z)-R_j(w)=(z-w)R_j(z)R_j(w)
\]

whenever both parameters lie in the relevant resolvent set.

Using the assumed transport and applying the identity to `R_0` at `phi(z),phi(w)` gives

\[
\begin{aligned}
R_1(z)-R_1(w)
&=A\bigl(R_0(\phi(z))-R_0(\phi(w))\bigr)\\
&=(\phi(z)-\phi(w))A R_0(\phi(z))R_0(\phi(w)).
\end{aligned}
\]

Applying the same identity directly to `R_1` gives

\[
\begin{aligned}
R_1(z)-R_1(w)
&=(z-w)R_1(z)R_1(w)\\
&=(z-w)A R_0(\phi(z))A R_0(\phi(w)).
\end{aligned}
\]

Subtracting and factoring yields

\[
A R_0(\phi(z))
\Bigl((\phi(z)-\phi(w))I-(z-w)A\Bigr)
R_0(\phi(w))=0.
\]

The first factor is `R_1(z)`, hence injective. Therefore

\[
\Bigl((\phi(z)-\phi(w))I-(z-w)A\Bigr)
R_0(\phi(w))=0.
\]

The range of a resolvent of a closed densely defined operator is its domain, so

\[
\operatorname{Ran}R_0(\phi(w))=\operatorname{Dom}H_0
\]

is dense. The operator in parentheses is bounded. It consequently vanishes on the whole Hilbert space:

\[
(\phi(z)-\phi(w))I=(z-w)A.
\]

For `z != w`, this proves

\[
A=\frac{\phi(z)-\phi(w)}{z-w}I.
\]

The scalar cannot be zero, because `A=0` would force the nonzero resolvent `R_1(z)` to vanish. In particular `phi(z) != phi(w)` whenever `z != w`: injectivity of the parameter map is a consequence, not an additional assumption.

No self-adjointness, compactness, Schatten hypothesis, normality, or arithmetic input is used. The load-bearing assumptions are exact resolvent families, dense domains, a bounded left edge, and independence of that edge from the spectral parameter.

## 2. Three spectral points force an affine parameter map

The same bounded operator `A` occurs for every pair of distinct points. Hence every divided difference of `phi` equals the same scalar `a`:

\[
\frac{\phi(z)-\phi(w)}{z-w}=a.
\]

Fixing one `w` gives

\[
\phi(z)=az+b,
\qquad
b=\phi(w)-aw.
\]

Substitution into the transport relation gives

\[
R_1(z)=a(H_0-(az+b)I)^{-1}.
\]

Define

\[
K=a^{-1}(H_0-bI).
\]

Then

\[
(K-z)^{-1}=a(H_0-(az+b)I)^{-1}=R_1(z).
\]

Equality of one resolvent determines the underlying closed operator, so

\[
H_1=K=a^{-1}(H_0-bI).
\]

Therefore arbitrary nonlinear spectral motion is incompatible with a fixed exact left transport. The only surviving maps are the ordinary affine transformations already induced by scalar rescaling and translation of the generator.

The distinction between two and three spectral points is important. Two points already force `A` to be a scalar equal to that pair's divided difference, but two values alone do not determine a globally affine map away from those points. The family statement needs a third point or a genuine parameter domain.

## 3. Consequence for a homogeneous prime-semigroup action

Suppose now that each prime direction is represented by a spectral-parameter-independent bounded edge `A_p` and a parameter map `phi_p`, with the same pair acting at every exponent-lattice vertex. Applying the theorem edgewise gives

\[
A_p=a_p I,
\qquad
\phi_p(z)=a_p z+b_p.
\]

If the parameter maps are required to represent the commuting prime-exponent semigroup, then

\[
\phi_p\circ\phi_q=\phi_q\circ\phi_p,
\]

which is equivalent to

\[
\boxed{(a_p-1)b_q=(a_q-1)b_p.}
\]

This leaves only two elementary affine regimes.

If every `a_p=1`, all prime maps are translations

\[
\phi_p(z)=z+b_p.
\]

The corresponding generator update is

\[
H_{\alpha+e_p}=H_\alpha-b_p I.
\]

Choosing `b_p=-log p` gives

\[
H_\alpha=H_0+\sum_p\alpha_p\log p\,I
       =H_0+(\log n(\alpha))I,
\]

which is exactly the canonical logarithmic energy translation already present in the prime-exponent model.

If some `a_r != 1`, commutativity forces all nontranslation maps to share one fixed spectral point. Writing

\[
c=\frac{b_r}{1-a_r},
\]

one obtains

\[
\phi_p(z)=c+a_p(z-c)
\]

for every `p` with `a_p != 1`, while any member with `a_p=1` must have `b_p=0`. After recentering at `c`, the entire action is only a commuting family of scalar dilations.

This classification does not use any special arithmetic property of the rational primes. The same affine family can be assigned to a free multiplicative semigroup or to generalized-prime directions. It therefore cannot by itself distinguish the Riemann zeta problem from matched multiplicative controls.

## 4. Relation to the existing operator branch

`PL-206` proved that a fixed bounded left edge satisfying

\[
R_1(z)=A R_0(z)
\]

at two distinct spectral parameters must be `A=I` and `H_1=H_0`. It consequently left two formal ways to retain nontrivial exact transport: let the edge depend on `z`, or move the spectral parameter.

The present finding closes the second option **while the edge remains fixed**. Replacing the same-parameter relation by

\[
R_1(z)=A R_0(\phi(z))
\]

does not create a new operator cocycle. Hilbert's identity forces `A` to be scalar and `phi` to be affine. The canonical prime translation is the `a=1` case and carries no residual operator datum beyond the scalar energy shift.

This is consistent with `PL-025`. Reversibly implementing exact `log p` energy translation by unitaries for two multiplicatively independent primes forces the spectrum of a self-adjoint generator to be all of `R`; the one-sided positive-lattice realization avoids that conclusion only by using proper isometries. The current result concerns a different architecture—left transport between resolvents—but reaches the same design boundary from the resolvent identity itself: exact fixed prime edges cannot hide a nontrivial zero-selecting operator behind a change of spectral coordinates.

What remains genuinely outside the theorem is the `z`-dependent transfer from `PL-206`, where

\[
R_1(z)=A(z)R_0(z)
\]

forces a nontrivial propagation law for `A(z)-I` rather than scalarization. Also outside are parameter-dependent left-right or conjugation actions, unbounded/domain-sensitive transport, approximate or ideal-valued covariance, non-fiberwise coupling, and source actions that do not reduce to one fixed edge between neighboring fibers.

## 5. Prior art and novelty audit

The algebraic input is classical. Hilbert's resolvent identity is standard operator theory; a modern survey emphasizing the resolvent and Hilbert identities as organizing tools is Leon A. Takhtajan, “Etudes of the resolvent,” *Russian Mathematical Surveys* **75**(1) (2020), 147–186, DOI `10.1070/RM9917`, arXiv `2004.11950`.

A targeted literature search for fixed bounded left intertwiners of the form

\[
R_1(z)=A R_0(\phi(z))
\]

and for automorphisms/reparameterizations of pseudo-resolvent families did not identify a source presenting this exact affine-collapse statement as a named theorem. That absence is not a novelty claim: the proof is an immediate rigidity consequence of the classical resolvent identity once this particular transport ansatz is posed.

The durable mathematical delta is therefore line-specific. `PL-206` explicitly retained parameter movement as a possible exact escape from same-parameter fixed-edge triviality. The calculation above shows that, under the same bounded fixed-left architecture, arbitrary parameter movement adds no genuine degree of freedom beyond scalar affine changes of the generator. No novelty is claimed for Hilbert's identity, affine resolvent rescaling, or general pseudo-resolvent theory.

## 6. Boundary conditions and adversarial checks

### Spectral-parameter independence of `A` is load-bearing

If the transfer is `A(z)` rather than one fixed bounded `A`, the pairwise factorization above no longer gives a common scalar. `PL-206` derives the corresponding forced propagation law, but does not trivialize all such families. The present finding must not be read as closing that branch.

### Exact equality is load-bearing

A compact, Schatten, trace-class, norm-small, or asymptotic error destroys the exact factorization used above. No affine classification is asserted for approximate or ideal-valued covariance.

### Left transport is load-bearing

Relations with operators on both sides, conjugation, boundary triples, scattering matrices, or genuinely non-fiberwise actions are not instances of `R_1(z)=A R_0(phi(z))` unless they first reduce to that exact form. They require separate programmability and arithmetic-rigidity audits.

### Dense domain is used exactly once

After injectivity removes the left resolvent, the proof obtains a bounded operator vanishing on `Ran R_0(phi(w))=Dom H_0`. Density extends that equality to the full space. If one leaves ordinary resolvents of closed densely defined operators, this step must be rechecked.

### The prime-semigroup corollary assumes homogeneous commuting parameter maps

The edgewise affine theorem does not by itself say that coefficients are independent of the lattice vertex. The displayed `p,q` classification applies only when one deliberately asks for a homogeneous representation of the commuting prime directions at the parameter-map level. Vertex-dependent affine data are not ruled out here, although they still scalarize edge by edge and would need an additional nonprogrammable compatibility law to become arithmetically meaningful.

### No zeta continuation is used

The result is pure operator algebra. It neither analytically continues an Euler product nor constrains Riemann zeros. Its significance is only that it removes a natural operator-design escape before zero-sensitive arithmetic enters.

## Falsification / audit test

The central claim is falsified by any example of closed densely defined `H_0,H_1`, a set `U` containing three distinct common admissible spectral points, a nonlinear map `phi:U -> rho(H_0)`, and one bounded nonzero operator `A` independent of `z` such that

\[
(H_1-z)^{-1}=A(H_0-\phi(z))^{-1}
\]

for every `z in U`.

Such an example would have to evade the factorization

\[
R_1(z)
\Bigl((\phi(z)-\phi(w))I-(z-w)A\Bigr)
R_0(\phi(w))=0,
\]

so apparent counterexamples should first be checked for failure of exact equality, boundedness or `z`-independence of `A`, dense domains, or the use of a genuine resolvent family.

## Consequence for the research line

The exact fixed-edge resolvent branch is now narrower than the surviving formulation after `PL-206` suggested. Moving the spectral parameter does not rescue a nontrivial fixed bounded prime edge: it only yields scalar affine reparameterization, and the canonical `log p` case is ordinary translation.

Therefore a new exact-resolvent prime-lattice mechanism must put its nontrivial arithmetic content somewhere that this theorem does not quotient away: a genuinely spectral-parameter-dependent transfer operator, a source-forced non-fiberwise coupling, domain/kernel structure outside bounded fixed-left transport, a controlled approximate/ideal-valued law, or another global completion that produces a target-specific sign, coercivity, trace, or localization statement. Merely replacing `z` by a prime-dependent `phi_p(z)` while keeping one fixed edge is no longer a live escape.