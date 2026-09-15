---
type: research-finding
status: active
finding_id: NB-146
research_line: nyman_beurling
created: 2026-09-15
updated: 2026-09-15
reviewed_for_relevance: 2026-09-15
sources:
  - INT-RIEMANN-EXPLICIT
review_after: 2026-10-15
---

# NB-146 — Separated right-half Poisson optimality has a factor-two self-dual boundary jump

## Summary

The positive exterior Poisson argument of `NB-144` is minimax-optimal under arbitrary positive multi-point sampling **for a packet separated from the critical line**, but its coefficient does not extend continuously to a packet centered on `Re rho = 1/2`.

For a right-half packet centered at

\[
\beta_G=1-\epsilon_G>\frac12
\]

and separated from the critical line by more than its horizontal width, functional-equation symmetry supplies a distinct reflected zero for every counted packet zero. If one uses only positivity of the Hadamard zero sum and the pointwise Euler-product majorant for `zeta'/zeta`, then no positive superposition of exterior samples can beat the leading coefficient

\[
\frac12\epsilon_G(1-\epsilon_G)\log G,
\]

and the one-point sampler of `NB-144` attains it whenever `epsilon_G log G -> infinity`.

At the self-dual boundary the orbit bookkeeping changes. A zero on the critical line satisfies

\[
1-\overline\rho=\rho,
\]

so the reflected contribution is not a second zero occurrence. For a symmetric packet centered on the critical line, with every zero counted once, the same positive-Poisson/Euler-majorant architecture has the sharp leading coefficient

\[
\frac14\log G.
\]

Thus the off-line coefficient has the limiting value `1/8` as `epsilon_G -> 1/2`, while the line-centered coefficient is `1/4`. The factor-two jump is real: away from the line, a counted right-half zero receives the Poisson mass of a distinct uncounted reflected partner for free; at the self-dual boundary that distinct partner disappears, or in a symmetric line-straddling packet it is already part of the count.

This finding supersedes the withdrawn `NB-145`, whose theorem incorrectly included the endpoint `epsilon_G=1/2` while still charging every counted zero together with a supposedly distinct reflected partner.

## Claim

Put

\[
L:=\log G,
\qquad
t_G\in[G,2G].
\]

For an exterior sample

\[
s=1+\delta+iv,
\qquad
0<\delta\le1,
\qquad
\frac G2\le |v|\le3G,
\]

define the Poisson contribution of a zero `rho=beta+i gamma` by

\[
P_{\delta,v}(\rho)
:=
\frac{1+\delta-\beta}
{(1+\delta-\beta)^2+(v-\gamma)^2}.
\tag{1}
\]

Let `mu_G` be any nonzero finite positive measure on such sample points and write

\[
W_G:=\mu_G(\Omega_G).
\tag{2}
\]

The explicit formula and the pointwise Euler-product majorant give the common positive budget

\[
\int\sum_\rho P_{\delta,v}(\rho)\,d\mu_G
\le
\frac12 L W_G
+
\int\delta^{-1}\,d\mu_G
+O(W_G).
\tag{3}
\]

Only two ingredients are permitted in the architecture considered here: zero-side positivity, which allows all unselected zeros to be discarded, and the absolute pointwise estimate

