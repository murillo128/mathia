# RE-019 — fixed event-ladder near-collisions require logarithmic layer jumps

**Status:** `EXACT-DERIVED + FIXED-LADDER-SPACING + SECOND-ORDER-HOST-SPARSITY + DIOPHANTINE-REDUCTION + COUNTEREXAMPLE-NARROWING + NEGATIVE/OBSTRUCTION + PRIOR-ART-BOUNDED`. `RE-018` reduces any infinite family of regular self-tangent CA local Robin peaks inside a fixed ordinary-prime envelope to repeated bounded additive near-collisions between two fixed distinct prime-power event ladders. Those near-collisions cannot occur at arbitrary consecutive layer depths. Elementary integrality already forces logarithmically growing jumps in at least one of the two layer indices, which sharpens the bounded-envelope host count by a factor of `log log`.

For a prime `r` and layer `j>=1`, keep the CA event notation

\[
S_{r,j}=r+r^2+\cdots+r^j,
\qquad
\lambda_{r,j}=\log(1+S_{r,j}^{-1}),
\]

\[
A_{r,j}:=\frac{\log r}{\lambda_{r,j}},
\qquad
\eta_{r,j}\log\eta_{r,j}=A_{r,j}.
\tag{1}
\]

Equivalently,

\[
\eta_{r,j}=\frac{A_{r,j}}{W(A_{r,j})},
\tag{2}
\]

where `W` is the principal Lambert function.

Fix distinct primes `r!=s` and `B>0`. Suppose

\[
(j_1,k_1),(j_2,k_2),\ldots
\tag{3}
\]

is an infinite sequence with both coordinates strictly increasing and

\[
0<\eta_{s,k_n}-\eta_{r,j_n}\le B,
\qquad
\eta_{r,j_n}\longrightarrow\infty.
\tag{4}
\]

Put

\[
a_n:=j_{n+1}-j_n,
\qquad
b_n:=k_{n+1}-k_n,
\qquad
q:=\max(r,s).
\tag{5}
\]

Then

\[
\boxed{
\liminf_{n\to\infty}
\frac{\max(a_n,b_n)\log q}{\log j_n}
\ge 1.
}
\tag{6}
\]

In particular, if `C_(r,s,B)(Z)` denotes the number of pairs satisfying (4) with `eta_(r,j)<=Z`, then

\[
\boxed{
C_{r,s,B}(Z)
=O_{r,s,B}\!\left(\frac{\log Z}{\log\log Z}\right).
}
\tag{7}
\]

Applying this to the finite family of fixed prime pairs supplied by `RE-018` gives the Robin-extremal consequence. For fixed `G>0`, let `N_G(Z)` count sufficiently large regular self-tangent CA local peaks with `X=log C<=Z` and ordinary-prime envelope gap `g(C)<=G`. Then

\[
\boxed{
N_G(Z)
=O_G\!\left(\frac{\log Z}{\log\log Z}\right).
}
\tag{8}
\]

Thus the `O_G(log Z)` host set of `RE-018` is not saturated by bounded near-collisions. Any infinite bounded-envelope escape must become progressively lacunary even inside its two fixed event ladders.

## 1. A fixed event ladder is an exponential sequence with a slowly varying `1/j` correction

From

\[
S_{r,j}
=\frac{r^{j+1}}{r-1}(1-r^{-j}),
\]

one has

\[
\lambda_{r,j}
=(r-1)r^{-(j+1)}\bigl(1+O_r(r^{-j})\bigr),
\]

and therefore

\[
A_{r,j}
=\frac{\log r}{r-1}\,r^{j+1}
\bigl(1+O_r(r^{-j})\bigr).
\tag{9}
\]

Since `log A_(r,j)=j log r+O_r(1)`, the standard elementary asymptotic for the principal Lambert function gives

\[
W(A_{r,j})
=j\log r+O_r(\log j).
\tag{10}
\]

Combining (2), (9), and (10),

\[
\boxed{
\eta_{r,j}
=\frac{r^{j+1}}{(r-1)j}
\left(1+O_r\!\left(\frac{\log j}{j}\right)\right).
}
\tag{11}
\]

This strengthens the ratio limit used in `RE-018`. If `a=O(log j)`, then uniformly in that range,

