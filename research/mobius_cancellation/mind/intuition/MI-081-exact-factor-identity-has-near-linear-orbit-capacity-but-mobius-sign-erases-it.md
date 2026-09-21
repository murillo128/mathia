# MI-081 — Exact factor identity has near-linear orbit capacity but Möbius sign erases it

**Evidence level:** exact combinatorial synthesis from [MC-430](../../findings/MC-430-exact-factor-identity-capacity-sign-quotient.md), refining the exact-identity escape left by MC-429 and the sign-projection obstruction MC-425/MI-077. Bell-number and primorial asymptotics are classical; the line-specific content is the capacity/semantics split for one squarefree integer's factor partitions.

For squarefree `n=p_1...p_r`, unordered active factorizations of `n` are in exact bijection with set partitions of the `r` prime divisors, so their number is the Bell number `B_r`. Along the primorial sequence `N_r`,

`B_r = N_r^(1-o(1))`.

Thus quotienting factor-slot order does **not** make full exact factor identity subpolynomial. The exact-identity escape from coarse fixed-dimensional summaries is combinatorially real and can retain almost polynomially maximal state volume.

But if each exact factor is subsequently read only through its Möbius sign, the Bell capacity collapses. For a partition into `d` blocks, the unordered sign multiset is determined by `d` and the number `k` of odd-cardinality blocks, with `k congruent r mod 2`. Across all depths there are only `O(r^2)` such symmetric sign states, hence only `X^(o(1))` for squarefree `n<=X`.

The durable distinction is therefore **capacity before projection versus semantics after projection**. Exact factor identity can escape the state-volume barrier only if the analytic mechanism actually uses prime-block incidence or comparably rich relational data before it is destroyed by the source projection. Enumerating many factorizations and then retaining only factorwise `mu(u_j)` does not turn Bell-number breadth into Möbius cancellation information.

**Boundary.** MC-430 does not prove that exact factor identity yields cancellation, and the `O(r^2)` quotient assumes permutation-invariant factorwise sign readout. Intrinsic ordered roles, cross-factor relations, exact identities used nonlocally, or another source projection may retain more information. Their survival through the later analytic architecture must be shown rather than inferred from raw Bell capacity.