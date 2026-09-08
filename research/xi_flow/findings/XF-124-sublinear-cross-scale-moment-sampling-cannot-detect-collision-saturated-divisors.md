# XF-124 — sublinear cross-scale moment sampling cannot detect collision-saturated divisors

**Status:** `EXACT-DERIVED` + `NEGATIVE/OBSTRUCTION` + `CROSS-SCALE-SAMPLING` + `COLLISION-SATURATION` + `QUERY-LOWER-BOUND`. XF-123 shows that the complete autonomous first-`K` q-scale moment history is compatible with arbitrary periodic transition times and asymptotically full collision density. Its positive boundary explicitly leaves open the possibility of escaping that non-identifiability by observing modes above `K` or by imposing cross-scale information. A first natural repair would be to add a sparse collection of higher power sums spread across the degree scale. That repair is still insufficient at the level of a single real-rooted slice.

For every fixed `C>0` and every family of sampled harmonic sets

\[
S_N\subset\{1,\ldots,\lfloor CN\rfloor\},
\qquad
|S_N|=o(N),
\tag{1}
\]

there are, for all sufficiently large even `N`, two degree-`N` polynomials whose roots all lie on the unit circle such that

- every root of the first polynomial is simple;
- every root of the second belongs to a simple double collision, so it has exactly `N/2` distinct root locations;
- and their raw power sums agree **exactly** on every sampled harmonic in `S_N`.

In fact the common sampled values can all be zero. Thus an arbitrary sublinear set of individual moment coordinates remains blind even when it is allowed to jump far above the q-scale cutoff and scatter throughout any fixed multiple of the full degree scale.

For the proper harmonic range `1<=m<N`, the construction gives a quantitative consequence: any fixed set of individual power-sum coordinates that is guaranteed to distinguish this collision-saturated family from an all-simple divisor must contain `Omega(N)` frequencies. A direct counting argument gives the explicit lower bound `N/60-O(1)` for the particular balanced family used below.

This is not yet a source-specific Xi matched-control theorem for higher modes, and it does not show equality of sparse high-mode **histories** under heat. It closes the weaker but important escape route in which a sublinear number of extra high-mode snapshots is expected, by itself, to detect collision geometry that XF-123 hides from the low prefix.

## 1. Two balanced symmetry orders leave linearly many adversarial choices

Write

\[
N=2M
\tag{2}
\]

and consider integer symmetry orders

\[
R\in I_M
:=
\left[
\left\lceil\frac M3\right\rceil,
\left\lfloor\frac{2M}3\right\rfloor
\right]\cap\mathbf Z,
\qquad
R':=M-R.
\tag{3}
\]

Then `R'` lies in the same interval and

\[
2R+2R'=2M=N.
\tag{4}
\]

The candidate set has linear size,

\[
|I_M|\ge \frac M3-O(1)=\frac N6-O(1).
\tag{5}
\]

Fix one harmonic `m` with `1<=m<=CN`. If `R|m`, then because `R>=M/3` and `N=2M`,

\[
\frac mR\le 6C.
\tag{6}
\]

For each possible integer quotient `k=m/R`, the value `R=m/k` is determined uniquely. Hence the condition `R|m` excludes at most

\[
J_C:=\lceil 6C\rceil
\tag{7}
\]

candidates in `I_M`. The condition `R'=M-R|m` excludes at most another `J_C` candidates. Therefore one sampled frequency forbids at most `2J_C` values of `R`.

For a whole sampled set `S_N`, the union bound gives at most

\[
2J_C|S_N|
\tag{8}
\]

forbidden candidates. Combining `(5)` and `(8)`, if

\[
2J_C|S_N|<|I_M|,
\tag{9}
\]

there exists an `R in I_M` such that

\[
\boxed{
R\nmid m
\quad\text{and}\quad
R'\nmid m
\qquad
\text{for every }m\in S_N.
}
\tag{10}
\]

Condition `(9)` holds automatically for every `|S_N|=o(N)` when `C` is fixed.

