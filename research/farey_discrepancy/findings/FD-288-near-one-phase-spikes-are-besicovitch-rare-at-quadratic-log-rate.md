# FD-288 — Near-one phase spikes are Besicovitch-rare at quadratic-log rate

- **Date:** 2026-09-23
- **Status:** proved unconditional generic-height sparsity bound with a finite-window transference gap
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** right-Perron-collar / logarithmic-derivative mean square / Besicovitch sparsity / phase-spike obstruction / route narrowing
- **Depends on:** FD-284, FD-285, FD-286, FD-287
- **Classification:** `DERIVED + UNCONDITIONAL-BESICOVITCH-SPARSITY + RIGHT-COLLAR + PHASE-SPIKE + SOURCE-SELECTION-GAP + ROUTE-NARROWING`

## Claim

FD-287 reduced internal self-cancellation of the polynomial-height right Perron collar to a near-one phase spike of size `asymp log x`. The present finding shows that such spikes are **generic-height sparse at quadratic-log rate** once one moves an asymptotically negligible distance to the strict right half-plane.

Put

\[
L:=\log(2Nx),
\qquad
\delta_L:=L^{-2},
\tag{1}
\]

and fix

\[
\eta\in(e^{-\pi/2},1).
\tag{2}
\]

For `u>0`, define

