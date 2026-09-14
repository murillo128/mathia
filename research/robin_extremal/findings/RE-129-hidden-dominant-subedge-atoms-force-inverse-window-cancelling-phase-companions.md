# RE-129 — hidden dominant subedge atoms force inverse-window cancelling-phase companions

**Status:** `EXACT-DERIVED + FINITE-ZERO-EDGE + NONISOLATED-EDGE + DOMINANT-ATOM-REDUCTION + GEVREY-LOCALIZATION + PHASE-SECTOR + CANCELLING-PHASE-LOCALIZATION + LOCAL-ZERO-COUNT + CA-PHASE-TRANSFER + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

Assume the attained finite-edge branch and notation of `RE-121`--`RE-128`,

\[
\frac12<\Theta:=\sup_{\zeta(\rho)=0}\Re\rho<1,
\qquad
\frac12<\sigma_0<\Theta,
\]

and fix `K>=0`. For a positive-ordinate subedge zero

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
:=e^{-(\Theta-\beta)u}
\left[
\frac1{\rho(1-\rho)}
+
\sum_{k=1}^{K}\frac{(-1)^k k!}{u^k(1-\rho)^{k+1}}
\right]
\tag{1}
\]

and

\[
\mathcal S_K(u)
=
2\Re\sum_{\substack{\zeta(\rho)=0\\
\sigma_0\le\Re\rho<\Theta\\
\Im\rho>0}}
a_{\rho,K}(u)e^{i\gamma u}.
\tag{2}
\]

Define the dominant coefficient at the central phase `U` by

\[
M_K(U):=
\max_{\substack{\zeta(\rho)=0\\
\sigma_0\le\Re\rho<\Theta\\
\Im\rho>0}}
|a_{\rho,K}(U)|.
\tag{3}
\]

The maximum exists for large `U`: uniformly on the fixed strip,

\[
|a_{\rho,K}(U)|
\ll_K \frac{e^{-(\Theta-\beta)U}}{1+\gamma^2},
\tag{4}
\]

so the coefficients tend to zero as `|gamma|->infinity`, while zeta zeros are discrete with finite multiplicity.

Fix `A>0`, `0<theta<1`, and `varepsilon>0`, put

\[
H:=U^{1-\theta},
\qquad
s:=1+\varepsilon,
\tag{5}
\]

and suppose

\[
M_K(U)\ge cU^{-A}
\tag{6}
\]

for fixed `c>0`. Choose a zero

\[
\rho_0=\beta_0+i\gamma_0
\tag{7}
\]

attaining (3). Let `c_*>0` be the reinforcing inner-radius constant from `RE-125`.

Then there are constants `epsilon_*>0`, `c_1>0`, `C_1>0`, and `U_0`, depending only on the fixed parameters, such that if `U>=U_0` and

\[
\sup_{|u-U|\le H}|\mathcal S_K(u)|
\le
\epsilon_* M_K(U),
\tag{8}
\]

there exists a distinct-ordinate zero

\[
\rho_1=\beta_1+i\gamma_1
\tag{9}
\]

with

\[
\boxed{
\frac{c_*}{U}
<|\gamma_1-\gamma_0|
\le
C_1\frac{(\log U)^{1+\varepsilon}}{H}
=C_1U^{-1+\theta}(\log U)^{1+\varepsilon}
}
\tag{10}
\]

and with a genuinely cancelling target-demodulated center projection,

\[
\boxed{
-\Re\!\left(
 a_{\rho_1,K}(U)e^{i(\gamma_1-\gamma_0)U}
\right)
\ge
c_1\frac{M_K(U)}{\log U}.
}
\tag{11}
\]

In particular,

\[
\boxed{
 c_1\frac{M_K(U)}{\log U}
\le
|a_{\rho_1,K}(U)|
\le
M_K(U).
}
\tag{12}
\]

The upper bound in (12), which is absent for a prescribed nonmaximal target, gives a quantitative phase margin. If

\[
\vartheta_1(U):=\arg a_{\rho_1,K}(U),
\]

then

\[
\boxed{
\cos\!\left((\gamma_1-\gamma_0)U+\vartheta_1(U)\right)
\le
-\frac{c_1}{\log U}.
}
\tag{13}
\]

Thus the companion is not merely strong and close: at the central phase it lies at least `asymp 1/log U` inside the cancelling half-plane.

The result applies to the strong-atom branch without assuming in advance that the chosen atom is dominant. If some zero `tilde rho` satisfies

\[
|a_{\widetilde\rho,K}(U)|\ge cU^{-A}
\]

and

\[
\sup_{|u-U|\le H}|\mathcal S_K(u)|
\le
\epsilon_*|a_{\widetilde\rho,K}(U)|,
\]

then (6) and (8) hold automatically because `M_K(U)>=|a_(tilde rho,K)(U)|`. Hence every hidden algebraically strong packet has a dominant atom for which the **spacing conclusion of `RE-128` and the signed phase conclusion of `RE-127` hold simultaneously at the inverse-window scale**.

As before,

\[
\Theta-\beta_j
\le
\frac{A\log U+O(\log\log U)}{U},
\qquad
\gamma_j\ll_A U^{A/2}
\qquad(j=0,1),
\tag{14}
\]

and along an unbounded hidden-atom sequence whose ordinates tend to infinity,

\[
|\gamma_1-\gamma_0|\log(2+\gamma_0)\to0.
\tag{15}
\]

When `A<K+1`, absence of such a dominant cancelling pair forces an algebraic continuum excursion, which `RE-123` transfers to actual regular CA states. The diffuse-cloud branch, where no individual coefficient is algebraically strong, remains separate.

## 1. Dominant-atom reduction

The coefficient asymptotic from `RE-124`--`RE-125` is

\[
a_{\rho,K}(U)
=
\frac{e^{-(\Theta-\beta)U}}{\rho(1-\rho)}
\left(1+O_K(U^{-1})\right),
\tag{16}
\]

uniformly on the fixed strip. Equation (6) therefore implies

\[
\gamma_0\ll_A U^{A/2}
\tag{17}
\]

and

\[
\Theta-\beta_0
\le
\frac{A\log U+O(1)}{U}.
\tag{18}
\]

The crucial extra fact supplied by the choice (3) is simply

\[
|a_{\rho,K}(U)|\le M_K(U)
\tag{19}
\]

for every positive-frequency atom. No new source hypothesis has been introduced; we have only selected a canonical atom already present in the packet.

This elementary selection is enough to remove the obstruction left explicitly open in `RE-128`. There, positive Taylor terms of the Gevrey filter were small relative to each annular coefficient, but an annular coefficient could be arbitrarily larger than the prescribed target. For the dominant target (19), that amplification is impossible.

## 2. Gevrey localization with aggregate Taylor error measured against the target

Use exactly the order-`s` Gevrey cutoff of `RE-128`, with

\[
0\le\widehat\phi\le1,
\qquad
\widehat\phi(\xi)=1\quad(|\xi|\le1/2),
\qquad
\widehat\phi(\xi)=0\quad(|\xi|\ge1),
\tag{20}
\]

and inverse-Fourier decay

\[
|\phi(t)|\le C_s e^{-c_s|t|^{1/s}}.
\tag{21}
\]

For a sufficiently large fixed `B`, set

\[
L:=\frac{H}{B(\log U)^s},
\qquad
\phi_L(t):=L^{-1}\phi(t/L).
\tag{22}
\]

The exact surviving frequency radius is

\[
L^{-1}=B\frac{(\log U)^s}{H}.
\tag{23}
\]

Form the target-demodulated average

\[
I_{\rho_0}(U)
:=
\int_{1-U}^{\infty}
\phi_L(t)\mathcal S_K(U+t)e^{-i\gamma_0(U+t)}\,dt.
\tag{24}
\]

The horizontal split, Gevrey time-tail bound, negative-frequency separation, and fixed-order Taylor remainder from `RE-128` contribute `o(U^-A)=o(M_K(U))`. For a surviving positive-frequency mode, the zeroth Taylor term is

\[
w_\rho(U)
 a_{\rho,K}(U)e^{i(\gamma-\gamma_0)U},
\qquad
w_\rho(U):=
\widehat\phi\!\left(L(\gamma-\gamma_0)\right)
\in[0,1].
\tag{25}
\]

The positive-order Taylor terms are bounded, relative to the frozen coefficient of that mode, by a convergent series whose first scale is

\[
\lambda_U
:=L\frac{\log U}{U}
=
\frac{U^{-\theta}}{B(\log U)^{\varepsilon}}.
\tag{26}
\]

By (17), the target lies at polynomial height. Since (23) is `o(1)`, the Riemann--von Mangoldt local count used in `RE-126`--`RE-128` gives

\[
\#\left\{\rho:
|\gamma-\gamma_0|\le L^{-1}
\right\}
\ll_A\log U
\tag{27}
\]

with multiplicity. Combining (19), (26), and (27), the **aggregate** positive-order Taylor contamination is therefore

\[
\ll_A
M_K(U)(\log U)\frac{\lambda_U}{1-O(\lambda_U)}
\ll
M_K(U)
U^{-\theta}(\log U)^{1-\varepsilon}
=o(M_K(U)).
\tag{28}
\]

This is the missing estimate. `RE-128` could control Taylor corrections only relative to each annular atom; dominance upgrades that per-atom estimate to a target-relative bound after summing every mode that survives the filter.

## 3. Inner-sector positivity now forces signed mass in the narrow annulus

Inside

\[
|\gamma-\gamma_0|\le\frac{c_*}{U},
\tag{29}
\]

we have `L|gamma-gamma_0|<1/2` for large `U`. Hence the multiplier in (25) is exactly one and all positive Fourier derivatives vanish. The phase-sector calculation of `RE-125` supplies a fixed `q_*>0` such that every inner atom satisfies

\[
\Re\!\left(
 a_{\rho,K}(U)e^{i(\gamma-\gamma_0)U}
\right)
\ge
q_*|a_{\rho,K}(U)|.
\tag{30}
\]

In particular, the dominant target contributes at least `q_*M_K(U)` to the real part of (24).

On the other hand, (8), the Gevrey time tail, and (28) give

\[
|I_{\rho_0}(U)|
\le
\|\phi\|_1\epsilon_*M_K(U)+o(M_K(U)).
\tag{31}
\]

Choose `epsilon_*` so that `||phi||_1 epsilon_*<q_*/4`. Taking real parts in (24)--(31) shows that the zeroth-order modes in the narrow transition annulus

\[
\mathcal A_{\theta,\varepsilon}(\rho_0;U)
:=
\left\{\rho\ne\rho_0:
\frac{c_*}{U}<|\gamma-\gamma_0|
\le
B\frac{(\log U)^{1+\varepsilon}}{H}
\right\}
\tag{32}
\]

must carry negative projected mass

\[
\sum_{\substack{\rho\in\mathcal A_{\theta,\varepsilon}\\
\Re(a_{\rho,K}(U)e^{i(\gamma-\gamma_0)U})<0}}
-\Re\!\left(
 a_{\rho,K}(U)e^{i(\gamma-\gamma_0)U}
\right)
\gg M_K(U).
\tag{33}
\]

The weights `w_rho` cause no sign loss: they are real and lie in `[0,1]`, so a negative weighted sum of size `gg M_K(U)` implies at least as much unweighted negative mass.

The same local count (27) shows that (32) contains `O_A(log U)` zeros with multiplicity. Pigeonholing (33) therefore gives a distinct-ordinate `rho_1` satisfying (10)--(11). Equation (12) follows from (11) and dominance (19), and dividing (11) by `|a_(rho_1,K)(U)|` gives (13).

The lower radius in (10) excludes equal-ordinate multiplicity. The horizontal localization and polynomial-height bounds in (14) follow from (12), (16), and (17) exactly as in `RE-126`--`RE-128`.

## 4. What this closes, and what it does not

`RE-127` localized the necessary **sign** only to the wider reciprocal annulus, while `RE-128` localized a comparable **magnitude** to the inverse-window annulus but explicitly could not transfer the sign there. The obstruction was that the annular coefficient entering a positive Taylor term might be much larger than the prescribed target. Selecting a coefficient-maximal target removes precisely that degree of freedom, and (28) merges the two conclusions.

The conclusion is deliberately existential at the packet level. It does **not** say that every prescribed algebraically strong zero has a cancelling companion at the narrow scale; a nonmaximal target may still suffer the amplification problem identified in `RE-128`. What is proved is enough for the branch dichotomy: whenever any algebraically strong atom is hidden, some dominant algebraically strong atom participates in an inverse-window, logarithmically comparable, correctly phased pair.

Nor does (10)--(13) rule out such pairs for zeta. The companion need not be consecutive, the pair may depend on `U`, and its scaled gap may wind through many `2pi` turns before landing in the cancelling half-plane. The theorem therefore does not convert current small-gap or half-isolation results into a contradiction. The remaining strong-atom gate is now genuinely a zero-geometry question: can an attained off-critical edge support infinitely many **dominant near-edge pairs** with spacing (10) and the cancelling projection (11)? The diffuse-cloud regime remains a logically separate escape, as do a nonattained edge and the endpoint `Theta=1`.

When `A<K+1`, the contrapositive has the same CA consequence as `RE-127`--`RE-128`: if no dominant pair satisfying (10)--(11) exists, then the residual cannot obey (8), so an algebraic continuum excursion survives on `|u-U|<=H`; `RE-123` then samples it on the superalgebraically fine regular-CA phase mesh.

## 5. Representation, adversarial audit, and prior-art boundary

No new arithmetic coordinate or probabilistic assumption is introduced. The dominant atom is selected from the same absolutely convergent subedge zero packet, and the filter is exactly the Gevrey readout already audited in `RE-128`. The only new estimate is the target-relative summation (28), obtained by combining coefficient maximality with the `O(log U)` number of modes surviving the inverse-window filter.

The main adversarial checks are the following. The maximum in (3) is attained because of reciprocal-square coefficient decay and zero discreteness. Multiplicity does not evade the result: equal-ordinate copies remain in the reinforcing inner ball and the cancelling companion produced by (32) has distinct ordinate. The local zero count is used only after (17) places the target at polynomial height and (23) gives a subunit interval. The polynomial factor `U^-theta` in (28) beats every fixed logarithmic loss, so the argument works for every fixed `varepsilon>0`, including `varepsilon<1`. The proof does not require the time-domain Gevrey kernel to be nonnegative; only `0<=hat(phi)<=1` is used for the zeroth-order sign. Far-horizontal, time-tail, Taylor-remainder, and conjugate-frequency errors are already `o(U^-A)` in `RE-128`, hence `o(M_K(U))` under (6).

A synthetic two-mode control with equal coefficients and spacing `pi/U`, already used in `RE-125`, remains a valid kill test against a stronger conclusion: such a pair is dominant, correctly phased, lies well inside the inverse-window radius because `H=o(U)`, and suppresses the target over the whole `H` window by `O(H/U)`. Thus `RE-129` does not falsely exclude the reciprocal-scale mechanism that the preceding findings identified as order-sharp.

The novelty audit separates the ingredients from the splice. Dominant-term selection, Gevrey frequency localization, Riemann--von Mangoldt local counting, and close-zero questions are classical. The closest zero-spacing literature remains Bui--Goldston--Milinovich--Montgomery, *Small gaps and small spacings between zeta zeros*, Acta Arithmetica **210** (2023), 133--153, DOI `10.4064/aa220731-15-2`, and Maynard--Pratt, *Half-Isolated Zeros and Zero-Density Estimates*, International Mathematics Research Notices **2024** (19), 12978--13014, DOI `10.1093/imrn/rnae191`. Those works study small spacings or vertical isolation, not the finite-edge Robin/CA residual or the dominant-coefficient mechanism (28). A targeted search found no prior theorem asserting the line-specific implication (10)--(13). No new external theorem is load-bearing beyond inputs already canonical in `RE-126`--`RE-128`, so `SOURCES.md` is unchanged.