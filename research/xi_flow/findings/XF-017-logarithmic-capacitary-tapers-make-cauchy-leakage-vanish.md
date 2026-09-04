# XF-017 — logarithmic capacitary tapers make Cauchy leakage vanish across diverging buffers

**Status:** `EXACT-DERIVED` + `CLASSICAL-CAPACITY-BRIDGE` + `STRUCTURAL/BOUNDARY`. XF-016 showed that a fixed-shape self-similar cutoff cannot make the inverse-square localization leakage lower order: in one dimension the `H^{1/2}` cost is scale invariant. That obstruction is sharp with respect to the ratio of inner and outer scales. If the cutoff is allowed to relax over a buffer whose scale ratio tends to infinity, a logarithmic capacitary profile has Cauchy localization cost `O(1/log R)`, and hence there are discrete tapers whose leakage tends to zero.

The gain is not produced by ordinary dilation. It comes from adding an independent outer scale. Thus criticality does not say that the boundary cost can never vanish; it says that a **fixed scale ratio cannot provide the small parameter**. For the Xi-flow program this replaces the cutoff no-go of XF-016 by a more precise requirement: any localization route based only on the Cauchy geometry must control the gap field on a buffer whose outer/inner ratio diverges.

## 1. Continuum logarithmic taper

For `R>1`, define the even compactly supported cutoff

\[
\psi_R(x)=
\begin{cases}
1,& |x|\le1,\\[2mm]
\displaystyle\frac{\log(R/|x|)}{\log R},&1<|x|<R,\\[3mm]
0,&|x|\ge R.
\end{cases}
\tag{1}
\]

Let

\[
\mathcal J(f)
:=\int_{x<y}\frac{(f(x)-f(y))^2}{(x-y)^2}\,dx\,dy
\tag{2}
\]

be the continuum Cauchy localization form appearing as the limit of XF-016.

To estimate (2), work in the upper half-plane and put `r=sqrt(x^2+y^2)`. The radial function

\[
U_R(x,y)=
\begin{cases}
1,&r\le1,\\[1mm]
\displaystyle\frac{\log(R/r)}{\log R},&1<r<R,\\[3mm]
0,&r\ge R
\end{cases}
\qquad(y\ge0)
\tag{3}
\]

has boundary trace `psi_R`. Its Dirichlet energy is explicit:

\[
\begin{aligned}
\int_{\mathbb H}|\nabla U_R|^2\,dx\,dy
&=\int_0^\pi\int_1^R
\frac{1}{r^2\log^2R}\,r\,dr\,d\theta\\
&=\boxed{\frac{\pi}{\log R}}.
\end{aligned}
\tag{4}
\]

For the harmonic extension `P psi_R`, the classical half-Laplacian/Douglas trace identity gives, with the normalization in (2),

\[
\mathcal J(\psi_R)
=\pi\int_{\mathbb H}|\nabla P\psi_R|^2\,dx\,dy.
\tag{5}
\]

The harmonic extension minimizes Dirichlet energy among extensions with the same trace. Using (3) as a competitor therefore yields the explicit bound

\[
\boxed{
\mathcal J(\psi_R)\le\frac{\pi^2}{\log R}.
}
\tag{6}
\]

No asymptotic theorem is needed for (6): the only imported ingredient is the classical `H^{1/2}` trace/extension identity. The logarithmic profile and its energy are computed directly.

## 2. Discrete Cauchy cutoffs inherit the logarithmic gain

For an integer scale `N`, sample (1) by

\[
\psi_i^{(N,R)}:=\psi_R(i/N),
\qquad i\in\mathbb Z,
\tag{7}
\]

and define the exact lattice cutoff cost

\[
J_{N,R}:=
\sum_{i<k}
\frac{(\psi_i^{(N,R)}-\psi_k^{(N,R)})^2}{(i-k)^2}.
\tag{8}
\]

The sequence equals one on `|i|<=N` and vanishes on `|i|>=RN`. For each fixed `R`, the compactly supported Lipschitz integrand in (8), including its integrable tail when one variable lies outside the support, is a Riemann discretization of (2). Hence

\[
\boxed{
J_{N,R}\longrightarrow \mathcal J(\psi_R)
\qquad(N\to\infty,\ R\text{ fixed}).
}
\tag{9}
\]

Combining (6) and (9),

\[
\limsup_{N\to\infty}J_{N,R}
\le\frac{\pi^2}{\log R}.
\tag{10}
\]

This already proves the existence of a genuinely lower-order localization family. For example, take `R_m=e^m`; after choosing `N_m` large enough that the discretization error in (9) is at most `1/m`,

\[
J_{N_m,R_m}\le\frac{\pi^2+1}{m}\to0.
\tag{11}
\]

Equivalently, by a standard diagonal choice there is a slowly diverging scale ratio `R_N -> infinity` for which

\[
\boxed{J_{N,R_N}\to0.}
\tag{12}
\]

This is precisely what a fixed-shape taper in XF-016 could not achieve.

## 3. The arithmetic-lattice leakage becomes `o(1)`

On the arithmetic-lattice linearization, XF-016 writes the leakage as

\[
R_N(\psi,u)
=\sum_{i<k}\frac{(\psi_i-\psi_k)^2u_i u_k}{(i-k)^2}.
\tag{13}
\]

If `|u_i|<=B`, then directly

\[
|R_N(\psi,u)|\le B^2J_{N,R}.
\tag{14}
\]

