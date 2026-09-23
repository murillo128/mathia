# FD-293 — Inverse-polylog occupation certificates require near-linear good-gap populations

- **Date:** 2026-09-23
- **Status:** proved an RH-conditional population floor for every FD-292 inverse-polylog remainder-good occupation certificate and isolated a gapwise localization limit of the current phase selector
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** complementary hard remainder / zero-gap occupation / RH zero-gap cap / admissible-height intersection / route sharpening
- **Depends on:** FD-277, FD-291, FD-292
- **Classification:** `DERIVED + RH-ZERO-GAP-CAP + GOOD-GAP-POPULATION-FLOOR + METHOD-LOCALIZATION-OBSTRUCTION`

## Claim

FD-292 reduces the remaining admissible-height problem to proving, for any convenient fixed `P>0`, an inverse-polylogarithmic lower bound

\[
\Omega_B(J)\ge \delta_P\frac{H}{L^P}
\tag{1}
\]

for the total reciprocal-log-safe occupation of remainder-good zero gaps in a polynomial Perron-height window

\[
J=[H,2H],\qquad
H=x^{\tau+o(1)},\qquad
0<\tau<\frac12,
\qquad
L:=\log(2Nx).
\tag{2}
\]

That target looks weak as a measure statement. Under RH it nevertheless has a strong **population consequence**: it cannot be supplied by a sparse family of exceptional good gaps.

Let `Gamma_*={gamma_j}` be the increasing sequence of distinct positive ordinates of nontrivial zeta zeros, put

\[
G_j=(\gamma_j,\gamma_{j+1}),
\tag{3}
\]

and let `K_B(J)` denote the number of remainder-good gaps whose FD-291 safe core

\[
G_j^{\rm safe}(J)
=
J\cap
\left[
\gamma_j+\frac1L,
\gamma_{j+1}-\frac1L
\right]
\tag{4}
\]

is nonempty. Under RH,

\[
\boxed{
\gamma_{j+1}-\gamma_j
\le
\frac{\pi+o(1)}{\log\log H}
}
\tag{5}
\]

uniformly for every gap whose safe core meets `J`. Consequently

\[
\boxed{
\Omega_B(J)
\le
\left(\frac{\pi+o(1)}{\log\log H}\right)K_B(J),
}
\tag{6}
\]

and any certificate of the form (1) necessarily forces

\[
\boxed{
K_B(J)
\ge
\left(\frac{\delta_P}{\pi}-o(1)\right)
\frac{H\log\log H}{L^P}.
}
\tag{7}
\]

Thus the FD-292 route needs `H^{1-o(1)}` remainder-good zero gaps in each relevant polynomial window. Finitely many good gaps, a sparse exceptional sequence, or even `O(H^alpha)` good gaps for any fixed `alpha<1` cannot provide the required occupation.

There is a second, method-level consequence. FD-292 obtains its `2m`-th-moment phase exceptional estimate on an interval of length `R` under

\[
\frac{R}{L^{2m(m+2)}}\longrightarrow\infty
\tag{8}
\]

for fixed `m`. But (5) gives every individual zero gap length

\[
R_j\ll\frac1{\log\log H}.
\tag{9}
\]

Hence the existing Montgomery--Vaughan selector of FD-292 **cannot be rerun gap by gap** to prove that each remainder-good gap contains a phase-good point. Its role is intrinsically aggregate at the present level of localization. The next theorem must therefore produce enough total occupation across a large population of remainder-good gaps, or replace the current phase selector by a genuinely finer local mechanism.

This finding does **not** prove that any zero gap is remainder-good. It converts the live occupation gate into a necessary population scale and rules out a tempting sparse-gap strategy inside the present FD-292 framework.

## 1. RH caps every relevant zero gap at `pi/log log H`

The source ledger already records the Carneiro--Chandee--Milinovich RH estimate

\[
|S(t)|
\le
\left(\frac14+o(1)\right)
\frac{\log t}{\log\log t},
\tag{10}
\]

where `S(t)` is the argument term in the Riemann--von Mangoldt formula. We only need its elementary consequence for a zero-free interval.

