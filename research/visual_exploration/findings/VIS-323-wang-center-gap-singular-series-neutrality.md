# VIS-323 — center-gap decimation is singular-series neutral before the maximally fragmented regime

## Claim

Keep the fixed-gate branch decomposition of `VIS-322`. Thus

`gcd(u,v)=1`, `u != v`,

`M/2 < u,v,q,r <= 2M`,

`h=qv-ur`, `|h|<=D`,

and put

`k=|v-u|`, `L=2 floor(D)+1`.

Assume the same subperiod condition

`L<max(u,v)`.

For one frozen branch `j`, decimation by residue class modulo `k` produces fixed-gap diagonal runs

`(q,r)=(Q+n sigma,R+n sigma)`,

where `sigma=sign(v-u)`, and the branch contains at most `min(k,L)+1` such runs. Let `g_s=R_s-Q_s` and `ell_s` be the fixed gap and length of run `s`.

Then the exact Bézout geometry forces much more than a run-count bound.

First, all run gaps of one branch lie in an integer interval of width `<k+1`, and every nonzero run gap satisfies

`|g_s|<5k`.

Second, the determinant residue and the prime-pair gap are the same coordinate modulo `k`:

`u g_s == -h (mod k)`.

Since `gcd(u,k)=1`, distinct determinant residue classes give distinct gap residue classes modulo `k`; the only possible repeated residue is the unique wrap class, whose two possible gaps differ by exactly `k`.

Third, if `S(g)` denotes the usual Hardy--Littlewood singular series for the pair `(n,n+g)`, with `S(g)=0` for odd `g`, then uniformly in the represented center and branch,

`sum_s S(g_s) << k+1`,

and therefore

`sum_s ell_s S(g_s) << L+k`.

In the non-maximally-fragmented regime

`k<=L`,

this becomes

`sum_s ell_s S(g_s) << L`.

Thus center-gap fragmentation does **not** produce an additional aggregate singular-series loss while `k<=L`: even though individual even gaps can carry large local factors, the total local-factor mass of all diagonal pieces is only proportional to the original determinant-window length after weighting by run length.

The remaining near-diagonal difficulty is therefore not exceptional growth of prime-pair singular series across the fragments. It is the **sieve-depth/run-length problem**: as `k` grows, each residue class contains only about `L/k` points, eventually leaving too little length for a useful fixed-gap prime-pair sieve before the maximally fragmented regime `k>L` is reached.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL PRIME-PAIR SINGULAR-SERIES AVERAGING + REPRESENTATION-REDUCTION + SIEVE-FRONTIER + NO-NOVELTY-CLAIM`.

No prime-pair asymptotic, uniform short-interval sieve theorem, Wang natural-window estimate, or stronger RH criterion is proved here.

## 1. Every diagonal run carries a small fixed gap

Use the canonical Bézout representative of `VIS-321`--`VIS-322`,

`au-bv=1`, `0<a<v`, `0<=b<u`,

and

`(q_j(h),r_j(h))=(u t_j(h)-bh, v t_j(h)-ah)`,

`t_j(h)=floor(U(h))-j`.

Suppose first that `v>u`. Put

`k=v-u`, `d=a-b`.

The identities from `VIS-322` give

`a/v=d/k-1/(kv)`.

Since

`U(h)=2M/v+(a/v)h`,

the fixed gap on the branch at determinant index `h` is

`g_j(h)=r_j(h)-q_j(h)`
` = k t_j(h)-d h`
` = 2Mk/v - h/v - k({U(h)}+j)`.

If instead `u>v`, put

`k=u-v`, `d=b-a`.

Then

`b/u=d/k+1/(ku)`,

and

`U(h)=2M/u+(b/u)h`.

Now

`g_j(h)=r_j(h)-q_j(h)`
` = -k t_j(h)+d h`
` = -2Mk/u - h/u + k({U(h)}+j)`.

In either orientation, as `h` ranges over the determinant window, the variable part contributed by the phase has width `<k`, while the affine `h/max(u,v)` term has width `<1` under the subperiod condition. Therefore the run gaps of one branch lie in one real interval of width `<k+1`.

Moreover `M/2<max(u,v)<=2M`, `j<=2`, `0<={U(h)}<1`, and `|h|/max(u,v)<1/2`. The displayed formulae therefore give the crude but uniform bound

`|g_j(h)|<5k`

for every nonzero branch gap.

At the natural Wang scale `D=O(M/log log M)`, zero gap is absent for sufficiently large `M`: if `q=r`, then

`|h|=|q(v-u)|=qk>M/2`,

whereas `D=o(M)`.

## 2. Determinant residue and prime-pair gap are the same `k`-coordinate

The decimation parameter is not merely a geometric partition. It also determines the pair shift modulo `k`.

When `v>u`, write `v=u+k` and `r=q+g`. Then

`h=qv-ur`
` = q(u+k)-u(q+g)`
` = qk-ug`.

When `u>v`, write `u=v+k`. Then

`h=qv-(v+k)(q+g)`
` = -qk-ug`.

Hence in both cases

`u g == -h (mod k)`.

Because

`gcd(u,k)=gcd(u,|v-u|)=gcd(u,v)=1`,

the map from determinant residue `h mod k` to gap residue `g mod k` is a bijection.

`VIS-322` showed that a `k`-step normally changes `(q,r)` by `(sigma,sigma)`, so `g` remains fixed. At the unique possible wrap the increment is

`(sigma,sigma)-sigma(u,v)`.

The corresponding gap change is therefore

`-sigma(v-u)=-k`.

Thus one residue class may contribute two gap values differing by exactly `k`, and no other duplication modulo `k` is possible.

This is the exact link between the combinatorial fragmentation parameter and the arithmetic shift entering a prime-pair sieve.

## 3. The singular-series mass of all run gaps is only `O(k)`

For nonzero even `g`, expand the standard pair singular series as

`S(g)`
` = 2 C_2 sum_(d|g, d odd squarefree) a(d)`,

with

`a(d)=product_(p|d) 1/(p-2)`.

All coefficients are nonnegative.

Let `I` be any integer interval containing the run gaps of one branch and put

`N_I = # (I cap Z)`.

