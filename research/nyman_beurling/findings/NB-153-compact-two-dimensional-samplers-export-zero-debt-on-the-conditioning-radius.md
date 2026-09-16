# NB-153 — Compact two-dimensional samplers export zero debt on the conditioning radius

**Status:** `LITERATURE+DERIVED + SOURCE-SPECIFIC + SIGNED-POISSON + XI-CONSERVATION + TWO-DIMENSIONAL-SAMPLER + CONDITIONING-TRADEOFF + NB-152-FRONTIER`.

`NB-152` closes the uniformly conditioned fixed-horizontal many-point route, but it deliberately leaves two apparent escape parameters open: the sampler may use bounded vertical offsets as well as horizontal ones, or it may let its scale-invariant conditioning deteriorate with height. Both possibilities can be quantified without changing the underlying completed-function conservation law.

A bounded two-dimensional cloud of exterior sample points gives no new escape. More precisely, zero total mass on any fixed compact set of complex offsets still cancels the common Hadamard/digamma background, while compactness preserves quadratic ordinate decay. If the condition number

\[
C_G:=\frac{\|\mu_G\|_{\rm TV}}{q_G}
\]

is allowed to grow but remains `o(log G)`, then a logarithmic target packet still forces `Omega(q_G log G)` negative charge on actual zeta zeros. The only change is quantitative: the debt can move out to ordinate radius `O(C_G)`, and the forced adverse population can fall from `Omega(log G)` to `Omega(log G/C_G)`. Thus bounded vertical geometry is harmless, and ill-conditioning below logarithmic order can only trade population for displacement; it cannot erase the signed-zero debt.

Fix a compact set

\[
K\subset\{w\in\mathbf C:\Re w>0\},
\tag{1}
\]

and write

\[
a_-:=\inf_{w\in K}\Re w>0,
\qquad
a_+:=\sup_{w\in K}\Re w,
\qquad
B:=\sup_{w\in K}|\Im w|<\infty.
\tag{2}
\]

For arbitrarily large `G`, let `mu_G` be a finite real signed Borel measure supported on `K` with

\[
\mu_G(K)=0,
\qquad
V_G:=\|\mu_G\|_{\rm TV}.
\tag{3}
\]

The sampler evaluates the completed logarithmic derivative on the translated two-dimensional cloud

\[
s_w(G)=1+w+iG,
\qquad w\in K.
\tag{4}
\]

For a nontrivial zero `rho=beta+i gamma`, counted with multiplicity, define

\[
Q_G(\rho)
:=
\Re\int_K\frac{d\mu_G(w)}{1+w+iG-\rho}.
\tag{5}
\]

Suppose there is a packet `F_G` of positive-ordinate zeros satisfying

\[
d_G:=|F_G|\ge\kappa\log G
\tag{6}
\]

for a fixed `kappa>0`, and suppose the sampler charges every target zero positively with

\[
q_G:=\inf_{\rho\in F_G}Q_G(\rho)>0.
\tag{7}
\]

Set

\[
C_G:=\frac{V_G}{q_G}.
\tag{8}
\]

Then the following statements hold.

First, the signed zero sum is absolutely convergent and obeys the uniform conservation law

\[
\boxed{
\sum_\rho Q_G(\rho)=O_K(V_G).
}
\tag{9}
\]

Second, if

\[
A_G^-:=
\sum_{\substack{\rho\notin F_G\\\gamma>0}}
(Q_G(\rho))_-,
\tag{10}
\]

then

\[
\boxed{
A_G^-
\ge
q_G\bigl(\kappa\log G-O_K(C_G)\bigr).
}
\tag{11}
\]

Hence every family with

\[
C_G=o(\log G)
\tag{12}
\]

satisfies

\[
A_G^-\ge(\kappa-o(1))q_G\log G.
\tag{13}
\]

Finally there is a constant `M=M(K,kappa)` such that, whenever `(12)` holds, the radius

\[
R_G:=M C_G
\tag{14}
\]

captures a fixed fraction of the adverse debt:

\[
\boxed{
\sum_{\substack{\rho\notin F_G\\\gamma>0\\|\gamma-G|\le R_G}}
(Q_G(\rho))_-
\gg_{K,\kappa}
q_G\log G.
}
\tag{15}
\]

Moreover the window in `(15)` contains at least

\[
\boxed{
\Omega_{K,\kappa}\!\left(\frac{\log G}{C_G}\right)
}
\tag{16}
\]

adverse zeros, counted with multiplicity. Since `C_G>=a_-`, the radius in `(14)` is always large enough, after increasing `M`, to dominate the fixed vertical diameter of `K`.

## 1. Zero mass on a compact complex cloud still gives absolute discrete conservation

Choose one reference point `w_0 in K`. Because `mu_G(K)=0`,

\[
\int_K\frac{d\mu_G(w)}{1+w+iG-\rho}
=
\int_K
\left(
\frac1{1+w+iG-\rho}
-
\frac1{1+w_0+iG-\rho}
\right)d\mu_G(w).
\tag{17}
\]

