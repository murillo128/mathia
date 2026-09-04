# XF-024 — span-normalized finite-block shape energies have exterior collision-positive spikes

**Status:** `EXACT-DERIVED` + `NEGATIVE/OBSTRUCTION` + `STRUCTURAL/BOUNDARY`. XF-021--XF-023 rule out broad centered quadratic/convex localization schemes because a collapsing gap can expose a positive `1/epsilon` boundary pole. A natural remaining escape from XF-018 is to avoid subtracting a mean altogether and instead normalize a finite block by its own physical span, turning the block into a scale-free shape variable. This includes coefficient-of-variation energies, entropies of normalized gaps, and other compact projective shape scores.

That finite-block escape still fails at the universal level. Let

\[
F:(0,\infty)^N\to\mathbb R
\]

be any `C^1` functional of a consecutive block of `N>=2` gaps. If there is a positive block configuration at which the derivative with respect to the rightmost gap is negative,

\[
\partial_NF<0,
\]

then placing a collapsing exterior gap `epsilon` immediately to the right gives the exact leading law

\[
\boxed{
\frac{d}{dt}F(g_1,\ldots,g_N)
=-\frac{2}{\epsilon}\,\partial_NF(g_1,\ldots,g_N)+O(1)
\longrightarrow +\infty.
}
\]

The same statement holds at the left edge with `\partial_1F`.

Consequently, every smooth finite-block **shape detector** that genuinely penalizes a one-edge compression has an exterior-collision witness. In particular, if `F` is scale invariant and the equal-gap ray is a strict local minimum in shape space, then some arbitrarily small compression of an edge gap has `\partial_NF<0`, so the positive spike is unavoidable. The obstruction therefore applies to the most direct span-normalized replacement for block variance, not merely to additive convex entropies or finite-range quadratic stencils.

For the canonical normalized quadratic shape energy

\[
\mathcal C_N(g)
:=
\frac{N\sum_{i=1}^N g_i^2}{\left(\sum_{i=1}^N g_i\right)^2}-1,
\]

which is nonnegative and vanishes exactly on equal gaps, the witness can be written explicitly. At

\[
g_1=\cdots=g_{N-1}=h,
\qquad
g_N=(1-\delta)h,
\qquad 0<\delta<1,
\]

one has

\[
\partial_N\mathcal C_N
=-\frac{2N(N-1)\delta}{h(N-\delta)^3}<0.
\]

If the next exterior gap is `epsilon`, then

\[
\boxed{
\mathcal C_N'
=
\frac{4N(N-1)\delta}{h(N-\delta)^3}\frac1\epsilon
+O(1)
\longrightarrow +\infty.
}
\]

Thus dividing by the block span does not cure the mean-removal problem left by XF-018--XF-020. The surviving route must be genuinely noncompact, configuration-dependent in a way that supplies compensating dynamics, or based on an exact signed flux cancellation across multiple scales rather than a standalone compact shape energy.

## 1. Universal exterior-collision law for a finite block functional

Work on an ordered real-simple configuration in the regime where XF-014 gives the exact gap equation

\[
g_i'
=2\sum_{k\ne i}c_{ik}(g_k-g_i),
\qquad
c_{ik}=c_{ki}>0.
\tag{1}
\]

Take a finite block

\[
I=\{1,\ldots,N\}
\]

with fixed positive gaps `g_1,...,g_N`, and put the first gap outside the block on the right equal to

\[
g_{N+1}=\epsilon\downarrow0.
\tag{2}
\]

Keep the remaining nearby gaps fixed and positive. For the adjacent pair `(N,N+1)`, XF-018's exact adjacent identity gives

\[
c_{N,N+1}
=\frac1{g_N\epsilon}.
\tag{3}
\]

Therefore its contribution to the velocity of the block-edge gap is

\[
2c_{N,N+1}(\epsilon-g_N)
=
\frac{2(\epsilon-g_N)}{g_N\epsilon}
=-\frac2\epsilon+\frac2{g_N}.
\tag{4}
\]

Every other interaction entering `g_N'` remains `O(1)` as `\epsilon\to0`, because both denominator spans stay bounded away from zero. For every interior block gap `g_i`, `i<N`, even the interaction with `g_{N+1}` is `O(1)`: at least the fixed positive span through `g_N` separates the two gap cells. Hence

