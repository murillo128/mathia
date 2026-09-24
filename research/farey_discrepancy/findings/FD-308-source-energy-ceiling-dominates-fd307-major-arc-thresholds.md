# FD-308 — Source-energy ceiling dominates the FD-307 major-arc thresholds

- **Date:** 2026-09-24
- **Status:** proved threshold-dominance audit and corrected the nonvacuous spectral frontier
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** block-Mertens source ceiling / Fejér low-pass witness / threshold dominance / vacuity audit / spectral frontier
- **Depends on:** FD-300, FD-304, FD-307
- **Classification:** `EXACT-DERIVED + THRESHOLD-DOMINANCE + VACUITY-AUDIT + FRONTIER-CORRECTION + ROUTE-REDUCTION`

## Claim

Let

\[
c:=1-\log_2(3/2)=0.4150374992\ldots
\tag{1}
\]

and retain the near-capacity premise used throughout FD-300--FD-307,

\[
L_N(x)\ge N^{1/2}x^{1+c-o(1)},
\qquad
x=N^{\lambda+o(1)}.
\tag{2}
\]

FD-300 already gives an unconditional source-energy ceiling

\[
\boxed{
\lambda\le \lambda_{\rm src}:=\frac1{2c}
=1.2047104198\ldots
}
\tag{3}
\]

for any capacity-bearing block-Mertens shell. The new observation is that the later **principal-major-arc selection** and **deep-capacity exclusion** thresholds of FD-307 lie entirely above this source ceiling once the RH shell floor of FD-304 is imposed.

Indeed, under RH write

\[
Q=x^{\rho+o(1)}.
\tag{4}
\]

FD-304 gives

\[
\rho\ge2c.
\tag{5}
\]

FD-307 localizes its Fejér witness to a rational major arc only when

\[
\lambda>
\lambda_{\rm loc}(\rho)
:=
\frac{37}{90c-12\rho},
\tag{6}
\]

and then obtains a principal-arc contradiction only when

\[
\lambda>
\lambda_{\rm kill}(\rho)
:=
\frac{41}{90c-16\rho}.
\tag{7}
\]

But (5) implies

\[
\boxed{
\lambda_{\rm loc}(\rho)
\ge
\frac{37}{66c}
=1.3507359253\ldots
>
\lambda_{\rm src},
}
\tag{8}
\]

and

\[
\boxed{
\lambda_{\rm kill}(\rho)
\ge
\frac{41}{58c}
=1.7032112832\ldots
>
\lambda_{\rm src}.
}
\tag{9}
\]

Therefore there is **no polynomial-depth regime in which the near-capacity premise remains feasible under FD-300 and the FD-307 principal-major-arc or kill hypotheses are simultaneously active**. Those implications remain mathematically valid, but they do not further shrink the live capacity region.

The same audit shows that the FD-307 shell-squeezing lower bound

\[
\rho\ge
\frac{90c-41/\lambda}{16}
\tag{10}
\]

is also nonbinding throughout the source-live range (3): there its right side is at most `c/2`, whereas FD-304 already gives `rho>=2c`.

What remains genuinely nonvacuous from FD-307 is its **Fejér low-pass spectral certificate**. In the common-window regime

\[
\boxed{
\frac{3}{10c}
=0.7228262519\ldots
<\lambda
\le
\frac1{2c}
=1.2047104198\ldots,
}
\tag{11}
\]

near-capacity still forces a fixed-block Möbius Fourier witness `alpha_*` satisfying

\[
\|\alpha_*\|_{\mathbb T}
\le
N^{-1/4-(3c/2)\lambda+o(1)}
\tag{12}
\]

and

\[
|F_X(\alpha_*)|
\ge
X^{1/2}
N^{(9c/4)\lambda-5/8-o(1)}.
\tag{13}
\]

Thus the corrected spectral frontier is not the already-subsumed deep `q=1` exclusion of FD-307. It is to rule out the low-frequency witness (12)--(13) **inside the live interval (11)**, especially near balanced depth `lambda=1`.

## 1. FD-300 closes all depths above `1/(2c)` before spectral localization

FD-300 shows that (2) forces a dyadic denominator shell `Q<q<=2Q` with

\[
E_Q
:=
\frac1Q
\sum_{Q<q\le2Q}|U_N(q)|^2
\ge
N x^{2c-o(1)},
\tag{14}
\]

