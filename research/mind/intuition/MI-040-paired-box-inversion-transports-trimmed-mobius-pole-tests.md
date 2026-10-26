# MI-040 — Paired-box inversion and deleted-start recovery transfer between prime and Möbius tests

**Evidence level:** supported conditional cross-line deduction from
[PL-475](../../prime_lattice/findings/PL-475-two-box-lengths-force-paired-macroscopic-prime-variance.md),
[MC-528](../../mobius_cancellation/findings/MC-528-multiplicity-aware-annihilation-forces-mobius-variance-on-every-block.md),
[MC-531](../../mobius_cancellation/findings/MC-531-bounded-jumps-recover-trimmed-mobius-variance.md),
[MC-532](../../mobius_cancellation/findings/MC-532-paired-boxes-recover-trimmed-mobius-variance-at-macroscopic-lengths.md), and
[PL-476](../../prime_lattice/findings/PL-476-trimmed-paired-prime-variance-retains-the-grh-obstruction.md).
The local mechanisms are retained in [Prime Lattice MI-067](../../prime_lattice/mind/intuition/MI-067-two-box-lengths-recover-smooth-pole-tests-at-macroscopic-scale.md)
and [Möbius MI-103](../../mobius_cancellation/mind/intuition/MI-103-bounded-jumps-price-deleted-starts-in-pole-tests.md).
MC-532 proves the composition and its quantified RH equivalence;
PL-476 transfers deleted-start recovery back to the prime source. This
note preserves the cross-line correspondence without claiming independent
adversarial approval, an arithmetic upper estimate, formal verification
or novelty.

The transferable object is a fixed **smooth mean-zero test**, not the
prime logarithmic derivative or its residue weights. Conditional on a
zeta zero \(\rho_0=\beta+i\gamma\), \(\beta>1/2\), of multiplicity
\(m\), MC-528 supplies
\[
T_\phi(X)=\sum_n\mu(n)\phi(n/X)
=X^{\rho_0}Q_{m-1}(\log X)+O(X^{\sigma_1}),
\quad 1/2<\sigma_1<\beta,
\]
with nonzero leading coefficient of \(Q_{m-1}\). Its input Gevrey bump
may be chosen inside \((\log(4/3),\log(5/3))\); the convergent
derivative series preserves support. Thus
\(\phi\in C_c^\infty((4/3,5/3))\) and \(\int\phi=0\), exactly
the input class of PL-475's source-independent inverse.

Write \(A_hf(u)=h^{-1}\int_0^h f(u-v)\,dv\). For sufficiently large
integers \(X\) and integer \(1\le H\le X/20\), put
\(K=\lfloor\sqrt2H\rfloor\), \(L_1=H\), \(L_2=K\). The two uniformly
bounded, mean-zero tests satisfy
\[
A_{H/X}f_1+A_{K/X}f_2=\phi+R_X,
\qquad \|R_X\|_\infty=O(X^{-1}),
\]
with the tests supported in one compact subset of \((1,2)\) and the
residual in a fixed compact set. Since \(|\mu(n)|\le1\),
the coefficient sum of this rounding error is \(O(1)\), rather than
the prime source's \(O(\log X)\). Hence, for arbitrary constants
\(c_1,c_2\), the sum of the complete pairings
\[
P_i=L_i^{-1}\int_X^{2X}\{M(y+L_i)-M(y)-c_i\}f_i(y/X)\,dy,
\qquad i=1,2,
\]
has modulus \(\gg X^\beta(\log X)^{m-1}\). When \(H=K\), these
are still two tests; their data may coincide and no independence is used.

Choose separate masks \(E_i\subset I_X=\{X,\ldots,2X-1\}\),
\(B_i=|E_i|<X/2\), and let
\[
V_i=\sum_{j\in I_X\setminus E_i}
|M(j+L_i)-M(j)-c_i|^2.
\]
The integer-window jump bound and MC-531's reconstruction lemma give
\(|P_i|\ll(\sqrt{XV_i}+B_i^2)/L_i\). The triangle inequality therefore
transfers the pole certificate to
\[
\boxed{
\frac{\sqrt{XV_1}+B_1^2}{H}
+\frac{\sqrt{XV_2}+B_2^2}{K}
\gg X^\beta(\log X)^{m-1}.}
\tag{*}
\]
All constants are independent of \(X,H\), masks and centers once the
selected zero and full zero set are fixed. The two repairs act on
different losses: two kernels recover the smooth target through the box
zeros; bounded jumps recover the complete pairing from omitted starts.
No cut test, incomplete contour or equality of the two centers is used.

