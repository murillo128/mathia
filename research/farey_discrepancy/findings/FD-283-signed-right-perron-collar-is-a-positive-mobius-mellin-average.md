# FD-283 — Signed right Perron collar is a positive Möbius Mellin average

- **Date:** 2026-09-23
- **Status:** proved route-narrowing identity
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** truncated Perron / signed horizontal contour / grouped repair kernel / Möbius Mellin transform / route narrowing
- **Depends on:** FD-281, FD-282
- **Classification:** `EXACT-DERIVED + GROUPED-PERRON-COLLAR + POSITIVE-MELLIN-WEIGHT + COEFFICIENT-SPACE-REDUCTION + ROUTE-NARROWING + PRIOR-ART-BOUNDARY`

## Claim

FD-282 leaves one potentially important escape from its absolute horizontal-collar obstruction: preserve the signs through the horizontal Perron integration and only then take the physical repair norm. On every **strict right subcollar** where the Dirichlet series for `1/zeta(s)` converges absolutely, that escape can be reduced exactly to a coefficient-space Möbius Mellin cancellation problem.

Put

\[
Y:=2Nx,
\qquad
c:=1+\frac1{\log Y},
\tag{1}
\]

fix `eta in (0,1)`, and set

\[
a:=1+\frac{\eta}{\log Y}.
\tag{2}
\]

Thus `1<a<c`. With the grouped kernel from FD-282,

\[
K_s(d):=\sum_{q\mid d}\frac{q^s-(q-1)^s}{s}
       =\sum_{q\mid d}\int_{q-1}^{q}u^{s-1}\,du,
\tag{3}
\]

define the positive-orientation upper-edge integral over this strict subcollar by

\[
J_d^+(a,c;T)
:=
\int_a^c
\frac{N^{\sigma+iT}K_{\sigma+iT}(d)}
     {\zeta(\sigma+iT)}\,d\sigma.
\tag{4}
\]

Then the exact identity is

\[
\boxed{
J_d^+(a,c;T)
=
\sum_{q\mid d}
\int_{q-1}^{q}\frac{du}{u}
\sum_{n\ge1}\mu(n)
 e^{iT\log(Nu/n)}
 W_{a,c}\!\left(\frac{Nu}{n}\right),
}
\tag{5}
\]

where

\[
W_{a,c}(r)
:=
\int_a^c r^\sigma\,d\sigma
=
\begin{cases}
\dfrac{r^c-r^a}{\log r}, & r\ne1,\\[6pt]
c-a, & r=1.
\end{cases}
\tag{6}
\]

For every `r>0`,

\[
\boxed{W_{a,c}(r)>0.}
\tag{7}
\]

Therefore integration in `sigma` does not create a new oscillatory phase for an individual Dirichlet/Mellin mode. Its only effect on that mode is multiplication by a positive radial weight. The oscillation is entirely the coefficient-space character

\[
e^{iT\log(Nu/n)}.
\tag{8}
\]

For a real source, the lower edge is the complex conjugate of the upper edge. With the usual rectangular orientation, the top edge is traversed from `c+iT` to `a+iT` and the bottom edge from `a-iT` to `c-iT`. Hence the paired strict-right horizontal contribution, including the Perron factor `1/(2 pi i)`, is

\[
\boxed{
H_d^{\mathrm{right}}(a,c;T)
=-\frac1\pi\operatorname{Im}J_d^+(a,c;T)
}
\tag{9}
\]

and consequently

\[
\boxed{
H_d^{\mathrm{right}}(a,c;T)
=-\frac1\pi
\sum_{q\mid d}
\int_{q-1}^{q}\frac{du}{u}
\sum_{n\ge1}\mu(n)
\sin\!\left(T\log\frac{Nu}{n}\right)
W_{a,c}\!\left(\frac{Nu}{n}\right).
}
\tag{10}
\]

The overall sign in (9)--(10) is fixed by the stated rectangular orientation; reversing the convention reverses that sign and changes none of the conclusions.

Thus the upper/lower pair does not supply a second independent cancellation mechanism either: it extracts one sine quadrature of the same Möbius Mellin transform. Any power saving over the `Nx` absolute-collar scale of FD-282 on this strict right subcollar must come from cancellation in the Möbius-weighted Mellin sum in (10), or from cancellation between this subcollar and the remaining horizontal portion closer to or left of `Re(s)=1`.

## Derivation

Because `sigma>=a>1`, the reciprocal zeta Dirichlet series is absolutely and uniformly convergent on the closed subcollar:

\[
\frac1{\zeta(s)}
=
\sum_{n\ge1}\frac{\mu(n)}{n^s}.
\tag{11}
\]

Using the integral representation in (3),

\[
N^sK_s(d)
=
\sum_{q\mid d}
\int_{q-1}^{q}(Nu)^s\,\frac{du}{u}.
\tag{12}
\]

The apparent `du/u` singularity at `u=0` is harmless before or after the rearrangement: for `Re(s)>=a>1`, the original integrand has size `O(u^{a-1})`; equivalently the weight in (6) is `O(u^a/|log u|)` as `u` tends to zero. The sum over `n` is absolutely convergent uniformly in `sigma`, so Fubini applies.

Substituting (11)--(12) into (4) gives

\[
J_d^+
=
\sum_{q\mid d}
\int_{q-1}^{q}\frac{du}{u}
\sum_{n\ge1}\mu(n)
\int_a^c
\left(\frac{Nu}{n}\right)^{\sigma+iT}
\,d\sigma.
\tag{13}
\]

For `r>0`,

\[
\int_a^c r^{\sigma+iT}\,d\sigma
=
e^{iT\log r}W_{a,c}(r),
\tag{14}
\]

