# VIS-369 — source-free degenerate positive metrics can prescribe the active singular spectrum

## Claim

Let

`A_W = B W^(1/2)`

be a Wang polynomial-coefficient map measured in an already priced positive coefficient metric `W>0`, and suppose `A_W` has rank `r` with singular-value decomposition

`A_W = U Sigma V^*`,

where the active singular values are

`sigma_1,...,sigma_r > 0`.

Choose any desired positive active singular values

`tau_1,...,tau_r > 0`.

Extend the right-singular vectors to a unitary basis and define

`d_i = tau_i/sigma_i` for `1<=i<=r`,

with any fixed positive `d_i` on the nullspace, for example `d_i=1`. Put

`D=diag(d_1,...,d_n)`,

`C = V D^2 V^*`,

and

`H = W^(1/2) C W^(1/2)`.

Then `H` is positive definite. With

`L = W^(1/2) V D V^*`,

one has `H=L L^*` and the Wang map in the new positive Hilbert coefficient metric is

`A_H = B L = U Sigma D V^*`.

Therefore the nonzero singular values of `A_H` are exactly the multiset

`{tau_1,...,tau_r}`.

So if a positive coefficient metric is allowed to degenerate freely and to align with the source-free right-singular geometry of the already priced Wang map, **its active singular spectrum can be prescribed arbitrarily**. In particular, one may manufacture an arbitrarily small singular direction, flatten the active spectrum, or impose any desired asymptotic singular scale without using arithmetic source information.

Positive-definite `H` preserves rank, so an exact new zero singular value is not created by this construction; exact rank loss requires a singular positive-semidefinite limit. Arbitrarily strong collapse is nevertheless available through positive-definite metrics by taking some `tau_i/sigma_i -> 0`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL SVD/RIGHT-PRECONDITIONING + DECISIVE NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This proves no stronger estimate for the normalized Chebyshev-theta remainder, the prime number theorem remainder, zeta zeros, or RH.

## 1. Representation audit: the resource is the full relative metric

The native object here is not a scalar condition number. It is the positive relative metric operator

`C = W^(-1/2) H W^(-1/2)`

acting on the full coefficient space, including both its eigenvalues and its orientation relative to the right-singular directions of `A_W`.

`VIS-368` used only the order bounds

`lambda_min(C) I <= C <= lambda_max(C) I`

to compare singular values. That scalar envelope was sufficient to prove that uniformly bounded positive correlations cannot change asymptotic singular scales, but it deliberately left open what happens when the relative metric degenerates.

The present argument does not replace the operator by `lambda_min`, `lambda_max`, a determinant, or a condition number. It keeps the complete eigenbasis of `C` and shows that alignment with the full right-singular basis is exactly enough to engineer the entire active singular spectrum. This is therefore a representation-level negative control, not a scalar proxy for one.

## 2. Exact SVD engineering

Write the full SVD as

`A_W = U Sigma V^*`.

Let `D` be any positive diagonal matrix in that right-singular basis. Since

`C^(1/2)=V D V^*`,

choosing the relative coefficient metric

`C=V D^2 V^*`

gives

`A_H = A_W C^(1/2)`
`    = U Sigma V^* V D V^*`
`    = U Sigma D V^*`.

The singular values of `U Sigma D V^*` are the diagonal entries of `Sigma D` on the active sector, up to their irrelevant ordering. Hence

`s_i(A_H)` as a multiset `= {sigma_i d_i : 1<=i<=r}`.

Taking `d_i=tau_i/sigma_i` proves the claim.

Nothing in this construction uses `G`, `theta`, primes, zeta zeros, or another arithmetic source statistic. Once the source-free polynomial coefficient map `A_W` is known, its own singular vectors provide all the geometry needed to manufacture the target spectrum.

## 3. Metric degeneration pays exactly for the manufactured gain

The relative metric has eigenvalues

`lambda_i(C)=d_i^2`.

