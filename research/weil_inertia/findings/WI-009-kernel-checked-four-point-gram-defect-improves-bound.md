# WI-009 — a kernel-checked four-point Gram-defect certificate raises the unconditional bound to 0.672847019766...

**Status:** `LITERATURE+DERIVED` for the external theorem and formal artifact; `EXACT-DERIVED` for the scope consequences relative to WI-001/WI-004/WI-008. The cited development is public, `sorry`-free at the advertised theorem surface, and its authors report an independent Palomar rebuild/kernel replay. This is not a claim of conventional peer review or priority.

## 1. Precise theorem now available

A public follow-up development in `teal-sea/zeta-lab`, built directly on the Alpöge--Furman/Anthropic formalization, proves an unconditional improvement over the Montgomery--Taylor value without introducing higher prime-side moments or Fourier support beyond the original bandwidth-one regime.

Write

\[
H_{\rm MT}
=
\frac32-\frac1{\sqrt2}\cot\!\frac1{\sqrt2}
=0.6725007036794116457\ldots.
\]

The four-point theorem in

```text
hunts/ainta_seven_point/lean-four-point/FourPoint/Main.lean
```

states, with no certificate hypothesis left open, that for every `epsilon>0` and all sufficiently large `T`,

\[
\left(
\frac{906250H_{\rm MT}-1085}{904171}-\varepsilon
\right)N(T,2T)
\le N_0^s(T,2T).
\]

Hence

\[
\boxed{
\liminf_{T\to\infty}
\frac{N_0^s(T,2T)}{N(T,2T)}
\ge
\frac{906250H_{\rm MT}-1085}{904171}
=0.6728470197666888276\ldots
}
\tag{1}
\]

This improves the Alpöge--Furman Montgomery--Taylor constant by

\[
3.46316087277\ldots\times10^{-4},
\]

or about `0.03463` percentage points.

The exact Lean theorem is `Zeta23Ext.Bridge.FourPoint.four_point_bound_ratio`. Its proof invokes the general `n_point_bound` at `n=4` and discharges the finite certificate internally through `four_point_cert`; there is no external numerical certificate assumption in the final theorem.

The public state-of-record for the development, compiled from revision `c02ad1a`, reports the n-point result as Palomar record `PALOMAR-2026-08-25-000005`, registered 25 August 2026. It says the pinned development was rebuilt in a sandbox and replayed through Lean's kernel and a second kernel, and explicitly distinguishes this mechanical verification from human peer review.

## 2. The mechanism is the rank--trace remainder, not a new prime moment

The starting point is the stability refinement first exposed in the public `ainta/zeta-simple-zeros` draft and subsequently formalized against the Anthropic development.

Let `V` have the simple-critical zero vectors as columns, put

\[
P=VV^*,\qquad M=V^*V,
\]

and let `Q` contain the remaining zero contribution, with at most `b` positive eigenvalues. Define

\[
\Psi(t)=
\begin{cases}
(t-1)^2,&0\le t\le2,\\
2t-3,&t\ge2.
\end{cases}
\]

Then the sharpened rank--trace inequality is

\[
\boxed{
\|P+Q\|_F^2
\ge
4\operatorname{tr}(P+Q)-3r-4b
+\operatorname{tr}\Psi(M).
}
\tag{2}
\]

The term

\[
\mathcal D(M):=\operatorname{tr}\Psi(M)\ge0
\]

is exactly the spectral defect discarded by the coarse rank--trace argument. After the same prime-side trace estimates and tail passage used for the Montgomery--Taylor theorem, the formal bridge yields

\[
\boxed{
N_0^s(T,2T)
\ge
H_{\rm MT}N(T,2T)
+\mathcal D(M^\circ)-o(N).
}
\tag{3}
\]

Thus any positive-density lower bound on the Gram defect gives an unconditional improvement while keeping the original arithmetic input unchanged.

