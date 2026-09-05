# PL-177 — Prime-density source-forced affine closure is Davenport-flat

## Claim

A canonical sparse/source-forced escape left open by `PL-176` also collapses unconditionally once both source directions are averaged at prime density.

Let `lambda` be the Liouville function and let `A_X` be any finite subset of `(X,2X]`. For `n>=1` and `a,b in A_X`, the four integers

\[
n,\qquad an,\qquad bn,\qquad (a+b-1)n
\]

form an ordinary additive parallelogram, because

\[
an+bn=n+(a+b-1)n.
\]

Complete multiplicativity gives the exact reduction

\[
\lambda(n)\lambda(an)\lambda(bn)\lambda((a+b-1)n)
=\lambda(a)\lambda(b)\lambda(a+b-1).
\]

Define the normalized two-source average

\[
Q(A_X)=\frac1{|A_X|^2}
\sum_{a,b\in A_X}
\lambda(a)\lambda(b)\lambda(a+b-1).
\]

Then for every fixed `C>0`,

\[
\boxed{
|Q(A_X)|\ll_C
\frac{X}{|A_X|(\log X)^C}.
}
\]

Consequently, if `|A_X| >= X/(log X)^K` for some fixed `K`, then `Q(A_X)` decays faster than every prescribed negative power of `log X` after renaming the Davenport exponent.

In particular, if `A_X` is the set of primes in `(X,2X]`, then `lambda(p)=lambda(q)=-1`, so

\[
Q(A_X)
=
\frac1{\pi(2X)-\pi(X)}^2
\sum_{X<p,q\le2X}\lambda(p+q-1)
\longrightarrow0
\]