At \(H=\lfloor X/20\rfloor\), suppose both channels on one unbounded
set of integer scales obey, for every \(\varepsilon>0\),
\[
B_i\ll_\varepsilon X^{3/4+\varepsilon},\qquad
V_i\ll_\varepsilon X^{1+\varepsilon}L_i,\qquad i=1,2.
\]
The scale set, masks and centers are fixed before the epsilon
quantifier. The left side of (*) is
\(O_\varepsilon(X^{1/2+\varepsilon/2}+X^{1/2+2\varepsilon})\),
contradicting any \(\beta>1/2\) when \(2\varepsilon<\beta-1/2\).
Thus those **unproved joint estimates** would imply RH. Conversely,
[MC-520](../../mobius_cancellation/findings/MC-520-rh-mellin-variance-closes-conditional-farey-window-target.md)
supplies both complete uncentered moment bounds under RH; empty masks
and zero centers give the required fixed families on all large integer
scales. The paired criterion is therefore equivalent to RH. This costs
a second length but removes the single-box logarithmic restriction from
the trimmed criterion. With empty masks, direct-sum Cauchy–Schwarz also
gives \(V_1/H^2+V_2/K^2\gg X^{2\beta-1}(\log X)^{2m-2}\).

The transfer uses the reciprocal-zeta test with its full Laurent term;
it does not identify reciprocal residues with same-sign prime residues.
The inverse alone has no arithmetic selectivity. A lone small variance,
a qualitative exceptional density, or a start-dependent fitted center
does not supply (*). The bounded-jump tent control establishes only the
generic absolute-mass cost, not optimality of the Möbius deletion budget.
Full-zero-set dependence and non-effective onset remain unchanged.

The reverse transfer has an explicit coefficient price. For a generic
source \(a_n\), the same integer-window identity gives
\(\Delta S_L(j)=a_{j+L+1}-a_{j+1}\). If this is bounded by
\(J_X\), the common finite lemma bounds a complete pairing by
\[
|P_i|\ll_\phi
 \{\sqrt{XV_i}+J_XB_i^2\}/L_i.
\]
Thus the two source-dependent costs separate:

| Source | Jump bound \(J_X\) | Rounded-target error | Isolated pole signal |
| --- | --- | --- | --- |
| \(\mu(n)\) | \(2\) | \(O(1)\) | \(X^{\rho_0}Q_{m-1}(\log X)\), nonzero leading coefficient |
| \(\Lambda(n)\mathbf1_{n\equiv1\ (5)}\) | \(\log(3X)\) | \(O(\log(3X))\) | \(-w_{\rho_0}X^{\rho_0}\), \(w_{\rho_0}>0\) |

PL-476 therefore proves, with \(V_i^{(p)}\) defined as the retained
energy of the prime window about its own constant and \(B_i^{(p)}\)
its omitted-start count,
\[
\sum_{i=1}^2
\frac{\sqrt{XV_i^{(p)}}+(B_i^{(p)})^2\log(3X)}{L_i}
\gg X^\beta.
\]
Here \(X\) is an integer, each \(B_i^{(p)}<X/2\), and the length,
mask and center choices have the same uniformity as in (*). A common
zero of the four mod-5 functions adds positive multiplicity weights;
logarithmic derivatives retain simple poles even at multiple zeros.
The Möbius logarithmic multiplicity factor must not be copied to primes.

