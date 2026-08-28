# PF-102 — a single compact endpoint defect reproduces the quarter-plane thresholds

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for interpreting the `Re s = 1/4` boundaries of PF-084/PF-087 as consequences of prime-gap fluctuations at infinity or of the exact cotangent deformation along the tail.

## Claim

PF-088 already showed that the quarter-plane boundary survives replacing the primes by the featureless integer lattice while keeping the cotangent deformation `V(x)=pi cot(pi/x)`. There is a stronger control: the same sharp boundary is produced when **one endpoint is moved and every other endpoint is left exactly unchanged**.

Start from

\[
x_n^0=n
\]

and fix an index `m`. For

\[
0<|\delta|<\frac12
\]

define

\[
x_n^{\delta}=
\begin{cases}
n+\delta,&n=m,\\
n,&n\ne m.
\end{cases}
\tag{1}
\]

This is an ordered zero-twist flute endpoint sequence. It is identical to the regular reference outside a compact index set and can be realized by a smooth compactly supported increasing deformation of the real coordinate.

For this one-defect surface:

\[
\boxed{
D_{\delta}(s)\in\mathcal S_1
\quad\Longleftrightarrow\quad
\operatorname{Re}s>\frac14
}
\]

in the same sense as PF-087: above `1/4` the direct relative kernel is actually finite rank, while at and below `1/4` it has a row outside `ell^2` and hence no bounded extension. The all-consecutive-block relative Ruelle product has the same sharp absolute-convergence boundary.

Thus the common quarter threshold needs neither prime sampling, prime-gap fluctuations, the cotangent map on the tail, nor an infinite family of endpoint defects. A **single compact local defect plus one-dimensional long-channel propagation** is sufficient.

## 1. Direct channel: one moved point gives the whole threshold

All reference gaps equal one. Around the moved endpoint,

\[
\Delta_{m-1}^{\delta}=1+\delta,
\qquad
\Delta_m^{\delta}=1-\delta.
\]

The primitive cusp-width normalization is

\[
W_n=2\left(\frac1{\Delta_{n-1}}+\frac1{\Delta_n}\right),
\]

so

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

Only the widths at `m-1,m,m+1` can change. For the width-one normalized direct denominator

\[
C_{ij}=\sqrt{W_iW_j}\,|x_j-x_i|,
\]

the reference lattice has `C^0_{ij}=4|j-i|`. Put `j=m+k`, `k>=2`. Then

\[
\boxed{
R_k
:=\frac{C_{m,m+k}^{\delta}}{C_{m,m+k}^{0}}
=
\frac{1-\delta/k}{\sqrt{1-\delta^2}}
\longrightarrow
\rho_{\delta}:=\frac{1}{\sqrt{1-\delta^2}}\ne1.
}
\tag{3}
\]

Define the same direct relative kernel as PF-087,

\[
D_{\delta}(s)_{ij}
=(C_{ij}^{\delta})^{-2s}-(C_{ij}^{0})^{-2s},
\qquad i\ne j.
\]

The `m`-th row is exactly

\[
D_{\delta}(s)_{m,m+k}
=(4k)^{-2s}\big(R_k^{-2s}-1\big).
\tag{4}
\]

For every `s` with `Re s>0`,

\[
R_k^{-2s}-1
\longrightarrow
(1-\delta^2)^s-1\ne0,
\]

because `0<1-delta^2<1`. Hence

\[
\boxed{
|D_{\delta}(s)_{m,m+k}|^2
\asymp_{s,\delta}
k^{-4\operatorname{Re}s}.
}
\tag{5}
\]

Therefore the row belongs to `ell^2` exactly when

\[
\operatorname{Re}s>\frac14.
\]

The full matrix is supported on the finite set of rows and columns touching `m-1,m,m+1`. Above `1/4`, every affected row/column is in `ell^2`, so the matrix is a finite sum of rank-one operators and is finite rank, hence trace class. At and below `1/4`, (5) gives a non-`ell^2` row, which is impossible for a bounded operator on `ell^2`.

Thus

