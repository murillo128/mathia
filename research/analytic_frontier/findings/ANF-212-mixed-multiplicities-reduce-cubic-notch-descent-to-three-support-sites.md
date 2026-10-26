# ANF-212 — Mixed multiplicities reduce cubic notch descent to three support sites

**Status:** EXACT-DERIVED + EXACT-RATIONAL-CERTIFICATE + REAL-SUPPORT-SEPARATION.
At `a=(5/12) eta^3` and every sufficiently small width, the smallest
number of distinct real sites that can beat the entire two-site class
is three when integer multiplicities are allowed, but four when every
site must be simple. An explicit three-site witness has multiplicities
`(1,2,2)` and total cardinality five. This resolves the support-versus-
cardinality boundary left by ANF-211; it neither finds the unrestricted
minimizer nor improves that finding's four-point energy witness.

## Object and exact support distinction

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
Continue removable values. Write
\[
\tau_\eta(u)=(1-|u|/\eta)_+,\quad
J_{\eta,a}=J_0-a\tau_\eta,\quad
\widehat{\tau_\eta}(x)=\eta\operatorname{sinc}^2(\eta x),
\tag{2}
\]
where `sinc(t)=sin(pi t)/(pi t)`, continuously at zero. For a nonempty
finite real multiset with distinct sites `x_i` and positive integer
multiplicities `m_i`, set
\[
N(W)=\sum_i m_i,\quad L(W)=\sum_i\ell(m_i),\qquad
\ell(1)=1,\quad\ell(m)=2m\quad(m\ge2),
\]
\[
Q_{\eta,a}(W)=\frac{\int J_{\eta,a}(u)
|\sum_i m_i e^{-2\pi iux_i}|^2du}{L(W)},\qquad
q_{2,\mathrm{supp}}=\inf_{|\operatorname{supp}W|\le2}Q_{\eta,a}(W).
\tag{3}
\]
The support cap in (3) allows arbitrary finite multiplicities. Fix
`lambda=5/12` and `a=lambda eta^3`. The small-width regime is inside
`eta<=1/4`, `a<=1/20`, where ANF-209 verifies `J_(eta,a)>=J_0/2`.

Put
\[
n=\left\lfloor\frac1{10\pi\eta}\right\rfloor,\qquad
x_0=0,\quad x_1=10n+\frac1{18b\pi n},\quad
x_2=17n+\frac3{16b\pi n},
\]
\[
W_\eta=\{x_0,x_1,x_1,x_2,x_2\}.
\tag{4}
\]
For all sufficiently small `eta>0`, these are three distinct sites and
\[
\boxed{
Q_{\eta,\lambda\eta^3}(W_\eta)
<1-2\lambda\eta^4-\frac{\eta^4}{8000}
<1-2\lambda\eta^4\le q_{2,\mathrm{supp}}.
}
\tag{5}
\]
At the same parameters, ANF-211 proves that every simple configuration
of at most three points has energy at least `q_(2,supp)`, and exhibits
a simple four-point configuration strictly below it. Thus
\[
\boxed{
\min_{Q(W)<q_{2,\mathrm{supp}}}|\operatorname{supp}W|=3,
\qquad
\min_{\substack{Q(W)<q_{2,\mathrm{supp}}\\W\ \mathrm{simple}}}|W|=4.
}
\tag{6}
\]
The equality of the pair minimum with (3) is justified below; it is
not an identification of support cardinality with total multiplicity.

## Weighted phases and the explicit source cost

For fixed positive integer `k` and fixed real `t`, expansion of (1)
at an integer gives
\[
K\left(kn+\frac{t}{b\pi n}\right)
=\frac{(-1)^{kn}}{dn^2}
\left(\frac{t}{k}-\frac1{k^2}\right)+O(n^{-4}).
\tag{7}
\]
The numerator has leading term `(-1)^(kn)(1-kt)` and the denominator
has leading term `-d k^2 n^2`. The fixed number of edges makes the
remainder uniform for this witness.

