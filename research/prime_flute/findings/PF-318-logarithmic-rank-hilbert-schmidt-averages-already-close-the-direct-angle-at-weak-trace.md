# PF-318 — logarithmic-rank Hilbert–Schmidt averages already close the direct angle at weak trace

**Status:** `EXACT-DERIVED + HILBERT-SCHMIDT-COUNTING + PRIME-DENSITY-ENDPOINT + POSITIVE/ROUTE-SHARPENING`.

PF-317 reduces the direct physical angle to the local nearest-neighbor block

\[
K_{LH}=\sum_{r=-1}^1\sum_n L_{n+r}KH_n,
\]

and observes that the retained nonconstant-low target on module `n` has only `O(1+\log P_n)` dimensions. Combining that finite target rank with PF-210 gives the convenient sufficient estimate

\[
\|L_{n+r}KH_n\|\lesssim P_n^{-1}.
\]

That operator-norm target is stronger than the weak-`S_1` endpoint actually needs. It is enough for the **mean square** singular scale of each local `L/H` block to be reciprocal-prime:

\[
\boxed{
\|L_{n+r}KH_n\|_{\mathcal S_2}^2
\lesssim
\frac{1+\log P_n}{P_n^2},
\qquad r=-1,0,1.
}
\tag{1}
\]

Equivalently, if `m_{n,r}=\operatorname{rank}(L_{n+r}KH_n)=O(1+\log P_n)`, then (1) asks only that

\[
\frac1{m_{n,r}}
\sum_{j=1}^{m_{n,r}}s_j(L_{n+r}KH_n)^2
\lesssim P_n^{-2}.
\tag{2}
\]

No individual singular value is required to be `O(P_n^{-1})`. In particular the largest local singular value may be as large as

\[
O\!\left(\frac{\sqrt{\log P_n}}{P_n}\right)
\]

without violating (1). Thus the new criterion is genuinely weaker than PF-317's pointwise operator-norm target by a possible `\sqrt{\log P_n}` factor.

The proof is a two-scale counting argument. At singular threshold `\sigma`, prime modules with `P_n\le\sigma^{-1}` are controlled only by their logarithmic target rank, which costs `O(\sigma^{-1})` by Chebyshev's bound for `\vartheta(x)`. Modules with `P_n>\sigma^{-1}` are controlled instead by

\[
N_{B_n}(\sigma)
\le \sigma^{-2}\|B_n\|_{\mathcal S_2}^2,
\]

and the weighted prime tail

\[
\sum_{p>X}\frac{1+\log p}{p^2}
\lesssim X^{-1}
\]

again gives `O(\sigma^{-1})`. Hence every fixed offset is weak trace class, and the three offsets remain weak trace class by the finite-sum singular-value inequality already used in PF-199/PF-210.

Applied to PF-317, (1) implies

\[
K_{LH}\in\mathcal S_{1,\infty}
\quad\Longrightarrow\quad
Z_{LH}\in\mathcal S_{1,\infty},
\]

because PF-317 writes `Z_{LH}` as a two-sided contraction sandwich of `K_{LH}`. The same criterion applies to PF-317's explicitly flat-strip-normalized local blocks: its `1+O(P_n^{-2})` strip-normalizer comparison preserves the Hilbert–Schmidt scale.

This changes the live local calculation. Instead of controlling the worst high input into every low output, one may estimate the **aggregate high-frequency leakage of an orthonormal basis of the retained low target**. Since `K=K^*`,

\[
\boxed{
\|L_{n+r}KH_n\|_{\mathcal S_2}^2
=
\sum_{e\in\mathcal E_{n+r}^{L}}
\|H_nKe\|^2,
}
\tag{3}
\]

for any orthonormal basis `\mathcal E_{n+r}^{L}` of the finite-dimensional low target. Thus an average-square Fourier/DtN leakage estimate is already endpoint-complete even when a uniform operator-norm estimate is inaccessible.

## Claim

Let `P_n` run through the prime labels of the prime-flute tail. For each fixed offset `r` in a finite set `R`, let

\[
B_{n,r}:H_n\to L_{n+r}
\]

be compact finite-rank operators such that, for fixed `r`, the source spaces `H_n` are mutually orthogonal and the target spaces `L_{n+r}` are mutually orthogonal. Suppose there are constants `A,D` independent of `n,r` with

\[
\boxed{
\operatorname{rank}B_{n,r}
\le A(1+\log P_n),
}
\tag{4}
\]

and

\[
\boxed{
\|B_{n,r}\|_{\mathcal S_2}^2
\le D^2\frac{1+\log P_n}{P_n^2}.
}
\tag{5}
\]

Then for each fixed `r`,

\[
B^{(r)}:=\bigoplus_n B_{n,r}
\]

is compact and belongs to `\mathcal S_{1,\infty}`. Moreover the finite sum

\[
B:=\sum_{r\in R}B^{(r)}
\]

