# WI-049 — the locked four-prime local main centers cellwise before marginal MRT

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + PRIOR-ART-REDIRECTION`. This finding does **not** certify the Yang--Yang one-sided fourth-moment theorem and does not change Mathia's current unconditional simple-critical proportion. It strengthens WI-045/WI-048 at the exact joint object isolated by WI-043: for every fixed admissible Yang cell `(b1,b2,j)`, the genuine four-form Hardy--Littlewood local factor of the locked square has mean exactly the **square of that cell's two-form local factor**, prime by prime and hence over every finite CRT conductor. Moreover, after taking the local cutoff beyond all source-scale collision determinants, the full Euler tail is generic and differs from the squared two-form tail by only `O(P^-1)`. Therefore the deterministic four-prime singular-series main has `o(1)` normalized bias in the actual Yang off-diagonal aggregation; it is not a source of a surviving leading locked covariance.

The finite-conductor identity is stable under arbitrary interval location. For primes through `P`, the centered four-form local product has interval discrepancy `O((log P)^4)`, **uniformly in the admissible lock and in the dominant coprime prime-power bases**. Abel summation carries the same conclusion through deterministic bounded-variation `k`-weights. The unresolved object is consequently narrower than in WI-048: any nonzero leading term in the exact locked covariance must survive **after the genuine four-prime singular-series main itself is removed**, or lie in the separately booked collision/analytic interface. That requires joint prime information, not a correction to the deterministic local Euler model.

## 1. Exact source object

The pinned source remains

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`.

For one cell, fix coprime positive bases `b1,b2` and a nonzero lock `j` with a nonvanishing local cell main. Choose one integer solution `(m0,n0)` of

\[
b_1n_0-b_2m_0=j.
\tag{1}
\]

Every solution is then

\[
m=m_0+b_1u,
\qquad
n=n_0+b_2u.
\tag{2}
\]

The exact equal-lock swap in `scripts/t2_swaps.py` pairs this point with the translated point

\[
m'=m_0+b_1(u-k),
\qquad
n'=n_0+b_2(u-k).
\tag{3}
\]

Thus the off-diagonal `S1` object is the four-form system

\[
L_1(u)=m_0+b_1u,
\quad
L_2(u)=m_0+b_1(u-k),
\quad
L_3(u)=n_0+b_2u,
\quad
L_4(u)=n_0+b_2(u-k).
\tag{4}
\]

This is the arithmetic system hidden inside the locked covariance of WI-043. The public paper's Proposition `Coincidence-counting closure` describes the local density of general affine lock chains by counting distinct normalized forbidden residues; `lean/RhGate/LocalClosure.lean` kernel-checks a finite `b=4,p=5` instance. The deduction below specializes that local law to the exact two-copy translation structure (4).

Primary source artifacts:

- `paper.tex`, Proposition `Coincidence-counting closure` and the one-sided fourth-moment welding discussion;
- `scripts/t2_swaps.py`, the exact `m'=m-rk`, `n'=n-qk` equal-lock swap and `D=S1-2S2+S3` identity;
- `pipeline/face_dispersion.py`, which models the lock-resolved four-point profile by factorized twin singular-series mains;
- `lean/RhGate/LocalClosure.lean`, an axiom-free finite instance of the source local law.

## 2. The local four-prime factor is an autocorrelation

Fix a prime `p`. Let

\[
U_p(j)
:=\{u\bmod p:\ p\nmid L_1(u)L_3(u)\}
\tag{5}
\]

be the admissible residue set for one copy of the Yang cell. Its ordinary two-form local factor is

\[
\kappa_p(j)
=
\frac{|U_p(j)|/p}{(1-1/p)^2}.
\tag{6}
\]

Because `(L_2,L_4)` is exactly `(L_1,L_3)` with `u` replaced by `u-k`, the number of residues on which all four forms are prime to `p` is

\[
C_p(k;j)
=|U_p(j)\cap(U_p(j)+k)|.
\tag{7}
\]

Hence the genuine four-form local factor is

\[
\boxed{
\sigma_{4,p}(k;j)
=
\frac{C_p(k;j)/p}{(1-1/p)^4}.
}
\tag{8}
\]

This formula is independent of any factorization ansatz. It is the actual Hardy--Littlewood local density of the four forms in (4).

