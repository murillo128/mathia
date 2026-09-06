# XF-071 — guarded log-Vieta quotient blocks ultra-infrared repopulation

**Status:** `EXACT-DERIVED` + `WEIGHTED-QUOTIENT-TRANSPORT` + `COLLISION-SAFE` + `STRUCTURAL/BRIDGE`. XF-069 shows that the Xi source selector cannot reach the fixed Vieta modes, while XF-070 shows that those same ultra-infrared modes have vanishing weight in the destination-matched `H^3` resource. The remaining algebraic concern is nonlinear: even if the unseen modes are harmless initially, could the exact periodic heat flow mix them back into the source-visible/destination-relevant band and recreate order-one weighted energy?

On the periodic model, the answer is no once one leaves a growing guard band. The formal logarithm of the normalized Vieta polynomial obeys an exact triangular Burgers system. An unknown block `m<J` with merely bounded log-Vieta coefficients can generate higher positive modes only through additive convolution, and the small coefficient `4 pi^2/L^2 = Theta(q^{-3})` makes this cascade perturbative on the Xi window. If the source-visible weighted `H^3` resource on `J<=m<=K` is `o(1)`, then after any fixed positive heat time the resource on a farther band `J_+<=m<=K` is still `o(1)`, even though the raw coefficients below `J` may remain order one.

A concrete choice matches the existing selector/frame architecture exactly:

\[
J=q^{1/4},\qquad
J_+=q^{1/2},\qquad
K\asymp q\log\log T,\qquad
M=q^2,\qquad N=2M.
\tag{1}
\]

Thus XF-059 may be invoked with source exponent `delta=1/4`, while the standard XF-062--XF-066 destination band starts at the larger `q^{1/2}` Vieta index. The interval between them is not wasted resolution: it is a **nonlinear guard band** that prevents the source-unresolved ultra-infrared sector from contaminating the transition resource at fixed heat time.

This closes the algebraic weighted-quotient transport problem left by XF-069--XF-070 for the periodic carrier. It does **not** prove the nonperiodic Xi-to-periodic interface estimate or prove that a positive-`Lambda` transition supplies an order-one destination state. Those remain the load-bearing Xi-specific steps.

## 1. The exact log-Vieta flow is a triangular Burgers system

Use the periodic heat coordinates of XF-067. Normalize the Vieta polynomial so that

\[
E(z,t)=\sum_{k=0}^N E_k(t)z^k,
\qquad E_0(t)=1,
\tag{2}
\]

and put

\[
a:=\frac{4\pi^2}{L^2}.
\tag{3}
\]

XF-067 gives

\[
E_k'=-a k(N-k)E_k.
\tag{4}
\]

With `D=z partial_z`, equation (4) is exactly

\[
\partial_tE=a(D^2-ND)E.
\tag{5}
\]

Now take the **formal** logarithm at `z=0`, which needs no analytic branch because `E_0=1`:

\[
C(z,t):=\log E(z,t)
=\sum_{m\ge1}c_m(t)z^m.
\tag{6}
\]

By the Newton generating identity used in XF-068--XF-070,

\[
\boxed{
c_m=(-1)^{m-1}\frac{P_m}{m}.\ }
\tag{7}
\]

Dividing (5) by `E=e^C` gives

\[
\boxed{
\partial_tC
=a\left(D^2C-NDC+(DC)^2\right).
}
\tag{8}
\]

Therefore, for every `1<=m<=N`,

\[
\boxed{
 c_m'
 =-a m(N-m)c_m
 +a\sum_{i=1}^{m-1}i(m-i)c_i c_{m-i}.
}
\tag{9}
\]

This identity is exact at finite amplitude. More importantly for the quotient problem, it is **one-sided in positive Vieta index**: the equation for `c_m` uses only `c_1,...,c_m`. No coefficient above `m` can replenish a lower mode, and an ultra-infrared block can reach a distant positive mode only through repeated additive convolution.

Equation (9) is coefficient-level and therefore survives root collisions and intervals with complex roots. Root labels, gap denominators, and a discriminant lower bound never enter.

## 2. A bounded infrared block keeps an exponentially small guarded tail

Fix a truncation `K<N` and an infrared cutoff `J`, and let `u_m(t)` solve (9) for `1<=m<=K` with initial data

