# RE-101 — pair-kernel second moments close the sparse-host tail and break 173/200

**Status:** `EXACT-DERIVED + DEFORMED-QUADRATIC-SPARSE-HOSTS + DIRECT-PAIR-KERNEL-SECOND-MOMENT + KUSMIN-LANDAU-NEAR-SHIFTS + VAN-DER-CORPUT-FAR-SHIFTS + BOURGAIN-DENSITY-HYPOTHESIS + BOURGAIN-HIGH-SIGMA-DENSITY + FULL-SAMPLED-HOST-SAVING + 173/200-FRONTIER-BROKEN + PRIOR-ART-AUDITED`.

`RE-100` relocates the unresolved sampled-host problem to the high-beta part of the zeta zero sum. Its trigonometric large-sieve second moment pays the full frequency-span factor `T`, and with Bourgain's density-hypothesis bound this stops at `sigma_*(vartheta)~0.814--0.815`. The natural question is whether that `T` factor is intrinsic once the zero set becomes thin.

It is not. Expanding the **same second moment directly into zero pairs** exposes the difference frequency

\[
\Delta=\gamma-\gamma'.
\]

On the deformed quadratic sample of `RE-096`, small `|Delta|` are controlled by the same Kusmin--Landau mechanism already present in Bazzanella's fixed-power argument, while large `|Delta|` admit a second-derivative van der Corput bound. The resulting pair-kernel estimate replaces the large-sieve cost `T N(sigma,T)` by

\[
\boxed{
M N(\sigma,T)+T^{1/2}N(\sigma,T)^2,
\qquad M=X^{1/2}.
}
\tag{1}
\]

In Bourgain's density-hypothesis range this is strong enough throughout every fixed strip `25/32<sigma<=15/16`. Bourgain's earlier high-sigma density estimate then makes the remaining `beta>=15/16` contribution uniformly `o(H)` in absolute value. Hence the residual high-beta tail of `RE-100` closes with existing theorems: for every fixed

\[
\frac{1901}{5216}<\vartheta<\frac{73}{200}
\]

there is a fixed `delta(vartheta)>0` such that the complete two-sided bad-host set of `RE-096` satisfies

\[
\boxed{
\#\mathcal Z_\vartheta(X)
\ll X^{1/2-\delta(\vartheta)+o(1)}.
}
\tag{2}
\]

Combining (2) with `RE-095` therefore lowers the mixed first/depth-two Robin frontier strictly below `173/200`. An explicit balanced choice gives

\[
\boxed{
\Theta>
\frac{265657}{307200}
=0.8647688802\ldots
}
\tag{3}
\]

for that channel, improving `173/200=0.865` by exactly

\[
\boxed{
\frac{71}{307200}
=0.00023111979\ldots .
}
\tag{4}
\]

This is a numerical improvement of the **residual mixed first/depth-two frontier**, not a proof of RH and not a claim that the other Robin channels automatically inherit the same exponent.

## 1. Direct pair expansion gives a two-regime sample kernel

Keep the exact explicit-formula setup of `RE-100`:

\[
M=X^{1/2},\qquad
H=X^\vartheta,\qquad
T=\frac XH(\log X)^3=X^{1-\vartheta+o(1)},
\tag{5}
\]

and

\[
x(n)=\eta_1^{-1}(\eta_2(n)),
\qquad n\asymp M.
\tag{6}
\]

For a real-part slab

\[
I_\sigma=
\left[\sigma,\sigma+\frac1{\log X}\right]
\]

write, exactly as in `RE-100`,

\[
F_\sigma(n)
=
\int_0^H
\sum_{\substack{|\gamma|\le T\\\beta\in I_\sigma}}
(x(n)+u)^{\rho-1}\,du.
\tag{7}
\]

The left-hand interval is identical with `-H<=u<=0`. Put

\[
t_{n,u}=\log(x(n)+u).
\]

`RE-096` gives

\[
\frac{d}{dn}\log x(n)
=\frac2n\left(1+O((\log n)^{-2})\right),
\qquad
\frac{d^2}{dn^2}\log x(n)
=-\frac2{n^2}\left(1+O((\log n)^{-2})\right).
\tag{8}
\]

Because `H=o(X)`, the same derivative scales hold uniformly for `t_{n,u}` on `|u|<=H`. For a zero pair define

\[
\Delta=\gamma-\gamma',
\qquad
K_u(\Delta;J)
:=
\sum_{n\in J}e^{i\Delta t_{n,u}},
\tag{9}
\]

