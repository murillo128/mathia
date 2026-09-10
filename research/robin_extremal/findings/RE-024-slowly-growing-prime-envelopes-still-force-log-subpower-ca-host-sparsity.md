# RE-024 — slowly growing prime envelopes still force log-subpower CA host sparsity

**Status:** `LITERATURE+DERIVED + UNIFORM-DIOPHANTINE-BOUND + GROWING-ENVELOPE-HOST-SPARSITY + COUNTEREXAMPLE-NARROWING + PRIME-RACE-CORNER-COMPATIBILITY + PRIOR-ART-BOUNDED`. `RE-017` turns a small ordinary-prime envelope around a regular self-tangent CA local peak into deep prime-power boundary layers. `RE-018`--`RE-020` sharpen the fixed-envelope case all the way to iterated-logarithmic host sparsity, but explicitly leave growing envelopes untreated because the admissible prime bases and the linear-form constants vary with the envelope width. Keeping that dependence instead of freezing it closes a nontrivial part of the growing-envelope chamber.

For `G>=1` and `Z` large, let `N_G(Z)` count sufficiently large regular self-tangent colossally abundant local peaks `C` with

\[
X:=\log C\le Z
\]

whose ordinary-prime envelope gap `g(C)` from `RE-017` satisfies

\[
g(C)\le G.
\tag{1}
\]

There are absolute constants `A,c>0` such that, uniformly for `G>=1`,

\[
\boxed{
N_G(Z)
\ll
G\,\exp(2G+A)
\left(
G^2\log(2G)+1+\log^*\log Z
\right),
}
\tag{2}
\]

once `Z` is beyond an absolute initial CA range. The implied constant is absolute; changing the harmless initial range changes only `A`.

Consequently, if `H(X)` is eventually nondecreasing and

\[
H(X)=o(\log\log X),
\tag{3}
\]

then the number `N_H(Z)` of such peaks with `X<=Z` and `g(C)<=H(X)` satisfies

\[
\boxed{
N_H(Z)=(\log Z)^{o(1)}.
}
\tag{4}
\]

More quantitatively, if for some fixed `c_0>=0`

\[
H(X)\le c_0\log\log X+o(\log\log X),
\tag{5}
\]

then the same argument gives the crude but explicit calibration

\[
\boxed{
N_H(Z)\le(\log Z)^{2c_0+o(1)}.
}
\tag{6}
\]

Thus the fixed-`G` hypothesis in the host-sparsity mechanism of `RE-020` is not a hard phase boundary. Envelopes may grow to infinity, even through arbitrary `o(log log X)` functions, while the admissible self-tangent peak hosts remain subpower in `log Z`. The coupled boundary-mass budget also halves the exponential coefficient in the quantitative `c_0 log log X` calibration compared with treating the two boundary bases independently.

There is also a direct compatibility with the newer race geometry of `RE-023`. Since `H(X)=o(log log X)` is in particular `o(sqrt(X))`, and `p~X` for the last active first-layer prime, every hypothetical Robin-counterexample sequence inside (3) necessarily obeys

\[
\boxed{
\mathcal E_\vartheta(p)\to-\sqrt2,
\qquad
\liminf\mathcal E_{\pi_\ell}(p)\ge\sqrt2.
}
\tag{7}
\]

So a slowly growing-envelope escape must satisfy **both** restrictions simultaneously: it lies on only `(log Z)^{o(1)}` admissible peak hosts up to event height `Z`, and those hosts must realize the same opposite-side selected prime-race corner as the entire sub-square-root envelope chamber. This remains a necessary-condition theorem, not an exclusion of Robin counterexamples.

## 1. The envelope bound gives a coupled growing base alphabet

`RE-017` proves that every prime factor `r` appearing at either adjacent CA boundary of a sufficiently large peak satisfies

\[
\log r<2g(C)+2+o(1).
\tag{8}
\]

Under (1), after one absolute initial range,

\[
\boxed{r<e^{2G+3}.}
\tag{9}
\]

The two bases selected from the opposite peak boundaries are much more tightly coupled than this individual bound suggests. At each peak choose one event atom deterministically from the left boundary and one from the right boundary; for a tied transition, choose for example the smaller prime base. Call the selected bases `r` and `s`. If `w_-` and `w_+` are the logarithmic masses of the two complete adjacent CA quotients, then

\[
\log r\le w_-,
\qquad
\log s\le w_+.
\]

The stronger total boundary-mass budget already proved in `RE-017` is

\[
w_-+w_+<2g(C)+2+o(1).
\]

