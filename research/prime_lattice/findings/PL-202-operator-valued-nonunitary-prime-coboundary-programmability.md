# PL-202 — Invertible operator-valued prime multishifts are flat gauges, and exact resolvent covariance remains fully programmable

**Status:** negative result / structural collapse  
**Evidence class:** EXACT-DERIVED + LITERATURE-ADJACENT + DECISIVE-NEGATIVE  
**Research line:** `prime_lattice`

## Claim

Let

\[
\Gamma=\mathbb N_0^{(\mathcal P)}
\]

be the finite-support prime-exponent lattice and let \(\mathcal K\) be an arbitrary complex Hilbert space. Write

\[
V_p(\delta_\alpha\otimes\xi)
 =\delta_{\alpha+e_p}\otimes\xi
\]

for the canonical prime shifts on \(\ell^2(\Gamma)\otimes\mathcal K\). For every prime \(p\) and vertex \(\alpha\), choose an invertible bounded operator

\[
A_p(\alpha)\in GL(\mathcal K)
\]

and define the operator-valued weighted shifts

\[
T_p(\delta_\alpha\otimes\xi)
 =\delta_{\alpha+e_p}\otimes A_p(\alpha)\xi.
\]

If the \(T_p\) commute exactly, then the operator-valued edge field is an algebraic coboundary. There is a uniquely normalized family \(G(\alpha)\in GL(\mathcal K)\), with \(G(0)=I\), such that

\[
\boxed{
A_p(\alpha)=G(\alpha+e_p)G(\alpha)^{-1}
}
\]

for every \(p,\alpha\). Hence on the algebraic finite-support core,

\[
\boxed{T_p=D_GV_pD_G^{-1}},
\qquad
D_G(\delta_\alpha\otimes\xi)
 =\delta_\alpha\otimes G(\alpha)\xi.
\]

Unlike the unitary case of `PL-197`, this need not be a bounded Hilbert-space similarity: bounded local weights do not imply uniform bounds on the accumulated vertex products \(G(\alpha)\) and their inverses. A bounded simultaneous similarity follows only when

\[
\sup_\alpha\|G(\alpha)\|<\infty,
\qquad
\sup_\alpha\|G(\alpha)^{-1}\|<\infty.
\]

That caveat does not rescue exact resolvent covariance. Let \(\{H_\alpha\}_{\alpha\in\Gamma}\) be **any** uniformly bounded family of self-adjoint operators on \(\mathcal K\), say

\[
\sup_\alpha\|H_\alpha\|\le M,
\]

and put

\[
H=\bigoplus_{\alpha\in\Gamma}H_\alpha,
\qquad
R=(H-i)^{-1}=\bigoplus_\alpha R_\alpha,
\qquad
R_\alpha=(H_\alpha-i)^{-1}.
\]

Define

\[
\boxed{
A_p(\alpha)=R_{\alpha+e_p}R_\alpha^{-1}.
}
\]

Then the weights and their inverses are uniformly bounded, the weighted prime shifts commute exactly, and

\[
\boxed{RV_p=T_pR\qquad\forall p.}
\]

Moreover the corresponding vertex gauge is boundedly invertible. Thus an exact common self-adjoint resolvent intertwiner can carry an **arbitrary uniformly bounded operator-valued spectral field** over the exponent lattice while the target prime action remains a bounded gauge of the canonical shifts. Passing from scalar nonunitary weights in `PL-201` to genuinely operator-valued invertible weights therefore does not supply arithmetic rigidity by itself.

This closes the simplest invertible operator-valued nonunitary escape left explicitly open by `PL-201`. It does **not** close singular/noninvertible weights, unbounded/domain-sensitive transports, ideal-valued or approximate covariance, genuinely noncommuting source actions, or target-relative quotients/compressions where the global cubical gauge argument may fail.

## 1. Exact commutation is the noncommutative flat-square relation

A direct calculation gives

\[
T_qT_p(\delta_\alpha\otimes\xi)
 =\delta_{\alpha+e_p+e_q}\otimes
 A_q(\alpha+e_p)A_p(\alpha)\xi,
\]

whereas

\[
T_pT_q(\delta_\alpha\otimes\xi)
 =\delta_{\alpha+e_p+e_q}\otimes
 A_p(\alpha+e_q)A_q(\alpha)\xi.
\]

Thus pairwise commutativity is equivalent to

\[
\boxed{
A_q(\alpha+e_p)A_p(\alpha)
 =A_p(\alpha+e_q)A_q(\alpha)
}
\]

for every \(p,q,\alpha\). This is exactly the commuting operator-valued multishift relation in the classical finite-dimensional-coordinate theory. In prime-lattice language it says that the ordered holonomy around every elementary prime square is trivial.

