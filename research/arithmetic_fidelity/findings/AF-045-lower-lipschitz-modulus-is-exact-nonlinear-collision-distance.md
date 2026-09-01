# AF-045 — Lower Lipschitz modulus is the exact nonlinear collision distance

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `STRUCTURAL-CLASSIFICATION`, `NEGATIVE/OBSTRUCTION`

## Claim

Let `(X,d,x_0)` be a pointed metric space with at least two points, let `V` be a real Banach space, and let

\[
\operatorname{Lip}_0(X;V)
=
\{f:X\to V:f(x_0)=0,\ \operatorname{Lip}(f)<\infty\}
\]

with norm

\[
\|f\|_{\mathrm{Lip}}
=
\operatorname{Lip}(f)
=
\sup_{x\ne y}
\frac{\|f(x)-f(y)\|}{d(x,y)}.
\]

Define the **lower Lipschitz fidelity modulus**

\[
\beta(f)
=
\inf_{x\ne y}
\frac{\|f(x)-f(y)\|}{d(x,y)}.
\]

For each distinct pair `x,y\in X`, define the pair-collision subspace

\[
\mathcal C_{x,y}
=
\{g\in\operatorname{Lip}_0(X;V):g(x)=g(y)\},
\]

and put

\[
\mathcal C
=
\bigcup_{x\ne y}\mathcal C_{x,y}
\]

for the set of non-injective Lipschitz maps. Also define

\[
\Sigma
=
\{g\in\operatorname{Lip}_0(X;V):\beta(g)=0\}
\]

for the stable-fidelity failure set. Then:

1. **Every fixed collision fiber has an exact distance formula.** For every `x\ne y`,
   \[
   \boxed{
   \operatorname{dist}_{\mathrm{Lip}}(f,\mathcal C_{x,y})
   =
   \frac{\|f(x)-f(y)\|}{d(x,y)}.
   }
   \]
   A nearest pair-colliding map always exists, and it is obtained by a rank-one Lipschitz perturbation built from a distance function.

2. **The lower Lipschitz modulus is exactly the distance to non-injectivity.**
   \[
   \boxed{
   \operatorname{dist}_{\mathrm{Lip}}(f,\mathcal C)
   =
   \beta(f).
   }
   \]
   Thus `\beta(f)` is not merely a lower distortion bound: it is the sharp `\operatorname{Lip}`-norm radius before an actual pair can be collapsed.

3. **`\beta` is 1-Lipschitz on the entire Lipschitz-map space.** For all `f,g`,
   \[
   \boxed{
   |\beta(f)-\beta(g)|
   \le
   \|f-g\|_{\mathrm{Lip}}.
   }
   \]
   Consequently `\Sigma` is closed.

4. **Stable fidelity failure is precisely the closure of exact collisions.**
   \[
   \boxed{
   \Sigma
   =
   \overline{\mathcal C}^{\|\cdot\|_{\mathrm{Lip}}}.
   }
   \]
   Hence
   \[
   \boxed{
   \operatorname{dist}_{\mathrm{Lip}}(f,\Sigma)
   =
   \operatorname{dist}_{\mathrm{Lip}}(f,\mathcal C)
   =
   \beta(f).
   }
   \]

5. **Stable fidelity is exactly bi-Lipschitz recoverability.** Since every `f\in\operatorname{Lip}_0(X;V)` already has a finite upper Lipschitz constant,
   \[
   \boxed{
   \beta(f)>0
   \iff
   f:X\to f(X)\text{ is bi-Lipschitz}.
   }
   \]
   The bi-Lipschitz embeddings therefore form an open subset of `\operatorname{Lip}_0(X;V)`, and `\beta(f)` is their exact distance to the complement.

6. **The perturbation radius is sharp.** If
   \[
   \|h\|_{\mathrm{Lip}}<\beta(f),
   \]
   then
   \[
   \boxed{
   \beta(f+h)
   \ge
   \beta(f)-\|h\|_{\mathrm{Lip}}>0.
   }
   \]
   No smaller Lipschitz perturbation can destroy stable recoverability; perturbations producing actual collisions exist at every radius arbitrarily close to `\beta(f)`, and at radius exactly `\beta(f)` whenever the defining pairwise infimum is attained.

