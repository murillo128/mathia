---
type: adversarial-review
target: research/prime_circle/findings/PC-272-swap-invariant-exact-dual-lattice-source-statistics-are-prime-character-autocorrelations.md
---

# Adversarial review

## Adversary

Section 5 does not establish its claimed source-domain boundary with the example currently given. The finding defines the source throughout by `p,r in P_q`, where `P_q` consists of primes `2<ell<q`, but the displayed `q=11`, `B=1` control uses `(p,r)=(2,1)` and `(p',r')=(4,2)`. Those are not two admissible prime-source pairs. The example therefore proves only that `Delta_B` is not determined by the quotient on the ambient set of nonzero residue pairs; it does not by itself prove that the restriction of `Delta_B` to the actual prime-pair source fails to factor through `a=pr^{-1}`. The preceding observation that multiplication by a unit need not preserve least-residue distance also does not supply the missing source collision, because one still needs two admissible prime pairs with the same quotient.

The intended boundary is repairable by an admissible finite control. For `q=13`, `B=1`, both `(3,5)` and `(7,3)` lie in `P_q^2` and satisfy `3*5^{-1}=7*3^{-1}=11 (mod 13)`, while direct enumeration of the eight nonzero vectors in the unit sup-norm box gives `Delta_1(3,5;13)=2/13` and `Delta_1(7,3;13)=3/13`. Thus the mathematical conclusion appears correct, but the canonical finding should replace the out-of-domain example (or explicitly narrow the assertion to ambient residue pairs) before treating the prime-source mesoscopic branch as proved not to factor through the quotient.