`PL-198` makes the relevance to resolvents sharper. If one starts instead from a single exact dense-range intertwiner

\[
RV_p=T_pR
\]

with the canonical commuting source tuple, then the target tuple must commute before any use of weighted-shift geometry. Hence exact common resolvent covariance plus invertible operator-valued weighted-shift form automatically lands in the flat regime treated here.

## 2. Flat invertible operator weights integrate to one vertex gauge

Fix \(G(0)=I\). If

\[
0=\alpha^{(0)},\quad
\alpha^{(j+1)}=\alpha^{(j)}+e_{p_j},\quad
\alpha^{(m)}=\alpha,
\]

is any monotone path to \(\alpha\), define

\[
G(\alpha)
 =A_{p_{m-1}}(\alpha^{(m-1)})\cdots
  A_{p_1}(\alpha^{(1)})A_{p_0}(0).
\]

Every vertex has finite support and finite total degree, so this is always a finite product. Any two words with the same finite multiset of prime letters differ by a finite sequence of adjacent swaps of distinct letters. Each adjacent swap is exactly one flat-square identity, including the operator order. Therefore the product is path independent even though the fiber operators need not commute with one another.

Appending a \(p\)-edge gives

\[
G(\alpha+e_p)=A_p(\alpha)G(\alpha),
\]

and invertibility yields

\[
A_p(\alpha)=G(\alpha+e_p)G(\alpha)^{-1}.
\]

Consequently

\[
D_GV_pD_G^{-1}(\delta_\alpha\otimes\xi)
 =\delta_{\alpha+e_p}\otimes
   G(\alpha+e_p)G(\alpha)^{-1}\xi
 =T_p(\delta_\alpha\otimes\xi)
\]

on finitely supported vectors.

No unitarity, commutativity of the individual fiber weights, or finite number of prime coordinates is used. Invertibility and square-flatness are the load-bearing hypotheses.

The operator-theoretic caveat is equally important. The diagonal gauge \(D_G\) is bounded and boundedly invertible exactly when the vertex products are uniformly controlled in both directions. Uniform bounds on individual edge weights and inverse edge weights do not imply such global control because condition numbers can accumulate with path length. Therefore the general theorem is an algebraic gauge trivialization, not a blanket bounded-similarity theorem.

## 3. Block resolvents program arbitrary bounded self-adjoint fiber geometry

The bounded-similarity caveat might appear to leave a rigidity escape: perhaps the extra operator-valued metric growth is constrained when the coboundary comes from a genuine self-adjoint resolvent. A direct construction shows that exact covariance itself imposes no such constraint even in the uniformly bounded gauge regime.

Take any uniformly bounded self-adjoint field \(H_\alpha\). For every \(\alpha\),

\[
R_\alpha=(H_\alpha-i)^{-1}
\]

is invertible and satisfies

\[
\|R_\alpha\|\le1,
\qquad
\|R_\alpha^{-1}\|=\|H_\alpha-i\|
 \le\sqrt{M^2+1}.
\]

Set

\[
A_p(\alpha)=R_{\alpha+e_p}R_\alpha^{-1}.
\]

Then uniformly in \(p,\alpha\),

\[
\|A_p(\alpha)\|
 \le\sqrt{M^2+1},
\qquad
\|A_p(\alpha)^{-1}\|
 \le\sqrt{M^2+1}.
\]

The flat-square relation telescopes:

\[
A_q(\alpha+e_p)A_p(\alpha)
 =R_{\alpha+e_p+e_q}R_\alpha^{-1}
 =A_p(\alpha+e_q)A_q(\alpha).
\]

Thus the target shifts commute. Also,

\[
RV_p(\delta_\alpha\otimes\xi)
 =\delta_{\alpha+e_p}\otimes R_{\alpha+e_p}\xi,
\]

while

\[
T_pR(\delta_\alpha\otimes\xi)
 =\delta_{\alpha+e_p}\otimes
 A_p(\alpha)R_\alpha\xi
 =\delta_{\alpha+e_p}\otimes R_{\alpha+e_p}\xi.
\]

Hence \(RV_p=T_pR\) exactly.

Taking

\[
G(\alpha)=R_\alpha R_0^{-1}
\]

shows that this programmed family is not exploiting an unbounded-gauge pathology: both \(G(\alpha)\) and \(G(\alpha)^{-1}\) are uniformly bounded. The tuple \(T=(T_p)_p\) is therefore boundedly simultaneously similar to the canonical prime shifts while the block operator \(H_\alpha\) at each exponent vector was arbitrary subject only to one common norm bound.

The fiber may be finite- or infinite-dimensional. Thus arbitrary bounded multiplicities, local spectral sets, matrix structures, and noncommuting choices of the self-adjoint blocks can be inserted vertex by vertex. Exact operator-valued covariance does not distinguish an arithmetic spectral field from an adversarially programmed one.

