# WP-039 — Translation-invariant Markov energies cannot carry Mangoldt support as their Fourier symbol

**Status:** `EXACT-DERIVED + CLASSICAL-HARMONIC-ANALYSIS + DECISIVE-NEGATIVE` for the nonlocal transverse-Dirichlet escape left open by `WP-038`. A conservative translation-invariant symmetric Dirichlet form on a compact abelian group has a nonnegative Fourier symbol whose zero set is necessarily a subgroup of the discrete dual. The Mangoldt support has the opposite behavior: it is positive on prime-power directions but vanishes on mixed-prime directions, and those mixed directions algebraically generate the prime directions. Therefore neither the arithmetic solenoid of `PC-064` nor the Prime-Lattice/Bohr prime torus can realize the finite Weil weights directly as the spectral energy of a scalar translation-invariant Markov generator, even if the generator is nonlocal and couples primes non-additively.

This is strictly broader than the place-additive obstruction `WP-031`: no place-by-place decomposition of the symbol is assumed. The price is a different structural hypothesis, namely translation invariance plus the Markov/Dirichlet property. The result does **not** rule out non-translation-invariant energies, matrix-valued/internal-state generators, compressions or quotients, nonlinear rank/volume readouts such as `WP-030`, or a genuinely nonseparable finite--archimedean construction whose total positive form never isolates the Mangoldt support as a positive Fourier symbol.

## 1. The escape being tested

`WP-038` derived the most canonical ordinary positive form on the arithmetic solenoid

\[
\Sigma_{\mathbb Q}\cong \mathbb A_{\mathbb Q}/\mathbb Q,
\qquad
\widehat{\Sigma_{\mathbb Q}}\cong\mathbb Q,
\]

and found its compatible leafwise Dirichlet symbol to be

\[
\psi_0(q)=4\pi^2q^2.
\]

That form is positive but place-additive after taking logarithms, has arbitrarily soft rational modes, and does not select prime powers. `WP-038` therefore left open an obvious stronger possibility: perhaps the Prime-Circle profinite/radial structure forces a **nonlocal transverse Dirichlet form** on the same compact group whose Fourier symbol already knows the Mangoldt support.

The strongest direct version would assign to denominator characters

\[
\chi_{1/n},\qquad n\ge2,
\]

a nonnegative energy of the form

\[
\boxed{
\psi(1/n)=a_n,
\qquad
a_{p^k}>0,
\qquad
a_n=0\ \text{when }n\text{ has at least two distinct prime factors}.
}
\tag{1}
\]

The exact positive values are irrelevant to the obstruction. They may be

\[
a_{p^k}=\frac{\log p}{p^{k/2}},
\]

or any positive rescaling/attenuation of the finite Weil coefficient. What matters is the exact prime-power support.

A parallel version on the Prime-Lattice Bohr/prime torus would ask for a translation-invariant Markov energy on a compact abelian group with dual exponent lattice

\[
\Gamma_{\mathcal P}=\bigoplus_p\mathbb Z e_p
\]

whose symbol is positive on the one-prime axes and zero on exponent vectors involving two or more distinct primes.

Both direct constructions are impossible for the same reason.

## 2. Translation-invariant conservative Dirichlet forms diagonalize on characters

Let `K` be a compact abelian group with normalized Haar measure and discrete dual `Gamma`. Let

\[
\mathcal E
\]

be a densely defined closed symmetric **conservative Dirichlet form** on `L^2(K)` which is invariant under translations of `K`. Let `T_t=e^{-tL}` be its self-adjoint Markov semigroup.

Because `T_t` commutes with every translation and every character space is one-dimensional, each character is an eigenvector:

\[
T_t\chi_\gamma=a_t(\gamma)\chi_\gamma.
\tag{2}
\]

Translation invariance and the Markov property imply that `T_t` is convolution by a probability measure `mu_t` on `K`. Equivalently,

\[
a_t(\gamma)=\widehat\mu_t(\gamma).
\tag{3}
\]

Self-adjointness and strong continuity give a real nonnegative generator symbol `psi` with

\[
\boxed{
T_t\chi_\gamma=e^{-t\psi(\gamma)}\chi_\gamma,
\qquad
\mathcal E(\chi_\gamma)=\psi(\gamma),
\qquad
\psi(0)=0.
}
\tag{4}
\]

