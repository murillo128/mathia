# AF-113 — Operator-norm blow-up needs relative-scale tightness

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `SCALE-ADAPTED-FIDELITY`, `RELATIVE-SCALE-TIGHTNESS`, `MULTISCALE-ESCAPE-OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

Let `H` be a complex separable Hilbert space, let

\[
1\le p<\infty,
\]

and let `(A_i)` be a net of nonzero positive operators in `\mathcal S_p(H)` such that

\[
\delta_i:=\|A_i\|\longrightarrow0,
\qquad
M_i:=\|A_i\|_p^p>0.
\tag{1}
\]

No lower bound on `M_i` is needed below because the spectral profile will be normalized by its total `p`-mass. AF-112 showed that every unscaled continuous critical-order probe collapses to the single scalar `M_i`. The natural first repair is to retain the shrinking operator scale `\delta_i` and inspect the spectrum relative to it.

Let `(\lambda_{ij})_j` be the positive eigenvalues of `A_i`, repeated with multiplicity. Since `A_i` is positive compact and nonzero, `\delta_i` is its largest eigenvalue. Define the probability measure

\[
\nu_i
:=
\frac1{M_i}
\sum_j \lambda_{ij}^p\,
\delta_{\lambda_{ij}/\delta_i}
\qquad\text{on }(0,1]\subset[0,1].
\tag{2}
\]

This is the **operator-norm blow-up profile** of the critical `p`-mass.

### 1. The blow-up profile is exactly the retained scale-adapted critical trace data

For every bounded continuous `\varphi:[0,1]\to\mathbb C`, functional calculus gives

\[
\boxed{
\frac{1}{M_i}
\operatorname{Tr}\!\left(
A_i^p\,\varphi(A_i/\delta_i)
\right)
=
\int_{[0,1]}\varphi(u)\,d\nu_i(u).
}
\tag{3}
\]

Thus the complete family of normalized observables

\[
\varphi
\longmapsto
M_i^{-1}\operatorname{Tr}\!\left(A_i^p\varphi(A_i/\delta_i)\right)
\tag{4}
\]

contains exactly the same information as `\nu_i`. In particular:

\[
\boxed{
\nu_i\Rightarrow\nu
\quad\Longleftrightarrow\quad
\frac{1}{M_i}\operatorname{Tr}\!\left(
A_i^p\varphi(A_i/\delta_i)
\right)
\to
\int\varphi\,d\nu
\text{ for every }\varphi\in C([0,1]).
}
\tag{5}
\]

Because `[0,1]` is compact, every net `(\nu_i)` has a weakly convergent subnet. Therefore adding the single scale `\delta_i` repairs AF-112's total collapse only up to a **relative spectral profile**: a cluster measure on `[0,1]` records how the critical `p`-mass is distributed among eigenvalues comparable with the largest one.

### 2. AF-112 is the quotient obtained by forgetting the relative coordinate

Let `f(t)=Lt^p+o(t^p)` as `t\downarrow0`. Writing

\[
f(t)=t^p h(t),
\qquad h(t)\to L,
\tag{6}
\]

one has

\[
\frac{\operatorname{Tr}(f(A_i))}{M_i}
=
\int h(\delta_i u)\,d\nu_i(u)
\longrightarrow L,
\tag{7}
\]

uniformly over the entire probability profile because `0\le\delta_i u\le\delta_i\to0`.

Hence every fixed unscaled critical observable factors through the forgetful map

\[
\nu_i\longmapsto\nu_i([0,1])=1.
\tag{8}
\]

The blow-up variable `u=\lambda/\delta_i` is exactly the information discarded in AF-112. This makes the repair semantics precise: the scale-adapted family does not manufacture a new invariant; it retains the relative coordinate that fixed tests force to zero.

### 3. A canonical maximum scale does not prevent a second collapse

The scale `\delta_i=\|A_i\|` is intrinsic to the operator, but that alone does **not** imply that it captures a non-negligible fraction of the critical mass. Define the logarithmic relative-scale measure

\[
\eta_i
:=
(-\log)_\#\nu_i
\qquad\text{on }[0,\infty),
\tag{9}
\]

where `u\mapsto-\log u`. Then `(\eta_i)` is tight exactly when

\[
\boxed{
\forall\varepsilon>0\ \exists c\in(0,1):
\quad
\nu_i([c,1])\ge1-\varepsilon
\quad\text{eventually}.
}
\tag{10}
\]

In spectral variables this is

\[
\boxed{
\forall\varepsilon>0\ \exists c\in(0,1):
\quad
\frac{
\sum_{\lambda_{ij}\ge c\delta_i}\lambda_{ij}^p
}{M_i}
\ge1-\varepsilon
\quad\text{eventually}.
}
\tag{11}
\]

Equation (11) is an exact **relative-scale tightness** condition. It says that almost all critical `p`-mass eventually lies within a fixed multiplicative factor of the chosen blow-up scale. Under (11), no weak cluster point of `(\nu_i)` can put mass at `0`; equivalently, no positive fraction of the normalized critical mass escapes to logarithmic scale `+\infty`.

If (11) fails, the operator-norm blow-up can itself lose information by sending a positive amount of `p`-mass to `u=0`, representing eigenvalues that are `o(\delta_i)` along a subnet. A single intrinsic scale therefore does not solve the cross-scale problem unless a no-escape theorem accompanies it.

### 4. Full subscale collapse has an exact tail criterion

The strongest failure is

\[
\nu_i\Rightarrow\delta_0.
\tag{12}
\]

This occurs if and only if for every fixed `c\in(0,1)`,

\[
\boxed{
\frac{
\sum_{\lambda_{ij}\ge c\delta_i}\lambda_{ij}^p
}{M_i}
\longrightarrow0.
}
\tag{13}
\]

Thus the complete critical mass may survive in `\mathcal S_p` while every fixed positive relative scale contains asymptotically none of it. In that regime the first blow-up has merely moved the collapse point from the absolute scale `0` to the relative boundary `u=0`.

Equation (13) is a decisive audit test. A proposed operator-norm rescaling cannot claim microscopic spectral fidelity merely because the rescaled spectra live in `[0,1]`; it must show that the relevant mass does not concentrate at the newly created boundary point.

### 5. An explicit spike-plus-cloud family defeats the maximum-scale repair

Fix `p\ge1`. On a Hilbert space with an orthonormal basis, let

\[
\delta_n=\frac1n,
\qquad
\beta_n=\frac1{n^2},
\qquad
N_n=\lfloor n^{2p}\rfloor,
\tag{14}
\]

and let `A_n` be a finite-rank positive diagonal operator with one eigenvalue `\delta_n` and `N_n` eigenvalues equal to `\beta_n`.

Then

\[
\|A_n\|=\delta_n\to0,
\tag{15}
\]

while

\[
M_n
=\delta_n^p+N_n\beta_n^p
=n^{-p}+\lfloor n^{2p}\rfloor n^{-2p}
\longrightarrow1.
\tag{16}
\]

The canonical maximum eigenvalue therefore carries vanishing normalized `p`-mass:

\[
\frac{\delta_n^p}{M_n}\longrightarrow0,
\tag{17}
\]

whereas essentially all mass lies at relative scale

\[
\frac{\beta_n}{\delta_n}=\frac1n\longrightarrow0.
\tag{18}
\]

Consequently

\[
\boxed{
\nu_n
=
\frac{\delta_n^p}{M_n}\,\delta_1
+
\frac{N_n\beta_n^p}{M_n}\,\delta_{1/n}
\Rightarrow\delta_0.
}
\tag{19}
\]

This is a matched control against the tempting principle that “rescale by the operator norm” automatically restores spectral shape. The scale is canonical and exact, yet asymptotically it follows a negligible spike while the order-one resource cloud lives one level lower.

By contrast, for the single-scale family

\[
B_n=n^{-1/p}Q_n
\tag{20}
\]

from AF-112, every nonzero eigenvalue equals `\|B_n\|`, so

\[
\nu_n=\delta_1
\tag{21}
\]

exactly. The difference between (19) and (21) is not whether a canonical scale exists; both have one. It is whether the scale is **coherent with the mass whose fidelity is being studied**.

## Derivation

Since `A_i\ge0` and `A_i\in\mathcal S_p`, the positive operator `A_i^p` is trace class and

\[
\operatorname{Tr}(A_i^p)=M_i.
\tag{22}
\]

The operator `\varphi(A_i/\delta_i)` is bounded with norm at most `\|\varphi\|_\infty`, commutes with `A_i`, and has eigenvalues `\varphi(\lambda_{ij}/\delta_i)` on the nonzero spectral subspace. Therefore

\[
\operatorname{Tr}\!\left(A_i^p\varphi(A_i/\delta_i)\right)
=
\sum_j\lambda_{ij}^p
\varphi(\lambda_{ij}/\delta_i),
\tag{23}
\]

which proves (3).

The equivalence (5) is exactly the bounded-continuous-test characterization of weak convergence of finite Borel measures on the compact metric space `[0,1]`. Equality of the whole family (4) at a fixed stage likewise determines `\nu_i` uniquely by the Riesz representation theorem.

For (7), continuity of `h` at zero gives

\[
\sup_{0\le u\le1}|h(\delta_i u)-L|
\longrightarrow0.
\tag{24}
\]

Integrating against the probability measure `\nu_i` proves the claim independently of the shape of `\nu_i`.

For (10), apply the definition of tightness to `\eta_i` on `[0,\infty)`. The compact interval `[0,R]` pulls back under `u=e^{-r}` to `[e^{-R},1]`, so tightness is precisely eventual concentration of normalized mass on `[c,1]` for some `c=e^{-R}>0` at each error tolerance.

To prove (13) implies (12), let `\varphi\in C([0,1])` and `\varepsilon>0`. Choose `c>0` so that

\[
|\varphi(u)-\varphi(0)|<\varepsilon
\qquad(0\le u<c).
\tag{25}
\]

Then

\[
\left|\int\varphi\,d\nu_i-\varphi(0)\right|
\le
\varepsilon
+2\|\varphi\|_\infty\nu_i([c,1]),
\tag{26}
\]

which tends to at most `\varepsilon`; letting `\varepsilon\downarrow0` gives weak convergence to `\delta_0`. Conversely, if `\nu_i\Rightarrow\delta_0`, then for every fixed `c>0`, the closed set `[c,1]` has `\delta_0`-mass zero, so Portmanteau gives

\[
\limsup_i\nu_i([c,1])=0,
\tag{27}
\]

which is (13).

The spike-plus-cloud calculation (14)--(19) is immediate from the spectral definition (2). It also shows that failure of relative-scale tightness is compatible with `M_n\to1`; the second collapse is not caused by loss of total Schatten resource.

## Exact controls and failure modes

### The blow-up scale is part of the retained structure

AF-112 used only the original operators and fixed functions of their absolute spectrum. AF-113 adds the stage-dependent scalar `\delta_i` before applying the downstream observable. That is a genuine lift. In an application the scale must therefore be independently forced by the source construction; selecting it after inspecting the desired spectral profile would encode the recovery mechanism by hand.

The operator norm is canonical for an abstract positive compact operator, but an RH-oriented construction still has to justify that operator norm is the mathematically relevant scale rather than merely an available one.

### Compactness of `[0,1]` is not the same as no escape

The measures `\nu_i` are automatically weakly precompact because their ambient interval is compact. This does not mean their microscopic information is retained: mass arriving at the boundary point `0` represents spectral structure escaping to scales smaller than every fixed fraction of `\delta_i`.

Thus ordinary weak compactness after normalization can hide a **boundary escape**. The correct no-escape condition is tightness after the logarithmic coordinate removes that artificial compactification point, namely (10)--(11).

### Relative-scale tightness preserves mass, not uniqueness of shape

Condition (11) prevents normalized critical mass from disappearing into `u=0`; it does not force `\nu_i` to have a unique limit. Several distinct cluster profiles may remain. Full scale-adapted fidelity therefore requires either convergence of `\nu_i`, a source-derived law selecting its cluster point, or retention of the whole profile family rather than only one scalar statistic.

### One blow-up does not solve genuinely multiscale structure

The spike-plus-cloud example shows one cascade step. The same construction can be iterated with several separated spectral scales. If order-one critical mass persists on levels whose logarithmic separation diverges, no single normalization by the largest eigenvalue can retain all levels in a compact subset of `(0,\infty)`.

A mechanism facing such a hierarchy needs additional structure: a multiscale/tangent profile, marked scale decomposition, renormalization tree, or an independent theorem ruling out the cascade. AF-113 does not claim that any particular multiscale lift is canonical.

### The result is restricted to positive spectral mass

Positivity is essential to interpreting `\lambda^p` as a probability weight without cancellation. For self-adjoint signed or nonnormal operators, AF-109--AF-112 show that eigenvalue moments can cancel or fail to represent singular-value geometry. The correct blow-up object there may need signed measures, singular-value measures, or additional phase/eigenvector markings.

### Relative spectral fidelity is not arithmetic fidelity

Even perfect knowledge of a limiting `\nu` says only how `p`-mass is distributed across relative spectral scales. It does not establish that the operator contains a rational-prime discriminator, that the scale is prime-specific, or that matched non-prime controls cannot realize the same profile.

Any arithmetic application must compare the **same scale-adapted profile** against matched Beurling/generalized-prime or other controls before treating the retained shape as arithmetic evidence.

## Prior art and novelty assessment

The underlying measure-theoretic and operator-theoretic mechanisms are classical. **No theorem-level novelty is claimed.**

- Barry Simon, ***Trace Ideals and Their Applications***, 2nd ed., Mathematical Surveys and Monographs 120, American Mathematical Society (2005), DOI `10.1090/surv/120`. Role: standard source for Schatten ideals, positive compact-operator spectral calculus, trace identities, and the operator-ideal framework used in (2)--(4).
- David Preiss, **“Geometry of measures in R^n: Distribution, rectifiability, and densities,”** *Annals of Mathematics* 125(3), 537--643 (1987), DOI `10.2307/1971410`. Role: authoritative classical precedent for obtaining new geometric information from blow-ups/rescalings of measures and for treating limiting tangent measures as genuine retained structure rather than reading everything at the collapsed absolute scale.
- P.-L. Lions, **“The concentration-compactness principle in the calculus of variations. The locally compact case, part 1,”** *Annales de l'Institut Henri Poincaré C, Analyse non linéaire* 1(2), 109--145 (1984). Role: classical no-escape/concentration-compactness precedent; the present logarithmic tightness test is an elementary probability-measure specialization of the broader principle that compactness of normalized objects requires ruling out mass escape.
- Patrick Billingsley, ***Convergence of Probability Measures***, 2nd ed., Wiley (1999), DOI `10.1002/9780470316962`. Role: standard weak-convergence and tightness framework used for (5), (10), and the Portmanteau criterion in (27).

Preiss's tangent-measure theory and Lions's concentration-compactness theory are far more general than the elementary one-dimensional spectral rescaling used here. AF-113 does not claim a new blow-up or compactness theorem. The durable Arithmetic Fidelity content is the exact placement of these classical mechanisms after AF-112: **a source-derived scale converts the collapsed critical scalar into a relative spectral probability profile, but the scale itself is faithful only when critical mass is tight in logarithmic relative scale; otherwise a second compression occurs at the new boundary and a multiscale lift or no-cascade theorem is required.**

## Consequences for Arithmetic Fidelity

AF-108--AF-113 now expose a hierarchy that is easy to conflate. A uniform Schatten budget preserves the operator category; exact Schatten-norm conservation can upgrade weak assembly to ideal-norm fidelity; infinitesimal operator scale then collapses fixed determinant or spectral probes to critical moments; critical homogeneity identifies the last unscaled scalar resource; and AF-113 shows how a scale-adapted lift recovers relative shape while introducing a new no-escape obligation.

The practical audit rule is therefore stronger than “keep a canonical scale.” For any collapsing family, identify the resource mass being preserved, derive the scale intrinsically, normalize the corresponding measure, and prove **relative-scale tightness** before interpreting a blow-up profile. If the tightness gate fails, the missing information is not gone in principle, but it has moved into a deeper scale hierarchy that the chosen compression still does not retain.

For the broader Mathia portfolio this supplies a precise cross-scale version of the discriminator-survival constraint. Boundary or transverse structure can remain informative only if the part carrying the discriminator does not escape through successively finer scales before the final analytic, spectral, positivity, or determinant operation observes it.