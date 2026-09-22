# WI-391 — Source-exact dilute carriers open a positive RH Weil floor beyond logarithmic compactness

**Status:** `EXACT-DERIVED + CLASSICAL-RH-INPUT + SOURCE-EXACT + STRUCTURAL-ESCAPE + PRIOR-ART-AUDITED + NON-ESTABLISHED-RH`.

## Claim

WI-388–WI-390 locate a sharp logarithmic compactness boundary for fixed-width endpoint-adaptive Weil trials. Below that boundary the recurrence argument forces a zero floor under RH; WI-388 shows that a dilute `1/log R` high-frequency sideband can escape the compactness hypothesis, but it deliberately leaves the endpoint phase factors uncontrolled. The phase gate can in fact be crossed if the carrier frequency is allowed to grow sufficiently fast relative to the endpoint.

There are constants `L,beta,kappa>0` and, for every sufficiently large integer `k`, a fixed-width positive-lobe profile `p_k` obtained by the standard exact Desogus source-slot perforation at

\[
A_k=\log(k+1),
\qquad x_k=k+1,
\tag{1}
\]

such that the reflected separated odd trial

\[
f_k(y)=p_k(y-A_k/2)-p_k(-y-A_k/2)
\tag{2}
\]

is exact on the required prime-power source slots and has a uniformly negative one-lobe archimedean margin after normalization, while **under RH**

\[
\boxed{
\liminf_{k\to\infty}\mathcal W[f_k]\ge \kappa>0.
}
\tag{3}
\]

Equivalently: the source-exact zero-floor theorems of WI-387/WI-390 cannot be extended to all fixed-width endpoint-adaptive profiles merely from exact source zeros plus a uniform negative archimedean lobe budget. Once a nonvanishing amount of logarithmically weighted Fourier mass is allowed to escape to frequencies `R_k` satisfying

\[
A_k=o(\log\log R_k),
\tag{4}
\]

the RH zero density in a fixed carrier window averages the endpoint factor `sin^2(A_k gamma/2)` to a positive constant before finite-frequency recurrence can suppress it.

A concrete choice is

\[
\boxed{
R_k=\exp\!\bigl(\exp(A_k^2)\bigr).
}
\tag{5}
\]

Then `log log R_k=A_k^2`, so (4) holds. No unconditional positive Weil gap, RH proof, or improved simple-critical-zero proportion is claimed. The result is an RH-side structural escape from the recurrence obstruction, not a completion of the source/arithmetic positivity program.

## 1. Start from the WI-388 dilute carrier

WI-388 constructs a fixed real even smooth normalized base profile

\[
\phi\in C_c^\infty((-L/2,L/2)),
\qquad \|\phi\|_2=1,
\qquad B_\phi\le-3\beta,
\tag{6}
\]

and, for every sufficiently large `R`, a real even normalized carrier `nu_R` on the same support, orthogonal to `phi`, such that

\[
\mathcal E(\nu_R)\ll 1+\log R,
\tag{7}
\]

where `mathcal E` is the WI-388 screened archimedean difference form. For a fixed sufficiently small `c>0`, put

\[
\varepsilon_R=\frac{c}{\log R},
\qquad
g_R=\sqrt{1-\varepsilon_R}\,\phi+
\sqrt{\varepsilon_R}\,\nu_R.
\tag{8}
\]

Then `||g_R||_2=1` and, after fixing `c` small enough once and for all,

\[
\boxed{B_{g_R}\le-\beta}
\tag{9}
\]

for all large `R`.

Write

\[
\widehat g_R(\xi)=\int g_R(s)e^{i\xi s}\,ds.
\tag{10}
\]

WI-388 also supplies fixed constants `delta,c_0>0` for which

\[
\boxed{
|\widehat g_R(\xi)|^2
\ge \frac{c_0c}{\log R}
\qquad (|\xi-R|\le\delta)
}
\tag{11}
\]

for all large `R`. The key point is the scale match: only `1/log R` of the `L^2` mass is spent on the escaping packet, while a fixed ordinate window near height `R` contains order `log R` zeros.

For the endpoint sequence (1), set

\[
g_k=g_{R_k},
\qquad R_k=\exp(\exp(A_k^2)).
\tag{12}
\]

The remaining issue left open by WI-388 is whether the endpoint multiplier `sin^2(A_k gamma/2)` can make essentially all of those `Theta(log R_k)` sampled zeros useless. Under RH, Littlewood's bound for the zeta argument rules this out at the scale (12).

## 2. RH gives a phase-weighted local zero asymptotic when `A=o(log log R)`

Choose once and for all

\[
0\le w\in C_c^\infty((-\delta,\delta)),
\qquad w\not\equiv0,
\qquad \|w\|_\infty\le1.
\tag{13}
\]

