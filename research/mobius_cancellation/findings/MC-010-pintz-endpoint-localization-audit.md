# MC-010 — Pintz endpoint localization has a repairable constant-window gap

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `PARTIAL-AUDIT`.

## Claim

A direct audit of the very recent Pintz preprint recorded as `MC-S19` finds two concrete presentation defects in the route used by `MC-009`:

1. equation (2.10) prints the auxiliary zero sum with denominator `gamma`, although the same object is defined earlier with `|gamma|` and is later used as a positive majorant; the literal signed definition would cancel conjugate zero pairs and cannot be the intended quantity;
2. Corollary 6.3 localizes a weighted lower bound to an interval ending at `Y`, while the cited Theorem 6.1 is stated with upper endpoint `Y e^3`; the proof as printed does not explicitly remove that final constant-factor slice.

The first defect is an unambiguous typographical error. The second is a genuine missing localization step in the displayed proof, but it is repairable without changing the theorem's asymptotic content: apply Theorem 6.1 with parameter `X=Y e^{-3}` so that its upper endpoint is exactly `Y`, then perform the same lower-end subtraction used in the paper. Under the parameter inequalities already imposed in Corollary 6.3, the discarded initial range is lower order.

Consequently these two defects do **not** presently invalidate the `D_M`/`Z` logarithmic-exponent consequence isolated in `MC-009`. They also do not complete the audit of Pintz's theorem: the analytic core of Theorem 6.1, including its contour/kernel argument and residue estimates, remains external literature input and still requires independent reconstruction before `MC-009` can lose its `NEEDS-AUDIT` status.

## 1. The printed `W(x)` definition cannot be literal

In Section 1 of `MC-S19`, Pintz defines the zero-weighted quantity with an absolute ordinate denominator,

\[
W(x)=\sum_{\rho:\,|\gamma|\le x}\frac{x^\beta}{|\gamma|},
\qquad \rho=\beta+i\gamma.
\]

Equation (2.10), however, prints the denominator as `gamma` rather than `|gamma|`. Taken literally, this cannot be the quantity used in Theorems 2.1–2.2. Nonreal zeta zeros occur in conjugate pairs `beta+i gamma` and `beta-i gamma`, and their contributions to the signed sum are

\[
\frac{x^\beta}{\gamma}+\frac{x^\beta}{-\gamma}=0.
\]

Thus the literal signed sum would collapse pairwise, whereas the paper subsequently takes `log W(x)` and later uses the comparison

\[
Z(x)\le W(x),
\qquad
Z(x)=\max_{\rho:\,\gamma>0}\frac{x^\beta}{\gamma}.
\]

Those operations require the positive absolute-ordinate version. The earlier definition, later inequality, and conjugation symmetry therefore determine the intended reading uniquely: equation (2.10) is missing the absolute-value bars.

This typo does not affect `MC-009`, whose extracted exponent statement uses `D_M` and `Z` directly rather than relying on algebra with the misprinted signed expression.

## 2. Corollary 6.3 has an endpoint mismatch as printed

The difficult `vartheta=1` case of `MC-S19` uses Theorem 6.1 to produce a weighted lower bound from a zero

\[
\rho_0=1-\eta_0+i\gamma_0.
\]

With parameter `Y`, Theorem 6.1 integrates up to

\[
Y_0=Y e^3.
\]

The factor `e^3` is not a notation ambiguity: in the proof it comes from the kernel variable `H=\log Y-\log x`, with the cutoff `H\le-3` corresponding exactly to `x\ge Y e^3`.

Corollary 6.3 then states the desired lower bound on a terminal interval of the form

\[
[Y^{1-\varepsilon/8},Y].
\]

Its proof cites Theorem 6.1, an estimate for the early interval, and an exponent gap that makes that early interval negligible. Those ingredients remove the **lower** part of the Theorem 6.1 integral, but as written they do not remove or control the remaining slice

\[
[Y,Y e^3].
\]

Because the integrand involves `|M(x)|`, one cannot infer a lower bound on the shorter interval merely by dropping a positive final slice. Therefore the displayed derivation of Corollary 6.3 has a real localization omission if Theorem 6.1 is invoked with the same parameter `Y`.

## 3. A constant rescaling repairs the localization

The omission is repaired by a parameter change rather than by a new analytic estimate.

