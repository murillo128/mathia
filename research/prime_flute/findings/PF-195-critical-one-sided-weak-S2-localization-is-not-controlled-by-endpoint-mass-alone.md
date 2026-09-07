# PF-195 — critical one-sided weak-`S_2` localization is not controlled by endpoint mass alone

**Status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE/ROUTE-BOUNDARY`. PF-190 identifies the two critical gradient-resolvent half-factors in PF-175 as the source of the full-surface `log^2(n)/n` endpoint envelope, while PF-191 shows that the exact-area Lambert/body comparison itself has summable strong-`L^1` metric-defect mass. The accepted weak-trace clue therefore isolates an attractive shortcut: put each gradient half-factor directly in weak `S_2` with quasi-norm proportional to the square root of the local endpoint mass, then multiply the two factors into weak `S_1`. That shortcut is **not available from `L^2` coefficient mass alone**. Levitina--Sukochev--Zanin give a critical one-sided Cwikel counterexample with `f in L^2(R)` for which `M_f(1-Delta)^(-1/4)` is not even `S_4`, hence cannot lie in `S_{2,infinity}`. Their positive critical weak-`S_2` theorem instead requires a stronger logarithmically weighted local-`L^infinity` condition. In the closest flat model of the PF gradient factor, feeding that sufficient condition the PF-191 Lambert profile loses the decisive `1/cosh(a)` effective-area gain and charges order `d`, whose prime/shift sum diverges. Thus the endpoint half-factor route now has a sharper gate: it needs a **PF-specific, mass-sensitive nonconcentration/localization theorem**, or it must be bypassed by a directly symmetrized weak-`S_1` estimate. No failure of weak trace class for the actual prime/shift relative resolvent is claimed.

## Claim

Use the PF-175 form factorization. On an area-preserving comparison, the principal coefficient term is schematically

\[
T_{\rm grad}
=
(dR_h)^*\, C\, dR_g,
\tag{1}
\]

with

\[
|C|\le C_0\delta,
\tag{2}
\]

where `delta` is the multiplicative metric deviation. Writing the polar/square-root splitting of `C` makes the critical half-factor coefficient

\[
a:=|C|^{1/2}.
\tag{3}
\]

On any PF-183 normalized thick module, where the inverse-unit-ball weight is uniformly comparable to a constant, finite endpoint defect mass

\[
A_1:=\int W\,\delta\,d\mu<\infty
\tag{4}
\]

implies only the mass estimate

\[
\boxed{\|a\|_{L^2}^2\le C A_1.}
\tag{5}
\]

The tempting critical analogue of PF-175 would be a uniform estimate of the schematic form

\[
\boxed{
\|M_a dR\|_{\mathcal S_{2,\infty}}
\le C\|a\|_{L^2},
}
\tag{6}
\]

or a geometry-localized version with the right-hand side controlled by `A_1^{1/2}`. Equation (6) is **not a generic critical Cwikel estimate**.

Levitina--Sukochev--Zanin, Theorem 5.1, prove that there exists a compactly supported

\[
f\in L^2(\mathbb R)
\tag{7}
\]

such that

\[
\boxed{
M_f(1-\Delta_{\mathbb R})^{-1/4}
\notin \mathcal S_4.
}
\tag{8}
\]

Since

\[
\mathcal S_{2,\infty}\subset \mathcal S_4,
\tag{9}
\]

(8) implies

\[
M_f(1-\Delta_{\mathbb R})^{-1/4}
\notin\mathcal S_{2,\infty}.
\tag{10}
\]

This one-dimensional operator has exactly the same critical Schatten scaling as a first-order-resolvent half-factor in dimension two: its Fourier multiplier has order `-1/2` in dimension one, whereas `d(1-Delta)^{-1}` has order `-1` in dimension two. Thus bare `L^2` multiplier mass cannot be invoked as an off-the-shelf endpoint principle for (6).

The same paper also gives the relevant positive boundary. Its Theorem 5.6 proves, in Euclidean space, that

\[
f\in \ell_{2,\log}(L^\infty),
\qquad
g\in\ell_{2,\infty}(L^4)
\tag{11}
\]

imply

\[
\boxed{M_f g(-i\nabla)\in\mathcal S_{2,\infty}.}
\tag{12}
\]

For the flat two-dimensional gradient-resolvent symbols

\[
g_j(\xi)=\frac{\xi_j}{1+|\xi|^2},
\tag{13}
\]

the local `L^4` norm on unit frequency cubes is `O(|m|^{-1})`, so the resulting cube sequence is in weak `ell^2`; hence (13) lies on the positive side of the theorem. The extra burden is on the **spatial coefficient**: (11) asks for logarithmically weighted square summability of unit-cube local suprema, not merely its `L^2` mass.

For the exact PF-191 Lambert profile that distinction is summability-critical. PF-191 proves on the finite triangular branch

\[
\delta(\tau,y)
\le
C\frac{d}{1+\sinh^2\tau}
\tag{14}
\]

for the adjacent half-cuff parameter change `a -> a+d`, while its actual integrated mass satisfies

\[
\boxed{
\int_{Q(a)}\delta\,d\mu
\le C\frac d{\cosh a}.}
\tag{15}
\]

If `b=\delta^{1/2}` is measured instead by the local-sup coefficient norm in (11), unit strips in the `tau` direction satisfy

\[
\|b\|_{L^\infty(\{j\le\tau\le j+1\})}^2
\le C d e^{-2j}
\tag{16}
\]

away from a fixed finite head. The logarithmic cube weight is harmless against this exponential tail, so the corresponding positive Cwikel coefficient norm has the scale

\[
\boxed{
\|b\|_{\ell_{2,\log}(L^\infty)}^2
\le C d,
}
\tag{17}
\]

not `Cd/cosh(a)`. In other words, a unit-cube supremum criterion cannot see the thin cross-sectional area that produces PF-191's endpoint gain.

For the exact prime/shift family, PF-121 records

\[
d_n=a_n^+-a_n\sim p_n^{-1}
\tag{18}
\]

up to the indexing convention inherited from PF-107, and PF-107 proves the corresponding additive cuff defect is not `ell^1`. Therefore

\[
\sum_n d_n=\infty,
\qquad
\sum_n \frac{d_n}{\cosh a_n}<\infty
\tag{19}
\]

at the level relevant here. A modulewise application of the standard local-sup weak-`S_2` criterion would consequently produce a two-half-factor scale of order `d_n`, losing exactly the effective-area suppression that made PF-191 useful. This does **not** prove that the actual PF half-factors have that bad scale; it proves that the cited generic sufficient theorem does not preserve the project-specific endpoint currency.

## 1. Why the counterexample targets the proposed half-factor shortcut

PF-175 reaches `S_r`, `r>1`, by placing each gradient-resolvent half-factor in `S_{2r}` and applying Schatten Hölder. PF-190 tracks the constants as `r downarrow 1` and finds one factor `(r-1)^{-1}` from each side. The accepted weak-trace clue asks whether one can replace the two critical strong-`S_2` limits by weak-`S_2` bounds and remove both logarithms.

At the level of ideal calculus that implication is sound: a product of two weak-`S_2` operators is weak `S_1` under the standard singular-value product inequality. PF-195 does not challenge that step. It challenges the **input estimate**. Equation (5) is exactly the data one gets by taking a square root of a finite `L^1` coefficient defect. Theorem 5.1 shows that this data, by itself, does not control a critical one-sided multiplier in weak `S_2` even on flat space with compactly supported coefficient.

The counterexample coefficient in Theorem 5.1 is not the PF coefficient and is not bounded in the way a globally quasi-isometric metric deviation is bounded. Therefore the theorem cannot be turned into a counterexample to the canonical prime/shift half-factor. Its role is narrower and exact: **any proof of (6) must use more than the endpoint mass hypothesis**. Uniform boundedness, smoothness, canonical spatial profile, bounded-overlap geometry, or a stronger nonconcentration norm may provide that extra input, but it has to be proved and its summability cost has to be tracked.

## 2. The standard positive endpoint condition loses the Lambert effective area

Theorem 5.6 explains what one classical repair looks like. It replaces bare `L^2` control by local `L^infinity` information summed with a logarithmic weight. This prevents the concentration mechanism behind Theorem 5.1 and restores weak `S_2`.

For PF this repair is not automatically cheap. The pointwise Lambert strain (14) is largest near `tau=0`, where it has size `O(d)`, but PF-191's area slice there has width `O(1/cosh a)`. The integral sees that width and produces (15); the local supremum does not. Equations (16)--(17) make the mismatch quantitative.

Thus the remaining endpoint problem is not simply "find a weak Cwikel theorem." It is to find one whose norm is sensitive to the **same geometric measure suppression** already established by PF-191, or to prove an additional canonical nonconcentration statement that converts the PF local-sup currency back into the summable mass currency. A theorem whose coefficient norm charges each Lambert body by its worst pointwise strain reintroduces PF-107's divergent harmonic-prime scale.

## 3. The symmetrized route remains genuinely different

The one-sided failure does not invalidate the other branch of the accepted clue. Solomyak's critical two-dimensional theorem, in the form revisited and optimized by Sukochev--Zanin, places the symmetrized model

\[
(1-\Delta_{\mathbb T^2})^{-1/2}
M_f
(1-\Delta_{\mathbb T^2})^{-1/2}
\tag{20}
\]

in weak trace class for `f in L log L`. Sukochev--Zanin show that this Orlicz scale is optimal in the relevant Orlicz/Lorentz classes.

Because the PF metric-deviation coefficient is uniformly bounded by quasi-isometry, finite local `L^1` mass implies finite local `L log L` mass with comparable size. That fact still does not transfer the torus theorem to a noncompact hyperbolic vector-gradient form, but it shows why the **direct two-sided operator** can have a better endpoint currency than either one-sided square-root factor considered separately.

Accordingly, PF-195 changes the priority inside the analytic endpoint gate. There are now two honest options:

1. prove a PF-specific weak-`S_2` half-factor estimate whose constant is controlled by endpoint mass because the actual coefficients satisfy a stronger spatial/nonconcentration property; or
2. avoid separate critical half-factors and prove a directly symmetrized weak-`S_1` estimate for the localized PF form, then solve the finite-color/off-diagonal reassembly problem.

Neither option is established here.

## Prior art and novelty assessment

**G. Levitina, F. Sukochev, D. Zanin**, *Cwikel estimates revisited*, Proceedings of the London Mathematical Society **120** (2020), 265--304. DOI `10.1112/plms.12301`; arXiv:1703.04254.

- Theorem 5.1 is the exact source of (7)--(10).
- Definition 5.5 and Theorem 5.6 are the source of the logarithmically weighted local-`L^infinity` sufficient condition in (11)--(12).
- The paper explicitly isolates `L_{2,infinity}` as the weak-ideal endpoint not covered by the ordinary `(L^2,L^infinity)` interpolation Cwikel mechanism.

**M. Cwikel**, *Weak type estimates for singular values and the number of bound states of Schrödinger operators*, Annals of Mathematics **106** (1977), 93--100. DOI `10.2307/1971160`.

- The classical one-sided weak-type estimate is stated for the noncritical range `p>2`; it does not supply the `p=2` half-factor endpoint required here.

**F. Sukochev, D. Zanin**, *Optimal Cwikel--Solomyak Estimates*, Journal of Fourier Analysis and Applications **29** (2023), article 21. DOI `10.1007/s00041-023-10003-9`.

- This records the symmetrized weak-trace `L log L` theorem of Solomyak and proves its optimality within the relevant Orlicz/Lorentz classes.

No novelty is claimed for any of these operator-ideal theorems. The durable project-specific result is the combination with PF-175/PF-190/PF-191: **the known generic critical one-sided theory neither follows from the PF endpoint mass nor preserves the Lambert `1/cosh(a)` gain under its standard positive local-sup hypothesis**. This removes a tempting but unjustified shortcut from the weak-trace clue while leaving a precise PF-specific and a symmetrized alternative.

## Falsification and boundary checks

PF-195 would be overclaimed if read as any of the following, none of which is asserted:

- the actual prime/shift gradient half-factor is not in `S_{2,infinity}`;
- bounded smooth coefficients on the PF normalized slabs cannot satisfy a stronger weak-`S_2` theorem;
- Theorem 5.1 is a two-dimensional hyperbolic counterexample;
- Theorem 5.6 gives the sharp coefficient space for the PF geometry;
- the symmetrized Cwikel--Solomyak theorem automatically applies to the hyperbolic relative resolvent;
- the full first relative resolvent is not weak trace class;
- PF-190's `log^2(n)/n` envelope is sharp;
- any RH consequence follows.

A positive result can bypass this route boundary in either of two decisive ways. One may prove a PF-specific estimate

\[
\|M_{|C|^{1/2}}dR\|_{\mathcal S_{2,\infty}}^{\#}
\le C
\left(\int W|C|\,d\mu\right)^{1/2}
\tag{21}
\]

on the actual canonical coefficient class, with a constant uniform through the normalized tail and a proof that explicitly uses whatever additional structure defeats the Cwikel counterexample. Alternatively, one may prove a direct two-sided estimate

\[
\|(dR)^* C\,dR\|_{\mathcal S_{1,\infty}}^{\#}
\le C\int W|C|\,d\mu
\tag{22}
\]

or an `L log L` variant with the same summable PF mass, without factoring through separate weak-`S_2` bounds.

For either route, the decisive global check remains PF-183-style reassembly: the local quasi-norms must sum through disjoint/bounded-overlap families without recreating a logarithmic loss in cross terms.

## Consequences for the research line

PF-192--PF-194 moved the endpoint geometric splice away from generic strong-`L^1` rigidity. PF-195 now performs the analogous cleanup on the analytic side: **generic critical one-sided weak-`S_2` Cwikel control cannot be inferred from the square root of the available `L^1` defect mass**.

This does not weaken PF-191. On the contrary, it identifies what any successful endpoint operator theorem must preserve: the actual integrated `d/cosh(a)` currency rather than a worst-cell `d` currency. The accepted weak-trace route remains live, but its half-factor branch is now explicitly PF-specific. The directly symmetrized weak-`S_1` branch is not merely an equivalent repackaging; current prior art gives it a different and potentially better critical coefficient scale.