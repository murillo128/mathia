# FD-150 — Ancestry depth trades only the child tax along a Sathe--Selberg phase curve

- **Date:** 2026-09-16
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** quantitative ancestry obstruction / depth-distortion phase diagram
- **Depends on:** FD-148, FD-149

## Claim

FD-149 locates the bounded-child-distortion transition near the typical squarefree prime-factor depth `log log T`. Two quantitative points remain hidden in that formulation. First, at a fixed fraction below typical depth the reachable coefficient mass has an explicit large-deviation scale, so the required child distortion can be quantified rather than merely declared divergent. Second, increasing the ancestry depth only relaxes the **child-side** endpoint tax: for a fixed anchor, the parent-side concentration tax of FD-148 remains linear in `T` at every depth.

Let

\[
V_T=\{n\le T:\mu^2(n)=1\},
\qquad
\nu_T(n)=|V_T|^{-1},
\qquad
\lambda_T:=\log\log T,
\tag{1}
\]

and let `D` be a fixed finite divisor-closed subset of the squarefree integers containing `1`. Write

\[
r_D:=\max_{d\in D}\omega(d).
\tag{2}
\]

For `L>=1`, retain the FD-149 ancestry relation

\[
E_T^{(\le L)}
=
\{(n,m)\in V_T^2:n\mid m,\ 1\le\omega(m/n)\le L\},
\tag{3}
\]

and let `eta_T` be an arbitrary probability measure on this edge set. Write `eta_T^-` and `eta_T^+` for its parent and child marginals and `h_{D,T}^{(<=L)}` for the anchored Cheeger constant.

Fix `alpha` with

\[
0<\alpha<1
\tag{4}
\]

and put

\[
L_T=\lfloor\alpha\lambda_T\rfloor.
\tag{5}
\]

Define the Poisson/Sathe--Selberg rate function

\[
I(\alpha):=1-\alpha+\alpha\log\alpha>0.
\tag{6}
\]

Then the descendants reachable from the anchor satisfy the two-sided estimate

\[
\boxed{
\nu_T(R_{D,L_T}(T))
\asymp_{D,\alpha}
\frac{1}
{\sqrt{\lambda_T}\,(\log T)^{I(\alpha)}}.
}
\tag{7}
\]

Consequently, if the child marginal obeys the FD-149 domination condition

\[
\eta_T^+(m)\le K_T\nu_T(m)
\qquad(m\in R_{D,L_T}(T)),
\tag{8}
\]

then

\[
\boxed{
h_{D,T}^{(\le L_T)}
\ll_{D,\alpha}
\frac{K_T}
{\sqrt{\log\log T}\,(\log T)^{I(\alpha)}}.
}
\tag{9}
\]

Thus uniformly positive anchored expansion forces the explicit child-distortion tax

\[
\boxed{
K_T
\gg_{c,D,\alpha}
\sqrt{\log\log T}\,(\log T)^{I(\alpha)}.
}
\tag{10}
\]

In particular, if `K_T=O((log T)^kappa)` with

\[
\kappa<I(\alpha),
\tag{11}
\]

then the anchored expansion still tends to zero. Even at the boundary `K_T=O((log T)^{I(alpha)})`, the residual factor `1/sqrt(log log T)` in (9) forces vanishing expansion.

The independent parent-side obstruction does not improve with depth. If, on the fixed seed,

\[
\eta_T^-(d)\le P_T\nu_T(d)
\qquad(d\in D),
\tag{12}
\]

then for **every** depth `L=L_T`, including depths much larger than `log log T`,

\[
\boxed{
h_{D,T}^{(\le L)}
\le
(\zeta(2)|D|+o_D(1))\frac{P_T}{T}.
}
\tag{13}
\]

Hence positive fixed-seed expansion always requires average parent amplification of order `T` unless the anchor itself is changed. Reaching the Erdos--Kac depth can remove the child-density obstruction, but it does not make a fixed anchor a bounded-distortion object.

The resulting resource picture is therefore sharper than a simple choice between endpoint concentration and depth. For a fixed anchor, the parent endpoint is intrinsically singular; ancestry depth controls how much **additional child-side singularity** must be paid. Below typical depth, that second price follows the explicit curve `I(alpha)`.

## 1. Reachable mass is squeezed between two rank tails

Because `1 in D`, every squarefree integer outside `D` with between one and `L` prime factors is reachable from the anchor through the edge `(1,m)`. Conversely FD-149 already gives, for every reachable `m`,

\[
\omega(m)\le r_D+L.
\tag{14}
\]

Thus

\[
\{m\in V_T\setminus D:1\le\omega(m)\le L\}
\subseteq
R_{D,L}(T)
\subseteq
\{m\in V_T\setminus D:\omega(m)\le L+r_D\}.
\tag{15}
\]

