# MC-086 — Source-natural initial reciprocal slabs remain Mertens-equivalent at reconstruction resolution

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

The source-natural physical-space escape left open by `MC-084` and `MC-085` has the same power-resolution barrier as the initial Fourier truncation.

Retain the Huxley--Watt notation

\[
M(N)=\sum_{n\le N}\mu(n),
\qquad
H_1(N)=\sum_{n\le N}\frac{\mu(n)}n,
\]

and the coarse term

\[
C_N:=N^2H_1(N)^2-\frac12M(N)^2.
\tag{1}
\]

For `1<=k<=N-1`, let

\[
\mathcal A_k
:=
\left\{(m,n):m,n\le N,\ \frac{N^2}{k+1}<mn\le\frac{N^2}{k}\right\},
\tag{2}
\]

and write the exact Huxley--Watt sawtooth annulus as in `MC-084`,

\[
W_N
=
\sum_{k=1}^{N-1}
\left(\left(k+\frac12\right)U_k-N^2V_k\right),
\tag{3}
\]

where

\[
U_k:=\sum_{(m,n)\in\mathcal A_k}\mu(m)\mu(n),
\qquad
V_k:=\sum_{(m,n)\in\mathcal A_k}\frac{\mu(m)\mu(n)}{mn}.
\tag{4}
\]

For an integer `2<=K<=N`, keep only the **initial reciprocal slabs**

\[
W_{N,<K}
:=
\sum_{1\le k<K}
\left(\left(k+\frac12\right)U_k-N^2V_k\right)
\tag{5}
\]

and define the source-coupled partial residual

\[
\boxed{S_{N,K}:=C_N+W_{N,<K}.}
\tag{6}
\]

The omitted tail

\[
T_{N,K}:=W_N-W_{N,<K}
\tag{7}
\]

is supported exactly on

\[
\{(m,n):m,n\le N,\ N<mn\le N^2/K\}.
\tag{8}
\]

Since the source sawtooth `z(x)=floor(x)+1/2-x` satisfies `|z(x)|<=1/2`, elementary hyperbola counting gives the source-generic bound

\[
\boxed{
|T_{N,K}|
\ll
\frac{N^2(1+\log K)}{K}.
}
\tag{9}
\]

Combining this with the exact scale-doubling identity and the `O(N log N)` low-product interior `I_N` from `MC-084` yields

\[
\boxed{
S_{N,K}
=
2M(N)-M(N^2)-I_N-T_{N,K}.
}
\tag{10}
\]

Consequently, fix `1/2<beta<1` and choose

\[
K=\lfloor N^\theta\rfloor,
\qquad
2-2\beta<\theta<1.
\tag{11}
\]

Then the truncation is genuinely proper, while

\[
T_{N,K}=o(N^{2\beta}),
\qquad
I_N=o(N^{2\beta}),
\tag{12}
\]

and therefore

\[
\boxed{
S_{N,K}=O(N^{2\beta})
\quad\Longleftrightarrow\quad
M(x)=O(x^\beta).
}
\tag{13}
\]

The RH epsilon-family is likewise unchanged by a proper physical-space cutoff. For every fixed `0<epsilon<1`, put

\[
K_\varepsilon(N)=\left\lfloor N^{1-\varepsilon/2}\right\rfloor.
\tag{14}
\]

Then

\[
S_{N,K_\varepsilon(N)}
=O_\varepsilon(N^{1+\varepsilon})
\quad\text{for every }0<\varepsilon<1
\tag{15}
\]

is equivalent to the usual RH consequence

\[
M(x)=O_\delta(x^{1/2+\delta})
\quad\text{for every }\delta>0.
\tag{16}
\]

Thus merely replacing the Fourier cutoff by the source-natural reciprocal-floor slabs does not create a cheaper coupled target. Once enough initial slabs are retained that the omitted physical tail is below the desired power scale by the generic absolute estimate (9), the retained coarse-plus-slab statistic is again an approximate coordinate system for the doubled Mertens target.

The obstruction is deliberately narrow. It does not rule out selective or noninitial slab families, arithmetic cancellation in the omitted tail beyond (9), a bilinear decomposition that estimates retained and omitted pieces jointly before absolute values, or a source-forced statistic that omits information in a way not recoverable by a generic tail estimate.

## 1. Exact support of the omitted reciprocal slabs

On `\mathcal A_k`, one has

\[
\left\lfloor\frac{N^2}{mn}\right\rfloor=k,
\]

so the slabs in (2) partition the annulus `N<mn<=N^2`. Their union for `K<=k<=N-1` is

\[
\frac{N^2}{N}<mn\le\frac{N^2}{K},
\]

which is exactly (8). Therefore

\[
T_{N,K}
=
\sum_{\substack{m,n\le N\\N<mn\le N^2/K}}
\mu(m)\mu(n)
 z\!\left(\frac{N^2}{mn}\right).
\tag{17}
\]

This identity matters because it identifies the cost of throwing away the high-index floor slabs without invoking Fourier approximation. The omitted information is simply a hyperbolic product region near the lower edge of the annulus.

## 2. Generic hyperbola bound for the physical tail

Set

\[
X:=\frac{N^2}{K}.
\tag{18}
\]

Using `|mu(m)mu(n)z(N^2/(mn))|<=1/2` and enlarging (17) to all pairs with `mn<=X`,

\[
|T_{N,K}|
\le
\frac12
\#\{(m,n):m,n\le N,\ mn\le X\}.
\tag{19}
\]

Split the first coordinate at `X/N=N/K`. For `m<=N/K`, there are at most `N` choices of `n`, so this range contributes `O(N^2/K)`. For `N/K<m<=N`,

\[
\#\{n\le N:mn\le X\}
\le \frac Xm,
\]

and hence