Therefore, after enlarging the same absolute initial range,

\[
\boxed{rs<e^{2G+3}.}
\tag{10}
\]

Put `Y_G=e^(2G+3)`. Even if primality is discarded completely, the number of possible ordered selected base pairs is at most

\[
\boxed{
\sum_{2\le m\le Y_G/2}
\left\lfloor\frac{Y_G}{m}\right\rfloor
\ll Y_G\log Y_G
\ll G e^{2G+3}.
}
\tag{11}
\]

Thus one does not pay two independent `e^(2G)` alphabet factors. The same peak-clearance inequality that compresses the individual boundary factors also couples the two choices through their product.

The two chosen event coordinates `x<y` satisfy, again by `RE-017`,

\[
0<y-x<G+1.
\tag{12}
\]

For large enough `x` the two bases must be distinct. Indeed, for one fixed base `r`, write

\[
S_{r,j}=r+\cdots+r^j,
\qquad
\lambda_{r,j}=\log(1+S_{r,j}^{-1}),
\qquad
A_{r,j}=\frac{\log r}{\lambda_{r,j}},
\]

so that

\[
A_{r,j}=\eta_{r,j}\log\eta_{r,j}.
\tag{13}
\]

The elementary bounds

\[
\frac1{S+1}\le\log(1+S^{-1})\le\frac1S
\]

give

\[
\frac{A_{r,j+1}}{A_{r,j}}
=\frac{\lambda_{r,j}}{\lambda_{r,j+1}}
\ge
\frac{S_{r,j+1}}{S_{r,j}+1}
\ge2.
\tag{14}
\]

On the other hand, for `f(t)=t log t`, two coordinates with `0<y-x<=G+1` obey

\[
\frac{f(y)}{f(x)}=1+O\!\left(\frac Gx\right).
\tag{15}
\]

Thus distinct events from the same base cannot form the two selected boundaries once `x` exceeds an absolute multiple of `G+1`. All same-base exceptions lie in a low initial range and are absorbed by the right side of (2).

## 2. Two repeated collisions with variable bases still produce a uniform linear form

Fix one ordered pair of distinct primes `(r,s)` satisfying (10), and order all selected boundary pairs using these bases by their left event coordinate:

\[
x_n=\eta_{r,j_n},
\qquad
y_n=\eta_{s,k_n},
\qquad
0<y_n-x_n\le G+1.
\tag{16}
\]

As in `RE-019`--`RE-020`, the layer indices are strictly increasing after discarding the finite initial range. Put

\[
a_n=j_{n+1}-j_n,
\qquad
b_n=k_{n+1}-k_n,
\qquad
m_n=\max(a_n,b_n).
\tag{17}
\]

The exact event parameter preserves the additive collision accuracy uniformly in the now-variable width. Since `A=f(eta)` and `f'(t)=log t+1`, equation (15) at two successive collisions gives

\[
\frac{A_{r,j_n+a_n}/A_{r,j_n}}
     {A_{s,k_n+b_n}/A_{s,k_n}}
=1+O\!\left(\frac G{x_n}\right).
\tag{18}
\]

The conversion from `A` to geometric sums is also uniform. From

\[
S_{r,j}
\le
\frac{A_{r,j}}{\log r}
\le S_{r,j}+1
\tag{19}
\]

and `log r<=2G+3`, one obtains

\[
r^{-j_n}+s^{-k_n}
\ll
\frac{G}{x_n\log x_n}.
\tag{20}
\]

Using the exact formula

\[
S_{r,j}=\frac{r(r^j-1)}{r-1}
\]

in (18), exactly as in `RE-020` but retaining the dependence on `G`, gives

\[
\boxed{
\frac{r^{a_n}}{s^{b_n}}
=1+O\!\left(\frac G{x_n}\right).
}
\tag{21}
\]

Therefore, once `x_n` is larger than an absolute multiple of `G`,

\[
\boxed{
|a_n\log r-b_n\log s|
\ll\frac G{x_n}.
}
\tag{22}
\]

The important point is that no fixed-base asymptotic constant has been hidden here. The loss from letting the envelope and the bases grow is explicit: only the factor `G` in the upper bound and the logarithmic heights of `r,s` in the Diophantine lower bound remain.

## 3. Matveev gives a uniform `x^(c/G^2)` jump

For distinct primes `r,s`, multiplicative independence makes

\[
\Lambda=a\log r-b\log s
\]

nonzero for positive integers `a,b`. A standard two-logarithm specialization of Matveev's explicit lower bound supplies an absolute constant `K>0` such that, with `m=max(a,b)>=2`,

