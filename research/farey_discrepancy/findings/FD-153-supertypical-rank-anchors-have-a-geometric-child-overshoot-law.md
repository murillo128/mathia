# FD-153 — Supertypical rank anchors have a geometric child-overshoot law

- **Date:** 2026-09-16
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** near-total-anchor phase law / moderate-deviation closure
- **Depends on:** FD-147, FD-151, FD-152

## Claim

FD-152 identifies the child-depth scale for a central rank anchor

\[
D_T(r)=\{n\le T:\mu^2(n)=1,\ \omega(n)\le r\}
\]

when

\[
r=\log\log T+O(\sqrt{\log\log T}).
\]

It deliberately leaves open the near-total-anchor regime in which the normalized anchor location tends to `+infinity`. In that regime the remaining upper tail is no longer Gaussian at fixed scale. Its conditional rank excess has a simpler local law: after a supertypical rank has already been anchored, the next prime-factor ranks form an asymptotically geometric tail. In the moderate-deviation transition this geometric law rescales to an exponential law.

Put

\[
V_T:=\{n\le T:\mu^2(n)=1\},
\qquad
\nu_T(n):=|V_T|^{-1},
\qquad
\lambda_T:=\log\log T,
\tag{1}
\]

and write

\[
q_T(k):=\nu_T(\omega(n)=k).
\tag{2}
\]

Let `r_T` satisfy

\[
\alpha_T:=\frac{r_T}{\lambda_T}>1,
\qquad
\alpha_T\le2-\varepsilon
\tag{3}
\]

for some fixed `epsilon>0`. Condition on the unanchored tail and define the rank overshoot

\[
J_T:=\omega(n)-r_T
\quad\text{under}\quad
\nu_T(\,\cdot\mid\omega(n)>r_T).
\tag{4}
\]

There are two useful regimes.

### Fixed supertypical ratio

If

\[
\alpha_T\longrightarrow\alpha\in(1,2),
\tag{5}
\]

then for every fixed integer `L>=1`,

\[
\boxed{
\nu_T(1\le J_T\le L)
\longrightarrow
1-\alpha^{-L}.
}
\tag{6}
\]

Equivalently, `J_T` converges to the geometric law on the positive integers with

\[
\boxed{
\Pr(J=j)=(1-\alpha^{-1})\alpha^{-(j-1)}.
}
\tag{7}
\]

At the same time the unanchored coefficient mass is already a large-deviation tail:

\[
\boxed{
1-\nu_T(D_T(r_T))
\asymp_{\alpha}
\frac{1}
{\sqrt{\lambda_T}\,(\log T)^{I(\alpha)}},
\qquad
I(\alpha)=1-\alpha+\alpha\log\alpha>0.
}
\tag{8}
\]

Thus a bounded number of additional ancestry ranks can expose a fixed fraction of the remaining coefficients only after the anchor has fixed `1-o(1)` of the entire squarefree coefficient space.

### Moderate-deviation transition

Suppose instead

\[
\alpha_T=1+\delta_T,
\qquad
\delta_T\to0,
\qquad
\delta_T\sqrt{\lambda_T}\to\infty.
\tag{9}
\]

Equivalently, with

\[
z_T:=\frac{r_T-\lambda_T}{\sqrt{\lambda_T}},
\tag{10}
\]

we have `z_T->infinity` but `z_T=o(sqrt(lambda_T))`. Then

\[
\boxed{
\delta_T J_T\Longrightarrow \operatorname{Exp}(1).
}
\tag{11}
\]

More precisely, for any depth sequence `L_T>=1`,

\[
\delta_TL_T\longrightarrow\ell\in[0,\infty]
\]

implies

\[
\boxed{
\nu_T(1\le J_T\le L_T)
\longrightarrow
1-e^{-\ell},
}
\tag{12}
\]

with the convention `e^{-infinity}=0`. Hence the conditional child-depth scale is

\[
\boxed{
L_T\asymp\delta_T^{-1}
\asymp
\frac{\sqrt{\log\log T}}{z_T}.
}
\tag{13}
\]

This interpolates continuously between the `sqrt(log log T)` depth of FD-152 and the constant depth of the fixed-`alpha>1` regime.

