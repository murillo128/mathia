# AF-354 — fast-vanishing Riesz order inherits endpoint oscillation

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `QUANTITATIVE-FIDELITY`, `ZERO-SENSITIVE-SOURCE`, `MOVING-PARAMETER-OBSTRUCTION`, `TARGET-METRIC-CALIBRATION`, `NO-NOVELTY-CLAIM`

## Claim

Let

\[
c_n:=\Lambda(n)-1,
\qquad
\mathcal R_\delta[c](X)
:=
\sum_{n\le X}c_n\left(1-\frac nX\right)^\delta,
\qquad \delta\ge0,
\tag{1}
\]

and evaluate the endpoint comparison on the fixed half-integer mesh

\[
X_N:=N+\frac12.
\tag{2}
\]

There is an absolute constant `C` such that, uniformly for `N>=2` and `0<delta<=1`,

\[
\boxed{
\left|
\mathcal R_\delta[\Lambda-1](X_N)
-
\mathcal R_0[\Lambda-1](X_N)
\right|
\le C\delta X_N.
}
\tag{3}
\]

Since

\[
\mathcal R_0[\Lambda-1](X_N)=\psi(N)-N,
\tag{4}
\]

Hardy--Littlewood's classical oscillation theorem immediately gives a moving-order obstruction. Write

\[
L(N):=\log\log\log N
\tag{5}
\]

for sufficiently large `N`. If `delta_N in (0,1]` satisfies

\[
\frac{\delta_N\sqrt N}{L(N)}\longrightarrow0,
\tag{6}
\]

then

\[
\boxed{
\mathcal R_{\delta_N}[\Lambda-1](X_N)
=
\Omega_\pm\!\left(\sqrt N\,L(N)\right).
}
\tag{7}
\]

In particular,

\[
\mathcal R_{\delta_N}[\Lambda-1](X_N)\ne O(\sqrt N).
\tag{8}
\]

Thus the fixed-order statement in AF-352 does **not** extend uniformly to arbitrarily fast vanishing positive orders. Every fixed `delta>0` lies on the well-conditioned side under RH, but a scale-dependent order tending to zero too quickly remains asymptotically indistinguishable from the unsmoothed endpoint at exactly the scale where the endpoint violates the critical `sqrt(X)` norm.

For the power schedule

\[
\delta_N=N^{-a},
\tag{9}
\]

condition `(6)` holds for every

\[
\boxed{a\ge\frac12.}
\tag{10}
\]

Hence no power-law smoothing order `N^{-a}` with `a>=1/2` can produce a critical-scale `O(sqrt(N))` profile. The range `0<a<1/2` is not decided by this argument.

There is also a quantitative consequence for AF-353's fixed-order conditioning profile

\[
K(\delta)
:=
\sup_{X\ge2,\ X\notin\mathbb N}
X^{-1/2}\left|\mathcal R_\delta[\Lambda-1](X)\right|.
\tag{11}
\]

Under RH, `K(delta)<infinity` for every fixed `delta>0` by AF-352. Moreover there is a sequence `delta_j->0+` such that

\[
K(\delta_j)
\gg
\log\log\log\frac1{\delta_j}.
\tag{12}
\]

Equivalently,

\[
\boxed{
\limsup_{\delta\downarrow0}
\frac{K(\delta)}{\log\log\log(1/\delta)}>0.
}
\tag{13}
\]

This is only a subsequential lower rate. It does not identify the true growth of `K(delta)` and remains far below AF-353's `delta^{-2}` absolute-zero triangle budget.

## Derivation

### 1. Small Riesz order differs from the endpoint by a logarithmic boundary weight

For `0<u<1` and `delta>0`, put

\[
w(u):=-\log(1-u)\ge0.
\tag{14}
\]

Then

\[
1-(1-u)^\delta
=1-e^{-\delta w(u)}
\le \delta w(u).
\tag{15}
\]

At `X=X_N=N+1/2`, every sampled point stays a fixed distance `1/2` from the kernel endpoint. Therefore

\[
\begin{aligned}
\left|
\mathcal R_\delta[c](X_N)-\mathcal R_0[c](X_N)
\right|
&\le
\sum_{n\le N}|c_n|
\left[1-\left(1-\frac n{X_N}\right)^\delta\right]\\
&\le
\delta
\sum_{n\le N}|c_n|
\log\frac{X_N}{X_N-n}.
\end{aligned}
\tag{16}
\]

Since `|Lambda(n)-1|<=Lambda(n)+1`, it is enough to prove

\[
\sum_{n\le N}(\Lambda(n)+1)
\log\frac{X_N}{X_N-n}
\ll X_N.
\tag{17}
\]

The point of `(17)` is that the apparent logarithmic singularity of the derivative in `delta` costs only linear total source mass after the arithmetic support is counted at the correct boundary scale.

