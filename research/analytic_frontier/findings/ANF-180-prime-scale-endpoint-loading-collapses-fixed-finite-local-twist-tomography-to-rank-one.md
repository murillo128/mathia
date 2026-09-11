# ANF-180 — Prime-scale endpoint loading collapses fixed finite local twist tomography to rank one

**Status:** `EXACT-DERIVED + MATCHED-CONTROL + FINITE-TOMOGRAPHY-BARRIER + GROWING-COMPLEXITY-GATE`. `ANF-177`--`ANF-179` show that the prime-scale endpoint-loading control survives a full local twist coherence window, saturates every fixed local magnitude norm, and remains target-sized under every fixed finite derivative jet after carrier removal and natural rescaling. A remaining generic escape is to replace derivatives by some other finite collection of local linear probes: shifted samples, finite differences, compactly supported convolutions, or a hand-designed finite family of differential filters whose symbols might distinguish the packet even though monomials do not.

That escape also fails at fixed finite complexity. By allowing the loading span to grow by an arbitrarily slow factor while remaining `o(K)`, one can place the same prime-sized atoms inside a normalized frequency band whose width tends to zero. After the distinguished carrier is selected, every fixed finite family of continuous twist multipliers is then asymptotically constant across the occupied band. Consequently the entire measurement vector becomes a scalar multiple of the unfiltered profile, up to `o(a_X)` error.

Concretely, let

\[
 a_X:=\sqrt{\delta X\log X},
 \qquad
 A_X:=\log X,
 \qquad
 q_X:=\lceil\log X\rceil,
\]

and let `psi_1,...,psi_m` be a fixed finite family of continuous complex symbols on a neighborhood of some `xi_* in (0,1)`, with

\[
\psi_r(\xi_*)\ne0
\qquad(1\le r\le m).
\]

There is a prime-scale matched control carrying the same bow-scale endpoint memory as `ANF-175` for which, after demodulation and coherence rescaling,

\[
F_X(y)=A_X\sum_{j\in S}\zeta_j e^{-iy\xi_j},
\]

all occupied frequencies satisfy `xi_j=xi_*+o(1)` and, uniformly for `|y|<=c` with any fixed `c`,

\[
\boxed{
T_{\psi_r}F_X(y)
=
\psi_r(\xi_*)F_X(y)+o(a_X)
\qquad(1\le r\le m),
}
\]

where

\[
T_{\psi}F_X(y)
:=
A_X\sum_{j\in S}\psi(\xi_j)\zeta_j e^{-iy\xi_j}.
\]

Moreover `|F_X(y)|\gg a_X` throughout that fixed rescaled window. Hence

\[
\boxed{
\bigl(T_{\psi_1}F_X(y),\ldots,T_{\psi_m}F_X(y)\bigr)
=
F_X(y)\bigl(\psi_1(\xi_*),\ldots,\psi_m(\xi_*)\bigr)+o(a_X),
}
\]

uniformly in `y`. The fixed finite local measurement vector is therefore asymptotically **rank one** on an admissible dangerous packet. Any useful local-twist theorem must introduce arithmetic placement information, an `X`-dependent/growing family of probes, or a filter whose resolving complexity increases with the packet rather than remaining fixed.

## 1. Compress the occupied normalized frequencies without losing prime-scale loading

Work in the bow regime used in `ANF-175`--`ANF-179`, with

\[
K=X^{1-2\varepsilon+o(1)},
\qquad
0<\varepsilon<\frac1{16},
\qquad
A_0X^2\le U\le B_0X^2,
\tag{1}
\]

and fix `delta>0`. Put

\[
N:=\left\lceil\frac{4\sqrt3\,a_X}{A_X}\right\rceil.
\tag{2}
\]

Choose a positive sequence `d_X -> 0` so slowly that

\[
\frac{a_X}{d_X}=o(K),
\qquad
\frac{a_X}{d_XX}=o(d_X).
\tag{3}
\]

