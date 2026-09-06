# WI-181 — unit trace imposes a quantitative activation gate on the full-Gram rank tail

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + ROUTE-SPECIFIC-OBSTRUCTION`. The proof below is an elementary finite-dimensional derivation from the WI-180 interface. Finite rational checks supplement, but do not prove, the general statement. This is not a Lean-certified or independently adversarially accepted result, and it does not improve an unconditional zeta-zero proportion.

WI-180 makes a nonlinear rank-screening penalty observable on the full simple-real Gram. Before seeking a source theorem to activate it, one must retain another exact source constraint: this Gram has unit diagonal and therefore trace equal to the number of simple real points. Every eigenvalue above 2 consumes both its own clipped defect and compensating trace deficit in the remaining eigenvalues.

Combining this trace cost with the exceptional-population charge gives a concrete gate. If a finite Lamzouri multiset satisfies

\[
Q\le(1+c)N,\qquad 0<c\le\tfrac13,
\]

and the WI-180 tail is positive, then

\[
\boxed{\frac nN>\alpha_*(c):=
\frac{5-3c+\sqrt{(5-3c)^2-16(1-c)}}8.}
\tag{A}
\]

At the ideal Montgomery–Taylor budget

\[
c=C_{\rm MT}-1=0.3274992963205885\ldots,
\]

this gives

\[
\alpha_*(c)=0.7921315071658177\ldots.
\]

This number is an **activation threshold**, not a lower bound proved for zeta zeros. In the actual asymptotic source theorem, the smoothing error and the height-dependent error must be included in `c`; taking their limits gives the displayed limiting threshold. In particular, the new tail is not an automatically available infinitesimal improvement around the approximately 67.25% baseline. An independent theorem forcing it positive could instead make a substantial jump; this finding does not forbid such a theorem.

## 1. Source interface and exact population bookkeeping

Use WI-170 and WI-180 notation. Let `N` count all labels with multiplicity, `D` count distinct elements, `n` count simple real elements, `r` count distinct repeated-real points, and `k` count distinct non-real conjugate pairs. Write

\[
e:=D-n=r+2k,\qquad M:=N-D=N-n-e,
\qquad O:=2\sum_{z\in Z_+}m_z.
\tag{1}
\]

Here `M` is multiplicity excess and `O` is the multiplicity-weighted non-real population. In particular, neither `e` nor `N-n` is automatically an off-critical population.

For the full simple-real Gram `G_s`, Lamzouri's normalization gives

\[
G_s\succeq0,\qquad (G_s)_{xx}=\|f_x\|^2=1,
\qquad \operatorname{tr}G_s=n.
\tag{2}
\]

Let its eigenvalues be `mu_1>=...>=mu_n>=0`, and put

\[
\Psi(t)=\begin{cases}(t-1)^2,&0\le t\le2,\\2t-3,&t\ge2,\end{cases}
\qquad d:=\operatorname{tr}\Psi(G_s).
\tag{3}
\]

WI-180 establishes

\[
Q-N\ge O+2M+d+\mathcal T_e(G_s),
\qquad
\mathcal T_e(G_s)=\sum_{j>e}(\mu_j-2)_+^2.
\tag{4}
\]

Every repeated-real point contributes at least one to `M`, so `M>=r`; every off-line pair contributes at least two to `O`, so `O>=2k=e-r>=e-M`. Consequently

\[
\boxed{O+2M\ge\max\{2M,e+M\}
=\max\{2M,N-n\}.}
\tag{5}
\]

This inequality remains valid with arbitrary higher real or non-real multiplicities. It is important not to replace distinct exceptional counts by label counts in the tail.

## 2. Trace forces a compensating subcritical defect

Let `G` be any positive-semidefinite matrix of size `n` with trace `n`, and define

\[
q:=\#\{j:\mu_j(G)>2\}.
\]

If `q>0`, then `2q<n`. Put `s=sum_{j<=q} mu_j`, so `s>2q`. The supercritical part contributes `2s-3q` to `tr Psi(G)`. The remaining eigenvalues lie in `[0,2]`, have sum `n-s`, and therefore satisfy, by Cauchy–Schwarz,

\[
\sum_{j>q}(\mu_j-1)^2
\ge\frac{((n-s)-(n-q))^2}{n-q}
=\frac{(s-q)^2}{n-q}.
\]

The function `2s-3q+(s-q)^2/(n-q)` is strictly increasing for `s>=2q`. It follows that

\[
\boxed{\operatorname{tr}\Psi(G)>
q+\frac{q^2}{n-q}=\frac{nq}{n-q}\qquad(q>0).}
\tag{6}
\]

The boundary value is approached by spectra with `q` eigenvalues tending to 2 from above and all remaining eigenvalues equal to `(n-s)/(n-q)`. Thus the estimate is sharp as an infimum at the trace-constrained spectral level whenever `2q<n`. This spectral sharpness does not assert realizability by a Montgomery–Taylor kernel Gram.

A convenient diagnostic is

\[
q<\frac{nd}{n+d}\qquad(q>0).
\tag{7}
\]

The extra term `q^2/(n-q)` is essential. Counting only one unit of defect per supercritical mode discards the trace compensation and produces a substantially weaker gate.

## 3. Finite activation test, including its integer improvement

Positivity of `T_e(G_s)` means `q>=e+1`. In particular,

\[
2(e+1)<n
\tag{8}
\]

is necessary. Equations (4)–(6) imply the explicit finite condition

\[
\boxed{
\mathcal T_e(G_s)>0
\ \Longrightarrow\
Q-N>\max\{2M,N-n\}
+\frac{n(e+1)}{n-e-1}.
}
\tag{9}
\]

The denominator is positive whenever activation is possible. If (8) fails, the tail is identically zero without evaluating (9). The actual positive tail adds further cost; (9) conservatively discards that cost.

Equivalently, an available upper bound `h>=d` excludes activation whenever

\[
h\le\frac{n(e+1)}{n-e-1},
\]

provided the denominator is positive. The weaker non-integer version uses `ne/(n-e)` and is useful for continuous population optimization. All these statements are necessary-condition tests, not source estimates for `d` or for `q`.

## 4. Optimize over all multiplicity compositions

Assume `Q-N<=cN` with `0<c<=1/3`. Equations (4)–(5) already give `n/N>=1-c>=2/3`. Set

\[
\alpha=n/N,\qquad \beta=e/N,\qquad b=1-\alpha,
\qquad M/N=b-\beta.
\]

If the tail is positive, (6) with `q>e` and (5) give

\[
c>\max\{2(b-\beta),b\}
+\frac{\alpha\beta}{\alpha-\beta}.
\tag{10}
\]

Here `0<=beta<=b` and activation requires `beta<alpha/2`. For `alpha>=2/3`, the right side of (10) is minimized at `beta=b/2`.

Indeed, for `beta>=b/2` it is `b+alpha beta/(alpha-beta)`, an increasing function. For `beta<=b/2` its derivative is

\[
-2+\frac{\alpha^2}{(\alpha-\beta)^2}<0,
\]

because `beta/alpha<=b/(2alpha)<=1/4`, so the second term is at most `16/9<2`. Therefore

\[
\boxed{c>F(\alpha):=
\frac{(1-\alpha)(4\alpha-1)}{3\alpha-1}.}
\tag{11}
\]

The minimizing composition is the relaxed all-real-double exceptional composition: `O=0`, `M=e=(N-n)/2`. It is a lower-cost control for the activation calculation, not a statement that the zeta exceptions are double zeros.

On `[2/3,1]`, `F` is strictly decreasing, since

\[
F'(\alpha)=\frac{-2(6\alpha^2-4\alpha+1)}{(3\alpha-1)^2}<0.
\]

Solving `F(alpha)=c` gives the root in (A). This proves (A) with no unmentioned assumption on multiplicity. Retaining the integer increment in (9) only strengthens the finite statement.

## 5. All-simple control and interpretation at the zeta source scale

If the entire multiset is simple, then `M=0`, `e=O=N-n`. With `x=e/N`, activation instead requires

\[
c>x+\frac{x(1-x)}{1-2x}
=\frac{x(2-3x)}{1-2x}.
\]

Hence

\[
\frac nN>
1-\frac{2+2c-\sqrt{(2+2c)^2-12c}}6.
\tag{12}
\]

At the ideal Montgomery–Taylor budget this is `0.8518463069096244...`. This stronger number requires simplicity of the entire finite multiset and must not be asserted for an arbitrary exceptional population.

Lamzouri's source result provides `Q/N=C_eta+o(1)` for each fixed admissible smoothing, with `C_eta` approaching `C_MT`. The finite theorem is applied with an actual upper budget `c=C_eta-1+error`, eventually below `1/3`; only afterward may the smoothing and height limits be taken in the established order. The finite decimal thresholds are not a justification for interchanging these limits or ignoring their constants.

The result concerns the **full-Gram** tail in WI-180. It does not establish the same threshold for the sharper, source-dependent quotient tail `T_k(S)` in WI-179: that tail has a different cutoff and a different trace. Nor does it invalidate the ordinary Gram-defect improvement in WI-178, which need not cross the eigenvalue-2 threshold.

## 6. Verification, prior art, and decisive boundaries

The analytic proof uses only Cauchy–Schwarz, exact population bookkeeping, and one-variable minimization. A finite check enumerated all 4,394 nonnegative spectra with dimensions `1..5`, entries in `(1/3) Z`, and sum equal to dimension. All 2,667 cases with nonzero supercritical count satisfied the strict inequality (6). A separate exact rational enumeration checked 10,959 relaxed population configurations with `3<=N<=80`, `n/N>=2/3`, and `0<=e<=N-n`, against the lower envelope (11), with no violation. These are reproducible finite audits of the proof's algebra, not evidence that the actual zeta Gram has a particular spectrum.

For a compact reproduction, enumerate weak compositions of `3*n` into `n` parts, divide each part by 3 using exact rational arithmetic, and compare `sum(Psi(mu))` with `n*q/(n-q)` when `q>0`. For the population check compare `max(2*(N-n-e),N-n)/N+n*e/(N*(n-e))` with `(1-alpha)*(4*alpha-1)/(3*alpha-1)` for the stated integer ranges. The proof, not this finite enumeration, establishes the unbounded assertion.

The primary source is Y. Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1, Proposition 2.1, equation (2.8), and Lemma 3.2. Equation (2.8) explicitly supplies the unit-norm condition. The internal operator interface is WI-180, based on WI-170 and WI-178–WI-179. Cauchy–Schwarz/convex trace bounds and population optimization are classical; no novelty is claimed for those principles. The line-specific delta is their quantitative composition with the newly proposed rank-tail bootstrap. A bounded literature comparison is not a priority claim.

Three interpretations would be false: that 79.21% has been proved unconditionally; that WI-180 itself is false; or that the rank route is impossible. What has been proved is that positivity of its extra full-Gram tail already demands enough source budget to force the much stronger conditional fraction (A). A successful source theorem can jump across this gate, but generic spectral elaboration cannot silently assume the gate has opened.

## 7. Consequence for the research line

A proposed source bound on `q_epsilon(G_s)`, the supercritical participation ratio, or `T_e(G_s)` should first be checked against (9)–(11). A contradiction with the gate means that the proposed source bound contains genuinely stronger information than the original second-moment budget, or has an incorrect normalization or exceptional cutoff. The task is to identify which, not to iterate the same relaxed budget.

The most distinct escape surfaces are a source-forced jump in full-Gram supercriticality, a sharper analysis of the unscreened quotient tail before the `r+k` index loss, or source-specific coupling between the exceptional even and odd blocks that improves the rank-only relaxation. None has been established here. Even a density-one result would still need a separate argument excluding individual off-critical zeros; multiple critical-line zeros remain compatible with RH.
