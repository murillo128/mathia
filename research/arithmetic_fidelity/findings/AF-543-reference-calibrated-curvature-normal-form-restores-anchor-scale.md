# AF-543 — Reference-calibrated curvature normal form restores anchor scale

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DIRICHLET-SOURCE` · `OUTWARD-TRANSPORT` · `CURVATURE-COMPRESSION` · `NONLINEAR-RENORMALIZATION` · `RELATIONAL-LIFT` · `FINITE-RESOLUTION` · `RECOVERY` · `NO-NOVELTY-CLAIM`

## Claim

AF-542 showed that the AF-541 two-point carrier contrast is destroyed after passing to the raw normalized-curvature defect: the first nonlinear carrier correction is of order `C_A/L_A`, far larger than the desired endpoint shape signal `L_A/(A H_A)`. That obstruction can be removed at curvature level, but not by the naive `r=0` odds transform. The exact prime-reference moment ratio appearing in the curvature formula must be retained as a calibration coordinate.

Fix `0<\theta<1`, put

\[
B_A=\lfloor A^\theta\rfloor,
\qquad
L_A=\log A,
\qquad
H_A=\log L_A,
\qquad
h_A=A^{-1},
\]

and choose the same common multiplier sequence as in AF-542,

\[
C_A\to\infty,
\qquad
\frac{C_AH_A}{L_A}\to0.
\tag{1}
\]

For `X\in\{A,B_A\}`, let `Q_{X,C_A}`, the exact AF-525 carrier `D_X(t)`, and the actual normalized-curvature defect

\[
\Delta_X(t)
=
1-\frac{\kappa_{Q_{X,C_A}}(1+t)}{\kappa_P(1+t)}
\]

be exactly as in AF-542. With the prime-reference moments

\[
M_j(t)=\sum_p(\log p)^j p^{-1-t},
\]

define

\[
r(t)=\frac{M_1(t)^2}{M_0(t)M_2(t)}.
\tag{2}
\]

The `D`-only part of the exact curvature map is

\[
g_r(D)
=
\frac{D\bigl[(1-2r)+(1-r)D\bigr]}
{(1-r)(1+D)^2}.
\tag{3}
\]

For `r<1/2` and `D` sufficiently small this map is strictly increasing, because

\[
g_r'(D)
=
\frac{1+D-2r}{(1-r)(1+D)^3}>0.
\tag{4}
\]

Let `\Psi_r` denote its local inverse at the origin and define the **reference-calibrated curvature normal form**

\[
D_X^\sharp(t):=\Psi_{r(t)}\!\bigl(\Delta_X(t)\bigr).
\tag{5}
\]

Thus `(5)` uses the actual curvature defect plus the canonical reference coordinate `r(t)`; it does not use the hidden cutoff `X`, the multiplier `C_A`, or the carrier `D_X` itself.

Write

\[
R_A^\sharp(t)
=\frac{D_{B_A}^\sharp(t)}{D_A^\sharp(t)}.
\tag{6}
\]

The ratio has a continuous boundary extension at `t=0`, and at the endpoint

\[
\boxed{
\log\frac{R_A^\sharp(h_A)}{R_A(h_A)}
=
-2(1-\theta)\frac{L_A}{A H_A}
+o\!\left(\frac{L_A}{A H_A}\right),
}
\tag{7}
\]

where `R_A=D_{B_A}/D_A` is the exact carrier ratio from AF-542. Moreover,

\[
\lim_{t\downarrow0}
\log\frac{R_A^\sharp(t)}{R_A(t)}=0.
\tag{8}
\]

Therefore, for the same weighted boundary functional

\[
Q_hf=f(h)-(1+h)f(0),
\]

AF-541 and `(7)`--`(8)` give

\[
\boxed{
-\frac{H_A}{h_A L_A}
Q_{h_A}\log R_A^\sharp
\longrightarrow
1-\theta.
}
\tag{9}
\]

Equivalently,

\[
\boxed{
\widehat\theta_A
:=1+rac{H_A}{h_A L_A}
Q_{h_A}\log R_A^\sharp
\longrightarrow\theta.
}
\tag{10}
\]

So AF-542's direct-transfer obstruction is not a no-go for all curvature-level renormalizations. Exact inversion of the universal `D`-only curvature background removes the much larger order-`C_A/L_A` contamination. The remaining first-moment curvature term lives exactly on the AF-541 finite-resolution scale and reverses the carrier coefficient, producing the minus sign in `(9)` rather than erasing the signal.

This is a recovery theorem for the cutoff exponent inside the rigid common-multiplier control family. It is not a rational-prime discriminator and it is not a curvature-only theorem in the strict sense: the calibration coordinate `r(t)` is a known statistic of the fixed prime reference and is load bearing.

## Derivation

### 1. Isolate the universal nonlinear curvature background

Use the AF-525/AF-542 notation

\[
\rho_0=\eta(1+D_X),
\qquad
\rho_1=\eta(1+E_{1,X}),
\qquad
\rho_2=\eta(1+E_{2,X}),
\]

with

\[
\eta=C_A^{-1-t}.
\]

AF-542 equation (5), multiplied by `D_X`, is the exact identity

\[
\Delta_X
=
\frac{
D_X(1-2r)+(1-r)D_X^2
-(1+D_X)E_{2,X}
+2rE_{1,X}
+rE_{1,X}^2
}
{(1-r)(1+D_X)^2}.
\tag{11}
\]

Setting `E_{1,X}=E_{2,X}=0` gives exactly `(3)`. Hence

\[
\Delta_X
=g_r(D_X)+\delta_X,
\tag{12}
\]

where

\[
\delta_X
=
\frac{
-(1+D_X)E_{2,X}
+2rE_{1,X}
+rE_{1,X}^2
}
{(1-r)(1+D_X)^2}.
\tag{13}
\]

At `t=h_A`, AF-542 gives `r=o(1)` and `D_X=o(1)` for both cutoffs. Equation `(4)` therefore makes `g_r` uniformly locally invertible for all sufficiently large `A`. Since `\Delta_X/D_X\to1`, the observed defect lies in the same local inverse branch and `(5)` is well defined.

By the mean-value theorem applied to

\[
g_r(D_X^\sharp)-g_r(D_X)=\delta_X,
\]

and `(4)`,

\[
\frac{D_X^\sharp-D_X}{D_X}
=
(1+o(1))
\left(
2r\frac{E_{1,X}}{D_X}
-\frac{E_{2,X}}{D_X}
+r\frac{E_{1,X}^2}{D_X}
\right)
\tag{14}
\]

at the endpoint. The large `-D_X` correction exposed by AF-542 is absent: it belonged to `g_r` and has been inverted exactly rather than treated perturbatively.

### 2. The surviving first-moment term has an exact source/reference factorization

Put

\[
k_A(t)=\frac{1-\eta}{\eta}=C_A^{1+t}-1,
\qquad
u_j(X,t)=\frac{B_j(X,t)}{M_j(t)},
\]

where

\[
B_j(X,t)=\sum_{p\le X}(\log p)^j p^{-1-t}.
\]

AF-525 gives

\[
D_X=k_A\nu_0,
\tag{15}
\]

\[
E_{1,X}
=k_A\nu_1
+d_A\frac{M_0}{M_1}(1-\nu_0),
\qquad d_A=\log C_A,
\tag{16}
\]

and

\[
E_{2,X}
=k_A\nu_2
+2d_A\frac{M_1}{M_2}(1-\nu_1)
+d_A^2\frac{M_0}{M_2}(1-\nu_0).
\tag{17}
\]

The prefix part of the first term in `(14)` simplifies exactly:

\[
2r\frac{k_A\nu_1}{k_A\nu_0}
=
\boxed{
2\frac{M_1}{M_2}\frac{B_1(X,t)}{B_0(X,t)}.
}
\tag{18}
\]

This factorization is the key residual after calibration. It couples one reference scale `M_1/M_2` to one cutoff-local logarithmic mean `B_1/B_0`.

At `t=h_A`, the classical prime-zeta/Mertens estimates already audited in AF-525, AF-529, and AF-542 give

\[
\frac{M_1(h_A)}{M_2(h_A)}
=
\frac1A(1+o(1)),
\tag{19}
\]

and, uniformly for the two fixed power-separated cutoffs,

\[
\frac{B_1(A,h_A)}{B_0(A,h_A)}
=
\frac{L_A}{H_A}(1+o(1)),
\tag{20}
\]

\[
\frac{B_1(B_A,h_A)}{B_0(B_A,h_A)}
=
\theta\frac{L_A}{H_A}(1+o(1)).
\tag{21}
\]

Define the endpoint signal scale

\[
s_A:=\frac{L_A}{A H_A}.
\tag{22}
\]

Equations `(18)`--`(21)` show that the prefix contribution to `(14)` equals

\[
2s_A(1+o(1))
\quad\text{for }X=A,
\tag{23}
\]

and

\[
2\theta s_A(1+o(1))
\quad\text{for }X=B_A.
\tag{24}
\]

### 3. Every other moment correction is smaller than the endpoint signal

The multiplier-shift part of `(16)` contributes to `2rE_{1,X}/D_X` at order

\[
O\!\left(
\frac{d_A}{k_A(h_A)}s_A
\right)
=o(s_A),
\tag{25}
\]

because `C_A\to\infty` implies

\[
\frac{d_A}{k_A(h_A)}
\sim\frac{\log C_A}{C_A}\to0.
\]

For `(17)`, the prefix term satisfies

\[
\frac{\nu_2}{\nu_0}
=
O\!\left(\frac{L_A^3}{A^2H_A}\right)
=o(s_A),
\tag{26}
\]

while the linear and quadratic support-shift terms, after division by `D_X`, are respectively

\[
O\!\left(
\frac{d_A}{k_A(h_A)}s_A
\right)
=o(s_A)
\tag{27}
\]

and

\[
O\!\left(
\frac{d_A^2}{k_A(h_A)}
\frac{L_A^2}{A^2H_A}
\right)
=o(s_A).
\tag{28}
\]

Finally AF-542's bounds give `E_{1,X}/D_X=O(L_A^2/(AH_A))`; together with `r=O(L_A^{-1})`, `D_X=o(1)`, and `(1)`, this implies

\[
r\frac{E_{1,X}^2}{D_X}=o(s_A).
\tag{29}
\]

Substituting `(23)`--`(29)` into `(14)` yields the two endpoint normal-form errors

\[
\boxed{
\log\frac{D_A^\sharp(h_A)}{D_A(h_A)}
=2s_A+o(s_A),
}
\tag{30}
\]

\[
\boxed{
\log\frac{D_{B_A}^\sharp(h_A)}{D_{B_A}(h_A)}
=2\theta s_A+o(s_A).
}
\tag{31}
\]

Taking the difference proves `(7)`.

### 4. The boundary correction vanishes

For fixed `A` and `C_A`, as `t\downarrow0`,

\[
P(1+t)\to\infty,
\qquad
r(t)\to0,
\qquad
D_X(t)\to0.
\]

The finite-prefix ratios satisfy `\nu_1=o(\nu_0)` and `\nu_2=o(\nu_0)`, while the support-shift terms in `(16)`--`(17)` vanish because `M_0/M_1\to0` and `M_1/M_2\to0`. Therefore `(14)` gives

\[
\frac{D_X^\sharp(t)}{D_X(t)}\to1
\qquad(t\downarrow0).
\tag{32}
\]

The common multiplier and prime-zeta factors cancel in `D_{B_A}/D_A`, so its limit is finite and positive. Equation `(32)` then proves `(8)`.

### 5. The calibrated curvature contrast recovers the hidden exponent

AF-541 applies in particular to the common-multiplier subfamily and gives

\[
\frac{H_A}{h_AL_A}
Q_{h_A}\log R_A
\longrightarrow1-\theta.
\tag{33}
\]

By `(7)`--`(8)`,

\[
\frac{H_A}{h_AL_A}
Q_{h_A}
\log\frac{R_A^\sharp}{R_A}
\longrightarrow-2(1-\theta).
\tag{34}
\]

Adding `(33)` and `(34)` proves `(9)` and `(10)`.

The sign reversal is not a defect in the decoder. It records the load-bearing first-moment residual that remains after the larger universal nonlinear carrier background has been removed exactly.

## Why the prime-reference calibration is load bearing

A tempting renormalization is the `r=0` odds transform

\[
D_X^{\mathrm{odds}}
=\frac{\Delta_X}{1-\Delta_X},
\tag{35}
\]

because `g_0(D)=D/(1+D)`. It does remove the AF-542 order-`D` nonlinearity when `r=0`, but the actual reference has `r(h_A)\asymp L_A^{-1}`.

Even before restoring the `E`-terms, direct substitution gives

\[
\frac{D^{\mathrm{odds}}}{D}
=
\frac{(1-2r)+(1-r)D}{1-r+D}.
\tag{36}
\]

At `D=0`,

\[
\partial_D
\log\!\left(
\frac{(1-2r)+(1-r)D}{1-r+D}
\right)
=
\frac{r^2}{(1-r)(1-2r)}.
\tag{37}
\]

AF-542 gives `D_A(h_A)-D_{B_A}(h_A)\asymp C_A/L_A`. Hence the cutoff-dependent residual left by `(35)` is of order

\[
\frac{C_A}{L_A^3},
\tag{38}
\]

whereas the target shape signal is only `s_A=L_A/(A H_A)`. Their ratio is

\[
\frac{A C_A H_A}{L_A^4}\to\infty.
\tag{39}
\]

Thus the simple odds transform still fails at the required transverse resolution. The exact `r(t)` calibration in `(3)`--`(5)` is not cosmetic: it removes a second, much smaller value-level background that is nevertheless enormous relative to the desired endpoint discriminator.

## Fidelity / representation audit

The observation chain is now

\[
\text{anchored source}
\longrightarrow
\Delta_X(t)
\longrightarrow
(\Delta_X(t),r(t))
\longrightarrow
D_X^\sharp(t)
\longrightarrow
Q_h\log R_A^\sharp.
\]

The lift adds no source-specific mark: `r(t)` depends only on the fixed prime reference already used to normalize the curvature. But it **does add representation information beyond the scalar normalized-curvature defect itself**. In strict Arithmetic Fidelity language, the theorem therefore establishes fidelity for a reference-calibrated curvature representation, not for raw curvature alone.

The result also sharpens AF-542's composition lesson. The obstruction there came from applying an ill-conditioned relational statistic after an uncontrolled nonlinear approximation. Here the dominant nonlinear stage is first put into an exact normal form. Once that background is removed, the previously subleading first-moment coupling becomes visible at precisely the target scale.

The surviving coefficient is not the original carrier coefficient. Compression has changed the observable geometry: after calibration, the first-moment residual contributes `-2(1-\theta)` relative to the carrier's `+(1-\theta)`, leaving the total `-(1-\theta)`. Recovery survives, but not by pretending curvature is the carrier.

## Prior-art / novelty audit

No novelty is claimed for the analytic ingredients. The inverse-function step in `(3)`--`(5)` is elementary one-variable calculus; the prime-zeta and Mertens moment asymptotics in `(19)`--`(21)` are the same classical inputs already sourced in AF-525, AF-529, AF-541, and AF-542. The decomposition `(11)` is the existing exact AF-525/AF-542 curvature identity.

A targeted literature check found only the expected general languages—local inversion/nonlinear calibration and classical Mertens/prime-zeta asymptotics—rather than a standard theorem about this specific transported-prime curvature normal form. No novelty claim is made from that absence. The durable Mathia delta is the source-specific representation result: **the AF-542 nonlinear obstruction can be normalized away exactly if the reference moment coordinate `r` is retained, and the remaining curvature signal has a computable nonzero asymptotic coefficient.**

## Boundaries and failure modes

- **Reference calibration is extra structure.** Equation `(5)` is not a function of `\Delta_X` alone. Any claim that raw normalized curvature by itself recovers `\theta` would need a separate theorem or a way to reconstruct `r` at the required accuracy.
- **Common multiplier only.** The theorem keeps AF-542's common `C_A`. It does not recover the uniform arbitrary-unequal-multiplier result of AF-541 at curvature level.
- **AF-525 growth regime remains load bearing.** The estimates use `C_A\to\infty` and `C_AH_A/L_A\to0`. Fixed multipliers or more aggressive growth require a separate calculation.
- **Boundary-limit observation.** The `t=0` term is the continuous boundary extension of the ratio, not a finite individual curvature defect: both defects vanish there.
- **Exact calibration, not noisy calibration.** The theorem does not quantify how errors in `r(t)` propagate through `\Psi_r`. Because the target scale is `L_A/(AH_A)`, approximate reference calibration requires its own conditioning theorem.
- **Cutoff exponent only.** The recovered parameter is `\theta`; the proof uses coarse Mertens moment structure and does not establish rational-prime identity against generalized-prime controls.
- **No RH consequence.** This is a representation/recovery theorem inside the Arithmetic Fidelity laboratory. It does not constrain Riemann zeros.

## Decisive audit test

For any proposed curvature-level repair of AF-542, first separate the `D`-only background from the `E_1,E_2` moment residuals in the exact identity `(11)`. A valid repair must be tested after the same endpoint contrast used by the discriminator.

For the normal form `(5)`, falsification reduces to one coefficient calculation: after calibration, show that either `(18)` is not the leading endpoint residual or that the supposedly smaller terms `(25)`--`(29)` survive at order `s_A`. Under `(1)`, the exact factorization `(18)` and the audited prime-moment asymptotics force the coefficient `2\alpha` for cutoff `A^\alpha`, so the ratio correction is `-2(1-\theta)` and the final coefficient in `(9)` is nonzero.

## Consequence for the research line

AF-542 closed the naive inference `\Delta_X\sim D_X =>` the AF-541 statistic transfers. AF-543 gives the first curvature-level escape from that obstruction. The escape is structurally informative: **remove the full universal nonlinear background before applying the transverse discriminator, and retain the reference coordinate needed to define that normal form.**

This does not settle the stronger live question of whether a finite-point statistic of raw curvature alone can succeed. It narrows it. Any raw-curvature-only route must now either reconstruct the needed reference calibration internally, cancel its effect relationally, or prove that a different nonlinear normal form avoids the `r` dependence. Conversely, if exact reference information is admitted, the common-multiplier endpoint obstruction of AF-542 is no longer fatal.