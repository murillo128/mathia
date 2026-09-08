# XF-123 — uniform q-scale flatness admits collision-saturated transitions at arbitrary time sequences

**Status:** `EXACT-DERIVED` + `SOURCE-SPECIFIC` + `UNIFORM-IN-TIME` + `COLLISION-SATURATION` + `DYNAMIC-NONIDENTIFIABILITY`. XF-120 showed that the full natural Xi q-scale prefix at one slice can be realized exactly while `1-o(1)` of the degree budget sits in simultaneous double collisions. XF-121 showed that at an arbitrary target time `tau`, a much smaller invisible crystal of only `O(K)` roots is enough to force the periodic Newman threshold to equal `tau`, provided the target Toeplitz section retains a fixed frame. XF-122 then proved the stronger source-specific fact

\[
\delta_K:=\sup_{t\ge0}\|T_K(c(t))-I\|_{\rm op}\longrightarrow0.
\tag{1}
\]

Those statements can be combined in a quantitatively stronger way. The uniformity in `(1)` means the target time need not be fixed as the Xi scale grows. For **every sequence of finite target times**

\[
\tau_K\ge0,
\tag{2}
\]

including sequences with `tau_K -> infinity`, one can construct an exact degree-`N` unit-circle matched control whose first `K` normalized moments follow the canonical Xi q-scale history for all positive heat times, whose periodic Newman threshold is exactly `tau_K`, and for which a fraction `1-o(1)` of all roots participate in simultaneous simple double collisions at that target time.

There is also an exact cone-level reserve law behind the construction. If a fraction `rho` of the roots is reserved for an invisible collision crystal and the remaining carrier fraction is `alpha=1-rho`, then the rescaled carrier moment section is positive semidefinite **if and only if**

\[
\boxed{
\rho\le\lambda_{\min}(T_K(c(\tau))).
}
\tag{3}
\]

Thus the smallest eigenvalue of the target Toeplitz section is exactly the maximal collision fraction that can be hidden by this carrier-plus-crystal split at the truncated moment-cone level. XF-122 drives that threshold uniformly to `1`. The only extra cost needed for an exact equal-weight carrier is to leave a fraction `alpha` satisfying

\[
\frac{\delta_K}{\alpha}\to0,
\qquad
\frac{K/N}{\alpha}\to0.
\tag{4}
\]

Since both `delta_K` and `K/N` vanish, such `alpha=o(1)` exists. Therefore the arbitrary-time transition controls of XF-121/XF-122 are not supported by a rare exceptional collision gadget: **the matched fiber at every target time reaches asymptotically full collision density**.

No RH assumption is used. This is a statement about the periodic finite-degree matched-control interface, not a claim that Xi itself develops such collisions.

## 1. Exact collision-reserve threshold inside the Toeplitz moment cone

Retain the XF-118/XF-122 scaling

\[
N=2q^2,
\qquad
K\asymp a^3\log a,
\qquad
N\asymp a^4,
\qquad
\frac KN\longrightarrow0,
\tag{5}
\]

and let

\[
c_0(t)=1,
\qquad
c_{-m}(t)=\overline{c_m(t)},
\qquad
T_K(c(t))=(c_{i-j}(t))_{0\le i,j\le K}.
\tag{6}
\]

Fix temporarily one target time `tau>=0`. Reserve `2R` roots for a moment-invisible collision factor and write

\[
n=N-2R,
\qquad
\alpha:=\frac nN,
\qquad
\rho:=\frac{2R}{N}=1-\alpha.
\tag{7}
\]

The `n` carrier roots must reproduce the raw degree-`N` target power sums. Hence their normalized moments relative to their own node count must be

\[
d_0=1,
\qquad
 d_m=\frac Nn c_m(\tau)=\frac1\alpha c_m(\tau),
\qquad 1\le |m|\le K.
\tag{8}
\]

Exactly as in the affine calculation behind XF-121,

\[
\begin{aligned}
T_K(d)
&=
\frac1\alpha T_K(c(\tau))
-
\left(\frac1\alpha-1\right)I\\
&=
I+\frac1\alpha\bigl(T_K(c(\tau))-I\bigr).
\end{aligned}
\tag{9}
\]

