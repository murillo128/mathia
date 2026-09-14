# RE-113 — edge-zero phase locking rules out sublinear minimal Robin recovery

**Status:** `LITERATURE+DERIVED + FINITE-ZERO-EDGE + EXTREME-FACE-SPECTRAL-PROJECTION + EDGE-ZERO-PHASE + ADAPTIVE-SELECTOR-COUPLING + INTER-BLOCK-RECOVERY + SUBLINEAR-ANTI-SATURATION + PRIOR-ART-AUDITED`.

`RE-112` compresses all finite-edge source information into the scalar envelope

\[
\Phi(x)-x=O_\Theta(x^\Theta),
\qquad
\frac12<\Theta:=\sup_{\zeta(\rho)=0}\Re\rho<1,
\]

and shows that recovery from an adaptive positive Robin state cannot occur faster than

\[
L:=V-Y\gg_\Theta h(C)Y^{2-\Theta}\log Y.
\]

If a short recovery is within a constant factor of that scale, `RE-112` extracts a positive-mass packet of first-layer primes saturating the favorable `Y^Theta` Chebyshev envelope. The scalar envelope still forgets the phase of the zeros that can actually contribute at order `x^Theta`.

Retaining that phase changes the frontier. The fixed off-critical zero-density estimate already used in `RE-112` makes the reciprocal coefficients on every fixed strip `Re rho>=sigma_0>1/2` absolutely summable. After normalizing the explicit formula by `x^Theta`, every zero with `Re rho<Theta` dies by dominated convergence. What remains is the uniformly convergent edge profile

\[
\boxed{
F_\Theta(u)
:=
\sum_{\substack{\zeta(\rho)=0\\ \Re\rho=\Theta}}
\frac{e^{i\Im(\rho)u}}{\rho},
}
\]

with zeros counted with multiplicity. It controls both the ordinary Chebyshev error and the full CA event sweep:

\[
\boxed{
 x-\vartheta(x)
 =x^\Theta\bigl(F_\Theta(\log x)+o(1)\bigr),
\qquad
 x-\Phi(x)
 =x^\Theta\bigl(F_\Theta(\log x)+o(1)\bigr).
}
\]

For an adaptive `RE-034` witness `C=C_b`, `Y=log C`, the exact selector itself fixes the edge phase:

\[
\boxed{
F_\Theta(\log Y)
=
 b\,h(C)Y^{1-\Theta}\log Y+o(1).
}
\]

Consequently, if the first recovery is genuinely sublinear, `L=o(Y)`, every crossed event sees asymptotically the same edge phase. The `RE-110` forward workload therefore satisfies

\[
\boxed{M_+(C,D)=o(Y^\Theta)}
\]

whenever the scalar `RE-112` minimum itself is sublinear, and hence

\[
\boxed{
L
=
\omega\!\left(h(C)Y^{2-\Theta}\log Y\right).
}
\]

Thus **a sublinear adaptive recovery cannot saturate the finite-edge lower scale of `RE-112`**. Any fixed-constant near-minimal family under the standing short-recovery hypothesis `L<=Y` is forced into the opposite regime:

\[
\boxed{
 h(C)\asymp
 \frac{Y^{\Theta-1}}{\log Y},
 \qquad
 L\asymp Y,
 \qquad
 F_\Theta(\log Y)\asymp 1.
}
\]

If the zero edge is not attained, then `F_Theta` is identically zero and such a near-minimal family is impossible altogether. The finite-edge problem has therefore sharpened from a generic `Y^Theta` saturation packet to an **edge-attainment and phase-locking condition at the adaptive selector itself**.

## 1. Representation gate: project the source onto the extreme zero face

The primitive source data are the nontrivial zeros `rho=beta+i gamma` of `zeta`. The target observable is the signed forward discrepancy of the full CA event staircase on a recovery interval. The nuisance terms are: zeros in a fixed lower strip, the truncation remainder in the explicit formula, prime-power corrections between `psi` and `vartheta`, and higher CA layers between `vartheta` and `Phi`.

