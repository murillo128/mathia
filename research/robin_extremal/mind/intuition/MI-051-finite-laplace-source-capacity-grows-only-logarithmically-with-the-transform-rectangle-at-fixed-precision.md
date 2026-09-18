# MI-051 — Finite-Laplace source capacity is logarithmic, but the whole real Euler ray can remain selector-scale near-null

**Evidence level:** exact conditioning synthesis from [RE-190](../../findings/RE-190-shrinking-euler-sampling-windows-collapse-to-reciprocal-mass-rank-one.md)--[RE-196](../../findings/RE-196-fixed-jet-matching-collapses-the-entire-real-euler-ray-by-log-powers.md). Generic finite-Laplace compactness, low-rank approximation, Abel summation and Taylor remainder bounds are prior-art territory; the Mathia content is the precision-aware compression law together with the matched-control separation between exact continuum identification and selector-scale stable discrimination.

RE-192 identified the mixed scale

`R=U log(Q_+/Q_-)`

for a source packet supported on `[Q_-,Q_+]` and observed on `1<=s<=1+U`. RE-193 then shows that a global Taylor view is far from optimal. After the exact prime-power reduction, the first-harmonic channel is the finite-Laplace kernel `e^(-ux)`, and a dyadic source decomposition gives, for tolerance `epsilon` above the explicit prime-power floor,

`rank = O((1+log(1+R))(1+log(1/epsilon)))`.

The geometry explains the logarithm. A source coordinate at distance `x` matters only in the spectral boundary layer `u=O(1/x)` before `e^(-ux)` becomes exponentially small. Each dyadic source scale therefore consumes only `O(log(1/epsilon))` separated directions, and the number of relevant scales is only `O(log(1+R))`. Exact continuum identification by analyticity can coexist with very small finite-precision capacity.

RE-194 converts Robin's selector-scale absolute debt `d_p~1/(sqrt(p)log p)` into the relative tolerance

`epsilon_Rob~min(1,d_p/V)`,  with  `V=sum_q |c_q|/q`,

which yields the worst-case upper bound

`O((1+log(1+R))(1+log_+(V/d_p)))`.

This is a valid norm-based capacity estimate, but RE-195 shows that its variation factor cannot be read backwards as source-visible complexity. For every fixed jet depth and any prescribed finite `Lambda_p`, an ordinary-prime `{0,1,2}` matched control can carry a remote packet with

`V >= Lambda_p`

while greedy Chebyshev sign balancing keeps the signed primitive logarithmic. Abel summation then makes the packet uniformly `O_U(p^-2)` in every fixed Euler window and `O_j((log p)^j/p^2)=o(d_p)` in every fixed boundary jet. The exact matching repair, KV fidelity and order-one transient Robin excursion survive on a disjoint prime channel.

RE-196 shows that the fixed-window qualifier is not the real escape. The structured RE-182 repair has bounded centered logarithmic transport moments at selector scale. If the first `K` Euler boundary jets are matched exactly and `s=1+u`, factoring the common selector decay `p^-u` leaves a normalized profile whose first `K` derivatives vanish at `u=0`. The first surviving Taylor remainder is `O_K(d_p u^(K+1))`, and multiplication by `p^-u` gives the global optimization

`sup_(u>=0) u^(K+1)p^-u = O_K((log p)^(-(K+1)))`.

The Chebyshev-balanced remote padding is even stronger: its exact Euler discrepancy is `O(p^-2)` uniformly on the **entire** real half-line `s>=1`, regardless of how large its reciprocal variation becomes. Combining the two pieces yields

`sup_(s>=1)|D_Q(s)| <<_K d_p/(log p)^(K+1) + p^-2`.

For every fixed `A>0`, choosing a fixed `K>A` therefore gives a genuine matched control with

`sup_(s>=1)|D_Q(s)| = o(d_p/(log p)^A)`

while the normalized Robin transient remains order one, every jet through `K` matches exactly, KV fidelity holds and reciprocal variation can be arbitrarily large.

So the channel sees a quotient much smaller than unsigned `ell^1` source mass **even when the observation family is the complete positive real Euler ray**. Exact injectivity is not contradicted: RE-174 still says exact data on an unbounded temperature set identify the infinite prime source. RE-196 instead shows that the inverse modulus can collapse below every fixed log-power fraction of the selector debt on the present matched-control class. Infinite spectral span and exact analytic uniqueness do not by themselves imply Robin-scale stable information.

The reusable capacity test must therefore be two-sided. `R` and requested relative precision govern upper bounds on how many scalar directions can be resolved, but any proposed lower bound needs a source complexity coercive **after quotienting balanced near-kernel directions** and a precision scale strong enough to survive the full-ray near-null family. Raw support width, dense sampling, exact analytic identifiability, infinite real temperature span and unsigned reciprocal variation are each insufficient by themselves.

**Boundary.** RE-196 is a fixed-depth statement: `K` is fixed before `p` tends to infinity, and no uniform control is claimed when jet depth grows with `p`. It does not contradict exact Dirichlet/Laplace uniqueness, settle the intermediate growing-depth region, cover complex temperatures, or rule out joint/nonlocal observables. A useful continuation must either identify a signed/quotiented source norm with a selector-scale inverse modulus, exploit genuinely growing-depth precision beyond the fixed-log-power near-nullity, or leave the one-sided scalar Euler channel for an invariant with independent Robin leverage.
