# AF-390 — Quasianalytic logarithmic curvature closes multiscale solid PF3 recognition

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `TARGET-FIDELITY` · `TOTAL-POSITIVITY` · `PF3` · `TOEPLITZ` · `MULTISCALE` · `QUASIANALYTICITY` · `UNIQUE-CONTINUATION` · `NO-NOVELTY-CLAIM`

## Claim

AF-389 leaves one precise smooth boundary stratum open: under nonnegative solid order-two/order-three Toeplitz minors on a sequence of meshes tending to zero, the logarithmic curvature

\[
q=-(\log f)''
\]

is nonnegative and every zero of `q` is infinitely flat. The remaining obstruction therefore disappears as soon as the source class has **flat-zero unique continuation**.

Let

\[
f:\mathbb R\to(0,\infty)
\]

be `C^\infty`, let `h_\nu>0` with `h_\nu\to0`, and define

\[
C_{j,\nu}(d)
:=
\det\!\left(f((d+a-b)h_\nu)\right)_{a,b=0}^{j-1},
\qquad j=2,3.
\tag{1}
\]

Assume

\[
C_{2,\nu}(d)\ge0,
\qquad
C_{3,\nu}(d)\ge0
\tag{2}
\]

for every `\nu` and every integer `d`. Write

\[
g=\log f,
\qquad q=-g''.
\tag{3}
\]

Assume additionally the following source-class property:

\[
q^{(m)}(x_0)=0\ \text{for every }m\ge0
\quad\Longrightarrow\quad
q\equiv0\ \text{on }\mathbb R.
\tag{UC}
\]

Then the translation kernel

\[
K_f(u,x)=f(u-x)
\tag{4}
\]

is totally nonnegative through order three on `\mathbb R\times\mathbb R`.

Consequently, inside any source class for which `(UC)` holds for the logarithmic curvature, the shrinking-mesh solid certificate is exact:

\[
\boxed{
\bigl[C_{2,\nu}(d),C_{3,\nu}(d)\ge0\ \forall \nu,d\bigr]
\iff
K_f\in TN_3.
}
\tag{5}
\]

The reverse implication is immediate. The forward implication is the new synthesis: AF-389 converts every lower-order degeneracy into an infinitely-flat zero, unique continuation removes that residual boundary stratum, and AF-385 then upgrades the retained solid samples to all continuum placements.

Real analyticity is only one sufficient source category. More generally, `(UC)` holds when `q` belongs to a quasianalytic Denjoy--Carleman class on the connected real line. Thus the actual regularity resource used by this recognition route is not analyticity itself but **quasianalytic flat-jet uniqueness for the logarithmic curvature**.

## Step 1: multiscale solid signs force a flat-zero dichotomy

AF-389 applies directly to `(2)`. It gives

\[
q(x)\ge0
\qquad (x\in\mathbb R)
\tag{6}
\]

and, at every zero `x_0` of `q`,

\[
q^{(m)}(x_0)=0
\qquad(m=0,1,2,\ldots).
\tag{7}
\]

Combining `(7)` with `(UC)` yields the dichotomy

\[
q>0\ \text{everywhere}
\qquad\text{or}\qquad
q\equiv0.
\tag{8}
\]

Indeed, if `q` has any zero then `(7)` makes that zero flat and `(UC)` forces `q\equiv0`; otherwise nonnegativity `(6)` implies strict positivity everywhere.

This isolates the precise role of the additional source regularity. The sampled determinant hierarchy itself supplies infinite-order contact information. The source class is used only to decide whether an infinitely-flat contact can remain local.

## Step 2: the nondegenerate branch supplies strict sampled order-two minors

Assume first

\[
q>0.
\tag{9}
\]

Then

\[
g''=-q<0,
\tag{10}
\]

so `g=\log f` is strictly concave. For every real `x` and every `h>0`, strict midpoint concavity gives

\[
2g(x)>g(x-h)+g(x+h).
\tag{11}
\]

Exponentiating,

\[
f(x)^2>f(x-h)f(x+h).
\tag{12}
\]

Hence every solid order-two Toeplitz minor is strictly positive:

\[
\det
\begin{pmatrix}
f(x)&f(x-h)\\f(x+h)&f(x)\end{pmatrix}>0.
\tag{13}
\]

In particular, for each sampled mesh `h_\nu` and integer offset `d`,

\[
C_{1,\nu}(d)=f(dh_\nu)>0,
\qquad
C_{2,\nu}(d)>0.
\tag{14}
\]

The assumed top-order generators remain

\[
C_{3,\nu}(d)\ge0.
\tag{15}
\]

Therefore AF-385 applies with `k=3`: sampled strictness at orders one and two together with nonnegative sampled solid order-three minors on a vanishing mesh sequence certifies all continuum minors through order three. Thus

\[
K_f\in TN_3.
\tag{16}
\]

No unsampled placement sign is assumed.

## Step 3: the degenerate branch is already totally nonnegative

Assume instead

\[
q\equiv0.
\tag{17}
\]

Then `g''=0`, so

\[
g(x)=ax+b,
\qquad
f(x)=e^{ax+b}.
\tag{18}
\]

The translation kernel factorizes as

\[
K_f(u,x)=e^{a(u-x)+b}
=e^b e^{au}e^{-ax}.
\tag{19}
\]

