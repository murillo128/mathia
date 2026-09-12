# WP-262 — Locally finite symmetric-Fock incidence gives bounded exact Mangoldt Grams, so closability alone does not select the mixed-prime geometry

**Status:** `EXACT-DERIVED + PRIME-SYMMETRIC-FOCK + MIXED-COMPOSITE-PAIR-INCIDENCE + INFINITE-DIMENSIONAL-BOUNDARY + EXACT-MANGOLDT-HALF-DENSITY + BOUNDED-CLOSABLE + CROSS-PRIME-COUPLED + GRAPH-PROGRAMMABILITY + COMPLETE-INCIDENCE-DEGENERATION + MATCHED-CONTROLS + PRIOR-ART-CLASSICALIZATION + DECISIVE-NARROWING + NOT-A-WEIL-BRIDGE`.

`WP-261` proves that the most direct coherent collapse of the symmetric-Fock Mangoldt carrier into a fixed finite-dimensional boundary is nonclosable throughout `0<sigma<=1`. Its matched control keeps the prime label orthogonal and is bounded, but then the prime channels remain separable. This leaves an apparently strong target for the next geometry: an **infinite-dimensional closable correspondence that preserves the exact critical Mangoldt diagonal while creating genuine cross-prime correlations**.

That target is necessary but not sufficient. The symmetric Fock sector already contains enough mixed-composite states to build such correspondences in abundance. For any locally finite graph `G` on the primes with no isolated vertices, the normalized pair-incidence map constructed below is bounded for every `sigma>0`, has diagonal

\[
(\log p)p^{-k\sigma},
\]

and at `sigma=1/2` therefore has precisely the finite Weil coefficient `Lambda(p^k)/sqrt(p^k)`. It also has nonzero mixed-prime Gram entries. The construction is an ordinary incidence Gram, so positivity and closability are independent of RH and require no zero data.

But the cross-prime geometry is programmable: changing `G` changes the support of the correlations while preserving the same exact diagonal and the same uniform boundedness theorem. Edge phases can likewise change the signs/phases of off-diagonal entries without affecting positivity. The maximally symmetric equal-incidence attempt does not remove this freedom: on finite complete prime sets the normalized off-diagonal correlations are `1/(N-1)` and vanish pairwise as `N` grows, whereas omitting the normalization makes the required diagonal diverge.

Thus `WP-261`'s analytic obstruction is not the decisive remaining bottleneck. A successful Weil bridge must derive a **specific, source-forced, non-programmable all-prime correlation law** before positivity is read out, and must then still prove that this law has the correct Weil orientation and supplies the Gamma and polar sectors. Infinite-dimensional closability plus exact Mangoldt norms and some cross-prime coupling is too weak a criterion.

## 1. The symmetric Fock sector already contains canonical states for every mixed prime pair

Retain the permutation-fixed sector from `WP-259`, with orthonormal integer basis

\[
\{e_n^{\rm sym}:n\ge1\},
\]

where unique factorization identifies occupation vectors with integers and

\[
H e_n^{\rm sym}=(\log n)e_n^{\rm sym}.
\tag{1}
\]

Let the prime-power source axis be

\[
\mathcal A
:=\overline{\operatorname{span}}
\{e_{p^k}^{\rm sym}:p\in\mathbb P,\ k\ge1\}.
\tag{2}
\]

Now let

\[
G=(\mathbb P,E)
\tag{3}
\]

be a simple locally finite graph on the primes with no isolated vertices, and write `d_p` for the finite positive degree of `p`. For every prime `p` and exponent `k>=1`, define

\[
\boxed{
v_{p,k}^G
:=\frac1{\sqrt{d_p}}
\sum_{q:\{p,q\}\in E}e_{(pq)^k}^{\rm sym}.
}
\tag{4}
\]

Every summand lies in the already existing symmetric Fock sector. No new Hilbert coordinates have been adjoined: the edge `{p,q}` at level `k` is represented by the mixed-composite occupation state `(pq)^k=p^kq^k`.

Unique factorization gives the exact incidence relations. First,

\[
\|v_{p,k}^G\|=1.
\tag{5}
\]

For distinct primes `p,q`,

\[
\boxed{
\langle v_{p,k}^G,v_{q,\ell}^G\rangle
=
\begin{cases}
(d_pd_q)^{-1/2},&k=\ell\text{ and }\{p,q\}\in E,\\
0,&\text{otherwise}.
\end{cases}
}
\tag{6}
\]

Indeed the two normalized sums share exactly one symmetric basis state precisely when the same edge `{p,q}` occurs at the same exponent `k`. Equality between distinct mixed-composite basis labels cannot occur accidentally because their prime supports and valuations are fixed by unique factorization.

