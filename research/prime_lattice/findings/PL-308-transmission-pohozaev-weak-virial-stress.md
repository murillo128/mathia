# PL-308 — Transmission-space Pohozaev closes the fixed-order admissibility gate and yields a weak virial stress identity

**Evidence:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + POHOZAEV-GATE-REDUCTION`

**Status:** `FIXED-s-POHOZAEV-ADMISSIBILITY-CLOSED + WEAK-VIRIAL-STRESS-EXACT + SMALL-s-UNIFORMITY-OPEN + ARITHMETIC-SIGN-OPEN`

## Precise claim

Let `I=(-1,1)`, fix an aperture `a>0` and an order `0<s<1`, and let `w` be a real normalized eigenstate of the fractional regularization used in `PL-307`, with zero extension outside `I`. Write

\[
q_{a,s}(w)
 =\frac{a^{-2s}E_s(w)-\|w\|_2^2}{2s}
 +c\|w\|_2^2+b_a(w),
\qquad
E_s(w)=\int_{\mathbb R}|\xi|^{2s}|\widehat w(\xi)|^2\,d\xi,
\]

and let `B_a` be the bounded self-adjoint lower-order operator associated with `b_a`. The eigen-equation is

\[
(-\Delta)^s w
 =a^{2s}\bigl[1+2s(\lambda_s(a)-c)\bigr]w
 -2s a^{2s}B_aw.
\tag{PL308-1}
\]

Then the actual completed-Weil right-hand side has enough fixed-order Sobolev regularity to bootstrap `w` into Grubb's `s`-transmission space `H^{s(\sigma)}(I)` for some

\[
\sigma>s+\frac12.
\tag{PL308-2}
\]

Consequently Grubb's low-regularity radial integration-by-parts/Pohozaev formula applies to `w` at **every fixed `s>0`**. In particular the endpoint quotient traces

\[
\tau_\pm=\gamma_0(d^{-s}w)(\pm1)
\]

exist, and the lower-order term admits the weak virial pairing

\[
V_a(w):=2\operatorname{Re}\langle B_aw,xw'\rangle,
\tag{PL308-3}
\]

where the bracket is the Sobolev duality furnished by the transmission theorem when the factors are not classically integrable. One has the exact identity

\[
\boxed{
\frac{\Gamma(1+s)^2}{2s}
\bigl(|\tau_+|^2+|\tau_-|^2\bigr)
 =E_s(w)+a^{2s}\bigl[b_a(w)+V_a(w)\bigr].
}
\tag{PL308-4}
\]

Thus the regularized completed-Weil eigenstate does **not** need the high interior Hölder hypotheses used in the Ros-Oton--Serra route of `PL-307` in order to possess the finite-`s` scalar boundary stress. The fixed-order Pohozaev-admissibility gate is closed by classical `\mu`-transmission theory. What remains hard is uniform passage as `s\downarrow0`: neither the bootstrap constants nor the weak virial pairings are shown to be uniformly compact, and no rational-prime-specific sign is obtained.

## 1. The lower Weil perturbation preserves the Sobolev regularity needed for the bootstrap

At a fixed finite aperture only finitely many prime-power channels are active. Their operators are compressed translations

\[
(C_hw)(x)=1_I(x)(Ew)(x+h),
\]

with `Ew` the zero extension. If `Ew\in H^t(\mathbb R)`, translation preserves that norm and restriction gives `C_hw\in H^t(I)`. The archimedean completion term has the bounded/Lipschitz convolution kernel already used in `PL-305`, so it is at least as regular as required below; the scalar pieces are harmless. Hence, for the only range needed in the iteration,

\[
Ew\in H^t(\mathbb R),\quad 0\le t<\frac12
\quad\Longrightarrow\quad
B_aw\in H^t(I).
\tag{PL308-5}
\]

The important point is that an interior source front produced by a translated boundary cusp may destroy a naive high-Hölder hypothesis, but it does **not** destroy this Sobolev mapping property: the compressed shift is the restriction of a genuine global translation of the zero extension.

## 2. Finite-step transmission bootstrap

Gerd Grubb's `\mu`-transmission theory applies to `P_s=(-\Delta)^s`, which is elliptic of order `2s`, type `s`, and factorization index `s`. In the `p=2` notation, if a supported distribution lies initially above the minimal admissible threshold and

\[
r^+P_su\in H^{\sigma-2s}(I),
\]

then elliptic regularity places it in the transmission solution space

\[
u\in H^{s(\sigma)}(I).
\tag{PL308-6}
\]

The form domain already gives `Ew\in H^s(\mathbb R)`. If `s>1/2`, the right-hand side of (PL308-1) is in `L^2(I)`, so taking `\sigma=2s` gives immediately `\sigma>s+1/2`.

Suppose now `0<s\le1/2`. While ordinary supported regularity remains below the boundary threshold, the standard characterization of the transmission spaces gives the familiar interior gain. More concretely, if for some `t<1/2`

\[
Ew\in H^t(\mathbb R),
\]

then (PL308-5) and (PL308-1) give `P_sw\in H^t(I)`. Grubb regularity therefore gives

\[
w\in H^{s(t+2s)}(I).
\tag{PL308-7}
\]

As long as `t+s<1/2`, this is the pre-boundary regime and yields the ordinary supported gain `Ew\in H^{t+2s}(\mathbb R)`. Iterating gains of `2s` reaches, after finitely many steps, a transmission parameter strictly above `s+1/2`; if an endpoint equality occurs, an arbitrarily small Sobolev loss followed by the next step moves strictly past it. Hence (PL308-2) holds for every fixed `s>0`.

This bootstrap is deliberately a **fixed-order statement**. The number of iterations grows as `s\downarrow0`, and the elliptic/transmission constants are not controlled uniformly here. It therefore does not contradict the `H^{1/2}` and BV compactness obstructions in `PL-293`, `PL-297`, and `PL-300`.

## 3. Grubb's low-regularity radial identity applies directly

Grubb's 2016 integration-by-parts theorem is stronger than the state-level hypothesis used in `PL-307`. For a classical elliptic even pseudodifferential operator of order `2s`, Theorem 4.7 extends the radial identity to `H^{s(\sigma)}` as soon as

\[
\sigma>s+\frac12,
\]

with the potentially singular products interpreted as Sobolev dualities. Corollary 4.8 specializes, for an `x`-independent homogeneous symbol, to the usual fractional Pohozaev identity. For `P_s=(-\Delta)^s` on the one-dimensional interval, Grubb uses the **interior** unit normal. At both endpoints `x\nu_{\rm int}=-1`. Setting `u=u'=w` therefore gives

