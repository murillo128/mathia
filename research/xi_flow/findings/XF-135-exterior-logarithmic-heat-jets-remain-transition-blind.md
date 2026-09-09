# XF-135 — exterior logarithmic heat jets remain transition-blind

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE/TRANSITION-CONDITIONING` + `LOG-DERIVATIVE-OBSERVABILITY` + `REFERENCE-INVARIANT` + `UNIT-CIRCLE-MATCHED-CONTROL` + `ZERO-DELAY` + `CROSS-SCALE`. XF-134 makes a complete zero-delay local function-value heat patch exponentially insensitive to an order-one change in periodic transition time. XF-133 explicitly left high spatial derivatives outside its observation norm, while the source-specific Xi carrier of XF-051 is naturally a logarithmic derivative and the accepted Gaussian-reference clue proposes dividing by a known caloric reference. Those two apparent repairs do not remove the target-side obstruction at any subexponential logarithmic-jet order.

Let `N=2M`, let `1<=r<M`, and let

\[
E_{\rm c}(w,s)=1+w^{2M}+t_*\Delta E(w,s)
\tag{1}
\]

be the transition-sharp XF-134 control, where `|t_*|<=2`, `Delta E` is the XF-133 central divided-difference packet, and

\[
\Lambda_{\rm per}(E_{\rm c})=0.
\tag{2}
\]

For any `rho>=0`, put

\[
E_{{\rm c},\rho}(w,s):=E_{\rm c}(w,s+\rho),
\qquad
\Lambda_{\rm per}(E_{{\rm c},\rho})=-\rho.
\tag{3}
\]

Use the same off-circle coordinate as XF-133--XF-134,

\[
\zeta_{\beta,N}:=-e^{\beta/N},
\qquad
Q_s(\beta):=E_{\rm c}(\zeta_{\beta,N},s).
\tag{4}
\]

Since `N=2M`, the stationary endpoint carrier is

\[
q_0(\beta):=1+\zeta_{\beta,N}^{2M}=1+e^\beta.
\tag{5}
\]

Write

\[
A_{M,r}:=\frac{(r!)^2}{(M^2-r^2)^r}.
\tag{6}
\]

Fix `sigma>0` and define the exterior patch

\[
\Omega_{B,\sigma}
:=\{\beta\in\mathbb C:|\beta|\le B,\ \operatorname{Re}\beta\ge\sigma\}.
\tag{7}
\]

Let

\[
d_\sigma:=\min\{1,\sigma/2\},
\qquad
m_\sigma:=e^{\sigma/2}-1.
\tag{8}
\]

Whenever

\[
\varepsilon_{M,r}(B,\sigma)
:=\frac{2e^{B+d_\sigma}}{m_\sigma}A_{M,r}
\le\frac12,
\tag{9}
\]

the logarithm of each observed control is analytic on the Cauchy disks needed below, and for every integer `j>=1`, every `rho>=0`, and every `s>=0`,

\[
\boxed{
\sup_{\beta\in\Omega_{B,\sigma}}
\left|
\partial_\beta^j\log Q_s(\beta)
-
\partial_\beta^j\log Q_{s+\rho}(\beta)
\right|
\le
\frac{8j!\,e^{B+d_\sigma}}{m_\sigma d_\sigma^j}
A_{M,r}.
}
\tag{10}
\]

Here `Q_(s+rho)` is exactly the trace of `E_(c,rho)` at observation time `s`. Thus the estimate is uniform over the **complete zero-delay future history** and over arbitrary finite time translations `rho`.

For

\[
r=\left\lfloor\frac M3\right\rfloor,
\tag{11}
\]

XF-133 gives

\[
A_{M,r}\le 8^{-r}
=\exp\left(-\frac{\log2}{2}N+O(1)\right).
\tag{12}
\]

Consequently, for every fixed `eta>0`, fixed `sigma>0`, and apertures

\[
B_N\le\left(\frac{\log2}{2}-\eta\right)N,
\tag{13}
\]

all fixed-order logarithmic jets are exponentially transition-blind. More strongly, if

\[
J_N\log(J_N+2)=o(N),
\tag{14}
\]

then

\[
\boxed{
\sup_{\substack{s\ge0,\ \rho\ge0\\
\beta\in\Omega_{B_N,\sigma}\\
1\le j\le J_N}}
\left|
\partial_\beta^j\log Q_s(\beta)
-
\partial_\beta^j\log Q_{s+\rho}(\beta)
\right|
\le
\exp(-\eta N+o(N)).
}
\tag{15}
\]

Thus not only finitely many derivatives but any logarithmic jet whose factorial Cauchy cost is subexponential in the degree remains exponentially insensitive to the transition-time shift.

## 1. XF-133 already gives the required analytic smallness on enlarged disks

By XF-134 and the stationary endpoint coefficients,

\[
Q_s(\beta)
=q_0(\beta)+u_s(\beta),
\qquad
u_s(\beta):=t_*\Delta E(\zeta_{\beta,N},s).
\tag{16}
\]

The symbol in `(16)` will be denoted `u_s`; explicitly,

\[
u_s(\beta):=t_*\Delta E(\zeta_{\beta,N},s).
\tag{17}
\]

XF-133 proves for every `C>=0`, simultaneously in all `s>=0` and all complex `|\gamma|<=C`,

\[
|\Delta E(\zeta_{\gamma,N},s)|
\le e^C A_{M,r}.
\tag{18}
\]

Since `|t_*|<=2`,

\[
|u_s(\gamma)|\le2e^C A_{M,r}.
\tag{19}
\]

Take `beta in Omega_(B,sigma)` and the closed disk `|gamma-beta|<=d_sigma`. By `(8)`,

\[
\operatorname{Re}\gamma\ge\frac\sigma2,
\qquad
|\gamma|\le B+d_\sigma.
\tag{20}
\]

On this disk the endpoint carrier obeys the elementary lower bound

\[
|q_0(\gamma)|=|1+e^\gamma|
\ge ||e^\gamma|-1|
\ge e^{\sigma/2}-1=m_\sigma.
\tag{21}
\]

Therefore

\[
v_s(\gamma):=\frac{u_s(\gamma)}{q_0(\gamma)}
\tag{22}
\]

is analytic and satisfies

\[
|v_s(\gamma)|
\le
\frac{2e^{B+d_\sigma}}{m_\sigma}A_{M,r}
=\varepsilon_{M,r}(B,\sigma).
\tag{23}
\]

Under `(9)`, `1+v_s` is zero-free there. We may therefore use the analytic branch

\[
F_s(\gamma):=\log(1+v_s(\gamma)),
\tag{24}
\]

normalized by its convergent power series. Since `|v_s|<=1/2`,

\[
|F_s(\gamma)|\le2|v_s(\gamma)|
\le2\varepsilon_{M,r}(B,\sigma).
\tag{25}
\]

This is the only place where exteriority is used: it supplies a source-independent nonvanishing floor for the simple endpoint carrier.

## 2. Cauchy differentiation converts value invisibility into jet invisibility

On the disk from `(20)`, Cauchy's derivative estimate applied to `(25)` gives for every `j>=1`

\[
|\partial_\beta^jF_s(\beta)|
\le
2j!d_\sigma^{-j}
\varepsilon_{M,r}(B,\sigma).
\tag{26}
\]

Because

\[
\log Q_s=\log q_0+F_s
\tag{27}
\]

locally on the zero-free disk, the known carrier term cancels when two heat times are compared. Applying `(26)` at `s` and `s+rho` yields

\[
\begin{aligned}
&|\partial_\beta^j\log Q_s(\beta)
-\partial_\beta^j\log Q_{s+\rho}(\beta)|\\
&\qquad\le
4j!d_\sigma^{-j}
\varepsilon_{M,r}(B,\sigma),
\end{aligned}
\tag{28}
\]

which is exactly `(10)` after substituting `(9)`.

No differentiated version of the barycentric construction is required. The value estimate of XF-133 is analytic on a slightly enlarged complex disk, and Cauchy theory automatically supplies all derivative estimates with the sharp generic factorial price. This also makes the quantifier in `(15)` transparent: by Stirling,

\[
\log(J_N!d_\sigma^{-J_N})
=O(J_N\log(J_N+2))=o(N),
\tag{29}
\]

while `(12)`--`(13)` retain an `eta N` exponential margin.

## 3. Root-spacing-normalized physical logarithmic derivatives obey the same bound

The XF-067 physical coordinate is

\[
w=-e^{-2\pi iz/L}.
\tag{30}
\]

Comparing with `(4)` gives

\[
\beta=-\frac{2\pi iN}{L}z,
\qquad
\partial_z=-\frac{2\pi iN}{L}\partial_\beta.
\tag{31}
\]

Hence the root-spacing-normalized spatial jets

\[
\left(\frac{L}{2\pi N}\right)^j
\partial_z^j\log E
\tag{32}
\]

have exactly the same magnitude as the `beta`-jets in `(10)`--`(15)`. The exterior condition `Re beta>=sigma` corresponds, up to the sign convention in `(31)`, to observing on one fixed side of the unit-circle line at vertical distance at least

\[
\frac{\sigma L}{2\pi N},
\tag{33}
\]

which is only of root-spacing order. Thus the obstruction does not arise from staying macroscopically far from the divisor.

At the same time, `(13)` still permits a spatial aperture occupying a fixed positive fraction of the period, as in XF-133--XF-134. The new result therefore covers a macroscopic local complex patch equipped with a growing family of root-spacing-normalized logarithmic derivatives.

## 4. Division by a common known reference cancels exactly in logarithmic jets

Let `W(\beta,s)` be any nonzero analytic reference on the observation patch, independent of which matched control is being observed. For every `j>=1`,

\[
\partial_\beta^j\log\frac{Q_s}{W_s}
-
\partial_\beta^j\log\frac{Q_{s+\rho}}{W_s}
=
\partial_\beta^j\log Q_s
-
\partial_\beta^j\log Q_{s+\rho}.
\tag{34}
\]

Thus a common reference division cannot improve the target-side separation measured by logarithmic jets: its entire contribution cancels. This applies in particular to the **structural role** proposed for the known Gaussian reference in the accepted Appell/reference clue. It does not refute that clue, because the clue's unresolved content is source-specific: the actual Xi numerator might obey additional estimates that exclude the XF-133/XF-134 packet before target-side inversion is attempted.

Equation `(34)` instead identifies the exact remaining obligation. Reference division can remove artificial seam zeros and geometric drift, but it does not by itself cure transition conditioning. A successful Xi bridge must show that the actual source lies in a quantitatively smaller class than these matched controls, or use an observation functional that is not equivalent to a subexponential family of local logarithmic jets.

## 5. Transition-time conditioning remains exponential

The controls in `(1)` and `(3)` satisfy

\[
|\Lambda_{\rm per}(E_{\rm c})
-\Lambda_{\rm per}(E_{{\rm c},\rho})|
=\rho.
\tag{35}
\]

For fixed `rho>0`, `(15)` says that their complete local logarithmic-jet histories differ by only `exp(-eta N+o(N))` in the stated observation norm. Therefore any Lipschitz decoder of `Lambda_per` on this two-point matched-control family has condition number at least

\[
\boxed{
\exp(\eta N-o(N))
}
\tag{36}
\]

up to the fixed multiplicative factor `rho`. As in XF-134, `rho=rho_N` may be any finite nonnegative sequence because the observation bound is uniform in `rho`; the same local logarithmic data consequently provide no degree-uniform compactness bound for the periodic transition time on this unrestricted matched-control class.

The result remains an obstruction for a **target-side continuity principle**, not a statement that the actual Xi family contains these controls or that its Newman constant has arbitrary scale. In particular, the exact infinite logarithmic derivative carrier of XF-051 can still be useful if a source theorem proves that Xi avoids the hidden central packet. What fails is the inference that local access to `H'/H`, finitely or subexponentially many of its normalized derivatives, or a common known-reference quotient is automatically a stable proxy for the transition.

