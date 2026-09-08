# PL-216 — The Bost–Connes temperature direction has infinite diagonal Fisher length throughout the high-temperature phase

## Claim

`PL-215` shows that distinct canonical Bost–Connes temperatures are globally disjoint whenever one inverse temperature lies in `0 < beta <= 1`. The same prime-product model gives a sharper **infinitesimal** obstruction: the canonical temperature direction is not an `L^2` tangent direction of the diagonal equilibrium measure anywhere in that whole high-temperature interval.

On the valuation coordinates of

\[
\mathcal R=\prod_p\mathbb Z_p,
\]

the canonical measure has independent geometric laws

\[
P_{\beta,p}(k)
=(1-p^{-\beta})p^{-k\beta},
\qquad k\ge0.
\]

Writing `x_p=p^(-beta)`, the local temperature score is

\[
S_{\beta,p}(k)
=\partial_\beta\log P_{\beta,p}(k)
=(\log p)\left(\frac{x_p}{1-x_p}-k\right),
\]

and therefore its local Fisher information is

\[
\boxed{
I_{\beta,p}
=\mathbb E_{\beta,p}|S_{\beta,p}|^2
=(\log p)^2\frac{p^{-\beta}}{(1-p^{-\beta})^2}.
}
\]

Consequently

\[
\boxed{
\sum_p I_{\beta,p}<\infty
\iff
\beta>1.
}
\]

In particular, for every `0 < beta <= 1`, including `beta=1/2`, the formal global score has infinite `L^2` norm. Thus the canonical family `beta -> mu_beta` does not possess a square-integrable diagonal temperature generator inside one high-temperature measure class. The obstruction changes at the thermodynamic threshold `beta=1`, not at the Riemann half.

There is also an exact local-deformation control. Replace the common temperature by prime-dependent perturbations `beta+epsilon_p`. In the tangent regime `|epsilon_p| log p` uniformly small, Kakutani's criterion gives

\[
\boxed{
\bigotimes_p P_{\beta+\epsilon_p,p}
\sim
\bigotimes_p P_{\beta,p}
\iff
\sum_p p^{-\beta}(\epsilon_p\log p)^2<\infty.
}
\]

Hence nontrivial same-measure-class diagonal deformations do exist, but they form a weighted square-summable cone of freely selectable local prime perturbations. Relative-density or commutative modular data built only from such a deformation records the chosen `epsilon_p`; it does not acquire an arithmetic compatibility law merely from equivalence of the product measures.

This closes a natural part of the same-sector escape left after `PL-215`: **neither differentiating the canonical temperature family at `beta=1/2` nor replacing it by an arbitrary equivalent primewise product perturbation supplies a source-forced RH selector**. A surviving Bost–Connes route must use genuinely non-diagonal same-sector data, a source-forced relation among prime channels, or a global trace/positivity mechanism not reducible to product-measure change of density.

**Evidence/status:** `HYBRID` (literature-backed Bost–Connes product measure plus exact derivation); `NEGATIVE/OBSTRUCTION`; `PRIOR-ART-AUDITED`; `NO-NOVELTY-CLAIM`.

## 1. Exact score and Fisher information on one prime coordinate

From `PL-215`, the valuation `K_p=v_p(a)` under the canonical diagonal `KMS_beta` measure has

\[
P_{\beta,p}(K_p=k)
=(1-x_p)x_p^k,
\qquad x_p=p^{-\beta}.
\]

Differentiate the log density:

\[
\begin{aligned}
\partial_\beta\log P_{\beta,p}(k)
&=\partial_\beta\log(1-p^{-\beta})-k\log p\\
&=(\log p)\frac{p^{-\beta}}{1-p^{-\beta}}-k\log p.
\end{aligned}
\]

The geometric law has

\[
\mathbb E K_p=\frac{x_p}{1-x_p},
\qquad
\operatorname{Var}(K_p)=\frac{x_p}{(1-x_p)^2}.
\]

Therefore the score has mean zero and

\[
I_{\beta,p}
=(\log p)^2\operatorname{Var}(K_p)
=(\log p)^2\frac{p^{-\beta}}{(1-p^{-\beta})^2}.
\]

