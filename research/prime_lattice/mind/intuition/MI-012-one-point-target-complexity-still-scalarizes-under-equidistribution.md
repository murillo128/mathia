# MI-012 — Arithmetic survival needs both parity-sensitive tail coupling and a source-prescribed phase

**Evidence level:** literature-backed exact reductions and matched controls through PL-192

## Core intuition

The affine Prime-Lattice branch has two independent erasure mechanisms. Local exponent data below every subpower cutoff misses the large-prime parity tail, while scalar phase observation can erase or counterfeit cancellation even after a hard target is retained. The surviving mechanism must therefore preserve **nonlocal parity-sensitive factorization information** and evaluate it in a phase regime selected by the source rather than by generic window geometry.

PL-191--PL-192 make the second requirement sharper. A fixed positive-width window whose normalized center escapes is neither intrinsically rigid nor intrinsically flat: ordinary prime density makes the unweighted control flat at many theorem-scale escaping centers, while finite-frequency Bohr recurrence forces the same control to return near its coherent profile at arbitrarily remote centers.

## Strongest justified principle

PL-184--PL-186 place every bounded statistic of the shifted-prime exponent vector below a subpower cutoff inside a Kubilius one-point model. PL-188 identifies the remaining parity boundary: strong Type-I/local-divisor information can coexist with the wrong Liouville parity, and breaking it requires an additional bilinear/parity-sensitive input.

PL-187 supplies broad-window erasure for every bounded coefficient sequence. PL-189 proves that a fixed positive-width window with bounded center is qualitatively different: compact Fourier support and analytic uniqueness force its zero-frequency mean to vanish if the whole window flattens. PL-190 reduces shrinking windows to a pointwise value.

PL-191 then gives a canonical matched control for the remaining subresolution moving-window regime. On a macroscopic rational-prime band with coefficients identically one, fixed-width windows centered at any `u_X -> infinity` inside the current `X^(13/15-o(1))` phase range flatten uniformly even though `F_X(0)=1`. PL-192 proves that this does not extend to arbitrary large centers: Bohr almost periodicity gives `T_X>X` at which the same carrier has a fixed coherent core. Hence phase escape alone contains no coefficient-blind arithmetic information.

The durable rule is: **a high phase is useful only when the arithmetic construction prescribes why that phase is sampled and why the target-specific coefficient coupling survives there.** Moving the window after seeing the carrier, or appealing to “very high frequency” in the abstract, is compatible with both universal flattening and universal recurrence.

## Counterevidence / boundary

PL-191 uses the current short-interval-PNT resolution range and does not identify a sharp transition at exponent `13/15`. PL-192 supplies arbitrarily large recurrence centers but no useful upper bound for the first recurrence. A source-forced center may still evade both controls, and joint/nonlocal/completed observables are not reduced to this scalar finite-band model.

## Epistemic status

**Proved matched-control boundary; open target-specific mechanism.** The density and almost-periodicity ingredients are classical, while their combination sharply classifies the remaining scalar window intuition.

## Falsification criterion

Produce a coefficient-blind asymptotic law valid for all escaping fixed-width centers despite the contradictory PL-191/PL-192 subsequences, or derive an independently source-prescribed phase together with a parity-sensitive target theorem that is not reproduced by the unweighted control. The latter would be a genuine escape rather than a contradiction.