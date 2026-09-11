# NB-039 — weighted-tail dilation copies make the inverse-distance compression threshold sharp

**Status:** `EXACT-DERIVED + DILATION-RENORMALIZATION + RECURSIVE-TARGET-LOSS-FLOOR + SHARP-COMPRESSION-THRESHOLD + SOURCE-DIRECTION-REFINEMENT + NEGATIVE/METHOD-BOUNDARY`. `NB-034` proves that the source-faithful weighted-tail quotient loses at most `1/M` of target energy, and therefore that `M/log N -> infinity` is an unconditional Burnol-scale sufficient condition for multiplicative distance preservation. `NB-038` then shows that the missing upper-section metric already carries `d_N^2` along one explicit Möbius/Vasyunin source direction, with a crude `M^{-1/2}` truncation error. The weighted nuisance sector itself contains a recursively dilated canonical Nyman section. This makes the `1/M` target loss unavoidable up to absolute constants and replaces the crude truncation error by the smaller-section distance.

Use the canonical generators

\[
g_n(x)=\left\{\frac1{nx}\right\}-\frac1n\left\{\frac1x\right\},
\qquad
V_N=\operatorname{span}(g_2,\ldots,g_N),
\qquad
d_N=\operatorname{dist}(e,V_N),
\quad e(x)=1,
\tag{1}
\]

and the weighted tail of `NB-034`,

\[
\widehat h_n:=ng_n-(n+1)g_{n+1},
\qquad
\widehat W_{M,N}:=
\operatorname{span}(\widehat h_M,\ldots,\widehat h_{N-1}),
\tag{2}
\]

\[
\widehat K_{M,N}:=V_N\cap\widehat W_{M,N}^{\perp},
\qquad
\widehat\kappa_{M,N}:=\operatorname{dist}(e,\widehat K_{M,N}).
\tag{3}
\]

For `2<=M<=N`, put

\[
K:=\left\lfloor\frac NM\right\rfloor.
\tag{4}
\]

Let `A_M` be the Bagchi dilation isometry used in `NB-014`, so

\[
A_Mg_j=\sqrt M\left(g_{Mj}-j^{-1}g_M\right).
\tag{5}
\]

Then the weighted tail contains a canonical dilated section:

\[
\boxed{
A_MV_K\subseteq\widehat W_{M,N}.
}
\tag{6}
\]

Write

\[
e_T:=\mathbf 1_{(0,1/M]},
\qquad
e_E:=e-e_T=\mathbf 1_{(1/M,1]}.
\tag{7}
\]

Because `A_Me=\sqrt M\,e_T`, (6) gives the recursive tail-distance bound

\[
\boxed{
\operatorname{dist}(e_T,\widehat W_{M,N})
\le\frac{d_K}{\sqrt M}.
}
\tag{8}
\]

Since every weighted edge vanishes on `(1/M,1]`, one has `e_E\perp\widehat W_{M,N}`. Combining (8) with the exact Pythagorean identity of `NB-034` yields

\[
\boxed{
\frac{1-d_K^2}{M}
\le
\widehat\kappa_{M,N}^2-d_N^2
=
\|P_{\widehat W_{M,N}}e\|^2
\le
\frac1M.
}
\tag{9}
\]

This already shows that the additive `1/M` estimate of `NB-034` is sharp in order. If `N>=2M`, then `K>=2` and monotonicity gives `d_K<=d_2`. In fact

\[
\boxed{d_2^2=1-\log2,}
\tag{10}
\]

so (9) becomes the uniform two-sided estimate

\[
\boxed{
\frac{\log2}{M}
\le
\widehat\kappa_{M,N}^2-d_N^2
\le
\frac1M
\qquad(N\ge2M).
}
\tag{11}
\]

Consequently, along **every** sequence with `N_j>=2M_j`, multiplicative preservation by the weighted skeleton has the exact scale criterion

\[
\boxed{
\frac{\widehat\kappa_{M_j,N_j}}{d_{N_j}}\longrightarrow1
\quad\Longleftrightarrow\quad
M_jd_{N_j}^2\longrightarrow\infty.
}
\tag{12}
\]

Thus the relevant compression scale is not merely bounded above by the Burnol choice: it is intrinsically `M >> d_N^{-2}` for this weighted quotient. Burnol's unconditional lower bound still makes `M/log N -> infinity` a universal sufficient condition. Under the standard conditional optimal asymptotic `d_N^2 \asymp 1/log N` already anchored through Bettin--Conrey--Farmer, the same superlogarithmic condition is also order-necessary for multiplicative preservation of this particular quotient.

The recursive inclusion also sharpens `NB-038`. With its notation

\[
R_N:=I-P_{V_N},
\qquad
S_{M,N}=F^*R_NF,
\qquad
a=B_M^{1/2}u_M=F^*e,
\qquad
q=B_M^{1/2}\eta_{M,N}=F^*r_N,
\tag{13}
\]

one has

\[
\boxed{
\left|\sqrt{a^*S_{M,N}a}-d_N\right|
\le\frac{d_K}{\sqrt M},
}
\tag{14}
\]

