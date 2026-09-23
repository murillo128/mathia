# NB-311 — endpoint remainder cancellation widens post-core near-isometry

- **Date:** 2026-09-23
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-290, NB-306, NB-308, NB-310
- **Classification:** `EXACT-DERIVED + CANONICAL-NYMAN-SOURCE + RECIPROCAL-SHELLS + ENDPOINT-CANCELLATION + PROJECTED-DILATION + POST-CORE-SPECTRUM + EXPLICIT-NEAR-ISOMETRY + STAIRCASE-BOUNDARY-LAYER + MOVING-CUTOFF + NON-TARGET-AWARE + PRIOR-ART-AUDITED`

## Claim

Let

\[
U_N:=\operatorname{span}\{g_2,\ldots,g_N\},
\qquad
2\le N<n\le 2N,
\qquad
h:=n-N.
\]

Put

\[
B:=\left\lfloor\frac Nh\right\rfloor\ge1.
\]

Then the single old-section approximant `(N/n) g_N` gives

\[
\boxed{
\operatorname{dist}(g_n,U_N)^2
\le
\left\|g_n-\frac Nn g_N\right\|_2^2
\le
\frac{h}{n^2}
\left(
6H_B+8+\pi^2
\right).
}
\tag{1}
\]

Thus the adjacent-chaining estimate used in `NB-310`, which was of order

\[
\frac{h^2\log n}{n^2},
\]

can be replaced by an endpoint estimate of order

\[
\frac{h}{n^2}
\left(1+\log\frac Nh\right).
\]

The improvement comes from keeping the exact cancellation between the endpoint remainder patterns instead of summing the norms of `h` adjacent defects.

Now return to the projected-dilation setting of `NB-310`. Let

\[
T_{N,m}:=P_{U_N}A_m|_{U_N},
\qquad
2\le m\le N,
\qquad
q:=\left\lfloor\frac Nm\right\rfloor,
\]

and let `s_post(N,m)` be the operator norm after removing the exact unit right-singular core `U_q` from `NB-306`. Set

\[
n:=m(q+1)=N+h,
\qquad
1\le h\le m\le N.
\tag{2}
\]

Combining (1) with the exact escape test from `NB-310` gives

\[
\boxed{
0<1-s_{\rm post}(N,m)^2
\le
\frac{m h}{n^2\sigma_{q+1}^2}
\left(
6H_{\lfloor N/h\rfloor}+8+\pi^2
\right),
}
\tag{3}
\]

where

\[
\sigma_j:=\operatorname{dist}(g_j,U_{j-1}).
\]

Using the universal pivot floor from `NB-308`,

\[
\sigma_{q+1}^2
\ge
\frac{3}{2\pi^2(q+1)^2},
\]

and `n=m(q+1)`, equation (3) becomes the completely explicit estimate

\[
\boxed{
0<1-s_{\rm post}(N,m)^2
\le
\min\left\{
1,
\frac{2\pi^2}{3}\,
\frac hm
\left(
6H_{\lfloor N/h\rfloor}+8+\pi^2
\right)
\right\}.
}
\tag{4}
\]

Consequently any moving family satisfying

\[
\boxed{
\frac hm
\left(1+H_{\lfloor N/h\rfloor}\right)
\longrightarrow0
}
\tag{5}
\]

has

\[
\boxed{s_{\rm post}(N,m)\longrightarrow1.}
\tag{6}
\]

In particular, in the first post-core strip `N/2<m<=N`, one has `q=1`, `s_post(N,m)=beta_(N+1)(m)`, `n=2m=N+h`, and `sigma_2^2=(log 2)/4`. Hence

\[
\boxed{
0<1-\beta_{N+1}(m)^2
\le
\min\left\{
1,
\frac{2h}{(N+h)\log2}
\left(
6H_{\lfloor N/h\rfloor}+8+\pi^2
\right)
\right\}.
}
\tag{7}
\]

Therefore the exact plateau edge from `NB-306` has a much wider asymptotic right-neighborhood than `NB-310` could prove:

\[
\boxed{
h=2m-N=o(N)
\quad\Longrightarrow\quad
\beta_{N+1}(m)\longrightarrow1.}
\tag{8}
\]

So the square-root-width condition produced by adjacent chaining in `NB-310` was mainly a triangle-inequality loss. The exact endpoint remainder geometry permits every sublinear additive overrun in the first post-core strip, and more generally gives the criterion (5) at arbitrary core depth.