\[
2\operatorname{Re}\langle P_sw,xw'\rangle
 =(2s-1)E_s(w)
 -\Gamma(1+s)^2\bigl(|\tau_+|^2+|\tau_-|^2\bigr).
\tag{PL308-8}
\]

No classical derivative of `w`, no pointwise interior Hölder estimate through order `1+2s`, and no pre-existing `H^{1/2}` estimate are required. The duality in Grubb's theorem is precisely what survives when the source contains translated fractional boundary singularities.

## 4. Exact weak virial stress identity

Put

\[
\alpha_{s,a}=a^{2s}\bigl[1+2s(\lambda_s(a)-c)\bigr].
\]

Equation (PL308-1) is

\[
P_sw=\alpha_{s,a}w-2sa^{2s}B_aw.
\tag{PL308-9}
\]

Once (PL308-2) holds, the same low-regularity duality makes both terms on the right pairable with `xw'`. By density in the transmission space, the ordinary dilation identity extends to this pairing:

\[
2\operatorname{Re}\langle w,xw'\rangle=-\|w\|_2^2=-1.
\tag{PL308-10}
\]

Thus the left side of (PL308-8) equals

\[
-\alpha_{s,a}-2sa^{2s}V_a(w).
\tag{PL308-11}
\]

On the other hand, pairing (PL308-9) with `w` gives the exact energy relation

\[
\alpha_{s,a}=E_s(w)+2sa^{2s}b_a(w).
\tag{PL308-12}
\]

Substituting (PL308-11)--(PL308-12) into (PL308-8) yields (PL308-4).

This identity is useful because it does not require differentiating the aperture dependence of a compressed translation. It packages all lower-order shape information into the well-defined weak dilation pairing `V_a(w)`.

## 5. Relation to `PL-307`

`PL-307` obtained, under a classical lower-order dilation identity,

\[
\frac{\Gamma(1+s)^2}{2s}
\bigl(|\tau_+|^2+|\tau_-|^2\bigr)
 =E_s(w)-a^{2s+1}\partial_a b_a(w).
\tag{PL308-13}
\]

The present identity is exactly consistent with it. Whenever fixed-state aperture differentiation is justified and dilation covariance gives

\[
V_a(w)=-b_a(w)-a\partial_ab_a(w),
\tag{PL308-14}
\]

(PL308-4) reduces to (PL308-13).

