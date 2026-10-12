# AF-554 — Critical-index tail transitions retain the reference profile through an exponential-integral window

## Status

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · PRIME-TAIL · DOUBLE-SCALING · CALIBRATION-INVARIANT · MATCHED-CONTROL · NO-NOVELTY-CLAIM

## Claim: a critical window missing from fixed-index boundary jets

Let \(1<q_1<q_2<\cdots\) be a locally finite simple positive generator system, with \(q_n\to\infty\). Assume its reciprocal-generator counting function satisfies the **uniform Mertens-type condition**
\[
M_Q(x):=\sum_{q_k\le x}\frac1{q_k}
=\kappa\log\log x+B_Q+O(1/\log x),\quad x\to\infty,\qquad \kappa>0.
\tag{1}
\]
Define \(Q(s)=\sum_{k\ge1}q_k^{-s}\), \(T_n(s)=\sum_{k\ge n}q_k^{-s}\), \(H_n=Q^{-1}\circ T_n\), for real \(s>1\), and set \(L_n=\log q_n\). These are well-defined strictly decreasing positive Dirichlet profiles, with both \(Q\) and each tail mapping \((1,\infty)\) onto \((0,\infty)\).

Write the standard exponential integral
\[
E_1(a)=\int_1^\infty\frac{e^{-au}}u\,du
=\int_a^\infty\frac{e^{-v}}v\,dv,\qquad a>0.
\tag{2}
\]
There is a constant \(C\) independent of \(n\) and **of \(a>0\)** such that, for large \(n\),
\[
\boxed{\left|T_n(1+a/L_n)-\kappa E_1(a)\right|
\le C\,e^{-a}/L_n.}
\tag{3}
\]
Consequently, the calibrated relative-transition functions
\[
\Phi_n(a):=H_n(1+a/L_n)
\]
converge in \(C^1_{\rm loc}((0,\infty))\) to the nonconstant, increasing diffeomorphism
\[
\boxed{\Phi_Q(a)=Q^{-1}\!\left(\kappa E_1(a)\right):
(0,\infty)\longrightarrow(1,\infty).}
\tag{4}
\]
On each compact \(K\Subset(0,\infty)\), the convergence in values and first derivatives has error \(O_K(1/L_n)\), and
\[
\boxed{\Phi_Q'(a)=
-\frac{\kappa e^{-a}}{a\,Q'(\Phi_Q(a))}>0.}
\tag{5}
\]

This is an exact *critical scale classification*, not just a diagonal example. For any \(a_n>0\), formula (3) gives
\[
\Phi_n(a_n)\longrightarrow
\begin{cases}
1,&a_n\to0,\\
\Phi_Q(a),&a_n\to a\in(0,\infty),\\
+\infty,&a_n\to+\infty.
\end{cases}
\tag{6}
\]
The middle regime \(s-1\asymp1/\log q_n\) is the only one giving a finite interior transition limit.

All full transitions \(H_n\), their rescaled critical limits, and their comparisons are **exactly invariant under any common strictly monotone output recalibration** of \(Q\) and its tails, as in AF-550. The source coordinate \(s\), the index \(n\), and the declared scale of the critical window remain part of the representation.

## Proof: harmonic-source measure and controlled Laplace tails

Set \(L=L_n\). For \(u\ge1\), let
\[
V_n(u)=\sum_{\substack{k\ge n\\q_k\le e^{uL}}}\frac1{q_k}
=M_Q(e^{uL})-M_Q(q_n^-).
\tag{7}
\]
Since \(M_Q(q_n^-)=M_Q(q_n)-1/q_n\), (1) gives, **uniformly for every \(u\ge1\)**,
\[
V_n(u)=\kappa\log u+R_n(u),\qquad
\sup_{u\ge1}|R_n(u)|\le C/L.
\tag{8}
\]
Indeed, the first Mertens error is \(O((uL)^{-1})\), the second \(O(L^{-1})\), and the single lower-endpoint atom contributes \(1/q_n=O(L^{-1})\). The constancy of the finite part \(B_Q\) is what permits the uniform cancellation.

The weighted tail is a Stieltjes integral:
\[
T_n(1+a/L)=\int_{[1,\infty)}e^{-au}\,dV_n(u)
=a\int_1^\infty e^{-au}V_n(u)\,du.
\tag{9}
\]
The integration by parts is valid because \(V_n(u)=O(1+\log u)\) and \(a>0\). The identity
\[
a\int_1^\infty e^{-au}\log u\,du=E_1(a)
\tag{10}
\]
and (8) imply (3), with an error at most \(C aL^{-1}\int_1^\infty e^{-au}du=C e^{-a}/L\). Thus this uniform tail law requires only the Mertens-type harmonic measure, **not** any RH or zero-distribution input.

For derivative control on a fixed \(K\Subset(0,\infty)\), differentiate the absolutely convergent integral in \(a\) and integrate by parts again:
\[
\frac{d}{da}T_n(1+a/L)
=-\int_{[1,\infty)}u e^{-au}\,dV_n(u)
=\int_1^\infty(1-au)e^{-au}V_n(u)\,du.
\tag{11}
\]
Using (8), the integral of the remainder is \(O_K(1/L)\), while the \(\kappa\log u\) term is
\[
-\kappa\int_1^\infty e^{-au}du=-\kappa e^{-a}/a.
\tag{12}
\]
Since \(Q'<0\) everywhere on \((1,\infty)\), inverse-function calculus on the compact image of \(K\) turns (3) and (11)--(12) into (4)--(5) with \(C^1(K)\) error \(O_K(1/L_n)\).

The endpoint limits \(E_1(a)\to\infty\) as \(a\downarrow0\), and \(E_1(a)\to0\) as \(a\to\infty\), together with (3) and the monotone inverse \(Q^{-1}\), prove (6). Notice that (6) would not follow from fixed-\(n\) Taylor expansions whose error constants can grow with \(n\).

## What the limiting curve does and does not retain

The limiting curve is a complete reparameterization of the reference Dirichlet profile **once \(\kappa\) is fixed**:
\[
\boxed{Q(s)=\kappa E_1(\Phi_Q^{-1}(s)),\qquad s>1.}
\tag{13}
\]
This follows by applying \(Q\) to (4), since \(\Phi_Q\) is a diffeomorphism onto \((1,\infty)\).

Thus the universal remote-tail part of the critical experiment is \(\kappa E_1(a)\); all source-specific information in \(\Phi_Q\) enters through the retained reference inverse \(Q^{-1}\). For two systems with possibly different \(\kappa\)'s, their limiting curves coincide **if and only if** the normalized reference functions \(Q/\kappa\) coincide. At fixed \(\kappa\), distinct analytic Dirichlet profiles give distinct full critical curves, but a finite set of points on the curve cannot in general identify an arbitrary generator system.

Equation (13) is important negative context: the limiting curve is **not** an unexpected low-dimensional compression of prime identity. It is a calibration-invariant way to retain a complete reference profile on a nontrivial moving scale. The tail universality is compatible with many generalized-prime controls, and recovering the reference from all \(a>0\) is inverse-function algebra rather than an RH mechanism.

## Rational-prime test with source-independent index sampling

For ordinary primes \(q_n=p_n\), Mertens' reciprocal-prime theorem supplies (1) with \(\kappa=1\) and a finite constant \(B_Q\). Let
\[
P(s)=\sum_{p}p^{-s},\qquad
H_n=P^{-1}\circ\sum_{k\ge n}p_k^{-s}.
\]
Then
\[
H_n(1+a/\log p_n)
\longrightarrow P^{-1}(E_1(a)).
\tag{14}
\]
An audit must not silently treat \(\log p_n\) as free data supplied by a purportedly compressed representation. Fortunately the index alone suffices: the classical prime counting asymptotic implies
\[
\frac{\log p_n}{\log n}
=1+O\!\left(\frac{\log\log n}{\log n}\right).
\tag{15}
\]
Therefore the **index-only** experiment, with no externally supplied \(p_n\), obeys
\[
\boxed{H_n(1+a/\log n)
\longrightarrow P^{-1}(E_1(a))}
\quad\text{in }C^1_{\rm loc}((0,\infty)).
\tag{16}
\]
The compact-\(a\) error is \(O_K(\log\log n/\log n)\). Indeed, (16) is (3)--(5) evaluated at \(a_n'=a\log p_n/\log n\), and \(a_n'=a+O_K(\log\log n/\log n)\). This is the source-natural sampling law appropriate to a marked family indexed by \(n\).

AF-552 proves a fixed-index boundary dilation \(H_n'(1+)=\exp(\sum_{k<n}1/p_k)\) and shows the reciprocal-prime adjacent signal along \(x_n\log p_n\to0\). The critical regime here is instead \(x_n\log p_n\to a>0\). It cannot be obtained by assuming AF-552's fixed-\(n\) remainder is uniform at the boundary: the transition image now approaches an **interior** value \(P^{-1}(E_1(a))>1\), not the boundary point \(1\).

## Matched generalized-prime control and the exact metric tariff

Use the AF-551 source-natural finite-prefix control. Fix
\[
1<c<\frac{\log7}{\log5},\qquad
q_j=p_j^c\ (j=1,2,3),\qquad q_j=p_j\ (j\ge4).
\tag{17}
\]
The ordering and all sufficiently remote tails are preserved. Define
\[
Q_c(s)=P(s)+\sum_{j=1}^3(p_j^{-cs}-p_j^{-s}).
\tag{18}
\]
Both sources have the same Mertens coefficient \(\kappa=1\), and for \(n\ge4\) their tails \(T_n\) are exactly equal. Yet for every \(s>1\),
\[
Q_c(s)<P(s),
\qquad
Q_c^{-1}(y)<P^{-1}(y)\quad(y>0).
\tag{19}
\]
Their index-only critical limits are therefore
\[
\Phi_P(a)=P^{-1}(E_1(a)),\qquad
\Phi_c(a)=Q_c^{-1}(E_1(a)),
\quad\Phi_c(a)<\Phi_P(a).
\tag{20}
\]
For every compact interval \(K\Subset(0,\infty)\),
\[
\boxed{\delta_{c,K}:=\min_{a\in K}
[\Phi_P(a)-\Phi_c(a)]>0.}
\tag{21}
\]
Consequently, for sufficiently large \(n\), the **calibration-invariant transition values at the same index-only critical samples** differ by at least \(\delta_{c,K}/2\) uniformly on \(K\). This is a fixed interior target-coordinate margin against a finite-prefix generalized-prime control which matches all remote tails and the ordinary prime-counting law.

The margin is **not** a claim of an order-one lower bound in every horizontal-registration metric. In the raw input \(s\)-coordinate the critical window has width \(O(1/\log n)\), and
\[
\frac{d}{ds}H_n(1+a/\log n)
=(\log n)\Phi'_P(a)(1+o_K(1)).
\tag{22}
\]
An input-registration error \(\eta_n\) can therefore create an order-one critical-profile perturbation unless \(\eta_n\log n\to0\). The natural resolved representation is the rescaled \(a\)-coordinate, not the unweighted input-warp distance of AF-551. Likewise (21) concerns already-formed exact relative transitions, not arbitrary additive errors in the uncalibrated raw outputs before composing with \(Q^{-1}\).

## Prior art, falsification, and boundary

Mertens' second theorem (including the \(O(1/\log x)\) remainder) supplies the arithmetic input; the Laplace--Stieltjes rescaling and exponential integral are classical Abelian analysis. DLMF §6.2.1 gives \(E_1\) and its integral representation. AF-550 supplies the elementary complete common-calibration quotient and AF-551--AF-552 supply the two comparison regimes. No priority is claimed for reciprocal-prime Mertens asymptotics, exponential integrals, Laplace transforms, monotone inversion, Tauberian theory, or inverse-relative distribution/registration mathematics.

The useful Mathia-specific delta is the **uniform double-scaling transition theorem (3)**, its critical-window phase classification, the index-only prime specialization, and the honest target-metric comparison (21)--(22). It is a third conditioning channel of the full AF-550 quotient, beyond AF-551's exponentially weak far-right residual and AF-552's infinitesimal first boundary jets.

Decisive checks and nonclaims:

1. Differentiate (9) and verify (11)--(12), including its negative sign and the \(e^{-a}/a\) coefficient.
2. Test the lower-endpoint atom in (8). Dropping \(1/q_n\) does not change the limit but must be accounted for in the uniform error.
3. Verify that the finite-prefix control leaves \(\kappa=1\) and every \(T_n\) with \(n\ge4\) unchanged, while the strict inverse inequality (19) remains true.
4. Keep the critical source scale explicit: outside \(a_n=(s_n-1)\log q_n\to a\in(0,\infty)\), the transition limit hits the boundary or escapes to infinity.
5. Do not claim a prime-specific signature from the universal \(E_1\) tail, absolute-scale recovery without the sampling coordinate, or a uniform raw-output error theorem under unrestricted recalibration.
6. No RH zero exclusion, zero-density conclusion, or downstream spectral/positivity transport is provided.

## Consequence for Arithmetic Fidelity

The same complete nonlocal quotient has three genuinely different observation regimes. Far-right \(s\to\infty\) recovery can be exponentially ill-conditioned (AF-551); fixed-index near-boundary first jets detect finite prefixes (AF-552); and increasing-index critical samples retain a nontrivial interior transition curve with a matched-control gap at polynomial/logarithmic **input-resolution cost**. Its apparent robustness depends on the rescaled index coordinate and on retaining the reference inverse: the source-specific part is not created by the universal tail limit. Any RH-facing downstream representation must independently preserve this window and its calibration-invariant comparison geometry before the result becomes relevant to zeros.
