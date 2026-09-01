# AF-043 — Closed-secant transversality classifies linear compression fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `STRUCTURAL-CLASSIFICATION`, `NEGATIVE/OBSTRUCTION`

## Claim

Let `S\subset\mathbb R^n` contain at least two points. Define its oriented unit-secant set

\[
\operatorname{Sec}(S)
=
\left\{
\frac{x-y}{\|x-y\|}:x,y\in S,\ x\neq y
\right\}
\subset S^{n-1}
\]

and its **closed secant carrier**

\[
\widehat{\operatorname{Sec}}(S)
=
\overline{\operatorname{Sec}(S)}
\subset S^{n-1}.
\]

For a linear map

\[
B:\mathbb R^n\to\mathbb R^q,
\]

define the chord-fidelity modulus on `S` by

\[
\kappa_S(B)
=
\inf_{x\neq y\in S}
\frac{\|B(x-y)\|}{\|x-y\|}.
\]

Then:

1. **The closed secant carrier is the exact stable-fidelity object.**
   \[
   \boxed{
   \kappa_S(B)
   =
   \min_{u\in\widehat{\operatorname{Sec}}(S)}\|Bu\|.
   }
   \]
   Consequently
   \[
   \boxed{
   B|_S\text{ is injective}
   \iff
   \operatorname{Sec}(S)\cap\ker B=\varnothing,
   }
   \]
   whereas
   \[
   \boxed{
   \kappa_S(B)>0
   \iff
   \widehat{\operatorname{Sec}}(S)\cap\ker B=\varnothing.
   }
   \]
   Exact fidelity therefore audits actual secants; stable fidelity audits **limit secants as well**.

2. **Linear compression stability is a nonlinear range–kernel transversality problem.** Put `N=\ker B` and define
   \[
   \tau_S(N)
   =
   \min_{u\in\widehat{\operatorname{Sec}}(S)}
   \operatorname{dist}(u,N).
   \]
   If `B\neq0` and `\gamma(B)` is its smallest nonzero singular value, then
   \[
   \boxed{
   \gamma(B)\,\tau_S(N)
   \le
   \kappa_S(B)
   \le
   \|B\|\,\tau_S(N).
   }
   \]
   For the orthogonal quotient `Q_N=P_{N^\perp}` the bounds are exact:
   \[
   \boxed{
   \kappa_S(Q_N)=\tau_S(N).
   }
   \]

3. **For compact `C^1` embedded manifolds, the closed secant carrier splits into the two gates isolated in AF-042.** If `S\subset\mathbb R^n` is a compact `C^1` embedded manifold, with or without boundary, and
   \[
   \operatorname{Tan}_1(S)
   =
   \{v\in T_xS:x\in S,\ \|v\|=1\},
   \]
   then
   \[
   \boxed{
   \widehat{\operatorname{Sec}}(S)
   =
   \operatorname{Sec}(S)
   \cup
   \operatorname{Tan}_1(S).
   }
   \]
   Hence
   \[
   \boxed{
   \kappa_S(B)>0
   \iff
   \begin{cases}
   B|_S\text{ is injective},\\
   T_xS\cap\ker B=\{0\}\quad\forall x\in S.
   \end{cases}}
   \]
   On compact smooth carriers, the apparently separate global-collision and tangent-rank tests are exactly the two components of one closed-secant avoidance condition.

4. **AF-041 is the linear-carrier specialization.** If `S=M` is a nonzero linear subspace, then
   \[
   \operatorname{Sec}(M)=M\cap S^{n-1},
   \]
   so `\tau_S(N)` is precisely the range–kernel angle/transversality modulus of AF-041. The closed-secant construction is therefore the nonlinear extension of that Hilbert-space gate.

