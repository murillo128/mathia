# WI-007 — support one is exactly the screening threshold for cross-scale depth detection

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for the route that tries to break WI-006 by adding any finite family of Alpöge--Furman-type compressions whose window supports all remain at or below Fourier support one. The Poisson/Gabor aliasing mechanism is classical, and Alpöge--Furman already identify support `>1` as the arithmetic threshold where prime-pair information enters. The new consequence here is the exact bridge between those two facts: on the WI-006 screening lattice, **horizontal depth is absent from every subcritical compression and reappears only through nonzero Poisson aliases, whose first possible contribution occurs when the window support crosses the support-one boundary.**

## 1. Question left open by WI-006

WI-006 showed that, for the Alpöge--Furman critical window of length

\[
L=\log(T/2\pi),
\qquad
h=\frac{2\pi}{L},
\]

a full vertical lattice of simple off-line mirror pairs

\[
\frac12+\delta+it_j,
\qquad
\frac12-\delta+it_j,
\qquad
t_j=t_0+jh,
\]
produces exactly the same compressed Weil operator as a lattice of on-line double zeros at the same ordinates. Long finite blocks are asymptotically equivalent in normalized trace norm.

That left a natural escape route: use a second compression at another scale. Perhaps two critical lattices cannot be aligned simultaneously, so a cross-scale observable might retain the horizontal displacement that the original scale erases.

There is an exact obstruction to this idea for every **shorter or equal** window. The relevant threshold is not whether the auxiliary sample grid is different. It is whether its time support crosses the dual-lattice spacing `L` of the adversarial zero configuration.

## 2. General alias formula for an auxiliary window

Fix the screening lattice

\[
t_j=t_0+j\frac{2\pi}{L},
\qquad j\in\mathbb Z.
\tag{1}
\]

Let `g` be any real even compactly supported window with

\[
\operatorname{supp}g\subset[-H/2,H/2].
\tag{2}
\]

The auxiliary compression may use **arbitrary real sampling frequencies** `alpha_k`; they do not need to equal the original Alpöge--Furman grid and do not need spacing `2pi/L`. For a finitely supported real coefficient vector `x=(x_k)`, set

\[
X(u):=\sum_k x_k e^{i\alpha_k u},
\tag{3}
\]

and

\[
c_{j,\delta}(x)
:=\sum_k x_k\widehat g(t_j-i\delta-\alpha_k).
\tag{4}
\]

With the Fourier convention of Alpöge--Furman,

\[
\widehat g(z)=\int_{\mathbb R}g(u)e^{-izu}\,du,
\]
so

\[
c_{j,\delta}(x)
=\int g(u)e^{-it_j u}e^{-\delta u}X(u)\,du.
\tag{5}
\]

Up to the common positive normalization used in the compressed Weil matrix, the mirror-pair quadratic form at `t_j` is

\[
2\operatorname{Re}\bigl(c_{j,\delta}(x)^2\bigr),
\tag{6}
\]
while an on-line double at the same ordinate is the case `delta=0`.

Summing (6) over the lattice and using

\[
\sum_{j\in\mathbb Z}e^{-ij(2\pi/L)s}
=L\sum_{m\in\mathbb Z}\delta(s-mL)
\tag{7}
\]
gives the exact identity

\[
S_\delta(x)
=2L\operatorname{Re}
\sum_{m\in\mathbb Z}
 e^{-it_0mL}e^{-\delta mL}A_m(x),
\tag{8}
\]
where

\[
A_m(x)
:=\int_{\mathbb R}
 g(u)g(mL-u)X(u)X(mL-u)\,du.
\tag{9}
\]

Because `g` is real even and `x,alpha_k` are real,

\[
A_{-m}(x)=\overline{A_m(x)}.
\tag{10}
\]

Writing

\[
y:=\delta L,
\]
pairing `m` with `-m` in (8), and subtracting the double-zero case therefore yields

\[
\boxed{
S_\delta(x)-S_0(x)
=4L\sum_{m\ge1}
\bigl(\cosh(my)-1\bigr)
\operatorname{Re}\!\left(e^{-it_0mL}A_m(x)\right).
}
\tag{11}
\]

Equation (11) is the exact depth ledger. **Every dependence on horizontal displacement is carried by nonzero Poisson aliases.**

## 3. Every support-`<=1` auxiliary scale is exactly blind

