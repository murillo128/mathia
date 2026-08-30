# WP-042 — a local Schwarzian sextic detects two-point Schiffer indefiniteness

**Status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + CLASSICAL-FRAMEWORK`. For a real `C^5` locally injective endpoint map `V`, the first nontrivial near-diagonal `2 x 2` Gram determinant of the Schiffer kernel is controlled by one explicit differential expression in the Schwarzian,
\[
\mathcal J_V
=
4S(V)S(V)''
-5S(V)'^2
-4S(V)^3.
\]
If `S(V)(x)>0` but `\mathcal J_V(x)<0`, the raw Schiffer kernel is already indefinite on every sufficiently small nonzero pair around `x`. For the exact cotangent map of WP-014,
\[
V(x)=\pi\cot(\pi/x),
\]
one has `S(V)=2\pi^2/x^4` and `\mathcal J_V=-32\pi^6/x^{12}<0`. Thus the WP-014 failure has a purely local projective-differential certificate; its global Mittag--Leffler argument is needed only for the stronger statement that **every** distinct tail pair fails. The criterion is a reusable falsifier for Schiffer-type Weil candidates, not a positive Weil mechanism.

## 1. Object and local question

For a real `C^5` map `V` with `V'(x)\ne0`, consider the Schiffer-type kernel already used in WP-014,
\[
K_V(x,y)
=
\frac{V'(x)V'(y)}{(V(y)-V(x))^2}
-\frac1{(y-x)^2},
\qquad x\ne y,
\tag{1}
\]
with its continuous diagonal extension.

A positive-semidefinite kernel must make every two-point matrix
\[
M_V(x,h)
=
\begin{pmatrix}
K_V(x,x) & K_V(x,x+h)\\
K_V(x+h,x) & K_V(x+h,x+h)
\end{pmatrix}
\tag{2}
\]
positive semidefinite. Therefore a local sign formula for
\[
D_V(x,h):=\det M_V(x,h)
\tag{3}
\]
is already a decisive obstruction: if `D_V(x,h)<0` for arbitrarily small nonzero `h`, no global completion can honestly claim that the **raw** kernel (1) itself was the missing positive geometric form.

