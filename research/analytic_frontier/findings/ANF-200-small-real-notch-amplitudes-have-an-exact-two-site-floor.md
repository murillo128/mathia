# ANF-200 — Small real notch amplitudes have an exact two-site floor

**Status:** EXACT-DERIVED + REAL-MULTISET + LOCAL-AMPLITUDE-REDUCTION + SHARP-QUADRATIC-RESPONSE. For each fixed dominated positive-Fourier profile with an inverse-square Fourier tail and positive exposure on the source zero set, the entire finite-real-multiset infimum is attained by two sites throughout a positive amplitude interval. This strengthens ANF-199's stationary-contact criterion: the nonstationary case also reduces exactly to a one-variable minimum, rather than merely having a two-site upper bound. The interval depends on the profile. No complex-configuration or zeta-zero consequence is established.

## Exact reduction and its quadratic consequence

Use the Fourier convention \(\widehat f(x)=\int f(u)e^{-2\pi iux}\,du\) and
\[
g(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin(1/\sqrt2)}
\mathbf1_{[-1/2,1/2]}(u),\qquad J_0=g*g,\qquad F=\widehat J_0=K^2,
\]
\[
K(x)=\frac{\cos(\pi x)-a x\sin(\pi x)}{1-2\pi^2x^2},
\qquad a=\sqrt2\pi\cot(1/\sqrt2),\qquad K(0)=1.
\tag{1}
\]
The removable points are continued. The positive source zeros are simple,
nonintegral numbers \(r_j\in(j,j+1/2)\). ANF-087 proves that no three
distinct real sites have all their differences in the zero set of \(K\).

Freeze a real even integrable profile with
\[
0\le\phi\le J_0,\qquad \Phi:=\widehat\phi\ge0,\qquad
\Phi(x)\le\frac{D_\phi}{1+x^2},\qquad
M:=\max_{j\ge1}\Phi(r_j)>0.
\tag{2}
\]
The maximum exists by decay. Put
\[
\mathcal Z_*:=\{r_j:\Phi(r_j)=M\},\qquad
\beta:=\Phi(0)+M,\qquad
\kappa:=\max_{r\in\mathcal Z_*}
\frac{\Phi'(r)^2}{4K'(r)^2}.
\tag{3}
\]
The active set is finite and nonempty. Compact support of \(\phi\) makes
\(\Phi\) smooth, indeed entire; no physical-space differentiability is
being assumed in (2).

For a nonempty finite real multiset \(W\), let
\[
L(W)=2|W|-\sigma(W),\quad S_W(u)=\sum_{x\in W}e^{-2\pi iux},\quad
E_f(W)=\int f(u)|S_W(u)|^2\,du,
\]
where \(\sigma\) counts distinct sites of multiplicity one. Write
\[
e(W)=E_{J_0}(W)/L(W)-1,\quad h_\phi(W)=E_\phi(W)/L(W),
\quad q_\phi^{\mathbb R}(t)=\inf_W\{1+e(W)-t h_\phi(W)\}.
\tag{4}
\]
There is \(t_\phi>0\), with \(t_\phi<1\), such that
\[
\boxed{
q_\phi^{\mathbb R}(t)=1-t\Phi(0)
 +\min_{x>0}\{F(x)-t\Phi(x)\}
\qquad(0<t\le t_\phi).
}
\tag{5}
\]
The infimum on the left includes every finite cardinality, multiplicity
and diameter. A pair of distinct simple sites, separated by a minimizing
\(x\) on the right, attains it. The same is true when both sites have
multiplicity two. At \(t=0\) the corresponding equality holds with
minimum zero.

In particular,
\[
\boxed{
q_\phi^{\mathbb R}(t)=1-\beta t-\kappa t^2+O_\phi(t^3)
\qquad(t\downarrow0).
}
\tag{6}
\]
Thus growing real clusters cannot amplify the two-site quadratic loss.
When \(\kappa=0\), the floor is exactly \(1-\beta t\) for all
sufficiently small positive \(t\), as in ANF-199. When \(\kappa>0\),
(6) identifies the exact coefficient that ANF-199 bounded only from one
side.

## Retain the source energy outside the matched edges

The proof uses ANF-195's fixed matching construction but preserves an
energy distinction that its square-root bound, and ANF-199's linear
criterion, could discard.

