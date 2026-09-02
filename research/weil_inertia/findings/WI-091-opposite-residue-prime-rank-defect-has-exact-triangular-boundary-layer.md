# WI-091 — Opposite-residue prime Ramanujan rank defect has an exact triangular boundary layer

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion and does not certify or repair the Yang--Yang one-sided fourth-moment candidate. It sharpens WI-087--WI-090 from the exact one-third-defect center to a whole near-extremal boundary layer. For every close opposite-residue prime pair, translating the sharp nearest-LCM boundary by `e` changes the cross-Gram rank by exactly `|e|` until full row rank is reached. Combined with the WI-088/WI-090 cycle bounds, this also implies that near-one-third pairwise defects at a fixed observation length have uniformly bounded local incidence: an additive defect loss `D` gives degree at most `8D+4` before the one-quarter alternative becomes available.

Let `p<q<2p` be distinct odd primes in opposite nonzero residue classes modulo `3`. Put

\[
r:=\frac{2p-q}{3},
\qquad
\beta:=\frac{p+q}{3}=p-r.
\tag{1}
\]

Then `r` and `beta` are positive integers. Define the canonical boundary

\[
\delta_c=
\begin{cases}
\displaystyle\delta_-:=\frac{pq+p-q}{3},
& p\equiv2,\ q\equiv1\pmod3,\\[3mm]
\displaystyle\delta_+:=\frac{pq+q-p}{3},
& p\equiv1,\ q\equiv2\pmod3.
\end{cases}
\tag{2}
\]

For every integer `e` satisfying

\[
\boxed{|e|\le r-1,}
\tag{3}
\]

the nearest-boundary Ramanujan cross Gram of WI-081/WI-086 has the exact rank

\[
\boxed{
\operatorname{rank}G_{p,q}^{(\delta_c+e)}
=\beta+|e|
=\frac{p+q}{3}+|e|.
}
\tag{4}
\]

The whole layer remains in WI-086's genuinely residual regime, so its excess-transversality defect is

\[
\boxed{
\tau_{p,q}(\delta_c+e)
=(p-1)-\operatorname{rank}G_{p,q}^{(\delta_c+e)}
=r-1-|e|.
}
\tag{5}
\]

Thus the sharp one-third obstruction of WI-087/WI-090 is the apex of an exact triangular profile. Moving one integer step away from the canonical boundary removes exactly one defect dimension, and at `|e|=r-1` the smaller prime block is already full row rank.

## 1. Shift the WI-087/WI-089 rational interpolant instead of rebuilding it

WI-087 constructs, for the orientation

\[
p\equiv2,\qquad q\equiv1\pmod3,
\tag{6}
\]

the parameters

\[
\alpha=r,
\qquad
\beta=p-r,
\qquad
\gamma=p-2r,
\tag{7}
\]

and the coprime polynomials

\[
P(X)=1+X^\alpha+X^\beta,
\qquad
Q(X)=1+X^\gamma+X^\beta.
\tag{8}
\]

They obey

\[
P-X^\alpha Q=1-X^p,
\qquad
P-X^\beta Q=(1+X^\alpha)(1-X^q),
\tag{9}
\]

are regular on both primitive prime-root node sets, and the reduced rational function

\[
R_-(X)=\frac{P(X)}{Q(X)}
\tag{10}
\]

agrees with `X^delta_-` on both node sets. WI-089 proves the mirror orientation

\[
p\equiv1,\qquad q\equiv2\pmod3
\tag{11}
\]

by taking

\[
R_+(X)=\frac{Q(X)}{P(X)},
\tag{12}
\]

which agrees with `X^delta_+` on the same respective primitive `p`- and `q`-root sets. Both numerator and denominator have degree `beta`, constant term `1`, are coprime, and have no zero at any interpolation node.

Fix the appropriate base representation

\[
R_c(X)=\frac{A(X)}{B(X)}
\tag{13}
\]

from (10) or (12). For an integer `e`, define

\[
(A_e,B_e)=
\begin{cases}
(X^eA,B),&e\ge0,\\
(A,X^{-e}B),&e<0.
\end{cases}
\tag{14}
\]

Then

\[
\frac{A_e(X)}{B_e(X)}=X^eR_c(X).
\tag{15}
\]

Every interpolation node is nonzero, so (15) agrees with

\[
X^{\delta_c+e}
\tag{16}
\]

on both primitive node sets. The representation remains reduced: `A(0)=B(0)=1`, so the added monomial factor is coprime to the opposite polynomial, while `gcd(A,B)=1` is already proved in WI-087/WI-089. Its exact rational degree in the Bezoutian sense is therefore

\[
\boxed{
D_e:=\max\{\deg A_e,\deg B_e\}
=\beta+|e|.
}
\tag{17}
\]

This is the only new interpolation step needed for the whole boundary layer.

