# PL-197 — Flat state-dependent unitary prime multishifts are pure gauge

**Status:** negative result / structural collapse  
**Evidence class:** EXACT-DERIVED + LITERATURE-ADJACENT + DECISIVE-NEGATIVE  
**Research line:** `prime_lattice`

## Claim

Let

\[
\Gamma=\mathbb N_0^{(\mathcal P)}
\]

be the finite-support prime-exponent lattice and let `K` be an arbitrary complex Hilbert space. Write `e_p` for the basis vector belonging to the prime `p`, and let

\[
V_p(\delta_\alpha\otimes\xi)=\delta_{\alpha+e_p}\otimes\xi
\]

be the canonical one-sided prime shift on

\[
\mathcal H=\ell^2(\Gamma)\otimes\mathcal K.
\]

Suppose that for every prime `p` and every vertex `alpha in Gamma` one chooses a unitary operator

\[
U_p(\alpha)\in\mathcal U(\mathcal K)
\]

and defines a state-dependent unitary weighted prime shift

\[
W_p(\delta_\alpha\otimes\xi)
 =\delta_{\alpha+e_p}\otimes U_p(\alpha)\xi.
\]

If the prime shifts commute exactly,

\[
W_pW_q=W_qW_p\qquad\forall p,q,
\]

then the whole state-dependent operator-valued connection is pure gauge. More precisely, there is a family of unitaries `g_alpha in U(K)`, with `g_0=I`, such that

\[
\boxed{
U_p(\alpha)=g_{\alpha+e_p}g_\alpha^*
}
\]

for every `alpha,p`. Hence the diagonal unitary

\[
G(\delta_\alpha\otimes\xi)=\delta_\alpha\otimes g_\alpha\xi
\]

satisfies

\[
\boxed{W_p=GV_pG^*\qquad\forall p.}
\]

Thus allowing the unitary attached to one prime edge to depend arbitrarily on all the other exponent coordinates does **not** create a new invariant as long as the resulting prime directions still form an exact commuting representation of the positive exponent monoid. The apparent cross-prime dependence can be removed by a vertexwise unitary gauge.

This closes a natural loophole left explicitly open by `PL-196`: relational dependence on the lattice state is not enough when it is flat. A surviving unitary prime mechanism must therefore carry source-forced curvature/noncommutation, nontrivial topology introduced by a quotient/compression, or another structure not globally removable by a diagonal gauge.

There is also a sharp adversarial control at the self-adjoint-resolvent level. Exact covariance with such a flat state-dependent prime action does **not** force the gauge itself to be arithmetic or canonical. In fact, an arbitrary Boolean field on the exponent lattice can be programmed into it.

For every function

\[
\varepsilon:\Gamma\to\{+1,-1\}
\]

and every `a>0`, define the bounded self-adjoint diagonal operator

\[
H_\varepsilon\delta_\alpha=a\varepsilon(\alpha)\delta_\alpha.
\]

Put

\[
r_+=\frac{a+i}{a^2+1},\qquad
r_-=\frac{-a+i}{a^2+1},\qquad
c=\frac1{\sqrt{a^2+1}},
\]

so that `|r_+|=|r_-|=c`, and set

\[
g_\alpha=c^{-1}r_{\varepsilon(\alpha)}\in\mathbb T.
\]

Then

\[
R_\varepsilon=(H_\varepsilon-i)^{-1}=cG,
\]

and, with `W_p=GV_pG^*`,

\[
\boxed{R_\varepsilon V_p=W_pR_\varepsilon\qquad\forall p.}
\]

The `W_p` commute exactly and their edge phases

\[
U_p(\alpha)=g_{\alpha+e_p}\overline{g_\alpha}
\]

encode the completely arbitrary sign field `varepsilon`. Consequently, state-dependent flat unitary covariance of a genuine self-adjoint resolvent is not merely gauge-trivial at the representation level; it is also **programmable** by data having no connection to rational primes, `log p`, analytic continuation, or the Riemann zero divisor.

## 1. Exact commutation is the zero-curvature square relation

A direct calculation gives