This already exhibits the structural difference from the common-vacuum collapse in `WP-261`: each target coordinate is shared by only two source prime channels rather than by all primes simultaneously.

## 2. The pair-incidence boundary map is bounded and has the exact critical Mangoldt diagonal

For `sigma>0`, set

\[
w_{p,k}^{(\sigma)}
:=(\log p)p^{-k\sigma}.
\tag{7}
\]

Define on the algebraic prime-power axis

\[
\boxed{
B_{\sigma,G}e_{p^k}^{\rm sym}
:=\sqrt{w_{p,k}^{(\sigma)}}\,v_{p,k}^G.
}
\tag{8}
\]

Equation (5) immediately gives

\[
\boxed{
\|B_{\sigma,G}e_{p^k}^{\rm sym}\|^2
=(\log p)p^{-k\sigma}.
}
\tag{9}
\]

At the target value `sigma=1/2`,

\[
\boxed{
\|B_{1/2,G}e_{p^k}^{\rm sym}\|^2
=\frac{\log p}{p^{k/2}}
=\frac{\Lambda(p^k)}{\sqrt{p^k}}.
}
\tag{10}
\]

So the exact finite-place coefficient survives unchanged.

The important point is that the all-prime map is nevertheless bounded. For a finitely supported vector

\[
x=\sum_{p,k}x_{p,k}e_{p^k}^{\rm sym},
\]

put

\[
c_{p,k}
:=\frac{\sqrt{w_{p,k}^{(\sigma)}}}{\sqrt{d_p}}x_{p,k}.
\tag{11}
\]

The coefficient of the target basis vector `e_{(pq)^k}^{sym}` for an edge `{p,q}` is exactly

\[
c_{p,k}+c_{q,k}.
\tag{12}
\]

Therefore

\[
\begin{aligned}
\|B_{\sigma,G}x\|^2
&=\sum_{k\ge1}\sum_{\{p,q\}\in E}
|c_{p,k}+c_{q,k}|^2\\
&\le2\sum_{k\ge1}\sum_{\{p,q\}\in E}
\bigl(|c_{p,k}|^2+|c_{q,k}|^2\bigr)\\
&=2\sum_{p,k}d_p|c_{p,k}|^2\\
&=2\sum_{p,k}w_{p,k}^{(\sigma)}|x_{p,k}|^2.
\end{aligned}
\tag{13}
\]

For every fixed `sigma>0`,

\[
W_\sigma
:=\sup_{p,k\ge1}(\log p)p^{-k\sigma}
<\infty,
\tag{14}
\]

because the maximum over `k` occurs at `k=1` and `(log t)t^{-sigma}` is bounded on `[2,infinity)`. Hence

\[
\boxed{
\|B_{\sigma,G}\|^2\le2W_\sigma<\infty.
}
\tag{15}
\]

Thus `B_{sigma,G}` extends to a bounded operator on the Hilbert completion of `A` for **every** positive `sigma`, including `sigma=1/2`. Uniform boundedness of the vertex degrees is not required; local finiteness and the intrinsic normalization `d_p^{-1/2}` are enough.

Consequently

\[
Q_{\sigma,G}:=B_{\sigma,G}^*B_{\sigma,G}\succeq0
\tag{16}
\]

is a bounded positive Gram operator. Equations (6)--(8) give its matrix exactly:

\[
\langle e_{p^k}^{\rm sym},Q_{\sigma,G}e_{q^\ell}^{\rm sym}\rangle
=
\begin{cases}
w_{p,k}^{(\sigma)},&p=q,\ k=\ell,\\[1mm]
\displaystyle
\frac{\sqrt{w_{p,k}^{(\sigma)}w_{q,k}^{(\sigma)}}}
{\sqrt{d_pd_q}},
&p\ne q,\ k=\ell,\ \{p,q\}\in E,\\[3mm]
0,&\text{otherwise}.
\end{cases}
\tag{17}
\]

At criticality this is therefore an infinite-dimensional, bounded, positive, genuinely cross-prime Gram with the exact Mangoldt/half-density diagonal that `WP-261` showed could not be coherently received by any fixed finite-dimensional boundary.

## 3. The geometry is exactly a normalized unsigned incidence Gram

For each fixed exponent `k`, ignore the arithmetic weights momentarily and define the normalized unsigned incidence operator

\[
J_G e_p
:=\frac1{\sqrt{d_p}}
\sum_{q:\{p,q\}\in E}e_{\{p,q\}},
\tag{18}
\]

where the edge basis is orthonormal. Then

\[
J_G^*J_G
=I+D^{-1/2}AD^{-1/2},
\tag{19}
\]

