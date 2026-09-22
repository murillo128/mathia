# NB-279 — Finite boundary repair collapses exactly to Hardy zero sampling

**Date:** 2026-09-22  
**Status:** `EXACT-DERIVED + FINITE-BOUNDARY-IDENTITY + HARDY-ZERO-SAMPLING + REPRODUCING-KERNEL-GRAM + NB-278-BOUNDARY-AUDIT + PRIOR-ART-AUDITED`.

`NB-278` closes the direct interior-current route: for every finite Dirichlet polynomial `P`, the differentiated canonical source

\[
\mathcal C_P(s)=-\zeta(s)\bigl(P'(s)-P'(1)\bigr)
\]

is entire, so it cannot converge across a zeta zero to the meromorphic current

\[
\mathcal C_0(s)=\frac{\zeta'}{\zeta}(s)+\zeta(s).
\]

The immediate remaining question was whether one can retain a **finite contour term before taking the singular interior-current limit**, and then estimate that term in the actual Nyman/Hardy norm.

There is an exact finite boundary identity, but it does not create a new arithmetic channel. Let

\[
\mathcal N[P](s)
=
\frac{\zeta(s)}s\bigl(P(s)-P(1)\bigr)
\]

and let the legal Nyman residual be

\[
r_P(s)
:=
\frac1s-\mathcal N[P](s).
\tag{1}
\]

At every zeta zero `\rho\ne0`,

\[
\boxed{
r_P(\rho)=\frac1\rho.
}
\tag{2}
\]

Therefore, if `\Omega\Subset\{\Re s>1/2\}` is a bounded Jordan domain whose boundary contains no zeta zero and whose closure avoids `s=1`, then

\[
\boxed{
\frac1{2\pi i}
\oint_{\partial\Omega}
 s\frac{\zeta'}{\zeta}(s)\,r_P(s)\,ds
=
N_\Omega,
}
\tag{3}
\]

where `N_\Omega` is the number of zeta zeros in `\Omega`, counted with multiplicity. More generally, for every function `q` holomorphic near `\overline\Omega`,

\[
\boxed{
\frac1{2\pi i}
\oint_{\partial\Omega}
 q(s)s\frac{\zeta'}{\zeta}(s)\,r_P(s)\,ds
=
\sum_{\rho\in\Omega}m(\rho)q(\rho).
}
\tag{4}
\]

Thus `NB-278`'s missing divisor can indeed be recovered from a **finite legal Nyman residual** on a contour. The crucial qualification is that the singular arithmetic information has moved into the dual weight `\zeta'/\zeta`. The finite source remains analytic; the test functional now carries the poles.

When the same identity is written in `H^2(\mathbb C_{1/2})`, it becomes exactly the classical point-evaluation obstruction at the zeta zeros. If `\rho_1,\ldots,\rho_n` are the distinct zeros in `\Omega`, set

\[
G_{jk}
:=
\frac1{\rho_j+\overline{\rho_k}-1},
\qquad
v_j:=\frac1{\rho_j}.
\tag{5}
\]

Then every finite Nyman residual satisfies the interpolation conditions

\[
(r_P(\rho_1),\ldots,r_P(\rho_n))=v,
\]

and hence

\[
\boxed{
\|r_P\|_{H^2(\mathbb C_{1/2})}^2
\ge
v^*G^{-1}v.
}
\tag{6}
\]

Conversely, optimizing `(4)` over holomorphic weights `q` gives no stronger linear certificate than `(6)`: on a finite set of distinct zeros, polynomial interpolation allows arbitrary values `q(\rho_j)`, so the optimized contour functional is precisely the dual formulation of the reproducing-kernel interpolation problem.

The boundary repair proposed after `NB-278` therefore **collapses exactly to Hardy zero sampling**. It is a legitimate finite bridge, but not a new source of coercivity. The remaining quantitative question is no longer whether a contour can see the divisor; it can. The question is whether the zero-sampling Gram `G` has enough inverse conditioning, for the actual Ford-scale zero geometry, to make `v^*G^{-1}v` large enough in the Nyman norm.

## 1. The legal finite residual already has fixed values at every zeta zero

For finite `P`, `(1)` can be written

\[
r_P(s)
=
\frac1s
-
\frac{\zeta(s)}s\bigl(P(s)-P(1)\bigr).
\tag{7}
\]

Let `\rho\ne0` be a zero of `\zeta`, of any multiplicity. The second term in `(7)` vanishes at `\rho`, so

\[
r_P(\rho)=\frac1\rho.
\tag{8}
\]

This identity is independent of the coefficients of `P`, its truncation length, its Hardy norm, Möbius cancellation, or the differentiated-current construction of `NB-276`--`NB-278`.

It also shows immediately why a boundary formula can recover information that the finite interior current cannot. `NB-278` says

\[
\bar\partial\mathcal C_P=0
\]

for every finite source. Equation `(8)` instead evaluates the **original legal residual** at points where the generator factor `\zeta` vanishes. No singularity needs to be created by `r_P`; the arithmetic information is encoded as a forced interpolation value.

That distinction is the entire mechanism below.

## 2. Exact finite contour identity

Let `\Omega` be as in the statement above. Consider

\[
F_P(s)
:=
s\frac{\zeta'}{\zeta}(s)r_P(s).
\tag{9}
\]

The residual `r_P` is holomorphic on a neighborhood of `\overline\Omega`. At a zero `\rho\in\Omega` of multiplicity `m(\rho)`,

\[
\frac{\zeta'}{\zeta}(s)
=
\frac{m(\rho)}{s-\rho}+O(1).
\tag{10}
\]

Using `(8)`, the residue of `(9)` is

\[
\operatorname*{Res}_{s=\rho}F_P(s)
=
m(\rho)\,\rho\,r_P(\rho)
=
m(\rho).
\tag{11}
\]

There are no other poles in `\Omega` because the only pole of `\zeta` is at `1`, which has been excluded. The residue theorem now gives `(3)` exactly.

Multiplying `(9)` by any `q` holomorphic near `\overline\Omega` changes `(11)` to

\[
\operatorname*{Res}_{s=\rho}
\left(
q(s)s\frac{\zeta'}{\zeta}(s)r_P(s)
\right)
=
m(\rho)q(\rho),
\tag{12}
\]

which proves `(4)`.

If one wants a contour containing `s=1`, the logarithmic derivative contributes the additional residue `-q(1)r_P(1)` there. It is canceled exactly by adding `q(s)r_P(1)\zeta(s)` to the integrand, whose residue at `1` is `+q(1)r_P(1)`. For the high Ford windows relevant to this line it is cleaner to keep `1` outside `\Omega`, and `(4)` is then the exact identity needed.

The important point is that `(3)`--`(4)` hold for **every finite legal source**. No infinite Dirichlet series, meromorphic continuation of `1/\zeta`, or limit through differentiated finite currents is being used.

## 3. The contour singularity lives in the dual, not in the finite source

Equation `(3)` may initially look like an escape from `NB-278`, but the analytic-class mismatch has not disappeared. It has changed sides.

The source object `r_P` is holomorphic. The factor

\[
s\frac{\zeta'}{\zeta}(s)
\tag{13}
\]

is meromorphic and already contains the complete zero divisor. In particular, the contour can count zeros because the **test functional itself** has the poles that the finite current `\mathcal C_P` lacked.

This is legitimate as a dual identity. It is not yet a Nyman lower bound. To obtain such a bound one must control the norm of this singular dual functional in the same Hardy geometry in which `r_P` is measured.

A crude contour Cauchy--Schwarz estimate makes the issue visible:

\[
N_\Omega
\le
\frac1{2\pi}
\|r_P\|_{L^2(\partial\Omega)}
\left\|
 s\frac{\zeta'}{\zeta}
\right\|_{L^2(\partial\Omega)}.
\tag{14}
\]

Shrinking or moving the contour can improve one factor only by changing the other. More importantly, the contour trace in `(14)` is not automatically controlled by the critical-line `H^2` norm with a Ford-uniform constant. The correct way to price the dual is through the reproducing kernels of the Hardy space.

## 4. Exact Hardy dual norm: the boundary identity is a zero-sampling Gram problem

Use the standard normalization

\[
\|f\|_{H^2(\mathbb C_{1/2})}^2
=
\frac1{2\pi}
\int_{-\infty}^{\infty}
|f(1/2+it)|^2\,dt.
\tag{15}
\]

For `\rho\in\mathbb C_{1/2}`, the reproducing kernel is

\[
k_\rho(s)
=
\frac1{s+\overline\rho-1},
\tag{16}
\]

so

\[
f(\rho)=\langle f,k_\rho\rangle,
\qquad
\|k_\rho\|^2
=
\frac1{2\Re\rho-1}.
\tag{17}
\]

For the distinct zero locations `\rho_1,\ldots,\rho_n`, the Gram matrix of these kernels is exactly `(5)` up to the harmless transpose convention dictated by which slot of the inner product is linear. It is positive definite.

Every finite Nyman residual obeys the interpolation vector

\[
V r_P=v,
\qquad
v_j=\frac1{\rho_j},
\tag{18}
\]

where `Vf=(f(\rho_j))_j`. The least-norm Hardy function satisfying `(18)` is the orthogonal projection onto `\operatorname{span}\{k_{\rho_j}\}` with coefficient vector `G^{-1}v`. Therefore

\[
\inf_{Vf=v}\|f\|_{H^2}^2
=
v^*G^{-1}v,
\tag{19}
\]

which proves `(6)`.

This also identifies the optimal content of the weighted contour identities. Define

\[
L_q(f)
:=
\sum_{j=1}^n
m_j q(\rho_j)\rho_j f(\rho_j).
\tag{20}
\]

Equation `(4)` says

\[
L_q(r_P)
=
\sum_{j=1}^n m_j q(\rho_j).
\tag{21}
\]

On a finite set of distinct points, a polynomial can interpolate arbitrary prescribed values of `q(\rho_j)`. Hence optimizing

\[
\frac{|L_q(r_P)|}{\|L_q\|}
\tag{22}
\]

over holomorphic `q` is just the dual optimization over all linear combinations of the point evaluations in `(18)`. Hilbert-space duality gives `(19)` again.

So the contour architecture does not manufacture an extra norm constraint beyond zero interpolation. It is an exact boundary representation of the same finite sampling geometry.

Multiplicity in `\zeta'/\zeta` merely weights the residue in `(20)`. A multiple zero also forces higher-order vanishing of `\mathcal N[P]`, hence additional derivative interpolation identities are available if one explicitly includes derivative evaluations. The logarithmic-derivative contour `(4)` by itself uses only the point-value channel; no claim is made here that `(19)` exhausts those extra higher-jet constraints at multiple zeros.

## 5. A single high zero already shows why the contour identity is not automatically coercive

For one zero `\rho=\beta+i\gamma` with `\beta>1/2`, `(17)` and `(8)` give the sharp one-point sampling bound

\[
\boxed{
\|r_P\|_{H^2}
\ge
\frac{\sqrt{2\beta-1}}{|\rho|}.
}
\tag{23}
\]

At high ordinate this is

\[
\asymp
\frac{\sqrt{2\beta-1}}{|\gamma|}.
\tag{24}
\]

Thus the mere existence of the exact finite contour identity does not produce a height-uniform floor. The arithmetic residue is order one, but the norm of the corresponding Hardy evaluation functional grows like `|\rho|/\sqrt{2\beta-1}` once the factor `\rho` required by `(11)` is included.

Several zeros can improve `(23)`, but only through the inverse geometry of `G`. The exact quantity is no longer a raw zero count, a contour length, or the `L^1` mass of a Ford packet. It is

\[
\boxed{
v^*G^{-1}v.
}
\tag{25}
\]

This is the discriminating currency left by the boundary repair.

In particular, simply placing more hypothetical zeros in a Ford-compatible region is not enough to conclude that `(25)` is large. Highly coherent reproducing kernels can make many point constraints almost redundant, while sufficiently separated or arithmetically structured samples can improve conditioning. That is precisely the kind of source-specific conditioning question that the earlier matched-packet controls deliberately did not settle.

## 6. Relation to NB-278 and to the earlier inverse-Gram findings

`NB-278` remains unchanged. Its statement is about trying to approximate the **interior meromorphic current** `\mathcal C_0` by finite differentiated currents `\mathcal C_P`; that is impossible even distributionally across a zero because every finite `\mathcal C_P` has zero `\bar\partial` current.

The present result says that retaining a boundary term before that collapse is mathematically legitimate, but the boundary term works only because its dual kernel carries `\zeta'/\zeta`. Once that dual is priced in `H^2`, the mechanism reduces to the forced values `(8)` and their reproducing-kernel Gram.

This also resembles, but is not the same as, `NB-271`. There the inverse Gram classified **resolved source-shell quadratic repairs** under the Euler anchor. Here `G` is the Gram of **target-side Hardy evaluation kernels at zeta zeros**, and the data vector is `v_j=1/\rho_j`. The two matrices live in different spaces and should not be conflated.

What they share is the structural lesson: an aggregate scalar identity becomes coercive only after the inverse conditioning of the relevant Gram geometry is paid explicitly.

## 7. Ford-scale consequence and the next discriminating calculation

The immediate proposal after `NB-278` was to derive a finite boundary/contour identity and ask whether its boundary term survives the Hardy/Nyman norm. Equations `(3)`--`(6)` answer the first half exactly and reduce the second half to a concrete matrix problem.

For any actual finite set of off-critical zeros in a Ford window, form

\[
G_{jk}
=
\frac1{\rho_j+\overline{\rho_k}-1},
\qquad
v_j=\frac1{\rho_j}.
\tag{26}
\]

The boundary route provides a useful Nyman lower bound exactly to the extent that

\[
v^*G^{-1}v
\tag{27}
\]

stays quantitatively large. If `(27)` vanishes at the relevant height/rank coupling, the contour identity is target-poor despite its exact residue. If `(27)` has an order-one floor, then the missing coercivity has been located in genuine **zero-sampling conditioning**, not in the finite differentiated current.

This is now the useful next calculation. It should be performed first on the same Ford-compatible packet geometries used as adversarial controls earlier in the line, while preserving the standing caveat that those packets are compatibility configurations, not assertions about the actual zeta zeros. After that, any positive result would still need a source-specific theorem showing that actual zeros possess the required separation/conditioning or another arithmetic regularity that forces `(27)`.

The distinction matters because local zero density alone does not determine an inverse Gram. Two configurations with the same number of zeros can have very different kernel conditioning. This is a sharper formulation of the missing arithmetic input than the earlier statement that the source must somehow provide regularity, cancellation, or uniformity.

## 8. Prior-art audit

A fresh audit checked the classical Nyman--Beurling/Báez-Duarte Hardy formulations, Burnol's zero-sensitive lower-bound work, the Hardy-space orthogonality literature around zeta zeros, and the 2026 Hardy approximation work of Manzur--Noor--Quintero. Reproducing-kernel point-evaluation bounds and the use of zeta zeros to obstruct Hardy approximation are established prior art; no novelty is claimed for those ingredients, the residue theorem, or formula `(19)` as an abstract RKHS interpolation fact.

The line-local contribution of this finding is narrower: it audits the specific boundary escape left open by `NB-278` and shows that **its optimized finite content factors exactly through the already-known zero-sampling currency**. The contour itself contributes no new coercive degree of freedom once the dual norm is priced.

The durable source anchors already present in `SOURCES.md` include Bagchi for the Hardy/Mellin Nyman formulation, Burnol for zero-sensitive approximation lower bounds, and Calderaro--Manzur--Noor--Santos for Hardy-space structure related to zeta zeros. None of the fresh sources changes a load-bearing step above, so no new durable literature dependency is added.

## 9. Adversarial audit and limitations

### 9.1 This does not prove a Ford-window lower bound

Equation `(27)` is exact but unevaluated for the actual Ford-scale zero geometry. A zero count, zero-density estimate, or compatible packet by itself does not control `G^{-1}`. Any claim of an order-one lower bound still requires a quantitative conditioning theorem.

### 9.2 The contour does not make the finite source meromorphic

All poles in `(3)`--`(4)` come from `\zeta'/\zeta`. The residual `r_P` remains holomorphic. Thus this finding does not contradict the analytic-class obstruction of `NB-278`; it identifies the only place where the missing singularity entered the boundary formulation.

### 9.3 Boundary traces are not substituted for Hardy norm without pricing the dual

The crude estimate `(14)` is diagnostic only. The actual norm statement used here is `(6)`, derived from bounded point evaluations inside `\mathbb C_{1/2}`. No unproved uniform trace estimate on moving Ford contours is assumed.

### 9.4 Zeros on the Hardy boundary are a different endpoint

The kernel formula `(16)` is for points with `\Re\rho>1/2`. If `\Re\rho=1/2`, point evaluation is a boundary operation and is not bounded on `H^2`; `(6)` is not asserted there. This is consistent with the Nyman--Beurling criterion: a proof cannot obtain RH by treating critical-line evaluation as a bounded interior functional.

### 9.5 Multiple zeros can carry higher-jet information

The logarithmic derivative has only a simple pole with residue equal to the multiplicity, so `(4)` sees a weighted point value. Because the Nyman generator contains `\zeta`, a multiple zero forces additional derivative conditions on the synthesized part. Those jet constraints may be encoded by derivative reproducing kernels, but they are outside the present boundary identity and are not needed for the simple-zero Ford audit.

## Conclusion

A finite contour repair **does exist**, so the topology obstruction of `NB-278` is not the end of the source-native route. But the repair is completely transparent: every legal finite Nyman residual already satisfies `r_P(\rho)=1/\rho`, and `\zeta'/\zeta` converts those forced values into residues on the contour.

After the dual is priced in the actual Hardy norm, the entire mechanism reduces to the zero-sampling Gram quantity

\[
v^*G^{-1}v.
\]

The next non-circular question is therefore not how to invent another contour or another finite differentiated current. It is whether the **actual Ford-scale zero geometry supplies enough reproducing-kernel conditioning** to keep this inverse-Gram quantity coercive, and which arithmetic theorem—separation, cancellation, density with uniformity, or another source-specific regularity—could force that behavior.