\[
W_qW_p(\delta_\alpha\otimes\xi)
 =\delta_{\alpha+e_p+e_q}\otimes
 U_q(\alpha+e_p)U_p(\alpha)\xi,
\]

whereas

\[
W_pW_q(\delta_\alpha\otimes\xi)
 =\delta_{\alpha+e_p+e_q}\otimes
 U_p(\alpha+e_q)U_q(\alpha)\xi.
\]

Therefore pairwise commutation is equivalent to the square-flatness identities

\[
\boxed{
U_q(\alpha+e_p)U_p(\alpha)
 =U_p(\alpha+e_q)U_q(\alpha)
}
\]

for every vertex `alpha` and every pair of primes `p,q`.

This is precisely the commuting operator-valued multishift condition familiar from multivariable weighted-shift theory. What matters here is that the exponent lattice is the positive cubical lattice itself: every vertex has finite support, so every path from the vacuum to a vertex uses only finitely many prime edges.

## 2. Flatness integrates to a global vertex gauge

Fix `g_0=I`. For a vertex

\[
\alpha=\sum_p\alpha_pe_p,
\]

choose any monotone edge path from `0` to `alpha` and define `g_alpha` to be the ordered product of the corresponding edge unitaries. Explicitly, if the path is

\[
0=\alpha^{(0)},\quad
\alpha^{(j+1)}=\alpha^{(j)}+e_{p_j},\quad
\alpha^{(m)}=\alpha,
\]

set

\[
g_\alpha
 =U_{p_{m-1}}(\alpha^{(m-1)})\cdots
  U_{p_1}(\alpha^{(1)})U_{p_0}(0).
\]

Any two words with the same finite multiset of prime letters are related by adjacent transpositions of distinct letters. Each adjacent transposition changes exactly one elementary square, and the square-flatness identity makes the two corresponding ordered products equal. Hence `g_alpha` is path independent even though the unitary group of the fiber may be noncommutative.

Appending the `p`-edge to a path ending at `alpha` gives

\[
g_{\alpha+e_p}=U_p(\alpha)g_\alpha,
\]

so

\[
U_p(\alpha)=g_{\alpha+e_p}g_\alpha^*.
\]

The diagonal operator `G` built from the `g_alpha` is unitary, and

\[
GV_pG^*(\delta_\alpha\otimes\xi)
 =\delta_{\alpha+e_p}\otimes
   g_{\alpha+e_p}g_\alpha^*\xi
 =W_p(\delta_\alpha\otimes\xi).
\]

Thus every exactly commuting unitary multishift on the bare exponent lattice is unitarily equivalent, by an explicit diagonal gauge, to the unweighted canonical prime shifts.

The countably infinite prime dimension causes no convergence issue: the construction of `g_alpha` at any particular lattice vertex is always a finite product because `alpha` has finite support and finite total degree.

## 3. Self-adjoint resolvent covariance can carry arbitrary Boolean gauge data

The gauge trivialization alone might leave open a stronger hope: perhaps requiring the weighted shifts to intertwine a genuine self-adjoint resolvent would select a distinguished gauge and thereby recover arithmetic information. The Boolean construction in the claim rules this out.

Indeed, for

\[
H_\varepsilon\delta_\alpha=a\varepsilon(\alpha)\delta_\alpha,
\]

we have

\[
R_\varepsilon\delta_\alpha
 =\frac1{a\varepsilon(\alpha)-i}\delta_\alpha
 =r_{\varepsilon(\alpha)}\delta_\alpha
 =c g_\alpha\delta_\alpha.
\]

Hence `R_epsilon=cG`. Since `W_p=GV_pG^*`,

\[
W_pR_\varepsilon
 =GV_pG^*cG
 =cGV_p
 =R_\varepsilon V_p.
\]

No compatibility condition on `varepsilon` is required. It can be a deterministic arithmetic sign, a random sign field, a transferred Beurling label, or an adversarially chosen pattern. Exact commuting covariance survives in every case because the edge weights are a coboundary.

This example is intentionally not a candidate Hilbert--Pólya operator: `H_epsilon` has only the two spectral values `{-a,a}`. Its role is stronger as a falsification control. It proves that once vertex-dependent unitary gauges are admitted, the existence of exact prime-shift covariance does not certify any arithmetic rigidity at all. A proposed mechanism must explain why its gauge/curvature is forced by zeta rather than merely inserted through vertex data.

