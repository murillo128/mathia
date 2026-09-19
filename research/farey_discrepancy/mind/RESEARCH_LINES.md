# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Separate source-side rigidity from the exact observation and recovery geometry

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-034-cheap-kernel-closure-can-still-have-large-resistance`.

FD-187--FD-194 establish the source and observation gates. Prime-extension energy is a genuine Möbius relation currency, while dyadic signed-Fourier observation has a sharp geometric square-root threshold: below the critical band permanent quotient holes remain, while at and above it cumulative source recovery has an explicit uniformly stable inverse. The transition is therefore one of geometry and injectivity, not a conditioning pathology of the raw coordinate map.

FD-195--FD-201 show why that stable coordinate recovery does not automatically survive quadratic compression. Classical Franel/Sobolev energies price the same geometric witnesses differently from the raw inverse; on reciprocal-prime shells the RH-facing positive diagonal budget is substantially more coercive than the square-root Mertens target. Fixed-mode cross-horizon differences do contain new Möbius interval increments, but independently squaring the shell rows restores the `H^(3/2+o(1))` random-multiplicative tariff.

FD-202 gives the first exact escape from that diagonal benchmark. For shell primes `K/2<p_1<...<p_m<=K`, `K~sqrt(H)`, normalize the centered fixed-mode rows to `S_i` and take adjacent-prime differences before applying a positive quadratic norm. The overlapping long Mertens intervals collapse to disjoint endpoint slabs, and the shell-normalized path energy

`G_(r,H)=K sum_i |S_i-S_(i+1)|^2`

has squarefree-Rademacher mean `~(6/pi^2)(1+r)H`. The gain is produced by a signed cross-mode projection before squaring. Its only algebraic kernel is the constant shell mode.

FD-203 resolves the first anchoring question and separates **kernel removal** from **uniform inverse conditioning**. For any scalar anchor `ell` with `ell(1)=1`, the anchored form

`||S||_ell^2=sum_i |S_i-S_(i+1)|^2+|ell(S)|^2`

has exact endpoint-difference dual norm

`||e_1-e_m||_(ell,*)^2=m-1`.

Hence every scalar anchor leaves some point-evaluation direction with squared dual cost `Omega(m)`. The endpoint anchor is sharp in order: `||e_i||_*^2=m-i+1`. Since `m~K/(2 log K)`, a one-dimensional anchor can close the kernel while the path still has resistance diameter `Theta(K/log K)`.

Crucially, that anchor itself is cheap in the source-faithful random benchmark. Adding the endpoint coordinate preserves an anchored shell expectation `Theta(H)` rather than restoring the old `H^(3/2)` tariff. The obstruction is therefore no longer “the constant mode costs too much.” It is that **a cheap anchor need not propagate cheaply through a sparse observation graph**.

The next discriminating question has two genuinely different branches. One is arithmetic: can the anchored coordinate itself be chosen as the geometric Mertens witness needed downstream, so no path propagation is required? The other is representational: can an exact signed nonlocal or multiscale projection add edges to the prime-shell observation graph, reduce effective-resistance diameter, and still keep the squarefree-random quadratic cost at `H^(1+o(1))`? Any such proposal must use the same physical observation map and must not hide the FD-198--FD-201 shellwide tariff in the anchor or added edges.

FD-203's resistance lower bound is a representation-space statement. Its extremizers are arbitrary shell vectors and are not proved realizable by Möbius or by the random-multiplicative control. A future source-compatibility theorem could therefore beat the unrestricted inverse bound, but it must state exactly which arithmetic constraint removes the high-resistance directions.

## Apply information budgets only after fixing source class, observation family and destination norm

The same Farey representation can be complete, target-rigid or permanently noninjective depending on the source class, observation family and destination norm. The current sequence of results separates quotient coverage, raw inverse conditioning, diagonal quadratic coercivity, cross-horizon source information, covariance-preserving signed projection, kernel dimension and inverse graph resistance.

Sample count and algebraic injectivity are not enough. A proposed improvement must say which source coordinates are acquired, which cross-coordinate relations the source class forces, whether nominally new coordinates survive exact divisor transport, what projection occurs before the norm, what random-multiplicative cost that projection pays, and what dual/effective-resistance price is required to recover the intended witness.

## Keep source coercivity, coordinate inversion and the Franel--Landau destination separate

Stable source recovery above the square-root observation threshold still does not prove the RH-critical discrepancy estimate. Conversely, source-rigidity theorems identify what relation-sensitive information would be sufficient if a representation exposed it at the required scale.

The high-value frontier is now narrower than another Sobolev reweighting or another low-rank anchor. It is a deterministic Möbius-specific compatibility that suppresses the high-resistance shell directions, or a representation-native signed projection whose random benchmark remains critical while its anchored observation graph has substantially smaller resistance. Either route must still connect to the actual Farey/Franel destination rather than stop at a well-conditioned auxiliary shell norm.
