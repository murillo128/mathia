# FD-167 — Full-field L2 inversion has uniform square-root-prefix conditioning

- **Date:** 2026-09-17
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** quantitative full-field stability / conditioning closure / robust permanent-source rigidity
- **Depends on:** FD-117, FD-166
- **Classification:** `EXACT-DERIVED + L2-STABILITY + CONDITIONING-CLOSURE`

## Claim

The conditioning question left open by `FD-166` has a uniform answer in the natural unnormalized `L^2` norm of the complete Farey discrepancy field.

Let

\[
a:\mathbb N\to\mathbb R,
\qquad
A(x):=\sum_{n\le x}a(n),
\tag{1}
\]

and let `\mathcal D_{H,A}` be the real source-controlled complete field from the `FD-117` transform, with `\mathcal D_H` the physical Möbius field. Put

\[
E_H:=\mathcal D_{H,A}-\mathcal D_H.
\tag{2}
\]

Then for every `1<=k<=H`,

\[
\boxed{
\left|
A\!\left(\left\lfloor\frac Hk\right\rfloor\right)
-
M\!\left(\left\lfloor\frac Hk\right\rfloor\right)
\right|
\le
\sqrt{30}\,\|E_H\|_{L^2(0,1)}.
}
\tag{3}
\]

Since every integer `1<=r<=floor(sqrt H)` belongs to the floor-quotient set `\mathcal Q_H`, this gives the uniform prefix modulus

\[
\boxed{
\max_{1\le r\le\lfloor\sqrt H\rfloor}
|A(r)-M(r)|
\le
\sqrt{30}\,\|E_H\|_2.
}
\tag{4}
\]

There is no loss depending on `H` or on the recovered prefix coordinate.

If in addition `a(n)` is integer-valued, then `A(r)-M(r)` is integral. Hence

\[
\boxed{
\|E_H\|_2<\frac1{\sqrt{30}}
\quad\Longrightarrow\quad
A(r)=M(r),\ a(r)=\mu(r)
\quad(1\le r\le\lfloor\sqrt H\rfloor).
}
\tag{5}
\]

Consequently, if `n_0` is the first coefficient at which a fixed integer-valued source differs from Möbius, then every horizon `H>=n_0^2` obeys the robust separation

\[
\boxed{
\|\mathcal D_{H,A}-\mathcal D_H\|_2
\ge
\frac1{\sqrt{30}}.
}
\tag{6}
\]

Thus the exact detection radius of `FD-166` is not ill-conditioned in complete-field `L^2`: a permanent discrete defect cannot hide behind an error tending to zero, or even behind an error uniformly smaller than the universal constant `1/sqrt(30)`.

## 1. Difference inversion removes the affine term

`FD-117` gives, for every `1<=k<=H`,

\[
M\!\left(\left\lfloor\frac Hk\right\rfloor\right)
=
\frac1k
\sum_{d\mid k}
\mu\!\left(\frac kd\right)
\left(1+2\pi i d\,\widehat{\mathcal D_H}(d)\right).
\tag{7}
\]

The source-controlled field uses the same transform with `M` replaced by `A`. Subtracting the two formulas cancels the affine `1` exactly and yields

\[
\Delta_H(k)
:=
A\!\left(\left\lfloor\frac Hk\right\rfloor\right)
-
M\!\left(\left\lfloor\frac Hk\right\rfloor\right)
=
\frac{2\pi i}{k}
\sum_{d\mid k}
\mu\!\left(\frac kd\right)d\,\widehat E_H(d).
\tag{8}
\]

This is already the relevant stability formula: approximate field agreement is passed through a finite divisor functional rather than through a long triangular solve.

## 2. The divisor functional has a universal L2 norm

Apply Cauchy--Schwarz to (8):

\[
|\Delta_H(k)|
\le
2\pi
\left(
\sum_{d\mid k}
\mu\!\left(\frac kd\right)^2
\frac{d^2}{k^2}
\right)^{1/2}
\left(
\sum_{d\mid k}|\widehat E_H(d)|^2
\right)^{1/2}.
\tag{9}
\]

With `e=k/d`, the first factor is bounded by the squarefree reciprocal-square sum

\[
\sum_{e\mid k}\frac{\mu(e)^2}{e^2}
\le
\sum_{e\ge1}\frac{\mu(e)^2}{e^2}
=
\frac{\zeta(2)}{\zeta(4)}
=
\frac{15}{\pi^2}.
\tag{10}
\]

Because `E_H` is real, Parseval gives

\[
\sum_{n\ge1}|\widehat E_H(n)|^2
=
\frac12
\left(\|E_H\|_2^2-|\widehat E_H(0)|^2\right)
\le
\frac12\|E_H\|_2^2.
\tag{11}
\]

The divisor frequencies in (9) are a subset of the positive frequencies, so combining (9)--(11) gives

