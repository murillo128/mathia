# AF-112 — Critical homogeneity controls infinitesimal spectral fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `SCHATTEN-CRITICAL-HOMOGENEITY`, `HOLOMORPHIC-FIDELITY-BARRIER`, `BLOW-UP-SCALE-REQUIRED`, `NO-NOVELTY-CLAIM`

## Claim

Let `H` be a complex separable Hilbert space, let

\[
1\le p<\infty,
\]

and let `(A_i)` be a net of positive operators in the Schatten class `\mathcal S_p(H)` such that

\[
\sup_i \|A_i\|_p\le C<\infty,
\qquad
\delta_i:=\|A_i\|\longrightarrow0.
\tag{1}
\]

Thus every individual spectral scale collapses to zero while an order-one amount of total `p`-Schatten mass may remain distributed over more and more eigenvalues.

AF-111 showed that standard regularized determinants see this regime only through integer trace moments and therefore have an integer summability threshold. The underlying phenomenon is more general: **for positive infinitesimal `\mathcal S_p` clouds, the local homogeneity of a scalar spectral observable at zero determines exactly what survives.**

### 1. The `p`-weighted spectral measure collapses to one scalar channel

Let `(\lambda_{ij})_j` be the nonzero eigenvalues of `A_i`, repeated with multiplicity, and define the finite positive measure

\[
\mu_i^{(p)}
:=
\sum_j \lambda_{ij}^{p}\,\delta_{\lambda_{ij}}
\qquad\text{on }[0,\infty).
\tag{2}
\]

Its total mass is

\[
M_i:=\mu_i^{(p)}([0,\infty))
=\sum_j\lambda_{ij}^p
=\|A_i\|_p^p,
\tag{3}
\]

and its support lies in `[0,\delta_i]`. Hence for every bounded continuous `\varphi:[0,\infty)\to\mathbb C`,

\[
\boxed{
\int \varphi(t)\,d\mu_i^{(p)}(t)
-\varphi(0)M_i
\longrightarrow0.
}
\tag{4}
\]

In particular, whenever `M_i\to M`,

\[
\boxed{
\mu_i^{(p)}\Longrightarrow M\,\delta_0
}
\tag{5}
\]

weakly as finite measures.

Thus after operator-scale collapse, every **unrescaled** continuous probe of the `p`-weighted spectral measure sees asymptotically only the total `p`-mass. The detailed distribution of that mass among shrinking eigenvalues is lost.

### 2. Critical-homogeneity theorem

Let `f:[0,\varepsilon)\to\mathbb C` be continuous with `f(0)=0`, and suppose the finite limit

\[
L:=\lim_{t\downarrow0}\frac{f(t)}{t^p}
\tag{6}
\]

exists. Then for all sufficiently large `i`, `f(A_i)` is trace class and

\[
\boxed{
\operatorname{Tr}(f(A_i))
-L\,\|A_i\|_p^p
\longrightarrow0.
}
\tag{7}
\]

More precisely, with

\[
\omega_f(r)
:=
\sup_{0<t\le r}
\left|
\frac{f(t)}{t^p}-L
\right|,
\tag{8}
\]

one has the exact estimate

\[
\boxed{
\left|
\operatorname{Tr}(f(A_i))-L\|A_i\|_p^p
\right|
\le
\omega_f(\delta_i)\,\|A_i\|_p^p
\le C^p\omega_f(\delta_i),
}
\tag{9}
\]

and `\omega_f(\delta_i)\to0`.

Consequently:

- if `f(t)=o(t^p)` at zero, then `\operatorname{Tr}(f(A_i))\to0`;
- if `f(t)=L t^p+o(t^p)`, the only surviving unscaled channel is `L\|A_i\|_p^p`;
- for the exact critical observable `f(t)=t^p`,
  \[
  \operatorname{Tr}(A_i^p)=\|A_i\|_p^p
  \tag{10}
  \]
  survives with no loss.

