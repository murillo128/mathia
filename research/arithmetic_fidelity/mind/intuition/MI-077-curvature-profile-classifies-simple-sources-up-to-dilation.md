# MI-077 — A full curvature profile canonically recovers a simple positive source modulo dilation

**Evidence level:** exact source-classification and constructive-recovery theorems from [AF-509](../../findings/AF-509-log-prime-sum-curvature-classifies-simple-sources-up-to-dilation.md) and [AF-510](../../findings/AF-510-curvature-has-explicit-canonical-inverse-on-dilation-quotient.md), contrasted with the finite-sample deformation results AF-483--AF-490.

For a simple locally finite unit-weight source `Q={q_1<q_2<...}`, let `P_Q(s)=sum_q q^(-s)` on a common half-plane of convergence and

`kappa_Q(s)=(log P_Q)''(s)=Var_(mu_(Q,s))(log q)`.

AF-509 identifies this logarithmic curvature as an exact gauge-classifying observable. If two such sources have the same curvature on a nonempty open interval, analyticity forces their log partition functions to differ by an affine function. Unit weights remove the independent mass factor, leaving precisely geometric dilation: `R=cQ`. Conversely dilation changes `log P` only by a linear term and therefore leaves the curvature profile unchanged.

AF-510 makes that quotient statement constructive. Writing `lambda_n=log(q_n/q_1)`, the quotient representative with smallest atom normalized to one is recovered directly from curvature by

`H_Q(s)=int_s^infinity (t-s) kappa_Q(t) dt = log(q_1^s P_Q(s))`

and hence

`F_Q(s)=exp(H_Q(s))-1=sum_(n>=2) exp(-s lambda_n)`.

The two integration constants are not extra choices: on the normalized quotient section the positive unit leading atom forces the boundary conditions at infinity. The normalized atoms can then be peeled from the positive exponential sum. In particular the first ratio is already encoded in the curvature tail: if `delta=log(q_2/q_1)`, then `kappa_Q(s)~delta^2 exp(-delta s)` and `delta=-lim_(s->infinity) s^(-1) log kappa_Q(s)`.

This separates three notions that should not be conflated. A finite family of samples can leave a large source fibre; the exact full curvature profile is faithful modulo one explicit dilation gauge; and stability of the inverse under finite windows, sampling and noise is a further quantitative problem. AF-510 makes the last distinction sharp because deeper normalized atoms are represented by exponentially smaller residuals after successive peeling. Exact quotient fidelity therefore does not imply numerically stable provenance recovery.

A separately justified source-class restriction may remove the final gauge. Primitive integer support excludes nontrivial common dilation and turns the exact quotient classifier into full source identification inside that category, but integrality is not derived by the curvature map itself. Likewise, a scalar fixing `q_1` supplies scale as side information rather than extracting it from `kappa_Q`.

**Boundary.** AF-509--AF-510 are exact and noiseless, assume a simple unit-weight positive source, and use the whole analytic tail profile. Arbitrary positive weights introduce an additional mass normalization; repeated atoms and finite/noisy observations require separate analysis. The results classify and reconstruct a source modulo dilation; they do not provide a finite-precision prime discriminator or an RH consequence.