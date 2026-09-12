# PF-307 — canonical seam-cut Schur angle saturates on tail blocks

**Status:** `EXACT-DERIVED + ASYMPTOTIC-DERIVED + NEGATIVE/ROUTE-NARROWING`.

PF-306 identifies the normalized constant-to-nonconstant Schur conversion as the first operator omitted by the scalar chain. It leaves two logically different possibilities: a depth-uniform angle gap could make the scalar control robust, or the angle could approach one and force a source-adapted analysis.

The canonical PF-205 simultaneous seam-cut representation already decides that dichotomy at the **global operator-norm level**. PF-216 proves that the raw low-symmetric constant compression has a growing coercive floor in the mass currency

\[
\mathfrak m_0[x]=\sum_n\frac{|x_n|^2}{q_n},
\]

whereas PF-217 constructs tail-block constant projections whose energy becomes negligible after nonconstant tangential relaxation. Combining those two statements with the PF-306 variational Schur-angle identity forces the normalized constant/nonconstant conversion angle to saturate:

\[
\boxed{\|C_{M,L(M)}\|\longrightarrow1}
\]

along finite Galerkin sections supported farther and farther out the prime-flute tail. More quantitatively, for the PF-217 block scale `M` there is `\eta>0` and a choice of sufficiently rich finite nonconstant Galerkin cutoff `L(M)` such that

\[
\boxed{
1-\|C_{M,L(M)}\|^2
\le
C\left(\frac{1+\log M}{M}+P_M^{-\eta}\right)
\longrightarrow0.
}
\tag{1}
\]

Here `C_{M,L}` is the PF-306 normalized Schur conversion for the constant/nonconstant split of the finite PF-205 normalized boundary-response section; it is deliberately renamed from `K` to avoid collision with PF-216's notation for exterior precision.

Thus a uniform global angle gap is not merely unproved on this canonical response: it is impossible. The surviving route is necessarily **source- and target-adapted**. This does not prove a large physical `P/H` mixed response, because the nearly screened directions constructed by PF-217 may be weakly reached by the actual source or suppressed by later reassembly. It proves that no argument may control the full response by replacing that accessibility question with `\sup\|C_{M,L}\|<1`.

## Claim

Use the PF-205 simultaneous natural-width seam cut and the normalized positive boundary form from PF-216--PF-217,

\[
\mathfrak a[f]
=\|f\|^2+\mathfrak k[f],
\qquad
K=\Lambda_Q^{-1/2}\Lambda_E\Lambda_Q^{-1/2}\ge0.
\tag{2}
\]

Let `P` be the orthogonal projection onto the low-symmetric constant module sector and `Q=I-P`. For a finite tail block and a finite tangential Galerkin cutoff, let `\mathcal A_{M,L}>0` denote a finite section retaining the corresponding constant variables and the selected nonconstant modes. With respect to

\[
\mathcal C_{M}\oplus\mathcal Q_{M,L},
\]

write

\[
\mathcal A_{M,L}
=
\begin{pmatrix}
H_{M,L}&B_{M,L}\\
B_{M,L}^*&J_{M,L}
\end{pmatrix},
\qquad
C_{M,L}
:=H_{M,L}^{-1/2}B_{M,L}J_{M,L}^{-1/2}.
\tag{3}
\]

Then every finite section satisfies `\|C_{M,L}\|<1`, but there is a sequence `M\to\infty` and finite cutoffs `L(M)\to\infty` for which (1) holds. In particular,

\[
\boxed{
\sup_{M,L}\|C_{M,L}\|=1.
}
\tag{4}
\]

The conclusion concerns the canonical PF-205 normalized response and its constant/nonconstant split. It does not assert that every other representation has the same finite matrices. What is invariant here is the variational screening statement on this exact response, which is already enough to rule out a representation-level uniform Schur-angle gap as the missing global estimate.

## 1. PF-216 makes the raw constant energy macroscopic

PF-216 proves that for every finitely supported low-symmetric vector

\[
x=\sum_n x_nu_n,
\]

