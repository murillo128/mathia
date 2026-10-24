# ANF-199 — Stationary source-zero contacts characterize linear real notch stability

**Status:** EXACT-DERIVED + REAL-MULTISET + STATIONARY-CONTACT-CLASSIFICATION + EXACT-INITIAL-AFFINE-FLOOR. For dominated positive-Fourier profiles with an inverse-square Fourier tail, the square-root loss in ANF-195 disappears exactly when every maximizing source zero is a stationary point of the notch transform. This gives an exact initial affine segment of the real certificate. Nonscalar profiles satisfying this condition exist, and some strictly improve the real normalized objective. None of these statements controls the complex configuration class.

## Statement

Use the Fourier convention \(\widehat f(t)=\int f(u)e^{-2\pi iut}\,du\) and
\[
g(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin(1/\sqrt2)}
\mathbf1_{[-1/2,1/2]}(u),\qquad J_0=g*g,\qquad F=\widehat J_0=K^2,
\]
\[
K(t)=\frac{\cos(\pi t)-a t\sin(\pi t)}{1-2\pi^2t^2},
\qquad a=\sqrt2\pi\cot(1/\sqrt2),\qquad K(0)=1.
\tag{1}
\]
Continue the removable points. ANF-087 gives the simple positive zeros
\(r_j\in(j,j+1/2)\), their sum-free property, and the impossibility of
three distinct real sites whose pairwise differences are all zeros of \(K\).

Freeze a real even integrable profile satisfying
\[
0\le\phi\le J_0,\qquad \Phi:=\widehat\phi\ge0,\qquad
\Phi(t)\le D_\phi/(1+t^2)\quad(t\in\mathbb R),
\]
\[
M:=\max_{j\ge1}\Phi(r_j)>0,\qquad
\mathcal Z_*:=\{r_j:\Phi(r_j)=M\}.
\tag{2}
\]
The active set \(\mathcal Z_*\) is finite and nonempty. Compact support
of \(\phi\) makes \(\Phi\) smooth with bounded derivatives of every
fixed order; no differentiability of \(\phi\) is assumed in (2).

For a nonempty finite real multiset \(W\), set
\[
L=2|W|-\sigma(W),\quad S_W(u)=\sum_{x\in W}e^{-2\pi iux},\quad
e(W)=\frac{\int J_0|S_W|^2}{L}-1,\quad
h_\phi(W)=\frac{\int\phi|S_W|^2}{L}.
\tag{3}
\]
Here \(\sigma\) counts distinct real sites of multiplicity one.
Below \(E_\phi(V)=\int\phi|S_V|^2\) and
\(E_0(V)=\int J_0|S_V|^2\) denote unnormalized energies.
ANF-195 proves the exact real envelope
\(\beta=\beta_\phi^{\mathbb R}=\Phi(0)+M\). Then
\[
\boxed{
\exists C_\phi<\infty\ \forall W:\quad h_\phi(W)\le\beta+C_\phi e(W)
\quad\Longleftrightarrow\quad
\Phi'(r)=0\quad\forall r\in\mathcal Z_*.
}
\tag{4}
\]
The constant is uniform in cardinality, multiplicity and diameter, but
depends on the fixed profile. If the condition fails, no exponent
\(p>1/2\) can replace the linear exponent in (4), while a bound
\(h_\phi\le\beta+A_\phi\sqrt e+B_\phi e\) does hold.

Equivalently, for the real floor
\[
q_\phi^{\mathbb R}(t)=\inf_W\{1+e(W)-t h_\phi(W)\},\qquad 0\le t<1,
\tag{5}
\]
stationarity in (4) holds if and only if this floor agrees with
\(1-t\beta\) on some interval of positive length starting at zero.
This is a statement about the entire finite-real-multiset infimum,
not merely the derivative supplied by ANF-099.

## Local contact is necessary, but its global sufficiency needs matching