also belongs to `\mathcal S_{1,\infty}`, with a counting bound depending only on `A,D,|R|` and the fixed prime-density constants.

For the PF-317 direct channel take

\[
R=\{-1,0,1\},
\qquad
B_{n,r}=L_{n+r}KH_n.
\tag{6}
\]

The PF-212 physical low cutoff gives (4) on the canonical tail. Therefore the Hilbert–Schmidt estimate (5) alone implies

\[
\boxed{
K_{LH}\in\mathcal S_{1,\infty}
\quad\text{and}\quad
Z_{LH}\in\mathcal S_{1,\infty}.
}
\tag{7}
\]

No operator-norm estimate `\|B_{n,r}\|=O(P_n^{-1})` is required.

## 1. Threshold counting with rank below the prime scale

For a compact operator `T`, write

\[
N_T(\sigma)=\#\{j:s_j(T)>\sigma\}.
\]

Because the fixed-offset blocks are orthogonal on both source and target sides, their singular values form a multiset union, exactly as in PF-199/PF-210:

\[
N_{B^{(r)}}(\sigma)
=\sum_n N_{B_{n,r}}(\sigma).
\tag{8}
\]

Fix `0<\sigma\le1` and put

\[
X=\sigma^{-1}.
\tag{9}
\]

For modules with `P_n\le X`, use only rank:

\[
\sum_{P_n\le X}N_{B_{n,r}}(\sigma)
\le
A\sum_{p\le X}(1+\log p).
\tag{10}
\]

PF-210 proves from the central-binomial-coefficient Chebyshev argument that

\[
\vartheta(X):=\sum_{p\le X}\log p\le C X,
\]

and `\pi(X)\le (\log2)^{-1}\vartheta(X)`. Hence

\[
\boxed{
\sum_{P_n\le X}N_{B_{n,r}}(\sigma)
\le C X
=\frac C\sigma.
}
\tag{11}
\]

This is the same prime-density gain as PF-210, but no local operator-norm cutoff has been used.

## 2. Hilbert–Schmidt counting above the prime scale

For every compact `T`,

\[
\sigma^2N_T(\sigma)
\le\sum_js_j(T)^2
=\|T\|_{\mathcal S_2}^2.
\tag{12}
\]

Therefore (5) gives

\[
\sum_{P_n>X}N_{B_{n,r}}(\sigma)
\le
\frac{D^2}{\sigma^2}
\sum_{p>X}\frac{1+\log p}{p^2}.
\tag{13}
\]

The remaining prime tail follows from the same Chebyshev estimate by dyadic decomposition. On

\[
2^kX<p\le2^{k+1}X
\]

one has

\[
\begin{aligned}
\sum_{2^kX<p\le2^{k+1}X}
\frac{1+\log p}{p^2}
&\le
\frac1{(2^kX)^2}
\sum_{p\le2^{k+1}X}(1+\log p)\\
&\le \frac{C}{2^kX}.
\end{aligned}
\tag{14}
\]

Summing `k\ge0` yields

\[
\boxed{
\sum_{p>X}\frac{1+\log p}{p^2}
\le\frac C X.
}
\tag{15}
\]

Equations (13), (15), and `X=\sigma^{-1}` give

\[
\boxed{
\sum_{P_n>X}N_{B_{n,r}}(\sigma)
\le\frac C\sigma.
}
\tag{16}
\]

Combining (11) and (16),

\[
\boxed{
N_{B^{(r)}}(\sigma)\le\frac C\sigma.
}
\tag{17}
\]

The large-`\sigma` regime is harmless, so `B^{(r)}\in\mathcal S_{1,\infty}`.

Compactness also follows directly: (5) implies

\[
\|B_{n,r}\|
\le\|B_{n,r}\|_{\mathcal S_2}
\lesssim\frac{\sqrt{1+\log P_n}}{P_n}
\longrightarrow0,
\]

and each block has finite rank. Thus the finite partial orthogonal sums converge in operator norm.

## 3. Three local pant offsets cost only a fixed constant

PF-214/PF-317 give exactly three module offsets for `K_{LH}`. For a finite family of compact operators, the standard Fan counting inequality used in PF-199 gives

\[
N_{S+T}(a+b)
\le N_S(a)+N_T(b).
\tag{18}
\]

Applying (18) to the `|R|` fixed offsets at threshold `\sigma/|R|` and using (17) gives

\[
N_B(\sigma)
\le
\sum_{r\in R}N_{B^{(r)}}(\sigma/|R|)
\le\frac{C_R}{\sigma}.
\tag{19}
\]

Thus finite nearest-neighbor overlap creates no logarithmic endpoint loss.

For PF-317, the target rank estimate follows from PF-212's fixed physical cutoff:

\[
\dim L_j=O(1+L_j)=O(1+\log P_j).
\]

For `r=-1,0,1`, adjacent prime labels have comparable logarithms on the tail, so (4) is uniform in the three offsets. If (5) holds, equations (17)--(19) prove the first implication in (7). PF-317 then gives

