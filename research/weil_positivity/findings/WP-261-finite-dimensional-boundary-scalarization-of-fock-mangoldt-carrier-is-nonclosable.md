# WP-261 — Finite-dimensional boundary scalarization of the symmetric-Fock Mangoldt carrier is nonclosable at Weil criticality

**Status:** `EXACT-DERIVED + PRIME-SYMMETRIC-FOCK + COMPRESSED-FREE-SHIFT + BOUNDARY-GRAM + EXACT-MANGOLDT-HALF-DENSITY-DIAGONAL + CROSS-PRIME-COHERENT-COLLAPSE + FINITE-DIMENSIONAL-NONCLOSABILITY + SHARP-SIGMA-THRESHOLD + ORTHOGONAL-LABEL-CONTROL + DRURY-ARVESON-CLASSICALIZATION + DECISIVE-NARROWING + NOT-A-WEIL-BRIDGE`.

`WP-259` leaves a precise positive finite-place carrier on the permutation-fixed prime Fock sector,

\[
T_{\rm sym}e_{p^k}^{\rm sym}
=(\log p)p^{-k/2}e_{p^k}^{\rm sym},
\]

while `WP-260` shows that the canonical bosonic Gibbs/Fisher Hessian cannot turn that carrier into the Weil pairing: the Hessian inserts an extra occupation factor and remains prime-factorized.

There is a more geometric way to try to create the missing coupling before positivity. The symmetric sector is the Drury--Arveson/symmetric-Fock compression of the free prime shifts. Its canonical compressed backward shifts erase one prime letter. On a prime-power axis they move

\[
e_{p^k}^{\rm sym}\longmapsto e_{p^{k-1}}^{\rm sym},
\]

and, crucially, **all prime states `e_p` land at the same vacuum**. Combining this boundary incidence with the mean-energy factor and critical damping from `WP-259` produces an algebraic Gram form whose diagonal is exactly the Mangoldt half-density and whose prime layer has genuine cross-prime entries.

The finite truncations are positive and require no hand-picked off-diagonal kernel. Nevertheless the all-prime form is nonclosable at every `0<sigma<=1`, in particular at the Weil value `sigma=1/2`. More generally, no finite-dimensional boundary space can receive the exact prime-layer norms through a closable operator in that regime. The obstruction is sharp: for `sigma>1` the same coherent boundary map is bounded.

Thus the first natural symmetric-Fock operation that actually creates cross-prime interaction before positivity fails for a structural reason stronger than the coefficient mismatch of `WP-260`: **critical Mangoldt boundary norms cannot be coherently collapsed into any fixed finite-dimensional boundary Hilbert space without losing closability.** Retaining an orthogonal prime label restores boundedness and the exact diagonal, but then returns to the separable carrier.

This is a decisive narrowing, not a Weil bridge. It does not rule out a source-forced **infinite-dimensional** correlated boundary/correspondence whose Gram is Bessel/closable and whose off-diagonal structure supplies the Weil orientation together with the Gamma and polar sectors.

## 1. Compressed free shifts on the permutation-fixed sector

Retain the full prime Fock space of `WP-256`,

\[
\mathcal F
=\mathbb C\Omega\oplus\bigoplus_{m\ge1}\mathcal K^{\otimes m},
\qquad
\mathcal K=\ell^2(\mathbb P),
\]

with left creation isometries `L_p`, and let

\[
\mathcal F_{\rm sym}=P_{\rm sym}\mathcal F
\]

be the permutation-fixed sector of `WP-259`.

For an occupation vector

\[
\alpha=(\alpha_q)_{q\in\mathbb P},
\qquad
|\alpha|=m,
\]

write `e_alpha` for the normalized symmetric occupation vector. The compressed creation operators

\[
S_p:=P_{\rm sym}L_p|_{\mathcal F_{\rm sym}}
\tag{1}
\]

are the standard symmetric-Fock/Drury--Arveson weighted shifts. Directly from normalized symmetrization,

\[
S_pe_\alpha
=
\sqrt{\frac{\alpha_p+1}{m+1}}
\,e_{\alpha+e_p},
\tag{2}
\]

and hence, when `m>=1`,

\[
S_p^*e_\alpha
=
\begin{cases}
\sqrt{\alpha_p/m}\,e_{\alpha-e_p},&\alpha_p>0,\\
0,&\alpha_p=0.
\end{cases}
\tag{3}
\]

