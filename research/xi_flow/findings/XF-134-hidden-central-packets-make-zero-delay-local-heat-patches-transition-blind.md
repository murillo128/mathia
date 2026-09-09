# XF-134 — hidden central packets make zero-delay local heat patches transition-blind

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE/TRANSITION-CONDITIONING` + `MATCHED-CONTROL` + `ZERO-DELAY` + `LOCAL-PATCH-OBSERVABILITY` + `UNIT-CIRCLE-ADMISSIBLE` + `CROSS-SCALE`. XF-132 and XF-133 show that complete zero-delay future heat data can be exponentially insensitive to admissible central coefficient directions, even when the observation consists of a continuum complex patch. Their explicit boundary was that this proved ill-conditioning of full-state tomography, not of the periodic Newman transition time itself. The same XF-133 central packet can in fact be scaled all the way to a nondegenerate collision while retaining the exponential patch invisibility.

Let `N=2M`, let `1<=r<M`, and use the XF-067 coefficient heat flow

\[
E(w,s)=\sum_{k=0}^{2M} E_k e^{-a k(2M-k)s}w^k,
\qquad a>0.
\tag{1}
\]

Let `Delta E` be the XF-133 central divided-difference packet built from the barycentric weights on `0^2,1^2,...,r^2`. Then there is an explicit real scalar `t_*` with `|t_*|<=2` such that

\[
E_{\rm c}(w,0):=1+w^{2M}+t_*\Delta E(w)
\tag{2}
\]

has all `2M` roots on the unit circle and has a nondegenerate double root at `w=1`. Its exact heat trajectory satisfies

\[
\boxed{\Lambda_{\rm per}(E_{\rm c})=0.}
\tag{3}
\]

For every `rho>=0`, define the forward-shifted target

\[
E_{{\rm c},\rho}(w,s):=E_{\rm c}(w,s+\rho).
\tag{4}
\]

Then

\[
\boxed{\Lambda_{\rm per}(E_{{\rm c},\rho})=-\rho.}
\tag{5}
\]

Nevertheless, for the whole XF-133 complex probe family

\[
\zeta_{\beta,N}:=-e^{\beta/N},
\qquad |\beta|\le B,
\tag{6}
\]

the two **complete zero-delay future histories** obey

\[
\boxed{
\sup_{s\ge0}\sup_{|\beta|\le B}
\left|
E_{\rm c}(\zeta_{\beta,N},s)
-
E_{{\rm c},\rho}(\zeta_{\beta,N},s)
\right|
\le
4e^B\frac{(r!)^2}{(M^2-r^2)^r}.
}
\tag{7}
\]

The bound is uniform in `rho`. Taking

\[
r=\left\lfloor\frac M3\right\rfloor
\tag{8}
\]

and any fixed `eta>0`, every aperture satisfying

\[
B_N\le\left(\frac{\log2}{2}-\eta\right)N
\tag{9}
\]

therefore gives

\[
\boxed{
\sup_{s\ge0,\ |\beta|\le B_N}
|E_{\rm c}(\zeta_{\beta,N},s)-E_{{\rm c},\rho}(\zeta_{\beta,N},s)|
\le e^{-\eta N+O(1)},
}
\tag{10}
\]

while the transition times differ by exactly `rho`. In the physical XF-067 coordinate `w=-e^{-2 pi i z/L}`, this includes every fixed disk

\[
|z|\le\left(\frac{\log2}{4\pi}-\varepsilon\right)L.
\tag{11}
\]

Thus the caveat in XF-132--XF-133 is real but removable: the exponentially hidden central directions can be chosen **transverse to the discriminant itself**. A direct transition-time decoder from this local heat-patch sup norm is exponentially ill-conditioned even when observation begins at the target slice. Since `rho=rho_N` may be any finite nonnegative sequence, the same patch data do not even provide a degree-uniform compactness bound for `Lambda_per` on this matched-control family.

## 1. The XF-133 packet has a coherent sign on the unit circle

For the quadratic interpolation nodes, XF-132 gives

\[
\omega_0=\frac{(-1)^r}{(r!)^2},
\qquad
\omega_j=
\frac{2(-1)^{r-j}}{(r-j)!(r+j)!}
\quad(1\le j\le r).
\tag{12}
\]

Put

\[
W_r:=\max_j|\omega_j|,
\qquad c_j:=\frac{\omega_j}{W_r}.
\tag{13}
\]

Hence

\[
c_j=(-1)^{r-j}|c_j|,
\qquad
\max_j|c_j|=1.
\tag{14}
\]

The XF-133 perturbation is

\[
\Delta E(w)=
(-1)^M c_0w^M
+
\frac12\sum_{j=1}^r
(-1)^{M-j}c_j
(w^{M-j}+w^{M+j}).
\tag{15}
\]

For `w=e^{i\theta}`, centering by `w^M` and using `(14)` gives the exact identity

\[
\boxed{
e^{-iM\theta}\Delta E(e^{i\theta})
=(-1)^{M+r}g_r(\theta),
}
\tag{16}
\]

where

\[
g_r(\theta):=
|c_0|+\sum_{j=1}^r|c_j|\cos(j\theta).
\tag{17}
\]

Write

\[
H_r:=g_r(0)=\sum_{j=0}^r|c_j|.
\tag{18}
\]

Since some `|c_j|=1`, `H_r>=1`, and by the triangle inequality

\[
|g_r(\theta)|\le H_r
\quad\text{for every real }\theta.
\tag{19}
\]

Choose

\[
\boxed{
t_*:=-\frac{2(-1)^{M+r}}{H_r}.
}
\tag{20}
\]

Then `|t_*|=2/H_r<=2`. This is the finite amplitude at which the locally invisible tangent packet first reaches a controlled collision.

## 2. Sign alternation keeps the whole divisor on the circle up to the collision

Let

\[
F_{\rm c}(\theta,s)
:=e^{-iM\theta}E_{\rm c}(e^{i\theta},s).
\tag{21}
\]

The central shell `M-j` has heat rate `a(M^2-j^2)`, so `(16)`--`(20)` give

\[
\boxed{
F_{\rm c}(\theta,s)
=
2\cos(M\theta)
-
\frac2{H_r}
\sum_{j=0}^r
|c_j|e^{-a(M^2-j^2)s}\cos(j\theta).
}
\tag{22}
\]

At `s=0`, equation `(22)` gives `F_c(0,0)=0`. For every `s>0`, because `j<=r`,

\[
\left|
\frac2{H_r}
\sum_{j=0}^r
|c_j|e^{-a(M^2-j^2)s}\cos(j\theta)
\right|
\le
2e^{-a(M^2-r^2)s}<2.
\tag{23}
\]

At the `2M` extrema

\[
\theta_k=\frac{k\pi}{M},
\tag{24}
\]

the leading term is `2(-1)^k`. The strict bound `(23)` therefore preserves its alternating sign. Every interval `(theta_k,theta_(k+1))` contains a zero of `F_c(.,s)`. There are `2M` such intervals modulo `2 pi`, while `E_c(.,s)` has degree `2M`; hence these are exactly all its roots, each simple and on the unit circle.

Letting `s` decrease to zero shows that all roots of `E_c(.,0)` remain on the unit circle. The root at `theta=0` is exactly double rather than higher order, because

\[
\begin{aligned}
\partial_\theta^2F_{\rm c}(0,0)
&=-2M^2+
\frac2{H_r}\sum_{j=1}^r j^2|c_j|\\
&\le -2(M^2-r^2)<0.
\end{aligned}
\tag{25}
\]

Thus `(2)` lies on a nondegenerate unit-circle discriminant while remaining an `O(1)` multiple of the exponentially hidden XF-133 direction.

## 3. The collision is transition-sharp

The centered heat flow has the exact PDE

\[
\boxed{
\partial_sF_{\rm c}
=-a(M^2+\partial_\theta^2)F_{\rm c}.
}
\tag{26}
\]

At `(theta,s)=(0,0)`, both `F_c` and its first theta derivative vanish, so `(26)` and `(25)` give

\[
\partial_sF_{\rm c}(0,0)
=-a\partial_\theta^2F_{\rm c}(0,0)>0.
\tag{27}
\]

The local even expansion at the double root is therefore

\[
F_{\rm c}(\theta,s)
=
\partial_\theta^2F_{\rm c}(0,0)
\left(\frac{\theta^2}{2}-as\right)
+O(|\theta|^4+|s||\theta|^2+s^2).
\tag{28}
\]

Hence the two local branches satisfy

\[
\theta_\pm(s)^2=2as+O(s^2).
\tag{29}
\]

For `s>0` they split along real `theta`, consistently with the global sign-alternation argument. For `s<0` sufficiently close to zero they form a nonreal conjugate pair in the `theta` coordinate, and therefore their `w=e^{i theta}` images leave the unit circle. Since all roots are on the circle for every `s>=0`, this proves `(3)` without importing a separate root-preservation theorem.

Time translation now gives `(5)` immediately. For `rho>0`, the target `E_(c,rho)(.,0)=E_c(.,rho)` lies in the strict regime `(23)`, so all its roots are simple and unit-circle-rooted; at `s=-rho` it reaches the same nondegenerate collision, and immediately before that time it has off-circle roots.

## 4. The transition-sharp pair inherits the complete XF-133 patch invisibility

The endpoint coefficients `1` and `w^(2M)` have zero heat rate, so if

\[
\Delta Q_\beta(s):=
\Delta E(\zeta_{\beta,N},s),
\tag{30}
\]

then

\[
\begin{aligned}
E_{\rm c}(\zeta_{\beta,N},s)
&=1+\zeta_{\beta,N}^{2M}+t_*\Delta Q_\beta(s),\\
E_{{\rm c},\rho}(\zeta_{\beta,N},s)
&=1+\zeta_{\beta,N}^{2M}+t_*\Delta Q_\beta(s+\rho).
\end{aligned}
\tag{31}
\]

XF-133 proves, simultaneously for every `s>=0` and every complex `|beta|<=B`,

\[
|\Delta Q_\beta(s)|
\le
e^B\frac{(r!)^2}{(M^2-r^2)^r}.
\tag{32}
\]

Therefore `(31)`, the triangle inequality, and `|t_*|<=2` give `(7)`. The estimate does not deteriorate when `rho` grows because both arguments `s` and `s+rho` remain inside the same uniform future-history bound.

For `r=floor(M/3)`, XF-133 gives

\[
\frac{(r!)^2}{(M^2-r^2)^r}
\le 8^{-r}
=
\exp\left(-\frac{\log2}{2}N+O(1)\right),
\tag{33}
\]

which proves `(9)`--`(10)`. The physical patch `(11)` is the same coordinate conversion as XF-133.

## 5. Exact transition-time conditioning lower bound

Let `Obs_N(E)` denote the complete patch trace on

\[
\{(s,\beta):s>=0,\ |\beta|<=B_N\}
\tag{34}
\]

with the sup norm. For any fixed `rho>0`, `(5)` and `(10)` imply

\[
|\Lambda_{\rm per}(E_{\rm c})-
\Lambda_{\rm per}(E_{{\rm c},\rho})|
=\rho,
\tag{35}
\]

but

\[
\|Obs_N(E_{\rm c})-Obs_N(E_{{\rm c},\rho})\|_\infty
\le e^{-\eta N+O(1)}.
\tag{36}
\]

Consequently any exact map from this observation space to `Lambda_per` that is Lipschitz on the two-point admissible family must have Lipschitz constant at least

\[
\boxed{
\rho\,e^{\eta N-O(1)}.
}
\tag{37}
\]

Equivalently, observation errors of half the right side of `(36)` make the two transition times minimax-indistinguishable. This is a transition functional obstruction, not merely a coefficient-reconstruction obstruction.

The stronger compactness statement follows because `rho=rho_N` may be any finite nonnegative sequence while `(36)` is unchanged. In particular, choosing `rho_N->infinity` yields targets whose complete local future heat patches converge exponentially to the collision target's patch while their periodic transition times diverge apart. This is an instability statement for the unrestricted periodic matched-control class; it is not an assertion about the scale of the actual Xi `Lambda`.

## 6. Prior-art and novelty boundary

The neighboring ingredients are classical in isolation. Root-location criteria for self-inversive polynomials and interlacing with roots of unity give broad ways to certify unit-circle root sets, while heat-equation observability theory gives many exponential spectral/control costs. XF-132 and XF-133 already audited those literatures, including clustered exponential-sum inversion and Lebeau--Robbiano-type heat observability.

No external theorem is load-bearing here. The new step is internal to the exact XF-067/XF-133 finite periodic model: the alternating signs of the barycentric packet make its unit-circle restriction a positive cosine combination, allowing the exponentially hidden tangent direction to be scaled explicitly to the discriminant; the centered heat PDE then proves that the resulting collision is transverse and fixes the transition time. A directed search did not locate this transition-sharp matched-control consequence in the neighboring self-inversive or heat-observability literature. No new external dependency is therefore added to `SOURCES.md`.

The result does not claim an optimal aperture constant. It inherits `log(2)/(4 pi)` from the convenient XF-133 choice `r=floor(M/3)`.

## 7. Consequence for the Xi-flow frontier

XF-133 left open the possibility that a direct transition functional might quotient away the exponentially hidden central tomography directions. For the **same local function-value heat-patch observation norm**, XF-134 closes that escape: one of those hidden directions can be followed all the way to a nondegenerate collision, and an arbitrarily large time translation along the same trajectory remains exponentially indistinguishable on the complete future patch.

Therefore a source-faithful Xi argument cannot obtain a stable transition-time bound merely by transferring the normalized heat solution on a fixed local complex patch and then applying an unrestricted target-side continuity principle. It needs structure outside this matched-control class: an Xi-specific theorem excluding the hidden central packet, a genuinely different observation norm that sees the discriminant transversely, sufficiently global spatial information, or another transition inequality using source constraints that the controls in `(2)`--`(4)` do not satisfy.

This is still a periodic matched-control obstruction, not an upper or lower bound on the actual de Bruijn--Newman constant and not a statement that the actual Xi divisor realizes these central packets.