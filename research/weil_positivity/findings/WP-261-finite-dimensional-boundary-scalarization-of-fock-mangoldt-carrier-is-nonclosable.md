# WP-261 — Finite-dimensional boundary scalarization of the symmetric-Fock Mangoldt carrier is nonclosable at Weil criticality

**Status:** `EXACT-DERIVED + PRIME-SYMMETRIC-FOCK + COMPRESSED-FREE-SHIFT + BOUNDARY-GRAM + EXACT-MANGOLDT-HALF-DENSITY-DIAGONAL + CROSS-PRIME-COHERENT-COLLAPSE + FINITE-DIMENSIONAL-NONCLOSABILITY + SHARP-SIGMA-THRESHOLD + ORTHOGONAL-LABEL-CONTROL + DRURY-ARVESON-CLASSICALIZATION + DECISIVE-NARROWING + NOT-A-WEIL-BRIDGE`.

`WP-259` leaves the exact positive prime-power carrier

\[
T_{\rm sym}e_{p^k}^{\rm sym}
=(\log p)p^{-k/2}e_{p^k}^{\rm sym},
\]

while `WP-260` shows that the canonical bosonic Gibbs/Fisher Hessian cannot turn it into the Weil pairing: the Hessian inserts an extra occupation factor and remains prime-factorized.

The symmetric Fock sector nevertheless contains a natural operation that does create cross-prime interaction before positivity. Compress the free prime creation operators to the permutation-fixed sector and use their adjoints as one-step backward incidence maps. Every prime state then lands at the same vacuum. Combining that common boundary with the `WP-259` mean-energy factor and half-density damping gives a positive algebraic Gram form whose diagonal is exactly `Lambda(p^k)/sqrt(p^k)` at the Weil exponent and whose first prime layer has nonzero cross-prime entries.

The finite truncations are genuinely positive and their off-diagonal entries are forced by the common vacuum rather than chosen as a kernel. But the all-prime form is nonclosable for every `0<sigma<=1`, in particular at `sigma=1/2`. More generally, **no finite-dimensional boundary Hilbert space can coherently receive the exact prime-layer squared norms `(log p)p^{-sigma}` through a closable operator in that regime**. The threshold is sharp: the same coherent boundary map is bounded for `sigma>1`.

Thus finite-dimensional coherent boundary collapse cannot be the missing global Weil geometry. Keeping an orthogonal prime label restores boundedness and the exact Mangoldt diagonal, but also restores prime separability. A surviving Fock route therefore needs a source-forced **infinite-dimensional** correlation/correspondence whose Gram remains closable at half density and whose off-diagonal structure supplies Weil orientation together with the Gamma and polar sectors.

## 1. Symmetric-Fock backward incidence

Retain the prime Fock space of `WP-256`,

\[
\mathcal F
=\mathbb C\Omega\oplus\bigoplus_{m\ge1}\mathcal K^{\otimes m},
\qquad
\mathcal K=\ell^2(\mathbb P),
\]

and let `P_sym` project onto the permutation-fixed sector `F_sym`. If `alpha=(alpha_q)` is an occupation vector with `|alpha|=m`, write `e_alpha` for its normalized symmetric basis vector. For the free left creation operators `L_p`, set

\[
S_p=P_{\rm sym}L_p|_{\mathcal F_{\rm sym}}.
\]

These are the standard symmetric-Fock/Drury--Arveson weighted shifts. Direct normalized symmetrization gives

\[
S_pe_\alpha
=\sqrt{\frac{\alpha_p+1}{m+1}}\,e_{\alpha+e_p},
\]

and therefore

\[
S_p^*e_\alpha
=
\begin{cases}
\sqrt{\alpha_p/m}\,e_{\alpha-e_p},&\alpha_p>0,\\
0,&\alpha_p=0.
\end{cases}
\]

Let

\[
P_{\rm ax}=P_{\rm sym}P_{\rm simp}
\]

be the `WP-259` prime-power axis projection. On its basis vectors all bosons occupy one prime mode, so

\[
S_q^*e_{p^k}^{\rm sym}
=\delta_{pq}e_{p^{k-1}}^{\rm sym},
\qquad k\ge1,
\]

with `e_{p^0}^{sym}=Omega`.

On the algebraic finite-support prime-power span define

