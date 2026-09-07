# XF-101 — current low Vieta trajectory admits every fixed positive transition time

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` + `MATCHED-CONTROL` + `TRANSITION-NONIDENTIFIABILITY` + `COLLISION-SAFE`. XF-100 leaves a precise low-band fork: perhaps the prime-free archimedean trajectory itself, together with the existence of a positive de Bruijn--Newman transition, forces nonvanishing distance from the collision-invisible periodic cone. That implication is false in the current state space.

For every fixed

\[
0<\tau\le \frac12,
\tag{1}
\]

and every sufficiently large Xi scale, there is a degree-`N` periodic backward-heat trajectory whose finite periodic Newman threshold is **exactly `tau`**, while its complete power-sum trajectory

\[
(P_1(t),\ldots,P_K(t))
\tag{2}
\]

is **identically equal for all `0<=t<=1/2`** to the prime-free periodic shadow constructed in XF-097. Consequently the same control is `o(1)`-close to the actual Xi sampled trajectory in the exact XF-079/XF-086 guarded resource throughout that interval.

The construction uses no approximation at the transition. One reserves only `2R=o(N)` roots with `R>K`, inserts an `R`-fold crystal of exact double collisions at time `tau`, and uses XF-085 on the remaining `N-2R` roots to restore the entire first-`K` moment prefix exactly. The autonomous triangular power-sum heat system then propagates that exact equality both forward and backward in time. Hence the current low Vieta state does not merely fail to *detect some collisions* as in XF-098/XF-099: it does not identify the transition time at all, even after the full low-frequency time history is supplied.

## 1. The XF-097 shadow has enough moment margin at every fixed time

Keep the canonical scales

\[
M=q^2,
\qquad N=2M,
\qquad
\Delta^2\asymp q^{-3},
\qquad
K\asymp q\log\log T,
\tag{3}
\]

and let `P_m^B(t)` denote the exact degree-`N` periodic shadow of XF-097. Write `Q_m(t)=\mathcal Z_t(m\Delta)` for the sampled Xi Volterra trajectory. XF-097 proves uniformly for `0<=t<=1/2` that

\[
|Q_m(t)|\ll \frac1{m\Delta},
\qquad
m|P_m^B(t)-Q_m(t)|\ll E_*,
\tag{4}
\]

for `1<=m<=K`, where `E_*` is only polylogarithmic at (3). Therefore

\[
\begin{aligned}
\sum_{m=1}^{K}|P_m^B(t)|
&\ll
(\Delta^{-1}+E_*)\sum_{m=1}^{K}\frac1m\\
&\ll
(\Delta^{-1}+E_*)\log(K+1).
\end{aligned}
\tag{5}
\]

Since `Delta^{-1}\asymp q^{3/2}`, `N\asymp q^2`, and `E_*` is polylogarithmic,

\[
\boxed{
\sup_{0\le t\le1/2}
\frac1N\sum_{m=1}^{K}|P_m^B(t)|=o(1).
}
\tag{6}
\]

Thus the exact equal-weight realization theorem XF-085 is not confined to the endpoint `t=0` used in XF-097. It can be reapplied at **any fixed target time** after removing any `o(N)` number of node slots.

Take the integer

\[
R:=K+1,
\qquad
n:=N-2R.
\tag{7}
\]

Because `K=o(N)`, one has `n\sim N` and `n/K\to\infty`. Equation (6) implies, for example, that for all sufficiently large scales

\[
2\sum_{m=1}^{K}|P_m^B(\tau)|\le \frac n2.
\tag{8}
\]

XF-085 with `kappa=1/2` therefore gives exactly `n` unit-circle nodes whose raw moments satisfy

\[
\boxed{
P_m^{A}(\tau)=P_m^B(\tau),
\qquad 1\le m\le K.
}
\tag{9}
\]

Let `A_tau(w)` be the corresponding degree-`n` unit-circle root polynomial. Repeated nodes are permitted by the quadrature theorem; they are irrelevant to the collision block below because its phase can be chosen away from the finite root set of `A_tau`.

## 2. A high-symmetry collision block costs no visible moment

For a phase `phi`, define

\[
\boxed{
C_\phi(w):=(w^R-e^{i\phi})^2.
}
\tag{10}
\]

This polynomial has degree `2R`. Its roots are the `R` solutions of `w^R=e^{i\phi}`, each with multiplicity exactly two. Its raw power sums are

\[
P_m^C
=
2e^{im\phi/R}
\sum_{r=0}^{R-1}e^{2\pi i mr/R}.
\tag{11}
\]

Hence

\[
\boxed{
P_m^C=0,
\qquad 1\le m<R.
}
\tag{12}
\]

Since `R=K+1`, the crystal is exactly invisible to every visible mode. Choose `phi` outside the finite set for which a root of `C_phi` is also a root of `A_tau`, and put

\[
\boxed{
F_\tau(w):=A_\tau(w)C_\phi(w).
}
\tag{13}
\]

Then `F_tau` has total degree

\[
n+2R=N,
\tag{14}
\]

all roots lie on the unit circle, and each crystal location is an **exact simple double zero of the total polynomial** because `A_tau` is nonzero there. Additivity of raw power sums under union of root multisets, together with (9) and (12), gives

\[
\boxed{
P_m^F(\tau)=P_m^B(\tau),
\qquad 1\le m\le K.
}
\tag{15}
\]

Thus one may implant `R=K+1` simultaneous collision sites while preserving the entire low Vieta prefix exactly. Only an `o(N)` fraction of the node budget was consumed, and the realization margin (6) pays for the remaining carrier.

## 3. The implanted trajectory has threshold exactly `tau`

Let `F_t` be the exact normalized periodic backward-heat trajectory passing through (13) at time `tau`, with the same period and degree convention as XF-067/XF-087/XF-097. Two established collision-safe facts determine its threshold.

First, periodic backward heat preserves unit-circle/root-realness in the real periodic coordinate in the forward `t` direction. This is the same Pólya--Benz/Kabluchko real-zero-preserver input already used and source-anchored in XF-098. Since `F_tau` is unit-circle-rooted,

\[
F_t\text{ is real-rooted in the periodic coordinate for every }t\ge\tau.
\tag{16}
\]

Second, every crystal root in (13) is a zero of exact multiplicity two. XF-002 applies without labeling roots through the collision and gives the universal local discriminant law in the physical coordinate,

\[
D(t)=8(t-\tau)+O((t-\tau)^2).
\tag{17}
\]

Consequently each such pair is nonreal for all sufficiently small positive `epsilon` at time `tau-epsilon`. Therefore the trajectory is not fully real-rooted arbitrarily close below `tau`, while (16) makes it fully real-rooted from `tau` onward. Its finite periodic transition threshold is exactly

\[
\boxed{\Lambda_{\rm per}(F)=\tau.}
\tag{18}
\]

No factorization of the heat flow into an `A` sector and a crystal sector is being assumed. In fact such a factorization would generally be false. Only the root multiplicity at the single slice `t=tau`, the local collision normal form, and global forward real-root preservation are used.

## 4. Triangular heat makes the entire visible trajectory identical

The decisive point is that equality (15) is not restricted to the collision slice. For any exact degree-`N` periodic trajectory, XF-087 gives the autonomous triangular system

\[
\boxed{
P_m'
=
\xi_m^2P_m
-\xi_m\Delta
\left(
NP_m+
\sum_{i=1}^{m-1}P_iP_{m-i}
\right),
\qquad
1\le m\le K.
}
\tag{19}
\]

Both `P^F` and `P^B` satisfy (19) with the same `N`, `Delta`, and data at `t=tau`. Uniqueness can be read directly mode by mode and does not require any root simplicity. For `m=1`, the difference satisfies a homogeneous scalar linear equation and vanishes. Assuming equality for all lower modes, the difference at mode `m` again satisfies a homogeneous scalar linear equation because every convolution term containing lower-mode differences has disappeared. Induction gives

\[
\boxed{
P_m^F(t)=P_m^B(t)
\quad
\text{for every }1\le m\le K
\text{ and every }0\le t\le\frac12.
}
\tag{20}
\]

This works in both time directions from `tau`; it is ordinary uniqueness for the finite polynomial coefficient trajectory, not a backward parabolic stability claim.

Combining (20) with the XF-097 shadow estimate yields

\[
\boxed{
\sup_{0\le t\le1/2}
\mathcal R_{[J,K]}
\left(
(P_m^F(t)-Q_m(t))_{m=J}^{K}
\right)
=o(1).
}
\tag{21}
\]

Hence **for every fixed positive `tau<=1/2`, the actual Xi guarded trajectory has a synthetic periodic control with transition threshold exactly `tau` and the same asymptotic guarded data throughout the whole observed time interval.** At the exact periodic level, the control does even better: its full first-`K` time history is identical to the canonical prime-free shadow, not merely close in norm.

## 5. Stress tests and evidence boundary

The reduced node count in (7) is load-bearing but harmless. XF-085 is a theorem for arbitrary prescribed node count above its `C_kappa K` threshold; it is not restricted to the original `N=2q^2`. Because `2R=O(K)=o(N)`, both the fixed normalized `ell^1` margin and the exact-node-count quadrature threshold survive.

The crystal phase cannot create accidental higher multiplicity at the implanted sites: there are only finitely many roots of `A_tau`, so a generic `phi` avoids them. Other repeated roots inside `A_tau` do not weaken the argument. They may create additional collisions at `tau`, but the deliberately implanted crystal already proves nonrealness immediately below `tau`, while forward real-root preservation still gives (16).

The conclusion is **not** that Xi itself can have arbitrary `Lambda`, nor that the full Xi function is approximated by these controls outside the current state space. The construction matches only the admitted finite periodic state: degree, exact periodic heat, unit-circle real side, and the complete first-`K` power-sum trajectory. It is therefore a matched falsifier for any transition-coercivity theorem whose hypotheses reduce to those data. An Xi-specific theorem may still rule out these controls through information not determined by the first `K` moments.

Equation (21) is also only an asymptotic statement about the actual Xi samples in the XF-086 guarded norm. Exact equality with Xi is neither claimed nor needed. The exact nonidentifiability statement is between finite periodic trajectories; XF-097 then transfers it to the present Xi observable with `o(1)` loss.

The choice `R=K+1` is minimal only for convenience. Any integer `R>K` with `R=o(N)` works. Thus the obstruction persists if the visible band is changed by constant factors or slowly varying modifiers while remaining `o(N)` and while the target prefix retains the XF-085 moment margin.

## 6. Prior art and novelty boundary

The two external ingredients are already load-bearing and already recorded in `SOURCES.md`. Gilboa--Peled's Chebyshev-type quadrature theorem supplies the exact equal-weight realization used in XF-085. The periodic backward-heat real-zero preservation used in XF-098 is recorded through Kabluchko's 2025 treatment and its Pólya--Benz input. A targeted prior-art check also finds the broader polynomial/backward-heat zero-dynamics literature, but no result located in that search combines a prescribed low trigonometric moment prefix with a high-symmetry collision block to realize an arbitrarily prescribed positive transition time while leaving the autonomous low-mode trajectory unchanged.

No novelty is claimed for roots-of-unity cancellation, Chebyshev quadrature, the real-zero-preserver theorem, or ODE uniqueness. The durable line-specific step is their scale-matched combination with the XF-097 moment margin and the XF-087 triangular state equation. No new source is load-bearing, so `SOURCES.md` requires no update.

## 7. Consequence for the live Xi-flow fork

XF-100 proposed one last low-band test before redesigning the observable: perhaps the archimedean low-frequency trajectory, plus the existence of a positive transition, forces a visible defect even though prime arithmetic is absent. Equations (18)--(21) give a negative matched control at exactly that interface.

The current first-`K` periodic state therefore cannot support a universal implication of the form

\[
\Lambda_{\rm per}>0
\quad\Longrightarrow\quad
\text{nonvanishing current guarded resource},
\tag{22}
\]

nor can the complete current low-mode time history identify or upper-bound the periodic transition time across the admitted carrier class. The obstruction is stronger than XF-099's special collision crystal: **the actual canonical prime-free shadow trajectory itself can be shared by controls having every prescribed fixed positive transition time.**

Accordingly the low-band branch of XF-100 is closed as a generic periodic-state route. Further progress toward an upper bound for Xi must import information that is not a function of the present autonomous prefix: for example a redesigned interface reaching prime-scale/atomic explicit-formula data, a non-prefix Xi-specific analytic constraint, or a different observable whose dynamics are not quotiented by the first-`K` triangular closure. This finding is a route obstruction, not evidence for a positive Xi transition.