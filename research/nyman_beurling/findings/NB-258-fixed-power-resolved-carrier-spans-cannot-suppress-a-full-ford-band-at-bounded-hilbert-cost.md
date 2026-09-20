# NB-258 — Fixed-power resolved carrier spans cannot suppress a full Ford band at bounded Hilbert cost

> **Representation:** _Nyman–Beurling vantage._ The line-specific data are the positive Mellin shell scale `H`, Ford scale `R`, capacity `J=R/H`, exact Euler normalization `B_lambda(0)=1`, and the shell-Hilbert norm of the synthesized source. The generic engine is a derivative/Taylor compactness argument for short exponential sums. This is a source-only method boundary: it rules out bounded-cost suppression of an entire fixed Ford-scale carrier band for `H`-resolved scalar dictionaries whose channel count stays below `J^(1-delta)` for some fixed `delta>0`; it does not identify this unprojected band energy with the final Hardy/Nyman distance.

**Date:** 2026-09-21  
**Status:** `EXACT-DERIVED + H-SEPARATED-SIGNED-CARRIER + FORD-BAND-ENERGY + TAYLOR-RIGIDITY + FIXED-POWER-MESOSCOPIC-SPAN + NB-257-REFINEMENT + SOURCE-ONLY + METHOD-BOUNDARY + FRESH-PRIOR-ART-AUDIT`.

`NB-257` shows that one Ford-scale notch can be amortized across genuinely resolved signed/complex carrier channels. For a filled `H`-grid of `K` channels, the least shell-Hilbert cost of imposing one notch at distance `Theta(1/R)` is `Theta(J/K^(3/2))`; at `K~J^(2/3)` that cost is only order one. The open question is whether this bounded-cost superoscillation can suppress the **whole** Ford-scale carrier band required by the energy route of `NB-250`--`NB-251`, rather than merely hitting one point.

It cannot at any fixed-power mesoscopic channel scale. Suppose the synthesized source has uniformly bounded shell-Hilbert norm and the resolved carrier dictionary has

\[
K\le J^{1-\delta}
\qquad(\delta>0\text{ fixed}).
\]

After Ford rescaling,

\[
C_J(x):=B_\lambda(x/R),
\qquad C_J(0)=1,
\]

there is an integer `q=q(delta)` for which

\[
\|C_J^{(q)}\|_{L^\infty(\mathbb R)}=o(1).
\]

Consequently, on every fixed bounded Ford interval, `C_J` is uniformly `o(1)`-close to a polynomial of fixed degree at most `q-1` whose value at the origin is one. Finite-dimensional polynomial coercivity then gives, for every fixed interval `I` of positive length,

\[
\boxed{
\liminf_{J\to\infty}
\int_I |B_\lambda(x/R)|^2\,dx
>0.
}
\]

The same lower bound survives the exact smooth-shell envelope because `F(Hx/R)=F(x/J)\to F(0)\ne0` uniformly on bounded `x`. Thus a bounded-Hilbert-cost resolved scalar architecture cannot drive an entire fixed Ford band to zero while `K` remains below any fixed power `J^(1-delta)`.

At the `NB-257` crossover `K~J^(2/3)`, the statement becomes especially transparent: the second Ford derivative tends to zero, so every bounded-cost carrier is asymptotically affine on bounded Ford coordinates. `NB-257`'s optimal one-notch construction converges to exactly such a linear ramp. A linear ramp can hit one prescribed point, but it cannot have vanishing `L^2` energy on any interval.

The resulting necessary scale is stronger than the one-notch crossover. Any bounded-cost family that genuinely suppresses a fixed Ford band must leave every fixed-power regime:

\[
\boxed{
K=J^{1-o(1)}.
}
\]

For a filled resolved dictionary `W\asymp KH`, this means

\[
\frac WR=J^{-o(1)}.
\]

The span may still be `o(R)` very slowly, for example at logarithmic distance, so this does not prove that `W` must be a fixed fraction of `R`. It does show that no fixed exponent gap below the Ford scale can support full-band suppression at bounded source Hilbert cost.

## 1. Exact resolved-shell Hilbert geometry

Retain the Ford normalization used in `NB-230`--`NB-257`:

\[
Q:=\log(10+|t_0|),
\qquad
R:=Q^{2/3}(\log Q)^{1/3},
\qquad
Y:=\frac XR\asymp1,
\qquad
J:=\frac RH\to\infty.
\tag{1}
\]

Fix

\[
0<a<b<1,
\qquad
0\le\phi\in C_c^\infty((a,b)),
\qquad
\phi\not\equiv0,
\tag{2}
\]

and let