\[
F_u(t):=-\frac{\zeta'}{\zeta}(1+u+it),
\tag{3}
\]

and the strict-inner phase envelope

\[
M^{\mathrm{str}}_{\eta,L}(t)
:=
\sup_{\delta_L\le u\le\eta/L}
\left|\operatorname{Im}F_u(t)\right|.
\tag{4}
\]

Let

\[
C_0:=\sum_{n\ge2}\frac{\Lambda(n)^2}{n^2}
=\sum_p\frac{(\log p)^2}{p^2-1}<\infty
\tag{5}
\]

and

\[
C_1:=
\sum_{n\ge2}
\frac{\Lambda(n)^2(\log n)^2}{n^2}<\infty.
\tag{6}
\]

For a measurable set `E subset R`, write

\[
\overline d_B(E)
:=
\limsup_{H\to\infty}
\frac{|E\cap[-H,H]|}{2H}
\tag{7}
\]

for its upper symmetric Besicovitch height density. Then, for every fixed `A>0`,

\[
\boxed{
\overline d_B
\left\{
 t:
 M^{\mathrm{str}}_{\eta,L}(t)\ge AL
\right\}
\le
\frac{
\left(\sqrt{C_0}+\dfrac{\eta\sqrt{C_1}}{L}\right)^2
}{A^2L^2}.
}
\tag{8}
\]

In particular,

\[
\boxed{
\overline d_B
\left\{
 t:
 M^{\mathrm{str}}_{\eta,L}(t)\ge AL
\right\}
\le
\frac{C_0+o_\eta(1)}{A^2L^2}.
}
\tag{9}
\]

Thus the order-`L` phase spikes required by FD-287 occupy at most `O(L^{-2})` of height in the Besicovitch sense.

The same split used in FD-287 gives the Farey/Perron interpretation. Define

\[
f(\eta):=
\frac{\pi/2+\log\eta}{\eta}.
\tag{10}
\]

At a polynomial height

\[
T=x^{\tau+o(1)},
\qquad 0<\tau<1/2,
\tag{11}
\]

Leong's already anchored bound on `zeta'/zeta` makes the ultra-thin slice

\[
1\le\sigma\le1+L^{-2}
\tag{12}
\]

cost only `o(1)` phase. Therefore, if the complete right collar loses the common-half-plane protection used in FD-287, then necessarily

\[
M^{\mathrm{str}}_{\eta,L}(T)
\ge
\bigl(f(\eta)-o(1)\bigr)L.
\tag{13}
\]

The same optimizer as in FD-287,

\[
\eta_*:=e^{1-\pi/2}=0.5650752749\ldots,
\tag{14}
\]

satisfies

\[
f(\eta_*)=e^{\pi/2-1}=\eta_*^{-1}.
\tag{15}
\]

Hence the corresponding strict-inner exceptional set obeys

\[
\boxed{
\overline d_B(E_L)
\le
\frac{C_0e^{2-\pi}+o(1)}{L^2}.
}
\tag{16}
\]

The conclusion is deliberately **generic in height, not local in the polynomial window**. Equation (16) does not imply that a source-selected sequence of Perron heights, or even the finite interval around `T=x^tau`, avoids `E_L`. A globally zero-density set may still contain every height selected by the construction. The next live bottleneck is therefore a finite-window or source-selection transference theorem, not another worst-case bound for `zeta'/zeta`.

## 1. Strict-right logarithmic derivatives have bounded Besicovitch energy

For every `u>0`, absolute convergence gives

\[
F_u(t)
=
\sum_{n\ge2}
\frac{\Lambda(n)}{n^{1+u}}e^{-it\log n}.
\tag{17}
\]

The frequencies `log n` are distinct. Expanding a finite Dirichlet polynomial and averaging over a symmetric height interval kills every off-diagonal term. Absolute convergence then passes the identity to (17):

\[
\lim_{H\to\infty}
\frac1{2H}
\int_{-H}^{H}|F_u(t)|^2\,dt
=
\sum_{n\ge2}
\frac{\Lambda(n)^2}{n^{2+2u}}
\le C_0.
\tag{18}
\]

Differentiating with respect to `u`, still in the absolutely convergent half-plane,

\[
\partial_uF_u(t)
=
-
\sum_{n\ge2}
\frac{\Lambda(n)\log n}{n^{1+u}}e^{-it\log n},
\tag{19}
\]

and the same orthogonality gives

\[
\lim_{H\to\infty}
\frac1{2H}
\int_{-H}^{H}|\partial_uF_u(t)|^2\,dt
=
\sum_{n\ge2}
\frac{\Lambda(n)^2(\log n)^2}{n^{2+2u}}
\le C_1.
\tag{20}
\]

Both constants are finite because the extra `n^{-2}` dominates every fixed logarithmic power. No hypothesis on the zeros of `zeta` is used here.

## 2. A one-dimensional maximal estimate turns mean square into spike sparsity

Let

\[
a:=\eta/L,
\qquad
b:=L^{-2}.
\tag{21}
\]

For each fixed `t` and every `u in [b,a]`, the fundamental theorem of calculus gives

\[
|F_u(t)|
\le
|F_a(t)|
+
\int_b^a|\partial_vF_v(t)|\,dv.
\tag{22}
\]

Therefore

\[
M^{\mathrm{str}}_{\eta,L}(t)
\le
|F_a(t)|
+
\int_b^a|\partial_vF_v(t)|\,dv.
\tag{23}
\]

Take the `L^2` norm in `t` over `[-H,H]`, normalized by `(2H)^{-1/2}`, and apply Minkowski. Because `b>0`, both Dirichlet series converge absolutely and uniformly on the compact strip `b<=v<=a`; the passage `H->infinity` is therefore legitimate termwise and uniformly on that strip. Using (18)--(20),

\[
\left\|M^{\mathrm{str}}_{\eta,L}\right\|_{B^2}
\le
\sqrt{C_0}
+
(a-b)\sqrt{C_1}
\le
\sqrt{C_0}
+
\frac{\eta\sqrt{C_1}}L.
\tag{24}
\]

Chebyshev's inequality for the upper Besicovitch density now gives (8). The important scale separation is that the maximal envelope over a strip of width `asymp L^{-1}` has **bounded mean-square energy**, while FD-287 requires a spike of height `asymp L`. The resulting exceptional density is therefore `asymp L^{-2}`.

This is not a new mean-value theorem for the logarithmic derivative. It is the elementary strict-right Dirichlet-series orthogonality translated into the exact near-one phase envelope singled out by the Farey Perron argument.

## 3. The `L^{-2}` boundary slice is negligible at the polynomial heights of FD-287

The reason for starting at `sigma=1+L^{-2}` is structural rather than cosmetic. At `sigma=1`, the Dirichlet series (17) is no longer absolutely convergent, and forcing a boundary-value theorem into the argument would add machinery without helping the actual Farey bottleneck.

At the polynomial heights relevant to FD-287, the omitted slice can instead be paid for pointwise. The already anchored explicit estimate

\[
\left|
\frac{\zeta'}{\zeta}(\sigma+iT)
\right|
\le24.303\log T,
\qquad \sigma\ge1,\ T\ge13,
\tag{25}
\]

implies

\[
\int_1^{1+L^{-2}}
\left|
\operatorname{Im}\frac{\zeta'}{\zeta}(\sigma+iT)
\right|d\sigma
\le
\frac{24.303\log T}{L^2}.
\tag{26}
\]

If `T=x^{tau+o(1)}` and `x=N^{lambda+o(1)}` with fixed positive `tau,lambda`, then `log T=O(L)` and (26) is `O(L^{-1})=o(1)`.

On the outer piece `1+eta/L<=sigma<=1+1/L`, FD-285 gives phase cost

\[
\log\frac1\eta+O_\eta(L^{-1}).
\tag{27}
\]

If the strict-inner envelope is at most `AL`, its phase cost is at most

\[
\left(\frac\eta L-L^{-2}\right)AL
\le\eta A.
\tag{28}
\]

Thus, with any fixed positive cone margin, the whole collar remains in a common phase half-plane whenever

\[
\log\frac1\eta+\eta A<\frac\pi2.
\tag{29}
\]

Letting the fixed margin tend to zero recovers the FD-287 threshold `A=f(eta)` and proves (13). Under RH and the prime-sector range `tau<1/2`, staying in that common half-plane preserves the `Nx/(L^2 log x)` signed prime witness exactly as in FD-287. RH enters only in that downstream prime-counting step, not in the spike-sparsity estimate (8).

## 4. The same split optimizes the generic-height sparsity constant

For fixed `eta`, the asymptotic density bound at the phase-protection threshold is

\[
\overline d_B(E_{\eta,L})
\le
\frac{C_0+o(1)}{f(\eta)^2L^2}.
\tag{30}
\]

Because the numerator is asymptotically independent of `eta`, minimizing this upper bound is equivalent to maximizing `f(eta)`. FD-287 already computed that maximum at

\[
\eta_*=e^{1-\pi/2},
\qquad
f(\eta_*)=\eta_*^{-1}.
\tag{31}
\]

Substitution gives (16), since

\[
\eta_*^2=e^{2-\pi}=0.3193100663\ldots.
\tag{32}
\]

So the optimizer that gave the strongest pointwise spike tariff in FD-287 also gives the strongest leading Besicovitch sparsity constant within this two-scale method.

## Adversarial stress test

The result survives the following failure checks.

1. **It does not reuse FD-270.** FD-270 averages a finite critical-zero packet over the dilation variable `u=log N`. Here the averaging variable is the Perron height `t`, the object is the strict-right logarithmic derivative, and the target is the near-one phase-spike obstruction isolated only in FD-287.
2. **No boundary Dirichlet-series claim is made.** All mean-square identities are proved on `Re(s)>1`, starting at `1+L^{-2}`. The missing boundary slice is handled separately and only in the polynomial-height application.
3. **The maximal envelope is actually controlled.** A pointwise spike may move with `sigma`; equation (22) controls the supremum over the entire strict-inner strip using both `F` and its `sigma` derivative, rather than applying a fixed-`sigma` estimate and silently taking a supremum.
4. **The derivative energy is finite.** The extra `(log n)^2` in (20) still leaves a convergent `n^{-2}`-weighted series, so differentiating once does not consume the mean-square budget.
5. **The result is generic-height only.** Besicovitch density sends the averaging horizon to infinity with `L` fixed. It gives no quantitative count in a finite polynomial window whose location and size grow with `x`.
6. **Source selection is not randomized.** A construction may choose every Perron height from `E_L` even though `E_L` has density `O(L^{-2})`. Equation (16) therefore does not by itself close the hard-Perron route.
7. **Half-plane failure and actual cancellation are not identified.** The phase spike is necessary for this sufficient half-plane protection to fail. A spike does not prove that the collar actually cancels, and cancellation involving `Re(s)<=1` or another contour segment remains outside the statement.
8. **No novelty claim is made for mean-square theory of `zeta'/zeta`.** The research delta is the conversion of elementary strict-right Dirichlet orthogonality into an `O(L^{-2})` exceptional-height set for the specific Farey right-collar phase obstruction.

## Consequence for the live route

FD-287 turned the surviving polynomial-height escape into a worst-case near-one phase spike. FD-288 shows that the spike is not a generic feature of height: after removing only an `L^{-2}` boundary slice, the phase derivative has bounded Besicovitch maximal energy, while the escape requires size `asymp L`. The bad set therefore has upper height density `O(L^{-2})`.

This is meaningful route narrowing, but not route closure. The decisive missing bridge is now explicit: one needs a **finite-window maximal estimate** strong enough on windows around the admissible polynomial Perron heights, or a theorem showing that the source-selected heights cannot concentrate inside the Besicovitch-exceptional set. A naive passage from (16) to the source-selected sequence would be invalid.

The natural next test is therefore local rather than global: estimate

\[
\operatorname{meas}
\left\{
T\in[H,2H]:
M^{\mathrm{str}}_{\eta,L}(T)\ge f(\eta)L
\right\}
\tag{33}
\]

uniformly when `H=x^{tau+o(1)}`. At `u=L^{-2}`, the effective Dirichlet-series length is far larger than any polynomial in `x`, so ordinary short Dirichlet-polynomial mean values do not automatically provide this transference. That obstruction, rather than the global mean square itself, is the new frontier.