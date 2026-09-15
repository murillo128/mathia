# AF-357 — Riesz small order samples exponentially thin endpoint shells and scalar source bounds cannot improve the endpoint modulus

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `QUANTITATIVE-FIDELITY`, `MOVING-PARAMETER-OBSTRUCTION`, `TARGET-METRIC-CALIBRATION`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-355 bounds the difference between a positive-order Riesz profile and the unsmoothed endpoint by

\[
\left|\mathcal R_\delta[\Lambda-1](X_N)-\mathcal R_0[\Lambda-1](X_N)\right|
\ll
\sqrt{X_N}\log^2(2X_N)\min\{1,\delta\log(2X_N)\},
\tag{1}
\]

under RH, while AF-356 shows that the same endpoint is nevertheless stable in Besicovitch `B^2`. The present finding identifies the physical scale hidden in `(1)` and proves that the factor `min{1,delta log X}` cannot be improved from the scalar source information used by AF-355, even after adding the trivial individual-jump bound.

For an arbitrary coefficient sequence `(c_n)` with partial sums

\[
C(t):=\sum_{n\le t}c_n,
\tag{2}
\]

define for noninteger `X=e^y` and `delta>0`

\[
\mathcal R_\delta[c](X)
:=
\sum_{n\le X}c_n\left(1-\frac nX\right)^\delta,
\qquad
E_\delta(y):=e^{-y/2}\mathcal R_\delta[c](e^y),
\tag{3}
\]

and set

\[
E_0(y):=e^{-y/2}C(e^y),
\tag{4}
\]

with `E_0(y)=0` below the first coefficient. Then the Riesz transform has the exact one-sided Beta-kernel representation

\[
\boxed{
E_\delta(y)
=
\delta\int_0^1
u^{1/2}E_0(y+\log u)(1-u)^{\delta-1}\,du.
}
\tag{5}
\]

Writing

\[
m_\delta
:=
\delta B\!\left(\frac32,\delta\right)
=
\frac{\Gamma(1+\delta)\Gamma(3/2)}{\Gamma(3/2+\delta)},
\tag{6}
\]

and letting `W_delta` have the `Beta(delta,3/2)` distribution, `(5)` is equivalently

\[
\boxed{
E_\delta(y)
=
m_\delta\,\mathbb E\left[
E_0\!\left(y+\log(1-W_\delta)\right)
\right],
}
\tag{7}
\]

with

\[
m_\delta
=
1-2(1-\log 2)\delta+O(\delta^2).
\tag{8}
\]

The small-order kernel does **not** probe a relative endpoint layer of width comparable to `delta`. Its quantiles are exponentially smaller. Precisely,

\[
\boxed{
-\delta\log W_\delta
\ \xrightarrow[d]{\delta\downarrow0}\ 
\operatorname{Exp}(1).
}
\tag{9}
\]

Hence, for every fixed `q in (0,1)`, if `w_q(delta)` is the `q`-quantile of `W_delta`, then

\[
\boxed{
\delta\log\frac1{w_q(\delta)}\longrightarrow-\log q,
\qquad
w_q(\delta)
=
\exp\!\left(\frac{\log q+o(1)}{\delta}\right).
}
\tag{10}
\]

Thus `delta` corresponds to a physical relative source scale `exp(-Theta(1/delta))`. In particular, `delta=a/log X` produces polynomial relative lags, while `delta=(log X)^{-A}` with `A>1` probes superpolynomially thin endpoint shells.

There is also an exact sharpness statement for AF-355's source-envelope argument. Put

\[
X=N+\frac12,
\qquad
h:=1-\frac NX=\frac1{2X},
\qquad
a:=1-\frac1X,
\tag{11}
\]

and regard

\[
D_{\delta,X}(C)
:=
\mathcal R_\delta[c](X)-\mathcal R_0[c](X)
\tag{12}
\]

as a linear functional of the discrete partial-sum profile. With the norm

\[
\|C\|_\infty:=\max_{1\le k\le N}|C(k)|,
\tag{13}
\]

its exact operator norm is

\[
\boxed{
\|D_{\delta,X}\|
=
1+a^\delta-2h^\delta.
}
\tag{14}
\]

Consequently, uniformly for `X>=5/2` and `0<delta<=1`,

\[
\boxed{
\|D_{\delta,X}\|
\asymp
\min\{1,\delta\log(2X)\}.
}
\tag{15}
\]

If `delta log X -> 0`, then more precisely

\[
\|D_{\delta,X}\|
=
\delta\log\!\bigl(4X(X-1)\bigr)
+O\!\left(\delta^2\log^2(2X)\right)
\sim 2\delta\log X.
\tag{16}
\]

