---
finding_id: NB-274
prefix: NB
title: Disjoint Ford bands kill the sqrt-K target-anchor branch for frequency-tight targets
status: proposed
verdict: pending
reviewed: false
created: 2026-09-21
updated: 2026-09-21
authors:
  - OpenAI
origin:
  kind: research-watch
  ref: nyman_beurling
depends_on:
  - NB-269
  - NB-272
  - NB-273
supersedes: []
superseded_by: []
related_findings:
  - NB-271
---

# Disjoint Ford bands kill the sqrt-K target-anchor branch for frequency-tight targets

## Claim

`NB-272` reduced every target-side obstruction in a resolved anchored section to two quantities: the unconstrained section defect `delta_K` and the Euler-anchor mismatch

\[
\mu_K=1-e_K^*R_K^{-1}b_K.
\]

`NB-273` then showed that an order-one floor coming from the second term forces the unconstrained coefficient vector

\[
a_K:=R_K^{-1}b_K
\]

to export a fixed amount of `ell^2` mass beyond every fixed shell prefix. The unresolved issue was whether the actual target pairings can produce that coefficient escape.

For the **exact full-line resolved Ford channel of `NB-269`**, the answer is no for every target family that remains frequency-tight in the normalized center variable. The reason is stronger than uniform conditioning: the shell atoms occupy pairwise disjoint Fourier cells, so the Gram is diagonal exactly and Bessel/Cauchy transfers target-frequency tightness directly to coefficient-tail tightness.

More precisely, let

\[
s_{K,j}(z)
=\int_a^b
\phi(u)A_{K,j}(u)e^{-i(j+u)z}\,du,
\qquad 0\le j<K,
\tag{1}
\]

with

\[
0<a<b<1,
\qquad
\operatorname{diam}(\operatorname{supp}\phi)<1,
\tag{2}
\]

and assume the live resolved family has uniformly nondegenerate shell norms

\[
0<q_-
\le
q_{K,j}:=\|s_{K,j}\|_2^2
\le
q_+<\infty.
\tag{3}
\]

The shallow matched packet of `NB-269` satisfies (3) because its channel amplitudes are uniformly bounded above and below on `supp phi`.

Let

\[
S_Kc=\sum_{j=0}^{K-1}c_js_{K,j},
\qquad
R_K=S_K^*S_K,
\qquad
b_{K,j}=\langle s_{K,j},g_K\rangle,
\tag{4}
\]

for a uniformly bounded target family `g_K in L^2(R_z)`. If its center-frequency tails are uniformly tight,

\[
\boxed{
\lim_{L\to\infty}
\sup_K
\|\mathbf 1_{[L,\infty)}\widehat g_K\|_2
=0,
}
\tag{5}
\]

then the unconstrained coefficients satisfy

\[
\boxed{
\lim_{L\to\infty}
\sup_K
\sum_{j=L}^{K-1}|(R_K^{-1}b_K)_j|^2
=0.
}
\tag{6}
\]

Consequently

\[
\boxed{
\frac{e_K^*R_K^{-1}b_K}{\sqrt K}\longrightarrow0,
\qquad
\mu_K=o(\sqrt K),
}
\tag{7}
\]

and the anchor penalty in the exact target identity of `NB-272` vanishes:

\[
\boxed{
\frac{|1-e_K^*R_K^{-1}b_K|^2}
{e_K^*R_K^{-1}e_K}
=o(1).
}
\tag{8}
\]

Thus, inside this exact disjoint-band channel,

\[
\boxed{
\inf_{e_K^*c=1}\|g_K-S_Kc\|_2^2
=
\delta_K^2+o(1).
}
\tag{9}
\]

For a fixed target `g` in the normalized center Hilbert space, condition (5) is automatic. Therefore the `sqrt(K)` target-anchor branch of `NB-272` cannot survive in the `NB-269` full-line resolved channel for a fixed `L^2` target. Any order-one target-side floor there must come from the section defect itself.

There is also a quantitative converse. If `delta_K -> 0` but the anchored residual stays above a fixed `eta>0`, then the target family cannot be frequency-tight: for every fixed `L`, along the obstructing subsequence it must retain an order-one amount of `L^2` mass at center frequencies beyond `L`. Quantitatively,

\[
\boxed{
\limsup_{K\to\infty}
\|\mathbf 1_{[L,\infty)}\widehat g_K\|_2^2
\gtrsim_{a,b}
\frac{q_-}{q_+}\,\eta,
}
\tag{10}
\]

up to the harmless fixed shift locating the first shell band.

