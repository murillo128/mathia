# MC-368 — Prime-shell bias is a subset-sum side channel

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The live frontier after `MC-366`--`MC-367` is to price the provenance of a **concrete arithmetic transcript**, rather than another abstract information channel. The most immediate transcript in the exact reciprocal endpoint is already present in `MC-296`: the normalized prime-shell character bias itself. Its information content is governed by an exact subset-sum problem in the endpoint defect-cell multiplicities.

Continue the exact endpoint partition of `MC-296`. Let

\[
\mathcal R_y=D_1\sqcup\cdots\sqcup D_R,
\qquad
n_i:=|D_i|>0,
\qquad
N:=|\mathcal R_y|=\sum_{i=1}^R n_i,
\qquad
d_i:=\frac{n_i}{N}.
\tag{1}
\]

Assume `R` is even, so the source-coordinate map used in `MC-338`--`MC-342` identifies the nonprincipal modes with

\[
X=(X_1,\ldots,X_R)
\sim \operatorname{Unif}\!\left(\{\pm1\}^R\setminus\{(+1,\ldots,+1)\}\right).
\tag{2}
\]

For a mode `a`, the actual prime-shell character sum is

\[
S(a):=\sum_{r\in\mathcal R_y}\chi_a(r)
=\sum_{i=1}^R n_i X_i(a),
\tag{3}
\]

and its normalized bias is

\[
T(a):=\frac{S(a)}N
=\sum_{i=1}^R d_i X_i(a).
\tag{4}
\]

If

\[
J(a):=\{i:X_i(a)=-1\},
\]

then, because `sum_i d_i=1`, one has

\[
\boxed{
T(a)=1-2d(J(a)),
\qquad
d(J):=\sum_{i\in J}d_i.
}
\tag{5}
\]

Thus the raw arithmetic scalar transcript `T` is exactly a subset-sum encoder for the endpoint source state.

Two consequences are sharp and point in opposite directions.

First, if the defect masses have distinct subset sums,

\[
J\ne K
\quad\Longrightarrow\quad
d(J)\ne d(K),
\tag{6}
\]

then `T` determines the complete source vector `X`. Hence for every source coordinate,

\[
\boxed{
\left\|\mathbf E[X_i\mid T]\right\|_2^2=1.
}
\tag{7}
\]

In the notation of `MC-338`, the own-phase leakage is `rho_i=1` for every `i`. Therefore the scalar prime-shell bias can contain the unrestricted matched filter completely; the `MC-338` energy inequality then gives no stronger floor than

\[
\mathcal E(W)\ge1
\tag{8}
\]

for exact dephasing.

Second, exact balance is radically different. If `R|N` and

\[
n_1=\cdots=n_R=N/R,
\tag{9}
\]

then `T=R^{-1}\sum_i X_i`. Exchangeability on the punctured cube gives

\[
\mathbf E[X_i\mid T]=T
\tag{10}
\]

for every `i`, and therefore

\[
\boxed{
\rho_i^2
=\mathbf E[T^2]
=\frac{2^R-R}{R(2^R-1)}
=\frac1R+O(2^{-R}).
}
\tag{11}
\]

Consequently every coefficient architecture whose source observation is only this exactly balanced shell bias, or any measurable coarsening of it, obeys

\[
\boxed{
\delta(W)
\ge
\left(
1-\sqrt{\mathcal E(W)}
\sqrt{\frac{2^R-R}{R(2^R-1)}}
\right)_+.
}
\tag{12}
\]

Exact dephasing in this balanced scalar channel costs

\[
\boxed{
\mathcal E(W)
\ge
\frac{R(2^R-1)}{2^R-R}
=R+o(1).
}
\tag{13}
\]

The apparent robustness of `(11)` is false. **Arbitrarily near-balanced integer shell multiplicities can again make the same scalar transcript target-complete.** For every even `R>=2` and every integer

\[
B>2^R-1,
\]

set

\[
\boxed{
n_i=B+2^{i-1},
\qquad
N=RB+2^R-1.
}
\tag{14}
\]

Then all subset sums of the `n_i` are distinct, while

\[
\boxed{
\max_i\left|\frac{n_i}{N}-\frac1R\right|
\le
\frac{2^R}{N}.
}
\tag{15}
\]

Letting `B` grow makes the cell-mass vector converge uniformly to the balanced point, but `(7)` continues to hold exactly for every member of the family. Hence there is **no exact-real implication**

