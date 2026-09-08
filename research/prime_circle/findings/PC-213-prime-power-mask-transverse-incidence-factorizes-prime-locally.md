# PC-213 — prime-power mask/transverse incidence factorizes prime-locally

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the first nonlinear incidence repair left open by PC-212: multiply source-derived prime-power coefficient masks before scalar contraction, retain the resulting position-space support projection, and couple it directly to the exact-order transverse Fourier projectors of PC-066.

PC-212 shows that pairwise common-refinement Gram data of the normalized cyclotomic coefficient masks are central, coprime-flat after centering, and supported on proper-divisor Fourier conductors. That result deliberately leaves open nonlinear incidence information that is lost by pairwise Gram contraction. The most canonical such repair on the Mangoldt-supported prime-power sector is to multiply several prime-power masks pointwise and then ask how the resulting compact-open position support meets the exact-order Fourier sectors.

This repair is genuinely noncommutative: multiplication by a compact-open subgroup indicator need not commute with an exact-order Fourier projector. Nevertheless its complete two-projection geometry is exactly soluble. If

\[
K=\widehat{\mathbb Z},
\qquad
H_M=M K,
\qquad
Q_M=M_{\mathbf 1_{H_M}},
\]

and `P_n` is the PC-066 projector onto characters of exact order `n`, put

\[
d=(n,M),
\qquad
r=\frac{n}{d}.
\]

Then, after the canonical unitary identification of `L^2(K)` with the support space `Q_ML^2(K)`, one has

\[
\boxed{
U_M^*Q_MP_nQ_MU_M
=
\frac{\varphi(n)}{M\varphi(r)}P_r.
}
\tag{1}
\]

Thus `Q_MP_nQ_M` has only one nonzero eigenvalue,

\[
\boxed{
\lambda(M,n)=\frac{\varphi(n)}{M\varphi(n/(n,M))},
}
\tag{2}
\]

with multiplicity `\varphi(n/(n,M))`. All remaining principal angles are right angles. The surviving nonzero angle, when it is not `0`, is repeated rather than forming a new spectral packet.

Moreover `\lambda(M,n)` factors exactly over primes. There is no irreducible mixed-prime coefficient. Consequently the first source-forced nonlinear product of distinct prime-power coefficient masks, even when it is coupled to the full exact-order transverse decomposition before taking traces or determinants, reduces to classical conductor stripping on `\mathbb Q/\mathbb Z` and independent one-prime valuation factors.

This is stronger than PC-212's pairwise Gram obstruction on the prime-power sector, but it does **not** classify individual mixed-composite masks `g_n`, non-Haar matrix fibers, vertexwise old/new incidence not reducible to compact-open support, or genuinely growing/nonlinear cross-level tensors.

## 1. Prime-power coefficient masks become compact-open support projections

Retain the common-refinement cylinder functions of PC-212. If

\[
\Phi_n(z)=\sum_{a=0}^{n-1}a_n(a)z^a,
\qquad
h_n=\|\Phi_n\|_{H^2}^2,
\]

then

\[
g_n(x)=\sqrt{\frac n{h_n}}\,a_n(x\bmod n),
\qquad x\in K.
\tag{3}
\]

For a prime power `p^s`, PC-212 gives the exact formula

\[
\boxed{
g_{p^s}(x)=p^{(s-1)/2}\mathbf1_{p^{s-1}K}(x).}
\tag{4}
\]

Now choose distinct primes `p_1,\ldots,p_t` and exponents `s_i\ge1`. Because the compact-open subgroups for distinct primes intersect by the Chinese remainder theorem,

\[
\bigcap_{i=1}^t p_i^{s_i-1}K
=
M K,
\qquad
M:=\prod_{i=1}^t p_i^{s_i-1}.
\tag{5}
\]

Therefore the pointwise product of the source-derived masks is

\[
\boxed{
G_M(x)
:=\prod_{i=1}^t g_{p_i^{s_i}}(x)
=
\sqrt M\,\mathbf1_{M K}(x).
}
\tag{6}
\]