The support condition (2) forces

\[
A_m(x)=0
\qquad\text{whenever}\qquad |m|L\ge H,
\tag{12}
\]
up to measure-zero endpoint contact, which vanishes for the tapered windows used by Alpöge--Furman.

Hence, if

\[
\boxed{H\le L,}
\tag{13}
\]
all `m != 0` terms vanish and (11) gives

\[
\boxed{
S_\delta(x)=S_0(x)
\qquad
\text{for every real }\delta,
\text{ every real sample set }\{\alpha_k\},
\text{ and every real }x.
}
\tag{14}
\]

Thus the WI-006 replacement symmetry is **not** tied to reusing the same critical sample grid. A second compression may have a different bandwidth, a different critical spacing, a shifted grid, or an arbitrary finite real frequency set: if its window support remains inside an interval of length `L`, the full screened lattice still produces exactly the same quadratic form for off-line pairs and on-line doubles.

Equivalently, an arbitrary finite family

\[
\{g_r:\operatorname{length}(\operatorname{supp}g_r)\le L\}_{r=1}^R
\tag{15}
\]
is jointly blind to the replacement. Cross-window mixed statistics built only from those individual compressed operators cannot recover a difference that is identically zero operator-by-operator.

This strictly strengthens the obstruction in WI-006, which only asserted blindness for windows at the same critical bandwidth/grid.

## 4. The first supercritical alias carries horizontal depth explicitly

Now suppose

\[
L<H<2L.
\tag{16}
\]

Only `m=0, +/-1` can contribute. Formula (11) becomes

\[
\boxed{
S_\delta(x)-S_0(x)
=4L\bigl(\cosh y-1\bigr)
\operatorname{Re}\!\left[
 e^{-it_0L}
 \int g(u)g(L-u)X(u)X(L-u)\,du
\right].
}
\tag{17}
\]

The horizontal depth has therefore not disappeared mysteriously. It is stored in an **alias channel** coupling the two pieces of the window separated by exactly one dual-lattice period `L`.

The overlap supporting that channel is

\[
\Omega_1
=
\operatorname{supp}g
\cap
\bigl(L-\operatorname{supp}g\bigr),
\tag{18}
\]
whose length is at most `H-L` for an interval-supported window. At `H=L` the overlap collapses and the depth signal vanishes exactly. For a macroscopic extension

\[
H=(1+\varepsilon)L,
\qquad \varepsilon>0\text{ fixed},
\tag{19}
\]
the alias region has length `epsilon L`, so an order-one normalized depth channel is available for ordinary bounded rescaled windows. By contrast, if `H=L+O(1)`, only an `O(1)` boundary layer overlaps while the main window has `Theta(L)` mass; for the nondegenerate bounded Alpöge--Furman window class this is only a vanishing fraction of the natural normalized bulk observable.

For still larger support, (11) shows exactly what happens: the `m`-th horizontal-depth harmonic appears when `H>mL`, weighted by

\[
\cosh(my)-1.
\tag{20}
\]

So the screening symmetry has a complete alias hierarchy rather than an all-or-nothing failure.

## 5. The zero-side alias threshold coincides with the prime-side arithmetic barrier

For an Alpöge--Furman-type explicit-formula test, a window of support length `H` produces products supported in `[-H,H]`, so the natural prime cutoff is

\[
X=e^H.
\tag{21}
\]

With the baseline

\[
L=\log(T/2\pi),
\]
write `H=lambda L`. Then

\[
X=(T/2\pi)^\lambda.
\tag{22}
\]

Alpöge--Furman explicitly analyze `0<lambda<1` in Remark 6.1 and obtain no improvement of the constant. Equation (14) gives a zero-side reason that is stronger and more specific for the WI-006 extremizer: **every such subcritical scale remains exactly blind to horizontal depth on the screening lattice.**

To make the first alias occupy a nonvanishing fraction of the window one needs

\[
\lambda>1
\quad\text{by a fixed amount}.
\tag{23}
\]

But then

\[
X=(T/2\pi)^{1+\varepsilon}\gg T,
\tag{24}
\]
and Alpöge--Furman §7.2 identify precisely this regime as the point where the off-diagonal prime sum is no longer dominated by the diagonal. Its evaluation requires prime-pair information of Hardy--Littlewood / Montgomery pair-correlation type, equivalently information beyond Fourier support one.