where

\[
U_N(q)=M(Nq)-M(N(q-1))
=\sum_{r=1}^{N}\mu(N(q-1)+r).
\tag{15}
\]

The block contains exactly `N` coefficients of modulus at most one, so deterministically

\[
|U_N(q)|\le N
\tag{16}
\]

and hence

\[
E_Q\le N^2.
\tag{17}
\]

Combining (14) and (17) gives

\[
x^{2c-o(1)}\le N.
\tag{18}
\]

With `x=N^(lambda+o(1))`, this is

\[
2c\lambda\le1,
\tag{19}
\]

which proves (3). This uses neither RH nor any external estimate for Möbius cancellation. It is simply the finite support ceiling of a length-`N` block after the exact FD-300 capacity reduction.

Consequently any later argument derived from the same premise (2) can improve the capacity region only if it produces a contradiction at some

\[
\lambda\le\frac1{2c}.
\tag{20}
\]

A threshold strictly above (20) may still describe a correct conditional implication, but it cannot be the first obstruction along this route.

## 2. The FD-307 major-arc threshold is already beyond the source ceiling

FD-307 works under RH with a carrying shell

\[
Q=x^{\rho+o(1)}.
\tag{21}
\]

FD-304 supplies the shell floor

\[
\rho\ge2c.
\tag{22}
\]

The localization threshold (6) is increasing in `rho`, because its denominator decreases as `rho` grows. Therefore its smallest possible value on the RH-admissible shell range occurs at `rho=2c`:

\[
\lambda_{\rm loc}(\rho)
\ge
\lambda_{\rm loc}(2c)
=
\frac{37}{90c-24c}
=
\frac{37}{66c}.
\tag{23}
\]

Its ratio to the source ceiling is exact:

\[
\frac{37/(66c)}{1/(2c)}
=
\frac{37}{33}
>1.
\tag{24}
\]

Equivalently,

\[
\frac{37}{66c}-\frac1{2c}
=
\frac{2}{33c}
=0.1460255054\ldots .
\tag{25}
\]

Thus the step in FD-307 that invokes the Vinogradov minor-arc ceiling to force the witness onto a rational major arc can never be reached while (2) remains compatible with FD-300.

The same comparison is stronger for the principal-arc kill threshold. Again its minimum on `rho>=2c` occurs at `rho=2c`:

\[
\lambda_{\rm kill}(\rho)
\ge
\lambda_{\rm kill}(2c)
=
\frac{41}{58c}.
\tag{26}
\]

Now

\[
\frac{41/(58c)}{1/(2c)}
=
\frac{41}{29}
>1,
\tag{27}
\]

and

\[
\frac{41}{58c}-\frac1{2c}
=
\frac{6}{29c}
=0.4985008634\ldots .
\tag{28}
\]

So both the shallow-shell exclusion `lambda>1.703211...` and the shell-uniform FD-307 exclusion `lambda>1.920071...` are strictly weaker, as capacity exclusions, than the unconditional FD-300 source ceiling `lambda>1.204710...`.

This does **not** invalidate either calculation in FD-307. It changes their programmatic status: they are correct implications in a parameter range where the common antecedent (2) has already been ruled out upstream.

## 3. The FD-307 shell squeeze is nonbinding in the live range

After its principal-major-arc comparison, FD-307 rewrites survival as

\[
\rho
\ge
\frac{90c-41/\lambda}{16}.
\tag{29}
\]

Suppose now that the source premise is still live, so that (3) holds. Then

\[
\frac1\lambda\ge2c,
\qquad
\frac{41}{\lambda}\ge82c.
\tag{30}
\]

Therefore

\[
\frac{90c-41/\lambda}{16}
\le
\frac{8c}{16}
=
\frac c2.
\tag{31}
\]

But FD-304 already gives

\[
\rho\ge2c,
\tag{32}
\]

and

\[
2c>\frac c2.
\tag{33}
\]

Hence (29) never strengthens the existing shell floor anywhere in the source-live range. The apparent progressive squeeze toward `rho=1` only starts after `lambda` has crossed the earlier FD-300 impossibility threshold.

This is useful for route selection: improving the present argument by optimizing the constants inside (6), (7), or (29) is not enough unless the resulting threshold is pushed all the way below `1/(2c)`.

