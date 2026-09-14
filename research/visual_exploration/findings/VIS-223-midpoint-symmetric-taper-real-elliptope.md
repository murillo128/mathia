# VIS-223 — midpoint-symmetric tapers gauge the prime-phase SDP to a real signed elliptope

## Claim

Keep the tapered prime-phase setup of `VIS-192`, `VIS-213`, and `VIS-221`. Let `v:[0,1]->R` be the fixed real taper with

`V=int_0^1 v(x) dx != 0`

and

`kappa_v(u)=V^(-1) int_0^1 v(x) exp(iux) dx`.

Write the taper about its midpoint as

`h(t)=v(1/2+t)`, `-1/2<=t<=1/2`,

with even and odd parts

`h_e(t)=[h(t)+h(-t)]/2`,

`h_o(t)=[h(t)-h(-t)]/2`.

Define the real functions

`C_v(u)=V^(-1) int_(-1/2)^(1/2) h_e(t) cos(ut) dt`,

`S_v(u)=V^(-1) int_(-1/2)^(1/2) h_o(t) sin(ut) dt`.

Then for every real `u`,

`kappa_v(u)=exp(iu/2)[C_v(u)+i S_v(u)]`.

Thus the universal linear phase `exp(iu/2)` in the taper transform is pure vertex gauge in the `VIS-213` prime graph. If

`D_H=diag_(p<=y) exp(iH log(p)/2)`,

then the canonical Hermitian coefficient matrix has the exact factorization

`A_(y,H)=D_H^* B_(y,H) D_H`,

where, for `p<q`,

`B_(p,q)=Q_y^(-1) p^(-alpha) q^(-alpha)`
`          [C_v(H log(q/p))+i S_v(H log(q/p))]`

and `B_(q,p)=conjugate(B_(p,q))`.

Consequently **all continuous residual edge phase after centering comes from midpoint asymmetry of the observation taper**. The left-endpoint choice of interval origin contributes only a removable coboundary.

In the important midpoint-symmetric case

`v(x)=v(1-x)`,

one has `S_v=0`, so `B_(y,H)` is a real symmetric zero-diagonal matrix. This includes the quadratic taper

`w(x)=6x(1-x)`

introduced in `VIS-188` and used as the canonical explicit smooth-window control in the present branch.

For every midpoint-symmetric real taper, the two optimization layers of the live worst-start problem therefore reduce exactly to

`M_abs(A)=M_abs(B)=max_(|z_p|=1)|z^*Bz|`

and

`U_abs(A)=U_abs(B)`
` = max_(X in E_n^R)|Tr(BX)|`,

where

`E_n^R={X in R^(n x n): X=X^T, X>=0, diag(X)=1}`

is the real elliptope. In particular, although the exact torus problem still has continuous `U(1)` vertex phases, the full correlation SDP does **not** require complex correlation matrices once the taper is midpoint-symmetric.

For the quadratic taper specifically,

`kappa_w(u)=exp(iu/2) r_w(u)`

with the real even centered transform

`r_w(u)=12[2 sin(u/2)-u cos(u/2)]/u^3`, `r_w(0)=1`.

Hence the switched prime matrix is a **real signed ratio-shell kernel**:

`B_(p,q)=Q_y^(-1) p^(-alpha)q^(-alpha) r_w(H log(q/p))`.

Its nonzero edge signs can change only when `H log(q/p)` crosses a nonzero root of

`tan(u/2)=u/2`.

