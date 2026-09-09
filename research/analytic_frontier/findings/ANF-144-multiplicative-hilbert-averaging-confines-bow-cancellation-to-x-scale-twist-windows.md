# ANF-144 — multiplicative Hilbert averaging confines bow cancellation to X-scale twist windows

**Status:** `LITERATURE+DERIVED + CLASSICAL-DIRICHLET-MEAN-VALUE + EXACT-BOW-LOCALIZATION + SHARP-MATCHED-CONTROL`. The logarithmic-twist average in `ANF-102` can be sharpened from an `X^2`-scale window with a harmonic `log K` loss to the classical Montgomery--Vaughan scale `X`, uniformly in the short-interval length. For every coefficient sequence supported where the moving interval can see it, the moving variance differs from its diagonal by only `O(X/L)` relatively after averaging over any twist interval of length `L`. Applied to the Matomäki--Radziwiłł--Shao--Tao--Teräväinen residual of `ANF-102`, every twist interval of length `omega(X)` has diagonal-scale average. Hence a distinguished bow twist with `o(XK log X)` variance cannot belong to a comparably small plateau wider than `O(X)`. This `X` scale is sharp for coefficient-general arguments: a two-adjacent-term real matched control has arbitrarily deep cancellation on fixed-fraction `Theta(X)` twist neighborhoods and vanishing relative variance throughout any prescribed `o(X)` neighborhood. Further progress must therefore use arithmetic structure at the distinguished twist, not another support-only mean-value estimate.

## 1. The moving variance has the classical `L+O(X)` mean-value scale

Let `X>=2`, `1<=K<=X/4`, and let `a(n)` be any finitely supported complex sequence on

\[
X<n\le 2X+K.
\tag{1}
\]

For `x in [X,2X]` and real `U`, put

\[
S_x(U):=\sum_{x<n\le x+K} a(n)n^{-iU},
\qquad
V_a(U;K):=\int_X^{2X}|S_x(U)|^2\,dx,
\tag{2}
\]

and define its exact moving diagonal

\[
D_a(K)
:=\int_X^{2X}\sum_{x<n\le x+K}|a(n)|^2\,dx.
\tag{3}
\]

Then there is an absolute constant `C` such that for every real `U_0` and every `L>0`,

\[
\boxed{
\left|
\frac1L\int_{U_0}^{U_0+L}V_a(U;K)\,dU-D_a(K)
\right|
\le C\frac{X}{L}D_a(K).
}
\tag{4}
\]

In particular the error scale is `X/L`, with no factor `K` and no `log K`.

For a fixed `x`, absorb the initial twist `U_0` into the coefficients and write the active frequencies as

\[
\lambda_n=\log n.
\tag{5}
\]

The Montgomery--Vaughan generalized Hilbert inequality gives the standard Dirichlet-polynomial mean-value estimate

\[
\int_{U_0}^{U_0+L}|S_x(U)|^2\,dU
=
L\sum_{x<n\le x+K}|a(n)|^2
+O\!\left(
\sum_{x<n\le x+K}
\frac{|a(n)|^2}{\delta_n}
\right),
\tag{6}
\]

where

\[
\delta_n
:=
\min_{\substack{m\ne n\\x<m\le x+K}}
|\log n-\log m|.
\tag{7}
\]

If the active set contains only one integer there is no off-diagonal term. Otherwise every `n` lies below `2X+K<=9X/4`, while distinct integers satisfy

\[
|\log n-\log m|
\gg \frac{|n-m|}{X}.
\tag{8}
\]

Thus `delta_n^{-1}<<X` uniformly, and (6) becomes

\[
\int_{U_0}^{U_0+L}|S_x(U)|^2\,dU
=
\left(L+O(X)\right)
\sum_{x<n\le x+K}|a(n)|^2.
\tag{9}
\]

Integrating (9) over `x` and using Fubini proves (4).

For completeness, the same estimate can be seen directly from the Hilbert form. If `b_n` denotes the active coefficient after the `U_0` phase is absorbed and

\[
H(b):=\sum_{m\ne n}\frac{b_n\overline{b_m}}{\lambda_n-\lambda_m},
\tag{10}
\]

