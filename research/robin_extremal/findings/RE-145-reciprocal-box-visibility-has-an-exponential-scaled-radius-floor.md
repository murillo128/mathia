# RE-145 — reciprocal-box visibility has an exponential scaled-radius floor

**Status:** `EXACT-DERIVED + FINITE-ZERO-EDGE + ROBIN-PACKET + CARDINALITY-FREE + QUANTITATIVE-RECIPROCAL-BOX + EXPONENTIAL-RADIUS-FLOOR + SUBLOG-RADIUS-COROLLARY + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

`RE-135` proves that every finite Robin packet contained in a **fixed** reciprocal-scale box has a visibility floor independent of its cardinality. Its compactness argument is deliberately qualitative: if the scaled radius is `R`, it produces some positive constant `m(R,kappa)` but does not say how fast that constant may deteriorate as `R->infinity`. `RE-144` then shows that this missing rate is real rather than cosmetic: arbitrarily slowly diverging scaled radius is enough for a matched simple spectrum to make the packet `o(M_0)`.

The present finding quantifies the compactness mechanism. For the positive empirical-measure representation that underlies `RE-135`, the loss caused by allowing scaled radius `R` to grow is **at most exponential in `R`**, uniformly in packet cardinality and arrangement. Consequently a Robin packet in a box of scaled radius `R(U)=o(log U)` still has a `U^{-o(1)}` visibility floor relative to its natural `N_U M_0(U)` scale. This does not restore a fixed positive floor and therefore does not contradict `RE-144`; instead it prices exactly how quickly the fixed-box theorem can deteriorate before source-specific information enters.

Fix

\[
0<\kappa<\frac12,
\qquad
\frac12<\sigma_0<\Theta<1,
\qquad
\gamma_*>0,
\tag{1}
\]

and write

\[
I_\kappa=[1-\kappa,1],
\qquad
\mathcal K_R
=
\{\lambda\in\mathbb C:
|\Re\lambda|\le R,
\ |\Im\lambda|\le R\}.
\tag{2}
\]

The main quantitative statement is representation-level and contains no zeta-zero assumption.

> **Quantitative positive-measure visibility.** There are explicit constants `c_kappa,C_kappa>0` such that, for every `R>=0` and every Borel probability measure `mu` on `K_R`,
> \[
> F_\mu(z):=\int_{\mathcal K_R}e^{\lambda z}\,d\mu(\lambda)
> \tag{3}
> \]
> satisfies
> \[
> \boxed{
> \sup_{x\in I_\kappa}|F_\mu(x)|
> \ge
> c_\kappa e^{-C_\kappa R}.
> }
> \tag{4}
> \]
> One admissible choice is
> \[
> c_\kappa
> =\frac12\left(\frac{\kappa}{2e}\right)^{16},
> \qquad
> C_\kappa
> =16\log\frac{2e}{\kappa}.
> \tag{5}
> \]

The constants are intentionally crude. What is load-bearing is the **linear exponent in `R`** and the complete absence of the number of atoms.

## 1. Interpolation propagates `F_mu(0)=1` to the observation interval with only exponential radius loss

The positivity of `mu` gives the normalization

\[
F_\mu(0)=1.
\tag{6}
\]

For real `t in [0,1]`, differentiation under the integral gives

\[
F_\mu^{(m)}(t)
=
\int_{\mathcal K_R}
\lambda^m e^{\lambda t}\,d\mu(\lambda),
\tag{7}
\]

and therefore

\[
|F_\mu^{(m)}(t)|
\le
(\sqrt2 R)^m e^R.
\tag{8}
\]

Set

\[
N:=\left\lceil16(1+R)\right\rceil,
\qquad
n:=N-1,
\tag{9}
\]

and interpolate `F_mu` at the `n+1` equally spaced points

\[
x_j
=1-\kappa+\frac{j\kappa}{n},
\qquad 0\le j\le n.
\tag{10}
\]

The Lagrange basis evaluated at zero obeys

\[
|L_j(0)|
=
\prod_{m\ne j}
\frac{x_m}{|x_j-x_m|}
\le
\frac{(n/\kappa)^n}{j!(n-j)!}.
\tag{11}
\]

Hence

\[
\sum_{j=0}^{n}|L_j(0)|
\le
\left(\frac n\kappa\right)^n
\frac{2^n}{n!}
\le
\left(\frac{2e}{\kappa}\right)^n.
\tag{12}
\]

For the interpolation remainder at zero, the Hermite--Genocchi divided-difference formula applied on the convex hull `[0,1]` gives

\[
|\mathcal R_n(0)|
\le
\frac{\sup_{0\le t\le1}|F_\mu^{(N)}(t)|}{N!}
\prod_{j=0}^{n}x_j
\le
 e^R
\left(
\frac{e\sqrt2 R}{N}
\right)^N.
\tag{13}
\]

Since `N>=16(1+R)`,

\[
\frac{e\sqrt2 R}{N}
\le
\frac{e\sqrt2}{16}<\frac14,
\tag{14}
\]

so the right-hand side of (13) is in fact far below `1/2`; the coarse bound

\[
|\mathcal R_n(0)|\le\frac12
\tag{15}
\]

is enough. Combining (6), the interpolation identity and (12)--(15),

\[
1
\le
\sup_{x\in I_\kappa}|F_\mu(x)|
\left(\frac{2e}{\kappa}\right)^n
+\frac12.
\tag{16}
\]

Because `n<16(1+R)`, this yields

\[
\sup_{I_\kappa}|F_\mu|
\ge
\frac12
\left(\frac{\kappa}{2e}\right)^{16(1+R)},
\tag{17}
\]

which is exactly (4)--(5).

This is the quantitative replacement for the compactness/identity-theorem step in `RE-135`. No finite-dimensional approximation, zero separation or cardinality bound has entered: (17) holds for **every probability measure** on the square, including weak limits of packets with unbounded local multiplicity.

## 2. Growing reciprocal boxes remain compatible with the Robin coefficient law

Now return to the leading finite-edge packet. Let `C_U` be a finite nonempty positive-ordinate packet with distinguished `rho_0=beta_0+i gamma_0 in C_U`, where

\[
\sigma_0\le\beta_0<\Theta,
\qquad
\gamma_0\ge\gamma_*,
\tag{18}
\]

and suppose every `rho=beta+i gamma in C_U` lies in the growing reciprocal box

\[
|\beta-\beta_0|
\le\frac{R(U)}{U},
\qquad
|\gamma-\gamma_0|
\le\frac{R(U)}{U}.
\tag{19}
\]

Take fixed correction depth `K>=0` and use the same Robin coefficient notation as `RE-135`,

\[
a_{\rho,K}(u)
=
e^{-(\Theta-\beta)u}
\left[
\frac1{\rho(1-\rho)}
+
\sum_{k=1}^{K}
\frac{(-1)^k k!}{u^k(1-\rho)^{k+1}}
\right].
\tag{20}
\]

Put

\[
d_\rho=\frac1{\rho(1-\rho)},
\qquad
\lambda_{\rho,U}
=U\bigl((\beta-\beta_0)+i(\gamma-\gamma_0)\bigr).
\tag{21}
\]

For `R(U)=o(U)`, all packet ordinates remain uniformly away from zero for sufficiently large `U`. The logarithmic derivative of `d_rho` is uniformly bounded in the fixed horizontal strip and on `|gamma|>=gamma_*/2`; hence (19) gives the explicit growing-radius form of the coefficient comparison used in `RE-135`,

\[
\frac{d_\rho}{d_{\rho_0}}
=1+O\!\left(\frac{1+R(U)}{U}\right),
\tag{22}
\]

uniformly in `rho in C_U`. The finite correction bracket contributes an additional `O_K(U^{-1})`. Therefore, after setting `u=Ux`, factoring the target damping/carrier and dividing by `N_U:=#C_U`,

