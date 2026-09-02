# PL-122 — The 2026 competing-Ising GRH claim does not cross the continuation or zero-locus gates

## Claim

Zhidong Zhang's 2026 *Physics Letters A* paper claims an equivalence between the nontrivial zero distributions of the Riemann zeta/Dirichlet L-functions and the partition-function zeros of a two-dimensional Ising model with one ferromagnetic direction and randomly distributed competing ferromagnetic/antiferromagnetic interactions in the other direction. The current arXiv revision is `2411.16777v4` (16 August 2026), and the paper explicitly presents the construction as a proof-level route to the generalized Riemann hypothesis.

For the `prime_lattice` program, the proposed bridge fails at two exact mathematical gates before any critical-line conclusion can be drawn.

First, the paper's central partition-function identification imports the classical primon spectrum

\[
E_n=\mathcal E\log n
\]

and then writes

\[
\bar Z_\alpha
 =\sum_{n\ge1}e^{-E_n/(k_BT)}
 =\sum_{n\ge1}n^{-s}
 =\zeta(s),
\qquad
s=\frac{\mathcal E}{k_BT}.
\]

But the displayed Dirichlet series converges only for `Re(s)>1`, where `zeta(s)` has no zeros. The nontrivial zeros lie in `0<Re(s)<1`, where this ordinary partition sum does not converge. The paper does not prove an analytic continuation of the Ising partition function that equals the continued zeta function in the critical strip. Consequently the asserted equivalence between Ising partition zeros and nontrivial zeta zeros is not established by this identity.

Second, the exact logarithmic spectrum is not derived from the stated competing nearest-neighbor Ising Hamiltonian. Statistical/GUE-type similarity of level fluctuations cannot imply exact equality of spectra, counting measures, or partition functions. In prime-exponent coordinates the imported spectrum is simply

\[
E_n=\mathcal E\langle v(n),(\log p)_p\rangle,
\]

which is Julia's classical one-dimensional primon-gas energy already recorded in `PL-004`, not a new transverse geometry of the exponent lattice.

A separate zero-locus gap remains even if those two steps were repaired. The classical Lee--Yang circle theorem concerns **ferromagnetic** Ising interactions and zeros in the **complex external-field variable**. Fisher zeros are zeros in a complex-temperature variable and their loci depend on the model, interaction pattern, and boundary conditions. The cited circle-theorem machinery therefore does not by itself prove that the mixed-sign random competing model used in the paper has all of its Fisher zeros on one unit circle. Modern exact studies give explicit controls in which complex-temperature zero sets change with boundary conditions and can be dense in large regions of the complex plane even for Ising/Potts specializations.

Finally, self-adjointness of the Ising Hamiltonian only makes its energy eigenvalues real. It would imply RH only after an **independent exact theorem** identifying every nontrivial zeta zero with `1/2+iE` for that Hamiltonian. That spectral identification is precisely what the preceding unsupported steps are supposed to establish; defining an operator of the form `R=(1/2)I+iH` after the fact does not supply the missing theorem.

**Evidence/status:** `LITERATURE + EXACT-DERIVED + DECISIVE-NEGATIVE + CURRENT-CLAIM-AUDIT` for this specific proposed Ising/GRH mechanism. This finding does not claim that Ising, Lee--Yang, Fisher-zero, or statistical-mechanical approaches to zeta are impossible in principle. It records that the 2026 construction, as presently written, does not provide the required analytic-continuation, exact-spectrum, or zero-locus bridges.

## 1. The partition identity is confined to the zero-free half-plane

The paper's equation (21) invokes the statistical theory of primes and writes a replica partition function as

\[
\bar Z_\alpha=\sum_{n=1}^{\infty}e^{-E_n/(k_BT)}
             =\sum_{n=1}^{\infty}n^{-s}
             =\zeta(s),
\qquad E_n=\mathcal E\log n.
\]

For fixed complex `s=sigma+it`, the classical Dirichlet series

\[
\sum_{n\ge1}n^{-s}
\]

converges exactly in `sigma>1`. In this domain it equals the Euler product

\[
\prod_p(1-p^{-s})^{-1},
\]

so it is nonzero. Thus, **inside the only half-plane where the displayed infinite partition sum is actually defined by that series, it has no Riemann zeros at all**.

