---
id: CLUE-prime-lattice-single-box-range-sparse-mellin-interpolation
type: research-clue
status: proposed
origin: research-watch
target_line: prime_lattice
based_on:
  - research/prime_lattice/findings/PL-470-positive-source-strip-growth-and-the-infinite-pole-tail-gate.md
  - research/prime_lattice/findings/PL-471-sparse-zero-annihilators-force-prime-variance-on-every-large-block.md
  - research/prime_lattice/findings/PL-473-box-fourier-zeros-obstruct-logarithmic-window-test-inversion.md
  - research/prime_lattice/findings/PL-475-two-box-lengths-force-paired-macroscopic-prime-variance.md
  - research/prime_lattice/findings/PL-486-subunit-order-mellin-filters-cannot-preserve-a-fixed-box-range.md
  - research/mobius_cancellation/findings/MC-528-multiplicity-aware-annihilation-forces-mobius-variance-on-every-block.md
---

# Can sparse-zero isolation be performed inside one fixed box range?

## Observation

PL-471 constructs a compact smooth Mellin test isolating one zero from
the full power-sparse set to the right of a fixed abscissa. PL-473
obstructs uniformly accurate inversion of a **preselected** nonzero
target as the box width varies. PL-475 changes the measurement to two
lengths and recovers that target through compact distributional
deconvolution. None decides whether one can choose the target inside
the range of a **single fixed macroscopic box** from the outset.

