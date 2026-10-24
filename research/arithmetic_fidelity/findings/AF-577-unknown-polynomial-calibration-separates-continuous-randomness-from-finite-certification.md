# AF-577 — Unknown polynomial calibration separates continuous randomness from finite certification

## Status and question

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · ORACLE-MODEL-BOUNDARY · MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

[[research/arithmetic_fidelity/findings/AF-571-polynomial-drift-has-exact-small-window-probe-saturation|AF-571]] assumes a known polynomial calibration degree. AF-575/576 instead bound a derivative but leave its strict slack unknown. Neither addresses calibration that is a polynomial of some finite, **unknown and unbounded** degree, with no derivative or coefficient bound.

In this different class, full curves identify the source exactly but no universally correct deterministic procedure can stop on any finite value transcript. Nevertheless, a continuously randomized exact-real oracle procedure identifies every fixed input almost surely, after at most the actual calibration degree plus two queries. The advantage disappears if a terminating computation must use only finitely many random bits: among policies that return a label almost surely on every input, the exact worst-case minimax error is the blind-guess value \(1-1/m\). This remains true without any uniform or expected bound on the bits or queries used. Every positive uniform noise margin also disappears.

The result locates an observation-model boundary, not a numerical recovery method. Its interpolation and identity-testing mechanism is classical.

## Experiment and separation criterion

Let \(I=(0,A)\), with \(0<A<\infty\), and let \(F_1,\ldots,F_m\), \(m\ge2\), be known real-analytic functions on \(I\), continuous on \([0,A]\). Let \(\Pi_r\) denote the real polynomials of degree at most \(r\), and set
\[
 \Pi=\bigcup_{r\ge0}\Pi_r,\qquad
 y=F_i+b,\quad i\in\{1,\ldots,m\},\quad b\in\Pi.
\tag{1}
\]
One fixed polynomial is shared by all queries of an input. Competing sources may have different polynomials. The only unknowns are the label and calibration; exact source evaluations and exact real comparisons are available. Only observations of \(y\), not arithmetic or source-evaluation work, are counted.

The necessary and sufficient condition for exact full-curve identification is
\[
 F_i-F_j\notin\Pi\quad\text{on }I\qquad(i\ne j).
\tag{2}
\]
Indeed, equality \(F_i+b_i=F_j+b_j\) would make the source gap polynomial; conversely a polynomial gap supplies an exact full-curve alias. Assume (2) below.

The following statements concern the same class (1).

1. A deterministic policy that never returns a wrong label on any admitted input cannot stop after finitely many queries on **any** input.
2. With one continuously distributed random validation coordinate, there is a policy correct with probability one on every fixed input. If \(b\) has degree \(d\), with \(d=0\) also used for the zero polynomial, it stops after at most \(d+2\) queries, almost surely. The degree is not supplied.
3. If all randomness comes from fair independent coin bits, and each label-returning execution reads finitely many bits and makes finitely many queries, worst-case error \(e\) forces the probability of returning any label on **each** input to be at most \(\min\{1,me/(m-1)\}\). Consequently the exact minimax error among policies returning almost surely on every input is \(1-1/m\). Zero error permits no positive probability of a finite label return on any input.
4. Under arbitrary additive observation error \(\|\eta\|_\infty\le\varepsilon\), the uniform full-curve identification radius is zero.

The finite-bit minimax statement also holds under a fixed query budget, since the matching blind-guess policy needs no queries. No sharp fixed-budget minimax error for **continuous-real randomness**, or optimal degree-dependent query count, is asserted. This is a separate interpolation argument; it does not extend [[research/arithmetic_fidelity/findings/AF-576-randomized-calibration-recovery-has-a-sharp-error-stopping-tail|AF-576]]'s smooth-nuisance coupling to polynomial nuisances.

## Every finite deterministic transcript has another label

