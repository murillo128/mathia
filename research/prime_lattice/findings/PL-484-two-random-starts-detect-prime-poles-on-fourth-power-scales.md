# PL-484 — Two random starts detect prime poles on fourth-power scales

**Evidence/status:** LITERATURE+DERIVED / EXACT CONDITIONAL TRANSFER;
CLASSICAL PROBABILITY; NO EXTERNAL NOVELTY CLAIM.
The source is the fixed von Mangoldt sequence; only the observation
locations are random. No prime-energy ceiling is established.

## Claim and scale quantifiers

For \(k\ge3\), fix \(X_k=k^4\), and at \(X=X_k\) put
\[
a_n=\Lambda(n)\mathbf1_{n\equiv1\ (5)},\quad
S_L(j)=\sum_{j<n\le j+L}a_n,\quad I_X=\{X,\ldots,2X-1\},
\]
\[
L_1=H=\lfloor X/20\rfloor,\qquad L_2=\lfloor\sqrt2H\rfloor.
\tag{1}
\]
In each channel draw two independent uniform starts
\(R_{i,k,1},R_{i,k,2}\in I_X\), **with replacement**. All draws
are independent across channels and scales. Fix this product law before
examining source values or zeros, and retain coincident draws. Define
\[
V_i(k)=\min_{c\in\mathbb R}\frac12\sum_{a=1}^2
       |S_{L_i}(R_{i,k,a})-c|^2
       =\frac14|S_{L_i}(R_{i,k,1})-S_{L_i}(R_{i,k,2})|^2.
\tag{2}
\]

There is an event of probability one on which **joint GRH for zeta and
the three primitive nonprincipal mod-5 Dirichlet functions is equivalent
to**
\[
\boxed{\text{for every }\varepsilon>0,\qquad
 V_i(k)\ll_{\varepsilon,\omega}X_k^{1+\varepsilon}
 \quad(i=1,2;\ \text{all sufficiently large }k).}
\tag{3}
\]
Constants and onset may depend on the sampling outcome. The whole
sequence is prescribed; (3) does not allow a favorable unbounded
subsequence selected after observing the energies.

More precisely, if any of these functions has a nontrivial zero
\(\rho=\beta+i\tau\), \(\beta>1/2\), then for every
\(1/2<\gamma<\beta\),
\[
\Pr\{\max_i V_i(k)>X_k^{2\gamma}\}
 \gg_\rho \frac{X_k^{-(1-\beta)/2}}{\sqrt{\log(3X_k)}}
\tag{4}
\]
for all sufficiently large \(k\), with onset also depending on
\(\gamma\). Almost surely these exceedances occur infinitely often,
simultaneously for all such zeros and exponents.

This changes the observation/scale trade from
[[research/prime_lattice/findings/PL-482-small-empirical-energy-permits-quarter-power-prime-observations|PL-482]]:
two starts per channel suffice with mandatory fourth-power-scale
coverage, while PL-482 uses quarter-power-many observations to permit any
common unbounded scale set. The finite lemma and independent-repetition
mechanism are already in the explicitly granted
[[research/mobius_cancellation/findings/MC-539-two-random-starts-detect-mobius-poles-on-fourth-power-scales|MC-539]].
The destination transfer below uses the prime source's growing jump
bound, positive pole residues, and its own GRH converse; it imports no
Möbius analytic estimate.

## 1. Reconstruct the finite pair-tail lemma

For a real population \(u_1,\ldots,u_N\) with
\(|u_{j+1}-u_j|\le A\), let \(J,K\) be independent uniform indices,
and set
\[
D=\mathbb E|u_J-u_K|,\qquad p_T=\Pr(|u_J-u_K|>T),\quad T\ge0.
\]
Then, for any \(A\ge0\), including a size-dependent bound,
\[
\boxed{D\le2T+ANp_T^2+Ap_T.}
\tag{5}
\]

