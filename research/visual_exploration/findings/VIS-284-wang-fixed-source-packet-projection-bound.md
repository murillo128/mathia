# VIS-284 — fixed-source Wang packets are bounded projections, and Laplace-null localization has a total-variation cost

## Claim

Keep the compact fixed-source regime of `VIS-274`–`VIS-283`: `H=T^theta` with fixed `0<theta<1`, `L=log T`, `I=(T,T+H]`, and

`x=e^(2*pi*q)`

with `q` in a fixed compact interval `K=[q_-,q_+] subset (0,infinity)`.

Let `h_T in C_c^infinity(K)` be any real packet family with

`sup_T ||h_T||_1 < infinity`,

and define the associated even Wang test

`g_T(alpha)=h_T(L|alpha|/(2*pi)).`

Write

`W_I(g_T)=sum_(gamma,gamma' in I) hat g_T(i(rho-rho')L/(2*pi)) w(rho-rho')`

and let

`ell_T=log(T/(2*pi))`.

Then the exact Fourier-inversion identity in Wang together with the uniform fixed-source field-energy expansion of `VIS-283` gives

`(2*pi/(H L)) W_I(g_T)`
` = 4*pi (ell_T^2/L^2) integral_K h_T(q)e^(-4*pi q)dq`
`   + (4*pi/L^2) integral_K h_T(q) Q_gamma(e^(2*pi q))dq`
`   + o_K,||h||_1(L^-2),`

where

`Q_gamma(x)=S_D(x)+C_Lambda/x^2`,

`S_D(x)=sum_(n>=2) [Lambda(n)^2/n] min(n/x,x/n)^2`,

and

`C_Lambda=sum_(n>=2) Lambda(n)^2/n^3`.

Thus a fixed-interior physical-source packet does not create a new coefficient-scale mechanism. It applies a bounded linear functional to the already established diagonal profile `Q_gamma`. In particular, if the packet is Laplace-null,

`integral_K h_T(q)e^(-4*pi q)dq=0`,

then

`(2*pi/(H L)) W_I(g_T)`
` = (4*pi/L^2) integral_K h_T(q)Q_gamma(e^(2*pi q))dq + o(L^-2).`

There is also a sharp qualitative localization control. Put

`w_0(q)=e^(-4*pi q)`,

`R(q)=Q_gamma(e^(2*pi q))/w_0(q)=e^(4*pi q)Q_gamma(e^(2*pi q)).`

On every fixed compact `K`, `R` is Lipschitz. If a Laplace-null packet `h` is supported in an interval `J subset K` of diameter `b`, then

`| integral_J h(q)Q_gamma(e^(2*pi q))dq |`
` <= C_K b ||h||_1.`

Consequently a Laplace-null packet whose support shrinks inside a fixed source interval and whose `L^1` norm remains bounded has a coefficient-scale arithmetic projection tending to zero. To keep a non-vanishing localized projection as `b->0`, its total variation must grow at least on the order of `1/b` along any sequence on which the projection stays bounded away from zero.

Any apparent amplification obtained by increasingly narrow Laplace-null packets in the fixed-interior regime is therefore inseparable from packet conditioning: the same diverging `L^1` norm also amplifies whatever remainder accompanies the fixed-source profile. A genuine source-threshold or off-compact gain must be sought by leaving this fixed-interior bounded-projection regime, not by reinterpreting packet localization itself as new arithmetic information.

**Evidence/status:** `EXACT-DERIVED + LITERATURE-TRANSFER + BOUNDED-PROJECTION CONTROL + LOCALIZATION/CONDITIONING OBSTRUCTION + NO-NOVELTY-CLAIM`.

No new pair-correlation theorem, new prime-power invariant, source-boundary asymptotic, moving-support theorem, off-critical-strip gain, or RH implication is claimed.

## 1. Exact fixed-source packet projection

Wang's exact Fourier-inversion identity is

`W_I(g)=2 integral_0^lambda g(alpha) F_I(T^alpha)d alpha`

for real even tests supported inside the fixed Wang margin. With

`q=L alpha/(2*pi)`, `d alpha=(2*pi/L)dq`,

and `g_T(alpha)=h_T(q)`, this becomes

`W_I(g_T)=(4*pi/L) integral_K h_T(q)F_I(e^(2*pi q))dq.`

The support of every `h_T` stays in the same compact `K`, so the source parameter `x=e^(2*pi q)` remains in one fixed compact subset of `(1,infinity)`.

