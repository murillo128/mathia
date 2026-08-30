# WI-046 — truncated welding local mains have uniform interval discrepancy under nonuniform weights

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + PRIOR-ART-REDIRECTION + NEEDS-AUDIT`. This finding does **not** certify the Yang--Yang one-sided fourth-moment theorem and does not change Mathia's current unconditional simple-critical proportion. It strengthens WI-045 at one precise interface: after truncating the deterministic singular-series local product at primes `p<=P`, its product along the structured welding shifts has a discrepancy over **every integer interval** bounded by

\[
\boxed{
D(P)=4\prod_{3\le p\le P}\left(\frac p{p-1}\right)^2
\ll (\log P)^2,
}
\]

uniformly in the coprime prime-power bases `(b1,b2)`. No complete CRT period is required. By Abel summation, any deterministic weight of bounded variation therefore incurs at most `D(P)` times its endpoint-plus-variation norm. At the Yang deterministic cutoff `P=40`,

\[
D(40)
=\frac{10319775578685444001}{228252171475353600}
=45.212168243489245\ldots.
\]

This removes a specific concern left open by WI-045: nonuniform **deterministic local residue weighting** does not by itself destroy the local `S1/S2/S3` centering. The unresolved welding problem remains genuinely analytic: the raw prime-dependent glue, the locally centered prime residual, moving windows, major/minor-arc errors, diagonal/Poisson bookkeeping, and the exact consumer normalization still have to be controlled before any Yang--Yang proportion can be promoted.

## 1. Source and exact object

The pinned public source remains

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`.

Its `scripts/t2_swaps.py` defines, for fixed `b1,b2`,

\[
A(b_2,j)=\sum_m\Lambda(m)
\Lambda\!\left(\frac{b_2m+j}{b_1}\right)
1_{b_1\mid b_2m+j},
\]

and expands the `S1` square by the exact equal-lock relation. With

\[
g=(b_1,b_2),\qquad r=b_1/g,\qquad q=b_2/g,
\]

one has

\[
m'=m-rk,\qquad n'=n-qk.
\tag{1}
\]

WI-045 reconstructed the deterministic local main for the two pair shifts in the asymptotically dominant coprime family, where `(r,q)=(b1,b2)`, and proved the finite CRT identity

\[
\frac1Q\sum_{k\bmod Q}
\tau_Q(b_1k)\tau_Q(b_2k)
=E_{2,Q}(b_1,b_2).
\tag{2}
\]

The remaining local question was whether a nonuniform `k`-weight could correlate strongly with the residue classes and invalidate the use of the unweighted CRT mean. The calculation below answers that finite/truncated question quantitatively.

Primary source artifacts:

- `paper.tex`, the one-sided fourth-moment section, especially the exact dispersion swaps and the statement that the glue layer uses factorized mains plus Abel summation;
- `scripts/t2_swaps.py`, especially `e2_const`, the exact `S1/S2/S3` swaps, and `kmax=(hi-lo)//r+1`;
- WI-033 for the logarithmic prime-power Mertens measure and bounded continuum selector geometry;
- WI-045 for the exact local collision identity and the `o(1)` mass of noncoprime prime-power base pairs.

## 2. Local factors have a positive divisor expansion

For a prime `p`, write the ordinary two-point Hardy--Littlewood local factor as in WI-045:

\[
\tau_p(h)=
\begin{cases}
A_p:=\dfrac p{p-1},&p\mid h,\\[2mm]
B_p:=\dfrac{p(p-2)}{(p-1)^2},&p\nmid h.
\end{cases}
\tag{3}
\]

Assume `(b1,b2)=1`.

### Generic odd primes

If `p\nmid b1 b2`, multiplication by either base is invertible modulo `p`, so the two divisibility events coincide with `p|k`. Hence

\[
\tau_p(b_1k)\tau_p(b_2k)
=B_p^2\bigl(1+a_p1_{p\mid k}\bigr),
\tag{4}
\]

where

\[
a_p=\frac{A_p^2}{B_p^2}-1
=\frac{2p-3}{(p-2)^2}>0.
\tag{5}
\]