Write
\[
S=S(V)
=
\frac{V'''}{V'}
-\frac32\left(\frac{V''}{V'}\right)^2
\tag{4}
\]
for the Schwarzian derivative in the chosen source coordinate.

## 2. Exact near-diagonal expansion

Taylor expansion of (1) at `y=x+h` gives
\[
\boxed{
K_V(x,x+h)
=
\frac{S}{6}
+\frac{S'}{12}h
+
\left(
\frac{S''}{40}
+\frac{S^2}{60}
\right)h^2
+o(h^2).
}
\tag{5}
\]

For audit, before rewriting in Schwarzian notation the three coefficients are
\[
\frac{2V'V'''-3(V'')^2}{12(V')^2},
\tag{6}
\]
\[
\frac{(V')^2V''''-4V'V''V'''+3(V'')^3}
{12(V')^3},
\tag{7}
\]
and
\[
\frac{
6(V')^3V'''''
-30(V')^2V''V''''
-20(V')^2(V''')^2
+90V'(V'')^2V'''
-45(V'')^4
}
{240(V')^4}.
\tag{8}
\]
Equations (6)--(8) reduce respectively to
\[
\frac S6,\qquad
\frac{S'}{12},\qquad
\frac{S''}{40}+\frac{S^2}{60}.
\]

In particular,
\[
K_V(x,x)=\frac{S(x)}6,
\tag{9}
\]
while
\[
K_V(x+h,x+h)
=
\frac S6+\frac{S'}6h+\frac{S''}{12}h^2+o(h^2).
\tag{10}
\]

Substituting (5), (9), and (10) into (3) cancels the constant and linear terms. The first possible nonzero term is
\[
\boxed{
D_V(x,h)
=
\frac{h^2}{720}
\left(
4SS''-5(S')^2-4S^3
\right)
+o(h^2).
}
\tag{11}
\]

Define
\[
\boxed{
\mathcal J_V(x)
:=
4S(V)(x)S(V)''(x)
-5S(V)'(x)^2
-4S(V)(x)^3.
}
\tag{12}
\]

Then:

- if `S(x)<0`, PSD already fails on the diagonal by (9);
- if `S(x)>0` and `\mathcal J_V(x)<0`, equation (11) gives `D_V(x,h)<0` for every sufficiently small nonzero `h`;
- if `S(x)>0` and `\mathcal J_V(x)>0`, only this infinitesimal two-point test is passed; higher minors and finite separations remain completely open;
- if `\mathcal J_V(x)=0`, the order-`h^2` test is inconclusive and higher expansion is required.

Thus `(S,\mathcal J)` gives a finite local rejection test, not a sufficient positivity criterion.

## 3. The obstruction is projectively natural at the two-point level

The expression (12) is not invariant under an arbitrary nonlinear reparametrization of the source. That boundary matters: a freely chosen coordinate could manufacture a different Schwarzian profile.

It does, however, have exactly the covariance forced by the Schiffer kernel under projective coordinates.

For a target Möbius transformation `A`,
\[
K_{A\circ V}(x,y)=K_V(x,y).
\tag{13}
\]
For a source Möbius transformation `\phi`,
\[
K_{V\circ\phi}(u,v)
=
\phi'(u)\phi'(v)
K_V(\phi(u),\phi(v)).
\tag{14}
\]
Consequently the two-point determinant transforms as
\[
D_{V\circ\phi}(u,h)
=
\phi'(u)^2\phi'(u+h)^2
D_V\!\left(\phi(u),\,\phi(u+h)-\phi(u)\right).
\tag{15}
\]
Comparing the `h^2` coefficients in (11) yields
\[
\boxed{
\mathcal J_{V\circ\phi}(u)
=
\phi'(u)^6
\mathcal J_V(\phi(u)).
}
\tag{16}
\]

So `\mathcal J_V\,dx^6` is a weight-six projective density under source Möbius changes, and the **sign** of `\mathcal J_V` is preserved on the real line. It is also unchanged by target Möbius postcomposition. This is the exact level of canonicality available here: projective-coordinate naturality, not invariance under arbitrary gauges.

For the Mathia application this is sufficient because WP-014's endpoint coordinate `x` is not introduced to repair a sign; it is the intrinsic tail parameter in the exact map being tested.

## 4. Exact specialization to the WP-014 cotangent map

Take
\[
V(x)=\pi\cot\frac{\pi}{x},
\qquad x>2.
\tag{17}
\]
The Schwarzian chain rule
\[
S(f\circ g)
=
(Sf\circ g)(g')^2+Sg
\tag{18}
\]
gives an immediate evaluation. Multiplication by `\pi` is Möbius, `S(\cot z)=2`, and `g(x)=\pi/x` is Möbius, hence `Sg=0`. Therefore
\[
\boxed{
S(V)(x)=\frac{2\pi^2}{x^4}.
}
\tag{19}
\]
Equation (9) becomes
\[
K_V(x,x)=\frac{\pi^2}{3x^4},
\]
exactly the diagonal value in WP-014.

Differentiate (19):
\[
S'=-\frac{8\pi^2}{x^5},
\qquad
S''=\frac{40\pi^2}{x^6}.
\tag{20}
\]
The derivative part of (12) cancels identically,
\[
4SS''-5(S')^2=0,
\tag{21}
\]
leaving
\[
\boxed{
\mathcal J_V(x)
=
-4S^3
=
-\frac{32\pi^6}{x^{12}}
<0.
}
\tag{22}
\]
Hence
\[
\boxed{
D_V(x,h)
=
-\frac{2\pi^6}{45x^{12}}h^2
+o(h^2)
<0
}
\tag{23}
\]
for every sufficiently small nonzero `h`.

This recovers the **local** core of WP-014 without using the pole lattice of `\csc^2`, Mittag--Leffler summation, or a global trigonometric inequality. WP-014 remains strictly stronger: it proves `D_V(x,y-x)<0` for every distinct `x,y>2`, not merely sufficiently close pairs.

The cancellation (21) is also structurally informative. For a positive scale law `S=Cx^{-4}`,
\[
4SS''-5(S')^2=0
\]
identically, so the two-point sign is forced entirely by the nonlinear `-4S^3` term.

## 5. Controls and falsification boundaries

### Möbius control

If `V` itself is Möbius, then `S=0` and the cross-ratio identity gives
\[
K_V\equiv0.
\]
Thus `\mathcal J_V=0`, as required. The criterion does not falsely manufacture an obstruction in the projectively trivial case.

### Constant-positive-Schwarzian control

If `S` is a positive constant on an interval, then
\[
\mathcal J_V=-4S^3<0.
\]
Thus positive diagonal Schwarzian is not enough for kernel PSD: even the simplest nonzero positive projective curvature already fails the local two-point test. This confirms that (12) is not extracting arithmetic specificity from the cotangent example.

### Positive-`\mathcal J` control

The sign is not universally negative. For the elementary power map
\[
V(x)=x^\alpha,\qquad x>0,\quad 0<\alpha<1,
\]
one has
\[
S(V)(x)=\frac{1-\alpha^2}{2x^2}
=:\frac{C}{x^2},
\qquad 0<C<\frac12.
\]
Then
\[
\mathcal J_V(x)
=
\frac{4C^2(1-C)}{x^6}
>0.
\]
Hence nearby `2 x 2` determinants are positive for this control. Together with the Möbius zero case and the cotangent negative case, this shows that `\mathcal J` is a genuine local discriminator rather than an expression whose sign is fixed algebraically.

### Coordinate boundary

Under arbitrary `C^5` source reparametrization, a new Schwarzian term `S(\phi)` enters the chain rule. Therefore the sign test must be applied in a coordinate forced by the candidate geometry, or at most compared across projectively equivalent coordinates. A route that first chooses a nonlinear coordinate because it makes `\mathcal J\ge0` has imported a gauge choice and fails the line's canonicality requirement.

### Scope boundary

A nonnegative `\mathcal J` everywhere would not establish positive definiteness. It controls only the first nontrivial near-diagonal `2 x 2` minor. A viable Schiffer candidate must still survive:

1. points where `S=0` or `\mathcal J=0`;
2. higher-order near-diagonal terms;
3. finite-separation `2 x 2` minors;
4. all higher Gram minors;
5. the finite-prime/archimedean matching and independent global sign theorem required by this research line.

## 6. Prior-art and novelty audit

The kernel (1), its relation to Grunsky--Schiffer theory, and the diagonal identity `K_V(x,x)=S(V)(x)/6` are classical projective-function-theory structure; WP-014 already places the candidate inside that prior-art boundary. Higher coefficients in near-diagonal expansions of univalent-function kernels are likewise naturally organized by higher Schwarzian/Aharonov-type invariants. The present result does **not** claim novelty for Schwarzian calculus, Grunsky theory, or the existence of such higher differential invariants.

The durable derived content is narrower:

\[
\boxed{
D_V(x,h)
=
\frac{\mathcal J_V(x)}{720}h^2+o(h^2)
}
\]
with the explicit weight-six expression (12), its projective covariance (16), and the exact specialization (19)--(23) to Mathia's cotangent endpoint map.

A targeted prior-art search by the differential combination in (12), two-point Schiffer/Grunsky determinants, higher Schwarzians, and Aharonov invariants did not identify a source that would justify promoting this to a general named theorem. Absence from that search is not evidence of novelty. The correct classification is therefore **exact derived specialization inside a classical framework**.

This also prevents a false interpretation of the result as an RH mechanism: the criterion is local and applies to non-arithmetic maps. Its value for `weil_positivity` is as a canonical early **falsifier**.

## 7. Consequence for the Weil-positivity search

WP-014 established that the strongest existing exact Prime-Flute Schiffer coupling is globally indefinite on every distinct real tail pair. WP-042 explains why failure is already encoded infinitesimally in the endpoint map:
\[
\boxed{
S>0,\quad \mathcal J<0
\quad\Longrightarrow\quad
\text{local two-point Schiffer indefiniteness}.
}
\tag{24}
\]

This gives the research line a reusable pre-screen for any future Mathia-native proposal that tries to obtain Weil positivity from a Schiffer/Grunsky endpoint kernel. Before doing global spectral, arithmetic, or archimedean work, compute `S` and `\mathcal J` in the canonical projective coordinate. A negative diagonal Schwarzian or a negative `\mathcal J` kills the raw-kernel positivity route locally.

The finding does **not** move the line closer to a positive global Weil form by itself. It narrows the search by showing that the finite Taylor certificate suggested by formalization is not an accidental proof trick: it is the manifestation of a projectively covariant local determinant obstruction. Any surviving Schiffer-based route must alter the object before positivity is invoked -- for example by a genuinely different compression, square, quotient, boundary response, cohomological pairing, or nonlocal assembly -- and must then independently derive the finite-prime and archimedean/global terms rather than inheriting them from the already-indefinite raw kernel.

## 8. Audit core

The result can be falsified without any zeta or zero computation:

1. expand (1) through order `h^2` and verify (5)--(8);
2. expand `S(x+h)/6` and compute the determinant to verify (11);
3. verify Möbius identities (13)--(14), then infer the weight-six law (16);
4. use the Schwarzian chain rule to verify (19);
5. differentiate (19) and check the exact cancellation (21) and sign (22);
6. compare the coefficient (23) with the near-diagonal expansion of WP-014's exact closed form.

Any coefficient mismatch in these finite checks invalidates the finding. No analytic continuation, RH assumption, zero data, or regularization enters the argument.
