# WP-084 — Fixed-shift positive cover family has a singular Fisher boundary at the covariant origin

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + POSITIVE-FAMILY + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-081` leaves a tempting escape from the pointed-cover obstruction. For every fixed real shift `c >= 0`, the cover coboundary

\[
D_{n,c}:=(\rho_n-I)(L+cI)^{-1},
\qquad
\rho_n(X)=nW_n^*XW_n,
\]

is positive trace class and has the **same** exact trace

\[
\operatorname{Tr}D_{n,c}=\log n.
\]

Thus the whole positive half-line preserves the finite `log p` coefficient, while the shift parameter is exactly the parameter that exposes the digamma/Gamma profile in `WP-074`--`WP-076`. One might therefore try to use the information geometry of the positive family itself as the missing positive archimedean response: keep the exact finite mass fixed and measure how the positive state changes with `c`.

This route has a sharp obstruction. Normalize

\[
P_{n,c}:=\frac{D_{n,c}}{\log n},
\qquad n>1,\ c\ge0.
\]

Then `P_{n,c}` is a diagonal density operator. In the canonical affine spectral-shift coordinate `c`, its classical Fisher/Hellinger metric is finite for every `c>0` but **diverges exactly at the unique scale-covariant point `c=0`**:

\[
\boxed{
\mathcal I_n(c)
:=
\sum_{k\ge0}
\frac{(\partial_c p_{n,c}(k))^2}{p_{n,c}(k)}
<\infty
\quad(c>0),
}
\]

whereas

\[
\boxed{
\mathcal I_n(0)=\infty.
}
\]

Equivalently,

\[
\left\|\partial_c\sqrt{P_{n,c}}\right\|_{HS}^2
=\frac14\mathcal I_n(c)
\]

is infinite at `c=0`. The same point is already the sharp positivity boundary of `WP-081`: for `-1/2<c<0`, `D_{n,c}` is eventually negative, while a nonreal shift is not self-adjoint. Hence the exact-log positive family cannot supply a finite Fisher/Hellinger archimedean tangent through the canonical Riemann representative before one even reaches the critical-line shift.

There is a second, purely operator-theoretic obstruction. Every nontrivial shift contrast

\[
D_{n,c_2}-D_{n,c_1},
\qquad c_1\ne c_2,\ c_1,c_2\ge0,
\]

is a nonzero self-adjoint trace-class operator of trace zero and is therefore **indefinite**. More generally, every nontrivial positive probability mixture of the shifted states remains positive with the exact finite trace, but its shift-dependent correction relative to the covariant representative is again nonzero, trace zero, and indefinite.

Thus the fixed-shift cone exhibits a precise positivity-versus-archimedean-variation split:

```text
positive fixed-shift representatives
    -> exact Tr = log n for every c >= 0
    -> exact finite Mangoldt prime-ray readout survives

shift-dependent relative information
    -> additive operator contrast has trace 0 and is indefinite
    -> canonical Fisher/Hellinger quadratic tangent diverges at c = 0

continue toward the critical spectral shift
    -> fixed-shift positivity has already ended
