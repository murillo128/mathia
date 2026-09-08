# MC-150 — Dirichlet-weighted semigroup rows create a non-RH critical-half threshold

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Work in the canonical number-state representation used in `MC-149`,

\[
\mathcal H=\ell^2(\mathbb N),
\qquad
S_m\varepsilon_k=\varepsilon_{mk},
\qquad
D_a\varepsilon_k=a_k\varepsilon_k,
\]

with `a=(a_k)` bounded. `MC-149` proved

\[
[D_a,S_m]\varepsilon_k=(a_{mk}-a_k)\varepsilon_{mk}
\tag{1}
\]

and showed that unweighted boundedness is universal while compact/Schatten decay rejects Möbius. The first source-natural interpolation between those endpoints is to weight the dilation coordinate by its Dirichlet/Boltzmann scale. For real `\sigma`, consider the collective row

\[
\mathcal R_\sigma(a)\xi
:=\bigl(m^{-\sigma}[D_a,S_m]\xi\bigr)_{m\ge2}
\in\bigoplus_{m\ge2}\mathcal H,
\tag{2}
\]

whenever the right-hand side is square summable.

This row has the exact norm criterion

\[
\boxed{
\|\mathcal R_\sigma(a)\|^2
=
\sup_{k\ge1}
\sum_{m\ge2}m^{-2\sigma}|a_{mk}-a_k|^2,
}
\tag{3}
\]

with the convention that an infinite supremum means that the row does not extend to a bounded operator on `\mathcal H`.

For every bounded sequence `a`,

\[
\boxed{
\sigma>\frac12
\quad\Longrightarrow\quad
\|\mathcal R_\sigma(a)\|
\le
2\|a\|_\infty\bigl(\zeta(2\sigma)-1\bigr)^{1/2}.
}
\tag{4}
\]

Thus the entire half-plane `\sigma>1/2` is again **target-complete**: the weighting accepts every bounded diagonal lookup table.

For the Möbius diagonal the opposite side fails already on the single vector `\varepsilon_1`. Since `\mu(1)=1` and `\mu(4r)=0`,

\[
\|\mathcal R_\sigma(\mu)\varepsilon_1\|^2
\ge
\sum_{r\ge1}(4r)^{-2\sigma},
\tag{5}
\]

so

\[
\boxed{
\mathcal R_\sigma(\mu)
\text{ is bounded }
\Longleftrightarrow
\sigma>\frac12.
}
\tag{6}
\]

The apparent critical-half threshold is **not** a Möbius-cancellation or RH mechanism. The support-matched control `q=\mu^2` has exactly the same full-dilation threshold, because `q(1)=1` and `q(4r)=0` gives the same lower bound `(5)`. Above `1/2`, `(4)` applies universally.

The conclusion survives the obvious attempt to remove squareful dilation contamination by retaining only prime dilations. Define

\[
\mathcal R^{\mathbb P}_\sigma(a)\xi
:=\bigl(p^{-\sigma}[D_a,S_p]\xi\bigr)_{p\in\mathbb P}.
\tag{7}
\]

Then

\[
\boxed{
\|\mathcal R^{\mathbb P}_\sigma(a)\|^2
=
\sup_{k\ge1}\sum_p p^{-2\sigma}|a_{pk}-a_k|^2.
}
\tag{8}
\]

For Möbius, `\mu(p)=-1`, hence

\[
\|\mathcal R^{\mathbb P}_\sigma(\mu)\varepsilon_1\|^2
=4\sum_p p^{-2\sigma}.
\tag{9}
\]

For the support control `q=\mu^2`, if `k` is squarefree then

\[
|q(pk)-q(k)|
=
\begin{cases}
1,&p\mid k,\\
0,&p\nmid k,
\end{cases}
\]

and therefore

\[
\sup_k\sum_p p^{-2\sigma}|q(pk)-q(k)|^2
=
\sum_p p^{-2\sigma}
\tag{10}
\]

in the extended sense. The Liouville function supplies a separate orientation control: `\lambda(p)=-1` for every prime, so `(9)` holds with `\mu` replaced by `\lambda`.

Since the prime reciprocal sum diverges and `p^{-\alpha}\ge p^{-1}` for `\alpha\le1`, while `\sum_p p^{-\alpha}` converges for `\alpha>1`, equations `(8)`--`(10)` give

\[
\boxed{
\mathcal R^{\mathbb P}_\sigma(\mu),
\mathcal R^{\mathbb P}_\sigma(\mu^2),
\mathcal R^{\mathbb P}_\sigma(\lambda)
\text{ are bounded exactly when }
\sigma>\frac12.
}
\tag{11}
\]

Thus the number `1/2` here is the Hilbert-square pullback of the ordinary Dirichlet convergence boundary `1`: the row norm squares the weight, replacing `m^{-\sigma}` or `p^{-\sigma}` by `m^{-2\sigma}` or `p^{-2\sigma}`. It is a generic `\ell^2` summability threshold, not evidence that the critical line has been selected.

