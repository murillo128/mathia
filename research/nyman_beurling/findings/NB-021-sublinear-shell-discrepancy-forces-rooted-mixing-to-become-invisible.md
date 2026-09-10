# NB-021 — sublinear shell discrepancy forces rooted mixing to become invisible

**Status:** `EXACT-DERIVED + SOURCE-NORMAL-EQUATION + INTRINSIC-DISCREPANCY-BARRIER + ROOTED-MIXING-INVISIBILITY + NEGATIVE/METHOD-BOUNDARY`. `NB-019` replaces the exponential lcm mixing scale of `NB-018` by the intrinsic consecutive-shell discrepancy of the canonical residual, while `NB-017` identifies the visible enrichment channel with multiplicative edge variation of the future target pairings. These two structures do not automatically reinforce one another. On every dilation that remains rooted deeply enough to see the old normal equations, sufficiently good shell mixing forces the limiting scalar itself to be small.

Let

\[
V_N=\operatorname{span}\{g_2,\ldots,g_N\},\qquad
r_N=e-P_Ne,\qquad d_N=\|r_N\|,
\]

and write `mu_N` for the arithmetic mean of the periodic harmonic-shell sequence of `r_N`. Let

\[
\Delta_N:=\Delta(r_N)
=\sup_{A\le B}\left|
\sum_{n=A}^{B}(r_{N,n}-\mu_N)
\right|
\]

be the intrinsic consecutive discrepancy introduced in `NB-019`, and put

\[
Q_m:=\sqrt m\,A_m^*,\qquad
D_m:=A_m^*-m^{-1/2}I.
\]

Then for every integer `m>=2` with `2m<=N`,

\[
\boxed{
|\mu_N|\le \frac{2\Delta_N}{m}.
}
\tag{1}
\]

In particular, with `L_N=floor(N/2)`,

\[
\boxed{
|\mu_N|
\le \frac{2\Delta_N}{L_N}
\le \frac{4\Delta_N}{N-1}.
}
\tag{2}
\]

Thus a nonvanishing deep-mixing scalar requires **linear intrinsic shell discrepancy**. Any sequence with

\[
\Delta_N=o(N)
\tag{3}
\]

necessarily has `mu_N -> 0`.

There is a stronger visibility consequence. Assume (3) along an unbounded sequence of section sizes and define

\[
K_N:=1+\left\lceil\sqrt{N(1+\Delta_N)}\right\rceil,
\qquad
L_N:=\left\lfloor\frac N2\right\rfloor.
\tag{4}
\]

Then `K_N<=L_N` eventually and the entire intermediate rooted band mixes to **zero**, uniformly:

\[
\boxed{
\sup_{K_N\le m\le L_N}\|Q_mr_N\|_2\longrightarrow0.
}
\tag{5}
\]

Consequently its contribution to the visible section-enrichment defect satisfies

\[
\boxed{
\sum_{m=K_N}^{L_N}
\|P_ND_mr_N\|^2
\longrightarrow0.
}
\tag{6}
\]

By contrast, if the limiting Nyman distance were positive,

\[
d_\infty:=\lim_{N\to\infty}d_N>0,
\tag{7}
\]

then on the same band

\[
\boxed{
\sum_{m=K_N}^{L_N}\|D_mr_N\|^2
=
\bigl(d_N^2+o(1)\bigr)
\sum_{m=K_N}^{L_N}\frac1m
\longrightarrow\infty,
}
\tag{8}
\]

and therefore the visible/full defect ratio restricted to this band tends to zero. More explicitly,

\[
\sum_{m=K_N}^{L_N}\frac1m
=
\frac12\log\frac{N}{1+\Delta_N}+O(1),
\tag{9}
\]

so under (7) the full defect in the band is asymptotic to

\[
\frac{d_\infty^2}{2}
\log\frac{N}{1+\Delta_N}.
\tag{10}
\]

This is a source-specific obstruction to the most direct use of the preperiod mixing mechanism. If the canonical residual has sublinear intrinsic discrepancy, then once the dilations are large enough to average that discrepancy but still small enough that the `g_2` normal equation anchors both ends of the multiplicative edge, the averaged residual cannot converge to a useful nonzero target component: it converges to zero. Under a hypothetical nonzero limiting distance, the semigroup defect is then large but asymptotically invisible to the old section throughout a logarithmically long harmonic band.

The result does **not** show that `Delta_N=o(N)` for the actual Nyman residual, nor does it upper-bound the complete visibility statistic `J_(N,M)`: channels before `K_N` and genuinely unrooted channels beyond `N/2` remain available. It instead sharpens the live `NB-015`/`NB-017` problem. A successful source-specific visibility estimate cannot simply combine “small discrepancy implies early mixing” with the fixed-section nonzero-`mu_N` picture of `NB-018`; in the rooted linear-depth corridor those two advantages are quantitatively incompatible.