Suppose `(t,t+h)` contains no distinct zero ordinate, with `t asymp H` and `h=o(H)`. Riemann--von Mangoldt gives

\[
0=N(t+h)-N(t)
=
\frac{h}{2\pi}\log t
+
S(t+h)-S(t)
+
O\!\left(\frac{h^2+1}{t}\right).
\tag{11}
\]

By (10),

\[
S(t+h)-S(t)
\ge
-\left(\frac12+o(1)\right)
\frac{\log H}{\log\log H}.
\tag{12}
\]

If for some fixed `epsilon>0`

\[
h\ge\frac{\pi+\epsilon}{\log\log H},
\tag{13}
\]

then the main term in (11) is

\[
\left(
\frac12+rac{\epsilon}{2\pi}+o(1)
\right)
\frac{\log H}{\log\log H},
\tag{14}
\]

which exceeds the worst possible negative contribution (12) for large `H`. This contradicts zero-freeness and proves (5).

This maximum-gap estimate is classical prior art, not a new zeta-zero theorem. Goldston--Gonek, *A note on S(T) and the zeros of the Riemann zeta-function* (2005, arXiv `math/0511092`), derive the same `(pi+o(1))/log log T` RH upper bound from sharp control of `S(t+h)-S(t)`. Here (5) is derived directly from the already anchored stronger-enough pointwise bound (10), so no new source dependency is required.

Multiplicity causes no problem. Equation (11) counts zeros with multiplicity, but an interval between consecutive **distinct** ordinates is genuinely zero-free. A multiple zero only increases the jump at an endpoint and does not weaken the zero-free-interval contradiction. Likewise, if a safe core meets an endpoint of `J`, (5) still applies because its containing gap has length `o(H)`, so both zero ordinates remain at height `asymp H`.

## 2. Occupation therefore costs a near-linear number of good gaps

For every gap counted by `K_B(J)`, its safe-core contribution is bounded by the full gap length:

\[
\operatorname{meas}G_j^{\rm safe}(J)
\le
\gamma_{j+1}-\gamma_j.
\tag{15}
\]

Summing (15) over remainder-good gaps and using (5) gives (6). Combining (6) with the FD-292 target (1) gives (7) immediately.

The adjective `near-linear` refers to the scale in the height parameter. Since `L asymp log x` and `log H asymp log x` in the polynomial regime,

\[
\frac{H\log\log H}{L^P}
=H^{1-o(1)}.
\tag{16}
\]

Thus the inverse-polylog occupation criterion cannot be realized by a sub-power population. It may still be realized by a very small *fraction* of all zero gaps. Riemann--von Mangoldt gives

\[
N(2H)-N(H)
=
\left(\frac1{2\pi}+o(1)\right)H\log H.
\tag{17}
\]

The number of distinct gaps intersecting `J` is at most this quantity up to endpoint terms. Therefore (7) forces at least the fraction

\[
\boxed{
\left(2\delta_P-o(1)\right)
\frac{\log\log H}{L^P\log H}
}
\tag{18}
\]

relative to that multiplicity-counted upper bound. In the polynomial scaling this is of order

\[
\frac{\log\log x}{(\log x)^{P+1}}.
\tag{19}
\]

Equation (18) is deliberately only a necessary density floor. It is not sufficient: even a much larger population could have tiny reciprocal-log-safe cores and fail (1).

This also sharpens the interpretation of the sufficient counting reformulation already noted in FD-292. There, assuming selected good gaps had a fixed extra `c/L` of safe width converted occupation into a lower bound on their count. Equation (7) goes in the opposite direction: the RH maximum-gap cap gives a **necessary** count for any occupation certificate, without imposing a lower bound on individual good-gap lengths.

## 3. The current phase selector cannot be localized to one zero gap

A possible response to (7) would be to abandon aggregate occupation and instead try to prove, for each remainder-good gap separately, that the FD-292 phase-bad set cannot fill the gap. The existing high-moment argument does not support that localization.

For fixed moment order `m`, FD-292 applies Montgomery--Vaughan on an interval of length `R` and obtains an error tending to zero only under (8). If the interval is one zero gap, (5) gives