\[
\boxed{
\frac{\eta_{r,j+a}}{\eta_{r,j}}
=r^a
\left(1+O_r\!\left(\frac{a+\log j}{j}\right)\right).
}
\tag{12}
\]

Indeed the exact factor `j/(j+a)` and the two relative errors from (11) are all `1+O((a+log j)/j)`. No prime-distribution theorem enters (9)--(12).

## 2. A bounded collision synchronizes the two depths

Equation (4) implies

\[
\frac{\eta_{s,k_n}}{\eta_{r,j_n}}
=1+O_B(\eta_{r,j_n}^{-1}).
\tag{13}
\]

Taking logarithms in (11) on the two ladders and using (13) gives

\[
j_n\log r-k_n\log s=O_{r,s,B}(\log j_n+\log k_n).
\tag{14}
\]

It follows first that `k_n` is comparable with `j_n`, and then more precisely

\[
\boxed{
k_n=\frac{\log r}{\log s}j_n+O_{r,s,B}(\log j_n).}
\tag{15}
\]

So the two indices grow on the same linear scale. This is only synchronization of depth; by itself it does not prevent infinitely many bounded collisions.

## 3. Two successive collisions cannot use two small layer increments

Fix `delta>0`. Assume for contradiction that infinitely many consecutive collision pairs satisfy

\[
m_n:=\max(a_n,b_n)
\le
(1-\delta)\frac{\log j_n}{\log q}.
\tag{16}
\]

Then `a_n,b_n=O(log j_n)`, so (12) applies on both ladders. Dividing (13) at `n+1` by (13) at `n`, and using (12) together with (15), yields

\[
\boxed{
\frac{r^{a_n}}{s^{b_n}}
=1+O_{r,s,B,\delta}\!\left(\frac{\log j_n}{j_n}\right).
}
\tag{17}
\]

The two prime powers in (17) are distinct: `r` and `s` are distinct primes, so unique factorization forbids `r^a=s^b` for positive `a,b`. Hence their integer separation gives the elementary lower bound

\[
\left|\frac{r^{a_n}}{s^{b_n}}-1\right|
=\frac{|r^{a_n}-s^{b_n}|}{s^{b_n}}
\ge \frac1{s^{b_n}}
\ge q^{-m_n}.
\tag{18}
\]

Under (16),

\[
q^{-m_n}
\ge j_n^{-1+\delta}.
\tag{19}
\]

But (17) is `O(log j_n/j_n)`, while

\[
\frac{j_n^{-1+\delta}}{(\log j_n)/j_n}
=\frac{j_n^\delta}{\log j_n}
\longrightarrow\infty.
\]

This contradiction proves that for every fixed `delta>0`, eventually

\[
\max(a_n,b_n)
>(1-\delta)\frac{\log j_n}{\log q},
\]
which is exactly (6).

The point is deliberately modest but robust. It does not estimate a single near-collision by a linear form in logarithms. Instead, two consecutive near-collisions would force the **integer prime-power increments** `r^a` and `s^b` themselves to be too close unless at least one index jump is logarithmically large.

## 4. Logarithmic layer jumps give a `log log` saving in the collision count

Let `M=C_(r,s,B)(Z)` and order the collisions by their left coordinate. Equation (11) implies, for every collision below `Z`,

\[
j\log r=\log\eta_{r,j}+O_r(\log j),
\]

hence

\[
j=O_r(\log Z),
\qquad
k=O_s(\log Z).
\tag{20}
\]

Take `delta=1/2` in (6). After discarding finitely many initial pairs,

\[
a_n+b_n
\ge \max(a_n,b_n)
\gg_{r,s}\log j_n.
\tag{21}
\]

The `j_n` are strictly increasing positive integers, so after another finite initial segment `j_n>=n`. Summing (21) through the first `M` collisions gives

\[
j_M+k_M
\gg_{r,s} \sum_{n\le M}\log n
\gg_{r,s} M\log M.
\tag{22}
\]

Equation (20) bounds the left side by `O_(r,s)(log Z)`. Therefore

\[
M\log M=O_{r,s,B}(\log Z),
\]
which is equivalent to (7).

