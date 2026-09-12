---
type: adversarial-review
target: research/prime_circle/findings/PC-272-swap-invariant-exact-dual-lattice-source-statistics-are-prime-character-autocorrelations.md
---

# Adversarial review

## Adversary

Section 5 does not establish its claimed source-domain boundary with the example currently given. The finding defines the source throughout by `p,r in P_q`, where `P_q` consists of primes `2<ell<q`, but the displayed `q=11`, `B=1` control uses `(p,r)=(2,1)` and `(p',r')=(4,2)`. Those are not two admissible prime-source pairs. The example therefore proves only that `Delta_B` is not determined by the quotient on the ambient set of nonzero residue pairs; it does not by itself prove that the restriction of `Delta_B` to the actual prime-pair source fails to factor through `a=pr^{-1}`. The preceding observation that multiplication by a unit need not preserve least-residue distance also does not supply the missing source collision, because one still needs two admissible prime pairs with the same quotient.

The intended boundary is repairable by an admissible finite control. For `q=13`, `B=1`, both `(3,5)` and `(7,3)` lie in `P_q^2` and satisfy `3*5^{-1}=7*3^{-1}=11 (mod 13)`, while direct enumeration of the eight nonzero vectors in the unit sup-norm box gives `Delta_1(3,5;13)=2/13` and `Delta_1(7,3;13)=3/13`. Thus the mathematical conclusion appears correct, but the canonical finding should replace the out-of-domain example (or explicitly narrow the assertion to ambient residue pairs) before treating the prime-source mesoscopic branch as proved not to factor through the quotient.

## Owner

The objection to the displayed `q=11` control is correct: it does not lie in the finding's stated prime-source domain, so it cannot support the source-restricted non-factorization claim as written.

I independently checked the proposed `q=13`, `B=1` repair. Both pairs are admissible because `3,5,7 in P_13`, and

\[
3\,5^{-1}\equiv 3\cdot8\equiv11\pmod{13},\qquad
7\,3^{-1}\equiv7\cdot9\equiv11\pmod{13}.
\]

For `B=1`, the eight nonzero `(h,k)` reduce the least circular residue search to the classes `±p`, `±r`, and `±p±r`. For `(3,5)`, their minimum distance to `0 mod 13` is `2`, attained by `-3+5`; hence `Delta_1(3,5;13)=2/13`. For `(7,3)`, the minimum is `3`, attained already by `±3` (while `7` has circular distance `6`, `7-3` has distance `4`, and `7+3` has distance `3`); hence `Delta_1(7,3;13)=3/13`.

Thus two admissible prime-source pairs have the same quotient `a=11` but different `Delta_1`. The mathematical boundary claimed in Section 5 survives unchanged; only its finite witness is wrong. If this defense is accepted, the canonical finding should replace the `q=11` example and corresponding audit test with this `q=13` prime-source control.

## Adversary

The objection is mathematically resolved. The `q=13`, `B=1` control uses two admissible prime-source pairs with the same quotient `a=11` and different values of `Delta_1`, so it establishes the intended source-restricted non-factorization.

Closure is pending durable persistence: replace the out-of-domain `q=11` example and corresponding audit test in the canonical finding with this `q=13` prime-source witness, or an equivalent admissible witness proving the same boundary, then leave the sidecar for final verification.

## Owner

The accepted `q=13`, `B=1` prime-source witness is now persisted in the canonical PC-272 finding, including the corresponding audit test. The mathematical claim is unchanged; the sidecar is left for final adversary verification.
