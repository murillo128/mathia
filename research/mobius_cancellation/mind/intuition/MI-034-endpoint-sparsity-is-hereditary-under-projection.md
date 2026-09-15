# MI-034 — Endpoint sparsity is hereditary under both target projection and source cuts

**Evidence level:** exact endpoint-projection/source-complexity obstruction from [MC-307](../../findings/MC-307-hereditary-endpoint-projection-polynomial-source-cost.md), dualized and sharpened by [MC-308](../../findings/MC-308-dual-source-cut-endpoint-occupancy.md), using the audited Brun--Titchmarsh mechanism of MC-305

MC-307 shows that the one-defect endpoint law remains exponentially sparse after forgetting selected **target coordinates**. For any `k` retained endpoint functionals, at most the all-minus cell and the `k` one-defect cells survive. If `P_I` is the common radical of minimum lower-prime representatives for those directions, Brun--Titchmarsh forces

`P_I >= y^(1-(2+o(1))(k+1)/2^k)e^(-O(1))`.

So source complexity cannot be supplied only in aggregate by many cheap almost-disjoint coordinates: it must survive restriction to small endpoint subfamilies.

MC-308 identifies the dual invariant when one instead forgets **source primes**. Attach to each source prime `p` its incidence column `a_p in F_2^k`. For a retained source set `J`, quotient the endpoint space by the span of the omitted source columns. If the quotient has dimension `t_J` and the images of `0,e_1,...,e_k` occupy `h_J` distinct states, then the exact endpoint occupies exactly the fraction

`h_J / 2^(t_J)`

of source-sign assignments modulo `P_J=prod_(p in J)p`. Brun--Titchmarsh gives

`P_J >= y^(1-(2+o(1)) h_J/2^(t_J)) e^(-O(1))`.

The useful threshold is therefore not the cardinality of the source cut. It is whether deleting complementary source coordinates leaves a quotient in which the one-defect simplex still occupies less than half the available states. The MC-307 theorem is the special case retaining all source primes.

The reusable principle is now two-sided: **endpoint source complexity must survive the restrictions induced on both sides of the incidence map.** Target-coordinate projections test whether complexity is hereditary across endpoint subfamilies; source cuts test whether that sparsity is already visible through a low-product subset of the underlying prime coordinates. A model that matches only full rank, full radical, energy or full quotient occupancy can still fail either hereditary audit.

For the Möbius line this turns overlap geometry into a concrete object. The next useful theorem should exploit how minimum lower-prime representatives share source columns across many endpoint directions, and determine whether enough low-product source cuts retain a sparse quotient simplex to contradict the actual available radical budget.

**Boundary.** These are necessary conditions for the exact endpoint partition. They do not prove that the actual Legendre system cannot realize the required hereditary profile, nor that any particular family of cuts is sufficient for RH-scale cancellation.