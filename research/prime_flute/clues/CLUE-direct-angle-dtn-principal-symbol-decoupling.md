---
id: CLUE-prime-flute-direct-angle-dtn-principal-symbol-decoupling
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-001-exact-cuff-coordinate.md
  - research/prime_flute/findings/PF-205-natural-width-cuff-smoothing-is-C1-uniform-and-critical-orlicz-summable.md
  - research/prime_flute/findings/PF-210-prime-density-makes-logarithmic-rank-low-modes-weak-trace-class.md
  - research/prime_flute/findings/PF-212-thin-fermi-boundary-frequency-split-closes-local-high-mode-gate.md
  - research/prime_flute/findings/PF-214-simultaneous-seam-precision-is-block-jacobi-and-uniform-adjacent-hopping-would-force-exponential-schur-locality.md
  - research/prime_flute/findings/PF-215-thin-pant-corridors-force-normalized-adjacent-hopping-to-diverge.md
  - research/prime_flute/findings/PF-232-hypercycle-straightening-shear-is-reciprocal-prime-form-small.md
  - research/prime_flute/findings/PF-233-variable-width-diagonal-corridor-has-exact-operator-valued-transfer-law.md
  - research/prime_flute/findings/PF-234-pf205-symmetric-seam-normalizer-is-quadratically-flat-comparable.md
  - research/prime_flute/findings/PF-235-hypercycle-boundary-compactification-has-only-quadratic-prime-dependent-defect.md
  - research/prime_flute/findings/PF-238-one-sided-seam-domination-closes-complete-lift-dressed-diagonal-transfer.md
  - research/prime_flute/findings/PF-239-reciprocal-prime-shear-makes-critical-band-leakage-absolutely-trace-summable.md
  - research/prime_flute/findings/PF-242-hypercycle-shear-is-exponentially-local-in-poschl-teller-mode-index.md
  - research/prime_flute/findings/PF-247-fixed-axis-compactification-is-parity-jacobi-in-corridor-modes.md
  - research/prime_flute/findings/PF-255-hypercycle-compactification-transport-is-a-parity-local-flow-with-a-two-derivative-leakage-bound.md
  - research/prime_flute/findings/PF-281-energy-normalized-cross-form-removes-bounded-frequency-coupling-gate.md
  - research/prime_flute/findings/PF-299-prime-seam-scale-has-critical-ell-one-accumulation.md
  - research/prime_flute/findings/PF-315-sequential-physical-band-elimination-factorizes-the-full-angle-defect.md
  - research/prime_flute/findings/PF-316-direct-channel-payment-makes-the-conditional-angle-endpoint-visible.md
  - research/prime_flute/findings/PF-317-positive-diagonal-completion-reduces-the-direct-angle-to-local-pant-crossing.md
  - research/prime_flute/findings/PF-318-logarithmic-rank-hilbert-schmidt-averages-already-close-the-direct-angle-at-weak-trace.md
  - research/prime_flute/findings/PF-319-corridor-form-smallness-alone-does-not-control-the-seam-normalized-direct-angle.md
  - research/prime_flute/findings/PF-320-form-smallness-controls-the-direct-angle-even-when-raw-seam-blocks-amplify.md
  - research/prime_flute/findings/PF-321-superlinear-seam-scale-local-angle-decay-is-trace-class.md
---

# Can the shear-deleted local pant angle gain any fixed superlinear power of the seam scale?

## Observation

PF-315--PF-316 reduce the full physical `P/H` endpoint to two genuine angle channels, the conditional post-low angle `T_H` and the direct angle

\[
Z_{LH}=J_{LL}^{-1/2}J_{LH}J_{HH}^{-1/2}.
\]

PF-317 shows that the direct channel may be bounded through local pant crossing, and PF-318 gives one convenient endpoint target: a local squared Hilbert--Schmidt budget

\[
C\frac{1+\log P_n}{P_n^2}
\]

is enough for the prime-density weak-`S_1` count.

PF-319 blocks the naive route from PF-232 form-smallness to the raw seam-normalized mixed block. PF-320 then changes the correct object: multiplicative closeness of positive forms controls their **intrinsic low/high angles**, even when the raw seam blocks amplify. For the PF-232 sandwich the actual sheared local angle differs from the shear-deleted local angle by operator norm `O(P_n^{-1})`; logarithmic low rank places that shear error inside PF-318's weak-trace budget. PF-320 also gives contraction-sandwich reassembly for sums of positive local forms, so common finite-pant completion may remain in both forms.

PF-321 now removes another unnecessary requirement from the **reference** problem. PF-299 proves that the exact tight-pant seam distances `s_n=(h_n+h_{n+1})/2` lie in every `ell^q`, `q>1`, and PF-321 strengthens this to

\[
\sum_n(1+\log P_n)s_n^q<\infty
\qquad(q>1).
\]

Therefore, for the logarithmic-rank local reference angles,

