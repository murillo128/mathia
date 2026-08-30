# PF-120 — cusp Busemann shifts must synchronize in any bilipschitz quadrilateral comparison

**Status:** `EXACT-DERIVED + NEGATIVE/BOUNDARY`. The cusp-distance calculation below is elementary hyperbolic geometry. The project-specific consequence is that the two natural sidewise isometries of the PF-119 Lambert quadrilateral carry a reciprocal-prime relative Busemann shift and therefore **cannot** be the boundary traces of one finite-bilipschitz comparison map. This identifies a precise cusp-gauge constraint on the accepted shift-clone operator program. It does not obstruct a synchronized comparison: the mismatch can be redistributed along the cusp rays with arbitrarily small extra one-dimensional Lipschitz cost. No interior quadrilateral homeomorphism, global flute comparison, compact relative resolvent, scattering, determinant, or RH conclusion is claimed.

## Claim

Let

\[
Q(a)=\{\text{the PF-119 ideal Lambert quadrilateral}\},
\qquad a>0,
\]

in the normalized upper half-plane model with boundary geodesics

\[
x=0,\qquad x=1,\qquad |z|=r(a),\qquad |z-1|=s(a),
\]

where

\[
\boxed{
r(a)=\tanh a,
\qquad
s(a)=\operatorname{sech}a,
\qquad
r(a)^2+s(a)^2=1.
}
\tag{1}
\]

The two vertical sides meet at the ideal cusp `infinity`. Consider two parameters `a,a'>0`, and suppose a `K`-bilipschitz homeomorphism

