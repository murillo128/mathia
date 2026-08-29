# WP-014 — the exact Prime-Flute Schiffer kernel is pointwise positive but not positive definite

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE` for the direct route that treats the exact nonprojective Grunsky–Schiffer coupling of PF-085 as the missing positive Weil pairing. The kernel is strictly positive at every real pair of tail endpoints, but every two distinct endpoints already give a `2 x 2` matrix with negative determinant. Thus its pointwise sign does **not** define a positive quadratic form. Moreover, the canonical positive repairs of the PF-085 compression are trace class, while the exact finite Weil operator from WP-004 is not even Hilbert–Schmidt. A successful exact-Prime-Flute route must therefore add a genuinely new singular/dynamical/global operation rather than read Weil positivity directly from the Schiffer coupling.

## 1. Candidate under test

WP-003 rules out the projective Prime-Flute sector as a prime-specific positivity mechanism because it has an exact all-composite isometric clone. One natural surviving object is the exact nonprojective endpoint map used in PF-085,

\[
V(x)=\pi\cot\frac{\pi}{x},\qquad x>2,
\]

with its exact Grunsky–Schiffer kernel

\[
\mathcal K_V(x,y)
=
\frac{V'(x)V'(y)}{(V(y)-V(x))^2}
-
\frac1{(y-x)^2}.
\]

PF-085 derives, for real `x,y>2`,

\[
\boxed{
\mathcal K_V(x,y)
=
\frac{\pi^2}{x^2y^2}
\left(\csc^2\delta-\frac1{\delta^2}\right),
\qquad
\delta=\pi\left(\frac1x-\frac1y\right),
}
\tag{1}
\]

with the continuous diagonal value

\[
\boxed{
\mathcal K_V(x,x)=\frac{\pi^2}{3x^4}.
}
\tag{2}
\]

The bracket in (1) is positive, so PF-085 correctly obtains positive rectangle defects and the exact separator-shortening inequality `L_E<L_0`. The question here is stronger and is the one required by the Weil-positivity line:

> Does this exact positive-looking coupling define a positive semidefinite kernel / geometric energy?

It does not.

## 2. Exact two-point obstruction

Put

\[
f(t):=\csc^2 t-\frac1{t^2},
\qquad f(0):=\frac13.
\]

For two distinct endpoints `x!=y`, equations (1)-(2) give

\[
M(x,y)
:=
\begin{pmatrix}
\mathcal K_V(x,x) & \mathcal K_V(x,y)\\
\mathcal K_V(y,x) & \mathcal K_V(y,y)
\end{pmatrix}
\]

and therefore

\[
\det M(x,y)
=
\frac{\pi^4}{x^4y^4}
\left(\frac19-f(\delta)^2\right).
\tag{3}
\]

Since `x,y>2`, one has

\[
0<|\delta|<\frac\pi2.
\]

The classical Mittag–Leffler expansion

\[
\csc^2 t
=
\sum_{k\in\mathbb Z}\frac1{(t-k\pi)^2}
\]

shows

\[
f(t)
=
\sum_{k\ne0}\frac1{(t-k\pi)^2}.
\]

Pair the terms `k` and `-k`. For `a=k\pi` and `0<|t|<\pi/2`,

\[
\frac1{(a-t)^2}+\frac1{(a+t)^2}-\frac2{a^2}
=
\frac{2t^2(3a^2-t^2)}{a^2(a^2-t^2)^2}
>0.
\]

Summing over `k>=1` yields

\[
\boxed{
f(t)>
2\sum_{k\ge1}\frac1{k^2\pi^2}
=\frac13
\qquad(0<|t|<\pi/2).
}
\tag{4}
\]

Substituting (4) into (3) gives the decisive sign:

\[
\boxed{
\det M(x,y)<0
\qquad\text{for every }x\ne y,\ x,y>2.
}
\tag{5}
\]

Thus every two distinct tail points already produce one positive and one negative eigenvalue.

Equivalently, the normalized off-diagonal correlation violates the Cauchy–Schwarz bound required of every PSD kernel:

\[
\boxed{
\frac{\mathcal K_V(x,y)}
{\sqrt{\mathcal K_V(x,x)\mathcal K_V(y,y)}}
=3f(\delta)>1.
}
\tag{6}
\]

This is stronger than saying that a large truncation eventually acquires a negative eigenvalue. The exact Schiffer kernel fails positive definiteness at the first nontrivial `2 x 2` test, for **every** pair of distinct real endpoints in its tail domain.

Changing the overall sign does not help, because the determinant in (5) is unchanged.

## 3. Pointwise positivity is therefore not geometric positivity

PF-085's pointwise inequality

\[
\mathcal K_V(x,y)>0
\]

remains correct and useful: rectangle integrals are positive and the exact cotangent endpoint deformation shortens the canonical separators relative to the projective reference.

But pointwise positivity of an interaction kernel is not positivity of the associated quadratic form. A positive semidefinite kernel must make every finite Gram matrix PSD. Equation (5) rules this out exactly.

Because `K_V` is continuous on compact subsets of `(2,infinity)^2`, the finite-point obstruction also gives an ordinary test-function obstruction. Choose two sufficiently narrow smooth bumps around any distinct `x` and `y`. Their `2 x 2` interaction matrix converges to `M(x,y)`, so the negative eigenvalue persists for narrow enough supports. Hence the corresponding integral pairing is not nonnegative on all smooth compactly supported test functions either.

Therefore the direct candidate

\[
\text{exact-circle Schiffer coupling}
\longrightarrow
\text{positive geometric quadratic form}
\longrightarrow
\text{global Weil positivity}
\]

fails before any arithmetic matching or archimedean completion is attempted.

## 4. Canonical positive repairs are too regular to recover the WP-004 finite operator

One can of course manufacture a positive operator from an indefinite compact coupling. The standard choices are things such as

\[
|A|=(A^*A)^{1/2},
\qquad
A^*A,
\qquad
J^*|A|J
\]

for a bounded comparison map `J`.

PF-085 proves something much stronger than compactness for the canonical prime-cell compression `A` of `K_V`:

\[
\boxed{
\sum_{m,n}|A_{mn}|<\infty,
\qquad A\in S_1.
}
\tag{7}
\]

Trace class is a two-sided operator ideal. Consequently `|A|`, `A^*A`, and every bounded compression/congruence `B A C` or `J^*|A|J` remain trace class (or better). In particular they are Hilbert–Schmidt.

By contrast, WP-004's exact positive finite-Weil operator

\[
T e_{p^k}
=(\log p)p^{-k/2}e_{p^k}
\]

satisfies

\[
\boxed{T\in S_q\iff q>2,}
\tag{8}
\]

so in particular

\[
\boxed{T\notin S_2\quad\text{and hence }T\notin S_1.}
\tag{9}
\]

Therefore no bounded linear compression, bounded change of Hilbert coordinates, bounded congruence, absolute-value repair, or positive square of the PF-085 trace-class coupling can equal the WP-004 finite-Weil operator.

This is an operator-ideal obstruction, not a comparison of numerical scales. The exact conformal endpoint interaction has summable global strength; the finite Weil axis operator sits exactly beyond the Hilbert–Schmidt boundary.

A Grunsky-style repair of the form `I-A^*A` does not evade the mismatch. If positive, it contains an identity component and is noncompact on the infinite-dimensional space, whereas `T` is compact. Removing the identity leaves a trace-class term and returns to the same ideal obstruction. This is the same structural warning seen elsewhere in the line: a universal positive diagonal/background cannot simply be retained when the exact Weil functional does not contain that term.

## 5. What this does and does not rule out

The result rules out the most direct positivity reading of the exact nonprojective Prime-Flute coupling:

```text
K_V itself                         -> indefinite already on two points
|A|, A* A, bounded congruences     -> positive possible, but trace class
WP-004 finite Weil operator T      -> not even Hilbert-Schmidt
```

It does **not** prove that every operation built from the exact endpoint geometry is too regular. Schatten class can be changed by genuinely singular operations, for example:

- an unbounded change of Hilbert-space weight;
- a non-Lipschitz spectral functional calculus near zero;
- a singular limit or renormalization;
- a dynamical transfer/propagation operator carrying slower long-range decay;
- a quotient or boundary construction whose main term is not a bounded sandwich of `A`;
- a global coupling to Prime-Lattice or archimedean degrees of freedom that is not present in PF-085.

Those are real escapes, not loopholes to suppress. But each introduces exactly the extra mechanism that this research line is asking to derive intrinsically. It can no longer be claimed that the already-existing exact Schiffer coupling supplies the missing positive form by itself.

The result also does not contradict PF-085. That finding proved **pointwise** positivity and positive rectangle defects; it did not prove that `K_V` is a positive-definite covariance kernel. Equation (5) distinguishes these two notions sharply.

## 6. Prior-art and novelty audit

The general warning is classical. Grunsky/Schiffer theory controls the relevant bilinear operator through Grunsky or Bergman–Schiffer inequalities; the Schiffer kernel is not, in general, asserted to be a PSD covariance kernel. Modern conformal-welding/Weil–Petersson work likewise organizes positivity through operator norms, squares, Fredholm determinants, and Hilbert–Schmidt/Schatten conditions rather than through pointwise positivity of the raw mixed kernel. PF-085 already records this classical operator-theoretic prior art.

Directed searches for the exact map

\[
V(z)=\pi\cot(\pi/z)
\]

combined with Grunsky/Schiffer positivity, positive-definite kernels, Weil positivity, and Riemann-zeta applications did not locate a prior source turning this specialization into an RH mechanism. No novelty is claimed for the Mittag–Leffler expansion, the Cauchy–Schwarz PSD test, trace ideals, or Grunsky theory.

The durable Mathia-specific result is the exact specialization (3)-(6) together with the cross-branch comparison (7)-(9): **the strongest surviving exact Prime-Flute conformal coupling has positive entries but the wrong quadratic-form sign, while its canonical positive repairs are spectrally much too nuclear to reproduce the exact Prime-Lattice finite-Weil operator through bounded geometry.**

## 7. Falsification / audit core

The decisive checks are finite and exact:

1. verify the PF-085 formula (1) and diagonal (2);
2. compute the `2 x 2` determinant to obtain (3);
3. use the paired Mittag–Leffler terms to prove `f(delta)>1/3` for every nonzero `|delta|<pi/2`;
4. conclude `det M<0` and the normalized Cauchy–Schwarz violation (6);
5. independently verify PF-085's absolute-entry summability and hence `A in S_1`;
6. compare with WP-004's exact Schatten criterion `T in S_q iff q>2`.

A future exact-Prime-Flute proposal escapes this finding only if it identifies a **specific canonical operation outside this bounded/trace-class Schiffer route** and proves why that operation is forced by the geometry rather than selected to repair the sign or Schatten mismatch.

## Consequence for the research line

After WP-003, exact cotangent data remained one of the principal ways Prime Flute could conceivably recover arithmetic specificity lost by the projective model. PF-085 supplied its most canonical conformal interaction. WP-014 now shows that this object does not supply the missing positivity:

\[
\boxed{
\text{exact nonprojective Schiffer geometry}
\;\not\Rightarrow\;
\text{PSD pairing},
}
\]

and its standard positive operator repairs cannot be the WP-004 finite boundary component under bounded extraction.

The surviving Prime-Flute route is therefore narrower: it must use the exact endpoint data inside a **genuinely dynamical, singular, quotient/cohomological, or boundary-response construction** whose positivity theorem is independent and whose slower/non-trace-class arithmetic sector is derived rather than inserted.