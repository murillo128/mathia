# MC-045 — A terminal prime-slab multiplicative twist is invisible to one-scale pretentious and Riesz data at square-root resolution

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Fix

\[
\frac{17}{30}<\alpha<\frac34
\]

and let `X` tend through large integers with

\[
H=\lfloor X^\alpha\rfloor.
\]

Define a completely multiplicative sign character `chi_X` on primes by

\[
\chi_X(p)=
\begin{cases}
-1,&X-H<p\le X,\\
+1,&\text{otherwise},
\end{cases}
\]

and extend it completely multiplicatively. Put

\[
\nu_X(n)=\mu(n)\chi_X(n).
\tag{1}
\]

Then `nu_X` is multiplicative, takes values in `{-1,0,1}`, and has exactly the Möbius square-free support:

\[
|\nu_X(n)|=\mu(n)^2.
\tag{2}
\]

Moreover, for every `n<=X-H`,

\[
\nu_X(n)=\mu(n),
\tag{3}
\]

while at the endpoint `X` the two summatory functions differ by

\[
\boxed{
\sum_{n\le X}\nu_X(n)-M(X)
=2\bigl(\pi(X)-\pi(X-H)\bigr)
=(2+o(1))\frac{H}{\log X}.
}
\tag{4}
\]

The last asymptotic is unconditional: Guth and Maynard's uniform short-interval prime theorem (`MC-S32`) applies because `alpha>17/30`. Thus the endpoint difference has size

\[
X^{\alpha+o(1)},
\tag{5}
\]

which is polynomially larger than the square-root scale.

At the same time this perturbation is asymptotically invisible to the **standard one-scale prime-harmonic pretentious metric**. At scale `X`,

\[
\boxed{
\mathbb D(\nu_X,\mu;X)^2
=2\sum_{X-H<p\le X}\frac1p
=(2+o(1))\frac{H}{X\log X}
=o(1).
}
\tag{6}
\]

In fact, if

\[
\mathcal M(f;X,T)
=\min_{|t|\le T}\mathbb D(f,n^{it};X)^2,
\]

then for every nonempty twist range `T=T(X)>0`,

\[
\boxed{
\mathcal M(\nu_X;X,T)-\mathcal M(\mu;X,T)=o(1).
}
\tag{7}
\]

So even the optimized standard Halász scalar at that scale changes by asymptotically nothing while the unsmoothed endpoint sum changes by `X^(alpha+o(1))`.

The same terminal-prime perturbation is simultaneously hidden by every fixed positive **integer-order one-scale Riesz smoothing** at the critical power resolution. For

\[
S_{k,a}(X)=\sum_{n\le X}a(n)\left(1-\frac nX\right)^k,
\qquad k\ge1,
\tag{8}
\]

one has

\[
\boxed{
0\le S_{k,\nu_X}(X)-S_{k,\mu}(X)
\le
2\bigl(\pi(X)-\pi(X-H)\bigr)\left(\frac HX\right)^k
=X^{\alpha(k+1)-k+o(1)}.
}
\tag{9}
\]

Because `alpha<3/4`, the largest exponent on the right for `k>=1` occurs at `k=1` and equals `2 alpha-1<1/2`. Hence

\[
\boxed{
S_{k,\nu_X}(X)-S_{k,\mu}(X)=o(X^{1/2})
\qquad\text{for every fixed integer }k\ge1,
}
\tag{10}
\]

whereas `(4)` is `X^(alpha+o(1))>>X^(1/2)`.

This closes a specific loophole left by `MC-044`. The terminal-block comparator there preserved exact square-free support but deliberately broke multiplicativity. The present family preserves **both exact support and multiplicativity**, yet a terminal prime slab can still be polynomially visible to the ordinary endpoint sum while being asymptotically invisible to the standard one-scale pretentious metric and subcritical in all fixed positive integer-order one-scale Riesz observations.

The result is a one-scale information obstruction, not a fixed-function counterexample to RH-equivalent criteria. The comparator `nu_X` depends on `X`. It therefore does not contradict `MC-042`, whose equivalence concerns one fixed coefficient sequence controlled for all sufficiently large scales. Instead it shows that a generic inverse theorem cannot recover Mertens-scale endpoint information from exact support, multiplicativity, a standard one-scale pretentious scalar, and finitely many same-scale fixed-order Riesz magnitudes alone.

## 1. Exact support, multiplicativity, and endpoint localization

The product of the multiplicative Möbius function with the completely multiplicative `chi_X` is multiplicative. Since `|chi_X(n)|=1`, equation `(2)` is immediate.

For `n<=X-H`, every prime divisor of `n` is at most `X-H`, so `chi_X(n)=1`, giving `(3)`.

