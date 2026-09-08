# PL-213 — Bost–Connes high-temperature factor type is `III_1` throughout; the modular scale does not select `1/2`

## Claim

The Bost–Connes system already supplies a genuinely operator-algebraic continuation of its arithmetic dynamics below the Gibbs trace-class boundary `beta=1`: for every real inverse temperature

\[
0<\beta\le 1,
\]

the unique KMS state generates a factor of type `III_1`. Consequently its Connes ratio-set/modular-scale invariant is the full positive multiplicative group

\[
\mathbb R_{+}^{\times}
\]

throughout the entire high-temperature interval, including `beta=1/2`. There is therefore **no factor-type transition, discrete modular-spectrum transition, or Connes-scale narrowing at the Riemann critical half**.

This closes a natural operator-algebraic escape left after `PL-024`, `PL-211`, and `PL-212`: replacing the divergent Gibbs trace by the canonical KMS/GNS von Neumann algebra does produce nontrivial type-III modular structure, but that structure is already maximally non-discrete for every `0<beta<=1`. It cannot by itself distinguish `beta=1/2`, encode the Riemann zero divisor, or turn the Bost–Connes thermodynamic continuation into analytic continuation of `zeta`.

The prime-exponent interpretation makes the coarseness transparent. The positive exponent cone

\[
\mathbb N_0^{(\mathcal P)}
\]

group-completes to

\[
\mathbb Z^{(\mathcal P)}\cong\mathbb Q_{+}^{\times},
\]

and the logarithmic energy extends to

\[
E(k)=\sum_p k_p\log p=\log q.
\]

For the Bost–Connes KMS measure the Radon–Nikodym scaling under the corresponding rational action is `q^beta` up to the inverse convention for the acting element. Neshveyev's theorem proves the nontrivial measurable statement that the resulting ratio set is not merely a countable collection of these raw derivatives but **all** of `R_+^times` for every `0<beta<=1`.

Thus

\[
\boxed{
0<\beta\le1
\quad\Longrightarrow\quad
\text{BC KMS}_\beta\text{ factor is type }III_1
\quad\Longrightarrow\quad
r\setminus\{0\}=\mathbb R_+^\times,
}
\]

