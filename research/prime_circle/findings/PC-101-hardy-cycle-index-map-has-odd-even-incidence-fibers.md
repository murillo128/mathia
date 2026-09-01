# PC-101 — Hardy cycle index map has an exact odd/even incidence-fiber classification

**Status:** `EXACT-DERIVED` + `STRUCTURAL-CLASSIFICATION` + `PRIOR-ART-BOUNDARY`. For every cyclically separated Hardy root word, the denominator-index map behind PC-082 is exactly the unsigned incidence map of a cycle. Odd cycle lengths have determinant `2` and give a one-to-one lattice parametrization after one parity condition; even cycle lengths have a one-dimensional alternating kernel, and the trace acquires an explicit piecewise-linear fiber multiplicity. In particular the quartic root-channel trace has the exact Abel-regrouped form

\[
\boxed{
\mathcal P_4(a,b,c,d)
=
\lim_{\rho\uparrow1}
\sum_{\substack{r,s,t,u\ge1\\r+t=s+u}}
\frac{\min(r,s,t,u)\,(\rho a)^r(\rho b)^s(\rho c)^t(\rho d)^u}{rstu}.
}
\]

The even-cycle rank drop therefore does **not** make the higher Hardy periods subcritical: the lost lattice dimension is restored exactly by a degree-one fiber count. After a finite chamber decomposition, every even cycle is again a finite combination of critical cyclotomic conical sums. This sharpens the general cone-period statement of PC-082 and the cubic classicalization of PC-100, but it does **not** prove that the `k>=4` boundary values reduce to cyclotomic multiple polylogarithms.

## 1. Starting point: the separated Hardy cycle trace

For roots of unity `alpha_1,...,alpha_k` with

\[
k\ge2,
\qquad
\alpha_i\alpha_{i+1}\neq1
\quad(i\bmod k),
\]

PC-086 gives the ordinary trace-class root word

\[
\mathcal P_k(\alpha_1,\ldots,\alpha_k)
=
\operatorname{Tr}(\mathcal H_{\alpha_1}\cdots\mathcal H_{\alpha_k}).
\]

Use the radial representatives only as an absolutely convergent device for regrouping. For `0<rho<1`, expansion of the diagonal gives

\[
\mathcal P_{k,\rho}
=
\sum_{j_1,\ldots,j_k\ge0}
\prod_{i=1}^k
\frac{(\rho\alpha_i)^{j_i+j_{i+1}+1}}
{j_i+j_{i+1}+1},
\qquad j_{k+1}=j_1,
\]

and PC-082/PC-086 imply

\[
\boxed{
\mathcal P_k=\lim_{\rho\uparrow1}\mathcal P_{k,\rho}.
}
\]

Set

\[
r_i=j_i+j_{i+1}+1,
\qquad
y_i=r_i-1.
\]

Then `y=B_k j`, where

\[
B_k=I+S
\]

and `S` is the cyclic shift. Equivalently, `B_k` is the unsigned vertex-edge incidence matrix of the cycle `C_k`. All arithmetic weights become simply

\[
\prod_i(\rho\alpha_i)^{r_i},
\]

so the only issue is the exact integer fiber of `B_k`.

## 2. Odd cycle lengths: determinant two and one parity coset

The eigenvalues of `S` are the `k`th roots of unity. Hence

\[
\boxed{
\det B_k=\prod_{\omega^k=1}(1+\omega)=1-(-1)^k.
}
\]

If `k` is odd,

\[
\boxed{\det B_k=2.}
\]

Thus every admissible denominator vector has a unique preimage. Explicitly, with cyclic indices,

\[
\boxed{
2j_i
=y_i-y_{i+1}+y_{i+2}-\cdots+y_{i+k-1}.
}
\]

The image lattice has index two. Since

\[
\sum_i y_i=2\sum_i j_i,
\]

the single congruence selecting it is

\[
\boxed{
\sum_i(r_i-1)\equiv0\pmod2.
}
\]

Together with the `k` inequalities supplied by `j_i>=0`, this gives a rational polyhedral cone cut by one parity coset. Each admissible `r` occurs with multiplicity one.

For `k=3` these inequalities are exactly the strict triangle inequalities and the congruence is `r+s+t` odd, recovering the PC-082 triangle cone. Thus the cubic geometry is the first odd instance of a general incidence-lattice fact, not a special three-variable coincidence.

