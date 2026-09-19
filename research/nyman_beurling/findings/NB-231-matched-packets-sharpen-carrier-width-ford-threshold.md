# NB-231 — Matched packets make `YD-log J` the sharp Bellotti carrier coordinate

**Date:** 2026-09-19  
**Status:** `DERIVED + NEGATIVE/METHOD-BOUNDARY + ZETA-SPECTRAL-MATCHED-CONTROL + EXACT-FORD-SCALE + CARRIER-WIDTH/DEPTH-SHARPNESS + PHASE-ALIGNED-PACKET + NB-225/NB-230-SYNTHESIS + SOURCE-ONLY + PRIOR-ART-AUDITED`.

`NB-230` proves an absolute upper transition for the exact-Ford residue carrier. With

\[
Q=\log(10+|t|),\qquad L=\log Q,\qquad R=Q^{2/3}L^{1/3},
\]

\[
Y=\frac XR\to Y_*\in(0,\infty),\qquad J=1+\frac RH,
\]

its Bellotti local-count argument gives

\[
\mathcal T(D_0,D_1)\ll e^{-YD_0}(D_0+J+1).
\]

Hence every moving depth with

\[
YD_0-\log J\to+\infty
\]

is already absolutely harmless.

The remaining issue is whether the `log J` threshold is merely an artifact of the upper bound. In the regime where the whole vertical carrier capacity still fits inside the already-audited growing-density allowance, it is not. If

\[
J\to\infty,\qquad J\le L,
\]

then for every fixed bounded offset `w` one can build an abstract zero packet, compatible with all population inputs used in `NB-225` and `NB-230`, at depth

\[
\boxed{D=\frac{\log J+w}{Y}}
\]

whose exact signed residue contribution stays bounded away from zero. The packet uses `Theta(J)` zeros, occupies only a fixed small fraction of the actual `1/H` vertical carrier, and has perfectly aligned moving-shell phases.

Thus, for the information set currently available, the transition variable is genuinely

\[
\boxed{YD-\log J.}
\]

`NB-230` proves decay when it tends to `+infinity`; the construction below shows that no population-only argument from the same hypotheses can force decay when it remains `O(1)`. In this controlled carrier-capacity regime even the **diverging additive margin** in `NB-230` is sharp.

This is a method boundary, not a claim that the actual zeta zeros realize the packet. It strengthens `NB-225` by using a fixed positive fraction of the carrier capacity rather than only an `o(J)` packet, and it closes the constant-scale gap between the lower obstruction and the upper cutoff of `NB-230`.

## 1. Exact carrier and the width budget

Fix `r>0` and a nonzero real profile

\[
\phi\ge0,\qquad \phi\in C_c^\infty((0,1)).
\]

As in `NB-224`--`NB-230`, set

\[
\sigma_X=1+\frac rX,
\qquad
h_{X,H}(u)=\frac1H\phi\!\left(\frac{u-X}{H}\right),
\]

and

\[
F(z)=\int_0^1\phi(y)e^{izy}\,dy.
\]

Then `F(0)>0`. For a zero `rho=beta+i gamma`, with

\[
d_\rho=R(1-\beta),
\qquad
v_\rho=(\gamma-t)+i(\sigma_X-\beta),
\]

the exact residue coefficient is

\[
L_{X,H}(v_\rho)
=
 e^{-r}e^{-Yd_\rho}
 e^{iX(\gamma-t)}F(Hv_\rho).
\tag{1}
\]

For the packet construction it is cleaner to write

\[
J_0:=\frac RH.
\]

Since the present regime has `J_0->infinity`, the harmless `+1` in the `NB-230` convention satisfies `J=1+J_0~J_0`. Replacing `log J_0` by `log J` changes only `o(1)` below, so we use `J_0` in the construction and translate back at the end.

Assume

\[
J_0\to\infty,
\qquad
J_0\le L.
\tag{2}
\]

The second condition is not needed by the carrier algebra. It is the conservative condition that keeps a `Theta(J_0)` packet inside the same `O(L)` population envelope already verified in `NB-225` against Bellotti's growing near-one density theorem and ordinary local zero counting.

## 2. A fixed fraction of the carrier can stay in one coherent profile patch

Because `F` is entire and `F(0)>0`, there is an `epsilon_F>0` such that

\[
|\Re z|\le\epsilon_F,
\qquad
0\le\Im z\le\epsilon_F
\]

implies

\[
\Re F(z)\ge \frac12F(0).
\tag{3}
\]

Choose a fixed positive integer `q`, large enough only to make the local spacing constant compatible with Bellotti's disk-count constant, exactly as in `NB-225`. Since `Y->Y_*>0`, choose a fixed `delta>0` so small that

