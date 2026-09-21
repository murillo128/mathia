# MI-067 — Finite affine moment side information only thins sparse positive fibers at support scale

**Evidence level:** exact metric synthesis from [AF-477](../../findings/AF-477-finite-moment-fibers-retain-hamming-cube-breadth.md).

Let `Psi:X->R^q` have affine image dimension `d`, and let `F_(r,u)(Psi)` be the probability measures supported on at most `r` atoms with fixed moment `int Psi dmu=u`. For every `k` with

`|X| >= k(d+2)` and `r >= k(d+1)`,

AF-477 constructs a value `u_k` for which one positive moment fiber contains an exact Hamming cube:

`||mu_epsilon-mu_eta||_1 = (2/k) d_H(epsilon,eta)`.

The construction is source-level, not tangent-level. Split `k` disjoint blocks of `d+2` atoms by Radon's theorem into mutually singular probability laws `alpha_j,beta_j` with the same `Psi`-moment, then average one choice from each block. All `2^k` choices are genuine positive laws in one fiber, and each uses at most `k(d+1)` atoms.

Consequently a Hilbert-valued map with finite upper TV-Lipschitz modulus cannot remain uniformly well conditioned on all such fibers. At every fixed resolution `0<delta<=2`, some `r`-sparse fiber has Hilbert distortion at least

`sqrt(floor(r/(d+1)))`

whenever enough latent atoms are available. Equivalently, a uniform distortion cap `D` across every nonempty `r`-sparse moment fiber requires the effective affine rank to grow on the support-complexity scale; a fixed finite list of moments cannot supply that protection as `r` grows.

This pins down what a successful source restriction must do. If a prime-derived class is substantially thinner than the full moment fiber, the reason cannot be finite affine side information alone: some additional nonconvex, singular, boundary, provenance, compatibility, or other source restriction must exclude the independent Radon switches, or the retained affine rank itself must scale with support complexity.

**Boundary.** This is a worst-fiber statement for the full positive finite-moment model, not a claim about every moment fiber and not a lower bound for an arbitrary arithmetic subclass. A narrower class may fail to realize the Radon-block cube. That realizability has to be proved inside the actual source class before the metric obstruction transfers.