\[
\boxed{
\|T_{0,n}^{(r)}\|\le C s_n^{1+\varepsilon}
\quad\text{for one fixed }\varepsilon>0
}
\]

already makes their orthogonal direct sum **trace class**. The earlier reciprocal-prime Hilbert--Schmidt criterion remains valid, but it is no longer the weakest useful target.

This relaxation aligns with PF-233's exact diagonal-corridor representation. Writing its variable width as `a_n=s_n b_n` gives the exact scaling `T_{a_n}=s_n^2\widetilde T_n` after mass conjugation, and the transfer function `F(x)=x/sinh x` has expansion `1-x^2/6+O(x^4)`. That does not yet prove physical `L/H` angle decay: the physical Fourier split, actual seam metric, unbounded transverse operator, and finite pant completion are still load-bearing. But it identifies a much cheaper decisive test: **does any fixed superlinear seam-scale cancellation survive those representation steps?**

There is now a concrete adversarial check against using that Taylor expansion too early. PF-235/PF-247 identify the fixed axis compactification `tau=log tan(theta/2)`, for which the reference corridor form `A=-partial_theta^2+csc^2(theta)` acquires exponentially growing weights as `|tau|` approaches the ends of a long cuff lift. Meanwhile PF-212's fixed physical low band contains `O(ell_n)` Fourier modes on a cuff of length `ell_n`, so elementary trigonometric-polynomial packets can concentrate a nonzero fraction of their mass in an `O(1)` tangential window while remaining entirely inside that fixed low band. PF-001 gives the exact calibration

\[
e^{\ell_n/2}=\coth(h_n/4),
\]

and PF-299 gives `s_n=(h_n+h_{n+1})/2\ge h_n/2`. Hence

\[
\boxed{
s_ne^{\ell_n/2}
\ge \frac{h_n}{2}\coth\frac{h_n}{4}
>2.
}
\]

So a proof must not assume, without an explicit finite-pant calculation, that `s_n^2\widetilde T_n` is uniformly small on the **entire physical-low sector** merely because `s_n\to0`. The shrinking seam scale is exactly capable of being cancelled by the long-cuff compactification scale. This is a falsification test for a proof strategy, not yet a lower bound on the intrinsic angle: the physical quotient, seam normalization, off-diagonal `L/H` projection, and common pant completion may still create the needed cancellation.

PF-215 remains the essential negative control: the complete adjacent normalized pant block diverges on the cuff-constant channel. The target here is specifically the retained nonconstant-low/high intrinsic angle after constants are removed.

## Research question

For one canonical one-cusp pant contribution, delete only the PF-232 hypercycle-straightening shear while retaining:

- the actual PF-205 seam energy used by simultaneous normalization;
- the variable-width diagonal corridor;
- the full common finite-pant/cusp-side completion;
- the fixed physical low/high cutoff from PF-212.

After distributing a positive block-diagonal share of the identity as in PF-320, let

\[
T_{0,n}^{(r)}
\]

be the intrinsic local low/high angle of this **shear-deleted** positive pant form for one of the finitely many neighboring offsets `r`.

Does the reference family satisfy either of the following endpoint-complete estimates?

\[
\boxed{
\|T_{0,n}^{(r)}\|\le C s_n^{1+\varepsilon}
\quad\text{for some fixed }\varepsilon>0,
}
\]

or, failing that, PF-318's mean-square criterion

\[
\boxed{
\|T_{0,n}^{(r)}\|_{\mathcal S_2}^2
\le C\frac{1+\log P_n}{P_n^2}?
}
\]

The first conclusion is stronger globally: PF-321 makes the shear-deleted reference direct angle trace class. The second is already enough for weak trace class. In either case PF-320 adds the actual shear at its established weak-`S_1` cost. The separate conditional post-low angle `T_H` remains independent.

## Why it may matter

The live theorem is narrower and more geometry-native than the previous raw-block question. PF-319 still says not to infer seam-normalized raw `K_{LH}` smallness from corridor form-smallness. PF-320 says that stronger raw estimate is unnecessary, and PF-321 says reciprocal-prime decay of the **reference angle** is also unnecessary.

The exact seam distance is the natural small geometric parameter of the tight pant. Because it lies in every `ell^q`, `q>1`, the global endpoint is extraordinarily tolerant of any fixed superlinear local gain. This suggests attacking the reference family in the variable-width corridor coordinates where PF-233 already exhibits an even small-`s_n` transfer expansion, rather than forcing a modulewise `P_n^{-1}` estimate from the outset.

The remaining representation question is sharp. The identity/principal part of PF-233's transfer cannot mix `L/H` if it remains diagonal in the physical split, while the first formal transfer correction is quadratic in `s_n`. The actual proof must determine whether mass conjugation, the physical cuff coordinate, seam normalization, and finite pant completion preserve **some** `s_n^{1+\varepsilon}` gain. The compactification stress test above says that this cannot be replaced by a blanket small-graph-norm estimate on all retained low modes: any successful Taylor argument must expose an **off-diagonal cancellation after the physical `L/H` projections**, or else use the weaker singular-value/Hilbert--Schmidt route. If that cancellation exists, no finer prime-by-prime PDE estimate is needed for this reference channel.

