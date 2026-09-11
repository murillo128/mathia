# ANF-176 — Endpoint memory has a sharp activation-saving boundary

**Status:** `DERIVED + MATCHED-CONTROL + ACTIVATION-SAVING-PHASE-DIAGRAM + PRIOR-ART-CALIBRATION`. `ANF-175` localized dangerous prime-scale endpoint loading at the critical absolute charge

\[
a_X:=\sqrt{\delta X\log X}
\]

and constructed a carrier-selected packet with total `l^1` mass `O(a_X)` that still forces bow-scale completion. The present finding turns that construction into an activation-versus-saving barrier for any long-interval theorem used only through relative correlation bounds. If an all-interval estimate activates at `H_0=X^(theta+o(1))` and allows error `H X^(-sigma+o(1))`, then the `ANF-175` packet is automatically invisible whenever

\[
\boxed{\theta-\sigma>\frac12.}
\]

The exact boundary is not the exponent alone but whether the theorem's smallest allowed absolute error is below `a_X`. In particular, every fixed logarithmic saving remains blind at every fixed activation exponent `theta>1/2`; at the current `theta=5/8` one needs roughly an `X^(-1/8)` relative power saving, while even a hypothetical exact-carrier theorem activated at the Guth--Maynard prime-counting exponent `17/30` would still need roughly `X^(-1/15)`. Reaching the actual loading scale `H_*=sqrt(X log X)` changes the regime: there any genuine `o(1)` relative saving already falls below the critical charge.

The result is an information-boundary statement, not a claim that a theorem below this boundary automatically closes the physical bow problem. It says that any strategy whose only source input is a relative long-interval estimate above the boundary cannot distinguish the prime-scale matched control from an acceptable source, despite its target-sized endpoint completion and Fejer scale-slope defect.

## 1. General activation-error profile

Keep the bow regime and matched packet of `ANF-175`. Thus

\[
K=X^{1-2\varepsilon+o(1)},
\qquad
0<\varepsilon<\frac1{16},
\qquad
a_X=\sqrt{\delta X\log X},
\tag{1}
\]

and there is a real-amplitude exact-carrier sequence

\[
b_j=c_j(X+j)^{-iU}
\tag{2}
\]

with prime-scale atom size and density, supported in a loading interval of length `Theta(a_X)`, such that

\[
\sum_j |b_j|\ll a_X
\tag{3}
\]

while

\[
E_-(b)\ge (\delta-o(1))XK\log X.
\tag{4}
\]

By `ANF-169` and `ANF-172`, this also forces a target-sized positive real dyadic correlation and an equivalent Fejer scale-slope defect.

Now consider a generic all-interval source theorem whose only downstream use is a bound

\[
\left|\sum_{j\in I} b_jF(j)\right|
\le B_X(|I|)
\tag{5}
\]

for every interval `I` with `|I|>=H_0` and every test in some class satisfying `|F(j)|<=1`. Assume for the moment that the admissible error is monotone at the lower edge, so `B_X(H)>=B_X(H_0)` for `H>=H_0`. The matched packet itself satisfies the stronger deterministic estimate

\[
\sup_{I}\sup_{|F|\le1}
\left|\sum_{j\in I}b_jF(j)\right|
\le \sum_j|b_j|
\ll a_X.
\tag{6}
\]

Therefore the decisive comparison is simply

\[
B_X(H_0)\quad\text{versus}\quad a_X.
\tag{7}
\]

If

\[
\boxed{\frac{B_X(H_0)}{a_X}\to\infty,}
\tag{8}
\]

then the packet obeys (5) with asymptotically vanishing relative slack throughout the theorem range while retaining (4). Such an estimate is structurally blind to the endpoint-memory obstruction. Conversely, if

\[
\boxed{B_X(H_0)=o(a_X),}
\tag{9}
\]

then this particular matched packet can no longer pass the theorem. Equation (9) is only a necessary calibration for eliminating the control, not a sufficient proof for the physical source.

This formulation avoids overinterpreting exponents. Slowly varying factors matter exactly on the boundary; away from it the power comparison decides everything.

## 2. The power phase diagram is `theta-sigma=1/2`

Write the activation and relative saving as

\[
H_0=X^{\theta+o(1)},
\qquad
B_X(H)=H X^{-\sigma+o(1)}.
\tag{10}
\]

At the first controlled scale,

\[
\frac{B_X(H_0)}{a_X}
=
X^{\theta-\sigma-1/2+o(1)}(\log X)^{-1/2}.
\tag{11}
\]

Hence

\[
\boxed{\theta-\sigma>\frac12
\quad\Longrightarrow\quad
B_X(H_0)\gg a_X,}
\tag{12}
\]

and the `ANF-175` matched control is invisible. If `theta-sigma<1/2`, the allowed error is power-smaller than the critical charge and the control is detected. On the critical line `theta-sigma=1/2`, logarithmic and other subpower factors decide the outcome; a bare bound `B_X(H_0)asymp X^(1/2)` is already `o(a_X)` by the factor `sqrt(log X)`.

Equivalently, at a fixed activation scale `H_0`, a relative theorem must reach

\[
\boxed{
\rho_X=o\!\left(\frac{a_X}{H_0}\right)
}
\tag{13}
\]

in order to place its absolute error below the packet's stored charge, where `B_X(H)=rho_X H`. For `H_0=X^theta`, this means

\[
\rho_X=o\!\left(X^{1/2-\theta}\sqrt{\log X}\right).
\tag{14}
\]

This is the quantitative tradeoff hidden by a statement such as “more cancellation above the activation threshold.” Lowering the activation exponent and strengthening the relative saving are interchangeable only through (13).

## 3. Fixed logarithmic savings are powerless at every fixed exponent above one half

