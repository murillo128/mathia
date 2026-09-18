# NB-211 — Full Vinogradov--Korobov contour pushes the prime Halasz gap to a log-squared diagonal corridor

**Date:** 2026-09-18  
**Status:** `LITERATURE+DERIVED + REFINEMENT + SOURCE-ACQUISITION + POSITIVE-EULER + PRIME-HALASZ + ZERO-FREE-REGION + DIAGONAL-CORRIDOR + NB-210-REFINEMENT`.

`NB-210` uses Matomaki--Radziwill's prime-supported Halasz inequality exactly as published. Its off-diagonal term is

\[
\exp\!\left[-\frac{\log P}{(\log T)^{2/3+\epsilon}}\right](\log T)^2,
\]

with `epsilon>0` fixed. That fixed epsilon is enough for every fixed subcritical height

\[
\log |t|\le X^{3/2-\delta},
\]

but it cannot be sent to zero along the coupled limit. The apparent boundary is therefore a quantifier boundary in the stated lemma, not yet a boundary of its proof.

The proof of Matomaki--Radziwill's Lemma 11 exposes a stronger statement. Its only source of the exponent `2/3+epsilon` is the deliberately weakened zero-free contour used to estimate a smoothed prime-power correlation kernel through `-zeta'/zeta`. Retaining the full Vinogradov--Korobov zero-free width instead gives an epsilon-free prime Halasz inequality with off-diagonal factor

\[
\boxed{
E_{\rm VK}(P,T)
:=
(\log(10T))^2
\exp\!\left[
-c\frac{\log P}
{(\log(10T))^{2/3}(\log\log(10T))^{1/3}}
\right]
}
\tag{1}
\]

for some absolute `c>0`. Feeding (1) into the fixed-harmonic amplification of `NB-210` yields constants `kappa_*,eta_*>0` such that, with

\[
x_a=e^{r_0/a},\qquad X_a=\log x_a=\frac{r_0}{a},
\]

and the normalized positive Euler-shell defect `mathcal A_a(t)` from `NB-208`--`NB-210`, one has for all sufficiently small `a`

\[
\boxed{
1\le |t|\le
\exp\!\left(
\kappa_*\frac{X_a^{3/2}}{(\log X_a)^2}
\right)
\quad\Longrightarrow\quad
\mathcal A_a(t)\ge\eta_*.
}
\tag{2}
\]

This is a genuine diagonal improvement over `NB-210`: the ordinate exponent is `X_a^(3/2-o(1))`, so it eventually exceeds `X_a^(3/2-delta)` for every fixed `delta>0`. It still does **not** reach the farther Ford corridor of `NB-205`,

\[
\log |t|\asymp
\frac{X_a^{3/2}}{\sqrt{\log X_a}},
\]

where only an `Omega(1/X_a)` gap is currently certified. The remaining separation in logarithmic height is a factor `(log X_a)^(3/2)`. After the present refinement, that gap is no longer caused by the fixed-epsilon formulation of Lemma 11; it comes from the polynomial prefactor in the prime correlation kernel together with the finite Vinogradov--Korobov contour width.

## 1. The prime Halasz proof admits an epsilon-free Vinogradov--Korobov form

Let

\[
P(s)=\sum_{P\le p\le2P}a_p p^{-s}
\]

and let `mathcal T subset [-T,T]` be well spaced. Matomaki--Radziwill prove their prime Halasz inequality by duality. After opening the dual square they dominate the prime correlation by the smoothed prime-power kernel

\[
K_P(\tau)
:=
\sum_{p^k}\log p\,p^{ik\tau}
 f\!\left(\frac{p^k}{P}\right),
\tag{3}
\]

where `f` is a fixed smooth cutoff. Mellin inversion gives

\[
K_P(\tau)
=
-\frac1{2\pi i}
\int
\widetilde f(s)
\frac{\zeta'}{\zeta}(s-i\tau)
P^s\,ds.
\tag{4}
\]

Their published proof truncates the integral and shifts it to a line of the form

\[
\sigma=1-c(\log T)^{-2/3-\epsilon},
\tag{5}
\]

which yields exactly the denominator `(log T)^(2/3+epsilon)` in the displayed Lemma 11 error. Nothing else in the duality argument introduces that epsilon.

Use instead the full Vinogradov--Korobov zero-free region. To avoid irrelevant small-height notation, put

\[
L_T:=\log(10T),
\qquad
R_T:=L_T^{2/3}(\log L_T)^{1/3}.
\tag{6}
\]

The standard Vinogradov--Korobov region, in particular the explicit modern form already anchored in this line through Bellotti, gives an absolute `c_0>0` such that `zeta(s)` has no zero in

\[
\Re s\ge1-\frac{c_0}{R_T}
\]

for all imaginary arguments of size `O(T)`; bounded imaginary arguments are absorbed by shrinking the constant. Shift (4) to

\[
\sigma=1-\frac{c_1}{R_T}
\tag{7}
\]

with fixed `0<c_1<c_0/2`.

The same local logarithmic-derivative formula used in the original proof gives on this contour

\[
\frac{\zeta'}{\zeta}(\sigma+iv)
=
\sum_{|v-\gamma|<1}
\frac1{\sigma+iv-\rho}
+O(L_T).
\tag{8}
\]

There are `O(L_T)` zeros in the unit window, while (7) stays a horizontal distance `gg 1/R_T` to their right. Hence

\[
\left|\frac{\zeta'}{\zeta}(\sigma+iv)\right|
\ll L_T R_T
\ll L_T^2.
\tag{9}
\]

The pole at `1` is crossed exactly as in Matomaki--Radziwill and produces the same rapidly decaying Mellin main term. Smooth Mellin decay handles the horizontal and truncation pieces exactly as in their proof. Therefore

\[
\boxed{
K_P(\tau)
=
\frac{\widetilde f(1+i\tau)}{1+i\tau}
P^{1+i\tau}
+
O\!\left(
P E_{\rm VK}(P,T)
\right)
}
\tag{10}
\]

uniformly for the differences `tau` arising from `mathcal T`, after harmless replacement of `T` by a fixed multiple inside the logarithms.

The main term in (10) has the same summable row bound `O(P)` on a well-spaced set that is used in the original proof. Repeating its duality step therefore gives the refined inequality

\[
\boxed{
\sum_{u\in\mathcal T}|P(iu)|^2
\ll
\left(
P+|\mathcal T|P E_{\rm VK}(P,T)
\right)
\sum_{P\le p\le2P}
\frac{|a_p|^2}{\log P}.
}
\tag{11}
\]

This is not a new Halasz mechanism. It is the same proof with the zero-free contour retained at its natural Vinogradov--Korobov width instead of weakened to a fixed power epsilon.

## 2. The harmonic plateau now has a moving diagonal range

Keep the fixed prime sub-shell from `NB-210`. Choose

\[
1<\kappa_0<\min\{2,e^\Delta\},
\]

put

\[
\mathcal P_a=\{p:x_a\le p<\kappa_0x_a\},
\qquad
M_a=|\mathcal P_a|\asymp\frac{x_a}{X_a},
\]

and define

\[
U_a(u)
:=
\frac1{M_a}
\sum_{p\in\mathcal P_a}p^{-iu}.
\tag{12}
\]

The positive Euler transfer proved in `NB-210` gives a constant `C_0`, depending only on the fixed shell parameters, such that

\[
1-\Re U_a(ht)
\le C_0 h\,\mathcal A_a(t).
\tag{13}
\]

Apply (11) with `P=x_a`, coefficients equal to one on `mathcal P_a` and zero on the rest of `[x_a,2x_a]`, and the well-spaced set

\[
\mathcal T_{H,t}=\{t,2t,\ldots,Ht\},
\qquad |t|\ge1.
\]

Since `M_a asymp x_a/X_a`, normalization by `M_a^2` gives

\[
\boxed{
\sum_{h=1}^{H}|U_a(ht)|^2
\le C_1
\left(
1+H E_a(H,t)
\right),
}
\tag{14}
\]

where `C_1` is fixed and

\[
E_a(H,t)
:=
Q^2
\exp\!\left[
-c\frac{X_a}{Q^{2/3}(\log Q)^{1/3}}
\right],
\qquad
Q:=\log(10H|t|),
\tag{15}
\]

with bounded `Q` absorbed into the constants.

Now choose once and for all an integer `H_0` sufficiently large relative to `C_1`. If `mathcal A_a(t)` is smaller than a sufficiently small fixed `eta_0`, then (13) forces

\[
|U_a(ht)|\ge\frac34
\qquad(1\le h\le H_0),
\tag{16}
\]

and hence

\[
\sum_{h=1}^{H_0}|U_a(ht)|^2
\ge\frac9{16}H_0.
\tag{17}
\]

For the chosen `H_0`, (14) contradicts (17) whenever `E_a(H_0,t)` is smaller than a fixed constant. Consequently there is a fixed `eta_*>0` such that

\[
\boxed{
E_a(H_0,t)=o(1)
\quad\Longrightarrow\quad
\mathcal A_a(t)\ge\eta_*.
}
\tag{18}
\]

The crucial change from `NB-210` is that (18) has no fixed epsilon parameter left to diagonalize.

## 3. Solving the off-diagonal inequality gives the log-squared `3/2` scale

Let

\[
Q_a^*
:=
\kappa\frac{X_a^{3/2}}{(\log X_a)^2}
\tag{19}
\]

for a fixed positive `kappa`. At the upper edge `Q<=Q_a^*+O(1)`, monotonicity gives

\[
Q^{2/3}(\log Q)^{1/3}
\le
\left(
\kappa^{2/3}
\left(\frac32\right)^{1/3}
+o(1)
\right)
\frac{X_a}{\log X_a}.
\tag{20}
\]

Therefore

\[
\frac{cX_a}{Q^{2/3}(\log Q)^{1/3}}
\ge
\left(
C\kappa^{-2/3}+o(1)
\right)
\log X_a
\tag{21}
\]

for some fixed `C>0`, whereas

\[
2\log Q
\le
3\log X_a-4\log\log X_a+O(1).
\tag{22}
\]

Choose `kappa=kappa_*` small enough that `C kappa_*^(-2/3)>4`. Combining (15), (21), and (22) gives

\[
\sup_{1\le |t|\le \exp(Q_a^*)}
E_a(H_0,t)
\longrightarrow0.
\tag{23}
\]

Equation (18) now proves (2).

The natural analytic threshold is visible directly from (15). The refined prime-Halasz argument succeeds whenever

\[
\boxed{
\frac{X_a}
{Q^{2/3}(\log Q)^{1/3}}
- C'\log Q
\longrightarrow+\infty
}
\tag{24}
\]

for a suitable fixed constant `C'`. Balancing the two terms in (24) gives

