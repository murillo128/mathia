# XF-147 — full-future real scans need near-antipodal reach for polynomial transition visibility

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE/FULL-FUTURE-MACROSCOPIC-SCAN-CONDITIONING` + `MATCHED-CONTROL` + `UNIT-CIRCLE-ADMISSIBLE` + `REAL-AXIS-SCAN` + `TRANSITION-TIME` + `SHARP-APERTURE-RATE`. XF-146 proves that the maximal-contact XF-141 pair stays base-two blind through the complete future history of a root-spacing tube. The same exact Gaussian representation yields a much stronger spatial statement: for every fixed centered real interval that omits a nonzero neighborhood of the antipodal point, the two histories remain exponentially close for **all** future heat time. The sharp exponential rate has an explicit aperture law. Polynomial transition visibility is not even permitted by this matched-control family until the observed interval reaches within `O(L sqrt(log N/N))` of the antipode.

## Claim

Use the maximal-contact family and notation of XF-141--XF-146:

\[
N=2M,\qquad r=M-1=\frac N2-1,
\tag{1}
\]

\[
E_\lambda(w,s)=1+w^N+\lambda t_*\Delta E(w,s),
\qquad
R_\lambda(x,s)=E_\lambda\!\left(-e^{-2\pi i x/L},s\right),
\tag{2}
\]

and, for fixed `rho>0`, choose `lambda_rho` so that

\[
\Lambda_{\rm per}(E_1)=0,
\qquad
\Lambda_{\rm per}(E_{\lambda_\rho})=-\rho.
\tag{3}
\]

For `0<=c<1/2`, define the complete future centered-strip separation

\[
S_N(c):=
\sup_{s\ge0}\sup_{|x|\le cL}
|R_1(x,s)-R_{\lambda_\rho}(x,s)|.
\tag{4}
\]

Then, for every even `N>=4`,

\[
\boxed{
S_N(c)
\le
4\max\!\left\{
2^{-(N-2)},
\sin(\pi c)^{N-2}
\right\}.
}
\tag{5}
\]

Moreover the exponential rate in `(5)` is sharp. Put

\[
\kappa(c)
:=
\min\!\left\{
\log2,
-\log\sin(\pi c)
\right\},
\tag{6}
\]

with the second entry interpreted as `+infinity` at `c=0`. Then

\[
\boxed{
\lim_{N\to\infty}
\frac1N\log S_N(c)
=-\kappa(c).
}
\tag{7}
\]

Thus there is a sharp aperture crossover at

\[
\sin(\pi c)=\frac12
\quad\Longleftrightarrow\quad
c=\frac16.
\tag{8}
\]

For `0<=c<=1/6`, the full-future visibility ceiling has the same base-two exponent as XF-146. For `1/6<c<1/2`, the edge of the observed interval controls the exponent:

\[
S_N(c)=\exp\!\left[-N\bigl(-\log\sin(\pi c)\bigr)+O(\log N)\right].
\tag{9}
\]

Consequently any Lipschitz decoder of `Lambda_per` from the complete future strip has condition number `K_N(c)` satisfying

\[
\boxed{
\liminf_{N\to\infty}\frac1N\log K_N(c)
\ge \kappa(c)>0
}
\tag{10}
\]

for every fixed proper aperture `c<1/2`.

There is also an exact near-antipodal boundary-layer law. Let

\[
c_N=\frac12-\varepsilon_N,
\qquad
0<\varepsilon_N<\frac13
\tag{11}
\]

eventually. Then

\[
\boxed{
2(1-\lambda_\rho)
\cos(\pi\varepsilon_N)^{N-2}
\le
S_N(c_N)
\le
4\cos(\pi\varepsilon_N)^{N-2}.
}
\tag{12}
\]

Hence, if `epsilon_N -> 0`,

\[
\log S_N(c_N)
=
-\frac{\pi^2}{2}N\varepsilon_N^2
+O(N\varepsilon_N^4+1).
\tag{13}
\]

In particular, if

\[
\frac{N\varepsilon_N^2}{\log N}\longrightarrow\infty,
\tag{14}
\]

then the matched histories are superpolynomially close and every transition decoder has superpolynomial condition number. This adversary stops forcing superpolynomial instability only when

\[
\boxed{
\varepsilon_N
=O\!\left(\sqrt{\frac{\log N}{N}}\right).
}
\tag{15}
\]

Equivalently, a centered real scan must reach to within

\[
O\!\left(L\sqrt{\frac{\log N}{N}}\right)
\tag{16}
\]

of the antipodal point before polynomial conditioning is even left open by this matched-control family. Since the mean root spacing is `L/N`, the remaining unobserved boundary layer may contain only `O(sqrt(N log N))` mean spacings.

## 1. A sharper pointwise envelope than XF-146

XF-146 starts from the exact XF-145 Gaussian representation

\[
t_*\Delta Q_\beta(s)
=-2(-1)^{M+r}e^{\beta/2-M^2u}
\mathbb E\,
\sinh^{2r}\!\left(
\frac y2+\sqrt{\frac u2}Z
\right),
\tag{17}
\]

where

\[
y=-\frac{2\pi ix}{L},
\qquad
u:=as,
\qquad
Z\sim N(0,1).
\tag{18}
\]

Write `y=iv`, `q=sqrt(u/2)`, and

\[
b:=\left|\sin\frac v2\right|
=\left|\sin\frac{\pi x}{L}\right|.
\tag{19}
\]

The exact identity

\[
|\sinh(qZ+iv/2)|^2
=\sinh^2(qZ)+b^2
\tag{20}
\]

was already used in XF-146. The previous estimate replaced the square root by `sinh|t|+b`, which is efficient only when `b=O(1/N)`. For arbitrary `0<=b<=1`, one can instead prove the sharp elementary envelope

\[
\boxed{
\sqrt{\sinh^2t+b^2}
\le
\frac12e^t\max\{1,2b\},
\qquad t\ge0.
}
\tag{21}
\]

Indeed, with `z=e^{-2t}`,

\[
\left[
2e^{-t}\sqrt{\sinh^2t+b^2}
\right]^2
=(1-z)^2+4b^2z.
\tag{22}
\]

The right-hand side is convex in `z in [0,1]`, so its maximum is attained at an endpoint and equals `max{1,4b^2}`. This proves `(21)`.

Raising `(21)` to the power `2r` in `(17)` and using

\[
\mathbb E e^{t|Z|}\le2e^{t^2/2}
\tag{23}
\]

gives

\[
|t_*\Delta Q_\beta(s)|
\le
4\,4^{-r}\max\{1,2b\}^{2r}
 e^{-(M^2-r^2)u}.
\tag{24}
\]

For maximal contact, `2r=N-2` and `M^2-r^2=N-1`, hence

\[
\boxed{
|t_*\Delta Q_\beta(s)|
\le
4e^{-(N-1)u}
\max\!\left\{
2^{-(N-2)},
 b^{N-2}
\right\}.
}
\tag{25}
\]

Since

\[
R_1-R_{\lambda_\rho}
=(1-\lambda_\rho)t_*\Delta Q,
\qquad
0<\lambda_\rho\le1,
\tag{26}
\]

and `b<=sin(pi c)` on `|x|<=cL`, `(25)` proves `(5)`.

## 2. The aperture exponent is attained

Two witnesses give matching lower bounds in the two aperture regimes.

First, XF-146 proves that at the center and at

\[
a s_N=\frac{\log N}{N},
\tag{27}
\]

one has

\[
|R_1(0,s_N)-R_{\lambda_\rho}(0,s_N)|
=
(1+o(1))\frac{16}{eN}2^{-N}.
\tag{28}
\]

Therefore every strip containing `x=0` has at least the base-two exponential signal.

Second, at the initial slice `s=0`, the exact maximal-contact identity is

\[
|R_1(x,0)-R_{\lambda_\rho}(x,0)|
=
2(1-\lambda_\rho)
\left|\sin\frac{\pi x}{L}\right|^{N-2}.
\tag{29}
\]

For fixed `rho>0`, XF-146 also gives

\[
0<\lambda_\rho\le e^{-a(N-1)\rho},
\tag{30}
\]

so `1-lambda_rho=1+o(1)`. Evaluating `(29)` at `x=cL` gives the edge lower bound. When `c<=1/6`, this edge term decays at least as fast as `2^{-N}` and the later center witness `(28)` determines the exponential rate. When `c>1/6`, the initial edge term is larger and determines it. This proves `(7)`--`(9)`.

For `c_N=1/2-epsilon_N`, the edge value in `(29)` is exactly `cos(pi epsilon_N)^{N-2}` up to the prefactor, while `(25)` gives the same expression as a uniform all-future upper bound because `cos(pi epsilon_N)>1/2` eventually. This proves `(12)`, and the expansion

\[
\log\cos z=-\frac{z^2}{2}+O(z^4)
\tag{31}
\]

gives `(13)`--`(16)`.

## 3. What this closes and what it does not

XF-143--XF-144 show that extremely small real motion can identify the finite periodic state exactly. XF-145 shows superexponential transition blindness for root-spacing scans over sub-inverse-degree heat windows, and XF-146 shows base-two exponential blindness for the complete future history of a root-spacing tube. XF-147 removes the remaining possibility that a **moderate macroscopic widening** of the same centered real scan repairs the conditioning. Any fixed fraction of a period strictly below the antipodal radius still leaves an exponential transition barrier.

The result does not prove that near-antipodal access is sufficient for stable recovery. Equation `(15)` is only the point at which this particular matched packet ceases to force superpolynomial conditioning. A sparse nonlocal observation that directly samples near the antipode may evade the contiguous-strip obstruction without observing the whole interval, and a source-specific Xi theorem may exclude the matched pair entirely.

The statement is also deliberately about the raw real heat trace. The common endpoint carrier used for logarithmic/reference-normalized root-spacing observations has many zeros across a macroscopic interval, so the zero-free logarithmic reduction from XF-146 cannot simply be extended to `|x|=Theta(L)`. No logarithmic or quotient claim is made here beyond the regions where its own zero-free hypotheses are separately verified.

## 4. Prior-art and novelty audit

The closest classical context is propagation of smallness for trigonometric/exponential polynomials, especially Remez and Turan--Nazarov inequalities, together with spectral/observability inequalities for heat equations. Those theories naturally allow constants exponential in the degree when one observes only a proper subset. A current audit found that broad mechanism, including sharp trigonometric Remez results and modern Turan--Nazarov formulations, but did not find the specific matched unit-circle heat pair, its exact `Lambda_per` separation, or the aperture law `(6)` with its `c=1/6` crossover and near-antipodal boundary layer.

No external theorem is load-bearing in the derivation: `(21)` is elementary, `(17)` and the transition pair are already canonical local evidence, and the sharpness witnesses are exact identities from XF-145--XF-146. Therefore this finding creates no new `SOURCES.md` dependency and makes no novelty claim for Remez/Turan--Nazarov theory itself.

## Research implication

For the target-side real-scan route, “use a somewhat wider local window” is no longer a meaningful escape from the maximal-contact obstruction. On this admissible family, **all future heat time still leaves an exponential transition modulus on every fixed proper centered aperture**. To stop this packet from forcing superpolynomial conditioning, the geometry must approach the antipodal point on the shrinking relative scale `sqrt(log N/N)`, use genuinely nonlocal placement that reaches that region, or invoke source-specific Xi structure that forbids the packet.

The next useful target-side test is therefore not another local derivative or longer-time refinement. It is to quantify the minimal nonlocal real observation geometry that intersects the near-antipodal visibility layer, and to ask whether such geometry can be represented by a source-faithful Xi observable without reintroducing a global inverse problem.