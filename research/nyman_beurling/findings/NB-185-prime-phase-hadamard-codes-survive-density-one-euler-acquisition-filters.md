# NB-185 — Prime-phase Hadamard codes survive density-one Euler acquisition filters

**Date:** 2026-09-17  
**Status:** `LITERATURE+DERIVED + EXACT-FINITE-RANK + KRONECKER-WEYL + PRIME-PHASE + DENSITY-ONE-INTERSECTION + SOURCE-FIDELITY-BOUNDARY + NB-184-COROLLARY`.

`NB-184` removes the typical-height scalar acquisition bottleneck throughout the quadratic-divergence regime `T a_T^2 -> infinity`: on a density-one set of heights, the actual capped-Poisson seminorm of the local Euler kernel is `o(a_T^(-1/2))`, so the normalized scalar acquisition gain beats the generic `sqrt(N)` packing tariff. The remaining source-side question is coherent rank. One possible negative mechanism would be that arithmetic relations among the prime phases themselves prevent many independent phase patterns from occurring inside that good-height set.

They do not, at any fixed finite rank. Distinct prime logarithms generate an equidistributed flow on the full finite torus. Because the `NB-184` acquisition-good set has relative density one, it cannot remove any fixed positive-density phase box. Consequently every fixed finite Hadamard phase code is realized, to arbitrary prescribed accuracy, by heights that are simultaneously `NB-184`-good. For powers of two `N`, one can choose `N` such heights in one dyadic block so that the raw `N x N` prime-phase matrix has all singular values on the `sqrt(N)` scale.

This is deliberately a **boundary result**, not the missing source-complexity theorem. The phase boxes shrink exponentially with dimension and the argument gives no uniform hitting-time estimate as `N` grows. It also does not turn separately visible prime characters into a source-faithful acquisition; `NB-180`--`NB-182` already show why independently exposing weak Euler channels must be charged. What `NB-185` removes is the weaker obstruction: finite algebraic relations among ordinary prime phases cannot by themselves explain the failure to obtain coherent rank. Any genuine negative theorem must be quantitative in growing dimension, amplitudes/acquisition cost, or target coupling.

## Claim

Fix `B>0` and a width schedule `a_T` such that

\[
a_T\to0,
\qquad
T a_T^2\to\infty.
\tag{1}
\]

Let