## 4. Prior-art and novelty audit

The general operator-theory setting is classical. Rajeev Gupta, Surjit Kumar, and Shailesh Trivedi, “Unitary equivalence of operator-valued multishifts,” *Journal of Mathematical Analysis and Applications* **487**(2) (2020), Article 124032, DOI `10.1016/j.jmaa.2020.124032`, studies commuting operator-valued multishifts with invertible weights. Their basic commutation condition is exactly the elementary-square relation above, and their unitary-equivalence theory is formulated through the corresponding path/moment operators. The later paper by Soumitra Ghara, Surjit Kumar, and Shailesh Trivedi, “A short note on similarity of operator-valued multishifts,” arXiv `2401.12144` (2024), gives a broader similarity classification for invertible operator weights.

For unitary edge weights, the present path-product argument is the discrete flat-connection specialization of that established multishift/gauge structure. No abstract novelty claim is made for flat connections, commuting multishifts, or their unitary equivalence. The durable line-specific contribution is the combination of two facts specialized to the prime exponent carrier:

1. even arbitrary cross-coordinate state dependence is pure gauge when the prime shifts remain exactly commuting; and
2. self-adjoint resolvent covariance does not canonically fix that gauge, because arbitrary Boolean vertex data can be realized exactly.

The proof itself is elementary and does not depend on an external theorem, so no `SOURCES.md` update is required; the cited multishift papers are novelty-audit adjacencies rather than evidentiary dependencies.

The result is also dimension-independent. The direct path argument works for the countably many rational-prime coordinates and an arbitrary Hilbert fiber, whereas standard multishift papers are usually formulated for finitely many coordinates and separable fibers.

## 5. Adversarial boundaries

The finding deliberately assumes **exact commutation** of the weighted prime shifts. If the elementary square products differ, the resulting curvature/holonomy is gauge invariant and is not removed by this theorem. However, `PL-036` already supplies an important control: arbitrary scalar projective curvature can be assigned freely on the bare free prime semigroup, so nonzero curvature is not automatically arithmetic evidence either.

The unitary hypothesis is also essential. Nonunitary or nonnormal transfer weights can carry genuine metric/spectral information through their moduli and are not reduced to a vertexwise unitary gauge by this argument. Such a construction would still need an independent coercivity or positivity principle and a rational-prime matched control before being relevant to RH.

Target-relative compressions and source-target maps are not covered. A Nyman/model-space compression, an adelic quotient, or another carrier may destroy the global cubical trivialization or create nontrivial topology. Likewise, a relation that only holds modulo a trace/Schatten ideal is not an exact flat connection and requires the relative-determinant analysis already isolated elsewhere in this line.

Finally, neither `log p` nor the Riemann zeta function appears in the theorem. The same gauge collapse and Boolean programmability hold for any countable free commutative monoid. This universality is the reason the result is a negative structural finding rather than positive evidence for RH.

## Consequence for the research line

`PL-193`--`PL-196` showed that fixed scalar and fixed operator-valued unitary prime cocycles collapse at the self-adjoint-resolvent level. The natural next repair was to let the edge unitary attached to `p` depend on the entire exponent vector, thereby creating explicit cross-prime state dependence.

`PL-197` shows that this repair still has no invariant content if the resulting prime action remains exactly commuting:

\[
\text{state-dependent unitary edge data}
+\text{flat prime squares}
\Longrightarrow
\text{global diagonal gauge of the canonical shifts}.
\]

Moreover self-adjoint resolvent covariance by itself does not select that gauge: arbitrary Boolean lattice fields already satisfy it in a two-point model.

Accordingly, the surviving relational-prime program must demand more than state dependence. It needs **source-forced, non-programmable structure** — for example constrained operator-valued curvature tied to `log p` and a global completion, a target-relative topology that prevents global gauge removal, or a nonunitary relation equipped with an independent positivity/coercivity theorem. Merely replacing fixed prime fibers by flat vertex-dependent unitary weights cannot encode a zero-localizing mechanism.