# FD-287 — Polynomial-height right-collar cancellation forces a near-one phase spike

- **Date:** 2026-09-23
- **Status:** proved RH-conditional route-narrowing bound
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** grouped Perron collar / two-scale reciprocal-zeta phase budget / signed prime witness / polynomial-height extension / route narrowing
- **Depends on:** FD-261, FD-282, FD-283, FD-284, FD-285, FD-286
- **Classification:** `DERIVED + RH-CONDITIONAL + SIGNED-PERRON-LOWER-BOUND + FULL-RIGHT-COLLAR + PRIME-PHASE-WITNESS + POLYNOMIAL-HEIGHT + PHASE-SPIKE-DICHOTOMY + ROUTE-NARROWING`

## Claim

FD-286 protects the entire strict-right Perron collar unconditionally at sub-Korobov--Vinogradov heights, but deliberately stops before polynomial height. FD-285, conversely, reaches polynomial height under RH but protects only a fixed outer part of the collar. Combining their two phase controls gives a quantitative dichotomy at polynomial height: **if the whole right collar is to self-cancel the prime witness, the near-one part of `zeta'/zeta` must develop a phase derivative of order `log x`.**

Fix `lambda>0` and let

\[
x=N^{\lambda+o(1)},\qquad
L:=\log(2Nx),\qquad
c:=1+\frac1L.
\tag{1}
\]

For `eta in (exp(-pi/2),1)` put

\[
a_\eta:=1+\frac{\eta}{L}
\tag{2}
\]

and define the near-one phase-derivative envelope

