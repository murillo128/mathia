# ANF-210 — Sharp triple-gap phase balance gives a cubic notch witness

**Status:** EXACT-DERIVED + SHARP-ASYMPTOTIC-CONSTANT + REAL-THREE-SITE-WITNESS.
The real Montgomery--Taylor triple gap satisfies
`lim_(H->infinity) H^4 kappa_H=3/(2 pi^4)`.
The minimizing leading phase is displaced three quarters of the way
from an integer toward the nearby kernel zero. The same displacement
gives a three-site configuration beating every real configuration
supported on at most two sites when `a=lambda eta^3`, for every fixed
`lambda>48/[pi^2(40-3 pi^2)]`. This is an upper bound on the initial
two-site window, not its exact transition constant.

## Kernel and claims

Use the Fourier convention `f_hat(x)=int f(u) exp(-2 pi i u x) du` and
\[
g(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin(1/\sqrt2)}
\mathbf1_{[-1/2,1/2]}(u),\quad J_0=g*g,\quad
F=\widehat J_0=K^2,
\]
\[
K(x)=\frac{\cos(\pi x)-b x\sin(\pi x)}{1-dx^2},
\qquad b=\sqrt2\pi\cot(1/\sqrt2),\quad d=2\pi^2.
\tag{1}
\]
Continue the removable values. For `H>0`, put
\[
\kappa_H=\min_{u,v\ge0,\ u+v\le H}
\{F(u)+F(v)+F(u+v)\}.
\tag{2}
\]
The compact minimum exists. The sharp asymptotic is
\[
\boxed{\lim_{H\to\infty}H^4\kappa_H=\frac3{2\pi^4}.}
\tag{3}
\]

For the notch, write
\[
\tau_\eta(u)=(1-|u|/\eta)_+,\quad
\Phi_\eta(x)=\widehat{\tau_\eta}(x)
=\eta\operatorname{sinc}^2(\eta x),\quad
J_{\eta,a}=J_0-a\tau_\eta,
\tag{4}
\]
where `sinc(t)=sin(pi t)/(pi t)`, continuously at zero. The parameter
`a` is removed spectral height. For a finite nonempty real multiset
with distinct sites `x_i` and positive integer multiplicities `m_i`, set
\[
L(W)=\sum_i\ell(m_i),\qquad
\ell(1)=1,\quad\ell(m)=2m\ (m\ge2),
\]
\[
Q_{\eta,a}(W)=\frac{\int J_{\eta,a}(u)
|\sum_i m_i e^{-2\pi iux_i}|^2du}{L(W)},\qquad
q^{\mathbb R}_{\eta,a}=\inf_W Q_{\eta,a}(W).
\tag{5}
\]
There is no span or cardinality constraint in (5). For every fixed
\[
\lambda>\lambda_0:=\frac{48}{\pi^2(40-3\pi^2)}
=0.4680328541\ldots,
\tag{6}
\]
and all sufficiently small `eta>0`, the explicit simple triple below
satisfies
\[
\boxed{Q_{\eta,\lambda\eta^3}(W_\eta)
<1-2\lambda\eta^4
\le Q_{\eta,\lambda\eta^3}(Z)}
\tag{7}
\]
for every real multiset `Z` supported on at most two distinct sites.
Small width ensures `eta<=1/4` and `a<=1/20`, so the dominated
positive-spectrum regime of ANF-209 applies.

## The phase-balanced upper witness

Define
\[
c_*:=\frac3{4b\pi},\qquad r_n=n+\frac{c_*}{n}
\quad(n\in\mathbb N).
\tag{8}
\]
Taylor expansion at the integer, with parity retained, gives
\[
\cos(\pi r_n)-b r_n\sin(\pi r_n)
=(-1)^n\{\tfrac14+O(n^{-2})\},
\]
\[
\cos(2\pi r_n)-2b r_n\sin(2\pi r_n)
=-2+O(n^{-2}).
\]
Consequently
\[
F(r_n)=\frac1{16d^2n^4}+O(n^{-6}),\qquad
F(2r_n)=\frac1{4d^2n^4}+O(n^{-6}),
\]
\[
\boxed{2F(r_n)+F(2r_n)
=\frac3{8d^2n^4}+O(n^{-6}).}
\tag{9}
\]
Choose `n=floor(H/2)-1`. For all large `H`, `2r_n<=H` and
`n/H->1/2`; (9) proves the upper limit in (3) is at most
`6/d^2=3/(2 pi^4)`. This works for every large real `H`, not only
a special sequence of spans.

## Low-energy triples cannot have a sublinear gap