### 2. The dense unit source pays only linear logarithmic boundary mass

Let

\[
d_n:=X_N-n\in\left\{\frac12,\frac32,\ldots,N-\frac12\right\}.
\tag{18}
\]

Group the `d_n` dyadically. A shell with `H<=d_n<2H` contains `O(H)` integers, while its weight is at most

\[
\log\frac{X_N}{H}.
\tag{19}
\]

Hence

\[
\sum_{n\le N}
\log\frac{X_N}{X_N-n}
\ll
\sum_{H\ \mathrm{dyadic},\ H\le X_N}
H\log\frac{2X_N}{H}
\ll X_N.
\tag{20}
\]

The last sum is a reversed geometric series: shells close to the endpoint have larger logarithmic weight but exponentially fewer sites.

### 3. The von Mangoldt source also pays only linear boundary mass

Consider

\[
S_\Lambda(X_N)
:=
\sum_{n\le N}\Lambda(n)
\log\frac{X_N}{X_N-n}.
\tag{21}
\]

Split the support into primes and proper prime powers.

For proper prime powers `p^k`, `k>=2`, there are `O(sqrt(X_N))` such integers up to `X_N`. Since

\[
\Lambda(p^k)\le\log X_N,
\qquad
\log\frac{X_N}{X_N-p^k}\le\log(2X_N),
\tag{22}
\]

their total contribution is

\[
O\!\left(\sqrt{X_N}\log^2 X_N\right)
=o(X_N).
\tag{23}
\]

For primes, use the same distance shells. When `H<sqrt(X_N)`, the trivial count of at most `O(H)` integer sites gives total contribution

\[
O\!\left(\sqrt{X_N}\log^2 X_N\right)
\tag{24}
\]

after summing the dyadic shells.

When `H>=sqrt(X_N)`, the Brun--Titchmarsh interval bound gives

\[
\#\{p:\ X_N-2H<p\le X_N-H\}
\ll \frac{H}{\log H}.
\tag{25}
\]

Because `log H >= (1/2)log X_N` in this range, the Mangoldt mass of such a shell is `O(H)`. Multiplying by the shell weight and summing gives

\[
\sum_{\substack{H\ \mathrm{dyadic}\\
\sqrt{X_N}\le H\le X_N}}
O\!\left(H\log\frac{2X_N}{H}\right)
=O(X_N).
\tag{26}
\]

Equations `(23)`--`(26)` prove

\[
S_\Lambda(X_N)\ll X_N.
\tag{27}
\]

Combining `(20)` and `(27)` proves `(17)`, and `(16)` gives the uniform endpoint modulus `(3)`.

### 4. A too-fast moving order cannot regularize Hardy--Littlewood oscillation

Hardy--Littlewood gives integer sequences `N_j^+ -> infinity` and `N_j^- -> infinity` and a constant `c>0` such that

\[
\psi(N_j^+)-N_j^+
\ge
c\sqrt{N_j^+}\,L(N_j^+),
\tag{28}
\]

and

\[
\psi(N_j^-)-N_j^-
\le
-c\sqrt{N_j^-}\,L(N_j^-).
\tag{29}
\]

If `(6)` holds, then `(3)` gives on either sequence

\[
\left|
\mathcal R_{\delta_{N_j}}[\Lambda-1](X_{N_j})
-
(\psi(N_j)-N_j)
\right|
\ll
\delta_{N_j}N_j
=
o\!\left(\sqrt{N_j}\,L(N_j)\right).
\tag{30}
\]

The perturbation is therefore asymptotically smaller than the positive and negative endpoint excursions. Their signs and order of magnitude survive, proving `(7)` and `(8)`.

For `(9)`,

\[
\frac{\delta_N\sqrt N}{L(N)}
=
\frac{N^{1/2-a}}{L(N)}
\longrightarrow0
\qquad(a\ge1/2),
\tag{31}
\]

which proves `(10)`.

### 5. Endpoint oscillation forces a subsequential growth rate for `K(delta)`

Take either absolute-value Hardy--Littlewood sequence `N_j` from `(28)`--`(29)` and set

\[
L_j:=L(N_j).
\tag{32}
\]

Let `C` be a valid constant in `(3)`, and choose

\[
\delta_j
:=
\frac{c}{4C}\frac{L_j}{\sqrt{N_j}}.
\tag{33}
\]

For large `j`, `0<delta_j<=1` and `delta_j->0`. By `(3)`, `(4)`, and the omega lower bound,

\[
\left|
\mathcal R_{\delta_j}[\Lambda-1](X_{N_j})
\right|
\ge
\frac c2\sqrt{N_j}\,L_j
\tag{34}
\]

after harmlessly adjusting constants for `X_{N_j}/N_j ->1`. Consequently

\[
K(\delta_j)\gg L_j.
\tag{35}
\]

From `(33)`,