`VIS-283`, using Wang's explicit-formula decomposition and the sharpenings in `VIS-278`–`VIS-282`, gives uniformly on such compact source sets

`(1/H) integral_I |A(x,t)|^2 dt`
` = x^-2 ell_T^2 + Q_gamma(x) + o_K(1).`

Wang's Lemma 2.4 gives

`2*pi F_I(x)=integral_I |A(x,t)|^2dt + O(xL^3).`

At fixed source the localization remainder divided by `H` is `O_K(L^3/H)=o(L^-m)` for every fixed `m`, as recorded in `VIS-281`. Hence uniformly for `q in K`,

`F_I(e^(2*pi q))/H`
` = (1/(2*pi))[e^(-4*pi q)ell_T^2 + Q_gamma(e^(2*pi q)) + o_K(1)].`

Substitution into the exact packet identity yields

`(2*pi/(HL))W_I(g_T)`
` = (4*pi/L^2) integral_K h_T(q)`
`     [e^(-4*pi q)ell_T^2 + Q_gamma(e^(2*pi q)) + o_K(1)]dq.`

Because `sup_T ||h_T||_1<infinity`, the uniform `o_K(1)` remainder integrates to `o(L^-2)`. This proves the displayed projection formula without invoking the generic moving-test derivative estimate from `VIS-266`.

That distinction matters. The test may narrow in the `q` coordinate while its derivative in the original `alpha` coordinate becomes large; the present result never Taylor-collapses the fixed-source layer. It first obtains a uniform pointwise fixed-source asymptotic and only then applies the packet as a bounded linear functional.

## 2. Laplace-null packets expose the exact `L^-2` profile

The universal fixed-source mode in `VIS-274` is precisely

`w_0(q)=e^(-4*pi q)`.

If

`<h_T,w_0>=0`,

the complete gamma-baseline term in the projection formula vanishes, not merely its leading `L->infinity` approximation. The remaining coefficient-scale term is therefore

`(4*pi/L^2)<h_T,Q_gamma(e^(2*pi q))>`

up to `o(L^-2)` for every uniformly `L^1`-bounded packet family in the fixed compact source regime.

For a fixed packet `h`, this identifies an explicit secondary coefficient. It is not a new arithmetic object: `Q_gamma` is the positive diagonal profile already derived in `VIS-283`, and packetization only evaluates it against `h`.

More generally,

`|<h_T,Q_gamma(e^(2*pi q))>|`
` <= ||h_T||_1 sup_(q in K)|Q_gamma(e^(2*pi q))|.`

Thus any packet family with uniformly bounded total variation produces a uniformly bounded `L^-2` coefficient. Changing packet shape, width, or center inside the same compact source region changes which part of `Q_gamma` is observed but cannot create an `L`-growing gain by itself.

## 3. Shrinking Laplace-null packets pay an inverse-width conditioning price

The stronger localization statement uses only continuity and the exact null constraint.

`VIS-282` shows that `S_D(x)` is continuous and piecewise smooth, with derivative jumps only at prime powers. On a fixed compact `x` interval there are only finitely many such breakpoints and the one-sided derivatives are bounded. Hence `S_D` is Lipschitz there. The same is true of

`Q_gamma(x)=S_D(x)+C_Lambda/x^2`

and therefore of

`R(q)=e^(4*pi q)Q_gamma(e^(2*pi q))`

on the fixed compact `K`.

Let `h` be Laplace-null and supported in an interval `J subset K` of diameter `b`. For any `q_0 in J`,

`integral_J h(q)Q_gamma(e^(2*pi q))dq`
` = integral_J h(q)w_0(q)[R(q)-R(q_0)]dq,`

because

`R(q_0) integral_J h(q)w_0(q)dq=0.`

If `Lip_K(R)` is a Lipschitz constant, then

`|R(q)-R(q_0)| <= Lip_K(R)b`

on `J`. Since `w_0` is bounded on `K`,

`|<h,Q_gamma>| <= ||w_0||_(infinity,K) Lip_K(R)b ||h||_1.`

This is the claimed bound.

It has a direct interpretation. A bounded-total-variation Laplace-null packet cannot become both arbitrarily localized and retain a nonzero response to the fixed-source diagonal profile. If a sequence with support diameter `b_j->0` satisfies

`|<h_j,Q_gamma>| >= c>0`,

