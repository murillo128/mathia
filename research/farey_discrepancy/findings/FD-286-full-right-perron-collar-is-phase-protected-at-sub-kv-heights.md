# FD-286 — Full right Perron collar is phase-protected at sub-Korobov–Vinogradov heights

- **Date:** 2026-09-23
- **Status:** proved unconditional route-narrowing bound
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** grouped Perron collar / reciprocal-zeta phase control / signed prime witness / unconditional prime-density input / route narrowing
- **Depends on:** FD-261, FD-282, FD-283, FD-284, FD-285
- **Classification:** `DERIVED + UNCONDITIONAL + SIGNED-PERRON-LOWER-BOUND + FULL-RIGHT-COLLAR + PRIME-PHASE-WITNESS + SUB-KV-HEIGHT + ROUTE-NARROWING`

## Claim

FD-285 protects any fixed outer fraction smaller than `1-exp(-pi/2)` of the strict-right Perron collar at polynomial heights, conditionally on RH. At substantially lower heights one can instead protect the **entire** strict-right collar, unconditionally. The key is that an explicit `O(log T)` bound for `zeta'/zeta` makes the reciprocal-zeta phase variation across the full width `1/log(2Nx)` tend to zero, while the unconditional Korobov–Vinogradov prime-number-theorem remainder still counts a positive-density prime phase sector after splitting `[x,2x]` into `O(T)` pieces.

Fix `lambda>0` and let

\[
x=N^{\lambda+o(1)},\qquad
L:=\log(2Nx),\qquad
c:=1+\frac1L.
\tag{1}
\]

Write

\[
\Omega(x):=(\log x)^{3/5}(\log\log x)^{-1/5}.
\tag{2}
\]

Let `T=T(x)>=13` satisfy

\[
\boxed{\log T=o(\Omega(x)).}
\tag{3}
\]

With the grouped physical kernel

\[
K_s(d)
:=\sum_{q\mid d}\frac{q^s-(q-1)^s}{s}
 =\sum_{q\mid d}\int_{q-1}^{q}u^{s-1}\,du,
\tag{4}
\]

define the upper/lower-paired contribution of the **whole** strict-right collar by

\[
\mathcal H_d^{R}(T)
:=-\frac1\pi\operatorname{Im}
\int_{1}^{c}
\frac{N^{\sigma+iT}K_{\sigma+iT}(d)}
     {\zeta(\sigma+iT)}\,d\sigma.
\tag{5}
\]

Then, unconditionally,

\[
\boxed{
\sum_{x<d\le2x}
\left|\mathcal H_d^{R}(T)\right|
\gg_{\lambda}
\frac{Nx}{L^2\log x}
= Nx^{1-o(1)}.
}
\tag{6}
\]

The implied lower bound is meant asymptotically along any height function satisfying (3). In particular, no RH assumption enters (6).

## 1. The full right collar has vanishing reciprocal-zeta phase width

Set

\[
g_T(\sigma):=\frac1{\zeta(\sigma+iT)}.
\tag{7}
\]

Nicol Leong proves the explicit uniform estimate

