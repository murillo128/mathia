# WI-227 — shallow screens localize at the radial-depth scale

**Status:** `EXACT-DERIVED + STRUCTURAL-RIGIDITY + BOOTSTRAP-CANDIDATE + CLASSICAL-IDENTITY + LITERATURE-CONTEXT`.

WI-224--WI-225 show that a scalar compact detector which pays for every remote dyadic zero from one **global** radial-mass budget has optimal natural-frequency cutoff `Theta(log T)`, hence physical localization radius `Theta(M)`. That leaves a logarithmic gap to the actual bow scale `M/log T`. The gap is not intrinsic once the screen is separated by horizontal depth before paying for its remote tail.

In the inherited WI-218--WI-225 dyadic-screen model, fix an interior reciprocal harmonic `0<k<d`, let

\[
M=T^{\vartheta+o(1)},\qquad \vartheta>0,\qquad L=\log T,
\]

and let `a_rho` be the normalized radial parameter of a functional-equation mirror pair. For any threshold `A=A(T)` in the critical-strip range, split the screen into

\[
\mathcal S_{\le A}:=\{\rho:a_\rho\le A\},
\qquad
\mathcal S_{>A}:=\{\rho:a_\rho>A\}.
\]

There are constants `c,C>0`, depending only on the fixed screen/detector parameters and not on `T` or `A`, such that every dyadic zero screen satisfying the inherited local cancellation hypothesis obeys the following dichotomy for all sufficiently large `T`:

\[
\boxed{
\sum_{\rho\in\mathcal S_{>A}}
\mu_\rho\cosh(k a_\rho)\ge cM
}
\tag{1}
\]

or

\[
\boxed{
\sum_{\substack{\rho\in\mathcal S_{\le A}\\
|\gamma_\rho-\gamma_0|\le C(A+1)M/L}}
\mu_\rho\cosh(k a_\rho)\ge cM.
}
\tag{2}
\]

Thus a screen whose radial depth is uniformly bounded is forced back to the **original physical bow scale** `O(M/log T)`, not merely WI-224's `O(M)` scale. More generally, if all screening mass has `a=o(log T)`, order-`M` radial-weighted source is forced into physical radius `o(M)`. Conversely, a screen which avoids every such sub-`M` localization must pay order-`M` radial-weighted mass at successively larger horizontal depth.

This does not prove RH or improve the simple-critical proportion. It supplies a new depth-versus-localization alternative of exactly the type left open after WI-225. The finite-harmonic sparse screens of WI-212 are consistent with it: their screening pairs have `a=log M+O(1)=vartheta log T+o(log T)`, so they escape the shallow branch by paying macroscopic radial depth.

## 1. Inherited screen model and target pairing

Use the notation of WI-224. At one fixed reciprocal harmonic,

\[
F_M:=K_{\eta_M}f_{M,k},
\qquad
\eta_M=\frac{L}{2dM}=o(1),
\]

and assume a dyadic screen assembled from functional-equation mirror pairs satisfies on one fixed compact interval `J`

\[
\|F_M+K_{\eta_M}g_M\|_{L^2(J)}=o(1).
\tag{3}
\]

The limiting target `F` is continuous and nonzero. Choose, exactly as in WI-224, a fixed subinterval `J_0 compactly contained in J` on which `F` has constant sign and `|F|>=c_0>0`, a fixed smooth nonnegative probability density `chi_0`, and a fixed support margin `delta>0`. For every integer `n>=2`, define

\[
b_n=\delta/n,
\qquad
h_{b_n}=b_n^{-1}{\bf 1}_{[-b_n/2,b_n/2]},
\qquad
\psi_n=h_{b_n}^{*n},
\qquad
\phi_n=\chi_0*\psi_n.
\tag{4}
\]

The entire family is supported in `J_0`, has unit mass, and is uniformly conditioned:

\[
\phi_n\ge0,
\qquad
\int\phi_n=1,
\qquad
\sup_n\|\phi_n\|_2<\infty.
\tag{5}
\]

Since `F_M->F` uniformly on `J_0`, positivity and (5) give a constant `c_1>0` such that, uniformly in `n`,

\[
|\langle\phi_n,F_M\rangle|\ge c_1
\tag{6}
\]

