# XF-070 — center Parseval quotients ultra-infrared log-Vieta energy

**Status:** `EXACT-DERIVED` + `WEIGHTED-SOURCE-QUOTIENT` + `DESTINATION-MATCHED-TANGENT` + `STRUCTURAL/REPAIR`. XF-069 shows that translating the compact selector center through one periodic block recovers each raw periodic power sum exactly, but also isolates an ultra-infrared block `|k|\lesssim q^\delta` that the Xi source selector does not reach. A single fixed mode in that block can stay order one while the XF-062--XF-066 third-difference transition energy vanishes. The missing question is whether this harmlessness persists for the **whole growing unresolved block**, in a norm that is actually induced by the selector rather than chosen afterward.

It does. Parseval in the translated center turns the exact XF-069 coefficient identity into a weighted `ell^2` identity for all periodic power sums. With the XF-060--XF-066 selector weight, the induced coefficient weight is

\[
\boxed{
w_k\asymp_g \frac{k^4}{M^2},
\qquad M=q^2,
}
\tag{1}
\]

and, at the arithmetic lattice, its first variation is exactly the same `M^3 H^3` scaling as the destination third-difference energy. Moreover, for any bounded-displacement periodic state,

\[
\boxed{
\sum_{1\le |k|\lesssim q^\delta}
w_k|P_k|^2
=O_g\!\left(A^2q^{7\delta-4}\right),
}
\tag{2}
\]

where `A` is the displacement oscillation after quotienting uniform translation. Therefore every fixed

\[
0<\delta<\frac47
\tag{3}
\]

makes the entire source-invisible block asymptotically null whenever `A=O(1)`. For the concrete XF-059/XF-062 choice `\delta=1/2`,

\[
\boxed{
\text{ultra-infrared weighted cost}
=O_g(A^2q^{-1/2})=o(1).
}
\tag{4}
\]

Thus XF-069's fixed-mode control extends to the complete growing infrared sector in the **exact center-averaged selector geometry**. Raw smallness of `P_1,\ldots,P_{q^{1/2}}` is unnecessary at this measurement level.

The result does **not** yet finish the Vieta bridge. The power sums are logarithmic Vieta coordinates, not the diagonally evolving elementary Vieta coefficients of XF-067. The remaining dynamical problem is to transport this weighted quotient through the nonlinear change of coordinates, or to construct an equivalent quotient of the diagonal Vieta state. The nonperiodic Xi-to-periodic interface error from XF-069 also remains load-bearing.

## 1. Exact center Parseval identity

Use the XF-069 periodic index-coordinate model

\[
M=q^2,
\qquad
N=2M,
\qquad
x_{j+N}=x_j+N,
\tag{5}
\]

with

\[
\chi=\widehat g\in C_c^\infty((-1,1)),
\qquad
C_g:=\int_{\mathbb R}|\chi(u)|^2\,du>0.
\tag{6}
\]

For translated center `r`, define

\[
\mathcal S_r(\theta)
:=
\sum_{j\in\mathbb Z}
g\!\left(\frac{x_j-r}{M}\right)
e^{-i\theta(x_j-r)}.
\tag{7}
\]

Let

\[
\xi_k:=\frac{2\pi k}{N}=\frac{\pi k}{M},
\qquad
P_k:=\sum_{j=0}^{N-1}e^{-i\xi_kx_j},
\qquad k\in\mathbb Z.
\tag{8}
\]

XF-069 proves the exact center-Fourier coefficient formula

\[
\frac1N\int_0^N
\mathcal S_r(\theta)e^{-i\xi_kr}\,dr
=
\frac{M}{N}\chi\!\bigl(M(\theta-\xi_k)\bigr)P_k.
\tag{9}
\]

For any measurable frequency set `B`, put

\[
\|F\|_{X(B)}^2
:=
M\int_B(M\theta^2)^2|F(\theta)|^2\,d\theta
=M^3\int_B\theta^4|F(\theta)|^2\,d\theta
\tag{10}
\]

