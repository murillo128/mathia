# XF-003 — the exterior real-zero field slows squared-gap opening at a simple collision

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-MECHANISM`. The zero-motion and gap identities are classical in the de Bruijn--Newman literature, going back to Csordas--Smith--Varga and used explicitly by Rodgers--Tao. The durable line-specific result here is their collision-safe reformulation with XF-002: the universal slope `D'(t_*)=8` acquires a strictly negative second-order correction determined by the exterior real-zero field.

## 1. Claim

Let `H_t` be the de Bruijn--Newman heat deformation in the normalization

\[
\partial_t H_t=-\partial_{zz}H_t.
\]

Suppose `(t_*,z_*)` is a simple double collision,

\[
H_{t_*}(z_*)=H'_{t_*}(z_*)=0,
\qquad
H''_{t_*}(z_*)\ne0,
\]

and that the forward side `t>t_*` is real-rooted. Let `x_-(t)<x_+(t)` be the two adjacent simple real zeros emerging from the collision and set

\[
g(t):=x_+(t)-x_-(t),
\qquad
q(t):=g(t)^2.
\]

On every collision-free interval on which this pair remains adjacent, the classical zero dynamics gives the exact identity

\[
\boxed{
q'(t)=8-4q(t)S(t),
}
\]

where

\[
S(t):=
\sum_{i\notin\{-,+\}}
\frac{1}{(x_i(t)-x_-(t))(x_i(t)-x_+(t))}.
\]

Because the pair is adjacent, every exterior real zero lies on the same side of both endpoints. Hence every summand is positive and

\[
S(t)>0,
\qquad
q'(t)<8.
\]

Thus the free two-body collision `z^2-2t` is the **fastest possible local opening** among real-rooted configurations with the same backward-heat normalization. Any exterior real zeros slow the squared gap rather than accelerate it.

If the pair is born at `t=t_*`, then XF-002 gives `q(t_*)=0` and `q'(t_*)=8`; integrating the strict inequality on the real-simple side yields

\[
\boxed{
0<q(t)<8(t-t_*)
}
\]

for every later time before the pair ceases to belong to the same simple adjacent regime. Equivalently, observing a gap `g(t)` implies the collision-age lower bound

\[
t-t_* > \frac{g(t)^2}{8}.
\]

For the actual de Bruijn--Newman threshold, a simple double collision with real-rooted forward side can only occur at `t_*=\Lambda`: XF-002 makes the pair nonreal immediately to the backward side, so an interior collision with `t_*>\Lambda` would contradict real-rootedness for all `t\ge\Lambda`.

## 2. Exact derivation from the classical gap dynamics

For simple real zeros the heat equation induces the zero-motion law

\[
x_k'(t)=2\sum_{j\ne k}'\frac{1}{x_k(t)-x_j(t)}.
\]

Csordas--Smith--Varga derive this dynamics, and Rodgers--Tao use it as their Theorem 4.1. Their gap identity, recorded as Lemma 4.2(i), is obtained by subtracting the equations for two zeros. For an adjacent pair `x_-<x_+` it reads directly

\[
\begin{aligned}
g'
&=\frac4g
+2\sum_i
\left(
\frac1{x_+-x_i}-\frac1{x_--x_i}
\right)\\
&=\frac4g
-2g\sum_i
\frac1{(x_i-x_-)(x_i-x_+)}\\
&=\frac4g-2gS.
\end{aligned}
\]

The exterior sum is absolutely convergent: after the singular interaction of the chosen pair cancels, the tail is inverse-square in the zero ordinates. Multiplying by `2g` gives

\[
q'=2gg'=8-4qS.
\]

The sign is not an estimate. Adjacency makes

\[
(x_i-x_-)(x_i-x_+)>0
\]

for every exterior zero, including multiplicity, so `S>0` exactly.

This identifies the exterior coupling requested by the decisive test in XF-002. In the squared-gap coordinate it is finite, multiplicative in `q`, and one-sided. The branchwise `|t-t_*|^{-1/2}` velocity singularity from XF-001 has disappeared completely.

## 3. The collision curvature is the inverse-square exterior field

The analytic discriminant `D(t)` from XF-002 equals `q(t)` on the forward real-rooted side and extends analytically through `t_*`. Let

\[
S_*:=
\sum_{i\notin\{-,+\}}
\frac1{(x_i(t_*)-z_*)^2}.
\]

At a simple isolated collision the exterior zeros remain separated from `z_*`, while the inverse-square tail is locally uniformly summable. Hence `S(t)\to S_*` as `t\downarrow t_*`. Since XF-002 gives `q(t_*)=0` and `q'(t_*)=8`, differentiating the collision-safe identity at the endpoint gives

\[
\boxed{
D''(t_*)=q''(t_*)=-32S_*<0.
}
\]

Therefore the local discriminant has the sharper expansion

