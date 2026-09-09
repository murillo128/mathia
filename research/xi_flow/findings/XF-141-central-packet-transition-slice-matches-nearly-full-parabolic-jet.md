# XF-141 — central packet transition slice matches a nearly full parabolic heat jet

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE/INSTANTANEOUS-JET-OBSERVABILITY` + `MATCHED-CONTROL` + `UNIT-CIRCLE-ADMISSIBLE` + `CROSS-SCALE` + `MIXED-SPACE-TIME-JET`. XF-134--XF-140 show that complete future local heat data can be exponentially transition-blind even after adding increasingly deep spatial logarithmic jets. A natural remaining repair is to use time derivatives at the observation slice as additional coordinates. For the same central packet, that repair fails much more sharply than the future-history estimates suggest: a quadratic number of mixed space-time jet coordinates can agree **exactly** while the periodic transition times differ by any prescribed finite amount.

## Result / observations

Let `N=2M`, choose any `1<=r<M`, and use the XF-133 packet

\[
\Delta E(w)=
(-1)^M c_0w^M
+
\frac12\sum_{j=1}^r(-1)^{M-j}c_j
(w^{M-j}+w^{M+j}),
\tag{1}
\]

where `c_j=omega_j/W_r` and

\[
\omega_0=\frac{(-1)^r}{(r!)^2},
\qquad
\omega_j=\frac{2(-1)^{r-j}}{(r-j)!(r+j)!}
\quad(1\le j\le r).
\tag{2}
\]

Write

\[
H_r:=\sum_{j=0}^r|c_j|,
\qquad
t_*:=-\frac{2(-1)^{M+r}}{H_r},
\tag{3}
\]

as in XF-134, and consider the amplitude family

\[
E_\lambda(w,s)
:=1+w^{2M}+\lambda t_*\Delta E(w,s),
\qquad 0<\lambda\le1,
\tag{4}
\]

under the exact coefficient heat flow

\[
E_k(s)=E_k(0)e^{-a k(2M-k)s},
\qquad a>0.
\tag{5}
\]

Use the XF-133 local coordinate

\[
\zeta_{\beta,N}:=-e^{\beta/N},
\qquad
Q_\lambda(\beta,s):=E_\lambda(\zeta_{\beta,N},s).
\tag{6}
\]

Then for every `rho>=0` there is a unique amplitude `lambda_(r,rho) in (0,1]` such that

\[
\boxed{
\Lambda_{\rm per}(E_1)=0,
\qquad
\Lambda_{\rm per}(E_{\lambda_{r,\rho}})=-\rho,
}
\tag{7}
\]

but at the common observation slice `s=0`,

\[
\boxed{
\partial_s^p\partial_\beta^q
Q_1(0,0)
=
\partial_s^p\partial_\beta^q
Q_{\lambda_{r,\rho}}(0,0)
\quad\text{whenever}\quad
2p+q<2r.
}
\tag{8}
\]

The same exact equality holds with `Q` replaced by `log Q`, using the local analytic logarithm at `Q(0,0)=2`, and therefore also after division by any common nonvanishing analytic reference.

Taking the maximal admissible packet depth

\[
r=M-1
\tag{9}
\]

gives exact transition blindness for every mixed derivative satisfying

\[
\boxed{
2p+q<N-2.
}
\tag{10}
\]

The number of jet coordinates in `(10)`, including the value coordinate, is exactly

\[
\sum_{p=0}^{r-1}2(r-p)
=r(r+1)
=M(M-1)
=
\boxed{\frac{N^2}{4}-\frac N2}.
\tag{11}
\]

Thus almost a quarter of the full `N x N` mixed derivative grid can be exactly identical between controls whose transition times differ by an arbitrary prescribed finite `rho`. This is exact non-identifiability of an **instantaneous mixed heat jet**, not merely exponential ill-conditioning.

## Derivation

Set `x=as`. XF-133 gives the exact packet trace

\[
\Delta Q_\beta(s)
=
e^{\beta/2}e^{-M^2x}
\frac1{W_r}
\sum_{j=0}^r
\omega_j e^{j^2x}
\cosh\!\left(\frac{\beta j}{N}\right).
\tag{12}
\]

The barycentric weights in `(2)` have two elementary exact identities. First, extending the coefficient symmetrically to `-r<=j<=r`,

\[
\sum_{j=0}^r\omega_j\cos(jt)
=
\frac{(-4)^r}{(2r)!}\sin^{2r}\!\left(\frac t2\right).
\tag{13}
\]

Indeed, with `k=r-j`, the two-sided sum is simply

\[
\frac{e^{irt}}{(2r)!}
(1-e^{-it})^{2r}.
\tag{14}
\]

Second, taking absolute values of the same binomial coefficients gives

\[
\boxed{
\sum_{j=0}^r|\omega_j|
=\frac{4^r}{(2r)!}.
}
\tag{15}
\]

Substituting `t=i beta/N` into `(13)` and using `H_rW_r=sum|omega_j|` therefore yields the exact transition-slice formula

\[
\boxed{
t_*\Delta Q_\beta(0)
=-2(-1)^{M+r}e^{\beta/2}
\sinh^{2r}\!\left(\frac{\beta}{2N}\right).
}
\tag{16}
\]

So the packet is already spatially flat to order `2r-1` at the observation center `beta=0`. The stronger mixed statement follows from the full two-variable series. Expanding `(12)` before the harmless nonvanishing factors gives

\[
\sum_{j=0}^r\omega_j e^{j^2x}
\cosh\!\left(\frac{\beta j}{N}\right)
=
\sum_{m,n\ge0}
\frac{x^m}{m!}
\frac{(\beta/N)^{2n}}{(2n)!}
\left(\sum_{j=0}^r\omega_jj^{2(m+n)}\right).
\tag{17}
\]

Because these are the order-`r` barycentric weights on the nodes `0^2,1^2,...,r^2`,

\[
\sum_{j=0}^r\omega_jj^{2\ell}=0
\quad(0\le\ell<r),
\qquad
\sum_{j=0}^r\omega_jj^{2r}=1.
\tag{18}
\]

Every monomial in `(17)` therefore has `m+n>=r`. Multiplication by `e^(beta/2-M^2x)` can only increase the weighted degree in which `x` has weight `1` and `beta` has weight `1/2`. Hence

\[
\partial_x^p\partial_\beta^q
\Delta Q_\beta(s)\big|_{(x,\beta)=(0,0)}=0
\quad\text{for}\quad
p+\frac q2<r,
\tag{19}
\]

which is `(8)` after `partial_s^p=a^p partial_x^p`.

The threshold is also sharp for this packet. On the boundary `p+n=r`,

\[
\partial_x^p\partial_\beta^{2n}
(t_*\Delta Q)(0,0)
=
-2(-1)^{M+r}\frac{(2r)!}{4^r}N^{-2n}
\ne0.
\tag{20}
\]

Thus the exact cancellation is not an artifact of a loose estimate: the first nonzero parabolic layer is precisely `2p+q=2r`.

It remains to show that the amplitude parameter can encode an arbitrary transition shift without changing any of the vanished jets. Center the unit-circle restriction as in XF-134,

\[
F_\lambda(\theta,s)
:=e^{-iM\theta}E_\lambda(e^{i\theta},s)
=
2\cos(M\theta)
-
\frac{2\lambda}{H_r}
\sum_{j=0}^r
|c_j|e^{-a(M^2-j^2)s}\cos(j\theta).
\tag{21}
\]

Define

\[
\mathcal A_r(s)
:=
\frac1{H_r}
\sum_{j=0}^r
|c_j|e^{-a(M^2-j^2)s}.
\tag{22}
\]

Since `r<M`, every rate in `(22)` is strictly positive. Therefore `A_r` is strictly decreasing, `A_r(0)=1`, and `A_r(s)->infinity` as `s->-infinity`. For a prescribed `rho>=0`, choose

\[
\boxed{
\lambda_{r,\rho}:=\mathcal A_r(-\rho)^{-1}.
}
\tag{23}
\]

Then `0<lambda_(r,rho)<=1`, and `F_lambda(0,-rho)=0`. For `s>-rho`,

\[
\lambda_{r,\rho}\mathcal A_r(s)<1,
\tag{24}
\]

so the perturbation in `(21)` has absolute value strictly below `2`. At the `2M` extrema `theta_k=k pi/M`, the leading term is `2(-1)^k`; sign alternation therefore places exactly one simple unit-circle root in every interval between consecutive extrema. Hence all `2M` roots are simple and on the unit circle for every `s>-rho`.

At `s=-rho`, the root at `theta=0` is exactly double because

\[
\begin{aligned}
\partial_\theta^2F_\lambda(0,-\rho)
&=-2M^2+
\frac{2\lambda}{H_r}
\sum_{j=1}^rj^2|c_j|e^{-a(M^2-j^2)(-\rho)}\\
&\le -2(M^2-r^2)<0.
\end{aligned}
\tag{25}
\]

The centered heat PDE from XF-134,

\[
\partial_sF_\lambda
=-a(M^2+\partial_\theta^2)F_\lambda,
\tag{26}
\]

then gives `partial_s F_lambda(0,-rho)>0`. The local branches satisfy

\[
\theta_\pm(s)^2
=2a(s+\rho)+O((s+\rho)^2),
\tag{27}
\]

so immediately before `-rho` the pair leaves the unit circle. This proves `(7)`.

Finally, `Q_lambda(0,0)=2` for every `lambda`, by `(16)`. Since `Q_1-Q_lambda` has no monomial of parabolic weight below `r`, analytic composition with `log` preserves that vanishing order. This proves the logarithmic-jet and common-reference statements.

## Checks / falsifier

The algebra has two direct low-order checks. For `r=1`, `(2)` gives `omega=(-1,1)` and `(13)` becomes `-1+cos t=-2 sin^2(t/2)`. For `r=2`, the weights are `(1/4,-1/3,1/12)`, their zeroth and second moments vanish, and their fourth moment equals `1`, exactly as `(18)` requires. A numerical root check at `M=3`, `r=2`, `a=1`, `rho=0.2` gives `lambda_(r,rho)=0.196659957...`: all six roots have modulus `1` at `s=0`, `w=1` becomes double at `s=-0.2`, and at `s=-0.21` the colliding pair has moduli approximately `0.86614` and `1.15455`.

A clean falsifier for the main statement would be any pair `(p,q)` with `2p+q<2r` for which the mixed packet derivative at `(0,0)` is nonzero. Equation `(17)`--`(18)` excludes this coefficientwise. Conversely `(20)` supplies nonzero derivatives on every even boundary point `2p+q=2r`, so the claimed anisotropic threshold is exact rather than merely sufficient.

## Relation to prior work

XF-132 introduced the quadratic-node barycentric cancellation as a temporal spectral-conditioning obstruction. XF-133 turned the same weights into a probe-independent central packet; XF-134 scaled that packet to a transition-sharp unit-circle collision; XF-135--XF-140 then quantified how much of the complete future logarithmic spatial jet can remain exponentially blind. XF-141 uses a different feature of exactly the same packet: before any Cauchy estimate, its two-variable Taylor series has a hard algebraic gap `m+n<r`. This turns **time derivatives at one slice** into exact null coordinates rather than merely poorly conditioned coordinates.

The distinction from XF-006 is also essential. XF-006 shows that any *fixed finite* collision jet at the collision point can be approximated by real-rooted polynomial controls. Here the equality is exact, the number of coordinates grows quadratically with degree, the observation point is the remote `w=-1` / `beta=0` center rather than the collision at `w=1`, and the two periodic controls can be chosen to have transition times separated by any prescribed `rho`.

The result does not weaken XF-130's algebraic identifiability from a complete off-circle heat trace. Nor does it contradict the complete-future estimates of XF-134--XF-140. A genuine positive-time interval sees the divided-difference packet unfold after its high-order contact at `s=0`; a finite but very deep time Taylor jet at one instant is not equivalent to that interval with degree-uniform conditioning.

## Implications

An instantaneous local criterion cannot be repaired merely by appending more heat derivatives to more spatial derivatives. In the periodic matched-control class, even the anisotropic jet containing every coordinate with `2p+q<N-2` can be exactly identical while `Lambda_per` changes by an arbitrary finite amount. The natural parabolic weighting is forced by the heat spectrum itself: one time derivative consumes the same cancellation order as two spatial derivatives.

This sharpens the next positive gate. A viable source-faithful Xi mechanism must use information that escapes this finite-order Taylor ideal: a genuinely positive heat-time interval, spatial data reaching a different center/shell, a nonlocal transform, or an Xi-specific theorem excluding the central packet. In particular, a Gaussian/reference quotient does not by itself help at one slice, because the common reference cancels after logarithmic differentiation.

## Uncertainties / scope

This is a target-side periodic matched-control theorem. It does **not** show that the actual Xi source can realize the packet, and it does not rule out a source-specific relation among mixed derivatives. The exact jet equality is centered at `beta=0` (`w=-1`), opposite the collision point `w=1`; simultaneous access to a second center, to the collision neighborhood itself, or to a positive interval of heat times lies outside the theorem.

For fixed positive `rho`, the retuned amplitude `lambda_(r,rho)` can be exponentially small in the degree because the central heat rates are of order `M^2`. That does not affect exact jet equality or unit-circle admissibility, but it matters if a future source theorem imposes lower bounds on the relevant coefficient direction. The result should therefore be used as an instantaneous-observability obstruction, not as evidence that Xi itself has such an amplitude family.

## Source audit

A directed prior-art audit checked classical symmetric/central finite differences and divided differences. The identity behind `(13)` is the standard binomial central-difference mechanism: the order-`n` symmetric difference is an alternating binomial sum, and its exponential generating symbol is a power of a sine/sinh factor. Hermite--Genocchi theory supplies the familiar interpolation context for the barycentric moment cancellation used in XF-132--XF-133. These are classical ingredients, but no external theorem is load-bearing here: `(13)` is proved directly by the binomial theorem, `(18)` is the defining exactness of the canonical barycentric weights already established in the line, and the transition argument is the internal XF-134 sign-alternation/PDE argument with an amplitude parameter.

The audit did not locate the specific combination of a transition-sharp unit-circle heat family, arbitrary finite transition retuning, and exact `Theta(N^2)` mixed-jet equality at a remote observation center. No new external dependency is therefore added to `SOURCES.md`.
