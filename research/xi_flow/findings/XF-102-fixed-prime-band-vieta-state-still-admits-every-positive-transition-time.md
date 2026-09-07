# XF-102 — fixed prime-band Vieta state still admits every positive transition time

**Status:** `EXACT-DERIVED` + `PRIME-ATOMIC-INTERFACE` + `DECISIVE-NEGATIVE` + `TRANSITION-NONIDENTIFIABILITY` + `INTERFACE-NARROWING`. XF-100 shows that the current `K \asymp q\log\log T` shadow is prime-blind, while XF-101 shows that its entire autonomous Vieta trajectory admits matched periodic controls with every prescribed fixed positive transition time. A natural repair is to enlarge the prefix to the first explicit-formula prime atoms. That repair is still insufficient if the redesigned source interface reduces the arithmetic data to a mesh-scale, fixed-physical-band power-sum prefix.

Fix a physical frequency cutoff

\[
\Lambda_*>\lambda_2:=\frac{\log 2}{2}
\tag{1}
\]

independent of the Xi scale, and set

\[
K_*:=\left\lfloor\frac{\Lambda_*}{\Delta}\right\rfloor,
\qquad
M=q^2,
\qquad
N=2M,
\qquad
\Delta^2\asymp q^{-3}.
\tag{2}
\]

Then `K_* \asymp \Delta^{-1}\asymp q^{3/2}=o(N)`. Let `psi` be any fixed nonnegative smooth bump supported in `[-1,1]` and satisfying

\[
\psi(u)\ge c_\psi>0
\qquad (|u|\le1/2).
\tag{3}
\]

Write `lambda_n=(\log n)/2`. From XF-052 the endpoint arithmetic sector is

\[
-\frac12\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,\delta_{\lambda_n}.
\tag{4}
\]

Instead of illegally point-evaluating this distribution at the prime atoms, test only that atomic sector at mesh scale and retain the exact smooth background `B` from XF-052. Define the raw moment target

\[
\boxed{
Q_m^{\psi}
:=
B(m\Delta)
-\frac1{2\Delta}
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}\,
\psi\!\left(\frac{m\Delta-\lambda_n}{\Delta}\right),
\qquad 1\le m\le K_*.
}
\tag{5}
\]

For every fixed `Lambda_*`, this prime-enriched prefix has a vanishing normalized `ell^1` cost, remains in that cone under the exact periodic heat flow, and therefore still admits the XF-101 collision implantation at every fixed `0<tau<=1/2`. In particular, merely reaching the first prime frequency does **not** repair transition identifiability inside a sublinear autonomous Vieta prefix.

## 1. The mesh-scale arithmetic extraction genuinely sees the first prime

Because `psi` is compactly supported, the sum in (5) is locally finite. Let

\[
m_2:=\operatorname{round}(\lambda_2/\Delta).
\tag{6}
\]

For all sufficiently small `Delta`, one has `1<=m_2<=K_*` and

\[
|m_2\Delta-\lambda_2|\le\frac\Delta2.
\tag{7}
\]

All coefficients in the atomic sector have the same sign and `psi>=0`, so the `n=2` atom alone gives

\[
\boxed{
\left|Q_{m_2}^{\psi}-B(m_2\Delta)\right|
\ge
\frac{c_\psi\log2}{2\sqrt2}\,\Delta^{-1}.
}
\tag{8}
\]

Thus this is not another prime-blind low-band state. It contains an explicit order-`Delta^{-1}` signature of the first prime-power atom, and similarly resolves every fixed finite collection of prime-power frequencies lying in the interior of the physical band.

The construction is intentionally a **distribution-safe source interface**, not a claim that `\mathcal Z_0(\lambda_n)` exists pointwise. Equation (5) pairs the atomic part of XF-052 with a normalized bump of width `Delta`; the background is an ordinary analytic function and is sampled directly.

## 2. A fixed physical prime band still costs only `o(N)` moment mass

On every fixed interval `(0,Lambda_*]`, the explicit background from XF-052 obeys

\[
|B(\xi)|\le C_{\Lambda_*}\left(1+\frac1\xi\right).
\tag{9}
\]

Hence

\[
\sum_{m=1}^{K_*}|B(m\Delta)|
\ll_{\Lambda_*}
K_*+\Delta^{-1}\sum_{m=1}^{K_*}\frac1m
\ll_{\Lambda_*}
\Delta^{-1}\log(\Delta^{-1}+2).
\tag{10}
\]

For the atomic sector, each fixed prime-power atom contributes to at most three integer mesh sites because `supp psi subset [-1,1]`. Moreover only atoms with `lambda_n<=Lambda_*+Delta` can contribute. Their total von Mangoldt weight is a finite constant depending on `Lambda_*`, so