Write the distinct sites as \(x_i\), with multiplicities \(m_i\), and
put \(\ell(1)=1\), \(\ell(m)=2m\) for \(m\ge2\). Then
\[
\Delta:=E_{J_0}(W)-L(W)
=\sum_{m_i\ge3}m_i(m_i-2)
 +2\sum_{i<j}m_im_jF(x_i-x_j)\ge0.
\tag{7}
\]
All terms are nonnegative. Whole-site subsets preserve the additivity of
\(L=\sum_i\ell(m_i)\).

First fix a large \(R>\max(1,r_1)\) with
\[
\frac{4D_\phi}{R^2}\sum_{n\ge1}n^{-2}\le M/2.
\tag{8}
\]
Around the finitely many positive source roots in \([0,R]\), there are
bounded neighborhoods \(\mathcal U_R\) and \(d_R>0\) such that
\[
F(y)+F(y-r)\ge\frac{d_R}{1+y^2}
\quad(y\in\mathbb R,\ r\in\mathcal U_R).
\tag{9}
\]
Here is the source dependence behind this ANF-195 estimate. At infinity,
\(K(y)=a\sin(\pi y)/(2\pi^2y)+O(y^{-2})\); the two leading squares
are bounded below using
\[
\sin^2\theta+\sin^2(\theta-\pi r)\ge1-|\cos(\pi r)|.
\]
This bound is uniformly positive near each of the finitely many
nonintegral roots. On compact \(y\)-sets, simultaneous vanishing at an
exact root would give a forbidden three-site zero packing. Continuity
and shrinking the finitely many neighborhoods prove (9). Consequently
\[
\Phi(y)+\Phi(y-r)\le C_R\{F(y)+F(y-r)\}
\quad(r\in\mathcal U_R,\ y\in\mathbb R)
\tag{10}
\]
for a profile-dependent finite \(C_R\).

Choose \(\gamma>0\) so small that every \(0<r\le R\) with
\(F(r)\le\gamma\) belongs to \(\mathcal U_R\), and
\[
\gamma<\min_{u,v\in[-R,R]}
\max\{F(u),F(v),F(u-v)\}.
\tag{11}
\]
The minimum is positive: vanishing at three distinct sites is excluded,
and coincident sites give \(F(0)=1\).

Delete the set \(B_0\) of sites with \(m_i\ge3\). Among the remaining
sites \(H\), simultaneously mark
\[
B_1=\{i\in H:D_i>\gamma\},\qquad
D_i=\sum_{j\in H,\ j\ne i}m_jF(x_i-x_j).
\]
Let \(B=B_0\cup B_1\), \(G=W\setminus B\). Each good multiplicity
is one or two. Each distinct good pair has source interaction at most
\(\gamma\). By (11), the distance-\(R\) graph on the good sites is a
matching. Denote its edge set by \(\mathcal E\), the union of paired
sites by \(P\), and its isolated sites by \(U\).

Separate the internal matched-edge energy from everything else:
\[
\Delta_P=2\sum_{\{i,j\}\in\mathcal E}m_im_jF(x_i-x_j),
\qquad \Delta_{\rm out}:=\Delta-\Delta_P\ge0.
\tag{12}
\]
The key refinement is
\[
L(B)\le(2+2/\gamma)\Delta_{\rm out},\qquad
E_\phi(B)\le E_{J_0}(B)\le L(B)+\Delta_{\rm out}.
\tag{13}
\]
For \(B_0\), use \(2m\le2m(m-2)\). For \(B_1\),
\[
\sum_{i\in B_1}m_i^2
\le\frac2\gamma\sum_{i\in B_1}m_iD_i
\le\frac2\gamma\Delta_{\rm out}.
\]
Every edge in the middle sum has an endpoint in \(B_1\), so it is not
an internal good matching edge. Counting marked endpoints charges each
unordered edge at most twice, exactly the ordered budget in (7). The
source surplus and off-diagonal interactions entirely within \(B\)
also belong to \(\Delta_{\rm out}\), proving the second part of (13).

## All other notch interactions use that remaining budget

The following bound holds with a finite \(C=C_\phi\ge0\), independent
of \(W\):
\[
\boxed{
E_\phi(W)\le\Phi(0)L(W)
 +2\sum_{\{i,j\}\in\mathcal E}m_im_j\Phi(x_i-x_j)
 +\frac M2 L(U)+C\Delta_{\rm out}.
}
\tag{14}
\]
To verify every term:

- The good diagonal is exactly \(\Phi(0)L(G)\), at most
  \(\Phi(0)L(W)\). The internal matched edges are retained exactly.
