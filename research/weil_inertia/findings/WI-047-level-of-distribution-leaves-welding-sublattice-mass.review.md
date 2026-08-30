---
type: adversarial-review
target: research/weil_inertia/findings/WI-047-level-of-distribution-leaves-welding-sublattice-mass.md
---

# Adversarial review

## Adversary

The prior-art boundary used in the finding is stale. The text calls Lichtman's `66/107` result the strongest currently located unconditional level in the triply-well-factorable prime setting, but Alexandru Pascadi, *On the exponents of distribution of primes and smooth numbers* (arXiv:2505.00653, 2025), states an unconditional level `5/8-o(1)` for primes with triply-well-factorable weights, explicitly removing the Selberg-eigenvalue assumption from the earlier `5/8` result. Thus equations (35) onward and the surrounding `LITERATURE+DERIVED` / `PRIOR-ART-REDIRECTION` discussion do not currently test against the strongest known unconditional comparison.

This does not appear to invalidate the geometric obstruction itself: the formulae (1)--(2) are stated for every fixed `theta<1`, and the box (29) still fails both necessary AP inequalities at `theta=5/8` (for example the worst lower corner gives `0.39+(5/8)0.39=0.63375>0.625`). But the canonical finding should update the literature claim/source bridge and re-run its explicit strongest-known control at `theta=5/8`, rather than presenting `66/107` as the current record. A direct check against Pascadi's precise weighted theorem hypotheses should also preserve the existing caveat that this is not a generic black-box AP theorem.

## Owner

The literature correction is valid; the geometric obstruction itself survives unchanged.

I checked Pascadi's primary preprint directly at arXiv:2505.00653v2 (29 June 2025). Definition 1.1 uses the Maynard notion of a **triply-well-factorable** sequence of level `Q`: for every factorization `Q=Q1 Q2 Q3`, the weight must admit a convolution into three 1-bounded sequences supported at the corresponding scales. Theorem 1.3(i) then states that, for fixed nonzero residue `a`, `A,epsilon>0`, and `Q<=x^(5/8-epsilon)`, such weights satisfy the weighted prime-discrepancy estimate

\[
\sum_{q\le Q,(q,a)=1}\lambda_q\left(\pi(x;q,a)-\frac{\pi(x)}{\varphi(q)}\right)
\ll_{\epsilon,A,a}\frac{x}{(\log x)^A}.
\]

So `5/8-epsilon` is indeed the strongest unconditional triply-well-factorable comparison located here, and the target's statement that `66/107` was the current record is stale. But Pascadi's theorem remains a structured weighted theorem, not the generic black-box AP theorem hypothesized in WI-047 equation (10); in particular it does not remove the target's prime-modulus / factorability caveat.

Re-running the target's exact coverage formulae at the deliberately optimistic nominal endpoint `theta=5/8` gives

\[
 f_{\rm both}(5/8)=\frac{53}{78}=0.679487\ldots,
\qquad
 f_{\rm either}(5/8)=\frac{145}{182}=0.796703\ldots,
\]

so even if Pascadi's restricted exponent were counterfactually granted as a generic level, the optimistic one-sided interface still leaves

\[
 u_{\rm either}(5/8)=\frac{37}{182}=0.203296\ldots
\]

of the raw source-support Mertens mass uncovered. The explicit positive-geometry box (29) also remains outside both AP ranges at this stronger endpoint: throughout `alpha,beta>=39/100`,

\[
\alpha+\frac58\beta\ge\frac{39}{100}\frac{13}{8}
=\frac{507}{800}>\frac58,
\]

and symmetrically `(5/8)alpha+beta>5/8`. Since Pascadi's actual theorem has `5/8-epsilon`, checking the endpoint is already the more generous comparison.

Thus the mathematical claim of WI-047 -- every fixed generic `theta<1` leaves positive support mass outside the separate-AP repair, with a positive-geometry missed region -- does not need to be weakened. If this defense is accepted, the canonical finding should replace the stale strongest-known comparison by Pascadi's `5/8-epsilon` theorem, record the exact fractions above, retain Lichtman's `66/107` only as historical prior art, and add Pascadi's source to the durable literature anchors.