The anchor cost can also be quantified in this window. The same local law gives

\[
\boxed{
1-\nu_T(D_T(r_T))
\asymp
\frac{
\exp\{-\lambda_T I(1+\delta_T)\}
}{\delta_T\sqrt{\lambda_T}}.
}
\tag{14}
\]

In particular the anchor mass tends to one. If additionally `z_T=o(lambda_T^(1/6))`, then `lambda_T I(1+delta_T)=z_T^2/2+o(1)`, so (14) has the usual Gaussian-Mills exponential scale `z_T^{-1}e^{-z_T^2/2}` up to bounded factors.

For the positive divisibility ancestry model of FD-152, the exact reachable shell remains

\[
R_{r_T,L_T}(T)
=\{n\in V_T:r_T<\omega(n)\le r_T+L_T\}.
\tag{15}
\]

If the child marginal satisfies

\[
\eta_T^+(m)\le K_T\nu_T(m)
\qquad(m\in R_{r_T,L_T}(T)),
\tag{16}
\]

then the complement cut gives

\[
\boxed{
 h_{r_T,T}^{(\le L_T)}
 \le
 K_T\,\Pr(J_T\le L_T).
}
\tag{17}
\]

Consequently, if `K_T<=K`, `0<c<K`, and

\[
\liminf h_{r_T,T}^{(\le L_T)}\ge c,
\tag{18}
\]

then in the moderate-deviation regime

\[
\boxed{
\liminf \delta_TL_T
\ge
-\log(1-c/K).
}
\tag{19}
\]

For fixed `alpha>1` and fixed integer depth `L`, the corresponding necessary condition is

\[
\boxed{
1-\alpha^{-L}\ge c/K.
}
\tag{20}
\]

Thus the near-total-anchor escape left by FD-152 is real at the level of the complement cut: bounded child distortion can reduce the required ancestry depth below the Gaussian width, eventually to `O(1)`. But it can do so only by anchoring an asymptotically total fraction of the source coefficients.

## 1. Squarefree Sathe--Selberg gives the local rank ratio

The squarefree Sathe--Selberg law already anchored in `SOURCES.md` gives, uniformly when `k/lambda_T` stays in a compact subset of `(0,2)`,

\[
q_T(k)
=
\bigl(A(k/\lambda_T)+o(1)\bigr)
\frac1{\log T}
\frac{\lambda_T^{k-1}}{(k-1)!},
\tag{21}
\]

where `A` is positive and smooth on such compact sets. Only ratios of neighboring ranks are needed here. From (21), uniformly for `k=r_T+j` as long as `j=o(sqrt(lambda_T))`,

\[
\frac{q_T(k+1)}{q_T(k)}
=
\frac{\lambda_T}{k}\,(1+o(1)).
\tag{22}
\]

For a fixed supertypical ratio `alpha>1`, (22) immediately gives for each fixed `j>=1`

\[
\frac{q_T(r_T+j)}{q_T(r_T+1)}
\longrightarrow
\alpha^{-(j-1)}.
\tag{23}
\]

The upper tail is endpoint-dominated. Indeed, on every fixed interval of ranks between `alpha lambda_T` and `beta lambda_T` with `alpha<beta<2`, the consecutive-rank ratio is eventually bounded by a constant below one. The still farther tail is exponentially smaller by the standard fixed-parameter Selberg--Delange exponential-moment bound for `omega`; its large-deviation exponent is strictly larger because `I(beta)>I(alpha)` for `beta>alpha>1`. Therefore summing (23) is legitimate and gives

\[
\sum_{j\ge1}q_T(r_T+j)
=
q_T(r_T+1)
\left(\frac1{1-\alpha^{-1}}+o(1)\right).
\tag{24}
\]

Dividing the first `L` terms of the same geometric sum by (24) proves (6)--(7).

Stirling's formula in (21) gives

\[
q_T(r_T+1)
\asymp_\alpha
\lambda_T^{-1/2}
\exp\{-\lambda_T I(\alpha)\}.
\tag{25}
\]

Since `exp(lambda_T)=log T`, equations (24)--(25) are exactly (8).

## 2. The geometric tail becomes exponential just above the Gaussian window