\[
\frac1{N_U}
\sum_{\rho\in C_U}
a_{\rho,K}(Ux)e^{i\gamma Ux}
=
e^{-(\Theta-\beta_0)Ux}
 d_{\rho_0}e^{i\gamma_0Ux}
\bigl(Q_U(x)+E_U(x)\bigr),
\tag{23}
\]

where

\[
Q_U(x)
=
\frac1{N_U}
\sum_{\rho\in C_U}e^{\lambda_{\rho,U}x}
\tag{24}
\]

is the Laplace transform of an empirical probability measure on `K_(R(U))`, while

\[
\boxed{
\|E_U\|_{L^\infty(I_\kappa)}
\ll
\frac{(1+R(U))e^{R(U)}}{U}.
}
\tag{25}
\]

The factor `e^R` in (25) is important when the radius grows; suppressing it inside an `O_R(.)` constant would make the quantitative extension circular.

By (17), if

\[
q_U
:=
\frac12
\left(\frac{\kappa}{2e}\right)^{16(1+R(U))},
\tag{26}
\]

then

\[
\sup_{x\in I_\kappa}|Q_U(x)|\ge q_U.
\tag{27}
\]

Also

\[
\|Q_U'\|_{L^\infty(I_\kappa)}
\le
\sqrt2 R(U)e^{R(U)}.
\tag{28}
\]

