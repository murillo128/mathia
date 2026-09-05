# PC-179 — signed radial-flux Mellinization is the classical Dirichlet-eta/zeta transform

**Status:** `EXACT-DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for treating a one-shell or linearly assembled Mellin transform of the signed cyclotomic radial flux as an independent Prime-Circle RH mechanism.

The proposed signed radial-flux clue points to a real and useful exact selector, but its most canonical archimedean spectralization classicalizes completely. For every primitive shell, the inward radial flux is a finite Möbius combination of universal Bose kernels. Its Mellin transform is the classical fixed-modulus Ramanujan Dirichlet series multiplied by `Gamma`; throughout the open critical strip its zeros are **exactly** the nontrivial zeros of `zeta`, with the same multiplicities. The strongest control is already the two-gon: its flux is `1/(e^x+1)`, so its Mellin transform is the standard Dirichlet-eta integral `Gamma(s) eta(s)`.

This is an exact geometric representation of the Riemann zero set, but it is not a new zero mechanism. A single elementary Prime-Circle shell already reproduces the whole zero set through a classical Mellin identity. Any surviving use of the signed flux must therefore couple shells **before** this scalar Mellin/endpoint collapse and must produce information not present in the `n=2` control.

## 1. Exact signed radial flux

For `n>1` and radial depth `x>0`, define

\[
F_n(x):=\log \Phi_n(e^{-x}),
\qquad
\rho_n(x):=-F_n'(x).
\]

The standard Ramanujan expansion of the cyclotomic logarithm is

\[
\log\Phi_n(z)
=
-\sum_{k\ge1}\frac{c_n(k)}{k}z^k,
\qquad |z|<1.
\]

Differentiating on the positive radial ray gives

\[
\boxed{
\rho_n(x)
=
-\sum_{k\ge1}c_n(k)e^{-kx}.
}
\tag{1}
\]

The cyclotomic Möbius factorization

\[
\Phi_n(z)=\prod_{d\mid n}(1-z^d)^{\mu(n/d)}
\]

gives the equivalent finite Lambert/Bose decomposition

\[
\boxed{
\rho_n(x)
=
-\sum_{d\mid n}
\mu(n/d)\frac{d}{e^{dx}-1}.
}
\tag{2}
\]

Each summand in (2) has a `1/x` singularity, but the singularities cancel because

\[
\sum_{d\mid n}\mu(n/d)=0
\qquad(n>1).
\]

Cyclotomic reciprocity also gives the finite boundary value

\[
\boxed{
\rho_n(0+)
=
\frac{\Phi_n'(1)}{\Phi_n(1)}
=
\frac{\varphi(n)}2.
}
\tag{3}
\]

Thus the signed profile is regular at the common vertex even though its full-root constituents are separately singular there.

## 2. Prime powers are exactly the pointwise-positive shells

For `n=p^a`, only the two top divisors survive in (2), so with `y=p^{a-1}x`,

\[
\boxed{
\rho_{p^a}(x)
=
p^{a-1}
\left(
\frac1{e^y-1}
-
\frac{p}{e^{py}-1}
\right).
}
\tag{4}
\]

Since

\[
e^{py}-1
=
(e^y-1)(1+e^y+\cdots+e^{(p-1)y})
>
p(e^y-1)
\]

for `y>0`, equation (4) proves

\[
\boxed{\rho_{p^a}(x)>0\quad(x>0).}
\tag{5}
\]

On the other hand,

\[
\int_0^\infty \rho_n(x)\,dx
=
F_n(0)-F_n(\infty)
=
\log\Phi_n(1)
=
\Lambda(n).
\tag{6}
\]

If `n>1` is not a prime power, then `Phi_n(1)=1`, so the integral is zero. By (3) the profile starts positive and it is not identically zero; hence it must take negative values. Therefore the positivity statement in the clue can be reconstructed entirely inside Prime Circle:

\[
\boxed{
\rho_n(x)>0\ \text{for every }x>0
\iff
n\text{ is a prime power}.
}
\tag{7}
\]

This is a geometric form of the classical cyclotomic prime-power selector, not yet an RH mechanism.

## 3. The radial Mellin transform factorizes exactly

Because `rho_n(x)=O(1)` at `0+` and decays exponentially at infinity, its Mellin transform

\[
\mathcal R_n(s)
:=
\int_0^\infty \rho_n(x)x^{s-1}\,dx
\tag{8}
\]

is holomorphic for `Re(s)>0`.

For `Re(s)>1`, termwise integration in (1) is absolutely justified and yields

\[
\mathcal R_n(s)
=
-\Gamma(s)
\sum_{k\ge1}\frac{c_n(k)}{k^s}.
\tag{9}
\]

The classical fixed-modulus Ramanujan Dirichlet series is

\[
\sum_{k\ge1}\frac{c_n(k)}{k^s}
=
\zeta(s)
\sum_{d\mid n}\mu(n/d)d^{1-s}.
\tag{10}
\]

The finite factor is

\[
\sum_{d\mid n}\mu(n/d)d^{1-s}
=
n^{1-s}\prod_{p\mid n}(1-p^{s-1}).
\tag{11}
\]

Consequently,

\[
\boxed{
\mathcal R_n(s)
=
-\Gamma(s)\zeta(s)\,
n^{1-s}\prod_{p\mid n}(1-p^{s-1}).
}
\tag{12}
\]

The right-hand side has a removable singularity at `s=1` for every `n>1`, and analytic continuation from `Re(s)>1` therefore identifies it with the integral (8) throughout `Re(s)>0`.

Equation (12) also explains the common-vertex von Mangoldt identity locally in Mellin space. If `omega(n)` is the number of distinct prime divisors, the finite Euler factor has a zero of order `omega(n)` at `s=1`, while `zeta` has a simple pole. Hence

- for `n=p^a`, the pole cancels one simple zero and leaves
  \[
  \mathcal R_{p^a}(1)=\log p;
  \]
- for `omega(n)>=2`, a zero of order `omega(n)-1` remains and
  \[
  \mathcal R_n(1)=0.
  \]

Thus the exact Mangoldt support is the elementary pole-zero cancellation at `s=1` inside the classical factorization (12).

## 4. Every shell has the same nontrivial zero set

Let `0<Re(s)<1`. Then for every prime `p`,

\[
|p^{s-1}|=p^{\operatorname{Re}(s)-1}<1,
\]

so no factor `1-p^{s-1}` can vanish. `Gamma(s)` has no zeros, and `n^{1-s}` is never zero. Therefore (12) gives the exact equivalence

\[
\boxed{
\mathcal R_n(s)=0
\iff
\zeta(s)=0,
\qquad
0<\operatorname{Re}(s)<1,
}
\tag{13}
\]

for **every** `n>1`, with the same zero multiplicities.

This is a strong matched control against over-interpreting the geometry. The nontrivial zero set does not depend on the shell, on primality, on the number of vertices, or on a cross-shell interaction. It is a universal scalar factor supplied by the Mellin transform of the Bose/Lambert tail.

The smallest shell makes the classicality explicit. Since

\[
\Phi_2(e^{-x})=1+e^{-x},
\]

one has

\[
\boxed{
\rho_2(x)=\frac1{e^x+1}.
}
\tag{14}
\]

Equation (12) becomes

\[
\boxed{
\mathcal R_2(s)
=
\Gamma(s)(1-2^{1-s})\zeta(s)
=
\Gamma(s)\eta(s).
}
\tag{15}
\]

This is exactly the standard Mellin integral for the Dirichlet eta function. In particular, the entire nontrivial Riemann zero set is already present in the radial flux of the single primitive vertex `-1`.

## 5. Why the positive kernel and the `1/2` Mellin line do not prove RH

For a prime-power shell, (5) gives a genuinely positive radial kernel. Moreover the Mellin-Plancherel transform on `L^2(R_+,dx)` naturally uses the half-density line `Re(s)=1/2`. It is therefore tempting to read (12) as a positivity or Hilbert-space explanation of the critical line.

That inference is not valid. Positivity of a function on `R_+` does not imply that the zeros of its Mellin transform lie on its Plancherel line. Equation (15) makes the issue decisive: such an argument applied to the elementary positive function `1/(e^x+1)` would already prove RH for the classical eta representation. No self-adjoint operator, de Branges structure, total-positivity theorem, sign-definite Weil form, or zero-confining inequality has been produced by the Prime-Circle geometry.

This also aligns with the earlier radial boundaries. PC-029 showed that spectralizing the inversion-even log-radius field gives elementary Ramanujan/cylinder data rather than the zeta functional equation, and PC-165 showed that the canonical dilation half-density itself is the classical continuous dilation representation. Equation (12) does not repair those obstructions; it is another classical Mellin presentation of zeta.

## 6. Prior-art and novelty audit

No novelty is claimed for the analytic ingredients.

- The Ramanujan-sum expansion of `log Phi_n` and the fixed-modulus Dirichlet series (10) are classical Ramanujan-sum theory; Ramanujan's 1918 paper is already anchored in `research/prime_circle/SOURCES.md`.
- The Mellin integral of `1/(e^x-1)` giving `Gamma(s) zeta(s)`, and the `n=2` specialization `1/(e^x+1)` giving `Gamma(s) eta(s)`, are standard classical zeta/eta integral representations.
- The finite Euler product in (11) is elementary Möbius inversion.

A directed prior-art check therefore finds the apparent `zeta` zero spectrum on the classical side before any Prime-Circle spectral interpretation. The research contribution here is a **scope classification**: the signed radial-flux clue has a real exact selector, but its canonical one-shell Mellin/archimedean spectralization is already the classical eta/zeta transform.

## 7. Boundary and research consequence

This finding rules out treating any of the following as independent Prime-Circle progress by themselves:

- the existence of zeta zeros in the Mellin transform of one signed radial-flux profile;
- the fact that prime-power radial flux is pointwise positive;
- the coincidence of the Mellin-Plancherel half-density with `Re(s)=1/2`;
- a linear shell combination followed by the same scalar Mellin transform, since every component already carries the same universal zeta factor.

It does **not** reject the broader signed-flux clue. What remains outside the theorem is exactly the hard part of that clue: a geometry-forced, genuinely cross-shell coupling applied to the signed profiles **before** scalar Mellin or endpoint integration, with a matched control showing that the coupling preserves arithmetic cancellation and produces a new sign/coercivity margin unavailable from the single-shell eta representation.

A decisive positive continuation must therefore exhibit a nonseparable coupled object `A_N` whose useful RH-relevant property is not inherited from the common factor in (12). A decisive negative continuation would show that the source-natural cross-shell couplings all reduce to fixed Möbius/divisor/Lambert algebra, shellwise positive statistics, or other classical transforms already present in the controls.

## Audit / falsification test

The core identity is exact. It can be falsified by any `n>1` and `s` with `Re(s)>1` for which direct numerical quadrature of (8) disagrees with (12). The critical-strip zero statement can be falsified by a zero of the finite factor in (12) with `0<Re(s)<1`; this is impossible because every such factor satisfies `|p^{s-1}|<1`.

The program-level negative classification would fail only if a later construction derives additional shell-coupled structure before Mellinization whose zero/sign condition cannot be reduced to the universal factor (12) or to the classical controls above.
