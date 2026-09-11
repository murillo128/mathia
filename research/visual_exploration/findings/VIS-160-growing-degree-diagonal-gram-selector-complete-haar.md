# VIS-160 — a deterministic growing-complexity Gram selector can pass every fixed finite-order Haar test

## Claim

Let `g_k` be the Gram points and let

`z_k=(p^(-i g_k))_p in Omega`

be the full prime-phase state. There exists a strictly increasing deterministic integer selector

`K : N -> N`

whose local polynomial degree tends to infinity, such that for

`w_n=z_(K(n))`

the following holds.

For every fixed `r>=1`, every fixed distinct integer offsets `b_1,...,b_r`, and every fixed finite set of primes `P`, the joint population

`(w_(n+b_1)|_P,...,w_(n+b_r)|_P)`

is Haar-equidistributed on `(T^P)^r`.

Thus one deterministic sampled Gram clock can pass **every fixed finite-order prime-phase Haar test**, even though it introduces no new arithmetic source beyond the Gram clock and the original prime phases.

The construction is diagonal and deliberately adversarial. It does **not** show that a natural prescribed growing-complexity selector has the same property, and it gives no quantitative uniformity when sample order, prime support, character complexity, or selector complexity grow together with height.

**Evidence/status:** `EXACT-DERIVED + NEGATIVE/CONTROL + CLASSICAL-DIAGONALIZATION/CUD-ANALOGUE + NO-NOVELTY-CLAIM`.

## 1. Enumerate every fixed finite-dimensional character test

A fixed finite-prime joint-Haar assertion is equivalent, by multidimensional Weyl's criterion, to vanishing of every nontrivial character average.

Enumerate all such tests as

`T_1,T_2,...`.

A test `T_q` specifies:

- a fixed sample order `r_q`;
- fixed distinct integer offsets `b_(q,1),...,b_(q,r_q)`;
- a fixed finite prime support;
- a nonzero integer character on the corresponding product torus.

This family is countable. Reorder the enumeration so that

`r_q<=q`.

For degree `j` and test `q<=j`, define the degree-`j` polynomial-clock character sequence

`u_(j,q)(n)=chi_q(z_((n+b_(q,1))^j),...,z_((n+b_(q,r_q))^j))`.

`VIS-158`, applied to the polynomial selector `P(n)=n^j`, gives

`(1/M) sum_(n<=M) u_(j,q)(n) -> 0`

for every `q<=j`, because `r_q<=q<=j`.

This is the only Gram-specific input needed below.

## 2. Choose stage boundaries after the required tests have converged

Put

`epsilon_j=2^(-j)`.

For each `j`, there are only finitely many tests `q<=j`. Therefore choose integers

`1<N_1<N_2<...`

recursively so that all of the following hold:

1. for every `q<=j` and every `M>=N_j-1`,

   `|(1/M) sum_(n<=M) u_(j,q)(n)| <= epsilon_j`;

2. `N_(j+1)>=2^j N_j`;

3. `N_j` is larger than the absolute values of all offsets occurring in `T_1,...,T_j`, plus a fixed safety margin.

The first condition is possible because each of the finitely many degree-`j` character averages converges to zero. The other conditions only require increasing the boundary further.

Now define a stage-degree function

`d(n)=j` for `N_j<=n<N_(j+1)`

and the selector

`K(n)=n^(d(n))`.

Inside each stage `K` is increasing. Across a boundary,

`K(N_(j+1)-1)=(N_(j+1)-1)^j < N_(j+1)^(j+1)=K(N_(j+1))`,

so `K` is strictly increasing globally.

## 3. Stage boundaries have zero density

Fix one character test `T_q` and put

`B_q=max_l |b_(q,l)|`.

Away from the `B_q`-neighborhood of a stage boundary, all shifted indices `n+b_(q,l)` lie in the same stage. Hence for `n` in stage `j`, away from those boundary neighborhoods,

`chi_q(w_(n+b_(q,1)),...,w_(n+b_(q,r_q))) = u_(j,q)(n)`.

Up to the beginning of stage `J`, the number of exceptional indices is at most `O(B_q J)`. But the imposed growth gives at least superexponential stage locations:

`N_J >= N_1 2^(1+2+...+(J-1))`.

Therefore

`J/N_J -> 0`,

and every fixed test loses only a zero-density set to stage-boundary crossings.

## 4. Every fixed character average vanishes

Let

