# ANF-211 — Four-point notch descent is invisible to every three-point test

**Status:** EXACT-DERIVED + EXACT-RATIONAL-CERTIFICATE + REAL-CARDINALITY-SEPARATION.
At the fixed cubic coefficient `a=(5/12) eta^3`, and for every sufficiently
small width, an explicit simple real four-point configuration has lower
normalized notch energy than every real multiset of total cardinality at
most three. The minimum in that capped class is still attained by a simple
pair. Thus the loss of two-site optimality at cubic width cannot be decided
by the best three-point test. This does not identify the first transition,
the unrestricted minimizer, or the complex floor.

## Object and precise separation

Use `f_hat(x)=int f(u) exp(-2 pi i u x) du` and
\[
g(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin(1/\sqrt2)}
\mathbf1_{[-1/2,1/2]}(u),\quad J_0=g*g,\quad F=\widehat J_0=K^2,
\]
\[
K(x)=\frac{\cos(\pi x)-b x\sin(\pi x)}{1-dx^2},
\qquad b=\sqrt2\pi\cot(1/\sqrt2),\quad d=2\pi^2.
\tag{1}
\]
Continue removable values. Put
\[
\tau_\eta(u)=(1-|u|/\eta)_+,\quad
J_{\eta,a}=J_0-a\tau_\eta,\quad
\widehat{\tau_\eta}(x)=\eta\operatorname{sinc}^2(\eta x),
\tag{2}
\]
where `sinc(t)=sin(pi t)/(pi t)`, continuously at zero. For a nonempty
finite real multiset, let its distinct sites and multiplicities be
`x_i,m_i`, and write
\[
N(W)=\sum_i m_i,\quad L(W)=\sum_i\ell(m_i),\qquad
\ell(1)=1,\quad\ell(m)=2m\quad(m\ge2),
\]
\[
Q_{\eta,a}(W)=\frac{\int J_{\eta,a}(u)
|\sum_i m_i e^{-2\pi iux_i}|^2du}{L(W)},\qquad
q^{\mathbb R}_{\le k}=\inf_{N(W)\le k}Q_{\eta,a}(W).
\tag{3}
\]
The cap counts total multiplicity, not just distinct sites. There is no
span or separation restriction. Throughout the claim fix
\[
\lambda=5/12,\qquad a=\lambda\eta^3.
\tag{4}
\]
Small width ensures `eta<=1/4` and `a<=1/20`; in particular the positive,
dominated notch regime of ANF-209 applies.

For all sufficiently small `eta>0`,
\[
\boxed{
q^{\mathbb R}_{\le4}\le Q_{\eta,a}(W_\eta)
<1-2\lambda\eta^4-\frac{\eta^4}{500}
<1-2\lambda\eta^4
\le q^{\mathbb R}_{\le3}=q^{\mathbb R}_{\le2}.
}
\tag{5}
\]
The last minimum is attained by a simple pair, and
\[
q^{\mathbb R}_{\le3}=1-2\lambda\eta^4+O(\eta^6).
\tag{6}
\]
The explicit witness uses four simple sites. In (1)'s normalization set
\[
(t_0,t_1,t_2,t_3)=(0,2/3,7/6,11/6),\qquad
n=\left\lfloor\frac3{10\eta}\right\rfloor,
\]
\[
\boxed{W_\eta=\left\{i n+\frac{t_i}{b\pi n}:0\le i\le3\right\}.}
\tag{7}
\]
Only the lower-order phase offsets are nonuniform. Taking four exact
integer-spaced sites gives a different leading source cost.

## A uniform phase-and-notch inequality for triples

Write `s(x)=(sin x/x)^2`, with `s(0)=1`. For all `x,y>0`, define
\[
C(x,y)=\frac{x^2+xy+y^2}{8x^2y^2(x+y)^2}.
\]
The finite certificate below proves the global bound
\[
\boxed{
C(x,y)-\frac5{12}\{s(x)+s(y)+s(x+y)-3/2\}\ge\frac1{1000}.
}
\tag{8}
\]
The variables here include the factor `pi`; they are not the arguments
of `sinc` in (2).

