# PC-356 — source-induced radial Gram metrics remain matched-control isometric

- **Finding ID:** `PC-356`
- **Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE`
- **Research line:** `prime_circle`
- **Result type:** exact Hilbert-metric / operator-theoretic obstruction
- **Scope:** closes the most direct source-induced non-diagonal radial-metric repair left open by PC-355

## Claim

PC-355 showed that the canonical free-Fock realization of the centered Prime-Circle inversion defect is blind to the reciprocal matched control when the centered letters carry a fixed parity-compatible Hilbert metric. A natural objection is that such a metric is too symmetric: the actual cyclotomic radial profiles induce a non-diagonal energy Gram matrix, and that matrix need not commute with the control parity.

That repair still fails when applied fairly to the matched control.

Let `S` be a finite shell set containing shell `2`. On the centered one-particle alphabet

\[
K_S=\operatorname{span}\{c\}\oplus
\operatorname{span}\{b_n:n\in S\setminus\{2\}\},
\]

write

\[
X_n(r)=\log\Phi_n(r),\qquad
W_n(r)=X_n(r)-\varphi(n)X_2(r),\qquad r>0.
\]

Define the radial realization

\[
T_Sc=f_0(r):=X_2'(r)=\frac1{1+r},
\]

and, for `n != 2`,

\[
T_Sb_n=f_n(r):=W_n'(r)
=\frac{\Phi_n'(r)}{\Phi_n(r)}-\frac{\varphi(n)}{1+r}.
\]

The reciprocity cancellation already used in the PC-350--PC-355 chain gives `f_n(r)=O(r^{-2})` as `r -> infinity`, while every `f_n` is bounded at `r=0`; hence all these functions lie in `L^2((0,infinity),dr)`. The Euclidean radial energy Gram form

\[
G_S(u,v):=\langle T_Su,T_Sv\rangle_{L^2(dr)}
\]

is positive definite and, in general, is **not** invariant under the centered parity

\[
Jc=c,\qquad Jb_n=-b_n.
\]

Nevertheless the reciprocal matched control has radial realization

\[
\widetilde T_S=T_SJ,
\]

and therefore induces

\[
\boxed{\widetilde G_S=J^*G_SJ.}
\]

Thus `J` is an isometry from the source one-particle Hilbert space `(K_S,G_S)` to the matched-control Hilbert space `(K_S,\widetilde G_S)`. Its tensor powers, and hence its second quantization, are unitary between the corresponding tensor/Fock Hilbertizations. Combining this with the exact PC-355 algebraic control law

\[
\widetilde{\mathcal D}_S=\theta_J(\mathcal D_S)
\]

shows that the source and matched control remain unitarily intertwined after this source-induced Hilbertization. Spectra, singular values, pseudospectra, numerical ranges, resolvents, and functorial `*`-polynomial spectral data of the associated bounded left-regular constructions still coincide.

The negative conclusion is stronger than saying that the metric accidentally respects parity: it need not. The obstruction is that a metric derived covariantly from the radial source is transported by the same involution that transports the signature.

## 1. The radial energy Gram is genuinely source-dependent and positive definite

For `n>1`, `Phi_n` has no positive real zero and `Phi_n(0)=1`, so all logarithmic derivatives above are real analytic on `(0,infinity)`. The centering by `varphi(n)X_2` removes the `1/r` term at infinity, giving

\[
f_n(r)=O(r^{-2})\qquad(n\ne2),
\]

whereas `f_0(r)=O(r^{-1})`. Hence every Gram integral is finite.

The map `T_S` is injective. Suppose

\[
a_0f_0(r)+\sum_{n\in S\setminus\{2\}}a_nf_n(r)=0
\]

on the positive ray. Since these are rational functions, analytic continuation gives the rational identity

\[
\frac{a_0-\sum_n a_n\varphi(n)}{1+r}
+\sum_n a_n\frac{\Phi_n'(r)}{\Phi_n(r)}=0.
\]

At a primitive `n`-th root of unity, `Phi_n'/Phi_n` has a simple pole of residue `1`. Primitive root sets for distinct `n` are disjoint, and the shell-`2` pole `r=-1` does not occur in any `n != 2` term. Taking residues forces every `a_n=0`, and then `a_0=0`. Therefore