The same quantified \(3/4\)-deletion and retained-energy criterion
above, now for the prime source, is equivalent to **joint GRH for zeta
and the three primitive nonprincipal mod-5 functions**. The extra
logarithm is absorbed by the strict exponent gap to \(\beta>1/2\).
Its converse is independent: the GRH prime-counting error
\(O(\sqrt{x}\log^2(3x))\), with empty masks and centers \(L_i/4\),
gives \(V_i^{(p)}\ll X^2\log^4(3X)\), sufficient at
\(L_i\asymp X\). It supplies no short-window analogue of MC-520.
The common operator and recovery lemma identify an observation budget;
the different arithmetic pole formulas and converse estimates remain
separate inputs. Constant coefficients also satisfy the jump bound but
give constant window sums, so recovery alone cannot force a pole signal.

The observation geometry further separates count from recovery cost.
[MC-533](../../mobius_cancellation/findings/MC-533-geometric-start-coverage-recovers-sparsely-sampled-mobius-variance.md)
gives a source-independent replacement: for any nonempty retained set
\(R_i\), assign each start to its nearest sample \(\pi_i(j)\), let
\(w_{i,r}=|\pi_i^{-1}(r)|\),
\(D_i=\sum_j|j-\pi_i(j)|\), and
\(\widetilde V_i=\sum_{r\in R_i}w_{i,r}|S_{L_i}(r)-c_i|^2\).
For jump bound \(J_X\), telescoping gives
\[
\sum_j|S_{L_i}(j)-c_i|
\le\sqrt{X\widetilde V_i}+J_XD_i,
\qquad
|P_i|\ll_\phi\frac{\sqrt{X\widetilde V_i}+J_XD_i}{L_i}.
\]
MC-533 and
[PL-478](../../prime_lattice/findings/PL-478-geometric-coverage-retains-sparsely-sampled-prime-variance.md)
prove this composition for their respective complete pole tests,
using \(J_X=2\) and \(\log(3X)\). The distinct pole signals remain
unchanged. Fix the grid of spacing \(g_X=\lfloor\sqrt X\rfloor\)
starting at \(X\) and ending at its last point below \(2X\), with
\(q_X\asymp\sqrt X\) samples. It pays \(D_i=O(X^{3/2})\) and
\(w_{i,\max}=O(\sqrt X)\). At \(H=\lfloor X/20\rfloor\),
define \(Q_i=\min_c\sum_{r\in R_X}|S_{L_i}(r)-c|^2\) for each
source separately. The same observation statement
\[
\exists\mathcal X\text{ unbounded, fixed before }\varepsilon,
\quad Q_i(X)/q_X\ll_\varepsilon X^{1+\varepsilon}
\quad(i=1,2;\ \forall\varepsilon>0;\ X\in\mathcal X)
\]
is equivalent to RH for Möbius, and to joint mod-5 GRH for the prime
source. This is a correspondence of observation criteria, not an
equivalence between the two hypotheses. Both channels share one scale
set within each criterion; no common scale set across sources is needed.
Their separate converses use pointwise Mertens and prime-counting
estimates, respectively, not complete-to-sparse mean-square inference.
The extra prime logarithm changes no exponent because every hypothetical
\(\beta>1/2\) leaves a strict power gap. Neither ceiling is proved.

[PL-477](../../prime_lattice/findings/PL-477-common-mask-paired-windows-retain-quadratic-deletion-ambiguity.md)
explains why this sparse-grid improvement does not remove the quadratic
worst-case cost for clustered deletions. Its common mask consists of
three separated intervals of length \(10m\), so nearest retained
coverage has \(D_i\asymp m^2\asymp B_X^2\) in both channels.
The balanced coefficient packet produces a primitive hidden in these
intervals and their endpoint translates; its nonzero first moment
changes the prescribed signed smooth target by
\(\asymp B_X^2/X\) while leaving both retained vectors identical.
Unlike a generic distance-envelope sequence, these are two compatible
window channels of each of two fixed positive sources. Thus neither
using a common mask nor replacing absolute mass by a signed target
alone yields a uniform power saving in that source class. Geometric
coverage can improve the budget; an improvement at the same bad geometry
requires a source restriction beyond these generic inputs. Arithmetic
could supply such a restriction.
The control is supported on a full residue class, not prime powers,
and does not establish a lower sampling bound for either arithmetic
source or identify their zero sets.

