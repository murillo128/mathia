# PF-129 — cusp synchronization has summable inverse-volume wave weight

**Status:** `EXACT-DERIVED + NEGATIVE/BOUNDARY`. PF-122 shows that the exact prime/shift-clone one-cusp pants have a canonical deep-cusp mismatch controlled only by the adjacent first difference of the single-cuff chart-scale defects, and that these first differences are in `ell^1`. PF-125 instead chose exact isometry sufficiently deep in each cusp because asymptotic coefficient convergence on the complete surface requires the perturbation to vanish along every fixed cusp. The present calculation combines those two ideas at the scattering scale: each cusp can be synchronized through a fixed Busemann-height slab and made exactly isometric above it with Güneysu--Thalmaier inverse-unit-ball weighted cost `O(d_n)`, where `sum d_n < infinity`. Thus the **entire family of cusp ends** can be removed from the global wave-operator obstruction with finite total weight. No global wave-operator, scattering-matrix, resonance, Schatten, determinant, or RH conclusion is claimed; compatibility with the lower pant-body comparison remains a separate gate.

## Claim

Use the PF-122 normalization of the `n`th one-cusp pentagon. Above `y=1` both the exact prime pant and its exact all-composite shift-clone mate are the same standard cusp strip

\[
C=\{(x,y):0\le x\le1,\ y\ge1\},
\qquad
 g=\frac{dx^2+dy^2}{y^2}.
\tag{1}
\]

Let

\[
A_n=\cosh a_n,
\qquad
B_n=\cosh a_{n+1},
\qquad
t_n=\frac{A_n}{A_n+B_n},
\tag{2}
\]

and use `+` for the shift clone. Put

\[
\epsilon_n=\log\frac{A_n^+}{A_n},
\qquad
 d_n:=|\epsilon_n-\epsilon_{n+1}|.
\tag{3}
\]

PF-119/PF-122 prove

\[
\boxed{\sum_n d_n<\infty.}
\tag{4}
\]

There is a smooth increasing diffeomorphism

\[
\psi_n:[0,1]\to[0,1]
\tag{5}
\]

which fixes `0,1`, sends the canonical split point `t_n` to `t_n^+`, and, after changing an absolute constant on a finite head, satisfies

\[
\boxed{
\|\psi_n-\operatorname{id}\|_{L^\infty}
+
\|\psi_n'-1\|_{L^\infty}
\le C d_n.
}
\tag{6}
\]

Fix once and for all `L>1` and a smooth cutoff `eta:[0,L]->[0,1]` equal to `0` near `0` and `1` near `L`. In Busemann coordinates `r=log y`, define on `0<=r<=L`

\[
\boxed{
F_n(x,r)=
\bigl((1-\eta(r))\psi_n(x)+\eta(r)x,\ r\bigr),
}
\tag{7}
\]

and set `F_n(x,r)=(x,r)` for `r>=L`. Then `F_n` fixes the two physical outer cusp rays, has the desired split-point trace at `r=0`, and is an exact hyperbolic isometry for `r>=L`. Moreover

\[
\boxed{
\log\operatorname{Bilip}(F_n)\le C_L d_n
}
\tag{8}
\]

on the tail.

Let

\[
h_n:=F_n^*g
\]

and let `delta_{g,h_n}` be the zeroth-order metric deviation used by Güneysu--Thalmaier. Then the contribution of the complete `n`th cusp to their inverse-unit-ball-volume weight satisfies

\[
\boxed{
\int_C
\mu_g(B_g(z,1))^{-1}
\delta_{g,h_n}(z)\,d\mu_g(z)
\le C_L d_n.
}
\tag{9}
\]

The same estimate holds, with another fixed constant, using `h_n` in the ball-volume weight. Consequently

\[
\boxed{
\sum_n
\int_C
\mu_g(B_g(z,1))^{-1}
\delta_{g,h_n}(z)\,d\mu_g(z)
<\infty.
}
\tag{10}
\]

Thus infinitely many cusps do **not** force divergence of the no-injectivity-radius scattering criterion for the prime/shift comparison. Any remaining failure must come from the bounded-height pant bodies, their interfaces with the synchronized cusps, non-cusp thin components, or the global assembly of those pieces.