\[
\boxed{
|a\log r-b\log s|
\ge
\exp\!\left(
-K(\log r)(\log s)\log(em)
\right).
}
\tag{23}
\]

This is the same external theorem already anchored for `RE-020`, now used before freezing `r` and `s`. The coupled pair budget (10) gives `log r+log s<2G+3`, so arithmetic-geometric mean yields

\[
(\log r)(\log s)
\le\frac{(\log r+\log s)^2}{4}
\le\left(G+\frac32\right)^2
\ll G^2.
\tag{24}
\]

Combining (22)--(24), there is an absolute `c>0` such that

\[
\boxed{
\log(em_n)
\ge
\frac{c}{G^2}
\log\!\left(\frac{x_n}{c^{-1}G}\right).
}
\tag{25}
\]

Equivalently,

\[
\boxed{
m_n
\ge
e^{-1}
\left(\frac{x_n}{c^{-1}G}\right)^{c/G^2}.
}
\tag{26}
\]

For fixed `G`, this recovers the positive event-scale power jump of `RE-020`. The new information is the uniform degradation: the usable exponent is only of order `G^{-2}` as the envelope grows.

This scale is sufficient. If

\[
\log x_n\ge A_1G^2\log(2G)
\tag{27}
\]

for a sufficiently large absolute `A_1`, then (26) implies

\[
m_n\ge\exp\!\left(c_1\frac{\log x_n}{G^2}\right)
\tag{28}
\]

with another absolute `c_1>0`.

## 4. Each base pair has only a polynomial-in-`G` initial segment and a tower-like tail

The event-size bounds of `RE-017` imply

\[
r^j\log r
\le
\eta_{r,j}\log\eta_{r,j}
<3r^j\log r.
\tag{29}
\]

Hence if `x=eta_(r,j)` lies below the threshold in (27), then

\[
j\ll G^2\log(2G).
\tag{30}
\]

Because `j_n` is strictly increasing, a fixed ordered pair `(r,s)` contributes at most

\[
O(G^2\log(2G))
\tag{31}
\]

collisions before (27) begins.

Beyond that threshold, a large jump in either index forces a large next event coordinate. From (29), if `m_n=a_n` then

\[
\log x_{n+1}\gg a_n;
\]

if `m_n=b_n`, the same estimate applies first to `y_(n+1)` and then to `x_(n+1)` because their additive difference is at most `G+1`. Thus (28) yields

\[
\boxed{
\log x_{n+1}
\ge
c_2\exp\!\left(
c_1\frac{\log x_n}{G^2}
\right).
}
\tag{32}
\]

After rescaling

\[
v_n=\frac{c_1}{4G^2}\log x_n,
\]

the threshold (27) can be increased by another absolute factor so that (32) implies

\[
\boxed{v_{n+1}\ge e^{v_n}.}
\tag{33}
\]

Therefore the number of post-threshold collisions for one base pair below `Z` is

\[
O(1+\log^*\log Z).
\tag{34}
\]

Combining (31) and (34), every admissible ordered pair contributes

\[
\boxed{
O\!\left(
G^2\log(2G)+1+\log^*\log Z
\right)
}
\tag{35}
\]

selected peak hosts. Multiplying by the coupled pair count (11), and absorbing the low-coordinate same-base exceptions, proves (2).

No prime-number theorem is needed for this counting step. Deliberately counting all integer pairs with product at most `Y_G`, rather than estimating prime pairs, already removes the spurious second independent exponential alphabet factor and is enough for the applications below.

## 5. `o(log log X)` envelopes are subpower in `log Z`

Let `H` satisfy (3), and count peaks with `X<=Z` and `g(C)<=H(X)`. By eventual monotonicity,

\[
g(C)\le H(Z),
\]

so (2) applies with

\[
G=H(Z).
\]

Taking logarithms of its right side gives

\[
\log N_H(Z)
\le
2H(Z)
+O\!\left(
\log(2+H(Z))+\log(1+\log^*\log Z)
\right).
\tag{36}
\]

Under `H(Z)=o(log log Z)`, the right side is `o(log log Z)`. Exponentiating proves (4).

If instead (5) holds, the leading exponential factor is

\[
e^{2H(Z)+O(1)}
\le
(\log Z)^{2c_0+o(1)},
\]

while the extra factor `H(Z)` and the remaining factors in (2) are `(log Z)^{o(1)}`. This proves (6).

