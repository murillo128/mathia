# XF-099 — collision crystal is exactly invisible below the symmetry frequency

**Status:** `EXACT-DERIVED` + `NEGATIVE/OBSTRUCTION` + `MATCHED-CONTROL` + `COLLISION-SAFE` + `LITERATURE-CALIBRATED`. XF-097 closes the current source-to-periodic bridge in the guarded power-sum resource, while XF-098 shows that an isolated periodic collision can remain `o(1)` in that resource under the full heat flow. The natural remaining hope is that a genuinely collective transition — many simultaneous or correlated collisions — must become visible in the same low-frequency prefix. That implication is false without an additional Xi-specific anti-aliasing input.

There is an explicit degree-`N=2M` periodic backward-heat trajectory with **`M=N/2` simultaneous simple double collisions at its transition time**, yet every power sum `P_m` with `1 <= m < M` vanishes identically for the entire trajectory. Hence any current guarded band `1 <= m <= K` with `K=o(M)` has exactly zero resource, not merely `o(1)`, even though every one of the `N` roots participates in the transition. Relative to the fine arithmetic `N`-lattice, the collision state also has multiplicity-counting discrepancy at most one. Thus neither collision count/density nor a Riemann--von Mangoldt-type local counting envelope, by themselves, can supply the missing destination coercivity. The surviving gate is genuinely spectral/Xi-specific: one must force symmetry-breaking mass into the visible modes (or change the observable).

## 1. A maximally collective periodic transition

Use the periodic variables and normalization of XF-067/XF-079. Let

\[
N=2M,\qquad L=Ns,\qquad w=e^{2\pi i z/L}.
\tag{1}
\]

At transition time `t=0`, take the monic root polynomial

\[
\boxed{
F_0(w)=(w^M-1)^2=w^{2M}-2w^M+1.
}
\tag{2}
\]

Its root multiset consists of the `M`th roots of unity, each with multiplicity two. In the physical periodic coordinate these are

\[
\boxed{
x_{r,+}(0)=x_{r,-}(0)=2rs\pmod L,\qquad 0\le r<M.}
\tag{3}
\]

Thus there are exactly `M=N/2` distinct collision locations, every collision is double rather than higher order, and every root belongs to one of them.

XF-067 gives the exact normalized backward-heat evolution of the Vieta coefficient `E_k`:

\[
E_k(t)=E_k(0)e^{-\delta_k t},
\qquad
\delta_k=\frac{4\pi^2}{L^2}k(N-k).
\tag{4}
\]

For (2), the only nonzero interior coefficient is the middle one `k=M`. Since

\[
\delta_M=\frac{4\pi^2M^2}{L^2}=\frac{\pi^2}{s^2},
\tag{5}
\]

the root polynomial along the full normalized heat trajectory is therefore exactly

\[
\boxed{
F_t(w)=w^{2M}-2\alpha(t)w^M+1,
\qquad
\alpha(t)=e^{-\pi^2t/s^2}.
}
\tag{6}
\]

No root ODE or simplicity assumption is used here; (6) is the collision-safe coefficient evolution itself.

For `t>0`, put `theta(t)=arccos(alpha(t))`. Then

\[
F_t(w)=
(w^M-e^{i\theta(t)})(w^M-e^{-i\theta(t)}),
\tag{7}
\]

so all `2M` roots lie on the unit circle and are simple:

\[
\boxed{
 x_{r,\pm}(t)
 =2rs\pm\frac{s}{\pi}\theta(t)
 \pmod L.
}
\tag{8}
\]

For `t<0`, write `eta(t)=arcosh(alpha(t))>0`. Then

\[
F_t(w)=(w^M-e^{\eta(t)})(w^M-e^{-\eta(t)}),
\tag{9}
\]

so one `M`-gon has radius `e^{eta/M}` and the other radius `e^{-eta/M}`. None of the roots lies on the unit circle. Hence the corresponding zeros in the physical `z` coordinate are nonreal. Consequently

\[
\boxed{
F_t\text{ is real-rooted in the periodic coordinate exactly for }t\ge0.
}
\tag{10}
\]

This is an explicit finite de Bruijn--Newman-type threshold at `t=0`, not just a local collision expansion. Expanding `theta(t)` at zero gives `theta(t)=pi sqrt(2t)/s+O(t^{3/2})`, so the squared gap inside each pair is

\[
\left(\frac{2s}{\pi}\theta(t)\right)^2
=8t+O(t^2),
\tag{11}
\]

matching the universal simple-double-collision law used in XF-098.

## 2. Every low power sum is identically zero through the transition

The root multiset of (6) is invariant under multiplication by every `M`th root of unity. For `t>0`, (7) gives directly

\[
\begin{aligned}
P_m(t)
&=\sum_{r=0}^{M-1}
\left[
 e^{im(\theta+2\pi r)/M}
 +e^{im(-\theta+2\pi r)/M}
\right]\\
&=2\cos\!\left(\frac{m\theta}{M}\right)
\sum_{r=0}^{M-1}e^{2\pi i mr/M}.
\end{aligned}
\tag{12}
\]

The geometric sum vanishes whenever `M` does not divide `m`. The same conclusion follows from the rotational symmetry of (6) at `t=0` and `t<0`. Therefore

\[
\boxed{
P_m(t)=0
\qquad
\text{for every real }t\text{ and every }1\le m<M.
}
\tag{13}
\]

