# AF-178 — Simple-Blaschke local condition number is exactly reciprocal double separation

**Status:** `EXACT-DERIVED`, `LITERATURE-CONTEXT`, `CONDITIONING-CLASSIFICATION`, `GAUGE-QUOTIENT`, `CHEBYSHEV-ALTERNATION`, `NO-NOVELTY-CLAIM`

## Claim

AF-175 and AF-177 left a factor-two gap in the local inverse condition number for recovering a simple finite-Blaschke zero divisor from the phase-quotiented `H^\infty` function. That gap is exact and can be closed.

Let

\[
B(z)=\eta\prod_{j=1}^n\phi_{a_j}(z),
\qquad
\phi_a(z)=\frac{z-a}{1-\overline a z},
\tag{1}
\]

be a degree-`n` finite Blaschke product with pairwise distinct zeros `a_1,\dots,a_n\in\mathbb D`. Set

\[
\delta_j(B)
=(1-|a_j|^2)|B'(a_j)|
=\prod_{k\ne j}\rho(a_j,a_k),
\qquad
\delta(B)=\min_j\delta_j(B)>0,
\tag{2}
\]

with

\[
\rho(z,w)=\left|\frac{z-w}{1-\overline w z}\right|.
\tag{3}
\]

For another degree-`n` finite Blaschke product `C` with zero divisor `\{b_1,\dots,b_n\}`, use the same metrics as AF-173--AF-177:

\[
\Delta(B,C)
=\inf_{|\lambda|=1}\|B-\lambda C\|_{H^\infty},
\tag{4}
\]

and

\[
d_{\mathrm{div}}^\rho(B,C)
=\min_{\sigma\in S_n}\max_j\rho(a_j,b_{\sigma(j)}).
\tag{5}
\]

Define

\[
\kappa_{\mathrm{loc}}(B)
=
\limsup_{\substack{C\to B\\ \deg C=n}}
\frac{d_{\mathrm{div}}^\rho(B,C)}{\Delta(B,C)}.
\tag{6}
\]

Then

\[
\boxed{
\kappa_{\mathrm{loc}}(B)=\frac{1}{2\delta(B)}.
}
\tag{7}
\]

Thus the interpolation/separation constant is not merely the correct conditioning scale up to a universal factor, as AF-177 established. For the fixed quotient `H^\infty` output metric and pseudohyperbolic divisor metric, `1/(2\delta(B))` is the **exact first-order inverse condition number** throughout the simple finite-Blaschke stratum.

The proof is a tangent-space extremal argument. A Frostman postcomposition gives the lower-bound direction already found in AF-177. The new step is a Chebyshev-style alternation/zero-count argument showing that no tangent perturbation can move any zero more cheaply in the quotient `H^\infty` norm.

## Derivation

### Tangent coordinates and the quotient output norm

Let `B_s` be a `C^1` path of degree-`n` finite Blaschke products with `B_0=B`, simple labeled zeros `a_j(s)`, and

\[
f=\left.\frac{d}{ds}B_s\right|_{s=0}.
\tag{8}
\]

Since `|B_s|=1` on `\mathbb T`, differentiation gives

\[
\operatorname{Re}(f\overline B)=0
\qquad (|z|=1).
\tag{9}
\]

Hence

\[
q(z)=-i\frac{f(z)}{B(z)}
\tag{10}
\]

is real-valued on `\mathbb T`. Infinitesimal output phase is exactly the additive-constant direction in `q`, so the tangent norm induced by `(4)` is

\[
M_B(f)
:=\inf_{c\in\mathbb R}\|f-i cB\|_{H^\infty}
=\inf_{c\in\mathbb R}\|q-c\|_{L^\infty(\mathbb T)}.
\tag{11}
\]

Differentiating `B_s(a_j(s))=0` gives

\[
f(a_j)=-B'(a_j)\dot a_j,
\tag{12}
\]

and therefore the pseudohyperbolic speed of the `j`th zero is

\[
v_j
:=\frac{|\dot a_j|}{1-|a_j|^2}
=\frac{|f(a_j)|}{\delta_j(B)}.
\tag{13}
\]

The tangent norm induced by the divisor bottleneck metric is consequently

\[
V_B(f)=\max_j v_j.
\tag{14}
\]

The problem is now finite-dimensional: determine the sharp constant in `V_B(f)\le K M_B(f)`.

### A Frostman tangent equioscillates at the full degree

Fix an index `i` and write

\[
w=f(a_i).
\tag{15}
\]

Consider the tangent

\[
f_w(z)=w-\overline w\,B(z)^2.
\tag{16}
\]

It is an admissible finite-Blaschke tangent: if

\[
F_t(u)=\frac{u-t}{1-\overline t\,u},
\tag{17}
\]

then differentiating `F_{-sw}\circ B` at `s=0` gives `(16)`. In particular

