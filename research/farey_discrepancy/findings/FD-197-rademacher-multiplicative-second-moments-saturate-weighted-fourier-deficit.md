# FD-197 — Rademacher multiplicative second moments saturate the weighted Fourier deficit

- **Date:** 2026-09-18
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** random multiplicative benchmark / weighted Fourier energy / second-moment barrier
- **Depends on:** FD-002, FD-117, FD-193, FD-196
- **Classification:** `EXACT-DERIVED + RANDOM-MULTIPLICATIVE-SECOND-MOMENT + WEIGHTED-ENERGY-BASELINE + NEGATIVE/GENERIC-CANCELLATION-BOUNDARY`

## Claim

`FD-196` isolates the weighted recovery line

\[
\gamma+\sigma\le \frac32
\]

for recovering the RH-scale Mertens bound from a square-root Farey Fourier band, while the generic transfer from classical Franel energy stays on

\[
\gamma+\sigma=2.
\]

The missing half power is not merely an artefact of comparing Sobolev norms. The same noncritical line is saturated, at the level of exact second moments, by the standard Rademacher random multiplicative model supported on squarefree integers.

Let `(X_p)_p` be independent Rademacher signs on the primes and define

\[
f(n)=
\begin{cases}
\prod_{p\mid n}X_p,& n\text{ squarefree},\\
0,& n\text{ not squarefree}.
\end{cases}
\tag{1}
\]

Write

\[
A_f(x):=\sum_{n\le x}f(n),
\qquad
\mathcal B_H^f(k):=
\sum_{d\mid k}d\,A_f\!\left(\left\lfloor\frac Hd\right\rfloor\right),
\tag{2}
\]

and for `0<=sigma<=1`

\[
\mathcal E^f_{H,\sigma}(K)
:=
\sum_{k\le K}\frac{|\mathcal B_H^f(k)|^2}{k^{2\sigma}}.
\tag{3}
\]

For every fixed `c>0`, put `K=floor(c sqrt(H))`. Then, as `H->infinity`,

\[
\boxed{
\mathbb E\,\mathcal E^f_{H,\sigma}(K)
=
H^{2-\sigma+o(1)}
}
\tag{4}
\]

in logarithmic-exponent sense for every fixed `0<=sigma<=1`. More quantitatively, for `0<=sigma<1`,

\[
H K^{2-2\sigma}
\ll_{c,\sigma}
\mathbb E\,\mathcal E^f_{H,\sigma}(K)
\ll_{\sigma,\varepsilon}
H K^{2-2\sigma+\varepsilon},
\tag{5}
\]

while at `sigma=1`,

\[
H\log K
\ll_c
\mathbb E\,\mathcal E^f_{H,1}(K)
\ll_\varepsilon H K^\varepsilon.
\tag{6}
\]

Thus the random-multiplicative second-moment exponent is

\[
\boxed{\gamma_{\rm RMF}(\sigma)=2-\sigma,}
\qquad
\boxed{\gamma_{\rm RMF}(\sigma)+\sigma=2.}
\tag{7}
\]

This is exactly the noncritical line found in `FD-196`. In particular, at the half-Sobolev weight,

\[
\boxed{
\mathbb E\,\mathcal E^f_{H,1/2}(c\sqrt H)
=
H^{3/2+o(1)},
}
\tag{8}
\]

whereas the `FD-196` RH-facing target is

\[
\mathcal E_{H,1/2}(c\sqrt H)=O_\varepsilon(H^{1+\varepsilon}).
\tag{9}
\]

So an `H^(1+epsilon)` theorem for the physical Möbius source would require a genuine half-power suppression relative not only to the classical Franel norm comparison but also to the natural multiplicative random-sign second moment. Generic multiplicativity plus random-phase/square-root-cancellation heuristics do not supply that gain.

This does **not** show that (9) is false for Möbius. The ensemble randomizes the prime values, whereas the physical source has the coherent deterministic choice `mu(p)=-1`. Equation (4) is a benchmark for what multiplicativity and pairwise sign orthogonality alone produce, not a lower bound for deterministic Möbius and not a claim about typical realizations beyond the stated second moment.

## 1. Exact covariance after the Farey divisor transform

For squarefree `m,n`, independence of the prime signs gives

\[
\mathbb E[f(m)f(n)]
=
\mathbf 1_{m=n}.
\]

Including nonsquarefree integers, where `f` vanishes, this is

\[
\boxed{
\mathbb E[f(m)f(n)]
=
\mu(n)^2\mathbf 1_{m=n}.
}
\tag{10}
\]

Expand the same divisor transform used by the physical Farey coefficients:

\[
\mathcal B_H^f(k)
=
\sum_{n\le H}w_{H,k}(n)f(n),
\qquad
w_{H,k}(n)
:=
\sum_{\substack{d\mid k\\ d\le H/n}}d.
\tag{11}
\]

The weights are nonnegative. By (10), all cross terms disappear exactly, so

\[
\boxed{
\mathbb E|\mathcal B_H^f(k)|^2
=
\sum_{n\le H}\mu(n)^2 w_{H,k}(n)^2.
}
\tag{12}
\]

This is an exact source-covariance identity, not an independence approximation after applying the Farey transform.

