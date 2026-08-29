# WP-010 — Nyman totality yields only tautological projection positivity; the canonical defect is zero-driven

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the direct Nyman/Gram/projection/Schur-complement positivity route.

## Claim

`PL-017` identifies a precise classical realization of the Prime-Lattice exponent semigroup inside the Nyman–Beurling–Báez-Duarte Hilbert-space criterion. Let

\[
M\subset L^2((0,1],dx)
\]

be Bagchi's step-function Hilbert space, let `g_l` be the integer-indexed Nyman vectors, and set

\[
K=\overline{\operatorname{span}}\{g_l:l\ge1\}\subset M.
\]

Bagchi's formulation gives

\[
\boxed{\mathrm{RH}\iff 1\in K\iff K=M.}
\tag{1}
\]

The natural Hilbert-geometric positivity attached to this subspace does **not** explain Weil positivity. If `P=P_K` is the orthogonal projection onto `K`, then

\[
D:=I-P\ge0,
\qquad
\mathcal E_K(f):=\langle f,Df\rangle=\|(I-P)f\|^2\ge0
\tag{2}
\]

for every closed subspace of every Hilbert space, independently of any arithmetic input. Equation (1) makes RH equivalent not to this positivity, which is automatic, but to the **vanishing** of the defect:

\[
\boxed{\mathrm{RH}\iff D=0.}
\tag{3}
\]

Likewise one may manufacture the self-adjoint involution

\[
J:=2P-I
\tag{4}
\]

and its quadratic form

\[
q_K(f)=\langle f,Jf\rangle
      =\|Pf\|^2-\|(I-P)f\|^2.
\tag{5}
\]

Then, for purely Hilbert-space reasons,

\[
\boxed{q_K\ge0\text{ on }M\iff K=M.}
\tag{6}
\]

Indeed, if `K=M`, then `J=I`. If `K` is proper, choose `0\ne f\in K^\perp`; then `q_K(f)=-\|f\|^2<0`. Combining (1) and (6) gives an RH-equivalent positivity criterion, but one that is completely tautological: the same construction converts **any** closed-subspace totality problem into a positivity problem.

Finite Gram matrices and their Schur complements do not escape this obstruction. For

\[
V_N=\operatorname{span}\{g_1,\ldots,g_N\},
\]

the Gram matrix of the `g_l` is positive semidefinite unconditionally, and the Schur complement in the Gram matrix of `(1,g_1,...,g_N)` is exactly the squared distance

\[
d_N^2=\operatorname{dist}(1,V_N)^2\ge0.
\tag{7}
\]

The hard statement is again the limiting **zero** condition

\[
\boxed{\mathrm{RH}\iff \inf_N d_N=0,}
\tag{8}
\]

not positivity of any finite Gram or Schur-complement form.

There is also a sharp classical control. For the original **continuous** Nyman subspace `NB`, Jean-François Burnol proves that under the Mellin transform

\[
NB=B H^2,
\tag{9}
\]

where `B` is the Blaschke product over zeta zeros with `Re(rho)>1/2`, and that if `P_{NB}` denotes orthogonal projection then

\[
\boxed{
\|P_{NB}1\|
=
\prod_{\zeta(\rho)=0,\ \Re\rho>1/2}
\left|\frac{1-\rho}{\rho}\right|.
}
\tag{10}
\]

Consequently the canonical positive projection defect satisfies

\[
\|(I-P_{NB})1\|^2
=
1-
\prod_{\Re\rho>1/2}
\left|\frac{1-\rho}{\rho}\right|^2.
\tag{11}
\]

For every zero with `Re(rho)>1/2`,

\[
|\rho|^2-|1-\rho|^2=2\Re\rho-1>0,
\]

so each factor in (10) is strictly below one. Thus this nearby canonical positive Hilbert defect is quantitatively controlled by the **off-critical zero divisor itself**; it vanishes under RH rather than providing an independent geometric theorem that forces RH.

Therefore the direct route

```text
PL-017 prime-exponent dilation lattice
    -> Nyman Hilbert subspace
    -> positive Gram / projection / Schur complement
    -> Weil-type positivity
```

is closed. The positivity is either universal Hilbert geometry with RH hidden in a vanishing/totality condition, or — in Burnol's continuous projection formula — is already measured explicitly by the prohibited off-critical zero data. Neither supplies the finite-prime plus archimedean/polar local-to-global decomposition required by the Weil-positivity research target.