Let

\[
P_{\rm ax}:=P_{\rm sym}P_{\rm simp}=P_{\rm simp}P_{\rm sym}
\tag{4}
\]

be the `WP-259` prime-power axis projection. Its range is exactly

\[
\mathcal A
:=\overline{\operatorname{span}}
\{e_{p^k}^{\rm sym}:p\in\mathbb P,\ k\ge1\}.
\tag{5}
\]

On a prime-power state all `k` bosons occupy the same mode, so equation (3) simplifies to

\[
S_q^*e_{p^k}^{\rm sym}
=\delta_{pq}e_{p^{k-1}}^{\rm sym},
\qquad
k\ge1,
\tag{6}
\]

where `e_{p^0}^{sym}:=Omega`.

On the algebraic finite-support prime-power span define

\[
R_0
:=\sum_p S_p^*P_{\rm ax}.
\tag{7}
\]

The sum is algebraically well-defined there: every basis vector has only one nonzero summand. Equation (6) gives

\[
\boxed{
R_0e_{p^k}^{\rm sym}=e_{p^{k-1}}^{\rm sym}.
}
\tag{8}
\]

Thus the symmetric compression contains a canonical one-step backward incidence relation on every prime-power tower. Crucially, the bottom edges of **all** towers land at the same vacuum.

## 2. The coherent boundary Gram has the exact Mangoldt half-density diagonal

On `mathcal A`, the commuting diagonal operators of `WP-259` satisfy

\[
He_{p^k}^{\rm sym}
=k\log p\,e_{p^k}^{\rm sym},
\qquad
Ne_{p^k}^{\rm sym}
=k e_{p^k}^{\rm sym},
\]

so

\[
(HN^{-1})^{1/2}e_{p^k}^{\rm sym}
=\sqrt{\log p}\,e_{p^k}^{\rm sym}.
\]

For `sigma>0` define the algebraic boundary operator

\[
C_\sigma
:=
R_0(HN^{-1})^{1/2}e^{-\sigma H/2}P_{\rm ax}.
\tag{9}
\]

Every factor in (9) is source-derived from the `WP-256`/`WP-259` construction: `P_ax` is the ambient simple-spectrum selector, `HN^{-1}` is the mean prime energy on a word, `e^{-\sigma H/2}` is the half-density damping, and `R_0` is the backward incidence supplied by the compressed free shifts.

Equation (8) yields the exact basis action

\[
\boxed{
C_\sigma e_{p^k}^{\rm sym}
=\sqrt{\log p}\,p^{-k\sigma/2}
 e_{p^{k-1}}^{\rm sym}.
}
\tag{10}
\]

Therefore the algebraic Gram form

\[
q_\sigma(x,y)
:=\langle C_\sigma x,C_\sigma y\rangle
\tag{11}
\]

is positive semidefinite on its algebraic domain, and its diagonal is

\[
\boxed{
q_\sigma(e_{p^k}^{\rm sym},e_{p^k}^{\rm sym})
=(\log p)p^{-k\sigma}.
}
\tag{12}
\]

At the Weil exponent `sigma=1/2`,

\[
\boxed{
q_{1/2}(e_{p^k}^{\rm sym},e_{p^k}^{\rm sym})
=
\frac{\Lambda(p^k)}{\sqrt{p^k}}.
}
\tag{13}
\]

Thus the exact finite coefficient from `WP-259` appears here not merely as a diagonal operator eigenvalue but as a **squared boundary norm**.

The form is not prime-factorized. For distinct primes `p!=q`, equation (10) at `k=1` gives

\[
C_\sigma e_p
=\sqrt{\log p}\,p^{-\sigma/2}\Omega,
\qquad
C_\sigma e_q
=\sqrt{\log q}\,q^{-\sigma/2}\Omega,
\]

and hence

\[
\boxed{
q_\sigma(e_p,e_q)
=
\sqrt{\log p\log q}\,(pq)^{-\sigma/2}.
}
\tag{14}
\]

For a finite prime set `F`, the prime-layer Gram is therefore the rank-one matrix

\[
G_F^{(\sigma)}
=u_F^{(\sigma)}(u_F^{(\sigma)})^*,
\qquad
u_p^{(\sigma)}
:=\sqrt{\log p}\,p^{-\sigma/2}.
\tag{15}
\]

