# PL-476 — Trimmed paired prime variance retains the joint-GRH obstruction

**Evidence/status:** LITERATURE+DERIVED / EXACT CONDITIONAL TRANSFER;
NON-EFFECTIVE ZERO-DEPENDENT CONSTANTS; NO EXTERNAL NOVELTY CLAIM.
No unconditional arithmetic variance ceiling is established.

## Claim and change in observation requirement

Let \(X\) be a positive integer, \(I_X=\{X,\ldots,2X-1\}\), and
\[
 a_n=\Lambda(n)\mathbf1_{n\equiv1\ (5)},\qquad
 S_L(j)=\sum_{j<n\le j+L}a_n.
\]
For integers \(1\le H\le X/20\), put
\(L_1=H\), \(L_2=K=\lfloor\sqrt2 H\rfloor\).
Independently choose masks \(E_i\subset I_X\), counts
\(B_i=|E_i|<X/2\), and constants \(c_i\in\mathbb C\). Define
\[
 V_i=\sum_{j\in I_X\setminus E_i}|S_{L_i}(j)-c_i|^2.
\tag{1}
\]
If zeta or any of the three primitive nonprincipal mod-5 Dirichlet
functions has a nontrivial zero \(\rho_0=\beta+i\gamma\),
\(\beta>1/2\), there are \(C>0,X_0\), depending on that zero
and the full zero set, such that
\[
 \boxed{
 \frac{\sqrt{XV_1}+B_1^2\log(3X)}{H}
 +\frac{\sqrt{XV_2}+B_2^2\log(3X)}{K}
 \ge C X^\beta.}
\tag{2}
\]
This holds for every integer \(X\ge X_0\), uniformly in all the
stated lengths, masks, and constant centers. Each center may be its
own retained empirical mean. The masks need not agree.

In particular, let \(H_X=\lfloor X/20\rfloor\) and
\(K_X=\lfloor\sqrt2 H_X\rfloor\). The following condition is
**equivalent to joint GRH for these four functions**: there exist an
unbounded set \(\mathcal X\) of integer scales and families of masks
and centers on it, fixed before epsilon varies, such that for every
\(\varepsilon>0\), both channels satisfy
\[
 B_i\ll_\varepsilon X^{3/4+\varepsilon},\qquad
 V_i\ll_\varepsilon X^{1+\varepsilon}L_i
 \quad(X\in\mathcal X\text{ sufficiently large}).
\tag{3}
\]
The converse is proved below using the classical GRH estimate for
\(\psi(x;5,1)\), independently of any Möbius variance theorem.

The local delta from
[[research/prime_lattice/findings/PL-475-two-box-lengths-force-paired-macroscopic-prime-variance|PL-475]]
is permission to omit quantitatively many whole integer starts,
separately in each channel. The complete analytic tests remain intact;
the omitted mass is recovered using the exact prime-window jump bound.
The bounded-source argument in
[[research/mobius_cancellation/findings/MC-532-paired-boxes-recover-trimmed-mobius-variance-at-macroscopic-lengths|MC-532]],
Section 3, motivates this transfer. Its finite lemma is reconstructed
fully here, with the prime coefficient envelope retained. Its
reciprocal-zeta principal parts and RH converse are not inputs.

## 1. A finite recovery lemma with an explicit jump price

Let \(r_j\in\mathbb C\) be indexed by \(N\) consecutive integers,
with \(|r_{j+1}-r_j|\le J\). Delete a set \(E\) of size
\(B<N/2\), and let \(V=\sum_{j\notin E}|r_j|^2\). Then
\[
 \sum_j|r_j|\le 2\sqrt{NV}+2JB^2.
\tag{4}
\]
For \(B=0\), Cauchy–Schwarz gives the stronger \(\sqrt{NV}\).
For \(B\ge1\), choose, for each omitted index \(j\), a block of
\(2B+1\) indices within the full index interval and containing \(j\).
Such a block exists because \(2B+1\le N\), including when \(j\)
is near an endpoint. It contains at least \(B+1\) retained indices,
all at distance at most \(2B\). Averaging over any \(B+1\) of them,
\[
 |r_j|\le\sqrt{V/(B+1)}+2BJ.
\]
Adding these bounds and the retained absolute mass gives
\[
 \sum_j|r_j|
 \le\left(\sqrt{N-B}+\frac{B}{\sqrt{B+1}}\right)\sqrt V+2JB^2
 \le2\sqrt{NV}+2JB^2.
\]
No regularity of the deletion set is assumed. Subtracting any constant
preserves the jump bound; subtracting a start-dependent fitted profile
need not do so.

