# FD-204 — Lowbit prime-shell trees achieve logarithmic resistance at critical-exponent random cost

- **Date:** 2026-09-19
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** multiscale prime-shell projection / source-localization / effective-resistance reduction / random-multiplicative benchmark
- **Depends on:** FD-197, FD-201, FD-202, FD-203
- **Classification:** `EXACT-DERIVED + MULTISCALE-PRIME-TREE + LOGARITHMIC-RESISTANCE + SOURCE-LOCALIZED-RANDOM-COST + CRITICAL-EXPONENT-BASELINE`

## Claim

`FD-203` leaves a concrete design problem: replace the prime path by sparse nonlocal signed edges that reduce inverse resistance without paying back the old `H^(3/2)` diagonal random tariff. A binary lowbit tree does exactly this up to logarithms.

Retain the fixed-mode cross-horizon sensor of `FD-201--FD-203`. Let

\[
K:=\lfloor\sqrt H\rfloor,
\qquad
K/2<p_1<\cdots<p_m\le K,
\]

and

\[
S_i:=S_{r,H}(p_i)
=
M\!\left(\left\lfloor\frac{rH}{p_i}\right\rfloor\right)
-
M\!\left(\left\lfloor\frac H{p_i}\right\rfloor\right),
\qquad r\ge2.
\]

Reverse the shell indexing so that the endpoint anchor `p_m` is node `j=0`: node `j` corresponds to `p_(m-j)`. For `j>=1`, write

\[
\lambda(j):=2^{\nu_2(j)},
\qquad
b(j):=j-\lambda(j),
\]

and join `j` to `b(j)`. Define

\[
Q_{\mathrm{lb}}(S)
:=
\sum_{j=1}^{m-1}
\left|
S_{m-j}-S_{m-b(j)}
\right|^2,
\]

\[
N_{\mathrm{lb}}(S)
:=
Q_{\mathrm{lb}}(S)+|S_m|^2,
\qquad
\mathcal G_{r,H}^{\mathrm{lb}}
:=K N_{\mathrm{lb}}(S).
\]

Then:

1. the lowbit graph is a rooted tree, and the exact squared dual norm of point evaluation at node `j` is

\[
\boxed{
\|e_{m-j}\|_{\mathrm{lb},*}^2
=
1+\operatorname{popcount}(j).
}
\]

Consequently

\[
\boxed{
\max_i \|e_i\|_{\mathrm{lb},*}^2
=
1+\lfloor\log_2 m\rfloor
}
\]

for `m>=2`. Thus the anchored inverse resistance drops from the `Theta(m)` path cost in `FD-203` to `Theta(log m)`.

2. For the same squarefree Rademacher multiplicative source used in `FD-197`, `FD-202` and `FD-203`,

\[
\boxed{
\mathbb E\,\mathcal G_{r,H}^{\mathrm{lb}}
=O_r(H\log K)
=H^{1+o(1)}.
}
\]

Hence the improved conditioning does **not** restore the `H^(3/2)` diagonal tariff. It costs only one logarithm over the critical `H` exponent.

3. Deterministically, any physical-Mobius bound of the form

\[
\mathcal G_{r,H}^{\mathrm{lb}}
=O\!\left(H\log^C H\right)
\]

would imply uniformly over the entire prime shell

\[
\boxed{
|S_i|
=
O\!\left(
K^{1/2}\log^{(C+1)/2} K
\right),
}
\]

up to harmless changes of the logarithmic exponent from replacing `log H` by `log K`. Thus a multiscale nonlocal projection can simultaneously retain the RH-sized square-root scale for all these cross-horizon Mertens increments and keep the random benchmark at critical **power** exponent `1`.

This is not yet an RH criterion. The `S_i` are interval increments `M(floor(rH/p_i))-M(floor(H/p_i))`, not absolute Mertens values, and no bound for `mathcal G_(r,H)^lb` is proved here for the physical Mobius source. The result isolates a viable observation geometry and removes the specific path-resistance obstruction of `FD-203`.

## 1. Exact logarithmic resistance

The parent operation

\[
j\mapsto j-2^{\nu_2(j)}
\]

clears the least significant nonzero binary digit of `j`. Repeating it therefore reaches zero after exactly

