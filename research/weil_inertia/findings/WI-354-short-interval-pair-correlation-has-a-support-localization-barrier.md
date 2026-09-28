# WI-354 — short-interval pair correlation has a support-localization barrier

**Status:** LITERATURE+DERIVED + RECENT-PREPRINT-AUDITED + PRIOR-ART-REDIRECT + DECISIVE-NEGATIVE + NON-RH + CORRECTED-ENDPOINT

## Claim

Biao Wang's September 2026 short-interval extension of the unconditional Montgomery/Lamzouri argument gives a useful new localization theorem, but it does not turn a positive-proportion result into exclusion of sparse or finite off-critical defects.

For an exact power interval
\[
I=(T,T+H],\qquad H=T^\theta,\qquad 0<\theta<1,\qquad L=\log T,
\]
Wang's Theorem 2.2 is stated for every fixed \(0<\lambda<\theta\) and fixed real even \(g\in C_c^\infty(\mathbb R)\) supported in \([-\lambda,\lambda]\):
\[
\sum_{\gamma,\gamma'\in I}
\widehat g\!\left(\frac{i(\rho-\rho')L}{2\pi}\right)
\frac{4}{4-(\rho-\rho')^2}
=
\frac{HL}{2\pi}
\left(g(0)+\int_{\mathbb R}|\alpha|g(\alpha)\,d\alpha\right)
+O_g(H+T^\lambda L^2).
\tag{1}
\]

The paper's displayed error, divided by the \(HL\) main scale, is
\[
O_g\!\left(\frac1L+T^{\lambda-\theta}L\right),
\tag{2}
\]
so the theorem as printed uses the strict margin \(\lambda<\theta\).

That printed margin is not the sharp boundary of the displayed proof for a fixed smooth test. The proof audit in WI-440 shows that, when \(H=T^\theta\) exactly and \(g\) is fixed with
\[
\operatorname{supp}g\subset[-\theta,\theta],
\]
the same argument can be rerun at \(x\le H\) and the support-integrated error is \(O_g(H)\). Hence the fixed-test pair formula reaches the endpoint
\[
\boxed{\lambda=\theta}
\tag{3}
\]
without any new zeta estimate. The previously stored inference that the localization term by itself forces a strict fixed gap was too strong: it came from replacing \(g\) by \(\|g\|_\infty\) before integrating the endpoint-sensitive error.

The substantive barrier survives in the form actually relevant to an RH bootstrap. The current proof does not supply support genuinely past the interval exponent, and the optimized zero-side coefficient weakens as the interval shortens. Wang obtains
\[
\boxed{
\liminf_{T\to\infty}
\frac{N_0^s(T,T^\theta)}{N(T,T^\theta)}
\ge
c(\theta)
:=2-\frac\theta2-
\frac1{\sqrt2}\cot\!\left(\frac\theta{\sqrt2}\right).
}
\tag{4}
\]
It is strictly increasing,
\[
c'(\theta)=\frac12\cot^2(\theta/\sqrt2)>0,
\tag{5}
\]
with unique zero
\[
\theta_0=0.550193964744154\ldots,
\tag{6}
\]
and
\[
c(1)=
\frac32-\frac1{\sqrt2}\cot(1/\sqrt2)
=0.672500703679\ldots.
\tag{7}
\]
Thus every fixed \(\theta<1\) gives \(c(\theta)<c(1)<1\). Localizing this same proportion mechanism makes the certified fraction weaker, not stronger.

For fixed \(\theta>0\),
\[
N(T,T^\theta)=\frac{T^\theta L}{2\pi}+O(T^\theta+L),
\tag{8}
\]
so (4) remains compatible with \(\asymp T^\theta L\) uncertified zeros in each interval and, a fortiori, with any finite or zero-density off-critical set. The theorem therefore does not provide the defect-to-zero bootstrap required by the Weil-inertia mandate.

## 1. Exact recent theorem and provenance

The primary source is Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1, submitted 7 September 2026, https://arxiv.org/abs/2609.07918.

This is a recent unrefereed preprint. The claims here distinguish the theorem as stated from the endpoint sharpening derived from its displayed proof.

Wang fixes
\[
0<\lambda<\theta<1,\qquad H=T^\theta,
\tag{9}
\]
and proves (1) as Theorem 2.2. Proposition 2.6 gives, uniformly on the stated range,
\[
\mathcal F_I(x)=
\frac{H}{2\pi}
\left(\frac{L^2}{x^2}+\log x\right)
+O\!\left(
H+\frac{HL}{x^2}+\frac{H\sqrt L}{x}
+xL^3+\frac{L}{\sqrt x}
\right).
\tag{10}
\]

The localization lemma contributing the \(xL^3\) term and the Montgomery--Vaughan mean-square estimate used in Proposition 2.6 remain meaningful at \(x\le H\). WI-440 reruns these estimates at the endpoint rather than substituting \(\lambda=\theta\) into the already-coarsened bound (1). Two facts matter.

First, the Montgomery--Vaughan estimate printed in the proof gives, for \(x\le H\),
\[
\|D_x\|_2^2\ll H\log x+H+x\log^2(2x)\ll HL^2,
\tag{11}
\]
so the cross term with \(E_x\) is \(O(HL/x)\), which is still support-integrable to \(O_g(H)\).

Second, the exact proof of Theorem 2.2 integrates the pointwise error against \(g(\alpha)\) with \(x=T^\alpha\). Since a fixed \(C_c^\infty\) function supported in \([-\theta,\theta]\) satisfies
\[
g(\theta)=g'(\theta)=0,
\tag{12}
\]
Taylor's theorem gives \(|g(\theta-u)|\ll_g u^2\). Therefore the apparently critical localization contribution satisfies
\[
L^3\int_0^\theta |g(\alpha)|T^\alpha\,d\alpha
=
HL^3\int_0^\theta |g(\theta-u)|e^{-Lu}\,du
\ll_g
HL^3\int_0^\infty u^2e^{-Lu}\,du
\ll_g H.
\tag{13}
\]
The source obtains \(T^\lambda L^2\) by first replacing \(|g(\alpha)|\) with \(\|g\|_\infty\). That simplification is harmless for fixed \(\lambda<\theta\), but it loses exactly the endpoint flatness needed at \(\lambda=\theta\).

Wang then applies Lamzouri's finite-multiset inequality. For \(f=\eta^2\) supported in \([-\lambda/2,\lambda/2]\), the cost is
\[
C(f)=\int f(u)^2\,du+
\iint |u-v|f(u)f(v)\,du\,dv,
\tag{14}
\]
whose unique minimizer is
\[
f_\lambda(u)=
\frac{\cos(\sqrt2 u)}
{\sqrt2\sin(\lambda/\sqrt2)}
\mathbf 1_{[-\lambda/2,\lambda/2]}(u),
\tag{15}
\]
with
\[
C_\lambda=
\frac\lambda2+
\frac1{\sqrt2}\cot(\lambda/\sqrt2).
\tag{16}
\]
Thus the endpoint sharpening changes the analytic support bookkeeping, not the limiting coefficient (4), which Wang already obtains by letting \(\lambda\uparrow\theta\).

## 2. The genuine support-localization barrier starts beyond the endpoint

The corrected lesson is not that the current proof intrinsically requires \(\lambda<\theta\). It is that the source's pointwise arithmetic/localization estimates are naturally controlled up to the interval scale \(x\le H\), and the smooth test removes the logarithmic endpoint loss when \(x\) reaches \(H\).

For support genuinely extending to an exponent \(\sigma>\theta\), the proof would have to control prime/localization scales \(x=T^\alpha>H\) on part of the support. The displayed Montgomery--Vaughan error \(x\log^2(2x)\) and the localization error \(xL^3\) then sit above the interval scale. The existing absolute-value argument supplies no \(o(HL)\) theorem in that regime. Endpoint flatness removes powers of \(L\) at \(\alpha=\theta\); it does not by itself provide the new cancellation needed on a whole region \(\alpha>\theta\).

This is a proof-interface statement, not a lower bound proving that support past \(\theta\) is impossible. A reorganized signed argument, smoother height localization, coupled zero/prime treatment before squaring, or stronger short-interval arithmetic could cross the boundary.

The distinction also matters for generalized interval lengths. WI-440 establishes the endpoint for the exact scale \(H=T^\theta\). It does not automatically upgrade the separate WI-226 extension to every \(H=T^{\theta+o(1)}\): a logarithmically shorter interval may have \(T^\theta/H\to\infty\), so the endpoint \(x=T^\theta\) can again lie beyond the actual interval length. The strict fixed support margin used in that generalized extension remains a valid safe regime.

## 3. Localization still cannot bootstrap the proportion to zero defect

The naive bootstrap fails independently of the corrected endpoint.

First, the optimized coefficient moves in the wrong direction:
\[
0<\theta_1<\theta_2\le1
\quad\Longrightarrow\quad
c(\theta_1)<c(\theta_2).
\tag{17}
\]
Shorter fixed-power intervals therefore leave a larger uncertified fraction.

Second, every fixed positive power interval contains \(\asymp T^\theta L\) zeros. A fixed number of off-critical zeros contributes only
\[
O(1)/(T^\theta L)=o(1)
\tag{18}
\]
to a normalized statistic. Reaching the exact support endpoint does not change this information-theoretic mismatch. To exclude an isolated exception through localization alone one would need a coefficient tending to one fast enough, a genuinely microscopic theorem, or a separate non-normalized coercive mechanism that forces an individual defect to remain visible.

This preserves the canonical distinction between density information and RH: a proportion theorem, even a very strong one, does not exclude a finite or zero-density off-line divisor unless some additional mechanism turns sparse defects into a uniform obstruction.

## 4. Relation to the current Weil-inertia frontier

The endpoint correction sharpens rather than reverses the broader negative result. Vertical localization of the existing Montgomery/Lamzouri proportion mechanism still does not produce sparse-defect exclusion.

The corrected interface is now precise:

\[
\text{fixed smooth support up to }\theta
\quad\text{is reachable at }H=T^\theta,
\tag{19}
\]
while
\[
\text{support genuinely beyond }\theta
\quad\text{is not supplied by the current proof.}
\tag{20}
\]

WI-440 contains the source-level derivation. The local clue about endpoint localization is therefore resolved in narrowed form: no new localization mechanism is needed merely to touch the endpoint, but a support-crossing mechanism remains open.

The coefficient-weighted dephasing clue remains rejected as a standalone support-crossing repair. Improving only the prime-polynomial mean square cannot by itself remove an unchanged \(xL^3\) localization majorant on scales \(x>H\), although such prime-side information could matter inside a proof that reorganizes localization simultaneously.

None of this weakens the cofinal Bombieri-inertia direction or another non-normalized individual-defect mechanism. Those approaches need not infer RH from a local positive proportion.

## 5. Prior art and novelty boundary

The short-interval theorem, the displayed explicit-formula estimates, the finite-multiset inequality, and the variational optimizer are Wang/Lamzouri/Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh inputs. No novelty is claimed for them.

The durable Mathia correction is the endpoint audit: the coarse \(O_g(H+T^\lambda L^2)\) statement is not sharp enough to decide \(\lambda=\theta\), because the proof discards the fixed test's vanishing at the support boundary. Retaining that vanishing and using the unsimplified Montgomery--Vaughan estimate closes the exact endpoint with \(O_g(H)\).

A targeted literature search through 28 September 2026 found Wang's v1 and secondary mirrors/summaries, but no independent source explicitly recording this endpoint sharpening. That absence is not evidence of priority, and no literature-priority claim is made.

## 6. Boundary conditions and falsification

The correction should be withdrawn or narrowed if any of the following fails on a direct source audit: the localization lemma ceases to hold when \(x\) reaches \(H\); the printed Montgomery--Vaughan estimate has an additional term requiring \(x=o(H)\); the \(E_x\) bound used in the cross term requires more than \(x<T\); or the exact Theorem 2.2 integral does not retain the factor \(g(\alpha)\) on the critical \(xL^3\) contribution.

The claim also depends on \(g\) being a fixed smooth compactly supported test. A \(T\)-dependent family with uncontrolled derivative norms is not covered, and the endpoint conclusion is not asserted for an arbitrary hard cutoff.

Finally, this finding does not establish a theorem for support \(\sigma>\theta\), for microscopic intervals, or for arbitrary \(H=T^{\theta+o(1)}\) at the endpoint. Those remain genuinely stronger problems.

## Research consequence

The short-interval theorem remains useful evidence but not the missing RH bootstrap. The correct proof-surface diagnosis is:

\[
\text{published strict margin}
\;\longrightarrow\;
\text{fixed smooth endpoint is actually reachable}
\;\longrightarrow\;
\text{support crossing and sparse-defect exclusion remain open}.
\]

Future work should not spend effort trying to repair an artificial logarithmic loss at \(\lambda=\theta\). The relevant analytic target is now support or defect information that genuinely crosses the interval-scale barrier, or an individual/cofinal coercive observable that avoids normalization by the local zero count.