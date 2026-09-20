# MI-042 — Point-sampling signed capacity has a sharp density-one threshold

**Evidence level:** exact source-specific synthesis from [FD-240](../../findings/FD-240-every-subfull-point-sampling-density-retains-a-macroscopic-signed-nullspace.md) and [FD-241](../../findings/FD-241-density-one-point-sampling-is-the-sharp-macroscopic-signed-coercivity-threshold.md), extending FD-238--FD-239. This concerns unrestricted signed profiles with `|b_n|=O(n)` and exact sampled response zeros; it does not transfer to physical nonnegative/source-coherent corrections without a separate theorem.

Let `S` be the prescribed point-sampling set for the divisor response, `E=N\S`, and let

`delta_k = |E cap B_k| / |B_k|`

be the omitted fraction on dyadic octave `B_k`. FD-240 gives the lower side: whenever `limsup delta_k>0`, one can construct integer signed coefficients with `|b_n|<=n`, exact response zero on every point of `S` (and the dyadic endpoints), globally controlled response, and a positive fraction of linear coefficient capacity on infinitely many octaves.

FD-241 gives the opposite endpoint. If `delta_k->0`, every exact-kernel profile satisfying `|b_n|<=Cn` is capacity-negligible:

`sum_(n in B_k)|b_n| / sum_(n in B_k)n -> 0`.

With `R(N)=|E cap [1,N]|` and dyadic `N`, the normalized octave mass is bounded by an absolute constant times

`C sqrt((R(N)+1)/N)`.

The decisive localization appears after Möbius inversion. Writing `g=mu*b` makes the response the partial sum of `g`. If two consecutive locations are sampled zeros, their difference forces `g` to vanish there, so `supp(g)` is contained in `E union (E+1)` apart from the initial endpoint. A bounded mean square for `sigma_-1` then prevents a zero-density increment support from rebuilding macroscopic coefficient capacity through divisor summation.

Thus **density one is the sharp threshold for macroscopic signed capacity coercivity of exact point samples**. This is not an injectivity theorem: a proper density-one set can retain nonzero exact-kernel directions, but those directions cannot carry a fixed fraction of the natural octave capacity under the linear envelope.

**Boundary.** Exact sampled zeros and the coefficient envelope are load-bearing. Approximate/noisy samples destroy the literal support restriction on `g`, and FD-241 does not classify finer kernel norms, nonlinear/non-pointwise measurements, or the physical positive/source-coherent class. Those require a quantitative stability or transversality argument rather than another density interpolation.