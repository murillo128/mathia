# VIS-182 — fixed bounded prime gaps are diluted in the full prime prefix

## Claim

Let

`w_p=p^(-alpha)`,

`Q_y=sum_(p<=y) w_p^2`,

with a fixed exponent `0<=alpha<=1/2`. Fix any finite set `Delta` of nonzero integer shifts. Then the normalized coefficient mass of prime pairs with one of those fixed gaps satisfies

`C_Delta(y)`
` = Q_y^(-1) sum_(d in Delta) sum_(p<=y-|d|, p and p+d prime) w_p w_(p+d)`
` -> 0`.

More precisely,

- for `0<=alpha<1/2`, `C_Delta(y)=O_(alpha,Delta)(1/log y)`;
- for `alpha=1/2`, `C_Delta(y)=O_Delta(1/log log y)`.

Consequently, in the full-prime linear-support variance problem of `VIS-181`, **no pre-fixed finite collection of bounded additive prime gaps can by itself carry an `O(1)` normalized off-diagonal variance defect**. The unresolved `alpha<1/2` region in the generic weighted Montgomery–Vaughan bound therefore cannot be explained by simply transplanting the fixed-gap two-prime mechanism of `VIS-180` into the full prime prefix.

Any surviving full-prefix linear-support defect for `alpha<1/2`, if one exists, must use gap scales that grow with `y`, an aggregate of increasingly many gap classes, or another distributed off-diagonal organization not captured by a fixed bounded-gap band.

**Evidence/status:** `CLASSICAL UPPER-BOUND SIEVE + PNT/PARTIAL SUMMATION + EXACT WEIGHT DILUTION + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This does **not** prove the full variance null for `alpha<1/2`, does not give a uniform estimate when the allowed gap set grows with `y`, and does not contradict the sparse bounded-gap obstruction in `VIS-180`.

## 1. Fixed-shift prime pairs have one fewer logarithm of density

For a fixed nonzero integer `d`, let

`N_d(x)=#{p<=x : p and p+d are prime}`.

For odd `d`, apart from the isolated possibility involving the prime `2`, there are no sufficiently large prime pairs of difference `d`, so the contribution is finite. For fixed even `d`, the classical Brun–Selberg upper-bound sieve gives

`N_d(x) <<_d x/(log x)^2`.

Only this upper bound is needed. No Hardy–Littlewood asymptotic, twin-prime conjecture, or lower bound for any fixed gap is assumed.

Fix a finite set `Delta`. Since its size and shifts are fixed, all implied constants below may depend on `Delta`.

## 2. Weighted fixed-gap mass for `alpha<1/2`

Put

`M_Delta(y)=sum_(d in Delta) sum_(p<=y-|d|, p and p+d prime) p^(-alpha)(p+d)^(-alpha)`.

On a dyadic block `x<p<=2x`, fixed `d` gives

`p^(-alpha)(p+d)^(-alpha) <<_(alpha,d) x^(-2alpha)`

once `x` is larger than `2|d|`. The sieve bound therefore gives

`sum_(x<p<=2x, p and p+d prime) p^(-alpha)(p+d)^(-alpha)`
` <<_(alpha,d) x^(1-2alpha)/(log x)^2`.

When `alpha<1/2`, the exponent `1-2alpha` is positive, so summing dyadic blocks up to `y` is dominated geometrically by the top scales:

`M_Delta(y) <<_(alpha,Delta) y^(1-2alpha)/(log y)^2`.

On the other hand, the prime number theorem plus partial summation gives

`Q_y=sum_(p<=y) p^(-2alpha)`
` ~ y^(1-2alpha)/[(1-2alpha) log y]`.

Hence

`C_Delta(y)=M_Delta(y)/Q_y <<_(alpha,Delta) 1/log y -> 0`.

The equal-weight case `alpha=0` is the simplest instance: a fixed gap class contains at most `O(y/log^2 y)` prime pairs, whereas the full prime prefix contains `~y/log y` coefficient mass in `Q_y`.

## 3. The critical weight `alpha=1/2`

At `alpha=1/2`, on a dyadic block `x<p<=2x`, the same argument gives

`sum_(x<p<=2x, p and p+d prime) [p(p+d)]^(-1/2)`
` <<_d 1/(log x)^2`.

Writing `x=2^k`, the sum over dyadic scales is bounded by a convergent series `sum_k O_d(k^-2)`. Therefore

`M_Delta(y)=O_Delta(1)`.

Mertens' theorem for primes gives

