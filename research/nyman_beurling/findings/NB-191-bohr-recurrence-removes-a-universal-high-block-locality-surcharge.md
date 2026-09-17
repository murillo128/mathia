# NB-191 — Bohr recurrence removes a universal high-block locality surcharge

**Date:** 2026-09-17  
**Status:** `DERIVED + NEGATIVE/OBSTRUCTION + SOURCE-ACQUISITION + HIGH-BLOCK-LOCALITY + BOHR-RECURRENCE + SHARP-INVERSE-MASS-TARIFF + NB-190-REFINEMENT`.

`NB-190` leaves acquisition locality as the most direct next negative route. Its fixed-accuracy synthesis of one normalized Euler--Wiener band uses an unrestricted Fourier--Stieltjes measure on the height variable; perhaps forcing that measure into a high block `[T,2T]` could impose a new time--frequency tariff beyond the sharp inverse-source-mass cost `Theta(K)`, where `K asymp 1/a`.

Locality alone cannot do this uniformly. For every fixed exterior width `a` and fixed positive synthesis accuracy, the compactly truncated `NB-190` band synthesizers can be translated into **every sufficiently high dyadic block** without changing their `Theta(K)` total-variation order. The reason is finite-frequency Bohr recurrence: the union of the `K` target bands contains only finitely many active Euler frequencies at fixed `a`, and their joint phase vector returns arbitrarily close to the identity with a syndetic set of height shifts. A common return shift works for all `K` bands simultaneously.

Consequently the uniformly source-normalized high-ordinate tariff from `NB-190` is also sharp under block localization: on every sufficiently high block at fixed `a`, one can synthesize each normalized band with total variation `Theta(H_T)`, matching the `Omega(H_T)` lower bound already proved there. What remains potentially useful is therefore not locality by itself but the **joint scaling** of the recurrence length with `a=a_T`. As `a -> 0` the active prime-log dimension explodes, so the first guaranteed common return may lie far beyond the arithmetic height under study. Any genuine locality obstruction must quantify that `a`--`T` competition rather than charge merely for being far from height zero.

## Setup

Retain the normalized Euler--Wiener source of `NB-182` and the balanced bands of `NB-189`--`NB-190`. Thus

\[
\lambda_n:=\log n,
\qquad
\alpha_{n,a}\ge0,
\qquad
\sum_{n\ge2}\alpha_{n,a}=1,
\tag{1}
\]

and, for fixed `0<r_0<r_1<2` and fixed `Delta>0`,

\[
S_{k,a}
:=
\{n:\ L_k\le\log n<L_k+\Delta\},
\qquad
L_k=\frac{r_0}{a}+k\Delta,
\tag{2}
\]

for `0<=k<K=K(a)`, where

\[
K\asymp a^{-1}.
\tag{3}
\]

Write

\[
\theta_{k,a}
:=
\sum_{n\in S_{k,a}}\alpha_{n,a}.
\tag{4}
\]

Then `NB-189` gives uniformly in `k`

\[
\theta_{k,a}\asymp a\asymp K^{-1}.
\tag{5}
\]

For a finite complex Borel measure `mu` on height, put

\[
\widehat\mu(\lambda)
:=
\int_{\mathbb R}e^{-it\lambda}\,d\mu(t),
\tag{6}
\]

and use the `NB-190` coefficient error

\[
\mathcal E_{k,a}(\mu)
:=
\sum_{n\ge2}
\alpha_{n,a}
\left|
\widehat\mu(\lambda_n)
-
\frac{\mathbf 1_{S_{k,a}}(n)}{\theta_{k,a}}
\right|.
\tag{7}
\]

The inverse-mass theorem of `NB-190` says that, for every fixed `0<epsilon<1`,

\[
\mathcal E_{k,a}(\mu)\le\epsilon
\quad\Longrightarrow\quad
\|\mu\|_{TV}\gg_\epsilon K,
\tag{8}
\]