## 1. PF-122 gives a uniformly small boundary trace

PF-122 constructs the piecewise-affine cusp map `phi_n` with slopes

\[
m_L=\frac{t_n^+}{t_n},
\qquad
m_R=\frac{1-t_n^+}{1-t_n},
\tag{11}
\]

and proves the exact bound

\[
|\log m_L|,
|\log m_R|
\le d_n.
\tag{12}
\]

For `d_n` small this implies

\[
|m_L-1|+|m_R-1|\le C d_n.
\tag{13}
\]

Since `phi_n(0)=0`, `phi_n(1)=1` and `phi_n(t_n)=t_n^+`, (13) also gives

\[
\|\phi_n-\operatorname{id}\|_\infty\le C d_n.
\tag{14}
\]

The corner at `t_n` is only an artifact of choosing a piecewise-affine interpolation. Smooth the derivative transition in an arbitrarily small interval around `t_n`, rescaling that interval when `t_n` approaches `0` or `1`, and adjust the two smooth pieces so that the integral constraints and the value `psi_n(t_n)=t_n^+` are retained. Because both one-sided slopes already lie in `[e^{-d_n},e^{d_n}]`, this smoothing can be chosen with

\[
e^{-C d_n}\le\psi_n'\le e^{C d_n}
\tag{15}
\]

and (6). No bound on `psi_n''` is needed for the zeroth-order metric comparison below. A finite initial set of cusps can be treated by arbitrary smooth label-preserving maps and contributes only a finite amount.

The important arithmetic/geometric input is therefore not the nonsummable common scale `epsilon_n`, but the first difference `d_n`. If `epsilon_n=epsilon_{n+1}`, then PF-122 gives `t_n^+=t_n` and the cusp trace can be the identity even though the common chart scale is nonzero.

## 2. A fixed Busemann slab removes the perturbation exactly at infinite depth

In coordinates `r=log y`, the cusp metric is

\[
\boxed{g=dr^2+e^{-2r}dx^2.}
\tag{16}
\]

Write the first component of (7) as `X_n(x,r)`. Its derivatives are