\[
\operatorname{popcount}(j)
\]

steps. Every nonroot node has one parent, the index strictly decreases along parent edges, and all nodes reach zero, so the graph is a rooted tree.

Use the root value and tree-edge differences as coordinates. In those coordinates the anchored norm is Euclidean:

\[
N_{\mathrm{lb}}(S)
=
|S_m|^2+
\sum_{e\in T_{\mathrm{lb}}}|\Delta_e S|^2.
\]

For the node indexed by `j`, point evaluation is the root value plus the signed sum of edge differences along its unique path to the root. That path has exactly `popcount(j)` edges. Its representing coefficient vector therefore has `1+popcount(j)` entries of modulus one, proving the exact dual formula.

For `1<=j<m`, the largest possible population count is `floor(log_2 m)`: the witness `j=2^q-1` works for `q=floor(log_2 m)`, and no smaller-than-`m` integer can require more binary digits. Hence

\[
|S_i|^2
\le
\left(1+\lfloor\log_2 m\rfloor\right)
N_{\mathrm{lb}}(S)
\]

uniformly in the shell.

This directly answers the conditioning half of the `FD-203` design problem. The path needed `Theta(m)` squared amplification from a distant endpoint anchor; the lowbit tree needs only `Theta(log m)`.

## 2. Every nonlocal edge remains source-localized

Put

\[
L_i:=\left\lfloor\frac H{p_i}\right\rfloor,
\qquad
R_i:=\left\lfloor\frac{rH}{p_i}\right\rfloor.
\]

For any shell indices `a<b`, the fixed-mode sensor satisfies the exact identity

\[
S_a-S_b
=
\sum_{R_b<n\le R_a}\mu(n)
-
\sum_{L_b<n\le L_a}\mu(n).
\]

Thus a nonlocal tree edge is still the difference of two explicit source slabs; it is not a transform-side coefficient with no arithmetic interpretation. Moreover, for `r>=2` the upper and lower slabs are disjoint. Indeed `p_b<2p_a<=r p_a`, so

\[
\frac{rH}{p_b}>\frac H{p_a}
\]

and therefore `R_b>=L_a` after flooring.

The key multiscale fact is a bounded-overlap property. In reversed index coordinates, the edge from `j` to `b(j)` spans the boundary interval

\[
(j-2^{\nu_2(j)},j].
\]

Fix a scale `s`. The indices with `nu_2(j)=s` are `j=(2q+1)2^s`, and their boundary intervals

\[
(2q\,2^s,(2q+1)2^s]
\]

are pairwise disjoint. Hence any adjacent prime boundary is crossed by at most one lowbit edge at each dyadic scale, and therefore by at most

\[
1+\lfloor\log_2 m\rfloor
\]

edges in total.

Because every long `L`-slab or `R`-slab is the disjoint union of the corresponding adjacent slabs, this index-space overlap bound transfers exactly to the source intervals. That is the mechanism that keeps the random price small despite the nonlocal edges.

## 3. Random-multiplicative cost

Let

\[
f(n)=\mu(n)^2\prod_{p\mid n}X_p
\]

be the squarefree Rademacher multiplicative source. As in `FD-197`,

\[
\mathbb E[f(a)f(b)]
=
\mu(b)^2\mathbf 1_{a=b}.
\]

For an edge joining shell indices `a<b`, the two source slabs above are disjoint, so

\[
\mathbb E|S_a^f-S_b^f|^2
=
\sum_{L_b<n\le L_a}\mu(n)^2
+
\sum_{R_b<n\le R_a}\mu(n)^2.
\]

Summing over all lowbit edges and using the bounded-overlap property gives the explicit upper bound

\[
\mathbb E Q_{\mathrm{lb}}(S^f)
\le
\left(1+\lfloor\log_2 m\rfloor\right)
\left(
\sum_{L_m<n\le L_1}\mu(n)^2
+
\sum_{R_m<n\le R_1}\mu(n)^2
\right).
\]

No prime-gap estimate is needed. Since `p_1>K/2`, `p_m<=K` and `K=floor(sqrt H)`,

\[
L_1-L_m=O(K),
\qquad
R_1-R_m=O_r(K).
\]

