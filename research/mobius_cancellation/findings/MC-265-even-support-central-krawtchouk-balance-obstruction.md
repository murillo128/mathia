# MC-265 — Perfect first-order shell balance is still too coarse on even fixed-weight Krawtchouk layers

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the notation and exact Krawtchouk expansion of `MC-264`. Let

\[
\kappa_t(d;N):=\frac{K_t(d;N)}{\binom Nt},
\]

where

\[
K_t(d;N)=\sum_{a=0}^t(-1)^a\binom da\binom{N-d}{t-a}.
\]

For the shell-signature distance

\[
d_y(u,v)=\#\left\{r\in\mathcal R_y:\left(\frac{uv}{r}\right)=-1\right\},
\]

`d_y(u,v)\approx N_y/2` is the strongest possible **first-order sign-balance statement** for the product character `r\mapsto (uv/r)`: approximately half the shell primes give each sign.

That information is nevertheless parametrically too coarse for the termwise route to the high-moment estimate proposed in `MC-264`.

Write

\[
N=2M+\varepsilon,\qquad \varepsilon\in\{0,1\},
\qquad d_*=M=\lfloor N/2\rfloor.
\]

The standard Krawtchouk generating function gives exactly

\[
(1-z)^{d_*}(1+z)^{N-d_*}
=(1-z^2)^M(1+z)^\varepsilon.
\tag{1}
\]

Hence for every even weight `t=2j`,

\[
\boxed{
K_{2j}(d_*;N)=(-1)^j\binom Mj,
}
\tag{2}
\]

and therefore

\[
\boxed{
|\kappa_{2j}(d_*;N)|
=\frac{\binom{\lfloor N/2\rfloor}{j}}{\binom N{2j}}.
}
\tag{3}
\]

When `t^2=o(N)`, Stirling and the falling-factorial expansion give

\[
\boxed{
|\kappa_t(d_*;N)|
=\exp\!\left[-\frac t2\log\frac Nt+O(t)\right]
=(\sqrt2+o(1))\left(\frac{t}{eN}\right)^{t/2}.
}
\tag{4}
\]

Thus even **perfect shell balance** leaves an even-order without-replacement parity correlation of scale roughly `(t/N)^(t/2)`. It does not make the fixed-weight Fourier/Krawtchouk layer pointwise negligible at the scale needed by `MC-264`.

To see the mismatch precisely, let `m=t+1` and keep the tensor coefficients `c_{m,y}(u)` and their quadratic mass

\[
D_{m,y}=\sum_u c_{m,y}(u)^2
\]

from `MC-264`. Since `c_{m,y}(u)` counts ordered `m`-tuples,

\[
\sum_u c_{m,y}(u)=k_y^m.
\tag{5}
\]

Dividing the exact identity of `MC-264` by the shell-family size gives

\[
\frac{S_{2m,y}(t)}{\binom{N_y}{t}}
=
D_{m,y}
+\sum_{u\ne v}c_{m,y}(u)c_{m,y}(v)
\kappa_t(d_y(u,v);N_y).
\tag{6}
\]

Suppose one tries to prove the candidate estimate

\[
S_{2m,y}(t)\le L_y\binom{N_y}{t}D_{m,y}
\tag{7}
\]

using only a uniform pointwise kernel bound

\[
|\kappa_t(d_y(u,v);N_y)|\le\eta_y
\qquad(u\ne v)
\tag{8}
\]

followed by absolute values. Equations `(5)`--`(6)` then give only

\[
\frac{S_{2m,y}(t)}{\binom{N_y}{t}}
\le
D_{m,y}+\eta_y\bigl(k_y^{2m}-D_{m,y}\bigr).
\tag{9}
\]

So this proof class needs, up to the harmless distinction between `L_y` and `L_y-1`,

\[
\eta_y\lesssim L_y\frac{D_{m,y}}{k_y^{2m}}.
\tag{10}
\]

But `MC-264` proves, uniformly for `m=O(\log\log y)`,

\[
\frac{D_{m,y}}{k_y^{2m}}
=\exp\!\left[-m\log\frac{k_y}{m}+O(m)\right].
\tag{11}
\]

At the live support scale

\[
t=\left(\frac1{\log2}+o(1)\right)\log\log y,
\qquad m=t+1,
\qquad N_y\asymp k_y\asymp\frac y{\log y},
\tag{12}
\]

the perfectly balanced even-layer value `(4)` satisfies

\[
\log\frac{|\kappa_t(d_*;N_y)|}{D_{m,y}/k_y^{2m}}
=
\left(\frac12+o(1)\right)t\log\frac{k_y}{t}.
\tag{13}
\]

Consequently

\[
\boxed{
\frac{|\kappa_t(d_*;N_y)|}{D_{m,y}/k_y^{2m}}
=\left(\frac{k_y}{t}\right)^{t/2+o(t)},
}
\tag{14}
\]

a super-polynomial factor in `y` at `(12)`. In particular, multiplying the desired right side `(10)` by any fixed power `L_y=y^{O(1)}` still does not bridge the gap.

Therefore a route that proves only that every off-diagonal product character has nearly zero **first-order shell bias** and then bounds the Krawtchouk expansion term by term cannot reach the support-matched high-moment estimate of `MC-264`. The missing arithmetic information must control the **signed aggregate distance distribution** at Krawtchouk order `t`, or force the relevant distances into a much smaller neighborhood of Krawtchouk zeros with enough uniformity to survive the coefficient weights.

