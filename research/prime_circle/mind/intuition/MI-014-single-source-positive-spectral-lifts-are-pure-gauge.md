# MI-014 — Single-source positive spectral lifts of the dual phase field are pure gauge

**Evidence level:** exact for fixed source-independent masks and Hermitian kernels through [PC-278](../../findings/PC-278-single-source-dual-window-phase-spectra-are-diagonal-unitary-pure-gauge.md). Source-dependent selection, anchor-sensitive nonlinearities, genuine flux, cross-source/cross-level couplings, and nonnormal constructions outside unitary invariants remain open.

Retaining the full dual-window phase field looks strictly richer than minimizing it to one scalar near-resonance. For a single source pair `(p,r)`, however, a fixed two-dimensional mask

`W_(p,r)(h,k)=A_(h,k) zeta_q^(hp+kr)`

factorizes exactly as

`W_(p,r)=D_p A E_r`

with diagonal unitaries `D_p,E_r`. Therefore every singular value, Schatten norm, rank and Gram spectrum is independent of the source. The source phases survive entrywise but disappear completely under the positive spectral quotient.

The same statement holds for a fixed Hermitian coefficient-graph kernel. Source modulation has the form

`K^(p,r) = U_(p,r) K U_(p,r)^*`,

because the edge phase is the discrete gradient `(u-v).(p,r)`. Every cycle has trivial holonomy. The source contributes only an exact coboundary gauge, so Hermitian spectrum, resolvent traces, heat traces and inertia are all source-independent.

This is stronger than a matched-control asymptotic. **Every source pair is exactly isospectral at every finite denominator and bandwidth** inside this category. Merely retaining vector/directional phase information does not help if the next operation immediately quotients it by diagonal-unitary equivalence.

The scalar near-resonance observable escapes because it first compares each phase to the distinguished anchor `1`; that nonlinearity breaks the gauge before compression. Other genuine escapes must likewise introduce a gauge-invariant source relation before taking positive spectral invariants: source-dependent phase selection, nonzero cycle flux, relative phases between different sources or levels, or a justified nonnormal identification not preserved by left/right unitary equivalence.

**Research consequence.** Do not use a fixed positive/Hermitian spectral wrapper as the default “richer” continuation of PC-277. First identify what breaks the single-source coboundary gauge, then audit that new object against source-only controls.

**Boundary.** PC-278 does not say that every spectralization is source-blind, and it does not close the intermediate scalar rational-microscopic window. It closes the fixed single-source positive/Hermitian route.
