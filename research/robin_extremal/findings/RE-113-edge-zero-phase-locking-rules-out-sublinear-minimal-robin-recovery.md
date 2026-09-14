# RE-113 — edge-zero phase locking rules out sublinear minimal Robin recovery

**Status:** `LITERATURE+DERIVED + FINITE-ZERO-EDGE + EXTREME-FACE-SPECTRAL-PROJECTION + EDGE-ZERO-PHASE + ADAPTIVE-SELECTOR-COUPLING + INTER-BLOCK-RECOVERY + SUBLINEAR-ANTI-SATURATION + PRIOR-ART-AUDITED`.

`RE-112` compresses finite-edge source information into the scalar envelope

\[
\Phi(x)-x=O_\Theta(x^\Theta),
\qquad
\frac12<\Theta:=\sup_{\zeta(\rho)=0}\Re\rho<1,
\]

and obtains the recovery lower scale

\[
L:=V-Y\gg_\Theta h(C)Y^{2-\Theta}\log Y.
\]

Retaining the phase of the zeros that can actually contribute at order `x^Theta` gives a stronger statement. The fixed high-strip zero-density estimate already used in `RE-112` makes the reciprocal coefficients there absolutely summable. After normalization by `x^Theta`, every zero with real part strictly below `Theta` dies by dominated convergence. The surviving extreme-face profile is

\[
\boxed{
F_\Theta(u)
:=
\sum_{\substack{\zeta(\rho)=0\\ \Re\rho=\Theta}}
\frac{e^{i\Im(\rho)u}}{\rho}.
}
\tag{1}
\]

Zeros are counted with multiplicity. Conjugate zeros occur together, so the absolutely convergent series is real-valued for real `u`. It controls both the ordinary Chebyshev error and the complete CA event sweep:

\[
\boxed{
 x-\vartheta(x)
 =x^\Theta\bigl(F_\Theta(\log x)+o(1)\bigr),
\qquad
 x-\Phi(x)
 =x^\Theta\bigl(F_\Theta(\log x)+o(1)\bigr).
}
\tag{2}
\]

For an adaptive `RE-034` witness `C=C_b`, with `Y=log C`, the exact selector locks the Robin height to this same edge phase:

\[
\boxed{
F_\Theta(\log Y)
=b\,h(C)Y^{1-\Theta}\log Y+o(1).
}
\tag{3}
\]

Consequently, if the first recovery is genuinely sublinear, `L=o(Y)`, then every crossed event sees asymptotically the same vanishing edge phase and the `RE-110` forward workload satisfies

\[
M_+(C,D)=o(Y^\Theta).
\]

The exact one-sided workload budget then improves the scalar corridor to

\[
\boxed{
L
=
\omega\!\left(h(C)Y^{2-\Theta}\log Y\right).
}
\tag{4}
\]

Thus a sublinear adaptive recovery cannot saturate the finite-edge scale of `RE-112`. Any unbounded family satisfying a **fixed-constant** near-minimal upper bound and the standing short-recovery condition `L<=Y` must instead satisfy

\[
\boxed{
 h(C)\asymp
 \frac{Y^{\Theta-1}}{\log Y},
 \qquad
 L\asymp Y,
 \qquad
 F_\Theta(\log Y)\asymp1.
}
\tag{5}
\]

If the zero edge is not attained, then `F_Theta` is identically zero and such a fixed-constant near-minimal family is impossible. The finite-edge frontier therefore moves from a generic `Y^Theta` saturation packet to an **edge-attainment and selector-phase condition**.

## 1. Representation gate: project onto the extreme zero face

The primitive source data are the nontrivial zeros `rho=beta+i gamma` of `zeta`. The target observable is the signed forward discrepancy of the full CA event staircase on a recovery interval. The nuisance terms are lower-strip zeros, explicit-formula truncation, prime-power corrections between `psi` and `vartheta`, and higher CA layers between `vartheta` and `Phi`.

Normalize by `x^(-Theta)`. Under this normalization the only modes that can remain at order one are zeros with `beta=Theta`; all modes with `beta<Theta` should disappear. This extreme-face projection is target-independent: it is defined from the zeta zero set and `Theta` before any recovery interval is inspected.

Fix `sigma_0` with `1/2<sigma_0<Theta`. The Ingham-density argument persisted in `RE-112` gives