For the consecutive gaps and their sum in (4), the pairs `(k,t)` are
\[
(10,1/18),\quad (7,19/144),\quad (17,3/16).
\]
Their residuals in (7) are exactly
\[
(R_1,R_2,R_3)=\left(-\frac1{225},-\frac{11}{7056},
\frac{35}{4624}\right).
\tag{8}
\]
The corresponding occupation products are `(2,4,2)`, while
`D=sum m_i^2=L=9`. The normalized diagonal therefore stays exactly
`1-a eta`; it does not pay a fixed excess for the two double sites.
Since `eta n->1/(10 pi)`, (7)--(8) give
\[
\frac{2}{9\eta^4}\{2F(x_1)+4F(x_2-x_1)+2F(x_2)\}
\longrightarrow C,
\]
\[
C=\frac{5000}{9}(2R_1^2+4R_2^2+2R_3^2)
=\frac{70956250217}{779675884848}.
\tag{9}
\]
Writing `s(z)=(sin z/z)^2`, the normalized notch exposure divided
by `eta` tends to
\[
H=1+\frac29\{2s(1)+4s(7/10)+2s(17/10)\}.
\tag{10}
\]
Consequently
\[
Q_{\eta,\lambda\eta^3}(W_\eta)
=1+\eta^4(C-\lambda H)+o(\eta^4).
\tag{11}
\]
The scale `1/(10 pi eta)` makes the arguments in (10) rational
radians. There is no missing factor of `pi` in `s`.

The unequal phases matter. More generally, if two scaled gaps have
limits `eta u->p>0`, `eta v->q>0`, and their offsets from integers
are of order `eta`, define `R_u=lim (-1)^(nearest integer to u)
K(u)/eta^2`, and similarly on the other edges, along a subsequence
where the offset limits exist. These leading values obey
\[
-pR_u-qR_v+(p+q)R_{u+v}
=\frac1d\left(\frac1p+\frac1q-\frac1{p+q}\right).
\tag{12}
\]
For positive edge weights `w_1,w_2,w_3`, weighted Cauchy--Schwarz
therefore gives the exact phase minimum
\[
\min\sum_{j=1}^3w_j R_j^2
=\frac{d^{-2}(1/p+1/q-1/(p+q))^2}
{p^2/w_1+q^2/w_2+(p+q)^2/w_3}.
\tag{13}
\]
Equality is realizable: the two free phase offsets parameterize the
whole affine plane (12). The weights change both the energy metric
in (13) and the notch exposure, so the unweighted triple minimum
cannot be reused. Formula (4) is a convenient rational phase choice,
not an asserted phase or geometry optimum. The proof of (5) needs
only its direct residuals (8), not minimization in (13).

## Exact sign certificate

For `0<=z<=17/10`, set
\[
P(z)=\sum_{j=0}^{5}\frac{(-1)^jz^{2j}}{(2j+1)!}.
\tag{14}
\]
The alternating terms decrease, so
`0<1-z^2/6<=P(z)<=sin(z)/z` on this interval, with continuous
values at zero. Squaring preserves the lower bound. Thus the
following complete rational calculation proves
\[
\boxed{C-\frac5{12}(H-2)<-\frac1{6400}.}
\tag{15}
\]

```python
from fractions import Fraction as R
from math import factorial

edges = [(10, R(1, 18)), (7, R(19, 144)), (17, R(3, 16))]
weights = [2, 4, 2]
residual = [t/k-R(1, k*k) for k, t in edges]
assert residual == [-R(1, 225), -R(11, 7056), R(35, 4624)]
C = R(5000, 9)*sum(w*r*r for w, r in zip(weights, residual))
assert C == R(70956250217, 779675884848)

def P(z):
    return sum((-1)**j*z**(2*j)/factorial(2*j+1) for j in range(6))

angles = [R(1), R(7, 10), R(17, 10)]
assert all(P(z) > 0 for z in angles)
H_lower = 1+R(2, 9)*sum(w*P(z)**2 for w, z in zip(weights, angles))
assert C-R(5, 12)*(H_lower-2) < -R(1, 6400)
```