then necessarily

`||h_j||_1 >= c/(C_K b_j).`

The apparent localization gain has therefore been purchased by an ill-conditioned signed packet. The result does not forbid such a design, but it makes its price explicit.

## 4. Why this is not another Wang seminorm obstruction

`VIS-266` and `VIS-267` study a different interface: how rapidly a moving test may vary while remaining controlled by Wang's theorem-level seminorm estimate after the concentrated main term has been reduced to the usual fixed-test form.

The present result stays inside the fixed-source representation introduced in `VIS-274`. It retains the complete source layer and uses the uniform compact-source expansion before packet integration. For uniformly `L^1`-bounded packet families, no derivative norm appears in the coefficient projection.

The new obstruction is instead intrinsic to **signed localization after the universal Laplace mode has been nulled**. A narrow packet with bounded total variation loses sensitivity to any Lipschitz residual profile. Preserving a finite response forces total variation to diverge, and once it diverges the uniform `o_K(1)` field-energy remainder can no longer automatically be integrated as `o(1)` without a correspondingly quantitative rate.

Thus narrowing can still be attempted, but its conditioning must be charged explicitly. It cannot be described as free source resolution.

## 5. Prior art and novelty boundary

The external analytic source is Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026), especially Theorem 2.2, Lemma 2.4, Proposition 2.6, and the exact Fourier-inversion identity in equation (2.22). At the time of this audit the arXiv record still lists only version 1, submitted 7 September 2026.

Wang supplies the pair-correlation identity and explicit-formula estimates. `VIS-274` supplies the fixed-source rescaling, and `VIS-278`–`VIS-283` supply the exact compact-source diagonal decomposition used here.

Boundedness of integration against an `L^1` test, Lipschitz control on compact intervals, and the inverse-width conditioning consequence of a vanishing weighted moment are elementary analysis. No novelty is claimed for those ingredients or for approximate-identity reasoning.

The durable Mathia content is the composition of those facts at the exact unresolved interface left by `VIS-283`: it identifies what packet localization can and cannot change once the fixed-source arithmetic profile has already been isolated.

## 6. Boundaries and falsification

The asymptotic projection formula requires source support inside one fixed compact `K subset (0,infinity)` and uniformly bounded `||h_T||_1`. It does not cover packets whose support approaches `q=0`, whose center escapes to growing `q`, or whose total variation diverges.

The inverse-width inequality itself remains valid for any individual Laplace-null packet supported in `K`, including packets with large total variation, but using such a family in the pair-correlation asymptotic requires a quantitative remainder strong enough to survive that amplification.

The finding also keeps the gamma baseline intact. Expanding `ell_T^2=(L-log(2*pi))^2` merely redistributes classical normalization terms and does not alter the Laplace-null conclusion.

A future source-boundary asymptotic could reveal a genuine singular mechanism outside the present compact regime. Such a result would not contradict this finding; it would cross exactly the boundary isolated here. Likewise a non-Lipschitz residual profile on a different source scaling would invalidate the inverse-width argument for that representation and should be analyzed separately.

No untouched confirmation-zero data, numerical fitting, or visual salience is used.

## Dependencies

- `VIS-274`: exact fixed-source rescaling and universal Laplace mode.
- `VIS-281`: fixed-source zero-window localization is power-small.
- `VIS-282`: exact fixed-source Dirichlet diagonal profile and its prime-power kinks.
- `VIS-283`: recombination leaves the positive diagonal profile `Q_gamma` and a power-small signed cross.

## Research consequence

The fixed-interior half of `CLUE-wang-fixed-source-packet-localization` is resolved. Every uniformly `L^1`-bounded packet supported in a fixed physical-source compact set sees the `L^-2` arithmetic sector only through the bounded linear projection

`h -> <h,Q_gamma(e^(2*pi q))>.`

After the universal Laplace mode is nulled, shrinking support does not generate extra arithmetic sensitivity: with bounded total variation the response vanishes at least linearly in the packet diameter, while a non-vanishing localized response requires inverse-width conditioning and therefore amplifies unresolved remainders as well.

The remaining live question is genuinely different and should be treated as the next thread: what happens when the packet approaches a source boundary, leaves the compact fixed-source regime, or adopts a singular normalization for which the bounded-projection argument no longer applies. Any claimed source-threshold or off-critical-strip gain must be demonstrated there rather than attributed to ordinary fixed-interior packet localization.
