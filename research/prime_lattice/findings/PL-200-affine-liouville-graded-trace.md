# PL-200 — Canonical Liouville grading of the affine prime semigroup collapses to a trace-class Helson twist

## Claim

`PL-199` left open the possibility that a Möbius/parity observable could add genuinely zero-sensitive structure to the classical affine semigroup `N ⋊ N^×`. The most canonical full-lattice parity does extend across the affine multiplication law, but its standard thermal realization still does not produce an operator mechanism in the critical strip.

Let

\[
P=\mathbb N\rtimes\mathbb N^\times,
\qquad
(a,m)(b,n)=(a+mb,mn),
\]

and let

\[
\lambda(m)=(-1)^{\Omega(m)}.
\]

Because `lambda` is completely multiplicative,

\[
\chi_\lambda(a,m)=\lambda(m)
\]

is a semigroup character `P -> {+1,-1}`. The additive generator has even parity and every prime dilation has odd parity. Thus the exponent-lattice orientation `(-1)^{sum_p v_p(m)}` is compatible with the genuinely noncommutative affine relation; it is not destroyed by adding ordinary integer translation.

In the standard extremal low-temperature representation audited in `PL-199`, the implementing Hamiltonian `H` has eigenvalue `log x` with multiplicity `x`. If `P_x` denotes that spectral projection, define the canonical multiplicative-parity unitary

\[
\Gamma_\lambda=\sum_{x\ge1}\lambda(x)P_x.
\]

Then `Gamma_lambda^2=I` and `[Gamma_lambda,H]=0`. Since `Gamma_lambda` is unitary,

\[
\|\Gamma_\lambda e^{-\beta H}\|_1
=
\|e^{-\beta H}\|_1.
\]

Consequently the ordinary graded trace exists **exactly in the same trace-class half-plane as the ungraded Gibbs trace**, namely `Re(beta)>2`. There,

\[
\operatorname{Tr}(\Gamma_\lambda e^{-\beta H})
 =\sum_{x\ge1}x\lambda(x)x^{-\beta}
 =\sum_{x\ge1}\frac{\lambda(x)}{x^{\beta-1}}
 =\frac{\zeta(2\beta-2)}{\zeta(\beta-1)}.
\]

The last equality is an absolutely convergent Euler-product identity in `Re(beta)>2`; no continuation is being used in deriving the operator trace.

The shifted Riemann critical line is `Re(beta)=3/2`, a full half-plane to the left of this trace-class boundary. Continuing the scalar quotient meromorphically does make it RH-sensitive: a zero `rho` of `zeta` with `Re(rho)>1/2` produces an uncancelled pole at `beta=1+rho`, because `Re(2rho)>1` implies `zeta(2rho) != 0`. But at such `beta` the displayed quantity is **not** the ordinary trace of `Gamma_lambda e^{-beta H}`. The zero information has entered only through the independently known meromorphic continuation of the scalar Liouville Dirichlet series.

Therefore the route

\[
\text{affine prime semigroup}
+\text{canonical exponent parity}
\longrightarrow
\text{ordinary graded Gibbs trace}
\longrightarrow
\text{RH zero localization}
\]

