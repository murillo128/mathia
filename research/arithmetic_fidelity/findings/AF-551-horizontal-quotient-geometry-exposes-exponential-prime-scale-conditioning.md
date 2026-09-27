# AF-551 — Horizontal quotient geometry exposes exponential prime-scale conditioning

## Status

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · QUOTIENT-GEOMETRY · CONDITIONING · DIRICHLET-TAIL · MATCHED-CONTROL · NO-NOVELTY-CLAIM

## Claim

AF-550 proves that complete relative transition profiles survive arbitrary common monotone output recalibration and that, for the rational-prime tails, the absolute logarithmic prime scale is encoded in an exponentially small departure from an affine asymptote. Its additive-output conditioning discussion still uses a vertical coordinate that an unrestricted recalibration can distort arbitrarily.

There is a calibration-invariant horizontal geometry in which the same instability remains.

Let \(I\) be an interval and let

\[
F=(f_i)_{i=1}^m,\qquad G=(g_i)_{i=1}^m
\]

be two labelled families of same-orientation diffeomorphisms from \(I\) onto target intervals, with a fixed reference branch \(i=1\). Write

\[
H_i^F=f_1^{-1}\circ f_i,\qquad
H_i^G=g_1^{-1}\circ g_i.
\tag{1}
\]

Each \(H_i\) is unchanged by an arbitrary common orientation-preserving postcomposition of its family. On a compact \(I\), define

\[
\boxed{
d_{\rm ref}([F],[G])
=
\max_{2\le i\le m}
\left\|
(H_i^F)^{-1}\circ H_i^G-\operatorname{id}_I
\right\|_\infty .
}
\tag{2}
\]

Within a fixed reference-orientation component, (2) is a genuine metric on the common-postcomposition quotient. It is therefore a natural way to measure the horizontal/domain displacement left after the output calibration has been removed.

For the prime-tail scale channel, this metric geometry exposes an exponential inverse-conditioning barrier using a source-natural matched generalized-prime control, not an arbitrary observation perturbation.

Let \(H_2\) be the rational-prime transition from AF-550,

\[
H_2(s)
=
\alpha s
-
\frac1{\log2}\left(\frac35\right)^s
+
o\!\left(\left(\frac35\right)^s\right),
\qquad
\alpha=\frac{\log3}{\log2}.
\tag{3}
\]

Fix

\[
1<c<\frac{\log7}{\log5}
\tag{4}
\]

and replace only the first three generalized-prime norms by

\[
q_1=2^c,\qquad
q_2=3^c,\qquad
q_3=5^c,
\qquad
q_k=p_k\quad(k\ge4).
\tag{5}
\]

This finite-prefix deformation preserves the ordering, the abscissa of convergence, the divergence of every tail at \(s=1\), and the entire asymptotic generalized-prime counting law outside a finite set. It also preserves exactly the leading transition slopes

\[
\frac{\log q_2}{\log q_1}
=
\frac{\log3}{\log2},
\qquad
\frac{\log q_3}{\log q_1}
=
\frac{\log5}{\log2}.
\tag{6}
\]

Let \(K_2\) be its corresponding second-tail transition. The AF-550 tail expansion gives

\[
K_2(s)
=
\alpha s
-
\frac1{c\log2}
\left(\frac35\right)^{cs}
+
o\!\left(\left(\frac35\right)^{cs}\right).
\tag{7}
\]

Thus the common leading slopes are identical while the absolute first norm changes from \(\log2\) to \(c\log2\).

Define the calibration-invariant horizontal comparison

\[
u_c=H_2^{-1}\circ K_2.
\tag{8}
\]

Then

\[
\boxed{
u_c(s)-s
=
\frac1{\log3}\left(\frac35\right)^s
+
o\!\left(\left(\frac35\right)^s\right).
}
\tag{9}
\]

The reverse warp \(u_c^{-1}\) has the opposite leading displacement. Hence the symmetric moving-tail horizontal discrepancy

\[
\Delta_S(H_2,K_2)
=
\max\left\{
\sup_{s\ge S}|u_c(s)-s|,
\sup_{s\ge S}|u_c^{-1}(s)-s|
\right\}
\tag{10}
\]

satisfies

\[
\boxed{
\Delta_S(H_2,K_2)
=
\frac1{\log3}
\left(\frac35\right)^S
(1+o(1)).
}
\tag{11}
\]

The target log-scale gap is nevertheless fixed:

\[
|\log q_1-\log2|=(c-1)\log2.
\tag{12}
\]

Therefore any decoder of the AF-550 scale channel
\((\alpha_2,\alpha_3,H_2)\) whose inverse is \(L_S\)-Lipschitz with respect to the tail horizontal discrepancy must obey

\[
\boxed{
L_S
\ge
(c-1)\log2\,\log3
\left(\frac53\right)^S
(1+o(1)).
}
\tag{13}
\]

The exponential instability of the absolute prime scale is therefore not an artifact of measuring additive error in an arbitrary output coordinate. It persists after quotienting unrestricted common output calibration and measuring the remaining discrepancy in a horizontal registration geometry.

