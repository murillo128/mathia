# RE-188 — Logarithmic Chebyshev growth cuts the Euler-jet spatial tariff to linear

**Status:** `EXACT-DERIVED + CONSTRUCTIVE-CONTROL + ORDINARY-PRIME-SUPPORT + MULTIPLICITY-012 + GROWING-EULER-JET-MATCHING + LINEAR-CHEBYSHEV-WINDOWS + KV-FIDELITY + TRANSIENT-ROBIN-AMBIGUITY + RE-187-STRENGTHENING + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-173, RE-186, RE-187.

`RE-187` widened the Chebyshev repair window to

\[
W\asymp \frac{K^2}{\log p}
\]

in order to suppress the exact prime-power tail of the first `K` Euler boundary jets. That quadratic spatial tariff is not intrinsic even to the same Chebyshev shell architecture. It comes from the coarse exterior estimate

\[
|T_m(2v-1)|\le e^{2m\sqrt v}.
\]

Using the exact logarithmic exterior growth of `T_m` instead, a window of width only

\[
\boxed{W=4K}
\tag{1}
\]

already makes every prime-power mode exponentially small. The rest of the `RE-187` microstepped ordinary-prime construction then survives unchanged at the level of scales.

Let

\[
L_p:=\log(16p),
\]

and assume

\[
\boxed{
K=o\!\left((\log p)^{5/3}(\log\log p)^{1/3}\right).
}
\tag{2}
\]

For every sufficiently large selector prime `p` and every integer `K\ge1` satisfying (2), there exists an ordinary-prime-supported source `Q_{p,K}` with

\[
\boxed{m_{Q_{p,K}}(q)\in\{0,1,2\}}
\tag{3}
\]

such that:

1. `Q_{p,K}` agrees with the ordinary prime source below `2p`;
2. it contains the canonical `RE-173` deletion packet `D_p\subset[2p,3p]` and has no repair below `16p`;
3. for
   \[
   D_Q(s):=\sum_q(m_Q(q)-1)[-\log(1-q^{-s})],
   \]
   every boundary derivative through depth `K` matches exactly,
   \[
   \boxed{D_Q^{(j)}(1+)=0,\qquad 0\le j\le K;}
   \tag{4}
   \]
4. the correction series is absolutely convergent in every derivative in (4);
5. for every fixed `b>0`, once `p` is sufficiently large,
   \[
   \boxed{
   |\vartheta_Q(X)-\vartheta(X)|\ll_b X e^{-bV(X)}
   \qquad(X\ge2p),
   }
   \tag{5}
   \]
   where
   \[
   V(X)=\frac{(\log X)^{3/5}}{(\log\log X)^{1/5}};
   \]
6. before any repair is visible, the canonical selector-scale Robin coordinate retains the order-one excursion of `RE-173`,
   \[
   \boxed{
   \mathcal A_{p,8p}(Q_{p,K})-
   \mathcal A_{p,8p}(P)\asymp1.
   }
   \tag{6}
   \]

Thus the sufficient scalar non-rigidity depth improves from the `RE-187` range

\[
K=o\!\left((\log p)^{4/3}(\log\log p)^{1/6}\right)
\]

to (2). Within the full-window Gauss--Chebyshev repair used by `RE-185`--`RE-187`, the spatial width scale is also sharp up to constants in the deep regime `K\gg\log p`: keeping the exact shell matrix uniformly close to its DCT model requires `W=\Omega(K)`. Hence the previous `K^2/\log p` tariff was a proof artifact, while a linear tariff is the correct scale for this representation.

## 1. Exact resummation from RE-187

Retain the positive Euler kernels

\[
H(q):=\log\frac q{q-1},
\qquad
U_j(q):=(\log q)^j\sum_{n\ge1}n^{j-1}q^{-n}
\quad(j\ge1),
\qquad U_0=H,
\]

and the centered kernels at baseline `x=e^L`,

\[
C_{j,L}(q)
:=
\sum_{r=0}^j\binom jr(-L)^{j-r}U_r(q).
\]

As in `RE-187`, exact resummation gives

\[
C_{j,L}(q)
=
\sum_{n\ge1}\frac{q^{-n}}n(n\log q-L)^j.
\tag{7}
\]

For a width `W>0`, put

\[
P_{m,W}(t):=T_m\!\left(\frac{2t}{W}-1\right),
\qquad
\Psi_{m,L,W}(q)
:=
\sum_{j=0}^m a_{mj}^{(W)}C_{j,L}(q),
\]

where `P_{m,W}(t)=\sum_j a_{mj}^{(W)}t^j`. Then

\[
\boxed{
\Psi_{m,L,W}(q)
=
\sum_{n\ge1}\frac{q^{-n}}n
P_{m,W}(n\log q-L).
}
\tag{8}
\]

If `q=e^{L+\alpha}` with `0\le\alpha\le W`, the `n=1` term is exactly `q^{-1}P_{m,W}(\alpha)`. Only the genuine prime powers `n\ge2` perturb the ideal Chebyshev response.

## 2. Exact exterior growth makes `W=4K` sufficient

For `z\ge1`,

\[
T_m(2z-1)
=
\cosh\!\left(m\,\operatorname{arcosh}(2z-1)\right),
\]

so

\[
\boxed{
|T_m(2z-1)|
\le
\exp\!\left(m\log(4z)\right).
}
\tag{9}
\]

Indeed `\operatorname{arcosh}x\le\log(2x)` for `x\ge1`. This logarithmic estimate, rather than the square-root majorant used in `RE-187`, is the decisive change.

Fix `W=4K`, `m\le K`, `q=e^{L+\alpha}`, and for a prime-power mode `n\ge2` write

\[
A:=(n-1)(L+\alpha),
\qquad
z:=\frac{(n-1)L+n\alpha}{W}
=\frac{A+\alpha}{W}.
\tag{10}
\]

Since `A\ge\alpha`,

\[
z\le\frac{2A}{W}=\frac{A}{2K}.
\tag{11}
\]

If `z\le1`, then the Chebyshev factor is bounded by one. If `z>1`, then `A>2K`. Put `y=A/K>2`. From (9)--(11),

\[
\log |P_{m,W}(n\log q-L)|
\le
K\log\frac{2A}{K}
=K\log(2y).
\]

For `y\ge2`, the elementary inequality

\[
\log(2y)\le\frac34y
\tag{12}
\]

holds because it is true at `y=2` and the difference `(3/4)y-\log(2y)` is increasing thereon. Hence

\[
\boxed{
|P_{m,W}(n\log q-L)|
\le e^{3A/4}
}
\tag{13}
\]

whenever `z>1`.

After dividing by `H(q)\ge q^{-1}`, the normalized `n`-th prime-power contribution is therefore at most

\[
q^{1-n}|P_{m,W}(n\log q-L)|
\le e^{-A/4}.
\tag{14}
\]

The denominator correction is no larger: using

\[
\frac{\Psi_{m,L,W}(q)}{H(q)}-P_{m,W}(\alpha)
=
\frac1{H(q)}
\sum_{n\ge2}\frac{q^{-n}}n
\left[
P_{m,W}(n\log q-L)-P_{m,W}(\alpha)
\right],
\tag{15}
\]

and `|P_{m,W}(\alpha)|\le1`, summation of the geometric tail yields

\[
\boxed{
\max_{m\le K}
\left|
\frac{\Psi_{m,L,W}(q)}{H(q)}-P_{m,W}(\alpha)
\right|
\ll e^{-(L+\alpha)/4}
\le e^{-L/4}.
}
\tag{16}
\]

Thus exact prime powers impose only a **linear** width tariff.

## 3. The linear scale is necessary for this Chebyshev frame

The improvement is not merely an upper-bound trick. Consider the rightmost ideal Gauss--Chebyshev node

\[
\alpha_0
=
\frac W2
\left(1+\cos\frac{\pi}{2(K+1)}\right).
\tag{17}
\]

For all `K\ge1`, `\alpha_0\ge3W/4`. Take the highest mode `m=K`. For the `n=2` prime-power term the exterior Chebyshev argument is

\[
\frac{2(L+2\alpha_0)}W-1
\ge2.
\tag{18}
\]

Hence

\[
T_K\!\left(\frac{2(L+2\alpha_0)}W-1\right)
\ge
T_K(2)
=
\cosh(K\operatorname{arcosh}2)
\gg e^{c_0K},
\tag{19}
\]

where `c_0=\operatorname{arcosh}2>0`.

At this node all exterior prime-power values of `T_K` are positive and exceed the interior value `P_{K,W}(\alpha_0)\in[-1,1]`, so the terms in (15) do not cancel. Also `H(q)\le2q^{-1}` for large `q`. The `n=2` term alone therefore gives

\[
\left|
\frac{\Psi_{K,L,W}(q)}{H(q)}-P_{K,W}(\alpha_0)
\right|
\gg
\exp(c_0K-L-W).
\tag{20}
\]

Consequently, if `K/L\to\infty` and the exact shell matrix is required even to stay uniformly `O(1)`-close to its ideal DCT matrix, then

\[
\boxed{W\ge(c_0-o(1))K.}
\tag{21}
\]

This lower bound concerns the **specific full-window Gauss--Chebyshev representation**. It is not a universal lower bound for every possible nonlinear or nonuniform repair architecture. Within the representation actually used by `RE-185`--`RE-187`, however, `W\asymp K` is sharp up to constants.

## 4. Microstepped prime shells still fit at linear width

Use the `RE-186`--`RE-187` microstep scales

\[
h:=e^{-a_0V(p)/8},
\qquad
x_n:=16p\,e^{nh},
\qquad
\delta_n:=e^{-a_0V(x_n)/4}.
\tag{22}
\]

Place the `K+1` scaled Gauss--Chebyshev nodes across `[0,W]` and perturb them by at most `h` into distinct residue classes modulo `h`, exactly as in `RE-187`. With `W=4K`, the smallest ideal node spacing is

\[
\asymp\frac{W}{K^2}\asymp\frac1K.
\tag{23}
\]

Under (2), `K` is only polylogarithmic in `p`, while `h` is smaller than every negative power of `\log p`. Thus

\[
\delta_n\le h^2=o(h/K),
\]

and all shells remain globally disjoint. Every ordinary prime is still edited at most once, so multiplicities remain in `{0,1,2}`.

The ideal shell matrix is the same DCT matrix as before and still satisfies

\[
\|A_K^{-1}\|_{\infty\to1}\ll K.
\tag{24}
\]

Moreover

\[
\left|P'_{m,W}(\alpha)\right|
\ll\frac{m^2}{W}
\ll K,
\tag{25}
\]

so the node perturbation and within-shell errors are `o(1)` after multiplication by `h+\delta_n`. Equation (16) makes the exact prime-power error even smaller. Recentring one generation by `h` costs

\[
\|\mathcal T_{h,W}\|_{\infty\to\infty}
\ll
K\exp\!\left(CK\sqrt{h/W}\right)
=O(K),
\tag{26}
\]

because `K\sqrt{h/W}=O(\sqrt{Kh})=o(1)`.

Therefore the same exact shell solve, ordinary-prime quantization, and contraction used in `RE-187` gives

\[
M_{n+1}
\le
\frac13M_n+O\!\left(\frac{K^2}{x_n}\right).
\tag{27}
\]

No new recurrence loss appears.

## 5. The initial selector debt remains subcritical

The deletion packet `D_p\subset[2p,3p]` lies a fixed logarithmic distance to the left of the first repair baseline. In the scaled interval of width `W=4K`, that distance is only `O(1/W)` beyond the left endpoint. The exact Chebyshev exterior formula therefore gives the same bound as in `RE-187`, now with

\[
M_0
\le
\exp\!\left(O\!\left(\frac K{\sqrt W}\right)\right)d_p
=
\exp(O(\sqrt K))d_p,
\tag{28}
\]

where

\[
d_p\asymp\frac1{\sqrt p\log p}.
\]

Condition (2) implies `\sqrt K=o(\log p)`, so

\[
\boxed{M_0=p^{-1/2+o(1)}.}
\tag{29}
\]

The weighted prime supply in every KV shell is exponentially larger than this requested mass, even at the far-right nodes. Iterating (27) drives the exact residual to zero. Since `K` is finite for each fixed `p`, the finite triangular change of coordinates back to raw Euler derivatives is exact, giving (4) and absolute convergence through depth `K`.

## 6. The remaining range is set by spatial KV invisibility

With the linear window, the first repair reservoir reaches logarithmic height at most

\[
S_p:=L_p+4K.
\tag{30}
\]

The shellwise correction begins with total `H`-mass `p^{-1/2+o(1)}`. The same partial-cutoff bookkeeping as in `RE-187` therefore keeps its relative Chebyshev discrepancy at `p^{-1/2+o(1)}` up to polylogarithmic factors. To lie below **every fixed** KV relative envelope in this construction, it is sufficient that

\[
V(e^{S_p})=o(L_p).
\tag{31}
\]

Condition (2) gives exactly this. Indeed `S_p\ge L_p`, and

\[
S_p=o\!\left(L_p^{5/3}(\log L_p)^{1/3}\right),
\]

so

\[
V(e^{S_p})
=
\frac{S_p^{3/5}}{(\log S_p)^{1/5}}
\le
\frac{S_p^{3/5}}{(\log L_p)^{1/5}}
=o(L_p).
\tag{32}
\]

Thus the `4/3` depth exponent of `RE-187` was the consequence of the quadratic window tariff, not a source-fidelity threshold. Once the exact Chebyshev growth cuts the window to `W\asymp K`, the same fixed-KV bookkeeping permits the larger `5/3` depth scale in (2).

This is still a **sufficient** range for this matched-control construction, not a universal rigidity boundary. More intricate sign ordering inside a remote reservoir, a nonuniform polynomial frame, or a genuinely non-scalar representation could have different spatial costs.

## 7. Representation and adversarial audit

The generic approximation-theory input is elementary: outside `[-1,1]`, Chebyshev polynomials grow like `\exp(m\operatorname{arcosh}x)`. The new point is to retain that logarithmic dependence on the exterior coordinate instead of replacing it by a square-root upper bound before coupling it to the exact Euler prime-power modes.

Three possible failure modes are load-bearing.

First, the denominator `H(q)` could in principle alter the prime-power estimate. Identity (15) includes that normalization exactly, and its subtraction contributes only the geometric `|P(\alpha)|\le1` tail.

Second, reducing `W` might cause shell collisions or bad interpolation conditioning. Equation (23) leaves spacing `\asymp1/K`, enormously larger than the microstep and shell scales, while the DCT inverse is unchanged and derivative sensitivity grows only polynomially.

Third, the broader depth range might destroy KV fidelity at the right edge. This is now the actual tariff: (32), rather than prime-power conditioning, is what restricts the stated range. The finding does not claim that `5/3` is a universal barrier; it identifies the first remaining obstruction for this exact linear-width construction.

The lower bound (21) also has a deliberately narrow scope. It proves that the linear width is not an artifact **within the full-window Gauss--Chebyshev frame**, because the positive `n=2` prime-power mode already forces it at the rightmost node. It does not exclude an adaptive basis or a repair architecture that avoids that node geometry altogether.

## 8. Prior-art audit

The identity `T_m(x)=\cosh(m\operatorname{arcosh}x)` for `x\ge1` and its logarithmic exterior growth are classical Chebyshev theory, not claimed as new. The external search also found the expected flexibility literature for Beurling/generalized prime systems, including Broucke--Kouroupis--Perfekt on perturbations of Beurling integer systems. Those results do not provide an ordinary-prime `{0,1,2}` control matching a growing exact Euler jet while preserving a transient Robin excursion.

No new external theorem is load-bearing here. Prime supply still uses only the Korobov--Vinogradov PNT already anchored in `research/robin_extremal/SOURCES.md`; the strengthening is the elementary estimate (9)--(16) inside the exact resummation of `RE-187`. `SOURCES.md` therefore requires no change.

## Conclusion

The spatial cost identified by `RE-187` can be reduced from

\[
W\asymp\frac{K^2}{\log p}
\]

to

\[
\boxed{W\asymp K}
\]

without changing the ordinary-prime support, `{0,1,2}` multiplicities, exact jet matching, microstepped shell packing, fixed-KV fidelity, or transient Robin ambiguity. This extends exact scalar matched non-rigidity through

\[
\boxed{
K=o\!\left((\log p)^{5/3}(\log\log p)^{1/3}\right).
}
\]

Moreover `W=\Omega(K)` is necessary for the same full-window Gauss--Chebyshev representation once `K\gg\log p`. The live question is therefore no longer whether the quadratic tariff of `RE-187` is intrinsic. It is not. The remaining scalar frontier is whether one can evade the **linear** spatial tariff by changing representation, or whether a selector-sensitive nonlocal invariant is needed before scalar repair finally becomes rigid.