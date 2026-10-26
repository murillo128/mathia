# PL-482 — Small empirical energy permits quarter-power prime observations

**Evidence/status:** LITERATURE+DERIVED / EXACT CONDITIONAL TRANSFER;
CLASSICAL CONCENTRATION; NO EXTERNAL NOVELTY CLAIM.
Only observation locations are random. No actual-prime energy ceiling,
unconditional zero exclusion, or complete second-moment recovery is proved.

## Claim and quantifiers

For each integer \(X\ge40\), put
\[
a_n=\Lambda(n)\mathbf1_{n\equiv1\ (5)},\qquad
S_L(j)=\sum_{j<n\le j+L}a_n,\qquad I_X=\{X,\ldots,2X-1\},
\]
\[
H=\lfloor X/20\rfloor,\quad L_1=H,\quad
L_2=\lfloor\sqrt2 H\rfloor,\quad q=\lceil X^{1/4}\rceil.
\tag{1}
\]
In each channel draw \(2q\) independent uniform starts
\(R_{i,X,a}\in I_X\), **with replacement**, independently across
channels and integer scales. Fix this product sampling law before
consulting the fixed prime source or its zeros. Define
\[
V_i(X)=\min_{c\in\mathbb R}\frac1{2q}
       \sum_{a=1}^{2q}|S_{L_i}(R_{i,X,a})-c|^2.
\tag{2}
\]
Repeated draws retain their multiplicities; the minimizer is the sample
mean, independently in each channel.

There is an event \(\Omega_*\) of probability one such that, for every
\(\omega\in\Omega_*\), **joint GRH for zeta and the three primitive
nonprincipal Dirichlet functions modulo 5 is equivalent to**: there is
one unbounded set \(\mathcal X\) of integer scales on which, for every
\(\varepsilon>0\),
\[
\boxed{V_i(X)\ll_{\varepsilon,\omega}X^{1+\varepsilon},
       \qquad i=1,2.}
\tag{3}
\]
The set may depend on the observations, but is common to both channels
and fixed before epsilon varies. Constants and thresholds may depend
on epsilon and the outcome, uniformly along that set.

More precisely, for every hypothetical nontrivial zero
\(\rho=\beta+i\gamma\), \(\beta>1/2\), of any of these functions,
on the same event and at every sufficiently large integer scale,
\[
\boxed{\sqrt{V_1(X)}+\sqrt{V_2(X)}
       +\sqrt X(\log X)^3\gg_\rho X^\beta.}
\tag{4}
\]
The analytic constant depends on the full zero set through the pole
test; the onset can also depend on the outcome. There is no
multiplicity-dependent logarithm on the right.

Relative to
[[research/prime_lattice/findings/PL-481-stratified-random-starts-retain-the-prime-variance-criterion|PL-481]],
this uses the small observed energy itself and changes the sampling law
to uniform independent draws. The sufficient observation count becomes
quarter-power rather than cube-root. The finite argument is the
destination reconstruction of Sections 1–2 of the explicitly granted
[[research/mobius_cancellation/findings/MC-537-small-sampled-energy-permits-quarter-power-mobius-observations|MC-537]];
its Möbius analytic inputs are not used. The proof below is self-contained
apart from the existing local prime pole tests and the classical GRH
prime-counting estimate.

## 1. Sample energy bounds mean absolute dispersion

Let \(u_1,\ldots,u_N\) be a fixed real population with
\(|u_{j+1}-u_j|\le A\). From \(2q\) independent uniform draws
with replacement obtain values \(Y_a\), and set
\[
V=\min_c\frac1{2q}\sum_a(Y_a-c)^2,\quad
D=\frac1{N^2}\sum_{j,k}|u_j-u_k|,\quad
B=\max_j u_j-\min_j u_j.
\]
For every \(t>0\), with
\(r=\min\{N,\lceil Nt/(2q)\rceil\}\), with probability at least
\(1-3e^{-t}\),
\[
D\le\left(4+\frac{16t}{\sqrt q}\right)\sqrt V
       +\frac{16Art}{q}
\le\left(4+\frac{16t}{\sqrt q}\right)\sqrt V
       +\frac{8ANt^2}{q^2}+\frac{16At}{q}.
\tag{5}
\]
This permits \(A\) to depend on the population size.

