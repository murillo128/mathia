---
id: WP-369
title: Power-law cusp sampling has a unique critical Whittaker scale that factorizes
branch: weil_positivity
status: supported
kind: index-adapted-whittaker-cusp-scale-trichotomy
claim_strength: exact power-law sampling trichotomy and critical-scale factorization for normalized Eisenstein Fourier-Whittaker modes
created: 2026-09-19
related: [WP-358, WP-363, WP-366, WP-367, WP-368]
clues: [CLUE-maass-selberg-remainder-sign-interface]
prior_art:
  - Henryk Iwaniec, Spectral Methods of Automorphic Forms, 2nd ed., AMS, 2002
  - NIST Digital Library of Mathematical Functions, 10.40.2, 10.45.7, and 10.30.3
  - Classical Kirillov/Whittaker realization of GL(2) automorphic Fourier coefficients
---

# WP-369 — Power-law cusp sampling has a unique critical Whittaker scale that factorizes

## Claim

`WP-368` left one explicit escape open: let the radial height approach the cusp origin as the arithmetic/Fourier index grows, instead of using one fixed source scale `Y>=Y_*>0`. For the normalized Fourier--Whittaker mode of the level-one Eisenstein family, that escape has a sharp scale transition.

Work with the standard normalized positive-index Whittaker coefficient

\[
w_{r,n}(Y)
=\lambda_r(n)\sqrt{Y}\,K_{ir}(2\pi nY),
\qquad
\lambda_r(n)=n^{ir}\sigma_{-2ir}(n).
\tag{1}
\]

A particular Eisenstein normalization may multiply every mode at fixed `r` by one common meromorphic scalar. Every `n`-scale statement below is unchanged by a finite nonzero common scalar; if that scalar vanishes at an exceptional parameter, the corresponding physical channel is simply null and cannot rescue the candidate.

For any index-adapted height `Y_n>0`, put

\[
t_n:=nY_n,
\qquad
\Psi_r(t):=\sqrt t\,K_{ir}(2\pi t).
\tag{2}
\]

Then there is an exact factorization

\[
\boxed{
 w_{r,n}(Y_n)
 =\lambda_r(n)n^{-1/2}\Psi_r(t_n).
}
\tag{3}
\]

Thus the critical `n^{-1/2}` scale is already the kinematic factor obtained when the Whittaker normalization `sqrt(Y)` is rewritten in the natural variable `nY`; all remaining finite--archimedean incidence is carried by the single profile `Psi_r(nY_n)`.

Now take the canonical power-law family

\[
Y_n=c\,n^{-\alpha},
\qquad c>0,\quad \alpha>0.
\tag{4}
\]

For fixed real `r`, the three regimes are:

\[
\boxed{
\begin{array}{ll}
0<\alpha<1:
& w_{r,n}(Y_n)
 =\frac12\lambda_r(n)n^{-1/2}
   e^{-2\pi c n^{1-\alpha}}
   \left(1+O_{r,c}(n^{-(1-\alpha)})\right),\\[1.2ex]
\alpha=1:
& w_{r,n}(Y_n)
 =B_r(c)\lambda_r(n)n^{-1/2},
 \quad B_r(c):=\sqrt c\,K_{ir}(2\pi c),\\[1.2ex]
\alpha>1,\ r\ne0:
& w_{r,n}(Y_n)=O_{r,c}\!\left(|\lambda_r(n)|n^{-\alpha/2}\right),\\[0.8ex]
\alpha>1,\ r=0:
& w_{0,n}(Y_n)=O_c\!\left(|\lambda_0(n)|n^{-\alpha/2}\log n\right).
\end{array}
}
\tag{5}
\]

On primes, `|lambda_r(p)|<=2`, so the comparison with the Weil finite-prime half-density is immediate. For `0<alpha<1` the formally correct `p^{-1/2}` prefactor is killed by stretched-exponential decay. For `alpha>1` the amplitude is `o(p^{-1/2})`. The **unique pure power-law scale with a non-exponentially-suppressed critical half-density is therefore**

\[
\boxed{Y_n\asymp n^{-1},\quad\text{and exactly }Y_n=c/n\text{ in the family (4).}}
\tag{6}
\]

But at that unique scale the candidate loses precisely the finite--archimedean incidence it was meant to preserve: `nY_n=c` is constant, so the Whittaker profile becomes one common archimedean scalar `B_r(c)` and the arithmetic index appears only through `lambda_r(n)n^{-1/2}`. If `B_r(c)=0`, the sampled channel is null; if `B_r(c)!=0`, the factorization is exact.