## 2. The rectangular Bezout--Vandermonde factorization gives rank `D_e`

For primitive roots `z^p=1` and `w^q=1`, WI-087 rewrites the finite-window cross-Gram entry as

\[
G_{z,w}^{(\delta)}
=\sum_{x=0}^{\delta-1}(z^{-1}w)^x
=z^{1-\delta}\frac{z^\delta-w^\delta}{z-w}.
\tag{18}
\]

The nonzero row phase does not affect rank. By (15)--(16), at

\[
\delta=\delta_c+e
\tag{19}
\]

the remaining divided-difference matrix is exactly the rational Loewner matrix of `A_e/B_e` on the two primitive-root node sets.

Take the Bezoutian of `A_e,B_e` in order `D_e`,

\[
\mathcal B_e(X,Y)
=
\frac{A_e(X)B_e(Y)-B_e(X)A_e(Y)}{X-Y}.
\tag{20}
\]

Because the two polynomials are coprime, the classical Bezout/resultant theorem makes its `D_e x D_e` coefficient matrix `B_e^{\rm Bez}` nonsingular. The rational Loewner matrix factors as

\[
L_e
=
D_Z^{-1}
V_Z^{(D_e)}
B_e^{\rm Bez}
\bigl(V_W^{(D_e)}\bigr)^T
D_W^{-1},
\tag{21}
\]

with invertible diagonal denominator-value matrices and the usual evaluation Vandermonde matrices on the primitive `p`- and `q`-root node sets.

Condition (3) is exactly what keeps both Vandermonde sides tall enough. Indeed,

\[
D_e
\le \beta+r-1
=p-1
<q-1.
\tag{22}
\]

The `p`-side and `q`-side Vandermonde matrices therefore both have full column rank `D_e`. Since the middle Bezoutian is invertible, (21) has rank exactly `D_e`. Combining with the harmless row phase in (18) proves (4).

No generic-position hypothesis enters here. The argument is exact over the cyclotomic node sets and reduces the shifted theorem to the same classical Bezoutian mechanism already audited in WI-087.

## 3. The entire triangular layer stays genuinely residual

The defect `tau` from WI-086 is defined once the boundary has passed both primitive-frequency dimensions. Since `q-1` is the larger dimension, it is enough to check

\[
\delta_c+e>q-1.
\tag{23}
\]

The worst case is `e=-(r-1)`. For the `delta_-` orientation,

\[
\delta_--(r-1)-(q-1)
=
\frac{pq-p-3q+6}{3}>0,
\tag{24}
\]

and for the `delta_+` orientation,

\[
\delta_+-(r-1)-(q-1)
=
\frac{pq-q-3p+6}{3}>0.
\tag{25}
\]

Both are positive for the admissible close odd-prime pairs, including the smallest cases. The upper edge also remains below `pq/2`, so these are legitimate nearest-LCM boundary lengths rather than an artifact of extending the finite-window formula beyond its boundary convention.

WI-086 therefore gives

\[
\tau=(p-1)-\operatorname{rank}G.
\tag{26}
\]

Using (4),

\[
\tau
=p-1-(p-r+|e|)
=r-1-|e|,
\]

which proves (5).

Exact regression examples are

\[
(p,q)=(11,13),\qquad
\operatorname{rank}G^{(47+e)}=8+|e|
\quad(-2\le e\le2),
\tag{27}
\]

and

\[
(p,q)=(17,19),\qquad
\operatorname{rank}G^{(107+e)}=12+|e|
\quad(-4\le e\le4).
\tag{28}
\]

Direct complex-SVD checks on more than one hundred small opposite-residue prime-pair/shift instances reproduced (4); those computations are falsification only and are not used as evidence for the theorem.

## 4. The WI-088 graph sees exactly the same boundary layer

The rational-interpolation proof has an exact combinatorial shadow in the partial-permutation graph of WI-088. Write

\[
d=q-p,
\qquad
t=2p-q=3r,
\tag{29}
\]

and, at the only quotient where WI-089 permits a free three-cycle,

\[
k=\left\lfloor\frac p3\right\rfloor,
\qquad
\delta=kq+s.
\tag{30}
\]

WI-088 uses the intervals

\[
A=\{0,\ldots,s-d-1\},
\qquad
C=\{s-d,\ldots,s-1\},
\qquad
B=\{s,\ldots,p-1\}
\tag{31}
\]

and the partial map

\[
g(x)=
\begin{cases}
x+(k+1)d,&x\in A,\\
x+kd,&x\in B,
\end{cases}
\pmod p.
\tag{32}
\]

At `delta=delta_c+e`, adding `e` only changes the remainder `s`; it does not change `k` throughout the relevant exceptional strip.

If

\[
p\equiv2,\qquad q\equiv1\pmod3,
\tag{33}
\]
then

