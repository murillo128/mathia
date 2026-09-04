# WP-149 — Spectator-prime parallel paths collapse resultant resistance and the finite-energy space

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PRIME-CIRCLE + CYCLOTOMIC-RESULTANT + GRAPH-DIRICHLET + SPECTATOR-PRIME-AMPLIFICATION + ZERO-EFFECTIVE-RESISTANCE + TRIVIAL-ENERGY-QUOTIENT + MEASURE-INDEPENDENT-DENSITY-OBSTRUCTION + MATCHED-FINITE-PRIME-CONTROL + PRIOR-ART-AUDITED`

## Claim

`WP-148` proved that the canonical conservative graph-Laplacian completion of the normalized Prime-Circle resultant kernel is positive on every finite cutoff but has infinite degree at every vertex, and that its finite-energy domain inside the natural counting `ell^2` shell space is `{0}`. It explicitly left open a source-forced non-counting vertex measure, a noncompact energy-space quotient, or another topology on the same positive resultant graph.

Those escapes do not work for the **unchanged canonical resultant Dirichlet energy**. The obstruction is stronger than infinite vertex degree. Every nonzero resultant edge has infinitely many pairwise edge-disjoint spectator-prime bypasses whose total parallel conductance is infinite. Consequently the effective resistance between the endpoints of every resultant edge is zero. Since the resultant graph is connected, every function of finite global Dirichlet energy is constant.

Thus the canonical positive energy space modulo constants is itself trivial, independently of any ambient `ell^2` vertex measure. For every faithful positive atomic measure on the shell set, the intersection of the finite-energy space with `ell^2(mu)` is either `{0}` or the one-dimensional constant space, hence is never dense. Changing only the shell measure cannot rescue `WP-148`; a viable continuation must change the interaction, the admissible objects, or the finite--archimedean coupling before the all-prime Dirichlet limit.

## 1. The normalized resultant graph

For distinct shell indices `m,n`, write

\[
J_{m,n}
=
\frac{\log|\operatorname{Res}(\Phi_m,\Phi_n)|}
{\sqrt{\varphi(m)\varphi(n)}}\ge0.
\tag{1}
\]

By Apostol's cyclotomic-resultant theorem, `J_{m,n}>0` exactly when one index is obtained from the other by multiplying by a prime power. `PC-004` identifies the interior prime-power values with the critical Weil half-density, while `WP-145`--`WP-148` study the same zero-order kernel as a candidate finite-place interaction.

The canonical conservative completion of `WP-148` has extended Dirichlet energy

\[
\mathcal E(f)
=
\frac12\sum_{u\ne v}J_{u,v}|f_u-f_v|^2
=
\sum_{\{u,v\}}J_{u,v}|f_u-f_v|^2.
\tag{2}
\]

No ambient vertex measure appears in (2). A measure matters only when one later asks whether the finite-energy functions form a dense domain in a chosen `ell^2(mu)` space.

## 2. A spectator prime copies every resultant edge exactly

Fix any edge `m<n` with

\[
n=mp^k,
\qquad c:=J_{m,n}>0.
\tag{3}
\]

Let `r` be any prime not dividing `mn`. Multiplication by this spectator prime scales both Euler populations by the same factor,

\[
\varphi(mr)=(r-1)\varphi(m),
\qquad
\varphi(nr)=(r-1)\varphi(n).
\tag{4}
\]

The quotient `(nr)/(mr)=p^k` is unchanged. Apostol's formula therefore scales the logarithmic resultant by the same factor `r-1`, so the square-root normalization cancels it exactly:

\[
\boxed{J_{mr,nr}=J_{m,n}=c.}
\tag{5}
\]

At the same time, the two fresh-prime edges have the universal weight already derived in `WP-148`,

\[
\boxed{
J_{m,mr}=J_{n,nr}
=:a_r
=\frac{\log r}{\sqrt{r-1}}.
}
\tag{6}
\]

Hence every spectator prime produces a three-edge bypass

\[
m\longleftrightarrow mr\longleftrightarrow nr\longleftrightarrow n
\tag{7}
\]

with conductances `a_r,c,a_r`. Distinct spectator primes give pairwise edge-disjoint bypasses; they share only the endpoints `m,n`.

This exact spectator invariance is the load-bearing arithmetic fact. It is stronger than merely having infinitely many neighbors at `m`: every original arithmetic edge is replicated as the middle edge of infinitely many parallel squares in the multiplicative shell graph.

## 3. The parallel conductance is infinite

Regard an edge of conductance `w` as a resistor of resistance `1/w`. The total series resistance of the bypass (7) is

\[
R_r
=
\frac2{a_r}+\frac1c,
\tag{8}
\]

so its effective conductance is

\[
g_r=R_r^{-1}.
\tag{9}
\]

Because `a_r=(\log r)/\sqrt{r-1}\to0`, for all sufficiently large spectator primes one has `a_r\le c`, and then

\[
R_r
\le \frac3{a_r},
\qquad
\boxed{g_r\ge\frac{a_r}{3}.}
\tag{10}
\]

Moreover

\[
a_r=\frac{\log r}{\sqrt{r-1}}\ge\frac1r
\tag{11}
\]

for every sufficiently large `r` (indeed already for small `r` as well). Euler's divergence of the reciprocal primes therefore gives

\[
\sum_{\substack{r\ \mathrm{prime}\\r\nmid mn}}g_r
\ge
\frac13\sum_{r\gg1}\frac1r
=\infty.
\tag{12}
\]

In a finite subnetwork containing any finite set `S` of these edge-disjoint bypasses, the bypasses are parallel between `m` and `n`. Thus its effective conductance between those endpoints is at least

\[
\sum_{r\in S}g_r,
\tag{13}
\]

in addition to the direct edge of conductance `c`. Consequently

\[
R_{\mathrm{eff},S}(m,n)
\le
\left(c+\sum_{r\in S}g_r\right)^{-1}
\longrightarrow0
\tag{14}
\]

as the spectator primes are exhausted.

So the natural finite-network trace limit **short-circuits every nonzero resultant edge**:

\[
\boxed{R_{\mathrm{eff}}(m,n)=0\qquad\text{whenever }J_{m,n}>0.}
\tag{15}
\]

This conclusion uses only positive conductances and finite subnetworks; it does not depend on choosing a self-adjoint realization of an infinite-degree Laplacian.

## 4. Every finite-energy function is constant

The same statement follows directly at the form level and is stronger for the present purpose. Let `f` be any complex-valued function with `\mathcal E(f)<\infty`, and put

\[
\Delta=f_m-f_n.
\tag{16}
\]

For one spectator prime `r`, let `E_r(f)` be the contribution of the three bypass edges:

\[
E_r(f)
=a_r|f_m-f_{mr}|^2
+c|f_{mr}-f_{nr}|^2
+a_r|f_{nr}-f_n|^2.
\tag{17}
\]

Weighted Cauchy--Schwarz along the path gives the series-resistance inequality

\[
|\Delta|^2
\le
\left(\frac2{a_r}+\frac1c\right)E_r(f)
=R_rE_r(f).
\tag{18}
\]

Hence, for all sufficiently large spectator primes,

\[
E_r(f)
\ge g_r|\Delta|^2
\ge\frac{a_r}{3}|\Delta|^2.
\tag{19}
\]

The bypass edge sets are pairwise disjoint, so their energies may be summed without overcounting. Equations (11)--(12) imply

\[
\mathcal E(f)
\ge
\sum_rE_r(f)
=\infty
\tag{20}
\]

unless `\Delta=0`. Therefore every finite-energy function satisfies

\[
f_m=f_n
\qquad\text{on every edge with }J_{m,n}>0.
\tag{21}
\]

The resultant graph is connected: if

\[
n=\prod_{j=1}^s p_j^{\alpha_j},
\]

then one reaches `n` from `1` by multiplying successively by the prime powers `p_j^{\alpha_j}`, each of which is a nonzero resultant edge. Thus (21) propagates globally and gives

\[
\boxed{
\{f:\mathcal E(f)<\infty\}
=
\{\text{constant functions}\}.
}
\tag{22}
\]

In particular the canonical energy Hilbert space modulo constants is the zero space. There is no nontrivial resistance boundary or noncompact finite-energy quotient to extract from the unchanged all-prime resultant conductances.

## 5. No faithful change of vertex measure can make the same form densely defined

Let `mu` be any faithful positive atomic measure on the countable shell set, so `mu(m)>0` for every shell retained by the arithmetic model. Consider the same Dirichlet energy (2) as a candidate quadratic form in

\[
\ell^2(\mu).
\tag{23}
\]

Equation (22) is independent of `mu`. Therefore

\[
\operatorname{Dom}(\mathcal E)\cap\ell^2(\mu)
=
\begin{cases}
\mathbb C\mathbf1,&\sum_m\mu(m)<\infty,\\
\{0\},&\sum_m\mu(m)=\infty.
\end{cases}
\tag{24}
\]

Because infinitely many shells have positive measure, neither space is dense in `ell^2(mu)`. Hence

\[
\boxed{
\text{changing only the faithful shell measure cannot turn the canonical resultant energy into a densely defined positive form.}
}
\tag{25}
\]

This strictly strengthens the counting-space statement of `WP-148`. The failure is not that counting measure was the wrong Hilbert normalization; the all-prime conductance network has already collapsed before an ambient `ell^2` measure is chosen.

Allowing zero measure on infinitely many shell vertices would quotient away arithmetic states and is not a faithful realization of the same Prime-Circle shell system. Altering the conductances by measure-dependent factors would likewise define a different energy and must be justified from Mathia independently.

## 6. Matched controls

The collapse is specifically an all-prime spectator effect.

If the multiplicative shell graph is restricted to a finite prime alphabet, every edge has only finitely many available spectator-prime bypass directions. The sum in (12) is then finite, and the argument forcing `f_m=f_n` disappears. This matches `WP-148`, which already showed finite weighted degree and ordinary finite-support energy on a finite prime alphabet.

Likewise, the proof would fail for a hypothetical deformation in which the fresh-prime conductances were summable. What matters is not merely graph connectivity or graph-Laplacian positivity but the combination of exact spectator replication (5) with the nonsummable critical fresh-prime weights (6).

Thus an apparently attractive repair such as a different shell measure cannot change the decisive series/parallel network invariant. To avoid the collapse one must modify at least one of the load-bearing ingredients before taking the global positive limit: the critical resultant conductances, the spectator-prime replication, or the way finite and archimedean sectors are assembled.

## 7. Relation to the previous Weil-positivity findings

`WP-145` showed that differentiating the log-resultant to obtain an independently positive Hessian destroys prime-power support and the `log p` amplitudes. `WP-146` kept the zero-order kernel and showed that ordinary conditional positivity already fails on a mixed-prime three-chain. `WP-147` amplified that failure to unbounded two-sided primitive inertia, excluding bounded-codimension and finite-rank repairs. `WP-148` then found the most canonical full-rank diagonal repair: the graph Laplacian is positive at every finite cutoff but has infinite degree and trivial domain in counting `ell^2`.

The present result closes two explicit escape routes left by `WP-148`: a source-forced non-counting vertex measure and a noncompact finite-energy/resistance quotient of the **same** graph. The reason is an exact arithmetic self-similarity not used in `WP-148`: spectator multiplication reproduces every original resultant edge while creating infinitely many parallel bypasses of divergent total conductance.

This is also distinct from `WP-096`--`WP-107`. Those findings constrain positive multiplicative-Toeplitz/prime-torus completions and their critical diagonal or information cost. Here the object is the concrete Prime-Circle cyclotomic-resultant graph, and the obstruction is electrical/Dirichlet degeneration of its canonical conservative completion.

## 8. Prior-art and novelty audit

The ingredients of the network argument are classical and are not claimed as new mathematics. T. M. Apostol, *Resultants of cyclotomic polynomials*, Proc. Amer. Math. Soc. **24** (1970), 457--462, supplies the prime-power resultant law. Series/parallel resistance, Rayleigh monotonicity, and graph Dirichlet energies are standard. For infinite weighted-network energy and resistance spaces see, for example, P. E. T. Jorgensen and E. P. J. Pearse, *A Hilbert space approach to effective resistance metric*, Complex Anal. Oper. Theory **4** (2010), 975--1013, arXiv:0906.2535, and P. Jorgensen and F. Tian, *Infinite weighted graphs with bounded resistance metric*, Math. Scand. **123** (2018), 278--308, DOI `10.7146/math.scand.a-106208`.

Directed searches combining `cyclotomic resultant`, `effective resistance`, `resistance network`, and `Dirichlet energy` did not locate a treatment of this normalized resultant graph or the spectator-prime short-circuit mechanism. The novelty claim is therefore deliberately narrow and Mathia-specific: equations (5)--(22) specialize classical network inequalities to the exact Prime-Circle normalized resultant weights and show that their all-prime conservative positive completion has only constant finite-energy functions.

This is not a new Weil criterion, not an RH-equivalent positivity theorem, and not evidence for RH. It is a decisive negative about one Mathia-native route that otherwise had the unusually strong property of retaining the exact finite-prime selector while acquiring an independent positive sign.

## 9. Consequence for the research mandate

The canonical resultant graph now fails in a stronger sense than `WP-148` established. Finite cutoffs are honest positive geometries, but the arithmetic all-prime limit becomes an ideal short circuit: every pair connected by a resultant edge has zero limiting effective resistance, all such equalities propagate through the connected multiplicative graph, and the global finite-energy quotient contains no geometry at all.

Therefore the route

\[
\boxed{
\text{exact normalized resultant selector}
\to
\text{canonical conservative graph positivity}
\to
\text{change of vertex measure / resistance completion}
\not\to
\text{nontrivial global Weil-positive geometry}
}
\tag{26}
\]

is closed for the unchanged all-prime interaction.

A surviving construction must change category before this parallel-path collapse occurs: for example, a source-forced mixed-prime interaction that changes the network, a finite--archimedean coupling that is nonseparable before the Dirichlet form is formed, or a different Mathia-native cohomological/boundary object whose positivity is not the conservative resultant graph energy. Such a construction must still preserve the exact finite prime-power coefficients and generate the archimedean/polar terms intrinsically.

## Internal dependencies

- `research/prime_circle/findings/PC-004-normalized-resultants-weil-local-kernels.md`
- `research/weil_positivity/findings/WP-096-exact-cover-positive-forms-are-prime-torus-grams-but-sparse-weil-support-needs-infinite-diagonal.md`
- `research/weil_positivity/findings/WP-145-resultant-hessian-positivity-loses-prime-power-support-and-splits-real-place-curvature.md`
- `research/weil_positivity/findings/WP-146-critical-resultant-kernel-is-conditionally-indefinite-on-mixed-prime-three-chain.md`
- `research/weil_positivity/findings/WP-147-disjoint-resultant-chains-force-unbounded-primitive-two-sided-inertia.md`
- `research/weil_positivity/findings/WP-148-canonical-resultant-graph-laplacian-has-infinite-critical-degree-and-trivial-l2-domain.md`