\[
\boxed{
|a^*q-d_N^2|
\le\frac{d_Nd_K}{\sqrt M},
}
\tag{15}
\]

and the exact coupling remainder of `NB-038` improves to

\[
\boxed{
\|q-S_{M,N}a\|_2
\le
\frac{d_K}{\sqrt M}\sqrt{\|S_{M,N}\|_{\mathrm{op}}}.
}
\tag{16}
\]

Hence the explicit source direction already satisfies

\[
a^*S_{M,N}a=(1+o(1))d_N^2,
\qquad
a^*q=(1+o(1))d_N^2
\tag{17}
\]

under the strictly source-adaptive condition

\[
\boxed{
\frac{M d_N^2}{d_{\lfloor N/M\rfloor}^2}\longrightarrow\infty.
}
\tag{18}
\]

For example, on the non-closure alternative `d_N -> d_infinity>0`, any cutoff with `M->infinity` and `N/M->infinity` satisfies (18), however slowly `M` grows. Thus the superlogarithmic cutoff is a sharp requirement for preserving the **weighted quotient distance** at the conjectural `1/log N` scale, but it is not an intrinsic requirement for seeing the Burnol/source-aligned defect itself.

## 1. Weighted telescoping contains a dilated Nyman section

For every integer `j` with `2<=j<=K`, telescoping the weighted edges gives

\[
\sum_{n=M}^{Mj-1}\widehat h_n
=Mg_M-Mj\,g_{Mj}.
\tag{19}
\]

The classical dilation identity (5) gives

\[
Mj\,g_{Mj}-Mg_M
=j\sqrt M\,A_Mg_j.
\tag{20}
\]

Therefore

\[
\boxed{
A_Mg_j
=-\frac1{j\sqrt M}
\sum_{n=M}^{Mj-1}\widehat h_n
\in\widehat W_{M,N}.
}
\tag{21}
\]

The upper index is legal because `Mj<=MK<=N`. Taking spans proves (6). This is a finite exact relation: no closure, Gram inversion, Möbius cancellation, or zero information is involved.

Let `v_K=P_{V_K}e`. Since `A_M` is an isometry and `A_Me=\sqrt M e_T`, the vector

\[
w:=\frac1{\sqrt M}A_Mv_K
\tag{22}
\]

belongs to `\widehat W_{M,N}` and satisfies

\[
e_T-w
=\frac1{\sqrt M}A_M(e-v_K).
\tag{23}
\]

Taking norms gives

\[
\|e_T-w\|=\frac{d_K}{\sqrt M},
\tag{24}
\]

which proves (8).

## 2. The discarded target mass is necessarily of order `1/M`

`NB-034` proves that every vector in `\widehat W_{M,N}` vanishes on the first `M-1` harmonic shells, whose union is `(1/M,1]` up to endpoints. Hence

\[
e_E\perp\widehat W_{M,N},
\qquad
P_{\widehat W_{M,N}}e=P_{\widehat W_{M,N}}e_T.
\tag{25}
\]

Orthogonal projection inside the tail interval gives

\[
\|P_{\widehat W_{M,N}}e\|^2
=
\|e_T\|^2-
\operatorname{dist}(e_T,\widehat W_{M,N})^2.
\tag{26}
\]

Since `||e_T||^2=1/M`, (8) implies the lower bound in (9); the upper bound follows from contraction. The exact orthogonal splitting `V_N=\widehat W_{M,N}\oplus\widehat K_{M,N}` then gives

\[
\widehat\kappa_{M,N}^2-d_N^2
=\|P_{\widehat W_{M,N}}e\|^2,
\tag{27}
\]

recovering the middle identity in (9).

For the absolute constant in (11), the shell formula from `NB-034` gives

\[
g_2|_{I_t}
=\left\{\frac t2\right\}
=
\begin{cases}
1/2,&t\ \text{odd},\\
0,&t\ \text{even}.
\end{cases}
\tag{28}
\]

Thus

\[
\sum_{t\ge1,\ t\text{ odd}}\frac1{t(t+1)}
=
1-\frac12+\frac13-\frac14+\cdots
=\log2,
\tag{29}
\]

and therefore

\[
\langle e,g_2\rangle=\frac{\log2}{2},
\qquad
\|g_2\|^2=\frac{\log2}{4}.
\tag{30}
\]

The one-dimensional projection onto `V_2=span(g_2)` has squared norm `log2`, proving (10). Since `d_K` is nonincreasing in `K`, `1-d_K^2>=1-d_2^2=log2` for every `K>=2`, and (11) follows.

Dividing (11) by `d_N^2` gives

\[
\frac{\log2}{Md_N^2}
\le
\frac{\widehat\kappa_{M,N}^2}{d_N^2}-1
\le
\frac1{Md_N^2},
\tag{31}
\]

which proves the equivalence (12). In particular, the `M/log N -> infinity` corridor of `NB-034` is not an artifact of its upper estimate if the true distance is of order `1/log N`: within this weighted quotient, the additive target penalty itself prevents relative preservation below the inverse-distance-squared scale.

