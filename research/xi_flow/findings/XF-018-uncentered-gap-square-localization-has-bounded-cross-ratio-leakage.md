# XF-018 — uncentered gap-square localization has a bounded cross-ratio leakage kernel

**Status:** `EXACT-DERIVED` + `CANDIDATE-CARRIER-CHANGE` + `STRUCTURAL/BOUNDARY`. XF-014--XF-017 localize the exact real-simple Xi gap diffusion by first centering the gaps around a reference spacing. That makes the useful bulk coercive, but its cutoff leakage contains `c_{ik}v_iv_k`; controlling it by absolute values therefore needs a lower-gap/conductance bound, because `c_{ik}` can diverge when gaps collapse while `v_i=g_i-h` does not.

There is an exact complementary localization in which this collision singularity disappears. If one localizes the **uncentered gap square** instead, the leakage coefficient is

\[
w_{ik}:=c_{ik}g_i g_k.
\]

For every pair of gaps on an ordered real-simple configuration,

\[
\boxed{0<w_{ik}\le1.}
\]

For nonadjacent gaps the coefficient is a bounded function of the cross-ratio of the four gap endpoints. More precisely, its logarithmic cross-ratio is exactly the continuum Cauchy interaction of the two gap intervals, and `w_{ik}` is dominated by that interaction. The resulting far tails telescope and are controlled by one endpoint gap divided by the intervening span, with no lower bound on the remote gaps.

This does **not** yet produce a localized variance Lyapunov or an upper bound for `Lambda`: on an arithmetic lattice the uncentered constant-gap mode makes dissipation and leakage cancel exactly. The gain is instead a sharp carrier tradeoff. Centering removes the neutral mean mode but exposes singular conductances; delaying the centering renormalizes those conductances into a collision-safe projective kernel, at the price of having to control the mean/span separately.

## 1. Exact uncentered localization identity

On any real-simple slice on which XF-014 applies,

\[
g_i'=2\sum_{k\ne i}c_{ik}(g_k-g_i),
\qquad
c_{ik}=\frac1{(x_i-x_k)(x_{i+1}-x_{k+1})}>0.
\tag{1}
\]

Let `psi_i` be finitely supported and define

\[
E_\psi^{(0)}
:=\frac12\sum_i\psi_i^2g_i^2.
\tag{2}
\]

Using symmetry of `c_{ik}` and

\[
(a-b)(p^2a-q^2b)
=(pa-qb)^2-(p-q)^2ab,
\tag{3}
\]

one obtains the exact identity

\[
\boxed{
\begin{aligned}
\frac{d}{dt}E_\psi^{(0)}
={}&-2\sum_{i<k}c_{ik}
(\psi_i g_i-\psi_k g_k)^2\\
&+2\sum_{i<k}c_{ik}g_i g_k
(\psi_i-\psi_k)^2.
\end{aligned}}
\tag{4}
\]

Thus the uncentered leakage is positive and its geometric coefficient is

\[
\boxed{w_{ik}:=c_{ik}g_i g_k.}
\tag{5}
\]

This is the exact analogue of the centered localization identity in XF-016, but the amplitudes `g_i g_k` now vanish together with collapsing endpoint gaps instead of remaining at the reference scale.

## 2. The conductance singularity renormalizes to a bounded cross-ratio

Fix `i<k` and write

\[
A=x_k-x_i,
\qquad
B=x_{k+1}-x_{i+1}.
\tag{6}
\]

Both denominator factors contain their corresponding endpoint gaps:

\[
A\ge g_i,
\qquad
B\ge g_k.
\]

Hence immediately

\[
\boxed{0<w_{ik}=\frac{g_i g_k}{AB}\le1.}
\tag{7}
\]

For adjacent gaps, `k=i+1`, equality holds: `w_{i,i+1}=1`.

Now suppose `k\ge i+2` and set

\[
C=x_k-x_{i+1},
\qquad
D=x_{k+1}-x_i.
\tag{8}
\]

A direct expansion gives

\[
AB-CD=g_i g_k.
\tag{9}
\]

Therefore, with

\[
\rho_{ik}
:=\frac{AB}{CD}
=\frac{(x_k-x_i)(x_{k+1}-x_{i+1})}
{(x_k-x_{i+1})(x_{k+1}-x_i)}
>1,
\tag{10}
\]