Fix the target endpoint `Y` of Corollary 6.3 and apply Theorem 6.1 with

\[
X=Y e^{-3}.
\]

Its upper endpoint is then

\[
X e^3=Y.
\]

The theorem's main lower bound changes only by constants depending on the already fixed exponents: for example `X^kappa=e^{-3\kappa}Y^\kappa`, and

\[
\log(\gamma_0 X)=\log(\gamma_0 Y)-3
\]

is asymptotically equivalent to `\log(\gamma_0Y)`. Thus the same lower-bound scale is obtained on an integral whose support now ends at exactly `Y`.

It remains to discard the initial range. Using only the trivial bound `|M(x)|\le x`, the weighted contribution below `Y^{1-\varepsilon'}` has the shape

\[
E\ll \frac{\gamma_0}{\kappa+\eta_0}
Y^{(1-\varepsilon')(\kappa+\eta_0)}.
\]

Corollary 6.3 chooses

\[
\varepsilon'=\varepsilon/8,
\qquad
\sqrt\varepsilon\ge\kappa\ge\varepsilon,
\qquad
\eta_0\le\varepsilon^2/100,
\qquad
\gamma_0\le Y^{\varepsilon^2/100},
\]

and the paper records the exponent separation

\[
\kappa-(1-\varepsilon')(\kappa+\eta_0)
\ge \varepsilon^2/10.
\]

The allowed polynomial contribution from `gamma_0`, together with the logarithmic and `gamma_0^{C(\eta_0+\kappa)^{3/2}}` losses in Theorem 6.1, is strictly smaller than this fixed exponent gap for sufficiently small `epsilon`. Hence the early contribution is lower order relative to the theorem's main lower bound. What survives is the same required lower bound over

\[
[Y^{1-\varepsilon/8},Y].
\]

Therefore the endpoint mismatch is a repairable proof-presentation gap: the corollary follows after the constant rescaling `Y -> Y e^{-3}` before performing the paper's existing lower-end subtraction.

## 4. Consequence for `MC-009`

`MC-009` extracts from Pintz's Theorem 2.2 the logarithmic-order identity

\[
\lim_{x\to\infty}\frac{\log D_M(x)}{\log x}
=\vartheta,
\]

and hence the RH-equivalent mean-absolute endpoint

\[
D_M(x)=O_\varepsilon(x^{1/2+\varepsilon})
\quad\text{for every }\varepsilon>0.
\]

The two issues found here do not presently break that extraction:

- the `W` typo is irrelevant to the `D_M`/`Z` branch and has a uniquely determined correction;
- the terminal-interval step used in the `vartheta=1` lower bound has the constant-rescaling repair above.

This is stronger support than merely accepting the preprint statement at face value, but it is **not** a full independent verification of Theorem 2.2. Theorem 6.1 is the load-bearing analytic input in the hard case, and its Mellin-kernel construction, contour displacement, interchange steps, zero contribution, and quantitative error terms have not yet been independently reconstructed here.

Accordingly `MC-009` should remain `NEEDS-AUDIT`. The present finding narrows the remaining audit surface instead of upgrading the theorem's evidence class.

## Prior art and novelty assessment

`MC-S19` is the primary and only literature source required for this finding. No novelty is claimed for Pintz's mean-absolute theorem, its zero-edge quantities, or the classical symmetry of the zeta zero set.

The Mathia-derived content is the internal consistency audit above: identifying the signed-denominator typo, isolating the precise endpoint mismatch in the Corollary 6.3 proof as printed, and giving the constant-rescaling repair. This is an audit/repair of fresh prior art, not a new bound for `M(x)`.

## Boundaries and next audit target

This finding does not prove Theorem 6.1, Theorem 2.2, RH, or any stronger unconditional Mertens estimate. It also does not show that every typographical or compressed step in `MC-S19` is harmless.

The next decisive audit target is the analytic core of Theorem 6.1 itself: reconstruct the Mellin kernel and truncation, justify the relevant integral/sum interchanges, verify the residue or zero contribution producing the lower bound, and check that the quoted losses are uniform in the stated `eta_0`, `kappa`, `gamma_0`, and `Y` ranges. A failure there would still require narrowing or withdrawing the dependent portion of `MC-009`; success would remove the main remaining theorem-level uncertainty.