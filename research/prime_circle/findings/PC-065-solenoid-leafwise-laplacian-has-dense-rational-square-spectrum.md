# PC-065 — canonical solenoid leafwise Laplacian has dense rational-square spectrum

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-STRUCTURE` + `DECISIVE-NEGATIVE` for using the canonical leafwise differential spectrum of the all-level compatible-circle refinement as a new RH mechanism.

## Claim

PC-064 identifies the canonical compatible refinement of the original circle with the universal arithmetic solenoid

\[
\Sigma_{\mathbb Q}
=\varprojlim_{m\mid n}(S^1,z\mapsto z^{n/m})
\cong \widehat{\mathbb Q}
\cong (\mathbb R\times\widehat{\mathbb Z})/\mathbb Z_{\rm diag}.
\]

A natural spectral escape is then to retain its one-dimensional laminated geometry instead of only its compact-group Fourier characters. The original level-one circle fixes a canonical real coordinate on the dense base leaf,

\[
t\longmapsto [(t,0)],
\qquad
\pi_1([(t,0)])=e^{2\pi i t},
\]

and hence a canonical leafwise translation generator. On the Pontryagin character `\chi_q`, `q\in\mathbb Q`,

\[
\chi_q([(t,0)])=e^{2\pi i q t}.
\]

Therefore the positive flat leafwise Laplacian inherited from the original circle is exactly

\[
\boxed{
\Delta_{\rm leaf}\chi_q=(2\pi q)^2\chi_q,
\qquad q\in\mathbb Q.
}
\]

This is not a compact-manifold-type spectral problem. Its point eigenvalues are the rational squares, dense in `[0,\infty)`, with nonzero eigenvalues accumulating at `0`. Consequently:

\[
\boxed{
\sigma(\Delta_{\rm leaf})=[0,\infty),
\qquad
(\Delta_{\rm leaf}+1)^{-1}\ \text{is not compact},
}
\]

and for every `t>0`,

\[
\boxed{
\operatorname{Tr}(e^{-t\Delta_{\rm leaf}})=\infty.
}
\]

The naive spectral-zeta series

\[
\sum_{q\in\mathbb Q\setminus\{0\}}
((2\pi q)^2)^{-s}
\]

has **no half-plane of absolute convergence at all**. Thus the most canonical differential spectralization of the PC-064 solenoid does not produce a trace-class heat kernel, a compact-resolvent eigenvalue sequence, or an intrinsic spectral zeta from which a Riemann-zero mechanism could emerge.

Any repair that orders rational frequencies by numerator/denominator height, inserts finite-adic weights, or suppresses the small rational modes adds a transverse arithmetic scale not supplied by the bare leaf metric. Such a repair may be worth studying only if that extra scale is independently forced by the original prime-circle geometry; it cannot be credited to the canonical solenoidal leafwise Laplacian itself.

## 1. The original circle fixes the leaf generator

PC-064 gives the compact-group exact sequence

\[
0\longrightarrow\widehat{\mathbb Z}
\longrightarrow\Sigma_{\mathbb Q}
\longrightarrow S^1
\longrightarrow0
\]

and the dense base leaf

\[
\iota:\mathbb R\to\Sigma_{\mathbb Q},
\qquad
\iota(t)=[(t,0)].
\]

The normalization is not arbitrary: the level-one projection is exactly the original circle coordinate

\[
\pi_1(\iota(t))=e^{2\pi i t}.
\]

Translations along this leaf define a strongly continuous unitary group on Haar `L^2(\Sigma_{\mathbb Q})`,

\[
(U_t f)(x)=f(x+\iota(t)).
\]

Since

\[
\widehat{\Sigma_{\mathbb Q}}\cong\mathbb Q,
\]

the characters `\{\chi_q:q\in\mathbb Q\}` form an orthonormal basis and satisfy

\[
U_t\chi_q=e^{2\pi i q t}\chi_q.
\]

The self-adjoint generator `A` of this flow and its positive square are therefore

\[
A\chi_q=2\pi q\,\chi_q,
\qquad
\Delta_{\rm leaf}=A^2,
\qquad
\Delta_{\rm leaf}\chi_q=(2\pi q)^2\chi_q.
\]

Equivalently, on finite Pontryagin sums this is the ordinary second derivative along each dense real leaf. Its closure is the diagonal self-adjoint operator with domain

\[
\mathcal D(\Delta_{\rm leaf})
=
\left\{
\sum_q a_q\chi_q:
\sum_q (2\pi q)^4|a_q|^2<\infty
\right\}.
\]

Thus no speculative operator wrapper is being chosen here: this is the direct flat leafwise differential operator selected by the compatible covers and the original circle scale.

## 2. Refinement creates arbitrarily soft modes

At a finite `n`-cover, the ordinary Fourier modes are indexed by integers `k`. Under the PC-064 direct-limit identification, the `k`-th mode at level `n` represents

\[
q=\frac{k}{n}\in\mathbb Q.
\]

Hence increasing the refinement level does not merely add higher frequencies. It also adds nonzero modes

\[
q=\frac1n
\]

whose leafwise energies are

\[
\lambda_{1/n}=\frac{(2\pi)^2}{n^2}\longrightarrow0.
\]

This is the opposite of the compact elliptic situation in which eigenvalues escape to infinity and only finitely many modes lie below a fixed energy. Here every neighborhood of zero contains infinitely many mutually orthogonal nonconstant eigenfunctions.

Because `\mathbb Q` is dense in `\mathbb R`, the eigenvalue set

\[
\{(2\pi q)^2:q\in\mathbb Q\}
\]

is dense in `[0,\infty)`. The operator is diagonal in a complete orthonormal basis, so its operator spectrum is the closure of its diagonal values:

\[
\boxed{
\sigma(\Delta_{\rm leaf})=[0,\infty).
}
\]

Every nonzero rational-square eigenvalue has the expected `q\leftrightarrow -q` multiplicity, but the decisive feature is not multiplicity: it is accumulation of point spectrum at every nonnegative energy and, in particular, at zero.

## 3. The resolvent is not compact and the heat operator is not trace class

On the character basis,

\[
(\Delta_{\rm leaf}+1)^{-1}\chi_q
=
\frac{1}{1+(2\pi q)^2}\chi_q.
\]

Taking `q=1/n`,

\[
\frac{1}{1+(2\pi/n)^2}\longrightarrow1.
\]

A compact diagonal operator must send any orthonormal sequence weakly converging to zero to a norm-null sequence. The orthonormal modes `\chi_{1/n}` violate this immediately. Therefore

\[
\boxed{
(\Delta_{\rm leaf}+1)^{-1}\ \text{is not compact}.
}
\]

The same soft modes kill the heat trace. For every `t>0`,

\[
\sum_{q\in\mathbb Q}e^{-t(2\pi q)^2}
\ge
\sum_{n\ge1}e^{-t(2\pi/n)^2}.
\]

The terms on the right tend to `1`, so

\[
\boxed{
\operatorname{Tr}(e^{-t\Delta_{\rm leaf}})=\infty
\qquad(t>0).
}
\]

Thus there is no ordinary compact-resolvent heat-trace package to Mellin-transform into a spectral zeta. Compactness of the underlying solenoid does not repair this, because the operator is elliptic only in the dense leaf direction and does not penalize transverse refinement.

## 4. The naive spectral zeta has no convergence half-plane

Remove the constant mode and formally write

\[
Z_{\rm leaf}(s)
=
\sum_{q\in\mathbb Q\setminus\{0\}}
((2\pi q)^2)^{-s}.
\]

Let `\sigma=\Re s`. Absolute convergence would require convergence of every subseries. The integer modes give

\[
\sum_{n\ge1}((2\pi n)^2)^{-\sigma}
\asymp
\sum_{n\ge1}n^{-2\sigma},
\]

which requires

\[
\sigma>\frac12.
\]

But the reciprocal modes give

\[
\sum_{n\ge1}((2\pi/n)^2)^{-\sigma}
\asymp
\sum_{n\ge1}n^{2\sigma},
\]

which requires

\[
\sigma< -\frac12.
\]

No `\sigma` satisfies both conditions. Therefore

\[
\boxed{
Z_{\rm leaf}(s)
\text{ has no domain of ordinary absolute convergence.}
}
\]

For real `s` one of these positive subseries already diverges, so there is not even an unordered positive spectral sum to continue from a genuine convergence region. A zeta regularization can of course be imposed after choosing an ordering or damping of `\mathbb Q`, but that additional choice is precisely where new arithmetic information would enter.

## 5. Why denominator or height regularization is extra structure

The rational label `q=a/b` carries several possible arithmetic sizes—`|q|`, denominator `b`, projective height `\max(|a|,b)`, prime-adic valuations, or combinations of them. The leaf metric sees only the real frequency `|q|`. It therefore makes

\[
1/n\to0
\]

cheap rather than expensive and cannot distinguish a mode of very large denominator from an ordinary small real frequency.

One can obtain discrete counting laws by replacing the leaf energy with, for example, a height-dependent quantity. But this changes the operator. It introduces a transverse metric/weight on the profinite fiber `\widehat{\mathbb Z}` or on the rational character group. Grouping by denominator can then manufacture divisor sums, Euler products, or Dirichlet series, but those factors arise from the chosen arithmetic height and not from `\Delta_{\rm leaf}`.

This distinction is important for the RH program. A nontrivial transverse weight is not forbidden, but it must be derived from another exact prime-circle structure—primitive birth labels, a genuinely cross-level energy, a shell-dependent nonlocal operator, or another intrinsic datum. Choosing a height because it produces `\zeta(s)` would be exactly the arbitrary spectral-wrapper failure mode that the research line excludes.

## 6. Prior art and novelty audit

No historical novelty is claimed for the universal solenoid, its rational Pontryagin modes, leafwise differentiation, or general leafwise Hodge theory.

- Juan M. Burgos and Alberto Verjovsky, **Adelic solenoid I: Structure and topology**, arXiv:1603.05676 (2016; later revisions), develop the universal arithmetic solenoid as the inverse-limit / adelic object used in PC-064.
- Juan M. Burgos and Alberto Verjovsky, **Adelic solenoid II: Ahlfors-Bers theory**, arXiv:1908.00970 (2019), use rational Pontryagin modes in solenoidal analysis and explicitly encounter the small-divisor phenomenon caused by the availability of arbitrarily small nonzero rational frequencies.
- Vicente Muñoz and Ricardo Pérez-Marco, **Hodge theory for Riemannian solenoids**, in *Functional Equations in Mathematical Analysis*, Springer (2011), 633–657; arXiv:1004.4120, develop leafwise differential forms, harmonic theory and `L^2` Hodge theory for measured Riemannian solenoids.
- Alberto Verjovsky, **Adelic Loop Groups and Perfectoid Analogies: Factorization and Holomorphic Bundles on the Adelic Projective Line**, arXiv:2607.10447 (11 July 2026), again makes the rational Fourier/Wiener algebra of the universal solenoid explicit; it is a current prior-art boundary for treating `\mathbb Q`-indexed fine frequency as newly discovered structure.

The project-specific exact consequence is the obstruction obtained by applying the original circle's flat leaf scale to the already identified PC-064 completion:

\[
\boxed{
\text{all compatible circle covers}
\Rightarrow
\mathbb Q\text{-frequencies}
\Rightarrow
\text{eigenvalues }(2\pi q)^2
\Rightarrow
\text{zero accumulation and no heat/spectral zeta trace}.
}
\]

Targeted searches did not identify this exact statement as an RH criterion or prime-circle result, but it is an immediate consequence of classical solenoidal Fourier analysis. Its value here is as a negative classification, not as a novelty claim.

## 7. Boundaries of the obstruction

PC-065 rules out only the most canonical **leafwise flat differential spectrum** of the PC-064 compatible-circle completion and any spectral determinant/zeta that presupposes compact-resolvent or trace-class heat behavior for that operator.

It does **not** rule out:

- an operator with a transverse term on `\widehat{\mathbb Z}` whose scale is independently forced by primitive/birth geometry;
- a genuinely nonlocal operator that couples archimedean leaf motion and finite-adic refinement before diagonalization;
- shell-dependent weights that preserve more than the bare compact-group completion;
- nonlinear metric or uniformization data not determined by the solenoid group law;
- finite-level cross-scale operators before passage to the inverse limit;
- or the global primitive-root uniformization/accessory branch of PC-017.

The constraint is sharper than PC-064's statement that the compact inverse limit is classical: even after retaining its natural laminated differential geometry, the unweighted leafwise spectrum is **too noncompact at low energy** to provide the usual spectral-zeta architecture. A surviving solenoidal route must explain, from prime-circle geometry itself, what penalizes transverse denominator growth.

## 8. Exact audit tests

The finding has direct falsifiers:

1. verify under the PC-064 duality that the character labelled `q=k/n` restricts to `e^{2\pi iqt}` on the base leaf;
2. apply the leaf translation generator and recover `A\chi_q=2\pi q\chi_q` and `\Delta_{\rm leaf}\chi_q=(2\pi q)^2\chi_q`;
3. use `q=1/n` to verify nonzero eigenvalues accumulate at zero;
4. test compactness of the resolvent on the orthonormal sequence `\chi_{1/n}`;
5. test the heat trace against the divergent positive subseries `\sum_n e^{-t(2\pi/n)^2}`;
6. split the formal spectral-zeta series into `q=n` and `q=1/n` subseries and verify their incompatible absolute-convergence requirements `\Re s>1/2` and `\Re s<-1/2`;
7. check that any proposed regularization which restores discreteness explicitly supplies a denominator/height/transverse weight absent from the flat leaf operator.

Failure of items 1–6 would invalidate the exact obstruction. A future spectral route can evade it only by deriving additional transverse or cross-level structure rather than by reordering the same rational-square spectrum.