For the lower limit, consider any sequence `H->infinity` and
`u,v>=0`, `u+v<=H`, for which
\[
F(u)+F(v)+F(u+v)\le C H^{-4}.
\tag{10}
\]
It suffices to analyze such sequences by the upper construction.
The existing coarse gap, ANF-114 equation (1), says
\[
F(u)+F(v)+F(u+v)
\ge\frac1{16[1+d(u+v)^2]^2}.
\tag{11}
\]
Thus `u+v` is bounded below by a positive constant times `H`.
Only this coarse consequence is needed from that finding; Wang's
Lemma 3.2 gives an alternative sufficient constant in (11).

The exact identity from (1), for `x>=1`, implies
\[
xK(x)=\frac bd\sin(\pi x)+O(x^{-1}).
\tag{12}
\]
Suppose along a subsequence `u/H->0`. Then `v` and `u+v` are
comparable to `H`. Equations (10)--(12) give
`sin(pi v)=O(H^(-1))` and `sin(pi(u+v))=O(H^(-1))`.
Subtracting angles gives `sin(pi u)=O(H^(-1))`, hence
`|cos(pi u)|->1` and `b u sin(pi u)->0`. But the numerator identity
\[
N(u):=\cos(\pi u)-bu\sin(\pi u)=(1-du^2)K(u)
\]
and (10) imply
`|N(u)|<=sqrt(C)(1+du^2)H^(-2)->0`, a contradiction.
The same argument excludes `v/H->0`. It includes bounded or zero
gaps and does not divide through a removable singularity.

After taking a subsequence, therefore,
\[
u/H\to p>0,\quad v/H\to q>0,\quad p+q\le1.
\tag{13}
\]
Now (12) also gives `sin(pi u),sin(pi v)=O(H^(-1))`.
Choose the nearest integers `n,m`. There are bounded real phase
offsets, with subsequential limits `s,t`, such that
\[
H(u-n)\to s,\qquad H(v-m)\to t.
\tag{14}
\]
This reduces every possible low-energy sequence to the same finite
phase problem; integer-like spacing was not assumed in the lower bound.

## An additive phase constraint fixes the sharp constant

Put `B=1/d` and `A=b pi/d`. Expanding (1) with (13)--(14) gives
\[
(-1)^nH^2K(u)\to R_1:=\frac{As}{p}-\frac{B}{p^2},\qquad
(-1)^mH^2K(v)\to R_2:=\frac{At}{q}-\frac{B}{q^2},
\]
\[
(-1)^{n+m}H^2K(u+v)\to
R_3:=\frac{A(s+t)}{p+q}-\frac{B}{(p+q)^2}.
\tag{15}
\]
The offsets of the two adjacent gaps add. Their three residuals obey
\[
-pR_1-qR_2+(p+q)R_3
=B\left(\frac1p+\frac1q-\frac1{p+q}\right).
\tag{16}
\]
Conversely, as `(s,t)` vary, they span exactly this affine plane.
The minimum squared residual is its squared distance to the origin:
\[
\begin{aligned}
R_1^2+R_2^2+R_3^2
&\ge
\frac{B^2(1/p+1/q-1/(p+q))^2}{p^2+q^2+(p+q)^2}\\
&=\frac{B^2(p^2+pq+q^2)}{2p^2q^2(p+q)^2}.
\end{aligned}
\tag{17}
\]
This is Cauchy--Schwarz with equality precisely when the residual
vector is proportional to `(-p,-q,p+q)`.

Let `l=p+q` and `z=pq<=l^2/4`. The final expression in (17) is
`B^2(l^2-z)/(2z^2 l^2)`. Subtracting `6B^2/l^4` leaves
`B^2(l^2-4z)(l^2+3z)/(2z^2 l^4)>=0`, so
\[
\frac{B^2(p^2+pq+q^2)}{2p^2q^2(p+q)^2}
\ge\frac{6B^2}{(p+q)^4}\ge6B^2.
\tag{18}
\]
Equations (15)--(18) prove the lower limit in (3).

Equality in this limiting problem forces `p=q=1/2` and
`(R_1,R_2,R_3)=(-B,-B,2B)`. Thus every sequence attaining
the constant in (3) has, with nearest integers as above,
\[
\frac uH,\frac vH\to\frac12,\qquad
H(u-n),H(v-m)\to\frac3{2b\pi}.
\tag{19}
\]
The exact zero near a large integer has displacement
`1/(b pi n)+O(n^(-3))`, by the numerator equation in (1).
The shift in (8) is three quarters of this leading displacement.
Making both adjacent interactions zero is suboptimal: it leaves all
the additive incompatibility in the long edge. The minimum instead
distributes that residual among all three edges as (16) requires.

## The same triple ends two-site attainment at a concrete cubic coefficient