Thus a factor `d_i` applied to the `i`-th active singular channel costs exactly a factor `d_i^2` in the corresponding relative metric eigenvalue. The square-root comparison in `VIS-368` is therefore channelwise sharp when the metric is aligned with the right-singular basis.

For example, asking for one active singular value to shrink by a factor `epsilon` can be achieved by putting relative metric eigenvalue `epsilon^2` on that right-singular direction. Asking to whiten the active spectrum to `tau_i=1` uses active relative eigenvalues

`lambda_i(C)=sigma_i^(-2)`.

The apparent improvement in operator conditioning has then simply been transferred into the coefficient metric. The physical problem has not acquired a free cancellation mechanism; it has changed which coefficient directions are declared cheap or expensive by exactly the amount required to obtain the desired spectrum.

This gives a sharper accounting rule than merely observing that `lambda_min(C)` tends to zero or `lambda_max(C)` diverges. **Degeneration is a new resource only after its operator-valued geometry is justified independently of the singular improvement it produces.** If the metric is selected from the SVD of the target map, the improvement is engineered preconditioning by construction.

## 4. Wang consequence

The accepted Wang clue asks whether a degenerating positive metric can escape the compact positive-Hilbert closures of `VIS-366`--`VIS-368`. The answer is now split into two cases.

An arbitrary source-independent positive metric chosen after inspecting the Wang coefficient map is not a meaningful escape. It can prescribe the active singular spectrum at will, so small singular values, spectral flattening, improved condition number, or a new asymptotic singular exponent are not arithmetic evidence by themselves.

A positive degenerating metric remains potentially meaningful only when its geometry is constrained independently of that target spectral engineering. Examples include a metric forced by the physical destination norm, a coefficient topology fixed before the singular optimization, or a source-dependent metric whose selection rule is itself derived from arithmetic information and whose full cost is propagated through the destination. In the source-dependent case, any apparent gain must be reformulated as a source estimate rather than credited to passive preconditioning.

This result does not address genuinely indefinite/non-Hilbert coefficient spaces, nonlinear source coupling, noncompact/global phase geometry, or infinite-dimensional limits whose physical topology is not an arbitrary positive right preconditioner.

## Prior-art audit

The mathematical ingredients are classical singular-value decomposition and positive right preconditioning. The same standard matrix-analysis background already anchored in `VIS-368` applies here: Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd ed., Cambridge University Press (2013), and Horn and Johnson, *Topics in Matrix Analysis*, Cambridge University Press (1991).

No novelty is claimed for SVD, positive-definite metric changes, whitening, right preconditioning, or spectrum shaping. The exact construction above is an elementary SVD consequence. The Mathia-specific content is only the negative-control consequence for the current Wang frontier: unconstrained positive metric degeneration is too expressive to count as arithmetic structure because it can manufacture the spectral phenomenon being measured.

## Dependencies

- `VIS-354`: Wang tail coefficients form a source-free truncated Vandermonde moment map.
- `VIS-361`: positive diagonal coefficient weights are priced by a weighted moment Gram.
- `VIS-366`: fixed-depth positive compact polynomial sampling is priced by Vandermonde partition sums.
- `VIS-367`: growing compact depth has a universal Chebyshev/capacity conditioning baseline.
- `VIS-368`: uniformly comparable positive Hilbert metrics are bounded preconditioners.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue narrowed by this result.

## Research consequence

The phrase “degenerating positive metric” is not by itself a live Wang mechanism. **If the metric may be chosen freely in the source-free right-singular basis, any desired positive active singular spectrum can be imposed exactly.** Such degeneration is therefore a representation choice, not evidence of arithmetic localization.

Future positive-metric proposals must expose what independently fixes the relative metric operator and must charge its full eigenvalue-and-orientation geometry through the physical coefficient and destination norms. The remaining frontier is source-justified or physically mandated metric degeneration, genuinely indefinite/non-Hilbert topology, noncompact/global geometry, nonlinear source coupling, or another mechanism not reducible to engineered positive right preconditioning.