and its smooth-cutoff construction gives an unrestricted measure with the matching upper bound `O_epsilon(K)`.

## Claim 1: finite Euler phase sets have syndetic common returns

Let `Lambda` be any finite subset of `R` and, for `delta>0`, define

\[
\mathcal P_\Lambda(\delta)
:=
\left\{
\tau\in\mathbb R:
\max_{\lambda\in\Lambda}
|e^{-i\tau\lambda}-1|<\delta
\right\}.
\tag{9}
\]

Then

\[
\boxed{
\mathcal P_\Lambda(\delta)
\text{ is relatively dense in }\mathbb R.
}
\tag{10}
\]

Equivalently, there is a finite inclusion length `L(Lambda,delta)` such that every real interval of length at least `L(Lambda,delta)` contains one common `delta`-return.

This needs no rational-independence assumption. Define the continuous homomorphism

\[
\Phi(t)
:=
(e^{-it\lambda})_{\lambda\in\Lambda}
\in\mathbb T^{|\Lambda|}
\tag{11}
\]

and let `G` be the compact closure of `Phi(R)`. If `U` is the identity neighborhood corresponding to the inequalities in (9), the translates `Phi(s)U`, `s in R`, cover `G`. Compactness gives finitely many `s_1,...,s_J` whose translates already cover `G`.

Put

\[
s_-:=\min_j s_j,
\qquad
s_+:=\max_j s_j.
\]

For every real `x`, choose `j` with `Phi(x) in Phi(s_j)U`. Then

\[
\Phi(x-s_j)\in U,
\]

so `x-s_j in mathcal P_Lambda(delta)`. As `x-s_j` lies in `[x-s_+,x-s_-]`, every interval of length `s_+-s_-` contains a return. This proves (10).

This is exactly the finite-frequency content of classical Bohr almost periodicity. The point needed below is stronger than merely having arbitrarily large returns: the returns are syndetic once the frequency set is fixed.

## Claim 2: the sharp NB-190 band synthesizers can be made compact in height

Fix `0<epsilon<1`. Apply the `NB-190` smooth-cutoff upper construction at a smaller fixed error, say `epsilon/4`. For each `k` it gives a finite measure `mu^0_(k,a)` satisfying

\[
\mathcal E_{k,a}(\mu^0_{k,a})
\le\frac\epsilon4,
\qquad
\|\mu^0_{k,a}\|_{TV}
\ll_\epsilon K.
\tag{12}
\]

Because each `mu^0_(k,a)` is finite, it can be truncated in total variation to a compact interval. Since there are only finitely many `k` at fixed `a`, there is one radius `R_(a,epsilon)<infinity` and compactly supported measures `widetilde mu^0_(k,a)` with

\[
\operatorname{supp}\widetilde\mu^0_{k,a}
\subset[-R_{a,\epsilon},R_{a,\epsilon}],
\tag{13}
\]

\[
\|\mu^0_{k,a}-\widetilde\mu^0_{k,a}\|_{TV}
\le\frac\epsilon4,
\tag{14}
\]

and hence

\[
\boxed{
\mathcal E_{k,a}(\widetilde\mu^0_{k,a})
\le\frac\epsilon2,
\qquad
\|\widetilde\mu^0_{k,a}\|_{TV}
\ll_\epsilon K.
}
\tag{15}
\]

Indeed, (6) gives

\[
|\widehat\mu(\lambda)-\widehat\nu(\lambda)|
\le\|\mu-\nu\|_{TV},
\]

and the source weights in (1) sum to one, so total-variation truncation perturbs the coefficient error by at most the same amount.

Thus fixed-accuracy sharp synthesis already has a finite height footprint before any high-block translation is attempted.

## Claim 3: one common recurrent shift localizes all K bands in the same high block

Let

\[
\Lambda_a^{\rm band}
:=
\left\{
\lambda_n:
\alpha_{n,a}>0,
\ n\in\bigcup_{k=0}^{K-1}S_{k,a}
\right\}.
\tag{16}
\]