\[
k_\xi(u)
:=
\frac1H\phi\!\left(\frac{u-X-\xi}{H}\right).
\tag{3}
\]

Use the same resolved scalar dictionary as `NB-257`: for odd `K`,

\[
\xi_j=jH,
\qquad
-\frac{K-1}{2}\le j\le\frac{K-1}{2},
\tag{4}
\]

with Euler-normalized coefficient measure

\[
\lambda=\sum_j c_j\delta_{\xi_j},
\qquad
\sum_j c_j=1.
\tag{5}
\]

As before, convert to the physical shell coefficients by

\[
d\nu(\xi)=e^{r\xi/X}\,d\lambda(\xi),
\tag{6}
\]

so the Euler normalization is exact:

\[
\int e^{-r\xi/X}\,d\nu(\xi)=1.
\tag{7}
\]

The synthesized source is

\[
h_\nu(u)
=
\sum_j e^{r\xi_j/X}c_j k_{\xi_j}(u).
\tag{8}
\]

Because `diam(supp phi)<1` and adjacent centers differ by `H`, the translated shells are disjoint. Hence

\[
\boxed{
H\|h_\nu\|_2^2
=
\|\phi\|_2^2
\sum_j e^{2r\xi_j/X}|c_j|^2.
}
\tag{9}
\]

Assume throughout this finding that

\[
K\le J^{1-\delta}
\qquad(\delta>0\text{ fixed})
\tag{10}
\]

and that the source Hilbert cost is uniformly bounded:

\[
H^{1/2}\|h_\nu\|_2\le M
\tag{11}
\]

for a fixed `M` independent of `J`.

The carrier span is

\[
W=(K-1)H,
\qquad
\frac WR\asymp\frac KJ\le J^{-\delta},
\tag{12}
\]

so, since `X\asymp R`, one also has `W/X=o(1)`. The Euler tilt in (9) is therefore uniformly `1+o(1)`, and (9)--(11) imply

\[
\boxed{
\|c\|_{\ell^2}\le C_{\phi,r,M}
}
\tag{13}
\]

for all sufficiently large `J`.

This is the exact source-side coercivity that survived `NB-256` and was exploited in `NB-257`. No coefficient total variation estimate is needed below.

## 2. Fixed-power channel count forces a finite-degree Ford limit

The normalized carrier is

\[
B_\lambda(z)
:=
\sum_j c_j e^{i\xi_j z}.
\tag{14}
\]

Introduce the Ford coordinate

\[
\boxed{
C_J(x)
:=
B_\lambda(x/R)
=
\sum_j c_j e^{ijx/J}.
}
\tag{15}
\]

The exact Euler normalization gives

\[
C_J(0)=1.
\tag{16}
\]

For every integer `q>=1`, differentiation of (15) and Cauchy--Schwarz give

\[
\begin{aligned}
|C_J^{(q)}(x)|
&\le
\|c\|_2
\left(
\sum_j\left|\frac jJ\right|^{2q}
\right)^{1/2}\\
&\ll_q
\|c\|_2\frac{K^{q+1/2}}{J^q}.
\end{aligned}
\tag{17}
\]

Using (10) and (13),

\[
\boxed{
\|C_J^{(q)}\|_\infty
\ll_{q,\phi,r,M}
J^{(1-\delta)/2-\delta q}.
}
\tag{18}
\]

Choose once and for all an integer

\[
q=q_\delta
>
\frac{1-\delta}{2\delta}.
\tag{19}
\]

Then the exponent in (18) is strictly negative, and therefore

\[
\boxed{
\|C_J^{(q_\delta)}\|_\infty=o(1).
}
\tag{20}
\]

Let `I` be any fixed bounded interval. Taylor expansion at the origin gives

\[
C_J(x)=P_J(x)+E_J(x),
\tag{21}
\]

where

\[
P_J(x)
:=
\sum_{m=0}^{q_\delta-1}
\frac{C_J^{(m)}(0)}{m!}x^m,
\qquad
P_J(0)=1,
\tag{22}
\]

and, by (20),

\[
\boxed{
\sup_{x\in I}|E_J(x)|=o(1).
}
\tag{23}
\]

Thus bounded shell-Hilbert cost plus a fixed exponent gap in the resolved channel count forces the Ford-rescaled carrier to be asymptotically finite-dimensional. The coefficients of `P_J` need not remain bounded; that is irrelevant for the energy lower bound because evaluation at zero is a bounded functional on every fixed finite-dimensional polynomial space.

## 3. Finite-dimensional coercivity leaves a positive full-band floor

For the fixed interval `I` and degree bound `q_\delta-1`, define

