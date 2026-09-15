# AF-355 — RH cancellation strengthens the moving-order endpoint obstruction to all polynomially vanishing Riesz orders

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `QUANTITATIVE-FIDELITY`, `ZERO-SENSITIVE-SOURCE`, `MOVING-PARAMETER-OBSTRUCTION`, `TARGET-METRIC-CALIBRATION`, `CONDITIONAL-RH`, `NO-NOVELTY-CLAIM`

## Claim

Retain AF-352--AF-354's notation

\[
c_n:=\Lambda(n)-1,
\qquad
\mathcal R_\delta[c](X)
:=
\sum_{n\le X}c_n\left(1-\frac nX\right)^\delta,
\qquad
X_N:=N+\frac12.
\tag{1}
\]

AF-354 obtained the unconditional endpoint modulus

\[
\left|\mathcal R_\delta[c](X_N)-\mathcal R_0[c](X_N)\right|
\ll \delta X_N,
\tag{2}
\]

which rules out sufficiently fast moving orders but deliberately discards all cancellation in `c_n`.

Under RH that cancellation can be retained by Abel summation. Uniformly for `N>=2` and `0<delta<=1`,

\[
\boxed{
\left|
\mathcal R_\delta[\Lambda-1](X_N)
-
\mathcal R_0[\Lambda-1](X_N)
\right|
\ll
\sqrt{X_N}\,\log^2(2X_N)
\min\!\left\{1,\delta\log(2X_N)\right\}.
}
\tag{3}
\]

In particular, whenever `delta log X_N <= 1`,

\[
\boxed{
\left|
\mathcal R_\delta[\Lambda-1](X_N)
-
\mathcal R_0[\Lambda-1](X_N)
\right|
\ll
\delta\sqrt{X_N}\,\log^3(2X_N).
}
\tag{4}
\]

Write

\[
L(N):=\log\log\log N
\tag{5}
\]

for sufficiently large `N`. Combining `(4)` with the classical Hardy--Littlewood oscillation of `psi(N)-N` gives the following **conditional obstruction on the RH side**. If RH holds and a moving order `delta_N in (0,1]` satisfies

\[
\boxed{
\frac{\delta_N\log^3 N}{L(N)}\longrightarrow0,
}
\tag{6}
\]

then

\[
\boxed{
\mathcal R_{\delta_N}[\Lambda-1](X_N)
=
\Omega_\pm\!\left(\sqrt N\,L(N)\right),
}
\tag{7}
\]

and therefore

\[
\mathcal R_{\delta_N}[\Lambda-1](X_N)\ne O(\sqrt N).
\tag{8}
\]

This strictly strengthens AF-354 in the regime relevant to an RH-compatible moving-order theorem. In particular, for every fixed `a>0`,

\[
\boxed{
\delta_N=N^{-a}
\quad\Longrightarrow\quad
\mathcal R_{\delta_N}[\Lambda-1](X_N)
\ne O(\sqrt N)
\quad\text{under RH}.
}
\tag{9}
\]

Thus **every polynomially vanishing Riesz order is already too close to the unsmoothed endpoint** to preserve the sharp critical `sqrt(X)` norm. The same conclusion holds for `delta_N=(log N)^{-A}` whenever `A>=3`. The much slower region

\[
\delta_N\gtrsim \frac{L(N)}{\log^3N}
\tag{10}
\]

remains open; failure of `(6)` is not a positive theorem.

There is also a stronger subsequential lower rate for AF-353's fixed-order conditioning profile

\[
K(\delta)
:=
\sup_{X\ge2,\ X\notin\mathbb N}
X^{-1/2}
\left|\mathcal R_\delta[\Lambda-1](X)\right|.
\tag{11}
\]

Under RH there is a sequence `delta_j->0+` such that

\[
\boxed{
K(\delta_j)\gg \log\log\frac1{\delta_j}.
}
\tag{12}
\]

Equivalently,

\[
\boxed{
\limsup_{\delta\downarrow0}
\frac{K(\delta)}{\log\log(1/\delta)}>0.
}
\tag{13}
\]

This improves AF-354's `log log log(1/delta)` subsequential lower rate by using the RH cancellation already available in the source partial sums rather than the absolute source mass.

## Derivation

### 1. Abel summation exposes the correct cancellation resource

Let

\[
C(t):=\sum_{n\le t}c_n
=\psi(t)-\lfloor t\rfloor.
\tag{14}
\]

Assume RH. Schoenfeld's classical conditional estimate gives, for all sufficiently large `t`,

\[
|\psi(t)-t|\ll \sqrt t\,\log^2 t.
\tag{15}
\]

After absorbing the floor correction and the finite initial range,

\[
|C(t)|\ll \sqrt t\,\log^2(2t)
\qquad(t\ge1).
\tag{16}
\]

For fixed `X=X_N` and

