# NB-149 — Jordan domination reinstates the positive Poisson log budget

**Status:** `EXACT-DERIVED + SOURCE-SPECIFIC + SIGNED-SAMPLING + JORDAN-DOMINATION + METHOD-OBSTRUCTION + NB-148-FRONTIER`.

`NB-148` showed that a zero-mass signed exterior sampler can cancel the universal `(1/2) log G` Hadamard background only by creating a sign-changing Poisson kernel with an equal integrated negative lobe. The immediate repair is to bound that adverse lobe by absolute values or by the negative Jordan part of the sampler. This finding shows exactly what that repair costs: it converts the signed problem back into a positive Poisson sampler, whose zero budget is again of order `log G`. Thus the Hadamard cancellation is useful only if the negative lobe is controlled by genuinely signed or location-sensitive information; a Jordan/triangle-inequality repair alone forfeits the gain.

Let

\[
\Omega_G:=\{(\sigma,v):\sigma=1+\delta,\ 0<\delta\le1,\ |v-G|\le H_G\},
\qquad H_G=o(G),
\tag{1}
\]

and let `nu` be a finite signed Borel measure on `Omega_G`, with Jordan decomposition

\[
\nu=\nu_+-\nu_-,
\qquad
|\nu|=\nu_++\nu_-.
\tag{2}
\]

For a nontrivial zeta zero `rho=beta+i gamma`, define

\[
P_{\sigma,v}(\rho)
:=
\frac{\sigma-\beta}
{(\sigma-\beta)^2+(v-\gamma)^2}>0,
\tag{3}
\]

and

\[
K_\nu(\rho):=\int_{\Omega_G}P_{\sigma,v}(\rho)\,d\nu(\sigma,v).
\tag{4}
\]

Then pointwise on the actual zero set,

\[
\boxed{
(K_\nu(\rho))_-
\le
K_{\nu_-}(\rho)
}
\tag{5}
\]

and

\[
\boxed{
|K_\nu(\rho)|
\le
K_{|\nu|}(\rho).
}
\tag{6}
\]

Consequently, summing over all nontrivial zeros and using the same positive exterior Hadamard estimate as `NB-144`--`NB-147`,

\[
\boxed{
\sum_\rho (K_\nu(\rho))_-
\le
\frac12\,\nu_-(\Omega_G)\log G
+
O\!\left(
\int_{\Omega_G}\frac{d\nu_-(\sigma,v)}{\sigma-1}
+
\nu_-(\Omega_G)
\right),
}
\tag{7}
\]

while

\[
\boxed{
\sum_\rho |K_\nu(\rho)|
\le
\frac12\,\|\nu\|_{\mathrm{TV}}\log G
+
O\!\left(
\int_{\Omega_G}\frac{d|\nu|(\sigma,v)}{\sigma-1}
+
\|\nu\|_{\mathrm{TV}}
\right).
}
\tag{8}
\]

If `nu(Omega_G)=0`, then

\[
\nu_+(\Omega_G)=\nu_-(\Omega_G)
=\frac12\|\nu\|_{\mathrm{TV}}.
\tag{9}
\]

Hence the generic Jordan bound for the adverse zero lobe has leading scale

\[
\boxed{
\frac14\|\nu\|_{\mathrm{TV}}\log G,
}
\tag{10}
\]

provided the exterior Euler cost is `o(||nu||_TV log G)`. In the natural normalization

\[
\nu_+(\Omega_G)=\nu_-(\Omega_G)=1,
\tag{11}
\]

this is exactly the familiar unit-positive-sampler budget

\[
\boxed{
\frac12\log G+o(\log G).
}
\tag{12}
\]

The same loss appears on the prime side if it is repaired by a triangle inequality:

