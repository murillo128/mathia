# AF-024 — Unconstrained smooth Weil tests can program local separable source geometry

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`

## Claim

Fix `A>0` and distinct visible generator logarithms

\[
0<c_1<\cdots<c_N<A.
\]

Assume they are multiplicatively nonresonant inside the visible window:

\[
mc_j\neq c_k
\]

for every `j,k` and every integer `m\ge2` with `mc_j<A`.

For a real test function `F\in C_c^\infty(0,A)`, write its exact one-generator Weil response as

\[
G_F(t)
=
\sum_{m\ge1} t e^{-mt/2}F(mt).
\]

Then the unconstrained smooth test class has the following local programming property.

1. **Arbitrary local one-generator germs can be realized independently at the selected centers.** For any finite collection of smooth germs
   \[
   H_1,\ldots,H_N
   \]
   at `c_1,\ldots,c_N`, there is a test
   \[
   F\in C_c^\infty(0,A)
   \]
   and pairwise disjoint neighborhoods `U_j\ni c_j` such that
   \[
   \boxed{
   G_F(t)=H_j(t)
   \qquad(t\in U_j).
   }
   \]

2. **Finite vector-valued test maps can therefore program arbitrary separable local geometry.** Given `d` retained tests and arbitrary smooth germs `H_{ij}` at the same centers, one can choose
   \[
   F_1,\ldots,F_d\in C_c^\infty(0,A)
   \]
   so that on a small ordered deformation chamber around
   \[
   c=(c_1,\ldots,c_N)
   \]
   the exact generalized-prime test map has the form
   \[
   \boxed{
   \Psi_i(\ell_1,\ldots,\ell_N)
   =C_{B,i}+\sum_{j=1}^N H_{ij}(\ell_j),
   \qquad 1\le i\le d,
   }
   \]
   where `B` is any fixed generalized-prime background.

3. **A single nonnegative smooth test can singularly isolate any such finite source point.** Choosing
   \[
   H_j(t)=(t-c_j)^2
   \]
   yields a nonnegative `F\in C_c^\infty(0,A)` for which
   \[
   \boxed{
   \Psi_F(\ell)-\Psi_F(c)
   =\sum_{j=1}^N(\ell_j-c_j)^2
   }
   \]
   throughout a sufficiently small ordered chamber. Consequently
   \[
   \Psi_F(\ell)=\Psi_F(c)
   \quad\Longleftrightarrow\quad
   \ell=c
   \]
   there, even though the destination is only one real scalar and `N` may be arbitrarily large.

4. At this isolated point,
   \[
   D\Psi_F(c)=0,
   \qquad
   D^2\Psi_F(c)=2I_N.
   \]
   Thus the singular escape left by AF-023 is genuine: first-order rank can vanish completely while second-order structure gives exact point identification.

5. For a rational-prime center
   \[
   c_j=\log p_j,
   \]
   the nonresonance hypothesis is automatic for distinct primes. Therefore **any finite visible block of ordinary rational primes can be made an isolated exact finite-test point by a source-tuned unconstrained smooth test**.

This is not evidence that such a test carries intrinsic rational-prime structure. It proves the opposite audit point: in the ambient `C_c^\infty` test category, pointwise fidelity and higher-order singular isolation can be manufactured around an arbitrary chosen finite source. A finite-test route acquires arithmetic meaning only after the admissible test class is constrained independently of the source strongly enough that this programming freedom is no longer available.

## Exact local response programming

The key observation is that nonresonance allows the first-power response near each selected generator to be separated from every higher-power image of every selected generator.

Because the set of visible multiples

\[
\{mc_j:1\le j\le N,\ m\ge1,\ mc_j<A\}
\]

is finite and no higher multiple `mc_j`, `m\ge2`, equals a selected center `c_k`, choose pairwise disjoint open intervals

\[
V_j\Subset(0,A),
\qquad c_j\in V_j,
\]

small enough that

\[
\boxed{
 mV_j\cap V_k=\varnothing
 }
\]

for every `j,k` and every integer `m\ge2` for which `mV_j` can meet `(0,A)`.

Shrink to intervals

\[
U_j\Subset V_j
\]

and choose smooth cutoffs

\[
0\le\chi_j\le1,
\qquad
\chi_j\equiv1\text{ on }U_j,
\qquad
\operatorname{supp}\chi_j\Subset V_j.
\]

Represent the prescribed germ `H_j` by a smooth function on `V_j`. Define

\[
F(x)
=
\sum_{j=1}^N
\chi_j(x)\frac{e^{x/2}}{x}H_j(x).
\]

Since every `V_j` is compactly contained in `(0,A)`, the factor `1/x` is harmless and

\[
F\in C_c^\infty(0,A).
\]

Now fix `t\in U_j`. The first-power term is

\[
t e^{-t/2}F(t)=H_j(t).
\]

For every `m\ge2`, the separation condition gives

\[
mt\notin\bigcup_k\operatorname{supp}\chi_k,
\]

so

\[
F(mt)=0.
\]

Hence the full prime-power response, with no approximation or omitted term, is

\[
G_F(t)
=
\sum_{m\ge1}t e^{-mt/2}F(mt)
=H_j(t).
\]

This proves the one-test statement. Applying the same construction independently to each row `i` realizes any prescribed family `H_{ij}` and proves the finite-vector statement.

The theorem is stronger than finite jet interpolation at the centers. It realizes the complete prescribed smooth germ on a neighborhood of each selected coordinate. The only geometry it cannot program by this mechanism is nonseparable cross-coordinate coupling: additivity of the Weil prime-power sum still forces the local map to be a sum of one-generator responses.

## Exact singular isolation by one scalar test

Take

\[
H_j(t)=(t-c_j)^2.
\]

With nonnegative cutoffs, the constructed test satisfies

\[
F(x)\ge0.
\]

Let `B` be any fixed generalized-prime background not containing the selected movable copies, and define

\[
Q_\ell
=B\sqcup\{e^{\ell_1},\ldots,e^{\ell_N}\}
\]

for `\ell_j\in U_j`. The retained scalar is

\[
W_{Q_\ell}(F)
=C_B+\sum_{j=1}^N G_F(\ell_j)
=C_B+\sum_{j=1}^N(\ell_j-c_j)^2.
\]

At the center,

\[
W_{Q_c}(F)=C_B.
\]

Therefore

\[
W_{Q_\ell}(F)=W_{Q_c}(F)
\]

if and only if every square vanishes. The exact level-set fiber through the center is locally the singleton

\[
\{c\}.
\]

The Jacobian is identically zero at the center because every first derivative vanishes, while the Hessian is positive definite. Thus AF-023's rank-drop requirement is not merely a logical loophole: the same finite-Weil-test model admits source points that are maximally singular at first order and nevertheless exactly isolated at second order.

Nothing about this construction is prime-specific. The same recipe isolates any finite visible nonresonant generalized-prime configuration. For ordinary primes, nonresonance follows from

\[
m\log p_j=\log p_k
\Longrightarrow
p_j^m=p_k,
\]

which is impossible for distinct rational primes and `m\ge2`.

## What this changes about finite-test fidelity

AF-022 and AF-023 established that finite-dimensional exact test data generically have large generalized-prime fibers and that every regular rational-prime center lies on a positive-dimensional exact same-test fiber when more source coordinates than outputs are free.

One might then try to rescue finite-test point fidelity by proving that the rational-prime point is an exceptional singular source. The present result shows why **singularity alone is not explanatory structure**.

In the unconstrained smooth category, one can prescribe the local response germs themselves. In particular, one can force

\[
\Psi(\ell)-\Psi(c)=\|\ell-c\|_2^2
\]

with a single scalar observable. The isolated singular geometry can therefore be inserted by choosing the test around the source rather than discovered as a consequence of an independently defined arithmetic mechanism.

This separates three increasingly strong claims:

\[
\text{finite-test noninjectivity in neighborhoods}
\]

from

\[
\text{pointwise isolation at a singular source}
\]

from

\[
\boxed{
\text{intrinsic pointwise fidelity under an independently constrained observable class}.
}
\]

Only the third has the right form for an arithmetic discriminator. The second can be manufactured for arbitrary controls.

This also sharpens the role of positivity. The isolating example may be chosen with `F\ge0`, so mere time-domain nonnegativity does not prevent source-tuned singular identification. Stronger constraints such as Fourier positivity, Paley--Wiener relations, evenness, fixed transform families, operator origin, or another source-independent admissibility principle must be audited in their own category.

## Prior art and novelty assessment

The ingredients are classical.

- Smooth localization by compactly supported bump functions and finite-set jet/germ interpolation are standard differential-topology/Whitney-extension techniques. The proof above is more elementary than the full Whitney extension theorem because the selected neighborhoods are disjoint and the desired local functions can simply be patched with cutoffs.
- Prosper Dovonon, Alastair R. Hall, and Frank Kleibergen, **“Inference in second-order identified models,”** *Journal of Econometrics* 218(2) (2020), 346--372, DOI `10.1016/j.jeconom.2020.04.020`, is direct neighboring prior art for the principle that nonlinear moment systems may be globally/locally identified at second order even when first-order Jacobian identification fails.
- Enrique Sentana, **“Finite underidentification,”** *Journal of Econometrics* 240(1) (2024), 105692, DOI `10.1016/j.jeconom.2024.105692`, studies nonlinear moment models in which isolated parameter values satisfy the moment conditions despite first-order underidentification.
- AF-023 already anchors the regular/singular boundary in the classical constant-rank theorem and modern singular-locus identifiability language.

No novelty is claimed for bump interpolation, rank-deficient higher-order identification, strict local minima, or singular moment-condition geometry.

A targeted literature search did not identify an established Beurling-prime theorem stating the exact local response-programming property above. That absence is not treated as proof of novelty. The Arithmetic Fidelity contribution is the exact specialization to the prime-power Weil response: **the ambient compactly supported smooth test class can independently program the local one-generator germs at any finite nonresonant block, and therefore can manufacture exact singular point fidelity with one scalar test.**

## Boundaries and failure modes

- The programming theorem uses the full unconstrained class `C_c^\infty(0,A)`. It does not automatically survive Fourier-support constraints, transform positivity, evenness, Paley--Wiener conditions, a fixed finite-dimensional test family, or tests generated intrinsically by another operator/geometric construction.
- The selected block is finite and visible: `c_j<A`. Invisible generators cannot be programmed through tests supported in `(0,A)`.
- Nonresonance is essential to the clean independent-localization proof. At resonant centers, a test value near one selected point can re-enter the response through a higher multiple of another coordinate, and the local germs become coupled.
- The theorem programs **separable** local maps of the form `sum_j H_{ij}(ell_j)`. It does not create arbitrary cross-coordinate interactions.
- The isolating test is deliberately source-tuned. Its existence proves that point isolation is too weak an audit criterion in the unconstrained test category; it does not propose this test as a natural RH observable.
- `F\ge0` in the quadratic example is only pointwise positivity of the test on log scale. No Fourier positivity or positive-definite-kernel property is claimed.
- Finite movement of generalized-prime generators preserves local finiteness and the exact prime-power construction, but this finding does not assert preservation of every stronger global Beurling counting asymptotic or analytic continuation property.
- The result concerns local source identification by finite exact test values. It says nothing about zeta-zero locations, multiplicity, simplicity, or RH.

## Decisive audit test

For any finite-test route that survives AF-023 by claiming singular pointwise rigidity:

1. identify the actual admissible test space, including every transform, positivity, symmetry, operator-origin, support, and source-independence constraint;
2. determine whether local bump/germ programming of the one-generator response remains possible at a finite nonresonant prime block;
3. if it does, test whether the claimed singular geometry can be reproduced around arbitrary matched generalized-prime centers by the same admissible construction;
4. if arbitrary centers can be isolated, do not treat pointwise isolation itself as rational-prime-specific evidence;
5. if the constrained test class forbids such programming, characterize the exact allowed jet/germ image and ask whether the rational-prime point is singular for a reason forced by that class rather than by source-dependent tuning;
6. only then study whether the surviving higher-order singularity is sufficient to isolate the prime point against the full matched control family.

The key new gate is therefore not merely

\[
D\Psi(c)\text{ singular?}
\]

but

\[
\boxed{
\text{is the singular higher-order geometry forced by the admissible category, or programmable from the chosen source?}
}
\]

## Consequence for the line

AF-023 forced every finite-test special-point escape into singular higher-order geometry. AF-024 now shows that the unconstrained smooth test category is too expressive for such singularity to carry intrinsic meaning: arbitrary finite nonresonant centers can be given prescribed separable local response germs, and a single nonnegative test can make any one of them an exact isolated quadratic minimum.

The finite-Weil-test frontier therefore moves from **whether singular isolation can occur** to **which source-independent admissibility constraints prevent arbitrary local response programming**.

The next useful classification target is the image of the local jet/germ map

\[
F\longmapsto
\bigl(G_F\text{ near }c_1,\ldots,G_F\text{ near }c_N\bigr)
\]

inside the actual constrained test categories used by explicit-formula, positivity, trace, or spectral mechanisms. Only restrictions that shrink this image for an intrinsic reason can turn exceptional singular fidelity into evidence about the arithmetic source rather than about the freedom used to choose the observable.