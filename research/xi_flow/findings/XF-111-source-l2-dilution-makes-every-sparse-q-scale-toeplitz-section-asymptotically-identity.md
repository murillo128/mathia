# XF-111 — source L2 dilution makes every sparse q-scale Toeplitz section asymptotically identity

**Status:** `EXACT-DERIVED` + `UNIFORM-SPARSE-POSITIVITY` + `BAD-SUBSPACE-INCOHERENCE` + `TOEPLITZ-FEASIBILITY-BOUNDARY`. XF-110 showed that the fixed-q-scale source Toeplitz matrix has vanishing off-diagonal `ell^2` coefficient mass, that only a vanishing fraction of its spectrum can be nonpositive, and that every *eigenvector* in that bad spectrum uses `Omega(q/(log q)^2)` coordinates. Its stated boundary left arbitrary nonpositive Rayleigh witnesses uncontrolled. The same `ell^2` dilution in fact gives a uniform restricted estimate on **every** coordinate set: every principal section with `o(q/(log q)^2)` coordinates converges to the identity in operator norm. Consequently every nonpositive Toeplitz witness, not only an eigenvector, must use `Omega(q/(log q)^2)` coordinates. Moreover every such sparse coordinate subspace has vanishing overlap with the entire exceptional spectral subspace of the full Toeplitz matrix.

Keep the mass-preserving q-scale source interface of XF-108--XF-110,

\[
N=2q^2,
\qquad
\Delta^2\asymp q^{-3},
\qquad
a:=N\Delta\asymp q^{1/2},
\qquad
\Delta\asymp a^{-3},
\tag{1}
\]

with fixed

\[
L=\log a+c,
\qquad
K=\left\lfloor\frac{L}{\Delta}\right\rfloor,
\qquad c\in\mathbf R,
\tag{2}
\]

and Hermitian Toeplitz moment matrix

\[
\widehat T_K=(\widehat\mu_{i-j})_{0\le i,j\le K},
\qquad
\widehat\mu_0=1.
\tag{3}
\]

XF-110 proves

\[
\boxed{
S_2(a):=\sum_{m=1}^K|\widehat\mu_m|^2
\ll_{\psi,c}\frac{(\log a)^2}{a^2}.
}
\tag{4}
\]

Let `I subset {0,...,K}` have `s=|I|`, let `\widehat T_I` denote the corresponding principal section, and let `A_K=\widehat T_K-I`. Then

\[
\boxed{
\|\widehat T_I-I_s\|_{\rm op}
\le
\sqrt{2sS_2(a)}.
}
\tag{5}
\]

Hence

\[
\boxed{
1-\sqrt{2sS_2(a)}
\le
\lambda_{\min}(\widehat T_I)
\le
\lambda_{\max}(\widehat T_I)
\le
1+\sqrt{2sS_2(a)}.
}
\tag{6}
\]

Uniformly over **all** coordinate sets,

\[
\boxed{
|I|=o\!\left(\frac{a^2}{(\log a)^2}\right)
\quad\Longrightarrow\quad
\|\widehat T_I-I_s\|_{\rm op}=o(1).
}
\tag{7}
\]

Equivalently, every unit vector `v` with `s=|supp v|` satisfies

\[
\boxed{
v^*\widehat T_Kv
\ge
1-\sqrt{2sS_2(a)}.
}
\tag{8}
\]

Therefore any arbitrary nonpositive Rayleigh witness obeys

\[
\boxed{
v^*\widehat T_Kv\le0
\quad\Longrightarrow\quad
|\operatorname{supp}v|
\ge
\frac1{2S_2(a)}
\gg_{\psi,c}
\frac{a^2}{(\log a)^2}
\asymp
\frac{q}{(\log q)^2}.
}
\tag{9}
\]

This closes the eigenvector-only boundary left explicit in XF-110.

## 1. Frobenius dilution is stronger than pointwise Gershgorin on sparse sections

For `i,j in I`, `i ne j`, the off-diagonal entry of `\widehat T_I-I_s` is `\widehat\mu_{i-j}`. For a fixed row index `i`, each positive lag `m` can occur at most twice among the differences `|i-j|`. Therefore