Suppose a policy stops on an admitted input \(y=F_i+b\). Write \(t_1,\ldots,t_k\) for its distinct queried coordinates. For any \(j\ne i\), ordinary Lagrange interpolation gives a polynomial \(c\) satisfying
\[
 c(t_\ell)=y(t_\ell)-F_j(t_\ell),\qquad 1\le\ell\le k.
\tag{3}
\]
The other admitted input \(F_j+c\) produces the same finite transcript. Induction over adaptive queries proves equality of every response, next coordinate, and stopping/output decision. Hence the policy cannot be correct on both inputs. Repeated queries add no constraints; a zero-query stop is equally ambiguous.

Unlike [[research/arithmetic_fidelity/findings/AF-575-unknown-calibration-slack-requires-unbounded-sampling-depth|AF-575]]'s midpoint construction, this argument applies at **every actual input**, not only along an excluded limiting transcript. No derivative constraint must be preserved, so ordinary polynomial interpolation suffices. Imposing a known degree bound would invalidate this arbitrary-finite-transcript extension.

## One random validation value supports all degree tests

Fix distinct deterministic interpolation nodes \(t_0,t_1,\ldots\in I\). Draw \(V\) uniformly from a fixed nonempty subinterval whose closure is inside \(I\), independently of the unknown input, and query \(y(V)\) once. This is an ideal continuously distributed exact real coordinate, not a finite-bit sample.

At stage \(r=0,1,\ldots\), query the next node \(t_r\). For each label \(j\), let \(P_{j,r}\in\Pi_r\) interpolate
\[
 P_{j,r}(t_\ell)=y(t_\ell)-F_j(t_\ell),\qquad 0\le\ell\le r.
\tag{4}
\]
If exactly one label satisfies
\[
 y(V)-F_j(V)=P_{j,r}(V),
\tag{5}
\]
stop and return it; otherwise continue. In particular, the validation value and coordinate are never used to fit the interpolants.

Fix an input \(y=F_i+b\). For every wrong label \(j\ne i\) and every \(r\),
\[
 R_{j,r}(a)=F_i(a)-F_j(a)+b(a)-P_{j,r}(a)
\tag{6}
\]
is analytic and not identically zero, by (2). Its zeros in \(I\) are discrete, hence countable and Lebesgue null. For the true label, \(R_{i,r}=b-P_{i,r}\) is either identically zero or a nonzero polynomial with finitely many roots.

All the functions in (6) are determined by the fixed input and deterministic node sequence, independently of \(V\). The union of their nontrivial zero sets over the finitely many labels and countably many stages is null. Thus, with probability one, (5) never accepts a wrong label or a nonidentical true-label interpolant. At \(r=d\), polynomial interpolation gives \(P_{i,d}=b\) identically. The policy then accepts exactly the true label, having used one validation query and \(d+1\) interpolation queries.

This proves correctness and finite termination separately for **each fixed input**. There need not be one probability-one set of validation coordinates that works for all inputs simultaneously. For each fixed coordinate, the interpolation adversary (3) still produces a bad input. This quantifier difference resolves the apparent conflict with deterministic impossibility.

Reusing one validation point is legitimate because the entire hypothetical sequence of interpolants is independent of that point; response-dependent interpolation nodes or incorporating the validation value into fitting would require another argument. For fixed input, the stopping events are measurable analytic-equality sets.

## Finite-bit return probability has a sharp error bound

For a coin-based policy \(\mathcal A\), let \(T\) be the time of its single label return, with \(T=\infty\) if it never returns a label. An explicit abstention, if allowed, is also a nonreturn for this definition. Define the **unconditional** worst-case error
\[
 e(\mathcal A)=\sup_{\substack{1\le i\le m\\ b\in\Pi}}
 \Pr_{F_i+b}\{T<\infty,\ \widehat i\ne i\}.
\]
Then every admitted fixed input \(y\) satisfies
\[
 e(\mathcal A)\ \ge\ \frac{m-1}{m}\Pr_y\{T<\infty\}.
\tag{6a}
\]
No moment bound or common finite cap on the random-bit count, query count, or stopping time is assumed. Only a returning execution must read finitely many bits and make finitely many value queries. All other operations may still use exact reals.