Thus `p` is the exact homogeneity at which diffuse spectral mass can remain visible without introducing a new scale.

### 3. Holomorphic trace observables have an integer fidelity barrier

Now let `f` be holomorphic in a complex neighborhood of `0`, with

\[
f(0)=0,
\qquad
f(z)=c_m z^m+O(z^{m+1}),
\qquad c_m\ne0,
\tag{11}
\]

where `m\in\mathbb N` is the order of vanishing at zero.

Under only the `\mathcal S_p` budget in (1), a holomorphic trace observable is uniformly guaranteed to be trace class once

\[
m\ge\lceil p\rceil.
\tag{12}
\]

On the positive cone, (7) then yields the sharp dichotomy:

\[
\boxed{
\begin{array}{ll}
m>p &\Longrightarrow\operatorname{Tr}(f(A_i))\to0,\\[4pt]
m=p\in\mathbb N
&\Longrightarrow
\operatorname{Tr}(f(A_i))-c_p\|A_i\|_p^p\to0.
\end{array}
}
\tag{13}
\]

Therefore, if `p\notin\mathbb N`, every holomorphic trace observable that is uniformly admissible from the bare `\mathcal S_p` hypothesis has integer order

\[
m\ge\lceil p\rceil>p
\]

and hence **collapses to zero**.

The noninteger `p`-mass is not absent from the operator. It is invisible specifically to unscaled observables holomorphic at the collapsed spectral point. The real functional-calculus observable

\[
f(t)=t^p
\tag{14}
\]

recovers it exactly, but for noninteger `p` this function does not extend holomorphically through `0` as a complex function.

This gives a category boundary sharper than AF-111's determinant statement:

\[
\boxed{
\text{noninteger critical Schatten mass}
\quad\text{survives continuous spectral calculus}
\quad\text{but is invisible to the uniformly admissible holomorphic trace calculus at }0.
}
\tag{15}
\]

### 4. The three homogeneity regimes are sharp on one explicit cloud

Let `Q_n` be the orthogonal projection onto an `n`-dimensional subspace and define

\[
A_n=n^{-1/p}Q_n.
\tag{16}
\]

Then

\[
A_n\ge0,
\qquad
\|A_n\|=n^{-1/p}\to0,
\qquad
\|A_n\|_p^p=1.
\tag{17}
\]

For a holomorphic `f` as in (11),

\[
\operatorname{Tr}(f(A_n))
=n f(n^{-1/p})
=c_m n^{1-m/p}+O\!\left(n^{1-(m+1)/p}\right).
\tag{18}
\]

Hence the same family realizes all three regimes:

\[
\boxed{
\begin{array}{lll}
m>p &:& \operatorname{Tr}(f(A_n))\to0,\\[2pt]
m=p\in\mathbb N &:& \operatorname{Tr}(f(A_n))\to c_p,\\[2pt]
m<p &:& |\operatorname{Tr}(f(A_n))|\asymp n^{1-m/p}\to\infty.
\end{array}
}
\tag{19}
\]

The last line shows why an order `m<p` holomorphic observable cannot be guaranteed trace class or uniformly controlled from an `\mathcal S_p` budget alone. The first line shows that moving above the critical homogeneity erases an order-one amount of `p`-mass.

### 5. Equal critical mass can hide different microscopic spectral shapes

The collapse in (4) is not merely a rephrasing of `\|A_i\|\to0`. Distinct shrinking spectral geometries can have the same surviving scalar channel.

Besides `A_n` from (16), choose constants `a,b\in(0,1)` with

\[
a^p+b^p=1,
\qquad a\ne b,
\tag{20}
\]

and define a positive finite-rank operator `B_n` with `n` eigenvalues equal to `a n^{-1/p}` and `n` eigenvalues equal to `b n^{-1/p}`. Then

\[
\|B_n\|\to0,
\qquad
\|B_n\|_p^p=1.
\tag{21}
\]

