# PC-036 — all even inverse-power pointed anchor spectra are finite Dirichlet-L special-value bundles

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for the natural singular-kernel extension of PC-035. Replacing the inverse-square pointed chord profile by any fixed even inverse power `|1-zeta|^{-2m}` does not create a new prime-circle spectral family: its complete multiplicative-character spectrum is a finite rational combination of classical values `L(2,chi),...,L(2m,chi)`. The exact `p <-> 2p` pointed comparison remains in the same finite bundle, with only explicit local factors involving `chi(2)`.

## 1. The singular-kernel escape left after PC-035

PC-035 classifies the pointed inverse-square profile at an odd prime `p`,

\[
w_{1,p}^-(a)=|1-\zeta_p^a|^{-2}
=\frac1{4\sin^2(\pi a/p)},
\]

and shows that its multiplicative character spectrum is classical `L(2,chi)` data. A direct escape is to make the geometric probe more singular and nonlinear before spectralization:

\[
w_{m,p}^-(a)
:=|1-\zeta_p^a|^{-2m}
=\frac1{4^m\sin^{2m}(\pi a/p)},
\qquad m\ge1.
\]

These kernels are increasingly concentrated at the common anchor and lie outside the bounded regular-linear probe setting of PC-021. The question is whether higher singularity introduces genuinely new arithmetic modes.

It does not. The whole hierarchy closes on finitely many positive even Dirichlet special values.

## 2. Exact Mittag-Leffler ladder for every even inverse power

Set

\[
F_m(x):=\csc^{2m}(\pi x).
\]

A direct differentiation gives

\[
F_m''(x)
=2m(2m+1)\pi^2F_{m+1}(x)
-4m^2\pi^2F_m(x),
\]

hence

\[
\boxed{
F_{m+1}(x)
=
\frac{\pi^{-2}F_m''(x)+4m^2F_m(x)}{2m(2m+1)}.
}
\]

Start from the classical Mittag-Leffler expansion

\[
F_1(x)
=\frac1{\pi^2}\sum_{r\in\mathbb Z}\frac1{(x+r)^2}.
\]

Induction through the differential recurrence yields positive rational coefficients `c_{m,j}` such that

\[
\boxed{
F_m(x)
=
\sum_{j=1}^{m}
 c_{m,j}\,\pi^{-2j}
\sum_{r\in\mathbb Z}\frac1{(x+r)^{2j}}.
}
\]

They are determined by

\[
c_{1,1}=1,
\]

and, with coefficients outside `1<=j<=m` understood as zero,

\[
\boxed{
 c_{m+1,j}
=
\frac{2m}{2m+1}c_{m,j}
+
\frac{(2j-2)(2j-1)}{2m(2m+1)}c_{m,j-1}.
}
\]

In particular,

\[
\begin{aligned}
\csc^2(\pi x)
&=\pi^{-2}S_2(x),\\
\csc^4(\pi x)
&=\frac23\pi^{-2}S_2(x)+\pi^{-4}S_4(x),\\
\csc^6(\pi x)
&=\frac8{15}\pi^{-2}S_2(x)+\pi^{-4}S_4(x)+\pi^{-6}S_6(x),
\end{aligned}
\]

where

\[
S_{2j}(x)=\sum_{r\in\mathbb Z}(x+r)^{-2j}.
\]

Thus increasing the inverse chord power never creates a new analytic kernel family: it only adds finitely many higher even Mittag-Leffler modes.

## 3. Complete multiplicative spectrum at prime level

For a Dirichlet character `chi mod p`, define

\[
C_{m,p}^-(\chi)
:=
\sum_{a=1}^{p-1}
\overline{\chi(a)}\,w_{m,p}^-(a).
\]

At `x=a/p`, each Mittag-Leffler term satisfies

\[
\sum_{r\in\mathbb Z}\frac1{(a/p+r)^{2j}}
=
p^{2j}
\sum_{r\in\mathbb Z}\frac1{(a+rp)^{2j}}.
\]

As `a=1,...,p-1` and `r` vary, `a+rp` runs once through all nonzero integers not divisible by `p`; extending `chi` by zero on multiples of `p` therefore gives

\[
\sum_{a=1}^{p-1}\overline{\chi(a)}
\sum_{r\in\mathbb Z}\frac1{(a+rp)^{2j}}
=
\bigl(1+\overline{\chi(-1)}\bigr)
L(2j,\overline\chi).
\]

Consequently

\[
\boxed{
C_{m,p}^-(\chi)
=
\frac{1+\overline{\chi(-1)}}{4^m}
\sum_{j=1}^{m}
 c_{m,j}
\left(\frac p\pi\right)^{2j}
L(2j,\overline\chi).
}
\]

All odd characters vanish identically. For every even character,

\[
\boxed{
C_{m,p}^-(\chi)
=
\frac{2}{4^m}
\sum_{j=1}^{m}
 c_{m,j}
\left(\frac p\pi\right)^{2j}
L(2j,\overline\chi).
}
\]

Thus the entire multiplicative spectrum of every fixed even inverse-power pointed kernel is contained in the finite classical bundle

\[
\boxed{
\{L(2,\chi),L(4,\chi),\ldots,L(2m,\chi)\}.
}
\]

The principal character is even more elementary. Since

\[
L(2j,\chi_0)=\zeta(2j)(1-p^{-2j}),
\]

and `zeta(2j)/pi^{2j}` is rational, `C_{m,p}^-(chi_0)` is a rational polynomial in `p^2` of degree `m`. For `m=2`, for example,

