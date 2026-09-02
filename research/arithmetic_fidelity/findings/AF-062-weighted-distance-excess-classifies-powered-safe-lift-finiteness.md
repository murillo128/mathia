# AF-062 — Weighted distance-excess decay classifies powered safe-lift finiteness

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-BOUNDARY`

## Claim

Let `(X,d)` be a metric space, let `S\subseteq X` be nonempty, fix `m\in X`, and write

\[
\delta=d(m,S).
\tag{1}
\]

For `p>1`, define the AF-057 powered far-field defect

\[
\Delta_{p,S}(m)
=
\sup_{x\in X}
\left(d(x,S)^p-d(x,m)^p\right)
\in[0,+\infty],
\tag{2}
\]

and define the **positive first-order distance excess**

\[
e_{S,m}(x)
=
\bigl(d(x,S)-d(x,m)\bigr)_+.
\tag{3}
\]

Finally set

\[
W_{p,S}(m)
=
\sup_{x\in X}
\left(d(x,m)+\delta\right)^{p-1} e_{S,m}(x).
\tag{4}
\]

Then:

1. **Powered safe-lift finiteness is exactly equivalent to weighted first-order excess boundedness.** One has the two-sided estimate
   \[
   \boxed{
   2^{1-p}W_{p,S}(m)
   \le
   \Delta_{p,S}(m)
   \le
   p\,W_{p,S}(m).
   }
   \tag{5}
   \]
   Consequently
   \[
   \boxed{
   \Delta_{p,S}(m)<\infty
   \iff
   W_{p,S}(m)<\infty.
   }
   \tag{6}
   \]
   By AF-057, in the exact `\ell^p` product refinement this is also equivalent to existence of a finite vertical safe lift above the prescribed base point `m`.

2. **The critical power is controlled by the decay rate of positive distance excess at infinity.** Assume `\delta>0`. If for some `\rho\ge1` and `C<\infty`,
   \[
   e_{S,m}(x)
   \le
   C\left(d(x,m)+\delta\right)^{1-\rho}
   \qquad\forall x\in X,
   \tag{7}
   \]
   then
   \[
   \boxed{
   \Delta_{p,S}(m)<\infty
   \qquad\text{for every }1<p\le\rho.
   }
   \tag{8}
   \]
   Conversely, if there are `c>0` and points `x_n` with `d(x_n,m)\to\infty` such that
   \[
   e_{S,m}(x_n)
   \ge
   c\left(d(x_n,m)+\delta\right)^{1-\rho},
   \tag{9}
   \]
   then
   \[
   \boxed{
   \Delta_{p,S}(m)=+\infty
   \qquad\text{for every }p>\rho.
   }
   \tag{10}
   \]
   Thus a threshold such as the Euclidean `p=2` transition of AF-057/AF-059 or the `\ell^r` threshold of AF-061 is not fundamentally a statement about a preferred exponent. It is a statement about how fast the positive distance excess decays along the worst escape directions.

3. **A positive first-order asymptotic gap kills every nonlinear power.** If for some escaping sequence
   \[
   \liminf_{n\to\infty}
   \left(d(x_n,S)-d(x_n,m)\right)>0,
   \tag{11}
   \]
   then
   \[
   \boxed{
   \Delta_{p,S}(m)=+\infty
   \qquad\forall p>1.
   }
   \tag{12}
   \]
   The only nontrivial finite-power thresholds therefore occur along directions where the first-order excess tends to zero and a finer decay scale survives.

4. **Horofunctions isolate the first-order obstruction in proper metric spaces.** Suppose `X` is proper, `S` is compact, and `x_n` escapes every compact set. Along any subsequence for which
   \[
   h_n(z)
   =
   d(x_n,z)-d(x_n,m)
   \tag{13}
   \]
   converges locally uniformly to a horofunction `h`, one has
   \[
   \boxed{
   d(x_n,S)-d(x_n,m)
   \longrightarrow
   \inf_{s\in S}h(s).
   }
   \tag{14}
   \]
   Hence:
   - if `\inf_S h>0`, that boundary direction forces (12);
   - if `\inf_S h<0`, that direction contributes no positive excess for all sufficiently large `n`;
   - if `\inf_S h=0`, the horofunction records a first-order tie and the finite-power question is decided by the rate at which the positive excess approaches zero.

5. **AF-061's power-gap amplification is a corollary of the first-order criterion.** If for some `\rho\ge1`, `c>0`, and an escaping sequence
   \[
   d(x_n,S)^\rho-d(x_n,m)^\rho\ge c,
   \tag{15}
   \]
   then the triangle inequality and the mean-value theorem imply
   \[
   e_{S,m}(x_n)
   \ge
   \frac{c}{\rho\left(d(x_n,m)+\delta\right)^{\rho-1}}.
   \tag{16}
   \]
   Equation (10) therefore recovers AF-061's conclusion that every `p>\rho` has infinite powered defect.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{powered far-field fidelity is a weighted first-order distance-excess problem;}
\text{ the power threshold records an asymptotic decay rate, not an intrinsic preferred norm exponent.}
}
\tag{17}
\]

This separates two layers that AF-059--AF-061 had exposed only in examples: the horofunction boundary detects whether a first-order escape direction already destroys every nonlinear powered lift, while zero first-order gap leaves a genuinely quantitative second layer governed by the decay of the residual excess.

## Derivation

Put

\[
a=d(x,S),
\qquad
b=d(x,m).
\tag{18}
\]

The point-to-set triangle inequality gives

\[
a\le b+\delta.
\tag{19}
\]

If `a\le b`, then the contribution to (2) is nonpositive and `e_{S,m}(x)=0`. Thus only points with `a>b` matter for either supremum.

### Upper bound in (5)

For `a>b`, the mean-value theorem for `t\mapsto t^p` gives some `\xi\in(b,a)` with

\[
a^p-b^p
=p\xi^{p-1}(a-b).
\tag{20}
\]

Using `\xi\le a\le b+\delta`,

\[
a^p-b^p
\le
p(b+\delta)^{p-1}(a-b)
=
p(b+\delta)^{p-1}e_{S,m}(x).
\tag{21}
\]

Taking the supremum proves

\[
\Delta_{p,S}(m)\le pW_{p,S}(m).
\tag{22}
\]

### Lower bound in (5)

First note that evaluating (2) at `x=m` gives

\[
\Delta_{p,S}(m)\ge\delta^p.
\tag{23}
\]

Now again assume `a>b`.

If `b\ge\delta`, then

\[
b+\delta\le2b,
\tag{24}
\]

and (20) also gives

\[
a^p-b^p
\ge
p b^{p-1}(a-b).
\tag{25}
\]

Therefore

\[
(b+\delta)^{p-1}e_{S,m}(x)
\le
\frac{2^{p-1}}{p}(a^p-b^p)
\le
2^{p-1}\Delta_{p,S}(m).
\tag{26}
\]

If instead `b<\delta`, then by (19)

\[
e_{S,m}(x)=a-b\le\delta,
\tag{27}
\]

so

\[
(b+\delta)^{p-1}e_{S,m}(x)
\le
(2\delta)^{p-1}\delta
=
2^{p-1}\delta^p
\le
2^{p-1}\Delta_{p,S}(m).
\tag{28}
\]

Taking the supremum over `x` yields

\[
W_{p,S}(m)
\le
2^{p-1}\Delta_{p,S}(m),
\tag{29}
\]

which is the left-hand inequality in (5).

The constants in (5) are only uniform comparison constants; no optimality claim is made for them. The exact content needed by the line is the equivalence of finiteness and the explicit weighted quantity that controls it.

### Polynomial decay gives the threshold test

Assume `\delta>0`. Under (7), for `1<p\le\rho`,

\[
\begin{aligned}
W_{p,S}(m)
&\le
C\sup_x
\left(d(x,m)+\delta\right)^{p-\rho}\\
&\le
C\delta^{p-\rho}<\infty.
\end{aligned}
\tag{30}
\]

Equation (6) gives (8).

Under (9), along the declared sequence,

\[
\left(d(x_n,m)+\delta\right)^{p-1}e_{S,m}(x_n)
\ge
c\left(d(x_n,m)+\delta\right)^{p-\rho}.
\tag{31}
\]

For `p>\rho` the right side tends to `+\infty`, so `W_{p,S}(m)=+\infty`; (6) gives (10).

If `\delta=0`, then `m\in\overline S` and (19) reduces to `d(x,S)\le d(x,m)` for every `x`, hence

\[
e_{S,m}\equiv0,
\qquad
\Delta_{p,S}(m)=0
\qquad\forall p\ge1.
\tag{32}
\]

Thus excluding `\delta=0` from the rate statement loses no nontrivial threshold case.

### Horofunction reduction of the first-order excess

For (14), observe that for every `n`,

\[
\begin{aligned}
d(x_n,S)-d(x_n,m)
&=
\inf_{s\in S}
\left(d(x_n,s)-d(x_n,m)\right)\\
&=
\inf_{s\in S}h_n(s).
\end{aligned}
\tag{33}
\]

Since `S` is compact and `h_n\to h` uniformly on `S`,

\[
\inf_{s\in S}h_n(s)
\longrightarrow
\inf_{s\in S}h(s),
\tag{34}
\]

proving (14).

Normalized distance functions such as (13), their closure, and the resulting horofunction/metric boundary are classical. Properness supplies the compactness needed to pass to locally uniformly convergent subsequences of normalized `1`-Lipschitz distance functions. The new content claimed here is not the horofunction compactification, but the exact bridge from its sign and convergence rate to AF-057's powered safe-lift finiteness observable.

### AF-061's persistent power gap implies the critical excess rate

Suppose (15) holds. For each `n`, put

\[
a_n=d(x_n,S),
\qquad
b_n=d(x_n,m).
\]

The left side of (15) is positive, so `a_n>b_n`. By the mean-value theorem,

\[
a_n^\rho-b_n^\rho
\le
\rho a_n^{\rho-1}(a_n-b_n).
\tag{35}
\]

Using `a_n\le b_n+\delta`,

\[
c
\le
\rho(b_n+\delta)^{\rho-1}e_{S,m}(x_n),
\tag{36}
\]

which is exactly (16). Equation (10) now gives AF-061's supercritical divergence.

## Exact controls

### Bounded sources have no far-field powered obstruction

If `X` has finite diameter, then both `d(x,m)+\delta` and `e_{S,m}(x)` are uniformly bounded. Hence

\[
W_{p,S}(m)<\infty
\]

for every finite `p`, and therefore every `\Delta_{p,S}(m)` is finite. This agrees with AF-057 and AF-060: the phase transitions there require an unbounded source and can be invisible on every compact truncation.

### Exterior Euclidean points are first-order failures

Let `S\subset\mathbb R^d` be compact, let `K=\operatorname{conv}(S)`, and let `m\notin K`. Strict separation gives a unit vector `u` and `a_0>0` such that

\[
\langle u,s-m\rangle\le-a_0
\qquad\forall s\in S.
\tag{37}
\]

Along `x_t=m+t u`, the normalized distance functions converge to the Euclidean Busemann function

\[
h(z)=-\langle u,z-m\rangle,
\tag{38}
\]

so

\[
\inf_{s\in S}h(s)\ge a_0>0.
\tag{39}
\]

Therefore every `p>1` diverges by (12). This recovers the exterior branch of AF-059 without expanding powered distances: the obstruction is already visible at first order on the metric boundary.

### Missing Euclidean hull-boundary points are zero-horogap failures

Let `m\in\partial K\setminus S` in the setting of AF-059 and choose an outward supporting unit vector `u`. Along `x_t=m+t u`, the limiting function again has form (38), but now

\[
\inf_{s\in S}h(s)=0.
\tag{40}
\]

The horofunction test alone is therefore silent. AF-059's fixed positive squared-distance gap yields instead

\[
e_{S,m}(x_t)\asymp t^{-1},
\tag{41}
\]

which corresponds to `\rho=2`: powers at or below `2` remain finite at this obstruction, while every `p>2` diverges. The critical value comes from the residual decay after first-order cancellation.

### The `\ell^r` two-point model has zero horogap and rate `t^{1-r}`

For AF-061's target

\[
S_a=\{(-a,0),(a,0)\}
\]

in `\ell^r`, inspect `x_t=(0,t)`. Then

\[
e_{S_a,0}(x_t)
=
(t^r+a^r)^{1/r}-t
\sim
\frac{a^r}{r}t^{1-r}.
\tag{42}
\]

The first-order horofunction gap is zero, while the positive excess has exactly the polynomial rate `\rho=r`. Equations (8)--(10) recover AF-061's sharp threshold `p=r`.

### Membership in the closed target is the trivial zero-excess case

If `m\in\overline S`, then `\delta=0`, so (32) gives zero powered defect for every `p`. This is the fixed-base form of AF-054/AF-060's warning that transported target points make unconstrained global existence vacuous. The present theorem is informative only when the retained provenance forces a base point outside the closed target.

## Prior art and novelty assessment

The ingredients of this finding are classical, and no novelty is claimed for point-to-set distance estimates, the mean-value theorem, Busemann functions, or horofunction compactification.

- Marc A. Rieffel, **“Group C*-algebras as compact quantum metric spaces,”** *Documenta Mathematica* 7 (2002), 605–651, DOI `10.4171/DM/133`. Role: established metric-compactification framework built from normalized distance functions and closely related to geodesic rays; direct prior-art boundary for treating asymptotic normalized distance profiles as new objects.
- Cormac Walsh, **“The horofunction boundary of finite-dimensional normed spaces,”** *Mathematical Proceedings of the Cambridge Philosophical Society* 142(3) (2007), 497–507, DOI `10.1017/S0305004107000096`. Role: direct finite-dimensional normed-space horofunction/Busemann boundary prior art, especially relevant to the `\ell^r` and renorming examples in AF-057--AF-061.
- Dmitri Burago, Yuri Burago, and Sergei Ivanov, ***A Course in Metric Geometry***, Graduate Studies in Mathematics 33, American Mathematical Society (2001). Role: standard metric-space background for distance-to-set functions, proper metric spaces, compactness arguments, and Busemann-type asymptotic geometry already neighboring AF-054/AF-057.

A targeted literature search located substantial established theory for metric/horofunction compactifications and normed-space Busemann boundaries. It did not identify the exact weighted quantity (4) or the two-sided estimate (5) as a standard named result, but that absence is **not** used as a novelty claim. The derivation is elementary once AF-057's powered defect is isolated. The durable contribution is an Arithmetic Fidelity classification: it converts the example-specific critical exponents of AF-057, AF-059, and AF-061 into one category-independent criterion and identifies precisely what classical horofunction data can and cannot decide.

## Boundaries and failure modes

- The theorem classifies finiteness of AF-057's powered defect. It does not make a lift natural, canonical, minimal, or admissible in an arithmetic category.
- By AF-060, a meaningful existence statement must retain the base/fiber/provenance constraint. Global safe-envelope nonemptiness remains trivial because transported target points are always safe.
- The uniform constants in (5) are not claimed optimal.
- The polynomial tests (7)--(10) are sufficient one-sided criteria. Different escape sequences may have different rates, oscillatory behavior, or logarithmic corrections; there need not be one globally sharp critical exponent describable by a single `\rho`.
- The horofunction statement requires compactness of `S` for the direct passage of infima in (14), and it is stated along locally uniformly convergent normalized-distance subsequences. It does not claim that every asymptotic question is visible from a first-order horofunction.
- A zero horofunction gap is deliberately inconclusive. It means only that first-order asymptotic geometry has tied; the decay rate of the residual positive excess must then be audited.
- Nothing here distinguishes rational primes or implies RH. This is an abstract structural theorem fulfilling the line mandate before arithmetic specialization.

## Consequence for the Arithmetic Fidelity frontier

AF-057 exposed a `p=2` phase transition in one Euclidean two-point model. AF-059 showed that first- and second-order far-field geometry determine different parts of a Euclidean compact-target phase diagram. AF-061 then moved the threshold from `2` to the source exponent `r`, proving that the exponent is representation-dependent.

The present theorem removes the remaining example dependence. The fundamental object is the positive excess

\[
e_{S,m}(x)=\bigl(d(x,S)-d(x,m)\bigr)_+,
\]

and the powered observable is finite exactly when that excess decays quickly enough after weighting by distance to the power `p-1`.

This suggests a sharper next frontier than varying more norms. For a proposed compression/refinement with retained provenance, identify its asymptotic boundary directions first. Directions with positive limiting excess are immediate no-go witnesses for every nonlinear power. Directions with negative limiting excess are harmless for this observable. Only **zero-gap boundary directions** carry unresolved structure, and there the research question is to determine which intrinsic higher-order or rate data survive and whether those rates are stable under the admissible equivalences of the mathematical category.
