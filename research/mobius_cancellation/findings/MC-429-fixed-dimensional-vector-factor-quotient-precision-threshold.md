# MC-429 — Fixed-dimensional vector factor quotients obey a dimension–precision threshold

**Evidence:** `EXACT-DERIVED · NEGATIVE/OBSTRUCTION · CLASSICAL-INGREDIENTS · FRONTIER-ADVANCE · PRIOR-ART-AUDITED · NO-NOVELTY-CLAIM · NON-RH`

## Claim

`MC-428` shows that a permutation-invariant **scalar** quantized factor-size channel has only subpolynomial state volume until its logarithmic mesh reaches the inverse-`log X` scale. It explicitly leaves open several retained coordinates, where the correct orbit count becomes a vector-partition problem.

That escape can be priced exactly enough to expose a dimension–precision law.

Let `n<=X` be squarefree, write `r=omega(n)`, and consider every ordered active factorization

\[
n=u_1\cdots u_d,
\qquad
1\le d\le r,
\qquad
u_j>1.
\tag{1}
\]

Fix an integer `k>=1`, independent of `X`. Retain each factor through a nonnegative integer vector

\[
q(u_j)=(q_{j,1},\ldots,q_{j,k})\in\mathbf Z_{\ge0}^k,
\tag{2}
\]

and suppose the downstream observable is invariant under permutations of the factor slots, so the raw retained state is the unordered multiset

\[
\{q(u_1),\ldots,q(u_d)\}.
\tag{3}
\]

Assume only the total budget

\[
\sum_{j=1}^d\|q(u_j)\|_1\le S.
\tag{4}
\]

Then the number `N_{k,\rm sym}(S,r)` of possible orbit states `(3)` satisfies

\[
\boxed{
N_{k,\rm sym}(S,r)
\le
(r+1)\exp\!\bigl(C_k S^{k/(k+1)}\bigr)
}
\tag{5}
\]

for a constant `C_k>0` depending only on `k`.

Consequently, consider `k` nonnegative additive factor channels

\[
A_\ell(u)=\sum_{p\mid u}w_\ell(p),
\qquad w_\ell(p)\ge0,
\tag{6}
\]

quantized at a common mesh `eta>0` by

\[
q_{j,\ell}=\left\lfloor\frac{A_\ell(u_j)}{\eta}\right\rfloor.
\tag{7}
\]

If their total masses satisfy, for fixed constants `C_\ell`,

\[
W_\ell(n):=\sum_{p\mid n}w_\ell(p)\le C_\ell\log X,
\qquad 1\le\ell\le k,
\tag{8}
\]

then with `C=\sum_\ell C_\ell`,

\[
S\le C\frac{\log X}{\eta}.
\tag{9}
\]

Hence for every fixed `delta<1/k`,

\[
\eta^{-1}\le(\log X)^{\delta+o(1)}
\tag{10}
\]

implies

\[
\boxed{N_{k,\rm sym}=X^{o(1)}}.
\tag{11}
\]

Conversely, if for some fixed `alpha>0` the symmetric vector channel carries at least `X^alpha` states along an unbounded sequence of `X`, then `(5)` and `(9)` force

\[
\boxed{
\eta^{-1}\ge c_{k,\alpha,C}(\log X)^{1/k}
}
\tag{12}
\]

for some constant `c_{k,\alpha,C}>0` along that sequence.

Thus a fixed number of retained coordinates can lower the first possible polynomial-capacity precision threshold, but only according to

\[
\boxed{
\text{fixed dimension }k
\quad\Longrightarrow\quad
\text{necessary inverse precision at least }(\log X)^{1/k}.
}
\tag{13}
\]

For `k=1`, this recovers the inverse-`log X` scale of `MC-428` up to the sharp scalar constant proved there. For `k=2`, polynomial orbit capacity already requires inverse precision on at least the square-root-`log X` scale. No fixed `k` permits constant or sub-`(log X)^{1/k}` precision to generate polynomially many permutation-invariant factor states.

This is a state-capacity obstruction only. It gives no new estimate for `M(x)` and no RH consequence.

## Exact vector-partition reduction

