# NB-291 — prescribed canonical pivot profiles coexist with arbitrary finite-section lethargy

- **Date:** 2026-09-22
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-287, NB-288, NB-289, NB-290
- **Classification:** `EXACT-DERIVED + MATCHED-NONARITHMETIC-CONTROL + TRIANGULAR-GENERATOR-GRAFTING + PRESCRIBED-GRAM-SCHMIDT-PIVOTS + DIRICHLET-ZERO-SAMPLES + ARBITRARY-LETHARGY + SCALAR-PIVOT-OBSTRUCTION-NEGATIVE + DILATION-OPERATOR-GEOMETRY-REMAINS-LIVE + ROUTE-NARROWING + PRIOR-ART-AUDITED`

## Claim

`NB-290` proves a genuine identity in the canonical Nyman source space,

\[
P_{V_{mn-1}^{\perp}}A_m w_n=\sqrt m\,w_{mn},
\tag{1}
\]

and derives from it the scalar pivot contraction

\[
\sigma_{mn}\le \frac{\sigma_n}{\sqrt m},
\qquad
\sigma_n:=\|(I-P_{V_{n-1}})g_n\|.
\tag{2}
\]

The full operator identity `(1)` is new information relative to the matched controls of `NB-288`--`NB-289`. The scalar pivot profile `(2)`, however, is **not**. The scaled triangular graft already recorded in `NB-289` can impose an arbitrary nonzero Gram--Schmidt pivot at every future index while preserving the exact prescribed Dirichlet zero-sample table, every nested section, every finite sampling Gram, every minimum-norm interpolation cost, every neutralized null innovation, and hence any prescribed finite-section lethargy profile.

More precisely, start beyond a surjective section `N_0` with

\[
V_{N_0}\subset V_{N_0+1}\subset\cdots\subset H,
\qquad
\dim(V_n\ominus V_{n-1})=1,
\]

with bounded sampling map

\[
L:H\to\mathbb C^d,
\qquad
L|_{V_{N_0}}\text{ onto},
\]

and choose unit innovations

\[
\psi_n\in V_n\ominus V_{n-1},
\qquad n>N_0.
\]

Fix a right inverse

\[
R_0:\mathbb C^d\to V_{N_0},
\qquad LR_0=I.
\]

For **arbitrary** desired samples `u_n in C^d` and arbitrary nonzero scalars `lambda_n`, define

\[
\boxed{
\phi_n
=
\lambda_n\psi_n
+
R_0\bigl(u_n-\lambda_nL\psi_n\bigr).
}
\tag{3}
\]

Then simultaneously

\[
\boxed{L\phi_n=u_n,}
\tag{4}
\]

\[
\boxed{\operatorname{span}(V_{n-1},\phi_n)=V_n,}
\tag{5}
\]

and

\[
\boxed{
(I-P_{V_{n-1}})\phi_n=\lambda_n\psi_n.
}
\tag{6}
\]

Thus the ordered Gram--Schmidt pivot of the grafted raw generator is exactly

\[
\boxed{\widetilde\sigma_n=|\lambda_n|.}
\tag{7}
\]

Take `u_n` to be the exact reduced Dirichlet first-free zero samples

\[
u_Z(n)
=
\bigl(n^{-\rho_j}-n^{-1}\bigr)_{j=1}^d
\tag{8}
\]

from `NB-282`--`NB-289`, and take

\[
\boxed{\lambda_n=\sigma_n^{\rm Ny},}
\tag{9}
\]

where `sigma_n^Ny>0` is the actual canonical Nyman pivot from `NB-290`. Then the synthetic arbitrary-lethargy control has, index by index in the tail,

1. the exact raw Dirichlet zero-sample vector `(8)`;
2. the exact canonical Nyman one-step pivot `sigma_n^Ny`;
3. therefore the same scalar divisibility contraction, scaled sequence `sqrt(n) sigma_n`, retention numbers `sqrt(m) sigma_(mn)/sigma_n`, scalar cocycle, and one-step Gram-determinant ratios derived from that pivot sequence in `NB-290`;
4. but exactly the same arbitrary finite-section excess as the underlying `NB-288` control.

Hence **no quantitative Nyman rate can follow from the raw sample table plus the scalar canonical pivot profile alone**. The discriminating content left in `NB-290` is the vector/operator geometry of `(1)` — or another relation of comparable strength tying dilations, old-section components, samples, and the canonical source norm together — not the scalar sequence `sigma_n` by itself.

This sharpens the post-`NB-290` frontier. A successful source-metric continuation must use information that cannot be installed by an old-section triangular correction while leaving every section unchanged.

## 1. Prescribing samples and pivots simultaneously

Equation `(3)` is the scaled form of the triangular graft from `NB-289`, now read through its Gram--Schmidt quotient rather than only through its sampling values.

The correction term

\[
R_0\bigl(u_n-\lambda_nL\psi_n\bigr)
\]

lies in

