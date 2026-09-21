# MI-089 — Ambient cancellation helps a source family only after its weighted image pays the occupancy tariff

**Evidence level:** exact finite harmonic-analysis and CRT synthesis from [MC-446](../../findings/MC-446-source-frame-box-mean-square-has-quadratic-occupancy-threshold.md) and [MC-447](../../findings/MC-447-crt-source-frame-fibers-collapse-to-shift-common-primes.md), continuing the incomplete source-frame branch isolated in MC-413.

A favorable second moment on a large ambient parameter box is not automatically a favorable estimate on the arithmetic image that the source actually occupies. For primitive characters, MC-446 computes the exact full `(u,a)`-box second moment of the incomplete translated correlations. In the rough squarefree range it has root-mean-square size `sqrt(H)`, so genuine collective cancellation exists before completion.

Transferring that ambient cancellation to a weighted source family by plain Cauchy has an exact price. If equal source frames are first aggregated into weights `W(u,a)`, the relevant participation ratio is

`R_eff(W)=||W||_1^2/||W||_2^2`.

The full-box `L^2` bound can beat the pointwise `H||W||_1` estimate only when `R_eff` exceeds `E_q(H)/H^2`, which is about `q^2/H` when `phi(q)~q`. Sparse arithmetic images therefore do not inherit ambient RMS cancellation merely because the ambient family cancels well.

MC-447 then removes two apparent ways of manufacturing the missing occupancy in the natural separated-modulus regime. When `d,e<=D`, `D^2<q` and `(h,q)=1`, the frame `(u,a)` recovers the exact lcm `L=[d,e]` and canonical CRT residue. Same-frame ambiguity comes only from primes common to `L` and `h`, with multiplicity at most `3^omega((L,h))`; if the shift is coprime to the sieve support, the divisor-pair map is injective. Fixing `a=hL^(-1)` is therefore just fixing the lcm, not gaining a second free averaging coordinate.

The reusable lesson is to price **image occupancy after quotienting collisions and weights**, not the size of the ambient family or the number of source preimages. A strong ambient moment can be diluted by a sparse image, while many algebraic source pairs can collapse to too few effective weighted frames. Conversely, failure of ambient Cauchy is not a no-go for a restricted arithmetic moment: the actual image may have Fourier, bilinear or dispersion structure that the ambient estimate throws away.

For the current q-vdC branch, the live object is therefore a restricted weighted second moment on the distinct CRT-idempotent `u`-frames, with the well-factorable coefficients inserted before Cauchy. Fibre multiplicity and the constrained `a` coordinate are no longer plausible free gains in the coprime-shift separated regime. A useful theorem must lower the diagonal/off-diagonal tariff on that actual arithmetic set, exploit coefficient cancellation or modulus factorization, or move to a quantitatively useful regime outside the separated hypotheses.

**Boundary.** The `q^2/H` scale is the tariff of the full ambient moment plus Cauchy, not a universal lower bound for every restricted estimate. MC-447 depends on squarefree support, `(h,q)=1` and `D^2<q`; wraparound, nonunit shifts, variable interval lengths and structured weighted dispersion remain open. No Mertens or individual character-sum improvement follows from the occupancy calculation alone.