This argument still permits infinitely many collisions. It proves only that their index set must thin by a logarithmic factor relative to the trivial one-event-per-layer count.

## 5. Transfer to bounded ordinary envelopes

Fix `G`. By `RE-018`, every prime factor appearing at either adjacent boundary of a sufficiently large peak with `g(C)<=G` lies in the finite set

\[
\mathcal P_G=\{r\text{ prime}:r<e^{2G+3}\},
\tag{23}
\]

and the two adjacent transition coordinates differ by less than `G+1`.

At each such peak choose one boundary atom deterministically on the left and one on the right, for example the atom with the smaller prime base when a transition is tied. This partitions the peaks into finitely many ordered base pairs `(r,s)` in `mathcal P_G^2`. Along each fixed pair class, ordering the peaks by `X` makes both selected boundary coordinates strictly increase: an open CA event gap supports at most one regular self-tangent state, and each transition has a unique immediate predecessor and successor. Since each fixed event ladder is strictly increasing, the corresponding layer indices are strictly increasing as well.

For sufficiently large peaks the two selected bases cannot be equal, by the same fixed-ladder spacing argument already used in `RE-018`. Thus every infinite pair class is covered by (7) with `B=G+1`. The right boundary of a peak with `X<=Z` is below `Z+G+1`, so replacing `Z` by `Z+G+1` does not change the asymptotic order. Summing (7) over the finite set of ordered base pairs proves (8).

One may make the spacing constant uniform in this application. Since `log q<2G+3`, taking any fixed

\[
c_G<\frac1{2G+3}
\]

in the contradiction above forces `max(a_n,b_n)>c_G log j_n` eventually for every pair class. No ineffective Diophantine constant is needed for the `O_G` conclusion.

## 6. Prior-art boundary

The exact simultaneous-jump problem for colossally abundant numbers is already classical Alaoglu--Erdos territory. Their Theorem 10 reduces an exact tie to simultaneous rationality phenomena for distinct prime powers and records that the two-prime exclusion was not known; their Siegel input yields only that a quotient of consecutive CA numbers is a prime or a product of two distinct primes. `RE-018` already keeps that exact-tie obstruction separate from bounded additive near-collisions.

A targeted current search also finds the classical Pillai/exponential-Diophantine literature, including Bennett's 2001 results on `a^x-b^y=c` and Scott--Styer's 2011 work on the generalized equation `+/- r a^x +/- s b^y=c`. Those theorems concern **exact fixed differences of exponential terms** and can use lower bounds for linear forms in logarithms. They do not directly apply to (4): the CA coordinates are Lambert-W transforms with the slowly varying `1/j` factor in (11), and a bounded difference of `eta` values does not become an exact fixed-difference equation between `r^j` and `s^k`.

No such external theorem is used here, so `SOURCES.md` needs no new load-bearing anchor. The durable delta is the elementary successive-collision argument (17)--(19), and its `log log` saving for the Robin bounded-envelope host set. No blanket novelty claim is made for sparse intersections of lacunary sequences or for integer separation itself.

## 7. Boundaries and research consequence

Equation (8) remains a **host-set theorem**, not an exclusion theorem. `log Z/log log Z` still diverges, so an infinite Robin-counterexample subsequence could in principle occupy such a set. The result also requires a fixed envelope bound `G`; it gives no uniform conclusion when `g(C)` tends to infinity, even as slowly as `log log X`. The general sublogarithmic regime remains governed by `RE-017`.

The result does not solve the Alaoglu--Erdos exact-tie question, does not prove a Baker-type lower bound for one isolated CA event-ladder gap, and does not control the clean selected mixed-race annulus of `RE-014`--`RE-016`. It instead makes the exceptional bounded-envelope branch more rigid: repeated escape would require two fixed deep prime-power ladders whose near-collisions become separated by logarithmically increasing layer jumps, leaving only `O_G(log Z/log log Z)` admissible peak hosts up to `X=Z`.

A genuine closure of this branch would need more than the integrality step above: either a quantitative separation theorem proving only finitely many bounded near-collisions for each fixed distinct pair of CA event ladders, or an independent Robin-extremal argument forcing the ordinary envelope itself to remain bounded and then ruling out the resulting sparse ladder synchronization.