For the prime source the exact endpoint identity is
\[
 S_L(j+1)-S_L(j)=a_{j+L+1}-a_{j+1}.
\tag{5}
\]
Here all relevant indices are below \(3X\), since
\(L\le K\le2H\le X/10\). Because
\(0\le a_n\le\log(3X)\), the difference in (5) has modulus at
most \(\log(3X)\). Positivity permits this bound without a factor
two. Applying (4) to \(r_j=S_{L_i}(j)-c_i\) yields
\[
 \sum_{j\in I_X}|S_{L_i}(j)-c_i|
 \le2\sqrt{XV_i}+2B_i^2\log(3X).
\tag{6}
\]

## 2. Keep the complete mean-zero tests and the prime pole formula

We use the exact destination inputs proved in PL-475, Sections 1–4,
and
[[research/prime_lattice/findings/PL-471-sparse-zero-annihilators-force-prime-variance-on-every-large-block|PL-471]],
Sections 1–3. For \(1/2<\sigma_0<\beta\), they supply a fixed
\(\varphi\in C_c^\infty((4/3,5/3);\mathbb C)\), with integral
zero, such that
\[
 T_\varphi(X):=\sum_n a_n\varphi(n/X)
 =-w_{\rho_0}X^{\rho_0}+O_\varphi(X^{\sigma_0}),\qquad
 w_{\rho_0}=\tfrac14\sum_\chi m_\chi(\rho_0)>0.
\tag{7}
\]
The sum in the weight includes the four functions, with zero
multiplicity zero when a function does not vanish there. The sparse-zero
Mellin construction cancels every other zero to the right of
\(\sigma_0\); the actual logarithmic-derivative explicit formula
bounds the remaining sum. At a common zero the residues add with the
same sign. A multiple zero changes \(w_{\rho_0}\), not the order
of the logarithmic-derivative pole. There is no reciprocal-pole
\((\log X)^{m-1}\) factor in this prime formula.

For \(h=H/X\), the two compact distributional deconvolvers of
PL-475 produce mean-zero smooth tests \(f_{1,h},f_{2,h}\), supported
in the fixed interval
\[
 [4/3-1/20,\,5/3+(1+\sqrt2)/20]\Subset(1,2),
\]
whose sup norms and first derivative norms are uniformly bounded for
\(0<h\le1/20\). Writing
\(A_af(u)=\int_0^1 f(u-at)\,dt\), they satisfy
\[
 A_hf_{1,h}+A_{\sqrt2h}f_{2,h}=\varphi.
\]
Since \(|K/X-\sqrt2h|<X^{-1}\),
\[
 \|A_hf_{1,h}+A_{K/X}f_{2,h}-\varphi\|_\infty
 \ll_\varphi X^{-1}.
\tag{8}
\]
This error has support in a fixed compact subset of \((0,3)\).
Summing it against \(a_n\) costs \(O_\varphi(\log(3X))\),
using \(O(X)\) terms of size at most \(\log(3X)\).
We do not assert an exact inverse for the rounded rational pair.

For each channel define the complete pairing
\[
 \mathcal L_i=\frac1{L_i}\int_X^{2X}
       (S_{L_i}(y)-c_i)f_{i,h}(y/X)\,dy,
 \qquad S_L(y)=\sum_{y<n\le y+L}a_n.
\]
Its constant center vanishes exactly. Extending the test by zero and
interchanging the finite sum with the integral gives
\[
 \mathcal L_i=\sum_n a_n(A_{L_i/X}f_{i,h})(n/X).
\tag{9}
\]
The coefficient at \(n\) is the integral of the test over
\([n-L_i,n]\), divided by \(L_i\); endpoint-crossing windows
are included. Thus (7)–(9) give, uniformly in \(H\),
\[
 |\mathcal L_1+\mathcal L_2|
 =|T_\varphi(X)+O_\varphi(\log(3X))|
 \ge \tfrac12 w_{\rho_0}X^\beta
\tag{10}
\]
for all sufficiently large \(X\).

For integer \(L\), \(S_L(y)=S_L(j)\) on \([j,j+1)\).
Consequently the uniform test bounds and (6) imply
\[
 |\mathcal L_i|\le\frac{\|f_{i,h}\|_\infty}{L_i}
                      \sum_{j\in I_X}|S_{L_i}(j)-c_i|
 \ll_\varphi\frac{\sqrt{XV_i}+B_i^2\log(3X)}{L_i}.
\tag{11}
\]
Combining (10) and (11) proves (2). At no stage is an analytic test
multiplied by a mask. In particular, no discontinuous masked Mellin
test is substituted into (7).

## 3. The macroscopic criterion and its independent converse

