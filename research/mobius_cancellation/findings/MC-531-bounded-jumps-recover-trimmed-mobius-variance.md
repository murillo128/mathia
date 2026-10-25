# MC-531 — Bounded jumps recover trimmed Möbius variance

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CONDITIONAL-TRANSFER`,
`NO-NOVELTY-CLAIM`. No arithmetic upper estimate is proved.

## Claim and mathematical delta

Let \(X,H\) be positive integers, \(I_X=\{X,\ldots,2X-1\}\), and
\[
 S_H(j)=M(j+H)-M(j).
\]
Delete an arbitrary set \(E\subset I_X\) of \(B=|E|<X/2\) starts.
For any single constant \(c\in\mathbb C\), define the retained energy
\[
 V_E(c)=\sum_{j\in I_X\setminus E}|S_H(j)-c|^2.
\tag{1}
\]
In particular \(c\) can be the empirical mean on the retained starts;
it need not be the complete-block mean, and need not be bounded a priori.

Suppose zeta has a zero \(\rho_0=\beta+i\gamma\), \(\beta>1/2\),
of multiplicity \(m\). For every fixed \(r>1\), there are constants
\(C>0,X_0\) such that
\[
 \boxed{\sqrt{X V_E(c)}+B^2
 \ge C H X^\beta(\log X)^{m-1}}
\tag{2}
\]
for every integer \(X\ge X_0\), every integer
\[
 1\le H\le\frac{X}{\log X(\log\log X)^r},
\tag{3}
\]
and every \(E,c\) as above. Constants may depend on the selected zero,
its full hypothetical companion zero set, and \(r\), but are uniform in
\(X,H,E,c\).

Thus MC-530's pole-forced variance floor survives arbitrary deletion
whenever
\[
 B^2=o\!\left(HX^\beta(\log X)^{m-1}\right).
\tag{4}
\]
The proof uses the additional exact arithmetic constraint
\[
 S_H(j+1)-S_H(j)=\mu(j+H+1)-\mu(j+1),\qquad
 |S_H(j+1)-S_H(j)|\le2.
\tag{5}
\]
It recovers a complete **linear test**, without first recovering the
complete second moment. For an empirical mean, paying only the amplitude
bound on omitted starts would cost \(HB\) before normalization. Equation (5)
reduces that cost to \(B^2\) using neighboring retained values.

For the near-linear length
\[
 H_X=\left\lfloor\frac{X}{\log X(\log\log X)^r}\right\rfloor,
\tag{6}
\]
the following statement is equivalent to RH: there is an unbounded set
\(\mathcal X\) of positive integers, with sets \(E_X\subset I_X\)
and constants \(c_X\) chosen for \(X\in\mathcal X\), such that for
**every** \(\varepsilon>0\), uniformly on this set at large \(X\),
\[
 |E_X|\ll_\varepsilon X^{3/4+\varepsilon},\qquad
 V_{E_X}(c_X)\ll_\varepsilon X^{1+\varepsilon}H_X.
\tag{7}
\]
The sets and centers can depend on the observed arithmetic data. They
are fixed as families before the epsilon quantifier. No density or
spacing requirement on \(\mathcal X\) is imposed. Neither estimate
in (7) is supplied unconditionally here.

The substantive extension of
[MC-530](MC-530-nonquasianalytic-tests-reach-logarithmic-mobius-windows.md)
is a permitted exceptional-start budget, rather than a larger inversion
range or another regularity class. The exponent \(3/4\) is a sufficient
budget from this recovery argument; it is not claimed to be the optimal
Möbius deletion threshold.

## 1. A discrete recovery lemma with arbitrary missing locations

Let \(u_1,\ldots,u_N\in\mathbb C\) satisfy
\(|u_{j+1}-u_j|\le L\), let \(E\subset\{1,\ldots,N\}\) have
cardinality \(B<N/2\), and put
\(V=\sum_{j\notin E}|u_j|^2\). Then
\[
 \boxed{\sum_{j=1}^N|u_j|\le2\sqrt{NV}+2LB^2.}
\tag{8}
\]
For \(B=0\), Cauchy–Schwarz proves a stronger bound. If \(B\ge1\),
then \(2B+1\le N\). For each \(j\in E\), choose any interval of
\(2B+1\) consecutive indices inside \(\{1,\ldots,N\}\) containing
\(j\). Such an interval exists even at either endpoint. At least
\(B+1\) of its indices are outside \(E\); every index has distance at
most \(2B\) from \(j\). Averaging the triangle inequality over those
good indices, then applying Cauchy–Schwarz, gives
\[
 |u_j|\le \sqrt{\frac{V}{B+1}}+2LB.
\tag{9}
\]
This uses the global retained energy only as an upper bound for the
local retained energy. It does not sum overlapping local energies.
Consequently
\[
 \sum_{j\in E}|u_j|
 \le B\sqrt{\frac{V}{B+1}}+2LB^2
 \le\sqrt{BV}+2LB^2.
\]
The retained contribution is at most \(\sqrt{(N-B)V}\).
Adding proves (8), with deliberately nonoptimal constants.

Apply this to \(u_j=S_H(j)-c\), using (5), \(N=X\) and \(L=2\):
\[
 \sum_{j\in I_X}|S_H(j)-c|
 \le2\sqrt{X V_E(c)}+4B^2.
\tag{10}
\]
Subtracting a constant preserves the jump bound. Subtracting an
arbitrary function of \(j\) does not.

## 2. Recover the pole-isolating linear measurement

MC-530, equations (17)–(20), supplies for \(h=H/X\) a complex test
\(f_h\in C_c^\infty((1,2))\) with
\[
 \int f_h=0,\qquad \sup_h\|f_h\|_\infty<\infty,
\tag{11}
\]
and, writing \(S_{X,H}(y)=M(y+H)-M(y)\), the exact pairing
\[
 L_{X,H}=\frac1H\int_X^{2X}S_{X,H}(y)f_h(y/X)\,dy.
\tag{12}
\]
Uniformly over (3), the same construction gives
\[
 |L_{X,H}|\ge c_0 X^\beta(\log X)^{m-1}
\tag{13}
\]
for all sufficiently large \(X\).

The analytic input to (13) is specific: [[research/mobius_cancellation/findings/MC-528-multiplicity-aware-annihilation-forces-mobius-variance-on-every-block|MC-528]]'s multiplicity-counted
sparse canonical product cancels every unwanted reciprocal-zeta pole;
local division gives a growth bound after exact cancellation; MC-530's
compact nonquasianalytic test dominates that growth and its finite
Bernoulli inverse has uniformly bounded sup norm. The retained pole
contributes \(X^{\rho_0}Q_{m-1}(\log X)\) with nonzero leading
coefficient. Its conjugate is cancelled, so selected-scale cosine zeros
cannot erase (13). No new contour shift, residue summation, simplicity,
or reciprocal-derivative bound is being assumed here.

By (11), replace \(S_{X,H}(y)\) in (12) by
\(S_{X,H}(y)-c\) for **any** one constant \(c\). For integer \(H\),
\(S_{X,H}(y)=S_H(j)\) on each unit interval \([j,j+1)\), apart
from endpoints of measure zero. It follows exactly that
\[
 |L_{X,H}|\le\frac{\|f_h\|_\infty}{H}
             \sum_{j\in I_X}|S_H(j)-c|
 \ll\frac{\sqrt{X V_E(c)}+B^2}{H}.
\tag{14}
\]
Combine (13) and (14) to obtain (2). The complete test is retained;
only its magnitude is reconstructed from the nonexceptional data.
In particular, the test is not multiplied by the indicator of the good
set, which would destroy its exact zero integral and analytic identity.
The original pairing includes windows crossing \(2X\); no endpoint
coefficient is dropped.

## 3. The three-quarter exceptional budget

Put \(D(X)=\log X(\log\log X)^r=X^{o(1)}\). At (6),
\(H_X\asymp X/D(X)\). If (7) holds, (14) gives, for each fixed
\(\varepsilon>0\),
\[
 |L_{X,H_X}|\ll_\varepsilon
 X^{1/2+\varepsilon/2}D(X)^{1/2}
 +X^{1/2+2\varepsilon}D(X).
\tag{15}
\]
If a zero has \(\beta>1/2\), choose \(\varepsilon\) so small
that \(2\varepsilon<\beta-1/2\). The right side is
\(o(X^\beta)\), contradicting (13) on every sufficiently large member
of the unbounded set. Functional-equation symmetry then gives RH.
For the converse, under RH [[research/mobius_cancellation/findings/MC-520-rh-mellin-variance-closes-conditional-farey-window-target|MC-520]]'s classical complete uncentered
estimate gives (7) with \(E_X=\varnothing\), \(c_X=0\), and all
integer \(X\) sufficiently large. Choosing the empirical mean also works.

More generally, at a fixed power length \(H=\lfloor X^\theta\rfloor\),
\(0<\theta<1\), suppose on an unbounded integer scale set that
\[
 B\ll_\varepsilon X^{\delta+\varepsilon},\qquad
 V_E(c)\ll_\varepsilon X^{1+\varepsilon}H,
 \qquad 0\le\delta<1,
\]
for every epsilon. The same calculation excludes zeros with
\[
 \Re\rho>\max\{1-\theta/2,\,2\delta-\theta\}.
\tag{16}
\]
Only a threshold below \(1\) gives a nonvacuous strip. The \(B^2\)
term has a strict advantage over the amplitude-only \(HB\) cost when
\(B=o(H)\). For \(B\) comparable to or larger than \(H\), (8)
is still valid but need not be the best bound.

## 4. Concentrated controls and sharpness boundary

The quadratic deletion term cannot be replaced uniformly by \(o(B^2)\)
using only bounded jumps and the retained energy. A triangular spike
of height \(\ell\), with unit slopes and zero values outside its
\(2\ell-1\) positive entries, has retained energy zero after deleting
those entries, but total absolute mass \(\ell^2\).

This phenomenon occurs even for genuine sliding sums of bounded
coefficients. Set \(a_n=1\) for \(n=q+1,\ldots,q+\ell\),
\(a_n=-1\) for \(n=q+\ell+1,\ldots,q+2\ell\), and zero
otherwise. Its prefix sum is
\[
 A(j)=\max\{0,\min(j-q,q+2\ell-j)\}.
\]
For \(H>2\ell\), the window sum
\(A(j+H)-A(j)\) consists of two disjoint triangular spikes of
opposite sign. Choose \(X>8\ell\) with \(H+2\ell<X\) and place both
inside the start block. Deleting their supports gives
\[
 B=4\ell-2,\qquad V_E(0)=0,\qquad
 \sum_{j\in I_X}|A(j+H)-A(j)|=2\ell^2.
\tag{17}
\]
Thus the \(B^2\) scale in the generic absolute-mass recovery is real,
including when \(B\ll H\). These coefficients are not multiplicative
or Möbius, and their two signed spikes can cancel in a smooth pairing.
Equation (17) proves neither optimality of (7) for Möbius nor failure
of a more phase-sensitive recovery method.

Exact finite checks verified (10), after squaring its nonnegative
residual, in 770,592 cases: lengths \(1\le N\le8\), increments
in \(\{-2,0,2\}\), centers in \(\{-3,0,3\}\), and every deletion
mask with \(B<N/2\). Sixty sliding-sum controls checked (17) for
\(1\le\ell\le20\) and \(H\in\{2\ell+1,3\ell,5\ell\}\).
These are falsification checks of the elementary lemma and indexing;
the proofs above, not the finite checks, establish the general result.

## Prior art, scope and remaining arithmetic input

The recovery lemma is elementary discrete Lipschitz interpolation and
Cauchy–Schwarz. No novelty is claimed for this method, tent controls,
or the classical link between short-interval moments and zero location.
[Zaccagnini, Section 3.3](https://arxiv.org/pdf/1603.02952)
(MC-S72) discusses strong Selberg-integral bounds and quasi-RH for
prime counts; that is adjacent context, not a theorem about the trimmed
signed Möbius moment (1).

[Matomäki–Radziwiłł](https://doi.org/10.4007/annals.2016.183.3.6)
(MC-S1) and
[Matomäki–Radziwiłł–Shao–Tao–Teräväinen, Theorem 1.1(i)](https://arxiv.org/html/2411.05770v2)
(MC-S2) supply almost-all short-interval theory. The latter's
logarithmic exceptional-measure and relative-cancellation bounds do not
supply the simultaneous power-strength inputs (7); its stated range
also stops at \(X^{1-\eta}\) for fixed \(\eta>0\), below (6).
This is a comparison with those theorem statements, not a no-go for
their proof methods or all subsequent short-interval results. The
local comparison in MC-001 deliberately retained only amplitudes and
exceptional mass; it did not exploit the bounded jumps in (5) or this
pole-isolating signed test.

The derived contribution is the explicit missing-start recovery budget
(2), including an arbitrary retained-set center, and its integration
with the existing all-block pole certificate. The literature check
supports classifying the ingredients as classical; it does not establish
external priority for the combined statement.

- The claim uses integer starts and deletion of whole unit cells. A
  measurable exceptional set cutting every cell is not automatically
  represented by its measure in (8).
- The same constant \(c\) is used at every retained start in a block.
  A fitted start-dependent center requires a new jump and pairing audit.
- The analytic certificate still depends on the full hypothetical zero
  set and has no effective or zero-uniform acquisition bound. Multiple
  poles with zero ordinary residue are covered by their leading Laurent
  coefficient, as in MC-528–MC-530.
- A density-one assertion with no quantitative exceptional budget is
  insufficient for (7). No exceptional-set bound, retained variance
  estimate, unconditional Mertens improvement, or proof of RH is obtained.
- No Lean check or independent adversarial approval is asserted. The
  finite recovery lemma is elementary; the load-bearing open problem
  remains an arithmetic estimate of the retained energy and exceptional
  count, not formal transcription of that lemma.

A source estimate can now leave a quantified set of starts uncontrolled
and still feed the zero-exclusion certificate. It must prove both terms
of (2) small on the same selected scales; qualitative almost-all
cancellation cannot replace that joint budget.