The off-diagonal entries were not selected separately; they are forced by the common vacuum endpoint of the source-derived backward incidence.

For `k>=2`, different prime towers remain orthogonal after one backward step. Hence the only new cross-prime interaction in this minimal construction is the bottom-boundary block (14). That limitation will matter below: even if the form were globally admissible, it would not yet reproduce the full Weil translation/autocorrelation geometry.

## 3. The all-prime coherent boundary form is nonclosable for `sigma<=1`

The prime-layer row in (10) is the linear functional

\[
\ell_\sigma(x)
=
\sum_p
\sqrt{\log p}\,p^{-\sigma/2}x_p,
\tag{16}
\]

initially on `c_00(P)`. It is bounded on `ell^2(P)` exactly when

\[
\sum_p\frac{\log p}{p^\sigma}<\infty.
\tag{17}
\]

The series in (17) is `-P'(sigma)` in the prime-zeta half-plane and converges for `sigma>1`. It diverges for every `0<sigma<=1`; at `sigma=1` this follows, for example, from the standard divergence of the logarithmic prime harmonic sum, and for smaller `sigma` by comparison.

Hence the coherent prime-layer functional is unbounded throughout `0<sigma<=1`. More is true: it is **not closable** there.

Choose pairwise disjoint finite prime sets `F_j` such that

\[
A_j
:=\sum_{p\in F_j}\frac{\log p}{p^\sigma}
\longrightarrow\infty.
\tag{18}
\]

This is possible because (17) diverges. Define

\[
x_j
:=
\frac1{A_j}
\sum_{p\in F_j}
\sqrt{\log p}\,p^{-\sigma/2}e_p.
\tag{19}
\]

Then

\[
\|x_j\|^2
=\frac1{A_j}
\longrightarrow0,
\tag{20}
\]

while

\[
C_\sigma x_j
=\Omega
\qquad\text{for every }j.
\tag{21}
\]

Consequently

\[
x_j\to0,
\qquad
C_\sigma x_j\to\Omega\ne0,
\tag{22}
\]

which is exactly the failure of closability. Equivalently, for `j!=l`,

\[
C_\sigma(x_j-x_l)=0,
\]

so the graph limit contains both `(0,0)` and `(0,Omega)`.

Therefore

\[
\boxed{
C_\sigma\text{ and }q_\sigma
\text{ are nonclosable for every }0<\sigma\le1.
}
\tag{23}
\]

In particular,

\[
\boxed{
q_{1/2}
\text{ has the exact Mangoldt half-density diagonal but no closed Hilbert-space form.}
}
\tag{24}
\]

The threshold is sharp. When `sigma>1`, the first-layer row (16) is bounded because (17) converges. On every higher layer equation (10) is an orthogonal weighted backward shift with coefficients

\[
\sqrt{\log p}\,p^{-k\sigma/2},
\qquad k\ge2,
\]

whose supremum is finite. The vacuum row and the orthogonal higher-layer blocks therefore combine to a bounded operator. Thus

\[
\boxed{
C_\sigma\in\mathcal B(\mathcal A,\mathcal F_{\rm sym})
\quad\Longleftrightarrow\quad
\sigma>1.
}
\tag{25}
\]

The singularity at the Weil value is not a minor endpoint effect: `1/2` lies strictly inside the entire nonclosable regime.

## 4. Finite-dimensional boundary spaces are ruled out, not only the common vacuum

The previous witness used the one-dimensional vacuum boundary. The obstruction is actually independent of that particular identification.

Let `K` be any finite-dimensional Hilbert space and let

\[
B_\sigma:c_{00}(\mathbb P)\to K
\tag{26}
\]

be a densely defined algebraic operator with the exact prime-layer diagonal norms

\[
\boxed{
\|B_\sigma e_p\|^2
=\frac{\log p}{p^\sigma}
\qquad(p\in\mathbb P).
}
\tag{27}
\]

Suppose `B_sigma` were closable. Because `K` is finite-dimensional, every coordinate functional of `B_sigma` would then be a closable densely defined scalar functional. A closable scalar functional on a Hilbert space is represented by an ambient Hilbert vector, so all coordinates extend boundedly. Hence the closure of `B_sigma` extends to a bounded operator on all of `ell^2(P)`.

A bounded operator from a Hilbert space into a finite-dimensional space has finite rank and is Hilbert--Schmidt. Therefore, for the prime orthonormal basis,