- The isolated sites are more than \(R\) apart. From each isolated site,
  the \(n\)-th neighbor in either direction has distance greater than
  \(nR\) and multiplicity at most two. Equation (8) bounds its weighted
  notch potential by \(M/2\). Summing over isolated sites and using
  \(\sum_U m_i\le L(U)\) proves the third term.
- For a good matched pair, (10) bounds its interaction with each outside
  good site by a fixed multiple of the corresponding two source
  interactions. Endpoint multiplicities one or two change the constant
  by at most two. Summing charges a pair--isolated edge once and a
  pair--pair edge twice before converting to ordered energies. All
  these edges belong to \(\Delta_{\rm out}\), not to \(\Delta_P\).
- Every interval of length \(R\) has at most two good sites. The tail in
  (2) therefore gives
  \(S_\phi:=\sup_y\sum_{j\in G}m_j\Phi(y-x_j)<\infty\), with a bound
  depending only on the frozen profile and \(R\). The ordered bad--good
  energy is at most \(2S_\phi\sum_Bm_i\le2S_\phi L(B)\). Together with
  (13), this pays for the bad--good and bad--bad terms using only
  \(\Delta_{\rm out}\).

Empty bad, paired or isolated subsets are allowed. Replacing
\(\Delta_{\rm out}\) by the total \(\Delta\) in (14) would discard
the exact budget needed for (5).

## A global lower bound attained by an actual pair

Set
\[
V_t(x)=F(x)-t\Phi(x),\qquad v(t)=\min_{x>0}V_t(x).
\]
For \(0<t<1\), the minimum exists and is negative. Indeed,
\(V_t(r)=-tM\) at an active root, \(V_t(x)\to0\) at infinity, and
\(V_t(0)=1-t\Phi(0)>0\), since \(\Phi(0)\le\int J_0=1\).
In particular \(v(t)\le-tM<0\).

Subtract \(t\) times (14) from \(E_{J_0}(W)=L+\Delta_P+\Delta_{\rm out}\):
\[
E_{J_0-t\phi}(W)\ge(1-t\Phi(0))L
 +\sum_{\{i,j\}\in\mathcal E}2m_im_jV_t(x_i-x_j)
 +(1-tC)\Delta_{\rm out}-\frac{tM}{2}L(U).
\tag{15}
\]
Choose, for example, \(t_\phi=1/[2(C+1)]\). The remaining-source
coefficient is then positive. Because \(v(t)<0\) and
\(2m_im_j\le m_i^2+m_j^2\), the matched sum is at least
\(v(t)L(P)\). Also
\[
-\frac{tM}{2}L(U)\ge v(t)L(U),\qquad
0\ge v(t)L(B).
\]
Using \(L=L(P)+L(U)+L(B)\) in (15) proves
\[
E_{J_0-t\phi}(W)\ge[1-t\Phi(0)+v(t)]L(W).
\tag{16}
\]
Conversely, for the simple pair \(W=\{0,x\}\), direct counting gives
\[
E_{J_0-t\phi}(W)/L(W)=1-t\Phi(0)+V_t(x).
\]
A minimizing separation proves (5). The same normalization holds for
two sites each of multiplicity two; no passage to infinitely distant
replicas or an unattained thermodynamic state is needed.

## Finite active branches determine the curvature

All minimizing separations remain in a fixed compact interval as
\(t\downarrow0\): outside a large interval \(\Phi<M/2\), so
\(V_t>-tM/2>v(t)\). On that compact interval they approach zeros of
\(F\), since away from the zero set \(F\) has a positive lower bound.
Only the roots in \(\mathcal Z_*\) survive for small \(t\). To see this,
choose small disjoint neighborhoods of the finitely many other roots
where \(\Phi\le M-\delta\) for one fixed \(\delta>0\). There
\(V_t\ge-t(M-\delta)>-tM\). The remaining compact complement is
excluded by its positive source minimum.

