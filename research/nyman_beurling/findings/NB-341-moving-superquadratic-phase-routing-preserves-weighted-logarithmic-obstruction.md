# NB-341 — Moving superquadratic phase routing preserves a weighted logarithmic obstruction

- **Status:** proved (author derivation; independent adversarial review pending)
- **Research line:** nyman_beurling
- **Depends on:** NB-304, NB-314, NB-315, NB-331, NB-338, NB-340
- **Classification:** EXACT-DERIVED + SOURCE-SIDE + GROWING-ASPECT-UNIFORMITY + MOVING-SUPERQUADRATIC-WINDOW + INTERIOR-PHASE-ROUTING + WEIGHTED-LOGARITHMIC-OBSTRUCTION + NON-TARGET-AWARE + PRIOR-ART-AUDITED

## Claim

For the actual Nyman finite section and compressed integer dilation, retain

\[
U_n=\operatorname{span}\{g_2,\ldots,g_n\},\qquad
T_{n,m}=P_{U_n}A_m|_{U_n},\qquad
E_{n,m}=\sqrt m\,T_{n,m}-R_n,
\]

with the rank-one comparison \(R_n\) of NB-314. Let \(H_n\ge1\) be **any real sequence with \(H_n=o(n)\)**. There is an **absolute** constant \(c>0\), independent of the sequence, such that for all sufficiently large \(n\),

\[
\boxed{
\inf_{\substack{m\in\mathbb Z\\n\le m\le H_n n^2}}
\left(1+\frac{m}{n^2}\right)\sqrt{\log n}\,
\|E_{n,m}\|\ \ge c.
}
\tag{1}
\]

In particular, uniformly across integer dilations \(n^2\ll m=o(n^3)\) in this sense,

\[
\|E_{n,m}\|\gg\frac{n^2}{m\sqrt{\log n}}.
\tag{2}
\]

The proof supplies an admissible adjacent observer \(\nu_q=g_q-(q-1)g_{q-1}/q\), with \(q\asymp n\), for **each** dilation in the moving window. For \(m>16n^2\), it satisfies a bound of the more precise form

\[
\left|q\langle E_{n,m}g_2,\nu_q\rangle\right|
\gg \frac{n^2}{m}.
\tag{3}
\]

This extends the fixed bounded-quadratic windows of NB-340 to every moving aspect ratio \(m/n^2=o(n)\). It is an **operator/source-channel lower bound**, not a lower bound on the Nyman--Beurling best-approximation distance or a consequence for RH. Its right side can tend to zero.

## 1. The critical Bernoulli identity remains uniform at growing aspect ratio

Write

\[
\mathfrak D(x)=\sum_{k\ge1}\frac{\|kx\|_{\mathbb Z}^{\,2}}{k^2},
\qquad
D_*=\mathfrak D(1/2)=\frac{\pi^2}{32},
\qquad \mathfrak D(0)=0.
\tag{4}
\]

The series converges uniformly, so \(\mathfrak D\) is continuous, even and \(1\)-periodic. The fixed-compact-aspect expansion in NB-338 is sufficient for NB-340, but not when \(m/n^2\to\infty\). We therefore return to the **exact** NB-338 alternating-block identity before its compact-aspect simplification.

Take integers \(8\le q\le n\), \(d\ge q\), \(0\le r<q\), and set

\[
m=dq+r,\qquad
\delta=\frac dq\ge1,\qquad
u=\frac mq=d+\frac rq,\qquad
v=\frac m{q-1}=d+\frac{d+r}{q-1},\qquad
c_q=\frac{q-1}{q}.
\tag{5}
\]

In particular \(c_qv=u\) exactly and \(r\le d\), as required by the alternating source-cell calculation. For \(\varphi(t)=\{t\}-1/2\), define

\[
F(x)=\int_x^\infty\frac{\varphi(t)}{t^2}\,dt,\qquad
S(x)=\sum_{k\ge1}\frac{(-1)^{k+1}B_2(kx)}{k^2},\qquad
B_2(x)=\{x\}^2-\{x\}+\frac16.
\tag{6}
\]

The continuous periodic primitive of \(\varphi\) gives, with an **absolute** remainder valid for every \(x\ge1\),

\[
F(x)=-\frac{B_2(x)}{2x^2}+O(x^{-3}).
\tag{7}
\]

NB-338 obtains from the exact alternating selector blocks, for
\(\mathcal F=\langle E_{n,m}g_2,\nu_q\rangle\),

\[
q\mathcal F=
\frac{qu}{2}\sum_{k\ge1}(-1)^{k+1}
\bigl[F(ku)-F(kv)\bigr].
\tag{8}
\]

As \(v\ge u\ge d\ge q\), inserting (7) and summing its absolutely
convergent error gives, **without an upper bound on \(\delta\)**,

\[
q\mathcal F
=\frac q4\left[\frac{c_q}{v}S(v)-\frac1uS(u)\right]
+O\left(\frac q{u^2}\right).
\tag{9}
\]