\[
\boxed{
\sum_{\substack{\zeta(\rho)=0\\ \Re\rho\ge\sigma_0}}
\frac1{1+|\Im\rho|}<\infty.
}
\tag{6}
\]

Hence (1) converges absolutely and uniformly. In particular `F_Theta` is bounded and uniformly continuous; as a uniform limit of trigonometric polynomials it is Bohr almost periodic. No higher-dimensional representation is needed after the scalar edge normalization.

## 2. The normalized source error converges to the edge profile

Use the same half-jump truncated Riemann--von Mangoldt formula as `RE-112`, with `T asy x`:

\[
\psi_0(x)-x
=
-\sum_{|\Im\rho|\le T}\frac{x^\rho}{\rho}
+O((\log x)^2).
\tag{7}
\]

After multiplying by `-x^(-Theta)`, zeros with `Re rho<sigma_0` contribute

\[
O\!\left(x^{\sigma_0-\Theta}(\log x)^2\right)=o(1).
\]

For `sigma_0<=Re rho<Theta`, each normalized term tends to zero and (6) provides a summable majorant independent of `x`, so dominated convergence gives an `o(1)` total. Zeros on the edge contribute `F_Theta(log x)+o(1)` because the omitted edge tail is uniformly controlled by the tail of (6). Therefore

\[
 x-\psi_0(x)
 =x^\Theta\bigl(F_\Theta(\log x)+o(1)\bigr).
\tag{8}
\]

The half-jump correction is `O(log x)`, while

\[
\psi(x)-\vartheta(x)
=O\!\left(x^{1/2}(\log x)^2\right)
=o(x^\Theta).
\]

This proves the first relation in (2). `RE-112` also gives

\[
\Phi_1(x)=\vartheta(x)+O(\log x),
\qquad
\Phi_{\ge2}(x)=O\!\left(x^{1/2}(\log x)^{3/2}\right),
\]

which proves the second relation in (2), and likewise

\[
 x-\Phi(x^-)
 =x^\Theta\bigl(F_\Theta(\log x)+o(1)\bigr).
\tag{9}
\]

The `o(1)` here is a global asymptotic. Writing it as a remainder `r(x)` means equivalently that `sup_(x>=X)|r(x)|->0`; this is the uniform tail form used on moving recovery intervals. Absolute convergence is asserted only on the fixed high strip (6), not for the full classical zero sum.

## 3. Adaptive selection locks Robin height to the edge phase

Let `C=C_b` be a regular adaptive-amplitude maximizer from `RE-034`, for fixed

\[
1-\Theta<b<\frac12.
\]

Write `Y=log C`, `h=h(C)>0`, and let `Z>Y` be its selector coordinate. `RE-034` proves

\[
\Phi(Z)=Y,
\qquad
Z-Y=(b+o(1))hY\log Y,
\tag{10}
\]

and

\[
Z-\vartheta(Z)=(b+o(1))hZ\log Z.
\tag{11}
\]

It also proves `h=o(1/log Y)`, hence `Z/Y->1` and `log Z-log Y->0`. Combining (2) with (11), then using uniform continuity of `F_Theta`, gives

\[
\boxed{
F_\Theta(\log Y)
=b\lambda_Y+o(1),
\qquad
\lambda_Y:=hY^{1-\Theta}\log Y.
}
\tag{12}
\]

Since `F_Theta` is bounded,

\[
\boxed{
\lambda_Y=O_{\Theta,b}(1),
\qquad
h(C)\ll_{\Theta,b}\frac{Y^{\Theta-1}}{\log Y}.
}
\tag{13}
\]

Thus an adaptive state does not sample an arbitrary point under the scalar `Y^Theta` envelope: its actual Robin height fixes the surviving edge phase at the same logarithmic scale.

## 4. Sublinear recovery is automatically super-minimal

Let `D` be the first later CA state with `h(D)<=0`, put `V=log D`, `L=V-Y`, and use the `RE-110` forward defect

\[
M_+(C,D)
=
\max_e(\eta_e-u_e)_+,
\qquad
u_e:=\Phi(\eta_e^-).
\tag{14}
\]

Here the second displayed symbol is only a typographical label; throughout the proof the physical left coordinate is

\[
\boxed{u_e:=\Phi(\eta_e^-).}
\tag{15}
\]

Assume `L=o(Y)`. The scalar `RE-112` lower bound gives

\[
L\gg_\Theta hY^{2-\Theta}\log Y
=\lambda_YY,
\]

