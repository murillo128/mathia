# Finding

**ID:** RE-192

**Status:** `EXACT-DERIVED + EULER-SPECTRAL-CONDITIONING + LOG-SOURCE-WIDTH + FACTORIAL-LOW-RANK + SOURCE-INFORMATION-BOUND + PRIOR-ART-BOUNDED`

**Research line:** `robin_extremal`

## Claim

For a finite signed ordinary-prime packet supported on a source interval

\[
Q_-\le q\le Q_+,
\qquad 2\le Q_-\le Q_+,
\]

write

\[
D(s):=\sum_q c_q\log(1-q^{-s})^{-1},
\qquad
V:=\sum_q\frac{|c_q|}{q},
\]

and observe the one-sided Euler profile on

\[
1\le s=1+u\le1+U.
\]

Let

\[
W:=\log\frac{Q_+}{Q_-},
\qquad
R:=UW.
\]

Normalize by the lower support edge,

\[
(\mathcal E_{U,Q_-,Q_+}c)(u)
:=Q_-^uD(1+u),
\qquad 0\le u\le U.
\]

For every integer `m>=1`, define

\[
x_q:=\log\frac q{Q_-}\in[0,W],
\qquad
\nu_k(c):=\sum_q\frac{c_q}{q}x_q^k,
\]

and

\[
(\mathcal R_m c)(u)
:=\sum_{k=0}^{m-1}\frac{(-u)^k}{k!}\nu_k(c).
\]

Then `rank(R_m)<=m` and

\[
\boxed{
\|\mathcal E_{U,Q_-,Q_+}-\mathcal R_m\|_{\ell^1(q^{-1})\to L^\infty[0,U]}
\le
\frac{R^m}{m!}+\frac{2}{Q_-}.
}
\tag{1}
\]

Thus the robust scalar information in an Euler interval is controlled by the single dimensionless product

\[
\boxed{
R=(\text{spectral span})\times(\text{logarithmic source width})
=U\log(Q_+/Q_-).
}
\tag{2}
\]

In particular, a source packet may span polynomially separated scales without producing growing stable rank if the spectral window shrinks inversely with that logarithmic width. If

\[
Q_-=p^A,
\qquad
Q_+=p^B,
\qquad
U=\frac{T}{\log p},
\]

with fixed `0<A<B` and `T>0`, then

\[
R=T(B-A)
\]

is fixed and the whole exact Euler profile is factorially compressible to a rank bounded independently of `p` at every fixed source-scale tolerance above the `O(p^{-A})` prime-power floor.

## Derivation

The Euler factor is absolutely convergent for real `u>=0`:

\[
\log(1-q^{-1-u})^{-1}
=
q^{-1-u}
+
\sum_{n\ge2}\frac{q^{-n(1+u)}}n.
\tag{3}
\]

After the lower-edge normalization, the first harmonic is exactly

\[
Q_-^u q^{-1-u}
=
\frac1q
\exp\left(-u\log\frac q{Q_-}\right)
=
\frac1q e^{-ux_q}.
\tag{4}
\]

The prime-power completion is uniformly smaller. Since `q>=Q_-`, for `n>=2` and `u>=0`,

\[
Q_-^u q^{-n(1+u)}
=
q^{-n}\exp\{-u(n\log q-\log Q_-)\}
\le q^{-n}.
\]

Hence

\[
Q_-^u
\sum_{n\ge2}\frac{q^{-n(1+u)}}n
\le
\sum_{n\ge2}q^{-n}
\le 2q^{-2},
\]

and therefore

\[
\boxed{
\sup_{0\le u\le U}
\left|
(\mathcal E c)(u)
-
\sum_q\frac{c_q}{q}e^{-ux_q}
\right|
\le
\frac{2V}{Q_-}.
}
\tag{5}
\]

For `0<=ux_q<=R`, Taylor's theorem for `e^{-z}` gives

\[
\left|
e^{-ux_q}
-
\sum_{k=0}^{m-1}\frac{(-ux_q)^k}{k!}
\right|
\le
\frac{R^m}{m!},
\tag{6}
\]

because the magnitude of every derivative of `e^{-z}` on the positive real axis is at most `1`. Multiplying by `|c_q|/q`, summing over the packet, and combining with (5) proves (1).

Equivalently, the approximation numbers satisfy

\[
a_{m+1}(\mathcal E)
\le
\frac{R^m}{m!}+\frac{2}{Q_-}.
\tag{7}
\]

This contains the two recent spectral regimes as endpoints. On a fixed multiplicative selector shell `Q_-=Ap`, `Q_+=Bp`, one has `W=log(B/A)=O(1)`. If `U=o(1)`, then `R=o(1)` and `m=1` gives the reciprocal-mass rank-one collapse of `RE-190`. If `U=Theta(1)`, then `R=Theta(1)` and (7) gives the fixed-window factorial compression of `RE-191`.

The new point is the mixed scaling. For polynomial source support `p^A<=q<=p^B`, the log-width is `W=(B-A)log p`, but sampling only to `U=T/log p` gives the same bounded rectangle `R=T(B-A)`. Therefore **logarithmically separated source scales by themselves do not escape low stable rank when the spectral span shrinks at the reciprocal rate**.