If `lambda` is an eigenvalue of `T_K(c(tau))`, the corresponding eigenvalue of `T_K(d)` is

\[
\frac{\lambda-\rho}{\alpha}.
\tag{10}
\]

Therefore

\[
\boxed{
T_K(d)\succeq0
\iff
\lambda_{\min}(T_K(c(\tau)))\ge\rho.
}
\tag{11}
\]

This is an exact identity, not an asymptotic sufficient condition. In particular, within this additive carrier-plus-invisible-crystal architecture, `(11)` is the sharp truncated-moment-cone threshold for how much of the degree may be reserved for collisions.

XF-122 gives uniformly in the target time

\[
1-\delta_K
\le
\lambda_{\min}(T_K(c(t)))
\le
1+\delta_K,
\qquad t\ge0,
\tag{12}
\]

with `delta_K=o(1)`. Thus positivity alone already permits collision fractions approaching one uniformly in `t`. Exact equal weights require a little more room because the carrier must itself contain enough nodes for the quadrature bridge; the next section shows that this still costs only an `o(1)` fraction of the degree.

## 2. A single vanishing carrier fraction works uniformly for every target time

Choose any sequence `alpha_K` satisfying

\[
\alpha_K\to0,
\qquad
\frac{\delta_K}{\alpha_K}\to0,
\qquad
\frac{K/N}{\alpha_K}\to0.
\tag{13}
\]

For example one may take

\[
\alpha_K
=
\sqrt{\delta_K}
+
\sqrt{K/N}
\tag{14}
\]

up to an immaterial even-integer rounding of `n=alpha_K N`. Because `N` is even and `alpha_K N \gg K\to\infty`, choose an even integer `n_K` with

\[
\frac{n_K}{N}=\alpha_K+o(\alpha_K),
\tag{15}
\]

and set

\[
R_K=\frac{N-n_K}{2}.
\tag{16}
\]

Then

\[
\frac{n_K}{N}\to0,
\qquad
\frac{n_K}{K}\to\infty,
\qquad
\frac{R_K}{N}\to\frac12,
\qquad
R_K>K
\tag{17}
\]

for all sufficiently large scales.

Now let `tau_K>=0` be **arbitrary at each scale**. It may be fixed, oscillatory, or diverge. Define the carrier moments by

\[
d_m^{(K)}
:=
\frac{N}{n_K}c_m(\tau_K),
\qquad 1\le|m|\le K.
\tag{18}
\]

Equation `(9)` and the uniform bound `(1)` give

\[
\boxed{
\|T_K(d^{(K)})-I\|_{\rm op}
\le
\frac{N}{n_K}\delta_K
=
\frac{\delta_K}{\alpha_K+o(\alpha_K)}
\longrightarrow0,
}
\tag{19}
\]

uniformly over the choice of `tau_K`. Meanwhile `(17)` gives the prescribed-node surplus

\[
\frac{n_K}{K}\longrightarrow\infty.
\tag{20}
\]

The Poisson-deconvolution bridge of XF-119, in the rescaled form already used in XF-120, therefore applies to `(18)`: for every sufficiently large scale there exist exactly `n_K` unit-circle nodes

\[
\nu_{1,K},\ldots,\nu_{n_K,K}
\tag{21}
\]

such that

\[
\boxed{
\sum_{j=1}^{n_K}\nu_{j,K}^{\,m}
=
N c_m(\tau_K),
\qquad 1\le m\le K.
}
\tag{22}
\]

The crucial point is that the node count in `(21)` is prescribed exactly. There is no rational-weight rounding and no moment error. The same sequence `n_K`, chosen from the uniform envelope `delta_K`, works regardless of how the target times `tau_K` vary.

## 3. The remaining `1-o(1)` degree can be put into exact double collisions

Let

\[
A_K(w):=\prod_{j=1}^{n_K}(w-\nu_{j,K})
\tag{23}
\]

be the carrier polynomial. Choose a phase `phi_K` so that none of the roots of