\[
\max_i|d_i-1/R|\to0
\quad\Longrightarrow\quad
\rho_i\to0.
\tag{16}
\]

Approximate equidistribution of endpoint defect masses cannot by itself justify treating the raw prime-shell bias as a low-information transcript. A viable arithmetic use of this scalar must additionally impose a canonical resolution/noise/coarsening condition, or prove exact additive collisions in the actual defect multiplicities.

No estimate for `M(x)` and no zero-free result follows.

## 1. The prime-shell character sum is exactly a weighted source readout

For the selected basis characters `lambda_1,...,lambda_R` of `MC-296`, a shell prime in the defect cell `D_i` has basis-character values `+1` in coordinate `i` and `-1` in every other selected coordinate. Products of the basis characters therefore give, for each nonprincipal mode, one fixed sign `X_i(a)` on the whole cell `D_i`.

Summing the mode character over the shell gives `(3)` immediately. If `J(a)` is the set of negative source coordinates, then

\[
\sum_i d_iX_i
=
\sum_{i\notin J}d_i-
\sum_{i\in J}d_i
=1-2d(J),
\]

which proves `(5)`. This is the source-coordinate form of the exact Fourier profile already derived in `MC-296`:

\[
x_{\lambda_I}=(-1)^{|I|}(1-2d(I)).
\]

The new point is not another formula for that profile. It is the provenance statement: when this arithmetic bias is admitted as coefficient information, its posterior ability to predict an own source phase is controlled by the additive collision structure of the endpoint multiplicities.

## 2. Distinct subset sums make one scalar target-complete

Equation `(5)` shows that observing `T` is equivalent to observing the subset sum `d(J)`. Under `(6)`, the value `d(J)` identifies `J`, hence identifies every sign `X_i`.

Therefore

\[
\mathbf E[X_i\mid T]=X_i
\]

almost surely, proving `(7)`. The puncture in `(2)` removes only the all-`+1` state, corresponding to `J=emptyset`; it does not affect injectivity on the remaining states.

This is precisely the inverse-resolution loophole isolated abstractly by `MC-341`--`MC-342`, now instantiated by a genuine arithmetic observable. Scalar dimension and bounded range do not imply low source information: exact real values can carry the full endpoint word through very fine subset-sum spacing.

## 3. Exact balance gives one-over-rank leakage

Under `(9)`, equation `(4)` becomes

\[
T=\frac1R\sum_{j=1}^R X_j.
\tag{17}
\]

Conditioned on a value of `T`, the punctured source law is invariant under coordinate permutations. Hence all conditional coordinate means are equal. Summing them and using `(17)` gives

\[
R\,\mathbf E[X_i\mid T]
=
\mathbf E\left[\sum_jX_j\,\middle|\,T\right]
=RT,
\]

which proves `(10)`.

On the full sign cube,

\[
\sum_{x\in\{\pm1\}^R}
\left(\sum_i x_i\right)^2
=2^R R.
\]

The punctured law deletes the all-`+1` vector, whose squared sum is `R^2`. With `m=2^R-1`,

\[
\mathbf E[T^2]
=
\frac{2^R R-R^2}{mR^2}
=
\frac{2^R-R}{R(2^R-1)},
\]

proving `(11)`. Any coarsening `Y=phi(T)` has

\[
\|\mathbf E[X_i\mid Y]\|_2
\le
\|\mathbf E[X_i\mid T]\|_2
\]

by conditional-expectation contraction, so `(12)` also applies to every downstream coarsening of the balanced scalar.

This is sharper for this concrete transcript than the generic joint-information tariff of `MC-340`: the exact balanced readout exposes only `Theta(1/R)` squared predictability per source coordinate.

## 4. Near-balance does not survive exact-real decoding

Take the integer family `(14)`. Suppose two subsets `J,K subseteq [R]` have the same multiplicity sum. Then

\[
B(|J|-|K|)
+
\sum_{i\in J}2^{i-1}
-
\sum_{i\in K}2^{i-1}
=0.
\tag{18}
\]

If `|J|=|K|`, uniqueness of binary expansion forces `J=K`. If `|J|!=|K|`, the first term has absolute value at least `B`, whereas the absolute value of the binary-sum difference is at most `2^R-1<B`. Equality is impossible. Hence all subset sums are distinct.

