# MI-041 — Low positive-density point sampling can still leave divisor response noncoercive

**Evidence level:** exact source-specific synthesis from [FD-238](../../findings/FD-238-dyadic-switched-response-has-a-macroscopic-signed-nullspace.md) and [FD-239](../../findings/FD-239-sublinear-off-dyadic-response-sampling-still-has-a-macroscopic-signed-nullspace.md). This concerns unrestricted signed profiles under the stated coefficient box; no conclusion is transferred to the physical nonnegative/source-coherent class without a transversality argument. The explicit density threshold below is a certified survival range for the construction, not a sharp coercivity boundary.

FD-238 showed that sampling only the dyadic switched response leaves a macroscopic signed kernel. FD-239 makes the obstruction quantitatively density-sensitive rather than merely grid- or sparsity-specific. Let `S` have `s_k` response samples in the octave `B_k=(2^(k-1),2^k]` and set

`eta=limsup_k s_k/|B_k|`.

If `eta<eta_0:=9/pi^2-3/4=0.161890652...`, there are integer coefficients with `|b_n|<=n` whose divisor response vanishes at every sampled point and every dyadic endpoint, remains `O(m)` globally, and retains normalized octave mass at least

`12/pi^2 - 1 - (4/3) eta`

in the liminf. The signed total on an octave is lower order, so both positive and negative parts retain asymptotically half of this macroscopic mass.

The mechanism is exact reset capacity. Writing `b=1*g` turns divisor response into the cumulative sum `Y(m)=sum_(n<=m)g(n)`. Each cell between consecutive requested samples uses one pivot while all nonpivots are saturated at `|g(n)|=phi(n)` with greedy signs. A cell can therefore be reset to zero at its right endpoint. Paying one pivot per sample costs only a linear amount of the available quadratic octave mass, and tracking that cost yields the explicit `eta_0` range.

The decisive quantity is therefore **response density relative to fresh source capacity**, not whether samples are dyadic or off-grid. Even `Theta(2^k)` scalar coordinates per octave need not create signed coercivity when their density is sufficiently small. Full all-integer response remains injective, so a transition must occur somewhere or depend on sample structure, but FD-239 does not locate a sharp threshold above `eta_0`.

This narrows the viable escape. A point-sampling theorem must either operate beyond the certified nullspace range with genuinely coercive density/structure, or exploit a source restriction quantitatively transverse to these signed constructions. Positivity and source coherence remain plausible precisely because the countermodel is signed; they are not consequences of the response data alone.

**Boundary.** The threshold `eta_0` is sufficient for survival of this particular pivot construction, not necessary. FD-239 does not prove positive-density sampling is ever sufficient below full observation, does not preserve arbitrary nonlinear or nonnegative source constraints, and does not convert the constructed profiles into physical corrections. The exact conclusion is only that every prescribed sample pattern with octave density below `9/pi^2-3/4` can be annihilated while retaining macroscopic signed capacity.