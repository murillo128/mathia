# XF-208 — smooth tapers do not uniformize vanishing collision coverage

**Status:** `EXACT-DERIVED` + `NEGATIVE/OBSTRUCTION` + `STRUCTURAL/BOUNDARY`.

The positive collision coefficient in XF-028 is a fixed-weight statement.
It is not uniform when the taper and the colliding gap vary together.
There are complete periodic real-entire heat flows and nonnegative tapers

\[
a_j^{(M)}=A((j+1)/M),\qquad A\in C_c^\infty(\mathbb R),
\]

with all the following properties at the time under consideration:

- every gap is positive and at most two;
- the ordered roots satisfy \(|x_i-i|\le1\), so interval counting differs
  from unit-density lattice counting by an absolute constant;
- the taper has a width-\(M\) unit plateau, where adjacent-pair coverage is
  \(W_k=a_{k-1}+a_k=2\);
- for every fixed \(r\ge1\), \(\|\Delta^r a^{(M)}\|_\infty=O_r(M^{-r})\);
- the small gap responsible for the adverse derivative is itself covered:
  \(W_0=a_0>0\).

Nevertheless the normalized triple-discriminant sum of XF-030 satisfies

\[
\boxed{
\mathcal K_{a^{(M)}}'(0)
=-\frac{50}{441}e^{M^2/2}+O(e^{-M^2/9})\longrightarrow-\infty.
}
\tag{1}
\]

Thus absolute taper smoothness, bounded upper gaps, bounded counting
discrepancy, and a positive-coverage core do not by themselves give a
uniform lower bound for the derivative of the **whole** tapered sum.
The defect is a covered but degenerating edge layer, not a negative
interior density or a failure of the fixed-weight collision asymptotic.
This does not rule out a better choice of taper, a source-dependent
boundary selection, a gap floor, or a time-integrated estimate.

A second smooth profile isolates a stronger boundary for a proposed
repair: even a uniform bound on neighboring-weight-squared divided by
coverage, at every covered pair, does not force a vanishing localization
loss. For that profile the same complete-flow construction gives
\(\mathcal K_a'(0)\to-50/441\); see Section 3a. Bounded edge cost and
edge cost tending to zero are different requirements.

## 1. A complete heat-flow control with a local spacing defect

Let \(M\ge6\) be an integer, \(N=8M\), and \(0<\epsilon<1/4\). In one
period take

\[
b_0=0,\quad b_1=\epsilon,\quad b_2=1+\epsilon,
\quad b_j=j\quad(3\le j<N),
\qquad x_{Nm+j}=Nm+b_j.
\tag{2}
\]

The gaps are one except

\[
g_0=\epsilon,\qquad g_1=1,\qquad g_2=2-\epsilon
\tag{3}
\]

and their periodic copies. In particular \(|x_i-i|\le1\) globally.
This gives the counting assertion without a limiting argument.

The entire function

\[
f_{N,\epsilon}(z)=\prod_{j=0}^{N-1}
\sin\frac{\pi(z-b_j)}N
\tag{4}
\]

has exactly this simple real zero set. Its finite Fourier sum defines
\(f_t=e^{-t\partial_z^2}f_{N,\epsilon}\) for every real \(t\).
For each fixed \(N,\epsilon\), all roots remain real and simple for
sufficiently small \(|t|\): each of the \(N\) roots per period continues
by the real implicit function theorem. Multiplication by
\(e^{\pi iz}\) turns the Fourier sum into a degree-\(N\) polynomial in
\(e^{2\pi iz/N}\) with nonzero constant and leading coefficients, so
these continued roots account for every root. No uniform time interval
in \(M\) or \(\epsilon\) is claimed.

At the initial time their exact velocities are

\[
v_j=x_j'=\frac{f''(b_j)}{f'(b_j)}
=\frac{2\pi}{N}\sum_{k\ne j}
\cot\frac{\pi(b_j-b_k)}N.
\tag{5}
\]

