# AF-437 — Recursive shell peeling amplifies earlier errors exponentially

**Status:** `EXACT-DERIVED`, `ARITHMETIC-FIDELITY`, `MULTISCALE-RECOVERY`, `CONDITIONING-BARRIER`, `CLASSICAL-PRONY-CONTEXT`, `NO-NOVELTY-CLAIM`

## Claim

AF-436 showed that the exact normalized Euler coefficients

\[
s_k=\zeta(2k)=\sum_{j\ge1}j^{-2k}
\]

retain the entire shell ladder: after the first `m-1` shells are removed exactly,

\[
r_{m,k}:=\sum_{j\ge m}j^{-2k}=m^{-2k}(1+o(1)).
\]

That exact-peeling hypothesis hides a second conditioning barrier. If an earlier shell is even slightly mislocated or misweighted, its error is measured at the much larger scale `j^{-2k}` and must be suppressed below the target scale `m^{-2k}`.

Write

\[
\lambda_j=j^{-2}.
\]

Suppose the first `m-1` atoms are peeled using approximate locations and weights

\[
\widehat\lambda_{j,k}=\lambda_j(1+\eta_{j,k}),
\qquad
\widehat w_{j,k}=1+\omega_{j,k},
\qquad j<m,
\]

and the observed moment also carries additive error `e_k`. Define

\[
\widehat r_{m,k}
:=s_k+e_k-
\sum_{j=1}^{m-1}
\widehat w_{j,k}\widehat\lambda_{j,k}^{\,k}.
\]

For fixed `m`, assume eventually

\[
|\eta_{j,k}|\le \frac{1}{2k},
\qquad
|\omega_{j,k}|\le \frac12.
\]

Then a sufficient condition for asymptotically faithful recovery of shell `m` by recursive peeling is

\[
\boxed{
 m^{2k}|e_k|
+
\sum_{j<m}
\left(\frac{m}{j}\right)^{2k}
\bigl(|\omega_{j,k}|+k|\eta_{j,k}|\bigr)
\longrightarrow 0.
}
\]

Under this condition,

\[
\frac{\widehat r_{m,k}}{r_{m,k}}\to1,
\qquad
\widehat r_{m,k}^{-1/(2k)}\to m,
\qquad
m^{2k}\widehat r_{m,k}\to1.
\]

The scale is sharp for this recursive peeling representation. If only shell `j<m` is perturbed, then:

- a weight error has relative target-scale contamination exactly of order
  \[
  |\omega_{j,k}|\left(\frac{m}{j}\right)^{2k};
  \]
- a location error with `k|\eta_{j,k}|\le1/2` has relative target-scale contamination comparable, up to universal constants, to
  \[
  k|\eta_{j,k}|\left(\frac{m}{j}\right)^{2k}.
  \]

Therefore uniform recursive recovery of shell `m` requires earlier shell `j` to be known at the approximate scales

\[
\boxed{
|\omega_{j,k}|=o\!\left(\left(\frac{j}{m}\right)^{2k}\right),
\qquad
|\eta_{j,k}|=o\!\left(\frac1k\left(\frac{j}{m}\right)^{2k}\right).
}
\]

Since `j<m`, these are exponentially shrinking tolerances. Exact recoverability of the full moment sequence therefore does not imply a numerically stable shell-by-shell provenance channel: deeper shell recovery inherits an **error cascade from every earlier peeling stage**.

## Exact derivation

Separate the target residual from the peeling error:

\[
\widehat r_{m,k}-r_{m,k}
=e_k+
\sum_{j<m}\lambda_j^k
\left[1-(1+\omega_{j,k})(1+\eta_{j,k})^k\right].
\]

AF-436 gives

\[
r_{m,k}=\lambda_m^k(1+o(1))=m^{-2k}(1+o(1)).
\]

For a pure location perturbation, use

\[
(1+\eta)^k-1
=\eta\sum_{q=0}^{k-1}(1+\eta)^q.
\]

If `|\eta|\le1/(2k)`, all factors are positive and

\[
\frac{k}{2}|\eta|
\le
\left|(1+\eta)^k-1\right|
\le
e^{1/2}k|\eta|.
\]

Indeed, the upper bound follows from

\[
(1+|\eta|)^{k-1}\le e^{k|\eta|}\le e^{1/2},
\]

