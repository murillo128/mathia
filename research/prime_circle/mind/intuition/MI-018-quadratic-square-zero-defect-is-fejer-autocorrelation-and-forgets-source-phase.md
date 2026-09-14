# MI-018 — Quadratic square-zero defect is Fejer autocorrelation and forgets source phase

**Evidence level:** exact finite identity plus prior-art boundary from [PC-299](../../findings/PC-299-square-zero-cross-gram-defect-is-fejer-source-autocorrelation.md)

For the low boundary-log block `A=X D Z^*`, the first nonzero two-step loop is `A^2=X D C D Z^*` with cross-Gram matrix `C=Z^*X`. PC-299 computes its source-averaged quadratic content exactly. In the opposite-mode channel,

`E |C_(-m,m)|^2 = 1/N + (2/N^2) sum_(t=1)^(N-1) (N-t)|muhat(mt)|^2`.

The complete symmetric Frobenius energy has the same structure: a universal `d^2/N` baseline plus a positive Fejer-weighted source power spectrum. For the prime source the excess is precisely a weighted mean square of classical additive exponential sums over primes.

This is important because the statistic is not attached after the operator analysis: `D C D` is the actual first loop-closure defect below the square-zero approximation. But a positive quadratic average observes only autocorrelation/Fourier power. It discards source Fourier phase, and matched laws with the same relevant power spectrum are invisible to it.

Therefore moving below the `r_q` square-zero scale is not enough by itself. A route based only on `||C||_F`, `||DCD||_F`, opposite-mode squared overlaps, or equivalent positive quadratic energies lands in the classical prime exponential-sum/pair-correlation interface. A genuinely new one-profile escape must retain information outside that quotient—cross-Gram phase, higher joint correlations, source-coupled left/right structure, noncommuting profiles, or cross-level relations.

The `1/N` baseline is not an operator-norm lower bound for distance to the square-zero class, and PC-299 does not identify its finite cyclic prime statistic with Montgomery pair correlation. Tails, re-orthogonalization, conditioning on distinct prime pairs, and mean-square versus in-probability/operator scales remain separate.