\[
\kappa_{I,\delta}
:=
\inf\left\{
\int_I |P(x)|^2\,dx:
\deg P<q_\delta,
\ P(0)=1
\right\}.
\tag{24}
\]

Because the polynomial space is finite-dimensional and evaluation at zero is continuous, one has

\[
\boxed{
\kappa_{I,\delta}>0.
}
\tag{25}
\]

The interval need not contain zero. A nonzero polynomial of bounded degree cannot have arbitrarily small `L^2` norm on an interval of positive length while retaining the fixed value `P(0)=1`.

From (21)--(23),

\[
\|C_J\|_{L^2(I)}
\ge
\|P_J\|_{L^2(I)}
-
|I|^{1/2}\|E_J\|_{L^\infty(I)},
\tag{26}
\]

so (24)--(25) yield

\[
\boxed{
\liminf_{J\to\infty}
\int_I |C_J(x)|^2\,dx
\ge
\kappa_{I,\delta}>0.
}
\tag{27}
\]

This already rules out full-band suppression for the normalized carrier.

Now restore the actual smooth shell. Write

\[
F(z)
:=
\int_a^b\phi(u)e^{izu}\,du.
\tag{28}
\]

Since `phi>=0` and is not identically zero,

\[
F(0)=\int_a^b\phi(u)\,du>0.
\tag{29}
\]

On Ford coordinates `z=x/R`,

\[
F(Hz)=F(x/J)=F(0)+o(1)
\tag{30}
\]

uniformly for `x` in every fixed bounded interval. The common main carrier `e^{iXz}` has unit modulus on the real axis. Therefore (27) implies

\[
\boxed{
\liminf_{J\to\infty}
\int_I
\left|
F(x/J)B_\lambda(x/R)
\right|^2dx
\ge
|F(0)|^2\kappa_{I,\delta}>0.
}
\tag{31}
\]

Equation (31) is the source-side full Ford-band obstruction promised in the title. It is stronger than pricing finitely many isolated notches: an entire positive-length Ford interval retains order-one energy.

The same proof works with any fixed continuous nonnegative band weight that is bounded below on some interval of positive length. What matters is not the exact box in (27), but the impossibility of concentrating the normalized carrier into a Ford spike of vanishing width while the resolved channel count has a fixed exponent gap below `J` and the source Hilbert cost stays bounded.

## 4. `NB-257` is exactly the affine endpoint of this hierarchy

At the one-notch crossover of `NB-257`,

\[
K\asymp J^{2/3}.
\tag{32}
\]

Here one may take `delta=1/3` and `q_delta=2`. Equation (18) becomes

\[
\|C_J''\|_\infty
\ll
\frac{K^{5/2}}{J^2}
\asymp
J^{-1/3}
\to0.
\tag{33}
\]

So every bounded-cost family at this scale is uniformly asymptotic, on bounded Ford intervals, to an affine function. The minimum-norm construction of `NB-257` indeed satisfies

\[
C_J(x)
=
1-\frac{x}{\vartheta}+o(1).
\tag{34}
\]

It can create the prescribed notch at `x=vartheta`, but (27) says that this does not come close to erasing an interval. The `J^(2/3)` crossover is therefore the correct scale for **one** independent Ford constraint, not for full carrier-band suppression.

More generally, the familiar fixed-rank superoscillation hierarchy is visible directly in (18). If

\[
K\asymp J^{2m/(2m+1)}
\tag{35}
\]

for fixed `m>=1`, then the `(m+1)`-st Ford derivative tends to zero:

\[
\|C_J^{(m+1)}\|_\infty=o(1),
\tag{36}
\]

so the bounded-cost carrier is asymptotically a polynomial of degree at most `m` on fixed Ford intervals. This is consistent with the idea that progressively more resolved channels can amortize progressively higher interpolation rank. But for every **fixed** `m`, polynomial coercivity still leaves the positive band floor (27).

This explains what "many independent Ford constraints" has to mean after `NB-257`: the interpolation rank cannot remain fixed. A fixed number of point constraints may move the polynomial profile around, but it cannot make the whole band energy disappear.

## 5. Necessary asymptotic scale for genuine band suppression

Suppose, conversely, that a family of `H`-resolved scalar sources has uniformly bounded shell-Hilbert cost and satisfies, for some fixed interval `I` of positive length,

\[
\int_I
|B_\lambda(x/R)|^2dx
\longrightarrow0.
\tag{37}
\]

Then (27) rules out

\[
K\le J^{1-\delta}
\tag{38}
\]

for every fixed `delta>0`. Hence necessarily

\[
\boxed{
\frac{\log K}{\log J}\to1
}
\tag{39}
\]

