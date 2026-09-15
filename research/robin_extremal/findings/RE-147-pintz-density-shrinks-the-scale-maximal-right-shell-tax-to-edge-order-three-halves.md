# RE-147 — Pintz density shrinks the scale-maximal right-shell tax to edge order three-halves

**Status:** `LITERATURE+DERIVED + EXACT-SPLICE + ACTUAL-ZETA-ZEROS + FINITE-ZERO-EDGE + SCALE-MAXIMAL-ANCHOR + PINTZ-ZERO-DENSITY + RIGHTWARD-SHELL + HIGH-TAIL + OBSERVATION-TAX + EDGE-THREE-HALVES + LEADING-PACKET + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

`RE-146` shows that choosing the leading Robin atom to be scale-maximal converts horizontal motion to the right into ordinate inflation and then lets a zero-density theorem price the resulting shell. Its quantitative statement used Ingham's classical density exponent

\[
\nu_I(\sigma)=\frac{3(1-\sigma)}{2-\sigma}.
\]

That is not the correct high-sigma input. Pintz's explicit 2023 density family near `Re s=1` gives, for `h=1-\sigma<1/12`,

\[
N(1-h,T)\ll_{\varepsilon,h}T^{\nu_P(h)+\varepsilon},
\qquad
\nu_P(h)\le 3\sqrt2\,h^{3/2}+18h^2.
\]

Splicing this into the same scale-maximal argument changes the required early-window loss from order `1-Theta` to order `(1-Theta)^(3/2)` as the finite zero edge `Theta` approaches `1`. If

\[
\delta:=1-\Theta<\frac1{12},
\]

then the right-shell certificate is available on every fixed relative observation window of width `kappa` satisfying

\[
\boxed{
\kappa>
\tau_P(\delta)
:=
\frac{3}{\sqrt2}\,\delta^{3/2}+9\delta^2.
}
\]

By contrast the Ingham version of `RE-146` required

\[
\kappa>
\tau_I(\delta)
:=
\frac{3\delta}{2(1+\delta)}.
\]

Thus

\[
\tau_P(\delta)
=
\frac{3}{\sqrt2}\delta^{3/2}+O(\delta^2),
\qquad
\tau_I(\delta)
=\frac32\delta+O(\delta^2).
\]

The gain is qualitative at the edge: the global zero-density price of eliminating a sufficiently rightward shell becomes sublinear in the edge gap. The same substitution also improves the weighted high-ordinate tail of `RE-141` from exponent `-2+O(delta)` to `-2+O(delta^(3/2))`.

This does **not** close the Robin visibility mechanism. The near-left cluster of `RE-144`, horizontally near but vertically remote modes, and synchronization of a local visibility witness with the early subwindow remain untouched. The result instead removes an avoidable quantitative tax from the part of the exterior that `RE-146` already knows how to control.

## 1. Pintz gives an explicit smooth high-sigma density envelope

Write

\[
N(\sigma,T)
:=
\#\{\rho=\beta+i\gamma:\zeta(\rho)=0,\ \beta\ge\sigma,\ |\gamma|\le T\},
\]

counting multiplicity. Pintz's Theorem 1 in *Density theorems for Riemann's zeta-function near the line Re s = 1* states that, for

\[
0<h<\frac1{12},
\]

one has

\[
N(1-h,T)
\ll_{\varepsilon,h}
T^{B(h)h+\varepsilon},
\tag{1}
\]

where

\[
B(h)
=
\max\left\{
\frac{3}{\ell\,[1-2(\ell-1)h]},
\frac{4}{k\,[1-(k-1)h]}
\right\},
\tag{2}
\]

and the integers `k=k(h)` and `ell=ell(h)` are characterized by

\[
k(k-1)h<1\le k(k+1)h,
\tag{3}
\]

\[
2\ell(\ell-1)h<1\le2\ell(\ell+1)h.
\tag{4}
\]

For the present splice it is useful to replace the stepwise expression (2) by a smooth upper envelope. Put

\[
s:=\sqrt{2h}.
\]

From (4),

\[
\ell>\frac1s-\frac12,
\qquad
\ell-1<\frac1s.
\]

Hence

\[
\frac{3}{\ell[1-2(\ell-1)h]}
<
\frac{3s}{(1-s/2)(1-s)}.
\tag{5}
\]

For `0<s<1/sqrt(6)`, direct expansion gives

\[
\frac{3s}{(1-s/2)(1-s)}
\le
3s+9s^2
=
3\sqrt{2h}+18h.
\tag{6}
\]

For the second branch put `r=sqrt(h)`. Equation (3) gives

\[
k>\frac1r-\frac12,
\qquad
k-1<\frac1r,
\]

and therefore

\[
\frac{4}{k[1-(k-1)h]}
<
\frac{4r}{(1-r/2)(1-r)}.
\tag{7}
\]

On `0<r<1/sqrt(12)`, the right side of (7) is at most

\[
3\sqrt2\,r+18r^2.
\tag{8}
\]

One quick verification is to use `(1-r/2)(1-r)>=1-3r/2`; after multiplying by `1-3r/2`, the desired inequality reduces to a concave quadratic whose two endpoint values on `[0,1/sqrt(12)]` are positive.

Combining (2), (6), and (8),

\[
\boxed{
B(h)\le3\sqrt{2h}+18h
}
\qquad
\left(0<h<\frac1{12}\right).
\tag{9}
\]

Thus Pintz gives the convenient zero-count exponent

\[
\boxed{
\nu_P(h)
:=
3\sqrt2\,h^{3/2}+18h^2
}
\tag{10}
\]

in the sense that, for every fixed `h<1/12` and every `epsilon>0`,

\[
N(1-h,T)
\ll_{\varepsilon,h}
T^{\nu_P(h)+\varepsilon}.
\tag{11}
\]

Pintz's Theorem 2 records the same limiting leading constant `3 sqrt(2)` directly. Equation (10) is preferable here because it is an explicit fixed-`h` envelope and therefore does not require any diagonal choice between `h` and an auxiliary epsilon.

## 2. Any zero-density exponent plugs directly into the scale-maximal shell lemma

Keep the leading coefficient notation of `RE-146`,

\[
d_\rho:=\frac1{\rho(1-\rho)},
\qquad
 a_{\rho,0}(u)
:=e^{-(\Theta-\beta)u}d_\rho,
\]

and at scale `U` choose a strict-subedge zero

\[
\rho_0=\beta_0+i\gamma_0
\]

maximizing

\[
M_\rho(U)
:=|a_{\rho,0}(U)|.
\]

Write

\[
M_0(U):=M_{\rho_0}(U)
\]

and assume the strong-atom branch

\[
M_0(U)\ge cU^{-A}.
\tag{12}
\]

As in `RE-146`, (12) implies

\[
(\Theta-\beta_0)U\le A\log U+O(1),
\tag{13}
\]

so `beta_0` approaches `Theta`, and also

\[
1+|\gamma_0|\ll U^{A/2}.
\tag{14}
\]

For a zero to the right of the anchor put

\[
\Delta:=\beta-\beta_0\ge0,
\qquad
q_\rho:=\frac{|d_\rho|}{|d_{\rho_0}|}.
\]

Scale maximality gives the exact inequality

\[
e^{U\Delta}q_\rho\le1.
\tag{15}
\]

Consequently, on the rightward shell

\[
\Delta\ge\frac RU,
\tag{16}
\]

one has `q_rho<=e^-R`. Since on a fixed strip

\[
|d_\rho|\asymp(1+\gamma^2)^{-1},
\tag{17}
\]

(15)--(17) force

\[
1+|\gamma|
\gg
e^{R/2}(1+|\gamma_0|).
\tag{18}
\]

Now suppose a fixed `sigma_-<Theta` has a zero-density estimate

\[
N(\sigma_-,T)
\ll_\varepsilon T^{\nu+\varepsilon}.
\tag{19}
\]

By (13), `beta_0>sigma_-` for all sufficiently large `U`, so every zero in (16) is counted by (19). For `p>0`, partial summation and (17) give, whenever

\[
2p>\nu+\varepsilon,
\]

\[
\sum_{\substack{\beta\ge\sigma_-\\ |\gamma|\ge H}}
|d_\rho|^p
\ll
H^{-2p+\nu+\varepsilon}.
\tag{20}
\]

Observe at an earlier scale

\[
u=tU,
\qquad
p:=1-t.
\]

For every rightward zero,

\[
\frac{|a_{\rho,0}(tU)|}{|a_{\rho_0,0}(tU)|}
=
(e^{U\Delta}q_\rho)^t q_\rho^p
\le q_\rho^p.
\tag{21}
\]

Using (18)--(20) in (21) yields

\[
\boxed{
\frac{
\sum_{\beta\ge\beta_0+R/U}|a_{\rho,0}(tU)|
}{|a_{\rho_0,0}(tU)|}
\ll
(1+|\gamma_0|)^{\nu+\varepsilon}
\exp\!\left[-\left(p-\frac{\nu+\varepsilon}{2}\right)R\right].
}
\tag{22}
\]

This is the general density-to-shell transfer behind `RE-146`. If a fixed `eta` satisfies

\[
\eta>\frac\nu2,
\tag{23}
\]

then, after choosing epsilon with `nu+epsilon<2 eta`, (22) is uniform for

\[
t\le1-\eta.
\]

Using (14),

\[
\boxed{
\frac{
\sum_{\beta\ge\beta_0+R/U}|a_{\rho,0}(tU)|
}{|a_{\rho_0,0}(tU)|}
\ll
U^{A(\nu+\varepsilon)/2}
 e^{-cR},
\qquad
c=\eta-\frac{\nu+\varepsilon}{2}>0.
}
\tag{24}
\]

No spacing, simplicity, pair correlation, or cancellation among the shell zeros is used. Multiplicity is already charged to the zero-density count.

## 3. Pintz turns the finite-edge observation tax into `O((1-Theta)^(3/2))`

Assume now

\[
\delta:=1-\Theta<\frac1{12}.
\tag{25}
\]

Take any fixed

\[
h>\delta
\]

sufficiently close to `delta`, and put

\[
\sigma_-:=1-h<\Theta.
\]

Pintz's bound (11) supplies (19) with

\[
\nu=\nu_P(h)
=3\sqrt2\,h^{3/2}+18h^2.
\tag{26}
\]

Suppose the available one-sided observation window is

\[
(1-\kappa)U\le u\le U.
\]

To obtain a nonempty early subwindow on which (24) holds, it is enough to choose

\[
\frac{\nu_P(h)}2<\eta<\kappa.
\tag{27}
\]

Because `nu_P` is continuous, such fixed `h>delta` and `eta` exist whenever

\[
\boxed{
\kappa>
\frac{\nu_P(\delta)}2
=
\frac{3}{\sqrt2}\delta^{3/2}+9\delta^2.
}
\tag{28}
\]

Thus (28) is a source-specific sufficient observation-width condition for the scale-maximal rightward-shell mechanism. Once (28) holds, there are fixed `h>delta`, `eta<kappa`, `epsilon>0`, and `c_*>0` such that uniformly on

\[
(1-\kappa)U\le u\le(1-\eta)U
\]

one has

\[
\boxed{
\frac{
\sum_{\beta\ge\beta_0+R/U}|a_{\rho,0}(u)|
}{|a_{\rho_0,0}(u)|}
\ll
U^{C_*}e^{-c_*R}.
}
\tag{29}
\]

In particular, choosing

\[
R=\lambda\log U
\]

with sufficiently large fixed `lambda` makes the whole sufficiently-rightward shell `o(1)` relative to the anchor throughout that early subwindow.

The earlier Ingham input had

\[
\nu_I(\Theta)
=
\frac{3\delta}{1+\delta},
\]

so its corresponding width tax was

\[
\tau_I(\delta)
=
\frac{3\delta}{2(1+\delta)}.
\tag{30}
\]

Pintz instead gives

\[
\tau_P(\delta)
=
\frac{3}{\sqrt2}\delta^{3/2}+9\delta^2.
\tag{31}
\]

For every `0<delta<1/12`, the explicit envelope (31) is already smaller than (30), and as `delta->0`,

\[
\boxed{
\frac{\tau_P(\delta)}{\tau_I(\delta)}
=\sqrt2\,\delta^{1/2}+O(\delta).
}
\tag{32}
\]

For example, at `Theta=0.99` (`delta=0.01`), the sufficient tax falls from approximately `0.01485` to `0.00302`. The number is only a sanity check; the structural point is the exponent change from `delta` to `delta^(3/2)`.

## 4. The weighted high tail receives the same exponent upgrade

The same zero-density substitution applies to the exterior tail mechanism of `RE-141`. From (11) and partial summation,

\[
\sum_{\substack{|\gamma|>T\\ \beta\ge1-h}}
\frac1{\gamma^2}
\ll_{\varepsilon,h}
T^{-2+\nu_P(h)+\varepsilon}.
\tag{33}
\]

As in `RE-141`, choose `h>delta` fixed and close to `delta`; zeros further left receive exponential horizontal damping on any fixed early part of the observation window. Letting `h` approach `delta` at the level of fixed constants therefore replaces the Ingham tail exponent

\[
-2+\frac{3\delta}{1+\delta}
\]

by the sufficient Pintz exponent

\[
\boxed{
-2+3\sqrt2\,\delta^{3/2}+18\delta^2+\varepsilon.
}
\tag{34}
\]

Thus near a zero edge close to `1`, the Robin coefficient's reciprocal-square decay is now lost only by `O(delta^(3/2))` to global zero density, rather than `O(delta)`. This strengthens the exterior budget but does not alter the local near-left matched obstruction.

## 5. Adversarial stress test

**Does (28) apply Pintz directly at the possibly unattained edge `Theta`?** No. The proof fixes `h>delta`, hence `sigma_-=1-h<Theta`, before `U` tends to infinity. Strong scale maximality gives `beta_0->Theta`, so eventually `beta_0>sigma_-`. Continuity of the explicit envelope then permits `h` to be chosen sufficiently close to `delta`. No zero at `beta=Theta` is assumed.

**Is the `3 sqrt(2)` coefficient being inferred from Pintz's asymptotic Theorem 2 with a hidden epsilon/edge diagonalization?** No. Equations (5)--(10) derive the smooth envelope directly from the fixed-`h` Theorem 1. Theorem 2 is only a consistency check on the leading constant.

**Could multiplicity or very small zero spacing defeat (20)?** No. The zero-density count is with multiplicity, and partial summation uses only the counting function. No minimum spacing enters.

**Does a thinner required early window make `RE-144` impossible?** No. `RE-144` hides through a one-sided near-left product cluster. The present argument prices only zeros with `beta>=beta_0+R/U`; it says nothing about the cluster on the other side of the anchor.

**Does (29) already dominate the local visibility floor of `RE-136`/`RE-145`?** Not automatically. The shell decay constant and the local floor constant are different, and the point where local visibility is achieved has not been synchronized with the early subwindow. This finding improves one side of that comparison but does not perform the missing splice.

**Could a more modern density estimate improve the numerical envelope further?** Yes. Equation (22) is deliberately stated for an arbitrary admissible exponent `nu`; any stronger published high-sigma bound can be inserted. The canonical claim here is narrower: Pintz's explicit theorem already changes the edge order of the tax from one to three-halves, so Ingham is no longer the correct quantitative bottleneck in `RE-146` near `Theta=1`.

## 6. Representation, prior-art boundary, and research effect

No new arithmetic coordinate is introduced. The representation is exactly the leading strict-subedge Robin packet used by `RE-141`--`RE-146`, with the same scale-maximal anchor and the same one-sided macroscopic observation window. The only changed ingredient is the source theorem used to count sufficiently rightward zeros after scale maximality has forced their ordinates upward.

The load-bearing literature input is János Pintz, *Density theorems for Riemann's zeta-function near the line Re s = 1*, Acta Arithmetica **208** (2023), no. 1, 1--13, DOI `10.4064/aa210824-10-5`, especially Theorem 1 and its explicit `B(h)` family. A targeted prior-art search also checked modern zero-density compilations and Robin/divisor-sum searches. The density estimates themselves are classical/current analytic-number-theory input; no source located states the scale-maximal Robin shell transfer (22), the observation-width threshold (28), or the comparison with the reciprocal-box visibility program.

The research consequence is therefore precise. On the strong scale-maximal branch with a finite edge `Theta>11/12`, **global zero density is substantially cheaper than `RE-146` recorded**: near `Theta=1` it consumes only `O((1-Theta)^(3/2))` of the macroscopic observation window and only `O((1-Theta)^(3/2))` of the reciprocal-square high-tail exponent. The unresolved work is pushed more decisively toward the genuinely local geometry: the near-left shell, vertically remote modes with nearly unchanged real part, and witness synchronization.