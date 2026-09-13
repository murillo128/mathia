# WI-277 — Commensurate cross-cut shifts obey a sharp finite-Toeplitz reserve

## Status

- **Evidence:** `EXACT-DERIVED + CLASSICAL-OPERATOR + MULTI-SHIFT-BOOTSTRAP + SHARP-RELAXATION + PRIOR-ART-AUDITED`.
- **Scope:** extends the one-shift compact-support reserve of `WI-276` to any finite nonnegative combination of commensurate cross-cut shifts. The resulting coefficient is the top eigenvalue of one finite symmetric Toeplitz matrix, so several firstness constraints can be consumed jointly instead of taking their scalar maximum.
- **What it does not claim:** this does not yet prove that the first-crossing source reserve exceeds the archimedean budget `K_+`, does not prove that a first null mode is one-signed, and does not force a prime-lag overlap on the sign-changing branch. It is a sharp support-only compatibility constraint for several shifts at once.
- **Novelty boundary:** finite-shift/numerical-radius and truncated-Toeplitz machinery is classical. The Mathia deduction is the simultaneous insertion of that finite Toeplitz extremal problem into the cross-cut family from `WI-276`, including an exact two-shift regime where the joint reserve is strictly stronger than both separately sharp one-shift reserves. A targeted audit found no prior source for this localized-Weil application; no priority claim is made.

## Claim

Retain the first-crossing setup and notation of `WI-276`. Thus `a=a_*` is an attained first unrestricted localized Weil crossing, `v` is a normalized real zero mode, the complementary cut energy `Q_t` is nonnegative and supported in `[-a,a]`, and

\[
f(t):=\sqrt{Q_t},\qquad
\mathcal S_v=\|f\|_2^2.
\tag{1}
\]

Fix `0<r<a`, put `h=2r`, and set

\[
N:=\left\lceil\frac{2a}{h}\right\rceil
=\left\lceil\frac a r\right\rceil.
\tag{2}
\]

For a finite family of nonnegative weights

\[
\alpha_k\ge0,\qquad
1\le k\le N-1,
\tag{3}
\]

where only indices with `kr<a` are used, let `J_N` be the `N x N` unilateral shift and define

\[
H_N(\alpha):=
\frac12\sum_k\alpha_k
\left(J_N^k+(J_N^*)^k\right),
\qquad
\rho_N(\alpha):=\lambda_{\max}(H_N(\alpha)).
\tag{4}
\]

Then the first-crossing source reserve obeys

\[
\boxed{
\mathcal S_v
\ge
\frac{\sum_k\alpha_k\,k r\,\lambda_{kr}}
{\sum_k\alpha_k+\rho_N(\alpha)}.
}
\tag{5}
\]

The coefficient in the weighted correlation step is sharp for arbitrary nonnegative compactly supported cut-energy profiles:

\[
\boxed{
\sup_{\substack{f\ge0,\ f\ne0\\
\operatorname{supp}f\subset[-a,a]}}
\frac{
\sum_k\alpha_k
\int_{\mathbb R}f(t)f(t+2kr)\,dt
}{
\|f\|_2^2
}
=
\rho_N(\alpha).
}
\tag{6}
\]

Thus (5) uses no hidden regularity of the Suzuki null mode. It records exactly the compatibility forced by asking one supported profile `f` to realize several translated correlations simultaneously.

Because (5) is homogeneous in `alpha`, the optimization may be normalized by `sum alpha_k=1`.

## 1. Commensurate translated cuts form one nilpotent shift model

Let `T=T_h` be the truncated translation from `WI-276` on `L^2(-a,a)`,

\[
(Tg)(t)=g(t+h)
\]

when both arguments lie in `(-a,a)`, and zero otherwise. Since the support interval is convex, composition introduces no extra truncation beyond the endpoints:

\[
T^k=T_{kh}.
\tag{7}
\]

Consequently

\[
I_{kh}:=
\int_{\mathbb R}f(t)f(t+kh)\,dt
=
\langle f,T^k f\rangle.
\tag{8}
\]

Decompose `(-a,a)` into translation orbits modulo `h`. Almost every fiber is a finite chain of length at most `N=ceil(2a/h)`, and a positive-measure family of fibers has length exactly `N`. On a chain of length `n`, the self-adjoint operator

\[
\frac12\sum_k\alpha_k(T^k+(T^*)^k)
\]

is exactly the `n x n` principal submatrix `H_n(alpha)` of `H_N(alpha)`. Cauchy interlacing therefore gives

\[
\lambda_{\max}(H_n(\alpha))
\le \rho_N(\alpha).
\tag{9}
\]