This is not recovery of arbitrary signals. The classical boxcar
frequency loss in [Johnstone--Raimondo (2004)](https://doi.org/10.1214/009053604000000391)
and the multichannel Bezout reconstruction in
[Casey--Walnut (1994)](https://doi.org/10.1137/1036140), already sources
140 and 142, concern the inversion side of the question. They do not
by themselves settle simultaneous sparse Mellin interpolation inside
the single-box range. No new deconvolution theorem or priority is
claimed here.

## Research question

Fix \(h_*=1/20\) and \(J=(4/3,5/3)\). Put
\[
A_hf(u)=h^{-1}\int_0^h f(u-v)\,dv,\qquad
K_{s,h}(v)=\frac{(v+h)^s-v^s}{hs},
\]
where the value at \(s=0\) is defined by continuity, and define
\[
\Phi_{h,f}(s)=\int(A_hf)(u)u^{s-1}\,du
            =\int_J f(v)K_{s,h}(v)\,dv.
\tag{1}
\]
All powers use the real logarithm of positive arguments. For
\(f\in C_c^\infty(J;\mathbb C)\), the target \(A_{h_*}f\)
has compact support in \((1,2)\), and
\(\Phi_{h_*,f}(1)=\int_J f\), since \(K_{1,h_*}=1\).

Let \(\mathcal Z\) be a discrete set in
\(\{s:\sigma_0<\Re s<1\}\), where \(1/2<\sigma_0<1\), with
\[
\#\{\lambda\in\mathcal Z:|\lambda|\le R\}
    \le C(1+R)^a,\qquad 0<a<1,
\]
and select \(\rho_0\in\mathcal Z\). Does there always exist such
an \(f\) satisfying
\[
\boxed{\int_J f=0,\qquad
\Phi_{h_*,f}(\rho_0)=1,\qquad
\Phi_{h_*,f}(\lambda)=0\quad
(\lambda\in\mathcal Z\setminus\{\rho_0\})?}
\tag{2}
\]
The function may depend on the entire set. No effective construction,
uniform norm over sets, or uniformity in \(h_*\) is requested. The
arithmetic instance uses the distinct zeros of the four mod-5 factors
in this half-plane, with coincident zeros merged as in PL-471.

An optional stronger version would make the same interpolation construction
usable for reciprocal poles. MC-528 supplies the exact source-side motivation:
outside a box-range restriction, a multiplicity-counted sparse canonical
product times a rapidly decaying Mellin transform cancels all unwanted
principal parts of `1/zeta`, while preserving a selected pole of arbitrary
finite order. Simple test zeros would not suffice at unwanted multiple poles.
The prime question (2) does not require this stronger version.

Give each point `lambda` a positive integer multiplicity `m_lambda`, with
`sum_(|lambda|<=R) m_lambda <= C(1+R)^a`, and put

`P(s)=(s-1) product_(lambda != rho_0) (1-s/lambda)^(m_lambda)`.

Can a fixed-box interpolant also satisfy
`Phi_(h_*,f)^(j)(lambda)=0` for every unwanted point and
`0<=j<m_lambda`, with `Phi_(h_*,f)(rho_0)=1`, while the entire quotient
`G=Phi_(h_*,f)/P` has a bound
`|G(sigma+it)|<=C exp(-c |t|^b)` for some `a<b<1`, uniformly on
each fixed closed vertical strip? Constants may depend on the strip and
the full set. This is a sufficient analytic strengthening, not an asserted
necessary condition for (2) or for a single-window arithmetic result.

## Why it may matter

For the actual identity-residue prime source, (2) would let PL-471's
full explicit formula act directly on \(\varphi=A_{h_*}f\), giving
\(\sum_n a_n\varphi(n/X)=-w_{\rho_0}X^{\rho_0}+O(X^{\sigma_0})\).
For \(H=\lfloor h_*X\rfloor\),
\[
\|A_{H/X}f-A_{h_*}f\|_\infty
 \le \|f'\|_\infty/(2X).
\]
The coefficient envelope \(a_n\le\log n\) makes the rounding
cost \(O_f(\log X)\). The mean-zero window pairing and
Cauchy--Schwarz would therefore yield the **single-length** floor
\[
V_1(X,H)\ge cH^2X^{2\Re\rho_0-1}
\]
on every sufficiently large block, in the notation of PL-475.
Thus a single macroscopic empirical-variance ceiling
\(V_1(X,H)\ll XH(\log X)^A\) on an unbounded scale set would
exclude this zero. The ceiling itself would remain unproved. This
conditional payoff changes the measurement hypothesis; it does not
identify the two variances in PL-475 or contradict PL-473.

## Decisive test

Prove (2) for the stated sparse class, or construct a set satisfying
those same strip and counting assumptions for which it fails. A
counterexample would refute a sparsity-only route, not the actual-prime
variance floor. A weakened positive result must state its extra
separation, geometry, or growth assumptions and check them for the
arithmetic application.

Finite interpolation is not the remaining obstruction. For any finite
set of distinct \(\lambda_j\) with \(0<\Re\lambda_j<1\),
\(1,K_{\lambda_j,h_*}\) are linearly independent on \(J\).
Indeed a dependence extends analytically to all \(v>0\).
Differentiating it gives
\[
\sum_j c_jv^{\lambda_j-1}
 =\sum_j c_j(v+h_*)^{\lambda_j-1}=O(1)\quad(v\downarrow0).
\]
With \(t=-\log v\), the left side is
\(\sum_j c_j e^{(1-\lambda_j)t}\). Since this sum is bounded
for \(t\ge0\), its Laplace transform is holomorphic on
\(\Re z>0\), but for large \(\Re z\) equals
\(\sum_j c_j/[z-(1-\lambda_j)]\). The distinct poles all lie
in that half-plane, so every \(c_j=0\); the constant coefficient
also vanishes. Independence of these distributions on \(J\) makes
the finite moment map from \(C_c^\infty(J)\) surjective.

This proves finite feasibility, not convergence to an infinite
interpolant. A packet-by-packet construction must control support,
all necessary derivative seminorms and the limiting selected value;
PL-470 explains why uncontrolled packet norms and a growing pole tail
cannot be discarded. The exact test (2) asks for the smooth
annihilator itself, not just non-density in an unspecified topology.

Nor does PL-471's genus-zero differential filter automatically preserve
the box range. Writing \(E=u\partial_u\) and
\(\tau_hg(u)=g(u-h)\), one has
\([E,\tau_h]=h\tau_h\partial_u\). Mellin filtering and additive
translation therefore do not commute. A claimed transfer of that
construction must supply the missing compatibility, not just cite the
existence of an unrestricted sparse Mellin interpolant.

[[research/prime_lattice/findings/PL-486-subunit-order-mellin-filters-cannot-preserve-a-fixed-box-range|PL-486]]
now excludes a universal version of that compatibility: if an entire
symbol satisfies \(|P(s)|\le C\exp(C|s|^a)\), \(a<1\), and
\(P(-u\partial_u)A_{h_*}f\) preserves even one nonzero box Fourier
zero for **every** mean-zero compact Gevrey input of order
\(1<q<1/a\), then \(P\) is constant. This includes the nonconstant
sparse products used in PL-471. It does not exclude a specially
chosen input satisfying both sets of constraints, so (2) remains the
decisive question and the clue remains proposed.

For the optional reciprocal version, test a selected double pole with zero
ordinary residue and unwanted repeated poles before passing to an infinite
set. The target is full Hermite cancellation **and** the displayed quotient
decay, not merely holomorphic removability. MC-528 proves, for the actual
zeta multiset and each `sigma_0<sigma_1<Re rho_0`,
`|P(s)/zeta(s)|<=C |t|^C exp(C |t|^a)` at sufficiently large heights,
uniformly for `sigma_1<=Re s<=2`, by cancelling local factors before
estimating them. The proposed decay would dominate that bound; its
availability inside the box range is unproved. If this stronger problem
fails, identify whether the obstruction concerns Hermite feasibility or
quotient growth, and keep the original simple-value question (2) separate.
The reciprocal datum and sufficient test are stated here completely;
the cross-line source path supplies provenance, not a reading grant.

## Evidence boundary

This is a proposed interpolation question, not an established
single-window theorem or an accepted clue. The finite calculation
checks that a finite packet is not already a counterexample; it does
not establish the infinite smooth separation in (2). No uniform
conditioning, numerical extrapolation, Lean result, independent
adversarial approval, variance ceiling, or RH/GRH progress is claimed.
The actual-source implication would still require PL-471's arithmetic
zero-density, logarithmic-derivative growth and noncancelling residues;
a generic positive or phase-deformed source does not inherit them.
The reciprocal extension likewise has no established fixed-box solution.
MC-528's unrestricted test and the existing near-linear or paired-window
Möbius results do not answer it. Even a positive solution would remove a
measurement restriction, not provide an independent variance ceiling.