with no special change at `beta=1/2`.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`.

The negative is deliberately restricted to the **factor type, ratio set, flow-of-weights class, and modular-scale closure** of the canonical high-temperature Bost–Connes equilibrium representation. It does not say that the full arithmetic algebra, individual state-dependent modular correlations, the cyclotomic observables of `PL-212`, the divisibility observables of `PL-211`, or later adelic/Weil/trace-formula constructions contain no finer arithmetic information.

## 1. The exponent lattice group-completes to the rational scaling group

The one-sided prime lattice is the free commutative monoid

\[
\mathcal L_+
=\mathbb N_0^{(\mathcal P)}.
\]

The map

\[
\alpha=(\alpha_p)_p
\longmapsto
n(\alpha)=\prod_p p^{\alpha_p}
\]

identifies `L_+` with the multiplicative monoid of positive integers. Its Grothendieck group is

\[
\mathcal L
n=\mathbb Z^{(\mathcal P)},
\]

which is canonically the multiplicative group of positive rationals:

\[
\alpha\longmapsto
q(\alpha)=\prod_p p^{\alpha_p}
\in\mathbb Q_+^\times.
\]

The energy functional used throughout this line extends without modification:

\[
E(\alpha)
=\left\langle\alpha,(\log p)_p\right\rangle
=\sum_p\alpha_p\log p
=\log q(\alpha).
\]

This is the group-level completion of the Bost–Connes covariance recorded in `PL-024`:

\[
[H,\mu_n]=(\log n)\mu_n,
\qquad
\sigma_t(\mu_n)=n^{it}\mu_n.
\]

The point of passing to the group completion is not to create a new arithmetic object. It is to identify exactly which multiplicative scale the modular theory of the nonsingular adelic action can see.

## 2. The canonical KMS continuation below `beta=1` is type `III_1`

For the original rational Bost–Connes system, the Gibbs representation at `beta>1` has

\[
\operatorname{Tr}(e^{-\beta H})=\zeta(\beta),
\]

and its extremal KMS states are type I. `PL-024` already records that this ordinary trace ceases to exist at `beta<=1` and that the KMS states there are not obtained by analytically continuing the scalar partition function.

The operator-algebraic replacement is much stronger than merely saying that a KMS functional still exists. Sergey Neshveyev proves for Bost–Connes type systems over number fields that for every

\[
0<\beta\le1
\]

the KMS state has type `III_1`. For the rational system this specializes exactly to the original Bost–Connes high-temperature phase. In the introduction of his 2011 paper he states the rational case explicitly: `beta>1` extremal states are type I with partition function `zeta(beta)`, while every `beta in (0,1]` has a unique KMS state of type `III_1`.

The theorem is not a formal consequence of the list of rational Radon–Nikodym factors. Neshveyev identifies the KMS state with a nonsingular adelic action and proves that its ratio set is full. In his notation, for the number-field system the relevant measure satisfies

\[
\frac{d(g\mu_\beta)}{d\mu_\beta}=N(g)^\beta,
\]

and Theorem 2.1 states that the action is type `III_1` for every `0<beta<=1`.

For an ergodic nonsingular action, the nonzero ratio set is a closed subgroup of `R_+^times`. Type `III_1` means precisely

\[
\boxed{
r(\mathcal R)\setminus\{0\}
=\mathbb R_+^\times.
}
\]

Equivalently, the associated flow of weights is trivial. This is the correct invariant to use here: the claim is about the **Connes modular scale / ratio-set invariant of the factor**, not about the point spectrum of one particular modular operator.

The primary source is:

- Sergey Neshveyev, “von Neumann Algebras Arising from Bost–Connes Type Systems,” *International Mathematics Research Notices* **2011**(1) (2011), 217–236, DOI `10.1093/imrn/rnq067`, arXiv `0907.1456`. The abstract and Theorem 2.1 prove type `III_1` for Bost–Connes type KMS states throughout `0<beta<=1`; Section 1 identifies type `III_1` with full positive ratio set and trivial flow of weights.

The underlying rational ergodicity/uniqueness theorem is:

- Sergey Neshveyev, “Ergodicity of the action of the positive rationals on the group of finite adeles and the Bost-Connes phase transition theorem,” *Proceedings of the American Mathematical Society* **130** (2002), 2999–3003, arXiv `math/0002141`.

No novelty is claimed for either theorem or for the Bost–Connes factor classification.

## 3. Why the number `1/2` cannot be recovered from the factor type

The theorem is already decisive for any proposal that asks the high-temperature GNS factor itself to select the critical half. The map

\[
\beta\longmapsto
\operatorname{type}(M_\beta)
\]

is constant on the whole interval:

\[
\operatorname{type}(M_\beta)=III_1,
\qquad
0<\beta\le1.
\]

Likewise the nonzero ratio set is constant:

\[
r(M_\beta)\setminus\{0\}
=\mathbb R_+^\times.
\]

Therefore `beta=1/2` is indistinguishable from `beta=1/3`, `2/3`, or any other point of the high-temperature regime by these invariants. This is stronger than the observation in `PL-024` that there is no thermodynamic phase transition at `1/2`: even after replacing the divergent Gibbs density matrix by the full type-III modular apparatus, the coarse modular invariant stays exactly the same.

The same conclusion holds for any construction that depends only on the **closure** of the rational modular scale. For fixed `beta>0`,

\[
\{q^\beta:q\in\mathbb Q_+^\times\}
\]

is dense in `R_+^times`, because `Q_+^times` is dense in `R_+^times` and `x -> x^beta` is a homeomorphism. Thus even before the nontrivial measurable ratio-set theorem is invoked, taking only the topological closure of available rational scaling values erases `beta` completely.

There is an even sharper finite-generator control. Unique factorization gives

\[
\frac{\log2}{\log3}\notin\mathbb Q,
\]

since a rational relation `m log2=n log3` would imply `2^m=3^n`. Hence the additive subgroup

\[
\{m\log2+n\log3:m,n\in\mathbb Z\}
\]

is dense in `R`, and after exponentiation

\[
\{2^m3^n:m,n\in\mathbb Z\}
\]

is dense in `R_+^times`. Raising to any positive `beta` leaves the closure unchanged.

This **does not prove** the type-`III_1` theorem: a raw dense set of possible Radon–Nikodym values need not belong to the measurable ratio set, because ratio-set membership requires recurrence on arbitrary positive-measure sets. Neshveyev's prime-ideal argument supplies precisely that hard ergodic step. The two-prime calculation is only an adversarial control showing why the topological modular closure itself is too coarse to carry deep all-prime or zero-divisor information.

## 4. The full ratio set is not analytic continuation of `zeta`

The parameter `beta` in this theorem is a **real inverse temperature**. The type-III statement is an operator-algebraic property of a KMS state and its GNS von Neumann algebra. It does not define a holomorphic function of complex `s`, does not extend the Euler product, and does not evaluate `zeta(beta)` where the Gibbs trace diverges.

This distinction is especially important at `beta=1/2`. The facts

\[
M_{1/2}\text{ is type }III_1
\]

and

\[
r(M_{1/2})\setminus\{0\}=\mathbb R_+^\times
\]

contain no assertion about

\[
\zeta(1/2+it),
\]

its zero divisor, the functional equation, or Weil positivity. There is no legitimate step

\[
\operatorname{Tr}(e^{-\beta H})=\zeta(\beta)
\quad(\beta>1)
\]

followed by “replace the trace with a type-III KMS factor” and then interpret the resulting modular data as the analytic continuation of the same scalar function. `PL-211` already exhibits this failure concretely for the canonical Möbius observable: the KMS limit at `beta=1/2` disagrees with the analytically continued Gibbs scalar. `PL-212` gives a second version: symmetry restoration projects the canonical finite cyclotomic equilibrium channel onto an elementary zeta-free function.

`PL-213` supplies the corresponding **factor-level** boundary. The operator-algebraic continuation is mathematically rich, but its coarsest intrinsic modular invariant is constant throughout the interval and hence carries no critical-half selector.

## 5. Adversarial audit: why `III_1` is not hidden Hilbert–Pólya data

A tempting interpretation would be that type `III_1` is “maximally continuous,” so perhaps a distinguished temperature inside that phase could emerge from the modular spectrum and be related to Riemann zeros. The present theorem does not support that inference.

First, the type invariant has already quotiented away the information needed to distinguish temperatures. For every `beta in (0,1]` it records the same closed scaling group. Any scalar statistic that is a function only of the Connes type, the ratio-set closure, or triviality of the flow of weights is therefore identically constant on the whole interval.

Second, maximal modular scale is not specific to the full rational-prime lattice. As the `2,3` control shows, dense logarithmic scaling already appears from two multiplicatively independent generators. The genuinely arithmetic part of Neshveyev's theorem is the ergodic realization of the full ratio set, but the resulting invariant no longer remembers which prime set produced it.

Third, type `III_1` does not place a discrete self-adjoint spectrum at the ordinates of the Riemann zeros. It is a classification of nonsingular modular behavior. Turning it into a Hilbert–Pólya mechanism would require additional source-forced data that selects a zero-sensitive operator, proves an appropriate self-adjointness/positivity statement, and connects its spectral parameter to the completed zeta divisor. None of those steps follows from the factor type.

A matched deformation principle is therefore immediate at the level of the proposed readout: **any two systems whose relevant KMS factors are type `III_1` are indistinguishable by factor type alone**, regardless of their detailed arithmetic observables. The readout is too coarse by definition. This is analogous to the information-loss controls elsewhere in the line: a mathematically natural quotient can be exact while erasing precisely the target-sensitive coordinate.

## 6. Relation to `PL-024`, `PL-211`, and `PL-212`

The sequence of Bost–Connes tests now separates three different layers.

`PL-024` tests the elementary log-prime covariance and thermodynamics. It shows

\[
[H,\mu_p]=(\log p)\mu_p
\]

is classical Bost–Connes structure and that the Gibbs/phase boundary is `beta=1`, not `1/2`.

`PL-211` tests a canonical Möbius orientation built from divisibility projections. It finds a genuine `beta=1/2` `L^2` support threshold, but proves that threshold is phase-blind; coherent Möbius parity appears only for `beta>1`, and the KMS extension does not analytically continue the Gibbs Möbius expectation.

`PL-212` then allows the arithmetic cyclotomic/Galois algebra to participate. In the unique high-temperature KMS state, symmetry restoration keeps only the invariant finite Galois harmonic, and that channel cancels the Riemann zeta denominator exactly. The zero-sensitive `L(s,chi)/zeta(s)` harmonics belong to the broken-symmetry family and do not continue as positive KMS states into the critical interval.

The present finding tests a remaining operator-algebraic escape: perhaps the **modular von Neumann algebra itself** has a finer threshold at the half. It does not. Its type and ratio-set invariant are already maximally non-discrete for the entire interval.

The combined boundary is therefore

\[
\boxed{
\begin{array}{rcl}
\text{Gibbs trace / symmetry breaking} &:& \beta=1,\\
\text{square-free second moment} &:& \beta=1/2\ \text{but phase-blind},\\
\text{high-temperature factor type} &:& III_1\ \text{for all }0<\beta\le1.
\end{array}
}
\]

These are three different mathematical phenomena and should not be conflated.

## 7. Boundaries and surviving routes

The negative does **not** say that modular theory is irrelevant to arithmetic or that the Bost–Connes system cannot participate in an RH program. It says only that the most canonical coarse modular invariants of its high-temperature KMS representation do not distinguish the Riemann critical half.

Several categories remain outside the claim:

- state-dependent arithmetic correlations inside the type-`III_1` factor that retain more than its isomorphism/type invariant;
- relative modular operators tied to a distinguished arithmetic target rather than the equilibrium factor alone;
- cyclotomic, endomotive, or adelic observables whose cross-prime relations survive the KMS averaging without reducing to the factor type;
- Connes' later adele-class trace formula and the completed Fourier/Weil machinery, where the zeta zeros enter through substantially more structure than the Bost–Connes KMS phase classification;
- a source-forced positivity, polarization, or totality theorem that acts on a zero-sensitive representation before the modular information is quotiented to the type-`III_1` invariant.

Any such escape must demonstrate explicitly which information it retains that the ratio-set/type classification forgets. Merely observing “type `III_1` at `beta=1/2`,” “full modular spectrum,” or “dense log-prime scaling” is no longer evidence for an RH mechanism.

## Prior-art and novelty audit

The decisive theorem is established prior art. Neshveyev's 2011 paper proves the full type-`III_1` statement and explains its equivalence to adelic ergodicity/ratio-set results. His 2002 paper proves the rational positive-rational ergodicity used in the Bost–Connes phase-transition analysis. Bost and Connes (1995) supply the original arithmetic system, time evolution, KMS phase diagram, and type-III setting.

A targeted search around Bost–Connes factor type, KMS modular spectrum, critical temperature, and Riemann hypothesis found the standard operator-algebraic classification and many richer arithmetic/quantum-statistical reformulations, but no theorem making `beta=1/2` a distinct Connes-type or ratio-set boundary. The novelty status is therefore deliberately negative: **the relevant modular mechanism is classical, and its exact theorem removes rather than creates a critical-half discriminator**.

The only line-specific derived content is the interpretation in prime-exponent coordinates, the explicit group-completion/log-energy identification, the two-generator density control, and the resulting information-boundary statement relative to the current `prime_lattice` program.

## Consequence for the research line

The Bost–Connes branch now has a sharper gate. It is not enough to move from a divergent Gibbs trace to a type-III KMS representation and then appeal to modular theory in the abstract. In the canonical system that move has already been carried out, and the resulting factor is `III_1` everywhere below the thermodynamic transition.

A viable Bost–Connes-derived RH mechanism must therefore use **finer arithmetic data than factor type or modular-scale closure**, and that finer data must survive two independent checks:

1. it must retain rational-prime/global-completion information that is lost by generic type-`III_1` classification; and
2. it must impose a zero-sensitive positivity, localization, totality, or spectral constraint that is not merely analytic continuation of a scalar Gibbs formula.

In particular, the appearance of a continuous modular scale at `beta=1/2` is not a new explanation of the critical line. The canonical high-temperature factor already has the same scale at every other `beta` in `(0,1]`.