\[
w_\delta(t):=\left(1-\frac tX\right)^\delta,
\tag{17}
\]

Abel summation gives

\[
\mathcal R_\delta[c](X)
=
C(N)w_\delta(N)
-
\int_1^N C(t)w_\delta'(t)\,dt.
\tag{18}
\]

Since

\[
w_\delta'(t)
=-\frac\delta X
\left(1-\frac tX\right)^{\delta-1},
\tag{19}
\]

and `h:=1-N/X=1/(2X)`, equations `(18)`--`(19)` imply

\[
\begin{aligned}
\mathcal R_\delta[c](X)-\mathcal R_0[c](X)
&=
C(N)(h^\delta-1)\\
&\quad+
\frac\delta X
\int_1^N
C(t)\left(1-\frac tX\right)^{\delta-1}dt.
\end{aligned}
\tag{20}
\]

This is the signed analogue of AF-354's absolute comparison. The crucial difference is that the arithmetic cancellation is compressed into the already-controlled partial sum `C(t)` before the endpoint singularity is integrated.

### 2. The endpoint singularity costs only one extra logarithm under RH

From `(16)`, for `1<=t<=N<X`,

\[
|C(t)|\ll \sqrt X\,\log^2(2X).
\tag{21}
\]

The boundary factor satisfies

\[
1-h^\delta
=
1-e^{-\delta\log(1/h)}
\le
\min\!\{1,\delta\log(1/h)\}.
\tag{22}
\]

For the integral term, direct integration gives

\[
\frac\delta X
\int_1^N
\left(1-\frac tX\right)^{\delta-1}dt
=
\left(1-\frac1X\right)^\delta-h^\delta
\le
1-h^\delta.
\tag{23}
\]

Because `h=1/(2X)`, equations `(20)`--`(23)` yield

\[
\left|
\mathcal R_\delta[c](X)-\mathcal R_0[c](X)
\right|
\ll
\sqrt X\,\log^2(2X)
\min\!\{1,\delta\log(2X)\},
\tag{24}
\]

which is `(3)`. In the small-order regime `delta log(2X)<=1`, this becomes `(4)`.

The extra `log X` is not inserted by a zero-sum triangle inequality. It is the explicit cost of approaching the kernel endpoint in the Abel kernel. The two earlier logarithms come from the standard RH control of the signed prime error itself.

### 3. Every polynomially vanishing order inherits the endpoint oscillation

Hardy--Littlewood's classical oscillation theorem supplies integer sequences `N_j^+->infinity` and `N_j^-->infinity` and a constant `c>0` such that

\[
\psi(N_j^+)-N_j^+
\ge
c\sqrt{N_j^+}\,L(N_j^+),
\tag{25}
\]

and

\[
\psi(N_j^-)-N_j^-
\le
-c\sqrt{N_j^-}\,L(N_j^-).
\tag{26}
\]

Since

\[
\mathcal R_0[\Lambda-1](X_N)=\psi(N)-N,
\tag{27}
\]

condition `(6)` and `(4)` imply on either oscillation sequence

\[
\left|
\mathcal R_{\delta_{N_j}}[\Lambda-1](X_{N_j})
-(\psi(N_j)-N_j)
\right|
=
o\!\left(\sqrt{N_j}\,L(N_j)\right).
\tag{28}
\]

The perturbation is smaller than the positive and negative endpoint excursions, so their signs and order of magnitude survive. This proves `(7)`--`(8)`.

For `delta_N=N^{-a}` with any `a>0`,

\[
\frac{N^{-a}\log^3N}{L(N)}\longrightarrow0,
\tag{29}
\]

proving `(9)`. Likewise `delta_N=(log N)^{-A}` satisfies `(6)` for every `A>=3` because

\[
\frac{\log^{3-A}N}{L(N)}\longrightarrow0.
\tag{30}
\]

AF-354's unconditional argument reached only `a>=1/2`; the RH partial-sum estimate therefore closes the entire remaining polynomial window `0<a<1/2` on the RH side.

### 4. The same modulus upgrades the lower growth rate of `K(delta)`

Take an absolute-value Hardy--Littlewood sequence `N_j` from `(25)`--`(26)` and write

\[
L_j:=L(N_j).
\tag{31}
\]

Let `C_0` be a constant valid in the small-order form `(4)`. Choose a sufficiently small fixed `eta>0` and set

\[
\delta_j
:=
\eta\frac{L_j}{\log^3 N_j}.
\tag{32}
\]

Then `delta_j->0`, `delta_j log N_j->0`, and by choosing `eta` relative to the omega constant and `C_0`, equations `(4)` and `(25)`--`(27)` give

\[
\left|
\mathcal R_{\delta_j}[\Lambda-1](X_{N_j})
\right|
\gg
\sqrt{N_j}\,L_j.
\tag{33}
\]

Hence

\[
K(\delta_j)\gg L_j.
\tag{34}
\]