\[
\sum_p\|B_\sigma e_p\|^2
<\infty.
\tag{28}
\]

Using (27), this requires

\[
\sum_p\frac{\log p}{p^\sigma}<\infty.
\tag{29}
\]

Thus

\[
\boxed{
0<\sigma\le1
\quad\Longrightarrow\quad
\text{no finite-dimensional boundary map satisfying (27) is closable.}
}
\tag{30}
\]

At the target exponent this says that no fixed finite-dimensional archimedean/global boundary can coherently receive every first-prime mode with squared norm

\[
\frac{\log p}{\sqrt p}
\tag{31}
\]

through an ordinary closed Hilbert-space operator.

This conclusion is stable under any bounded finite-dimensional correction applied afterward. If `D` is bounded on the source and has finite-dimensional range, then for the witness (19), `Dx_j->0`; it cannot cancel the nonzero graph limit `C_sigma x_j->Omega`. Repairing (23) therefore requires changing the boundary category or the source map before the singular collapse, not appending an ordinary bounded counterterm.

## 5. Matched control: retaining the prime label is bounded but loses the coupling

The divergence is caused by coherent identification, not by the diagonal Mangoldt norms themselves. Keep an orthogonal copy of the prime label in the codomain and define

\[
\widehat C_\sigma e_{p^k}^{\rm sym}
:=
\sqrt{\log p}\,p^{-k\sigma/2}
\bigl(e_p\otimes e_{p^{k-1}}^{\rm sym}\bigr).
\tag{32}
\]

Distinct `(p,k)` basis vectors now have orthogonal images. Since

\[
\sup_{p,k\ge1}(\log p)p^{-k\sigma}<\infty
\qquad(\sigma>0),
\tag{33}
\]

`widehat C_sigma` is bounded for every positive `sigma`.

Its Gram is exactly diagonal:

\[
\widehat C_\sigma^*\widehat C_\sigma e_{p^k}^{\rm sym}
=(\log p)p^{-k\sigma}e_{p^k}^{\rm sym}.
\tag{34}
\]

At `sigma=1/2`,

\[
\boxed{
\widehat C_{1/2}^*\widehat C_{1/2}
=T_{\rm sym}
\quad\text{on }\mathcal A.
}
\tag{35}
\]

Thus the exact positive carrier from `WP-259` has a perfectly regular boundary-factorization once prime labels are kept orthogonal. What fails is precisely the finite-dimensional coherent collapse that tries to turn those labels into cross-prime Gram entries.

This gives a sharp matched control:

\[
\boxed{
\begin{array}{ll}
\text{retain prime boundary label}
&\Rightarrow\text{ bounded exact Mangoldt carrier, prime-separable};\\[2mm]
\text{collapse prime labels coherently in fixed finite dimension}
&\Rightarrow\text{ cross-prime coupling, but nonclosable for }\sigma\le1.
\end{array}
}
\tag{36}
\]

This is more specific than the Fisher-factorization failure in `WP-260`. The symmetric Fock geometry **does** contain a canonical operation that begins to mix prime channels: the common lower boundary of the compressed backward shifts. What fails is the Hilbert-space admissibility of that mixing when the exact critical diagonal is retained.

## 6. Finite truncations are positive but have no unrenormalized global limit

For a finite prime set `F`, the coherent prime block (15) is positive rank one with unique nonzero eigenvalue

\[
\lambda_F(\sigma)
=\|u_F^{(\sigma)}\|^2
=
\sum_{p\in F}\frac{\log p}{p^\sigma}.
\tag{37}
\]

At `sigma=1/2`,

\[
\lambda_F(1/2)\longrightarrow\infty
\tag{38}
\]

as the truncation exhausts the primes. Therefore finite positivity is not evidence for a global closed form.

One can normalize the coherent block by `lambda_F(sigma)^{-1}` to keep its norm bounded, but then the diagonal at each fixed prime becomes

\[
\frac{(\log p)p^{-\sigma}}
{\lambda_F(\sigma)}
\longrightarrow0.
\tag{39}
\]

That normalization destroys the exact Mangoldt coefficient it was meant to transport. Subtracting a divergent scalar/rank-one counterterm instead would no longer be positivity forced by the original Gram and would require a separately justified renormalized category.

## 7. Prior art and novelty boundary