At any active root \(r\), the two simple sites \(W_\delta=\{0,r+\delta\}\)
satisfy
\[
e(W_\delta)=K(r+\delta)^2
=K'(r)^2\delta^2+O(\delta^3),
\]
\[
h_\phi(W_\delta)-\beta
=\Phi'(r)\delta+O(\delta^2).
\tag{6}
\]
If \(\Phi'(r)\ne0\), choose the sign of \(\delta\) to make the
linear term positive. This disproves every uniform \(O(e^p)\) upper
modulus with \(p>1/2\), including (4).

Suppose instead that every active derivative vanishes. There is a finite
\(A\ge0\) with the pointwise bound
\[
\Phi(t)\le M+A F(t)\qquad(t\in\mathbb R).
\tag{7}
\]
Indeed \(\Phi<M\) outside a compact interval. At a source zero with
\(\Phi(r)<M\), continuity gives a neighborhood with the same strict
inequality. At an active zero, Taylor's theorem gives
\(\Phi(t)-M=O((t-r)^2)\), while simplicity gives
\(F(t)\asymp(t-r)^2\). The remaining compact set is bounded away
from the zero set. Evenness handles negative roots. There are only
finitely many roots to check in the compact interval.

Summing (7) over all pairs would incorrectly charge \(M\) quadratically
in the number of sites. The following reconstruction of ANF-195's fixed
matching argument avoids that loss.

Write distinct sites as \(x_i\) with multiplicities \(m_i\), and
\(\Delta=Le(W)\). The exact positive decomposition is
\[
\Delta=\sum_{m_i\ge3}m_i(m_i-2)
 +2\sum_{i<j}m_im_jF(x_i-x_j).
\tag{8}
\]
For each sufficiently large fixed \(R\), there are neighborhoods
\(\mathcal U_R\) of the finitely many positive source roots in
\([0,R]\) and \(d_R>0\) such that
\[
F(t)+F(t-r)\ge\frac{d_R}{1+t^2}
\qquad(t\in\mathbb R,\ r\in\mathcal U_R).
\tag{9}
\]
For clarity, (9) is source-specific: the asymptotic
\(K(t)=\frac{a}{2\pi^2}\sin(\pi t)/t+O(t^{-2})\) and
\[
\sin^2\theta+\sin^2(\theta-\pi r)\ge1-|\cos(\pi r)|
\]
give the uniform bound at infinity, because the finitely many roots
are nonintegral. On compact \(t\)-sets, simultaneous vanishing would
give the forbidden zero triple \(0,r,t\). Shrinking the finitely many
neighborhoods proves (9). In particular (2) implies
\[
\Phi(t)+\Phi(t-r)\le C_{\phi,R}\{F(t)+F(t-r)\}.
\tag{10}
\]

Choose \(R>\max(1,r_1)\) so large that
\(4D_\phi R^{-2}\sum_{n\ge1}n^{-2}\le M/2\).
Next choose a fixed \(\gamma>0\) small enough that:

- every \(0<r\le R\) with \(F(r)\le\gamma\) lies in \(\mathcal U_R\);
- \(\gamma<\min_{u,v\in[-R,R]}\max\{F(u),F(v),F(u-v)\}\).

The last minimum is positive by the zero-triple exclusion, including
coincident-site limits since \(F(0)=1\).

Delete every site of multiplicity at least three, and then every
remaining site with incident sum
\(\sum_{j\ne i}m_jF(x_i-x_j)>\gamma\), calculated within the
remaining sites. Call the deleted multiset \(B\), and the rest \(G\).
Equation (8), with whole-site deletion, gives
\[
L(B)\le(2+2/\gamma)\Delta,\quad
E_\phi(B)\le E_0(B)\le L(B)+\Delta\ll_\phi\Delta.
\tag{11}
\]
For the first deletion use \(2m\le2m(m-2)\) for \(m\ge3\);
for the second use \(m_i^2\le2m_i\) and sum the incident energies.
All off-diagonal source energies in a subset are subterms of (8).

The distance-\(R\) graph on \(G\) is a matching. Otherwise a vertex
and two neighbors contradict the second choice of \(\gamma\).
Let \(P\) be the union of matched pairs and \(U\) the isolated sites.
All good multiplicities are one or two and
\(L(G)=\sum_{G}m_i^2=L(P)+L(U)\). Its notch energy has these parts:

- The diagonal is \(\Phi(0)L(G)\).
- By (7) and \(2m_im_j\le m_i^2+m_j^2\), matched edges contribute at
  most \(ML(P)+A\Delta\).
- Isolated sites are more than \(R\) apart. Their ordered mutual
  energy is at most \((M/2)L(U)\), by the choice of \(R\), the
  multiplicity bound two and the inverse-square tail.
- Interactions involving a pair and a site outside it are
  \(O_\phi(\Delta)\) by (10). Endpoint weights one or two cost at
  most a factor two. Summing over pairs charges an edge between two
  paired components twice and a pair--isolated edge once; the ordered
  source sum in (8) pays for both.

Thus \(E_\phi(G)\le\beta L(G)+O_\phi(\Delta)\). Every interval of
length \(R\) contains at most two good sites. The inverse-square tail
therefore gives
\(\sup_y\sum_{j\in G}m_j\Phi(y-x_j)<\infty\).
The ordered \(B\)--\(G\) notch interaction is consequently
\(O_\phi(\sum_{B}m_i)=O_\phi(L(B))=O_\phi(\Delta)\).
Together with (11) this proves (4), including empty components and
unbounded original multiplicities.

Without stationarity, the same compact-root argument gives
\(\Phi(t)\le M+A|K(t)|\). Only the matched-edge estimate changes:
weighted Cauchy--Schwarz bounds its additional term by
\(A\sqrt{L(P)\Delta}\). Every other term above is still
\(O_\phi(\Delta)\). This proves the asserted square-root upper bound
throughout (2), without importing an \(H^1\) assumption.

## Exact initial affine floor versus immediate curvature

Enlarge the constant in (4) to \(C_\phi\ge1\). For
\(0\le t\le1/(2C_\phi)\),
\[
1+e-t h_\phi\ge1-t\beta+(1-tC_\phi)e\ge1-t\beta.
\]
The equality pair \(\{0,r\}\), \(r\in\mathcal Z_*\), attains
the last floor. Hence
\[
q_\phi^{\mathbb R}(t)=1-t\beta
\qquad(0\le t\le1/(2C_\phi)).
\tag{12}
\]
Conversely, if equality holds at even one \(t_0>0\), every multiset
satisfies \(h_\phi\le\beta+e/t_0\), so (4) forces stationarity.

If an active root has \(d=\Phi'(r)\ne0\) and \(k=K'(r)\ne0\),
insert \(\delta=t d/(2k^2)\) into (6). It gives the explicit upper
bound
\[
q_\phi^{\mathbb R}(t)
\le1-t\beta-\frac{d^2}{4k^2}t^2+O_\phi(t^3)
\qquad(t\downarrow0).
\tag{13}
\]
Indeed for every fixed \(t>0\), a sufficiently small signed
\(\delta\) makes the linear term \(-td\delta\) dominate the
quadratic source cost, so \(q_\phi^{\mathbb R}(t)<1-t\beta\).
This is an upper bound from actual configurations, not an asserted
second-order expansion of the full infimum.

## Nonscalar stationary profiles exist and the linear exponent can be sharp

Fix \(0<\lambda<1\). For all sufficiently large root indices \(n\),
choose a real \(v_n\) near \(r_n\) solving
\[
F'(r_n-v_n)+F'(r_n+v_n)=0,\qquad
v_n-r_n=O(r_n^{-2}).
\tag{14}
\]
Here is an existence proof with no numerical root-selection premise.
Since \(J_0\ge0\), \(\int J_0=1\), and it is positive on an
interval,
\(F''(0)=-4\pi^2\int u^2J_0(u)\,du<0\).
Choose \(0<\delta_0<1/4\) so that \(F''\le-\kappa<0\) on
\([-\delta_0,\delta_0]\). Differentiating (1) gives
\(F^{(j)}(t)=O(t^{-2})\) at infinity for \(j=0,1,2\).
The left side of (14), as a function of \(v\), is negative at
\(r_n-\delta_0\), positive at \(r_n+\delta_0\), and has
derivative at least \(\kappa/2\) between them for large \(n\).
It has one root there. Its value at \(v=r_n\) is
\(F'(2r_n)=O(r_n^{-2})\), proving the displacement bound.

Define the fixed profile
\[
\phi_n(u)=\frac{J_0(u)}{1+\lambda}
 [1+\lambda\cos(2\pi v_nu)],
\]
\[
\Phi_n(t)=\frac1{1+\lambda}
 \left[F(t)+\frac\lambda2\{F(t-v_n)+F(t+v_n)\}\right].
\tag{15}
\]
It is nonscalar, continuous and even, and
\[
\frac{1-\lambda}{1+\lambda}J_0\le\phi_n\le J_0,
\qquad\Phi_n\ge0,\qquad\Phi_n(t)\ll_n(1+t^2)^{-1}.
\tag{16}
\]
The last bound is for each fixed \(n\), with no uniformity in \(n\).

The unique positive active source root is \(r_n\). To prove this,
\(|K(t)|<1\) for every nonzero real \(t\), since \(K\) is the
Fourier transform of the positive density \(g\) of total mass one.
Fourier decay and continuity imply
\(q_*:=\sup_{|t|\ge1/4}F(t)<1\).
Distinct source roots are more than \(1/2\) apart. Thus, for \(j\ne n\)
and large \(n\),
\[
F(r_j-v_n)+F(r_j+v_n)\le q_*+O(r_n^{-2}),
\]
whereas at \(j=n\) the same sum is \(1+O(r_n^{-2})\).
At all these roots the unshifted \(F\) term vanishes. This proves
uniqueness and \(M_n>0\). Also \(F'(r_n)=0\), so (14) gives
\(\Phi_n'(r_n)=0\). Therefore (4) and (12) apply to this genuine
spectral direction, not just to ANF-197's source rescalings.

For each such fixed profile set \(r=r_n\), and consider the four
distinct simple sites \(W_m=\{0,r,m,m+r\}\) for sufficiently large
positive integers \(m\). Exact pair counting gives
\[
e(W_m)=F(m)+\tfrac12\{F(m-r)+F(m+r)\}>0,\qquad e(W_m)\to0,
\]
\[
h_{\phi_n}(W_m)-\beta_n
=\Phi_n(m)+\tfrac12\{\Phi_n(m-r)+\Phi_n(m+r)\}
\ge\frac{e(W_m)}{1+\lambda}.
\tag{17}
\]
Strict source positivity follows already from
\(F(m)=(1-2\pi^2m^2)^{-2}>0\).
The inequality uses Fourier-side domination
\(\Phi_n\ge F/(1+\lambda)\) in (15), not the smaller physical-side
constant in (16). Hence no \(O(e^p)\) bound with \(p>1\) is possible
for these stationary examples. Their linear rate is sharp.

They can also improve the **real** normalized objective. Put
\[
C(J)=J(0)+\int_{-1}^1|u|J(u)\,du,\quad
C_0=C(J_0),\quad b_*=J_0(0)/C_0.
\]
One has \(b_*>1/2\): Cauchy--Schwarz on the length-one support of
\(g\) gives \(J_0(0)=\int g^2\ge1\), while
\(\int|u|J_0(u)\,du<\int J_0=1\).
Riemann--Lebesgue and (14)--(15) give
\[
\frac{C(\phi_n)}{C_0}\longrightarrow
 \frac{1+\lambda b_*}{1+\lambda},\qquad
\beta_n\longrightarrow\frac{1+\lambda/2}{1+\lambda}.
\tag{18}
\]
Thus \(C(\phi_n)/C_0>\beta_n\) for large \(n\). Throughout the
positive initial interval (12),
\(C(J_0-t\phi_n)/(1-t\beta_n)<C_0\).
The interval may shrink with \(n\); no profile-uniform amplitude
claim is made. These profiles have full support \([-1,1]\), not a
prescribed proper central support.

## Prior art, audit controls and boundary

The source kernel is classical: [Carneiro--Chandee--Littmann--Milinovich,
section 3.5, Corollary 14](https://arxiv.org/pdf/1406.5462).
The finite-real envelope, matching decomposition and paired-source tail
estimate are ANF-195; the zero geometry is ANF-087. The new conclusion
is the necessary-and-sufficient stationary-contact condition, its exact
initial affine-floor interpretation, and a nonscalar sharp linear class.

Double contact as a way to certify energy inequalities is classical.
[Cohn--Kumar, *Universally optimal distribution of points on spheres*,
sections 2.1 and 5](https://arxiv.org/pdf/math/0607446) construct auxiliary
functions matching both values and derivatives at active distances.
That method does not directly supply (4): here the number of points and
the real diameter are unrestricted, and a global sum of the contact
bound (7) would lose a factor of cardinality. The source-paid matching
and paired tail are essential additional inputs.
[Sütő's compact-Fourier ground-state theory](https://arxiv.org/abs/math-ph/0508004)
concerns infinite-volume configurations and density thresholds, rather
than this normalized finite-multiset stability classification. Targeted
searches by positive pair energies, stationary contact, Hermite energy
certificates and Montgomery--Taylor stability identified these classical
mechanisms, not a direct statement of (4). No global novelty claim is made.

The proof is exact analytic derivation. Its critical checks are the
whole-site multiplicity tax (8), the two-endpoint estimate (9), fixed-scale
matching instead of summing a constant over all pairs, and stationarity
at **every** active root. Cancellation at only one of several maximizing
roots is insufficient. The inverse-square tail is part of the theorem:
the weaker \(H^1\) squared-cost argument in ANF-195 yields a square-root
cross-component loss and does not establish this linear criterion.

As noncertifying numerical sanity checks, ordinary floating-point
bisection at \(\lambda=1/2\) and \(n\in\{5,10,20,40\}\) found
contact derivative residuals below \(2\cdot10^{-15}\), with the chosen
root maximizing the sampled values over the first 500 source roots.
The twelve four-site checks at those indices and
\(m\in\{100,1000,10000\}\) satisfied (17). These finite checks
do not establish the all-root maximum, uniform multiset bound or
existence assertion; those follow from the displayed analytic proofs.

This does not prove that any triangular notch has stationary maximizing
roots, classify the exceptional widths mentioned in ANF-195, or control
the unrestricted complex envelope. Positive real pair energies underlie
(8)--(11); they cannot be silently used at complex differences. No new
zero-density bound, unconditional zero proportion, RH conclusion, or
Lean verification is asserted.
