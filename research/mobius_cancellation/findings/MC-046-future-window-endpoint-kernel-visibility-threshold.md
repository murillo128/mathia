# MC-046 — Terminal prime slabs remain hidden across sublinear future windows for endpoint-vanishing kernels

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Use the multiplicative exact-support comparator from `MC-045`. Fix

\[
\frac{17}{30}<\alpha<\frac34,
\qquad
H=\lfloor X^\alpha\rfloor,
\]

let `chi_X` be the completely multiplicative sign character which equals `-1` on primes in `(X-H,X]` and `+1` on all other primes, and put

\[
\nu_X(n)=\mu(n)\chi_X(n).
\tag{1}
\]

Write

\[
P_X=\pi(X)-\pi(X-H).
\]

By Guth--Maynard (`MC-S32`),

\[
P_X=(1+o(1))\frac{H}{\log X}.
\tag{2}
\]

The same **single fixed function** `nu_X` remains separated from Möbius by a polynomially super-square-root partial-sum discrepancy throughout every sublinear future interval. If

\[
X\le Y<2(X-H),
\]

then

\[
\boxed{
\sum_{n\le Y}\nu_X(n)-M(Y)=2P_X
=(2+o(1))\frac{H}{\log X}.
}
\tag{3}
\]

At the same time, the standard prime-harmonic pretentious distance between the two functions never grows after scale `X`:

\[
\boxed{
\mathbb D(\nu_X,\mu;Y)^2
=2\sum_{X-H<p\le X}\frac1p
=(2+o(1))\frac{H}{X\log X}
=o(1)
\qquad (Y\ge X).
}
\tag{4}
\]

Thus replacing one-scale pretentious data by the same standard distance observed at many later scales does not recover the missing terminal-prime information.

There is a complementary quantitative statement for Riesz and more general endpoint-vanishing kernels. Let `K:[0,1]->C` satisfy, for fixed constants `C>0` and `r>=1`,

\[
|K(u)|\le C(1-u)^r,
\qquad 0\le u\le1,
\tag{5}
\]

and define

\[
T_{K,a}(Y)=\sum_{n\le Y}a(n)K(n/Y).
\tag{6}
\]

For `Y=X+Delta<2(X-H)`, the exact localization in `(3)` gives

\[
\boxed{
|T_{K,\nu_X}(Y)-T_{K,\mu}(Y)|
\le
2CP_X\left(\frac{\Delta+H}{Y}\right)^r.
}
\tag{7}
\]

For the order-`k` Riesz kernel `K_k(u)=(1-u)^k`, this is exact up to the distribution of the slab primes:

\[
S_{k,\nu_X}(Y)-S_{k,\mu}(Y)
=2\sum_{X-H<p\le X}\left(1-\frac pY\right)^k.
\tag{8}
\]

If

\[
\Delta=X^\beta,
\qquad
\alpha<\beta<1,
\]

then `Delta/H -> infinity`, so the weight is uniform across the prime slab and

\[
\boxed{
S_{k,\nu_X}(X+X^\beta)-S_{k,\mu}(X+X^\beta)
=(2+o(1))\frac{X^{\alpha+k\beta-k}}{\log X}.
}
\tag{9}
\]

Hence the order-`k` Riesz observation crosses the square-root **power** scale only after the additive future-shift exponent passes

\[
\boxed{
\beta_k^*=1-\frac{\alpha-1/2}{k}.
}
\tag{10}
\]

More precisely, for `beta<beta_k^*` the difference in `(9)` is `o(X^(1/2))`; for `beta>beta_k^*` it is polynomially larger than `X^(1/2)`; at equality it is still only `X^(1/2+o(1))/log X`. Because `alpha<3/4`, one has `beta_k^*>alpha` for every integer `k>=1`, so `(9)` legitimately describes the transition regime.

There is a useful uniform corollary. For **every fixed**

\[
\beta<\frac{14}{15},
\tag{11}
\]

one can choose

\[
\frac{17}{30}<\alpha<\min\left(\frac34,\frac32-\beta\right).
\tag{12}
\]

Then `(3)` is polynomially above square-root scale, but for every cutoff

\[
X\le Y\le X+X^\beta
\tag{13}
\]

and every positive integer Riesz order `k>=1`,

\[
\boxed{
|S_{k,\nu_X}(Y)-S_{k,\mu}(Y)|=o(X^{1/2}).
}
\tag{14}
\]