[MC-534](../../mobius_cancellation/findings/MC-534-common-squarefree-coefficients-retain-signed-sampling-ambiguity.md)
adds a different admissible-class obstruction: for each fixed nonzero
\(\phi\in C_c^1((1,2);\mathbb C)\), any \(q\le\kappa_\phi X\)
integer interval queries admit two sequences with exact magnitudes
\(|a^\pm(n)|=\mu(n)^2\), identical query values in \(\{-1,0,1\}\),
and target separation \(\gg_\phi X/(q+1)\). Here \(q\) counts all
intervals across both channels. Deterministic adaptive queries obey the
same obstruction; no randomized average-case conclusion follows.

The explicit bridge to PL-477 is the prefix difference. If
\(F(n)=\sum_{k\le n}(a^+(k)-a^-(k))\), an observed window sees
only \(F(j+L)-F(j)\), whereas its smooth target sees
\[
\sum_n(a^+(n)-a^-(n))\phi(n/X)
=-\sum_nF(n)\{\phi((n+1)/X)-\phi(n/X)\}.
\]
PL-477 hides one balanced primitive and its two translates with a common
mask; its area is of order \(B^2\). MC-534 pins the primitive to zero
at every queried endpoint and places nonnegative square-free sign bridges
between them. Their total area is \(\gg_\phi X^2/(q+1)\), and a
fixed derivative-phase interval prevents signed cancellation. Both controls
therefore expose the same endpoint-observation kernel, with different
source constraints and different geometry budgets. The square-free control
rules out saving a sample-count power using signedness and common-source
consistency alone: for fixed \(0<\delta<1/2\), \(q\le X^{1/2-\delta}\) leaves ambiguity
\(\gg_\phi X^{1/2+\delta}\). It does not transfer that lower bound to
the positive prime class, impose multiplicativity, or retain the arithmetic
pole formula. A better actual-source recovery must exclude the respective
control; the shared finite operator alone cannot do so.

The random small-energy interface changes the recovery cost again.
[MC-537](../../mobius_cancellation/findings/MC-537-small-sampled-energy-permits-quarter-power-mobius-observations.md) and
[PL-482](../../prime_lattice/findings/PL-482-small-empirical-energy-permits-quarter-power-prime-observations.md), retained in
[Möbius MI-104](../../mobius_cancellation/mind/intuition/MI-104-small-random-sample-energy-controls-dispersion-but-subquarter-multiplicative-bridges-survive.md) and
[Prime Lattice MI-068](../../prime_lattice/mind/intuition/MI-068-empirical-energy-controls-prime-pole-tests-with-quarter-power-random-starts.md), use the same two macroscopic lengths but replace the deterministic grid by `2q` independent uniform draws with replacement per channel. Here `V_i` is the **average** sample-centered energy, with repeated draws counted.

For fixed populations with jump bound `J_X`, the common finite lemma gives, outside probability `3exp(-t)` per channel,

`D_i <= (4+16t/sqrt(q))sqrt(V_i)+8J_X X t^2/q^2+16J_X t/q`,

where `D_i=X^(-2)sum_(j,k)|S_(L_i)(j)-S_(L_i)(k)|`. Jensen and exact zero mean of the test give `|P_i|<=C_phi XD_i/L_i`. Thus only mean absolute dispersion is needed; complete second-moment recovery and nearest-sample coverage weights are unnecessary for this observation law. Small sample energy bounds both paired differences and the sampled range, producing the `X/q^2` remainder. This is not a deterministic bound for all sample placements.

With `q=ceil(X^(1/4))`, `t=4log X`, the source correspondence is explicit:

| Fixed source | Jump bound | Almost-sure recovery remainder | Pole signal |
| --- | --- | --- | --- |
| Möbius | `2` | `sqrt(X)(log X)^2` | `X^beta(log X)^(m-1)` |
| Identity-residue mod-5 Mangoldt | `log(3X)` | `sqrt(X)(log X)^3` | `X^beta` |

