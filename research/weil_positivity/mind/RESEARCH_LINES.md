# Weil-positivity research lines

This file holds the current mathematical lines of investigation suggested by the durable Weil-positivity intuitions. It is not a roadmap, task queue, status page, or history.

## Build a source-native critical boundary correspondence in a category large enough for the Mangoldt spectrum

**Linked intuitions:** `MI-001-positivity-needs-a-sign-producing-global-operation`, `MI-010-source-forced-critical-gram-can-have-the-wrong-weil-orientation`, `MI-011-prime-ray-marginals-do-not-determine-mixed-prime-coupling`, `MI-012-automorphic-multiplicity-does-not-prevent-global-scalarization`, `MI-013-critical-sector-transport-needs-new-global-arithmetic-structure`.

WP-216--WP-266 separate coefficient sourcing, interaction, regulator covariance, critical normalization, and finite-part sign. Hamiltonian diagonal centering gives a regulator-independent trace-class index-one operator below critical scale, but source-canonical transport to the Weil half-density produces a non-square-summable critical row.

WP-267 shows that ordinary linear-relation closure is too destructive: it makes the critical boundary coordinate maximally multivalued and deletes the common-vacuum coherence. WP-268 then shows that the row itself is naturally hostable on the source-generated rapid-energy nuclear rigging

\[
\Phi_{\exp}=\bigcap_{a>0}\operatorname{Dom}e^{aH},
\]

although no finite polynomial Hamiltonian scale suffices.

WP-269 now classifies the corresponding **stationary positive-covariance** category. The exact source-native critical spectral measure

\[
\nu_{1/2}
=
\frac12\sum_{p,k\ge1}
(\log p)p^{-k/2}
\bigl(\delta_{k\log p}+\delta_{-k\log p}\bigr)
\]

is not tempered and is not infra-exponentially tempered. Its exponential damping threshold is exact:

\[
\int e^{-a|\xi|}\,d\nu_{1/2}(\xi)<\infty
\quad\Longleftrightarrow\quad
a>\frac12.
\]

Therefore ordinary positive-definite distributions are ruled out by Bochner--Schwartz, and positive-definite Fourier hyperfunctions are still too small. A source-faithful positive stationary covariance with these exact masses can live only in a larger exponential-growth category such as Fourier ultra-hyperfunctions, or after a source-forced cancellation/quotient changes the spectral growth before positivity is read.

This sharpens the live theorem. Merely finding a topology that hosts the critical boundary functional is no longer enough, and neither is invoking ordinary generalized-function positivity. A viable construction must derive from the source a finite--archimedean correspondence in an admissible exponential-type category, preserve mixed-prime coherence, remain regulator-covariant, and still force the Weil translation/autocorrelation orientation. Alternatively it must change the positive spectrum structurally before the stationary boundary law is formed.

## Treat amplitude hostability, spectral-growth category, mixed-prime coherence, and Weil orientation separately

WP-268 and WP-269 expose two different category thresholds. The **amplitude** row becomes continuous at a single exponential Hilbert level only beyond energy exponent `1/4`; after squaring to spectral mass, the positive stationary measure requires damping beyond `1/2`. The factor of two is the expected amplitude-to-mass transition, not a new positivity mechanism.

The reusable warning is that a canonical distributional host can coexist with failure of every standard positive-definite distribution/hyperfunction realization. Enlarging the test category preserves existence, but the source must still determine the boundary law and the completed finite--archimedean orientation. Ultra-hyperfunctional admissibility, if used, is only a category permission, not a Weil-positivity theorem.