So the logarithmic endpoint loss in AF-355 is not an artifact of a loose integration estimate: it is the exact worst-case modulus of the Riesz-to-endpoint map when the only retained source resource is a uniform bound on `C`.

Finally, adding a per-step jump bound does not change the order at the arithmetic scale. Let `M,J>0`, let

\[
r:=\left\lceil\frac MJ\right\rceil,
\qquad
s:=\left\lceil\frac{2M}{J}\right\rceil,
\tag{17}
\]

and suppose

\[
X\ge16\left(1+\frac MJ\right).
\tag{18}
\]

Then there is a coefficient sequence supported on `{1,...,N}` such that

\[
|C(k)|\le M,
\qquad
|c_k|\le J,
\tag{19}
\]

for every `k`, but

\[
\boxed{
|D_{\delta,X}(C)|
\ge
cM\min\!\left\{
1,
\delta\log\!\left(\frac{X}{1+M/J}\right)
\right\}
}
\tag{20}
\]

for all `0<delta<=1`, with a universal constant `c>0`.

For the RH-calibrated scalar resources

\[
M_X\asymp\sqrt X\log^2X,
\qquad
J_X\asymp\log X,
\tag{21}
\]

one has

\[
\log\!\left(\frac{X}{1+M_X/J_X}\right)
=
\frac12\log X-\log\log X+O(1),
\tag{22}
\]

so `(20)` has the same `M_X min{1,delta log X}` order as AF-355. Therefore neither the RH pointwise envelope for the signed prime error nor that envelope plus the individual Mangoldt jump-size bound can, by themselves, yield a better moving-order comparison theorem.

This is an abstract-source obstruction, not a construction of alternative primes. It says exactly which information is still missing: an improvement for the actual `Lambda-1` source must use coupling across scales -- for example local signed averages, maximal/tail control, endpoint-to-past correlation, or zero-phase structure -- rather than only scalar bounds on partial sums and jumps.

## Derivation

### 1. Abel summation gives the Beta kernel exactly

For `delta>0`, Stieltjes integration by parts gives

\[
\mathcal R_\delta[c](X)
=
\frac\delta X
\int_0^X
C(t)\left(1-\frac tX\right)^{\delta-1}dt.
\tag{23}
\]

Substitute `t=Xu`. Since

\[
e^{-y/2}C(e^yu)
=
u^{1/2}E_0(y+\log u),
\tag{24}
\]

one obtains `(5)`. Now set `w=1-u`. The unnormalized kernel becomes

\[
\delta(1-w)^{1/2}w^{\delta-1}dw,
\tag{25}
\]

whose total mass is `m_delta` in `(6)`. Normalizing it gives `W_delta~Beta(delta,3/2)` and proves `(7)`. Equation `(8)` follows from the logarithmic derivative of the Gamma ratio:

\[
\frac{d}{d\delta}\log m_\delta\bigg|_{\delta=0}
=
\psi(1)-\psi(3/2)
=
2\log2-2.
\tag{26}
\]

The representation makes the endpoint geometry explicit. For `X=N+1/2`, the unsmoothed partial sum is constant on the final interval `[N,X)`, whose relative width is `h=1/(2X)`. The mass that the Beta kernel places inside that final plateau is asymptotically controlled by `h^delta`. Thus the natural geometric transition occurs when `delta log X` is order one, exactly the parameter appearing in AF-355.

### 2. The logarithm of the Beta lag has an exponential limit

Fix `z>0` and put `x_delta=exp(-z/delta)`. Then

\[
\mathbb P(-\delta\log W_\delta>z)
=
\mathbb P(W_\delta<x_\delta)
=
\frac{\int_0^{x_\delta}w^{\delta-1}(1-w)^{1/2}dw}
{B(\delta,3/2)}.
\tag{27}
\]

Because `x_delta->0`, uniformly on the numerator range `(1-w)^{1/2}=1+o(1)`, while

\[
\int_0^{x_\delta}w^{\delta-1}dw
=
\frac{x_\delta^\delta}{\delta}
=
\frac{e^{-z}}{\delta},
\qquad
B(\delta,3/2)\sim\frac1\delta.
\tag{28}
\]

Therefore the tail in `(27)` tends to `e^{-z}`, proving `(9)` and the quantile law `(10)`.

This scaling is useful because it translates a formal smoothing order into the actual source resolution. A theorem formulated in `delta` alone can look weak or strong for the wrong reason unless its hypotheses are compared at the corresponding `exp(-Theta(1/delta))` endpoint scale.

### 3. The partial-sum envelope has an exact endpoint-comparison norm

AF-355's Abel identity, specialized to `X=N+1/2`, is

\[
D_{\delta,X}(C)
=
(h^\delta-1)C(N)
+
\frac\delta X
\int_1^N
C(t)\left(1-\frac tX\right)^{\delta-1}dt.
\tag{29}
\]

