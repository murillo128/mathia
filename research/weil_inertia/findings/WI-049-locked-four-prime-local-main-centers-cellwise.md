# WI-049 — the locked four-prime local main centers cellwise before marginal MRT

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + PRIOR-ART-REDIRECTION + NEEDS-AUDIT`. This finding does **not** certify the Yang--Yang one-sided fourth-moment theorem and does not change Mathia's current unconditional simple-critical proportion. It strengthens WI-045/WI-048 at the exact joint object isolated by WI-043: for every fixed admissible Yang cell `(b1,b2,j)`, the genuine four-form Hardy--Littlewood local factor of the locked square has mean exactly the **square of that cell's two-form local factor**, prime by prime and hence over every finite CRT conductor. Thus the deterministic four-prime singular-series main cancels cellwise against the `S2/S3` centering; it is not a source of a surviving leading locked covariance.

The finite-conductor identity is stable under arbitrary interval location. For primes through `P`, the centered four-form local product has interval discrepancy `O_j((log P)^4)`, uniformly in the dominant coprime prime-power bases. Abel summation therefore carries the same conclusion through deterministic bounded-variation `k`-weights. The unresolved object is consequently narrower than in WI-048: any nonzero leading term in the exact locked covariance must survive **after the genuine four-prime singular-series main itself is removed**. That requires joint prime information, not a correction to the deterministic local Euler model.

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

For every finite subset `U` of the additive group `F_p`, the elementary autocorrelation identity

\[
\sum_{k\bmod p}|U\cap(U+k)|=|U|^2
\tag{9}
\]

holds: both sides count ordered pairs `(u,v) in U^2`, with the unique shift `k=v-u`.

Applying (9) to (7) gives

\[
\begin{aligned}
\frac1p\sum_{k\bmod p}\sigma_{4,p}(k;j)
&=
\frac{|U_p(j)|^2/p^2}{(1-1/p)^4}\\
&=\boxed{\kappa_p(j)^2}.
\end{aligned}
\tag{10}
\]

No distinction between generic primes, coefficient primes, parity, or higher base valuations is needed for (10): all of that arithmetic is already encoded by the set `U_p(j)`. If the cell is locally obstructed, `U_p` is empty and both sides are zero.

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

CRT independence of the residue `k mod p` and (10) give the exact finite-conductor identity

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

before any `j`-averaging. Therefore the genuine Hardy--Littlewood main of `A(b2,j)^2` already matches the square of the exact cell main at each fixed admissible lock. Cross-pair local collisions do not create a deterministic leading covariance that was missed by the factorized twin model.

This is precisely the interface relevant to `CLUE-yang-locked-covariance-leading-scale`: the finite source covariance can be nonzero as an algebraic prime-data expression, but its asymptotic leading term cannot be justified merely by pointing to a missing four-point singular-series main.

## 5. Explicit generic local factor

The autocorrelation form also gives a useful interval-discrepancy expansion.

Let `B=b1*b2`. For a generic prime

\[
p\ge5,
\qquad
p\nmid B j,
\tag{16}
\]

the pair-admissible set is `F_p` with two distinct residues removed. Their difference is a unit multiple of `j/B`. Consequently

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

we obtain the exact positive expansion

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

At an admissible prime at which the two forbidden pair residues coincide -- in particular a prime dividing `j`, or a coefficient prime dividing exactly one of the coprime bases -- one has one forbidden residue and

\[
\boxed{
\sigma_{4,p}(k;j)
=H_p\left(1+\frac{1_{p\mid k}}{p-2}\right),
\qquad
H_p=\frac{p^3(p-2)}{(p-1)^4}.
}
\tag{20}
\]

The primes `2,3` form a finite periodic factor and can be handled exactly. Equations (19)--(20) re-prove (10) by elementary averaging and expose the only residue modes present in the deterministic joint local main.

## 6. Uniform interval discrepancy at finite conductor

Let

\[
Q_P=\prod_{p\le P}p
\tag{21}
\]

and keep an admissible fixed nonzero `j`. Expand the positive factors (19)--(20), folding `p=2,3` into a finite periodic prefactor. At every prime `p>=5` one selects at most one residue condition. The total nonconstant coefficient at a generic prime is

\[
\beta_p=\frac4{p-4},
\tag{22}
\]

while at a one-forbidden-residue prime it is

\[
\beta_p=\frac1{p-2}<\frac4{p-4}.
\tag{23}
\]

A choice of residue mode at distinct primes is a single CRT class modulo the product of those primes. For any integer interval `I`, the count of one residue class modulo any modulus differs from its uniform density by at most one. Therefore the complete finite expansion and (13) give

\[
\left|
\sum_{k\in I}
\bigl(\sigma_{4,Q_P}(k;j)-\kappa_{Q_P}(j)^2\bigr)
\right|
\ll_j
\prod_{5\le p\le P}\left(1+\frac4{p-4}\right).
\tag{24}
\]

The implied constant is uniform in the coprime prime-power bases. Indeed the generic baseline product converges because `D_p=1+O(p^-2)`, replacing a generic prime by (20) multiplies that baseline by

\[
\frac{H_p}{D_p}=\frac{p-2}{p-4},
\tag{25}
\]

and at most two such replacements come from the bases; the further replacements from primes dividing fixed `j` contribute only a `j`-dependent constant.

Finally,

\[
1+\frac4{p-4}=\frac p{p-4}.
\tag{26}
\]

Comparison with `(p/(p-1))^4` leaves an absolutely convergent Euler-product ratio, so Mertens' product theorem yields

\[
\boxed{
\left|
\sum_{k\in I}
(\sigma_{4,Q_P}(k;j)-\kappa_{Q_P}(j)^2)
\right|
\ll_j (\log P)^4.
}
\tag{27}
\]

No complete CRT period is required.

As in WI-046, discrete Abel summation then gives, for any deterministic real weight `w_k` on `I`,

\[
\boxed{
\left|
\sum_{k\in I}w_k
(\sigma_{4,Q_P}(k;j)-\kappa_{Q_P}(j)^2)
\right|
\ll_j
(\log P)^4
\left(\|w\|_\infty+\operatorname{TV}(w)\right).
}
\tag{28}
\]

Thus at every fixed finite local conductor the true four-point singular-series main has negligible relative bias on a long Yang `k`-interval with its deterministic bounded-variation geometry.

## 7. Diagonal and full-Euler boundaries

The source books exact diagonal pieces separately. This matters because the four affine forms cease to be distinct at the global diagonal `k=0`, and in the special unit-base case `b1=b2=1` also at the cross-diagonals `k=+/-j`. The ordinary four-distinct-form Euler product is not the correct object on those finitely many shifts. Equations (10) and (13) are local finite-product identities and remain valid; the interval statement (27) is to be read for the source's off-diagonal bookkeeping, with the finitely many exact diagonals removed separately.

This finding deliberately does **not** claim the full infinite-product analogue of (27) uniformly in the power-sized Yang coefficients. WI-048 proved such a completion for the easier factorized pair-pair local product using a one-divisor positive expansion. The genuine four-form expansion has three residue modes per generic prime and cross-diagonal tails; a full-Euler, power-uniform passage requires its own audit. Classical singular-series averaging results strongly suggest the relevant mechanism but are not imported here as a source-uniform theorem.

## 8. Prior-art audit

The source's own Proposition `Coincidence-counting closure` is the closest prior art. It proves the general local count for an affine lock chain from the number of distinct normalized forbidden residues, and the public verification artifacts exhaustively test finite instances. Equation (10) is an elementary autocorrelation corollary specialized to the exact repeated-cell translation in the one-sided `S1` square. No priority claim is made for the identity.

More broadly, averaging Hardy--Littlewood singular series is classical: Gallagher's 1976 short-interval argument established the foundational mean law, with later simplified/strengthened proofs by Pintz and Ford. Vivian Kuperberg's **Sums of singular series along arithmetic progressions and with smooth weights**, *International Journal of Number Theory* 21 (2025), 53--74, DOI `10.1142/S1793042125500046`, is especially relevant because it studies constrained arithmetic-progression and smooth-weight singular-series averages. Those results support the general arithmetic picture behind (24)--(28), but this finding does not assume that their parameter-uniformity covers the power-sized Yang coefficient family.

The Mathia contribution recorded here is therefore not a new singular-series principle. It is the exact identification of the WI-043 locked four-prime local object as an autocorrelation, the resulting **fixed-cell** centering (10)--(13), and the finite-conductor interval/BV consequence (27)--(28), together with the research consequence that a surviving Yang locked covariance must be genuinely analytic rather than a missing deterministic local main.

## 9. Decisive verification / falsification gate

Narrow or retire this finding if any of the following fails under the exact source normalization.

1. The off-diagonal `S1` four-form system after restoring `g=(b1,b2)` is not a common translation of the same two-form cell in the shift parameter used by the consumer.
2. The source local factor `kappa_p(j)` differs from the two-form admissible density (6) by a normalization not already carried outside the local product.
3. A coefficient-prime or prime-power valuation introduces additional `k`-dependent local modes not represented by the admissible-set autocorrelation (7).
4. The deterministic source `k`-weight before the analytic residual is isolated is not reducible to the BV interface used in (28).

The first three are exact algebraic/local checks and should be suitable for an adversarial review. The fourth affects only the weighted interval corollary, not the prime-by-prime identity (10) or finite-CRT identity (13).

## 10. Consequence for the locked-covariance clue

The durable separation is now

\[
\boxed{
\text{true four-prime local main}
\longrightarrow
\text{cellwise centered exactly}
}
\tag{29}
\]

but

\[
\boxed{
\text{actual prime residual covariance}
\quad\text{remains uncontrolled}.}
\tag{30}
\]

Accordingly, the finite nonzero covariance recorded by `CLUE-yang-locked-covariance-leading-scale` is more informative than a local-factor mismatch, but less close to an asymptotic theorem than its raw size might suggest. A persistent normalized limit would have to come from a genuine joint four-prime residual (or from a still-unresolved analytic weighting/diagonal interface), not from the Hardy--Littlewood singular series of the four forms. The shortest next test is therefore to subtract the genuine four-form local model, not merely the product of the two marginal twin models, in the exact source computation and remeasure the normalized residual across scales.