In the standard harmonic-analysis language, `psi` is a conditionally negative-definite function on `Gamma`, and conversely such symbols generate translation-invariant Markov/Dirichlet semigroups under the usual hypotheses. The subgroup argument below does not need the full Levy--Khintchine representation; it follows directly from (3)--(4).

## 3. Exact kernel theorem: the zero set of the symbol is a subgroup

Define

\[
H_\psi:=\{\gamma\in\Gamma:\psi(\gamma)=0\}.
\tag{5}
\]

If `gamma in H_psi`, then by (3)--(4)

\[
\widehat\mu_t(\gamma)
=\int_K\overline{\chi_\gamma(x)}\,d\mu_t(x)
=1
\qquad(t>0).
\tag{6}
\]

But `|chi_gamma|=1`. Equality in the triangle inequality for the probability integral in (6) forces

\[
\chi_\gamma(x)=1
\quad\text{for }\mu_t\text{-almost every }x.
\tag{7}
\]

Hence if `gamma,delta in H_psi`, then both characters equal one on a common full-`mu_t` set, so

\[
\chi_{\gamma+\delta}
=\chi_\gamma\chi_\delta=1,
\qquad
\chi_{-\gamma}=\overline{\chi_\gamma}=1
\quad\mu_t\text{-a.e.}
\tag{8}
\]

Therefore

\[
\widehat\mu_t(\gamma+\delta)
=\widehat\mu_t(-\gamma)=1
\]

for every `t>0`, and (4) gives

\[
\gamma+\delta,-\gamma\in H_\psi.
\]

Thus

\[
\boxed{H_\psi\le\Gamma\text{ is a subgroup}.}
\tag{9}
\]

This elementary subgroup property is also immediate from the Schoenberg/Hilbert-cocycle realization of a conditionally negative-definite symbol: `sqrt(psi(gamma-delta))` is a translation-invariant Hilbert pseudometric, so the zero class of the identity is a subgroup.

A useful corollary is the **integer-multiple heredity**

\[
\boxed{
\psi(\gamma)=0
\Longrightarrow
\psi(m\gamma)=0
\quad\text{for every }m\in\mathbb Z.
}
\tag{10}
\]

This is exactly what the Mangoldt support violates in the arithmetic-solenoid parametrization.

## 4. One mixed denominator kills a prime denominator on the arithmetic solenoid

Take `K=Sigma_Q`, so `Gamma=Q` additively. Assume a direct Mangoldt-support symbol (1). Choose distinct primes `p` and `q`.

Because `pq` is not a prime power,

\[
\psi\!\left(\frac1{pq}\right)=0.
\tag{11}
\]

But `H_psi` is a subgroup. Multiplying the zero-frequency element in (11) by the integer `q` gives

\[
\frac q{pq}=\frac1p\in H_\psi.
\tag{12}
\]

Therefore

\[
\boxed{
\psi(1/p)=0,
}
\tag{13}
\]

contradicting the required positive prime value `a_p>0`.

So already the two denominator characters

\[
\chi_{1/(pq)},\qquad\chi_{1/p}
\]

produce a complete finite certificate. No asymptotic, analytic continuation, zeta identity, zero data, or regularization enters.

The obstruction is stronger than a mismatch of coefficients. **Any** exact support rule which assigns zero energy to a fine denominator `1/(pq)` while assigning positive energy to the coarser divisor denominator `1/p` is incompatible with a scalar translation-invariant Markov generator on `Sigma_Q`.

In covering language: a zero mode at a finer arithmetic level propagates through integer powers to zero modes at the divisor levels. Mangoldt support requires the opposite selective behavior.

## 5. The same obstruction holds on the Prime-Lattice exponent torus

The conclusion is not an artifact of representing arithmetic by reciprocal rational frequencies. Let

\[
\Gamma_{\mathcal P}=\bigoplus_p\mathbb Z e_p
\]

and write

\[
\alpha(n)=\sum_p v_p(n)e_p.
\]

Suppose a translation-invariant Markov symbol `psi` satisfies

\[
\psi(\alpha(p^k))>0
\]

on one-prime axes and vanishes whenever at least two distinct prime coordinates are nonzero.

For distinct primes `p,q`, both

\[
e_p+e_q=\alpha(pq)
\]

and

\[
e_p+2e_q=\alpha(pq^2)
\]

must lie in `H_psi`. Since `H_psi` is a subgroup,

\[
(e_p+2e_q)-(e_p+e_q)=e_q\in H_\psi,
\]