along every such suppressing sequence, equivalently

\[
\boxed{
K=J^{1-o(1)}.
}
\tag{40}
\]

For the filled resolved dictionary `W\asymp KH`, this becomes

\[
\boxed{
\frac WR
\asymp
\frac KJ
=
J^{-o(1)}.
}
\tag{41}
\]

This is deliberately weaker than `W\asymp R`. For example `K=J/\log J` is compatible with (40) while still giving `W/R\to0`. The theorem closes every **fixed-power** mesoscopic gap, not logarithmic or slower gaps.

That distinction is important for the next pass. If the scalar signed route survives at all, it must now live in a near-Ford-rank regime such as `K=J/L(J)` with `L(J)=J^{o(1)}`, or it must exploit the later Hardy projection in a way that the source-side band energy does not see. The `J^(2/3)` architecture from `NB-257` is no longer a candidate for suppressing the whole band.

## 6. Adversarial review and representation boundary

The theorem depends on four assumptions that should not be silently weakened.

First, the carrier channels are genuinely resolved at scale `H`, so the shell synthesis is Hilbert-coercive as in `NB-257`. If sub-`H` opposite dipoles are allowed, `NB-256` shows that coefficient geometry can become representation-dependent.

Second, the channel dictionary is the filled `H`-grid of `NB-257` (or, with the same proof, a quasi-filled resolved dictionary whose total span is `O(KH)`). If `K` channels are allowed to occupy a much larger span than `KH`, the derivative bound (18) changes and the conclusion must be re-audited in terms of that larger span.

Third, the source Hilbert cost is uniformly bounded. If `H^(1/2)||h||_2` is allowed to grow, the right side of (18) acquires the same growth and the threshold changes.

Fourth, (31) is a **source-side carrier-band** lower bound. It does not prove a lower bound for the final Hardy-projected Nyman distance, does not control actual zeta zeros, and does not show that every sufficient route in `NB-250` must pay this floor. A later projection could in principle alter which part of this source-side energy reaches the destination. Any destination-level claim still has to be proved after the legal Hardy projection fixed by `NB-248`--`NB-250`.

The matched-zero packets used earlier in the line are not needed here. This finding is pure source/Hilbert geometry after the Nyman-specific normalization has fixed the relevant scales.

## 7. Prior-art audit

The generic phenomenon is superoscillation energy/conditioning. Ferreira and Kempf, *Superoscillations: Faster Than the Nyquist Rate*, IEEE Trans. Signal Process. 54 (2006), 3732--3740, DOI `10.1109/TSP.2006.877642`, studies minimum-energy band-limited interpolation and the rapid energy/dynamic-range cost of imposing increasingly fast local behavior. A fresh September 2026 search also finds active work on superoscillation dynamic-range laws and interpolation, including Haitang Yang, *Scaling law linking field and weight dynamic ranges in superoscillation*, Phys. Rev. A 114, 013505 (published 7 July 2026), and recent Lagrange-type superoscillation approximation work.

No novelty is claimed for Taylor's theorem, finite-dimensional polynomial norm equivalence, or the generic fact that superoscillatory interpolation becomes ill-conditioned. The line-local contribution is the exact Nyman/Ford scaling: disjoint positive-Mellin shells identify source `L^2` with resolved coefficient `ell^2`; `R=JH` turns the `q`-th derivative tariff into `K^(q+1/2)/J^q`; and this yields the fixed-power threshold (39)--(41) for suppressing a whole Ford band rather than one notch.

The fresh search did not identify a Nyman--Beurling result proving this fixed-power carrier-band obstruction, nor is any external theorem load-bearing in the proof above. `SOURCES.md` therefore needs no new durable dependency.

## 8. Resulting frontier

`NB-257` leaves open whether many Ford constraints restore a divergent Hilbert tariff. `NB-258` resolves the first substantial version of that question: **a whole fixed Ford interval cannot be suppressed at bounded source Hilbert cost by any filled `H`-resolved scalar dictionary with `K<=J^(1-delta)` for fixed `delta>0`.**

The interpolation-rank hierarchy is now explicit. The `J^(2/3)` scale buys an affine Ford profile and one bounded-cost notch; higher fixed powers buy higher but still finite polynomial degree; genuine full-band decay forces the rank into the near-full regime `K=J^(1-o(1))`.

The next non-circular target is therefore narrow: analyze the critical near-full-rank window, for example `K=J/L(J)` with slowly growing `L`, or move the argument through the exact Hardy projection and test whether the destination energy already enforces a stronger lower bound before that regime is reached. Another fixed-rank notch calculation would no longer address the live obstruction.