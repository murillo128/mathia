# AF-577 — Unknown polynomial calibration separates continuous randomness from finite certification

## Status and question

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · ORACLE-MODEL-BOUNDARY · MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

[[research/arithmetic_fidelity/findings/AF-571-polynomial-drift-has-exact-small-window-probe-saturation|AF-571]] assumes a known polynomial calibration degree. AF-575/576 instead bound a derivative but leave its strict slack unknown. Neither addresses calibration that is a polynomial of some finite, **unknown and unbounded** degree, with no derivative or coefficient bound.

In this different class, full curves identify the source exactly but no universally correct deterministic procedure can stop on any finite value transcript. Nevertheless, a continuously randomized exact-real oracle procedure identifies every fixed input almost surely, after at most the actual calibration degree plus two queries. The advantage disappears if a terminating computation must use only finitely many random bits: no such procedure can have both zero error and almost-sure finite termination on every input. Every positive uniform noise margin also disappears.

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
3. If all randomness comes from fair independent coin bits, and each terminating execution reads finitely many bits and makes finitely many queries, zero error and almost-sure finite termination on every input are impossible.
4. Under arbitrary additive observation error \(\|\eta\|_\infty\le\varepsilon\), the uniform full-curve identification radius is zero.

These statements do not assert a sharp fixed-budget minimax error or an optimal degree-dependent query count. They do not extend [[research/arithmetic_fidelity/findings/AF-576-randomized-calibration-recovery-has-a-sharp-error-stopping-tail|AF-576]]'s smooth-nuisance testing lower bound to polynomial nuisances.

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

## Finite-bit zero-error stopping remains impossible

Suppose a coin-based policy is correct almost surely and terminates almost surely on every input. Fix any one input. A terminating computation that reads finitely many coin bits is determined by a finite bit word and its finite oracle transcript. The termination event is a countable union of such cylinders, so at least one terminating correct word has positive probability.

Fix that word, its output label \(i\), and its queried coordinates. Choose \(j\ne i\), and use (3) to construct a polynomial calibration for label \(j\) with the same responses. On this second **fixed** input, every coin stream extending the word follows the same execution and returns \(i\). That cylinder has positive probability, contradicting zero error.

The argument allows arbitrary finite, response-dependent bit and query counts; it does not assume a uniform bound. It does not prohibit Monte Carlo algorithms with a nonzero error allowance. The continuously random coordinate above implicitly supplies infinitely many random bits at unit query cost, so it lies outside this finite-bit stopping model. Exact equality testing is a second idealization. Neither resource is justified merely by the analyticity of the source.

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

Thus every finite set of distinct odd prime-edit locations satisfies (2), on every fixed finite positive window. No far-out prime threshold or shrinking-window jet asymptotic is needed for this exact separation argument. The source family remains generalized-prime matched controls indexed by rational-prime edits, not alternative ordinary-prime systems.

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

## Prior art, mathematical delta, and limits

[Kaltofen and Lee (2003), *Early termination in sparse interpolation algorithms*, §1.2 and §6](https://kaltofen.math.ncsu.edu/bibliography/03/KL03.pdf), explicitly discuss interpolation without a supplied degree bound and testing a deterministically fitted interpolant at a random point. Thus the central algorithmic idea is existing prior art. Their finite-sampling Monte Carlo guarantees are not the zero-error continuous-real oracle model used here.

[Mityagin (2015), *The Zero Set of a Real Analytic Function*, Proposition 0](https://arxiv.org/abs/1512.07276), supplies a general null-zero-set theorem; in one dimension the isolated-zero argument above suffices. [Gulwani (2013), *Example-Based Learning in Computer-Aided STEM Education*, Property 1](https://www.microsoft.com/en-us/research/wp-content/uploads/2013/05/education13.pdf), already proposes analytic identity testing for synthesis. Its informal random-selection statement is not used for the probability theorem here: our distribution is explicitly supported on a bounded interval, and the proof uses univariate null sets. Interpolation and polynomial approximation are classical; de Boor's *Divided Differences* is already anchored under AF-571. No priority is claimed for these methods.

The local addition is the precise polynomial-calibration source quotient, its prime-edit nonpolynomiality certificate, and the separation between full-curve uniqueness, finite deterministic certification, continuous-random almost-sure identification, finite-bit zero-error impossibility, and positive-noise recovery. It rules out treating analyticity or randomized identity checks as a cost-free physical repair of AF-575/576.

Polynomial calibration of unknown finite degree is a new explicit hypothesis, not a consequence of the prime construction. Allowing all analytic nuisances would instead create immediate exact aliases by taking a nuisance equal to a source gap. A known polynomial degree bound restores ordinary finite deterministic tests. The present result neither supplies a finite-precision implementation nor revises the smooth-calibration claims of AF-575/576. It establishes no ordinary-prime discriminator, uniform noise floor, or RH implication.