**Finite collections of returning executions can be matched simultaneously.** Fix \(y=F_i+b\). Its returning executions are a countable disjoint union of coin cylinders \(C_w\) indexed by the finite words read at return. The words are prefix-free: once the policy returns, later unread bits cannot change that execution. Each cylinder fixes one finite oracle transcript and one returned label \(\ell_w\).

Take any finite subset \(W\) of these words, and let \(D_W\subset I\) be the finite union of **all** coordinates queried on their executions. Values at repeated coordinates are consistent because they all come from the same fixed function \(y\). For each label \(j\), choose one polynomial \(c_{j,W}\) interpolating
\[
 c_{j,W}(t)=y(t)-F_j(t)\qquad(t\in D_W).
\tag{6b}
\]
It has degree at most \(|D_W|-1\) when \(D_W\ne\varnothing\); take zero when there are no queries. On the single competing input \(y_{j,W}=F_j+c_{j,W}\), every seed in every cylinder of \(W\) follows the original execution and returns \(\ell_w\). This follows by induction through coin reads, adaptive queries, responses, and the return decision. The polynomial depends on the policy, the reference input, and the **finite set** of words, but not on the subsequently realized random seed. Matching separate inputs for separate seeds would not prove the bound.

Write
\[
 q_W=\sum_{w\in W}2^{-|w|},\qquad
 q_{j,W}=\sum_{w\in W:\,\ell_w=j}2^{-|w|}.
\]
For every \(j\), the fixed input \(y_{j,W}\) has error at least \(q_W-q_{j,W}\). Since \(\sum_j q_{j,W}=q_W\),
\[
 e(\mathcal A)\ge\max_j(q_W-q_{j,W})
 \ge\frac{m-1}{m}q_W.
\tag{6c}
\]
Finite subsets exhaust the countable returning cylinders, so \(q_W\uparrow\Pr_y\{T<\infty\}\), proving (6a). The competing input may change along this exhaustion; this is legitimate because \(e\) is a supremum over all fixed inputs. No input is chosen after observing the actual seed.

In particular, if \(\Pr_y\{T<\infty\}=1\) on every input, then \(e\ge1-1/m\). Uniform random guessing attains equality without observing \(y\); a uniform label can be sampled with almost-surely finitely many fair bits by rejection sampling. Thus
\[
 \inf_{\mathcal A:\,\Pr_y(T<\infty)=1\ \forall y}e(\mathcal A)
 =1-\frac1m.
\tag{6d}
\]
The return-probability coefficient in (6a) is sharp too: return a uniform label with probability \(\gamma\) and otherwise never return. Then every input has return probability \(\gamma\) and error \(\gamma(m-1)/m\). For rational \(\gamma\), this uses only almost-surely finite coin sampling before that decision; rational choices also establish sharpness of the coefficient. At zero error, (6a) rules out any positive return probability on any input.

The load-bearing property is simultaneous finite interpolation in every label class, not analyticity. Analytic nonpolynomial gaps make the source label globally well-defined and enable the continuous-random success theorem, but they do not obstruct (6b). For a known degree bound, (6b) eventually leaves the admitted class. For an unknown unrestricted degree, increasing the random-bit or query budget, even adaptively and without a uniform cap, cannot yield uniform error below blind guessing with almost-sure return. This does not rule out guarantees restricted by the actual degree, coefficient size, or another quantitative promise, nor does it equate input-dependent errors with one uniform error allowance.

The continuously random coordinate above implicitly supplies infinitely many random bits at unit query cost, so its returning executions need not contain positive-probability finite-bit cylinders. It lies outside the hypothesis of (6a). Exact equality testing is a second idealization. Neither resource is justified merely by the analyticity of the source.

## Prime-edit curves satisfy the nonpolynomial separation criterion

Use the registered generalized-prime controls from AF-559/570:
\[
 P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s},\quad
 h_p(s)=p^{-s}-(p+1)^{-s},\quad Q_p=P-h_p,
 \quad \Phi_p(a)=Q_p^{-1}(E_1(a)),
 \quad E_1(a)=\int_a^\infty e^{-v}\frac{dv}{v}.