\[
\sum_{m=1}^{K_*}
\left|
\frac1{2\Delta}
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
\psi\!\left(\frac{m\Delta-\lambda_n}{\Delta}\right)
\right|
\ll_{\Lambda_*,\psi}\Delta^{-1}.
\tag{11}
\]

Combining (10) and (11),

\[
\boxed{
\sum_{m=1}^{K_*}|Q_m^{\psi}|
\ll_{\Lambda_*,\psi}
\Delta^{-1}\log(\Delta^{-1}+2).
}
\tag{12}
\]

At the Xi scaling this gives

\[
\boxed{
\frac1N\sum_{m=1}^{K_*}|Q_m^{\psi}|
=O_{\Lambda_*,\psi}(q^{-1/2}\log q)
=o(1),
\qquad
\frac{K_*}{N}=O_{\Lambda_*}(q^{-1/2})=o(1).
}
\tag{13}
\]

Therefore XF-085 applies with any fixed interior margin, for example `kappa=1/2`, once `q` is sufficiently large. There exists an exact degree-`N` equal-weight unit-circle carrier `G_0` whose first `K_*` raw power sums are precisely (5). **Crossing the first prime is a failure of the old XF-097 stability proof, not a static node-budget obstruction.**

## 3. The normalized `ell^1` margin is forward-invariant on every fixed physical band

Let `P_m(t)` be the first `K_*` power sums of the exact degree-`N` periodic heat trajectory through `G_0`, put

\[
u_m(t):=\frac{P_m(t)}{N},
\qquad
a:=N\Delta,
\qquad
\xi_m:=m\Delta,
\tag{14}
\]

and define

\[
S(t):=\sum_{m=1}^{K_*}|u_m(t)|,
\qquad
D(t):=\sum_{m=1}^{K_*}\xi_m|u_m(t)|.
\tag{15}
\]

The exact triangular equation of XF-087 becomes

\[
\boxed{
\dot u_m
=
\xi_m(\xi_m-a)u_m
-a\xi_m\sum_{i=1}^{m-1}u_i u_{m-i}.
}
\tag{16}
\]

Since `xi_m<=Lambda_*`, the upper Dini derivative of `S` satisfies

\[
\begin{aligned}
D^+S
&\le
-(a-\Lambda_*)D
+a\sum_{i+j\le K_*}(\xi_i+\xi_j)|u_i||u_j|\\
&\le
\boxed{
\left[-(a-\Lambda_*)+2aS\right]D.
}
\end{aligned}
\tag{17}
\]

Here the second line uses `xi_{i+j}=xi_i+xi_j`. Now

\[
a=N\Delta\asymp q^{1/2}\to\infty,
\tag{18}
\]

while (13) gives `S(0)=o(1)`. Thus, for all sufficiently large `q`,

\[
a\ge2\Lambda_*,
\qquad
S(0)\le\frac18.
\tag{19}
\]

At the barrier `S=1/8`, (17) is at most `-aD/4`. A standard first-crossing argument yields

\[
\boxed{
S(t)\le S(0)=o(1)
\qquad\text{for every }0\le t\le\frac12.
}
\tag{20}
\]

This is stronger than the small-`K\Delta` perturbative estimate that breaks in XF-100. It does **not** compare the periodic trajectory with the Xi continuum at prime scale; it says only that once a fixed physical-band target has an exact periodic realization, its normalized moment margin cannot blow up under the autonomous periodic heat system.

## 4. The XF-101 collision implant survives all the way through the fixed prime band

Fix any

\[
0<\tau\le\frac12.
\tag{21}
\]

Set

\[
R:=K_*+1,
\qquad
n:=N-2R.
\tag{22}
\]

Because `K_*=o(N)`, one has `n\sim N` and `n/K_*->infinity`. Equation (20) gives

\[
\sum_{m=1}^{K_*}|P_m(\tau)|=o(N)=o(n).
\tag{23}
\]

Hence XF-085 can be applied again, now with exactly `n` nodes, to realize the degree-`N` target prefix `P_m(tau)` on a unit-circle polynomial `A_tau` of degree `n`. Choose a phase `phi` avoiding the finite root set of `A_tau` and form the same high-symmetry collision crystal as XF-101,

\[
C_\phi(w):=(w^R-e^{i\phi})^2.
\tag{24}
\]

Its first `K_*` power sums vanish exactly because `R>K_*`. Therefore

\[
F_\tau(w):=A_\tau(w)C_\phi(w)
\tag{25}
\]