## 4. The genuinely live output of FD-307 is the low-pass witness

The first half of FD-307 does activate below the source ceiling. Its fixed-block Fourier representation and Fejér localization require only

\[
\lambda>rac{3}{10c}
=0.7228262519\ldots,
\tag{34}
\]

which overlaps substantially with (3). Intersecting the two conditions gives exactly the live interval (11).

At balanced depth

\[
\lambda=1,
\tag{35}
\]

FD-307 therefore supplies

\[
\boxed{
\|\alpha_*\|_{\mathbb T}
\le
N^{-0.8725562489\ldots+o(1)}
}
\tag{36}
\]

and

\[
\boxed{
|F_X(\alpha_*)|
\ge
X^{1/2}
N^{0.3088343734\ldots-o(1)}.
}
\tag{37}
\]

Under RH the carrying shell satisfies

\[
2c\le\rho\le1,
\qquad
X=NQ=N^{1+\rho+o(1)}.
\tag{38}
\]

Thus (37), expressed purely as a power of `X`, lies between

\[
X^{0.6544171867\ldots-o(1)}
\quad\text{and}\quad
X^{0.6687550366\ldots-o(1)},
\tag{39}
\]

while (36) localizes the frequency to a neighborhood between the scales

\[
X^{-0.4362781245\ldots+o(1)}
\quad\text{and}\quad
X^{-0.4767871533\ldots+o(1)}.
\tag{40}
\]

These calibrations explain why the FD-306 Vinogradov minor-arc ceiling at `X^(4/5)` cannot currently force major-arc membership in the balanced live regime: the necessary Farey spike is only at roughly `X^0.65--X^0.67`. The gap is a fixed power, not a logarithmic loss that can be recovered by bookkeeping.

Accordingly, the next spectral target should be one of the following equivalent kinds of strengthening: a Möbius additive bound tailored to the much narrower low-frequency neighborhood (36), a source-side improvement that lowers the forced capacity scale before Fourier localization, or a new structural input that upgrades the amplitude in (37). Re-running the existing general minor-arc comparison cannot reach `lambda=1` without a genuinely stronger exponent.

## 5. Adversarial audit, scope, and prior-art boundary

The threshold comparisons above are exact algebraic consequences of previously established findings. The audit uses the **same near-capacity antecedent** (2) throughout; it does not compare unrelated regimes or replace one notion of capacity with another. The FD-300 ceiling is unconditional, so adding RH later cannot reopen `lambda>1/(2c)`. The FD-304 shell floor is used only to minimize the FD-307 shell-dependent thresholds over the shell range where FD-307 itself operates.

No assertion is made that FD-307 is false. Its Fejér identity, low-pass localization, principal-major-arc implication, and principal-arc estimate remain intact. What is corrected is the significance of its last two thresholds for the active Farey route: the principal-major-arc and kill branches have empty intersection with the parameter region not already excluded by FD-300.

The finding also does not close the balanced regime. At `lambda=1`, (36)--(37) remain a genuine necessary spectral anomaly, and no existing result invoked in this line has yet been shown to exclude it. In particular, replacing the `X^(4/5)` general minor-arc ceiling by the mere knowledge that Möbius has logarithmic cancellation is far too weak for the polynomial gap in (39).

This is an internal threshold-dominance audit rather than an external number-theory theorem. No new literature result is load-bearing, so `SOURCES.md` requires no update. The useful novelty is programmatic: it removes a vacuous branch from the current frontier and identifies the exact nonvacuous interval in which the FD-307 low-pass certificate still needs to be attacked.

## Conclusion

The current capacity route has two nested gates. FD-300 already eliminates every fixed polynomial depth

\[
\lambda>1.2047104198\ldots,
\tag{41}
\]

before any additive Fourier argument is needed. FD-307 contributes new live information only on

\[
0.7228262519\ldots
<\lambda
\le
1.2047104198\ldots,
\tag{42}
\]

where it forces a low-frequency Möbius Fourier spike but does not yet place that spike on a classical major arc.

The corrected frontier is therefore to exclude that low-pass certificate inside (42), with `lambda=1` as the central calibration point. The later FD-307 `q=1` major-arc and deep-kill thresholds are correct but already subsumed by the earlier source-energy ceiling and should not be treated as progress on the live capacity region.