the raw exterior precision satisfies

\[
\langle x,Kx\rangle
\ge c\,\mathfrak m_0[x].
\tag{5}
\]

Hence the full positive normalized form obeys

\[
\boxed{
\mathfrak a[x]
=\|x\|^2+\langle x,Kx\rangle
\ge c\,\mathfrak m_0[x].
}
\tag{6}
\]

PF-217 then constructs tail-block vectors `x^{(M)}` supported in modules `M\le n\le2M` with

\[
\mathfrak m_0[x^{(M)}]\ge c_1M.
\tag{7}
\]

Therefore

\[
\boxed{
\mathfrak a[x^{(M)}]\ge c_2M.
}
\tag{8}
\]

This is exactly the denominator needed by the PF-306 screening fraction: the constant projection carries macroscopic raw energy before nonconstant relaxation.

## 2. PF-217 simultaneously supplies a cheap nonconstant relaxation

For the same tail blocks PF-217 constructs a smooth tangential bump with the prescribed low-symmetric projection and proves that, for some `\eta>0`,

\[
\boxed{
\mathfrak s_{\rm low}[x^{(M)}]
\le
C\bigl(1+\log M+MP_M^{-\eta}\bigr),
}
\tag{9}
\]

where

\[
\mathfrak s_{\rm low}[x]
=\inf_{y\in Q\operatorname{Dom}(\mathfrak a)}
\mathfrak a[x+y].
\tag{10}
\]

Combining (8)--(9) gives

\[
\boxed{
\frac{\mathfrak s_{\rm low}[x^{(M)}]}
{\mathfrak a[x^{(M)}]}
\le
C\left(\frac{1+\log M}{M}+P_M^{-\eta}\right)
\longrightarrow0.
}
\tag{11}
\]

This ratio is stronger for the present purpose than PF-217's original comparison with `\mathfrak m_0`: PF-216 turns the same mass currency into a lower bound for the actual raw constant energy.

## 3. The shorting ratio is exactly the Schur-angle deficit

For any finite positive section (3), PF-306's completion-of-the-square identity gives, for nonzero constant input `x`,

\[
1-
\frac{
\inf_{y\in\mathcal Q_{M,L}}
\langle(x,y),\mathcal A_{M,L}(x,y)\rangle
}{
\langle x,H_{M,L}x\rangle
}
=
\frac{
\|C_{M,L}^*H_{M,L}^{1/2}x\|^2
}{
\|H_{M,L}^{1/2}x\|^2
}
\le\|C_{M,L}\|^2.
\tag{12}
\]

The PF-217 trial profile is smooth in the tangential cuff coordinate and supported in finitely many consecutive modules. Its nonconstant component can therefore be approximated in the positive form norm by finite tangential Galerkin truncations. For each `M`, choose `L(M)` large enough that the finite-section trial energy differs from the PF-217 bound by at most `o(M)`; for example an error bounded independently of `M` is already sufficient.

Using `x=x^{(M)}` in (12), together with (8)--(11), yields

\[
\|C_{M,L(M)}\|^2
\ge
1-
C\left(\frac{1+\log M}{M}+P_M^{-\eta}\right)-o(1).
\tag{13}
\]

Since finite positivity also gives `\|C_{M,L(M)}\|<1`, equations (1) and (4) follow.

No infinite-dimensional block inversion is needed for this conclusion. The saturation is witnessed by finite sections chosen after the explicit PF-217 smooth screening trial is fixed.

## 4. What actually saturates

The nearly unit Schur angle is not an abstract high-frequency artifact inserted by an arbitrary Galerkin basis. PF-217 constructs it geometrically. On a block `M\le n\le2M`, the low projection is carried by a slowly varying discrete envelope, while each constant boundary profile is replaced by a long tangential bump centered at the zero-twist common-perpendicular foot. The bump preserves a macroscopic constant projection but avoids the pant ends that created PF-216's raw mass floor.

