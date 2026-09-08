# PF-230 — hyperbolic corridor has a `pi/s` axis inverse-width budget

**Status:** `EXACT-DERIVED + HYPERBOLIC-GEOMETRY + GEOMETRIC-CALIBRATION + POSITIVE/ROUTE-NARROWING`. PF-215 gives the exact Fermi graph of one finite cuff axis over its neighboring cuff axis inside the canonical thin one-cusp pant. PF-226/PF-227 use a fixed central part of that geometry to prove order `s_n^{-1}` raw channel multiplicity, while PF-228 deliberately replaces the pant by a pessimistically periodized straight corridor whose control count can be as large as `O(L_n/s_n)`. The exact hyperbolic graph yields a sharper geometric calibration.

If two ultraparallel geodesics have common-perpendicular distance `s>0`, write the second one as a Fermi graph `r=r_s(t)` over the first, with `t=0` at the common perpendicular. PF-215 records

\[
\sinh r_s(t)
=
\frac{\sinh s}
{\sqrt{1-\cosh^2s\,\tanh^2t}}.
\tag{1}
\]

This simplifies exactly to

\[
\boxed{\tanh r_s(t)=\tanh s\,\cosh t,}
\tag{2}
\]

on the maximal graph interval

\[
|t|<T_s,
\qquad
\boxed{T_s=\operatorname{arcosh}(\coth s)
      =\operatorname{arsinh}(\operatorname{csch}s)
      =\log\coth(s/2).}
\tag{3}
\]

Hence `T_s=\log(2/s)+O(s^2)`, but on every fixed tangential window

\[
\boxed{\frac{r_s(t)}s\longrightarrow\cosh t}
\tag{4}
\]

locally uniformly as `s\downarrow0`. The scaled axis-to-axis corridor therefore retains an order-one variable-width profile; a constant-width flat strip is **not** an asymptotically exact geometric perturbation on any fixed nontrivial `t`-window.

The same conclusion survives the PF-205 natural-width trimming on fixed windows. If the two pant-facing artificial boundaries are at normal distances `\rho_1,\rho_2` from the two cuffs, then along the first cuff's normal ray the second artificial boundary is exactly at

\[
R_{s,\rho_2}(t)
=
r_s(t)-
\operatorname{arsinh}\!\left(
\frac{\sinh\rho_2}{\cosh s}\cosh r_s(t)
\right),
\tag{5}
\]

so the remaining ray length is

\[
\ell_{s,\rho_1,\rho_2}(t)=R_{s,\rho_2}(t)-\rho_1.
\tag{6}
\]

For `\rho_i=O(s)` and fixed `|t|\le T`,

\[
\boxed{
\ell_{s,\rho_1,\rho_2}(t)
=
s\cosh t-\rho_1-\rho_2+O_T(s^3).
}
\tag{7}
\]

In the canonical PF-205 choice `w_j=\kappa d_j` with fixed sufficiently small `\kappa<1/4` and `\rho_j=\operatorname{arsinh}w_j`, the exact PF scales imply

\[
\frac{\rho_n+\rho_{n+1}}{s_n}\le \kappa+o(1)<1
\tag{8}
\]

after a finite head. Thus the actual trimmed central corridor remains uniformly `s_n`-thin but its scaled width still has the nonconstant `\cosh t` fanout on fixed windows.

There is also a useful exact calibration for the **untrimmed axis graph**. For every fixed `A>1`, the part with `r_s(t)\le As` has tangential length tending to `2\operatorname{arcosh}A`, even though the maximal graph interval has length `2T_s\asymp\log(1/s)`. Moreover, defining

\[
M_{\rm axis}(s):=
\int_{-T_s}^{T_s}\frac{dt}{r_s(t)},
\tag{9}
\]

one has

\[
\boxed{sM_{\rm axis}(s)\longrightarrow\pi,}
\qquad
\boxed{M_{\rm axis}(s)=\frac{\pi+o(1)}s.}
\tag{10}
\]

