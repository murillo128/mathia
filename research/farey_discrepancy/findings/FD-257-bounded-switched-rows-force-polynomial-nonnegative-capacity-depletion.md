# FD-257 — Bounded switched rows force polynomial nonnegative-capacity depletion

- **Date:** 2026-09-21
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response positivity / quantitative switched stability / dyadic capacity / finite-response topology / source-side boundary obstruction
- **Depends on:** FD-229, FD-230, FD-236, FD-237
- **Classification:** `EXACT-DERIVED + QUANTITATIVE-POSITIVITY-OBSTRUCTION + BOUNDED-SWITCHED-ROWS + POLYNOMIAL-CAPACITY-DEPLETION + FINER-RESPONSE-TOPOLOGY`

## Claim

FD-230 proves qualitatively that a nonnegative linear-capacity divisor cushion whose switched rows are `o(4^j)` must have vanishing relative mass on late dyadic divisor bands. The physical switched constructions of FD-225--FD-237 operate at a much finer target scale: the desired switched rows are bounded. At that scale the depletion is not merely qualitative.

Let

\[
(\mathscr A b)(m)
=
\sum_{d\le m}
b_d M\!\left(\left\lfloor\frac md\right\rfloor\right),
\tag{1}
\]

assume

\[
0\le b_d\le C d
\qquad(d\ge1),
\tag{2}
\]

and put

\[
B_k=[2^k,2^{k+1})\cap\mathbb N,
\qquad
s_k:=4^{-(k+1)}\sum_{d\in B_k}b_d.
\tag{3}
\]

Write

\[
y_j=(\mathscr A b)(2^j),
\qquad
u_j=4^{-j}y_j,
\tag{4}
\]

and use the switched schedule

\[
r_j=(1,4,4,1,4,4,\ldots),
\qquad
\mathcal R_j(b):=(E-I)^{r_j}y_j,
\tag{5}
\]

where `E` shifts the dyadic sample index. Suppose that for one finite constant `B`,

\[
\boxed{
|\mathcal R_j(b)|\le B
\qquad(j\ge0).
}
\tag{6}
\]

Then there is an absolute constant `A` such that

\[
\boxed{
s_k
\le
A(C+B)\left(\frac{23}{24}\right)^k
\qquad(k\ge0).
}
\tag{7}
\]

Equivalently, since

\[
\sum_{d\in B_k}d\asymp4^k,
\]

the relative dyadic capacity mass satisfies

\[
\boxed{
\frac{\sum_{d\in B_k}b_d}
     {\sum_{d\in B_k}d}
\ll
(C+B)\left(\frac{23}{24}\right)^k.
}
\tag{8}
\]

In terms of the divisor scale `x=2^k`,

\[
\boxed{
\frac{\sum_{x\le d<2x}b_d}
     {\sum_{x\le d<2x}d}
\ll
(C+B)x^{-\beta},
\qquad
\beta=\log_2\frac{24}{23}
=0.0614005\ldots .
}
\tag{9}
\]

The constant `23/24` is not asserted to be optimal. It is a convenient explicit value obtained from the same elementary Mertens tail bounds used in FD-230. With those bounds alone, the weighted contraction works for every

\[
r>r_0=0.9554100411\ldots,
\tag{10}
\]

where `r_0` is the unique real root in `(1/2,1)` of

\[
16r^3-12r^2-3=0.
\tag{11}
\]

Thus the elementary method permits any power exponent strictly below

\[
\log_2(1/r_0)=0.0658080\ldots.
\tag{12}
\]

This is a quantitative source-side strengthening of FD-230 at the bounded switched-response scale. It does not yet obstruct the canonical Mertens repair: no matching lower bound is known for how much nonnegative slack that repair must consume on the same deep bands.

## Bounded switched rows make the normalized response exponentially small

Define

\[
\delta_j:=4^{-j}\mathcal R_j(b).
\tag{13}
\]

Because `y_{j+t}=4^{j+t}u_{j+t}`,

\[
\boxed{
\delta_j=(4E-I)^{r_j}u_j,
}
\tag{14}
\]

and (6) gives

\[
|\delta_j|\le B4^{-j}.
\tag{15}
\]

The qualitative proof in FD-229 uses strict stability of the normalized period-three switched recurrence. For the present rate it is useful to write that recurrence explicitly.

For a row of order one,

\[
4u_{j+1}-u_j=\delta_j.
\tag{16}
\]

For a row of order four,

\[
256u_{j+4}
-256u_{j+3}
+96u_{j+2}
-16u_{j+1}
+u_j
=\delta_j.
\tag{17}
\]

For `n>=1`, define the period state

\[
X_n=
\begin{pmatrix}
u_{3n}\\
u_{3n-1}\\
u_{3n-2}
\end{pmatrix}.
\tag{18}
\]

