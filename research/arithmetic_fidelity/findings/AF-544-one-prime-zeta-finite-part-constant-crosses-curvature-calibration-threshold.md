# AF-544 — One prime-zeta finite-part constant crosses the curvature calibration threshold

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DIRICHLET-SOURCE` · `CURVATURE-COMPRESSION` · `NONLINEAR-RENORMALIZATION` · `CALIBRATION` · `CONDITIONING` · `FINITE-RESOLUTION` · `RECOVERY` · `NO-NOVELTY-CLAIM`

## Claim

AF-543 recovers the hidden cutoff exponent `theta` from the normalized-curvature defect by inverting the exact `D`-only curvature background with the reference coordinate

\[
r(t)=\frac{M_1(t)^2}{M_0(t)M_2(t)}.
\]

Exact knowledge of the full moment ratio is stronger than necessary, but its **finite part at the prime-zeta singularity is load bearing** at the AF-541 endpoint resolution.

Keep the AF-543 setup

\[
B_A=\lfloor A^\theta\rfloor,
\qquad
L_A=\log A,
\qquad
H_A=\log L_A,
\qquad
h_A=A^{-1},
\]

with `0<theta<1` and a common multiplier `C_A` satisfying

\[
C_A\to\infty,
\qquad
\frac{C_AH_A}{L_A}\to0.
\tag{1}
\]

Write

\[
P(1+t)=M_0(t)=\log(1/t)+\beta_P+O(t),
\tag{2}
\]

where

\[
\beta_P
=\sum_{m\ge2}\frac{\mu(m)}m\log\zeta(m)
=-0.3157184520\ldots\neq0
\tag{3}
\]

is the finite part of the prime zeta function at `s=1`. Then

\[
\boxed{
r(t)=\frac1{\log(1/t)+\beta_P}
+O\!\left(\frac{t}{\log(1/t)}\right).
}
\tag{4}
\]

Let `g_u` and its local inverse `Psi_u` be the AF-543 normal-form map, and for any common calibration `u(t)` define

\[
D_X^{[u]}(t)=\Psi_{u(t)}(\Delta_X(t)),
\qquad
R_A^{[u]}(t)=\frac{D_{B_A}^{[u]}(t)}{D_A^{[u]}(t)}.
\tag{5}
\]

At the endpoint, put

\[
\varepsilon_A=u(h_A)-r(h_A).
\]

Whenever `epsilon_A=o(L_A^{-1})`, the calibration error transported through the **ratio** satisfies

\[
\boxed{
\log\frac{R_A^{[u]}(h_A)}{R_A^\sharp(h_A)}
=
2(-\log\theta)\frac{C_A-1}{L_A^2}\,\varepsilon_A
\,(1+o(1)).
}
\tag{6}
\]

Thus the sharp common-calibration scale for the AF-541/AF-543 discriminator is

\[
\boxed{
\varepsilon_A
\asymp
\frac{L_A^3}{A(C_A-1)H_A}.
}
\tag{7}
\]

More precisely, if

\[
\lambda_A
=
\frac{A(C_A-1)H_A}{L_A^3}\,\varepsilon_A
\longrightarrow\lambda\in\mathbb R,
\tag{8}
\]

and the calibration has the correct boundary value `u(t)->0` so that the ratio correction vanishes at `t=0`, then

\[
\frac{H_A}{h_AL_A}Q_{h_A}\log R_A^{[u]}
\longrightarrow
-(1-\theta)+2(-\log\theta)\lambda.
\tag{9}
\]

Consequently the AF-543 estimator

\[
\widehat\theta_A^{[u]}
=1+rac{H_A}{h_AL_A}Q_{h_A}\log R_A^{[u]}
\]

converges to

\[
\boxed{
\theta+2(-\log\theta)\lambda.
}
\tag{10}
\]

This threshold separates two natural approximations to the reference coordinate.

The leading singular approximation

\[
u_0(t)=\frac1{\log(1/t)}
\tag{11}
\]

is **not** accurate enough. At `t=h_A`,

\[
u_0(h_A)-r(h_A)
=
\frac{\beta_P}{L_A^2}(1+o(1)),
\tag{12}
\]

so

\[
\left|
\frac{A(C_A-1)H_A}{L_A^3}
\bigl(u_0(h_A)-r(h_A)\bigr)
\right|
\asymp
\frac{A(C_A-1)H_A}{L_A^5}
\longrightarrow\infty.
\tag{13}
\]

The normalized curvature estimator therefore diverges rather than recovering `theta`.

By contrast, retaining the single finite-part constant,

\[
u_1(t)=\frac1{\log(1/t)+\beta_P},
\tag{14}
\]

gives from `(4)`

\[
\varepsilon_A
=O\!\left(\frac1{A L_A}\right),
\tag{15}
\]

and hence

\[
\frac{A(C_A-1)H_A}{L_A^3}\varepsilon_A
=O\!\left(\frac{C_AH_A}{L_A^4}\right)
=o(1).
\tag{16}
\]

Therefore

\[
\boxed{
-\frac{H_A}{h_AL_A}Q_{h_A}\log R_A^{[u_1]}
\longrightarrow1-\theta,
}
\tag{17}
\]

so the same cutoff exponent is recovered without evaluating the exact reference moment ratio.

The structural point is sharper than “calibration must be accurate.” A term of size `L_A^{-2}` is negligible relative to the reference coordinate itself, which is of size `L_A^{-1}`, but it is enormous after the downstream finite-resolution discriminator. Removing exactly that finite-part error pushes the residual calibration uncertainty down to order `1/(A L_A)`, safely below the transported fidelity threshold.

## Derivation

### 1. The prime-zeta finite part controls the reference moment ratio

The classical Möbius inversion for the prime zeta function is

\[
P(s)=\sum_{m\ge1}\frac{\mu(m)}m\log\zeta(ms).
\tag{18}
\]

Near `s=1`, the `m=1` term is

\[
\log\zeta(1+t)=\log(1/t)+O(t),
\]

while every `m>=2` term is analytic in a common neighborhood of `t=0`; the series of those analytic terms and its local derivatives converge normally there. Hence

\[
P(1+t)=\log(1/t)+\beta_P+a_1t+O(t^2)
\tag{19}
\]

for a finite constant `a_1`, with `beta_P` given by `(3)`.

Since

\[
M_1(t)=-\frac{d}{dt}P(1+t),
\qquad
M_2(t)=\frac{d^2}{dt^2}P(1+t),
\]

we obtain

\[
M_1(t)=\frac1t-a_1+O(t),
\qquad
M_2(t)=\frac1{t^2}+O(1).
\tag{20}
\]

Therefore

\[
\frac{M_1(t)^2}{M_2(t)}=1+O(t),
\tag{21}
\]

and division by `(19)` proves `(4)`.

At `t=h_A`, `(4)` gives

\[
r(h_A)=\frac1{L_A+\beta_P}+O\!\left(\frac1{A L_A}\right).
\tag{22}
\]

Equation `(12)` follows because

\[
\frac1{L_A}-\frac1{L_A+\beta_P}
=
\frac{\beta_P}{L_A(L_A+\beta_P)}.
\tag{23}
\]

### 2. Exact inverse sensitivity exposes the common-calibration cancellation

AF-543 defines

\[
g_u(D)
=
\frac{D[(1-2u)+(1-u)D]}{(1-u)(1+D)^2}.
\tag{24}
\]

For a fixed observed defect `y`, let

\[
z(u)=\Psi_u(y),
\qquad
g_u(z(u))=y.
\]

Direct differentiation gives

\[
\partial_u g_u(D)
=-\frac{D}{(1-u)^2(1+D)^2},
\tag{25}
\]

and

\[
\partial_Dg_u(D)
=
\frac{1+D-2u}{(1-u)(1+D)^3}.
\tag{26}
\]

Hence, on the AF-543 local inverse branch,

\[
\boxed{
\frac{d}{du}\log z(u)
=S(z(u),u)
:=
\frac{1+z(u)}{(1-u)(1+z(u)-2u)}.
}
\tag{27}
\]

The crucial fact is that the leading sensitivity is common to both cutoffs. Indeed,

\[
\partial_z S(z,u)
=-\frac{2u}{(1-u)(1+z-2u)^2}.
\tag{28}
\]

For the two observed defects, write

\[
z_X(u)=\Psi_u(\Delta_X(h_A)).
\]

Then

\[
\frac{d}{du}\log\frac{z_{B_A}(u)}{z_A(u)}
=S(z_{B_A}(u),u)-S(z_A(u),u).
\tag{29}
\]

By the mean-value theorem in the `z` variable,

\[
\frac{d}{du}\log\frac{z_{B_A}(u)}{z_A(u)}
=
\frac{2u\,[z_A(u)-z_{B_A}(u)]}
{(1-u)(1+\xi_A(u)-2u)^2}
\tag{30}
\]

for an intermediate `xi_A(u)`.

AF-543 gives `z_X(r)=D_X^\sharp=D_X(1+o(1))` at the endpoint, and AF-542 gives

\[
D_A(h_A)-D_{B_A}(h_A)
=
(-\log\theta)\frac{C_A-1}{L_A}(1+o(1)).
\tag{31}
\]

The AF-543 normal-form correction is only of relative order `L_A/(AH_A)`, so it is negligible on the much larger difference scale `(31)`. Thus

\[
z_A(r)-z_{B_A}(r)
=
(-\log\theta)\frac{C_A-1}{L_A}(1+o(1)).
\tag{32}
\]

Also `(22)` implies `r(h_A)=L_A^{-1}(1+o(1))`. If `epsilon_A=o(L_A^{-1})`, the whole calibration path from `r` to `r+epsilon_A` remains in the same uniformly invertible small-`u`, small-`z` branch, and `(27)` keeps each `z_X(u)` within a `1+o(1)` relative factor of `z_X(r)`. Equations `(30)`--`(32)` therefore hold uniformly along that path and give

\[
\frac{d}{du}\log\frac{z_{B_A}(u)}{z_A(u)}
=
2(-\log\theta)\frac{C_A-1}{L_A^2}(1+o(1)).
\tag{33}
\]

Integrating `(33)` over the calibration error proves `(6)`.

### 3. The endpoint discriminator turns `(6)` into a sharp accuracy scale

For each fixed `A`, both `u_0(t)` and `u_1(t)` tend to zero with the true `r(t)` as `t->0`. The defects and their inverse-normal-form carriers also vanish, so `(28)` shows that the calibration-induced **ratio** correction tends to zero at the boundary. Thus the extra term passes through

\[
Q_hf=f(h)-(1+h)f(0)
\]

only through its endpoint value.

AF-543 proved

\[
\frac{H_A}{h_AL_A}Q_{h_A}\log R_A^\sharp
\longrightarrow-(1-\theta).
\tag{34}
\]

Multiplying `(6)` by `H_A/(h_AL_A)=AH_A/L_A` yields

\[
\frac{H_A}{h_AL_A}
Q_{h_A}
\log\frac{R_A^{[u]}}{R_A^\sharp}
=
2(-\log\theta)
\frac{A(C_A-1)H_A}{L_A^3}\varepsilon_A
(1+o(1)).
\tag{35}
\]

Equations `(8)`, `(34)`, and `(35)` prove `(9)` and `(10)`. They also show that `(7)` is not merely sufficient: it is the first-order common-calibration transition scale. Errors little-o of `(7)` disappear; errors asymptotic to a nonzero multiple of `(7)` produce a nonzero limiting bias; larger same-sign errors inside the local regime dominate the desired signal.

For `u_0`, `(12)` and `beta_P!=0` force the normalized bias magnitude in `(13)` to diverge because `A H_A/L_A^5 -> infinity`. For `u_1`, `(15)` and `(1)` give `(16)`, proving `(17)`.

## Why common versus differential calibration matters

Equation `(27)` also exposes a stricter failure mode. The cancellation in `(30)` uses the **same** reference calibration for numerator and denominator. If the two cutoffs are instead inverted with independent errors `epsilon_{B,A}` and `epsilon_{A,A}`, then `S(z,u)=1+o(1)` individually, so the ratio acquires the first-order term

\[
(\varepsilon_{B,A}-\varepsilon_{A,A})(1+o(1))
\tag{36}
\]

before the smaller common-mode term `(6)`. Differential calibration must therefore satisfy

\[
\varepsilon_{B,A}-\varepsilon_{A,A}
=o\!\left(\frac{L_A}{AH_A}\right)
\tag{37}
\]

to be invisible to the endpoint discriminator.

So reference sharing is itself part of the retained relational structure. A common calibration error is suppressed by the additional factor `r(D_A-D_B) asymp (C_A-1)/L_A^2`; independent calibration errors are not.

## Fidelity / representation audit

AF-543 established that the exact reference coordinate `r(t)` repairs the AF-542 nonlinear representation failure. AF-544 identifies how much of that coordinate really has to survive.

The answer is not “the whole reference moment triple.” At this endpoint scale, the singular law `r~1/log(1/t)` alone is too coarse, but adding the single finite-part constant `beta_P` is enough. The representation budget is therefore smaller than AF-543's exact lift yet larger than the leading asymptotic class.

This is an explicit example of **target-relative asymptotic fidelity**. Two calibrations can be relatively equivalent at the reference-coordinate scale,

\[
\frac{u_0(h_A)}{r(h_A)}\to1,
\]

while only one is equivalent in the stronger seminorm induced by the downstream discriminator. The relevant approximation order is set by `(7)`, not by the size of `r` itself.

The result also makes provenance relational. The finite-part coordinate is common reference data, not source-specific cutoff data. Its error can be much larger than the final signal when viewed separately and still cancel sufficiently in the ratio—provided the same calibration is used on both branches. What survives is therefore a shared reference relation, not merely two individually accurate reconstructions.

## Prior-art / novelty audit

No novelty is claimed for the ingredients. Fröberg's classical prime-zeta framework and the Möbius inversion already recorded in `SOURCES.md` give `(18)`; the local expansion `(19)` is the standard logarithmic singularity plus its analytic finite part. Classical inverse/implicit-function conditioning explains the sensitivity calculation `(25)`--`(30)`, and the general conditioning language is already represented in the line's Demmel source anchor.

A targeted literature check also found modern work explicitly studying the coefficient expansion of the prime zeta function around `s=1`; this reinforces that neither `beta_P` nor the expansion itself should be treated as new. No standard source located in that check states the source-specific conclusion `(6)`--`(17)` for the AF-543 curvature normal form.

The durable Mathia delta is therefore the composition result: **the downstream curvature discriminator has a calculable common-calibration threshold, the leading `1/log` reference asymptotic lies on the wrong side of it, while retaining exactly the prime-zeta finite part moves the error to the safe `1/(A log A)` scale.** No broader novelty claim is made.

## Boundaries and failure modes

- **Common-multiplier regime.** The theorem inherits AF-543's common `C_A` and growth condition `(1)`; it does not restore AF-541's arbitrary unequal-multiplier result at curvature level.
- **Shared calibration is load bearing.** Formula `(6)` is a common-mode cancellation theorem. Independently calibrated numerator and denominator obey the stricter differential threshold `(37)`.
- **Local inverse branch.** The sensitivity argument assumes `epsilon_A=o(1/L_A)`, which includes both approximations `(11)` and `(14)` and every calibration accurate enough for `(7)`.
- **Finite-part sufficiency is scale-specific.** The fact that one constant suffices uses `h_A=1/A` and the AF-541 weighted contrast. A finer endpoint scale could require additional coefficients of the prime-zeta expansion.
- **Reference information remains extra structure.** `beta_P` is a statistic of the fixed prime reference. This is still a calibrated curvature representation, not a raw-curvature-only recovery theorem.
- **No prime-specific discriminator.** The recovered parameter is the artificial cutoff exponent `theta` inside the rigid transported-prime control family. The theorem does not distinguish rational primes from generalized-prime systems.
- **No RH consequence.** The result quantifies representation fidelity and calibration conditioning only.

## Decisive audit test

The finding can be killed in either of two places. First, recompute the singular expansion of `r(t)` from `(18)` and test whether the error after retaining `beta_P` is really `O(t/log(1/t))`; an omitted derivative-scale term larger than this would invalidate `(15)`. Second, differentiate the exact inverse relation `g_u(Psi_u(y))=y` and check `(27)`--`(30)`; any uncancelled `O(epsilon_A)` term in the common ratio would move the threshold from `(7)` back to the much smaller signal scale.

Under the stated common-reference setup, both calculations are exact: the individual `O(epsilon_A)` sensitivities cancel because their leading value is the same, leaving the `u(z_A-z_B)` factor in `(30)`.

## Consequence for the research line

AF-542 showed that value-level carrier equivalence is too weak for a later finite-difference discriminator. AF-543 repaired that failure using an exact reference coordinate. AF-544 now localizes the amount of reference information required: **one finite-part constant is enough at the natural endpoint scale, while dropping that constant is asymptotically catastrophic.**

This gives a concrete template for the broader Arithmetic Fidelity program. When a normal form depends on reference data, do not ask only whether an approximation to that reference converges. Differentiate the final relational observable with respect to the calibration coordinate, compute the target-relative threshold after all downstream amplification, and only then decide which asymptotic coefficients must be retained.