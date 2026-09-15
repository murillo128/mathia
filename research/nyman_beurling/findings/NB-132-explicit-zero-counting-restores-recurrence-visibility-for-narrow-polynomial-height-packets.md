# NB-132 — explicit zero counting restores recurrence visibility for narrow polynomial-height packets

**Status:** `DERIVED + SOURCE-SPECIFIC + EXPLICIT-ZERO-COUNTING + OFF-CRITICAL-SYMMETRY + SHORT-BAND-RANK-BOUND + RECURRENCE-VISIBILITY + NB-124/NB-130-SEPARATOR + POSITIVE-ROUTE-NARROWING + PRIOR-ART-AUDITED`.

`NB-130` and `NB-131` expose a serious formal obstruction: at any fixed natural cutoff `R`, a rank-`R` zero-power packet can interpolate arbitrary data on `1,...,R`, can be packed into an arbitrarily narrow ordinate band, and can then be translated to arbitrarily large height without any extra height-conditioning cost. That obstruction is deliberately source-free. It does not require the support points to be zeros of `zeta`.

For genuine zeta zeros, narrow packets at polynomial height cannot have that rank. The explicit zero-counting error already anchored in `SOURCES.md`, combined with off-critical functional-equation symmetry, forces only logarithmically many right-half-plane zero states into a fixed-width ordinate band. In an explicit parameter range this logarithmic rank is smaller than the geometric sample depth `log_q R`, so the recurrence that was intentionally hidden in `NB-130` becomes visible again and the stable annihilator certificate of `NB-124` applies.

## Claim

Fix an integer `q>=2`, constants `A>0` and `W>0`, and assume

\[
A\left(\frac{W}{4\pi}+0.10076\right)
<
\frac1{\log q}.
\tag{1}
\]

Then there is `R_0=R_0(q,A,W)` such that for every integer `R>=R_0` the following holds.

Let `F` be any finite multiset of **genuine nontrivial zeros of the Riemann zeta function**

\[
\rho=\beta+i\gamma,
\qquad
\beta>\frac12,
\tag{2}
\]

whose positive ordinates lie in one half-open interval

\[
T<\gamma\le T+W,
\qquad
T+W\le R^A,
\tag{3}
\]

with each zero used no more often than its true zeta multiplicity. Let `d(F)` be the resulting total confluent rank. Then

\[
\boxed{
 d(F)+1\le \log_q R,
}
\tag{4}
\]

and hence

\[
\boxed{
 R\ge q^{d(F)+1}.
}
\tag{5}
\]

Consequently the `q`-geometric recurrence of the packet is visible inside the natural cutoff, and the weighted annihilator certificate of `NB-124` applies. In particular, such a packet cannot perfectly capture the harmonic target: its packet space has a strict packet-specific target-angle gap.

The point is not that `d(F)=O(\log R)` abstractly. The point is that the explicit leading coefficient can be put **below the recurrence-visibility threshold** `1/log q`.

## Derivation

### 1. Off-critical symmetry halves the available zero count

Let

\[
D_+(T,W)
:=
\sum_{\substack{\zeta(\rho)=0\\
                  \Re\rho>1/2\\
                  T<\Im\rho\le T+W}}
 m(\rho),
\tag{6}
\]

where `m(rho)` is the true multiplicity. If `rho=beta+i gamma` is a zero with `beta>1/2`, then functional-equation symmetry and conjugation give the distinct zero

\[
1-\overline\rho=(1-\beta)+i\gamma
\tag{7}
\]

with the same multiplicity and the same positive ordinate. Therefore, writing `N(x)` for the usual positive-ordinate zero-counting function counted with multiplicity,

\[
\boxed{
2D_+(T,W)
\le
N(T+W)-N(T).
}
\tag{8}
\]

Critical-line zeros only enlarge the right-hand side, so they cause no problem. Since `F` uses only genuine right-half zeros and respects true multiplicity,

\[
d(F)\le D_+(T,W).
\tag{9}
\]

This is the source-specific restriction absent from the formal Vandermonde packets of `NB-130`.

### 2. Insert the explicit zero-counting error

The Bellotti--Wong--Fiori estimate already recorded in `SOURCES.md` gives, for large positive `x`,

\[
\left|
N(x)-M(x)
\right|
\le E(x),
\tag{10}
\]

where

\[
M(x)
=
\frac{x}{2\pi}\log\frac{x}{2\pi e},
\qquad
E(x)
=
0.10076\log x
+0.24460\log\log x
+8.08344.
\tag{11}
\]

Hence

\[
N(T+W)-N(T)
\le
M(T+W)-M(T)+E(T+W)+E(T).
\tag{12}
\]

For bounded `T`, the interval contains only finitely many zeros, so (4) is automatic once `R` is large enough. We may therefore work in the high-`T` range. Since

\[
M'(x)=\frac1{2\pi}\log\frac{x}{2\pi},
\tag{13}
\]

and `T+W<=R^A`, fixed `A,W` give

\[
\frac12\bigl(M(T+W)-M(T)\bigr)
\le
\frac{AW}{4\pi}\log R+O_{A,W}(1).
\tag{14}
\]

The explicit error contributes

\[
\frac12\bigl(E(T+W)+E(T)\bigr)
\le
0.10076\,A\log R
+0.24460\log\log R
+O_A(1).
\tag{15}
\]

Combining (8)--(15),

\[
\boxed{
 d(F)
\le
A\left(\frac{W}{4\pi}+0.10076\right)\log R
+0.24460\log\log R
+O_{A,W}(1).
}
\tag{16}
\]