then the off-diagonal part of the normalized `U` average is `1/L` times the difference of two such Hilbert forms, one with coefficients `b_n` and one with `b_ne^{-iL\lambda_n}`. Montgomery--Vaughan bounds each by `O(\sum |b_n|^2/\delta_n)`, and the two coefficient vectors have identical moduli. This is exactly why the moving short-interval geometry does not pay the harmonic `log K` loss used in the direct pairwise estimate of `ANF-102`.

## 2. The bow residual cannot stay small on any super-`X` twist interval

Use the residual from `ANF-102`,

\[
a_X(n)=\Lambda(n)-\Lambda^\sharp(n),
\qquad
\Lambda^\sharp(n)
=
\frac{P(R)}{\varphi(P(R))}
1_{(n,P(R))=1},
\quad
R=e^{(\log X)^{1/10}},
\tag{11}
\]

and its moving variance

\[
V_X(U;K)
=
\int_X^{2X}
\left|
\sum_{x<n\le x+K}a_X(n)n^{-iU}
\right|^2dx.
\tag{12}
\]

`ANF-102` proves in the bow range

\[
K=X^{1-2\epsilon+o(1)},
\qquad 0<\epsilon<\frac14,
\tag{13}
\]

that the exact diagonal satisfies

\[
D_X(K)=(1+o(1))XK\log X.
\tag{14}
\]

Substituting (14) into (4) gives, uniformly in the center `U_0`,

\[
\boxed{
\frac1L\int_{U_0}^{U_0+L}V_X(U;K)\,dU
=
D_X(K)\left(1+O\!\left(\frac XL\right)\right).
}
\tag{15}
\]

Consequently, for every `L=L(X)` satisfying

\[
\frac{L}{X}\longrightarrow\infty,
\tag{16}
\]

one has

\[
\boxed{
\frac1L\int_{U_0}^{U_0+L}V_X(U;K)\,dU
=(1+o(1))XK\log X
}
\tag{17}
\]

uniformly for every twist interval of that length. The `X^2` averaging window in `ANF-102` was therefore far from the intrinsic mean-value boundary.

There is also a useful deterministic plateau consequence. Fix `eta in (0,1)`. If an interval `I` of length `L` satisfies

\[
V_X(U;K)\le (1-\eta)D_X(K)
\qquad\text{for every }U\in I,
\tag{18}
\]

then (15) forces

\[
1-\eta
\ge
1-C\frac XL,
\tag{19}
\]

and hence

\[
\boxed{L\le C\eta^{-1}X.}
\tag{20}
\]

In particular, a hypothetical distinguished bow twist with `V_X=o(XK log X)` may still exist, but it cannot sit inside a uniformly vanishing plateau of width `omega(X)`. Since the bow twist scale is `U asymp X^2`, the generic mean-value theorem localizes any robust exceptional behavior to relative twist precision

\[
\frac{\Delta U}{U}=O\!\left(\frac1X\right).
\tag{21}
\]

This is a substantially narrower target than the full `U asymp X^2` regime, but it is not yet an arithmetic contradiction.

## 3. Two adjacent coefficients show that the `X` scale is sharp

The `X` in (4) is not an artifact of the proof. It is forced by the nearest logarithmic frequency spacing.

Take an integer `K>=2`, choose an integer `M` with

\[
X+K\le M\le 2X-1,
\tag{22}
\]

and set

\[
a(M)=1,
\qquad
a(M+1)=-1,
\qquad
a(n)=0\ \text{otherwise}.
\tag{23}
\]

Both terms are present simultaneously for an `x` interval of length `K-1`; each appears alone on one boundary interval of length `1`. Therefore

\[
D_a(K)=2K
\tag{24}
\]

and, with

\[
\delta_M:=\log\left(1+\frac1M\right),
\tag{25}
\]

the variance is exactly

\[
\boxed{
V_a(U;K)
=2+4(K-1)\sin^2\!\left(\frac{U\delta_M}{2}\right).
}
\tag{26}
\]

At `U=0`, only the two one-sided boundary pieces remain and

