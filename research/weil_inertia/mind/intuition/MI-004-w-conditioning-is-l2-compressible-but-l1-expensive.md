# MI-004 — The conditioning spectrum has exact cross-conductor structure, but current pair-AP input pays the wrong refinement cost

**Evidence level:** supported by exact Fourier-conductor identities, lossless-sparsification no-go results, and a literature-backed conditioned-pair interface whose source bridge remains explicitly audited

## Core intuition

The `W`-local pair main is not merely an `L^2`-compressible spectrum with a large Wiener norm. Its conductor pieces have genuine projective structure: the corresponding residue-class pair errors form an exact divisor martingale, and reduced additive frequencies are consistent across refinements. The remaining analytic gate is therefore no longer “discover cross-conductor orthogonality.” It is to exploit the orthogonality without paying the full common refinement modulus.

## Strongest justified principle

WI-058--WI-060 establish the basic norm separation. Squared Fourier mass is concentrated at subpolynomial conductors, but no fixed polylogarithmic cutoff captures asymptotically all energy, and a sufficient retained spectrum has super-polylogarithmic Wiener mass. Termwise additive-twist estimates assembled absolutely are therefore structurally too expensive.

WI-061 identifies relevant prior art at the conditioned-pair level: Mikawa's theorem controls twin-prime correlations in residue classes and exposes a modulus-weighted pair-error square function before final Cauchy--Schwarz. This is the right kind of source information missing from ordinary unconditioned pair estimates, but the finding retains its explicit audit boundary and does not by itself splice the Yang geometry.

WI-062 gives a sharp abstract warning for a diagonal conductor-norm assembly, while its current reviewed specialization must not be overused. WI-063 supplies an independent stronger spectral fact: **any** asymptotically lossless selection or attenuation of Fourier modes has conductor-weighted diagonal cost larger than every fixed power of `log X`. Clever sparse pruning or soft tapering therefore cannot make a norm-only assembly cheap.

WI-064 then reveals the missing structure and simultaneously kills its most direct use. After the natural all-residue extension and normalization, Mikawa pair errors satisfy exact conditional-expectation identities on the divisor lattice; equivalent reduced Fourier frequencies agree at every multiple modulus. All conductors dividing one common `Q` are therefore orthogonal coordinates of one fine residue error vector. A single Parseval step can exploit this and replace the diagonal conductor sum by the total retained Fourier energy. But feeding the fine vector into Mikawa's residue-maximum theorem costs a factor `Q`, and any common refinement that captures `1-o(1)` of the local-main energy is super-polylogarithmic. Fixed logarithmic savings still lose.

Thus the surviving interface is very precise: **residue-averaged or vector-valued conditioned pair dispersion across a hierarchy of moduli**, blockwise martingale control, or a direct covariance estimate that sees the projective structure without collapsing it to one huge modulus.

## What remains possible

A blockwise/vector-valued pair-AP theorem could exploit orthogonality at multiple scales while avoiding both the Wiener triangle inequality and the single-refinement `Q` loss. A weighted residue-summed square function is another natural target. A direct source-normalized covariance theorem that never scalarizes conductors separately would also escape the current no-go.

What is no longer enough is to ask generically for “cross-conductor cancellation,” to choose a clever lossless subset of modes, or to combine all modes at one common refinement and invoke a residue maximum.

## Status / novelty

The conductor law, sparsification obstruction, and divisor-martingale identities are persisted exact findings. The Mikawa bridge is literature-backed but retains the evidence boundary recorded in WI-061 and the open review around WI-062; the synthesis relies for its strongest unconditional structural claims on WI-063--WI-064 rather than treating the reviewed specialization as settled.

## Falsification criterion

Find an asymptotically lossless spectral pruning with only polylogarithmic conductor-weighted cost, contradicting WI-063, or a one-common-refinement lossless assembly that avoids the refinement-modulus cost within the current residue-maximal interface, contradicting WI-064. A positive advance should prove a genuinely hierarchical/vector-valued conditioned pair estimate or direct covariance theorem.

## Lean-formalizable core

- Exact conductor-energy product law.
- Lossless-retention versus conductor-weighted-cost inequality.
- Divisor-lattice conditional-expectation identity.
- Consistency of reduced Fourier frequencies across refinements.