Thus the two barriers coincide:

\[
\boxed{
\begin{array}{c}
\text{zero side: first order-one depth-sensitive Poisson alias}\\[2mm]
\Updownarrow\\[2mm]
\text{support crosses }1\\[2mm]
\Updownarrow\\[2mm]
\text{prime side: off-diagonal prime-pair information becomes load-bearing.}
\end{array}
}
\tag{25}
\]

This is not merely a numerical coincidence of constants. Both thresholds are the same support boundary in the explicit formula, read from opposite sides.

## 6. Long finite screening blocks remain subcritically indistinguishable

The exact identities above use the full lattice. WI-006 already established that, for a long block `J` of `M` consecutive screening centers and fixed bounded normalized depth `y`, replacing the full lattice by `J` costs only a sublinear boundary term in trace norm for the Alpöge--Furman `C^2` windows.

The same localization argument applies to every fixed `H/L<=1`. The zero lattice spacing `2pi/L` is then at least as dense as the critical sampling needed by a window of length `H`, and the shifted windows `g(u)e^{-delta u}` retain uniform Bessel bounds for bounded `y`. Together with the same `|widehat g(s)|=O(|s|^{-2})` decay, the boundary discrepancy remains `o(M)`.

Consequently a macroscopic finite block of screened off-line pairs and the corresponding on-line doubles are asymptotically indistinguishable **simultaneously at every fixed finite collection of subcritical scales**. The full-lattice equality (14) is therefore not an artifact that disappears as soon as the zeta zero count forces occupied blocks and gaps.

This finite-block statement inherits the same scope as WI-006: it is a falsifier for what the currently used zero-side information can distinguish, not a claim that actual zeta zeros form such blocks.

## 7. Prior art and novelty audit

No novelty is claimed for Poisson aliasing or painless Gabor-frame diagonalization.

- Alpöge--Furman Lemma 2.1 proves the no-alias Poisson--Gabor identity at `h=2pi/L` for windows supported in an interval of length `L`.
- Daubechies--Grossmann--Meyer and the subsequent painless Gabor-frame literature treat the general phenomenon that sufficiently dense sampling relative to compact window support makes the frame operator diagonal/multiplicative.
- Alpöge--Furman Remark 6.1 already studies shorter `lambda<1` windows, while §7.2 states that pushing the prime length past `T` / Fourier support past one requires prime-pair information. Classical Goldston--Montgomery theory identifies the same support-`>1` regime with prime-pair/short-interval information.

A bounded novelty search found no source formulating the specific replacement-symmetry consequence (11)--(25) for off-critical Weil mirror pairs versus critical-line doubles. Absence of a search hit is not evidence of novelty. The durable contribution here is the exact **scope classification**: the seemingly plausible multiscale escape from WI-006 fails throughout the entire support-one region, and the first zero-side mechanism that can see horizontal depth is exactly the mechanism whose prime-side evaluation demands new arithmetic input.

## 8. Research consequence

The permanent double/off-line replacement test from WI-006 can now be strengthened.

A proposed discriminator based on this compressed-Weil/Gabor architecture fails automatically if every window it uses satisfies

\[
H\le L.
\]

Changing grid spacing, shifting the grid, combining several shorter scales, or taking richer spectral functions of those matrices does not help: the underlying operators are already equal on the full screening lattice and asymptotically equal on long finite blocks.

The first viable escape routes are therefore narrower than WI-006 suggested:

1. **cross support one by a nonvanishing amount**, and pay for genuinely new prime-pair / pair-correlation information;
2. prove vertical zero statistics strong enough to forbid the long screening blocks before Poisson averaging can erase depth;
3. construct a non-averaged/per-zero observable that retains `delta` without collapsing onto the `u+v=0` Poisson diagonal;
4. find arithmetic information that couples scales before each individual compression loses the horizontal coordinate.

The key structural lesson is

\[
\boxed{
\text{support }\le1
\Longrightarrow
\text{screening is an exact gauge for horizontal depth};
\qquad
\text{support }>1
\Longrightarrow
\text{depth appears as aliasing, but prime pairs enter.}
}
\tag{26}
\]

This does not improve the unconditional `0.6725...` proportion by itself. It does identify, exactly rather than heuristically, why a free multiscale refinement cannot do so and where genuinely new information must enter.