## 1. Old normal equations anchor the deep-mixing scalar

`NB-017` gives the exact future-pairing field

\[
q_k=\langle r_N,g_k\rangle,
\qquad
s_k=kq_k,
\]

and the dilation-pairing identity

\[
\boxed{
\langle Q_mr_N,g_j\rangle
=\frac{s_{mj}-s_m}{j}.
}
\tag{11}
\]

The projection normal equations give `s_k=0` for every `k<=N`. Hence, whenever `2m<=N`, equation (11) with `j=2` gives

\[
\boxed{
\langle Q_mr_N,g_2\rangle=0.
}
\tag{12}
\]

On the other hand `NB-019` proves the basis-invariant discrepancy estimate

\[
\boxed{
\|Q_mr_N-\mu_Ne\|_\infty
\le\frac{2\Delta_N}{m}.
}
\tag{13}
\]

In Bagchi's real-space model `g_2` is nonnegative: on the harmonic shell `I_n` it equals `{n/2}`, hence it is `1/2` for odd `n` and zero for even `n`. Moreover

\[
\langle e,g_2\rangle=\|g_2\|_1=\frac{\log2}{2}>0,
\tag{14}
\]

as used already in the parity normal equation of `NB-009`. Pair (12) with the constant part in (13):

\[
\begin{aligned}
|\mu_N|\,\langle e,g_2\rangle
&=
|\langle \mu_Ne-Q_mr_N,g_2\rangle|\\
&\le
\|Q_mr_N-\mu_Ne\|_\infty\|g_2\|_1\\
&\le
\frac{2\Delta_N}{m}\langle e,g_2\rangle.
\end{aligned}
\]

Cancel the positive factor in (14) to obtain (1). Taking `m=L_N` proves (2).

This argument is deliberately intrinsic. It does not use a coefficient norm, a Gram condition number, the lcm period, a zero estimate, or a closure assumption. The only two inputs are the actual source normal equation and the discrepancy mixing estimate for the actual residual.

## 2. Sublinear discrepancy creates a long band that mixes to zero

Assume (3). From (4),

\[
\frac{K_N}{N}\longrightarrow0,
\]

so `K_N<=L_N` eventually. For every `K_N<=m<=L_N`, combine (13) with (2):

\[
\begin{aligned}
\|Q_mr_N\|_2
&\le |\mu_N|+
\|Q_mr_N-\mu_Ne\|_2\\
&\le
\frac{4\Delta_N}{N-1}
+
\frac{2\Delta_N}{m}\\
&\le
\frac{4\Delta_N}{N-1}
+
\frac{2\Delta_N}{K_N}.
\end{aligned}
\tag{15}
\]

The first term tends to zero. For the second,

\[
\frac{\Delta_N}{K_N}
\le
\frac{\Delta_N}{\sqrt{N(1+\Delta_N)}}
\le
\sqrt{\frac{\Delta_N}{N}},
\tag{16}
\]

which also tends to zero. This proves the uniform convergence (5).

The choice (4) is only a convenient balancing scale. More generally, any band with

\[
\Delta_N=o(K_N),
\qquad
K_N=o(N),
\qquad
K_N\le m\le N/2
\]

has the same zero-mixing conclusion. Equation (4) shows that such a band exists automatically under the sole hypothesis `Delta_N=o(N)`.

## 3. The mixed band loses visible energy even when full defect grows

Because `P_Nr_N=0`,

\[
\sqrt m\,P_ND_mr_N=P_NQ_mr_N.
\tag{17}
\]

Projection is contractive, so (15) already implies pointwise smallness. A direct summation gives a stronger total statement. From (2), (13), and `(a+b)^2<=2a^2+2b^2`,

\[
\|Q_mr_N\|_2^2
\le
\frac{32\Delta_N^2}{(N-1)^2}
+
\frac{8\Delta_N^2}{m^2}.
\tag{18}
\]

Hence

\[
\boxed{
\sum_{m=K_N}^{L_N}\|P_ND_mr_N\|^2
\le
\frac{32\Delta_N^2}{(N-1)^2}
\sum_{m=K_N}^{L_N}\frac1m
+
\frac{4\Delta_N^2}{(K_N-1)^2}.
}
\tag{19}
\]

For the second term,

\[
\frac{\Delta_N^2}{(K_N-1)^2}
\le
\frac{\Delta_N^2}{N(1+\Delta_N)}
\le
\frac{\Delta_N}{N}
\longrightarrow0.
\tag{20}
\]

For the first, since `K_N-1>=sqrt(N(1+Delta_N))`,

\[
\sum_{m=K_N}^{L_N}\frac1m
\le
\log\frac{L_N}{K_N-1}
\le
\frac12\log\frac{N}{1+\Delta_N}+O(1).
\tag{21}
\]

