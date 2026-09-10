# NB-027 — Möbius locking forces logarithmic coefficient mass transverse to an adjacent matching

**Status:** `EXACT-DERIVED + EXTERNAL-MOBIUS-SIGN-PATTERN-INPUT + TARGET-SELECTED-TRANSVERSE-MASS + ADJACENT-NUISANCE-SEPARATION + METHOD-BOUNDARY`. `NB-024` shows that a good canonical Nyman approximation forces its normalized coefficient vector into a low-Rayleigh regime, while `NB-025`--`NB-026` show that adjacent generator differences create a large source-independent supply of low-Rayleigh, target-poor nuisance directions. The first source-specific separation can be made exact: on the scale where `NB-020` locks the best coefficients to Möbius values, a logarithmically growing amount of coefficient mass is forced into the pair-sum direction orthogonal to one of the two canonical checkerboard adjacent-difference matchings.

Let

\[
V_N=\operatorname{span}(g_2,\ldots,g_N),\qquad
r_N=e-P_{V_N}e,\qquad d_N=\|r_N\|,
\]

and write

\[
P_{V_N}e=\sum_{n=2}^N a_{N,n}g_n,
\qquad
s_n:=\|g_n\|,
\qquad
\alpha_{N,n}:=a_{N,n}s_n.
\tag{1}
\]

Thus `alpha_N` is the coefficient vector in the individually normalized dictionary `phi_n=g_n/s_n` used in `NB-024`--`NB-026`. For `2<=n<N` define the Euclidean-unit adjacent nuisance vector

\[
u_n:=\frac{s_ne_n-s_{n+1}e_{n+1}}
{\sqrt{s_n^2+s_{n+1}^2}},
\tag{2}
\]

and its orthogonal companion

\[
w_n:=\frac{s_{n+1}e_n+s_ne_{n+1}}
{\sqrt{s_n^2+s_{n+1}^2}}.
\tag{3}
\]

For `epsilon in {0,1}` and `Y<=N`, let

\[
U_{N,Y}^{(\epsilon)}
:=\operatorname{span}\{u_n:2\le n<Y,\ n\equiv\epsilon\pmod2\}.
\tag{4}
\]

The supports in each parity class are disjoint, so the vectors in (4) are orthonormal. There are absolute constants `c>0` and `Y_0` such that, for every `N` with `0<d_N<1`, if

\[
Y_N:=\left\lfloor
\min\left\{N,\frac1{32d_N\log(e/d_N)}\right\}
\right\rfloor\ge Y_0,
\tag{5}
\]

then

\[
\boxed{
\max_{\epsilon\in\{0,1\}}
\left\|P_{(U_{N,Y_N}^{(\epsilon)})^\perp}\alpha_N\right\|_2^2
\ge c\log Y_N.
}
\tag{6}
\]

In particular, along any subsequence on which `d_N->0`, the right side tends to infinity. The target-selected coefficient vector therefore cannot explain all of its growing Euclidean mass by alignment with both candidate descriptions of a **single disjoint adjacent-difference matching**. A logarithmically divergent component survives transverse to at least one of the two fixed checkerboard nuisance spaces.

This does not yet prove that the surviving component is itself low-Rayleigh. It is a coefficient-space separation theorem, not a spectral projection theorem and not an improvement of the Nyman distance. Its value is that the universal adjacent cancellation mechanism from `NB-025`--`NB-026` is no longer merely compared to the target-selected vector by scale: the Möbius source forces an explicit transverse component at essentially the same inverse-distance logarithmic scale.

## 1. The locking scale can be made uniform with an elementary divisor bound

`NB-020` proves the exact coefficient stability estimate

\[
|a_{N,k}+\mu(k)|\le2d_N\sigma(k),
\qquad 2\le k\le N.
\tag{7}
\]

No refined maximal-order theorem for `sigma` is needed here. Since