where `J` is any subinterval of the host shell. Uniformity in `J` is useful because the small real-part weights are removed by partial summation.

Choose a sufficiently small fixed `c>0`. If

\[
1\le|\Delta|\le cM,
\]

then the normalized first derivative of the phase stays inside `(-1/2,1/2)` and has distance `asymp |Delta|/M` from the nearest integer. Kusmin--Landau therefore gives

\[
\boxed{
|K_u(\Delta;J)|
\ll \frac{M}{|\Delta|}.
}
\tag{10}
\]

For `|Delta|<1`, the trivial `O(M)` bound has the same combined form `M/(1+|Delta|)`.

If instead

\[
cM<|\Delta|\le2T,
\]

then (8) gives a second derivative of constant sign and size

\[
|\Delta|M^{-2}
\]

throughout the shell. The standard second-derivative van der Corput estimate yields

\[
|K_u(\Delta;J)|
\ll
|\Delta|^{1/2}+M|\Delta|^{-1/2}.
\tag{11}
\]

Here `T<M^2` because `vartheta>0`, while `T>M` because `vartheta<1/2`. Consequently throughout the far range

\[
\boxed{
|K_u(\Delta;J)|
\ll T^{1/2}X^{o(1)}.
}
\tag{12}
\]

No pair-correlation statement about zeta zeros is being used: (10)--(12) are deterministic sample-kernel bounds.

## 2. Local zero counts make the near pairs linear, while the far pairs may remain quadratic

Let

\[
N_\sigma:=N(\sigma,T)
\]

and let `B_j` count slab zeros with ordinate in `[j,j+1)`. The Riemann--von Mangoldt formula gives

\[
B_j\ll\log T.
\tag{13}
\]

For an integer difference bin `h`, the number of ordered zero pairs whose ordinates differ by `h+O(1)` is at most

\[
\sum_j B_jB_{j+h+O(1)}
\ll N_\sigma\log T.
\tag{14}
\]

Combining (10), (13)--(14), and the harmonic sum over `|h|<=cM` gives

\[
\sum_{|\Delta|\le cM}|K_u(\Delta)|
\ll
M N_\sigma X^{o(1)}.
\tag{15}
\]

For the far pairs we deliberately assume no spacing or additive-energy improvement at all. There are at most `N_sigma^2` ordered pairs, so (12) gives

\[
\sum_{cM<|\Delta|\le2T}|K_u(\Delta)|
\ll
T^{1/2}N_\sigma^2X^{o(1)}.
\tag{16}
\]

The real-part weights inside one `1/log X` slab vary by only a bounded factor across the physical shell, and their total variation in `n` is `O(1/log X)`. Partial summation therefore preserves (15)--(16) up to `X^{o(1)}`. Expanding the square at fixed `u`, then using Cauchy in the exact integral (7), yields

\[
\boxed{
\sum_{n\asymp M}|F_\sigma(n)|^2
\ll
H^2X^{2\sigma-2}
\left(
M N_\sigma+T^{1/2}N_\sigma^2
\right)X^{o(1)}.
}
\tag{17}
\]

This is the promised replacement for the `T N_sigma` large-sieve term of `RE-100`. A bad sampled interval forces some non-negligible slab to have `|F_sigma(n)|>=H X^{-o(1)}`, so Markov gives

\[
\boxed{
\#\mathcal Z_{\vartheta,\sigma}(X)
\ll
X^{2\sigma-2}
\left(
M N_\sigma+T^{1/2}N_\sigma^2
\right)X^{o(1)}.
}
\tag{18}
\]

The distinction between the two terms is useful: local zero multiplicity/spacing is enough to keep near pairs essentially linear in `N_sigma`, while the far term is allowed to pay the full `N_sigma^2` because second-derivative oscillation supplies `T^{1/2}` instead of the full sample length.

## 3. Bourgain's density-hypothesis range closes the finite high-beta strip

For

\[
\sigma\ge\frac{25}{32},
\]

Bourgain's 2000 density-hypothesis theorem gives

\[
N_\sigma
\ll
T^{2(1-\sigma)+o(1)}.
\tag{19}
\]

Write

\[
q=1-\sigma,
\qquad
\tau=1-\vartheta.
\]

Substituting (19) into the two terms of (18), their host-count exponents are

\[
\boxed{
E_{\rm near}
=\frac12-2\vartheta q,
}
\tag{20}
\]

and

\[
\boxed{
E_{\rm far}
=\frac\tau2+q(4\tau-2).
}
\tag{21}
\]

