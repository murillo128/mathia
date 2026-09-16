---
type: adversarial-review
target: research/arithmetic_fidelity/findings/AF-376-uniform-separation-defeats-e-polya-frequency-determination.md
---

# Adversarial review

## Adversary

The compact-support exclusion invokes Schoenberg's characterization in the wrong direction. For an integrable Pólya-frequency function, the bilateral Laplace transform is `F(z)=1/Psi(z)` on its strip of convergence, where `Psi` is a Laguerre--Pólya entire function; equation (8) instead identifies `F` itself with the Laguerre--Pólya product. The subsequent argument from positivity of `F(t)` to vanishing `alpha_i`, and hence to (9), therefore does not follow from the cited theorem.

This does not appear to damage the uniformly-discrete determinant construction, and the intended conclusion that a nonzero compactly supported integrable function cannot be a full Pólya-frequency function is classical and likely easy to restore. For example, Schoenberg's support classification says a nontrivial PF function is either one-sided (vanishing on a semi-axis) or nonvanishing on the real line, which already excludes bounded compact support; alternatively the reciprocal Laplace-transform characterization can be used correctly with the needed analytic-continuation argument. Please replace the load-bearing exclusion proof with a correct version and fix the statement of Schoenberg's theorem. As stored, the proof of the required false-positive distinction relies on a false transform identity.