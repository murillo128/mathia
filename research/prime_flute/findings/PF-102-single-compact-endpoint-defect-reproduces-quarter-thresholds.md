# PF-102 — a single compact endpoint defect reproduces the quarter-plane thresholds

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for interpreting the `Re s = 1/4` boundaries of PF-084/PF-087 as consequences of prime-gap fluctuations at infinity or of the exact cotangent deformation along the tail.

## Claim

PF-088 already showed that the quarter-plane boundary survives replacing the primes by the featureless integer lattice while keeping the cotangent deformation `V(x)=pi cot(pi/x)`. There is a stronger control.

Start from the completely regular endpoint sequence

\[
x_n^0=n.
\]

Move **one** endpoint and leave every other endpoint unchanged:

\[
 x_n^{\delta}=
 \begin{cases}
 n+\delta,&n=m,\\
 n,&n\ne m,
 \end{cases}
 \qquad 0<|\delta|<\frac12.
\tag{1}
\]

This is still an ordered zero-twist flute endpoint sequence. It can moreover be realized by a smooth compactly supported increasing deformation of the real coordinate, so the control is not a discontinuous combinatorial trick.

For this one-defect surface, both canonical sectors that produced the quarter boundary satisfy the same sharp transition as PF-084/PF-087:

\[
\boxed{
\operatorname{Re}s>\frac14
}
\]

is exactly the ordinary absolute-convergence / trace-class regime, while at and below `1/4` the fixed defect propagated to arbitrarily distant channels already forces divergence or non-boundedness.

Thus the quarter threshold needs neither

- prime sampling;
- prime-gap fluctuations;
- the cotangent map on the tail;
- an infinite family of endpoint defects.

A **single compact local defect plus one-dimensional long-channel propagation** is sufficient.

Consequently the `1/4` boundary itself cannot be used as evidence for an RH-relevant prime-flute mechanism. Any remaining information in PF-084/PF-087 must lie beyond that boundary exponent: in genuinely prime-dependent coefficients, a canonical subtraction of this propagation background, non-direct scattering, or a full spectral object not reducible to the selected channel family.

## 1. Minimal lattice control

Let the reference endpoints be `x_n^0=n`, and perturb only `x_m` as in (1). All reference gaps are one. The two gaps adjacent to the moved point become

\[
\Delta_{m-1}^{\delta}=1+\delta,
\qquad
\Delta_m^{\delta}=1-\delta.
\]

Every other gap is unchanged.

The primitive width normalization used in PF-086/PF-087 is

\[
W_n=2\left(\frac1{\Delta_{n-1}}+\frac1{\Delta_n}\right).
\]

Hence

\[
W_m^0=4,
\qquad
\boxed{
W_m^{\delta}
=2\left(\frac1{1+\delta}+\frac1{1-\delta}\right)
=\frac4{1-\delta^2}.
}
\tag{2}
\]

Only the widths at `m-1,m,m+1` can change. Away from these three cusps, the endpoint sequence and all local widths are exactly the reference ones.

This is therefore stronger than the integer control of PF-088: the geometry is **identical to the regular reference outside a compact index set**.

## 2. The direct scattering sector still has the exact `1/4` transition

For the width-one normalized direct denominator,

\[
C_{ij}=\sqrt{W_iW_j}\,|x_j-x_i|,
\]

the reference lattice has

\[
C_{ij}^0=4|j-i|.
\]

Take `j=m+k`, with `k>=2`. Since the far cusp is unperturbed,

\[
W_j^{\delta}=4,
\]

and (2) gives the exact ratio

\[
\boxed{
R_k
:=\frac{C_{m,m+k}^{\delta}}{C_{m,m+k}^{0}}
=
\frac{1-\delta/k}{\sqrt{1-\delta^2}}
\longrightarrow
\rho_{\delta}:=rac1{\sqrt{1-\delta^2}}\ne1.
}
\tag{3}
\]