Since Haar probability satisfies `m_K(MK)=1/M`, this product is again a unit vector in `L^2(K)`.

Equation (6) is the first nonlinear operation on the PC-212 prime-power states that does not immediately reduce to their pairwise inner products. As a multiplication operator,

\[
M_{G_M}=\sqrt M\,Q_M,
\qquad
Q_M:=M_{\mathbf1_{MK}},
\tag{7}
\]

so the retained datum is the actual position-space support projection, not a scalar overlap.

## 2. Exact-order characters restrict by conductor stripping

PC-066 decomposes

\[
L^2(K)=\bigoplus_{n\ge1}E_n,
\qquad
P_n:L^2(K)\to E_n,
\tag{8}
\]

where `E_n` is spanned by the characters of exact order `n` in

\[
\widehat K\cong\mathbb Q/\mathbb Z.
\]

Let `\gamma` have exact order `n`. Restricting its character from `K` to the subgroup `H_M=MK` amounts, after the parametrization `x\mapsto Mx`, to replacing `\gamma` by `M\gamma`. Its exact order is

\[
\boxed{
\operatorname{ord}(M\gamma)
=
\frac{n}{(n,M)}
=r.
}
\tag{9}
\]

The restriction map from exact-order-`n` characters onto exact-order-`r` characters is uniform. Indeed write

