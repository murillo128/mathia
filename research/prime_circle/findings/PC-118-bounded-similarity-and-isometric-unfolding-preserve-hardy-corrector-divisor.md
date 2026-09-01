# PC-118 — bounded similarity and isometric unfolding preserve the Hardy-corrector divisor

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` + `DECISIVE-BOUNDARY`. PC-117 proves that for the arbitrary-conductor one-new-prime Hardy corrector

\[
X_{p,q}:=\frac{G_{p,q}}{\sqrt{\varphi(q)}},
\qquad p\nmid q,
\]

one has, along every joint path `p,q -> infinity` with `p` prime,

\[
\det{}_2(I-zX_{p,q})
\longrightarrow
\exp\!\left[-\frac{\gamma-4+5\log2}{2}z^2\right]
\]

locally uniformly on `C`. PC-117 deliberately left conductor-dependent **non-scalar conjugation or unfolding** outside its operator-norm argument. For the spectral-divisor question, however, the conjugation part of that escape is not real: every bounded invertible similarity preserves the complete eigenvalue divisor and both the ordinary and regularized Fredholm determinants exactly, even when the condition number of the conjugating map diverges with the conductor. The same is true for an isometric unfolding into a larger Hilbert space, because it only adds a zero complement.

Thus no conductor-dependent change of coordinates, weighted Hilbert metric, microlocal isometry, or other genuine representation change of the **same** finite corrector can turn the PC-117 zero-free Gaussian determinant into an RH divisor. Such transformations may change operator norms, singular vectors, strong-limit geometry, or the appearance of the kernel, but they cannot change its eigenvalues or determinant zeros. A surviving non-scalar repair must alter the operator rather than merely its representation: for example by a non-similarity left/right weighting, a non-invertible compression/quotient, a genuinely singular domain-changing limit, a nonlinear organization before the PC-113 split, or a different intrinsic operator family.

No historical novelty is claimed for similarity invariance of spectrum, trace ideals, Fredholm determinants, or regularized determinants. The durable Prime-Circle content is the closure of the explicit coordinate-conjugation/unfolding boundary left by PC-117 for the exact geometry-forced Hardy corrector.

## 1. The PC-117 corrector is in the determinant classes needed below

PC-113 gives the exact split

\[
R_{pq}=J_p\otimes R_q+G_{p,q},
\]

where every `R_n` is trace class. Since `J_p` acts on a finite-dimensional factor and `R_q` is trace class,

\[
J_p\otimes R_q\in\mathcal S_1,
\]

and therefore

\[
\boxed{G_{p,q}\in\mathcal S_1\subset\mathcal S_2.}
\]

The scalar-normalized corrector `X_{p,q}` is consequently trace class for every finite `(p,q)`, even though its trace norm need not stay bounded along the conductor limit. Both

\[
\det(I-zX_{p,q})
\quad\text{and}\quad
\det{}_2(I-zX_{p,q})
\]

are therefore defined at every stage.

For the `det_2` limit PC-117 uses only the Hilbert--Schmidt scale, so the argument below is stated at that level and then specialized to the ordinary determinant when useful.

## 2. Arbitrary bounded similarity preserves the entire determinant function

Let `C_{p,q}` be any bounded invertible operator on the finite-conductor Hardy space on which `X_{p,q}` acts. No uniform bound on

\[
\|C_{p,q}\|\,\|C_{p,q}^{-1}\|
\]

is assumed. Define

\[
\boxed{Y_{p,q}:=C_{p,q}X_{p,q}C_{p,q}^{-1}.}
\]

Because Schatten ideals are two-sided operator ideals,

\[
Y_{p,q}\in\mathcal S_1\subset\mathcal S_2.
\]

Similarity preserves every nonzero eigenvalue with algebraic multiplicity. If the eigenvalues of `X_{p,q}` are `lambda_j`, then those of `Y_{p,q}` are exactly the same `lambda_j`. Hence the canonical product definition of the Hilbert--Schmidt regularized determinant gives stagewise

\[
\begin{aligned}
\det{}_2(I-zY_{p,q})
&=
\prod_j(1-z\lambda_j)e^{z\lambda_j}\\
&=
\boxed{\det{}_2(I-zX_{p,q}).}
\end{aligned}
\]

Since the operators are actually trace class, the ordinary Fredholm determinant is likewise exactly invariant:

\[
\boxed{
\det(I-zY_{p,q})
=
\det(I-zX_{p,q}).
}
\]

Equivalently,

\[
I-zY_{p,q}
=C_{p,q}(I-zX_{p,q})C_{p,q}^{-1},
\]

so invertibility, algebraic spectral multiplicity, and the Fredholm zero divisor are all unchanged.

This statement is exact for every finite conductor. It does not become weaker when the condition number of `C_{p,q}` diverges. Such divergence can make `\|Y_{p,q}\|` behave very differently from `\|X_{p,q}\|`, but it cannot move a single eigenvalue or determinant zero.

## 3. Isometric microlocal unfolding also cannot change the divisor

The natural unfoldings used earlier in the Hardy branch are often not square coordinate matrices on a fixed Hilbert space: they embed a finite residue coordinate isometrically into a continuum space of step functions. This does not create an escape either.

Let

\[
J_{p,q}:\mathcal H_{p,q}\longrightarrow\mathcal K_{p,q}
\]

be any isometry, `J_{p,q}^*J_{p,q}=I`, and extend the unfolded operator by zero off the range:

\[
\boxed{
\widehat X_{p,q}:=J_{p,q}X_{p,q}J_{p,q}^*.
}
\]

The orthogonal decomposition

\[
\mathcal K_{p,q}
=\operatorname{Ran}J_{p,q}\oplus(\operatorname{Ran}J_{p,q})^\perp
\]

identifies `\widehat X_{p,q}` unitarily with

\[
X_{p,q}\oplus0.
\]

Therefore its nonzero eigenvalues are again exactly those of `X_{p,q}`, with the same algebraic multiplicities, and

\[
\boxed{
\det{}_2(I-z\widehat X_{p,q})
=
\det{}_2(I-zX_{p,q})
}
\]

for every `z`. The same holds for the ordinary determinant.

This includes pure residue reindexings, Fourier transforms, Chinese-remainder coordinate changes, step-function mesh embeddings, unitary micro/macro splits, and their compositions, provided they are genuinely only coordinate/unfolding maps of the same operator. PC-114 is a useful warning about topology rather than a counterexample: its two-scale unfolding can expose a nontrivial `S_q \otimes K` operator limit that ordinary strong coordinates hide, while the finite-stage nonzero eigenvalue divisor remains the divisor of the original corrector.

## 4. Weighted Hilbert metrics are similarities when the algebraic operator is unchanged

A common proposed non-scalar repair is to change the conductor-dependent Hilbert metric. Let `W_{p,q}>0` be bounded and boundedly invertible and define

\[
\langle u,v\rangle_W
:=\langle W_{p,q}u,v\rangle.
\]

The canonical unitary from this weighted Hilbert space to the original one is

\[
U_{p,q}=W_{p,q}^{1/2}.
\]

If one keeps the **same algebraic corrector** `X_{p,q}`, its representation in the original Hilbert space after this metric change is

\[
\boxed{
U_{p,q}X_{p,q}U_{p,q}^{-1}
=W_{p,q}^{1/2}X_{p,q}W_{p,q}^{-1/2},
}
\]

which is exactly the similarity of Section 2. Consequently a conductor-dependent change of counting measure, residue weights, or equivalent positive Hilbert norm does not change the determinant divisor merely by changing the metric in which the same map is represented.

This distinction matters. The symmetrically preconditioned operator

\[
W_{p,q}^{1/2}X_{p,q}W_{p,q}^{1/2}
\]

is generally **not** a representation of the same linear map under a new inner product; it is a new operator. It may have different eigenvalues, but then the weights are part of the proposed Prime-Circle mechanism and must be derived and falsified as new structure rather than described as an unfolding or coordinate normalization.

## 5. PC-117's Gaussian determinant is therefore similarity-universal

Apply Sections 2 and 3 to the normalized corrector of PC-117. For arbitrary bounded invertible `C_{p,q}`,

\[
\det{}_2\!\left(
I-zC_{p,q}X_{p,q}C_{p,q}^{-1}
\right)
=
\det{}_2(I-zX_{p,q}).
\]

Hence PC-117 immediately implies

\[
\boxed{
\det{}_2\!\left(
I-zC_{p,q}X_{p,q}C_{p,q}^{-1}
\right)
\longrightarrow
\exp\!\left[-\frac{\gamma-4+5\log2}{2}z^2\right]
}
\]

locally uniformly on `C` along every arbitrary-conductor joint path covered there.

Likewise, for every isometric unfolding `J_{p,q}`,

\[
\boxed{
\det{}_2\!\left(
I-zJ_{p,q}X_{p,q}J_{p,q}^*
\right)
\longrightarrow
\exp\!\left[-\frac{\gamma-4+5\log2}{2}z^2\right].
}
\]

The conclusion needs no convergence of the transformed operators themselves and no uniform control of the conjugating maps. The determinant functions are equal **before** the limit is taken.

This is stronger than an operator-norm no-go. A violently ill-conditioned similarity can change norm geometry, pseudospectra, singular vectors, and strong-limit behavior, yet the spectral divisor relevant to a Fredholm/Hilbert--Pólya interpretation is fixed exactly.

## 6. A singular limiting representation does not evade the stagewise divisor statement

There is one subtle boundary. A sequence of similarities with diverging condition number may converge, after embedding, to an operator that is not similar to the original finite-stage family. Its limiting spectrum can differ because spectral convergence under strong or weak topology is not automatic.

That does **not** change the conclusion above about the determinant mechanism. If the proposed spectral entire function is still obtained as

\[
\det{}_2(I-zY_{p,q})
\]

at finite conductor and then passed to a locally uniform limit, the function is exactly the PC-117 determinant at every stage and therefore has the same zero-free Gaussian limit. To use instead the determinant of a new singular strong-limit operator, one must separately prove that such a determinant exists and explain why it, rather than the nonconvergent finite-stage determinant sequence, is the canonical Prime-Circle spectral object.

Thus a singular limit may define a genuinely new operator problem, but it is no longer an escape by **conjugating the PC-117 determinant**. It crosses the boundary into a new domain-changing construction whose analytic category and geometric necessity require independent justification.

## 7. Prior-art and novelty audit

The operator-theoretic facts used here are classical.

- Similarity invariance of spectrum and algebraic multiplicity is standard linear/operator theory.
- For trace-class operators, the Fredholm determinant is the canonical product over eigenvalues and is invariant under bounded similarity. Barry Simon, *Trace Ideals and Their Applications*, 2nd ed., AMS (2005), already anchored in `research/prime_circle/SOURCES.md` for PC-107, is the standard trace-ideal reference.
- The regularized determinant `det_2` is likewise determined by the eigenvalues through the canonical factors `(1-z lambda)e^{z lambda}` and is therefore similarity invariant. The same trace-ideal framework covers this fact.
- Isometric embedding followed by zero extension is merely unitary equivalence to `X \oplus 0`; no special arithmetic theorem is involved.

Directed prior-art searches for Fredholm-determinant similarity invariance and regularized-determinant similarity invariance returned only the standard trace-ideal/operator-theoretic framework, exactly as expected. There is no theorem-level novelty claim here.

The nonclassical content is only the **research consequence for the exact Prime-Circle Hardy branch**: PC-117 had isolated a conductor-dependent non-scalar conjugation/unfolding as one possible remaining escape from its scalar-normalized Gaussian collapse. Once the target is the Fredholm zero divisor, that coordinate part is pure gauge independently of how conductor-dependent or ill-conditioned the representation becomes.

## 8. Falsification boundary and surviving route

The conclusion applies when the purported repair is one of the following:

1. bounded invertible similarity of the finite-stage corrector;
2. unitary coordinate change;
3. isometric embedding with zero extension;
4. replacement of the Hilbert metric while keeping the same algebraic operator.

It does **not** apply to a transformation that actually changes the operator, such as a non-similarity left/right weighting, a non-invertible compression or quotient, a nonlinear functional of several conductors, or an unbounded/domain-changing operation whose output is not similar to the finite corrector. Nor does it classify a completely different intrinsic Prime-Circle operator family.

These exceptions are not loopholes in the proof; they are the exact distinction between changing coordinates and changing mathematics. In particular, a future weighted or preconditioned candidate must derive its asymmetric weights from the Prime-Circle geometry and survive a matched control. Merely choosing weights so that the transformed eigenvalues approach a desired divisor would be an arbitrary spectral wrapper and fail the line mandate.

The Hardy frontier after PC-117 is therefore narrower:

\[
\boxed{
\text{coordinate / metric unfolding of }X_{p,q}
\;\text{cannot alter its RH-relevant divisor}.}
\]

Any surviving non-scalar mechanism must modify the operator before spectral interpretation, not merely reveal the same operator in a conductor-dependent representation.