\[
\frac{4\pi q\delta}{Y_*}<\epsilon_F.
\tag{4}
\]

Put

\[
M=\lfloor\delta J_0\rfloor.
\tag{5}
\]

Unlike the deliberately conservative choice `M<=J_0^{1/2}` in `NB-225`, this packet consumes a fixed positive fraction of the full vertical capacity. It still fits inside a fixed small fraction of the Fourier carrier.

Indeed choose the ordinates

\[
\gamma_j
=t+\frac{2\pi qj}{X},
\qquad 1\le j\le M.
\tag{6}
\]

Then

\[
e^{iX(\gamma_j-t)}=1
\tag{7}
\]

for every `j`, while

\[
H|\gamma_j-t|
\le
\frac{2\pi qHM}{X}
=
\frac{2\pi q}{Y}\frac{M}{J_0}
\le
\frac{2\pi q\delta}{Y}+o(1)
<\frac12\epsilon_F
\tag{8}
\]

for all sufficiently large `Q`.

Thus exact phase alignment is compatible with occupying `Theta(J_0)` carrier slots; one does not need the packet to collapse into an `o(1)` neighborhood of the carrier origin.

## 3. Put the packet exactly on the `NB-230` transition

Let `w=w(Q)` be any real quantity satisfying

\[
|w|\le W
\tag{9}
\]

for some fixed `W`, and define

\[
D=\frac{\log J_0+w}{Y}.
\tag{10}
\]

Place simple packet zeros at

\[
\rho_j
=1-\frac DR+i\gamma_j,
\qquad 1\le j\le M.
\tag{11}
\]

Since `J_0->infinity`,

\[
D\to\infty.
\tag{12}
\]

The horizontal Ford damping is exactly

\[
e^{-YD}
=
\frac{e^{-w}}{J_0}.
\tag{13}
\]

The imaginary displacement inside `F` is still negligible:

\[
H(\sigma_X-\beta_j)
=
\frac{rH}{X}+\frac{HD}{R}
=
\frac{r}{YJ_0}+\frac{D}{J_0}
=o(1),
\tag{14}
\]

because `D=O(log J_0)` and `log J_0/J_0->0`. Together with (8), equation (3) gives, uniformly in `j`,

\[
\Re F(Hv_{\rho_j})\ge\frac12F(0)
\tag{15}
\]

for all sufficiently large `Q`.

Insert (7), (13), and (15) into the exact coefficient (1). The packet contribution satisfies

\[
\begin{aligned}
\Re\sum_{j=1}^M L_{X,H}(v_{\rho_j})
&=
 e^{-r}\frac{e^{-w}}{J_0}
 \sum_{j=1}^M \Re F(Hv_{\rho_j})\\
&\ge
 e^{-r}\frac{e^{-w}}{J_0}
 M\frac{F(0)}2.
\end{aligned}
\]

Since `M/J_0->delta`,

\[
\boxed{
\liminf_{Q\to\infty}
\Re\sum_{j=1}^M L_{X,H}(v_{\rho_j})
\ge
\frac{\delta F(0)}2e^{-r-W}>0.
}
\tag{16}
\]

This is the sharpness statement. A bounded value of

\[
YD-\log J_0=w
\]

still permits an order-one exact residue contribution. By contrast `NB-230` gives `o(1)` as soon as this quantity tends to `+infinity`.

The distinction is not a hidden constant in a covering estimate. It is realized by an explicit coherent packet using the actual moving-shell phase and the actual Fourier profile.

## 4. The packet obeys the same population information as `NB-225`

The checks are the same in nature as `NB-225`, but the larger cardinality `M~delta J_0` must be kept explicit.

First, the Vinogradov--Korobov zero-free boundary has fixed normalized depth. Equation (12) puts the packet eventually to the left of every such fixed boundary, so it does not contradict the zero-free region.

Second, from `J_0<=L`,

\[
D=O(\log L)=o(L^\alpha)
\tag{17}
\]

for every fixed `alpha>0`, while

\[
M\le\delta L.
\tag{18}
\]

This is still within the growing near-one population allowance audited in `NB-225`: at these depths Bellotti's theorem permits asymptotically far more than `O(L)` points. Fixed-depth density bounds do not see the packet at all because `D->infinity`.

Third, the ordinate spacing is

\[
\gamma_{j+1}-\gamma_j
=\frac{2\pi q}{X}
\asymp_{Y_*,q}\frac1R.
\tag{19}
\]

A disk centered on the `1`-line with radius `K/R` misses the packet when `K<D` horizontally. When `K>=D`, it intersects a vertical interval of length `O(K/R)` and therefore contains at most `O_{Y_*,q}(K)` packet points. Choosing the fixed `q` large enough makes the implied spacing constant compatible with Bellotti's local `O(K)` disk law throughout its range. The fact that the *full* packet has `Theta(J_0)` points causes no violation because a Bellotti disk of depth `K~D~log J_0` only sees `O(D)` consecutive points at once.