Integrating over the fibers yields the exact weighted support inequality

\[
\boxed{
\sum_k\alpha_k I_{kh}
\le \rho_N(\alpha)\,\mathcal S_v.
}
\tag{10}
\]

This is the multishift replacement for applying Haagerup--de la Harpe separately to each `I_{kh}`.

## 2. Sharpness survives the nonnegative-profile restriction

The matrix `H_N(alpha)` is real symmetric with nonnegative entries. Hence a top eigenvector

\[
b=(b_0,\ldots,b_{N-1})
\]

may be chosen nonnegative. Because `2a>(N-1)h`, choose a sufficiently short measurable set `E` such that

\[
E,E+h,\ldots,E+(N-1)h
\]

are disjoint and contained in `(-a,a)`. Put

\[
f=\sum_{j=0}^{N-1}b_j\,\mathbf1_{E+jh}.
\tag{11}
\]

Then direct counting gives

\[
\frac{\sum_k\alpha_k I_{kh}}{\|f\|_2^2}
=
\frac{\langle b,H_N(\alpha)b\rangle}{\|b\|_2^2}
=
\rho_N(\alpha),
\tag{12}
\]

which proves (6). Therefore no smaller coefficient than `rho_N(alpha)` is available from compact support and `Q_t>=0` alone for that chosen linear combination.

This sharpness is compatible with, but stronger in organization than, the one-shift sharpness of `WI-276`: each individual shift has its own extremizer, while the joint problem asks for one profile that serves all shifts simultaneously.

## 3. Summed firstness gives the source reserve

Apply the upper half of the `WI-276` cross-cut squeeze at radius `kr`:

\[
\mathcal F_v(kr)
\le
\mathcal S_v+I_{kh}.
\tag{13}
\]

Firstness independently gives

\[
\mathcal F_v(kr)\ge kr\,\lambda_{kr}.
\tag{14}
\]

Multiply by `alpha_k`, sum, and use (10):

\[
\sum_k\alpha_k\,kr\,\lambda_{kr}
\le
\left(\sum_k\alpha_k\right)\mathcal S_v
+\sum_k\alpha_k I_{kh}
\le
\left(\sum_k\alpha_k+\rho_N(\alpha)\right)\mathcal S_v.
\tag{15}
\]

This proves (5).

If only one `alpha_k` is nonzero, (5) reduces to the corresponding one-shift `WI-276` reserve. Indeed `J_N^k` decomposes into chains whose maximal length is `ceil(N/k)=ceil(a/(kr))`, reproducing the coefficient

\[
\cos\frac{\pi}{\lceil a/(kr)\rceil+1}.
\tag{16}
\]

## 4. Two shifts can beat both individually sharp one-shift bounds

The gain is already explicit in the smallest nontrivial case. Suppose

\[
\frac a3\le r<\frac a2,
\]

so `N=3` and both radii `r` and `2r` are active. Normalize

\[
\alpha_1=t,\qquad
\alpha_2=1-t,\qquad
0\le t\le1.
\]

Then

\[
H_3(t)=
\frac12
\begin{pmatrix}
0&t&1-t\\
t&0&t\\
1-t&t&0
\end{pmatrix},
\tag{17}
\]

and its largest eigenvalue is exactly

\[
\rho_3(t)=
\frac{1-t+\sqrt{(1-t)^2+8t^2}}{4}.
\tag{18}
\]

Write

\[
L_1=r\lambda_r,\qquad
L_2=2r\lambda_{2r},\qquad
x=\frac{L_2}{L_1}
=\frac{2\lambda_{2r}}{\lambda_r}.
\tag{19}
\]

The normalized two-shift reserve is

\[
R_x(t)
=
L_1\,
\frac{t+(1-t)x}{1+\rho_3(t)}.
\tag{20}
\]

Its endpoint derivatives are

