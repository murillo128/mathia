# FD-131 — vanishing worst-level ancestry defect survives every fixed low-rank Möbius anchor

**Status:** `EXACT-DERIVED + APPROXIMATE-ANCESTRY + PRIME-EDGE-GRAPH + FIXED-RANK-ANCHOR + LEVELWISE-NORMALIZATION + COFINITE-EXACT-PRIME-DIRECTIONS + VANISHING-WORST-LEVEL-DEFECT + MACROSCOPIC-MOBIUS-DISAGREEMENT + NEGATIVE/OBSTRUCTION`.

`FD-130` rules out the plain global mean of prime-ancestry defects: a whole multiplicative-rank interface can contain only `O(H)` bad edges and disappear inside the complete prime-edge volume. A natural repair is to normalize **separately at every multiplicative rank** and then take the worst rank, so the rank cut used in `FD-130` can no longer hide.

That repair is still insufficient if the normalization continues to average over prime directions inside each rank. For every fixed anchor depth `K`, one can replace the rank cut by a fixed finite-prime subcube cut. The resulting common infinite source agrees exactly with Möbius through rank `K`, satisfies exact Möbius ancestry in all but `K+1` prime directions, and yet its normalized defect tends to zero **uniformly over all multiplicative ranks** while the source remains different from Möbius on a positive proportion of integers.

For `H>=2` and `j>=0`, refine the complete ancestry graph of `FD-130` by
\[
\mathcal E_{j,H}
:=
\{(p,n):p\text{ prime},\ n\le H/p\text{ squarefree},\ p\nmid n,\ \omega(n)=j\}.
\tag{1}
\]
For fixed `1<=r<infinity`, define the worst level-normalized defect
\[
\mathfrak L_{r,H}(a)
:=
\sup_{\substack{j\ge0\\|\mathcal E_{j,H}|>0}}
\frac1{|\mathcal E_{j,H}|}
\sum_{(p,n)\in\mathcal E_{j,H}}
|a_{pn}+a_n|^r.
\tag{2}
\]

Then for every fixed `K>=0` there is one squarefree-supported unit-sign source `a^(K)` such that
\[
a^{(K)}_n=\mu(n)\qquad(\omega(n)\le K),
\tag{3}
\]
and
\[
\boxed{\mathfrak L_{r,H}(a^{(K)})\longrightarrow0}
\qquad(H\to\infty),
\tag{4}
\]
while
\[
\boxed{
\liminf_{H\to\infty}
\frac1H\#\{n\le H:a^{(K)}_n\ne\mu(n)\}>0.
}
\tag{5}
\]
Moreover, the ancestry identity `a_{pn}=-a_n` is exact for every prime outside one fixed set of `K+1` primes.

Thus even the **supremum of all rankwise mean defects** has no scale-uniform coercivity toward the Möbius source after any fixed low-rank anchor. Rank visibility alone does not repair `FD-130`; an ancestry norm must also prevent dilution across prime directions, use a genuinely local/supremum condition, let the anchor depth grow, or bypass coefficient recovery.

## 1. A finite-prime subcube gauge preserves the low-rank anchor

Put
\[
s:=K+1,\qquad
Q:=p_1p_2\cdots p_s,
\tag{6}
\]
where `p_1,...,p_s` are any fixed distinct primes. On squarefree integers define
\[
b_Q(n):=
\begin{cases}
-1,&Q\mid n,\\
+1,&Q\nmid n,
\end{cases}
\qquad
a^{(K)}_n:=\mu(n)b_Q(n),
\tag{7}
\]
and put `a_n^(K)=0` on nonsquarefree integers.

If `omega(n)<=K=s-1`, then `Q` cannot divide `n`, so `b_Q(n)=1` and (3) follows. The source therefore preserves exactly the same fixed low-rank Möbius anchor contemplated after `FD-130`.

For an ancestry edge `n -> pn`, the Möbius factor already contributes the required sign change:
\[
a^{(K)}_{pn}+a^{(K)}_n
=
\mu(n)\bigl(b_Q(n)-b_Q(pn)\bigr).
\tag{8}
\]
Hence an edge is defective exactly when
\[
Q\mid pn,\qquad Q\nmid n.
\tag{9}
\]
Because `p\nmid n`, this means that `p` is one of the `s` primes dividing `Q` and `n` contains all the other prime factors of `Q`.