To prove it, pair the draws and put
\(Z_b=|Y_{2b-1}-Y_{2b}|\), \(\bar Z=q^{-1}\sum_bZ_b\).
These variables are independent, lie in \([0,B]\), and have mean
\(D\). When \(B>0\), convexity gives
\(e^{-z}\le1-(1-e^{-1})z\) for \(0\le z\le1\).
Exponential Markov therefore yields
\[
\Pr\{\bar Z\le D/2\}
\le \exp\bigl(-(1/2-e^{-1})qD/B\bigr)
\le e^{-qD/(8B)}.
\]
Consequently, outside an event of probability at most \(e^{-t}\),
\[
D\le2\bar Z+8Bt/q.
\tag{6}
\]
For \(D\le8Bt/q\) this is automatic; otherwise failure is covered
by the displayed lower-tail estimate. A constant population has
\(B=D=V=0\) and needs no division by \(B\).

Fix one maximizing and one minimizing index before sampling. Around
each choose any consecutive \(r\)-point set containing it. Every
index in that set is within \(r-1\) of the extremum, including when
the extremum is an endpoint. If \(r<N\), the probability of missing
either set is at most
\[
2(1-r/N)^{2q}\le2e^{-t};
\]
if \(r=N\), neither is missed. On the two-hit event,
\[
B\le\max_aY_a-\min_aY_a+2Ar.
\tag{7}
\]
For the sample mean \(\bar Y\), Cauchy–Schwarz and the two extreme
deviations give the deterministic inequalities
\[
\bar Z\le q^{-1}\sum_a|Y_a-\bar Y|\le2\sqrt V,
\qquad
\max_aY_a-\min_aY_a\le2\sqrt{qV}.
\tag{8}
\]
Intersect (6) and (7), substitute (8), and use a union bound to prove
(5). The concentration step uses the **fixed true range** \(B\);
the sampled bound for that range is substituted only afterwards.
No independence between the two events is required.

For the population mean \(\bar u\), Jensen gives
\(N^{-1}\sum_j|u_j-\bar u|\le D\). Thus, simultaneously for
every set of complex weights satisfying \(\sum_jw_j=0\) and
\(|w_j|\le F\), and every \(L>0\),
\[
\left|\frac1L\sum_jw_ju_j\right|\le\frac{FN}{L}D.
\tag{9}
\]
This recovers bounded mean-zero pairings, without estimating either
mean and without asserting control of the population variance. Since
(9) is deterministic once \(D\) is bounded, there is no union over
weights or zero tests.

## 2. Prime jumps and one probability-one event

For the two populations in (1),
\[
S_L(j+1)-S_L(j)=a_{j+L+1}-a_{j+1},\qquad
|S_L(j+1)-S_L(j)|\le\log(3X)=A_X.
\tag{10}
\]
Both coefficients are nonnegative and at most \(\log(3X)\);
a factor two is unnecessary. This identity includes prime powers
and windows crossing \(2X\).

Apply (5) with \(N=X\), \(q=\lceil X^{1/4}\rceil\), and
\(t=4\log X\). Here \(t/\sqrt q\) is eventually bounded,
and the two remainder terms are
\(O(\sqrt X(\log X)^3)\). Writing
\[
D_i(X)=X^{-2}\sum_{j,k\in I_X}
              |S_{L_i}(j)-S_{L_i}(k)|,
\]
we obtain, with failure probability at most \(6X^{-4}\) for both
channels together,
\[
D_i(X)\ll\sqrt{V_i(X)}+\sqrt X(\log X)^3,
\qquad i=1,2.
\tag{11}
\]
The first Borel–Cantelli lemma defines \(\Omega_*\) so that (11)
holds at every sufficiently large integer scale. Cross-scale
independence is not needed for this step. The event concerns only
dispersion of the two fixed prime populations; by (9) it works for
all bounded mean-zero tests at once. It is not a uniform event over
sources chosen after the samples.