\[
|\Delta_H(k)|
\le
2\pi
\sqrt{\frac{15}{\pi^2}}
\frac{\|E_H\|_2}{\sqrt2}
=
\sqrt{30}\,\|E_H\|_2,
\tag{12}
\]

which proves (3). The constant is explicit and universal; no optimality claim is made.

## 3. The square-root prefix inherits the same modulus

As used in `FD-166`,

\[
\{1,\ldots,\lfloor\sqrt H\rfloor\}
\subseteq
\mathcal Q_H
=
\left\{\left\lfloor\frac Hk\right\rfloor:1\le k\le H\right\}.
\tag{13}
\]

For every `r` in that consecutive prefix choose any `k` with `floor(H/k)=r` and apply (3). This proves (4) without accumulating errors across coordinates.

If `a` is integer-valued, each `A(r)-M(r)` is an integer. Under the strict hypothesis in (5), (4) makes its absolute value strictly smaller than `1`, hence it vanishes. Consecutive differencing with `A(0)=M(0)=0` then gives `a(r)=mu(r)` on the whole prefix.

For (6), let `n_0` be the first coefficient defect. Then

\[
A(n_0)-M(n_0)
=
a(n_0)-\mu(n_0)
\in\mathbb Z\setminus\{0\}.
\tag{14}
\]

Every `H>=n_0^2` exposes `n_0` in the prefix (13), so (4) forces `\sqrt{30}\|E_H\|_2>=1`.

## 4. Representation transplant and hostile audit

The quantitative inequality is mostly representation-level. Once a real complete field has Fourier data related to cumulative source coordinates by the divisor inversion (8), Cauchy--Schwarz, the squarefree divisor mask and Parseval give the same uniform conditioning. The proof does **not** use Möbius cancellation, prime phases or a zero-free region. What is specifically Farey is `FD-117`, which identifies the physical complete field with exactly this divisor/Fourier transform of the Mertens staircase. The robust exact lock in (5) additionally uses discreteness of the source lattice, not a new analytic property of `mu`.

The main endpoint checks are benign. Formula (8) is only used for `1<=k<=H`, where every divisor of `k` lies inside the `FD-117` cutoff. The positive-frequency factor `1/2` in (11) requires the real-field hypothesis and is not available for an arbitrary complex synthetic field. The strict threshold in (5) is essential to the stated lattice argument, and `sqrt(30)` is only a convenient universal bound, not asserted to be sharp.

The result is also tied to **complete-field `L^2` observation**. It gives no conditioning theorem when only finitely many Farey samples, a sparse Fourier subset, a coarsened field, or an unrelated norm is available. If the source is real but nonintegral, (4) remains valid but approximate agreement need not snap to exact coefficients. If the source may vary with `H`, (5) still locks each observed square-root prefix but does not by itself produce one permanent global source.

Clue transition check: no accepted clue changes status. This finding follows the explicit conditioning frontier left by `FD-166` and the current research map rather than resolving one of the surviving clue-specific programs.

## 5. Research consequence

The complete-field conditioning branch is now closed in a strong form: its inverse has an `H`-independent modulus in the same `L^2` ambient geometry used by the Franel/Cramer--von Mises formulation. In particular, conditioning itself consumes no power of `H`; any exponent loss needed to reach the Franel--Landau destination must enter elsewhere.

For a fixed integer-valued source, an even stronger cross-horizon statement follows. If there is any unbounded set of horizons on which

\[
\|\mathcal D_{H,A}-\mathcal D_H\|_2<\frac1{\sqrt{30}},
\tag{15}
\]

then the locked square-root prefixes exhaust every finite coordinate and force `a=mu` identically. The errors need not tend to zero.

The live information question is therefore **partial observation**: how much of the field or Fourier spectrum can be discarded while retaining a stable growing prefix, and what conditioning loss is then unavoidable? Separately, this theorem still does not prove the RH-critical discrepancy bound. Stable recovery of the Möbius source and coercivity of the Franel--Landau destination remain distinct gates.

## Prior-art check

A fresh search around Farey discrepancy, Mertens/Farey Fourier formulas, Parseval and inversion stability recovered the classical Farey--Mertens and Franel--Landau neighborhood already represented in this line, plus recent work on local Farey discrepancy, but did not expose a load-bearing external theorem for (3). The estimate above is a direct consequence of the internal `FD-117` inversion and elementary Parseval/Cauchy--Schwarz. No new source anchor is therefore added to `SOURCES.md`.

## Related findings

- `FD-002` — Franel quadratic discrepancy is an exact Cramer--von Mises/Mertens energy.
- `FD-117` — full Farey discrepancy field is invertibly equivalent to the quotient Mertens staircase.
- `FD-166` — unbounded exact complete fields rigidify a permanent source but left conditioning open.