## 3. Exact cellwise local centering

For every finite subset `U` of the additive group `F_p`,

\[
\sum_{k\bmod p}|U\cap(U+k)|=|U|^2
\tag{9}
\]

because both sides count ordered pairs `(u,v) in U^2`, with the unique shift `k=v-u`. Applying (9) to (7) gives

\[
\begin{aligned}
\frac1p\sum_{k\bmod p}\sigma_{4,p}(k;j)
&=
\frac{|U_p(j)|^2/p^2}{(1-1/p)^4}\\
&=\boxed{\kappa_p(j)^2}.
\end{aligned}
\tag{10}
\]

No distinction between generic primes, coefficient primes, parity, or higher base valuations is needed for (10): all of that arithmetic is encoded by `U_p(j)`. If the cell is locally obstructed, `U_p` is empty and both sides are zero.

For a squarefree conductor

\[
Q=\prod_{p\mid Q}p,
\tag{11}
\]

put

\[
\sigma_{4,Q}(k;j)=\prod_{p\mid Q}\sigma_{4,p}(k;j),
\qquad
\kappa_Q(j)=\prod_{p\mid Q}\kappa_p(j).
\tag{12}
\]

CRT independence of `k mod p` and (10) gives

\[
\boxed{
\frac1Q\sum_{k\bmod Q}\sigma_{4,Q}(k;j)
=\kappa_Q(j)^2.
}
\tag{13}
\]

This is pointwise in the cell lock `j`.

## 4. Why this is stronger than the deterministic identity in WI-045

WI-045 audited a different local object. The public dispersion model replaces the four-prime main by the product of two twin-shift mains. On the dominant coprime family this gives, prime by prime,

\[
\tau_p(b_1k)\tau_p(b_2k),
\tag{14}
\]

whose `k`-average is the source second-moment factor `E_{2,p}`. Averaging the cell square `\kappa_p(j)^2` over the lock distribution gives the same `E_{2,p}`. That identity explains the **globally aggregated** deterministic `S1/S2/S3` cancellation.

Equation (10) says more about the actual joint four-prime main:

\[
\boxed{
\text{true four-form local main at fixed }j
\xrightarrow{\;k\text{-average}\;}
\kappa_p(j)^2
}
\tag{15}
\]

before any `j`-averaging. Therefore the genuine Hardy--Littlewood main of the cell square already matches the square of the exact cell main at each fixed admissible lock. Cross-pair local collisions do not create a deterministic leading covariance that was missed by the factorized twin model.

## 5. Explicit generic local factor

Let `B=b1*b2`. For a generic prime

\[
p\ge5,
\qquad
p\nmid B j,
\tag{16}
\]

the pair-admissible set is `F_p` with two distinct residues removed. Their difference is a unit multiple of `j/B`, so

\[
C_p(k;j)
=p-4
+2\,1_{p\mid k}
+1_{Bk\equiv j\ (p)}
+1_{Bk\equiv-j\ (p)}.
\tag{17}
\]

Writing

\[
D_p=\frac{p^3(p-4)}{(p-1)^4},
\tag{18}
\]

one gets the exact positive expansion

\[
\boxed{
\sigma_{4,p}(k;j)
=D_p\left(
1+
\frac{2\,1_{p\mid k}
+1_{Bk\equiv j\ (p)}
+1_{Bk\equiv-j\ (p)}}{p-4}
\right).
}
\tag{19}
\]

At an admissible prime at which the two forbidden pair residues coincide — in particular a prime dividing `j`, or a coefficient prime dividing exactly one of the coprime bases — one has one forbidden residue and

\[
\boxed{
\sigma_{4,p}(k;j)
=H_p\left(1+\frac{1_{p\mid k}}{p-2}\right),
\qquad
H_p=\frac{p^3(p-2)}{(p-1)^4}.
}
\tag{20}
\]

The primes `2,3` form a finite periodic factor and are bounded absolutely. Equations (19)--(20) also expose the only residue modes present in the deterministic joint local main.

## 6. Uniform finite-conductor interval discrepancy

Let

\[
Q_P=\prod_{p\le P}p.
\tag{21}
\]

Expand the positive factors (19)--(20), folding `p=2,3` into a finite periodic prefactor. At a generic prime the total positive coefficient mass is exactly

