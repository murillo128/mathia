# WI-249 — Odd compact-window discrepancy has exponentially large recurrent quasimodes

## Status

- **Evidence:** `EXACT-DERIVED + LITERATURE-BACKED + DECISIVE-NEGATIVE + PRIOR-ART-AUDITED`.
- **Scope:** this closes a narrower route left open by `WI-248`: after passing from the raw prime comb to the exact density-one discrepancy of `WI-241`, and after restricting to odd compactly supported tests, one still cannot obtain an RH-facing source bound that is uniform over the whole odd window. It does **not** constrain the first-crossing zero mode of `WI-247`, prove RH, or improve the simple-critical-zero proportion.
- **Novelty boundary:** the localized source formula is Suzuki's; recurrence of prime logarithms is the same classical Kronecker--Weyl mechanism used in Chuk's pointwise-comb barrier; the Riemann--Lebesgue lemma and PNT are classical. The exact smooth odd quasimode argument below, including the triangular window taper after density subtraction and its `(2+o(1))e^a/a` discrepancy lower bound, was not located in the targeted line-local/external audit. No priority claim is made.

## Claim

Use the exact odd-sector discrepancy normalization from `WI-241`:

\[
\Delta_\Lambda^a(v)
:=\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}C_v(\log n)
-\int_0^{2a}e^{h/2}C_v(h)\,dh,
\]

where

\[
C_v(h)=\operatorname{Re}\int_{\mathbb R}v(x+h)\overline{v(x)}\,dx.
\]

For every `a>0`, define the triangularly tapered prime mass

\[
D(a):=
\sum_{\log n<2a}
\frac{\Lambda(n)}{\sqrt n}
\left(1-\frac{\log n}{2a}\right).
\]

Then

\[
\boxed{
\sup_{\substack{v\in C_c^\infty(-a,a),\ v\ {\rm real\ odd}\\ \|v\|_2=1}}
\Delta_\Lambda^a(v)
\ge D(a).
}
\]

Moreover, as `a -> infinity`,

\[
\boxed{
D(a)=\left(2+o(1)\right)\frac{e^a}{a}.
}
\]

Consequently every radius-only upper bound

\[
\Delta_\Lambda^a(v)\le U(a)
\qquad
\text{for all normalized odd }v\in C_c^\infty(-a,a)
\]

must satisfy

\[
\boxed{
U(a)\ge\left(2+o(1)\right)\frac{e^a}{a}.
}
\]

In the Weil form the source occurs as `-2 Delta`, so the corresponding unavoidable all-odd source scale is `(4+o(1))e^a/a`.

This is exponentially larger than the order-one first-crossing tariff of `WI-244`--`WI-247`. Therefore subtracting the density-one continuum and imposing odd parity do **not** rescue a source estimate that is uniform over the entire compact window. Any RH-facing source theorem must use information special to the first odd zero mode: the zero-mode equation, prior positivity at smaller radii, spectral-mass localization, or another genuinely directional constraint.

## 1. Smooth odd high-frequency carriers

Fix `a>0`. Let `w\in C_c^\infty(-a,a)` be real, even, and nonzero, and put

\[
v_t(x):=\frac{w(x)\sin(tx)}{\|w\sin(t\cdot)\|_2}.
\]

Then `v_t` is a normalized real odd admissible test. Write

\[
A_w(h):=\int_{\mathbb R}w(x+h)w(x)\,dx.
\]

The product-to-sum identity gives

\[
\begin{aligned}
\int w(x+h)w(x)\sin(t(x+h))\sin(tx)\,dx
&=\frac12\cos(th)A_w(h)\\
&\quad-\frac12\int w(x+h)w(x)\cos(2tx+th)\,dx,
\end{aligned}
\]

while

\[
\|w\sin(t\cdot)\|_2^2
=\frac12\|w\|_2^2
-\frac12\int w(x)^2\cos(2tx)\,dx.
\]

By the Riemann--Lebesgue lemma, for each fixed `h`,

\[
\boxed{
C_{v_t}(h)
-\cos(th)\frac{A_w(h)}{\|w\|_2^2}
\longrightarrow0
\qquad(t\to\infty).
}
\]

The continuum comparison term simultaneously vanishes:

\[
\boxed{
\int_0^{2a}e^{h/2}C_{v_t}(h)\,dh\longrightarrow0.
}
\]

