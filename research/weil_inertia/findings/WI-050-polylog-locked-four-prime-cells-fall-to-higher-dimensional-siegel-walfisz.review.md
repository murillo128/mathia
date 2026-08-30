---
type: adversarial-review
target: research/weil_inertia/findings/WI-050-polylog-locked-four-prime-cells-fall-to-higher-dimensional-siegel-walfisz.md
---

# Adversarial review

## Adversary

The Bienvenu step has a load-bearing source-geometry gap in the proof of the volume hypothesis. The finding claims that on the coprime family the source has shift range `K \asymp Y/max(b1,b2)` and, for `b1,b2 <= (log X)^B`, chooses a uniform subbody with `|k| <= c X/(log X)^B`. But the pinned `scripts/t2_swaps.py` normalization used by the finding gives

- `m_range(b2)` of length `Theta(X/b2)` from `b2*m in [s0 X,s1 X]`;
- on the coprime family `r=b1` and `m'=m-b1*k`;
- the `S1` loop requires both `m` and `m'` to remain in that same `m` window.

Therefore an interior source point only allows `|k| = O(X/(b1*b2))` from the `m'` constraint. When both coefficients are near `(log X)^B`, the displayed choice `|k| <= c X/(log X)^B` is too large by another polylogarithmic factor and does not define a subbody of the exact source region. So equation (12), which is the explicit verification of Bienvenu's `Vol(K) >> N^3 log^{-A} N` hypothesis, is not established by the argument currently written.

This looks repairable rather than fatal: using the exact source windows, one should be able to take an interior `m` interval of size `Theta(X/b2)`, an `n` interval of size `Theta(X/b1)` from the lock strip, and `|k| <= c X/(b1*b2)` while simultaneously checking the translated `m'` and `n'` constraints. That would give a volume on the order of `X^3/(b1^2 b2^2)`, still `>= X^3 log^{-4B} X` in a fixed polylogarithmic coefficient range and hence sufficient for Bienvenu after adjusting `A`. But that corrected source-normalized volume argument needs to be proved and persisted; until then, the theorem application has a genuine gap at its volume gate.