so `lambda_Y=o(1)`. By (12), `F_Theta(log Y)=o(1)`.

Write (9) as

\[
\Phi(x^-)=x-x^\Theta\bigl(F_\Theta(\log x)+r(x)\bigr),
\qquad
\sup_{x\ge X}|r(x)|\to0.
\tag{16}
\]

For every crossed event with positive forward defect, `u_e in [Y,V]=Y+o(Y)`. Boundedness of `F_Theta`, (16), and `Theta<1` first imply `eta_e asy Y` uniformly. Hence `log eta_e-log Y=o(1)` uniformly. Uniform continuity of `F_Theta` and the uniform tail bound for `r` then give

\[
F_\Theta(\log\eta_e)+r(\eta_e)=o(1)
\]

uniformly over crossed events. Therefore

\[
\eta_e-u_e=o(Y^\Theta),
\qquad
\boxed{M_+(C,D)=o(Y^\Theta).}
\tag{17}
\]

The exact one-sided budget from `RE-110`,

\[
L M_+(C,D)
\ge(1+o(1))hY^2\log Y,
\]

now gives (4):

\[
L=\omega\!\left(hY^{2-\Theta}\log Y\right)
=\omega(\lambda_YY).
\tag{18}
\]

This is a qualitative but strict gain over `RE-112`: every genuinely sublinear adaptive recovery pays an unbounded factor beyond the scalar edge minimum.

## 5. Fixed-constant near-minimal recovery is forced to macroscopic scale

Consider an unbounded adaptive family satisfying `L<=Y` and, for one fixed `K`,

\[
L\le K hY^{2-\Theta}\log Y
=K\lambda_YY.
\tag{19}
\]

If `lambda_Y` had a subsequence tending to zero, (19) would make that recovery sublinear, contradicting (18). Hence `liminf lambda_Y>0`. Together with (13),

\[
\lambda_Y\asymp_{\Theta,b,K}1,
\qquad
h(C)\asymp_{\Theta,b,K}\frac{Y^{\Theta-1}}{\log Y}.
\tag{20}
\]

The scalar lower bound and `L<=Y` then yield `L asy Y`, while (12) gives a positive edge phase bounded away from zero. This proves (5).

If no zero satisfies `Re rho=Theta`, then `F_Theta` is identically zero. Equation (12) gives `lambda_Y->0`, so any fixed-constant upper bound (19) would force `L=o(Y)` and contradict (18). Therefore

\[
\boxed{
\text{an unbounded fixed-constant near-minimal adaptive recovery family}
\Longrightarrow
\exists\rho:\ \Re\rho=\Theta.
}
\tag{21}
\]

The `RE-112` saturation packet, if it occurs near the scalar minimum infinitely often, therefore cannot be a small-amplitude sublinear phenomenon. It requires an attained rightmost zero line, positive edge phase at the selected scale, edge-sized Robin height, and a macroscopic recovery corridor.

## 6. Prior-art boundary and source target

Explicit-formula spectral expansions and almost-periodic organization of prime-number-theorem errors are classical. Wintner's limiting-distribution work and the modern Akbary--Ng--Shahabi framework are conceptual prior-art boundaries for almost-periodic prime-counting errors. Their general limiting-distribution theory is not invoked as the exact uniform finite-edge expansion (2). That expansion is derived here directly from the specific high-strip reciprocal summability already established in `RE-112`; no novelty is claimed for the general principle that zero phases organize prime-counting errors.

The prior-art audit found no theorem imposing the selector-conditioned phase lock (12) or deriving the sublinear anti-saturation consequence (18) for colossally abundant Robin recovery. The line-specific contribution is the coupling of the extreme zero face to the exact adaptive selector and the one-sided CA workload budget.

The finite-edge frontier is therefore narrower than in `RE-112`. Sublinear recoveries cannot realize the scalar minimum. Fixed-constant near-minimal recoveries, if any, are forced into a **macroscopic edge-amplitude phase-lock regime**. The next useful source theorem should attack recurrence of

\[
F_\Theta(\log Y)\asymp1,
\qquad
h(C)\asymp\frac{Y^{\Theta-1}}{\log Y}
\]

on adaptive CA maxima, or couple this edge phase to the reciprocal-Mertens coordinate already locked to the same selector in `RE-034`. The separate `Theta=1` branch remains governed by the unconditional `RE-109`--`RE-111` workload problem.