## 3. Even cycle lengths: one alternating kernel and an exact fiber count

Now let `k` be even. Then

\[
\boxed{
\operatorname{rank}B_k=k-1,
\qquad
\ker B_k=\mathbb R(1,-1,1,-1,\ldots,-1).
}
\]

The same alternating vector spans the left kernel, so a necessary and sufficient integer compatibility condition is

\[
\boxed{
A_k(r):=
\sum_{i=1}^k(-1)^{i-1}r_i=0.
}
\]

There is no additional parity obstruction. To count the nonnegative preimages, define alternating prefixes

\[
A_0(r)=0,
\qquad
A_m(r)=\sum_{i=1}^m(-1)^{i-1}r_i.
\]

Choose `t=j_1`. Solving successively gives the exact formulas

\[
\boxed{
\begin{aligned}
j_i&=t-A_{i-1}(r), && i\ \text{odd},\\
j_i&=A_{i-1}(r)-1-t, && i\ \text{even}.
\end{aligned}
}
\]

Therefore the allowable integer `t` form one interval. Its cardinality is

\[
\boxed{
M_k(r)=
\left[
\min_{\substack{1\le m\le k-1\\m\ \mathrm{odd}}}A_m(r)
-
\max_{\substack{0\le m\le k-2\\m\ \mathrm{even}}}A_m(r)
\right]_+,
}
\]

where `[x]_+=max(x,0)`. Consequently the radial trace may be regrouped exactly as

\[
\boxed{
\mathcal P_{k,\rho}
=
\sum_{\substack{r_1,\ldots,r_k\ge1\\A_k(r)=0}}
M_k(r)
\frac{\prod_i(\rho\alpha_i)^{r_i}}
{\prod_i r_i}.
}
\]

This identity is first proved at `rho<1`, where all sums are absolute. The boundary value `rho -> 1^-` is then the ordinary Hardy trace by PC-086. No conditionally convergent rearrangement is being assumed.

## 4. Quartic cycle: the fiber is exactly `min(r,s,t,u)`

For `k=4`, write the denominator indices as `(r,s,t,u)`. Compatibility is

\[
\boxed{r+t=s+u.}
\]

The prefix formula gives

\[
M_4
=
\min(r,r-s+t)-\max(0,r-s).
\]

Using `r-s+t=u`, a two-case check yields

\[
\boxed{M_4(r,s,t,u)=\min(r,s,t,u).}
\]

Hence

\[
\boxed{
\mathcal P_4(a,b,c,d)
=
\lim_{\rho\uparrow1}
\sum_{\substack{r,s,t,u\ge1\\r+t=s+u}}
\frac{\min(r,s,t,u)\,(\rho a)^r(\rho b)^s(\rho c)^t(\rho d)^u}{rstu}.
}
\]

The formula has direct finite meaning. Given a compatible quadruple, choose `j_1=x`; then

\[
j_2=r-1-x,
\qquad
j_3=s-r+x,
\qquad
j_4=u-1-x.
\]

The number of integers satisfying all four nonnegativity inequalities is exactly `min(r,s,t,u)`. Exhaustive integer checks over small compatible quadruples agree with this count; they are controls only, while the interval derivation above is exact.

The `k=2` specialization is another useful control. Compatibility gives `r_1=r_2=r` and `M_2(r,r)=r`, so

\[
\mathcal P_2(a,b)
=
\lim_{\rho\uparrow1}
\sum_{r\ge1}\frac{(\rho^2ab)^r}{r}
=-\operatorname{Log}(1-ab),
\]

which is exactly the PC-080 separated-pair trace.

## 5. The odd/even rank change preserves critical homogeneity

The parity distinction looks at first like it might improve convergence for even cycles because the denominator lattice loses one dimension. The fiber multiplicity restores that dimension exactly.

For odd `k`, the admissible cone has dimension `k`, multiplicity one, and denominator degree `k`. On a dyadic region where all `r_i` are comparable to `R`, the absolute mass per logarithmic scale is therefore order one.

For even `k`, the compatibility hyperplane has dimension `k-1`, while `M_k(r)` is homogeneous piecewise linear of degree one. Thus the effective summand has degree

\[
1-k=-(k-1),
\]

again equal to minus the cone dimension. There are interior rays with `M_k(r)>0` — for example `r_1=\cdots=r_k=R`, where `M_k=R` — so the unweighted absolute sum is again logarithmically critical.

