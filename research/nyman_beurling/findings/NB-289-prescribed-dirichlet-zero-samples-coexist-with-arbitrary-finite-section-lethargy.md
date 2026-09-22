# NB-289 — prescribed Dirichlet zero samples coexist with arbitrary finite-section lethargy

- **Date:** 2026-09-22
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-282, NB-284, NB-287, NB-288
- **Classification:** `EXACT-DERIVED + MATCHED-NONARITHMETIC-CONTROL + FIRST-FREE-SAMPLING + DIRICHLET-ZERO-SAMPLES + SEMIGROUP-SAMPLE-ALGEBRA + TRIANGULAR-GENERATOR-GRAFTING + ARBITRARY-LETHARGY + METRIC-COUPLING-NECESSARY + NEGATIVE-CONTROL + ROUTE-NARROWING + PRIOR-ART-AUDITED`

## Claim

The negative control in `NB-288` survives after one imposes the **exact reduced first-free zero-sample vector of every future Dirichlet atom**. Hence the raw pointwise algebra of the Dirichlet samples, including their exact multiplicative semigroup identity, cannot by itself force a quantitative finite-section rate.

More precisely, let

\[
V_{N_0}\subset V_{N_0+1}\subset\cdots\subset H,
\qquad
\dim(V_{n}\ominus V_{n-1})=1,
\]

be nested finite-dimensional sections in a Hilbert space, let

\[
L:H\to\mathbb C^d
\]

be bounded and onto on `V_(N_0)`, and let `y in C^d` be fixed. Write `P_n` for the orthogonal projection onto `V_n` and

\[
K_n=LP_nL^*,
\qquad
\mathcal C_n=y^*K_n^{-1}y.
\]

For **any prescribed sequence** of vectors

\[
u_n\in\mathbb C^d,
\qquad n>N_0,
\]

there exist generators `phi_n in V_n` satisfying simultaneously

\[
\boxed{L\phi_n=u_n}
\tag{1}
\]

and

\[
\boxed{
V_n=V_{N_0}+\operatorname{span}
\{\phi_{N_0+1},\ldots,\phi_n\}
}
\tag{2}
\]

for every `n>N_0`.

Consequently, prescribing the complete future sample table does not change any section projector `P_n`, any sampling Gram `K_n`, any minimum-norm interpolation cost `C_n`, or the genuine finite-section excess isolated in `NB-284`--`NB-287`.

Applying this triangular grafting to the arbitrary-lethargy systems of `NB-288` shows that, for any strictly decreasing sequence

\[
a_n\downarrow0,
\]

one can have

\[
\boxed{
\mathfrak A_n
:=\mathcal C_n-\mathcal C_\infty
=a_n
}
\tag{3}
\]

while every future generator has any chosen pointwise sample vector.

In particular, for a zero packet

\[
Z=\{\rho_1,\ldots,\rho_d\}
\]

one may impose the actual reduced Dirichlet first-free samples from `NB-282`,

\[
\boxed{
u_Z(n)
=
\bigl(n^{-\rho_j}-n^{-1}\bigr)_{j=1}^d,
\qquad n>N_0.
}
\tag{4}
\]

Thus arbitrary finite-section lethargy is compatible with the exact future zero-sample table of the Dirichlet monomials `n^{-s}`.

The control does **not** preserve the canonical Nyman generator Gram, generator norms, dilation operators, or source-space metric relations. That failure is the point of the result: a successful rate estimate must use some coupling between the arithmetic sample table and the canonical Nyman Hilbert geometry. The sample values alone, even with their exact multiplicative identities, are insufficient.

## 1. Triangular sample-grafting lemma

Choose unit vectors

\[
\psi_n\in V_n\ominus V_{n-1},
\qquad n>N_0.
\]

Since `L|_(V_(N_0))` is onto a finite-dimensional space, choose a bounded right inverse

\[
R_0:\mathbb C^d\to V_{N_0},
\qquad LR_0=I_{\mathbb C^d}.
\]

