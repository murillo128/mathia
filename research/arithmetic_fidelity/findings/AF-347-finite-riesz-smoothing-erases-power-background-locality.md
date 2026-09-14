# AF-347 — finite Riesz smoothing erases power-background locality after order `k-1`

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `ZERO-SENSITIVE-SOURCE`, `SOURCE-COMPLEXITY-CONSERVATION`, `NO-NOVELTY-CLAIM`

## Claim

AF-344--AF-346 show that the weighted perfect-`k`-power background

\[
b_k(n):=
\begin{cases}
 k m^{k-1},&n=m^k\text{ with }m\ge2,\\
 0,&\text{otherwise},
\end{cases}
\qquad k\ge2,
\tag{1}
\]

is an arithmetic-faithful escape from raw sign/locality statistics: it has residue one at `s=1`, is holomorphic at the nontrivial zeta zeros, preserves the right-half-plane RH pole discriminator after subtraction from the prime layer, but carries order-`X` mass on only order `X^{1/k}` sites of amplitude order `X^{1-1/k}`.

A finite amount of classical Riesz smoothing can erase even that visible locality defect.

Fix integers `k>=2` and `r>=0`. Along the exact power cutoffs

\[
X=M^k,
\qquad M\to\infty,
\tag{2}
\]

define the order-`r` polynomially smoothed mass

\[
\mathcal R_{k,r}(X)
:=
\sum_{n\le X}b_k(n)
\left(1-\frac nX\right)^r.
\tag{3}
\]

Then

\[
\boxed{
\mathcal R_{k,r}(X)
=
\frac{X}{r+1}
+
O_{k,r}\!\left(
X^{\max\{1-(r+1)/k,\,0\}}
\right).
}
\tag{4}
\]

Thus every extra Riesz order removes one factor `X^{1/k}` from the polynomial discrepancy budget until no positive power remains. In particular,

\[
\boxed{
r\ge k-1
\quad\Longrightarrow\quad
\mathcal R_{k,r}(M^k)
=
\frac{M^k}{r+1}+O_{k,r}(1).
}
\tag{5}
\]

The comparison with a genuinely dense unit background is equally sharp. Put

\[
\mathcal U_r(X)
:=
\sum_{1\le n\le X}
\left(1-\frac nX\right)^r.
\tag{6}
\]

For fixed integer `r>=0`, classical power-sum/Euler--Maclaurin theory gives

\[
\mathcal U_r(X)=\frac{X}{r+1}+O_r(1).
\tag{7}
\]

Therefore

\[
\boxed{
r\ge k-1
\quad\Longrightarrow\quad
\mathcal R_{k,r}(M^k)-\mathcal U_r(M^k)=O_{k,r}(1).
}
\tag{8}
\]

This happens while the unsmoothed source geometries remain radically different:

\[
\#\operatorname{supp}(b_k)\cap[1,X]
\asymp X^{1/k},
\qquad
\max_{n\le X}b_k(n)\asymp X^{1-1/k},
\tag{9}
\]

and consecutive support locations near `X` are separated on scale

\[
(m+1)^k-m^k\asymp X^{1-1/k}.
\tag{10}
\]

So a destination that sees only sufficiently high fixed-order Riesz-smoothed mass can make this sparse, high-amplitude, zero-pole-blind background bounded-error indistinguishable from dense unit mass even though the raw locality profile is still extreme.

The relevant fidelity conclusion is:

\[
\boxed{
\text{a source locality resource must be consumed before, or quantitatively through, smoothing that can erase it.}
}
\tag{11}
\]

Merely proving that the raw source has sparse support, large gaps, or concentrated amplitude does not make that resource available to a downstream theorem whose first operation has already averaged those distinctions away.

## Derivation

### 1. Restore the harmless `m=1` term

It is convenient first to include `m=1` and write

\[
\widetilde{\mathcal R}_{k,r}(M^k)
:=
k\sum_{m=1}^{M}
 m^{k-1}
\left(1-\frac{m^k}{M^k}\right)^r.
\tag{12}
\]

The difference from `(3)` is exactly

\[
k\left(1-M^{-k}\right)^r,
\tag{13}
\]

which is `O_k(1)`. It is therefore enough to prove `(4)` for `(12)`.

Expanding the smoothing polynomial gives

\[
\widetilde{\mathcal R}_{k,r}(M^k)
=
k\sum_{j=0}^{r}
(-1)^j\binom rj M^{-kj}
\sum_{m=1}^{M}m^{k(j+1)-1}.
\tag{14}
\]

Set

\[
d_j:=k(j+1)-1.
\tag{15}
\]

### 2. The continuous main term is exactly `X/(r+1)`

For every integer `d>=1`, Faulhaber's formula has the form

\[
\sum_{m=1}^{M}m^d
=
\frac{M^{d+1}}{d+1}
+
\sum_{\ell=1}^{d}c_\ell(d)M^{d+1-\ell},
\tag{16}
\]

