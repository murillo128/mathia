# FD-177 — Long dyadic block repair preserves every subextremal multiplicative-rank window

- **Date:** 2026-09-17
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** restricted temporal acquisition / dyadic block repair / growing-rank compatibility / sparse permanent null source
- **Depends on:** FD-117, FD-170, FD-172, FD-173, FD-175, FD-176
- **Classification:** `EXACT-DERIVED + PERMANENT-SOURCE + DYADIC-NULL + SUBEXTREMAL-RANK-FIDELITY + ARBITRARILY-SPARSE-DELETION + NONMULTIPLICATIVE`

## Claim

`FD-176` left the dyadic base `B=2` open because its one-step repair recurrence spends the full linear source exponent. Grouping several consecutive dyadic samples into one block removes that loss.

Fix any

\[
0<\rho<1,
\qquad
\eta>0,
\tag{1}
\]

and any finite cutoff `X`. There exists one permanent arithmetic source `a\not\equiv\mu` such that

\[
a(n)\in\{0,\mu(n)\}\qquad(n\ge1),
\tag{2}
\]

\[
a(n)=\mu(n)\qquad(n\le X),
\tag{3}
\]

and, for every sufficiently large squarefree `n`,

\[
\omega(n)\le
\rho\frac{\log n}{\log\log n}
\quad\Longrightarrow\quad
a(n)=\mu(n).
\tag{4}
\]

The construction can be started far enough out that every prescribed finite exceptional prefix is also untouched. In particular all prime coefficients remain exactly physical. Nevertheless

\[
\boxed{
P_a(2^m)=P_\mu(2^m)
\qquad\text{for every }m\ge1,
}
\tag{5}
\]

where `P_a(H)` is the midpoint sensor of `FD-170`.

Moreover, if

\[
S:=\{n:a(n)=0,\ \mu(n)\ne0\}
\tag{6}
\]

is the deletion set, then the source may be chosen so that

\[
\boxed{S(x)=O_{\rho,\eta,X}(x^\eta).}
\tag{7}
\]

Thus the dyadic ladder remains blind even when every squarefree coefficient below any fixed subextremal fraction of the maximal `omega(n)` scale is forced to equal Möbius, and the deviations themselves are allowed only on an arbitrarily small polynomial-size set. The obstruction from `FD-175` is therefore not peculiar to fixed rank, and the exponent-gap failure noted for `B=2` in `FD-176` is an artifact of repairing one dyadic sample at a time.

## 1. Midpoint deletion balance and nearest-integer form

Retain the exact deletion balance of `FD-175`. For a squarefree deletion set `S`, put

\[
\sigma(d):=-\mu(d)\in\{-1,+1\},
\tag{8}
\]

and

\[
C_H(S)
=
\sum_{\substack{d\in S\\d\le H}}
\sigma(d)W_H(d),
\qquad
W_H(d)=\#\{r\le H/d:r\text{ odd}\}.
\tag{9}
\]

Then

\[
P_a(H)=P_\mu(H)
\iff
C_H(S)=0.
\tag{10}
\]

The odd-multiple weight has the useful exact form

\[
W_H(d)
=
\left\lfloor\frac{H}{2d}+\frac12\right\rfloor.
\tag{11}
\]

Write

\[
R(x):=\lfloor x+1/2\rfloor.
\tag{12}
\]

Fix a block base `L` and suppose the old deletion set is contained in `[1,L]` and already satisfies `C_L=0`. For `r>=1` define the dyadic rounding defect

\[
\delta_r(d)
:=
W_{2^rL}(d)-2W_{2^{r-1}L}(d).
\tag{13}
\]

If `x=L/(2d)`, then

\[
\delta_r(d)
=
R(2^r x)-2R(2^{r-1}x).
\tag{14}
\]

Let the fractional part of `x` have binary expansion

\[
\{x\}=0.b_1b_2b_3\ldots,
\tag{15}
\]

using the terminating expansion at dyadic rationals. The tie-up convention in `R` gives the exact digit identity

