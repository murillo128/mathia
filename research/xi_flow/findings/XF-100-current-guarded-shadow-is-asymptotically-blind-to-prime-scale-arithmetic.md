# XF-100 — current guarded shadow is asymptotically blind to prime-scale arithmetic

**Status:** `EXACT-DERIVED` + `SOURCE-SPECIFIC-BOUNDARY` + `FIXED-TIME-PRIME-BLINDNESS` + `BANDWIDTH-PHASE-BOUNDARY`. XF-099 shows that a macroscopic periodic collision crystal can remain exactly invisible to every current guarded mode because its first nonzero power sum sits at the symmetry frequency `m=M`, far above the live cutoff `K=o(M)`. One obvious response is to use Xi's explicit-formula prime frequencies as an anti-aliasing certificate. At the current source-to-periodic scales, that response cannot work inside the existing guarded cone.

The reason is stronger than endpoint prime-freeness. Let

\[
\lambda_2:=\frac{\log 2}{2},
\qquad
\xi_m=m\Delta,
\qquad
M=q^2,
\qquad
N=2M,
\qquad
\Delta^2\asymp q^{-3},
\tag{1}
\]

and keep the XF-097 bandwidth

\[
K\asymp q\log\log T.
\tag{2}
\]

Then `K Delta -> 0`, so all endpoint samples through `K` lie below `lambda_2`. XF-052 therefore makes the **entire initial prefix**

\[
Q_m(0)=\mathcal Z_0(m\Delta)=B(m\Delta),
\qquad 1\le m\le K,
\tag{3}
\]

purely archimedean/polar: no prime-power datum appears anywhere in that vector. XF-097 realizes exactly this whole vector by an `N`-node real periodic divisor and proves that its exact periodic heat trajectory `P(t)` shadows the actual Xi samples `Q(t)` in the guarded resource for every fixed `0<=t<=1/2`:

\[
\boxed{
\sup_{0\le t\le1/2}
\mathcal R_{[J,K]}(P(t)-Q(t))=o(1).
}
\tag{4}
\]

But the periodic prefix is itself an exact autonomous system. By XF-087,

\[
P_m'
=
\xi_m^2P_m
-
\xi_m\Delta
\left[
\frac12P_0P_m+
\sum_{i=1}^{m-1}P_iP_{m-i}+
\frac12P_mP_0
\right],
\tag{5}
\]

so the evolution of `(P_1,...,P_K)` uses no mode above `K`. Hence the full fixed-time trajectory on the right side of `(4)` is determined by the prime-free endpoint vector `(3)` alone. Combining `(3)`--`(5)` gives the main conclusion:

\[
\boxed{
\text{throughout the current guarded cone, the actual Xi trajectory is }o(1)
\text{-close to a fixed-time trajectory generated from no prime data.}
}
\tag{6}
\]

This does **not** say that the exact continuum field below `lambda_2` is globally independent of the prime spectrum at positive time. XF-053 deliberately left that stronger nonperturbative statement open. Equation `(6)` is the statement actually needed by the present architecture: after XF-097, any such nonperturbative high-to-low effect is below the resolution of the current guarded norm on the whole fixed heat interval.

Consequently, the suggestion left open by XF-099 — use the explicit-formula prime spectrum to break the collision-crystal aliasing **without changing the present bandwidth/interface** — is unavailable. To make prime arithmetic directly visible one must cross a new bandwidth scale, and the current source-to-grid proof does not survive that crossing.

## 1. The first prime sits parametrically above the whole live Vieta prefix

The first arithmetic atom of the endpoint explicit formula is at `lambda_2`. On the periodic mesh, its index scale is

\[
m_2:=\frac{\lambda_2}{\Delta}.
\tag{7}
\]

Since `Delta\asymp q^{-3/2}`,

\[
\boxed{
m_2\asymp q^{3/2}.}
\tag{8}
\]

The existing live cutoff instead satisfies

\[
K\asymp q\log\log T,
\]

and therefore

\[
\boxed{
\frac{K}{m_2}
\ll q^{-1/2}\log\log T
\longrightarrow0.
}
\tag{9}
\]

Thus the separation is not a constant-factor accident. The current guarded architecture observes a vanishing fraction of the Fourier index needed merely to reach the first prime-power frequency. Every endpoint sample used by the XF-097 exact real-carrier construction lies in the prime-free interval of XF-052.

The distinction between **prime-free** and **small** is important. The background values are not zero; near the endpoint,

\[
B(\xi)=-\frac1{4\xi}+\frac74+O(\xi).
\tag{10}
\]