For `L=L_T=floor(alpha lambda_T)`, the two rank thresholds differ by only the fixed amount `r_D`. It is therefore enough to estimate the squarefree lower tail of `omega` at a fixed fraction of its normal order.

This also shows why the estimate is not merely an upper bound inherited from FD-149. For every fixed divisor-closed anchor containing `1`, the complement-cut reachable set really contains the entire low-rank squarefree population apart from the fixed anchor itself; changing the finite anchor can modify only the constant in the large-deviation scale.

## 2. Sathe--Selberg gives the exact logarithmic exponent

Let

\[
S_k(T)
:=
\#\{m\le T:\mu^2(m)=1,\ \omega(m)=k\}.
\tag{16}
\]

The squarefree Sathe--Selberg local law, in the fixed proportional-rank regime `k=alpha lambda_T+O(1)`, gives

\[
\frac{S_k(T)}{|V_T|}
\asymp_\alpha
\frac1{\log T}
\frac{\lambda_T^{k-1}}{(k-1)!}.
\tag{17}
\]

Only the order is needed here; the analytic Sathe--Selberg factor is positive and bounded above and below when `alpha` stays in a compact subset of `(0,1)`.

Stirling's formula at `k=alpha lambda_T+O(1)` gives

\[
\frac1{\log T}
\frac{\lambda_T^{k-1}}{(k-1)!}
\asymp_\alpha
\lambda_T^{-1/2}
\exp\{-\lambda_T I(\alpha)\}.
\tag{18}
\]

Since `exp(lambda_T)=log T`, this is

\[
\boxed{
\frac{S_k(T)}{|V_T|}
\asymp_\alpha
\frac1{\sqrt{\lambda_T}(\log T)^{I(\alpha)}}.
}
\tag{19}
\]

For `alpha<1`, the lower tail is endpoint-dominated. In the factorial core of (17), decreasing `k` by one multiplies the local mass by approximately `k/lambda_T=alpha<1`. On any fixed compact subinterval below `1`, the Sathe--Selberg analytic factor stays bounded, so summing the ranks below `alpha lambda_T+O(1)` changes (19) only by an `alpha`-dependent constant. Ranks a fixed positive fraction farther below the endpoint are exponentially smaller and the finitely small ranks are covered by the classical fixed-rank estimates.

Therefore

\[
\boxed{
\nu_T\!\left(\omega(m)\le\alpha\lambda_T+O(1)\right)
\asymp_\alpha
\frac1{\sqrt{\lambda_T}(\log T)^{I(\alpha)}}.
}
\tag{20}
\]

Applying (20) to both sides of (15), with the fixed shift `r_D` and the removal of the fixed set `D`, proves (7).

## 3. The child-distortion phase curve

The complement-cut inequality from FD-149 is

\[
h_{D,T}^{(\le L)}
\le
\frac{K_T\nu_T(R_{D,L}(T))}
{1-\nu_T(D)}.
\tag{21}
\]

Because `D` is fixed,

\[
\nu_T(D)=O_D(T^{-1}).
\tag{22}
\]

Substituting (7) into (21) proves (9), and the contrapositive under `h>=c>0` proves (10).

The curve has a useful explicit form. The function

\[
I(\alpha)=1-\alpha+\alpha\log\alpha
\tag{23}
\]

is strictly decreasing on `(0,1)`, from `1` to `0`. Thus a child law with only polylogarithmic distortion

\[
K_T\lesssim(\log T)^\kappa
\tag{24}
\]

cannot support constant anchored exposure at a depth fraction `alpha` whenever `kappa<I(alpha)`. The tradeoff is not qualitative: it has a classical large-deviation exponent.

Writing `alpha=1-delta` for a fixed `0<delta<1`,

\[
I(1-\delta)
=
\delta+(1-\delta)\log(1-\delta)
=
\frac{\delta^2}{2}+\frac{\delta^3}{6}+O(\delta^4).
\tag{25}
\]

Hence a fixed fractional deficit below the typical depth costs

\[
K_T
\gg
\sqrt{\log\log T}
(\log T)^{\delta^2/2+O(\delta^3)}.
\tag{26}
\]

For example, depth `L_T~(1/2)log log T` has

\[
I(1/2)=\frac12-\frac12\log2\approx0.153426,
\tag{27}
\]

so the complement cut alone requires child amplification at least of order

\[
\sqrt{\log\log T}(\log T)^{0.153426\ldots}.
\tag{28}
\]

This interpolates the wide gap left between the fixed-depth bound and the Erdos--Kac transition of FD-149. It does not replace either endpoint regime: fixed depth corresponds to `alpha->0`, where a separate fixed-rank asymptotic is sharper, while the central window `L_T=lambda_T+O(sqrt(lambda_T))` is governed by Erdos--Kac rather than endpoint domination of the lower tail.