\[
\boxed{
\delta_r(d)=b_{r+1}-b_r.
}
\tag{16}
\]

Indeed the defect is `+1` on binary cylinders beginning `01`, `-1` on those beginning `10`, and zero on `00` or `11`. This is the extra structure missed by the one-step absolute bound `|\delta_r|<=1`: the nonzero defects are signed bit transitions rather than independent errors.

For the old support define

\[
E_r:=\sum_{d\in S}\sigma(d)\delta_r(d).
\tag{17}
\]

Since `C_L=0`, repeated use of (13) gives, for every `1<=j<=k`,

\[
C_{2^jL}(S_{\rm old})
=
\sum_{r=1}^j2^{j-r}E_r.
\tag{18}
\]

The problem is therefore to cancel these `k` old-support responses simultaneously with fresh deletions above `L`.

## 2. One fresh shell contains a unimodular basis for all `k` dyadic samples

Fix an integer block length `k>=2`. For a fresh deletion `d\in(L,2L]`, put

\[
z:=L/d\in[1/2,1).
\tag{19}
\]

Its response vector across the block is

\[
v(d)=
\bigl(W_{2L}(d),W_{4L}(d),\ldots,W_{2^kL}(d)\bigr),
\tag{20}
\]

with

\[
W_{2^jL}(d)=R(2^{j-1}z).
\tag{21}
\]

Choose `k` disjoint nondegenerate intervals in the `z` coordinate. Let

\[
J_1=[1/2,\,1/2+2^{-k}),
\tag{22}
\]

and, for `2<=s<=k`,

\[
J_s=
\left[
\frac12+2^{1-s}-2^{-k},
\frac12+2^{1-s}
\right).
\tag{23}
\]

Put `I_s(L)={d\in(L,2L]:L/d\in J_s}`. Each `I_s(L)` is a fixed-ratio interval of length comparable with `L`, with constants depending only on `k`.

Every `d\in I_s(L)` has the same response vector `v^(s)`. Write

\[
b_1=1,
\qquad
b_j=2^{j-2}\quad(j>=2).
\tag{24}
\]

Then

\[
v^{(1)}_j=b_j,
\tag{25}
\]

while, for `s>=2`,

\[
v^{(s)}_j
=
\begin{cases}
b_j,&j<s,\\
b_j+2^{j-s},&j>=s.
\end{cases}
\tag{26}
\]

This follows directly by scaling the interval (23): below coordinate `s` the perturbation stays strictly below the half-integer threshold, while from coordinate `s` onward it rounds to the indicated integer tail. In particular the `k x k` matrix with columns `v^(1),...,v^(k)` is unimodular: subtracting its first column from the others leaves a lower-triangular tail matrix with unit diagonal.

Let `x_s` be the signed sum of `sigma(d)` over new deletions chosen from `I_s(L)`. The unique integer solution cancelling all old responses (18) is

\[
\boxed{
\begin{aligned}
x_1&=E_2+E_3+\cdots+E_k,\\
x_2&=-(E_1+E_2),\\
x_s&=-E_s\qquad(3\le s\le k).
\end{aligned}
}
\tag{27}
\]

Substitution into (25)--(26) gives

\[
C_{2^jL}(S_{\rm old}\cup S_{\rm fresh})=0
\qquad(1\le j\le k).
\tag{28}
\]

Thus one shell `(L,2L]` can repair an entire block of `k` consecutive dyadic observations.

## 3. The binary cocycle makes the full block cost only `k` fresh deletions per old deletion

Suppose the old support contains `N` deletions. Equation (27) requires

\[
M_{\rm fresh}
:=
\sum_{s=1}^k|x_s|
\le
\left|\sum_{r=2}^kE_r\right|
+|E_1+E_2|
+\sum_{r=3}^k|E_r|.
\tag{29}
\]

Apply the triangle inequality before summing over old coordinates. For one old deletion, (16) telescopes:

\[
\sum_{r=2}^k\delta_r
=b_{k+1}-b_2,
\qquad
\delta_1+\delta_2
=b_3-b_1.
\tag{30}
\]