\[
\boxed{
\begin{array}{ll}
\operatorname{Re}s>1/4:
&D_{\delta}(s)\in\mathcal S_1\text{ and is finite rank},\\[1mm]
0<\operatorname{Re}s\le1/4:
&D_{\delta}(s)\text{ has no bounded extension on }\ell^2.
\end{array}
}
\tag{6}
\]

This isolates the mechanism: the selected direct kernel propagates one local width mismatch to infinitely many distant channels with amplitude `k^{-2s}`; the quarter line is the `ell^2` threshold of that single propagated row.

## 2. All-block Ruelle sector: one moved edge is enough

Use the perturbed left edge

\[
a=m-1,
\qquad
b=m+\delta
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
\tag{7}
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
\tag{8}
\]

For the exact hyperbolic separator length

\[
L=4\operatorname{arsinh}\sqrt\chi,
\]

we have `L=2 log chi+4 log 2+o(1)` as `chi->infinity`, so

\[
\boxed{
L_k^{\delta}-L_k^0
\longrightarrow
-2\log(1+\delta)\ne0.
}
\tag{9}
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

and `log(1-z)=-z+O(z^2)`, (9) gives, for fixed `Re s>0`,

\[
\boxed{
F_k(s)
=
\big(1-(1+\delta)^{2s}\big)(2k)^{-4s}(1+o(1)).
}
\tag{10}
\]

The coefficient is nonzero whenever `Re s>0`. Hence

\[
\boxed{
\sum_k|F_k(s)|<\infty
\quad\Longleftrightarrow\quad
\operatorname{Re}s>\frac14.
}
\tag{11}
\]

Only blocks whose four boundary endpoints touch the single moved vertex differ from the reference. There are finitely many such row/column families of block indices. Thus (11) is the sharp ordinary absolute-convergence boundary of the **full compact-defect all-block relative product**, not merely of the displayed subfamily.

The all-block construction therefore copies one local defect into infinitely many long separating geodesics. Its quarter abscissa does not require a nontrivial tail deformation.

## 3. The control is a smooth compactly supported deformation

Choose

\[
\psi\in C_c^\infty(m-1/2,m+1/2),
\qquad
\psi(m)=1,
\]

and set

\[
F_{\delta}(x)=x+\delta\psi(x).
\]

If

\[
|\delta|\,\|\psi'\|_{\infty}<1,
\]

then `F_delta'(x)>0`. Hence `F_delta` is a smooth increasing coordinate deformation, equals the identity outside a compact interval, and satisfies

\[
F_{\delta}(n)=x_n^{\delta}.
\]

So the control is compatible with the same ordered-endpoint / orthogonal-side-pairing construction used throughout the flute line. It is not an arbitrary zeta-like generating function and it introduces no asymptotic Schwarzian or endpoint tail at all.

## 4. Prime-preserving compact control

The same test can be made while leaving the actual prime tail untouched.

Fix `m` and write

\[
X=g_{m-1}=p_m-p_{m-1},
\qquad
Y=g_m=p_{m+1}-p_m.
\]

Choose

\[
0<|\delta|<\frac12\min(X,Y)
\]

and, if needed, avoid the single additional value `delta=Y-X`. Define

\[
q_n=p_n\quad(n\ne m),
\qquad
q_m=p_m+\delta.
\tag{12}
\]

The sequence stays ordered. The cusp width at the moved point changes because

\[
\frac1{X+\delta}+\frac1{Y-\delta}
-
\frac1X-rac1Y
=
-\frac{\delta(X+Y)(X-Y+\delta)}
{XY(X+\delta)(Y-\delta)}.
\tag{13}
\]

Thus the fixed direct row again has a nonunit limiting width ratio. PF-087's prime-tail summability estimate immediately gives the same sharp direct-kernel dichotomy as (6).

For the all-block sector, use the moved left edge

\[
a=p_{m-1},
\qquad
b=p_m+\delta
\]

and the unmodified far edge `c=p_n,d=p_{n+1}`. Relative to the unperturbed prime reference,

\[
\boxed{
\frac{\chi_{m,n}^{\delta}}{\chi_{m,n}^{0}}
=
\left(1-\frac{\delta}{p_n-p_m}\right)
\frac{X}{X+\delta}
\longrightarrow
\frac{X}{X+\delta}\ne1.
}
\tag{14}
\]

The separator therefore acquires a nonzero constant asymptotic length shift. PF-084's tail estimate gives convergence for `Re s>1/4`. At the boundary,

\[
e^{-L_{m,n}^0/4}
\asymp_m
\frac{\sqrt{g_n}}{p_n}
\ge
\frac{c_m}{p_n},
\]

so Euler's divergence of `sum_p 1/p` forces divergence. Thus the prime-control quarter boundary survives even though **every sufficiently far prime vertex and prime gap is exactly unchanged**.

## 5. Consequence for the earlier quarter-plane findings

PF-088 established that prime sampling is unnecessary for the exponent `1/4`. PF-102 adds the stronger statement

\[
\boxed{
\text{a nontrivial asymptotic endpoint deformation is unnecessary as well.}
}
\]

The minimal mechanism is

```text
one local non-Mobius endpoint/width defect
        +
one-dimensional arbitrarily long channels
        +
Ruelle weight e^{-sL} or direct amplitude distance^{-2s}
        ->
Re s = 1/4.
```

PF-084 and PF-087 remain exact statements about their chosen relative sectors, but their common boundary is **not a tail invariant of the exact prime-flute geometry**. It cannot by itself support an RH interpretation, a Riemann--Siegel analogy, or a prime-specific transfer-operator transition.

The result also sharpens PF-085's warning. A selected direct/all-block sector can display a sharp abscissa even when the endpoint perturbation is compact. That is not enough to identify the sector with a canonical full relative Laplacian or physical scattering determinant.

## 6. Boundary of the negative result

PF-102 does **not** say that the exact prime-flute is a compact perturbation of the projective reference, nor that their full Laplacians or physical scattering operators are equivalent.

It does not rule out prime-dependent coefficients after subtraction of the universal long-channel background, non-direct scattering terms, localized tangent/Feshbach effects that depend on several gap ratios, or an absolute nonperturbative invariant of the exact `pi cot(pi/p)` geometry.

It rules out the specific interpretation

\[
\boxed{
\text{quarter-plane transition}
\Longrightarrow
\text{accumulated exact-circle / prime-gap structure at infinity}.
}
\]

## 7. Prior-art / novelty audit

No novelty is claimed for the operator-theoretic ingredients. Finite-rank decompositions, `p`-series thresholds, and compactly supported perturbations are classical. Relative scattering and relative determinant theory routinely studies controlled or compact perturbations; for example Borthwick--Judge--Perry construct relative Laplacian determinants for hyperbolic-near-infinity metrics on infinite-area surfaces. Standard Ruelle zeta theory, on the other hand, is attached to the full primitive periodic-orbit set of a hyperbolic dynamical system, whereas PF-084 was already explicitly a selected all-consecutive-block sector.

Directed searches over relative Selberg/Ruelle zeta functions, compact perturbations of hyperbolic scattering, infinitely generated Fuchsian groups, and infinite-type flute spectral theory did not locate this exact single-endpoint control or an intrinsic theorem assigning the PF-084/PF-087 quarter threshold to the full flute spectrum.

The durable project-specific contribution is therefore an **adversarial impossibility result**, not a new general theorem:

\[
\boxed{
\text{one compact endpoint defect reproduces the same sharp quarter boundary.}
}

## 8. Formalizable core

Natural finite Lean candidates are:

1. derive (2), (3), (7), and (8) for the one-point lattice perturbation;
2. prove (9) from `L=4 asinh sqrt(chi)` and (8);
3. reduce (5) and (10) to the standard `p`-series criterion;
4. prove that a matrix supported in finitely many rows/columns, with those rows/columns in `ell^2`, is finite rank;
5. formalize the prime one-point width identity (13) and cross-ratio identity (14).

The prime-tail bridge then uses only the summability lemmas already established in PF-084/PF-087.