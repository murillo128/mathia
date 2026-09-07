# XF-086 — guarded selector energy automatically enters the exact equal-weight cone

**Status:** `EXACT-DERIVED` + `STRUCTURAL/BRIDGE` + `GUARDED-H3-TO-L1` + `STATIC-EQUAL-WEIGHT-GATE-CLOSED`. XF-084 turns the real-divisor source bridge into a finite trigonometric moment problem, and XF-085 proves exact equal-weight `N`-node realization whenever the prescribed visible moments lie in a fixed Gershgorin interior cone

\[
2\sum_{m\in S}|Q_m|\le (1-\kappa)N.
\tag{1}
\]

That left a new-looking source obligation: prove an unweighted `ell^1` bound for the transported moment vector. In the guarded Xi architecture this obligation is actually automatic. The exact XF-070/XF-079 selector norm already weights mode `m` by `m^4/M^2`, while XF-071 deliberately starts the transported visible block at a growing index `J`. Duality between this weighted `ell^2` norm and `ell^1` gives an explicit gain `J^{-3/2}`. Consequently **every moment vector with bounded guarded selector resource lies arbitrarily deep inside the XF-085 fixed-margin cone as `J -> infinity`**.

More precisely, let `M=q^2`, `N=2M`, let the fixed selector window satisfy

\[
\chi=\widehat g\in C_c^\infty((-1,1)),
\qquad
C_g:=\int_{-1}^{1}|\chi(u)|^2\,du>0,
\tag{2}
\]

and let `S` be any subset of `{J,...,K}`. Define the exact full-sideband resource of a prescribed raw moment vector `Q=(Q_m)_{m\in S}` by

\[
\boxed{
\mathcal R_S(Q)
:=
\frac1{4M^2}
\sum_{m\in S}|Q_m|^2 I_m,
\qquad
I_m:=\int_{-1}^{1}(\pi m+u)^4|\chi(u)|^2\,du.
}
\tag{3}
\]

Then for every integer `J>=1`,

\[
\boxed{
\frac2N\sum_{m\in S}|Q_m|
\le
\frac{4}{\sqrt{3C_g}(\pi-1)^2}
\,J^{-3/2}\,\mathcal R_S(Q)^{1/2}.
}
\tag{4}
\]

Hence the quantitative criterion

\[
\boxed{
\mathcal R_S(Q)=o(J^3)
\quad\Longrightarrow\quad
\frac2N\sum_{m\in S}|Q_m|=o(1).
}
\tag{5}
\]

In particular, `\mathcal R_S(Q)=O(1)` is far stronger than necessary. At the canonical XF-071 source guard `J=q^{1/4}`, a bounded selector resource gives normalized moment mass `O(q^{-3/8})`; at the destination guard `J_+=q^{1/2}`, it gives `O(q^{-3/4})`.

Combining (4) with XF-085 closes the **static** real-divisor realization gate throughout the resource regime already used by the Xi-flow transport. For any fixed `0<kappa<1`, every family with `\mathcal R_S(Q)=o(J^3)` eventually satisfies (1). Since the Xi node budget has

\[
N=2q^2,
\qquad
K=O(q\log\log T)=o(N),
\tag{6}
\]

XF-085 then supplies exactly `N` unit-circle nodes of equal weight whose raw moments equal the prescribed `Q_m` on every `m in S`, with the unconstrained modes up to `K` chosen as in its benign completion. No exponentially accurate center-local function approximation, root matching, or weight quantization is needed for this finite selector state.

This does **not** finish the Xi-to-periodic bridge. One must still extract or transport a finite target moment vector from the actual Xi Gaussian/reference data with controlled `\mathcal R_S`, and the resulting real divisor must still be connected to the heat-compatible state used downstream. Positive-`Lambda` transition mass also remains separate. What is removed is a distinct algebraic concern: once the target visible state is controlled in the same guarded `X(B)` resource already required by XF-070--XF-071, equal-weight real-divisor existence at the exact Xi node budget no longer imposes an additional `ell^1` hypothesis.

## 1. Exact dual norm of the guarded selector resource

XF-070 and XF-079 give, on a union of complete disjoint selector sidebands, the exact coefficient resource

\[
\mathcal R_S(Q)
=
\sum_{m\in S}w_m|Q_m|^2,
\qquad
w_m=\frac{I_m}{4M^2}.
\tag{7}
\]

Apply Cauchy--Schwarz with the exact weights:

\[
\begin{aligned}
\sum_{m\in S}|Q_m|
&=
\sum_{m\in S}
\bigl(\sqrt{w_m}|Q_m|\bigr)w_m^{-1/2}\\
&\le
\mathcal R_S(Q)^{1/2}
\left(\sum_{m\in S}w_m^{-1}\right)^{1/2}.
\end{aligned}
\tag{8}
\]