The formal audit is especially useful here. In `Zeta23Ext/StableRankTrace.lean`, the profile `Psi` is identified with the upstream multiplicity-aware scalar function `gc 2` plus the constant `1`; the enhanced inequality is proved as a corollary of the already formalized upstream `rank_trace_mult`, rather than as an unrelated new linear-algebra skeleton. The tail passage and the uniform kernel limit are separately proved in the bridge files `S8.lean` and `S9.lean`.

## 3. Four consecutive simple zeros force a positive local defect

At the Montgomery--Taylor window, normalized simple-zero vectors have limiting overlap

\[
\langle v_\gamma,v_{\gamma'}\rangle
\to k(x_\gamma-x_{\gamma'}),
\]

where

\[
k(x)=\frac{K(x)}{K(0)},
\qquad
K(x)=\int_{-1/2}^{1/2}
\cos(\sqrt2\,t)\cos(2\pi xt)\,dt,
\]

and set `w(x)=k(x)^2`.

For four ordered simple critical zeros with three nonnegative normalized gaps `g_0,g_1,g_2`, the formal development writes the local functional exactly as

\[
\begin{aligned}
F_4(g_0,g_1,g_2)
={}&\frac{g_0+g_1+g_2}{2500}\\
&+\frac23\bigl(w(g_0)+w(g_1)+w(g_2)\bigr)\\
&+w(g_0+g_1)+w(g_1+g_2)\\
&+2w(g_0+g_1+g_2).
\end{aligned}
\tag{4}
\]

The finite part is not merely an external interval-arithmetic assertion. The Lean theorem `four_point_cert` proves

\[
\boxed{
F_4(g_0,g_1,g_2)\ge\frac{2310}{10^6}
\qquad(g_i\ge0)
}
\tag{5}
\]

inside the proof assistant. The generated package reduces the noncompact region by the positive span term, covers the remaining compact gap region by exact rational cell lemmas, and proves the box inequalities used by the universal statement.

With block size

\[
m=435,
\]

one has

\[
\frac{2310}{10^6}(435-3)=0.99792<1,
\]

which is the block-cap condition required by the general n-point bridge. Substituting (5) into that bridge gives exactly (1).

## 4. Why this escapes WI-001 without contradicting its barrier

WI-001 showed that the first two **aggregate spectral moments** at bandwidth one admit explicit extremizers, and that those data alone cannot force the simple-critical proportion far beyond the current range. The four-point theorem does not manufacture a new value of

\[
\operatorname{tr}G^k
\]

from the primes. Instead it refuses to forget the fact that the positive part associated with simple critical zeros is a Gram matrix of a very specific translation/Gabor family.

The abstract two-moment extremizer can make the rank contribution look as if the simple-zero vectors were mutually orthogonal. But actual vectors from the Montgomery--Taylor kernel cannot realize that local orthogonality pattern for every short run of consecutive zeros. The defect `D(M)` measures this mismatch, and the four-point certificate proves that a positive amount of mismatch must recur globally.

Therefore the correct scope statement is

\[
\boxed{
\text{two aggregate moments are insufficient}
\;\not\Rightarrow\;
\text{all bandwidth-one zero-side structure is exhausted}.
}
\]

The remaining room below the Alpöge--Furman bandwidth-one ceiling can be attacked using structured Gram information already present in the same compression.

## 5. Relation to WI-004: the remainder is now productive

WI-004 derived an explicit positive remainder in the rank--trace inequality and used it mainly to rigidify near-extremizers. The formal follow-up shows a stronger use of the same philosophy: one component of that slack can be forced to have positive density from the geometry of the **simple-zero Gram matrix itself**.

Schematically,

\[
\text{rank--trace equality}
\Rightarrow
M\approx I
\Rightarrow
\text{simple-zero vectors locally almost orthogonal},
\]

while the kernel certificate proves that repeated local configurations of actual consecutive simple zeros cannot satisfy the last condition with zero cost. Thus the remainder is not only a diagnostic of what equality would require; it can be converted into an unconditional numerical gain.

This materially redirects the line: before seeking new prime moments, every positive term thrown away in the existing zero-side decomposition should be tested for a **local realizability obstruction** under the exact Montgomery--Taylor kernel.

## 6. Why this does not break the screening obstruction of WI-005--WI-007

The result does not distinguish

\[
\text{double zero on the line}
\quad\text{from}\quad
\text{screened simple off-line pair}.
\]

WI-005--WI-007 concern the exceptional contribution `Q` and show that, at bandwidth one, critical-lattice aggregation can erase horizontal depth and make those two exceptional populations matrix-equivalent at the relevant scale.

The four-point improvement acts elsewhere: it studies the internal geometry of `P`, the simple-critical contribution that we are trying to lower-bound. It proves that an abstract extremizer cannot pack the already-certified simple zeros with zero Gram defect. The bookkeeping of the complement may remain blind to whether its mass is in doubles or off-line pairs.

So both statements can hold simultaneously:

1. bandwidth-one compression cannot identify the **type** of exceptional zero responsible for the complement;
2. bandwidth-one Gram geometry can nevertheless force **more total simple-critical zeros** than the coarse rank--trace moments alone certify.

This distinction is essential for future work.

## 7. Relation to WI-008: a third escape from the higher-moment tradeoff

WI-008 ruled out the recipe

\[
\text{shorten bandwidth}
\to
\text{buy }\operatorname{tr}G^k
\to
\text{use the same shortened matrix as rank carrier}.
\]

The four-point theorem stays at full bandwidth `lambda=1`, retains the order-`N` rank carrier, and uses only the already established prime-side first/second trace estimates. The extra information is zero-side and local, not a higher arithmetic moment.

Thus the viable routes are now at least three genuinely different classes:

- new arithmetic information, such as support beyond one or higher prime correlations;
- joint/auxiliary compressions or a different operator architecture;
- **stability/local-realizability certificates inside the existing full-bandwidth Gram geometry**, now known to produce an unconditional gain.

The third route is no longer speculative.

## 8. Prior art, verification status, and boundaries

The mathematical chain has several provenance layers that must not be collapsed.

- Alpöge--Furman/Anthropic supply the full-bandwidth Weil compression, zero decomposition, prime-side trace estimates, and original rank--trace theorem.
- The public `ainta/zeta-simple-zeros` draft isolates the stability-enhanced spectral defect and gives seven-point computer-assisted certificates, including a claimed `0.673008527927...` theorem. That larger value is not used here as established evidence merely because its external interval verifier runs.
- `teal-sea/zeta-lab` formalizes the stability bridge against the Anthropic Lean code and supplies the four-point certificate *inside Lean*, yielding the smaller but substantially stronger-evidence value `0.672847019766...`.
- The zeta-lab state-of-record reports Palomar registration `PALOMAR-2026-08-25-000005` and an independent rebuild/kernel replay. This is strong mechanical verification, but explicitly not human peer review.
- Still larger public figures around `0.6730--0.6734` use external finite certificates, retuned windows, or additional candidate bridges. They remain separate `NEEDS-AUDIT` objects unless their entire theorem interface is similarly discharged.

No novelty claim is made here for the stability inequality, the Gabor kernel, convex pinching, or n-point block assembly. The durable Mathia contribution is the scope update: **there is now a formally checked unconditional escape from the 0.6725007 baseline that uses local Gram rigidity rather than new prime-side moments.**

## 9. Research consequence

The next high-value target is not merely to increase `n` in an expensive finite certificate. The important structural question is what is the strongest lower bound on

\[
\frac{\mathcal D(M^\circ)}{N}
\]

that can be forced analytically from the one-dimensional ordered-zero geometry and the exact kernel `k`, and what extremal point process minimizes that defect.

A useful candidate theorem would replace finite `n`-point box searches by a global variational or transfer-operator statement of the form

\[
\mathcal D(M^\circ)
\ge
c\,N_0^s-d\,N-o(N)
\]

with explicit optimal or near-optimal `c,d`. Such a theorem would stay inside the already verified bandwidth-one arithmetic regime while potentially capturing much more of the gap between `0.672847...` and the known information-class ceiling.

Conversely, a rigorous extremal construction showing that local Gram-defect certificates saturate below some constant would be equally valuable: it would identify exactly when genuinely new prime-side information becomes unavoidable.