\[
\boxed{
D(t)
=8\tau-16S_*\tau^2+O(\tau^3),
\qquad
\tau=t-t_*.
}
\]

The first coefficient is universal; the first non-universal coefficient is already a concrete statistic of the rest of the zero configuration. This is the first place in the local collision jet where the environment enters.

The same identity can be read from the Weierstrass factorization used in XF-002. If

\[
H_t(z)=U(t,z)
\bigl((z-z_*)^2+b(t)(z-z_*)+c(t)\bigr),
\]

then direct coefficient comparison with `H_t+H_{zz}=0` gives

\[
D''(t_*)
=32\,\partial_{zz}\log U(t_*,z_*).
\]

For the real-rooted de Bruijn--Newman slice, the canonical product for the exterior factor gives

\[
\partial_{zz}\log U(t_*,z_*)=-S_*.
\]

Thus the local analytic calculation and the classical particle dynamics give the same curvature formula.

## 4. Exact finite matched controls

The two-body polynomial

\[
F_2(t,z)=z^2-2t
\]

solves the same backward heat equation. There are no exterior zeros, so `S=0` and

\[
q(t)=8t
\]

exactly. It saturates the universal opening speed.

A four-body control shows that the negative curvature is not Xi-specific. Start at the collision slice with

\[
F_4(0,z)=z^2(z^2-a^2)
\]

and evolve by the exact backward heat flow. Because the polynomial heat series terminates,

\[
F_4(t,z)
=z^4-(a^2+12t)z^2+2a^2t+12t^2.
\]

At `t=0` the origin is a simple double collision and the exterior zeros are `\pm a`, so

\[
S_* = \frac2{a^2}.
\]

The central pair has squared gap

\[
q(t)=8t-\frac{32}{a^2}t^2+O(t^3),
\]

exactly matching `D''(0)=-32S_*=-64/a^2`.

This control is important epistemically: exterior slowdown is a structural feature of real-rooted backward heat flow, not by itself a selector for the Riemann xi function or an upper bound on `\Lambda`.

## 5. Prior-art and novelty boundary

The zero ODE and gap dynamics are classical. Rodgers--Tao, **The de Bruijn--Newman constant is non-negative**, *Forum of Mathematics, Pi* 8 (2020), e6, state the ODE and explicitly identify the gap identity with Csordas--Smith--Varga, **Lehmer pairs of zeros, the de Bruijn--Newman constant Λ, and the Riemann hypothesis**, *Constructive Approximation* 10 (1994), 107--129, DOI `10.1007/BF01205170`. That literature already exploits close-pair repulsion and the influence of the remaining zeros in lower-bound arguments for `\Lambda`.

Accordingly no novelty is claimed for repulsive gap dynamics, the inverse-square exterior statistic, or the fact that nearby zeros constrain de Bruijn--Newman evolution. The Mathia-specific contribution is the exact bridge to XF-002's collision-safe coordinate: the environment term that was left unresolved there is not singular at a simple collision and has a fixed sign, while its boundary value is exactly the second derivative of the analytic discriminant.

## 6. Boundary conditions and failure modes

The result concerns a simple multiplicity-two collision and the adjacent pair that emerges from it. A higher-multiplicity collision requires a higher-degree Weierstrass polynomial and need not reduce to one squared gap. The inequality `q'<8` also uses that every exterior zero is real and outside the pair interval; it is not valid as a sign argument on the backward side where the colliding pair is nonreal or for an arbitrarily selected non-adjacent pair.

The result does not provide an upper bound on `\Lambda`. Its strongest feature is also its limitation: the sign `S>0` is universal for real-rooted heat-flow configurations. A proof of `\Lambda=0` therefore cannot stop at local collision regularity or repulsion. It must exploit quantitative structure of `S(t)` or another global observable that distinguishes the actual Xi zero field from matched real-entire controls with positive transition time.

A decisive next test is to determine whether the Xi-specific zero statistics available near height `T` impose a quantitative lower or upper law on the normalized exterior field `S` over the microscopic collision time scale. If the same `S` profiles can be realized by matched non-Xi real-zero configurations with positive transition time, then this entire second-order collision jet is insufficient and the line must move to genuinely higher-order or nonlocal information.

## 7. Consequence for `xi_flow`

XF-001 showed that root coordinates become singular at collisions; XF-002 showed that the discriminant removes that coordinate singularity. The present result settles the first exterior-coupling question left open there: in the collision-safe variable the rest of the real zero set contributes a finite damping term

\[
-4qS,
\]

not a new singularity, and its collision-limit curvature is strictly negative.

The local problem is therefore no longer "can the collision be crossed without infinite zero speed?" At simple collisions it can be described analytically and with a one-sided exterior correction. The live frontier is whether the **size and organization of the exterior field** contain enough Xi-specific information to constrain when such a collision can occur.