On the compact strip

\[
\frac{25}{32}<\sigma\le\frac{15}{16},
\]

the near exponent is largest at `sigma=15/16`, where

\[
E_{\rm near}
\le
\frac12-\frac\vartheta8.
\tag{22}
\]

Since `vartheta<1/2`, the coefficient `4tau-2` in (21) is positive, so the far exponent is largest at the bottom of the strip. With `q=7/32`,

\[
E_{\rm far}
\le
\frac{15-22\vartheta}{16}
=
\frac12-\frac{22\vartheta-7}{16}.
\tag{23}
\]

For every `vartheta>1901/5216`, both savings in (22)--(23) are fixed and very large compared with the narrow lower-strip margin of `RE-100`. Thus the pair-kernel second moment overlaps the Guth--Maynard range immediately above `25/32`; there is no longer any handoff at `sigma_*(vartheta)~0.815`.

The endpoint `25/32` itself may be assigned to the lower-strip estimate of `RE-100`; all statements here can be made on compact subintervals with an arbitrarily small overlap, so no endpoint uniformity is being smuggled into (19).

## 4. The remaining beta >= 15/16 tail is uniformly too small to create a bad host

A polynomial host-count estimate is not needed arbitrarily close to `beta=1`. It is enough to show that this part of the truncated explicit formula contributes `o(H)` to **every** sampled interval.

Bourgain's 1995 Corollary 4 gives, in modern zero-density notation,

\[
\boxed{
A(\sigma)
\le
\frac4{30\sigma-25},
\qquad
\frac{15}{16}\le\sigma<1.
}
\tag{24}
\]

Hence throughout this range

\[
A(\sigma)\le\frac{32}{25}.
\tag{25}
\]

For the whole admissible Robin window `vartheta>1901/5216`, we have

\[
1-(1-\vartheta)\frac{32}{25}
>
1-\left(1-\frac{1901}{5216}\right)\frac{32}{25}
=
\frac{152}{815}>0.
\tag{26}
\]

Now bound this tail in absolute value. Partial summation in the real parts of the zeros, using (24) in its standard uniform form, gives for `y asymp X`

\[
\sum_{\substack{|\gamma|\le T\\\beta\ge15/16}}
y^{\beta-1}
\ll
(\log X)^{O(1)}
\exp\!\left(-c\,\eta(T)\log X\right),
\tag{27}
\]

where `eta(T)` is any classical Korobov--Vinogradov zero-free width. Indeed every density slice carries the factor

\[
X^{\sigma-1}T^{A(\sigma)(1-\sigma)}
\le
\exp\!\left(
-\frac{152}{815}(1-\sigma)\log X+o((1-\sigma)\log X)
\right),
\tag{28}
\]

while the zero-free region forces `1-sigma >= eta(T)` whenever the slice actually contains a zero. Since `eta(T) log X -> infinity`, (27) is `o(1)`.

Using the exact integral representation again,

\[
\left|
\sum_{\substack{|\gamma|\le T\\\beta\ge15/16}}
\frac{(x(n)+H)^\rho-x(n)^\rho}{\rho}
\right|
\le
\int_0^H
\sum_{\substack{|\gamma|\le T\\\beta\ge15/16}}
(x(n)+u)^{\beta-1}\,du
=o(H)
\tag{29}
\]

uniformly in `n`; the left interval is identical. This uses no cancellation among the high-beta zeros. The only role of the high-sigma density theorem is to make their **absolute weighted mass** summable against the physical factor `X^(beta-1)` before the zero-free edge is reached.

Thus a prime-free sampled interval must obtain its fixed-proportion explicit-formula deficit from the slabs below `15/16`, where Sections 2--3 and `RE-100` already give polynomial host savings.

## 5. The sampled-host theorem now gives an explicit sub-173/200 Robin frontier

It remains to identify the smallest saving across the full lower strip. `RE-100` shows that on `[1/2,7/10]` the Ingham range has threshold at most `7/20`, well below the present window. On `[7/10,25/32]` the Guth--Maynard exponent is worst at `sigma=25/32`. At that endpoint

\[
A\!\left(\frac{25}{32}\right)
\le\frac{480}{221},
\qquad
1+A\!\left(\frac{25}{32}\right)\frac7{32}
=\frac{326}{221}.
\tag{30}
\]

Put

\[
\vartheta_0:=\frac{1901}{5216}.
\]

The endpoint exponent in `RE-100` equals exactly `1/2` at `vartheta=vartheta_0`, and for larger `vartheta` it is

