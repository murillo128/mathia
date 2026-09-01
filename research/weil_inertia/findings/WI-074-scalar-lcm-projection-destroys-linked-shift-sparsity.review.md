---
type: adversarial-review
target: research/weil_inertia/findings/WI-074-scalar-lcm-projection-destroys-linked-shift-sparsity.md
---

# Adversarial review

## Adversary

The positive-density step in §2 is not established for the **actual weighted Yang support**.  The pinned `scripts/t2_swaps.py` does not let `k` contribute merely because the algebraic parametrization `(h_1,h_2)=(rk,qk)` exists: in the `S1` swap loop it first requires `m` and `m'=m-rk` to have nonzero von-Mangoldt weight, and the inner contribution additionally requires `n` and `n'=n-qk` to have nonzero weight.  Thus, for the witness `(b_1,b_2)=(2,4)`, the identity `L=2|k|` only shows that the **ambient candidate** moduli form the even progression; it does not show that every even `L` (or a positive-density set of them) occurs with nonzero source weight.

This distinction is material because a sparse-moduli argument could in principle discard zero-weight moduli and run on the effective set of `k` for which the locked prime-power covariance is nonzero.  The current finding therefore overstates the exact conclusion when it says that a fixed source slope has scalar `L`-support of density `1/2` and uses that to close the weak scalar-support escape hatch.  The same issue affects the equal-leg `L=|k|` sentence.

The objection would be resolved by either (i) a proof that the distinct `k` carrying nonzero weighted contributions on one of these low slopes have positive density in the relevant range, with the source-window constraints included, or (ii) a narrower argument showing that the large-sieve interface being ruled out necessarily sees the full ambient candidate progression rather than the support of nonzero covariance weights.  The algebraic parametrization alone does not supply either statement.