Together, the strict margin (15) and (11) prove the first inequality
in (5), with `1/8000` leaving room for the vanishing remainder.
The floor defining `n` permits every sufficiently small width, not
only a selected sequence. No effective width cutoff is claimed.

## The comparison covers arbitrary multiplicities on two sites

Let `Z` have at most two distinct real sites. Put `D=sum m_i^2`
and `N=sum m_i`. Pointwise real positivity `F>=0` gives `E_0>=D`,
and `E_tau<=eta N^2<=2 eta D`. Also `D>=L`. Hence, for `2a eta<1`,
\[
Q_{\eta,a}(Z)\ge (1-2a\eta)D/L\ge1-2a\eta.
\tag{16}
\]
This directly proves the last inequality in (5), without a maximum
multiplicity assumption.

For completeness, the infimum in (3) is the simple-pair minimum.
Let `A=1-a eta` and `V(r)=F(r)-a eta sinc^2(eta r)`. For small
width, `v=min_(r>0)V(r)<0`: a fixed positive zero of `K` supplies a
negative value, while `V` is positive at zero and tends to zero at
infinity. Thus the minimum exists. For any two multiplicities `m,k`,
`2mk<=m^2+k^2=D`, so, because `v<0`,
\[
AD+2mk V(r)\ge AD+2mk v\ge(A+v)D\ge(A+v)L.
\tag{17}
\]
The last step uses `A+v>=1-2a eta>0`. A simple pair and a pair of
double sites attain `A+v`. Single-site multisets also obey this lower
bound. ANF-211's simple-triple exclusion and simple four-point
witness can therefore be compared to precisely the same (3), proving
(6). The witness (4) has five points with multiplicity, so it does
not contradict ANF-211's total-cardinality-three exclusion.

## Prior art, validation and consequence

[Wang, Lemma 3.2](https://arxiv.org/html/2609.24167v1#S3)
uses the same Montgomery--Taylor numerator and additive triple
constraint to obtain a fourth-power gap. ANF-210 derives the sharp
unweighted phase minimum; (12)--(13) are its elementary weighted
least-squares version, not a new optimization principle.
[Knausgård, sections 7.1--7.2](https://arxiv.org/html/2610.08965v1#S7.SS1)
explicitly uses labelled simple/double configurations and relaxed
mixed-occupation periodic trial states. Thus neither introducing
integer weights nor their possible energetic advantage is claimed
as new. That constrained-density problem does not supply the
free-span shrinking-notch separation (5)--(6). Targeted searches by
the kernel, weighted triple energy and mixed-occupation notch did
not identify this exact comparison; no exhaustive novelty claim is
made.

The embedded rational certificate and both ANF-211 certificates
were executed successfully. The latter support the imported universal
simple-triple exclusion and four-point witness; a sampled triple
search would not establish (6). Direct parity-reduced floating-point
evaluation of (4) at shrinking widths agrees with (11), but only
the exact expansion and rational inequality prove eventual descent.
In particular the same witness has not yet descended at `eta=10^-3`;
the asymptotic qualifier is essential. No Lean verification is asserted.

The mathematical change is an exact distinction between total
cardinality and distinct support in this cubic regime. Four distinct
sites are necessary for a **simple** descending configuration; only
three are necessary when a simple site and two double sites may share
the phase constraint. Uniformly doubling a simple triple gives the
same normalized energy and cannot produce this effect.

This does not show that five is the smallest total multiplicity for
a three-site descending configuration, that (4) minimizes even the
three-site class, or that it beats ANF-211's simple four-point witness.
It does not locate the first transition coefficient, prove finite
attainment of the unrestricted infimum, or address nonreal
configurations. No new zero-density bound, zero proportion or RH
consequence follows.
