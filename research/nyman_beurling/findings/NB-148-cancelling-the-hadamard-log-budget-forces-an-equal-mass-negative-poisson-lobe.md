# NB-148 — Cancelling the Hadamard log budget forces an equal-mass negative Poisson lobe

**Status:** `EXACT-DERIVED + SOURCE-SPECIFIC + SIGNED-SAMPLING + POISSON-CONSERVATION + METHOD-OBSTRUCTION + NB-147-FRONTIER`.

`NB-146` and `NB-147` show that positive exterior Poisson sampling has exhausted its leading `Theta(log G)` occupancy budget. A natural next move is therefore to use signed combinations of exterior logarithmic-derivative samples so that the universal `(1/2) log G` term cancels. This finding isolates the exact tax paid by that cancellation: the resulting zero-side Poisson kernel has zero vertical mass, so any positive target lobe must export an equal amount of negative mass elsewhere. In particular, cancelling the Hadamard background and retaining global zero-side positivity are incompatible unless the sampler is zero-side trivial.

Let `nu` be a finite signed Borel measure on exterior sample points

\[
\Omega_G:=\{(\sigma,v):\sigma>1,\ |v-G|\le H_G\},
\qquad H_G=o(G),
\tag{1}
\]

with finite total variation. For a fixed horizontal zero coordinate `beta<1`, define the signed Poisson superposition

\[
K_{\nu,\beta}(\gamma)
:=
\int_{\Omega_G}
\frac{\sigma-\beta}
{(\sigma-\beta)^2+(v-\gamma)^2}
\,d\nu(\sigma,v),
\tag{2}
\]

and let

\[
M_\nu:=\nu(\Omega_G).
\tag{3}
\]

Then the exact conservation law is

\[
\boxed{
\int_{\mathbb R}K_{\nu,\beta}(\gamma)\,d\gamma
=\pi M_\nu
}
\qquad(\beta<1).
\tag{4}
\]

Consequently, if `M_nu=0`, then

\[
\boxed{
\int (K_{\nu,\beta})_+\,d\gamma
=
\int (K_{\nu,\beta})_-\,d\gamma .
}
\tag{5}
\]

Thus every nonzero zero-mass sampler has a sign-changing zero kernel for every horizontal line on which it has nonzero charge. More quantitatively, if it creates positive integrated charge `A` on a target ordinate interval `I`,

\[
\int_I K_{\nu,\beta}(\gamma)\,d\gamma\ge A>0,
\tag{6}
\]

then its negative lobe obeys

\[
\boxed{
\int_{\mathbb R}(K_{\nu,\beta})_-\,d\gamma\ge A.
}
\tag{7}
\]

This is not merely a harmonic-analysis normalization. In the exterior Hadamard identity used by `NB-144`--`NB-147`, the universal zero budget of a signed sampler supported in `(1)` is

\[
\frac12\int_{\Omega_G}\log |v|\,d\nu(\sigma,v)
=
\frac{M_\nu}{2}\log G
+
O\!\left(
\frac{H_G}{G}\,\|\nu\|_{\mathrm{TV}}
\right).
\tag{8}
\]

Hence the canonical way to cancel the leading `(1/2) log G` term is precisely `M_nu=0`; `(4)`--`(7)` say that the same operation forces zero-side sign loss. A signed scheme can therefore improve on `NB-147` only by supplying genuinely new information that controls where actual zeta zeros meet the negative lobe (or by obtaining compensating cancellation on the prime side). Signed sampling alone does not preserve the positivity mechanism that made `NB-147` unconditional.

## Derivation

For `x>0`, write

\[
P_x(y):=\frac{x}{x^2+y^2}.
\tag{9}
\]

Its vertical mass is independent of `x`:

\[
\int_{\mathbb R}P_x(y)\,dy=\pi.
\tag{10}
\]

Because `nu` has finite total variation and every sample in `(1)` has `sigma-beta>0`, Tonelli applied to the total variation gives

\[
\int_{\mathbb R}
\int_{\Omega_G}
P_{\sigma-\beta}(v-\gamma)
\,d|\nu|(\sigma,v)\,d\gamma
=
\pi\|\nu\|_{\mathrm{TV}}<\infty.
\tag{11}
\]

Fubini is therefore legitimate, and `(10)` yields

\[
\int_{\mathbb R}K_{\nu,\beta}(\gamma)\,d\gamma
=
\int_{\Omega_G}\pi\,d\nu
=
\pi M_\nu,
\]

which proves `(4)`. If `M_nu=0`, the integral of `K` vanishes. Since `K` is integrable, its positive and negative parts have equal mass, proving `(5)`. Equation `(7)` follows because the positive part has total mass at least the positive net mass contributed on `I`.

For `(8)`, write `v=G+u` with `|u|<=H_G=o(G)`. Uniformly on the support,

\[
\log|v|=\log G+O(H_G/G).
\tag{12}
\]

Integrating `(12)` against the signed measure gives `(8)`.

