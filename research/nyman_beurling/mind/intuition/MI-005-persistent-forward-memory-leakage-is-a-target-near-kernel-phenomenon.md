# MI-005 — Stable tails are a global continuation phenomenon, not a one-cell memory phenomenon

**Evidence level:** supported by the exact causal recursion and stable-tail theorems NB-063--NB-066, finite future Gram/Schur characterization NB-067, and matched boundary-chain control NB-068; no bounded certificate for the actual Nyman source is yet proved.

The late Nyman--Beurling quotient is not blocked by missing finite rank. NB-062--NB-066 show that visible natural spaces form a causal flag and that a hypothetical persistent target would converge to one fixed stable-tail mode whose trace is natural on every finite window while the exact global continuation norm diverges. A bounded subsequence of the continuation constants `Lambda_R` excludes the entire stable-tail space.

NB-067 makes this global obstruction finitely observable. If `A_R` is the visible prefix Gram and `S_(R,N)` is the Schur complement after optimally using future innovations through horizon `N`, then

\[
\Xi_{R,N}
=
\lambda_{\max}(A_R^{-1/2}S_{R,N}A_R^{-1/2})
\downarrow 1+\Lambda_R^2.
\]

So finite source-only generalized eigenvalues give rigorous upper certificates for the infinite continuation problem.

NB-068 proves that the canonical one-cell memory map is not a substitute for this quantity. There are two matched causal sources with the same finite visible/defect flag and

\[
\Gamma_R=0
\qquad\text{for every }R,
\]

for both sources. One has no stable tail. The other, a nearest-neighbor scalar boundary chain, has

\[
\mathcal T_\infty=\operatorname{span}\{t\}
\]

and exact continuation blow-up

\[
\Lambda_R^2
=
\frac{T_{<R}^2}{T_{\ge R}^2}
\to\infty.
\]

Its finite certificates satisfy

\[
\Xi_{R,N}
=
1+
\frac{T_{<R}^2}{T_{R:N+1}^2},
\]

and therefore diverge for every horizon schedule. The hidden global mode is fully visible to the normalized Schur geometry while being completely invisible to every one-step `Gamma_R`.

The reusable lesson is stronger than “local information may be insufficient.” **A global compatibility obstruction can be assembled entirely through directions that are removed as harmless at each individual step.** Finite causal bandwidth, zero one-cell memory, and identical local flags do not determine the stable tail; the cumulative extension cost does.

The remaining arithmetic task is therefore to control the actual Nyman future Schur complements or prove a source-specific property that rules out the boundary-chain mechanism. A useful theorem must act on the cumulative continuation geometry, not merely sharpen local leakage estimates.

**Boundary.** NB-068 is an abstract matched control, not a claim that the Nyman source contains such a boundary chain. It proves only that local-memory arguments cannot exclude one. NB-067 remains a sufficient finite certificate, but no uniformly bounded subsequence for the actual source has yet been established.