Now assume (9). Put `delta=delta_T` and suppress `T` temporarily. The characteristic overshoot scale suggested by (22) is `1/delta`. This scale is still much smaller than the Gaussian width because

\[
\frac{1/\delta}{\sqrt\lambda}
=
\frac1{\delta\sqrt\lambda}
\longrightarrow0.
\tag{26}
\]

Hence (22) may be multiplied uniformly over `j=O(1/delta)`. For such `j`,

\[
\begin{aligned}
\log\frac{q_T(r+j)}{q_T(r+1)}
&=
-\sum_{m=1}^{j-1}
\log\!\left(1+\delta+O\!\left(\frac m\lambda\right)\right)
+o(1)\\
&=
-(j-1)\delta
+O(j\delta^2)
+O(j^2/\lambda)
+o(1).
\end{aligned}
\tag{27}
\]

If `delta j` remains bounded, then

\[
j\delta^2=O(\delta)\to0,
\qquad
j^2/\lambda
=O((\delta^2\lambda)^{-1})\to0,
\tag{28}
\]

so

\[
\boxed{
\frac{q_T(r+j)}{q_T(r+1)}
=
\exp\{-\delta(j-1)+o(1)\}
}
\tag{29}
\]

uniformly on bounded `delta j` ranges.

To pass from the local ratios to the whole conditional tail, first truncate at `j<=M/delta` with fixed `M`. Equation (29) makes the truncated tail a Riemann sum for `e^{-u}`. Beyond that point the rank ratios only decrease at first order as the rank rises; a geometric majorant gives a remainder `O(e^{-cM})` relative to the full tail, uniformly for large `T`. Ranks a fixed positive fraction above `lambda_T` are again exponentially negligible by the same Selberg--Delange exponential-moment bound. Sending `T->infinity` and then `M->infinity` proves

\[
\Pr(\delta_TJ_T>x)\longrightarrow e^{-x}
\qquad(x\ge0),
\tag{30}
\]

which is (11), and (12) follows.

The same summation shows

\[
\sum_{j\ge1}q_T(r_T+j)
\asymp
\frac{q_T(r_T+1)}{\delta_T}.
\tag{31}
\]

Uniform Stirling in (21) gives

\[
q_T(r_T+1)
\asymp
\lambda_T^{-1/2}
\exp\{-\lambda_T I(1+\delta_T)\},
\tag{32}
\]

so (31)--(32) prove (14).

## 3. The ancestry consequence is a conditional hazard law

FD-152 proves the exact shell identity (15) and the child-side complement-cut estimate

\[
h_{r,T}^{(\le L)}
\le
K_T
\frac{\nu_T(r<\omega\le r+L)}
{\nu_T(\omega>r)}.
\tag{33}
\]

The quotient in (33) is exactly `Pr(J_T<=L)`. Substitution of (6) gives the fixed-`alpha` law, while substitution of (12) gives the moderate-deviation law.

Under (18), (17) forces

\[
\liminf\Pr(J_T\le L_T)\ge c/K.
\tag{34}
\]

If `delta_TL_T->ell`, (12) turns this into

\[
1-e^{-\ell}\ge c/K,
\tag{35}
\]

which is equivalent to (19). The same argument with (6) yields (20).

This identifies the correct local resource. Above the central window, ancestry depth is governed by the **hazard of the remaining rank tail**, not by its absolute location. For `r=lambda+z sqrt(lambda)` with `z->infinity` and `z=o(sqrt(lambda))`, the hazard scale is `delta~z/sqrt(lambda)`, hence the conditional depth scale is `sqrt(lambda)/z`.

## 4. The apparent escape spends almost the entire source

The parent-side complement-cut screen of FD-151 is

\[
h_{r,T}^{(\le L)}
\le
P_T\frac{p_T(r)}{1-p_T(r)}.
\tag{36}
\]

For the supertypical anchors here, (8) or (14) gives `p_T(r)->1`, so (36) no longer forces a growing parent distortion. This is exactly why the near-total-anchor regime was left open by FD-152.

But that disappearance has a precise source cost. In the fixed-`alpha>1` regime the unanchored fraction is only

\[
\asymp_\alpha
[\sqrt{\log\log T}(\log T)^{I(\alpha)}]^{-1},
\tag{37}
\]

