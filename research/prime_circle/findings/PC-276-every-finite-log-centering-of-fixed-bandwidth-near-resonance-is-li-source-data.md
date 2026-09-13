# PC-276 — every finite logarithmic centering of fixed-bandwidth near-resonance is Li-source data

**Status:** `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the finite-order logarithmic-centering escape left open by PC-275.

PC-275 identifies the first centered fixed-bandwidth prime/grid near-resonance correction: after multiplication by `log q`, the limit is the pushforward of the first logarithmic-integral source bias `-(1+log t)dt`. A natural continuation is to subtract that deterministic term, multiply by another power of `log q`, and ask whether a zeta-zero or genuinely geometric statistic appears at the next order.

For every **fixed finite order**, it does not. The entire Poincaré hierarchy in powers of `1/log q` is forced by the classical normalized logarithmic-integral source before the Prime-Circle observable is applied. The zero-sensitive prime-number-theorem remainder lies beyond every fixed power of `1/log q`; a fixed-bandwidth Lipschitz Prime-Circle pushforward does not promote it into this hierarchy.

Write

\[
D_B(x,y)
:=
\min_{0<\max(|h|,|k|)\le B}
\|hx+ky\|_{\mathbb R/\mathbb Z},
\tag{1}
\]

and let `rho^prime_{q,B}` and `rho^grid_{q,B}` be the same distinct-pair laws as in PC-273--PC-275. Put `L=log q`. Define polynomials `P_m` recursively by

\[
P_0(u)=1,
\qquad
P_m(u)=(-u)^m-\sum_{j=1}^m j!\,P_{m-j}(u)
\quad(m\ge1),
\tag{2}
\]

and signed measures

\[
\sigma_m(dt):=P_m(\log t)\,dt.
\tag{3}
\]

The first terms are

\[
P_1(u)=-(1+u),
\qquad
P_2(u)=u^2+u-1,
\qquad
P_3(u)=-u^3-u^2+u-3.
\tag{4}
\]

For every fixed integer `K>=0` and every fixed Lipschitz test `g:[0,1]\to\mathbb R`, the normalized prime source satisfies

\[
\boxed{
\int g\,d\nu_q
=
\sum_{m=0}^{K}\frac1{L^m}
\int_0^1 g(t)P_m(\log t)\,dt
+O_{g,K}(L^{-K-1})
+O_g\!\left(L e^{-c\sqrt L}\right)
+O_g(L/q).
}
\tag{5}
\]

Here `c>0` is any admissible classical de la Vallee-Poussin constant after harmless weakening. In particular, for every `m>=1`,

\[
\int_0^1P_m(\log t)\,dt=0,
\tag{6}
\]

so each `sigma_m` is a signed mass-zero correction to Lebesgue measure.

Consequently, for every fixed `B`, fixed `K`, and fixed Lipschitz `phi`,

\[
\boxed{
\begin{aligned}
&\int\phi\,d\rho^{\mathrm{prime}}_{q,B}
-
\int\phi\,d\rho^{\mathrm{grid}}_{q,B}\\
&\qquad=
\sum_{r=1}^{K}\frac1{L^r}
\int_{[0,1]^2}
\phi(D_B(x,y))
\sum_{a+b=r}
P_a(\log x)P_b(\log y)\,dx\,dy
+O_{B,\phi,K}(L^{-K-1})
+O_{B,\phi}\!\left(L e^{-c\sqrt L}\right)
+O_{B,\phi}(L/q).
\end{aligned}
}
\tag{7}
\]

Equivalently, defining

\[
\kappa_{B,r}
:=
(D_B)_*\left(\sum_{a+b=r}\sigma_a\otimes\sigma_b\right),
\tag{8}
\]

we have the finite-order asymptotic expansion

\[
\rho^{\mathrm{prime}}_{q,B}-\rho^{\mathrm{grid}}_{q,B}
\sim
\sum_{r\ge1}\frac{\kappa_{B,r}}{(\log q)^r}
\tag{9}
\]

in the precise Poincaré sense that (7) holds to every **fixed** truncation order against fixed Lipschitz tests. No convergence of the infinite series is asserted.

Thus subtracting any finite number of deterministic logarithmic corrections and rescaling by the next power of `log q` can only expose another coefficient of the same classical `Li` source hierarchy. If a particular coefficient vanishes for a chosen test, the next finite coefficient is still of the same origin. This closes the route

\[
\text{fixed }B
\;\longrightarrow\;
\text{prime/grid centering}
\;\longrightarrow\;
(\log q)^K\text{ rescaling at finite }K
\;\longrightarrow\;
\text{new RH statistic}.
\tag{10}
\]

## 1. Exact normalized Li source and the beyond-all-log remainder

The cleanest separation is to introduce the exact normalized logarithmic-integral source

\[
d\lambda_q(t)
:=
\frac{q}{\operatorname{Li}(q)-\operatorname{Li}(2)}
\frac{\mathbf 1_{[2/q,1]}(t)}{L+\log t}\,dt.
\tag{11}
\]

It is a probability measure. The quantitative prime number theorem

\[
\pi(x)=\operatorname{Li}(x)+O\!\left(xe^{-c\sqrt{\log x}}\right)
\tag{12}
\]

combined with Stieltjes partial summation gives, for every fixed Lipschitz `g`,

\[
\boxed{
\int g\,d\nu_q-
\int g\,d\lambda_q
=
O_g\!\left(L e^{-c'\sqrt L}\right)+O_g(L/q)
}
\tag{13}
\]

for some `c'>0`. The first term is smaller than `L^{-A}` for every fixed `A>0`. Thus the ordinary PNT remainder is **beyond all finite logarithmic orders** in this scaling.