The terminal coefficient is negative and the integral measure is positive. Its total mass is

\[
\frac\delta X
\int_1^N
\left(1-\frac tX\right)^{\delta-1}dt
=
a^\delta-h^\delta.
\tag{30}
\]

Hence the total variation of the functional is exactly

\[
(1-h^\delta)+(a^\delta-h^\delta)
=
1+a^\delta-2h^\delta,
\tag{31}
\]

which proves the upper bound in `(14)`. Equality is attained by the admissible partial-sum profile `C(k)=1` for `k<N` and `C(N)=-1` (equivalently `c_1=1`, `c_N=-2`, and all other `c_k=0`), proving the exact norm.

For `0<delta<=1`, write `L=log(1/h)=log(2X)`. Since

\[
1-h^\delta=1-e^{-\delta L}\asymp\min\{1,\delta L\},
\tag{32}
\]

while `1-a^delta=O(delta/X)`, `(15)` follows. Expanding both exponentials in the regime `delta log X->0` yields `(16)`.

Thus any proof that uses only a uniform envelope `|C(t)|<=M` is already optimal, up to constants, at the level of abstract source classes. A smaller modulus requires a structural restriction on which sign profiles of `C` are actually admissible.

### 4. A jump-size bound still admits the same endpoint scale

Let `r,s` be as in `(17)`. Construct discrete partial sums as follows. Starting from `C(0)=0`, increase to `+M` in `r` steps with increments of magnitude at most `J`; keep `C(k)=M` through the central plateau; over the final `s` steps decrease linearly from `+M` to `-M`. Since `2M/s<=J`, the resulting coefficients satisfy `(19)`.

Condition `(18)` gives

\[
r\le\frac X{16},
\qquad
q:=\frac{s+1/2}{X}\le\frac18,
\qquad
A:=1-\frac rX\ge\frac{15}{16}.
\tag{33}
\]

In `(29)`, the initial ramp is nonnegative and may be discarded in a lower bound. On the central interval use `C=M`; on the final ramp use only `C>=-M`; and use the exact terminal value `C(N)=-M`. This gives

\[
\frac{D_{\delta,X}(C)}M
\ge
1+A^\delta-2q^\delta.
\tag{34}
\]

Now

\[
1+A^\delta-2q^\delta
=
2(1-q^\delta)-(1-A^\delta).
\tag{35}
\]

Because `q<=1/8`,

\[
1-q^\delta\asymp\min\{1,\delta\log(1/q)\},
\tag{36}
\]

whereas `1-A^delta<=delta log(16/15)`. The latter is a uniformly smaller-order subtraction relative to `(36)`, so `(34)` implies

\[
D_{\delta,X}(C)
\gg
M\min\{1,\delta\log(1/q)\}.
\tag{37}
\]

Since `s<=2M/J+1`, condition `(18)` makes

\[
\log(1/q)
\asymp
\log\!\left(\frac{X}{1+M/J}\right)
\tag{38}
\]

at the level needed inside `min{1,delta(.)}`, proving `(20)` after adjusting a universal constant.

The point of `(20)` is not that this artificial sequence resembles `Lambda-1`. It is a sufficiency test for the information used by the proof: every sequence in this class obeys the same two scalar resources that one would feed into an envelope-plus-jump argument, yet some members still attain the AF-355 endpoint scale. Those resources therefore cannot certify a smaller modulus.

## Arithmetic calibration and what remains open

For `c_n=Lambda(n)-1`, RH gives the classical envelope

\[
|C(t)|=|\psi(t)-\lfloor t\rfloor|
\ll\sqrt t\log^2(2t),
\tag{39}
\]

while trivially, for `n<=X`,

\[
|c_n|\le\log X+1.
\tag{40}
\]

Taking the coarser uniform resources `M_X asymp sqrt(X)log^2X` and `J_X asymp log X` in the abstract class yields `(22)`. Therefore merely combining Schoenfeld-type partial-sum control with the pointwise Mangoldt bound cannot close AF-355's slow moving-order window.

AF-356 independently shows that the normalized endpoint is Lipschitz-stable in `B^2` even while the supremum conditioning diverges. Together, AF-356 and the present sharpness result isolate the missing resource more tightly: it must constrain **rare coherent endpoint excursions across the Beta-distributed one-sided lag hierarchy**. Mean-square control is too weak, and scalar `L^infinity` plus jump size is also too weak.

A natural next audit is therefore source-native and scale-aware. Any proposed maximal, short-interval, signed-average, or phase-coherence estimate should first be translated to the physical relative lag `w~exp(-Theta(1/delta))` from `(10)`, then tested for enough uniformity to control the supremum Riesz-to-endpoint difference in the slow regime left open by AF-355. Failure to beat `(20)` on an appropriately arithmetic source class would be a genuine no-go result; success only for the unrestricted scalar class is impossible by the theorem above.