for all sufficiently large `T`. Pairing (3) against `phi_n` therefore yields

\[
\boxed{
|\langle\phi_n,K_{\eta_M}g_M\rangle|\ge c_1/2
}
\tag{7}
\]

for every choice `n=n(T)`. The uniform `L^2` bound is what makes a growing detector order legal despite the unspecified `o(1)` rate in (3).

For one mirror pair, WI-221--WI-224 give two exponential channels with

\[
|c_+|=\frac{\mu e^{ka}}M,
\qquad
|c_-|=\frac{\mu e^{-ka}}M,
\qquad
|\alpha_\pm|=\frac aM,
\qquad
|\xi_\pm|=\frac{|\nu|}{M},
\tag{8}
\]

and

\[
\nu=\frac{(\gamma-\gamma_0)L}{2\pi d}.
\tag{9}
\]

Hence the coefficient `l^1` contribution of one pair is exactly

\[
|c_+|+|c_-|=\frac{2\mu\cosh(ka)}M.
\tag{10}
\]

Throughout the zeta critical strip `a=O(L)`, while `M` is a fixed positive power of `T` up to `T^{o(1)}`. Thus `|alpha_\pm|=o(1)` uniformly over the full dyadic screen.

## 2. Unit natural-frequency shells contain only `O(M)` zero labels

The improvement over WI-224 comes from not multiplying one stopband supremum by the global `N_T/M` source budget. Instead partition the shallow screen into unit shells in the natural frequency `xi=nu/M`.

By (9), one unit interval in `xi` corresponds to an ordinate interval of length

\[
\Delta\gamma=\frac{2\pi dM}{L}.
\tag{11}
\]

The classical Riemann--von Mangoldt formula

\[
N(t)=\frac{t}{2\pi}\log\frac{t}{2\pi}-\frac{t}{2\pi}+O(\log t)
\tag{12}
\]

implies uniformly for `t asymp T` that an interval of length `Delta gamma` contains

\[
O(\Delta\gamma\,L+L)=O(M)
\tag{13}
\]

zero labels counted with multiplicity. Here `M=T^{vartheta+o(1)}` with fixed `vartheta>0`, so `L=o(M)`. Intersecting a shell with the dyadic range can only reduce this count.

For the shallow part `a<=A`, (10) and (13) therefore give, uniformly for every unit natural-frequency shell,

\[
\boxed{
\sum_{\rho\ \mathrm{in\ one\ shell},\ a_\rho\le A}
(|c_\rho^+|+|c_\rho^-|)
\ll_d \cosh(kA).
}
\tag{14}
\]

This is the source-aware replacement for the global factor `N_T/M=T^{1-vartheta+o(1)}` used in WI-224. It is the only new zeta-specific ingredient in the argument.

## 3. The spline detector has a summable far-shell envelope

Let

\[
\Phi_n(z):=\int\phi_n(u)e^{zu}\,du.
\]

WI-224 gives the exact factorization

\[
\Phi_n(z)
=X_0(z)
\left(
\frac{\sinh(z\delta/(2n))}{z\delta/(2n)}
\right)^n,
\tag{15}
\]

where `X_0` is the Fourier--Laplace transform of the fixed smooth core. On `|Re z|<=1`, `|X_0(z)|` is uniformly bounded. Write

\[
z=\alpha+2\pi i\xi,
\qquad
x=\frac{\alpha\delta}{2n},
\qquad
y=\frac{\pi\xi\delta}{n}.
\]

Using

\[
|\sinh(x+iy)|^2=\sinh^2x+\sin^2y
\]

and `|alpha|<=1`, there is a fixed constant `B_0>=1` such that for every `n>=2` and every `|xi|>= B_0 n`,

\[
\boxed{
|\Phi_n(\alpha+2\pi i\xi)|
\le C_0\left(\frac{B_0n}{2|\xi|}\right)^n.
}
\tag{16}
\]

Indeed the numerator in the sinc factor is uniformly bounded on the strip, while its denominator is at least a fixed multiple of `|xi|/n`; enlarging `B_0` makes the ratio at `|xi|=B_0n` at most `1/2`.

The Gallagher box is harmless here. If