### Coefficient odd primes

If, say, `p|b1` and `p\nmid b2`, then the first factor is always `A_p` while the second distinguishes `p|k`. Thus

\[
\tau_p(b_1k)\tau_p(b_2k)
=A_pB_p\bigl(1+c_p1_{p\mid k}\bigr),
\tag{6}
\]

with

\[
c_p=\frac{A_p}{B_p}-1
=\frac1{p-2}>0.
\tag{7}
\]

The case `p|b2` is symmetric. Since the bases are coprime, no odd prime divides both.

### The prime 2

Whether both bases are odd or exactly one is even,

\[
\boxed{
\tau_2(b_1k)\tau_2(b_2k)=4\,1_{2\mid k}.
}
\tag{8}
\]

This is the exact parity mode already identified in WI-044/WI-045.

## 3. Exact interval discrepancy bound

Let

\[
Q_P=\prod_{p\le P}p,
\qquad
F_P(k)=\prod_{p\le P}\tau_p(b_1k)\tau_p(b_2k).
\tag{9}
\]

For every odd `p<=P`, let `alpha_p=a_p` in the generic case and `alpha_p=c_p` at a coefficient prime. Let `C_p=B_p^2` or `A_pB_p` respectively, and put

\[
C_P=\prod_{3\le p\le P}C_p,
\qquad
\alpha_d=\prod_{p\mid d}\alpha_p
\quad(d\mid Q_P/2).
\tag{10}
\]

Expanding the positive Euler factors gives the exact divisor formula

\[
\boxed{
F_P(k)
=4C_P\,1_{2\mid k}
\sum_{\substack{d\mid Q_P/2\\d\mid k}}\alpha_d.
}
\tag{11}
\]

Let `I` be any interval of `K` consecutive integers and let `N_I(m)` be the number of multiples of `m` in `I`. Then

\[
\sum_{k\in I}F_P(k)
=4C_P\sum_{d\mid Q_P/2}\alpha_d N_I(2d).
\tag{12}
\]

For every `m`, independently of the interval location and without assuming `K>=m`,

\[
\left|N_I(m)-\frac Km\right|\le1.
\tag{13}
\]

The period mean of (11) is the finite local collision mean of WI-045,

\[
\bar F_P
=E_{2,Q_P}(b_1,b_2).
\tag{14}
\]

Subtracting `K\bar F_P` from (12) and applying (13) therefore gives

\[
\left|\sum_{k\in I}(F_P(k)-\bar F_P)\right|
\le
4C_P\sum_{d\mid Q_P/2}\alpha_d
=4C_P\prod_{3\le p\le P}(1+\alpha_p).
\tag{15}
\]

Now the source-specific cases disappear completely. At a generic prime,

\[
B_p^2(1+a_p)=A_p^2,
\tag{16}
\]

while at a coefficient prime,

\[
A_pB_p(1+c_p)=A_p^2.
\tag{17}
\]

Consequently

\[
\boxed{
\left|\sum_{k\in I}
\left(F_P(k)-E_{2,Q_P}(b_1,b_2)\right)\right|
\le
4\prod_{3\le p\le P}\left(\frac p{p-1}\right)^2
=:D(P).
}
\tag{18}
\]

The bound is independent of `b1,b2`, the location and length of `I`, and the enormous CRT modulus `Q_P`. Mertens' product theorem gives

\[
D(P)\asymp (\log P)^2,
\tag{19}
\]

and the upper bound `D(P)\ll(log P)^2` is all that is needed below.

For the finite deterministic truncation used in the Yang one-sided main, `P=40`, direct exact rational multiplication gives

\[
\boxed{
D(40)
=\frac{10319775578685444001}{228252171475353600}
<45.213.
}
\tag{20}
\]

## 4. Abel summation handles arbitrary bounded-variation deterministic weights

Let `a_k=F_P(k)-E_{2,Q_P}` and let `w_k` be any real weights supported on an integer interval `I=[u,v]`. By (18), every prefix partial sum