\[
K_{a,t}(u)
:=-\frac{\zeta'}{\zeta}(1+a+i(t+u)),
\qquad |u|\le B,
\]

and let `mathcal H_{a,B}(t)` be the capped-Poisson source seminorm from `NB-184`,

\[
\mathcal H_{a,B}(t)
:=
\sup_{u\ne v}
\frac{|K_{a,t}(u)-K_{a,t}(v)|}
{\min\{1,|u-v|/a\}}.
\tag{2}
\]

For fixed `eta>0`, put

\[
G_T(\eta)
:=
\left\{
t\in[T,2T]:
\sqrt{a_T}\,\mathcal H_{a_T,B}(t)\le\eta
\right\}.
\tag{3}
\]

By `NB-184`,

\[
\frac{|G_T(\eta)|}{T}\to1.
\tag{4}
\]

Now fix an integer `m>=1`, distinct primes

\[
p_1,\ldots,p_m,
\]

and a Borel set `U subset (S^1)^m` whose boundary has Haar measure zero. Define the prime-phase hitting set

\[
E_T(U)
:=
\left\{
t\in[T,2T]:
(e^{-it\log p_1},\ldots,e^{-it\log p_m})\in U
\right\}.
\tag{5}
\]

Then

\[
\boxed{
\frac{|E_T(U)|}{T}
\longrightarrow
\mu_m(U),
}
\tag{6}
\]

where `mu_m` is normalized Haar measure on `(S^1)^m`. Moreover the same asymptotic survives the `NB-184` filter:

\[
\boxed{
\frac{|E_T(U)\cap G_T(\eta)|}{T}
\longrightarrow
\mu_m(U).
}
\tag{7}
\]

In particular, let `N=2^r`, let `H_N in {+1,-1}^{N x N}` be the Sylvester Hadamard matrix, and fix distinct primes `p_1,...,p_N`. For every fixed `eta>0` and `delta>0`, all sufficiently large `T` admit distinct heights

\[
t_1,\ldots,t_N\in G_T(\eta)
\tag{8}
\]

such that

\[
\boxed{
\max_{1\le i,j\le N}
\left|
e^{-it_i\log p_j}-(H_N)_{ij}
\right|
<\delta.
}
\tag{9}
\]

Let

\[
P_{ij}:=e^{-it_i\log p_j}.
\tag{10}
\]

Since every singular value of `H_N` equals `sqrt(N)`, one has

\[
\boxed{
s_j(P)
\ge
\sqrt N-N\delta,
\qquad 1\le j\le N.
}
\tag{11}
\]

Thus choosing

\[
\delta\le\frac1{2\sqrt N}
\tag{12}
\]

gives

\[
\boxed{
s_j(P)\ge\frac12\sqrt N
\qquad(1\le j\le N).}
\tag{13}
\]

So for every fixed finite Hadamard rank, Hadamard-scale prime-phase coherence occurs inside the density-one set where the actual local Euler acquisition cost is already supercritical in the sense of `NB-184`.

There is also an unbounded but nonquantitative diagonal consequence. Given any sequence `N_r=2^r`, tolerances `delta_r<=1/(2 sqrt(N_r))`, and acquisition tolerances `eta_r -> 0`, one may choose an increasing sequence `T_r -> infinity` and widths satisfying (1) such that each dyadic block `[T_r,2T_r]` contains `N_r` heights satisfying (8)--(13) with `(N,delta,eta)=(N_r,delta_r,eta_r)`. Hence there is no **qualitative finite-rank ceiling** coming from prime-phase algebra. The unresolved issue is quantitative growth: nothing here controls how large `T_r` must be relative to `N_r` or `a_{T_r}^{-1}`.

## Derivation

### 1. Distinct prime logarithms have no nontrivial integer relation

Let `k=(k_1,...,k_m) in Z^m` be nonzero. If

\[
\sum_{j=1}^m k_j\log p_j=0,
\tag{14}
\]

then exponentiating gives

\[
\prod_{j=1}^m p_j^{k_j}=1.
\tag{15}
\]

After moving negative exponents to the other side, unique factorization forces every `k_j=0`, a contradiction. Therefore

\[
\lambda_k
:=
\sum_{j=1}^m k_j\log p_j
\ne0
\qquad(k\ne0).
\tag{16}
\]

This is the only arithmetic input needed for the phase-flow statement.

### 2. The continuous prime-phase flow is equidistributed on every long dyadic block

For a nonzero character `k in Z^m`,

\[
\frac1T
\int_T^{2T}
\exp\left(
-it\sum_{j=1}^m k_j\log p_j
\right)dt
=
\frac{e^{-2iT\lambda_k}-e^{-iT\lambda_k}}
{-iT\lambda_k}.
\tag{17}
\]

Hence

\[
\left|
\frac1T
\int_T^{2T}e^{-it\lambda_k}dt
\right|
\le
\frac2{T|\lambda_k|}
\to0.
\tag{18}
\]

The zero character has average one. The usual trigonometric-polynomial approximation of continuous functions on the finite torus now gives

\[
\frac1T
\int_T^{2T}
F(e^{-it\log p_1},...,e^{-it\log p_m})dt
\to
\int_{(S^1)^m}F\,d\mu_m
\tag{19}
\]

for every continuous `F`. Approximating the indicator of any boundary-null Borel set from above and below proves (6).

This is exactly the classical Kronecker--Weyl/Bohr phase mechanism, written here in the continuous-height form needed by the present line. `NB-006` already used the complementary finite-recurrence side of the same prime-log geometry; the new content is not the torus theorem itself.

### 3. A density-one acquisition filter cannot erase a fixed phase box

Write

\[
B_T(\eta):=[T,2T]\setminus G_T(\eta).
\]

Equation (4) says

\[
|B_T(\eta)|=o(T).
\tag{20}
\]

For every fixed boundary-null `U`,

\[
|E_T(U)|-|B_T(\eta)|
\le
|E_T(U)\cap G_T(\eta)|
\le
|E_T(U)|.
\tag{21}
\]

Divide by `T` and use (6) and (20). Both bounds converge to `mu_m(U)`, proving (7).

This step is where `NB-184` changes the source-side interpretation. Prime-phase recurrence by itself says that finite phase targets are reachable. Equation (7) says they remain reachable even after requiring the **same height** to lie in the set where the actual local Euler kernel has cheap capped-Poisson acquisition.

### 4. Hadamard rows are positive-measure phase targets

For the `i`th Hadamard row define

\[
U_i(\delta)
:=
\left\{
(z_1,...,z_N)\in(S^1)^N:
\max_j|z_j-(H_N)_{ij}|<\delta
\right\}.
\tag{22}
\]

For every `delta>0`, this is a nonempty open set with positive Haar measure; its boundary has measure zero. By (7), for each fixed row `i`,

\[
\frac{|E_T(U_i(\delta))\cap G_T(\eta)|}{T}
\to
\mu_N(U_i(\delta))>0.
\tag{23}
\]

There are only finitely many rows, so for all sufficiently large `T` every one of the `N` intersections is nonempty. When `delta<1`, boxes around distinct `+/-1` Hadamard rows are disjoint in at least one coordinate, so the selected heights may automatically be taken distinct; alternatively, positive measure allows distinct choices directly. This proves (8)--(9).

### 5. Entrywise phase accuracy preserves Hadamard-scale singular values

Write

\[
P=H_N+R.
\]

Equation (9) gives

\[
\|R\|_{op}
\le
\|R\|_F
<
N\delta.
\tag{24}
\]

Since

\[
H_NH_N^*=NI_N,
\]

all singular values of `H_N` are exactly `sqrt(N)`. Singular-value perturbation therefore gives

\[
s_j(P)
\ge
s_j(H_N)-\|R\|_{op}
\ge
\sqrt N-N\delta,
\tag{25}
\]

which is (11), and (12) yields (13).

For fixed `N`, multiplying column `j` by the genuine nonzero prime Euler amplitude

\[
\frac{\log p_j}{p_j^{1+a_T}}
\]

also preserves exact rank for all `T`. This observation must not be overread: it does **not** make the prime channels separately available at bounded source cost. The quantitative decay and unevenness of those amplitudes are precisely the acquisition/conditioning issue isolated by `NB-180`--`NB-182`.

## Representation audit

The theorem concerns three different objects that must remain separate.

First, the phase flow

\[
t\mapsto(e^{-it\log p_j})_{j\le N}
\]

is genuine source data: these are actual Euler phases. Second, the `NB-184` good set is also source-faithful: it is defined by the actual capped-Poisson seminorm of `-zeta'/zeta` at that height. Their intersection is therefore meaningful and does not arise from an artificial coordinate normalization.

Third, however, the matrix `P` is only a **phase-accessibility matrix**. Its columns are not individually normalized source probes, and its Hadamard singular values are not an `NB-178` complexity certificate. Turning phase accessibility into such a certificate would require an acquisition map that exposes enough of these channels while retaining their Euler amplitudes or paying the correct Wiener/Hilbert tariff. That is exactly the boundary established by `NB-180`--`NB-182`.

Thus the representation-safe conclusion is negative and precise: finite prime-phase algebra does not forbid coherent rank. It is not the stronger claim that the source already supplies the required rank at bounded cost.

## Prior-art boundary

The finite-dimensional phase statement is classical. Kronecker--Weyl/Bohr almost periodicity uses rational independence of prime logarithms to obtain dense or equidistributed prime phases, and this mechanism is standard background in the universality theory of the Riemann zeta function. Modern effective universality results, such as Lamzouri--Lester--Radziwill, *An effective universality theorem for the Riemann zeta function*, Comment. Math. Helv. 93 (2018), 709--736, DOI `10.4171/CMH/448`, sit far beyond the elementary fixed-finite phase assertion used here.

No such external theorem is load-bearing in the derivation: (14)--(19) prove the exact equidistribution statement directly, and the only source-specific second ingredient is the already persisted density-one theorem `NB-184`. Therefore no new durable dependency is needed in `SOURCES.md`.

A targeted prior-art search did not identify the line-specific intersection statement (7) for the capped-Poisson seminorm, but no novelty claim is made for the underlying torus dynamics. The durable contribution here is to locate the boundary of the post-`NB-184` coherent-rank problem: **phase reachability is not the finite-dimensional obstruction**.

## Self-adversarial review and limits

### Fixed dimension is essential to the argument

For fixed `N` and `delta`, every Hadamard row box has a positive constant Haar measure, so an `o(T)` bad set cannot erase it. When `N=N(T)` grows, however, the phase-box measure can be exponentially or worse small. The `NB-184` estimate only says that the bad relative measure tends to zero; it does not compare that decay with `mu_N(U_i(delta))`.

Therefore (7) cannot be promoted to a growing-rank theorem by substituting `N=N(T)`. The diagonal corollary merely chooses `T` after fixing each finite rank and may require enormous, uncontrolled heights.

### No effective simultaneous hitting time is obtained

Equation (18) is effective for each fixed Fourier character, but passing from it to an indicator of a tiny `N`-dimensional box without a quantitative Diophantine/discrepancy analysis loses the dependence on `N` and `delta`. A useful growing-rank result would need a discrepancy or large-sieve statement strong enough to compare the phase-box hitting density with the explicit exceptional-density bound in `NB-184`.

### The selected heights are not zero ordinates or Nyman target data

The heights in (8) are chosen from the continuum after seeing the desired phase row. Nothing says that actual zeta zeros, a prescribed zero packet, or a source-selected Nyman approximation occurs at those heights. This finding does not alter the global target-conditioning boundary in the line.

### Raw phase rank is not bounded-cost source rank

Hadamard singular values for `P` do not contradict `NB-181` or `NB-182`. Those findings charge the acquisition needed to turn Euler information into scalar probes. `NB-185` keeps the true phases but does not pay for separately reading them. The result therefore rules out an algebraic phase obstruction, not the amplitude/acquisition obstruction.

## Updated frontier

After `NB-184`, typical scalar Euler exposure is already affordable throughout `T a^2 -> infinity`. `NB-185` now removes a second qualitative excuse: any fixed finite collection of ordinary prime phases can realize arbitrary open phase patterns, including Hadamard rows, **inside that same acquisition-good set**.

The coherent-rank frontier is consequently quantitative. A positive route must control a growing number `N=N(a,T)` of source-natural phase directions on a common set of heights while retaining actual Euler amplitudes and acquisition cost. A negative route can no longer appeal merely to finite rational dependence of prime phases; it must prove that the hitting/discrepancy scale, amplitude decay, scalar aggregation, or target coupling prevents the required `N~1/a` rank before the quadratic acquisition boundary is reached.