\[
\frac{R_x'(0)}{L_1}
=
\frac23-\frac{4x}{9},
\tag{21}
\]

and

\[
\frac{R_x'(1)}{L_1}
=
(\sqrt2-2)x+\frac{15}{2}-5\sqrt2.
\tag{22}
\]

Therefore, whenever

\[
\boxed{
\frac52-\frac{5\sqrt2}{4}
<
\frac{2\lambda_{2r}}{\lambda_r}
<
\frac32,
}
\tag{23}
\]

the derivative at `0` is positive and the derivative at `1` is negative. Hence some interior `0<t<1` gives

\[
R_x(t)>
\max\{R_x(0),R_x(1)\}.
\tag{24}
\]

The joint Toeplitz reserve is then strictly stronger than both separately sharp one-shift reserves.

For the neutral ratio `x=1`, the exact choice

\[
t=\frac29
\]

gives

\[
\rho_3(2/9)=\frac49,
\qquad
R_1(2/9)=\frac9{13}L_1,
\tag{25}
\]

whereas the better endpoint is only

\[
R_1(0)=\frac23L_1
\]

and the other endpoint is `(2-sqrt(2))L_1`. Thus the gain is not a convex re-averaging of scalar `WI-276` bounds. It is the incompatibility of their separate support extremizers.

Equation (23) is only a sufficient profile condition. This finding does not assert that Suzuki's actual eigenvalue curve satisfies it at some `r`; that is now a concrete spectral-profile test.

## 5. Consequence for the first-crossing program

`WI-276` closed the one-shift support-only optimization: no individual correlation `I_h` can have a uniformly smaller coefficient without extra structure. The present result shows that this does **not** close support-only information at several shifts, because the individually sharp extremizers need not be jointly compatible.

For each fixed base radius `r`, the entire commensurate family is reduced to a finite eigenvalue optimization,

\[
\sup_{\alpha_k\ge0}
\frac{\sum_k\alpha_k\,kr\,\lambda_{kr}}
{\sum_k\alpha_k+\rho_N(\alpha)}.
\tag{26}
\]

This is the exact next support-only reserve to compare with `R_harm(a)` and the one-signed archimedean budget `K_+`. A certified profile estimate making the maximum exceed `K_+` would force positive weighted prime overlap on the one-signed branch. Conversely, if an admissible `lambda_r` profile keeps the optimized Toeplitz reserve and `R_harm(a)` below `K_+`, then generic compact-support multishift consistency is exhausted and the route must use genuine Suzuki source/eigenfunction structure, the signed-source multiplier form, or the sign-changing archimedean geometry.

The theorem is also a boundary result: for every fixed nonnegative weight vector `alpha`, (6) is sharp in the abstract supported-profile class. Further improvement cannot come from replacing `rho_N(alpha)` by a universally smaller support-only coefficient.

## Prior art and novelty audit

- Uffe Haagerup and Pierre de la Harpe, **The numerical radius of a nilpotent operator on a Hilbert space**, *Proc. Amer. Math. Soc.* 115 (1992), 371--379, DOI `10.1090/S0002-9939-1992-1072339-6`, is the classical sharp one-shift theorem used in `WI-276`.
- Pamela Gorkin and Jonathan R. Partington, **Norms of Truncated Toeplitz Operators and Numerical Radii of Restricted Shifts**, *Comput. Methods Funct. Theory* 19 (2019), 487--508, DOI `10.1007/s40315-019-00282-z`, is representative classical prior art for computing numerical radii of restricted shifts through finite/truncated Toeplitz operators.
- Saeed Karami, **Numerical Radius Of The Powers Of Jordan Block And Its Application For Eigenvalue Of Nonnegative Symmetric Toeplitz Matrices**, *Applied Mathematics E-Notes* 23 (2023), 537--543, records the individual-power/Jordan-block side of the same finite-matrix landscape.
- `WI-276` supplies the load-bearing localized-Weil identity `F_v(r)<=S_v+I_{2r}` and the one-shift sharp support reduction. The direct-integral/fiber reduction above is elementary finite-shift operator theory, not claimed as a new general operator theorem.
- A targeted search for nilpotent/truncated-shift polynomial numerical radius, finite Toeplitz numerical-radius bounds, and the localized Weil/Suzuki first-crossing setting found classical operator-theory machinery but no source deriving (5), (23), or their first-crossing consequence. This is a novelty audit, not a priority claim.

## Audit and falsification tests

The exact claim can be killed by any of the following:

1. exhibit a compactly supported nonnegative `f` and nonnegative `alpha` violating (10);
2. show that the truncated translations fail the semigroup identity `T_{kh}=T_h^k` on the interval model used by `WI-276`;
3. show that an orbit fiber can have length greater than `ceil(2a/h)`;
4. show that the maximal-chain Perron construction does not realize the Rayleigh quotient in (12);
5. find an algebraic error in (18)--(23).

Each step is finite or elementary once the `WI-276` cross-cut inequality is accepted. No numerical quadrature or external computer certificate is used.

## Formalization disposition

The finite matrix statement `(4)--(6)` is bounded for fixed `N`, but the useful theorem here includes the `L^2` orbit-fiber reduction from truncated translations to all chain lengths. Formalizing only the matrix eigenvalue calculation would not verify the load-bearing analytic bridge, while formalizing the full direct-integral statement would require disproportionate measure/operator infrastructure relative to its present role. No automatic Lean handoff is opened at this stage.
