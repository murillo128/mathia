# AF-265 — Dangerous Keiper zero surgery is compact-open invisible

**Status:** `EXACT-DERIVED`, `ARITHMETIC-FIDELITY`, `MATCHED-CONTROL`, `ZERO-SURGERY`, `STABILITY-OBSTRUCTION`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-263 shows that a reflection-symmetric off-critical zero quartet can carry any prescribed positive profinite Keiper cancellation level while preserving the classical order-one completed-function category. AF-264 then shows that even the first endpoint jet can be preserved exactly by balanced zero replacement.

There is a stronger **stability** obstruction that does not require balancing at all: dangerous zero quartets can escape to arbitrarily large height while becoming invisible in the compact-open topology of entire functions.

Fix

\[
\frac12<\beta<1,
\qquad
c\in(0,+\infty].
\tag{1}
\]

There exists a sequence

\[
\rho_n=\beta+i\gamma_n,
\qquad
\gamma_n\longrightarrow+\infty,
\tag{2}
\]

such that, writing

\[
1-\frac1{\rho_n}=r_n e^{i\theta_n},
\qquad
\alpha_n=\frac{\theta_n}{\pi},
\tag{3}
\]

one has the same prescribed profinite cancellation level at every stage,

\[
\boxed{K_{\mathrm{pc}}(\alpha_n)=c.}
\tag{4}
\]

Let

\[
Q_n=
\{\rho_n,\overline{\rho_n},1-\rho_n,1-\overline{\rho_n}\},
\qquad
P_n(s)=\prod_{z\in Q_n}(s-z),
\tag{5}
\]

and normalize the insertion by

\[
M_n(s)=\frac{P_n(s)}{P_n(0)}
=\prod_{z\in Q_n}\left(1-\frac{s}{z}\right),
\qquad
F_n(s)=M_n(s)\xi(s).
\tag{6}
\]

Then every `F_n` is entire of order one, satisfies

\[
F_n(1-s)=F_n(s),
\qquad
F_n(\overline s)=\overline{F_n(s)},
\qquad
F_n(0)=\xi(0),
\qquad
F_n(1)=\xi(1),
\tag{7}
\]

has all zeros in the open critical strip, and has the same leading Riemann--von Mangoldt zero-count asymptotic as `xi`. Nevertheless each `F_n` contains the added off-critical quartet `Q_n` with the prescribed invariant `(4)`.

At the same time,

\[
\boxed{F_n\longrightarrow\xi\quad\text{uniformly on every compact subset of }\mathbb C.}
\tag{8}
\]

More quantitatively, for every `R>0`,

\[
\sup_{|s|\le R}|M_n(s)-1|
\le
\left(1+\frac{R}{\gamma_n}\right)^4-1
\longrightarrow0,
\tag{9}
\]

and therefore

\[
\sup_{|s|\le R}|F_n(s)-\xi(s)|
\le
\sup_{|s|\le R}|\xi(s)|
\left[
\left(1+\frac{R}{\gamma_n}\right)^4-1
\right]
\longrightarrow0.
\tag{10}
\]

Consequently every fixed finite endpoint jet is asymptotically invisible as well. For every integer `m>=0`,

\[
\boxed{
\max_{0\le j\le m}
\left|F_n^{(j)}(0)-\xi^{(j)}(0)\right|
\longrightarrow0,
}
\tag{11}
\]

and by reflection the same holds at `s=1`.

For finite `c>0`, the sequence may be chosen so far out that eventually

\[
c>\log q_{\rho_n},
\qquad q_{\rho_n}=r_n^{-1}>1,
\tag{12}
\]

so the periodically-complete one-pair rate of the inserted pair remains genuinely dangerous:

\[
q_{\rho_n}e^{-c}<1.
\tag{13}
\]

Thus **every compact-open neighborhood of `xi` contains matched order-one Riemann-symmetric controls with an arbitrarily prescribed positive profinite Keiper obstruction**. Equivalently, the property “this completed function contains no such dangerous high quartet” has zero robustness radius in the compact-open topology.

## Why it matters

AF-264 establishes an exact non-fidelity result for the first endpoint jet by using a signed replacement fiber. The present result separates exact identifiability from stable identifiability. Pure addition cannot preserve the first derivative exactly, but it can change that derivative—and every other fixed finite local observable—by an arbitrarily small amount while retaining a phase obstruction of fixed strength.

That distinction is important for the current source problem. A theorem that merely says a finite collection of derivatives, compact values, contour integrals, or other compact-open-continuous observables differs between `xi` and every nontrivial zero insertion does not yet provide a usable discriminator. To exclude the dangerous Keiper phases stably, the observable needs a positive modulus that survives when the responsible zero moves to high height. Equations `(8)`--`(13)` show that no such modulus exists for any observation continuous in the ordinary compact-open topology alone.