\[
Z_{LH}
=(I+K_{LL})^{-1/2}K_{LH}(I+K_{HH})^{-1/2},
\]

with both diagonal factors contractions, hence

\[
s_j(Z_{LH})\le s_j(K_{LH}),
\]

which proves the second implication.

## 4. The local target becomes an averaged leakage estimate

Let

\[
B_{n,r}=L_{n+r}KH_n.
\]

Since `K` is positive and self-adjoint,

\[
B_{n,r}^*=H_nKL_{n+r}.
\]

If `\mathcal E_{n+r}^{L}` is any orthonormal basis of `\operatorname{Ran}L_{n+r}`, then

\[
\begin{aligned}
\|B_{n,r}\|_{\mathcal S_2}^2
&=\|B_{n,r}^*\|_{\mathcal S_2}^2\\
&=\sum_{e\in\mathcal E_{n+r}^{L}}
\|H_nKe\|^2.
\end{aligned}
\tag{20}
\]

This identity is useful because the output band is explicit and finite. A proof of PF-317's stronger operator-norm target must control the worst unit vector in the entire high source. By contrast, (20) asks for the summed high-frequency leakage generated by only `O(\log P_n)` explicit low Fourier modes.

Thus any local DtN/pseudodifferential estimate of the form

\[
\sum_{e\in\mathcal E_{n+r}^{L}}
\|H_nKe\|^2
\lesssim
\frac{1+\log P_n}{P_n^2}
\tag{21}
\]

already closes the direct-angle endpoint. Individual low rows may be worse than `P_n^{-1}` provided the square average remains at reciprocal-prime scale.

PF-317's flat shifted-strip replacement changes the source/target seam-energy normalizers by bounded factors `1+O(P_n^{-2})`; Schatten-2 norms are stable under bounded two-sided multiplication. Hence (21) may be tested with the explicit flat strip normalizer used in the accepted direct-angle clue.

## Prior-art and novelty audit

No novelty is claimed for the operator-ideal ingredients. The estimate `N_T(\sigma)\le\sigma^{-2}\|T\|_{\mathcal S_2}^2` is the elementary counting inequality for a Hilbert–Schmidt singular-value sequence. Weak Schatten/Lorentz ideals defined by `\sup_j j^{1/p}s_j(T)` and the corresponding singular-value counting language are standard; modern Cwikel--Solomyak literature uses the same framework. The finite-sum estimate is the classical Ky Fan singular-value inequality already audited in PF-199. The prime input is exactly the elementary Chebyshev `\vartheta(X)=O(X)` bound proved inside PF-210; (15) is its immediate dyadic tail consequence.

The project-specific contribution is the **endpoint combination** of those elementary facts with PF-317's three-offset locality and PF-212's logarithmic low-band rank. PF-210 required a reciprocal-prime **operator norm** per logarithmic-rank module. The present result shows that the PF-317 direct angle needs only reciprocal-prime **root-mean-square singular scale**. That changes the next geometric proof obligation from worst-case `L/H` decoupling to an averaged high-leakage estimate over the explicit finite low band.

A targeted literature check found only the standard weak-Schatten/singular-value framework and standard Chebyshev-function estimates; no external result was found that states this prime-indexed logarithmic-rank Hilbert--Schmidt endpoint criterion or its Prime-Flute application. Novelty is claimed only for this project-specific reduction, not for the underlying ideal or number-theoretic inequalities.

## Boundaries and falsification

1. **The Hilbert–Schmidt estimate is not proved here.** Equation (5)/(21) is the new local sufficient target, not an established property of the pant DtN block.
2. **Logarithmic target rank is load-bearing.** A raw inverse-seam population of order `s_n^{-1}` cannot be substituted for (4); PF-226/PF-227 show why such a replacement would be dangerous.
3. **Mean square is enough, arbitrary large rows are not.** The criterion permits a `\sqrt{\log P_n}` loss in the largest singular value but not concentration whose squared mass exceeds (5).
4. **Finite offset locality is load-bearing.** The last step uses PF-214/PF-317's fixed three-offset structure; an unbounded number of reassembly colors would require a new count.
5. **No trace-class conclusion is claimed.** The result is exactly at weak `S_1`; the per-module trace-norm envelope can still be non-summable.
6. **Only the direct channel is addressed.** PF-316 still requires the independent conditional channel `T_H` to satisfy its own weak-trace bound before the full physical angle closes.
7. **Constant-mode growth remains irrelevant to this criterion.** PF-215's divergent constant-to-constant block lies outside the retained nonconstant-low target and does not falsify (21). A genuine negative result must force excess Hilbert–Schmidt mass in the nonconstant `L/H` corner itself.

The immediate falsification test is therefore concrete: compute or bound the left side of (21) for the actual flat-normalized one-pant block. Growth larger than `C(1+\log P_n)/P_n^2` along a canonical subsequence would kill this averaged endpoint route even if individual singular values still tend to zero.