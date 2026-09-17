# MI-051 — Finite-Laplace source capacity is logarithmic, but unsigned reciprocal variation is not coercive complexity

**Evidence level:** exact conditioning synthesis from [RE-190](../../findings/RE-190-shrinking-euler-sampling-windows-collapse-to-reciprocal-mass-rank-one.md)--[RE-195](../../findings/RE-195-chebyshev-balanced-padding-makes-reciprocal-variation-noncoercive.md). Generic finite-Laplace compactness, low-rank approximation and Abel summation are prior-art territory; the Mathia content is the precision-aware compression law together with the matched-control separation between unsigned reciprocal variation and actual scalar Euler response.

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

So the channel sees a quotient much smaller than unsigned `ell^1` source mass. **Large reciprocal variation can lie almost entirely in balanced directions that the finite-Laplace/Euler map suppresses.** The `log(V/d_p)` term says how much worst-case accuracy a source of norm `V` might require; it does not say that increasing `V` produces independent robust Euler coordinates or that a source-fidelity theorem controlling signed Chebyshev mass controls `V`.

The reusable capacity test must therefore be two-sided. `R` and the requested relative precision govern an upper bound on how many scalar directions can be resolved, but any proposed lower bound needs a source complexity that is coercive **after quotienting balanced near-kernel directions**. Raw support width, dense sampling, exact analytic identifiability and unsigned reciprocal variation are each insufficient by themselves.

**Boundary.** RE-193--RE-195 remain scalar upper/noncoercivity results, not matching singular-value asymptotics or a Robin criterion. RE-195 is proved for every fixed Euler-jet depth and fixed spectral width; it does not settle the intermediate growing-depth region or all possible joint/nonlocal observables. A useful continuation must either identify a signed/quotiented source norm that lower-bounds actual Euler response under the matched controls, or leave the one-sided scalar Euler channel for an invariant with independent Robin leverage.
