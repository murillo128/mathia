# MC-031 — Huxley–Watt truncation tails expose a spectral-dimension barrier and an epsilon-dependent Fourier resolution budget

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/BOUNDARY`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

The two decompositions of the Huxley–Watt residual matrix that most directly preserve pre-product-collapse information — spectral truncation and Fourier truncation of the sawtooth kernel — have different quantitative resolution barriers at the RH-compatible scale.

Let

\[
\mathbf m=(\mu(1),\ldots,\mu(N))^{\rm T},
\qquad
Z_{mn}=-\psi\!\left(\frac{N^2}{mn}\right),
\]

where `psi(x)={x}-1/2`. In the exact scale-doubling identity of `MC-020`, the signed residual is `\mathbf m^{\rm T}Z\mathbf m`. Treating this residual separately at the RH-compatible scale requires

\[
\mathbf m^{\rm T}Z\mathbf m=O_\varepsilon(N^{1+\varepsilon}).
\tag{1}
\]

Huxley and Watt give two relevant generic truncation estimates.

First, after ordering the eigenvalues of `Z` and retaining the extreme spectral modes selected by a parameter `R`, their equation (3.6) has normalized tail `O(R^{-1/2})`. For `1\le R\le N/2`, the corresponding unnormalized uncertainty is

\[
O(N^2R^{-1/2}).
\tag{2}
\]

To make (2) as small as `N^{1+\varepsilon}` by this generic bound requires

\[
R\gtrsim N^{2-2\varepsilon}.
\tag{3}
\]

For every fixed `\varepsilon<1/2`, this exceeds the available `O(N)` spectral dimension. Thus the source's generic Parseval/eigenvalue tail estimate cannot certify RH-scale accuracy for any proper spectral truncation. This is not a lower bound on the actual Möbius-weighted tail: sharper arithmetic information about the projections `\widetilde e_k\cdot\mathbf m`, or using the full exact spectrum, may do better.

Second, Huxley and Watt insert the usual truncated Fourier expansion of `-psi` and obtain, for `1\le H\le N`,

\[
\mathbf m^{\rm T}Z\mathbf m
=
\sum_{1\le h\le H}\frac{Q_h(N)}{\pi h}
+
O\!\left(
\frac{N^2(\log N)^2\log H}{H}
\right),
\tag{4}
\]

where

\[
Q_h(N)
=
\sum_{m,n\le N}
\mu(m)\mu(n)
\sin\!\left(\frac{2\pi hN^2}{mn}\right).
\tag{5}
\]

If `H=N^\theta` with fixed `\theta<1`, the source remainder is

\[
N^{2-\theta}\operatorname{polylog}N.
\tag{6}
\]

Hence no one fixed exponent `\theta<1`, independent of the target `\varepsilon`, certifies the full family of bounds (1). But the `O_\varepsilon` quantifier is essential: for each fixed `\varepsilon>0`, choosing

\[
H=N^{1-\delta},
\qquad
0<\delta<\varepsilon,
\tag{7}
\]

makes the source remainder `O_\varepsilon(N^{1+\varepsilon})` after absorbing the logarithms into the power margin. Thus ordinary RH-compatible control does **not** force a single schedule `H=N^{1-o(1)}` as `N\to\infty`. The correct uniform statement is that the admissible Fourier exponent must approach `1` only as the requested target exponent `\varepsilon` approaches `0`; no fixed sublinear exponent works simultaneously for every `\varepsilon`.

Finally, applying absolute values separately to the retained Fourier modes gives

\[
\left|\sum_{h\le H}\frac{Q_h(N)}{\pi h}\right|
\le
\frac1\pi\sum_{h\le H}\frac{|Q_h(N)|}{h}.
\tag{8}
\]

For any polynomial choice `H=N^{1-\delta}` with fixed `\delta<1`, a uniform estimate `|Q_h(N)|\le B(N)` therefore needs essentially

\[
B(N)\lesssim \frac{N^{1+\varepsilon}}{\log N}
\tag{9}
\]

to reach (1) by triangle inequality. Since the trivial bound is `Q_h(N)=O(N^2)`, termwise mode control still asks for a square-root-scale gain in a two-variable Möbius quadratic sum. The Fourier expansion reorganizes the signed information but does not create that cancellation automatically.

The surviving mechanisms are correspondingly specific: arithmetic control of the spectral projections stronger than the generic tail estimate; joint cancellation across the `h`-family before absolute values; a sharper source-natural Fourier remainder; or cancellation of `\mathbf m^{\rm T}Z\mathbf m` with the harmonic/coarse terms in the unsplit Huxley–Watt identity. None is ruled out here.

## 1. Critical residual scale

For `g=1`, Huxley and Watt's exact matrix identity is

\[
M(N^2)=2M(N)-\mathbf m^{\rm T}A\mathbf m,
\tag{10}
\]

with

\[
A=N^2\mathbf f\mathbf f^{\rm T}-\frac12\mathbf u\mathbf u^{\rm T}+Z.
\tag{11}
\]

As recorded in `MC-020`, this yields

\[
M(N^2)
=2M(N)-N^2H(N)^2+\frac12M(N)^2-\mathbf m^{\rm T}Z\mathbf m.
\tag{12}
\]

At target horizon `N^2`, RH-scale cancellation is `O_\varepsilon(N^{1+\varepsilon})`. Equation (1) is therefore the natural target only for a strategy that estimates the `Z`-quadratic form separately. The line has already established that this separation can be lossy: a coupled proof may obtain cancellation between the displayed terms without satisfying (1) term by term.

The present result audits the separate-residual route because both source truncations are proposed decompositions of exactly that residual information.

## 2. Spectral truncation has only an `R^{-1/2}` generic normalized tail

Huxley and Watt diagonalize `Z`, writing its ordered eigenvalues as `\widetilde\lambda_k` and the corresponding orthonormal eigenvectors as `\widetilde e_k`. Their equation (3.6), after the two explicit rank-one pieces in (11) are separated, retains modes satisfying

\[
\min\{k,N+1-k\}<R
\]

and places the omitted contribution in an `O(R^{-1/2})` normalized remainder.

When `R\le N/2`, the retained set contains at most `2R` modes. Multiplying the normalized formula by `N^2` gives (2). If this source-generic remainder were the only tail information available, imposing target accuracy `N^{1+\varepsilon}` gives (3).

For every fixed `\varepsilon<1/2`, the right-hand side of (3) grows faster than `N`; hence no proper `O(N)`-dimensional truncation can be certified at the target scale from this estimate. Taking all `N` eigenmodes is, of course, the exact spectral decomposition and has no actual tail. The conclusion is therefore not that spectral information is useless, but that **dimensional truncation plus the generic eigenvalue/Parseval bound is not the missing power gain**.

A successful spectral continuation must prove something arithmetic about the Möbius projections `(\widetilde e_k\cdot\mathbf m)^2`, or obtain a substantially sharper tail estimate adapted to `\mathbf m`, rather than relying only on the ambient operator spectrum.

## 3. Fourier truncation has an epsilon-dependent polynomial resolution budget

Huxley and Watt also substitute the standard truncated Fourier expansion of `-psi` into `Z`. Their resulting formula is (4), with the matrices `Z(h)` having entries

\[
Z(h)_{mn}=\sin\!\left(\frac{2\pi hN^2}{mn}\right).
\tag{13}
\]

The quadratic form of `Z(h)` against `\mathbf m` is exactly (5). Put `H=N^\theta` with fixed `0<\theta\le1`. The source remainder becomes

\[
O\!\left(N^{2-\theta}(\log N)^2\log H\right).
\tag{14}
\]

If `\theta=1-\delta` for fixed `\delta>0`, then (14) is `O(N^{1+\delta}\operatorname{polylog}N)`. This fails the target (1) whenever the requested `\varepsilon` is smaller than `\delta`, so no fixed deficit `\delta>0` works for the complete `O_\varepsilon` family.

However, for a **fixed** target `\varepsilon>0`, the truncation parameter may depend on that fixed `\varepsilon`. Choosing, for example,

\[
\delta=\varepsilon/2,
\qquad
H=N^{1-\varepsilon/2},
\tag{15}
\]

gives

\[
\frac{N^2(\log N)^2\log H}{H}
=
N^{1+\varepsilon/2}\operatorname{polylog}N
=
O_\varepsilon(N^{1+\varepsilon}).
\tag{16}
\]

More generally any fixed `0<\delta<\varepsilon` works, with the logarithmic margin absorbed into `N^{\varepsilon-\delta}`. Therefore the source remainder itself permits a genuinely sublinear polynomial number of frequencies for every fixed `\varepsilon`; what it forbids is a **single fixed polynomial compression exponent** `\theta<1` that works uniformly across arbitrarily small `\varepsilon`.

This is a resolution statement, not a lower bound for the true Fourier tail. A new arithmetic estimate for the truncation error could change it further. The precise negative conclusion is that the standard sawtooth Fourier remainder does not reduce the entire RH-equivalent `O_\varepsilon` family to `N^\theta` reciprocal-phase modes for one universal `\theta<1`.

## 4. Separate mode bounds still carry a square-root-scale cancellation burden

Each `Q_h(N)` in (5) contains `O(N^2)` bounded terms. Using only `|\mu|\le1` gives

\[
|Q_h(N)|\le N^2.
\tag{17}
\]

If the modes are combined by absolute values, (8) and `\sum_{h\le H}1/h=\log H+O(1)` show that a uniform mode estimate contributes `O(B(N)\log H)`. For the polynomial schedules in (7), `\log H\asymp\log N`, giving (9).

Thus the correction to the resolution quantifier does not remove the termwise-cancellation bottleneck: a triangle-inequality proof still needs `Q_h(N)` to save almost one full power of `N` relative to the trivial `N^2` count, up to the target `N^\varepsilon` slack and logarithms. No independence assumption justifies such a bound, because the coefficients factor as `\mu(m)\mu(n)` and the phase depends on the reciprocal product `mn`.

There is a distinct possible escape. The signed values `Q_h(N)` may cancel across `h`, so a theorem for the weighted aggregate in (4) could be much stronger than triangle inequality even when no uniform individual estimate is available. Such a theorem would be a genuinely new arithmetic input and is not supplied by the Fourier identity itself.

## 5. Prior art and novelty boundary

The exact matrix identity, decomposition (11), spectral formula with `O(R^{-1/2})` normalized tail, and Fourier formula (4) are all from M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the Möbius function*, Chebyshevskii Sbornik 19(3) (2018), 20–34, DOI `10.22405/2226-8383-2018-19-3-20-34`, arXiv `1807.05890`; see `MC-S24`. The source states the Fourier decomposition with error `O(N^2(\log N)^2\log H/H)` for `H=1,2,\ldots,N` and notes that proper use of the truncation remained unexplored there.

The arithmetic in (2)–(9) and (14)–(16) is scale bookkeeping applied to those published error terms. A targeted prior-art check around the source and the later spectral study of the same sawtooth kernel found an established operator/eigenvalue program, so no novelty is claimed for the kernel, its spectrum, the Fourier expansion, or spectral approximation as a research direction.

The durable line-specific result is the quantitative mechanism boundary: **the published generic truncation estimates do not by themselves provide one low-complexity representation that certifies the full RH-compatible family**. Spectrally, the generic proper-truncation certificate stalls above the critical scale. Fourier-theoretically, a fixed target `\varepsilon` admits `H=N^{1-\delta(\varepsilon)}` for any `0<\delta(\varepsilon)<\varepsilon`, but no exponent `\theta<1` independent of `\varepsilon` works for every target. Termwise control of the retained modes still requires a nearly square-root-scale bilinear gain.

## 6. Consequence for the active frontier

`MC-029` showed that total-product collapse destroys the remaining cutoff provenance and reconstructs the Möbius target itself. The present finding tests the opposite move: retain the pre-collapse sawtooth kernel but decompose it spectrally or harmonically.

That move preserves genuinely more structure, but the generic approximation machinery is not yet a bootstrap. The spectral route requires arithmetic information about Möbius projections beyond the ambient eigenvalue tail. The Fourier route has more room than a near-linear-in-`N` claim would suggest for each fixed `\varepsilon`, yet a universal fixed compression exponent cannot cover the whole RH-equivalent family, and triangle-inequality control of the retained modes still asks for a power-sized arithmetic gain.

The next useful question should therefore distinguish the two routes rather than treating their truncation budgets as identical: whether the Möbius vector has atypically small projections on dangerous kernel eigenspaces; whether the reciprocal-phase family `Q_h(N)` has joint cancellation stronger than termwise bounds; whether one can improve the Fourier remainder using arithmetic information about the reciprocal products; or whether the unsplit matrix identity forces cancellation between the residual and the RH-equivalent harmonic coarse mode.

A candidate that only invokes the source's ambient spectral tail cannot reach the critical power scale. A Fourier candidate may choose an `\varepsilon`-dependent sublinear polynomial cutoff, but must still produce the missing arithmetic cancellation rather than obtaining it from truncation bookkeeping alone.