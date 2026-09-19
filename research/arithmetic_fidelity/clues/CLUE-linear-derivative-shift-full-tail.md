---
id: CLUE-linear-derivative-shift-full-tail
type: research-clue
status: accepted
origin: research-watch
target_line: arithmetic_fidelity
based_on:
  - research/arithmetic_fidelity/findings/AF-417-linear-derivative-shift-renormalizes-left-tail-plancherel-sectors.md
  - research/arithmetic_fidelity/findings/AF-418-full-height-rectangles-expose-sigma-2-absolute-tail-transition.md
  - research/arithmetic_fidelity/findings/AF-419-subcritical-linear-shifts-admit-uniform-full-tail-resummation.md
  - research/arithmetic_fidelity/findings/AF-420-critical-derivative-window-has-sharp-subthreshold-absolute-resummation-domain.md
  - research/arithmetic_fidelity/findings/AF-421-finite-critical-windows-reduce-to-full-column-saddle-hierarchy.md
  - research/arithmetic_fidelity/findings/AF-422-square-transition-detuning-controls-adjacent-packet-cancellation.md
  - research/arithmetic_fidelity/findings/AF-423-adjacent-residual-packets-have-universal-inverse-n-drift.md
  - research/arithmetic_fidelity/findings/AF-424-complete-square-packet-cancellation-has-explicit-derivative-offset-detuning.md
---

# Linear derivative-shift full-tail resummation

## Question

AF-417 proves that if `s_n/n -> sigma` and `x=c/n`, every fixed excess degree in the exceptional-`1` Cauchy--Binet sector is renormalized by `e^{sigma d}`. The resulting degree-by-degree coefficients are exactly those of

\[
\exp\!\left(-\frac{e^\sigma c^2}{4\pi^2}\right).
\]

Does the **complete signed** exceptional-`1` partition sector satisfy the locally uniform limit

\[
\frac{D_{n+1,\,1\in A}^{(s_n)}(c/n)}{E_n^{(s_n)}(c/n)}
\longrightarrow
\exp\!\left(-\frac{e^\sigma c^2}{4\pi^2}\right)
\]

for finite `sigma>=0`, uniformly for `c` in compact subsets of `(0,\infty)`? If not, what additional large-partition scaling data control the limit?

## Why this is nontrivial

AF-415 proves the corresponding full resummation only for a fixed derivative shift. Its absolute Schur domination uses an excess-degree bound whose constant depends on `s`. When `s_n` grows linearly with `n`, the factor

\[
\prod_i(k_i/i)^{s_n-1}
\]

cannot be replaced over the whole partition range by an `n`-independent constant to `|lambda|` using the fixed-shift argument. AF-417 therefore establishes the candidate limit only degree by degree.

AF-418 shows that this is a genuine large-partition obstruction rather than only a missing estimate. For every fixed `r>=1`, the full-height rectangle `lambda=(r^n)` has an exact normalized magnitude whose leading exponent is

\[
\frac1n\log C_{n,r}
=
r\left(\frac{s_n}{n}-2\right)\log n
+r\log\!\left(\frac{c^2}{4\pi^2}\right)
-\frac{s_n}{n}\log(r!)+o(1).
\]

Hence AF-415-style absolute domination is impossible for `sigma>2`. At `sigma=2`, the growing rectangle retains the finer scale

\[
\left(\frac{s_n}{n}-2\right)\log n,
\]

which is invisible to every fixed partition.

AF-419 closes the strictly subcritical branch. If `limsup s_n/n<2`, a column-height split plus Pieri's rule gives a shape-uniform absolute majorant and the complete exceptional-`1` sector converges to the fixed-degree candidate.

AF-420 penetrates the critical window itself. With

\[
a=\frac{c^2}{4\pi^2},
\qquad
b_n(a)=a\,n^{s_n/n-2},
\]

if `s_n/n -> 2` and `limsup b_n(A)<1`, the full sector converges uniformly on `0<=a<=A` to `exp(-a e^{s_n/n})`. If

\[
\tau_n=\left(\frac{s_n}{n}-2\right)\log n\to\tau,
\]

this gives the exact absolute subthreshold domain `a<e^{-tau}`. Conversely, for `a e^tau>1` the single full-height column grows exponentially; on `s_n=2n`, the boundary `a=1` already gives a linearly growing full-height term.

AF-421 resolves the missing signed organization throughout the finite-`tau` window. If `b_n->b in (0,infinity)`, the exponentially leading partition families are full-column packets around `(r^n)`, with rates

\[
L_r(b)=\frac{b^r}{(r!)^2}.
\]

Away from the square transition values `b=1,4,9,...`, one packet with `r=floor(sqrt(b))` dominates. At `b=m^2`, only the adjacent packets `r=m-1,m` tie on the exponential scale; even `n` reinforces them, while odd `n` can cancel only through their exact amplitude ratio `F_{n,m}`.

AF-422 resolves the next rectangle-amplitude scale. Writing `s_n=2n+d_n`, define

