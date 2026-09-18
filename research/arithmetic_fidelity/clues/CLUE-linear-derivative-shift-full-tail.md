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

AF-421 resolves the missing signed organization throughout the finite-`tau` window. If `b_n->b in (0,infinity)`, the exponentially leading partition families are exactly packets around full-height rectangles `(r^n)`, with rates

\[
L_r(b)=\frac{b^r}{(r!)^2}.
\]

Away from the square transition values `b=1,4,9,...`, one packet with `r=floor(sqrt(b))` dominates and carries the same residual Schur-Cauchy factor `exp(-a e^2)`. Thus every non-square superthreshold value `b>1` gives genuine signed divergence rather than hidden cancellation back to the fixed-partition candidate.

At `b=m^2`, only the adjacent packets `r=m-1,m` tie on the exponential scale. Their exact amplitude ratio is

\[
F_{n,m}
=
\left(\frac{a}{n^2}\right)^n
\left(\frac{n+m}{m}\right)^{s_n-1}
\frac{\zeta(2(n+m))}{\zeta(2m)}
\left(\frac{2(n+m)-1}{2m-1}\right)^2.
\]

For even `n` their signs agree. For odd `n` they oppose, so only a finer regime with `F_{n,m}` sufficiently close to `1` can still support leading cancellation. The first square is already closed on the exact sequence `s_n=2n,a=1`: the complete signed sector diverges linearly with parity-alternating sign.

## Decisive test

The finite-`tau` problem is now reduced to the **square-transition fibers**

\[
b=m^2,\qquad m\ge1,
\]

and specifically to the odd-`n` subregimes where the adjacent-packet ratio `F_{n,m}` approaches `1` closely enough that their leading terms can cancel.

Derive the next asymptotic scale of `F_{n,m}` under `b_n->m^2`. Determine whether the two leading packets:

1. have an explicit nonzero residual after cancellation;
2. require a third packet or a near-full-column packet at the same next order; or
3. can genuinely recover the fixed-partition exponential under a fine-tuned derivative-depth sequence.

For `m=1`, retain AF-421's next coordinate

\[
\Gamma_n=n\,b_n^n,
\]

which already classifies whether the one-full-column packet vanishes, stays finite, or dominates inside the `b_n->1` layer.

Separately, for genuinely supercritical ratios `sigma>2`, AF-418 still rules out absolute control but AF-421 does not apply because `b_n` no longer has a finite limit. Determine the correct growing full-column saddle there rather than extrapolating the finite-window classification.

## Downstream gate

Only after the exceptional-`1` signed sector is controlled at the remaining square-transition fibers and in the genuinely supercritical derivative-depth regime should AF-416's omitted-`1` and one-/zero-singular-block estimates be revisited for growing `s_n`. Their fixed-shift negligibility cannot be assumed.

## Research disposition

Accepted. AF-419 resolves all strictly subcritical derivative ratios. AF-420 resolves the finite-`tau` absolute subthreshold phase. AF-421 then resolves the signed finite-window problem away from the discrete square transitions and closes the exact first boundary `s_n=2n,a=1` by proving parity-alternating linear divergence. The live finite-window question is now only the finer odd-`n` cancellation problem at `b=m^2`; the genuinely supercritical `sigma>2` regime remains separate.