\[
C_K(w):=
\left(w^{R_K}-e^{i\phi_K}\right)^2
\tag{24}
\]

coincides with a carrier root. This is always possible because only finitely many phases are forbidden.

The collision factor has degree `2R_K=N-n_K`. It consists of `R_K` distinct unit-circle sites, each of multiplicity exactly two. Its raw power sums are

\[
P_m(C_K)
=
2\sum_{r=0}^{R_K-1}
\exp\!\left(
\frac{im(\phi_K+2\pi r)}{R_K}
\right)
=0,
\qquad 1\le m<R_K.
\tag{25}
\]

Since `R_K>K`, the whole collision crystal is invisible to the observed prefix. Hence

\[
F_K(w):=A_K(w)C_K(w)
\tag{26}
\]

has degree exactly `N`, all its roots lie on the unit circle at the target slice, and `(22)`--`(25)` give

\[
\boxed{
P_m(F_K)=N c_m(\tau_K),
\qquad 1\le m\le K.
}
\tag{27}
\]

At the same time the fraction of the degree carried by simple double collisions is

\[
\boxed{
\frac{2R_K}{N}
=1-\frac{n_K}{N}
=1-o(1).
}
\tag{28}
\]

Thus almost every root slot can sit in a collision at an arbitrarily chosen target time while the complete natural q-scale prefix is matched **exactly**.

Equation `(11)` explains why this saturation is not accidental. The collision reserve consumes a fraction `rho_K=1-alpha_K`; the target Toeplitz section has smallest eigenvalue `1-o(1)` uniformly in time; and the carrier keeps just enough slack, `alpha_K \gg delta_K+K/N`, to remain near-isometric after the `1/alpha_K` moment amplification and still have `n_K\gg K` equal-weight nodes.

## 4. The same control matches the complete first-`K` positive-time history and has threshold `tau_K`

The target-slice construction alone would only reproduce XF-120 at a moving slice. The dynamic content comes from the exact triangular power-sum evolution of XF-087.

At time `tau_K`, `(27)` says that the control and the canonical q-scale Xi source have identical first `K` normalized moments. For each `m<=K`, the heat equation for the `m`th moment depends only on moments of order at most `m`. Hence the first-`K` system is a closed finite triangular ODE. Uniqueness therefore forces the matched control and the canonical admitted trajectory to have identical first-`K` moments throughout their common positive-time evolution. In particular, the match propagates from the target slice both back to the source slice and forward to all later positive times:

\[
\boxed{
P_m(F_K(t))=N c_m(t),
\qquad
1\le m\le K,
\quad t\ge0.
}
\tag{29}
\]

Here `F_K(t)` denotes the finite periodic heat evolution normalized as in XF-087--XF-122. Equation `(29)` is a moment-history statement; the factorization `(26)` is asserted only at the target slice and is not assumed to persist under heat.

At `t=\tau_K`, the roots supplied by `(24)` are isolated simple double roots because `phi_K` was chosen to avoid the carrier. The collision-safe local discriminant law used in XF-099, XF-101, XF-120 and XF-121 makes each such pair leave the real/unit-circle divisor immediately on the backward side of the collision. Conversely, at the target slice every root of `(26)` is real in the periodic divisor coordinate, and the standard polynomial real-zero preserver used throughout the matched-control branch keeps all roots real for later heat times. Therefore

\[
\boxed{
\Lambda_{\rm per}(F_K)=\tau_K.
}
\tag{30}
\]

Because `(1)` is uniform on the whole half-line, nothing in the construction requires the sequence `tau_K` to stay in a compact interval. One may prescribe, for example, `tau_K -> infinity`. The controls then reproduce the same complete first-`K` positive-time q-scale history while their transition thresholds escape to infinity.

This is stronger than the fixed-`tau` statement of XF-122. It shows that the autonomous q-scale history supplies not even a compactness bound for the transition parameter inside the periodic matched-control class.

## 5. Stress tests and limits of the statement

### 5.1 The carrier cannot be shrunk arbitrarily at fixed Toeplitz defect