Define the same direct-channel relative kernel as PF-087,

\[
D_{\delta}(s)_{ij}
=(C_{ij}^{\delta})^{-2s}-(C_{ij}^{0})^{-2s},
\qquad i\ne j.
\]

The `m`-th row is therefore

\[
D_{\delta}(s)_{m,m+k}
=(4k)^{-2s}\big(R_k^{-2s}-1\big).
\tag{4}
\]

For every `s` with `Re s>0`,

\[
R_k^{-2s}-1
\longrightarrow
\rho_{\delta}^{-2s}-1
=(1-\delta^2)^s-1\ne0,
\]

because `0<1-delta^2<1`. Thus

\[
\boxed{
|D_{\delta}(s)_{m,m+k}|^2
\asymp_{s,\delta}
k^{-4\operatorname{Re}s}.
}
\tag{5}
\]

It follows immediately that the `m`-th row belongs to `ell^2` exactly when

\[
\operatorname{Re}s>\frac14.
\]

Moreover the whole matrix is supported on the finite set of rows and columns touching `m-1,m,m+1`. Hence, above the boundary, it is a finite sum of rank-one row/column operators and is in fact **finite rank**, therefore trace class:

\[
\boxed{
D_{\delta}(s)\in\mathcal S_1
\qquad(\operatorname{Re}s>1/4).
}
\tag{6}
\]

At and below the boundary, (5) gives a non-`ell^2` row. As in PF-087, a bounded operator on `ell^2` must have every row in `ell^2`, because the row is the coefficient vector of `D_{\delta}(s)^*e_m`. Therefore

\[
\boxed{
D_{\delta}(s)
\text{ has no bounded extension on }\ell^2
\qquad(0<\operatorname{Re}s\le1/4).
}
\tag{7}
\]

So the sharp Fredholm threshold of the selected direct channel is reproduced by a **single compact defect**.

This is an important interpretation check: the transition is a property of how the direct kernel propagates one local mismatch through the infinite one-dimensional channel set, not a property that requires a nontrivial geometric tail.

## 3. The all-block relative Ruelle sector has the same compact-defect boundary

The same phenomenon occurs for the canonical consecutive-block separators of PF-084.

Fix the perturbed left edge

\[
a=m-1,
\qquad
b=m+\delta,
\]

and a far unperturbed right edge

\[
c=n,
\qquad
d=n+1,
\qquad
k=n-m\to\infty.
\]

The reference and perturbed cross-ratios are

\[
\chi_k^0=k(k+2),
\]

and

\[
\boxed{
\chi_k^{\delta}
=\frac{(k-\delta)(k+2)}{1+\delta}.
}
\tag{8}
\]

Therefore

\[
\boxed{
\frac{\chi_k^{\delta}}{\chi_k^0}
=
\frac{1-\delta/k}{1+\delta}
\longrightarrow
\frac1{1+\delta}\ne1.
}
\tag{9}
\]

For the exact hyperbolic separator length

\[
L=4\operatorname{arsinh}\sqrt\chi,
\]

large `chi` gives `L=2 log chi+4 log 2+o(1)`. Thus

\[
\boxed{
L_k^{\delta}-L_k^0
\longrightarrow
-2\log(1+\delta)\ne0.
}
\tag{10}
\]

Let

\[
F_k(s)
=
\log
\frac{1-e^{-sL_k^{\delta}}}
     {1-e^{-sL_k^0}}.
\]

Since

\[
L_k^0=4\log(2k)+o(1),
\]

(10) and `log(1-z)=-z+O(z^2)` imply, for fixed `Re s>0`,

\[
\boxed{
F_k(s)
=
\big(1-(1+\delta)^{2s}\big)
(2k)^{-4s}(1+o(1)).
}
\tag{11}
\]

The coefficient is nonzero for `Re s>0`. Hence