Consequently the simplest weighted escape left by `MC-149` closes: **separable Dirichlet weighting of the raw canonical semigroup commutators either becomes universal above the half threshold or fails on Möbius at and below it, and matched non-Möbius controls exhibit the same boundary.** A surviving transverse Bost--Connes route must use structure not reducible to this one-coordinate square-summability test.

## 1. Exact row norm

For a finitely supported vector

\[
\xi=\sum_k\xi_k\varepsilon_k,
\]

equation `(1)` gives

\[
[D_a,S_m]\xi
=
\sum_k(a_{mk}-a_k)\xi_k\varepsilon_{mk}.
\]

For each fixed `m`, the vectors `\varepsilon_{mk}` are orthonormal as `k` varies. The external direct sum in `(2)` also makes distinct dilation coordinates orthogonal. Hence Tonelli's theorem for the resulting nonnegative series gives

\[
\begin{aligned}
\|\mathcal R_\sigma(a)\xi\|^2
&=
\sum_{m\ge2}m^{-2\sigma}
\sum_k|a_{mk}-a_k|^2|\xi_k|^2\\
&=
\sum_k
\left(
\sum_{m\ge2}m^{-2\sigma}|a_{mk}-a_k|^2
\right)|\xi_k|^2.
\end{aligned}
\tag{12}
\]

The row is therefore diagonal at the level of `\mathcal R_\sigma(a)^*\mathcal R_\sigma(a)`, with diagonal entries

\[
A_{\sigma,a}(k)
:=
\sum_{m\ge2}m^{-2\sigma}|a_{mk}-a_k|^2.
\tag{13}
\]

It extends boundedly to all of `\mathcal H` exactly when `\sup_k A_{\sigma,a}(k)<\infty`, and its norm squared is that supremum. This proves `(3)`.

If `\sigma>1/2`, boundedness of `a` gives

\[
A_{\sigma,a}(k)
\le
4\|a\|_\infty^2
\sum_{m\ge2}m^{-2\sigma}
=
4\|a\|_\infty^2(\zeta(2\sigma)-1)
\]

uniformly in `k`, proving `(4)`. No arithmetic property of `a` is used. The favorable half-plane is therefore universal by construction.

## 2. The full-dilation half threshold is already squarefree-support data

At `k=1`, Möbius gives

\[
A_{\sigma,\mu}(1)
=
\sum_{m\ge2}m^{-2\sigma}|\mu(m)-1|^2.
\tag{14}
\]

Every multiple of four is squareful and has `\mu(4r)=0`, so `(5)` follows. The series `\sum_r r^{-2\sigma}` diverges exactly when `\sigma\le1/2`. Combined with the universal upper bound `(4)`, this proves `(6)`.

But the same proof uses no Möbius orientation. For

\[
q(n)=\mu(n)^2,
\]

we again have `q(1)=1` and `q(4r)=0`, hence

\[
A_{\sigma,q}(1)
\ge
4^{-2\sigma}\sum_{r\ge1}r^{-2\sigma}.
\tag{15}
\]

Therefore `\mathcal R_\sigma(q)` has the same exact boundedness threshold. The full row's critical half can already be generated by the squarefree-support zero pattern that the line repeatedly treats as an adversarial control. It cannot be interpreted as recovered parity orientation or Mertens cancellation.

The use of the progression `4\mathbb N` is deliberately crude. A density theorem for squareful numbers is unnecessary: an explicit infinite subprogression supplies the complete divergence certificate.

## 3. Prime restriction still does not make the threshold Möbius-specific

Restricting the row to prime dilations removes the direct squareful-dilation witness `m=4r`. Formula `(8)` follows from the same orthogonality calculation as `(3)`.

For Möbius, the base state already gives

\[
\mu(p)-\mu(1)=-2,
\]

and hence `(9)`. The classical divergence

\[
\sum_p\frac1p=\infty
\tag{16}
\]

recorded in `MC-S6` implies divergence of `\sum_pp^{-2\sigma}` for every `\sigma\le1/2`; convergence for `\sigma>1/2` follows by comparison with `\sum_{n\ge2}n^{-2\sigma}`. This establishes the Möbius prime-row threshold without analytic continuation or zero information.

The support control is slightly subtler and more diagnostic. If `k` is squarefree, then `q(k)=1`. Multiplication by a prime `p` preserves squarefreeness exactly when `p\nmid k`, while `pk` contains `p^2` when `p\mid k`. Thus

\[
\sum_p p^{-2\sigma}|q(pk)-q(k)|^2
=
\sum_{p\mid k}p^{-2\sigma}.
\tag{17}
\]

Taking `k` to be the product of any finite initial set of primes and then enlarging that set shows

\[
\sup_k\sum_{p\mid k}p^{-2\sigma}
=
\sum_pp^{-2\sigma},
\]

which proves `(10)`. The prime-only **operator norm** therefore has the same half threshold even after Möbius signs are removed entirely.

