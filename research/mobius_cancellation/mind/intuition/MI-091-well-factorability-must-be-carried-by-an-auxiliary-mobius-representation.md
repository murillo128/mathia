# MI-091 — Well-factorability must be carried by an auxiliary Möbius representation

**Evidence level:** exact support obstruction from [MC-452](../../findings/MC-452-truncated-mobius-is-not-well-factorable.md), calibrating the retained-variable route of MC-409 and the post-recombination obstruction of MC-451.

Standard well-factorability is not an intrinsic property of a finite Möbius prefix. For a balanced split `Q=Q_1Q_2`, any convolution `lambda=gamma_1*gamma_2` with `supp(gamma_i)<=Q_i` vanishes at primes larger than both support bounds. Raw truncated Möbius instead equals `-1` at every prime in that range. Taking `Q=(p-1)^2` and `Q_1=Q_2=p-1` already gives an exact contradiction at the prime `p`.

The useful factorability in a dispersion or q-vdC argument must therefore be introduced **before** the lossy scalarization step through an auxiliary coefficient system: a designed sieve weight, a signed decomposition, a smoothing, a retained bilinear representation, or another source-frame transformation. It cannot be recovered by simply relabeling `mu(n)1_(n<=Q)` as a standard well-factorable weight.

This makes the signed-transfer step load-bearing. A positive upper-sieve majorant may have excellent factorable variables while no longer controlling the signed Möbius observable needed for `M(x)`. Any auxiliary representation must prove that the cancellation estimate transfers back to the actual Möbius sum with enough sign information preserved; factorability of a neighboring surrogate is not by itself progress on the target.

The same representation-first lesson is consistent with MC-451. There, final fixed-lcm recombination erased the visible divisor Möbius signs. Here, the raw coefficient sequence never possessed the standard all-splits convolution variables in the first place. In both cases, the variables that a dispersion theorem needs must genuinely survive at the stage where the theorem is applied.

The live question is therefore not whether truncated Möbius is well factorable, but whether one can construct an auxiliary factorable or partially factorable representation whose retained variables yield cancellation **and** whose signed transfer back to Möbius is quantitative enough to improve the target sum.

**Boundary.** MC-452 rules out only standard all-splits well-factorability of raw truncated Möbius. It does not exclude one-split, approximate, averaged, smoothed, multi-stage or other weaker factorizations, and it does not weaken the deliberately factorable auxiliary sieve construction of MC-409. No cancellation estimate for `M(x)` follows from the obstruction itself.