has total degree `N`, is unit-circle-rooted at `t=tau`, contains exact simple double collision sites, and satisfies

\[
P_m^{F}(\tau)=P_m(\tau),
\qquad 1\le m\le K_*.
\tag{26}
\]

The collision normal form XF-002 makes the roots nonreal immediately below `tau`, while the Pólya--Benz/Kabluchko real-zero-preserver input already used in XF-098 keeps them real from `tau` onward. Thus

\[
\boxed{
\Lambda_{\mathrm{per}}(F)=\tau.
}
\tag{27}
\]

Finally, both degree-`N` trajectories satisfy the same triangular system (16). Mode-by-mode uniqueness from the common data (26) gives

\[
\boxed{
P_m^F(t)=P_m(t)
\quad
(1\le m\le K_*,\ 0\le t\le1/2).
}
\tag{28}
\]

So for **every** fixed positive transition time in the observed interval there is a periodic control whose complete first-`K_*` time history is identical to a trajectory initialized from a source state that explicitly contains the first prime atom.

## 5. Stress tests and evidence boundary

The fixed-physical-band assumption is load-bearing. If `Lambda_*` grows with `q`, the number and total weight of prime-power atoms also grow, `K_*/N` may cease to vanish, and the node reserve for the collision crystal may disappear. This finding does not analyze that regime.

Mesh-scale regularization is also load-bearing only as a concrete legal extraction of the distributional endpoint data. The argument extends to any family of atomic tests whose total raw `ell^1` contribution over a fixed physical band is `o(N)` and whose prefix length is `o(N)`. It does not claim that (5) is the unique or optimal Xi source interface.

Most importantly, there is **no prime-scale Xi-to-periodic shadow theorem here**. XF-100 already shows that the XF-097 continuum/trapezoid stability proof fails parametrically at `K_* \asymp \Delta^{-1}`. Equation (28) is an exact nonidentifiability statement inside the finite periodic state class after a distribution-safe prime-enriched endpoint extraction. An Xi-specific analytic condition that is not determined by this prefix may still reject the controls.

The first-prime visibility check (8) prevents a vacuous interpretation: the negative result is not caused by smoothing the arithmetic atom away. Conversely, the vanishing normalized cost (13) shows why seeing a fixed number of atomic spectral lines is too cheap to exhaust a degree-`N` carrier with `N \asymp q^2`.

## 6. Prior art and novelty boundary

The load-bearing external inputs are already recorded in `SOURCES.md`: the Guinand--Weil explicit-formula framework supplies the prime-power atomic spectrum used in XF-052; Gilboa--Peled supplies the exact prescribed-node-count equal-weight trigonometric quadrature used in XF-085; and the Pólya--Benz/Kabluchko real-zero-preserver input is already used in XF-098/XF-101. A targeted prior-art check found these standard components but no theorem combining mesh-regularized explicit-formula atoms, the Xi node scaling, triangular periodic heat, and a hidden roots-of-unity collision block to establish transition nonidentifiability. No new source is load-bearing, so `SOURCES.md` requires no update.

The new line-specific step is the conjunction of three quantitative facts: a fixed physical explicit-formula band has only `O(\Delta^{-1}\log\Delta^{-1})=o(N)` raw moment mass after mesh-scale atomic extraction; this normalized `ell^1` cone is forward-invariant under the exact periodic Vieta flow by (17); and `K_* \asymp \Delta^{-1}=o(N)` still leaves enough unused degree for the exact XF-101 collision implant.

## 7. Consequence for the live Xi-flow frontier

XF-100 identified prime-scale arithmetic as one possible way to escape the prime-blind low-band obstruction. This finding rules out the most direct version of that repair: **extend the autonomous Vieta prefix to a fixed physical band, regularize the prime atoms legally at mesh scale, and hope their presence makes the periodic transition identifiable.** It does not.

The obstruction is now structural rather than merely low-frequency. As long as the proposed Xi interface is compressed into a power-sum prefix of length `K=o(N)` with an `o(N)` raw `ell^1` margin, an invisible collision crystal can live above that prefix and can be implanted at an arbitrary positive heat time without changing the complete visible history. Reaching the first prime changes the source analysis, but it does not change this aliasing theorem.

A successful next interface must therefore import information that the autonomous sublinear prefix does not determine: for example a genuinely non-prefix Xi-specific analytic constraint, an observable coupling to enough of the degree-`N` spectrum to destroy the `R>K` crystal reserve, or a source/destination quantity whose heat dynamics are not closed by the triangular low-mode system. The remaining task is no longer simply to make prime atoms visible; it is to make them visible in a state that cannot quotient away the transition geometry.