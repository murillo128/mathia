# ANF-096 — arithmetic endpoint cancellation moves the diluted surgery threshold to three log n

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + SPARSE-SURGERY + DIRICHLET-CANCELLATION + ENDPOINT-LAPLACE + NEAR-EXTREMIZER-RIGIDITY + QUOTIENT-FRONTIER`. `ANF-095` gives a worst-case sparse-surgery budget based on summing the norms of `m` edited conjugate pairs separately. On the exact dense arithmetic block used to generate the exponential conditioning in `ANF-092/093`, that triangle bound is off by two powers of the block size at the vertical endpoint. The physical equal-weight synthesis is a Dirichlet kernel whose denominator stays nonzero at `alpha=+-1`, so the exponentially amplified endpoint sees only order-one horizontal amplitude rather than order `m`. As a result, the explicit diluted conditioning family cannot be turned into a Montgomery--Taylor near-extremal nonseparable witness at the `ANF-095` height. Its actual transition occurs only at

\[
\boxed{
4\pi Y_n=3\log n+2\log\log n+O(1),
}
\]

and below that transition **every near-extremal member of this lifted family converges to the separable cone in the protected destination norm**.

Fix the arithmetic spacing and block from `ANF-092/093`,

\[
d:=\frac34,
\qquad
C_n:=\{0,d,2d,\ldots,nd\},
\qquad
A_n(\alpha):=\sum_{j=0}^n e^{-2\pi i d j\alpha}.
\tag{1}
\]

For a common conjugate height `Y>=0`, put

\[
B_{n,Y}:=C_n+i\{-Y,+Y\}.
\tag{2}
\]

There are constants `0<c<C<infinity`, depending only on the fixed Montgomery--Taylor profile and on `d=3/4`, such that whenever

\[
1\le Y\le\log n
\tag{3}
\]

and `n` is sufficiently large,

\[
\boxed{
 c\left(n+\frac{e^{4\pi Y}}{Y^2}\right)
 \le
 E_{\rm MT}(B_{n,Y})
 \le
 C\left(n+\frac{e^{4\pi Y}}{Y^2}\right).
}
\tag{4}
\]

Moreover, if `0<=y<=1` and `Y->infinity`, then the actual central-notch defect produced by changing the whole block from height `y` to height `Y` satisfies

\[
\boxed{
 c\frac{e^{4\pi Y}}{Y^2}
 \le
 \left\|S_{B_{n,Y}}-S_{B_{n,y}}\right\|_s^2
 \le
 C\left(n+\frac{e^{4\pi Y}}{Y^2}\right).
}
\tag{5}
\]

Now use the exact dilution of `ANF-092`. Let

\[
q_n=n^3,
\qquad
T_n=n^{10},
\tag{6}
\]

let `mathcal H_n` be its `q_n`-point high-zero padding comb translated by `T_n`, and let

\[
y_n=r^{n/8},
\qquad
r=\sin(3\pi/8).
\tag{7}
\]

The safe separable comparator is

\[
P_n=(C_n\cup\mathcal H_n)+i\{-y_n,+y_n\},
\tag{8}
\]

while the physical surgery that lifts only the conditioning block is

\[
W_n^{(Y)}=
\bigl(C_n+i\{-Y_n,+Y_n\}\bigr)
\cup
\bigl(\mathcal H_n+i\{-y_n,+y_n\}\bigr).
\tag{9}
\]

For every sequence `1<=Y_n<=log n`, define

\[
\boxed{
\Omega_n
:=
\frac{e^{4\pi Y_n}}{n^3Y_n^2}.
}
\tag{10}
\]

Then

\[
\boxed{
\frac{\Delta(W_n^{(Y)})}{L(W_n^{(Y)})}\longrightarrow0
\quad\Longleftrightarrow\quad
\Omega_n\longrightarrow0,
}
\tag{11}
\]

and, whenever these equivalent conditions hold,

\[
\boxed{
d_{\rm sep}(W_n^{(Y)})\longrightarrow0.}
\tag{12}
\]

Thus the exact `ANF-092/093` finite-difference conditioning witness is not a physical near-extremal obstruction after lifting. Its exponentially bad signed Gram direction survives, but the actual positive multiset synthesis has a different endpoint geometry and remains inside the protected separable tube throughout the whole source-negligible regime.

## 1. The physical arithmetic block is a Dirichlet kernel, not the bad binomial Rayleigh vector

The structure factor of (2) is

\[
S_{B_{n,Y}}(\alpha)
=2\cosh(2\pi\alpha Y)A_n(\alpha),
\tag{13}
\]

with the exact geometric-sum identity

\[
\boxed{
|A_n(\alpha)|^2
=
\frac{\sin^2\!\bigl(\pi(n+1)d\alpha\bigr)}
     {\sin^2(\pi d\alpha)}.
}
\tag{14}
\]

The distinction from `ANF-093` is load-bearing. Its exponentially small source direction uses the **signed binomial coefficients**

\[
(-1)^j\binom nj,
\tag{15}
\]

whose synthesis is `(1-e^{-2 pi i d alpha})^n`. The physical block itself has coefficient `+1` at every center, so its synthesis is (14). The two objects have completely different behavior at the spectral endpoints.

Because `d=3/4`, the only zero of the denominator in (14) on `[-1,1]` is at `alpha=0`. At the endpoint,

\[
|\sin(\pi d)|=\sin(3\pi/4)>0.
\tag{16}
\]

Hence the large Dirichlet peak lives at the center `alpha=0`, where the vertical factor equals one, while the exponentially large factor `cosh(2 pi alpha Y)` lives near `|alpha|=1`, where the arithmetic synthesis is only order one apart from its rapid numerator oscillation. This separation is exactly what the pairwise triangle bound of `ANF-095` discards.

## 2. Exact endpoint geometry gives `n + exp(4 pi Y)/Y^2`

Retain the positive density from `ANF-087`,

\[
g(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin(2^{-1/2})}
\mathbf 1_{[-1/2,1/2]}(u),
\qquad
K=\widehat g.
\tag{17}
\]

Since `F_MT=K^2`, its spectrum is

\[
J_{\rm MT}=g*g.
\tag{18}
\]

The endpoint value of `g` is strictly positive, so convolution over the shrinking overlap interval gives constants `c_0,C_0>0` such that

\[
\boxed{
 c_0(1-|\alpha|)
 \le J_{\rm MT}(\alpha)
 \le C_0(1-|\alpha|)
}
\tag{19}
\]

whenever `|alpha|` is sufficiently close to one. Globally `J_MT` is bounded and nonnegative.

For `0<=alpha<=1/2`, (14) gives

\[
|A_n(\alpha)|
\le C_d\min\left(n+1,\frac1\alpha\right),
\tag{20}
\]

whereas on `1/2<=alpha<=1`,

\[
|A_n(\alpha)|\le C_d.
\tag{21}
\]

Write `lambda=4 pi Y`. On the central half interval, split at `alpha=1/n` and at `alpha=4/lambda`. Under (3), direct integration of (20) gives

\[
\int_0^{1/2}
J_{\rm MT}(\alpha)
4\cosh^2(2\pi\alpha Y)|A_n(\alpha)|^2\,d\alpha
\ll
n+\frac{e^{\lambda/2}}{\lambda}.
\tag{22}
\]

On the endpoint half interval, (19) and (21) give

\[
\int_{1/2}^1
J_{\rm MT}(\alpha)
4\cosh^2(2\pi\alpha Y)|A_n(\alpha)|^2\,d\alpha
\ll
\frac{e^\lambda}{\lambda^2}.
\tag{23}
\]

For `Y>=1`, the second exponential term absorbs the one in (22). Reflection gives the upper half of (4).

The endpoint scale is also a lower bound. Put `t=1-alpha` and integrate only over

\[
\frac1\lambda\le t\le\frac2\lambda.
\tag{24}
\]

There `J_MT(1-t)\gg t`, the vertical factor is `\gg e^\lambda`, and the denominator in (14) is uniformly bounded. The numerator oscillates on scale `1/n`, while the interval in (24) has length `1/lambda`. Since `lambda=O(log n)=o(n)`, the elementary identity for the integral of `sin^2` gives

\[
\int_{1/\lambda}^{2/\lambda}
\sin^2\!\bigl(\pi(n+1)d(1-t)\bigr)\,dt
\gg\frac1\lambda.
\tag{25}
\]

Therefore

\[
E_{\rm MT}(B_{n,Y})
\gg\frac{e^\lambda}{\lambda^2}.
\tag{26}
\]

Lamzouri's global floor independently gives

\[
E_{\rm MT}(B_{n,Y})\ge L(B_{n,Y})=4(n+1).
\tag{27}
\]

Taking the larger of (26) and (27) proves the lower half of (4).

The central notch does not alter this endpoint calculation. Its subtraction is supported in `[-eta,eta]` with `eta<1`, so `J_s=J_MT` on a fixed neighborhood of `alpha=+-1`. For bounded `y` and `Y->infinity`, the high-height term dominates `cosh(2 pi alpha y)` uniformly on (24). Repeating (22)--(26) for

\[
2\bigl(\cosh(2\pi\alpha Y)-\cosh(2\pi\alpha y)\bigr)A_n(\alpha)
\tag{28}
\]

proves (5).

## 3. The actual destination screening threshold is three times higher than the pairwise one

The comparator `P_n` in (8) is exactly separable, has the same cardinality as `W_n^{(Y)}`, and has no real sites. By the all-height separable floor of `ANF-085`,

\[
\|S_{P_n}\|_s^2\gg q_n\asymp n^3.
\tag{29}
\]

The difference `S_{W_n^{(Y)}}-S_{P_n}` is supported entirely on the `C_n` block and is exactly the defect in (28) with `y=y_n`. Hence (5) gives

\[
\boxed{
 d_{\rm sep}(W_n^{(Y)})^2
 \le
 C_s\left(
 \frac1{n^2}
 +
 \frac{e^{4\pi Y_n}}{n^3Y_n^2}
 \right)
 =C_s\bigl(n^{-2}+\Omega_n\bigr).
}
\tag{30}
\]

Consequently `Omega_n->0` forces (12).

Compare this with the worst-case budget of `ANF-095`. There `m_n=n+1`, `N_n=2(n^3+n+1)`, and summing individual pair norms yields the screening parameter

\[
\Xi_{m_n,N_n}(Y)
\asymp
\frac1n\frac{e^{4\pi Y}}{Y^2}.
\tag{31}
\]

The actual arithmetic synthesis instead uses

\[
\Omega_n
\asymp
\frac1{n^3}\frac{e^{4\pi Y}}{Y^2}.
\tag{32}
\]

Thus the explicit `C_n` block gains a factor `n^{-2}` over pairwise triangle summation. The `Xi=Theta(1)` height from `ANF-095`,

\[
4\pi Y=\log n+2\log\log n+O(1),
\tag{33}
\]

still satisfies

\[
\Omega_n\asymp n^{-2}\longrightarrow0.
\tag{34}
\]

So this exact conditioning block is actually deep inside the separable tube at the old critical height.

The first height at which (30) stops forcing the defect to zero is

\[
\frac{e^{4\pi Y_n}}{Y_n^2}\asymp n^3,
\tag{35}
\]

or

\[
\boxed{
4\pi Y_n
=3\log n+2\log\log n+O(1).
}
\tag{36}
\]

The extra `2 log n` is horizontal coherence information that `Xi` intentionally ignores.

## 4. The source transition moves to exactly the same scale

Let

\[
P_n^{\rm pad}
:=\mathcal H_n+i\{-y_n,+y_n\}.
\tag{37}
\]

`ANF-095` retains from `ANF-092` the near-extremal padding estimate

\[
E_{\rm MT}(P_n^{\rm pad})=4q_n(1+o(1)).
\tag{38}
\]

Since

\[
S_{W_n^{(Y)}}=S_{P_n^{\rm pad}}+S_{B_{n,Y_n}},
\tag{39}
\]

Minkowski and (4) show that

\[
\Omega_n\to0
\quad\Longrightarrow\quad
E_{\rm MT}(W_n^{(Y)})
\le4q_n(1+o(1)).
\tag{40}
\]

The affine floor gives the reverse estimate because

\[
L(W_n^{(Y)})=4(q_n+n+1)=4q_n(1+o(1)),
\tag{41}
\]

so `Omega_n->0` implies the forward direction of (11).

For the converse, the large translation `T_n=n^{10}` makes the padding/block cross energy negligible throughout `Y_n<=log n`. The explicit formula for `K` from `ANF-087` gives, whenever the real part of `z` has size `asymp T_n` and `|Im z|<=Y_n+1`,

\[
|K(z)|\ll\frac{e^{\pi(Y_n+1)}}{T_n}.
\tag{42}
\]

There are only `O(q_n n)` cross pairs, hence their total contribution to `E_MT` is

\[
O\!\left(
\frac{q_n n e^{2\pi Y_n}}{T_n^2}
\right)
=o(q_n).
\tag{43}
\]

The endpoint lower bound in (4), together with the exact floor for the padding, therefore yields

\[
\Delta(W_n^{(Y)})
\ge
c\frac{e^{4\pi Y_n}}{Y_n^2}
-4(n+1)-o(q_n).
\tag{44}
\]

If `Omega_n` fails to tend to zero, a subsequence has `Omega_n>=epsilon>0`, and (44) gives a fixed positive lower bound for `Delta/L` on that subsequence. This proves the reverse implication in (11).

Therefore the **same refined parameter `Omega_n` controls both sides** for the exact physical surgery. Below `Omega_n=1`, the block is source-negligible and destination-negligible after normalization by the `n^3` padding. At `Omega_n=Theta(1)`, both its endpoint Montgomery--Taylor energy and its destination defect become macroscopic. The matching phenomenon of `ANF-095` survives, but at the true arithmetic scale (36), not at the pairwise worst-case scale (33).

For example, for every fixed `epsilon>0`,

\[
4\pi Y_n
=3\log n+(2-\epsilon)\log\log n
\tag{45}
\]

still gives

\[
\frac{\Delta(W_n^{(Y)})}{L(W_n^{(Y)})}\to0,
\qquad
d_{\rm sep}(W_n^{(Y)})\to0,
\tag{46}
\]

whereas replacing `2-epsilon` by `2+epsilon` makes the relative source excess bounded away from zero and in fact forces the endpoint contribution to grow relative to the padding.

## 5. What this kills, and what remains open

`ANF-093` proves a real and important fact: after the exact Lamzouri Schur quotient, a normalized **signed binomial direction** on `C_n` is exponentially smaller on the source window than on the longer destination window. `ANF-096` shows that this is not enough to manufacture a physical obstruction by simply lifting that same sparse block. The multiset does not carry the binomial coefficients; its equal positive occupancies produce the Dirichlet synthesis (14), and that synthesis cancels coherently at the vertically amplified spectral endpoint.

Thus the explicit `ANF-092/093` family is now closed as a near-extremal nonseparable candidate:

\[
\boxed{
\Delta(W_n^{(Y)})/L(W_n^{(Y)})\to0
\quad\Longrightarrow\quad
d_{\rm sep}(W_n^{(Y)})\to0.
}
\tag{47}
\]

This does **not** prove a general quotient-rigidity theorem. A different sparse block could have physical endpoint synthesis of order `m`, or could exploit a more delicate source cancellation against the carrier rather than the remote-padding geometry used here. Nor does (44) rule out a configuration with a fixed nonzero relative excess that still lies inside the broader fatal window of `ANF-086`; the exact constant comparison with `rho_s/(1-s)` is not made here.

The surviving gate is correspondingly sharper. It is no longer enough to exhibit an exponentially bad signed Rayleigh direction and then amplify the associated sites vertically. A genuine obstruction must make the **physical positive multiset defect**, after optimization against the separable cone, retain endpoint-scale destination mass while its full Montgomery--Taylor energy remains inside the allowed near-extremal budget. The horizontal synthesis of the actual edited block, not merely an auxiliary Gram condition number, is now load-bearing.

## 6. Audit and prior-art boundary

The proof uses only the exact Montgomery--Taylor factor and spectrum already fixed in `ANF-087`, the `ANF-092` padding geometry, the all-height separable denominator from `ANF-085`, and the elementary geometric-sum identity (14). The endpoint estimate (19) follows directly from `J_MT=g*g` and the strict positivity of `g` at `+-1/2`; (25) is the elementary integral of a rapidly oscillating `sin^2`. No cancellation sign is assumed in the energy, and the only place the remote translation is used is the explicit cross bound (43).

A targeted prior-art search found the classical Dirichlet-kernel identity and generic weighted Fourier-kernel asymptotics, but no result whose statement supplies the line-specific combination (4), the `n^{-2}` correction from `Xi` to `Omega`, or the matched threshold (36) for the Montgomery--Taylor/central-notch surgery. No external theorem is load-bearing, so `SOURCES.md` is unchanged.

## Research consequence

The most concrete sparse-conditioning witness left by `ANF-093` does not survive physical realization. Its old `Xi=Theta(1)` height is a false alarm caused by pairwise triangle summation: the equal-weight arithmetic block remains both source-negligible and destination-negligible there. The true transition for that family is `4 pi Y=3 log n+2 log log n+O(1)`, and at that transition source and destination become macroscopic together. Any next counterexample search should therefore optimize the **physical endpoint structure factor modulo the separable cone**, rather than continue amplifying the signed generalized-eigenvector of the source/destination Gram pair.