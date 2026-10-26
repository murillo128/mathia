# ANF-208 — Real notch energy has a uniform two-scale law

**Status:** EXACT-DERIVED + ALL-REAL-MULTISETS + WIDTH-UNIFORM-ENERGY-BOUND + SHARP-ORDER. For small removed height `a`, the unrestricted finite-real-multiset energy deficit of a triangular notch has order `a eta + a^(4/3)`, with constants independent of its width `eta`. In particular, at `a=lambda eta`, the real infimum has deficit `Theta_lambda(eta^(4/3))`. This supplies the missing real lower bound for ANF-207's lattice witness. Arbitrary real multiplicities, cardinalities and spans are included; the analogous lower bound for complex configurations is not proved.

## Object and precise uniform statement

Use `f_hat(x)=int f(u) exp(-2 pi i u x) du` and
\[
g(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin(1/\sqrt2)}
\mathbf1_{[-1/2,1/2]}(u),\qquad J_0=g*g,\qquad F=\widehat J_0=K^2,
\]
\[
K(x)=\frac{\cos(\pi x)-\sqrt2\pi\cot(1/\sqrt2)x\sin(\pi x)}
{1-2\pi^2x^2},\qquad K(0)=1,
\tag{1}
\]
with the removable values continued. For `0<eta<=1/2`, put
\[
\tau_\eta(u)=(1-|u|/\eta)_+,\qquad
J_{\eta,a}=J_0-a\tau_\eta,\qquad
\Psi_\eta(x)=\widehat{\tau_\eta}(x)
=\eta\operatorname{sinc}^2(\eta x).
\tag{2}
\]
Here `sinc(x)=sin(pi x)/(pi x)` continuously at zero, and `a` is
the **removed spectral height**, not a relative notch amplitude.

Write a nonempty finite real multiset as distinct sites `x_i` with
positive integer multiplicities `m_i`. Set
\[
L=\sum_i\ell(m_i),\qquad
\ell(1)=1,\quad\ell(m)=2m\ (m\ge2),\qquad
S_W(u)=\sum_i m_i e^{-2\pi iux_i},
\]
and write `E_f(W)=int f|S_W|^2`, with `E_0=E_(J_0)`. Define
\[
Q_{\eta,a}(W)=\frac{\int J_{\eta,a}|S_W|^2}{L},\qquad
q^{\mathbb R}_{\eta,a}=\inf_{W\subset\mathbb R} Q_{\eta,a}(W).
\tag{3}
\]
Thus `L=2|W|-sigma(W)` with `sigma` counting simple real sites.
The infimum has no prescribed density, separation or diameter.

There are absolute constants `a_*>0`, `c>0` and `C<infinity` such that
\[
\boxed{
c(a\eta+a^{4/3})\le1-q^{\mathbb R}_{\eta,a}
\le C(a\eta+a^{4/3})
\quad(0<a\le a_*,\ 0<\eta\le1/2).
}
\tag{4}
\]
One nonoptimal explicit choice is
\[
A=16(1+2\pi^2)^2,\quad \delta=(30A)^{-1/3},\quad
a_* =\delta^4,\quad
c=\frac{2}{5\pi^2},\quad C=9+6/\delta.
\tag{5}
\]
These parameters give `a_*<1/20`. As in ANF-207,
`g>=3/4` on its support, so
`J_0(u)>=(9/16)(1-|u|)` and `(1/10)tau_eta<=J_0`.
Consequently the entire stated family remains dominated and positive:
`J_(eta,a)>=(1-10a)J_0`.

## A weighted triple gap controls squared cell occupancies

Real pair positivity gives the exact nonnegative excess
\[
\Delta:=E_0(W)-L
=\sum_{m_i\ge3}m_i(m_i-2)
 +2\sum_{i<j}m_im_jF(x_i-x_j)\ge0.
\tag{6}
\]
ANF-114 supplies, for every ordered triple of real sites spanning
at most `R`,
\[
F(x_i-x_j)+F(x_i-x_k)+F(x_j-x_k)\ge\kappa_R,
\qquad \kappa_R:=\frac1{16(1+2\pi^2R^2)^2}.
\tag{7}
\]
This is a quantitative property of (1), not a general consequence of
positive definiteness. Its proof uses the addition law for the numerator
of `K`, before dividing by the denominator, so removable points are
included.