which proves (5). Since `r^sigma` is positive for real `sigma`, (7) is immediate. Equivalently, in the closed form (6), numerator and denominator have the same sign on either side of `r=1`.

Finally, real coefficients imply

\[
\frac{N^{\sigma-iT}K_{\sigma-iT}(d)}
     {\zeta(\sigma-iT)}
=
\overline{
\frac{N^{\sigma+iT}K_{\sigma+iT}(d)}
     {\zeta(\sigma+iT)}}.
\tag{15}
\]

The oriented sum of the top and bottom strict-right edges is therefore

\[
-J_d^++\overline{J_d^+}
=-2i\operatorname{Im}J_d^+,
\tag{16}
\]

and (9)--(10) follow.

## What this rules out

The clue after FD-282 correctly observes that taking absolute values before the `sigma` integration may destroy cancellation. But on the strict right collar there is no separate large-`T` oscillation *along `sigma`* to exploit. For each fixed coefficient mode `(n,u)`, the phase `T log(Nu/n)` is independent of `sigma`; the `sigma` integral only averages its amplitude with a positive weight.

In particular, integration by parts in `sigma` cannot produce a `1/T` gain from the factor in (8): differentiating with respect to `sigma` never touches that phase. Any gain obtained after carrying out the `sigma` integral exactly is already a statement about cancellation among the different Möbius/Mellin modes.

Likewise, pairing the upper and lower edges does not generically cancel the strict-right collar. It replaces the complex Mellin sum by its imaginary part. At exact resonance `Nu/n=1` the individual mode is real and the paired horizontal contribution of that mode vanishes, but away from resonance the pair retains the sine factor in (10).

The local phase scale near `n=Nu` is informative but not a localization theorem. Since

\[
\frac{d}{dn}
\left[T\log\left(\frac{Nu}{n}\right)\right]
=-\frac{T}{n},
\tag{17}
\]

an order-one phase change near `n\asymp Nu` occurs over

\[
\Delta n\asymp\frac{Nu}{T}.
\tag{18}
\]

This identifies the natural coefficient-space oscillation scale. It does **not** show that terms outside such a window are negligible.

## Weight geometry

The positive weight has no hidden sign change. By the integral mean-value bound,

\[
(c-a)\min(r^a,r^c)
\le
W_{a,c}(r)
\le
(c-a)\max(r^a,r^c).
\tag{19}
\]

Hence on every fixed multiplicative annulus `e^(-A)<=r<=e^A`, the weight is comparable, up to constants depending on `A`, to `(c-a)r` because `a,c=1+O(1/log Y)`. The strict-right collar is therefore a positive smooth radial averaging of the same logarithmic Mellin phases, not an additional source of rapid oscillation.

## Relation to the FD-282 plateau

FD-282 proves a lower bound for an **absolute** grouped right-collar functional by exposing prime self-divisor coordinates. FD-283 does not convert that certificate into a signed lower bound. Equation (10) shows exactly why: once signs are retained, every physical coordinate contains a Möbius-weighted sine sum, and such sums may cancel.

What FD-283 does remove is one proposed source of that cancellation. The phrase "phase varies with sigma" is not the right mechanism on `Re(s)>1` after the absolutely convergent coefficient expansion. The `sigma` dependence is radial and positive mode by mode. Therefore a proof that beats the FD-282 plateau must establish one of two genuinely stronger facts:

1. cancellation in the coefficient-space Möbius Mellin transform in (10), after the exact Farey physical grouping; or
2. cancellation between the strict-right subcollar and the adjoining horizontal segment where the absolutely convergent expansion (11) is no longer available.

The first possibility is close to the line-ownership boundary of `farey_discrepancy`. If the physical kernel can be removed and the remaining estimate is purely a generic Möbius Mellin cancellation statement, that subproblem belongs naturally to `mobius_cancellation` rather than being new Farey geometry. If the divisor-replicated kernel or cross-strip cancellation remains essential, it stays within the present line.

## Stress tests and non-claims

The reduction is intentionally restricted to `a>1`. Sending `a` to `1` requires additional control because the absolutely convergent Dirichlet expansion of `1/zeta(s)` is lost at the boundary. No assertion is made here about the horizontal segment with `Re(s)<=1`, nor about cancellation between that segment and the strict-right collar.

The positivity of `W_{a,c}` does not imply positivity of the full integrated sum. Different coefficient modes carry different phases and may cancel strongly. FD-283 therefore proves neither a lower bound for the signed horizontal contour nor a failure of the hard-Perron route.

Conversely, the identity should not be read as evidence that Möbius cancellation is weak. It only identifies **where** any saving has to live. A sufficiently strong estimate for the sine transform in (10) could still beat the `Nx` certificate scale while keeping `T` inside the cluster-prunable regime.

Generic signed and modified truncated-Perron treatments are classical. In particular, Ramaré's *Modified truncated Perron formulae* (Ann. Math. Blaise Pascal 23 (2016), DOI `10.5802/ambp.356`) develops general formulas relating variations of summatory functions to truncated Perron integrals. No claim of novelty is made for retaining signs in Perron integrals or for the elementary Mellin identity itself. The contribution here is the exact reduction after the specific consecutive-difference/divisor-replication transform used by the Farey repair program.

## Research consequence

The signed-horizontal clue remains live, but its decisive test is narrower than before. On a strict right collar, searching for a `T`-driven cancellation merely from integrating in `sigma`, or from pairing conjugate horizontal edges, cannot by itself cross the FD-261 target. The candidate power saving must be proved as a **Möbius Mellin cancellation estimate in the physical grouped kernel**, or must use cancellation with the part of the contour not covered by absolute convergence.

This is useful route pruning: it prevents spending further effort on an apparent contour-phase mechanism that disappears after exact expansion, while preserving the two channels that can still change the polynomial-depth balance.