\[
u_m(0)=c_m(0)\quad(1<=m<J),
\qquad
u_m(0)=0\quad(J<=m<=K).
\tag{10}
\]

Assume only

\[
|c_m(0)|\le A,
\qquad 1\le m<J.
\tag{11}
\]

This is precisely the type of information available from a bounded-displacement real periodic state: XF-070 gives `|P_m|<=2 pi A_* m`, hence (7) gives `|c_m|<=2 pi A_*`. But the argument below only needs (11), not root reality.

Set

\[
r=e^{1/J},
\qquad
U_r(t):=\sum_{m=1}^K |u_m(t)|r^m.
\tag{12}
\]

The linear part of (9) is dissipative for `m<N`. Taking upper Dini derivatives and dropping that favorable term yields

\[
\begin{aligned}
U_r'
&\le
 a\sum_{i+j\le K}ij|u_i||u_j|r^{i+j}\\
&\le a\left(\sum_{m=1}^K m|u_m|r^m\right)^2
\le aK^2U_r^2.
\end{aligned}
\tag{13}
\]

Initially,

\[
U_r(0)
\le A\sum_{m<J}e^{m/J}
\le eAJ.
\tag{14}
\]

Hence for every fixed `tau_0>0`, if

\[
a\tau_0K^2AJ=o(1),
\tag{15}
\]

then uniformly for `0<=t<=tau_0`,

\[
\boxed{U_r(t)\le 2eAJ}
\tag{16}
\]

for all sufficiently large scales. Since

\[
\sum_m m^p|u_m|
\le
\left(\sup_{m\ge1}m^pe^{-m/J}\right)U_r,
\tag{17}
\]

(16) gives, for each fixed `p`,

\[
\boxed{
\sum_{m=1}^K m^p|u_m(t)|
\ll_p A J^{p+1}.
}
\tag{18}
\]

If `J_+/J->infinity` and eventually `J_+>=3J`, the same analytic weight gives the guarded `H^3` tail

\[
\boxed{
\left(
\sum_{m=J_+}^K m^6|u_m(t)|^2
\right)^{1/2}
\ll
A J J_+^3 e^{-J_+/J}.
}
\tag{19}
\]

Thus an order-one unknown infrared block does not merely have small destination weight at the initial time. Under the **full nonlinear periodic heat flow**, the part it creates beyond a growing guard band is exponentially small in `J_+/J`.

## 3. Source-visible weighted energy is stable against the unknown low block

Write the actual logarithmic state as

\[
c=u+v.
\tag{20}
\]

By construction `v_m(0)=0` for `m<J`. Triangularity of (9) then gives

\[
\boxed{v_m(t)=0\qquad(1\le m<J)}
\tag{21}
\]

for the whole interval of existence. Subtracting the equations for `c` and `u`,

\[
v_m'
=-a m(N-m)v_m
+a\bigl(B(u,v)_m+B(v,u)_m+B(v,v)_m\bigr),
\tag{22}
\]

where

\[
B(a,b)_m:=\sum_{i+j=m}ij\,a_i b_j.
\tag{23}
\]

Use the unnormalized positive-frequency `H^3` norm

\[
H_3(v):=
\left(\sum_{m=J}^K m^6|v_m|^2\right)^{1/2}.
\tag{24}
\]

The elementary inequality `(i+j)^3<=4(i^3+j^3)` and Young's convolution inequality give

\[
\|B(u,v)\|_{H^3}
+\|B(v,u)\|_{H^3}
\ll
A KJ^2 H_3(v).
\tag{25}
\]

Indeed, (18) with `p=1,4` gives

\[
\sum i|u_i|\ll AJ^2,
\qquad
\sum i^4|u_i|\ll AJ^5,
\tag{26}
\]

while the support property (21) gives

\[
\|m v_m\|_2\le J^{-2}H_3(v),
\qquad
\|m^4v_m\|_2\le K H_3(v).
\tag{27}
\]

The visible-visible interaction is also tame because the visible block starts at the growing index `J`:

\[
\boxed{
\|B(v,v)\|_{H^3}
\ll
KJ^{-3/2}H_3(v)^2.
}
\tag{28}
\]

For example,

