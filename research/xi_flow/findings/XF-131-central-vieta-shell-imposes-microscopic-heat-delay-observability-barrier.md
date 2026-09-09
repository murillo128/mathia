# XF-131 — central Vieta shell imposes a microscopic heat-delay observability barrier

**Status:** `EXACT-DERIVED` + `NEGATIVE/CONDITIONING-BOUNDARY` + `MATCHED-CONTROL` + `TEMPORAL-OBSERVABILITY` + `TRANSITION-SHARP`. XF-130 proves that one normalized off-circle heat trace determines the complete periodic unit-circle divisor exactly, with only `O(N)` spatial reflected-shell conditioning when the probe is one root spacing off the real line. That leaves a separate question: how much heat-time delay can be tolerated before the collision-sensitive information in that trace becomes too small to transfer stably from the actual Xi source?

For even degree `N=2M`, the answer has an exact worst-case model. The central Vieta shell `k=M` alone supports a one-parameter family whose periodic Newman transition time can be prescribed exactly, while its contribution to the XF-130 trace is damped at the **largest** normalized heat rate

\[
\boxed{
\delta_M
=\frac{4\pi^2}{L^2}M(N-M)
=\frac{\pi^2N^2}{L^2}.
}
\tag{1}
\]

For every `rho>=0`, define

\[
\boxed{
E_\rho(w,0)
:=1-2e^{-\delta_M\rho}w^M+w^{2M}.
}
\tag{2}
\]

All zeros of `(2)` lie on the unit circle at the target slice. Its normalized XF-067 heat evolution is

\[
E_\rho(w,s)
=1-2e^{-\delta_M(\rho+s)}w^M+w^{2M},
\tag{3}
\]

and its periodic transition time is exactly

\[
\boxed{
\Lambda_{\rm per}(E_\rho)=-\rho.
}
\tag{4}
\]

At `rho=0`, every one of the `N` root slots belongs to a double collision at `s=0`; for every `rho>0`, all roots are simple there. Nevertheless, if the one-point trace is observed only after a delay `s_0>0`, then for the collision control `rho=0` and any comparison `rho>0`,

\[
\boxed{
\left\|Q_{\zeta,0}-Q_{\zeta,\rho}\right\|_{L^\infty([s_0,\infty))}
=2\bigl(1-e^{-\delta_M\rho}\bigr)|\zeta|^M e^{-\delta_Ms_0}.
}
\tag{5}
\]

At the XF-130 root-spacing probe `|zeta|=e^{sigma/N}`, the factor `|zeta|^M=e^{sigma/2}` is fixed. Thus a delayed trace can distinguish these targets exactly at infinite precision, but any quantitatively stable reconstruction of collision geometry or transition time pays an unavoidable factor `exp(delta_M s_0)`. The natural temporal clock of the one-channel observable is therefore

\[
\boxed{
\tau_{\rm cent}:=\delta_M^{-1}
=\frac{L^2}{\pi^2N^2},
}
\tag{6}
\]

which is the square of the mean root-spacing scale up to the fixed factor `pi^{-2}`. At the current Xi scaling `L/N\asymp1/\log T`, this is `Theta(1/log^2 T)`.

This does **not** contradict XF-130's exact identifiability. It identifies the previously open temporal-conditioning boundary: one root-spacing of spatial displacement is enough algebraically, but a heat delay much larger than `(6)` erases the fastest collision-sensitive shell exponentially before source/localization error is taken into account.

## 1. The central-shell family has an exactly computable transition

Put

\[
q_\rho(s):=e^{-\delta_M(\rho+s)}
\tag{7}
\]

and set `x=w^M`. Equation `(3)` becomes

\[
x^2-2q_\rho(s)x+1=0.
\tag{8}
\]

When `rho+s>0`, one has `0<q_rho(s)<1`, so the two roots of `(8)` are

\[
x_\pm
=q_\rho(s)\pm i\sqrt{1-q_\rho(s)^2},
\qquad |x_\pm|=1.
\tag{9}
\]

They are distinct, and each has `M` distinct `M`th roots on the unit circle. Thus all `N=2M` roots of `E_rho(.,s)` are simple and unimodular.

At the boundary `s=-rho`, `q_rho(s)=1` and

\[
E_\rho(w,-\rho)
=(1-w^M)^2.
\tag{10}
\]

