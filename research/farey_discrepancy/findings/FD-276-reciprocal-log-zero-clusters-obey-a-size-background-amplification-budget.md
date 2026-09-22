# FD-276 — Reciprocal-log zero clusters obey a size-background amplification budget

- **Date:** 2026-09-22
- **Status:** proved uniform growing-cluster band bound; threshold consequence conditional on RH and simple zeros
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** zeta-zero clusters / growing divided differences / Cauchy control / divisor-replicated repair / background conditioning
- **Depends on:** FD-261, FD-274, FD-275
- **Classification:** `EXACT-DERIVED + RH-CONDITIONAL + GROWING-CLUSTER-CAUCHY-LEDGER + SIZE-BACKGROUND-TARIFF`

## Claim

FD-275 proves that every fixed-size simple critical-zero cluster has only linear divisor-band cost before the desingularized background `H_C^(-1)` is charged. Its remaining explicit loophole is that the cluster size may grow, because the Hermite--Genocchi derivative order then grows and the fixed-`m` constants in FD-275 no longer give a uniform statement.

That loophole can be quantified without any hidden `m`-dependent constant by combining FD-274's exact divided-difference compression with a Cauchy estimate on a reciprocal-logarithmic zero-free collar.

Keep the normalized packet amplitude

\[
A_{N,d}(s)
=
N^{s-1/2}\frac{K_s(d)}s
=
N^{s-1/2}
\sum_{q\mid d}
\int_{q-1}^{q}t^{s-1}\,dt
\tag{1}
\]

from FD-275. Let `x>=2`, `N>=1`, set

\[
L:=\log(2Nx),
\qquad
\eta:=L^{-1},
\tag{2}
\]

and assume `L` is large enough that `eta<=1/4`.

Let

\[
\mathcal C=\{\rho_1,\ldots,\rho_m\}
\]

be a consecutive cluster of distinct simple critical-line zeros and let `I_C` be the vertical segment joining its extreme nodes. Assume RH and that every nontrivial zero outside `C` has Euclidean distance at least `2 eta` from `I_C`. Writing

\[
\zeta(s)=P_{\mathcal C}(s)H_{\mathcal C}(s),
\qquad
P_{\mathcal C}(s)=\prod_{\rho\in\mathcal C}(s-\rho),
\]

define the reciprocal background envelope on the `eta`-collar

\[
\mathfrak B_{\mathcal C}(\eta)
:=
\sup_{\operatorname{dist}(s,I_{\mathcal C})\le\eta}
|H_{\mathcal C}(s)|^{-1}.
\tag{3}
\]

Then the grouped complex repair packet of FD-274 satisfies the **uniform-in-cluster-size** band bound

\[
\boxed{
\sum_{x<d\le2x}|Q_{\mathcal C}(N,d)|
\ll
x\,(2L)^{m-1}\,
\mathfrak B_{\mathcal C}(\eta).
}
\tag{4}
\]

The implied constant is absolute once `eta<=1/4`; in particular it does not depend on `m`, on the cluster height, or on its internal gaps. The corresponding real packet changes only the harmless factor coming from `2 Re`.

Consequently, in the polynomial-depth regime

\[
x=N^{\lambda+o(1)},
\qquad \lambda>0,
\tag{5}
\]

one has `log(2L)=log log x+O(1)`. If a complete reciprocal-log cluster by itself contributes at the FD-261 positive-capacity threshold

\[
\sum_{x<d\le2x}|Q_{\mathcal C}(N,d)|
\ge
x^{2-\beta-o(1)},
\qquad
\beta=\log_2\frac32,
\tag{6}
\]

then necessarily

\[
\boxed{
(m-1)\log(2L)
+
\log \mathfrak B_{\mathcal C}(\eta)
\ge
(1-\beta-o(1))\log x.
}
\tag{7}
\]

Thus cluster cardinality and external/background conditioning obey a single additive exponent budget. Two useful corollaries are:

\[
\mathfrak B_{\mathcal C}(\eta)=x^{o(1)}
\quad\Longrightarrow\quad
\boxed{
m
\ge
(1-\beta-o(1))
\frac{\log x}{\log\log x},
}
\tag{8}
\]

and

\[
m=o\!\left(\frac{\log x}{\log\log x}\right)
\quad\Longrightarrow\quad
\boxed{
\mathfrak B_{\mathcal C}(\eta)
\ge
x^{1-\beta-o(1)}.
}
\tag{9}
\]

Numerically,

\[
1-\beta
=0.4150374992\ldots .
\tag{10}
\]

More generally, if

\[
m=
(\kappa+o(1))
\frac{\log x}{\log\log x},
\qquad
\mathfrak B_{\mathcal C}(\eta)=x^{b+o(1)},
\]

then a threshold-sized single-cluster contribution requires

\[
\boxed{
\kappa+b\ge1-\beta.
}
\tag{11}
\]

So FD-275's bounded-cluster tariff extends to a growing-cluster trichotomy: a reciprocal-log cluster cannot reach the required `x^(2-beta)` scale unless it has near-`log x/log log x` cardinality, polynomial external/background conditioning, or both resources sharing the budget (11).

## Evidence

The first ingredient is a collar version of FD-275's integral band ledger. If

\[
U_\eta(\mathcal C)
:=
\{s:\operatorname{dist}(s,I_{\mathcal C})\le\eta\},
\]

then every `s=sigma+it` in this collar satisfies

\[
\frac12-\eta\le\sigma\le\frac12+\eta.
\]

From (1),

\[
|A_{N,d}(s)|
\le
N^\eta
\sum_{q\mid d}
\int_{q-1}^{q}t^{\sigma-1}\,dt.
\tag{12}
\]

For `q=1`, uniformly in `sigma>=1/2-eta`,

\[
\int_0^1 t^{\sigma-1}\,dt
=\frac1\sigma
\ll1.
\tag{13}
\]

For `q>=2`, since `t>=1`,

\[
\int_{q-1}^{q}t^{\sigma-1}\,dt
\ll q^{-1/2+\eta}.
\tag{14}
\]

Summing over `x<d<=2x` and counting multiples gives

\[
\begin{aligned}
\sum_{x<d\le2x}
\sup_{s\in U_\eta(\mathcal C)}|A_{N,d}(s)|
&\ll
N^\eta
\left[
 x
+
\sum_{q\le2x}
\left(\frac{x}{q}+1\right)q^{-1/2+\eta}
\right]\\
&\ll
N^\eta x,
\end{aligned}
\tag{15}
\]

because `eta<=1/4` makes `sum q^(-3/2+eta)` convergent uniformly and the secondary sum is `O(x^(1/2+eta))=O(x^(3/4))`. With the specific choice `eta=1/L`,

\[
N^\eta
=
\exp\!\left(\frac{\log N}{\log(2Nx)}\right)
\le e,
\tag{16}
\]

so the collar band cost remains `O(x)`.

The second ingredient removes the growing derivative-order constants. FD-274 gives exactly

\[
Q_{\mathcal C}(N,d)
=
[\rho_1,\ldots,\rho_m]
\left(\frac{A_{N,d}}{H_{\mathcal C}}\right).
\tag{17}
\]

Put

\[
f_d(s)=A_{N,d}(s)H_{\mathcal C}(s)^{-1}.
\]

Because the cluster is externally separated by at least `2 eta`, RH implies that `H_C` has no zero in `U_eta(C)`. The function `f_d` is therefore holomorphic there. Hermite--Genocchi gives

\[
|Q_{\mathcal C}(N,d)|
\le
\frac1{(m-1)!}
\sup_{s\in I_{\mathcal C}}
|f_d^{(m-1)}(s)|.
\tag{18}
\]

For every point of `I_C`, the disk of radius `eta/2` lies inside `U_eta(C)`. Cauchy's derivative estimate therefore gives