So the complete **axis-to-axis** Fermi graph has inverse-width scale `1/s`, not `\log(1/s)/s`. This is a geometric calibration only. The PF-205 trimmed interfaces, normalized DtN operators, physical `P/H` projections, global Schur inverse, and nested cut reassembly can change operator counting and are not bounded by (10) without a new theorem.

## Claim

Let `\gamma_0,\gamma_s\subset\mathbb H^2` be disjoint geodesics with common-perpendicular distance `s>0`. Use Fermi coordinates `(r,t)` around `\gamma_0`, so

\[
g=dr^2+\cosh^2r\,dt^2,
\tag{11}
\]

and normalize `t=0` at the common perpendicular. Let `r_s(t)` denote the graph of `\gamma_s` over `\gamma_0` on its maximal Fermi interval. Then:

1. `r_s` satisfies the exact identities (2)--(3).
2. For every fixed `T<\infty`,
   \[
   r_s(t)=s\cosh t+O_T(s^3)
   \quad(|t|\le T).
   \tag{12}
   \]
3. If inward equidistant boundaries are taken at `\rho_1,\rho_2=O(s)`, then (5)--(7) hold wherever the second boundary is reached by the first Fermi normal ray.
4. For each fixed `A>1`,
   \[
   \{t:r_s(t)\le As\}
   =
   \left\{|t|\le
   \operatorname{arcosh}\!\left(\frac{\tanh(As)}{\tanh s}\right)\right\},
   \tag{13}
   \]
   whose length tends to `2\operatorname{arcosh}A`.
5. The axis inverse-width integral (9) satisfies (10).

When `\gamma_0,\gamma_s` are the neighboring finite cuff axes of PF-215, these conclusions apply with `s=s_n=(h_n+h_{n+1})/2`; (5)--(8) apply to the PF-205 natural-width seam offsets on every fixed central window.

## 1. Exact simplification of the PF-215 graph

Starting from (1), use

\[
1-\cosh^2s\,\tanh^2t
=
\frac{1-\sinh^2s\,\sinh^2t}{\cosh^2t}.
\tag{14}
\]

Hence

\[
\sinh r_s(t)
=
\frac{\sinh s\,\cosh t}
{\sqrt{1-\sinh^2s\,\sinh^2t}}.
\tag{15}
\]

Adding one and using `\cosh^2t-\sinh^2t=1` gives

\[
\cosh r_s(t)
=
\frac{\cosh s}
{\sqrt{1-\sinh^2s\,\sinh^2t}}.
\tag{16}
\]

Dividing (15) by (16) proves (2). The graph exists exactly while the right side of (2) is below one, which gives (3). The small-`s` expansion of `\coth(s/2)` gives

\[
T_s=\log(2/s)+O(s^2).
\tag{17}
\]

Equation (2) is equivalently

\[
r_s(t)=\operatorname{artanh}(\tanh s\,\cosh t).
\tag{18}
\]

On fixed `|t|\le T`, `\tanh s=s+O(s^3)` and `\operatorname{artanh}x=x+O(x^3)`, proving (12).

## 2. Exact natural-width offset formula on fixed windows

In the hyperboloid model compatible with the PF-215 Fermi coordinates, the signed distance `d_s(r,t)` to the second geodesic satisfies

\[
\sinh d_s(r,t)
=
\cosh s\,\sinh r
-
\sinh s\,\cosh r\,\cosh t.
\tag{19}
\]

The zero set of (19) is exactly (2). Using (15)--(16), the right side factorizes as

\[
\cosh s\,\sinh r
-
\sinh s\,\cosh r\,\cosh t
=
\frac{\cosh s}{\cosh r_s(t)}
\sinh(r-r_s(t)).
\tag{20}
\]