More precisely, there are only finitely many chambers according to which odd prefix realizes the minimum and which even prefix realizes the maximum. On each chamber,

\[
M_k(r)=A_{m_\mathrm{odd}}(r)-A_{m_\mathrm{even}}(r)
\]

is one linear form. Expanding that numerator as a signed sum of the coordinates `r_i` cancels one denominator factor term by term. Hence every even cycle is a finite linear combination of root-of-unity-weighted rational-cone sums with

\[
\boxed{
\dim=k-1,
\qquad
\text{denominator degree}=k-1.
}
\]

So both parities land on the same critical conical boundary identified abstractly in PC-082, but by different exact lattice mechanisms.

## 6. Prior-art and novelty audit

The linear-algebra core is classical. `B_k` is the ordinary unsigned incidence matrix of a cycle: odd cycles are non-bipartite and give the determinant-two case, while even cycles are bipartite and carry the alternating null vector. The determinant formula above is included explicitly so that no graph-theoretic novelty is being claimed.

The arithmetic target is likewise surrounded by established conical-period theory already anchored in `research/prime_circle/SOURCES.md`: Terasoma's rational-cone theorem places **absolutely convergent** finite-order-character cone values in cyclotomic multiple-zeta spaces, while Guo--Paycha--Zhang develop conical zeta values and their renormalizations. PC-100 further proves by a special horn decomposition that the first odd critical case, `k=3`, actually lands in weight-three cyclotomic multiple-polylogarithms despite failing absolute convergence.

The present calculation does not justify extrapolating PC-100 to `k>=4`. In particular, splitting the even fiber count into finitely many rational chambers proves a critical cyclotomic-cone classification, but not that the Hardy-selected boundary value agrees with a standard regularized conical zeta value or reduces to cyclotomic MPVs. Directed comparison with the conical/Mordell--Tornheim literature finds strong neighboring reduction technology, not an already identified Prime-Circle cycle-fiber theorem; the safe novelty conclusion is therefore **structural classification and boundary sharpening**, not a new period theorem.

## 7. RH consequence and remaining boundary

The exact odd/even incidence geometry supplies no new candidate RH parameter. Cycle parity changes how the same static Hardy period is coordinatized:

\[
\boxed{
\begin{array}{c}
 k\ \text{odd}:\ \text{index-2 lattice cone, multiplicity }1,\\[2mm]
 k\ \text{even}:\ \text{codimension-1 cone, piecewise-linear fiber multiplicity}.
\end{array}
}
\]

In both cases the resulting conical sum is critical. There is still no geometry-forced free complex variable, gamma factor, `s<->1-s` symmetry, positivity criterion for RH, or zero divisor. The even-cycle singularity of the incidence map is therefore **not** by itself a new spectral mechanism.

What remains genuinely open after PC-100 and this finding is narrower: determine whether the critical boundary values at `k>=4` reduce to classical cyclotomic MPVs/regularized conical values, and separately whether repeated-shell words outside rootwise cyclic separation or an intrinsically generated infinite-shell/global Hardy construction produce a new analytic family. The parity/fiber phenomenon itself is now exact and should not be treated as unexplained extra arithmetic.

## 8. Falsification surface

1. For odd `k`, diagonalize `I+S`; its determinant must be `2`, and the displayed alternating inverse must recover every `j_i`.
2. Verify that the odd image lattice is exactly the single parity coset `sum(r_i-1)=0 mod 2`; any additional congruence would refute the index argument.
3. For even `k`, solve recursively from `j_1=t`; closure must be equivalent to `A_k(r)=0`, with no further integer congruence.
4. The nonnegativity interval for `t` must have cardinality exactly the displayed `M_k(r)`. Brute-force checks at `k=4` and `k=6` agree once the positive part is included.
5. At `k=4`, enumerate compatible positive quadruples and verify both the fiber equations and `M_4=min(r,s,t,u)`.
6. At `k=2`, the formula must reduce to `-Log(1-ab)`, and at `k=3` the odd inverse must reduce to the triangle/parity cone of PC-082.
7. The regrouped infinite formula must be derived first at `rho<1`; dropping the Abel bridge before proving a separate rearrangement theorem would be invalid because the absolute series is critical.
8. No claim that `k>=4` values are cyclotomic MPVs is licensed by this finding. Such a claim requires a separate reduction or a theorem covering the exact Hardy boundary prescription.