\[
\sum_{m\ge J}m|v_m|
\le
\left(\sum_{m\ge J}m^{-4}\right)^{1/2}H_3(v)
\ll J^{-3/2}H_3(v),
\tag{29}
\]

and `\|m^4v_m\|_2<=KH_3(v)`.

The diagonal term in (22) is nonpositive in the `H^3` energy. Therefore (25)--(28) imply

\[
\boxed{
\frac{d}{dt}H_3(v)
\le
C aAKJ^2H_3(v)
+C aKJ^{-3/2}H_3(v)^2
}
\tag{30}
\]

in the upper-Dini sense, with an absolute numerical `C` after fixing the harmless convolution constants.

Normalize by the XF-070 destination scale,

\[
X(v):=\frac{H_3(v)}M.
\tag{31}
\]

Then

\[
\boxed{
X'
\le
C aAKJ^2X
+C aKMJ^{-3/2}X^2.
}
\tag{32}
\]

This is the quantitative quotient estimate. The first coefficient measures coupling from the unknown infrared block; the second measures self-interaction of the source-visible quotient. Both vanish on the Xi scaling below.

## 4. The existing `delta=1/4` source band and `delta=1/2` destination band leave a sufficient guard

Use

\[
M=q^2,
\qquad
N=2q^2,
\qquad
s^{-2}\asymp q,
\qquad
L=Ns,
\tag{33}
\]

so that

\[
a=\frac{4\pi^2}{L^2}\asymp q^{-3}.
\tag{34}
\]

Take

\[
J\asymp q^{1/4},
\qquad
J_+\asymp q^{1/2},
\qquad
K\le Cq\log\log T.
\tag{35}
\]

For bounded `A`, condition (15) is automatic because

\[
aK^2AJ
=O\!\left(q^{-3/4}(\log\log T)^2\right)
=o(1).
\tag{36}
\]

The two coefficients in (32) satisfy

\[
aAKJ^2
=O\!\left(q^{-3/2}\log\log T\right)
=o(1),
\tag{37}
\]

and

\[
aKMJ^{-3/2}
=O\!\left(q^{-3/8}\log\log T\right)
=o(1).
\tag{38}
\]

Therefore, for every fixed `tau_0>0`, if

\[
X(v(0))=O(1),
\tag{39}
\]

then the scalar Riccati comparison from (32) gives

\[
\boxed{
\sup_{0\le t\le\tau_0}X(v(t))
\le
X(v(0))(1+o(1)).
}
\tag{40}
\]

Combining (19), (31), and (40),

\[
\boxed{
\sup_{0\le t\le\tau_0}
\frac1M
\left(
\sum_{m=J_+}^K m^6|c_m(t)|^2
\right)^{1/2}
\le
X(v(0))(1+o(1))+o(1).
}
\tag{41}
\]

In particular,

\[
\boxed{
X(v(0))=o(1)
\quad\Longrightarrow\quad
\sup_{0\le t\le\tau_0}
\frac1{M^2}
\sum_{m=J_+}^K m^6|c_m(t)|^2
=o(1).
}
\tag{42}
\]

The order-one unknown modes below `q^{1/4}` are therefore unable to repopulate the standard `q^{1/2}`-to-`q log log T` transition band with order-one normalized `H^3` energy during fixed positive heat time.

More generally, one may take `J=q^alpha` and any `J_+=q^beta` with `0<alpha<beta<1`, subject to the displayed smallness conditions. The choice `alpha=1/4`, `beta=1/2` is useful because both edges are already present in the source/destination machinery and require no new analytic input.

## 5. This is exactly the weighted resource extracted by center Parseval

On the source-visible band, XF-070 gives the exact sideband weight

\[
w_m
=\frac1{4M^2}
\int_{-1}^1(\pi m+u)^4|\chi(u)|^2\,du.
\tag{43}
\]

Since `J->infinity`, uniformly for `J<=m<=K`,

\[
w_m
=
\left(\frac{C_g\pi^4}{4}+o(1)\right)
\frac{m^4}{M^2}.
\tag{44}
\]

Using `P_m=(-1)^{m-1}mc_m`,

\[
\boxed{
\sum_{m=J}^K w_m|P_m|^2
=
\left(\frac{C_g\pi^4}{4}+o(1)\right)
X(v(0))^2.
}
\tag{45}
\]