\[
|A|=2r+e,
\qquad
B=\{p-r+e,\ldots,p-1\},
\tag{34}
\]

and the two translations reduce modulo `p` to

\[
x\mapsto x-r\quad(x\in A),
\qquad
x\mapsto x+2r\quad(x\in B).
\tag{35}
\]

Every free three-cycle is therefore uniquely of the form

\[
\boxed{
\{x,\ r+x,\ p-r+x\},
}
\tag{36}
\]

where

\[
\max\{0,e\}
\le x
<\min\{r,r+e\}.
\tag{37}
\]

Conversely every `x` in (37) gives such a cycle. Hence

\[
c_3=\max\{0,r-|e|\}.
\tag{38}
\]

For the mirror orientation

\[
p\equiv1,\qquad q\equiv2\pmod3,
\tag{39}
\]
one has

\[
|A|=r+e,
\qquad
B=\{p-2r+e,\ldots,p-1\},
\tag{40}
\]

with reduced translations

\[
x\mapsto x-2r\quad(x\in A),
\qquad
x\mapsto x+r\quad(x\in B).
\tag{41}
\]

The free three-cycles are exactly

\[
\boxed{
\{x,\ p-2r+x,\ p-r+x\},
}
\tag{42}
\]

with the same range (37), again giving (38).

This identifies the three-term polynomials of WI-087/WI-089 with the support pattern of the free three-cycles in the exact row-kernel graph. More importantly, (38) shows that **no** free three-cycle exists once `|e|>=r`. WI-088 already excludes cycles of length one or two. Therefore every residual close-prime boundary outside this triangular opposite-residue layer, as well as every same-residue case from WI-090 and every quotient `k!=floor(p/3)` from WI-089, falls to the one-quarter cycle-counting alternative

\[
\boxed{
\tau_{p,q}(\delta)
\le
\max\left\{0,
\left\lfloor\frac{2p-q}{4}\right\rfloor-1
\right\}.
}
\tag{43}
\]

Equation (43) is not a claim that the rank is exactly full outside the triangular layer. It is the safe universal bound furnished by the persisted partial-permutation argument once three-cycles are absent.

## 5. Near-sharp defects have bounded incidence at fixed observation length

The exact profile also upgrades WI-090's fixed-`N` matching statement from exact equality to quantitative near-equality.

For a residual close-prime pair put

\[
C_3(t):=\left\lfloor\frac t3\right\rfloor-1,
\qquad
C_4(t):=\max\left\{0,\left\lfloor\frac t4\right\rfloor-1\right\},
\qquad
t=2p-q.
\tag{44}
\]

Assume `C_3(t)>0`. Suppose its actual pairwise defect satisfies

\[
\tau_{p,q}(\delta_N)
\ge C_3(t)-D
\tag{45}
\]

for an integer `D>=0`, and suppose

\[
\boxed{
D<\left\lfloor\frac t3\right\rfloor
 -\left\lfloor\frac t4\right\rfloor.
}
\tag{46}
\]

Under `C_3(t)>0`, condition (46) is exactly `C_3(t)-D>C_4(t)`, so (43) excludes every one-quarter alternative. Thus the pair must lie in opposite nonzero residue classes, use `k=floor(p/3)`, have `t=3r`, and lie inside the exact triangular layer. Equations (5) and (45) force

\[
\boxed{|e|\le D.}
\tag{47}
\]

WI-089's sharp-boundary congruence can now be translated by `e`. For either endpoint `ell`, with the other prime denoted `m`, define

\[
\varepsilon(\ell)=
\begin{cases}
+1,&\ell\equiv1\pmod3,\\
-1,&\ell\equiv2\pmod3.
\end{cases}
\tag{48}
\]

Because `delta_N` is the distance to the nearest multiple of `pq`, there is a sign `eta in {+1,-1}` such that

\[
\boxed{
3N
\equiv
\eta\bigl(\varepsilon(\ell)m+3e\bigr)
\pmod\ell.
}
\tag{49}
\]

For fixed `ell`, fixed sign `eta`, fixed `e`, and a fixed orientation of the partner (`m>ell` or `m<ell`), equation (49) determines at most one candidate partner in the close-prime interval: respectively `ell<m<2ell` or `ell/2<m<ell`. There are two signs, two orientations, and at most `2D+1` possible shifts. Hence the graph of pairs satisfying (45)--(46) at a fixed observation length obeys

\[
\boxed{
\deg_N(\ell)\le4(2D+1)=8D+4.
}
\tag{50}
\]

For `D=0`, WI-090's stronger exact argument gives the sharp degree bound `1`; (50) is intentionally a coarse stability bound. Its value is that the local one-third obstruction cannot be treated as independently repeatable around one modulus even after allowing a fixed additive loss from the ceiling.

## 6. Stress tests and failure boundaries

The load-bearing points are finite and explicit.