5. **For a bi-Lipschitz upstream representation, all additional linear-compression loss is concentrated in the secant modulus.** Let `(X,d)` be a metric space and let `A:X\to\mathbb R^n` satisfy
   \[
   a(A)
   =
   \inf_{x\neq y}
   \frac{\|A(x)-A(y)\|}{d(x,y)}>0,
   \qquad
   L(A)
   =
   \sup_{x\neq y}
   \frac{\|A(x)-A(y)\|}{d(x,y)}<\infty.
   \]
   With `S=A(X)`,
   \[
   \boxed{
   a(A)\,\kappa_S(B)
   \le
   \beta(B\circ A)
   \le
   L(A)\,\kappa_S(B),
   }
   \]
   where
   \[
   \beta(B\circ A)
   =
   \inf_{x\neq y}
   \frac{\|B(A(x)-A(y))\|}{d(x,y)}.
   \]
   Thus a stable upstream encoding followed by a linear compression is stably faithful exactly when its **closed secant carrier stays uniformly transverse to the downstream kernel**.

6. **Properness of the upstream embedding and uniform tangent transversality do not control noncompact long-range secants.** For irrational `\alpha`, define
   \[
   A_\alpha(t)
   =
   \bigl(t,\cos t,\sin t,\cos(\alpha t),\sin(\alpha t)\bigr)
   \in\mathbb R^5
   \]
   and let `B:\mathbb R^5\to\mathbb R^4` delete the first coordinate. Then `A_\alpha` is a proper bi-Lipschitz embedding, `B\circ A_\alpha` is injective, and the tangent of `A_\alpha(\mathbb R)` stays a fixed positive angle from `\ker B`. Nevertheless
   \[
   \boxed{
   \kappa_{A_\alpha(\mathbb R)}(B)=0.
   }
   \]
   Long secants approach the forgotten first-coordinate direction by Diophantine recurrence. Hence noncompact stable fidelity needs a **far-field secant condition** in addition to exact injectivity and every pointwise/local differential gate.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{linear compression is stably faithful on a nonlinear carrier exactly when the kernel misses the closed unit-secant carrier, not merely the actual secants or tangents.}
}
\]

This supplies the category-appropriate uniform secant condition requested by AF-042 and puts AF-041's range–kernel geometry and AF-042's global/tangent decomposition into one exact framework.

## Derivation

### The closed secant carrier computes the modulus exactly

For every distinct `x,y\in S`, put

\[
u_{x,y}
=
\frac{x-y}{\|x-y\|}.
\]

Linearity gives

\[
\frac{\|B(x-y)\|}{\|x-y\|}
=
\|Bu_{x,y}\|.
\]

Therefore

\[
\kappa_S(B)
=
\inf_{u\in\operatorname{Sec}(S)}\|Bu\|.
\]

The unit sphere is compact in finite dimension, so `\widehat{\operatorname{Sec}}(S)` is compact. Since `u\mapsto\|Bu\|` is continuous, passing to the closure does not change the infimum and the infimum is attained:

\[
\kappa_S(B)
=
\min_{u\in\widehat{\operatorname{Sec}}(S)}\|Bu\|.
\]

Now `B|_S` fails injectivity exactly when there are `x\neq y` with `B(x-y)=0`, equivalently when an **actual** unit secant lies in `\ker B`.

By contrast, `\kappa_S(B)=0` exactly when the minimum on the compact closed secant carrier vanishes, equivalently when some **actual or limiting** secant lies in `\ker B`.

Thus the distinction

\[
\operatorname{Sec}(S)
\quad\text{versus}\quad
\widehat{\operatorname{Sec}}(S)
\]

is the exact distinction between collision-free recovery and uniformly stable recovery.

### Quantitative transversality

Let `N=\ker B`. Since `B` vanishes on `N`,

\[
Bu=B P_{N^\perp}u.
\]

For finite-dimensional `B\neq0`, its restriction to `N^\perp` has smallest singular value `\gamma(B)>0`. Hence for every `u`,

\[
\gamma(B)\,\operatorname{dist}(u,N)
\le
\|Bu\|
\le
\|B\|\,\operatorname{dist}(u,N).
\]

