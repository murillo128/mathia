# NB-147 — Reflection closure exactly interpolates the positive Poisson occupancy coefficient

**Status:** `EXACT-DERIVED + SOURCE-SPECIFIC + EULER-PRODUCT + REFLECTION-CLOSURE + LOCAL-OCCUPANCY + METHOD-OPTIMALITY + NB-146-COMPLETION`.

`NB-146` identified two endpoint regimes for positive exterior Poisson sampling: a separated one-sided packet near the critical line has limiting coefficient `1/8`, while a reflection-closed symmetric packet has coefficient `1/4`. It also left arbitrary asymmetric cells crossing `Re s=1/2` open because the answer depends on which reflected partners are already counted.

The missing invariant is the **reflection closure of the counted packet**. Once the packet is closed under the functional-equation involution, the positive-sampling problem has one exact weighted quantity, and the apparent factor-two boundary jump becomes an interpolation by the amount of reflection boundary exposed by the packet.

Let

\[
J(\rho):=1-\overline\rho,
\qquad
L:=\log G,
\]

and let `C_G` be any finite packet of actual nontrivial zeta zeros, counted with their full multiplicities, satisfying

\[
 t_G\in[G,2G],
 \qquad
 |\gamma-t_G|\le h_G=o(1),
 \qquad
 \eta\le\beta\le1-\eta
\tag{1}
\]

for some fixed `eta>0`. Define its reflection closure as the multiset union

\[
\widehat C_G:=C_G\cup J(C_G),
\tag{2}
\]

where an orbit member already present in `C_G` is not counted twice. Then

\[
\boxed{
 \sum_{\rho\in\widehat C_G}
 \frac1{1-\beta}
 \le
 \left(\frac12+o(1)\right)L.
}
\tag{3}
\]

Moreover `(3)` is the exact leading certificate available from the whole positive exterior Poisson architecture of `NB-146` when the prime side is controlled only by the pointwise absolute Euler-product majorant. Arbitrary positive multi-point or continuous sampling cannot assign more leading Poisson charge to `\widehat C_G` than the left side of `(3)` times the sampler mass, while the single sample

\[
 s_G=1+L^{-1/2}+it_G
\tag{4}
\]

attains that charge up to `1+o(1)` with `o(L)` Euler-side cost.

The near-critical consequence is especially simple. Suppose additionally

\[
 |\beta-1/2|\le r_G=o(1)
 \qquad(\rho\in C_G).
\tag{5}
\]

Write

\[
 d_G:=|C_G|,
\]

and let `b_G` be the total multiplicity of packet zeros whose reflected partner is not already in the packet:

\[
 b_G:=\#\{\rho\in C_G:J(\rho)\notin C_G\}.
\tag{6}
\]

Then the closure has exactly

\[
 |\widehat C_G|=d_G+b_G,
\tag{7}
\]

so `(3)` becomes

\[
\boxed{
 d_G+b_G
 \le
 \left(\frac14+o(1)\right)L.
}
\tag{8}
\]

If `d_G>0` and

\[
 q_G:=\frac{b_G}{d_G}\in[0,1],
\tag{9}
\]

then

\[
\boxed{
 d_G
 \le
 \left(
 \frac{1}{4(1+q_G)}+o(1)
 \right)L.
}
\tag{10}
\]

Thus `q_G=0` gives the self-dual coefficient `1/4`, `q_G=1` gives the separated one-sided coefficient `1/8`, and every partially exposed packet lies quantitatively between them. The Poisson kernel itself never jumps; what changes is the ratio between the counted packet and its reflection closure.

## Derivation

For `s=1+delta+iv`, write

\[
P_{\delta,v}(\rho)
:=
\frac{1+\delta-\beta}
{(1+\delta-\beta)^2+(v-\gamma)^2}.
\tag{11}
\]

The logarithmic-derivative identity and the absolutely convergent von Mangoldt series used in `NB-144` and `NB-146` give, at `(4)`,

\[
\sum_\rho P_{L^{-1/2},t_G}(\rho)
\le
\frac12L+O(\sqrt L).
\tag{12}
\]

Every term is nonnegative. For `rho in \widehat C_G`, `(1)` implies uniformly

\[
P_{L^{-1/2},t_G}(\rho)
=
\frac1{1-\beta}+o(1).
\tag{13}
\]

Before summing the error, note that `(1)` also gives a fixed positive lower bound for every term in `(13)`. Hence `(12)` first yields `|\widehat C_G|=O(L)`. The uniform `o(1)` error in `(13)` therefore sums to `o(L)`, and retaining only the closure terms in `(12)` proves `(3)`.

For the method-optimality statement, let `mu_G` be any finite positive measure on exterior samples `s=1+delta+iv`, with `0<delta<=1` and `|v|` comparable with `G`, and let `W_G` be its mass. Pointwise,

\[
P_{\delta,v}(\rho)
\le
\frac1{1+\delta-\beta}
\le
\frac1{1-\beta}.
\tag{14}
\]

Therefore the total integrated charge that any such sampler can place on the selected reflection closure satisfies

\[
\sum_{\rho\in\widehat C_G}
\int P_{\delta,v}(\rho)\,d\mu_G
\le
W_G
\sum_{\rho\in\widehat C_G}\frac1{1-\beta}.
\tag{15}
\]

