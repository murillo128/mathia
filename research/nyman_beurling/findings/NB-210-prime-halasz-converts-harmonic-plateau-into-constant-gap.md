# NB-210 — Prime Halász converts the harmonic plateau into a constant positive-return gap below every `exp(X^(3/2-delta))` height

**Date:** 2026-09-18  
**Status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION + SOURCE-ACQUISITION + POSITIVE-EULER + PRIME-HALASZ + CORRELATED-HARMONICS + NB-208-REFINEMENT`.

`NB-208` shows that one accurate positive Euler return forces not one but a whole harmonic plateau of almost-maximal prime phase sums. `NB-209` then observes that generic large-value estimates still pay the ambient-support tariff and miss a plateau of length `asymp X=log x` by one logarithmic dimension. There is, however, a classical prime-specific inequality that removes exactly that support loss: Matomäki--Radziwiłł's Halász inequality for prime-supported Dirichlet polynomials.

Combining that inequality with the `NB-208` amplification yields a stronger pointwise conclusion than the earlier barycenter argument. Let

\[
x_a=e^{r_0/a},\qquad X_a=\log x_a=\frac{r_0}{a},\qquad y_a=e^\Delta x_a,
\]

and keep the normalized positive Euler-shell defect

\[
\mathcal A_a(t)
=
\sum_{x_a\le n<y_a}
 w_{n,a}|e^{-it\log n}-1|,
\qquad
w_{n,a}
=
\frac{\Lambda(n)n^{-1-a}}
{\sum_{x_a\le m<y_a}\Lambda(m)m^{-1-a}}.
\tag{1}
\]

Then for every fixed

\[
0<\delta<\frac32
\tag{2}
\]

there is a constant `eta_delta>0` such that, for all sufficiently small `a`,

\[
\boxed{
1\le |t|\le
\exp\!\left(X_a^{3/2-\delta}\right)
\quad\Longrightarrow\quad
\mathcal A_a(t)\ge \eta_\delta.
}
\tag{3}
\]

Thus the correlated-prime route does more than recover the missing factor noted in `NB-209`: throughout every fixed subcritical `3/2-delta` logarithmic-height regime it upgrades the positive-return obstruction from an `Omega(1/X_a)` gap to an **order-one gap**.

This does **not** improve the outer first-return frontier of `NB-205`. Ford's explicit integer exponential-sum estimate already excludes `o(1/X_a)` returns up to the larger height

\[
\exp\!\left\{
\kappa\frac{X_a^{3/2}}{\sqrt{\log X_a}}
\right\},
\qquad
\kappa<1/\sqrt{133.66}.
\tag{4}
\]

The new information is instead that the logarithmic sparse-support loss identified by `NB-209` is **not intrinsic**: known prime-specific Halász technology removes it. What prevents this route from reaching the exact Ford edge is the height-dependent off-diagonal term in that inequality, not the density `1/X_a` of the prime support.

## 1. Positive Euler alignment forces fixed harmonic prime alignment

Choose once and for all

\[
1<\kappa_0<\min\{2,e^\Delta\}
\tag{5}
\]

and put

\[
\mathcal P_a
=
\{p:\ x_a\le p<\kappa_0x_a\},
\qquad
M_a=|\mathcal P_a|.
\tag{6}
\]

By the prime number theorem,

\[
M_a\asymp_{\kappa_0}\frac{x_a}{X_a}.
\tag{7}
\]

On this fixed prime sub-shell, `log p=X_a+O(1)` and `p^{-a}=e^{-r_0+O(a)}`. The denominator in (1) is bounded above and below by positive constants depending only on `r_0,Delta`, so uniformly for `p in P_a`,

\[
w_{p,a}\asymp_{r_0,\Delta,\kappa_0}
\frac{X_a}{x_a}.
\tag{8}
\]

Consequently

\[
\frac1{M_a}
\sum_{p\in\mathcal P_a}
|1-e^{-it\log p}|
\ll
\mathcal A_a(t).
\tag{9}
\]

For every integer `h>=1`,

\[
|1-z^h|\le h|1-z|
\qquad(|z|=1),
\tag{10}
\]

and hence, for

\[
D_a(u):=\sum_{p\in\mathcal P_a}p^{-iu},
\qquad
U_a(u):=\frac{D_a(u)}{M_a},
\tag{11}
\]

we obtain the quantitative harmonic transfer

\[
\boxed{
1-\Re U_a(ht)
\le C h\,\mathcal A_a(t)
}
\tag{12}
\]

with `C` depending only on the fixed shell parameters.

In particular, once an integer `H_0` is fixed, there is a fixed `eta(H_0)>0` such that

\[
\mathcal A_a(t)\le \eta(H_0)
\quad\Longrightarrow\quad
|D_a(ht)|\ge \frac34 M_a
\qquad(1\le h\le H_0).
\tag{13}
\]

No asymptotic accuracy is needed here. A sufficiently small **constant** positive Euler return already creates a fixed-length plateau of almost-maximal prime sums.

## 2. The prime Halász inequality removes the sparse-support loss

Matomäki and Radziwiłł prove the following prime-supported Halász inequality (their Lemma 11). For

\[
P(s)=\sum_{P\le p\le2P} a_p p^{-s}
\tag{14}
\]

and any well-spaced set `Tcal subset [-T,T]`,

\[
\sum_{u\in\mathcal T}|P(iu)|^2
\ll_\epsilon
\left(
P+|\mathcal T|P
\exp\!\left[-\frac{\log P}{(\log T)^{2/3+\epsilon}}\right]
(\log T)^2
\right)
\sum_{P\le p\le2P}
\frac{|a_p|^2}{\log P}.
\tag{15}
\]

The factor `1/log P` in the coefficient square sum is exactly the prime-density gain missing from the generic estimates audited in `NB-209`.

Apply (15) with `P=x_a`, with `a_p=1` on `P_a` and zero on the remainder of `[x_a,2x_a]`, and with

\[
\mathcal T_{H,t}=\{t,2t,\ldots,Ht\}.
\tag{16}
\]

For `|t|>=1` this set is well-spaced and lies in `[-T_{H,t},T_{H,t}]` with

\[
T_{H,t}=H|t|.
\tag{17}
\]

Since

\[
\sum_{x_a\le p\le2x_a}
\frac{|a_p|^2}{\log x_a}
=
\frac{M_a}{X_a},
\tag{18}
\]

(15), (7), and (11) give

\[
\boxed{
\sum_{h=1}^{H}|U_a(ht)|^2
\ll_{\epsilon,\kappa_0}
1+H E_{a,\epsilon}(H,t),
}
\tag{19}
\]

where

\[
E_{a,\epsilon}(H,t)
:=
\exp\!\left[
-\frac{X_a}{(\log(H|t|))^{2/3+\epsilon}}
\right]
(\log(H|t|))^2.
\tag{20}
\]

This is the decisive cancellation of the `NB-209` tariff. A generic integer-support estimate would leave a baseline of order `X_a^2` after normalization; the prime Halász inequality leaves an order-one baseline.

## 3. A fixed number of harmonics already rules out a small constant return

Fix `epsilon>0`. Let `K_epsilon` be a constant large enough that (19) implies

\[
\sum_{h=1}^{H}|U_a(ht)|^2
\le
K_\epsilon\left(1+H E_{a,\epsilon}(H,t)\right)
\tag{21}
\]

for all sufficiently small `a`. Choose once and for all an integer

\[
H_0>4K_\epsilon.
\tag{22}
\]

If `A_a(t)<=eta(H_0)`, then (13) gives

\[
\sum_{h=1}^{H_0}|U_a(ht)|^2
\ge
\frac9{16}H_0.
\tag{23}
\]

On the other hand, if

\[
E_{a,\epsilon}(H_0,t)
\le \frac1{8K_\epsilon},
\tag{24}
\]

then (21) gives an upper bound incompatible with (22)--(23) after enlarging `H_0` by a fixed factor if necessary. Therefore there is a fixed `eta_epsilon>0` such that

\[
\boxed{
E_{a,\epsilon}(H_0,t)\longrightarrow0
\quad\Longrightarrow\quad
\mathcal A_a(t)\ge\eta_\epsilon
}
\tag{25}
\]

uniformly over the corresponding ordinates.

The constants in (22) and hence in `eta_epsilon` are ineffective for our purposes only in the ordinary sense that we do not track the implied constant in (15). Their positivity and independence of `a,t` are all that is needed.

## 4. The height range is every fixed exponent below `3/2`

Fix `delta` as in (2). Choose a fixed `epsilon>0` sufficiently small that

\[
\left(\frac23+\epsilon\right)
\left(\frac32-\delta\right)<1.
\tag{26}
\]

For

\[
1\le |t|\le\exp(X_a^{3/2-\delta}),
\tag{27}
\]

and fixed `H_0`, write

\[
Q=\log(H_0|t|)
\le X_a^{3/2-\delta}+O(1).
\tag{28}
\]

If `beta=2/3+epsilon`, then (26) gives a constant `gamma>0` with

\[
\frac{X_a}{Q^\beta}
\ge X_a^{\gamma+o(1)}.
\tag{29}
\]

Consequently

\[
\log E_{a,\epsilon}(H_0,t)
\le
2\log Q-X_a^{\gamma+o(1)}
\longrightarrow-\infty
\tag{30}
\]

uniformly in (27). Equation (25) now proves (3).

The same argument can be stated without the power simplification: for each fixed `epsilon>0`, a constant positive gap holds whenever

\[
(\log|t|)^2
\exp\!\left[-c
\frac{X_a}{(\log|t|)^{2/3+\epsilon}}
\right]
=o(1),
\tag{31}
\]

with harmless changes for bounded `|t|` and fixed harmonic dilation. The `3/2-delta` form is simply the clean uniform corollary that avoids pretending the fixed-`epsilon` theorem is uniform as `epsilon->0`.

## 5. What this changes relative to `NB-194`, `NB-205`, and `NB-209`

`NB-194` obtains an order-one positive-return gap from a single Euler barycenter, but only while

\[
\log|t|
\ll
\frac{X_a^{3/5}}{(\log X_a)^{1/5}}.
\tag{32}
\]

The harmonic plateau plus prime Halász inequality pushes an order-one gap all the way to every fixed

\[
\log|t|\le X_a^{3/2-\delta}.
\tag{33}
\]

The gain comes from using **correlated repeated near-maximality**, not from a stronger pointwise prime-number theorem.

`NB-205` still has the farther outer boundary for the much weaker target accuracy `o(1/X_a)`: its Ford corridor reaches

\[
\log|t|
\asymp
\frac{X_a^{3/2}}{\sqrt{\log X_a}}.
\tag{34}
\]

For every fixed `delta>0`, (34) eventually exceeds `X_a^(3/2-delta)`. Thus (3) is a strength-of-gap improvement, not a new first-possible-return height.

Finally, `NB-209` left two plausible diagnoses for the missing logarithmic dimension: perhaps one needed a prime-density-aware large-value theorem, or perhaps much more of the phase-pinned harmonic structure had to be used. The first ingredient already exists in prior art. Matomäki--Radziwiłł's factor `1/log P` removes the sparse-support baseline completely in the regime where its off-diagonal term is small. The surviving bottleneck is therefore more specific:

\[
\boxed{
\text{extend prime-sensitive correlated control to the moving Ford/VK edge,}
}
\tag{35}
\]

rather than merely replace ambient length by prime support size in a generic large-value estimate.

## 6. Stress tests and boundaries

### Fixed `epsilon` is load-bearing

Lemma 11 is stated for fixed `epsilon>0`, with an implied constant depending on it. Nothing above lets `epsilon=epsilon_a->0`. Therefore (3) is deliberately stated for each fixed `delta>0`; it does not yield a diagonal corridor

\[
\log|t|
\asymp
X_a^{3/2}/\sqrt{\log X_a}.
\tag{36}
\]

Treating the theorem as uniform in `epsilon` would erase exactly the remaining boundary.

### Positivity is load-bearing

The transfer (9)--(12) starts from the positive `ell^1` Euler defect. Signed or complex source combinations may cancel before any individual prime-phase average becomes nearly maximal. The result therefore does not address the signed/complex escape route.

### This remains source acquisition, not Nyman distance

Equation (3) is a theorem about the positive Euler shell. It does not prove that a near-optimal Nyman--Beurling approximant must realize such a positive return. The destination bridge remains separate and necessary.

### Prime support is genuinely used

The improvement over `NB-209` is not a generic sparse-set argument. The factor `1/log P` in (15) comes from the prime-supported Halász inequality. Replacing the primes by an arbitrary set of the same cardinality does not preserve the estimate.

### Near-maximal phase pinning is stronger than what the theorem consumes

The source transfer actually gives `Re U_a(ht)` close to `1`; Lemma 11 uses only the weaker consequence that `|U_a(ht)|` is large. Thus (3) is robust under weakening the plateau to large modulus, but this also indicates where further improvement might live: the unused common phase pinning and arithmetic-progression structure of the ordinates are extra information not exploited by the prime Halász bound.

## 7. Prior art and novelty audit

The load-bearing external theorem is Kaisa Matomäki and Maksym Radziwiłł, *Multiplicative functions in short intervals*, Annals of Mathematics 183 (2016), 1015--1056, DOI `10.4007/annals.2016.183.3.6`, Lemma 11. The authors explicitly introduce it as a prime-supported Halász inequality that recovers the logarithmic loss suffered by the corresponding integer-support estimate. Their proof uses duality and a zero-free-region estimate for the prime-power correlation kernel.

No novelty is claimed for that inequality or for the prime number theorem estimates used in (7)--(8). The line-local derived contribution is the bridge

\[
\text{one positive Euler return}
\Longrightarrow
\text{harmonic prime plateau (`NB-208`)}
\Longrightarrow
\text{prime-Halász contradiction},
\tag{37}
\]

which yields the constant-gap corridor (3) and resolves the specific sparse-support tariff diagnosed in `NB-209`.

A search of current large-value literature, including the 2026 Guth--Maynard estimates already audited in `NB-209`, did not reveal a published prime-supported theorem that both retains the `1/log P` Halász gain and is uniform enough at the exact moving Ford scale (36). That absence is not a theorem of impossibility; it is the remaining literature boundary for this route.

## 8. Consequence for the research line

The next source-side question is narrower than the one left by `NB-209`. There is no need to rediscover a generic prime-density correction: classical prime Halász already supplies it and even upgrades the return gap to order one below every fixed `3/2-delta` exponent.

To move the actual `o(1/X_a)` first-return frontier beyond `NB-205`, one needs at least one genuinely new ingredient: quantitative uniformity in the prime-Halász off-diagonal term near the moving `3/2` edge, a stronger prime-correlation estimate at those heights, or an argument exploiting the **common phase pinning and arithmetic-progression structure** that (15) discards. Independently, the destination theorem connecting Nyman approximation to this positive source condition remains unresolved.