with `A` the graph adjacency operator in form sense and `D=diag(d_p)`. Equation (13) is the direct incidence proof of

\[
0\preceq J_G^*J_G\preceq2I.
\tag{20}
\]

This is the normalized **signless-Laplacian** Gram rather than the oriented graph Laplacian. The plus sign is forced here because the same mixed-composite Fock state is reached from both endpoints with the same phase in (4).

Thus the positivity theorem is not mysterious and not arithmetic: it is ordinary incidence-Gram positivity. Graph incidence matrices, signless Laplacians, and normalized adjacency estimates are classical graph theory. No novelty is claimed for (19)--(20). The Mathia-specific content is that the existing symmetric prime-Fock occupation basis realizes the edge space internally and that the critical Fock coefficient carrier can be transported into this bounded incidence geometry without losing its exact diagonal.

A concrete infinite control is the path graph obtained by listing primes in increasing order and joining consecutive primes. Every degree is one or two, the graph is connected, and (15)--(17) give infinitely many nonzero cross-prime critical correlations. This proves that the `WP-261` finite-dimensional nonclosability theorem does not extend to arbitrary infinite-dimensional Fock-internal boundaries.

## 4. The escape is real analytically but fails the source-selection gate

The preceding construction satisfies several conditions that had looked close to the remaining frontier:

- the positive form lives inside the Mathia symmetric-Fock geometry;
- the critical diagonal is exactly `Lambda(p^k)/sqrt(p^k)`;
- positivity follows from a source-independent Gram theorem rather than RH;
- the map is bounded, hence closed/closable;
- infinitely many cross-prime matrix elements can be nonzero.

Nevertheless it does **not** answer the Weil-positivity mandate. The decisive defect is that the Fock structure used in `WP-256`--`WP-261` supplies the mixed-composite basis states but does not select the graph `G`. The same theorem works for every locally finite graph. A path, a tree, disjoint finite-degree components, an expander-like exhaustion, or many other incidence laws all preserve (9), (15), and positivity while producing different off-diagonal forms.

Even the off-diagonal phases are programmable. For each incidence `(p,e)` replace the coefficient `1/sqrt(d_p)` in (4) by

\[
\frac{\alpha_{p,e}}{\sqrt{d_p}},
\qquad |\alpha_{p,e}|=1.
\tag{21}
\]

The norm and boundedness proof are unchanged, while an edge `e={p,q}` contributes the phase

\[
\overline{\alpha_{p,e}}\alpha_{q,e}
\tag{22}
\]

to the off-diagonal Gram entry. In particular real signs can be flipped edge by edge while `B^*B` remains positive.

This is the infinite-dimensional analogue of the canonicity warning in `WP-222`: existence of a positive compression/correlation is not evidence that the arithmetic source selected the desired sign. Here the freedom occurs **before** any completed Weil comparison and while the exact critical diagonal is held fixed.

Using prime order to choose the path is a possible additional rule, but it is still an additional rule. Nothing in the existing Fock creation, gauge, permutation-fixed, Hamiltonian, or multiplicity structures proves that nearest-neighbor energy incidence is the correlation law entering the explicit formula. A future proposal must derive its relation from the source construction rather than choose it because its Gram has attractive properties.

## 5. Equal complete incidence does not canonically remove the graph choice

A natural response is to avoid choosing sparse edges and couple every pair of primes equally. Finite complete graphs give an exact matched control showing why this does not produce a nontrivial infinite correlation law.

Take `N` primes and the complete graph `K_N`. Then `d_p=N-1` for every vertex and

\[
v_{p,k}^{(N)}
=\frac1{\sqrt{N-1}}
\sum_{q\ne p}e_{(pq)^k}^{\rm sym}.
\tag{23}
\]

For `p\ne q`,

\[
\boxed{
\langle v_{p,k}^{(N)},v_{q,k}^{(N)}\rangle
=\frac1{N-1}.
}
\tag{24}
\]

The diagonal remains exactly one, but every fixed pairwise correlation tends to zero as the complete prime set grows:

\[
\frac1{N-1}\longrightarrow0.
\tag{25}
\]

Thus equal all-pairs incidence with unit diagonal converges on every fixed finite prime core to the orthogonal/separable control rather than to a nontrivial global coupling.

If the degree normalization is omitted instead, the unnormalized incidence vector has

\[
\|\sum_{q\ne p}e_{(pq)^k}^{\rm sym}\|^2=N-1,
\tag{26}
\]

so the diagonal in (9) acquires the factor `N-1` and diverges. The two simplest symmetric choices therefore give the exact dichotomy