\[
\boxed{
g_N'=-\frac2\epsilon+O(1),}
\tag{5}
\]

while

\[
\boxed{g_i'=O(1)\qquad(1\le i<N).}
\tag{6}
\]

For any `C^1` finite-block functional `F`, the chain rule now gives

\[
\begin{aligned}
F'
&=\sum_{i=1}^N\partial_iF\,g_i'\\
&=-\frac2\epsilon\,\partial_NF+O(1).
\end{aligned}
\tag{7}
\]

Thus

\[
\boxed{
\partial_NF<0
\quad\Longrightarrow\quad
F'\to+\infty
}
\tag{8}
\]

under a collapsing gap immediately outside the support. Reflecting the configuration gives the identical left-edge law

\[
F'=-\frac2\epsilon\,\partial_1F+O(1).
\tag{9}
\]

This is the finite-block obstruction in its most economical form: the collapsing exterior gap does not need to lie inside the energy. It drives the **edge gap of the observed block** downward at speed `2/epsilon`, so any energy that wants that edge gap to increase has a positive singular derivative.

## 2. Strict shape sensitivity forces the bad derivative

The preceding identity by itself is only a sign test. To connect it to mean removal, suppose now that `F` is intended to measure the shape of the block independently of its overall scale. Assume

\[
F(\lambda g)=F(g)
\qquad(\lambda>0),
\tag{10}
\]

and that the equal-gap ray is a strict local minimum in shape space. Concretely, for some `h>0`, define the one-edge compression path

\[
\gamma(s)
=(h,\ldots,h,(1-s)h),
\qquad 0\le s\ll1.
\tag{11}
\]

Strict local shape minimality implies

\[
F(\gamma(s))>F(\gamma(0))
\tag{12}
\]

for all sufficiently small `s>0`.

Let

\[
f(s):=F(\gamma(s)).
\]

For any sufficiently small `s_1>0` satisfying (12), the mean-value theorem gives an `s_*\in(0,s_1)` with

\[
f'(s_*)>0.
\tag{13}
\]

But

\[
f'(s)
=-h\,\partial_NF(\gamma(s)),
\tag{14}
\]

so

\[
\boxed{
\partial_NF(\gamma(s_*))<0.
}
\tag{15}
\]

Combining (15) with (7) proves:

\[
\boxed{
\begin{array}{c}
\text{finite block} + C^1 + \text{genuine edge-compression sensitivity}\\[2mm]
\Longrightarrow\\[2mm]
\text{an exterior collision produces a positive }1/\epsilon\text{ spike.}
\end{array}
}
\tag{16}
\]

Permutation symmetry is not needed for the local lemma, but any symmetric scale-free shape energy with a strict minimum at the arithmetic shape automatically satisfies the same edge-compression hypothesis at either endpoint.

The scale-invariance assumption is likewise not needed for (7). Its role is to identify the class relevant to the proposed span-normalized mean removal: `F` depends only on ratios such as

\[
p_i=\frac{g_i}{\sum_jg_j},
\tag{17}
\]

or on equivalent finite-block projective coordinates, rather than on the absolute local spacing.

## 3. Explicit failure of normalized quadratic variance

The simplest projective shape energy is

\[
\mathcal C_N(g)
=
\frac{NQ}{S^2}-1,
\qquad
Q:=\sum_{i=1}^Ng_i^2,
\qquad
S:=\sum_{i=1}^Ng_i.
\tag{18}
\]

By Cauchy--Schwarz,

\[
\mathcal C_N\ge0,
\tag{19}
\]

with equality exactly when all `N` gaps are equal. It is the squared coefficient of variation up to a conventional normalization and is exactly what one obtains by dividing the block variance by the square of the block mean/span.

Differentiate (18):

\[
\boxed{
\partial_j\mathcal C_N
=
\frac{2N(g_jS-Q)}{S^3}.
}
\tag{20}
\]

Take

\[
g_1=\cdots=g_{N-1}=h,
\qquad
g_N=(1-\delta)h,
\qquad0<\delta<1.
\tag{21}
\]

Then

\[
S=h(N-\delta)
\tag{22}
\]

and

\[
Q=h^2\left[(N-1)+(1-\delta)^2\right].
\tag{23}
\]

A direct simplification gives

\[
g_NS-Q
=-h^2\delta(N-1),
\tag{24}
\]

hence

\[
\boxed{
\partial_N\mathcal C_N
=-\frac{2N(N-1)\delta}{h(N-\delta)^3}<0.
}
\tag{25}
\]

Substituting into (7),

\[
\boxed{
\mathcal C_N'
=
\frac{4N(N-1)\delta}{h(N-\delta)^3}\frac1\epsilon
+O(1).
}
\tag{26}
\]

This witness can be taken arbitrarily close to the arithmetic lattice by taking `delta` arbitrarily small before sending `epsilon` to zero. The problem is therefore not a large-amplitude distortion of the core. A nearly equilibrated finite block can still acquire an arbitrarily large positive shape-energy derivative from a sufficiently tight collision immediately outside it.

Equation (26) also shows why merely **dividing by the span** is not qualitatively safer than subtracting the mean. In the uncentered square of XF-018 the boundary derivative is positive, so the same exterior collision contributes a negative singular term. Once the energy is converted into a true shape detector, a compressed edge must have negative restoring derivative somewhere, and the sign of the singular boundary flux reverses.

## 4. Relation to XF-021--XF-023

XF-021 treats additive centered convex entropies. Convexity forces a negative derivative below the preferred spacing, so an exterior collision produces a positive pole. XF-024 removes the additive and convex hypotheses: the only property needed is that the final **finite-block shape functional** has negative derivative at some compressed edge state.

XF-022 rules out finite-range translation-invariant quadratic overlap by examining the discrete Laplacian of the energy gradient at an **interior** collapsing gap. XF-023 rules out fixed summable weighted variances because a collapsing gap probes negative discrete curvature of the taper. The present result is complementary: it applies even if the mean-removal functional is nonlinear and scale-free, provided it remains a standalone compact block shape score.

In particular, the following apparent repairs are all inside the obstruction whenever they are `C^1` and genuinely detect an edge compression:

- block variance divided by the squared block mean or span;
- smooth divergences/entropies of the normalized proportions `p_i=g_i/S` with a strict minimum at `p_i=1/N`;
- smooth symmetric functions of finitely many gap ratios whose equal-gap shape is a strict local minimum.

The theorem does **not** say that every finite cross-ratio appearing in the program is bad. XF-018's `w_{ik}` is a collision-safe **interaction coefficient**, not a standalone compact shape Lyapunov with an arithmetic-shape minimum. The distinction between a safe carrier and a mean-removing energy remains essential.

## 5. Matched-control and source boundary

The obstruction is again universal for ordered logarithmic-repulsion gap dynamics. It does not prove that an actual high Xi zero block realizes the adversarial geometry (21) together with an arbitrarily small neighboring exterior gap. A genuinely Xi-specific theorem excluding that configuration could defeat the witness.

For the line's required matched-control test, however, the geometry is realizable exactly. Take a sufficiently long finite real-rooted polynomial with consecutive positive root gaps equal to the prescribed block values, followed by the exterior gap `epsilon`, and keep all other nearby gaps fixed positive. The backward-heat root ODE has the same adjacent logarithmic-repulsion singularity. The edge gap therefore has the leading velocity (5), while all remaining root interactions are bounded as `epsilon\to0`.

Hence no inequality asserting a universal upper Lyapunov law for such a compact shape functional can follow from the positive-conductance gap equation alone. Any successful Xi argument must add information not shared by these matched polynomial controls.

The finding also stays entirely inside the real-simple regime. It studies the approach `epsilon\downarrow0` from positive gaps and does not apply the ordered gap ODE through the actual collision time.

## 6. Prior art and novelty boundary

The chain-rule principle that a singular boundary velocity can defeat a local Lyapunov function is elementary, and scale-normalized shape variables are standard throughout dynamical systems and interacting-particle work. The broad log-gas/Dyson/Calogero literature also contains many global convexity and relaxation arguments. A targeted search around normalized spacings, gap-ratio Lyapunovs, and log-gas shape energies did not identify a theorem whose mathematical content is the finite-block Xi/log-repulsion boundary law (7) together with the strict-shape-minimum corollary (16). Absence from that search is not treated as novelty evidence.

No external theorem is load-bearing. The only dynamical input is the exact Xi gap equation already source-anchored through Rodgers--Tao in XF-014. The durable contribution is the classification of another proposed mean-removal escape: **compact span normalization does not remove the adjacent-collision obstruction; it converts it into the sign of the block-edge shape derivative.** `SOURCES.md` therefore requires no new entry.

## 7. Consequence for `xi_flow`

After XF-021--XF-024, the broad-buffer program should not spend further effort replacing block variance by another smooth fixed finite-block shape score merely because that score is nonlinear, ratio-based, or scale invariant. If the score genuinely regards equal spacing as locally optimal and detects compression of an edge gap, a sufficiently small collision just outside the block forces a positive `1/epsilon` derivative.

The remaining mean-removal route must avoid having a final artificial edge with ordinary restoring sensitivity. Plausible survivors are genuinely noncompact/global functionals, adaptive weights whose own time derivative cancels the exterior pole, or multiscale signed flux identities in which boundary terms cancel before any compact shape energy is formed. Xi-specific spacing information could also rescue a scale-dependent construction by proving that the external collision scale cannot outrun the relevant localization scale. Those possibilities lie outside the theorem and are now the sharper frontier left by the collision-safe cross-ratio carrier of XF-018--XF-020.