\[
\left|
\int_{\Omega_G}
-\frac{\zeta'}{\zeta}(\sigma+iv)
\,d\nu(\sigma,v)
\right|
\le
\int_{\Omega_G}
\left|\frac{\zeta'}{\zeta}(\sigma+iv)\right|
\,d|\nu|(
\sigma,v)
\ll
\int_{\Omega_G}\frac{d|\nu|}{\sigma-1}.
\tag{13}
\]

Thus zero-total-mass cancellation removes the common Hadamard term only so long as the subsequent argument continues to exploit signs. Replacing the dangerous part by `nu_-` or the whole expression by `|nu|` re-enters the positive cone classified by `NB-147`.

## Derivation

Because the Poisson kernel `(3)` is positive,

\[
K_\nu=K_{\nu_+}-K_{\nu_-},
\qquad
K_{\nu_+},K_{\nu_-}\ge0.
\tag{14}
\]

For nonnegative numbers `A,B`,

\[
(A-B)_-\le B,
\qquad
|A-B|\le A+B.
\tag{15}
\]

Applying `(15)` to `(14)` proves `(5)` and `(6)` pointwise. Moreover `K_{|nu|}` is summable over the zero divisor in the exterior regime, so `(6)` also gives absolute convergence of the signed zero sum whenever needed. Tonelli is legitimate for both positive Jordan pieces.

For any finite positive measure `mu` on `(1)`, the logarithmic-derivative/Hadamard identity used throughout `NB-144`--`NB-147`, together with the absolutely convergent Euler-product estimate for `Re s>1`, gives uniformly on the support

\[
\sum_\rho P_{\sigma,v}(\rho)
\le
\frac12\log G
+
O\!\left(\frac1{\sigma-1}+1\right).
\tag{16}
\]

Integrating `(16)` against `mu` gives

\[
\sum_\rho K_\mu(\rho)
\le
\frac12\mu(\Omega_G)\log G
+
O\!\left(
\int\frac{d\mu}{\sigma-1}+\mu(\Omega_G)
\right).
\tag{17}
\]

Taking `mu=nu_-` in `(17)` after `(5)` proves `(7)`. Taking `mu=|nu|` after `(6)` proves `(8)`. Equation `(9)` is the elementary Jordan identity obtained from `nu(Omega_G)=0`, and `(10)`--`(12)` follow immediately.

There is also a useful exact interpretation of the scale in `(7)`. If a positive measure `mu` has

\[
\int_{\Omega_G}\frac{d\mu}{\sigma-1}
=o\!\left(\mu(\Omega_G)\log G\right),
\tag{18}
\]

then the same Hadamard identity and the absolute Euler-product bound show that its total zero-side Poisson mass is

\[
\sum_\rho K_\mu(\rho)
=
\left(\frac12+o(1)\right)
\mu(\Omega_G)\log G.
\tag{19}
\]

So under the cheap-exterior regime `(18)`, the Jordan majorant used in `(7)` is itself genuinely of logarithmic size. The method has not merely introduced a loose notation `O(log G)`; it has replaced the cancelled signed object by a positive object carrying the same leading Hadamard mass that `NB-148` was designed to remove.

## What this does and does not rule out

The theorem rules out a specific proof architecture: cancel the common Hadamard background with a zero-mass signed sampler, then control the negative zero contribution solely by `(K_nu)_-<=K_{nu_-}` or control the whole signed zero contribution solely by `|K_nu|<=K_|nu|`. Under the inexpensive exterior scaling needed for the original cancellation to matter, these substitutions restore a positive `Theta(log G)` budget. They therefore cannot by themselves turn the logarithmic local occupancy barrier of `NB-146`/`NB-147` into the `o(log G)` confluence law sought by the Nyman branch.

This is a method obstruction, not a lower bound for the actual adverse contribution. Equation `(7)` does **not** say that actual zeta zeros sample the negative lobe with `Omega(log G)` mass. They may miss most of it, or signed contributions may cancel after additional structure is used. What the theorem says is that Jordan domination cannot certify such favorable behavior: it discards exactly the sign/location information that would be needed to see it.

Nor does `(13)` prove that the prime-side signed combination is large. It only shows that controlling it by absolute values erases any cancellation there as well. A successful signed argument may still exploit correlations in the von Mangoldt series, arrange the negative lobe in a zero-poor region using source-specific information, or couple the signed kernel directly to the Nyman target so that adverse mass is not estimated separately.

## Relation to `NB-148`

`NB-148` produced a continuous conservation law: a zero-mass sampler has equal positive and negative **Lebesgue-integrated** Poisson mass along each horizontal zero line. It explicitly left open whether the actual discrete zeta zero set samples the negative lobe strongly enough to matter. The most immediate bridge from continuous negative mass to the discrete zero sum is positivity: dominate the adverse values by the negative Jordan sampler. Equations `(5)`--`(12)` show why that bridge is too expensive in isolation.

The frontier therefore becomes sharper. Signed exterior sampling is still a live route, but the next useful input must remain signed after the Hadamard cancellation. It must use the geometry of where zeros fall relative to the negative lobe, cancellation/correlation on the Euler side, or target-aware information that couples the positive and negative pieces before absolute values are taken. Merely invoking the positive machinery a second time after cancellation returns to the same logarithmic barrier.

## Stress tests and boundaries

If `nu` is already positive, then `nu_-=0`, `(5)` is vacuous and `(8)` is just the positive estimate of `NB-147`; the finding introduces no artificial loss. If `nu` has zero total mass, `(9)` is exact regardless of whether the sampler is discrete, continuous, or obtained as a coalescing finite difference. If the negative Jordan piece is supported at very small `delta`, the `delta^{-1}` term in `(7)` may dominate `log G`; this only makes absolute-value repair more expensive and does not help the route.

The support restriction `H_G=o(G)` is used only to replace `log|v|` uniformly by `log G+o(1)` in the Hadamard term. Macroscopically separated sampling heights require a weighted logarithmic bookkeeping and are not classified by `(7)` in this form. No RH, zero-density theorem, spacing hypothesis, simplicity assumption, or statistical model for the zeros is used.

Most importantly, `(7)` is an upper bound on the Jordan *majorant*, not a claim that the true negative part saturates it. Any theorem showing that a carefully engineered negative lobe is sampled by only `o(log G)` zero mass would evade this obstruction precisely because it supplies the missing location-sensitive information.

## Prior-art search

A targeted literature search found the standard Hahn--Jordan/total-variation framework for Poisson integrals of signed measures and classical work on logarithmic derivatives of zeta functions. These cover the generic ingredients behind `(5)`--`(8)`, but no external result is load-bearing: the pointwise domination is the elementary Jordan inequality `(15)`, and the zeta-specific budget is exactly the positive exterior estimate already established and sourced in `NB-144`--`NB-147`. The present claim is the method-level synthesis that applying Jordan domination after `NB-148` reinstates the positive `Theta(log G)` budget, not novelty of Jordan decomposition or Poisson integration. No new `SOURCES.md` entry is required.

## Source map

- `NB-146`, `NB-147`: positive exterior Poisson budget and its reflection-closure method boundary.
- `NB-148`: zero-mass Hadamard cancellation and forced negative Poisson lobe.
- Hadamard/logarithmic-derivative identity and exterior Euler-product majorant: already anchored in the Nyman-Beurling source file and used in `NB-144`--`NB-148`.
- Hahn--Jordan decomposition and total variation: standard measure theory; used only through the elementary inequalities `(14)`--`(15)`.

## Consequence for the line

The obvious absolute-value repair of `NB-148` is now classified. Cancelling the universal logarithmic background and then bounding the adverse lobe by its negative Jordan sampler simply recreates a unit positive sampler, hence a `(1/2) log G` zero budget under the natural normalization. Bounding the whole signed kernel by total variation is twice as expensive. Therefore any genuine improvement from signed exterior sampling must preserve sign or exploit zero location after the cancellation step; otherwise the argument returns to the positive logarithmic barrier it was meant to escape.