The correct normalization is `x^(-Theta)`. Under this normalization the source has a canonical extreme-face projection: zeros with `beta<Theta` should disappear, while zeros with `beta=Theta` retain only their logarithmic phases `e^(i gamma log x)`. This representation is target-independent: it is defined solely from the zeta zero set and the scalar edge `Theta`, before any Robin recovery is inspected.

The decisive kill test is whether the high-strip coefficients are summable strongly enough to justify passing from the truncated explicit formula to that extreme face. `RE-112` supplies exactly this. Fix `sigma_0` with

\[
\frac12<\sigma_0<\Theta.
\]

Its Ingham-density argument proves

\[
\boxed{
\sum_{\substack{\zeta(\rho)=0\\ \Re\rho\ge\sigma_0}}
\frac1{1+|\Im\rho|}<\infty.
}
\tag{1}
\]

Hence the edge series defining `F_Theta` converges absolutely and uniformly on `R`. In particular `F_Theta` is bounded and uniformly continuous; as a uniform limit of trigonometric polynomials it is a Bohr almost-periodic function. No exterior or higher-dimensional representation is introduced: after the scalar edge normalization, the only order-`x^Theta` information is this one signed phase field.

## 2. The normalized Chebyshev and CA-event errors converge to the edge profile

Use the same half-jump truncated Riemann--von Mangoldt formula as `RE-112`, with `T asy x`:

\[
\psi_0(x)-x
=
-\sum_{|\Im\rho|\le T}\frac{x^\rho}{\rho}
+O((\log x)^2).
\tag{2}
\]

After multiplying by `-x^(-Theta)`, split the zero sum at `sigma_0`. The lower part contributes

\[
O\!\left(x^{\sigma_0-\Theta}(\log x)^2\right)=o(1).
\tag{3}
\]

For zeros with `sigma_0<=Re rho<Theta`, each normalized term

\[
\frac{x^{\rho-\Theta}}{\rho}
\]

tends to zero. Equation (1) dominates the entire high-strip family by a summable sequence independent of `x`, so dominated convergence gives

\[
\sum_{\substack{|\Im\rho|\le x\\
\sigma_0\le\Re\rho<\Theta}}
\frac{x^{\rho-\Theta}}{\rho}
=o(1).
\tag{4}
\]

The zeros on the edge contribute

\[
\sum_{\substack{|\Im\rho|\le x\\\Re\rho=\Theta}}
\frac{e^{i\Im(\rho)\log x}}{\rho}
=
F_\Theta(\log x)+o(1),
\tag{5}
\]

because the omitted edge tail is uniformly bounded by the tail of the absolutely convergent series (1). Thus

\[
\boxed{
 x-\psi_0(x)
 =x^\Theta\bigl(F_\Theta(\log x)+o(1)\bigr).
}
\tag{6}
\]

The jump between `psi` and `psi_0` is `O(log x)`, and

\[
\psi(x)-\vartheta(x)
=O\!\left(x^{1/2}(\log x)^2\right)
=o(x^\Theta).
\]

Therefore

\[
\boxed{
 x-\vartheta(x)
 =x^\Theta\bigl(F_\Theta(\log x)+o(1)\bigr).
}
\tag{7}
\]

Finally `RE-112` gives

\[
\Phi_1(x)=\vartheta(x)+O(\log x),
\qquad
\Phi_{\ge2}(x)=O\!\left(x^{1/2}(\log x)^{3/2}\right),
\]

so the same profile controls the complete CA staircase, including left limits:

\[
\boxed{
 x-\Phi(x)
 =x^\Theta\bigl(F_\Theta(\log x)+o(1)\bigr),
\qquad
 x-\Phi(x^-)
 =x^\Theta\bigl(F_\Theta(\log x)+o(1)\bigr).
}
\tag{8}
\]

The `o(1)` in (6)--(8) is a genuine global asymptotic, hence is uniform after imposing a sufficiently large lower cutoff. No claim of absolute convergence is made for the full classical zero sum; absolute summability is used only on the fixed high strip where (1) applies.