Therefore the saturation mechanism is a **constant-to-tangential screening channel on long tail blocks**. In PF-306 language, the raw constant energy has directions that can be screened to an asymptotically negligible fraction once the retained nonconstant sector is allowed to relax.

This is the exact opposite of a uniform-angle-gap scenario. It does not say that every singular direction of `C_{M,L}` is nearly unit, nor does it provide a Weyl count of near-unit angles. It proves existence of at least one increasingly screened direction on the canonical tail blocks.

## 5. Consequence for the current mixed-response route

PF-306 proposed two possible ways to make the scalar chain useful inside the full response:

- prove a uniform global bound `\|C_{M,L}\|\le1-\varepsilon`; or
- if the norm saturates, prove that the actual physical source/reassembly avoids the nearly singular directions.

The first option is now closed for the canonical PF-205 response. The second is not optional bookkeeping; it is the live mathematical gate.

The relevant next object is therefore not the unrestricted operator norm of the Schur resolvent, but its action on the actual normalized `P/H` source and target ranges. Schematically, if `Z_{M,L}` denotes the genuine source vertex after the scalar normalization, one needs a bound on quantities of the form

\[
(I-C_{M,L}C_{M,L}^*)^{-1/2}Z_{M,L}
\tag{14}
\]

or on the corresponding two-sided source/reassembly compression. Equation (13) says that replacing (14) by the full resolvent norm cannot work.

This conclusion aligns with the accepted source-weighted-return clue. PF-303--PF-305 show that scalar return depth is harmless in the killing-normalized currency; PF-306 identifies the first post-scalar conversion vertex; the present result shows that this vertex has no global gap. What remains is to compare the physical source/reassembly with the explicit nearly screened tangential directions, or to identify another factor that suppresses them.

## 6. Prior art and novelty audit

The abstract ingredients are classical. Positive-operator shorting, Schur complements, and their variational interpretation are standard; PF-306 already records Anderson--Trapp, *Shorted Operators. II*, SIAM J. Appl. Math. 28(1), 60--71 (1975), DOI `10.1137/0128007`, and Li--Mathias, *Extremal Characterizations of the Schur Complement and Resulting Inequalities*, SIAM Review 42(2), 233--246 (2000), DOI `10.1137/S0036144599337290`. A structure-directed audit also finds the classical finite-truncation/infinite-network shorting literature; no novelty is claimed for the passage from a small shorted/raw energy ratio to a near-unit normalized Schur angle.

The Mathia-specific content is the geometric input that makes that ratio tend to zero: PF-216 supplies the growing raw constant floor in the exact PF seam normalization, while PF-217 supplies a zero-twist tangential screening trial on the same response. Their combination with PF-306 closes the previously live global-angle-gap branch for the prime-flute tail.

No theorem-level novelty is claimed beyond this project-specific specialization and route consequence.

## 7. Boundaries and falsification tests

This finding does **not** prove noncompactness, failure of weak trace class, divergence of the physical mixed response, or any RH consequence. Operator-norm saturation can be harmless if the actual source has vanishing overlap with the nearly screened directions.

It also does not prove a near-unit angle count of positive density. One witness direction per growing tail block is enough for (4), but weak/Schatten conclusions require quantitative multiplicity or source-weighted information.

The finite-section approximation must preserve the PF-217 trial energy. This is why the statement allows `L(M)` to grow with the tail block. Fixing a tangential cutoff independent of `M` is not justified by PF-217 and is not claimed here.

The result is tied to the canonical PF-205 simultaneous-cut normalized response. Any attempt to transport the numerical singular values of `C_{M,L}` to a materially different interface representation must prove the appropriate blockwise equivalence rather than appeal to notation. The variational conclusion inside this representation is exact and sufficient to falsify a uniform gap there.

A direct audit is available from the persisted proofs: recheck PF-216's lower bound (6), PF-217's explicit trial upper bound (9), and the PF-306 completion-of-the-square identity (12). If those three statements hold in the stated common PF-205 constant/nonconstant split, (13) is immediate. If a future representation changes that split or the positive form, it must re-establish the dictionary before importing the saturation claim.