The most canonical positive readout of this sampled boundary, the ordinary translation-invariant `L^2(S^1)` norm of a finite Fourier packet, then gives

\[
\left\|
B_r(c)\sum_{1\le n\le X}
\frac{\lambda_r(n)}{\sqrt n}e(nx)
\right\|_{L^2(S^1)}^2
=
|B_r(c)|^2
\sum_{1\le n\le X}\frac{|\lambda_r(n)|^2}{n}.
\tag{7}
\]

The right side diverges as `X->infinity`. Indeed the classical Eisenstein Rankin--Selberg series is

\[
\sum_{n\ge1}\frac{|\lambda_r(n)|^2}{n^s}
=
\frac{\zeta(s)^2\zeta(s+2ir)\zeta(s-2ir)}{\zeta(2s)},
\tag{8}
\]

which has a double pole at `s=1` for `r!=0` and a fourth-order pole at `s=1` for `r=0`. Hence ordinary Hilbert positivity both **squares the half-density to `1/n`** and fails to give a finite global norm. Adding a desired `log n` or Mangoldt amplitude before squaring only worsens the diagonal growth and does not restore a linear Weil carrier.

So the power-law index-adapted escape left by `WP-368` closes in a precise way:

\[
\boxed{
\text{fixed/slow cusp approach}
\Rightarrow\text{Whittaker tail suppression};
\quad
Y_n=c/n
\Rightarrow\text{critical scale but exact separation};
\quad
\text{faster approach}
\Rightarrow\text{subcritical amplitude}.
}
\tag{9}
\]

This is independent of RH and uses no zero data.

**Classification:** `EXACT-DERIVED + NORMALIZED-WHITTAKER-MODE + INDEX-ADAPTED-CUSP-SCALE + POWER-LAW-TRICHOTOMY + UNIQUE-CRITICAL-SCALE + FINITE-ARCHIMEDEAN-FACTORIZATION + HILBERT-SQUARE-DIVERGENCE + MATCHED-CONTROL + NEGATIVE/NARROWING + CLASSICAL-BESSEL-INGREDIENT + NO-GRAND-NOVELTY-CLAIM`.

## 1. The exact `nY` reduction exposes what the cusp scale can and cannot carry

The standard Fourier expansion of the unitary-axis Eisenstein family has normalized nonconstant coefficients proportional, after removing a scalar common to all arithmetic indices, to

\[
\lambda_r(n)\sqrt Y\,K_{ir}(2\pi nY).
\tag{10}
\]

That common scalar is irrelevant to the arithmetic-index scale whenever finite and nonzero. If a chosen uncompleted normalization makes it vanish at a special spectral parameter, the entire corresponding physical Fourier channel vanishes rather than acquiring a different `n`-dependence. Equation (3) is then only the identity `sqrt(Y_n)=n^{-1/2}sqrt(nY_n)`, but it is structurally decisive for this research route.

The variable `nY` is the standard archimedean Whittaker/Kirillov scaling variable. Consequently an index-dependent sampling rule does not create a new independent finite-place weight and archimedean weight. It produces the universal half-density factor `n^{-1/2}` multiplied by the profile `Psi_r(t_n)`. To retain a nonvanishing critical-size envelope, the sequence `t_n=nY_n` must avoid both ends of the positive half-line, because

\[
\Psi_r(t)\longrightarrow0
\quad(t\to\infty)
\tag{11}
\]

exponentially, while

\[
\Psi_r(t)\longrightarrow0
\quad(t\to0^+)
\tag{12}
\]

for every fixed real `r`: for `r!=0`, `K_{ir}(x)` is bounded oscillatory at the origin, and for `r=0`, `K_0(x)=-\log x+O(1)`, so the extra `sqrt t` still drives the product to zero.

Thus any genuinely unsuppressed index-adapted route must live in the transition regime

\[
nY_n\asymp1.
\tag{13}
\]

This does not by itself close every possible non-power-law sampling. It does sharply identify the only regime in which one can even ask for a scale-free Weil comparison without adding an external renormalization.

## 2. The power-law trichotomy is forced by the two classical Bessel asymptotics

For `0<alpha<1`, the Whittaker argument

\[
2\pi nY_n=2\pi c n^{1-\alpha}
\tag{14}
\]

tends to infinity. The classical expansion

\[
K_{ir}(x)
=\sqrt{\frac{\pi}{2x}}e^{-x}
\left(1+O_r(x^{-1})\right)
\tag{15}
\]

gives

