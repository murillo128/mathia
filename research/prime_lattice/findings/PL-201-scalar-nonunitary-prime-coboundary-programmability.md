# PL-201 — Scalar nonunitary prime multishifts are coboundaries, and exact resolvent covariance can encode arbitrary bounded spectral fields

**Status:** negative result / structural collapse  
**Evidence class:** EXACT-DERIVED + LITERATURE-ADJACENT + DECISIVE-NEGATIVE  
**Research line:** `prime_lattice`

## Claim

Let

\[
\Gamma=\mathbb N_0^{(\mathcal P)}
\]

be the finite-support prime-exponent lattice, with canonical prime shifts

\[
V_p\delta_\alpha=\delta_{\alpha+e_p}
\]

on \(\ell^2(\Gamma)\). Consider scalar state-dependent weighted prime shifts

\[
W_p\delta_\alpha=w_p(\alpha)\delta_{\alpha+e_p},
\qquad
w_p(\alpha)\in\mathbb C^\times.
\]

If the \(W_p\) commute exactly, then their entire scalar edge field is a multiplicative coboundary: there is a nowhere-zero vertex function \(g:\Gamma\to\mathbb C^\times\), normalized by \(g(0)=1\), such that

\[
\boxed{
 w_p(\alpha)=\frac{g(\alpha+e_p)}{g(\alpha)}
}
\]

for every prime \(p\) and vertex \(\alpha\). Hence, on finitely supported vectors,

\[
\boxed{W_p=GV_pG^{-1}},
\qquad
G\delta_\alpha=g(\alpha)\delta_\alpha.
\]

When \(g\) is bounded above and bounded away from zero, this is a bounded simultaneous similarity. Thus passing from unitary edge phases in `PL-197` to arbitrary nonzero scalar moduli does not create curvature or a new prime-lattice invariant; it only replaces a unitary gauge by a possibly nonunitary vertex metric/potential.

More decisively for the exact-resolvent branch, this metric data is itself fully programmable. Let \(h:\Gamma\to\mathbb R\) be **any bounded real field** and define the bounded self-adjoint diagonal operator

\[
H_h\delta_\alpha=h(\alpha)\delta_\alpha,
\qquad
R_h=(H_h-i)^{-1}.
\]

Writing

\[
r_\alpha=\frac1{h(\alpha)-i},
\]

define

\[
\boxed{
 w_p(\alpha)=\frac{r_{\alpha+e_p}}{r_\alpha}
 =\frac{h(\alpha)-i}{h(\alpha+e_p)-i}.
}
\]

Then every \(W_p\) is bounded with nonzero bounded weights, the family commutes exactly, and

\[
\boxed{R_hV_p=W_pR_h\qquad\forall p.}
\]

Because \(h\) was arbitrary, a genuine self-adjoint resolvent can transfer through an exactly commuting scalar nonunitary prime action while the edge moduli/phases encode an arbitrary bounded vertexwise spectral field. Exact scalar nonunitary prime covariance therefore supplies **no arithmetic rigidity by itself**. Any proposed RH mechanism in this class must explain what independently forces the vertex potential from rational-prime arithmetic, analytic continuation, a target-relative constraint, positivity/coercivity, or another non-programmable global structure.

This closes the simplest scalar part of the `nonunitary/nonnormal transport` escape left open by `PL-197` and `PL-198`. It does **not** close operator-valued nonunitary weights, weights with genuine singularities/zeros, approximate covariance modulo an operator ideal, target-relative compressions/topology, or source actions carrying nontrivial arithmetic relations before the intertwiner.

## 1. Exact commutation is the scalar zero-curvature relation

A direct calculation gives

\[
W_qW_p\delta_\alpha
 =w_p(\alpha)w_q(\alpha+e_p)
  \delta_{\alpha+e_p+e_q},
\]

while

\[
W_pW_q\delta_\alpha
 =w_q(\alpha)w_p(\alpha+e_q)
  \delta_{\alpha+e_p+e_q}.
\]

Therefore pairwise commutativity is equivalent to

\[
\boxed{
 w_q(\alpha+e_p)w_p(\alpha)
 =w_p(\alpha+e_q)w_q(\alpha)
}
\]

for all \(p,q,\alpha\). This is the scalar multiplicative version of the flat-square condition used for unitary operator-valued weights in `PL-197`.

The important point is that allowing \(|w_p(\alpha)|\neq1\) does not alter the curvature equation. The moduli may change the Hilbert-space metric, but exact commutation still says that the product around every elementary prime square has trivial holonomy.

## 2. Every nowhere-zero flat scalar field integrates to one vertex potential

Fix \(g(0)=1\). For a vertex

\[
\alpha=\sum_p\alpha_pe_p,
\]

choose any monotone path from \(0\) to \(\alpha\) and define \(g(\alpha)\) as the product of the edge weights encountered along that path.

