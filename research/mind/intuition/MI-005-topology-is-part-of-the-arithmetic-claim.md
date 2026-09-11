# MI-005 — Finite degree bounds local depth, not the number of prime locations

**Evidence level:** supported; exact identification statements are relative to the declared source class and observation map.

For a normalized local Euler factor `E(z)=product_(j<=r)(1-alpha_j z)^-1`, `r<=d`, the first `d` power sums `c_k=sum_j alpha_j^k` determine the factor by Newton identities. The bound is sharp: `(1-(Az)^d)^-1` and `(1-(Bz)^d)^-1` agree through `d-1` but differ at `d` when `A^d!=B^d`. Consequently a fixed degree bound requires only `d` coefficients per prime, but still data at every prime ([AF-274](../../arithmetic_fidelity/findings/AF-274-fixed-local-euler-degree-gives-sharp-finite-depth-fidelity.md)).

Finite global analytic samples do not evade that breadth in the same category. With `M=sum_j(r_j+1)` finite real right-half-plane jet conditions and any cutoff `P_0`, [AF-276](../../arithmetic_fidelity/findings/AF-276-finite-right-half-plane-jets-leave-exact-far-prime-euler-fibers.md) selects `M+1` primes beyond `P_0` so that

\[
Z_a(s)=\zeta(s)\prod_\ell\frac{1-q_\ell^{-s}}{1-a_\ell q_\ell^{-s}}
\]

has a nontrivial one-dimensional local fiber preserving every sampled jet. The modified local factors remain degree one. This is nonidentifiability with exact observations, not numerical conditioning and not a construction satisfying every completed-zeta axiom.

A contrasting quantifier occurs in [PF-292](../../prime_flute/findings/PF-292-fixed-physical-high-pass-forces-diverging-local-frequency-floor.md): restricting an increasingly dense set of frequencies from one fixed physical band to a fixed window produces a growing observation space whose orthogonal complement has a diverging Dirichlet frequency floor. A fixed bandwidth there is not a fixed finite test family. Comparing that annihilation result with AF's finite-jet obstruction while ignoring the growing number of tests would reverse the conclusion for the wrong reason.