\[
\boxed{
\sum_{a=1}^{p-1}|1-\zeta_p^a|^{-4}
=
\frac{(p^2-1)(p^2+11)}{720}.
}
\]

So neither the nonprincipal nor principal sectors introduce a new spectral variable or new zero set.

## 4. The exact pointed `p <-> 2p` control also stays in the same bundle

For odd prime `p`, identifying `mu_{2p}^*=-mu_p^*` turns the fixed-anchor profile into

\[
w_{m,p}^+(a)
:=|1+\zeta_p^a|^{-2m}
=\frac1{4^m\cos^{2m}(\pi a/p)}.
\]

Because

\[
\sec^{2m}(\pi x)=\csc^{2m}(\pi(x+1/2)),
\]

the same coefficients `c_{m,j}` give a half-integer Mittag-Leffler expansion. At `x=a/p`, the denominators are

\[
a/p-r-\frac12
=
\frac{2a-p(2r+1)}{2p}.
\]

As `a` and `r` vary, the integers `2a-p(2r+1)` run once through all odd integers not divisible by `p`. Since modulo `p` one has `a = 2^{-1}N`, the character weight contributes the explicit local factor `chi(2)`. Removing the even integers from the Dirichlet series contributes `1-bar chi(2)2^{-2j}`.

Therefore

\[
\boxed{
C_{m,p}^+(\chi)
:=
\sum_{a=1}^{p-1}\overline{\chi(a)}w_{m,p}^+(a)
=
\frac{1+\overline{\chi(-1)}}{4^m}
\sum_{j=1}^{m}
 c_{m,j}
\bigl(2^{2j}\chi(2)-1\bigr)
\left(\frac p\pi\right)^{2j}
L(2j,\overline\chi).
}
\]

For `m=1`, this reduces exactly to PC-035:

\[
C_{1,p}^+(\chi)
=(4\chi(2)-1)C_{1,p}^-(\chi).
\]

For higher powers there is no single common multiplier because each `L(2j,chi)` receives its own factor `2^{2j}chi(2)-1`. This is extra information relative to the inverse-square case, but it is still only a finite recombination of the same classical positive-even `L`-values plus the local Euler datum at `2`.

## 5. Why this is a decisive negative for the singular pointed-kernel hierarchy

The obvious response to PC-035 is that `1/chord^2` may simply be too weak, while increasingly singular powers could retain finer prime-circle structure. PC-036 rules out that entire natural hierarchy at once:

\[
\boxed{
\text{common anchor}
\to
|1-\zeta|^{-2m}
\to
\text{multiplicative character spectrum}
\to
\text{finite }\{L(2j,\chi)\}_{j\le m}.
}
\]

Increasing `m` does add higher positive even special values, but it never produces a free spectral parameter, a zeta-zero divisor, a critical-line symmetry, or an operator whose spectrum is not already part of the classical Dirichlet package. At fixed `m`, the reduction is finite and exact.

Therefore the route

\[
\boxed{
\text{make the pointed chord kernel more singular}
\to
\text{diagonalize multiplicatively}
\to
\text{new RH mechanism}
}
\]

is closed for every integral even inverse power.

This sharpens the surviving boundary from PC-035: a viable pointed construction must not merely change the scalar singularity at the anchor. It must retain genuinely nonseparable information before character diagonalization, couple different shells/levels, use a non-power nonlinear interaction, or enter the global uniformization/monodromy sector.

## 6. Prior art and novelty audit

No theorem-level novelty is claimed for the analytic ingredients.

- Gauthier and Bruckman studied all even integral powers of cosecant and secant using differential identities and Mittag-Leffler expansions, exactly the classical analytic ladder used above for the unweighted kernels.
- Beck and Halloran place finite trigonometric sums weighted by Dirichlet characters inside an established discrete-Fourier/class-number literature rather than a new prime-circle phenomenon.
- Liu and Xin (2026) give a current systematic treatment of root-of-unity-weighted powers of cotangent, tangent, cosecant, and secant, including all even powers, using constant terms and partial fractions. Their weights are additive roots of unity rather than the multiplicative characters used here, so this is a neighboring prior-art boundary rather than an exact citation for the displayed formula.
- The passage from the Mittag-Leffler lattice sums to `L(2j,chi)` is an immediate absolutely convergent residue-class regrouping for `j>=1`; the `j=1` case is already PC-035.

The project-specific contribution is the **scope obstruction**: the whole singular pointed family suggested by PC-035 does not escape into a new spectral object. The exact formulas above are recorded because they close that research branch, not as a novelty claim for trigonometric character sums.

## 7. Boundary and exact audit tests

This finding does **not** classify:

- noninteger inverse powers, where branch choices and different analytic transforms enter;
- kernels mixing several chords or vertices before the character transform;
- the joint noncommuting matrix data of primitive-shell blocks and the anchor;
- cross-level couplings in `n`;
- squarefree multi-prime grounding patterns;
- global pointed uniformization, monodromy, Liouville, or Weil-Petersson data from PC-017.

The exact claim can be audited without numerical fitting:

1. differentiate `F_m=csc^{2m}(pi x)` twice and verify the recurrence;
2. induct the Mittag-Leffler decomposition and the coefficient recurrence;
3. regroup residue classes modulo `p` and verify the parity factor `1+bar chi(-1)`;
4. check `m=1` against PC-035;
5. check the principal `m=2` mode against `(p^2-1)(p^2+11)/720`;
6. repeat the lattice regrouping at half-integers and verify the factor `2^{2j}chi(2)-1`;
7. for `m=1`, recover exactly the PC-035 multiplier `4chi(2)-1`.

Failure of any one of these exact identities would invalidate the classification.
