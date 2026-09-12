# MI-007 — Matched first-layer packets convert selector dilation into an opposite Chebyshev--Mertens error drift

**Evidence level:** supported by the exact matched-packet prime-set identity RE-068, timing compression RE-069, selector-dilation/Chebyshev law RE-070, and the reciprocal-prime error law RE-071; no contradiction with known joint prime-error estimates is claimed.

The matched first-layer branch is exactly silent to additive endpoint prime statistics. RE-068 shows that the physical labels crossed by the packet are precisely the ordinary primes in the selector interval, while RE-069 shows that direct positional delay is compressed to an absolutely summable contribution by the Robin workload.

RE-070 finds the first surviving coordinate before that compression. The tied common-amplitude selector expands the target interval while the exact Chebyshev mass remains equal to the logarithmic state increment. Therefore every sufficiently late matched packet forces a positive increment of the Chebyshev error `H_vartheta(Z)=Z-vartheta(Z)`.

RE-071 shows that the same packet forces a second, oppositely oriented coordinate. For the normalized logarithmic Mertens-product error `E_l`, the increment across the packet is negative. Both signs come from the same selector derivative: interval dilation makes the Chebyshev mass underdense, while the Robin-height/Mertens normalization turns the same matched prime set into a decrease of `E_l`. The prime-square correction between the two Euler weights is too small to change that sign, uniformly even when packet cardinality grows.

For sublinear packets, the two increments are tied asymptotically: the magnitude of the Mertens decrease is the Chebyshev increase divided by `Y log Y`. Thus the surviving object is not one prime statistic but a **joint trajectory in two differently normalized error coordinates** forced by one adaptive selector geometry.

This sharpens the target. A contradiction may come from a theorem controlling the admissible joint drift of `H_vartheta` and `E_l` on these source-selected intervals, or from a cross-packet argument showing that the required saddle cannot recur. Re-proving additive multiset identities or direct timing bounds attacks coordinates already known to be blind.

**Boundary.** RE-071 gives a necessary opposite-drift law under the false-RH matched first-layer hypotheses. It does not prove the packets recur indefinitely, does not handle higher CA layers, and does not by itself contradict known Chebyshev/Mertens error estimates.