\[
\sum_{\substack{j\in I\\j\ne i}}
|\widehat\mu_{i-j}|^2
\le
2S_2(a).
\tag{10}
\]

Summing `(10)` over the `s` retained rows gives

\[
\|\widehat T_I-I_s\|_{\rm HS}^2
\le
2sS_2(a).
\tag{11}
\]

Since the operator norm is bounded by the Hilbert--Schmidt norm, `(5)` follows immediately. The min--max principle gives `(6)`, and `(4)` then gives `(7)`.

For a vector `v` supported on `I`, its full Toeplitz quadratic form equals the quadratic form of the principal section:

\[
v^*\widehat T_Kv=v_I^*\widehat T_Iv_I.
\tag{12}
\]

Applying `(6)` proves `(8)`. If the left side of `(8)` is nonpositive, then `\sqrt{2sS_2(a)}\ge1`, which proves `(9)`.

The gain over XF-106 is exactly the switch from `ell^infty` coefficient control to `ell^2` coefficient control. XF-106 used `|\widehat\mu_m|=O(a^{-1})` and a row `ell^1` estimate, producing the threshold `s=Omega(a)`. At the q-scale source, `(4)` instead makes the restricted Frobenius perturbation only `O(\sqrt{s}\log a/a)`, raising the support threshold to almost `a^2 asymp q`.

More generally, for any fixed depression `0<delta<=1`,

\[
v^*\widehat T_Kv
\le(1-\delta)\|v\|_2^2
\quad\Longrightarrow\quad
|\operatorname{supp}v|
\ge
\frac{\delta^2}{2S_2(a)}.
\tag{13}
\]

Thus `(7)` is a restricted near-isometry statement, not merely a sign test.

## 2. Sparse coordinate spaces are incoherent with the whole exceptional spectrum

The same argument controls more than principal-minor signs. For fixed `eta>0`, let

\[
E_\eta
=
\mathbf 1_{\{|\widehat T_K-I|\ge\eta\}}
\tag{14}
\]

be the spectral projector onto eigenvalues satisfying `|lambda-1|>=eta`. Functional calculus gives the positive-semidefinite operator inequality

\[
E_\eta
\preceq
\eta^{-2}A_K^2.
\tag{15}
\]

For each coordinate `i`,

\[
(A_K^2)_{ii}
=
\sum_{j\ne i}|\widehat\mu_{i-j}|^2
\le
2S_2(a),
\tag{16}
\]

so

\[
\boxed{
(E_\eta)_{ii}
\le
\frac{2S_2(a)}{\eta^2}
}
\tag{17}
\]

uniformly in `i`. If `P_I` is the coordinate projector onto a set `I` of size `s`, positivity and the trace bound yield

\[
\begin{aligned}
\|P_IE_\eta P_I\|_{\rm op}
&\le
\operatorname{tr}(P_IE_\eta P_I)\\
&=
\sum_{i\in I}(E_\eta)_{ii}\\
&\le
\frac{2sS_2(a)}{\eta^2}.
\end{aligned}
\tag{18}
\]

Consequently every unit vector `v` supported on `I` satisfies

\[
\boxed{
\|E_\eta v\|_2^2
\le
\frac{2sS_2(a)}{\eta^2}.
}
\tag{19}
\]

In particular, if `s=o(a^2/(log a)^2)`, then for every fixed `eta>0` the vector has `o(1)` mass in the entire exceptional spectrum outside `[1-eta,1+eta]`. Taking `eta=1`, the projector `P_-` onto the nonpositive spectrum obeys `P_-\preceq E_1`, so

\[
\boxed{
\|P_-v\|_2^2
\le
2sS_2(a)
=o(1)
}
\tag{20}
\]

for every such sparse family. Thus the thin bad spectrum of XF-110 is not allowed to align strongly with *any* sparse coordinate subspace, even when the sparse vector is not itself an eigenvector.