Delete every zero vector from the multiset `(3)` and record separately the number `z` of deleted entries. Since `d<=r`, there are at most `r+1` choices for `z`.

For each remaining vector `v\in\mathbf Z_{\ge0}^k\setminus\{0\}`, define its scalar weight

\[
|v|=v_1+\cdots+v_k.
\tag{14}
\]

There are exactly

\[
a_t
=
\#\{v\in\mathbf Z_{\ge0}^k:|v|=t\}
=
\binom{t+k-1}{k-1}
\tag{15}
\]

distinct vector types of weight `t`. Therefore the number `P_k(s)` of unordered multisets of nonzero `k`-vectors with total scalar weight exactly `s` has generating function

\[
F_k(z)
:=
\sum_{s\ge0}P_k(s)z^s
=
\prod_{t\ge1}(1-z^t)^{-a_t}.
\tag{16}
\]

This is the standard weighted-partition generating function with polynomially growing part multiplicities `a_t\asymp_k t^{k-1}`.

It remains only to obtain a sufficiently strong elementary upper bound. Put `z=e^{-\tau}` with `0<\tau<=1`. Then

\[
\log F_k(e^{-\tau})
=
\sum_{m\ge1}\frac1m
\left[
(1-e^{-\tau m})^{-k}-1
\right],
\tag{17}
\]

because

\[
\sum_{t\ge0}\binom{t+k-1}{k-1}x^t=(1-x)^{-k}.
\tag{18}
\]

For `0<y<=1`,

\[
(1-e^{-y})^{-k}-1\ll_k y^{-k},
\tag{19}
\]

while for `y>=1` the same expression is `O_k(e^{-y})`. Splitting the `m`-sum at `m=1/\tau` therefore gives

\[
\log F_k(e^{-\tau})
\le A_k\tau^{-k}
\tag{20}
\]

for some constant `A_k`.

Since every coefficient of `F_k` is nonnegative,

\[
\sum_{s\le S}P_k(s)
\le
\exp(\tau S)F_k(e^{-\tau}).
\tag{21}
\]

For `S>=1`, choosing `\tau=S^{-1/(k+1)}` in `(20)`--`(21)` yields

\[
\sum_{s\le S}P_k(s)
\le
\exp\!\bigl(C_kS^{k/(k+1)}\bigr).
\tag{22}
\]

Multiplying by the `r+1` possible zero-vector multiplicities proves `(5)`.

For the additive specialization `(6)`--`(9)`, flooring cannot increase the coordinate totals:

\[
\sum_j q_{j,\ell}
\le
\left\lfloor\frac{W_\ell(n)}{\eta}\right\rfloor.
\tag{23}
\]

Summing over `ell` gives `(9)`. Under `(10)`, equation `(5)` gives

\[
\log N_{k,\rm sym}
\ll_k
(\log X)^{(1+\delta)k/(k+1)+o(1)}
+\log(r+1).
\tag{24}
\]

Since `delta<1/k`, the exponent of `log X` in the first term is strictly less than one. Also `r<=\log X/\log2`, so `\log(r+1)=O(\log\log X)`. This proves `(11)`.

If instead `N_{k,\rm sym}>=X^\alpha`, then `(5)` and `(9)` imply

\[
\alpha\log X
\le
C'_k\left(\frac{\log X}{\eta}\right)^{k/(k+1)}
+O(\log\log X),
\tag{25}
\]

with the fixed total-mass constant absorbed into `C'_k`. Rearranging gives `(12)`.

## Relation to the current frontier

`MC-426` rules out fixed-dimensional **bounded** additive factor summaries even before quotienting factor order. `MC-427` shows that unbounded nonnegative additive data with insufficient quantized total mass still has subpolynomial ordered state volume. `MC-428` then proves a much stronger scalar statement after quotienting artificial factor-slot permutations: scalar log-size needs inverse-`log X` precision before polynomial orbit capacity is possible.

The vector-coordinate loophole left open by `MC-428` is real but quantitatively limited. A second, third, or other fixed number of additive coordinates genuinely enlarges the orbit space because a part of scalar weight `t` can now have `binom(t+k-1,k-1)` vector types. That changes the partition entropy law from `sqrt(S)` to `S^{k/(k+1)}`. It does **not** make precision free.

