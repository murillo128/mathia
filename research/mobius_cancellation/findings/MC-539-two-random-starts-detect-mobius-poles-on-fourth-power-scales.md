# MC-539 — Two random starts detect Möbius poles on fourth-power scales

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CONDITIONAL-TRANSFER`,
`NO-NOVELTY-CLAIM`. The randomness is in observation locations, not in
Möbius coefficients. No arithmetic energy ceiling is proved.

## Claim: sample count can be exchanged for prescribed scale coverage

Fix the deterministic scales \(X_k=k^4\), \(k\ge3\), and set
\[
 I_X=\{X,\ldots,2X-1\},\qquad
 L_1(X)=\lfloor X/20\rfloor,\qquad
 L_2(X)=\lfloor\sqrt2 L_1(X)\rfloor.
\tag{1}
\]
At each scale draw just **two** uniform starts with replacement in
each channel, \(R_{i,k,1},R_{i,k,2}\in I_{X_k}\). All draws are
independent, including across scales. With
\(S_L(j)=M(j+L)-M(j)\), define
\[
 V_i(k)=\min_{c\in\mathbb R}\frac12\sum_{a=1}^2
             |S_{L_i}(R_{i,k,a})-c|^2
       =\frac14|S_{L_i}(R_{i,k,1})-S_{L_i}(R_{i,k,2})|^2.
\tag{2}
\]
There is an event of probability one on which RH is equivalent to
\[
 \boxed{\text{for every }\varepsilon>0,\quad
        V_i(k)\ll_\varepsilon X_k^{1+\varepsilon}
        \quad(i=1,2;\ \text{all sufficiently large }k).}
\tag{3}
\]
The constants and onset in (3) may depend on the draws. The scales
are fixed before the draws, and (3) must hold along the **whole
prescribed sequence**, not a favorable unbounded subsequence.

More precisely, if zeta has a zero \(\rho=\beta+i\tau\),
\(\beta>1/2\), then almost surely, for every \(1/2<\gamma<\beta\),
\[
             \max_i V_i(k)>X_k^{2\gamma}
                  \quad\text{for infinitely many }k.
\tag{4}
\]
The same conclusion holds for any fixed increasing integer sequence
\(X_k\to\infty\) satisfying
\[
             \sum_k X_k^{-d}=\infty
                         \quad\text{for every }0<d<1/4.
\tag{5}
\]

[MC-537](MC-537-small-sampled-energy-permits-quarter-power-mobius-observations.md)
uses quarter-power-many samples on each scale and permits an arbitrary
unbounded scale set selected after sampling. Here the decisive input
is repeated independent detection across a prescribed scale sequence.
[MC-538](MC-538-one-fixed-multiplicative-source-defeats-subquarter-random-observations.md)
has a fixed multiplicative control on extremely lacunary scales; its
conclusion does not supply (3) on the scales (1).

## 1. Bounded jumps turn dispersion into a pair-tail lower bound

Let \(u_1,\ldots,u_N\) be any real population with
\(|u_{j+1}-u_j|\le A\), \(A\ge0\). Let \(J,K\) be independent
uniform indices, and for \(T\ge0\) write
\[
 D=\mathbb E|u_J-u_K|,\qquad
 p_T=\Pr\{|u_J-u_K|>T\}.
\]
Then the following finite, translation-invariant inequality holds:
\[
                    \boxed{D\le2T+ANp_T^2+Ap_T.}
\tag{6}
\]
In particular, for \(A>0\) and \(D>2T\),
\[
 p_T\ge\frac{\sqrt{1+4N(D-2T)/A}-1}{2N}.
\tag{7}
\]

To prove (6), averaging over the second index supplies an anchor
\(a\) for which
\[
 B:=\#\{j:|u_j-u_a|>T\}\le Np_T.
\]
Let \(G=\{j:|u_j-u_a|\le T\}\). It is nonempty since it
contains \(a\). Bounded jumps imply
\[
 |u_j-u_a|\le T+A\operatorname{dist}(j,G).
\tag{8}
\]
A complementary consecutive component of length \(b\) contributes
at most \(b(b+1)/2\) to the sum of distances: this bound includes
components touching either endpoint. Summing components gives
\[
 \sum_{j=1}^N\operatorname{dist}(j,G)\le B(B+1)/2.
\tag{9}
\]
The triangle inequality, (8), and (9) now yield
\[
 D\le\frac2N\sum_j|u_j-u_a|
       \le2T+\frac{A}{N}B(B+1)
       \le2T+ANp_T^2+Ap_T.
\]
Solving the quadratic gives (7). Constant signals, \(A=0\),
\(N=1\), ties, and repeated observations cause no exception to (6).
No estimate of the population mean or variance is required.

Consequently, for fixed \(A>0,c>0\), if
\(D\ge cN^\beta\), \(0<\beta<1\), and
\(T=2N^\gamma\) with \(\gamma<\beta\), then for all large \(N\),
\[
                  p_T\gg_{A,c} N^{-(1-\beta)/2}.
\tag{10}
\]
The quadratic exceptional-set cost improves the bound obtainable
from the unrestricted range \(O(AN)\) alone.

## 2. The inherited pole test supplies dispersion on every block

For a hypothetical zero as in (4), of any multiplicity \(m\),
[MC-532, Sections 1–3](MC-532-paired-boxes-recover-trimmed-mobius-variance-at-macroscopic-lengths.md)
supplies compact smooth mean-zero tests \(f_{i,h}\),
\(h=L_1/X\), with uniformly bounded sup norms, such that
\[
 P_i(X)=L_i^{-1}\int_X^{2X}S_{L_i}(y)f_{i,h}(y/X)\,dy,
 \qquad |P_1(X)+P_2(X)|\gg_\rho X^\beta(\log X)^{m-1}
\tag{11}
\]
on every sufficiently large integer block. Constants inherit
dependence on the full hypothetical zero set. The full-multiplicity
annihilator and rounded paired-box inverse are existing analytic
inputs; random sampling supplies neither of them.

For the fixed population \(u_j=S_{L_i}(j)\), \(j\in I_X\), put
\(D_i(X)=X^{-2}\sum_{j,r\in I_X}|u_j-u_r|\). If
\(\bar u=X^{-1}\sum_j u_j\), Jensen gives
\[
                    X^{-1}\sum_j|u_j-\bar u|\le D_i(X).
\]
The cell weights \(w_j=\int_j^{j+1}f_{i,h}(y/X)\,dy\) have
zero sum and uniformly bounded magnitude. Integer window sums are
constant on these cells. Since \(L_i\asymp X\),
\[
 |P_i(X)|=\left|L_i^{-1}\sum_jw_j(u_j-\bar u)\right|
                    \ll_\rho D_i(X).
\tag{12}
\]
Thus (11) implies
\[
                  D_1(X)+D_2(X)\gg_\rho X^\beta
\tag{13}
\]
for every large \(X\). At least one channel has this dispersion
scale, although the channel may change with \(X\).

Each population has jumps at most two, because
\[
 S_L(j+1)-S_L(j)=\mu(j+L+1)-\mu(j+1).
\]
Apply (10), with \(A=2\), to whichever channel satisfies (13).
For fixed \(1/2<\gamma<\beta\), the event
\(E_k=\{\max_i V_i(k)>X_k^{2\gamma}\}\) therefore satisfies
\[
                 \Pr(E_k)\gg_\rho X_k^{-(1-\beta)/2}.
\tag{14}
\]
This estimate uses the distribution of one independent pair, including
coincident draws. It does not require the arithmetic window values
themselves to be independent.

## 3. Independent repetitions and the scale quantifier

The events \(E_k\) are independent because the coefficient sequence
is fixed and the draws at distinct scales are independent. Under (5),
the sum of the lower bounds (14) diverges. For \(X_k=k^4\) it is
\[
                 \sum_k k^{-2(1-\beta)}=\infty,
                         \qquad\beta>1/2.
\tag{15}
\]
The second Borel–Cantelli lemma gives infinitely many \(E_k\).
Explicitly, for every fixed \(K\),
\[
 \Pr\!\left(\bigcap_{k=K}^nE_k^c\right)
 =\prod_{k=K}^n(1-\Pr(E_k))
 \le\exp\!\left(-\sum_{k=K}^n\Pr(E_k)\right)\longrightarrow0.
\]
Intersecting over rational \(\gamma\in(1/2,\beta)\) proves (4)
for every real \(\gamma\) in that interval as well. If desired one
can also intersect over the countable set of zeros. No uncountable
intersection of probability-one events is needed.

Choose \(0<\varepsilon<2\gamma-1\). Along the infinitely many
events in (4), \(\max_i V_i(k)/X_k^{1+\varepsilon}\to\infty\).
This contradicts (3), even when its constants are allowed to depend
on the draws. Functional-equation symmetry then gives RH.

Conversely, RH gives the classical bound
\(M(y)\ll_\delta y^{1/2+\delta}\). All queried endpoints are
\(O(X_k)\), so (2) is \(O_\delta(X_k^{1+2\delta})\), uniformly
in the sampled starts. Taking \(\delta=\varepsilon/2\) proves
(3) for **every** sampling outcome under RH.

## 4. A generic sharp boundary for faster polynomial scales

The exponent four in (1) cannot be increased using only bounded
jumps and an every-scale dispersion floor. This statement concerns
fixed signal families, not the actual Möbius function.

Fix \(a>4\), let \(X_k=\lceil k^a\rceil\), and choose
\[
                         3/4<\kappa<1-1/a.
\]
Before any sampling, prescribe at each scale the same population in
both channels:
\[
 u_j=(A_k-|j-\lfloor3X_k/2\rfloor|)_+,
                  \qquad A_k=\lfloor X_k^\kappa\rfloor.
\tag{16}
\]
For large \(k\), the tent lies inside \(I_{X_k}\), has jumps at
most one, mass exactly \(A_k^2\), and at least \(X_k/2\) zero
entries. Pairs with exactly one zero entry give
\[
                         D_i(X_k)\ge A_k^2/X_k
                                  \asymp X_k^{2\kappa-1},
                         \qquad 2\kappa-1>1/2.
\tag{17}
\]
But the probability that any of the four draws meets the nonzero
support is at most \(8A_k/X_k\). The sum is finite, because
\(a(\kappa-1)<-1\). The first Borel–Cantelli lemma implies that
almost surely both observed variances are eventually zero along the
entire prescribed sequence, despite (17).

These tents are not one common multiplicative coefficient realization
or a model of reciprocal zeta. They show the sharp polynomial scale
boundary for the generic dispersion-and-jump inference used here.
MC-538's stronger common-source comparator retains its own lacunary
scope; no extension of that comparator to these polynomial scales is
asserted. Optimality of the exponent four for Möbius remains open.

## Prior art, validation, and evidence boundary

The quadratic hidden-area mechanism is classical in
[Baran–Demaine–Katz, Section 2](https://erikdemaine.org/papers/Integration_Algorithmica/paper.pdf)
(MC-S85). Equations (6)–(9) derive the discrete pair-tail version
directly. Independent repeated detection is exactly the second
Borel–Cantelli lemma, for example
[Durrett, Theorem 2.3.7](https://services.math.duke.edu/~rtd/PTE/PTE5_011119.pdf)
(MC-S92); the product proof is included above. No new concentration,
integration, or probability principle is claimed.

[Verjovsky, Sections 9–10](https://arxiv.org/html/2607.25002v2#S9)
(MC-S86) provides nearby prior art on derivative persistence and
RH-equivalent local Fourier moments. Those are full moments on
Fourier arcs. The present observation law is one pair of physical
starts per channel at each predetermined scale, combined with the
existing every-block pole certificate. The structural literature
comparison supports this distinction, not an external novelty claim.

Exact integer checks covered all 3,280 populations of lengths one
through eight starting at zero with increments in \(\{-1,0,1\}\).
They verified (6) and its anchor construction for 26,048 half-integer
threshold cases. All 4,083 nonempty subsets in lengths one through
eleven verified (9), including one-sided gaps. Another 120 integer
tents verified their area, dispersion lower bound, support count,
and four-draw hit bound; four rational choices of \(a>4\) checked
the strict exponent interval in (16). These are finite bookkeeping
audits. The proof, not the enumeration, establishes the infinite-scale
claim; no Lean verification or independent adversarial approval is
asserted.

The mathematical delta is a sharp generic trade between observations
per scale and mandatory coverage across scales. It does not make
RH probable, supply (3), or turn finite observations into an RH test.
There are \(O(Y^{1/4})\) queried windows through scale \(Y\) on
the fourth-power sequence, and computing each window sum is a
separate cost. This is no claim of computational speedup. Independence
across scales is load-bearing for the divergent-sum direction; one
cannot reuse arbitrarily dependent draws or retain only favorable
scales. Centered energy also does not recover Farey's complete
uncentered variance. The elementary finite lemma has no identified
separate high-value formalization target.