\[
Q^{2/3}(\log Q)^{4/3}\asymp X_a,
\]

or

\[
\boxed{
Q\asymp
\frac{X_a^{3/2}}{(\log X_a)^2}.
}
\tag{25}
\]

Thus the power `(log X_a)^2` is not an artifact of choosing a convenient corollary. It is the actual threshold of this contour-plus-Halasz estimate up to constants and lower-order logarithms.

## 4. This strictly diagonalizes `NB-210` but still stops before Ford

For every fixed `delta>0`,

\[
\frac{X_a^{3/2}/(\log X_a)^2}
{X_a^{3/2-\delta}}
=
\frac{X_a^\delta}{(\log X_a)^2}
\longrightarrow\infty.
\tag{26}
\]

Hence (2) is strictly stronger than taking any one of the fixed-delta statements in `NB-210`; it follows the exponent all the way to `3/2-o(1)`. This does not contradict the fixed-epsilon warning in `NB-210`. Applying Lemma 11 **as stated** still cannot justify a moving epsilon. The present argument instead reruns its proof with a different, epsilon-free contour.

The Ford frontier of `NB-205` lies farther out:

\[
Q_{\rm Ford}
\asymp
\frac{X_a^{3/2}}{\sqrt{\log X_a}}.
\tag{27}
\]