The pant-facing equidistant curve at distance `\rho_2` from the second cuff has signed distance `-\rho_2`. Setting (20) equal to `-\sinh\rho_2` gives (5) exactly. Subtracting the first inward offset `\rho_1` gives (6).

If `\rho_i=O(s)` and `|t|\le T`, equations (12), `\cosh r_s/\cosh s=1+O_T(s^2)`, and the Taylor expansions of `\sinh`/`\operatorname{arsinh}` give

\[
\operatorname{arsinh}\!\left(
\frac{\sinh\rho_2}{\cosh s}\cosh r_s(t)
\right)
=\rho_2+O_T(s^3),
\tag{21}
\]

which proves (7).

For PF-205, `w_j=\kappa d_j`, `\rho_j=\operatorname{arsinh}w_j`, `d_j=P_j^{-1}(1+o(1))`, and `h_j=g_jP_j^{-1}(1+o(1))`. Since every odd-prime gap is at least two and `P_{n+1}/P_n\to1`,

\[
\frac{\rho_n}{s_n}\le\frac\kappa2+o(1),
\qquad
\frac{\rho_{n+1}}{s_n}\le\frac\kappa2+o(1),
\tag{22}
\]

which proves (8). In particular the natural-width smoothing does not flatten the `\cosh t` profile or consume the central corridor.

## 3. Minimum-scale axis width is bounded

By monotonicity of `\tanh`, for fixed `A>1`,

\[
r_s(t)\le As
\iff
\tanh s\,\cosh t\le\tanh(As),
\tag{23}
\]

which proves (13). Since

\[
\frac{\tanh(As)}{\tanh s}\longrightarrow A,
\tag{24}
\]

continuity of `\operatorname{arcosh}` gives the limiting length `2\operatorname{arcosh}A`.

This statement concerns the untrimmed axis graph. It shows exactly why a logarithmically long maximal Fermi interval is not the same thing as a logarithmically long region of minimum thickness.

## 4. Exact axis inverse-width asymptotic

Extend

\[
f_s(t):=
\begin{cases}
\displaystyle \frac{s}{r_s(t)},& |t|<T_s,\\
0,& |t|\ge T_s
\end{cases}
\tag{25}
\]

onto all of `\mathbb R`. For every fixed `t`, eventually `|t|<T_s`, and (12) gives

\[
f_s(t)\longrightarrow\operatorname{sech}t.
\tag{26}
\]

For domination, `\operatorname{artanh}x\ge x` on `[0,1)`, so from (18)

\[
r_s(t)
\ge
\tanh s\,\cosh t.
\tag{27}
\]

Therefore

\[
0\le f_s(t)
\le
\frac{s}{\tanh s}\operatorname{sech}t.
\tag{28}
\]

The factor `s/\tanh s` is uniformly bounded near zero, while `\operatorname{sech}t` is integrable. Dominated convergence yields

\[
\lim_{s\downarrow0}sM_{\rm axis}(s)
=
\int_{\mathbb R}\operatorname{sech}t\,dt
=\pi,
\tag{29}
\]

which proves (10).

The constant `\pi` is mainly an audit check. No Weyl law, DtN singular-value count, or operator ideal follows from (29) alone.

## 5. Relation to the current weak-trace frontier

PF-226 proves a lower bound of order `s_n^{-1}` raw channels by using a fixed central window. PF-230 explains why the **axis geometry** naturally singles out the same inverse-seam scale: the minimum-scale part of the maximal graph has bounded tangential width, and its complete axis inverse-width integral is only order `s_n^{-1}`.

PF-228 intentionally used a stronger control: a straight cylinder periodized with `\mathcal L_n=O(\log P_n)`, producing an allowed counting budget `O(\mathcal L_n/s_n)`. That theorem remains valid and useful because it proves weak-trace compatibility even for this pessimistic enlarged population. PF-230 does **not** replace that operator count by `O(s_n^{-1})`; the natural-width trim and normalized boundary operators still require their own comparison. PF-229 likewise remains a scalar serial control and is unaffected.