Because the prime coordinates are independent, the squared `L^2` norm of a finite-prime score sum is the sum of the local Fisher informations. Thus an `L^2` limit of the canonical temperature score can exist only if

\[
\sum_p I_{\beta,p}<\infty.
\]

For large `p`, `(1-p^(-beta))^(-2)` is bounded above and below by positive constants, so convergence is equivalent to convergence of

\[
\sum_p (\log p)^2p^{-\beta}.
\]

If `beta>1`, this converges by comparison with the corresponding integer series. If `beta<=1`, then for all sufficiently large primes

\[
(\log p)^2p^{-\beta}\ge p^{-1},
\]

and Euler's divergence of `sum_p 1/p` gives divergence. Hence the threshold is exactly `beta=1`.

This is an `L^2` statement about the diagonal product measure. It is not an analytic continuation of the Gibbs partition function and it makes no statement about `zeta(beta+it)`.

## 2. The Hellinger expansion reproduces the same tangent threshold

The infinitesimal calculation is consistent with the exact Kakutani geometry already used globally in `PL-215`. For two geometric laws with

\[
x=p^{-\beta},
\qquad
y=p^{-(\beta+\epsilon)},
\]

the Hellinger affinity is

\[
h_p
=\frac{\sqrt{(1-x)(1-y)}}{1-\sqrt{xy}},
\]

and the exact identity is

\[
1-h_p^2
=\frac{(\sqrt{x}-\sqrt{y})^2}
{(1-\sqrt{xy})^2}.
\]

Put `u=epsilon log p`. Then `y=xe^(-u)` and

\[
(\sqrt{x}-\sqrt{y})^2
=x(1-e^{-u/2})^2.
\]

For `|u|` bounded by a sufficiently small fixed constant, elementary Taylor bounds give

\[
1-h_p\asymp p^{-\beta}u^2
=p^{-\beta}(\epsilon\log p)^2
\]

uniformly for all sufficiently large `p`. Finite exceptional primes do not affect product-measure equivalence. Kakutani's theorem therefore yields, for a prime-dependent perturbation satisfying the same local smallness condition,

\[
\bigotimes_p P_{\beta+\epsilon_p,p}
\sim
\bigotimes_pP_{\beta,p}
\iff
\sum_p p^{-\beta}(\epsilon_p\log p)^2<\infty.
\]

This is the prime-coordinate analogue of a Cameron–Martin tangent condition: equivalence is controlled by a weighted `ell^2` norm. No Gaussian structure is being claimed; the only input is the exact Hellinger affinity and Kakutani's classical product-measure theorem.

A constant perturbation `epsilon_p=delta` is not in this tangent cone for `beta<=1`. More strongly, `PL-215` already proves from the exact, non-infinitesimal affinity that `mu_beta` and `mu_(beta+delta)` are mutually singular whenever the two temperatures are distinct and one is at most `1`.

## 3. Why this narrows the same-sector modular route

After `PL-213` showed that the factor type is `III_1` throughout the high-temperature interval, `PL-215` ruled out comparing two distinct canonical temperatures as normal states in one canonical high-temperature factor. A possible repair would be to avoid a finite temperature jump and try to extract a **temperature derivative** at a fixed `beta`, hoping that an infinitesimal relative modular Hamiltonian retains more arithmetic information.

The Fisher calculation shows that the diagonal prime-product model does not support that repair in `L^2`. The finite-prime score operators have variance

\[
\sum_{p\le P}I_{\beta,p},
\]

which diverges as `P -> infinity` for every `beta<=1`. Thus the canonical global temperature direction already leaves the square-integrable tangent space before one asks whether its spectrum or determinant could contain zeta-zero information.

This does **not** prove that no distributional or unbounded infinitesimal object can be defined. It proves the narrower and falsifiable statement needed here: there is no square-integrable diagonal score furnishing a normal Cameron–Martin-like temperature tangent in the high-temperature prime-product representation.

## 4. Equivalent diagonal perturbations are available but are not rigid

The weighted condition

\[
\sum_p p^{-\beta}(\epsilon_p\log p)^2<\infty
\]

also shows why merely insisting on same-sector equivalence does not solve the problem. There are infinitely many nonzero primewise perturbations satisfying it, including every finitely supported perturbation and arbitrarily chosen sufficiently rapidly decaying tails.