Therefore, even the trivial bound `mu(n)^2<=1` yields

\[
\mathbb E Q_{\mathrm{lb}}(S^f)
=O_r(K\log m).
\]

The endpoint anchor is the same one already audited in `FD-203`:

\[
\mathbb E|S_m^f|^2=O_r(K).
\]

Multiplying by `K` gives

\[
\boxed{
\mathbb E\,\mathcal G_{r,H}^{\mathrm{lb}}
=O_r(K^2\log m)
=O_r(H\log K).
}
\]

The statement is deliberately an upper bound, not an asymptotic. The present argument proves that the lowbit geometry has critical power exponent `1`; it does not prove that the logarithmic overhead is necessary for this particular source.

## 4. Consequence and remaining boundary

Suppose an analytic Farey argument could prove

\[
\mathcal G_{r,H}^{\mathrm{lb}}
=O(H\log^C H)
\]

for the physical Mobius source. Since `H/K=K+O(1)`,

\[
N_{\mathrm{lb}}(S)
=O(K\log^C K).
\]

Combining this with the exact logarithmic point-evaluation resistance gives

\[
|S_i|^2
=O(K\log^{C+1}K),
\]

uniformly over the prime shell. Thus the same observation family simultaneously avoids both obstructions isolated earlier: it does not overcount each long interval independently as in `FD-201`, and it does not propagate an anchor through `Theta(m)` path resistance as in `FD-203`.

The remaining gap is now outside this finite-dimensional conditioning problem. Uniform control of the `S_i` gives square-root-sized **multiplicative-interval increments** of Mertens. To reach an RH criterion one still needs either an outer cross-scale telescoping/anchoring mechanism that recovers absolute `M(n)`, or a direct representation-native Farey quantity that controls `mathcal G_(r,H)^lb` at only polylogarithmic loss. FD-204 supplies neither step.

There is also a natural optimization question left open by the logarithm: is there another sparse signed graph on the ordered prime shell whose source slabs have only `O(1)` aggregate overlap while its anchored effective-resistance diameter is `O(log m)` or better? The path has optimal `O(H)` random scale but `Theta(m)` resistance; the lowbit tree has `O(H log K)` random cost and `Theta(log m)` resistance. Determining the best achievable cost-resistance tradeoff is now a concrete finite combinatorial problem tied to the exact source-slab representation.

## 5. Representation, prior-art and formalization audits

The construction is representation-safe. Randomness is introduced at the multiplicative source before the Farey transform, exactly as in `FD-197`, and every nonlocal shell edge is mapped back by an exact identity to two Mobius source slabs with all floors retained. The lowbit tree itself is intentionally a transform-side projection; the arithmetic claim is only the exact slab identity and its bounded source-overlap consequence.

The binary lowbit decomposition is standard data-structure prior art: Peter M. Fenwick's 1994 binary indexed tree organizes cumulative information by binary portions of the index and supports logarithmic traversals. Effective resistance/Dirichlet energy on trees is likewise classical. A targeted search found those generic ingredients but no Farey/Mertens use of the lowbit tree to balance source-interval reuse against prime-shell inverse resistance. Neither external ingredient is load-bearing here: the required parent-depth, overlap and point-evaluation statements are proved directly above. `SOURCES.md` therefore remains unchanged.

No clue status changes. The accepted local clues concern different Farey-order or source-compatibility mechanisms and are neither proved nor falsified by this prime-mode multiscale projection. No formalization issue is opened: the finite lowbit-tree lemmas are elementary, while the substantive research boundary is the still-missing analytic control and outer cross-scale recovery.

## Conclusion

`FD-203` showed that the critical random source cost and good inverse conditioning had separated on the prime path. FD-204 reconnects them up to logarithms. A sparse lowbit tree keeps every edge exactly source-localized, reuses each adjacent source slab only `O(log m)` times, and reduces anchored point-evaluation resistance from `Theta(m)` to `Theta(log m)`. Its squarefree-random scaled cost is only `O(H log K)=H^(1+o(1))`.

So the lost half power is no longer forced by either diagonal squaring or path resistance. The live problem is sharper: obtain a natural Farey bound for this multiscale projected energy and recover absolute Mertens information across scales, or improve the finite cost-resistance tradeoff further.