\[
\boxed{
\sum_k|F_k(s)|<\infty
\quad\Longleftrightarrow\quad
\operatorname{Re}s>\frac14.
}
\tag{12}
\]

Only blocks whose four boundary endpoints touch the single moved vertex differ from the reference. There are only finitely many such row/column families of block indices. Therefore (12) is also the sharp ordinary absolute-convergence boundary of the **full compact-defect all-block relative product**.

Again, no tail deformation is present: a local change has been copied into infinitely many long block geodesics by the chosen all-block orbit family.

## 4. The control comes from a smooth compactly supported endpoint deformation

The one-point sequence (1) can be realized geometrically rather than imposed only on the discrete set.

Choose

\[
\psi\in C_c^\infty(m-1/2,m+1/2),
\qquad
\psi(m)=1,
\]

and define

\[
F_{\delta}(x)=x+\delta\psi(x).
\]

For `|delta|` small enough that

\[
|\delta|\,\|\psi'\|_{\infty}<1,
\]

we have `F_delta'(x)>0`. Thus `F_delta` is a smooth increasing coordinate deformation, is **exactly the identity outside a compact interval**, and satisfies

\[
F_{\delta}(n)=x_n^{\delta}.
\]

So the control is compatible with the same ordered-endpoint / orthogonal-side-pairing construction used throughout the prime-flute line.

No asymptotic jet, Schwarzian tail, prime distribution, or noncompact metric defect is needed to generate the quarter threshold in these selected sectors.

## 5. Prime-preserving compact control

The same argument can be performed without replacing the prime sampling.

Fix a prime index `m`, put

\[
X=g_{m-1}=p_m-p_{m-1},
\qquad
Y=g_m=p_{m+1}-p_m,
\]

and choose

\[
0<|\delta|<\frac12\min(X,Y)
\]

with, if necessary, `delta != Y-X`. Define

\[
q_n=p_n\quad(n\ne m),
\qquad
q_m=p_m+\delta.
\tag{13}
\]

The condition keeps the sequence ordered. The extra exclusion merely guarantees that the width at the moved cusp changes, because

\[
\frac1{X+\delta}+\frac1{Y-\delta}
-rac1X-rac1Y
=
-\frac{\delta(X+Y)(X-Y+\delta)}
{XY(X+\delta)(Y-\delta)}.
\tag{14}
\]

Thus the fixed direct row again has a nonunit limiting width ratio. PF-087's already-proved prime-tail estimate then gives the same dichotomy: the finitely supported row/column defect is trace class for `Re s>1/4` and has no bounded extension at or below `1/4`.

For the all-block sector, retain the left edge

\[
a=p_{m-1},
\qquad
b=p_m+\delta
\]

and let the right edge be `c=p_n,d=p_{n+1}`. Relative to the unperturbed prime reference,

\[
\boxed{
\frac{\chi_{m,n}^{\delta}}{\chi_{m,n}^{0}}
=
\left(1-\frac{\delta}{p_n-p_m}\right)
\frac{X}{X+\delta}
\longrightarrow
\frac{X}{X+\delta}\ne1.
}
\tag{15}
\]

Therefore the long separator again acquires a nonzero constant asymptotic length shift. PF-084's prime-tail summability estimate gives convergence above `1/4`; at the boundary

\[
e^{-L_{m,n}^0/4}
\asymp_m
\frac{\sqrt{g_n}}{p_n}
\ge \frac{c_m}{p_n},
\]

so Euler's divergence of `sum_p 1/p` gives divergence. The same fixed local defect therefore reproduces the prime-control quarter boundary while leaving **every sufficiently far prime vertex and prime gap exactly unchanged**.

This prime-preserving version is the direct reason the control matters for the actual research line: the `1/4` transition does not require the exact cotangent correction or any new fluctuation occurring out in the prime tail.

## 6. Consequence for PF-084, PF-087, and PF-088

PF-084 and PF-087 remain exact mathematical statements about their chosen relative sectors. PF-102 changes what their common boundary can mean.