\[
M_\eta(T)
:=
\sup_{1\le\sigma\le a_\eta}
\left|
\operatorname{Im}
\frac{\zeta'}{\zeta}(\sigma+iT)
\right|.
\tag{3}
\]

Assume RH and `T>=13`. If, for some fixed `delta>0`,

\[
\boxed{
\log\frac1\eta
+
\frac{\eta}{L}M_\eta(T)
\le
\frac\pi2-\delta,
}
\tag{4}
\]

then the **entire** right collar `1<=sigma<=c` remains in one strict phase half-plane. Consequently, whenever the RH prime-sector count is uniform at the chosen height (in particular for `T=x^{tau+o(1)}` with fixed `0<tau<1/2`), the paired grouped collar

\[
\mathcal H_d^R(T)
:=-\frac1\pi\operatorname{Im}
\int_1^c
\frac{N^{\sigma+iT}K_{\sigma+iT}(d)}
     {\zeta(\sigma+iT)}\,d\sigma
\tag{5}
\]

satisfies

\[
\boxed{
\sum_{x<d\le2x}
|\mathcal H_d^R(T)|
\gg_{\lambda,\eta,\delta}
\frac{Nx}{L^2\log x}
= Nx^{1-o(1)}.
}
\tag{6}
\]

Here

\[
K_s(d)
:=\sum_{q\mid d}\frac{q^s-(q-1)^s}{s}
 =\sum_{q\mid d}\int_{q-1}^{q}u^{s-1}\,du
\tag{7}
\]

is the same grouped physical kernel as in FD-282--FD-286.

The contrapositive of (4) is the useful structural statement. At polynomial heights below the prime-counting ceiling, defeating the right-collar prime plateau by **internal right-collar cancellation** requires

\[
\boxed{
M_\eta(T)
\ge
\left(
\frac{\pi/2+\log\eta}{\eta}
-o(1)
\right)L.
}
\tag{8}
\]

Optimizing the coefficient over `eta` gives

\[
\eta_*:=e^{1-\pi/2}=0.5650752749\ldots,
\tag{9}
\]

and

\[
\boxed{
\sup_{1\le\sigma\le1+\eta_*/L}
\left|
\operatorname{Im}\frac{\zeta'}{\zeta}(\sigma+iT)
\right|
\ge
\left(e^{\pi/2-1}-o(1)\right)L
}
\tag{10}
\]

as a necessary condition for that self-cancellation mechanism. Numerically,

\[
e^{\pi/2-1}=1.7696757307\ldots.
\tag{11}
\]

Finally, inserting Leong's unconditional explicit estimate

\[
\left|\frac{\zeta'}{\zeta}(\sigma+iT)\right|
\le 24.303\log T,
\qquad \sigma\ge1,\ T\ge13,
\tag{12}
\]

turns the dichotomy into a polynomial-height extension of FD-286. Define

\[
\kappa_*:=
\frac{e^{\pi/2-1}}{24.303}
=0.07281717198\ldots.
\tag{13}
\]

If

\[
T=x^{\tau+o(1)},
\qquad
0<\tau<
\min\left\{
\frac12,
\kappa_*\left(1+\frac1\lambda\right)
\right\},
\tag{14}
\]

then, under RH, the full-collar lower bound (6) holds. At the first-row scale `lambda=1`, this gives the explicit sufficient range

\[
\boxed{0<\tau<0.1456343439\ldots.}
\tag{15}
\]

Thus the full right collar is protected not merely at `T=x^{o(1)}` but through a genuine fixed polynomial-height interval.

## 1. Split the collar where the outer phase budget is exact

Write

\[
g_T(\sigma):=\frac1{\zeta(\sigma+iT)}.
\tag{16}
\]

On the outer interval `[a_eta,c]`, FD-285 uses absolute convergence in `sigma>1` to obtain

\[
\left|
\arg g_T(\sigma)-\arg g_T(c)
\right|
\le
\log\frac{\zeta(a_\eta)}{\zeta(c)}.
\tag{17}
\]

Since `a_eta-1=eta/L` and `c-1=1/L`, the Laurent expansion at `1` gives, for fixed `eta`,

\[
\log\frac{\zeta(a_\eta)}{\zeta(c)}
=
\log\frac1\eta+O_\eta(L^{-1}).
\tag{18}
\]

This is sharper than spending Leong's uniform `24.303 log T` bound across the whole collar. In particular, it costs no factor `log T/L` on the outer piece.

## 2. The inner slice pays only its actual phase derivative

Along a continuous argument branch,

\[
\frac{d}{d\sigma}\arg g_T(\sigma)
=
-\operatorname{Im}
\frac{\zeta'}{\zeta}(\sigma+iT).
\tag{19}
\]

Therefore every `sigma in [1,a_eta]` satisfies

\[
\left|
\arg g_T(\sigma)-\arg g_T(a_\eta)
\right|
\le
\frac{\eta}{L}M_\eta(T).
\tag{20}
\]

Combining (18) and (20), the whole collar obeys

\[
\left|
\arg g_T(\sigma)-\arg g_T(c)
\right|
\le
\log\frac1\eta
+
\frac{\eta}{L}M_\eta(T)
+O_\eta(L^{-1}).
\tag{21}
\]

Hence (4), with a slightly smaller fixed margin after absorbing the `O(1/L)` term, puts every `g_T(sigma)` in the common cone

\[
|\arg z-\arg g_T(c)|
\le
\frac\pi2-\frac\delta2.
\tag{22}
\]

This is the step that converts a possible cancellation mechanism into the phase-spike tariff (8).

## 3. A common phase half-plane protects the full prime coefficient

For a prime `p in (x,2x]`, define the ideal self-divisor coefficient over the **whole** right collar by

\[
A_p^R(T)
:=
\int_1^c
N^\sigma p^{\sigma-1}g_T(\sigma)\,d\sigma.
\tag{23}
\]

The scalar weight `N^sigma p^(sigma-1)` is positive. Under (22), projection onto the direction `g_T(c)` is nonnegative on the whole collar and is at least a fixed positive fraction of the modulus. Keeping only the outer interval for the size lower bound therefore gives

\[
|A_p^R(T)|
\gg_{\lambda,\eta,\delta}
\int_{a_\eta}^{c}
N^\sigma p^{\sigma-1}|g_T(\sigma)|\,d\sigma.
\tag{24}
\]

For `sigma>1`,

\[
|g_T(\sigma)|
\ge\frac1{\zeta(\sigma)}.
\tag{25}
\]

On `[a_eta,c]`, `1/zeta(sigma) >>_eta 1/L`; the interval has width `(1-eta)/L`; and `N^sigma p^(sigma-1)` stays within constant multiples of `N`. Thus

\[
\boxed{|A_p^R(T)|\gg_{\lambda,\eta,\delta}N/L^2.}
\tag{26}
\]

Moreover all `A_p^R(T)` remain in one fixed cone of angular radius `<pi/2`. This is enough for a robust prime phase sector; the coefficient phases need not be `o(1)`-close to each other.

As in FD-286, the exact prime cell

\[
\int_{p-1}^{p}u^{s-1}\,du
\tag{27}
\]

differs from `p^(s-1)` by relative `O((T+1)/p)`. Using Leong's bound `|1/zeta(sigma+iT)|<=30.812 log T`, the integrated error is

\[
\ll \frac{NT\log T}{xL}.
\tag{28}
\]

For every fixed `tau<1`, (28) is `o(N/L^2)` when `T=x^{tau+o(1)}`. The height range in (14) is therefore safely inside the cell-approximation range.

## 4. RH supplies enough primes in the robust phase sector

The `q=1` divisor cell contributes the same real scalar `B(T)` to every prime coordinate, exactly as in FD-286. It need not be small. Choose the robust sine sector so that the prime self-divisor term has the same sign as `B(T)`. Because the coefficient cone has a fixed positive angular margin, the selected phase sector has fixed positive angular measure.

Inside `[x,2x]`, the condition on

\[
T\log p+\Phi_T
\pmod{2\pi}
\tag{29}
\]

is a union of `O(T)` intervals with total Euclidean length `>>x`. Under RH, Schoenfeld's estimate

\[
\vartheta(y)=y+O(\sqrt y\log^2 y)
\tag{30}
\]

makes the total endpoint error over those intervals

\[
O(T\sqrt x\log^2 x).
\tag{31}
\]

For `T=x^{tau+o(1)}` with `tau<1/2`, (31) is `o(x)`. Hence the robust sector contains `>>x/log x` primes. Each such prime contributes `>>N/L^2` after the exact `q=1` translation and the error (28), proving (6).

This is the only place where RH is needed in the polynomial-height theorem. The phase-budget inequalities themselves use only the zero-free right edge and the already anchored explicit bounds.

## 5. The optimized spike constant and the polynomial-height corollary

Ignoring an arbitrarily small fixed cone margin, (4) can hold only if

\[
M_\eta(T)
<
\frac{\pi/2+\log\eta}{\eta}L.
\tag{32}
\]

The coefficient

\[
f(\eta):=
\frac{\pi/2+\log\eta}{\eta}
\tag{33}
\]

has derivative

\[
f'(\eta)
=
\frac{1-(\pi/2+\log\eta)}{\eta^2},
\tag{34}
\]

so its maximum on `(exp(-pi/2),1)` occurs at

\[
\eta_*=e^{1-\pi/2}.
\tag{35}
\]

At this point

\[
f(\eta_*)
=
\frac1{\eta_*}
=e^{\pi/2-1}.
\tag{36}
\]

This proves the optimized necessary spike (10) **within this two-piece phase-budget method**.

For the explicit corollary, Leong's bound (12) gives

\[
M_{\eta_*}(T)
\le24.303\log T.
\tag{37}
\]

If `T=x^(tau+o(1))`, then

\[
L
=
\left(1+\frac1\lambda+o(1)\right)\log x.
\tag{38}
\]

Thus a fixed cone margin survives whenever

\[
24.303\tau
<
e^{\pi/2-1}
\left(1+\frac1\lambda\right),
\tag{39}
\]

which is exactly the second restriction in (14). Compared with applying the uniform `24.303 log T` bound over the entire collar from the outset, the optimized split preserves the exact outer phase budget and buys a strictly larger polynomial-height window.

## Adversarial stress test

The main ways this argument could overstate the advance were checked explicitly.

1. **The theorem does not assume common prime-coefficient phase.** The `A_p^R(T)` may move inside a fixed cone. The prime sector is chosen with enough angular margin to work uniformly for every phase in that cone.
2. **The inner slice is not discarded.** Under (4) it has nonnegative projection onto the same common direction, so it cannot cancel the outer lower bound. The proof uses the outer slice only to certify amplitude.
3. **The `q=1` cell is not treated as a small error.** It is kept as the coordinate-independent scalar `B(T)` and the prime phase sector is selected to reinforce its sign, as in FD-286.
4. **Polynomial-height prime counting is paid for.** There are `O(T)` phase intervals. Schoenfeld's RH error yields the explicit ceiling `tau<1/2`; no unconditional polynomial-height PNT claim is made.
5. **The exact prime-cell replacement is paid for.** Its error is (28), negligible for `tau<1`, hence in the whole stated range.
6. **The phase spike is necessary only for internal right-collar self-cancellation.** A large contribution from `Re(s)<=1`, another contour segment, or a different Perron representation may still cancel the protected right collar.
7. **The constant `e^(pi/2-1)` is not claimed globally sharp.** It is the optimum of this specific split: exact FD-285 outer phase budget plus an `L^infinity` bound for the inner phase derivative. A more structured estimate of the signed inner phase could improve it.
8. **Large near-one phase derivatives are not ruled out.** Equation (10) identifies what a surviving polynomial-height escape must do; it does not assert that such spikes never occur.

## Consequence for the live route

FD-286 showed unconditionally that the complete right collar cannot self-cancel at sub-Korobov--Vinogradov height. The present finding extends that protection, under RH, to a genuine polynomial range. At `lambda=1`, every fixed height exponent `tau<0.1456343439...` is excluded as a source of internal right-collar cancellation.

Beyond that window, the route is no longer described merely as "the right collar may rotate enough." It now has a quantitative local requirement: before the collar can destroy its prime witness, the near-one interval of width about `0.565/L` must support `|Im zeta'/zeta|` on the order of at least `1.770 L`, unless one uses cancellation from outside the right collar.

The next useful test is therefore to study the distribution, rather than just the worst-case upper bound, of these near-one phase spikes at polynomial heights. If one can show that (10) fails on all or almost all source-selected heights in a larger range, the right-collar plateau extends correspondingly. If such spikes are common, then the live mechanism has finally been localized to a concrete zeta-phase event.

## Prior-art audit

A bounded search across explicit `zeta'/zeta` estimates, Perron/Mertens formulas, and Farey-discrepancy literature found the expected generic ingredients but no equivalent two-scale application to the grouped Farey repair field. Leong supplies the explicit logarithmic-derivative and reciprocal bounds; Schoenfeld supplies the RH prime-counting error. Neither source contains the phase-budget split (17)--(21), the optimized threshold (10), or the divisor-replicated prime-witness consequence (6). The novelty claim is limited to that synthesis and route-narrowing consequence.

No new literature theorem is introduced beyond sources already anchored for FD-284 and FD-286, so `SOURCES.md` does not need an update in this pass.

## Evidence status

- Equations (17)--(21), (23)--(28), and (32)--(39) are exact identities or elementary estimates once the Perron collar is fixed.
- Equation (12) and the reciprocal bound used in (28) are literature inputs from Nicol Leong, already used by FD-286.
- Equation (30) is the RH-conditional Schoenfeld input already anchored for FD-284.
- The band lower bound (6) and polynomial range (14) are derived from those inputs and are conditional on RH only through the polynomial-height prime-sector count.
- No numerical experiment is used as evidence; the displayed decimals are evaluations of exact constants.

## Sources

- Nicol Leong, *Explicit estimates for the logarithmic derivative and the reciprocal of the Riemann zeta function*, Journal of Number Theory **285** (2026), 230--261, DOI `10.1016/j.jnt.2026.01.007`, arXiv `2405.04869`; Corollaries 2 and 4.
- Lowell Schoenfeld, *Sharper Bounds for the Chebyshev Functions theta(x) and psi(x). II*, Mathematics of Computation **30**(134) (1976), 337--360, DOI `10.1090/S0025-5718-1976-0457374-X`, Theorem 10.
