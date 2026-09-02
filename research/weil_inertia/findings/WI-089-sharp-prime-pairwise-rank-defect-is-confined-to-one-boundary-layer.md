# WI-089 — Sharp prime pairwise rank defect is confined to one boundary layer

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion and does not certify or repair the Yang--Yang one-sided fourth-moment candidate. It sharpens the residual prime-pair rank closure of WI-088 in the direction that WI-088 left live: simultaneous consistency of the worst pairwise defects. The one-third defect ceiling of WI-088 can be approached only on one boundary quotient, exact ceiling cases occupy at most nine remainders for a fixed prime pair, the opposite-mod-3 sharp cases form a matching for a fixed observation length, and the full exact-ceiling pair graph has uniformly bounded degree.

Let `p<q<2p` be distinct odd primes and let

\[
d=q-p,
\qquad
t=p-d=2p-q.
\tag{1}
\]

In the genuinely residual close-prime regime of WI-088, write the nearest-LCM boundary length as

\[
\delta=kq+s,
\qquad d<s<p,
\tag{2}
\]

and set

\[
A=s-d,
\qquad B=p-s,
\qquad A+B=t.
\tag{3}
\]

Let

\[
\tau_{p,q}(\delta)
=(p-1)-\operatorname{rank}G_{p,q}^{(N)}
\tag{4}
\]

be the residual transversality defect from WI-086/WI-088. WI-088 proves

\[
\tau_{p,q}(\delta)
\le
\max\left\{0,
\left\lfloor\frac{t}{3}\right\rfloor-1
\right\}.
\tag{5}
\]

The exact graph hidden in that proof gives substantially more rigidity.

First, put

\[
k_0=\left\lfloor\frac p3\right\rfloor,
\qquad
a_0=p-3k_0\in\{1,2\}.
\tag{6}
\]

Then every free directed 3-cycle in the WI-088 partial-permutation graph forces

\[
\boxed{k=k_0}
\tag{7}
\]

and contains exactly `a_0` vertices of the `A` region and `3-a_0` vertices of the `B` region. Consequently, whenever

\[
\boxed{k\ne\left\lfloor\frac p3\right\rfloor,}
\tag{8}
\]

all free cycles have length at least four and

\[
\boxed{
\tau_{p,q}(\delta)
\le
\max\left\{0,
\left\lfloor\frac{2p-q}{4}\right\rfloor-1
\right\}.
}
\tag{9}
\]

Thus the one-third scale is not available throughout the residual boundary: away from a single quotient it drops universally to a one-quarter cycle-counting scale.

On the exceptional quotient `k=k_0`, if `c_3` is the number of free 3-cycles and `c` the total number of free cycles, then

\[
c_3\le
u:=
\min\left\{
\left\lfloor\frac{A}{a_0}\right\rfloor,
\left\lfloor\frac{B}{3-a_0}\right\rfloor
\right\},
\tag{10}
\]

and

\[
4c-c_3\le t.
\tag{11}
\]

Hence

\[
\boxed{
\tau_{p,q}(\delta)
\le
\max\left\{0,
\left\lfloor\frac{t+\nu}{4}\right\rfloor-1
\right\}.
}
\tag{12}
\]

Equation (12) recovers WI-088 because `nu<=floor(t/3)`, but it is strictly sharper whenever the available `A/B` populations cannot support enough 3-cycles in the required ratio.

More rigidly, write

\[
t=3r+j,
\qquad r=\left\lfloor\frac t3\right\rfloor,
\qquad j\in\{0,1,2\}.
\tag{13}
\]

If the positive WI-088 ceiling is attained,

\[
\tau_{p,q}(\delta)=r-1\ge1,
\tag{14}
\]

then necessarily `k=k_0` and, writing

\[
A=a_0r+e,
\tag{15}
\]

one must have

\[
\boxed{
-a_0j\le e\le(4-a_0)j.
}
\tag{16}
\]

Therefore, for a fixed prime pair `(p,q)`, exact positive ceiling defect can occur at **at most**

\[
\boxed{4j+1\le9}
\tag{17}
\]

remainders `s`, all in the single quotient `k=floor(p/3)`. In particular, any sequence satisfying

\[
\frac{\tau_{p,q}(\delta)}{2p-q}\longrightarrow\frac13
\tag{18}
\]

must have

\[
k=\left\lfloor\frac p3\right\rfloor
\tag{19}
\]

for all sufficiently large terms and