where `c_1(d)=1/2`, and for `ell>=2` one may take

\[
c_\ell(d)
=
\frac{B_\ell}{\ell!}
 d(d-1)\cdots(d-\ell+2).
\tag{17}
\]

For each fixed `ell`, `c_ell(d)` is a polynomial in `d` of degree at most `ell-1`.

Substituting only the leading term of `(16)` into `(14)` gives

\[
\begin{aligned}
&k\sum_{j=0}^{r}
(-1)^j\binom rj M^{-kj}
\frac{M^{k(j+1)}}{k(j+1)}\\
&\qquad =
M^k
\sum_{j=0}^{r}
\frac{(-1)^j}{j+1}\binom rj.
\end{aligned}
\tag{18}
\]

The elementary beta/binomial identity

\[
\sum_{j=0}^{r}
\frac{(-1)^j}{j+1}\binom rj
=
\int_0^1(1-t)^r\,dt
=
\frac1{r+1}
\tag{19}
\]

therefore produces exactly

\[
\frac{M^k}{r+1}.
\tag{20}
\]

Equivalently, this is the continuous reference integral

\[
\int_0^{M^k}
\left(1-\frac t{M^k}\right)^r dt
=
\frac{M^k}{r+1}.
\tag{21}
\]

### 3. Finite differences kill one source scale per smoothing order

Consider a correction level `ell<k`. Since

\[
d_j=k(j+1)-1\ge k-1\ge\ell,
\tag{22}
\]

that Faulhaber term is present for every `j=0,...,r`. After multiplication by the prefactor in `(14)`, its total contribution is

\[
k M^{k-\ell}
\sum_{j=0}^{r}
(-1)^j\binom rj c_\ell(d_j).
\tag{23}
\]

Because `d_j` is affine in `j` and `c_ell` has degree at most `ell-1`, the function

\[
j\longmapsto c_\ell(d_j)
\tag{24}
\]

is a polynomial of degree at most `ell-1`. The alternating binomial sum in `(23)` is, up to sign, its `r`-th finite difference. Hence

\[
\sum_{j=0}^{r}
(-1)^j\binom rj c_\ell(d_j)=0
\qquad\text{whenever }\ell\le r.
\tag{25}
\]

So all positive-power Faulhaber corrections with

\[
1\le\ell\le\min\{r,k-1\}
\tag{26}
\]

cancel identically.

If `r<k-1`, the first correction not forced to vanish is at `ell=r+1`, of size

\[
M^{k-r-1}.
\tag{27}
\]

Every later positive-power term is smaller. Thus

\[
\widetilde{\mathcal R}_{k,r}(M^k)
=
\frac{M^k}{r+1}
+O_{k,r}(M^{k-r-1}).
\tag{28}
\]

If instead `r>=k-1`, every correction carrying a positive power of `M` is annihilated by `(25)`. Terms with `ell>=k` have scale `M^{k-ell}=O(1)` or smaller after the normalization in `(14)`; terms absent from some low-degree power sums occur only in this nonpositive-power range and therefore do not affect the bound. Consequently

\[
\widetilde{\mathcal R}_{k,r}(M^k)
=
\frac{M^k}{r+1}+O_{k,r}(1).
\tag{29}
\]

Restoring `(13)` proves `(4)`--`(5)` because `X=M^k`.

The argument deliberately gives an upper bound rather than a claim of sharpness at every `(k,r)`. Bernoulli-number parity can cancel the first formally available correction and improve the actual exponent for particular pairs. What matters here is the uniform threshold: by order `k-1`, no positive-power discrepancy survives.

### 4. Dense unit mass has the same smoothed main term

Expanding `(6)` gives

\[
\mathcal U_r(X)
=
\sum_{j=0}^{r}
(-1)^j\binom rj X^{-j}
\sum_{n=1}^{X}n^j.
\tag{30}
\]

Applying the same power-sum expansion shows that its leading term is

\[
X\sum_{j=0}^{r}
\frac{(-1)^j}{j+1}\binom rj
=
\frac{X}{r+1},
\tag{31}
\]

while every remaining term is `O_r(1)`. This proves `(7)` and hence `(8)`.

## Relation to AF-344--AF-346

AF-344 exposed the perfect-power escape: the RH pole discriminator can survive while sign density collapses because order-`X` mass is concentrated onto only order `X^{1/k}` composite sites. AF-345 then identified prime-gap occupancy as the exact sign currency for nonnegative backgrounds, and AF-346 proved that for every fixed `k>=3` the same power family saturates the resulting gap-mass concentration exponent.

Those results show that raw sign count and one gap-mass moment are too weak. A natural response is to retain a stronger locality profile: support gaps, amplitude, local concentration, or a related norm. AF-347 supplies a separate warning about where that profile must live. A standard finite-order smoothing map can erase the polynomial visibility of the power background itself.