## 3. The recursive tail control refines the source-aligned defect

Keep the `NB-038` decomposition

\[
e=e_E+e_T,
\qquad
r_N=R_Ne.
\tag{32}
\]

Because `\widehat W_{M,N}\subseteq V_N`, equation (22) gives `R_Nw=0`; hence

\[
R_Ne_T
=R_N(e_T-w)
=\frac1{\sqrt M}R_NA_M(e-P_{V_K}e).
\tag{33}
\]

Orthogonal contraction and (24) give

\[
\boxed{
\|R_Ne_T\|\le\frac{d_K}{\sqrt M}.
}
\tag{34}
\]

`NB-038` identifies

\[
\sqrt{a^*S_{M,N}a}=\|R_Ne_E\|,
\qquad
a^*q=\langle e_E,r_N\rangle.
\tag{35}
\]

The reverse triangle inequality applied to
`r_N=R_Ne_E+R_Ne_T` now proves (14). Also

\[
d_N^2-a^*q
=\langle e_T,r_N\rangle
=\langle R_Ne_T,r_N\rangle,
\tag{36}
\]

so Cauchy--Schwarz and (34) prove (15).

Finally `NB-038` gives the exact vector relation

\[
q-S_{M,N}a=F^*R_Ne_T.
\tag{37}
\]

Since `R_Nw=0`, one may replace `e_T` by `e_T-w` on the right. Moreover

\[
\|F^*R_N\|^2
=\|F^*R_NF\|
=\|S_{M,N}\|_{\mathrm{op}}.
\tag{38}
\]

Equations (24), (37), and (38) prove (16). If (18) holds, then

\[
\frac{d_K}{\sqrt M\,d_N}\longrightarrow0,
\tag{39}
\]

and (14)--(15) imply (17).

If instead `d_N -> d_infinity>0` and `M->infinity`, `N/M->infinity`, then also `d_K->d_infinity`; hence `d_K/d_N->1` and (39) follows automatically. This does not prove the non-closure alternative or RH failure. It says that **if** the limiting residual is nonzero, the source-aligned upper-section defect is already visible at arbitrarily slowly growing weighted-skeleton dimensions.

## 4. Adversarial boundary

The result does not make the defect pair `(Z_{M,N},eta_{M,N})` cheap to compute. Equation (6) embeds a smaller canonical section inside the discarded weighted tail, but evaluating `S_{M,N}=F^*R_NF` still contains the full upper-section projection. The accepted target-data clue therefore remains open.

The distinction between (12) and (18) is essential. Relative preservation of the **quotient target distance** requires `M d_N^2 -> infinity` because the nuisance space itself removes `Theta(1/M)` target mass. Recovering the source-aligned defect of `NB-038` only requires `M d_N^2/d_K^2 -> infinity`, which can be much weaker when the Nyman distances vary slowly across the multiplicative scale `N -> N/M`. Conflating these two requirements would incorrectly turn a target-loss lower bound into an oracle lower bound.

The endpoint `K<2` is also excluded from the absolute floor (11). When `N<2M`, the recursive copy `A_MV_K` is trivial and no positive `log2/M` lower bound follows. The exact recursive inequality (9) remains valid with the natural convention `V_0=V_1={0}`, `d_0=d_1=1`.

No claim is made that `\widehat W_{M,N}` equals `A_MV_K`; it is generally much larger. Accordingly, (8) is an upper bound for the tail approximation error and the first inequality in (9) need not be an equality. The theorem is a one-sided recursive embedding, not a self-similar decomposition of the whole weighted tail.

## 5. Prior-art and research consequence

The dilation identity (5) and integer semigroup structure are classical Nyman--Beurling/Báez--Duarte machinery; Bagchi's 2006 Hilbert-space treatment is already anchored in `SOURCES.md`, and `NB-014` already uses the same identity. The weighted shell-kernel space itself is the local construction of `NB-034`. Burnol and Bettin--Conrey--Farmer enter only in the scale interpretations already anchored for this line.

A targeted literature check covered Bagchi's semigroup formulation, finite-section Nyman distances, Ehm's recent Gram-matrix decompositions, recent multiscale Gram-compressibility work, and current subspace-angle work. The accessible statements did not identify the exact finite containment (6), the recursive loss sandwich (9), or the sharp criterion (12). This is not a priority claim: the substantive line-local delta is the synthesis of the classical dilation law with the specific weighted-tail quotient already persisted in Mathia.

The weighted-skeleton frontier is now sharper in two different senses. First, its target-distance compression threshold is completely calibrated: for `N>=2M`, it preserves relative distance **if and only if** `M` dominates `d_N^{-2}`. Second, the upper-section source defect can become visible at much thinner cutoffs whenever adjacent multiplicative scales have comparable Nyman distances. The remaining route cannot gain by treating the `1/M` target loss as a loose proof artifact. Any improvement must either change the nuisance quotient itself or exploit the arithmetic structure of the defect pair without reconstructing the full finite distance.