The conceptual gain is that (PL308-4) is already meaningful at finite `s` before proving (PL308-14). Therefore the high-regularity Pohozaev hypothesis and the classical fixed-state aperture derivative are not independent prerequisites for **existence of the scalar stress**. They are needed only if one wants to replace the weak virial term by the explicit aperture derivative used in the zero-order first-crossing program.

## 6. Adversarial source-front check

A compressed shift transports the fractional endpoint behavior `d(x)^s` to an interior front. For noninteger `s` this can violate the high interior Hölder assumptions appearing in the Ros-Oton--Serra state-level proposition used by `PL-307`. That observation could have killed the earlier proof route if those hypotheses were essential.

It does **not** kill the transmission-space route. The translated zero extension remains in the same `H^t(\mathbb R)` class, and Grubb's radial formula was explicitly developed to operate below the classical differentiability threshold by replacing products with Sobolev dualities. Hence source fronts are a reason to use (PL308-8), not an obstruction to it.

The check does not prove any `s`-uniform estimate. As `s\downarrow0`, the duality indices approach the critical `\pm1/2` boundary and the amount of regularity available above the Pohozaev threshold can collapse. This is exactly where the zero-order problem remains nontrivial.

## Prior-art and novelty audit

The transmission regularity itself is classical. Grubb's 2015 paper develops the full `\mu`-transmission Sobolev scale for fractional powers and proves the elliptic regularity implication used in (PL308-6). Grubb's 2016 paper proves the integration-by-parts and radial Pohozaev identities for even elliptic pseudodifferential operators, including the low-regularity Sobolev-duality form for transmission index above `s+1/2`. Ros-Oton--Serra remains the earlier fractional-Laplacian Pohozaev anchor used in `PL-307`.

The mathematical delta stored here is narrower: applying those classical transmission theorems to the **actual finite compressed-prime-shift plus completion right-hand side** shows that fixed-`s` Pohozaev admissibility is automatic after a finite Sobolev bootstrap, despite the translated boundary fronts, and yields the exact weak completed-Weil stress identity (PL308-4). A targeted search found the general fractional/transmission Pohozaev literature but no source carrying this completed-Weil specialization. No global novelty is claimed for Grubb's theorem or for Pohozaev calculus itself.

## Evidence boundaries and remaining gates

This result closes only the fixed-order analytic admissibility gate. It does not establish any of the following:

- uniform transmission/Sobolev estimates as `s\downarrow0`;
- convergence of `V_a(w_{s,a})`, `\partial_ab_a(w_{s,a})`, or the renormalized endpoint traces;
- uniform BV or derivative-measure compactness for the actual completed-Weil branch;
- differentiability through all prime-power activation thresholds;
- a sign for the first eigenvalue crossing;
- any rational-prime-specific rigidity. The Grubb mechanism is generic for this class of elliptic fractional problems.

The live zero-order gate is therefore sharper than in `PL-307`: prove source-structured **uniform small-`s` convergence of the weak lower virial**, or prove enough BV/derivative-measure compactness to identify it with the explicit `PL-305` aperture derivative and pass that derivative to `s=0`. Only after that does the arithmetic sign/first-crossing problem become available.

## Consequence for the research line

The finite-`s` boundary-stress mechanism is no longer conditional on a hard-to-verify Ros-Oton--Serra high-Hölder hypothesis for the actual completed-Weil eigenstate. The obstruction has moved entirely to the singular `s\downarrow0` limit and then to arithmetic sign. In particular, further work should not spend effort reproving classical fixed-order Pohozaev regularity for each translated source front; it should attack uniform source-structured compactness or the weak-virial limit itself.

## Sources

- Gerd Grubb, “Fractional Laplacians on domains, a development of Hörmander's theory of `\mu`-transmission pseudodifferential operators,” *Advances in Mathematics* **268** (2015), 478–528. DOI: https://doi.org/10.1016/j.aim.2014.09.018. arXiv: https://arxiv.org/abs/1310.0951.
- Gerd Grubb, “Integration by parts and Pohozaev identities for space-dependent fractional-order operators,” *Journal of Differential Equations* **261**(3) (2016), 1835–1879. DOI: https://doi.org/10.1016/j.jde.2016.04.017. arXiv: https://arxiv.org/abs/1511.03901.
- Xavier Ros-Oton, Joaquim Serra, “The Pohozaev identity for the fractional Laplacian,” *Archive for Rational Mechanics and Analysis* **213**(2) (2014), 587–628. DOI: https://doi.org/10.1007/s00205-014-0740-2. arXiv: https://arxiv.org/abs/1207.5986.