One way to see the second limit is to write it as a quadratic integral over the compact square `[-a,a]^2`; after inserting `v_t=w\sin(tx)` it is a finite sum of Fourier transforms of `L^1` kernels evaluated at frequencies of size `t`. Multidimensional Riemann--Lebesgue then applies. This step is important: the quasimode does not merely maximize the discrete prime term while leaving an uncontrolled density-one contribution; the continuum term genuinely oscillates away.

## 2. Prime-log recurrence aligns every discrete source atom

Only finitely many primes occur for fixed `a`. Their logarithms are linearly independent over `Q`: clearing denominators in a rational relation and exponentiating would give a nontrivial multiplicative relation among distinct primes, impossible by unique factorization.

Kronecker--Weyl recurrence therefore supplies a sequence `t_j -> infinity` such that, simultaneously for every prime `p<e^{2a}`,

\[
t_j\log p\longrightarrow0\pmod{2\pi}.
\]

Every relevant prime power is `n=p^k`, so the same sequence gives

\[
\cos(t_j\log n)\longrightarrow1.
\]

Combining this with the previous section and the finiteness of the prime-power sum yields

\[
\lim_{j\to\infty}\Delta_\Lambda^a(v_{t_j})
=
\sum_{\log n<2a}
\frac{\Lambda(n)}{\sqrt n}
\frac{A_w(\log n)}{\|w\|_2^2}.
\]

Now choose an even smooth plateau sequence `w_epsilon` converging in `L^2` to the indicator of `(-a,a)`. For every fixed `0\le h<2a`, translation continuity gives

\[
\frac{A_{w_\varepsilon}(h)}{\|w_\varepsilon\|_2^2}
\longrightarrow
\frac{|(-a,a)\cap(-a-h,a-h)|}{2a}
=1-\frac{h}{2a}.
\]

The set of relevant prime powers is finite, so the limits may be taken after the recurrence limit without any uniformity issue. Hence

\[
\sup_{\substack{v\in C_c^\infty(-a,a),\ v\ {\rm odd}\\ \|v\|_2=1}}
\Delta_\Lambda^a(v)
\ge
\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
\left(1-\frac{\log n}{2a}\right)
=D(a).
\]

The triangular taper is therefore not a heuristic boundary correction. It is the exact overlap profile approached by smooth compact-window odd high-frequency carriers.

## 3. The tapered mass is still exponentially large

Put `X=e^{2a}`. Then

\[
D(a)
=
\int_{1^-}^{X}
 x^{-1/2}
\left(1-\frac{\log x}{\log X}\right)
\,d\psi(x),
\]

where `psi(x)=sum_{n\le x} Lambda(n)`. Partial summation together with the classical PNT (for instance its standard de la Vallee Poussin error form) permits replacement of `d psi(x)` by `dx` with error `o(e^a/a)`. The main integral is elementary. Writing `x=u^2` and `sqrt X=e^a`,

\[
\begin{aligned}
\int_1^{e^{2a}}x^{-1/2}
\left(1-\frac{\log x}{2a}\right)dx
&=2\int_1^{e^a}\left(1-\frac{\log u}{a}\right)du\\
&=\frac{2e^a}{a}-2-\frac2a.
\end{aligned}
\]

Therefore

\[
\boxed{D(a)=\left(2+o(1)\right)e^a/a.}
\]

The boundary taper wins a factor of order `a` compared with the untapered half-comb mass, but it does not change the exponential radius scale.

## 4. Why this is a different barrier from WI-248

`WI-248`, auditing Chuk's compact-window argument, proves that the raw pointwise prime comb has exact recurrent supremum

\[
A_a=2\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
=(4+o(1))e^a.
\]

That no-go acts **before** using the compact-window autocorrelation and before the pole/PNT-main-density cancellation isolated in `WI-241`. It therefore left a plausible repair: perhaps one could first subtract the density-one continuum exactly, restrict to odd tests, and then bound the surviving signed discrepancy uniformly on the compact window.

The present finding closes precisely that repair. The smooth odd quasimodes retain the compact-window overlap geometry and the exact discrepancy subtraction, yet prime-log recurrence still produces

\[
\sup_{\rm odd}\Delta_\Lambda^a
\ge(2+o(1))e^a/a.
\]