The same conclusion holds for any fixed family of kernels satisfying `(5)` with a uniform constant and at least a linear endpoint zero. The exponent `14/15=3/2-17/30` is **not** asserted to be an intrinsic arithmetic barrier: it is exactly the blind-window exponent obtainable from the present construction using the current uniform prime-asymptotic threshold `17/30` in `MC-S32`.

This strengthens the one-scale obstruction of `MC-045` in a precise direction. Exact support and multiplicativity do not make the endpoint perturbation recoverable merely because one observes the same standard pretentious carrier or endpoint-vanishing smoothings at a collection of nearby future scales. What matters is how far into the future the carrier transports current endpoint coefficients, or whether it avoids endpoint vanishing altogether.

## 1. Why the discrepancy stays localized at every sublinear future cutoff

For a slab prime

\[
p\in(X-H,X],
\]

we have `p>X-H`. Since `H=o(X)`, eventually `X-H>X/2`. If

\[
Y<2(X-H),
\]

then no composite integer `n<=Y` can be divisible by such a prime: a multiple `pm` with `m>=2` satisfies

\[
pm\ge2p>2(X-H)>Y.
\]

The functions `nu_X` and `mu` therefore differ below `Y` only on the slab primes themselves. Each changed prime contributes

\[
\nu_X(p)-\mu(p)=1-(-1)=2,
\]

which proves `(3)`.

In particular, if `Y=X+X^beta` with any fixed `beta<1`, then `Y<2(X-H)` for all sufficiently large `X`. The endpoint discrepancy from `MC-045` is therefore not a single-cutoff accident: it survives unchanged throughout every sublinear additive future window.

## 2. Standard multiscale pretentious data remains blind

Pretentious distance is defined only from prime values. Once the observation scale has passed `X`, the complete set of primes on which `nu_X` and `mu` differ has already entered the distance. Thus for every `Y>=X`,

\[
\mathbb D(\nu_X,\mu;Y)^2
=2\sum_{X-H<p\le X}\frac1p,
\]

and `(2)` plus `p=X(1+o(1))` on the slab gives `(4)`.

The same conclusion extends to the optimized ordinary Halasz profile on any polynomial scale horizon. If

\[
\mathcal M(f;Y,T)
=\min_{|t|\le T}\mathbb D(f,n^{it};Y)^2,
\]

then the triangle inequality gives, uniformly in `t`,

\[
|\mathbb D(\nu_X,n^{it};Y)-\mathbb D(\mu,n^{it};Y)|
\le \mathbb D(\nu_X,\mu;Y).
\tag{15}
\]

For `X<=Y<=X^C` with fixed `C>1`, both distances on the left are `O(sqrt(log log X))`, while `(4)` gives

\[
\mathbb D(\nu_X,\mu;Y)
=X^{(\alpha-1)/2+o(1)}.
\]

Consequently

\[
\boxed{
\mathcal M(\nu_X;Y,T)-\mathcal M(\mu;Y,T)=o(1)
}
\tag{16}
\]

uniformly over such `Y` and over any common nonempty twist range. This is fully consistent with Jung--Lemke Oliver (`MC-S7`): ordinary prime-only pretentiousness is not a power-cancellation-faithful metric in general. The new role here is only to close the specific idea that **same-function multiscale repetition of that standard carrier** repairs the `MC-045` endpoint defect.

## 3. Endpoint-vanishing kernels have an explicit future-visibility law

For a slab prime `p` and `Y=X+Delta`,

\[
0\le 1-\frac pY
=\frac{Y-p}{Y}
\le\frac{\Delta+H}{Y}.
\tag{17}
\]

Since the functions differ below `Y` only at those primes, `(5)` and `(17)` immediately give `(7)`.

For `K_k(u)=(1-u)^k`, no absolute-value relaxation is needed: every changed prime contributes with the same positive sign, which yields `(8)`.

If `Delta=X^beta` with `beta>alpha`, then uniformly across the slab

\[
Y-p=\Delta+(X-p)
=\Delta(1+o(1)),
\qquad
Y=X(1+o(1)).
\]

Therefore

\[
\left(1-\frac pY\right)^k
=(1+o(1))\left(\frac\Delta X\right)^k
\]

uniformly over all slab primes. Summing and using `(2)` proves `(9)`.

The exponent in `(9)` is

\[
e_k(\alpha,\beta)=\alpha+k\beta-k.
\tag{18}
\]

Solving `e_k=1/2` gives `(10)`. Moreover

\[
\beta_k^*-\alpha
=1-\alpha-\frac{\alpha-1/2}{k}
\ge\frac32-2\alpha>0,
\tag{19}
\]

so the transition always lies in the `Delta>>H` regime under the standing assumption `alpha<3/4`.