Writing `x_N=(1+Delta_N)/N -> 0`, the first term in (19) is `O(x_N^2 log(1/x_N))`, hence tends to zero. This proves (6).

For the full defect, the exact identity is

\[
\sqrt m\,D_mr_N=Q_mr_N-r_N.
\tag{22}
\]

Equation (5) gives uniformly on the band

\[
\left|
\|Q_mr_N-r_N\|-d_N
\right|
\le\|Q_mr_N\|=o(1).
\tag{23}
\]

Since `0<=d_N<=1`, squaring (23) is uniform as well, and therefore

\[
\sum_{m=K_N}^{L_N}\|D_mr_N\|^2
=
(d_N^2+o(1))
\sum_{m=K_N}^{L_N}\frac1m,
\]

which is (8). Finally, (4) and elementary harmonic-sum asymptotics give (9). Under `d_infinity>0`, both factors in (8) stay positive and the harmonic width diverges, proving (10) and the vanishing restricted visible/full ratio.

The asymmetry is important: the same mixing that makes `Q_mr_N` simple makes it **orthogonal to useful old-section visibility**, because the rooted normal equation forces its only possible scalar limit to zero.

## 4. Consequence for coefficient-controlled mixing

`NB-019` also gives the finite canonical majorant

\[
\Delta_N\le\frac{\mathfrak A_N}{8},
\qquad
\mathfrak A_N=\sum_{j=2}^N j|a_{N,j}|.
\tag{24}
\]

Combining (2) and (24) yields the exact coefficient-side constraint

\[
\boxed{
\mathfrak A_N\ge 2(N-1)|\mu_N|.
}
\tag{25}
\]

Thus `mathfrak A_N=o(N)` implies `mu_N->0` and, via (24), places the residual in the zero-mixing regime above. This is complementary to `NB-020`, which proves a lower floor `mathfrak A_N \gg min(N^2,d_N^{-2})` from early-shell Möbius locking. `NB-020` says the coefficient budget cannot be anomalously tiny once the target is approximated well; (25) says that if the budget is nevertheless sublinear in `N`, then it cannot sustain a nonzero deep-mixing scalar.

The coefficient corollary is weaker than the intrinsic formulation: a large absolute coefficient budget may coexist with small `Delta_N` through cancellation. The live quantity is therefore still the actual shell discrepancy or, beyond this rooted band, the actual edge variation of `s_k`, not an arbitrary basis-conditioned `l1` norm.

## 5. Prior-art boundary and falsification controls

The semigroup/dilation framework and the discrete Nyman family are classical in Báez-Duarte and Bagchi, already anchored in `SOURCES.md`. Generalized Nyman-Beurling work also contains independent coefficient-control conditions, so coefficient size by itself is not claimed as a new theme. A targeted search of the nearby semigroup, periodic-dilation, coefficient-control, and optimal-coefficient literature did not locate the specific implication (1)--(2) or the rooted-band separation (6)--(10). Search absence is not a novelty proof; the status here is `EXACT-DERIVED`, and the mathematical delta is the explicit incompatibility between the `NB-019` discrepancy-mixing mechanism and old-section visibility while the multiplicative edges remain source-anchored.

The load-bearing controls are exact. Equation (1) requires `2m<=N`; once `m>N/2`, the endpoint `2m` is no longer killed by the old normal equations and the argument does not apply. Equation (6) concerns only the intermediate band in (4), not all channels entering `J_(N,M)`. The divergence in (8) additionally assumes `d_infinity>0`; without that hypothetical obstruction, the full defect may shrink with the residual. Most importantly, `Delta_N=o(N)` is a conditional regime, not a proved property of canonical Nyman residuals.

The finding is falsified by a violation of the exact pairing identity (11), the intrinsic mixing bound (13), the normal equations `s_k=0` for `k<=N`, or any sequence satisfying `Delta_N=o(N)` for which the visible-band bound (19) does not tend to zero. None of these steps invokes RH, density of the Nyman span, or an asymptotic estimate for zeta.

## 6. Research consequence

The accepted scale-coupled visibility problem remains open, but one natural shortcut is now closed. Improving `NB-019` to a sublinear intrinsic discrepancy estimate would not, by itself, turn deep averaging into a positive source-visible fraction on linear rooted depths. It would force the opposite behavior: the long mixed part of that corridor becomes asymptotically invisible while retaining large full semigroup defect under the nonzero-distance alternative.

A positive continuation must therefore obtain its useful graph energy **before** this zero-mixing regime, from channels on the scale `m=O(Delta_N)`, or from genuinely unrooted multiplicative transport after the `2m<=N` anchor disappears. Either route must still pay the residual-relevant compressed frame cost in the `NB-015` telescoping budget. This is a narrowing of the source-specific anchored-energy target, not an improvement of the Nyman distance and not a new RH consequence.