\[
D_p\left(1+\frac4{p-4}\right)
=\left(\frac p{p-1}\right)^4,
\tag{22}
\]

while at a one-forbidden-residue prime it is

\[
H_p\left(1+\frac1{p-2}\right)
=\left(\frac p{p-1}\right)^3
\le
\left(\frac p{p-1}\right)^4.
\tag{23}
\]

Every choice of residue mode across distinct primes is one CRT class. The count of any residue class in any integer interval differs from its uniform density by at most one. Combining this with (13) and the positivity of the expansion yields the **source-uniform** estimate

\[
\boxed{
\left|
\sum_{k\in I}
\bigl(\sigma_{4,Q_P}(k;j)-\kappa_{Q_P}(j)^2\bigr)
\right|
\ll
\prod_{5\le p\le P}
\left(\frac p{p-1}\right)^4
\ll (\log P)^4.
}
\tag{24}
\]

The implied constant is independent of the admissible lock `j` and of the dominant coprime prime-power bases. This removes the earlier `O_j` dependence.

Discrete Abel summation therefore gives, for any deterministic real weight `w_k` on `I`,

\[
\boxed{
\left|
\sum_{k\in I}w_k
(\sigma_{4,Q_P}(k;j)-\kappa_{Q_P}(j)^2)
\right|
\ll
(\log P)^4
\left(\|w\|_\infty+\operatorname{TV}(w)\right).
}
\tag{25}
\]

No complete CRT period is required.

## 7. Full-Euler passage at the Yang source scale

The remaining issue is to compare the finite product with the genuine full singular series uniformly over the power-sized coefficient, lock, and shift family. At the source scale the dominant coprime cells have

\[
b_i\le X,
\qquad |j|\ll X,
\qquad |k|\ll X,
\qquad B=b_1b_2\le X^2.
\tag{26}
\]

Hence every nonzero collision determinant among

\[
B,\qquad j,\qquad k,\qquad Bk-j,\qquad Bk+j
\tag{27}
\]

has size `O(X^3)`. Take `P=X^4`. For every prime `p>P`, and away from the exact collision shifts `Bk=\pm j`, the four residues are distinct and generic. Therefore

\[
\sigma_4(k;j)=D_{>P}\,\sigma_{4,Q_P}(k;j),
\qquad
\kappa(j)^2=K_{>P}\,\kappa_{Q_P}(j)^2,
\tag{28}
\]

where

\[
D_{>P}=\prod_{p>P}\frac{p^3(p-4)}{(p-1)^4},
\qquad
K_{>P}=\prod_{p>P}\frac{p^2(p-2)^2}{(p-1)^4}.
\tag{29}
\]

Both products converge absolutely. Prime by prime,

\[
K_p-D_p
=\frac{4p^2}{(p-1)^4}>0,
\tag{30}
\]

and `0<D_p,K_p<=1`. Product telescoping therefore gives

\[
0\le K_{>P}-D_{>P}
\le
\sum_{p>P}\frac{4p^2}{(p-1)^4}
\ll P^{-1}.
\tag{31}
\]

Thus

\[
\boxed{
\sigma_4(k;j)-\kappa(j)^2
=D_{>P}(\sigma_{4,Q_P}(k;j)-\kappa_{Q_P}(j)^2)
+(D_{>P}-K_{>P})\kappa_{Q_P}(j)^2.
}
\tag{32}
\]

A crude Mertens bound gives `\kappa_{Q_P}(j)^2\ll(\log P)^4` uniformly. For an interval of `K` noncollision shifts, (24) and (31)--(32) therefore imply

\[
\boxed{
\left|
\sum_{k\in I}(\sigma_4(k;j)-\kappa(j)^2)
\right|
\ll
(\log P)^4+
\frac{K(\log P)^4}{P}.
}
\tag{33}
\]

With deterministic weights,

\[
\boxed{
\left|
\sum_{k\in I}w_k(\sigma_4(k;j)-\kappa(j)^2)
\right|
\ll
(\log P)^4(\|w\|_\infty+\operatorname{TV}(w))
+
\frac{(\log P)^4}{P}\sum_{k\in I}|w_k|.
}
\tag{34}
\]