\[
\frac{V_a(0;K)}{D_a(K)}=\frac1K.
\tag{27}
\]

More importantly, since `delta_M<=1/M<=1/X`, for every `r_X>0`,

\[
\sup_{|U|\le r_XX}
\frac{V_a(U;K)}{D_a(K)}
\le
\frac1K+rac{r_X^2}{2}.
\tag{28}
\]

Thus if `K=K(X)->infinity` and `r_X->0`,

\[
\boxed{
\sup_{|U|\le r_XX}
\frac{V_a(U;K)}{D_a(K)}
\longrightarrow0.
}
\tag{29}
\]

The vanishing-cancellation neighborhood may therefore have any sublinear width `r_XX=o(X)` allowed by a slowly vanishing `r_X`; for fixed fractional savings, choosing a sufficiently small fixed `r` gives a cancellation plateau of width `Theta(X)`. No argument that sees only arbitrary coefficients on integers `n asymp X`, their support length, and the logarithmic twist can improve the `X` localization scale to a universal smaller order. The source-specific arithmetic of `Lambda-Lambda^sharp` must enter.

## 4. Prior-art boundary and novelty assessment

The load-bearing analytic estimate is classical. Montgomery and Vaughan, **Hilbert's Inequality**, *Journal of the London Mathematical Society* (2) 8:1 (1974), 73--82, DOI `10.1112/jlms/s2-8.1.73`, gives the generalized Hilbert inequality underlying the standard mean-value theorem for Dirichlet polynomials. In its familiar form,

\[
\int_{T_0}^{T_0+L}
\left|\sum_{n\le N}c_nn^{-it}\right|^2dt
=
L\sum_{n\le N}|c_n|^2
+O\!\left(\sum_{n\le N}n|c_n|^2\right),
\tag{30}
\]

uniformly in the starting point. Equation (4) is the immediate moving-window specialization obtained by applying that theorem before integrating in `x`.

Matomäki--Radziwiłł--Shao--Tao--Teräväinen, **Higher uniformity of arithmetic functions in short intervals II. Almost all intervals**, *Inventiones Mathematicae* 244 (2026), 967--1091, DOI `10.1007/s00222-026-01408-6`, supplies the `Lambda^sharp` framework already anchored in `ANF-102`. No new literature theorem is being claimed here.

The Mathia delta is the combination of three exact observations: the classical `O(X)` mean-value remainder removes the `log K` loss from the stored bow calculation; the resulting every-interval estimate localizes any robust special-twist cancellation to absolute width `O(X)`; and the explicit adjacent-pair control (26) proves that this scale is sharp for coefficient-general reasoning. Both literature anchors are already present in `research/analytic_frontier/SOURCES.md`, so no source-list change is required.

## 5. Boundaries, falsification tests, and research consequence

The result does **not** show that the actual distinguished bow twist is generic. It does not rule out an isolated or rapidly varying arithmetic resonance, does not bound the measure of all low-variance twists, and does not prove the macroscopic negative off-diagonal correlation required by `ANF-102` impossible. A large positive spike can compensate many small values inside an interval unless one adds higher-moment or pointwise information, so (15) must not be misread as a density theorem for exceptional twists.

The decisive audit of (4) is elementary: for each fixed `x`, apply the Montgomery--Vaughan mean-value theorem to the finite active polynomial and verify that every active integer lies at `asymp X`, so `sum n|a(n)|^2<<X sum|a(n)|^2`; then integrate in `x`. The sharpness audit is the exact three-region overlap computation leading to (26). Failure of either calculation would falsify the claimed localization.

For the analytic-frontier program, the remaining bow problem is now more precise. Any proof that averages the twist on a scale `omega(X)` necessarily washes the variance back to the prime diagonal, while support-only information cannot exclude cancellation on `Theta(X)` scales. A successful source-side theorem must therefore preserve the sign of the off-diagonal correlation at a twist specified to `O(X)` absolute accuracy inside the `U asymp X^2` regime, or explicitly subtract the unavoidable diagonal before averaging. This replaces a broad `U asymp X^2` uniformity request by a genuinely local arithmetic-resonance problem.