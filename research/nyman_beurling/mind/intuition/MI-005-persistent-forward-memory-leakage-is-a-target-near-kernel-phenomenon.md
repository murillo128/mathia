# MI-005 — Stable tails are causal continuation phenomena not controlled by local flags, branching, or global Gram conditioning

**Evidence level:** supported by NB-063--NB-071; no bounded continuation certificate or stable-tail triviality theorem for the actual Nyman source is proved.

NB-066--NB-067 show that a hypothetical persistent Nyman target is a global continuation problem. Its finite traces are natural, but the least compatible future norm diverges; finite normalized Schur complements converge to that continuation cost and therefore provide a source-only certificate.

NB-068 proves that canonical one-cell memory is not a substitute. A nearest-neighbor scalar chain can have `Gamma_R=0` at every step and still carry a stable boundary mode. NB-069--NB-070 then add the exact source covariance missing from that control: integer-dilation branching induces exact Gram block-renormalization identities, excludes bounded fixed-band nonorthogonality, and forces every bounded nonorthogonal branch-compatible source to retain order-one aggregate Gram mass arbitrarily far from the additive diagonal.

NB-071 shows that those restrictions still do not determine the stable tail. The explicit block-isometry control

`D_j^(rho)=(I-rho V_m)e_j`, `rho>1`,

obeys exact integer-dilation branching and has the same full finite-window local flag as the flat control: the same natural trace spaces, innovation direction, zero one-cell memory, and pure local defect sectors. Its Gram operator is uniformly well-conditioned,

`(rho-1)^2 I <= H_rho <= (rho+1)^2 I`,

but its stable tail is the infinite-dimensional defect `ker(I-rho V_m*)`. Along geometric cutoffs its continuation constants grow like `rho^N`, and the NB-067 Schur certificates diverge accordingly.

The escape is neither poor conditioning nor unsigned far mass alone. Fixed signed parent-child correlations recur along the multiplicative tree at unbounded additive distance, and descendant-block compression reproduces the coarse correlation exactly. Thus **global Riesz conditioning can be excellent while finite causal continuation is exponentially ill-conditioned**.

The live invariant must therefore distinguish the actual Nyman source from this branch-compatible tree control. Candidate inputs include arithmetic sign/phase structure of the canonical Gram entries across multiplicative descendants, a source-specific relation between finite causal trace norm and the nonlocal Gram continuation, or another exact identity that forbids backward-eigenvector defects of the NB-071 type. Strengthening additive locality, one-cell memory, branching covariance, or ordinary Gram condition number cannot close the route.

The reusable distinction is now six-way: local memory can vanish; finite local flags can match exactly; branching can hold exactly; global Gram conditioning can stay uniformly good; coherent far signed couplings can still support a stable tail; and causal continuation cost can nevertheless diverge. The target quantity is continuation geometry, not ordinary source conditioning.

**Boundary.** NB-071 is a structural matched control, not the canonical Nyman Gram matrix. It does not prove the actual stable tail is nonzero, and it leaves open which arithmetic feature excludes or permits its multiplicative-tree mechanism. Its role is to close a broad class of generic source-only arguments.