Since `H=o(X)`, eventually `X-H>X/2`. Therefore a prime

\[
p\in(X-H,X]
\]

cannot divide any composite integer `n<=X`: if `n=pm` with `m>=2`, then `n> X`. Thus among integers at most `X`, changing the signs of the terminal-slab primes changes **only those primes themselves**. For such a prime,

\[
\mu(p)=-1,
\qquad
\nu_X(p)=+1,
\]

so each contributes exactly `2` to the difference of the endpoint sums. This proves the first equality in `(4)`.

To invoke `MC-S32`, apply Guth–Maynard's Corollary 1.3 to the interval beginning at `x=X-H` and of length `y=H`. Since `X-H~X` and `alpha>17/30`, one may choose a fixed positive `epsilon` smaller than `alpha-17/30`; for sufficiently large `X` the interval lies in their uniform range. Therefore

\[
\pi(X)-\pi(X-H)
\sim \frac{H}{\log X},
\tag{11}
\]

which completes `(4)`–`(5)` without any RH input.

This use of a **prime** terminal block matters. The arbitrary terminal sign flip in `MC-044` destroys multiplicativity because changing a generic value does not propagate consistently through products. Here multiplicativity is preserved globally by defining the perturbation at the Euler generators themselves, while the inequality `p>X/2` prevents that propagation from reaching any composite below the observation cutoff.

## 2. The standard pretentious metric forgets the same endpoint slab

At a prime outside `(X-H,X]`, `nu_X(p)=mu(p)=-1`. At a prime inside the slab, `nu_X(p)=+1` and `mu(p)=-1`. Hence the standard pretentious distance gives exactly

\[
\mathbb D(\nu_X,\mu;X)^2
=2\sum_{X-H<p\le X}\frac1p.
\tag{12}
\]

Every prime in the sum satisfies `p=X(1+o(1))`, and `(11)` gives the number of such primes. Consequently

\[
\sum_{X-H<p\le X}\frac1p
=(1+o(1))\frac{\pi(X)-\pi(X-H)}{X}
=(1+o(1))\frac{H}{X\log X},
\tag{13}
\]

which is `(6)`.

There is a slightly stronger consequence for the scalar actually entering the standard Halász formulation. Let

\[
\delta_X=\mathbb D(\nu_X,\mu;X).
\]

The triangle inequality (`MC-S5`, and the established pretentious framework used in `MC-002`) gives for every real `t`

\[
|\mathbb D(\nu_X,n^{it};X)-\mathbb D(\mu,n^{it};X)|\le\delta_X.
\tag{14}
\]

Every such distance is at most

\[
\left(2\sum_{p\le X}\frac1p\right)^{1/2}
=O(\sqrt{\log\log X}),
\tag{15}
\]

so

\[
|\mathbb D(\nu_X,n^{it};X)^2-
  \mathbb D(\mu,n^{it};X)^2|
\ll
\delta_X\sqrt{\log\log X}+\delta_X^2
=o(1)
\tag{16}
\]

uniformly in `t`. Taking minima over any common range proves `(7)`.

Thus the effect is not merely that the pairwise distance tends to zero. The entire optimized one-scale Halász distance profile is uniformly perturbed by `o(1)` at the squared-distance level, even though `(4)` changes the endpoint partial sum by a polynomial amount.

This is consistent with, rather than new relative to, Jung–Lemke Oliver (`MC-S7`): their power-cancellation work explicitly establishes that ordinary prime-only pretentiousness is too coarse for transferring power cancellation in general and motivates stronger notions. The durable role here is narrower: `(12)`–`(16)` give an exact **terminal-prime, Möbius-support, multiplicative** realization aligned with the separate Riesz endpoint-blindness problem of `MC-044`.

## 3. Fixed positive Riesz orders attenuate the perturbation below square-root scale

For `p` in the terminal slab,

\[
0\le1-\frac pX\le\frac HX.
\tag{17}
\]

As established in Section 1, these primes are the only terms at most `X` on which `nu_X` and `mu` differ. Therefore for integer `k>=1`,

\[
S_{k,\nu_X}(X)-S_{k,\mu}(X)
=2\sum_{X-H<p\le X}
\left(1-\frac pX\right)^k,
\tag{18}
\]

and `(17)` gives `(9)` after applying `(11)`.

The exponent

\[
e_k=\alpha(k+1)-k
=\alpha-k(1-\alpha)
\tag{19}
\]

strictly decreases with `k`. Thus

\[
e_k\le e_1=2\alpha-1<\frac12,
\tag{20}
\]

which proves `(10)`. Dividing by the fixed factor `Gamma(k+1)` gives the same conclusion for the Gamma-normalized Riesz means used in `MC-042`.