Every such path is finite because \(\alpha\) has finite support and finite total degree. Any two monotone paths with the same endpoint differ by a finite sequence of adjacent transpositions of distinct prime steps. The flat-square relation makes the path product invariant under each such transposition. Hence \(g(\alpha)\) is well defined, even though the lattice has countably many coordinate directions.

Appending the \(p\)-edge gives

\[
g(\alpha+e_p)=w_p(\alpha)g(\alpha),
\]

so

\[
w_p(\alpha)=g(\alpha+e_p)g(\alpha)^{-1}.
\]

For the diagonal map \(G\delta_\alpha=g(\alpha)\delta_\alpha\), one then has on the algebraic finite-support core

\[
GV_pG^{-1}\delta_\alpha
 =\frac{g(\alpha+e_p)}{g(\alpha)}
  \delta_{\alpha+e_p}
 =W_p\delta_\alpha.
\]

Thus the scalar nonunitary connection has no invariant curvature on the bare positive exponent lattice. Its only remaining datum is the growth of the vertex potential \(|g(\alpha)|\).

If

\[
0<c\le |g(\alpha)|\le C<\infty
\qquad\forall\alpha,
\]

then \(G\) and \(G^{-1}\) are bounded and the whole tuple is simultaneously similar to the canonical unweighted prime shifts. If these bounds fail, the algebraic gauge still exists but need not define a bounded similarity; the possible operator-theoretic effect then lies in **metric growth of the potential**, not in a new flat-lattice holonomy.

This distinction matches the classical similarity theory of invertibly weighted multishifts. Ghara, Kumar and Trivedi give a complete similarity criterion for operator-valued multishifts in terms of their moment operators; in the scalar specialization the relevant moments are precisely these path products. Their theorem is formulated for finite \(d\), whereas the path argument above needs no finite-dimensional reduction because each prime-lattice vertex is reached by a finite path.

## 3. A genuine self-adjoint resolvent can program an arbitrary bounded vertex field

The previous section by itself might leave a possible rigidity hope: perhaps requiring the coboundary to arise from a self-adjoint resolvent would constrain the vertex potential strongly enough to make it arithmetic. It does not.

Let \(h:\Gamma\to[-M,M]\) be arbitrary. Then

\[
H_h\delta_\alpha=h(\alpha)\delta_\alpha
\]

is a bounded self-adjoint operator, and

\[
R_h\delta_\alpha=r_\alpha\delta_\alpha,
\qquad
r_\alpha=(h(\alpha)-i)^{-1}.
\]

Since

\[
1\le |h(\alpha)-i|\le\sqrt{M^2+1},
\]

we have

\[
\frac1{\sqrt{M^2+1}}
 \le |r_\alpha|\le1.
\]

Consequently the ratios

\[
w_p(\alpha)=r_{\alpha+e_p}/r_\alpha
\]

are uniformly nonzero and satisfy

\[
\frac1{\sqrt{M^2+1}}
 \le |w_p(\alpha)|
 \le\sqrt{M^2+1}.
\]

Thus each weighted shift is bounded, and all edge weights are uniformly invertible as scalars.

Now

\[
R_hV_p\delta_\alpha
 =r_{\alpha+e_p}\delta_{\alpha+e_p},
\]

whereas

\[
W_pR_h\delta_\alpha
 =r_\alpha w_p(\alpha)\delta_{\alpha+e_p}
 =r_{\alpha+e_p}\delta_{\alpha+e_p}.
\]

Hence \(R_hV_p=W_pR_h\) exactly. Also,

\[
w_q(\alpha+e_p)w_p(\alpha)
 =\frac{r_{\alpha+e_p+e_q}}{r_\alpha}
 =w_p(\alpha+e_q)w_q(\alpha),
\]

so the \(W_p\) commute automatically, in agreement with the dense-range transfer principle of `PL-198`.

Taking

\[
g(\alpha)=r_\alpha/r_0
\]

shows even more: for bounded \(h\), the resulting target prime action is boundedly similar to the canonical prime shifts. The exact covariance therefore permits one to place an **arbitrary bounded real spectral label at every exponent vector** while keeping the prime action in the same similarity class as the bare lattice.

This strengthens the Boolean programmability control in `PL-197`. There, constant-modulus resolvent values allowed an arbitrary two-valued field while preserving unitary edge weights. Once scalar nonunitary weights are admitted, the same construction accommodates every bounded real field, not merely a sign field. The extra modulus information is therefore not evidence of arithmetic specificity; it can be inserted freely through the vertex resolvent values.

## 4. Metric growth outside bounded similarity is also not selected by flatness

The bounded-field control is already enough to refute rigidity of the exact scalar covariance condition. It is nevertheless useful to identify what changes when the potential is not bounded above and below.

Given any real function \(\varphi:\Gamma\to\mathbb R\), set

\[
g(\alpha)=e^{\varphi(\alpha)},
\qquad
w_p(\alpha)=e^{\varphi(\alpha+e_p)-\varphi(\alpha)}.
\]

