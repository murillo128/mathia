# MC-534 — Common square-free coefficients retain signed ambiguity under sparse window sampling

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`,
`MATCHED-CONTROL`, `NO-NOVELTY-CLAIM`.

## Claim and mathematical boundary

Fix a nonzero complex test \(\phi\in C_c^1((1,2))\), independently of
an integer scale \(X\). For a real coefficient sequence define
\[
 A(t)=\sum_{n\le t}a(n),\qquad
 T_{\phi,X}(a)=\sum_n a(n)\phi(n/X).
\tag{1}
\]
There are constants \(c_\phi,\kappa_\phi>0\) and \(X_\phi\) such that,
for every \(X\ge X_\phi\) and every list of \(q\le\kappa_\phi X\)
integer interval observations
\[
 \mathcal O_\ell(a)=A(v_\ell)-A(u_\ell),
 \qquad 0\le u_\ell<v_\ell,\quad 1\le\ell\le q,
\tag{2}
\]
there are two sequences \(a^+,a^-\in\{-1,0,1\}^{\mathbb N}\) with
**exactly the Möbius magnitudes**
\[
 |a^+(n)|=|a^-(n)|=\mu(n)^2
\tag{3}
\]
for which
\[
 \mathcal O_\ell(a^+)=\mathcal O_\ell(a^-)\in\{-1,0,1\}
 \quad\hbox{for every }\ell,
 \qquad
 |T_{\phi,X}(a^+)-T_{\phi,X}(a^-)|
 \ge c_\phi\frac{X}{q+1}.
\tag{4}
\]
The sequences differ from one fixed alternating-square-free baseline
only inside a fixed subinterval of \((X,2X)\). Within each sequence,
all lengths and starts in (2) come from its **one common prefix sum**.
No window functions are assigned independently.

In particular (2) may collect sampled starts for both macroscopic
lengths \(H=\lfloor X/20\rfloor\) and
\(K=\lfloor\sqrt2H\rfloor\), with arbitrary separate start sets.
Every observed value, and hence every observed centered variance, is
identical for the two controls. Their centered energy in any channel
with \(q_i\) observations is at most \(q_i\), by taking center zero.
Nevertheless a fixed signed smooth target remains ambiguous by order
\(X/(q+1)\).

This closes two gaps in the generic sharpness control of
[MC-533](MC-533-geometric-start-coverage-recovers-sparsely-sampled-mobius-variance.md):
compatibility of the channels with common coefficients, and possible
cancellation in the particular signed target. It also preserves the
exact square-free support. It does **not** prove a sampling lower bound
for Möbius: these signs are not multiplicative and are not assigned by
prime-factor parity. Neither reciprocal-zeta structure nor its pole-test
identity is imposed.

## 1. A baseline that makes every interval sum small

Let
\[
 Q(t)=\sum_{n\le t}\mu(n)^2,\qquad
 B(n)=Q(n)\pmod2\in\{0,1\},\qquad b(n)=B(n)-B(n-1).
\tag{5}
\]
Thus \(b\) alternates \(+1,-1\) along the square-free integers, is
zero elsewhere, and has prefix \(B\). Every interval sum of \(b\)
belongs to \(\{-1,0,1\}\).

Because a nonzero compactly supported \(C^1\) function cannot have
identically zero derivative, choose a closed interval
\([s,t]\Subset(1,2)\), a complex number \(\omega\) with
\(|\omega|=1\), and \(\eta>0\) such that
\[
 \operatorname{Re}(-\omega\phi'(u))\ge\eta
 \qquad(s\le u\le t).
\tag{6}
\]
They depend only on the fixed test. Put \(p=\lceil sX\rceil\),
\(r=\lfloor tX\rfloor\). Partition \([p,r]\) at **every observed
endpoint** lying strictly inside it:
\[
 p=z_0<z_1<\cdots<z_k=r,\qquad k\le2q+1.
\tag{7}
\]
Outside \((p,r]\) both controls equal \(b\). It suffices to modify
signs in each gap \((z_{j-1},z_j]\) while retaining the baseline
prefix at both endpoints.

## 2. Exact square-free bridges with the same endpoints

In one gap enumerate its \(m_j\) square-free positions increasingly,
put \(h_j=\lfloor m_j/2\rfloor\), and let
\(e=B(z_{j-1})\in\{0,1\}\). At the first \(h_j\) active positions
assign \(+1\) to \(a^+\) and \(-1\) to \(a^-\). At the next
\(h_j\) active positions reverse those signs. If \(m_j\) is odd,
assign the final active position the same sign \(1-2e\) in both
controls. All inactive positions remain zero.

The even part has total zero; the optional final step changes \(e\)
to \(1-e\). Both prefixes therefore finish at \(B(z_j)\). Induction
over gaps proves endpoint matching. Outside the modified interval the
prefixes again equal \(B\), so this also handles observations crossing
the block or having either endpoint outside it. Equation (4)'s exact
observation agreement follows.

Let
\[
 D(n)=A^+(n)-A^-(n).
\]
It is nonnegative everywhere and zero at all partition endpoints and
outside \((p,r)\). At the position of the \(\ell\)-th square-free
integer of a gap, for \(1\le\ell\le2h_j\), it equals
\[
 2\min\{\ell,2h_j-\ell\}.
\tag{8}
\]
The optional odd step has difference zero. Keeping just these distinct
integer positions in the sum, and using nonnegativity at all other
positions, gives the exact lower bound
\[
 \sum_{n=p}^{r-1}D(n)\ge2\sum_{j=1}^k h_j^2.
\tag{9}
\]
A final active position at \(r\) causes no loss: its difference is zero.

Write \(S=Q(r)-Q(p)=\sum_jm_j\). Since
\(\sum_jh_j\ge(S-k)/2\), Cauchy–Schwarz yields
\[
 \boxed{\sum_{n=p}^{r-1}D(n)
 \ge\frac{(S-k)_+^2}{2k}.}
\tag{10}
\]
This argument uses the **total** square-free population in the fixed
interval, not a density estimate in each possibly very short gap.
Repeated endpoints, empty active gaps, odd populations and highly
clustered observations all obey the same inequality.

## 3. A signed target sees the hidden primitive

Discrete summation by parts, with compactly supported difference
primitive \(D\), gives
\[
 T_{\phi,X}(a^+)-T_{\phi,X}(a^-)
 =-\sum_{n=p}^{r-1}D(n)
       \bigl(\phi((n+1)/X)-\phi(n/X)\bigr).
\tag{11}
\]
Every unit cell appearing here is contained in \([sX,tX]\).
Equation (6) and the fundamental theorem of calculus therefore give
\[
 \boxed{
 \operatorname{Re}\!\left(\omega
  [T_{\phi,X}(a^+)-T_{\phi,X}(a^-)]\right)
 \ge\frac{\eta}{X}\sum_nD(n)
 \ge\frac{\eta(S-k)_+^2}{2Xk}.}
\tag{12}
\]
Thus smooth signed cancellation does not erase this particular
control: the primitive was placed on an interval of fixed derivative
phase. Mean zero of \(\phi\), when imposed by the pole test, does
not affect this local argument.

For completeness, the elementary square-free estimate is
\[
 Q(y)=\sum_{d\le\sqrt y}\mu(d)\lfloor y/d^2\rfloor
     =\frac{y}{\zeta(2)}+O(\sqrt y).
\tag{13}
\]
The identity follows from \(\mu(n)^2=\sum_{d^2\mid n}\mu(d)\).
The floor errors contribute \(O(\sqrt y)\), and the tail of the
absolutely convergent series \(\sum_d\mu(d)/d^2=1/\zeta(2)\)
contributes the same order. This uses no zero-free continuation.
Consequently \(S\ge d_\phi X\) for all sufficiently large \(X\),
with some fixed \(d_\phi>0\). Taking, for example,
\(\kappa_\phi=d_\phi/8\) and increasing \(X_\phi\) ensures
\(k\le S/2\). Now (12) and \(k\le2q+1\) prove (4).

Any estimator based only on these interval values and the known
square-free magnitudes must output the same value for both controls.
Its worst-case absolute error is at least half their target separation,
even if the estimator is nonlinear or uses the exact uncentered values.
For a deterministic adaptive strategy with at most \(q\) interval
queries, run it against the baseline (5), then construct the pair using
all endpoints on that transcript. Inductively the two controls give the
same transcript. This is a deterministic worst-case statement; no
randomized average-case lower bound is asserted.

## 4. Relation to the current paired Möbius test

For any fixed \(0<\delta<1/2\), using only
\(q\le X^{1/2-\delta}\) total interval observations leaves target
separation \(\gg_\phi X^{1/2+\delta}\). This rules out a uniform
square-root-exponent recovery from such data over all sequences with
(3), even after imposing a common coefficient source and targeting one
fixed signed smooth functional. More generally, \(q=O(X^a)\),
\(0\le a<1\), permits separation \(\gg X^{1-a}\).
This is the same power cost as MC-533's geometric recovery for a fixed
number of well-spaced window channels, now with a stronger admissible
control. The constants depend on \(\phi\); a scale-varying test is
outside this assertion.

The fixed complex pole-isolating \(\phi\) used in
[MC-532](MC-532-paired-boxes-recover-trimmed-mobius-variance-at-macroscopic-lengths.md)
is among the admissible tests. Its source-independent two-box identity
and rounding estimate apply to bounded coefficients generally. Thus
for these controls the sum of the two **complete** normalized test
pairings differs by the target difference plus \(O_\phi(1)\), despite
identical sparse observations in both channels. This assertion uses
only MC-532's finite-interchange and bounded-coefficient rounding
argument, not its reciprocal-zeta asymptotic. In particular, knowing
that the two window functions are compatible does not remove the
sample ambiguity.

The controls can also be fixed across a prescribed separated sequence
of scales. Let \(X_{j+1}\ge4X_j\), and at scale \(X_j\) prescribe
observations with starts in \([X_j,2X_j)\), lengths at most \(X_j\),
and \(q_j\le\kappa_\phi X_j\). Perform the construction on the
disjoint intervals \((p_j,r_j]\). Each modification has zero total
relative to the baseline. Other modified intervals lie outside the
observed coefficient range \((X_j,3X_j)\) and the support of
\(\phi(n/X_j)\). Hence one pair of infinite sequences satisfies
(3), all the prescribed observation equalities, and the signed
separation (12) at every selected scale. At least one fixed member
has \(|T_{\phi,X_j}|\gg X_j/(q_j+1)\) on an infinite subsequence.
No claim concerns arbitrary densely interlaced scale observations.

## Prior art, validation and consequences

The recovery obstruction is a classical indistinguishable-input
construction. [Baran–Demaine–Katz, Sections 2–3](https://erikdemaine.org/papers/Integration_Algorithmica/paper.pdf)
(MC-S85) bounds the uncertainty left between samples by Lipschitz
[[research/prior_art/incremental/PA-lipschitz-integration-recovery|upper and lower envelopes]]. [Krieg–Vybíral, Section 2.1](https://doi.org/10.1007/s00041-023-10021-7)
(MC-S87) explicitly describes the standard use of functions that
vanish at observation points while retaining a large integral.
The counting input (13) is classical (MC-S12) and is derived here.
No new quadrature principle, square-free estimate or external novelty
is claimed. The local mathematical delta is the exact realization of
that obstruction by **common square-free sign coefficients**, with
identical interval measurements and a nonvanishing signed smooth
pairing. MC-533's distance sequence did not provide these properties.

The square-free controls in
[MC-523](MC-523-density-one-dyadic-window-control-permits-near-linear-prefixes.md)
and [MC-524](MC-524-density-one-window-control-coexists-with-prescribed-sparse-poles.md)
address missing scales, with additional qualitative correlation or
meromorphic-continuation requirements. They do not state this
same-block exact observation match or its query-count bound. Conversely,
those extra properties are not retained here. No substitution of this
control into a theorem with those additional hypotheses is justified.

Exact finite checks covered 87,380 support/partition/parity cases:
every binary support of length at most eight, every internal endpoint
partition, and both initial prefix parities. They checked exact
magnitudes, endpoint agreement, all endpoint-interval sums,
nonnegativity of \(D\), and (9)–(10). Another 168 exact-rational
checks used the actual square-free support, scales
\(X\in\{40,80,120,200,500,1000\}\), both rounded macroscopic
lengths, and observation counts \(q\in\{0,1,2,3,5,10,20\}\), with
four start lists per case (pseudorandom seed 534). The test was
\(\phi(u)=(3/2-u)(u-5/4)^2(7/4-u)^2\) on \([5/4,7/4]\), zero outside;
on \([23/16,25/16]\), \(-\phi'\ge1/512\). These checked (11)–(12),
including windows crossing \(2X\). The test is \(C^1\), sufficient
for this theorem; the analytic pole test is smoother. The proof, rather
than this finite enumeration, supplies the general result. No Lean
check or independent adversarial approval is asserted.

Exact support, bounded jumps, common coefficients and signed smooth
recovery therefore do not by themselves improve the square-root
**sample exponent** of the generic method. A reduction of that exponent
for actual Möbius must use an additional constraint that excludes the
constructed signs, such as a proved consequence of their missing
multiplicative or reciprocal-zeta structure. This result establishes
neither that such an arithmetic improvement is impossible nor any new
bound for \(M(x)\). Its elementary endpoint construction does not
supply a separate high-value Lean handoff.