\[
\frac{A}{2p-q}\longrightarrow\frac{a_0}{3},
\qquad
\frac{B}{2p-q}\longrightarrow\frac{3-a_0}{3}.
\tag{20}
\]

For opposite nonzero residue classes modulo `3`, the classification becomes exact. In that case `j=0`, so (16) forces `e=0` and there is only one possible sharp boundary. If

\[
p\equiv2\pmod3,
\qquad q\equiv1\pmod3,
\tag{21}
\]

it is the WI-087 boundary

\[
\delta_-=rac{pq+p-q}{3}.
\tag{22}
\]

If instead

\[
p\equiv1\pmod3,
\qquad q\equiv2\pmod3,
\tag{23}
\]

then the unique possible boundary is the mirror

\[
\boxed{
\delta_+=\frac{pq+q-p}{3}.
}
\tag{24}
\]

This second family is genuinely sharp as well. With the WI-087 parameters

\[
\alpha=\frac{2p-q}{3},
\qquad
\beta=\frac{p+q}{3},
\qquad
\gamma=\frac{2q-p}{3},
\tag{25}
\]

and

\[
P(X)=1+X^\alpha+X^\beta,
\qquad
Q(X)=1+X^\gamma+X^\beta,
\tag{26}
\]

WI-087 proves

\[
P-X^\alpha Q=1-X^p,
\qquad
P-X^\beta Q=(1+X^\alpha)(1-X^q),
\tag{27}
\]

and proves that `P,Q` are coprime and regular on both prime root sets. For the mirrored residue classes, use the inverse interpolant

\[
R_+(X)=\frac{Q(X)}{P(X)}.
\tag{28}
\]

On `p`-th roots it equals `X^beta`, while on `q`-th roots it equals `X^gamma`. Since

\[
\delta_+\equiv\beta\pmod p,
\qquad
\delta_+\equiv\gamma\pmod q,
\tag{29}
\]

the same Bezoutian/Vandermonde factorization as WI-087 gives

\[
\boxed{
\operatorname{rank}G_{p,q}^{(\delta_+)}
=\beta=\frac{p+q}{3},
}
\tag{30}
\]

and therefore

\[
\boxed{
\tau_{p,q}(\delta_+)
=\frac{2p-q-3}{3}.
}
\tag{31}
\]

So WI-087 and (24)--(31) are the two opposite-residue realizations of the same sharp boundary-layer geometry.

There is also a simultaneous-consistency consequence at fixed observation length `N`. Call an edge `{p,q}` **canonical sharp** when `p<q<2p`, the primes occupy opposite nonzero residue classes modulo `3`, and

\[
\delta_N(p,q)\in\{\delta_-,\delta_+\}
\tag{32}
\]

with the appropriate member selected by the residue orientation. Define

\[
\varepsilon(\ell)=
\begin{cases}
+1,&\ell\equiv1\pmod3,\\
-1,&\ell\equiv2\pmod3.
\end{cases}
\tag{33}
\]

For either sharp family one has at each endpoint `ell`, with the other endpoint denoted `m`,

\[
3\delta_{\rm sharp}\equiv\varepsilon(\ell)m\pmod\ell.
\tag{34}
\]

Because `delta_N` may come from either side of the nearest `pq` boundary, a canonical sharp edge at fixed `N` therefore satisfies

\[
\boxed{
3N\equiv\eta\,\varepsilon(\ell)m\pmod\ell,
\qquad \eta\in\{+1,-1\}.
}
\tag{35}
\]

Suppose a prime `q` had canonical sharp neighbors `p<q<r`. Applying (35) at the common endpoint `q` gives

\[
r\equiv\pm p\pmod q.
\tag{36}
\]

Since `q<r<2q`, the `+` case forces `r=q+p`, an even integer greater than two. The `-` case forces

\[
r=2q-p.
\tag{37}
\]

But `p` and `r` have the same nonzero residue modulo `3`, opposite that of `q`, so the right side of (37) is divisible by `3`; since `r>q>3`, it cannot be prime. Thus

\[
\boxed{
\text{for each fixed }N,\text{ the canonical sharp prime-pair edges form a matching.}
}
\tag{38}
\]

The same method gives a coarse uniform sparsity theorem for **all** exact positive ceiling cases, including same-residue pairs. Under (14), equations (13)--(16) give

\[
3\delta
=(p+3-2a_0)q+(2a_0-3)p-a_0j+3e.
\tag{39}
\]

Modulo either endpoint, the coefficient of the partner prime is `+1` or `-1`. For fixed `N`, fixed endpoint, nearest-boundary sign, `j`, and `e`, the partner residue is therefore uniquely determined. The admissible values are:

- for an endpoint congruent to `1 mod 3`, `j=0` or `1`, giving `1+5=6` possible `(j,e)` pairs;
- for an endpoint congruent to `2 mod 3`, `j=0` or `2`, giving `1+9=10` possible `(j,e)` pairs.

Including the two nearest-boundary signs, there are at most `12` candidate partners on either orientation for a `1 mod 3` endpoint and at most `20` for a `2 mod 3` endpoint. Since `q<2p` makes the relevant residue representative unique on each orientation,

\[
\boxed{
\deg_N(\ell)\le40
}
\tag{40}
\]

for the graph whose edges are residual prime pairs attaining a positive WI-088 ceiling at observation length `N`.

## 1. Three-cycle arithmetic forces one quotient

The proof begins inside the exact partial-bijection graph of WI-088. Every free cycle is disjoint from the forced-zero set and is constant under the partial map

\[
g(x)=
\begin{cases}
x+(k+1)d,&x\in A,\\
x+kd,&x\in B,
\end{cases}
\pmod p.
\tag{41}
\]

WI-088 already excludes cycles of lengths one and two. Consider a free 3-cycle and let `a` be the number of its vertices lying in `A`. The total translation around the cycle is

\[
(3k+a)d\equiv0\pmod p.
\tag{42}
\]

Since `d` is invertible modulo the prime `p`, this means

\[
3k+a\equiv0\pmod p.
\tag{43}
\]

The residual boundary gives

\[
1\le k\le\frac{p-1}{2}.
\tag{44}
\]

For a positive ceiling case one necessarily has `p>3`; with `0<=a<=3`, the integer `3k+a` lies strictly between `0` and `2p`. Hence it must equal `p`. The cases `a=0` and `a=3` would make the prime `p!=3` divisible by `3`, so

\[
a=a_0\in\{1,2\},
\qquad
k=\frac{p-a_0}{3}=\left\lfloor\frac p3\right\rfloor.
\tag{45}
\]

This proves (7). If `k!=k_0`, every free cycle has length at least four. At most `t` vertices are available to free cycles, so `c<=floor(t/4)`. WI-088 gives `tau<=max(0,c-1)` after the zero-mean constraint, proving (9).

When `k=k_0`, each free 3-cycle uses exactly `a_0` `A`-vertices and `3-a_0` `B`-vertices. This proves (10). If there are `c_3` 3-cycles and `c-c_3` longer cycles, their total number of vertices is at least

\[
3c_3+4(c-c_3)=4c-c_3,
\]

which proves (11) and then (12).

## 2. Equality forces a bounded remainder window

Assume the positive WI-088 ceiling (14). Since `tau<=c-1`, one must have `c>=r`. Equation (11) then gives

\[
c_3\ge4c-t\ge4r-(3r+j)=r-j.
\tag{46}
\]

The required `A/B` populations therefore satisfy

\[
A\ge a_0(r-j),
\qquad
B\ge(3-a_0)(r-j).
\tag{47}
\]

Writing `A=a_0r+e`, the first inequality gives `e>=-a_0j`. Since

\[
B=t-A=(3-a_0)r+j-e,
\]

the second gives `e<=(4-a_0)j`. This is (16), whose integer interval contains exactly `4j+1` values.

The same counting proves the near-extremal statement (18)--(20). If `k!=k_0`, (9) keeps `tau/t` at most `1/4+o(1)`. Hence an asymptotic ratio `1/3` forces the exceptional quotient. Then (46) implies `c_3/t->1/3`; (47), together with `A+B=t`, squeezes the two region densities to (20).

## 3. The mirrored sharp family is an exact Loewner--Bezout consequence

When `j=0`, equation (16) gives `e=0`, so the sharp remainder is unique. The `p=2 mod 3`, `q=1 mod 3` orientation simplifies to (22), already realized by WI-087. The opposite orientation simplifies to (24).

No new interpolation theorem is needed for the mirror. WI-087's identities (27), node regularity, coprimality, and nonsingular Bezoutian are symmetric under exchanging numerator and denominator. Taking `Q/P` instead of `P/Q` gives the two restrictions in (29). The monomial Loewner matrix for `X^delta_+` is therefore the rational Loewner matrix for `Q/P` on the same primitive-root node sets. The Bezoutian changes only by sign under `P,Q` exchange, so its rank remains `beta`; the same Vandermonde dimension check from WI-087 applies. This proves (30)--(31).