Writing `y=G-gamma`, the difference equals

\[
\frac{w_0-w}
{(1+w+iG-\rho)(1+w_0+iG-\rho)}.
\tag{18}
\]

The real parts of both denominator factors are at least `a_-`. Their imaginary parts are `y+Im w` and `y+Im w_0`, with both offsets bounded by `B`. Compactness therefore gives a constant `D_K` such that

\[
\left|
\int_K\frac{d\mu_G(w)}{1+w+iG-\rho}
\right|
\le
D_K\frac{V_G}{1+(G-\gamma)^2}.
\tag{19}
\]

The classical unit-interval zero count `N(t+1)-N(t)\ll\log(t+2)` makes the right side summable over the full nontrivial zero divisor. Thus the zero sum may be integrated termwise in the genus-one Hadamard expansion of `xi'/xi`, and both its constant term and every `1/rho` regularizer vanish against the zero total mass. Consequently

\[
\sum_\rho Q_G(\rho)
=
\Re\int_K
\frac{\xi'}{\xi}(1+w+iG)
\,d\mu_G(w).
\tag{20}
\]

Uniformly for `w in K`,

\[
\frac{\xi'}{\xi}(s)
=
\frac1s+
\frac1{s-1}
-
\frac12\log\pi
+
\frac12\psi(s/2)
+
\frac{\zeta'}{\zeta}(s).
\tag{21}
\]

Here `Re s>=1+a_->1`, so the Euler series for `zeta'/zeta` is absolutely convergent and uniformly bounded on the whole translated cloud. The rational terms are `O_K(1/G)`. Stirling gives, uniformly for `w in K`,

\[
\psi((1+w+iG)/2)
=
\log(iG/2)+O_K(1/G).
\tag{22}
\]

The common logarithm and constant term cancel against `(3)`, leaving `(9)`. The argument uses no one-dimensional ordering of the support: bounded vertical offsets enter only through compactness.

## 2. A logarithmic target packet creates actual negative zero debt until conditioning reaches logarithmic size

The target contribution is at least

\[
\sum_{\rho\in F_G}Q_G(\rho)
\ge q_Gd_G
\ge\kappa q_G\log G.
\tag{23}
\]

Zeros with negative ordinate are too far from the translated cloud to absorb a logarithmic target contribution. Indeed, for `w=a+iv`,

\[
\Re\frac1{1+w+iG-\rho}
=
\frac{a+1-\beta}
{(a+1-\beta)^2+(G+v-\gamma)^2},
\tag{24}
\]

so compactness of `K` and shell counting give

\[
\sum_{\gamma<0}|Q_G(\rho)|
\ll_K
V_G\frac{\log G}{G}
=o(V_G).
\tag{25}
\]

Splitting the remaining positive-ordinate zeros outside `F_G` into their positive and negative charges, equations `(9)`, `(23)` and `(25)` yield

\[
A_G^-
\ge
q_Gd_G-O_K(V_G).
\tag{26}
\]

Substituting `V_G=q_GC_G` proves `(11)`. In particular, `(12)` makes the conservation error lower order relative to the target packet and gives `(13)`.

This identifies a genuine scale threshold for this representation. Bounded conditioning is not essential to the sign-debt mechanism; what is essential is only that coefficient variation remain sublogarithmic relative to useful target charge. A condition number of order `log G` is the first scale at which the `O(V_G)` completed-function remainder can itself be as large as the `q_G log G` target contribution.

## 3. Conditioning buys displacement linearly and adverse population inversely

For `|G-gamma|` larger than a fixed multiple of `B+1`, equation `(24)` gives

\[
|Q_G(\rho)|
\ll_K
\frac{V_G}{(G-\gamma)^2}.
\tag{27}
\]

Hence, uniformly for `R` above that fixed threshold and `R=o(G)`, Riemann--von Mangoldt shell counting gives

\[
\sum_{\substack{\gamma>0\\|\gamma-G|\ge R}}
|Q_G(\rho)|
\ll_K
V_G
\left(
\frac{\log G}{R}
+
\frac{\log G}{G}
\right).
\tag{28}
\]

There is also the pointwise bound

\[
|Q_G(\rho)|
\le
\int_K\frac{d|\mu_G|(w)}{\Re w+1-\beta}
\le
\frac{V_G}{a_-}.
\tag{29}
\]

Equation `(29)` applied to a target zero shows `q_G<=V_G/a_-`, hence

\[
C_G\ge a_-.
\tag{30}
\]

Take `R=M C_G`. Because of `(30)`, `M` can be chosen from `K` and `kappa` alone so that `R` is above the fixed threshold in `(28)`. Under `(12)`, one also has `R=o(G)`. Using `V_G=q_GC_G`, the main tail term becomes

\[
\ll_K
q_GC_G\frac{\log G}{MC_G}
=
O_K(M^{-1}q_G\log G).
\tag{31}
\]

Choosing `M` sufficiently large and combining `(13)` with `(31)` proves `(15)`. Finally `(29)` says that each adverse zero can carry at most `q_GC_G/a_-`; dividing the mass in `(15)` by this pointwise maximum proves `(16)`.

Thus the two costs are explicit. To move a fixed fraction of the adverse charge out to distance much larger than `C_G`, the sampler must increase its condition number by the same order. To reduce the forced adverse population to `O(1)` while keeping the support in the same fixed compact set, `(16)` requires

\[
C_G=\Omega(\log G).
\tag{32}
\]

The bounded-conditioning theorem `NB-152` is the endpoint `C_G=O(1)`: it recovers a bounded radius and an `Omega(log G)` adverse population.

## 4. What the two-dimensional extension does and does not close

The conclusion is representation-specific. It is a theorem about zero-mass exterior Cauchy/Poisson samplers whose entire support is a fixed compact translate of the sampling height and remains a positive distance to the right of `Re s=1`. It is not an intrinsic zero-spacing theorem and does not assert that arbitrary linear functionals of the zero divisor have the same localization behavior.

Within that representation, however, allowing vertical offsets of bounded size changes nothing essential. Three-point, many-point, continuous, nonuniform and genuinely two-dimensional sample clouds all obey the same conservation identity. Nor does mildly deteriorating coefficient conditioning provide an escape: every `C_G=o(log G)` family still creates logarithmic adverse charge, at radius `O(C_G)`, on at least `Omega(log G/C_G)` actual zeros.

The surviving regimes are therefore sharper than after `NB-152`. A fixed compact exterior sampler must spend at least logarithmic conditioning if it wants the completed-function remainder to be capable of absorbing the packet without a forced large adverse population. Alternatively it must leave the fixed-compact geometry: move horizontally toward `Re s=1`, let horizontal or vertical support grow with `G`, or change the source-side argument so that signed Euler/Nyman information is retained instead of estimating the completed sampler only by its total variation.

The theorem does not claim that `C_G=Omega(log G)` is sufficient for isolation; it is only the first conditioning scale not ruled out by this conservation argument. Likewise growing vertical support is not certified as useful; it is merely outside the compactness hypothesis needed for the uniform quadratic tail bound.

## Prior-art search

Bruna and Melnikov, *On translates of the Poisson kernel and zeros of harmonic functions*, Bull. London Math. Soc. 39 (2007), 317--326, classify completeness/uniqueness phenomena for Poisson-kernel translates. Chirre and Molero, *Explicit conditional bounds for zeta(s) at the edge of the critical strip*, Port. Math. (published online 19 June 2026), use Guinand--Weil together with extremal majorants and minorants for the Poisson kernel to bound logarithmic derivatives under RH. Classical differenced-logarithmic-derivative arguments also provide the background already recorded in `NB-151`--`NB-152`.

Those sources delimit the generic Poisson/logarithmic-derivative landscape but do not supply the target-conditioned statement above: a zero-mass, compact two-dimensional translated sampler with condition number `C_G` forces actual adverse zeta-zero charge at radius `O(C_G)` and population `Omega(log G/C_G)` throughout the sublogarithmic-conditioning regime. The proof is the direct completed-function calculation `(17)`--`(31)`, so no new external result is load-bearing and no `SOURCES.md` update is required.

## Source map

- `NB-148`: zero-mass sampling cancels the Hadamard logarithm but exports a signed Poisson debt.
- `NB-149`: Jordan/total-variation domination loses the signed advantage and restores the positive logarithmic budget.
- `NB-150`: mesoscopic two-point samplers have both lobes occupied at logarithmic scale by ordinary zero density.
- `NB-151`: fixed two-point horizontal differencing forces a bounded-neighbor adverse packet.
- `NB-152`: arbitrary fixed-horizontal measure-valued samplers with bounded conditioning force the same bounded-neighbor logarithmic adverse population.
- Riemann--von Mangoldt/unit-interval zero counting and the completed `xi` logarithmic derivative are already anchored in the line and remain the only load-bearing classical inputs.

## Consequence for the line

The bounded-vertical-offset loophole left by `NB-152` is closed, and the ill-conditioning loophole now has a quantitative threshold. **A fixed compact exterior sample cloud with `C_G=o(log G)` cannot isolate a logarithmic target packet: it must export `Omega(q_G log G)` adverse charge to radius `O(C_G)` and at least `Omega(log G/C_G)` actual zeros.**

The next signed-sampling question should therefore not add more points inside a bounded two-dimensional cloud. It must test one of the genuinely different currencies left by the theorem: logarithmic-or-worse conditioning together with useful prime-side cancellation, support that moves toward the `Re s=1` boundary, support diameter growing with height, or an explicitly target-aware Nyman coupling that preserves sign rather than collapsing the sampler to a zero-side certificate.