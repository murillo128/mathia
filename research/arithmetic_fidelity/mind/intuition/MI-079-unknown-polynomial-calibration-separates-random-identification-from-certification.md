# MI-079 — Unknown polynomial calibration separates random identification from finite certification

**Evidence level:** supported synthesis of the exact oracle-model results in [AF-577](../../findings/AF-577-unknown-polynomial-calibration-separates-continuous-randomness-from-finite-certification.md), [AF-578](../../findings/AF-578-continuous-randomness-retains-fixed-budget-polynomial-calibration-obstruction.md), and [AF-579](../../findings/AF-579-unbounded-query-locations-preserve-polynomial-budget-obstruction.md). Interpolation, randomized identity testing and Gaussian-prior testing bounds are classical; this is no new recovery theorem.

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

This advantage requires an exact continuous coordinate and exact equality tests. For fair-coin policies whose label-returning executions use finitely many bits and queries, AF-577 proves the sharper bound
\[
e(\mathcal A):=\sup_x\Pr_x(T<\infty,\widehat i\ne i)
\ \ge\ \frac{m-1}{m}\Pr_y(T<\infty)
\quad\text{for every fixed input }y.
\]
Here \(T\) is the label-return time; abstention or nonreturn contributes no error. To see why the bound concerns one fixed adversary rather than a seed-dependent choice, take any finite set \(W\) of returning prefix-free coin words on \(y\). Interpolate **one polynomial for each label** on the union of all their queried coordinates. Repeated coordinates are consistent because every transcript comes from the same \(y\). Each resulting input reproduces every execution in \(W\), including adaptive choices. If \(q_W\) is their total probability and \(q_{j,W}\) the mass returning label \(j\), some matched label incurs error at least
\[
\max_j(q_W-q_{j,W})\ge(1-1/m)q_W.
\]
Exhausting the countable returning words proves the bound. The competing input may change with the finite set \(W\), but never with the realized seed.

Consequently almost-sure return on every input has exact minimax error \(1-1/m\), attained by blind uniform guessing. No uniform cap or finite expected cost is needed; unrestricted input-dependent finite bits and queries cannot lower this worst-case error. Returning a uniform label with probability \(\gamma\) gives equality \(e=\gamma(1-1/m)\), with finite-bit sampling for rational \(\gamma\). This is a uniform guarantee over unbounded polynomial degree, not an exclusion of degree-dependent success bounds. The continuous-coordinate procedure has no positive-mass finite-bit cylinders and lies outside this argument.

Its **fixed-cap** boundary is nevertheless just as sharp, under the additional smoothness in AF-578. Rescale the bounded window to \([0,1]\). If every source is \(C^{N-1}[0,1]\), then even continuously randomized adaptive policies capped at \(N\) values have minimax error
\[
R_N=c_m:=1-1/m,
\]
already for nuisances of degree at most \(N-1\) with unrestricted coefficients. The uniformity over arbitrarily close nodes comes from lifting the smooth source gap \(g\), rather than arbitrary sampled data. At \(r\le N\) distinct nodes, the degree-at-most-\(r-1\) interpolant of \(g\) has monomial coefficient vector \(c\), padded to length \(N\), satisfying
\[
\|c\|_2\le B_N(g):=\sum_{k=0}^{N-1}\frac{2^k}{k!}\|g^{(k)}\|_\infty.
\]
For one fixed Gaussian coefficient vector \(\beta\sim N(0,L^2I_N)\), successive normalized innovations \(u_j\) of the evaluation vectors are orthonormal. The conditional mean-shift energy obeys \(\sum_j|u_j^Tc|^2\le B_N(g)^2\), hence the complete adaptive transcript laws satisfy
\[
\operatorname{TV}(P_i^L,P_j^L)\le B_N(F_i-F_j)/(2L).
\]
Sending \(L\to\infty\) hides every label in a prior over fixed admissible polynomials, independently of the realized seed. Ill-conditioning of arbitrary Vandermonde inversion does not defeat this smooth-gap bound. This is calibration uncertainty, not measurement noise.

For sources smooth on the closed window, write \(q_N=\sup_x\Pr_x(T>N)\). Truncation and uniform guessing give
\[
e+c_m q_N\ge c_m\qquad\text{for every finite }N.
\]
If the sources also have the analytic nonpolynomial gaps above, this is sharp for per-input almost-surely returning continuous-random policies: mix the exact procedure with immediate guessing. Zero error has \(q_N=1\) for every cap despite finite stopping on each fixed input; any \(e<c_m\) forces \(\sup_x\mathbb E_xT=\infty\), not a single nonterminating input. With a **known** degree bound \(d\) and sources in \(C^d[0,1]\), \(d+1\) queries still have minimax error \(c_m\), whereas \(d+2\) suffice almost surely through independent continuous validation. This bounded-window proof uses the derivative bounds and unrestricted nuisance coefficients; AF-579 transports it to a ray under the separate endpoint condition below.

