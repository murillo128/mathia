# WP-020 — Q-invariant coupled Hodge insertions still collapse to an index

**Status:** `EXACT-DERIVED + CLASSICAL-EQUIVARIANT-INDEX + DECISIVE-NEGATIVE`. WP-019 ruled out a **decoupled** supersymmetric archimedean completion of the exact Prime-Lattice Mangoldt selector from WP-018. A natural escape was to couple the finite and archimedean sectors inside one odd self-adjoint supercharge and hope that the positive operator `Q^2` would retain nonzero archimedean spectral data while the grading still extracts the finite arithmetic term. Coupling by itself does not evade the cancellation. For any even insertion that commutes with the coupled supercharge, the graded spectral trace localizes exactly to `ker Q`; every positive eigenvalue cancels equivariantly. Conversely, the canonical residual-energy insertion that produces `Lambda(n)` in WP-018 is **provably not** invariant under the intrinsic Boolean differential: its commutator is the logarithmically weighted edge differential. Thus the live route is forced into a sharp fork: either preserve supersymmetric/equivariant invariance and collapse to an index, or keep the exact Mangoldt insertion and lose any automatic positivity inherited from `Q^2 >= 0`.

## 1. The remaining escape after WP-019

WP-018 associates to every exponent vector

\[
\alpha=v(n)\in\mathbb N_0^{(\mathbb P)}
\]

its backward Boolean cube

\[
C_\alpha=\{\alpha-\mathbf 1_T:T\subseteq S(\alpha)\},
\]

a parity grading `Gamma`, and the positive diagonal residual-energy operator

\[
R_\alpha e_T
=
E(\alpha-\mathbf 1_T)e_T,
\qquad
E(\alpha)=\sum_p\alpha_p\log p,
\]

with the exact arithmetic identity

\[
\operatorname{Str}R_\alpha=\Lambda(n).
\tag{1}
\]

WP-019 showed that tensoring this finite object with an independent supersymmetric archimedean factor cannot work: a spectral supertrace of the independent positive Laplacian sees only its index.

The obvious next repair is to abandon the tensor product and let a single odd operator `Q` couple finite and archimedean degrees of freedom. The question here is deliberately narrower than “can a coupled cohomology prove RH?”:

> Does genuine coupling alone prevent the McKean--Singer cancellation if the arithmetic observable remains a symmetry of the coupled differential/supercharge?

The answer is no, exactly.

## 2. Equivariant cancellation does not require factorization

Let

\[
\mathcal H=\mathcal H^+\oplus\mathcal H^-
\]

be a `Z_2`-graded Hilbert space with grading `Gamma`. Let `Q` be an odd self-adjoint operator,

\[
\Gamma Q=-Q\Gamma,
\qquad
H=Q^2\ge0.
\]

Assume first that `H` has discrete spectrum of finite multiplicity. Let `B` be an even bounded operator satisfying

\[
[B,Q]=0,
\tag{2}
\]

and let `phi(H)` be a spectral multiplier for which `B phi(H)` is trace class.

For every positive eigenvalue `lambda` of `H`,

\[
U_\lambda=\frac{Q}{\sqrt\lambda}
\]

is an odd unitary isomorphism

\[
U_\lambda:\mathcal H^+_\lambda\overset{\sim}{\longrightarrow}\mathcal H^-_\lambda.
\]

Equation (2) implies that `U_lambda` intertwines the restrictions of `B`:

\[
B|_{\mathcal H^-_\lambda}
=U_\lambda B|_{\mathcal H^+_\lambda}U_\lambda^{-1}.
\]

Hence

\[
\operatorname{Tr}\left(B|_{\mathcal H^+_\lambda}\right)
=
\operatorname{Tr}\left(B|_{\mathcal H^-_\lambda}\right),
\]

and the entire positive `lambda` contribution cancels in the supertrace. Therefore

\[
\boxed{
\operatorname{Str}\bigl(B\,\phi(Q^2)\bigr)
=
\phi(0)\,\operatorname{Str}\bigl(B|_{\ker Q}\bigr).
}
\tag{3}
\]

For the heat kernel,

\[
\boxed{
\operatorname{Str}\bigl(B e^{-tQ^2}\bigr)
=
\operatorname{Str}\bigl(B|_{\ker Q}\bigr),
\qquad t>0.
}
\tag{4}
\]

This is the elementary spectral pairing behind the **equivariant McKean--Singer formula**. Crucially, no tensor-product or decoupling hypothesis appears. `Q` may contain arbitrary finite/archimedean interaction terms. What matters is only oddness, self-adjointness, traceability, and invariance of the insertion under `Q`.

Thus a coupled positive Hodge operator cannot expose its positive spectrum through a `Q`-invariant graded insertion. If the intended `Gamma`-factor or polar term is supposed to arise from the nonzero spectrum of `Q^2`, equation (3) erases exactly that information.