\[
\sum_{N/K<m\le N}\frac Xm
\ll
\frac{N^2}{K}(1+\log K).
\tag{20}
\]

Equations (19)--(20) prove (9). No Möbius cancellation, zero-free region, Fourier estimate, or distribution theorem is used.

The power content of (9) is the same as the Huxley--Watt Fourier-tail budget audited in `MC-085`: if `K=N^theta`, then the generic physical tail has scale

\[
N^{2-\theta+o(1)}.
\tag{21}
\]

After square interpolation, this corresponds to the Mertens exponent `1-theta/2`. The logarithmic factors differ between representations, but the reconstruction threshold in powers of `N` does not.

## 3. Reverse recovery at every supercritical exponent

`MC-084` gives the exact full source-coupled identity

\[
C_N+W_N
=
2M(N)-M(N^2)-I_N,
\qquad
I_N=O(N\log N).
\tag{22}
\]

Subtract (7) and use (6) to obtain (10).

Assume first that `M(x)=O(x^beta)` with `1/2<beta<1`. Under (11), equations (9) and (12) give

\[
S_{N,K}
=
O(N^\beta)+O(N^{2\beta})+o(N^{2\beta})
=
O(N^{2\beta}).
\tag{23}
\]

Conversely suppose `S_{N,K}=O(N^{2\beta})`. Equation (10), the trivial bound `|M(N)|<=N`, (9), and `I_N=O(N log N)` yield

\[
M(N^2)=O(N^{2\beta}).
\tag{24}
\]

For arbitrary real `x`, let `N=floor(sqrt(x))`. Since every increment of `M` has absolute value at most one,

\[
|M(x)-M(N^2)|\le x-N^2\le 2N+1.
\tag{25}
\]

Because `beta>1/2`, (24)--(25) give `M(x)=O(x^beta)`. This proves (13) without assuming any prior Mertens power saving.

## 4. Proper slabs still carry the RH epsilon-family

For the cutoff (14), equation (9) gives

\[
T_{N,K_\varepsilon}
=O_\varepsilon\!\left(
N^{1+\varepsilon/2}\log N
\right)
=O_\varepsilon(N^{1+\varepsilon}).
\tag{26}
\]

The interior `I_N=O(N log N)` is also within the target scale.

If RH's Mertens family (16) holds, apply it with exponent `1/2+epsilon/2` in (10) to obtain (15). Conversely, (15), (10), (26), and `|M(N)|<=N` give

\[
M(N^2)=O_\varepsilon(N^{1+\varepsilon}).
\tag{27}
\]

Square interpolation then yields

\[
M(x)=O_\varepsilon(x^{1/2+\varepsilon/2}).
\tag{28}
\]

Given any `0<delta<1/2`, choose `epsilon=2delta`; larger `delta` are already covered by the trivial bound. Hence (15) and (16) are equivalent as families.

The important point is that `K_epsilon(N)<N` for every fixed positive epsilon: the physical slab family remains strictly partial. Yet as the requested exponent approaches `1/2`, the cutoff exponent approaches one, exactly as in the Fourier audit of `MC-085`.

## 5. Prior art and novelty boundary

The parent scale-doubling identity, the matrix decomposition with `z(x)=-psi(x)`, and the exact sawtooth residual are from M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the Möbius function* (2018), recorded as `MC-S24`. `MC-084` already derived the reciprocal-floor slab representation (3) from that source object.

The lattice-point estimate (19)--(20) is an elementary Dirichlet-hyperbola count. A targeted literature check around the Huxley--Watt sawtooth formulation and reciprocal floor decomposition found the source identity and standard hyperbola language, but no basis for a novelty claim about the present truncation threshold. **No novelty claim is made.**

The durable line-specific content is the reverse-recovery audit demanded by the current accepted annular clue: the most direct proper physical-space truncation has the same power-level reconstruction barrier as the proper initial Fourier truncation. This is a structural obstruction for this route, not a new classical theorem about Möbius sums.

## 6. Boundaries and decisive continuation

This result does **not** estimate any individual `U_k` or `V_k` nontrivially and does not prove that their Möbius signs fail to cancel. It only shows that discarding the high-index tail by the generic absolute estimate (9) makes the remaining coupled statistic target-equivalent as soon as the discarded part is below the target scale.

Accordingly, a slab-based continuation survives only if it supplies genuinely new arithmetic information. Viable possibilities include:

- a signed estimate for `T_{N,K}` substantially stronger than (9), proved from hypotheses independently weaker than Mertens at the desired exponent;
- a selective or noninitial slab family whose complement is independently cheaper than the full target information;
- a bilinear relation that controls retained and omitted slab contributions jointly before triangle inequalities are applied;
- a source-forced under-resolved statistic that yields a strict contraction without allowing reconstruction of `M(N^2)` through a generic tail estimate.

A candidate is killed if its only bridge from the partial statistic to the full Huxley--Watt residual is (9) at a cutoff chosen precisely so that the tail lies below the desired Mertens scale.

The exact claims admit finite checks: the slab union in (8), the tail identity (17), the source-coupled recovery (10), and the pair-count bound (19) can all be verified by direct enumeration for finite `N,K`. A failure of any exact identity would invalidate the result; improving (9) by genuine Möbius cancellation would lie outside its negative conclusion.

## Consequence for the research line

`MC-085` closed the source-natural initial Fourier family at reconstruction resolution. `MC-086` closes the analogous source-natural initial reciprocal-floor slab family: the two representations have the same power cutoff threshold `theta>2-2beta` for recovering a target exponent `beta>1/2` from generic remainder control.

The annular frontier is therefore narrower. A useful residual must be genuinely under-resolved **and** carry an independently controlled signed interaction; merely choosing a proper source-natural truncation and paying a generic complement bound does not reduce the information burden.