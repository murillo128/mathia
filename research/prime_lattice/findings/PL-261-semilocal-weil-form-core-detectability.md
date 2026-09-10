# PL-261 — Semilocal Weil form cores make every RH failure finitely detectable

**Evidence:** `LITERATURE+DERIVED`

**Status:** `PRIOR-ART-REDIRECT + SHARP-BOUNDARY`

## Claim

The sparse-observability gap left open in `PL-260` is **not a universal limitation of finite-dimensional Weil compression**. Connes--Consani prove that, for every fixed semilocal scale `lambda>1`, the Laurent polynomials form a core for the semilocal Weil quadratic form `QW_lambda`, and that the lower bound of the closed form is the limit of the smallest eigenvalues of the nested finite Laurent compressions `E_N=span{U^k: |k|<=N}`. Combining this with their recalled semilocal Weil criterion gives the direct consequence

\[
\boxed{
\neg RH
\Longrightarrow
\exists\lambda>1\ \exists N_0\ \forall N\ge N_0:
\lambda_{\min}(QW_\lambda|_{E_N})<0.
}
\]

Thus **every** RH failure, including one whose off-line zero divisor is infinite and arbitrarily sparse, is existentially detected by a finite member of this particular source-forced Galerkin family. A sparse defect cannot hide forever from the Connes--Consani Laurent core.

This is not a new RH mechanism and not a Mathia theorem claim. It is a prior-art consequence of the form-core theorem and the Weil positivity criterion. It closes one uncertainty in `PL-260`: the missing problem is no longer whether some canonical finite Weil compression can in principle approximate every negative direction. For this semilocal family, that completeness is already proved. The unsolved burden is to prove the finite forms nonnegative from arithmetic/source structure without assuming RH.

## 1. Exact finite-detectability deduction

For fixed `lambda>1`, Connes--Consani consider the semilocal Weil quadratic form `QW_lambda` on

\[
L^2([\lambda^{-1},\lambda],d^*u).
\]

Their Lemma 2.2 proves that the Laurent polynomial algebra

\[
\mathbb C[U,U^{-1}]
\]

is a core for `QW_lambda`. Proposition 2.3 gives the corresponding lower-semicontinuous closure statement. Most importantly for finite observability, Corollary 2.4 states that if

\[
E_N=\operatorname{span}\{U^k:|k|\le N\},
\]

then the lower bound of `QW_lambda` is

\[
m_\lambda
=
\lim_{N\to\infty}
\lambda_{\min}(QW_\lambda|_{E_N}).
\]

The spaces `E_N` are nested, so the finite minimum eigenvalues are nonincreasing with `N`.

The same paper recalls the semilocal Weil implication

\[
QW_\lambda\ge0\ \text{for every }\lambda>1
\quad\Longrightarrow\quad RH,
\]

while under RH the forms are strictly positive. Hence if RH is false, there is some finite scale `lambda` and some admissible vector `f` for which `QW_lambda(f)<0`. After normalizing `f`, this gives `m_lambda<0`. Corollary 2.4 then yields an `N_0` such that

\[
\lambda_{\min}(QW_\lambda|_{E_N})<0
\qquad (N\ge N_0).
\]

No hypothesis about the number or density of off-line zeros enters this deduction. It therefore covers precisely the sparse-infinite regime that Bombieri's finite-total-defect stabilization, as used in `PL-260`, did not by itself settle.

## 2. What this changes relative to `PL-259` and `PL-260`

`PL-259` isolates a real limitation of the Alpöge--Furman/Lamzouri first/second-moment method: normalized bulk moments can be insensitive to an `o(N)` exceptional set of zeros. `PL-260` then records Bombieri's stronger finite-total statement: exact finite-truncation inertia eventually detects every finite set of off-line zeros, but the stored boundary correctly declined to pass that theorem automatically to an infinite sparse divisor.

The Connes--Consani core theorem supplies the missing **existential completeness statement**, but for a different and explicitly identified nested Galerkin family. It says that if the full semilocal Weil form has any negative direction, Laurent polynomials approximate the form strongly enough that a finite compression eventually inherits a strict negative direction. Therefore the following concern can be retired for this family:

\[
\text{``an infinite sparse RH defect might remain invisible to every finite source-side compression.''}
\]

What cannot be retired is the arithmetic sign problem. The theorem does not provide an unconditional estimate proving

\[
QW_\lambda|_{E_N}\ge0
\]

for every `lambda,N`. Proving that cofinal family positive would amount to proving the corresponding Weil positivity and hence RH. Finite detectability is therefore a completeness result, not a positivity mechanism.

This distinction is useful for the line's current operator target. A successful construction no longer needs a new abstract argument showing that finite Galerkin spaces can see an arbitrary negative Weil direction: one canonical construction already has that property. It needs a **source-forced reason that those finite matrices cannot become negative**.

## 3. Prime-exponent interpretation

The arithmetic input remains the explicit-formula axis skeleton already identified in `PL-013`, `PL-259`, and `PL-260`. For a compact multiplicative support window `[lambda^{-1},lambda]`, the non-archimedean part of the semilocal formula is finite: only prime-power contributions inside the support scale occur. In exponent coordinates these are