and in the moderate regime it is given by (14). Thus the anchor directly fixes the Möbius orientation on `1-o(1)` of the squarefree coefficient space before the shallow transfer begins.

The depth reduction is therefore not a free improvement of the ancestry mechanism. The phase diagram is now continuous:

\[
\text{central anchor }z=O(1)
\Rightarrow
L\asymp\sqrt\lambda,
\]

\[
\text{moderate anchor }z\to\infty,\ z=o(\sqrt\lambda)
\Rightarrow
L\asymp\sqrt\lambda/z,
\]

and

\[
\text{fixed }\alpha>1
\Rightarrow
L=O(1),
\]

but the last two regimes simultaneously drive the anchored coefficient mass to one.

## 5. Stress tests and boundaries

This result closes only the explicit near-total-anchor gap in the **complement-cut necessary condition**. It does not prove a positive Cheeger lower bound for any edge measure. Other cuts may still have arbitrarily small exposure even after the parent and child screens here are paid.

The squarefree Sathe--Selberg input is used only below its classical proportional-rank boundary; (3) deliberately stays a fixed distance below `2 lambda_T`. No claim is made for anchors with rank at or beyond that boundary. The moderate law also requires `delta_T sqrt(lambda_T)->infinity`; when this quantity stays bounded, the conditional Gaussian law of FD-152 is the correct regime and (11) must not be extrapolated backward.

The ancestry model remains positive, divisibility-based and finite-`L^q`, with rank anchors and depth measured by added prime factors. Signed transfers, non-divisibility observations, `L^infinity`, and genuinely nonlocal Farey functionals remain outside the theorem.

The source-cost statement is a cardinality fact, not a proof that near-total anchoring is logically circular. A future Farey-native identity could in principle impose agreement on almost every coefficient without observing them separately. Such a mechanism would have to be exhibited and audited against the reconstruction/information barriers of FD-142--FD-144; FD-153 only removes the possibility of treating the shrinking child depth as an independent gain.

## 6. Prior art and novelty boundary

Sathe--Selberg local laws and moderate/large deviations for additive prime-factor counts are classical. The existing Tenenbaum source anchor already supplies the squarefree local law needed for (21); no novelty is claimed for the rate function `I`, for geometric endpoint domination of a large-deviation tail, or for the exponential scaling limit of a geometric law. General moderate- and large-deviation theorems for Erdős--Kac additive functions are nearby prior art as well.

The line-specific contribution is the exact splice with FD-152's rank-shell ancestry cut: **the conditional upper-tail hazard is the child-depth currency of a near-total rank anchor**. This turns FD-152's qualitative warning about `z_T->infinity` into the quantitative interpolation (13), while simultaneously pricing the source expenditure through (8) and (14).

No new external theorem is load-bearing beyond the squarefree Sathe--Selberg/Selberg--Delange machinery already anchored in `SOURCES.md`, so no source-file update is required.

## 7. Falsifiable next test

The complement-cut phase diagram is now closed from fixed seeds through central and supertypical rank anchors. A positive ancestry proposal should not be credited merely for achieving depth below `sqrt(log log T)` by moving the anchor into the upper tail. It should state the actual anchor mass and explain what Farey-native observable forces agreement on that set.

The next source-valid test is therefore orthogonal to further rank-tail asymptotics: construct an explicit Farey/Franel-derived anchor or boundary functional and determine whether it can impose a macroscopic or near-total coefficient anchor **without already containing enough information to reconstruct the Möbius orientation being recovered**. If not, the near-total-anchor escape is only a transfer of information from the edge law into the boundary condition.

## Conclusion

The near-total-anchor regime does reduce ancestry depth, but in a completely quantified way. Above the typical rank, the remaining squarefree coefficients have a geometric conditional overshoot; in the moderate window that overshoot becomes exponential after scaling by the excess `delta_T`. Hence the child-depth scale falls from `sqrt(log log T)` to `sqrt(log log T)/z_T`, and eventually to a constant for a fixed supertypical rank ratio. The price is simultaneous: the anchor fixes `1-o(1)` of the squarefree coefficient space. The complement-cut escape of FD-152 is therefore not an unpriced loophole; it is a direct exchange of child depth for almost-total source anchoring.