\[
n=dr,
\qquad
M=dM',
\qquad
(M',r)=1.
\]

Multiplication by `M'` permutes `(\mathbb Z/r\mathbb Z)^\times`, while the usual reduction

\[
(\mathbb Z/n\mathbb Z)^\times
\longrightarrow
(\mathbb Z/r\mathbb Z)^\times
\]

is surjective. Hence every exact-order-`r` character has exactly

\[
\boxed{
\frac{\varphi(n)}{\varphi(r)}
}
\tag{10}
\]

exact-order-`n` lifts under restriction.

Summing the characters gives the equivalent Ramanujan identity

\[
\boxed{
c_n(Mx)
=
\frac{\varphi(n)}{\varphi(r)}c_r(x),
\qquad
r=\frac{n}{(n,M)}.
}
\tag{11}
\]

This is also immediate from the classical divisor/Hölder formulas for Ramanujan sums. The important point here is not novelty of (11), but what it does to the source-derived Prime-Circle incidence operator.

## 3. The support/exact-order sandwich has one singular value

Define

\[
U_M:L^2(K)\longrightarrow Q_ML^2(K)
\]

by

\[
\boxed{
(U_Mf)(Mx)=\sqrt M\,f(x).
}
\tag{12}
\]

Multiplication by `M` identifies `K` topologically with `MK`, and ambient Haar measure on `MK` is `1/M` times its normalized Haar measure, so `U_M` is unitary onto `Q_ML^2(K)`.

The exact-order projector has the convolution kernel

\[
(P_nf)(x)
=
\int_K c_n(x-y)f(y)\,dm_K(y).
\tag{13}
\]

For `f\in L^2(K)`, evaluate the compressed operator at `Mt`. Using the change of variables `y=Mu` on `MK` and then (11),

\[
\begin{aligned}
(U_M^*Q_MP_nQ_MU_Mf)(t)
&=
\frac1M\int_K c_n(M(t-u))f(u)\,dm_K(u)\\
&=
\frac{\varphi(n)}{M\varphi(r)}
\int_K c_r(t-u)f(u)\,dm_K(u).
\end{aligned}
\tag{14}
\]

Therefore

\[
\boxed{
U_M^*Q_MP_nQ_MU_M
=
\lambda(M,n)P_r,
\qquad
\lambda(M,n)
=
\frac{\varphi(n)}{M\varphi(r)}.
}
\tag{15}
\]

No limiting argument or scalar trace has been taken. Equation (15) is an exact operator identity on the full profinite Hilbert space.

Since `P_r` has rank `\varphi(r)`, the nonzero spectrum is

\[
\boxed{
\operatorname{Spec}_{\ne0}(Q_MP_nQ_M)
=
\{\lambda(M,n)\}^{\times\varphi(r)}.
}
\tag{16}
\]

The corresponding nonzero singular values of `Q_M|_{E_n}` are all

\[
\sqrt{\lambda(M,n)}.
\tag{17}
\]

Thus the two subspaces `MK`-supported functions and exact-order-`n` Fourier modes are isoclinic on their interacting part. There is no family of unequal principal angles from which a new spectral statistic could be extracted.

For completeness, when `0<\lambda(M,n)<1`, the standard two-projection geometry gives

\[
\boxed{
\|[Q_M,P_n]\|
=
\sqrt{\lambda(M,n)(1-\lambda(M,n))}.
}
\tag{18}
\]

When `\lambda(M,n)=1`, the interacting angle is zero and the projections commute on the exact reduced-conductor channel. The apparent noncommutativity is therefore completely controlled by the one classical scalar (2).

## 4. The scalar factor is a product of independent prime-local terms

Write

\[
M=\prod_p p^{j_p},
\qquad
n=\prod_p p^{k_p}.
\tag{19}
\]

Then

\[
r=\frac n{(n,M)}
=
\prod_p p^{(k_p-j_p)_+},
\tag{20}
\]

and multiplicativity of `\varphi` gives

\[
\boxed{
\lambda(M,n)
=
\prod_p \lambda_p(j_p,k_p),
}
\tag{21}
\]

where

\[
\boxed{
\lambda_p(j,k)=
\begin{cases}
1,&k>j,\\[1mm]
(1-p^{-1})p^{k-j},&1\le k\le j,\\[1mm]
p^{-j},&k=0.
\end{cases}
}
\tag{22}
\]

There is no mixed coefficient involving two distinct primes. Even the complete noncommutative incidence between the position projection and an exact-order Fourier block is the external product of one-prime conductor-stripping responses.

The condition for the nonzero angle to collapse to zero is correspondingly local:

\[
\boxed{
\lambda(M,n)=1
\iff
v_p(n)>v_p(M)
\text{ for every }p\mid M.
}
\tag{23}
\]

In that regime the subgroup mask does not partially cut the relevant conductor; it simply identifies the exact reduced-conductor sector after restriction.

## 5. Returning to the Prime-Circle nonlinear mask product

For the actual source-derived product (6),

\[
M_{G_M}=\sqrt M Q_M.
\]

Hence (15) immediately yields

\[
\boxed{
U_M^*M_{G_M}P_nM_{G_M}U_M
=
\frac{\varphi(n)}{\varphi(r)}P_r,
\qquad
r=\frac n{(n,M)}.
}
\tag{24}
\]

This is the strongest form of the obstruction. The operation has deliberately retained more information than PC-212's pairwise Gram kernel:

- distinct prime-power coefficient states are multiplied **before** contraction;
- their common support is retained as a position-space projection;
- that projection is coupled to the full exact-order transverse decomposition;
- the two projections generally do not commute.

Nevertheless the entire sandwich is just exact conductor restriction with the classical character-lift multiplicity `\varphi(n)/\varphi(r)`.

In particular, composing several distinct prime-power channels cannot produce an irreducible mixed-prime transverse tensor through this incidence mechanism. The only interaction between prime axes is the elementary formation of the integer `M`; after that, every spectral and angle invariant factorizes as (21).

## 6. Matched controls and failure boundary

The obstruction is not prime-specific. Equation (15) holds for **every** integer `M` and every exact-order projector `P_n`; it depends only on the compact-open subgroup `MK` and ordinary character restriction. A matched composite/conductor control preserving the same subgroup index and exact-order Fourier sector produces exactly the same operator identity. Thus the response cannot certify that `M` arose as a product of prime-power birth masks rather than from another realization of the same profinite support.

The theorem is also deliberately narrower than a universal nonlinear no-go.

First, an individual mixed-composite coefficient field `g_N` from PC-212 is generally not a normalized indicator of one compact-open subgroup. PC-212 shows that such fields can have nonconstant profiles on proper-divisor conductor sectors. Their multiplication operators are not classified by (15).

Second, the theorem addresses only the canonical position/Fourier incidence obtained from the prime-power masks. An old/new vertex operator that retains actual embedded roots, a matrix-valued/non-Haar transport, or a tensor whose coefficients depend on more than compact-open membership is outside the result.

Third, arbitrary growing products or renormalized infinite-depth constructions require an independently specified topology and operator domain. Equation (15) closes every finite subgroup-mask/exact-order sandwich, but it does not justify exchanging an infinite product with a spectral limit.

Finally, no choice of a subsequent scalar functional of `\lambda(M,n)` becomes intrinsic RH evidence merely because it is spectral. Weighting the conductor variable afterward would reintroduce the arbitrary scale already exposed by PC-066.

## 7. Prior art and novelty audit

The abstract harmonic-analysis ingredients are classical.

PC-066 already records the Pontryagin decomposition of `L^2(\widehat{\mathbb Z})` into exact-order character spaces and identifies their projectors with Ramanujan-sum kernels. More generally, the duality between a closed subgroup and the quotient of the dual by its annihilator is standard Pontryagin theory; Walter Rudin's *Fourier Analysis on Groups* gives the classical subgroup/quotient Fourier framework. Restricting a character to `MK` and reducing its conductor from `n` to `n/(n,M)` is an elementary specialization of that theory.

The kernel identity (11) is standard Ramanujan-sum arithmetic. Ramanujan's original trigonometric sums and the classical divisor formula for `c_n` are already anchored in `research/prime_circle/SOURCES.md`. The prime-power compact-open/Haar viewpoint is likewise ordinary profinite and `p`-adic harmonic analysis; PC-212 already places its prime-power cylinder orthogonalization beside standard `p`-adic Haar/wavelet theory.

No novelty is claimed for subgroup annihilators, character restriction, Ramanujan identities, isoclinic projection geometry, or prime-local totient factorization. The durable Prime-Circle-specific result is the **composition of those classical facts with the exact source-derived mask formula of PC-212**: the first nonlinear pointwise fusion of the Mangoldt-supported prime-power masks, even before scalar contraction and even after coupling to the canonical transverse exact-order projectors, has only conductor-stripping incidence and no irreducible mixed-prime sector.

A targeted prior-art check found the expected general subgroup/quotient duality and `p`-adic Haar structure, not a distinct RH mechanism attached to this particular Prime-Circle sandwich. The appropriate classification is therefore a classicalization/boundary result rather than a novelty claim.

## 8. Consequence for the surviving frontier

PC-212 left open the possibility that the coefficient masks were too aggressively compressed by pairwise Gram data. PC-213 shows that, on the prime-power sector where the masks have the cleanest source-forced form, **retaining their position support and coupling it noncommutatively to exact-order Fourier sectors still does not restore mixed-prime information**.

The chain

\[
\text{prime-power cyclotomic masks}
\longrightarrow
\text{pointwise nonlinear fusion}
\longrightarrow
\text{compact-open incidence with }P_n
\longrightarrow
\text{new mixed-prime spectral carrier}
\]

therefore stops at the third arrow: the incidence is exactly the classical conductor map `n\mapsto n/(n,M)` with independent local totient factors.

A continuation of the common-refinement route must retain information not encoded by compact-open support of the prime-power coefficient masks. Plausible category exits remain individual mixed-composite profile geometry, old/new vertex incidence before coefficient-mask reduction, non-Haar or matrix-valued fibers, intrinsically non-Cauchy/non-separable growing tensors, or global uniformization/monodromy. Those are open boundaries, not evidence that a surviving RH mechanism exists.
