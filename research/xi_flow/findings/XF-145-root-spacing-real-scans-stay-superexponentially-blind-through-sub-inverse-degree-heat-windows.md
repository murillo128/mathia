# XF-145 — root-spacing real scans stay superexponentially blind through sub-inverse-degree heat windows

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE/SHORT-TIME-REAL-SCAN-CONDITIONING` + `MATCHED-CONTROL` + `UNIT-CIRCLE-ADMISSIBLE` + `REAL-AXIS-SCAN` + `TRANSITION-TIME` + `SUPEREXPONENTIAL-BLINDNESS`. XF-143 and XF-144 show that real-axis information breaks the exact reflected-shell degeneracy: two half-spacing heat traces recover the full periodic state, and even an arbitrarily small nonconstant real scan is generically injective. That exact identifiability does not imply a usable short-time modulus. The transition-sharp central packet of XF-141 remains **superexponentially** invisible to every root-spacing real scan throughout any heat window `o(1/N)`.

## Claim

Let `N=2M`, take the maximal XF-141 packet depth

\[
r=M-1=\frac N2-1,
\tag{1}
\]

and use the XF-141 amplitude family

\[
E_\lambda(w,s)
=1+w^N+\lambda t_*\Delta E(w,s),
\qquad 0<\lambda\le1,
\tag{2}
\]

under

\[
E_k(s)=E_k(0)e^{-a k(N-k)s},
\qquad a>0.
\tag{3}
\]

For every prescribed `rho>=0`, XF-141 gives a unique `lambda_rho in (0,1]` with

\[
\Lambda_{\rm per}(E_1)=0,
\qquad
\Lambda_{\rm per}(E_{\lambda_\rho})=-\rho.
\tag{4}
\]

Write the real-axis physical probe as

\[
R_\lambda(x,s)
:=E_\lambda\!\left(-e^{-2\pi i x/L},s\right).
\tag{5}
\]

Fix `C>0`. Let `S_N>=0` be any heat-time horizon and put

\[
u_N:=aS_N.
\tag{6}
\]

There are constants depending only on `C` such that, whenever `N` is sufficiently large,

\[
\boxed{
\sup_{\substack{0\le s\le S_N\\ |x|\le CL/N}}
|R_1(x,s)-R_{\lambda_\rho}(x,s)|
\le
C_0^r (r u_N)^r e^{2r^2u_N}
+
C_0^r\left(\frac{C}{N}\right)^{2r}.
}
\tag{7}
\]

The bound is uniform in `rho`. In particular, if

\[
\boxed{N aS_N\longrightarrow0,}
\tag{8}
\]

then

\[
\boxed{
\sup_{\substack{0\le s\le S_N\\ |x|\le CL/N}}
|R_1-R_{\lambda_\rho}|
\le
\exp\!\left[
-r\log\frac1{NaS_N}+O_C(N)
\right]
+
\exp[-2r\log N+O_C(N)],
}
\tag{9}
\]

with the first term omitted when `S_N=0`. Since `r=N/2-1`, every `o(1/N)` heat window is therefore **superexponentially transition-blind**:

\[
\boxed{
N aS_N\to0
\quad\Longrightarrow\quad
\|R_1-R_{\lambda_\rho}\|_{L^\infty}=e^{-\omega(N)}
}
\tag{10}
\]

while the transition times differ by exactly `rho`.

A useful polynomial-scale specialization is: for every fixed `epsilon>0` and `A>0`,

\[
S_N\le\frac{A}{aN^{1+\epsilon}}
\tag{11}
\]

implies

\[
\boxed{
\sup_{\substack{0\le s\le S_N\\ |x|\le CL/N}}
|R_1-R_{\lambda_\rho}|
\le
\exp\!\left[-\frac{\epsilon}{2}N\log N+O_{A,C,\epsilon}(N)\right].
}
\tag{12}
\]

Consequently, for any fixed `rho>0`, every Lipschitz decoder from this complete real space-time tube to `Lambda_per` has condition number at least

\[
\boxed{
\exp\!\left[\frac{\epsilon}{2}N\log N-O_{A,C,\epsilon}(N)\right].
}
\tag{13}
\]

This remains true for an arbitrary moving scan `x=x(s)` contained in the tube, since its trace is a restriction of the observation in `(7)`.

At the initial slice one gets the sharper exact identity

\[
\boxed{
|R_1(x,0)-R_{\lambda_\rho}(x,0)|
=
2(1-\lambda_\rho)
\left|\sin\frac{\pi x}{L}\right|^{N-2}.
}
\tag{14}
\]

Hence

\[
\boxed{
\sup_{|x|\le CL/N}
|R_1(x,0)-R_{\lambda_\rho}(x,0)|
\le
2\left(\frac{\pi C}{N}\right)^{N-2}
=
\exp[-N\log N+O_C(N)].
}
\tag{15}
\]

Thus even a continuum real arc one root-spacing wide can be exactly identifying at fixed degree while being `N^{Theta(N)}`-ill-conditioned for the transition functional.

## Derivation

### 1. The XF-141 packet has an exact heat-semigroup representation

Use the XF-141 coordinate

\[
\zeta_{\beta,N}=-e^{\beta/N},
\qquad
Q_\lambda(\beta,s)=E_\lambda(\zeta_{\beta,N},s),
\tag{16}
\]

and set

\[
u:=as,
\qquad
y:=\frac\beta N.
\tag{17}
\]

For the quadratic barycentric weights `omega_j` of XF-141,

\[
\sum_{j=0}^r|\omega_j|=\frac{4^r}{(2r)!}
\tag{18}
\]

and the transition normalization `t_*` cancels the coefficient normalization exactly. XF-141 therefore gives

\[
t_*\Delta Q_\beta(s)
=
-2(-1)^{M+r}e^{\beta/2-M^2u}
\frac{(2r)!}{4^r}
\sum_{j=0}^r
\omega_j e^{j^2u}\cosh(jy).
\tag{19}
\]

At `u=0`, the central-difference identity is

\[
\frac{(2r)!}{4^r}
\sum_{j=0}^r\omega_j\cosh(jy)
=
\sinh^{2r}\!\left(\frac y2\right).
\tag{20}
\]

Because `partial_y^2 cosh(jy)=j^2 cosh(jy)`, multiplying the `j`th term by `e^{j^2u}` is exactly the heat semigroup in `y`. Thus `(19)` becomes the exact identity

\[
\boxed{
t_*\Delta Q_\beta(s)
=
-2(-1)^{M+r}e^{\beta/2-M^2u}
\left(e^{u\partial_y^2}
\sinh^{2r}\!\frac y2\right)_{y=\beta/N}.
}
\tag{21}
\]

This is the useful strengthening of the transition-slice formula in XF-141. It exposes directly how quickly positive heat time can unfold the order-`2r` spatial contact.

For `u>=0`, the finite exponential polynomial in `(21)` has the exact Gaussian representation

\[
\boxed{
e^{u\partial_y^2}f(y)
=
\mathbb E\,f(y+\sqrt{2u}\,Z),
\qquad Z\sim N(0,1),
}
\tag{22}
\]

with `f(y)=sinh^(2r)(y/2)`. No PDE approximation or infinite-dimensional heat-kernel theorem is being imported here; `(22)` follows termwise from `E exp(tZ)=exp(t^2/2)` for the finitely many exponentials in `f`.

### 2. Root-spacing real observation converts the packet to a Gaussian high moment

For the physical real probe `(5)`, comparison with `(16)` gives

\[
\beta=-\frac{2\pi iN x}{L},
\qquad
y=-\frac{2\pi i x}{L}.
\tag{23}
\]

Hence `|e^(beta/2)|=1`. Write `y=iv`, where on the root-spacing tube

\[
|v|\le\frac{2\pi C}{N}.
\tag{24}
\]

Since

\[
R_1-R_{\lambda_\rho}
=(1-\lambda_\rho)t_*\Delta Q,
\tag{25}
\]

and `0<=1-lambda_rho<=1`, equations `(21)`--`(22)` give

\[
|R_1-R_{\lambda_\rho}|
\le
2\,\mathbb E
\left|
\sinh\!\left(
\frac{iv+\sqrt{2u}Z}{2}
\right)
\right|^{2r}.
\tag{26}
\]

Put `q=sqrt(u/2)`. The elementary exact identity

\[
|\sinh(qZ+iv/2)|^2
=
\sinh^2(qZ)+\sin^2(v/2)
\tag{27}
\]

turns the two-variable cancellation problem into a positive Gaussian moment. Using

\[
(A+B)^r\le2^{r-1}(A^r+B^r),
\qquad
|\sinh t|\le |t|e^{|t|},
\tag{28}
\]

we obtain

\[
|R_1-R_{\lambda_\rho}|
\le
2^r q^{2r}
\mathbb E\!\left[|Z|^{2r}e^{2rq|Z|}\right]
+
2^r\left(\frac{\pi C}{N}\right)^{2r}.
\tag{29}
\]

Cauchy--Schwarz and the standard Gaussian moment/MGF bounds give

\[
\begin{aligned}
\mathbb E\!\left[|Z|^{2r}e^{2rq|Z|}\right]
&\le
\left(\mathbb E|Z|^{4r}\right)^{1/2}
\left(\mathbb E e^{4rq|Z|}\right)^{1/2}\\
&\le
(C_1r)^r e^{2r^2u}.
\end{aligned}
\tag{30}
\]

Here one may use explicitly

\[
\mathbb E|Z|^{4r}
=\frac{(4r)!}{2^{2r}(2r)!},
\qquad
\mathbb E e^{t|Z|}\le2e^{t^2/2}.
\tag{31}
\]

Since `q^(2r)=(u/2)^r`, equations `(29)`--`(31)` prove `(7)` after absorbing fixed powers of `2` into `C_0^r`.

### 3. Every `o(1/N)` heat window remains superexponentially blind

Take the supremum over `u<=u_N`. With `r=N/2-1`,

\[
r u_N\le\frac12Nu_N,
\qquad
2r^2u_N\le\frac12N(Nu_N).
\tag{32}
\]

If `Nu_N->0`, the exponential tilt in `(7)` contributes only `e^{o(N)}`. The first term therefore has logarithm

\[
-r\log\frac1{Nu_N}+O(N),
\tag{33}
\]

while the spatial term has logarithm

\[
-2r\log N+O_C(N).
\tag{34}
\]

This proves `(9)`--`(10)`. If `u_N=A N^(-1-epsilon)`, then

\[
\log\frac1{Nu_N}
=\epsilon\log N-\log A,
\tag{35}
\]

and `(12)` follows because `r=N/2+O(1)`.

The scale statement is worth keeping precise. The theorem proves a superexponential obstruction for **every** window with `aNS_N->0`. It does not prove stable recovery at `S_N asymp 1/(aN)`. Rather, `1/(aN)` is the first heat-time scale at which this particular high-contact argument no longer forces a superexponential loss. That is now the natural quantitative escape scale to test.

### 4. The initial slice has an exact `N^{-N}` profile

At `u=0`, `(21)` reduces to the XF-141 transition-slice formula. Substituting `(23)` gives

\[
\sinh\!\left(\frac y2\right)
=
-i\sin\!\left(\frac{\pi x}{L}\right).
\tag{36}
\]

Because `2r=N-2`, equations `(21)` and `(25)` yield `(14)` exactly. For fixed `C` and large `N`, `|pi x/L|<=pi C/N`, so `|sin t|<=|t|` gives `(15)`.

This immediately calibrates the two-point geometry of XF-143. At `x=0` the two controls agree exactly, while at its second half-spacing point

\[
x=\frac{L}{2N}
\tag{37}
\]

their initial values differ by at most

\[
2\left(\frac{\pi}{2N}\right)^{N-2}.
\tag{38}
\]

Therefore the `O(N)` reflected-shell spatial inversion in XF-143 is not where the central packet becomes visible. Its distinguishing signal must come from **positive heat-time unfolding**. This separates the spatial and temporal conditioning mechanisms cleanly.

## Logarithmic and reference-normalized observations

The obstruction is not an artifact of raw polynomial scale. Fix `0<C<1/4`. On the same real tube, the endpoint carrier is

\[
B(x):=1+e^{-2\pi iNx/L},
\tag{39}
\]

and

\[
|B(x)|\ge2\cos(\pi C)>0.
\tag{40}
\]

Equation `(7)` applied to the packet itself shows that, when `aNS_N->0`,

\[
\sup_{0\le s\le S_N,\ |x|\le CL/N}
|t_*\Delta Q|=e^{-\omega(N)}.
\tag{41}
\]

Hence for all sufficiently large `N`, every intermediate amplitude `theta in [lambda_rho,1]` keeps

\[
|B+\theta t_*\Delta Q|
\ge \cos(\pi C)
\tag{42}
\]

throughout the tube. Choosing the logarithms by continuation from `x=0`,

\[
\log R_1-\log R_{\lambda_\rho}
=
\int_{\lambda_\rho}^{1}
\frac{t_*\Delta Q}{B+\theta t_*\Delta Q}\,d\theta,
\tag{43}
\]

so the logarithmic difference obeys the same superexponential scale as `(7)` up to a `C`-dependent constant. Dividing both controls by any common nonvanishing analytic reference cancels from `(43)` exactly. Thus a Gaussian/reference quotient does not repair this short-time target-side conditioning loss by itself.

## Exact identifiability versus quantitative stability

For each fixed degree `N`, knowing `R_lambda(x,0)` on any nontrivial real interval determines the polynomial state by the identity theorem; a nonconstant moving trace also breaks the exact reflected degeneracy under the hypotheses of XF-144. XF-145 is therefore deliberately **not** another non-identifiability theorem. It is a quantitative transition-functional theorem: on a root-spacing spatial aperture, the central packet can hide an `O(1)` change of `Lambda_per` below every `e^{-cN}` noise scale throughout every `o(1/N)` heat window.

For a fixed `rho>0`, let `Obs_N` be either the full tube in `(7)` or any moving path contained in it, equipped with the sup norm. Then

\[
|\Lambda_{\rm per}(E_1)-\Lambda_{\rm per}(E_{\lambda_\rho})|=\rho.
\tag{44}
\]

Combining this with `(12)` gives `(13)`. More strongly, `rho=rho_N` may be any finite nonnegative sequence; the observation upper bound does not depend on it. One may therefore let `rho_N->infinity` while the short-time root-spacing traces converge superexponentially. Exact injectivity provides no degree-uniform compactness for the transition functional on this matched-control family.

## Checks and falsifiers

The static formula has an immediate finite-degree check. For `N=6`, `M=3`, `r=2`, and the XF-141 example `rho=0.2`, one has `lambda_rho=0.196659957...`. At the half-spacing point `x=L/12`, equation `(14)` gives

\[
|R_1-R_{\lambda_\rho}|
=2(1-\lambda_\rho)\sin^4(\pi/12)
\approx0.00720965,
\tag{45}
\]

below the amplitude-independent bound

\[
2\sin^4(\pi/12)\approx0.00897460.
\tag{46}
\]

For larger degree the decay becomes extremely fast: at `C=1/2`, the static upper bound `(15)` is already about `10^{-53.1}` for `N=40` and `10^{-176.5}` for `N=100`.

A decisive falsifier for `(7)` would be a failure of the semigroup identity `(21)` or of the Gaussian representation `(22)`. Both are coefficientwise identities on the finite exponential basis `e^(jy)`, so no convergence issue is present. The only asymptotic step is the Gaussian-moment estimate. The conclusion `e^{-omega(N)}` requires `aNS_N->0`; the theorem deliberately makes no superexponential claim at the boundary scale `S_N asymp 1/(aN)`.

## Prior-art and novelty audit

The closest classical quantitative context is Remez/Turan--Nazarov propagation of smallness for algebraic, trigonometric, and exponential polynomials. Nazarov's local estimates for exponential polynomials allow degree-dependent amplification when information is restricted to a small subset, and sharp Remez inequalities for trigonometric polynomials make the same exact-identifiability-versus-conditioning distinction. On an interval whose relative width is `Theta(1/N)`, the generic propagation scale permits factors of order `N^{Theta(N)}`. The static bound `(15)` realizes that scale inside a **transition-sharp, unit-circle-admissible Newman matched-control family** rather than for an arbitrary polynomial.

The neighboring heat-control literature also studies rapidly worsening observability/control costs as the observation time tends to zero; Miller's small-time heat-control bounds and later fast-control work are representative. Those results are context rather than dependencies. XF-145 uses neither a Remez theorem nor an external heat-observability theorem in its proof: the bound follows from the exact XF-141 central-difference packet, the finite exponential heat semigroup, and elementary Gaussian moments. No new external theorem is load-bearing, so no `SOURCES.md` update is required.

The mathematical delta from XF-144 is not merely that small scans can be badly conditioned. XF-144 gives exact injectivity and notes inverse-excursion conditioning qualitatively. XF-145 supplies an explicit transition-sharp family and a **joint space-time scale law**: root-spacing excursion plus any `o(1/N)` heat duration leaves the transition signal superexponentially small, with the concrete rate `(9)` and the polynomial-window rate `(12)`.

## Consequence for the Xi-flow frontier

The positive target-side lesson of XF-143--XF-144 survives, but its quantitative gate is now sharper. A real scan is genuinely different information from an instantaneous jet, yet merely making the scan nonconstant is not enough for a source-faithful Xi argument at realistic precision. If the transferred observation remains inside one root-spacing neighborhood of the remote `w=-1` center, then the heat history must reach at least the inverse-degree scale before the XF-141 central packet ceases to impose a superexponential conditioning barrier.

The next target-side question is therefore no longer just whether a moving real probe is injective. It is to quantify observability on the boundary scale

\[
\boxed{s\asymp\frac1{aN}}
\tag{47}
\]

and beyond: does a root-spacing scan acquire a polynomially or merely exponentially conditioned transition signal once the outermost packet shells have had `Theta(1)` relative heat time to separate? A complementary source-side escape remains unchanged: prove that the actual Xi source cannot realize the XF-141 central packet direction with the required amplitude. Either route would evade the theorem; exact real-axis scanning alone does not.