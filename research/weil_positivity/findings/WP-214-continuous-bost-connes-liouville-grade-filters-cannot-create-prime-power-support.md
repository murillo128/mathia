# WP-214 — Continuous Bost–Connes Liouville-grade filters cannot create prime-power support

**Status:** `DERIVED + EXACT + BOST-CONNES-KMS + LIOUVILLE-GRADING + CONTINUOUS-FUNCTIONAL-CALCULUS + DENSE-RATIONAL-LOG-GRADES + PRIME-POWER-SUPPORT-OBSTRUCTION + BOREL-TARGET-CODING-CONTROL + PRIOR-ART-CLASSICALIZATION + DECISIVE-CORRECTION + NOT-A-WEIL-BRIDGE`.

This finding replaces withdrawn `WP-213`, whose density calculation was correct but whose repeated use of “physical time generator/Hamiltonian” conflated two distinct Bost–Connes operators. The standard state Hamiltonian on `ell^2(N)` has the discrete spectrum `log n`; the dense rational-log spectrum occurs instead in the **Liouville/time-grade generator** implementing the dynamics on operator modes. The distinction is mathematically decisive.

In the standard representation let

\[
H\varepsilon_n=(\log n)\varepsilon_n.
\]

On the doubled Hilbert space define the self-adjoint Liouvillean

\[
L:=H\otimes I-I\otimes H.
\]

Then

\[
L(\varepsilon_a\otimes\varepsilon_b)
=\log(a/b)(\varepsilon_a\otimes\varepsilon_b),
\]

so its rational multiplicative grades are

\[
\Gamma:=\{\log q:q\in\mathbb Q_+^\times\}.
\]

This is exactly the grading seen algebraically from the Bost–Connes dynamics: a homogeneous operator of ratio `q` transforms by `q^{it}`. The set `Gamma` is dense in `R`.

The signed prime-power grades required by the finite Weil term are

\[
\mathcal P:=\{\pm k\log p:p\text{ prime},\ k\ge1\}.
\]

`P` is locally finite, hence `Gamma\P` is dense. Therefore any continuous scalar multiplier `F:R->C` satisfying

\[
F(\log q)=0
\qquad
(\log q\in\Gamma\setminus\mathcal P)
\]

must satisfy

\[
\boxed{F\equiv0.}
\]

Thus **continuous scalar functional calculus of the Liouville/time-grade generator cannot manufacture exact prime-power support from a source occupying the full rational grading**. The obstruction is topology, not boundedness or sign.

Arbitrary Borel functional calculus evades the theorem but immediately becomes target coding. Since `P` is Borel, `1_P(L)` is an orthogonal spectral projection, and a nonnegative Borel symbol assigning `log p` at `+- k log p` yields a positive self-adjoint multiplier with a closed quadratic form. The same construction works for any prescribed locally finite frequency set and any nonnegative weights. Positivity and closability therefore do not make such a selector arithmetic or canonical.

The corrected boundary is consequently:

\[
\boxed{
\text{continuous scalar calculus of }L
\Longrightarrow
\text{no nonzero prime-power selector},
}
\]

while

\[
\boxed{
\text{arbitrary Borel calculus of }L
\Longrightarrow
\text{support and weights can be inserted by definition}.
}
\]

This statement deliberately makes **no corresponding claim about continuous scalar calculus of the state Hamiltonian `H`**. Its spectrum is discrete, and `WP-215` shows that smooth positive interpolation on `H` can encode prime-power support; the price appears as asymptotic regularity loss rather than a topological impossibility.

## 1. The two generators must not be identified

Bost and Connes' standard representation has

\[
H\varepsilon_n=(\log n)\varepsilon_n,
\qquad n\ge1,
\tag{1}
\]

and the time evolution is implemented by conjugation with `e^{itH}`. For the multiplicative isometry `mu_a`,

\[
e^{itH}\mu_a e^{-itH}=a^{it}\mu_a.
\tag{2}
\]

