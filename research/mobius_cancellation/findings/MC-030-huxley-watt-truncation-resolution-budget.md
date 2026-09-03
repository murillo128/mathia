# MC-030 — Huxley–Watt spectral and Fourier truncations do not reach the critical scale from their generic tail bounds

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/BOUNDARY`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

The two decompositions of the Huxley–Watt residual matrix that most directly preserve pre-product-collapse information — spectral truncation and Fourier truncation of the sawtooth kernel — have a precise resolution budget. The generic remainder estimates proved in the source do not by themselves reduce the Möbius problem to a small finite family of modes at the critical square-root scale.

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

First, after ordering the eigenvalues of `Z` and retaining the extreme spectral modes selected by a parameter `R`, their equation (3.6) has normalized tail

\[
O(R^{-1/2}).
\]

For a genuine truncation with `1\le R\le N/2`, at most `2R` extreme modes are retained, so the corresponding unnormalized uncertainty is

\[
O(N^2R^{-1/2}).
\tag{2}
\]

To make (2) as small as `N^{1+epsilon}` by this bound would require

\[
R\gtrsim N^{2-2\varepsilon},
\tag{3}
\]

which exceeds the available `O(N)` spectral dimension whenever `epsilon<1/2`. Thus the source's generic Parseval/eigenvalue tail estimate cannot certify RH-scale accuracy for any proper spectral truncation. This is not a lower bound on the actual tail: sharper arithmetic information about the projections `e_k\cdot\mathbf m`, or using the full exact spectrum, may do better.

Second, Huxley and Watt insert the usual truncated Fourier expansion of `-psi` and obtain, for `2\le H\le N`,

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

If one relies only on the remainder in (4), a truncation `H=N^theta` certifies an error of order

\[
N^{2-\theta}\,\operatorname{polylog}N.
\tag{6}
\]

Consequently no fixed `theta<1` can certify the full family of RH-compatible bounds (1): for any fixed deficit `delta=1-theta>0`, the available error is `N^{1+delta}` up to logarithms. To make the source remainder itself compatible with (1) for arbitrarily small `epsilon`, one must take

\[
H=N^{1-o(1)}
\tag{7}
\]

(up to the explicit logarithmic factors). Fourier truncation therefore replaces the residual by an almost linearly growing family of reciprocal-phase quadratic sums unless one proves a sharper remainder theorem.

Finally, applying absolute values separately to the Fourier modes gives

\[
\left|\sum_{h\le H}\frac{Q_h(N)}{\pi h}\right|
\le
\frac1\pi\sum_{h\le H}\frac{|Q_h(N)|}{h}.
\tag{8}
\]

A uniform estimate `|Q_h(N)|\le B(N)` would therefore need essentially

\[
B(N)\lesssim \frac{N^{1+\varepsilon}}{\log H}
\tag{9}
\]

to reach (1) by triangle inequality when `H=N^{1-o(1)}`. Since the trivial bound is `Q_h(N)=O(N^2)`, the missing input is already square-root-scale cancellation in a two-variable Möbius quadratic sum. The Fourier expansion reorganizes the signed information but does not create that cancellation automatically.

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
=2M(N)-N^2H(N)^2+rac12M(N)^2-\mathbf m^{\rm T}Z\mathbf m.
\tag{12}
\]

At target horizon `N^2`, RH-scale cancellation is `O_epsilon(N^{1+epsilon})`. Equation (1) is therefore the natural target only for a strategy that estimates the `Z`-quadratic form separately. The line has already established that this separation can be lossy: a coupled proof may obtain cancellation between the displayed terms without satisfying (1) term by term.

The present result audits the separate-residual route because both source truncations are proposed decompositions of exactly that residual information.

## 2. Spectral truncation has only an `R^{-1/2}` generic normalized tail

Huxley and Watt diagonalize `Z`, writing its ordered eigenvalues as `tilde lambda_k` and the corresponding orthonormal eigenvectors as `tilde e_k`. Their equation (3.6), after the two explicit rank-one pieces in (11) are separated, retains modes satisfying

\[
\min\{k,N+1-k\}<R
\]

and places the omitted contribution in an `O(R^{-1/2})` normalized remainder.

When `R\le N/2`, the retained set contains at most `2R` modes. Multiplying the normalized formula by `N^2` gives (2). If this source-generic remainder were the only tail information available, imposing target accuracy `N^{1+epsilon}` gives (3).

For every fixed `epsilon<1/2`, the right-hand side of (3) grows faster than `N`; hence no proper `O(N)`-dimensional truncation can be certified at the target scale from this estimate. Taking all `N` eigenmodes is, of course, the exact spectral decomposition and has no actual tail. The conclusion is therefore not that spectral information is useless, but that **dimensional truncation plus the generic eigenvalue/Parseval bound is not the missing power gain**.

A successful spectral continuation must prove something arithmetic about the Möbius projections `(tilde e_k\cdot\mathbf m)^2`, or obtain a substantially sharper tail estimate adapted to `\mathbf m`, rather than relying only on the ambient operator spectrum.

## 3. Fourier truncation needs near-linear frequency resolution under the source remainder

Huxley and Watt also substitute the standard truncated Fourier expansion of `-psi` into `Z`. Their resulting formula is (4), with the matrices `Z(h)` having entries

\[
Z(h)_{mn}=\sin\!\left(\frac{2\pi hN^2}{mn}\right).
\tag{13}
\]

The quadratic form of `Z(h)` against `\mathbf m` is exactly (5). Put `H=N^theta` with fixed `0<theta\le1`. The source remainder becomes

\[
O\!\left(N^{2-\theta}(\log N)^2\log H\right),
\tag{14}
\]

which proves (6).

Suppose `theta=1-delta` for a fixed `delta>0`. Then (14) is only an `O(N^{1+delta}\operatorname{polylog}N)` certificate. Choosing any target epsilon smaller than `delta` shows that this bound does not reach the RH-compatible scale. Thus any use of the published remainder estimate that aims at all `epsilon>0` must let `delta` tend to zero, giving (7).

This is a resolution statement, not a lower bound for the true Fourier tail. A new arithmetic estimate for the truncation error could change it. What fails is the idea that the standard sawtooth Fourier remainder already reduces the problem to finitely many, or `N^theta` with fixed `theta<1`, reciprocal-phase modes without paying a power loss.

## 4. Separate mode bounds still carry the square-root cancellation burden

Each `Q_h(N)` in (5) contains `O(N^2)` bounded terms. Using only `|mu|<=1` gives

\[
|Q_h(N)|\le N^2.
\tag{15}
\]

If the modes are then combined by absolute values, (8) and the harmonic sum `sum_{h<=H}1/h=log H+O(1)` show that a uniform mode estimate contributes `O(B(N)log H)`. This gives the necessary target *for that proof architecture* in (9).

For `H=N^{1-o(1)}`, the required bound is essentially `N^{1+epsilon}` per mode, up to logarithms: square-root scale relative to the `N^2` summands. No independence assumption justifies such a bound, because the coefficients factor as `mu(m)mu(n)` and the phase depends on the reciprocal product `mn`.

There is a distinct possible escape. The signed values `Q_h(N)` may cancel across `h`, so a theorem for the weighted aggregate in (4) could be much stronger than triangle inequality even when no uniform individual estimate is available. Such a theorem would be a genuinely new arithmetic input and is not supplied by the Fourier identity itself.

## 5. Prior art and novelty boundary

The exact matrix identity, decomposition (11), spectral formula with `O(R^{-1/2})` normalized tail, and Fourier formula (4) are all from M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the Möbius function*, Chebyshevskii Sbornik 19(3) (2018), 20–34, DOI `10.22405/2226-8383-2018-19-3-20-34`, arXiv `1807.05890`; see `MC-S24`. The authors explicitly present spectral, Fourier, and Perron decompositions as possible ways to investigate the Mertens quadratic form, and state that they had not yet explored proper use of the Fourier truncation.

The arithmetic in (2)–(9) is only scale bookkeeping applied to those published error terms. A targeted prior-art check around the source and the later spectral study of the same sawtooth kernel found an established operator/eigenvalue program, so no novelty is claimed for the kernel, its spectrum, the Fourier expansion, or spectral approximation as a research direction.

The durable line-specific result is the quantitative mechanism boundary: **the published generic truncation errors do not themselves convert the pre-collapse Huxley–Watt residual into a low-complexity RH-scale observable**. Spectrally, the generic proper-truncation certificate stalls above the critical scale; Fourier-theoretically, the published remainder requires near-linear frequency resolution, after which termwise mode control still demands a square-root-scale bilinear gain.

## 6. Consequence for the active frontier

`MC-029` showed that total-product collapse destroys the remaining cutoff provenance and reconstructs the Möbius target itself. The present finding tests the opposite move: retain the pre-collapse sawtooth kernel but decompose it spectrally or harmonically.

That move preserves genuinely more structure, but the generic approximation machinery is not yet a bootstrap. The next useful question must be arithmetic rather than representational: whether the Möbius vector has atypically small projections on the dangerous kernel eigenspaces, whether the reciprocal-phase family `Q_h(N)` has a joint cancellation law stronger than termwise estimates, or whether the unsplit matrix identity forces cancellation between the residual and the RH-equivalent harmonic coarse mode.

A candidate that only lowers the number of retained modes while using the source's ambient tail estimates cannot reach the critical power scale. A candidate that can prove a fixed-power improvement for the Möbius-weighted spectral projections or the joint `h`-sum from information weaker than RH would constitute genuinely new progress.