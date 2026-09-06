# VIS-059 — overlap collisions are periodic-cylinder masses

## Claim

Let `(G_t)_(t in Z)` be a stationary process on a finite alphabet `A`. For a fixed block length `m>=2`, define the overlapping block process

`Y_t=(G_t,...,G_(t+m-1))`

with stationary block law `P_m`, and put

`q_m = sum_(w in A^m) P_m(w)^2`,
`c_h = Pr(Y_0=Y_h)`.

For every overlap lag `1<=h<m`, the equality event `Y_0=Y_h` is exactly the event that the length-`m+h` word

`G_0 G_1 ... G_(m+h-1)`

has period `h`, meaning

`G_i=G_(i+h)` for every `0<=i<m`.

Equivalently,

`c_h = sum_(a in A^h) Pr(G_j = a_(j mod h) for 0<=j<m+h)`.

Thus the short-lag covariance terms in the empirical overlapping-block variance are not an amorphous dependence penalty: they are exact masses of finite periodic cylinders.

Now define the set of internally `h`-periodic `m`-blocks

`D_h^(m) = {w in A^m : w_i=w_(i+h) for 0<=i<m-h}`

and its population mass

`p_h = P_m(D_h^(m))`.

Because a length-`m+h` period-`h` collision necessarily begins with an internally period-`h` `m`-block,

`0 <= c_h <= p_h`.

Therefore the block law alone supplies the sharp interval-only envelope

`|c_h-q_m| <= B_h`,
`B_h := max(q_m, |p_h-q_m|)`.

The word "sharp" here is only relative to the information `c_h in [0,p_h]`: without additional extension probabilities, the farthest point of that interval from `q_m` is one of its endpoints. No claim is made that every endpoint value is realizable by a stationary process with the prescribed `P_m`.

For the active three-gap case `m=3`,

`c_1 = sum_(a in A) Pr(aaaa)`,
`c_2 = sum_(a,b in A) Pr(ababa)`,

while the triple-law envelopes use only

`p_1 = sum_(a in A) P_3(aaa)`,
`p_2 = sum_(a,b in A) P_3(aba)`.

