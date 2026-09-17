# RE-184 — Growing Euler-jet depth below the KV shell scale remains non-rigid

**Status:** `EXACT-DERIVED + CONSTRUCTIVE-CONTROL + ORDINARY-PRIME-SUPPORT + MULTIPLICITY-012 + GROWING-EULER-JET-MATCHING + KV-FIDELITY + TRANSIENT-ROBIN-AMBIGUITY + RE-178-GAP-PARTIAL + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-173, RE-178, RE-180, RE-182.

`RE-182` proves that every *fixed* Euler-jet depth can be matched exactly by an ordinary-prime-supported `{0,1,2}` control while preserving the `RE-173` transient Robin excursion and every fixed Korobov--Vinogradov source envelope. Its proof deliberately leaves all interpolation constants dependent on the fixed depth. `RE-178`, from the opposite capacity direction, identifies the much larger scale

\[
K_{\rm cap}(p)\asymp \frac{\log p}{\log\log p}
\]

as the first order at which raw higher-jet leverage can change a polynomial KV-capacity exponent.

The fixed-depth hypothesis in `RE-182` is not essential. A genuinely unbounded number of exact boundary derivatives can still be hidden.

Put

\[
V(x):=\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}}.
\tag{1}
\]

Let `K=K(p)` be any integer-valued function with

\[
\boxed{
K(p)\log(K(p)+2)=o(V(p)).
}
\tag{2}
\]

For every sufficiently large selector scale `p`, there exists an ordinary-prime-supported source `Q_{p,K}` with

\[
\boxed{m_{Q_{p,K}}(q)\in\{0,1,2\}}
\tag{3}
\]

such that, writing

\[
D_Q(s):=\sum_q(m_Q(q)-1)[-\log(1-q^{-s})],
\tag{4}
\]

we have:

1. `Q_{p,K}` agrees with the ordinary prime source below `2p`;
2. it contains the canonical `RE-173` deletion packet `D_p\subset[2p,3p]` and has no repair below `16p`;
3. every boundary jet through the **growing** depth `K(p)` matches exactly,
   \[
   \boxed{
   D_{Q_{p,K}}^{(j)}(1+)=0,
   \qquad 0\le j\le K(p);
   }
   \tag{5}
   \]
4. all series in (5) are absolutely convergent, so the equalities follow by legitimate termwise differentiation;
5. uniformly for `x\ge2p`,
   \[
   \boxed{
   |\vartheta_{Q_{p,K}}(x)-\vartheta(x)|
   \ll
   e^{C K\log(K+2)}
   \left(\sqrt p+(1+\log x)^2\right)
   }
   \tag{6}
   \]
   for an absolute constant `C`; consequently, for every fixed `b>0`,
   \[
   \boxed{
   |\vartheta_{Q_{p,K}}(x)-\vartheta(x)|
   \ll_b x e^{-bV(x)}
   \qquad(x\ge2p)
   }
   \tag{7}
   \]
   once `p` is sufficiently large along the family (2);
6. before any repair is visible, the `RE-173` normalized Robin coordinate still moves by order one,
   \[
   \boxed{
   \mathcal A_{p,8p}(Q_{p,K})-
   \mathcal A_{p,8p}(P)\asymp1.
   }
   \tag{8}
   \]

In particular one may take, for example,

\[
K(p)=\lfloor(\log p)^{1/2}\rfloor.
\tag{9}
\]

Thus **unbounded scalar dimension by itself does not restore source rigidity**. Exact matching can survive for a growing number of Euler derivatives, well beyond every fixed finite family, while retaining ordinary prime labels, bounded nonnegative integer multiplicity, KV fidelity, and an order-one transient Robin ambiguity.

The condition (2) is not claimed sharp. It is the range in which the centered Vandermonde interpolation from `RE-182` can be made quantitative using prime shells whose relative width is still supplied by the same unconditional KV prime-number-theorem input. It remains far below the capacity crossover of `RE-178`.

## 1. Uniform Euler-kernel control up to the growing depth

Retain the exact kernels of `RE-182`:

\[
H(q):=\log\frac q{q-1},
\qquad
U_j(q):=(\log q)^j\sum_{n\ge1}n^{j-1}q^{-n}
\quad(j\ge1),
\tag{10}
\]

with `U_0(q)=H(q)`. The sign convention is chosen so that `U_j=(-1)^jD_q^{(j)}(1+)` for one Euler factor.

The elementary inequality `n\le2^{n-1}` gives, whenever `2^{j-1}<q`,

\[
\sum_{n\ge2}n^{j-1}q^{-n}
\le
\frac{2^{j-1}q^{-2}}{1-2^{j-1}/q}.
\tag{11}
\]

Hence uniformly for `0\le j\le K`, throughout all repair shells below,

\[
\boxed{
\frac{U_j(q)}{H(q)}
=(\log q)^j
\left(1+O\left(\frac{2^K}{q}\right)\right).
}
\tag{12}
\]

Condition (2) implies `K=o(V(p))=o(\log p)`, so `2^K=p^{o(1)}` and the error in (12) is negligible already at the first repair scale.

At a baseline `x=e^L`, define the centered kernels

\[
C_{m,L}(q)
:=
\sum_{j=0}^{m}\binom mj(-L)^{m-j}U_j(q),
\qquad 0\le m\le K.
\tag{13}
\]

By (12) and the binomial theorem, for `q` between `x` and `2^Kx(1+o(1))`,

\[
\boxed{
\frac{C_{m,L}(q)}{H(q)}
=(\log q-L)^m
+O\left(
\frac{2^K(2L+K+1)^m}{x}
\right).
}
\tag{14}
\]

For `m\le K`, the error in (14) is

\[
\exp\{-\log x+O(K\log\log x+K)\}.
\tag{15}
\]

At `x\ge16p` this tends to zero uniformly under (2), and for fixed `p,K` it decreases again at sufficiently large later baselines. Exact matching of all centered coordinates `m\le K` is equivalent, by the triangular change of basis (13), to exact matching of the raw jets `j\le K`.

## 2. The growing Vandermonde inverse costs only exponentially in `K`

Use the same geometric shell nodes as `RE-182`,

\[
c_r:=2^r,
\qquad
\alpha_r:=r\log2,
\qquad 0\le r\le K.
\tag{16}
\]

The limiting centered response matrix is

\[
V_K(m,r)=\alpha_r^m.
\tag{17}
\]

For fixed `K` its invertibility was enough in `RE-182`; here we need its dependence on `K`. This is elementary. The Lagrange polynomial attached to node `r` is

\[
\ell_r(t)
=
\prod_{\substack{0\le s\le K\\s\ne r}}
\frac{t-s\log2}{(r-s)\log2}.
\tag{18}
\]

The `\ell^1` norm of its coefficient vector is at most

\[
\frac{
\prod_{s\ne r}(1+s\log2)
}{
(\log2)^K r!(K-r)!
}
\le C_0^K\binom Kr
\le(2C_0)^K
\tag{19}
\]

for an absolute `C_0`. Consequently

\[
\boxed{
\|V_K^{-1}\|_{\infty\to1}\le e^{C_1K}.
}
\tag{20}
\]

No factorial loss is hidden in the inverse after the nodes are kept at the natural spacing `r\log2`. The larger cost in the growing-depth construction comes from resolving degree-`K` responses across nonzero-width prime shells and from translating the centered basis between successive repair scales.

## 3. KV-wide thin shells still contain far more prime mass than the repair needs

Fix once and for all a constant `a_0>0` for which the line's anchored unconditional PNT gives

\[
\vartheta(y)=y+O\bigl(y e^{-a_0V(y)}\bigr).
\tag{21}
\]

At baseline `x`, take relative shell width

\[
\delta_x:=e^{-a_0V(x)/4}
\tag{22}
\]

and shells

\[
I_{x,r}:=
[c_rx,c_rx(1+\delta_x)],
\qquad 0\le r\le K.
\tag{23}
\]

Because `K=o(V(x))=o(\log x)`, we have uniformly for `0\le r\le K`

\[
V(c_rx)=V(x)(1+o(1)).
\tag{24}
\]

Subtracting (21) at the two endpoints of (23) therefore gives

\[
\vartheta(c_rx(1+\delta_x))-
\vartheta(c_rx)
\sim c_rx\delta_x.
\tag{25}
\]

Since `H(q)\asymp1/q` on a shell,

\[
\boxed{
\sum_{q\in I_{x,r}}H(q)
\asymp\frac{\delta_x}{\log x}.
}
\tag{26}
\]

This is the only place where the KV scale enters the growing-dimensional construction. Across one shell, the main polynomial response in (14) changes by at most

\[
\delta_x e^{C_2K\log(K+2)}.
\tag{27}
\]

Under (2), (27) is `e^{-(a_0/4+o(1))V(x)}`. The Euler-factor remainder in (14), after multiplication by the inverse bound (20), is smaller still. Thus the exact shell response matrix is a perturbation of `V_K` whose inverse satisfies

\[
\boxed{
\|A_x^{-1}\|_{\infty\to1}
\le e^{C_3K}
}
\tag{28}
\]

for every sufficiently large first baseline and all later baselines.

The shell capacity is ample. The initial debt has size `d_p\asymp(\sqrt p\log p)^{-1}`. Even after the `e^{O(K)}` interpolation overhead, its required signed `H`-mass is

\[
e^{O(K)}d_p
=p^{-1/2+o(1)},
\tag{29}
\]

whereas (26) is only subpolynomially small. Hence each shell contains overwhelmingly more unused ordinary-prime mass than is required.

## 4. Quantization contracts after recentering even though `K` grows

Take the first baseline

\[
x_0:=16p,
\qquad L_0:=\log x_0.
\tag{30}
\]

For the canonical `RE-173` deletion packet `D_p\subset[2p,3p]`, put

\[
\rho_m^{(0)}:=
\sum_{q\in D_p}C_{m,L_0}(q).
\tag{31}
\]

Here `\log(q/x_0)` remains in one fixed compact interval, so (14) gives

\[
\boxed{
M_0:=\|\rho^{(0)}\|_\infty
\le e^{C_4K}d_p.
}
\tag{32}
\]

Solve the real shell system `A_{x_0}w=\rho^{(0)}`. By (28), its total signed mass is `e^{O(K)}M_0`. In each shell choose distinct ordinary primes of sign `sgn(w_r)` until their total `H`-mass is the largest one not exceeding `|w_r|`. A positive coefficient duplicates one ordinary copy and a negative coefficient deletes it, so multiplicities remain in `{0,1,2}`.

The shell variation (27), the Euler-factor error (14), and one-prime rounding in each shell imply that after one quantization step the centered residual at the same baseline satisfies

\[
M'_x
\le
\eta_x M_x+
\frac{e^{C_5K\log(K+2)}}{x},
\tag{33}
\]

where

\[
\eta_x
\le
\exp\{-cV(x)+C_6K\log(K+2)\}
\tag{34}
\]

for some absolute `c>0`.

Now take

\[
R:=2^{K+3},
\qquad
x_n:=R^nx_0.
\tag{35}
\]

This makes all generation shells disjoint. Recentring from `L_n` to `L_{n+1}=L_n+\log R` is exact:

\[
C_{m,L_{n+1}}
=
\sum_{j=0}^{m}
\binom mj(-\log R)^{m-j}C_{j,L_n}.
\tag{36}
\]

Its `\ell^\infty` operator norm is at most

\[
(1+\log R)^K
\le e^{C_7K\log(K+2)}.
\tag{37}
\]

Combining (33)--(37) with (2), and increasing the starting threshold if necessary, gives the recurrence

\[
\boxed{
M_{n+1}
\le R^{-3}M_n+
\frac{B_K}{x_n},
\qquad
B_K:=e^{C_8K\log(K+2)}.
}
\tag{38}
\]

Hence

\[
\boxed{
M_n
\ll
R^{-3n}M_0+
\frac{B_K}{x_{n-1}}
}
\qquad(n\ge1).
\tag{39}
\]

The construction therefore drives every one of the `K+1` centered residuals to zero exactly. Because the generations are geometrically separated and the residuals satisfy (39), for every `j\le K`

\[
\sum_q|m_Q(q)-1|\,|D_q^{(j)}(1+)|<\infty.
\tag{40}
\]

Indeed the `j`-th kernel is at most a constant multiple of `(\log q)^jH(q)` here, and the geometric factors `R^{-n}` and `R^{-3n}` dominate the polynomial-in-`n` growth of `(\log x_n)^K`. The raw residuals also tend to zero because conversion back from the centered basis costs at most `(1+L_n)^K`, again dominated by the geometric decay in (39). This proves the exact identities (5).

The infinite continuation is essential, just as in `RE-182`: `RE-172` forbids any nontrivial *finite* ordinary-prime perturbation from matching even the zeroth Mertens coordinate exactly.

## 5. The Chebyshev cost remains KV-small uniformly along the family

At generation `n`, every selected prime is at most `2^Kx_n(1+\delta_{x_n})`. The total selected `H`-mass is at most `e^{O(K)}M_n` plus the one-prime rounding scale. Since `H(q)\asymp1/q`, the total absolute Chebyshev mass of that generation is bounded by

\[
e^{C_9K}x_n\log x_n
\left(
M_n+
\frac{B_K}{x_n}
\right).
\tag{41}
\]

Insert (39). The part propagated from the original selector debt sums to

\[
\ll
\sqrt p\,e^{C_{10}K},
\tag{42}
\]

while completed rounding generations below height `x` contribute at most

\[
e^{C_{11}K\log(K+2)}(1+\log x)^2.
\tag{43}
\]

Together with the original deletion packet this proves (6).

Condition (2) gives

\[
e^{C K\log(K+2)}=e^{o(V(p))}=p^{o(1)}.
\tag{44}
\]

For every fixed `b>0`, at the first relevant height `x\asymp p` the right side of (7) is `p^{1-o(1)}`, whereas (6) is `p^{1/2+o(1)}` plus polylogarithmic terms with a sub-KV coefficient. Since `x e^{-bV(x)}` is eventually increasing and dominates every fixed polylogarithm, the same comparison holds uniformly for all `x\ge2p`. Thus (7) follows.

No repair prime lies below `16p`. The Robin observation height in `RE-173` is `8p`, so none of the growing-dimensional interpolation can alter the already-created prefix excursion. Equation (8) follows unchanged.

## 6. What changes relative to RE-182 and RE-178

`RE-182` established non-rigidity for every fixed finite jet family but left open the logical possibility that *any* dimension tending to infinity with the selector might restore rigidity. The present result rules that out. The matched-control family can absorb at least every depth satisfying (2), including the concrete polynomial-logarithmic depth `(\log p)^{1/2}`.

This still leaves a substantial quantitative gap. `RE-178` places the scalar-capacity crossover at

\[
K_{\rm cap}(p)\asymp\frac{\log p}{\log\log p},
\tag{45}
\]

whereas the present sufficient construction reaches only roughly

\[
K\ll \frac{V(p)}{\log V(p)}
\]

up to little-`o` slack. The obstruction in this proof is **not** Euler-jet capacity itself. It is the need to keep a degree-`K` interpolation stable across ordinary-prime shells that are wide enough for unconditional PNT/KV supply. Closing the gap therefore requires better joint conditioning/quantization, not another fixed-dimensional scalar argument.

The result also does not settle the growing-temperature-panel problem left by `RE-183`. Boundary derivatives at one point and samples at separated temperatures have different conditioning as their dimension grows.

## 7. Representation audit, prior art, and failure modes

The generic mathematics here is classical: centered moments, Lagrange/Vandermonde interpolation, and quantization of real masses by a dense discrete supply. No novelty is claimed for those components. The bound (20) is derived directly from the Lagrange formula rather than imported as a new theorem.

A targeted prior-art search for prescribed Euler-product derivatives/values, prime-supported moment interpolation, and Vandermonde Euler-product constructions found generic Euler-product and interpolation material but no result supplying the combined statement used here: ordinary prime labels, coefficients restricted to `{-1,0,1}`, a number of exactly matched boundary derivatives growing with the selector, absolute convergence at the boundary, fixed-KV Chebyshev fidelity, and a preserved transient Robin displacement. The only load-bearing external arithmetic input is the same unconditional KV/PNT estimate already anchored in `SOURCES.md`; no source-registry update is required.

Several stronger statements do not follow.

First, (2) is a sufficient range, not a sharp threshold. Failure of this shell construction above it would not imply rigidity.

Second, the first repair generation now carries factors `e^{O(K)}` or `e^{O(K\log K)}` in the available upper bounds. `RE-180` still gives its selector-scale **lower** deletion tariff, but this finding does not claim that the exact `Theta(\sqrt p/\log p)` upper tariff from fixed `K` remains uniform as `K\to\infty`.

Third, exact jet matching is strengthened matched-control data, not an invariant already implied by the physical Robin problem. The finding is a sufficiency obstruction: even this growing scalar information set does not identify the transient source behavior in the stated range.

Fourth, this is not a Robin counterexample and gives no RH consequence. It narrows the information-theoretic source frontier by showing that the phrase "dimension growing with the selector" is still too weak unless a quantitative growth rate or a genuinely non-scalar joint invariant is specified.

## Conclusion

The finite-dimensional escape of `RE-182` persists into a genuinely growing regime. Whenever

\[
K(p)\log(K(p)+2)=o(V(p)),
\]

one can match **all** Euler boundary derivatives through order `K(p)` exactly with an ordinary-prime `{0,1,2}` source, remain inside every fixed KV envelope, and keep the selector-scale transient Robin excursion.

The live rigidity boundary is therefore quantitative. A source invariant whose dimension merely tends to infinity is not enough; it must grow fast enough, be conditioned strongly enough, or encode joint arithmetic placement information that the prime-shell interpolation cannot reproduce.

**Provenance:** derived against default-branch snapshot `8dcb16ed6bdc7044f1a8947773270bea56579e48`; stable finding prefix `RE`; no adversarial sidecar was open; local clues were inspected; `SOURCES.md`, clue states, `README.md`, `graph/**`, and `mind/**` were not modified.