This remains a source-side statement. It does not control occupation by the first-free Ford datum, the finite-section Nyman distance, the arithmetic defect, or RH. It is an upper bound on the post-core defect, not an asymptotic formula and not a lower bound on the gap.

## 1. The endpoint comparison has an exact reciprocal-shell formula

On the reciprocal shell

\[
I_k:=\left(\frac1{k+1},\frac1k\right],
\qquad k\ge1,
\]

the canonical generator has the constant value

\[
g_j|_{I_k}
=
\frac{k\bmod j}{j}.
\tag{9}
\]

Define

\[
e_{N,n}
:=
g_n-\frac Nn g_N.
\tag{10}
\]

Because `(N/n)g_N in U_N`,

\[
\operatorname{dist}(g_n,U_N)
\le
\|e_{N,n}\|_2.
\tag{11}
\]

Equation (9) gives the exact shell value

\[
\boxed{
e_{N,n}(k)
=
\frac{(k\bmod n)-(k\bmod N)}{n}.}
\tag{12}
\]

This identity is the cancellation that is lost by the adjacent triangle inequality in `NB-310`. Indeed the adjacent scaled defects

\[
d_j:=g_j-\frac{j-1}{j}g_{j-1}
\]

still telescope to

\[
e_{N,n}
=
\sum_{j=N+1}^{n}\frac jn d_j,
\tag{13}
\]

but (12) estimates their sum as one remainder pattern rather than paying separately for all `h=n-N` terms.

The Hilbert norm is

\[
\|e_{N,n}\|_2^2
=
\sum_{k\ge1}
\frac{|e_{N,n}(k)|^2}{k(k+1)}.
\tag{14}
\]

We now bound that sum directly.

## 2. Each `n`-shell block has only a controlled remainder mismatch

Write

\[
k=bn+s,
\qquad
b\ge0,
\qquad
0\le s<n,
\]

and for `b>=1` put

\[
t_b:=bh\bmod N.
\tag{15}
\]

Since `n=N+h`, reduction modulo `N` gives

\[
k\bmod N
=(s+t_b)\bmod N,
\]

where the representative is taken in `{0,...,N-1}`. Thus the unweighted squared energy in the `b`-th `n`-block is

\[
E_b
:=
\sum_{s=0}^{n-1}
|e_{N,n}(bn+s)|^2.
\tag{16}
\]

There are two cases.

### Case 1: `t_b <= N-h`

For `0<=s<N-t_b`, equation (12) gives numerator `-t_b`; for the remaining `h+t_b` values of `s` it gives numerator `N-t_b`. Therefore

\[
E_b
=
\frac{
(N-t_b)t_b^2+(h+t_b)(N-t_b)^2
}{n^2}.
\tag{17}
\]

Since `N-t_b<=N<n`,

\[
E_b
\le h+t_b.
\tag{18}
\]

Also `t_b=bh mod N <= bh`, hence

\[
E_b\le (b+1)h.
\tag{19}
\]

### Case 2: `t_b>N-h`

Write

\[
u:=N-t_b,
\qquad
0<u<h.
\]

The numerator in (12) then has exactly three plateau values:

- `-(N-u)` on `u` positions;
- `u` on `N` positions;
- `N+u` on `h-u` positions.

Consequently

\[
E_b
=
\frac{
u(N-u)^2+Nu^2+(h-u)(N+u)^2}{n^2}.
\tag{20}
\]

Using `u<h<=N` and `n>=N`,

\[
E_b\le 6h.
\tag{21}
\]

Equations (19) and (21) therefore imply uniformly for all `b>=1`

\[
\boxed{E_b\le6(b+1)h.}
\tag{22}
\]

There is also the trivial bound

\[
\boxed{E_b\le n\le2N,}
\tag{23}
\]

because the difference of the two remainders in (12) has absolute value at most `n`.

## 3. Weighted block summation gives the endpoint modulus

For `b>=1`, every shell in the `b`-th block has `k>=bn`. Therefore

\[
\sum_{k=bn}^{(b+1)n-1}
\frac{|e_{N,n}(k)|^2}{k(k+1)}
\le
\frac{E_b}{b^2n^2}.
\tag{24}
\]

Let

\[
B:=\left\lfloor\frac Nh\right\rfloor.
\]

For `1<=b<=B` use (22), while for `b>B` use (23). This gives