Hence the two exceptional overlap terms in `VIS-058` are respectively controlled by constant-run triples and period-two triples before any long-lag mixing assumption enters.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL WORD-PERIOD STRUCTURE + DEPENDENCE-CERTIFICATE REFINEMENT + NO-NOVELTY-CLAIM`.

This does not provide a stochastic model for Riemann zeros, a long-lag mixing rate, a data-valid confidence interval for the unknown population block law, or an RH consequence.

## 1. Overlap equality is exactly a word-period condition

Write

`Y_0=(G_0,...,G_(m-1))`,
`Y_h=(G_h,...,G_(h+m-1))`.

The equality `Y_0=Y_h` means coordinatewise

`G_i=G_(i+h)` for `i=0,...,m-1`.

Those are precisely all period-`h` equalities required for the length `m+h` word from time `0` through `m+h-1`. No probabilistic argument is needed for this equivalence; stationarity is used only so that the block law and collision probabilities have the time-independent notation used in `VIS-058`.

Every period-`h` word is determined by its first `h` symbols. Summing the probabilities of the disjoint periodic cylinders indexed by `a=(a_0,...,a_(h-1)) in A^h` gives the displayed exact formula for `c_h`.

This also shows why an automatic "overlap reduces effective sample size" rule is too coarse. The overlap contribution depends on the actual periodic-cylinder masses of the process. Depending on the law, a short-lag collision can equal, exceed, or fall below the independent-copy collision level `q_m`.

## 2. The `m`-block law already gives a nontrivial short-lag envelope

The exact `c_h` depends on the length-`m+h` law, not merely on `P_m`. But equality of the two overlapping blocks forces the initial block itself to satisfy every internal period-`h` equality that fits inside length `m`.

Therefore

`{Y_0=Y_h} subseteq {Y_0 in D_h^(m)}`,

so `c_h<=p_h`. Positivity gives the interval `0<=c_h<=p_h`.

For a known scalar `q_m`, the largest possible value of `|x-q_m|` over `x in [0,p_h]` is

`max(q_m, |p_h-q_m|)`.

This yields `B_h`. The envelope can be much smaller than the fallback `b_h=1` used in `VIS-058` when internally periodic blocks are rare and the independent-copy collision probability is small.

The price is explicit. `p_h` is a property of the population block law. Replacing it by the same finite empirical table without accounting for its estimation error would move the uncertainty problem rather than solve it.

## 3. Three-gap overlap has two concrete periodic channels

For `m=3` and `h=1`, equality

`(G_0,G_1,G_2)=(G_1,G_2,G_3)`

forces

`G_0=G_1=G_2=G_3`.

Thus

`c_1=sum_a Pr(G_0=G_1=G_2=G_3=a)`.

The corresponding triple-law support condition is only `G_0=G_1=G_2`, so

`p_1=sum_a P_3(a,a,a)`.

For `h=2`, equality

`(G_0,G_1,G_2)=(G_2,G_3,G_4)`

forces the alternating word

`G_0 G_1 G_0 G_1 G_0`.

Hence

`c_2=sum_(a,b) Pr(G_0=a,G_1=b,G_2=a,G_3=b,G_4=a)`,

and its triple-law envelope is

`p_2=sum_(a,b) P_3(a,b,a)`.

So the two overlap corrections have a direct representation that can be inspected in the same fixed triple alphabet used by the Fisher residual experiment: constant-run mass and period-two return mass. Their exact values require one- and two-symbol extensions beyond the triple table; their safe intrinsic ceilings do not.

## 4. The `VIS-058` variance certificate can separate overlap from long memory

For `n>=3` consecutive overlapping triples, `VIS-058` gives

`V_n = E ||P_hat_n-P_3||_2^2`
` = (1/n^2) [ n(1-q_3) + 2 sum_(h=1)^(n-1) (n-h)(c_h-q_3) ].`

Suppose the underlying symbol process additionally has the `beta`-mixing envelope used there, so for `h>=3`,

`|c_h-q_3| <= beta(h-2)`.

Set

`B_1=max(q_3, |p_1-q_3|)`,
`B_2=max(q_3, |p_2-q_3|)`.

Then the same one-sided argument yields

`V_n <= Vbar_n^(per)`
` := (1/n^2) [ n(1-q_3)`
`    + 2(n-1)B_1`
`    + 2(n-2)B_2`
`    + 2 sum_(r=1)^(n-3) (n-r-2) beta(r) ].`

Compared with the coarse `b_1=b_2=1` fallback, this makes the certificate diagnose two qualitatively different sources of dependence: finite deterministic overlap geometry through `p_1,p_2`, and genuine separated-block dependence through the long-lag envelope.

Any valid upper bound on `V_n` can then enter the existing `VIS-058 -> VIS-057` chain unchanged: finite-support norm conversion gives a raw-law radius, `VIS-057` propagates it through the nonlinear Markov closure, and the observable residual-energy margin controls Fisher-direction error.

The same decomposition holds for general `m`: the exceptional lags `h<m` are periodic-cylinder channels, while nonoverlapping blocks begin at `h>=m` and may be controlled by whatever process dependence theorem is actually justified.

## 5. Prior art and novelty boundary

Periodicity and self-overlap of finite words are classical combinatorics on words. Guibas and Odlyzko, **Periods in strings**, *Journal of Combinatorial Theory, Series A* 30:1 (1981), 19–42, DOI `10.1016/0097-3165(81)90038-8`, studies periods precisely as shifts under which a word matches itself. Their companion paper, **String overlaps, pattern matching, and nontransitive games**, *Journal of Combinatorial Theory, Series A* 30:2 (1981), 183–208, DOI `10.1016/0097-3165(81)90005-4`, develops classical overlap/correlation structure for strings.

Accordingly, no novelty is claimed for the equivalence between an overlapping block matching its shift and a periodic word, nor for the language of periodic cylinders. `VIS-058` already records that empirical-measure covariance and mixing control are classical probability topics.

The durable Mathia-specific content is the interface between those two standard structures: the exceptional short-lag collision terms appearing in the exact overlapping-triple sampling variance are identified with concrete periodic channels, and the active three-gap certificate obtains a triple-law-only envelope before invoking any long-memory model.

## 6. Boundary conditions and falsification

The alphabet and block partition are fixed in advance. Changing bin edges, sparse-cell support, or symbolization changes `P_m`, `D_h^(m)`, and the periodic masses, so this theorem does not certify adaptive representations.

The exact formulas for `c_h` concern a genuine stochastic process law. A deterministic finite zeta window still does not become a repeated sample merely because its observed words can be counted. To use the envelope inferentially, one must justify a population/process model or another uncertainty construction and propagate uncertainty in `q_m` and `p_h` rather than treating empirical plug-in values as known constants.

The bound `c_h<=p_h` can be loose because an internally periodic `m`-block may fail to continue periodically for the extra `h` symbols required by `Y_0=Y_h`. A length-`m+h` law, a transition model, or direct extension probabilities can sharpen it. This is a feature of the boundary: it distinguishes what the current triple law determines from what only higher-order process information can determine.

Falsify the exact claim by giving a finite-alphabet sequence for which `Y_0=Y_h` at some `h<m` without the length-`m+h` segment having period `h`, or a stationary law with `c_h>p_h`. Either would contradict the deterministic event inclusion itself. A numerically weak `B_h` does not falsify the theorem; it only means the triple law alone is insufficiently informative for that process.

## Research consequence

`VIS-058` left the two overlap lags as separate finite-range terms to be computed or bounded directly. They now have a canonical form: for the active three-gap experiment they are the masses of `aaaa` and `ababa` cylinders, with safe ceilings already visible in the population triple law through the `aaa` and `aba` masses.

This removes one avoidable ambiguity from the higher-window uncertainty design without pretending to solve the real missing problem. A future zeta/CUE direction comparison should report or bound these periodic channels separately from its long-lag dependence model. If the short-lag terms dominate, the failure is local overlap geometry; if the long-lag term dominates, additional process structure is required. The next independent step remains empirical/process-level: obtain a defensible uncertainty law for the finite higher-window data rather than extending the Fisher algebra again.