Because `N=2M`, this becomes the exact operator-norm estimate

\[
\boxed{
\frac2N\sum_{m\in S}|Q_m|
\le
2\,\mathcal R_S(Q)^{1/2}
\left(\sum_{m\in S}\frac1{I_m}\right)^{1/2}.
}
\tag{9}
\]

The guard now supplies the entire gain. For `m>=1` and `|u|<1`,

\[
\pi m+u\ge \pi m-1\ge(\pi-1)m,
\tag{10}
\]

so

\[
I_m
\ge
C_g(\pi-1)^4m^4.
\tag{11}
\]

Therefore, for `S` contained in `{J,J+1,...}`,

\[
\sum_{m\in S}\frac1{I_m}
\le
\frac1{C_g(\pi-1)^4}
\sum_{m=J}^{\infty}m^{-4}.
\tag{12}
\]

The elementary integral bound

\[
\sum_{m=J}^{\infty}m^{-4}
\le J^{-4}+\int_J^\infty x^{-4}\,dx
\le\frac43J^{-3}
\tag{13}
\]

inserted into (9) proves (4).

There is no hidden dependence on the upper visible cutoff `K`, on the number of constrained modes, or on their phases. The only analytic constant is the fixed selector window through `C_g`.

## 2. The `J^3` threshold is intrinsic to this resource, not a loose union bound

Equation (9) is the exact norm of the embedding from the diagonal weighted space `(ell^2(w_m))` into `ell^1` on the prescribed support. Equality in Cauchy--Schwarz is attained, up to arbitrary phases, by vectors with

\[
|Q_m|\propto w_m^{-1}.
\tag{14}
\]

On a full dyadic block `J<=m<=2J`, XF-070 gives `w_m\asymp_g m^4/M^2`, so

\[
\sum_{m=J}^{2J}w_m^{-1}
\asymp_g M^2J^{-3}.
\tag{15}
\]

Thus the best possible normalized `ell^1` control from `\mathcal R_S` alone has scale

\[
\frac2N\|Q\|_{\ell^1}
\asymp_g
J^{-3/2}\mathcal R_S(Q)^{1/2}.
\tag{16}
\]

In particular, the boundary `\mathcal R_S(Q)\asymp J^3` can genuinely carry order-one normalized `ell^1` mass. One may choose the Cauchy--Schwarz extremal on `J<=m<=2J`; after scaling to make `(2/N)sum|Q_m|\asymp 1`, its typical raw moment size is only `O(M/J)`, below the trivial real-divisor bound `|P_m|<=N` for growing `J`. Hence the exponent in (5) is not an artifact of allowing individually impossible moments.

The favorable conclusion therefore comes specifically from the Xi architecture: its source/destination state has `O(1)` or smaller guarded `H^3` resource while the guard index tends to infinity. That combination sits parametrically far below the intrinsic `J^3` loss threshold.

## 3. XF-085 then gives exact equal-weight realization with room to spare

Fix, for example, `kappa=1/2`. If

\[
\mathcal R_S(Q)^{1/2}
\le
\frac{\sqrt{3C_g}(\pi-1)^2}{8}J^{3/2},
\tag{17}
\]

then (4) gives

\[
2\sum_{m\in S}|Q_m|\le\frac N2.
\tag{18}
\]

XF-085 constructs the positive trigonometric density

\[
W(\theta)
=1+2\operatorname{Re}
\sum_{m\in S}\frac{Q_m}{N}e^{im\theta},
\tag{19}
\]

with unconstrained moments through degree `K` set to zero. Equation (18) forces

\[
\frac12\le W(\theta)\le\frac32
\tag{20}
\]

uniformly, hence a fixed doubling constant. The Gilboa--Peled Chebyshev-type trigonometric quadrature theorem used in XF-085 then gives, for every sufficiently large prescribed node count `N>=C K`, an equal-weight degree-`K` quadrature for `W`.

Writing its nodes as `nu_1,...,nu_N` on the unit circle yields

\[
\boxed{
\sum_{j=1}^N\nu_j^{-m}=Q_m,
\qquad m\in S,
}
\tag{21}
\]

with exactly `N` roots. Since `N/K -> infinity` in (6), the node budget condition is automatic. Repeated nodes are allowed at this existence stage, exactly as in XF-084--XF-085.

The important change from XF-085 is logical rather than a stronger quadrature theorem: the fixed-margin hypothesis is no longer an independent thing to verify for a guarded resource-bounded state. It is a consequence of the norm already selected by the Xi-flow source/destination geometry.

## 4. Compatibility with the existing source and guard scales

XF-060 proves that the actual Xi carrier has