with arbitrary logarithmic-power saving. Thus the source-forced pattern obtained by taking two prime-axis multipliers and closing their additive parallelogram does **not** retain a non-Haar parity invariant after broad averaging over both prime axes.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART/REDIRECT + NEGATIVE/OBSTRUCTION`. The exact prime-axis reduction is elementary. The cancellation uses the classical Davenport uniform exponential-sum estimate for Liouville, already derived line-locally in `PL-176`; closely adjacent published prior art of Banks--Shparlinski proves strong cancellation for related prime-pair additive Möbius sums. This finding is decisive only for **two-source affine closure averaged over a polylogarithmically dense source family**, including the primes. It does not control a fixed prime pair, a single-axis average, a thinner source family, a jointly conditioned pair family, or a completed/target-relative coupling.

## Exact prime-lattice / additive closure

In exponent coordinates,

\[
\lambda(m)=(-1)^{\langle v(m),\mathbf 1\rangle}.
\]

Multiplying the base point `n` by `a` or `b` is translation of `v(n)` by `v(a)` or `v(b)` in the positive exponent lattice. For primes `p,q`, these are the canonical basis translations `e_p,e_q`. The fourth point is not the multiplicative corner `pqn`; it is chosen by ordinary additive closure:

\[
(p+q-1)n=n+(p-1)n+(q-1)n.
\]

Hence the configuration mixes the intrinsic prime-axis action with an external additive parallelogram in a source-forced way. It is genuinely outside the complete `(x,h,k)` direction averaging treated by `PL-176`: the shifts `(p-1)n,(q-1)n` are tied to the multiplicative source and the base point.

Nevertheless, parity collapses before any averaging. Complete multiplicativity gives

\[
\begin{aligned}
&\lambda(n)\lambda(an)\lambda(bn)\lambda((a+b-1)n)\\
&\qquad=\lambda(n)^4\lambda(a)\lambda(b)\lambda(a+b-1)\\
&\qquad=\lambda(a)\lambda(b)\lambda(a+b-1).
\end{aligned}
\]

The base point disappears exactly. In the prime case the two source signs also disappear, leaving only `lambda(p+q-1)`. Thus averaging over `n` cannot restore information lost by this configuration.

## Fourier reduction for an arbitrary source family

Write

\[
W_{A_X}(\theta)
=
\sum_{a\in A_X}\lambda(a)e(a\theta)
\]

and

\[
F_{4X}(\theta)
=
\sum_{m\le4X}\lambda(m)e(-m\theta),
\qquad e(t)=e^{2\pi i t}.
\]

Since `a,b in (X,2X]`, the value `m=a+b-1` lies in the support of `F_{4X}`. Fourier orthogonality therefore gives the exact identity

\[
\boxed{
\sum_{a,b\in A_X}
\lambda(a)\lambda(b)\lambda(a+b-1)
=
\int_0^1
W_{A_X}(\theta)^2F_{4X}(\theta)e(-\theta)\,d\theta.
}
\]

No distribution theorem for the source set is used in this identity. By Cauchy/triangle inequality and Parseval,

\[
\left|\sum_{a,b\in A_X}
\lambda(a)\lambda(b)\lambda(a+b-1)\right|
\le
\|F_{4X}\|_\infty
\int_0^1|W_{A_X}(\theta)|^2d\theta
=
\|F_{4X}\|_\infty |A_X|.
\]

The source family enters only through its cardinality.

## Davenport input

Davenport's classical estimate gives, for every fixed `C>0`,

\[
\sup_{\theta\in\mathbf R}
\left|\sum_{m\le M}\mu(m)e(m\theta)\right|
\ll_C \frac{M}{(\log M)^C}.
\]

As in `PL-176`, the Liouville form follows from the exact square-divisor identity

\[
\lambda(n)=\sum_{d^2\mid n}\mu(n/d^2).
\]

Indeed,

\[
\sum_{n\le M}\lambda(n)e(n\theta)
=
\sum_{d\le\sqrt M}
\sum_{r\le M/d^2}\mu(r)e(rd^2\theta).
\]

Splitting at `d=M^{1/4}`, Davenport handles the first range uniformly in `theta`, while the trivial bound contributes `O(M^{3/4})` in the second. After renaming the arbitrary logarithmic exponent,

\[
\boxed{
\|F_M\|_\infty
\ll_C \frac{M}{(\log M)^C}
}
\]

for every fixed `C>0`.

Applying this at `M=4X` to the exact Fourier identity gives

\[
\left|\sum_{a,b\in A_X}
\lambda(a)\lambda(b)\lambda(a+b-1)\right|
\ll_C
\frac{X|A_X|}{(\log X)^C},
\]

hence the claimed normalized bound

\[
|Q(A_X)|
\ll_C
\frac{X}{|A_X|(\log X)^C}.
\]

If `|A_X| >= X/(log X)^K`, then for every desired `A>0` choose Davenport exponent `C>A+K` to obtain `Q(A_X) <<_A (log X)^{-A}`. For the prime source, the prime number theorem gives `|A_X| asymp X/log X`, so the hypothesis holds with `K=1`.

The important point is structural: **prime sparsity is nowhere near sparse enough to evade the uniform Fourier bound once both source axes are averaged independently**.

## Prior-art / novelty audit

This is a research exclusion, not a novelty claim.

- H. Davenport, “On some infinite series involving arithmetical functions (II),” *The Quarterly Journal of Mathematics* **os-8**(1) (1937), 313--320, DOI `10.1093/qmath/os-8.1.313`, is the classical source for the uniform logarithmic-power Möbius exponential-sum estimate. The Liouville variant used here follows by the displayed square-divisor identity.
- William D. Banks and Igor E. Shparlinski, “Multiple sums with the Möbius function,” *The Quarterly Journal of Mathematics* **77**(1) (March 2026), 109--127, DOI `10.1093/qmath/haaf049`, establish strong cancellation for a broad family of additive Möbius sums; in particular their applications include sums of `mu(p+q)` over prime pairs. This is close prior art for the additive-convolution mechanism, although it is not the exact shifted Liouville statistic above.
- `PL-176` already records the line-local Davenport-to-Liouville reduction and shows that complete additive-cube averaging is Fourier/Gowers-flat. The present result tests the specific residual class that `PL-176` deliberately left open: source-forced sparse directions tied to multiplicative prime axes.

Targeted searches for the exact four-point identity with `(n,an,bn,(a+b-1)n)` and for the exact dyadic `lambda(p+q-1)` average did not reveal a matching published formulation. That does not support a novelty claim: the proof is an immediate application of classical Fourier orthogonality plus Davenport, and the 2026 Banks--Shparlinski paper shows that closely neighboring prime-pair Möbius cancellation is already an explicit literature topic.

## Adversarial checks and limitations

- **Not a fixed-pair Chowla result.** The proof averages over both source variables. It gives no cancellation for a prescribed pair `(a,b)` or `(p,q)`.
- **Not a single-axis theorem.** If one source direction is fixed and only the other is averaged, the `L^2`/Parseval gain used above no longer produces the same normalized estimate automatically.
- **Polylogarithmic density is essential to this argument.** Davenport supplies arbitrary powers of `log`, not a fixed power of `X`. The bound is decisive for primes and any source family of size at least `X/(log X)^K`, but it does not settle genuinely thin families of size `X^{1-delta}` or smaller.
- **Independent double averaging is essential.** A coupled condition on `(a,b)`, a thin curve in source-pair space, phase conditioning, or another non-product sampling rule can destroy the exact `W(θ)^2` reduction and needs a separate test.
- **No analytic continuation or critical-line mechanism.** Everything is a finite additive Fourier estimate. The result does not use the functional equation, zeros, or continuation of zeta and therefore cannot single out `Re(s)=1/2`.
- **The base variable carries no hidden rescue.** Its disappearance is exact from `lambda(n)^4=1`; no choice of averaging measure in `n` can restore it for this observable.
- **Operator or spectral repackaging adds nothing.** Any trace whose scalar expansion is this two-source average inherits the same Fourier bound unless additional target-relative data are inserted before the source averaging.

## Consequence for the research line

`PL-176` left source-forced sparse configurations as a legitimate escape because complete additive-cube averaging can erase arithmetic information that a non-diffuse source might retain. The present calculation shows that **source forcing and prime sparsity alone are insufficient**. When the source directions are generated independently from a family as large as the primes and the fourth vertex is obtained by the canonical additive closure, complete multiplicativity collapses the degree-four parity to a one-dimensional additive Liouville observable, and Davenport plus Parseval flattens the remaining double-source average.

The active affine clue should therefore exclude this entire polylog-dense two-source closure family. Surviving candidates must prevent the multiplicative collapse, avoid broad independent averaging over both source axes, use a genuinely thinner or jointly constrained source geometry, or introduce a completed/target-relative coupling before the Fourier flattening occurs. Fixed/single-axis and phase-conditioned variants remain mathematically open to this argument and should not be conflated with the eliminated family.