Here are the analytic reductions outside the finite box. By symmetry
assume `x<=y`. If `y>=3`, then
`S:=s(x)+s(y)+s(x+y)<=1+2/9`, so the left side of (8) is at least
`25/216`. If `2<=y<=3`, then `S<=3/2`, while `C` decreases in each
positive variable and `C(x,y)>=C(3,3)=1/864`. The monotonicity follows,
for example, by differentiating its logarithm: with `A=x^2+xy+y^2`,
`(2x+y)/A-2/x-2/(x+y)<0`.
If `y<=2` and `x<=1/10`, then
\[
C(x,y)\ge\frac1{8x^2(x+y)^2}\ge\frac{10000}{3528},
\qquad \frac5{12}(S-3/2)\le\frac58.
\]
Thus only `[1/10,2]^2` needs a certificate.

For `t>=0` put
\[
P(t)=1-t^2/3+2t^4/45-t^6/315+2t^8/14175,\qquad
U(t)=\begin{cases}P(t),&t\le2,\\t^{-2},&t>2.\end{cases}
\tag{9}
\]
For every `z>=t>=0` one has `s(z)<=U(t)`. When `t>2`, use
`sin^2 z<=1`. When `t<=2`, the degree-ten global lower Taylor
polynomial for `cos(2t)` gives `s(t)<=P(t)`. Also `s` decreases on
`[0,pi]`, and for `z>=pi`,
` s(z)<=1/pi^2<1/9<=s(2)<=s(t)`;
the last bound uses `sin 2>=2-2^3/6=2/3` and `pi>3`.
This justifies (9) even when `x+y` crosses `pi`.

On a box `[i/100,(i+1)/100] x [j/100,(j+1)/100]`, use `C` at the
upper-right corner and the three `U` values at the lower endpoints.
The following complete standard-library Python certificate uses exact
rational arithmetic only. It covers all 18,145 boxes with
`10<=i<=j<=199`; symmetry covers the other half of the square.

```python
from fractions import Fraction as R


def P(t):
    z = t*t
    return 1-z/3+2*z*z/45-z**3/315+2*z**4/14175


def U(t):
    return P(t) if t <= 2 else 1/(t*t)


def C(x, y):
    return (x*x+x*y+y*y)/(8*x*x*y*y*(x+y)**2)


count = 0
minimum = R(100)
for i in range(10, 200):
    for j in range(i, 200):
        lower = C(R(i+1, 100), R(j+1, 100)) - R(5, 12)*(
            U(R(i, 100))+U(R(j, 100))+U(R(i+j, 100))-R(3, 2))
        assert lower > R(3, 1000)
        minimum = min(minimum, lower)
        count += 1
assert count == 18145
assert minimum == R(809086132959856637, 248122901376000000000)
```

The minimum certificate value is at `i=j=85`, approximately
`0.0032608281`. The stronger finite-box bound `3/1000`, together with
the explicit exterior estimates, proves (8). This is a covering
certificate, not a sample of the function or a floating-point optimizer.

## Every low-energy triple enters that limiting problem

Let `W={0,u,u+v}`, `u,v>0`, be any simple real triple. Its exact energy is
\[
Q_{\eta,a}(W)=1+\frac23\{F(u)+F(v)+F(u+v)\}
-\lambda\eta^4\left[1+\frac23\{
\operatorname{sinc}^2(\eta u)+\operatorname{sinc}^2(\eta v)
+\operatorname{sinc}^2(\eta(u+v))\}\right].
\tag{10}
\]
We claim, uniformly over all simple triples,
\[
\boxed{
\liminf_{\eta\downarrow0}\inf_{u,v>0}
\frac{Q_{\eta,\lambda\eta^3}(\{0,u,u+v\})-(1-2\lambda\eta^4)}
{\eta^4}\ge\frac1{1500}.
}
\tag{11}
\]
It is enough to analyze a sequence on which the displayed quotient is
bounded above. Equation (10), `0<=sinc^2<=1`, and real pair positivity
then imply `F(u)+F(v)+F(u+v)=O(eta^4)`.

If `max(eta u,eta v)` is unbounded, pass to a subsequence where it
tends to infinity. At least two notch terms in (10) tend to zero, so
its quotient above `1-2 lambda eta^4` has lower limit at least
`lambda/3=5/36`. This also covers a fixed close pair plus an escaping
third point, with no phase constraint imposed on that close pair.