This includes all periodic images; it is not a finite truncation of the
infinite gap equation. The same formula follows from the classical
cotangent partial fraction, [DLMF 4.22.3](https://dlmf.nist.gov/4.22.E3).

Uniformly for \(N=8M\) and \(0<\epsilon<1/4\), (5) gives

\[
v_0=-2/\epsilon+O(1),\quad v_1=2/\epsilon+O(1),
\quad v_2,v_3,v_4=O(1).
\tag{6}
\]

Here uniformity matters. To check it, compare the complete root set with
the integer lattice: in each period only roots 1 and 2 have moved, to
\(\epsilon\) and \(1+\epsilon\). The lattice principal-value field is
\(\pi\cot(\pi z)\). Remove its local poles before evaluating at the
roots in (6); only the mutual \(0,\epsilon\) pole remains singular.
Each replacement in a nonzero period changes the reciprocal field by
\(O((|m|N)^{-2})\), summably and uniformly. The finitely many other
local distances are bounded below. This proves (6), and also bounds the
derivative of the exterior field between 0 and \(\epsilon\). Thus the
more precise difference is

\[
v_1-v_0=4/\epsilon+O(\epsilon).
\tag{7}
\]

## 2. The full weighted derivative has an explicit adverse minimum

Use the exact XF-030 notation

\[
\mathcal J_j=F(d_j),\quad d_j=\log(g_{j+1}/g_j),\quad
\phi(r)=-\frac{(r-1)(r+2)(2r+1)}{(r+1)(r^2+r+1)}.
\]

For \(y_j=\log g_j\), the complete derivative is
\(\mathcal J_j'=\phi(g_{j+1}/g_j)(y_{j+1}'-y_j')\).
Equations (3), (6), and (7) imply

\[
y_0'=4/\epsilon^2+O(1),\qquad
y_1'=-2/\epsilon+O(1),\qquad y_2',y_3'=O(1).
\tag{8}
\]

Since \(\phi(1/\epsilon)=-2+O(\epsilon)\) and
\(\phi(2-\epsilon)=-20/21+O(\epsilon)\), it follows that

\[
\mathcal J_0'=8/\epsilon^2+O(1/\epsilon),\qquad
\mathcal J_1'=-\frac{40}{21\epsilon}+O(1),\qquad
\mathcal J_2'=O(1).
\tag{9}
\]

All starts \(3\le j\le3M\) have two equal gaps, and hence
\(\mathcal J_j'=0\) exactly, regardless of the exterior field.
The two negative-index triples meeting the defect will have zero weight.
There is no other copy of the defect inside the taper support.

For a taper supported on \(0\le j<3M\), write
\(\alpha=a_0>0,\ \beta=a_1>0,\ \gamma=a_2\ge0\). Therefore

\[
\mathcal K_a'
=\frac{8\alpha}{\epsilon^2}
-\frac{C\beta}{\epsilon}
+O(\alpha/\epsilon+\beta+\gamma),
\qquad C=40/21,
\tag{10}
\]

with an absolute remainder constant for this family. Completing the
square in \(1/\epsilon\) shows that the displayed leading terms attain
their minimum at

\[
\epsilon=\frac{16\alpha}{C\beta}
=\frac{42\alpha}{5\beta},\qquad
\min\left(\frac{8\alpha}{\epsilon^2}
-\frac{C\beta}{\epsilon}\right)
=-\frac{50}{441}\frac{\beta^2}{\alpha}.
\tag{11}
\]

When \(\alpha/\beta\to0\), this choice is within the small-gap regime.
The relevant edge quantity is therefore the **neighboring weight squared
divided by collision coverage**, here \(a_1^2/W_0\). An absolute bound on
\(\Delta a\) does not control it.

## 3. One fixed smooth profile makes the defect grow with the buffer

Choose a fixed nonnegative smooth profile \(A\), bounded by one, such that

\[
A(s)=0\ (s\le0\text{ or }s\ge3),\quad
A(s)=e^{-1/s^2}\ (0<s\le1/2),\quad
A(s)=1\ (1\le s\le2).
\tag{12}
\]

Smooth interpolation on the two remaining intervals supplies such a
profile. Put \(a_j=A((j+1)/M)\). Then

\[
\alpha=e^{-M^2},\quad \beta=e^{-M^2/4},\quad
\gamma=e^{-M^2/9},\qquad
\epsilon_M=\frac{42}{5}e^{-3M^2/4}.
\tag{13}
\]

The finite-difference bound follows by applying the fundamental theorem
of calculus \(r\) times to \(A\). The plateau has
\(W_k=2\) for \(M\le k\le2M-1\), whereas the colliding pair at index
zero has \(W_0=e^{-M^2}>0\). Its distance from the plateau grows like
\(M\), so this is a widening-buffer family with a fixed smooth profile.

Substitution of (13) into (10)--(11) proves (1):
\(\beta^2/\alpha=e^{M^2/2}\) and the remainder is
\(O(\beta+\gamma)=O(e^{-M^2/9})\).
The negative term is the actual total derivative, not a negative term
in a summation-by-parts representation whose companions were omitted.

## 3a. Bounded relative edge weights still permit a fixed negative loss

Choose instead a fixed smooth profile \(B\), positive on \((0,3)\),
zero outside that interval, and bounded by one, with
\[
B(s)=e^{-1/s}\quad(0<s\le1/2),\qquad
B(s)=1\quad(1\le s\le2),\qquad
B(s)=e^{-1/(3-s)}\quad(5/2\le s<3).
\tag{14}
\]
Positive smooth interpolation gives such a profile. Set
\(a_j=B((j+1)/M)\), still with \(N=8M\), and use the same roots
(2). All fixed-order taper differences are \(O_r(M^{-r})\), and the
plateau again has coverage two. Now
\[
\alpha=e^{-M},\qquad \beta=e^{-M/2},\qquad
\gamma=e^{-M/3},\qquad
\epsilon_M=\frac{42}{5}e^{-M/2}.
\tag{15}
\]
In particular the adverse pair has strictly positive coverage and
\(\beta^2/W_0=\beta^2/\alpha=1\). The uniform expansion (10) gives
\[
\boxed{\mathcal K_a'(0)=-\frac{50}{441}+O(e^{-M/3}).}
\tag{16}
\]
No term elsewhere in the plateau has been dropped: starts from 3 to the
end of the support still have equal adjacent gaps, so their instantaneous
derivative is exactly zero.

The relative bound holds across **all covered pairs**, not just at the
chosen small gap. Define
\[
R_M=\sup_{k:W_k>0}
\frac{(a_{k-2}+a_{k+1})^2}{W_k},\qquad
W_k=a_{k-1}+a_k.
\tag{17}
\]
Then \(R_M\le C_B\), uniformly for all sufficiently large \(M\).
For a left-edge index whose relevant weights lie in the first region
of (14), the inward neighbor satisfies
\[
\frac{a_{k+1}^2}{W_k}
\le\frac{a_{k+1}^2}{a_k}
=\exp\!\left[-\frac{Mk}{(k+1)(k+2)}\right]\le1,
\qquad k\ge0.
\tag{18}
\]
The outward weight obeys \(a_{k-2}\le a_k\le1\), with weights before
the support taken as zero, so \(a_{k-2}^2/W_k\le1\) as well.
The inequality \((u+v)^2\le2(u^2+v^2)\) bounds (17) there by four.
Reflection about the right endpoint proves the same bound at that
edge. At all remaining indices, a denominator weight lies in a fixed
compact subinterval of \((0,3)\), on which \(B\) has a positive
minimum; the numerator is at most four. This proves the stated uniform
bound without imposing a positive lower bound on every \(W_k\).

The restriction \(W_k>0\) in (17) is essential. A compact taper also
has uncovered pairs just outside its support; (17) asserts no bound
there. In the present control those exterior gaps are of ordinary
size, and the adverse pair is the **covered** pair at index zero.
Thus the fixed negative limit does not exploit an uncovered collision.

Equations (15)--(18) rule out a universal estimate
\(\mathcal K_a'(0)\ge-o(1)\) from absolute smoothness, positive core
coverage, the upper-gap/counting hypotheses, and bounded \(R_M\) alone.
They do not rule out an order-one lower bound. The mechanism is the
same quadratic-versus-linear collision balance as (10)--(11), now at
its bounded-cost threshold; it is not a separate interior obstruction.

## 4. What is excluded, and what remains open

For each **fixed** taper, (10) is eventually positive as
\(\epsilon\downarrow0\), exactly as XF-028 requires. In (13), coverage
shrinks simultaneously and the gap is chosen at the negative minimum
before that positive regime. The two limits are not interchangeable.

This example excludes a uniform pointwise localization theorem based
only on the listed absolute smoothness, core-coverage, upper-gap, and
counting hypotheses. It also identifies a concrete repair obligation:
control relative edge weights such as \(a_{j+1}^2/(a_{j-1}+a_j)\), avoid
small gaps at the selected boundary, or supply an estimate that uses
additional source or time information. Section 3a shows that merely
bounding these ratios on covered pairs does not give an error tending
to zero; the particular singular edge cost in (11) must instead vanish
or be offset by additional production. No sufficiency theorem for such
a repair is proved here.

The defect remains at a degenerating taper edge. It does **not** answer
the stronger question of negative aggregate production in a region
with a uniform coverage floor, nor construct an adverse configuration
with gaps bounded uniformly below. It therefore narrows, rather than
closes, the overlap-discriminant clue. In particular this is not the
genuinely interior/nonlocal obstruction sought in its strongest test.

Nor is instantaneous divergence a time-integrated obstruction: the
small-pair evolution occurs on the shrinking scale \(\epsilon_M^2\).
The construction supplies no adverse integral over fixed time and no
uniform real-simple time interval. Its bounded counting discrepancy
does not make it an Xi source configuration. The controls are periodic
real-entire functions, with no assertion of Xi's even symmetry,
arithmetic source law, global counting asymptotic, or transition time.
No upper or lower bound on the de Bruijn--Newman constant follows.

## 5. Prior art, validation, and mathematical delta

The reciprocal zero law and the need to control boundary interaction
are classical. Rodgers--Tao's [primary paper](https://arxiv.org/abs/1801.05914),
Section 9 (proof of Proposition 28 in arXiv v5), selects boundaries with
a quantitative separating gap for its localized-energy propagation.
It does not assert that arbitrary smooth predetermined tapers suffice.
The cotangent sum is classical, as is completing a square to absorb a
linear singular term into positive quadratic production.

The new line-local content is the explicit joint limit (13) and its
complete heat-flow realization: even infinitely smooth widening tapers
and **strictly positive** pair coverage can have arbitrarily negative
full production when the coverage degenerates relative to the adjacent
weight. This strengthens the previous warnings about uncovered edges
and coefficient-only localization into a quantitative counterexample.
No new general log-gas theorem or literature-wide novelty is claimed.
The bounded-ratio profile (14) is a further specialization of the same
balance, kept here to delimit the proposed relative-weight repair rather
than treated as an independent mechanism. It separates an order-one
edge allowance from the vanishing error required by a stronger
localization estimate.

The proof retains all periodic images and supplies uniform remainder
bounds before taking the joint limit. Exact rational algebra checks
\(\phi(2)=-20/21\), the leading Laurent coefficients, and the optimizer
and minimum in (11). These checks support the displayed analytic proof;
no numerical trajectory, finite truncation, or formal Lean verification
is being used as evidence for it.