## 4. Depth never removes the fixed-anchor parent tax

Define the parent marginal for the depth-`L` edge measure by

\[
\eta_T^-(n)
:=
\sum_{m:(n,m)\in E_T^{(\le L)}}\eta_T(n,m).
\tag{29}
\]

Test the same complement cut

\[
A_T=V_T\setminus D.
\tag{30}
\]

Because `D` is divisor-closed, no divisibility edge of any length can enter `D` from `A_T`. Every crossing edge therefore starts in `D`, so

\[
\eta_T(\partial A_T)
\le
\sum_{d\in D}\eta_T^-(d).
\tag{31}
\]

If (12) holds,

\[
\eta_T(\partial A_T)
\le
P_T\nu_T(D).
\tag{32}
\]

The squarefree counting law gives

\[
\nu_T(D)
=(\zeta(2)|D|+o_D(1))T^{-1}.
\tag{33}
\]

Dividing (32) by `nu_T(A_T)=1-nu_T(D)` proves (13).

This is the parent half of FD-148 with the one-step hypothesis removed. The proof never used the length of a crossing edge, only divisor closure of the anchor. Consequently a depth-`log log T` construction with a bounded child marginal can evade the **child** sparsity wall of FD-149, but it must still assign order-one edge probability to paths leaving a coefficient set of mass `Theta_D(1/T)` if it wants positive fixed-seed expansion.

That distinction matters when interpreting a proposed source-native transfer. A construction may naturally become nonlocal without naturally concentrating its parent marginal on the anchor. Typical-depth reach by itself is therefore not a positive mechanism.

## 5. Matched controls and scope

The child exponent in (10) is sharp for the complement-cut cardinality mechanism up to constants at each fixed `alpha`. Equation (15) and the Sathe--Selberg estimate show that the anchor can genuinely reach a coefficient fraction of exactly the order in (7); no stronger child-distortion exponent can be extracted from this cut alone.

Likewise, the linear parent tax is a fixed-anchor statement. A growing anchor `D_T` can change `nu_T(D_T)` and therefore the parent cost. That spends nonlocal information in the anchor instead of the transfer and must be audited separately against the source-reconstruction boundary of FD-142--FD-144.

The result remains restricted to positive ancestry edge measures and finite-`L^q` binary coercivity through FD-147. Signed or oscillatory transfers, `L^infinity`, and genuinely nonlocal destination functionals outside the positive edge model are not covered.

The theorem is only a necessary-condition screen. Even a measure that pays the parent tax and satisfies the child-depth phase curve may have other cheap anchored cuts, so neither (10) nor typical-depth reach is a sufficiency theorem for a positive Cheeger constant.

## 6. Prior-art and evidence boundary

The Sathe--Selberg local distribution and the rate function in (6) are classical probabilistic number theory. No novelty is claimed for the large-deviation law of `omega(n)`. The existing `research/farey_discrepancy/SOURCES.md` already anchors Gerald Tenenbaum's treatment of Selberg--Delange/Sathe--Selberg exact central prime-factor counts, explicitly including the squarefree variant used in FD-139, so no new external dependency is needed.

A literature audit also finds classical moderate/large-deviation treatments of Erdos--Kac-type additive functions; these reinforce that the number-theoretic tail itself is prior art. The line-specific durable statement is the splice of that tail with the exact fixed-anchor complement-cut obstruction of FD-148--FD-149, producing the explicit depth-versus-child-distortion phase curve and separating it from the depth-independent parent tax.

No RH input, zero-density theorem, numerical experiment, or source-specific Möbius cancellation is used. The argument is exact apart from standard squarefree counting and Sathe--Selberg asymptotics.

## 7. Falsifiable next test

A proposed positive Farey-native ancestry weighting should now expose three quantities before a full coercivity proof is attempted:

\[
L_T,
\qquad
P_T:=\max_{d\in D}\frac{\eta_T^-(d)}{\nu_T(d)},
\qquad
K_T:=\max_{m\in R_{D,L_T}(T)}\frac{\eta_T^+(m)}{\nu_T(m)}.
\tag{34}
\]

For a fixed anchor, if `P_T=o(T)`, the construction is dead regardless of depth. If `L_T~alpha log log T` with fixed `alpha<1` and

\[
K_T=o\!\left(
\sqrt{\log\log T}(\log T)^{I(\alpha)}
\right),
\tag{35}
\]

it is also dead on the child side. Only after both endpoint screens survive is it meaningful to test the remaining non-anchor cuts and then the later information-budget obstruction of FD-144.

The first genuinely new positive candidate would therefore not be merely a depth-`log log T` ancestry graph. It would need a Farey/arithmetic reason for the unavoidable fixed-anchor parent concentration, together with enough multiplicative reach or child distortion to cross the phase curve without simply encoding the coefficient source.