\[
V_{N_0}\subseteq V_{n-1}.
\tag{10}
\]

Applying `L` to `(3)` gives

\[
L\phi_n
=
\lambda_nL\psi_n
+u_n-\lambda_nL\psi_n
=u_n,
\]

which proves `(4)`.

Because `lambda_n` is nonzero and the correction lies in the old section,

\[
\phi_n\notin V_{n-1},
\]

and subtracting the correction recovers the same one-dimensional quotient direction. Therefore

\[
\operatorname{span}(V_{n-1},\phi_n)
=
\operatorname{span}(V_{n-1},\psi_n)
=V_n,
\]

which proves `(5)`.

Finally, `psi_n` is orthogonal to `V_(n-1)` while the correction belongs to it. Orthogonal projection therefore kills the correction exactly:

\[
(I-P_{V_{n-1}})\phi_n
=
\lambda_n\psi_n.
\]

Since `||psi_n||=1`, `(7)` follows.

There is no compatibility condition between `u_n` and `lambda_n`. The former is installed through an old-section correction; the latter is the coefficient of the genuinely new quotient direction. These are independent degrees of freedom once a fixed finite section is already sample-surjective.

## 2. Every finite-section quantity from NB-284--NB-289 is unchanged

The graft changes the raw generator list but not the nested subspaces. Hence

\[
P_n^{\rm graft}=P_n
\qquad(n\ge N_0).
\tag{11}
\]

With `L` and the interpolation datum `y` fixed,

\[
K_n^{\rm graft}
=LP_n^{\rm graft}L^*
=LP_nL^*
=K_n.
\tag{12}
\]

Therefore the finite minimum-norm cost

\[
\mathcal C_n=y^*K_n^{-1}y,
\]

the infinite cost, and the genuine finite-section excess satisfy

\[
\boxed{
\mathfrak A_n^{\rm graft}=\mathfrak A_n.
}
\tag{13}
\]

The normalized Gram--Schmidt direction of `phi_n` is `psi_n` up to the phase of `lambda_n`. Taking `lambda_n>0`, as in `(9)`, makes it exactly `psi_n`. Thus the normalized sample vector

\[
v_n=L\psi_n,
\]

the optimal repair from `NB-285`, and the neutralized null innovation from `NB-287`,

\[
q_n
=
\frac{\psi_n-R_{n-1}L\psi_n}
{\sqrt{1+(L\psi_n)^*K_{n-1}^{-1}(L\psi_n)}},
\tag{14}
\]

are unchanged as well. Consequently the exact Parseval representation

\[
\mathfrak A_M
=
\sum_{r\ge M}
|\langle h_M,q_{r+1}\rangle|^2
\tag{15}
\]

is unchanged term by term.

Thus prescribing the pivot profile does not merely preserve endpoint costs. It leaves intact the entire future null-innovation energy profile that carries arbitrary lethargy in `NB-287`--`NB-288`.

## 3. The complete scalar pivot output of NB-290 can be matched

Let

\[
\sigma_n^{\rm Ny}
=
\|(I-P_{V_{n-1}^{\rm Ny}})g_n\|
\]

be the canonical Nyman pivot. Finite independence gives `sigma_n^Ny>0`, so `(9)` is admissible.

Then `(7)` gives

\[
\widetilde\sigma_n=\sigma_n^{\rm Ny}
\qquad(n>N_0).
\tag{16}
\]

Every statement that depends only on this scalar sequence is therefore reproduced in the synthetic control. In particular, whenever all relevant indices lie in the grafted tail,

\[
\widetilde\sigma_{mn}
\le
\frac{\widetilde\sigma_n}{\sqrt m},
\tag{17}
\]

and

\[
\sqrt{mn}\,\widetilde\sigma_{mn}
\le
\sqrt n\,\widetilde\sigma_n.
\tag{18}
\]

The scalar retention numbers

\[
\widetilde c_{m,n}
:=
\frac{\sqrt m\,\widetilde\sigma_{mn}}
{\widetilde\sigma_n}
\tag{19}
\]

are numerically identical to the canonical ones and hence obey the same cocycle

\[
\widetilde c_{km,n}
=
\widetilde c_{k,mn}\widetilde c_{m,n}.
\tag{20}
\]

Likewise, if one takes any fixed basis of `V_(N_0)` followed by the ordered grafted generators, the Schur-complement determinant update is

\[
\frac{\det \widetilde G_n}{\det \widetilde G_{n-1}}
=
\widetilde\sigma_n^2.
\tag{21}
\]

Thus the tail one-step determinant ratios can also be made identical to the canonical Nyman ratios from `NB-290`.

This does **not** make the full synthetic Gram matrix canonical. Off-diagonal inner products and raw generator norms generally differ, and those differences are exactly where additional metric information may still live.

## 4. What cannot be grafted by this argument

The control matches the scalar consequence of the canonical dilation theorem, not the theorem itself.

In the real Nyman system, `NB-290` proves

