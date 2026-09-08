# AF-209 — Positive-width Euler bands are injective and BV complexity restores signed coercivity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-BRIDGE`, `QUANTITATIVE-FIDELITY`, `SOURCE-COMPLEXITY-GATE`, `NO-NOVELTY-CLAIM`

## Claim

AF-208 shows that compact support and bounded total variation of a signed Peano carrier do not by themselves give a uniform lower recovery modulus for a fixed Euler band: increasingly fine oscillations form an approximate null sequence. The obstruction is instability rather than exact non-identifiability.

Fix

\[
m\ge1,\qquad x>0,\qquad \sigma>0,\qquad 0<T<\infty,\qquad L>x,
\]

and write, for `s=\sigma+i\tau`,

\[
g_{m,\tau}(t)
:=(-1)^mF_{\sigma+i\tau}^{(m)}(t)
=s^m\sum_{k\ge1}k^{m-1}e^{-kst},
\]

\[
\phi_\tau(t):=g_{m,\tau}(t)-g_{m,\tau}(x),
\qquad
h(t):=g_{m,0}(x)-g_{m,0}(t).
\]

For a finite signed measure `\eta` on `[x,L]` define

\[
(\mathcal A_T\eta)(\tau)
:=\int_{[x,L]}\phi_\tau(t)\,d\eta(t),
\qquad |\tau|\le T.
\]

Then:

1. **A genuine vertical interval is exactly injective modulo the invisible anchor atom.**
   \[
   \boxed{
   \ker \mathcal A_T=\operatorname{span}\{\delta_x\}
   \quad\text{on }M([x,L]).
   }
   \]
   Consequently `\mathcal A_T` is injective on absolutely continuous signed measures `b(t)dt`, hence on `L^1([x,L])` densities.

2. **Normalized precompact source complexity turns that exact injectivity into a uniform lower modulus.** Put
   \[
   V_h(b):=\int_x^L h(t)|b(t)|\,dt,
   \qquad
   D_T(b):=\|\mathcal A_T(b(t)dt)\|_{C([-T,T])}.
   \]
   Let `\mathcal C\subset L^1([x,L])` be a cone such that
   \[
   \mathcal S:=\{b\in\mathcal C:V_h(b)=1\}
   \]
   has relatively compact closure in `L^1`. Then there is a constant `c_\mathcal C>0` such that
   \[
   \boxed{
   D_T(b)\ge c_\mathcal C V_h(b)
   \qquad(b\in\mathcal C).
   }
   \]

3. **A concrete bounded-variation budget supplies the required compactness.** For every finite `M>0`, let
   \[
   \mathcal C_M
   :=\{b\in BV([x,L]):\operatorname{Var}(b)\le M V_h(b)\}.
   \]
   Then there is
   \[
   c=c(m,x,\sigma,T,L,M)>0
   \]
   with
   \[
   \boxed{
   D_T(b)\ge cV_h(b)
   \qquad(b\in\mathcal C_M).
   }
   \]

Thus AF-208's compact-operator obstruction has a sharp conceptual repair: **exact injectivity is already present in every positive-width Euler band, while quantitative coercivity returns once the normalized signed source class is genuinely precompact in a topology on which the observation map is continuous.** A homogeneous BV/oscillation budget is one explicit realization of that source-complexity gate.

The positive-width assumption is essential. At `T=0` the observation is one scalar functional and has an infinite-dimensional smooth kernel; no analogous injectivity statement holds.

## Derivation

### 1. The anchored Euler kernel reduces to a dilation-Laplace transform

Let `\eta\in M([x,L])` and put

\[
c:=\eta([x,L]),
\qquad
q:=\eta-c\delta_x.
\]

Then

\[
(\mathcal A_T\eta)(\tau)
=\int g_{m,\tau}(t)\,dq(t).
\]

For `\Re s>0` define the Laplace transform

\[
R_q(s):=\int_{[x,L]}e^{-st}\,dq(t).
\]

Because `x>0`, the Euler series is absolutely and locally uniformly convergent on the right half-plane, and therefore

\[
H_q(s)
:=s^{-m}\int g_{m,s}(t)\,dq(t)
=\sum_{k\ge1}k^{m-1}R_q(ks)
\tag{1}
\]

is holomorphic for `\Re s>0`. Here `g_{m,s}(t)` denotes the same analytic expression with complex parameter `s`.

If `\mathcal A_T\eta=0`, equation `(1)` vanishes for every point of the nontrivial segment

\[
\{\sigma+i\tau:|\tau|\le T\}.
\]

The identity theorem therefore gives

\[
H_q(s)=0
\qquad(\Re s>0).
\tag{2}
\]

This is where a continuum band differs qualitatively from one or finitely many sampled frequencies.

### 2. Möbius inversion recovers the underlying Laplace transform

The arithmetic coefficient

\[
a(k)=k^{m-1}
\]

is completely multiplicative. Its Dirichlet inverse is

\[
a^{-1}(n)=\mu(n)n^{m-1},
\]

where `\mu` is the Möbius function. Hence the dilation sum `(1)` has the formal inverse