## 2. Matching lower and upper exponents

If `n<=H/k`, every divisor of `k` is active in (11). Hence

\[
w_{H,k}(n)=\sigma_1(k)\ge k.
\tag{13}
\]

Let

\[
Q(x):=\sum_{n\le x}\mu(n)^2.
\]

The classical squarefree-density estimate gives `Q(x)=x/zeta(2)+o(x)`. Uniformly for `k<=c sqrt(H)`, the quantity `H/k` tends to infinity, so for all sufficiently large `H`,

\[
\mathbb E|\mathcal B_H^f(k)|^2
\ge
Q(H/k)\sigma_1(k)^2
\gg_c Hk.
\tag{14}
\]

For the reverse bound, Cauchy--Schwarz inside (11) gives

\[
w_{H,k}(n)^2
\le
\tau(k)
\sum_{\substack{d\mid k\\ d\le H/n}}d^2.
\tag{15}
\]

Summing first over `n`, using only `mu(n)^2<=1`, yields

\[
\begin{aligned}
\mathbb E|\mathcal B_H^f(k)|^2
&\le
\tau(k)\sum_{d\mid k}d^2\left\lfloor\frac Hd\right\rfloor\\
&\le
H\tau(k)\sigma_1(k).
\end{aligned}
\tag{16}
\]

Since `sigma_1(k)/k=sigma_{-1}(k)<=tau(k)` and the classical divisor bound gives `tau(k)=k^{o(1)}`, for every `epsilon>0`,

\[
\frac{\mathbb E|\mathcal B_H^f(k)|^2}{k^{2\sigma}}
\ll_\varepsilon
H k^{1-2\sigma+\varepsilon}.
\tag{17}
\]

Combining (14) and (17), then summing `k<=K`, proves (5). At `sigma=1` the lower sum is harmonic and the same subpower upper bound gives (6). Taking `K asy sqrt(H)` proves (4) and (7).

At the critical half-Sobolev weight, the calculation is especially transparent:

\[
\frac{\mathbb E|\mathcal B_H^f(k)|^2}{k}
=H^{1+o(1)}
\]

in the exponent sense uniformly over the square-root band, and there are `Theta(sqrt(H))` such modes. Their positive quadratic energies therefore accumulate at exponent `3/2`.

## 3. Consequence for the `FD-196` frontier

`FD-196` showed that merely reweighting the classical Franel energy leaves a half-power gap: the inherited exponent is `gamma=2-sigma`, while RH-scale Mertens recovery needs `gamma<=3/2-sigma`. The present calculation shows that `2-sigma` is also the exact logarithmic exponent of the random-multiplicative ensemble mean.

This sharpens the interpretation of the gap. A future proof of the critical estimate cannot be justified by saying that multiplicativity should make the square-root-band modes behave like generic random signs. The standard multiplicative random-sign model already has exact prime-factor multiplicativity and squarefree support, yet its quadratic Farey energy lands on the wrong side of the phase diagram by precisely `H^(1/2)`.

The remaining possible source of that suppression is therefore genuinely Möbius-specific: coherent use of the fixed prime phase `mu(p)=-1`, deterministic divisor compatibility across modes or horizons, or another arithmetic identity absent from the randomized prime-sign ensemble. This is a barrier to a class of heuristics, not a barrier to the physical theorem.

## 4. Representation audit

The benchmark is source-native in the relevant sense. The randomization is imposed on prime coordinates before any Farey/divisor transform, and the source remains exactly multiplicative on squarefree integers. Equation (12) then propagates its true covariance through the same raw transform `mathcal B_H` used for Möbius. No inverse, lossy projection or ill-conditioned coordinate change is introduced to manufacture the `H^(2-sigma)` scale.

The boundary is equally important. The model does **not** preserve the physical prime values: it randomizes them. Thus the finding says that squarefree multiplicativity and second-order random cancellation are insufficient to beat the `FD-196` line. It does not say that the deterministic Möbius phase cannot create extra cancellation, and it does not convert an ensemble expectation into a typical-realization theorem.

A useful exact reformulation is that the deficit already exists in the covariance geometry of the multiplicative source. Any successful `H^(1+epsilon)` half-Sobolev estimate must use information beyond that covariance geometry.

## 5. Prior-art and formalization gates

Rademacher random multiplicative functions supported on squarefree integers are standard probabilistic models for multiplicative functions and for Möbius-type cancellation. Harper, *Moments of Random Multiplicative Functions, I* (Forum of Mathematics, Pi 8 (2020), e1, DOI `10.1017/fmp.2019.7`) uses exactly this model and records the same pairwise orthogonality mechanism for ordinary partial sums. The present theorem is instead the direct second-moment calculation after the Farey divisor transform and its comparison with the weighted recovery line of `FD-196`. The targeted prior-art search found no direct treatment of this Farey weighted-band energy. The external reference is contextual rather than load-bearing because (10)--(17) give the complete calculation, so `SOURCES.md` is unchanged.

No formalization issue is opened. The reusable finite core is elementary probability plus a divisor-sum estimate, while the substantive conclusion is the asymptotic comparison with the `FD-196` Fourier phase diagram. Formalizing it would require probability/source infrastructure disproportionate to the additional structural coverage.