There are exactly `M` distinct unit-circle locations, each with multiplicity two. Every root slot participates in a collision.

For `s<-rho`, `q_rho(s)>1`; the two roots of `(8)` are positive real reciprocals, one larger than one and one smaller than one. Their `M`th roots therefore lie on two reciprocal circles of radii different from one. Hence the divisor is not unit-circle-real in the periodic coordinate. This proves `(4)` directly, without invoking any root-motion formula at the collision.

The family `(2)` is consequently more than a conditioning toy. Its parameter `rho` is exactly minus the periodic transition time. It gives an explicit fiber through the discriminant on the same coefficient heat flow used by XF-067--XF-130.

## 2. Heat delay exponentially suppresses a fixed transition-time difference

For the XF-130 observable

\[
Q_{\zeta,\rho}(s):=E_\rho(\zeta,s),
\tag{11}
\]

equation `(3)` gives

\[
Q_{\zeta,\rho}(s)
=1-2e^{-\delta_M(\rho+s)}\zeta^M+\zeta^{2M}.
\tag{12}
\]

Therefore, for any `rho_1,rho_2>=0`,

\[
Q_{\zeta,\rho_1}(s)-Q_{\zeta,\rho_2}(s)
=-2\left(e^{-\delta_M\rho_1}-e^{-\delta_M\rho_2}\right)
\zeta^M e^{-\delta_Ms}.
\tag{13}
\]

The modulus decreases monotonically with `s`, so restriction to `s>=s_0` yields the exact norm

\[
\boxed{
\left\|Q_{\zeta,\rho_1}-Q_{\zeta,\rho_2}\right\|_\infty
=2\left|e^{-\delta_M\rho_1}-e^{-\delta_M\rho_2}\right|
|\zeta|^M e^{-\delta_Ms_0}.
}
\tag{14}
\]

Taking `rho_1=0` proves `(5)`. This comparison is especially strong because its target difference need not shrink with degree. Fix any `rho>0`. Then

\[
\Lambda_{\rm per}(E_0)-\Lambda_{\rm per}(E_\rho)=\rho,
\tag{15}
\]

while their delayed traces differ by only the exponentially damped amount `(5)`. If `delta_M rho` is large, the prefactor `1-e^{-delta_M rho}` is already close to one; the smallness comes entirely from the observation delay.

At the root-spacing radial probe

\[
|\zeta_N|=e^{\sigma/N},
\qquad \sigma\ne0\ \text{fixed},
\tag{16}
\]

one has exactly

\[
|\zeta_N|^M=e^{\sigma/2}.
\tag{17}
\]

Thus moving the spatial observation point one root spacing off the circle neither creates nor repairs the exponential temporal loss. XF-130's `O(N)` reflected-shell inversion and the present `e^{delta_M s_0}` temporal conditioning are genuinely different costs.

## 3. Exact minimax stability lower bound

The instability can be stated without choosing a reconstruction algorithm. Equip delayed traces with the sup norm on `[s_0,infinity)`. Suppose an observation may have additive error bounded by `eta` in that norm. The two closed error balls around `Q_{zeta,0}` and `Q_{zeta,rho}` intersect whenever

\[
2\eta
\ge
\left\|Q_{\zeta,0}-Q_{\zeta,\rho}\right\|_\infty.
\tag{18}
\]

Indeed their midpoint belongs to both balls. Therefore no estimator can, uniformly over this two-point admissible family, distinguish transition time `0` from transition time `-rho` under errors satisfying `(18)`. A necessary robust-resolution condition is

\[
\boxed{
\eta
<
\bigl(1-e^{-\delta_M\rho}\bigr)|\zeta|^M e^{-\delta_Ms_0}.
}
\tag{19}
\]

Equivalently, any map from exact delayed traces to `Lambda_per` that is Lipschitz on this pair must have Lipschitz constant at least

\[
\boxed{
\operatorname{Lip}
\ge
\frac{\rho}{2(1-e^{-\delta_M\rho})|\zeta|^M}
 e^{\delta_Ms_0}.
}
\tag{20}
\]

This is an exact lower bound, not a heuristic appeal to generic backward-heat ill-posedness.

A useful scale consequence follows immediately. If the source-to-periodic trace is known only to polynomial accuracy `eta_N=N^{-A}` and `rho` is fixed so that `1-e^{-delta_M rho}` is bounded below, then `(19)` requires, up to fixed constants,

