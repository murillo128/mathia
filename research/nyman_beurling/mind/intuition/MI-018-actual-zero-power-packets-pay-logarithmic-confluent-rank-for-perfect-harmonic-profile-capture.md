# MI-018 — Actual zero-power packets pay logarithmic confluent rank for perfect harmonic-profile capture

**Evidence level:** exact consequence of [NB-123](../../findings/NB-123-perfect-target-capture-by-a-finite-zero-packet-requires-logarithmic-confluent-rank.md), using the target equality characterization of NB-117 and the elementary annihilating recurrence of finite confluent exponential-polynomial sequences. No stable near-perfect capture bound, zero-spacing estimate, RH consequence or novelty claim for Prony/annihilating-filter theory is made.

The matched controls of NB-119--NB-122 show that increasingly rich Nyman orthogonality and even the entire nested cutoff prefix do not exclude perfect visible target capture. NB-123 identifies the first exact separator coming from the **actual zero-power representation itself**.

For a finite packet `F` of actual nontrivial zeta zeros, let `d(F)` be its total confluent multiplicity. Sampling its primitive on a geometric grid `n=q^k` gives a finite exponential-polynomial sequence

`u_k = sum_j lambda_j^k p_j(k)`, `lambda_j=q^(-conj(rho_j))`,

with total recurrence order at most `d(F)`. Its block increments obey the same annihilating polynomial `A_(F,q)(E)`.

Perfect target capture at cutoff `R` forces, by the NB-117 equality case, the primitive to equal `C+D/n` on `1<=n<=R` with `D!=0`. Hence the first `K=floor(log_q R)` geometric block increments are the pure mode

`v_k = D(1-q^-1)q^-k`.

But every actual nontrivial zero has `Re rho<1`, so `q^-1` is not a characteristic root of the zero packet: `A_(F,q)(q^-1)!=0`. If `K>d(F)`, the first recurrence equation applied to the forced target blocks gives a contradiction. Therefore

`d(F) >= floor(log_q R)`,

and in particular `d(F)>=floor(log_2 R)`.

This sharply separates **source equations** from **source representation**. The inverse-section controls can satisfy all audited nested Nyman equations while remaining outside the finite zero-power class. Once the actual transformation law is imposed, bounded-rank and sublogarithmic-rank packets cannot realize the perfect target extremizer.

The next quantity is not another nested projection. It is the conditioning of the approximate annihilator. Near-perfect capture would make the observed geometric increments only approximately equal to the missing `q^-1` mode, and converting that error into a target-angle gap requires control of `|A_(F,q)(q^-1)|` and of coefficient amplification when the sampled zero nodes cluster or the confluent rank grows.

**Boundary.** The theorem excludes exact perfect capture only below logarithmic packet rank. It does not bound capture uniformly away from one, does not control high-rank packets, and does not show that actual zero configurations have a well-conditioned annihilator. The durable new resource is the finite recurrence forced by zero-power structure, not zero count by itself.