This set is finite for every fixed `a`. Choose

\[
0<\delta
\le
\frac{\epsilon}{2+\epsilon},
\tag{17}
\]

and let

\[
L_{a,\epsilon}
:=
L(\Lambda_a^{\rm band},\delta)
<\infty
\tag{18}
\]

be the inclusion length from Claim 1.

Suppose

\[
T-2R_{a,\epsilon}
\ge
L_{a,\epsilon}.
\tag{19}
\]

Then the interval

\[
[T+R_{a,\epsilon},\,2T-R_{a,\epsilon}]
\]

contains some `tau in mathcal P_(Lambda_a^band)(delta)`. Translate every compact seed by this **same** `tau`:

\[
\mu_{k,a,T}
:=
(t\mapsto t+\tau)_*\widetilde\mu^0_{k,a}.
\tag{20}
\]

Equation (19) gives

\[
\boxed{
\operatorname{supp}\mu_{k,a,T}
\subset[T,2T]
\quad(0\le k<K),
}
\tag{21}
\]

while translation preserves total variation,

\[
\|\mu_{k,a,T}\|_{TV}
=
\|\widetilde\mu^0_{k,a}\|_{TV}
\ll_\epsilon K.
\tag{22}
\]

Its Fourier--Stieltjes transform is

\[
\widehat\mu_{k,a,T}(\lambda)
=
e^{-i\tau\lambda}
\widehat{\widetilde\mu^0_{k,a}}(\lambda).
\tag{23}
\]

Outside the target band `S_(k,a)`, multiplying by the unit phase in (23) leaves the coefficient error **exactly unchanged**. Inside the band,

\[
\begin{aligned}
&\sum_{n\in S_{k,a}}\alpha_{n,a}
\left|
 e^{-i\tau\lambda_n}
 \widehat{\widetilde\mu^0_{k,a}}(\lambda_n)
 -\frac1{\theta_{k,a}}
\right|\\
&\le
\sum_{n\in S_{k,a}}\alpha_{n,a}
\left|
\widehat{\widetilde\mu^0_{k,a}}(\lambda_n)
-\frac1{\theta_{k,a}}
\right|
+
\delta
\sum_{n\in S_{k,a}}
\alpha_{n,a}
\left|
\widehat{\widetilde\mu^0_{k,a}}(\lambda_n)
\right|.
\end{aligned}
\tag{24}
\]

The last weighted amplitude is bounded by

\[
\sum_{n\in S_{k,a}}
\alpha_{n,a}
\left|
\widehat{\widetilde\mu^0_{k,a}}(\lambda_n)
\right|
\le
1+
\mathcal E_{k,a}(\widetilde\mu^0_{k,a})
\le1+\frac\epsilon2,
\tag{25}
\]

because the target row has weighted band mass exactly one. Combining (15), (17), (24) and (25) gives

\[
\boxed{
\mathcal E_{k,a}(\mu_{k,a,T})
\le\epsilon
\qquad(0\le k<K).
}
\tag{26}
\]

Therefore, for every fixed sufficiently small `a` and fixed `0<epsilon<1`, there is a finite threshold `T_0(a,epsilon)` such that **every** dyadic block `[T,2T]` with `T>=T_0(a,epsilon)` supports simultaneous synthesis of all `K asymp1/a` normalized Euler bands with

\[
\boxed{
\mathcal E_{k,a}(\mu_{k,a,T})\le\epsilon,
\qquad
\|\mu_{k,a,T}\|_{TV}\ll_\epsilon K.
}
\tag{27}
\]

Together with the universal lower bound (8), this is sharp:

\[
\boxed{
\inf_{\substack{
\operatorname{supp}\mu\subset[T,2T]\\
\mathcal E_{k,a}(\mu)\le\epsilon
}}
\|\mu\|_{TV}
\asymp_\epsilon K
\qquad
(T\ge T_0(a,\epsilon)).
}
\tag{28}
\]