Solving successively the order-one equation at `3n` and the preceding order-four equations at `3n-2` and `3n-1` gives

\[
X_{n+1}=PX_n+F_n,
\tag{19}
\]

with

\[
P=
\begin{pmatrix}
-5/32 & 15/256 & -1/256\\
-1/8 & 1/16 & -1/256\\
1/4 & 0 & 0
\end{pmatrix},
\tag{20}
\]

and

\[
F_n=
\begin{pmatrix}
\frac5{32}\delta_{3n}
+\frac1{256}\delta_{3n-2}
+\frac1{256}\delta_{3n-1}\\[3pt]
\frac14\delta_{3n}
+\frac1{256}\delta_{3n-2}\\[3pt]
\frac14\delta_{3n}
\end{pmatrix}.
\tag{21}
\]

The characteristic polynomial of `P` is

\[
\left(\lambda-\frac1{64}\right)
\left(
\lambda-\frac{-7+3\sqrt5}{128}
\right)
\left(
\lambda-\frac{-7-3\sqrt5}{128}
\right).
\tag{22}
\]

Hence

\[
\rho(P)
=
\frac{7+3\sqrt5}{128}
=0.107095\ldots
<
\frac7{64}
<
\frac18.
\tag{23}
\]

The three eigenvalues are distinct, so for an absolute matrix norm constant,

\[
\|P^n\|\ll \left(\frac7{64}\right)^n.
\tag{24}
\]

The trivial estimate `|M(q)|<=q` and (2) give

\[
|y_j|
\le
\sum_{d\le2^j}Cd\frac{2^j}{d}
\le C4^j,
\tag{25}
\]

so the initial normalized state is `O(C)`. From (15) and (21),

\[
\|F_n\|\ll B\,64^{-n}.
\tag{26}
\]

Iterating (19), and using `1/64<7/64`, gives

\[
\|X_n\|
\ll
(C+B)\left(\frac7{64}\right)^n.
\tag{27}
\]

Since `7/64<1/8`, the three phases of (27) imply the deliberately relaxed but simpler estimate

\[
\boxed{
|u_j|\ll(C+B)2^{-j}.
}
\tag{28}
\]

Thus bounded *unnormalized* switched rows force the quadratic-scale normalized response to decay at least geometrically. This is the extra quantitative input absent from the `o(4^j)` hypothesis of FD-230.

## The positive Mertens tail is a weighted contraction

FD-230 proves, without any regularity assumption inside the dyadic bands, that nonnegativity gives

\[
\boxed{
|u_j-s_{j-1}|
\le
\sum_{\ell=2}^{j}c_\ell s_{j-\ell}
+O(C2^{-j}),
}
\tag{29}
\]

where

\[
c_\ell
=
4^{1-\ell}
\max_{2^{\ell-1}\le q\le2^\ell}|M(q)|.
\tag{30}
\]

The elementary values of `M` through `8`, followed by `|M(q)|<=q`, give exactly the bounds already used in FD-230:

\[
c_2=\frac14,
\qquad
c_3=\frac18,
\qquad
c_\ell\le2^{2-\ell}\quad(\ell\ge4).
\tag{31}
\]

Put `k=j-1`. Combining (28) with (29),

\[
s_k
\le
A_0(C+B)2^{-k}
+
\sum_{\ell=2}^{k+1}
c_\ell s_{k+1-\ell}
\tag{32}
\]

for one absolute `A_0`.

To turn this into a rate, test the convolution against the weight `r^k`, with `1/2<r<1`. From (31),

\[
\begin{aligned}
\sum_{\ell\ge2}c_\ell r^{1-\ell}
&\le
\frac1{4r}
+\frac1{8r^2}
+\sum_{\ell\ge4}2^{2-\ell}r^{1-\ell}\\
&=
\frac{4r^2+3}{8r^2(2r-1)}.
\end{aligned}
\tag{33}
\]

The right side is strictly below one exactly when

\[
16r^3-12r^2-3>0.
\tag{34}
\]

This proves (10)--(11). For the concrete choice

\[
r=\frac{23}{24},
\tag{35}
\]

the weighted kernel mass is

\[
\boxed{
\sum_{\ell\ge2}c_\ell r^{1-\ell}
\le
\frac{5766}{5819}
<1.
}
\tag{36}
\]

Because `2^{-k}<=r^k`, equation (32) and induction now give

\[
s_k\ll(C+B)r^k.
\tag{37}
\]

Indeed, enlarge the implicit constant to dominate the finitely many initial values; if (37) holds below `k`, substituting it into (32) multiplies the inductive constant by at most `5766/5819`, while the forcing is an additional fixed multiple of `(C+B)r^k`. The positive margin `53/5819` absorbs that forcing uniformly. This proves (7).

