# XF-145 — root-spacing real scans stay superexponentially blind through sub-inverse-degree heat windows

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE/SHORT-TIME-REAL-SCAN-CONDITIONING` + `MATCHED-CONTROL` + `UNIT-CIRCLE-ADMISSIBLE` + `REAL-AXIS-SCAN` + `TRANSITION-TIME` + `SUPEREXPONENTIAL-BLINDNESS`. XF-143 and XF-144 show that real-axis information breaks the exact reflected-shell degeneracy: two half-spacing heat traces recover the full periodic state, and even an arbitrarily small nonconstant real scan is generically injective. Exact identifiability does not imply a usable short-time modulus. The transition-sharp central packet of XF-141 remains **superexponentially** invisible to every root-spacing real scan throughout any heat window `o(1/N)`.

## Claim

Let `N=2M`, take the maximal XF-141 packet depth

\[
r=M-1=\frac N2-1,
\tag{1}
\]

and use its amplitude family

\[
E_\lambda(w,s)=1+w^N+\lambda t_*\Delta E(w,s),
\qquad 0<\lambda\le1,
\tag{2}
\]

under the coefficient heat flow

\[
E_k(s)=E_k(0)e^{-a k(N-k)s},
\qquad a>0.
\tag{3}
\]

For every prescribed `rho>=0`, XF-141 gives `lambda_rho in (0,1]` such that

\[
\Lambda_{\rm per}(E_1)=0,
\qquad
\Lambda_{\rm per}(E_{\lambda_\rho})=-\rho.
\tag{4}
\]

Observe the real axis through

\[
R_\lambda(x,s)
:=E_\lambda\!\left(-e^{-2\pi i x/L},s\right).
\tag{5}
\]

Fix `C>0`, let `S_N>=0`, and put `u_N=aS_N`. There is an absolute `C_0>1` such that for all sufficiently large even `N`, uniformly in `rho`,

\[
\boxed{
\sup_{\substack{0\le s\le S_N\\ |x|\le CL/N}}
|R_1(x,s)-R_{\lambda_\rho}(x,s)|
\le
C_0^r(ru_N)^r e^{2r^2u_N}
+
C_0^r\left(\frac{C}{N}\right)^{2r}.
}
\tag{6}
\]

Consequently, if

\[
NaS_N\longrightarrow0,
\tag{7}
\]

then

\[
\boxed{
\sup_{\substack{0\le s\le S_N\\ |x|\le CL/N}}
|R_1-R_{\lambda_\rho}|
\le
\exp\!\left[-r\log\frac1{NaS_N}+O_C(N)\right]
+
\exp[-2r\log N+O_C(N)],
}
\tag{8}
\]

where the first term is omitted for `S_N=0`. Because `r=N/2-1`, every `o(1/N)` heat window is therefore superexponentially transition-blind:

\[
\boxed{
NaS_N\to0
\quad\Longrightarrow\quad
\|R_1-R_{\lambda_\rho}\|_{L^\infty}=e^{-\omega(N)},
}
\tag{9}
\]

while the transition times differ by exactly `rho`.

For the useful polynomial family

\[
S_N\le\frac{A}{aN^{1+\varepsilon}},
\qquad A>0,\quad\varepsilon>0,
\tag{10}
\]

define

\[
\gamma_\varepsilon:=\min\left\{\frac\varepsilon2,1\right\}.
\tag{11}
\]

Then `(8)` gives

\[
\boxed{
\sup_{\substack{0\le s\le S_N\\ |x|\le CL/N}}
|R_1-R_{\lambda_\rho}|
\le
\exp[-\gamma_\varepsilon N\log N+O_{A,C,\varepsilon}(N)].
}
\tag{12}
\]

The saturation at `gamma_epsilon=1` is real: even at `s=0`, a root-spacing spatial window contributes an `exp[-N log N+O(N)]` floor to this bound. Thus for fixed `rho>0`, any Lipschitz decoder from the complete tube in `(12)` to `Lambda_per` must have condition number at least

\[
\boxed{
\exp[\gamma_\varepsilon N\log N-O_{A,C,\varepsilon}(N)].
}
\tag{13}
\]

The same lower bound applies to any moving scan `x=x(s)` contained in the tube, because its trace is only a restriction of the full observation.

At the initial slice there is a sharper exact identity:

\[
\boxed{
|R_1(x,0)-R_{\lambda_\rho}(x,0)|
=2(1-\lambda_\rho)
\left|\sin\frac{\pi x}{L}\right|^{N-2}.
}
\tag{14}
\]

Therefore

\[
\boxed{
\sup_{|x|\le CL/N}|R_1(x,0)-R_{\lambda_\rho}(x,0)|
\le2\left(\frac{\pi C}{N}\right)^{N-2}
=\exp[-N\log N+O_C(N)].
}
\tag{15}
\]

So a continuum real arc one root-spacing wide can be exactly identifying at fixed degree while being `N^{Theta(N)}`-ill-conditioned for the transition functional.

## Derivation

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
\qquad y:=\frac\beta N.
\tag{17}
\]

For the quadratic barycentric weights `omega_j`, XF-141 proves

\[
\sum_{j=0}^r|\omega_j|=\frac{4^r}{(2r)!}
\tag{18}
\]

and the transition normalization cancels the coefficient normalization. Hence

\[
t_*\Delta Q_\beta(s)
=-2(-1)^{M+r}e^{\beta/2-M^2u}
\frac{(2r)!}{4^r}
\sum_{j=0}^r\omega_j e^{j^2u}\cosh(jy).
\tag{19}
\]

At `u=0`, the central-difference identity is

\[
\frac{(2r)!}{4^r}\sum_{j=0}^r\omega_j\cosh(jy)
=\sinh^{2r}\!\left(\frac y2\right).
\tag{20}
\]

Since `partial_y^2 cosh(jy)=j^2 cosh(jy)`, multiplying the `j`th term by `e^(j^2u)` is exactly the heat semigroup in `y`. Therefore

\[
\boxed{
t_*\Delta Q_\beta(s)
=-2(-1)^{M+r}e^{\beta/2-M^2u}
\left(e^{u\partial_y^2}\sinh^{2r}\!\frac y2\right)_{y=\beta/N}.
}
\tag{21}
\]

For `u>=0`, this finite exponential polynomial has the exact Gaussian representation

\[
\boxed{
e^{u\partial_y^2}f(y)
=\mathbb E\,f(y+\sqrt{2u}\,Z),
\qquad Z\sim N(0,1),
}
\tag{22}
\]

with `f(y)=sinh^(2r)(y/2)`. This follows coefficientwise from `E e^(tZ)=e^(t^2/2)`; there is no convergence or infinite-dimensional semigroup issue.

For the physical real probe `(5)`,

\[
\beta=-\frac{2\pi iNx}{L},
\qquad
y=-\frac{2\pi ix}{L}=iv,
\qquad |v|\le\frac{2\pi C}{N}.
\tag{23}
\]

Because

\[
R_1-R_{\lambda_\rho}=(1-\lambda_\rho)t_*\Delta Q,
\tag{24}
\]

and `0<=1-lambda_rho<=1`, `(21)`--`(22)` imply, with `q=sqrt(u/2)`,

\[
|R_1-R_{\lambda_\rho}|
\le2\,\mathbb E\left|\sinh(qZ+iv/2)\right|^{2r}.
\tag{25}
\]

The exact identity

\[
|\sinh(qZ+iv/2)|^2
=\sinh^2(qZ)+\sin^2(v/2)
\tag{26}
\]

turns the cancellation into a positive Gaussian moment. Using

\[
(A+B)^r\le2^{r-1}(A^r+B^r),
\qquad
|\sinh t|\le|t|e^{|t|},
\tag{27}
\]

gives

\[
|R_1-R_{\lambda_\rho}|
\le2^r q^{2r}\mathbb E\!\left[|Z|^{2r}e^{2rq|Z|}\right]
+2^r\left(\frac{\pi C}{N}\right)^{2r}.
\tag{28}
\]

Cauchy--Schwarz and the elementary Gaussian estimates

\[
\mathbb E|Z|^{4r}=\frac{(4r)!}{2^{2r}(2r)!},
\qquad
\mathbb E e^{t|Z|}\le2e^{t^2/2}
\tag{29}
\]

yield

\[
\mathbb E\!\left[|Z|^{2r}e^{2rq|Z|}\right]
\le(C_1r)^r e^{2r^2u}.
\tag{30}
\]

Since `q^(2r)=(u/2)^r`, `(28)`--`(30)` prove `(6)`.

Now `r=N/2-1` gives

\[
ru_N\le\frac12Nu_N,
\qquad
2r^2u_N\le\frac12N(Nu_N).
\tag{31}
\]

Under `Nu_N->0`, the Gaussian tilt is only `e^{o(N)}` and the two terms of `(6)` have logarithms

\[
-r\log\frac1{Nu_N}+O(N),
\qquad
-2r\log N+O_C(N),
\tag{32}
\]

which proves `(8)`--`(9)`. For `u_N<=A N^(-1-epsilon)`, the first term contributes `-(epsilon/2)N log N+O(N)` and the second contributes `-N log N+O(N)`, producing the minimum in `(11)`--`(12)`.

At `u=0`, `(21)` becomes the XF-141 transition-slice formula. Since

\[
\sinh\!\left(\frac y2\right)
=-i\sin\!\left(\frac{\pi x}{L}\right),
\tag{33}
\]

and `2r=N-2`, equation `(14)` follows exactly; `(15)` is then just `|sin t|<=|t|`.

## Consequences for XF-143 and XF-144

At the two points used in XF-143, the initial-slice difference is zero at `x=0` and, at

\[
x=\frac{L}{2N},
\tag{34}
\]

is at most

\[
2\left(\frac{\pi}{2N}\right)^{N-2}.
\tag{35}
\]

Thus the `O(N)` reflected-shell spatial inversion of XF-143 is not where this packet becomes quantitatively visible. Its distinguishing signal must come from **positive heat-time unfolding**.

Likewise, XF-144's arbitrarily small moving real probe can remain exactly injective while being superexponentially useless at finite precision. XF-145 sharpens its qualitative conditioning caveat into a joint scale law: root-spacing excursion plus any heat duration `o(1/N)` leaves an `O(1)` transition-time difference below every `e^{-cN}` noise scale.

The theorem does **not** assert stable recovery at

\[
s\asymp\frac1{aN}.
\tag{36}
\]

It says only that this inverse-degree scale is the first one at which the present high-contact argument stops forcing superexponential blindness. Quantitative observability at and beyond `(36)` is therefore the next target-side gate.

## Logarithmic and reference-normalized observations

The obstruction is not an artifact of raw polynomial scale. Fix `0<C<1/4`. The endpoint carrier

\[
B(x)=1+e^{-2\pi iNx/L}
\tag{37}
\]

satisfies

\[
|B(x)|\ge2\cos(\pi C)>0
\tag{38}
\]

on `|x|<=CL/N`. The derivation above applied directly to `t_*Delta Q` gives `e^{-omega(N)}` uniformly on every tube with `NaS_N->0`. Hence for large `N`, all intermediate amplitudes `theta in [lambda_rho,1]` remain uniformly nonzero there. Choosing logarithms by continuation from `x=0`,

\[
\log R_1-\log R_{\lambda_\rho}
=\int_{\lambda_\rho}^1
\frac{t_*\Delta Q}{B+\theta t_*\Delta Q}\,d\theta,
\tag{39}
\]

so the logarithmic difference has the same superexponential scale up to a `C`-dependent constant. Dividing both controls by any common nonvanishing analytic reference cancels from `(39)` exactly. A Gaussian/reference quotient therefore does not repair this short-time target-side conditioning loss by itself.

## Checks and falsifiers

For `N=6`, `M=3`, `r=2`, and the XF-141 example `rho=0.2`, `lambda_rho=0.196659957...`. At the half-spacing point `x=L/12`, `(14)` gives

\[
|R_1-R_{\lambda_\rho}|
=2(1-\lambda_\rho)\sin^4(\pi/12)
\approx0.00720965,
\tag{40}
\]

below the amplitude-independent bound `2 sin^4(pi/12) approximately 0.00897460`. At `C=1/2`, the static bound is already about `10^-53.1` for `N=40` and `10^-176.5` for `N=100`.

A decisive falsifier for the main estimate would be failure of `(21)` or `(22)`. Both are coefficientwise identities on a finite exponential basis. The only asymptotic hypothesis used for superexponential decay is `NaS_N->0`; no claim is made that the same rate survives at the boundary scale `(36)`.

## Prior-art and novelty audit

The closest classical quantitative context is Remez/Turan--Nazarov propagation of smallness for algebraic, trigonometric, and exponential polynomials. Nazarov's local estimates permit degree-dependent amplification from a small observation set, and sharp Remez inequalities for trigonometric polynomials make the same exact-identifiability-versus-conditioning distinction. On a set of relative width `Theta(1/N)`, the generic propagation scale allows factors of order `N^{Theta(N)}`. The static matched control `(15)` realizes that scale while changing the periodic Newman transition time by an arbitrary prescribed amount.

The neighboring heat-control literature also has rapidly worsening observability/control costs as the observation time tends to zero; Miller's small-time heat-control bounds and later fast-control work are representative. These are contextual rather than load-bearing. XF-145 uses neither a Remez theorem nor an external heat-observability theorem: the proof is the exact XF-141 central packet plus elementary finite-dimensional heat/Gaussian identities. No `SOURCES.md` change is therefore required.

The new mathematical content beyond XF-144 is the explicit **joint space-time transition-conditioning law** `(6)`--`(12)`. Exact real-axis scanning remains a genuine new coordinate, but root-spacing motion does not become quantitatively useful merely by being nonconstant. A source-faithful Xi route must either transport enough positive heat history to cross the inverse-degree boundary, enlarge/change the spatial observation geometry, or prove that the actual Xi source cannot realize this central packet direction.