# MC-172 — Gallagher localization identifies the signed near-diagonal heat energy

**Status:** `LITERATURE+EXACT-DERIVED`, `CLASSICAL-GALLAGHER-MECHANISM`, `FRONTIER-REDUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

The finite-time heat orbit of `MC-169`–`MC-171` admits a classical but previously unused localization that identifies a precise arithmetic quantity between phase-blind stationary statistics and the RH-equivalent anchored heat bound.

For a prime-phase vector

\[
z=(z_p)_p\in\mathbb T^{\mathcal P},
\qquad
\chi_z(n)=\prod_p z_p^{v_p(n)},
\]

set

\[
a_{\beta,z}(n)
:=\mu(n)^2\chi_z(n)e^{-\beta(\log n)^2},
\qquad
\Theta_z(\beta,t)
:=\sum_{n\ge1}a_{\beta,z}(n)n^{-it}.
\tag{1}
\]

The true Möbius phase is `z_p=-1` for every prime, so `a_{\beta,z}(n)=\mu(n)e^{-\beta(\log n)^2}`; the all-plus square-free control is `z_p=1`.

For `T>=1`, define the multiplicative short-interval energy

\[
\boxed{
\mathcal G_z(\beta,T)
:=
T\int_0^\infty
\left|
\sum_{y<n\le y e^{1/T}}a_{\beta,z}(n)
\right|^2\frac{dy}{y}.
}
\tag{2}
\]

Then three exact facts hold.

First, Gallagher's classical Dirichlet-series lemma gives

\[
\boxed{
V_z(\beta,T)
:=\frac1{2T}\int_{-T}^{T}|\Theta_z(\beta,t)|^2dt
\ll \mathcal G_z(\beta,T),
}
\tag{3}
\]

with an absolute implied constant after fixing the standard Gallagher parameter. Thus a finite spectral time mean is controlled by a genuinely local signed Möbius quadratic statistic, without analytic continuation of `1/zeta`.

Second, `(2)` has the exact near-diagonal expansion

\[
\boxed{
\mathcal G_z(\beta,T)
=
\sum_{m,n\ge1}
 a_{\beta,z}(m)\overline{a_{\beta,z}(n)}
\left(1-T\left|\log\frac mn\right|\right)_+.
}
\tag{4}
\]

Consequently

\[
\mathcal G_z(\beta,T)
=D(\beta)+\mathcal C_z(\beta,T),
\tag{5}
\]

where

\[
D(\beta)=\sum_{n\ge1}\mu(n)^2e^{-2\beta(\log n)^2}
\tag{6}
\]

is exactly the phase-blind diagonal from `MC-170`–`MC-171`, while `\mathcal C_z` is a signed correlation of distinct integers whose logarithms differ by less than `1/T`. The local energy is nonnegative by `(2)`, but its off-diagonal part retains prime orientation rather than squaring it away.

Third, Haar-randomizing the prime phases kills every off-diagonal term exactly:

\[
\boxed{
\int_{\mathbb T^{\mathcal P}}
\mathcal G_z(\beta,T)\,dm_\infty(z)
=D(\beta).
}
\tag{7}
\]

So the diagonal is not merely a convenient normalization: it is the exact independent-prime-phase baseline of this local energy.

For the all-plus phase and an exponential time horizon

\[
T_\beta=e^{\tau/\beta},
\qquad \tau\ge0,
\tag{8}
\]

the energy has the sharp exponential type

\[
\boxed{
\lim_{\beta\downarrow0}
\beta\log \mathcal G_+(\beta,T_\beta)
=
\max\left(\frac18,\frac12-\tau\right).
}
\tag{9}
\]

Hence the same `tau=3/8` boundary found in `MC-171` has an arithmetic short-interval meaning. Below `3/8`, coherent phase can lift the Gallagher energy exponentially above its random-phase diagonal baseline; above `3/8`, even the all-plus control has only diagonal exponential type.

This identifies a concrete live intermediate question for the true Möbius phase:

\[
\boxed{
\limsup_{\beta\downarrow0}
\beta\log \mathcal G_\mu
\!\left(\beta,e^{\tau/\beta}\right)
\le \frac18
\quad\text{for some fixed }0<\tau<\frac38?
}
\tag{10}
\]

Equation `(10)` is **not claimed to be equivalent to RH or to imply a new Mertens exponent**. It is instead a phase-sensitive local-variance target that is strictly different in form from the RH-equivalent fixed-time heat condition of `MC-169`, while `(3)` proves exactly what finite-time spectral information it would buy. The decisive next step is to determine whether `(10)`, or a quantitatively weaker version with a useful exponent gap, is accessible from Möbius short-interval/correlation machinery without importing an RH-equivalent estimate.

## 1. Gallagher's lemma gives the local energy directly

Gallagher's 1970 lemma concerns an absolutely convergent exponential sum

\[
S(t)=\sum_\nu s(\nu)e^{2\pi i\nu t}.
\]

In the Dirichlet-series specialization recorded explicitly by Coppola and Laporta (`MC-S43`), one takes

\[
\nu=\frac{\log n}{2\pi}
\]

and obtains

\[
\int_{-T}^{T}
\left|\sum_n a_n n^{it}\right|^2dt
\ll
T^2\int_0^\infty
\left|\sum_{y<n\le y e^{1/T}}a_n\right|^2\frac{dy}{y}.
\tag{11}
\]

For every fixed `beta>0`, the coefficients in `(1)` are absolutely summable, so `(11)` applies without truncation. Replacing `t` by `-t` does not change the `L^2` norm. Divide `(11)` by `2T` and use `(2)` to obtain `(3)`.

The point of `(3)` is directional. Gallagher gives a sufficient arithmetic quantity for controlling the finite-time orbit; no reverse inequality is asserted here. In particular, a small `V_z` does not by itself prove a small `\mathcal G_z`.

## 2. Exact triangular correlation kernel

Absolute convergence also permits expansion of `(2)`. For fixed positive integers `m,n`, both terms occur in the local sum precisely when

\[
y<\min(m,n),
\qquad
\max(m,n)\le y e^{1/T}.
\]

The logarithmic measure of the allowed `y` interval is therefore

\[
\int
\mathbf 1_{\{y<m,n\le y e^{1/T}\}}
\frac{dy}{y}
=
\left(\frac1T-\left|\log\frac mn\right|\right)_+.
\tag{12}
\]

Multiplying by the outer `T` in `(2)` proves `(4)`.

This formula exposes the information carrier precisely. The kernel

\[
K_T(u)=(1-T|u|)_+
\tag{13}
\]

keeps only pairs with multiplicative separation

\[
e^{-1/T}<m/n<e^{1/T},
\]

but unlike an absolute correlation budget it retains the signed phase

\[
\chi_z(m)\overline{\chi_z(n)}.
\]

The diagonal `m=n` contributes exactly `(6)`. Everything that can distinguish the true all-minus Möbius phase from a support-matched phase deformation is therefore isolated in `\mathcal C_z`.

This is a different quotient from the stationary averaging in `MC-170`. There, exact time resonance forced equal prime-exponent vectors and erased the starting phase. Here, finite time replaces exact resonance by the triangular logarithmic neighborhood `(13)`, so near-diagonal phase relations survive.

## 3. Random prime phases give the diagonal exactly

For Haar-independent prime phases,

\[
\int \chi_z(m)\overline{\chi_z(n)}\,dm_\infty(z)=0
\]

unless

\[
v_p(m)=v_p(n)
\qquad\text{for every prime }p.
\]

Unique factorization then forces `m=n`. Averaging `(4)` over the prime torus therefore removes every off-diagonal pair and proves `(7)`.

Thus `D(beta)` is an exact matched-control benchmark. A bound of diagonal order for the true Möbius phase would not merely say that a quadratic statistic is small; it would say that the deterministic all-minus prime orientation suppresses the entire near-diagonal energy down to the mean level of arbitrary independent prime phases.

This still must not be called randomness of Möbius. Equation `(7)` is a control identity, not evidence that the true phase behaves randomly.

## 4. The all-plus control recovers the `3/8` phase-washout boundary

Put

\[
b_\beta(n)=\mu(n)^2e^{-\beta(\log n)^2}.
\]

For the all-plus phase all terms in `(4)` are nonnegative. Let

\[
N_T(n)
=
\#\left\{m\ge1:\left|\log\frac mn\right|<\frac1T\right\}.
\]

For `T>=1`, elementary interval length gives

\[
N_T(n)\ll 1+\frac nT.
\tag{14}
\]

Using `2b_m b_n<=b_m^2+b_n^2`, symmetry, `0<=K_T<=1`, and `(14)`,

\[
\mathcal G_+(\beta,T)
\ll
\sum_n b_\beta(n)^2\left(1+\frac nT\right)
=
D(\beta)+\frac{E(\beta)}T,
\tag{15}
\]

where

\[
E(\beta)
:=
\sum_{n\ge1}n\mu(n)^2e^{-2\beta(\log n)^2}.
\tag{16}
\]

The square-free counting law used in `MC-170`–`MC-171` gives

\[
\lim_{\beta\downarrow0}\beta\log D(\beta)=\frac18,
\qquad
\lim_{\beta\downarrow0}\beta\log E(\beta)=\frac12.
\tag{17}
\]

Therefore `(15)` gives

\[
\limsup_{\beta\downarrow0}
\beta\log\mathcal G_+(\beta,e^{\tau/\beta})
\le
\max\left(\frac18,\frac12-\tau\right).
\tag{18}
\]

For the reverse exponential inequality, `MC-171` proves

\[
\lim_{\beta\downarrow0}
\beta\log V_+(\beta,e^{\tau/\beta})
=
\max\left(\frac18,\frac12-\tau\right).
\tag{19}
\]

Gallagher `(3)` implies `V_+\ll\mathcal G_+`, so `(19)` supplies the matching lower exponential type. This proves `(9)`.

The arithmetic meaning of the finite-time threshold is now explicit. The large-time Montgomery--Vaughan estimate of `MC-171` expressed the competition as `D(beta)` versus `E(beta)/T`; Gallagher localization identifies the same competition as diagonal variance versus signed multiplicative short-interval coherence.

## 5. Scale geometry: `tau=3/8` corresponds to `X^(1/4)` windows

The coherent off-diagonal term `E(beta)/T` has its Gaussian saddle at

\[
\log X_\beta=\frac1{2\beta}.
\tag{20}
\]

At this scale,

\[
T_\beta=e^{\tau/\beta}=X_\beta^{2\tau},
\]

and Gallagher's multiplicative interval has additive length

\[
H_\beta
\asymp
\frac{X_\beta}{T_\beta}
=
X_\beta^{1-2\tau}.
\tag{21}
\]

Thus

\[
\tau=\frac38
\quad\Longleftrightarrow\quad
H_\beta\asymp X_\beta^{1/4}.
\tag{22}
\]

For every `0<tau<3/8`, the unresolved phase-sensitive heat regime corresponds at the coherent saddle to multiplicative windows longer than `X^(1/4)`. This does **not** mean that an `X^(1/4)` pointwise short-interval theorem would solve the problem; the required currency is the signed quadratic energy `(2)`, not only an entrywise magnitude bound.

The 2026 almost-all theorem `MC-S2` illustrates the distinction. In its applicable range it supplies, outside a controlled exceptional set,

\[
\left|\sum_{x<n\le x+H}\mu(n)\right|
\ll_A \frac{H}{(\log X)^A}.
\tag{23}
\]

For polynomial `H`, squaring the retained bound gives

\[
\frac{H^2}{(\log X)^{2A}},
\tag{24}
\]

whereas a random-phase/diagonal local-variance budget is of order `H`. Their ratio

\[
\frac{H}{(\log X)^{2A}}
\]

still diverges by a power of `X`. Hence even before paying for exceptional intervals, `(23)` as a black-box magnitude statement does not imply the square-root second-moment scale needed to force `(2)` down to its diagonal benchmark. This is the quadratic counterpart of the absolute local-to-global loss in `MC-001`, but now attached to the exact finite-time heat observable rather than to a generic dyadic sum.

For the particular coherent-saddle windows `(21)`, the `MC-S2` threshold `H>=X^(1/3+epsilon)` corresponds to

\[
\tau\le\frac13-\frac\epsilon2.
\tag{25}
\]

So modern almost-all technology reaches a genuine portion of the sub-washout geometric range, but its published relative log-saving magnitude scale is still exponentially too weak for the diagonal Gallagher-energy target.

## 6. Prior-art and novelty audit

The central transform is classical. Gallagher (`MC-S42`) introduced the mean-square exponential-sum inequality in 1970. Coppola and Laporta (`MC-S43`) state the Dirichlet-series specialization `(11)` explicitly, derive weighted/Cesàro versions, and describe the right-hand quadratic means as Selberg-integral-type tools for short intervals. **No novelty is claimed for Gallagher localization, the triangular kernel, Selberg-type short-interval variance, or their general relationship to Dirichlet-polynomial mean values.**

A targeted search for Möbius short-interval variance found substantial short-interval cancellation literature but no unconditional number-field result at the square-root variance scale required by `(10)`. The closest exact variance analogue found in the audit is Keating and Rudnick (`MC-S44`) for Möbius sums over `F_q[t]`, where short-interval variances can be calculated in a function-field limit using unitary matrix integrals. That result is an analogue and control, not evidence for the integer Möbius estimate proposed here.

The line-specific contribution is therefore an **information-budget reduction**, not a new theorem of analytic number theory: specializing Gallagher to the already canonical heat orbit, expanding the local quadratic form exactly, calibrating it against prime-phase controls, and showing that its exponential phase boundary is precisely the `3/8` horizon of `MC-171`.

This audit also separates the present object from earlier correlation findings. `MC-039`–`MC-041` classified qualitative/logarithmically weighted fixed-complexity correlation information and its Tauberian losses. The kernel `(13)` instead couples a growing family of *multiplicatively near-diagonal* pairs at a scale tied directly to the heat time horizon. A proposed theorem about `(10)` must be audited on its own hypotheses rather than treated as another name for Chowla.

## 7. Boundaries and falsification controls

The reduction is useful only with its limitations kept explicit.

- Gallagher `(3)` is one-sided. A finite-time mean-square estimate does not automatically bound `\mathcal G_z` in reverse.
- A bound such as `(10)` is not shown here to imply RH, pointwise Mertens cancellation, or the fixed-`t` heat estimate of `MC-169`.
- The local energy uses the heat-weighted coefficients and a multiplicative window whose length varies with `y`; replacing it by one fixed unweighted short-interval theorem requires a justified dyadic/weight transfer.
- `\mathcal G_z` is a quadratic magnitude after the local signed sum. It preserves pairwise orientation but may still discard higher-order structure needed for an anchored pointwise theorem.
- The Haar identity `(7)` is only a matched phase control. It does not license probabilistic independence assumptions for Möbius.
- The all-plus calculation proves that support alone can generate the larger `1/2-tau` type. A useful Möbius theorem must distinguish the actual all-minus prime law from this control.
- The exact-support residue-biased multiplicative comparators of `MC-005`/`MC-039` also correspond to fixed prime-phase vectors. Any proposed general principle such as "nonpretentious phases have diagonal Gallagher energy" must be tested against those comparators rather than assumed Möbius-specific.
- Current almost-all bounds of size `H/log^A X` are not square-root-variance estimates. Exceptional-set improvements alone cannot repair the good-window information-class gap in `(24)`.

The decisive falsification test for this route is now concrete: choose a fixed `tau<3/8` and either prove a Möbius-specific bound giving a strict exponential gain over the all-plus type in `(9)`, ideally down to `1/8`, or construct a matched arithmetic phase satisfying the proposed input hypotheses whose Gallagher energy retains the larger coherent type. Only after such a gain exists is it worth testing whether the resulting finite-time `L^2` control transfers further toward an anchored Mertens/RH statement.

## Consequence for the research line

`MC-169` showed that the source-forced fixed-time heat orbit reaches RH exactly. `MC-170` showed that stationary scalar statistics wash the phase out completely. `MC-171` located the finite-time transition at `tau=3/8` but left the sub-washout arithmetic mechanism unidentified.

`MC-172` fills that structural gap without claiming new cancellation: **the missing finite-time currency is a Gallagher/Selberg-type signed near-diagonal Möbius energy.** Its diagonal is the exact random-prime-phase baseline; its coherent all-plus excess reproduces the `3/8` boundary; and existing logarithmic short-interval magnitude theorems do not supply the square-root local-variance budget needed to control it.

The next high-value question is therefore no longer "find another heat statistic." It is to decide whether the true Möbius phase has quantitatively suppressed Gallagher energy on any genuinely sub-washout horizon, and, if so, which arithmetic theorem supplies that suppression without already encoding RH.