\[
\begin{aligned}
w_{r,n}(Y_n)
&=\lambda_r(n)\sqrt c\,n^{-\alpha/2}
 K_{ir}(2\pi c n^{1-\alpha})\\
&=\frac12\lambda_r(n)n^{-1/2}
 e^{-2\pi c n^{1-\alpha}}
 \left(1+O_{r,c}(n^{-(1-\alpha)})\right),
\end{aligned}
\tag{16}
\]

which proves the first line of (5). The cancellation of the powers of `n` down to `n^{-1/2}` is exact at leading order, but the stretched exponential makes that formal prefactor unusable as a global arithmetic half-density.

At `alpha=1`, the argument is exactly `2 pi c` for every index, giving the second line of (5) with no asymptotic approximation.

For `alpha>1`, the argument tends to zero. For fixed `r!=0`, the standard small-argument expansion of `K_{ir}` is an oscillatory bounded combination of `x^{ir}` and `x^{-ir}`, hence `K_{ir}(x)=O_r(1)`. For `r=0`, `K_0(x)=-log x+O(1)`. Substitution gives the last two lines of (5). On primes the boundedness of `lambda_r(p)` makes both estimates `o(p^{-1/2})`; on general integers `|lambda_r(n)|<=d(n)=n^{o(1)}`, so the same conclusion holds for each fixed `alpha>1`.

No analytic continuation in `r`, no zeta zero, and no regularization enters this trichotomy.

## 3. The unique critical power law freezes the incidence

The attractive feature of `WP-366` was literal nonseparability: at one common height `Y`, the archimedean function sees `nY`, so changing the arithmetic index changes the radial profile. The price, classified by `WP-368`, is exponential suppression at large `n` when `Y` remains bounded away from zero.

The power law `Y_n=c/n` removes exactly that suppression. But it does so by setting

\[
nY_n=c
\tag{17}
\]

for every `n`. Thus

\[
w_{r,n}(c/n)
=B_r(c)\frac{\lambda_r(n)}{\sqrt n},
\tag{18}
\]

which is a tensor separation of the sampled archimedean profile from the arithmetic sequence. The mechanism that generated finite--archimedean incidence in `WP-366` has been neutralized rather than converted into a global coupling.

This remains true even if `Y=c/n` is defended as representation-theoretically natural rather than chosen to fit the desired exponent: the naturality comes precisely from keeping the Kirillov/Whittaker coordinate `nY` fixed. That natural phase-space ray is a good way to expose the half-density, but it is not a source of mixed finite--archimedean curvature or an independent sign theorem.

A slowly varying rule `Y_n=t_n/n` with nonconstant `t_n` is not covered by this exact factorization into one common scalar. Equation (3) shows the burden such an escape must carry: the complete new incidence is the bounded modulation `Psi_r(t_n)`, so `t_n` itself must be source-forced independently of the desired Weil coefficients. Choosing it after inspecting prime or Gamma weights would merely encode the target in the sampling rule.

## 4. Canonical positivity at the critical scale squares and diverges

Define the finite sampled Fourier packet

\[
\mathcal T_{c,X}E_r(x)
:=
B_r(c)\sum_{1\le n\le X}
\frac{\lambda_r(n)}{\sqrt n}e(nx).
\tag{19}
\]

This is deliberately the most favorable diagonal control: the arithmetic half-density survives linearly before positivity is imposed. Parseval then gives (7) exactly.

For real `r`, `lambda_r(n)` is real, and the Ramanujan--Wilson/Rankin--Selberg identity specialized to the Eisenstein coefficients gives (8). At `s=1`, `zeta(s)^2` already forces divergence. For `r!=0`, the factors `zeta(1+/-2ir)` are finite and nonzero and `zeta(2)` is finite, so the pole is exactly order two. For `r=0`, (8) becomes `zeta(s)^4/zeta(2s)` and the pole is order four.

Thus the infinite sampled vector is not an `L^2(S^1)` boundary vector at the critical scale. More importantly for the Weil-positivity mandate, the finite-cutoff norm reads the **square** `|lambda_r(n)|^2/n`, not a linear `Lambda(n)/sqrt n` coefficient. This is the same carrier-versus-sign tension seen from a different geometry in `WP-358`: the operation with the clean Hilbert sign acts after the half-density has been squared.

One can of course insert extra positive Fourier multipliers that decay with `n`, subtract a divergent scalar, or introduce cross-index kernels. None is supplied by the bare sampled Whittaker boundary. Such a modification is a new candidate and must derive its weights and sign from source geometry before comparison with the Weil formula.