\[
\boxed{G_S=T_S^*T_S>0.}
\]

This is not a coordinate metric imposed after the fact; it is a direct radial Dirichlet/energy metric formed from the centered cyclotomic profiles themselves.

## 2. The `{2,3}` pair proves that the metric itself breaks parity

For shell `3`,

\[
\Phi_3(r)=1+r+r^2,
\qquad
f_3(r)=W_3'(r)
=\frac{r-1}{(1+r)(1+r+r^2)}.
\]

Direct partial-fraction integration yields

\[
G_{00}=\int_0^\infty\frac{dr}{(1+r)^2}=1,
\]

\[
G_{03}=\int_0^\infty f_0(r)f_3(r)\,dr
=\frac{\pi}{\sqrt3}-2\ne0,
\]

and

\[
G_{33}=\int_0^\infty f_3(r)^2\,dr
=5-\frac{8\pi}{3\sqrt3}.
\]

Thus

\[
G_{\{2,3\}}=
\begin{pmatrix}
1 & \pi/\sqrt3-2\\
\pi/\sqrt3-2 & 5-8\pi/(3\sqrt3)
\end{pmatrix},
\]

with

\[
\det G_{\{2,3\}}
=1+\frac{4\sqrt3\pi}{9}-\frac{\pi^2}{3}>0.
\]

For `J=diag(1,-1)`, the nonzero cross term changes sign, so

\[
JG_{\{2,3\}}J\ne G_{\{2,3\}}.
\]

Hence PC-355's blindness is not merely an artifact of having chosen a one-particle metric that commutes with parity.

## 3. Recomputing the same source-native metric on the matched control restores exact isometry

The reciprocal matched control keeps the calibration profile and flips every centered transverse profile:

\[
f_0\mapsto f_0,\qquad f_n\mapsto-f_n.
\]

Therefore its radial realization is exactly `\widetilde T_S=T_SJ`. If the control is subjected to the same construction as the cyclotomic source, its Gram form is

\[
\widetilde G_S
=\widetilde T_S^*\widetilde T_S
=J^*G_SJ.
\]

Consequently, for all `u,v in K_S`,

\[
\langle Ju,Jv\rangle_{\widetilde G_S}
=\langle u,v\rangle_{G_S}.
\]

So `J:(K_S,G_S)->(K_S,\widetilde G_S)` is unitary even though `J` need not be unitary as an endomorphism of the single fixed metric `(K_S,G_S)`.

Taking tensor powers gives a unitary

\[
\Gamma(J)=\bigoplus_{m\ge0}J^{\otimes m}
:
\mathcal F(K_S,G_S)
\longrightarrow
\mathcal F(K_S,\widetilde G_S).
\]

At every finite tensor cutoff this is elementary finite-dimensional Hilbert-space algebra. Combining it with `\widetilde{\mathcal D}_S=\theta_J(\mathcal D_S)` yields unitary equivalence of the corresponding left-regular signature constructions. The non-diagonal metric changes the coordinate adjoint and singular geometry, but it changes them covariantly on the matched control as well.

## 4. The same obstruction covers a larger radial feature class

Let `A` be any fixed bounded radial transform into a Hilbert space `H_A` for which source and control are processed by the same rule, and define

\[
G_{S,A}=T_S^*A^*AT_S.
\]

The control realization is `AT_SJ`, hence

\[
\boxed{\widetilde G_{S,A}=J^*G_{S,A}J.}
\]

The same source/control isometry follows. If the form is only semidefinite, `J` carries the source nullspace to the control nullspace and the statement descends to the Hilbert quotients.

This includes common bounded radial smoothing, bounded integral kernels, finite collections of radial observables, and other Hilbert feature maps applied covariantly after the centered profiles are formed. It does **not** claim a no-go for arbitrary unbounded forms, shell-dependent domains, or geometric structures that are not obtained by applying the same radial feature construction to source and control.