Hence each of the first two absolute values costs at most one. Also

\[
\sum_{r=3}^k|\delta_r|\le k-2.
\tag{31}
\]

Therefore every old coordinate contributes at most `k` to the right side of (29), and

\[
\boxed{M_{\rm fresh}\le kN.}
\tag{32}
\]

After one complete block the total deletion count grows by at most

\[
N_{\rm new}\le(k+1)N,
\tag{33}
\]

while the horizon grows by the factor `2^k`. Iterating blocks with

\[
L_{j+1}=2^kL_j
\tag{34}
\]

therefore gives

\[
N_j\ll(k+1)^j
=L_j^{\alpha_k},
\qquad
\boxed{
\alpha_k:=\frac{\log_2(k+1)}{k}.
}
\tag{35}
\]

Since `alpha_k<1` for every `k>=2` and `alpha_k->0`, the deletion set has zero density, and by choosing `k` large it can have arbitrarily small positive polynomial counting exponent.

The block partition covers every dyadic horizon, not merely the coarser subsequence `2^{kj}`. At block `j`, (28) enforces the intermediate horizons `2L_j,4L_j,...,2^kL_j`; the last is the next block base. Starting the first block above the prescribed cutoff leaves every earlier dyadic sample untouched.

To seed a nontrivial source, choose at the first active block two admissible squarefree deletions of opposite Möbius sign inside the same interval `I_1(L)`. Their complete `k`-sample response vectors agree, so their signed contributions cancel at every sample in that first block.

## 4. Long blocks recover every fixed `rho<1` growing-rank fidelity window

The finite repair theorem above is purely combinatorial. To force all modifications into high multiplicative rank, use the same primorial reservoir as `FD-176`, now separately inside each fixed-ratio interval `I_s(L)`.

Fix `rho<1`. Choose `k` so large that

\[
\alpha_k<1-\rho,
\tag{36}
\]

and then choose

\[
\rho<\rho'<1-\alpha_k.
\tag{37}
\]

At a large block base `L`, let

\[
r=
\left\lfloor
\rho'\frac{\log L}{\log\log L}
\right\rfloor
\tag{38}
\]

with parity adjusted by at most one according to the required Möbius sign, and let `P_r=p_1\cdots p_r`. The prime number theorem gives

