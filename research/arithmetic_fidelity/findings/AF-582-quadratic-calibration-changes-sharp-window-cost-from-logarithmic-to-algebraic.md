# AF-582 — Quadratic calibration changes sharp window cost from logarithmic to algebraic

## Status

EXACT-DERIVED · LITERATURE+DERIVED · POLYNOMIAL-NUISANCE · SHARP-RANGE-COST · PRIME-EDIT-MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

## A coordinate budget changes the known-degree recovery theorem

[[research/arithmetic_fidelity/findings/AF-581-known-polynomial-degree-restores-sharp-full-ray-adaptive-recovery|AF-581]] recovers the full-ray noise margin at every known polynomial degree using finite but unrestricted query locations. The first quadratic case already shows why the coordinate range is a separate resource: even complete observation on a bounded window loses a much larger fraction of the full-ray margin than under affine calibration.

Consider the binary analytic control
\[
 F_0(x)=0,\qquad F_1(x)=f(x)=xe^{1-x},\qquad
 y(x)=F_i(x)+b(x)+\eta(x),\quad
 b\in\Pi_r,\quad |\eta(x)|\le\varepsilon,
 \qquad 0<x\le B.
 \tag{1}
\]
Here \(r\) is a known nonnegative integer and \(\Pi_r\) denotes the real polynomials of degree at most \(r\). One unrestricted-coefficient polynomial is shared by all readings of an input; competing labels may use different polynomials. Let
\[
 E_r(B)=\inf_{p\in\Pi_r}\|f-p\|_{C[0,B]},\qquad
 \varepsilon_r(B)=E_r(B)/2.
 \tag{2}
\]
The latter is the supremal deterministic unique-identification radius with the whole window available. The continuous extension through zero makes the open-left and closed-window norms equal. The factor two comes from two error balls: their difference can have norm at most \(2\varepsilon\). On the full ray every nonconstant polynomial has infinite error against bounded \(f\); hence \(E_r(\infty)=1/2\) and \(\varepsilon_r(\infty)=1/4\) for every fixed \(r\).

**Theorem.** As \(B\to\infty\), the fractional losses of the full-ray radius satisfy
\[
 \boxed{1-4\varepsilon_1(B)
   =e^{1-B}+O(e^{2-2B}),}
 \tag{3}
\]
whereas
\[
 \boxed{1-4\varepsilon_2(B)
   =\frac{1+2\log B}{B^2}
       +O\!\left(\frac{(\log B)^2}{B^3}\right).}
 \tag{4}
\]
Both are exact best-approximation statements, rather than bounds for a chosen anchor scheme. Thus no additional samples or adaptivity inside this window can remove the loss in (4). Conversely three fixed readings for \(r=1\), and four for \(r=2\), approach the respective full-window radii. A query at zero in the extremal designs is replaced by a positive node tending to zero. All recovery radii are suprema; at a pairwise midpoint tie unique identification fails.

For a required retained fraction \(1-\delta\), define the minimum range
\[
 R_r(\delta)=\inf\{B>1:4\varepsilon_r(B)\ge1-\delta\}.
\]
Then
\[
 \boxed{R_1(\delta)=1+\log(1/\delta)+o(1),\qquad
 R_2(\delta)\sim\sqrt{\frac{\log(1/\delta)}{\delta}}.}
 \tag{5}
\]
The second law is a sharp resource obstruction even for binary identification. It is distinct from AF-581's multiway adaptive query-count gap and from AF-571's shrinking-window Taylor-jet law.

## Affine benchmark: an exact three-contact certificate

