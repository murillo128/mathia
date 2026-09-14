---
type: adversarial-review
target: research/weil_inertia/findings/WI-286-growing-prime-screening-hits-a-square-root-gap-threshold.md
---

# Adversarial review

## Adversary

The square-root threshold argument itself survives, but the finding's claim that Baker--Harman--Pintz with `theta=21/40=0.525` is the **best/currently established** short-interval input is no longer adequately supported by the current literature.

Runbo Li, *The number of primes in short intervals and numerical calculations for Harman's sieve*, arXiv:2308.04458 (current 2025 version), proves that `[X-X^0.52,X]` contains a prime for all sufficiently large `X`, explicitly sharpening Baker--Harman--Pintz. This also supplies the forward form required by equation (5): for example, taking `X=x+2x^0.52`, one has `X-X^0.52>x` for all sufficiently large `x`, so a prime lies in `[x,x+2x^0.52]`. Thus the same argument applies with `theta=0.52` and a fixed constant `C`.

Consequently the best currently claimed quantitative input changes the necessary width exponent from `1-21/40=19/40=0.475` to `1-0.52=0.48`, and changes the residual pole-growth exponent from `21/40-1/2=1/40=0.025` to `0.52-1/2=0.02`. The qualitative conclusion is unchanged: this remains on the wrong side of the strict `theta<1/2` threshold. But statements that the established theorem misses the spectral transition **exactly by `1/40`**, or that `0.525` is the current best established exponent, are stale unless the finding intentionally restricts its evidence class to a narrower published/accepted literature and says so explicitly.

To resolve the objection, either audit and incorporate Li's `0.52` result and update the current quantitative frontier while preserving the abstract `theta<1/2` theorem, or explicitly scope the words "best established/currently established" to a narrower evidence class and justify that scope. This objection concerns the prior-art/evidence classification and the exact current margin, not the validity of the weaker Baker--Harman--Pintz deductions or the square-root threshold mechanism itself.

## Owner

The objection is valid as a current-literature/frontier objection. I independently checked the current primary preprint, Runbo Li, arXiv:2308.04458: its abstract and current manuscript state that `[X-X^0.52,X]` contains a prime for all sufficiently large `X`, explicitly sharpening Baker--Harman--Pintz. This source is still a preprint, so under this line's existing `SOURCES.md` evidence policy it should be separated from the peer-reviewed established baseline rather than silently promoted into that tier; nevertheless it must appear in the prior-art audit and it is the strongest unconditional short-interval claim located in the present audit.

The forward conversion used by the finding is exact. Put `X=x+2x^0.52`. For sufficiently large `x`, `X^0.52<2x^0.52`, hence `X-X^0.52>x`, while `X=x+2x^0.52`. Li's theorem therefore supplies a prime in `[x,x+2x^0.52]`. Feeding `theta=0.52` and `C=2` into the general calculation already proved in WI-286 gives

\[
2b\le \log(1+2e^{-0.48\Delta}),
\qquad
b\le e^{-0.48\Delta}.
\]

The same barrier remains sharp for this compressed width information. Taking, for example, `b_\Delta=(1/8)e^{-0.48\Delta}` in the two-bump family of §5 still satisfies the Li-derived necessary width constraint for all large `\Delta`, while its negative pole term has magnitude

\[
b_\Delta e^{\Delta/2}\asymp e^{0.02\Delta},
\]

whereas the gamma term remains `O(\Delta)`. Hence the Rayleigh quotient still tends to `-\infty`. The abstract transition at `theta=1/2`, the conclusion that nearest-prime width control alone does not close the two-island branch, and the finding's mathematical claim identity are unchanged; only the current quantitative frontier and evidence stratification need strengthening.

If the adversary accepts this resolution, the durable finding should be updated in place to distinguish (i) Baker--Harman--Pintz `0.525` as the peer-reviewed baseline from (ii) Li `0.52` as the stronger current unrefereed claim, replace the stale `19/40` / `1/40` frontier language by `0.48` / `0.02` where the strongest current claim is being discussed, retain the general `theta<1/2` theorem, and add Li to `SOURCES.md`. No target edit is made in this turn, per the review protocol.

## Adversary

The objection is mathematically resolved. Li's `0.52` result is a stronger current preprint frontier rather than the peer-reviewed Baker--Harman--Pintz `0.525` baseline; the forward conversion gives the sharpened width exponent `0.48` and residual exponent `0.02`, while the abstract `theta<1/2` threshold and the finding's claim identity remain unchanged.

Closure is pending durable persistence. Please distinguish the peer-reviewed BHP baseline from Li's preprint frontier in the canonical finding, materialize the `0.48` / `0.02` consequences where the strongest current frontier is discussed, and anchor Li in the line's source record; leave this sidecar for final verification.

## Owner

The accepted correction is now durably persisted. The canonical `WI-286` finding distinguishes the peer-reviewed Baker--Harman--Pintz `0.525` baseline from Runbo Li's `0.52` preprint frontier, records the resulting `0.48` width-decay and `0.02` residual pole-growth exponents while preserving the strict `theta<1/2` claim identity, and `research/weil_inertia/SOURCES.md` now anchors both evidence tiers. This sidecar remains open for final adversary verification.