Under (1), the leading coefficient in (16) is strictly smaller than `1/log q`. The `log log R` and constant terms can therefore be absorbed for all sufficiently large `R`, giving (4) and (5).

### 3. The hidden recurrence is now inside the observed depth

For a packet of total confluent rank `d`, its primitive samples on the `q`-geometric grid obey an order-`d` confluent recurrence. `NB-124` shows that once the natural cutoff reaches

\[
R\ge q^{d+1},
\tag{17}
\]

the recurrence annihilator is an admissible weighted dual certificate. Because every off-critical packet root has modulus strictly larger than the missing harmonic root `q^{-1}`, the certificate has a nonzero missing-root margin and forces a strict target-angle gap.

Equation (5) is exactly (17). Thus the actual-zero source law closes the loophole that made the formal `NB-130` packet invisible: a narrow polynomial-height zeta packet does not have enough rank to postpone its recurrence beyond the available geometric depth.

## Explicit dyadic corollary

For `q=2` and linear height `A=1`, condition (1) becomes

\[
W
<
4\pi\left(\frac1{\log2}-0.10076\right)
=
16.863253\ldots.
\tag{18}
\]

Therefore every fixed right-half-plane zeta packet contained in an ordinate interval of width, say, `W=1` below height `R` is eventually recurrence-visible on the dyadic grid. Numerically, its leading rank coefficient from (16) is only

\[
\frac1{4\pi}+0.10076
=0.180337\ldots,
\tag{19}
\]

whereas the dyadic visibility budget is

\[
\frac1{\log2}=1.442695\ldots.
\tag{20}
\]

The constants are not optimized. Their role is to show an explicit nonempty regime, with substantial slack, in which actual-zero geometry defeats the formal linear-rank construction.

## Matched formal control

The matched control is `NB-130`. For the same cutoff `R`, any fixed real part `beta in (1/2,1)`, any height, and **any prescribed fixed width `W>0`**, it constructs `R` formal support points inside that band and exactly interpolates arbitrary natural-prefix data on `1,...,R`. The packet has rank `R`, so its recurrence starts far beyond the visible `O(log R)` geometric depth. `NB-131` then translates that support arbitrarily high while keeping the exact prefix fixed after re-solving the coefficients.

The present result proves that this particular control is not source-faithful in the regime (1)--(3): genuine zeta zeros can supply only the logarithmic rank (16), and that rank is low enough for `NB-124` to see the recurrence. This is a genuine separation between formal finite interpolation and actual-zero geometry, not another source-free packet inequality.

The control also identifies the load-bearing limits. If the height is allowed to be exponential in `R`, then `log T` is already of order `R`, so global zero counting no longer prevents a fixed-width interval from carrying rank comparable with `R`. Likewise, if `W` grows too quickly, the main-term contribution `W log T` can consume the recurrence budget. **Polynomial height and sufficiently narrow ordinate width are therefore essential to this gate.**

## Adversarial stress tests

The following failure modes were checked before canonicalization.

First, multiplicities do not evade the count: `N(T+W)-N(T)` and `D_+(T,W)` both count true multiplicity, and the symmetry partner has the same multiplicity. Second, zeros on the critical line do not invalidate (8); they only increase the total zero count while not contributing to `D_+`. Third, the half-open interval `(T,T+W]` matches the difference of zero-counting functions and avoids an endpoint double-counting convention.

Fourth, the result is not merely the one-zero multiplicity argument of `NB-112`. That finding bounded the multiplicity of one off-critical zero. Here the same explicit source law is used to bound the **total confluent rank across an entire multi-ordinate packet**, then compared with the recurrence depth required by `NB-124`. Fifth, the conclusion does not assume that the zeros are separated; arbitrarily tight clustering is already included because the count is with multiplicity and the annihilator is confluent.

Finally, (16) does **not** produce a Burnol-scale quantitative gap. The `NB-124` missing-root margin and annihilator coefficient norm can still deteriorate as the packet changes with `R`. This finding restores recurrence visibility and rules out exact formal interpolation in the stated actual-zero regime; it does not claim a uniform `Omega(1/R)` target defect.

## Prior-art audit

The load-bearing external estimate is the Bellotti--Wong--Fiori explicit zero-counting bound already anchored in `SOURCES.md`, so no source-file update is needed. The standard functional-equation/conjugation symmetry is also already used in `NB-112`.

A targeted audit for Nyman--Beurling arguments combining short ordinate-band zero counts with geometric power-sum recurrence visibility did not locate this splice in the literature. Classical and recent zero-counting work controls the number of zeta zeros; recurrence/Prony-type interpolation controls finite exponential sums; the line-local contribution here is to use the former as the missing source-specific **rank cap** that activates the existing `NB-124` dual certificate and invalidates the `NB-130` formal matched control in a concrete polynomial-height regime.

## Route consequence

`NB-130`--`NB-131` showed that finite natural-prefix data alone cannot distinguish formal high-rank support from vanishing Burnol mass. `NB-132` identifies one place where actual zeta geometry does distinguish them: **narrow packets at polynomial height cannot carry enough confluent rank to hide their recurrence past the natural cutoff.**

The next obstruction is therefore sharper. Inside this regime, the problem is no longer recurrence invisibility; it is quantitative conditioning of the visible annihilator. A useful next theorem would have to turn actual-zero location, spacing, or coefficient structure into a lower bound on the `NB-124` missing-root margin relative to its weighted coefficient norm at the Burnol scale. Outside this regime, especially at superpolynomial heights or growing ordinate widths, rank visibility itself remains open.