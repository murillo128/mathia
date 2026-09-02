# PL-119 — Meyer’s adelic difference representation already realizes every zeta zero spectrally; positivity/unitarity is the RH content

## Claim

Ralf Meyer’s global adelic spectral construction gives a stronger prior-art control than merely realizing the Riemann zeros as eigenvalues of some non-self-adjoint operator. For a global field `K`, Meyer constructs a summable virtual representation

\[
\pi=\pi_+\ominus\pi_-
\]

of the idèle class group `C_K` whose spectrum consists exactly of the poles and zeros of the completed `L`-function, with spectral multiplicity equal to the analytic order, and whose character is the raw Weil explicit-formula distribution. For `K=Q`, the nontrivial zeros of `zeta` are therefore present in an exact global spectral/trace formula built from adelic harmonic analysis rather than from a formal continuation of an Euler product.

The decisive negative for the prime-lattice program is that this construction is deliberately **not biased toward the critical line**: hypothetical off-line zeros enter the global spectrum in exactly the same way as critical-line zeros. Meyer states that the corresponding modified Weil distribution is positive definite if and only if the zero spectrum lies on the critical line, hence if and only if GRH (RH for `Q`) holds. He can put variants of the representation on Banach or Hilbert spaces, but cannot make the representation unitary when off-critical zeros or the relevant non-semisimple multiplicity phenomena are present.

Thus the chain

\[
\text{exact prime-place data}
\to
\text{global adelic/Fourier completion}
\to
\text{analytic continuation + explicit formula}
\to
\text{all zeros as spectrum}
\]

already exists unconditionally. What it does **not** supply is the positive/unitary polarization that would force that spectrum onto the self-dual axis. This materially sharpens `PL-118`: the missing Hodge/positivity arrow is not just an aesthetic desideratum of the Deninger program; a separate exact global spectral realization shows that spectrality plus the full explicit formula can coexist with arbitrary hypothetical off-line zeros.

**Evidence/status:** `LITERATURE + EXACT-READING + PRIOR-ART-REDIRECT + DECISIVE-NEGATIVE` against the claim that global spectral realization, an exact trace formula, or adelic completion alone can force RH. No novelty is claimed for Meyer’s construction or for Weil positivity; the durable contribution here is the obstruction diagnosis relative to the prime-exponent line.

## The global difference representation is genuinely adelic

Let

\[
\mathbb A_K,
\qquad
C_K=\mathbb A_K^\times/K^\times
\]

be the adele ring and idèle class group. Meyer works with the Bruhat–Schwartz space `S(A_K)` and forms the coinvariant representation

\[
\mathcal H_+=\mathcal S(\mathbb A_K)/K^\times.
\]

A second ingredient is a weighted Schwartz representation `H_-` of `C_K`. The summation map over `K^\times`, the adelic Fourier transform, and Poisson summation embed the two representations into a common ambient space which intentionally omits the critical strip; after removing their common subrepresentation one obtains the global difference representation `pi`.

This matters for the research mandate. The construction is not the classical Bohr transform in new notation, and it does not continue an Euler product term-by-term into `0<Re(s)<1`. The analytic continuation and functional-equation structure are supplied by the global additive Fourier/Poisson geometry of the adeles. In particular, this is exactly the kind of additional global structure that `PL-014` showed is absent from the bare prime torus.

Meyer emphasizes the contrast with Connes’s Hilbert-space spectral interpretation: his global function spaces are chosen smaller and are **no longer biased in favor of the critical line**, so all poles and zeros occur uniformly in the representation. That choice is precisely what makes the present construction a useful falsification control: exact global arithmetic spectrality does not itself imply axis localization.

## Exact spectrum and exact Weil character

Meyer proves that the positive part has the two completed-`L` poles as spectrum and that the negative part has exactly the zero set. In his notation the virtual spectral multiplicity satisfies

\[
\operatorname{mult}(\omega,\pi)
=
\operatorname{ord}(\omega,L_K),
\]