From the first section, `I` may be chosen with `N_I<k+2` and with every nonzero element satisfying `|g|<5k`.

For an odd squarefree `d`, the number of even multiples of `d` in `I` is at most

`N_I/(2d)+1`.

Therefore

`sum_(g in I, g != 0) S(g)`
` <= 2 C_2 [ (N_I/2) sum_d a(d)/d + sum_(d<=5k) a(d) ]`.

The first Euler product is convergent and in fact

`sum_d a(d)/d`
` = product_(p>2) (1+1/[p(p-2)])`
` = 1/C_2`.

For the second term,

`sum_(d<=5k) a(d)`
` <= product_(3<=p<=5k) (1+1/(p-2))`
` << log(2+k)`,

by the classical reciprocal-prime/Mertens estimate, since

`log(1+1/(p-2))=1/p+O(1/p^2)`.

Hence

`sum_(g in I, g != 0) S(g) << k+log(2+k) << k+1`.

The actual run gaps form only a subset of `I`, so positivity gives

`sum_s S(g_s) << k+1`.

This is a finite uniform upper bound, not an asymptotic statement and not an appeal to a prime-pair conjecture.

## 4. Weighting by run length removes the local-factor fragmentation cost

The determinant window contains `L` consecutive integer indices.

Every residue class modulo `k` therefore contains at most

`ceil(L/k)`

indices. A fixed-gate run is contained in one such class. The unique wrap class may split into two runs, but each run separately still has length at most `ceil(L/k)`.

Thus

`sum_s ell_s S(g_s)`
` <= ceil(L/k) sum_s S(g_s)`
` << ceil(L/k)(k+1)`
` << L+k`.

When `k<=L`, this becomes

`sum_s ell_s S(g_s) << L`.

The same estimate holds separately for each `j=0,1,2`, so summing the at-most-three branches changes only the absolute constant.

This matters because a standard upper-bound sieve for one fixed-gap run is naturally weighted by its pair singular series. If one bounds every run separately and then recombines them, the local-factor part of that recombination is therefore harmless in aggregate for `k<=L`. The cost that remains is whether a run of length only `O(L/k)` is long enough for the available sieve theorem to deliver the desired logarithmic saving uniformly in the moving offset and gap.

No sieve theorem is invoked here to assert such a saving. The result isolates which component of the decomposition can no longer be blamed for failure.

## 5. Consequence for the center-gap split

The center-gap frontier from `VIS-322` now separates into three structural scales.

For `k` small relative to `L`, there are few long runs. Their total singular-series mass is controlled, and classical fixed-gap upper-bound sieve methods are the natural next tool.