This is a proof-method obstruction, not a lower bound for the actual arithmetic moment `(6)`. The off-diagonal Krawtchouk terms can cancel, and such cancellation is precisely the surviving possibility.

## 1. The central value is an exact finite-population effect

For a sign vector with exactly `M` minus signs among `N=2M+\varepsilon` coordinates, choosing a uniformly random `t`-subset without replacement gives

\[
\mathbb E\prod_{r\in T}\sigma_r
=\kappa_t(M;N).
\tag{15}
\]

Thus `(2)`--`(4)` have a direct probabilistic interpretation. Exact first-order balance says the population mean of the signs is zero up to the unavoidable one-coordinate discrepancy when `N` is odd. It does **not** make products of an even number of sampled coordinates independent. Sampling without replacement leaves a deterministic parity correlation, and `(3)` is its exact magnitude.

For `N` even, odd Krawtchouk layers vanish exactly at the center because `(1-z^2)^{N/2}` contains only even powers. This does not remove the obstruction: generation must exclude blind relations on even support layers as well. For odd `N`, the extra `(1+z)` in `(1)` also gives nonzero nearest-center odd coefficients, but no odd-layer estimate is needed for the present no-go.

The point is therefore not that a balanced sign vector is unusually bad. The nonzero even coefficient is the **universal finite-population correction at perfect balance**.

## 2. Why this is stronger than the low-moment obstruction

`MC-263` showed that a natural second moment cannot detect one isolated blind subset. `MC-264` then showed that increasing the moment to `2(t+1)` removes that single-atom counting barrier: at the natural tensor diagonal scale, one blind atom becomes visible with substantial room for analytic loss.

The present result identifies a different bottleneck **inside a possible proof of that stronger estimate**. The high-moment amplification is quantitatively sufficient, but a first-order pseudorandomness theorem for the shell signatures is not. Even at the ideal first-order balance point, the order-`t` Krawtchouk coefficient is exponentially larger than the pointwise scale that a triangle-inequality proof of `(7)` would need.

So the frontier cannot be reduced to “prove every Legendre product character is balanced on the shell.” It must retain at least one further layer of structure: a signed distribution theorem for the distances `d_y(u,v)`, an association-scheme/Fourier cancellation mechanism across the weighted pair family, or a direct high-moment argument that never absoluteizes those off-diagonal terms separately.

## 3. Prior art and novelty boundary

No novelty is claimed for Krawtchouk polynomials, their generating function, the central/nearest-central evaluation `(2)`, hypergeometric sampling without replacement, or the fact that zero first moment does not imply higher-order independence. The Krawtchouk/Hamming-scheme framework and the fixed-weight transform were already audited in `MC-264`, including the standard generating-function identity and coding-theory literature.

A targeted literature check through 13 September 2026 confirms that the generating-function formula is standard; NIST DLMF §18.23.3 records the classical Krawtchouk generating function, and the Hamming-sphere literature treats Krawtchouk values as the fixed-weight Fourier transform. This finding does not claim any new special-function identity.

The durable Mathia delta is the scale comparison `(13)`--`(14)`: the **ideal first-order balance value itself** is super-polynomially too large for a pointwise-absolute-value proof of the exact support-matched moment estimate isolated in `MC-264`. That comparison narrows the live analytic target from generic shell balance to signed high-order distance-distribution control.

## 4. Boundaries and falsification tests

- **Not a lower bound for `S_{2m,y}(t)`.** Equation `(9)` is an upper bound obtained by absoluteizing the off-diagonal sum. Large individual Krawtchouk values may cancel in the actual arithmetic sum.
- **Not a claim about actual distances.** The argument does not assert that the Legendre-signature distances equal `\lfloor N_y/2\rfloor`; it shows that knowing only first-order balance cannot supply the pointwise decay required by this proof class.
- **Even support is enough for the obstruction.** The exact central odd-layer behavior is different, but a generation proof must also eliminate even-weight blind relations in the live range.
- **Krawtchouk-root localization is not ruled out.** A much stronger arithmetic theorem could force weighted pair mass near zeros of `K_t`, rather than merely near Hamming center. That would evade this no-go and is a concrete surviving possibility.
- **Signed association-scheme cancellation is not ruled out.** Any method that uses the signed distance distribution before taking absolute values lies outside `(8)`--`(10)`.
- **No RH-scale conclusion.** No blind relation is excluded, no estimate `(7)` is proved, and no improved bound for `M(X)` follows.

## Consequence for the research line

`MC-264` remains the quantitative high-moment exit: moment order `2(t+1)` is sufficient to make a single blind support detectable if the sparse-shell moment can be controlled near its natural diagonal scale. `MC-265` shows that **pairwise shell balance is not the missing theorem**. The fixed-weight transform remembers even-order finite-population dependence at a scale far above the diagonal target.

The next useful analytic object is therefore the weighted signed distribution

\[
\sum_{u,v}c_{m,y}(u)c_{m,y}(v)K_t(d_y(u,v);N_y),
\]

not merely individual estimates for `d_y(u,v)-N_y/2`. A successful route must exploit cancellation or rigidity of that full distribution; a failed attempt to do so would give a substantially sharper reason why the high-moment escape itself cannot close the shell-generation gap.