# MC-469 — Empty-vector sieve component survives small-outer-cell pruning

**Status:** `LITERATURE+DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

A concrete modern upper-linear-sieve decomposition shows that the next coefficient-mass test after `MC-467`--`MC-468` cannot be closed by support pruning alone.

In Jared Duker Lichtman's modified linear sieve, the auxiliary rough-block weights are

\[
\lambda_{(D_1,\ldots,D_r)}(d)
=
\mathbf 1_{d=p_1\cdots p_r}
\mathbf 1_{D_j<p_j\le D_j^{1+\tau}\ \forall j},
\tag{1}
\]

and the factorable components are

\[
\lambda^{(r)}_{(D_1,\ldots,D_r)}
=
\lambda_{(D_1,\ldots,D_r)}*\lambda^{(r)},
\tag{2}
\]

where `lambda^(r)` is the upper or lower beta-sieve weight according to the parity of `r`. The complete modified weight is a finite signed sum of these components,

\[
\widetilde\lambda^*
=
\sum_{0\le r\le \varepsilon^{-2}}
\sum_{(D_1,\ldots,D_r)\in\mathcal D_r^*}
\frac{(-1)^r}{\gamma(D_1,\ldots,D_r)}
\lambda^{(r)}_{(D_1,\ldots,D_r)}.
\tag{3}
\]

The paper explicitly includes `r=0`, the empty vector. At `r=0`, `(1)` has no prime-block variables, so

\[
\lambda_{()}=\delta_1.
\tag{4}
\]

Because zero is even, `lambda^(0)` is the upper beta-sieve side, and therefore the empty-vector component is

\[
\lambda^{(0)}_{()}
=
\delta_1*\lambda^{(0)}
=
\lambda^{(0)}.
\tag{5}
\]

Thus the concrete finite decomposition contains a component with a legitimate staged split

\[
\alpha=\delta_1,
\qquad
\beta=\lambda^{(0)}.
\tag{6}
\]

For the `MC-458` source-frame staging, this component fixes the outer factor at the identity. Hence the paired outer variables are `r=r'=1`, and the geometric parameters of `MC-463`--`MC-467` become

\[
R=[r,r']=1,
\qquad
T=\frac{r'}{(h,r')}=1.
\tag{7}
\]

So the support-shrinkage mechanism of `MC-467` supplies **no growing outer-scale suppression at all** for this component. The necessary bulk gate

\[
T<\frac{4N}{pR}
\tag{8}
\]

reduces here to the scale condition `1<4N/p`; there is no power of an outer factor to exploit. Likewise, the root-scale vacuity observation of `MC-468` cannot remove `(6)`: the outer factor is already the Dirichlet identity.

This is a narrow but decisive obstruction to one version of the current clue. In this concrete sieve construction, the statement

> the surviving small-`r'`/small-lcm cells have too little componentwise coefficient mass

cannot be established merely by showing that every nontrivial rough-block component has large support. There is an unavoidable **empty-vector base component** concentrated at the minimal outer cell before recombination.

The result does **not** give a lower bound for the fully recombined coefficient `widetilde lambda^*`: different signed components in `(3)` may cancel after recombination. It says instead that any proof which handles the finite components separately, or applies a triangle/positive bound before such cancellation is retained, must explicitly pay the `r=0` base component. To beat the source-frame tariff on that component, the proof must use the residual beta-sieve amplitude, cross-component interference retained before positivity, or a separate endpoint/oscillatory mechanism. Support geometry alone cannot do it.

No Möbius bound, character-sum improvement, prime-distribution exponent, or RH consequence follows.

## 1. The empty-vector component is forced by the published decomposition

Lichtman, *A modification of the linear sieve, and the count of twin primes*, Algebra & Number Theory **19** (2025), 1--37, equations (5-14)--(5-16), defines the rough-block indicator `(1)`, its convolution with the parity-dependent beta-sieve weight `(2)`, and the finite signed decomposition `(3)`. The same section later treats `r=0` explicitly as “the empty vector.”

For an empty vector, the product `p_1\cdots p_r` is the empty product `1`. Therefore `(1)` reduces exactly to the Dirichlet identity sequence `delta_1`; no asymptotic argument or interpretation is involved. Substitution into `(2)` gives `(5)`.

This is precisely the sort of construction-specific information that `MC-468` required. `MC-468` showed that generic well-factorability cannot provide an anti-concentration law. The present finding does not infer anything from generic factorability: it opens the actual finite decomposition and reads off one exact component from its defining formula.

## 2. Nonempty components do obey an explicit rough-block support filter

The same formula `(1)` gives useful information in the opposite direction for `r>=1`. Every nonempty rough-block component is supported on an outer block

\[
a=p_1\cdots p_r,
\qquad
D_j<p_j\le D_j^{1+\tau},
\tag{9}
\]

so necessarily

\[
a> D_1\cdots D_r.
\tag{10}
\]

Consequently, if the `MC-467` surviving region imposes an outer-factor cutoff `a<=Y`, every nonempty vector with