and then

\[
(e_p+e_q)-e_q=e_p\in H_\psi.
\tag{14}
\]

Hence

\[
\boxed{
\psi(e_p)=\psi(e_q)=0,
}
\tag{15}
\]

again contradicting the prime-power requirement.

Thus even a highly nonlocal, non-place-additive conditionally negative-definite symbol cannot directly select the Prime-Lattice axes. The problem is the subgroup geometry of the nullspace, not separability across primes.

## 6. Relation to WP-030 and WP-031

This sharpens the architecture boundary around the positive Mangoldt selector.

`WP-030` succeeds locally because it uses the support-dependent **top Gram volume**

\[
\sqrt{\det G_{v(n)}}=\Lambda(n).
\]

Its zero mechanism is rank deficiency. Rank-deficient supports do not need to form a subgroup or linear radical, so mixed-prime inputs can vanish while singleton inputs remain positive.

`WP-031` then proves that this selector cannot be replaced by a fixed place-additive Hilbert feature followed by a positive quadratic readout: the zero set of a PSD quadratic form is a linear radical.

The present result removes the place-additivity assumption. A translation-invariant nonlocal Markov energy can mix all prime coordinates through an arbitrary conditionally negative-definite symbol, but its zero set still has rigid algebraic closure:

\[
\boxed{
\text{PSD place-additive readout: zero set is a linear radical,}
}
\]

\[
\boxed{
\text{translation-invariant Markov symbol: zero set is a subgroup.}
}
\]

Mangoldt support violates both closures. The nonlinear rank/volume mechanism of `WP-030` is therefore not merely compensating for a poor choice of additive metric; it also lies genuinely outside scalar translation-invariant Dirichlet-symbol geometry.

## 7. Why adding an archimedean symbol does not turn this into a local-to-global proof

A possible objection is that the research target is the **global** Weil form, not a positive finite-place symbol in isolation. Perhaps one could choose a total conditionally negative-definite symbol

\[
\psi_{\rm tot}=\psi_{\rm fin}+\psi_\infty
\tag{16}
\]

whose total values never vanish on mixed-prime frequencies, thereby avoiding (9), while `psi_fin` is recovered afterward as the Mangoldt term.

This is not excluded as an abstract algebraic decomposition, but it does not preserve the desired sign mechanism. If `psi_fin` has Mangoldt support, Sections 4--5 prove that `psi_fin` itself cannot be a translation-invariant Markov symbol. Therefore the positive theorem for `psi_tot` cannot be localized termwise to the finite Weil contribution. Extracting

\[
\psi_{\rm fin}=\psi_{\rm tot}-\psi_\infty
\]

uses a **difference** of positive/negative-definite structures, and conditional negative definiteness is not preserved under arbitrary subtraction.

So the direct local-to-global chain

```text
positive finite Markov symbol carrying Mangoldt
    + positive archimedean Markov symbol
    -> one global positive Dirichlet form
```

is impossible.

A surviving global construction would have to couple finite and archimedean data *before* the Markov/positivity theorem in a way for which the finite Mangoldt term appears only after a signed, compressed, boundary, cohomological, or otherwise nonlocal readout. That is qualitatively closer to the global mechanisms in Weil/Connes-type prior art and is no longer a positive local Dirichlet explanation of the finite coefficients.

## 8. Sub-Markov killing does not rescue exact support

The conservative assumption is natural for an intrinsic energy on a compact group, but the exact-support hypothesis essentially forces it anyway.

A translation-invariant sub-Markov semigroup is convolution by subprobability measures. If the total mass is strictly smaller than one at time `t`, then for every character

\[
|\widehat\mu_t(\gamma)|
\le \mu_t(K)<1.
\]

Hence no nontrivial character can have generator energy exactly zero. But the Mangoldt support requires infinitely many exact zeros, for example at every `1/(pq)`.

Therefore any sub-Markov realization satisfying the desired zero pattern must have unit mass, reducing to the conservative case above. Uniform killing cannot evade the subgroup certificate while retaining exact Mangoldt support.

## 9. Matched controls and novelty audit

The ambient harmonic-analysis theorem is classical, not a Mathia discovery.

