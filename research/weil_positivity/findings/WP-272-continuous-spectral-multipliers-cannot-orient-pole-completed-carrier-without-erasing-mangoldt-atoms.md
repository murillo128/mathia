---
id: WP-272
title: Continuous spectral multipliers cannot orient the pole-completed critical carrier without erasing Mangoldt atoms
branch: weil_positivity
status: supported
kind: source-side-multiplier-obstruction
claim_strength: exact RH-independent local-measure no-go for continuous scalar filtering of the canonical pole completion
created: 2026-09-12
related: [WP-005, WP-039, WP-269, WP-270, WP-271]
prior_art:
  - Bochner--Schwartz positive-measure criterion
  - M. Shoeib and M. Torky, A Fourier-Multiplier Obstruction for the Zeta Weil Form, 2026
---

# WP-272 — Continuous spectral multipliers cannot orient the pole-completed critical carrier without erasing Mangoldt atoms

## Claim

`WP-270` and `WP-271` isolate the canonical source-side pole completion

\[
T_{\rm pole}
=\nu_{1/2}-\cosh(\xi/2)\,d\xi,
\qquad
\nu_{1/2}
=\frac12\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\bigl(\delta_{\log n}+\delta_{-\log n}\bigr).
\tag{1}
\]

`WP-271` closes finite-order conditional positivity, but leaves an apparently broader nonlocal escape: apply a smooth or continuous scalar spectral filter before reading positivity. This includes translation-invariant differential and pseudodifferential energies, Sobolev/fractional filters, convolution filters with continuous transfer function, and square filters `A^*A` whose spectral multiplier is `|m|^2`.

That route has an exact local obstruction. Let `q:R->R` be continuous. If the locally finite signed measure

\[
qT_{\rm pole}
\tag{2}
\]

is a positive Radon measure, then

\[
\boxed{
q(\pm\log n)=0
\quad\text{for every prime power }n=p^k.
}
\tag{3}
\]

So every continuous scalar multiplier that succeeds in making the pole-completed carrier positive necessarily **erases every Mangoldt atom**. In particular it cannot preserve, rescale positively, or geometrically read the finite Weil coefficients.

There is a sharper corollary for positive energies. If

\[
q(\xi)\ge0
\qquad(\xi\in\mathbb R),
\tag{4}
\]

then positivity of `qT_pole` forces

\[
\boxed{q\equiv0.}
\tag{5}
\]

Hence no nonzero continuous square multiplier `q=|m|^2` can convert the canonical pole completion into a positive spectral measure at all.

The proof is purely local, uses no zero data, and does not assume RH or temperedness. It therefore survives the category distinction of `WP-269`--`WP-271`: the obstruction already exists at the level of locally finite signed measures before one asks whether the resulting object belongs to distributions, Fourier hyperfunctions, or a larger exponential-growth category.

**Classification:** `EXACT-DERIVED + RH-INDEPENDENT + LOCAL-SIGN-SEPARATION + CONTINUOUS-MULTIPLIER-NO-GO + POSITIVE-SQUARE-FILTER-NO-GO + MATCHED-DISCONTINUOUS-CONTROL + PRIOR-ART-AUDITED + NOT-A-GENERAL-FOURIER-MULTIPLIER-NOVELTY-CLAIM`.

## 1. The arithmetic support is locally discrete and the pole background fills every gap

Write

\[
S
:=\{\pm\log(p^k):p\text{ prime},\ k\ge1\}.
\tag{6}
\]

Every compact interval meets `S` in only finitely many points, because a bounded logarithmic interval corresponds to a bounded range of positive integers. Thus `S` is a closed locally discrete subset of `R`, with no finite accumulation point. Its complement

\[
\mathbb R\setminus S
\tag{7}
\]

is open and dense.

On that complement the arithmetic part of (1) vanishes identically. Therefore

\[
\boxed{
T_{\rm pole}|_{\mathbb R\setminus S}
=-\cosh(\xi/2)\,d\xi,
}
\tag{8}
\]

and the density on the right is strictly negative everywhere.

At each `s in S`, by contrast, `T_pole` has a strictly positive atom