For equivalent product measures the Radon–Nikodym density is the limit of the finite-prime density products. On the diagonal commutative algebra, the associated relative modular unitary is simply the appropriate power of that density. Its primewise logarithm is therefore built from the selected local perturbations `epsilon_p`.

Nothing in Kakutani equivalence relates the value chosen at one prime to another, forces the exact arithmetic weights `log p` to satisfy a new global identity, or couples the resulting density to the Riemann zero divisor. The situation matches the programmability controls `PL-208`--`PL-210`: regularity and same-sector implementability are admissibility conditions, not arithmetic rigidity.

A future positive construction could of course specify a particular `epsilon_p` by an independent arithmetic rule. It would then have to prove that the rule supplies a non-programmable trace, positivity, or localization identity and that the identity fails on matched arbitrary weighted-`ell^2` controls. The present result does not exclude that stronger possibility.

## 5. The critical half remains a different phenomenon

At `beta=1/2`,

\[
I_{1/2,p}
=(\log p)^2\frac{p^{-1/2}}{(1-p^{-1/2})^2},
\]

so the global Fisher sum diverges very strongly. But the same is true at `beta=1/3`, `2/3`, `1`, and every other high-temperature inverse temperature. There is no change of tangent geometry at `1/2`.

This keeps separate the distinct half-critical effect found in `PL-211`: the square-free/Möbius observable has a second-moment support threshold at `beta=1/2`. That observable threshold does not turn the surrounding equilibrium measure family into a differentiable same-sector thermal path. The two phenomena arise from different sums over the prime lattice and should not be conflated.

The currently established Bost–Connes boundaries are therefore consistent:

- ordinary Gibbs trace and symmetry breaking change at `beta=1`;
- canonical diagonal measure class changes at `beta=1`;
- the diagonal Fisher/tangent threshold is `beta=1`;
- high-temperature GNS factors remain type `III_1` throughout `0<beta<=1`;
- the `beta=1/2` square-free `L^2` threshold is observable-specific and does not become a thermal or modular phase boundary.

## 6. Prior-art and adversarial audit

The ingredients are classical. Neshveyev's adelic description supplies the canonical Bost–Connes product measures, and Kakutani's 1948 theorem supplies the equivalence/singularity criterion. `PL-215` already records both sources and derives the exact local Hellinger affinity. The present Fisher formula and weighted tangent criterion are exact consequences of that persisted product law; **no novelty claim is made**.

A targeted literature search around Bost–Connes KMS measures, Hellinger/Kakutani equivalence, temperature singularity, and Fisher information did not expose a theorem that should be claimed as a new RH mechanism. Absence of a search hit is not used as novelty evidence. The durable value is the line-specific negative: the most canonical infinitesimal repair of the cross-temperature obstruction also fails to produce a distinguished critical-half direction.

Several boundaries are essential.

First, infinite Fisher information does not forbid all unbounded, distributional, or noncommutative generators. It rules out the square-integrable **diagonal** temperature score.

Second, the weighted-`ell^2` criterion concerns primewise product perturbations of the canonical diagonal measure. The type-`III_1` Bost–Connes factor has many normal states not of this form; they are not classified here.

Third, equivalence of product measures is not being identified with quasi-equivalence of arbitrary full Bost–Connes representations. The claim about relative density is made on the diagonal product-measure sector, where Kakutani applies directly.

Fourth, no statement about analytic continuation, the functional equation, Weil positivity, or zeta-zero localization follows from the Fisher calculation. The real parameter `beta` remains an inverse temperature.

## Research consequence

The Bost–Connes branch should no longer treat the canonical temperature derivative at `beta=1/2` as a hidden same-sector modular observable. The diagonal product geometry has infinite Fisher length in that direction throughout the whole high-temperature phase. Same-measure-class primewise perturbations survive only after replacing the uniform temperature direction by a weighted square-summable local deformation, and that freedom is itself too programmable to count as arithmetic rigidity.

The live route is therefore narrower: use **genuinely non-diagonal same-sector arithmetic data** or a global trace/positivity construction that derives a relation among prime channels from the ordinary zeta problem rather than choosing that relation as a product-measure perturbation.