For an arbitrary desired sample vector `u_n`, define

\[
\boxed{
\phi_n
=
\psi_n+R_0\bigl(u_n-L\psi_n\bigr).
}
\tag{5}
\]

Then

\[
L\phi_n
=L\psi_n+u_n-L\psi_n
=u_n,
\]

which proves (1).

The correction term in (5) lies in

\[
V_{N_0}\subseteq V_{n-1}.
\]

Therefore

\[
\phi_n-\psi_n\in V_{n-1}.
\]

It follows in both directions that

\[
\operatorname{span}(V_{n-1},\phi_n)
=
\operatorname{span}(V_{n-1},\psi_n)
=V_n.
\tag{6}
\]

Induction gives (2).

This is an invertible unit-diagonal triangular change of generators relative to the nested filtration. It changes the visible sample vector of each newly introduced generator while leaving the generated section **exactly** unchanged.

There is also a harmless scaled form. For any nonzero scalar `lambda_n`,

\[
\phi_n
=
\lambda_n\psi_n
+R_0\bigl(u_n-\lambda_nL\psi_n\bigr)
\tag{7}
\]

still satisfies `L phi_n=u_n` and generates the same one-dimensional quotient `V_n/V_(n-1)`. The unit choice in (5) is enough for the present control.

## 2. Every finite-section quantity from NB-284--NB-288 is preserved

The construction changes a generator list, not the nested subspaces. Hence the orthogonal projectors satisfy exactly the same identities before and after grafting:

\[
P_n^{\rm graft}=P_n.
\]

Since the sampling map `L` and datum `y` are also unchanged,

\[
K_n^{\rm graft}
=LP_n^{\rm graft}L^*
=LP_nL^*
=K_n.
\tag{8}
\]

Therefore

\[
\mathcal C_n^{\rm graft}
=y^*(K_n^{\rm graft})^{-1}y
=\mathcal C_n,
\tag{9}
\]

and similarly the infinite closed source space, infinite minimum cost, and genuine finite-section excess are unchanged:

\[
\boxed{
\mathfrak A_n^{\rm graft}=\mathfrak A_n.
}
\tag{10}
\]

The same is true of the source minimizer

\[
h_n=P_nL^*K_n^{-1}y,
\]

the missing representer Gram `E_n` of `NB-285`, and the total Parseval tail of `NB-287`.

The individual orthogonalized innovations obtained by Gram--Schmidt from the **new** generator list are also unchanged up to phase when the unit-diagonal choice (5) is used. Indeed, subtracting the old section removes the correction in `V_(n-1)` and leaves precisely `psi_n`. Thus the orthogonal source innovation remains `psi_n`.

The neutralized null innovation of `NB-287` is therefore the same vector as before:

\[
q_n^{\rm graft}=q_n.
\tag{11}
\]

Consequently its target coefficient and the telescoping energy drop remain exactly

\[
|\langle h_{n-1},q_n\rangle|^2
=
\mathcal C_{n-1}-\mathcal C_n.
\tag{12}
\]

So the control does not merely preserve the endpoint costs. It preserves the entire future null-innovation energy profile that `NB-287` identified as the exact finite-section obstruction.

## 3. Grafting the exact Dirichlet zero-sample table

For the finite Dirichlet polynomial notation of `NB-282`,

\[
P(s)=\sum a_n n^{-s},
\qquad
Q_P(s)=P(s)-P(1),
\]

the reduced first-free information at a packet of zeros is carried by the values

\[
Q_P(\rho_j).
\]

A single monomial `n^{-s}` therefore contributes the vector

\[
u_Z(n)
=
\bigl(n^{-\rho_j}-n^{-1}\bigr)_{j=1}^d.
\tag{13}
\]

Set `u_n=u_Z(n)` in (5) for every `n>N_0`. Then the synthetic generator `phi_n` has **exactly** the same reduced first-free zero samples as the true Dirichlet atom labelled by `n`:

\[
L\phi_n
=
\bigl(n^{-\rho_j}-n^{-1}\bigr)_{j=1}^d.
\tag{14}
\]

For zeros of multiplicity `m_j`, the physical first source-dependent jet used in `NB-281`--`NB-283` differs from this reduced coordinate by a fixed nonzero diagonal factor involving `zeta^(m_j)(rho_j)/rho_j` and the chosen normalization. Prescribing the reduced samples is therefore equivalent, packet by packet, to prescribing the physical first-free jet samples after an invertible diagonal change of sample coordinates. The grafting lemma works in either coordinate system.

This observation is stronger than imposing merely the rank or span of the sample vectors. The complete numerical table

\[
\{u_Z(n):n>N_0\}
\]

is reproduced exactly.

## 4. Exact multiplicative sample algebra also survives

The reduced Dirichlet sample vectors satisfy an exact coordinatewise semigroup relation. Define

\[
D_Z(m)
=
\operatorname{diag}
\bigl(m^{-\rho_1},\ldots,m^{-\rho_d}\bigr).
\]

Then

\[
\boxed{
u_Z(mn)
=
D_Z(m)u_Z(n)+n^{-1}u_Z(m).
}
\tag{15}
\]

Indeed, in the `j`th coordinate,

\[
\begin{aligned}
m^{-\rho_j}
\bigl(n^{-\rho_j}-n^{-1}\bigr)
+n^{-1}\bigl(m^{-\rho_j}-m^{-1}\bigr)
&=(mn)^{-\rho_j}-(mn)^{-1}.
\end{aligned}
\]

Therefore, whenever `m,n>N_0`, all three labels `m,n,mn` lie in the grafted tail and their synthetic generators satisfy through `L` exactly the same relation:

\[
\boxed{
L\phi_{mn}
=
D_Z(m)L\phi_n+n^{-1}L\phi_m.
}
\tag{16}
\]

Thus even the exact multiplicative identities among the future **sample vectors** do not constrain the finite-section excess. They coexist with any lethargy profile supplied by `NB-288`.

This statement is deliberately limited to sample algebra. It does not assert a source-space operator identity such as the actual Bagchi dilation law

\[
A_mg_j=\sqrt m\,(g_{mj}-j^{-1}g_m),
\]

which is the stronger structure used by `CLUE-visible-semigroup-defect-controls-section-enrichment`. The synthetic control need not possess any operator `A_m` implementing (16) isometrically on the source space.

Hence `NB-289` does not resolve or refute that accepted clue. It separates two levels of information:

\[
\text{exact semigroup identities after sampling}
\]

from

\[
\text{semigroup identities coupled to the canonical source norm and dilation geometry}.
\]

Only the second level can potentially distinguish the real Nyman system from this control.

## 5. Arbitrary lethargy with canonical-looking samples

Now start from the system constructed in `NB-288` for an arbitrary profile

\[
a_{N_0}>a_{N_0+1}>\cdots>0,
\qquad a_n\downarrow0,
\]

with

\[
\mathfrak A_n=a_n,
\]

uniformly positive and uniformly conditioned sampling Grams, bounded optimal right inverses, and one-dimensional sample-visible enrichments.

Apply the grafting lemma using the Dirichlet table (13). Equations (8)--(12) show that all of the benign conditioning properties and the entire prescribed excess profile survive unchanged, while (14) makes every future raw sample vector identical to the Dirichlet one.

Thus one may have simultaneously:

1. the exact reduced Dirichlet zero sample `n^(-rho_j)-n^(-1)` for every future labelled atom;
2. the exact multiplicative sample identity (15) throughout the tail;
3. uniformly well-conditioned finite sampling Grams and uniformly bounded optimal sample repair;
4. every enrichment direction genuinely sample-visible; and
5. an arbitrarily slowly decaying, or diagonally persistent, finite-section excess.