Equivalently, all log-Vieta coordinates

\[
c_m(t)=(-1)^{m-1}\frac{P_m(t)}m
\tag{14}
\]

vanish identically below the first symmetry frequency `M`. This is stronger than the triangular stability estimate in XF-098: no nonlinear replenishment can occur because the exact heat trajectory remains inside the `M`-fold symmetric three-term family (6).

At the current Xi-flow scales,

\[
M=q^2,
\qquad
K=O(q\log\log T)=o(M).
\tag{15}
\]

Hence for all sufficiently large parameters every visible guarded sideband lies below `M`. Using the exact XF-079 resource formula, for any guarded set `B` supported on those sidebands,

\[
\boxed{
\|\mathcal S_r(t)\|_{X(B)}^2
=
\frac1{4M^2}
\sum_{m\in B}|P_m(t)|^2 I_m
=0
}
\tag{16}
\]

for every translated center `r` and every `t>=0` (indeed for every real `t` at the algebraic power-sum level). Thus the present destination resource is **exactly blind** to this maximally collective transition.

## 3. Collision mass and counting discrepancy do not repair the blind spot

Compare the transition state (3) with the fine arithmetic `N`-lattice

\[
X_{\rm lat}=\{0,s,2s,\ldots,(N-1)s\}.
\tag{17}
\]

The collision crystal is obtained by moving every odd lattice node one lattice unit to the preceding even node. In the sparse-displacement notation of XF-098 this has

\[
\boxed{A_1=M=N/2.}
\tag{18}
\]

This is far beyond the XF-098 sufficient invisibility regime

\[
A_1=o\!\left(\frac{M^2}{K^{7/2}}\right),
\tag{19}
\]

yet (16) is still exactly zero. Therefore the `A_1` threshold in XF-098 is only a one-sided sufficient condition for invisibility; **large total displacement, even of order `N`, does not force guarded mass**. Phase organization can cancel the whole visible prefix.

Counting with multiplicity is equally insensitive. Choose a seam at a lattice point and let `N_cr(x)` and `N_lat(x)` be the two counting staircases away from their jumps. On each pair of lattice cells the difference alternates between `1` and `0`, so

\[
\boxed{
\sup_x|N_{\rm cr}(x)-N_{\rm lat}(x)|=1.
}
\tag{20}
\]

The average density is exactly the same, and the counting error is uniformly `O(1)`, despite `M` simultaneous double collisions. This does not claim that the crystal satisfies the full Xi explicit formula or any prime-frequency constraint. It does show that an argument which uses only multiplicity-counting density/envelopes cannot promote “many collisions” to a lower bound in the current guarded Fourier resource. The classical Riemann--von Mangoldt law counts zeros with multiplicity and supplies density plus a counting error; an Xi-specific coercive step must use information finer than that generic counting structure.

## 4. Prior-art calibration and novelty boundary

Periodic backward heat, preservation of real-rootedness, and the unitary-Hermite/Lee--Yang setting are classical/modern neighboring theory; Kabluchko (2025), already anchored in `SOURCES.md`, is the relevant current reference. The factorization of a reciprocal trinomial `w^(2M)-2 cos(theta) w^M+1` into two rotated regular `M`-gons is elementary and no novelty is claimed for it.

A targeted literature search did not locate the specific use of the invariant three-term heat family (6) as a de Bruijn--Newman matched control exhibiting all three properties simultaneously: an extensive set of threshold collisions, `O(1)` multiplicity-counting discrepancy from the fine lattice, and exact annihilation of every low power sum below the symmetry frequency. The Mathia-specific contribution is the conjunction of those facts with the XF-079 guarded selector and the current scale separation `K=o(M)`.

No new durable literature dependency is needed, so `SOURCES.md` is unchanged.

## 5. Boundary, falsification, and consequence for the Xi gate

This construction is **not** an Xi surrogate satisfying the source bridge of XF-097. In particular, the actual Xi prefix is not identically zero, and the prime-frequency/explicit-formula structure may rule out this exact rotational aliasing. The finding therefore does not weaken XF-097 and does not assert a counterexample to any Xi-specific positive-`Lambda` theorem.

It does falsify a stronger destination claim: no theorem based only on periodic backward heat, real-rootedness loss at a transition, the number or density of simultaneous collisions, total bounded lattice displacement, or multiplicity-counting regularity can conclude that the present low-frequency guarded resource is macroscopic. Even the maximal collision fraction `M/N=1/2` can be spectrally invisible.

The decisive audit is finite and exact: start from (2), apply the XF-067 coefficient law only to `k=M`, obtain (6), solve the quadratic in `w^M`, and evaluate the geometric sum in (12). Any normalization error must show up either as a failure of the heat multiplier in (6), a root leaving the unit circle for `t>0`, or a nonzero `P_m` with `1<=m<M`.

The remaining Xi-flow frontier is therefore narrower than after XF-098. A hypothetical `Lambda>0` must force **visible symmetry breaking**, not merely a collective collision set. A successful coercive theorem must inject Xi-specific information that prevents transition defects from organizing into a high-symmetry/aliased pattern — for example through an explicit-formula or prime-frequency constraint, a quantitative aperiodicity statement, or a different observable whose bandwidth reaches the relevant symmetry scale. Which of these is available remains open.