\[
v(p^r)=r e_p,
\qquad
\log(p^r)=\langle r e_p,(\log q)_q\rangle=r\log p.
\]

Thus at each fixed `lambda` the finite-detectability theorem is fed by finitely many pieces of the prime-power coordinate rays, together with the pole and archimedean terms of the completed explicit formula. It does **not** use mixed-prime interior vectors of the exponent lattice.

This is a meaningful boundary for the prime-lattice program. If mixed exponent geometry is to contribute something beyond established Weil theory, it must produce an additional sign/rigidity principle that is absent from the axis-ray explicit formula. It cannot be justified merely as a device for making finite truncations complete, because the Laurent-core theorem already provides that completeness without mixed-prime data.

## 4. Analytic-continuation and spectral audit

No Euler product is being continued through `Re(s)=1`. The zeta zeros enter through Weil's completed explicit formula, where meromorphic continuation, the pole, the functional equation, and the archimedean place have already been incorporated. The finite Galerkin statement concerns the closed semilocal quadratic form and its form core, not a formal truncation of an Euler product.

Likewise, the negative finite eigenvalue in this finding should not be reinterpreted as an eigenvalue equal to a Riemann zero. The statement is only

\[
\text{RH failure}
\Longrightarrow
\text{negative direction of a Weil form}
\Longrightarrow
\text{negative eigenvalue of some finite Galerkin compression}.
\]

It is a sign certificate. It neither localizes the offending zero nor reconstructs the divisor, and it does not turn the finite matrix into a Hilbert--Pólya operator.

## 5. Prior-art and novelty audit

Primary source:

- **Alain Connes, Caterina Consani**, “Spectral triples and `zeta`-cycles,” *L'Enseignement Mathématique* **69**(1/2) (2023), 93--148, DOI `10.4171/LEM/1049`; already recorded as source 27 in `research/prime_lattice/SOURCES.md`. Lemma 2.2 proves that `C[U,U^{-1}]` is a core for `QW_lambda`; Proposition 2.3 records the closure approximation; Corollary 2.4 identifies the lower bound with the limit of the smallest eigenvalues on `E_N`. The introduction also states that positivity of `QW_lambda` for all `lambda` implies RH and that RH gives strict positivity.

The finite-detectability implication above is an elementary composition of those published statements. No originality is claimed for the functional-analytic ingredients. The durable line-specific addition is the correction to the boundary left by `PL-260`: **sparse-infinite observability is already guaranteed for the Connes--Consani semilocal Laurent-core family**, even though it remains unresolved for Bombieri's particular truncation scheme and is invisible to the aggregate moment statistics used in `PL-259`.

A targeted repository audit found no stored `PL-*` finding whose main claim is this form-core consequence. `PL-013` cites Connes--Consani as spectral prior art but focuses on small eigenvectors, prolate functions, zeta-cycles, and the gap to a genuine RH spectral realization; it does not record Corollary 2.4 as a universal finite negativity detector. `PL-260` explicitly leaves arbitrary sparse-infinite finite-compression observability as a possible missing completeness theorem. This finding resolves that point only for the named semilocal Galerkin family and must not be generalized to unrelated truncations.

## 6. Adversarial boundaries

1. **The scale is existential.** Failure of RH gives some `lambda`; the result does not give an effective bound for that scale from a hypothetical off-line zero.

2. **The Galerkin dimension is existential.** The form-core theorem gives some `N_0` after which negativity appears, but no useful quantitative estimate for `N_0` is derived here.

3. **Do not transfer cofinality across truncation schemes.** The conclusion is proved for the nested Laurent spaces in Connes--Consani. It does not automatically imply Bombieri's exact negative-index stabilization, Alpöge--Furman's finite matrices, or another finite operator family has the same eventual inertia.

4. **Detectability is not positivity.** The theorem guarantees that a negative full-form direction cannot hide from all finite Laurent compressions. It gives no new reason that such a direction does not exist.

5. **It is not divisor-complete.** A negative eigenvalue certifies failure of Weil positivity but does not identify all off-line zeros or their multiplicities.

6. **It does not activate the mixed prime lattice.** The non-archimedean source remains supported on prime-power axis rays. Any proposed mixed-coordinate mechanism still needs an independent arithmetic derivation and a matched control showing that it adds information rather than re-encoding the completed zeta formula.

## Consequence for the research line

The finite-observability question should now be split by truncation family rather than treated as a generic obstacle. For the Connes--Consani semilocal Weil form, a nested finite source-side core is already complete enough that **every** RH failure forces a finite negative Galerkin eigenvalue. This closes the existential sparse-detection gap left after `PL-260`.

The live problem is sharper: explain, from source-side arithmetic or another source-forced positive structure, why all of these cofinal finite forms should be nonnegative. Any successor proposal that merely constructs another increasingly rich finite basis or argues that finite matrices approximate the Weil form has not advanced RH. A genuinely new mechanism must constrain the **sign** of the finite source-forced form, retain the completed/global ingredients that make the Weil criterion RH-sensitive, and survive the line's Helson/Beurling and zero-insensitive controls.