Finally,

\[
M=O(L)=o(Q),
\tag{20}
\]

so ordinary unit-interval zero counting leaves ample room. Conjugate and functional-equation-reflected partners may be added exactly as in `NB-225`; they do not alter the local near-one carrier at `+t`.

Thus every population theorem used in the current endpoint route permits the packet. What it does not permit, after `NB-230`, is moving the same order-one mass a **diverging additive distance** beyond the `YD=log J` balance.

## 5. The carrier-width cutoff is an information-theoretic phase transition

Combining `NB-230` with (16) gives a clean two-sided statement for the audited information set when `1<<J_0<=L`:

\[
\boxed{
YD-\log J_0\to+\infty
\quad\Longrightarrow\quad
\text{absolute residue tail }=o(1),
}
\tag{21}
\]

whereas

\[
\boxed{
YD-\log J_0=O(1)
\quad\Longrightarrow\quad
\text{the same hypotheses permit an order-one coherent packet.}
}
\tag{22}
\]

So `log J` is not merely the right order of magnitude. In this regime its coefficient and the need for a diverging additive margin are sharp for every argument that uses only the currently audited zero-free and population inputs.

This also clarifies the relation to `NB-225`. There the choice

\[
M\le J_0^{1/2}
\]

was intentionally made so that `F(Hv)=F(0)+o(1)` uniformly. That was sufficient to prove a population-only obstruction but spent only a vanishing fraction of the available carrier. Here continuity on a **fixed** small profile patch is enough. Spending `M~delta J_0` raises the packet from depth roughly `(1/2Y)log J_0` to the exact balance `(1/Y)log J_0+O(1)`.

For much larger capacities, for example `J_0>>L`, this finding deliberately makes no sharpness claim at the full `log J_0` depth. The carrier itself can hold `Theta(J_0)` aligned points, but the conservative compatibility check with the growing-density theorem can no longer be certified merely from `M<=L`. That is a separate population question and should not be hidden inside the carrier construction.

## 6. Representation audit and surviving frontier

The packet is an abstract spectral control, not a constructed subset of the true zeta zero set. Therefore (22) is a logical no-go for the present theorem package, not evidence that zeta actually saturates the threshold.

The result is also still source-side. It sharpens the exact residue carrier governing the positive Euler return, but it does not prove that a small Nyman--Beurling approximation error must realize that return. The destination bridge remains independent.

Within the source problem, however, the next theorem is now tightly specified. In the regime `1<<J<=L`, no improvement of the `NB-230` cutoff is available from population information alone: an actual-zeta input must rule out the phase-aligned `Theta(J)` packet **inside** the bounded transition coordinate `YD-log J=O(1)`. Suitable information would have to couple horizontal depth to vertical phase or spacing in a way stronger than the local `O(D)` disk population law. Improving estimates only for `YD-log J->+infinity` targets a region that is already absolutely harmless.

## 7. Prior-art and self-review boundary

No new external theorem is used. The load-bearing inputs are exactly the Bellotti zero-free, growing-density, and local disk-count statements already anchored for `NB-224`--`NB-230`; the new step is the larger matched-packet construction and the exact comparison with the `NB-230` upper transition.

The most delicate check is the Fourier profile. Taking `Theta(J)` points means `Hv_j` no longer tends to zero in its real component. Equation (3) is why the argument remains valid: the packet is restricted to a sufficiently small **fixed** fraction `delta` of the carrier, where continuity keeps the real part of `F` positive. No unjustified `F(Hv)=F(0)+o(1)` claim is made.

The second delicate check is density compatibility. The restriction `J<=L` is intentional and load-bearing for the clean statement. Removing it would require re-auditing Bellotti's growing-depth density allowance against `Theta(J)` points and cannot be inferred from the carrier algebra alone.

Finally, the packet contribution is measured using the exact residue coefficient (1), before absolute values. Because the moving phase is exactly `1` and `Re F` stays positive on the chosen profile patch, the lower bound is genuinely signed and cannot be dismissed as an absolute-mass artifact.

## Conclusion

For carrier capacities `1<<R/H<=log log|t|`, the `NB-230` variable

\[
YD-\log\!\left(1+\frac RH\right)
\]

is the sharp transition coordinate for the presently audited source information. A diverging positive value kills the residue absolutely; any bounded value still admits a Bellotti-compatible, fully phase-aligned packet carrying order-one mass.

The unresolved source theorem has therefore become very local: it must exclude an actual-zeta coherent packet **at the transition itself**, not improve control above it. That is the point where new depth-phase arithmetic information is now genuinely required.