\[
\boxed{
\delta_Ms_0\lesssim A\log N,
\qquad
s_0\lesssim A\,\tau_{\rm cent}\log N.
}
\tag{21}
\]

To preserve an order-one collision-sensitive contrast one needs the sharper `s_0=O(tau_cent)`. Delays much larger than `tau_cent log N` suppress the central-shell signal beyond every fixed inverse power of `N`.

## 4. Why the central shell is the unavoidable worst temporal direction

Under the XF-067 normalized coefficient flow,

\[
\delta_k=\frac{4\pi^2}{L^2}k(N-k).
\tag{22}
\]

For `0<=k<=N`, this is maximized exactly at the center. When `N=2M`,

\[
\delta_M=\max_k\delta_k.
\tag{23}
\]

The family `(2)` isolates that fastest direction while retaining a complete root-geometric interpretation: it crosses the unit-circle discriminant exactly when the central coefficient reaches magnitude `2`. Thus the shell responsible for the worst heat-time conditioning is not an algebraically irrelevant coefficient. It can by itself encode the periodic transition time and an all-slots double collision.

This also explains why more patient observation at large positive heat time does not help. The slow shells are easier to recover from heat tails, but this collision control places the transition information entirely in the fastest shell. Any target-independent stable theorem must therefore control the central shell rather than infer it from slower asymptotics.

Finite differentiation at a delayed time does not remove the basic obstruction without paying the same inverse-heat cost. The `r`th time derivative of the difference `(13)` gains only the explicit factor `delta_M^r` while retaining `e^{-delta_Ms_0}`. For any fixed derivative order, or any regime in which derivative measurement errors are not correspondingly exponentially small, the central-shell loss remains exponential.

## 5. Prior-art boundary

The broad phenomenon that backward recovery for the heat equation is exponentially ill-conditioned is classical, and modern inverse-heat/source-identification work continues to formulate that instability explicitly. Likewise, conditions for self-inversive polynomials to have all zeros on the unit circle are classical. A directed audit against those literatures did not reveal a theorem needed for the argument above.

The proof here is elementary once XF-067 and XF-130 are in place: the trinomial reduces to the quadratic `(8)`, and the heat trace difference is the single central exponential `(13)`. No external result is load-bearing, so this finding does not add a new `SOURCES.md` dependency.

The line-specific contribution is the exact alignment of three quantities inside the current Xi-flow periodic interface: the collision discriminant, the periodic transition parameter, and the fastest Vieta heat rate. That alignment produces the sharp delayed-observation lower bound `(19)` and fixes the heat clock that any source-transfer theorem must respect.

## 6. Consequences and boundaries for the Xi source bridge

This finding narrows, but does not resolve, the accepted Gaussian-reference/source-localization route. XF-130 reduced periodic collision observability to one normalized complex trace at vertical displacement `Theta(L/N)`. XF-131 now shows that a source-faithful transfer of that trace must also specify **when** in heat time it is accurate. A relative localization estimate valid only after a positive delay `s_0` is not enough by itself: its error must beat the central-shell threshold `(19)`.

At the current Xi root-spacing scale

\[
\frac LN\asymp\frac1{\log T},
\tag{24}
\]

equation `(6)` becomes

\[
\tau_{\rm cent}\asymp\frac1{\log^2T}.
\tag{25}
\]

Thus a fixed positive heat delay would require trace accuracy on the order of `exp(-Theta(log^2 T))` in this worst-case periodic family. Polynomial-in-`N` accuracy permits only the logarithmically enlarged window `(21)`. Any claimed Xi transfer should therefore state its heat-time offset and compare its normalized error to this explicit central-shell scale.

There are several legitimate escape routes, none established here. A source theorem may access the normalized trace essentially at the target slice; it may prove exponentially stronger relative accuracy than current polynomial conditioning suggests; it may construct a preconditioned observable that rescales the central heat mode before source error enters; or Xi-specific structure may rule out the central-shell matched family. What is ruled out is treating XF-130's exact full-history identifiability as automatically stable under an uncontrolled positive heat delay.

The result is also deliberately finite-periodic. It does not assert that the actual Xi divisor realizes `(2)`, does not give an upper bound on the true de Bruijn--Newman constant, and does not convert periodic transition coercivity into an Xi theorem. Its role is to expose a precise source-access requirement that any such conversion must overcome.