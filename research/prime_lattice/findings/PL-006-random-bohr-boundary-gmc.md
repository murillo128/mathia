# PL-006 — The critical Bohr boundary already exists as a randomized GMC distribution

## Claim

A rigorous renormalized/statistical boundary theory at the prime-lattice radius

\[
|z_p|=p^{-1/2}
\]

already exists. Saksman and Webb show that randomized Euler products with independent Haar prime phases have boundary values on \(\Re s=1/2\) as generalized functions, and that random vertical shifts of the actual Riemann zeta function converge in law to this boundary object.

The limiting boundary is governed by complex Gaussian multiplicative chaos (GMC). However, it is almost surely **not even a complex Borel measure on any open interval**, so this standard boundary object has no ordinary pointwise zero set from which the Riemann zeros could simply be read.

**Evidence/status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION`.

The existence and GMC structure are published theorems. The prime-lattice consequence is the prior-art redirect and the obstruction to a direct pointwise-zero interpretation of this boundary limit.

## Randomized prime-torus boundary

For the first \(N\) primes, define

\[
\zeta_{N,\mathrm{rand}}(s)
=
\prod_{k=1}^{N}
\left(1-p_k^{-s}e^{2\pi i\theta_k}\right)^{-1},
\]

where the \(\theta_k\) are independent uniform variables on \([0,1]\). These are precisely independent Haar phases on the finite prime torus.

Saksman and Webb prove that as \(N\to\infty\),

\[
\zeta_{N,\mathrm{rand}}(1/2+ix)
\]

converges almost surely, in the sense of generalized functions, to a randomized zeta boundary value

\[
\zeta_{\mathrm{rand}}(1/2+ix).
\]

They also identify it as the generalized-function boundary value of a random analytic Euler product in the half-plane \(\Re s>1/2\).

For the actual zeta function, if \(\omega\) is uniform on \([0,1]\), then

\[
\mu_T(x)=\zeta(1/2+ix+i\omega T)
\]

converges in law, after the harmless spatial weight used in the theorem, to this nontrivial random boundary object in \(W^{-\alpha,2}\) for every \(\alpha>1/2\).

Thus the same `1/2` boundary singled out in `PL-001` has a rigorous statistical continuation, but only after weakening the topology from ordinary functions to distributions.

## Prime Gaussian field and multiplicative chaos

A key decomposition is

\[
\log\zeta_{N,\mathrm{rand}}(1/2+ix)
=
\mathcal G_N(x)+\mathcal E_N(x),
\]

where

\[
\mathcal G_N(x)
=
\sum_{k=1}^{N}
\frac{1}{\sqrt{2p_k}}\,
p_k^{-ix}
\left(W_k^{(1)}+iW_k^{(2)}\right)
\]

is a Gaussian prime field and \(\mathcal E_N\) converges smoothly.

The limiting complex field has covariance

\[
\mathbb E\,
\mathcal G(x)\overline{\mathcal G(y)}
=
\log\zeta(1+i(x-y)),
\]

and the randomized zeta boundary factors as a smooth nowhere-zero random function times a complex Gaussian multiplicative chaos distribution.

This is a precise harmonic/probabilistic structure generated directly by the prime frequencies `log p`, not a metaphorical spectral analogy.

## Critical modulus chaos

For normalized modulus powers of the randomized truncated Euler products, the critical GMC exponent is

\[
\beta_c=2.
\]

At \(\beta=\beta_c\), Saksman and Webb prove that

\[
\sqrt{\log\log N}\,
\frac{|\zeta_{N,\mathrm{rand}}(1/2+ix)|^{2}}
{\mathbb E|\zeta_{N,\mathrm{rand}}(1/2+ix)|^{2}}
\,dx
\]

converges in distribution to a nontrivial critical GMC measure.

So a concrete deterministic renormalization exists at the critical prime-lattice boundary. This directly answers the previously natural question whether the divergence at `Re(s)=1/2` can support a nontrivial renormalized boundary theory: **yes, in a stochastic/distributional sense, and this is established prior art**.

## Pointwise-zero obstruction

The same theory imposes a sharp limitation. Saksman and Webb prove that, almost surely,

\[
\zeta_{\mathrm{rand}}(1/2+ix)
\]

does not coincide with a complex Borel measure on any open subinterval of the critical line. It is genuinely a generalized function, not an ordinary function.

Therefore the route

```text
construct the standard Haar-prime/GMC boundary at Re(s)=1/2
-> inspect its pointwise zeros
-> identify the Riemann zeros
```

is not well-defined.

This is a substantive negative result for a natural version of the prime-lattice boundary idea. Any zero mechanism based on this boundary must add structure capable of recovering deterministic/microscopic analytic information rather than treating the generalized-function limit itself as an ordinary zeta function.

## Prior art and novelty assessment

The critical-line generalized-function limit, randomized Euler-product construction, Gaussian decomposition, and GMC interpretation are established results of Saksman and Webb.

No novelty claim is made for the boundary construction or multiplicative-chaos theory.

The Mathia-specific consequence is that the speculative idea of a "renormalized Bohr boundary" is already substantially realized in the literature, while the theorem that the limit is not even a measure sharply rules out the most naive pointwise-zero use of that boundary.

## Boundary conditions and counterarguments

- The theorem is a statement about the **law of random vertical shifts** and randomized Euler products. It is not a deterministic analytic continuation formula for a fixed copy of \(\zeta\).
- The generalized-function limit can encode statistical information without possessing pointwise values.
- The obstruction does not rule out extracting zero statistics from correlations, phase information, microscopic limits, or additional analytic structures.
- Saksman–Webb explicitly distinguish global/mesoscopic statistics from the much harder microscopic scale where individual zeros become visible.
- Existence of a critical GMC measure for \(|\zeta_{N,\mathrm{rand}}|^2\) does not by itself provide a Hilbert–Pólya operator, determinant, or proof of RH.

## Audit criterion

A future boundary-based prime-lattice mechanism must specify what extra datum turns the distribution-valued statistical boundary into deterministic information about individual zeta zeros.

If the proposal uses only the limiting GMC law or generalized boundary distribution and nevertheless assumes pointwise evaluation or a classical zero set, it fails this finding's existence/regularity audit.

## Consequence for the research line

The `Re(s)=1/2` boundary is not an unexplored singular surface. It already carries a rich and rigorous prime-generated random geometry.

The remaining opportunity, if any, lies beyond the coarse statistical boundary: in additional deterministic or microscopic structure that survives analytic continuation and can distinguish the actual zero configuration.