## Prior art and novelty assessment

No novelty claim is made for the constituent summability or Beta-function machinery.

- G. H. Hardy and Marcel Riesz, *The General Theory of Dirichlet's Series*, Cambridge Tracts in Mathematics and Mathematical Physics 18, Cambridge University Press (1915). Role: classical Riesz typical means, Dirichlet-series summability, and Abel/partial-summation framework.
- G. H. Hardy and J. E. Littlewood, **“Contributions to the Theory of the Riemann Zeta-Function and the Theory of the Distribution of Primes,”** *Acta Mathematica* 41 (1916), 119–196, DOI `10.1007/BF02422942`. Role: classical Riesz/von-Mangoldt background and the prime-error setting used by AF-351–AF-355.
- B. Kuttner, **“Some Theorems on the Relation between Riesz and Abel Typical Means,”** *Proceedings of the Cambridge Philosophical Society* 57(1) (1961), 61–75, DOI `10.1017/S0305004100034861`. Role: established comparison theory between Riesz and Abel typical means; confirms that the kernel manipulation sits inside classical summability theory.
- Lowell Schoenfeld, **“Sharper Bounds for the Chebyshev Functions θ(x) and ψ(x). II,”** *Mathematics of Computation* 30(134) (1976), 337–360, DOI `10.2307/2005976`. Role: the standard RH `sqrt(x) log^2 x` prime-error envelope used only for the arithmetic calibration `(39)`.
- Andreas Defant and Ingo Schoolmann, **“Riesz means in Hardy spaces on Dirichlet groups,”** arXiv:`1908.06458` (2019). Role: neighboring modern maximal-operator treatment of Riesz means for Dirichlet groups and ordinary Dirichlet series; useful context that maximal Riesz control is an established analytic direction rather than a Mathia-invented category.

A targeted search for small/variable Riesz order, Beta-kernel endpoint scaling, Riesz-to-endpoint operator norms, and maximal Riesz control did not locate the exact combination `(9)`, `(14)`, and `(20)` for this arithmetic endpoint problem. That absence is not evidence of novelty. The durable contribution recorded here is the source-audit consequence: the current scalar resources are provably insufficient to improve the moving-order modulus, and the smoothing parameter has an explicit exponential physical-lag interpretation that any stronger arithmetic theorem must respect.

## Boundaries and failure modes

### The sharpness examples are not generalized-prime controls

The profiles attaining `(14)` and `(20)` are abstract coefficient sequences. They show insufficiency of declared source summaries, not existence of a Beurling-prime system, Euler product, or zeta-like object with the same behavior. No conclusion about RH follows from them alone.

### The Beta law is a kernel statement, not a concentration theorem for primes

Equation `(10)` describes where the Riesz kernel places weight. It says nothing by itself about the size, sign, or correlation of `psi(x)-x` on those shells. Arithmetic information enters only through the source profile being averaged.

### `delta log X ~ 1` is a geometric kernel transition, not the solved RH threshold

The final half-step has relative width `1/(2X)`, so the Beta kernel changes from being mostly trapped in that plateau to sampling earlier partial sums around the `delta log X=Theta(1)` scale. This does not prove that the actual prime profile changes behavior exactly there. AF-355's rigorous oscillation transfer currently reaches a much smaller regime; the gap is precisely where stronger source information is required.

### Jump control is deliberately scalar

Equation `(20)` rules out improvement from a uniform bound on individual `|c_n|` combined with `sup|C|`. It does not rule out short-interval cancellation, correlation inequalities, structured sign constraints, maximal estimates, or zero-based phase information. Those are the intended remaining escape routes.

## Consequence for Arithmetic Fidelity

AF-353–AF-356 established that arbitrarily weak positive Riesz smoothing preserves the RH discriminator at every fixed order, becomes singular in uniform conditioning as the order tends to zero, transfers endpoint oscillation for sufficiently fast moving orders, and yet remains stable in mean square. AF-357 adds the missing source-resolution map and a sharp proof-resource audit.

The smoothing order should henceforth be interpreted through the scale

\[
w\sim e^{-\Theta(1/\delta)},
\tag{41}
\]

not through `w~delta`. At that scale, the `min{1,delta log X}` loss is already optimal for every argument whose source input is only a partial-sum envelope, even if a pointwise jump bound is added. The unresolved Arithmetic Fidelity question is therefore no longer “can Abel summation be sharpened?” but “what source-native cross-scale constraint of the rational-prime error excludes the abstract endpoint profiles that saturate `(20)` while remaining strong enough to control the supremum target?”
