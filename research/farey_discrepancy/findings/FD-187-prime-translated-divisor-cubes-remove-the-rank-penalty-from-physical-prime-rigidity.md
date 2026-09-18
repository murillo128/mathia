# FD-187 — Prime-translated divisor cubes remove the rank penalty from physical-prime rigidity

- **Date:** 2026-09-18
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** exact finite q-capacity certificate / strengthened physical-prime rigidity
- **Depends on:** FD-181, FD-186

## Claim

FD-186 proves that, on the squarefree fibre with physical prime values `a(p)=-1`, one changed composite already forces prime-extension energy of order `x/log x`. Its finite certificate used one direct edge and one factor-by-factor detour, losing a factor `(omega(n_0)+1)^(q-1)`. That loss is not intrinsic. Every fresh prime translates the **entire divisor Boolean cube** of the changed coefficient into the prime-extension graph, and the exact `q`-capacity of that cube replaces the path-length penalty.

Let `a` be real-valued, supported on the squarefree integers, with

\[
a(1)=1,\qquad a(p)=-1\quad\text{for every prime }p,
\tag{1}
\]

and let

\[
\mathcal M_{a,q}(x)
:=
\sum_{\substack{n,pn\le x\\\mu^2(n)=\mu^2(pn)=1\\p\text{ prime}}}
|a(pn)-a(p)a(n)|^q,
\qquad 1\le q<\infty.
\tag{2}
\]

Choose any changed squarefree composite

\[
n_0=p_1\cdots p_k,\qquad k=\omega(n_0)\ge2,
\qquad
\Delta:=|a(n_0)-\mu(n_0)|>0.
\tag{3}
\]

For `q>1` define

\[
B_{k,q}
:=
1+
\sum_{j=0}^{k-1}
\left(k\binom{k-1}{j}\right)^{-1/(q-1)}.
\tag{4}
\]

Then for every sufficiently large `x`,

\[
\boxed{
\mathcal M_{a,q}(x)
\ge
\bigl(\pi(x/n_0)-k\bigr)
\frac{\Delta^q}{B_{k,q}^{\,q-1}}
\qquad(q>1),
}
\tag{5}
\]

while for `q=1`,

\[
\boxed{
\mathcal M_{a,1}(x)
\ge
\bigl(\pi(x/n_0)-k\bigr)\Delta.
}
\tag{6}
\]

Hence the prime number theorem gives

\[
\boxed{
\liminf_{x\to\infty}
\frac{\log x}{x}\mathcal M_{a,q}(x)
\ge
\frac{\Delta^q}{n_0 B_{k,q}^{\,q-1}}>0
\qquad(q>1),
}
\tag{7}
\]

with the evident denominator `1` for `q=1`.

This strictly strengthens the FD-186 coefficient for every `k>=2` and `q>1`, because `B_{k,q}<k+1`. More importantly, for every fixed `q>1`,

\[
\boxed{B_{k,q}\longrightarrow1\qquad(k\to\infty).}
\tag{8}
\]

Thus the earlier multiplicative-rank penalty disappears asymptotically: apart from the unavoidable fan-density factor `1/n_0`, a high-rank defect costs asymptotically the full local amount `Delta^q` per fresh-prime certificate.

For `q=2`, the formula has the exact electrical interpretation

\[
B_{k,2}
=
1+R_{\mathrm{opp}}(Q_k),
\qquad
R_{\mathrm{opp}}(Q_k)
=
\sum_{j=0}^{k-1}\frac1{k\binom{k-1}{j}},
\tag{9}
\]

where `Q_k` is the unit-resistor `k`-cube and the resistance is between antipodal vertices. The extra `1` is the direct prime-extension edge in series with that cube.

## 1. Normalize multiplicativity to an ordinary graph gradient

Exactly as in FD-186, on squarefree integers put

\[
c(n):=\frac{a(n)}{\mu(n)}.
\tag{10}
\]

Because `|mu(n)|=1` on this fibre and `a(p)=-1=mu(p)`, every prime has `c(p)=1`, while

\[
|a(pn)-a(p)a(n)|
=
|c(pn)-c(n)|.
\tag{11}
\]

Also `Delta=|c(n_0)-1|`. This is a pointwise sign normalization, not a reconstruction or change of information.

Fix a prime `r<=x/n_0` with `r` not dividing `n_0`. Inside the physical prime-extension graph take the finite subgraph `G_r` consisting of:

- the direct edge `n_0 -- n_0 r`;
- every vertex `r d` with `d|n_0`;
- every edge `r d -- r d p_i` whenever `p_i` does not divide `d`.

The translated vertices `r d` form exactly the Boolean divisor cube `Q_k`: the bottom vertex is `r`, the top vertex is `n_0r`, and multiplication by one of the `p_i` changes one Boolean coordinate. All vertices are squarefree and at most `n_0r<=x`. The two boundary values relevant to the finite variational problem are

\[
c(r)=1,
\qquad
c(n_0)=1\pm\Delta.
\tag{12}
\]

Thus any actual source assignment on `G_r` has at least the minimum possible `q`-energy among all vertex assignments with those two boundary values.

## 2. The exact finite q-capacity is a weighted layer chain

Permuting the factors `p_1,...,p_k` acts transitively on every Hamming layer of the cube while fixing the two boundary vertices `r` and `n_0` and the direct edge. For `q>1`, convexity lets us average any admissible assignment over this symmetry group without increasing its energy. Therefore a minimizer may be taken constant on each cube layer.

Between layers `j` and `j+1` there are

\[
m_j
=
\binom{k}{j}(k-j)
=
k\binom{k-1}{j}
\tag{13}
\]

parallel unit edges. Let `t_*` be the increment across the direct edge and `t_j` the increment between layers `j` and `j+1`. Their signed sum is the prescribed boundary difference,

\[
t_*+\sum_{j=0}^{k-1}t_j=\pm\Delta,
\tag{14}
\]

and the energy is

\[
|t_*|^q+
\sum_{j=0}^{k-1}m_j|t_j|^q.
\tag{15}
\]

Weighted Hölder gives

\[
\Delta
\le
\left(
|t_*|^q+\sum_jm_j|t_j|^q
\right)^{1/q}
\left(
1+\sum_jm_j^{-1/(q-1)}
\right)^{(q-1)/q}.
\tag{16}
\]

The second factor is `B_(k,q)^((q-1)/q)`. Equality is attainable by taking all increments with the same sign and magnitudes proportional to `1` on the direct edge and to `m_j^{-1/(q-1)}` on layer `j`. Consequently

\[
\boxed{
\inf_{f(n_0)-f(r)=\pm\Delta}
\sum_{e\in E(G_r)}|\nabla f(e)|^q
=
\frac{\Delta^q}{B_{k,q}^{q-1}}.
}
\tag{17}
\]

This is an **exact** finite certificate, not merely a lower bound obtained from a selected path.

For `q=1`, a path from `n_0` to `r` gives total variation at least `Delta`, and equality is obtained by setting every translated-cube vertex equal to `1`, leaving the whole jump on the direct edge. Hence the exact minimum is `Delta`, proving the local form of (6).

When `q=2`, (15) is ordinary electrical energy. Collapsing equal-potential Hamming layers puts the conductances `m_j` in series, so the antipodal cube resistance is `sum_j 1/m_j`; adding the direct edge gives (9). For example, `B_(2,2)=2`, `B_(3,2)=11/6`, and `B_(4,2)=5/3`, compared with the FD-186 path denominators `3,4,5`.

## 3. Fresh-prime cubes are edge-disjoint

The local certificates can be summed. If `r` and `s` are distinct primes not dividing `n_0`, a translated-cube vertex `r d`, `d|n_0`, contains exactly one prime outside the fixed factor set `{p_1,...,p_k}`, namely `r`. Unique factorization therefore prevents a cube edge belonging to `G_r` from also belonging to `G_s`.

The direct edges `n_0--n_0r` are distinct for distinct `r`. A direct edge cannot be a translated-cube edge because its parent `n_0` contains no fresh prime, whereas both endpoints of every cube edge contain the corresponding fresh prime. The subgraphs may share the vertex `n_0`, but they share no edge, which is exactly what the energy sum requires.

There are `pi(x/n_0)-k` admissible fresh primes once `x` is large enough that all prime divisors of `n_0` are included. Summing (17) over those edge-disjoint subgraphs gives (5)--(6), and PNT gives (7).

## 4. The capacity penalty tends to one

Write `alpha=1/(q-1)>0`. The excess over one is

\[
B_{k,q}-1
=
\sum_{j=0}^{k-1}
\left(k\binom{k-1}{j}\right)^{-\alpha}.
\tag{18}
\]

Fix an integer `J` with `(J+1)alpha>1`. The `2J` boundary-layer terms are `O_J(k^{-alpha})`. On the remaining layers `J<=j<=k-1-J`, unimodality of the binomial coefficients gives