For intermediate `k<=L`, there can be many shorter runs, but the aggregate local-factor weight remains `O(L)`. A failure here must come from loss of usable run length, uniformity in the moving family, or from paying sieve/remainder constants separately on too many short intervals -- not from a hidden accumulation of large singular series.

For `k>L`, the determinant segment has at most one sampled index in most residue classes. Center-gap decimation no longer creates averaging length, and the estimate `O(L+k)` is too weak to compress the fragmentation. This remains the genuinely maximally fragmented regime and may require the coefficient-weighted energy route, a multi-run sieve, or another averaging mechanism across represented centers.

Thus the natural next parameter is not merely the number of diagonal pieces. It is the ratio

`L/k`,

which measures the sieve depth available per center-gap residue class after the exact representation reduction.

## Prior-art and novelty boundary

The prime-pair singular series and its average behavior are classical. P. X. Gallagher, **On the distribution of primes in short intervals**, *Mathematika* 23 (1976), 4--9, DOI `10.1112/S0025579300016442`, established the foundational average-singular-series phenomenon used throughout prime-tuple heuristics and sieve comparisons. D. A. Goldston and Ade Irma Suriajaya, **A singular series average and the zeros of the Riemann zeta-function**, *Acta Arithmetica* 200 (2021), 71--90, DOI `10.4064/aa200821-24-2`, study refined Riesz/Cesàro averages of the pair singular series and their zeta-zero terms.

The bound above does not claim a new general singular-series average theorem. It uses only the elementary positive divisor expansion of the two-point singular series, the fact that the `VIS-322` run gaps occupy one interval of length `O(k)`, and the exact residue dictionary `u g == -h (mod k)` forced by the Wang Bézout coordinates. The Mathia-specific content is that this classical arithmetic weight is automatically neutralized by the exact center-gap decomposition before the regime becomes maximally fragmented.

The reciprocal-prime estimate used to bound the finite Euler product is classical Mertens-level prior art already anchored in `SOURCES.md`.

## Boundaries and falsification

The statement is an aggregate **singular-series** bound, not a bound for actual primes. It does not imply

`# {n in run : Q+n and R+n prime} << ell_s S(g_s)/log^2 M`

uniformly for every very short run; establishing a sufficiently uniform upper-bound sieve with acceptable remainder is precisely the next issue.

The argument treats the standard two-point singular series. Additional arithmetic structure in the moving offsets `(Q,R)`, correlations between different runs, or the deterministic Wang coefficients/phases may matter in a later aggregate estimate and are not controlled here.

The useful `O(L)` weighted bound is asserted only for `k<=L`. When `k>L`, a branch may already be point-fragmented, and the present interval-average argument does not create a new averaging direction.

The zero-gap exclusion uses the natural asymptotic Wang scale. If a non-natural wider determinant window admits `g=0`, remove that degenerate diagonal separately rather than assigning it the ordinary pair singular series.

Falsify the exact claim by finding an admissible fixed-gate branch for which its run gaps cannot be contained in an interval of width `<k+1`, the congruence `u g == -h (mod k)` fails, the wrap changes the gap by something other than `-k`, or the displayed positive-divisor estimate fails for the resulting finite gap set.

## Dependencies

- `VIS-319`: supplies the exact unimodular Bézout chart preserving both prime-coordinate exclusions.
- `VIS-320`: supplies the at-most-three rational-rotation branches and subperiod natural window.
- `VIS-321`: freezes the moving gate up to a bounded correction and identifies the unimodular mechanical path.
- `VIS-322`: supplies center-gap decimation, the unique-wrap statement, and the `min(k,L)+1` fixed-gap run decomposition.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue owning the remaining natural-window occupancy frontier.

## Research consequence

For `k<=L`, do not spend another step trying to control unusually large singular-series factors run by run: their total length-weighted contribution is already `O(L)`. The next useful theorem should quantify **how much fixed-gap sieve saving survives on runs of length about `L/k`**, uniformly in the moving offsets/gaps generated by the Wang branches, and then recombine that bound through the known center-gap and destination-taper weights.

A useful next split is therefore by sieve depth `L/k`, not by singular-series size. If existing short-interval upper-bound sieve technology loses too much as `L/k` shrinks, locate the threshold in `k`; below it, classical fixed-gap sieving should suffice in principle, while above it one should stop treating the pieces independently and switch to a multi-run or coefficient-weighted aggregation.
