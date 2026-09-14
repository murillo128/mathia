# MC-287 — Half-cube density collapses the odd shell obstruction to near-injectivity

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`

## Claim

Continue the projected shell setup of `MC-285`–`MC-286`. Let

\[
S\subset \mathbf F_2^d
\]

be the set of distinct occupied projected Legendre-sign cells, let `K=|S|`, let `n_s>=1` be the shell multiplicity of `s\in S`, and put

\[
N=\sum_{s\in S}n_s.
\]

Fix an odd target shell weight `t>=3`. If

\[
\boxed{K>2^{d-1}}
\tag{1}
\]

then `S` contains an odd zero-sum nucleus `B` of size at most three. Moreover, if

\[
\boxed{N-K\ge t-1,}
\tag{2}
\]

then the multiplicities can pad that nucleus by equal-cell pairs to produce an exact `t`-element shell row whose projected product is the all-positive endpoint.

Consequently, any endpoint-normalized empirical-Christoffel certificate of the type studied in `MC-281` with energy strictly below one must satisfy the deterministic dichotomy

\[
\boxed{
K\le 2^{d-1}
\quad\text{or}\quad
N-K\le t-2.
}
\tag{3}
\]

Thus there is no intermediate dense-occupancy escape for odd weights. Outside the half-cube regime, failure to contain an exact odd endpoint row forces the projected shell map to be nearly injective: at most `t-2` shell primes may be repetitions beyond the number of distinct projected cells.

In the live regime `N\asymp y/(2\log y)` and `t=O(\log\log y)`, the second branch of `(3)` gives

\[
K\ge N-t+2
\]

and hence

\[
2^d\ge N-t+2,
\qquad
d\ge \log_2 y-\log_2\log y+O(1).
\tag{4}
\]

For distinct odd-prime coordinates this again forces primorial-scale coordinate conductor

\[
\log Q(U)
\ge
\left(\frac1{\log 2}+o(1)\right)
\log y\,\log\log y
\tag{5}
\]

on the near-injective branch. The alternative branch `K<=2^{d-1}` remains genuinely different: it allows half-cube-scale concentration, including the affine-hyperplane obstruction isolated in `MC-286`.

No Möbius summatory bound is improved and no RH consequence follows. The result only closes a finite-combinatorial gap in the current odd-weight Christoffel route.

## 1. More than half the Boolean cube forces a one- or three-cell odd nucleus

The only group-theoretic input is the standard half-density sumset fact

\[
|A|>\frac{|G|}{2}
\quad\Longrightarrow\quad
A+A=G
\tag{6}
\]

for a finite abelian group `G`. Indeed, for every `v\in G`, the two sets `A` and `A+v` each have more than half the elements of `G`, so they intersect. Thus `v=x+y` for some `x,y\in A`.

Apply this to `G=F_2^d` and `A=S`. If `0\in S`, then

\[
B=\{0\}
\]

is already an odd zero-sum nucleus.

Assume instead that `0\notin S`, choose any `v\in S`, and use `(6)` to write

\[
v=x+y,
\qquad x,y\in S.
\tag{7}
\]

Then

\[
x+y+v=0.
\tag{8}
\]

The three elements are distinct: `x=y` would imply `v=0`, while `x=v` or `y=v` would force the remaining element to be zero. Hence

\[
B=\{x,y,v\}
\]

is a three-cell odd zero-sum nucleus.

The threshold is sharp as a support statement. An affine hyperplane

\[
H=\{x\in\mathbf F_2^d:\lambda(x)=1\}
\]

has exactly `2^{d-1}` elements and contains no odd zero-sum subset, because every odd sum of elements of `H` still has `lambda=1`. This is precisely the affine obstruction characterized in `MC-286`.

## 2. Collision excess `N-K` supplies all required parity-neutral padding

Let `B\subset S` be any odd zero-sum nucleus of odd size `k<=t`. The exact pair capacity from `MC-286` is

\[
P_B
=
\sum_{s\in S}
\left\lfloor\frac{n_s-1_B(s)}2\right\rfloor.
\tag{9}
\]

A slightly sharper support-only lower bound than the coarse estimate recorded there follows directly from `floor(m/2)>=(m-1)/2` for every nonnegative integer `m`:

\[
P_B
\ge
\frac{N-k-K}{2}.
\]

Since `P_B` is an integer,

\[
\boxed{
P_B\ge
\left\lceil\frac{N-K-k}{2}\right\rceil.
}
\tag{10}
\]

If `(2)` holds, then

\[
N-K-k\ge t-k-1.
\]

Both `t` and `k` are odd, so `(t-k)/2` is an integer and `(10)` gives

\[
P_B\ge\frac{t-k}{2}.
\tag{11}
\]

Reserve one shell prime in each nucleus cell and add `(t-k)/2` disjoint equal-cell pairs. Every pair contributes zero in `F_2^d`, while the nucleus sums to zero, so the selected `t` distinct shell primes have projected endpoint product `+1` on every used coordinate.

Combining this padding lemma with Section 1 proves that `(1)` and `(2)` force an exact odd endpoint row.

## 3. The Christoffel consequence is a sharp occupancy dichotomy

By `MC-281`, an endpoint-normalized polynomial evaluates to `1` on every projected endpoint row. A single such row contributes `1` to its counting-measure empirical energy. Therefore energy `<1` requires that no exact endpoint row of the prescribed shell weight exist.

For odd `t>=3`, Sections 1–2 show that the simultaneous conditions

\[
K>2^{d-1},
\qquad
N-K\ge t-1
\]

are incompatible with energy `<1`. Negating them gives `(3)`.

The two surviving branches have different meanings:

- `K<=2^{d-1}` is a **concentration branch**. It includes the exact affine-hyperplane obstruction of `MC-286`, but the inequality alone does not assert that such an affine obstruction actually exists.
- `N-K<=t-2` is a **near-injective branch**. Since `N-K` is the collision excess of the shell-to-pattern map, all but `O(t)` of the shell multiplicity must be spent on distinct projected patterns.

At live `t=O(log log y)`, there is therefore no broad middle regime in which many patterns are occupied, many shell primes collide, and yet the odd endpoint is absent for purely combinatorial reasons.

## 4. Relation to the current frontier

`MC-285` showed that even shell weights are killed by equal-pattern pairing whenever `N-K>=t`. `MC-286` identified the exact support-level odd obstruction as affine span and gave the exact multiplicity criterion once an odd nucleus is known, but its generic nucleus bound `|B|<=d+1` left a large gap when `d` greatly exceeds the live weight `t`.

The present result closes that gap in the dense-support regime. Once more than half of the projected cube is occupied, the required odd nucleus has size at most three, independent of `d`. The only remaining way to avoid an odd endpoint at that density is to have too little duplicate mass to pad the nucleus to the prescribed weight, namely `N-K<=t-2`.

This changes the source-native arithmetic target. It is no longer enough to ask whether some generated product-character direction can remain constant negative. A prospective odd-weight Christoffel escape must now explain one of two much more rigid phenomena: **half-cube-or-smaller pattern concentration**, or **almost injective encoding of roughly `y/log y` shell primes into the used Legendre coordinates**. Any arithmetic theorem ruling out both regimes at the certificate's admissible support scale kills the route.

## 5. Prior art and novelty boundary

The half-density lemma `(6)` is classical elementary additive combinatorics. In the binary-matroid literature, essentially the same statement appears explicitly as Lemma 3.1 of Jim Geelen and Peter Nelson, *The critical number of dense triangle-free binary matroids*, Journal of Combinatorial Theory, Series B 116 (2016), 238–249, DOI `10.1016/j.jctb.2015.08.003`: a subset of `F_2^n` with more than `2^{n-1}` elements represents every vector as a sum of two of its elements. No novelty is claimed for this fact, for affine-hyperplane sharpness, or for the elementary pair-count inequality.

The line-specific contribution is their exact composition with the `MC-286` odd-nucleus/pair-capacity criterion and the `MC-281` endpoint-energy obstruction, yielding the occupancy dichotomy `(3)` and its near-injective support consequence for the actual shell representation.

## Boundaries and falsification tests

- The density condition `K>2^{d-1}` is sufficient, not necessary, for a short odd zero-sum nucleus. Much sparser supports may still contain one.
- The collision condition `N-K>=t-1` is sufficient, not necessary, for padding a particular nucleus. The exact criterion remains `(9)`.
- The first branch of `(3)` does not prove affine concentration; it only says that dense-support forcing no longer applies.
- The second branch does not prove that a Christoffel certificate exists. It is only a necessary combinatorial escape condition.
- The result uses only projected shell occupancy and multiplicity. It provides no analytic estimate showing which branch the actual Legendre shell occupies at large support.
- A counterexample to the claim would require a set `S` with `K>2^{d-1}` and multiplicities with `N-K>=t-1` but no exact odd `t` zero-sum selection. Sections 1–2 construct such a selection explicitly, so the finite statement is exact.

## Consequence for the research line

The odd/even split is now substantially tighter. Even weights require almost maximal pattern diversity once low-support pairing is excluded; odd weights either compress to at most half of the Boolean cube or become near-injective at the same `O(t)` collision scale. The surviving arithmetic question is therefore a quantitative shell-occupancy dichotomy rather than generic affine-span algebra: can the actual quadratic-character shell sustain half-cube concentration at the support scales relevant to a certificate, and if not, can it really encode nearly every shell prime into a distinct used-coordinate pattern without paying the support/conductor cost already exposed by `MC-284`–`MC-285`?