The obstruction is also more global than a finite-jet counterexample. The controls converge to `xi` as entire functions on every fixed bounded region. Their extra zero divisors simply move beyond every fixed observation window. Arithmetic Fidelity therefore has to distinguish two resources that a local approximation can conflate: accuracy on all currently inspected compact sets versus uniform control of structure that can escape to infinity.

## Exact derivation

### 1. AF-263 supplies a fixed cancellation level at arbitrarily large height

AF-263 proves more than the existence of one control above a prescribed threshold. Its continued-fraction construction may start with arbitrarily large even first denominator while retaining the exact AF-261 realization mechanism. Hence for the fixed `beta` and fixed `c` in `(1)` there is a sequence of irrational phases `alpha_n->0` satisfying `(4)`.

AF-256's exact phase-to-zero pullback, used in AF-263, is

\[
\gamma
=
\frac12\left(
\cot(\pi\alpha)
+
\sqrt{\cot^2(\pi\alpha)+4\beta(1-\beta)}
\right).
\tag{14}
\]

Therefore `alpha_n->0` gives `gamma_n->+infinity`, proving `(2)` while preserving `(4)`.

The associated radial factor satisfies

\[
q_{\rho_n}^2
=
\frac{\beta^2+\gamma_n^2}
{(1-\beta)^2+\gamma_n^2}
\longrightarrow1.
\tag{15}
\]

For finite positive `c`, equation `(15)` implies `(12)` for all sufficiently large `n`, and then `(13)` is exactly the AF-261/AF-258 periodically-complete one-pair rate criterion. For `c=+infinity`, the extended-value rate is zero.

### 2. The normalized quartet multiplier tends to one on compact sets

Every root `z` in `Q_n` has imaginary part of magnitude `gamma_n`, so

\[
|z|\ge\gamma_n.
\tag{16}
\]

Because the quartet has even cardinality,

\[
\frac{P_n(s)}{P_n(0)}
=
\prod_{z\in Q_n}
\frac{s-z}{-z}
=
\prod_{z\in Q_n}\left(1-\frac{s}{z}\right),
\tag{17}
\]

which is `(6)`.

Fix `R>0`. For `|s|<=R`, equation `(16)` gives

\[
\left|\frac{s}{z}\right|
\le\frac{R}{\gamma_n}.
\tag{18}
\]

Using

\[
\left|\prod_{j=1}^4(1+u_j)-1\right|
\le
\prod_{j=1}^4(1+|u_j|)-1,
\tag{19}
\]

with `u_j=-s/z_j` yields `(9)`. Since every compact subset of `C` is contained in some disk, `M_n->1` locally uniformly. Multiplication by the fixed entire function `xi` gives `(8)` and the explicit bound `(10)`.

### 3. All fixed finite jets converge automatically

Local uniform convergence of holomorphic functions implies local uniform convergence of every fixed derivative. Applying this classical fact to `(8)` gives

\[
F_n^{(j)}\longrightarrow\xi^{(j)}
\tag{20}
\]

uniformly on compact sets for each fixed `j`, and hence `(11)`.

The finite-jet convergence can also be seen directly. Expanding `(17)`, for `1<=j<=4`,

\[
M_n^{(j)}(0)
=(-1)^j j!\,
 e_j\left(\left\{z^{-1}:z\in Q_n\right\}\right),
\tag{21}
\]

so

\[
|M_n^{(j)}(0)|
\le
j!\binom4j\gamma_n^{-j},
\tag{22}
\]

while `M_n^{(j)}(0)=0` for `j>4`. Leibniz then gives, for fixed `k`,

\[
F_n^{(k)}(0)-\xi^{(k)}(0)
=
\sum_{j=1}^{\min(k,4)}
\binom{k}{j}
M_n^{(j)}(0)\xi^{(k-j)}(0),
\tag{23}
\]

which tends to zero termwise. Reflection supplies the corresponding statement at `1` because both `F_n` and `xi` satisfy `G(1-s)=G(s)`.

Notice that `(22)` is only a convenient uniform bound. The quartet symmetry gives additional cancellations—for example AF-264 computes the first logarithmic-derivative displacement as `O(gamma_n^{-2})`—but no sharper rate is needed for the present obstruction.

### 4. The global analytic control remains in the same coarse class

The multiset `Q_n` is invariant under `z->1-z` and conjugation, so exactly as in AF-263,

\[
P_n(1-s)=P_n(s),
\qquad
P_n(\overline s)=\overline{P_n(s)},
\tag{24}
\]

and `P_n(1)=P_n(0)>0`. Therefore `(7)` follows from the standard properties of `xi`.

Multiplication by a nonzero quartic does not change order one. The four added zeros all lie in `0<Re(s)<1`. In the upper half-plane the multiplier adds two zeros once the counting height exceeds `gamma_n`, so