Partition the real line into half-open cells `I_j=[jR,(j+1)R)`.
Let `n_j` be the total multiplicity in `I_j`, `D_j=sum_(x_i in I_j)m_i^2`,
`L_j=sum_(x_i in I_j)ell(m_i)`, and
\[
O_j=2\sum_{\substack{i<k\\x_i,x_k\in I_j}}
m_im_kF(x_i-x_k),\qquad
\Delta_j=D_j-L_j+O_j\ge0.
\tag{8}
\]
The cell estimate is
\[
\boxed{n_j^2\le3L_j+\frac3{\kappa_R}\Delta_j.}
\tag{9}
\]
To prove it, suppress the cell index and sum (7) over distinct
support triples, with weight `m_i m_k m_l`. The weighted sum of the
three interactions equals
\[
\sum_{i<k}m_im_k(n-m_i-m_k)F(x_i-x_k)
\le\frac n2 O.
\]
The weighted number of triples is
\[
\sum_{i<k<l}m_im_km_l
=\frac{n^3-3nD+2\sum_i m_i^3}{6}.
\]
Thus `kappa_R(n^3-3nD)<=3nO`, and division by `n>0`
gives `n^2<=3D+3O/kappa_R`. Since `D-L>=0` and
`kappa_R<=1`, (9) follows. Empty cells give zero on both sides.
Cells containing one or two distinct sites are also covered: the
triple sum is zero, and the displayed cubic identity still proves
the same inequality. Multiplicity has never been replaced by a count
of distinct support points.

All omitted cross-cell terms in (6) are nonnegative. Summing (9)
therefore yields
\[
\boxed{\sum_j n_j^2\le3L+\frac3{\kappa_R}\Delta.}
\tag{10}
\]
The coefficient of `L` stays bounded as `R` grows; only the
**excess** pays the fourth-power scale cost. A bound on total source
energy with a scale-dependent coefficient multiplying `L` would
not suffice for (4).

## Sum the actual notch interaction at that cell scale

For points in cells whose indices differ by `h`, (2) has the
nonnegative majorant
\[
b_h=\begin{cases}
\eta,&|h|\le1,\\
\min\{\eta,[\pi^2\eta R^2(|h|-1)^2]^{-1}\},&|h|\ge2.
\end{cases}
\tag{11}
\]
Indeed `sinc^2(v)<=min(1,1/(pi^2 v^2))`, and nonadjacent cells
have distance at least `(|h|-1)R`. For the decreasing function
`f(s)=min(eta,1/(pi^2 eta R^2 s^2))`,
\[
\sum_{n\ge1}f(n)\le\int_0^\infty f(s)\,ds=\frac2{\pi R}.
\]
Hence
\[
\sum_{h\in\mathbb Z}b_h\le3\eta+\frac4{\pi R}
\le3\eta+\frac2R.
\tag{12}
\]
The cell masses have finite support. Cauchy--Schwarz gives
`sum_j n_j n_(j-h)<=sum_j n_j^2` for each `h`, so
\[
E_{\tau_\eta}(W)
\le\sum_h b_h\sum_j n_jn_{j-h}
\le(3\eta+2/R)\sum_j n_j^2.
\tag{13}
\]
Combining with (10), and putting `e=Delta/L`, gives the uniform bound
\[
\boxed{
\frac{E_{\tau_\eta}(W)}L
\le(3\eta+2/R)\left(3+\frac{3e}{\kappa_R}\right)
\qquad(R>0).
}
\tag{14}
\]
No inverse-square tail constant depending on `eta` has been hidden:
the crossover in the minimum in (11) is summed explicitly. There
is also no deletion error or assumption on the number of occupied
cells.

For example, `R=e^(-1/4)` for `0<e<=1`, with
`kappa_R^(-1)<=A R^4` for `R>=1`, gives the coarse but
width-uniform exposure modulus
\[
\frac{E_{\tau_\eta}(W)}L
\le9(1+A)(\eta+e^{1/4}).
\tag{15}
\]
For `e=0`, let `R` tend to infinity in (14). This is not a
replacement for ANF-195's sharper fixed-profile square-root modulus
or its exact equality envelope. It retains uniformity as the profile
width changes, which those profile-dependent constants do not supply.

## Absorb the excess and obtain the lower energy bound

For `R>=1`, (14) implies
\[
Q_{\eta,a}(W)
\ge1-3a(3\eta+2/R)
 +\{1-3Aa(3\eta+2/R)R^4\}e.
\tag{16}
\]
Choose the scale before examining `W`:
\[
R=\delta\min\{a^{-1/3},(a\eta)^{-1/4}\}.
\tag{17}
\]
If `a<=delta^4` and `eta<=1/2`, both candidates in (17),
after multiplication by `delta`, are at least one. Furthermore,
\[
3Aa(3\eta+2/R)R^4
\le9A\delta^4+6A\delta^3
\le15A\delta^3=\tfrac12.
\tag{18}
\]
The remaining excess in (16) is nonnegative and can be dropped.
Since
\[
\frac aR=\delta^{-1}
\max\{a^{4/3},a^{5/4}\eta^{1/4}\},\qquad
a^{5/4}\eta^{1/4}=(a^{4/3})^{3/4}(a\eta)^{1/4}
\le\max\{a^{4/3},a\eta\},
\]
we obtain, for every real multiset,
\[
Q_{\eta,a}(W)\ge1-9a\eta-6a/R
\ge1-(9+6/\delta)(a\eta+a^{4/3}).
\tag{19}
\]
Taking the infimum proves the right side of (4), without assuming
an attaining configuration.

## Finite witnesses give the reverse order in both regimes

