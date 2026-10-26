# ANF-213 — Small real notch minima reduce exactly to simple and double sites

**Status:** EXACT-DERIVED + ALL-REAL-MULTISETS + WIDTH-UNIFORM-REDUCTION.
For every triangular-notch width `0<eta<=1/2` and removed height
`0<a<=1/100`, every finite real multiset contains a nonempty submultiset
with no greater normalized energy, site multiplicities only one or two,
and at most four units of multiplicity in any half-open interval of
length `1/4`. Consequently these restrictions preserve the unrestricted
real infimum exactly. Every finite minimizer must satisfy them. This is
an exact variational reduction, including beyond the cubic two-site
window; it does not prove finite attainment or bound total cardinality.

## Object and exact reduction

Use `f_hat(x)=int f(u) exp(-2 pi i u x) du` and set
\[
g(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin(1/\sqrt2)}
\mathbf1_{[-1/2,1/2]}(u),\quad J_0=g*g,\quad
K=\widehat g,\quad F=\widehat J_0=K^2.
\tag{1}
\]
Thus `g>=0`, `int g=1`, `K(0)=F(0)=1`, and `F>=0` on the
real line. Define
\[
\tau_\eta(u)=(1-|u|/\eta)_+,\quad
\Phi_\eta(x)=\widehat{\tau_\eta}(x)
=\eta\operatorname{sinc}^2(\eta x),\quad
J_{\eta,a}=J_0-a\tau_\eta,
\]
\[
V(x)=F(x)-a\Phi_\eta(x),\qquad A=V(0)=1-a\eta,
\tag{2}
\]
where `sinc(t)=sin(pi t)/(pi t)`, continuously at zero. The amplitude
`a` is removed spectral height. Throughout,
\[
0<\eta\le\tfrac12,\qquad 0<a\le\tfrac1{100},\qquad
\tfrac{199}{200}\le A<1.
\tag{3}
\]
For a nonempty finite real multiset with distinct sites `x_i` and
positive integer multiplicities `m_i`, put
\[
\ell(0)=0,\quad\ell(1)=1,\quad\ell(m)=2m\ (m\ge2),\qquad
L(W)=\sum_i\ell(m_i),
\]
\[
E(W)=\sum_{i,j}m_im_jV(x_i-x_j)
=\int J_{\eta,a}(u)\left|\sum_i m_i e^{-2\pi iux_i}\right|^2du,
\qquad Q(W)=E(W)/L(W).
\tag{4}
\]
Let
\[
M(W)=\max_{y\in\mathbb R}
\sum_{x_i\in[y,y+1/4)}m_i,
\qquad
\mathcal R=\{W:m_i\in\{1,2\},\ M(W)\le4\}.
\tag{5}
\]
The maximum exists: the attained occupancies form a nonempty finite
set of integers. The claim is
\[
\boxed{\forall W\ \exists\ \varnothing\ne Z\subseteq W:
\quad Z\in\mathcal R,\qquad Q(Z)\le Q(W).}
\tag{6}
\]
Containment retains the original positions and only reduces integer
multiplicities, possibly removing entire sites. In particular,
\[
\boxed{q^{\mathbb R}_{\eta,a}:=\inf_W Q(W)
=\inf_{W\in\mathcal R}Q(W).}
\tag{7}
\]
There is no original separation, span, density or cardinality assumption.

The spectrum stays positive in (3). With `theta=1/sqrt(2)`,
`sin theta<=theta` and `cos theta>=1-theta^2/2=3/4` give
`g>=3/4` on its support. Hence
`J_0(u)>=(9/16)(1-|u|)` on `[-1,1]`. On the notch support
`J_0>=9/32>1/4`, so `tau_eta<=4J_0` and
`J_(eta,a)>=(1-4a)J_0>0` wherever `J_0>0`.
Also `E_(J_0)>=sum m_i^2>=L`; thus the infimum is positive.

## Local repulsion and a width-uniform attraction bound

Because `g` is an even probability density on `[-1/2,1/2]`,
\[
|x|\le\tfrac14\quad\Longrightarrow\quad
K(x)=\int g(u)\cos(2\pi ux)\,du
\ge\cos(\pi|x|)\ge\tfrac1{\sqrt2}.
\]
Consequently
\[
F(x)\ge\tfrac12\quad(|x|\le\tfrac14).
\tag{8}
\]
No kernel-zero asymptotic or triple-gap theorem is used here.

For every finite multiset and every real `y`,
\[
\boxed{\sum_jm_j\Phi_\eta(y-x_j)\le7M(W).}
\tag{9}
\]
To prove this, partition the line into half-open cells of length
`h=1/4`, with `y` in the cell indexed zero. Each cell has mass at
most `M(W)`. The cells with indices `-1,0,1` contribute at most
`3 eta M(W)`. For `|k|>=2` the distance is at least
`(|k|-1)h`, and
\[
0\le\Phi_\eta(x)\le
\min\{\eta,1/(\pi^2\eta x^2)\}.
\]
The decreasing majorant
`f(t)=min(eta,1/(pi^2 eta h^2 t^2))` satisfies
\[
\sum_{n\ge1}f(n)\le\int_0^\infty f(t)\,dt
=\frac2{\pi h}.
\]
Thus the row sum divided by `M(W)` is at most
\[
3\eta+\frac4{\pi h}\le\frac32+\frac{16}{\pi}
<\frac{41}{6}<7,
\tag{10}
\]
using `pi>3`. The bound includes the self-interaction and is uniform
as the notch becomes narrow; replacing the whole tail by its height
would introduce an invalid factor of total cardinality.