For the balance estimate,

\[
\frac{n_i}{N}-\frac1R
=
\frac{R2^{i-1}-(2^R-1)}{RN},
\]

and the numerator has absolute value at most `R2^R`, giving `(15)`.

Thus even the **integer provenance** of actual cell counts does not rescue approximate balance as an information constraint. Along this family, the normalized defect masses converge to exact balance while the shell bias jumps from the `Theta(1/R)` leakage of `(11)` to perfect source recovery `(7)`.

At the critical endpoint scale considered earlier in the line, where `2^R` is only logarithmic in the prime-shell scale while `N` is of order the number of primes in a dyadic interval, there is ample arithmetic resolution for such a finite-precision code in principle. This sentence is a scale comparison only, not a claim that actual prime defect multiplicities realize `(14)`.

## 5. Prior art and novelty boundary

The additive coding mechanism is classical. Distinct-subset-sum sets are a standard object in additive combinatorics; Tom Bohman, *A construction for sets of integers with distinct subset sums*, Electronic Journal of Combinatorics **5** (1998), R3, studies exactly the condition that all `2^R` subset sums be distinct. Binary/superincreasing weights are also the elementary encoding mechanism behind classical knapsack constructions such as Merkle--Hellman.

No novelty is claimed for binary positional encoding, superincreasing/subset-sum uniqueness, exchangeability, or conditional expectation. A targeted prior-art audit on 18 September 2026 found no basis for such a claim.

The durable Mathia delta is the exact composition of those classical mechanisms with the reciprocal endpoint provenance already stored in `MC-296` and the leakage-energy theorem of `MC-338`: the **actual unweighted prime-shell character bias is itself a subset-sum transcript in the defect-cell counts**. This simultaneously supplies a concrete low-leakage calibration at exact balance and an explicit near-balanced arithmetic-count control where the same scalar becomes source-complete.

This finding therefore does not propose a new character-sum theorem. It prevents a false next step: replacing the parity-query model of `MC-367` by the raw shell bias and assuming that near-equal source masses make that scalar informationally weak.

## Boundaries and falsification tests

- **Even rank.** The clean punctured-cube source law `(2)` is used throughout. The result is already sufficient to falsify a generic near-balance-to-low-leakage principle; no odd-rank extension is claimed.
- **Exact endpoint partition.** Equation `(3)` uses the exact source-cell partition of `MC-296`. Outside that construction the transcript must be re-derived from its own arithmetic provenance.
- **Exact-real observation.** The full-leakage branch `(7)` assumes exact access to the scalar shell bias. Quantization, noise, smoothing, finite numerical precision or an analytically forced tolerance can merge subset sums and must be priced separately.
- **Exact balance is singular.** Equation `(11)` is not stable under arbitrary tiny perturbations in exact real arithmetic. It may become stable after a canonical finite-resolution quotient, but such a quotient is an additional hypothesis.
- **The construction is a matched control, not an arithmetic existence claim.** The integer profile `(14)` proves that positivity, integrality, fixed total mass and arbitrarily small normalized imbalance do not forbid complete scalar coding. It does not assert that the rational-prime Legendre defect cells actually have these sizes.
- **Multiple or weighted observables can only reveal more.** The result does not upper-bound architectures that observe individual prime contributions, several shell sums, log-weighted sums, or other side channels.
- **No Mertens consequence.** Nothing here controls `M(x)`, proves a zero-free region, or rules out the endpoint arithmetic construction.

## Consequence for the research line

The concrete-transcript question posed after `MC-367` now has a sharp first answer. The raw prime-shell character bias is **not** intrinsically a low-rank or low-information observation: its information content is the subset-sum geometry of the exact defect multiplicities. Exact equal cell sizes suppress own-phase leakage to `Theta(1/R)`, but arbitrarily near-equal positive integer cell sizes can encode every source phase perfectly.

Accordingly, future arithmetic provenance tariffs cannot use approximate cell equidistribution alone. They must identify a canonical loss of resolution — noise, smoothing, quantization, a theorem controlling inverse conditioning, or exact additive collisions forced by arithmetic — before the analog shell bias can feed the `MC-338` obstruction. This is the concrete arithmetic version of the inverse-conditioning warning in `MC-341`--`MC-342`, and it narrows the surviving bridge beyond the coordinate/parity sketches of `MC-366`--`MC-367`.