The identification of symmetric Fock space with Drury--Arveson space, and of its coordinate multipliers/d-shift with the symmetric compression of free creation operators, is classical multivariable operator theory. A standard survey is Michael Hartz and Orr Moshe Shalit, *Operator Theory and Function Theory in Drury--Arveson Space and Its Quotients*, arXiv:`1308.1081`, with updated Springer reference versions. The weighted-shift formulas (2)--(3) are standard consequences of the normalized monomial/occupation basis.

The prime zeta function

\[
P(s)=\sum_p p^{-s}
\]

and its derivative

\[
P'(s)=-\sum_p(\log p)p^{-s}
\]

in the half-plane of convergence are classical; see C.-E. Fröberg, *On the prime zeta function*, BIT 8 (1968), 187--202, DOI `10.1007/BF01933420`.

The facts about closable operators, bounded functionals on Hilbert space, and finite-rank operators being Hilbert--Schmidt are standard functional analysis. No novelty is claimed for any of those ingredients, for the Drury--Arveson shift itself, or for prime-zeta convergence.

A bounded search across Drury--Arveson/symmetric-Fock operator theory and prime/Riemann-gas literature found the standard ingredients but not a theorem identifying this exact Mathia compatibility obstruction. The durable Mathia-specific result is the combination forced by `WP-256`--`WP-259`: the source-derived prime-power selector and mean-energy square root fix the diagonal boundary norm to `Lambda(p^k)p^{-k sigma}`, while the most direct compressed-shift operation that creates cross-prime interaction identifies the prime layer in finite dimension. Equations (25), (30), and (35) then show that this interaction is nonclosable throughout `sigma<=1`, including the required Weil value `1/2`.

This is a negative compatibility theorem, not a claim that finite-dimensional boundary responses are absent from classical operator theory.

The normalization is also importantly different from `WP-227`. There the Weil numbers
\[
c_{p,k}=(\log p)p^{-k/2}
\]
are imposed as **cross-block amplitudes** of a positive completion, so positivity charges the squared Hilbert--Schmidt budget
\[
\sum_{p,k}c_{p,k}^2
=\sum_p\frac{(\log p)^2}{p-1}.
\]
Here the same target coefficient is instead the **Gram diagonal / squared boundary norm**
\[
\|C_{1/2}e_{p^k}\|^2=c_{p,k},
\]
so a finite-dimensional coherent boundary would have to carry amplitudes `sqrt(c_{p,k})`. Its first prime layer already costs
\[
\sum_p c_{p,1}
=\sum_p\frac{\log p}{\sqrt p}
=+\infty.
\]
Thus the present obstruction is not a rediscovery of the `WP-227` trace bound: it is a stronger finite-dimensional **closability** obstruction for the source-native symmetric-Fock boundary scalarization that only becomes available after `WP-259`.

## 8. Consequence for the Weil-positivity mandate

`WP-260` left open a nonseparable source-forced pairing because the canonical Gibbs/Fisher metric was too local. The compressed symmetric shifts provide a natural next candidate and sharpen what "nonseparable" must mean.

The candidate succeeds at two nontrivial finite-side requirements:

1. its squared boundary norms reproduce the exact Mangoldt half-density without inserting `Lambda` by hand;
2. its coherent bottom boundary creates genuine cross-prime Gram terms before positivity.

But those two successes are incompatible with a closed all-prime form when the boundary has fixed finite dimension. Therefore

\[
\boxed{
\text{critical Mangoldt boundary norms}
+
\text{finite-dimensional coherent prime collapse}
\not\Rightarrow
\text{a closable positive global pairing}.
}
\tag{40}
\]

This does **not** rule out all nonseparable Fock/correspondence mechanisms. An infinite-dimensional boundary can preserve the critical norms, and a bounded Bessel family can have nonzero cross-prime correlations. What remains missing is precisely a **source-forced infinite-dimensional correlation kernel or correspondence** whose Gram is closable at `sigma=1/2`, is not merely the orthogonal label-preserving carrier (34), produces the Weil translation/autocorrelation orientation rather than an arbitrary positive completion, and simultaneously supplies the Gamma and polar sectors.

The finite-dimensional archimedean shortcut is therefore closed. Any surviving Fock-interface route must explain why its infinite-dimensional boundary correlation is canonical and arithmetic, rather than choosing a kernel to regularize the divergence.