while for negative `\eta`, Bernoulli's inequality gives

\[
(1-|\eta|)^{k-1}
\ge 1-(k-1)|\eta|
\ge \frac12.
\]

Hence a location error in shell `j` contributes

\[
\lambda_j^k\left|(1+\eta_{j,k})^k-1\right|
\asymp
j^{-2k}k|\eta_{j,k}|.
\]

After division by the target shell scale `m^{-2k}`, this becomes

\[
\asymp
k|\eta_{j,k}|
\left(\frac{m}{j}\right)^{2k}.
\]

For a pure weight perturbation the identity is exact:

\[
\lambda_j^k-
(1+\omega_{j,k})\lambda_j^k
=-\omega_{j,k}j^{-2k},
\]

so its relative target-scale size is

\[
|\omega_{j,k}|
\left(\frac{m}{j}\right)^{2k}.
\]

With both errors present,

\[
\begin{aligned}
\left|1-(1+\omega)(1+\eta)^k\right|
&\le |\omega|
+\left|(1+\eta)^k-1\right|
+|\omega|\left|(1+\eta)^k-1\right|\\
&\le C\bigl(|\omega|+k|\eta|\bigr)
\end{aligned}
\]

for a universal constant `C` under the stated small-error bounds. Summing over the finitely many earlier shells and adding `e_k` proves the sufficient condition.

The one-shell lower bounds show sharpness of the scale for worst-case independent peeling errors. If the admissible error budget on one earlier shell permits `k|\eta_{j,k}|(m/j)^{2k}` or `|\omega_{j,k}|(m/j)^{2k}` to remain bounded away from zero, a perturbation of that shell alone produces a nonvanishing relative error at the shell-`m` scale. If the quantity diverges, that earlier-shell contamination dominates the target residual.

This is a worst-case statement. Carefully correlated errors can cancel each other, so the theorem does not claim that every perturbation at the threshold destroys recovery.

## Common-radius normalization is the first stage of the same cascade

AF-435 selects the common Taylor radius

\[
R=2\pi
\]

from coefficient root growth. AF-436 then normalizes by `R^{2k}` before reading the shell moments. If the normalization uses

\[
\widehat R_k=R(1+\delta_k),
\]

then, before any shell peeling,

\[
\widehat s_k=(1+\delta_k)^{2k}s_k.
\]

For `2k|\delta_k|\le1/2`, the same estimate gives

\[
\left|(1+\delta_k)^{2k}-1\right|
\asymp k|\delta_k|.
\]

Because `s_k\to1`, resolving shell `m` from an empirically estimated common radius therefore requires, for this normalization route,

\[
\boxed{
|\delta_k|=o\!\left(\frac{m^{-2k}}{k}\right).
}
\]

This requirement disappears when `R=2\pi` is supplied exactly by the analytic source identity rather than estimated from noisy coefficients. The distinction matters: an exact symbolic source normalization and a data-estimated normalization have radically different provenance conditioning even though they define the same formal moment sequence in the zero-error limit.

## Why this is stronger than the AF-436 noise threshold

AF-436 established the direct observation threshold

\[
|e_k|=o(m^{-2k})
\]

after **exact** removal of shells `1,\ldots,m-1`. The present result shows that direct coefficient noise is only one term in the budget. Recursive inference creates additional effective noise from all previous estimates.

For example, recovering shell `m` after a relative location error `\eta_{1,k}` in the first atom requires

\[
k|\eta_{1,k}|m^{2k}\to0.
\]

Thus a first-shell error that is tiny on its own natural scale may still swamp every deeper shell. The provenance ladder is triangular: each recovered shell becomes part of the normalization for all later ones, and the scale ratio between shell `j` and shell `m` is exactly

\[
\frac{j^{-2k}}{m^{-2k}}
=\left(\frac{m}{j}\right)^{2k}.
\]

This supplies the conditioning analysis explicitly left open in AF-436.

## Prior-art and novelty audit

The general instability of recovering exponential sums or atomic measures from noisy moments is classical. Prony-type inversion is governed by the geometry and conditioning of Vandermonde/Hankel systems, and support separation is a standard stability parameter.

Relevant prior art includes:

- Dmitry Batenkov and Yosef Yomdin, **“On the Accuracy of Solving Confluent Prony Systems,”** *SIAM Journal on Applied Mathematics* 73(1), 134–154 (2013), DOI `10.1137/110836584`. This studies local stability and maximal possible accuracy for Prony-type systems through their Jacobian/confluent-Vandermonde geometry.
- Gerlind Plonka, **“Prony Methods for Recovery of Structured Functions,”** *GAMM-Mitteilungen* 37(2), 239–258 (2014), DOI `10.1002/gamm.201410011`. This surveys classical Prony reconstruction and related exponential-sum recovery methods.
- Stefan Kunis, Thomas Peter, Tim Römer, and Ulrich von der Ohe, **“A Multivariate Generalization of Prony's Method,”** *Linear Algebra and its Applications* 490, 31–47 (2016), DOI `10.1016/j.laa.2015.10.023`. This gives uniqueness and stable-reconstruction conditions for finitely supported measures in terms including moment order and support separation.
- Thanh Mai Pham Ngoc, **“A Statistical Minimax Approach to the Hausdorff Moment Problem,”** *Inverse Problems* 24(4), 045018 (2008), DOI `10.1088/0266-5611/24/4/045018`. This treats noisy Hausdorff moment inversion explicitly as an ill-posed statistical inverse problem.

No novelty is claimed for Prony conditioning, moment ill-posedness, Vandermonde sensitivity, or the fact that node errors are amplified in high powers. The Arithmetic Fidelity result here is the **exact shell-relative error budget for the current Euler coefficient ladder**: the factor `(m/j)^{2k}` identifies how much precision at every earlier provenance layer is required before shell `m` remains visible, and it separates exact symbolic recoverability from recursive stable recoverability inside the concrete compression chain studied in AF-433–AF-436.

## Relation to the current transport problem

AF-434 showed that the present full-column packet saddle aggregates shell information into zeta factors and does not transport shell labels into its leading rate. AF-436 then showed that the exact source sequence does contain those labels at nested residual scales `m^{-2k}`.

The present result sharpens the next design gate. A candidate shell-resolved carrier cannot merely retain the exact sequence formally. It must either:

1. transport the shell contributions **before** recursive subtraction makes them exponentially fragile;
2. provide a joint recovery mechanism whose conditioning is proved better than the sequential peeling bound; or
3. exploit exact symbolic shell structure so that earlier provenance is not re-estimated from noisy downstream data.

This is directly relevant to the current packet-aperture question. A downstream target that only resolves polynomial or root-rate differences cannot consume deep shell identity if the carrier first reconstructs that identity through a peeling stage requiring exponentially finer calibration than the target retains.

## Boundaries and failure modes

- The exponential gate is a theorem about the **recursive peeling representation**. It is not a universal minimax lower bound for every joint moment-inversion algorithm.
- The proof fixes `m` and lets `k\to\infty`. Uniform recovery when `m=m(k)` grows requires a separate analysis.
- The shell model here has unit positive weights and locations `j^{-2}`. Signed, complex, repeated, or continuously distributed atoms may have different conditioning and cancellation mechanisms.
- The one-shell lower bounds are worst-case and exclude beneficial cancellation between correlated location and weight errors.
- If the integer shell ladder and `R=2\pi` are supplied exactly as external analytic structure, the corresponding estimation errors are zero. This finding then becomes a warning about downstream numerical/reconstructive representations, not an obstruction to exact symbolic manipulation.
- A joint Prony/Hankel reconstruction can have different conditioning from sequential dominant-atom peeling. This finding does not rule out such a carrier; it gives that alternative a concrete benchmark to beat.
- Nothing here distinguishes rational primes, proves RH, or supplies a zero criterion. The result concerns the fidelity and conditioning of one source-provenance representation.

## Decisive audit test

For any proposed downstream carrier that claims to preserve shell `m` from the Euler coefficient sequence, determine whether it reconstructs or transports earlier shells. If it uses recursive subtraction, compute the effective location and weight errors for every `j<m` and test

\[
m^{2k}|e_k|
+
\sum_{j<m}
\left(\frac{m}{j}\right)^{2k}
\bigl(|\omega_{j,k}|+k|\eta_{j,k}|\bigr).
\]

If this quantity does not tend to zero, shell-`m` recovery is not stable by that peeling mechanism. A claimed repair must then either preserve the shell labels earlier, use a provably better-conditioned joint inverse, or provide exact structure that removes the offending estimation stage.