\[
A(t)=\sum_{u\le k\le t}a_k
\]

satisfies `|A(t)|<=D(P)`. Discrete Abel summation yields

\[
\sum_{k=u}^{v}w_k a_k
=w_vA(v)+\sum_{k=u}^{v-1}(w_k-w_{k+1})A(k),
\]

and therefore

\[
\boxed{
\left|\sum_{k\in I}w_k
(F_P(k)-E_{2,Q_P})\right|
\le
D(P)\left(
|w_v|+\sum_{k=u}^{v-1}|w_{k+1}-w_k|
\right).
}
\tag{21}
\]

Equivalently, after harmless endpoint normalization, the right side is bounded by `D(P)(||w||_infty+TV(w))`.

Thus if a deterministic overlap weight varies on its natural interval scale `K`, with

\[
\|w\|_\infty+TV(w)=O(M),
\qquad
\sum_k w_k\asymp MK,
\tag{22}
\]

its **relative** finite-local-product bias is

\[
\boxed{
O\!\left(\frac{(\log P)^2}{K}\right).
}
\tag{23}
\]

Piecewise-affine/triangular interval-overlap weights are of this type. What (21) does **not** cover is the raw prime-dependent welding coefficient before its deterministic main has been extracted; that distinction is load-bearing.

## 5. The potentially short `k`-ranges occupy only a boundary strip

The exact pinned `t2_swaps.py` uses

\[
\texttt{kmax}=\left\lfloor\frac{hi-lo}{r}\right\rfloor+1,
\tag{24}
\]

where `b2*m` lies in a fixed physical block `[s0 X,s1 X]`. On the continuum-dominant coprime large-base family, `r=b1` and

\[
hi-lo\asymp \frac{X}{b_2},
\]

so the natural number of available outer shifts is

\[
K\asymp\frac{X}{b_1b_2}.
\tag{25}
\]

The small-base truncations caused by the auxiliary `m<=X` condition carry negligible logarithmic Mertens mass and are not used to justify (25) globally.

Write

\[
\beta_i=\frac{\log b_i}{\log X}.
\]

WI-033 proved the quantitative weak convergence

\[
\frac1{\log X}
\sum_{p^a\le X^u}\frac{\log p}{p^a}
=u+O\!\left(\frac1{\log X}\right)
\tag{26}
\]

uniformly for `0<=u<=1`, and that the actual Yang selector/overlap geometry is bounded in this normalization.

Fix any `B>0` and put `L_X=(log X)^B`. In the nontrivial off-diagonal range, cells for which the scale (25) is at most `L_X` lie, up to fixed block constants, in

\[
1-O\!\left(\frac{\log\log X}{\log X}\right)
\le \beta_1+\beta_2
\le
1+O\!\left(\frac1{\log X}\right).
\tag{27}
\]

By (26), the normalized two-base Mertens mass of this strip is

\[
\boxed{
O\!\left(\frac{\log\log X}{\log X}\right)=o(1).
}
\tag{28}
\]

The bounded source geometry cannot amplify it to positive limiting mass. Away from (27), `K` dominates an arbitrary fixed power of `log X`; hence (23) is `o(1)` even if the local cutoff `P` is allowed to grow polylogarithmically slowly. For the actual deterministic finite cutoff `P=40`, the conclusion is stronger.

WI-045/WI-039 already showed that prime-power pairs with a common underlying prime have normalized two-base Mertens mass `O((log X)^{-2})`. Thus the coprime restriction used in Sections 2--4 also loses only `o(1)` at this continuum stage.

## 6. What is closed and what remains open

The exact conclusion is narrower than the Yang paper's sentence that the whole glue layer closes by factorization and Abel summation. What is now proved is:

\[
\boxed{
\text{finite local Euler main}
+\text{ arbitrary interval location}
+\text{ BV deterministic }k\text{-weight}
\Longrightarrow
\text{uniform }O((\log P)^2)\text{ absolute residue bias}.
}
\tag{29}
\]

