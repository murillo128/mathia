# RE-125 — invisible algebraic subedge atoms require a reciprocal-scale ordinate annulus

**Status:** `EXACT-DERIVED + FINITE-ZERO-EDGE + NONISOLATED-EDGE + SPECTRAL-LOCALIZATION + PHASE-SECTOR + ZERO-CLUSTERING-NECESSITY + CA-PHASE-TRANSFER + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

Assume the attained finite-edge branch and notation of `RE-121`--`RE-124`,

\[
\frac12<\Theta:=\sup_{\zeta(\rho)=0}\Re\rho<1,
\qquad
\frac12<\sigma_0<\Theta,
\]

and fix an expansion order `K>=0`. For a positive-ordinate subedge zero

\[
\rho=\beta+i\gamma,
\qquad
\sigma_0\le\beta<\Theta,
\qquad
\gamma>0,
\]

write

\[
a_{\rho,K}(u)
:=
 e^{-(\Theta-\beta)u}
\left[
\frac1{\rho(1-\rho)}
+
\sum_{k=1}^{K}
\frac{(-1)^k k!}{u^k(1-\rho)^{k+1}}
\right],
\tag{1}
\]

so that the signed subedge packet is

\[
\mathcal S_K(u)
=
2\Re
\sum_{\substack{\zeta(\rho)=0\\
\sigma_0\le\Re\rho<\Theta\\
\Im\rho>0}}
 a_{\rho,K}(u)e^{i\gamma u}.
\tag{2}
\]

`RE-124` showed that an algebraically strong atom can remain invisible only if comparable coefficient mass lies within ordinate distance `U^(-1+eta)` for every fixed `eta>0`. That localization still allowed exact multiplicity and arbitrarily tighter micro-clusters to count as possible cancellation. The actual zeta coefficients rule those out.

Define

\[
R_*:=
\max_{\sigma_0\le\beta\le\Theta}
\frac{2\beta-1}{2\sqrt{\beta(1-\beta)}},
\qquad
\omega_*:=\arctan R_*<\frac\pi2,
\tag{3}
\]

and fix, for example,

\[
c_*:=\frac14\left(\frac\pi2-\omega_*\right)>0.
\tag{4}
\]

Then for every fixed `A>0`, `0<eta<1`, and `K>=0`, there is a constant
`C=C(A,K,eta,sigma_0,Theta)` such that, for every sufficiently large `U`, every target zero `rho_0=beta_0+i gamma_0` satisfying

\[
|a_{\rho_0,K}(U)|\ge cU^{-A}
\tag{5}
\]

with fixed `c>0` obeys

\[
\boxed{
|a_{\rho_0,K}(U)|
\le
C\left[
\sup_{|u-U|\le U^{1-\eta/2}}|\mathcal S_K(u)|
+
\sum_{\substack{\rho\ne\rho_0\\
\sigma_0\le\Re\rho<\Theta,\ \Im\rho>0\\
c_*/U<|\Im\rho-\gamma_0|\le U^{-1+\eta}}}
|a_{\rho,K}(U)|
\right]
+o(U^{-A}).
}
\tag{6}
\]

Thus **the competing mass cannot live arbitrarily closer than reciprocal scale**. If the packet hides an individually algebraically strong atom, comparable coefficient mass must occur in the ordinate annulus

\[
\boxed{
\frac{c_*}{U}
<
|\gamma-\gamma_0|
\le
U^{-1+\eta}.
}
\tag{7}
\]

Exact multiplicity, equal ordinates, and `o(1/U)` micro-clusters reinforce rather than cancel the target. The remaining strong-atom escape therefore requires genuine reciprocal-scale phase rotation. The separate diffuse-cloud escape from `RE-124`, where no individual atom reaches the target algebraic scale, remains open.

When `A<K+1`, if the annular mass in (6) is `o(|a_{rho_0,K}(U)|)`, then `RE-123` transfers the surviving continuum excursion to actual regular CA states. Hence (7) is a necessary zero-geometry condition for hiding a strong algebraic anomaly on the CA staircase, not merely in the continuum model.

## 1. Positive-ordinate coefficients lie in a fixed open right-half-plane sector

The leading coefficient has a sign geometry that was not used in `RE-124`. For

\[
b_\rho:=\frac1{\rho(1-\rho)},
\]

we have

\[
\rho(1-\rho)
=
\gamma^2+\beta(1-\beta)
+i\gamma(1-2\beta).
\tag{8}
\]

Since `beta>1/2`, the denominator lies in the fourth quadrant and therefore `b_rho` lies in the first quadrant. More precisely,

\[
\tan\arg b_\rho
=
\frac{\gamma(2\beta-1)}
     {\gamma^2+\beta(1-\beta)}.
\tag{9}
\]

For fixed `beta`, the right-hand side is maximized at

\[
\gamma=\sqrt{\beta(1-\beta)},
\]

with value

\[
\frac{2\beta-1}{2\sqrt{\beta(1-\beta)}}.
\tag{10}
\]

Because `sigma_0<=beta<=Theta<1`, (3) is finite and gives the uniform sector bound

\[
0<\arg b_\rho\le\omega_*<\frac\pi2.
\tag{11}
\]

The fixed-order algebraic corrections do not destroy this sector. Dividing (1) by its leading term gives

\[
a_{\rho,K}(U)
=
e^{-(\Theta-\beta)U}b_\rho
\left(1+O_K(U^{-1})\right)
\tag{12}
\]

uniformly over the strip; indeed every ratio

\[
\frac{\rho}{(1-\rho)^k}
\]

is uniformly bounded there for fixed `k>=1`. Consequently, for all sufficiently large `U`, every positive-frequency coefficient `a_{rho,K}(U)` lies in a slightly enlarged fixed sector still strictly inside the open right half-plane.

This is a source-specific fact. An arbitrary complex exponential packet would not have it.

## 2. Sub-reciprocal neighbors reinforce after demodulation

Demodulate at the target ordinate `gamma_0`. A neighboring positive-frequency atom contributes at phase `U`

\[
a_{\rho,K}(U)e^{i(\gamma-\gamma_0)U}.
\tag{13}
\]

If

\[
|\gamma-\gamma_0|\le\frac{c_*}{U},
\tag{14}
\]

then its extra phase rotation lies in `[-c_*,c_*]`. By (4), (11), and (12), there is a fixed constant

\[
q_*=q_*(\sigma_0,\Theta)>0
\]

such that, for all sufficiently large `U`, every atom satisfying (14) obeys

\[
\boxed{
\Re\left(
 a_{\rho,K}(U)e^{i(\gamma-\gamma_0)U}
\right)
\ge
q_*|a_{\rho,K}(U)|.
}
\tag{15}
\]

Thus all atoms in the inner reciprocal ball point into the same open half-plane after target demodulation. They cannot cancel one another. Repeated copies from a multiple zero have `gamma=gamma_0` and therefore reinforce exactly in this projection.

The statement is deliberately one-sided. Once `|gamma-gamma_0|` reaches a sufficiently large constant multiple of `1/U`, the phase rotation can cross into the opposite half-plane and cancellation becomes possible.

## 3. The RE-124 matched filter removes everything outside the outer radius

Use the same band-limited extraction as `RE-124`, but choose the frequency cutoff so that

\[
0\le\widehat\phi\le1,
\qquad
\widehat\phi(\xi)=1\quad(|\xi|\le1/2),
\qquad
\widehat\phi(\xi)=0\quad(|\xi|\ge1).
\tag{16}
\]

Set

\[
L=U^{1-\eta},
\qquad
H=U^{1-\eta/2},
\qquad
\phi_L(t)=L^{-1}\phi(t/L),
\tag{17}
\]

and form the target-demodulated average

\[
I_{\rho_0}(U)
:=
\int_{1-U}^{\infty}
\phi_L(t)\mathcal S_K(U+t)
 e^{-i\gamma_0(U+t)}\,dt.
\tag{18}
\]

The horizontal split, amplitude derivative bounds, Taylor expansion, and physical-tail estimate of `RE-124` apply unchanged. In particular, to arbitrary fixed algebraic accuracy, only positive-frequency atoms satisfying

\[
|\gamma-\gamma_0|\le L^{-1}=U^{-1+\eta}
\tag{19}
\]

survive. The negative-frequency conjugate packet is separated from the target by `gamma+gamma_0` and is killed by the same frequency support for large `U`.

There is one extra gain inside the inner ball (14). Since

\[
L|\gamma-\gamma_0|
\le
c_*U^{-\eta}<\frac12
\tag{20}
\]

for large `U`, the cutoff is identically one there. All positive derivatives of `hat phi` vanish on that plateau, so after Taylor-freezing the slowly varying amplitude, each inner atom contributes exactly its frozen quantity (13), up to the common `o(U^-A)` remainder. By (15), the real part of the entire inner contribution is bounded below by `q_*` times its absolute coefficient mass.

Atoms in the transition shell

\[
\frac{c_*}{U}<|\gamma-\gamma_0|\le U^{-1+\eta}
\tag{21}
\]

need not have a favorable phase. The same derivative estimates as `RE-124` bound their total filtered contribution by a constant times

\[
\sum_{\rho\text{ in }(21)}|a_{\rho,K}(U)|.
\tag{22}
\]

Finally,

\[
|I_{\rho_0}(U)|
\le
\|\phi\|_1
\sup_{|u-U|\le H}|\mathcal S_K(u)|
+o(U^{-A}).
\tag{23}
\]

Taking real parts, retaining the target inside the positive inner contribution, and moving the shell contribution to the other side gives (6).

## 4. The reciprocal lower radius is order-sharp for this mechanism

The phase-sector argument cannot exclude competitors at every constant multiple of `1/U`. A two-mode frozen-coefficient control already shows why. Take two equal positive-frequency coefficients with ordinates `gamma_0` and

\[
\gamma_1=\gamma_0+\frac\pi U.
\]

At `u=U+t`, their sum is

\[
e^{i\gamma_0(U+t)}
+
e^{i\gamma_1(U+t)}
=
e^{i\gamma_0(U+t)}
\left(1-e^{i\pi t/U}\right).
\tag{24}
\]

Hence throughout the `RE-124` observation window `|t|<=H=U^(1-eta/2)`,

\[
\left|1-e^{i\pi t/U}\right|
\ll
U^{-\eta/2}.
\tag{25}
\]

So a competitor separated by a constant times `1/U` can suppress a target by a power on precisely the long window used for spectral localization. This control is not asserted to be an actual zeta-zero configuration; it is a kill test against overstrengthening (6). The theorem isolates the **order** `1/U`, not a universal sharp numerical constant.

## 5. Transfer to the CA staircase

Suppose the target satisfies (5) along an unbounded sequence `U_j`, the annular mass in (6) is

\[
o(|a_{\rho_0,K}(U_j)|),
\tag{26}
\]

and `A<K+1`. Equation (6) gives phases `u_j` with

\[
|u_j-U_j|\le U_j^{1-\eta/2},
\qquad
|\mathcal S_K(u_j)|\gg U_j^{-A}.
\tag{27}
\]

The superalgebraically fine regular-CA phase mesh of `RE-123` then supplies regular CA states `C_j` for which

\[
\mathcal S_K(\log\log C_j)
=
\mathcal S_K(u_j)+o(U_j^{-A}).
\tag{28}
\]

Combining this with the order-`K` edge expansion gives an actual CA residual excursion

\[
|R_K(\log\log C_j)|\gg U_j^{-A}.
\tag{29}
\]

Therefore exact multiplicity or a cluster narrower than reciprocal scale cannot be the hidden selector that prevents a strong finite-edge atom from appearing on the CA staircase.

## 6. Representation and adversarial audit

The source data are unchanged from `RE-121`--`RE-124`: the same subedge zeta zeros and the same absolutely convergent signed packet. The new ingredient is only the argument geometry of the coefficient already present in that representation. The half-plane projection and matched filter are linear readouts; no independent arithmetic coordinate is introduced.

The main adversarial checks are as follows.

First, the sector is uniform without any zero-height assumption. Formula (10) maximizes over every `gamma>0`, and compactness of `beta in [sigma_0,Theta]` with `Theta<1` leaves a fixed angular margin from `pi/2`.

Second, the `1/U` corrections in (1) perturb the coefficient argument by only `O_K(1/U)` uniformly. They cannot close that fixed angular margin for large `U`.

Third, multiplicity is not mistaken for cancellation. Equal-ordinate copies have exactly the same demodulated phase and lie in the positive half-plane contribution (15).

Fourth, the proof does not differentiate the full packet. As in `RE-124`, high-frequency oscillation remains exact and only the slowly varying amplitude is Taylor-expanded, preserving reciprocal-square summability.

Fifth, the conjugate negative-frequency packet cannot contaminate the target extraction: after demodulation its frequency is `-(gamma+gamma_0)`, bounded away from zero, so compact Fourier support removes it for large `U`.

Sixth, the synthetic pair (24) shows that the conclusion should not be strengthened to exclude all `O(1/U)` competitors. The reciprocal scale is a real phase-resolution boundary for this method.

A separate adversarial review of the coefficient sector, correction terms, filter plateau, multiplicity, conjugate packet, shell bound, and CA transfer found no material objection, so no `.review.md` sidecar is opened.

## 7. Prior-art boundary

The nearest external literature located in the audit concerns zero detection that is sensitive to vertical isolation, notably Maynard--Pratt's *Half-Isolated Zeros and Zero-Density Estimates*, together with the broader classical literature on zero spacing and frequency-localized explicit-formula arguments. Those works prevent any broad novelty claim for using vertical zero geometry or harmonic localization themselves.

`RE-125` makes only the narrower line-specific claim obtained by splicing the Robin/CA coefficient from (1) with the `RE-124` matched filter: positive-ordinate finite-edge coefficients occupy a fixed open half-plane sector, so sub-reciprocal neighbors reinforce and any strong hidden atom needs comparable mass in the reciprocal annulus (7). A targeted prior-art search found no theorem asserting this phase-sector annulus necessity for the finite-edge Robin/CA residual.

No new external theorem is load-bearing in the proof. The sector calculation is elementary, and the only analytic localization used is already canonical in `RE-124`; therefore `SOURCES.md` does not require a new dependency.

## 8. Consequence for the finite-edge frontier

`RE-124` reduced strong-atom invisibility to near-reciprocal clustering but left the whole inner cluster as a possible cancellation reservoir. `RE-125` removes its sub-reciprocal core. **A strong atom can be hidden only by coefficient mass that has accumulated enough relative phase to rotate against it**, which requires ordinate displacement at least a fixed constant times `1/U`, while `RE-124` still supplies the upper radius `U^(-1+eta)`.

The strong-atom branch is therefore no longer generic "zero clustering." It is a reciprocal-scale annular crowding problem. One must control whether polynomial-height near-edge zeros can place comparable weight in

\[
c_*/U<|\gamma-\gamma_0|\le U^{-1+\eta}
\]

with phases capable of cancellation. The separate diffuse branch, in which every atom is individually below the target algebraic scale but many modes combine collectively, remains untouched and is now the other sharply defined obstruction.