## 3. The adaptive selector locks Robin height to the edge phase

Let `C=C_b` be a regular adaptive-amplitude maximizer from `RE-034`, for fixed

\[
1-\Theta<b<\frac12.
\tag{9}
\]

Write

\[
Y=\log C,
\qquad
h=h(C)>0,
\]

and let `Z>Y` be its exact selector coordinate. `RE-034` proves

\[
\Phi(Z)=Y,
\qquad
Z-Y=(b+o(1))hY\log Y,
\tag{10}
\]

and, more specifically,

\[
Z-\vartheta(Z)
=(b+o(1))hZ\log Z.
\tag{11}
\]

It also proves `h=o(1/log Y)`, so `Z/Y->1` and `log Z-log Y->0`. Combining (7) with (11) gives

\[
F_\Theta(\log Z)
=(b+o(1))hZ^{1-\Theta}\log Z+o(1).
\tag{12}
\]

Uniform continuity of `F_Theta` and `Z/Y->1` therefore yield the selector phase lock

\[
\boxed{
F_\Theta(\log Y)
=b\lambda_Y+o(1),
\qquad
\lambda_Y:=hY^{1-\Theta}\log Y.
}
\tag{13}
\]

Since `F_Theta` is bounded, every adaptive finite-edge witness automatically satisfies

\[
\boxed{
\lambda_Y=O_{\Theta,b}(1),
\qquad
h(C)\ll_{\Theta,b}\frac{Y^{\Theta-1}}{\log Y}.
}
\tag{14}
\]

This is the exact source-phase counterpart of the scalar envelope used in `RE-112`. The selector does not sample an arbitrary point of the `Y^Theta` envelope: its Robin height fixes the value of the surviving edge mode at the same logarithmic phase.

## 4. Sublinear recovery cannot saturate the scalar finite-edge minimum

Let `D` be the first later CA state with `h(D)<=0`, put

\[
V=\log D,
\qquad
L=V-Y,
\]

and use the forward workload defect of `RE-110`,

\[
M_+(C,D)
=
\max_e(\eta_e-u_e)_+,
\qquad
u_e:=\Phi(\eta_e^-).
\tag{15}
\]

Assume first that

\[
L=o(Y).
\tag{16}
\]

The scalar `RE-112` envelope and the exact recovery budget imply

\[
L\gg_\Theta hY^{2-\Theta}\log Y
=\lambda_Y Y.
\tag{17}
\]

Hence (16) forces

\[
\lambda_Y=o(1).
\tag{18}
\]

By the selector phase lock (13),

\[
F_\Theta(\log Y)=o(1).
\tag{19}
\]

For every crossed event with positive forward defect, `u_e in [Y,V]=Y+o(Y)`. Equation (8) first gives `eta_e asy Y`; hence

\[
\log\eta_e-\log Y=o(1).
\]

Uniform continuity of `F_Theta`, together with (19), gives

\[
F_\Theta(\log\eta_e)=o(1)
\]

uniformly over all crossed events. Applying (8) at the event left limit now yields

\[
\eta_e-u_e
=
\eta_e^\Theta\bigl(F_\Theta(\log\eta_e)+o(1)\bigr)
=o(Y^\Theta)
\]

uniformly, and therefore

\[
\boxed{
M_+(C,D)=o(Y^\Theta).
}
\tag{20}
\]

The exact one-sided budget from `RE-110` is

\[
L M_+(C,D)
\ge
(1+o(1))hY^2\log Y.
\tag{21}
\]

Combining (20)--(21),

\[
\boxed{
L
=
\omega\!\left(hY^{2-\Theta}\log Y\right)
=
\omega(\lambda_Y Y).
}
\tag{22}
\]

This is strictly stronger than the scalar `RE-112` corridor on every genuinely sublinear recovery. The improvement is qualitative rather than a new fixed power: the missing factor is exactly the inverse smallness of the edge phase selected by the Robin state.

