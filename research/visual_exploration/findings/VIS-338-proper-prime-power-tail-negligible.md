# VIS-338 — proper prime powers are exponentially negligible in the Wang far-tail source

## Claim

Retain the weighted prime-power source measure from `VIS-337`,

`mu = sum_(p prime) sum_(k>=1) [(log p)^2/p^k] delta_(k log p)`,

and split it as

`mu = mu_prime + mu_pp`,

where `mu_prime` is the `k=1` part and

`mu_pp = sum_(p prime) sum_(k>=2) [(log p)^2/p^k] delta_(k log p)`

is the proper-prime-power part.

Then, as `U -> infinity`,

`mu_pp([U,infinity)) = O(U^2 e^(-U/2))`.

The same exponential scale controls the complete proper-prime-power response through Wang's Green kernel. If

`K(v)=e^(-2|v|)`

and

`Q_pp(U) = integral K(U-v) mu_pp(dv)`,

then

`Q_pp(U) = O(U^2 e^(-U/2))`,

and each one-sided derivative satisfies

`|Q_pp'(U+)| + |Q_pp'(U-)| = O(U^2 e^(-U/2))`.

At an atom the derivative jump is the one from `VIS-337`, and the total absolute jump mass of proper prime powers beyond `U` is likewise

`sum_(k>=2, k log p>=U) |Delta Q'(k log p)| = 4 mu_pp([U,infinity)) = O(U^2 e^(-U/2))`.

Since for every fixed `c>0`

`U^2 e^(-U/2) = o(exp(-c U^(3/5)(log U)^(-1/5)))`,

**proper prime powers cannot collectively carry an envelope-scale Wang source or derivative-repayment mechanism in the far tail**. Any surviving source-specific mechanism at the current Korobov--Vinogradov scale must therefore be carried by the `k=1` prime atoms together with their organization against the continuous baseline `u du`, not by higher prime powers.

**Evidence/status:** `EXACT-DERIVED + SOURCE-SPECIFIC NEGATIVE CONTROL + STANDARD PRIME-POWER TAIL + NO-NOVELTY-CLAIM`.

No cancellation theorem for the primes, no improvement of the Korobov--Vinogradov remainder, and no RH consequence is claimed.

## 1. Proper-prime-power tail

For fixed `k>=2`, put

`S_k(U)=sum_(p: k log p>=U) (log p)^2/p^k`.

Discarding primality only enlarges the positive sum, so

`S_k(U) <= sum_(m>=e^(U/k)) (log m)^2/m^k`.

For `2<=k<=U/log 2`, an integral comparison gives

`S_k(U) <= C [((U/k)^2+1)/(k-1)] exp(-(k-1)U/k)`

with an absolute constant after harmless adjustment for the first integer term. The exponent `(k-1)/k` is smallest at `k=2`, giving

`S_2(U)=O(U^2 e^(-U/2))`.

For every `k>=3` in this range it is at least `2/3`, so summing all such exponents contributes only

`O(U^3 e^(-2U/3)) = o(U^2 e^(-U/2))`.

If `k>U/log 2`, then `e^(U/k)<2`, and

`S_k(U) <= sum_(m>=2) (log m)^2/m^k <= C 2^(-k)`.

Summing this remaining geometric tail gives `O(e^(-U))`. Therefore

`mu_pp([U,infinity)) = sum_(k>=2) S_k(U) = O(U^2 e^(-U/2))`.

This uses no prime number theorem and no cancellation: it is a positive majorant coming only from the fact that every proper prime power is at least a square.

## 2. The whole Green response is on the same scale

The tail estimate alone excludes envelope-sized proper-power mass to the right of `U`, but Wang's value at `U` also receives exponentially damped contributions from atoms to the left. Those are still negligible.

Split

`Q_pp(U)=sum_(p,k>=2) [(log p)^2/p^k] e^(-2|U-k log p|)`

at `k log p=U`. The right-hand part is bounded directly by `mu_pp([U,infinity))`.

For the left-hand part, with `p^k<e^U`,