fails at exactly the same analytic-continuation boundary as the ungraded thermodynamic route. The parity observable changes `zeta(beta-1)` into the classical Liouville quotient `zeta(2beta-2)/zeta(beta-1)`, but it does not make the continued divisor an operator trace, a positive KMS invariant, or a new spectral law in the critical strip.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION` for the **canonical energy-diagonal Liouville/parity repair of the standard affine-semigroup thermal representation**.

This does not rule out target-relative parity observables, square-free Möbius projections, relative/renormalized traces with an independently justified continuation theorem, or additive correlations that are not functions only of the multiplicative energy label.

## 1. The affine semigroup really does retain exponent parity

The negative is not that addition makes the prime-exponent parity inconsistent. In fact the opposite is true.

For any completely multiplicative unimodular character `chi` on the positive integers,

\[
\widetilde\chi(a,m)=\chi(m)
\]

satisfies

\[
\widetilde\chi((a,m)(b,n))
 =\chi(mn)
 =\chi(m)\chi(n)
 =\widetilde\chi(a,m)\widetilde\chi(b,n).
\]

Thus every prime-phase character lifts through the affine semigroup by ignoring the additive coordinate. The Liouville choice is the distinguished `Z/2` case

\[
\chi(p)=-1\qquad\text{for every prime }p,
\]

so

\[
\chi(n)=(-1)^{\sum_p v_p(n)}=\lambda(n).
\]

On the square-free hypercube this agrees with the nonzero Möbius orientation. On the full exponent lattice, `lambda` — not literal `mu`, which vanishes on squareful integers — is the completely multiplicative extension that makes every prime coordinate odd.

This matters for the audit because `PL-199` introduced a truly relational noncommutative source action. The simplest parity escape cannot be rejected by saying that the affine relation `V_n S=S^n V_n` destroys multiplicative parity: the semigroup law is homogeneous for exactly this character.

At the same time, the construction immediately exposes a Helson-type flexibility. Replacing the uniform choice `chi(p)=-1` by arbitrary prime phases gives another semigroup character. Hence the raw affine relation by itself does not select the Liouville phase from the full multiplicative character family. Any claimed rigidity must come from a further distinguished observable, target, completion, or positivity principle.

## 2. The canonical graded trace has no improved operator domain

Use the spectral data of the standard affine-semigroup Hamiltonian already established and sourced in `PL-199`:

\[
H\big|_{E_x}=(\log x)I,
\qquad
\dim E_x=x.
\]

For a unimodular completely multiplicative `chi`, define

\[
\Gamma_\chi\big|_{E_x}=\chi(x)I.
\]

This is a unitary commuting with `H`. Therefore left multiplication by `Gamma_chi` does not change singular values:

\[
s_j(\Gamma_\chi e^{-\beta H})
=s_j(e^{-\beta H}).
\]

The trace norm is consequently

\[
\|\Gamma_\chi e^{-\beta H}\|_1
 =\sum_{x\ge1}x^{1-\operatorname{Re}\beta},
\]

which is finite exactly for `Re(beta)>2`.

Whenever this condition holds, the trace can be evaluated block by block:

\[
\operatorname{Tr}(\Gamma_\chi e^{-\beta H})
 =\sum_{x\ge1}\chi(x)x^{1-\beta}.
\]

Writing `s=beta-1`, this is simply the completely multiplicative Dirichlet series

\[
F_\chi(s)=\sum_{x\ge1}\frac{\chi(x)}{x^s},
\qquad \operatorname{Re}s>1.
\]

For general prime phases this is precisely the scalar Euler/Helson-twist object whose flexibility is already a falsification control in `PL-003` and `PL-073`. The affine multiplicity shifts the variable by one but does not create a new continuation mechanism.

For the Liouville character,

\[
F_\lambda(s)
 =\prod_p(1+p^{-s})^{-1}
 =\prod_p\frac{1-p^{-s}}{1-p^{-2s}}
 =\frac{\zeta(2s)}{\zeta(s)},
\]

hence

\[
\operatorname{Tr}(\Gamma_\lambda e^{-\beta H})
 =\frac{\zeta(2\beta-2)}{\zeta(\beta-1)}
\]

for `Re(beta)>2`.

This is a genuine operator identity in that half-plane, not a merely formal partition-function analogy. The obstruction is equally genuine: because `Gamma_lambda` is unitary, grading cannot improve trace class by cancellation. Any value assigned below `Re(beta)=2` must use a different notion of trace or an external continuation/regularization.

## 3. RH sensitivity appears only after the scalar continuation step

Set again `s=beta-1`. The meromorphic continuation

\[
F_\lambda(s)=\frac{\zeta(2s)}{\zeta(s)}
\]

is a classical RH-sensitive scalar function. In the open half-plane `Re(s)>1/2`, the numerator has no zeros: if `Re(s)>1/2`, then `Re(2s)>1`, where the Euler product for `zeta(2s)` is nonzero. Therefore every zero `rho` of `zeta` with `Re(rho)>1/2` gives a genuine pole of `F_lambda` at `s=rho`.

Equivalently, apart from the ordinary pole/zero bookkeeping on the boundary,

\[
\text{RH}
\quad\Longleftrightarrow\quad
F_\lambda(s)\text{ has no nontrivial poles in }\operatorname{Re}s>\tfrac12.
\]

Translated back to the affine thermal variable, this is the half-plane

\[
\operatorname{Re}\beta>\tfrac32.
\]

But the operator supertrace is available only in `Re(beta)>2`. Thus the RH-sensitive annulus of analytic continuation

\[
\tfrac32<\operatorname{Re}\beta\le2
\]

contains **no ordinary graded trace supplied by the standard Hamiltonian representation**.

This is the same logical distinction emphasized repeatedly in this line for determinants, spectral zeta functions, and KMS partition functions: a meromorphically continued scalar attached to an operator is not automatically an operator trace or spectrum at the continued parameter.

The standard Laca–Raeburn KMS phase diagram from `PL-199` also supplies no parity-localization event at `beta=3/2`: the real point `3/2` remains inside the unique-KMS interval `[1,2]`. Moreover a graded trace is signed rather than a positive state, so its scalar poles cannot be promoted to a KMS positivity boundary merely by nomenclature.

## 4. Matched controls: the grading is compatible but not selective

This finding sharpens rather than duplicates `PL-073`.

`PL-073` showed that Liouville/Möbius orientation is a prime-torus gauge for **unpointed Haar or Gram-spectral statistics**. The present observable is not Haar-unpointed: it keeps the energy decomposition fixed and inserts a distinguished phase in a thermal trace, so it really can see `lambda` and yields `zeta(2s)/zeta(s)` rather than erasing the signs.

However, once the signs are visible, the result is still only a scalar completely multiplicative Dirichlet series. The general character calculation gives the matched control

\[
\Gamma_\chi
\quad\leadsto\quad
F_\chi(s)=\sum_n\chi(n)n^{-s}.
\]

The affine semigroup accommodates the whole prime-character family, while `PL-003` records that Helson-type prime twists can have very different zero and continuation behavior. Therefore the existence of the grading plus a character-weighted trace is not a rational-prime zero-localization principle. The special continuation of the all-minus Liouville character is additional classical arithmetic input.

The free arithmetic-gas interpretation is likewise prior art. `PL-004`, anchored by Julia in `SOURCES.md` source 4, already prevents treating prime occupation parity, fermionic/supertrace language, or `log p` thermodynamics as a discovery. The new line-specific point here is narrower: even after the category exit of `PL-199` to the noncommutative affine semigroup, the **canonical full-lattice parity insertion still returns to a scalar character Dirichlet series and does not cross the operator trace boundary**.

A targeted novelty audit around arithmetic gases, Möbius/supersymmetry, graded Riemann-gas partition functions, affine-semigroup KMS systems, and multiplicative-character twists recovered classical Riemann-gas/supersymmetry constructions and the existing Helson/affine frameworks rather than a theorem in which this standard affine Liouville supertrace itself forces RH. No novelty is claimed for the Liouville Dirichlet identity, arithmetic supersymmetry language, semigroup characters, or the Laca–Raeburn Hamiltonian spectrum.

## 5. Boundary conditions and surviving routes

The negative is intentionally narrow.

First, literal Möbius weighting is not the same observable on the full lattice. `mu(n)` has zeros on squareful states, so inserting `mu` changes support as well as parity. A square-free projection followed by orientation can therefore contain information absent from the unitary Liouville grading.

Second, a **relative or renormalized** supertrace could in principle survive below the ordinary trace-class boundary. Such a construction would need an independently justified trace formula, subtraction, determinant, scattering theory, or boundary-value theorem. Simply declaring the meromorphic continuation of `zeta(2s)/zeta(s)` to be the graded trace is exactly the continuation import ruled out by the line mandate.

Third, a target-relative observable can couple parity to addition in a way that is not a function only of the energy label `x`. Correlations involving the successor, Nyman targets, Weil test functions, or another fixed arithmetic section are not covered by the block-diagonal calculation.

Fourth, twisted KMS functionals or nonpositive graded functionals are not classified here. The conclusion is only that the ordinary trace-class Gibbs/supertrace mechanism supplied by the standard affine representation does not reach the RH-sensitive region. A different functional must establish its own existence and continuation rather than inheriting the scalar quotient by definition.

Finally, the result does not say that the affine semigroup is uninformative. Its additive/multiplicative relation remains genuinely rational-integer-specific. What fails is the simplest attempt to make that relation RH-sensitive by appending the canonical exponent-parity sign to the already-known logarithmic thermal spectrum.

## 6. Decisive audit tests

The finding should be withdrawn or narrowed if any of the following occurs:

1. the function `(a,m) -> lambda(m)` fails to be multiplicative for the affine law `(a,m)(b,n)=(a+mb,mn)`;
2. the standard spectral multiplicity `dim E_x=x` used in `PL-199` is incorrect for the cited low-temperature representation;
3. `Gamma_lambda e^{-beta H}` is an ordinary trace-class operator for some `Re(beta)<=2`, despite having the same singular values as `e^{-beta H}`;
4. the trace identity `sum lambda(x)x^{1-beta}=zeta(2beta-2)/zeta(beta-1)` fails in its absolute-convergence region;
5. an established operator/KMS theorem extends this **same** graded trace canonically into `Re(beta)>3/2` and ties its positivity or spectrum to the location of zeta zeros without simply importing the meromorphic continuation of the scalar quotient.

Items 1, 3, and 4 are exact calculations; item 2 is inherited from the literature-audited `PL-199`; item 5 is the substantive novelty boundary.

## Consequence for the research line

The explicit “Möbius/parity observable” loophole left by `PL-199` is now narrower. The canonical full-exponent parity is perfectly compatible with the affine semigroup, but when inserted in the standard logarithmic thermal representation it yields only

\[
\frac{\zeta(2\beta-2)}{\zeta(\beta-1)}
\]

in the same trace-class region `Re(beta)>2`. Its RH-sensitive poles occur only after scalar meromorphic continuation into a region where the ordinary operator supertrace no longer exists.

A surviving parity-based affine mechanism therefore has to be **more than an energy-diagonal character insertion**. It must make parity interact with the additive/target-relative structure in a way that both survives the Helson character control and carries a mathematically justified operator, trace, positivity, or boundary object across the critical-strip continuation barrier.