\[
\frac{\sigma(k)}k=\sum_{d\mid k}\frac1d\le H_k\le1+\log k,
\tag{8}
\]

we have `sigma(k)<=k(1+log k)`. Put `L_N=log(e/d_N)`. From (5), every `k<=Y_N` satisfies `k<1/d_N` and hence

\[
1+\log k\le L_N,
\qquad
2d_N\sigma(k)
\le2d_NY_NL_N
\le\frac1{16}.
\tag{9}
\]

Thus throughout the whole declared section,

\[
\boxed{|a_{N,k}+\mu(k)|\le\frac1{16}\qquad(k\le Y_N).}
\tag{10}
\]

The extra `log(e/d_N)` in (5) is only the price of using the elementary uniform bound (8). It is not asserted to be an intrinsic locking threshold. Importantly,

\[
\log Y_N=\log(1/d_N)+O(\log\log(1/d_N))
\]

on the inverse-distance branch, so this loss does not change the logarithmic mass scale established below.

## 2. Same-sign consecutive Möbius values force pair-sum mass

The load-bearing external arithmetic input is the theorem of Matomäki, Radziwiłł and Tao that every possible two-term value pattern of

\[
(\mu(n),\mu(n+1))\in\{-1,0,1\}^2
\]

occurs with positive lower natural density. In particular the set

\[
\mathcal S:=\{n:\mu(n)=\mu(n+1)\in\{-1,1\}\}
\tag{11}
\]

has positive lower natural density. Partial summation therefore gives an absolute constant `c_0>0` and a threshold `Y_0` such that

\[
\boxed{
\sum_{\substack{n<Y\\n\in\mathcal S}}\frac1n
\ge c_0\log Y
\qquad(Y\ge Y_0).
}
\tag{12}
\]

Indeed, positive lower natural density gives `A(t)>=delta t` eventually for the counting function of `S`, and Abel summation gives a `delta log Y+O(1)` lower bound for the harmonic weight.

Now take `n in S` with `n<Y_N`. Equation (10) and equality of the two nonzero Möbius signs give

\[
|a_{N,n}+a_{N,n+1}|
\ge2-\frac18
=\frac{15}{8}.
\tag{13}
\]

On the other hand, the exact normalized-coordinate rotation (2)--(3) gives

\[
\boxed{
\langle\alpha_N,w_n\rangle
=
\frac{s_ns_{n+1}}
{\sqrt{s_n^2+s_{n+1}^2}}
(a_{N,n}+a_{N,n+1}).
}
\tag{14}
\]

This is the source-sensitive point. Alternating Möbius signs would make the adjacent **difference** direction natural; equal signs instead force the canonical coefficient vector into the orthogonal pair-sum direction.

## 3. Canonical generator sizes turn the sign pattern into harmonic transverse energy

`NB-024` already supplies

\[
s_k^2\ge\frac1{4k}.
\tag{15}
\]

A matching upper bound with a harmless constant follows directly from the same harmonic-shell formula. On shells `I_t`, `g_k={t/k}`. For `t<k`,

\[
\sum_{t<k}\frac{|g_k(I_t)|^2}{t(t+1)}
=\frac1{k^2}\sum_{t<k}\frac{t}{t+1}<\frac1k,
\]

while the tail is at most

\[
\sum_{t\ge k}\frac1{t(t+1)}=\frac1k.
\]

Hence

\[
\boxed{\frac1{4k}\le s_k^2\le\frac2k.}
\tag{16}
\]

Combining (13)--(16), for every `n in S`, `n<Y_N`,

\[
\begin{aligned}
|\langle\alpha_N,w_n\rangle|^2
&=
\frac{s_n^2s_{n+1}^2}{s_n^2+s_{n+1}^2}
|a_{N,n}+a_{N,n+1}|^2\\
&\ge \frac{1}{128n}.
\end{aligned}
\tag{17}
\]

