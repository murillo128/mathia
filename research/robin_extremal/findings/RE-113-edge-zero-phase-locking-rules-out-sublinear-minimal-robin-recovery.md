# RE-113 — edge-zero phase locking rules out sublinear minimal Robin recovery

**Status:** `LITERATURE+DERIVED + FINITE-ZERO-EDGE + EXTREME-FACE-SPECTRAL-PROJECTION + EDGE-ZERO-PHASE + ADAPTIVE-SELECTOR-COUPLING + INTER-BLOCK-RECOVERY + SUBLINEAR-ANTI-SATURATION + PRIOR-ART-AUDITED`.

Assume RH is false with finite zero edge

\[
\frac12<\Theta:=\sup_{\zeta(\rho)=0}\Re\rho<1.
\tag{1}
\]

`RE-112` uses the fixed off-critical zero-density estimate to obtain the scalar source envelope

\[
\Phi(x)-x=O_\Theta(x^\Theta)
\tag{2}
\]

and hence, for recovery from a positive CA state `C` at `Y=log C` to the first later nonpositive state `D` at `V=log D`,

\[
L:=V-Y\gg_\Theta h(C)Y^{2-\Theta}\log Y.
\tag{3}
\]

The scalar envelope still forgets the phase of the zeros that can contribute at exact order `x^Theta`. Retaining that phase gives a stricter selected-source law. Define

\[
\boxed{
F_\Theta(u)
:=
\sum_{\substack{\zeta(\rho)=0\\ \Re\rho=\Theta}}
\frac{e^{i\Im(\rho)u}}{\rho},
}
\tag{4}
\]

with multiplicity. The series converges absolutely and uniformly; conjugate zeros pair, so `F_Theta` is real-valued, bounded and uniformly continuous. Then

\[
\boxed{
 x-\vartheta(x)
 =x^\Theta\bigl(F_\Theta(\log x)+o(1)\bigr),
\qquad
 x-\Phi(x^-)
 =x^\Theta\bigl(F_\Theta(\log x)+o(1)\bigr).
}
\tag{5}
\]

For an adaptive `RE-034` witness `C=C_b`, fixed `1-Theta<b<1/2`, the exact selector locks the Robin height to the same edge phase:

\[
\boxed{
F_\Theta(\log Y)
=b\lambda_Y+o(1),
\qquad
\lambda_Y:=h(C)Y^{1-\Theta}\log Y.
}
\tag{6}
\]

In particular `lambda_Y=O(1)`. If its first recovery is genuinely sublinear, `L=o(Y)`, then (3) forces `lambda_Y=o(1)`, so (6) makes the edge phase vanish at the selector. Uniform continuity propagates that vanishing phase across every crossed event. The forward discrepancy from `RE-110` therefore improves from `O(Y^Theta)` to

\[
\boxed{M_+(C,D)=o(Y^\Theta),}
\tag{7}
\]

and the exact one-sided workload budget yields

\[
\boxed{
L
=
\omega\!\left(h(C)Y^{2-\Theta}\log Y\right)
=
\omega(\lambda_YY).
}
\tag{8}
\]

Thus **no genuinely sublinear adaptive recovery can saturate the scalar finite-edge minimum of `RE-112`**. Any unbounded family satisfying a fixed-constant near-minimal upper bound

\[
L\le K h(C)Y^{2-\Theta}\log Y,
\qquad L\le Y,
\tag{9}
\]

for one fixed `K`, is forced into the opposite regime:

\[
\boxed{
 h(C)\asymp\frac{Y^{\Theta-1}}{\log Y},
 \qquad
 L\asymp Y,
 \qquad
 F_\Theta(\log Y)\asymp1
}
\tag{10}
\]

with the favorable sign. If the supremum `Theta` is not attained by a zeta zero, then `F_Theta` is identically zero and such a fixed-constant near-minimal family is impossible.

## 1. Extreme-face representation of the finite-edge source

The primitive source data are the nontrivial zeros `rho=beta+i gamma`. Normalize the Chebyshev error by `x^Theta`; lower-strip zeros, explicit-formula truncation, prime-power corrections, and higher CA layers are nuisance terms. The representation kill test is whether the high-strip zero coefficients are summable strongly enough to project onto the extreme face `beta=Theta` without target-dependent choices.

Fix `sigma_0` with `1/2<sigma_0<Theta`. The Ingham-density argument already persisted in `RE-112` gives

\[
\boxed{
\sum_{\substack{\zeta(\rho)=0\\ \Re\rho\ge\sigma_0}}
\frac1{1+|\Im\rho|}<\infty.
}
\tag{11}
\]

Use the same half-jump truncated Riemann--von Mangoldt formula as `RE-112`, with `T asy x`:

\[
\psi_0(x)-x
=
-\sum_{|\Im\rho|\le T}\frac{x^\rho}{\rho}
+O((\log x)^2).
\tag{12}
\]

After multiplying by `-x^(-Theta)`, zeros below `sigma_0` contribute `O(x^(sigma_0-Theta)(log x)^2)=o(1)`. For `sigma_0<=beta<Theta`, each normalized term tends to zero and (11) gives a summable majorant independent of `x`, so dominated convergence makes their total `o(1)`. Zeros with `beta=Theta` give `F_Theta(log x)+o(1)` because the omitted edge tail is uniformly controlled by the tail of (11). Hence

