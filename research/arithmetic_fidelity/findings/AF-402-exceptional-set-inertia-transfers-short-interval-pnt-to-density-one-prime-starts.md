# AF-402 — Exceptional-set inertia transfers short-interval PNT to density-one prime starts

## Status

`LITERATURE+DERIVED` · `EXACT-DERIVED` · `ARITHMETIC-FIDELITY` · `EXCEPTIONAL-SET` · `SPARSE-SAMPLING` · `MOVING-SCALE` · `QUANTITATIVE-RECOVERY` · `NO-NOVELTY-CLAIM`

## Claim

AF-401 deliberately did not use the almost-all short-interval prime number theorem, because a Lebesgue-density-zero exceptional set of real starting points could in principle still contain every prime starting point. The missing transfer is supplied by an **inertia plus packing** argument: failure of the short-interval PNT at one starting point persists on a real interval of controlled width, while prime starting points cannot pack into such intervals faster than Brun--Titchmarsh permits.

For fixed `0<theta<1`, put

\[
A_\theta(x)=\psi(x+x^\theta)-\psi(x)-x^\theta
\]

and, for fixed `delta>0`, let

\[
E_\delta(X,\theta)
=\{x\in[X,2X]: |A_\theta(x)|\ge \delta x^\theta\}.
\tag{1}
\]

Then for every fixed `theta` and `delta` there is a fixed `delta'>0` such that

