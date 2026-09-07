# PL-198 — Dense-range exact prime intertwining forces zero curvature

**Status:** negative result / structural collapse  
**Evidence class:** EXACT-DERIVED + LITERATURE-ADJACENT + DECISIVE-NEGATIVE  
**Research line:** `prime_lattice`

## Claim

Let \(\mathcal H_0,\mathcal H_1\) be Hilbert spaces. Let \(\{V_p\}_p\subset B(\mathcal H_0)\) be a bounded family indexed by the rational primes and let \(\{W_p\}_p\subset B(\mathcal H_1)\). Suppose a single bounded operator

\[
R:\mathcal H_0\to\mathcal H_1
\]

has dense range and intertwines every prime direction exactly:

\[
\boxed{R V_p=W_pR\qquad\forall p.}
\]

Then every finite noncommutative polynomial relation satisfied by the source tuple is inherited by the target tuple. In particular, if

\[
V_pV_q=V_qV_p\qquad\forall p,q,
\]

then necessarily

\[
\boxed{W_pW_q=W_qW_p\qquad\forall p,q.}
\]

Applied to the prime-exponent lattice, let

\[
\Gamma=\mathbb N_0^{(\mathcal P)},
\qquad
V_p(\delta_\alpha\otimes\xi)
 =\delta_{\alpha+e_p}\otimes\xi
\]

be the canonical commuting prime shifts on \(\ell^2(\Gamma)\otimes\mathcal K\). If a self-adjoint operator \(L=L^*\) has resolvent

\[
R=(L-i)^{-1}
\]

and there are bounded state-dependent unitary weighted prime shifts

\[
W_p(\delta_\alpha\otimes\xi)
 =\delta_{\alpha+e_p}\otimes U_p(\alpha)\xi
\]

such that

\[
R V_p=W_pR\qquad\forall p,
\]

then the \(W_p\) commute automatically. Their elementary-square curvature therefore vanishes, and `PL-197` applies: there are vertex unitaries \(g_\alpha\) with

\[
U_p(\alpha)=g_{\alpha+e_p}g_\alpha^*,
\]

so the whole target prime action is a diagonal gauge of the canonical flat shifts.

Consequently, the nonzero-curvature escape left open after `PL-197` cannot coexist with a **single exact common resolvent intertwiner from the canonical commuting prime lattice**. A curved prime action must already break at least one of those hypotheses: exact equality, a common dense-range intertwiner, bounded target transport, or the commuting canonical source action.

## 1. Dense-range intertwining transfers all polynomial relations

For a word \(w=p_1\cdots p_m\) in finitely many prime labels, repeated use of the intertwining identities gives

\[
R V_{p_1}\cdots V_{p_m}
 =W_{p_1}\cdots W_{p_m}R.
\]

Hence for every noncommutative polynomial \(P\) involving finitely many coordinates,

\[
\boxed{R P(V)=P(W)R.}
\]

If \(P(V)=0\), then

\[
P(W)R=0.
\]

The range of \(R\) is dense and \(P(W)\) is bounded. Therefore \(P(W)\) vanishes on a dense subspace and hence on all of \(\mathcal H_1\):

\[
\boxed{P(V)=0\Longrightarrow P(W)=0.}
\]

No injectivity, normality, positivity, or spectral theorem is needed. Dense range and bounded target operators are the only analytic inputs.

Taking

\[
P(X,Y)=XY-YX
\]

shows immediately that pairwise commutativity transfers from the source tuple to the target tuple. More generally, an exact common dense-range intertwiner cannot manufacture a projective, \(q\)-commuting, or otherwise polynomially curved relation that is absent from the source representation.

## 2. A self-adjoint resolvent supplies the dense range automatically

For a self-adjoint operator \(L\), the nonreal resolvent

\[
R=(L-i)^{-1}
\]

is bounded and

\[
\operatorname{Ran}R=\operatorname{Dom}L.
\]

The domain of a self-adjoint operator is dense, so \(R\) satisfies the only range hypothesis needed above. Thus from

\[
R V_p=W_pR
\]

we get directly

\[
\begin{aligned}
W_pW_qR
 &=W_pRV_q\\
 &=RV_pV_q\\
 &=RV_qV_p\\
 &=W_qRV_p\\
 &=W_qW_pR.
\end{aligned}
\]

Therefore

\[
(W_pW_q-W_qW_p)R=0.
\]

Since the commutator is bounded and \(\operatorname{Ran}R\) is dense,

\[
W_pW_q=W_qW_p.
\]

This is stronger than the previous exact-unitary covariance obstructions in one respect: self-adjoint resolvent geometry is not what kills the curvature. The curvature has already disappeared before using \(\operatorname{Im}R=R^*R\), normality, mean ergodicity, or any special form of the \(W_p\). It is eliminated purely by the algebra of one common dense-range intertwiner.

## 3. State-dependent unitary curvature therefore collapses to the `PL-197` gauge class

For the state-dependent weighted shifts

\[
W_p(\delta_\alpha\otimes\xi)
 =\delta_{\alpha+e_p}\otimes U_p(\alpha)\xi,
\]