7. **Nearest exact collision is equivalent to pairwise attainment.** There exists `g\in\mathcal C` satisfying
   \[
   \|f-g\|_{\mathrm{Lip}}=\beta(f)
   \]
   if and only if some actual pair `x\ne y` attains
   \[
   \frac{\|f(x)-f(y)\|}{d(x,y)}=\beta(f).
   \]
   Thus the distinction between an actual worst pair and a limiting family of pairs survives exactly as an attainment/non-attainment distinction in function space.

8. **Lipschitz-free linearization identifies the canonical carrier.** Let `\mathcal F(X)` be the Lipschitz-free Banach space of the pointed metric space and
   \[
   m_{x,y}
   =
   \frac{\delta_x-\delta_y}{d(x,y)}
   \]
   the normalized elementary molecule. The canonical linearization
   \[
   \widehat f:\mathcal F(X)\to V
   \]
   satisfies
   \[
   \|\widehat f\|=\|f\|_{\mathrm{Lip}},
   \qquad
   \widehat f(m_{x,y})
   =
   \frac{f(x)-f(y)}{d(x,y)}.
   \]
   Therefore
   \[
   \boxed{
   \beta(f)
   =
   \inf_{x\ne y}\|\widehat f(m_{x,y})\|.
   }
   \]
   Pairwise collision is exactly the event that the linearized operator kills an elementary molecule. AF-043/AF-044's secant carrier is therefore the Euclidean-image specialization of a more intrinsic **molecule carrier** for arbitrary metric data.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{for arbitrary metric inputs and Banach-valued Lipschitz representations, the lower Lipschitz modulus is exactly the distance to collision and to stable fidelity loss.}
}
\]

This removes the finite-dimensional linearity assumption from AF-044 at the correct global metric level. The price is equally precise: without compactness of the relevant molecule carrier, the distance need not be attained by an actual collision even when it is strictly positive.

## Derivation

### Exact distance to one prescribed collision

Fix `x\ne y`. If `g\in\mathcal C_{x,y}`, then

\[
(f-g)(x)-(f-g)(y)
=
f(x)-f(y),
\]

so

\[
\|f(x)-f(y)\|
\le
\|f-g\|_{\mathrm{Lip}}d(x,y).
\]

Therefore

\[
\operatorname{dist}_{\mathrm{Lip}}(f,\mathcal C_{x,y})
\ge
\frac{\|f(x)-f(y)\|}{d(x,y)}.
\]

For the reverse inequality, set

\[
v
=
\frac{f(x)-f(y)}{d(x,y)}
\in V
\]

and define the scalar distance potential

\[
\psi_x(z)
=
d(z,x)-d(x_0,x).
\]

The triangle inequality gives

\[
\|\psi_x\|_{\mathrm{Lip}}\le1,
\qquad
\psi_x(x_0)=0,
\]

while

\[
\psi_x(x)-\psi_x(y)
=-d(x,y).
\]

Define the rank-one Lipschitz perturbation

\[
h(z)=\psi_x(z)v.
\]

Then `h(x_0)=0`,

\[
\|h\|_{\mathrm{Lip}}
\le
\|v\|
=
\frac{\|f(x)-f(y)\|}{d(x,y)},
\]

and in fact equality holds because the pair `(x,y)` realizes that ratio for `h`. Moreover

\[
h(x)-h(y)
=-(f(x)-f(y)).
\]

Thus `g=f+h` satisfies `g(x)=g(y)` and

\[
\|f-g\|_{\mathrm{Lip}}
=
\frac{\|f(x)-f(y)\|}{d(x,y)}.
\]

This proves the exact fixed-pair formula and gives an explicit nearest point of every `\mathcal C_{x,y}`.

### Distance to the union of all collisions

Since

\[
\mathcal C
=
\bigcup_{x\ne y}\mathcal C_{x,y},
\]

one has

\[
\begin{aligned}
\operatorname{dist}_{\mathrm{Lip}}(f,\mathcal C)
&=
\inf_{x\ne y}
\operatorname{dist}_{\mathrm{Lip}}(f,\mathcal C_{x,y})\\
&=
\inf_{x\ne y}
\frac{\|f(x)-f(y)\|}{d(x,y)}\\
&=
\beta(f).
\end{aligned}
\]