\[
\begin{aligned}
\sum_{b=1}^{\infty}
\sum_{k=bn}^{(b+1)n-1}
\frac{|e_{N,n}(k)|^2}{k(k+1)}
&\le
\frac{6h}{n^2}
\sum_{b=1}^{B}
\frac{b+1}{b^2}
+
\frac{2N}{n^2}
\sum_{b>B}\frac1{b^2}\\
&\le
\frac{h}{n^2}
\left(
6H_B+\pi^2+4
\right).
\end{aligned}
\tag{25}
\]

For the last step, use

\[
\sum_{b=1}^{B}\frac1{b^2}\le\frac{\pi^2}{6},
\qquad
\sum_{b>B}\frac1{b^2}\le\frac1B,
\tag{26}
\]

and

\[
\frac NB\le2h.
\tag{27}
\]

Indeed, if `N/h>=2`, then `B=floor(N/h)>=(N/h)/2`; if `1<=N/h<2`, then `B=1` and again `N/B<2h`.

It remains to handle the block `b=0`. Formula (12) vanishes for `1<=k<N`. Only the `h` shells `N<=k<n` can contribute. Since `|e_(N,n)(k)|<=1` and `k>=N`,

\[
\sum_{k=1}^{n-1}
\frac{|e_{N,n}(k)|^2}{k(k+1)}
\le
\frac h{N^2}
\le
\frac{4h}{n^2},
\tag{28}
\]

where `n<=2N` was used in the final inequality.

Combining (25) and (28) proves (1).

A useful scale summary is

\[
\boxed{
\operatorname{dist}(g_{N+h},U_N)^2
\ll
\frac{h}{(N+h)^2}
\left(1+\log\frac Nh\right),
\qquad
1\le h\le N.
}
\tag{29}
\]

The logarithm records how many low-`b` blocks remain in the regime where the accumulated residue shift `bh` has not yet saturated the trivial block-energy bound.

## 4. Substitution into the exact post-core escape identity

`NB-310` uses the first canonical innovation outside the exact dilation core,

\[
w_{q+1}:=(I-P_{U_q})g_{q+1},
\qquad
\|w_{q+1}\|_2=\sigma_{q+1},
\]

and proves the exact escape relation

\[
J_{N,m}w_{q+1}
=
\sqrt m\,(I-P_{U_N})g_n,
\qquad
n=m(q+1),
\tag{30}
\]

where

\[
J_{N,m}:=(I-P_{U_N})A_m|_{U_N}.
\]

Therefore the Rayleigh defect of this explicit post-core vector is

\[
\frac{
\|w_{q+1}\|_2^2-
\|T_{N,m}w_{q+1}\|_2^2
}{
\|w_{q+1}\|_2^2
}
=
\frac{
m\,\operatorname{dist}(g_n,U_N)^2
}{
\sigma_{q+1}^2
}.
\tag{31}
\]

Since `s_post(N,m)` is the supremum of `||T v||/||v||` over the post-core space, (31) and (1) give (3).

Now `NB-308` gives

\[
\sigma_{q+1}^2
\ge
\frac{3}{2\pi^2(q+1)^2}.
\tag{32}
\]

Because `n=m(q+1)`, substitution into (3) cancels the full core-depth factor:

\[
\begin{aligned}
1-s_{\rm post}(N,m)^2
&\le
\frac{m h}{n^2}
\left(6H_{\lfloor N/h\rfloor}+8+\pi^2\right)
\frac{2\pi^2(q+1)^2}{3}\\
&=
\frac{2\pi^2}{3}\frac hm
\left(6H_{\lfloor N/h\rfloor}+8+\pi^2\right).
\end{aligned}
\tag{33}
\]

Adding the trivial upper bound `1` proves (4), and condition (5) proves (6).

This is the central gain over `NB-310`. Its adjacent triangle inequality produced a factor `h^2`; the exact endpoint remainder pattern leaves only `h`, at the price of the natural harmonic factor describing the number of unsaturated residue blocks.

## 5. The first post-core strip admits every sublinear overrun

If

\[
\frac N2<m\le N,
\]

then `q=1`, the exact core is zero, and

\[
s_{\rm post}(N,m)=\beta_{N+1}(m),
\qquad
n=2m=N+h.
\tag{34}
\]

Moreover

\[
\sigma_2^2=\|g_2\|_2^2=\frac{\log2}{4}.
\tag{35}
\]

Substituting (1) directly into (31) and using `m=n/2` proves (7).