and average this exact selector norm over one translated-center period:

\[
\mathfrak X_B
:=
\frac1N\int_0^N
\|\mathcal S_r\|_{X(B)}^2\,dr.
\tag{11}
\]

Parseval in `r`, followed by `u=M(\theta-\xi_k)`, gives

\[
\boxed{
\mathfrak X_B
=
\frac1{4M^2}
\sum_{k\in\mathbb Z}|P_k|^2
\int_{U_{k,B}}
(\pi k+u)^4|\chi(u)|^2\,du,
}
\tag{12}
\]

where

\[
U_{k,B}
:=
\left\{u\in\operatorname{supp}\chi:
\xi_k+\frac{u}{M}\in B
\right\}.
\tag{13}
\]

Equation (12) is exact. It uses no root ordering, simplicity, small displacement, or heat evolution. It is simply the `L^2` version of XF-069's center extraction.

Because `\operatorname{supp}\chi\subset(-1,1)` while adjacent center frequencies have scaled spacing

\[
M(\xi_{k+1}-\xi_k)=\pi>2,
\tag{14}
\]

the sidebands

\[
I_k:=\left\{\theta:
|M(\theta-\xi_k)|<1
\right\}
\tag{15}
\]

are pairwise disjoint. Whenever `I_k\subset B`, its contribution to (12) is the full weight

\[
\boxed{
w_k
:=
\frac1{4M^2}
\int_{-1}^{1}
(\pi k+u)^4|\chi(u)|^2\,du.
}
\tag{16}
\]

For every `|k|\ge1`,

\[
\frac{C_g}{4M^2}(\pi|k|-1)^4
\le w_k\le
\frac{C_g}{4M^2}(\pi|k|+1)^4,
\tag{17}
\]

and hence

\[
\boxed{
w_k
=
\frac{C_g\pi^4}{4M^2}|k|^4
\left(1+O_g(|k|^{-1})\right).
}
\tag{18}
\]

This is the selector-induced weight; no destination norm has been inserted by hand.

## 2. The induced weight is the tangent third-difference weight

Linearize around the arithmetic lattice,

\[
x_j=j+\varepsilon a_j,
\qquad 0\le j<N.
\tag{19}
\]

For `k` not divisible by `N`, the unperturbed power sum vanishes and

\[
\left.\frac d{d\varepsilon}P_k\right|_{\varepsilon=0}
=-i\xi_k
\sum_{j=0}^{N-1}a_je^{-i\xi_kj}.
\tag{20}
\]

With the unitary DFT,

\[
\widehat a_k
:=N^{-1/2}
\sum_ja_je^{-i\xi_kj},
\tag{21}
\]

this gives

\[
\left|
\left.\frac d{d\varepsilon}P_k\right|_0
\right|^2
=N\xi_k^2|\widehat a_k|^2.
\tag{22}
\]

On any growing slow-frequency range with `|k|\to\infty` and `|k|/M\to0`, equations (18), (22), `N=2M`, and `|e^{i\xi_k}-1|\sim|\xi_k|` yield

\[
\boxed{
w_k
\left|
\left.\frac d{d\varepsilon}P_k\right|_0
\right|^2
=
\left(\frac{C_g}{2}+o(1)\right)
M^3|e^{i\xi_k}-1|^6
|\widehat a_k|^2.
}
\tag{23}
\]

The right side is exactly the modewise XF-065--XF-066 third-difference energy, up to the fixed window constant. Thus the center-Parseval metric is not merely infrared-weighted: its tangent geometry is the destination `H^3` geometry already used by the nonlinear selector frame.

There is also a direct Vieta interpretation. With the sign convention

\[
u_j:=e^{-2\pi i x_j/N},
\tag{24}
\]

put

\[
E(z):=\prod_{j=1}^N(1+u_jz)
=\sum_{m=0}^NE_mz^m.
\tag{25}
\]

Then the Newton generating identity used in XF-068 becomes