\[
\left|\frac{\zeta'}{\zeta}(\sigma+iT)\right|
\le 24.303\log T,
\qquad \sigma\ge1,\ T\ge13.
\tag{8}
\]

Hence, along a continuous argument branch of `g_T` on `[1,c]`,

\[
\left|\arg g_T(\sigma)-\arg g_T(c)\right|
\le 24.303\frac{\log T}{L}.
\tag{9}
\]

Because `Omega(x)=o(log x)` and (3) holds, the right side is `o(1)`. Thus the vectors `g_T(sigma)` across the **entire** interval `[1,c]` lie in a cone of angular radius `o(1)` around one common direction. This is stronger than the fixed `pi/2` cone budget used in FD-285, but only in the sub-Korobov–Vinogradov height regime (3).

The endpoint `sigma=1` causes no singularity here: `T>=13`, `zeta(1+iT)` is finite and nonzero, and (8) is stated uniformly for `sigma>=1`.

## 2. Prime self-divisors retain amplitude `N/L^2`

For a prime `p in (x,2x]`, the divisor set is `{1,p}`. Separate the `q=p` cell and define

\[
A_p(T)
:=\int_1^c
N^\sigma p^{\sigma-1}g_T(\sigma)\,d\sigma.
\tag{10}
\]

The scalar weight in (10) is positive. Since the integrand directions lie in the common `o(1)` cone from (9), positive averaging cannot cancel them. Therefore

\[
|A_p(T)|
\ge (1-o(1))
\int_1^c N^\sigma p^{\sigma-1}|g_T(\sigma)|\,d\sigma.
\tag{11}
\]

For `sigma>1`, absolute convergence gives

\[
|\zeta(\sigma+iT)|\le\zeta(\sigma),
\qquad
|g_T(\sigma)|\ge\frac1{\zeta(\sigma)}.
\tag{12}
\]

Writing `sigma=1+t`, one has for `0<t<=1/L`

\[
\zeta(1+t)
=1+\sum_{n\ge2}n^{-1-t}
\le 1+\int_1^\infty u^{-1-t}\,du
=1+\frac1t,
\tag{13}
\]

so

\[
\frac1{\zeta(1+t)}\ge\frac{t}{1+t}\gg t.
\tag{14}
\]

Also `N^sigma p^(sigma-1)=N(Np)^t` stays between positive constant multiples of `N` on `0<=t<=1/L`, uniformly for `p in (x,2x]`. Consequently

\[
\boxed{|A_p(T)|\gg_\lambda \frac{N}{L^2}.}
\tag{15}
\]

Moreover, all `A_p(T)` lie in the same `o(1)` angular cone, uniformly in those primes.

## 3. The exact prime cell differs negligibly from the ideal phase mode

The physical `q=p` cell is

\[
I_p(s):=\int_{p-1}^{p}u^{s-1}\,du.
\tag{16}
\]

Uniformly for `1<=sigma<=c`,

\[
I_p(\sigma+iT)
=p^{\sigma+iT-1}
\left(1+O\!\left(\frac{T+1}{p}\right)\right).
\tag{17}
\]

Leong also proves, for `sigma>=1` and `T>=13`,

\[
\left|\frac1{\zeta(\sigma+iT)}\right|
\le 30.812\log T.
\tag{18}
\]

Thus the integrated error incurred by replacing (16) with `p^(s-1)` is

\[
\ll
\frac{NT\log T}{xL}.
\tag{19}
\]

Condition (3) implies `T=x^{o(1)}`, hence

\[
\frac{NT\log T}{xL}
=o\!\left(\frac{N}{L^2}\right).
\tag{20}
\]

So the prime-cell contribution to (5) is

\[
S_p(T)
=-\frac1\pi\operatorname{Im}
\left(e^{iT\log(Np)}A_p(T)\right)
+o\!\left(\frac{N}{L^2}\right),
\tag{21}
\]

with a common amplitude lower bound (15) and a common phase up to `o(1)`.

## 4. The `q=1` cell need not be small

FD-284 treated the `q=1` divisor cell as an error, which forced a polynomial lower bound on `T`. That is unnecessary. For every prime coordinate it contributes the **same real scalar**

\[
B(T)
:=-\frac1\pi\operatorname{Im}
\int_1^c
\frac{N^{\sigma+iT}}
     {(\sigma+iT)\zeta(\sigma+iT)}\,d\sigma.
\tag{22}
\]

Therefore

\[
\mathcal H_p^R(T)=B(T)+S_p(T)+o(N/L^2).
\tag{23}
\]

If `B(T)>=0`, choose primes for which the sine in (21) makes `S_p(T)` positive and bounded below by a fixed positive fraction of `|A_p(T)|`. If `B(T)<0`, choose the opposite sine sector. In either case the common translation `B(T)` reinforces rather than cancels the selected prime coordinates. A robust sector such as `sin(theta)>=3/4` or `sin(theta)<=-3/4` leaves room for the `o(1)` variation of `arg A_p(T)` and for the error in (21).

This is an exact sign-selection argument; it does **not** require an upper bound or a smallness estimate for `B(T)`.

## 5. Unconditional PNT counts enough robust prime phases

The robust sign condition is a fixed angular sector for

\[
T\log p+\Phi_T
\pmod{2\pi},
\tag{24}
\]

where `Phi_T` is independent of `p` up to `o(1)`. Inside `[x,2x]` the selected real set is a union of `O(T)` intervals. Because `T>=13`, the total phase travel `T log 2` exceeds one full period; uniformly in the initial phase, the selected intervals have total Euclidean length `>>x`.

Use the unconditional Korobov–Vinogradov-strength prime-number-theorem remainder already anchored in this line:

\[
\vartheta(y)
=y+O\!\left(y\,\operatorname{polylog}(y)
 e^{-c\Omega(y)}\right)
\tag{25}
\]

for some fixed `c>0`. Summing endpoint errors over the `O(T)` selected intervals gives

\[
O\!\left(
Tx\,\operatorname{polylog}(x)e^{-c\Omega(x)}
\right)
=o(x)
\tag{26}
\]

by (3). Hence the selected phase sector contains Chebyshev mass `>>x`, and therefore

\[
\#\{p\in(x,2x]: p\text{ is in the selected robust sector}\}
\gg \frac{x}{\log x}.
\tag{27}
\]

For every such prime, (15), (21), and (23) imply

\[
|\mathcal H_p^R(T)|\gg_\lambda\frac{N}{L^2}.
\tag{28}
\]

Summing only these prime coordinates proves (6).

## Adversarial stress test

The main ways this argument could falsely create a lower bound were checked explicitly.

1. **No hidden triangle inequality before the signed object.** The `sigma` integration and upper/lower pairing are performed before `|H_d^R|` is taken. The lower bound comes from a cone-preserving integral plus a prime sign sector, not from replacing the signed collar by its absolute mass.
2. **The line `sigma=1` is legitimate.** At `T>=13` there is no pole or zero of `zeta(1+iT)`; the explicit logarithmic-derivative and reciprocal bounds are stated for `sigma>=1`.
3. **The prime-cell approximation is uniform.** Its cost is (19), and (3) makes it `o(N/L^2)`.
4. **The common `q=1` mode cannot spoil every prime coordinate.** It is retained exactly as the scalar `B(T)` and the prime phase sector is chosen to have the same sign.
5. **The prime-sector count pays for all interval endpoints.** There are `O(T)` intervals, so the height hypothesis is deliberately the little-o condition (3); no untracked fixed constant in the Korobov–Vinogradov exponent is used.
6. **No claim is made at polynomial height.** When `T=x^tau`, the crude bound (8) permits `O(1)` or larger phase rotation across the full collar, and the unconditional endpoint-error summation in (26) also stops winning. FD-285 remains complementary: under RH it handles polynomial heights but protects only a fixed outer fraction of the collar.

## Consequence for the live route

For every sub-Korobov–Vinogradov height (3), internal cancellation inside the strict-right collar `(1,1+1/L]` cannot reduce its grouped physical-band contribution below power scale: an `Nx^(1-o(1))` signed plateau survives unconditionally. Thus, in this height regime, a hard-Perron rescue must obtain its compensation from the part of the contour with `Re(s)<=1` or from another contour component. It cannot come from redistributing phase inside the strict-right collar itself.

This also removes the technical lower-height restriction inherited from the FD-284 treatment of the `q=1` cell. The common divisor cell need not be negligible; its coordinate-independent translation can be absorbed by choosing the matching prime phase sector.

The result does **not** give a lower bound for the complete horizontal contour, does not control cancellation against `Re(s)<=1`, and does not extend (without new input) to polynomial `T`. Those remain the live boundaries.

## Prior-art audit

The two external inputs are standard analytic-number-theory estimates, not claimed as new: Leong's explicit bounds on `zeta'/zeta` and `1/zeta` for `sigma>=1`, and a Korobov–Vinogradov-strength PNT remainder. A bounded search across explicit zeta bounds, Perron/Mertens formula literature, and Farey discrepancy work found no equivalent application that keeps the divisor-replicated Farey kernel grouped, retains the full signed upper/lower collar, uses the prime coordinates to absorb the common `q=1` translation, and derives (6). The novelty claim is limited to this synthesis and route-narrowing consequence.

## Evidence status

- Equations (4), (10)--(17), and (21)--(23) are exact identities or elementary estimates after fixing the Perron collar.
- Equations (8) and (18) are literature theorems from Leong.
- Equation (25) is the already anchored unconditional PNT input of Korobov–Vinogradov strength.
- The lower bound (6) is derived from those inputs; it is unconditional but asymptotic.
- No numerical experiment is used as evidence.

## Sources

- Nicol Leong, *Explicit estimates for the logarithmic derivative and the reciprocal of the Riemann zeta function*, Journal of Number Theory **285** (2026), 230--261, DOI `10.1016/j.jnt.2026.01.007`, arXiv `2405.04869`; Corollaries 2 and 4.
- Daniel R. Johnston, *Zero-density estimates and the optimality of the error term in the prime number theorem*, arXiv `2411.13791` (current version 22 March 2026); used only for a qualitative Korobov–Vinogradov-strength PNT remainder, as already anchored in `SOURCES.md`.