The remaining issue is therefore no longer an abstract possibility that `R_K^{-1}` spreads a benign target vector into a `sqrt(K)` anchor mismatch. In the exactly resolved Ford channel it cannot do so. To keep that branch alive, the **transformed target itself must migrate to shell frequencies tending to infinity**, or one must leave the exact disjoint-band channel.

## 1. Exact disjoint-band geometry

Use the unitary Fourier transform in the center variable `z`. From (1),

\[
\operatorname{supp}\widehat s_{K,j}
\subset
E_j:=j+\operatorname{supp}\phi.
\tag{11}
\]

Because `diam(supp phi)<1`, the sets `E_j` are pairwise disjoint. Hence

\[
\langle s_{K,j},s_{K,k}\rangle=0
\qquad(j\ne k),
\tag{12}
\]

and therefore

\[
\boxed{
R_K
=\operatorname{diag}(q_{K,0},\ldots,q_{K,K-1}).
}
\tag{13}
\]

This is precisely the full-line Plancherel diagonalization used in `NB-269`, now viewed as a finite synthesis map rather than only as an energy identity.

The unconstrained least-squares coefficient vector is consequently explicit:

\[
\boxed{
a_{K,j}
=(R_K^{-1}b_K)_j
=\frac{\langle s_{K,j},g_K\rangle}{q_{K,j}}.
}
\tag{14}
\]

Since `s_{K,j}` lies entirely in `E_j`, only the corresponding target-frequency cell contributes:

\[
\langle s_{K,j},g_K\rangle
=
\langle s_{K,j},P_{E_j}g_K\rangle.
\tag{15}
\]

Cauchy-Schwarz gives

\[
|b_{K,j}|^2
\le
q_{K,j}\,\|P_{E_j}g_K\|_2^2,
\tag{16}
\]

so

\[
\boxed{
|a_{K,j}|^2
\le
\frac1{q_-}\|P_{E_j}g_K\|_2^2.
}
\tag{17}
\]

The disjointness now matters a second time. Summing (17) over all shells `j>=L`,

\[
\sum_{j=L}^{K-1}|a_{K,j}|^2
\le
\frac1{q_-}
\sum_{j=L}^{K-1}\|P_{E_j}g_K\|_2^2.
\tag{18}
\]

Because

\[
E_j\subset[j+a,j+b],
\]

the union of the cells with `j>=L` lies inside `[L+a,infinity)`. Their mutual orthogonality therefore yields

\[
\boxed{
\sum_{j=L}^{K-1}|a_{K,j}|^2
\le
\frac1{q_-}
\|\mathbf 1_{[L+a,\infty)}\widehat g_K\|_2^2.
}
\tag{19}
\]

Equation (19) is the main bridge. `NB-273` required coefficient-tail tightness but did not identify a mechanism producing it. In the exact `NB-269` channel, target-frequency tightness produces it immediately and uniformly in the rank.

For a single fixed `g in L^2`,

\[
\|\mathbf 1_{[L,\infty)}\widehat g\|_2\to0
\]

by square-integrability, so no extra regularity or pointwise Fourier decay is required.

## 2. The normalized anchor pairing must vanish

The same geometry gives a quantitative version of the compactness argument in `NB-273`. First, (17) summed over every shell gives

\[
\|a_K\|_2^2
\le
\frac1{q_-}\|g_K\|_2^2.
\tag{20}
\]

Assume

\[
\sup_K\|g_K\|_2\le G.
\tag{21}
\]

Fix a shell cutoff `L<K` and split the anchor sum into a prefix and a tail. By Cauchy-Schwarz,

\[
\frac1{\sqrt K}
\left|\sum_{j=0}^{L-1}a_{K,j}\right|
\le
\frac{G}{\sqrt{q_-}}
\sqrt{\frac LK}.
\tag{22}
\]

For the tail, use (19):

\[
\frac1{\sqrt K}
\left|\sum_{j=L}^{K-1}a_{K,j}\right|
\le
\left(\sum_{j=L}^{K-1}|a_{K,j}|^2\right)^{1/2}
\le
\frac1{\sqrt{q_-}}
\|\mathbf 1_{[L+a,\infty)}\widehat g_K\|_2.
\tag{23}
\]

Combining,

\[
\boxed{
\frac{|e_K^*a_K|}{\sqrt K}
\le
\frac{G}{\sqrt{q_-}}\sqrt{\frac LK}
+
\frac1{\sqrt{q_-}}
\|\mathbf 1_{[L+a,\infty)}\widehat g_K\|_2.
}
\tag{24}
\]