\[
\log E(z)
=
\sum_{k\ge1}(-1)^{k-1}\frac{P_k}{k}z^k.
\tag{26}
\]

Therefore (18) is equivalently an `H^3`-type weight

\[
w_k|P_k|^2
\asymp_g
\frac{k^6}{M^2}
\left|\frac{P_k}{k}\right|^2
\tag{27}
\]

on the logarithmic Vieta coefficients. This is the precise weighted/quotient source state suggested by XF-069 and MI-007.

## 3. Bounded displacement kills the whole unresolved infrared block

Now assume the periodic roots are a bounded displacement of the index lattice,

\[
x_j=j+c+b_j,
\qquad
\|b\|_{\ell^\infty}=A,
\tag{28}
\]

where the uniform translation `c` has been separated exactly as in XF-065. For every integer `k` with `0<|k|<N`, lattice cancellation gives

\[
\sum_{j=0}^{N-1}e^{-i\xi_kj}=0.
\tag{29}
\]

Hence

\[
P_k
=e^{-i\xi_kc}
\sum_{j=0}^{N-1}
e^{-i\xi_kj}
\left(e^{-i\xi_kb_j}-1\right),
\tag{30}
\]

and the elementary bound `|e^{-iy}-1|\le|y|` yields

\[
\boxed{|P_k|\le2\pi|k|A.}
\tag{31}
\]

Combining (17) and (31), for every `1\le J<N`,

\[
\boxed{
\sum_{1\le|k|\le J}w_k|P_k|^2
\le
C_\chi\frac{A^2}{M^2}
\sum_{1\le|k|\le J}|k|^6
\le
C_\chi' A^2\frac{J^7}{M^2}.
}
\tag{32}
\]

XF-059 permits a lower selector edge

\[
\theta_-=q^{-2+\delta}
\tag{33}
\]

for any fixed `\delta>0`. Since `M=q^2`, the corresponding periodic index is

\[
J_-=
\frac{M\theta_-}{\pi}+O(1)
=
\frac{q^\delta}{\pi}+O(1).
\tag{34}
\]

Only `O(1)` sidebands straddle the exact edge because of the fixed compact support of `\chi`; they obey the same bound. Therefore the entire source-unresolved block has

\[
\boxed{
\sum_{0<|k|\lesssim J_-}
w_k|P_k|^2
=O_g\!\left(A^2q^{7\delta-4}\right).
}
\tag{35}
\]

For every fixed `\delta<4/7` and `A=O(1)`, this is `o(1)`. At the standard `\delta=1/2` used in XF-062--XF-066,

\[
\boxed{
\sum_{0<|k|\lesssim q^{1/2}/\pi}
w_k|P_k|^2
=O_g(A^2q^{-1/2}).
}
\tag{36}
\]

This upgrades XF-069's single-mode example. The unresolved block may contain many individually non-small raw power sums, but its **total exact selector-induced destination-matched energy** still vanishes.

Under the convenient XF-066 state package

\[
A=O(1),
\qquad
\liminf Q_3(b)>0,
\tag{37}
\]

the omission is not only absolutely `o(1)` but negligible relative to any order-one transition-scale third-difference mass. Thus the infrared quotient is quantitatively compatible with the existing destination theorem.

## 4. What this repairs in the source-to-state bridge

XF-069 showed that requiring

\[
P_1,\ldots,P_{q^\delta}=o(1)
\tag{38}
\]

is the wrong source target: fixed low modes are outside the moving-line selector, barely damp over fixed heat time, and can remain order one while the transition energy vanishes. Equation (35) gives the correct replacement on the source-measurement side. The source theorem only needs to control the sidebands it actually reaches; the omitted infrared sidebands carry `o(1)` of the center-averaged `X_T` resource under bounded displacement.

Moreover, (12) makes the source-visible part especially clean. If `B` is chosen inside the XF-059 cone with a one-sideband margin at its ends, then