A real singleton has `Q=1-a eta`, so always
`1-q^R>=a eta`. When `eta<=a^(1/3)/4`, use the ANF-207
integer lattice segment
\[
\ell=\lceil a^{-1/3}\rceil,\qquad
M=\left\lfloor\frac1{2\eta\ell}\right\rfloor+1,\qquad
X=\{0,\ell,\ldots,(M-1)\ell\}.
\tag{20}
\]
That finite witness gives
\[
Q_{\eta,a}(X)\le1-c_0a^{4/3},\qquad c_0=\frac1{2\pi^2}.
\tag{21}
\]
For clarity, the two estimates behind it are
\[
E_0(X)/M-1\le
\frac8{3(2\pi^2-1)^2}\ell^{-4}
\le C_*a^{4/3},\quad C_*<\frac1{2\pi^2},
\]
\[
aE_{\tau_\eta}(X)/M\ge\frac{4a\eta M}{\pi^2}
\ge\frac{2a}{\pi^2\ell}\ge\frac{a^{4/3}}{\pi^2}.
\tag{22}
\]
The first uses the exact integer values
`F(k ell)=(1-2 pi^2 k^2 ell^2)^(-2)` and the finite pair sum.
The second uses `eta diam(X)<=1/2`, hence
`sinc^2(eta(x-y))>=4/pi^2`, and `ell<=2a^(-1/3)`.
All cardinalities are finite.

In this narrow regime `a eta<=a^(4/3)/4`, so (21) yields
`1-q^R>=(4c_0/5)(a eta+a^(4/3))`. In the complementary regime,
`a^(4/3)<4a eta`, and the singleton yields at least one fifth
of the same sum. Taking `c=4c_0/5` proves the left side of (4).

For any fixed `lambda>0`, setting `a=lambda eta` consequently gives
\[
\boxed{1-q^{\mathbb R}_{\eta,\lambda\eta}
\asymp_\lambda\eta^{4/3}\quad(\eta\downarrow0).}
\tag{23}
\]
This applies below, at and above the ANF-205--ANF-206 distant-copy
threshold `lambda=(1/2)cot^2(1/sqrt(2))`. The order of the real
infimum's deficit does not decide whether that infimum is attained.
The crossover `a~eta^3` in (4) separates the two energy scales;
it does not prove a matching lower bound on ANF-200's exact two-site
attainment interval.

## Prior art, checks and remaining boundary

ANF-114 already proves the fourth-power triple gap; ANF-207 already
constructs (20)--(22) and gives a complex cardinality lower bound
for that benchmark. The new step is the weighted cell estimate
(9)--(10) and its combination with the width-explicit notch row sum.
Together they rule out a larger-order energy drop from **any real
configuration**, which neither earlier result establishes.

Cell occupation-square estimates are classical in
[Ruelle, *Superstable Interactions in Classical Statistical Mechanics*,
section 1, condition (SS)](https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B28%5D.pdf).
The present estimate is derived directly for the excess above the
affine multiplicity baseline and tracks its coefficient as the cell
size grows. No Gibbs-state or thermodynamic theorem is imported.
[Sütő's compact-Fourier ground states](https://arxiv.org/pdf/math-ph/0508004)
and [Procacci's stability constant](https://arxiv.org/pdf/2005.10362)
are neighboring frameworks, not the changing-width estimate (4).
The source kernel itself is the classical
[Carneiro--Chandee--Littmann--Milinovich extremizer](https://arxiv.org/abs/1406.5462).

A targeted contemporary comparison is
[Knausgård, arXiv:2610.08965v1, sections 7.1--7.2](https://arxiv.org/html/2610.08965v1#S7.SS1):
it studies labelled real pair-energy configurations under an asymptotic
span constraint and periodic trial states. That objective is distinct
from (3)'s free finite-multiset infimum and its simultaneous notch
height/width limit. Its claimed zero-counting constants and numerical
certificates are not used or independently validated here. Searches
by Montgomery--Taylor stability, ground states and weak attractive
pair-potential perturbations did not identify (4); this is a derived
specialization of classical methods, not an exhaustive novelty claim.

As noncertifying arithmetic checks, 400 generated real configurations
(seed 208, one through 34 distinct sites, multiplicities one through
14, random and integer-lattice geometry) satisfied (10), (13) and
(14) in ordinary double precision. Three instances of (20) with
`eta=a` and `a=a_*,a_*/8,a_*/64` had respectively 26,412,
105,875 and 423,960 sites; direct finite lag sums gave
`(1-Q)/a^(4/3)` approximately `0.4327,0.4336,0.4341`,
consistent with both sides of (4). These samples are falsification
checks only. The proof is (6)--(22); no Lean validation or numerical
optimality is claimed.

The decisive restrictions are real support, positive integer
multiplicities, the exact `L` baseline, and the source-specific
triple gap. Nonreal sources lose the nonnegative pair decomposition
that justifies summing local excesses in (10). Thus (23) does not
upper-bound the deficit of the unrestricted complex infimum.
Nor does it identify an optimal constant, select a crystal, or
establish finite attainment. The fixed-profile complex exposure
envelope of ANF-099 remains open. No improved zero proportion,
zero-density estimate or RH conclusion follows.