Unlike the finite-dimensional closed-secant proof of AF-044, no compactness, differentiability, linearity of `f`, or finite-dimensionality of `X` or `V` enters this identity.

### `\beta` is 1-Lipschitz

For each fixed pair `x\ne y`, the reverse triangle inequality gives

\[
\left|
\frac{\|f(x)-f(y)\|}{d(x,y)}
-
\frac{\|g(x)-g(y)\|}{d(x,y)}
\right|
\le
\|f-g\|_{\mathrm{Lip}}.
\]

Taking infima over the same pair set yields

\[
\beta(f)
\ge
\beta(g)-\|f-g\|_{\mathrm{Lip}},
\]

and exchanging `f,g` gives the claimed 1-Lipschitz estimate. Hence

\[
\Sigma=\beta^{-1}(\{0\})
\]

is closed.

Every non-injective map belongs to `\Sigma`, so

\[
\overline{\mathcal C}\subseteq\Sigma.
\]

Conversely, if `f\in\Sigma`, then

\[
\operatorname{dist}_{\mathrm{Lip}}(f,\mathcal C)
=
\beta(f)
=0,
\]

which is exactly `f\in\overline{\mathcal C}`. Therefore

\[
\Sigma=\overline{\mathcal C}.
\]

Finally, for any `g\in\Sigma`, the 1-Lipschitz estimate gives

\[
\beta(f)
\le
\|f-g\|_{\mathrm{Lip}},
\]

so

\[
\operatorname{dist}(f,\Sigma)\ge\beta(f).
\]

The reverse inequality follows from `\mathcal C\subseteq\Sigma` and the collision-distance identity. Thus all three quantities agree.

### Bi-Lipschitz interpretation and sharp radius

If `\beta(f)>0`, then for all `x,y`,

\[
\beta(f)d(x,y)
\le
\|f(x)-f(y)\|
\le
\|f\|_{\mathrm{Lip}}d(x,y).
\]

The lower inequality makes `f` injective and gives a Lipschitz inverse on `f(X)` with constant at most `1/\beta(f)`. Conversely every bi-Lipschitz embedding has a positive lower constant, so `\beta(f)>0`.

The 1-Lipschitz property now gives the perturbation estimate

\[
\beta(f+h)
\ge
\beta(f)-\|h\|_{\mathrm{Lip}}.
\]

Hence the open ball of radius `\beta(f)` around a bi-Lipschitz embedding consists entirely of bi-Lipschitz embeddings. The exact distance identity proves that this radius cannot be enlarged.

### Attainment criterion

If an actual pair `(x,y)` attains `\beta(f)`, the distance-potential construction above gives `g\in\mathcal C_{x,y}` with

\[
\|f-g\|_{\mathrm{Lip}}=\beta(f).
\]

Conversely suppose `g\in\mathcal C` is a nearest exact collision. Choose `x\ne y` with `g(x)=g(y)`. Then

\[
\frac{\|f(x)-f(y)\|}{d(x,y)}
\le
\|f-g\|_{\mathrm{Lip}}
=
\beta(f).
\]

The reverse inequality holds by definition of `\beta`, so this pair attains the infimum.

Thus non-attainment of the lower Lipschitz infimum is exactly non-proximinality of the union of pair-collision subspaces at `f`.

## Lipschitz-free-space formulation

For a pointed metric space `(X,d,x_0)`, the Lipschitz-free space `\mathcal F(X)` is generated by the evaluation vectors `\delta_x` and has the universal property that every `f\in\operatorname{Lip}_0(X;V)` has a unique bounded linearization

\[
\widehat f:\mathcal F(X)\to V
\]

with

\[
\widehat f(\delta_x)=f(x),
\qquad
\|\widehat f\|=\|f\|_{\mathrm{Lip}}.
\]

For the normalized elementary molecule

\[
m_{x,y}
=
\frac{\delta_x-\delta_y}{d(x,y)},
\]

one has `\|m_{x,y}\|=1` and