Given any sufficiently small `eta>0`, let
\[
n=\left\lfloor\frac1{4\eta}\right\rfloor,\qquad
W_\eta=\{0,r_n,2r_n\}.
\tag{20}
\]
Its three sites are simple and `L(W_eta)=3`. The exact energy is
\[
Q_{\eta,a}(W_\eta)
=1+\frac23\{2F(r_n)+F(2r_n)\}
-a\eta\left[1+\frac43\operatorname{sinc}^2(\eta r_n)
 +\frac23\operatorname{sinc}^2(2\eta r_n)\right].
\tag{21}
\]
Since `eta n->1/4`, (9) and the exact values
`sinc^2(1/4)=8/pi^2`, `sinc^2(1/2)=4/pi^2` yield, for fixed `lambda`,
\[
Q_{\eta,\lambda\eta^3}(W_\eta)
=1+\eta^4\left[\frac{16}{\pi^4}
-\lambda\left(1+\frac{40}{3\pi^2}\right)\right]
+o(\eta^4).
\tag{22}
\]

For any real multiset `Z` supported on one or two sites, let
`D=sum m_i^2` and `N=sum m_i`. Real pair positivity gives `E_0>=D`,
while `E_tau<=eta N^2<=2eta D` and `D>=L`. Hence
\[
Q_{\eta,a}(Z)\ge1-2a\eta\qquad(2a\eta<1).
\tag{23}
\]
The difference between (22) and (23)'s floor, divided by `eta^4`,
tends to
\[
\frac{16}{\pi^4}
-\lambda\left(\frac{40}{3\pi^2}-1\right),
\tag{24}
\]
which is strictly negative exactly when `lambda>lambda_0`.
This proves (7) for all sufficiently small widths, including widths
not of the form `1/(4n)`.

For the initial interval `A_2(eta)` defined in ANF-209, it follows that
\[
\boxed{\limsup_{\eta\downarrow0}\frac{A_2(\eta)}{\eta^3}
\le\lambda_0.}
\tag{25}
\]
The earlier large-lattice bound `(8 pi^2)^3` can therefore be replaced
asymptotically by (6), and only three simple sites are needed for this
upper obstruction. Neither (3) nor (25) asserts that a triple minimizes
the full notch energy, or that the chosen scaled gap `1/4` optimizes
all triple notch witnesses. At `lambda=lambda_0`, (24) is zero and
this leading-order test gives no strict comparison.

## Prior art, checks and evidence boundary

The kernel in (1) is classical; see [Carneiro--Chandee--Littmann--Milinovich,
Corollary 14](https://arxiv.org/pdf/1406.5462). [Wang,
*Proportions of the non-trivial zeros of the Riemann zeta function*,
Lemma 3.2](https://arxiv.org/html/2609.24167v1#S3) already proves the
fourth-power lower bound
`(sqrt(5)-2)^2/(1+2 pi^2 H^2)^2`, using the same numerator addition
mechanism as ANF-114. The fourth-power lower-bound mechanism is
therefore prior art. That lemma does not determine (3), (19) or the
shrinking-notch consequence (25). No zero-counting theorem from
Wang is used here.

[Knausgård, sections 7.1--7.2](https://arxiv.org/html/2610.08965v1#S7.SS1)
studies constrained-density real pair energy and relaxed periodic
trial states. [Sütő's compact-Fourier ground-state work](https://arxiv.org/abs/math-ph/0508004)
is another classical neighboring framework. Neither supplies the
free-span three-point asymptotic or this changing-width notch
comparison. Searches by the exact kernel, three-point gap, phase
relaxation and weak pair-potential perturbations did not identify the
sharp constant; no exhaustive novelty claim is made. The new local
step is the complete reduction of every low-energy triple to the
affine residual plane (16), followed by its sharp phase balance.

As noncertifying checks, stable parity-reduced double-precision
evaluation at `n=10,100,1000,10000` gave
`(2r_n)^4[2F(r_n)+F(2r_n)]` approaching
`0.015398973382...=3/(2 pi^4)`. The notch comparison (24) was
checked at `lambda=lambda_0-0.01,lambda_0+0.01,0.5`; the scaled
differences converged to the predicted values with the expected
signs. Exact rational arithmetic at 1,600 positive `(p,q)` pairs
checked the algebraic identity (17) and bound (18). These samples
are checks only; the proof is (8)--(24), with no numerical optimizer,
interval certification or Lean proof asserted.

The lower-bound audit must retain the exclusion of sublinear gaps,
the additive offset in the long edge, and the parity in (15).
The notch audit must retain the diagonal and the `2/3` ordered-pair
normalization in (21), as well as all multiplicities in (23).
The exact asymptotic is not an effective optimal bound at each finite
span. The notch threshold is sufficient for a witness, not a proved
phase-transition value. Real support is essential throughout; the
unrestricted complex exposure problem remains open. No improved
zeta-zero proportion, zero-density estimate or RH conclusion follows.