## 1. The projection defect is positive for every closed subspace

Let `H` be any Hilbert space and `K` any closed subspace. The orthogonal projection `P_K` satisfies

\[
P_K=P_K^*=P_K^2.
\]

Hence

\[
I-P_K=(I-P_K)^*=(I-P_K)^2
\]

is itself an orthogonal projection, so

\[
\langle f,(I-P_K)f\rangle=\|(I-P_K)f\|^2\ge0.
\]

No arithmetic statement is used. In particular, inserting the Nyman subspace into this lemma cannot make positivity evidence for RH; the only arithmetic content is whether the positive operator happens to be zero.

For Bagchi's `K`, equation (1) gives

\[
K=M\iff P_K=I\iff I-P_K=0.
\]

Thus the most canonical positive operator in the Nyman geometry turns the target into a **defect-vanishing problem**. That is a valid RH reformulation but not the sought mechanism: there is no theorem saying a nontrivial arithmetic energy must be nonnegative and thereby forcing a Weil inequality. Nonnegativity was present before the arithmetic subspace was chosen.

## 2. Converting totality into positivity with `2P-I` is universal and circular

One might object that (2) has the wrong logical orientation and use the signed reflection `J=2P-I` instead. This yields exactly the desired logical shape,

\[
J\ge0\iff K=M,
\]

but only because an orthogonal reflection has eigenvalue `+1` on `K` and `-1` on `K^\perp`.

This gives a useful falsification principle for the research line:

> If a proposed positivity criterion is obtained from an already RH-equivalent totality statement merely by applying a universal functional calculus to its projection, then the sign is not an independent geometric theorem; the hard statement has just been moved into the assertion that the negative spectral subspace is absent.

The same critique applies to `I-c(I-P)` for any fixed `c>1`, to signatures built from the decomposition `K\oplus K^\perp`, and to equivalent projection-reflection packages. They are mechanically available for every totality problem.

## 3. Finite Gram and Schur-complement positivity also has no RH content

Take finitely many vectors `g_1,...,g_N`. Their Gram matrix

\[
G_N=(\langle g_i,g_j\rangle)_{i,j=1}^N
\]

is positive semidefinite simply because

\[
c^*G_Nc=\left\|\sum_i c_i g_i\right\|^2\ge0.
\]

Now form the block Gram matrix for `(1,g_1,...,g_N)`:

\[
\Gamma_N=
\begin{pmatrix}
\|1\|^2 & b^*\\
b & G_N
\end{pmatrix}
\ge0,
\qquad
b_i=\langle g_i,1\rangle.
\tag{12}
\]

When `G_N` is invertible, the scalar Schur complement is

\[
\|1\|^2-b^*G_N^{-1}b
=\|1-P_{V_N}1\|^2
=d_N^2\ge0.
\tag{13}
\]

With linear dependencies, the Moore–Penrose inverse gives the same projection formula. Again, every finite stage is positive for every vector family. The Nyman criterion concerns whether these positive defects tend to zero as the span becomes dense.

Therefore neither a positive Nyman Gram matrix nor a positive Schur complement can be advertised as Mathia-native Weil positivity unless an additional structure produces a nontrivial signed/global form whose positivity is not an automatic Gram theorem.

## 4. Burnol's continuous Nyman projection makes the zero-data dependence explicit

Burnol's theorem provides a particularly strong novelty and circularity control because it computes the projection norm itself for the original continuous Nyman subspace.

After Mellin transformation, the relevant Hardy-space subspace is the invariant subspace `B H^2`, with `B` the Blaschke product formed from precisely the zeta zeros in `Re(s)>1/2`. The projection of the target vector is correspondingly controlled by `B`, yielding (10).

This has two consequences for the present question.

First, canonical positive projection geometry in the classical Nyman setting is already known prior art. A Mathia construction that merely rediscovers it is not a new geometric explanation.

Second, its quantitative defect is **downstream of the off-line zeros**. Formula (11) can measure the failure of RH, but it does not establish the absence of that failure from an independent positivity theorem. Under RH the Blaschke product is empty and the defect collapses to zero.

This is almost the opposite of the desired Weil mechanism: the research target seeks a positive geometric object existing independently whose decomposition forces the arithmetic inequality. Burnol's projection defect instead records how far an RH-equivalent approximation space fails to be total, with the failure explicitly parameterized by the forbidden zero divisor.