Thus the normalized complex packet cannot collapse faster than exponentially in its scaled reciprocal radius, regardless of how many atoms occupy the box.

## 3. A sublogarithmic radius still transfers to a real Robin visibility floor

The complex lower bound must survive the fast real carrier. Choose `x_0 in I_kappa` with

\[
|Q_U(x_0)|\ge q_U.
\tag{29}
\]

Let

\[
\delta_U
:=
\min\left\{
\frac\kappa4,
\frac{q_U}{8(1+\sqrt2 R(U)e^{R(U)})}
\right\}.
\tag{30}
\]

At least one one-sided interval of length `delta_U` issuing from `x_0` is contained in `I_kappa`. On that interval, (28) gives

\[
|Q_U(x)-Q_U(x_0)|\le\frac{q_U}{8}.
\tag{31}
\]

Write

\[
d_{\rho_0}=|d_{\rho_0}|e^{i\theta_0},
\qquad
\omega_U=\gamma_0U.
\tag{32}
\]

If

\[
R(U)=o(\log U),
\tag{33}
\]

then, because `q_U=e^{-O_kappa(R(U))}`,

\[
\omega_U\delta_U\longrightarrow\infty
\tag{34}
\]

and simultaneously

\[
\frac{(1+R(U))e^{R(U)}}{U}
=o(q_U).
\tag{35}
\]

Consequently the phase `omega_U x+theta_0` traverses a full turn while `Q_U` changes by at most `q_U/8`, and the perturbation `E_U` is eventually at most `q_U/8`. There is therefore some `x_U in I_kappa` for which

\[
\left|
\Re\left(
 e^{i(\omega_Ux_U+\theta_0)}
 (Q_U(x_U)+E_U(x_U))
\right)
\right|
\ge\frac{q_U}{2}.
\tag{36}
\]

Since `x_U<=1` and `Theta-beta_0>0`, the target damping at `x_U` is no smaller than its value at `x=1`. Using (23), (36), and the target version of the fixed-`K` coefficient expansion gives