In particular, if `p\nmid Q`, then
\[
b_Q(pn)=b_Q(n)
\quad\text{and}\quad
a^{(K)}_{pn}=-a^{(K)}_n
\tag{10}
\]
for every admissible `n`. Thus **all but finitely many prime directions satisfy exact Möbius ancestry globally**. The only defects lie in the fixed coordinate set `p|Q`.

## 2. Exact rankwise defect count

Let
\[
N_m(H):=
\#\{u\le H:u\text{ squarefree},\ \omega(u)=m\},
\tag{11}
\]
and
\[
N_{m,Q}(H):=
\#\{u\le H:u\text{ squarefree},\ \omega(u)=m,\ Q\mid u\}.
\tag{12}
\]

Every rank-`j+1` squarefree child `u` has exactly `j+1` prime parents `u/p`. Therefore
\[
\boxed{
|\mathcal E_{j,H}|=(j+1)N_{j+1}(H).
}
\tag{13}
\]

Now suppose `u` is divisible by `Q`. Removing any one of the `s` primes of `Q` gives a parent for which (9) holds, while removing a prime outside `Q` leaves both parent and child divisible by `Q` and creates no defect. Conversely every defective edge has a child divisible by `Q`. Hence the number of defective edges in level `j` is exactly
\[
\boxed{
B_{j,Q}(H)=s\,N_{j+1,Q}(H).
}
\tag{14}
\]

Each defective edge has `|a_{pn}+a_n|=2`. Consequently, whenever the level is nonempty,
\[
\boxed{
D_{r,j,H}
:=
\frac1{|\mathcal E_{j,H}|}
\sum_{(p,n)\in\mathcal E_{j,H}}
|a^{(K)}_{pn}+a^{(K)}_n|^r
=
2^r\frac{s}{j+1}
\frac{N_{j+1,Q}(H)}{N_{j+1}(H)}.
}
\tag{15}
\]

This already gives the uniform tail bound
\[
D_{r,j,H}\le 2^r\frac{s}{j+1}.
\tag{16}
\]
Unlike the rank-step gauge of `FD-130`, no single low level carries a macroscopic fraction of bad edges.

## 3. Every fixed rank loses the fixed-prime subcube

For each fixed integer `m>=1`, Landau's classical fixed-`m` almost-prime theorem gives
\[
N_m(H)
\sim
\frac{H(\log\log H)^{m-1}}{(m-1)!\log H}.
\tag{17}
\]
The squarefree/distinct-prime form used here is exactly the `pi_m` version of that theorem.

If `m<s`, then `N_{m,Q}(H)=0`. If `m=s`, then `N_{s,Q}(H)=1` once `H>=Q`, whereas `N_s(H)\to\infty`. If `m>s`, division by `Q` gives the elementary bound
\[
N_{m,Q}(H)
\le
N_{m-s}(H/Q).
\tag{18}
\]
Applying (17) at the two fixed ranks `m` and `m-s` yields
\[
\boxed{
\frac{N_{m,Q}(H)}{N_m(H)}
=
O_{m,Q}\bigl((\log\log H)^{-s}\bigr)
\longrightarrow0.
}
\tag{19}
\]

Therefore `D_{r,j,H}->0` for every fixed level `j`. To upgrade this pointwise statement to the worst-level norm (2), fix `epsilon>0` and choose `J` so large that
\[
2^r\frac{s}{J+1}<\epsilon.
\tag{20}
\]
By (16), every level `j>=J` already has `D_{r,j,H}<epsilon` for every `H`. There are only finitely many levels `j<J`; by (19) each of their defects tends to zero. Hence for sufficiently large `H` all of them are also below `epsilon`. This proves
\[
\boxed{
\sup_{\substack{j\ge0\\|\mathcal E_{j,H}|>0}}
D_{r,j,H}\longrightarrow0,
}
\tag{21}
\]
which is (4).

The quantifier order matters. No uniform-in-`m` form of Landau's theorem is being imported. One first controls the high-rank tail by the exact degree factor `s/(j+1)`, and then uses the classical fixed-rank asymptotic only on finitely many remaining levels.

## 4. Vanishing worst-level defect still does not recover Möbius

