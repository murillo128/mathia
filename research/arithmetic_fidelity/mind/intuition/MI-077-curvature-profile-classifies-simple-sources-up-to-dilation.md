# MI-077 — A full curvature profile classifies simple positive sources only up to dilation

**Evidence level:** exact source-classification theorem from [AF-509](../../findings/AF-509-log-prime-sum-curvature-classifies-simple-sources-up-to-dilation.md), contrasted with the finite-sample deformation results AF-483--AF-490.

For a simple locally finite unit-weight source `Q`, let `P_Q(s)=sum_q q^(-s)` on a common half-plane of convergence. AF-509 identifies the logarithmic curvature

`kappa_Q(s)=(log P_Q)''(s)=Var_(mu_(Q,s))(log q)`

as an exact gauge-classifying observable. If two such sources have the same curvature on a nonempty open interval, analyticity forces their log partition functions to differ by an affine function. Unit weights remove the independent mass factor, leaving precisely the geometric dilation gauge: `R=cQ`. Conversely dilation changes `log P` by a linear term and therefore leaves the curvature profile unchanged.

This is the positive counterpart to the finite-data nonfaithfulness results. Finitely many moments or prime-sum samples leave large fibers, but an entire open-interval curvature profile can collapse the simple unit-weight fiber to one explicit one-parameter gauge. One additional scalar fixing the smallest atom removes that gauge. If the admitted source class is primitive integer support, dilation is already excluded and the profile becomes exact source identification inside that class.

The reusable distinction is between **measurement richness** and **source-class rigidity**. The open-interval profile supplies genuinely infinite tied analytic information; primitivity is a separate admissible-class restriction. Neither may be silently inferred from the other. A representation can therefore be highly nonfaithful under every finite sample while becoming exact once a full analytic profile and an independently justified gauge-fixing source class are retained.

**Boundary.** AF-509 is exact and noiseless. It does not give stable recovery from approximate curvature, finite windows or finitely many samples; arbitrary weights or repeated atoms introduce extra ambiguity; and primitive integer support is an external source restriction that must be justified by the application. The result is a source-identification theorem, not an RH consequence.