\[
f_w(a_j)=w
\qquad\text{for every }j.
\tag{18}
\]

On the unit circle write

\[
B(e^{i\theta})=e^{i\beta(\theta)},
\qquad
w=|w|e^{i\gamma}.
\tag{19}
\]

Its real boundary quotient is

\[
q_w
=-i\frac{f_w}{B}
=-i\left(\frac{w}{B}-\overline w B\right)
=2|w|\sin(\gamma-\beta).
\tag{20}
\]

A degree-`n` finite Blaschke product restricts to an orientation-preserving `n`-fold covering of `\mathbb T`; explicitly,

\[
\beta'(\theta)
=\sum_{j=1}^n
\frac{1-|a_j|^2}{|e^{i\theta}-a_j|^2}>0.
\tag{21}
\]

As `\theta` traverses the circle, `\beta` increases by `2\pi n`. Therefore `q_w` has `2n` cyclically ordered extrema whose values alternate exactly between

\[
+2|w|,
\quad
-2|w|.
\tag{22}
\]

This is the extremal pattern that forces the sharp tangent inequality.

### Alternation rules out every cheaper tangent with the same zero motion

Take any `c\in\mathbb R` and put

\[
q'=q-c.
\tag{23}
\]

Suppose, for contradiction, that

\[
\|q'\|_\infty<2|w|.
\tag{24}
\]

At each point where `q_w=+2|w|`, the difference

\[
d=q'-q_w
\tag{25}
\]

is strictly negative; at each point where `q_w=-2|w|`, it is strictly positive. The signs therefore alternate at the `2n` cyclically ordered extremal points. By continuity, `d` has at least one zero in every intervening arc, hence at least `2n` distinct zeros on `\mathbb T`.

That many zeros are impossible unless `d\equiv0`. To see the degree bound directly, differentiate the finite-Blaschke factorization. Up to a real constant coming from output phase,

\[
q(z)
=-i\sum_{j=1}^n
\left(
-\frac{\dot a_j}{z-a_j}
+\frac{\overline{\dot a_j}\,z}{1-\overline{a_j}z}
\right)
+\text{constant}.
\tag{26}
\]

The same representation holds for `q_w`. Because `f(a_i)=f_w(a_i)=w`, equation `(12)` says that the `i`th zero velocity is identical for the two tangents. Hence both the pole at `a_i` and its reflected pole cancel in `d`. After putting the remaining terms over the common denominator

\[
D_i(z)=\prod_{j\ne i}(z-a_j)(1-\overline{a_j}z),
\tag{27}
\]

we obtain

\[
d(z)=\frac{N_i(z)}{D_i(z)},
\qquad
\deg N_i\le 2n-2.
\tag{28}
\]

The denominator has no zeros on `\mathbb T`. A nonzero numerator of degree at most `2n-2` cannot have `2n` distinct unit-circle zeros. Thus the alternating-sign conclusion forces `d\equiv0`; but then `q'=q_w` and `\|q'\|_\infty=2|w|`, contradicting `(24)`.

Therefore, for every real `c`,

\[
\|q-c\|_\infty\ge 2|f(a_i)|.
\tag{29}
\]

Since `i` was arbitrary,

\[
\boxed{
M_B(f)\ge 2\max_i|f(a_i)|.
}
\tag{30}
\]

Using `(13)`,

\[
M_B(f)
\ge 2\max_i\delta_i(B)v_i
\ge 2\delta(B)V_B(f),
\tag{31}
\]

so every tangent satisfies

\[
V_B(f)\le\frac{1}{2\delta(B)}M_B(f).
\tag{32}
\]

### Frostman postcomposition attains the bound

For the tangent `f_w` in `(16)`, equation `(18)` gives

\[
V_B(f_w)
=\max_j\frac{|w|}{\delta_j(B)}
=\frac{|w|}{\delta(B)}.
\tag{33}
\]

Equation `(20)` has range exactly `[-2|w|,2|w|]`, so its best constant approximation is `0` and

\[
M_B(f_w)=2|w|.
\tag{34}
\]

Hence

\[
\frac{V_B(f_w)}{M_B(f_w)}
=\frac{1}{2\delta(B)}.
\tag{35}
\]

The differential inverse norm is therefore exactly `1/(2\delta(B))`.

### The tangent identity equals the metric local condition number

It remains to connect the differential calculation to the limsup in `(6)`. Simplicity of the zeros provides disjoint neighborhoods in which nearby degree-`n` finite Blaschke products have unique labeled zeros. These zero coordinates, together with output phase, give a finite-dimensional `C^1` local chart. Because all poles remain uniformly outside `\mathbb T`, the map from zero coordinates to the corresponding rational inner function is `C^1` in the `H^\infty` norm.

For a local path with tangent `f`, the source metric has the expansion

\[
d_{\mathrm{div}}^\rho(B,B_s)
=|s|V_B(f)+o(|s|),
\tag{36}
\]

