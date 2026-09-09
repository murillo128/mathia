---
id: CLUE-farey-gcd-critical-counterterm-certificate
type: research-clue
status: proposed
origin: master-researcher
target_line: weil_positivity
based_on:
  - research/farey_discrepancy/findings/FD-001-denominator-shell-discrepancy-is-a-ramanujan-mertens-frame.md
  - research/weil_positivity/findings/WP-218-euler-schur-regularization-has-a-negative-toeplitz-symbol.md
---
# A Farey/GCD bridge identifies the noncompact critical counterterm

## Observation

FD-001 computes the L2 Gram structure of denominator-shell discrepancy. WP-218 identifies a negative essential Toeplitz symbol in the local Euler-Schur kernel. The following bridge makes their relation explicit, without claiming that positivity of a discrepancy Gram proves Weil positivity.

On the circle, define the mean-zero counting distribution b_m = sum_{a=1}^m delta_{a/m} - m dx. Its nonzero Fourier coefficients are m times the indicator that m divides k. For s > 1/2, use the homogeneous H^{-s} inner product with Fourier weight |k|^{-2s}. Directly summing over nonzero multiples of lcm(m,n) gives

<b_m,b_n>_{H^{-s}} = 2 zeta(2s) mn / lcm(m,n)^{2s}.

Consequently h_m = m^{s-1} b_m satisfies

<h_m,h_n>_{H^{-s}} / (2 zeta(2s))
= gcd(m,n)^{2s} / (mn)^s
= product_p p^{-s |v_p(m)-v_p(n)|}.

The normalized prime-local kernel is R_r(a,b) = r^{|a-b|}, with r = p^{-s}. Its entrywise critical limit as s decreases to 1/2 is exactly r = p^{-1/2}. This is a connection between the objects, not a new arithmetic estimate.

Important distinction: the actual L2 primitive/discrepancy calculation in FD-001 corresponds to s = 1 and r = p^{-1}. It does not already provide the critical r = p^{-1/2} form. The unnormalized H^{-1/2} energy diverges because 2 zeta(2s) diverges. A normalized kernel limit is not an unrenormalized critical Hilbert-space energy.

There is also an exact identity exposing the missing term. On l2(N_0), let S e_a = e_{a+1}, D = I-S, e_0 the first unit vector, and v_r = (1,r,r^2,...). Put

E_r = e_0 e_0^* - (1-r)(e_0 v_r^* + v_r e_0^*).

Then rank(E_r) <= 2 and

D R_r D^* = 2(1-r) I + ((1-r)^2/r)(I-R_r) + E_r.

For interior entries a,b >= 1 this follows from taking the two finite differences of r^{|a-b|}: the diagonal is 2(1-r), and each off-diagonal entry is -(1-r)^2 r^{|a-b|-1}. The boundary row is accounted for by E_r: its (0,0) entry is 2r-1 and its (0,b), b>=1, entry is -(1-r)r^b. This verifies the full bounded-operator identity for 0<r<1, not only a finite-section approximation.

Solving for the WP local term gives

I-R_r = [r/(1-r)^2] D R_r D^* - [2r/(1-r)] I - [r/(1-r)^2] E_r.

Thus a positive difference energy comes with an explicit negative NONCOMPACT scalar term. A finite-rank boundary correction cannot compensate that term. Multiplying this identity by the local log p factor does not change the obstruction.

## Research question

Does the genuine source-fixed archimedean/pole/mixed-prime remainder supply a noncompact compensation for this explicitly identified term on the actual Weil domain? Or does this bridge only re-express the already known negative essential symbol?

The useful target is a counterterm certificate, not a generic positive Gram representation. The operator domain, coefficient normalization, coupling across primes and order of removing cutoffs must be taken from the actual source; do not invent an independent sum of local scalar counterterms on an undefined global space.

## Why it may matter

The bridge imports an exact arithmetic positive-kernel representation from Farey/GCD geometry, but simultaneously exposes why its positivity does not resolve WP-218. It replaces an unspecified hope for a geometric positivity repair with an explicit source term that must be present and large enough.

No claim of literature novelty is made for GCD kernels, Sobolev counting energies, or Toeplitz finite differences. The proposed contribution is a portfolio-specific, falsifiable comparison of FD-001 with WP-218.

## Decisive test

First independently verify the displayed identity, including the unilateral boundary. As a local algebra sanity check, 60-by-60 sections were tested at r = 0.1, 0.25, 2^{-1/2}, 3^{-1/2}, and 0.95; the maximum absolute residual was at most 1.42e-16 in floating point. The entrywise argument above, not the numerical test, establishes the identity.

Next insert the exact Gamma/pole/mixed-prime remainder from the real source, retaining its domain and normalization. Test its quadratic form on normalized shift-localized packets approaching the negative-symbol region, uniformly as the local/prime cutoffs and s>1/2 regularization are removed. A useful positive result must demonstrate genuine noncompact domination, not a compact correction, finite-section positivity, or a change of basis that suppresses the tested packet.

If the candidate compensation is only compact, the WP-218 essential-spectrum obstruction rejects it immediately. If the source remainder fails on an admissible packet, record that precise candidate rejection and stop. If the domination survives, state the exact uniform estimate and identify what remains for the full Weil form; do not infer RH from a local identity.

## Evidence boundary

Owner: weil_positivity. Imports: FD-001 and WP-218 at reviewed commit 16e9325e032fabb3b9a59664b7f7a15174a65ec2. FD-001 is used for arithmetic discrepancy/Gram structure, and WP-218 for the source kernel and noncompact obstruction. The bridge identity and its local sanity checks were developed in this extraordinary Master/Visionary audit.

The normalized kernel is well defined at the entrywise critical limit; the underlying unnormalized energy is not. Positivity of D R_r D^* must not be confused with positivity of I-R_r. No actual source remainder, full prime limit, repository test suite, Lean proof, or global positivity certificate was verified in this audit.

This proposed clue requires owner-side semantic deduplication against concurrently added clues. Stop/re-export criterion: re-export to farey_discrepancy only a verified new source-level compensation or a precise obstruction to the proposed compensation. If all that survives is the known Toeplitz no-go in different notation, close the bridge rather than opening a new line or promoting a finding.