The numerical constant is intentionally weakened. From (16), the first factor alone is at least `1/(128n)`, while (13) is larger than one.

Split the favorable indices in (12) by the parity of `n`. One parity `epsilon` carries at least half their harmonic weight. For this parity, the vectors `w_n` on favorable edges have pairwise disjoint supports, hence are orthonormal; moreover each is orthogonal to **all** the nuisance vectors spanning `U_(N,Y_N)^(epsilon)`. Consequently

\[
\begin{aligned}
\left\|P_{(U_{N,Y_N}^{(\epsilon)})^\perp}\alpha_N\right\|_2^2
&\ge
\sum_{\substack{n<Y_N\\n\in\mathcal S\\n\equiv\epsilon\ (2)}}
|\langle\alpha_N,w_n\rangle|^2\\
&\ge
\frac1{128}
\sum_{\substack{n<Y_N\\n\in\mathcal S\\n\equiv\epsilon\ (2)}}\frac1n\\
&\ge c\log Y_N,
\end{aligned}
\tag{18}
\]

which proves (6).

The checkerboard formulation is useful because the two spaces in (4) are fixed by the dictionary geometry, not chosen edge-by-edge from the Möbius signs. Only the final choice between the two parities is source-selected.

## 4. Adversarial controls and what the theorem does not say

Several controls are essential.

First, (6) is in the Euclidean coefficient norm associated with the individually normalized canonical atoms. It does not imply a comparable amount of **Hilbert projection energy** outside the nuisance space. The Gram map may strongly suppress or cancel the transverse coefficient component.

Second, the theorem only defeats a single disjoint adjacent matching at a time. The sum of the even and odd adjacent-difference spaces is much larger, and overlapping adjacent cancellations can interact. Equation (6) therefore does not say that the canonical vector is far from the span of all local finite differences.

Third, (6) does not say that `P_(U^perp) alpha_N` has small Rayleigh quotient. `NB-024` controls the Rayleigh quotient of the full target-selected vector, while `NB-026` constructs low-Rayleigh nuisance sectors. Separating those two statements at the level of the **low spectral projector itself** remains open.

Fourth, the same-sign Möbius input is genuinely arithmetic. If one replaces the source coefficients by an artificial perfectly alternating sign pattern, the pair-sum lower bound can disappear and the vector can align strongly with a checkerboard adjacent-difference family. Thus the conclusion is not another source-independent Gram fact.

Finally, no implication is reversed. Large transverse coefficient mass does not imply `d_N` is small; the theorem says that *if* the canonical residual is small enough to force uniform Möbius locking through `Y_N`, then local sign statistics force the displayed geometry.

## 5. Prior-art boundary and research consequence

Matomäki--Radziwiłł--Tao's positive-density theorem for two-term Möbius value patterns is classical input here and is now anchored in `SOURCES.md`. A targeted prior-art check across Nyman--Beurling/Báez-Duarte coefficient work, finite Gram analyses, Möbius sign-pattern work, and searches combining these topics did not locate the finite-section projection statement (6). Search absence is not a priority proof. The new content claimed here is only the synthesis of the exact local locking from `NB-020`, the adjacent normalized coordinates of `NB-025`, and the positive-density same-sign Möbius input into the transverse-mass inequality.

This answers one precise part of the live spectral question in `RESEARCH_LINES.md`. The target-selected coefficient vector is not merely another arbitrary inhabitant of the large adjacent low-Rayleigh background: at the Möbius-locked scale it carries logarithmically growing mass in pair-sum channels transverse to at least one canonical adjacent matching. The next theorem must preserve this source information while restoring the missing spectral statement—either show that a quantitative portion of the **low-Rayleigh** target-selected mass survives after quotienting a richer universal finite-difference sector, or prove that overlapping/multiscale nuisance modes can absorb the transverse component without changing the Nyman distance. `NB-027` establishes the coefficient-space separation only; RH, closure, and any improved approximation rate remain open.