This sharpens the generic terminal-block sensitivity estimate in `MC-044` by providing an arithmetic comparator on which the suppressed block is generated entirely by prime-value changes and therefore remains multiplicative. The price is equally important: the construction is **scale-dependent**. At a later cutoff comparable to a fixed multiple of `X`, the changed primes acquire order-one Riesz weight, and a genuinely multiscale theorem can in principle detect them. The finding rules out same-scale recovery, not multiscale recovery.

## 4. What the comparator does and does not preserve

At its observation scale the comparator preserves more than the support-matched control of `MC-044`:

- exact Möbius square-free support;
- multiplicativity on all positive integers;
- exact agreement with Möbius on every integer through `X-H`;
- exact agreement at every prime below the terminal slab;
- asymptotic agreement in the standard one-scale pretentious metric and in the optimized Halász scalar;
- sub-square-root perturbation of every fixed positive integer-order same-scale Riesz mean.

Yet it does **not** preserve Möbius's exact prime-value law in the terminal slab, because that law would determine the function itself once multiplicativity and exact support are fixed. Nor does the family define one fixed comparator whose behavior is controlled coherently over all scales. These are not cosmetic exclusions: they identify precisely where a surviving Möbius-specific inverse theorem must obtain information that this matched control omits.

In particular this result does not rule out:

- a theorem exploiting the exact law `mu(p)=-1` at all primes rather than only a prime-harmonic summary;
- strong or power-cancellation-aware pretentious information that retains more than the standard distance;
- a same-function multiscale relation tying terminal prime signs at scale `X` to observations at later scales;
- translated/localized kernels whose weight remains order one on current-scale prime coefficients;
- derivative/variation information sufficient to invert Riesz smoothing;
- nonlinear Euler-factor or bilinear structure that couples the high-prime slab to lower scales.

Any such proposal must actually use the additional datum. Merely adding the word “multiplicative” to a one-scale inverse hypothesis no longer excludes the obstruction.

## 5. Prior art and novelty boundary

Three ingredients are established prior art.

First, standard pretentious distance and Halász's scalar are classical and already anchored by `MC-S4`–`MC-S7`. Jung and Lemke Oliver in particular make the general power-cancellation limitation of ordinary pretentiousness explicit. No novelty is claimed for the principle that a small ordinary pretentious distance need not preserve power cancellation.

Second, Riesz/Cesàro smoothing and its Tauberian inverse questions are classical; the Möbius Riesz family is anchored by Inoue (`MC-S31`), while `MC-042`–`MC-044` already audit the fixed-order zero burden, growing-order normalization, and endpoint visibility within this line.

Third, the only external quantitative prime-distribution input used here is Guth and Maynard (`MC-S32`), whose 2026 uniform short-interval theorem supplies `(11)` for every fixed `alpha>17/30`. Their theorem is not a Möbius-cancellation result and no new short-interval prime estimate is claimed.

A targeted literature search around sparse prime perturbations, ordinary pretentious distance, modified multiplicative functions, and short-interval behavior found the established general pretentious framework and adjacent modified-multiplicative-function literature, but does not justify a novelty claim for the present construction. The finding is retained as a **Mathia-specific matched-control synthesis** because it closes a concrete open failure mode in the current chain: `MC-044`'s endpoint-blindness comparator can be upgraded from support-preserving to support-preserving **and multiplicative** while remaining invisible to the one-scale summaries under audit.

## 6. Consequence for the active local-to-global transfer problem

`MC-002` showed that a single standard pretentious scalar has only prime-harmonic information budget. `MC-005` showed that exact support plus multiplicativity plus qualitative mean cancellation can still allow almost-linear logarithmic bias. `MC-042`–`MC-044` showed that fixed-order Riesz critical bounds remain RH-equivalent, rapidly growing normalized order becomes vacuous, and one-scale smoothing can hide terminal endpoint information even after mass renormalization.

The present result identifies a common one-scale quotient behind two of those obstructions. A terminal prime contributes order `1` to the ordinary endpoint sum, only order `1/X` to prime-harmonic distance, and only order `(H/X)^k` to a same-scale order-`k` Riesz observation. There are unconditionally `X^(alpha+o(1))` such primes in a terminal slab for `alpha>17/30`. Consequently exact support and multiplicativity do not restore the information discarded by either weighting scheme.

The live escape is therefore narrower. A smoothing/pretentious transfer route must retain **scale coherence or stronger prime-sensitive structure**, not merely more one-scale scalar summaries. A decisive next candidate should specify how information about a prime slab near the current endpoint is transported into a carrier where it has non-negligible weight without simply inserting the exact Möbius prime signs as the answer. A scale-dependent matched multiplicative perturbation such as `(1)` should be the first falsification control for any purported generic one-scale inverse theorem.