pairwise commutativity is equivalent to the square relations

\[
U_q(\alpha+e_p)U_p(\alpha)
 =U_p(\alpha+e_q)U_q(\alpha).
\]

`PL-197` proves that on the positive prime-exponent lattice these flat square relations integrate globally: there is a vertex gauge \(g_\alpha\) with

\[
U_p(\alpha)=g_{\alpha+e_p}g_\alpha^*.
\]

Hence

\[
W_p=GV_pG^*
\]

for the diagonal unitary \(G(\delta_\alpha\otimes\xi)=\delta_\alpha\otimes g_\alpha\xi\).

The logical order is now sharper than in `PL-197`. There, flatness was assumed and then shown to be pure gauge. Here exact common resolvent covariance from the canonical prime action **forces** that flatness first. Thus one cannot repair the `PL-197` obstruction merely by postulating nonzero state-dependent curvature while retaining the same exact intertwining architecture.

This also explains why a genuinely curved target action cannot be obtained by an exact similarity or quasiaffine transfer of the canonical exponent-lattice shifts. Polynomial relations are functorial under such a dense-range intertwiner; the target cannot acquire a commutator that the source does not possess.

## 4. Prior art and novelty audit

Dense-range intertwining and quasiaffine transforms are classical operator theory. For example, Eitoku Goya and Teishirô Saitô, “On intertwining by an operator having a dense range,” *Tohoku Mathematical Journal* **33** (1981), 127–131, DOI `10.2748/tmj/1178229499`, studies precisely the dense-range intertwining setting. Modern operator literature routinely calls an injective dense-range intertwiner a quasiaffinity and studies properties transferred under such transforms.

The polynomial-relation argument above is more elementary than those classification results: it is an immediate algebraic consequence of \(RV_p=W_pR\) plus density of \(\operatorname{Ran}R\). It should therefore be treated as a classical operator principle, not as a new abstract theorem.

The durable mathematical delta is line-specific. `PL-197` explicitly left source-forced nonzero curvature/noncommutation as a possible escape from flat gauge triviality. The present result shows that **this escape is unavailable inside the exact common-resolvent-intertwining architecture already used throughout the prime-shift branch**. No external theorem is needed for the proof, and the Goya–Saitô paper is a novelty-audit adjacency rather than an evidentiary dependency; no `SOURCES.md` update is required.

## 5. Adversarial boundaries

The dense-range hypothesis is load-bearing. If \(\operatorname{Ran}R\) is not dense, the target commutator is forced to vanish only on \(\overline{\operatorname{Ran}R}\) and may act nontrivially on its complement. A proposed compression or boundary model must therefore state exactly what the target space is and whether the induced map is still dense there; merely calling a construction “compressed” does not evade the theorem.

A **single common intertwiner** is also essential. If each prime direction is related by a different map \(R_p\), the word calculation no longer transports joint polynomial relations. Likewise, if the relation is only approximate or holds modulo a compact/Schatten ideal,

\[
RV_p-W_pR\in\mathcal J,
\]

then the commutator of the target shifts is controlled only through accumulated error terms. Density alone does not turn an ideal-valued defect into zero. This is precisely the kind of genuinely relative regime not closed here.

Boundedness of the target \(W_p\) is used to extend vanishing from the dense range to the whole target Hilbert space. The state-dependent unitary weighted shifts of `PL-197` satisfy this automatically. Unbounded transports would require domain invariance and closure arguments not supplied by this finding.

Finally, the source relation itself matters. If a completed arithmetic construction replaces the canonical commuting \(V_p\) by a source action with nontrivial forced relations or curvature, those relations may of course transfer. The theorem says only that **curvature cannot be created downstream by exact dense-range intertwining when it is absent upstream**.

No prime distribution, \(\log p\), Euler product, analytic continuation, or zeta zero enters the argument. Its universality is therefore a negative control, not positive evidence for RH.

## Consequence for the research line

The exact unitary prime-shift branch now has a stricter boundary. `PL-193`--`PL-196` eliminated fixed scalar and operator-valued cocycles, and `PL-197` showed that arbitrary state dependence is pure gauge whenever the target prime shifts commute. `PL-198` removes the immediate curvature repair whenever the target is obtained from the canonical prime shifts through one exact dense-range resolvent intertwiner:

\[
\text{commuting source prime shifts}
+\text{one exact dense-range intertwiner}
\Longrightarrow
\text{commuting target shifts}
\Longrightarrow
\text{flat state-dependent unitary connection}
\Longrightarrow
\text{pure gauge}.
\]

A surviving relational prime mechanism must therefore move the nontrivial structure **upstream** or weaken the transfer law in a mathematically controlled way. Viable categories remain source actions whose noncommutativity is forced by global arithmetic completion, target/source couplings where no single dense-range exact intertwiner exists, covariance modulo a genuinely informative operator ideal, or nonunitary/nonnormal transport equipped with an independent coercivity theorem. Simply inserting curved edge data downstream of the canonical commuting exponent lattice is incompatible with exact common resolvent covariance.