\[
\mathfrak E_T^{(2),\Xi}=o(1)
\tag{22}
\]

in the derivative-weighted moving-line selector norm. XF-070 identifies the periodic counterpart of that norm with (7), and XF-079 shows that the same periodic resource is pointwise in the selector center rather than requiring a full center average.

XF-071 then chooses the source-visible log-Vieta band

\[
J\asymp q^{1/4},
\qquad
K\asymp q\log\log T,
\tag{23}
\]

and a destination band beginning at

\[
J_+\asymp q^{1/2}.
\tag{24}
\]

If a source-to-periodic interface produces a finite moment target with merely

\[
\mathcal R_{[J,K]}(Q)=O(1),
\tag{25}
\]

then (4) gives

\[
\frac2N\sum_{m=J}^{K}|Q_m|
=O_g(q^{-3/8})=o(1).
\tag{26}
\]

On the farther destination band the same argument gives `O_g(q^{-3/4})`. Thus even an interface that loses the Xi source's `o(1)` resource down to a uniform `O(1)` bound still retains enormous margin for exact real-divisor realization.

More generally, (5) allows the interface resource to grow as `o(q^{3/4})` at the source guard `J=q^{1/4}` without leaving the fixed-margin cone. The equal-weight existence step therefore has substantially more tolerance than the downstream transition argument, which needs the normalized guarded resource itself to remain small.

## 5. Stress tests and evidence boundary

The growing lower guard is load-bearing. If `J=O(1)`, equation (4) supplies no asymptotic gain; a bounded weighted selector resource can then have order-one normalized `ell^1` moment mass, and XF-085's fixed-margin hypothesis remains a genuine separate condition. This is consistent with XF-069--XF-071: the purpose of the infrared quotient and guard band is precisely to stop insisting on the unresolved fixed modes.

Complete sidebands are used only to identify `\mathcal R_S` with the exact XF-079 `X(B)` norm. The algebraic inequality (9) remains true for any abstract moment vector equipped with the same weights. Edge-clipped sidebands can be handled with their exact reduced weights, but no uniform lower bound is available if an edge clips almost all of a sideband; the clean statement therefore keeps the one-sideband margin already standard in XF-070.

No root reality is assumed in deriving (4). Root reality enters only after XF-085 realizes the moment vector by an equal-weight unit-circle measure. Accordingly this finding is a **static existence theorem**, not a proof that the realized nodes evolve under the same periodic heat carrier demanded by XF-067--XF-071. It also does not show simplicity, preserve a particular ordering, or identify the real divisor with actual Xi zeros.

The conclusion is likewise not a transition theorem. XF-060 supplies small actual-Xi source resource; XF-071 supplies collision-safe guarded transport once a compatible periodic state is available. A separate interface still has to say that the moments extracted from the Gaussian/reference Xi description and the moments used by that periodic state agree in the exact guarded resource. A separate positive-transition theorem must still force nontrivial destination mass under `Lambda>0`.

## 6. Prior-art and novelty boundary

The weighted `ell^2 -> ell^1` estimate (8) is elementary Cauchy--Schwarz, and no novelty is claimed for it. Equal-weight trigonometric quadrature is classical; the load-bearing existence theorem remains the Gilboa--Peled result already anchored in `research/xi_flow/SOURCES.md` and used by XF-085. A targeted literature audit found the expected Chebyshev-type quadrature and trigonometric moment frameworks, but no external theorem is needed for the line-specific implication (4)--(6).

The durable Mathia delta is the recognition that **the exact selector-induced `m^4/M^2` resource and the existing growing nonlinear guard are dual to the only additional norm hypothesis introduced by XF-085**. This turns the apparent Gershgorin/equal-weight side condition into an automatic corollary throughout the state regime the Xi-flow architecture already transports. `SOURCES.md` therefore needs no new anchor.

## 7. Consequence for `xi_flow`

After XF-086, the real-divisor source bridge should no longer spend effort proving a separate fixed-margin `ell^1` estimate for guarded visible moments. The correct static gate is now:

\[
\boxed{
\text{produce the finite target moments with }
\mathcal R_{[J,K]}=o(J^3).
}
\tag{27}
\]

At the actual Xi-flow scales, any `O(1)` control in the destination-matched selector norm is already more than sufficient. XF-085 then realizes those visible moments exactly by an `N=2q^2` equal-weight real divisor.

This narrows the live bridge to two genuinely Xi/dynamical questions rather than a third moment-geometry problem: first, carry the Gaussian/reference Xi data into the finite guarded moment state with controlled `\mathcal R`; second, make the resulting real-divisor state heat-compatible through the interval needed by XF-071. The independent positive-`Lambda` transition-mass gate remains unchanged.