## 5. No finite/archimedean Weil decomposition is generated

`WP-004` was useful because the Prime-Lattice axis compression generated, without zeta zeros,

\[
\frac{\Lambda(n)}{\sqrt n}
\]

on exactly the prime-power support. The Nyman construction has a different virtue: it packages RH as cyclicity/totality for an arithmetic Hilbert subspace and realizes the multiplicative semigroup through dilations.

But the projection forms above do not themselves decompose into

```text
finite prime-power term
+ archimedean gamma term
+ pole / normalization term
```

with those pieces forced by one geometric object. In Bagchi's Mellin formulation the generators already involve

\[
G_l(s)=\frac{(l^{-s}-l^{-1})\zeta(s)}{s},
\]

so passing from the totality criterion to a projection reflection does not derive the explicit formula's local terms; it simply starts from an RH-equivalent zeta-dependent subspace.

This distinguishes the present no-go from `WP-004`/`WP-005`: the Nyman route has a genuine global Hilbert structure, but its ordinary positivity is universal and its arithmetic content sits in totality. It therefore does not supply the missing sign theorem that the exact finite Prime-Lattice weights lacked.

## 6. Prior art and novelty assessment

- Nyman and Beurling give the original `L^2` closure criterion for RH.
- Báez-Duarte proves the integer-indexed strengthening.
- Bagchi organizes the criterion in the exact semigroup/Hardy/Mellin form used by `PL-017`, including RH as totality of the integer Nyman family.
- Burnol computes the projection of the constant function onto the continuous Nyman subspace and identifies its Mellin image through the Blaschke product of off-critical zeros.
- Positivity of orthogonal projections, Gram matrices, and Schur complements is standard Hilbert-space linear algebra.

No novelty is claimed for any of those components. The durable Mathia-specific conclusion is the adversarial synthesis: **the newly explicit Prime-Lattice/Nyman bridge does not open a new positivity route**, because every direct Hilbert-positive form it suggests is either universal or quantitatively zero-driven, while the actual RH content remains totality/vanishing.

## 7. Boundary conditions and audit tests

### Continuous versus integer-indexed Nyman spaces

Burnol's projection formula concerns the original continuous Nyman subspace. `PL-017` uses Bagchi/Báez-Duarte's integer-indexed subspace `K`. This finding does **not** assert that their orthogonal projections are unconditionally identical, nor does it transfer formula (10) to the discrete `K`.

The exact no-go for the discrete `K` needs no such identification: equations (2), (3), (6), and the finite Gram/Schur argument follow directly from the totality criterion and Hilbert geometry. Burnol is used as a close classical control showing what the canonical projection geometry looks like in the continuous formulation and where zero data enter quantitatively.

### Falsification tests

The finding would be falsified or materially weakened if any of the following failed:

1. Bagchi's integer criterion were not `RH iff K=M` for the stated `K`;
2. the projection/reflection lemma (6) failed for a proper closed subspace;
3. the Schur complement (13) were not the squared distance to the finite span;
4. Burnol's theorem did not identify the continuous Nyman projection norm with the product over zeros in `Re(rho)>1/2`.

A future construction **escapes** rather than falsifies this result if it uses Nyman/Prime-Lattice data inside a larger geometric object whose positivity is a non-universal theorem and whose local-to-global decomposition independently produces the finite and archimedean Weil terms. Merely changing basis, taking another Gram matrix, or applying functional calculus to `P_K` does not escape.

## Consequence for the research line

The `PL-017` discovery materially narrows the remaining search. The multiplicative lattice already has a classical global Hilbert realization, and RH already appears there as totality. But ordinary Hilbert-space positivity cannot bridge the remaining gap:

```text
prime-exponent lattice
    -> Nyman dilation semigroup                         [PL-017]
    -> closed arithmetic subspace K
    -> projection / Gram / Schur positivity            [automatic]
    -> RH only through K=M or defect -> 0               [hard part unchanged]
```

So the next viable global mechanism must do something stronger than convert cyclicity into a positive norm. It must produce a **non-universal geometric sign theorem** whose own decomposition retains the exact finite Prime-Lattice weights, forces the archimedean/polar counterterms, and is not equivalent by construction to the absence of an orthogonal complement or to a zero-supported Blaschke factor.