But `(32)` gives

\[
\log\frac1{\delta_j}
=
3\log\log N_j
-
\log L_j
+O(1),
\tag{35}
\]

and therefore

\[
\log\log\frac1{\delta_j}
=
\log\log\log N_j+O(1)
=
L_j+O(1).
\tag{36}
\]

Combining `(34)`--`(36)` proves `(12)`--`(13)`.

## Prior art and novelty assessment

No novelty claim is made for the constituent ingredients.

- Lowell Schoenfeld, **“Sharper Bounds for the Chebyshev Functions θ(x) and ψ(x). II,”** *Mathematics of Computation* 30(134), 337--360 (1976), DOI `10.2307/2005976`. Theorem 10 gives under RH the explicit bound `|psi(x)-x| < (8pi)^{-1} sqrt(x) log^2 x` for `x>=73.2`, which supplies `(15)`.
- G. H. Hardy and J. E. Littlewood, **“Contributions to the Theory of the Riemann Zeta-Function and the Theory of the Distribution of Primes,”** *Acta Mathematica* 41, 119--196 (1916), DOI `10.1007/BF02422942`, supplies the classical Riesz/von-Mangoldt framework and the endpoint oscillation input used in `(25)`--`(26)`.
- G. H. Hardy and Marcel Riesz, ***The General Theory of Dirichlet's Series***, Cambridge Tracts in Mathematics and Mathematical Physics 18, Cambridge University Press (1915), is classical background for Riesz typical means and Abel/Dirichlet summation methods.

A targeted search for Riesz means of the von Mangoldt function, small or variable smoothing order, and RH endpoint estimates found the classical fixed-order Riesz framework and extensive neighboring work on Riesz summability, but did not locate the exact coupled estimate `(3)` or the moving-order consequence `(6)`--`(9)`. That absence is not treated as evidence of novelty. AF-355 is recorded as a source-native consequence of combining standard RH partial-sum control with the endpoint comparison question isolated by AF-354.

## Boundaries and failure modes

### The strengthening is conditional on RH

Unlike AF-354's modulus `(2)`, equation `(3)` uses the RH estimate for `psi(t)-t`. It therefore cannot replace AF-354 as an unconditional statement. Its role is narrower but strategically sharper: **even on the favorable RH branch**, where every fixed positive order is well conditioned by AF-352, a large class of orders tending to zero still fails the uniform critical norm.

### The result remains one-sided

Condition `(6)` is sufficient for endpoint inheritance, not necessary. Nothing here proves that schedules with `delta_N log^3N` comparable to or larger than `L(N)` satisfy `O(sqrt N)`. In particular, the transition scale in `(10)` is an obstruction boundary produced by the present modulus, not a proved phase transition.

### The logarithmic loss is not claimed optimal

The factor `log^3X` comes from the classical uniform RH bound `|C(t)|<<sqrt(t)log^2t` plus one endpoint logarithm. Better cancellation information localized to the terminal interval could improve this modulus. Conversely, the derivation does not justify removing any logarithm merely from fixed-order spectral cancellation.

### The half-integer mesh remains part of the comparison

As in AF-354, `X_N=N+1/2` keeps the last sampled atom a fixed positive distance from the kernel endpoint. The estimate extends to meshes with comparable fixed endpoint clearance, but no uniform claim is made as a noninteger `X` approaches an integer arbitrarily closely while `delta->0`.

### The stronger `K(delta)` rate is still subsequential

Equation `(12)` uses the sparse sequences supplied by the omega theorem. It does not give a pointwise lower bound for every sufficiently small `delta`, and it remains vastly below AF-353's `delta^{-2}` absolute zero-coefficient budget. The gap continues to measure unresolved cancellation among critical zero modes.

## Consequence for Arithmetic Fidelity

AF-354 priced endpoint recovery using absolute source mass and obtained the competition `delta sqrt(X)/L(X)`. AF-355 shows that this is not the intrinsic source-side scale once the source is known to satisfy its RH cancellation law. Under RH, the relevant signed perturbation is instead

\[
\text{endpoint perturbation}
\ll
\delta\sqrt X\log^3X
\tag{37}
\]

in the small-order regime, while the endpoint itself has excursions of size

\[
\sqrt X\,L(X).
\tag{38}
\]

The resulting dimensionless competition is

\[
\boxed{
\frac{\delta\log^3X}{\log\log\log X}.
}
\tag{39}
\]

This is a clean example of **conditional fidelity depending on source regularity**. The same compression kernel has a much smaller effective distance from the identity when measured on a source class with strong signed partial-sum cancellation than when measured on arbitrary coefficient mass. In Arithmetic Fidelity terms, a compression cannot be assigned a single conditioning cost independently of the source class and target norm: the recoverability modulus is jointly controlled by the transform, the source regularity available before compression, and the metric in which the preserved discriminator is tested.