Each row yields `sqrt(V_1)+sqrt(V_2)+remainder >= c_rho signal` on all large integer scales. Each source separately has a probability-one event, uniform over its bounded mean-zero tests. On it, the same quantified observation premise—one common unbounded scale set before epsilon, with both `V_i<<_epsilon X^(1+epsilon)` for every epsilon—is equivalent to that row's zero hypothesis. Extra prime logarithms do not change the exponent because every excluded `beta>1/2` leaves a strict power gap. The separate pointwise converses remain necessary; no equivalence between RH and joint mod-5 GRH is implied.

[MC-538](../../mobius_cancellation/findings/MC-538-one-fixed-multiplicative-source-defeats-subquarter-random-observations.md) now fixes the order-of-choices escape in the earlier query controls. For each `0<=alpha<1/4` and `3/4<kappa<1-alpha`, one deterministic square-free multiplicative sign source and predetermined lacunary scales have almost-sure small sampled energies in **both** channels, yet a fixed smooth target of size at least `X^(2kappa-1)/log^2 X`. The balanced primitive has width `X^kappa`; its signed response is its area divided by `X`, while sampling sees it only at window endpoints with total hit probability `O(X^(alpha+kappa-1))`. Thus multiplicativity and fixing the source before the random seed do not save a power for this class. The current bridge has no composite copies below the observation horizon; lacunarity absorbs the old prescribed-prime second-moment factor.

That control is not in the positive prime-coefficient class and does not retain Möbius's prime signs or reciprocal-zeta formula. [PL-483](../../prime_lattice/findings/PL-483-fixed-prime-supported-sources-evade-subquarter-uniform-observations.md), retained in Prime Lattice MI-068, supplies a distinct positive control: fixed `b^+,b^-` with `a/2<=b^+,b^-<=3a/2`, modifications only at primes `1 mod 5`, and cumulative error `O(x^kappa)` relative to `a=Lambda 1_(1 mod 5)`. On `X_k=4^k`, their subquarter-power samples eventually equal the baseline's almost surely, while a fixed smooth target separates them by `asymp X_k^(2kappa-1)`. This is the same endpoint kernel and area mechanism, now realized by balanced prime-capacity packets.

The source classes and the energy conclusions must remain separate:

| Fixed control | Retained structure | What the missed samples establish |
| --- | --- | --- |
| MC-538 | Multiplicativity and exact square-free magnitudes | Small sampled energies despite a large signed target, on its predetermined lacunary scales |
| PL-483 | Positive relative weights, exact prime-power support and leading PNT | Exact equality with baseline samples on `4^k`; no bound on their common energy |

Neither control retains its actual arithmetic pole identity. The prime result excludes uniform signed recovery over the enlarged class; it does not establish optimality of the exact-prime energy criterion. Neither row bounds an estimator using accumulated observations at other scales.

[MC-539](../../mobius_cancellation/findings/MC-539-two-random-starts-detect-mobius-poles-on-fourth-power-scales.md) shows why the scale quantifier is another observation resource. For jumps at most `J_X`, pair dispersion `D` and pair-tail probability `p_T` satisfy `D<=2T+J_X X p_T^2+J_X p_T`. In the Möbius row, `J_X=2` and the pole certificate forces dispersion `gg X^beta` in at least one channel on every large block. Two starts per channel then detect variance greater than `X^(2gamma)`, `1/2<gamma<beta`, with probability `gg X^(-(1-beta)/2)`. Independent repetition at `X_k=k^4` makes those probabilities nonsummable. Consequently the two-sample energy ceiling on **every sufficiently late prescribed scale** is almost surely RH-equivalent. It does not allow a favorable unbounded subset selected after the draws.

The common relation is `window difference = primitive endpoint difference`, with target size set by primitive area. Sparse scales make endpoint hits summable in both control classes; prescribed sufficiently dense scales make the pole-forced pair detections nonsummable. The latter uses the actual every-block pole certificate, not just retained support or multiplicativity. MC-539 proves this alternative for Möbius; this note does not assert a new prime two-sample theorem. No arithmetic ceiling, finite decision procedure, cross-scale recovery lower bound, or optimal actual-source sampling rate follows.