This produces a concrete representation audit for proposed factor lifts. If the downstream construction is symmetric in factor slots and retains `k` fixed nonnegative additive channels whose total quantized mass is `O(log X/eta)`, then before assigning analytic significance to their apparent state richness one must pay the dimension–precision threshold `(12)`. Increasing the number of coarse channels and increasing the precision of a small number of channels are two interchangeable capacity resources at this combinatorial level.

The remaining escapes are now narrower: dimension growing with `X`; channels whose total variation is larger than `O(log X/eta)`; signed coordinates with large hidden positive/negative variation; exact factor identity; intrinsically asymmetric factor roles; or genuinely nonadditive/relational data. Each escape still has to survive the later coefficient, shell, Cauchy, and positivity operations before it can count as cancellation-relevant information.

## Prior art and novelty boundary

The partition theory is classical. P. A. MacMahon, *The Enumeration of the Partitions of Multipartite Numbers*, Proceedings of the Cambridge Philosophical Society **22** (1925), 951--963, DOI `10.1017/S0305004100014547`, is an early systematic source on multipartite/vector partition enumeration.

The generating function `(16)` is a standard weighted-partition product. Modern Meinardus-type treatments explicitly study products of the form

\[
\prod_{t\ge1}(1-z^t)^{-b_t}
\]

and polynomially growing part-type counts. See Boris L. Granovsky and Dudley Stark, *Developments in the Khintchine--Meinardus Probabilistic Method for Asymptotic Enumeration*, Electronic Journal of Combinatorics **22** (2015), P4.32, DOI `10.37236/4581`, and Dudley Stark, *The asymptotic number of weighted partitions with a given number of parts*, Ramanujan Journal **57** (2022), 949--967, DOI `10.1007/s11139-020-00350-2`. In this classical framework, weights `b_t\asymp t^{k-1}` naturally lead to logarithmic counting scale `s^{k/(k+1)}`.

No novelty is claimed for vector partitions, weighted-partition generating functions, Meinardus asymptotics, or the exponent `k/(k+1)`. The proof above deliberately uses only a crude exponential generating-function bound rather than invoking a sharp asymptotic.

The durable contribution is the **mechanism-specific frontier consequence**: after quotienting factor-slot permutations, a fixed-dimensional quantized additive factor lift has an explicit dimension–precision capacity boundary, and the scalar inverse-log threshold of `MC-428` is the first member of the general law `(13)`.

## Limits and decisive test

- **Fixed `k` is load-bearing.** The constant in `(5)` depends on `k`; no uniform conclusion is claimed when the retained dimension grows with `X`. That is a genuine remaining escape and must be priced separately.
- **Permutation invariance is load-bearing.** Intrinsically asymmetric factor variables should not be quotiented merely because they appear in a product decomposition.
- **Nonnegative total budget is load-bearing.** Signed additive channels require control of positive/negative variation. A small final signed sum does not imply a small state budget.
- **The `O(log X)` mass specialization is not automatic.** A concrete retained coordinate must prove `(8)` or supply its actual mass scale; otherwise only the abstract bound `(5)` applies.
- **Vector state capacity is not analytic usefulness.** Passing `(12)` gives no Möbius cancellation theorem, character estimate, Fourier independence, or positive-kernel gain.
- **Arithmetic realizability was discarded.** The weighted-partition count allows vector multisets that may not arise from partitioning the prime factors of one integer. Enforcing realizability can only decrease the state family.
- **Exact factor identities remain outside the theorem.** Infinite precision can encode the integer factors themselves and is not a coarse summary.

The next first-kill test for a symmetric factor-lift proposal is therefore explicit: identify the fixed retained dimension `k`, prove the actual total quantized mass `S`, and compare it with `(5)`. If the proposal survives only by letting `k` grow, retaining hidden signed variation, or using exact/nonadditive data, that extra structure must be named and justified as canonical before any polynomial state count is credited as a route to Möbius cancellation.