Taking minima over `\widehat{\operatorname{Sec}}(S)` gives

\[
\gamma(B)\tau_S(N)
\le
\kappa_S(B)
\le
\|B\|\tau_S(N).
\]

If `B=Q_N=P_{N^\perp}`, then

\[
\|Q_Nu\|=\operatorname{dist}(u,N),
\]

so equality holds identically. This is the exact nonlinear counterpart of AF-041's quotient specialization.

## Compact-manifold secant closure

Assume now that `S\subset\mathbb R^n` is a compact `C^1` embedded manifold.

### Tangent directions are limiting secants

Let `x\in S` and let `v\in T_xS` be unit length. Choose a `C^1` curve `c` in `S` with

\[
c(0)=x,
\qquad
c'(0)=v.
\]

For a boundary point, choose the available one-sided curve; because the secant set is oriented and symmetric under `u\mapsto-u`, the opposite tangent direction is recovered as well. Then

\[
\frac{c(t)-c(0)}{\|c(t)-c(0)\|}
\longrightarrow
v
\]

as `t\to0` through the allowed side. Hence

\[
\operatorname{Tan}_1(S)
\subseteq
\widehat{\operatorname{Sec}}(S).
\]

### Every non-actual limit secant is tangent

Conversely, let

\[
u_j
=
\frac{x_j-y_j}{\|x_j-y_j\|}
\longrightarrow u,
\qquad
x_j\neq y_j.
\]

Compactness gives a subsequence with

\[
x_j\to x,
\qquad
y_j\to y.
\]

If `x\neq y`, then continuity immediately gives

\[
u=
\frac{x-y}{\|x-y\|}
\in\operatorname{Sec}(S).
\]

If `x=y`, use a local `C^1` graph chart centered at `x`. After an orthogonal change of coordinates, nearby points of `S` have the form

\[
(z,h(z)),
\]

where `Dh(0)=0`. For nearby `z,w`, the mean-value/first-order remainder estimate gives

\[
\|h(z)-h(w)\|
=
o(\|z-w\|)
\]

as `z,w\to0`. Therefore the normal component of `x_j-y_j` is negligible relative to its tangential component, and every limiting normalized chord lies in the unit tangent space `T_xS`.

Thus

\[
\widehat{\operatorname{Sec}}(S)
\subseteq
\operatorname{Sec}(S)
\cup
\operatorname{Tan}_1(S),
\]

which proves the equality.

The two compact gates now follow immediately. Kernel intersection with `\operatorname{Sec}(S)` is a global collision; kernel intersection with `\operatorname{Tan}_1(S)` is differential rank loss. Compactness guarantees that there is no third asymptotic component.

## Composition through a stable upstream encoding

Let `S=A(X)`. For `x\neq y`, factor

\[
\frac{\|B(A(x)-A(y))\|}{d(x,y)}
=
\frac{\|B(A(x)-A(y))\|}{\|A(x)-A(y)\|}
\cdot
\frac{\|A(x)-A(y)\|}{d(x,y)}.
\]

The first factor is at least `\kappa_S(B)` and the second at least `a(A)`, giving

\[
\beta(B\circ A)
\ge
 a(A)\kappa_S(B).
\]

Choose a sequence of pairs whose unit secants approach the minimizing direction for `\kappa_S(B)`. The second factor is at most `L(A)`, so

\[
\beta(B\circ A)
\le
L(A)\kappa_S(B).
\]

In particular, once the upstream representation is already bi-Lipschitz, the only new source of instability introduced by the linear downstream stage is its relative geometry against the image's closed secant carrier.

There is also a one-way obstruction that does not require `A` to be stably faithful:

\[
\beta(B\circ A)
\le
\|B\|\,\beta(A).
\]

Therefore bounded downstream linear processing cannot repair an upstream metric fidelity modulus that has already collapsed to zero.

## Proper noncompact control: local fidelity survives while far secants collapse

Fix irrational `\alpha` and set

