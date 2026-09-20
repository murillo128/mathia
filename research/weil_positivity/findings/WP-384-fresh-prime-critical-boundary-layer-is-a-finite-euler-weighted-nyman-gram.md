---
id: WP-384
title: Fresh-prime critical boundary layer is a finite-Euler-weighted Nyman Gram
branch: weil_positivity
status: supported
kind: pointed-cyclotomic-boundary-layer-classicalization
claim_strength: exact RH-independent fresh-prime scaling theorem showing that the canonical critical pointed-Dirichlet boundary layer genuinely escapes compact-open continuity but its full fixed-base Gram limit is the classical Nyman modulus-square carrier multiplied by finite Euler/Jordan factors; every mixed shell retains strictly positive energy, so this boundary escape does not produce prime-power selection, Gamma/polar completion, or Weil positivity
created: 2026-09-20
related: [WP-168, WP-378, WP-379, WP-380, WP-381, WP-382, WP-383]
clues: [CLUE-weil-positivity-noncharacter-finite-archimedean-incidence]
prior_art:
  - classical cyclotomic fresh-prime recursion and Möbius decomposition
  - Nyman--Beurling/Müntz Mellin geometry and Hardy-space formulations already audited in WP-168 and SOURCES.md
  - classical generalized Jordan-totient identity J_s(m)=m^s product_{p|m}(1-p^{-s})
---

# WP-384 — Fresh-prime critical boundary layer is a finite-Euler-weighted Nyman Gram

## Claim

`WP-383` left a precise escape: a useful response could be genuinely boundary-accumulating or scale-dependent, so that the fresh-prime spectator does not disappear under a fixed compact-open-continuous map. The most canonical such test is already present in the pointed local Dirichlet geometry itself. Keep a fixed base shell `m>1`, adjoin a fresh prime `q`, apply the source-forced critical half-density, and measure the intrinsic pointed energy

\[
V_{m,q}(z):=\frac{F_{mq}(z)}{\sqrt{mq}},
\qquad
F_n(z):=\log\Phi_n(z),
\tag{1}
\]

with

\[
D_1(F)=\left\|\frac{F(z)-F(1)}{z-1}\right\|_{H^2}^2.
\tag{2}
\]

Because `q` is fresh, `mq` has at least two distinct prime divisors, hence

\[
F_{mq}(1)=\Lambda(mq)=0.
\tag{3}
\]

The family in (1) is a genuine boundary layer: as `q -> infinity` through primes not dividing `m`,

\[
V_{m,q}\longrightarrow0
\tag{4}
\]

uniformly on every compact subdisk, while its pointed energy converges to a **strictly positive** limit. More generally, for any fixed finite set of bases `m,n>1` and fresh primes `q` avoiding all of them,

\[
\boxed{
\langle V_{m,q},V_{n,q}\rangle_{D_1}
\longrightarrow
\frac1{2\pi}\int_{-\infty}^{\infty}
 c_m(\tau)\overline{c_n(\tau)}
 \frac{|\zeta(\tfrac12+i\tau)|^2}{\tfrac14+\tau^2}
\,d\tau,
}
\tag{5}
\]

where

\[
\boxed{
c_m(\tau)
:=m^{-1/2}J_{\frac12-i\tau}(m)
=m^{-i\tau}\prod_{p\mid m}
\left(1-p^{-1/2+i\tau}\right),
}
\tag{6}
\]

and

\[
J_s(m):=\sum_{d\mid m}\mu(m/d)d^s
=m^s\prod_{p\mid m}(1-p^{-s}).
\tag{7}
\]

In particular,

\[
\boxed{
\lim_{q\to\infty}D_1(V_{m,q})
=rac1{2\pi}\int_{-\infty}^{\infty}
\frac{|\zeta(\tfrac12+i\tau)|^2}{\tfrac14+\tau^2}
\prod_{p\mid m}
\left|1-p^{-1/2+i\tau}\right|^2
\,d\tau>0.
}
\tag{8}
\]

