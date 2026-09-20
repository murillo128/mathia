# MI-039 — Positive liftability is exactly one-sided sparsity in the switched blind affine class

**Evidence level:** exact synthesis from FD-230--[FD-233](../../findings/FD-233-aggregate-negative-sparsity-exactly-characterizes-switched-preserving-positive-lifts.md). No Mertens or RH conclusion is claimed.

The switched divisor geometry has a genuine signed blind space, but signed invisibility is not yet physical realizability. FD-232 proved the necessary one-sided obstruction: if a signed representative has a fixed positive fraction of negative aggregate capacity on late dyadic blocks, every nonnegative lift requires comparable slack and cannot preserve a subquadratic switched response.

FD-233 proves the converse at coefficient level. For any signed linear-envelope profile `b`, a switched-preserving positive lift exists **iff** `sum_{d in B_k} b_d^- / C_k -> 0`. When this holds, no further cancellation theorem for the added slack is needed: the pointwise-minimal choice `s=b^-`, `a=b^+` already has switched response `o(4^j)`, because sparse nonnegative band mass implies `A s(m)=o(m^2)` and every bounded-order switched difference preserves that scale.

The reusable object is therefore the affine correction class modulo the switched-blind space, measured by asymptotic negative-capacity density. Given the source-forced correction `c`, the coefficient-level question is exactly whether some `c+h`, with `h` switched-blind, has vanishing late-band negative fraction. A positive lower bound on the best such fraction is an intrinsic one-sided obstruction; one representative with vanishing fraction removes the coefficient-level positivity obstruction automatically.

**Boundary.** This equivalence stops before discrete source realization. Integer occupancy, finite prime-reservoir capacity and exact source-side constraints remain additional gates. FD-233 also does not establish which side of the affine criterion the actual Mertens correction occupies.