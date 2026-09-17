# RE-185 — Chebyshev shell interpolation removes the growing-jet log loss

**Status:** `EXACT-DERIVED + CONSTRUCTIVE-CONTROL + ORDINARY-PRIME-SUPPORT + MULTIPLICITY-012 + GROWING-EULER-JET-MATCHING + KV-FIDELITY + TRANSIENT-ROBIN-AMBIGUITY + RE-184-STRENGTHENING + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-178, RE-182, RE-184.

`RE-184` shows that a growing number of exact Euler boundary jets can still be hidden by an ordinary-prime-supported `{0,1,2}` matched control, provided

\[
K\log(K+2)=o(V(p)),
\qquad
V(x):=\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}}.
\tag{1}
\]

Its proof already shows that the Vandermonde inverse itself costs only `e^{O(K)}`. The extra `\log K` comes from using unscaled monomials across a logarithmic repair interval of length `\asymp K`: shell variation and, especially, recentering the degree-`K` monomial basis between successive generations cost `e^{O(K\log K)}`.

That loss is not source rigidity. It is a coordinate-conditioning artifact.

There is an absolute constant `c_*>0` such that, for every sufficiently large selector prime `p` and every integer

\[
\boxed{
1\le K\le c_*V(p),
}
\tag{2}
\]

there exists an ordinary-prime-supported source `Q_{p,K}` with

\[
\boxed{m_{Q_{p,K}}(q)\in\{0,1,2\}}
\tag{3}
\]

having the same six properties as the `RE-184` construction:

1. it agrees with the ordinary prime source below `2p`;
2. it contains the canonical `RE-173` deletion packet `D_p\subset[2p,3p]` and has no repair below `16p`;
3. writing
   \[
   D_Q(s):=\sum_q(m_Q(q)-1)[-\log(1-q^{-s})],
   \]
   every boundary jet through depth `K` matches exactly,
   \[
   \boxed{
   D_{Q_{p,K}}^{(j)}(1+)=0,
   \qquad 0\le j\le K;
   }
   \tag{4}
   \]
4. the series in (4) are absolutely convergent, so termwise differentiation is legitimate;
5. for an absolute `C`, uniformly for `x\ge2p`,
   \[
   \boxed{
   |\vartheta_{Q_{p,K}}(x)-\vartheta(x)|
   \ll
   e^{CK}\left(\sqrt p+(1+\log x)^2\right),
   }
   \tag{5}
   \]
   after enlarging `C` if necessary; hence every fixed Korobov--Vinogradov envelope
   \[
   |\vartheta_{Q_{p,K}}(x)-\vartheta(x)|\ll_b x e^{-bV(x)}
   \tag{6}
   \]
   still holds for all sufficiently large `p` along the family (2);
6. before repair is visible, the normalized Robin coordinate retains the `RE-173` order-one excursion,
   \[
   \boxed{
   \mathcal A_{p,8p}(Q_{p,K})-
   \mathcal A_{p,8p}(P)\asymp1.
   }
   \tag{7}
   \]

In particular every depth

\[
\boxed{K=o(V(p))}
\tag{8}
\]

is admissible without choosing the small constant in (2). Thus the `K\log K=o(V)` range of `RE-184` is not the natural interpolation boundary. Exact source-faithful non-rigidity reaches a small constant fraction of the **KV shell scale** itself.

This is still far below the raw higher-jet capacity crossover from `RE-178`,

\[
K_{\rm cap}(p)\asymp\frac{\log p}{\log\log p},
\tag{9}
\]

because `V(p)=o(\log p/\log\log p)`. The new frontier is therefore no longer monomial conditioning. It is whether the KV shell scale is a genuine ordinary-prime quantization barrier or can itself be crossed by a different repair geometry.

## 1. Normalize the logarithmic repair window before interpolating

Retain the exact Euler kernels from `RE-184`,

\[
H(q):=\log\frac q{q-1},
\qquad
U_j(q):=(\log q)^j\sum_{n\ge1}n^{j-1}q^{-n}
\quad(j\ge1),
\tag{10}
\]

with `U_0=H`. At a repair baseline `x=e^L`, `RE-184` uses the centered monomial kernels corresponding to powers of

\[
\alpha:=\log(q/x).
\]

Instead use the degree-`m` Chebyshev polynomial on the normalized interval `0\le\alpha\le K`,

\[
P_{m,K}(\alpha)
:=T_m\!\left(\frac{2\alpha}{K}-1\right),
\qquad 0\le m\le K.
\tag{11}
\]

Write

\[
P_{m,K}(t)=\sum_{j=0}^m a_{mj}t^j
\]

and define the **exact** Chebyshev-centered Euler coordinates

\[
\Psi_{m,L}(q)
:=
\sum_{j=0}^m a_{mj}C_{j,L}(q),
\tag{12}
\]

where `C_{j,L}` are the exact centered kernels of `RE-184`. Since (11) is a triangular polynomial basis with nonzero diagonal, vanishing of all `\Psi_{m,L}` coordinates for `0\le m\le K` is exactly equivalent to vanishing of all centered monomial coordinates, hence to exact matching of the raw Euler jets `U_j`, `0\le j\le K`.

The asymptotic response is now bounded on the whole repair window. The uniform Euler estimate from `RE-184` gives

\[
\boxed{
\frac{\Psi_{m,L}(q)}{H(q)}
=P_{m,K}(\alpha)+\mathcal E_{m,L}(q),
}
\tag{13}
\]

and, for `m\le K`, `0\le\alpha\le K+O(1)`,

\[
\max_m|\mathcal E_{m,L}(q)|
\le
\exp\{-L+O(K\log(L/K+2)+K)\}.
\tag{14}
\]

For `K=O(V(p))` and `L\ge\log(16p)`, the exponent in (14) is `-\log p+o(\log p)`, because

\[
K\log\log p=O(V(p)\log\log p)=o(\log p).
\tag{15}
\]

Thus the exact Euler-factor remainder remains negligible throughout the larger range (2).

## 2. Gauss--Chebyshev shell nodes have a polynomial inverse

Let

\[
\theta_r:=\frac{(2r+1)\pi}{2(K+1)},
\qquad
z_r:=\cos\theta_r,
\qquad
\alpha_r:=\frac K2(1+z_r),
\qquad 0\le r\le K.
\tag{16}
\]

Place the `r`-th repair shell around

\[
q\asymp x e^{\alpha_r}.
\tag{17}
\]

The limiting response matrix is the discrete-cosine matrix

\[
A_K(m,r)=T_m(z_r)=\cos(m\theta_r).
\tag{18}
\]

Its inverse is explicit. Discrete cosine orthogonality gives, for a desired response vector `\rho=(\rho_m)_{0\le m\le K}`,

\[
w_r
=
\frac1{K+1}
\left(
\rho_0+2\sum_{m=1}^K\rho_m\cos(m\theta_r)
\right),
\tag{19}
\]

so

\[
\boxed{
\|w\|_1\le 2(K+1)\|\rho\|_\infty.
}
\tag{20}
\]

The interpolation cost is therefore polynomial, not exponential.

The node clustering at the endpoints causes no shell collision. The smallest separation between adjacent `\alpha_r` is `\asymp K^{-1}`. Use the same unconditional KV shell width as `RE-184`,

\[
\delta_x:=e^{-a_0V(x)/4}.
\tag{21}
\]

For `K=O(V(x))`,

\[
\delta_x=o(K^{-A})
\tag{22}
\]

for every fixed `A`, so the `K+1` shells are disjoint. Since `\alpha_r\le K-O(K^{-1})` and `K=o(\log x)`, the anchored prime-number-theorem estimate used in `RE-184` applies uniformly to every shell and gives the same available `H`-mass

\[
\sum_{q\in I_{x,r}}H(q)
\asymp\frac{\delta_x}{\log x}.
\tag{23}
\]

That remains overwhelmingly larger than the repair mass, which is `p^{-1/2+o(1)}` at the first generation.

## 3. Shell variation is only polynomial in the depth

On `[-1,1]`, the elementary Markov bound for the explicit Chebyshev polynomial gives

\[
|T_m'(z)|\le m^2.
\tag{24}
\]

Across one relative shell of width `\delta_x`, `\alpha` moves by `O(\delta_x)` and the normalized coordinate `z=2\alpha/K-1` moves by `O(\delta_x/K)`. Hence, uniformly for `m\le K`,

\[
\boxed{
\Delta P_{m,K}=O(K\delta_x).
}
\tag{25}
\]

Combining (14), (20), and (25), the exact shell response matrix differs from (18) by an operator whose relevant norm is

\[
\operatorname{poly}(K)e^{-a_0V(x)/4}
+
\exp\{-\log x+o(\log x)\}.
\tag{26}
\]

It follows by a Neumann-series perturbation of the explicit inverse (19) that, for all sufficiently large baselines,

\[
\boxed{
\|A_x^{-1}\|_{\infty\to1}\ll K.
}
\tag{27}
\]

This removes the first `e^{O(K\log K)}` loss in the quantitative implementation of `RE-184`.

## 4. Recentring a normalized Chebyshev basis costs only `e^{O(K)}`

The more important gain is between repair generations. Take

\[
R:=e^{K+3},
\qquad
x_{n+1}:=Rx_n.
\tag{28}
\]

This clears all shells from generation `n`. If `h=\log R=K+3`, then replacing the baseline `L` by `L+h` translates the normalized coordinate by

\[
z\mapsto z-\frac{2h}{K}=z-c_K,
\qquad
c_K=2+O(K^{-1}).
\tag{29}
\]

For every `m\le K`, expand `T_m(z-c_K)` back in the Chebyshev basis on `[-1,1]`. This basis change costs only a fixed-base exponential. Indeed, on `z\in[-1,1]` the translated argument lies in a fixed compact interval independent of `K`, so

\[
\sup_{|z|\le1}|T_m(z-c_K)|\le C_0^m
\tag{30}
\]

for an absolute `C_0`. The Chebyshev coefficient formula then bounds each coefficient by twice this supremum, and summing at most `m+1` coefficients gives

\[
\boxed{
\|\mathcal T_h\|_{\infty\to\infty}
\le e^{C_1K}.
}
\tag{31}
\]

This is an **exact algebraic** recentering statement for the coordinates (12), not an asymptotic statement about the Euler kernels: both bases are invertible polynomial combinations of the same raw kernels `U_0,\ldots,U_K`.

Equation (31) is the key improvement over the monomial estimate

\[
(1+h)^K=e^{\Theta(K\log K)}
\]

used in `RE-184`.

## 5. The initial debt is also tame in the normalized basis

At the first baseline `x_0=16p`, the deleted packet lies in `2p\le q\le3p`, so

\[
\alpha=\log(q/x_0)
\]

is confined to one fixed negative interval. Therefore the normalized argument in (11) is

\[
-1-O(K^{-1}).
\]

Using `T_m(\cosh u)=\cosh(mu)` and `\operatorname{arcosh}(1+c/K)=O(K^{-1/2})`, uniformly for `m\le K`,

\[
\left|T_m\!\left(-1-O(K^{-1})\right)\right|
\le e^{C_2\sqrt K}.
\tag{32}
\]

If `d_p\asymp(\sqrt p\log p)^{-1}` is the `RE-173` Mertens debt, the first Chebyshev-coordinate residual therefore satisfies

\[
\boxed{
M_0\ll e^{C_2\sqrt K}d_p.
}
\tag{33}
\]

After (20), the first-generation repair requires only

\[
\operatorname{poly}(K)e^{O(\sqrt K)}d_p=p^{-1/2+o(1)}
\tag{34}
\]

of signed `H`-mass when `K=O(V(p))`, still far below the shell supply (23).

## 6. Quantization now contracts up to a small constant fraction of `V`

Solve the real shell system at generation `n` and quantize it exactly as in `RE-184`: in each shell, select distinct ordinary primes until the requested signed `H`-mass is reached from below. Positive weights duplicate one copy; negative weights delete one copy. Thus all multiplicities remain in `{0,1,2}`.

By (25)--(27) and one-prime rounding, the residual at the same baseline obeys

\[
M'_n
\le
\left[
\operatorname{poly}(K)e^{-c_0V(x_n)}
+
 e^{-\log x_n+o(\log x_n)}
\right]M_n
+
\frac{\operatorname{poly}(K)}{x_n}
\tag{35}
\]

for some absolute `c_0>0`. Recentring with (31) gives

\[
M_{n+1}
\le
\exp\{C_3K-c_0V(x_n)+O(\log K)\}M_n
+
\frac{e^{C_3K}\operatorname{poly}(K)}{x_n}.
\tag{36}
\]

Choose `c_*>0` so small that

\[
(C_3+4)c_*<c_0.
\tag{37}
\]

Then (2), monotonicity of `V`, and (28) imply, after increasing the starting threshold,

\[
\boxed{
M_{n+1}\le R^{-3}M_n+
\frac{e^{C_4K}}{x_n}.
}
\tag{38}
\]

The same geometric argument as in `RE-184` now drives all `K+1` exact coordinates to zero. Since `K` is finite for each fixed `p`, the `R^{-3n}` and `x_n^{-1}` decay dominates every polynomial in `\log x_n` arising when converting back from the Chebyshev-centered basis to the raw Euler jets. Hence the correction series is absolutely convergent in every derivative `0\le j\le K`, and (4) follows exactly.

If only `K=o(V(p))` is desired, no small-constant bookkeeping is needed: the exponent in the first term of (36) is `-(c_0+o(1))V(x_n)`, which dominates any fixed multiple of `K`.

## 7. Source fidelity and the Robin excursion survive unchanged

The construction changes only the interpolation geometry of `RE-184`. It still uses actual ordinary primes supplied by the anchored unconditional PNT in disjoint shells, and it still realizes signed corrections only by deleting or duplicating one ordinary copy.

The total first-generation Chebyshev discrepancy is at most

\[
e^{O(K)}\sqrt p.
\tag{39}
\]

Later generations contribute at most `e^{O(K)}(1+\log x)^2` after summing the geometrically decaying repair mass and the one-prime rounding terms. This gives (5). Since `K=O(V(p))=o(\log p)`, for every fixed `b>0`,

\[
e^{O(K)}\sqrt p
=o\!\left(p e^{-bV(p)}\right),
\tag{40}
\]

and the same comparison only improves at later `x`. Thus the fixed KV source envelope remains intact.

Nothing changes below the first repair scale `16p`. The canonical deletion packet is therefore still fully visible at the transient cutoff `8p`, which proves the order-one Robin ambiguity (7).

## 8. What improved, and what did not

`RE-184` left a logarithmic gap between its constructive range and the KV shell scale. This finding removes that gap:

\[
K\log K=o(V(p))
\quad\longrightarrow\quad
K=o(V(p)),
\tag{41}
\]

and, with fixed constants tracked, to `K\le c_*V(p)`.

The mechanism is representation-sensitive but not source-free. The generic part is classical: normalize the interpolation interval, use Chebyshev nodes, discrete cosine orthogonality, and the bounded translation behavior of a Chebyshev basis. The source-specific part is what makes those numerical facts relevant here: the coordinates are exact linear combinations of Euler boundary jets, each real weight must be quantized by **ordinary primes** in a shell of relative width `e^{-\Theta(V)}`, multiplicities must remain nonnegative integers, and the resulting source must stay inside every fixed KV discrepancy envelope while preserving the pre-repair Robin excursion.

The result does **not** prove that `K\asymp V(p)` is sharp, and it does not approach the raw capacity scale (9). It shows only that the previous `\log K` loss was not intrinsic. At depth comparable with `V(p)`, the two genuinely exponential effects now meet on equal terms:

\[
\text{recentring cost }e^{CK}
\qquad\text{versus}\qquad
\text{prime-shell resolution }e^{-cV(p)}.
\tag{42}
\]

Crossing that balance would require either a repair architecture whose inter-generation transport is subexponential in `K`, a nonlocal/multiscale use of prime shells that avoids one full recentering per generation, or a proof that ordinary-prime quantization itself enforces an `e^{-\Theta(V)}` information limit.

## 9. Adversarial self-review

The main failure modes are quantitative rather than conceptual.

First, the translated Chebyshev basis must not secretly reintroduce `K^K`. Equation (31) avoids that trap without monomial conversion: the Chebyshev coefficient formula bounds the coefficients directly by the supremum of `T_m(z-c_K)` on `[-1,1]`, and `c_K` stays bounded. The resulting cost is genuinely `C^K\operatorname{poly}(K)`.

Second, the clustered Gauss--Chebyshev nodes must still support disjoint prime shells. Their minimum logarithmic separation is `\asymp K^{-1}`, whereas the actual relative shell width is `e^{-cV}`. For `K=O(V)`, the latter is smaller than every negative power of `K`; no endpoint collision occurs.

Third, changing polynomial basis must not turn the `n\ge2` Euler-factor tail into a dominant error. Equation (14) records the worst conversion loss. At `K=O(V(p))`, even `K\log\log p=o(\log p)`, so the `q^{-2}` origin of that tail still wins by a full power of `p`.

Fourth, (2) is an **existence range with a sufficiently small absolute constant**, not a statement that every fixed multiple of `V(p)` works. The constant depends on the fixed exponential rate in the anchored PNT shell error and on the fixed-base exponential recentering constant. No sharp constant is claimed.

Finally, this remains a matched-control non-rigidity result. It does not show that the actual prime source possesses such repairs, that Robin's inequality fails, or that exact Euler jets are source-native observables of the extremal problem. Its use is negative and structural: even a number of exact scalar boundary constraints growing to the KV shell scale can fail to identify the ordinary prime source.

## 10. Prior-art audit

The interpolation ingredients used here are standard approximation theory: Gauss--Chebyshev nodes, discrete cosine orthogonality, the bound `|T_m'|\le m^2` on `[-1,1]`, and fixed-base growth of translated Chebyshev polynomials. They are derived above in the only forms needed, so no new external theorem is load-bearing.

A targeted prior-art search found the expected literature on Chebyshev/Vandermonde conditioning and discrete cosine interpolation, but no result matching the source-specific statement here: exact growing Euler-jet interpolation by ordinary-prime shell edits with `{0,1,2}` multiplicity, fixed KV fidelity, and a preserved transient Robin excursion. `SOURCES.md` therefore needs no new dependency.

## Conclusion

The `K\log K` restriction in `RE-184` came from asking unscaled monomials to carry information across a logarithmic interval whose length itself grows like `K`. Normalizing that interval and interpolating in Chebyshev coordinates changes the transport cost from `e^{O(K\log K)}` to `e^{O(K)}`. The matched-control construction consequently survives through every `K=o(V(p))`, and through a sufficiently small constant fraction of `V(p)`.

The remaining gap to `K_{\rm cap}(p)` is therefore not an interpolation-conditioning gap. The next credible obstruction has to live at or beyond the **KV shell-resolution scale itself**, or exploit arithmetic information not captured by finite/growing Euler boundary jets.