\[
\binom{k-1}{j}\ge\binom{k-1}{J}\asymp_J k^J,
\tag{19}
\]

so their total contribution is

\[
O_J\!\left(k\,[k\binom{k-1}{J}]^{-\alpha}\right)
=O_J\!\left(k^{1-(J+1)\alpha}\right)=o(1).
\tag{20}
\]

This proves (8). Also every `m_j>=1`, so `B_(k,q)<=k+1`, with strict inequality for `k>=2`; hence (5) dominates FD-186 at every finite rank as well.

The interpretation is useful. The single-detour proof paid for graph distance because it selected one route. The full divisor cube has exponentially many overlapping routes, and its `q`-capacity between antipodes grows enough that the effective series cost of the cube vanishes relative to the unavoidable direct edge. The only asymptotic loss that remains in (7) is the natural density `pi(x/n_0)~x/(n_0 log x)` of fresh-prime copies.

## 5. Consequence and boundary

FD-186 already proves qualitative rigidity on the physical-prime fibre. FD-187 strengthens the quantitative modulus: the coefficient of `x/log x` attached to a changed `n_0` no longer deteriorates like a power of `omega(n_0)`. For fixed `q>1`, high multiplicative rank actually makes the finite detour certificate closer to its local optimum.

This does **not** solve the Farey observation-design problem left by FD-182. The prime-extension energy is still an added source-side relational observable; no new inequality here derives it from midpoint data or from a specified sparse family of Farey spatial samples. Nor does this remove the moved-prime escape classified by FD-185: the normalization `c(p)=1` is essential to pin the bottom vertex of every translated divisor cube.

The representation audit is clean. The map `a -> c=a/mu` is pointwise and isometric on squarefree coefficients, and every edge of every Boolean cube used above is an actual prime-extension multiplicativity edge. The improved constant comes from retaining more of the existing source graph, not from adding measurements or using an invertible transform with hidden conditioning.

## 6. Prior-art and novelty boundary

The finite graph mechanism is classical in its generic form. Effective resistance on hypercubes is standard electrical-network material; for example Jeremy Moody and P. K. Aravind, *Resistor Networks based on Symmetrical Polytopes*, Electronic Journal of Graph Theory and Applications **3**(1) (2015), 56--69, DOI `10.5614/ejgta.2015.3.1.7`, treats hypercube resistor networks. Nonlinear `p`-resistance / `p`-energy on graphs is also established prior art; see Morteza Alamgir and Ulrike von Luxburg, *Phase transition in the family of p-resistances*, NeurIPS 24 (2011), and the later p-resistance literature.

No novelty is claimed for effective resistance, p-capacity, convex symmetrization on a cube, or the weighted Hölder minimization in (16). Those facts are rederived above so no external graph theorem is load-bearing. A targeted prior-art search did not surface the arithmetic embedding used here: one changed Möbius coefficient, replicated over fresh primes, produces edge-disjoint translated divisor cubes whose exact capacity sharpens the `x/log x` prime-extension rigidity constant. The only asymptotic theorem imported into the claim is PNT, already anchored in `SOURCES.md` through Newman.

## 7. Falsification checks

The main failure modes were checked explicitly.

First, using only one path reproduces FD-186 and loses `(k+1)^(q-1)`; the gain therefore genuinely comes from parallel divisor routes. Second, different fresh-prime cubes are only vertex-overlapping at `n_0`, not edge-overlapping, so summing their energies does not double-count. Third, the direct edge must remain in the finite network: omitting it would compare `c(r)` with the unconstrained value `c(n_0r)` and would not certify the defect at `n_0`. Fourth, the argument fails if prime values move, because then `c(r)` is no longer pinned to `1`; this is exactly the separate FD-185 branch rather than a hidden extension of the present theorem.

For `q=2`, direct Laplacian solves for `k=2,...,6` agree with the layer formula `R_opp(Q_k)=sum_j [k binom(k-1,j)]^{-1}`. These finite checks support the indexing and series reduction but are not used as evidence for the proof.

## Research disposition

Proved. The physical-prime source-side separator is now quantitatively stronger than FD-186: the exact translated-divisor-cube certificate replaces the path-length rank penalty by a `q`-capacity factor `B_(k,q)^(q-1)` with `B_(k,q)->1`. The live Farey-side question remains unchanged: identify minimal spatial Farey information that controls prime-extension energy below the critical `x/log x` scale, or prove that a proposed sparse spatial sensor still has a null source carrying this relation energy.