## 4. Prior-art and novelty audit

The multishift framework is established operator theory. Rajeev Gupta, Surjit Kumar, and Shailesh Trivedi, “Unitary equivalence of operator-valued multishifts,” *Journal of Mathematical Analysis and Applications* **487**(2) (2020), Article 124032, DOI `10.1016/j.jmaa.2020.124032`, arXiv `1904.00983`, gives the operator-valued multishift setup with invertible weights and the elementary-square commutation condition used above.

Soumitra Ghara, Surjit Kumar, and Shailesh Trivedi, “A short note on the similarity of operator-valued multishifts,” *Archiv der Mathematik* **123**(3) (2024), DOI `10.1007/s00013-024-02026-5`, arXiv `2401.12144`, gives a complete finite-\(d\) similarity characterization in terms of multishift moment/path-product operators. This is close prior art for the bounded-similarity side of the claim.

Accordingly, no novelty is claimed for operator-valued weighted multishifts, their commuting-square relation, path/moment operators, or diagonal similarity. The direct path proof above is the flat invertible specialization and extends to countably many rational-prime axes simply because each exponent vector is reached by a finite path.

The durable line-specific delta is narrower: combining this classical multishift structure with `PL-198` and the exact self-adjoint-resolvent architecture closes the **operator-valued invertible nonunitary** escape that `PL-201` deliberately left open. The block-resolvent construction shows that exact covariance can encode an arbitrary uniformly bounded self-adjoint fiber field while retaining a bounded gauge of the bare prime lattice. A targeted literature audit found the general multishift and similarity theory above but no arithmetic or RH-specific rigidity theorem contradicting this programmability control.

The calculation is self-contained and the cited papers delimit novelty rather than supply an external arithmetic theorem, so no `SOURCES.md` update is required.

## 5. Adversarial boundaries

**Invertibility is load-bearing.** If some \(A_p(\alpha)\) has kernel or non-dense range, the path product cannot be divided to recover a global vertex gauge. Such singular support defects may create genuine invariant subspaces or boundary geometry. They remain viable only if their singular pattern is forced by arithmetic rather than inserted by hand.

**Boundedness and domains matter.** The programmed example uses a bounded self-adjoint block field specifically to keep the resolvent gauge uniformly controlled. Unbounded \(H_\alpha\), unbounded edge transports, or domain-changing similarities can carry additional data not covered by this argument and require explicit common-core and closure analysis.

**Exact equality matters.** Relations only modulo compact, Schatten, trace-class, or other ideals do not reduce to the pointwise square identity. They remain in the relative determinant/spectral-shift regime, with the programmability controls already developed elsewhere in the line.

**The source action matters.** `PL-198` transfers polynomial relations from the source. A genuinely noncommuting or curved arithmetic source can therefore evade the flat conclusion, but its nontrivial relations must be independently derived from rational-prime/completed-zeta structure rather than introduced as free parameters.

**Target-relative topology may matter.** A Nyman/model-space compression, adelic quotient, boundary construction, or other target can prevent the global directed-cube integration used here. Such a mechanism must exhibit the obstruction explicitly and survive matched Helson/generalized-prime controls.

Finally, neither \(\log p\), analytic continuation, the functional equation, nor the Riemann zeros enter the gauge theorem or the programmability example. The same construction works on any countable free commutative monoid. This universality is precisely why it is a decisive negative control rather than positive evidence for RH.

## Consequence for the research line

`PL-197` showed that exactly commuting state-dependent **unitary** operator weights are pure gauge. `PL-198` showed that one exact common dense-range intertwiner from the canonical prime shifts forces the target action to commute. `PL-201` then showed that scalar nonunitary edge moduli are still one vertex potential and that arbitrary bounded scalar spectral fields can be programmed through a self-adjoint resolvent.

The remaining obvious repair was to retain exact covariance but use genuinely operator-valued invertible nonunitary weights, hoping that noncommuting fiber geometry or condition numbers would create a new invariant. In the flat exact regime that repair also collapses:

\[
\boxed{
\text{invertible operator-valued flat prime weights}
\Longrightarrow
\text{one operator-valued vertex gauge},
}
\]

while

\[
\boxed{
\text{arbitrary bounded self-adjoint fiber field}
\Longrightarrow
\text{an exact commuting resolvent-covariant prime gauge}.
}
\]

Therefore the next viable operator-valued route must leave at least one of these hypotheses: invertibility, bounded/global gauge control, exact covariance, a flat commuting source, or the bare contractible exponent lattice. Merely enlarging the fiber from scalars to matrices/operators does not add RH-sensitive rigidity.