## 5. Matched controls and falsification attempts

**Fixed height.** `alpha=0` is the endpoint already controlled by `WP-368`: the Whittaker argument grows linearly and the arithmetic tail is exponentially erased. Equation (16) continuously extends that mechanism to every `0<alpha<1` as stretched-exponential suppression.

**Approach `alpha=1` from below.** The power prefactor is already `n^{-1/2}` for every `alpha<1`, so simply observing that exponent is misleading. The residual factor `exp(-2 pi c n^(1-alpha))` is decisive and cannot be absorbed into a scale-free Weil coefficient.

**Approach `alpha=1` from above.** Small-argument Whittaker behavior does not produce a compensating blow-up on the unitary axis. The factor `sqrt Y` wins, giving `n^{-alpha/2}` up to bounded oscillation, or one logarithm at `r=0`.

**Use the critical sampling but keep positivity only at finite cutoff.** The finite norm is perfectly positive, but its coefficient is `|lambda_r(n)|^2/n`. Letting the cutoff grow diverges, and retaining a cutoff leaves a cutoff-dependent positive approximation rather than a global Weil form.

**Insert `log n` to repair the finite-prime coefficient.** The sampled Whittaker geometry itself does not produce that derivative weight. If it is externally inserted in the amplitude, positivity produces `(log n)^2/n`, not the desired linear half-density. A source-defined differential operation could be a new route only if it acts before the square and remains tied to the same global sign theorem.

**Let `t_n=nY_n` vary inside a compact interval.** This is the main surviving escape and is outside the pure-power classification. It preserves the `n^{-1/2}` factor while retaining the bounded profile `Psi_r(t_n)`. It is not enough to choose an arbitrary sequence: the map `n -> t_n` must itself arise from Mathia/automorphic geometry, survive matched nonprime controls, and feed an independent positive global form without becoming an inserted arithmetic kernel.

## 6. Prior-art and novelty boundary

No novelty is claimed for the Eisenstein Fourier expansion, the Whittaker/Kirillov variable `nY`, either Bessel asymptotic, Parseval, or the Eisenstein Rankin--Selberg series. These are classical ingredients. NIST DLMF 10.40.2 supplies the large-argument `K` asymptotic; DLMF 10.45.7 records the small-argument imaginary-order behavior, with DLMF 10.30.3 covering the logarithmic `K_0` case. Standard automorphic references such as Iwaniec give the Fourier--Whittaker normalization used in (1).

A bounded literature audit around Kirillov/Whittaker scaling, Fourier coefficients sampled near shrinking cusps/horocycles, and small-scale automorphic equidistribution confirms that the `nY` scaling itself is standard representation-theoretic structure. It did not surface a theorem presented as the specific Weil-positivity route obstruction above. That is not a historical novelty proof.

The line-specific contribution is the exact stress test of the escape left by `WP-368`: after retaining the normalized physical `sqrt Y` Whittaker factor and allowing arithmetic-index-dependent power-law heights, the full family has one and only one unsuppressed critical power scale, and that scale is exactly the one on which `nY` becomes constant and the finite--archimedean Whittaker incidence separates. The inherited positive boundary norm then squares the half-density and diverges.

## 7. Consequence for the Weil-positivity frontier

`WP-366` showed that averaging the genuinely mixed `nY` Whittaker geometry over all scales with a dilation-covariant positive scalar form Mellin-separates back to Rankin--Selberg. `WP-367` extended that separation to arbitrary common homogeneous positive radial forms. `WP-368` showed that bounded common positive geometry at a source-fixed height bounded away from zero exponentially erases large arithmetic indices.

The present result closes the simplest remaining repair: **move the source height toward zero by a pure arithmetic power law.** The only exponent that keeps the normalized Fourier--Whittaker mode at the unsuppressed critical half-density is `Y_n=c/n`, and there the supposedly mixed archimedean coordinate is frozen. Ordinary boundary Hilbert positivity then returns a divergent Rankin--Selberg square rather than the linear Weil carrier.

A surviving Whittaker route must therefore add genuinely new structure. The most concrete remaining possibilities are a source-forced nonconstant transition sequence `t_n=nY_n` that stays away from both `0` and `infinity`; a canonical cross-index/operator-valued boundary form that acts before diagonal squaring; or a different cohomological/intersection sign theorem that does not obtain positivity by an ordinary Fourier `L^2` norm. Any such route must still generate the Mangoldt/Gamma/polar normalization intrinsically and survive the branch's prior-art and matched-control gates.