The constants are uniform in `k`; the threshold is common to all bands because the recurrence was imposed on their finite union.

## Claim 4: the high-ordinate source-safe tariff remains exactly Theta(H_T)

Use the source-safe normalization from `NB-182` and `NB-190`,

\[
H_T
:=
\min\left\{a^{-1},\frac{\log T}{\log\log T}\right\},
\qquad
\kappa_T
:=
\frac{\mathcal W(a)}{C_BH_T}
\asymp_B
\frac1{aH_T}.
\tag{29}
\]

A unit source-normalized high-ordinate height sample equals `kappa_T` times the `mathcal W(a)`-normalized scalar sample. Hence the localized coefficient mask generated by `mu_(k,a,T)` in Claim 3 is generated from source-normalized samples by the measure

\[
\nu_{k,a,T}
:=
\kappa_T^{-1}\mu_{k,a,T}.
\tag{30}
\]

It has the same support `[T,2T]` and the same synthesis error, while

\[
\|\nu_{k,a,T}\|_{TV}
\ll
\frac K{\kappa_T}
\asymp_B
H_T.
\tag{31}
\]

But `NB-190` already proves for every high-block-supported source-normalized synthesizer with fixed error below one that

\[
\|\nu\|_{TV}
\gg H_T.
\tag{32}
\]

Therefore on all blocks beyond the recurrence threshold,

\[
\boxed{
\inf_{\substack{
\operatorname{supp}\nu\subset[T,2T]\\
\text{source-normalized band error}\le\epsilon
}}
\|\nu\|_{TV}
\asymp_{B,\epsilon}
H_T.
}
\tag{33}
\]

The same holds simultaneously for all `K` bands. Their localized RMS acquisition gain is consequently `Theta(H_T)`, not something larger forced merely by their high-block support.

## What this rules out, and what it does not

The result closes one tempting overinterpretation of the locality question left by `NB-190`. A theorem of the form

> moving the synthesis measure far out on the height axis necessarily adds an extra asymptotic total-variation factor

is false at fixed `a`. Finite Euler frequency sets are almost periodic, and once a dyadic block is longer than their common recurrence inclusion length, the sharp low-height synthesizer can be transplanted into that block at no additional order of variation.

This does **not** show that locality is irrelevant in the actual coupled limit. The quantities

\[
R_{a,\epsilon},
\qquad
L_{a,\epsilon}
\tag{34}
\]

may grow extremely rapidly as `a downarrow0`. The active logarithmic bands reach integers of size roughly `exp(r_1/a)` and involve a rapidly growing prime-log phase dimension. The proof gives finiteness and syndetic recurrence for each fixed `a`; it gives no useful bound placing `T_0(a,epsilon)` inside the arithmetic regime where `a=a_T` is being studied.

Accordingly, a genuine high-block obstruction must be **quantitative in both variables**. It would have to show that for the relevant coupling `a=a_T`, the block length `T` is still too short to contain a sufficiently accurate common almost period, or prove a stronger source-native restriction not invariant under the recurrent phase translation above. Merely requiring `supp mu subset [T,2T]` cannot supply such a theorem.

The result also does not address the destination-side caveat from `NB-189`: the Poisson-packed matched controls carrying the DFT code are still synthetic. Even perfectly localized acquisition says nothing by itself about whether the actual realized Nyman template range contains that geometry.

## Representation and prior-art audit

The recurrence mechanism is generic and classical. Finite trigonometric polynomials are Bohr almost periodic, and their epsilon-almost periods are relatively dense; modern Dirichlet-series treatments state the same fact for vertical restrictions of Dirichlet polynomials. A focused prior-art search included Ingo Schoolmann, *On Bohr's theorem for general Dirichlet series*, Math. Nachr. 293 (2020), 1591--1612, DOI `10.1002/mana.201800542`, which explicitly places Dirichlet polynomials on vertical lines in the almost-periodic framework. The compact-group proof of the only recurrence fact used here is given above, so no external theorem is load-bearing.