\[
R_q(s)
=\sum_{n\ge1}\mu(n)n^{m-1}H_q(ns).
\tag{3}
\]

For the present compactly supported measure the inversion is absolutely justified. On every half-plane `\Re s\ge\delta>0`,

\[
|R_q(js)|\le \|q\|_{TV}e^{-jx\delta},
\]

and therefore the double series arising from substitution of `(1)` into `(3)` is dominated by

\[
\|q\|_{TV}
\sum_{n,k\ge1}(nk)^{m-1}e^{-nkx\delta}
=
\|q\|_{TV}
\sum_{j\ge1}d(j)j^{m-1}e^{-jx\delta}<\infty.
\]

Rearrangement gives

\[
\begin{aligned}
\sum_{n\ge1}\mu(n)n^{m-1}H_q(ns)
&=
\sum_{j\ge1}j^{m-1}R_q(js)
\sum_{n\mid j}\mu(n)\\
&=R_q(s).
\end{aligned}
\]

Combining with `(2)` yields `R_q\equiv0`. Uniqueness of the Laplace transform for compactly supported finite signed measures gives `q=0`, hence

\[
\eta=c\delta_x.
\]

Conversely `\delta_x` is visibly annihilated by every anchored kernel `\phi_\tau`. This proves

\[
\ker\mathcal A_T=\operatorname{span}\{\delta_x\}.
\]

If `\eta=b(t)dt` is absolutely continuous, equality with `c\delta_x` forces `c=0` and `b=0` almost everywhere. Thus the positive-width Euler band separates every two distinct `L^1` signed densities on the fixed interval, even though AF-208 proves that it does not separate them with a uniform total-variation condition number.

### 3. Precompact normalized source classes convert injectivity into coercivity

The map

\[
\mathcal A_T:L^1([x,L])\to C([-T,T])
\]

is bounded because `\phi` is continuous on the compact product `[-T,T]\times[x,L]`. Likewise `V_h` is continuous in the `L^1` norm because `h` is bounded.

Let `\mathcal S` be the normalized slice of a cone `\mathcal C` from the claim, and let `K=\overline{\mathcal S}^{L^1}`. Relative compactness makes `K` compact. Continuity of `V_h` gives

\[
V_h(b)=1
\qquad(b\in K),
\]

so `0\notin K`. Exact injectivity on `L^1` then gives

\[
D_T(b)>0
\qquad(b\in K).
\]

Continuity of `D_T` on compact `K` produces a strictly positive minimum

\[
c_\mathcal C:=\min_{b\in K}D_T(b)>0.
\]

Rescaling any nonzero element of the cone by `V_h(b)` proves the lower estimate. This is the stable-inversion step missing from AF-208: injectivity alone does not control the inverse, but injectivity on a compact normalized source set does.

### 4. A homogeneous BV budget compactifies the normalized carrier class

It remains to verify the concrete corollary. Normalize `b\in\mathcal C_M` by

\[
V_h(b)=1.
\]

Set

\[
H:=\int_x^L h(t)\,dt>0.
\]

The weighted average implies that some Lebesgue point `t_0\in(x,L)` satisfies, up to an arbitrarily small error,

\[
|b(t_0)|\le H^{-1}.
\]

For a BV representative,

\[
|b(t)|\le |b(t_0)|+\operatorname{Var}(b)
\]

for almost every `t`, so the normalized class has the uniform bound

\[
\|b\|_{L^1}
\le
(L-x)(H^{-1}+M).
\tag{4}
\]

Together with

\[
\operatorname{Var}(b)\le M,
\]

standard BV compactness on a bounded interval makes the normalized class relatively compact in `L^1`. Total variation is lower semicontinuous under `L^1` convergence, while `V_h` is continuous, so its closure remains inside the same normalized BV bound. The previous step therefore gives the claimed constant `c(m,x,\sigma,T,L,M)>0`.

This condition is homogeneous: multiplying `b` by a scalar multiplies `\operatorname{Var}(b)`, `V_h(b)`, and `D_T(b)` by the same absolute factor. It constrains complexity rather than amplitude.

## Exact controls and boundaries

### The AF-208 null sequence exits every fixed BV-complexity cone

AF-208 constructs smooth signed densities on one fixed compact interval whose Euler-band discrepancy tends to zero while `V_h` stays bounded away from zero. Their carrier scale becomes increasingly oscillatory; in particular the unit-mass anchor bump is squeezed into a width tending to zero and the remote component contains frequency tending to infinity. The BV variation therefore diverges while `V_h` remains order one. The sequence is excluded by every fixed ratio bound

\[
\operatorname{Var}(b)\le M V_h(b).
\]

The new theorem therefore does not contradict AF-208; it identifies precisely one missing compactness resource that its counterexample spends.

### A single real Euler observable is not enough

If `T=0`, then

\[
D_0(b)=\left|\int_x^L\phi_0(t)b(t)dt\right|
\]

