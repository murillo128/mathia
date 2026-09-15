# VIS-243 — complement symmetry closes the cyclic overlap multiplicities

## Claim

Continue the endpoint-phase-quotiented tent statistic and symmetric-Dirichlet gap calibration of `VIS-241`--`VIS-242`. Normalize the circumference to `1`, write

`S_(i,r)=sum_(a=0)^(r-1) X_(i+a)`

for the mass of the forward cyclic arc of `r` gaps, and keep the complement-symmetric kernel

`q_u(s)=q_u(1-s)`

from `VIS-242`.

Define

`R_m={1,...,floor(m/2)}`

and weights

`w_r=1`

except when `m` is even and `r=m/2`, where `w_r=1/2`.

Then the oriented-arc representation of the cut-averaged statistic has the exact half-circle quotient

`bar T = sum_(r in R_m) w_r sum_(i=0)^(m-1) q_u(S_(i,r))`.

For `r,s in R_m`, let

`A_r={0,...,r-1} subset Z/mZ`,
`B_(s,d)={d,...,d+s-1} subset Z/mZ`,
`k_(r,s)(d)=|A_r intersect B_(s,d)|`.

Put

`a=min(r,s)`, `b=max(r,s)`.

Because `r+s<=m` on the half-circle domain, the overlap multiplicities are exactly

`N_(r,s,0)=m-r-s+1`,

`N_(r,s,a)=b-a+1`,

`N_(r,s,k)=2` for `1<=k<a`,

and zero otherwise.

Consequently, if

`C_(r,s,k)=M_(r,s,k)-mu_r mu_s`

uses the low-dimensional Dirichlet expectations of `VIS-242`, then

`Var_G(bar T)`
` = m sum_(r,s in R_m) w_r w_s [`
`     (m-r-s+1) C_(r,s,0)`
`     + (b-a+1) C_(r,s,a)`
`     + 2 sum_(k=1)^(a-1) C_(r,s,k)`
`   ]`.

Thus the remaining displacement sum in `VIS-242` is completely explicit. Complementary arc lengths never need to be evaluated separately, unavoidable-overlap cases disappear from the canonical domain, and every interior overlap size has multiplicity exactly two.

**Evidence/status:** `EXACT-DERIVED + ELEMENTARY CYCLIC CROSS-CORRELATION + REPRESENTATION-QUOTIENT + NO-NOVELTY-CLAIM`.

No prime residual, fitted Dirichlet parameter, asymptotic law, or RH consequence is asserted.

## 1. Complement symmetry reduces all arc lengths to at most a half-circle

For every cyclic gap configuration,

`S_(i+r,m-r)=1-S_(i,r)`.

Since `q_u(s)=q_u(1-s)`,

`q_u(S_(i+r,m-r))=q_u(S_(i,r))`.

In the full representation from `VIS-242`,

`bar T=(1/2) sum_(i=0)^(m-1) sum_(r=1)^(m-1) q_u(S_(i,r))`,

terms of lengths `r` and `m-r` are therefore identical after the shift `i -> i+r`. If `r<m/2`, the two length classes combine and cancel the outer factor `1/2`. When `m` is even and `r=m/2`, the class is its own complement, so its factor remains `1/2`.

This gives exactly

`bar T = sum_(r in R_m) w_r sum_i q_u(S_(i,r))`.

The quotient is pointwise for every gap configuration; it uses no probabilistic property of the Dirichlet law. Its only substantive hypothesis is the complement symmetry of the endpoint-quotiented pair kernel.

## 2. Two half-circle arcs have a three-level overlap multiplicity law

Fix `r,s in R_m` and assume without loss of generality that `r<=s`, so `a=r`, `b=s`. Since both lengths are at most `m/2`,

`r+s<=m`.

Hold `A_r={0,...,r-1}` fixed and move the start `d` of `B_(s,d)` once around `Z/mZ`.

The two intervals have positive overlap for exactly `r+s-1` shifts: the moving start can enter from the left through the fixed interval and leave through the right, with the two endpoint-touching positions counted once each in the discrete convention. Hence the number of disjoint shifts is

`m-(r+s-1)=m-r-s+1`.

At the opposite extreme, the shorter interval `A_r` is completely contained in `B_(s,d)` for exactly