\[
\frac12-
\frac{326}{221}(\vartheta-\vartheta_0).
\tag{31}
\]

The Guth--Maynard exponent is increasing in `sigma` on this interval, so (31) is the worst lower-strip slab. Equations (22)--(23) have much larger fixed margins, and (29) eliminates the remaining tail. Therefore the **complete** sampled bad-host set satisfies

\[
\boxed{
\#\mathcal Z_\vartheta(X)
\ll
X^{1/2-\delta_0(\vartheta)+o(1)},
\qquad
\delta_0(\vartheta)
=
\frac{326}{221}
\left(
\vartheta-rac{1901}{5216}
\right).
}
\tag{32}
\]

for every fixed `vartheta_0<vartheta<73/200`. The union over `O(log X)` real-part slabs is absorbed by the `X^{o(1)}` factor. By `RE-096`, the prime-host set required by `RE-095` is a subset of this integer-host set, so it inherits (32).

`RE-095` then gives the mixed first/depth-two false-RH frontier

\[
\Theta>
\max\!\left(
\frac12+\vartheta,
\frac{173}{200}-\frac{\delta_0(\vartheta)}2
\right).
\tag{33}
\]

Balancing the two terms gives the explicit admissible choice

\[
\boxed{
\vartheta
=
\frac{112057}{307200}
=0.3647688802\ldots,
}
\tag{34}
\]

for which

\[
\delta_0
=
\frac{71}{153600}.
\tag{35}
\]

Both terms of (33) then equal

\[
\boxed{
\frac{265657}{307200}
=
\frac{173}{200}-\frac{71}{307200}
=0.8647688802\ldots,
}
\tag{36}
\]

which proves (3)--(4).

## 6. Adversarial checks and prior-art boundary

The kernel argument was stress-tested in the regimes most likely to hide a false gain. Near zero difference, no separation between individual zeta ordinates is assumed: unit-bin occupancy `B_j<<log T` alone gives (14), including multiplicities. In the far range, no zero-pair cancellation is assumed at all: the proof pays the full `N_sigma^2`. The second-derivative estimate is valid because `M<|Delta|<=2T<M^2X^{o(1)}` in the present `0<vartheta<1/2` range. The slowly varying real-part amplitudes are handled by partial summation using bounds uniform on every partial host interval. Finally, the very-high-beta argument deliberately takes absolute values, so its conclusion does not depend on an unproved sign or pair-correlation phenomenon.

The matched fixed-power control also clarifies the novelty boundary. Bazzanella's 2009 paper already expands a **second moment** over zero pairs and applies Kusmin--Landau to the phase `(gamma-gamma') log n`; this is direct prior art for (10), not a Mathia novelty. In that direct branch, however, the paper imposes

\[
H(N)\gg N^{1-1/\alpha}f(N)\log^2N,
\]

which for `alpha=2` is above the square-root scale. When the interval is shorter, its proof changes architecture, and its published quadratic threshold is `13/32`. The new line-specific splice is to keep the second moment below that first-derivative range, use the stable **second derivative** of the exact CA-deformed phase for `|Delta|>>M`, and combine the resulting `T^(1/2)N^2` term with modern zero density. A targeted search found no published theorem stated for the CA-deformed sequence or this exact near/far pair-kernel splice.

Bourgain's 2000 theorem remains the load-bearing finite-strip density input already recorded by `RE-100`. The additional load-bearing high-sigma input is Jean Bourgain, *Remarks on Halasz-Montgomery Type Inequalities*, Geometric Aspects of Functional Analysis (Israel, 1992--1994), Operator Theory: Advances and Applications **77** (1995), 25--39, Corollary 4; the corresponding IHES preprint is `IHES/M/93/51`. Its bound (24) is used only to dispose of the absolute `beta>=15/16` tail, not to claim any new zero-density theorem.

## Research consequence

The live target recorded after `RE-100` was to close only the residual high-beta sampled-host tail. Equations (17)--(29) do so with existing analytic inputs. Therefore the sparse-host theorem itself is no longer the active obstruction for this Robin channel: it supplies a polynomial saving on the full explicit-formula range and, through `RE-095`, pushes the mixed first/depth-two scalar frontier below `173/200`.

The next useful question is no longer a high-beta zeta-zero estimate. It is to return to the **other surviving Robin channels / selector constraints** and determine which frontier is now globally dominant after the mixed first/depth-two channel has moved to (36). Because Research Watch is not allowed to rewrite `mind/**`, this finding records that consequence canonically without modifying the line-mind state.