The line-specific content is the combination of that recurrence with the exact `NB-190` coefficient topology and sharp inverse-source-mass synthesis law. In particular: the seed probes are the true-amplitude normalized Euler bands from `NB-189`; fixed-accuracy compact truncation preserves their `Theta(K)` scalar-translate cost; one common phase return preserves all `K` coefficient masks simultaneously; and the high-ordinate normalization converts the localized `Theta(K)` Wiener cost into the sharp `Theta(H_T)` source-safe cost.

Searches over Bohr/Kronecker recurrence, vertical translates of Dirichlet series, Fourier--Stieltjes interpolation and Nyman--Beurling approximation did not locate this specific inverse-source-mass/high-block-localization comparison. That absence is not used as novelty evidence. `research/nyman_beurling/SOURCES.md` remains unchanged because the only external mathematics invoked for context is classical almost periodicity, while the proof needed here is self-contained.

## Self-adversarial audit

The most important limitation is the order of limits. Claim 3 is strong for **fixed `a` followed by `T -> infinity`**. It does not imply that a prescribed shrinking width `a_T` ever enters the recurrence regime. Replacing this with a statement uniform in `a` would require a quantitative inclusion-length theorem and is not justified here.

The recurrence acts only on the finite set of channels where the target band coefficient is nonzero. That is sufficient: outside the target band the coefficient error is measured against zero, and the height translation in (23) changes only phase, not magnitude. There is therefore no hidden requirement to recur all Euler frequencies.

The compact-support reduction is also essential. Translating the untruncated Schwartz measure from `NB-190` would not literally place its support inside `[T,2T]`. Claim 2 removes that loophole in total variation before recurrence is applied.

No assertion is made that the recurrence threshold is computationally accessible, polynomial in `1/a`, or even singly exponential in `1/a`. The finite active prime-log dimension makes the naive recurrence scale potentially enormous. This is why the finding is an obstruction to a **pure locality** argument, not a positive construction in the natural coupled high-ordinate regime.

Finally, the measures are allowed to be complex, exactly as in the Fourier--Stieltjes acquisition model of `NB-182`--`NB-190`. A positivity restriction on the height-side mixing measure would be a different architecture and is not tested here.

## Research consequence

`NB-190` identifies high-block localization as a possible extra tariff. `NB-191` shows that this tariff cannot depend only on how far the acquisition block sits from the origin: at every fixed width, Bohr recurrence eventually transports the sharp inverse-mass band synthesizers into every high dyadic block without additional order of total variation.

The next sharp discriminator is therefore the **common-return inclusion length**

\[
L_{a,\epsilon}
\]

for the growing union of Euler band frequencies. A useful negative theorem must compare `L_(a_T,epsilon)` with the available block length `T`; a useful positive theorem could instead produce sufficiently early common returns, perhaps using the prime-log structure rather than generic torus recurrence. Either direction is now a quantitative Diophantine problem coupled to the Poisson width, rather than an abstract time--frequency-locality slogan.

## Evidence ledger

**Internal load-bearing dependencies:** `NB-182` for the scalar Fourier--Stieltjes Euler acquisition model and source-safe high-ordinate normalization; `NB-189` for the `K asymp1/a` positive-mass Euler bands with `theta_(k,a) asymp a`; `NB-190` for the sharp unrestricted fixed-accuracy `Theta(K)` band synthesis and the `Omega(H_T)` source-normalized lower bound. `NB-006` is a line-local precedent for prime-log simultaneous recurrence, but its quantitative alias theorem is not needed for the proof above.

**External load-bearing dependencies:** none.

**Context-only prior art consulted:** classical Bohr/Kronecker almost periodicity and modern Dirichlet-series formulations such as Schoolmann (2020).