\tag{7}
\]
Here \(p\) is any odd rational-prime edit location. The positive Dirichlet series \(Q_p\) is analytic and strictly decreasing on \(s>1\), with range \((0,\infty)\). Its derivative never vanishes. Consequently \(\Phi_p\) is real analytic on \(a>0\). As \(a\downarrow0\), \(E_1(a)\to\infty\) and \(\Phi_p(a)\to1\), giving the required continuous endpoint extension. [[research/arithmetic_fidelity/findings/AF-570-shrinking-windows-turn-affine-prime-edit-separation-into-curvature|AF-570]] gives the stronger analytic extension there, but that is unnecessary for this argument.

For odd primes \(p<q\), [[research/arithmetic_fidelity/findings/AF-559-all-pair-prime-edit-separation-has-uniform-sharp-critical-window|AF-559]]'s exact gap identity follows directly from
\[
 k(s):=h_p(s)-h_q(s)
 =s(s+1)\int_p^q\int_v^{v+1}u^{-s-2}\,du\,dv>0.
\tag{8}
\]
Writing \(s_p=\Phi_p(a)<s_q=\Phi_q(a)\), the mean-value theorem gives
\[
 0<s_q-s_p=\frac{k(s_q)}{-Q_p'(\xi)},
 \qquad s_p<\xi<s_q.
\]
Since the generator \(2\) is unchanged and \(0<k(s)<p^{-s}\),
\[
 0<\Phi_q(a)-\Phi_p(a)
 \le\frac{(2/p)^{s_q}}{\log2}\longrightarrow0
 \qquad(a\to\infty).
\tag{9}
\]
Here \(s_q\to\infty\) because \(E_1(a)\to0\). If this positive analytic gap equalled a polynomial on any open observation window, the real-analytic identity theorem would extend that equality to all \(a>0\). By (9) the polynomial would tend to zero at infinity and therefore be identically zero, contradicting (8).

Thus every finite set of distinct odd prime-edit locations satisfies (2), on every fixed finite positive window. Both the continuous-random identification theorem and the finite-bit minimax bound (6d) apply to these same source curves under (1). No far-out prime threshold or shrinking-window jet asymptotic is needed for this exact separation argument. The source family remains generalized-prime matched controls indexed by rational-prime edits, not alternative ordinary-prime systems.

## Positive noise and exact controls

For any two sources let \(g=F_j-F_i\). By polynomial uniform approximation on \([0,A]\), for every \(\varepsilon>0\) there is \(p\in\Pi\) with
\[
 \|g-p\|_\infty<2\varepsilon.
\tag{10}
\]
The admitted curves \(F_i\) and \(F_j-p\) are therefore within \(2\varepsilon\); opposite errors of size at most \(\varepsilon\) make their full observations identical. Exact full-curve separation coexists with intersecting uniform closures. Analyticity and polynomial calibration alone give no positive robust identification margin.

A rational analytic control is \(F_0=0\), \(F_1(a)=1/(1+a)\) on \([0,1/2]\). For its degree-at-most-\(r\) interpolant \(L_r\) at distinct nodes \(t_0,\ldots,t_r\),
\[
 \frac1{1+a}-L_r(a)
 =\frac{(-1)^{r+1}\prod_{\ell=0}^r(a-t_\ell)}
 {(1+a)\prod_{\ell=0}^r(1+t_\ell)}.
\tag{11}
\]
This proves directly that the false analytic residual has only the interpolation nodes as zeros in this control. More generally, adding polynomial calibration preserves nonidentity, though it may create extra isolated zeros. Truncated geometric sums give explicit full-curve approximants in (10), with remainder \((-a)^{k+1}/(1+a)\).

Exact rational arithmetic checked 99 interpolation, polynomial-reproduction and alias identities for orders \(0\) through \(8\), using \(t_\ell=(\ell+1)/20\); it also checked 12 geometric-remainder identities. The continuous-randomness and finite-bit claims rest on the proofs above, not a simulation of a continuous distribution. Formula (11) is independently verified by multiplying both sides by \(1+a\) and comparing roots and leading coefficients.

A separate exact-rational check tests the simultaneous adaptive-transcript step in (6b), using \(F_0=0\), \(F_1(x)=1/(1+x)\), \(F_2(x)=1/(2+x)\) and reference input \(y(x)=x^2-x/7\) on \((0,1/2)\). On coin word \(1^k0\), query \(t=1/(k+3)\), then
\[
 u=\frac14+\frac1{100(k+1)}+
       \frac{y(t)}{100(1+|y(t)|)},
 \qquad \widehat i=(k+\mathbf1_{\{y(u)>0\}})\bmod3.
\]
For each \(L=1,\ldots,8\), interpolate all \(2L\) observed nodes for all three labels on the words \(k<L\). All 108 reconstructed executions retained both query locations, both responses, and the return label exactly. Their cylinder mass is \(1-2^{-L}\), and the three matched error masses sum to twice that mass, as required by (6c). This finite sanity check verifies the construction on an explicit analytic control; countable exhaustion and the universal bound are proved above.

## Prior art, mathematical delta, and limits

[Kaltofen and Lee (2003), *Early termination in sparse interpolation algorithms*, §1.2 and §6](https://kaltofen.math.ncsu.edu/bibliography/03/KL03.pdf), explicitly discuss interpolation without a supplied degree bound and testing a deterministically fitted interpolant at a random point. Thus the central algorithmic idea is existing prior art. Their Theorem 1's error bound depends on the true degree and the sampling-set size; it is not a uniform guarantee over unbounded degree. This dependence is consistent with (6d), not an escape from it.

[Mityagin (2015), *The Zero Set of a Real Analytic Function*, Proposition 0](https://arxiv.org/abs/1512.07276), supplies a general null-zero-set theorem; in one dimension the isolated-zero argument above suffices. [Gulwani (2013), *Example-Based Learning in Computer-Aided STEM Education*, Property 1](https://www.microsoft.com/en-us/research/wp-content/uploads/2013/05/education13.pdf), already proposes analytic identity testing for synthesis. Its informal random-selection statement is not used for the probability theorem here: our distribution is explicitly supported on a bounded interval, and the proof uses univariate null sets. Interpolation and polynomial approximation are classical; de Boor's *Divided Differences* is already anchored under AF-571. No priority is claimed for these methods.

[Devroye (1986), *Non-Uniform Random Variate Generation*, Chapter XV, §§1–2](https://luc.devroye.org/chapter_fifteen_1.pdf), distinguishes random bits from continuously distributed exact reals and describes finite-word decision trees. [Giles, Hefter, Mayer and Ritter (2019), *Random bit multilevel algorithms for stochastic differential equations*, §5.2, Lemma 11 and Example 14](https://arxiv.org/abs/1808.10623), give a finite-bit truncation/enumeration lower-bound method and a problem separable by continuous randomness but not by random bits at finite worst-case expected cost. Thus neither the observation-model distinction nor finite-execution reduction is new. Here simultaneous polynomial interpolation gives the exact label-error bound (6a) without any expected-cost hypothesis.

The local addition is the precise polynomial-calibration source quotient, its prime-edit nonpolynomiality certificate, and the separation between full-curve uniqueness, finite deterministic certification, continuous-random almost-sure identification, finite-bit blind-guess minimax error, and positive-noise recovery. In particular, allowing a fixed nonzero error below \(1-1/m\) does not make finite-bit identification uniformly feasible merely by permitting unbounded input-dependent stopping. It rules out treating analyticity or randomized identity checks as a cost-free physical repair of AF-575/576.

Polynomial calibration of unknown finite degree is a new explicit hypothesis, not a consequence of the prime construction. Allowing all analytic nuisances would instead create immediate exact aliases by taking a nuisance equal to a source gap. A known polynomial degree bound restores ordinary finite deterministic tests. The present result neither supplies a finite-precision implementation nor revises the smooth-calibration claims of AF-575/576. It establishes no ordinary-prime discriminator, uniform noise floor, or RH implication.