\[
N_{F_n}(T)=N_\xi(T)+2
\qquad(T>\gamma_n),
\tag{25}
\]

counting multiplicity. Thus the leading Riemann--von Mangoldt asymptotic is unchanged.

There is also an exact local version of the escape. For any fixed bounded set, once `n` is large enough all four added zeros lie outside it, and `M_n` is nonvanishing there. Hence the zero divisor of `F_n` inside that bounded region is exactly the zero divisor of `xi`; the difference is entirely in the high part of the global divisor.

## Prior-art audit

The complex-analysis mechanism in `(8)` is classical. Uniform convergence on compact subsets is the standard topology for holomorphic functions, and the Weierstrass convergence theorem gives convergence of fixed derivatives. Hurwitz's theorem explains the complementary zero-set statement: locally uniform convergence controls zeros in any fixed bounded region whose boundary avoids limit zeros, but it does not prevent additional zeros from escaping to infinity. Finite insertion of prescribed zeros by polynomial multiplication is elementary and sits inside the classical Weierstrass/Hadamard factorization framework.

Accordingly, **no novelty is claimed** for compact-open convergence, derivative convergence, Hurwitz stability on bounded domains, polynomial zero insertion, or the possibility that zeros escape every compact set. Those are standard facts of complex analysis.

The Arithmetic Fidelity content is the source-specific coupling. AF-261 realizes every positive profinite cancellation level, AF-256 pulls those phases back to off-critical zero coordinates, and AF-263 places the resulting quartets inside the Riemann-symmetric order-one completed-function category. Combining those exact ingredients with the classical compact-open topology proves that a fixed-strength Keiper cancellation obstruction can be made arbitrarily small to every bounded holomorphic observation at once. The novelty claim is restricted to this derived information-boundary statement; no new theorem of complex analysis is asserted.

A literature search around perturbations of zeros of entire functions, Hadamard products, Hurwitz convergence, and Taylor data found the general analytic behavior to be standard rather than a separate new phenomenon. That audit strengthens, rather than weakens, the interpretation here: the mathematical content to preserve is the exact arithmetic phase coupling, not the generic fact that distant zeros are locally hard to see.

## Boundaries

**This is a stability obstruction, not exact full-jet ambiguity.** For each fixed `n`, the analytic multiplier `M_n` is nonconstant, so `F_n` does not have the complete infinite jet of `xi` at an endpoint. Since entire functions are analytic, exact equality of the full infinite jet would force equality of the functions. AF-010 already separates finite-jet failure from full analytic-jet uniqueness in a more general setting.

**AF-264 remains strictly stronger for the first jet in the exact sense.** AF-264 constructs a different balanced replacement control with exact equality of value and first derivative. AF-265 instead uses addition-only surgery and proves approximate equality for every fixed finite jet simultaneously as the added quartet moves upward.

**Compact-open closeness is not global divisor closeness.** The inserted zeros lie farther and farther away. A topology or observable that explicitly tracks the divisor uniformly with height, or attaches height-dependent weight that does not vanish on the escaping quartet, is not covered by this no-go.

**The controls are not L-functions.** No Dirichlet series, Euler product, arithmetic coefficients, or Selberg-class axioms are asserted for `F_n`. A stronger arithmetic category may exclude these controls; indeed AF-263 identifies such source-specific structure as the next required input.

**Only the inserted pair obstruction is controlled.** Equation `(13)` is the AF-261/AF-258 one-pair periodically-complete rate for the target quartet. It does not determine the full Li sequence of `F_n` after interaction with all other zeros.

**No assertion is made about actual off-critical zeta zeros.** The `rho_n` are matched analytic controls. They show that compact-open information plus the listed completed-function symmetries cannot by themselves supply a robust phase-safety theorem.

## Research consequence

The post-AF-262 source question now has a topological obstruction in addition to the exact first-jet obstruction of AF-264. Any condition intended to prove

\[
K_{\mathrm{pc}}(\alpha_\rho)<\log q_\rho
\tag{26}
\]

for every hypothetical off-critical Riemann zero must be sensitive to information that does **not** disappear when the responsible zero moves to arbitrarily high height.

In particular, no finite family of observables that is continuous for compact-open convergence can provide a positive uniform separation margin between `xi` and all dangerous AF-263 controls. The next useful candidate therefore has to consume genuinely nonlocal source information: for example exact Dirichlet-series/Euler-product data, a height-uniform explicit-formula constraint, a global divisor norm with nonvanishing high-zero weight, or another zeta-specific structure whose control is not exhausted on bounded subsets of the `s`-plane.

This gives a concrete test for proposed source restrictions. Before attempting a difficult proof, ask whether the restriction is compact-open continuous at `xi`. If it is, AF-265 already shows that it cannot by itself be a robust separator against the current dangerous matched-control family.