For example,

\[
d_X=\frac1{\log\log X}
\tag{4}
\]

works. Define

\[
B_X:=Nq_X,
\qquad
L_X:=\frac{B_X}{d_X}.
\tag{5}
\]

Thus

\[
B_X=\Theta_\delta(a_X),
\qquad
L_X=\Theta_\delta\!\left(\frac{a_X}{d_X}\right)=o(K),
\qquad
L_X=o(X).
\tag{6}
\]

Fix `xi_* in (0,1)`. For all sufficiently large `X`, place the `N` candidate sites with spacing `q_X` in a physical band of width `B_X` centered at `xi_*L_X`; for instance one may take

\[
j_r=
\left\lfloor\left(\xi_*-\frac{d_X}{2}\right)L_X\right\rfloor+r q_X,
\qquad 1\le r\le N.
\tag{7}
\]

Because `B_X=d_XL_X`, all these sites lie between `0` and `L_X` for large `X`. Partition the exact carrier rays

\[
v_j:=(X+j)^{-iU}
\tag{8}
\]

into six sectors of angular width `pi/3` and retain a sector containing at least `N/6` candidates. Call that active set `S`, and define

\[
P_X(t):=A_X\sum_{j\in S}(X+j)^{-it}.
\tag{9}
\]

Exactly as in `ANF-175`, projection onto the sector center gives

\[
|P_X(U)|
\ge
\frac{\sqrt3}{2}A_X|S|
\ge
\frac{\sqrt3}{12}A_XN
\ge a_X.
\tag{10}
\]

The prime-scale marginal control is unchanged. Every coefficient interval `J` of length `H` satisfies

\[
\sum_{j\in J}|c_j|
\le
A_X\left(\frac{H}{q_X}+1\right)
\ll H+\log X,
\tag{11}
\]

while the total `l^1` mass obeys

\[
M_X:=A_X|S|\ll_\delta a_X.
\tag{12}
\]

Thus the packet remains invisible to every bounded-test allowance larger than the absolute `a_X` scale, exactly as in `ANF-175`--`ANF-176`. The only cost of frequency compression is the slowly enlarged leading loading span `L_X`; by (6) that span still occupies `o(K)` of the endpoint.

## 2. The occupied normalized frequency band has width `o(1)`

Demodulate the common base carrier and use the loading span as the local frequency scale:

\[
G_X(t):=X^{it}P_X(t),
\qquad
W_X:=\frac{X}{L_X}.
\tag{13}
\]

Set

\[
F_X(y):=G_X(U+W_Xy)
=A_X\sum_{j\in S}\zeta_j e^{-iy\xi_j},
\tag{14}
\]

where

\[
\zeta_j:=\exp\!\left(-iU\log\left(1+\frac jX\right)\right),
\qquad
\xi_j:=\frac{X}{L_X}\log\left(1+\frac jX\right).
\tag{15}
\]

From (7),

\[
\frac{j}{L_X}=\xi_*+O(d_X)+O(L_X^{-1}).
\tag{16}
\]

Since `j<=L_X=o(X)`, the expansion `log(1+z)=z+O(z^2)` gives

\[
\xi_j
=
\frac{j}{L_X}+O\!\left(\frac{L_X}{X}\right).
\tag{17}
\]

Condition (3) makes `L_X/X=o(d_X)`, hence

\[
\boxed{
\sup_{j\in S}|\xi_j-\xi_*|=O(d_X)=o(1).
}
\tag{18}
\]

The physical twist window corresponding to a fixed `y` interval has width

\[
W_X
=\Theta_\delta\!\left(d_X\frac{X}{a_X}\right).
\tag{19}
\]

For the concrete choice (4),

\[
W_X\asymp
\frac{1}{\log\log X}\sqrt{\frac{X}{\log X}}
\longrightarrow\infty.
\tag{20}
\]