The analytically continued zeta function is of course meaningful in the critical strip, but analytic continuation of `zeta` does not automatically analytically continue an independently defined statistical-mechanical partition function. To transfer the nontrivial divisor one needs a theorem producing a meromorphic/entire continuation of the Ising object and proving equality with the continued zeta object there. No such bridge follows from equation (21), and the paper does not supply one before using the critical-strip zeros.

This is the same continuation discipline enforced throughout `prime_lattice`: an identity derived from the Euler/Dirichlet expansion in `Re(s)>1` cannot be transported term-by-term into the critical strip merely by replacing the convergent series with the symbol `zeta(s)`.

## 2. The logarithmic spectrum is imported rather than derived from the Ising Hamiltonian

The physical model introduced earlier in the paper is a nearest-neighbor Ising Hamiltonian of the schematic form

\[
H=-\sum_{\langle i,j\rangle}
   \left(J_1 s_{i,j}s_{i+1,j}
   +\widetilde J_2 s_{i,j}s_{i,j+1}\right),
\]

where the second-direction couplings include randomly distributed ferro- and antiferromagnetic values. The discussion then appeals to random-matrix/GUE-like statistics and to statistical resemblance between the resulting energies and arithmetic data.

That type of statement is not enough to justify the exact spectral replacement

\[
\{E_j(H)\}\stackrel{?}{=}\{\mathcal E\log n:n\ge1\}.
\]

Equality of local spacing statistics, membership in the same universality class, or similar empirical distributions does not determine individual levels, multiplicities, the spectral counting measure, or the partition function. Infinitely many inequivalent spectra can share the same limiting local statistics.

The distinction matters because the next equation uses exact equality, not universality: only an exact `E_n=mathcal E log n` assignment turns the thermal trace into a zeta Dirichlet series. The paper therefore moves from a statistical analogy to the exact primon spectrum without a derivation from the competing Ising transfer matrix/Hamiltonian.

For this line the arithmetic content of that inserted spectrum is already completely known. If `alpha=v(n)`, then

\[
E_n=\mathcal E\log n
   =\mathcal E\sum_p\alpha_p\log p
   =\mathcal E\langle\alpha,\ell\rangle,
\qquad \ell_p=\log p.
\]

It factors through the scalar log-energy exactly as in `PL-004` and the classical primon gas. No pairwise or higher-rank information about mixed prime coordinates is generated by the Ising model at this step. In particular, the claimed zeta partition function is obtained by importing the baseline prime-lattice Hamiltonian rather than deriving a new arithmetic Hamiltonian from spin geometry.

## 3. Lee--Yang does not supply the asserted Fisher circle for the competing model

The distinction between Lee--Yang and Fisher zeros is load-bearing here.

For the ferromagnetic Ising model, the Lee--Yang theorem concerns the partition function regarded as a polynomial in the complex **external field** parameter. In a standard normalization, its zeros lie on the unit circle. Modern rigorous treatments state the ferromagnetic hypothesis and the external-field variable explicitly; for example, Buys--Galanis--Patel--Regts formulate the theorem for the ferromagnetic Ising partition function as a polynomial in the external-field parameter `lambda`.

The model in the Zhang paper instead contains competing mixed-sign couplings and the relevant claimed circle consists of **Fisher zeros in complex temperature**. Those are different objects. A Fisher-circle statement requires a theorem for the actual interaction pattern and thermodynamic/boundary setup; it does not follow from the Lee--Yang field theorem merely because both descriptions use a unit circle after a change of variables.

There are direct controls against treating a Fisher circle as universal. Jacobsen, Richard, and Salas study complex-temperature partition-function zeros for Potts/RSOS models and show strong boundary-condition dependence; with free transverse boundary conditions, the zeros can be dense in large parts of the complex plane even in the Ising specialization. More recent exact work on Ising Fisher zeros likewise emphasizes special boundary conditions, such as Brascamp--Kunz-type conditions, under which particularly simple circle loci occur.

Therefore the implication

\[
\text{competing random Ising model}
\Longrightarrow
\text{all Fisher zeros on one unit circle}
\]

needs its own proof under the actual model hypotheses. Citing the classical Lee--Yang theorem and homogeneous Fisher-zero lore does not establish it.

