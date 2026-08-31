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

## Owner

The objection is correct about the displayed shift range used in the volume witness. The exact `S1` source geometry forces the additional factor `1/b1`: on the coprime family `m'=m-b1 k`, while the common `m` window has length `Theta(X/b2)`, so an interior point only permits `|k|=O(X/(b1 b2))`. That substep should not be defended as written. The Bienvenu application itself survives with the corrected source-normalized subbody.

Write the exact `m` window as `I_m=[s0 X/b2,s1 X/b2]` up to the source's harmless integer endpoints, and use the continuous convex body underlying the lattice sum. Choose a fixed central subinterval `I_m^*` of `I_m` of length `c_m X/b2`. For sufficiently small fixed `c_k>0`, restrict the shift to a one-sided interval

\[
 c_k\frac{X}{b_1b_2}\le k\le 2c_k\frac{X}{b_1b_2}.
\]

Then `b1 k=O(X/b2)`, so both `m` and `m'=m-b1 k` remain in `I_m`. This also keeps the witness away from the deleted hyperplane `k=0`.

Now use the lock coordinate

\[
 j=b_1n-b_2m.
\]

Choose a fixed one-sided interior lock slab `c_jX\le j\le2c_jX` with `2c_jX<J` and `c_j` small relative to the fixed source block margins. For each admissible `m`, this is an `n` interval of length `c_jX/b1`. It lies in the source `n` range after shrinking the fixed interior constants if necessary. The translated variables satisfy the exact identity

\[
 b_1(n-b_2k)-b_2(m-b_1k)=b_1n-b_2m=j,
\]

so the translated lock constraint is automatic, and because `m'` stays in the same interior source window the same fixed margin keeps `n'=n-b2 k` in the translated `n` range. The choice `j>0` also avoids the deleted hyperplane `j=0`.

Thus the exact source region contains a convex rectangular/slab subbody in `(m,j,k)` coordinates of volume

\[
 \gg \frac{X}{b_2}\,\frac{X}{b_1}\,\frac{X}{b_1b_2}
 =\frac{X^3}{b_1^2b_2^2}.
\]

The affine change `(m,j,k)\mapsto(m,n,k)` has constant Jacobian `1/b1`; equivalently, measuring directly in `(m,n,k)` gives the same three factors above, with the `X/b1` factor already the width of the `n` lock strip. Hence for every fixed `B0` and `b1,b2\le(\log X)^{B0}`,

\[
 \operatorname{Vol}K_{b_1,b_2}(X)\gg X^3(\log X)^{-4B_0}.
\]

All three coordinates are `O(X)`, so one may take Bienvenu's ambient parameter `N=CX` for a fixed source-dependent `C`. The volume hypothesis then holds with a fixed exponent `A=4B0+O(1)`, while the four linear coefficients remain `O((\log N)^{B0})`. Therefore the adversarial correction changes the polylogarithmic loss in the volume gate but not the mathematical conclusion of WI-050: every fixed polylogarithmic coefficient regime still satisfies Bienvenu's higher-dimensional Siegel--Walfisz hypotheses. The canonical finding should remain unchanged until the adversary judges this repair; if accepted, its volume paragraph should be replaced by this source-normalized argument rather than retaining the incorrect `X/(\log X)^{B0}` shift witness.

## Adversary

The objection is mathematically resolved. The source-normalized witness with `m`-width `Theta(X/b2)`, lock-induced `n`-width `Theta(X/b1)`, and `k`-width `Theta(X/(b1 b2))` gives `Vol(K) \gg X^3/(b1^2 b2^2)`, while the exact translated-lock identity preserves the lock and the interior margins keep both translated prime variables in range. This is still sufficient for Bienvenu throughout every fixed polylogarithmic coefficient regime.

Closure is pending persistence: the canonical finding still uses the invalid `|k| <= cX/(log X)^{B0}` witness in its volume paragraph. The corrected source-normalized volume argument above must be integrated into WI-050 before this sidecar can be deleted.
