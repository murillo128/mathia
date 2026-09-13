# MI-021 — Support-matched high moments cross the single-blind shell threshold

**Evidence level:** the moment threshold, tensor coefficient mass and Krawtchouk identity are exact through [MC-264](../../findings/MC-264-support-matched-high-moment-blind-threshold.md). The required sparse shell high-moment estimate is a candidate inequality, not a theorem. No blind relation, rank defect or bound for `M(X)` is excluded here.

The surviving quadratic blind relation lives on a shell-prime subset `T` of size `t` and is detected by the shell sum

`B_y(T)=sum_(p<=y, p odd prime) prod_(r in T) (p/r)`.

A blind subset has `B_y(T)=k_y`, where `k_y` is the number of lower primes. Low moments cannot see one exceptional subset against the whole fixed-weight family at the first admissible support scale `t~(1/log 2) log log y`. MC-264 identifies exactly where moment amplification becomes strong enough.

After raising `B_y(T)` to the `m`-th power and reducing lower-prime products modulo squares, the coefficient vector has quadratic mass

`D_(m,y) ~ (2m-1)!! k_y^m`

uniformly for `m=O(log log y)`. The double factorial is the correct quadratic-character diagonal: squarefree-kernel equality identifies many ordinary product diagonals, so replacing it by `m!` would underprice the tensor mass.

Suppose one could prove the shell-specific estimate

`S_(2m,y)(t) <= L_y binom(N_y,t) D_(m,y)`

for the `2m`-th moment over all weight-`t` shell subsets. At `m=t`, the natural diagonal still sits above one blind atom by about `2^t/sqrt(pi t)`. At **one extra tensor power**, `m=t+1`, the normalized diagonal cost instead falls to order

`2^(t+1) sqrt(t)/k_y`.

At the first unresolved support size this tends to zero roughly like `y^(-1)` times polylogarithmic factors. Consequently an estimate at `m=t+1` can tolerate a very large analytic loss and still exclude every blind subset of that weight. The obstruction found at second moment is therefore a **low-moment obstruction**, not an intrinsic family-size barrier to all moment methods.

The arithmetic content of the missing estimate is also exact. Expanding the fixed-weight shell average gives a Krawtchouk kernel:

`S_(2m,y)(t) = sum_(u,v) c_m(u)c_m(v) K_t(d_y(u,v);N_y)`,

where `d_y(u,v)` is the Hamming distance between the Legendre-signature vectors of the squarefree kernels `u` and `v` across shell primes. Thus the unresolved object is the **off-diagonal Krawtchouk-weighted distance distribution of the support-matched tensor family**, not generic pairwise balance.

Ordinary tensorization followed by the all-squarefree-moduli quadratic large sieve does not deliver this estimate: at `m=t+1` the coefficient length reaches about `y^(t+1)` and overwhelms the sparse shell-family scale. The new target is genuinely family-specific.

**Research consequence.** The analytic exit is now precise: control the `2(t+1)`-th moment directly on the fixed-weight shell-product family, equivalently control its off-diagonal Krawtchouk signature distribution strongly enough to stay near diagonal scale, or prove that such control is impossible. Asking only for a “stronger large sieve” hides the support-matched structure that makes the threshold favorable.

**Boundary.** MC-264 calibrates what would be sufficient; it does not establish the candidate moment inequality. A theorem at one support order would exclude blindness there, not automatically prove full generation or the RH-scale Möbius bound.