The exact Bernoulli-series identity of NB-338 is
\(S(x)=\pi^2/72-\mathfrak D(x)\). Put \(H=\pi^2/72\).
Using \(c_q/v=c_q^2/u\), equation (9) is

\[
q\mathcal F
=\frac q{4u}
\left[
\mathfrak D(u)-\mathfrak D(v)
-(1-c_q^2)\bigl(H-\mathfrak D(v)\bigr)
\right]+O(q/u^2).
\tag{10}
\]

Since \(\mathfrak D\) and \(H-\mathfrak D\) are bounded,
\(1-c_q^2\le2/q\), \(u\ge\delta q\), and
\(q/u=\delta^{-1}+O(1/(q\delta^2))\), this proves the growing-aspect uniform lemma

\[
\boxed{
q\langle E_{n,m}g_2,\nu_q\rangle
=\frac{\mathfrak D(m/q)-\mathfrak D(m/(q-1))}{4\delta}
+O\left(\frac1{q\delta}\right),
}
\quad
\substack{8\le q\le n,\ d/q=\delta\ge1,\\
m=dq+r,\ 0\le r<q\le d}.
\tag{11}
\]

The implied constant is **absolute**. Indeed the Bernoulli remainder
is \(O(q/u^2)=O(1/(q\delta^2))\), while the finite normalization
contributes \(O(1/(q\delta))\). No phase differentiation, Diophantine
separation, or fixed compact interval for \(d/q\) enters this step.

## 2. A fixed finite phase grid survives growing aspect ratios

Choose once and for all an integer \(M\ge4\) large enough that continuity
of \(\mathfrak D\) and (4) ensure

\[
\sup_{\|x\|_{\mathbb Z}\le1/M}\mathfrak D(x)<D_*/8,
\qquad
\inf_{\|x-1/2\|_{\mathbb Z}\le1/M}\mathfrak D(x)>7D_*/8.
\tag{12}
\]

For \(16n^2<m\le H_n n^2\), write \(t=m/n^2>16\) and choose

\[
K=\lceil2t\rceil,\qquad
\theta=K+1/M,\qquad
Q=\operatorname{round}\sqrt{\frac m\theta}.
\tag{13}
\]

Then \(2t\le\theta\le3t\). Rounding implies, uniformly in the
admissible moving range,

\[
\frac n{\sqrt3}+O(1)\le Q\le\frac n{\sqrt2}+O(1),
\qquad
\frac m{Q^2}=\theta+O_M(t/n).
\tag{14}
\]

Thus every \(Q,Q+1,\ldots,Q+M-1\) belongs to the original section
\([8,n]\) for all large \(n\), and every one is comparable to \(n\)
with absolute constants.

Set \(x_j=m/(Q+j)\), \(0\le j<M\). For each of the fixed
\(M-1\) consecutive steps,

\[
x_j-x_{j-1}=
-\frac m{(Q+j-1)(Q+j)}
=-\theta+O_M(t/n).
\tag{15}
\]

Because \(K\) is integral, summation yields the **uniform circular phase approximation**

\[
x_j\equiv x_0-\frac jM+O_M(H_n/n)\pmod1,
\qquad 0\le j<M.
\tag{16}
\]

The error tends to zero uniformly over every integer \(m\) in the
window by the single hypothesis \(H_n=o(n)\).
A complete \(M\)-point rational rotation grid contains a point
within \(1/(2M)\) of \(0\) and another within \(1/(2M)\) of \(1/2\).
For sufficiently large \(n\), the actual phases are within \(1/M\)
of those two locations. By (12),

\[
\max_{j<M}\mathfrak D(x_j)
-\min_{j<M}\mathfrak D(x_j)\ge D_*/2.
\tag{17}
\]

Telescoping along the \(M-1\) adjacent steps therefore gives
some \(1\le j<M\) such that

\[
\left|\mathfrak D\!\left(\frac m{Q+j}\right)
-\mathfrak D\!\left(\frac m{Q+j-1}\right)\right|
\ge\frac{D_*}{2M}.
\tag{18}
\]

Put \(q=Q+j\), \(d=\lfloor m/q\rfloor\), and \(r=m-dq\).
Then \(0\le r<q\), and (14)--(15) imply

\[
\delta=\frac dq=\theta+O_M(H_n/n),
\qquad
t\le\delta\le4t
\tag{19}
\]

eventually, uniformly in the same window. In particular
\(d\ge q\), so the integer remainder condition in (11) is satisfied.

Insert (18) into (11). Since \(q\asymp n\), the absolute
\(O(1/(q\delta))\) remainder is smaller than half the main bound
for all sufficiently large \(n\), uniformly in \(m\). Hence

\[
\boxed{
\left|q\langle E_{n,m}g_2,\nu_q\rangle\right|
\ge\frac{D_*}{16M\delta}
\ge\frac{D_*}{64Mt}.
}
\tag{20}
\]

Unlike a fixed-aspect critical profile, this argument stays uniform
when \(t\to\infty\), because \(M\) is fixed and the accumulated phase
error is \(O_M(t/n)\), not \(O_M(t)\).

## 3. Convert the phase witness into the weighted Hilbert obstruction