The simplest discrete example makes the exported negative lobe explicit. Take two samples at the same ordinate, with horizontal zero-distances `0<a<b`, and coefficients `+1,-1`. Then

\[
P_a(y)-P_b(y)
=
\frac{(b-a)(ab-y^2)}
{(a^2+y^2)(b^2+y^2)}.
\tag{13}
\]

The kernel is positive exactly for

\[
|y|<\sqrt{ab},
\tag{14}
\]

negative for `|y|>sqrt(ab)`, and has zero integral. Differencing does produce the desired localizing lobe, but the negative tail is not an artefact of this two-point choice: `(4)` shows that it is forced for every zero-mass signed superposition, including continuous samplers and coalescing finite differences.

## What this does and does not rule out

The result rules out the tempting architecture

\[
\text{cancel the universal log term}
\quad+\quad
\text{retain all-zero positivity}
\quad+\quad
\text{discard the rest of the zero sum}.
\tag{15}
\]

That architecture cannot be nontrivial. If `M_nu=0` and `K_{nu,beta}` were nonnegative for every ordinate on a fixed horizontal line, `(4)` would force `K_{nu,beta}=0` almost everywhere; for finite discrete sampling the rational kernel then vanishes identically.

The finding does **not** prove that signed sampling is useless. On the contrary, `(13)` shows exactly why it is attractive: a positive lobe can be concentrated around the target packet while the universal logarithmic background disappears. What remains is now a sharply identified source-specific obligation. One must control the zeta zeros lying in the negative lobe strongly enough that their signed contribution cannot erase the target gain, and simultaneously control the signed prime-side combination of `zeta'/zeta`. Those are new arithmetic inputs; they are not contained in the positive Euler-product majorant used by `NB-147`.

Nor does `(7)` assert that the negative *integrated kernel mass* is automatically sampled by actual zeta zeros. A zero-free negative lobe would cost nothing in the discrete zero sum. The obstruction is therefore to a positivity-only proof, not to a localization proof supplied with additional local zero information. This distinction is essential: the theorem identifies exactly what a successful signed argument has to buy rather than declaring the whole signed route dead.

## Why this matters for the Nyman–Beurling frontier

`NB-147` reduced positive exterior sampling to an exact weighted reflection-closure budget. The obvious escape was to cancel that leading budget by taking signed or oscillatory combinations. Equations `(4)`--`(8)` show that this escape necessarily exchanges one resource for another: cancelling the `Theta(log G)` Hadamard background creates a zero-mean boundary kernel, and zero-mean localization must carry an equal negative lobe.

The next useful theorem can therefore be stated more narrowly. It must either provide a local zero-distribution estimate strong enough to bound the negative lobe of a chosen signed kernel, construct a target-aware signed kernel whose negative lobe lies in a region controlled by existing source information, or obtain prime-side cancellation that permits a different balance. Merely adding more signed exterior samples without such control cannot inherit the monotone-discard argument of `NB-144`--`NB-147`.

## Assumptions and boundaries

- The conservation law `(4)` is exact for every finite signed sampler with finite total variation and every fixed `beta<1`; no RH, zero-density theorem, spacing hypothesis, or simplicity assumption is used.
- The bridge `(8)` assumes the sample ordinates remain in an `o(G)` window around the same large height. This is the natural local packet regime of `NB-144`--`NB-147`; samples spread across macroscopically different heights can cancel logarithms by a different weighted identity and are not classified here.
- The theorem concerns the zero-side Poisson kernel. It does not estimate the signed Euler/von-Mangoldt side.
- Equal positive and negative *Lebesgue mass* does not imply equal discrete mass on the actual zeta zeros. Any use of `(7)` against the zeta zero set needs an additional sampling/distribution input.

## Prior-art search

Searches were made for signed/differenced Poisson-kernel combinations and differenced logarithmic-derivative explicit formulas. Differenced logarithmic derivatives are classical tools in zero-free-region arguments; for example, Ethan S. Lee, *On an explicit zero-free region for the Dedekind zeta-function* (arXiv:2002.05456), explicitly uses a differenced logarithmic derivative. Bruna and Melnikov, *On translates of the Poisson kernel and zeros of harmonic functions*, Bull. London Math. Soc. 39 (2007), 317--326, study spans of Poisson-kernel translates and harmonic uniqueness. These sources delimit the general harmonic-analysis background, but the exact line-local conclusion here is elementary and source-specific: cancelling the common Hadamard `log G` mass in the `NB-147` sampling architecture is the same zero-total-mass condition that forces an equal negative Poisson lobe. No external theorem is load-bearing for `(4)`--`(8)`.

## Source map

- `NB-144`, `NB-146`, `NB-147`: line-local source of the exterior logarithmic-derivative/Poisson architecture and the positive-sampling `Theta(log G)` budget being tested.
- Classical Poisson identity `(10)`: derived directly here.
- Hadamard leading term in `(8)`: the same standard logarithmic-derivative identity already anchored and used in `NB-144`--`NB-147`.
- External prior-art hits above are contextual only; no `SOURCES.md` addition is required.