Consequently

\[
\frac{Q_{\rm Ford}}{Q_{\rm Halasz,VK}}
\asymp
(\log X_a)^{3/2}.
\tag{28}
\]

At the Ford scale, the Vinogradov--Korobov contour saving in (15) is only `exp(-O(1))`: indeed

\[
\frac{X_a}
{Q_{\rm Ford}^{2/3}(\log Q_{\rm Ford})^{1/3}}
\asymp1.
\tag{29}
\]

It therefore cannot absorb the polynomial prefactor `Q^2`. Even making the harmonic plateau longer does not repair this within the same inequality, because the off-diagonal contribution in (14) is already proportional to `H` on both the lower and upper sides. The live improvement target is no longer epsilon-uniformity. It is to reduce the actual prime-correlation off-diagonal at heights where the zero-free contour itself supplies only constant exponential saving.

This makes the unused structure noted in `NB-210` more sharply relevant: all the large values occur at the arithmetic progression `t,2t,...` and are phase-pinned near `+1`, while (11) consumes only their squared moduli and treats a general well-spaced set. Any route to the Ford edge through correlated primes must exploit information of that kind, or obtain a genuinely stronger prime-correlation kernel than the present zero-free-contour estimate.

## 5. Adversarial checks

**The Bellotti region controls zeros, not `zeta'/zeta` by itself.** Equation (9) is not imported from the zero-free statement. It follows from the same local logarithmic-derivative formula explicitly used in Matomaki--Radziwill's proof, together with `O(L_T)` zeros per unit-height window and the horizontal separation supplied by the zero-free contour. The resulting `L_T R_T` bound is smaller than the retained coarse `L_T^2` factor.