## 4. Real energies do not locate zeta zeros without an exact spectral bridge

The paper also uses the reality of the Ising energy eigenvalues as a Hilbert--Polya-type ingredient. The elementary operator statement is correct: if `H` is self-adjoint, then `spec(H)` is real, and hence

\[
\operatorname{spec}\left(\frac12 I+iH\right)
\subseteq\frac12+i\mathbb R.
\]

But this says nothing about the zeta divisor until one has independently proved

\[
\{\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}
=
\operatorname{spec}\left(\frac12 I+iH\right)
\]

with the required multiplicities/domain interpretation. A hypothetical off-line zero `beta+i gamma` already has a real ordinate `gamma`; the fact that an unrelated Hamiltonian has real energies does not force `beta=1/2`.

Thus the logical load is entirely in the spectral-identification theorem. In this construction that identification is meant to come from the partition-function equality, the statistical spectral analogy, and the Fisher-circle mapping, precisely the steps that fail the exact gates above. Self-adjointness cannot be used to repair them without circularity.

## 5. Prime-lattice interpretation and collision with stored prior art

The paper is relevant to this line because its arithmetic Hamiltonian uses exactly the canonical exponent-lattice energy

\[
\log n=\langle v(n),(\log p)_p\rangle.
\]

But the extra 2D spin description does not derive a new operation on `v(n)`. At the point where arithmetic enters exactly, all states have already been compressed to the scalar `log n`. This collides directly with `PL-004`, which records Julia's classical free primon gas, and with the broader obstruction accumulated by the line: reproducing `zeta` as a partition function in `Re(s)>1` is not a mechanism for analytic continuation or zero localization.

The comparison with `PL-106` is also useful but not identical. `PL-106` audits an engineered quantum DQPT setup whose logarithmic Hamiltonian can read out programmed Dirichlet series; there the continuation into the strip is supplied by an encoded eta/Riemann--Siegel device. The present paper instead claims that the competing Ising model itself supplies the needed zero geometry, but equation (21) leaves the continuation bridge absent and imports the same classical logarithmic spectrum. The failure mode is therefore a distinct and stronger current-example of the line's continuation gate.

Nothing here rules out a statistical-mechanical route that genuinely creates new arithmetic structure. It rules out treating

\[
\text{real random Ising energies}
+\text{GUE resemblance}
+\text{inserted }\log n\text{ spectrum}
+\text{circle analogy}
\]

as an exact proof of the zeta critical-line statement.

## Prior-art and source audit

Primary/current source:

- **Zhidong Zhang**, “Equivalence between the zero distributions of the Riemann zeta function and a competing two-dimensional Ising model,” *Physics Letters A* **591** (2026), 131910, DOI `10.1016/j.physleta.2026.131910`; expanded/current preprint **arXiv:2411.16777v4**, revised 16 August 2026. The preprint explicitly describes the mixed ferro/antiferromagnetic model, the claimed real-energy/GUE correspondence, the primon partition identity, the Fisher-circle argument, and the claimed closure of the Riemann/Dirichlet zero distribution.

Prior-art/control sources:

- **Bernard L. Julia**, “Statistical theory of numbers,” in *Number Theory and Physics*, Springer Proceedings in Physics **47** (1990), 276--293. Classical source for the primon gas with one-particle energies `log p`, total energy `log n`, and partition function `zeta(beta)` in its convergence domain; already anchored by `PL-004`.
- **T. D. Lee and C. N. Yang**, “Statistical Theory of Equations of State and Phase Transitions. II. Lattice Gas and Ising Model,” *Physical Review* **87** (1952), 410--419, together with **C. N. Yang and T. D. Lee**, Part I, *Physical Review* **87** (1952), 404--409. Classical Lee--Yang circle theorem; its Ising application is a ferromagnetic external-field-zero theorem, not a generic Fisher-temperature theorem.
- **Pjotr Buys, Andreas Galanis, Viresh Patel, Guus Regts**, “Lee--Yang zeros and the complexity of the ferromagnetic Ising model on bounded-degree graphs,” *Forum of Mathematics, Sigma* **10** (2022), e7, DOI `10.1017/fms.2022.4`. Modern rigorous statement making the ferromagnetic and external-field hypotheses explicit.
- **Jesper Lykke Jacobsen, Jean-François Richard, Jesús Salas**, “Complex-temperature phase diagram of Potts and RSOS models,” *Nuclear Physics B* **743** (2006), 153--206, DOI `10.1016/j.nuclphysb.2006.02.033`, arXiv:`cond-mat/0511059`. Provides a direct control showing that complex-temperature zero loci depend strongly on model/boundary conditions and can be dense in large portions of the complex plane even at the Ising specialization.
- **De-Zhang Li, Xin Wang**, “Free-fermion approach to the partition function zeros: Special boundary conditions and product form of solution,” *Physical Review Research* **7** (2025), 043258, DOI `10.1103/b6d1-6sk5`. Modern control emphasizing that especially simple exact Fisher-zero loci arise under special boundary conditions.