\[
a_s\delta_s,
\qquad a_s>0.
\tag{9}
\]

The continuous negative background and the positive arithmetic atoms therefore require opposite multiplier signs if one tries to orient (1) pointwise in spectral space.

## 2. Positivity on the gaps forces the continuous multiplier to be nonpositive there

Assume `qT_pole` is a positive Radon measure. Let `U` be any open interval whose closure is disjoint from `S`. Restricting (2) to `U` and using (8) gives

\[
(qT_{\rm pole})|_U
=-q(\xi)\cosh(\xi/2)\,d\xi.
\tag{10}
\]

A positive measure cannot have a negative absolutely continuous density. Since `cosh(ξ/2)>0`,

\[
q(\xi)\le0
\quad\text{for Lebesgue-a.e. }\xi\in U.
\tag{11}
\]

Continuity upgrades this to pointwise inequality. As `U` was arbitrary,

\[
\boxed{
q(\xi)\le0
\qquad(\xi\notin S).
}
\tag{12}
\]

This conclusion is stronger than the first-gap witness in `WP-271`: every atom-free spectral gap imposes the same orientation, and no finite-order or polynomial structure of the filter has been assumed.

## 3. Continuity then forces every arithmetic atom to vanish

Fix `s in S`. Positivity of the atomic part of `qT_pole` gives

\[
q(s)a_s\ge0.
\tag{13}
\]

Since `a_s>0`,

\[
q(s)\ge0.
\tag{14}
\]

But `S` is locally discrete, so there are points of `R\S` arbitrarily close to `s`. Equation (12) and continuity imply

\[
q(s)\le0.
\tag{15}
\]

Combining (14) and (15) yields

\[
\boxed{q(s)=0.}
\tag{16}
\]

Because `s` was arbitrary, (3) follows. In particular, any exact requirement such as

\[
q(\pm\log(p^k))=1
\tag{17}
\]

or merely `q(±log(p^k))>0` is incompatible with positivity of the filtered pole completion.

If `q>=0` globally, then (12) gives `q=0` on the dense complement of `S`; continuity gives `q=0` on `S` as well. This proves (5).

For a translation-invariant positive filter `A^*A` with continuous scalar symbol `m`, the spectral weight is

\[
q(\xi)=|m(\xi)|^2\ge0.
\tag{18}
\]

Thus the only way such a filter can make the source-side carrier positive is the trivial zero filter. Ordinary differential squares, fractional/Sobolev squares with continuous symbols, and continuous scalar pseudodifferential transfer functions are all special cases.

## 4. The obstruction is independent of the RH-dependent category descent

The result does not require `T_pole` to be tempered. Equation (1) is always a locally finite signed Radon measure: every compact interval sees finitely many Mangoldt atoms and a finite smooth pole mass. Multiplication by a continuous function is therefore locally well-defined regardless of the global growth class.

This separates the present obstruction from `WP-270`. If RH is false, `T_pole` fails to be tempered, but the local sign argument above is still valid. If RH is true, `T_pole` becomes tempered, but the same argument still says that no continuous scalar spectral multiplier can make it positive while retaining any arithmetic atom.

It also strengthens the particular conditional-positive obstruction of `WP-271`. Multiplication by `|xi|^{2s}` was one way to see that a finite-order conditional derivative cannot reverse the negative gap. Here **every** continuous nonnegative multiplier is excluded, including nonpolynomial and genuinely nonlocal ones, and even a sign-changing continuous multiplier must kill all arithmetic atoms if the output is positive.

## 5. Aggressive falsification: discontinuity can cheat, and that is the exact boundary

Continuity is load-bearing. If arbitrary bounded Borel multipliers are admitted, one can define the hand-picked selector

\[
q_{\rm cheat}(\xi)
=
\begin{cases}
+1,&\xi\in S,\\
-1,&\xi\notin S.
\end{cases}
\tag{19}
\]

Then, as a signed-measure multiplication,

\[
q_{\rm cheat}T_{\rm pole}
=\nu_{1/2}+\cosh(\xi/2)\,d\xi\ge0.
\tag{20}
\]