**The contour sees imaginary parts up to a constant multiple of `T`.** In (4), the Mellin ordinate and the difference `tau` combine. Defining `L_T` with `10T` and choosing the contour from the minimum zero-free width on that enlarged range absorbs this without changing any asymptotic exponent.

**No moving epsilon is hidden in the proof.** All constants in (1), (10), and (11) are fixed after choosing one safe fraction of the Vinogradov--Korobov zero-free width. The diagonal parameter is `T`, not an epsilon inserted into a theorem whose implied constant then changes.

**The fixed harmonic depth is deliberate.** Only a fixed `H_0` is used after (14). Therefore no growth of the number of sample ordinates, no extra spacing issue, and no hidden dependence of the Halasz constant on a moving harmonic budget enters (2).

**The log-squared frontier is a method boundary, not a first-return theorem.** Failure of condition (24) says only that this refined prime-Halasz proof stops certifying a constant gap. It does not construct a positive Euler return beyond that height and does not weaken the farther `Omega(1/X_a)` Ford exclusion already proved in `NB-205`.

**Positivity remains load-bearing.** The transfer (13) starts from the positive `ell^1` Euler-shell defect. Signed or complex source combinations can cancel before individual prime phases become nearly aligned, so (2) does not address that branch.

**This remains source acquisition, not Nyman distance.** Nothing here proves that a near-optimal Nyman--Beurling approximant must realize the positive return measured by `mathcal A_a(t)`. The destination bridge remains a separate theorem requirement.

## 6. Prior art and novelty boundary

The two load-bearing literature ingredients are already anchored in `SOURCES.md`:

- Kaisa Matomaki and Maksym Radziwill, *Multiplicative functions in short intervals*, Annals of Mathematics 183 (2016), Lemma 11 and its proof. The proof explicitly writes the prime-power correlation kernel through `-zeta'/zeta`, shifts a zero-free contour, and obtains the published fixed-epsilon off-diagonal factor.
- Chiara Bellotti, *Explicit bounds for the Riemann zeta function and a new zero-free region*, J. Math. Anal. Appl. 536 (2024), 128249. Its explicit Vinogradov--Korobov region has width of order `1/((log T)^(2/3)(log log T)^(1/3))`. The classical Vinogradov--Korobov region of the same shape would also suffice here; the explicit constant is not used.

A targeted search checked later short-interval and prime-supported Halasz literature and did not locate this exact diagonal Nyman/Euler consequence. That absence is not treated as a novelty claim. The epsilon-free inequality (11) should itself be regarded as a routine sharpening of the published proof once the full zero-free width is retained, not as a new general theorem of independent priority.

The project-local delta is the coupled consequence: the prime harmonic plateau from `NB-208` plus the proof-level Vinogradov--Korobov refinement of `NB-210` yields an **order-one** positive Euler gap through the moving height

\[
\log|t|
\asymp
\frac{X_a^{3/2}}{(\log X_a)^2},
\]

and identifies the polynomial prime-kernel prefactor, rather than fixed-epsilon quantifiers or sparse-prime density, as the next obstruction on this route.

## 7. Consequence for the research frontier

The positive-source branch should no longer treat `NB-210`'s fixed `delta` as the natural endpoint of prime-Halasz amplification. The same mechanism has a uniform diagonal corridor at `X_a^(3/2)/(log X_a)^2`. The remaining gap to `NB-205` is now quantitative and sharply localized:

\[
\boxed{
\text{constant-gap prime correlation: }
\frac{X_a^{3/2}}{(\log X_a)^2}
\quad\text{vs.}\quad
\text{Ford }o(1/X_a)\text{ exclusion: }
\frac{X_a^{3/2}}{\sqrt{\log X_a}}.
}
\]

The next responsive test is therefore to exploit the **phase-pinned arithmetic progression** of prime values, or another prime-specific correlation estimate, to remove part of the `(log X_a)^(3/2)` height gap. Merely invoking a sharper fixed-epsilon large-value theorem, increasing the number of harmonics, or improving prime density on the fixed shell does not address the boundary isolated here.

The two larger structural frontiers remain unchanged: signed/complex synthesis is not controlled by the positive return argument, and the destination-coupled theorem connecting successful Nyman approximation to the relevant Euler acquisition condition is still missing.