\[
q_\eta(z)=\int_0^1e^{(\eta+z)v}\,dv,
\]

then `K_eta(e^{z\cdot})=q_eta(z)e^{z\cdot}` and `|q_eta(z)|<=e^2` once `|eta|,|Re z|<=1`. Thus (16) also bounds the full detector pairing with one screen channel up to a fixed constant.

Sum (16) over the unit shells `j<=|xi|<j+1`, `j>=B_0n`. From (14),

\[
\begin{aligned}
|\langle\phi_n,K_{\eta_M}g_{\le A,\mathrm{far}}\rangle|
&\ll
\cosh(kA)
\sum_{j\ge B_0n}
\left(\frac{B_0n}{2j}\right)^n\\
&\ll
\cosh(kA)\,2^{-n}.
\end{aligned}
\tag{17}
\]

The last bound is elementary: compare `sum j^{-n}` with its tail integral; because the lower endpoint is proportional to `n`, the apparent factor from the number of shells is absorbed uniformly for `n>=2`.

Choose now

\[
\boxed{
n=\lceil C_1(A+1)\rceil}
\tag{18}
\]

with one fixed `C_1` sufficiently large. Since `cosh(kA)<=e^{kA}`, equations (17)--(18) make the entire far shallow contribution at most `c_1/8`, uniformly in `A` and large `T`.

This is the key difference from WI-225. Logvinenko--Sereda forbids a normalized fixed-support detector from having a uniformly smaller stopband than `exp(-C R)`, and consequently forces `R=Omega(log T)` when that stopband is multiplied by the **global** polynomial mass `N_T/M`. Here no such global multiplication occurs: Riemann--von Mangoldt gives only `O(M)` labels per natural-frequency shell, and the full summable sinc-power tail is retained instead of being replaced by one stopband supremum. The relevant cost is `exp(O(A))`, so detector order `O(A+1)` suffices.

## 4. Pairing the remaining two pieces gives the depth--localization dichotomy

Let

\[
R_A:=B_0n=O(A+1)
\tag{19}
\]

and decompose the screen pairing in (7) into

\[
g_M
=g_{\le A,\mathrm{near}}
+g_{\le A,\mathrm{far}}
+g_{>A},
\]

where `near` means `|xi|<R_A`. By (7) and (17),

\[
|\langle\phi_n,K_{\eta_M}
(g_{\le A,\mathrm{near}}+g_{>A})\rangle|
\ge 3c_1/8.
\tag{20}
\]

Hence at least one of the two remaining pieces has detector pairing bounded below by a fixed positive constant.

For every channel in the full critical strip, `|Re z|=o(1)`. Since `phi_n` is a probability density on one fixed compact interval and the Gallagher multiplier is uniformly bounded,

\[
|\langle\phi_n,K_{\eta_M}e^{z\cdot}\rangle|\le C_2
\tag{21}
\]

with `C_2` independent of `n,T,A,z`. Combining (10), (20), and (21), a fixed lower bound for the deep pairing forces

\[
\sum_{a_\rho>A}\mu_\rho\cosh(ka_\rho)\gg M,
\tag{22}
\]

which is (1). A fixed lower bound for the near shallow pairing instead forces

\[
\sum_{\substack{a_\rho\le A\\ |\xi_\rho|<R_A}}
\mu_\rho\cosh(ka_\rho)\gg M.
\tag{23}
\]

Finally (9) and (19) give

\[
|\gamma_\rho-\gamma_0|
<\frac{2\pi dM}{L}R_A
\le C(A+1)\frac{M}{L},
\tag{24}
\]

which is (2).

No Jutila global zero-density estimate is needed for (1)--(2). The argument uses only the inherited exact screen dictionary, the uniformly conditioned spline family already constructed in WI-224, and the classical local zero-count consequence of Riemann--von Mangoldt.

## 5. Consequences for the bow obstruction

The most useful specialization is bounded radial depth. If every screening pair has

\[
a_\rho\le A_0=O(1),
\]

then the first alternative is empty, `cosh(ka)` is uniformly bounded, and (2) gives not merely weighted mass but

\[
\boxed{
\#\{\text{screen zero labels within }O(M/L)\text{ of }\gamma_0\}
\gg M.
}
\tag{25}
\]

