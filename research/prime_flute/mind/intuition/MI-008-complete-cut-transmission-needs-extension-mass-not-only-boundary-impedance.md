# MI-008 — Prime-Flute compactness requires genuinely diverging local response frequency

**Evidence level:** proved operator/form-theoretic boundary

## Core intuition

Energy normalization reduces the endpoint to the relative geometry of heavy low/high extension ranges. The cheapest noncompactness witness is an exact scalar **high-band shorting deficit**, but fixed-window response profiles cannot keep it positive unless their local complexity itself diverges.

The physical cutoff is fixed globally, yet the dense low-frequency grid forces every admissible high profile on a fixed pant window to move to arbitrarily high **local** Sobolev frequency. A persistent local heavy angle therefore requires the normalized mixed-response Riesz representatives to develop high-frequency mass or lose uniform amplitude/regularity control.

## Strongest justified claim

PF-279--PF-289 show that the strength factors remain heavy, the thresholded angle is exactly a product of heavy-range projections, and separated local vectors with positive Rayleigh floors and persistent normalized mixed correlation force noncompactness.

PF-290 optimizes the high-vector choice exactly: the squared optimal mixed correlation equals the variational energy drop `delta=1-inf_h k[ell+h]/k[ell]`, equivalently a projection energy and Schur complement. A positive limsup of these deficits on a separated tail kills compactness.

PF-291 shows that the physical low-frequency grid becomes complete on every fixed window, so every precompact family of fixed-window response profiles has vanishing optimized pairing with the high-pass space. Scalar reciprocal-width profiles are therefore insufficient.

PF-292 sharpens this from compactness to frequency. The constrained local Dirichlet frequency floor `omega_n` of the high-pass space diverges. More generally there is a moving cutoff `R_n->infinity` below which the high projection becomes asymptotically blind. Hence any uniformly `L^2`-bounded response family with a fixed positive fractional Sobolev bound has vanishing high-pass projection and cannot sustain the PF-290 local obstruction.

## Synthesis of evidence

The next local test is now quantitative: can the **genuine mixed DtN response** generate nonvanishing mass above a diverging local tangential frequency scale, or force its normalized amplitude/regularity to blow up? Merely invoking a two-dimensional response, variable width, or another bounded smooth profile is no longer enough.

If a uniform positive Sobolev estimate can be proved for the actual normalized response family, the PF-290 local noncompactness route closes and the positive endpoint problem must return to global heavy-range projection counts.

## Counterevidence / boundary cases

PF-292 gives no rate for `omega_n` beyond divergence and does not prove a uniform Sobolev bound for the true mixed response. The physical high witnesses do exist, so some local frequency scale reaches at least up to the thin-corridor scale.

Failure of the local falsifier still does not prove weak trace class.

## Epistemic status

**Exact local frequency boundary:** persistent local shorting requires genuinely escaping tangential frequency or regularity; every uniformly positive-Sobolev response family is asymptotically annihilated by the fixed physical high-pass.

## Novelty/prior-art status

Shorted forms, Schur complements, Fourier completeness, Rellich compactness, and Sobolev spectral tails retain their finding-level classifications.

## Falsification criterion

Invalidate the PF-290 shorting identity, PF-291 strong high-pass annihilation, or PF-292 diverging frequency floor. Strategically, prove or disprove a uniform fractional-Sobolev bound for the genuine normalized mixed DtN response.