Thus the sharp boundary-sensitive escape from `WP-383` exists, but its sign mechanism immediately classicalizes. Equation (8) is exactly the `WP-168` Nyman modulus-square density with the finitely many Euler factors at `p|m` removed, up to the irrelevant conjugation inside an absolute value. It is positive for the same unconditional autocorrelation reason as `WP-168`, not because a Weil explicit-formula form has acquired the correct sign.

This is a decisive negative for the canonical fixed-base fresh-prime boundary layer. Every term `mq` in the family is a mixed-prime shell with `Lambda(mq)=0`, yet its critical geometric energy stays bounded away from zero. The layer therefore does not realize prime-power support, and it generates neither the archimedean Gamma term nor the polar counterterm required by global Weil positivity.

**Classification:** `EXACT-DERIVED + GENUINE-BOUNDARY-LAYER + NON-COMPACT-OPEN + FIXED-BASE-GRAM-LIMIT + JORDAN-EULER-MULTIPLIER + NYMAN-CLASSICALIZATION + MIXED-SHELL-POSITIVE-CONTROL + DECISIVE-NEGATIVE + NOT-A-WEIL-BRIDGE`.

## 1. Fresh-prime cyclotomic incidence gives a finite dilation packet

Fix `m>1` and a prime `q` with `q` not dividing `m`. The standard cyclotomic recursion gives

\[
\Phi_{mq}(z)=\frac{\Phi_m(z^q)}{\Phi_m(z)},
\tag{9}
\]

so for the analytic logarithms normalized by `F_n(0)=0`,

\[
F_{mq}(z)=F_m(z^q)-F_m(z).
\tag{10}
\]

Use the full-root controls of `WP-168`,

\[
A_N(z):=\log\frac{1-z^N}{1-z}.
\tag{11}
\]

For `m>1`, Möbius inversion and `sum_{d|m} mu(m/d)=0` give

\[
F_m(z)=\sum_{d\mid m}\mu(m/d)A_d(z).
\tag{12}
\]

Moreover

\[
A_d(z^q)=A_{dq}(z)-A_q(z).
\tag{13}
\]

The common `A_q` term cancels in the Möbius sum, hence

\[
F_m(z^q)=\sum_{d\mid m}\mu(m/d)A_{dq}(z),
\tag{14}
\]

and therefore

\[
\boxed{
F_{mq}(z)
=\sum_{d\mid m}\mu(m/d)
\bigl(A_{dq}(z)-A_d(z)\bigr).
}
\tag{15}
\]

This identity is the entire arithmetic input. No zero data, RH assumption, fitted kernel, or regularization is used.

For any fixed `0<r<1`, `F_m(z^q)->F_m(0)=0` uniformly on `|z|<=r`, while `F_m(z)` is fixed. Division by `sqrt(mq)` therefore proves (4). On the other hand, because (3) holds,

\[
T_1V_{m,q}
=\frac{V_{m,q}(z)}{z-1}
=\frac{B_{mq}(z)}{\sqrt{mq}},
\qquad
B_n(z):=\frac{\Lambda(n)-F_n(z)}{1-z},
\tag{16}
\]

so this is exactly a normalized version of the canonical Hardy boundary response singled out as outside the compact-open hypothesis in `WP-383`.

## 2. `WP-168` gives the exact fixed-base Gram limit

`WP-168` proved that for

\[
U_N:=N^{-1/2}A_N
\tag{17}
\]

and sequences with `M/N -> r`,

\[
\langle U_N,U_M\rangle_{D_1}
\longrightarrow
K(r)
=r^{-1/2}\int_0^\infty a(x)a(x/r)\,dx,
\tag{18}
\]

where

\[
a(x):=H_{\lfloor x\rfloor}-\log x-\gamma
\in L^2(0,\infty).
\tag{19}
\]

