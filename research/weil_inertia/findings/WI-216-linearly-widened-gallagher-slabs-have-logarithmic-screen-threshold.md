# WI-216 — linearly widened Gallagher slabs have a logarithmic screen-complexity threshold

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY + CLASSICAL-IDENTITY + LITERATURE-CONTEXT`.

WI-214 shows that a growing polylogarithmic family of off-line functional-equation pairs can flatten the two **fixed** natural reciprocal slabs around `t=1,2`, while WI-215 proves that every **fixed** finite screen fails on even one fixed natural slab. The missing regime is when the observation window grows together with the screen complexity.

That regime has an exact threshold at logarithmic complexity. Let

\[
L=\log T,
\qquad
M=T^{\vartheta+o(1)},\quad \vartheta>0,
\]

and fix one reciprocal harmonic `k` and the WI-209--WI-215 bow parameter `h>0`. Suppose a selected screen has at most `n=n(T)` independent complex exponential channels in the unfolded natural coordinate `u`. Then:

> **Lower bound.** If `n=O(L)` along a sequence, there is a slab of width `O(n/M)` around `t=k` on which the selected bow-plus-screen Gallagher energy is at least a constant multiple of
> \[
> \frac{L}{n+1}
> \]
> times the **full raw-prime Gallagher diagonal** at the matching short length. Consequently a screen whose selected residue is `o` of that global diagonal on its own linearly widened slab must satisfy
> \[
> \boxed{\frac{n(T)}{\log T}\longrightarrow\infty.}
> \]
>
> **Matching upper construction.** The conjugation-closed WI-214 midpoint screen extends from fixed `u`-windows to `|u|\le J/4`. On both reciprocal harmonics its normalized residual is `O_h(J^{-1})` uniformly on that growing window. Hence its selected Gallagher energy on the whole linearly widened slab is
> \[
> O_h\!\left(\frac{L}{J}\right)
> \]
> times the global raw-prime diagonal. Taking any even subpolynomial `J` with `J/L\to\infty` makes both slabs subdiagonal, while still using only `4J` functional-equation pairs and `8J` exponential channels.

Thus the transition scale is genuinely logarithmic: `O(log T)` channel complexity cannot make a linearly widened natural slab subdiagonal, whereas `omega(log T)` complexity is sufficient inside the existing WI-214 structural countermodel. This is a complexity statement about the selected bow-plus-screen source residue, not an impossibility theorem for actual zeta zeros or for the full explicit formula.

## 1. Integer translates give an `n`-uniform frame lower bound

Retain the WI-215 normalized bow profile

\[
f_{M,k}(u)
=\frac1M B_M\!\left(k+\frac{u}{M}\right),
\]

so on fixed compact sets

\[
f_{M,k}(u)\to f_k(u)
:=C_k\frac{\sin(\pi u)}{\pi u},
\qquad C_k:=2\cosh(hk).
\tag{1}
\]

Use the unit box operator

\[
(K_1r)(s):=\int_s^{s+1}r(v)\,dv,
\qquad F_k:=K_1f_k.
\tag{2}
\]

The classical Fourier identity

\[
\frac{\sin(\pi u)}{\pi u}
=\int_{-1/2}^{1/2}e^{2\pi i\xi u}\,d\xi
\tag{3}
\]

gives

\[
F_k(s)
=C_k\int_{-1/2}^{1/2}
 e^{2\pi i\xi s}m(\xi)\,d\xi,
\qquad
m(\xi):=\int_0^1e^{2\pi i\xi v}\,dv.
\tag{4}
\]

For `|xi|<=1/2`,

\[
|m(\xi)|
=\left|\frac{\sin(\pi\xi)}{\pi\xi}\right|
\ge\frac2\pi.
\tag{5}
\]

Therefore, for every vector `a=(a_0,...,a_n)` with `sum |a_j|^2=1`, Plancherel and orthogonality of the integer Fourier modes on `[-1/2,1/2]` give the **uniform-in-`n`** bound

\[
\begin{aligned}
\left\|\sum_{j=0}^na_jF_k(\cdot+j)\right\|_{L^2(\mathbb R)}^2
&=C_k^2\int_{-1/2}^{1/2}
|m(\xi)|^2
\left|\sum_{j=0}^na_je^{2\pi i j\xi}\right|^2d\xi\\
&\ge
\boxed{\frac{4C_k^2}{\pi^2}}.
\end{aligned}
\tag{6}
\]

This is the quantitative replacement for WI-215's fixed-`n` positive Gram eigenvalue `mu_n`: using integer translates avoids any deterioration of the global lower frame bound as `n` grows.

## 2. Only an `O(n)` slab is needed

The price for the uniform frame bound is that the observation slab must grow with the number of translates. The box-integrated sinc has the elementary tail estimate

\[
\int_{|s|>R}|F_k(s)|^2ds
\le\frac{3C_k^2}{\pi^2R},
\qquad R\ge2.
\tag{7}
\]

Indeed, for `s>=R`, equation (2) and `|sinc(v)|<=1/(pi|v|)` give `|F_k(s)|<=C_k/(pi s)`; for `s<=-R`, the same argument gives `|F_k(s)|<=C_k/(pi(|s|-1))`.

Put

\[
R_n:=4(n+1),
\qquad
I_n:=[-R_n-n,R_n].
\tag{8}
\]

Outside `I_n`, every shifted argument `s+j`, `0<=j<=n`, lies outside `[-R_n,R_n]`. Hence pointwise Cauchy--Schwarz and (7) imply

\[
\int_{\mathbb R\setminus I_n}
\left|\sum_{j=0}^na_jF_k(s+j)\right|^2ds
\le
(n+1)\frac{3C_k^2}{\pi^2R_n}
=\frac{3C_k^2}{4\pi^2}.
\tag{9}
\]

Combining (6) and (9),

\[
\boxed{
\left\|\sum_{j=0}^na_jF_k(\cdot+j)\right\|_{L^2(I_n)}^2
\ge\frac{13C_k^2}{4\pi^2}.
}
\tag{10}
\]

Thus the target retains a fixed amount of translated energy on a window whose length is only `O(n)`.

## 3. Every `n`-channel screen has an exact translating null vector

Let the normalized selected screen be the fully enlarged WI-215 class

\[
g_M(u)=\sum_{\ell=1}^n c_{\ell,M}e^{z_{\ell,M}u},
\tag{11}
\]

with arbitrary complex coefficients and exponents depending on `M`. This class contains every screen built from at most `N` off-line functional-equation pairs after taking `n<=2N`; allowing arbitrary channels only strengthens the lower-bound statement.

Write

\[
\eta_M:=\frac{L}{2dM},
\]

and define exactly as in WI-215

\[
H_M(s)
:=K_1\!\left[e^{\eta_M\cdot}
(f_{M,k}+g_M)\right](s).
\tag{12}
\]

Multiplication by `e^{eta_Mu}` and application of `K_1` preserve the at-most-`n` exponential-channel property of the screen. Therefore its `n+1` integer translates have an exact linear dependence: there is an `a=a^{(M)}` with `sum |a_j|^2=1` such that

\[
\sum_{j=0}^na_j
K_1[e^{\eta_M\cdot}g_M](s+j)=0
\tag{13}
\]

identically in `s`.

For the threshold claim it is enough to consider a subsequence with `n<=CL` for some fixed `C`. On all arguments used in (8)--(13), `|u|=O_C(L)`, and the exact bow formula gives uniformly

\[
e^{\eta_Mu}f_{M,k}(u)
=f_k(u)+O_{h,k,C}\!\left(\frac{L^2}{M}\right).
\tag{14}
\]

After one box integration, summing `n+1` translates with `||a||_1<=sqrt(n+1)`, and taking the `L^2(I_n)` norm, the total perturbation from (14) is `o(1)` because `M=T^{\vartheta+o(1)}` dominates every fixed power of `L`. Thus (10) yields, for all sufficiently large `T` on the subsequence,

\[
\left\|
\sum_{j=0}^na_jH_M(\cdot+j)
\right\|_{L^2(I_n)}^2
\ge\frac{C_k^2}{\pi^2}.
\tag{15}
\]

Let

\[
J_n:=[-5(n+1),5(n+1)].
\tag{16}
\]

Every `I_n+j` lies in `J_n`. Applying Cauchy--Schwarz in the translate index to the left side of (15) gives

\[
\frac{C_k^2}{\pi^2}
\le
(n+1)\int_{J_n}|H_M(s)|^2ds,
\]

hence the quantitative screen obstruction

\[
\boxed{
\int_{J_n}|H_M(s)|^2ds
\ge
\frac{C_k^2}{\pi^2(n+1)}.
}
\tag{17}
\]

No separation, bounded radial depth, coefficient bound, phase regularity, or nonconfluence assumption is used.

## 4. Gallagher conversion forces superlogarithmic complexity

WI-215 gives the exact physical identity

\[
Q_M(s)
=-X_k^{1/2}\frac{L}{d}H_M(s),
\qquad
X_k:=T^{k/d},
\tag{18}
\]

and

\[
\frac{dx_{k,M}(s)}{ds}
=X_ke^{sL/(dM)}\frac{L}{dM}.
\tag{19}
\]

When `n<=CL`, equation (16) has `|s|=O(L)`, so the exponential factor in (19) is `1+o(1)`. Equations (17)--(19) therefore give selected physical residue energy

\[
\int_{x(J_n)}|Q_M(x)|^2dx
\ge
\left(\frac{C_k^2}{\pi^2(n+1)}+o\!\left(\frac1{n+1}\right)\right)
\frac{X_k^2L^3}{d^3M}.
\tag{20}
\]

For unit box length, the **full** raw-prime Gallagher diagonal at the matching physical short length is the WI-215 scale

\[
X_kK_k\log X_k
\sim
k\frac{X_k^2L^2}{d^2M}.
\tag{21}
\]

Consequently

\[
\boxed{
\frac{
\int_{x(J_n)}|Q_M(x)|^2dx
}{X_kK_k\log X_k}
\ge
\left(
\frac{C_k^2}{\pi^2kd}+o(1)
\right)
\frac{L}{n+1}.
}
\tag{22}
\]

This compares the selected energy on only an `O(n/M)` neighborhood of one reciprocal harmonic against the **entire** raw-prime diagonal, exactly as in WI-213--WI-215. The global diagonal is not multiplied by the slab width.

If `n=o(L)`, the selected residue is still superdiagonal by a diverging factor. More strongly, if `n/L` stays bounded along any subsequence, (22) stays bounded away from zero there. Hence

\[
\boxed{
\text{subdiagonal on the linearly widened slab}
\quad\Longrightarrow\quad
\frac{n(T)}{\log T}\to\infty.
}
\tag{23}
\]

Since an off-line functional-equation pair contributes at most two complex exponential channels, the same implication holds for the number `N(T)` of such pairs:

\[
\boxed{
N(T)/\log T\to\infty.
}
\tag{24}
\]

This is much stronger than the qualitative `n(T)->infty` conclusion of WI-215, but it deliberately asks the observation window to widen proportionally to the screen complexity.

## 5. The WI-214 screen reaches the same logarithmic scale from above

The lower bound is order-sharp inside the existing countermodel. Let `J` be the even WI-214 midpoint-packet size and retain its corrected conjugation-closed lift symmetry

\[
n_{J+1-j,M}=-n_{j,M}-1.
\]

Its ideal packet is

\[
A_J(u)
=\frac{\sin(\pi u)}{J\sin(\pi u/J)}.
\tag{25}
\]

The fixed-window estimate used in WI-214 extends directly to a window linear in `J`. For `|u|<=J/4`, put `x=pi u/J`. Since `1/sin x-1/x` is bounded on `[-pi/4,pi/4]` after removing the origin,

\[
\boxed{
\left|A_J(u)-\frac{\sin(\pi u)}{\pi u}\right|
\ll\frac1J.
}
\tag{26}
\]

The same elementary sine lower bound gives

\[
\boxed{|uA_J(u)|\ll1}
\qquad (|u|\le J/4).
\tag{27}
\]

The paired integer lifts differ from their midpoint frequencies by at most `1/M`, so replacing the ideal packet costs `O(J/M)` uniformly on this widened window. The radial factors in WI-214 vary by only

\[
1+O_h(J\log M/M),
\tag{28}
\]

and these errors are `o(J^{-1})` whenever `J=T^{o(1)}` because then `J^2\log M/M->0`.

Equations (26)--(28) control the main cancellation layers. The only potentially larger cross-layer term is WI-214's first-layer leakage into the second harmonic. Its leading form is proportional to

\[
\frac{u}{J}A_J(u),
\]

which is `O(J^{-1})` by (27); the exact phase-filter remainder is smaller under the same subpolynomial hypothesis. The second-layer leakage into the first harmonic remains smaller still. Therefore the repaired WI-214 screen satisfies simultaneously

\[
\boxed{
\sup_{|u|\le J/4}
\frac{|R_{M,J}(k+u/M)|}{M}
\ll_h\frac1J,
\qquad k=1,2.
}
\tag{29}
\]

After the unit box integration, the normalized `H_M` energy over either widened slab is therefore `O_h(J^{-1})`. Using the same exact physical Jacobian as (18)--(21),

\[
\boxed{
\frac{
\int_{|u|\le J/4+O(1)}|Q_{k,M}|^2
}{X_kK_k\log X_k}
\ll_{h,d,k}
\frac{L}{J}.
}
\tag{30}
\]

Thus every even choice satisfying

\[
J=T^{o(1)},
\qquad
\frac{J}{L}\to\infty
\tag{31}
\]

makes **both** linearly widened reciprocal slabs subdiagonal. The screen still costs only `4J=o(M)` functional-equation pairs, and under the WI-214 strip condition `d\vartheta<1/2` all of them remain inside the critical strip. Its effective exponential-channel count is at most `8J`.

Equations (23) and (30) therefore match at the logarithmic scale: the selected-source problem has no room for a sublogarithmic or merely bounded-multiple-of-log screen on a slab whose normalized width is proportional to its own channel budget, while a superlogarithmic screen can achieve subdiagonal energy in the explicit two-harmonic countermodel.

## 6. What this changes and what it does not

The result prices one of the quantities left explicitly open by WI-214 and WI-215. Merely saying that the screen complexity must diverge was too weak: a continuum bootstrap that observes a window growing with the proposed screen now forces a **quantitative logarithmic complexity charge**. This separates three scales that must not be conflated:

\[
\text{zero-count cost }N(T),
\qquad
\text{effective exponential complexity }n(T),
\qquad
\text{observation width in }u.
\]

The logarithmic charge is nevertheless far below the bow population `M=T^{\vartheta+o(1)}`. Even `N(T)=L\ell(T)` with `ell(T)->infty` costs zero asymptotic density, so (23)--(24) do **not** give a defect-to-zero theorem by themselves. They say instead that any such bootstrap must either keep widening the independent source observations faster than the screen can cheaply grow, prove a zeta-specific restriction on superlogarithmic off-line packets, or control the full signed source error so that complementary terms cannot cancel the selected residue.

The result also does not contradict WI-214. Its displayed choice `J=L^{2/3+o(1)}` was designed to flatten two **fixed** slabs, where the Gallagher ratio is `O(L/J^2)` at the weaker second harmonic. A slab whose width itself grows like `J` collects `J` times as much normalized residual energy, changing the relevant scale to `O(L/J)` and moving the transition from `sqrt L` to `L`. WI-216 is precisely this observation-complexity tradeoff.

Finally, (22) is still a selected-residue statement. Actual zeta must satisfy the full explicit formula, where complementary zeros, pole/trivial terms, contour terms and structured prime-side contributions may cancel the selected bow-plus-screen vector. As in WI-195, WI-209 and WI-215, excluding that cancellation requires an independent source-fixed upper bound; none is inferred here.

## 7. Prior art and novelty audit

All harmonic-analysis ingredients are classical. Anselone--Korevaar's finite-dimensional translation theory, already recorded for WI-215, explains why finite exponential packets have finite translation rank. Ron and Shen, *Frames and Stable Bases for Shift-Invariant Subspaces of L2(R^d)*, Canadian Journal of Mathematics 47 (1995), 1051--1094, DOI `10.4153/CJM-1995-056-1`, gives the general Fourier-fiber framework for stable translate systems. In the present one-generator sinc case, however, the needed lower frame estimate is exactly the one-line Parseval calculation (3)--(6); no black-box frame theorem is required.

On the approximation side, Kircheis--Potts--Tasche, *Nonuniform fast Fourier transforms with nonequispaced spatial and frequency data and fast sinc transforms*, Numerical Algorithms 92 (2023), 2307--2339, DOI `10.1007/s11075-022-01389-6`, records finite positive exponential approximation of sinc. WI-214 already uses the simpler exact midpoint geometric sum. Equations (26)--(29) are its elementary extension from fixed compact windows to windows of length proportional to the packet size.

A targeted search around shift-invariant/Riesz translate bounds, sinc exponential approximation, Gallagher short-interval norms, off-critical zeta screening and recent pair-correlation/simple-critical-zero work found the classical translate and approximation frameworks but no published theorem coupling them to the WI-209--WI-215 bow normalization or producing the `log T` screen-complexity threshold (23)--(31). Absence from that search is not used as a priority claim. The mathematical delta recorded here is the exact zeta-source/Gallagher scaling consequence and the matched lower/upper complexity boundary, not the underlying Parseval or sinc identities.

## 8. Audit and falsification boundary

The lower bound can be falsified by exhibiting an `n=O(log T)` exponential-channel screen for which the exact WI-215 `H_M` residue on `J_n` violates (17); because (6), the tail estimate (7), and the exact translation dependence (13) are independent, such a counterexample would have to expose an error in the finite-`M` passage (14) or the source dictionary (18)--(21).

The upper half can be falsified by showing that one of the repaired WI-214 layers ceases to satisfy `O(J^{-1})` on `|u|<=J/4`. The decisive checks are the midpoint identities (26)--(27), the one-unit lift error, and the first-layer leakage proportional to `(u/J)A_J(u)`. Strip and count admissibility remain exactly the WI-214 conditions.

No unconditional simple-critical-zero proportion changes in this finding. Its contribution is a sharp structural boundary on one candidate defect-to-zero mechanism: **linearly widening continuum observations turn the qualitative finite-rank obstruction into a logarithmic complexity tariff, but that tariff is still asymptotically negligible compared with the available zero count.**