Thus the normalized band may shrink to a point while the physical local-twist window still grows without bound.

## 3. The unfiltered profile remains critically large on the compressed band

At `y=0`, equation (14) differs from `P_X(U)` only by a common unit phase, so

\[
|F_X(0)|\ge a_X.
\tag{21}
\]

For fixed `c>0` and `|y|<=c`, remove the common phase `e^{-iy\xi_*}`. Using `|e^{-iu}-1|<=|u|`, (12), and (18),

\[
\begin{aligned}
|F_X(y)-e^{-iy\xi_*}F_X(0)|
&\le
A_X\sum_{j\in S}
\left|e^{-iy(\xi_j-\xi_*)}-1\right|\\
&\le
cM_X\sup_{j\in S}|\xi_j-\xi_*|\\
&=o(a_X).
\end{aligned}
\tag{22}
\]

Therefore, uniformly for every fixed rescaled window,

\[
\boxed{
F_X(y)=e^{-iy\xi_*}F_X(0)+o(a_X),
\qquad
|F_X(y)|\ge(1-o(1))a_X.
}
\tag{23}
\]

The frequency compression does not weaken the endpoint charge; it makes the local twist profile closer to a single pure mode.

## 4. Every fixed finite continuous multiplier becomes scalar on the packet

Let `psi` be continuous near `xi_*`. Define its action on the finite exponential polynomial by

\[
T_\psi F_X(y)
:=
A_X\sum_{j\in S}\psi(\xi_j)\zeta_j e^{-iy\xi_j}.
\tag{24}
\]

Subtract `psi(xi_*)F_X(y)`:

\[
\left|
T_\psi F_X(y)-\psi(\xi_*)F_X(y)
\right|
\le
M_X
\sup_{j\in S}|\psi(\xi_j)-\psi(\xi_*)|.
\tag{25}
\]

By (18), continuity, and (12), the right-hand side is `o(a_X)`. Hence

\[
\boxed{
T_\psi F_X(y)
=
\psi(\xi_*)F_X(y)+o(a_X)
}
\tag{26}
\]

uniformly for `|y|<=c`. For a fixed finite family `psi_1,...,psi_m`, the same `o(a_X)` statement holds simultaneously, giving

\[
\boxed{
\mathbf T F_X(y)
=
F_X(y)\,\mathbf\psi(\xi_*)+o(a_X),
}
\tag{27}
\]

where

\[
\mathbf T F_X
:=(T_{\psi_1}F_X,\ldots,T_{\psi_m}F_X),
\qquad
\mathbf\psi(\xi_*):=(\psi_1(\xi_*),\ldots,\psi_m(\xi_*)).
\]

If every `psi_r(xi_*)` is nonzero, then (23) and (26) imply

\[
|T_{\psi_r}F_X(y)|\asymp_{\psi_r,\delta}a_X
\tag{28}
\]

uniformly on the same fixed `y` window. Thus every component of the finite measurement vector remains at its coefficient-generic maximal scale, while the vector carries asymptotically only the single scalar degree of freedom `F_X(y)`.

## 5. Fixed local samples, derivatives, finite differences, and compactly supported probes are covered

Equation (27) is not specific to derivative monomials. It immediately includes any fixed finite family of normalized constant-coefficient differential operators, whose symbols are polynomials in `xi`, and any fixed finite collection of local twist shifts, whose symbols are exponentials `e^{-is\xi}`. Finite differences and finite combinations of shifts have exponential-polynomial symbols.

More generally, a fixed compactly supported linear probe in the rescaled twist variable has a Fourier--Laplace symbol `psi(xi)`. Classical Paley--Wiener--Schwartz theory says such symbols are entire. A nonzero entire function cannot vanish on a real interval, so for any fixed finite family of nonzero compactly supported probes there is some `xi_* in (0,1)` at which all symbols are simultaneously nonzero. Choosing that `xi_*` in the construction above therefore gives the same rank-one collapse.