\[
D_1\cdots D_r\ge Y
\tag{11}
\]

is eliminated before any character estimate. This is the legitimate construction-specific support pruning that the clue was asking for.

But `(10)`--`(11)` produce a **dichotomy**, not a complete closure:

- nonempty rough-block components can be filtered by the product of their prescribed prime bins;
- the empty-vector component has `a=1` and survives every positive small-outer cutoff.

Therefore the correct next coefficient accounting is not one undifferentiated “small-cell mass” calculation. It must split the decomposition at `r=0` versus `r>=1` from the outset.

## 3. Consequence for the staged source-frame route

Take the empty-vector component and stage it as in `(6)`. In the notation of `MC-458`,

\[
w(m)
=
\sum_{r\mid m}\alpha_r B_\beta(m/r)
=
B_{\lambda^{(0)}}(m),
\tag{12}
\]

because `alpha=delta_1`. The outer progression geometry then has no nontrivial factor scale. Equations `(7)` are exact, so the `MC-467` attempt to couple growing outer support to shrinking source intervals has already reached its endpoint: there is no growing outer support in this component.

What remains inside the staged kernel is exactly the object that the earlier frontier had postponed,

\[
B_{\lambda^{(0)}}(C_{s_0}+r_1s_0j),
\tag{13}
\]

with the corresponding reduced coefficient and source shift. A power gain, if any, must now come from arithmetic or oscillatory structure of this residual beta-sieve divisor sum, from coherent interaction with other components before positive closure, or from a separately justified endpoint mechanism.

This sharpens `MC-453`. That finding proved that boundedly many factorable components cannot create a polynomial gain merely by being split and then squared separately. `MC-469` identifies a concrete reason the current small-cell pruning also cannot make all of those component costs disappear: one published factorable upper-sieve decomposition contains a base component sitting exactly at the minimal outer cell.

It also sharpens `MC-468`. The abstract class-level objection there said that factorability does not force spreading. Here the actual construction is stronger: one component is not merely *allowed* to concentrate at the identity; it is exactly the empty-vector upper-sieve component of the decomposition.

## 4. Prior-art and novelty boundary

The decomposition `(1)`--`(3)`, its programmable factorability, and the explicit `r=0` empty-vector case are Lichtman's sieve construction, not new mathematics. The observation that the empty product makes `lambda_()` equal to `delta_1` is immediate Dirichlet-convolution algebra and carries no novelty claim.

The durable result is the transfer to the current Möbius frontier: when this concrete construction is inserted into the `MC-458` staging, the empty-vector component lands at `R=T=1`. Therefore a componentwise support-pruning strategy cannot establish that all surviving small outer cells have negligible mass. That exact obstruction was not supplied by the generic well-factorability no-go of `MC-468`.

A targeted prior-art check on 22 September 2026 confirmed the relevant formulas and the explicit empty-vector case in the published Algebra & Number Theory paper. No claim is made that every Rosser--Iwaniec, beta-sieve, or well-factorable decomposition has the identical finite-component organization.

## Boundaries and falsification tests

- **This is construction-specific.** The claim applies to the Lichtman decomposition above. A different upper-sieve representation may organize its components differently and must be checked from its own formula.
- **No lower bound on the recombined weight.** Equation `(3)` is a signed sum. Other components can cancel the empty-vector contribution after recombination. The obstruction applies when the proof separates components, uses triangle inequalities, or closes positively before controlling that interference.
- **No claim that the base residual is large.** `B_{lambda^(0)}` may admit useful cancellation or a stronger estimate. The finding only shows that outer support pruning does not provide it.
- **The bulk gate is not asserted automatically.** For `(7)`, the `MC-467` necessary condition becomes `1<4N/p`. Whether a particular parameter regime satisfies that inequality is separate; the point is that no growing outer-factor power appears.
- **Nonempty-bin pruning remains live.** Equations `(10)`--`(11)` are genuine construction-specific support information and should be used to price all `r>=1` pieces.
- **Cross-component interference remains live.** A proof retaining the signed combination `(3)` through an oscillatory transform lies outside the componentwise obstruction and must estimate those cross terms explicitly.
- **No RH input or conclusion.** The argument uses only the published finite sieve decomposition and exact source-frame bookkeeping from the canonical finding chain.

## Consequence for the research line

The accepted staged-source clue should now bifurcate its coefficient test. First isolate the `r=0` empty-vector component and send it directly to the residual-amplitude/endpoint analysis; do not expect `MC-467` support shrinkage to remove it. For `r>=1`, use the exact bin product `D_1\cdots D_r` to discard components whose rough-block support cannot enter the surviving small-outer region, and only then price their coefficient mass.

If the surviving proof still handles the finite decomposition componentwise, the base component is a mandatory tariff. If instead it attempts to cancel the base component against nonempty pieces, that cancellation must be kept before triangle inequalities or positive closure and becomes a distinct, explicitly testable mechanism.