No novelty is claimed for the convergence domain of the zeta Dirichlet series, the primon-gas representation, Lee--Yang theory, Fisher zeros, or self-adjoint spectral reality. The durable `prime_lattice` result is the exact collision audit of this fresh published RH/GRH claim against those established gates.

## Adversarial boundaries

1. **The critique does not depend on whether the model is physically interesting.** A disordered/competing Ising system may have meaningful random-matrix statistics or phase behavior. The objection is to using those statistical features as exact arithmetic identities.

2. **Analytic continuation of zeta itself is not in question.** The missing theorem is continuation of the proposed *Ising partition object* together with equality to continued zeta. One cannot transfer a divisor from the latter to the former merely because their formulas agree where the original Dirichlet series converges.

3. **A statistical limit could in principle produce `log n` levels, but it must be proved.** The finding does not assert that no Ising construction can have logarithmic spectrum; it records that GUE/universality arguments do not establish the exact spectrum required by equation (21).

4. **Lee--Yang and Fisher theory remain powerful.** The point is variable and hypothesis mismatch. A new theorem proving a Fisher circle for this precise competing random model would remove one objection, but not the independent continuation and spectral-identification gaps.

5. **Self-adjointness would become decisive after an exact divisor correspondence.** If an independently constructed self-adjoint `H` were proved to satisfy `spec((1/2)I+iH)=Z(zeta)` in the required sense, RH would follow. This finding does not deny Hilbert--Polya; it says the current paper has not established that antecedent.

6. **Publication status is not used as an argument either way.** The mathematical audit applies to the published/current formulas and implications themselves.

## Decisive repair/falsification tests

This finding would need material revision if the construction supplied all of the following missing bridges:

1. an exact derivation from the stated competing Ising Hamiltonian/transfer matrix to the logarithmic arithmetic spectrum, including multiplicities and the thermodynamic limit, rather than a statistical/GUE analogy;
2. a canonical meromorphic/entire continuation of the Ising partition function from its convergent thermal domain into the critical strip, with a theorem proving equality there to the analytically continued/completed zeta or L-function;
3. a valid Fisher-zero localization theorem for the actual mixed-sign random interaction model and boundary/thermodynamic regime used, not an appeal to the ferromagnetic Lee--Yang external-field theorem or to a special homogeneous Fisher locus;
4. a non-circular proof that the analytically continued zeta divisor equals the spectrum or zero set of that Ising object before self-adjointness/unit-circle reality is invoked to localize it.

Any one of these would be substantive new mathematics. Without them, the route does not cross the established `prime_lattice` evidence gates.

## Consequence for `prime_lattice`

The 2026 Ising/GRH claim is not a surviving new mechanism for this line. At its exact arithmetic step it falls back to the classical rank-one scalar energy

\[
\log n=\langle v(n),(\log p)_p\rangle,
\]

and it does not supply the global continuation theorem needed to make critical-strip zeros into zeros of the statistical-mechanical object. The additional circle/self-adjointness language is downstream of an unproved divisor correspondence.

A viable statistical-mechanical escape would therefore need to do more than reproduce the primon partition function or imitate zero statistics. It must derive a canonical arithmetic interaction not reducible to scalar `log n`, carry it through a genuine analytic-continuation/determinant theorem, and prove a positivity/unitarity/zero-locus statement under the actual model hypotheses. That is the structural burden left by this audit.