At order zero, `(4)` recovers the AF-344 scale

\[
\mathcal R_{k,0}(X)-X
=O_k(X^{1-1/k}).
\tag{32}
\]

After one smoothing order the guaranteed discrepancy loses a factor `X^{1/k}`; after `k-1` orders it is only bounded. Thus the locality resource exposed by AF-344 is not automatically conserved by downstream averaging.

This does not contradict AF-345 or AF-346. Their prime-gap occupancy and concentration laws are properties of the raw ordered source. Equation `(8)` instead shows that a particular later compression can cease to see those raw distinctions at polynomial scale.

## Exact controls and boundaries

### Exact-power cutoffs are part of the theorem

The clean cancellation theorem is stated on `X=M^k`. This is already enough to establish the fidelity obstruction: a downstream representation cannot claim a uniform polynomial separation of the power background from dense unit mass if that separation collapses to `O(1)` on an unbounded subsequence.

No claim is made here that the same bounded error holds uniformly for every real or integer cutoff `X`. Extending `(4)` away from exact powers requires tracking the moving terminal fractional cell and is a separate quantitative question.

### The smoothing order depends on the background family

For each fixed `k`, order `r=k-1` suffices. There is no claim that one fixed finite `r` hides the entire family as `k` varies. Indeed, `(4)` retains a positive-power error whenever `k>r+1` at the level of this bound.

### Smoothed mass fidelity is not raw-source fidelity

Equation `(8)` concerns one family of polynomially smoothed cumulative observables. It does not say the two coefficient sequences are close in `ell^p`, support geometry, pointwise amplitude, prime-gap occupancy, or any unsmoothed local metric. Those distinctions remain enormous by `(9)`--`(10)`.

The result is precisely that these distinctions can be unavailable after a particular compression.

### This is not an AF-338 growing-order theorem

AF-338 concerns strict sign regularity of the full Euler-log sampling matrix on escaping multiplicative windows. The present Riesz operator is a different compression. AF-347 neither extends AF-338 to growing sign order nor proves which locality norm its determinant constants consume.

Its role is diagnostic: a proposed stronger source certificate is useful only if the actual destination operation transports it rather than first applying an averaging map that destroys it.

### The result does not need prime-gap theory

Unlike AF-346, no Baker--Harman--Pintz input or statement about primes between consecutive powers is needed. The theorem holds already for `k=2`; the Legendre-conjecture boundary in AF-346 is irrelevant here because the smoothing calculation acts directly on the background coefficients.

### RH pole fidelity is inherited, not reproved

AF-344 already proves

\[
B_k(s)=k\bigl(\zeta(ks-k+1)-1\bigr),
\tag{33}
\]

with residue one at `s=1` and no poles at nontrivial zeta zeros, so subtraction from the prime layer preserves the same right-half-plane RH pole discriminator. AF-347 changes only the downstream observation applied to that already-audited source family.

## Prior art and novelty assessment

No novelty claim is made for the constituent mathematics.

- Riesz's typical means are classical. Hardy's *Divergent Series*, §4.16, records the weighted form `sum_{lambda_n<=omega}(1-lambda_n/omega)^kappa a_n` and its regularity; modern Dirichlet-series work continues to use typical Riesz means as a standard summation method.
- NIST DLMF §24.4(iii), especially Eq. 24.4.7, gives the classical Bernoulli-polynomial formula for finite sums of powers. DLMF §2.10(i) records the Euler--Maclaurin framework underlying the same expansion.
- The cancellation in `(25)` is the elementary fact that an `r`-th finite difference annihilates polynomials of degree below `r`.

A targeted search did not identify a standard theorem organized around this exact weighted perfect-power background and the threshold `r=k-1`. Search failure is not evidence of novelty. AF-347 is therefore classified as an exact Arithmetic Fidelity synthesis of classical Riesz smoothing, Faulhaber/Bernoulli power sums, and finite-difference cancellation.

## Consequence for Arithmetic Fidelity

AF-346 closes the hope that prime-gap concentration alone can strengthen the current sign-based source certificate: simple power backgrounds already saturate that exponent while preserving the RH pole discriminator. AF-347 closes a second shortcut: **raw locality is not a conserved resource merely because it is stronger than sign count.**

For the same counterexample family, sufficiently high but still finite polynomial smoothing turns a source with vanishing support density, diverging amplitudes, and diverging support gaps into a bounded-error match to dense unit mass along `X=M^k`.

The next viable source/destination theorem must therefore be explicitly smoothing-aware. It must either:

1. consume a locality/concentration quantity before the averaging step;
2. prove that the actual destination operator transports a declared locality norm with a quantitative modulus; or
3. retain a relational mark that the smoothing map cannot erase.

A source regularity theorem without a transport theorem is not enough: the relevant resource must survive in the category where the RH-sensitive destination theorem actually acts.