What PF-230 does rule out is a naive perturbative route that says the actual fixed-window geometry becomes a constant-width strip solely because `s_n\to0`. Equation (7) shows the correct fixed-window leading profile after the actual PF-205 trimming is `\cosh t` minus the two normalized offset ratios. Any dressed comparison must either analyze that variable profile or prove a transformation under which it becomes harmless.

## 6. Prior-art and novelty audit

No novelty is claimed for Fermi coordinates, equidistant curves, right-angled hyperbolic pants/hexagon geometry, or the elementary hyperbolic identities used above. Equation (1) was already derived and persisted in PF-215; equations (2)--(10) and the offset factorization (19)--(21) are direct consequences of that exact local geometry.

A structure-directed literature check found the standard variable-width thin-domain spectral literature, including Leonid Friedlander and Michael Solomyak, *On the spectrum of the Dirichlet Laplacian in a narrow strip*, Israel Journal of Mathematics 170 (2009), 337--354, DOI `10.1007/s11856-009-0032-y`. That work is relevant methodological prior art because it makes the width profile load-bearing in thin-strip spectral asymptotics. It does **not** provide the normalized cross-boundary DtN estimate, hyperbolic pant comparison, reciprocal-prime weighting, or weak-ideal statement needed here, and no theorem from it is imported into this derivation.

The project-specific durable content is therefore modest but precise: the PF-215 axis corridor has an exact `cosh` scaled profile and a `\pi/s` axis inverse-width integral, while the PF-205 natural-width trimming preserves a nonconstant variable profile on every fixed central window. No claim of a new general hyperbolic-geometry theorem is made.

## 7. Falsification and boundary checks

1. Equation (10) concerns the **untrimmed neighboring cuff axes**. It is not an upper bound for the inverse-width integral after PF-205 trimming, because moving the interfaces inward decreases the corridor width.
2. Equations (5)--(8) apply the actual PF-205 trimming only on fixed central Fermi windows where the second artificial boundary is reached by the first normal-ray foliation. They do not describe the whole cusp-side pant core.
3. An inverse-width integral is a geometric calibration, not a singular-value counting theorem for `B_n`, `P[D,E_n]H`, a DtN map, or any dressed operator.
4. Local metric flatness and variable boundary profile are deliberately separated. The metric coefficients approach Euclidean ones when `r=O(s)`, but equations (4) and (7) prevent replacing the opposite boundary by one constant line uniformly on a fixed nonzero window.
5. PF-228's `O(\mathcal L_n/s_n)` periodized control population remains a valid deliberately pessimistic model. PF-230 does not prove that the actual operator has only `O(s_n^{-1})` singular channels.
6. No prime-specific spectral separation follows. The same local hyperbolic geometry applies to matched non-prime controls with the same seam scale.
7. Nothing here proves weak `S_1`, wave-operator completeness, scattering/determinant/resonance control, or any RH implication.

## Consequences for the research line

The actual-PF one-cut frontier is narrower in a useful way. A constant-width flat cylinder is too crude to be justified as an asymptotically exact geometric model of the whole central pant window: after the real natural-width seam trimming, the leading fixed-window profile is still variable. At the same time the untrimmed axis geometry provides no independent reason to expect an extra logarithmic supply of minimum-scale width; its exact inverse-width calibration is `\pi/s+o(1/s)`.

Accordingly, the next useful comparison is a **variable-profile dressed DtN/Poisson estimate** that respects the exact hyperbolic fanout and the PF-205 artificial boundaries. PF-226/PF-227 remain the raw lower controls, PF-228/PF-229 remain favorable dressed controls, and PF-230 identifies a more faithful geometric leading model without pretending to solve the operator problem. The nested weak-`S_1` reassembly remains a separate gate even if that one-cut comparison succeeds.