Suppose a theorem gives, for every fixed `A>0`,

\[
B_X(H)=H(\log X)^{-A}
\tag{15}
\]

on all intervals `H>=X^theta` with a fixed `theta>1/2`. Then

\[
\frac{B_X(X^\theta)}{a_X}
=
X^{\theta-1/2}(\log X)^{-A-1/2}
\longrightarrow\infty
\tag{16}
\]

for every fixed `A`. Thus **arbitrarily strong fixed-log cancellation does not compensate for any fixed positive power gap above the square-root exponent**.

This sharpens the strategic conclusion of `ANF-175`. The problem is not special to the present `5/8` theorem. Improving `5/8` to any exponent `theta>1/2` while retaining only `H log^{-A}X` errors still leaves the same matched control invisible. The decisive event is either reaching the near-square-root loading scale itself, or acquiring a power saving that moves `(theta,sigma)` across the line `theta-sigma=1/2`.

At the physical loading scale

\[
H_*\asymp a_X\asymp\sqrt{X\log X},
\tag{17}
\]

a genuine relative saving `rho_X=o(1)` gives `rho_XH_*=o(a_X)` immediately. This is why the square-root scale is qualitatively different from every fixed exponent above one half, not merely quantitatively closer to the target.

## 4. Calibration against the current and newest short-interval exponents

The current load-bearing all-interval higher-uniformity theorem of Matomäki--Shao--Tao--Teräväinen activates for the von Mangoldt residual at

\[
H_0=X^{5/8+\eta}
\tag{18}
\]

and gives arbitrary fixed logarithmic saving against fixed-complexity nilsequences. `ANF-173` shows that, after a sufficiently high fixed Taylor approximation, this controls the exact distinguished logarithmic twist throughout the remaining endpoint range once the theorem is activated. In the phase diagram it has `sigma=0`, so its distance from the critical line is

\[
\frac58-\frac12=\frac18.
\tag{19}
\]

A relative power saving of order `X^(-1/8)` at the `5/8` activation scale would make the corresponding absolute error `O(X^(1/2))=o(a_X)`; fixed logarithmic savings cannot.

Guth and Maynard's 2026 large-value work gives asymptotics for primes in ordinary short intervals of length `x^(17/30+o(1))`. That theorem is **not** an exact-carrier estimate for `vartheta-Q_R`, so it cannot be inserted into the bow argument directly. It is nevertheless a useful calibration of how far exponent-only progress can move the boundary. Even a hypothetical source-faithful exact-carrier analogue activated at

\[
\theta=\frac{17}{30}
\tag{20}
\]

would still lie above one half by

\[
\frac{17}{30}-\frac12=\frac1{15}.
\tag{21}
\]

Thus arbitrary fixed-log savings at that activation would remain blind to `ANF-175`; one would need about an `X^(-1/15)` relative power saving, or an equivalent absolute `o(sqrt(X log X))` remainder. The point is not that `17/30` is weak—it is a major improvement for the ordinary short-interval prime problem—but that the bow endpoint consumes a different absolute memory scale.

## 5. Failure boundary and what this does not prove

The phase diagram is deliberately an information-boundary result. It reuses the adversarial prime-scale packet of `ANF-175`, whose sites are selected after seeing the exact carrier. The physical residual does not have that freedom. A source theorem exploiting the actual joint prime/rough placement law could therefore cross the boundary in ways not captured by a generic estimate of the form (5).

Nor does `B_X(H_0)=o(a_X)` by itself prove the final bow bound. The endpoint completion is a sum over many prefixes, and short uncontrolled prefixes still require their own accounting. The claim here is only one-way and sharp for the persisted matched control: if the theorem allowance at its first controlled scale is much larger than the total mass `O(a_X)`, then no argument that sees the source only through that allowance can rule the control out.

The same caveat applies to the Guth--Maynard comparison. Their `17/30` result is used only as an exponent calibration. The needed bow input remains source-faithful cancellation of `vartheta-Q_R` at the distinguished twist, or direct control of the signed dyadic / Fejer scale-slope statistic.

## 6. Prior-art audit

The relevant external anchors are already recorded in `SOURCES.md`. Matomäki--Shao--Tao--Teräväinen provide the all-interval `5/8` higher-uniformity theorem used by `ANF-164` and `ANF-173`. Guth--Maynard provide the 2026 `17/30+o(1)` ordinary short-interval prime consequence of their new Dirichlet-polynomial large-value estimates. Neither source states the activation-saving boundary above; equations (6)--(16) are a deterministic consequence of the Mathia matched control and the absolute bow charge scale.

A targeted audit found no external result that turns an activation exponent alone into control of this endpoint-memory functional. No new source entry is required because both literature anchors are already present and load-bearing in the local source ledger.

## Verdict

The endpoint obstruction has a clean activation-saving phase diagram. For a theorem that begins at `H_0=X^(theta+o(1))` and allows relative error `X^(-sigma+o(1))`, the prime-scale matched control survives whenever `theta-sigma>1/2`. Fixed logarithmic savings correspond to `sigma=0` at the power level, so **every fixed activation exponent above one half remains structurally blind, no matter how many fixed logarithms are gained**.

This changes the frontier from “close the gap between `5/8` and square root” to a more flexible quantitative target: cross `theta-sigma=1/2`. At `5/8`, that means roughly an `X^(-1/8)` relative power saving; at a hypothetical exact-carrier `17/30`, roughly `X^(-1/15)`; at the true loading scale `sqrt(X log X)`, any genuine relative `o(1)` saving is already strong enough to detect the matched packet. Exponent progress above one half and power-saving progress should therefore be evaluated through this single boundary rather than as separate goals.