# RE-001 — Robin counterexample blocks contain regular self-tangent colossally abundant peaks

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + COUNTEREXAMPLE-REDUCTION + SELF-TANGENT-CA + PRIOR-ART-ALIGNED`. The Robin-extremal pilot asked whether exact prime-exponent moves can retain the full `log log n` normalization strongly enough to restrict hypothetical counterexample profiles. They can, but the useful object is not a generic continuous relaxation. The exact normalization selects the **tangent parameter**

\[
\varepsilon_X=\frac1{X\log X},\qquad X=\log n,
\]

and a local maximum of Robin's quotient along the colossally abundant ladder is automatically a regular colossally abundant state for this intrinsic parameter. Consequently every finite block of colossally abundant Robin counterexamples contains a regular **self-tangent** counterexample. Robin's 1984 oscillation results imply that, if RH is false, there are infinitely many such blocks and hence infinitely many regular self-tangent colossally abundant counterexamples.

The exact discrete bookkeeping then has no rounding remainder: prime-power layers form an event measure on the `X=log n` axis, and between self-tangent states the change in the Robin quotient is exactly a signed integral of the event discrepancy against the derivative of `1/(X log X)`. This same self-tangent/workload representation is independently developed in Marco Mantovanelli's August 2026 preprint *Colossally Abundant Numbers, Robin's Inequality, and an Exact Prime-Layer Workload*. The representation is therefore **not claimed as novel**. Its durable Mathia role is to close the first discretization question and move the line to the sign/size of the exact workload, where prime-distribution strength enters.

## 1. Consecutive colossally abundant states carry an exact transition slope

Write

\[
\rho(n):=\frac{\sigma(n)}n,
\qquad
G(n):=\frac{\rho(n)}{\log\log n},
\qquad
X:=\log n.
\tag{1}
\]

For `X>1` put

\[
H(X):=\log\log X,
\qquad
g(X):=H'(X)=\frac1{X\log X}.
\tag{2}
\]

Then

\[
\log G(n)=\log\rho(n)-H(\log n),
\tag{3}
\]

and

\[
H''(X)=-\frac{\log X+1}{X^2(\log X)^2}<0.
\tag{4}
\]

Thus `H` is strictly concave throughout the large-number regime relevant to Robin's criterion.

Let `A<B` be consecutive colossally abundant numbers. The classical Alaoglu--Erdos/Robin variational description gives a transition parameter `epsilon(A,B)>0` at which both states maximize

\[
\log\rho(m)-\varepsilon\log m.
\]

Hence, with `x=log A` and `y=log B`,

\[
\boxed{
\log\rho(B)-\log\rho(A)
=\varepsilon(A,B)(y-x).
}
\tag{5}
\]

This is already the exact exchange identity needed by the discrete relaxation: a whole CA transition, including a tied transition containing more than one prime layer, has one supporting slope and no unquantified rounding term.

## 2. A local Robin peak on the CA ladder is self-tangent

Let

\[
A<C<B
\]

be three consecutive colossally abundant numbers and assume

\[
G(C)>G(A),
\qquad
G(C)\ge G(B).
\tag{6}
\]

Put

\[
x=\log A,\qquad X=\log C,\qquad y=\log B,
\]

and denote the adjacent CA transition slopes by

\[
\varepsilon_-:=\varepsilon(A,C),
\qquad
\varepsilon_+:=\varepsilon(C,B).
\]

Using (3) and (5), the first inequality in (6) gives

\[
\varepsilon_-
>
\frac{H(X)-H(x)}{X-x}.
\tag{7}
\]

Strict concavity of `H` makes the backward secant larger than the tangent at its right endpoint, so

\[
\frac{H(X)-H(x)}{X-x}>H'(X)=g(X).
\tag{8}
\]

Similarly the second inequality in (6) gives

\[
\varepsilon_+
\le
\frac{H(y)-H(X)}{y-X}
<g(X),
\tag{9}
\]

where the final strict inequality is the forward-secant form of concavity. Therefore

\[
\boxed{
\varepsilon_+<\frac1{X\log X}<\varepsilon_-.
}
\tag{10}
\]

A colossally abundant state remains the maximizer for every supporting slope between its adjacent transition slopes. Equation (10) therefore proves

\[
\boxed{
C\text{ is colossally abundant for }
\varepsilon_C=\frac1{\log C\,\log\log C}.
}
\tag{11}
\]

Moreover the inequalities are strict, so `epsilon_C` is not a tied transition value: the CA maximizer at this parameter is unique. In the event-coordinate language below, `C` is a **regular self-tangent state**.

This argument keeps the complete Robin normalization. Replacing `H` by its tangent before checking the discrete state would only give a heuristic continuous optimum; here concavity shows exactly why the discrete CA supporting interval contains the intrinsic tangent slope.

## 3. Hypothetical failure forces self-tangent counterexample states

Robin proved two facts about the CA subsequence that are load-bearing here: if RH is false, infinitely many colossally abundant numbers satisfy

\[
G(C)>e^\gamma,
\tag{12}
\]

while there are also infinitely many colossally abundant numbers with

\[
G(C)<e^\gamma.
\tag{13}
\]

Hence, under failure of RH, the ordered CA sequence has infinitely many finite blocks on which `G>e^gamma`, bracketed by CA states below the Robin threshold. In each such block choose the **leftmost** state `C` at which `G` is maximal within the block. Its immediate CA predecessor has smaller `G`, while its immediate successor has `G<=G(C)`. The hypotheses (6) hold, so (11) applies.

Therefore

\[
\boxed{
\mathrm{RH\ false}
\Longrightarrow
\text{infinitely many regular self-tangent CA states }C
\text{ with }G(C)>e^\gamma.
}
\tag{14}
\]

This is stronger than merely restricting a hypothetical violation to the colossally abundant set: the parameter witnessing colossally abundance is forced to agree with the tangent of the **same** Robin normalization at `X=log C`.

No prime-number-theorem error estimate is used in (5)--(14). The reduction is variational plus the strict concavity of `log log X`; the analytic difficulty enters only after this exact subclass has been isolated.

## 4. Prime layers give an exact workload with no discretization remainder

For a prime `p` and layer `j>=1`, the logarithmic gain from increasing the exponent of `p` from `j-1` to `j` is

\[
\lambda_{p,j}
:=
\log\frac{1-p^{-(j+1)}}{1-p^{-j}}.
\tag{15}
\]

Its CA threshold is

\[
m_{p,j}:=\frac{\lambda_{p,j}}{\log p}.
\tag{16}
\]

Since `g(X)=1/(X log X)` is strictly decreasing, define the event location `eta_{p,j}` by

\[
g(\eta_{p,j})=m_{p,j}.
\tag{17}
\]

Let

\[
d\Phi=\sum_{p,j}(\log p)\,\delta_{\eta_{p,j}},
\qquad
\Phi(X):=\int_{(0,X]}d\Phi.
\tag{18}
\]

Away from tied event points, the CA state selected by the parameter `g(X)` is

\[
C_X=\prod_{\eta_{p,j}\le X}p,
\qquad
\boxed{\log C_X=\Phi(X).}
\tag{19}
\]

Define the workload/discrepancy

\[
D(X):=X-\Phi(X).
\tag{20}
\]

A self-tangent state is exactly a zero `D(X)=0`: then `X=log C_X` and the external parameter `g(X)` equals the intrinsic Robin tangent parameter of that same state.

At an event `eta_{p,j}`, equation (17) gives the exact abundance gain

\[
\lambda_{p,j}=g(\eta_{p,j})\log p.
\tag{21}
\]

Consequently, if `a<b` are regular self-tangent zeros and `C_a,C_b` their CA states,

\[
\begin{aligned}
\log\frac{G(C_b)}{G(C_a)}
&=\int_{(a,b]}g(x)\,d\Phi(x)-\int_a^bg(x)\,dx\\
&=-\int_a^bg(x)\,dD(x)\\
&=\boxed{\int_a^bD(x)g'(x)\,dx},
\end{aligned}
\tag{22}
\]

because `D(a)=D(b)=0`. Thus the entire finite transition and normalization cost is encoded by one signed workload. There is no separate continuous-to-discrete rounding error left to estimate.

## 5. Prior art and the actual remaining barrier

Alaoglu and Erdos already give the prime-exponent threshold structure behind (5) and (15)--(19). Robin's 1984 paper supplies the RH criterion, the CA envelope, and the above/below-threshold CA behavior used in (12)--(14).

Most importantly for novelty, Marco Mantovanelli's August 2026 preprint *Colossally Abundant Numbers, Robin's Inequality, and an Exact Prime-Layer Workload* independently organizes the CA thresholds on the `X=log n` axis with exactly the tangent parameter

\[
\varepsilon_X=(X\log X)^{-1},
\]

calls `D(X)=0` a self-tangent CA state, and states the packet identity (22). Its public companion at Zenodo DOI `10.5281/zenodo.22014299` provides exact finite certificates for the event sweep and self-tangent returns. The preprint further reports a prime-frontier asymptotic for the workload. Those later asymptotics are prior-art context here; they are not needed to prove (5)--(22).

Accordingly, **self-tangency and the workload representation are prior art, not a new Mathia mechanism**. The substantive outcome of this finding is the exact counterexample reduction (14), independently reconstructed together with the workload splice, and the consequent removal of the vague "rounding error" from the research question.

The remaining RH-facing obligation is now precise: obtain an unconditional sign or exclusion theorem for the workload integral in (22) on the self-tangent counterexample class, or prove that the required control is already equivalent to an RH-strength estimate for the prime-distribution component of `D`. Merely deriving the CA exponent formula, optimizing a smooth exponent profile, or numerically enumerating further CA states no longer addresses that gate.

## 6. Boundaries and falsification checks

The local-peak implication uses **consecutive CA states**, not arbitrary integer neighbors. A Robin counterexample is not asserted to be self-tangent merely because it is colossally abundant; the block-maximum argument and Robin's oscillation facts are what produce the self-tangent subclass under RH failure.

The strict concavity of `H(X)=log log X` is load-bearing. Replacing the exact normalization by an asymptotic surrogate can move the tangent outside the supporting interval and invalidates (10). Likewise, the transition identity (5) requires the true supporting parameter shared by consecutive CA states; an arbitrary two-prime exchange does not automatically have that slope.

Equation (22) is exact only when the endpoints are self-tangent zeros of the same CA event process. It does not by itself give the sign of the integral. Since `g'(x)<0`, a useful theorem must control the signed distribution of `D`, not merely its absolute size or average magnitude. A prime-number-theorem error estimate that is already RH-equivalent would only move the target conclusion into the hypothesis.

Finally, the recent workload preprint is a 2026 preprint, not an independent proof of RH. Its overlap is used to set the prior-art boundary. The exact identities persisted here have been reconstructed directly from the CA variational definition and Robin normalization rather than treating the preprint's finite certificates or asymptotic claims as proof of the Mathia reduction.