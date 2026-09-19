# VIS-324 — polynomially long center-gap runs admit the target Selberg upper-bound scale

## Claim

Keep the fixed-gate Wang branch decomposition of `VIS-322` and the singular-series control of `VIS-323`. Thus

`gcd(u,v)=1`, `u != v`,

`M/2 < u,v,q,r <= 2M`,

`h=qv-ur`, `|h|<=D`,

and put

`k=|v-u|`, `L=2 floor(D)+1`.

Assume the same subperiod condition `L<max(u,v)`. For one frozen branch `j`, center-gap decimation produces at most `min(k,L)+1` fixed-gap diagonal runs. Write their lengths and gaps as `ell_s` and `g_s`.

Then, in the non-maximally-fragmented regime `1<=k<=L`, the number `P_j` of branch points for which both prime coordinates are prime satisfies the uniform upper bound

`P_j << L/log^2(3+L/k) + k`.

The implied constant is absolute.

Consequently, at the natural Wang scale

`L asymp M/log log M`,

for every fixed `delta>0`, all represented centers with

`k<=M^(1-delta)`

satisfy

`P_j <<_delta L/log^2 M`.

The same holds after summing the at-most-three frozen branches. Thus every center whose diagonal runs remain polynomially long already has the two-prime upper-bound density needed at the natural scale. Any worst-cell excess capable of defeating the `VIS-316` target must concentrate in the near-maximal center-gap regime

`k=M^(1-o(1))`,

including the fully fragmented range `k>L`, or must arise from a different aggregation mechanism not visible in the branchwise prime-pair count.

**Evidence/status:** `LITERATURE+DERIVED + RANGE-CLOSURE + SIEVE-FRONTIER + NO-NOVELTY-CLAIM`.

This is a standard Selberg upper-bound sieve inserted into the exact `VIS-322`--`VIS-323` representation. No prime-pair asymptotic, lower bound, new sieve theorem, full worst-cell estimate, Wang natural-window theorem, or stronger RH criterion is claimed.

## 1. Standard translation-uniform prime-pair upper bound

Let `A` and `g!=0` be integers, and let `I` be an interval of `m` consecutive integers on which the two affine forms

`A+n`, `A+n+g`

are positive and larger than the sifting range. The classical dimension-two Selberg upper-bound sieve gives

`# {n in I : A+n and A+n+g are prime}`
` << S(g) m/log^2(3+m) + 1`,

where `S(g)` is the usual Hardy--Littlewood two-point singular series; for odd `g`, the count is already `O(1)` because two primes larger than `2` cannot differ by an odd integer.

The needed uniformity in the translating offset `A` is built into the elementary sieve setup. For squarefree `d`, the number of `n` in an interval for which

`d | (A+n)(A+n+g)`

is

`m rho_g(d)/d + O(rho_g(d))`,

with `rho_g(p)=2` for `p` not dividing `g` and `rho_g(p)=1` for `p|g`. The remainder is independent of the size or arithmetic position of `A`. Choosing an ordinary Selberg sifting level that is a fixed small power of `m` gives the displayed upper bound; replacing the truncated local factor by the full `S(g)` only weakens the upper bound.

This is classical sieve theory, not a Mathia-specific theorem. The Mathia-specific step is that the exact Wang branch geometry supplies precisely such translated fixed-gap intervals and controls the aggregate local factors across them.

## 2. Run lengths are all `L/k` except for one possible split class

Before the unique possible mechanical wrap, each residue class of the determinant index modulo `k` is a fixed-gap diagonal run. Among `L` consecutive determinant indices, every represented residue class contains either

`floor(L/k)` or `ceil(L/k)`

indices.

`VIS-322` shows that at most one residue class can wrap, splitting that class into two fixed-gap runs whose total length is at most `ceil(L/k)`. Every other run therefore has length comparable to

`T=L/k`.

There are at most `k+1` runs on one branch when `k<=L`.

## 3. The non-wrap runs sum at the target logarithmic scale

Apply the standard prime-pair upper bound to every non-wrap run. Since each such run has

`ell_s >= floor(L/k)`,

and `VIS-323` proves

`sum_s ell_s S(g_s) << L`,

one obtains

`sum_(s nonwrap) #prime-pairs(s)`
` << L/log^2(3+L/k) + k`.

The additive `k` is only the accumulated `O(1)` sieve remainder over at most `k` runs. The potentially large individual singular series do not accumulate: their length-weighted mass was already neutralized by `VIS-323`.

## 4. The unique wrap cannot reopen a singular-series loss

The wrap class may split into two runs with lengths `a,b` satisfying

`a+b <= ceil(L/k)`.

`VIS-323` also gives

`|g_s|<5k`

for every nonzero run gap. The standard Mertens bound for the prime-pair local factor therefore gives

`S(g_s) << log log(3k)`.

For two nonnegative lengths with `a+b<=T+1`,

`a/log^2(3+a) + b/log^2(3+b)`
` << T/log^2(3+T) + 1`.

Hence the two wrap pieces contribute at most

`<< log log(3k) T/log^2(3+T) + log log(3k)`.

Since