Therefore the diagonal family from (12) satisfies

\[
\boxed{|R_N(\psi,u)|=o(1)}
\tag{15}
\]

uniformly over bounded perturbations. The useful inner plateau still has `2N+1` sites; the vanishing cost is paid by expanding the support to order `R_N N` sites.

This gives a decisive stress test of the interpretation of XF-016. The scale-critical `H^{1/2}` geometry forbids an `o(1)` error under **self-similar dilation**, but it does not forbid `o(1)` localization when a diverging buffer ratio is available. The fixed-ratio obstruction and the logarithmic-capacity escape are fully compatible.

## 4. What survives for the exact nonlinear conductances

For the exact gap equation of XF-014, the leakage is

\[
2\sum_{i<k}c_{ik}(\psi_i-\psi_k)^2v_iv_k,
\qquad v_i=g_i-h.
\tag{16}
\]

Whenever the interactions contributing to (16) satisfy the two bounds

\[
h^2c_{ik}\le\frac1{m^2(i-k)^2},
\qquad
|v_i|\le Bh,
\tag{17}
\]

one gets

\[
\left|2\sum_{i<k}c_{ik}(\psi_i-\psi_k)^2v_iv_k\right|
\le\frac{2B^2}{m^2}J_{N,R}.
\tag{18}
\]

Thus the capacitary gain is compatible with the nonlinear flow **if** a sufficiently broad two-sided control regime is already available. This hypothesis is deliberately stated at the pair level. Because `(psi_i-psi_k)^2` remains nonzero when one index lies outside the support, a local envelope only on the visible support does not automatically justify (17) for the full infinite-system leakage. The far tail must be estimated separately or incorporated into a stronger global/renormalized argument.

This is an important distinction from XF-015. Its lower bulk coercivity needed only an upper gap envelope: small gaps increase conductances. An **upper bound on leakage**, by contrast, needs control preventing conductances from becoming arbitrarily large, or some signed cancellation that avoids taking absolute values. The capacitary taper solves the geometric cutoff cost; it does not supply that missing Xi-specific exterior information.

## 5. The vanishing cost comes with a storage/buffer price

The logarithmic taper is broad. Its continuum `L^2` mass satisfies

\[
\begin{aligned}
\int_{\mathbb R}\psi_R(x)^2\,dx
&=2+\frac{2R}{\log^2R}
\int_0^{\log R}s^2e^{-s}\,ds\\
&\sim\boxed{\frac{4R}{\log^2R}}.
\end{aligned}
\tag{19}
\]

Consequently

\[
\sum_i\bigl(\psi_i^{(N,R)}\bigr)^2
\asymp \frac{NR}{\log^2R}
\tag{20}
\]

when `N` and `R` are large in the Riemann regime. The small leakage is therefore not free: the localized entropy samples an increasingly large outer buffer. A proof that only knows the inner `N`-gap block cannot insert (12) and declare the boundary solved.

At the Xi fixed-time scale `N~h^{-2}~log^2 T`, the geometric message is nevertheless favorable. One may let `R=R(T)` diverge arbitrarily slowly, so the outer window can remain only mildly larger than the mesoscopic core while the pure Cauchy cutoff cost tends to zero. The new burden is to propagate legitimate gap/conductance or signed-correlation control across that diverging-ratio buffer.

## 6. Prior art and novelty boundary

The extension representation of `(-Delta)^{1/2}` by harmonic functions in the upper half-space is classical; Caffarelli and Silvestre give the standard modern fractional-Laplacian formulation. The Douglas/trace identity identifying boundary `H^{1/2}` energy with harmonic Dirichlet energy is likewise classical. No novelty is claimed for critical capacity, logarithmic cutoffs, harmonic-extension minimization, or the `1/log R` energy law as an abstract analytic phenomenon.

The Mathia contribution here is the consequence for the exact obstruction exposed by XF-016: **the Cauchy boundary leakage has a capacitary escape once the inner/outer scale ratio is allowed to diverge, and the required price can be stated explicitly as a growing buffer rather than as an impossible fixed-shape estimate.** A targeted literature check found the underlying capacity mechanism to be standard and did not identify a Xi-flow theorem that already supplies the broad nonlinear envelope needed by (17); absence from that search is not used as novelty evidence.

The matched-control test remains decisive. Arithmetic lattices and synthetic one-dimensional logarithmic-repulsion systems share the same capacitary localization mechanism. It is not an Xi-specific selector and does not by itself upper-bound `Lambda`.

## 7. Consequence for `xi_flow`

XF-016 ruled out the simplest smooth-taper repair of the nonlinear boundary flux. XF-017 shows exactly how that no-go can be escaped geometrically: **replace a fixed-shape cutoff by a logarithmic taper with a diverging outer/inner scale ratio.** The pure inverse-square leakage then falls at least as fast as `1/log R` along an explicit discrete family.

The research frontier is therefore no longer whether critical `H^{1/2}` localization can ever have a vanishing boundary cost. It can. The hard Xi-specific question is whether unconditional information in the real-simple regime can control the amplitudes and conductances, or provide enough signed cancellation, throughout a buffer growing from `N~log^2 T` to `R(T)N` with `R(T)->infinity`. If that broad-buffer input can be supplied, the boundary obstruction of XF-016 is not fundamental; if it cannot, the failure is arithmetic/exterior-information loss rather than fractional scale criticality itself.