So the current prefix still contains a large deterministic archimedean profile. What it does not contain is arithmetic information capable of distinguishing two states by their prime-power spectrum. XF-097 already shows that this full background prefix is compatible with an exact finite real periodic divisor.

## 2. The periodic heat flow cannot pull hidden higher modes into the prefix

Equation `(5)` gives an exact finite-dimensional domain-of-dependence statement. Suppose two periodic heat trajectories `P` and `\widetilde P` have the same node count `N` and satisfy

\[
P_m(0)=\widetilde P_m(0),
\qquad 1\le m\le K.
\tag{11}
\]

Then

\[
\boxed{
P_m(t)=\widetilde P_m(t),
\qquad 1\le m\le K,
}
\tag{12}
\]

for every common heat time on which the polynomial trajectories are defined, regardless of every initial power sum above `K`.

The proof is triangular and collision-safe. For `m=1`, the right side of `(5)` depends only on `P_1` and the fixed `P_0=N`, so uniqueness of the scalar ODE gives equality. Assuming equality through `m-1`, subtract the two `m`-equations. Every convolution term contains either the difference in mode `m` itself or a lower difference already equal to zero. The resulting linear homogeneous ODE for `P_m-\widetilde P_m`, with zero initial datum, gives `(12)`. No root labels, simplicity, or real-root interval are used.

This exact autonomy generalizes the symmetry calculation in XF-099. The collision crystal is not invisible merely because its particular formula happens to preserve `P_m=0` for `m<M`; **every** change confined to higher periodic Vieta data is causally unable to descend into the prefix under the exact periodic heat flow.

Accordingly, adding a hidden high-frequency certificate to the finite carrier does not help unless the observable bandwidth itself reaches that certificate. Heat evolution supplies no down-conversion mechanism in these one-sided coordinates.

## 3. XF-097 transfers this exact blindness to the actual Xi trajectory at guarded resolution

The possible loophole is that the exact Xi continuum flow is not literally the finite trapezoid system. XF-097 closes precisely that loophole at the current scales. It constructs the periodic initial state from the **whole** Xi prefix `(3)`, not only from the guarded block, and proves the fixed-time error `(4)` after retaining the endpoint counterterm of XF-088 and the positive-time regularity of XF-095--XF-096.

Let `P^B(t)` denote that periodic trajectory, emphasizing that its first `K` initial moments are the deterministic background samples `B(m Delta)`. By the autonomy just proved, the vector

\[
(P_1^B(t),\ldots,P_K^B(t))
\tag{13}
\]

is a deterministic functional only of those `K` prime-free numbers and of the fixed parameters `N,Delta`. Any choice of higher moments compatible with the real equal-weight realization gives the same prefix trajectory.

Equation `(4)` can therefore be rewritten as the source-specific approximation

\[
\boxed{
\sup_{0\le t\le1/2}
\mathcal R_{[J,K]}
\left(
(Q_m(t)-P_m^B(t))_{m=J}^K
\right)
=o(1).
}
\tag{14}
\]

This is the appropriate nonperturbative replacement for the finite-jet statement of XF-053. XF-053 proved that every fixed heat jet below `lambda_2` is prime-independent but could not sum the shrinking-band Taylor series. XF-097 later bypassed that uniform-analyticity problem by a real periodic shadow plus direct fixed-time stability. The consequence `(14)` is not exact continuum spectral independence, but it is stronger for the present goal: any prime-dependent contribution that survives in the actual Xi samples has `o(1)` size in the exact guarded norm being used downstream.

A proposed transition coercivity theorem can still exploit the deterministic background geometry itself. What `(14)` rules out is using **prime-scale arithmetic as the missing anti-aliasing input while keeping the same guarded state space and cutoff**. At that resolution the prime information has already been quotiented below `o(1)`.

## 4. Reaching the first prime is a genuine bandwidth phase change

To sample frequencies of order `lambda_2`, one needs

\[
K_{\rm prime}\asymp \Delta^{-1}\asymp q^{3/2},
\tag{15}
\]

rather than the present `K\asymp q log log T`. This is not a harmless enlargement inside the proof of XF-097. Two of its small parameters immediately cease to be small.

First, the triangular stability coefficient used there is

\[
K\Delta\log(K+1).
\tag{16}
\]

At `(15)`,

\[
\boxed{
K_{\rm prime}\Delta\log K_{\rm prime}
\asymp \log q,
}
\tag{17}
\]

instead of `o(1)`. The fixed-time bootstrap that propagates the continuum/trapezoid error therefore no longer closes by the existing argument.

