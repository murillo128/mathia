# MI-072 — Accumulated history becomes a fidelity resource only under a coupled noise budget

**Evidence level:** exact deterministic minimax synthesis from [AF-489](../../findings/AF-489-global-lp-relative-noise-has-sharp-horizon-sample-accumulation-law.md), refining the pointwise-noise horizon obstruction of MI-071 and AF-488.

For the local one-generator Dirichlet family `F_q(s)=G(s)+a q^{-s}`, write `theta=log q` and sample at `s_k=s_*+kh`, `0<=k<=N`, with terminal horizon `H=s_N`. If the relative perturbations satisfy one fixed global budget `||xi||_p<=epsilon`, then the sharp deterministic minimax radius is

`R_(N,p)=Theta(epsilon/||s||_p)`.

On a fixed-step expanding lattice this gives `Theta(H^(-1-1/p))` for every finite `p`, while `p=infinity` gives the AF-488 law `Theta(H^-1)`. The mechanism is exact duality after logarithmic linearization: the parameter sensitivity is the `ell_p` norm of the whole abscissa vector, not just its largest coordinate.

The accumulation gain is therefore not produced by history alone. It appears only because a growing set of observations must share a **non-growing coupled perturbation budget**. If the global allowance instead scales as `epsilon N^(1/p)`, corresponding to a constant per-sample average allowance, the gain disappears and the rate returns to `Theta(H^-1)`. The same happens when the number of retained samples stays bounded while their locations move to scale `H`.

This sharpens the fidelity-resource hierarchy. Sample cardinality is useful only after the admissible error geometry couples those samples strongly enough that additional observations increase the effective sensitivity norm faster than the adversary's budget. Under coherent pointwise noise the terminal horizon remains the resource; under a fixed finite-`p` global budget, horizon and sample accumulation jointly determine the inverse modulus.

**Boundary.** AF-489 is local to one known-amplitude moving generator with real multiplicative noise, fixed positive sample spacing, fixed total `ell_p` budget and a compact parameter neighborhood. It is not a growing-depth Dirichlet inversion theorem, does not cover arbitrary complex noise without a branch-controlled formulation, and does not establish rational-prime provenance. Stochastic or correlated noise laws may have different accumulation exponents.