\[
\boxed{
\sup_{(1-\kappa)U\le u\le U}
|\mathcal S_{C_U,K}(u)|
\ge
c_\kappa'
 e^{-C_\kappa'R(U)}
 N_U |a_{\rho_0,K}(U)|
}
\tag{37}
\]

for all sufficiently large `U`, with constants depending only on the fixed strip/window data and `K`, not on `N_U` or the packet arrangement.

In particular,

\[
R(U)=o(\log U)
\quad\Longrightarrow\quad
 e^{-C_\kappa'R(U)}=U^{-o(1)},
\tag{38}
\]

so

\[
\boxed{
\sup_I|\mathcal S_{C_U,K}|
\ge
U^{-o(1)}N_U|a_{\rho_0,K}(U)|.
}
\tag{39}
\]

The same proof actually permits a sufficiently small fixed multiple of `log U`: what is required is that the exponential radius loss in `q_U`, the derivative cost `e^R(1+R)`, and the coefficient perturbation all remain dominated by the carrier scale `U`. The sublogarithmic formulation is retained because it is invariant under the deliberately nonoptimized constants in (5).

## 4. `RE-144` is compatible and shows the exponential radius dependence is the correct order

`RE-144` constructs a matched one-sided current-stage packet from `j` elementary factors. Its local cardinality is

\[
N_j=2^j,
\tag{40}
\]

its scaled two-dimensional radius is

\[
R_j=O_\kappa(j),
\tag{41}
\]

and its unnormalized packet can be suppressed by

\[
\sup|\mathcal S_j|
\ll q_1^j M_{0,j}
\qquad(0<q_1<1).
\tag{42}
\]

After normalization by the natural `N_j M_(0,j)` scale,

\[
\frac{\sup|\mathcal S_j|}{N_jM_{0,j}}
\ll
\left(\frac{q_1}{2}\right)^j
=
 e^{-\Omega_\kappa(R_j)}.
\tag{43}
\]

Thus (17) has the right **functional order in scaled radius** within the matched class: a universal cardinality-free bound better than `e^{-O(R)}` cannot follow merely from positivity of the empirical mass and confinement to `K_R`. The constants in (5) are not claimed sharp, and (43) is not asserted to saturate them.

There is no contradiction with the decisive negative conclusion of `RE-144`. If `R_j->infinity` but `R_j=o(log U_j)`, then both statements allow

\[
\frac{\sup|\mathcal S_j|}{M_{0,j}}
\longrightarrow0
\tag{44}
\]

while the rate is only subpolynomial in `U_j`. `RE-144` rules out a **constant** visibility floor for every divergent scaled radius; `RE-145` proves that sublogarithmic escape cannot buy more than a subpolynomial loss from the positive local packet itself.

This distinction matters whenever the remaining error terms are polynomially smaller than the target scale, even though it does not by itself rule out the qualitative `o(M_0)` hiding required by the strongest contradiction setup.

## 5. Falsifiable test and adversarial audit

The exact representation-level test is (4). A counterexample would be a sequence `R_j` and probability measures `mu_j` supported on `K_(R_j)` for which

\[
\sup_{I_\kappa}|F_{\mu_j}|
<
\frac12
\left(\frac\kappa{2e}\right)^{16(1+R_j)}.
\tag{45}
\]

Such a sequence would contradict the explicit interpolation calculation (7)--(17), so the claim does not rest on numerical evidence or compactness intuition.

Several boundaries are load-bearing.

First, `mu` is a **positive probability measure**. Arbitrary signed or complex coefficients do not satisfy `F(0)=1` after normalization and can have exact high-order cancellation. The theorem is useful here precisely because the Robin coefficient ratios inside a reciprocal box converge uniformly to the common target coefficient, leaving positive empirical masses in the normalized leading representation.

Second, (37) is a packet theorem, not a theorem about the full Robin residual. Atoms outside the box may still cancel the visible local packet. The far-left and high-height decompositions of `RE-141`--`RE-144` remain separate obligations.

Third, fixed correction depth `K` is essential to the displayed uniform coefficient expansion. No statement is made for `K=K(U)->infinity` without a fresh remainder audit.

Fourth, no claim is made that actual zeta zeros satisfy `R(U)=o(log U)` around the relevant strong atom. `RE-144` already shows that current one-level zero-counting/density inputs do not force such a localization. Equation (37) prices a radius assumption; it does not manufacture one.

Finally, the interpolation constant is deliberately wasteful. Sharpening `16`, replacing the square by a smaller support geometry, or optimizing the carrier transfer may improve the coefficient of `R` in the exponent, but cannot change the exponential-in-`R` order without additional structure because of (43).

## 6. Prior-art and novelty boundary

The surrounding harmonic-analysis literature contains much stronger and much more general Remez/Turán--Nazarov propagation principles for exponential polynomials and analytic functions. Those results are the correct prior-art neighborhood, not something this finding claims to supersede. In their usual exponential-polynomial form, however, the quantitative loss is expressed through the number/effective degree of exponential terms or a related growth parameter.

The contribution here is the **Robin-specific positive-measure splice**: starting from the empirical-probability representation isolated in `RE-135`, the elementary interpolation argument turns `F_mu(0)=1` plus support radius `R` into an explicit cardinality-free `e^{-O_kappa(R)}` modulus, and then tracks the previously hidden `R`-dependence through the Robin coefficient perturbation and real-carrier step. No external theorem is load-bearing in this derivation, so `SOURCES.md` requires no new anchor.

A targeted literature audit, including current Remez/Turán--Nazarov work, did not change that boundary: the general propagation theory is prior art, while the exact normalized Robin packet consequence and its comparison with the `RE-144` matched control are the line-specific content.

## 7. Research effect

`RE-135` and `RE-144` should no longer be read as a binary fixed-radius/growing-radius dichotomy. The correct picture has a quantitative middle layer:

\[
\text{scaled radius }R
\quad\Longrightarrow\quad
\text{normalized local visibility at least }e^{-O_\kappa(R)}.
\tag{46}
\]

A bounded `R` gives the fixed positive floor of `RE-135`. Any `R->infinity` can still drive that floor to zero, as `RE-144` proves constructively. But `R=o(log U)` can only drive it to zero subpolynomially in the Robin phase.

The next source-specific question is therefore sharper than “is the reciprocal radius bounded?” One can ask whether actual-zero geometry or the exterior-tail decomposition supplies a **rate comparison**: either force `R(U)` below a logarithmic budget, or show that cancellation arriving from outside the controlled packet is polynomially smaller than the `e^{-O(R(U))}` local floor. If neither is available, the `RE-144` product mechanism remains a genuine obstruction to qualitative target visibility.