The bounded-window class has zero uniform noise radius, even with the full curve: polynomial density in \(C[0,A]\) gives, for every \(\varepsilon>0\), a \(p\in\Pi\) with
\[
\|(F_j-F_i)-p\|_\infty<2\varepsilon.
\]
The two admitted observations \(F_i\) and \(F_j-p\) can then be equalized by opposite errors of size at most \(\varepsilon\). Disjoint exact source classes have intersecting uniform closures.

For the prime-edit controls in AF-577, \(\Phi_p=(P-h_p)^{-1}\circ E_1\), with \(P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s}\), \(h_p(s)=p^{-s}-(p+1)^{-s}\), and \(E_1(a)=\int_a^\infty e^{-v}dv/v\). For odd primes \(p<q\), their gap is positive and analytic on \(a>0\), and
\[
0<\Phi_q(a)-\Phi_p(a)\le(2/p)^{\Phi_q(a)}/\log2\longrightarrow0
\quad(a\to\infty).
\]
A polynomial gap on any observation interval would extend to the whole ray and have to be zero, a contradiction. AF-578 also supplies the analytic extension across \(a=0\), so the fixed-order derivative bounds hold on bounded windows including that endpoint. This verifies the separation and smoothness premises without a far-out-prime or shrinking-window limit. These are generalized-prime matched controls, not an ordinary-prime discriminator.

On the **whole ray** \(a>0\), AF-579 separates full-curve robustness from the finite-cap obstruction. For cap \(N\), put \(n=N-1\) and
\[
x=\frac a{1+a},\qquad
z(x)=(1-x)^n\{y(a)-F_1(a)\},\qquad
H_i(x)=(1-x)^n(F_i-F_1)\!\left(\frac{x}{1-x}\right).
\]
If every \(H_i\in C^n[0,1]\), this invertibly recodes each finite exact query into the bounded-window theorem, because
\[
a^k\longmapsto x^k(1-x)^{n-k},\quad 0\le k\le n,
\]
is a bijection of \(\Pi_n\). It proves \(R_N^{\rm ray}=c_m\) already on that degree-restricted subclass. The map depends on the cap; it does not turn all unknown degrees into one fixed finite-dimensional class. No value at infinity is queried. For the prime-edit gaps, AF-579 proves analytic extension at zero and, for every fixed \(j\ge0\),
\[
|\partial_a^j(\Phi_q-\Phi_p)(a)|\le C_{p,q,j}e^{-c_pa},\qquad
c_p=\log(p/2)/\log2>0
\]
for sufficiently large \(a\). These bounds make the compactified gap flat at \(x=1\), validating every finite cap. Bounded gaps alone would not establish that smoothness.

Yet for every bounded real gap \(g\) on the ray,
\[
\inf_{b\in\Pi}\|g-b\|_\infty
=\inf_{c\in\mathbb R}\|g-c\|_\infty
=\tfrac12(\sup g-\inf g),
\]
since nonconstant polynomials are unbounded. The ordered prime-edit gaps are positive and vanish at both ends. For fixed \(S=\{p_1<\cdots<p_m\}\), set
\(d(S)=\min_{i<m}\sup_{a>0}(\Phi_{p_{i+1}}-\Phi_{p_i})(a)>0\).
The supremal full-ray identification radius under arbitrary uniform error is \(d(S)/4\): uniqueness holds strictly below it, and a midpoint alias occurs at equality. Nonadjacent gaps are sums of positive adjacent gaps, so no smaller pair distance is omitted. Thus a positive full-curve margin coexists with \(R_N^{\rm ray}=c_m\) at every finite cap and the same sharp noiseless stopping law. The elementary pair \(0,a/(1+a)^2\) has radius \(1/16\) and capped error \(1/2\); this separation is not prime-specific. The exact response rescaling changes the noise geometry, so the full-ray radius is proved separately, not transported through compactification.

The nuisance class is decisive. A known degree bound permits ordinary finite deterministic tests; allowing arbitrary analytic nuisances permits exact source-gap aliases. The smooth, strictly derivative-bounded class of [AF-575](../../findings/AF-575-unknown-calibration-slack-requires-unbounded-sampling-depth.md) instead admits deterministic finite stopping at each input, while [AF-576](../../findings/AF-576-randomized-calibration-recovery-has-a-sharp-error-stopping-tail.md) rules out uniform probabilistic query bounds there. Neither conclusion can be imported merely from the words “unknown calibration.” No noisy variable-stopping theorem follows from the positive full-ray margin.