Now set `P=X^4`. The overlap weights already isolated in WI-046/WI-048 satisfy `\|w\|_\infty+TV(w)=O(M)` and total mass `\asymp MK`. On cells with `K>(\log X)^A` for any fixed `A>4`, the right side of (34), divided by `MK`, is `o(1)`. WI-046/WI-048 separately show that the complementary polylog-short `k` cells and the noncoprime same-underlying-prime base family carry only `o(1)` normalized Mertens mass. Because (24)--(34) are uniform in `j`, summing over the full lock range causes no new loss.

Therefore the genuine full four-form Hardy--Littlewood local main has **`o(1)` normalized deterministic bias in the actual Yang off-diagonal source aggregation**.

## 8. Diagonal boundary

The source books exact diagonal pieces separately. The four affine forms cease to be distinct at `k=0`, and the cross-collisions occur whenever

\[
\boxed{Bk=\pm j}
\tag{35}
\]

is integral — not only in the unit-base case. At those shifts the ordinary four-distinct-form Euler product is not the correct object. There are at most two such cross-collision shifts per cell. On long `k`-intervals their deterministic shift density is zero, while the polylog-short cells are already part of the `o(1)` boundary mass above.

These collision/diagonal terms remain separately booked. The result here is specifically the **off-diagonal deterministic local-main** statement; it does not absorb the prime-dependent residual or the unresolved analytic/diagonal interface into the singular series.

## 9. Prior-art audit

The source's Proposition `Coincidence-counting closure` is the closest prior art. It proves the general local count for an affine lock chain from the number of distinct normalized forbidden residues, and the public verification artifacts exhaustively test finite instances. Equation (10) is an elementary autocorrelation corollary specialized to the exact repeated-cell translation in the one-sided `S1` square. No priority claim is made for the identity.

More broadly, averaging Hardy--Littlewood singular series is classical: Gallagher's 1976 short-interval argument established the foundational mean law, with later simplified/strengthened proofs by Pintz and Ford. Vivian Kuperberg's **Sums of singular series along arithmetic progressions and with smooth weights**, *International Journal of Number Theory* 21 (2025), 53--74, DOI `10.1142/S1793042125500046`, is especially relevant because it studies constrained arithmetic-progression and smooth-weight singular-series averages. Those results support the general arithmetic picture but are not needed for the source-uniform tail completion (28)--(34), which follows directly from the explicit local factors and the source-scale determinant bound.

The Mathia contribution recorded here is not a new singular-series principle. It is the exact identification of the WI-043 locked four-prime local object as an autocorrelation, the fixed-cell centering (10)--(13), the uniform finite-conductor interval/BV estimate (24)--(25), and the source-scale full-Euler completion (28)--(34). Together they show that a surviving Yang locked covariance must be genuinely post-local-main rather than an omitted deterministic four-form Euler contribution.

## 10. Verification / falsification boundary and consequence

Narrow or retire this finding if any of the following fails under the exact source normalization:

1. the off-diagonal `S1` four-form system after restoring `g=(b1,b2)` is not a common translation of the same two-form cell in the shift parameter used by the consumer;
2. the source local factor `kappa_p(j)` differs from the two-form admissible density (6) by a normalization not already carried outside the local product;
3. a coefficient-prime or prime-power valuation introduces additional `k`-dependent local modes not represented by the admissible-set autocorrelation (7);
4. the deterministic source `k`-weight before the analytic residual is isolated is not reducible to the BV interface used in (25)/(34);
5. the source-scale bounds (26)--(27), or the WI-046/WI-048 negligible-short-cell/noncoprime-mass inputs, fail under the exact consumer decomposition.

The durable separation is

\[
\boxed{
\text{full four-prime deterministic local main}
\longrightarrow
\text{cellwise centered with }o(1)\text{ normalized source bias}
}
\tag{36}
\]

but

\[
\boxed{
\text{actual prime residual covariance}
\quad\text{remains uncontrolled}.}
\tag{37}
\]

Accordingly, the finite nonzero covariance recorded by `CLUE-yang-locked-covariance-leading-scale` cannot be promoted by appealing to a missing Hardy--Littlewood four-form main or to an Euler-tail bias. A persistent normalized limit would have to come from a genuine joint four-prime residual or from the separately booked analytic/diagonal interface. The shortest decisive test is therefore to subtract the genuine four-form local model in the exact source computation and remeasure the normalized post-local-main residual across scales.