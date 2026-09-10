# AF-253 — Affine root fidelity is controlled by the fiber-norm exponent

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `OUTPUT-SAMPLING`, `AFFINE-CONSTRAINTS`, `DIOPHANTINE-FIDELITY`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-252 closes torsion affine constraints by a finite-residue dichotomy but leaves the genuinely different case in which the affine class has infinite order in the quotient torus. For arbitrary affine cosets, the missing quantity is the root-scale decay of the **whole restricted fiber polynomial**.

Let

\[
P(x)=\sum_{k\in F}c_k e^{2\pi i\langle k,x\rangle},
\qquad x\in\mathbb T^d,
\tag{1}
\]

be a nonzero trigonometric polynomial. Let `H <= T^d` be a connected subtorus of dimension `r>=1`, let

\[
C=a+H,
\tag{2}
\]

and give `C` the Haar probability measure transported from `H`. For each `n>=1`, define the fiber restriction

\[
P_{n,C}(u)=P(na+u),
\qquad u\in H,
\tag{3}
\]

and its intrinsic fiber norm

\[
R_n(P,C)
:=\|P_{n,C}\|_{L^2(H)}.
\tag{4}
\]

Changing the representative `a` of `C` only translates the argument `u`, so `(4)` depends on the affine coset, not on the chosen representative.

Define the fiber-collapse exponent

\[
\chi(P,C)
:=\limsup_{n\to\infty}
\frac{1}{n}\log^+\frac1{R_n(P,C)},
\tag{5}
\]

with `log^+(1/0)=+infinity`, and define the exponential-cancellation set

\[
\mathcal E_C(P)
=
\left\{\alpha\in C:
\limsup_{n\to\infty}
\frac{-\log|P(n\alpha)|}{n}>0
\right\}.
\tag{6}
\]

Then there is an exact zero-one alternative at Haar scale:

\[
\boxed{
\chi(P,C)>0
\quad\Longrightarrow\quad
\mathcal E_C(P)=C,
}
\tag{7}
\]

whereas

\[
\boxed{
\chi(P,C)=0
\quad\Longrightarrow\quad
\mu_C\bigl(\mathcal E_C(P)\bigr)=0.
}
\tag{8}
\]

In the second branch, for Haar-almost every `alpha in C`, the entire amplitude sequence is root-faithful:

\[
\boxed{
\lim_{n\to\infty}|P(n\alpha)|^{1/n}=1.
}
\tag{9}
\]

Therefore every unbounded output sampling inherits root rate one for almost every point of the coset.

The exponent `(5)` has an exact quotient-frequency interpretation. Let

\[
\rho:\mathbb Z^d\to\widehat H
\tag{10}
\]

be restriction of ambient characters to `H`, and group the finite frequency set `F` by equal restricted character. For each `lambda in rho(F)`, choose one representative `k_lambda in F`. On the quotient torus

\[
Q=\mathbb T^d/H,
\qquad q=a+H,
\tag{11}
\]

define the vector trigonometric polynomial

\[
B_\lambda(y)
=
\sum_{\substack{k\in F\\rho(k)=\lambda}}
 c_k\,\chi_{k-k_\lambda}(y),
\qquad
B=(B_\lambda)_\lambda.
\tag{12}
\]

Here `k-k_lambda` annihilates `H`, so it is canonically a character of `Q`. Then Parseval gives

\[
\boxed{
R_n(P,C)^2
=
\sum_{\lambda\in\rho(F)}|B_\lambda(nq)|^2
=\|B(nq)\|_2^2.
}
\tag{13}
\]

Thus whole-fiber collapse is itself a finite-dimensional shrinking-target problem on the quotient. If

\[
Z_B=\{y\in Q:B(y)=0\},
\tag{14}
\]

is empty, then `chi(P,C)=0`. If `Z_B` is nonempty, compact Łojasiewicz control together with the Lipschitz bound for `B` implies

\[
\boxed{
\chi(P,C)>0
\iff
\limsup_{n\to\infty}
\frac1n\log^+
\frac1{\operatorname{dist}(nq,Z_B)}>0.
}
\tag{15}
\]

So an infinite-order affine constraint can make cancellation non-generic only by driving its quotient orbit **exponentially close to the simultaneous coefficient-annihilator set**.

Two immediate rigidity corollaries are useful:

- if `rho` is injective on `F`, no two ambient frequencies collide after restriction to `H`, every component of `B` is a nonzero constant up to the harmless chosen phase convention, and `R_n` is constant; hence `chi(P,C)=0` for every affine translate;
- if `q` is torsion, `B(nq)` is periodic, so `chi(P,C)>0` exactly when one periodically visited quotient point lies in `Z_B`. This recovers AF-252's catastrophic component criterion as the torsion specialization of `(13)`--`(15)`.

## Why it matters

AF-251 and AF-252 left an important ambiguity. For a non-homogeneous affine constraint with infinite quotient orbit, the restricted polynomial changes with `n`; there was no fixed finite family of components to which the previous Łojasiewicz/Hausdorff argument could be applied uniformly. Equation `(13)` isolates the moving part before asking about pointwise cancellation inside a fiber.

There are now two mathematically distinct ways to lose exponential information. **Coefficient collapse** occurs when the whole fiber polynomial has exponentially small norm; `(7)` shows that this is catastrophic and affects every point of the affine coset. If that coefficient layer is only subexponentially small, then the remaining **within-fiber cancellation** is governed by normalized trigonometric polynomials with a fixed finite frequency budget. Lawton's small-value estimate is uniform after `L^2` normalization, so Borel--Cantelli forces that second mechanism to remain Haar exceptional.

This resolves the infinite-order affine boundary of AF-252 at the measure-theoretic level and sharpens the source-side target. A genuine arithmetic affine relation does not become dangerous merely because its quotient orbit is infinite or dense. To create a positive-measure failure, the source must force exponential recurrence of the quotient phase to the fixed set `Z_B`; otherwise almost every point on the constrained coset remains root-faithful.

## Derivation / evidence

### 1. Parseval isolates the whole-fiber coefficient layer

Write the restriction `(3)` by grouping ambient frequencies with the same character on `H`:

\[
P_{n,C}(u)
=
\sum_{\lambda\in\rho(F)}
 A_{n,\lambda}\,\lambda(u),
\tag{16}
\]

where

\[
A_{n,\lambda}
=
\sum_{\substack{k\in F\\rho(k)=\lambda}}
 c_k e^{2\pi i n\langle k,a\rangle}.
\tag{17}
\]

Distinct characters of `H` are orthonormal in `L^2(H)`. Therefore

\[
R_n^2
=
\sum_\lambda |A_{n,\lambda}|^2.
\tag{18}
\]

If `a` is replaced by `a+h_0`, each grouped coefficient is multiplied by the unit phase `lambda(nh_0)`, so `(18)` also proves intrinsicity of `R_n`.

Let `M=|rho(F)|`. Cauchy--Schwarz gives the uniform fiber bound

\[
\|P_{n,C}\|_\infty
\le
\sum_\lambda|A_{n,\lambda}|
\le
\sqrt M\,R_n.
\tag{19}
\]

This is the decisive estimate for the catastrophic branch.

### 2. Positive fiber exponent forces every point to fail

Suppose `chi(P,C)>0` and choose `0<c<chi(P,C)`. Infinitely many `n` satisfy

\[
R_n<e^{-cn}.
\tag{20}
\]

For `alpha=a+h`, multiplication by `n` gives

\[
P(n\alpha)=P(na+nh)=P_{n,C}(nh).
\tag{21}
\]

Equations `(19)` and `(20)` yield along the same infinite subsequence

\[
|P(n\alpha)|
\le \sqrt M e^{-cn}
\tag{22}
\]

for **every** `h in H`. The fixed factor `sqrt(M)` disappears after division by `n`, proving `(7)`. Exact zeros of `R_n` are included automatically.

### 3. Zero fiber exponent leaves a uniformly normalized finite-frequency family

Assume now `chi(P,C)=0`. Apart from at most finitely many indices with `R_n=0`, define

\[
G_n=\frac{P_{n,C}}{R_n},
\qquad
\|G_n\|_{L^2(H)}=1.
\tag{23}
\]

Every `G_n` has Fourier support contained in the same set `rho(F)` of at most `M` characters. By Parseval, its largest Fourier coefficient has modulus at least `M^{-1/2}`.

Wayne Lawton's finite-frequency small-value theorem, used already in AF-250, then gives constants `C_M>0` and `gamma_M>0` independent of `n` such that