For the sharper proper-harmonic range `S_N subset {1,...,N-1}`, `(6)` is strict with `C=1`, so `m/R<6` and there are at most five possible quotients. Each sampled harmonic therefore excludes at most ten values of `R`. Since `(5)` supplies `N/6-O(1)` candidates, any set that hits every balanced pair `(R,M-R)` must satisfy

\[
\boxed{
|S_N|\ge \frac N{60}-O(1).
}
\tag{11}
\]

No analytic estimate enters this counting step; it is an exact divisor-avoidance statement.

## 2. The same sampled moments occur for an all-simple divisor and an all-double divisor

For a unit complex number `u`, let

\[
Q_{r,u}(w):=w^r-u.
\tag{12}
\]

Its `r` roots form a rotated regular `r`-gon. Their raw `m`th power sum is

\[
P_m(Q_{r,u})
=
\begin{cases}
0,&r\nmid m,\\
r\,u^{m/r},&r\mid m.
\end{cases}
\tag{13}
\]

Choose `R` satisfying `(10)`. Pick unit phases `u,v` generically so that the root sets of `Q_{R,u}` and `Q_{R',v}` are disjoint, and define the collision-saturated polynomial

\[
\boxed{
F_N(w)
:=
Q_{R,u}(w)^2Q_{R',v}(w)^2.
}
\tag{14}
\]

Its degree is `2R+2R'=N`. It has exactly `R+R'=M=N/2` distinct unit-circle root locations and every one has multiplicity exactly two.

Independently choose four unit phases `u_1,u_2,v_1,v_2` so that all roots of the four factors below are pairwise distinct, and set

\[
\boxed{
G_N(w)
:=
Q_{R,u_1}(w)Q_{R,u_2}(w)
Q_{R',v_1}(w)Q_{R',v_2}(w).
}
\tag{15}
\]

Again `deg G_N=N`, but now every root is simple and lies on the unit circle. Generic phases exist because coincidences impose only finitely many forbidden phase relations.

For every `m in S_N`, neither `R` nor `R'` divides `m`. Equation `(13)` therefore annihilates the contribution of every factor in both `(14)` and `(15)`. Consequently

\[
\boxed{
P_m(F_N)=P_m(G_N)=0
\qquad
\text{for every }m\in S_N.
}
\tag{16}
\]

The indistinguishability is exact, with no asymptotic error, no weight rounding, and no appeal to cancellation between large nonzero moments. The sampled coordinates simply miss both symmetry orders.

This is the cross-scale extension of the aliasing mechanism isolated in XF-099. XF-099 fixed one symmetry order `M` and showed invisibility for the contiguous prefix `m<M`. Here the symmetry order is selected **after the sparse frequency set is known**, from a linear family of balanced orders, so invisibility survives arbitrary holes, scattered high frequencies, and frequencies of order `N` itself.

## 3. Deterministic adaptive sparse querying does not evade the obstruction

The same argument applies to a deterministic adaptive moment-query procedure. Suppose an algorithm is allowed to choose its next harmonic after seeing the previous power-sum values, all queries are restricted to `m<=CN`, and the total number of queries is `s_N=o(N)`.

Run the algorithm conceptually along the transcript in which every answer is zero. This produces a definite queried set `S_N` of size at most `s_N`. Choose `R` only after that transcript has been generated, using `(10)`, and then construct `F_N` and `G_N` by `(14)`--`(15)`. Equation `(16)` shows that both polynomials realize the entire zero transcript. Therefore the algorithm asks exactly the same sequence of adaptive questions on both inputs and returns the same output, although one divisor is completely simple and the other is completely collision-saturated.

Hence, within any fixed degree-scale band `m<=CN`, deterministic adaptivity does not change the asymptotic lower bound:

\[
\boxed{
\text{universal simple-vs-double discrimination by individual power sums requires }\Omega_C(N)\text{ queries.}
}
\tag{17}
\]

The statement is intentionally about coordinate queries. It does not rule out a single nonlinear observable that combines all coefficients, nor a structural Xi identity that couples many harmonics at once.

## 4. Stress tests and exact boundary

### 4.1 Full moment data defeats the construction

There is no contradiction with Newton identities or finite moment reconstruction. For a monic degree-`N` polynomial, the first `N` consecutive power sums determine all elementary symmetric coefficients recursively and hence determine the full root multiset including multiplicities. The present obstruction is precisely a **sublinear sparse-coordinate** lower bound, not an indeterminacy theorem for full degree-`N` data.

### 4.2 Frequencies much larger than the degree are outside the counting theorem

The fixed-`C` hypothesis in `(1)` matters. If queries are allowed at arbitrarily enormous harmonics, one integer `m` can have many divisors in `I_M`, and the constant bound `(8)` disappears. The natural independent Vieta information of a degree-`N` polynomial already lives in the first `N` power sums, so the degree-scale regime is the relevant first target; this finding makes no query-complexity claim for sparse exponents growing superlinearly without bound.

### 4.3 Snapshot equality does not imply equality of sparse high-mode heat histories

Unlike the contiguous first-`K` system used in XF-087--XF-123, an arbitrary scattered set of high moments is not closed under the triangular heat ODE. The evolution of one sampled high mode depends on unsampled lower modes. Therefore `(16)` is a target-slice statement and cannot be propagated to all heat times by the triangular uniqueness argument of XF-123.

This leaves a genuine possible escape: **dynamic cross-scale coupling** may reveal information that sparse snapshots do not. A positive next step should exploit the time derivative or transport of high modes together with their unobserved lower-mode forcing, rather than merely append isolated high-mode values to the q-scale prefix.

### 4.4 The construction is not source-specific to the Xi high moments

The common sampled values in `(16)` are zero. XF-119--XF-123 provide exact source-specific realization only for the natural low q-scale prefix, where Toeplitz near-isometry and prescribed-node quadrature are available. No corresponding theorem has yet been proved for arbitrary Xi target moments near the degree scale. Thus XF-124 does **not** say that Xi's actual high-mode samples admit both divisors; it says that collision geometry alone cannot make a sublinear high-mode coordinate set universally coercive.

### 4.5 The two slices really represent different collision status

At the displayed slice, `F_N` consists entirely of isolated double roots, while `G_N` has finitely many separated simple unit-circle roots. Under the same collision-safe periodic polynomial heat framework used in XF-099/XF-123, a double root in `F_N` splits off the real divisor immediately on the backward side, whereas simple roots of `G_N` remain real for a nonzero backward interval by local root continuity. Thus the sampled snapshot cannot even decide whether the observed slice itself is a transition boundary or lies strictly inside a real-rooted interval. This local statement does not require the two subsequent moment histories to agree.

## 5. Prior-art audit and consequence for the Xi gate

A directed literature audit covered classical Prony reconstruction of finitely supported measures from structured moment families, super-resolution from Fourier data, Newton/Girard recovery of polynomial coefficients from consecutive power sums, and the literature on vanishing sums of roots of unity. Those subjects delimit the surrounding problem but do not supply the present statement. In particular, Prony-type uniqueness theorems use sufficiently rich structured moment sets with size tied to support complexity, while the construction above is an adversarial **arbitrary sparse-coordinate** lower bound built from balanced cyclic subgroups. The roots-of-unity vanishing identity `(13)` itself is elementary and no novelty is claimed for it.

The Mathia-specific contribution is the consequence for the frontier created by XF-123: moving above `K` is not enough unless the new information has enough density or enough structural coupling to defeat divisor aliasing. No external theorem is load-bearing in `(2)`--`(17)`, so `SOURCES.md` remains unchanged.

The remaining positive routes are now more specific. One may seek a source-specific Xi theorem that couples a sparse high mode to the already matched low prefix through its **heat derivative/history**, a cross-scale identity that aggregates linearly many harmonics without storing them coordinate-by-coordinate, or genuinely global degree/entire-function geometry. What no longer suffices is the generic claim that sampling `o(N)` additional individual harmonics somewhere above the q-scale cutoff must expose a macroscopic collision set.