More generally, a homogeneous ratio operator such as `mu_a mu_b^*` has time grade `log(a/b)` wherever the algebraic expression acts. The operator-space or doubled-Hilbert implementation is therefore naturally governed by

\[
L=H\otimes I-I\otimes H.
\tag{3}
\]

Equation (3) gives

\[
\operatorname{Spec}_{\rm point}(L)
\supseteq
\{\log(a/b):a,b\in\mathbb N\}
=\Gamma.
\tag{4}
\]

By contrast,

\[
\operatorname{Spec}(H)=\{\log n:n\in\mathbb N\},
\tag{5}
\]

which has no finite accumulation point. The density theorem below belongs to (4), not (5).

This distinction is not terminological bookkeeping. A continuous function can interpolate arbitrary values on the discrete set (5), while continuity on the dense set (4) rigidly determines the function.

## 2. Dense unwanted Liouville grades force a continuous selector to vanish

The positive rationals are dense in `R_+`, and logarithm is a homeomorphism `R_+ -> R`. Hence

\[
\overline\Gamma=\mathbb R.
\tag{6}
\]

For every `R>0`, only finitely many signed prime powers satisfy `k log p <= R`, because this is equivalent to `p^k<=e^R`. Thus

\[
\mathcal P\cap[-R,R]
\]

is finite. Removing a locally finite subset from a dense subset of `R` leaves a dense subset, so

\[
\boxed{
\overline{\Gamma\setminus\mathcal P}=\mathbb R.
}
\tag{7}
\]

Let `F:R->C` be continuous and suppose a scalar Liouville multiplier is intended to remove every unwanted rational grade:

\[
F(\gamma)=0
\qquad
(\gamma\in\Gamma\setminus\mathcal P).
\tag{8}
\]

By (7), continuity gives

\[
\boxed{F(x)=0\quad\text{for every }x\in\mathbb R.}
\tag{9}
\]

In particular it also vanishes on every desired prime-power grade. Requiring `F>=0`, allowing `F` to be unbounded, or choosing a smooth/analytic subclass cannot repair (9); all remain continuous.

The statement is about **creating support**. If an independently defined source object has already annihilated all unwanted rational grades, a continuous multiplier may act on that smaller source. Then the arithmetic selector has been supplied upstream and must itself pass the Mathia canonicality and sign audit.

## 3. Uniform suppression is equally rigid on the dense grading

Suppose instead that

\[
|F(\gamma)|\le\epsilon
\qquad
(\gamma\in\Gamma\setminus\mathcal P).
\tag{10}
\]

For every `x in R`, choose `gamma_j in Gamma\P` with `gamma_j->x`. Continuity gives

\[
|F(x)|\le\epsilon.
\]

Hence

\[
\boxed{
\sup_{x\in\mathbb R}|F(x)|\le\epsilon.
}
\tag{11}
\]

A continuous Liouville filter therefore cannot uniformly suppress all unwanted rational grades while retaining an order-one response on a desired prime-power grade. Strong limits of continuous filters may converge to discontinuous Borel projections, but such a limit is necessarily non-uniform/singular in the grade topology and still requires a source reason for choosing the prime-power set.

## 4. Borel spectral selection proves that positivity is not the missing theorem

Because `P` is closed and Borel, the spectral theorem permits

\[
P_{\rm pp}:=\mathbf 1_{\mathcal P}(L),
\tag{12}
\]

an orthogonal projection. Likewise define

\[
M_\Lambda(E)
=
\begin{cases}
\log p,&E=\pm k\log p,\\
0,&E\notin\mathcal P.
\end{cases}
\tag{13}
\]

Then `M_Lambda(L)` is positive self-adjoint on its natural domain and its quadratic form

\[
Q_\Lambda(\xi)=\|M_\Lambda(L)^{1/2}\xi\|^2
\tag{14}
\]

is closed and nonnegative.

This is a matched control, not a candidate Weil mechanism. For any locally finite `S subset R` and any prescribed `a:S->[0,infinity)`, the Borel multiplier taking value `a(E)` on `S` and zero elsewhere has exactly the same positivity and closedness. The arithmetic data live entirely in the chosen symbol.