## A minimizing submultiset cannot be overcrowded

Among the finitely many nonempty submultisets of a given `W`, choose
`Z` minimizing `Q`. Since every singleton has energy `A`,
\[
q:=Q(Z)\le\min\{Q(W),A\}.
\tag{11}
\]
For a site `x_i` of `Z`, write
`P_i=sum_j m_j V(x_i-x_j)`. Deleting one copy at that site, when
the resulting `Z'` is nonempty, gives exactly
\[
D_i:=E(Z)-E(Z')=2P_i-A,
\qquad d_i:=L(Z)-L(Z')=
\begin{cases}1,&m_i=1,\\3,&m_i=2,\\2,&m_i\ge3.\end{cases}
\tag{12}
\]
In particular, the double-to-single transition loses **three** units
of `L`. Optimality among submultisets implies
\[
D_i\le d_i q\le3A.
\tag{13}
\]

Suppose `M:=M(Z)>=5`. Select an interval realizing this mass and
any site `x_i` in it. All its points are within `1/4` of `x_i`.
Equation (8), positivity of every other `F` term, and (9) imply
\[
P_i\ge\tfrac12 M-7aM,\qquad
D_i\ge(1-14a)M-A.
\]
Since `M>=5`, (3) gives
\[
D_i-3A\ge\tfrac{43}{50}\,5-4A
\ge\tfrac3{10}>0,
\tag{14}
\]
contradicting (13). The deletion is legal because `|Z|>=5`.
Therefore `M(Z)<=4`.

## Multiplicity three or higher is then strictly removable

Suppose some `m_i>=3`. Keep its self-term exactly and use only
`F>=0` on other sites. Equations (9) and `M(Z)<=4` give
\[
P_i\ge m_i A-28a,\qquad
D_i\ge(2m_i-1)A-56a.
\tag{15}
\]
Here `d_i=2`, so
\[
D_i-2q\ge3A-56a
\ge3\frac{199}{200}-\frac{56}{100}
=\frac{97}{40}>0.
\tag{16}
\]
This contradicts the first inequality in (13). The remaining multiset
is nonempty because the removed copy came from a site of multiplicity
at least three. Thus `Z` has only simple and double sites, proving
(6)--(7).

The same argument applies to every configuration with `Q<=A` that
cannot be improved by deleting one copy. Therefore every finite global
minimizer obeys (5). More constructively, whenever `Q<=A`, a deletion
from an overcrowded interval decreases `Q`; once every such interval
has mass at most four, removing a copy from any site of multiplicity
at least three also decreases `Q`. The process is finite and never
empties the configuration. This is not a claim that simultaneously
clipping all original multiplicities at two preserves the energy ratio.

## Prior art, audit and consequence

[Ruelle, *Superstable Interactions in Classical Statistical Mechanics*,
section 1](https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B28%5D.pdf),
provides the classical local-repulsion and summable-attraction framework.
[Bellissard--Radin--Shlosman, *The characterization of ground states*,
proof of Lemma 3](https://arxiv.org/pdf/0907.5393), uses particle removal
to rule out excessive local repulsion. Its displayed proof concerns
hard-core finite-range interactions; those hypotheses are not assumed
here. Neither a new superstability principle nor a new deletion method
is claimed. The proof above instead supplies the finite, explicit,
width-uniform bounds for this bounded kernel and its affine denominator.

[Knausgård, section 7.1](https://arxiv.org/html/2610.08965v1#S7.SS1)
studies labelled simple/double Montgomery--Taylor configurations, but
uses their restriction to obtain an upper bound on a different,
constrained-density objective. It does not identify that restricted
minimum with the arbitrary-multiplicity notch quotient in (7).
Targeted checks of this literature and particle-removal/local-density
arguments did not identify the precise reduction (6); no exhaustive
novelty claim is made.

Locally, ANF-081 bounds the error of clipping near the real equality
face, and ANF-195/ANF-200/ANF-209 use excess-paid deletion or matching
to control notch exposure and the two-site window. Equations (6)--(7)
give a different conclusion: the **actual** unrestricted real minimum
may be optimized over bounded local occupation and multiplicities
`1/2`, with no approximation error and no assumption that pairs remain
optimal. In particular this applies throughout `a=lambda eta^3` for
any fixed `lambda>0` and sufficiently small widths. ANF-212's mixed
`(1,2,2)` witness lies inside the surviving class. Higher site
multiplicities are excluded as a separate route to lowering the global
real floor; this does not establish optimality of that witness.

The decisive audit is entirely elementary: (8)'s cosine bound, the full
tail integral in (10), the exact denominator increments `(1,3,2)`, and
the strict rational margins (14) and (16). These constants were checked
with exact rational arithmetic, and the energy-removal identity was
checked algebraically. No numerical optimization, finite search over
configurations or Lean verification is used as proof.

The interval cap is not a minimum gap: up to four units may still
cluster within a short interval. Nor is it a total-cardinality cap;
arbitrarily many intervals may be occupied. The theorem neither locates
the first cubic transition nor gives compactness modulo translation,
finite attainment, an unrestricted complex floor, or any new zeta-zero
bound. Its real restriction is load-bearing: the positive real pair
terms used in (8), (14) and (15) do not survive arbitrary nonreal
geometry. The amplitude `1/100` and local cap four are sufficient
constants, not asserted sharp.