while the quotient output metric has

\[
\Delta(B,B_s)
=|s|M_B(f)+o(|s|).
\tag{37}
\]

For `(37)`, one inequality follows by choosing `\lambda_s=e^{-ics}` for any fixed `c`. Conversely, any asymptotically minimizing phases must satisfy `\lambda_s\to1`; once `\Delta=O(|s|)`, also `|1-\lambda_s|=O(|s|)`. Passing to a subsequence writes

\[
\lambda_s=1+i c s+o(|s|)
\tag{38}
\]

for some bounded real first-order phase `c`, which yields the lower tangent quotient `(11)`.

The same argument applies to arbitrary sequences `C_k\to B`: normalize their local zero-coordinate displacements, pass to a convergent tangent direction in the finite-dimensional unit sphere, and use the uniform first-order expansions `(36)`--`(37)`. Equation `(32)` then gives

\[
\limsup_{k\to\infty}
\frac{d_{\mathrm{div}}^\rho(B,C_k)}{\Delta(B,C_k)}
\le\frac{1}{2\delta(B)}.
\tag{39}
\]

AF-177's exact Frostman family gives the reverse limsup. This proves `(7)`.

## Prior art and novelty assessment

No theorem-level novelty claim is made. The proof is self-contained, but its extremal mechanism lies squarely in classical rational Chebyshev/equioscillation territory.

- Peter Borwein, Tamás Erdélyi, and John Zhang, **“Chebyshev Polynomials and Markov--Bernstein Type Inequalities for Rational Spaces,”** *Journal of the London Mathematical Society* 50(3) (1994), 501--519, DOI `10.1112/jlms/50.3.501`, develops Chebyshev systems of rational functions with prescribed poles and derives sharp Bernstein-type inequalities through equioscillation.
- Xin Li, R. N. Mohapatra, and R. S. Rodriguez, **“Bernstein-Type Inequalities for Rational Functions with Prescribed Poles,”** *Journal of the London Mathematical Society* 51(3) (1995), 523--531, DOI `10.1112/jlms/51.3.523`, establishes sharp Chebyshev-norm derivative inequalities for rational functions with prescribed poles on the unit circle.
- Christer Glader and Göran Högnäs, **“An Equioscillation Characterization of Finite Blaschke Products,”** *Complex Variables, Theory and Application* 42(2) (2000), 107--118, DOI `10.1080/17476930008815276`, characterizes finite Blaschke products through maximal equioscillation order.
- AF-175 supplies the previous one-sided recovery modulus, and AF-177 supplies the universal Frostman lower witness.

A targeted search for finite-Blaschke zero perturbation, `H^\infty` quotient distance, pseudohyperbolic divisor conditioning, and equioscillation did not locate the exact metric identity `(7)` in this formulation. That absence is not evidence of novelty. The appropriate classification is a line-specific exact derivation placed in established rational approximation and Blaschke-product extremal context.

## Boundary conditions and falsification checks

- The reference divisor must be simple. When zeros collide, `\delta(B)=0`, the simple-zero chart breaks down, and AF-174's Hölder-type regime is the relevant boundary behavior.
- Equation `(7)` is a **local first-order** condition number. It does not imply a global Lipschitz inverse with constant `1/(2\delta(B))` on a finite neighborhood.
- The numerical factor `2` belongs to the exact metric pair `(4)`--`(5)`, especially the quotient `H^\infty` normalization. Other source or output metrics need their own tangent audit.
- Quotienting output phase is essential to the stated condition number. A phase-fixed norm contains an additional gauge direction and need not have the same extremal constant.
- The zero-count argument uses the full finite-Blaschke tangent class. Restricting the admissible perturbations can improve conditioning; enlarging the source category beyond same-degree finite Blaschke products can invalidate the chart entirely.
- The result does not say that the Frostman direction is the unique extremizer. It proves that its ratio is globally sharp in tangent space.
- No arithmetic or RH conclusion follows from `(7)`. Any arithmetic transfer must identify an intrinsic analogue of `\delta(B)`, the correct retained quotient metric, and a concrete matched control at the same information layer.

## Consequences for the research line

AF-177's factor-two enclosure can now be replaced by an exact local classification. The simple finite-Blaschke example exhibits all three ingredients that a useful Arithmetic Fidelity conditioning theorem should expose: the retained quotient is fixed first, an intrinsic source regularity modulus `\delta(B)` is identified, and an explicit canonical perturbation attains the inverse condition number.

The sharper lesson is that a recovery theorem should not stop once it proves continuity or even a one-sided Lipschitz bound. The tangent fiber can contain an extremal direction whose alternation structure fixes the optimal constant. Here that direction is supplied by postcomposition, while the impossibility of a cheaper inverse is certified by a degree loss after one zero-motion constraint is fixed. This converts the earlier heuristic that separation controls conditioning into an exact statement for a complete nontrivial compression model.