\[
\mathfrak X_B
=
\sum_{k:\,I_k\subset B}w_k|P_k|^2
+\text{two edge contributions},
\tag{39}
\]

with no cross terms between different `k`. Therefore a center-uniform actual-Xi source estimate plus the XF-069 periodic-interface comparison would control a **weighted square sum of all visible raw power sums at once**, rather than requiring a separate worst-mode estimate followed by a union bound.

This is useful because the weight in that square sum is already the correct tangent destination weight. The source side and the destination side now agree on which ultra-infrared directions are negligible.

## 5. Stress tests and evidence boundary

The bounded-displacement assumption is load-bearing only for (31)--(36), not for the exact Parseval identity (12). If `A` grows, the precise criterion is

\[
A^2q^{7\delta-4}=o(1).
\tag{40}
\]

Thus the result does not silently extend the `A=O(1)` XF-066 specialization to arbitrary finite-amplitude states.

The lattice cancellation in (29) requires `0<|k|<N`; the source-invisible and source-visible slow cones satisfy `|k|=o(N)`, so no aliasing index is encountered. Uniform translation is exactly harmless because it only multiplies `P_k` by a phase.

Equation (23) is a **tangent identification**, not a nonlinear equivalence between the weighted power-sum norm and `Q_3`. XF-065 supplies a separate nonlinear selector frame under small measurement parameters and slow-band concentration. The present finding does not replace those hypotheses.

Most importantly, the logarithmic Vieta coordinates `P_k/k` do not evolve diagonally under periodic heat. XF-067 diagonalizes the elementary coefficients `E_k`, and unresolved low `P_m` can enter higher `E_k` through Newton identities. Equation (35) proves that those low modes are negligible in the exact source/destination measurement geometry; it does **not** yet prove that the same quotient commutes with the diagonal heat flow. That is the remaining weighted-Vieta transport problem.

Finally, (12) is a periodic identity. It does not prove that the actual Xi zeros on a `\log^3 T` window admit a periodic surrogate with small center-averaged mismatch. The interface theorem isolated in XF-069 remains independently necessary.

## 6. Prior-art and novelty boundary

The passage from the center-Fourier coefficients (9) to the `L^2` identity (12) is classical Parseval/Moyal/Gabor analysis for translated windows and periodic Fourier series. The prior-art audit found the expected short-time Fourier/Gabor and Poisson-summation framework; no novelty is claimed for Parseval, periodic window decomposition, or the elementary bound (31). No external theorem is load-bearing because every identity used here is derived directly from XF-069 and finite Fourier algebra, so `SOURCES.md` does not need a new anchor.

The line-specific content is the scale match: the exact XF-060 selector weight turns center Parseval into the coefficient weight `k^4/M^2`; bounded displacement then makes the **entire** XF-059 source-invisible block cost `O(A^2q^{7\delta-4})`, with the threshold `\delta<4/7`; and the same weight linearizes to the XF-065--XF-066 `M^3H^3` transition energy. This converts MI-007's qualitative quotient principle into a quantitative source-side theorem.

## 7. Consequence for `xi_flow`

The ultra-infrared gap identified by XF-069 is now narrower than raw-coordinate language suggested. It is not necessary to force the missing `q^\delta` power sums to zero, and for `\delta=1/2` their whole selector-induced `H^3` cost is already `O(q^{-1/2})` under the bounded-displacement transition package.

The next bridge should therefore preserve this weighted quotient rather than reconstruct every raw low Vieta coordinate. Two tasks remain load-bearing: prove the center-averaged nonperiodic Xi-to-periodic interface estimate on the source-visible sidebands, and show that the exact diagonal Vieta heat flow transports a quotient equivalent to the weighted logarithmic state of (27) without reintroducing an order-one cost from the discarded infrared factor. Success on those two points would remove the artificial all-power-sums hypothesis from XF-068 while retaining the collision-safe nonlinear heat transport of XF-067.

No upper bound on `Lambda` follows here, and no RH implication is claimed.