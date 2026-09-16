# MI-029 — Irrational one-parameter radialization removes collisions by decoding the full source tensor

**Evidence level:** proved for the PC-316 product field by PC-317--PC-318, with the irrational case established in [PC-318](../../findings/PC-318-irrational-radial-rays-are-tensor-decoders-and-barnes-zeta-packets.md).

The two-index PC-316 field along a positive radial ray has coefficients

`R(t)=sum_(k,l>=1) a(k)b(l) exp(-(lambda k+mu l)t)`,

with `a,b` periodic. The information content of this one-dimensional trace is controlled exactly by arithmetic collisions among the frequencies `lambda i+mu j`.

If `lambda/mu` is rational, PC-317 shows that collisions fold the two indices into an eventually quasipolynomial one-index sequence; the Mellin image is a finite Hurwitz-zeta packet. The scalarization is compressive, but classically so.

If `lambda/mu` is irrational, the opposite happens. After stripping the two known geometric denominators, the trace is a finite exponential polynomial with `qr` pairwise distinct frequencies. A finite Vandermonde system recovers every residue coefficient `a_i b_j`. For the canonical normalized Prime-Circle sources, row and column sums fix the factorization and recover both cyclic source packets themselves. The Mellin image is correspondingly a finite Barnes double-zeta packet.

Thus **irrationality is not an intermediate source-sensitive compression here; it is collision removal all the way to decoding**. Exact injectivity is itself a no-go for the intended nonreconstructive scalar invariant. Its finite-window conditioning can still deteriorate at growing levels through Diophantine near-collisions, but that does not restore a useful quotient.

PC-317 and PC-318 exhaust positive one-parameter radial rays of this construction. A surviving route must retain genuinely multivariable geometry, introduce a source-forced coupling not equivalent to the additive radial frequency map, or prove an independent zero-selection theorem for the exact classical multiple-zeta packet. Merely choosing an irrational slope does not create new arithmetic content.