\[
\frac{|f_d^{(m-1)}(s)|}{(m-1)!}
\le
\left(\frac2\eta\right)^{m-1}
\sup_{w\in U_\eta(\mathcal C)}|f_d(w)|.
\tag{19}
\]

Combining (18)--(19), summing in `d`, and using (3) and (15) yields

\[
\begin{aligned}
\sum_{x<d\le2x}|Q_{\mathcal C}(N,d)|
&\le
\left(\frac2\eta\right)^{m-1}
\mathfrak B_{\mathcal C}(\eta)
\sum_{x<d\le2x}
\sup_{w\in U_\eta(\mathcal C)}|A_{N,d}(w)|\\
&\ll
xN^\eta
\left(\frac2\eta\right)^{m-1}
\mathfrak B_{\mathcal C}(\eta).
\end{aligned}
\tag{20}
\]

Using (2) and (16) proves (4). The factorial in Hermite--Genocchi is cancelled exactly by the factorial in Cauchy's derivative estimate, so there is no untracked `m!` or `C_m` term.

Taking logarithms in (4) under the threshold assumption (6) proves (7). Under (5),

\[
L\asymp\log x,
\qquad
\log(2L)=\log\log x+O(1),
\tag{21}
\]

which gives (8)--(11).

## Reciprocal-log cluster partition

The external-separation hypothesis is natural rather than an extra rare event. Under RH and simplicity, fix `eta` as in (2) and join two consecutive critical zeros whenever their ordinate gap is less than `2 eta`. Every maximal connected component is a consecutive reciprocal-log cluster whose two exterior gaps, when they exist, are at least `2 eta`. For every component fully contained in the finite zero packet, the collar hypothesis used above is automatic after its own zeros are divided out of `zeta`.

Thus an arbitrarily tiny internal gap does not create a new case. It merely joins two nodes into the same cluster. The only ways for a complete component to make (4) large are its cardinality `m` and the collar background envelope `mathfrak B_C(eta)`.

This clustering scale is also the same local order `1/log T` that appears in the separated-zero literature used by FD-273, up to constants when zero height and divisor depth are polynomially related. The present result does not import a zero-spacing theorem from that literature; it uses the reciprocal-log scale only as the analytic collar at which Cauchy control becomes power-neutral in `N`.

## Stress tests

The first stress test is a very tight but growing cluster with flat background. Set formally `H_C=1` and allow all internal spacings to tend to zero while keeping the cluster externally isolated. Equation (4) depends on none of those internal spacings. If `m=o(log x/log log x)`, the entire cluster remains at `x^(1+o(1))` band scale. Coalescing many simple nodes therefore does not evade FD-274 through the raw barycentric denominators.

The second stress test is large cluster size. The previous FD-275 estimate had an implicit fixed-`m` constant and so could not distinguish genuine growth from an artifact of repeated Leibniz differentiation. Equation (20) tracks the order exactly: the only growth charged to the analytic interpolation step is `(2/eta)^(m-1)`. At `eta=1/log(2Nx)`, this becomes `(2 log(2Nx))^(m-1)`, which is still subpolynomial precisely when `m=o(log x/log log x)` in the polynomial-depth regime.

The third stress test is the collar width. Choosing a much smaller collar would artificially increase the Cauchy factor and weaken the conclusion. Choosing `eta=1/log(2Nx)` is the largest universally useful scale for this argument that keeps the horizontal packet factor `N^eta` bounded by an absolute constant. Any improvement using a wider collar would only strengthen (4); a narrower externally forced collar is absorbed by enlarging the cluster until a reciprocal-log exterior gap is reached.

The fourth stress test is an adversarial background. Nothing in complex analysis prevents `H_C` from being extremely small on a zero-free collar. In that case `mathfrak B_C(eta)` is genuinely large and (4) records that resource rather than hiding it in a derivative constant. Hence the finding does not claim that growing close-zero clusters are harmless. It gives an exact exponent ledger for what they must spend.

## Prior-art check