\[
R_0=\sum_p S_p^*P_{\rm ax}.
\]

The sum is algebraically well-defined because each basis vector has only one nonzero summand, and

\[
\boxed{R_0e_{p^k}^{\rm sym}=e_{p^{k-1}}^{\rm sym}.}
\]

This is the relevant source-native incidence relation: every prime-power tower steps downward, while the bottom edges of **all** prime towers meet at the common vacuum.

## 2. The boundary Gram has the exact Mangoldt half-density diagonal

On the prime-power axis the `WP-259` Hamiltonian and number operator satisfy

\[
He_{p^k}^{\rm sym}=k\log p\,e_{p^k}^{\rm sym},
\qquad
Ne_{p^k}^{\rm sym}=k e_{p^k}^{\rm sym},
\]

hence

\[
(HN^{-1})^{1/2}e_{p^k}^{\rm sym}
=\sqrt{\log p}\,e_{p^k}^{\rm sym}.
\]

For `sigma>0` define the algebraic boundary operator

\[
C_\sigma
=R_0(HN^{-1})^{1/2}e^{-\sigma H/2}P_{\rm ax}.
\]

Its exact basis action is

\[
\boxed{
C_\sigma e_{p^k}^{\rm sym}
=\sqrt{\log p}\,p^{-k\sigma/2}e_{p^{k-1}}^{\rm sym}.
}
\]

Therefore the algebraic Gram form

\[
q_\sigma(x,y)=\langle C_\sigma x,C_\sigma y\rangle
\]

is positive semidefinite and has diagonal

\[
\boxed{
q_\sigma(e_{p^k}^{\rm sym},e_{p^k}^{\rm sym})
=(\log p)p^{-k\sigma}.
}
\]

At the Weil exponent,

\[
\boxed{
q_{1/2}(e_{p^k}^{\rm sym},e_{p^k}^{\rm sym})
=\frac{\Lambda(p^k)}{\sqrt{p^k}}.
}
\]

Thus the exact finite coefficient from `WP-259` appears here as a **squared boundary norm**, not merely as a diagonal eigenvalue.

The form is also genuinely nonseparable on the first prime layer. For `p!=q`, both states land at the vacuum and

\[
\boxed{
q_\sigma(e_p,e_q)
=\sqrt{\log p\,\log q}\,(pq)^{-\sigma/2}.
}
\]

For a finite prime set `F`, this block is

\[
G_F^{(\sigma)}
=u_F^{(\sigma)}(u_F^{(\sigma)})^*,
\qquad
u_p^{(\sigma)}:=\sqrt{\log p}\,p^{-\sigma/2},
\]

where the symbol on the right is the `p`-component of `u_F^{(sigma)}`. Equivalently, and avoiding any component-label ambiguity,

\[
(G_F^{(\sigma)})_{pq}
=\sqrt{\log p\,\log q}\,(pq)^{-\sigma/2}.
\]

The off-diagonal entries are therefore forced by the common boundary endpoint. For `k>=2`, different prime towers remain orthogonal after one backward step, so this minimal construction only mixes the bottom prime layer; it does not yet reproduce the full Weil translation/autocorrelation geometry.

## 3. Exact nonclosability threshold

On the first prime layer, `C_sigma` contains the scalar functional

\[
\ell_\sigma(x)
=
\sum_p\sqrt{\log p}\,p^{-\sigma/2}x_p.
\]

It is bounded on `ell^2(P)` exactly when

\[
\sum_p\frac{\log p}{p^\sigma}<\infty.
\]

This is `-P'(sigma)` in the prime-zeta half-plane. It converges for `sigma>1` and diverges for every `0<sigma<=1`.

The divergent regime is not merely unbounded: it is nonclosable. Choose pairwise disjoint finite prime sets `F_j` with

\[
A_j:=\sum_{p\in F_j}\frac{\log p}{p^\sigma}\longrightarrow\infty
\]

and define

\[
x_j
=\frac1{A_j}
\sum_{p\in F_j}\sqrt{\log p}\,p^{-\sigma/2}e_p.
\]

Then

\[
\|x_j\|^2=A_j^{-1}\longrightarrow0,
\qquad
C_\sigma x_j=\Omega.
\]

Hence

