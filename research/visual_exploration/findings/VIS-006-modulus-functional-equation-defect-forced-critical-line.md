# VIS-006 — Modulus-only functional-equation defects force the critical line for every Schwarz-symmetric input

## Claim

Let

`chi(s) = pi^(s-1/2) Gamma((1-s)/2) / Gamma(s/2)`

be the standard factor in the Riemann functional equation `zeta(s)=chi(s)zeta(1-s)`. Let `F` be any meromorphic function satisfying Schwarz symmetry

`F(conj(s)) = conj(F(s))`.

At points where `F(s)`, `F(1-s)`, and `chi(s)` are finite and nonzero, define the modulus-only functional-equation defect

`A_F(s) = log|F(s)| - log|chi(s) F(1-s)|`.

Then

`A_F(1-conj(s)) = -A_F(s)`.

Consequently,

`A_F(1/2+i t) = 0`

for every real `t` where the defect is defined, **whether or not `F` satisfies the Riemann functional equation**.

In particular, a heatmap of `A_F` has a forced critical-line nodal set for `F=1`, for every finite Euler product with positive real generators, for rational-prime truncations, and for Grosswald–Schnitzer-style deformed-generator truncations. A visually sharp trench at `Re(s)=1/2` in this observable is therefore a symmetry artifact, not evidence of arithmetic rigidity or zero localization.

**Evidence/status:** `CLASSICAL-IDENTITY + EXACT-DERIVED + NEGATIVE/OBSTRUCTION`.

No novelty is claimed for the Riemann functional-equation factor, Schwarz reflection, or the identities used below. The durable contribution is the explicit falsification control for visual RH research: taking absolute values destroys the phase information needed to distinguish a genuine functional equation from a generic reflection-symmetric input.

## Derivation

The chosen gamma factor has the two elementary symmetries

`chi(1-s) = 1/chi(s)`

and

`chi(conj(s)) = conj(chi(s))`

where both sides are defined. Hence

`|chi(1-conj(s))| = 1/|chi(s)|`.

Schwarz symmetry of `F` similarly gives

`|F(conj(s))| = |F(s)|`

and

`|F(1-conj(s))| = |F(1-s)|`.

Now evaluate the defect at the reflected point:

`A_F(1-conj(s))`

`= log|F(1-conj(s))| - log|chi(1-conj(s)) F(conj(s))|`

`= log|F(1-s)| + log|chi(s)| - log|F(s)|`

`= -A_F(s)`.

On the critical line `s=1/2+i t`, the reflection `1-conj(s)` equals `s`, so antisymmetry forces `A_F(s)=0`.

The result is independent of Euler products, primes, zeros, analytic continuation, or Hamburger's theorem. Those structures can affect the off-axis texture of the observable, but not its central nodal line.

## The trivial control already kills the visual inference

Take `F(s)=1`. It certainly satisfies Schwarz symmetry, so

`A_1(s) = -log|chi(s)|`

and therefore `A_1(1/2+i t)=0`.

But `F=1` does not satisfy the Riemann functional equation `F(s)=chi(s)F(1-s)` except at points where `chi(s)=1`. The full complex residual is simply

`1-chi(s)`,

which is generally nonzero on the critical line even though the modulus defect vanishes there.

Thus the implication

`modulus defect vanishes on Re(s)=1/2  =>  functional equation`

is false in the strongest possible matched control: no arithmetic input is needed to manufacture the apparent critical-line feature.

## Grosswald–Schnitzer control

`PL-125` records that Grosswald and Schnitzer may replace rational primes by generators `q_n` with `p_n <= q_n <= p_(n+1)` while preserving the continued zeta zero divisor in `Re(s)>0`. `PL-126` then shows that nontrivial **integer** deformations cannot also satisfy the full Riemann functional equation inside Hamburger's finite-order ordinary Dirichlet-series class.

The present result separates those two facts visually. For any finite positive-real generator set,

`F_q(s) = product_j (1-q_j^(-s))^(-1)`

has Schwarz symmetry because `log q_j` is real. Therefore its modulus defect has the same forced critical-line zero as the undeformed prime truncation even though the full functional equation is precisely the global structure that distinguishes zeta from the integer deformation in `PL-126`.

So a modulus heatmap cannot visualize the discriminator established by Hamburger rigidity. Any useful visualization of that discriminator must retain phase/complex information or incorporate additional coefficient/growth data.

Visualization: [[research/visual_exploration/visualizations/functional-equation-modulus-trench.md]].

## Computational audit

The retained visualization sampled `0.05 <= Re(s) <= 0.95`, `2 <= Im(s) <= 40` for three inputs: `F=1`, the first 30 prime Euler factors, and the integer admissible sequence beginning `2,4,6,8,12,...` obtained from `q_1=2`, `q_n=p_n+1` for `n>=2`.

The maximum numerical `|A_F(1/2+i t)|` over the sampled ordinates was below `5e-15` in every panel. The maximum defect in the exact antisymmetry check `A_F(s)+A_F(1-conj(s))` was below `1.5e-14`. These computations audit the renderer and formulas; the claim itself is the exact derivation above, not a numerical inference.

## Prior art and novelty assessment

The Riemann reflection formula and standard completed functional equation are classical. NIST DLMF §25.4 records the reflection formulas:

https://dlmf.nist.gov/25.4

Schwarz conjugation for the finite real-generator Euler products used here follows directly from `q^(-s)=exp(-s log q)` with real `log q`; no analytic-continuation premise is needed for that finite control.

`PL-125` and `PL-126` already contain the relevant Grosswald–Schnitzer and Hamburger literature audit. No claim is made that the antisymmetry identity itself is new. A focused search for a named “functional-equation modulus defect” did not reveal a standard research invariant that would justify a novelty claim. The value of the result is methodological and negative: it identifies an exact representation-induced critical-line feature that a visual researcher must subtract from any supposed arithmetic signal.

## Boundary conditions

The logarithmic defect is defined only where the displayed factors are finite and nonzero. At an actual zero or pole, one should work with a regularized/limiting formulation rather than subtracting divergent logarithms. This does not affect the finite Euler-product control used in the visualization, whose factor singularities lie off the sampled critical strip.

The theorem concerns **modulus-only** defects. It does not say that the complete functional equation is weak or visually useless. Indeed `PL-126` establishes the opposite inside Hamburger's class: the full complex self-duality plus ordinary Dirichlet-series/growth hypotheses rigidly identifies zeta. The obstruction here is exactly the information loss caused by replacing a complex relation with absolute values.

Nor does the result imply anything about RH. Functional-equation symmetry identifies a reflection axis but does not force all zeros onto it.

## Consequence for the research line

Treat any critical-line ridge, trench, sign flip, or nodal set obtained from a modulus comparison of `F(s)` with `chi(s)F(1-s)` as **baseline symmetry** until a residual survives this exact antisymmetry control.

For visual work on the Grosswald–Schnitzer/Hamburger boundary, the next informative observable must retain what `A_F` discards: phase, a complex reflection cocycle, coefficient rigidity, or a quantitative growth constraint. The associated Prime Lattice clue asks whether that missing information admits a scale-aware quantitative rigidity statement rather than merely the exact all-or-nothing Hamburger theorem.