we have

\[
\boxed{
w_{ik}=1-\rho_{ik}^{-1}.
}
\tag{11}
\]

The quantity `rho_{ik}` is one of the standard cross-ratio conventions for the ordered quadruple

\[
x_i<x_{i+1}<x_k<x_{k+1}.
\]

Consequently the nonadjacent leakage weight is invariant under a real Möbius transformation wherever that transformation is defined and preserves the ordering of the four points. This projective invariance belongs only to the renormalized coefficient (11); the Xi zero-motion equation itself is not being claimed Möbius invariant.

Writing

\[
\ell_{ik}:=\log\rho_{ik}>0,
\tag{12}
\]

we get the useful domination

\[
\boxed{w_{ik}=1-e^{-\ell_{ik}}\le\ell_{ik}.}
\tag{13}
\]

Thus the potentially unbounded conductance `c_{ik}` has disappeared from the cutoff error after multiplication by the natural uncentered gap amplitudes.

## 3. The logarithmic cross-ratio is exactly a Cauchy cell interaction

Let

\[
I_i=(x_i,x_{i+1}),
\qquad
I_k=(x_k,x_{k+1})
\]

be two nonadjacent gap intervals. Direct integration yields

\[
\begin{aligned}
\int_{I_i}\int_{I_k}\frac{dy\,dx}{(y-x)^2}
&=
\log\frac{(x_k-x_i)(x_{k+1}-x_{i+1})}
{(x_k-x_{i+1})(x_{k+1}-x_i)}\\
&=\boxed{\ell_{ik}}.
\end{aligned}
\tag{14}
\]

Combining (13) and (14),

\[
\boxed{
w_{ik}
\le
\int_{I_i}\int_{I_k}\frac{dy\,dx}{(y-x)^2}
\qquad(|i-k|\ge2).}
\tag{15}
\]

So the nonlinear leakage kernel is not merely asymptotic to the inverse-square geometry near a lattice. Away from adjacent cells it is a bounded nonlinear compression of the **exact continuum Cauchy interaction between the physical gap intervals**.

On the arithmetic lattice `x_i=ih`, if `n=k-i\ge2`,

\[
\rho_{ik}=\frac{n^2}{n^2-1},
\qquad
\ell_{ik}=\log\frac{n^2}{n^2-1},
\qquad
\boxed{w_{ik}=\frac1{n^2}.}
\tag{16}
\]

Thus the cross-ratio kernel recovers the precise discrete Cauchy weight from XF-008 and XF-016, not merely its order of decay.

## 4. Far tails telescope without a lower-gap hypothesis

The logarithmic cross-ratio has an exact one-dimensional coboundary form. For fixed `i` and `k\ge i+2`, define

\[
f_{i,k}
:=\log\frac{x_k-x_i}{x_k-x_{i+1}}.
\tag{17}
\]

Then

\[
\boxed{\ell_{ik}=f_{i,k}-f_{i,k+1}.}
\tag{18}
\]

Since the Xi zero sequence is unbounded, `f_{i,k}\to0` as `k\to+\infty`. Hence for every integer `L\ge2`, equations (13) and (18) give

\[
\begin{aligned}
\sum_{k\ge i+L}w_{ik}
&\le \sum_{k\ge i+L}\ell_{ik}\\
&=f_{i,i+L}\\
&=\boxed{
\log\left(
1+\frac{g_i}{x_{i+L}-x_{i+1}}
\right)}.
\end{aligned}
\tag{19}
\]

By symmetry, the left tail satisfies

\[
\boxed{
\sum_{k\le i-L}w_{ki}
\le
\log\left(
1+\frac{g_i}{x_i-x_{i-L+1}}
\right).
}
\tag{20}
\]

Equivalently, the entire nonadjacent row obeys

\[
\boxed{
\sum_{|k-i|\ge2}w_{ik}
\le
\log\left(1+\frac{g_i}{g_{i-1}}\right)
+
\log\left(1+\frac{g_i}{g_{i+1}}\right).
}
\tag{21}
\]

These estimates require no pointwise lower bound on remote gaps. What they require for a **uniform** mesoscopic tail bound is more specific: the endpoint gap `g_i` must not dominate the cumulative physical span between it and the remote region. This replaces the pairwise lower-gap condition used as a sufficient hypothesis in XF-017 by a cumulative-span/non-domination condition.