## Reference-gauged metric on the calibration quotient

For a homeomorphism \(h:I\to I\),

\[
\|h-\operatorname{id}\|_\infty
=
\|h^{-1}-\operatorname{id}\|_\infty,
\tag{14}
\]

because writing \(y=h(x)\) gives

\[
|h^{-1}(y)-y|=|x-h(x)|.
\]

This proves symmetry of (2).

For three profile families \(F,G,K\), set

\[
U_i^{FG}=(H_i^F)^{-1}\circ H_i^G.
\]

Then

\[
U_i^{FK}=U_i^{FG}\circ U_i^{GK}.
\tag{15}
\]

Consequently

\[
\|U_i^{FK}-\operatorname{id}\|_\infty
\le
\|U_i^{FG}-\operatorname{id}\|_\infty
+
\|U_i^{GK}-\operatorname{id}\|_\infty,
\tag{16}
\]

and taking the maximum over \(i\) gives the triangle inequality.

Finally, \(d_{\rm ref}=0\) exactly when all relative transitions agree. By AF-550's complete-orbit theorem, that is exactly equality of the common-postcomposition orbit once the reference orientation is fixed. Thus (2) is a metric on that quotient, not merely a coordinate-dependent seminorm on raw outputs.

The metric is reference-gauged: changing the marked reference branch or reparameterizing the source domain changes the geometry. That is a feature, not a hidden invariance claim. In the ordered prime-tail problem, the first tail is retained provenance and supplies the declared reference.

## Relation to horizontal registration

The geometry has an operational registration interpretation. Suppose a second observed family is generated by one common output recalibration together with branchwise domain warps,

\[
g_i=\psi\circ f_i\circ v_i,
\tag{17}
\]

where each \(v_i:I\to I\) is orientation preserving. Then

\[
H_i^G
=
v_1^{-1}\circ H_i^F\circ v_i.
\tag{18}
\]

If

\[
\delta_j=\|v_j-\operatorname{id}\|_\infty
\]

and \((H_i^F)^{-1}\) is Lipschitz, then

\[
\left\|
(H_i^F)^{-1}\circ H_i^G-\operatorname{id}
\right\|_\infty
\le
\delta_i
+
\operatorname{Lip}\!\left((H_i^F)^{-1}\right)\delta_1.
\tag{19}
\]

So the quotient coordinate measures a genuine horizontal registration error after common vertical calibration has been cancelled.

For continuous strictly increasing distribution functions \(F,G\), the same expression reduces to the standard one-dimensional quantile displacement:

\[
\sup_x |F^{-1}(G(x))-x|
=
\sup_{0<u<1}|F^{-1}(u)-G^{-1}(u)|.
\tag{20}
\]

The right-hand side is the familiar \(W_\infty\) monotone-transport distance. This is prior-art calibration for the geometry, not a novelty claim for (2).

## Generic exponential residual threshold

The arithmetic calculation is an instance of a simple general fact. Suppose two increasing transition profiles satisfy

\[
H(s)=\alpha s+C e^{-\beta s}+o(e^{-\beta s}),
\qquad
K(s)=\alpha s+o(e^{-\beta s}),
\tag{21}
\]

with \(\alpha,\beta>0\) and \(C\ne0\). Let

\[
u=H^{-1}\circ K.
\]

Since both profiles equal \(\alpha s+o(1)\), one first has \(u(s)-s\to0\). Writing \(u(s)=s+\eta(s)\) in \(H(u(s))=K(s)\) gives

\[
\alpha\eta(s)+C e^{-\beta s}+o(e^{-\beta s})=0,
\]

hence

\[
\boxed{
u(s)-s
=
-\frac C\alpha e^{-\beta s}
+
o(e^{-\beta s}).
}
\tag{22}
\]

Thus removing the first exponentially small residual from a transition costs only an exponentially small horizontal warp. Conversely, a horizontal perturbation \(u(s)=s+\kappa e^{-\gamma s}\) with \(\gamma<\beta\) changes the apparent leading residual exponent to \(\gamma\), while a critical perturbation with \(\gamma=\beta\) can cancel the first residual coefficient when \(\kappa=-C/\alpha\).

For the prime transition (3),

\[
C=-\frac1{\log2},
\qquad
\beta=\log(5/3),
\]

so the critical horizontal warp is exactly

\[
s\longmapsto
s+\frac1{\log3}\left(\frac35\right)^s.
\tag{23}
\]

Equation (9) shows that this is not merely an artificial perturbation direction: it is the leading quotient displacement from the rational primes to every fixed finite-prefix power deformation (5) with \(c>1\).

## Matched generalized-prime control

The finite-prefix construction is stricter than the global power-rescaling control used in AF-550.

A global replacement \(p_k\mapsto p_k^c\) rescales the convergence boundary. By contrast, (5) changes only three generator norms. Therefore

\[
\sum_k q_k^{-s}
-
\sum_p p^{-s}
\]