For every `f` satisfying (6) with the same `p`,

\[
\operatorname{Tr}(f(A_n))\to L,
\qquad
\operatorname{Tr}(f(B_n))\to L.
\tag{22}
\]

Yet after the explicit blow-up `t\mapsto n^{1/p}t`, the weighted spectral shapes are different: `A_n` is concentrated at scale `1`, whereas `B_n` has critical mass split between the distinct scales `a` and `b`.

Therefore an unscaled critical-homogeneity observable cannot recover microscopic shape from the collapsing cloud. To retain that structure one must introduce additional information, for example a **blow-up/rescaling scale**, a marked decomposition, or another relational lift that prevents all critical mass from being pushed to the single point `0`.

## Derivation

For (4), every point in the support of `\mu_i^{(p)}` lies in `[0,\delta_i]`. Hence

\[
\begin{aligned}
\left|
\int\varphi(t)\,d\mu_i^{(p)}(t)-\varphi(0)M_i
\right|
&=
\left|
\sum_j\lambda_{ij}^p
\bigl(\varphi(\lambda_{ij})-\varphi(0)\bigr)
\right|\\
&\le
M_i
\sup_{0\le t\le\delta_i}|\varphi(t)-\varphi(0)|\\
&\le
C^p
\sup_{0\le t\le\delta_i}|\varphi(t)-\varphi(0)|,
\end{aligned}
\tag{23}
\]

which tends to zero by continuity of `\varphi` at zero. If `M_i\to M`, this is exactly weak convergence to `M\delta_0`, proving (5).

For (7), define for `t>0`

\[
h(t)=\frac{f(t)}{t^p}
\]

and set `h(0)=L`. The existence of (6) makes `h` continuous at zero. Since eventually `\sigma(A_i)\subset[0,\delta_i]\subset[0,\varepsilon)`, functional calculus gives

\[
\operatorname{Tr}(f(A_i))
=\sum_j f(\lambda_{ij})
=\sum_j\lambda_{ij}^p h(\lambda_{ij})
=\int h(t)\,d\mu_i^{(p)}(t).
\tag{24}
\]

The ratio `f(t)/t^p` is bounded near zero, so `|f(t)|\le Kt^p`; hence the series in (24) converges absolutely and `f(A_i)` is trace class. Applying (23) to `h` proves (9).

For the holomorphic corollary, (11) gives on the positive real axis

\[
\frac{f(t)}{t^p}
=t^{m-p}\bigl(c_m+O(t)\bigr).
\tag{25}
\]

If `m>p`, the ratio tends to zero. If `m=p`, necessarily `p` is an integer and the ratio tends to `c_p`. Equation (13) is then a direct instance of (7).

If `m\ge\lceil p\rceil`, the local factorization `f(z)=z^m g(z)` with `g` holomorphic shows independently that `f(A_i)` is trace class: `A_i\in\mathcal S_m`, `A_i^m\in\mathcal S_1`, and `g(A_i)` is bounded for all sufficiently large `i`.

Finally, (18) follows by substituting the single nonzero eigenvalue scale `n^{-1/p}` with multiplicity `n` into the Taylor expansion (11). Equations (20)--(22) follow from the same critical-homogeneity estimate and the exact equality of the two `p`-mass budgets.

## Exact controls and failure modes

### Positivity is doing real work

The measure `\mu_i^{(p)}` is built from positive eigenvalues and directly represents the singular-value resource `\|A_i\|_p^p`. For general nonnormal operators, eigenvalue moments can cancel or fail to encode singular-value geometry, as AF-109 and AF-110 already show.

The holomorphic trace estimate for powers extends more broadly through Schatten ideal inequalities, but the exact identification of the surviving critical coefficient with **total `p`-mass** is a positive-operator statement. Do not silently transfer (7) to arbitrary operators by replacing singular values with eigenvalues.

### The theorem is unscaled

