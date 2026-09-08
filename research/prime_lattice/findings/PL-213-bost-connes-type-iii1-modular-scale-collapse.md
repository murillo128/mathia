# PL-213 — Bost–Connes high-temperature factor type is `III_1` throughout; the modular scale does not select `1/2`

## Claim

The Bost–Connes system already supplies a genuine operator-algebraic continuation of its arithmetic dynamics below the Gibbs trace-class boundary `beta=1`: for every real inverse temperature

\[
0<\beta\le1,
\]

the unique KMS state generates a factor of type `III_1`. Consequently its Connes ratio-set/modular-scale invariant is the full positive multiplicative group

\[
\mathbb R_+^\times
\]

throughout the entire high-temperature interval, including `beta=1/2`. There is therefore **no factor-type or Connes-scale transition at the Riemann critical half**.

This closes a natural operator-algebraic escape left after `PL-024`, `PL-211`, and `PL-212`: replacing the divergent Gibbs trace by the canonical KMS/GNS von Neumann algebra does produce nontrivial type-III modular structure, but that structure is already maximally non-discrete for every `0<beta<=1`. It cannot by itself distinguish `beta=1/2`, encode the Riemann zero divisor, or turn the Bost–Connes thermodynamic continuation into analytic continuation of `zeta`.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`.

The negative is deliberately restricted to the **factor type, ratio set, flow-of-weights class, and topological modular-scale closure** of the canonical high-temperature Bost–Connes equilibrium representation. It does not say that the full arithmetic algebra, state-dependent modular correlations, the cyclotomic observables of `PL-212`, the divisibility observables of `PL-211`, or later adelic/Weil/trace-formula constructions contain no finer arithmetic information.

## 1. The exponent lattice group-completes to the rational scaling group

The one-sided prime lattice is the free commutative monoid

\[
\mathcal L_+=\mathbb N_0^{(\mathcal P)}.
\]

The map

\[
\alpha=(\alpha_p)_p
\longmapsto
n(\alpha)=\prod_p p^{\alpha_p}
\]

identifies `L_+` with the multiplicative monoid of positive integers. Its Grothendieck group is

\[
\mathcal L=\mathbb Z^{(\mathcal P)},
\]

canonically identified with the multiplicative group of positive rationals by

\[
\alpha\longmapsto q(\alpha)=\prod_p p^{\alpha_p}
\in\mathbb Q_+^\times.
\]

The logarithmic energy extends exactly:

\[
E(\alpha)
=\left\langle\alpha,(\log p)_p\right\rangle
=\sum_p\alpha_p\log p
=\log q(\alpha).
\]

This is the group-level completion of the Bost–Connes covariance already recorded in `PL-024`,

\[
[H,\mu_n]=(\log n)\mu_n,
\qquad
\sigma_t(\mu_n)=n^{it}\mu_n.
\]

The group completion is not a new arithmetic object. It only identifies the multiplicative scale available to the modular theory of the nonsingular adelic action.

## 2. The canonical high-temperature KMS factor is type `III_1`

For `beta>1`, the standard positive-energy representation has the ordinary Gibbs partition trace

\[
\operatorname{Tr}(e^{-\beta H})=\zeta(\beta),
\]

and extremal KMS states are type I. At `beta<=1` this trace is no longer finite; `PL-024` already records that the KMS states that continue to exist are not obtained by analytically continuing that scalar trace.

Sergey Neshveyev proves the stronger operator-algebraic statement. For Bost–Connes type systems over number fields, Theorem 2.1 of his 2011 paper states that every KMS state in

\[
0<\beta\le1
\]

has type `III_1`. For the rational system, the introduction states explicitly that every `beta in (0,1]` has a unique KMS state of type `III_1`.

The proof is formulated through a nonsingular adelic action. The KMS measure has Radon–Nikodym scaling

\[
\frac{d(g\mu_\beta)}{d\mu_\beta}=N(g)^\beta,
\]

and Neshveyev proves that the associated ratio set is full. For an ergodic nonsingular action, the nonzero ratio set is a closed subgroup of `R_+^times`; type `III_1` means precisely

\[
\boxed{
r(\mathcal R)\setminus\{0\}=\mathbb R_+^\times.
}
\]

Equivalently, the associated flow of weights is trivial. The claim here is therefore about the **Connes modular scale / ratio-set invariant of the factor**, not about the point spectrum of one particular modular operator.

The primary sources are:

- Sergey Neshveyev, “von Neumann Algebras Arising from Bost–Connes Type Systems,” *International Mathematics Research Notices* **2011**(1) (2011), 217–236, DOI `10.1093/imrn/rnq067`, arXiv `0907.1456`. The abstract and Theorem 2.1 prove type `III_1` throughout `0<beta<=1`; Section 1 identifies type `III_1` with full positive ratio set and trivial flow of weights.
- Sergey Neshveyev, “Ergodicity of the action of the positive rationals on the group of finite adeles and the Bost-Connes phase transition theorem,” *Proceedings of the American Mathematical Society* **130** (2002), 2999–3003, arXiv `math/0002141`. This supplies the rational positive-rational ergodicity underlying the high-temperature phase analysis.
- Jean-Benoît Bost and Alain Connes, “Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory,” *Selecta Mathematica, New Series* **1** (1995), 411–457, DOI `10.1007/BF01589495`.

No novelty is claimed for these results or for the factor classification.

## 3. Why the factor invariant cannot recover `1/2`

The theorem is already decisive for any proposal that asks the high-temperature GNS factor itself to select the critical half. Both

\[
\operatorname{type}(M_\beta)=III_1
\]

and

\[
r(M_\beta)\setminus\{0\}=\mathbb R_+^\times
\]

are constant for every `0<beta<=1`. Thus `beta=1/2` is indistinguishable from `1/3`, `2/3`, or any other point of the high-temperature phase by factor type, ratio set, or triviality of the flow of weights.

This is stronger than the thermodynamic observation in `PL-024`. There is not merely no phase transition at `1/2`; even after replacing the divergent density matrix by the full type-III modular framework, its coarse intrinsic modular invariant remains unchanged.

The same information loss is visible at the purely topological scale level. For fixed `beta>0`,

\[
\{q^\beta:q\in\mathbb Q_+^\times\}
\]

is dense in `R_+^times`, because `Q_+^times` is dense and `x\mapsto x^beta` is a homeomorphism. Hence any construction using only the closure of the rational scaling values erases `beta` automatically.

There is even a two-prime control. Unique factorization gives

\[
\frac{\log2}{\log3}\notin\mathbb Q,
\]

so the additive subgroup

\[
\{m\log2+n\log3:m,n\in\mathbb Z\}
\]

is dense in `R`; exponentiating gives a dense subgroup

\[
\{2^m3^n:m,n\in\mathbb Z\}
\subset\mathbb R_+^\times.
\]

Raising to any positive `beta` leaves that closure unchanged.

This two-generator calculation **does not prove** type `III_1`: a dense set of possible Radon–Nikodym values need not belong to the measurable ratio set, because ratio-set membership requires recurrence on arbitrary positive-measure sets. Neshveyev's prime-ideal/adelic argument supplies exactly that hard ergodic step. The calculation is only an adversarial control showing that topological modular closure itself is too coarse to retain deep all-prime or zero-divisor information.

## 4. The factor classification is not analytic continuation of `zeta`

The parameter `beta` in the KMS theorem is a real inverse temperature. Type `III_1` is an operator-algebraic property of the KMS state's GNS von Neumann algebra. It does not define a holomorphic function of complex `s`, extend the Euler product, or evaluate `zeta(beta)` where the Gibbs trace diverges.

In particular,

\[
M_{1/2}\text{ is type }III_1
\]

and

\[
r(M_{1/2})\setminus\{0\}=\mathbb R_+^\times
\]

contain no assertion about `zeta(1/2+it)`, its zero divisor, the functional equation, or Weil positivity. There is no legitimate continuation step from

\[
\operatorname{Tr}(e^{-\beta H})=\zeta(\beta)
\qquad(\beta>1)
\]

to the high-temperature type-III factor that preserves the same scalar analytic meaning.

`PL-211` already exhibits this failure concretely for the canonical Möbius observable: at `beta=1/2` the finite-prime KMS observable tends to zero, while the analytically continued Gibbs scalar `1/zeta(1/2)^2` is finite and nonzero. `PL-212` gives a second information boundary: symmetry restoration projects the canonical finite cyclotomic equilibrium channel onto an elementary function in which the Riemann zeta denominator cancels.

The present finding is the factor-level counterpart. The operator-algebraic continuation is mathematically substantial, but its coarse modular invariant is constant throughout the interval and cannot be a critical-half selector.

## 5. Adversarial and novelty audit

A tempting interpretation is that type `III_1` is “maximally continuous,” so perhaps its modular spectrum can itself become Hilbert–Pólya data. Three controls block that inference.

First, the factor invariant has already quotiented away the temperature information: every `beta in (0,1]` gives the same type and full ratio set. Any statistic depending only on those invariants is therefore constant on the whole critical-temperature interval.

Second, dense modular scaling is not specific to the full rational-prime system. The `2,3` control already gives dense logarithmic scale. The genuinely nontrivial arithmetic theorem is that the adelic action realizes the full **measurable ratio set**, but once that theorem is compressed to the type-`III_1` label, the readout no longer identifies which prime arithmetic produced it.

Third, a type-`III_1` factor does not place a discrete self-adjoint spectrum at the ordinates of the Riemann zeros. A Hilbert–Pólya mechanism would still require a source-forced zero-sensitive operator plus a self-adjointness/positivity/localization theorem. None follows from factor type or full ratio set.

The decisive prior art is Neshveyev's theorem itself. A targeted search around Bost–Connes factor type, KMS modular structure, the critical temperature, and RH found the established type-`III_1` classification and richer arithmetic quantum-statistical constructions, but no theorem making `beta=1/2` a distinct Connes-type or ratio-set boundary. The line-specific content here is therefore a **negative/prior-art redirect**, not a novelty claim.

The matched-control lesson is readout-relative: any two systems whose relevant equilibrium factors are type `III_1` are indistinguishable by factor type alone, regardless of their finer arithmetic observables. A new proposal must identify exactly what extra operator/state data it retains before taking this coarse quotient.

## 6. Consequence for the Bost–Connes branch

The recent Bost–Connes findings now separate three different thresholds/information layers:

\[
\begin{array}{rcl}
\text{Gibbs trace / symmetry breaking} &:& \beta=1,\\
\text{square-free second-moment support} &:& \beta=1/2\ \text{but phase-blind},\\
\text{high-temperature factor type} &:& III_1\ \text{for all }0<\beta\le1.
\end{array}
\]

They should not be conflated. `PL-024` supplies the first line, `PL-211` the second, `PL-212` shows that canonical cyclotomic symmetry restoration removes the zeta-sensitive harmonic from the positive high-temperature equilibrium channel, and `PL-213` closes the coarse modular-factor escape.

A viable Bost–Connes-derived RH mechanism must therefore use **finer arithmetic data than factor type, ratio set, or modular-scale closure**. It must retain rational-prime/global-completion information that generic type-`III_1` classification forgets and then impose a zero-sensitive positivity, localization, totality, or spectral constraint that is not merely analytic continuation of a scalar Gibbs formula.

This negative does not rule out state-dependent relative modular operators, arithmetic correlations within the factor, endomotive/adelic observables, Connes' later adele-class trace formula, Weil positivity, or another source-forced target coupling. It only removes the claim that the canonical high-temperature modular **type/scale itself** supplies a new explanation of `Re(s)=1/2`.