Whenever `n` is squarefree and divisible by `Q`, equation (7) gives
\[
a^{(K)}_n=-\mu(n)\ne\mu(n).
\tag{22}
\]
Such integers have positive lower density. A self-contained lower bound, parallel to `FD-130`, is enough. Put `X=floor(H/Q)` and restrict to
\[
m\le X,\qquad m\equiv1\pmod Q.
\tag{23}
\]
These `m` are coprime to `Q`. Removing those divisible by `q^2` for a prime `q\nmid Q` and using the Chinese remainder theorem gives
\[
\#\{m\le X:m\equiv1\!\!\pmod Q,\ m\text{ squarefree}\}
\ge
(2-\zeta(2))\frac{X}{Q}-O_Q(\sqrt X).
\tag{24}
\]
For every retained `m`, the integer `n=Qm` is squarefree, at most `H`, and satisfies (22). Therefore
\[
\boxed{
\#\{n\le H:a^{(K)}_n\ne\mu(n)\}
\ge
(2-\zeta(2))\frac{H}{Q^2}-O_Q(\sqrt H).
}
\tag{25}
\]
This proves (5). In particular, for every fixed finite `r>=1`,
\[
\liminf_{H\to\infty}
\frac1H\sum_{n\le H}|a^{(K)}_n-\mu(n)|^r
\ge
2^r\frac{2-\zeta(2)}{Q^2}>0.
\tag{26}
\]

Combining (21) and (26) rules out any constant `C=C(K,r)` independent of `H` for which all squarefree-unit sources satisfy
\[
\frac1H\sum_{n\le H}|a_n-\mu(n)|^r
\le
C\,\mathfrak L_{r,H}(a).
\tag{27}
\]

Thus the failure in `FD-130` is not repaired merely by preventing dilution **between multiplicative ranks**. This witness dilutes the boundary **within every rank**, across the increasing collection of prime directions.

## 5. What this removes from the current frontier

The obstruction is deliberately stronger than `FD-130` in the direction that result left open. Its rank-step witness has an entire level `K -> K+1` defective, so a worst-level normalization detects it immediately. The present finite-prime subcube gauge replaces that interface by a codimension-`s` coordinate cut: defects occur across all sufficiently high ranks, but their fraction in each individual level tends to zero. Taking the supremum over levels still loses the source.

The witness also has more exact ancestry than cardinality alone suggests: every prime direction outside the fixed set dividing `Q` is exact at every scale. This does not contradict `FD-129`. A complete growing prime prefix eventually insists on every prime dividing `Q` as well; exact recovery then forbids this gauge. Here those finitely many directions remain approximate, and levelwise averaging lets their defect vanish.

The surviving multiplicative route is therefore narrower. A coercive condition must keep **prime-direction information** visible as well as multiplicative rank, use a genuinely local or `L^infinity` defect that sees the size-`2` bad edges, let the exact anchor depth grow so that a fixed `Q` is eventually frozen out, or prove a direct Fourier-skeleton estimate that does not pass through coefficient recovery. The theorem does not show that such stronger conditions work.

It also does **not** construct a Fourier-skeleton saturating source and does not provide a square-root partial-sum envelope. As in `FD-130`, the conclusion is a stability obstruction: vanishing approximate-ancestry defect under a natural stronger normalization still does not imply Möbius-like coefficients.

## 6. Adversarial checks and prior-art boundary

The exact edge count was checked both by child degree and by direct finite enumeration for several `K` and horizons. The two descriptions agree: every `Q`-divisible rank-`j+1` child contributes exactly `s` bad parents and no other edge is bad. The `j<K` anchor levels have zero defect; the first unanchored level has only `s` bad edges over `(K+1)N_{K+1}(H)` total edges and hence already vanishes.

The only external theorem used in the proof is the classical fixed-`m` almost-prime asymptotic (17). E. M. Wright's proof of Landau's theorem explicitly covers the distinct-prime counting function required here; it is anchored in `SOURCES.md`. No uniform Sathe--Selberg estimate, RH input, or zero-density theorem is used.

A targeted prior-art audit also checked neighboring Boolean-cube/slice influence and edge-isoperimetric literature. Coordinate and finite-subcube cuts with small averaged influence are classical phenomena, so no novelty is claimed for that general graph principle. The line-specific result is the exact transplantation to the truncated Möbius prime-ancestry graph, including the fixed-rank Möbius anchor, cofinite exact prime directions, the all-ranks supremum in (21), and the positive-density coefficient failure. No external source was found that supplies this Farey/Möbius stability statement directly.

The boundary conditions are sharp for the claim made here. The result is for every fixed finite `r`; an `L^infinity` edge defect does not vanish because the bad edges retain size `2`. The anchor depth `K` is fixed; a growing `K(H)` is a different hypothesis. The construction leaves finitely many prime directions defective; a condition that monitors each such direction without averaging it away can detect this witness. These stronger regimes remain open rather than being ruled out by (21).