\[
 x-\psi_0(x)
 =x^\Theta\bigl(F_\Theta(\log x)+o(1)\bigr).
\tag{13}
\]

The half-jump correction is `O(log x)` and

\[
\psi(x)-\vartheta(x)
=O\!\left(x^{1/2}(\log x)^2\right)
=o(x^\Theta).
\]

This proves the first formula in (5). `RE-112` gives

\[
\Phi_1(x)=\vartheta(x)+O(\log x),
\qquad
\Phi_{\ge2}(x)=O\!\left(x^{1/2}(\log x)^{3/2}\right),
\]

which proves the second formula in (5), and the same statement for `Phi(x)` itself. The `o(1)` is global: its remainder `r(x)` satisfies `sup_(x>=X)|r(x)|->0`. Absolute convergence is asserted only on the fixed high strip (11), not for the full classical zero sum.

This representation is target-independent and one-dimensional after normalization: at order `x^Theta`, all surviving information is the signed logarithmic phase field `F_Theta`.

## 2. The adaptive selector fixes the edge phase

For a regular adaptive-amplitude maximizer `C=C_b`, `RE-034` supplies an exact selector coordinate `Z>Y` with

\[
\Phi(Z)=Y,
\qquad
Z-Y=(b+o(1))h(C)Y\log Y,
\tag{14}
\]

and

\[
Z-\vartheta(Z)=(b+o(1))h(C)Z\log Z.
\tag{15}
\]

It also proves `h(C)=o(1/log Y)`, so `Z/Y->1` and `log Z-log Y->0`. Combining (5) with (15), then using uniform continuity of `F_Theta`, gives exactly (6). Since `F_Theta` is bounded,

\[
\boxed{
 h(C)\ll_{\Theta,b}\frac{Y^{\Theta-1}}{\log Y}.
}
\tag{16}
\]

The selector therefore does not sample an arbitrary point beneath the scalar `Y^Theta` envelope. Its actual Robin height calibrates the surviving right-edge zero phase at the same logarithmic scale.

## 3. Sublinear recovery forces phase anti-saturation

Let the crossed event groups have coordinates `eta_e` and physical left coordinates

\[
u_e:=\Phi(\eta_e^-).
\tag{17}
\]

`RE-110` defines

\[
M_+(C,D):=\max_e(\eta_e-u_e)_+
\tag{18}
\]

and proves the exact one-sided recovery budget

\[
L M_+(C,D)
\ge(1+o(1))h(C)Y^2\log Y.
\tag{19}
\]

Assume `L=o(Y)`. Equation (3) gives `lambda_Y=o(1)`, hence (6) gives `F_Theta(log Y)=o(1)`. For every crossed event with positive forward defect, `u_e in [Y,V]=Y+o(Y)`. Writing the left-limit form of (5) as

\[
\Phi(x^-)
=x-x^\Theta\bigl(F_\Theta(\log x)+r(x)\bigr),
\qquad
\sup_{x\ge X}|r(x)|\to0,
\tag{20}
\]

boundedness of `F_Theta` and `Theta<1` first force `eta_e asy Y` uniformly. Hence `log eta_e-log Y=o(1)` uniformly. Uniform continuity then gives `F_Theta(log eta_e)=o(1)` for all crossed events, and (20) yields

\[
\eta_e-u_e=o(Y^\Theta)
\]

uniformly. This proves (7); inserting it into (19) proves (8).

Now suppose a fixed-constant near-minimal family satisfies (9). If `lambda_Y` had a subsequence tending to zero, (9) would make that subsequence sublinear and contradict (8). Hence `liminf lambda_Y>0`; boundedness from (6) gives `lambda_Y asy 1`. Equations (3), (9), and (16) then imply (10).

If the edge is not attained, `F_Theta` is identically zero, so (6) gives `lambda_Y->0`; (9) would again contradict (8). Therefore

\[
\boxed{
\text{unbounded fixed-constant near-minimal adaptive recovery}
\Longrightarrow
\exists\rho:\Re\rho=\Theta.
}
\tag{21}
\]

## 4. Prior-art boundary and new source target

Explicit-formula spectral expansions and almost-periodic organization of prime-number-theorem errors are classical. Wintner's limiting-distribution work and the Akbary--Ng--Shahabi framework are conceptual prior-art boundaries for almost-periodic prime-counting errors. Their general limiting-distribution theory is not invoked as the uniform finite-edge expansion (5); that expansion is derived here from the specific high-strip reciprocal summability already established in `RE-112`. No novelty is claimed for the general principle that zero phases organize prime-counting errors.

The prior-art audit found no theorem imposing the selector-conditioned phase lock (6) or deriving the sublinear anti-saturation law (8) for colossally abundant Robin recovery. The line-specific contribution is the coupling of the extreme zero face to the exact adaptive selector and the one-sided CA workload budget.

The finite-edge frontier is therefore narrower than in `RE-112`. Sublinear recoveries cannot realize the scalar minimum. Fixed-constant near-minimal recoveries, if any, are forced into a **macroscopic edge-amplitude phase-lock regime**. The next useful source theorem should attack recurrence of

\[
F_\Theta(\log Y)\asymp1,
\qquad
h(C)\asymp\frac{Y^{\Theta-1}}{\log Y}
\]

on adaptive CA maxima, preferably coupled to the reciprocal-Mertens coordinate already locked to the same selector in `RE-034`. The separate `Theta=1` branch remains governed by the unconditional `RE-109`--`RE-111` workload problem.