For `R` large and `A>0`, define the multiplicity-weighted phase count

\[
Z(R,A)=
\sum_{\gamma>0}m_\gamma
w(\gamma-R)
\sin^2\!\left(\frac{A\gamma}{2}\right).
\tag{14}
\]

Let `N(t)` count positive ordinates with multiplicity. The Riemann--von Mangoldt formula in its standard `M(t)+S(t)` form, followed by Stieltjes integration by parts against

\[
F_{R,A}(t)=w(t-R)\sin^2(At/2),
\tag{15}
\]

gives

\[
Z(R,A)
=
\frac{\log R}{2\pi}
\int_{\mathbb R}w(u)
\sin^2\!\left(\frac{A(R+u)}2\right)du
+
O_w\!\left(
1+(1+A)\sup_{|t-R|\le\delta}|S(t)|
\right).
\tag{16}
\]

The derivative of (15) has `L^1` norm `O_w(1+A)`, which is the only reason the factor `1+A` occurs. Assuming RH, Littlewood's classical estimate is

\[
S(t)=O\!\left(\frac{\log t}{\log\log t}\right).
\tag{17}
\]

Hence

\[
Z(R,A)
=
\frac{\log R}{2\pi}
\int w(u)
\sin^2\!\left(\frac{A(R+u)}2\right)du
+
O_w\!\left(
\frac{(1+A)\log R}{\log\log R}
\right).
\tag{18}
\]

The main integral itself has no adverse phase subsequence. Indeed,

\[
\int w(u)\sin^2\!\left(\frac{A(R+u)}2\right)du
=
\frac12\int w
-
\frac12\Re\!\left(
 e^{iAR}\int w(u)e^{iAu}du
\right).
\tag{19}
\]

Because `w` is smooth and compactly supported, its Fourier transform decays rapidly. Thus as `A->infinity`, uniformly in the carrier-center phase `AR`, the right side of (19) tends to `(1/2) integral w`. Combining this with (18) gives the exact scale statement

\[
\boxed{
A\to\infty,
\qquad
\frac{A}{\log\log R}\to0
\quad\Longrightarrow\quad
Z(R,A)\ge c_w\log R
}
\tag{20}
\]

for some fixed `c_w>0` and all sufficiently large pairs `(R,A)` in that regime.

For (12), `A_k/log log R_k=1/A_k->0`, so

\[
Z(R_k,A_k)\ge c_w\log R_k.
\tag{21}
\]

This is the phase information missing from WI-388. It is not pair correlation or a spacing theorem: it is a direct weighted consequence of the ordinary Riemann--von Mangoldt formula plus the RH bound for `S(t)`.

## 3. The unperforated adaptive trial already has a positive RH spectral floor

Let

\[
f_k^0(y)=g_k(y-A_k/2)-g_k(y+A_k/2).
\tag{22}
\]

Under RH the Weil form is the nonnegative spectral square used throughout WI-386--WI-390:

\[
\mathcal W[f_k^0]
=
4\sum_{\gamma>0}m_\gamma
|\widehat g_k(\gamma)|^2
\sin^2\!\left(\frac{A_k\gamma}{2}\right),
\tag{23}
\]

up to the fixed harmless convention of whether positive and negative ordinates are both written explicitly. Since `0<=w<=1`, restricting (23) to the packet in (11) and using (21) gives

\[
\begin{aligned}
\mathcal W[f_k^0]
&\ge
4\frac{c_0c}{\log R_k}
\sum_{\gamma>0}m_\gamma
w(\gamma-R_k)
\sin^2\!\left(\frac{A_k\gamma}{2}\right)\\
&\ge 4c_0cc_w.
\end{aligned}
\tag{24}
\]

Therefore

\[
\boxed{
\liminf_{k\to\infty}\mathcal W[f_k^0]
\ge \kappa_0:=4c_0cc_w>0.
}
\tag{25}
\]

This does not contradict WI-387/WI-390. The family `(g_k)` intentionally violates their compactness hypothesis: an order-one amount of `log(2+|xi|)`-weighted Fourier energy moves to `R_k`, so there is no uniformly integrable logarithmic spectral tail on which finite-frequency recurrence could act.

## 4. Exact source perforation does not destroy the carrier reserve

It remains to impose the exact prime-power source slots **at the same endpoints `A_k`**, rather than using the diagonal-after-the-fact compatibility statement of WI-388.

Let `chi_k` be the centered positive-lobe cutoff of WI-390, `eta_k=1-chi_k`, and let `E_k=supp eta_k`. Put

\[
p_k=\chi_k g_k,
\qquad
r_k=g_k-p_k=\eta_k g_k.
\tag{26}
\]