\[
A_\alpha(t)
=
\bigl(t,\cos t,\sin t,\cos(\alpha t),\sin(\alpha t)\bigr).
\]

The first coordinate gives

\[
\|A_\alpha(t)-A_\alpha(s)\|
\ge
|t-s|.
\]

Also

\[
\|A_\alpha'(t)\|
=
\sqrt{2+\alpha^2},
\]

so

\[
\|A_\alpha(t)-A_\alpha(s)\|
\le
\sqrt{2+\alpha^2}\,|t-s|.
\]

Thus `A_\alpha` is bi-Lipschitz. It is also proper because the first coordinate is exactly `t`.

Let

\[
B(x_0,x_1,x_2,x_3,x_4)
=
(x_1,x_2,x_3,x_4),
\]

so

\[
\ker B=\operatorname{span}\{e_0\}.
\]

The downstream map is

\[
F_\alpha(t)
=
(B\circ A_\alpha)(t)
=
(\cos t,\sin t,\cos(\alpha t),\sin(\alpha t)).
\]

As in AF-042, irrationality implies that `F_\alpha` is injective. Moreover

\[
\|F_\alpha'(t)\|
=
\sqrt{1+\alpha^2}
\]

for every `t`. The normalized tangent of the upstream curve therefore stays a fixed distance

\[
\frac{\sqrt{1+\alpha^2}}{\sqrt{2+\alpha^2}}
>0
\]

from `\ker B`. There is no tangent collapse at any point and no exact global collision.

Nevertheless Dirichlet approximation supplies infinitely many integers `q\ge1` and `p` such that

\[
|q\alpha-p|<\frac1q.
\]

Put `t_q=2\pi q`. Then the first circle pair returns exactly, while

\[
\begin{aligned}
\|B(A_\alpha(t_q)-A_\alpha(0))\|
&=
|e^{2\pi i q\alpha}-1|\\
&=
|e^{2\pi i(q\alpha-p)}-1|\\
&\le
2\pi|q\alpha-p|\\
&<
\frac{2\pi}{q}.
\end{aligned}
\]

On the other hand

\[
\|A_\alpha(t_q)-A_\alpha(0)\|
\ge
|t_q|
=
2\pi q.
\]

Hence

\[
\frac{\|B(A_\alpha(t_q)-A_\alpha(0))\|}
{\|A_\alpha(t_q)-A_\alpha(0)\|}
<
\frac1{q^2}
\longrightarrow0.
\]

Equivalently, the normalized long secants converge to `e_0\in\ker B`:

\[
\frac{A_\alpha(t_q)-A_\alpha(0)}
{\|A_\alpha(t_q)-A_\alpha(0)\|}
\longrightarrow e_0.
\]

Therefore

\[
\widehat{\operatorname{Sec}}(A_\alpha(\mathbb R))
\cap
\ker B
\neq\varnothing,
\qquad
\kappa_{A_\alpha(\mathbb R)}(B)=0.
\]

This isolates a third noncompact failure mode that is absent from AF-042's compact classification:

\[
\text{actual secants}
\quad+
\text{infinitesimal tangent directions}
\quad+
\boxed{\text{asymptotic / far-field secant directions}}.
\]

The example also kills a tempting repair: requiring the **upstream** embedding to be proper does not suffice, because the downstream compression may discard precisely the coordinate that made the carrier proper.

## Prior art and novelty assessment

The secant geometry is classical. No novelty is claimed for Whitney-style secant/tangent avoidance, secant-based dimensionality reduction, or stable manifold embeddings.