## 5. Why freezing the source metric is not a matched control

One can manufacture a distinction by computing `G_S` from the cyclotomic source once, freezing it, replacing `\mathcal D_S` by `\theta_J(\mathcal D_S)`, and then comparing both operators in the unchanged Hilbert space `(K_S,G_S)`. Since `JG_SJ != G_S` generically, `J` is then no longer unitary and singular/selfadjoint spectral data can change.

But this gives the control an external piece of source-side information that is not recomputed from the control by the same rule. Under the Prime-Circle matched-control criterion this is not a fair control unless there is an independent geometric reason that the frozen metric is part of the common ambient problem rather than a statistic derived from the source being tested.

A successful repair must therefore supply a metric, domain, boundary condition, angular/chord coupling, or other operator datum that is intrinsically fixed by the roots-of-unity geometry **before** the reciprocal profile flip and is not itself transported by `J`. Merely replacing the orthonormal word metric by a source-derived radial Gram matrix does not do this.

## Prior-art and novelty audit

The tensor/Fock Hilbertization and unitary covariance principles are standard operator-theoretic framework, already audited in PC-355. No novelty is claimed for them. The line-local contribution here is the explicit cyclotomic realization `T_S`, the proof that its radial Gram is positive definite and genuinely parity-breaking in fixed coordinates, and the exact conclusion that the same natural construction still restores unitary equivalence when recomputed on the matched control.

The Gram-congruence identity `\widetilde G=J^*GJ` is elementary once the Prime-Circle control involution is identified. A targeted novelty check found no reason to reinterpret this covariance as a new zeta/RH spectral mechanism. This result is therefore deliberately a boundary theorem, not a novelty claim for operator theory.

## Falsification / disproof audit

- **Integrability:** `f_0=O(r^{-1})` and every centered `f_n=O(r^{-2})` at infinity, while all profiles are bounded at zero, so the proposed Gram entries are finite.
- **Definiteness:** disjoint primitive-root pole sets make `T_S` injective, so the Gram is positive definite rather than a quotient artifact.
- **Nontrivial metric:** the exact `{2,3}` cross term `pi/sqrt(3)-2` is nonzero, proving `JGJ != G` for a concrete cyclotomic source.
- **Matched control:** recomputing the same construction after `W_n -> -W_n` gives `\widetilde T=TJ` and `\widetilde G=J^*GJ` exactly.
- **Tensor/Fock lift:** tensor powers of the one-particle isometry intertwine the corresponding left-regular constructions at every finite degree, and hence on the natural completed direct sum whenever the bounded realization is defined.
- **Covariant transforms:** a common bounded radial feature transform `A` merely replaces `G` by `T^*A^*AT` and preserves the same congruence.
- **Frozen-metric escape:** keeping the source Gram fixed while changing only the signature can distinguish source/control, but that is not a matched control unless an independent geometric argument forces the frozen datum.
- **Scope:** no claim is made about a source-forced angular/chord metric, shell-dependent domain, boundary condition, nonlinear cross-shell geometry, or another datum not transported with the radial profiles.
- **RH check:** the construction derives no spectral parameter, zeta-zero equation, gamma factor, functional equation, or critical-line positivity theorem.

## Boundary assessment

PC-355 left open the possibility that the full-Fock obstruction was an artifact of an overly symmetric one-particle Hilbert structure. PC-356 removes the most direct version of that objection. **The actual centered cyclotomic radial profiles induce a positive, non-diagonal Gram metric that can break parity in fixed coordinates, yet the fair matched control induces the congruent metric `J^*GJ`, making the same parity an exact isometry between the two Hilbertized problems.**

Therefore a viable continuation cannot merely ask the radial source to choose its own Hilbert metric and then spectralize the all-depth signature. It must identify additional roots-of-unity geometry that is fixed independently of the reciprocal profile flip and hence cannot be transported away by `J`: for example a genuinely angular/chord coupling, a source-forced domain or boundary condition, or another covariant whose comparison with the control is meaningful in one common ambient geometry. Whether such a datum exists and has any RH strength remains open.