\[
\#\{p\in[X,2X]: p\text{ prime},\ |A_\theta(p)|\ge \delta p^\theta\}
\ll_{\theta,\delta}
\frac{|E_{\delta'}(X,\theta)|+o(X)}{\log X}.
\tag{2}
\]

Here the harmless `o(X)` term only absorbs endpoint bookkeeping; equivalently one may define the exceptional set on a fixed enlarged dyadic interval and omit it.

Consequently, whenever the short-interval PNT holds for almost all real starts at exponent `theta`, it also holds for a **relative-density-one set of prime starts**:

\[
\psi(p+p^\theta)-\psi(p)\sim p^\theta
\tag{3}
\]

for all but `o(X/log X)` primes `p` in `[X,2X]`.

Guth--Maynard's zero-density estimates imply, in the formulation recorded by Gafni--Tao, that the short-interval PNT holds for almost all real starts for every

\[
\theta>\frac{2}{15}.
\tag{4}
\]

Thus `(3)` holds at density-one prime starts throughout the same open range `theta>2/15`.

For the AF-399--AF-401 prime-log locality observable

\[
B_N(h)=\pi(e^h p_N)-N,
\tag{5}
\]

fix

\[
0<\beta<\frac{13}{15},
\qquad h_N=p_N^{-\beta}.
\tag{6}
\]

Then, in relative natural density among prime indices,

\[
\boxed{
B_N(p_N^{-\beta})\sim Np_N^{-\beta}.
}
\tag{7}
\]

More explicitly, for every fixed `eta>0`,

\[
\frac1M\#\left\{N\le M:
\left|\frac{B_N(p_N^{-\beta})}{Np_N^{-\beta}}-1\right|>\eta
\right\}\longrightarrow0.
\tag{8}
\]

Hence AF-401's **all-starting-primes** conversion range `beta<13/30` has a strictly deeper **density-one-prime-starts** counterpart `beta<13/15`. At the lower edge `theta=2/15+epsilon`, equivalently `beta=13/15-epsilon`, the expected successor breadth is

\[
B_N(h_N)=N^{2/15+\varepsilon+o(1)}
\tag{9}
\]

up to the corresponding logarithmic factor. The endpoint `2/15` itself is not asserted.

## Inertia-to-sparse-sampling lemma

The transfer mechanism is more general than the prime application. Let `S` be a discrete sample set in an interval and `E` a measurable exceptional set. Suppose every bad sample `s in S` carries an interval `I_s subset E` of length at least `L`, and suppose every interval of length `L` contains at most `Q` sample points. Then

\[
\boxed{
\#\{\text{bad samples}\}\le \frac{Q}{L}|E|.
}
\tag{10}
\]

Indeed,

\[
\#\{\text{bad samples}\}\,L
\le \sum_s |I_s|
=\int \sum_s 1_{I_s}(x)\,dx
\le Q|E|.
\tag{11}
\]

This isolates the two resources required to transfer an almost-everywhere statement to a sparse prescribed sampling set:

1. **inertia**: point failure must occupy positive ambient measure rather than live only at the sampled point;
2. **packing control**: the sample set cannot concentrate too strongly on one inertia interval.

Without either ingredient, ambient density zero alone gives no sparse-sample conclusion.

## Short-interval inertia at a bad prime start

Fix a bad prime `p in [X,2X]`, so

\[
|A_\theta(p)|\ge \delta p^\theta.
\tag{12}
\]

Choose

\[
L=c_{\theta,\delta}\frac{X^\theta}{\log X}
\tag{13}
\]

with a sufficiently small fixed positive constant `c_{theta,delta}`. If `|x-p|<=L`, the lower endpoint of the von Mangoldt sum moves by at most `L`, while

\[
|(x+x^\theta)-(p+p^\theta)|\le (1+o(1))L.
\tag{14}
\]

Since `Lambda(n)<=log(3X)` throughout the relevant range, changing either endpoint across distance `O(L)` changes the sum by at most

\[
O(L\log X)=O(c_{\theta,\delta}X^\theta).
\tag{15}
\]

Also

\[
|x^\theta-p^\theta|
\ll X^{\theta-1}L=o(X^\theta).
\tag{16}
\]

Taking `c_{theta,delta}` sufficiently small therefore gives a fixed `delta'=delta'(theta,delta)>0` such that every `x` in a one-sided interval of length `L` pointing into `[X,2X]` satisfies

\[
|A_\theta(x)|\ge \delta' x^\theta.
\tag{17}
\]

Thus every bad prime start carries an inertia interval `I_p subset E_{delta'}(X,theta)` of length comparable to `X^theta/log X`.

This `1/log X` loss in inertia width is natural at this level of argument: shifting an endpoint across one integer can change a von Mangoldt sum by `O(log X)`, so a worst-case deterministic Lipschitz bound must budget that jump size.

## Packing the prime starts

For the same

\[
L\asymp\frac{X^\theta}{\log X},
\]

Brun--Titchmarsh gives, uniformly for intervals of length `L`,

\[
\#\{p\in[t,t+L]:p\text{ prime}\}
\ll_\theta \frac{L}{\log L}
\asymp_\theta \frac{L}{\log X}.
\tag{18}
\]

Applying `(10)` with

\[
Q\ll_\theta\frac{L}{\log X}
\tag{19}
\]

gives `(2)`. In particular, if

\[
|E_{\delta'}(X,\theta)|=o(X),
\tag{20}
\]

then the number of bad prime starts is

\[
o\!\left(\frac{X}{\log X}\right),
\tag{21}
\]

which is negligible relative to the number of primes in `[X,2X]`.

More generally, any quantitative exceptional-measure estimate

\[
|E_{\delta'}(X,\theta)|\ll X^{\mu+o(1)}
\tag{22}
\]

immediately yields

\[
\#\{\text{bad prime starts in }[X,2X]\}
\ll \frac{X^{\mu+o(1)}}{\log X}.
\tag{23}
\]

The exact exceptional-set exponents can therefore be transported to prime starts without pretending that a measure estimate alone controls a sparse set.

## From von Mangoldt mass to prime count

For fixed `theta>0`, prime powers make a negligible contribution on an interval of length `p^theta`. For each `k>=2`, the number of `k`-th powers in such an interval is

\[
O\!\left(p^{\theta-1+1/k}+1\right),
\]

so after weighting by `Lambda`, the total contribution of all proper prime powers is `o(p^theta)`. Hence `(3)` implies

\[
\vartheta(p+p^\theta)-\vartheta(p)\sim p^\theta,
\tag{24}
\]

and since every prime in the interval has logarithm `log p+o(1)`,

\[
\pi(p+p^\theta)-\pi(p)
\sim \frac{p^\theta}{\log p}
\tag{25}
\]

at the same density-one set of prime starts.

## Translation to the shrinking logarithmic wall

For `(6)`, set

\[
\theta=1-\beta>\frac{2}{15}.
\tag{26}
\]

The exact AF interval in `(5)` has additive length

\[
\Delta_p=p(e^{p^{-\beta}}-1)
=p^{1-\beta}(1+O(p^{-\beta}))
=p^\theta(1+o(1)).
\tag{27}
\]

The difference between `Delta_p` and `p^theta` is `O(p^{1-2beta})`; even with the trivial von Mangoldt bound its effect is

\[
O\!\left((p^{1-2\beta}+1)\log p\right)=o(p^{1-\beta}).
\tag{28}
\]

Therefore `(25)` remains valid with upper endpoint `e^{p^{-beta}}p`. At `p=p_N`, the prime number theorem `p_N/log p_N~N` then gives

\[
B_N(p_N^{-\beta})
\sim \frac{p_N^{1-\beta}}{\log p_N}
\sim Np_N^{-\beta},
\tag{29}
\]

in relative density among prime indices. The dyadic prime-start statement implies `(8)` by the usual dyadic summation; diagonalizing over tolerances gives an equivalent density-one subsequence formulation.

## Prior-art and novelty audit

Ayla Gafni and Terence Tao, **“On the number of exceptional intervals to the prime number theorem in short intervals,”** arXiv:`2505.24017` (2025; revised 2026), explicitly record that Guth--Maynard's zero-density estimates give the PNT in all short intervals for `theta>17/30` and in almost all short intervals for `theta>2/15`. They formulate the exceptional sets `E_delta(X,theta)` by Lebesgue measure and develop quantitative exceptional-set exponents. Their discussion also converts exceptional measure into bounds for indices supporting abnormally large prime gaps by exploiting the interval of failures generated by a large gap.

The structural idea that exceptional-set failure has **inertia** is established prior art. Danilo Bazzanella and Alberto Perelli, **“The exceptional set for the number of primes in short intervals,”** *Journal of Number Theory* 80 (2000), 109--124, DOI `10.1006/jnth.1999.2429`, study the basic structure of these exceptional sets and prove inertia/decrease properties. Danilo Bazzanella, **“Prime numbers in intervals starting at a fixed power of the integers,”** *Journal of the Australian Mathematical Society* 87 (2009), 83--99, DOI `10.1017/S1446788709000020`, explicitly uses that exceptional-set structure to obtain short-interval information on prescribed sparse starting sequences.

No novelty is claimed for the almost-all `2/15` exponent, exceptional-set methods, inertia, Brun--Titchmarsh, or sparse-start transfer as a general analytic-number-theory strategy. The Arithmetic Fidelity contribution is the exact composition needed by AF-401: isolate an elementary inertia-plus-packing transfer, apply it specifically to **prime starting points**, and then translate the resulting density-one short-interval law into the successor-depth resource `(7)` for the prime-log representation.

A targeted prior-art search located the neighboring sparse-start literature above but did not locate an explicit published statement of exactly `(2)` for all prime starting points. That absence is not treated as evidence of novelty; `(2)` is presented as a direct derived lemma from classical ingredients.

## Boundaries and falsification

The conclusion is **density one**, not an all-primes theorem. A zero-density set of prime indices may remain exceptional, so this does not replace AF-401 when a downstream discriminator must work at every prime start.

The exponent `2/15` is an open boundary here. The imported theorem gives every fixed `theta>2/15`; neither `(3)` nor `(7)` asserts the endpoint.

The transfer also requires deterministic inertia and packing. If a different observable can jump by its full error scale under arbitrarily small changes of the start point, or if the chosen sampling set has no suitable local packing bound, ambient exceptional measure does not transfer by `(10)`. Those are exact falsification conditions for reusing this mechanism elsewhere.

Equation `(7)` remains a **representation-resource law**, not a rational-prime discriminator. A matched source with the same almost-all local density and analogous sampling regularity can satisfy the same density-one successor conversion. The result therefore says how deeply an already-declared local observable can be represented on almost all prime starts; it does not show that the observable distinguishes rational primes from generalized-prime controls.

No RH consequence follows. All imported short-interval information is unconditional, and density-one prime-start fidelity leaves exceptional indices untouched.

## Consequences

AF-400--AF-402 now separate three different source-information regimes cleanly:

- regular variation prices fixed logarithmic walls but does not control arbitrary shrinking walls;
- uniform short-interval PNT controls every prime start down to `theta>17/30`, equivalently `beta<13/30` in the shrinking-wall parametrization;
- almost-all short-interval PNT plus inertia and prime packing controls a density-one set of prime starts down to `theta>2/15`, equivalently `beta<13/15`.

The conceptual gain is that **ambient almost-everywhere information is not itself a sparse-sample resource**. It becomes one only after paying two additional structural costs: persistence thickness of failure and local packing of the sample set. This is a reusable Arithmetic Fidelity principle for transporting statements through a sampling compression.

For the current prime-log locality branch, the next boundary is correspondingly sharper. Any downstream mechanism requiring `beta>=13/15` cannot inherit even a density-one successor law from the present almost-all short-interval theorem through this transfer alone; it needs stronger exceptional-set input, more structure than worst-case endpoint inertia, or a different representation.