The same statement persists in the usual Fredholm/heat-kernel settings whenever the equivariant graded trace is defined. Continuous-spectrum, relative, or regularized traces can acquire boundary/anomaly terms; those are explicitly outside this no-go and are listed below as surviving routes.

## 3. The exact WP-018 Mangoldt insertion is not Q-invariant

The abstract theorem becomes Mathia-specific once we test the actual operator that succeeds arithmetically.

Give the Boolean cube `C_alpha` its canonical oriented coboundary

\[
d_\alpha e_T
=
\sum_{p\in S(\alpha)\setminus T}
\varepsilon(T,p)e_{T\cup\{p\}},
\tag{5}
\]

where `epsilon(T,p)=+/-1` is any consistent cubical orientation. Since

\[
R_\alpha(T)
=E(\alpha)-\sum_{q\in T}\log q,
\]

an edge adding `p` changes the residual energy by exactly

\[
R_\alpha(T\cup\{p\})-R_\alpha(T)=-\log p.
\tag{6}
\]

Therefore

\[
\boxed{
[R_\alpha,d_\alpha]e_T
=-
\sum_{p\in S(\alpha)\setminus T}
\varepsilon(T,p)(\log p)e_{T\cup\{p\}}.
}
\tag{7}
\]

In particular,

\[
[R_\alpha,d_\alpha]\ne0
\]

for every nontrivial cube. With the canonical Hodge supercharge

\[
Q_\alpha=d_\alpha+d_\alpha^*,
\]

one likewise has

\[
[R_\alpha,Q_\alpha]\ne0.
\tag{8}
\]

This is not an accident or a defect of orientation. The commutator is exactly the **logarithmically weighted edge differential**. The same local energy drop `log p` that makes the alternating finite difference recover `Lambda(p^k)=log p` is what prevents the arithmetic insertion from being a symmetry of the Hodge differential.

Thus WP-018 escapes the equivariant-index collapse only by sitting on the other side of the fork: its successful arithmetic observable is intrinsically non-`Q`-invariant.

## 4. The rigidity fork

Equations (3) and (7) give a clean dichotomy for the most natural coupled-Hodge repair of WP-019.

### A. Make the arithmetic insertion Q-invariant

If a coupled finite/archimedean construction replaces `R_alpha` by an even insertion `B` with `[B,Q]=0`, then

\[
\operatorname{Str}(B\phi(Q^2))
\]

sees only the zero modes of the coupled system. Any dependence intended to come from positive archimedean eigenvalues is lost by (3).

A parameter-dependent `B(s)` could of course place nonconstant functions directly on the zero modes, but that does not derive the gamma/polar sector from the positive geometry of `Q^2`; the desired analytic structure has simply moved into the insertion. In a finite-dimensional kernel an equivariant group action can also have a nonconstant character, but again the positive spectrum has disappeared. This is not the proposed Hodge-positivity mechanism.

### B. Keep the canonical Mangoldt insertion

For `B=R_alpha`, equation (7) says `[B,Q_alpha] != 0` already in the finite Mathia object. Then the equivariant cancellation theorem does not apply, which is why the graded trace can retain the local arithmetic finite difference.

But now the hoped-for sign theorem also does not follow from `Q^2 >= 0`. The functional

\[
A\mapsto\operatorname{Str}(R_\alpha A)
\]

is signed; WP-018 already gives one-edge positive diagonal controls whose supertrace has either sign. Coupling `Q` to an archimedean sector does not change that logical fact. A successful construction in this branch therefore needs an **additional order/positivity theorem** controlling the noncommuting insertion after the global assembly.

The two desired properties are not formally compatible through bare supersymmetry:

```text
Q-invariant insertion
    -> equivariant McKean--Singer cancellation
    -> only zero modes / index survive

canonical Prime-Lattice Mangoldt insertion R_alpha
    -> [R_alpha,Q_alpha] != 0
    -> arithmetic edge differences survive
    -> positivity is no longer inherited from Q^2 >= 0
```

## 5. Matched control: arbitrary coupling does not help in the invariant regime

Take any graded finite-dimensional spaces `H_f`, `H_infty` and any odd self-adjoint matrix `Q` on their graded tensor product. `Q` need not split as

\[
Q_f\otimes1+\Gamma_f\otimes Q_\infty;
\]

its off-diagonal blocks may be arbitrary and may mix the two sectors completely.

Choose any even `B` from the commutant of `Q`. Then every positive singular value/eigenvalue pair of `Q` still contributes equally to the even and odd traces of `B phi(Q^2)`, and (3) holds verbatim.

Hence “add interaction terms” is not by itself a route around WP-019. The obstruction is **equivariance**, not factorization. This matched control is deliberately arithmetic-free: exactly the same cancellation occurs for a randomly chosen coupled supersymmetric matrix. A claimed global Weil mechanism must therefore identify a specific Mathia structure that both breaks the cancellation in the right way and comes with an independent sign theorem.

## 6. Prior art and novelty audit