The exact eigenvalue identity `(10)` prevents the argument from hiding an algebraic failure. If the reserved collision fraction exceeds `lambda_min(T_K(c(tau)))`, then `T_K(d)` has a negative eigenvalue and no positive representing measure for the carrier exists. Thus the cone-level threshold `(11)` is genuinely sharp for this split.

The equal-weight proof deliberately stays farther inside the cone by imposing `delta_K/alpha_K -> 0`. This is sufficient, not claimed optimal. Improving the prescribed-node bridge near the boundary might reduce the carrier fraction further, but is unnecessary for the `1-o(1)` saturation conclusion.

### 5.2 The invisible crystal requires `R_K>K`

The vanishing in `(25)` fails at multiples of `R_K`. The construction therefore uses `R_K>K`, not merely many collision sites. Because `R_K~N/2` and `K/N->0`, this gate has enormous asymptotic slack.

### 5.3 Parity and accidental triple collisions do not create a hidden obstruction

`N=2q^2` is even. Choosing `n_K` even makes `R_K` integral. Since `n_K\gg K\to\infty`, changing `n_K` by at most one or two nodes does not affect `(13)`--`(20)`. The phase `phi_K` removes coincidences between the crystal and the finite carrier root set, so the reserved sites are genuine multiplicity-two collisions rather than uncontrolled higher multiplicities.

### 5.4 No persistent carrier/crystal decomposition is assumed

After the target slice the heat evolution mixes the factors. The argument never evolves `A_K` and `C_K` separately. Exact target moments plus triangular uniqueness give `(29)`, while the transition statement uses only local collision behavior at `tau_K` and global forward real-zero preservation.

### 5.5 This does not construct a pathological Xi deformation

The controls are finite periodic matched models. Their role is adversarial: they show what the first-`K` q-scale interface fails to determine. Xi has additional cross-scale consistency, higher modes, entire-function geometry and arithmetic structure that these controls are not required to reproduce.

## 6. Prior-art audit

The only external load-bearing realization input remains the Gilboa--Peled theorem on Chebyshev-type trigonometric quadrature for doubling weights, already anchored in `research/xi_flow/SOURCES.md` and already used in XF-085/XF-119. The present argument does not strengthen that theorem; it uses the Mathia-specific Poisson-deconvolution bridge of XF-119 to place the amplified carrier moments in its uniformly regular regime.

The collision crystal uses only the elementary roots-of-unity identity in `(25)`. A directed search for roots-of-unity power-sum vanishing did not expose a theorem matching the present combination of a q-scale Toeplitz moment fiber, prescribed-node carrier, invisible high-order collision crystal and de Bruijn--Newman transition placement. The real-zero heat-flow preservation and local collision mechanism are already anchored in the Xi-flow source list and earlier matched-control findings. No new external source is load-bearing here, so `SOURCES.md` should remain unchanged.

## 7. Consequence for the frontier

XF-120 left open whether collision saturation was merely a peculiarity of the source slice. XF-121/XF-122 then moved the transition to arbitrary fixed times, but their explicit construction needed only `2K+2=o(N)` colliding roots. That left a possible interpretation in which the q-scale history failed only because of a sparse exceptional defect while the bulk divisor geometry remained constrained.

The present result removes that interpretation. For every target-time sequence, even one escaping to infinity, the exact same canonical first-`K` positive-time history is compatible with controls for which **almost the entire degree is sitting in simultaneous double collisions at the transition slice**. Quantitatively, the maximal invisible collision reserve at the moment-cone level is exactly governed by `lambda_min(T_K(c(tau)))`, and XF-122 sends this quantity uniformly to one.

Therefore no statistic that factors only through the autonomous first-`K` q-scale history can infer the transition time, bound it in a compact set, or exclude macroscopic collision degeneracy in the matched periodic fiber. A positive route must leave that sigma-algebra: it needs cross-scale compatibility involving modes beyond `K`, information tied to the full degree `N`, or genuinely global Xi entire-function/arithmetic geometry.

That is the current negative endpoint of the q-scale autonomous-prefix program.