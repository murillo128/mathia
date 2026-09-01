# MI-007 — Critical prime-support bulk is Poisson-classical; arithmetic survives only in finer spectral sectors

**Evidence level:** supported by exact Gram identities, bounded-cluster controls, and conditional Hardy--Littlewood bulk theorems

## Core intuition

Prime support and pointing do expose arithmetic that the unpointed exponent-lattice bulk misses, but the ordinary finite-horizon empirical spectrum is now classified much further. At the mean-prime-gap scale, the support-only macroscopic bulk is the Poisson-sinc law under the natural full local Hardy--Littlewood hierarchy. Meanwhile bounded prime clusters force extreme ill-conditioning at every sublinear observation time. Ordinary bulk, extreme spectrum, and exact von-Mangoldt depth are therefore distinct information layers.

## Strongest justified principle

PL-072--PL-080 already classicalize the integer-band and smoothed coefficient regimes: local sharp windows give sinc/prolate kernels, macroscopic integer bulk is locally Toeplitz, determinant onset is Nyquist/Ingham, and smoothed growing-lag von Mangoldt statistics route to classical short-interval variance and Montgomery pair correlation. The half-weight `1/2` is a canonical balance scale but not a selector.

PL-081 finds the first genuine prime-support split above the mean-gap horizon: for `X/log X << T <= X`, the empirical prime Gram law tends to `delta_1`, yet bounded gaps can still force the smallest eigenvalue to zero along subsequences. PL-082 strengthens the extreme side. For every `T=o(X)`, bounded prime clusters produce arbitrarily large almost-rank-one principal blocks, so along subsequences the bottom edge tends to zero and the top edge becomes unbounded. No uniform frame/Riesz or extreme-spectral rigidity can survive in the full sublinear regime even when the bulk is benign.

PL-083--PL-085 classify the critical support-only bulk under increasingly strong local Hardy--Littlewood hypotheses. At `T=cX/log X`, the second moment is exactly the Poisson-sinc second moment; every fixed trace moment matches the Palm Poisson sinc Gram hierarchy; and under the full fixed-order local tuple hierarchy the empirical spectral measure converges to the deterministic Poisson-sinc Euclidean-random-matrix law. This is a meaningful prime-statistics limit, but it is classical local-tuple input rather than a new RH spectral law.

PL-086 shows that prime-only von-Mangoldt half-weighting on a fixed multiplicative shell is asymptotically just a deterministic envelope: `log p/log X=1+O(1/log X)`. It cannot restore a new prime-only bulk. PL-087 closes the most obvious prime-power escape for the ordinary dimension-normalized bulk: higher prime powers retain the pointwise exponent-depth factor `1/k`, but occupy only vanishing matrix rank, so every weak bulk limit is the same as the prime block, uniformly in the time scale.

## What remains possible

The surviving positive-cone observables are finer than the ordinary bulk: hard-edge statistics, raw or suitably renormalized determinants, growing-order moments, depth-conditioned/subextensive sectors, target-relative/Nyman data, or a completed Weil form that weights the sparse prime-power sector non-macroscopically. Any candidate must show why its statistic is not already determined by bounded-cluster geometry, Hardy--Littlewood local tuples, Poisson sampling, or a vanishing-rank perturbation.

## Status / novelty

The prolate/Nyquist, Hardy--Littlewood, Poisson, bounded-gap, and rank-interlacing ingredients are classical or literature-backed; the persisted findings locate their exact roles in the Prime Lattice hierarchy. The full Poisson bulk statement is conditional on the stated local tuple hierarchy and does not control the hard edge, determinants, or growing-order correlations.

## Falsification criterion

Produce an ordinary dimension-normalized critical prime-support bulk law incompatible with the PL-085 Poisson-sinc moment hierarchy while retaining its hypotheses, or a higher-prime-power sector of nonvanishing matrix density on the fixed shell of PL-087. A positive advance should instead isolate a finer statistic that distinguishes matched Poisson/generalized-prime controls and is not a restatement of classical prime correlations.

## Lean-formalizable core

- Rank/interlacing stability of empirical spectral laws.
- Vanishing-rank contribution of higher prime powers.
- Near-rank-one cluster eigenvalue bounds.
- Moment-to-bulk bookkeeping under a prescribed tuple-correlation hierarchy.
