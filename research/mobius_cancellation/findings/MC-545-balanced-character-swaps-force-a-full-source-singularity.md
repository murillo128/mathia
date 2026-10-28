# MC-545 — Balanced character swaps force a full-source singularity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `MATCHED-CONTROL`,
`CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`. This constructs one fixed
real multiplicative function of exact square-free magnitude. It proves
a full-source obstruction to a global power bound, not an every-block
dispersion floor or a sparse-sampling counterexample for Möbius.

## Claim and distinction from selected-prime targets

[MC-544](MC-544-fixed-character-backgrounds-cancel-balanced-prime-replicas.md)
selects large balanced targets inside a character source whose complete
prefix remains \(O(\sqrt x)\). Here the signs are actually **changed**
on balanced prime packets at every sufficiently large dyadic scale.
The exact Euler quotient includes all composite effects. Those effects
cannot restore the same global square-root bound.

Fix \(3/4<\kappa<1\), and write
\[
 \beta=2\kappa-1,\qquad a=3/2,\qquad
 \alpha_\kappa=\frac{3\beta}{16a^{\beta+1}\log2}\in(0,1).
\tag{1}
\]
The deterministic construction below gives \(f_\kappa\), independent
of any observations, with \(|f_\kappa(n)|=\mu(n)^2\). Its Dirichlet
series, initially defined for \(\Re s>1\), has a holomorphic
continuation \(A_\kappa(s)\) to \(\Re s>\beta\), and
\[
 \boxed{\lim_{\epsilon\downarrow0}
 \frac{\log A_\kappa(\beta+\epsilon)}{\log(1/\epsilon)}
       =\alpha_\kappa.}
\tag{2}
\]
The real logarithm is well-defined here: \(A_\kappa(\sigma)>0\)
for real \(\sigma>\beta\). In particular, \(\beta\) is a
nonremovable, **nonmeromorphic** singularity, and for every
\(\delta>0\),
\[
 \boxed{\sum_{n\le x}f_\kappa(n)\ne O(x^{\beta-\delta}).}
\tag{3}
\]
The construction remains at finite ordinary pretentious distance from
MC-544's fixed character source. Its unsigned prime-change series
converges exactly at exponents \(t>\kappa\). Thus the paired signed
Euler logarithm reaches \(2\kappa-1\), below the absolute-cost
threshold \(\kappa\), but develops the genuine full-source
singularity (2) at that boundary.

Neither convergence of the original Dirichlet series throughout
\(\Re s>\beta\), a sharp summatory asymptotic, nor a meromorphic
continuation across the boundary is claimed.

The same singularity also survives **every fixed nonzero compact smooth
test**, including signed tests with arbitrarily many vanishing Mellin
moments: for \(0\ne w\in C_c^\infty((0,\infty);\mathbb C)\) and
every \(\delta>0\),
\[
 T_w(X):=\sum_{n\ge1}f_\kappa(n)w(n/X)
             \ne O_w(X^{\beta-\delta}).                 \tag{3a}
\]
This holds over real scales and over integer scales. It is an
unbounded-subsequence obstruction for each fixed test, not a lower
bound on every block or a statement about a family of tests varying
with the scale. Section 4 derives it from (2), without a Tauberian
asymptotic.

## 1. One infinite assignment of balanced prime swaps