\[
\boxed{
\text{equal complete incidence}
\Rightarrow
\begin{cases}
\text{normalized: fixed correlations vanish},\\
\text{unnormalized: exact diagonal diverges}.
\end{cases}
}
\tag{27}
\]

This does **not** rule out a dense all-prime kernel with nonuniform decaying edge weights, a measure-valued incidence space, or another infinite correspondence. It shows that such a construction must contain additional structure selecting those weights. Equal permutation-symmetric pair incidence does not supply the missing law for free.

## 6. Aggressive falsification and matched controls

**Arbitrary-label control.** Replace the primes by any countable label set, choose arbitrary bounded nonnegative diagonal weights `a_{j,k}`, and repeat (4) with any locally finite graph. The same incidence proof gives a bounded positive cross-label Gram. Therefore the analytic mechanism by itself is not Riemann-specific and survives generalized/random-label controls.

**Arithmetic-weight control.** The exact Mangoldt diagonal matters only through the scalar weights in (8). The incidence positivity theorem does not know that `w_{p,k}` came from prime energies, free-word multiplicity, or `Lambda`. This is precisely why the result is a narrowing rather than a positive Weil bridge.

**Support-programming control.** Given two different locally finite graphs on the same prime set, both constructions have identical diagonal coefficients but generally different zero patterns off diagonal. Hence diagonal data plus positivity plus closability do not determine the mixed-prime support.

**Phase-programming control.** Equation (21) keeps every source norm and the positive Gram theorem while changing off-diagonal phases. Therefore even a fixed support graph does not determine an oriented correlation law unless the source fixes the incidence phases.

**Target-space control.** `Q_{1/2,G}` is a positive form on the prime-power coefficient axis. The Weil finite-place term is an oriented translation/autocorrelation form on the Weil test space. No map derived here identifies the two. Feeding the same coefficients into the direct translation construction returns the sign and self-energy obstructions of `WP-005` and `WP-009`.

**Archimedean control.** The incidence construction contains no Gamma factor, pole term, or finite--archimedean completion. Adding such terms after the graph has already been selected would not explain why this particular cross-prime law was canonical.

**Dense-kernel boundary.** Equation (27) excludes only equal complete incidence in the ordinary Hilbert normalization. It does not exclude a source-derived nonuniform dense kernel, a different measure class, a correspondence module, or another operator category. Such an escape would be substantive precisely because it would have to derive the nonuniform coupling and its domain from Mathia/arithmetic structure rather than insert it.

These controls prevent the wrong conclusion. `WP-262` does not say that infinite-dimensional correlations cannot work. It says that **analytic admissibility of one such correlation is too easy to count as evidence**.

## 7. Prior-art and novelty boundary

The graph-theoretic component is classical. Unsigned vertex--edge incidence Grams give the signless Laplacian `D+A`; degree normalization gives `I+D^{-1/2}AD^{-1/2}` and the elementary bound by `2I`. The symmetric/bosonic Fock occupation basis is likewise standard and was already classicalized in `WP-259`--`WP-261`. No historical novelty is claimed for incidence operators, signless Laplacians, graph normalization, Fock symmetrization, or Gram positivity.

The bounded novelty audit did not identify a prior result asserting the Mathia-specific synthesis used here: transport of the exact symmetric-Fock Mangoldt coefficient carrier through mixed-composite occupation states to classify the infinite-dimensional escape left by `WP-261`. Absence from a bounded search is not a novelty proof, and the finding does not need historical novelty to be useful.

The durable result is the exact classification step. `WP-261` showed that finite-dimensional coherent boundary reception is impossible at the critical norms. `WP-262` shows that passing to an infinite-dimensional Fock-internal boundary immediately restores bounded closability and cross-prime positivity, but with large graph/phase programming freedom. Hence the meaningful gate was never merely the existence of an infinite-dimensional closable positive completion.

## 8. Consequence for the Weil-positivity search

The frontier should now be stated more strongly. A candidate completion must not merely provide

\[
\text{exact Mangoldt diagonal}
+\text{cross-prime terms}
+\text{positive closable Gram}.
\tag{28}
\]

Those properties admit a huge family of incidence realizations unrelated to the completed explicit formula. The next construction must instead derive, from the intrinsic Mathia/arithmetic source, a **specific all-prime correlation law that is not freely programmable by graph, phase, basis, or normalization choices**. It must survive matched generalized-prime controls, transport into the full Weil autocorrelation test geometry with the correct orientation, and generate the archimedean Gamma and polar terms in the same source-defined object.

This is a substantive narrowing of the live Fock route: `WP-261` identified the need for an infinite-dimensional closable correspondence; `WP-262` shows that such correspondences are plentiful. What remains difficult is **source selection plus the Weil sign**, not Hilbert-space closability by itself.