1. **Negative shifts.** For `e<0`, the monomial belongs in the denominator in (14). The constant terms `A(0)=B(0)=1` are essential: they ensure that adding the power of `X` introduces no common factor and no pole on the nonzero root-of-unity node sets.
2. **Rectangular rather than square interpolation.** The proof uses only `D_e<=p-1<q-1`; it does not assume equal node counts. Full column rank of both evaluation Vandermonde matrices plus nonsingularity of the Bezoutian is enough.
3. **Do not extrapolate (4) past (3).** When `|e|>=r`, the shifted rational degree is at least `p`, so the simple tall-Vandermonde rank argument no longer proves an exact rank. Equation (43), not full rank, is the justified universal conclusion there.
4. **Prime hypotheses matter.** The row-kernel cycle classification and primitive-node dimensions use prime moduli. Composite Ramanujan spaces can have noninvertible steps and different cyclotomic dimensions.
5. **Pairwise structure is not yet the Yang covariance theorem.** The result constrains one finite-window prime-pair Ramanujan interface. It does not show that the full signed multi-modulus operator is the sum of independent pair defects, and it does not supply the missing four-prime covariance estimate.
6. **Nearest-boundary sign is retained.** Equation (49) includes both sides of the nearest `pq` multiple through `eta`; dropping that sign would give a false fixed-`N` uniqueness statement.

A direct numerical rank sweep over small opposite-residue prime pairs and every shift in (3) found no counterexample to (4). A separate exact integer enumeration of the WI-088 partial map reproduces (38). These checks are not substitutes for the exact Loewner/Bezout and interval-map arguments above.

## 7. Prior art and novelty boundary

The algebraic machinery is classical or already persisted.

- WI-081 supplies the nearest-LCM finite-window factorization into primitive-root Vandermonde blocks.
- WI-086 identifies residual rank loss with the excess-transversality defect `tau` after both Ramanujan dimensions have saturated.
- WI-087 supplies the reduced three-term `P/Q` interpolant, its node regularity and coprimality, and the exact Bezoutian/Vandermonde rank proof at `delta_-`.
- WI-089 supplies the inverse `Q/P` mirror at `delta_+`, the unique three-cycle quotient, and the fixed-`N` canonical matching congruence.
- WI-090 proves that same-residue pairs have no free three-cycle and that every exact positive one-third-ceiling pair is one of those two opposite-residue centers.
- S. Barnett, **A Note on the Bezoutian Matrix**, *SIAM Journal on Applied Mathematics* 22 (1972), 84--86, DOI `10.1137/0122009`, is classical Bezoutian/GCD background. Nonsingularity of an order-`D` Bezout matrix for coprime polynomials is the standard resultant criterion used in (20)--(21).
- Ricardo Pachón, Pedro Gonnet and Joris van Deun, **Fast and Stable Rational Interpolation in Roots of Unity and Chebyshev Points**, *SIAM Journal on Numerical Analysis* 50 (2012), 1713--1734, DOI `10.1137/100797291`, is direct roots-of-unity rational-interpolation prior art. It supports the ambient interpolation setting, not the close-prime boundary arithmetic derived here.
- Tao's prime cyclic Fourier uncertainty theorem and Loukaki's 2025 `pq` extension are nearby Fourier-minor/transversality prior art, but their objects are support/minor nonsingularity statements rather than this nearest-LCM shifted Ramanujan cross-Gram profile.

A targeted search across Loewner rational interpolation, Bezoutians/resultants, roots-of-unity interpolation, partial Fourier uncertainty, and Ramanujan-subspace rank did not locate the exact formulas (4)--(5), the cycle count (38), or the fixed-`N` stability bound (50). This is **not** a priority claim: the durable claim is the exact consequence reconstructed above from the persisted WI-087--WI-090 structure plus classical interpolation algebra.

## 8. Consequence for the research program

The one-third pairwise obstruction is more rigid than WI-088 alone suggested. Its strongest form is not spread over a broad residual boundary region. For an opposite-residue prime pair it has an exact integer slope away from one canonical boundary,

\[
\tau=r-1-|e|,
\qquad |e|\le r-1,
\tag{51}
\]

while every route to a defect larger than the one-quarter cycle scale is forced into this same layer. At fixed `N`, allowing `D` dimensions of slack from the one-third ceiling permits only `O(D)` candidate neighbors per modulus.

This does not close the global signed Ramanujan-operator problem of WI-079--WI-085, because many moderately defective pair blocks may still interact and pairwise rank is not itself an operator-norm or four-prime covariance estimate. It does remove one pessimistic assembly model: a global argument may not freely attach arbitrarily many near-maximal one-third pairwise losses to the same prime modulus. Any source-faithful worst-case construction must respect the arithmetic boundary congruence (49) and the bounded-incidence geometry (50).
