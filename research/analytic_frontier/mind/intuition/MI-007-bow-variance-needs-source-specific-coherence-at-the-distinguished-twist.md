# MI-007 — Bow cancellation is source alignment inside a fixed spectral geometry

**Evidence level:** exact post-sieve normal forms, matched local-statistics controls, unitary-gauge reduction, and sharp box near-kernel scale through ANF-154

## Core intuition

The distinguished bow twist does not create a distinguished Gram spectrum. After the exact gauge reduction, the moving-window operator is one fixed untwisted geometry and the arithmetic question is entirely in how the demodulated prime innovation sits inside its spectral decomposition.

Small quadratic energy is therefore an alignment statement, but not automatically a periodicity statement. The positive spectrum itself collapses down to scale `K/N^2`, so substantial distance from the exact periodic kernel can coexist with very small normalized bow energy.

## Strongest justified principle

ANF-150--ANF-152 show that matched post-sieve controls can reproduce the available local prime statistics while retaining diagonal bow variance, and that any fixed amount of source energy above a positive Gram level prevents subdiagonal cancellation.

ANF-153 proves that the logarithmic twist is a diagonal unitary gauge: normalized spectrum, rank and nullity are independent of the twist. Its exact kernel is the zero-mean `K`-periodic class after de-normalization. ANF-154 then gives the sharp quantitative boundary. The smallest positive normalized box scale is `Theta(K/N^2)` in the bow regime, and a one-quantum detuning of a kernel character has energy of that order while staying globally orthogonal to the exact kernel.

## Program consequence

Seek a source theorem for the actual demodulated post-sieve innovation that controls spectral mass relative to the fixed bow operator at the collapsing scale relevant to the target. Do not search for twist-specific eigenvalue effects, and do not replace the spectral problem by approximate periodicity unless the much stronger `q=o(K/N^2)` regime has independently been reached.

## Counterevidence / boundary

The spectral reduction is exact but does not show that the primes align with the near-nullspace. The sharp box examples are matched geometric controls, not models of prime coefficients. A global arithmetic relation could still force the required alignment without making the source close to any exact periodic vector.

## Epistemic status

**Exact destination geometry and sharp near-kernel rigidity scale; the source mechanism producing or forbidding the required spectral alignment remains open.**

## Falsification criterion

Invalidate the unitary-gauge reduction or the `K/N^2` near-kernel scale, or derive the required bow cancellation while retaining a quantitatively incompatible amount of source mass in the fixed positive spectral sector. A positive continuation should prove the source-specific spectral projection estimate itself.