`Q_y=sum_(p<=y) 1/p = log log y + O(1)`,

so

`C_Delta(y)=O_Delta(1/log log y) -> 0`.

This is consistent with, but weaker than, the complete weighted variance closure already obtained for `alpha=1/2` in `VIS-181`.

## 4. Why this controls a variance mechanism

In the Dirichlet-polynomial expansion used by `VIS-179` and `VIS-181`, the off-diagonal part of `|A_y(t)|^2` contains terms indexed by distinct prime pairs, with coefficient product `w_p w_q/Q_y` multiplied by a time-averaging kernel of modulus at most `1`.

Restrict that off-diagonal sum to pairs with `q-p in Delta`. Its absolute contribution is therefore bounded, up to the fixed normalization constants in the variance identity, by `C_Delta(y)`.

Thus every pre-fixed bounded-gap band contributes `o(1)` to the normalized full-prefix variance for `0<=alpha<=1/2`. This conclusion is independent of any cancellation between different fixed gaps: the total absolute coefficient mass of the band already vanishes.

For `alpha<1/2`, this is information that the coarse leverage term in `VIS-181` does not expose. The generic Montgomery–Vaughan bound aggregates all near-diagonal interactions through `L_y=sum p w_p^2`; its failure to vanish at linear support does not imply that any fixed local gap class remains macroscopically visible.

## 5. Why this does not contradict `VIS-180`

`VIS-180` deliberately chooses only two primes from an infinite recurrent bounded-gap subsequence. In that sparse support,

`Q_y=2`,

so the single close pair carries order-one normalized coefficient mass and its slow beat survives when `H~y`.

Here the support is the **entire prime prefix**. Even if a fixed gap occurs as often as sieve theory permits, its pair count has density at most `O(1/log y)` relative to the prime population at the relevant weighted scale when `alpha<1/2`; at `alpha=1/2` the corresponding weighted mass is bounded while `Q_y` grows like `log log y`.

The two findings therefore identify different normalization regimes rather than conflicting conclusions: bounded gaps can obstruct a theorem uniform over arbitrary sparse supports while becoming negligible inside a diffuse full-prime support.

## 6. Prior art and novelty boundary

The input `N_d(x) <<_d x/(log x)^2` is a standard consequence of Brun–Selberg upper-bound sieve methods for primes separated by a fixed shift. A convenient modern reference is Kevin Broughan, **Bounded Gaps Between Primes: The Epic Breakthroughs of the Early Twenty-First Century**, Cambridge University Press (2021), Chapter 2, “The Sieves of Brun and Selberg”, DOI `10.1017/9781108872201.004`, which develops the fixed-even-shift prime-pair upper-bound sieve. The prime-number-theorem and reciprocal-prime asymptotics used to normalize `Q_y` are classical.

The weighted dyadic estimate above is an immediate line-specific consequence of those standard inputs. No new sieve theorem, prime-pair asymptotic, or general Dirichlet-polynomial theorem is claimed. A targeted literature search did not identify this exact `VIS-181` normalization consequence as a named result; that absence is not used as a novelty claim.

## 7. Boundaries and falsification

The finite set `Delta` must remain fixed as `y` grows. The constants in the sieve bound depend on the shifts, and this finding supplies no uniformity for `|d|<=D(y)` with `D(y)->infinity`.

Accordingly, one cannot sum the `O(1/log y)` conclusion over an increasing family of gaps. A broad near-diagonal band may still carry non-negligible aggregate mass even though every fixed finite band vanishes separately.

The result controls only the bounded-gap portion of the `|A_y|^2` off-diagonal channel. It does not by itself close the other terms in the variance identity, higher moments, discrete sampling, shrinking events, or zeta-facing observables outside the additive prime-log field.

Falsify the finding by finding an error in the fixed-shift sieve upper bound as applied here, the dyadic weighted summation, the partial-summation asymptotic for `Q_y`, or the passage from normalized pair coefficient mass to the absolute fixed-gap contribution in the variance expansion.

## Research consequence

The open `alpha<1/2` linear-support region is narrower than `VIS-181` alone shows. **Fixed bounded prime gaps are not the missing full-prefix mechanism.**

The next quantitative boundary is an expanding near-diagonal window: determine how much normalized coefficient mass and time-kernel coherence can accumulate from gaps `d=d(y)` or bands `1<=d<=D(y)` with `D(y)->infinity`. Any proposed full-prefix variance anomaly should be tested against that growing-gap aggregate before being interpreted as source-sensitive structure.