Otherwise pass to `eta u->p`, `eta v->q`, with finite nonnegative
limits. The coarse triple gap from ANF-114,
\[
F(u)+F(v)+F(u+v)\ge[16(1+d(u+v)^2)^2]^{-1},
\tag{12}
\]
forces `p+q>0`. Neither limit can be zero. Indeed, suppose `p=0` and
`q>0`. From (1), for large `z`,
\[
zK(z)=(b/d)\sin(\pi z)+O(z^{-1}).
\tag{13}
\]
Applying this to `v` and `u+v` gives both sines `O(eta)`, hence
`sin(pi u)=O(eta)`. Therefore `|cos(pi u)|->1` and
`bu sin(pi u)->0`. But
`cos(pi u)-bu sin(pi u)=(1-du^2)K(u)=o(1)`, since
`K(u)=O(eta^2)` and `eta u->0`. This is a contradiction. The same
argument applies with `u,v` interchanged, including bounded gaps.

Thus `p,q>0`. By (13) all three phases approach integers to order
`eta`. Let `n,m` be the nearest integers to `u,v`, and pass to
bounded offset limits `(u-n)/eta->alpha`, `(v-m)/eta->beta`.
Put `A=b pi/d`, `B=1/d`. The parity-adjusted kernel limits are
\[
R_1=A\alpha/p-B/p^2,\quad
R_2=A\beta/q-B/q^2,\quad
R_3=A(\alpha+\beta)/(p+q)-B/(p+q)^2.
\tag{14}
\]
The long-edge phase adds, so
\[
-pR_1-qR_2+(p+q)R_3=B(1/p+1/q-1/(p+q)).
\]
Cauchy--Schwarz, or distance to this affine plane, yields the ANF-210
phase minimum in a normalization not requiring `p+q<=1`:
\[
\lim\frac{F(u)+F(v)+F(u+v)}{\eta^4}
\ge\frac{B^2(p^2+pq+q^2)}{2p^2q^2(p+q)^2}
=C(\pi p,\pi q).
\tag{15}
\]
The limit can be arranged by the same subsequence; a lower limit
suffices. Substitution into (10) and then (8) proves (11). This
argument exhausts every low-energy sequence rather than assuming
comparable gaps or integer-like phases at the outset.

In particular, for all sufficiently small widths every simple triple
has energy at least `1-2 lambda eta^4+eta^4/3000`.
A simple pair at any fixed positive zero `r_0` of `K` has
\[
Q_{\eta,a}(\{0,r_0\})
=1-\lambda\eta^4[1+\operatorname{sinc}^2(\eta r_0)]
=1-2\lambda\eta^4+O(\eta^6).
\tag{16}
\]
Such zeros exist by the numerator sign changes between sufficiently
large consecutive integers. The pair minimum is attained: its
separation-dependent term `F(r)-a eta sinc^2(eta r)` is continuous,
negative at a fixed root for small width, positive at zero, and tends
to zero at infinity.

The remaining multiplicity patterns with `N<=3` cannot improve this
pair. A singleton or a double point has energy `1-lambda eta^4`; a
triple point has `3(1-lambda eta^4)/2`. For multiplicities `(2,1)`,
`D=sum m_i^2=L=5`, `N^2=9`, so positivity of `F` and
`E_tau<=eta N^2` give `Q>=1-(9/5)lambda eta^4`. Every simple pair
has `Q>=1-2 lambda eta^4`. This proves (6), exact pair attainment
within the capped class, and the right side of (5).

## The four phases share the incompatibility differently

For the four sites in (7), set `k=j-i`. Taylor expansion of (1),
retaining integer parity, gives
\[
K(x_j-x_i)=\frac{(-1)^{kn}}{d n^2}
\left\{\frac{t_j-t_i}{k}-\frac1{k^2}\right\}+O(n^{-4}).
\tag{17}
\]
There are six edges; the constant in the remainder is harmless because
this number stays fixed. The six residuals, in edge order
`01,02,03,12,13,23`, are exactly
\[
(-1/3,\ 1/3,\ 1/2,\ -1/2,\ 1/3,\ -1/3),
\qquad \sum R_{ij}^2=17/18.
\tag{18}
\]
They also solve the four-site least-squares phase equations
`sum_(j!=i) [(t_i-t_j)/(i-j)^2-1/(i-j)^3]=0`; minimality within
that phase family is not needed for the witness. The shared edge
phases are not three independent copies of the sharp triple phases.

