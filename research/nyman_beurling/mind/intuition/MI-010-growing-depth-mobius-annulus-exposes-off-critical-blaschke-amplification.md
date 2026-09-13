# MI-010 — Growing depth exposes a Möbius near-kernel and off-critical Blaschke amplification

**Evidence level:** exact through [NB-092](../../findings/NB-092-growing-depth-mobius-annulus-mode-forces-polynomial-blaschke-gram-gain.md) for the raw growing-depth Gram direction and the amplification caused by any fixed off-critical zero. The bridge from unnormalized generalized Gram gain to normalized radial/entropy obstruction remains open.

Every fixed multiplicative-depth band is source-silent after subtracting its universal raw Gram baseline, but the constants in that statement deteriorate with depth. NB-092 shows that this nonuniformity carries actual arithmetic structure rather than being merely technical.

On the growing band `I_(m,q)={m,...,mq-1}`, the coefficient choice

`c_j = m^(-1) sum_(d<=floor(j/m)) mu(d)/d`

is the Möbius inverse of a constant integer-cell profile. Its raw visible combination is exactly the flat logarithmic annulus `e^(-t/2) 1_[log m,log(mq))`. The raw Rayleigh quotient is therefore controlled by

`Q_q = sum_(r<q) |sum_(d<=r) mu(d)/d|^2`,

and `lambda_min(K_tilde_(m,mq)) <= (1-1/q)/Q_q`.

The same `Q_q` detects the zero frontier. If `Theta=sup Re rho`, then

`limsup log Q_q / log q >= 2Theta-1`.

Under false RH, the raw growing-depth band consequently loses every depth-uniform spectral floor along this canonical Möbius direction. This is qualitatively different from the fixed-depth calibrated regime.

More importantly, the arithmetic inner factor amplifies **that same direction**. A single off-critical zero `rho=beta+i gamma` makes the fully Blaschke-deflated energy at least `q^(2beta-1)` times the raw annulus energy up to a zero-dependent constant. Since the remaining generalized eigenvalues are at least one, the determinant ratio obeys

`log(det K_(m,mq) / det K_tilde_(m,mq)) >= (2beta-1) log q + O_rho(1)`.

Thus growing depth supplies a real source signal: false RH simultaneously creates a Möbius raw near-kernel and a polynomial Blaschke repair of that near-kernel at the exponent of the off-critical zero.

**Research consequence.** The live problem is no longer to discover source sensitivity at `q=q(R)->infinity`. It is to show that the unnormalized generalized Gram gain survives the diagonal/correlation normalization actually entering the Nyman radial entropy, or to place the same annulus amplification inside a genuinely inter-scale statistic that lower-bounds the radial obstruction. A growing determinant by itself is not enough if normalization removes exactly the gained volume.

**Boundary.** NB-092 gives a one-way zero-frontier implication and an exact source-sensitive direction. It does not prove that the normalized correlation determinant diverges, that the aggregate radial charge diverges, or that the Nyman distance criterion follows.