# AF-406 — Finite Pólya-frequency positivity is not zero-set faithful under exponential gauge

**Status:** `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `TARGET-FIDELITY`, `TOTAL-POSITIVITY`, `LAGUERRE-POLYA`, `RIEMANN-XI`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-REDIRECT`, `NO-NOVELTY-CLAIM`

## Claim

Finite-order Pólya-frequency positivity is not a faithful invariant of the zero set, even on the classical Riemann-`xi` generating function family.

Write

\[
\xi_1(z)=\xi(\sqrt z+1/2)=\sum_{k\ge 0} b_k z^k.
\tag{1}
\]

Katkova proved three facts that are decisive for the fidelity interpretation of finite total positivity:

1. `xi_1 in PF_44` unconditionally;
2. `xi_1 in APF_m` for every finite `m`;
3. for every finite `m` there exists `n_0(m)` such that, for every integer `n >= n_0(m)`,

\[
e^{nz}\xi_1(z)\in PF_m.
\tag{2}
\]

The multiplier `e^{nz}` has no zeros, so

\[
Z(e^{nz}\xi_1)=Z(\xi_1)
\tag{3}
\]

with multiplicity. Therefore, for every fixed finite `m`, the truth value of membership in `PF_m` can be changed to positive along a **zero-preserving exponential gauge orbit** without changing the discriminator relevant to RH.

Consequently, a finite-order Pólya-frequency verdict cannot by itself be a zero-set-faithful certificate. Any attempt to use finite `PF_m` positivity as a proxy for the Laguerre–Pólya / RH target must either fix the exponential gauge by an independent canonical normalization or retain additional structure that is not manufactured by the gauge.

This strengthens AF-372 in a source-specific direction. AF-372 gives generic false positives at every bounded determinant order. Katkova's theorem shows, for the actual `xi_1` source, that finite-order positivity is also **gauge-manufacturable while the entire zero divisor is held fixed**.

## Exact fidelity statement

Let

\[
F_n(z)=e^{nz}\xi_1(z),
\qquad n\ge 0,
\tag{4}
\]

and let the target discriminator be any property depending only on the zero divisor, for example

\[
D(F)=\mathbf 1_{\{Z(F)\subset(-\infty,0]\}}.
\tag{5}
\]

Equation `(3)` gives

\[
D(F_n)=D(\xi_1)
\qquad\text{for every }n.
\tag{6}
\]

For a fixed finite `m`, define

\[
C_m(F)=\mathbf 1_{\{F\in PF_m\}}.
\tag{7}
\]

Katkova's Theorem 3 gives an `n_0(m)` for which

\[
C_m(F_n)=1
\qquad(n\ge n_0(m)).
\tag{8}
\]

Thus `C_m` is not invariant on zero-divisor fibers. In Arithmetic Fidelity language, it cannot be an intrinsic observable of the quotient that forgets the zero-free exponential factor.

The obstruction is stronger than ordinary finite-order insufficiency. It is not merely that two unrelated functions may share the same finite positivity verdict. Here a transformation that preserves **all zeros exactly** can force the finite positivity verdict after sufficiently strong exponential tilting.

## Relation to all-order total positivity

There is no corresponding contradiction with the all-order criterion.

Katkova recalls the classical Aissen–Schoenberg–Whitney–Edrei equivalence

\[
\xi_1\in PF_\infty
\quad\Longleftrightarrow\quad
\xi_1\in L\!\! -\! P^+
\quad\Longleftrightarrow\quad
\mathrm{RH}.
\tag{9}
\]

Her finite-order smoothing result states that, for each fixed `m`, one can choose `n` large enough to obtain `PF_m`. It does **not** provide one finite `n` for which the tilted function is in `PF_m` simultaneously for every `m`, unless the all-order target is already satisfied.

Hence the quantifiers are the essential surviving structure:

\[
\forall m\ \exists n_0(m)\ \forall n\ge n_0(m): F_n\in PF_m
\tag{10}
\]

is strictly weaker than

\[
\exists n\ \forall m: F_n\in PF_m.
\tag{11}
\]

This is another concrete instance of the Arithmetic Fidelity theme that every fixed finite compression can look fully positive while the unbounded relational hierarchy retains the target information.

## Consequence for the current confluent-Hankel branch

AF-404 and AF-405 study the signed confluent determinants

\[
H_r(t)=(-1)^{r(r-1)/2}
\det\bigl(f^{(i+j)}(t)\bigr)_{0\le i,j<r}
\tag{12}
\]

for the full Euler/log kernel. These are local confluent shadows of a translation-minor hierarchy; they are not themselves equivalent to the complete `PF_r` condition.

Katkova's result therefore does **not** settle the open `H_5` sign question and does not make finite-order calculations useless. It changes their interpretation: even the stronger statement `PF_m` at a fixed finite order is not, without gauge normalization, a faithful zero-set certificate. A proof of `H_5>0` would be a genuine structural fact about that kernel, but it must not be promoted to evidence that finite positivity alone is approaching an RH-equivalent discriminator.

The useful next question is therefore not only how far the confluent flag stays positive, but which normalization or relational datum prevents zero-preserving exponential tilts from manufacturing the same finite-order signature.

## Prior-art and novelty audit

- Olga M. Katkova, **“Multiple Positivity and the Riemann Zeta-Function,”** *Computational Methods and Function Theory* **7**(1) (2007), DOI `10.1007/BF03321628`; arXiv:`math/0505174`. Role: Theorem 1 proves `xi_1 in PF_44`; Theorem 2 proves `xi_1 in APF_m` for every finite `m`; Theorem 3 proves that for each finite `m`, sufficiently large exponential multipliers `e^{nz}` put `xi_1` in `PF_m` without changing its zero set.
- I. J. Schoenberg, **“On the Zeros of the Generating Functions of Multiply Positive Sequences and Functions,”** *Annals of Mathematics* **62** (1955), 447–471. Role: classical finite-order multiple-positivity and zero-location background used by Katkova.
- M. Aissen, I. J. Schoenberg, A. Whitney and A. Edrei, **“On the Generating Functions of Totally Positive Sequences,”** *Journal d'Analyse Mathématique* **2** (1953), 93–109. Role: all-order Pólya-frequency / Laguerre–Pólya characterization underlying the RH equivalence for `xi_1`.

No novelty is claimed for Katkova's finite-order theorems, the zero preservation under multiplication by a zero-free exponential, or the classical Pólya-frequency characterizations. The Arithmetic Fidelity contribution is the quotient-level interpretation: **finite multiple positivity is not invariant under a natural zero-preserving gauge, whereas the target discriminator is**. That mismatch is a direct fidelity obstruction and supplies a sharper audit rule for finite positivity evidence.

## Decisive audit rule

When a finite-order positivity condition is proposed as evidence for a zero-set target, first quotient by zero-free exponential factors or otherwise fix that freedom canonically. If the condition can be forced by `F -> e^{az}F` while the zero divisor remains unchanged, the condition is measuring representation-dependent smoothing rather than the target zero geometry.