\[
x_j\to0
\quad\text{but}\quad
C_\sigma x_j\to\Omega\ne0,
\]

which proves

\[
\boxed{
C_\sigma\text{ and }q_\sigma
\text{ are nonclosable for every }0<\sigma\le1.
}
\]

In particular, the positive algebraic form with the exact Weil half-density diagonal does **not** define a closed Hilbert-space quadratic form.

The threshold is sharp. For `sigma>1`, the vacuum row is bounded by the convergent prime sum. On every higher layer, the images are orthogonal and the coefficients `sqrt(log p) p^{-k sigma/2}` have finite supremum. Therefore

\[
\boxed{
C_\sigma\in\mathcal B(\mathcal A,\mathcal F_{\rm sym})
\quad\Longleftrightarrow\quad\sigma>1.
}
\]

The Weil exponent `1/2` thus lies strictly inside the nonclosable regime rather than at a delicate endpoint.

## 4. Any finite-dimensional boundary has the same obstruction

The vacuum witness is only the one-dimensional instance of a general finite-dimensional no-go. Let `K` be any finite-dimensional Hilbert space and

\[
B_\sigma:c_{00}(\mathbb P)\to K
\]

be an algebraic map satisfying the exact prime-layer norms

\[
\boxed{
\|B_\sigma e_p\|^2=\frac{\log p}{p^\sigma}.
}
\]

If `B_sigma` were closable, each scalar coordinate functional would be closable. A densely defined closable scalar functional on a Hilbert space is represented by an ambient Hilbert vector, so the finitely many coordinates extend boundedly and `B_sigma` extends to a bounded operator on all of `ell^2(P)`.

Every bounded operator into a finite-dimensional Hilbert space is finite-rank and Hilbert--Schmidt. Consequently

\[
\sum_p\|B_\sigma e_p\|^2<\infty,
\]

which here requires

\[
\sum_p\frac{\log p}{p^\sigma}<\infty.
\]

Therefore

\[
\boxed{
0<\sigma\le1
\Longrightarrow
\text{no finite-dimensional boundary map with the exact prime norms is closable.}
}
\]

At `sigma=1/2`, no fixed finite-dimensional archimedean/global boundary can coherently receive every prime mode with squared norm `(log p)/sqrt(p)` through an ordinary closed Hilbert-space operator.

A bounded finite-dimensional correction applied afterward cannot repair this. For the explicit witness above, any bounded correction sends `x_j` to zero while the bad boundary component tends to a nonzero vector. Repair must therefore change the boundary category or source map **before** the singular coherent collapse.

## 5. Matched control: keep the prime label

The divergence comes from coherent identification, not from the Mangoldt diagonal itself. Retain an orthogonal prime label and define

\[
\widehat C_\sigma e_{p^k}^{\rm sym}
=
\sqrt{\log p}\,p^{-k\sigma/2}
(e_p\otimes e_{p^{k-1}}^{\rm sym}).
\]

Distinct `(p,k)` basis vectors now have orthogonal images. Since

\[
\sup_{p,k\ge1}(\log p)p^{-k\sigma}<\infty
\qquad(\sigma>0),
\]

`widehat C_sigma` is bounded for every positive `sigma`, with

\[
\widehat C_\sigma^*\widehat C_\sigma e_{p^k}^{\rm sym}
=(\log p)p^{-k\sigma}e_{p^k}^{\rm sym}.
\]

Hence at the target value

\[
\boxed{
\widehat C_{1/2}^*\widehat C_{1/2}=T_{\rm sym}
\quad\text{on the prime-power axis}.
}
\]

This gives the exact dichotomy:

\[
\boxed{
\begin{array}{ll}
\text{retain the prime boundary label}
&\Rightarrow\text{ bounded exact Mangoldt carrier, prime-separable};\\[2mm]
\text{collapse all prime labels into fixed finite dimension}
&\Rightarrow\text{ cross-prime coherence, nonclosable for }\sigma\le1.
\end{array}
}
\]

So `WP-260` did not exhaust the symmetric-Fock geometry: the compressed shifts do provide a natural operation that begins to mix prime channels. What fails is the Hilbert-space admissibility of finite-dimensional coherent mixing while the exact critical diagonal is retained.

## 6. Finite truncations do not define the global form