WI-390 establishes the source geometry

\[
\mu_k:=|E_k|
\ll_L \frac1{\sqrt{x_k}\log x_k},
\qquad
\kappa_k:=\widetilde D[\eta_k]
\ll_L x_k^{-1/2},
\tag{27}
\]

where

\[
\widetilde D[v]
=\frac12\iint
h(|s-t|)|v(s)-v(t)|^2\,ds\,dt,
\qquad
h(u)=\frac{e^{-u/2}}{1-e^{-2u}}.
\tag{28}
\]

The high carrier oscillation looks dangerous because `R_k` is vastly larger than the inverse source-slot width. The `1/log R_k` dilution cancels exactly the only growing cost.

For the normalized WI-388 carrier, define the pointwise jump density

\[
J_R(t)=
\int h(|s-t|)|\nu_R(s)-\nu_R(t)|^2\,ds.
\tag{29}
\]

The same increment decomposition used in WI-388, now before integrating in `t`, gives uniformly on the fixed support

\[
\boxed{
\|\nu_R\|_\infty\ll1,
\qquad
\sup_t J_R(t)\ll 1+\log R.
}
\tag{30}
\]

Indeed the oscillatory increment is bounded by `min(2,R|s-t|)`; splitting the `h(u)~1/u` singularity at `u=1/R` contributes `O(1)+O(log R)`. Orthogonalization by the vanishing scalar in WI-388 and normalization by a quantity tending to `1/sqrt(2)` preserve the estimate.

The elementary product inequality

\[
|\eta(s)v(s)-\eta(t)v(t)|^2
\le
2\eta(s)^2|v(s)-v(t)|^2
+2|v(t)|^2|\eta(s)-\eta(t)|^2
\tag{31}
\]

then yields

\[
\widetilde D[\eta_k\nu_{R_k}]
\ll
\mu_k(1+\log R_k)+\kappa_k.
\tag{32}
\]

After the dilute amplitude is restored,

\[
\boxed{
\widetilde D[
\sqrt{\varepsilon_{R_k}}\,\eta_k\nu_{R_k}]
\ll
c\mu_k+
\frac{c\kappa_k}{\log R_k}
\longrightarrow0.
}
\tag{33}
\]

Likewise

\[
\|\sqrt{\varepsilon_{R_k}}\,\eta_k\nu_{R_k}\|_2^2
\ll \frac{c\mu_k}{\log R_k}\to0.
\tag{34}
\]

For the fixed base `phi`, the same argument with bounded `J_phi` gives

\[
\|\eta_k\phi\|_2^2+
\widetilde D[\eta_k\phi]
\ll \mu_k+\kappa_k\to0.
\tag{35}
\]

Since `sqrt(tilde D)` is a seminorm, (8), (33), and (35) imply

\[
\boxed{
\|r_k\|_2^2+\widetilde D[r_k]\to0.
}
\tag{36}
\]

This is stronger than the diagonal statement in WI-388 for the present family: the exact source cutoff is negligible **uniformly along the prescribed endpoint/carrier coupling (12)** even though the full profiles are not logarithmically compact.

By the multiplier comparison and fixed-support zeta-sampling estimate of WI-389/WI-390, (36) implies

\[
\boxed{
\sum_\rho |\widehat r_k(\gamma)|^2\to0.
}
\tag{37}
\]

The perturbation from `f_k^0` to the reflected exact source-zero odd pair `f_k` has transform magnitude at most `2|hat r_k(gamma)|` at each critical-line zero. Under RH, therefore,

\[
\mathcal W[f_k-f_k^0]\to0.
\tag{38}
\]

Using the triangle inequality in the RH spectral Hilbert seminorm together with (25),

\[
\sqrt{\mathcal W[f_k]}
\ge
\sqrt{\mathcal W[f_k^0]}
-
\sqrt{\mathcal W[f_k-f_k^0]},
\tag{39}
\]

so for all sufficiently large `k`, for example,

\[
\boxed{
\mathcal W[f_k]\ge \kappa_0/4>0.
}
\tag{40}
\]

This proves (3). Also `||p_k||_2->1`; normalizing each lobe changes (40) only by a factor tending to one and preserves the exact source zeros.

Finally, (36) controls the same screened norm entering the one-lobe archimedean functional. The unperforated family has uniformly bounded screened energy by (7)--(8), and (9) has a fixed strict margin. Hence after normalization,

\[
B_{p_k/\|p_k\|_2}\le-\beta/2
\tag{41}
\]

for all sufficiently large `k`. The source-exact positive RH spectral floor is therefore compatible with the gamma-negative local geometry that motivated the fixed-width construction.

## 5. What this changes, and what it does not