Averaging over the second index gives an anchor \(a\) with
\(B:=\#\{j:|u_j-u_a|>T\}\le Np_T\). Its good set
\(G=\{j:|u_j-u_a|\le T\}\) contains \(a\), and bounded jumps give
\[
|u_j-u_a|\le T+A\operatorname{dist}(j,G).
\]
A complementary interval of length \(b\) contributes at most
\(b(b+1)/2\) to the sum of distances, also when it touches an endpoint.
Hence
\[
\sum_j\operatorname{dist}(j,G)\le B(B+1)/2,
\qquad
D\le\frac2N\sum_j|u_j-u_a|
 \le2T+\frac A N B(B+1),
\]
which proves (5). This includes constant populations, ties, \(N=1\),
and the diagonal pairs \(J=K\). Translation of every value does not
change the statement. Neither a population variance nor its mean needs
to be estimated.

If \(D\ge cX^\beta\), \(N=X\), \(A=\log(3X)\), and
\(T=2X^\gamma\) with \(\gamma<\beta\), then eventually
\(Q:=(D-2T)/A\gg_c X^\beta/\log(3X)\to\infty\).
Equation (5) gives \(Xp_T^2+p_T\ge Q\). Since \(p_T\le1\),
\[
p_T\ge\sqrt{Q/(2X)}
 \gg_c X^{-(1-\beta)/2}/\sqrt{\log(3X)}.
\tag{6}
\]
The logarithmic cost is retained, rather than treating prime jumps as
uniformly bounded in \(X\).

## 2. The actual prime pole test forces dispersion on every block

Fix \(1/2<\sigma_0<\beta\). PL-471, Sections 1–3, supplies
a fixed compact smooth mean-zero test
\(\varphi\in C_c^\infty((4/3,5/3))\) with
\[
\sum_n a_n\varphi(n/X)
 =-w_\rho X^\rho+O_\varphi(X^{\sigma_0}),\qquad
w_\rho=\tfrac14\sum_\chi m_\chi(\rho)>0.
\tag{7}
\]
Here the sum is over the four functions in the claim. All zeros with
real part exceeding \(\sigma_0\) are annihilated except at \(\rho\). The fixed
modulus zero-density theorem and logarithmic-derivative contour bounds
are essential arithmetic inputs. The complex test retains a single
mode, so its modulus has no cosine zeros. Coincident zeros add with
positive multiplicities; logarithmic derivatives have simple poles,
with no reciprocal-zeta multiplicity logarithm.

The compact two-box inverse in PL-475, Sections 1–4, gives mean-zero
tests \(f_{i,h}\), \(h=H/X\), supported in a fixed compact subset of
\((1,2)\), with uniformly bounded sup and first derivative norms. As
reconstructed in PL-482, Section 3, their pairings satisfy
\[
P_i(X)=\frac1{L_i}\int_X^{2X}S_{L_i}(y)f_{i,h}(y/X)\,dy,
\]
\[
P_1(X)+P_2(X)
 =-w_\rho X^\rho+O_\varphi(X^{\sigma_0})+O_\varphi(\log(3X)).
\tag{8}
\]
Rounding the second length changes the normalized width by less than
\(X^{-1}\). Its target error is \(O(X^{-1})\), and summing against
\(O(X)\) coefficients bounded by \(\log(3X)\) gives the last error.
No exact inverse for the rational rounded length ratio is assumed.

For each channel set
\[
D_i(X)=X^{-2}\sum_{j,r\in I_X}|S_{L_i}(j)-S_{L_i}(r)|.
\]
Integer-length window sums are constant on cells \([j,j+1)\). The
weights \(w_{i,j}=\int_j^{j+1}f_{i,h}(y/X)\,dy\) have exactly
zero sum and bounded magnitude. If \(\bar u_i\) is the population
mean, Jensen's inequality gives
\(X^{-1}\sum_j|S_{L_i}(j)-\bar u_i|\le D_i(X)\). Since
\(L_i\asymp X\),
\[
|P_i(X)|
 =\left|L_i^{-1}\sum_jw_{i,j}(S_{L_i}(j)-\bar u_i)\right|
 \ll_\rho D_i(X).
\]
Thus (8) implies
\[
D_1(X)+D_2(X)\gg_\rho X^\beta
\tag{9}
\]
at every sufficiently large integer scale. The channel carrying the
lower bound can change with \(X\).

Finally,
\[
S_L(j+1)-S_L(j)=a_{j+L+1}-a_{j+1},\qquad
|S_L(j+1)-S_L(j)|\le\log(3X).
\tag{10}
\]
Both terms lie between zero and \(\log(3X)\), so a factor two is
unnecessary. This includes prime powers and windows crossing \(2X\).
Apply (6) to a channel with \(D_i\gg_\rho X^\beta\). Its
pair-tail event at \(T=2X^\gamma\) is exactly
\(V_i>X^{2\gamma}\), by (2). The union of the two channel events
has at least that probability, proving (4).

## 3. Independent repetition and the separate converse

For fixed \(\rho,\gamma\), the events
\(E_k=\{\max_i V_i(k)>X_k^{2\gamma}\}\) are independent:
the populations are deterministic and the observation draws at distinct
scales are independent, even though the arithmetic windows overlap.
At \(X_k=k^4\), (4) gives the divergent lower sum
\[
\sum_k\Pr(E_k)\gg_\rho
 \sum_k\frac{k^{-2(1-\beta)}}{\sqrt{\log(3k^4)}}=\infty,
 \qquad 2(1-\beta)<1.
\tag{11}
\]
The second Borel–Cantelli lemma applies. Directly, for every \(K\),
\[
\Pr\Bigl(\bigcap_{k=K}^{n}E_k^c\Bigr)
 =\prod_{k=K}^{n}(1-\Pr(E_k))
 \le\exp\Bigl(-\sum_{k=K}^{n}\Pr(E_k)\Bigr)\longrightarrow0.
\]
Intersect over the countably many zeros and rational
\(\gamma\in(1/2,\beta)\). For a real exponent choose a larger
rational one below \(\beta\). This supplies one probability-one
event with every asserted exceedance statement. It is an event for the
fixed source, not a uniform guarantee over sources chosen after sampling.

If (3) holds and a strict-right zero exists, choose
\(1/2<\gamma<\beta\) and \(0<\varepsilon<2\gamma-1\).
Along the infinitely many exceedances,
\(\max_i V_i(k)/X_k^{1+\varepsilon}\to\infty\), contradicting
even outcome-dependent constants in (3). Functional-equation symmetry
of the four-function family then gives joint GRH.

Conversely, joint GRH for these four functions gives
\[
\psi(x;5,1)=x/4+O(\sqrt x\log^2(3x)).
\tag{12}
\]
The classical bound is stated in Lee, Corollary 1.1, equation (4),
and obtained character by character in Section 5 (source 144).
Only these four functions' hypotheses are needed at modulus five.
Every queried endpoint is \(O(X)\), so
\(|S_{L_i}(R)-L_i/4|\ll\sqrt X\log^2(3X)\) for all starts.
Using \(c=L_i/4\) in (2) proves
\(V_i(k)\ll X_k\log^4(3X_k)\ll_\varepsilon X_k^{1+\varepsilon}\)
for every outcome. This converse does not transfer a complete mean
square to a sparse sample.

More generally the argument works for any fixed increasing integer
sequence \(X_k\to\infty\) with
\[
\sum_k X_k^{-d}=\infty\qquad\text{for every }0<d<1/4.
\tag{13}
\]
For a selected zero, choose \((1-\beta)/2<d<1/4\); the rate in
(4) eventually dominates a constant times \(X_k^{-d}\). Thus the
logarithm does not change this sufficient coverage condition.

## 4. Generic controls and the exact evidence boundary

The fourth-power boundary belongs to this generic dispersion-and-jump
argument, not to an optimality theorem for primes. For \(a>4\), set
\(X_k=\lceil k^a\rceil\), choose \(3/4<\kappa<1-1/a\), and
prescribe both populations before sampling as
\[
u_j=(M_k-|j-\lfloor3X_k/2\rfloor|)_+,
\qquad M_k=\lfloor X_k^\kappa\rfloor.
\tag{14}
\]
These tents have jumps at most one, mass \(M_k^2\), and at least
\(X_k/2\) zero entries eventually. Pairs with exactly one zero entry
give \(D_i\ge M_k^2/X_k\asymp X_k^{2\kappa-1}\), a strict
super-square-root floor at every scale. Yet the four draws hit the
nonzero support with probability at most \(8M_k/X_k\), whose sum
converges because \(a(\kappa-1)<-1\). Almost surely both energies
are eventually zero. These are fixed population families; no common
prime coefficient realization or arithmetic pole formula is asserted.

The same tents on \(X_k=k^4\), with \(3/4<\kappa<1\), also
explain the favorable-subsequence failure of the proof: the probability
that all four draws miss the support tends to one. These independent
miss events occur infinitely often almost surely, so a favorable
unbounded set with both energies zero coexists with the infinitely many
large detections forced by (5). This is a generic counterexample to
weakening the scale quantifier, not a claim about favorable subsequences
of the canonical prime source.

PL-483's fixed positive prime-supported reweightings have an additional
common-source constraint, but their invisibility is established only
on geometric scales. Their sampled energies equal the baseline's
unknown energies, and their modified source need not retain (7).
Consequently neither those controls nor the tents refute (3), prove
optimal actual-prime sampling, or remove the required arithmetic input.
Phase twists and generalized-prime systems likewise do not inherit (7)
or (12) from bounded jumps or lattice geometry alone.

The finite lemma, classical Lipschitz hidden-area mechanism and
independent repetition are not new. Baran–Demaine–Katz, Section 2
(source 152), provides the neighboring Lipschitz integration framework;
Durrett, Theorem 2.3.7 (source 153), gives the exact probability principle.
Zaccagnini, Section 3.3 (source 123), compares strong complete Selberg
integrals with zero-free regions. That full-integral result is distinct
from the two-start observation law and prescribed scale sequence here.
The local mathematical delta is the proved prime transfer of MC-539's
mechanism, including the logarithmic jump loss and the independent
mod-5 converse. No external priority, new probabilistic principle, or
new source of prime cancellation is claimed.

An exact rational self-check covered 3,280 populations of
sizes one through eight, starting at 17 with increments in
\(\{-3,0,2\}\). For 49,820 half-integer threshold cases it checked
the anchor, endpoint-gap distance bound and (5), each with three valid
jump envelopes, including enlarged size-independent envelopes. Another
186,988 ordered sample pairs checked the exact sample-mean factor in
(2); 64 two-channel probability cases checked the union bound, and four
rational choices \(a>4\) checked the strict tent exponent interval.
These are finite bookkeeping checks; the displayed proof establishes
the asymptotic transfer. No numerical prime-energy estimate, Lean
verification, or independent adversarial approval is asserted.

This criterion leaves the actual energy bound unproved. It gives no
finite GRH decision procedure, effective zero-uniform onset, full
population variance, covariance-cone positivity, or computational
speedup. There are \(O(Y^{1/4})\) window queries through scale \(Y\),
and evaluating each window has a separate cost. Cross-scale independence
and prescribed coverage are load-bearing. The reused elementary finite
lemma offers no separate high-value formalization target.