Cycle holonomy from `VIS-214` correspondingly collapses from general `U(1)` phase to `±1`: after the midpoint gauge, every surviving cycle gain is exactly the product of its edge signs.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL FOURIER-CENTERING/SWITCHING + REAL-ELLIPTOPE REDUCTION + REPRESENTATION CONTROL + NO-NOVELTY-CLAIM`.

No asymptotic estimate for `U_abs/sqrt(R_v)`, new window theorem, new signed-graph theorem, improved Grothendieck constant, SDP exactness theorem, or RH consequence is claimed.

## 1. Midpoint centering isolates the only nontrivial taper phase

Change variables `x=1/2+t` in the transform:

`kappa_v(u)`
` = exp(iu/2) V^(-1) int_(-1/2)^(1/2) h(t) exp(iut) dt`.

Decompose `h=h_e+h_o`. Since `h_e` is even and `h_o` is odd,

`int h_e(t) sin(ut) dt=0`

and

`int h_o(t) cos(ut) dt=0`

on the symmetric interval. Therefore

`V^(-1) int h(t) exp(iut) dt`
` = C_v(u)+iS_v(u)`,

which proves

`kappa_v(u)=exp(iu/2)[C_v(u)+iS_v(u)]`.

Here `C_v` is real and even, while `S_v` is real and odd. No approximation, smoothness beyond integrability, prime asymptotic, or optimization input enters this identity.

The interpretation is useful because `u=H log(q/p)`. The deterministic linear phase is

`exp(iH log(q/p)/2)`
` = conjugate(exp(iH log p/2)) exp(iH log q/2)`,

which is exactly a vertex coboundary. It is therefore removable by the same diagonal switching already identified abstractly in `VIS-214`.

There is also a direct observation-coordinate interpretation. Multiplying the prime-torus coordinate

`z_p(T)=exp(iT log p)`

by `exp(iH log p/2)` replaces it by

`z_p(T+H/2)`.

The gauge is simply the change from anchoring the observation window at its left endpoint `T` to anchoring phase at its midpoint `T+H/2`.

Thus a visual or spectral analysis that treats this linear phase as arithmetic magnetic structure is measuring an observation-origin artifact.

## 2. Symmetric tapers leave only a real signed kernel

If `v(x)=v(1-x)`, then `h_o=0` and therefore `S_v=0`. Put

`r_v(u)=C_v(u)`.

Then `r_v` is real and even and

`kappa_v(u)=exp(iu/2)r_v(u)`.

For the `VIS-213` coefficient

`A_(p,q)=Q_y^(-1)p^(-alpha)q^(-alpha)kappa_v(H log(q/p))`

on `p<q`, define

`d_p=exp(iH log p/2)`.

The preceding factorization gives

`A_(p,q)=conjugate(d_p) B_(p,q) d_q`

with

`B_(p,q)=Q_y^(-1)p^(-alpha)q^(-alpha)r_v(H log(q/p)) in R`.

Hermitian symmetry makes `B` real symmetric, and in matrix form

`A=D_H^* B D_H`.

Diagonal unitary switching preserves the unit-modulus torus. The bijection `z -> D_H z` gives immediately

`max_(|z_p|=1)|z^*Az|`
` = max_(|y_p|=1)|y^*By|`.

So the complex-looking phase synchronization problem generated by a symmetric taper is exactly a real-weight `XY`/unimodular quadratic problem after recentering. It does **not** reduce the torus variables to signs `±1`; only the edge coefficients become real.

## 3. The complex correlation SDP collapses exactly to the real elliptope

`VIS-221` and `VIS-222` use the complex correlation body

`E_n^C={X=X^*, X>=0, diag(X)=1}`.

First apply the same gauge. The map

`X -> Y=D_H X D_H^*`

is a bijection of `E_n^C`, and cyclicity of trace gives

`Tr(A X)=Tr(B Y)`.

Hence `U_abs(A)=U_abs(B)` even before using reality of `B`.

Now let `B` be real symmetric and `Y in E_n^C`. Write

`Y=R+iK`

with `R=Re(Y)` real symmetric and `K=Im(Y)` real skew-symmetric.

For every real vector `x`,

`x^T R x = x^* Y x >= 0`,

so `R>=0`, and `diag(R)=1`. Thus `R in E_n^R`.

Moreover a real symmetric matrix is Frobenius-orthogonal to a real skew-symmetric matrix, so

`Tr(BY)=Tr(BR)`.

Therefore every complex feasible value is attained by a real correlation matrix. The reverse inclusion is trivial, and hence

`max_(Y in E_n^C)|Tr(BY)|`
` = max_(R in E_n^R)|Tr(BR)|`.

This is an exact dimensional reduction of the live SDP surface, not an approximation. `VIS-222`'s symmetric-Grothendieck comparison remains valid; the present result only shows that, for symmetric tapers, the SDP side can be studied entirely inside the ordinary real elliptope.

## 4. The quadratic taper makes the remaining signs explicit ratio shells

For

`w(x)=6x(1-x)`

one has `V=1` and, after setting `x=1/2+t`,

`w(1/2+t)=3/2-6t^2`.

Direct integration of the centered even transform gives

`r_w(u)`
` = int_(-1/2)^(1/2) (3/2-6t^2) cos(ut) dt`
` = 12[2 sin(u/2)-u cos(u/2)]/u^3`

for `u!=0`, with the continuous value `r_w(0)=1`.

Hence the only edge phase remaining after midpoint switching is the sign of `r_w`. Away from zeros, sign changes occur when

`2 sin(u/2)-u cos(u/2)=0`,

equivalently

`tan(u/2)=u/2`.

The first positive nonzero root is approximately `u=8.9868`; subsequent roots generate further deterministic sign shells. In the prime graph these shell boundaries are multiplicative:

`q/p=exp(u_j/H)`.

This gives a mathematically faithful representation for the current static branch: vertices are primes, edge magnitudes are the existing `p^(-alpha)q^(-alpha)|r_w(H log(q/p))|/Q_y`, and edge colors/signs are determined by which centered-window ratio shell contains `q/p`.

No arithmetic conclusion follows merely from the appearance of those shells. They are imposed by the chosen observation kernel.

## 5. Cycle holonomy becomes signed rather than continuously magnetic

`VIS-214` showed that cycle holonomy is the gauge-invariant obstruction to coefficient-envelope attainment for a general complex gain graph.

Under a midpoint-symmetric taper, the switched edge gains are just

`sign(B_(p,q)) in {+1,-1}`

on nonzero edges. Therefore for every surviving oriented cycle `C`,

`prod_(e in C) gain_e in {+1,-1}`,

so its phase holonomy is exactly `0` or `pi`.

Equivalently, in the original uncentered representation the factors `exp(iH log(q/p)/2)` telescope around every cycle and contribute no holonomy at all. All surviving holonomy is the parity of negative centered-transform edges.

This narrows the interpretation of the magnetic language in `VIS-214`--`VIS-221`. The connection-Laplacian, cycle-packing, stress, and SDP machinery remain mathematically valid, but for symmetric tapers they act on a signed weighted graph embedded in a continuous-phase vertex optimization. A generic `U(1)` edge-phase control is therefore not representation-matched to this branch.

In particular, the `VIS-214` possibility that a single odd cycle has holonomy different from both `0` and `pi` cannot occur for a midpoint-symmetric taper. Frustration can still be extensive: different signed cycles can make the graph neither balanced nor antibalanced, and the exact `XY` optimum can still be far below the coefficient envelope.

## 6. Prior art and novelty boundary

The Fourier fact behind the first reduction is classical linear-phase window theory. Fredric J. Harris, **On the use of windows for harmonic analysis with the discrete Fourier transform**, *Proceedings of the IEEE* 66:1 (1978), 51--83, DOI `10.1109/PROC.1978.10837`, treats centered symmetric windows and the phase shift introduced by moving between centered and zero-based observation coordinates. `VIS-188` already uses Harris as the prior-art boundary for the same windowing family.

Switching/gauge equivalence and cycle balance for unit gain graphs are classical and were already source-audited in `VIS-214`. The present finding does not claim a new gain-graph theorem; it identifies the special gain class forced by the Mathia taper.

The real correlation body

`{X real symmetric: X>=0, diag(X)=1}`

is the classical elliptope. Monique Laurent and Svatopluk Poljak, **On the Facial Structure of the Set of Correlation Matrices**, *SIAM Journal on Matrix Analysis and Applications* 17:3 (1996), 530--547, DOI `10.1137/0617031`, is a standard reference. The equality between the complex and real SDP values for a real objective matrix is the elementary real-part argument above and is not claimed as a new optimization theorem.

Finally, `VIS-222` already audits Friedland--Lim's symmetric Grothendieck inequality. Nothing here improves that universal approximation factor. The Mathia-specific content is the exact dictionary from observation-window symmetry to the gauge class and SDP geometry of the canonical prime matrix.

## Boundaries and falsification

The real reduction requires midpoint symmetry `v(x)=v(1-x)`. A general real endpoint-zero taper from `VIS-192` need not satisfy it. For an asymmetric taper, the residual term

`S_v(u)=V^(-1) int h_o(t) sin(ut) dt`

can produce genuine continuous edge phases after the midpoint coboundary is removed.

The result also does not say that the real signed kernel is easy to optimize. The torus variables remain continuous complex phases, the real elliptope may have high-rank optimizers, and the prime-specific asymptotic value of `U_abs(B)/sqrt(R_v)` remains completely open.

Zeros of `r_v` remove edges from the support graph. Statements about signs and cycle products apply only to nonzero edges, exactly as in `VIS-214`.

Falsify the finding by locating an error in the centered even/odd Fourier decomposition, the diagonal switching identity, preservation of the torus or correlation body under `D_H`, positive semidefiniteness of `Re(Y)`, the quadratic-taper transform, or the cycle-sign specialization.

## Research consequence

The accepted clue `CLUE-prime-phase-sdp-rms-tightness` remains unresolved, but for midpoint-symmetric tapers its finite-dimensional object is now sharper:

`U_abs(A_(y,H))`
` = max_(X in E_n^R)|Tr(B_(y,H)X)|`

with a real signed ratio-shell matrix `B_(y,H)`.

The next static test should therefore estimate this **real elliptope** value on the canonical prime matrices rather than spend effort on generic complex SDP geometry. Numerical exploration can use the signed ratio-shell representation directly, while any arithmetic-specific control should preserve the edge-magnitude profile and the observation-kernel semantics before perturbing the sign organization.

A generic independent `U(1)` phase scramble is useful as a broad optimization control but is no longer a matched null for the symmetric-taper representation: it introduces continuous edge phase that the actual centered window does not possess.

This does not settle whether the normalized SDP/worst-start ratio is bounded or divergent. It removes one layer of representational freedom from that question and isolates the remaining difficulty in the signed prime-ratio weight geometry itself.