This statement is not an RH result. Equation (13) uses only a classical zero-free-region PNT estimate. The finer oscillatory content of the exact `nu_q-lambda_q` residual is where the classical explicit formula and zeta zeros may enter. The point here is that this residual is not the source of any coefficient at a fixed algebraic order in `1/log q`.

## 2. Derivation of the all-orders source coefficients

For a fixed truncation order `K`, split the integral in (11) at `t=q^{-1/2}`. The lower interval has normalized mass `O(q^{-1/2})`, hence is negligible compared with every fixed power of `1/L`. On the bulk interval, `|log t|<=L/2`, so the geometric expansion is uniform:

\[
\frac1{L+\log t}
=
\frac1L\sum_{a=0}^{K+1}
\left(-\frac{\log t}{L}\right)^a
+O_K\!\left(\frac{|\log t|^{K+2}}{L^{K+3}}\right).
\tag{14}
\]

Since

\[
\int_0^1|\log t|^m\,dt=m!,
\tag{15}
\]

the integrated remainder is controlled at every fixed order. Repeated integration by parts in `Li(q)` gives its standard Poincaré expansion

\[
\frac{\operatorname{Li}(q)}q
=
\frac1L
\left(
1+\frac{1!}{L}+\frac{2!}{L^2}+\cdots+
\frac{K!}{L^K}+O_K(L^{-K-1})
\right).
\tag{16}
\]

Let the formal reciprocal of `sum_{j>=0} j! z^j` be `sum_{m>=0} b_m z^m`. Dividing the numerator expansion by (16) gives

\[
P_m(u)=\sum_{a=0}^{m}(-u)^a b_{m-a},
\tag{17}
\]

which is equivalent to recurrence (2). The identity

\[
\int_0^1(\log t)^a\,dt=(-1)^a a!
\tag{18}
\]

then makes (6) immediate: the total-mass coefficients are exactly the nonconstant coefficients of a formal series multiplied by its reciprocal.

For `m=1`, equation (3) gives

\[
\sigma_1(dt)=-(1+\log t)dt,
\tag{19}
\]

so PC-275 is precisely the first member of this hierarchy rather than a special isolated correction.

## 3. Pair pushforward and fixed-bandwidth closure

For fixed `B` and fixed Lipschitz `phi`, set

\[
G_B(x,y)=\phi(D_B(x,y)).
\tag{20}
\]

PC-273 establishes the required fixed Lipschitz control for `D_B`. Applying (5) successively in the two variables gives

\[
\int G_B\,d(\nu_q\otimes\nu_q)
=
\sum_{r=0}^{K}\frac1{L^r}
\int_{[0,1]^2}G_B(x,y)
\sum_{a+b=r}P_a(\log x)P_b(\log y)\,dx\,dy
+O_{B,\phi,K}(L^{-K-1})
+O_{B,\phi}\!\left(L e^{-c\sqrt L}\right).
\tag{21}
\]

The all-residue grid product differs from Lebesgue product by `O_{B,phi}(1/q)`. Passing from ordered product pairs to distinct unordered pairs costs `O(1/M_q)=O(L/q)` on the prime side and `O(1/q)` on the grid side. These errors are beyond every fixed logarithmic order, giving (7).

In particular, for every fixed `K>=1`,

\[
L^K\left[
\rho^{\mathrm{prime}}_{q,B}-\rho^{\mathrm{grid}}_{q,B}
-
\sum_{r=1}^{K-1}L^{-r}\kappa_{B,r}
\right]
\Longrightarrow
\kappa_{B,K}
\tag{22}
\]

