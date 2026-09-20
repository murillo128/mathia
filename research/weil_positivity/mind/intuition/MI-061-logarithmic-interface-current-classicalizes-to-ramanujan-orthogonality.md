# MI-061 — Logarithmic interface current classicalizes to Ramanujan orthogonality

**Evidence level:** exact source-specific synthesis from [WP-389](../../findings/WP-389-logarithmic-interface-current-classicalizes-to-ramanujan-orthogonality.md), following the boundary/domain obstructions of WP-384--WP-388. The Ramanujan identities are classical; the line-specific conclusion is that the canonical first-order interface completion of the WP-384 boundary carrier is not a Weil finite-place selector.

For the pointed boundary shell profile `h_m`, the jump across integer `k` satisfies the exact identity

`j_m(k):=k Delta_k h_m = c_m(k)/sqrt(m)`,

where `c_m(k)` is the classical Ramanujan sum. The logarithmic factor `k` is the scale-covariant normalization associated with `x d/dx`; it removes the forced `1/k` size of the raw harmonic-floor jump.

Classical Ramanujan orthogonality then gives the complete shell Gram:

`lim_(X->infty) (1/X) sum_(k<=X) j_m(k) conjugate(j_n(k)) = delta_(m,n) phi(m)/m`.

The nearest-neighbor positive interface energy has the same intensive limit:

`lim_(X->infty) (1/log X) sum_(k<=X) k |Delta_k f|^2 = sum_m |alpha_m|^2 phi(m)/m`

for every finite shell combination `f=sum_m alpha_m h_m`.

Thus the interface route genuinely recovers infinitely many boundary degrees of freedom that regular strongly local diffusion cannot read, but **their canonical positive geometry is the classical Ramanujan Hilbert basis**. Every mixed-prime shell has positive norm. For `m=p^a`, the weight `phi(m)/m=1-1/p` forgets the exponent `a`, and for squarefree mixed `pq` it remains strictly positive. The prime-power selector and Mangoldt weight are therefore absent.

Once the shell currents are orthogonal, inserting a diagonal operator that vanishes on mixed shells can trivially manufacture the desired support, but that is an additional arithmetic spectral multiplier. The interface geometry itself does not force it. A surviving positive boundary mechanism must instead supply a source-forced non-diagonal interaction, retain finite-prelimit structure discarded by the limiting carrier, or postpone finite-place selection until a coupled finite--archimedean sign theorem.

**Boundary.** WP-389 closes the ordinary mean-square/logarithmic nearest-neighbor geometry of the first-order integer-interface current. It does not classify arbitrary non-Markov off-diagonal kernels, finite-`q` prelimit terms, or indefinite finite--archimedean couplings. Ramanujan orthogonality is a classicalization result, not an RH criterion or a proof that every interface-based route fails.