\[
\Xi_{n,m}
=
\log n
+n\log\!\left(\frac{b_n}{m^2}\right)
-d_n\log m
\]

and

\[
K_m
=
\frac{4m e^{2m}}{(2m-1)^2\zeta(2m)}.
\]

Then

\[
F_{n,m}=K_m e^{\Xi_{n,m}}(1+o(1)).
\]

Therefore every even square-transition subsequence is closed, and every odd subsequence is closed unless

\[
\Xi_{n,m}\to-\log K_m.
\]

For `m>=2`, all non-tuned square-transition regimes diverge exponentially. On the natural exact-square path `a=m^2, s_n=2n`, one has `F_{n,m}~K_m n`, so the `m`-column packet dominates for every `m`; `m=1` recovers AF-421's explicit linear boundary result.

AF-423 resolves the first complete-packet correction on that remaining interface. The residual packets satisfy

\[
\log\frac{G_{n,m}}{G_{n,m-1}}
=
\frac{2ae^2}{n}+o(n^{-1}),
\]

so `F_{n,m}->1` still leaves a deterministic inverse-`n` packet asymmetry. First packet-level cancellation additionally requires `n log F_{n,m}->-2ae^2`.

AF-424 translates that implicit condition back into the source detuning and retains the varying derivative depth before sending it to zero. With `alpha_n=d_n/n`, it proves

\[
\log\frac{G_{n,m}}{G_{n,m-1}}
=
\frac{a e^{2+\alpha_n}(2+\alpha_n)}{n}+O(n^{-2})
\]

and, for `Q_{n,m}=F_{n,m}G_{n,m}/G_{n,m-1}`,

\[
\log Q_{n,m}
=
\Omega_{n,m}
+
\frac{-m^2+m-1-\frac12m^2\alpha_n+a e^{2+\alpha_n}(2+\alpha_n)}{n}
+O(n^{-2}),
\]

where

\[
\Omega_{n,m}=\Xi_{n,m}+\log K_m+m\alpha_n.
\]

Thus cancellation through the `n log Q` scale is equivalent to the explicit source-coordinate condition

\[
n(\Xi_{n,m}+\log K_m)+m d_n
\longrightarrow
m^2-m+1-2ae^2.
\]

For `a!=m^2`, the square condition also forces `alpha_n~log(m^2/a)/log n`, so the residual packet already contains a deterministic `1/(n log n)` scale before ordinary `1/n^2` corrections. The previous `n log F` condition had hidden this derivative-offset coordinate.

## Decisive test

The remaining finite-window problem is now the **odd square interface after AF-424's explicit complete-packet tuning**. Fix `m>=1`, assume `b_n->m^2`, and impose

\[
n(\Xi_{n,m}+\log K_m)+m d_n
\longrightarrow
m^2-m+1-2ae^2.
\]

Derive the next nonzero asymptotic of `Q_{n,m}-1`. If an `n^{-2}` or other polynomial-scale mismatch is forced by the admissible integer/source parameters, it still dominates every exponentially smaller neighboring saddle for `m>=2` and closes that tuned branch.

If successive polynomial coefficients can instead be tuned away, stop treating a formal power-series cancellation as evidence for recovery. Identify the first beyond-all-orders contribution to the complete packet ratio, including the residual tall-column sector suppressed in AF-423--AF-424, and compare it with the first subleading full-column saddle. The decisive scale is the one at which the residual of the two tied packets becomes comparable with the next exponential partition family.

For `m=1`, the same packet ratio laws apply but `Lambda_1=1`, so the polynomial boundary must be analyzed separately rather than imported from the `m>=2` exponential hierarchy.

Separately, for genuinely supercritical ratios `sigma>2`, AF-418 still rules out absolute control but AF-421--AF-424 do not apply because `b_n` no longer has a finite limit. Determine the correct growing full-column saddle there rather than extrapolating the finite-window classification.

## Downstream gate

Only after the exceptional-`1` signed sector is controlled on the fully tuned packet-level square interface and in the genuinely supercritical derivative-depth regime should AF-416's omitted-`1` and one-/zero-singular-block estimates be revisited for growing `s_n`. Their fixed-shift negligibility cannot be assumed.

## Research disposition

Accepted. AF-419 resolves all strictly subcritical derivative ratios. AF-420 resolves the finite-`tau` absolute subthreshold phase. AF-421 reduces the signed finite-window problem to discrete square saddle collisions; AF-422 isolates the leading rectangle detuning; AF-423 exposes the first complete-packet inverse-`n` drift; AF-424 makes that cancellation interface explicit in the source variables and reveals the derivative-offset correction hidden by `alpha_n->0`. The live finite-window question is now the next nonzero term after AF-424's condition and, if polynomial tuning survives, the first exponentially small residual/tall-column scale at which a subleading saddle becomes competitive. The genuinely supercritical `sigma>2` regime remains a separate moving-saddle problem.