This is stronger than applying the generic deep-layer count of `RE-017` to the same regime. That result gives `Z^epsilon` for every fixed `epsilon>0` when `g=o(log X)`; here the stronger Diophantine synchronization inherited from `RE-020` reduces `o(log log X)` envelopes to **subpower sparsity in `log Z` itself**.

## 6. Coupling to the selected prime-race corner

`RE-023` proves that if the ordinary envelope of a regular self-tangent local peak satisfies

\[
g=o(\sqrt p),
\]

then any Robin-counterexample sequence must satisfy the joint normalized race condition (7). Along (3), `p~X` and

\[
H(X)=o(\log\log X)=o(\sqrt X),
\]

so every peak counted asymptotically by `N_H` lies in that sub-square-root chamber.

Consequently a hypothetical counterexample family with slowly growing envelopes cannot choose independently between the event-ladder and prime-race obstructions. Its host coordinates are constrained by (4), while at those same coordinates the standard and reciprocal prime errors must approach opposite sides of the selected corner (7). This is more rigid than either statement alone, but no probabilistic independence or sign cancellation is assumed between them.

In particular, sparsity still does **not** imply Robin. A set of `(log Z)^{o(1)}` selected inputs can support arbitrarily exceptional values of a deterministic arithmetic function unless a further source-specific estimate couples the host geometry to the finite-annulus mixed race of `RE-022`.

## 7. Prior-art and novelty boundary

The external Diophantine input is classical. Matveev's 2000 theorem gives explicit lower bounds for nonzero homogeneous linear forms in logarithms of algebraic numbers; for the rational integers `r,s`, its standard two-logarithm specialization has exactly the logarithmic-height dependence used in (23). `SOURCES.md` already contains this source because it is load-bearing for `RE-020`.

Alaoglu--Erdos remains the classical CA source for exponent thresholds, consecutive-CA quotient structure, and the unresolved exact two-prime simultaneous-jump obstruction. Mantovanelli's August 2026 work is the closest current prior art for the self-tangent prime-layer event representation. None of those sources is being credited with a growing-envelope host theorem here.

A fresh targeted search of current CA transition work, Robin-extremal literature, and applications of linear forms in logarithms to CA prime-power transitions did not locate the two-parameter estimate (2) or its `H=o(log log X)` consequence (4). No novelty is claimed for Matveev's theorem, for generic sparse intersections of exponential sequences, or for the fixed-base result already proved in `RE-020`. The repository-level delta is the explicit bookkeeping of the **base-height dependence** in that argument, together with the coupled product constraint (10) inherited from the peak-clearance budget. This shows that the fixed-envelope mechanism survives a quantitatively growing alphabet without paying for two independent boundary alphabets.

No new source anchor is required.

## 8. Falsification boundaries and research consequence

The remaining `e^(2G)` scale in (2) is still a crude base-pair counting loss, not a predicted sharp constant. Treating the two selected boundary bases independently would give `r,s<e^(2G+3)` and waste another `e^(2G)` factor. The actual peak-clearance budget couples them through `rs<e^(2G+3)`, so counting even all integer pairs costs only `O(G e^(2G))`. Sharper counting of prime pairs may improve polynomial or logarithmic factors; removing the `e^(2G)` scale itself would require additional arithmetic or transition structure beyond this product budget.

The local-peak hypothesis remains load-bearing because `RE-017` obtains the base compression from the secant-clearance condition. The theorem is not asserted for arbitrary regular self-tangent states. The envelope `g` is the consecutive ordinary-prime envelope containing the two actual adjacent CA transitions, not necessarily the actual CA gap.

The Matveev step concerns **successive occurrences of one selected ordered base pair**. It does not give a single-collision lower bound for `|eta_(r,j)-eta_(s,k)|`, does not solve the Alaoglu--Erdos exact-tie problem, and does not make the source race random or independent of the selector. If a hidden dependence stronger than `(log r)(log s)` were required in the two-logarithm specialization of (23), the `G^{-2}` exponent and hence the stated threshold would need correction; this is the primary literature-audit checkpoint.

The result materially reduces the growing-envelope branch left open by `RE-020`: any hypothetical counterexample family with `g=o(log log X)` must now occupy a `(log Z)^{o(1)}` event-host set and simultaneously satisfy the selected race corner of `RE-023`. The remaining obstruction is sharper than generic sparsity: one must either push the uniform Diophantine argument to wider envelopes, or prove that the finite-annulus mixed race of `RE-022` cannot realize its `2sqrt(2)` threshold on this increasingly thin CA-selected host set.