This makes the scale-coherence obligation quantitative. A fixed-order anchored Riesz kernel does eventually see the slab, unlike standard pairwise pretentious distance, but only after the future shift has made the previously terminal coefficients large enough under the kernel's endpoint zero.

## 4. A whole nearby bank of positive Riesz orders can remain subcritical

Let `Y-X<=X^beta` with `beta<1`, and put

\[
m=\max(\alpha,\beta).
\]

Then `(17)` gives

\[
1-\frac pY\ll X^{m-1}.
\]

For every integer `k>=1`, this weight lies in `[0,1]` and is no larger than its order-one value. Hence, uniformly in `k`,

\[
|S_{k,\nu_X}(Y)-S_{k,\mu}(Y)|
\le
2P_X\frac{X^\beta+H}{Y}
=X^{\alpha+m-1+o(1)}.
\tag{20}
\]

If `(12)` holds, then either `beta<=alpha`, in which case

\[
\alpha+m=2\alpha<\frac32,
\]

or `beta>alpha`, in which case

\[
\alpha+m=\alpha+\beta<\frac32.
\]

Thus `(20)` is `o(X^(1/2))`, proving `(14)`. The ordinary partial-sum discrepancy `(3)` is instead

\[
X^{\alpha+o(1)}\gg X^{1/2}.
\]

Existence of an `alpha` satisfying `(12)` is equivalent, at the lower endpoint supplied by `MC-S32`, to

\[
\beta<\frac32-\frac{17}{30}=\frac{14}{15}.
\]

This `14/15` is therefore a **source-limited control frontier**, not a proposed natural constant. If future uniform prime asymptotics reach intervals of length `X^(theta+epsilon)` with smaller `theta`, the identical construction would extend the blind-window range to `beta<3/2-theta`, subject to the independent same-scale condition `alpha<3/4`.

## 5. Prior art and novelty boundary

The ingredients are established.

- `MC-S7` explicitly shows that ordinary prime-only pretentiousness does not, in general, detect power cancellation and develops stronger prime-power-sensitive notions. No novelty is claimed for that principle.
- `MC-S31` anchors generalized Riesz means of the Möbius function and the classical smoothing framework. `MC-042`--`MC-044` already record the fixed-order RH equivalence, normalization-vacuity threshold, endpoint attenuation, and exact scale-derivative inversion relevant here.
- `MC-S32` is the sole quantitative prime-distribution input. Its uniform asymptotic for intervals of length above `X^(17/30+epsilon)` supplies the slab population `(2)`.
- `MC-045` introduced the present prime-slab multiplicative comparator and proved same-scale invisibility. The derivation above does not claim a new summability theorem; it computes the exact future response of that comparator and turns the previously qualitative "scale coherence" escape into an explicit visibility threshold.

A targeted literature check around Riesz/Tauberian summability, power-cancellation-aware pretentiousness, and Guth--Maynard short-interval prime asymptotics finds these mechanisms in their established settings but no reason to treat the numerical visibility laws `(9)`--`(14)` as an independent novelty claim. They are retained as a Mathia-specific matched-control consequence because they sharpen the live inverse-theorem falsification test.

## 6. Consequence for the local-to-global program

`MC-045` left same-function multiscale structure as one possible escape from its one-scale obstruction. The present finding separates two very different meanings of that phrase.

For standard pretentious distance, observing more scales supplies no new information about this perturbation at all: the pairwise distance is already saturated once the flipped slab primes have entered. Repetition of the same prime-harmonic quotient is not scale coherence.

For endpoint-vanishing smoothings such as positive-order Riesz kernels, future scales do transport the hidden coefficients back into view, but the transport has a calculable delay. A bank of nearby anchored smoothings can therefore remain blind even when it includes every positive integer Riesz order. Merely replacing one diagonal scale by a short multiscale window is not enough.

A surviving transfer mechanism must use information not preserved by this control, for example:

- a translated/localized kernel whose current endpoint coefficients have order-one weight;
- future-scale control extending beyond the relevant visibility threshold, together with a valid inverse/Tauberian theorem;
- stronger prime-sensitive or prime-power-sensitive structure than standard pretentious distance;
- the exact Möbius prime law in a way that is not equivalent to inserting the answer;
- or a nonlinear/bilinear coupling that forces terminal prime information to interact with already visible lower scales.

The terminal prime-slab family `(1)` should remain a first falsification control for any proposed generic multiscale inverse theorem built only from exact support, multiplicativity, standard pretentious scalars, and anchored endpoint-vanishing smoothings.