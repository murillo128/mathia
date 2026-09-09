# MC-179 — Support-only smooth remainders force growing prime-extraction depth

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `RATE-BUDGET`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-178` leaves two plausible escapes from the Chinis one-large-prime ceiling at polynomial short-interval scales: obtain signed cancellation inside the smooth remainder, or iterate the factor extraction until the complementary variable is genuinely short. The second escape is not a bounded-depth repair if the terminal smooth sector is still disposed of only by support cardinality.

Fix

\[
0<\theta<1,
\qquad H=X^\theta,
\tag{1}
\]

and let

\[
\Psi(X,y):=\#\{n\le X:P^+(n)\le y\}
\tag{2}
\]

be the count of `y`-smooth integers. For a fixed `A>=1` put

\[
y=(\log X)^A.
\tag{3}
\]

The classical smooth-number estimate recorded in Montgomery--Vaughan, Corollary 7.9, gives

\[
\boxed{
\Psi(X,(\log X)^A)=X^{1-1/A+o(1)}.
}
\tag{4}
\]

Thus shrinking the terminal cutoff from the polynomial regime of `MC-178` to a fixed polylogarithmic cutoff does make the smooth sector power-sparse. But there is an exact cost.

First, if `a_n` is any `1`-bounded sequence supported on the `y`-smooth integers and

\[
V_a(X,H)
:=
\int_X^{2X}
\left|\sum_{x<n\le x+H}a_n\right|^2\,dx,
\tag{5}
\]

then the pure support/cardinality estimate is

\[
\boxed{
V_a(X,H)
\le (H+1)H\,\Psi(3X,y).
}
\tag{6}
\]

Consequently `(3)` and `(4)` give

\[
V_a(X,H)
\le
X^{1+2\theta-1/A+o(1)}.
\tag{7}
\]

The fixed-power local-variance currency of `MC-177` is

\[
XH^{2-\eta}
=
X^{1+2\theta-\theta\eta},
\qquad 0<\eta\le1.
\tag{8}
\]

Therefore a terminal smooth sector that is discarded **only through `(6)`** reaches the target exponent `(8)` only when

\[
\boxed{
\frac1A\ge\theta\eta.
}
\tag{9}
\]

Equivalently, to buy a fixed local suppression `eta` by support sparsity alone one must push the smoothness cutoff down at least to the polylogarithmic scale

\[
y\le (\log X)^{1/(\theta\eta)}
\tag{10}
\]

at exponent level. A fixed polynomial cutoff `y=X^delta` cannot do this, exactly as `MC-178` found: its smooth sector has positive limiting density.

Now consider the other side of the decomposition. Suppose a prime-by-prime factor-extraction scheme is required, uniformly for every square-free `n<=X` outside the terminal `y`-smooth class, to remove at most `r=r(X)` individual prime factors larger than `y` and leave a complementary factor at the mean-value length

\[
m\le \frac XH=X^{1-\theta}.
\tag{11}
\]

Then necessarily

\[
\boxed{
r(X)
\ge
\left(\frac\theta A+o(1)\right)
\frac{\log X}{\log\log X}.
}
\tag{12}
\]

Combining `(9)` and `(12)` yields the rate tradeoff

\[
\boxed{
r(X)
\ge
\left(\theta^2\eta+o(1)\right)
\frac{\log X}{\log\log X}
}
\tag{13}
\]

for this method class whenever the terminal support estimate itself is supposed to supply a fixed `eta>0` in the local variance budget.

Hence **no fixed-depth prime-by-prime large-factor decomposition can turn Chinis's smooth-remainder strategy into a fixed-power polynomial-window variance gain merely by lowering the terminal cutoff and continuing to discard the final smooth sector by cardinality.** The depth must diverge. At the direct-transfer optimum of `MC-177`, `theta=2/3`, this becomes

\[
r(X)
\ge
\left(\frac{4\eta}{9}+o(1)\right)
\frac{\log X}{\log\log X}.
\tag{14}
\]

In particular, diagonal/square-root local variance (`eta=1`) would require at least

\[
\left(\frac49+o(1)\right)
\frac{\log X}{\log\log X}
\tag{15}
\]

individual large-prime removals in the worst case if the terminal smooth sector is paid for only by support.

This does **not** rule out an iterated Dirichlet-polynomial method. It says that the viable escape identified in `MC-178` cannot be a bounded number of copies of the same one-prime extraction plus a final cardinality estimate. A successful continuation must instead exploit signed cancellation inside the smooth sector, extract structured composite blocks or many prime factors at once, or control a genuinely growing-depth/multiscale decomposition without losing Möbius orientation.

## 1. The support-only local-variance cost

Let

\[
N_y(x):=\#\{n\in(x,x+H]:P^+(n)\le y\}.
\]

For coefficients supported on this set with `|a_n|<=1`,

\[
\left|\sum_{x<n\le x+H}a_n\right|^2
\le N_y(x)^2
\le (H+1)N_y(x).
\tag{16}
\]

Each smooth integer `n` can contribute to `N_y(x)` for a set of `x` of length at most `H`. Since `H<=X`, every relevant `n` is at most `3X`, and therefore

\[
\int_X^{2X}N_y(x)\,dx
\le H\Psi(3X,y).
\tag{17}
\]

Equations `(16)` and `(17)` prove `(6)`.

For fixed `A>=1`, Montgomery--Vaughan's Corollary 7.9 gives upper and lower bounds which are both

\[
X^{1-1/A+o(1)}
\]

when `y=(log X)^A`. The same exponent holds with `X` replaced by `3X`; this follows directly from the corollary, or by squeezing `(log X)^A` between `(log(3X))^(A-epsilon)` and `(log(3X))^(A+epsilon)` and then letting `epsilon` tend to zero. This proves `(7)`.

The comparison with `(8)` is then purely algebraic. The standard support disposal `(6)` has the desired exponent only if

\[
1+2\theta-\frac1A
\le
1+2\theta-\theta\eta,
\]

which is exactly `(9)`.

This is deliberately a statement about a **support/cardinality proof step**. It does not assert that Möbius or Liouville signs restricted to the smooth sector actually have variance as large as `(7)`. Phase-sensitive cancellation inside that sector could be much stronger and is one of the explicit surviving routes.

## 2. A square-free worst case forces growing extraction depth

The lower bound `(12)` is elementary once the terminal cutoff is polylogarithmic. Write

\[
L=\log X,
\qquad y=L^A.
\]

By the prime number theorem,

\[
\pi(3y)-\pi(y)
\sim \frac{2y}{\log y}.
\tag{18}
\]

For every fixed `A>=1`, this supplies enough distinct primes in `(y,3y]` to choose

\[
k=
\left\lfloor
\frac{L}{\log(3y)}
\right\rfloor
\tag{19}
\]

of them for all sufficiently large `X`. Let their product be `n`. Then `n` is square-free, so its Möbius value is nonzero, and

\[
n\le (3y)^k\le X.
\tag{20}
\]

If an extraction removes any `r` of these prime factors, the remaining complementary factor contains at least `k-r` primes, each larger than `y`. Hence

\[
m\ge y^{k-r}.
\tag{21}
\]

A uniform guarantee `(11)` therefore requires

\[
(k-r)\log y
\le (1-\theta)L.
\tag{22}
\]

But

\[
k
=
\left(1+o(1)\right)
\frac{L}{A\log L},
\qquad
\log y=A\log L,
\tag{23}
\]

so `(22)` rearranges to `(12)`.

The construction is useful because it remains entirely inside the square-free support of Möbius. The obstruction is not caused by prime powers or by the zero values of `mu`. It is a worst-case factor-size obstruction: when all available extracted primes sit near the terminal threshold, a bounded number of individual removals changes `log n` by only `O(log log X)`, whereas shortening from `X` to `X^(1-theta)` costs `theta log X`.

## 3. The combined sparsity-depth tradeoff

Suppose the decomposition aims for the `MC-177` local variance scale `(8)` and the only estimate on its terminal `y`-smooth contribution is `(6)`. Then `(9)` forces

\[
A\le\frac1{\theta\eta}.
\tag{24}
\]

The extraction lower bound `(12)` is decreasing in `A`. Even at the largest cutoff compatible with `(24)`, it therefore gives

\[
\frac\theta A
\ge\theta^2\eta,
\]

which proves `(13)`.

This makes the tension in `MC-178` quantitative. A large cutoff gives strong one-step shortening but leaves a dense smooth sector. A small cutoff makes support disposal cheap, but each extracted prime then removes too little logarithmic mass and the number of required extractions grows like `log X/log log X`. In this method class there is no fixed-depth setting that buys both a polynomially short complement and a fixed-power terminal variance saving.

The conclusion is stronger than merely observing that `Psi(X,X^delta)` has positive density. It identifies the exact asymptotic depth cost of moving the smooth cutoff far enough down that cardinality can enter the fixed-power Gallagher currency.

## 4. Prior art and novelty assessment

The smooth-number estimate `(4)` is classical. The same Montgomery--Vaughan volume already retained in this line as `MC-S12` states in Corollary 7.9 that for `y=(log x)^a` in a range containing every fixed `a>=1`, `Psi(x,y)` is squeezed between two quantities of order `x^(1-1/a+o(1))`. Hildebrand--Tenenbaum saddle-point theory gives the much more general framework for `Psi(x,y)`. No novelty is claimed for these results.

`MC-178` already audits Jake Chinis's large-prime-factor decomposition and its smooth-number remainder, and shows that the published one-block extension is only subpower at fixed polynomial windows. Classical Buchstab/Ramaré-style decompositions also make repeated prime-factor extraction a standard analytic-number-theory operation. No novelty is claimed for iteration itself, for `(18)`, or for the elementary fact that many threshold-sized prime factors may be needed to accumulate a polynomial factor.

A targeted literature check found no theorem turning this fixed-depth support-only architecture into fixed-power integer Möbius/Liouville variance at polynomial windows. Recent all-interval and higher-uniformity results provide strong qualitative or logarithmic cancellation, but those rate classes were already priced as `eta=0` by `MC-175`--`MC-178` and do not alter the exponent accounting here.

The Mathia-specific durable contribution is the **rate dictionary** `(9)`--`(13)`: it combines the classical polylogarithmic smooth-number density with the exact local-variance currency of `MC-177` and a square-free worst-case factor construction to show that the remaining “iterate the Chinis split” escape necessarily leaves the bounded-depth regime if its final error is still paid by support alone.

## Boundaries and failure modes

This finding does not prove that a growing-depth decomposition is analytically feasible. Repeated identities can introduce combinatorial coefficients, overlap, exceptional sets, loss of phase, or Dirichlet-polynomial ranges that overwhelm the nominal shortening gain.

The depth lower bound applies when one stage removes one individual prime factor and the uniform shortening guarantee is required for all relevant square-free integers. An identity that extracts a composite block containing many prime factors in one operation is outside the statement and is a legitimate escape route.

Likewise, `(9)` prices the standard cardinality estimate `(6)`. A theorem exploiting cancellation among the smooth Möbius coefficients is not constrained by that inequality and would directly evade the support-only half of the obstruction.

No inference about zeta zeros is made here. The result does not use `1/zeta(s)`, Perron inversion, contour shifting, or an RH assumption. Its role is only to narrow the source-side mechanism that could supply the local variance hypothesis already priced by `MC-177`.

## Consequence for the live frontier

The next factorization attack should not ask whether two or three additional large-prime extractions improve Chinis's polynomial-window block bound. They cannot close the fixed-power gap within the support-only terminal architecture.

The meaningful alternatives are now sharper: prove signed cancellation in the polynomially or polylogarithmically smooth Möbius sector; design a structured block extraction that removes many prime factors without paying growing-depth losses; or develop a genuinely multiscale decomposition whose full coefficient and overlap budget survives through roughly `log X/log log X` effective prime-extraction depth. Any candidate should be converted back to the `MC-177` currency by exhibiting an actual fixed `eta>0`, not merely a smaller smooth remainder or another subpower saving.