As a check, applying `(20)` to a nonpositive eigenvector `v` with support size `s` gives `P_-v=v`, hence `1<=2sS_2(a)` and recovers the almost-q eigenvector support bound of XF-110. Equation `(9)` is stronger in quantifier because it applies to every nonpositive Rayleigh witness, including mixtures of positive and negative spectral directions.

## 3. Stress tests and exact boundary

The result does **not** prove global Toeplitz positivity. At the fixed q-scale cutoff,

\[
K+1\asymp a^3\log a,
\tag{21}
\]

whereas the guaranteed near-identity range is only `o(a^2/(log a)^2)`. There remains a large interval of genuinely collective supports between almost `q` coordinates and the full `q^{3/2}log q` matrix dimension. An indefinite matrix can therefore satisfy every estimate above.

The conclusion also remains only at the weighted Toeplitz/Caratheodory relaxation isolated in XF-084. Even eventual positivity of `\widehat T_K` would not by itself produce the exact equal-weight real-divisor carrier required by XF-085. Conversely, failure of equal-weight realization need not produce a negative Toeplitz witness.

The fixed offset `c` in `L=log a+c` and the q-scale `ell^2` estimate `(4)` are load-bearing for the stated powers. A moving cutoff requires recomputing `S_2(a)` before importing `(7)`--`(9)`. The matrix inequalities `(5)`, `(8)`, `(15)`, and `(19)` themselves are deterministic and remain valid for any Hermitian Toeplitz matrix after substituting its actual `S_2`.

No RH input enters. No use is made of PNT beyond whatever is already built into the canonical mass-preserving source interface; the quantitative `S_2` bound being consumed here was proved in XF-110 from Chebyshev-level prime estimates.

## 4. Prior-art audit

The norm inequalities used above are elementary finite-dimensional linear algebra. The language is neighboring to restricted-isometry/restricted-eigenvalue theory, and structured Toeplitz/Fourier matrices are extensively studied there, but those results concern different matrix ensembles and recovery questions. No novelty is claimed for `||A||op<=||A||HS`, the min--max principle, spectral projectors, or the general idea of sparse restricted conditioning.

A targeted search also rechecked the nearby RH-facing Toeplitz literature already identified in XF-106 and XF-109. Connes--van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the Spectral Action* (Communications in Mathematical Physics 406 (2025), article 312), studies zero localization from positive Toeplitz/convolution forms, while Michalowski, *An explicit uniform cubic wedge for consecutive Toeplitz minors of the Riemann xi coefficients* (arXiv:2607.16795, 2026), studies a different Toeplitz matrix formed from the positive Taylor coefficients of normalized xi. Neither is the Guinand--Weil/Vieta source moment matrix `(3)`, and neither supplies the q-scale restricted estimate `(5)` or the witness threshold `(9)`. The durable additional statement here is therefore the Xi-source specialization of XF-110's `ell^2` dilution, not a new matrix-norm theorem. No new external theorem is load-bearing, so `SOURCES.md` needs no change.

## 5. Consequence for the live source-side frontier

The collective obstruction is substantially more constrained than after XF-106. At the natural q arithmetic scale, **every** nonpositive source-Toeplitz certificate now needs

\[
|\operatorname{supp}v|
\gg
\frac{q}{(\log q)^2},
\tag{22}
\]

not merely `Omega(q^{1/2})`. Together with XF-107 and XF-109, such a witness must simultaneously span physical lag length `log a-O(1)` and carry fixed coefficient-Fourier mass outside the PNT-flat central arc. XF-110 adds that the whole nonpositive eigenspace still has only `O(q^{1/2}(log q)^3)` dimensions.

This leaves a sharply collective, long-range, rough, low-dimensional source obstruction. Searching for a small principal minor, a sparse polynomial certificate, or a sparse vector with a tiny admixture of bad spectral modes can no longer resolve the q-scale feasibility gate. A useful next step must control the genuinely dense rough sector itself, or exploit an Xi-specific structure showing that the thin exceptional subspace cannot actually cross zero.

Nothing here supplies the separate destination-side theorem required to convert source feasibility into an upper bound on the de Bruijn--Newman constant.