PF-088 established

\[
\text{prime sampling is unnecessary for the exponent }1/4.
\]

PF-102 adds the stronger statement

\[
\boxed{
\text{a nontrivial asymptotic endpoint deformation is unnecessary as well.}
}
\]

The minimal mechanism is now exposed:

```text
one local non-Mobius endpoint/width defect
        +
one-dimensional family of arbitrarily long channels
        +
Ruelle weight e^{-sL} or direct amplitude distance^{-2s}
        ->
Re s = 1/4.
```

For the direct kernel, the quarter line is literally the `ell^2` threshold of one propagated row. For the all-block Euler product, it is literally the `ell^1` threshold of one fixed-left family of long separators.

Hence the quarter boundary is **not a tail invariant of the exact prime-flute geometry**. In particular it cannot by itself support an analogy with the Riemann critical line, a Riemann--Siegel scale, or a prime-specific transfer-operator transition.

The result also strengthens the warning in PF-085. A selected direct/all-block sector can exhibit a sharp nontrivial abscissa even when the geometric perturbation is compact. That is not enough to identify the sector with a canonical full relative Laplacian/scattering determinant.

## 7. What this negative result does not say

PF-102 does not prove that the full exact prime-flute is spectrally equivalent to a compact perturbation of a regular flute. It is not.

It also does not rule out:

- prime-dependent coefficients after the universal long-channel contribution is removed;
- non-direct scattering terms;
- a genuine relative Laplacian or scattering construction, if one can be defined for the infinite-cusp surface;
- localized tangent/Feshbach phenomena that depend on several gap ratios;
- an absolute nonperturbative invariant of the exact `pi cot(pi/p)` geometry.

The result is deliberately narrower and stronger where it applies: **the sharp `1/4` transition of PF-084/PF-087 is reproducible without any nontrivial tail geometry at all.**

## 8. Prior-art / novelty audit

No novelty is claimed for the underlying operator facts. A finite set of `ell^2` rows/columns gives a finite-rank operator; the `p`-series threshold is elementary; compactly supported perturbations and relative scattering/determinant constructions are standard themes in spectral theory. Borthwick--Judge--Perry, for example, construct relative Laplacian determinants for controlled hyperbolic-near-infinity perturbations of infinite-area surfaces, and classical scattering theory routinely treats compact perturbations.

Likewise, the standard Ruelle zeta is a product over the full primitive periodic-orbit set of a hyperbolic dynamical system; PF-084's all-consecutive-block product was already explicitly recorded as a selected canonical sector rather than a full Ruelle zeta.

Directed searches over relative Selberg/Ruelle zeta functions, compact perturbations of hyperbolic scattering, and infinite-type flute spectral theory did not locate this exact single-endpoint control or a theorem identifying PF-084/PF-087's quarter threshold with an intrinsic spectral invariant.

The project-specific contribution is therefore a **decisive adversarial control**, not a new general theorem:

\[
\boxed{
\text{the same sharp quarter boundary is produced by one compact endpoint defect.}
}
\]

That control removes the remaining interpretation in which the common `1/4` boundary was evidence for accumulated exact-circle or prime-gap structure along the infinite tail.

## 9. Formalizable core

The following finite/algebraic statements are natural Lean candidates:

1. For the one-point lattice perturbation, derive (2), (3), (8), and (9).
2. Prove `L_delta-L_0 -> -2 log(1+delta)` from `L=4 asinh sqrt(chi)` and (9).
3. Prove the elementary equivalence `sum k^(-4 sigma)<infinity iff sigma>1/4` for real `sigma>0` using the standard p-series theorem.
4. Show that a matrix supported in finitely many rows/columns with each row/column in `ell^2` is finite rank.
5. Formalize the prime one-point cross-ratio ratio (15) and width identity (14).

The bridge from these identities to the existing PF-084/PF-087 prime-tail summability lemmas uses only results already recorded in this research line.