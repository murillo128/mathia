# MI-012 — Source-conditioned bad-host sparsity converts directly into a depth-two frontier gain

**Evidence level:** the exponent conversion is exact through [RE-095](../../findings/RE-095-source-conditioned-sampled-gap-sparsity-lowers-the-depth-two-moment-frontier.md), conditional on a sampled-host scarcity estimate at the CA depth-two source points. The required source-conditioned prime theorem is not proved, and ambient exceptional-set estimates alone do not supply it.

After the higher-depth reductions, the residual mixed first/depth-two cells are indexed by ordinary primes `q` with analytic sample points

`x_q = eta_1^(-1)(eta_2(q)) ~ q^2/2`.

RE-094 priced an ambient short-interval theorem by the measure of bad starts near scale `X`. RE-095 asks for less but more source-specific information: count only prime hosts `q~X^(1/2)` for which one of the one-sided intervals of length `2X^vartheta` adjacent to `x_q` is prime-free.

If that bad-host set has size

`#B_vartheta(X) <= X^(kappa(vartheta)+o(1))`,

then the residual mixed-cell threshold mass is bounded by the sum of a small-chamber term and a bad-host/prime-gap-moment term. At the exponent level the resulting false-RH frontier is

`Theta > max(1/2+vartheta, 123/200 + kappa(vartheta)/2)`.

The trivial host count `kappa=1/2` reproduces the existing `173/200` barrier exactly. Any genuine polynomial host saving `kappa=1/2-delta` lowers the second term by `delta/2`. Thus **any** fixed power saving in bad prime-indexed hosts, at some `vartheta<73/200`, is quantitatively useful; no full PNT asymptotic at the sample points is required.

The important control is negative. Turning an ambient exceptional-start measure `X^(m(vartheta)+o(1))` into a host count cannot beat the direct RE-094 max law. Either it leaves the trivial square-root host count, or the interval-length term `1/2+vartheta` already dominates. Therefore a useful `kappa<1/2` estimate must exploit information genuinely conditioned on the sparse prime source—`q` prime, the deformed quadratic map `x_q`, or additional CA selector structure—not merely repackage an ambient almost-all theorem.

**Research consequence.** The `173/200` frontier now has an exact source-information price: prove polynomial scarcity of bad prime hosts at the sampled depth-two points. The gain converts linearly, by one half, through Cauchy--Schwarz against the existing prime-gap second moment. This makes the missing theorem much narrower than a new uniform short-interval PNT and separates it from stronger but source-insensitive ambient estimates.

**Boundary.** RE-095 is a conditional conversion theorem. It neither proves the sampled-host scarcity estimate nor shows that the actual CA selector forces it. The `173/200` number remains a frontier of the present information package, not an intrinsic transition of Robin/CA geometry.