against fixed Lipschitz tests. The limiting object is always a deterministic pushforward of logarithmic-polynomial source densities.

There is a stronger exact-source formulation. Let `rho^Li_{q,B}` be the pair law obtained by replacing each prime source coordinate by `lambda_q` before applying `D_B`. Then (13) and the fixed Lipschitz norm of `G_B` imply

\[
\boxed{
\left|
\int\phi\,d\rho^{\mathrm{prime}}_{q,B}
-
\int\phi\,d\rho^{\mathrm{Li}}_{q,B}
\right|
\ll_{B,\phi}
L e^{-c'\sqrt L}+L/q.
}
\tag{23}
\]

So the whole finite `1/log q` hierarchy is already present in the non-arithmetic normalized `Li` control.

## 4. Prior-art and novelty audit

The number-theoretic input is classical. H. L. Montgomery and R. C. Vaughan, *Multiplicative Number Theory I: Classical Theory*, Cambridge University Press (2006), Chapter 6, gives the quantitative prime number theorem and logarithmic-integral approximation used already in PC-273/PC-275. The factorial asymptotic expansion (16) follows by the standard repeated integration-by-parts expansion of the logarithmic integral. Stieltjes partial summation then yields the fixed-test estimate (13).

A targeted novelty check for weighted prime empirical measures, smooth weighted prime sums, higher logarithmic-integral corrections, and Poincaré expansions of `Li` found no separate nonclassical mechanism needed here. The coefficients in (2)--(5) are formal consequences of normalizing the classical density `dt/log(qt)`. The project-local content is the exact conclusion for the Prime-Circle near-resonance carrier: **every finite logarithmic centering of the fixed-bandwidth law is exhausted by those source coefficients before the geometry acts.**

Accordingly this is not claimed as new analytic number theory. It is a decisive boundary result inside the Prime-Circle search. It prevents higher finite powers of `log q` from being counted as progress merely because PC-275's first coefficient has been removed.

No new external source dependency beyond the PNT/`Li` input already used in PC-273/PC-275 is required, so `SOURCES.md` is unchanged.

## 5. What this does and does not rule out

This result rules out **fixed bandwidth plus any finite algebraic logarithmic recentering** as an independent route to RH. It also shows that exact Li-centering is the correct baseline if the goal is to expose genuinely finer source fluctuations.

It does **not** say that the exact Li-centered residual contains no zeta-zero information. Classical explicit formulas do put zero-sensitive oscillations in the PNT remainder. If a future construction merely detects those oscillations after a fixed Lipschitz pushforward, that is inherited explicit-formula data rather than a new Prime-Circle mechanism. A substantive continuation would have to show that the geometry adds something not already equivalent to that classical source remainder.

The main surviving directions are therefore moving bandwidth `B=B(q)` where fixed-test uniformity fails; shrinking/singular or directional observables such as the minimizing `(h,k)` rather than only `D_B`; conditioned prime families; and genuinely nonlocal or cross-level couplings forced by the roots-of-unity geometry. Those lie outside equations (5)--(23).

## 6. Falsification and audit tests

The result has direct checks. First, recurrence (2) must reproduce PC-275 at order one and must give `P_2(u)=u^2+u-1`; any disagreement falsifies the normalization algebra. Second, every `P_m(log t)` for `m>=1` must integrate to zero on `[0,1]`; failure exposes an incorrect reciprocal-series coefficient. Third, for any fixed `K` and fixed Lipschitz `g`, subtracting the first `K` terms in (5) must leave `o(L^{-K})`; a residual of order `L^{-j}` with `j<=K` not accounted for by `P_j` would falsify the source expansion.

On the pair side, fixed `B` and fixed Lipschitz `phi` must obey (7). Growing `B`, discontinuous minimizer labels, shrinking targets, exact Li-centering followed by a non-logarithmic rescaling, or nonlocal/cross-level observables are deliberately outside the theorem and are valid continuations rather than counterexamples.

## 7. Research-line consequence

PC-273 closes the raw fixed/sublog law, PC-274 closes the raw law uniformly over bandwidth, and PC-275 identifies the first centered fixed-bandwidth coefficient. PC-276 now closes the **entire finite logarithmic hierarchy at fixed bandwidth**. The hierarchy is not a sequence of increasingly hidden prime-circle spectral effects; it is the ordinary normalized logarithmic-integral source expansion transported through `D_B`.

The live boundary is therefore sharper: either remove the exact normalized Li source and accept that the remaining one-source channel is classical explicit-formula territory, or change the observation regime so that the roots-of-unity geometry contributes a genuinely new coupling, scale, singular observable, or nonlocal structure.