No cancellation inside `b` is used. The positivity in (2) is load-bearing: it is what converts the older divisor bands into the absolute Mertens-tail inequality (29).

## Finite growing blocks inherit the same interior rate

The argument is causal in the response index. To control `u_j`, the period recurrence uses only switched equations whose deepest sample is at most `2^j`; to control `s_k`, equation (29) needs `u_{k+1}` and divisor coefficients only up to `2^{k+1}`.

Consequently the same constants apply to a finite divisor grid `1<=d<=D`: if all scheduled switched rows whose complete stencils end at or before `2^{k+1}` satisfy (6), then (7) holds for that band. In particular, one may zero-extend the coefficient vector beyond `D`; for every band with `2^{k+1}<=D`, the response values and switched equations used in the proof are unchanged.

This is the form relevant to the growing scale-adapted reservoirs. Their depth `D=D_N` may vary with `N`, but the depletion constant does not depend on `D`.

Let the physical reservoir scale from FD-236 be

\[
L_N=\frac{N}{D\log N},
\qquad
|I_d^*\cap\mathbb P|\asymp L_Nd.
\tag{38}
\]

If a nonnegative cushion is normalized by a common source scale so that its coefficients satisfy a uniform version of (2), and its normalized switched rows remain uniformly bounded, then on every eligible dyadic band

\[
\frac{\text{cushion mass on }B_k}
     {\text{normalized linear capacity on }B_k}
\ll
(2^k)^{-\beta}.
\tag{39}
\]

In the strongest physical case, where the actual switched contribution is required to stay `O(1)` while the common occupancy scale tends to infinity, the normalized `B` in (6) even tends to zero. The same polynomial depletion therefore remains.

This sharpens the boundary picture of FD-236--FD-237. FD-236 showed that normalizing response by the natural quadratic capacity scale `L_N4^j` was too coarse because it quotiented out the canonical Mertens repair itself. The present theorem works at the much finer bounded-row scale and shows that positive slack then cannot remain merely `o(1)` in relative band capacity: it is forced polynomially toward the lower capacity face. FD-237 says integrality is cheap for profiles with divisor-sized interior margin; the present result emphasizes that obtaining such an interior margin at deep bands is the genuinely difficult part.

## What this does and does not settle

The theorem supplies a quantitative target for the source-side obstruction, but it does not by itself complete it. To rule out the current reservoir countermodel one would still need a lower bound showing that the concrete Mertens correction requires more than

\[
O(x^{-\beta})
\]

of relative nonnegative slack on some divisor bands at scale `x`, uniformly in the growing-block regime. No such one-sided lower bound is proved here.

Conversely, the result rules out a softer escape: at bounded switched scale, a nonnegative cushion cannot retain a slowly vanishing fraction such as `1/log x` or `1/log log x` of every late dyadic band's linear capacity. Any such profile would eventually exceed the polynomial ceiling (9). Irregular redistribution inside a band does not help, because (29) already permits arbitrary cellwise placement.

The exponent is not claimed sharp. The number `23/24` comes from the crude universal bound `|M(q)|<=q` after the first two old bands. Inserting more exact finite Mertens maxima into (30), or using a stronger unconditional tail estimate, can improve the weighted contraction and hence `beta`. Such optimization would change only the numerical exponent, not the new qualitative fact that **bounded switched rows imply a fixed positive power of capacity depletion**.

The theorem also remains entirely on the nonnegative cushion side. Signed linear-capacity profiles can be switched-invisible by FD-231 and FD-238, so no analogue of (7) is possible without a one-sided hypothesis.

## Prior-art boundary

A targeted literature audit around discrete Volterra convolution stability found the expected classical exponential-stability framework for exponentially decaying kernels. That general theory is not load-bearing here. The switched state matrix (20), its spectrum, the positive divisor-tail inequality (29), and the weighted contraction (33) are all explicit within the Mathia divisor-response model.

No prior-art result located in the audit matches the arithmetic statement (7)--(9): a bounded period-three Farey/Mertens switched response forcing polynomial depletion of arbitrary nonnegative mass inside dyadic divisor bands. No general novelty is claimed for exponential stability or weighted convolution induction themselves, and no new external theorem is needed. Therefore this pass adds no dependency to `SOURCES.md`.

## Status

**Proved.** Bounded switched rows give the explicit response decay (28); the FD-230 positive Mertens-tail inequality becomes a strict weighted contraction for every `r>r_0`, and `r=23/24` yields the concrete polynomial capacity decay (7)--(9). The statement is quantitative, uniform over arbitrary within-band redistribution, and valid on growing finite blocks away from unavailable response rows. It does not imply RH and does not yet prove a source-level obstruction for the canonical Mertens repair.
