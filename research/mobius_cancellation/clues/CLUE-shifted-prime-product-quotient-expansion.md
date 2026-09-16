---
id: CLUE-mobius-cancellation-shifted-prime-product-quotient-expansion
type: research-clue
status: rejected
origin: research-watch
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-305-endpoint-coset-occupancy-forces-near-shell-radical.md
  - research/mobius_cancellation/findings/MC-306-near-shell-singleton-source-profile-saturates-current-capacities.md
  - research/mobius_cancellation/findings/MC-317-random-linear-erasure-augmentation-closes-generic-endpoint.md
---

# Can shifted prime-product expansion kill the one-defect endpoint at near-shell source scale?

## Observation

`MC-317` closes the generic binary-code route permissively: the endpoint generalized-weight profile can occur in ordinary `[2R,R]` codes, so any further obstruction must use the arithmetic realization of the columns. `MC-305` identifies one such realization. For a common squarefree source radical `P`, the selected quadratic-character map

\[
\Theta:(\mathbb Z/P\mathbb Z)^\times\to\{\pm1\}^R
\]

is onto, while an exact one-defect endpoint puts every shell prime into only the `R` sign cells with exactly one `+1` coordinate.

This concentration becomes much stronger after multiplication. If `r` and `s` are endpoint shell primes, then `\Theta(rs)=\Theta(r)\Theta(s)`. Products with the same defect index land in the identity cell; products with different defect indices land in a cell with exactly two flipped coordinates. Hence all pair products of endpoint shell primes occupy at most

\[
1+\binom R2=O(R^2)
\]

of the `2^R` selected quotient cells. At the critical frontier `2^R\asymp\log y` and `R\asymp\log\log y`, this is a vanishing fraction of the quotient.

Established product-of-primes results point in the opposite direction for less localized prime sets. Matomäki--Teräväinen prove that, for every sufficiently large modulus `q`, products of two primes `p_1,p_2\le q` occupy at least `(2/3-\varepsilon)\varphi(q)` reduced residue classes modulo `q`; Szabó obtains related positive-density product-set expansion and develops a sieve/character-sum route to multiplicative support growth. Those theorems do not directly apply here because the endpoint uses a translated dyadic shell, essentially primes in `(y,2y]`, with `P=y^{1+o(1)}` rather than all primes up to the modulus.

## Research question

Does a shifted/dyadic analogue of prime-product expansion hold at the near-shell modulus scale forced by `MC-305`--`MC-306`?

A sufficient target is the following qualitative statement. Let `q` be odd squarefree with `q=y^{1+o(1)}` and let

\[
\mathcal P_I=\{p\in(y,2y]:p\equiv1\pmod4,\ (p,q)=1\}.
\]

Is there an absolute `c>0` such that, uniformly in the relevant range where `y=q/(\log q)^{O(1)}` (or more generally `y=q^{1-o(1)}`), the product set

\[
\mathcal P_I\mathcal P_I\pmod q
\]

occupies at least `c\varphi(q)` reduced residue classes?

The full residue-class theorem is stronger than necessary. For the actual selected quadratic subgroup it would suffice to prove that the projection of these products under `\Theta` occupies `c2^R` sign cells, or any number `\omega(R^2)` uniformly at the endpoint scale.

## Why it may matter

This attacks exactly the arithmetic localization left open by `MC-306` and avoids the generic coding obstruction of `MC-317`. If pair products from the shell occupy a fixed positive fraction of reduced classes modulo `P`, then surjectivity and equal fiber size of `\Theta` force their quotient image to occupy at least a fixed positive fraction of the `2^R` sign cells. The endpoint, however, permits only `1+\binom R2` cells. Since

\[
\frac{2^R}{R^2}\to\infty
\]

at the critical rank, the two statements would be incompatible.

Such a theorem would therefore kill the near-shell matched endpoint profile of `MC-306` for a reason that is genuinely arithmetic: primes in a long translated interval would be forced to expand multiplicatively across simultaneous Legendre-sign cells. It would not require a new generic code bound, a stronger scalar large sieve, or an RH-level zero-free input.

## Decisive test

First determine whether the existing product-of-primes literature already contains a theorem uniform enough for a translated interval of length `q/(\log q)^{O(1)}` near `q`, with squarefree `q` and the fixed condition `p\equiv1\pmod4`. The unshifted Matomäki--Teräväinen and Szabó results are not enough by themselves.

If no such theorem is available, test whether Szabó's sieve/character-sum support argument or the Matomäki--Teräväinen multiplicative dense-model argument survives this localization. The quantitative audit must keep three points explicit: the trivial Fourier mass of primes in the shifted interval, uniform control of nonprincipal character sums after the shift, and the product-support inequality converting those bounds into a positive-density residue set. Burgess-type estimates are shift-uniform for ordinary character sums, but that fact alone does not establish the required prime-supported theorem.

The fixed `1 mod 4` condition must be retained rather than discarded; it may be handled by working modulo `4q` or by an equivalent character decomposition, with all density losses tracked. If full residue-class expansion is too strong, repeat the analysis directly in the selected quotient and ask only for `\omega(R^2)` occupied `\Theta`-cells.

Kill or sharply narrow the direction if a source-compatible family with `q=y^{1+o(1)}` can keep shell-prime pair products inside `O(R^2)` selected cells without contradicting the strongest available shifted character-sum/sieve bounds, or if every proof of positive-density expansion in this regime requires zero-free information comparable to the RH-scale target being sought.

## Evidence boundary

No shifted-shell product-expansion theorem is established here. The published results located in the bounded prior-art check concern products of primes from initial ranges such as `p\le q`, not the exact translated dyadic shell needed by the endpoint. The observation that endpoint pair products occupy only Hamming weights `0` and `2` in the selected quotient is exact, but turning that sparsity into a contradiction requires a new or already-existing arithmetic localization theorem whose hypotheses and uniformity have not yet been verified. This is therefore a research clue, not a finding.

## Research disposition

Rejected as a line-local research priority after `MC-321` and `MC-322`. The endpoint that motivated this clue is now ruled out more directly in the same prime-shell observation category: the Puchta/Klurman--Mangerel--Teräväinen prime Halász--Montgomery inequality bounds the simultaneous character-bias energy on the exact dense dyadic prime shell. `MC-321` already contradicts the natural one-defect family in its common-modulus range, and `MC-322` strengthens that obstruction to a bounded `\ell^2` shell-bias budget for every fixed-power range `q\le y^{3-\delta}`.

A translated prime-product expansion theorem may remain independently interesting, but it is strictly stronger than what is now needed to decide this endpoint and is not established by the current evidence. Continuing to pursue it here would therefore spend research effort on an unproved theorem after its original target has already been closed. Reopen only if a future mechanism introduces a genuinely new target whose survival depends specifically on shifted product-set expansion rather than on prime-shell character-bias energy.