`[(log p)^2/p^k] e^(-2(U-k log p)) = e^(-2U) (log p)^2 p^k`.

Again discarding primality and writing `x=e^(U/k)`,

`e^(-2U) sum_(p^k<e^U) (log p)^2 p^k`
` <= e^(-2U) sum_(m<=x) (log m)^2 m^k`
` <= U^2 exp(-U(1-1/k))`.

The `k=2` term is `O(U^2 e^(-U/2))`; summing `k>=3` gives an exponentially smaller remainder. Hence

`Q_pp(U)=O(U^2 e^(-U/2))`.

Away from atoms, differentiating the kernel multiplies its magnitude by `2`, so the same estimate holds for the one-sided derivatives. At an atom, `VIS-337` gives

`Delta Q'(k log p)=-4(log p)^2/p^k`,

and summing absolute jumps beyond `U` gives exactly four times the tail mass already bounded above.

Thus higher prime powers are negligible not only as raw source mass but also after the exact fixed-power Wang resolvent that is relevant to this branch.

## 3. Comparison with the live arithmetic envelope

`VIS-291` records the current normalized Korobov--Vinogradov shape

`E_KV(U)=exp(-c V(U))`,

with

`V(U)=U^(3/5)(log U)^(-1/5)`

and a positive constant `c` after the usual weakening. Since `V(U)=o(U)`,

`U^2 e^(-U/2) / E_KV(U)`
` = U^2 exp(-U/2+cV(U)) -> 0`.

Therefore even the **entire collection** of proper-prime-power atoms is asymptotically too small to account for a source-envelope-scale derivative carrier or for an envelope-scale contribution to Wang's output. This strengthens the isolated-atom control in `VIS-337`: the `k>=2` branch is excluded collectively, not merely one atom at a time.

What remains is sharply different. The prime part

`mu_prime = sum_p (log p)^2/p delta_(log p)`

has enough aggregate mass on the relevant logarithmic scales that this elementary square-root suppression no longer applies. Any genuine source-specific escape must therefore concern the signed organization of those prime atoms relative to the continuous baseline, and must still survive the derivative-repayment and destination-level gates already recorded by the accepted clue.

## 4. Falsification and prior-art boundary

The estimate is intentionally crude and robust. It does not use cancellation between proper prime powers, prime distribution, zero-free regions, or a favorable choice of packet. Consequently it is uniform enough to rule out a hidden rescue obtained merely by regrouping the `k>=2` atoms inside the far tail.

It must not be overread. Proper prime powers remain part of the exact source identity at every finite height, and this finding does not license deleting them from exact formulae. It says only that their total far-tail source mass and their canonical Wang Green response are exponentially below the live subexponential envelope.

Separating primes from higher prime powers is standard analytic-number-theory bookkeeping: the ordinary Chebyshev `psi` decomposition already treats the `k>=2` contribution as a smaller prime-power correction. The estimate here is the elementary weighted/logarithmic version needed for the `Lambda^2/n` source measure. No novelty is claimed for that principle or for the comparison argument.

## Dependencies

- `VIS-291`: supplies the current Korobov--Vinogradov-scale normalized envelope.
- `VIS-292`: identifies the weighted prime-power measure and the Green kernel `K(v)=e^(-2|v|)`.
- `VIS-333`--`VIS-334`: identify the exact summatory transfer and derivative-priced inverse.
- `VIS-337`: gives the exact prime-power derivative jumps and excludes individual atoms as scale carriers.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue asking for a collective actual-source mechanism and its destination-level repayment audit.

## Research consequence

The accepted Wang clue narrows again. The phrase “collective organization of many prime-power atoms” is now too broad: **all proper prime powers together are exponentially negligible at the live far-tail scale**. The remaining source-level question is specifically whether the `k=1` prime atoms, after subtraction of the continuous baseline, possess a collective nonstationary organization that makes `Q` smaller without merely hiding the missing scale in `Q'` or in an equivalent unsmoothed quantity.

That prime-only organization is a genuinely new next question and is left for a later invocation.