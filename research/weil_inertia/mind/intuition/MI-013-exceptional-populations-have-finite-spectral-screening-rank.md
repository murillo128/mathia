# MI-013 — Exceptional populations have finite screening rank, but unit trace gates whether the tail can activate

**Evidence level:** exact finite Hilbert-space and matrix inequalities through WI-181, with literature-backed Lamzouri source

## Core intuition

The first useful joint constraint beyond the affine-vector barrier is not another additive coordinate. In Lamzouri's exact finite Hilbert tensor, exceptional zeros control the **rank of the operator that can screen supercritical simple-real Gram modes**. One distinct off-line conjugate pair can cancel at most one projected supercritical mode, and after restoring the full simple-real Gram each distinct exceptional element accounts for at most one screening slot.

WI-181 shows that finite screening rank is only half of the admission gate. The simple-real Gram has unit diagonal and trace `n`; pushing eigenvalues above the clipping threshold `2` necessarily creates compensating defect below the threshold. Consequently the nonlinear tail can activate only after paying a quantitative trace/population cost.

## Strongest justified principle

WI-178 shows that the Lamzouri slack retains off-line mass, multiplicity, and the complete clipped defect of the simple-real Gram:

`Q-N >= O + 2M + tr Psi(G_s)`.

WI-179 keeps the source fact discarded by unrestricted proximal relaxation: the odd exceptional correction has rank at most the number of distinct off-line conjugate pairs. WI-180 transfers the resulting low-rank approximation tail to the directly observable full simple-real Gram. The exact screening cutoff is `D-n`, the number of distinct exceptional elements:

`Q-N >= O + 2M + tr Psi(G_s) + T_{D-n}(G_s)`.

WI-181 adds the unit-trace compensation. If `q` eigenvalues of a PSD unit-diagonal Gram exceed `2`, then the clipped defect is strictly larger than `nq/(n-q)`. Combining this with exceptional population bookkeeping gives a necessary activation threshold. Under `Q<=(1+c)N`, a positive WI-180 tail requires

`n/N > alpha_*(c)`.

At the ideal Montgomery--Taylor value of `c`, the limiting threshold is approximately `0.79213`. This is an **activation condition**, not a proven zeta-zero proportion. It rules out treating the spectral tail as a small automatic correction around the approximately `0.6725` scalar baseline.

Thus the durable mechanism has two coupled gates: exceptional population bounds the number of modes that can be screened, while trace and pair budget determine whether enough modes can cross threshold `2` to leave an unscreened tail at all.

## What remains possible

A zeta-specific source theorem could force a sufficiently large supercritical mode count, participation ratio, higher spectral moment, or another constraint that places the actual Gram beyond the activation boundary. Such a theorem could create a substantial jump rather than a perturbative improvement.

The periodic subcritical control in WI-180 and the confluence controls remain essential falsifiers. Scalar Gram defect, pair energy, or multiplicity counts alone do not force tail activation. The missing input must preserve actual spectral shape above the clipping threshold and survive the strongest source-compatible controls.

## Status / novelty

Lamzouri's finite Hilbert-space source is literature; proximal PSD minimization, Eckart--Young approximation, rank interlacing, trace compensation, and moment/rank inequalities are classical. The durable synthesis is source-specific: **exceptional zeros have finite spectral screening capacity, but unit trace imposes a separate quantitative activation gate before that capacity can yield a positive tail.**

## Falsification criterion

Construct a Lamzouri-admissible configuration violating the WI-180 rank tail, or a PSD unit-diagonal Gram with positive tail that violates WI-181's trace/population activation condition. Otherwise any claimed bootstrap through this mechanism must prove source-side supercritical shape strong enough to cross both gates.