where the order is positive for poles and negative for zeros in the virtual character convention. Equivalently, when `pi_-` is considered separately, each zero occurs with its positive zero multiplicity.

The representation is summable and its character can be computed spectrally:

\[
\chi_\pi(f)
=
\sum_{\omega}
\operatorname{ord}(\omega,L_K)\,\widehat f(\omega).
\]

Meyer’s Theorem 5.8 identifies this character with the raw Weil distribution, while Theorem 5.11 identifies the spectrum with the poles and zeros with the stated multiplicities. This is an actual trace/character theorem, not a determinant defined after inserting the zero set by hand.

For the specialized Riemann-zeta model Meyer makes the operator statement even more concrete. He constructs a nuclear Fréchet space `H_-^0` and the generator `D_-` of a smooth representation of `R_+^×` such that

\[
\operatorname{spec}(D_-)
=
\{\rho:\xi(\rho)=0\},
\]

with algebraic multiplicity equal to the zero order. Its virtual character has both a spectral expression and the geometric expression

\[
W=\sum_p W_p+W_\infty,
\]

where

\[
W_p(f)
=
\sum_{e\ge1} f(p^{-e})p^{-e}\log p
+
\sum_{e\ge1} f(p^e)\log p.
\]

Equating the two is the Riemann–Weil explicit formula.

## Prime-exponent interpretation: the local terms are exactly prime-power axes

The idèle class group must **not** be identified with the free exponent lattice: quotienting by `K^×` introduces global relations, and the adelic construction contains local units, the archimedean place, Fourier transform, and Poisson summation. Nevertheless, the nonarchimedean geometric character has a precise exponent-lattice support.

For `K=Q`, the terms `p^e` and `p^{-e}` in `W_p` are the positive and negative repetitions of the prime direction. On the positive-integer lattice the corresponding arithmetic support is

\[
e e_p,
\qquad e\ge1,
\]

with orbit/energy increment

\[
\log(p^e)=e\log p.
\]

Thus the same prime-power axis skeleton already isolated in `PL-013` and the same `log p` weights demanded by the line enter a fully global trace formula. The important point is negative: **even after those local axis contributions are assembled with the archimedean term into the exact global Weil character, axis localization of the zeros is not automatic.**

This distinguishes the result from a generic Helson or Beurling twist control. Meyer uses the exact rational/global-field adele structure and Poisson summation; the failure of localization persists even after admitting precisely the rigid local-global completion that generic multiplicative models lack.

## Positivity is exactly where RH re-enters

Meyer distinguishes the raw Weil distribution, which is the natural character of `pi`, from the usual modified Weil distribution. His character formula implies that the modified Weil distribution is positive definite exactly when the spectrum of `pi_-` is contained in

\[
|x|^{1/2}\widehat{C_K},
\]

the critical unitary axis of quasi-characters. This is equivalent to GRH; for `K=Q` it is RH.

This gives an unusually clean separation:

\[
\text{adelic representation + spectral divisor + explicit formula}
\quad\text{is unconditional},
\]

whereas

\[
\text{positive-definite Weil form / unitary critical-axis realization}
\quad\Longleftrightarrow\quad
\text{RH/GRH}.
\]

Meyer explicitly says that he cannot prove this positivity. He also notes that the representation can be modified to live on a Banach space, even a Hilbert space, but that this does **not** solve the issue: the representation cannot in general be made unitary when off-critical zeros are present (and the spectral multiplicity structure creates an additional obstruction at multiple zeros). Therefore the missing property is not “put the construction in a Hilbert space”; it is a compatible positive/unitary structure whose spectral theorem constrains the divisor.

This is the same load-bearing distinction reached from another direction in `PL-118`. Deninger’s Hodge identity would give

\[
\Theta=\tfrac12 I+A,
\qquad A^*=-A,
\]

