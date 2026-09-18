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

AF-422 now resolves the next scale of that ratio. Writing `s_n=2n+d_n`, define

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

## Decisive test

The remaining finite-window problem is now the **odd, packet-level tuned square interface**. Fix `m>=1`, assume

\[
b_n\to m^2,
\qquad
\Xi_{n,m}\to-\log K_m,
\]

and derive the first asymptotic difference between the complete residual packets attached to the two tied rectangles. Equivalently, determine the asymptotic of

\[
\frac{G_{n,m}}{G_{n,m-1}}
\]

at the precision at which `F_{n,m}->1`, and hence of the complete adjacent-packet ratio

\[
F_{n,m}\frac{G_{n,m}}{G_{n,m-1}}.
\]

Decide whether the tuned interface leaves a nonzero residual, exposes a still finer retained coordinate, recruits the next partition saddle, or can genuinely restore the fixed-partition exponential. Do not infer this from `F_{n,m}` alone: AF-422 proves only that its tuning is necessary for leading rectangle cancellation, not sufficient for complete-packet cancellation.

For `m=1`, AF-421's coordinate

\[
\Gamma_n=n\,b_n^n
\]

is the same transition scale in another form, since `Xi_{n,1}=log Gamma_n`; the unresolved cancellation fiber is the special tuning `Gamma_n->1/K_1` on odd `n`.

Separately, for genuinely supercritical ratios `sigma>2`, AF-418 still rules out absolute control but AF-421--AF-422 do not apply because `b_n` no longer has a finite limit. Determine the correct growing full-column saddle there rather than extrapolating the finite-window classification.

## Downstream gate

Only after the exceptional-`1` signed sector is controlled on the tuned packet-level square interface and in the genuinely supercritical derivative-depth regime should AF-416's omitted-`1` and one-/zero-singular-block estimates be revisited for growing `s_n`. Their fixed-shift negligibility cannot be assumed.

## Research disposition

Accepted. AF-419 resolves all strictly subcritical derivative ratios. AF-420 resolves the finite-`tau` absolute subthreshold phase. AF-421 reduces the signed finite-window problem to discrete square saddle collisions, and AF-422 resolves the next rectangle-amplitude scale: outside the odd tuning `Xi_{n,m}->-log K_m`, the square fibers are closed as well, with exponential divergence for `m>=2`. The live finite-window question is now only the complete-packet asymptotic on that fine-tuned odd interface. The genuinely supercritical `sigma>2` regime remains a separate moving-saddle problem.