\[
\mu_H\{u:|G_n(u)|<v\}
\le C_M v^{\gamma_M},
\qquad 0<v\le1.
\tag{24}
\]

For `M>=2`, one may take `gamma_M=1/(M-1)` up to the theorem's fixed coefficient-height constant; the lower bound `M^{-1/2}` on the largest normalized coefficient makes that constant uniform over the whole moving family. If `M=1`, every normalized restriction has constant modulus one and the small-value event is empty for `v<1`.

The multivariate torus form `(24)` is the same Kronecker-flow lift used in AF-250: choose a one-parameter flow separating the finitely many restricted frequencies, apply Lawton to that one-variable almost-periodic polynomial, and identify its mean small-value frequency with Haar measure on `H`.

### 4. Borel--Cantelli gives Haar-generic all-sampling fidelity

Fix `epsilon>0`. Since `chi(P,C)=0`, for all sufficiently large `n`,

\[
R_n\ge e^{-\epsilon n/2}.
\tag{25}
\]

Let

\[
E_n(\epsilon)
=
\{h\in H:|P(n(a+h))|<e^{-\epsilon n}\}.
\tag{26}
\]

Because `H` is a connected torus, multiplication `h -> nh` is surjective and Haar preserving. Using `(21)`, `(23)`, `(25)`, and `(24)`,

\[
\mu_H(E_n(\epsilon))
\le
C_M e^{-\gamma_M\epsilon n/2}
\tag{27}
\]

for all sufficiently large `n`. The series of `(27)` is summable. The first Borel--Cantelli lemma therefore shows that for almost every `h`, only finitely many `E_n(epsilon)` occur.

Intersect over positive rational `epsilon`. For almost every `alpha in C`, no positive exponential defect occurs. Since `P` is bounded on the compact ambient torus, the upper root bound tends to one, giving `(9)` and then `(8)`.

No equidistribution, mixing, or independence of the orbit is used. The only dynamical input in this step is Haar preservation of multiplication on the fiber torus.

### 5. The quotient vector is the exact moving-coefficient invariant

Factor `(17)` by the chosen representative `k_lambda`. Since every difference `k-k_lambda` is trivial on `H`, it descends to a quotient character. Up to the unit scalar `chi_{k_lambda}(na)`, the grouped coefficient is exactly `B_lambda(nq)`. Taking moduli and summing proves `(13)`.

Consequently `R_n` is not an arbitrary sequence of norms: it is the amplitude of one fixed vector-valued trigonometric polynomial sampled along the quotient orbit `nq`.

If `Z_B` is empty, compactness gives `inf_Q ||B||_2>0`, so `chi=0`. If `Z_B` is nonempty, set `D(y)=||B(y)||_2`. The function `D` is Lipschitz on the compact torus and vanishes exactly on `Z_B`, so

\[
D(y)\le L\,\operatorname{dist}(y,Z_B).
\tag{28}
\]

Conversely, after representing the torus algebraically, the semialgebraic Łojasiewicz inequality gives constants `A,C>0` with

\[
\operatorname{dist}(y,Z_B)^A
\le C D(y).
\tag{29}
\]

Equations `(28)`--`(29)`, evaluated at `y=nq`, show that positive exponential decay of `R_n=D(nq)` is equivalent to positive exponential recurrence to `Z_B`, proving `(15)`. The exact exponent can change by the Łojasiewicz power; the zero-versus-positive dichotomy does not.

### 6. The two-mode Li cancellation is the simplest irrational example

Take `d=2`, the diagonal subtorus

\[
H=\{(t,t):t\in\mathbb T\},
\tag{30}
\]

and the Li-shaped mode

\[
P(x_1,x_2)
=-2\cos(2\pi x_1)-2\cos(2\pi x_2).
\tag{31}
\]

For the affine translate represented by `a=(0,theta)`, direct grouping gives

\[
R_n
=2\sqrt2\,|\cos(\pi n\theta)|.
\tag{32}
\]

Thus `(5)` is, up to the fixed constant, exactly AF-249's half-integer exponential approximation exponent. If `theta=1/2`, odd indices give `R_n=0` and `(7)` reduces to AF-252's torsion catastrophic component. If `theta` is irrational but has positive half-integer exponential approximation exponent, `R_n` becomes exponentially small along an infinite subsequence and **the entire affine diagonal**, not merely one specially chosen point, lies in `E_C(P)`.

