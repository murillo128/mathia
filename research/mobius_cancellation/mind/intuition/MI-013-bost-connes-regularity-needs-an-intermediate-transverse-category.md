# MI-013 — Bost--Connes cancellation has a near-diagonal middle category, but its useful strength is expensive

**Evidence level:** exact finite-algebra, modular-twist, heat-orbit, Gallagher-localization, and variance-pricing results through MC-175

## Core intuition

The earlier Bost--Connes channels collapse into phase-blind size, local phase selection, or a global signed endpoint already as hard as the Möbius/RH target. Gallagher localization supplies a genuine middle category: a positive finite-time heat norm controlled by an exact **signed near-diagonal Möbius energy** whose off-diagonal terms retain prime orientation.

The remaining issue is no longer whether such an intermediate observable exists. It is how much cancellation can be proved in it without silently asking for a major zero-free theorem. Diagonal heat type in the robust sub-washout range is already analytically expensive, and support-only autocorrelation routes can erase precisely the orientation the Gallagher energy retains.

## Strongest justified principle

MC-156--MC-171 classify the finite algebra, modular twist, and stationary/long-window heat endpoints. MC-172 derives the Gallagher energy, its exact triangular near-diagonal expansion, its independent-prime-phase diagonal baseline, and the `tau=3/8` matched-control washout boundary.

MC-173 proves an exact information-loss control: Doyle's additive autocorrelation transfer is identical for every support-matched unit prime phase, so its strong square-free `ell^2` input cannot by itself control the signed Gallagher off-diagonal.

MC-174 prices the full diagonal target. For `1/8<=tau<3/8`, diagonal Gallagher heat type transfers to fixed vertical modulations and yields a fixed zero-free half-plane `Re(s)>sqrt(1/4+2tau)`.

MC-175 then interpolates local variance strength. Under the declared power envelope, square-root local variance is required throughout `1/8<=tau<=1/4`; only later horizons allow a weaker fixed power, and the first horizon permitted by a saving exponent `eta>0` already corresponds conditionally to the fixed zero-free boundary `Re(s)>sqrt(1-eta/4)`.

## Program consequence

Treat the Gallagher near-diagonal energy as a graded cancellation currency. Seek a source-sensitive local second-moment theorem whose exponent is genuinely stronger than coherent size, retain the Möbius phase through the proof, and state the exact heat/zero-free consequence of the achieved rate. Do not impose diagonal type as a supposedly modest intermediate target.

## Counterevidence / boundary

The pricing results do not prove that a useful subdiagonal exponent is inaccessible, and MC-174 does not make the Gallagher target RH-equivalent. Other signed local statistics or proof architectures may achieve a favorable tradeoff outside the MC-175 envelope. The exact no-go in MC-173 is specific to autocorrelation routes that square away the phase.

## Epistemic status

**Supported intermediate signed category with exact quantitative pricing; no new Möbius variance theorem or zeta zero-free region is established.**

## Falsification criterion

Produce a support-only/autocorrelation argument that distinguishes the true Möbius prime phase in the MC-172 energy, or derive diagonal Gallagher type in the MC-175 early range from a fixed variance exponent below square-root scaling under the stated envelope. A positive continuation should instead prove and price a genuinely phase-sensitive local variance gain.