For \(B>1\), put \(s=e^{1-B}\). The chord-subtracted profile
\[
 H(x)=f(x)-sx
\]
is nonnegative on \([0,B]\), vanishes at both endpoints, and has its unique maximum at \(x_1\in(0,1)\), where
\[
 (1-x_1)e^{1-x_1}=s.
\]
Indeed \(f(x)/x=e^{1-x}\ge s\), and \(f'(x)-s\) crosses zero once before one and is negative thereafter. Writing \(w=1-x_1\), one has \(we^w=s\), so
\[
 2E_1(B)=H(x_1)=e^w(1-w)^2,
 \qquad p_1(x)=E_1(B)+sx.
 \tag{6}
\]
The residual \(f-p_1\) alternates as \(-E_1,+E_1,-E_1\) at \(0,x_1,B\) and stays between those values. Chebyshev alternation proves optimality. Since \(w=s+O(s^2)\), (6) gives (3).

## Quadratic certificate and its moving interior contact

For \(t>2\), define
\[
 v=e^{1-t},\qquad
 H_t(x)=f(x)-v\{(t+1)x-x^2\}.
 \tag{7}
\]
Then \(H_t(0)=H_t(t)=0\) and \(H_t'(t)=0\). There is a unique critical point \(x(t)\in(0,1)\), determined by
\[
 (1-x)e^{1-x}=v(t+1-2x).
 \tag{8}
\]
It is a strict maximum. To check the entire interval, not just the proposed contact nodes, use
\[
 H_t''(x)=e^{1-x}(x-2)+2v.
 \tag{9}
\]
This is strictly increasing on \([0,2]\), is negative at one and positive at two, and stays positive after two. Thus \(H_t'\) first decreases and then increases. Its only zeros on \([0,\infty)\) are \(x(t)\) and \(t\): \(H_t'(0)>0\), \(H_t'(1)<0\), and \(t>2\) is the second root. Consequently \(H_t\) rises from zero to
\[
 h(t):=H_t(x(t))>0,
\]
falls to zero at \(t\), and increases thereafter.

For all sufficiently large \(B\), choose \(t=t_B\) by
\[
 h(t)=H_t(B)=f(B)+e^{1-t}\{B^2-(t+1)B\},
 \qquad \log B<t<3\log B<B.
 \tag{10}
\]
Existence and uniqueness in this bracket do not rely on a numerical solver. At \(t=\log B\) the right-hand side grows like \(eB\), whereas at \(t=3\log B\) it tends to zero; \(h(t)\to1\). Moreover, differentiating at the stationary maximum gives
\[
 h'(t)=e^{1-t}x(t)\{t-x(t)\}>0,
 \qquad
 \partial_t H_t(B)=e^{1-t}B(t-B)<0.
 \tag{11}
\]
There is exactly one crossing. With \(E=h(t_B)/2\), the polynomial
\[
 p_2(x)=E+e^{1-t_B}\{(t_B+1)x-x^2\}
 \tag{12}
\]
has residual values \(-E,+E,-E,+E\) at
\[
 0,\quad x(t_B),\quad t_B,\quad B.
 \tag{13}
\]
The monotonicity established using (9) proves \(|f-p_2|\le E\) everywhere. Four-point alternation therefore proves that (12) is the best quadratic approximant and \(E_2(B)=h(t_B)/2\).

The decisive structural feature is the extra interior contact \(t_B\). It moves logarithmically far into the exponentially decaying source tail, while the last contact remains at the allowed boundary \(B\). Merely replacing infinite anchors by a large finite coordinate misses this tail-contact optimization.

## Derivation of the range law

From (8), as \(t\to\infty\),
\[
 x(t)=1+O(vt),\qquad
 h(t)=1-vt+O(v^2t^2),\qquad v=e^{1-t}.
 \tag{14}
\]
The second estimate follows by expanding about \(x=1\): \(H_t(1)=1-vt\), \(H_t'(1)=-v(t-1)\), and the displacement of the maximizing point is \(O(vt)\), with bounded second derivative there.

The bracket in (10) first gives \(t=O(\log B)\), \(h(t)\to1\), and hence \(vB^2\to1\). Feeding this into (10) and then taking logarithms yields
\[
 v=B^{-2}\{1+O(\log B/B)\},\qquad
 t_B=1+2\log B+O(\log B/B).
 \tag{15}
\]
Equations (14)--(15) imply
\[
 2E_2(B)=h(t_B)
 =1-\frac{1+2\log B}{B^2}
   +O((\log B)^2/B^3),
\]
which proves (4). The errors \(E_r(B)\) are nondecreasing in \(B\). The exact formulas also give strict increase for sufficiently large \(B\); in the quadratic case this follows from (11) and \(\partial_BH_t(B)>0\). Inverting (3)--(4) proves (5), including its leading constant.

## Fixed probes and transfer to prime-edit controls

At the \(r+2\) alternation nodes, normalize the divided-difference weights to total variation one:
\[
 \lambda_j=\frac{\prod_{k\ne j}(x_j-x_k)^{-1}}
                  {\sum_l|\prod_{k\ne l}(x_l-x_k)^{-1}|}.
 \tag{16}
\]
They annihilate \(\Pi_r\), and their alternating signs match the residual up to a common sign. Therefore \(|\sum_j\lambda_j f(x_j)|=E_r(B)\), while observation error changes the contrast by at most \(\varepsilon\). The two labels are separated whenever \(2\varepsilon<E_r(B)\). Moving the zero node slightly right preserves the limit. At most \(r+1\) distinct observations admit a polynomial-interpolation alias even adaptively, by feeding a fixed zero transcript and fitting each label's polynomial. Thus the respective three- and four-probe counts are minimal for deterministic guaranteed recovery in this binary experiment.

For the registered prime-edit family, write
\[
 P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s},\quad
 Q_p(s)=P(s)-p^{-s}+(p+1)^{-s},\quad
 \Phi_p(a)=Q_p^{-1}(E_1(a)),\quad
 E_1(a)=\int_a^\infty e^{-u}\,du/u.
\]
For odd primes \(p<q\), let \(D_{p,q}=\sup_{a>0}(\Phi_q-\Phi_p)(a)\), \(c=e^{B_1}\), where \(B_1\) is the prime-reciprocal Meissel--Mertens constant, and define
\[
 g_{p,q}(x)=\frac{(\Phi_q-\Phi_p)(x/(c\log p))}{D_{p,q}}.
\]
[[research/arithmetic_fidelity/findings/AF-559-all-pair-prime-edit-separation-has-uniform-sharp-critical-window|AF-559]], equation (3), supplies
\[
 \alpha_p:=\sup_{q>p}\sup_{x>0}|g_{p,q}(x)-f(x)|\longrightarrow0.
 \tag{17}
\]
Here the first supremum is over larger odd rational primes. Rescaling the coordinate and dividing by \(D_{p,q}\) maps unrestricted \(\Pi_r\) bijectively to itself. Distance to a fixed subspace is 1-Lipschitz, so the actual binary full-window radius \(\varepsilon_{r;p,q}(B)\), on \(0<a\le B/(c\log p)\), satisfies
\[
 \left|\frac{\varepsilon_{r;p,q}(B)}{D_{p,q}/4}
                 -2E_r(B)\right|\le2\alpha_p.
 \tag{18}
\]
This bound is uniform in \(q>p\) and \(B>0\). The denominator is the actual full-ray polynomial-quotient radius from AF-581. The same TV-one contrast nodes give an achievable radius at least \(D_{p,q}(E_r(B)-\alpha_p)/2\), as a supremum with positive nodes. Thus the profile's finite-probe certificate transfers as well as its full-window obstruction, without assuming derivative convergence.

For fixed \(B\), (18) proves convergence to the exact profile ratio. For growing \(B\), a sufficient condition for (18) to transfer the leading loss in (4) is \(\alpha_p=o(\log B/B^2)\); for its affine counterpart, \(\alpha_p=o(e^{1-B})\) suffices. These are sufficient uniform-error conditions, not claimed necessary conditions on the quotient. The unquantified convergence in (17) permits suitable diagonal choices, but gives no explicit joint prime/range/precision rate. Taking the remote-prime limit first and the large-window limit second is valid. No unrestricted joint-limit conclusion follows from this estimate.

## Prior art, validation and boundaries

Chebyshev alternation, divided-difference annihilators and the noise-ball quotient are classical. [NIST DLMF §3.11(i)](https://dlmf.nist.gov/3.11.i) states the alternation certificate. Sachdeva and Vishnoi, [*Faster Algorithms via Approximation Theory*](https://sachdevasushant.github.io/pubs/fast-algos-via-approx-theory.pdf), §§1 and 4, give the classical uniform-approximation setting and interval/degree tradeoffs for the exponential. Dette and Titoff, [*Optimal discrimination designs*](https://arxiv.org/abs/0908.1912), connect statistical model discrimination to best uniform approximation. None of those general tools is claimed as new. The derived contribution here is the explicit quadratic tail-contact certificate, its sharp bounded-range loss, and the error-controlled application to the existing prime-edit profile. No priority claim is made for the standalone approximation formulas.

A scratch-only Python `decimal` check at 70-digit precision solved (8)--(10) for \(B=10,20,100,1000,10^4,10^6\). It checked all four residual contacts, all three polynomial-annihilation moments, and the dual contrast identity to absolute error below \(10^{-60}\), plus a 4,002-point residual check per window. The ratio of the exact loss to \((1+2\log B)/B^2\) was respectively approximately \(1.80054,1.45128,1.11018,1.01494,1.00194,1.000029\). Five affine windows separately checked (6). These are numerical normalization and formula checks, not interval-certified proofs; global optimality rests on (9)--(13) and alternation, and the prime transfer rests on (17)--(18).

The result concerns absolute adversarial errors and one shared, known-degree calibration. It does not bound finite-precision arithmetic cost, relative errors, unknown degree, or separately changing calibration. The sharp formulas are binary; they do not assert one common optimal design for arbitrary multiway source sets. The quadratic certificate is proved for sufficiently large windows, while AF-571 covers a different small-window regime. No claim is made for higher-degree range asymptotics.

The general control (1) shows the effect is not arithmetic-specific. In the arithmetic instantiation, the sources are generalized-prime systems indexed by rational-prime edit locations. Their separation does not certify ordinary-prime provenance or imply RH. The concrete consequence for this line is that a supplied polynomial degree restores finite-query recovery but does not make the accessible coordinate range free: the first quadratic nuisance already imposes an algebraic range cost for a near-full noise margin.