```

This rules out using the **canonical monotone/information-geometric variation of the `WP-081` positive fixed-shift family** as a finite archimedean positive sector. It does not rule out a noncommuting deformation introduced before diagonalization, a non-monotone/nonlocal metric with an independent geometric theorem, a singular quotient/compression, or a genuinely nonseparable finite--archimedean object formed before positivity.

## 1. Exact diagonal family and normalization

Write

\[
a=\frac12+c.
\]

From `WP-081`,

\[
D_{n,c}e_k=d_{n,c}(k)e_k,
\]

with

\[
\boxed{
d_{n,c}(k)
=
\sum_{r=0}^{n-1}\frac1{nk+r+a}
-
\frac1{k+a}.
}
\tag{1}
\]

For every `n>1` and `c>=0`,

\[
d_{n,c}(k)>0,
\qquad
\sum_{k\ge0}d_{n,c}(k)=\log n.
\tag{2}
\]

Therefore

\[
p_{n,c}(k):=\frac{d_{n,c}(k)}{\log n}
\tag{3}
\]

is an honest probability distribution on `N_0`, equivalently the spectrum of a trace-one positive diagonal operator `P_{n,c}`. No zeta zero, analytic continuation, or regularized trace enters this normalization.

Differentiating (1) gives the exact tangent

\[
\boxed{
\partial_c d_{n,c}(k)
=
-\sum_{r=0}^{n-1}\frac1{(nk+r+a)^2}
+\frac1{(k+a)^2}.
}
\tag{4}
\]

Since the total trace in (2) is independent of `c`, the tangent has zero total mass whenever termwise differentiation is justified; the asymptotics below give absolute summability locally in `c` and justify it directly.

## 2. At the covariant origin the state tail is one order thinner than its shift tangent

At `c=0`, `D_{n,0}=Q_n` is the scale-covariant defect of `WP-074`. Its exact centered-block expansion is

\[
\boxed{
d_{n,0}(k)
=
C_n(k+\tfrac12)^{-3}
+O_n(k^{-5}),
\qquad
C_n:=\frac{n^2-1}{12n^2}.
}
\tag{5}
\]

Expanding (4) at the same point gives

\[
\boxed{
\partial_c d_{n,c}(k)\big|_{c=0}
=
A_n(k+\tfrac12)^{-2}
+O_n(k^{-3}),
\qquad
A_n:=\frac{n-1}{n}.
}
\tag{6}
\]

The crucial mismatch is therefore

```text
state at c=0:       d(k)  ~ C_n / k^3
canonical c-tangent d'(k) ~ A_n / k^2.
```

The affine shift direction creates a heavier tail than the positive covariant state has available to absorb in quadratic information norm.

Indeed,

\[
\frac{(\partial_c d_{n,c}(k)|_{c=0})^2}{d_{n,0}(k)}
=
\frac{A_n^2}{C_n}\frac1{k+1/2}
+O_n(k^{-2}),
\tag{7}
\]

and

\[
\boxed{
\frac{A_n^2}{C_n}
=
12\frac{n-1}{n+1}>0.
}
\tag{8}
\]

Consequently the Fisher series contains a positive harmonic tail:

\[
\mathcal I_n(0)
=
\frac1{\log n}
\sum_{k\ge0}
\frac{(\partial_c d_{n,c}(k)|_{c=0})^2}{d_{n,0}(k)}
=
\infty.
\tag{9}
\]

The divergence is not caused by a zero eigenvalue: every `d_{n,0}(k)` is strictly positive. It comes from the **relative tail order** of the canonical shift tangent.

## 3. Every interior positive shift has finite Fisher energy

For a fixed `c>0`, `WP-081` gives

\[
d_{n,c}(k)
=
A_n c\,k^{-2}+O_{n,c}(k^{-3}).
\tag{10}
\]

Equation (4) gives simultaneously

\[
\partial_c d_{n,c}(k)
=
A_n k^{-2}+O_{n,c}(k^{-3}).
\tag{11}
\]

Hence

\[
\frac{(\partial_c d_{n,c}(k))^2}{d_{n,c}(k)}
=
\frac{A_n}{c}k^{-2}+O_{n,c}(k^{-3}),
\tag{12}
\]

which is summable. Thus

\[
\boxed{
\mathcal I_n(c)<\infty
\qquad(c>0),
}
\tag{13}
\]

and (9)--(13) give a sharp information-geometric boundary on the entire positive half-line.

The square-root embedding makes the same conclusion without information-geometric terminology:

\[
\partial_c\sqrt{p_{n,c}(k)}
=
\frac{\partial_c p_{n,c}(k)}{2\sqrt{p_{n,c}(k)}},
\]

so

\[
\boxed{
4\left\|\partial_c\sqrt{P_{n,c}}\right\|_{HS}^2
=
\mathcal I_n(c).
}
\tag{14}
\]

Thus the failure at `c=0` is a literal failure of Hilbert--Schmidt differentiability of the positive square-root state path in the canonical affine shift coordinate.

For commuting density operators this is the classical Fisher/Hellinger geometry. Standard monotone quantum information metrics reduce on commuting directions to this classical metric up to normalization; the present obstruction therefore is not repaired merely by choosing a different standard monotone quantum metric while leaving the family diagonal. No novelty is claimed for Fisher, Hellinger, or monotone-state geometry themselves.

## 4. The additive shift tangent is necessarily indefinite

There is an even cheaper sign obstruction. For any admissible `c_1,c_2`,

\[
\operatorname{Tr}(D_{n,c_2}-D_{n,c_1})=0.
\tag{15}
\]

If `c_1\ne c_2`, the difference is nonzero. Indeed, subtracting the `WP-081` asymptotics gives

\[
d_{n,c_2}(k)-d_{n,c_1}(k)
=
A_n(c_2-c_1)k^{-2}+O(k^{-3}).
\tag{16}
\]

A nonzero positive or negative trace-class self-adjoint operator has strictly positive or strictly negative trace, respectively. Therefore

\[
\boxed{
D_{n,c_2}-D_{n,c_1}
\text{ is indefinite for }c_1\ne c_2.
}
\tag{17}
\]

The infinitesimal tangent `partial_c D_{n,c}` is likewise a nonzero trace-zero trace-class diagonal operator and hence indefinite. Squaring that tangent through Fisher/Hellinger geometry is the most canonical way to recover a positive quadratic response, but Sections 2--3 show that this response is singular exactly at the covariant origin.

## 5. Positive averaging preserves the finite mass but hides shift information in an indefinite contrast

The fixed-shift half-line is not merely a one-parameter set of matched controls. Let `nu` be any probability measure on `[0,infinity)`. Since every `D_{n,c}` is positive and has trace norm `log n`, the diagonal mixture

\[
\overline D_{n,\nu}
:=
\int_{[0,\infty)}D_{n,c}\,d\nu(c)
\tag{18}
\]

is a positive trace-class operator and Tonelli gives

\[
\boxed{
\operatorname{Tr}\overline D_{n,\nu}=\log n.
}
\tag{19}
\]

Thus **arbitrary positive averaging over the shift parameter preserves the exact finite log-degree coefficient**.

If `nu != delta_0`, however, the mixture differs from the covariant representative. At `k=0`, (1) simplifies to

\[
d_{n,c}(0)
=
\sum_{r=1}^{n-1}\frac1{r+1/2+c},
\tag{20}
\]

which is strictly decreasing in `c`. Hence

\[
\langle e_0,\overline D_{n,\nu}e_0\rangle
<
\langle e_0,D_{n,0}e_0\rangle
\qquad(\nu\ne\delta_0).
\tag{21}
\]

So

\[
A_{n,\nu}:=\overline D_{n,\nu}-D_{n,0}
\]

is nonzero while, by (19),

\[
\operatorname{Tr}A_{n,\nu}=0.
\]

Therefore

\[
\boxed{
A_{n,\nu}\text{ is indefinite whenever }\nu\ne\delta_0.
}
\tag{22}
\]

This eliminates a broad averaging repair. One may keep positivity and the exact finite trace by averaging whole representatives, but the **new information introduced by the averaging cannot itself be split off as a positive additive archimedean correction**.

## 6. Relation to the Gamma/digamma spectral shift

`WP-074` shows that the same half-integer ladder has the exact relative-resolvent trace

\[
\operatorname{Tr}\left[
(L+\tfrac12I)^{-1}
-
(L+\tfrac{s-1}{2}I)^{-1}
\right]
=
\psi(s/2)+\gamma.
\tag{23}
\]

`WP-075`--`WP-076` identify the corresponding shifted-resolvent parameter as

\[
c=\frac{s-1}{2}.
\tag{24}
\]

The real positive fixed-shift family therefore occupies `s>=1`. To reach the critical line,

\[
\Re s=\frac12
\quad\Longrightarrow\quad
\Re c=-\frac14.
\tag{25}
\]

But `WP-081` proves that the exact-log fixed-shift defect ceases to be positive immediately for real `c<0`, and nonreal `c` destroys self-adjointness. The new result strengthens that boundary: even when approached from the positive side, the canonical Fisher/Hellinger shift tangent already has infinite quadratic cost at `c=0`.

This does **not** say that `c=0` is at infinite metric distance; the metric coefficient is parametrization-dependent and a nonlinear reparametrization may soften the speed. The invariant content used here is narrower and exact: in the affine spectral parameter canonically tied to `s`, the commuting positive state path is not Fisher/Hellinger differentiable at the unique covariant representative, and the additive relative tangent is indefinite.

## 7. Matched controls and prior-art audit

Nothing in (1)--(22) uses primality, zeta zeros, the functional equation, or a special arithmetic property of `n`. It uses only the normalized block-cover transfer, the half-integer ladder, the fixed-shift positive cocycles of `WP-081`, and ordinary positive-state geometry. The same singularity and indefinite shift contrast occur for every matched integer-degree block-cover system with the same asymptotic ladder. They are therefore **universal cover geometry**, not an arithmetic sign theorem.

The weighted-composition semigroup is already classical prior art in `SOURCES.md` through Noor and Manzur--Noor--Santos. Fisher/Hellinger information geometry and monotone metrics on commuting state spaces are classical as well. A directed audit around the Hardy weighted-composition semigroup, resolvent defects, Fisher/Hellinger metrics, and monotone quantum metrics did not locate a source asserting the Mathia-specific tail-order singularity (5)--(13) or the consequence (22). No theorem-level novelty is claimed for the classical information-geometric framework; the durable content is the obstruction produced by inserting the exact `WP-081` positive cover family into it.

This also blocks an overclaim in the other direction. The result does **not** prove that every conceivable positive shift-sensitive functional is singular. A nonlinear non-monotone metric, a noncommuting dilation, or a global coupling may behave differently. Such a construction would have to supply its own independent geometric reason for positivity and survive the same matched controls.

## 8. Exact falsification surface

The finding is falsified if any of the following fails under the `WP-081` normalization:

1. the exact diagonal formula (1) or constant trace (2);
2. the `WP-074` cubic tail (5);
3. the tangent quadratic tail (6);
4. the harmonic Fisher asymptotic (7)--(9);
5. convergence of the Fisher series for any fixed `c>0` as in (10)--(13);
6. nonzero trace-zero indefiniteness of a distinct shift contrast (17);
7. positivity and exact trace of the probability mixture (18)--(19);
8. strict decrease of the zeroth diagonal (20), which forces the mixture contrast to be nonzero;
9. a positive additive shift contrast inside this same fixed-shift family that is nonzero while retaining zero trace;
10. a finite Fisher/Hellinger tangent at `c=0` for the canonical affine shift parameter.

Items 4 and 10 are especially cheap to audit: the ratio of the exact leading tail coefficients is

\[
\frac{A_n^2}{C_n}=12\frac{n-1}{n+1},
\]

so any correct asymptotic calculation must produce a nonzero harmonic term.

## Research consequence

`WP-081` showed that the exact positive finite-place package does not select the Riemann representative: every `c>=0` has the same `log n`, the same positive prime-power Möbius trace, and the same critical cover overlap. `WP-083` then showed that homogeneous Jensen deformations are flat and recover exact Mangoldt support only at a singular inverse-scale endpoint.

The present result closes the most canonical way to exploit the surviving fixed-shift degree of freedom as an archimedean **positive geometry**. The shift parameter can change the positive state without changing its finite mass, but the relative operator direction is indefinite, while the canonical positive quadratic information metric is singular exactly at the covariant origin and positivity itself ends on the other side.

A viable finite--archimedean completion must therefore introduce new structure before this diagonal shift geometry is read out: for example a genuinely noncommuting/nonseparable coupling, a quotient or compression with a new sign theorem, a cohomological/intersection pairing, or another global operation that both retains the exact finite coefficients and generates the archimedean/polar sector without treating shift variation as an ordinary positive-state tangent.