Divide (15) by `sqrt(mq)`. The fixed terms `A_d/sqrt(mq)` vanish in `D_1`, because only finitely many divisors `d|m` occur. For the growing terms,

\[
\frac{A_{dq}}{\sqrt{mq}}
=\sqrt{\frac d m}\,U_{dq}.
\tag{20}
\]

Applying (18) to every pair `dq,eq` in the finite divisor packets and summing gives the continuum profiles

\[
\boxed{
h_m(x)
:=\frac1{\sqrt m}
\sum_{d\mid m}\mu(m/d)a(x/d),
}
\tag{21}
\]

with

\[
\boxed{
\langle V_{m,q},V_{n,q}\rangle_{D_1}
\longrightarrow
\int_0^\infty h_m(x)h_n(x)\,dx.
}
\tag{22}
\]

This proves that the persistence of energy in (8) is not an artifact of evaluating one coordinate or of an arbitrary boundary regularization. It is the scaling limit of the intrinsic positive `D_1` Gram itself.

## 3. Mellin diagonalization exposes the finite Euler factors

`WP-168` derived, for `0<Re(s)<1`,

\[
\int_0^\infty a(x)x^{s-1}\,dx
=-\frac{\zeta(1-s)}{s}.
\tag{23}
\]

Dilation in (21) gives

\[
\begin{aligned}
\int_0^\infty h_m(x)x^{s-1}\,dx
&=-\frac1{\sqrt m}
\left(\sum_{d\mid m}\mu(m/d)d^s\right)
\frac{\zeta(1-s)}s\\
&=-\frac{J_s(m)}{\sqrt m}
\frac{\zeta(1-s)}s.
\end{aligned}
\tag{24}
\]

The divisor polynomial is the generalized Jordan factor (7). Put `s=1/2-i tau`. Mellin Plancherel applied to (22) yields (5). On the diagonal,

\[
|c_m(\tau)|^2
=\prod_{p\mid m}
\left|1-p^{-1/2+i\tau}\right|^2,
\tag{25}
\]

because `|m^{-i tau}|=1`. If

\[
\zeta_m(s):=\zeta(s)\prod_{p\mid m}(1-p^{-s}),
\tag{26}
\]

then (8) can equivalently be written

\[
\lim_{q\to\infty}D_1(V_{m,q})
=\frac1{2\pi}\int_{-\infty}^{\infty}
\frac{|\zeta_m(\tfrac12+i\tau)|^2}
{\tfrac14+\tau^2}
\,d\tau.
\tag{27}
\]

For fixed `m`, every local multiplier is uniformly separated from zero and infinity on the critical line:

\[
1-p^{-1/2}
\le
\left|1-p^{-1/2+i\tau}\right|
\le
1+p^{-1/2}.
\tag{28}
\]

Consequently, with `C=||a||_2^2=K(1)>0`,

\[
C\prod_{p\mid m}(1-p^{-1/2})^2
\le
\lim_{q\to\infty}D_1(V_{m,q})
\le
C\prod_{p\mid m}(1+p^{-1/2})^2.
\tag{29}
\]

The mixed-shell energy is therefore not merely nonzero at generic parameters; it is quantitatively positive for every fixed `m>1`.

## 4. Matched controls and falsification

The control `m=1` removes the Möbius packet and recovers exactly the `WP-168` full-root Nyman carrier. Thus the zeta modulus square in (5) is not created by prime-power incidence; it is already the universal coefficient-lattice carrier.

For every `m>1`, the indices `mq` are mixed-prime and satisfy `Lambda(mq)=0`, while (29) gives a strictly positive limiting norm. In particular, the explicit mixed base `m=6` yields

\[
|c_6(\tau)|^2
=|1-2^{-1/2+i\tau}|^2
 |1-3^{-1/2+i\tau}|^2>0
\tag{30}
\]

for every real `tau`. The boundary layer therefore fails the most direct prime-power-support control.