- D. S. Broomhead and M. Kirby, **“A New Approach to Dimensionality Reduction: Theory and Algorithms,”** *SIAM Journal on Applied Mathematics* 60(6) (2000), 2114–2142, DOI `10.1137/S0036139998338583`. Role: explicit constructive-Whitney dimensionality reduction and the notion of a projection chosen to remain easy to invert; direct prior art for treating projection quality through secant geometry.
- D. S. Broomhead and M. J. Kirby, **“Dimensionality Reduction Using Secant-Based Projection Methods: The Induced Dynamics in Projected Systems,”** *Nonlinear Dynamics* 41 (2005), 47–67, DOI `10.1007/s11071-005-2792-1`. Role: direct unit-secant prior art; the method explicitly optimizes projections by their action on the set of unit secants of the data.
- Richard G. Baraniuk and Michael B. Wakin, **“Random Projections of Smooth Manifolds,”** *Foundations of Computational Mathematics* 9(1) (2009), 51–77, DOI `10.1007/s10208-007-9011-z`. Role: stable manifold-embedding prior art guaranteeing preservation of all pairwise Euclidean and geodesic distances under sufficiently large random projections.
- John M. Lee, ***Introduction to Smooth Manifolds***, 2nd ed., Graduate Texts in Mathematics 218, Springer (2012), DOI `10.1007/978-1-4419-9982-5`. Role: classical immersion/embedding and local manifold-chart machinery underlying the compact secant-to-tangent closure argument and AF-042.

The individual ingredients are therefore not new. The Arithmetic Fidelity contribution is the exact **common audit object** they expose for this program: raw secants encode exact collision fidelity; closed secants encode stable fidelity; compact `C^1` closed secants split into the global and tangent gates of AF-042; linear carriers recover AF-041's range–kernel angle; and noncompact carriers acquire asymptotic secant directions that neither exact injectivity nor local differential tests can see.

The novelty claim is intentionally limited to this structural unification and its use as a reusable stopping rule for Mathia compression chains, not to the underlying secant or projection mathematics.

## Boundary conditions and falsification controls

- The exact minimum formula uses finite-dimensional ambient space so the closed unit-secant carrier is compact. Infinite-dimensional analogues need an explicit compactness or closed-range/uniform-angle hypothesis; AF-041 already shows why naïve finite-dimensional compactness cannot be imported.
- `\kappa_S(B)` measures stability relative to **ambient Euclidean chord distance on the retained carrier**. It need not control an intrinsic geodesic metric unless the upstream representation supplies the corresponding metric comparison.
- Avoiding `\operatorname{Sec}(S)\cap\ker B` proves only exact injectivity. A kernel direction in the closure is enough to destroy every uniform inverse modulus without creating any collision.
- On noncompact carriers, tangent transversality is only local. Far-field secant directions must be audited separately; properness of an earlier stage is not inherited through an arbitrary compression.
- A different nonlinear downstream map need not be characterized by one fixed kernel. The appropriate analogue is the closed family of normalized pairwise difference directions after linearization only when that reduction is mathematically justified.
- A purported application to rational-prime structure must identify the actual carrier `S`, metric/discriminator being protected, and downstream null directions. Merely describing a representation as “marked,” “transverse,” or “nonlocal” does not establish closed-secant separation.

## Consequences for the research line

1. **AF-041 and AF-042 now share one exact geometry.** Range–kernel transversality is the linear-subspace case; global injectivity plus immersion is the compact-manifold case. Both ask whether a downstream kernel meets the relevant closed direction carrier.
2. **Noncompact/asymptotic research has a sharper gate.** The missing condition is not another local rank theorem: it is uniform separation of the downstream kernel from all limiting unit secants, including far-field limits.
3. **Finite-stage success remains weak evidence.** A family can have positive secant margins at every finite truncation while those margins tend to zero. Any limiting argument must retain a scale-uniform lower bound on `\tau_S(N)`.
4. **Properness must be attached to the retained representation, not an upstream one.** A compression may erase the coordinate responsible for escape to infinity while preserving injectivity and every local tangent check.
5. **The eventual arithmetic use is concrete and falsifiable.** For a proposed prime-derived representation followed by a linear/spectral projection, identify a matched control and compute or bound the closed-secant/kernel distance. If it vanishes, no downstream bounded linear operation can manufacture stable prime specificity after that compression.