is one linear functional. Choose two nonzero smooth bumps with disjoint support in `(x,L)` and scale one against the other so that their `\phi_0` integrals cancel. This gives a nonzero smooth density with `D_0=0` and finite `\operatorname{Var}(b)/V_h(b)`. Hence some positive-width set of frequencies, or more generally an observation set with an accumulation point in the analytic domain, is genuinely required for signed exact recovery.

### Finite frequency sampling is also insufficient for unrestricted smooth sources

Any finite list of frequencies gives only finitely many linear constraints on the infinite-dimensional space `C_c^\infty((x,L))`, so it has a nontrivial kernel. The analytic-continuation argument applies to a continuum band, not to a finite numerical sampling of that band. Quantitative discretization would need an additional finite-dimensional or approximation theorem.

### BV is sufficient, not claimed minimal

The proof uses only relative `L^1` compactness of the normalized source class. BV is one natural explicit condition that provides it. Finite-dimensional parametrizations, stronger Sobolev budgets, shape constraints, or other compact embeddings can do the same. No claim is made that the BV ratio is the weakest possible arithmetic source condition.

## Source-realizable Peano corollary

AF-207 proves that every smooth compactly supported signed density `b\in C_c^\infty((x,L))` with

\[
\int_x^L b(t)dt=1
\]

is the normalized order-`m` Peano carrier of a pair of moment-matched probability measures obtained from the Jordan decomposition of `(-1)^m b^{(m)}(t)dt`.

Therefore the BV-coercive subclass is not merely an abstract family of test densities. Every such smooth mass-one carrier satisfying

\[
\operatorname{Var}(b)\le M V_h(b)
\]

is source-realizable in the same exact sense as AF-207/AF-208, and its fixed Euler band obeys the uniform lower recovery estimate above.

## Arithmetic Fidelity consequence

AF-207 and AF-208 separated positivity from signed recovery and then showed that localization alone does not cure the signed instability. AF-209 separates two further notions that must not be conflated:

\[
\boxed{
\text{exact discriminator survival}
\quad\neq\quad
\text{stable discriminator survival}.
}
\]

On compactly supported signed densities, a positive-width Euler band already preserves the source exactly. The apparent information loss in AF-208 is instead an arbitrarily bad inverse condition number along high-complexity directions. Restricting the normalized source to a precompact reservoir turns the same observation family into a uniformly faithful one.

For eventual prime applications, this gives a more precise audit template. When an analytic compression appears to forget arithmetic structure, first determine its exact kernel. If the arithmetic discriminator is not in that kernel, the next question is not whether more symbolic information is needed but whether the admissible arithmetic source class has enough compactness/regularity to stay away from approximate null directions. Conversely, a claim based on exact injectivity alone is still insufficient for quantitative control.

## Prior art and novelty assessment

The ingredients are classical, and no novelty is claimed for them individually.

- D. V. Widder, **“An Inversion of the Lambert Transform,”** *Mathematics Magazine* 23 (1950), 171–182, DOI `10.2307/3029825`, is classical inversion prior art for Lambert-type transforms.
- R. R. Goldberg, **“Inversions of Generalized Lambert Transforms,”** *Duke Mathematical Journal* 25 (1958), 459–476, DOI `10.1215/S0012-7094-58-02540-7`, gives broader generalized-Lambert inversion theory.
- H. M. Srivastava, J. Maan, and E. R. Negrín, **“A unified presentation of the Lambert and the Widder–Lambert transforms over Lebesgue spaces and over the space of distributions of compact support on R+,”** *RACSAM* 120 (2026), article 68, DOI `10.1007/s13398-026-01862-0`, is recent prior art extending Lambert/Widder-Lambert inversion and mapping theory to Lebesgue spaces and compactly supported distributions.
- Classical Möbius inversion supplies the explicit inverse for the dilation coefficients `k^{m-1}`; the exponential support gap `x>0` supplies the absolute convergence needed for rearrangement here.
- D. V. Widder, *The Laplace Transform*, Princeton University Press (1941), is standard background for uniqueness of Laplace transforms.
- Standard BV compactness and lower-semicontinuity results, for example in L. Ambrosio, N. Fusco, and D. Pallara, *Functions of Bounded Variation and Free Discontinuity Problems*, Oxford University Press (2000), supply the compactness step.

The literature search found substantial inversion theory for Lambert and generalized Lambert transforms, including compactly supported distributions, so the injectivity mechanism should be treated as a classical bridge rather than a novelty claim. The durable Mathia-specific result is the placement of that inversion fact against AF-208's compact-operator obstruction: **the fixed Euler band can be exactly faithful and nevertheless unstable, and an explicit homogeneous source-complexity compactness condition restores a uniform arithmetic-fidelity modulus without changing the observation family.**

## Research disposition

The signed Euler branch should no longer treat exact injectivity as the missing resource on fixed compact support. For every genuine vertical interval it is already available by analytic continuation plus Möbius/Laplace inversion.

The live question is now sharper: determine which source-complexity class is mathematically natural for the arithmetic carriers supplied by the other Mathia lines, and whether its normalized profiles are precompact in a topology strong enough for the desired discriminator norm. BV provides a clean existence proof, but the eventual arithmetic value depends on deriving such a complexity bound intrinsically rather than imposing it after the fact.