Since `eta n->3/10` and `L(W_eta)=4`, (17)--(18) imply
\[
Q_{\eta,a}(W_\eta)=1+\eta^4\{C_4-\lambda H_4\}+o(\eta^4),
\]
\[
C_4=\frac{10625}{729\pi^4},\qquad
H_4=1+\frac32\operatorname{sinc}^2(3/10)
+\operatorname{sinc}^2(3/5)+\frac12\operatorname{sinc}^2(9/10)
=1+\frac{5325+1525\sqrt5}{648\pi^2}.
\tag{19}
\]
The factors `3/2,1,1/2` count the ordered interactions divided by four.
The exact angle values in the last expression give
\[
C_4-\frac5{12}(H_4-2)<-\frac1{400}.
\tag{20}
\]
For a reproducible rational check of its sign, use the classical bounds
`333/106<pi<355/113` and `559/250<sqrt(5)`:

```python
from fractions import Fraction as R

lo_pi, hi_pi, lo_root = R(333, 106), R(355, 113), R(559, 250)
assert lo_root**2 < 5
upper = R(10625, 729)/lo_pi**4 - R(5, 12)*(
    (5325+1525*lo_root)/(648*hi_pi**2)-1)
assert upper < -R(1, 400)
```

The actual coefficient in (20) is approximately `-0.00279405`.
The strict margin and the `o(eta^4)` remainder prove the left side
of (5), with `1/500` in place of `1/400`, for every sufficiently small
width. The floor in (7) does not restrict widths to a subsequence.

## Prior art, audit boundary and consequence

The Montgomery--Taylor kernel is classical; see
[Carneiro--Chandee--Littmann--Milinovich, Corollary 14](https://arxiv.org/pdf/1406.5462).
[Wang, Lemma 3.2](https://arxiv.org/html/2609.24167v1#S3) supplies
prior art for the fourth-power triple gap and numerator-addition
argument. ANF-210 supplies the sharp limiting phase plane; it gives a
sufficient triple witness, not the optimum among all configurations.
The present result uses that plane to **exclude every simple triple**
at a coefficient where four points already descend, rather than just
improving the sufficient triple coefficient.

[Knausgård, sections 7.1--7.2](https://arxiv.org/html/2610.08965v1#S7.SS1)
studies constrained-density pair energy and relaxed periodic trial
states. [Sütő](https://arxiv.org/abs/math-ph/0508004) treats
compact-Fourier pair potentials and infinite-volume ground states.
These are close frameworks for energy optimization, but neither is
used as a theorem about this shrinking triangular notch, free span or
cardinality separation. Searches by the kernel, notch, three/four-point
energy and ground-state mechanism did not identify (5); this is not
an exhaustive novelty claim. Taylor enclosures, least-squares phase
balancing and rational interval certificates are standard methods.

Both embedded exact certificates were executed successfully. The
covering argument (8)--(9) and the sequential analysis (10)--(16) are
load-bearing: a numerical search over equal-gap triples would not prove
the claimed exclusion. Independent double-precision checks of (7),
with parity-reduced trigonometric evaluation, confirmed the scaled
coefficient in (20); those diagnostics are not evidence for the
universal bound. No Lean verification is asserted.

The separation is real and uses total cardinality. It does not exclude
all multisets on three distinct sites with arbitrary multiplicities,
nor configurations with nonzero imaginary parts. It does not prove that
four points attain the unrestricted floor, that the first transition
occurs at `5/12`, or that there is a unique transition. ANF-209's initial
window remains cubic, with its exact coefficient undetermined. What is
ruled out is determining that loss by testing only cardinalities at most
three: at the explicit coefficient (4), their exact optimum is still a
pair while a valid four-point source beats it. No zero-density,
zero-proportion or RH consequence is established.