Therefore “use a singular positive spectral projector” does not solve the research mandate unless an independent Mathia construction forces that projector or its support before the desired arithmetic consequence is identified.

## 5. Relation to the KMS findings and to `WP-215`

`WP-209` identifies the Bost–Connes critical KMS midpoint as a source-forced origin of the half-density. `WP-211` and `WP-212` show that the canonical forward and inverse Kubo–Mori scalar multipliers preserve unwanted support and fail the bounded-mass requirement. The present theorem says that replacing those particular grade multipliers by an arbitrary **continuous scalar function of the Liouville grade** cannot solve the selector problem either.

The statement does not extend to `F(H)`. On the state Hamiltonian the integer-log spectrum is discrete, so a continuous, even smooth, nonnegative function can be engineered to take arbitrary prescribed values on the eigenvalues. `WP-215` gives the exact control and shows why this apparent escape is still not a geometric derivation: the selector is target-coded, and the critical Weil amplitudes force loss of every global Hölder exponent `alpha>=1/2`.

Thus the Bost–Connes route has two different failure modes rather than one:

\[
\text{Liouville grade }L:
\quad
\text{continuity is too rigid},
\tag{15}
\]

whereas

\[
\text{state Hamiltonian }H:
\quad
\text{continuity is too permissive and can encode the answer}.
\tag{16}
\]

A genuine construction must explain why its operator, domain, and arithmetic support are source-forced before the final positive form is read out.

## 6. Aggressive falsification and exact scope

**Could a discontinuous Liouville multiplier select prime powers?** Yes; (12)--(14) do so. This is why the theorem is a regularity/canonicity boundary, not an impossibility theorem for all spectral calculus.

**Could a non-scalar operator couple grades and evade (9)?** Yes. Matrix/operator-valued mixing does not reduce to `F(log q)` and remains a live category, subject to the independent sign and finite--archimedean assembly requirements.

**Could a source observable already have prime-power support?** Yes. Then the density obstruction is irrelevant, but the source itself must derive that support independently rather than hide a Mangoldt projector in its definition.

**Does the standard Hamiltonian have the dense spectrum used in (7)?** No. That was the defect in withdrawn `WP-213`. The discrete Hamiltonian case is treated separately in `WP-215`.

**Does any argument here use RH or zeta-zero data?** No. It uses only the multiplicative Bost–Connes time grading and elementary spectral topology.

## 7. Prior-art and novelty boundary

No novelty is claimed for the Bost–Connes system, the Hamiltonian (1), implementation of the time evolution, the Liouvillean difference construction, continuous/Borel functional calculus, or the spectral theorem. Bost and Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Mathematica 1 (1995), 411–457, DOI `10.1007/BF01589495`, is already a durable anchor in this line's `SOURCES.md`.

No novelty is claimed for the elementary topological fact that a continuous function vanishing on a dense set is zero. The durable Mathia-specific content is the corrected operator dictionary and the resulting exact boundary for the live KMS escape: dense rational-log grades belong to the Liouville/operator-mode generator, where regular scalar selection is impossible, while the standard state Hamiltonian belongs to a different interpolation problem.

This is not a new positivity theorem, a reformulation of Weil's criterion, or evidence for RH.

## Consequence for the research frontier

The corrected result narrows rather than closes the Bost–Connes direction. The KMS critical point still supplies a source-forced half-density, but scalar Liouville functional calculus cannot manufacture Mangoldt support continuously, while arbitrary Borel calculus can manufacture it only by inserting the target. The standard state Hamiltonian does not restore canonicity either, as `WP-215` shows.

A surviving route must therefore introduce arithmetic support through additional source geometry, a non-scalar/global coupling, a cohomological boundary, or a singular structure selected for an independent reason. It must still produce the archimedean and polar sectors in the same audited normalization and obtain the final Weil sign from an independent theorem.