For fixed tolerance `epsilon` above the prime-power floor, (7) also gives a coarse rank budget depending only on `R` and `epsilon`. Using `m!>=(m/e)^m`, any

\[
m\ge\max\{2eR,\log_2(1/\epsilon)\}
\]

makes the first term at most `epsilon`. Thus bounded `R` implies uniformly bounded stable rank. A growing robust source rank through this scalar channel can evade the present bound only if `R->infinity` or if the available arithmetic precision is driven into the factorial/prime-power residual scale.

## Representation audit

The decisive representation is not a derivative jet and not a list of sample values. It is the exact Euler discrepancy in the logarithmic source coordinate

\[
x=\log(q/Q_-).
\]

After multiplying the output by `Q_-^u`, the first Euler harmonic is the finite Laplace kernel `e^{-ux}` on the rectangle `[0,U]x[0,W]`. The only geometric size entering the elementary separated approximation is the rectangle product `UW`.

Ownership is preserved: the coefficients are still the ordinary-prime multiplicity discrepancies `c_q`; no surrogate source is introduced. Signed cancellation is preserved linearly rather than replaced by absolute estimates until the operator norm is taken. Width is explicit through `W`, and the bound is robust for arbitrary finite signed coefficients and arbitrary sampling density. The low-rank mechanism itself is generic finite-Laplace geometry; the line-specific content is that the exact Euler-factor channel reduces to it with a uniform `O(Q_-^{-1})` source-scale remainder.

## Exact or empirical?

Exact and derived. Equations (3)--(7) are deterministic inequalities. No numerical experiment, asymptotic fit, zero statistic, or probabilistic model is used.

## Source dependence

The prime-specific input is modest but real: the observable is the exact Euler-factor discrepancy of an ordinary-prime multiplicity packet, and the `n>=2` prime-power completion supplies the explicit `O(Q_-^{-1})` error relative to `V`. The factorial compression of `e^{-ux}` is generic transform geometry and would hold for any signed measure on a bounded logarithmic interval.

The finding does **not** construct a `{0,1,2}` matched control at this tolerance, does not show that growing `R` is sufficient for Robin leverage, and does not derive a source-native precision theorem. It is an upper bound on robust scalar information, not a lower bound and not a Robin criterion.

## Prior-art audit

A targeted search was run for finite/truncated Laplace transforms, Mellin-to-Laplace logarithmic coordinates, and super-exponential singular/eigenvalue decay. The nearby generic literature is the same family already identified by `RE-191`: Lederman--Rokhlin study the singular system of the truncated Laplace transform, and Bourguiba--Karoui prove super-exponential spectral decay for a weighted finite bilateral Laplace operator. The Mellin/Laplace correspondence under logarithmic change of variables is classical.

No external theorem is load-bearing here: the rank-`m` approximation and its error are proved directly from the Euler expansion and Taylor's theorem. The audit did not locate a prior result phrased as the ordinary-prime Euler-packet bound (1), nor the specific Robin matched-control consequence that polynomial source separation combined with a `1/log p` spectral window still has bounded stable rank. This is a bounded novelty claim about the line-specific reduction, not about finite-Laplace compression itself.

## Literature status

The generic finite-Laplace conditioning phenomenon is established prior art and is not claimed as new. The present contribution is an exact Mathia line lemma that exposes the invariant `U log(Q_+/Q_-)`, unifies `RE-190` and `RE-191`, and removes one apparent multi-scale escape from the scalar frontier. Because the proof imports no load-bearing external result, `SOURCES.md` needs no new durable dependency.

## Caveats

Equation (1) is one-sided on the real half-plane `Re s>=1`; it does not analyze vertical imaginary sampling or continuation through `Re s=1`. It is only an approximation-number upper bound; the true stable rank may be smaller, and no matching lower bound is claimed. Exact continuum data remain source-rigid by analyticity even when their finite-precision stable rank is small. Finally, a fixed spectral span together with polynomial source width gives `R=Theta(log p)`, so genuinely broad support at constant distance is **not** closed by this finding.

## Next experiment

Attack the first regime in which the dimensionless rectangle actually grows: honest ordinary-prime `{0,1,2}` matched controls with `R_p=U_p log(Q_{+,p}/Q_{-,p})->infinity`. The cleanest test is fixed `U>0` with support spanning `p^A` to `p^B`, where `R_p=Theta(log p)`. Determine whether exact/approximate matching at the source-native tolerance can still coexist with a selector-scale Robin excursion and a fixed KV envelope, or whether integer multiplicity, transport across logarithmic scales, or inverse conditioning imposes a new tariff.

## Sources

- `RE-190`, *Shrinking Euler sampling windows collapse to reciprocal-mass rank one*.
- `RE-191`, *Fixed Euler-temperature windows are factorially compressible*.
- R. R. Lederman and V. Rokhlin, *On the Analytical and Numerical Properties of the Truncated Laplace Transform I*, SIAM Journal on Numerical Analysis **53** (2015), 1214--1235, DOI `10.1137/140990681`.
- N. Bourguiba and A. Karoui, *Weighted finite Laplace transform operator: spectral analysis and quality of approximation by its eigenfunctions*, Integral Transforms and Special Functions **29** (2018), 679--698, DOI `10.1080/10652469.2018.1489804`.