- Schoenberg theory identifies conditionally negative-definite functions with the exponents of positive-definite semigroups and with squared Hilbert-cocycle lengths.
- Ola Bratteli, Palle E. T. Jorgensen, Akitaka Kishimoto, and Donald W. Robinson, *A C*-algebraic Schoenberg theorem*, Annales de l'Institut Fourier 34 (1984), no. 3, 155--187, DOI `10.5802/aif.981`, classifies invariant dissipations for compact abelian group actions in negative-definite terms.
- Emil Popescu, *Non-local Dirichlet forms generated by pseudodifferential operators on compact abelian groups*, Proceedings in Applied Mathematics and Mechanics 7 (2007), 2160001--2160002, DOI `10.1002/pamm.200700692`, explicitly uses negative-definite Fourier symbols to construct nonlocal Dirichlet forms on compact abelian groups.
- The `WP-009` literature anchors on Levy/Feller and jump-type Dirichlet forms provide the same prior-art warning from the stochastic side: Markov positivity severely constrains the admissible symbol or jump measure.

The literature audit found no basis for treating the subgroup theorem itself as new, and no historical novelty is claimed for it. The durable Mathia-specific consequence is the two-line arithmetic certificate (11)--(13), together with its exponent-lattice analogue (14)--(15), closing the direct nonlocal translation-invariant Dirichlet escape left open by `WP-038`.

The obstruction is deliberately **not RH-specific**. It survives arbitrary relabeling of the prime generators and any positive choice of prime-power amplitudes. That is exactly why it is useful here: it identifies a universal geometric architecture which is too rigid even to reproduce the finite support pattern required before RH-sensitive global positivity could begin.

## 10. Boundaries and escape routes

`WP-039` rules out only the direct scalar translation-invariant Markov-symbol architecture. It does **not** rule out:

- a positive translation-invariant quadratic Fourier multiplier which is not Markov/Dirichlet; without the Markov property an arbitrary nonnegative symbol can be prescribed, though its positivity then lacks the diffusion/energy theorem tested here;
- a non-translation-invariant solenoidal energy whose geometry distinguishes arithmetic strata or basepoints;
- a matrix-valued or graded generator with internal fibers, where the arithmetic readout is not the scalar character energy;
- a compression, quotient, Schur complement, boundary response, or cohomological pairing applied before reducing to a scalar symbol;
- the nonlinear rank/volume selector of `WP-030`;
- a total finite--archimedean positive object whose scalar Fourier symbol does not itself have Mangoldt support and whose explicit-formula terms emerge only after a separately justified global operation;
- or multiplicative correspondences/fixed-point structures on the solenoid rather than additive translation-invariant diffusion.

These are genuine escapes. In particular, the result must not be paraphrased as saying that nonlocal operators on `Sigma_Q` are useless. It says something narrower and exact: **if the positivity theorem is the scalar translation-invariant Markov/Dirichlet theorem, then the Fourier nullspace is a subgroup, and the Mangoldt selector cannot be its spectral energy.**

## 11. Exact falsification tests and research consequence

The core claim can be audited finitely and without numerical computation:

1. verify that a translation-invariant conservative Markov semigroup on a compact abelian group acts on each character by a scalar Fourier coefficient of a probability convolution measure;
2. verify that zero generator energy implies that coefficient is exactly one for every positive time;
3. use equality in the triangle inequality to show the corresponding character is one almost surely under every transition measure;
4. multiply/invert such characters to prove that the zero-energy set is a subgroup;
5. on `Sigma_Q`, combine `psi(1/(pq))=0` with integer multiplication by `q` to force `psi(1/p)=0`;
6. on the prime exponent group, subtract the two mixed-support zeros `e_p+2e_q` and `e_p+e_q` to force the axis `e_q` into the zero subgroup.

Failure of steps 1--4 would contradict standard translation-invariant Markov harmonic analysis. Steps 5--6 are elementary group identities.

The research consequence is a sharp narrowing of the main positive-solenoid frontier exposed by `WP-038`:

\[
\boxed{
\text{nonlocal transverse Dirichlet form}
+\text{translation invariance}
+\text{direct Mangoldt Fourier support}
\quad\text{is impossible}.
}
\]

A viable Mathia-native solenoidal route must therefore break at least one of those three ingredients. The most structurally faithful surviving targets are now **non-translation-invariant arithmetic coupling**, **matrix/graded or boundary compression before scalarization**, or a **single nonseparable finite--archimedean form whose sign theorem applies before any explicit-formula decomposition**. Those are materially stronger requirements than merely replacing the rational-square leafwise Laplacian of `WP-038` by a more complicated positive pseudodifferential symbol.