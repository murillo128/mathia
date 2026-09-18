# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Price recurrence only after canonical PNT/pole centering

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability` through `MI-030-pnt-endpoint-modes-cap-jump-only-coercivity-before-completion`.

The local activation, positive-bulk and compact-completion questions are no longer the frontier. PL-338 shows every finite prime-power activation is born with favorable reflected sign when the transported boundary trace is nonzero. PL-339 gives total-source-scale jump coercivity. PL-340--PL-341 identify the sharp PNT prime-block edges `+/-e^a`, while PL-342 promotes those edges to essential spectrum by high-frequency Kronecker recurrence. Finite-rank correction and bounded compact completion therefore cannot suppress the sharp bounded prime edge by themselves.

PL-343 separates existence from prevalence in exactly the recurrence channel used by PL-342. For the weighted endpoint observable `H_a` on the active prime torus,

`mu_a{|H_a| >= eta e^a} <= 2 exp[-(eta^2/8+o(1)) e^(2a)/a]`.

Unique ergodicity transfers the same estimate to long-time density along the physical prime-log orbit for each fixed aperture. Thus the raw edge witnesses needed for essential spectrum are exponentially rare in time even though they exist arbitrarily far out.

PL-344 shows why that rarity is not a first-hit theorem and why the raw first hit is not the completed obstruction. The endpoint weights concentrate the PNT response into an `O(1)` logarithmic boundary layer, and for bounded modulation one has the deterministic profile

`F_a(tau)= [e^a/(1-e^-a)] * e^(2ia tau)/(1+i tau)^2 + o_T(e^a)`.

For every fixed `tau_0`, phase alignment therefore produces `tau_a=tau_0+O(1/a)` with raw edge response

`H_a(tau_a)= +/- e^a/(1+tau_0^2)+o(e^a)`.

So an edge-sized raw prime response can occur at uniformly bounded modulation despite the exponentially small long-time density in PL-343. More importantly, the canonical zeta-pole quadratic form has the same leading bounded-frequency PNT response with the opposite sign. On these states,

`Q_pole(M_tau u_a^+) - H_a(tau)=o_T(e^a)`.

The leading early recurrence is therefore a **PNT-universal background profile that is cancelled by canonical completion**, not a surviving arithmetic instability.

The live theorem must be posed after this centering. Identify the atomic-prime-minus-PNT/pole residual actually left by the completed form, then compare the earliest modulation at which that centered residual reaches a dangerous scale with the unbounded logarithmic principal energy on the same state. A useful result must control the destination-surviving residual itself; recurrence or first-hit estimates for raw `H_a` no longer address the completed coercivity question.

## Keep universal bulk response distinct from rational-prime residual structure

PL-339--PL-344 use PNT-scale positive mass, compressed-shift geometry, finite rational independence, classical concentration/ergodicity and the canonical pole profile. Their sharp bulk spectrum, essential-edge recurrence, exponential Haar rarity and bounded-modulation deterministic response are therefore PNT-universal matched-control phenomena. None by itself supplies rational-prime RH rigidity.

A successful continuation must expose structure remaining **after** the PNT/pole profile has been removed: a rational-prime-specific centered residual, a source-selected branch persistence/noncollapse theorem for that residual, or another same-state quantity not reproduced by a generalized-prime control. Re-proving positivity, sharpening the raw edge, or converting PL-343 prevalence into a raw first-hit estimate would not close the completed operator because PL-344 already identifies and cancels the bounded-frequency leading profile.

## Keep transport, prevalence, centering and completed-state energy distinct

Norm-resolvent continuity transports eigenbranches; activation analysis fixes local birth signs; the bounded block determines ordinary and essential spectral edges; Haar concentration measures prevalence of raw recurrence witnesses; PNT asymptotics determine the bounded-frequency deterministic profile; pole completion removes that universal profile. These are different resources.

The completed low spectrum depends on the arithmetic remainder that survives canonical centering and on how its dangerous states interact with the unbounded principal term. Essential-spectrum existence of the uncentered block, exponentially small time density, and early raw recurrence do not decide that centered same-state competition.