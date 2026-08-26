# PF-042 — canonical adjacent principal-series transfer telescopes; branching is the only nontrivial route, and the ordinary branched determinant is already obstructed

**Status:** `DECISIVE-NEGATIVE` for one-dimensional deterministic transfer along the canonical cusp/cuff chain; combined with PF-035/PF-036 this closes the ordinary Selberg/Ruelle transfer-operator route unless a genuinely new renormalized branching formalism is introduced.

## 1. Exact Fuchsian chain

For consecutive ideal endpoints let

\[
G(a,b)=\frac1{b-a}
\begin{pmatrix}
a+b&-2ab\\
-2&a+b
\end{pmatrix}\in PSL_2(\mathbb R).
\]

For the prime-flute endpoint sequence \(u_0<u_1<u_2<\cdots\), set

\[
G_n:=G(u_{n-1},u_n).
\]

The hyperbolic element \(G_n\) is the distinguished cuff side-pairing; its trace determines the cuff length by

\[
|\operatorname{tr}G_n|=2\cosh(\ell_n/2).
\]

The canonical loop around the cusp between the two adjacent cuffs is

\[
P_n:=G_nG_{n+1}^{-1}.
\]

PF-018 computed this element explicitly and showed that it is parabolic with fixed point \(-u_n\).

The crucial identity is now purely algebraic:

\[
\boxed{
P_mP_{m+1}\cdots P_N
=G_mG_{N+1}^{-1}.
}
\]

Every intermediate side-pairing cancels. Thus the canonical holonomy that transports from one cuff frame to another through a consecutive block depends only on the two endpoint frames, not on the internal sequence

\[
\ell_{m+1},\ldots,\ell_N
\]

or on the corresponding internal prime-gap fluctuations.

Geometrically, \(G_mG_{N+1}^{-1}\) is the separating holonomy of the entire block. Its conjugacy class can be written using only the outer endpoint data (equivalently the appropriate four-point cross-ratio). The intermediate gaps survive only if one asks for additional loops/branches inside the block.

## 2. Derivative weights do not rescue the deterministic transfer

The same collapse holds for the standard weighted-composition actions used in boundary spectral theory and thermodynamic formalism.

For example, in a principal-series convention write

\[
(\tau_s(g)f)(x)=j_s(g,x)\,f(gx),
\]

with the usual automorphy factor satisfying the cocycle law

\[
j_s(gh,x)=j_s(g,hx)j_s(h,x).
\]

Equivalently, for orientation-preserving Möbius maps one may use the derivative weight \(|g'(x)|^s\) with the corresponding left/right-action convention. In either convention \(\tau_s\) is a representation (or the same statement with reversed multiplication order).

Therefore

\[
\boxed{
\tau_s(P_m)\tau_s(P_{m+1})\cdots\tau_s(P_N)
=\tau_s(G_mG_{N+1}^{-1})
}
\]

(up to the harmless reversal imposed by convention).

This is stronger than the unweighted matrix telescoping: **the Jacobian/derivative weights telescope as well by the chain rule**. Thus adding the standard spectral parameter \(s\) to a single deterministic transport path does not make the internal prime gaps reappear.

The same argument applies to any honest representation of \(PSL_2(\mathbb R)\): finite-dimensional matrix representations, Koopman-type actions, principal/complementary series, or boundary realizations of Laplace eigenfunctions.

Hence the branch

\[
\boxed{
\text{ordered prime cuffs/cusps}
\to
\text{one local } PSL_2(\mathbb R)\text{ transfer per step}
\to
\text{ordered product / monodromy spectrum}
\to
\text{prime-gap fluctuations}
}
\]

is structurally empty: the product is an endpoint observable.

## 3. Why standard Ruelle operators use branching

Classical Selberg/Ruelle transfer operators avoid this triviality by **summing over inverse branches** of an expanding boundary map,

\[
(\mathcal L_s f)(x)
=\sum_{y\in F^{-1}(x)}|F'(y)|^{-s}f(y),
\]

rather than following a single deterministic chain. The periodic words of the branched system then reproduce closed geodesics, and in the usual geometrically finite settings the Fredholm determinant of a nuclear transfer operator gives the Selberg/dynamical zeta function.

This is standard thermodynamic formalism: Mayer, Morita, Pohl and related work construct such branched systems for cofinite/geometrically finite Fuchsian groups and identify suitable Fredholm determinants with Selberg zeta functions.

For the prime-flute, however, the ordinary branched escape is already obstructed by the previously established short-orbit geometry:

- there are infinitely many distinct primitive closed geodesics with \(L_j\to0\);
- consequently the ordinary Selberg/Ruelle Euler product has no nontrivial initial right half-plane in which its factors approach \(1\) (PF-035);
- including iterates makes the Selberg orbital measure infinite on every positive length window (PF-036).

Thus the conventional dichotomy is now:

\[
\boxed{
\begin{array}{ll}
\text{no branching:} & \text{exact endpoint telescoping},\\[1mm]
\text{ordinary branching over periodic words:} & \text{short-orbit/Fredholm-zeta obstruction}.
\end{array}
}
\]

A transfer-operator route can survive only if it introduces a **new, geometrically forced renormalization of the branching sector**. Merely choosing a different Banach space or rewriting the same periodic-orbit determinant does not address the obstruction.

## 4. Relation to the distinguished cuff lengths

The individual generators \(G_n\) do contain

\[
\ell_n\sim2\log\frac{4p_n}{g_n}
\]

through their traces. PF-037 already showed that microlocal data near one cuff are universal functions of \(\ell_n\).

PF-042 adds a different negative statement: **even when one tries to accumulate those local data in their natural Fuchsian order, the canonical adjacent transport removes all intermediate \(\ell_n\) exactly**. Any nontrivial spectral dependence on a finite block must therefore arise from genuinely different homotopy classes/branching words, hence from multi-gap geometry such as the separating cross-ratios and pointed tangents, not from the serial product of local transfers.

This is compatible with PF-034: a finite prime-derived island has nontrivial two-dimensional spectral data because it retains a whole family of loops inside the block, rather than collapsing the block to its endpoint holonomy.

## 5. Interior/exterior geometry

Nothing here identifies the exterior orthogonal-circle copy with a second intrinsic hyperbolic channel. The exact ambient inversion/interior-exterior duality remains as previously recorded. Applying the ambient involution to the chain simply conjugates the same group identities, so it does not undo the telescoping.

## 6. Novelty check

Known ingredients:

- the cocycle/representation property of principal-series weighted composition operators is classical;
- deterministic products of group representations necessarily represent the group product;
- standard Selberg transfer operators are branched sums over an expanding symbolic dynamics, and their determinant identities are classical in the geometrically finite/cofinite cases;
- thermodynamic formalisms for infinitely generated conformal/Fuchsian systems also exist in the literature, but do not remove the prime-flute short-orbit accumulation by themselves.

Directed searches did not locate this exact prime-flute specialization or the combined `deterministic telescoping versus branched short-orbit obstruction` formulation. The value of the finding is therefore primarily **structural and negative**, not a claim that the representation-theoretic identities themselves are new.

## 7. Research consequence

Do not spend further effort on transfer matrices/operators obtained by assigning one honest \(PSL_2(\mathbb R)\) action to each successive cusp/cuff and multiplying them along the flute. Such constructions are endpoint-only.

The only transfer-like direction still worth pursuing is one whose branching/renormalization is forced by a genuinely two-dimensional prime-derived decomposition (for example the isolated-block tangents of PF-034) and whose determinant is defined independently of the already divergent ordinary periodic-orbit product.