## 5. Near-minimal finite-edge recovery must be macroscopic and edge-amplitude

Consider an unbounded family of adaptive witnesses whose first recoveries satisfy the standing short condition

\[
L\le Y
\tag{23}
\]

and a fixed-constant near-minimal upper bound

\[
L
\le
K\,hY^{2-\Theta}\log Y
=K\lambda_Y Y
\tag{24}
\]

for one fixed `K`. If `lambda_Y` had a subsequence tending to zero, (24) would make that recovery sublinear, contradicting (22). Hence

\[
\liminf\lambda_Y>0.
\tag{25}
\]

Together with the upper bound (14),

\[
\boxed{
\lambda_Y\asymp_{\Theta,b,K}1,
\qquad
h(C)\asymp_{\Theta,b,K}\frac{Y^{\Theta-1}}{\log Y}.
}
\tag{26}
\]

The lower corridor (17), (23), and (26) then give

\[
\boxed{L\asymp_{\Theta,b,K}Y.}
\tag{27}
\]

Finally the phase lock (13) shows

\[
\boxed{F_\Theta(\log Y)\asymp_{\Theta,b,K}1}
\tag{28}
\]

with the recovery-favorable positive sign.

Thus the `RE-112` near-minimal first-layer packet cannot live on a small-amplitude sublinear recovery. If it occurs infinitely often at all, the selected Robin peaks themselves must be of the full finite-edge spectral size and the recovery must consume a macroscopic fraction of the logarithmic scale.

There is an immediate edge-attainment corollary. If no zeta zero satisfies `Re rho=Theta`, then

\[
F_\Theta\equiv0.
\]

Equation (13) gives `lambda_Y->0` on every adaptive family, so (24) would force `L=o(Y)` and contradict (22). Therefore

\[
\boxed{
\text{an unbounded fixed-constant near-minimal adaptive recovery family}
\Longrightarrow
\exists\rho:\ \Re\rho=\Theta.
}
\tag{29}
\]

This is stronger than merely asking for a `Y^Theta` Chebyshev saturation packet: the rightmost zero line must exist, its almost-periodic phase must be positive at the selected logarithmic scale, and the Robin peak must already have edge-sized height.

## 6. Prior-art boundary and the new source target

The explicit-formula spectral expansion and almost-periodic organization of normalized prime-number-theorem errors are classical themes. Wintner's limiting-distribution work and the modern Akbary--Ng--Shahabi framework treat almost-periodic prime-counting error terms. No novelty is claimed for representing an explicit-formula error by zero phases, nor for the general theory of almost-periodic functions. The edge profile here is obtained directly from the same truncated explicit formula and Ingham zero-density input already used in `RE-112`; the new line-specific content is the coupling of that extreme-face profile to the exact adaptive Robin selector and the one-sided CA recovery budget.

A prior-art audit did not find a theorem imposing this selector-conditioned phase lock or deriving the sublinear anti-saturation consequence for colossally abundant Robin recovery. Akbary--Ng--Shahabi concerns limiting distributions of classical prime-number-theory errors rather than CA-selected inter-block recoveries; recent work on Chebyshev-prime phase statistics likewise does not impose the adaptive Robin selector.

The finite-edge frontier therefore splits more sharply than in `RE-112`. A scalar `Y^Theta` envelope is no longer enough to model a fast selected recovery. Sublinear recoveries must pay an unbounded factor beyond the scalar lower scale. Near-minimal recoveries, if they exist, are forced into a **macroscopic edge-amplitude phase-lock regime**. The next useful source theorem should attack recurrence of the joint condition

\[
F_\Theta(\log Y)\asymp1,
\qquad
h(C)\asymp \frac{Y^{\Theta-1}}{\log Y}
\]

on adaptive CA maxima, or couple this edge phase to the reciprocal-Mertens coordinate already locked to the same selector in `RE-034`. The separate `Theta=1` branch remains governed by the unconditional `RE-109`--`RE-111` workload problem.