and hence force the critical axis. Meyer shows that a global arithmetic representation can already supply the zero spectrum and trace formula **without** supplying that positivity/skew-adjointness. The missing polarization is therefore mathematically substantive rather than merely a missing packaging step.

## Relation to `PL-033`, `PL-014`, `PL-044`, and `PL-118`

This finding does not duplicate `PL-033`. Automorphic Lax–Phillips scattering already proves that the nontrivial zeta zeros can be genuine eigenvalues of a non-self-adjoint generator, so `PL-033` killed “zeros as operator spectrum” as a sufficient novelty target. Meyer adds a different and stronger control: the **full adelic local-global character is the Weil explicit formula**, all zeros are represented unconditionally, and the exact missing condition is identified as positive definiteness/unitarity equivalent to RH.

It also sharpens but does not duplicate `PL-014`. Tate’s adelic Fourier transform explains the functional equation and singles out `Re(s)=1/2` as the self-dual axis, but supplies no zero-repelling mechanism. Meyer continues through to a global zero-spectrum representation and still finds that the zeros need not lie on that axis without positivity.

`PL-044` studies semilocal/finite Weil forms and the danger that finite spectral reality can be universal while the global limit carries the hard arithmetic content. Meyer gives the complementary infinite/global control: an exact global character and exact zero spectrum already exist, yet positivity remains equivalent to RH. Recent self-adjoint finite constructions such as Connes–Consani–Moscovici’s 2025 zeta spectral triples likewise leave rigorous convergence to the full `Xi` divisor as the RH-level missing step; they do not supply a known counterexample to the present diagnosis.

Finally, `PL-118` records Deninger’s prime-orbit/Hodge program. The two findings fit together as a strong prior-art funnel: prime orbit lengths and global spectral realization are both classical; what remains missing is an arithmetic positive polarization or an equivalent theorem that forces the centered generator to be skew-adjoint/unitary.

## Adversarial audit

### This is not a Hilbert–Pólya theorem

The word “spectrum” here is representation-theoretic. In the global idèle-class construction the spectrum is a set of quasi-characters of a summable representation on nuclear bornological spaces. In the specialized zeta model there is an actual generator `D_-` on a nuclear Fréchet space whose spectrum is the zero set. Neither construction gives a self-adjoint operator whose ordinary Hilbert-space spectral theorem would prove RH.

### “Hilbertizable” is not “unitary”

Meyer explicitly allows Banach/Hilbert realizations after modifying the representation. Therefore it would be false to claim that the zero representation cannot live on a Hilbert space. The obstruction relevant here is that the arithmetic representation is not supplied with a compatible **unitary** structure forcing spectral parameters to the critical axis.

### The positivity equivalence is not a proof mechanism

Saying that the modified Weil distribution is positive definite iff RH is a rigorous reduction, not an explanation of why positivity holds. This finding therefore records a no-go/prior-art boundary, not progress toward proving the missing inequality.

### The explicit formula is not being formally continued from `Re(s)>1`

The local prime-power formula resembles the logarithmic derivative of the Euler product, but Meyer’s global character theorem is obtained from adelic function spaces, summation, Fourier transform, and Poisson summation. Its validity is not justified by evaluating an Euler product inside the critical strip. This passes the line’s analytic-continuation gate.

### The construction is arithmetic enough for the negative control

A generic multiplicative frequency model could be dismissed under the line’s Helson/Beurling falsification controls. Meyer’s construction cannot: it is built from the actual adele ring and idèle class quotient of the global field and recovers the exact Weil local terms plus the archimedean contribution. Therefore its failure to force the critical line is a genuine warning against attributing too much power to “full local-global completion + trace formula” alone.

## Prior art and novelty audit

Primary sources:

- **Ralf Meyer**, “On a representation of the idele class group related to primes and zeros of L-functions,” *Duke Mathematical Journal* **127**(3) (2005), 519–595. DOI: `10.1215/S0012-7094-04-12734-4`. arXiv: `math/0311468`. The introduction explicitly contrasts the construction with Connes, states that the global spaces are no longer biased toward the critical line, states the positive-definite modified Weil distribution iff GRH criterion, and explains the non-unitarity issue. Theorems 5.8 and 5.11 give the character/Weil-distribution identity and the pole/zero spectral multiplicity theorem.
- **Ralf Meyer**, “A spectral interpretation for the zeros of the Riemann zeta function,” seminar article (2005), pp. 117–137, arXiv: `math/0412277` (revised version 2013). This specializes the construction to `Q`, producing a nuclear Fréchet generator `D_-` whose spectrum is exactly the nontrivial zeta zeros with algebraic multiplicity and writing the prime-place character terms `W_p` explicitly.
- **Alain Connes**, “Trace formula in noncommutative geometry and the zeros of the Riemann zeta function,” *Selecta Mathematica* **5** (1999), 29–106. DOI: `10.1007/s000290050042`. Prior construction with critical zeros as absorption spectrum and hypothetical off-line zeros as resonances; Meyer’s work is explicitly motivated by and contrasted with it.

Current-status control:

- **Alain Connes, Caterina Consani, Henri Moscovici**, “Zeta Spectral Triples,” arXiv:`2511.22755` (27 November 2025). Their finite self-adjoint operators numerically approach low zeta zeros, but the authors state that a rigorous proof of convergence to the `Xi` divisor would establish RH. This is consistent with, rather than a resolution of, the positivity/localization gap.

No novelty is claimed for any of these constructions or criteria. Repository audit found no stored finding centered on Meyer’s global idèle-class difference representation. `PL-033` is the closest zero-spectrum prior-art result, but lacks the exact adelic Weil-character/positivity separation recorded here.

## Falsification conditions

This finding would need withdrawal or material narrowing if any of the following were false:

1. Meyer’s global difference representation did not have the completed `L` poles and zeros as its spectrum with analytic multiplicities;
2. its summable character did not equal the raw Weil explicit-formula distribution;
3. the modified Weil distribution were not positive definite exactly when the zero spectrum lies on the critical unitary axis;
4. the global construction actually supplied unconditional unitarity/self-adjointness forcing that axis;
5. the specialized Riemann model did not have a generator whose spectrum is exactly the nontrivial zeta zero set with algebraic multiplicity;
6. the prime-place character terms were not the explicit `p^{±e}`/`log p` contributions stated above;
7. another stored `prime_lattice` finding already contained this exact global adelic spectrum-plus-character-plus-positivity obstruction, making `PL-119` duplicate rather than complementary evidence.

The primary sources explicitly establish items 1–3 and 5–6. Item 4 is explicitly denied as an available theorem: the inability to prove the positivity/unitarity constraint is the RH-level gap. Item 7 was checked against the current finding inventory and the nearest anchors `PL-014`, `PL-033`, `PL-044`, and `PL-118`.

## Consequence for the research line

The search space should now treat the following as established prior art rather than missing targets:

\[
\text{prime-power axis terms with }\log p
+\text{archimedean completion}
+\text{global adelic Fourier/Poisson geometry}
+\text{exact explicit-formula trace}
+\text{all zeta zeros as spectrum}.
\]

A new exponent-lattice spectral proposal is therefore not materially strengthened merely by adding an adelic completion, a trace formula, or an exact spectral realization of the divisor. To survive the current audit it must supply a property that Meyer’s representation lacks and that is not equivalent to inserting RH as an assumption: a canonical positive pairing, unitary/polarized cohomology, skew-adjoint centered generator, or another arithmetic rigidity theorem that **forces** the already-representable zero spectrum onto `Re(s)=1/2`.

That makes the frontier after `PL-118` unusually precise: the unsolved arrow is not

\[
\text{arithmetic} \to \text{spectrum},
\]

but

\[
\text{arithmetic} \to \text{positive/unitary polarization} \to \text{critical-axis localization}.
\]
