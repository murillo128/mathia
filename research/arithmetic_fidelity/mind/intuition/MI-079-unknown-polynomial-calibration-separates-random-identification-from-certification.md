# MI-079 — Unknown polynomial calibration separates random identification from finite certification

**Evidence level:** supported synthesis of the exact oracle-model results in [AF-577](../../findings/AF-577-unknown-polynomial-calibration-separates-continuous-randomness-from-finite-certification.md). Interpolation and randomized identity testing are classical; this is no new recovery theorem.

Let known real-analytic curves \(F_1,\ldots,F_m\), \(m\ge2\), on \(I=(0,A)\) extend continuously to \([0,A]\). Observe \(y=F_i+b\), where one fixed polynomial \(b\) has finite but unknown, unbounded degree and no coefficient bound. Write \(\Pi\) for all polynomials. Then
\[
F_i-F_j\notin\Pi\quad(i\ne j)
\]
is exactly the full-curve identification condition. It gives **no finite deterministic certificate at any input**: for every finite transcript at distinct nodes \(t_1,\ldots,t_k\) and every other label \(j\), a polynomial interpolates \(y(t_\ell)-F_j(t_\ell)\). The resulting alternative input follows the same adaptive transcript and stopping decision.

Nevertheless, draw one ideal continuously distributed coordinate \(V\) in an interior interval, independently of the input. At deterministic distinct nodes \(t_0,t_1,\ldots\), fit the degree-at-most-\(r\) interpolants
\[
P_{j,r}(t_\ell)=y(t_\ell)-F_j(t_\ell),\qquad 0\le\ell\le r.
\]
Return the unique label satisfying \(y(V)-F_j(V)=P_{j,r}(V)\), when there is one. The validation coordinate and value never enter the fits. For a fixed input, every false-label residual is nonzero analytic; all such residuals over all stages have a null union of zero sets. When \(r=\deg b=d\), the true residual vanishes identically. Thus the procedure is almost surely correct on each fixed input and stops within \(d+2\) queries, counting the single validation query; take \(d=0\) for \(b=0\).

The quantifiers carry the effect:
\[
\forall x\quad\mathbb P_V(\text{correct finite termination on }x)=1,
\]
without a common probability-one set working for every \(x\). Fixing \(V\) first restores the interpolation adversary. Reusing \(V\) is valid only because the entire sequence of possible interpolants is independent of it.

This advantage requires an exact continuous coordinate and exact equality tests. If a terminating execution reads finitely many fair coin bits, some terminating correct finite bit word has positive probability. Interpolate a false-label input on that word's finite transcript. Every coin stream extending the word then makes the same incorrect decision on that fixed input, contradicting zero error. Arbitrarily many input-dependent bits do not remove this obstruction when every terminating execution uses finitely many. Nonzero-error Monte Carlo recovery is not excluded.

The same class has zero uniform noise radius, even with the full curve: polynomial density in \(C[0,A]\) gives, for every \(\varepsilon>0\), a \(p\in\Pi\) with
\[
\|(F_j-F_i)-p\|_\infty<2\varepsilon.
\]
The two admitted observations \(F_i\) and \(F_j-p\) can then be equalized by opposite errors of size at most \(\varepsilon\). Disjoint exact source classes have intersecting uniform closures.

For the prime-edit controls in AF-577, \(\Phi_p=(P-h_p)^{-1}\circ E_1\), with \(P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s}\), \(h_p(s)=p^{-s}-(p+1)^{-s}\), and \(E_1(a)=\int_a^\infty e^{-v}dv/v\). For odd primes \(p<q\), their gap is positive and analytic on \(a>0\), and
\[
0<\Phi_q(a)-\Phi_p(a)\le(2/p)^{\Phi_q(a)}/\log2\longrightarrow0
\quad(a\to\infty).
\]
A polynomial gap on any observation interval would extend to the whole ray and have to be zero, a contradiction. This verifies the separation premise without a far-out-prime or shrinking-window limit. These are generalized-prime matched controls, not an ordinary-prime discriminator.

The nuisance class is decisive. A known degree bound permits ordinary finite deterministic tests; allowing arbitrary analytic nuisances permits exact source-gap aliases. The smooth, strictly derivative-bounded class of [AF-575](../../findings/AF-575-unknown-calibration-slack-requires-unbounded-sampling-depth.md) instead admits deterministic finite stopping at each input, while [AF-576](../../findings/AF-576-randomized-calibration-recovery-has-a-sharp-error-stopping-tail.md) rules out uniform probabilistic query bounds there. Neither conclusion can be imported merely from the words “unknown calibration.”