Thus (42) is not a new arbitrary norm imposed on the Vieta coordinates. It is the same log-Vieta `H^3` resource that the translated selector sees by exact Parseval and that linearizes to the XF-062--XF-066 third-difference destination energy.

This materially weakens the source-to-periodic interface theorem still needed after XF-069. That theorem no longer has to recover `P_1,...,P_K`, nor does it need rapid pointwise control of every visible mode. It is enough to make the **center-averaged weighted source resource** on, say, `m>=q^{1/4}` tend to zero. The exact periodic heat then transports that quotient to the standard destination band `m>=q^{1/2}` without contamination from the unseen lower modes.

## 6. Stress tests and boundaries

The XF-069 long-wave control passes the theorem in the intended way. Its order-one `P_1` lies wholly inside the discarded block. If no visible log-Vieta state is present initially, (19) shows that the contribution generated above the `q^{1/2}` guard is exponentially small in `q^{1/4}` over every fixed heat interval. The theorem therefore preserves, rather than contradicts, the matched fact that `P_1` can be large while destination third-difference energy vanishes.

A guard band is load-bearing. Taking `J_+=J` would leave the first low-low convolution products directly at the retained edge, and (19) would no longer give a small tail. Likewise, keeping `J` fixed would destroy the factor `J^{-3/2}` in (38); the source theorem's ability to reach **any fixed positive power** above the selector resolution scale is what makes the nonlinear quotient stable.

The bounded-low-block hypothesis is also real. Equation (42) does not permit arbitrarily large hidden coefficients. A sufficient geometric condition is bounded displacement oscillation at the periodic source slice, via the XF-070 estimate `|c_m|<=2 pi A_*`. The proof actually allows moderate growth: for `J=q^alpha`, the low-only majorant remains valid whenever `A q^{-1+alpha}(log log T)^2=o(1)`, with the other displayed coefficients checked simultaneously.

No claim is made about the nonperiodic boundary/interface error. XF-069's center-translation identity says exactly what must still be compared between Xi and a periodic surrogate; XF-071 starts **after** such a source-visible weighted comparison is available. Nor does this result show that a positive-`Lambda` transition forces order-one mass in the guarded destination band. Those are independent geometric/dynamical gates.

## 7. Prior-art and novelty boundary

The logarithmic transform from a linear heat equation to a viscous Hamilton--Jacobi/Burgers equation is classical Cole--Hopf structure, and backward heat of trigonometric polynomials is already represented in the Kabluchko source anchored in `research/xi_flow/SOURCES.md`. Newton's generating identity is classical and was already used in XF-067--XF-070. No novelty is claimed for equation (8) viewed abstractly.

The line-specific contribution is the **finite-index guard-band estimate at the Xi scaling**: equations (13)--(19) and (25)--(42) show that an uncontrolled, heat-undamped ultra-infrared log-Vieta block cannot recreate order-one destination-matched `H^3` energy beyond a larger growing cutoff, while the source-visible weighted quotient is stable under the exact full periodic heat flow. The prior-art audit found neighboring Cole--Hopf/Burgers and trigonometric backward-heat literature, but no result matching this source-cutoff/guard-cutoff estimate or its `q^{-3}` Xi scaling. The proof is self-contained, so no new load-bearing source is added to `SOURCES.md`.

## 8. Consequence for `xi_flow`

XF-069 identified the ultra-infrared Vieta block as a possible fatal gap, and XF-070 showed only that its **initial** weighted cost is negligible. XF-071 supplies the missing dynamical statement on the periodic carrier: after sacrificing the already-available gap between a `delta=1/4` source cutoff and the standard `delta=1/2` destination cutoff, the hidden low modes remain asymptotically invisible to the exact nonlinear heat evolution in the destination-matched resource.

So the periodic algebraic bridge no longer requires source-small `P_1,...,P_K`. The remaining source-side burden is genuinely geometric: prove a center-averaged weighted Xi-to-periodic interface estimate on the source-visible band. Separately, the transition side still has to force nontrivial guarded `H^3` mass. Until those two Xi-specific statements are proved, XF-071 gives no upper bound on `Lambda` and no consequence for RH by itself.