## Decisive test

Work on one local positive pant form and its fixed physical `L/H` split. Keep the actual seam normalizer, but replace the PF-232 sheared corridor by its shear-deleted variable-width diagonal form while leaving every common completion term unchanged.

Before using the PF-233 Taylor expansion uniformly, test the most adversarial fixed-low packets allowed by the growing cuff length. On one lifted cuff cell of length `ell_n`, choose a normalized nonconstant trigonometric polynomial supported in `0<|xi|<=kappa` whose phases align in an `O(1)` window adjacent to a cell end. Under the PF-235/PF-247 fixed compactification, compute its reference `A`-form contribution before the finite-pant quotient/completion step. The exact PF-001/PF-299 relation above shows that any estimate which needs `s_n A^{1/2}` to vanish uniformly on the whole physical-low space is at the critical scale and must be proved rather than assumed.

Then exploit PF-233 at the exact scale `a_n=s_nb_n`. Separate the identity/principal transfer from

\[
F(s_n\widetilde T_n^{1/2})-I,
\qquad
F(x)=\frac{x}{\sinh x}.
\]

The decisive quantity is the **projected off-diagonal piece** after transport to the actual physical cuff representation, not the unprojected Taylor remainder. Test whether the `L/H` projection, seam-energy normalization, and common finite-pant completion cancel the compactification-critical low packets strongly enough that the intrinsic mixed angle obeys

\[
\|T_{0,n}^{(r)}\|=O(s_n^{1+\varepsilon})
\]

for any fixed `\varepsilon>0`. A quadratic `O(s_n^2)` estimate is more than enough by PF-321. The estimate must be on the **intrinsic angle** with its own low/high diagonal energies, not on the raw externally normalized mixed block.

If a superlinear operator-norm estimate fails, identify whether the compactification-critical packet produces genuine linear/order-one `L/H` angle mass or whether only the unprojected graph norm is large. In the latter case the Taylor proof route fails but the angle may still be small. In either case fall back to PF-318 and estimate the local singular-value distribution or Hilbert--Schmidt leakage directly. A negative result must exhibit nonconstant-low/high angle mass incompatible with both PF-321's weighted seam-scale summability and PF-318's weak-`S_1` threshold count; constant-mode growth from PF-215 and raw metric amplification from PF-319 are not such witnesses.

PF-238 remains useful for identifying which diagonal transfer pieces survive the actual seam metric, and PF-242/PF-255 remain independent structural information if the physical-coordinate transport itself becomes the obstruction. Reintroduce them only where they address the representation step that actually loses the superlinear gain.

## Evidence boundary

PF-321 is an implication theorem, not the missing local PDE estimate. It proves that a fixed superlinear seam-scale bound on the shear-deleted local intrinsic angles would put the reference direct channel in `S_1`; it does not prove that such a bound holds.

PF-233 gives the exact scaled transfer representation and an even small-argument expansion, but the unbounded transverse operator means the Taylor series cannot simply be applied in operator norm on the whole boundary space. The fixed physical `L/H` split and the full finite pant completion must be handled before any `O(s_n^2)` claim is promoted.

The compactification-critical packet test added here is likewise **not** a finding that the physical angle is large. PF-001, PF-212, PF-235, PF-247, and PF-299 make the scale collision precise enough to falsify an unjustified uniform low-sector graph-smallness step, but the lifted-cell packet has not yet been propagated through the actual one-cusp-pant quotient, seam normalization, projected `L/H` corner, and common completion. A large unprojected `A`-form can disappear from the intrinsic angle after those operations. Any promotion to a negative finding requires that projected physical-angle calculation.

PF-320 proves only that the actual shear changes the local angle by `O(P_n^{-1})` in operator norm and therefore by the PF-318-compatible squared Hilbert--Schmidt budget after logarithmic low-rank counting. It does not transfer PF-233's formal quadratic corridor expansion through the complete physical reference problem.

The fixed-domain DtN literature remains prior-art guidance rather than a degeneration theorem. No current external source supplies this canonical shrinking-pant physical-angle endpoint.

The clue therefore remains `accepted`, not `resolved`.

## Research disposition

Outcome: `accepted`.

PF-321 materially relaxes the preferred proof obligation, while the exact cuff/compactification calibration prevents an equally naive use of that relaxation. The first target remains **any fixed superlinear seam-scale decay of the shear-deleted local intrinsic angle**, but it must now be demonstrated in the projected physical angle rather than inferred from uniform smallness of the full PF-233 Taylor remainder on retained low modes. If that off-diagonal cancellation is absent, PF-318's reciprocal-prime mean-square criterion remains the fallback. PF-320 then adds the real shear without reopening the raw seam-block problem.