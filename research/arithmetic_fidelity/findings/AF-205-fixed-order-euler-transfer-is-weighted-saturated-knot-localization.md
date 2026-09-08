# AF-205 — Fixed-order Euler transfer is exactly weighted saturated knot localization

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-BRIDGE`, `QUANTITATIVE-RECOVERY`, `SOURCE-LOCALIZATION`, `ARITHMETIC-CONTROL`, `NO-NOVELTY-CLAIM`

## Claim

AF-204 identifies the exact varying-profile transfer gate for the quartic five-node Euler control. The same mechanism is not peculiar to order four. For every **fixed cancellation order** `m>=1`, the full finite vertical band is quantitatively calibrated by one positive real-axis defect, and minimal-support source geometry converts that defect into a saturated knot-diameter resource.

Fix

\[
m\ge1,\qquad x>0,\qquad \sigma>0,\qquad T<\infty,
\]

and write

\[
F_s(u)=-\log(1-e^{-su}),
\qquad s=\sigma+i\tau,
\qquad |\tau|\le T.
\]

Define the sign-corrected `m`-th derivative

\[
g_{m,\tau}(u)
:=(-1)^mF_{\sigma+i\tau}^{(m)}(u)
=(\sigma+i\tau)^m
\sum_{k\ge1}k^{m-1}e^{-k(\sigma+i\tau)u}.
\tag{1}
\]

On the real axis,

\[
g_{m,0}(u)
=\sigma^m\sum_{k\ge1}k^{m-1}e^{-k\sigma u}>0
\tag{2}
\]

and `g_{m,0}` is strictly decreasing on `(0,infinity)`.

Let `nu=mu_+-mu_-` be the normalized minimal-support order-`m` moment-flat source on `m+1` distinct ordered knots

\[
x=u_0<u_1<\cdots<u_m,
\qquad D:=u_m-x,
\tag{3}
\]

as in AF-195/AF-199. Put

\[
\delta:=W_1(\mu_+,\mu_-)>0,
\qquad
Q_m:=\frac{\int u^m\,d\nu(u)}{\delta^m}>0,
\tag{4}
\]

and let `beta` be the normalized positive Peano B-spline carrier. Then

\[
\widetilde E_m(\tau)
:=(-1)^m\delta^{-m}
\int F_{\sigma+i\tau}(u)\,d\nu(u)
=
\frac{Q_m}{m!}
\int g_{m,\tau}(v)\,d\beta(v).
\tag{5}
\]

Define the real-axis endpoint defect

\[
\Lambda_{m,\sigma}(\beta)
:=
1-
\frac{1}{g_{m,0}(x)}
\int g_{m,0}(v)\,d\beta(v),
\tag{6}
\]

and the observation-weighted saturated diameter function

\[
c_{m,\sigma,x}(r)
:=
1-
\frac{g_{m,0}(x+r)}{g_{m,0}(x)},
\qquad r\ge0.
\tag{7}
\]

There is a finite constant `C=C(m,x,sigma,T)` such that

\[
\boxed{
\frac{g_{m,0}(x)}{m!}
Q_m\Lambda_{m,\sigma}(\beta)
\le
\sup_{|\tau|\le T}
\left|
\widetilde E_m(\tau)
-
\frac{Q_m}{m!}g_{m,\tau}(x)
\right|
\le
\frac{C g_{m,0}(x)}{m!}
Q_m\Lambda_{m,\sigma}(\beta).
}
\tag{8}
\]

The source geometry itself satisfies the stronger all-order comparison

\[
\boxed{
\frac{m^m}{(m+1)^{m+1}}
\,c_{m,\sigma,x}(D)
\le
\Lambda_{m,\sigma}(\beta)
\le
c_{m,\sigma,x}(D).
}
\tag{9}
\]

Consequently the entire fixed-band discrepancy is two-sided comparable to

\[
\boxed{Q_m\,c_{m,\sigma,x}(D).}
\tag{10}
\]

For any sequence at fixed `m,x,sigma,T`, therefore,

\[
\boxed{
\sup_{|\tau|\le T}
\left|
\widetilde E_{m,n}(\tau)
-
\frac{Q_{m,n}}{m!}g_{m,\tau}(x)
\right|
\longrightarrow0
\quad\Longleftrightarrow\quad
Q_{m,n}c_{m,\sigma,x}(D_n)\longrightarrow0.
}
\tag{11}
\]

The function `c_{m,sigma,x}` is increasing and concave, vanishes at zero, and tends to one at infinity. Hence, with constants depending only on `m,x,sigma`,

\[
c_{m,\sigma,x}(D)\asymp \min\{D,1\},
\tag{12}
\]

so the same gate has the simpler equivalent form

\[
\boxed{
Q_{m,n}\min\{D_n,1\}\longrightarrow0.
}
\tag{13}
\]

Thus the fixed-order minimal-support Euler problem has an exact source-side resource at every order: **surviving moment profile multiplied by observation-saturated physical localization**. Ordinary diameter is the correct local coordinate when `D->0`, but it is not the globally intrinsic resource; once the source has moved beyond the Euler observation scale, the localization penalty saturates rather than continuing to grow linearly.

## Derivation

### 1. Peano transport gives the all-order normalized Euler profile

AF-195 gives, for the normalized signed source,

\[
\int u^m\,d\nu(u)=\frac1A,
\tag{14}
\]

where `A` is the positive barycentric mass. AF-199 gives the normalized Peano representation

\[
\int f\,d\nu
=
\frac{1}{A m!}
\int f^{(m)}(v)\,d\beta(v).
\tag{15}
\]

Since `Q_m=(A\delta^m)^{-1}`, substituting `f=F_s` into `(15)` and multiplying by `(-1)^m delta^{-m}` yields `(5)` exactly.

The Euler logarithm is absolutely represented for `Re(s)>0` by

\[
F_s(u)=\sum_{k\ge1}\frac{e^{-ksu}}k.
\tag{16}
\]

Termwise differentiation on every half-plane `Re(s)>=sigma>0`, `u>=x>0`, gives `(1)`. At `tau=0`, `(2)` is positive and

\[
g_{m,0}'(u)
=-\sigma^{m+1}
\sum_{k\ge1}k^m e^{-k\sigma u}<0.
\tag{17}
\]

Hence the defect `(6)` is nonnegative and vanishes only when the positive carrier is concentrated at the anchor.

### 2. One real positive defect controls the whole complex finite band

Put

\[
h(v):=g_{m,0}(x)-g_{m,0}(v).
\tag{18}
\]

Then

\[
g_{m,0}(x)\Lambda_{m,\sigma}(\beta)
=
\int h(v)\,d\beta(v).
\tag{19}
\]

For fixed `m,x,sigma,T`, the exponential series gives finite constants

\[
M:=\sup_{v\ge x,\ |\tau|\le T}|g_{m,\tau}(v)|<\infty,
\qquad
L:=\sup_{v\ge x,\ |\tau|\le T}|g_{m,\tau}'(v)|<\infty.
\tag{20}
\]

Strict negativity of `(17)` also gives

\[
m_0:=\min_{x\le w\le x+1}(-g_{m,0}'(w))>0.
\tag{21}
\]

For `x<=v<=x+1`,

\[
|g_{m,\tau}(v)-g_{m,\tau}(x)|
\le L(v-x)
\le \frac{L}{m_0}h(v).
\tag{22}
\]

For `v>=x+1`,

\[
|g_{m,\tau}(v)-g_{m,\tau}(x)|
\le2M
\le
\frac{2M}{h(x+1)}h(v).
\tag{23}
\]

Therefore for some finite `C=C(m,x,sigma,T)`,

\[
|g_{m,\tau}(v)-g_{m,\tau}(x)|
\le C h(v)
\qquad(v\ge x,\ |\tau|\le T).
\tag{24}
\]

Using `(5)`, positivity of `beta`, `(19)`, and `(24)` proves the upper half of `(8)`. At `tau=0`, monotonicity makes the discrepancy have one sign and gives the exact identity

\[
\frac{Q_m}{m!}g_{m,0}(x)-\widetilde E_m(0)
=
\frac{Q_m g_{m,0}(x)}{m!}
\Lambda_{m,\sigma}(\beta).
\tag{25}
\]

The band supremum is at least this real-axis value, proving the lower half of `(8)`.

This is the same positive-measure mechanism isolated by AF-204, but no step uses `m=4`.

### 3. The Peano carrier converts the defect to saturated knot diameter

AF-202 identifies the normalized Peano carrier with the Dirichlet barycentric law

\[
V=\sum_{j=0}^m\Theta_j u_j,
\qquad
(\Theta_0,\ldots,\Theta_m)
\sim\operatorname{Dirichlet}(1,\ldots,1),
\tag{26}
\]

and proves, for every `0<r<D`,

\[
\beta([x+r,\infty))
\ge
\left(1-\frac rD\right)^m.
\tag{27}
\]

Because `g_{m,0}` is positive and decreasing,

\[
\Lambda_{m,\sigma}(\beta)
=
\int c_{m,\sigma,x}(v-x)\,d\beta(v).
\tag{28}
\]

Support in `[x,x+D]` immediately gives

\[
\Lambda_{m,\sigma}(\beta)
\le c_{m,\sigma,x}(D).
\tag{29}
\]

For any `0<theta<1`, `(27)` at `r=theta D` gives

\[
\Lambda_{m,\sigma}(\beta)
\ge
(1-\theta)^m
c_{m,\sigma,x}(\theta D).
\tag{30}
\]

The ratio in `(7)` has an exact probability-mixture form. Define

\[
w_k
:=
\frac{k^{m-1}e^{-k\sigma x}}
{\sum_{j\ge1}j^{m-1}e^{-j\sigma x}},
\qquad
\sum_{k\ge1}w_k=1.
\tag{31}
\]

Then

\[
c_{m,\sigma,x}(r)
=
\sum_{k\ge1}w_k(1-e^{-k\sigma r}).
\tag{32}
\]

Each summand is increasing and concave, so `c_{m,sigma,x}` is increasing and concave with `c(0)=0`. Consequently

\[
c(\theta D)\ge\theta c(D).
\tag{33}
\]

Substitution into `(30)` yields

\[
\Lambda_{m,\sigma}(\beta)
\ge
\theta(1-\theta)^m c(D).
\tag{34}
\]

The elementary maximum of `theta(1-theta)^m` occurs at

\[
\theta=\frac1{m+1},
\tag{35}
\]

with value

\[
\frac{m^m}{(m+1)^{m+1}}.
\tag{36}
\]

Together with `(29)`, this proves `(9)`. Notice that this improves the fixed choice `theta=1/2` used in AF-202 from an exponentially small `2^{-(m+1)}` comparison to a constant asymptotic to `1/(e(m+1))`.

### 4. Saturated diameter is equivalent to `min(D,1)`

From `(32)`, `c(r)` increases from zero toward one. Concavity gives, for `0<=D<=1`,

\[
c(1)D\le c(D)\le c'(0)D,
\tag{37}
\]

where

\[
c'(0)
=
\sigma
\frac{\sum_{k\ge1}k^m e^{-k\sigma x}}
{\sum_{k\ge1}k^{m-1}e^{-k\sigma x}}
>0.
\tag{38}
\]

For `D>=1`, monotonicity gives

\[
c(1)\le c(D)\le1.
\tag{39}
\]

Hence there are positive constants `a,b`, depending only on `m,x,sigma`, with

\[
a\min\{D,1\}
\le c(D)
\le b\min\{D,1\},
\tag{40}
\]

proving `(12)` and the equivalent sequence gate `(13)`.

In the genuinely local regime `D_n->0`, `(38)` gives

\[
c(D_n)\sim c'(0)D_n,
\tag{41}
\]

so `(11)` reduces to `Q_{m,n}D_n->0`. This recovers the quartic local form in AF-204. The saturated formulation is stronger as a general fixed-order statement because it does not require a separate lower bound on `Q_m` to force `D_n->0`.

## Consequence for the Arithmetic Fidelity frontier

AF-204 left two possible interpretations of its quartic gate: either `QD` was a special accident of the five-node fourth-order algebra, or the Euler observation was exposing a more general resource law. Equations `(8)`--`(13)` settle that distinction.

At every fixed cancellation order, three pieces must be declared together:

- `Q_m`: the surviving amplitude after lower moments have been compressed away;
- `D`: the physical source localization scale;
- `c_{m,sigma,x}(D)`: the amount of that physical displacement actually visible to the declared Euler half-plane observation.

The intrinsic product is not raw transport distance and not raw diameter. It is

\[
Q_m\,c_{m,\sigma,x}(D),
\]

which becomes `Q_mD` only below the observation's local resolution scale and saturates to order `Q_m` for macroscopic escape.

This is exactly the kind of distinction the Arithmetic Fidelity mandate asks for: a source property survives compression only after its amplitude is weighted by the sensitivity profile of the downstream observation. It also prevents an overgeneralization of AF-204. There is no all-order claim here that transfer by itself forces `D->0`; if a source family can make `Q_m->0`, macroscopic geometry may become invisible because the surviving response amplitude itself vanishes.

The next unresolved problem is therefore sharper. For growing cancellation order, moving half-plane edge, or growing bandwidth, determine whether the constants in `(8)` and the source factor in `(9)` remain controlled after the relevant complexity normalization. In particular, `(36)` shows that the crude Dirichlet localization loss is only order `1/m`, not exponential, but `g_{m,0}`, `c_{m,sigma,x}`, and the complex-band constant `C` also vary with `m`. A genuine growing-complexity theorem must track those dependencies rather than reusing the fixed-order equivalence formally.

## Prior art and novelty assessment

The structural ingredients are classical and are not claimed as new mathematics in isolation.

- Carl de Boor, **“Divided Differences,”** *Surveys in Approximation Theory* 1 (2005), 46--69, arXiv:`math/0502036`, gives the standard divided-difference, Peano-kernel, B-spline, and Genocchi--Hermite machinery used by AF-195/AF-199/AF-202.
- B. C. Carlson, **“B-splines, hypergeometric functions, and Dirichlet averages,”** *Journal of Approximation Theory* 67 (1991), 311--325, DOI `10.1016/0021-9045(91)90006-V`, is direct prior art for the B-spline/Dirichlet-average representation behind the barycentric carrier.
- Francesco Altomare and Michele Campiti, ***Korovkin-type Approximation Theory and Its Applications***, De Gruyter Studies in Mathematics 17 (1994), DOI `10.1515/9783110884586`, is broad prior art for convergence and testing of positive linear operators. Quantitative positive-operator error estimates and Peano-kernel remainder estimates are likewise established approximation-theory tools.

A targeted literature audit did not justify treating positive-measure testing, B-spline localization, exponential-mixture concavity, or all-order divided-difference representation as novel. The durable result here is the exact synthesis forced by the Arithmetic Fidelity Euler source class: the whole fixed complex band is calibrated by one real defect, that defect is uniformly equivalent to an observation-saturated knot diameter for every minimal-support fixed order, and the resulting exact transfer resource is `Q_m c_{m,sigma,x}(D)` or equivalently `Q_m min(D,1)`. No novelty claim is made beyond this line-specific derived bridge.

## Boundaries and falsification checks

- **Fixed order is essential.** The constants in `(8)`, `(9)`, and `(40)` depend on `m`; the finding does not assert a uniform growing-order theorem.
- **Fixed half-plane edge and finite band are essential.** Moving `sigma` toward zero or allowing `T` to grow can destroy the uniform bounds in `(20)`--`(24)`.
- **Minimal-support Peano geometry is essential for `(9)`.** The lower source comparison uses the Dirichlet barycentric law forced by `m+1` ordered knots. Arbitrary positive carriers or nonminimal moment-flat controls need not retain a fixed fraction of mass at the extreme-knot scale.
- **The anchor is one-sided.** All knots lie in `[x,infinity)`. Two-sided or moving-anchor source families require a separate defect geometry.
- **The sign correction in `(5)` is bookkeeping only.** Removing it changes the phase of the endpoint model for odd `m`, not the absolute transfer error.
- **No minimizer theorem follows.** The exact profile transfer gate does not prove projective compactness or transfer of the homogeneous `Q_m` optimizer to a scalar full-Euler minimizer. The accepted quartic clue therefore remains open in its optimizer-transfer component.
- **No rational-prime specificity follows.** These are matched generalized Euler-generator controls. The theorem identifies an observation-specific fidelity resource; it does not show that ordinary rational primes possess it uniquely and has no direct RH consequence.

A decisive way to falsify the stated all-order extension would be to produce, at fixed `m,x,sigma,T`, a minimal-support source for which the Peano identity `(5)`, the real-axis defect equality `(25)`, or the source comparison `(9)` fails. The first two reduce to classical divided-difference calculus and direct Euler differentiation; `(9)` reduces to the AF-202 Dirichlet tail law plus concavity of the explicit mixture `(32)`.