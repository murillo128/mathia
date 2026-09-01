# MI-006 — Marginal fidelity is exactly an interaction-support problem

**Evidence level:** supported by exact pushforward, Walsh, and simplicial-kernel classifications

## Core intuition

Knowing every chosen marginal perfectly can still lose the discriminator if the missing information lives only in how those coordinates interact. The correct object is not the list of marginal dimensions but the interaction support retained by the observation scenario. Joint relational lifts restore information precisely when they add the missing interaction coordinates, not merely because they are higher-dimensional.

## Strongest justified principle

AF-031 separates marginal and joint feature data in full generality. Given features `phi_1,...,phi_m`, complete knowledge of each one-dimensional pushforward determines the individual feature laws but can forget their coupling. The joint pushforward under `Phi=(phi_1,...,phi_m)` recovers the whole feature law, and if `Phi` is injective on the source support it recovers the source measure itself. The lost directions are exactly those in the kernel of the marginalization map on joint feature laws.

AF-032 makes the interaction hierarchy explicit on the Boolean cube. All marginals of order at most `k` retain exactly the Walsh coefficients supported on subsets of size at most `k`; every higher-degree interaction lies in the exact kernel. Two probability laws can therefore agree on every proper marginal and differ only in the top parity interaction.

AF-033 generalizes the combinatorics to an arbitrary marginal scenario. Downward-closing the observed coordinate sets gives a simplicial complex `Delta`; the retained Walsh coordinates are exactly its faces, and the missing faces are exactly the linear kernel. A target functional is recoverable exactly when its Walsh support lies in `Delta`. Choosing the smallest collection of marginals sufficient for a given target becomes an exact weighted set-cover problem on the target interaction support.

The lesson is stronger than “use joint statistics.” One should first identify the interaction basis appropriate to the source category, then ask which interactions the proposed observation family actually spans. Complete low-order marginals can be perfectly measured and still be categorically incapable of recovering a high-order target.

## What remains possible

Beyond finite Boolean products, the analogous interaction-support decomposition may be ANOVA/Hoeffding, tensor, cumulant, representation-theoretic, or operator-valued rather than Walsh. A useful extension would identify an exact decomposition in which an admissible family corresponds to a downward-closed or otherwise computable interaction set and derive target-relative minimal lifts there.

## Status / novelty

The probability pushforward facts, Walsh basis, and simplicial closure are classical ingredients; the exact fidelity-lattice and target-relative interpretation are persisted Mathia evidence. This intuition does not assert that every nonlinear source admits a simplicial interaction model.

## Falsification criterion

Find two finite Boolean probability laws agreeing on every marginal indexed by `Delta` but differing on a Walsh coefficient whose support is a face of `Delta`, or recover a target with Walsh support outside `Delta` from only those marginals. A positive generalization should derive the corresponding exact kernel in a non-Boolean category rather than infer it from dimension counting.

## Lean-formalizable core

- Joint-versus-marginal pushforward factorization.
- Walsh characterization of `k`-marginal kernels.
- Simplicial scenario kernel and target recoverability criterion.
- Finite weighted set-cover formulation for minimal target lifts.