\[
\log\frac1{\delta_j}
=
\frac12\log N_j
-
\log L_j
+O(1),
\tag{36}
\]

so

\[
\log\log\log\frac1{\delta_j}
=
\log\log\log N_j+o(1)
=L_j+o(1).
\tag{37}
\]

Equations `(35)` and `(37)` prove `(12)`--`(13)` under RH. If RH is false, AF-352 already implies `K(delta)=infinity` for each fixed positive `delta`, so the finite-conditioning interpretation is relevant only on the RH side.

## Prior art and novelty assessment

No novelty claim is made for the constituent analytic-number-theory ingredients.

- G. H. Hardy and J. E. Littlewood, **“Contributions to the Theory of the Riemann Zeta-Function and the Theory of the Distribution of Primes,”** *Acta Mathematica* 41, 119--196 (1916), DOI `10.1007/BF02422942`, is classical prior art for Riesz means of the von Mangoldt function and the endpoint oscillation input used in `(28)`--`(29)`.
- H. L. Montgomery and R. C. Vaughan, **“The large sieve,”** *Mathematika* 20(2), 119--134 (1973), DOI `10.1112/S0025579300004708`, supplies the classical Brun--Titchmarsh interval estimate used in `(25)`.
- G. H. Hardy and Marcel Riesz, ***The General Theory of Dirichlet's Series***, Cambridge Tracts in Mathematics and Mathematical Physics 18, Cambridge University Press (1915), is classical background for Riesz typical means and consistency between smoothing orders.

A targeted literature search found extensive classical work on fixed-order Riesz typical means, inclusion/consistency relations, and Riesz smoothing of arithmetic sums, but did not locate the exact coupled statement `(6)`--`(8)`. That absence is not treated as evidence of novelty. AF-354 is recorded as a derived synthesis of classical endpoint oscillation, a standard sieve upper bound, and the specific moving-order fidelity question created by AF-352--AF-353.

## Boundaries and failure modes

### The half-integer mesh is deliberate

The derivative of `(1-n/X)^delta` at `delta=0` contains

\[
\log\frac{X}{X-n}.
\tag{38}
\]

If `X` is allowed to approach an integer sample point arbitrarily closely, this logarithm has no uniform bound for that final atom. The half-integer mesh fixes a nonzero endpoint clearance and is already sufficient to inherit the classical omega obstruction. More generally, any mesh with a fixed positive distance from the integers admits the same argument with a mesh-dependent constant.

### The result is a one-sided obstruction, not a moving-order RH criterion

Condition `(6)` identifies schedules that are definitely too close to the unsmoothed endpoint. Its failure does not imply that the moving-order profile is `O(sqrt(X))`, nor does it provide an RH equivalence for `delta=delta(X)`.

In particular, AF-354 leaves open all power schedules `delta_N=N^{-a}` with `0<a<1/2` and all more general schedules for which `delta_N sqrt(N)` is comparable to or larger than `L(N)`.

### The `delta^{-2}` absolute zero budget is not contradicted

AF-353 measured the sum of the absolute critical-zero coefficients and found quadratic divergence as `delta->0+`. Equation `(13)` concerns the actual physical supremum profile and gives only a much smaller subsequential lower rate. The two quantities answer different questions; there remains a large unresolved gap between triangle-inequality conditioning and cancellation-aware conditioning.

### No optimality is claimed for the linear source modulus

Equation `(3)` is an absolute comparison obtained from `|Lambda(n)-1|` and therefore ignores cancellation in the source itself. It is strong enough to locate a forbidden moving-order regime, but it is not claimed to be the optimal modulus for the signed arithmetic source.

## Consequence for Arithmetic Fidelity

AF-352 showed that every **fixed** positive Riesz order preserves the off-critical zero discriminator while making the critical-line tail absolutely summable. AF-353 then showed that the fixed-order conditioning constant must diverge as the order approaches zero. AF-354 identifies the first source-side scale behind that singular limit.

The endpoint and large-scale limits do not commute. The relevant quantity is not merely whether `delta` is positive, but whether the amount of smoothing remains large enough compared with the source's own growing endpoint excursion. On the half-integer mesh,

\[
\boxed{
\text{Riesz perturbation from the endpoint}
\ \ll\ \delta X,
\qquad
\text{endpoint excursion}
\ \asymp_{\Omega}\ \sqrt X\log\log\log X.
}
\tag{39}
\]

Therefore the dimensionless competition is

\[
\boxed{
\frac{\delta\sqrt X}{\log\log\log X}.
}
\tag{40}
\]

When `(40)` tends to zero, the compression is too weak at the target scale: the endpoint obstruction survives unchanged. This sharpens the line's current distinction between **discriminator survival**, **fixed-parameter conditioning**, and **parameter-uniform conditioning**. A future positive moving-order theorem must now beat a concrete source-native obstruction rather than merely control AF-353's absolute zero budget.