No index-theoretic novelty is claimed.

- H. P. McKean Jr. and I. M. Singer, *Curvature and the eigenvalues of the Laplacian*, Journal of Differential Geometry **1** (1967), 43--69, DOI `10.4310/jdg/1214427880`, is the classical heat-supertrace source behind the cancellation already used in WP-019.
- M. F. Atiyah and G. B. Segal, *The index of elliptic operators: II*, Annals of Mathematics **87** (1968), 531--545, DOI `10.2307/1970716`, is the classical equivariant-index/fixed-point framework: an operator commuting with a group action yields an equivariant index character. The elementary identity (3) is the spectral form of the same invariant pairing principle.
- Daniel Quillen, *Superconnections and the Chern character*, Topology **24** (1985), 89--95, DOI `10.1016/0040-9383(85)90047-3`, is the standard superconnection prior-art boundary. Coupled superconnections can carry nontrivial transgression/local data, but their Chern-character formalism does not turn the supertrace of a symmetry-preserving positive square into a new positive Weil functional.

The Mathia-specific content is equation (7) and the resulting fork. WP-019 left **genuine finite/archimedean coupling** as an explicit escape. WP-020 shows that coupling remains invisible to the graded positive spectrum whenever the arithmetic insertion is `Q`-invariant, while the one canonical insertion currently known to recover the exact finite Weil coefficients is intrinsically non-invariant for a structural reason: its commutator is the weighted incidence differential itself.

So this is a narrowing result, not a proposed proof mechanism and not a rediscovery of the equivariant index theorem.

## 7. What survives

This finding does **not** rule out all coupled cohomological or superconnection routes. In particular it leaves open:

- a non-`Q`-invariant insertion with a separate geometric order theorem strong enough to control the assembled quadratic form;
- a boundary or APS/eta mechanism where spectral asymmetry contributes an anomaly rather than cancelling pairwise;
- a relative or renormalized trace whose defect is forced geometrically and is proved to have the required sign;
- a non-Fredholm/continuous-spectrum construction where the failure of trace pairing itself produces a canonical boundary term;
- a compression, quotient, Schur complement, or intersection pairing whose positivity theorem is not merely `Q^2 >= 0`;
- a genuinely global differential for which the finite arithmetic term is no longer represented by `R_alpha` alone but is recovered as a boundary/transgression of the coupled object.

These are real escapes. The new constraint is that **breaking the equivariant cancellation must be part of the mathematical mechanism, not merely an incidental coupling**, and the resulting sign can no longer be credited to ordinary Hodge positivity without further proof.

## 8. Falsification and audit tests

Withdraw or narrow this finding if any of the following fails:

1. for every `lambda>0`, `Q/sqrt(lambda)` gives an odd isomorphism between the even and odd `lambda` eigenspaces of `Q^2`;
2. if an even `B` commutes with `Q`, that isomorphism intertwines `B`, forcing equality of the two traces and giving (3);
3. this argument uses no tensor-factorization assumption on `Q`;
4. for the canonical Boolean differential (5), the residual-energy difference across an edge is exactly `-log p`, giving the commutator (7);
5. consequently the WP-018 insertion is not `Q_alpha`-invariant on any nontrivial cube;
6. positivity of `Q^2` alone does not imply positivity of the signed functional `Str(R_alpha ·)`;
7. the claimed archimedean use of a positive nonzero spectrum cannot survive (3) unless the relevant information is placed in zero modes, the insertion, a boundary/anomaly term, or a trace defect instead.

Items 1--6 are exact finite/spectral statements independent of RH. Item 7 is the explicit scope statement: this finding rules out **ordinary equivariant Hodge-supertrace transport of positivity**, not every possible cohomological completion.

## 9. Consequence for the research line

The cohomological search is now more sharply constrained than after WP-019. “Couple the Boolean finite complex to an archimedean supersymmetric system” is not yet enough. The successful finite-place mechanism and the universal Hodge sign mechanism sit on opposite sides of an exact commutator condition.

A viable Mathia-native global object must therefore explain one of two genuinely new things:

1. why a **noncommuting** arithmetic/archimedean insertion nevertheless defines a positive Weil-type form by a theorem stronger than ordinary Hodge positivity; or
2. why a canonical **boundary/anomaly/relative defect** of the coupled complex carries both the Mangoldt edge data and the gamma/polar completion with an independently forced sign.

This points away from bare supersymmetric completion and toward precisely the boundary, relative, compression, and intersection mechanisms that remained outside the earlier no-go results.

## Internal dependencies

- `research/weil_positivity/findings/WP-018-local-boolean-energy-supertrace-recovers-von-mangoldt-but-is-not-positive.md`
- `research/weil_positivity/findings/WP-019-decoupled-supersymmetric-archimedean-completion-collapses-to-an-index.md`
- `research/weil_positivity/findings/WP-015-prime-flute-dtn-positivity-does-not-survive-critical-scattering-continuation.md`
