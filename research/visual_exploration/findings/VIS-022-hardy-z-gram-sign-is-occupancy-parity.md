# VIS-022 — Gram-point Hardy Z sign is the parity projection of Gram occupancy

## Claim

Let

`Z(t) = exp(i theta(t)) zeta(1/2 + it)`

be Hardy's real-valued `Z` function. Let `a < b` be real numbers such that neither endpoint is a zero of `Z`, and let `M(a,b)` be the total multiplicity of zeros of `Z` in `(a,b)`. Then

`sgn Z(b) / sgn Z(a) = (-1)^{M(a,b)}`.

Let `N(T)` count all nontrivial zeros `rho = beta + i gamma` of `zeta(s)` with `0 < gamma <= T`, counted with multiplicity, and assume also that neither endpoint is a zero ordinate. The functional-equation symmetry about the critical line pairs every off-critical-line zero `beta + i gamma` with `1-beta + i gamma` with the same multiplicity. Therefore the off-line contribution to `N(b)-N(a)` is even, so

`M(a,b) = N(b) - N(a) (mod 2)`

and hence exactly at the level of signs

`sgn Z(b) / sgn Z(a) = (-1)^{N(b)-N(a)}`.

For consecutive Gram points `g_n,g_{n+1}` from VIS-021, with

`C_n = N(g_{n+1}) - N(g_n)`, 

this becomes

`sgn Z(g_{n+1}) / sgn Z(g_n) = (-1)^{C_n}`.

Thus the complete sign sequence sampled at Gram points is determined by the Gram-interval occupancy sequence together with one initial sign. It is not an independent analytic channel: it is the one-bit parity projection of occupancy.

**Evidence/status:** `CLASSICAL-COROLLARY + EXACT-DERIVED + NEGATIVE/OBSTRUCTION`.

No RH assumption is used. No novelty is claimed for the parity mechanism; the Mathia contribution is the resulting visual-independence boundary.

## Exact derivation

Because `Z(t)` is real analytic on the real axis, crossing a real zero of multiplicity `m` multiplies its sign by `(-1)^m`. Multiplying over all critical-line zeros between two nonzero endpoints gives

`sgn Z(b) = (-1)^{M(a,b)} sgn Z(a)`.

Now partition the nontrivial zeros counted by `N(b)-N(a)` according to whether they lie on the critical line. Critical-line zeros contribute exactly `M(a,b)`. For a zero `rho = beta + i gamma` with `beta != 1/2`, the functional equation together with conjugation gives a zero `1-beta + i gamma`; the two members have the same multiplicity. Consequently every off-line contribution at positive ordinate `gamma` occurs in an even-multiplicity package. Therefore

`N(b)-N(a) - M(a,b)`

is even, proving the parity identity.

Specializing to consecutive Gram points immediately gives the formula in the claim. Iterating it yields

`sgn Z(g_m) = sgn Z(g_n) (-1)^{C_n + C_{n+1} + ... + C_{m-1}}`

for any later Gram point whose endpoints avoid zeros. Hence even the longer sampled sign pattern is recoverable from occupancies up to one initial bit.

## What this removes from the visual search space

VIS-021 showed that Gram occupancy `C_n`, the discrete increment of the Gram-sampled `S` term, and the zero-counting discrepancy are algebraically interconvertible. The present result quotients one more natural-looking channel: the endpoint sign of Hardy's `Z` function.

In particular, coloring Gram points as good/bad by the sign of `(-1)^n Z(g_n)`, plotting the binary sign sequence, or highlighting sign flips between adjacent Gram points cannot corroborate an occupancy anomaly independently when the occupancy sequence is already known. These views forget information rather than add it: they retain only occupancy parity plus an initial sign convention.

This is stronger than the usual observation that an odd number of critical-line zero multiplicities forces an endpoint sign change. The key visual-control point is that **all** nontrivial zeros counted off the critical line disappear modulo two because of the exact reflection symmetry. The occupancy count therefore supplies the same endpoint-sign parity without assuming that every counted zero lies on the critical line.

## Prior art and novelty assessment

The ingredients and parity mechanism are classical. DLMF §25.10 defines the real-valued Hardy `Z(t)` and states both the symmetry of nontrivial zeros about the critical line and the use of `Z` sign changes to detect critical-line zeros. DLMF §25.4 records the functional equation underlying the reflection symmetry. Hutchinson's 1925 treatment of Gram's law and the later Gram-block literature use the sign of `Z(g_n)` as a standard diagnostic.

The parity argument itself also appears explicitly in expository treatments of Turing's method: the number of off-critical-line zeros below a Gram height is even by reflection symmetry, while the sign of `Z` records the parity of critical-line crossings. For example, J. Dousselin's exposition *Méthode d'Alan Turing et hypothèse de Riemann* cites Edwards p. 173 while making exactly this even-off-line-zero comparison.

Accordingly, the displayed identities are not presented as a new theorem. Their durable value here is a **representation-dependence obstruction**: a visual atlas that already includes exact Gram occupancy must not count sampled `Z` signs or good/bad Gram-point coloring as an independent source of structure.

## Boundary conditions

The clean sign formulas require endpoints where `Z` is nonzero. The statement also avoids heights that are zero ordinates so that the difference of the standard `N(T)` values needs no limiting convention. Equivalent one-sided formulations can be made at exceptional endpoints, but they add no content to the visual-independence result.

Multiplicity matters. An even-multiplicity critical-line zero does not change the sign of `Z`, exactly as the parity formula records. Off-critical-line zeros contribute even total multiplicity at each reflected ordinate even if a critical-line zero happens to share that same ordinate.

The result does not reconstruct `|Z(g_n)|`, derivatives, extrema, local shape inside a Gram interval, or the precise locations and multiplicities of its critical-line zeros from `C_n`. Those remain genuinely richer candidate channels. It only collapses the Gram-sampled **sign** channel.

## Visual consequence

No canonical PNG is retained. A binary sign strip next to the occupancy strip would visually demonstrate the parity relation, but once the exact identity is known such a rendering is deterministic from the occupancy data and would create a duplicate visual artifact rather than a new research instrument.

## Research consequence

The canonical visual-atlas clue should treat Gram-sampled `Z` sign as belonging to the same information family as Gram occupancy, but at a strictly coarser level: occupancy determines sign transitions modulo two, while sign cannot recover occupancy magnitude. Future Gram-based visual exploration should therefore spend its independent-channel budget on data such as `|Z|`, derivatives/local shape, sub-Gram zero location, or a representation whose information is not a deterministic quotient of `N(g_n)` and `C_n`.