If the target family satisfies (5), first let `K -> infinity` with `L` fixed and then let `L -> infinity`. Equation (24) gives

\[
\boxed{
\frac{e_K^*a_K}{\sqrt K}\to0.
}
\tag{25}
\]

Since

\[
\mu_K=1-e_K^*a_K,
\]

we obtain `mu_K=o(sqrt(K))`.

The exact diagonal Gram also gives

\[
\frac K{q_+}
\le
D_K:=e_K^*R_K^{-1}e_K
=\sum_{j=0}^{K-1}\frac1{q_{K,j}}
\le
\frac K{q_-}.
\tag{26}
\]

Therefore

\[
0\le
\frac{|\mu_K|^2}{D_K}
\le
q_+\frac{|\mu_K|^2}{K}
\to0.
\tag{27}
\]

Substituting (27) into the exact target identity from `NB-272`,

\[
\inf_{e_K^*c=1}\|g_K-S_Kc\|_2^2
=
\delta_K^2+
\frac{|\mu_K|^2}{D_K},
\tag{28}
\]

proves (9).

The conclusion is stronger than saying that the target does not create a new Gram matrix, which was the content of `NB-272`. Here the remaining affine target-anchor term itself is forced to vanish under a concrete and natural Hilbert-space condition.

## 3. Converse: an anchor floor forces target-frequency escape

The previous implication can be reversed into a necessary condition for any surviving anchor obstruction in this exact channel.

Assume along a subsequence that

\[
\delta_K^2\to0
\tag{29}
\]

but

\[
\inf_{e_K^*c=1}\|g_K-S_Kc\|_2^2
\ge\eta>0.
\tag{30}
\]

Then for all sufficiently large `K` on that subsequence, the anchor penalty in (28) is at least `eta/2`. Using the lower bound in (26),

\[
|\mu_K|^2
\ge
\frac\eta2D_K
\ge
\frac{\eta}{2q_+}K.
\tag{31}
\]

Hence

\[
\liminf
\frac{|e_K^*a_K|}{\sqrt K}
\ge
\sqrt{\frac{\eta}{2q_+}}.
\tag{32}
\]

Fix `L`. The prefix term in (24) tends to zero as `K -> infinity`. Therefore (24) and (32) force

\[
\limsup_{K\to\infty}
\|\mathbf 1_{[L+a,\infty)}\widehat g_K\|_2
\ge
\sqrt{\frac{q_-\eta}{2q_+}}.
\tag{33}
\]

Equivalently,

\[
\boxed{
\limsup_{K\to\infty}
\|\mathbf 1_{[L+a,\infty)}\widehat g_K\|_2^2
\ge
\frac{q_-}{2q_+}\eta
}
\tag{34}
\]

for every fixed `L`.

Thus the coefficient escape found abstractly in `NB-273` has a direct destination-space meaning in the `NB-269` channel: **a target-anchor floor requires the target itself to export a fixed amount of energy to arbitrarily remote resolved center-frequency cells.**

This is only a necessary condition. High-frequency target energy need not align with the one-dimensional source direction inside each cell, so target-frequency escape does not by itself imply an anchor obstruction.

## 4. Relation to the preceding route

`NB-269` established the exact Fourier-cell separation of the full-line resolved Ford channel and used it to show that the uniform carrier can have only `Theta(1/K)` Hardy energy while retaining an order-one center spike. `NB-271` then showed that a new positive Gram repair would need relative strength `Omega(K)`. `NB-272` removed target cross terms as a source of such a Gram and isolated `delta_K` and `mu_K`. Finally, `NB-273` showed that a `sqrt(K)` mismatch requires the coefficients `a_K=R_K^{-1}b_K` to lose tail compactness.

The present finding closes that last mismatch branch **inside the exact disjoint-band full-line model** whenever the target family is frequency-tight. In that model the inverse Gram is not a mysterious dense operator: it is diagonal. Consequently it cannot manufacture coefficient escape from a target whose own center-frequency mass stays tight.

There are two useful consequences.

First, a fixed `L^2` target cannot maintain an order-one anchor floor in this channel once the unconstrained section defect vanishes. The anchor penalty is automatically `o(1)`.

Second, if the canonical Nyman target after the same rank-coupled center normalization turns out to be a moving family `g_K`, the exact question is now whether it satisfies the uniform frequency-tightness condition (5). Proving that property would eliminate the target-anchor branch without any direct inverse-section analysis. Failing it would identify a genuinely new phenomenon: the normalized target itself would have to drift to Ford shell frequencies of increasing index.