WI-387 proves recurrence once zeta-sampled tails are uniformly tight. WI-389 identifies uniform logarithmic Fourier-tail integrability as the intrinsic scalar compactness condition, and WI-390 shows that exact source perforation preserves that barrier. WI-388 constructs the escaping logarithmic sideband but leaves its endpoint phases uncontrolled. Equations (16)--(40) close precisely that remaining gap:

\[
\boxed{
\text{dilute log-cost carrier}
+
A_k=o(\log\log R_k)
+
\text{RH local zero regularity}
\Longrightarrow
\text{source-exact positive spectral floor}.
}
\tag{42}
\]

Thus the logarithmic boundary is not only a failure of a proof technique. On the RH spectral side there are actual fixed-width source-exact adaptive families beyond it for which the zero-floor conclusion is false.

The result does **not** supply an unconditional coercive Weil theorem. Its key phase-density input (17) assumes RH, and positivity of the spectral square in (23), (38), and (39) is also the RH representation. Nor does a positive RH-side floor by itself solve the source/arithmetic side needed for a proof of RH; the profile complexity has been moved to doubly exponential carrier frequencies, and no claim is made that the resulting trials fit an independent finite-dimensional SDP, determinant, or inertia certification with useful off-line sign control.

What it does settle is the scope of the recurrence no-go. A future theorem trying to rule out every fixed-width adaptive profile cannot rely only on exact source slots, negative `B_g`, or generic logarithmic compactness arguments. It must add genuinely zeta-specific control strong enough to constrain this moving packet, constrain the allowed endpoint/carrier relation, or change the geometric/operator category.

## Prior-art and novelty audit

The number-theoretic input in Section 2 is classical. Littlewood proved under RH the order

\[
S(t)=O(\log t/\log\log t)
\]

in J. E. Littlewood, *On the zeros of the Riemann zeta-function*, Proceedings of the Cambridge Philosophical Society 22 (1924), 295--318, DOI `10.1017/S0305004100014225`. Modern stronger constants are given by E. Carneiro, V. Chandee, and M. B. Milinovich, *Bounding S(t) and S_1(t) on the Riemann hypothesis*, arXiv:1309.1526, which proves `|S(t)| <= (1/4+o(1)) log t/log log t` under RH. Only the order of magnitude is used here. The smoothed phase-weighted estimate (16)--(20) is a direct Stieltjes-integration consequence of Riemann--von Mangoldt plus that classical `S(t)` bound.

The harmonic-analytic ingredients are inherited locally: WI-388 supplies the dilute carrier, logarithmic archimedean cost, negative lobe margin, and packet lower bound; WI-389 supplies the fixed-support logarithmic zeta-sampling inequality; WI-390 supplies the exact source-hole measure/capacity estimates and the screened-form multiplier comparison.

A targeted literature search around smoothed fixed-window zeta zero counts, `S(t)`-controlled short intervals, Weil-criterion high-frequency modulation, and adaptive carrier test functions found the classical ingredients but no source packaging the endpoint phase average together with a `1/log R` Weil sideband and exact moving prime-power source perforation. That negative search is not a priority claim. The new content recorded here is the exact coupling (4), the phase-weighted local count (20) in the needed form, and the source-exact transfer (33)--(40) for the escaping family.

## Evidence boundary

- **Classical / literature-backed:** Riemann--von Mangoldt; Littlewood's RH bound `S(t)=O(log t/log log t)`; rapid Fourier decay of a fixed smooth bump; Stieltjes integration by parts.
- **Persisted exact inputs:** WI-388's carrier construction and packet lower bound; WI-389's fixed-support zeta-sampling inequality; WI-390's source-hole measure, screened capacity, and source-exact cutoff geometry.
- **Exact deduction here:** the weighted local phase lower bound under `A=o(log log R)`; the explicit carrier schedule (5); the pointwise carrier jump estimate (30); cancellation of the source-mask cost by `epsilon_R= c/log R`; and the resulting positive source-exact RH Weil floor.
- **Conditional:** (17), the nonnegative spectral representation, and therefore the positive floor (3) assume RH.
- **Not claimed:** RH; an unconditional positive Weil gap; a new simple-critical-zero proportion; a non-RH dichotomy; useful finite-frequency complexity; or a proof that this escaping family detects off-critical zeros with a favorable sign.

## Research consequence

The fixed-width recurrence branch has now separated into two genuinely different regimes. Logarithmically compact families are ruled out by WI-390, while this finding shows that sufficiently fast noncompact logarithmic escape can produce a true source-exact RH-side positive floor. The next useful question is no longer whether generic Sobolev/logarithmic compactness can be weakened. It is whether arithmetic or off-line signature information can control, exploit, or exclude the moving high-frequency packet itself.