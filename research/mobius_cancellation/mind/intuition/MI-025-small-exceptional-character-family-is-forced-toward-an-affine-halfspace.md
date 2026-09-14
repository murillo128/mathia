# MI-025 — Near-negative exceptional characters obey dual odd-girth and occupancy rigidity

**Evidence level:** exact finite Fourier consequence of [MC-289](../../findings/MC-289-odd-moment-character-bias-from-collision-rich-shells.md), [MC-290](../../findings/MC-290-odd-moment-exception-set-near-affine-rigidity.md), and [MC-291](../../findings/MC-291-near-negative-spectrum-dual-odd-girth.md). These are interface theorems for the collision-rich odd shell; they supply no new character-sum estimate or bound for `M(x)`.

Let `eta=N^2/(2^r sum_s n_s^2)` be the effective occupancy and let `A_lambda` be the generated quadratic-character shell sums. When short odd relations are absent, MC-289 gives exact odd moments. MC-290 shows that if analytic input controls all but `J` characters above `-delta`, those moments force the exceptional family toward the affine endpoint: when `epsilon_m=delta^(m-2)(eta^-1-1)` is small and `log J=o(m)`, one exceptional character is `-1` on a `1-o(1)` fraction of weighted shell mass.

MC-291 adds a collective constraint that does not come from another moment estimate. Write the positive-side defect of a negative character as `d_lambda=(1+A_lambda/N)/2` and let `E_tau={lambda ne 0:d_lambda<=tau}`. If distinct `lambda_1,...,lambda_j in E_tau` have odd cardinality and sum to zero, then

`sum_i d_(lambda_i) >= 1`.

Hence `E_tau` has no odd circuit of length `j` with `j tau<1`. The near-negative spectrum itself therefore inherits a dual odd-girth gap. Applying finite-geometric rigidity to its span gives a second dichotomy: either `E_tau` is exponentially sparse in that span, or all near-negative modes are compatible with one common source cell on which they simultaneously take the preferred value `-1`.

Effective occupancy controls how large that compatible family can be. If `R` linearly independent near-negative modes satisfy `R tau<1`, their common preferred-sign cell contains at least `(1-R tau)N` weighted shell mass, and Cauchy--Schwarz gives

`eta <= 2^(-R)/(1-R tau)^2`.

In particular, when `R tau<=1/2`, `R<=log_2(4/eta)`. A collision-rich shell with non-negligible participation ratio therefore cannot support a high-rank family of almost constant-negative generated characters.

The reusable interface is now two-level. A small analytically exceptional family is forced **toward** the affine endpoint by MC-290; MC-291 then constrains the geometry of all modes that get sufficiently close. Future arithmetic input can attack exceptional-family size, one-sided threshold, effective occupancy, conductor, dual rank, or the impossibility of concentrating most source mass in a common preferred-sign cell for the actual Legendre shell.

**Boundary.** These conclusions depend on the exact finite Fourier identities and on `eta` not being too small. They do not exclude the affine endpoint, prove a lower bound on `eta`, control conductor, or supply the required exceptional-character theorem. The common sign cell is a structural alternative, not evidence that the actual arithmetic shell realizes it.