The resulting weights satisfy every flat-square identity identically. If the edge increments \(\varphi(\alpha+e_p)-\varphi(\alpha)\) are bounded, the corresponding weighted shifts are bounded even when \(g\) itself grows or decays without bound. For example,

\[
\varphi(\alpha)=c|\alpha|_1
\]

gives the constant family \(W_p=e^cV_p\). More irregular Lipschitz vertex fields give equally valid commuting nonunitary multishifts.

Thus the failure of bounded similarity does not by itself make the metric arithmetic. It merely moves the information carrier from curvature to the large-scale growth class of a freely chosen potential. A viable construction would have to derive that growth from an independent rational-prime or completed-zeta principle and then prove a discriminating theorem against generic vertex potentials.

## 5. Prior-art and novelty audit

The abstract multishift structure is classical. Rajeev Gupta, Surjit Kumar and Shailesh Trivedi, “Unitary equivalence of operator-valued multishifts,” *Journal of Mathematical Analysis and Applications* **487**(2) (2020), Article 124032, DOI `10.1016/j.jmaa.2020.124032`, studies commuting operator-valued multishifts with invertible weights and their unitary classification.

More directly, Soumitra Ghara, Surjit Kumar and Shailesh Trivedi, “A short note on the similarity of operator-valued multishifts,” *Archiv der Mathematik* **123**(3) (2024), DOI `10.1007/s00013-024-02026-5`, arXiv `2401.12144`, proves a complete similarity characterization in terms of multishift moments. In its scalar specialization, comparison with the unweighted tuple is governed by uniform upper and lower control of the path-product moments, exactly the bounded-potential distinction isolated above.

Accordingly, no novelty is claimed for weighted multishifts, flat cocycles, path-product moments, diagonal similarity, or the abstract similarity criterion. The durable line-specific content is the exact negative control obtained by combining that structure with the prime-exponent carrier and the self-adjoint-resolvent architecture of `PL-197`--`PL-198`: **allowing scalar nonunitary state dependence makes the resolvent covariance more programmable, not more rigid**.

A targeted literature audit around commuting scalar/operator-valued multishifts, similarity of invertible weighted shifts, cocycle/path-product descriptions, and resolvent intertwiners found the general multishift classification above but no theorem making an arbitrary scalar state-dependent flat prime action arithmetically selective or RH-sensitive. The proof of the programmability example is elementary and does not depend on a literature theorem, so these sources delimit novelty rather than supply the exact calculation.

## 6. Adversarial boundaries

The scalar hypothesis is load-bearing. For genuinely operator-valued nonunitary weights, the flat-square relation still has a path-product form when weights are invertible, and finite-dimensional similarity theory is classical, but boundedness, condition numbers, polar parts and countably many prime directions can interact in ways not covered by the scalar calculation here. No general operator-valued nonunitary collapse is claimed.

Nowhere-zero edge weights are also assumed. Zeros or noninvertible weights can create invariant support defects that cannot be removed by division by a vertex potential. Such defects would need a source-derived reason and a matched generic control before being interpreted arithmetically.

The result concerns **exact** commuting covariance. Relations that hold only modulo compact/Schatten ideals are not coboundary equalities and remain in the relative-determinant/spectral-shift regime already isolated elsewhere in the line.

Target-relative compression or topology can also break the global cubical integration argument. The bare exponent lattice is contractible in the relevant directed sense; a quotient, model-space compression, adelic boundary, or other target can introduce genuine obstruction classes. Such topology has to be derived rather than added ad hoc.

Finally, programmability is a falsification control, not a theorem that every nonunitary construction is useless. A distinguished construction could still be relevant if its vertex metric is **forced independently** by rational primes and if a positivity/coercivity/continuation theorem makes that forced metric discriminate the Riemann zero divisor from matched Helson/generalized-prime controls. Exact scalar covariance alone supplies none of those ingredients.

## Consequence for the research line

The sequence `PL-193`--`PL-198` progressively removed fixed scalar covariance, fixed operator-valued unitary cocycles, flat state-dependent unitary weights, and downstream curvature created through one exact dense-range intertwiner. One stated escape was to abandon unitarity and let edge moduli carry genuine metric or spectral information.

For **scalar** state-dependent edge weights, that escape now collapses to a sharper form:

\[
\text{exact commuting nonzero scalar weights}
\Longrightarrow
\text{one vertex potential }g,
\]

and

\[
\text{exact self-adjoint resolvent covariance}
\Longleftarrow
\text{an arbitrary bounded real vertex field }h.
\]

Thus scalar edge moduli can carry spectral data, but the data is not selected by the prime lattice; it can be programmed freely while the weighted prime tuple remains boundedly similar to the canonical shifts. The surviving nonunitary program must therefore demand an additional non-programmable structure: genuinely operator-valued metric data, singular/support geometry, target-relative topology, ideal-valued covariance, or a completed arithmetic principle that fixes the potential and proves a zero-sensitive coercive law.