\[
F:Q(a)\longrightarrow Q(a')
\]

maps the two vertical cusp rays to the corresponding vertical cusp rays. If, for some positive constants `kappa_0,kappa_1`, its boundary traces satisfy

\[
F(iy)=i\,\kappa_0 y\,(1+o(1)),
\qquad
F(1+iy)=1+i\,\kappa_1 y\,(1+o(1))
\qquad (y\to\infty),
\tag{2}
\]

then necessarily

\[
\boxed{\kappa_0=\kappa_1.}
\tag{3}
\]

Thus a finite-bilipschitz comparison cannot assign different asymptotic Busemann translations to the two rays of the same cusp.

Now take the two most obvious boundary isometries that send the finite endpoints of those rays to the corresponding endpoints for `Q(a')`:

\[
I_0(iy)=i\,\lambda y,
\qquad
\lambda:=\frac{r(a')}{r(a)},
\tag{4}
\]

and

\[
I_1(1+iy)=1+i\,\kappa y,
\qquad
\kappa:=\frac{s(a')}{s(a)}.
\tag{5}
\]

They are individually hyperbolic isometries of their vertical geodesics. But

\[
\boxed{
\frac{\lambda}{\kappa}
=
\frac{\sinh a'}{\sinh a}.
}
\tag{6}
\]

Therefore, whenever `a' != a`, equations (3)--(6) imply

\[
\boxed{
\text{no finite-bilipschitz }Q(a)\to Q(a')
\text{ can restrict to both }I_0\text{ and }I_1.
}
\tag{7}
\]

For the exact prime/shift-clone half-cuffs

\[
a_n=\frac{\ell_n}{2},
\qquad
a_n^+=\frac{\ell_n^+}{2},
\]

define the natural cusp-normalization mismatch

\[
M_n:=
\log\frac{\lambda_n}{\kappa_n}
=
\log\frac{\sinh a_n^+}{\sinh a_n}.
\tag{8}
\]

Using the exact collar identity from PF-032/PF-114,

\[
\sinh a_n\,\sinh\frac{h_n}{2}=1,
\]

one obtains

\[
\boxed{
M_n
=
-\log\frac{\sinh(h_n^+/2)}{\sinh(h_n/2)}
=
-\delta_n+o(p_n^{-1})
=
\frac1{p_n}+o(p_n^{-1}),
}
\tag{9}
\]

where

\[
\delta_n=\log\frac{h_n^+}{h_n}
=-\frac1{p_n}+o(p_n^{-1})
\]

is the PF-114 shift factor. In particular

\[
\boxed{
\sum_n M_n=\infty.
}
\tag{10}
\]

So the same reciprocal-prime scale that appears in the nonsummable relative seam mode also appears as the mismatch between two **independently canonical cusp gauges**. Equation (7) shows that this mismatch cannot be interpreted as two simultaneously realizable boundary isometries of a genuine bilipschitz comparison.

However, (10) is **not** a bilipschitz obstruction. Once one chooses a common asymptotic cusp scale, either vertical boundary map can interpolate from its forced finite endpoint to that common scale over an arbitrarily long cusp interval. For any fixed pair `a,a'` and any `eta>0`, such a one-dimensional interpolation can be chosen with logarithmic derivative in

\[
[1-\eta,1+\eta]
\]

outside the unavoidable endpoint-length ratios. Thus the cusp mismatch can be pushed arbitrarily far toward the ideal end and paid with arbitrarily small additional boundary stretch. The unresolved problem remains the **interior** extension with synchronized cusp data.

## 1. Universal cusp synchronization lemma

For points on the two vertical rays at equal height, put

\[
P_y=iy,
\qquad
Q_y=1+iy.
\]

The upper-half-plane distance formula gives

\[
\cosh d(P_y,Q_y)
=1+\frac1{2y^2},
\]

hence

\[
d(P_y,Q_y)=2\operatorname{arsinh}\frac1{2y}\longrightarrow0.
\tag{11}
\]

Under the boundary asymptotics (2), write

\[
P_y'=i\kappa_0y(1+o(1)),
\qquad
Q_y'=1+i\kappa_1y(1+o(1)).
\]

The same exact distance formula yields

\[
\begin{aligned}
\cosh d(P_y',Q_y')
&=
1+
\frac{
1+(\kappa_0-\kappa_1)^2y^2+o(y^2)
}{
2\kappa_0\kappa_1y^2(1+o(1))
}\\
&\longrightarrow
1+
\frac{(\kappa_0-\kappa_1)^2}{2\kappa_0\kappa_1}\\
&=
\cosh\left|\log\frac{\kappa_0}{\kappa_1}\right|.
\end{aligned}
\tag{12}
\]

Therefore

\[
\boxed{
d(P_y',Q_y')
\longrightarrow
\left|\log\frac{\kappa_0}{\kappa_1}\right|.}
\tag{13}
\]

But `K`-Lipschitzness gives

\[
d(P_y',Q_y')\le Kd(P_y,Q_y)\longrightarrow0.
\]

Equations (11)--(13) force (3).

The argument needs only the upper Lipschitz bound. It is a local statement about one cusp and contains no prime arithmetic.

## 2. The two natural endpoint-preserving side isometries are incompatible

On the outer ray `x=0`, the finite endpoint is

\[
i r(a),
\]

so the unique orientation-preserving hyperbolic isometry of that vertical geodesic sending the finite endpoint to `i r(a')` is multiplication of height by

\[
\lambda=\frac{r(a')}{r(a)}.
\]

On the central ray `x=1`, the finite endpoint is

\[
1+i s(a),
\]

and the analogous boundary isometry multiplies height by

\[
\kappa=\frac{s(a')}{s(a)}.
\]

Using `r=tanh a` and `s=sech a`,

\[
\frac{\lambda}{\kappa}
=
\frac{\tanh a'}{\tanh a}
\frac{\operatorname{sech}a}{\operatorname{sech}a'}
=
\frac{\sinh a'}{\sinh a},
\]

which proves (6). Since `sinh` is strictly increasing, the ratio equals one exactly when `a'=a`.

This kills a tempting construction strategy for the accepted clue: map each geodesic side by its own canonical endpoint-preserving isometry and then try to fill the interior. The boundary data themselves already violate the cusp synchronization lemma.

## 3. Exact shift-clone size of the gauge mismatch

PF-114 uses

\[
h_n^+=h_n e^{\delta_n},
\qquad
\delta_n=-\frac1{p_n}+o(p_n^{-1}),
\tag{14}
\]

with `delta_n<0` on the tail. The collar identity gives

\[
\frac{\sinh a_n^+}{\sinh a_n}
=
\frac{\sinh(h_n/2)}{\sinh(h_n^+/2)}.
\tag{15}
\]

Let

\[
E(x)=\log\frac{\sinh(x/2)}{x/2}.
\]

Then `E(x)=x^2/24+O(x^4)` and `E'(x)=O(x)` as `x->0`. From (15),

\[
M_n
=-\delta_n+E(h_n)-E(h_n^+).
\tag{16}
\]

PF-114 proves `h_n->0`; moreover (14) gives

\[
h_n-h_n^+
=h_n\bigl(1-e^{\delta_n}\bigr)
=O(h_n/p_n).
\]

The mean-value theorem and `E'(x)=O(x)` therefore give

\[
E(h_n)-E(h_n^+)
=O(h_n^2/p_n)
=o(p_n^{-1}).
\tag{17}
\]

Combining (14), (16), and (17) proves (9). Since `M_n>0` on the tail and Euler's reciprocal-prime sum diverges, (10) follows.

A weaker conclusion, sufficient for divergence, follows even without the pointwise refinement (17): PF-114's `sum h_n^2<infinity` makes the correction in (16) absolutely summable while `sum(-delta_n)=infinity`.

## 4. Why synchronization is a constraint, not a new obstruction

Suppose one vertical side is parametrized by hyperbolic arclength

\[
t=\log(y/y_0)\in[0,\infty)
\]

from its finite endpoint. Let the target finite endpoint enforce an initial height ratio `gamma>0`, while a global cusp construction requires a common asymptotic height ratio `kappa>0`.

Choose a smooth cutoff `chi:[0,infinity)->[0,1]` with

\[
\chi(0)=0,
\qquad
\chi(t)=1\text{ for }t\ge T,
\qquad
|\chi'(t)|\le C/T.
\]

Define the target arclength coordinate by

\[
f(t)=t+\chi(t)\log\frac{\kappa}{\gamma}.
\tag{18}
\]

Then the boundary map

\[
y=y_0e^t
\longmapsto
 y'=y_0' e^{f(t)}
\]

starts at the required target endpoint and, for `t>=T`, has the desired common asymptotic Busemann shift. Its one-dimensional metric derivative is

\[
f'(t)
=1+\chi'(t)\log\frac{\kappa}{\gamma}.
\tag{19}
\]

For any `eta>0`, choosing

\[
T>\frac{C|\log(\kappa/\gamma)|}{\eta}
\]

makes

\[
|f'(t)-1|<\eta.
\tag{20}
\]

Thus the difference between the two natural gauges may be **diluted along the infinite cusp**. Equation (7) rules out simultaneous boundary isometries, but it does not give a positive lower bound on the extra bilipschitz cost after the boundary gauges are synchronized.

This distinction matters for PF-114. A nonsummable sequence of local logarithmic gauge mismatches does not automatically sum into a global metric or operator obstruction when each mismatch lives in an infinite cusp where its transition can be moved outward.

## 5. Consequence for the accepted relative-operator clue

PF-119 reduced the missing local comparison to the one-parameter quadrilateral `Q(a)` and showed that the **relative placement of the two normalized half-pant cusp charts** has summable shift-clone defect. PF-120 now adds a different constraint inside each `Q(a)`:

\[
\boxed{
\text{the two asymptotic rays of one cusp must use one common Busemann gauge.}
}
\tag{21}
\]

The natural endpoint-preserving isometries violate (21) by a mismatch

\[
M_n\sim\frac1{p_n}.
\]

Therefore the next positive construction must not try to preserve all canonical sidewise isometries simultaneously. It must choose a synchronized cusp gauge, interpolate at least one ray away from its endpoint-preserving isometry, prescribe the finite-cuff map, and then control the **interior** metric tensor/Jacobian.

At the same time, Section 4 shows that the reciprocal-prime mismatch is not itself the sought nonlocal amplification mechanism. It can be absorbed at the boundary with arbitrarily small additional local stretch. Any genuine negative answer to the accepted clue still has to arise from the interior quadrilateral extension, coherent gluing across the doubled pants, or a later global/operator obstruction.

## 6. Prior-art and novelty audit

No novelty is claimed for the elementary fact that two asymptotic geodesic rays become arbitrarily close in a hyperbolic cusp, or for the general principle that a bilipschitz map cannot send such vanishing transverse distances to a positive limiting distance. Equation (13) is just the exact upper-half-plane distance formula written in Busemann coordinates.

The closest audited comparison literature remains the same family already attached to the accepted clue:

- Y. Minsky, *Bounded geometry for Kleinian groups*, Invent. Math. 146 (2001), Lemmas 8.2--8.3, constructs coarse bilipschitz comparisons of pants/right-angled hexagons under bounded additive boundary-length changes, including cusp limits, but does not prescribe two independently shifted asymptotic rays or give the project-specific mismatch (8)--(10).
- M. Vuorinen and G. Wang, *Hyperbolic Lambert quadrilaterals and quasiconformal mappings*, Ann. Acad. Sci. Fenn. Math. 38 (2013), 433--453, studies metric inequalities and quasiconformal images of hyperbolic Lambert quadrilaterals. It does not supply the boundary-synchronized `Q(a)->Q(a')` homeomorphism required here.
- The explicit near-isometric pants constructions of Wu--Zhang cited in the accepted clue prescribe compatible boundary data precisely so that local pieces glue; their hypotheses do not cover this one-cusp/two-unbounded-cuff degeneration.

Directed searches for Lambert-quadrilateral maps with independently prescribed cusp-ray Busemann translations and for the exact `tanh/sech` mismatch (6) located no theorem that would turn the project-specific application into a previously established result. The durable content here is not a new general cusp theorem. It is the exact identification

\[
\boxed{
\text{prime/shift-clone natural side-gauge mismatch}
=
\log\frac{\sinh a_n^+}{\sinh a_n}
\sim\frac1{p_n},
}
\tag{22}
\]

together with the proof that this mismatch is **forbidden as simultaneous bilipschitz boundary data but arbitrarily dilutable after synchronization**.

## 7. Audit / falsification core

The result has six independent checks:

1. verify the PF-119 normalized quadrilateral radii `r=tanh a`, `s=sech a` and the two vertical sides meeting at the same ideal cusp;
2. compute the exact source distance (11) and the limiting target distance (13); any finite upper Lipschitz bound must force equal asymptotic Busemann scales;
3. verify the endpoint-preserving side isometries have scales `lambda=r'/r` and `kappa=s'/s`, and reduce their ratio exactly to `sinh(a')/sinh(a)`;
4. insert the exact collar identity and PF-114 shift factor to derive (16)--(17), hence the reciprocal-prime mismatch (9) and divergence (10);
5. check that the interpolation (18)--(20) really has arbitrarily small one-dimensional excess stretch when its transition length is allowed to grow;
6. do **not** promote the boundary interpolation to an interior bilipschitz homeomorphism, global strong metric equivalence, compact relative resolvent, or spectral equivalence.

Failure of steps 1--4 falsifies the substantive boundary claim. Step 5 protects against the opposite overinterpretation: the nonsummable gauge mismatch is not by itself an operator obstruction.