At an active root \(r\), \(F''(r)=2K'(r)^2>0\). The implicit function
theorem gives the unique local minimizing branch
\[
x_r(t)=r+\frac{\Phi'(r)}{2K'(r)^2}t+O_\phi(t^2),
\]
\[
V_t(x_r(t))=-tM-
 \frac{\Phi'(r)^2}{4K'(r)^2}t^2+O_\phi(t^3).
\tag{17}
\]
Negative roots give the same values by evenness. There are only finitely
many positive active branches, so taking their minimum gives (6), with
the maximum in (3), including ties. If every active derivative vanishes,
\(x_r(t)=r\) is the exact local branch, giving the affine case.

For \(\kappa>0\), the same result also identifies the sharp leading
constant of the real exposure modulus:
\[
\sup_{e(W)\le\varepsilon}h_\phi(W)
=\beta+2\sqrt\kappa\,\sqrt\varepsilon+O_\phi(\varepsilon).
\tag{18}
\]
Indeed (6) and \(1+e-th_\phi\ge q_\phi^{\mathbb R}(t)\) give
\(h_\phi-\beta\le\varepsilon/t+\kappa t+O_\phi(t^2)\); take
\(t=\sqrt{\varepsilon/\kappa}\). For the lower bound, choose a root
maximizing (3), and a signed displacement with \(F(r+\delta)=\varepsilon\)
and \(\delta\Phi'(r)>0\). Simplicity gives
\(\delta=\operatorname{sgn}(\Phi'(r))\sqrt\varepsilon/|K'(r)|+O_\phi(\varepsilon)\).
The actual pair then attains the asserted leading constant.

## Prior art, checks and boundary

The source kernel and its one-delta extremal role are classical:
[Carneiro--Chandee--Littmann--Milinovich, section 3.5, Corollary 14](https://arxiv.org/pdf/1406.5462).
Finite normalized pair-energy floors belong to classical stability
constant theory, as explained in ANF-018 and
[Procacci, section 1](https://arxiv.org/pdf/2005.10362).
[Sütő's theorem](https://arxiv.org/pdf/math-ph/0508004) treats
compact-Fourier infinite-volume ground states at prescribed densities;
it does not identify this finite-particle optimum with a two-site energy.
No RH-conditional zero statistic from these sources is used.

The derivation specific to this line is the allocation (12)--(14),
which makes the source cost outside a matching absorb the entire
outside-notch interaction and leaves the internal pair potential
unchanged. ANF-195 already supplies matching and paired-tail control;
ANF-199 supplies stationary contacts and individual Taylor upper bounds.
Neither states the exact perturbed all-cardinality floor (5). Targeted
checks against Montgomery--Taylor perturbations, classical pair-potential
stability and ground-state reductions did not identify that formula;
this is not a claim of exhaustive literature novelty. The Taylor and
implicit-function steps are classical. Existing SOURCES anchors suffice.

The decisive audit points are: the marked-site incident sums contain no
internal good matching edge; the two-endpoint estimate pays for outside
edges without spending \(\Delta_P\); the negative sign of \(v(t)\)
reverses the matched-weight comparison correctly; and multiplicity
normalization uses \(L\), not total particle number. The proof does not
rely on compactness of the original configuration class.

As a noncertifying numerical falsification attempt, use the triangular
profile \(\phi(u)=\tfrac1{10}(1-5|u|)_+\). It is admissible: on its
support, \(g\ge3/4\) follows from \(\cos(1/\sqrt2)\ge3/4\) and
\(\sin(1/\sqrt2)\le1/\sqrt2\). Hence
\(J_0(u)\ge(9/16)(1-|u|)\ge9/20>1/10\).
Ordinary floating-point evaluation gives \(r_1\approx1.0572782910\),
\(\beta\approx0.03722572960\), and
\(\kappa\approx7.92572779\cdot10^{-6}\). Local pair minimization at
\(t=0.02,0.01,0.005,0.001\) gives the coefficient in (6) to relative
error below \(2\cdot10^{-4}\). At each of \(t=0.001,0.01,0.02\),
1,660 sampled configurations (1,500 random configurations, seed 200,
with one through 18 sites in \([-30,30]\) and multiplicities one through
five, plus 160 separated pair arrays) stayed
above the candidate pair floor within a \(2\cdot10^{-12}\) tolerance.
These samples neither certify \(t_\phi\) nor prove the global bound;
(7)--(16) provide the analytic proof. No Lean validation is claimed.

The interval is fixed-profile and may become arbitrarily small under
profile variation; ANF-198's nonuniform controls are not contradicted.
The inverse-square tail is essential to the stated proof and is stronger
than the bare regularity of all profiles in ANF-195. The excluded case
\(M=0\) is the source-rescaling case treated separately by ANF-197.
Most importantly, positivity of the real pair terms in (7) does not
extend to arbitrary complex differences. This closes the small-amplitude
real finite-cluster optimization under (2), while the complex
near-extremizer exposure question in ANF-099 remains open. It supplies
no improved unconditional zero proportion, zero-density estimate or RH
conclusion.