\[
P_r=L^{\rho'+o(1)}.
\tag{39}
\]

For each fixed interval `I_s(L)=(c_sL,c'_sL)` in source coordinates, primes

\[
\frac{c_sL}{P_r}<q\le\frac{c'_sL}{P_r}
\tag{40}
\]

produce squarefree integers `n=P_rq\in I_s(L)` once `L` is large. Since `q>p_r` eventually,

\[
\omega(n)=r+1
=(\rho'+o(1))\frac{\log L}{\log\log L}.
\tag{41}
\]

The PNT in this fixed-ratio interval supplies

\[
L^{1-\rho'+o(1)}
\tag{42}
\]

such integers. Changing the parity of `r` supplies either Möbius sign. Because

\[
1-\rho'>\alpha_k,
\tag{43}
\]

this reservoir dominates every signed correction demand in (27), all of which are `O_k(L^{\alpha_k})`. Thus every block can be repaired using only deletions whose rank exceeds

\[
\rho\frac{\log n}{\log\log n}
\tag{44}
\]

for sufficiently large `L`.

Starting after an arbitrary finite prefix yields (2)--(5). Equation (35) gives `S(x)=O(x^{alpha_k})`. Since `alpha_k->0`, for the independently prescribed `eta>0` we may enlarge `k` further until

\[
\alpha_k<\eta,
\tag{45}
\]

which proves (7).

The constant `1` in the restriction `rho<1` is not an artifact of the proof normalization: the extremal possible order of `omega(n)` is `(1+o(1))log n/log log n`. This pass reaches every fixed fraction strictly below that scale. It does **not** settle the endpoint where the admissible correction reservoir itself becomes subpower and primorial-extremal.

## 5. Stress tests and boundary

The improvement is not obtained by weakening the observation model. Every dyadic midpoint sample remains exact, and the source is permanent. Nor is it obtained by changing coefficient signs or creating nonsquarefree support: modifications remain deletion-only, `a(n) in {0,mu(n)}`, and every protected coefficient is exactly physical.

The mechanism is specifically dyadic. What saves source budget is not a generic longer-block averaging argument but the exact nearest-integer doubling cocycle (16), together with the unimodular family of fresh response signatures (25)--(26). Treating the `k` rounding defects independently would reproduce the linear one-step loss and miss the telescoping binary structure.

The theorem remains an identifiability counterexample in a nonmultiplicative source class. It does not produce a multiplicative source distinct from Möbius, does not weaken the exact target-rigidity theorem `FD-172`, and does not imply any new Mertens cancellation or Franel--Landau estimate. Rather, it rules out a much larger family of candidate weakenings of multiplicativity: exact product compatibility on every squarefree coefficient whose rank is at most any fixed subextremal fraction of the maximal rank scale still does not suffice.

There is also no contradiction with `FD-173`. That theorem works inside the fully multiplicative cone, where one defective prime propagates coherently through all squarefree products. Here all prime values and an arbitrarily deep rank window are correct, but a tiny set of near-extremal-rank composites is allowed to decouple from its prime factors and supplies the correction degrees of freedom.

## Representation audit

The representation is unchanged from `FD-170`, `FD-175`, and `FD-176`: the exact midpoint temporal sensor is rewritten as the weighted deletion balance (9). The new step remains in the same source coordinates and exploits structure already present in the dyadic row family. No norm, reconstruction map, or observable is introduced.

The generic finite ingredient is a rounded-dilation block system whose one-step defects are binary transitions and whose fresh-shell response vectors contain a unimodular basis. The Farey/Möbius-specific splice is that the midpoint sensor has precisely the odd-multiple weight (11), while high-rank squarefree numbers of either Möbius sign can be populated in every fixed-ratio fresh interval through a primorial-times-prime construction.

The information deliberately lost is still global multiplicativity at the modified near-extremal composites. Local coefficient fidelity, prime fidelity, squarefree support, sign compatibility, every prescribed finite prefix, and now every fixed subextremal multiplicative-rank window all survive.

## Prior-art audit

A targeted search around nearest-integer dyadic rounding cocycles, lacunary Möbius sampling, and Farey midpoint reconstruction found standard rounding facts, general lacunary/spectral sampling literature, and the classical Farey-discrepancy sources already represented locally, but no direct analogue of the blockwise permanent null construction above. No novelty claim is made for nearest-integer rounding, binary carries, unimodular elimination, primorial asymptotics, or fixed-ratio prime counts.

The only analytic input used in the permanent high-rank source is the prime number theorem, already anchored in `SOURCES.md` by Newman. No new durable external dependency is introduced, so `SOURCES.md` is unchanged.

The exact finite block lemma (16)--(35) has a bounded formal surface, but the substantive permanent-source theorem also uses the asymptotic prime reservoir. No formalization handoff is opened in this pass because formalizing only the elementary block core would not certify the source-fidelity conclusion that makes the result research-significant.

## Consequence for the research frontier

`FD-176` isolated the dyadic ladder as the case where one-step repair appeared to leave no positive growing-rank window. That boundary disappears. For any fixed `rho<1`, sufficiently long dyadic blocks make the source-repair exponent smaller than `1-rho`, and the remaining near-extremal-rank composites contain enough correction capacity to hide every dyadic sample.

The local-rank route is therefore almost exhausted: no fixed fractional cutoff below the extremal `omega(n)` scale can replace full multiplicativity. The remaining sharp boundary is the endpoint regime itself—compatibility extending to `(1-o(1))log n/log log n` or all squarefree ranks—or a genuinely cross-coordinate condition that couples the protected low-rank region to the rare near-primorial composites instead of merely enlarging the set of coordinates checked independently.

No accepted clue changes status.