\[
\partial_xX_n
=1+(1-\eta(r))(\psi_n'(x)-1),
\tag{17}
\]

and

\[
\partial_rX_n
=\eta'(r)(x-\psi_n(x)).
\tag{18}
\]

By (6), uniformly on the fixed slab,

\[
|\partial_xX_n-1|\le C d_n,
\qquad
 e^{-r}|\partial_rX_n|\le C_L d_n.
\tag{19}
\]

In the orthonormal frame `(e^r partial_x, partial_r)`, the differential of `F_n` is therefore `I+O_L(d_n)`. For large `n` it is orientation preserving and gives (8). The transported metric eigenvalues and volume-density ratio are consequently `1+O_L(d_n)`, so the Güneysu--Thalmaier deviation obeys

\[
\boxed{
\delta_{g,h_n}(z)\le C_L d_n
\qquad (0\le r\le L),
}
\tag{20}
\]

while it vanishes identically for `r>=L`.

This exact cutoff is essential. A nontrivial horizontal cusp distortion kept for all Busemann heights would generally have infinite inverse-volume weighted mass even if its amplitude were arbitrarily small, because unit-ball volumes collapse linearly with the cusp circumference. The construction avoids that issue rather than trying to dominate it.

## 3. The inverse-volume penalty is harmless on a fixed-height slab

On the standard width-one cusp, for `0<=r<=L` the circumference of the horocycle is at least `e^{-L}`. A fixed sufficiently small hyperbolic rectangle around every point of this slab therefore lies inside its ambient unit ball and has area bounded below by a constant `c_L>0`. Hence

\[
\mu_g(B_g(z,1))^{-1}\le c_L^{-1}
\qquad (0\le r\le L).
\tag{21}
\]

The slab itself has finite uniformly bounded area,

\[
\mu_g\{0\le r\le L\}
=\int_0^L e^{-r}\,dr
<1.
\tag{22}
\]

Combining (20)--(22), and using that the deviation is zero above the slab, proves (9). Equation (8) gives a uniform tail quasi-isometry; therefore the corresponding target unit-ball volumes are comparable by a constant depending only on `L` and a finite head bound, proving the symmetric version as well.

Finally (4) turns the per-cusp estimate into the global summability statement (10).

## 4. Relation to PF-125 and PF-128

PF-125 solved a different problem: it built a complete marked homeomorphism whose transported metric tends to the prime metric in the ordinary Frechet sense at infinity, including along every fixed cusp, and hence obtained compact relative resolvent through PF-123. Its generic pantwise bound is `1+O(1/p_n)`, which is not an `ell^1` budget and therefore cannot by itself prove a global scattering integral.

PF-129 isolates a better normalization specifically for the cusp ends. PF-122 shows that their genuine marked mismatch is the **summable differential mode** `d_n`, and the finite-height cutoff above converts that mode into a finite total Güneysu--Thalmaier weight while retaining exact isometry at infinite depth.

PF-128 addresses the other obvious collapse mechanism: a full standard collar around a matched short canonical separator has inverse-volume weighted cost `O(|log(L_+/L)|)`, which PF-109 improves to `O(P^-3)`. The two findings are complementary:

```text
cusps:
    adjacent chart-scale difference d_n in ell^1
    -> exact deep isometry with total finite wave weight

canonical short collars:
    log core-length mismatch O(P^-3)
    -> no collapse amplification of the local wave weight
```

What remains is not the mere existence of infinitely many cusps or the unbounded width of canonical pinching collars. The unresolved global gate is to reconcile these optimized thin-part maps with the bounded-height pant-body comparison and to control every remaining Margulis-thin component and interface in one smooth complete marking.

## 5. Prior art and novelty audit

No novelty is claimed for cutoff interpolation on a standard cusp, for the elementary lower bound on unit-ball area over a compact Busemann-height slab, or for the general scattering theorem.

Batu Güneysu and Anton Thalmaier, *Scattering theory without injectivity radius assumptions, and spectral stability for the Ricci flow*, Ann. Inst. Fourier 70 (2020), 437--456, DOI `10.5802/aif.3316`, prove an integral criterion for existence and completeness of wave operators for quasi-isometric complete metrics without an injectivity-radius lower bound. Under the lower-Ricci specialization used throughout this branch, the relevant geometric penalty is controlled by the inverse volume of a unit ball. Their theorem is general prior art; PF-129 does not strengthen it.

The project-specific content is only the composition

\[
\boxed{
\text{PF-122 exact cusp trace}
+
\sum_n|\epsilon_n-\epsilon_{n+1}|<\infty
+
\text{finite-height exact-isometry cutoff}
\Longrightarrow
\text{finite total cusp contribution to the wave weight}.}
\]

Directed checks found the general no-injectivity-radius scattering criterion and standard cusp geometry, but no prior source for this cotangent prime/shift-clone specialization. That specialization is useful as a **negative boundary**: a successful wave-operator comparison would also hold against an exact all-composite control, so cusp-end scattering regularity cannot be a primality selector by itself.

## 6. Audit / falsification core

A later review can check PF-129 through the following finite chain:

1. verify PF-122's exact slope formulas and `|log m_L|,|log m_R|<=d_n`;
2. use PF-119/PF-122 to verify `sum d_n<infinity` for the exact shift clone;
3. smooth the piecewise-affine trace while retaining endpoints, split-point image and the `C^1` bound (6);
4. differentiate the fixed-height interpolation (7) in the cusp orthonormal frame and obtain `dF_n=I+O_L(d_n)`;
5. note that the map is exactly the identity for `r>=L`;
6. establish the uniform unit-ball lower bound only on the compact-height slab `0<=r<=L`, where no injectivity-radius degeneration occurs;
7. integrate the Güneysu--Thalmaier zeroth-order deviation to obtain `O(d_n)` and sum over cusps;
8. do **not** infer global wave operators until the lower pant-body/interface map and all remaining thin components are controlled in the same smooth complete comparison.

A refutation would have to break the PF-122 first-difference bound, the smooth boundary interpolation with uniform first-derivative control, or the fixed-slab weighted estimate. Failure of the later body/gluing problem would not refute PF-129; it would identify the remaining global mechanism explicitly excluded here.