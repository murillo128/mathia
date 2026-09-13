# MI-012 — Depth-two bad-host sparsity can be proved on the full deformed quadratic host sequence

**Evidence level:** the frontier conversion is exact through [RE-095](../../findings/RE-095-source-conditioned-sampled-gap-sparsity-lowers-the-depth-two-moment-frontier.md). [RE-096](../../findings/RE-096-depth-two-bad-hosts-reduce-to-a-phase-stable-deformed-quadratic-sequence.md) proves that the prime-host bad set embeds in an all-integer deformed-quadratic bad set and gives the exact leading deformation/phase geometry. The required scarcity theorem is still open.

After the higher-depth reductions, the residual mixed first/depth-two cells are indexed by ordinary primes `q` and sampled at

`x_q = eta_1^(-1)(eta_2(q))`.

RE-095 shows that if the bad prime-host count at one-sided interval length `2X^vartheta` is `X^(kappa(vartheta)+o(1))`, then the false-RH frontier becomes

`Theta > max(1/2+vartheta, 123/200 + kappa(vartheta)/2)`.

Any fixed saving below the trivial `kappa=1/2` is useful when `vartheta<73/200`.

RE-096 removes an unnecessary restriction from the analytic theorem. The map extends canonically to every large integer host, and the prime-host bad set is a subset of the integer bad set for the sequence `x(n)`. Therefore it is sufficient to prove

`#Z_vartheta(X) <= X^(1/2-delta+o(1))`

for some `vartheta<73/200` and `delta>0`, where `Z_vartheta(X)` counts **all integers** `n~X^(1/2)` whose adjacent interval at `x(n)` is prime-free. The CA selector still uses prime hosts, but the upper-bound theorem need not.

The sample is not physically close to a fixed quadratic lattice at the required interval scale. RE-096 gives

`x(t)=t^2/2 * (1 + (log 2)/(2 log t) + O(1/(log t)^2))`,

so `x(t)-t^2/2 ~ (log 2)t^2/(4 log t)`, much larger than `X^vartheta` for every fixed `vartheta<1`. Pointwise transfer from intervals beginning at `n^2/2` is therefore invalid.

Yet the oscillatory geometry is stable:

`d/dt log x(t) = 2/t + O(1/(t(log t)^2))`

and

`d^2/dt^2 log x(t) = -2/t^2 + O(1/(t^2(log t)^2))`.

Thus zero-sum phases have the same first/second derivative scales as a quadratic sequence up to logarithmic errors. The nearest fixed-power prior art still works only at a longer interval exponent than the Robin window, but its analytic phase architecture is now a meaningful comparison class.

**Research consequence.** The missing theorem is no longer inherently prime-indexed. Adapt sparse-sequence/explicit-formula machinery to the exact smooth deformed quadratic sequence `x(n)` and prove a power saving in bad integer hosts. Physical closeness to squares is false; phase-derivative closeness is the resource that survives.

**Boundary.** RE-096 does not provide the scarcity bound, and the fixed-power literature does not transfer automatically. The deformation must be carried through every zero-sum, amplitude and uniformity range.