`log log(3k)/k << 1`,

and `T=L/k`, this is

`<< L/log^2(3+L/k) + k`.

Thus the one geometric discontinuity in the mechanical branch does not create a new arithmetic loss.

## 5. Branch occupancy bound

Combining the non-wrap and wrap estimates gives

`P_j << L/log^2(3+L/k) + k`

for every frozen branch and every `1<=k<=L` under the `VIS-322` hypotheses.

There are at most three branches, so the same estimate holds, up to an absolute constant, for the complete fixed-gate strip over one represented center `(u,v)`.

This estimate makes the remaining cost explicit. The sieve saving is controlled by the logarithm of the effective run length `L/k`; the only extra combinatorial term is the number of residue classes `k`.

## 6. Polynomially long runs already meet the Wang target

Now specialize to the natural central-shell scale

`L asymp M/log log M`.

Fix `delta>0` and assume

`k<=M^(1-delta)`.

Then

`L/k >> M^delta/log log M`,

so for sufficiently large `M`,

`log(3+L/k) >>_delta log M`.

Therefore

`L/log^2(3+L/k) <<_delta L/log^2 M`.

Also

`k / (L/log^2 M)`
` << M^(-delta) log^2 M log log M`
` = o_delta(1)`.

Hence

`P_j <<_delta L/log^2 M`.

In the `VIS-315`--`VIS-316` notation, a natural ratio cell has determinant width `D asymp M^2/V` and expected two-prime upper-bound scale `D/log^2 M`. Thus all represented centers with `k<=M^(1-delta)` satisfy the required cell scale with `A_M=O_delta(1)` individually. They cannot be responsible for an unbounded worst-cell excess.

The unresolved center-gap regime is consequently compressed to gaps larger than every fixed power-saving threshold: `k=M^(1-o(1))`. In that range the effective run length is only `M^(o(1))`, so a classical branchwise Selberg sieve no longer automatically supplies two powers of `log M`; when `k>L` even the residue-class averaging length disappears.

## Prior-art and novelty boundary

The upper bound for two prime translates is classical. Standard references include Henryk Iwaniec and Emmanuel Kowalski, *Analytic Number Theory*, AMS Colloquium Publications 53, Chapter 6 (elementary sieve methods), and John Friedlander and Henryk Iwaniec, *Opera de Cribro*, AMS Colloquium Publications 57, Chapters 7--8 (Selberg sieve and sifting many residue classes). These sources treat the general upper-bound sieve framework from which the two-linear-form estimate follows. Classical Brun/Selberg twin-prime bounds are special cases.

No novelty is claimed for the sieve theorem or for the fact that prime pairs have an `N/log^2 N` upper bound with the appropriate singular series. The Mathia-specific content is the insertion of that theorem into the exact Bézout/mechanical decomposition of `VIS-319`--`VIS-323`, which shows that the available run length `L/k` is sufficient throughout every fixed polynomial power-saving range and therefore isolates the genuinely hard center-gap scale.

## Boundaries and falsification

The result is an **upper bound only**. It does not show that any branch contains the expected number of prime pairs, and it does not control signs or phases of Wang coefficients.

The fixed `delta>0` is essential to the final `log^2 M` comparison. If `k=M^(1-o(1))`, then `log(L/k)` may be `o(log M)`, and the branchwise sieve can lose the logarithmic strength required by the natural-window target.

The estimate also does not solve `k>L`, where most residue classes contain at most one determinant index. That is a different averaging problem.

The proof uses the fixed-gate branch structure and unique-wrap statement from `VIS-321`--`VIS-322`; without those exact representation facts, a generic thin strip need not decompose into the same translated prime-pair intervals.

Falsify the claim by exhibiting an admissible `VIS-322` branch for which the residue classes do not have the stated run lengths, more than one class undergoes a gap-changing wrap, the standard dimension-two sieve is not translation-uniform for these intervals, or the `VIS-323` weighted singular-series estimate fails to control the recombined non-wrap runs.

## Dependencies

- `VIS-319`: unimodular Bézout chart preserving both prime-coordinate exclusions.
- `VIS-320`: at-most-three rational-rotation branches in the natural subperiod window.
- `VIS-321`: fixed-gate reduction up to bounded endpoint error.
- `VIS-322`: center-gap decimation and unique-wrap fixed-gap run decomposition.
- `VIS-323`: `O(L+k)` length-weighted singular-series mass and `|g_s|<5k`.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue owning the remaining Wang occupancy frontier.

## Research consequence

The run-length frontier is now sharply divided. For every fixed `delta>0`, center gaps `k<=M^(1-delta)` are already controlled at the natural two-prime upper-bound scale by a classical branchwise Selberg sieve. The live problem is no longer "can fixed-gap sieve theory help at all?" but whether one can bridge the **subpolynomial run-length regime** `L/k=M^(o(1))`, especially the transition to `k>L`, by a multi-run sieve, coefficient-weighted energy estimate, or another averaging direction that uses many short fragments together.

Do not spend further effort proving branchwise prime-pair upper bounds in polynomially long runs. The next coherent question starts only at the `k=M^(1-o(1))` boundary.