The moving-family version of `NB-288` is preserved as well. Given packet-dependent dimensions, cutoffs and an `O(1)` desired excess floor at the matched cutoff, perform the same grafting separately for each packet. The resulting family has the exact packet-specific Dirichlet sample table while retaining the same matched floor and the same uniform conditioning estimates.

Hence **raw arithmetic sample values do not exclude the NB-288 lethargy mechanism**.

## 6. What the control does not preserve

The result is a falsification test, not a model of the full Nyman system. The synthetic generators `phi_n` generally have different norms and mutual inner products from the canonical Nyman atoms. Their source Gram can be arbitrarily distorted because the correction

\[
R_0(u_n-L\psi_n)
\]

lies in the old section and can be large or strongly correlated with old generators.

Likewise, the construction does not preserve:

- the canonical `L^2`/Hardy norm of each Nyman generator;
- the exact generator Gram as a function of the integer labels;
- the Bagchi dilation operators and their isometry properties;
- localization of the orthogonalized Dirichlet atoms in integer or Mellin scale;
- Möbius structure, coefficient weights, or any arithmetic estimate tied to the source norm.

These are not defects in the theorem. They identify the information that a successful continuation must use.

Suppose an attempted proof of a uniform finite-section rate uses only the exact zero-sample table (13), algebraic identities among those sample vectors such as (15), surjectivity, nestedness, and generic Hilbert-space conditioning. The same proof would apply to the grafted `NB-288` control, contradicting its arbitrary prescribed profile. Therefore at least one additional **metric coupling** specific to the actual Nyman atoms is indispensable.

A viable next estimate must distinguish the true atoms by linking their sampled first-free data to their canonical source geometry. Examples of appropriately stronger targets include a source-norm estimate for the triangular corrections, a localization/Jackson bound for the orthogonalized actual Dirichlet atoms, a dilation identity with controlled operator norm on the relevant quotient, or a direct target-aware bound on

\[
\sum_{r\ge M_X}
|\langle h_{X,M_X},q_{X,r+1}\rangle|^2
\]

that uses the actual Nyman Gram rather than only `L q` or the raw sample table.

## Stress tests and adversarial checks

### The prescribed samples may be arbitrary

No boundedness assumption on the sequence `u_n` is needed for the algebraic section-preservation statement. A large `u_n` merely makes the old-section correction in (5) large. For the Dirichlet samples (13), this issue is mild anyway: for zeros strictly inside the relevant Hardy half-plane, each coordinate decays with `n` in modulus.

### The right inverse does not change with the stage

The proof deliberately uses a single right inverse into `V_(N_0)`. Therefore every correction is contained in every later old section. No recursive stability hypothesis is hidden in the construction.

### The future direction is not lost

Because the coefficient of `psi_n` in (5) is one,

\[
\phi_n\notin V_{n-1}.
\]

Thus every grafted atom really enlarges the section by one dimension. The construction is not obtaining arbitrary samples by adding redundant vectors.

### Exact sample visibility is preserved, not source visibility

If `u_n` is nonzero then the grafted raw generator is sample-visible. This does not imply that the orthogonal quotient direction `psi_n` has a large sample after subtraction of the old section. That distinction is exactly the one exposed by `NB-287` and `NB-288`.

### The base section is intentionally not claimed canonical

Only labels `n>N_0` are forced to have their canonical Dirichlet zero samples. This is sufficient to preserve every multiplicative sample identity whose participating labels all lie in the tail, and it is sufficient for the asymptotic finite-section question. No claim is made that a fixed arbitrary lethargy control can simultaneously reproduce all canonical metric data in the finite base section.

### The theorem is coordinate-stable

Replacing the reduced sample coordinates by `T u_n` for any fixed invertible matrix `T` simply replaces `L` by `TL` and the right inverse by `R_0T^{-1}`. In particular the diagonal normalization between reduced `Q_P(rho_j)` values and the physical first-free jets does not affect the control.

## Relation to prior art and novelty boundary

