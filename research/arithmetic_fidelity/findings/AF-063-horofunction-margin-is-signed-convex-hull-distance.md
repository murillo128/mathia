# AF-063 — Horofunction margin is signed convex-hull distance in smooth normed spaces

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-BOUNDARY`

## Claim

Let `(V,\|\cdot\|)` be a finite-dimensional real normed space whose norm is smooth and strictly convex. Let `S\subset V` be nonempty and compact, put

\[
K=\operatorname{conv}(S),
\tag{1}
\]

and fix `m\in V`. Normalize the horofunction compactification at `m`, so an escaping sequence `x_n` produces functions

\[
h_n(z)=\|x_n-z\|-\|x_n-m\|.
\tag{2}
\]

For a boundary horofunction `h`, define its target gap

\[
g_S(h)=\inf_{s\in S}h(s),
\tag{3}
\]

and define the **first-order horofunction fidelity margin**

\[
\Gamma_S(m)=\sup_{h\in\partial_h V} g_S(h).
\tag{4}
\]

Then:

1. **The horofunction margin depends on `S` only through its convex hull and is exactly a signed convex-hull distance.** If `h_K(\varphi)=\sup_{k\in K}\varphi(k)` is the support function and `\|\varphi\|_*=1`, then
   \[
   \boxed{
   \Gamma_S(m)
   =
   \sup_{\|\varphi\|_*=1}
   \bigl(\varphi(m)-h_K(\varphi)\bigr).
   }
   \tag{5}
   \]
   Consequently,
   \[
   \boxed{
   \Gamma_S(m)=
   \begin{cases}
   \operatorname{dist}(m,K), & m\notin K,\\[1mm]
   0, & m\in\partial K,\\[1mm]
   -\operatorname{dist}(m,V\setminus K), & m\in\operatorname{int}K.
   \end{cases}
   }
   \tag{6}
   \]
   Here the last line is present only when `K` has nonempty ambient interior.

2. **The sign of `\Gamma_S(m)` exactly classifies the first-order far-field regime.** For the AF-062 positive excess
   \[
   e_{S,m}(x)
   =
   \bigl(\operatorname{dist}(x,S)-\|x-m\|\bigr)_+,
   \tag{7}
   \]
   one has:
   - `\Gamma_S(m)>0` exactly outside `K`; some escaping direction has a positive limiting distance advantage for `S` over `m`;
   - `\Gamma_S(m)<0` exactly in `\operatorname{int}K`; every horofunction direction has a uniform negative gap;
   - `\Gamma_S(m)=0` exactly on `\partial K`; first-order asymptotics tie and only a finer decay scale can decide powered fidelity.

3. **Every exterior base point fails every nonlinear powered safe-lift test.** For
   \[
   \Delta_{p,S}(m)
   =
   \sup_{x\in V}
   \left(
   \operatorname{dist}(x,S)^p-\|x-m\|^p
   \right),
   \qquad p>1,
   \tag{8}
   \]
   AF-062 and (6) give
   \[
   \boxed{
   m\notin K
   \Longrightarrow
   \Delta_{p,S}(m)=+\infty
   \quad\text{for every }p>1.
   }
   \tag{9}
   \]
   Thus the exterior obstruction is intrinsically first-order and does not depend on a preferred power.

4. **Every ambient-interior base point is finitely liftable for every finite power.** If `m\in\operatorname{int}K`, then
   \[
   \boxed{
   \Delta_{p,S}(m)<\infty
   \quad\text{for every finite }p>1.
   }
   \tag{10}
   \]
   In fact there is `R<\infty` such that
   \[
   \operatorname{dist}(x,S)<\|x-m\|
   \qquad\text{whenever }\|x-m\|\ge R,
   \tag{11}
   \]
   so the powered defect is nonpositive outside a compact ball.

5. **All nontrivial critical-power phenomena are forced onto the convex-hull boundary.** If `m\in\partial K`, then `\Gamma_S(m)=0`; the horofunction boundary records only a first-order tie. AF-062's weighted excess then shows that the actual threshold is determined by the decay rate of
   \[
   \operatorname{dist}(x,S)-\|x-m\|
   \tag{12}
   \]
   along zero-gap escape directions. In particular:
   - AF-059's missing Euclidean hull-boundary points have residual excess of order `t^{-1}` and critical power `2`;
   - AF-061's symmetric two-point `\ell^r` model for `1<r<\infty` has residual excess of order `t^{1-r}` and critical power `r`.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{in smooth strictly convex finite-dimensional normed spaces,}
\quad
\text{first-order horofunction fidelity is exactly convex-hull fidelity.}
}
\tag{13}
\]

The convex hull is therefore not merely a convenient control for the powered safe-lift examples. It is the exact quotient seen by the entire first-order horofunction layer: exterior points are universally lost, interior points are uniformly safe, and only boundary ties can retain higher-order information about the original nonconvex target or the source norm.

## Derivation

### Linear form of all boundary horofunctions

For a finite-dimensional normed space with smooth and strictly convex norm, the classical horofunction description gives every boundary horofunction, with basepoint `0`, in the form

\[
h_\varphi(z)=-\varphi(z),
\qquad
\|\varphi\|_*=1.
\tag{14}
\]

Lemmens--Power explicitly record this description and the associated dual-unit-ball compactification, citing the earlier normed-space horofunction theory. Translating the normalization from `0` to `m` gives

\[
h_\varphi^{(m)}(z)
=
-\varphi(z-m),
\qquad
\|\varphi\|_*=1,
\tag{15}
\]

and every dual unit functional occurs.

Therefore

\[
\begin{aligned}
g_S(h_\varphi^{(m)})
&=
\inf_{s\in S}\bigl(-\varphi(s-m)\bigr)\\
&=
\varphi(m)-\sup_{s\in S}\varphi(s)\\
&=
\varphi(m)-h_K(\varphi),
\end{aligned}
\tag{16}
\]

because a linear functional has the same supremum on `S` and on `\operatorname{conv}(S)`. Taking the supremum over all horofunctions proves (5).

### Outside the hull: the margin is ordinary distance

Put

\[
\delta=\operatorname{dist}(m,K)>0.
\tag{17}
\]

For every `\varphi` with `\|\varphi\|_*\le1` and every `k\in K`,

\[
\varphi(m)-h_K(\varphi)
\le
\varphi(m-k)
\le
\|m-k\|.
\tag{18}
\]

Taking the infimum over `k` gives the upper bound

\[
\varphi(m)-h_K(\varphi)\le\delta.
\tag{19}
\]

Conversely, the open ball `B(m,\delta)` is disjoint from the compact convex set `K`. Hahn--Banach separation gives a nonzero continuous linear functional `\varphi` separating them. After normalizing `\|\varphi\|_*=1`, the support value of the radius-`\delta` ball is `\varphi(m)-\delta`, and sharp separation yields

\[
h_K(\varphi)
\le
\varphi(m)-\delta.
\tag{20}
\]

Combining (19)--(20) gives

\[
\sup_{\|\varphi\|_*=1}
\bigl(\varphi(m)-h_K(\varphi)\bigr)
=\delta,
\tag{21}
\]

which is the exterior line of (6).

### Inside the hull: the same margin is negative depth

Suppose `m\in\operatorname{int}K` and define the centered depth

\[
r
=
\operatorname{dist}(m,V\setminus K)
=
\sup\{a\ge0:m+aB\subseteq K\},
\tag{22}
\]

where `B` is the closed unit ball of `V`. The support-function characterization of a closed convex set gives

\[
m+aB\subseteq K
\iff
\varphi(m)+a\le h_K(\varphi)
\quad\forall\,\|\varphi\|_*=1.
\tag{23}
\]

Hence the largest admissible `a` is

\[
r
=
\inf_{\|\varphi\|_*=1}
\bigl(h_K(\varphi)-\varphi(m)\bigr).
\tag{24}
\]

Negating (24) proves

\[
\Gamma_S(m)=-r<0.
\tag{25}
\]

If `m\in\partial K`, the same formula has `r=0`; equivalently, a supporting functional at `m` attains

\[
\varphi(m)=h_K(\varphi),
\tag{26}
\]

while every dual functional has `\varphi(m)\le h_K(\varphi)`. Thus `\Gamma_S(m)=0`, completing (6).

### Exterior divergence follows from AF-062

If `m\notin K`, choose a boundary horofunction `h` with

\[
\inf_S h=\Gamma_S(m)=\delta>0.
\tag{27}
\]

By the definition of the horofunction boundary there is an escaping sequence `x_n` whose normalized distance functions converge to `h`. AF-062 proves, for compact `S`,

\[
\operatorname{dist}(x_n,S)-\|x_n-m\|
\longrightarrow
\inf_S h
=\delta.
\tag{28}
\]

Thus the first-order excess stays bounded below by a positive constant along an escaping sequence. AF-062's power amplification criterion then gives (9) for every `p>1`.

### Interior finiteness is a compactness consequence of the negative margin

Now let `m\in\operatorname{int}K`. Equation (25) gives a uniform boundary gap

\[
\inf_S h\le-r<0
\qquad
\forall h\in\partial_hV.
\tag{29}
\]

Suppose (11) were false. Then there would be an escaping sequence `x_n` with

\[
\operatorname{dist}(x_n,S)-\|x_n-m\|\ge0
\qquad\forall n.
\tag{30}
\]

Finite dimensionality makes `V` proper, so after passing to a subsequence the normalized distance functions converge locally uniformly to a boundary horofunction `h`. AF-062 again gives

\[
\operatorname{dist}(x_n,S)-\|x_n-m\|
\longrightarrow
\inf_Sh.
\tag{31}
\]

The left side has nonnegative limit inferior by (30), contradicting (29). Therefore (11) holds for some `R`.

For `\|x-m\|\ge R`, equation (11) implies

\[
\operatorname{dist}(x,S)^p-\|x-m\|^p<0.
\tag{32}
\]

On the compact ball `\overline B(m,R)`, the same defect is continuous and therefore bounded above. This proves (10) simultaneously for every fixed finite `p>1`.

## Exact controls

### Convexification is invisible at first order

If compact sets `S_1,S_2\subset V` satisfy

\[
\operatorname{conv}(S_1)=\operatorname{conv}(S_2)=K,
\tag{33}
\]

then (5) gives

\[
\Gamma_{S_1}(m)=\Gamma_{S_2}(m)
\qquad\forall m\in V.
\tag{34}
\]

Thus no first-order horofunction-gap observable can distinguish a sparse target from a filled-in target with the same convex hull. Any claimed discriminator between them must live in residual convergence rates, finite-scale data, marking, or another enrichment beyond the limiting horofunction value.

### Genuine target points remain stronger than boundary ties

If `m\in S`, then

\[
\operatorname{dist}(x,S)\le\|x-m\|
\qquad\forall x,
\tag{35}
\]

so `\Delta_{p,S}(m)=0` for every `p\ge1`. If instead `m\in\partial K\setminus S`, equation (6) gives the same first-order margin `0`, yet AF-059 and AF-061 show that higher powers can diverge. Therefore `\Gamma=0` must not be interpreted as full fidelity; it marks precisely the layer at which first-order asymptotics stop deciding.

### Euclidean space recovers AF-059's global phase diagram skeleton

For the Euclidean norm, (6), (9), and (10) recover the universal parts of AF-059 without expanding squared distances:

- outside `K`, every `p>1` diverges;
- inside `\operatorname{int}K`, every finite `p>1` is finite;
- only `\partial K` can contain a power-dependent transition.

AF-059's specifically Euclidean work is then isolated to the boundary theorem that missing target points switch at `p=2`.

### The `\ell^r` family locates the representation dependence on the boundary

For `1<r<\infty`, the `\ell^r` norm is smooth and strictly convex, so the present theorem applies. AF-061's two-point midpoint lies on the boundary of the lower-dimensional convex hull, hence `\Gamma=0` for every such `r`. Nevertheless its powered threshold is exactly `p=r`. Therefore the representation dependence discovered in AF-061 is not a change in the first-order convex-hull quotient: it is entirely a change in the decay rate after a zero first-order tie.

## Prior art and novelty assessment

The ingredients are classical, and no novelty is claimed for horofunction compactification, Hahn--Banach separation, support functions, convex hulls, or signed distance/depth formulas.

- Bas Lemmens and Kieran Power, **“Horofunction Compactifications and Duality,”** *Journal of Geometric Analysis* 33, 154 (2023), DOI `10.1007/s12220-023-01205-0`. In their discussion of finite-dimensional normed spaces with smooth and strictly convex norm, they explicitly record that boundary horofunctions are the linear functionals `h(z)=-x^*(z)` with `\|x^*\|=1` and that the horofunction compactification is naturally homeomorphic to the closed dual unit ball. This is the direct literature bridge used in (14)--(15).
- Cormac Walsh, **“The horofunction boundary of finite-dimensional normed spaces,”** *Mathematical Proceedings of the Cambridge Philosophical Society* 142(3), 497--507 (2007), DOI `10.1017/S0305004107000096`. Role: general finite-dimensional normed-space horofunction/Busemann theory and the dual-unit-ball facial structure beyond the smooth strictly convex specialization.
- **“Support function,”** *Encyclopedia of Mathematics*. Role: standard support-function duality for closed convex sets and the fact that support functions determine the closed convex set; together with Hahn--Banach separation this supplies the classical convex-analytic side of (5)--(6).

A targeted literature search across horofunction boundaries, support functions, convex hulls, and normed-space distance formulas found the two classical halves separately: dual-functional descriptions of horofunctions and support-functional descriptions of convex sets. No absence result from that search is used as evidence of novelty. The durable Arithmetic Fidelity contribution claimed here is only their exact composition with AF-062's distance-excess observable: it identifies the **entire first-order fidelity quotient** as convexification and proves that all nontrivial powered thresholds in this category are boundary residual phenomena.

## Boundaries and failure modes

- The linear horofunction formula (14) is used only under the declared finite-dimensional, smooth, strictly convex norm hypothesis. General finite-dimensional norms can have non-linear horofunctions associated with faces of the dual ball; no version of (5)--(6) is asserted there without a separate audit.
- Compactness of `S` ensures `K` is compact, support values are finite and attained, and AF-062's passage from local-uniform horofunction convergence to `\inf_S h` is valid. Extensions to unbounded or merely closed targets require additional hypotheses.
- Equation (6) classifies only the limiting first-order gap. It deliberately does not predict the critical power on `\partial K`.
- `\operatorname{int}K` is ambient interior. If `K` is lower-dimensional, its ambient interior is empty and every point of `K` lies in the first-order tie regime. AF-061's two-point target is exactly such a control.
- The theorem does not make convexification an acceptable lift by itself. Rather, it is a no-go statement: any mechanism restricted to first-order horofunction gaps necessarily forgets all distinctions between compact targets with the same convex hull.

## Consequences for Arithmetic Fidelity

AF-062 separated positive first-order horofunction gaps from zero-gap residual decay but did not identify the global geometry of those regimes. The present result closes that gap in the smooth strictly convex finite-dimensional norm category:

\[
V\setminus K
\quad\longleftrightarrow\quad
\Gamma>0
\quad\longleftrightarrow\quad
\text{all }p>1\text{ fail},
\tag{36}
\]

\[
\operatorname{int}K
\quad\longleftrightarrow\quad
\Gamma<0
\quad\longrightarrow\quad
\text{all finite }p>1\text{ are safe},
\tag{37}
\]

while

\[
\partial K
\quad\longleftrightarrow\quad
\Gamma=0
\quad\longrightarrow\quad
\text{inspect higher-order decay / retained provenance}.
\tag{38}
\]

This is a reusable stopping rule for future metric-compression proposals. If their observable sees only limiting normalized distance differences, then its maximal target discriminator is the convex hull. To recover structure of the original target beyond convexification, the proposal must retain a rate, a mark, a finite-scale profile, a non-linear boundary observable, or another independently justified enrichment.