For a finite prime set `F`, the coherent prime block is positive rank one and its unique nonzero eigenvalue is

\[
\lambda_F(\sigma)
=\sum_{p\in F}\frac{\log p}{p^\sigma}.
\]

At `sigma=1/2`, this diverges as `F` exhausts the primes. Normalizing by `lambda_F(1/2)^{-1}` keeps the block norm bounded but sends every fixed diagonal coefficient to zero:

\[
\frac{(\log p)p^{-1/2}}{\lambda_F(1/2)}\longrightarrow0.
\]

So normalized finite positivity does not converge to the desired global carrier. Subtracting an ad hoc divergent rank-one counterterm would leave the geometry-forced Gram category and would require a separately justified renormalized theory.

## 7. Prior art and novelty boundary

The identification of symmetric Fock space with Drury--Arveson space, and of its coordinate multipliers with the symmetric compression of free creation operators, is classical multivariable operator theory. A standard survey is Michael Hartz and Orr Moshe Shalit, *Operator Theory and Function Theory in Drury--Arveson Space and Its Quotients*, arXiv:`1308.1081`. The weighted-shift formulas above are standard consequences of the normalized occupation basis.

The prime zeta function `P(s)=sum_p p^{-s}` and the identity `P'(s)=-sum_p (log p)p^{-s}` in its half-plane of convergence are classical; see C.-E. Fröberg, *On the prime zeta function*, BIT 8 (1968), 187--202, DOI `10.1007/BF01933420`. The functional-analytic facts about closable scalar functionals and finite-rank Hilbert--Schmidt operators are also standard.

No novelty is claimed for those ingredients. A bounded search across symmetric-Fock/Drury--Arveson operator theory and prime/Riemann-gas literature found the standard pieces but not this exact Mathia compatibility obstruction. The Mathia-specific content is their forced combination after `WP-256`--`WP-259`: the prime-power selector and mean-energy factor fix the diagonal boundary norm, while the most direct compressed-shift incidence that creates cross-prime interaction identifies the prime layer in a common finite-dimensional boundary. The exact prime-sum threshold then kills closability at and well beyond the Weil exponent.

This is also **not** a restatement of `WP-227`. There the target numbers

\[
c_{p,k}=(\log p)p^{-k/2}
\]

are cross-block amplitudes of a positive completion, so positivity charges the squared budget

\[
\sum_{p,k}c_{p,k}^2
=\sum_p\frac{(\log p)^2}{p-1}.
\]

Here the same target coefficient is the **Gram diagonal / squared boundary norm**,

\[
\|C_{1/2}e_{p^k}\|^2=c_{p,k},
\]

so finite-dimensional coherent collapse must carry amplitudes `sqrt(c_{p,k})`. Its first layer already demands

\[
\sum_p c_{p,1}
=\sum_p\frac{\log p}{\sqrt p}
=+\infty.
\]

`WP-227` is therefore an auxiliary-trace obstruction for a different normalization; `WP-261` is a finite-dimensional **closability** obstruction for the source-native symmetric-Fock boundary scalarization.

## 8. Consequence and remaining escape

The candidate succeeds at two nontrivial finite-side requirements: its squared boundary norms reproduce the exact Mangoldt half-density without inserting `Lambda` by hand, and its common bottom boundary generates genuine cross-prime Gram terms before positivity. Those successes are incompatible with a closed all-prime form in fixed finite boundary dimension:

\[
\boxed{
\text{critical Mangoldt boundary norms}
+
\text{finite-dimensional coherent prime collapse}
\not\Rightarrow
\text{a closable positive global pairing}.
}
\]

This does **not** rule out every nonseparable Fock/correspondence mechanism. An infinite-dimensional boundary can preserve the critical norms, and a bounded Bessel family can have nonzero cross-prime correlations. What remains open is a **source-forced infinite-dimensional correlation kernel or correspondence** whose Gram is closable at `sigma=1/2`, is not merely the orthogonal label-preserving carrier, produces the oriented Weil translation/autocorrelation structure rather than an arbitrary positive completion, and simultaneously supplies the Gamma and polar sectors.

The finite-dimensional archimedean shortcut is therefore closed. Any surviving Fock-interface route must explain why its infinite-dimensional boundary correlation is canonical and arithmetic, rather than choosing a kernel only to regularize the divergence.