`s-r+1=b-a+1`

shifts. These are the consecutive placements whose left and right ends bracket all `r` sites of `A_r`.

Between disjointness and full containment, every overlap size

`k=1,...,r-1`

occurs exactly twice: once while the moving interval enters across one end of `A_r`, and once while it exits across the other end. Therefore

`N_(r,s,0)=m-r-s+1`,
`N_(r,s,a)=b-a+1`,
`N_(r,s,k)=2`, `1<=k<a`.

The formula includes the even half-circle case `r=s=m/2`: there is one disjoint shift, one full-overlap shift, and two shifts for every intermediate overlap size.

Two immediate audits are

`sum_k N_(r,s,k)=m`

and

`sum_k k N_(r,s,k)=rs`.

The second identity is also the usual cyclic cross-correlation count: summed over all shifts, every one of the `r` sites of `A_r` meets each of the `s` sites of the moving interval exactly once.

## 3. The `VIS-242` variance sum becomes explicit

Write

`Y_(i,r)=q_u(S_(i,r))`.

From the half-circle quotient,

`Var_G(bar T)`
` = sum_(r,s in R_m) w_r w_s sum_(i,j) Cov(Y_(i,r),Y_(j,s))`.

Cyclic stationarity of the symmetric-Dirichlet gap law makes the covariance depend on `i,j` only through the displacement `d=j-i mod m`. There are exactly `m` choices of the first start `i`, so

`Var_G(bar T)`
` = m sum_(r,s in R_m) w_r w_s sum_(d=0)^(m-1) C_(r,s,k_(r,s)(d))`.

Substituting the multiplicity law from the previous section gives

`Var_G(bar T)`
` = m sum_(r,s in R_m) w_r w_s [`
`     (m-r-s+1) C_(r,s,0)`
`     + (b-a+1) C_(r,s,a)`
`     + 2 sum_(k=1)^(a-1) C_(r,s,k)`
`   ]`.

This is algebraically equivalent to `VIS-242`, but it removes two avoidable layers of bookkeeping: complementary arc lengths and explicit displacement enumeration. In particular, all required Dirichlet category sizes now satisfy `m-r-s+k>=0` automatically, and the implementation needs only the overlap sizes `0,...,min(r,s)` with fixed known coefficients.

## 4. Prior-art and novelty boundary

The sequence `d -> k_(r,s)(d)` is the circular cross-correlation of two binary interval indicators. Circular correlation and interval-overlap counting are elementary standard constructions; no novelty is claimed for that combinatorics or for complementing an arc on a circle.

The Mathia-specific value of the result is narrower: `VIS-242` left the exact dependent-gap variance as a sum over all arc lengths and displacements, while the present quotient writes the coefficients needed by that particular calibration in closed form and removes the complement-redundant half of the arc-length domain. No external theorem is needed for the derivation.

## Boundaries and falsification

The half-circle quotient applies to the endpoint-phase-invariant statistic `bar T` because its kernel obeys `q_u(s)=q_u(1-s)`. It must not be transferred automatically to a post-cut endpoint-sensitive statistic, to an oriented kernel, or to another visual statistic lacking complement symmetry.

The overlap multiplicity formula is deterministic and independent of `alpha`. It says nothing about whether the symmetric-Dirichlet family is a faithful final model of prime gaps; it only simplifies exact evaluation once that null has been chosen.

A direct falsification is finite and exact: enumerate all `m` shifts for any `1<=r,s<=floor(m/2)` and compare the observed overlap histogram with the displayed multiplicities. The count identities `sum N=m` and `sum kN=rs` provide independent implementation audits.

## Research consequence

The general-`alpha` confirmation calibration no longer requires explicit cyclic-displacement bookkeeping. For every `(r,s)` it needs only the at-most-four-component Dirichlet expectations `M_(r,s,k)` for `0<=k<=min(r,s)`, multiplied by the closed coefficients above, and only for arc lengths up to a half-circle.

This does not answer the accepted confirmation clue. It makes its next numerical step cleaner and less error-prone: freeze the null and representation choices independently, evaluate these deterministic coefficients together with the low-dimensional Dirichlet moments, and only then test whether the prime-coordinate statistic has a stable residual.