At \(H_X=\lfloor X/20\rfloor\), both lengths are comparable to
\(X\). Under (3), the left side of (2) is
\[
 O_\varepsilon\bigl(X^{1/2+\varepsilon/2}
              +X^{1/2+2\varepsilon}\log(3X)\bigr).
\tag{12}
\]
Given \(\beta>1/2\), choose
\(0<\varepsilon<\min\{1/4,(\beta-1/2)/2\}\).
Then (12) is \(o(X^\beta)\), contradicting (2) along the unbounded
set \(\mathcal X\). The same epsilon makes \(B_i<X/2\)
automatic eventually. Excluding every \(\beta>1/2\), followed by
functional-equation symmetry within the four-function family, proves
joint GRH. No density or spacing hypothesis on \(\mathcal X\) is used.

Conversely, joint GRH gives the classical fixed-modulus estimate
\[
 \psi(x;5,1)=x/4+O(\sqrt{x}\log^2(3x)).
\tag{13}
\]
This follows by applying the GRH explicit-formula bound separately to
the four character sums and using character orthogonality. Source 120
is the classical reference; [Lee (2023), Corollary 1.1, equation (4),
and its character-wise proof](https://doi.org/10.1093/qmath/haad031),
source 144, provides an explicit version. Only these four functions'
zeros are needed for fixed modulus 5.

Take all sufficiently large integer scales, empty masks, and
\(c_i=L_i/4\). Applying (13) at \(j\) and \(j+L_i\), both
comparable to \(X\), gives
\[
 |S_{L_i}(j)-L_i/4|\ll\sqrt X\log^2(3X),\qquad
 V_i\ll X^2\log^4(3X)
       \ll_\varepsilon X^{1+\varepsilon}L_i.
\]
This proves (3) for the same fixed families for every epsilon.
It uses only macroscopic \(L_i\asymp X\); it is not a claim of
that variance bound uniformly for arbitrarily short lengths.

## Prior art, controls, and evidence boundary

The compact inverse is classical [[research/prior_art/incremental/PA-multichannel-compact-distribution-deconvolution|multichannel deconvolution]]:
[Casey–Walnut (1994)](https://doi.org/10.1137/1036140), source 142,
and [Pensky–Sapatinas (2011)](https://doi.org/10.1214/11-EJS597),
source 143, supply the neighboring boxcar/Diophantine literature.
PL-475 already proves the exact localized version used here.
The finite recovery lemma is elementary discrete Lipschitz recovery,
not a new inversion principle. The closest prime exceptional-set
comparison is [Bazzanella–Perelli (2000)](https://doi.org/10.1006/jnth.1999.2429),
source 145, which studies inertia and decrease of exceptional sets for
short-interval prime asymptotics. No theorem there is invoked as the
arbitrary-mask, constant-center bound (6). The broad variance-to-zero
converse is also classical; [Zaccagnini (2016), Section 3.3](https://arxiv.org/abs/1603.02952),
source 123, records the Selberg-integral version. No external priority
or new prime-distribution estimate is claimed.

The resulting local transfer changes which observations would suffice;
it supplies neither their energy bounds nor their deletion counts.
The following limits are essential.

- **Quantitative deletion is required.** A qualitative \(B=o(X)\)
  does not imply (3) or control the deletion term in (12). The
  exponent \(3/4\) and logarithmic cost are sufficient, not asserted
  optimal for these signed tests or for the prime source.
- **Two simultaneous channels.** Both estimates must hold on the same
  base blocks. One favorable length, or separate unbounded scale sets
  with no common unbounded subset, does not supply (12). No independence
  of the windows or masks is assumed.
- **Whole starts and constant centers.** The masks remove entire
  integer cells. Partial-cell masks require a different argument.
  Distinct retained empirical centers are allowed; a fitted function
  of the start changes the jump and mean-zero calculations.
- **Empty and coincident cases.** Empty masks recover PL-475's paired
  floor after squaring and using Cauchy–Schwarz. At \(H=K=1\), the
  two measurements may coincide; (8) retains its error and the proof
  never divides by \(K-H\).
- **Arithmetic selectivity stays in (7).** The inverse and (4) apply
  to general coefficient systems. Constant or twisted coefficients,
  generalized primes, and generic lattice completions do not inherit
  the noncancelling mod-5 zero formula. No relative covariance frame
  or positivity gate follows from this transfer.
- **Non-effectivity remains.** The tests and onset depend on the full
  hypothetical sparse zero set. No finite-zero implementation,
  uniformity as \(\beta\downarrow1/2\), critical-line variance
  floor, or zero simplicity is claimed.

An auxiliary exact-rational check used 200 paired nonnegative
residue-supported coefficient arrays (400 channel cases, seed 476),
including 97 coincident pairs. It verified the endpoint difference,
(4), zero-sum complete cell weights and the exact centered pairing (9)
with compact piecewise-polynomial test primitives. Cases included
empty masks, masks just below half the starts, endpoint masks, distinct
constant and retained-mean centers, and crossing windows. This checks
discrete bookkeeping for generic coefficients, not the analytic
inverse, the actual logarithmic weights, or zero locations. The
proof above is the evidence; no Lean or independent adversarial
validation is claimed.