## 6. Prior-art and novelty boundary

Cauchy derivative estimates, logarithmic derivatives of zero-free analytic functions, and quantitative observability/propagation-of-smallness for parabolic equations are classical. A directed audit included the measurable-set heat observability inequalities of Apraiz--Escauriaza--Wang--Zhang and the quantitative space-time analyticity work of Escauriaza--Montaner--Zhang, as well as the surrounding Lebeau--Robbiano spectral-observability literature. Those results establish broad positive observability principles with quantitative costs; they do not supply or invalidate the explicit transition-sharp matched-control lower bound derived here.

No external theorem is load-bearing in `(10)`--`(36)`: the proof uses only the canonical XF-133 analytic packet estimate, the XF-134 transition-sharp pair, the elementary carrier lower bound `(21)`, and Cauchy's integral estimate. The literature search did not locate the specific combination of unit-circle transition controls, complete zero-delay future history, exterior logarithmic jets, and exact common-reference cancellation. No new source dependency is therefore added to `SOURCES.md`.

The theorem does **not** cover derivative orders or derivative weights whose Cauchy cost is itself exponential enough to cancel the margin in `(12)`, nor genuinely global spatial observation beyond the XF-133 aperture class. It also does not establish source accessibility for Xi or a positive upper bound on `Lambda`.

## 7. Consequence for the Xi-flow frontier

XF-134 closed the possibility that a transition functional could simply quotient away the hidden central directions while using the same local function-value patch. XF-135 closes a second nearby escape: passing to the natural logarithmic derivative, taking any jet with `J_N log J_N=o(N)`, or dividing by a common known analytic reference does not restore stable transition identification on the matched-control class.

The q-scale/source-local route must therefore obtain **Xi-specific exclusion of the central packet or a genuinely stronger transition-relevant observable**. In particular, proving a very accurate local Gaussian/reference approximation is not sufficient unless its source error is small in a norm whose discriminant sensitivity beats the exponential lower bound above. Conversely, the result does not kill the accepted Gaussian-reference clue: it sharpens its downstream gate from generic quotient stability to source-restricted transition coercivity.