The genuine Hilbert norms from NB-304 and NB-314 give

\[
\|\nu_q\|_2^2
\le\frac{2H_{q-2}+1+\pi^2/18}{q^2},
\qquad
\|g_2\|_2=\frac{\sqrt{\log2}}2.
\tag{21}
\]

For \(q\asymp n\), \(\|\nu_q\|_2\le C\sqrt{\log n}/q\)
with an absolute \(C\), so Cauchy--Schwarz and (20) imply

\[
\|E_{n,m}\|
\ge\frac{|\langle E_{n,m}g_2,\nu_q\rangle|}
{\|g_2\|_2\|\nu_q\|_2}
\ge\frac{c_{\rm high}}{t\sqrt{\log n}}
\quad(16n^2<m\le H_n n^2),
\tag{22}
\]

where \(c_{\rm high}>0\) is absolute.

For \(n\le m\le16n^2\), apply the **already proved**
fixed-window uniform theorem NB-340 with \(B=16\).
It yields an absolute \(c_{\rm low}>0\) such that for all
sufficiently large \(n\),

\[
\inf_{n\le m\le16n^2}
\sqrt{\log n}\,\|E_{n,m}\|\ge c_{\rm low}.
\tag{23}
\]

Since \(1+t\ge1\) in (23) and \((1+t)/t\ge1\) in (22),
choosing \(c=\min(c_{\rm low},c_{\rm high})>0\) proves (1).
The constants do not depend on \(H_n\); only how large \(n\)
must be depends on the rate at which \(H_n/n\to0\).

The scale (2) is equivalent to the high-window part of (1).
There is **no assertion at \(m\asymp n^3\)**: the accumulated
rational-grid phase error in (16) may then be order one, and
the present proof no longer supplies the requisite fixed phase contrast.

## 4. Falsification controls, prior-art scope, and limits

- **Finite-section control.** The selected \(q\) always belongs to
  the ambient \(U_n\); the actual operator \(T_{n,m}\), rank-one
  comparator \(R_n\), and source \(g_2\) are never replaced by a
  smaller ambient section.
- **Growing-parameter control.** The compact-\(\delta\)
  \(O(1/q)\) statement of NB-338 is not extrapolated to growing
  \(\delta\). Equation (11) is rederived from its exact
  alternating-block representation and an absolute
  Bernoulli-tail estimate, keeping the \(q-1\) denominator.
- **Arithmetic admissibility.** Taking the quotient remainder
  \(r<q\) is insufficient alone for NB-338; here \(d\ge q\)
  is separately checked, ensuring \(r\le d\).
- **Quantifier control.** The same fixed \(M\) and absolute
  constants work for every \(m\) in a given moving range.
  The required large-\(n\) threshold may depend on \(H_n\),
  but the constant in (1) does not.
- **Matched generic control.** The finite rotation-grid lemma
  works for any continuous periodic profile separating two
  phases. Arithmetic information enters only through the
  exact Nyman coefficient formula (8)--(11) and the
  physical witness norms (21).

The nearest external context remains the discrete
Nyman--Beurling approximation literature (Báez-Duarte,
*Arithmetical Aspects of Beurling's Real Variable
Reformulation of the Riemann Hypothesis*, arXiv:math/0011254),
the multiplicative fractional-part autocorrelation of
Báez-Duarte--Balazard--Landreau--Saias (arXiv:math/0306251),
and the Wilton/regularity analysis of Balazard--Martin
(arXiv:1305.4395). Those sources provide the surrounding
approximation and autocorrelation setting; the finite-grid
argument and new growing-aspect bound are elementary
line-local deductions from NB-338 and NB-340. A targeted
literature check did not locate this exact finite-section
moving-window bound, but **no claim of independent
bibliographic novelty** is made. No external theorem is
load-bearing; the existing SOURCES.md requires no change.

NB-315 gives the compatible upper bound
\(\|E_{n,m}\|\le C_{\rm mix}n^{5/2}/m\).
Its scale is not contradicted by (2): the estimates differ
by a factor comparable to \(\sqrt{n\log n}\).
The new lower bound vanishes when \(m\gg n^2\);
it neither rules out absolute rank-one operator mixing
nor strengthens the known upper convergence threshold.
Above all, the test uses an available **source/probe**
direction, not the actual moving first-free Ford target
or a norm-certified Nyman distance. The target-occupation,
finite-section conditioning and off-critical contraction
bridges remain absent. Neither RH nor its negation follows.

## Research consequence

The fixed-\(B\) quantifier in NB-340 is no longer a barrier
to retaining an adjacent source witness: the same mechanism
continues through every sequence \(n^2\ll m=o(n^3)\), but
its certified strength decays as \(n^2/m\), up to the
Hilbert factor \(1/\sqrt{\log n}\). The genuinely new
mathematical input is the \(O(1/(q\delta))\) error
uniform in an **unbounded** critical aspect ratio,
combined with a rational phase grid whose accumulated
rounding error remains \(o(1)\) exactly while \(m=o(n^3)\).
This does not resolve target occupation or establish
a transition at the cubic boundary.