Thus bounded-depth screening is forced back to the same **order of vertical scale** as the original Maynard--Pratt bow. This is precisely the scale at which ordinary Riemann--von Mangoldt count budgets and the reciprocal-harmonic Fejer obstruction of WI-210 can potentially interact without the logarithmic capacity loss recorded in WI-224.

More generally, if `A_T=o(L)` and the screen has no order-`M` radial-weighted mass beyond depth `A_T`, then (2) localizes order-`M` source to

\[
\boxed{
o(M)}
\tag{26}
\]

physical ordinate radius. This strictly beats the `Theta(M)` scalar/global-mass frontier of WI-224--WI-225 because it adds source information that their minimax statement deliberately discards.

The opposite branch is also structurally useful. If a screen avoids localization at the radius associated with some threshold `A`, it must carry order-`M` radial weight at depth greater than `A`. Repeating the statement for an increasing family of thresholds produces a **depth-escalation ledger**. It is not yet an iteration theorem: (22) is weighted source mass, not raw distinct-zero count, and the same deep pairs may witness several thresholds. A future bootstrap must show that the deep alternative itself consumes an incompatible zero-density/source budget or creates a new coherent defect that cannot be recycled indefinitely.

WI-212 gives the correct stress test. Its exact sparse finite-harmonic completion uses only `O_d(1)` additional off-line pairs, but their radial depth is

\[
a=\log M+O(1)=\vartheta L+o(L).
\tag{27}
\]

For every threshold `A=o(L)`, those pairs land in the deep branch (1), with individual weights large enough to carry order-`M` source. Therefore (1)--(2) do not contradict the known algebraic countermodel; they identify exactly the currency it spends to evade local count.

## 6. Evidence boundary and prior-art audit

The ingredients are separated by provenance.

- **Classical identity:** Riemann--von Mangoldt gives the deterministic `O(M)` zero-label bound in every unit natural-frequency shell through (11)--(13).
- **Existing Mathia construction:** WI-224 supplies the uniformly `L^2`-conditioned compact spline family and its exact Fourier--Laplace factorization (15); WI-225 supplies the Logvinenko--Sereda barrier for the different global-stopband architecture.
- **New exact deduction here:** paying shallow source shell by shell, summing the full spline tail, choosing detector order proportional to radial depth, and obtaining the dichotomy (1)--(2).
- **Stress-test prior art inside the line:** WI-212's sparse deep self-reciprocal screens show why a radial-depth alternative is necessary and why finite reciprocal moments alone cannot replace it.

A bounded external audit around local Riemann--von Mangoldt zero counts, compact Fourier/B-spline detectors, zero-density localization, Logvinenko--Sereda, and explicit-formula zero contributions found the expected classical ingredients and neighboring uses of local zero counts to control zero contributions, but no source stating this radial-depth/shellwise screening dichotomy for the Montgomery/Weil-inertia bow problem. Absence of such a hit is not used as a priority claim.

The theorem is conditional only on the **inherited dyadic-screen model** (3), not on RH. It does not show that the full complementary term in the source-fixed explicit formula is a dyadic zero screen: non-dyadic zero ranges, the structured `Lambda^sharp` component, pole/trivial terms, and any contour remainder must still be kept in the source ledger before the accepted distinguished-twist clue can be resolved. It also does not turn (22) into positive-density distinct off-line zeros, because radial weights can be large.

## Research consequence

The scalar-localization problem should no longer be summarized simply as a hard `Theta(M)` physical floor. That floor is sharp only when remote zeros are paid through one global total-mass supremum. Once the actual zeta source is stratified by vertical shell and horizontal depth, a screen capped at depth `A` localizes at physical scale

\[
\boxed{O((A+1)M/\log T)}.
\]

The next useful step is therefore not another scalar-window optimization. It is to combine this depth-localization alternative with a **local radial-depth budget**: either sharpen WI-210's count/moment obstruction on the resulting `O((A+1)M/log T)` neighborhood, or prove that order-`M` source at progressively larger `a` violates zero-density, multiplicity, or source-covariance constraints. Such a theorem would turn the present depth-escalation ledger into the defect-to-zero bootstrap sought by the canonical research mandate.