No Paley--Wiener theorem is needed for the core argument: (24)--(27) use only continuity of the finitely many symbols at one common nonzero point. The classical theory merely shows that the hypothesis automatically covers the usual finite local linear tomography built from compactly supported probes.

`ANF-179` is recovered by taking `psi_k(xi)=(-i\xi)^k` for finitely many fixed derivative orders. The present result is stronger: changing the finite basis of local measurements does not help. The obstruction is finite-dimensional local linear observation itself, not the choice of monomial coordinates.

## 6. The bow-scale completion and Fejer defect survive unchanged

All coefficients vanish after the final active site, which lies at `O(L_X)=o(K)`. Every later prefix therefore retains the charge (10), and the left endpoint completion again satisfies

\[
E_-(b)
\ge
(K-O(L_X))|P_X(U)|^2
\ge
(\delta-o(1))XK\log X.
\tag{29}
\]

The diagonal contribution remains lower order:

\[
K\sum_{j\in S}A_X^2
\ll
K a_X\log X
=o(XK\log X).
\tag{30}
\]

Thus the completion is genuinely off-diagonal. The consequences of `ANF-169` and `ANF-172` still apply: some dyadic block must carry a positive real shifted-correlation contribution of target order, equivalently a target-sized adjacent-scale Fejer slope defect.

Hence the rank-one local-tomography behavior (27) coexists with exactly the endpoint statistic the bow argument must rule out.

## 7. Stress tests, prior-art boundary, and what remains open

The shrinking frequency band is paid for by the factor `d_X^{-1}` in the loading span. This is not free, but any arbitrarily slow `d_X->0` satisfying (3) is enough for the finite-family collapse, while `L_X=o(K)` still leaves almost the entire endpoint over which to store the critical charge. The construction therefore does **not** contradict `ANF-175`'s sharp `Theta(a_X)` minimum loading scale under the prime marginal envelope; it deliberately loads more slowly to defeat a stronger observer.

The theorem is only a fixed-complexity obstruction. It does not cover a number of probes growing with `X`, symbols whose oscillation/zero structure becomes finer with `X`, or an arithmetic filter designed from the actual prime/rough source. It also does not claim that arbitrary nonlinear finite statistics fail: a nonlinear statistic can be engineered to vanish on the rank-one response manifold. Such a statistic would still need a source theorem showing why the physical residual cannot lie near that manifold.

The prior-art audit finds mature harmonic-analysis background for band-limited observability, sampling, Paley--Wiener theory, and Turan--Nazarov inequalities for exponential polynomials. No novelty is claimed for those general principles. They do not supply the Mathia-specific statement that a prime-scale, endpoint-dangerous matched control can simultaneously preserve the bow completion while collapsing any prescribed fixed finite local linear measurement family to rank one. Equations (2)--(30) are a direct construction, so no new external theorem is load-bearing and `SOURCES.md` does not require a new anchor.

The analytic frontier is therefore narrower than after `ANF-179`. **Replacing a fixed derivative jet by any other fixed finite local linear tomography cannot by itself detect the endpoint memory.** A viable twist-side theorem must make its resolving complexity grow with `X`, use a nonlocal statistic whose effective symbol variation resolves a shrinking normalized frequency band, or exploit source-specific arithmetic placement. The direct alternative remains control of the signed dyadic correlation / Fejer scale-slope defect itself.

## Falsification criterion

This finding is falsified if the compressed-band construction cannot simultaneously satisfy `L_X=o(K)`, the prime-scale interval envelope (11), endpoint charge (10), and normalized frequency compression (18), or if there exists a fixed finite continuous symbol family with a common nonzero point for which the rank-one estimate (27) fails. It is overclaimed if read as excluding `X`-dependent/growing-complexity filters, nonlinear source-specific statistics, or arithmetic placement theorems; those remain explicit escape routes.