The distinction is genuine. If many intervening gaps collapse while `g_i` remains macroscopic, a distant index can still have `w_{ik}` close to one. Thus (19)--(20) do not magically produce index-space decay from ordering alone; they identify exactly which geometric degeneration destroys it.

## 5. The price is the neutral mean mode

The collision-safe kernel does not make (4) a localized Lyapunov. On an arithmetic lattice `g_i=h`, the gap vector is stationary, while

\[
c_{ik}(\psi_i g_i-\psi_k g_k)^2
=w_{ik}(\psi_i-\psi_k)^2.
\]

Therefore the two terms in (4) cancel pairwise and

\[
(E_\psi^{(0)})'=0.
\tag{22}
\]

This is the exact matched-control that prevents an uncentered square from being mistaken for a coercive fluctuation energy. XF-016 removed this constant mode by replacing `g_i` with `g_i-h`; doing so is precisely what reintroduced the dangerous factor `c_{ik}v_iv_k` into the cutoff leakage.

For a hard finite block `I={a,\ldots,b}` of `N` gaps, however, the mean subtraction can be written separately as

\[
\boxed{
\frac12\sum_{i\in I}(g_i-\bar g_I)^2
=
\frac12\sum_{i\in I}g_i^2
-
\frac1{2N}(x_{b+1}-x_a)^2,
}
\tag{23}
\]

because

\[
\sum_{i=a}^b g_i=x_{b+1}-x_a.
\tag{24}
\]

This does not close the argument: differentiating the span term imports endpoint velocities and hence exterior information. But it isolates a different proof obligation. Instead of bounding singular centered leakage for every pair across a broad buffer, one may try to combine the collision-safe uncentered localization with a source-valid estimate for the block span/endpoint flux. Whether that reorganization is genuinely stronger is now a precise question rather than a heuristic.

## 6. Stress tests, prior art, and novelty boundary

The identities above remain restricted to the real-simple regime of XF-014. At an actual collision the ordered real-simple ODE ceases to be the permitted description. The point of (7) is only that **the localization coefficient itself does not blow up on approach to such a collision**.

The mechanism is universal for ordered one-dimensional logarithmic repulsion. Any matched synthetic system satisfying the same gap equation inherits (4)--(21), so the result is not an Xi-specific selector and by itself says nothing about the sign of `Lambda`.

Cross-ratio invariance is classical, as is the elementary identity expressing the logarithm of a cross-ratio as the double integral (14). A targeted prior-art search across log-gas/Dyson, Calogero, discrete-Schwarzian, and fractional-localization language found the expected broad uses of cross-ratios but did not identify a theorem that already packages the Xi/log-repulsion **uncentered cutoff leakage** as the bounded weight (11) with the tail reduction (19)--(21). Absence from that search is not used as novelty evidence. No new external theorem is load-bearing here, so `SOURCES.md` does not need a new anchor.

The durable contribution is the exact carrier comparison inside the existing Xi-flow program: the lower-gap singularity in the centered cutoff estimate is not intrinsic to the nonlinear gap conductances. It is created by centering before localization. Localizing `g^2` first renormalizes the error to a bounded cross-ratio/Cauchy-cell kernel, but leaves the neutral span mode to be handled separately.

## 7. Consequence for `xi_flow`

XF-017 left a broad-buffer requirement stated in terms of two-sided pair-level conductance and amplitude control. XF-018 shows that this is **not the only possible nonlinear localization interface**. For the uncentered square, the relevant exterior kernel is collision-safe and its remote mass is governed by cumulative physical spans through (19)--(20), not by a uniform lower gap at every intervening site.

The next useful test is therefore sharper. One should ask whether unconditional Xi information in the real-simple regime can control, on `N\asymp\log^2T` cores with a slowly growing outer buffer, the two quantities that the new organization actually needs: large-gap/cumulative-span non-domination for the cross-ratio tails, and the endpoint span term required to remove the neutral mean mode. If those can be bounded at the needed scale, the strong pairwise lower-gap hypothesis of the centered route can be bypassed; if they cannot, the remaining obstruction is source-level large-gap/span information rather than collision singularity of the conductance network.