It has rank one and is strictly positive entrywise. Every minor of order at least two therefore vanishes, while every order-one minor is positive. Hence

\[
K_f\in TN_k
\qquad\text{for every }k,
\tag{20}
\]

and in particular `K_f\in TN_3`.

Thus both branches of `(8)` satisfy the target, proving the forward implication of `(5)`.

## Why quasianalyticity is the relevant retained source resource

AF-387 shows that a single fixed lattice can hide a negative non-solid order-three minor on a nonstrict lower-order boundary. AF-388 and AF-389 show that one continuous profile sampled on arbitrarily fine compatible lattices cannot sustain any finite-order contact with that boundary. The only remaining alias is therefore an infinitely-flat one.

The theorem above identifies exactly what closes that alias for this proof architecture: a class in which the infinite jet at one point determines whether `q` is zero. In standard language this is quasianalyticity of the admissible curvature class. The extra resource is consequently much weaker conceptually than demanding an explicit formula or analytic continuation for `f`; it is a **source-class uniqueness rule for the information that the multiscale certificate has already recovered**.

This is an Arithmetic Fidelity instance of a recurring pattern:

\[
\text{compressed samples}
\;\Longrightarrow\;
\text{a complete local jet constraint}
\;\xrightarrow{\text{source rigidity}}\;
\text{global exclusion of the residual fibre}.
\tag{21}
\]

The retained data need not reconstruct `f`. They only need to recover enough local boundary information that the declared source category turns the remaining fibre into a trivial one.

## Denjoy--Carleman corollary

Let `\mathcal Q` be a quasianalytic Denjoy--Carleman class on real intervals, with the usual restriction/continuation interpretation, and suppose

\[
q=-(\log f)''\in\mathcal Q.
\tag{22}
\]

By quasianalyticity, the Taylor/Borel map is injective: if every derivative of `q` vanishes at a point, `q` vanishes on the connected interval and hence, by overlapping restrictions, on the connected real line. Thus `(UC)` holds and `(5)` follows.

This strictly extends the real-analytic corollary in AF-389 at the level relevant to recognition. Real-analytic functions form a quasianalytic class, but quasianalytic Denjoy--Carleman classes can be strictly larger than the analytic class.

No closure theorem is needed here for `f\mapsto-(\log f)''`: the corollary assumes directly that the resulting `q` lies in the declared quasianalytic class. If one instead wants to state the hypothesis as `f\in\mathcal Q`, the necessary closure under logarithm/composition and differentiation must be checked for that particular Denjoy--Carleman category rather than silently assumed.

## Prior-art and novelty audit

The ingredients are classical or already persisted locally, and no novelty is claimed for quasianalytic uniqueness or for the underlying total-positivity recognition theorem.

- Vincent Thilliez, **“On Quasianalytic Local Rings,”** *Expositiones Mathematicae* **26**(1) (2008), 1--23, DOI `10.1016/j.exmath.2007.04.001`. Role: authoritative Denjoy--Carleman/quasianalytic background, including injectivity of the Taylor/Borel map and the Denjoy--Carleman criterion. This source is already anchored in `SOURCES.md` for AF-010.
- Christian Grussler and Tobias Damm, **“Efficient k-Sign Consistency Verification of Hankel Matrices via Schur Polynomials,”** arXiv:`2602.08122` (2026), especially Proposition 2. Role: finite structured-minor recognition underlying AF-385 and already anchored by the preceding PF3 certificate findings.
- H. F. Weinberger, **“A Characterization of the Polya Frequency Functions of Order 3,”** *Applicable Analysis* **15** (1983), 53--69, DOI `10.1080/00036818308839439`. Role: classical full-`PF_3` characterization territory, already anchored by AF-389; it prevents treating `(5)` as a new characterization of the unrestricted `PF_3` class.

A focused search for combinations of quasianalytic/Denjoy--Carleman regularity with Pólya-frequency or Toeplitz total-positivity recognition did not locate this exact shrinking-solid-minor formulation. That absence is not used as evidence of novelty. Equation `(5)` is recorded as a derived source-class/resource theorem obtained by combining the multiscale boundary rigidity of AF-389 with the sampled recognition theorem AF-385 and classical quasianalytic uniqueness.

## Boundaries and falsification checks

The unique-continuation hypothesis applies to `q=-(\log f)''`, not merely to `f`. A smooth positive `f` can have an infinitely-flat nonnegative `q` without `(UC)`, so AF-389's remaining smooth boundary case is not removed by this theorem.

The mesh sequence must tend to zero. The theorem does not repair the fixed-lattice counterexample mechanism of AF-387.

Both sampled orders are load-bearing. The order-two inequalities are what give `q\ge0`; the order-three hierarchy is what forces zeros of `q` to be infinitely flat. Quasianalyticity alone cannot manufacture either sign.

The result is target-fidelity, not source identification. It certifies the continuum `TN_3` property from compressed placement data inside a rigid source class; it does not reconstruct `f`, distinguish rational primes, establish all-order Pólya frequency, or imply RH.

Finally, `(UC)` is sufficient for closing the residual fibre in this argument, not claimed to be logically necessary for every possible recognition theorem. A weaker class-specific mechanism might forbid precisely the infinitely-flat counterexamples compatible with `(2)` without being quasianalytic in full generality. That is now the sharper residual question.