Liouville gives an independent calibration in the other direction. Since

\[
\lambda(1)=1,
\qquad
\lambda(p)=-1,
\]

the exact base-state divergence `(9)` is shared by a function with no squarefree-support zeros. Hence neither support nor the local prime sign by itself can certify the desired global Möbius behavior: different controls realize the same threshold for different elementary reasons.

## 4. Why the half appears

The mechanism is now transparent. The unweighted family in `MC-149` has one bounded operator per dilation. Combining those operators into a Hilbert row replaces a scalar weight `w_m` by the square mass `|w_m|^2` in the norm. Choosing the canonical Dirichlet scale

\[
w_m=m^{-\sigma}
\]

therefore asks for convergence of

\[
\sum_m m^{-2\sigma}
\]

or, on prime dilations,

\[
\sum_p p^{-2\sigma}.
\]

Their convergence boundary is `2\sigma=1`. The resulting `\sigma=1/2` is consequently a **quadratic summability artifact of the chosen Hilbert aggregation**. Nothing in the derivation refers to zeta zeros, the functional equation, first-absolute Mertens excursion, or even to Möbius after the universal upper bound is established.

This is a useful falsification pattern for future critical-half sightings in arithmetic Hilbert constructions: whenever a parameter enters a coefficient as `n^{-\sigma}` and the decisive norm immediately squares coefficients, first test whether the apparent half boundary is just the pullback of the ordinary abscissa `1` before assigning RH significance.

## 5. Prior art and novelty assessment

The canonical Bost--Connes number-state representation and semigroup isometries are established prior art and were already audited in `MC-138`--`MC-149`. `MC-149` also records the standard weighted-shift/operator-theoretic facts needed for the individual commutators and the nearby spectral-triple literature. This finding does not claim novelty for those objects.

The passage from a family of operators to an `\ell^2` direct-sum row and the identity `(12)` are standard Hilbert-space orthogonality. The analytic convergence input is also classical: `\sum n^{-s}` converges for `s>1`, while the reciprocal-prime divergence used in the prime row is already anchored as `MC-S6` (Rosser--Schoenfeld/Mertens second theorem). No zero-free region, RH-equivalent estimate, or modern cancellation theorem is used.

A targeted literature search around Bost--Connes semigroup commutators, Dirichlet-weighted rows, prime-weighted commutators, and Möbius did not locate an external theorem with the exact formulation `(3)`--`(11)`. **No novelty inference is drawn from that absence.** The result is an elementary specialization of standard direct-sum operator algebra plus classical local values of `\mu`, `\mu^2`, and `\lambda`, and is persisted because it closes a live line-specific candidate class.

## Boundaries and falsification tests

- **Separable scalar Dirichlet weights only.** The result treats `m^{-\sigma}` or `p^{-\sigma}` multiplying the raw canonical commutator. A weight depending jointly on dilation and number state, a matrix-valued weight, or another relational coupling is not reduced to `(3)` automatically.
- **Raw commutators only.** Twisted commutators, alternative derivations/Dirac operators, cocycles, or different representations are outside the claim. `MC-149` already identifies nearby twisted spectral-triple literature as a boundary rather than something ruled out.
- **Hilbert row aggregation only.** Other norms or nonlinear aggregations have different summability exponents and require separate analysis. In particular, moving the apparent critical parameter by changing the ambient `\ell^q` norm would itself be evidence that the threshold is functional-analytic rather than RH-specific.
- **No Mertens estimate follows.** Boundedness or failure of these rows supplies no bound for `M(x)`, its first absolute mean, or any zero divisor.
- **Matched controls are decisive.** The full row shares its threshold with `\mu^2`; the prime row shares it with both `\mu^2` in operator norm and `\lambda` already at the base state. Any stronger interpretation must explain what additional observable separates these controls.
- **The threshold is exact, not numerical.** The lower bounds use explicit infinite families and the classical reciprocal-prime divergence, so finite computation cannot move the boundary.
- **The result does not close the entire intermediate Bost--Connes frontier.** It closes the first separable Dirichlet-weighted row suggested by the raw-commutator dichotomy. Weighted/twisted/averaged constructions that introduce genuinely new relational information remain open only if their selectivity and transfer to Mertens excursion are independently proved.

## Consequence for the line

The most immediate weighting of the transverse semigroup family left open by `MC-149` produces an exact critical-half threshold, but that threshold is a false positive for RH: it is forced by ordinary Dirichlet convergence after Hilbert squaring and is reproduced by matched non-Möbius controls.

Further Bost--Connes work should therefore not treat a `1/2` regularity boundary in a separable `\ell^2`-weighted commutator family as evidence of critical-line selection. A surviving intermediate category must derive its selectivity from a source-forced interaction that does more than place the raw dilation differences in a Dirichlet-weighted square sum, and it must still supply a non-tautological quantitative bridge to anchored additive Mertens excursion.