`S_(j,q)(M)=sum_(n<=M) u_(j,q)(n)`.

For `j>=q` and `M` inside stage `j`, the choice of `N_j` gives

`|S_(j,q)(M)-S_(j,q)(N_j-1)|`
` <= epsilon_j M + epsilon_j(N_j-1)`
` <= 2 epsilon_j M`.

Let `C_q(M)` be the cumulative character sum for the actual piecewise selector `K`. Apart from the zero-density boundary corrections from the previous section,

`|C_q(M)|/M`
` <= |C_q(N_j-1)|/M + 2 epsilon_j + o(1)`

for `N_j<=M<N_(j+1)`.

At the end of the stage, the entire earlier history has relative mass at most

`N_j/N_(j+1) <= 2^(-j)`.

Consequently the endpoint averages tend to zero. Feeding that endpoint estimate into the displayed within-stage bound gives, uniformly through each later stage,

`C_q(M)/M -> 0`.

The finitely many early stages `j<q` do not affect the limit.

Since `q` was arbitrary, every enumerated nontrivial finite-dimensional character has zero empirical average. Multidimensional Weyl's criterion therefore yields Haar equidistribution for every fixed sample order, fixed offset pattern, and fixed finite prime support.

## 5. What this closes

`VIS-157`--`VIS-159` showed that a fixed selector of increasing algebraic complexity can imitate Haar behavior through an arbitrarily high but still fixed finite order before a deterministic clock character appears one order later.

The present diagonal construction removes a tempting residual escape: **merely allowing selector complexity to grow with height is not enough**. One can schedule increasing polynomial degrees so that every fixed finite-order test is eventually placed below the current degree threshold and hence is washed out, while the selector remains fully deterministic.

This is the prime-phase analogue of the classical warning supplied by completely uniformly distributed sequences: deterministic constructions can pass all fixed finite-dimensional uniform-distribution tests. Emilio Almansi and Verónica Becher, *Completely uniformly distributed sequences based on de Bruijn sequences*, Mathematics of Computation 89 (2020), 2537–2551, DOI `10.1090/mcom/3534`, gives a modern deterministic CUD construction and a Weyl-criterion proof. The general deterministic-CUD phenomenon is therefore prior art; no novelty is claimed for diagonalization or for complete uniform distribution itself.

The Mathia-specific value is narrower: it composes the exact Gram-clock controls of `VIS-158` into one increasing selector and shows that **all fixed-order prime-phase Haar appearances can coexist with a purely deterministic observation clock**.

## Boundary and falsification

The construction is existential and adversarial. The boundaries `N_j` are chosen after the finitely many degree-`j` character tests have reached prescribed accuracy. No usable rate for `N_j` is claimed.

The theorem does not provide uniform control for tests whose order, offsets, prime support, Fourier/character complexity, or required accuracy grow with the observation height. Such a jointly growing test can still distinguish the diagonal selector because the construction guarantees only one fixed test at a time in the eventual limit.

The result also does not classify a natural pre-specified selector such as a particular explicit `d(n)`, `alpha(n)`, regularly varying rule, or source-driven/data-dependent subsequence. Those require their own quantitative sampled-clock law rather than this diagonal existence argument.

No claim is made for joint observables containing `zeta`, Hardy `Z`, derivatives, zero occupancy, nearby-zero geometry, or another analytic coordinate not measurable from the fixed-prime phase state. Haar empirical distribution here is deterministic and is not stochastic independence or mixing. Nothing here implies RH or a stronger zeta criterion.

Falsify the result by finding a fixed finite-prime product character omitted by the countable enumeration, a failure of the `VIS-158` degree-`j` Haar theorem for one enumerated test, a positive-density stage-boundary contribution, or a defect in the diagonal block-average estimate.

## Visual consequence

No canonical PNG is retained. Any finite-dimensional visual panel built only from fixed prime phases and fixed offsets can be made asymptotically Haar-looking by this deterministic growing-complexity selector. A further scatter plot would therefore be weaker than the exact character control.

## Research consequence

The accepted `CLUE-zeta-prime-phase-recursive-geometry` should no longer list generic "selector complexity growing with height" as an information escape. A surviving sampling-based route must impose **quantitative, pre-specified structure** that the diagonal clock cannot satisfy—for example a coupled test whose dimension/support/character complexity grows with height at a controlled rate—or else add an independently anchored analytic coordinate whose information is not determined by the sampled prime-phase clock.