is a finite Dirichlet sum, so the abscissa of convergence and all large-index counting behavior are unchanged. Condition (4) ensures that the deformed prefix remains ordered before the undeformed norm \(7\).

The first three logarithmic norms are multiplied by the same \(c\), so the slope data in (6) are unchanged. But the first residual exponent of the second transition becomes

\[
c\log(5/3),
\]

and the absolute first log norm becomes \(c\log2\). The matched control therefore differs in exactly the scale information that AF-550 extracts from the residual while preserving both its leading projective data and the coarse global tail class.

This supplies a source-class obstruction rather than only an ambient observation-space obstruction: rational primes and a natural generalized-prime deformation can be exponentially close in the calibration-invariant tail registration coordinate while their decoded absolute scale remains separated by a fixed amount.

## Prior-art / novelty audit

No novelty is claimed for horizontal curve registration, phase/amplitude separation, one-dimensional monotone transport, \(W_\infty\), or quotient metrics under group actions.

J. O. Ramsay and Xiaochun Li, “Curve Registration,” Journal of the Royal Statistical Society Series B 60(2), 351–363 (1998), DOI 10.1111/1467-9868.00129, is classical functional-registration prior art for monotone horizontal/time warps.

J. S. Marron, James O. Ramsay, Laura M. Sangalli, and Anuj Srivastava, “Functional Data Analysis of Amplitude and Phase Variation,” Statistical Science 30(4), 468–484 (2015), DOI 10.1214/15-STS524, reviews phase variation as lateral deformation distinct from amplitude variation.

Filippo Santambrogio, *Optimal Transport for Applied Mathematicians*, Birkhäuser (2015), DOI 10.1007/978-3-319-20828-2, supplies standard one-dimensional monotone-rearrangement and \(L^\infty\)/supremal-transport context for (20). AF-551 also reuses the relative-distribution prior art already recorded under AF-550.

The metric proof, the asymptotic inversion (22), and the finite-prefix generalized-prime control are derived directly here. A targeted search did not identify this exact prime-tail quotient-conditioning statement, but absence from that search is not a novelty claim. The Arithmetic Fidelity contribution is the boundary conclusion: AF-550's exponentially weak absolute-scale carrier remains exponentially ill-conditioned in a calibration-invariant horizontal geometry and against a control that preserves the convergence boundary and all but finitely many prime norms.

## Boundaries and failure modes

- **The reference branch is retained structure.** Equation (2) depends on the marked reference profile. Changing the reference is another quotient problem.
- **The source coordinate is not quotiented.** Arbitrary reparameterization of the input variable would erase the horizontal geometry being used here.
- **The tail discrepancy is a conditioning profile, not the whole quotient metric.** Equation (10) measures how the quotient coordinate behaves on \(s\ge S\); behavior on a bounded prefix may remain \(O(1)\).
- **The matched control is a generalized-prime system, not another rational-prime sequence.** Its role is falsification of stable prime-specific recovery at the declared information layer.
- **Only the AF-550 scale channel is lower-bounded.** The result concerns the decoder using \((\alpha_2,\alpha_3,H_2)\). A richer downstream representation may retain additional, better-conditioned information and must be audited separately.
- **Exact fidelity is unchanged.** For every finite \(S\), the profiles are distinct and exact infinite-precision data can separate them. The theorem is about inverse conditioning, not exact orbit collision.
- **No RH consequence follows.** The result sharpens the stability boundary of one prime-recovery representation; it does not establish or refute a route to RH.

## Decisive audit tests

1. Verify symmetry and the triangle inequality in (14)–(16), and verify that zero distance is exactly AF-550 orbit equality.
2. Substitute (17) and derive the registration bound (19) without using an output-coordinate norm.
3. Check that (4) makes the sequence (5) strictly increasing and that finite modification leaves the convergence boundary at \(s=1\).
4. Apply the AF-550 two-term tail expansion to (5) and verify (7), including the coefficient \(1/(c\log2)\).
5. Expand \(H_2^{-1}\circ K_2\) directly and verify the coefficient \(1/\log3\) in (9).
6. Use (11) and (12) to verify the exponential inverse-Lipschitz lower bound (13).

## Consequence for the research line

AF-550 established that full nonlocal tail transitions escape unrestricted output calibration exactly, but left open whether the exponentially small scale carrier was merely badly expressed in a vertical output coordinate.

AF-551 closes that escape negatively for the AF-550 scale channel. After quotienting common output recalibration, the rational-prime transition and a finite-prefix generalized-prime control with a fixed \(O(1)\) scale change approach one another at the exact exponential rate \((3/5)^S\) in horizontal tail registration. Recovering the absolute first log norm from that channel therefore requires an inverse condition number growing at least as \((5/3)^S\).

The next useful representation must do more than preserve the exact transition orbit. It must retain a better-conditioned source relation—possibly a boundary/global coupling, a non-tail normalization, or another target-sensitive carrier—whose separation from matched generalized-prime controls does not collapse at the same exponential rate.