\[
\left|\frac{\zeta'}{\zeta}(1+\delta+iv)\right|
\le \delta^{-1}+O(1).
\tag{4}
\]

### A. Separated right-half packet

Assume

\[
0<\epsilon_G<\frac12,
\qquad
\beta_G:=1-\epsilon_G,
\tag{5}
\]

and let `C_G^+` consist of `d_G` actual zeta zeros, counted with multiplicity, satisfying

\[
|\beta-\beta_G|\le h_G,
\qquad
|\gamma-t_G|\le h_G,
\tag{6}
\]

with

\[
h_G=o\!\left(\min\left\{\epsilon_G,\frac12-\epsilon_G\right\}\right).
\tag{7}
\]

Condition `(7)` keeps the packet strictly in the right half-plane and makes the reflected zero

\[
\widetilde\rho:=1-\overline\rho
\tag{8}
\]

a distinct zero occurrence outside the counted packet for all sufficiently large `G`.

If `q_G^+(mu_G)` denotes the minimum integrated Poisson charge obtained by retaining a counted packet zero together with its distinct reflected partner, then

\[
q_G^+(\mu_G)
\le
\frac{1+o(1)}{\epsilon_G(1-\epsilon_G)}W_G.
\tag{9}
\]

Consequently every certificate obtained from `(3)` solely by those two permitted ingredients has asymptotic leading floor

\[
\boxed{
\text{positive-Poisson certificate for }d_G
\ \ge\
\left(\frac12-o(1)\right)
\epsilon_G(1-\epsilon_G)L.
}
\tag{10}
\]

If in addition

\[
\epsilon_G L\to\infty,
\tag{11}
\]

then the one-point choice

\[
v=t_G,
\qquad
\delta_G:=\sqrt{\frac{\epsilon_G}{L}}
\tag{12}
\]

attains

\[
\boxed{
 d_G
\le
\left(\frac12+o(1)\right)
\epsilon_G(1-\epsilon_G)L.
}
\tag{13}
\]

Thus the `NB-144` coefficient is minimax-optimal throughout the separated right-half regime covered by `(5)`--`(7)`.

### B. Critical-line-centered packet

Let `C_G^0` instead contain `d_G^0` actual zeros, counted with their actual multiplicities **once each**, in the symmetric cell

\[
\left|\beta-\frac12\right|\le h_G,
\qquad
|\gamma-t_G|\le h_G,
\qquad
h_G=o(1).
\tag{14}
\]

No reflected zero is added as an extra occurrence. Define `q_G^0(mu_G)` as the minimum integrated charge of one counted zero itself. Then

\[
q_G^0(\mu_G)
\le
(2+o(1))W_G,
\tag{15}
\]

so every certificate produced by the same architecture has the leading floor

\[
\boxed{
\text{positive-Poisson certificate for }d_G^0
\ \ge\
\left(\frac14-o(1)\right)L.
}
\tag{16}
\]

Conversely, the one-point choice

\[
v=t_G,
\qquad
\delta_G:=L^{-1/2}
\tag{17}
\]

gives

\[
\boxed{
 d_G^0
\le
\left(\frac14+o(1)\right)L.
}
\tag{18}
\]

Hence `1/4` is the exact minimax leading coefficient of this positive exterior Poisson architecture for a line-centered symmetric packet.

The two regimes do not glue continuously:

\[
\lim_{\epsilon\uparrow1/2}
\frac{\epsilon(1-\epsilon)}2
=
\frac18,
\qquad
\text{whereas at the self-dual packet }\quad
c_{\mathrm{line}}=\frac14.
\tag{19}
\]

## Derivation

### 1. The common positive budget

For `1<sigma<=2` and `|v|` comparable with `G`, the same logarithmic-derivative identity used in `NB-144` gives

\[
\sum_\rho
\frac{\sigma-\beta}
{(\sigma-\beta)^2+(v-\gamma)^2}
=
\frac12\log|v|
+
\Re\frac{\zeta'}{\zeta}(\sigma+iv)
+O(1),
\tag{20}
\]

with zeros counted with their actual multiplicities. Every term on the left is nonnegative. On `sigma=1+delta`, absolute convergence of the von Mangoldt Dirichlet series gives `(4)`. Integrating `(20)` against the positive measure `mu_G` and using `log|v|=L+O(1)` on the sample region yields `(3)`.

This step is linear in the sampling measure and therefore already includes arbitrary finite or continuous positive averaging, `G`-dependent sample placement, and adaptive positive weights. There is no extra gain hidden in passing from one point to many points unless one introduces information beyond positivity and `(4)`.

### 2. Distinct reflection doubles the usable charge off the line

For a right-half zero `rho=beta+i gamma`, functional-equation symmetry gives the distinct same-ordinate zero `(8)`. Their combined charge at one sample is

\[
\begin{aligned}
P_{\delta,v}(\rho)+P_{\delta,v}(\widetilde\rho)
={}&
\frac{1+\delta-\beta}
{(1+\delta-\beta)^2+(v-\gamma)^2}
\\
&+
\frac{\delta+\beta}
{(\delta+\beta)^2+(v-\gamma)^2}.
\end{aligned}
\tag{21}
\]

Using `x/(x^2+y^2)<=1/x`, `(6)` and `(7)` gives uniformly over the packet

\[
P_{\delta,v}(\rho)+P_{\delta,v}(\widetilde\rho)
\le
\frac1{\epsilon_G-h_G}
+
\frac1{1-\epsilon_G-h_G}
=
\frac{1+o(1)}{\epsilon_G(1-\epsilon_G)}.
\tag{22}
\]

Integration proves `(9)`. Retaining one such **distinct pair** for each of the `d_G` counted right-half zeros in `(3)` gives

\[
d_G q_G^+(\mu_G)
\le
\frac12 L W_G
+
\int\delta^{-1}\,d\mu_G
+O(W_G).
\tag{23}
\]

Within the declared proof architecture the numerator has unavoidable leading scale `(1/2)L W_G`, while `(9)` is a universal ceiling on the charge per counted zero. Therefore the right side of the resulting upper-bound certificate cannot have leading coefficient below `(10)`.

For the one-point choice `(12)`, condition `(11)` implies

\[
\frac{\delta_G}{\epsilon_G}
=\frac1{\sqrt{\epsilon_G L}}\to0,
\qquad
\frac{\delta_G^{-1}}L
=\frac1{\sqrt{\epsilon_G L}}\to0.
\tag{24}
\]

Together with `(6)`--`(7)`, this gives uniformly

\[
P_{\delta_G,t_G}(\rho)
+
P_{\delta_G,t_G}(\widetilde\rho)
=
\frac{1+o(1)}{\epsilon_G(1-\epsilon_G)}.
\tag{25}
\]

The Euler-side cost is `o(L)`, so `(23)` becomes `(13)`. The lower method floor and explicit one-point construction match.

### 3. The self-dual line has only one zero occurrence to charge

At `beta=1/2`, reflection fixes the zero:

\[
1-\overline{\left(\frac12+i\gamma\right)}
=
\frac12+i\gamma.
\tag{26}
\]

The zero sum `(20)` counts that zero with its actual multiplicity once. Writing a second reflected kernel for the same occurrence would therefore double-count it.

More generally, for every zero in the symmetric line-centered cell `(14)`, regardless of whether it lies exactly on the line or is one member of a distinct off-line pair,

\[
P_{\delta,v}(\rho)
\le
\frac1{1+\delta-\beta}
\le
\frac1{\frac12-h_G}
=2+o(1).
\tag{27}
\]

Because `d_G^0` counts every zero in the cell once, no reflection bonus is needed or available in the per-zero accounting. Integrating `(27)` yields `(15)`. Retaining the `d_G^0` packet occurrences in `(3)` gives

\[
d_G^0 q_G^0(\mu_G)
\le
\frac12 L W_G
+
\int\delta^{-1}\,d\mu_G
+O(W_G),
\tag{28}
\]

and the ceiling `(15)` forces the method floor `(16)`.

For `(17)`, one has `delta_G=o(1)`, `delta_G^{-1}=o(L)`, and `(14)` implies uniformly

\[
P_{\delta_G,t_G}(\rho)=2+o(1).
\tag{29}
\]

Thus `(28)` yields `(18)`. Again the universal positive-sampler floor is attained by one sample.

### 4. Why the factor-two jump is structural

Suppose first that a right-half packet remains separated from the line. Its count `d_G` records only the right member of each reflection orbit, while positivity allows `(23)` to spend the mass of both the right zero and the distinct left partner against that one counted object. At fixed `epsilon`, the limiting pair charge is

\[
K_{\mathrm{pair}}(\epsilon)
=
\frac1\epsilon+
\frac1{1-\epsilon}
=
\frac1{\epsilon(1-\epsilon)}.
\tag{30}
\]

As `epsilon` tends to `1/2`, this tends to `4`, leading to the formal coefficient `(1/2)/4=1/8`.

At the critical line, however, the reflection orbit can have size one. A self-dual zero contributes only

\[
K_{\mathrm{line}}
=
\frac1{1/2}=2,
\tag{31}
\]

so the coefficient is `(1/2)/2=1/4`. For an off-line pair lying inside the symmetric line-centered cell, both orbit members are already included in `d_G^0`; their total limiting charge is `4` for two counted zeros, again `2` per counted occurrence. Thus `(31)` is not an artifact of assuming that all zeros in the cell lie exactly on the critical line.

This is an orbit-counting discontinuity, not a discontinuity of the Poisson kernel itself. The kernel varies continuously as the horizontal coordinate approaches `1/2`; what changes is whether reflection supplies a **distinct zero outside the counted packet** whose positive mass can be charged without increasing the count.

### 5. Reproducible verification

The correction can be checked without numerical computation. For an exactly aligned off-line pair centered at `beta=1-epsilon`, the limiting charge as `delta -> 0` is

\[
K_{\mathrm{pair}}(\delta;\epsilon)
=
\frac1{\delta+\epsilon}
+
\frac1{\delta+1-\epsilon}
\longrightarrow
\frac1{\epsilon(1-\epsilon)}.
\tag{32}
\]

At the self-dual line, with the zero counted once,

\[
K_{\mathrm{line}}(\delta)
=
\frac1{\delta+1/2}
\longrightarrow2.
\tag{33}
\]

Multiplying the common leading budget `(1/2)L` by the reciprocal charges gives

\[
\frac12\epsilon(1-\epsilon)L
\quad\text{off the line},
\qquad
\frac14L
\quad\text{on a line-centered symmetric packet}.
\tag{34}
\]

Finally,

\[
\lim_{\epsilon\uparrow1/2}
\frac12\epsilon(1-\epsilon)
=
\frac18
\ne
\frac14.
\tag{35}
\]

Equation `(35)` is precisely the factor-two endpoint error in the withdrawn `NB-145`: it continued the two-element reflection-orbit charge into the fixed-point regime.

### 6. Representation applicability audit

No projected-versus-orthogonal norm identification occurs here. The argument is a scalar inequality for the actual zeta zero divisor obtained directly from the logarithmic derivative and a positive sampling measure. There is no finite-section Gram matrix, quotient norm, compressed operator, state-space coordinate map, or replacement of a projected target quantity by an ambient one. The representation-specific failure modes covered by `mathia-research-representation` are therefore not applicable to this derivation.

## Scope and relation to earlier findings

`NB-144` already states its fixed-interior theorem for `0<epsilon<1/2`; that theorem is unaffected. The separated regime above strengthens only the **method-optimality** interpretation: arbitrary positive multi-point exterior sampling cannot improve the coefficient as long as the packet remains strictly on one side of the critical line and the prime side is bounded only by `(4)`.

The `1/8` appearing in `NB-111` has a different meaning. There it is a Laguerre target-poorness threshold for the rank of a one-zero derivative-state packet. The present correction neither weakens nor contradicts that theorem. It says only that the positive exterior Poisson occupancy certificate has a `1/4` leading floor for a line-centered symmetric zero packet; no claim is made that `1/8` is impossible in other Nyman geometries.

`NB-112` already exhibits the same reflection-orbit boundary in a different calculation: an off-critical zero and its reflected partner are distinct and spend multiplicity twice in a zero-counting jump, while on `beta=1/2` the reflected zero is the original zero and that factor two disappears. The present finding applies the same bookkeeping principle to the exterior Poisson mass budget.

The line-centered theorem should not be extrapolated to arbitrary asymmetric cells that cross the critical line. Such cells require explicit accounting of which reflection partners are already counted and which lie outside. The invariant quantity is the reflection-orbit bookkeeping, not merely the center coordinate.

## References

- `NB-111`, *Laguerre tail coercion opens an explicit one-eighth logarithmic window*: independent target-space `1/8` threshold; not the Poisson coefficient studied here.
- `NB-112`, *zero-counting symmetry eliminates the one-zero multiplicity rescue*: same-ordinate reflection symmetry is distinct off the critical line and self-dual on it.
- `NB-144`, *Euler-product Poisson mass forces logarithmic confluence away from the one-line*: source of the positive zero budget, Euler-product majorant, and sharp one-point coefficient for strict right-half packets.
- `INT-RIEMANN-EXPLICIT`: internal anchor for the classical logarithmic-derivative/Hadamard explicit-formula identity and functional-equation zero symmetry used above.

No new external literature dependency is load-bearing in this correction.

## Open problem mapping

The positive exterior Poisson cone is now quantitatively exhausted in the two clean orbit regimes. For a separated right-half packet its sharp coefficient is `epsilon(1-epsilon)/2`; for a symmetric line-centered packet it is `1/4`. Adding more exterior points, continuous positive averaging, or adaptive positive weights cannot by itself turn either fixed-interior `Theta(log G)` certificate into the `o(log G)` occupancy law needed by the logarithmic-confluence branch.

Any improvement must therefore spend information absent from `(3)`--`(4)`: signed or oscillatory combinations that forfeit zero-side positivity, cancellation or correlations in the von Mangoldt Dirichlet series beyond its absolute majorant, genuinely local zero-correlation input, or a target-aware Nyman argument proving that the surviving logarithmic packets are necessarily target-bearing. The critical-line boundary must be handled with orbit-aware counting in any such continuation.