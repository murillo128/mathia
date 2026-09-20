# MI-077 — Factor multiplicity remains subpolynomial after fixed-dimensional bounded source summaries

**Evidence level:** exact combinatorial synthesis from [MC-425](../../findings/MC-425-growing-factor-depth-does-not-create-polynomial-mobius-sign-channels.md) and [MC-426](../../findings/MC-426-bounded-additive-factor-summaries-have-subpolynomial-state-volume.md), following the state-count bounds of MC-423--MC-424. These are source-channel obstructions, not cancellation theorems for richer factor data.

A large family of ordered factorizations is not automatically a large family of arithmetic source states. MC-425 gives the coarsest example: for squarefree `n`, retaining each active factor only through `mu(u_j)` leaves fewer than `2^omega(n)=X^(o(1))` sign words across all possible depths.

MC-426 shows that replacing one sign bit by a fixed list of bounded additive prime-local statistics still does not create polynomial source capacity. Give each prime `p|n` an increment `a(p) in Z^m` with `||a(p)||_infty<=B`, for fixed `m,B`, and retain a factor only through

`S(u)=sum_(p|u) a(p)`.

Across every ordered active factorization and every depth up to `omega(n)`, the number of distinct retained words is

`exp(O_(B,m)(omega(n))) = X^(o(1))`.

The reason is conservation rather than a finite alphabet: each additive coordinate has only `O(omega(n))` total mass to distribute among at most `omega(n)` blocks, so weak-composition counting remains exponential only in `omega(n)`. For fixed `B`, achieving even `X^delta` retained states forces `m=Omega_(B,delta)(log log X)`.

Thus **state multiplicity must be counted after the exact source projection, and fixed-dimensional bounded additive enrichment still collapses the all-depth factorization family to subpolynomial volume**. Exact counts such as `omega(u_j)` and fixed vectors of prime-class incidences are already inside this obstruction; merely replacing Möbius parity by several bounded additive coordinates is not a new polynomial channel.

**Boundary.** MC-426 does not rule out growing dimension, unbounded or increasingly precise prime weights, exact identities, residues/characters with growing modulus or conductor, or genuinely non-additive relations between factors. Nor does `X^(o(1))` state volume imply analytic uselessness. A surviving factor lift must identify which hypothesis it escapes and prove that the retained information contributes to cancellation rather than only increasing labels.