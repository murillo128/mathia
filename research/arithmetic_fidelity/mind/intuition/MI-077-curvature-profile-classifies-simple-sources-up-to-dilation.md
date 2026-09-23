# MI-077 — A full curvature profile canonically recovers a simple positive source modulo dilation

**Evidence level:** exact source-classification and constructive-recovery theorems from [AF-509](../../findings/AF-509-log-prime-sum-curvature-classifies-simple-sources-up-to-dilation.md) and [AF-510](../../findings/AF-510-curvature-has-explicit-canonical-inverse-on-dilation-quotient.md), sharpened by the exact instability construction [AF-511](../../findings/AF-511-remote-prime-replacement-destroys-positive-relative-curvature-provenance-margin.md) and contrasted with the finite-sample deformation results AF-483--AF-490.

For a simple locally finite unit-weight source `Q={q_1<q_2<...}`, let `P_Q(s)=sum_q q^(-s)` on a common half-plane of convergence and

`kappa_Q(s)=(log P_Q)''(s)=Var_(mu_(Q,s))(log q)`.

AF-509 identifies this logarithmic curvature as an exact gauge-classifying observable. If two such sources have the same curvature on a nonempty open interval, analyticity forces their log partition functions to differ by an affine function. Unit weights remove the independent mass factor, leaving precisely geometric dilation: `R=cQ`. Conversely dilation changes `log P` only by a linear term and therefore leaves the curvature profile unchanged.

AF-510 makes that quotient statement constructive. Writing `lambda_n=log(q_n/q_1)`, the quotient representative with smallest atom normalized to one is recovered directly from curvature by

`H_Q(s)=int_s^infinity (t-s) kappa_Q(t) dt = log(q_1^s P_Q(s))`

and hence

`F_Q(s)=exp(H_Q(s))-1=sum_(n>=2) exp(-s lambda_n)`.

The two integration constants are not extra choices: on the normalized quotient section the positive unit leading atom forces the boundary conditions at infinity. The normalized atoms can then be peeled from the positive exponential sum. In particular the first ratio is already encoded in the curvature tail: if `delta=log(q_2/q_1)`, then `kappa_Q(s)~delta^2 exp(-delta s)` and `delta=-lim_(s->infinity) s^(-1) log kappa_Q(s)`.

AF-511 makes the exact-versus-stable distinction quantitative even with the scale gauge removed. For the ordinary prime source `P`, replace a remote odd prime `p_n` by the composite `p_n+1`. The resulting primitive integer source keeps the least generators and the same natural scale anchor, yet for every fixed `sigma>1`

`sup_(s>=sigma) |log kappa_Rn(s)-log kappa_P(s)| -> 0`.

The mechanism is exponential shielding: the one-atom perturbation is suppressed like `(2/p_n)^s`, whereas the persistent `2,3` pair supplies a curvature floor of order `(2/3)^s`, leaving relative error of order `(3/p_n)^s` up to polynomial logarithmic factors. Thus the full half-line profile remains exactly injective while the prime source has no positive isolation radius in this relative-profile topology.

This separates four notions that should not be conflated. A finite family of samples can leave a large source fibre; the exact full curvature profile is faithful modulo one explicit dilation gauge; fixing primitive integer scale can turn exact quotient equality into exact source identification; and robust provenance still depends on a declared topology and target margin. Primitive integer support removes the gauge but does not prevent remote arithmetic edits from becoming arbitrarily small in `sup_(s>=sigma)|Delta log kappa|`.

The reusable lesson is that exact inversion and robust classification are different mathematical claims even when the observation family is infinite. A robust prime discriminator based on curvature must either use a topology that prices remote generators more strongly, add independent arithmetic incidence such as additive/congruence structure, or ask only for a coarser property whose decision classes are positively separated in the chosen observation norm.

**Boundary.** AF-509--AF-511 assume simple unit-weight positive sources. AF-511 is a fixed-`sigma>1` statement for a specific relative whole-tail metric and remote prime-to-composite replacements; it does not prove instability in every stronger topology, give a minimax lower bound for noisy inversion, or rule out a robust discriminator for a coarser RH-relevant property. Exact classification modulo dilation remains valid, and arbitrary positive weights, repeated atoms and other observation norms require separate analysis.