Equation (4) says that the weighted measure collapses because its entire support shrinks to zero. It does not say the microscopic spectral profile is absent. The pair `A_n,B_n` demonstrates that a blow-up can retain information that every unscaled critical test loses.

Therefore this result is a no-go for an **unscaled** scalarization. A candidate mechanism that introduces a canonically forced scale before compression lies outside the theorem and must be audited separately.

### Critical mass is not full spectral fidelity

Even at exact homogeneity `p`, equation (7) retains at most one scalar resource channel unless the test family itself changes with the shrinking scale. Two clouds with equal `p`-mass but different rank profiles or rescaled spectral distributions remain indistinguishable to the whole fixed class `f(t)=Lt^p+o(t^p)`.

Thus matching the critical Schatten norm is sufficient for resource conservation in AF-109 when combined with a known WOT limit, but it is not a complete invariant of an isolated infinitesimal cloud.

### Holomorphic collapse is a category statement, not a claim that fractional powers are unnatural

For positive operators, `A^p` is canonical for every real `p>0` by the continuous/Borel spectral calculus. When `p` is noninteger, what fails is holomorphicity through the spectral collapse point `0`, not mathematical legitimacy.

The distinction matters for determinant- and zeta-like constructions because many such scalar observables are built from holomorphic expansions in the small operator. AF-112 says that their local Taylor order must match the critical resource homogeneity exactly; an integer Taylor calculus cannot accidentally recover a noninteger critical moment.

## Prior art and novelty assessment

The ingredients are classical. **No theorem-level novelty is claimed.**

- Barry Simon, ***Trace Ideals and Their Applications***, 2nd ed., Mathematical Surveys and Monographs 120, American Mathematical Society (2005), DOI `10.1090/surv/120`. Role: standard source for Schatten ideals, singular values, trace-class functional calculus, trace estimates, and the operator-ideal framework used throughout AF-108--AF-112.
- Patrick Billingsley, ***Convergence of Probability Measures***, 2nd ed., Wiley Series in Probability and Statistics (1999), DOI `10.1002/9780470316962`. Role: standard weak-convergence-of-measures framework; (5) is an elementary support-shrinking specialization of the usual bounded-continuous-test characterization.

The measure collapse (4), the critical-homogeneity estimate (9), and the holomorphic trichotomy are direct elementary consequences of these standard structures. The durable Arithmetic Fidelity content is the classification they provide: **an infinitesimal positive `\mathcal S_p` cloud has one unscaled critical scalar resource, its total `p`-mass; every smoother/higher-homogeneity fixed probe loses it, while noninteger critical mass necessarily lies outside a holomorphic-at-zero Taylor channel.**

## Consequences for Arithmetic Fidelity

AF-111's integer determinant threshold is now a corollary of a more general fidelity law rather than a determinant-specific accident. A regularized trace-log begins at an integer power `r`; AF-112 says that in an infinitesimal `\mathcal S_p` cloud that power can retain order-one mass only when `r=p`. If `r>p`, the observable is supercritical and vanishes. If `p` is noninteger, the first admissible integer power is automatically supercritical.

The result also identifies the next legitimate escape route. Once all unscaled `p`-weighted spectral mass concentrates at zero, adding more fixed smooth or holomorphic scalar tests cannot recover microscopic provenance. A surviving mechanism must instead change the information layer: introduce an independently justified blow-up scale, retain marked/relational spectral structure, or use a non-holomorphic critical observable such as the exact `p`-power on the positive cone.

This sharpens the line's composition audit for operator-based RH proposals. Before interpreting a determinant, trace, zeta-regularization, or other analytic scalarization, determine the resource exponent carried by the upstream operator family and the local homogeneity of the downstream observable at the collapse point. If the observable is supercritical, the relevant mass has already been erased. If it is exactly critical, only the corresponding scalar resource survives unless extra scaled or relational structure is retained. No later operation on the unscaled scalar output can reconstruct the discarded spectral shape.