## 3. Compose with the actual prime pole tests

Fix \(\rho=\beta+i\gamma\) and \(1/2<\sigma_0<\beta\).
[[research/prime_lattice/findings/PL-471-sparse-zero-annihilators-force-prime-variance-on-every-large-block|PL-471]],
Sections 1–3, constructs a fixed compact smooth mean-zero test
\(\varphi\), supported inside \((4/3,5/3)\), with
\[
\sum_n a_n\varphi(n/X)
=-w_\rho X^\rho+O_\varphi(X^{\sigma_0}),\qquad
w_\rho=\tfrac14\sum_\chi m_\chi(\rho)>0.
\tag{12}
\]
The index \(\chi\) here denotes zeta and the three primitive
nonprincipal mod-5 factors. The full power-sparse zero set supplies the
annihilator; logarithmic-derivative growth justifies its explicit
formula. Coincident zeros contribute positive multiplicities. Multiple
zeros still give simple logarithmic-derivative poles, so (12) has no
reciprocal-zeta multiplicity logarithm.

[[research/prime_lattice/findings/PL-475-two-box-lengths-force-paired-macroscopic-prime-variance|PL-475]],
Sections 1–4, supplies deterministic tests \(f_{i,h}\),
\(h=H/X\), with zero integral, support in one fixed compact subset
of \((1,2)\), and uniformly bounded sup and first derivative norms.
Its compact two-box inverse, including integer rounding, gives
\[
P_i(X)=\frac1{L_i}\int_X^{2X}S_{L_i}(y)f_{i,h}(y/X)\,dy,
\]
\[
P_1(X)+P_2(X)
=-w_\rho X^\rho+O_\varphi(X^{\sigma_0})+O_\varphi(\log X).
\tag{13}
\]
The last error is essential: \(L_2/X\) differs from \(\sqrt2h\)
by less than \(X^{-1}\), giving target error \(O(X^{-1})\).
Summing against \(0\le a_n\le\log n\) on \(O(X)\) indices
costs \(O(\log X)\). No exact inverse for a rational rounded
length ratio is asserted.

For integer lengths, \(S_L(y)=S_L(j)\) on \([j,j+1)\).
Set \(w_{i,j}=\int_j^{j+1}f_{i,h}(y/X)\,dy\).
Their sum is exactly zero and their magnitudes are uniformly bounded.
Since \(L_i\asymp X\), (9) and (11) bound each \(|P_i(X)|\)
by a constant depending on the test times
\(\sqrt{V_i(X)}+\sqrt X(\log X)^3\). Equation (13) has modulus
at least \(w_\rho X^\beta/2\) eventually, proving (4).

On any outcome in \(\Omega_*\), suppose (3) holds. For a strict-right
zero choose \(0<\varepsilon<2\beta-1\). Both square-root energy
terms and the recovery remainder in (4) are \(o(X^\beta)\), a
contradiction along the common unbounded set. Functional-equation
symmetry of the four-function family gives joint GRH. The event was
already fixed at all large integer scales before selecting the set,
epsilon, zero or weights.