The common positive budget has unavoidable leading term `(1/2)L W_G`; controlling the prime side only by the absolute Euler-product majorant adds a nonnegative cost `\int delta^{-1}d\mu_G+O(W_G)`. Hence no positive sampler in this architecture can force a smaller leading threshold for the weighted closure mass than `(1/2)L`. The one-point sampler `(4)` makes `(13)` simultaneous for every closure zero and has `delta^{-1}=O(\sqrt L)=o(L)`, so it reaches that threshold. This proves the claimed minimax exactness.

Under `(5)`, every member of the closure also satisfies `beta=1/2+o(1)`, so every weight in `(3)` is `2+o(1)`. Functional-equation symmetry preserves multiplicity. Every packet occurrence whose partner is absent contributes one new occurrence to the closure; every already completed two-element orbit and every critical-line fixed point contributes none. This proves `(7)`--`(10)`.

## A concrete asymmetric-cell corollary

Take a right-shifted cell whose horizontal interval is

\[
I_G=
\left[
\frac12+a_G-r_G,
\frac12+a_G+r_G
\right],
\qquad
0\le a_G\le r_G=o(1),
\tag{16}
\]

and whose vertical radius is `o(1)`. Reflection maps `I_G` to the interval centered at `1/2-a_G`. A zero of `C_G` has its reflected partner still inside the cell exactly when

\[
\beta\le\frac12+r_G-a_G.
\tag{17}
\]

Thus `b_G` is precisely the multiplicity in the exposed right flank

\[
\frac12+r_G-a_G<\beta\le\frac12+a_G+r_G.
\tag{18}
\]

If that flank count is `f_G`, `(8)` reads

\[
\boxed{
 d_G+f_G
 \le
 \left(\frac14+o(1)\right)L.
}
\tag{19}
\]

This gives a direct quantitative penalty for asymmetry of a cell crossing the critical line.

A useful rigidity consequence is that a near-critical packet with almost maximal self-dual occupancy must be almost reflection-saturated. If

\[
 d_G\ge\left(\frac14-\varepsilon_G\right)L,
 \qquad
 \varepsilon_G\to0,
\tag{20}
\]

then `(8)` forces

\[
\boxed{
 b_G\le \varepsilon_G L+o(L)=o(L).
}
\tag{21}
\]

So a packet approaching the `1/4` ceiling cannot contain a positive proportion of one-sided reflection orbits.

## Stress tests and boundaries

The closure in `(2)` is essential. Counting `C_G` and `J(C_G)` with multiplicity **twice** when both orbit members already belong to `C_G` recreates exactly the endpoint error corrected in `NB-146`. Critical-line zeros are fixed points of `J` and are counted once. Distinct off-line partners already present in the packet are also each counted once.

The compact-substrip hypothesis in `(1)` keeps `1/(1-beta)` uniformly bounded and makes the one-point approximation `(13)` uniform. Near `Re s=1`, the moving-scale analysis of `NB-144` is the appropriate formulation instead. The vertical tightness `h_G=o(1)` is likewise load-bearing for simultaneous saturation by the single sample `(4)`; without it, different ordinates cannot all attain their pointwise Poisson maxima at one `v`.

This remains a local occupancy law, not a Nyman target-coercivity theorem. It still permits `Theta(log G)` packets. It does not exclude off-critical zeros, prove RH, or show that surviving packets are target-bearing. Signed sampling, cancellation or correlations on the von Mangoldt side, higher moments, and target-projection information remain outside the positive cone classified here.

## Relation to earlier findings

`NB-144` is recovered by taking a separated right-half packet: the reflection closure adds one distinct partner for every counted zero, and its two weights tend to `1/epsilon+1/(1-epsilon)`. `NB-146` is recovered near the critical line at the two extremes `q_G=1` and `q_G=0`. The present result fills the explicit gap left there for asymmetric cells crossing the critical line and identifies the weighted reflection closure, rather than the packet center, as the exact invariant of the positive Poisson certificate.

The near-critical law `(10)` also removes the appearance of a literal analytic discontinuity at `Re s=1/2`: `1/8` and `1/4` are the two endpoint values of one orbit-exposure parameter. What was discontinuous in `NB-146` was the choice of packet geometry being compared, not the kernel.

## Prior art and sources

The load-bearing analytic ingredients are unchanged from `NB-144`/`NB-146`: the classical logarithmic-derivative/Hadamard identity, positivity of its zero Poisson kernel for `Re s>1`, the absolutely convergent Euler-product majorant for `zeta'/zeta`, and functional-equation symmetry of the zero divisor. They are already anchored by `INT-RIEMANN-EXPLICIT` and the existing Nyman-Beurling source file, so no new `SOURCES.md` entry is required.

A targeted literature check found standard treatments of zeta log-derivative bounds and the symmetry of nontrivial zeros, but no separate theorem phrased as the reflection-closure weighted occupancy law `(3)` or the exposure interpolation `(10)`. The claim of this finding is therefore the derived packet-level classification and its exact method boundary, not novelty of the classical explicit-formula ingredients.

## Consequence for the line

Positive exterior Poisson sampling is now classified not only in the two clean regimes of `NB-146` but for arbitrary tight interior packets through the reflection-closure mass `(3)`. Adding positive samples cannot improve that invariant. A near-critical packet can approach the weaker `1/4` occupancy ceiling only by becoming asymptotically reflection-saturated; a one-sided packet pays the full `1/8` ceiling.

This sharpens the remaining source problem without solving it: any route from local zeta information to the `o(log G)` confluence law needed by the Nyman branch must use structure not contained in positive Poisson mass plus the absolute Euler-product bound, or must convert the surviving reflection-saturated logarithmic packets into target-bearing states.