Second, the corrected endpoint state/sampling contribution isolated in XF-095--XF-097 contains

\[
\frac{\Delta^4K^9}{M^2}
\tag{18}
\]

up to polylogarithmic factors. With `Delta^2\asymp q^{-3}`, `M=q^2`, and `(15)`,

\[
\boxed{
\frac{\Delta^4K_{\rm prime}^9}{M^2}
\asymp q^{7/2},
}
\tag{19}
\]

rather than tending to zero. This does not prove that prime-scale shadowing is impossible; it proves that the current perturbative norm and bookkeeping are parametrically the wrong tool there.

There is an additional source-interface change before one even attempts the stability proof. At and beyond `lambda_2`, XF-052 represents the endpoint arithmetic sector by **distributional prime-power atoms**, not by an ordinary smooth function that can simply be evaluated at every mesh point. The full-prefix point-sample realization in XF-097 was legal precisely because `K Delta<lambda_2`. Crossing `(15)` therefore requires a smoothed atomic extraction, a modified sideband observable, or another source-to-moment interface; the current formula `Q_m(0)=Z_0(m Delta)` cannot simply be extended through the prime spectrum.

Hence `K\sim q^{3/2}` is a real architectural boundary, not merely a more expensive value of the existing cutoff.

## 5. Stress tests and falsification controls

The claim is intentionally narrower than an exact support theorem for the continuum Xi flow. Several checks prevent overreading it.

**Low-to-high transport is allowed.** One-sided Volterra convolution can create frequencies larger than those present in an input by addition. The statement is only that higher periodic modes cannot move downward into an autonomous prefix, and that the actual Xi prefix is already shadowed by that finite autonomous system at guarded resolution.

**The endpoint background is retained.** Equations `(3)` and `(10)` are not a claim that the source prefix vanishes. The real carrier of XF-097 matches the entire singular background prefix exactly at `t=0`; the new conclusion is only absence of prime-power information from the data generating its low-mode trajectory.

**No exact positive-time continuum prime-free theorem is asserted.** XF-053's nonperturbative continuum question remains logically distinct. If a future calculation exhibits a prime-dependent contribution below `lambda_2` at fixed positive time, it would not contradict this finding unless that contribution has nonvanishing XF-086 guarded resource on the canonical band, because `(14)` says such a contribution must be guarded-small under the already-proved XF-097 shadow estimate.

**The first prime boundary is open.** At exactly `lambda_2` the explicit formula has an atomic term, so ordinary pointwise sampling is not the correct operation. Statements here about the smooth prime-free endpoint field are restricted to frequencies strictly below that boundary.

**The collision crystal is not declared Xi-compatible.** XF-099 remains a synthetic obstruction to universal coercivity. This finding only shows that direct prime-frequency anti-aliasing cannot distinguish it inside the present low-frequency guarded coordinates; Xi may still exclude it through another source-specific geometric or analytic mechanism.

## 6. Prior-art and novelty boundary

No new external theorem is load-bearing. The prime-frequency gap and endpoint background are already anchored by the Guinand--Weil explicit-formula sources in `SOURCES.md` through XF-048/XF-052. One-sided convolution support and the high-support ideal were already audited and derived internally in XF-051/XF-053. The exact periodic triangular system is XF-087, and the fixed-time source-to-periodic shadow is XF-097.

The durable Mathia delta is the scale-matched consequence of combining those previously separate facts with the XF-099 aliasing obstruction: **the current guarded Xi trajectory is asymptotically shadowed for fixed heat time by a finite trajectory generated entirely from the prime-free endpoint prefix, while the first arithmetic frequency lives at index `Theta(q^{3/2})`, beyond both the current cutoff and the regime of the present shadow proof.** No `SOURCES.md` update is required.

## 7. Boundary for the next pass

The destination problem now has a cleaner fork. One route is to stay at the current `K\asymp q log log T` and find a genuinely Xi-specific transition constraint that operates on the deterministic low-frequency/archimedean state already present there; prime atoms cannot be invoked as hidden data that heat will later bring into the cone. The other route is to redesign the source-to-grid observable so that it reaches `xi=Theta(1)`, beginning at `lambda_2`, while handling atomic explicit-formula data and replacing the XF-097 small-`K Delta` stability argument.

A useful next falsification target is therefore sharp: determine whether the **archimedean low-frequency trajectory itself**, together with the existence of a positive de Bruijn--Newman transition, forces nonvanishing distance from the collision-invisible periodic cone. A negative matched control at that level would close the current low-band strategy; a positive coercive inequality would attack exactly the remaining `Lambda>0` gate without pretending that prime information is already visible.