Let \(f_0(2)=1\), \(f_0(p)=\chi_4(p)\) for odd primes, and
\(f_0(p^r)=0\) for \(r\ge2\). Choose a fixed integer \(k_0\)
large enough for the following packets to be disjoint, with
\(W_k<Y_k/6\):
\[
 Y_k=2^k,\qquad u_k=3Y_k/2,\qquad
 W_k=4\lfloor Y_k^\kappa/4\rfloor\qquad(k\ge k_0).
\tag{4}
\]
Define the two candidate sets
\[
 \begin{split}
 U_k&=\{p:u_k<p\le u_k+W_k/4,\quad p\equiv3\pmod4\},\\
 V_k&=\{q:u_k+3W_k/4<q\le u_k+W_k,\quad q\equiv1\pmod4\}.
 \end{split}
\tag{5}
\]
Put \(h_k=\min(|U_k|,|V_k|)\); retain the smallest \(h_k\)
primes in each set, denoting the retained sets by \(P_k,Q_k\).
Empty early packets may simply contribute nothing. Flip \(f_0(p)\)
on \(P_k\cup Q_k\) for all \(k\ge k_0\), leave every other
prime value unchanged, and extend multiplicatively with zero on
prime powers of exponent at least two. This defines \(f_\kappa\)
on all integers at once. The prime changes are \(+2\) on \(P_k\)
and \(-2\) on \(Q_k\), so each packet has exactly zero total
prime change. For the prime-change primitive
\(C_k(n)=2\#\{p\in P_k:p\le n\}-2\#\{q\in Q_k:q\le n\}\),
one has \(C_k\ge0\), finite support, and
\(\sum_n C_k(n)=2\Delta_k\), where \(\Delta_k\) is defined below.
Its area is therefore of order \(Y_k^{2\kappa}/\log Y_k\);
this prime-only primitive is not identified with the full-source prefix.

The fixed-modulus short-interval prime theorem of
[Thorner–Zaman, Theorem 1.1 and Remark 1.2](https://arxiv.org/pdf/2108.10878v2)
(MC-S99) supplies
\[
 |U_k|\sim |V_k|\sim h_k\sim\frac{W_k}{8\log Y_k}.
\tag{6}
\]
Indeed, every fixed positive fraction of either interval has length
comparable to \(Y_k^\kappa\), above the theorem's
\(x^{7/12+\eta}\) threshold for a fixed suitable \(\eta>0\).
At modulus four the possible fixed exceptional-zero correction tends
to zero; no GRH or moving-modulus estimate is needed.

Applying the same theorem to a fixed finite partition of each interval,
then refining the partition, gives their normalized first moments.
Equalizing the populations deletes only \(o(h_k)\) primes; each
centered coordinate \(p-u_k\) has size at most \(W_k\). Hence
\[
 \frac1{h_k}\sum_{p\in P_k}(p-u_k)=W_k/8+o(W_k),\qquad
 \frac1{h_k}\sum_{q\in Q_k}(q-u_k)=7W_k/8+o(W_k),
\]
and therefore
\[
 \Delta_k:=\sum_{q\in Q_k}q-\sum_{p\in P_k}p
       =(3/4+o(1))h_kW_k.
\tag{7}
\]
For every nonempty packet one also has the exact bounds
\(h_kW_k/2<\Delta_k<h_kW_k\). These use only interval placement,
not a prime-distribution theorem.

## 2. The exact quotient retains all composites

The baseline Euler product is
\[
 A_0(s)=\sum_{n\ge1}\frac{f_0(n)}{n^s}
       =\frac{L(s,\chi_4)}{(1-2^{-s})\zeta(2s)}
             \quad(\Re s>1).
\tag{8}
\]
It is holomorphic for \(\Re s>1/2\), and positive and nonzero on
the real interval \(s>1/2\). For the latter assertion,
\(L(\sigma,\chi_4)=\sum_{m\ge0}[(4m+1)^{-\sigma}
-(4m+3)^{-\sigma}]>0\) for \(\sigma>0\), while the two real
denominator factors in (8) are positive when \(\sigma>1/2\).

For \(\Re s>1\), the full modified series satisfies exactly
\[
 A_\kappa(s)=A_0(s)e^{\mathcal L(s)},\qquad
 \mathcal L(s)=\sum_{k\ge k_0}\left[
    \sum_{p\in P_k}\ell(p^{-s})-
    \sum_{q\in Q_k}\ell(q^{-s})\right],
\tag{9}
\]
where
\[
 \ell(z)=\log\frac{1+z}{1-z}
        =2\sum_{r\ge0}\frac{z^{2r+1}}{2r+1}\qquad(|z|<1).
\tag{10}
\]
The power series fixes the logarithm, so no branch convention is
implicit. The lower primes originally have sign \(-1\), which fixes
the positive sign in (9). Reversing that sign would change the result.

This is not an additive approximation that discards old prime
replicas. For example, if \(c=f_0(p)\in\{-1,1\}\) at a changed
prime, the local Dirichlet-convolution quotient is
\[
 \frac{1-cz}{1+cz}=1+2\sum_{r\ge1}(-c)^rz^r.
\tag{11}
\]
Multiplying these quotients accounts for products involving arbitrarily
many changed primes and for the prime-power terms that cancel when
the final square-free source is recovered.

On a compact subset of \(\Re s>\beta\), pair the members of
\(P_k,Q_k\) arbitrarily. The derivative of \(t^{-s}\) gives
\[
 \left|\sum_{p\in P_k}p^{-s}-\sum_{q\in Q_k}q^{-s}\right|
 \ll h_kW_kY_k^{-\Re s-1}
 \ll \frac{Y_k^{\beta-\Re s}}{\log Y_k}.
\tag{12}
\]
The terms of degree at least three in (10) are bounded absolutely by
\[
 O\left(h_kY_k^{-3\Re s}\right)
     =O\left(\frac{Y_k^{\kappa-3\Re s}}{\log Y_k}\right).
\tag{13}
\]
Since \(3\beta>\kappa\), the sum in (13) converges even in a
neighborhood of the real point \(\beta\). Equations (12)–(13)
prove locally uniform convergence of (9) for \(\Re s>\beta\).
Together with (8), they prove the asserted holomorphic continuation.
They do not identify that continuation with a conditionally convergent
ordinary ordering of the coefficient series.

## 3. The signed area creates a noninteger singularity

For real \(\sigma\) in a fixed compact neighborhood of \(\beta\),
Taylor expansion around \(u_k=aY_k\), (6), and (7) give, uniformly,
\[
 \begin{split}
 2\left(\sum_{p\in P_k}p^{-\sigma}
           -\sum_{q\in Q_k}q^{-\sigma}\right)
 &=2\sigma u_k^{-\sigma-1}\Delta_k
          +O(h_kW_k^2Y_k^{-\sigma-2})\\
 &=\left(\frac{3\sigma}{16a^{\sigma+1}}+o(1)\right)
          \frac{Y_k^{\beta-\sigma}}{\log Y_k}.
 \end{split}
\tag{14}
\]
For \(\sigma=\beta+\epsilon\), the main series is explicit:
\[
 \sum_{k\ge k_0}\frac{Y_k^{-\epsilon}}{\log Y_k}
 =\frac1{\log2}\sum_{k\ge k_0}\frac{2^{-k\epsilon}}k
 =\frac{\log(1/\epsilon)}{\log2}+O(1).
\tag{15}
\]
The uniform \(o(1)\) in (14) contributes
\(o(\log(1/\epsilon))\): split off finitely many terms and bound
the remaining errors by their tail supremum times (15). The sum
of (13) stays bounded. Finally \(\log A_0(\beta+\epsilon)\)
stays bounded. This proves (2), equivalently
\[
 A_\kappa(\beta+\epsilon)
       =\epsilon^{-\alpha_\kappa+o(1)}.
\tag{16}
\]
Here \(0<\alpha_\kappa<3/(16\log2)<1\). A meromorphic
function at \(\beta\) which diverges along this ray would have a
positive integer pole order, and that integer would equal the limit
in (2). Thus the singularity is not meromorphic. Equation (16) alone
does not specify its complex monodromy or a full local power expansion.

If \(F_\kappa(x)=\sum_{n\le x}f_\kappa(n)\) were
\(O(x^{\beta-\delta})\), the integral
\[
 s\int_1^\infty F_\kappa(x)x^{-s-1}\,dx
\tag{17}
\]
would be holomorphic for \(\Re s>\beta-\delta\) and equal to
the original series for \(\Re s>1\). Uniqueness of analytic
continuation contradicts (16). This proves (3) for the **complete**
source, including every composite coefficient.

For comparison, (6) gives
\[
 \sum_{p\text{ changed}}p^{-t}<\infty
 \quad\Longleftrightarrow\quad t>\kappa\qquad(t>0).
\tag{18}
\]
At equality the block terms are comparable to \(1/k\). In particular
\(2\sum_{p\text{ changed}}1/p<\infty\), the ordinary squared
pretentious distance from \(f_0\). Equation (11) gives the strong
absolute convolution cost \(2\sum_{p\text{ changed}}
p^{-t}/(1-p^{-t})\), with the same threshold (18).
Finiteness of the ordinary distance therefore does not restore
MC-544's square-root prefix bound. That general failure is classical;
the paired threshold and (2) are the present construction's certificate.

## 4. Smooth tests cannot remove the fractional singularity

Write \(\alpha=\alpha_\kappa\). If \(G\) is any nonzero
holomorphic germ at \(\beta\), its zero there has some finite order
\(m\ge0\). Equation (2) implies
\[
 \lim_{\epsilon\downarrow0}
 \frac{\log|G(\beta+\epsilon)A_\kappa(\beta+\epsilon)|}
      {\log\epsilon}=m-\alpha\notin\mathbb Z.            \tag{19}
\]
A nonzero meromorphic germ has an integer value for this limit, its
signed order of vanishing. Consequently \(GA_\kappa\) admits no
meromorphic extension to a neighborhood of \(\beta\). This does
not require a complex fractional-power expansion for \(A_\kappa\).
In particular, a zero of the multiplier can remove radial blowup
without making the product holomorphic: for \(m\ge1\), its modulus
is \(\epsilon^{m-\alpha+o(1)}\to0\), still with noninteger order.

For the test in (3a), set
\[
 W(s)=\int_0^\infty w(t)t^{s-1}\,dt.
\]
Compact support away from zero makes \(W\) entire. It is not
identically zero: on any fixed vertical line it is the Fourier
transform of the compactly supported function
\(u\mapsto e^{\sigma u}w(e^u)\), and Fourier uniqueness applies.
Thus (19) applies even when \(W(\beta)=0\).

Suppose, contrary to (3a), that \(T_w(X)=O(X^{\beta-\delta})\).
If \(\operatorname{supp}w\subset[c,d]\) with \(0<c<d<\infty\),
then \(T_w(X)=0\) for \(X<1/d\), and it is bounded on every compact
scale interval. Therefore
\[
 B_w(s)=\int_0^\infty T_w(X)X^{-s-1}\,dX                \tag{20}
\]
is holomorphic for \(\Re s>\beta-\delta\); on each compact
subset the power margin also dominates all logarithmic derivatives.
For \(\Re s>1\), absolute convergence, \(|f_\kappa(n)|\le1\)
and \(t=n/X\) give
\[
 B_w(s)=W(s)\sum_{n\ge1}f_\kappa(n)n^{-s}
       =W(s)A_\kappa(s).                                \tag{21}
\]
The identity theorem extends this equality throughout
\(\Re s>\beta\). But (20) would then be a holomorphic extension
of \(WA_\kappa\) across \(\beta\), contradicting (19).
No coefficient-series convergence to the left of 1 is used.

The integer-scale assertion follows without a sampling hypothesis.
Termwise differentiation is locally finite, and
\[
 |T_w'(X)|\le \frac{\|w'\|_\infty}{X^2}
                    \sum_{n\le dX}n=O_w(1)\quad(X\ge1). \tag{22}
\]
If a power bound held at all sufficiently large integers, choose
\(0<\delta'<\min(\delta,\beta)\). Nearest-integer comparison
and (22) would give \(T_w(X)=O(X^{\beta-\delta'})\) at every
large real scale, already excluded. Equivalently, for every fixed
\(w\ne0\), \(\delta>0\), \(C>0\) and \(X_0\), some integer
\(X\ge X_0\) has \(|T_w(X)|>CX^{\beta-\delta}\).
The scale can depend on all these choices.

Vanishing moments are an actual control here. Given a nonzero
nonnegative \(v\in C_c^\infty((0,\infty))\), put
\(w_m=(t\,d/dt+\beta)^m v\). Integration by parts gives
\(W_m(s)=(\beta-s)^m V(s)\), with \(V(\beta)>0\).
Thus each finite order \(m\) occurs, yet (3a) holds for every
\(w_m\). More generally, any finite linear combination of dilated
compact tests is covered whenever the combined test is nonzero.

This is the precise limit on importing the meromorphic-pole
annihilation step of
[MC-528](MC-528-multiplicity-aware-annihilation-forces-mobius-variance-on-every-block.md).
An analytic multiplier with a zero of matching integer order can
cancel a pole; it cannot cancel this fractional radial order, even
if it has infinitely many other zeros. This excludes that cancellation
step for this source. It does not exclude a different branch-sensitive
inversion argument, nor prove an every-block dispersion estimate.

## Mathematical delta, prior art, and unresolved observation question

The earlier character control could cancel a selected target completely.
The present deterministic dyadic swaps retain a signed area in the
Euler logarithm, and all composite terms together cannot cancel its
fractional real singularity. This is an actual infinite multiplicative
assignment and a full-source power obstruction, without an ensemble
expectation or an independent-orientation premise.
The smooth-test consequence (3a) shows that this obstruction is not
confined to a sharp cutoff and cannot be suppressed by fixed moment
cancellation. It is a corollary of the same source singularity,
retained here rather than assigned a separate finding identity.

The ingredients are classical. [Jung–Lemke Oliver, introduction and
Theorem 1.1](https://lemkeoliver.github.io/papers/07-PowerCancellation.pdf)
(MC-S7) already explain why sparse character modifications can destroy
power cancellation despite finite ordinary pretentious distance.
[Seip, Section 6.1](https://arxiv.org/html/1812.11729v2#S6.SS1)
(MC-S100) constructs singularities by choosing prime Euler factors
and separating the first prime term from higher powers. Those are
established mechanisms, not discoveries claimed here. Seip's
unimodular completely multiplicative, meromorphic constructions are
not being imported as an exact-square-free real-sign theorem or as
a sampling theorem. The short-interval population input is precisely
MC-S99. No Selberg–Delange or signed Tauberian asymptotic is assumed.

The Mellin holomorphy, inversion and dilation identities used in
Section 4 are classical; see [Zagier, Section 1](https://people.mpim-bonn.mpg.de/zagier/files/tex/MellinTransform/fulltext.pdf)
(MC-S71). The corresponding local transform argument already appears
for Möbius in [MC-521, Section 3](MC-521-smooth-deconvolution-removes-the-variance-zero-free-boundary-loss.md).
There a single test can mask an integer-order reciprocal-zeta pole;
here the noninteger order makes every nonzero compact test retain a
singularity. This elementary consequence of integer analytic orders
is not claimed as a new Mellin or Tauberian theorem.

The local delta is the quantitative compatibility calculation for
balanced, sublinear-width packets at **every dyadic scale**:
the count exponent is \(\kappa\), the signed displacement exponent
is \(2\kappa-1\), and the full continuation has the noninteger
radial exponent (1). No external novelty is asserted.

This is only partial progress on
[the dense full-source dispersion clue](../clues/CLUE-dense-multiplicative-full-source-dispersion.md).
Failure of a global \(O(x^{\beta-\delta})\) bound does **not**
prove dispersion on every large block, or on the two prescribed
window populations. The same limitation applies to (3a): the
exceptional scales for different tests need not coincide, a fitted
center is not a fixed compact test, and no prescribed sparse scale
sequence is controlled. It also gives no sample upper tail. The actual
coefficient series has signed terms, so (16) cannot be converted into
an asymptotic for \(F_\kappa\) by an unproved positive Tauberian step.
The isolated meromorphic-pole certificate used for Möbius is likewise
inapplicable to this nonmeromorphic boundary without a new argument.
The source remains character-pretentious and does not have
\(\mu(p)=-1\). No RH or optimal Möbius sampling rate follows.

The next decisive test for this specific source is a full-source
window-tail estimate that includes all earlier-packet replicas and
products of changed primes. Repeating a single-packet area argument
would not establish either required observation property. A failure
of this source would not exclude all multiplicative constructions.

## Validation boundary

The convergence and limiting statements are proved above using the
cited short-interval theorem; finite computations cannot verify them.
An exact-integer audit at \(\kappa=4/5\), \(k=13,\ldots,20\),
checked packet disjointness, residue signs, exact balance, displacement
bounds, and the rational mean-value bounds for each paired
\(p^{-1}-q^{-1}\). The coefficient identity \(f_\kappa=f_0*b\)
from (11) and exact square-free magnitude were checked through
\(2^{21}\). A separate 10,000-coefficient finite model with changed
primes \(3,5,7,13\) checked the same convolution including interactions
of multiple changed primes and repeated prime powers; that model is
only an algebra check, not an instance of the asymptotic packet law.
No Lean verification or independent adversarial approval is asserted.
The elementary quotient identities alone are not a separate high-value
formalization target; the load-bearing analytic and observation steps
are not being delegated in this invocation. Section 4 is an analytic
consequence of (2), checked through absolute convergence in (21),
holomorphic uniqueness, finite zero orders, the moment-cancelled
control, and the integer-scale bound (22); finite source numerics
are not evidence for its asymptotic quantifiers.