Conversely, joint GRH gives the classical fixed-modulus estimate
\[
\psi(x;5,1)=x/4+O(\sqrt x\log^2(3x));
\tag{14}
\]
see [Lee (2023), Corollary 1.1, equation (4), and its character-wise
proof](https://arxiv.org/pdf/2301.13457), source 144. Only these four
functions' GRH is needed. At every sampled start, (14) implies
\[
|S_{L_i}(R_{i,X,a})-L_i/4|\ll\sqrt X\log^2(3X).
\]
Using \(c=L_i/4\) in (2) proves
\(V_i(X)\ll X\log^4(3X)\ll_\varepsilon X^{1+\varepsilon}\)
for every outcome and every large integer scale. This converse does
not transfer a full mean square to a sparse sample.

## Prior art, falsification controls and boundary

The exponential-moment argument in (6) is classical concentration;
source 150 records Hoeffding's foundational paper. The neighboring
[Maurer–Pontil empirical Bernstein bound, Theorem 4](https://www.cs.mcgill.ca/~colt2009/papers/012.pdf),
source 151, exploits observed variance on a fixed bounded range.
It is not applied with a random range here. Equations (6)–(8) supply
that extra bookkeeping explicitly. The bounded-jump recovery is
generic, and its finite lemma is already present in MC-537.

Classical Lipschitz integration and hidden-area obstructions are
treated by [Baran–Demaine–Katz](https://erikdemaine.org/papers/Integration_Algorithmica/paper.pdf),
source 152. For the generic law here, a smaller exponent cannot give
the same square-root-scale implication from only small observed energy
and bounded jumps: if \(0\le\alpha<1/4\), choose
\(3/4<\kappa<1-\alpha\) and the deterministic tent
\(u_j=(\lfloor X^\kappa\rfloor-|j-\lfloor3X/2\rfloor|)_+\).
Its jumps are at most one. A fixed mean-zero smooth test equal to one
near its support has normalized pairing
\(\asymp X^{2\kappa-1}\), larger than square-root size. Yet
\(2\lceil X^\alpha\rceil\) uniform draws hit the tent with
probability \(O(X^{\alpha+\kappa-1})\). Along dyadic scales this
is summable, so eventually all those samples miss it and have variance
zero almost surely. These populations are fixed before drawing but
need not arise from one coefficient sequence or from prime windows.
This is a generic observation-law boundary, not prime sample optimality
or necessity of the logarithmic factor in (4).

Strong prime variance implying zero restrictions is classical;
[Zaccagnini, Section 3.3](https://arxiv.org/pdf/1603.02952), source 123,
is the Selberg-integral comparison. That complete-integral statement is
not the sampled criterion (3). The local delta is the proved transfer
with growing prime jumps, simultaneous test control, positive pole
weights, and an independent prime-counting converse. No new probability
principle or external priority is claimed.

Constants, singleton populations, endpoint extrema and repeated draws
are covered in (5)–(9). Removing repeated draws or choosing starts
adaptively would change the sampling law. Phase twists, generalized
prime systems and positive prime-supported reweightings may share the
jump bound but do not inherit (12) or (14). Controls selected against a
query transcript, as in PL-480, do not refute a fixed-source
probability-one guarantee.

An exact rational self-check covered 121 populations of sizes one
through five, starting at 7 with increments in \(\{-2,0,3\}\),
and 60,866 ordered outcomes for \(q=1,2\). It verified (8), the
population Jensen bound, translation invariance, and 235,594 conditional
extremum-neighborhood range bounds. For 232 nonconstant population/query
pairs the exact lower-tail probabilities were compared numerically with
the exponential upper bound. Rational complex cell weights of a linear
and a quadratic mean-zero polynomial also checked (9). Separately,
symbolic log-prime coefficients verified 4,838 endpoint identities and
82 finite-sum window-pairing identities at integer scales 40 through 80
for both rounded lengths. These are bookkeeping checks, not evidence
for (3), an asymptotic numerical test, or formal verification.

Neither sampling nor dispersion recovery proves the actual energy
premise. This result gives no finite GRH decision procedure,
zero-uniform onset, full uncentered variance, covariance-cone positivity,
critical-line lower bound or simplicity assertion. No independent
adversarial approval is claimed. The elementary concentration assembly
offers no separate high-value Lean fertility target.