Hermite--Genocchi, Cauchy's derivative estimate, and the analyticity of divided differences in their nodes are classical complex/interpolation theory and are not claimed as new. The relation between close zeta zeros and small values of `zeta'(rho)` is likewise classical and is already part of the literature boundary recorded around FD-273--FD-275.

A targeted search was run for zeta-zero clusters, reciprocal derivative residues, divided differences, Cauchy estimates on close-zero neighborhoods, and current close-gap density results. It found the established close-zero/derivative literature and standard complex-analytic interpolation machinery, but no result applying a reciprocal-log zero-free collar to the exact FD-271 consecutive-difference/divisor-replication packet, nor a size-versus-background exponent budget equivalent to (7)--(11).

The substantive content is therefore the repository-specific growing-cluster transfer: FD-274 compresses the signed residues to one divided difference, the FD-275 integral representation stays linear on a complex collar, and Cauchy removes all hidden derivative-order constants. No external theorem is load-bearing for (4)--(11), so this finding adds no new `SOURCES.md` dependency.

## Implications

FD-273 forces nonexceptional threshold-scale finite-packet coherence toward the close-zero complement. FD-274 removes internal inverse-gap singularities, and FD-275 shows that every bounded cluster must pay a polynomial background-conditioning tariff. FD-276 now closes the explicit **growing but sub-`log x/log log x` cluster-size loophole**: such a cluster still has only `x^(1+o(1))` packet-side band amplification unless its desingularized background is polynomially ill-conditioned.

The surviving spectral route is therefore sharper. At reciprocal-log resolution, a threshold cluster must spend a total exponent `1-beta=0.415037...` between two resources: cluster cardinality at scale `log x/log log x`, and the zero-free-collar inverse background `mathfrak B_C`. This replaces an unquantified high-derivative escape by the directly testable ledger (7).

A useful next question is now aggregate rather than single-cluster: can many reciprocal-log components, each individually below the budget, add coherently on the source-selected integer horizons? The FD-270--FD-273 phase-cancellation machinery suggests that this should require another coherence resource, but (4) by itself does not sum different clusters with their phases retained.

## Limitations

The result assumes RH to turn a reciprocal-log exterior gap on the critical line into a genuinely zero-free complex collar. Without RH, off-line zeros could create poles of `H_C^(-1)` inside that collar. The nodal divided-difference identity of FD-274 remains unconditional, but the collar estimate does not.

Zeros are assumed distinct and simple. A multiple zero produces a higher-order pole in `1/zeta` and requires confluent residue/Hermite analysis. This remains a separate escape exactly as in FD-274--FD-275.

The bound is for a complete cluster whose reciprocal-log collar is contained in the finite packet's zero bookkeeping. If the truncation height cuts through a reciprocal-log component, the resulting boundary fragment must be treated together with the omitted neighboring zeros or absorbed into the explicit-formula remainder. The claim does not hide that truncation-edge term.

Most importantly, no upper bound on `mathfrak B_C(eta)` for the actual zeta function is proved. A zero-free function can still be very small. Equation (7) is a necessary resource budget, not a proof that the remaining background resource is absent. Nor does a collection of many individually subthreshold clusters automatically remain subthreshold after their signed contributions are summed.

## Decisive audit

For any proposed close-zero mechanism with growing cluster size, first partition the simple critical zeros at reciprocal-log scale and factor each complete component from `zeta`. For a component of size `m`, measure `mathfrak B_C(eta)` on the `eta=1/log(2Nx)` collar. If

\[
(m-1)\log(2\log(2Nx))
+
\log\mathfrak B_C(eta)
<
(1-\beta-o(1))\log x,
\]

then that component cannot supply the FD-261 threshold by itself.

Conversely, a genuine single-cluster escape must exhibit quantitatively either roughly `0.415 log x/log log x` reciprocal-log-connected zeros, a polynomially large desingularized inverse background, or a combination satisfying (11). Internal gap size, zero height, and untracked high derivative constants no longer constitute independent amplification resources in this ledger.