This example shows why the infinite-order case is not captured by checking exact componentwise vanishing: exponential approach to the quotient annihilator set is already enough for full-coset root-rate loss.

## Prior-art audit

Wayne M. Lawton, **“Distribution of Small Values of Bohr Almost Periodic Functions with Bounded Spectrum,”** *Journal of Siberian Federal University. Mathematics & Physics* 12(5) (2019), 571--578, DOI `10.17516/1997-1397-2019-12-5-571-578`, arXiv:`1904.09373`, proves the polynomial small-value estimate used in `(24)`. In the finite-frequency case its constant depends only on the number of frequencies and the modulus of the largest coefficient; Parseval normalization is what makes that theorem uniform over the moving fiber family here.

Edward Dobrowolski, **“A Note on Lawton's Theorem,”** *Canadian Mathematical Bulletin* 60(3) (2017), 484--489, DOI `10.4153/CMB-2016-066-x`, gives neighboring multivariable small-value bounds for polynomials with bounded numbers of coefficients. This confirms that coefficient-uniform finite-frequency sublevel control is classical approximation/Mahler-measure technology, not a new ingredient of AF-253.

The quotient-character decomposition `(16)`--`(18)`, Parseval, Haar invariance, and Borel--Cantelli are classical harmonic/measure theory. The equivalence `(15)` uses the standard compact semialgebraic Łojasiewicz inequality; AF-251 already audits that ingredient and the neighboring shrinking-target literature. AF-252 already audits torsion cosets through Laurent's Diophantine-geometry work.

A targeted search across affine-subtorus restrictions, trigonometric-polynomial small values, quotient-frequency cancellation, and toral shrinking-target formulations did not locate the exact zero-one synthesis `(5)`--`(15)`. No broad novelty is claimed. The durable contribution is the Arithmetic Fidelity reduction: separate moving whole-fiber coefficient collapse from normalized within-fiber cancellation, prove that the former is exactly a quotient shrinking-target exponent, and show that only the former can make the exponential failure nonexceptional on an affine coset.

## Boundaries and failure modes

**The null branch is measure-theoretic.** AF-251 obtains Hausdorff codimension for one fixed polynomial and AF-252 for finitely many torsion components. Here the normalized fiber polynomial varies with `n`; `(24)` is sufficient for Haar-nullity but this finding does not claim the same codimension bound for arbitrary infinite-order affine translates. A uniform metric-entropy theorem for the moving normalized zero sets would be needed for that strengthening.

**Connectedness of `H` matters.** It guarantees that multiplication by `n` is Haar preserving through a surjective torus endomorphism. Disconnected subgroup constraints require componentwise bookkeeping and are not included.

**Fixed finite frequency budget.** The uniform Lawton constant depends on the finite restricted-frequency count. No uniform statement is claimed when the number of active modes grows with `n`.

**Positive `chi` is a source condition, not generic evidence.** Equation `(15)` says exactly what an affine source would have to force, but it does not prove that actual Riemann-zero phases do or do not have this exponential recurrence property.

**Output sampling remains downstream of source access.** As in AF-244--AF-252, preserving an already-formed root discriminator does not reduce the cancellation-coherent arithmetic depth required to construct the relevant Li coefficient.

## Research consequence

The affine phase frontier now has a clean hierarchy. Homogeneous constraints are safe generically by AF-251. Torsion affine constraints are the periodic specialization classified in AF-252. Arbitrary infinite-order affine constraints reduce to one new invariant, `chi(P,C)`: if the grouped coefficient vector approaches its quotient annihilator set exponentially, the whole coset collapses; if it does not, only a Haar-null subset can still exhibit exponential cancellation.

For zeta/Li applications, the next useful theorem is therefore source-specific rather than another generic torus statement. Given any genuine affine relation among a finite dominant zero-phase family, form its quotient vector `B` and ask whether arithmetic information about the actual phases can prove

\[
\limsup_{n\to\infty}
\frac1n\log^+
\frac1{\operatorname{dist}(nq,Z_B)}=0.
\tag{33}
\]

That is the exact non-torsion analogue of AF-249's half-integer irrationality-base barrier. It identifies the property that must survive the affine compression before any downstream Li root-rate argument can be trusted.