\[
\widehat f(m_{x,y})
=
\frac{f(x)-f(y)}{d(x,y)}.
\]

Therefore the metric fidelity modulus is the restricted minimum modulus of `\widehat f` on the canonical molecule set:

\[
\boxed{
\beta(f)
=
\inf_{m\in\operatorname{Mol}_1(X)}
\|\widehat f(m)\|,
}
\]

where `\operatorname{Mol}_1(X)=\{m_{x,y}:x\ne y\}` denotes the normalized elementary molecules, not the whole unit sphere of `\mathcal F(X)`.

The fixed-pair distance construction is also linear in this representation. The scalar function `\psi_x` is a norm-one functional on `\mathcal F(X)` whose value on `m_{x,y}` is `-1`; tensoring it with `v` produces the rank-one operator perturbation that kills `m_{x,y}`. Thus the nonlinear-looking collision repair is exactly the same rank-one range-kernel move seen in AF-044, after passing through the canonical free linearization.

This gives a clean hierarchy:

\[
\text{metric pairs}
\longrightarrow
\text{normalized molecules}
\longrightarrow
\text{linearized representation}
\longrightarrow
\text{restricted minimum modulus}.
\]

No arbitrary embedding of `X` into Euclidean space is required. The molecule carrier is forced by the metric itself.

## Boundary controls

### Injective Lipschitz maps can have zero stable margin

Take

\[
X=[0,1],
\qquad
V=\mathbb R,
\qquad
f(t)=t^2,
\]

with base point `0`. The map is Lipschitz and injective, but for `0\le s<t\le1`,

\[
\frac{|t^2-s^2|}{t-s}
=t+s.
\]

Hence

\[
\beta(f)=0.
\]

The theorem predicts exact collisions arbitrarily close in Lipschitz norm. They are explicit: for `t>0`,

\[
g_t(z)=z^2-tz
\]

satisfies

\[
g_t(0)=g_t(t)=0,
\qquad
\|g_t-f\|_{\mathrm{Lip}}=t\to0.
\]

Thus ordinary injectivity can be destroyed by arbitrarily small `\operatorname{Lip}`-norm perturbations even on a compact interval. This is the fully nonlinear analogue of AF-044's injective-but-zero-secant-margin parabola example.

### Positive distance need not be attained by an actual collision

Let

\[
X=\mathbb N_0
\]

with its ordinary metric and base point `0`, and define

\[
f(n)=n+\log(n+1).
\]

For `n>m`,

\[
\frac{|f(n)-f(m)|}{n-m}
=
1+
\frac{\log(n+1)-\log(m+1)}{n-m}
>1.
\]

The infimum is nevertheless `1`, for example along pairs escaping to infinity. Hence

\[
\boxed{\beta(f)=1}
\]

but no actual pair attains the value. Therefore

\[
\operatorname{dist}_{\mathrm{Lip}}(f,\mathcal C)=1
\]

and there is **no nearest non-injective map**.

By contrast the stable-failure set can attain the same distance in this example. Let

\[
g(n)=\log(n+1).
\]

Then `\beta(g)=0` while

\[
\|f-g\|_{\mathrm{Lip}}=1.
\]

So `g\in\Sigma` is a nearest stable-failure map even though no nearest exact collision exists. This cleanly separates the closed stable-loss set from the nonclosed union of exact pair-collision sets without relying on finite-dimensional secant compactness.

### Finite pair sets remove the attainment issue

If `X` is finite, the pairwise infimum is a minimum. Every injective Lipschitz map then has `\beta(f)>0`, and every positive distance to `\mathcal C` is attained by a pair-specific rank-one perturbation. Thus the distinction between exact and stable fidelity is inherently an infinite/limiting phenomenon in this metric category.

## Prior art and novelty assessment

None of the ingredients should be presented as a new general theory of metric embeddings.