\[
R
\le
\frac{\pi+o(1)}{\log\log H},
\tag{20}
\]

whereas

\[
L^{2m(m+2)}\longrightarrow\infty.
\tag{21}
\]

Thus

\[
\frac{R}{L^{2m(m+2)}}\longrightarrow0,
\tag{22}
\]

which is the opposite of the hypothesis needed for the FD-292 finite-window estimate. Increasing the fixed moment only worsens this localization requirement.

This is a limitation of the **current Montgomery--Vaughan implementation**, not a theorem that phase control is impossible on zero-gap scales. A different local estimate for `zeta'/zeta`, a pointwise phase mechanism tied to zero-free gaps, or a joint remainder/phase identity could bypass (22). The conclusion is narrower: one cannot cite FD-292 itself to certify phase-goodness independently inside each individual remainder-good gap.

## 4. Consequence for the live gate

FD-292 made the phase-exceptional set smaller than `H/L^P` for every chosen fixed `P`; that removed any distinguished inverse-polylog exponent from the intersection problem. FD-293 shows what is paid on the other side of that trade: **even an arbitrarily weak fixed inverse-polylog occupation certificate requires a macroscopic population on the exponent scale**.

The most direct remaining target is therefore no longer merely

\[
\text{find some remainder-good gap},
\tag{23}
\]

but rather prove an aggregate theorem of the form

\[
K_B(J)
\gtrsim
\frac{H\log\log H}{L^P}
\tag{24}
\]

*together with enough safe-core length to make the sum in `Omega_B(J)` reach `H/L^P`*. The count (24) alone is not sufficient, but any proof of the FD-292 occupation gate must at least operate at this population scale under RH.

This identifies a useful adversarial test for future remainder estimates. A bound that certifies only isolated cutoffs, finitely many favorable gaps, or a sub-power family `H^alpha` with fixed `alpha<1` cannot close the present route, regardless of how small the remainder is on those gaps. A viable theorem must either control the full remainder on a near-linear population of zero gaps, prove the occupation measure directly without enumerating gaps, or replace the current phase/remainder intersection architecture.

## 5. Prior-art and adversarial audit

The zero-gap cap (5) is classical and is not claimed as new. The literature search recovered Goldston--Gonek's RH bound of `(pi+o(1))/log log T` for the largest consecutive zero gap. The new content here is only the **line-specific transfer** of that cap to the FD-291/292 physical remainder-good occupation variable, plus the incompatibility between zero-gap scale and the present FD-292 Montgomery--Vaughan window condition.

No prior-art result found in this pass supplies the missing statement that the complete divisor-replicated hard remainder is good on `H^{1-o(1)}` zero gaps, or directly supplies `Omega_B(J) >= H/L^P`. Generic Mertens/Perron estimates remain on the wrong side of the FD-281 pointwise cost barrier unless they preserve additional signed or gapwise structure.

Adversarially, three distinctions are essential. First, (7) is **necessary only for a certificate at the occupation scale (1)**; it is not a necessary condition for the bare existence of one admissible height by some different argument. Second, many good gaps do not imply enough occupation because their safe cores may be short. Third, (22) rules out only reusing the present FD-292 mean-value estimate on one gap at a time; it does not rule out a stronger future local phase theorem.

The argument remains genuinely Farey-owned at this stage. The good/bad label is attached to the full physical remainder norm after consecutive sampling and divisor replication in FD-291, not to a generic Mertens or Mellin remainder before the Farey map. If a future proof of (1) discards that physical structure and reduces entirely to generic Möbius cancellation, the ownership rule in the line README should still move that part to `mobius_cancellation`.

## Net effect

The live gate is narrower than “prove some good remainder heights.” Under RH and within the FD-292 intersection route, an inverse-polylogarithmic occupation certificate requires a **near-linear population of remainder-good zero gaps**, while the phase-sparsity theorem itself is too coarse to be localized gap by gap. The next substantive step must therefore be a genuinely aggregate remainder-good occupation/population theorem, or a new mechanism coupling phase and remainder at zero-gap scale.