Arbitrary prescribed approximation-error profiles for nested subspaces are classical Bernstein-lethargy territory. A modern exact formulation for reflexive Banach spaces is A. G. Aksoy and Q. Peng, *Bernstein Lethargy Theorem and Reflexivity*, arXiv:1803.09874. `NB-288` already used this literature only as context; its own interpolation control was explicit.

Nyman--Beurling generalizations formulated through Dirichlet polynomials and zero-value extremal problems are also established prior art. For example, D. K. Dimitrov and W. D. Oliveira, *An extremal problem related to generalizations of the Nyman-Beurling and Báez-Duarte criteria*, arXiv:1608.07887, studies Dirichlet-polynomial interpolation at zeros. The finite first-free reduction used here, however, is inherited locally from `NB-281`--`NB-283` and is rederived in `NB-282` for this research line.

No novelty is claimed for the triangular basis change (5), for existence of finite-dimensional right inverses, for the elementary multiplicative identity (15), or for Bernstein lethargy itself.

The research delta is narrower and source-specific: **after the exact excess/null-innovation formulation of `NB-284`--`NB-288`, imposing the complete future Dirichlet zero-sample table and its semigroup algebra still does not constrain the excess profile unless those samples are coupled to the canonical Nyman metric geometry.** This is the matched control required to prevent subsequent work from mistaking pointwise arithmetic structure for a quantitative source-space estimate.

The external literature is contextual rather than load-bearing; the proof is contained above. No new source is therefore required in `SOURCES.md`.

## Falsification boundary

The finding would be falsified by any step in the triangular lemma that changes a section, the sampling map, or the excess. Equation (6) is the decisive check: because the correction lies in `V_(n-1)` and `psi_n` spans the one-dimensional quotient, the generated subspace is identical. Equations (8)--(12) then follow from definitions.

It would also be falsified as an Nyman-specific control if the claimed canonical data included source norms or generator Grams. They do not. The claim is explicitly restricted to raw first-free zero samples and identities visible **after applying the sample map**.

A future theorem that proves a rate from the actual Nyman generator Gram, from the exact dilation isometries, or from an arithmetic localization inequality would not contradict `NB-289`; it would supply precisely the missing metric coupling that this control isolates.

## Consequences for the active research frontier

`NB-288` showed that generic Hilbert geometry and excellent sample conditioning do not prevent arbitrary moving finite-section lethargy. A natural reaction was to hope that the actual arithmetic sample vectors of Dirichlet atoms might already rule out that control. `NB-289` closes that weaker route.

The next discriminating object cannot be merely

\[
\bigl(n^{-\rho_j}-n^{-1}\bigr)_{j}
\]

or algebraic relations among those vectors. The research question must involve how those vectors are realized by the **canonical Nyman atoms in the canonical source norm**.

In the language of `NB-287`, what remains to be estimated is still the tail

\[
\mathfrak A_{M_X}(Z_X)
=
\sum_{r\ge M_X}
|\langle h_{X,M_X},q_{X,r+1}\rangle|^2,
\]

but a successful bound now has to use a property of the actual orthogonalized Dirichlet innovations `q_(X,r)` that is not recoverable from their pointwise first-free samples alone.

This also sharpens the accepted semigroup-enrichment clue rather than reopening it. The exact Bagchi dilation law remains a plausible stronger input because it is an **operator identity in the source Hilbert space**, not just the coordinate identity (15). Any continuation through that clue must retain the source norm, target residual, and compressed-frame costs already required there.

## Research disposition

Proved as a negative control and route-narrowing result.

The substantive conclusion is:

\[
\boxed{
\text{exact Dirichlet zero-sample algebra}
\;\not\Rightarrow\;
\text{uniform finite-section rate}
}
\]

under generic Hilbert geometry, even when combined with the benign conditioning properties of `NB-288`.

The remaining plausible source of a quantitative rate is a **metric arithmetic coupling**: canonical generator Gram structure, source-space dilation/localization, or another estimate that ties the exact sample data to the actual Nyman norm. This is the next live target.