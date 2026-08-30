# WP-033 — Stable Hilbert renorming cannot rescue the critical Mangoldt Gram selector

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE` for the explicit WP-032 escape of changing the finite-place base measure or Hilbert norm while retaining the WP-030 rank-one selector as an intrinsic positive Gram geometry. If the exact critical singleton masses are required to be diagonal values on **unit** prime-event states, then every diagonal reweighting of the Prime-Lattice Hilbert space — and, more generally, every realization in which those normalized event states form a Bessel sequence — inherits the same nonclosability obstruction. A Hilbert weight can make the coordinate formula summable only by changing the normalized arithmetic diagonal. In the canonical Hamiltonian-weighted scale this repair moves the exponent from the critical value `1/2` back into the Euler half-plane.

## 1. Coordinate-invariant formulation of the WP-030 selector

WP-030 gives, on each finite support, a positive rank-one Gram object whose singleton top volume is nonzero and whose every higher principal determinant vanishes. WP-032 showed that the direct global rank-one form is nonclosable on the canonical counting Hilbert space and explicitly left open a change of finite-place base measure/Hilbert norm.

To test that escape without making the answer depend on coordinate normalization, let `H` be a Hilbert space and let

\[
u_j\in H,\qquad \|u_j\|=1,
\tag{1}
\]

be normalized local event states. For the Riemann finite weights it already suffices to take `j=p` over the primes and

\[
w_p=\frac{\log p}{\sqrt p}>0.
\tag{2}
\]

Let `q` be a positive semidefinite Hermitian form on the algebraic span of the `u_j`. The coordinate-invariant rank-one Mangoldt Gram requirements are

\[
q(u_j,u_j)=w_j
\tag{3}
\]

and

\[
\det
\begin{pmatrix}
q(u_i,u_i)&q(u_i,u_j)\\
q(u_j,u_i)&q(u_j,u_j)
\end{pmatrix}=0
\qquad(i\ne j).
\tag{4}
\]

Equation (3) says that the desired arithmetic singleton mass is the geometric value on a unit state, rather than on an arbitrarily rescaled coordinate vector. Equation (4) is exactly the two-point shadow of the WP-030 rank-one/top-volume support rule.

The question is whether changing the ambient Hilbert metric can make such a positive form closable.

## 2. Pairwise zero determinants force one scalar functional

As in WP-032, positivity plus (4) forces equality in Cauchy--Schwarz for every pair. In the pre-Hilbert space obtained from `q` after quotienting its radical, all nonzero images of the `u_j` are therefore collinear.

Consequently there is a linear functional `L` on `span{u_j}` such that

\[
\boxed{q(x,y)=L(x)\overline{L(y)}}
\tag{5}
\]

and, after harmless phases,

\[
|L(u_j)|^2=w_j.
\tag{6}
\]

This statement does not use orthogonality of the event states in the ambient Hilbert metric. It is forced by the **positive selector itself**.

If `L` is unbounded in the ambient Hilbert norm, choose `y_m` with

\[
|L(y_m)|>m\|y_m\|.
\]

After rescaling and changing phase, obtain `x_m` satisfying

\[
L(x_m)=1,
\qquad
\|x_m\|<\frac1m.
\tag{7}
\]

Then

\[
x_m\to0,
\qquad
q(x_m-x_n)=0,
\qquad
q(x_m)=1.
\tag{8}
\]

This is exactly the closability obstruction used in WP-032. Therefore

\[
\boxed{q\text{ closable }\Longrightarrow L\text{ bounded on }\overline{\operatorname{span}}\{u_j\}.}
\tag{9}
\]

By Riesz representation there is then an `h in H` (after restricting to that closed span) with

\[
L(x)=\langle x,h\rangle.
\tag{10}
\]

## 3. A Bessel family forces summable singleton masses

Assume now that the normalized event states form a Bessel sequence: there is a finite constant `B` such that

\[
\sum_j |\langle x,u_j\rangle|^2
\le B\|x\|^2
\qquad(x\in H).
\tag{11}
\]

This includes orthonormal systems, Riesz bases/sequences, frames, and every uniformly stable deformation of the canonical orthogonal prime-event basis.

Using (6) and (10),

\[
\sum_j w_j
=
\sum_j |L(u_j)|^2
=
\sum_j |\langle u_j,h\rangle|^2
\le B\|h\|^2
<\infty.
\tag{12}
\]

Hence:

> **Bessel rank-one no-go.** If normalized event states `{u_j}` are Bessel and a PSD form has positive singleton diagonals `w_j` together with vanishing two-point Gram determinants, closability of the form forces `sum_j w_j < infinity`.

The contrapositive is the useful statement here:

\[
\boxed{
\sum_j w_j=\infty
\quad\Longrightarrow\quad
\text{no closable rank-one PSD selector on any Bessel family of unit event states.}
}
\tag{13}
\]

This is strictly stronger than testing the canonical counting basis alone.

## 4. The critical Riemann masses violate the Bessel condition

For the critical prime singleton masses (2),

\[
\sum_p\frac{\log p}{\sqrt p}=\infty.
\tag{14}
\]

No prime number theorem is needed. For every sufficiently large prime,

\[
\frac{\log p}{\sqrt p}\ge\frac1p,
\]

and Euler's prime harmonic series diverges.

Therefore (13) gives

\[
\boxed{
q(u_p)=\frac{\log p}{\sqrt p},
\quad
\det q|_{\{u_p,u_q\}}=0
\quad\Longrightarrow\quad
q\text{ is nonclosable whenever }\{u_p\}\text{ is Bessel.}
}
\tag{15}
\]

The full prime-power event family only strengthens the conclusion. If one uses

\[
w_{p,k}=\frac{\log p}{p^{k/2}},
\tag{16}
\]

the `k=1` subfamily already has infinite total mass.

Thus the obstruction is present before the Weil autocorrelation lift, before the archimedean gamma term, and before any zero data enter.

## 5. Why a diagonal base-measure change does not help

Consider the most literal escape left by WP-032. Give the prime coordinate vectors a diagonal Hilbert metric

\[
\langle e_p,e_q\rangle_\mu
=\mu_p\,\delta_{pq},
\qquad \mu_p>0.
\tag{17}
\]

The normalized event states are

\[
u_p=\mu_p^{-1/2}e_p,
\tag{18}
\]

and they are still orthonormal. Hence they are Bessel with bound `B=1`, independently of the choice of positive weights `mu_p`.

If the arithmetic weight is required to remain an intrinsic geometric diagonal,

\[
q(u_p)=w_p,
\tag{19}
\]

then (15) applies verbatim. **No diagonal reweighting can restore closability.**

There is an apparent algebraic escape: demand instead

\[
q(e_p)=w_p
\tag{20}
\]

on the now non-unit coordinate vectors. But then the geometric value on a unit event is

\[
q(u_p)=\frac{w_p}{\mu_p}.
\tag{21}
\]

Choosing a rapidly growing `mu_p` can make these normalized masses summable, but it has not preserved the critical Weil diagonal; it has moved the arithmetic normalization into the chosen coordinate embedding.

To restore (19) one must instead impose

\[
q(e_p)=\mu_p w_p,
\tag{22}
\]

and the divergence/nonclosability immediately returns.

This is the coordinate-invariant reason that "change the base measure" is not by itself a solution to WP-032.

## 6. The canonical Hamiltonian-weighted scale only shifts back to the Euler half-plane

Prime Lattice already supplies a canonical positive generator

\[
A e_n=(\log n)e_n
\tag{23}
\]

(`PL-007`). Its most natural diagonal Hilbert reweightings are graph/Gibbs weights generated by `A`. On prime states take, for `tau>0`,

\[
\|e_p\|_\tau^2=p^\tau=e^{\tau\log p}.
\tag{24}
\]

If one keeps the **coordinate** value `q(e_p)=w_p`, then the normalized state has

\[
q(u_p)
=
\frac{\log p}{p^{1/2+\tau}}.
\tag{25}
\]

The total normalized mass is

\[
\sum_p\frac{\log p}{p^{1/2+\tau}},
\tag{26}
\]

which converges exactly when

\[
\frac12+\tau>1,
\qquad\text{i.e.}\qquad
\tau>\frac12.
\tag{27}
\]

For the forward implication compare with `sum_n (log n)n^{-alpha}` for `alpha>1`; for `alpha<=1` the prime summands dominate the divergent `1/p` tail after finitely many primes.

So the canonical heat/Hamiltonian weighting makes the rank-one form honest only after shifting its normalized arithmetic exponent into

\[
\Re s>1.
\tag{28}
\]

That is precisely the Euler-product half-plane already identified repeatedly in WP-009, WP-013, WP-032, and PL-007.

If, instead, one insists that the **unit** states in the weighted Hilbert space still satisfy the critical value (19), then one must use (22), and no value of `tau` helps.

Thus the Hamiltonian-weighted repair has an exact dichotomy:

\[
\boxed{
\begin{array}{ll}
\text{make the form closable} &\Rightarrow \text{change the normalized coefficient to an off-critical/Euler weight},\\[2mm]
\text{preserve the exact critical unit-state coefficient} &\Rightarrow \text{retain nonclosability}.
\end{array}}
\tag{29}
\]

## 7. The obstruction survives stable non-diagonal deformations

The Bessel formulation is useful because it shows that the negative is not an artifact of having chosen a diagonal metric.

Suppose a new Mathia geometry replaces the orthogonal prime-event states by normalized states `{u_p}` that are no longer orthogonal but remain a Bessel sequence. This includes any Riesz/stable-basis deformation and any frame-like representation with a finite upper frame bound.

Equation (12) still applies. Therefore no such stable deformation can carry the exact divergent critical singleton masses inside a closable rank-one selector.

A surviving Hilbert route must do something genuinely stronger: the normalized prime-event family must fail the Bessel upper bound, or the Mangoldt support must cease to be encoded by one global rank-one positive form.

Failure of the Bessel bound is a precise structural requirement, not a contradiction. It means that the infinitely many local event states must already possess enough global coherence/overlap that

\[
\sup_{\|h\|=1}\sum_p|\langle h,u_p\rangle|^2=\infty.
\tag{30}
\]

Such a geometry is no longer a stable renorming of independent prime directions. If Mathia forces one canonically, it would constitute genuinely new global coupling and must be audited on its own merits.

## 8. Archimedean enlargement cannot repair a Bessel finite restriction

Let

\[
H=H_{\rm fin}\oplus H_\infty
\tag{31}
\]

and allow arbitrary positive coupling in a candidate global closed form. If its restriction to the normalized finite event states in `H_fin` still satisfies (3)--(4) with a Bessel family and divergent critical masses, the same sequence (7)--(8) lies entirely in the finite subspace and violates closability of the global form.

Therefore an archimedean sector can escape only by changing the finite representation **before** the exact critical masses are interpreted as unit-state Gram diagonals — for example through a genuinely nonlocal quotient, non-Bessel global state family, support-dependent exterior construction, or a different cohomological/correspondence object.

Merely adjoining infinity after a stable Hilbert renorming does not help.

## 9. Matched controls and sharpness

The summability condition is not a generic impossibility for rank-one positive geometry.

If `{u_j}` is an orthonormal family and

\[
\sum_j w_j<\infty,
\tag{32}
\]

then

\[
h=\sum_j\sqrt{w_j}\,u_j\in H
\]

and

\[
q(x)=|\langle x,h\rangle|^2
\tag{33}
\]

is a bounded rank-one PSD form with

\[
q(u_j)=w_j
\]

and all higher principal determinants zero.

Thus, in the canonical independent-event geometry, summability is exactly the boundary between a legitimate global positive rank-one selector and the WP-032/WP-033 failure.

The argument also applies to generalized-prime/free-monoid controls whenever their proposed critical singleton masses have divergent total mass. A control with summable masses would evade this particular no-go, confirming that the obstruction is an operator-geometry condition rather than an RH theorem in disguise.

## 10. Prior-art and novelty audit

No theorem-level novelty is claimed for the functional analysis used here.

- The Bessel-sequence inequality (11), orthonormal/Riesz/frame special cases, and the Riesz representation step are standard Hilbert/frame theory.
- The fact that vanishing positive `2 x 2` Gram determinants force a rank-one Gram span is elementary Cauchy--Schwarz geometry and was already isolated in WP-032.
- The divergence of the prime harmonic series and the half-plane convergence in (26) are classical.

A targeted search of frame/Bessel and rank-one positive-form literature did not reveal an independent RH mechanism attached to this observation; none is claimed. The durable content is the Mathia-specific architecture consequence: **the base-measure/Hilbert-renorming escape explicitly left open by WP-032 does not work if the exact Mangoldt weights are required to remain geometric values on normalized local states.**

This is not another reformulation of zeta or its zeros. It is a no-go theorem about which Hilbert representations can even host the promising WP-030 positive selector at the critical normalization.

## 11. Boundary of the obstruction

WP-033 does **not** rule out:

- a non-Bessel normalized family of prime states forced by genuinely global Mathia geometry;
- a non-diagonal global metric whose local event family is not Bessel;
- a support-dependent determinant/exterior operation performed before any global Hilbert completion, as in WP-030;
- a representation in which the Weil coefficient is produced by a separate, rigorously derived test-function embedding rather than by the unit-state diagonal itself;
- an indefinite or graded intermediate object whose final positive theorem is not a rank-one Gram form;
- a quotient, boundary response, cohomology, or correspondence construction that changes the finite-place state space before the critical coefficients are read out;
- a non-Hilbert/distributional completion where closable positive-form theory is not the appropriate category.

In particular, equation (21) is not declared illegitimate by fiat. It is simply a **different normalization**: if a future global test-function geometry forces exactly that coordinate scaling and then derives the Weil functional without inserting it, it must be analyzed as a new mechanism rather than as a harmless renorming of WP-030.

## 12. Falsification tests and research consequence

The claim is falsified if any of the following fails:

1. positivity plus zero two-point Gram determinants forces rank one and the representation (5);
2. an unbounded `L` gives the explicit nonclosability witness (7)--(8);
3. closability therefore makes `L` bounded and representable by a Hilbert vector `h`;
4. a Bessel family then forces `sum_j |L(u_j)|^2<infinity`;
5. the exact critical prime masses have divergent total sum;
6. every diagonal Hilbert reweighting has an orthonormal normalized coordinate family and hence remains inside the Bessel no-go when unit-state diagonals are preserved;
7. Hamiltonian weighting with coordinate diagonals fixed replaces the normalized exponent `1/2` by `1/2+tau` and becomes summable only for `tau>1/2`;
8. adding an arbitrary archimedean Hilbert summand cannot repair a nonclosable finite restriction.

All eight tests are exact and require no RH assumption, zero data, analytic continuation, or numerical experiment.

The resulting search boundary is sharper than WP-032:

\[
\boxed{
\text{WP-030 local positive Gram selector}
\;\not\to\;
\text{critical global closed selector by any stable Hilbert/base-measure renorming}.
}
\]

A viable global positivity route must now introduce genuinely non-Bessel/nonlocal coupling, change the support-selection architecture before globalization, or leave the ordinary Hilbert rank-one category entirely. The natural `log n` Hamiltonian does not supply a hidden weighted-space fix: its positive weighting only makes the construction honest after the normalized arithmetic data have moved back to the Euler half-plane.

## Internal dependencies

- `research/weil_positivity/findings/WP-004-prime-lattice-axis-compression-realizes-finite-weil-weight.md`
- `research/weil_positivity/findings/WP-030-incidence-gram-volume-recovers-von-mangoldt-positively-but-is-a-rank-test.md`
- `research/weil_positivity/findings/WP-032-global-determinantal-gram-completion-is-nonclosable-at-critical-weights.md`
- `research/prime_lattice/findings/PL-007-canonical-prime-flow-schatten-ladder.md`
