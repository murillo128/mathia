# MI-010 — Growing depth exposes a Möbius near-kernel and a finite-state Blaschke leverage defect

**Evidence level:** exact through [NB-092](../../findings/NB-092-growing-depth-mobius-annulus-mode-forces-polynomial-blaschke-gram-gain.md) for the growing-depth Möbius annulus and off-critical amplification, and through [NB-093](../../findings/NB-093-single-zero-growing-depth-gram-gain-is-rank-one-causal-state-leverage.md) for the exact single-zero rank-one Gram update and normalized-correlation interface. The sign and size of the normalized radial/entropy response remain open.

Every fixed multiplicative-depth band can be source-silent after subtracting its universal raw Gram baseline, but the constants deteriorate with depth. NB-092 shows that this nonuniformity carries actual arithmetic structure. On the growing band `m<=j<mq`, a canonical Möbius coefficient vector synthesizes an exact flat logarithmic annulus. Its raw Rayleigh quotient is controlled by

`Q_q = sum_(r<q) |sum_(d<=r) mu(d)/d|^2`,

and false RH forces `Q_q` to grow at zero-frontier exponent at least `2Theta-1`. The same off-critical zero amplifies that annulus through its Blaschke factor by `q^(2beta-1)`.

NB-093 identifies what this gain actually is for one zero. An elementary half-plane Blaschke factor is a **one-state causal all-pass filter**. At every finite cutoff, removing it changes the visible Gram by exactly one positive rank-one update

`K_R^(rho) = A_R + s_R s_R^*`.

Hence the entire single-zero generalized spectrum consists of one nontrivial eigenvalue `1+tau_R`, with

`tau_R = s_R^* A_R^(-1) s_R`,

and the Möbius annulus forces `tau_R >= q^(2beta-1+o(1))`. The polynomial determinant repair is therefore not a diffuse volume effect: it is one inverse-correlation leverage blow-up of the causal state left by the finite-horizon zero condition.

Diagonal normalization has an exact competing bill. If `nu_j=|s_(j,R)|^2/(A_R)_(jj)`, then

`det R_R^(rho) / det R_tilde_R = (1+tau_R) / prod_j(1+nu_j)`.

So the normalized bridge is now a concrete comparison between **global inverse-correlation leverage** and **coordinatewise state-energy inflation**. Large unnormalized gain alone has no sign implication: a matched diagonal control can make the normalized ratio exactly one even with arbitrarily large `tau_R`.

The finite-divisor extension is correspondingly finite-state: each elementary Blaschke factor adds one causal leakage state, so a finite off-critical divisor produces a finite-rank update. This turns the next theorem into a source-geometry question rather than another determinant estimate.

**Research consequence.** Do not seek a stronger lower bound on `det K/det A`; for one zero that quantity is already exact. Determine how the actual Nyman state vector sits in the raw correlation geometry: whether `log(1+tau_R)` dominates or is dominated by `sum_j log(1+nu_j)` on the growing Möbius band, and how multiple zero states interact after normalization.

**Boundary.** The rank-one identity does not decide the normalized determinant sign, aggregate radial charge, or Nyman distance. It isolates the exact interface that those targets must control.