So there is no abstract impossibility of assigning the desired sign separately to the discrete and continuous pieces. The obstruction says that a **continuous geometric spectral response cannot do so**. The discontinuous control succeeds only by encoding the full prime-power support `S` into the filter itself, exactly the kind of hand-picked arithmetic selector excluded by the research mandate unless an independent Mathia construction forces it.

There is also a nontrivial continuous positive-output control that demonstrates the arithmetic loss sharply. Since `S` is closed, for example

\[
q(\xi)=-\operatorname{dist}(\xi,S)^2
\tag{21}
\]

is continuous, nonpositive, and vanishes on `S`. It gives

\[
qT_{\rm pole}
=\operatorname{dist}(\xi,S)^2\cosh(\xi/2)\,d\xi\ge0,
\tag{22}
\]

but every Mangoldt atom has disappeared. Thus (3) is sharp: continuous scalar filtering can obtain positivity only by discarding the arithmetic atomic sector.

The theorem does not cover operators that mix distinct spectral frequencies, matrix-valued/noncommutative filters whose positivity is not reducible to scalar multiplication, compressions or boundary maps, singular limits whose multiplier ceases to be continuous, or a source construction that changes the finite--archimedean carrier before (1) is formed. Those are genuine remaining escapes rather than hidden exceptions to the lemma.

## 6. Prior-art and novelty audit

The measure-theoretic sign argument itself is elementary and no novelty is claimed for it. The classical Bochner--Schwartz framework, already audited in `WP-269` and `WP-271`, supplies the surrounding principle that a translation-invariant positive covariance must have positive spectral measure. The new line-specific content is the exact application to the source-normalized carrier (1), where the positive arithmetic part is discrete and the independently forced pole background is strictly negative on its complement.

The closest direct multiplier prior art is Shoeib--Torky, *A Fourier-Multiplier Obstruction for the Zeta Weil Form* (2026), already recorded in `SOURCES.md` and used by `WP-005`. Their no-go concerns a fixed same-space **positive Gram multiplier form** for the full Weil functional: an absolutely continuous multiplier measure cannot equal the atomic zero-sampling measure that positivity would give under RH. The present statement is different in object and logic. It never invokes the zero-side representation or RH; instead it starts from the **source-side pole-completed signed measure** and proves that any continuous scalar filter making that measure positive must erase its positive Mangoldt atoms. It therefore closes a source-filter route left open after `WP-270`--`WP-271`, rather than reproving the same-space Weil-form theorem.

`WP-039` is also adjacent but distinct. It proves that the zero set of a translation-invariant Markov/Dirichlet symbol is a subgroup, so a nonnegative Markov symbol cannot itself have exact Mangoldt support on the arithmetic solenoid or prime torus. The present theorem assumes neither a Markov semigroup nor a conditionally negative-definite symbol. It concerns an arbitrary continuous scalar multiplier applied to the already assembled signed finite--pole carrier on the additive logarithmic line.

A directed literature search around Bochner--Schwartz positivity, continuous Fourier multipliers, and signed spectral measures recovered these classical frameworks and the Shoeib--Torky same-space obstruction, but no stronger theorem is needed for (3): the decisive step is simply positivity of a signed Radon measure on the open gaps plus continuity at the arithmetic atoms.

## Consequence

After `WP-269`--`WP-272`, a broad smooth-filter escape is closed. The critical source carrier may be hosted in an exponential-growth category, the canonical pole subtraction may descend to tempered distributions exactly on RH, and finite-order conditional positivity cannot repair its sign. Now, even allowing arbitrary continuous scalar spectral processing, positivity can be obtained only by deleting every finite arithmetic atom; a positive square filter can produce only the zero measure.

A surviving Mathia-native geometry therefore has to do something structurally stronger than scalar spectral reweighting. It must mix frequencies or sectors before the sign is read, derive a singular/discontinuous arithmetic boundary law from independent geometry, use a genuinely noncommutative or matrix-valued completion, or replace the pole-completed carrier itself by a different source-forced finite--archimedean object. Smooth translation-invariant filtering of `T_pole` cannot be the missing Weil positivity mechanism.