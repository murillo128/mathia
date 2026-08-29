# PC-040 — prime-cover Weil–Petersson weights are universal holonomy samples

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-REDIRECTION`; no RH claim. The exact roots-of-unity moduli point, its cyclic eigendifferentials, and Weil–Petersson invariance under the finite automorphism are classical and appear explicitly in Lochak. The prime-circle-specific contribution here is the exact pushdown of the complete Petersson weight system to one universal holonomy family on the thrice-punctured sphere, together with the resulting intrinsic `alpha <-> 1-alpha` center.

PC-030 left symmetric second-order / Weil–Petersson geometry as one of the principal surviving sectors of the nonlinear uniformization branch. At prime level that sector is especially clean because the anchored birth surface is the full cyclic cover

\[
Y_p=\widehat{\mathbb C}\setminus\bigl(\{0,\infty\}\cup\mu_p\bigr)
\xrightarrow{\;w=z^p\;}
B=\widehat{\mathbb C}\setminus\{0,1,\infty\}.
\]

The result below shows that the Weil–Petersson metric at this highly symmetric point is not an unexplained `(p-1)`-dimensional arithmetic object. In its canonical cyclic eigenbasis, all diagonal Petersson weights are rational samples of one positive function of a continuous unitary holonomy parameter on the fixed base `B`.

## 1. The complete cotangent space is the nontrivial cyclic-character sector

The Teichmüller cotangent space at `Y_p` is the space `Q(Y_p)` of integrable holomorphic quadratic differentials, equivalently meromorphic quadratic differentials on the sphere with at most simple poles at the `p+2` punctures. Hence

\[
\dim_{\mathbb C}Q(Y_p)=p-1.
\]

For `1 <= k <= p-1`, define

\[
\boxed{
q_{p,k}(z)
:=\frac{z^{k-2}}{z^p-1}\,dz^2.
}
\]

At a root of unity the denominator has a simple zero; at `0` only `k=1` has a simple pole; and in the coordinate `u=1/z` the worst case `k=p-1` has a simple pole at infinity. Thus every `q_{p,k}` lies in `Q(Y_p)`.

Let

\[
T(z)=\zeta_p z
\]

be a generator of the deck group. Then

\[
\boxed{T^*q_{p,k}=\zeta_p^k q_{p,k}.}
\]

The `p-1` characters are distinct, so these differentials form a basis of `Q(Y_p)`. There is no trivial-character cotangent direction: an invariant quadratic differential would descend to `B`, but `Q(B)=0` because `M_{0,3}` is rigid.

For prime `p`, every nontrivial character has exact order `p`. Thus the whole moduli cotangent space at the prime birth configuration is a finite-dimensional analogue of the exact-order spectral birth sector in PC-022.

This character decomposition is not historically new. Lochak studies exactly the special roots-of-unity point `(0,1,zeta,...,zeta^{r-1},infinity)` in `M_{0,r+2}`, writes the standard rational basis of quadratic differentials, and observes that rotation diagonalizes it; he also explicitly notes that the finite automorphism acts isometrically for the Weil–Petersson scalar product.

## 2. Cyclic symmetry makes the Weil–Petersson form diagonal

Let `rho_p(z)|dz|` be the complete curvature `-1` hyperbolic metric on `Y_p`. Under the standard Petersson convention on cotangent vectors,

\[
\langle q,r\rangle_{WP,*}
=
\int_{Y_p}
\frac{\phi_q(z)\overline{\phi_r(z)}}{\rho_p(z)^2}\,dA(z),
\qquad q=\phi_q(z)dz^2.
\]

Any alternate standard normalization changes all weights below by one common constant and does not affect the conclusions.

Because `T` is a conformal automorphism of the complete hyperbolic surface, it is an isometry for the Petersson pairing. Therefore

\[
\langle q_{p,k},q_{p,l}\rangle
=
\zeta_p^{k-l}\langle q_{p,k},q_{p,l}\rangle.
\]

Hence

\[
\boxed{
\langle q_{p,k},q_{p,l}\rangle_{WP,*}=0
\qquad(k\ne l).
}
\]

So the only remaining information is the positive diagonal weight

\[
h_{p,k}:=\|q_{p,k}\|_{WP,*}^2.
\]

## 3. Exact pushdown: every weight is a sample of one universal function

Since `w=z^p:Y_p->B` is an unbranched hyperbolic covering, the complete metric on `Y_p` is exactly the pullback of the complete metric `rho_B(w)|dw|` on `B`.

Put

\[
\alpha=\frac{k}{p}\in(0,1).
\]

On a local inverse branch of `w=z^p`,

\[
dz=\frac1p z^{1-p}dw,
\]

and therefore

\[
\begin{aligned}
q_{p,k}
&=\frac{z^{k-2}}{w-1}\frac{z^{2-2p}}{p^2}dw^2\\
&=\boxed{
\frac1{p^2}\frac{w^{\alpha-2}}{w-1}\,dw^2
}.
\end{aligned}
\]

The fractional power is not a single-valued scalar differential on `B`; it is naturally a quadratic differential valued in the unitary flat line bundle whose monodromy around `0` is `e^{2 pi i alpha}` and around infinity is its inverse. Its modulus is single-valued.

There are `p` sheets, all with the same modulus. Consequently

\[
\boxed{
h_{p,k}=p^{-3}I\!\left(\frac{k}{p}\right),
}
\]

where the entire level-independent analytic content is

\[
\boxed{
I(\alpha)
:=
\int_B
\frac{|w|^{2\alpha-4}}{|1-w|^2\rho_B(w)^2}\,dA(w),
\qquad 0<\alpha<1.
}
\]

The endpoint restrictions are exactly those required for integrability at the cusps `0` and infinity. The cusp at `1` is harmless because the inverse hyperbolic density cancels the apparent simple-pole square strongly enough for integrability.

Thus

\[
\boxed{
\{h_{p,k}:1\le k\le p-1\}
=
\left\{p^{-3}I(k/p):1\le k\le p-1\right\}.
}
\]

Prime dependence enters only through the elementary global factor `p^{-3}` and through sampling the same universal holonomy profile at the primitive `p`-torsion points of `R/Z`.

## 4. The half point is intrinsic here, but it is a character-duality center

The involution

\[
M(w)=1/w
\]

is an automorphism of the thrice-punctured sphere exchanging `0` and infinity. A direct pullback gives, up to sign,

\[
M^*\left(
\frac{w^{(1-\alpha)-2}}{w-1}dw^2
\right)
=
-\frac{w^{\alpha-2}}{w-1}dw^2.
\]

Since `M` preserves the complete hyperbolic metric,

\[
\boxed{I(\alpha)=I(1-\alpha).}
\]

This is stronger conceptually than the arbitrary re-centering warning in PC-029: `alpha` is already a canonical holonomy coordinate in `R/Z`, and complex-conjugate / inverse characters are intrinsically paired by

\[
\alpha\longleftrightarrow1-\alpha.
\]

The fixed nontrivial unitary character is therefore genuinely at `alpha=1/2`.

There is also an exact convexity statement. Define the finite positive measure

\[
d\nu(w)
:=
\frac{|w|^{-3}}{|1-w|^2\rho_B(w)^2}\,dA(w).
\]

Then

\[
I(1/2+t)=\int_B e^{2t\log|w|}\,d\nu(w).
\]

Inversion preserves `nu` and sends `log|w|` to its negative. Hence the function is even in `t`; Holder's inequality makes `log I(1/2+t)` convex, and it is strictly convex because `log|w|` is not almost surely constant. Therefore

\[
\boxed{
I(\alpha)>I(1/2)
\quad\text{for }\alpha\ne1/2,
}
\]

and for odd prime `p` the smallest sampled cotangent weights occur at the conjugate pair

\[
k=\frac{p-1}{2},\qquad k=\frac{p+1}{2}.
\]

So a genuine `1/2` does emerge from this second-order geometry, but it is the self-dual point of a unitary-character interval, not yet the real part of a complex zeta spectral parameter.

## 5. Research consequence: a useful structure, but not an RH bridge by itself

This calculation both narrows and sharpens the open sector left by PC-030.

What is nontrivial:

- the complete prime-level Weil–Petersson cotangent metric is diagonal in the exact-order cyclic character basis;
- all its diagonal weights are controlled by one universal positive function `I(alpha)` on the fixed thrice-punctured base;
- inversion gives an intrinsic, non-arbitrarily shifted center at `alpha=1/2`;
- positivity gives strict log-convexity and a canonical central extremum.

What this does **not** supply:

- no complex variable `s` has appeared;
- there is no zero set, functional equation of a completed zeta function, or gamma factor;
- `alpha=1/2` is a holonomy self-duality point, not an identification with `Re(s)=1/2`;
- the `p`-dependence is universal rational sampling, not a newly generated prime-specific analytic kernel.

Thus it would be circular to declare the central holonomy point to be the Riemann critical line merely because both contain `1/2`. A substantive continuation would need a **forced coupling between the holonomy parameter `alpha` and an independent spectral/Mellin variable**, or an interaction among levels that is not recoverable from sampling `I`.

Conversely, this is not a complete no-go for the WP branch: the universal function `I(alpha)` itself is a genuine hyperbolic/Petersson object, and the present derivation does not evaluate its analytic continuation or prove that every nonlinear functional of the sampled weights is classical. The result is best treated as a prior-art redirection and a precise boundary, not as an RH claim.

## 6. Prior-art audit

The strongest direct prior-art hit is:

- Pierre Lochak, *On arithmetic curves in the moduli spaces of curves*, Journal of the Institute of Mathematics of Jussieu **4**:3 (2005), 443–508, DOI `10.1017/S1474748005000101`.

Lochak explicitly identifies the roots-of-unity configuration with `0` and infinity as a maximal cyclic special point in genus-zero moduli, writes a basis `q_j=z^j dz^2/P(z)` of the cotangent space, diagonalizes the rotation action on those differentials, and notes that finite automorphisms act isometrically for the Weil–Petersson scalar product. Under `P(z)=z(z^p-1)`, his basis is exactly the basis above after the index shift `k=j+1`.

Therefore neither the cyclic eigenspace decomposition nor the observation that Weil–Petersson respects it should be presented as new. PC-022 already supplies the parallel decomposition of the full automorphic `L^2` spectrum into the same rational holonomy family on `B`.

Directed searches for the combination of this roots-of-unity special point with an explicit pushdown formula for the Petersson norms `h_{p,k}=p^{-3}I(k/p)` and the resulting strict `alpha <-> 1-alpha` convexity did not locate a source stating that exact package. Absence in search is not evidence of historical priority; the pushdown is elementary once the cyclic cover and quadratic-differential basis are written down.

The durable value is therefore the research classification:

\[
\boxed{
\text{prime-level WP second-order weights}
=
\text{universal flat-holonomy profile on }B
\text{ sampled at }k/p.
}
\]

## 7. Audit and falsification tests

The exact claims can be checked independently as follows:

1. verify that each `q_{p,k}` has at most simple poles at `0`, infinity and `mu_p`, and that the `p-1` distinct deck characters exhaust `Q(Y_p)`;
2. apply deck invariance of the Petersson pairing to verify off-diagonal orthogonality;
3. substitute `w=z^p` and check the coefficient `p^{-2}w^{k/p-2}/(w-1)`;
4. account for the `p` sheets to recover the exact `p^{-3}` norm factor;
5. pull the local-system differential through `w -> 1/w` to verify `I(alpha)=I(1-alpha)`;
6. apply Holder to the moment-generating representation at `alpha=1/2` to verify strict log-convexity.

A failure of the `p^{-3}` pushdown or the inversion identity would invalidate the main new derivation. No claim is made that `I(alpha)` is historically new, that it has Riemann zeros, or that the holonomy midpoint solves any part of RH.