Suppose now that `h=o(N)`. Then `n~N`, `B=floor(N/h)->infinity`, and

\[
H_B=O\!\left(1+\log\frac Nh\right).
\]

Writing `x=h/N`, the right side of (7) is bounded by a constant multiple of

\[
x\left(1+\log\frac1x\right),
\]

which tends to zero as `x->0`. This proves (8).

More generally, for every fixed core depth `q`, the relation `N=qm+O(m)` makes `h=o(m)` sufficient for (5). The theorem itself is stronger and retains the exact moving-depth criterion (5), which remains meaningful when `q` also grows.

## 6. Relation to NB-310 and remaining boundary

`NB-310` established that explicit post-core near-isometries exist close to each staircase edge, with the sufficient width

\[
h=o\!\left(\sqrt{\frac{m}{\log n}}\right).
\]

That theorem used the correct first post-core vector, but estimated its escaped product generator by chaining `h` adjacent scaled defects and applying the triangle inequality. The present endpoint identity shows that the adjacent defects cancel strongly in aggregate. The resulting sufficient criterion is instead (5), and in the first strip it includes the full sublinear window `h=o(N)`.

This does **not** determine what happens for a fixed positive fraction of the strip, for example `h~cN` in the first post-core region. In that regime `B` stays bounded and (7) gives only an order-one upper bound. Nor does the argument provide a matching lower bound on `1-s_post^2`; the true defect may be much smaller than (4).

The result is also entirely source-side. It says that a large post-core singular value survives much deeper past the exact-core boundary than `NB-310` could certify. It does not show that the actual Nyman/Ford target occupies that singular direction. No conclusion about the finite-section Nyman distance or RH follows from (1)--(8).

## 7. Prior-art audit

A fresh search was made before publication across the standard neighboring literature on the Nyman--Beurling/Baez-Duarte discrete family, fractional-part Gram matrices and multiplicative autocorrelation, and semigroup/dilation formulations. The closest background remains the classical discrete criterion, the Gram/autocorrelation literature around Vasyunin-type formulas and fractional-part autocorrelation, and the semigroup viewpoint already recorded in `SOURCES.md`.

In the sources reviewed, I did not find the specific endpoint estimate

\[
\left\|g_{N+h}-\frac{N}{N+h}g_N\right\|_2^2
\ll
\frac{h}{(N+h)^2}
\left(1+\log\frac Nh\right)
\]

or its finite-section post-core singular-value consequence (4). This is a search result, not a novelty claim. No external theorem is load-bearing for the proof above, so no new durable source dependency is required.

## 8. Adversarial checks and limitations

The argument was checked against the following failure modes.

First, the block decomposition must treat `s>=N` separately when reducing modulo `N`; this is exactly why Case 2 has three plateaus rather than two. Equation (20) includes all `n=N+h` shell positions.

Second, the estimate `N/B<=2h` remains valid in the endpoint range `h>N/2`: then `B=1` and `N<2h`. Thus no hidden assumption `h<<N` enters the finite bound (1).

Third, block `b=0` cannot be absorbed into the `1/b^2` summation. It is handled separately in (28), and contributes only another `4h/n^2`.

Fourth, the passage from (3) to (4) uses only the proved pivot floor from `NB-308` and the exact identity `n=m(q+1)`; no conditioning estimate is inserted implicitly.

Finally, (4) is one-sided. It constructs a near-isometric post-core direction when its right side is small, but it does not assert that the displayed vector is extremal, that the bound is sharp, or that a comparable lower defect bound holds.

## Conclusion

The post-core boundary layer is substantially wider than the adjacent-defect proof of `NB-310` suggested. Exact shell cancellation between the two endpoints yields

\[
\operatorname{dist}(g_{N+h},U_N)^2
\ll
\frac{h}{(N+h)^2}
\left(1+\log\frac Nh\right),
\]

and therefore

\[
1-s_{\rm post}(N,m)^2
\ll
\frac hm
\left(1+\log\frac Nh\right)
\]

at the first product index beyond the exact dilation core. In the first post-core strip, every sublinear additive overrun `h=2m-N=o(N)` still has `beta_(N+1)(m)->1`.

Thus the loss of the exact unit-singular core at `m=N/2` is followed not merely by a thin square-root neighborhood of near-isometry, but by a full sublinear staircase boundary layer. Any macroscopic decay mechanism for the projected-dilation norm must therefore occur deeper in the linear-to-quadratic transition, or rely on target occupation rather than source geometry alone.