Together with the Mertens boundary-strip estimate, the deterministic local residue modes therefore cannot be the positive-density obstruction in the Yang continuum normalization.

This does **not** prove the missing implication

\[
\text{actual locally centered }(S_1-2S_2+S_3)
\longrightarrow o(1)
\tag{30}
\]

for the zeta prime data. In particular, (18)--(23) do not control:

- the prime-dependent welding weight before pair-main extraction;
- covariance of the two prime-pair residuals after local centering;
- moving prime windows unless their deterministic post-extraction weights are explicitly reduced to the BV interface above;
- major/minor-arc approximation errors and their uniformity in the large reduced coefficients;
- diagonal and Poisson terms booked separately by the source;
- the low/covered-zone normalization, continuum/tail remainder, or the numerical `R(1)` ledger.

So WI-037, WI-039, WI-042, and WI-043 remain genuine warnings about the **analytic prime residual**. WI-046 only removes the finite-local deterministic weighting fork that survived WI-045.

## 7. Prior-art and novelty audit

Averaging Hardy--Littlewood singular series is classical. Gallagher's 1976 short-interval work proves the foundational average singular-series law, and later treatments such as Pintz's 2010 note give alternative proofs and extensions. Modern work on singular-series averages similarly exploits Euler/divisor expansions and residue-class counting. None of that is claimed as new here.

The identities (11)--(18) are an elementary, source-specific specialization of that general arithmetic mechanism to the two structured shifts produced by the Yang dispersion swap. The useful audit point is the **uniform-in-interval** error `D(P)` and its exact compatibility with the Yang local factors; no claim of priority is made for this inequality or for its Abel-summation corollary.

Source-backed facts are the Yang exact swap, the finite local tables, the `P=40` deterministic split, and its stated use of factorized mains plus Abel summation. Literature-backed facts are the Hardy--Littlewood local factors, CRT, Mertens' product theorem, Mertens prime-power summation, and classical singular-series averaging. The boundary-strip argument uses WI-033's already-audited source normalization rather than an unweighted count of bases.

## 8. Decisive audit and falsification tests

Reject or narrow this finding if any of the following fails:

1. recompute (4)--(7) from the two values `A_p,B_p`, including coefficient primes of arbitrary positive valuation;
2. verify (8) separately when both bases are odd and when exactly one base is even;
3. expand (11) directly for several small squarefree `Q_P` and exhaust every residue class `k mod Q_P`;
4. verify the period mean of (11) agrees with WI-045's `E_{2,Q_P}(b1,b2)`;
5. verify the cancellation `C_p(1+alpha_p)=A_p^2` in both the generic and coefficient-prime cases;
6. independently recompute the rational value (20);
7. verify from pinned `t2_swaps.py` the shift range (24), and apply (25) only in the large-base regime where the source's `m<=X` cap does not alter the block width;
8. rederive the Mertens boundary-strip estimate (28) in the exact WI-033 normalization and confirm that the source selector remains uniformly bounded there;
9. do **not** apply (21) to the raw prime-dependent welding coefficient merely because it is supported on an interval; first isolate a deterministic local main and prove the remaining prime residual is controlled;
10. do **not** promote the Yang `0.6916` candidate, or any higher-moment candidate, from this local transport result alone.

## 9. Consequence for `weil_inertia`

WI-045 reduced the welding problem from a possible local singular-series mismatch to a weighted residual. WI-046 removes the next deterministic sub-obstruction: **slow/nonuniform finite-local weighting does not require complete CRT periods and cannot create a macroscopic residue bias on the continuum-dominant cells**.

The efficient next target is therefore no longer another local-factor computation. It is to write the source's post-main-extraction `S1-2S2+S3` residual exactly and decide whether the surviving object is:

\[
\boxed{
\text{a BV-weighted linear combination of marginal pair discrepancies}
\quad\text{or}\quad
\text{a genuinely joint prime-pair residual}.
}
\]

In the first case WI-041's maximal MRT control may become sufficient after the present local transport lemma. In the second, a true bilinear/four-point or coefficient-uniform input remains necessary. That is now the load-bearing fork.