This also sharpens the next computation. It is not enough to quote the canonical discrete-generator pairing `-log n/n` from `NB-001`: the shell index in `NB-269` is a resolved center-frequency index, not the original Nyman generator number. The needed object is the target after the **same legal Hardy projection, demodulation, and `z=H(t-t_0)` rescaling** used to define (1). Its frequency tails, rather than an unrelated generator-coordinate decay law, decide whether the anchor branch survives.

## Adversarial review

The strongest failure mode is a coordinate mismatch. A fixed canonical target before Ford rescaling need not remain a fixed or uniformly frequency-tight target after the `K`-dependent projection, demodulation, and center rescaling. The theorem therefore does **not** assert that the actual Nyman target satisfies (5). Establishing the transformed target family and checking its frequency tightness is the next required target-aware calculation.

The second limitation is geometric. Exact orthogonality holds for the **full-line** `NB-269` channel because the bands `j+supp phi` are disjoint. A hard-window restriction in `z` convolves frequency and destroys exact shell orthogonality. The finding does not replace the hard-window analysis with a false diagonal statement. It says only that when the exact full-line channel is used as the source Hilbert geometry in the `NB-272` target identity, the anchor mismatch cannot survive a frequency-tight target.

Third, the lower shell-norm bound `q_->0` is essential. It holds for the shallow matched packet regime used in `NB-269`, where the channel amplitudes have a uniform positive lower bound, but it need not hold for an arbitrary zero configuration or arbitrary translated depth cutoff. If `q_{K,j}` degenerates, division by the Gram diagonal can amplify remote target components and (19) can fail.

Fourth, the section defect remains completely open. Even with pairwise disjoint frequency cells, each shell contributes only the particular direction `s_{K,j}` inside its cell. A target may retain order-one energy orthogonal to those directions. Equation (9) says precisely that after the anchor term disappears, this is the only target-side obstruction left in the exact channel; it does not show `delta_K -> 0`.

Finally, the shallow Ford packet remains a compatibility control rather than a statement about the actual zeta zero set. Nothing here proves or disproves RH, and no claim is made that the complete Nyman residual is exhausted by the `NB-269` channel.

## Prior-art check

A targeted search after deriving the criterion found the expected general Hilbert-space ingredients—orthogonal Fourier cells, Bessel bounds, and finite-section Gram analysis—and the recent Beurling-Nyman work of Carvill (`arXiv:2510.18132`) on polynomial off-diagonal Gram decay and block compressibility. That literature concerns the original/multiscale Beurling-Nyman generator geometry and does not supply the rank-coupled statement above linking the exact `NB-269` disjoint Ford cells to the `sqrt(K)` target-anchor alternative of `NB-272`/`NB-273`.

No external theorem is load-bearing: the proof is the direct projection estimate (16)--(19) plus the exact anchored identity already derived internally. `SOURCES.md` therefore does not need a new dependency.

## What is established

Within the exact full-line resolved Ford synthesis of `NB-269`, with uniformly nondegenerate shell norms, any uniformly bounded target family whose normalized center-frequency tails are uniformly tight has uniformly tight unconstrained coefficient tails. Its normalized Euler-anchor pairing is `o(1)` at the `sqrt(K)` scale, so the anchor penalty in `NB-272` vanishes.

Conversely, if the section defect tends to zero while an order-one anchored floor persists, the target family must keep a fixed positive amount of `L^2` energy beyond every fixed center-frequency cutoff. Coefficient escape in `NB-273` therefore becomes actual target-frequency escape in this model.

## What is not established

The transformed canonical Nyman target has not yet been written explicitly in the `NB-269` center variable, so its uniform frequency tightness is not established here. The finding also does not estimate the section defect `delta_K`, does not extend exact diagonalization to a fixed hard window, and does not rule out an additional source-source component of the full Nyman norm outside the resolved channel.

## Open seam

The next discriminating calculation is now concrete: carry the canonical Nyman target through the same legal Hardy projection, demodulation, and rank-coupled rescaling that produced the resolved current (1), and determine whether the resulting target family `g_K` satisfies

\[
\lim_{L\to\infty}
\sup_K
\|\mathbf 1_{[L,\infty)}\widehat g_K\|_2=0.
\]

If it does, the target-anchor branch is closed in the exact resolved channel and only the section defect or genuinely new source-source geometry can carry an obstruction. If it does not, the escaping target-frequency profile itself becomes the next object to quantify.