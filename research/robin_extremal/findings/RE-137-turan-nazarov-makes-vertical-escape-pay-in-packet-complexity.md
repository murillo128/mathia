# RE-137 — Turán–Nazarov makes vertical escape pay in packet complexity

**Status:** `LITERATURE+DERIVED + EXACT-SPLICE + FINITE-ZERO-EDGE + LEADING-PACKET + TURAN-NAZAROV + ANISOTROPIC-OBSERVABILITY + VERTICAL-DIAMETER-FREE + COMPLEXITY-OR-HORIZONTAL-SPREAD + FINITE-ORDER-STABILITY + MATCHED-CONTROL + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

`RE-135`--`RE-136` show that a finite reciprocal-scale packet containing a target atom has a fixed-window visibility floor, and that the best uniform floor over a scaled box of radius `R` decays exponentially in `R`. Those results treat horizontal and vertical displacement symmetrically. For the Robin coefficient law that symmetry is too coarse.

The leading-order packet admits a stronger **anisotropic** statement: arbitrary vertical spectral diameter costs nothing in the observability constant. A packet can become uniformly small on a one-sided macroscopic window only by paying in either horizontal spread or packet complexity. This is a direct splice of the classical Turán--Nazarov inequality with the sector geometry of the Robin coefficient `1/[rho(1-rho)]`.

Assume

\[
\frac12<\sigma_0<\Theta<1,
\qquad 0<\kappa<1,
\tag{1}
\]

and let `C` be any finite multiset of positive-ordinate points

\[
\rho=\beta+i\gamma,
\qquad \sigma_0\le\beta<\Theta,
\qquad \gamma>0.
\tag{2}
\]

No spacing, simplicity, height, or vertical-diameter hypothesis is imposed. For `K=0`, write

\[
a_{\rho,0}(u)
:=
\frac{e^{-(\Theta-\beta)u}}{\rho(1-\rho)},
\tag{3}
\]

and

\[
\mathcal S_{C,0}(u)
:=
2\Re\sum_{\rho\in C}a_{\rho,0}(u)e^{i\gamma u}.
\tag{4}
\]

Fix a distinguished `rho_0=beta_0+i gamma_0` in `C`, let

\[
N:=\#C
\tag{5}
\]

(counting multiplicity), and define the scaled **horizontal** spread

\[
H_C(U)
:=
U\max_{\rho\in C}|\beta-\beta_0|.
\tag{6}
\]

Then there are constants `c_Theta>0` and `C_T>1`, independent of `U`, `C`, all ordinates, and the vertical diameter of `C`, such that

\[
\boxed{
\sup_{(1-\kappa)U\le u\le U}
|\mathcal S_{C,0}(u)|
\ge
c_\Theta
\exp[-H_C(U)]
\left(\frac{\kappa}{C_T}\right)^{2N-1}
|a_{\rho_0,0}(U)|.
}
\tag{7}
\]

Equivalently, after absorbing fixed constants,

\[
\boxed{
\sup_{(1-\kappa)U\le u\le U}
|\mathcal S_{C,0}(u)|
\ge
c_{\Theta,\kappa}
\exp[-H_C(U)-C_\kappa N]
|a_{\rho_0,0}(U)|.
}
\tag{8}
\]

The ordinate spread

\[
U\max_{\rho\in C}|\gamma-\gamma_0|
\tag{9}
\]

does not occur in (7)--(8). Thus **vertical escape by itself is not an escape mechanism for a bounded-complexity leading packet**.

There is also a finite-order stability consequence. Fix `K>=0`, `A>0`, and suppose `rho_0` maximizes `|a_(rho,K)(U)|` on `C`, with

\[
M:=|a_{\rho_0,K}(U)|\ge cU^{-A}.
\tag{10}
\]

If `kappa A<1`, then for every fixed `eta>0`, the same lower bound survives for `mathcal S_(C,K)` whenever

\[
(1+\kappa)H_C(U)
+C_1(\kappa)N
+\log(N+1)
\le
(1-\kappa A-\eta)\log U,
\tag{11}
\]

for a sufficiently large fixed `C_1(kappa)`. More precisely, for all sufficiently large `U`,

\[
\boxed{
\sup_{(1-\kappa)U\le u\le U}
|\mathcal S_{C,K}(u)|
\ge
c_{K,\Theta,\kappa}
\exp[-H_C(U)-C_\kappa N]M.
}
\tag{12}
\]

For every fixed `A`, one may choose a smaller relative subwindow with `kappa A<1`. Hence a symmetric hiding hypothesis on `|u-U|<=kappa_0 U` automatically gives access to such a one-sided subwindow.

The complementary matched control is also informative. For every `0<kappa<1/2`, there are purely vertical finite product packets with **zero horizontal spread** that hide on the one-sided window `[(1-kappa)U,U]` once their cardinality grows. For `kappa<1/3`, the same construction hides on the full symmetric window `[(1-kappa)U,(1+kappa)U]`. Thus the cardinality term is not a technical artifact: horizontal drift is not necessary if enough vertically organized modes are available.

The combined conclusion is sharper than the isotropic escape language of `RE-135`--`RE-136`:

\[
\boxed{
\text{small packet}
\Longrightarrow
\text{horizontal spread and/or growing local complexity},
}
\tag{13}
\]

while vertical diameter alone is absent from the lower bound. For the actual zeta problem this redirects the missing source-specific input: controlling how many relevant off-critical modes can cooperate is at least as important as controlling how far their ordinates spread.

## 1. The leading Robin coefficients lie in one strict sector

Put

\[
d_\rho:=\frac1{\rho(1-\rho)}.
\tag{14}
\]

Since

\[
\rho(1-\rho)
=
\beta(1-\beta)+\gamma^2
+i\gamma(1-2\beta),
\tag{15}
\]

the real part of the denominator is positive. In particular `Re d_rho>0` for every point in (2).

More quantitatively, write

\[
A_\rho:=\beta(1-\beta)+\gamma^2,
\qquad
B_\rho:=\gamma(1-2\beta).
\tag{16}
\]

Then

\[
\frac{\Re d_\rho}{|d_\rho|}
=
\frac{A_\rho}{\sqrt{A_\rho^2+B_\rho^2}}.
\tag{17}
\]

For fixed `beta`, the ratio `|B_rho|/A_rho` is maximized at

\[
\gamma=\sqrt{\beta(1-\beta)},
\tag{18}
\]

where

\[
\frac{|B_\rho|}{A_\rho}
=
\frac{2\beta-1}{2\sqrt{\beta(1-\beta)}}.
\tag{19}
\]

Consequently

\[
\boxed{
\Re d_\rho
\ge
2\sqrt{\Theta(1-\Theta)}\,|d_\rho|
}
\tag{20}
\]

uniformly for `1/2<beta<=Theta`. The constant decreases as the allowed right edge approaches `1`, but remains strictly positive for every fixed finite edge `Theta<1`.

This common sector is the Robin-specific ingredient. At the extrapolation anchor `x=0`, all positive-ordinate terms reinforce rather than cancel.

## 2. Turán--Nazarov removes the vertical diameter

Scale

\[
u=Ux,
\qquad x\in[0,1],
\tag{21}
\]

and remove the target horizontal damping by defining

\[
Q_C(x)
:=
e^{(\Theta-\beta_0)Ux}\mathcal S_{C,0}(Ux).
\tag{22}
\]

Using conjugate pairing,

\[
Q_C(x)
=
\sum_{\rho\in C}
\left[
 d_\rho e^{\lambda_\rho^+x}
+\overline{d_\rho}e^{\lambda_\rho^-x}
\right],
\tag{23}
\]

where

\[
\lambda_\rho^\pm
:=
U(\beta-\beta_0)\pm iU\gamma.
\tag{24}
\]

Thus `Q_C` is an exponential polynomial with at most `2N` distinct exponential terms, and

\[
\max_\rho|\Re\lambda_\rho^\pm|
\le H_C(U).
\tag{25}
\]

Crucially, the imaginary parts `+/- U gamma` may be arbitrarily large.

At `x=0`, (20) gives

\[
Q_C(0)
=2\sum_{\rho\in C}\Re d_\rho
\ge
4\sqrt{\Theta(1-\Theta)}\,|d_{\rho_0}|.
\tag{26}
\]

The point `x=0` is only an analytic extrapolation anchor for the finite exponential polynomial; it is not being interpreted as a physical CA sample.

Nazarov's measurable Turán inequality states that if

\[
p(x)=\sum_{j=1}^{m}c_je^{\lambda_jx},
\qquad \lambda_j\in\mathbb C,
\tag{27}
\]

`J` is a finite real interval and `E subset J` is measurable with positive measure, then for an absolute constant `C_T`,

\[
\max_J|p|
\le
\exp\!\left(
|J|\max_j|\Re\lambda_j|
\right)
\left(
\frac{C_T|J|}{|E|}
\right)^{m-1}
\sup_E|p|.
\tag{28}
\]

Apply (28) to `Q_C` with

\[
J=[0,1],
\qquad
E=[1-\kappa,1].
\tag{29}
\]

Since `m<=2N`, equations (25)--(29) imply

\[
\sup_E|Q_C|
\ge
4\sqrt{\Theta(1-\Theta)}
|d_{\rho_0}|
 e^{-H_C(U)}
\left(\frac{\kappa}{C_T}\right)^{2N-1}.
\tag{30}
\]

On `E`,

\[
|\mathcal S_{C,0}(Ux)|
=e^{-(\Theta-\beta_0)Ux}|Q_C(x)|
\ge
e^{-(\Theta-\beta_0)U}|Q_C(x)|.
\tag{31}
\]

But

\[
e^{-(\Theta-\beta_0)U}|d_{\rho_0}|
=|a_{\rho_0,0}(U)|.
\tag{32}
\]

Equations (30)--(32) prove (7).

The structural point is exact: the Turán--Nazarov factor depends on the real parts of the exponents and on the number of exponential terms, but not on their imaginary frequencies. After the Robin rescaling, those two resources become horizontal zero spread and packet cardinality. The vertical ordinates disappear from the observability cost.

## 3. Finite-order stability in the strong-atom regime

For fixed `K`, the finite-order Robin coefficient differs uniformly from the leading coefficient by

\[
a_{\rho,K}(u)
=a_{\rho,0}(u)\left(1+O_K(u^{-1})\right),
\tag{33}
\]

on the fixed strip, uniformly in `gamma`. Indeed, for `k>=1`, the ratio of the `k`th correction to `d_rho` is bounded by

\[
\frac{k!}{u^k}
\frac{|\rho|}{|1-\rho|^k}
\ll_{K,\sigma_0,\Theta}u^{-k},
\tag{34}
\]

and the factor `|rho|/|1-rho|^k` is uniformly bounded for fixed `k>=1` on the strip.

Suppose now that `rho_0` maximizes `|a_(rho,K)(U)|` on `C`, with `M` as in (10). Then, for large `U`,

\[
|a_{\rho,0}(U)|\le2M
\qquad(\rho\in C),
\tag{35}
\]

and

\[
|a_{\rho_0,0}(U)|\ge\frac12M.
\tag{36}
\]

The strong-atom hypothesis also bounds the target edge depth. The bracket in the coefficient law is uniformly bounded above, so

\[
M\ll e^{-(\Theta-\beta_0)U}.
\tag{37}
\]

Together with `M>=cU^-A`,

\[
\boxed{
(\Theta-\beta_0)U
\le A\log U+O_{A,K}(1).
}
\tag{38}
\]

For `u=Ux` with `x in [1-kappa,1]`, every member of `C` satisfies

\[
(\Theta-\beta)U
\le
(\Theta-\beta_0)U+H_C(U),
\tag{39}
\]

and therefore

\[
|a_{\rho,0}(u)|
\le
2M
\exp\!\left[
\kappa\bigl((\Theta-\beta_0)U+H_C(U)\bigr)
\right].
\tag{40}
\]

Using (33), (38), and summing before cancellation gives

\[
\boxed{
\sup_{(1-\kappa)U\le u\le U}
|\mathcal S_{C,K}(u)-\mathcal S_{C,0}(u)|
\ll
MN U^{-1+\kappa A}e^{\kappa H_C(U)}.
}
\tag{41}
\]

Meanwhile (7), (36), and fixed constants give

\[
\sup_{(1-\kappa)U\le u\le U}
|\mathcal S_{C,0}(u)|
\gg
M e^{-H_C(U)-C_\kappa N}.
\tag{42}
\]

The ratio of (41) to the right-hand side of (42) is at most

\[
\ll
N U^{-1+\kappa A}
\exp[(1+\kappa)H_C(U)+C_\kappa N].
\tag{43}
\]

Condition (11) makes (43) `O(U^-eta)`, after enlarging `C_1(kappa)` to absorb the fixed Turán constant. Hence the finite-order corrections cannot erase the leading Turán--Nazarov signal, proving (12).

A convenient sufficient form is the following. If `kappa A<1`, there is a fixed `c_*=c_*(A,K,kappa)>0` such that

\[
H_C(U)+N\le c_*\log U
\tag{44}
\]

implies (12) for all sufficiently large `U`. No vertical-diameter restriction is added.

## 4. Purely vertical matched control shows why complexity remains live

The absence of vertical diameter from the lower bound does **not** mean that vertical geometry is harmless when cardinality grows. A simple product construction shows the opposite.

First use the one-sided window

\[
I_\kappa=[1-\kappa,1],
\qquad 0<\kappa<\frac12.
\tag{45}
\]

Choose `alpha>0` so that

\[
\frac{2\pi}{3(1-\kappa)}
<\alpha<\frac{4\pi}{3}.
\tag{46}
\]

Such an `alpha` exists exactly because `kappa<1/2`. Then

\[
\alpha I_\kappa
\subset
\left(\frac{2\pi}{3},\frac{4\pi}{3}\right),
\tag{47}
\]

and therefore

\[
\boxed{
q:=\max_{x\in I_\kappa}|1+e^{i\alpha x}|<1.
}
\tag{48}
\]

At stage `j`, choose a large `U_j`, a common real part

\[
\beta_j:=\Theta-U_j^{-2},
\tag{49}
\]

and a common base ordinate

\[
\Gamma_j:=U_j^{A/2}.
\tag{50}
\]

For `1<=ell<=j`, let

\[
\varepsilon_{j,\ell}:=U_j^{-3}3^{-\ell},
\tag{51}
\]

and, for every subset `S subset {1,...,j}`, set

\[
\rho_{j,S}
:=
\beta_j+i\left[
\Gamma_j+
\frac1{U_j}
\sum_{\ell\in S}(\alpha+\varepsilon_{j,\ell})
\right].
\tag{52}
\]

All `2^j` points have **exactly the same real part**, so

\[
H_C(U_j)=0.
\tag{53}
\]

The ternary perturbations make the ordinates distinct. Uniformly for `x in I_kappa`, the finite-order brackets at two stage points differ relatively by

\[
O_K\!\left(
\frac{j}{U_j\Gamma_j}
+\frac1{U_j}
\right),
\tag{54}
\]

while the horizontal damping is identical. Freezing the common bracket therefore gives

\[
\sum_S a_{\rho_{j,S},K}(U_jx)e^{i\Im(\rho_{j,S})U_jx}
=
 a_{\rho_{j,\varnothing},K}(U_jx)e^{i\Gamma_jU_jx}
\prod_{\ell=1}^j
\left[
1+e^{i(\alpha+\varepsilon_{j,\ell})x}
\right]
+\mathcal E_j(x).
\tag{55}
\]

For sufficiently large `j`, the strict margin in (48) gives a fixed `q_1<1` with every factor in (55) bounded by `q_1`. Before cancellation,

\[
\sup_{x\in I_\kappa}|\mathcal E_j(x)|
\ll_K
|a_{\rho_{j,\varnothing},K}(U_jx)|
\left(
\frac{j}{U_j\Gamma_j}+\frac1{U_j}
\right)2^j.
\tag{56}
\]

Choosing `U_j` sufficiently lacunary makes the parenthesis times `2^j` tend to zero. Hence

\[
\boxed{
\sup_{x\in I_\kappa}
\left|
\sum_S a_{\rho_{j,S},K}(U_jx)e^{i\Im(\rho_{j,S})U_jx}
\right|
=o\!\left(
|a_{\rho_{j,\varnothing},K}(U_j)|
\right),
}
\tag{57}
\]

while all `2^j` atoms have asymptotically the same center magnitude `(1+o(1))U_j^-A`. The scaled vertical diameter is `O(j)`.

For a symmetric relative window `x in [1-kappa,1+kappa]`, the same one-factor construction works whenever

\[
\frac{2\pi}{3(1-\kappa)}
<
\frac{4\pi}{3(1+\kappa)},
\tag{58}
\]

which is equivalent to

\[
\boxed{\kappa<\frac13.}
\tag{59}
\]

Thus for every symmetric window narrower than one third of the center scale, a formal packet can achieve macroscopic hiding with **zero horizontal spread**. The escape resources are growing cardinality and growing vertical diameter. For wider symmetric windows, `RE-133` supplies the horizontal damping that this pure-phase factor lacks.

As in `RE-133`, the stages may be made arbitrarily lacunary and closed under conjugation and the functional equation symmetry. This matched control remains formal: it is not asserted to be a zeta zero set or to satisfy an Euler product or zeta explicit-formula constraints.

## 5. Consequence: an anisotropic escape alternative

Suppose a finite packet `C_U` contains a target `rho_0` and satisfies the leading-order hiding bound

\[
\sup_{(1-\kappa)U\le u\le U}
|\mathcal S_{C_U,0}(u)|
\le
\epsilon_U|a_{\rho_0,0}(U)|.
\tag{60}
\]

Then (8) forces

\[
\boxed{
H_{C_U}(U)+C_\kappa N_U
\ge
\log\frac1{\epsilon_U}-O_{\Theta,\kappa}(1).
}
\tag{61}
\]

Therefore, if `epsilon_U->0`, a packet with bounded horizontal spread cannot hide unless its cardinality diverges. A packet with bounded cardinality cannot hide unless its horizontal spread diverges. **Unbounded vertical diameter with both quantities bounded is insufficient.**

Under the strong-atom and logarithmic-complexity hypotheses of Section 3, the same alternative holds for the finite-order packet.

For the full infinite zeta packet, (61) is not by itself a contradiction. If a chosen finite core is visible, the complement may still cancel it at the witnessing point. The valid consequence is the same concentration-versus-exterior-cancellation logic used in `RE-134`--`RE-136`: a hidden full packet must either place enough horizontal/complexity resource inside the chosen core or import a cancelling contribution from outside it.

This changes the interpretation of the remaining `RE-136` escape. The missing source theorem is not merely a statement that ordinates cannot run far away. Large vertical distance alone does not buy invisibility for a finite low-complexity core. What matters is whether actual off-critical zeta zeros can supply a growing number of coherently organized modes, or a growing horizontal edge spread, while preserving the cancellation needed by the Robin packet.

## 6. Adversarial audit

Several tempting overstatements are excluded.

First, the Turán--Nazarov theorem is load-bearing in (7). The line-specific derivation is the rescaling (22)--(25), the exact Robin sector estimate (20), and the restoration of the target damping in (31)--(32). No novelty is claimed for the general exponential-polynomial inequality.

Second, imaginary frequencies genuinely disappear only from the **leading-order finite-packet lower bound**. The full finite-order law contains `u^-k` corrections. Section 3 does not silently ignore them: it proves a quantitative perturbation estimate and imposes the explicit complexity budget (11). No unrestricted `K>=1` vertical-diameter-free theorem is claimed.

Third, the target need not be the largest atom for the exact `K=0` inequality. Maximality is introduced only for the finite-order perturbation bound, where it controls the aggregate correction before cancellation.

Fourth, the analytic anchor `x=0` is outside the observed interval. This is precisely what Turán--Nazarov controls: propagation of smallness from the observed set back to the anchor. The proof does not pretend that `u=0` is a valid CA asymptotic sample.

Fifth, multiplicity causes no loophole. If repeated exponents are combined, the actual number `m` of distinct exponential terms only decreases, strengthening the Turán exponent. Counting multiplicity by `N` therefore gives a valid weaker bound.

Sixth, (7) is a statement about a selected finite packet, not the entire infinite subedge sum. Exterior cancellation remains possible and is stated explicitly.

Seventh, the pure-vertical control is intentionally one-sided for every `kappa<1/2`; its symmetric version is claimed only for `kappa<1/3`. The wider symmetric case still requires another mechanism such as the horizontal damping in `RE-133`.

Finally, the September 2026 global advances proving that more than two thirds of zeta zeros are simple and on the critical line, and that more than five sixths are distinct, do not supply the local bounded-complexity theorem needed here. A lacunary off-critical cluster may have zero global density and still be compatible with such proportion statements. This is consistent with the warning already built into the Research Watch contract: density/proportion control is not exclusion of every exceptional off-critical configuration.

## 7. Prior-art boundary and research effect

The external theorem used in (28) is F. L. Nazarov, *Local estimates for exponential polynomials and their applications to inequalities of the uncertainty principle type*, Algebra i Analiz **5** (1993), no. 4, 3--66; English translation, St. Petersburg Mathematical Journal **5** (1994), 663--717. The exact feature used here is that, for complex exponents, the propagation factor depends exponentially on the largest absolute **real** part and algebraically on the number of terms, while the imaginary frequencies do not enter that factor.

A current neighboring reference is Omer Friedland, *A Disk-Growth Remez Principle and a Modular Proof of the Measurable Turán-Nazarov Inequality*, arXiv:2606.24823 (23 June 2026), which gives a modern modular proof of the measurable inequality. Neither source concerns Robin's divisor-sum residual, colossally abundant phases, or the coefficient sector (20).

The recent simple/distinct-zero results of Alpöge--Furman, *More than two thirds of the zeta zeros are simple and on the critical line*, arXiv:2608.13637 (13 August 2026), and Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882 (September 2026), were checked as current zeta-side prior art. They materially improve global proportions but do not give the uniform microscopic local-complexity exclusion required by (61).

`RE-135` established a fixed-box visibility floor independent of local occupancy. `RE-136` quantified the cost of increasing an isotropic scaled radius. `RE-137` separates the two coordinates: for a finite leading packet, **vertical spectral diameter is free in the lower bound; horizontal spread and term complexity are the resources that pay for propagation of smallness**. The pure-vertical matched control then shows why the complexity resource cannot be dropped.

The next source-specific question is consequently sharper. One does not need a blanket minimum-spacing theorem for all zeta zeros. One needs a theorem preventing enough **relevant off-critical modes** from forming a growing, coherently cancelling local family at the same horizontal edge depth, or else a theorem forcing any such family to import enough horizontal spread that the Robin damping destroys it. Global simplicity percentages, global pair-correlation averages, and one-level zero-density estimates still allow rare lacunary exceptional clusters and therefore do not close this frontier.