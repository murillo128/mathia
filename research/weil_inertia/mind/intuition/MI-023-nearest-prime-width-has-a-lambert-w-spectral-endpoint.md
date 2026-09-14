# MI-023 — Two-island complete screening is exactly a nearest-prime-power Lambert-W gap constraint

**Evidence level:** exact for the one-signed, completely screened, symmetric two-island branch through [WI-288](../../findings/WI-288-two-island-complete-screening-is-exactly-a-nearest-prime-power-gap-condition.md), using the prime-deleted spectral endpoint of WI-284/WI-287. This is not a theorem for many-component supports, sign-changing modes, incomplete screening, or existence/nonexistence of prime-power gaps of the required size.

For two symmetric narrow islands

`E=(-R-b,-R+b) union (R-b,R+b)`,

let `Delta=2R` and `x=e^Delta`. Same-island overlaps with prime-power translations are impossible once `b<log(2)/4`; cross-island overlap occurs exactly when a translation lag lies in `(Delta-2b,Delta+2b)`. Therefore complete screening by **all** active prime powers is equivalent, without approximation, to

`2b <= delta_pp(x)`,

where

`delta_pp(x)=min_(q prime power)|log q-log x|`.

This changes the interpretation of the earlier nearest-prime width relaxation. On the symmetric two-island topology, retaining the whole aperture-growing family does not reveal an additional many-prime support invariant: its support content is exactly the actual nearest-prime-power gap. A coarse short-interval theorem loses information only because it upper-bounds that actual gap, not because the full family contains hidden extra overlap geometry.

The spectral zero-bottom condition supplies the opposite inequality. WI-287's gamma uncertainty and exact pole edge imply that a hypothetical completely screened first-crossing null support must have

`2b sqrt(x) >= W(c_0 sqrt(x))`.

Combining with exact screening gives

`sqrt(x) delta_pp(x) >= W(c_0 sqrt(x)) = (1/2)log x - log log x + O(1)`.

Thus the consecutive prime-power gap containing `x` must have additive length at least

`sqrt(x) log x - 2 sqrt(x) log log x + O(sqrt(x))`

at the necessary scale. This is a condition on the hypothetical RH-failure branch, not a claim that such gaps occur.

The live two-island problem is now sharply arithmetic. Improving how many screening lags are retained cannot beat this reduction; one must rule out the required actual prime-power gaps, or introduce amplitude information from the null equation beyond support disjointness. Any genuinely new support-geometric use of simultaneous screening must change the topology (for example many components) or the sign/completeness assumptions.

**Boundary.** Current unconditional prime short-interval theorems still permit gaps much larger than the Lambert scale needed here, so no contradiction follows. Prime powers rather than primes are the exact support object, although prime-gap theorems provide valid upper bounds because primes are prime powers.