The diagonal density depends on `m` only through its radical. Replacing `p` by `p^a` in a fixed base changes the harmless phase `m^{-i tau}` in (6) but not (25). Thus this positive scalarization also forgets prime-power exponent information at the level of individual energies.

`WP-380` does not already imply this result. Its universality theorem requires the reciprocal-root mass `eta(n)=sum_{p|n}p^{-1/2}` to tend to zero. Along `n=mq` with fixed `m>1`, the contribution from the primes dividing `m` stays fixed, so that hypothesis deliberately fails. The present calculation covers exactly that missing fixed-base regime.

The strongest possible reinterpretation of (27) also fails. Removing finitely many Euler factors from zeta does not produce the completed explicit-formula distribution: the density remains an absolutely continuous modulus square, no Gamma factor appears, and no polar subtraction is generated. Off-critical zeros cannot make the norm negative. The positivity is therefore logically incapable of forcing RH.

## 5. Representation audit

**Intrinsic/native lens.** The construction uses only the primitive cyclotomic shells, fresh-prime incidence, the source-forced critical half-density, and the pointed local Dirichlet norm already intrinsic to Prime Circle. No test kernel is chosen.

**Boundary-response lens.** Equation (4) together with (29) is the decisive topology change: the normalized shells disappear on every fixed interior compact set while retaining positive `D_1` energy. This is a genuine boundary concentration, not an interior packet in disguise, and so it really does test the escape left by `WP-383`.

**Mellin/spectral lens.** The boundary layer becomes multiplication of the universal Nyman carrier by the finite Dirichlet polynomials `c_m(tau)`. This representation forgets the original cyclotomic branch geometry but makes the sign source transparent: the Gram is an ordinary `L^2` norm against a fixed positive spectral density.

**Arithmetic lens.** The generalized Jordan factor remembers which primes divide the fixed base, but after modulus-square scalarization its exponent data disappears from the diagonal and mixed shells remain positive. Thus the extra arithmetic decoration is real but is the wrong decoration for a Mangoldt selector.

The representation-invariant conclusion is the exact fixed-base Gram limit (5). The Nyman/Euler language is its spectral identification, not an independent assumption.

## 6. Prior-art and novelty audit

No novelty is claimed for the ingredients in isolation: the cyclotomic recursion and Möbius formula are classical, the generalized Jordan identity (7) is elementary multiplicative number theory, and `WP-168` already audited the Mellin profile (23) against Nyman--Beurling/Müntz and Hardy-space prior art recorded in `SOURCES.md`.

A bounded targeted literature search for Nyman--Beurling/Müntz formulas with finite Euler or Jordan factors found broad classical/generalized Dirichlet-series overlap rather than evidence that the Mellin multiplier itself is new. The line-specific contribution claimed here is narrower: combining the exact fresh-prime **primitive cyclotomic** packet with the forced `D_1` critical scaling shows that the first canonical non-compact-open boundary escape left by `WP-383` has the explicit fixed-base limit (5)--(8) and therefore classicalizes instead of producing Weil positivity.

## Consequence for the research line

The route

\[
\boxed{
\text{fresh-prime primitive shell}
+\text{critical }(mq)^{-1/2}\text{ scaling}
+\text{pointed }D_1\text{ boundary energy}
\not\Rightarrow
\text{prime-power selector or global Weil positivity}
}
\tag{31}
\]

is now closed for every fixed base `m` and every fixed finite packet of bases. The obstruction is stronger than a failure of compact-open continuity: the genuinely surviving boundary mass is explicitly a finite-Euler-weighted Nyman Gram.

This does **not** rule out a double scaling in which the base `m` itself grows with `q`, nor a boundary construction that retains phase or couples the finite and archimedean sectors before taking a modulus square. Those routes remain live only if the scale is source-forced and if the resulting positivity produces the Gamma/polar completion rather than another weighted Nyman carrier.