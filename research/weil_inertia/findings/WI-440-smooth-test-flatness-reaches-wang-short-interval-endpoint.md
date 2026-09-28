# WI-440 — smooth test flatness reaches Wang's short-interval endpoint

**Status:** PRIMARY-SOURCE-AUDIT + LITERATURE+DERIVED + EXACT-ENDPOINT + MATERIAL-CORRECTION + NON-RH + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM

Parent: WI-354

Clue: CLUE-wang-endpoint-localization-cancellation

## Claim

Biao Wang's Theorem 2.2 is stated for
\[
0<\lambda<\theta<1,\qquad H=T^\theta,
\]
but the displayed proof admits an exact endpoint sharpening for every fixed real even
\[
g\in C_c^\infty(\mathbb R),
\qquad
\operatorname{supp}g\subset[-\theta,\theta].
\]

With \(L=\log T\) and \(I=(T,T+H]\), the same pair-correlation expression satisfies
\[
\sum_{\gamma,\gamma'\in I}
\widehat g\!\left(\frac{i(\rho-\rho')L}{2\pi}\right)
\frac{4}{4-(\rho-\rho')^2}
=
\frac{HL}{2\pi}
\left(
g(0)+\int_{\mathbb R}|\alpha|g(\alpha)\,d\alpha
\right)
+O_g(H).
\tag{1}
\]

Thus the strict support gap in the theorem statement is not forced at equality by Wang's zero-window localization term. The apparent endpoint obstruction comes from a later coarse step in the proof: the factor \(g(\alpha)\) is replaced by \(\|g\|_\infty\) before the error is integrated. For a fixed smooth compactly supported test, that replacement discards exactly the quadratic vanishing at the support boundary that is sufficient to absorb the \(xL^3\) error at \(x=H\).

This is an endpoint correction, not a support-crossing theorem. The present proof still does not yield a pair-correlation asymptotic for tests whose support genuinely extends past \(\theta\), and it does not exclude sparse off-critical zeros.

## 1. Source-level reconstruction

The primary source is Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1, 7 September 2026, https://arxiv.org/abs/2609.07918.

Wang writes
\[
A(x,t)=-D_x(t)+B_x(t)+E_x(t)
\tag{2}
\]
and proves the zero-window comparison
\[
2\pi F_I(x)
=
\int_I |A(x,t)|^2\,dt+O(xL^3).
\tag{3}
\]
The proof of this localization estimate uses the displayed pointwise bounds on \(A\), \(A_I\), and \(A-A_I\); no step there needs \(x=o(H)\). The global explicit-formula remainder used for \(E_x\) is stated in the range relevant here with \(x<T\), which is satisfied when \(x\le H=T^\theta<T\).

For the prime polynomial Wang invokes the Montgomery--Vaughan estimate
\[
\int_I |D_x(t)|^2\,dt
=
H\log x+O\!\left(H+x\log^2(2x)\right).
\tag{4}
\]
Inside the printed theorem the strict inequality \(\lambda<\theta\) is used to simplify this to the stronger uniform norm bound \(\|D_x\|_2\ll\sqrt{HL}\). At the endpoint that simplification is unavailable, but the unsimplified estimate is still enough. For \(1\le x\le H\),
\[
\|D_x\|_2^2\ll HL^2,
\qquad
\|D_x\|_2\ll \sqrt H\,L.
\tag{5}
\]
Since \(|E_x(t)|\ll 1/x\),
\[
\|E_x\|_2\ll \frac{\sqrt H}{x}
\]
and hence
\[
\left|\int_I D_x(t)\overline{E_x(t)}\,dt\right|
\le
\|D_x\|_2\|E_x\|_2
\ll
\frac{HL}{x}.
\tag{6}
\]

Keeping the other displayed estimates unchanged, the proof of Proposition 2.6 therefore reruns for \(1\le x\le H\) with the endpoint-safe bound
\[
F_I(x)
=
\frac{H}{2\pi}
\left(\frac{L^2}{x^2}+\log x\right)
+
O\!\left(
H+\frac{HL}{x^2}+\frac{HL}{x}
+xL^3+\frac{L}{\sqrt x}
\right).
\tag{7}
\]
The \(xL^2\) error from (4) is absorbed by \(xL^3\).

## 2. Smooth support flatness removes the endpoint loss

Wang's proof of Theorem 2.2 uses the exact identity obtained by integrating \(F_I(T^\alpha)\) against \(g(\alpha)\). The printed proof then estimates the error by first taking absolute values and replacing
\[
|g(\alpha)|\le \|g\|_\infty,
\]
which turns the localization term into the coarse bound
\[
L^3\int_0^\lambda T^\alpha\,d\alpha
\ll T^\lambda L^2.
\tag{8}
\]
At \(\lambda=\theta\), (8) is too large relative to the \(HL\) main scale.

For the actual fixed test, however, compact smooth support supplies additional information. Because \(g\) is smooth on \(\mathbb R\) and vanishes identically to the right of \(\theta\),
\[
g(\theta)=g'(\theta)=0.
\tag{9}
\]
Hence for \(0\le u\le\theta\),
\[
|g(\theta-u)|\le C_g u^2.
\tag{10}
\]
With \(x=T^\alpha\) and \(H=T^\theta\),
\[
\begin{aligned}
L^3\int_0^\theta |g(\alpha)|T^\alpha\,d\alpha
&=
HL^3\int_0^\theta |g(\theta-u)|e^{-Lu}\,du\\
&\le
C_gHL^3\int_0^\infty u^2e^{-Lu}\,du\\
&=
O_g(H).
\end{aligned}
\tag{11}
\]

Every other error in (7) is also \(O_g(H)\) after support integration:
\[
HL\int_0^\theta |g(\alpha)|e^{-L\alpha}\,d\alpha=O_g(H),
\tag{12}
\]
\[
HL\int_0^\theta |g(\alpha)|e^{-2L\alpha}\,d\alpha=O_g(H),
\tag{13}
\]
and
\[
L\int_0^\theta |g(\alpha)|e^{-L\alpha/2}\,d\alpha=O_g(1).
\tag{14}
\]
The main terms are treated exactly as in Wang. This proves (1).

The argument needs only a fixed \(C^2\) boundary flatness estimate for the critical term, although Wang's test class is \(C_c^\infty\).

## 3. What this correction does and does not change

The endpoint result changes the causal diagnosis of the support restriction. The \(O(xL^3)\) localization estimate is real, but it does not by itself force a strict gap once the fixed smooth test is retained through the final integral. Therefore improving zero-window localization is not necessary merely to reach \(\lambda=\theta\).

The support-crossing problem remains. If a test genuinely uses \(\alpha>\theta\), then \(x=T^\alpha>H\) on that part of the support. The source's displayed pointwise bounds contain both the localization term \(xL^3\) and the Montgomery--Vaughan error \(x\log^2(2x)\). The present absolute-value proof does not turn those contributions into \(o(HL)\) on a region of prime scales beyond the interval length. New cancellation, a different localization architecture, or stronger short-interval arithmetic is required to prove such an extension.

The exact interval scale also matters. Equation (1) is established here for \(H=T^\theta\). It does not automatically give endpoint support for every generalized \(H=T^{\theta+o(1)}\). If \(H\) is logarithmically shorter than \(T^\theta\), then \(x=T^\theta\) can exceed the actual interval length and the endpoint bookkeeping above no longer applies unchanged. Thus WI-226's safe strict-margin extension to logarithmically perturbed bow-scale intervals is not contradicted.

Finally, the endpoint sharpening does not improve Wang's limiting simple-zero proportion. Wang already obtains \(c(\theta)\) by taking \(\lambda\uparrow\theta\) after the asymptotic limit. Nor does (1) make a fixed-power normalized pair statistic sensitive to a finite or zero-density exceptional set.

## 4. Consequence for the local clues

The endpoint-localization clue is resolved in narrowed form. Its first target, reaching the boundary \(\lambda=\theta\), needs neither signed endpoint cancellation nor a new smoothing: retaining the fixed test's existing boundary flatness already closes it. The remaining mathematically live question is genuine support crossing \(\lambda>\theta\).

The coefficient-weighted prime-dephasing clue remains rejected as a standalone support-crossing mechanism, but its previous rationale must be corrected. Prime-side refinement is not needed to repair equality. Beyond the endpoint, improving only \(D_x\) still leaves the independent \(xL^3\) localization majorant unchanged, so it cannot by itself prove a support-crossing theorem.

## 5. Prior art and novelty audit

Theorem 2.2, Lemma 2.4, Proposition 2.6, the decomposition (2), and the Montgomery--Vaughan estimate (4) are source inputs from Wang's preprint and its cited unconditional pair-correlation framework. No novelty is claimed for those ingredients.

The Mathia contribution is the proof-surface correction: preserve the test weight through the error integration, use the smooth support endpoint conditions (9), and avoid the \(\|D_x\|_2\ll\sqrt{HL}\) simplification when \(x=H\). Together these give the endpoint formula (1).

A targeted search through 28 September 2026 for arXiv:2609.07918 together with endpoint, \(\lambda=\theta\), and equivalent support-bound language found Wang's v1 and secondary mirrors/summaries, but no independent source explicitly stating this endpoint sharpening. The preprint itself remains at v1 in the search surface. Absence of a hit is not evidence of priority, so this finding makes no literature-priority claim.

## 6. Falsification and boundary checks

This finding should be withdrawn or narrowed if a direct source check shows any hidden use of \(x=o(H)\) in Lemma 2.4, an additional term in the Montgomery--Vaughan estimate that is not controlled for \(x=H\), a stronger restriction than \(x<T\) in the bound for \(E_x\), or a step in Theorem 2.2 that removes the factor \(g(\alpha)\) before the critical error for a reason other than convenience.

The fixed-test quantifier is essential. A \(T\)-dependent family whose derivative norms grow with \(T\) is not covered by the \(O_g(H)\) argument. Nor is a nonsmooth hard cutoff.

No conclusion is claimed for support genuinely beyond \(\theta\), for microscopic intervals, or for arbitrary logarithmically perturbed interval lengths at the endpoint.

## Research consequence

The exact support boundary in Wang's displayed proof is sharper than the printed coarse error suggests. For \(H=T^\theta\), fixed smooth tests can touch \(\theta\) with a relative error \(O_g(1/L)\).

The next useful question is therefore not how to recover the endpoint. It is how to cross it, or how to replace normalized pair-correlation information by a source-independent individual-defect/cofinal coercive mechanism.