\[
P_{V_{mn-1}^{\perp}}A_m\psi_n
=
c_{m,n}\psi_{mn},
\tag{22}
\]

where the same source-space operator `A_m` is an isometry, acts on every generator by the exact Bagchi covariance law, and transports the whole old section into the correct larger canonical section.

The synthetic construction above provides no operator `A_m` with those properties. Merely defining the scalar number `c_(m,n)` from the prescribed pivots does not reproduce `(22)`. Nor does the control preserve

\[
\langle A_m\psi_n,\psi_k\rangle
\quad(k<mn),
\]

the old-section remainder of a dilated innovation, canonical generator norms, the full canonical Gram, or the interaction of the dilation with the sampling map.

This is the decisive distinction. `NB-290` remains a correct exact theorem, but its **scalar pivot contraction is not by itself a discriminant against arbitrary finite-section lethargy**. The potentially useful information is the common vector geometry that produces the contraction.

Accordingly, the next source-side target should not be another inequality involving only

\[
\sigma_n,
\qquad
\sqrt n\,\sigma_n,
\qquad
c_{m,n},
\]

or determinant pivots. It should retain at least one genuinely cross-index object, for example the old-section component

\[
P_{V_{mn-1}}A_m\psi_n,
\]

its first-free sample image, its correlation with the finite minimum-norm source, or a residual-specific compressed frame quantity of the type isolated by `CLUE-visible-semigroup-defect-controls-section-enrichment`.

## 5. Adversarial checks

### Pivot prescription does not alter the section

A very small `lambda_n` does not make the new generator redundant. The quotient of `phi_n` modulo `V_(n-1)` is exactly `lambda_n psi_n`, and `lambda_n` is nonzero. Hence every stage still gains one dimension.

### Large old-section corrections are allowed but not hidden

The right-inverse correction in `(3)` may be large. The result does not claim canonical generator norms or canonical off-diagonal Gram entries. It claims exactly the quantities proved above: samples, subspaces, scalar pivots, and all section-defined interpolation data. Any argument that additionally uses raw norms or off-diagonal source inner products lies outside this control and remains viable.

### The scalar cocycle is not an operator cocycle

Equation `(20)` follows algebraically from a prescribed scalar sequence. It should not be confused with the canonical source-space identity `(22)`. A proof that uses only `(20)` still applies to the arbitrary-lethargy control; a proof that uses an actual isometric dilation and its old-section remainder need not.

### The matched control is target-aware at the finite-section level

Because `P_n`, `L`, `y`, `h_n`, and the `q_n` are unchanged, the control retains the exact target-aware finite-section obstruction from `NB-287`, not merely a Gram-spectrum surrogate. Therefore the negative conclusion is relevant to the active moving-packet quantity `mathfrak A_n`.

### No closure conclusion is imported

The construction starts from an arbitrary-lethargy family supplied by `NB-288`. It does not assume density of the canonical Nyman span, convergence of the actual Nyman distance, RH, or any zero-free statement.

## 6. Prior-art and novelty boundary

The linear algebra used here is classical. Under an invertible triangular change of an ordered generating family, adding an old-span correction does not change the nested flag, and the diagonal coefficient on the new orthogonal quotient rescales the corresponding Gram--Schmidt/QR pivot. No novelty is claimed for that fact.

The Nyman-specific semigroup geometry is also classical at its base level: Bagchi's 2006 survey gives the Hardy/real-space dilation isometries and the covariance law used throughout this line. Modern work such as Werner Ehm's 2024 analysis of Nyman--Beurling Gram matrices and Hugh Carvill's 2025 multiplicative-ladder Gram study concerns substantially richer Gram structure than a bare scalar pivot sequence. Michel Balazard's 2006 work on integer dilations likewise studies a related but different distance of the unanchored fractional-part dilates to their predecessors.

A targeted search did not supply a reason to regard the triangular pivot-prescription lemma itself as new; it is standard Hilbert/QR algebra. The line-local mathematical delta is instead the matched-control consequence **after** `NB-290`: the exact Dirichlet sample table and the complete canonical scalar pivot sequence can coexist with arbitrary prescribed finite-section lethargy. Therefore the pivot sequence cannot be the missing metric coupling.

No external theorem is load-bearing for the proof, so `SOURCES.md` is unchanged.

## Research disposition

Record as a decisive restriction on the interpretation of `NB-290`.

The canonical identity

\[
P_{V_{mn-1}^{\perp}}A_mw_n
=
\sqrt m\,w_{mn}
\]

remains genuine source-space structure. But all information obtained from it after collapsing to the scalar pivot profile can be installed on the `NB-288`--`NB-289` arbitrary-lethargy control by choosing the triangular graft diagonal appropriately.

The live question is therefore narrower: **does the vector-valued dilation geometry — especially the old-section remainder and its target/sample visibility — force a quantitative bound that the triangular control cannot reproduce?** This is the level at which the accepted visible-semigroup enrichment clue remains genuinely discriminating.