Finite exact calculations for `(p,q)=(13,17),(19,23),(31,41),(37,41),(43,47)` reproduce the predicted ranks at `delta_+`, but those computations are regression diagnostics only and are not used as evidence for the proof.

## 4. Fixed-window simultaneous sharpness is arithmetically sparse

Equation (34) follows by reducing (22) or (24) modulo either endpoint. If

\[
N\bmod pq=\delta_{\rm sharp}
\quad\text{or}\quad
pq-\delta_{\rm sharp},
\]

then (35) follows with the corresponding sign. The matching proof after (35) uses only primality, the close-prime condition on both incident edges, and the opposite mod-3 orientation. It therefore rules out any attempt to realize a star, chain, or denser graph made entirely from the canonical opposite-residue one-third-defect pairs at one common observation length.

For the general ceiling graph, substitute `k=(p-a_0)/3`, `s=d+a_0r+e`, and `3r=t-j` into `delta=kq+s`; this gives (39). Reducing modulo the smaller or larger endpoint leaves the partner prime with coefficient `+1` or `-1`, plus a constant determined by `(j,e)`. The counts following (39) are exactly the sizes of the integer interval (16) in the residue-compatible cases. The close-prime interval then makes each admissible partner residue represent at most one partner on each orientation, proving (40).

The degree bound is intentionally coarse. It is a universal sparsity statement, not a classification of which of the at most forty arithmetic candidates actually satisfy the full row-kernel equations. Many candidates may fail before reaching the WI-088 ceiling.

## 5. Prior art, evidence boundary, and research consequence

The ingredients around this result are established or classical.

- WI-081 supplies the nearest-LCM boundary factorization and exact prime residue-sum row-kernel equations.
- WI-086 identifies the residual defect with the row-kernel/excess-transversality dimension after both prime Ramanujan dimensions have saturated.
- WI-087 supplies the original sharp Loewner--Bezout family and the classical rational-interpolation/Bezoutian prior-art anchors.
- WI-088 supplies the partial-bijection graph, the exclusion of one- and two-cycles, and the sharp universal one-third pairwise defect ceiling.
- The surrounding Ramanujan-subspace and exact-period matrix structure is classical and already anchored in `SOURCES.md`, notably Vaidyanathan's 2014 Ramanujan-subspace papers and Ushiroya's 2018 Ramanujan-matrix spectral identities.

A targeted audit of finite Ramanujan/Fourier cross-Gram rank, consecutive partial Fourier/Vandermonde systems, root-of-unity Loewner matrices, rational interpolation, and Ramanujan-subspace literature found the neighboring classical machinery but no direct theorem matching the boundary-layer or fixed-window sparsity statements above. That search outcome is **not** a priority claim. The durable content here is the exact deduction from the already-audited WI-088 graph plus the WI-087 Bezoutian construction.

The limitations are load-bearing.

1. The result concerns residual **prime pairwise rank**. It does not determine singular values, signed eigenvalues, source coefficients, or the inertia of a weighted sum of several Ramanujan blocks.
2. The one-quarter estimate (9) is an upper bound on defect obtained from selected row-kernel equations; it need not be attained.
3. Conditions (7) and (16) are necessary for exact ceiling. Except for the two opposite-residue Loewner--Bezout families proved above, no sufficiency is asserted.
4. The matching theorem applies to the canonical opposite-residue exact-ceiling families. The broader graph only has the coarse degree bound (40).
5. No composite-modulus extension is asserted. Primality enters through the WI-081 row-kernel model, invertibility modulo `p`, and the prime congruence arguments.
6. Nothing here changes the scalar aliasing obstruction of WI-083--WI-085: after source labels are erased, universal finite-window scalar geometry still factors through the same finite quotient.

The research consequence is nevertheless substantive. WI-088 showed that a single residual close-prime pair can lose asymptotically one third of the smaller primitive-frequency dimension. This finding shows that those extremizers cannot be treated as independently repeatable local obstructions. Near-one-third defect forces a unique quotient and a fixed `A/B` population ratio; exact ceiling occupies a bounded remainder set; and the strongest exact families are pairwise disjoint at fixed `N`. Any attempt to turn pairwise Ramanujan rank loss into a global signed-inertia obstruction must therefore respect this arithmetic compatibility graph rather than summing worst-case pairwise deficits freely. Conversely, any improvement that still uses only universal pairwise rank is now sharply constrained: the remaining information lies in singular-value magnitude, source weights/signs, higher-order consistency across several moduli, or source labels that scalarization discards.