Thus the continuum subtraction and odd parity reduce the worst recurrent source by a polynomial factor in the radius, not to the order-one scale needed by the first-crossing tariff.

This does **not** say that the first-crossing vector itself can realize the quasimodes above. In fact the construction deliberately sends its carrier frequency to infinity, while the archimedean mean multiplier grows logarithmically there. These tests are not shown to satisfy the zero-mode equation. That distinction is exactly the surviving opportunity: the next theorem must exploit a relation between the source and the spectral mass of the attained zero mode, rather than bound the source on every odd test of the same support.

## 5. Prior-art and novelty audit

The load-bearing inputs separate cleanly.

- **Literature-backed source formula:** Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096 (2026), supplies the localized von Mangoldt translation formula used in `WI-241` and the compact-support operator framework used in `WI-238`/`WI-247`.
- **Recent compact-window barrier:** Marcus Chuk, *Weil positivity in compact windows: certified two-sided bounds and a Landau--Widom decay law*, arXiv:2608.24827 (2026), proves that the raw finite prime comb has exact pointwise supremum equal to its coefficient mass and records the resulting doubly exponential pointwise-envelope barrier. `WI-248` independently audited the recurrence step.
- **Classical ingredients:** Kronecker--Weyl simultaneous recurrence, the Riemann--Lebesgue lemma, unique factorization, and the Prime Number Theorem.
- **Exact deduction here:** modulating a smooth even compact-window plateau by an odd sine, aligning the finite prime-log phases, letting the continuum comparison oscillate away, then taking the plateau limit yields the triangularly tapered discrepancy lower bound and its `(2+o(1))e^a/a` asymptotic.

A targeted search around localized Weil autocorrelations, odd compact windows, von Mangoldt discrepancy, truncated-sine carriers, and prime-log recurrence located Suzuki's source formula and Chuk's pointwise-comb recurrence, but no statement of this post-subtraction odd-window lower bound. Search absence is recorded only as audit context, not as a priority claim.

## 6. Stress tests and boundaries

1. **No inadmissible hard cutoff is used.** The triangular profile is obtained as a limit of even `C_c^infty` plateaux; every modulated test before the plateau limit is smooth, compactly supported, and odd.
2. **The continuum subtraction is retained exactly.** The second term in `Delta` tends to zero on the high-frequency family by Riemann--Lebesgue; it is not dropped by an absolute-value estimate.
3. **Recurrence is qualitative, not effective.** The argument needs only arbitrarily late simultaneous phase alignment for a finite set of prime logarithms. It gives no useful bound on the first recurrence height.
4. **The PNT asymptotic is unconditional.** It is used only to measure the radius growth of the explicit positive lower bound `D(a)`; the fixed-radius inequality `sup Delta >= D(a)` is independent of any asymptotic prime estimate.
5. **This is not an RH counterexample.** The high-frequency quasimodes merely show that the whole odd window contains vectors with large positive discrepancy. They are not first-crossing eigenvectors and are not claimed to make the Weil form negative or zero.
6. **The first-crossing class remains viable.** `WI-247` says RH failure forces a very special attained odd zero mode. The present no-go shows that oddness and compact support alone are insufficient to characterize that class; the zero-mode equation or prior-radius positivity must enter the source estimate.
7. **Normalization check.** `WI-241` writes `Q_W=Q_mean-2 Delta`. The displayed asymptotic is for `Delta` itself; the corresponding term in the Weil form has twice that magnitude.

## Falsification and next gate

The finding fails if the `WI-241` sign/normalization of `Delta` is wrong, if the modulated smooth autocorrelation limit above does not hold, if prime-log Kronecker recurrence cannot be inherited by the finite prime powers, if the continuum comparison fails to vanish along the same high-frequency sequence, or if the tapered PNT asymptotic is incorrect.

Assuming those checks stand, the next high-value gate is sharply narrower than a uniform source norm: derive from

\[
Q_W^a(v_*)=0,
\qquad
\lambda_b^->0\quad(b<a),
\]

an additional spectral or autocorrelation constraint on the first odd crossing `v_*`, and use **that** constraint to show that its signed discrepancy cannot meet the `WI-246` tariff. Any bound that applies to every normalized odd vector supported in `[-a,a]` is now known to be structurally too coarse.