- G. Godefroy and N. J. Kalton, **“Lipschitz-free Banach spaces,”** *Studia Mathematica* 159(1) (2003), 121–141, DOI `10.4064/sm159-1-6`. Role: classical Lipschitz-free Banach-space framework behind the canonical linearization of pointed Lipschitz maps.
- Marek Cúth, Michal Doucha, and Tamás Titkos, **“Isometries of Lipschitz-free Banach spaces,”** *Journal of the London Mathematical Society* 110(5) (2024), e70000, DOI `10.1112/jlms.70000`. Role: modern explicit reference for normalized elementary molecules and the universal property `\|\widehat f\|=\operatorname{Lip}(f)` used in the molecule-carrier formulation.
- E. J. McShane, **“Extension of range of functions,”** *Bulletin of the American Mathematical Society* 40(12) (1934), 837–842, DOI `10.1090/S0002-9904-1934-05978-0`. Role: foundational scalar Lipschitz extension theory and classical context for the distance-function Lipschitz potentials used in the explicit collision repair.
- Kevin Wildrick and Thomas Zürcher, **“Sharp Differentiability Results for the Lower Local Lipschitz Constant and Applications to Non-embedding,”** *Journal of Geometric Analysis* 25(4) (2015), 2590–2616, DOI `10.1007/s12220-014-9527-9`. Role: established lower-Lipschitz language in metric-to-Banach analysis; the existence and importance of lower metric distortion constants are not new here.

AF-044 already placed restricted minimum moduli and exact distance-to-instability statements next to classical conic condition theory and Renegar-style condition measures. The present theorem extends that audit from a finite-dimensional linear compression acting on a declared Euclidean carrier to the full Banach space of Lipschitz representations of an arbitrary metric carrier.

A targeted literature search did not locate the exact displayed identity

\[
\operatorname{dist}_{\mathrm{Lip}}
(f,\{\text{non-injective Lipschitz maps}\})
=
\beta(f)
\]

as a separately named theorem. That absence is **not** a novelty claim: the proof is an elementary consequence of standard Lipschitz distance functions, and the free-space formulation is classical linearization machinery. The durable Mathia value is the exact synthesis and its consequence for this line: nonlinear metric fidelity has the same sharp distance-to-loss structure as the linear secant theory, with elementary molecules replacing Euclidean secants and noncompactness controlling attainment.

## Boundaries and failure modes

- The theorem is about perturbations measured in the global Lipschitz seminorm after fixing a base point. Uniform/sup-norm, `C^1`, Sobolev, probabilistic, or operator-topology perturbations define different failure geometries.
- `\beta(f)>0` certifies metric recoverability of the entire declared carrier. It does not certify that the retained metric information contains a later arithmetic discriminator; AF-001's fiber/discriminator test remains logically separate.
- The target Banach structure is used by the rank-one repair. For a general metric-valued target there is no vector addition, so the exact perturbation construction does not transfer automatically.
- The molecule set need not be compact or closed in a way that yields a minimizing molecule. The distance formula is universal; nearest-point statements require separate attainment/proximinality hypotheses.
- Local differential nondegeneracy is neither assumed nor sufficient. This theorem is a global pairwise statement and therefore does not replace AF-007's infinitesimal audit when the representation category is smooth and local structure matters independently.
- No arithmetic or RH conclusion follows. An arithmetic application must still identify the exact upstream discriminator and prove that the chosen metric representation is relevant to it rather than merely well-conditioned as a generic embedding.

## Consequence for the line

AF-042 through AF-044 isolated stable fidelity on compact smooth carriers and under finite-dimensional linear compression as a secant/tangent transversality problem with a sharp distance-to-failure modulus. This finding shows that the **distance-to-loss principle itself is not tied to Euclidean secants**: it survives for arbitrary metric sources and nonlinear Banach-valued Lipschitz representations after replacing secants by the canonical elementary molecules of the Lipschitz-free space.

Accordingly, future compression proposals can be separated into two audits:

1. **metric conditioning:** compute or bound the lower molecule modulus `\beta` in the perturbation category actually being used;
2. **discriminator relevance:** independently prove, via AF-001-style fiber logic or a stronger category-specific theorem, that the surviving metric distinctions contain the structural discriminator of interest.

A proposal that fails the first audit is arbitrarily close to an actual collision in its natural Lipschitz function space. A proposal that passes the first but fails the second can be perfectly recoverable as a metric embedding while still forgetting the arithmetic property one hoped to transport. This distinction prevents condition-number language from being mistaken for prime specificity.