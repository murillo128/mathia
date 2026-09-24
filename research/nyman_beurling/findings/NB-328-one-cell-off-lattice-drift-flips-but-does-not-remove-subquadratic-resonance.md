# NB-328 — One-cell off-lattice drift flips but does not remove subquadratic resonance

- **Date:** 2026-09-24
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-304, NB-314, NB-327
- **Classification:** `EXACT-DERIVED + SOURCE-SIDE + WEIGHTED-BILINEAR-MIXING + OFF-LATTICE-DRIFT + ADJACENT-WITNESS + RANK-ONE-ERROR + LINEAR-TO-SUBQUADRATIC-RESONANCE + SIGN-REVERSAL + METHOD-DISCRIMINATOR + NON-TARGET-AWARE + PRIOR-ART-AUDITED`

## Claim

Let

\[
U_n:=\operatorname{span}\{g_2,\ldots,g_n\},
\qquad
T_{n,m}:=P_{U_n}A_m|_{U_n},
\]

let `R_n` be the rank-one comparison operator from `NB-314`, and use the same adjacent cancellation as in `NB-327`,

\[
u_n:=g_n-\frac{n-1}{n}g_{n-1}.
\tag{1}
\]

For arbitrary integers `n>=3` and `d>=1`, put

\[
m^+_{n,d}:=dn
\tag{2}
\]

and define

\[
\mathcal E^+_{n,d}
:=
\left\langle
(\sqrt{dn}\,T_{n,dn}-R_n)g_2,u_n
\right\rangle.
\tag{3}
\]

Then

\[
\boxed{
\left|
\mathcal E^+_{n,d}+\frac{\log2}{4n}
\right|
\le
\frac{2d}{(n-1)^2}.
}
\tag{4}
\]

Consequently, for every integer sequence `d_n=o(n)`, one has

\[
\boxed{
n\mathcal E^+_{n,d_n}\longrightarrow-\frac{\log2}{4}.
}
\tag{5}
\]

Combining this with `NB-327`, which proves

\[
n\mathcal E^-_{n,d_n}\longrightarrow+\frac{\log2}{4}
\qquad
\text{for }m^-_{n,d_n}=d_n(n-1),
\tag{6}
\]

shows that a full one-cell drift of the selector across the first adjacent-profile period does **not** create subquadratic mixing. It reverses the sign of this explicit rank-one-error channel while preserving its magnitude.

Using `||g_2||_2^2=\log2/4` and the adjacent-witness estimate from `NB-304`,

\[
\|u_n\|_2^2
\le
\frac{2H_{n-2}+1+\pi^2/18}{n^2},
\tag{7}
\]

we therefore also have, for every `d_n=o(n)`,

\[
\boxed{
\liminf_{n\to\infty}
\sqrt{\log n}\,
\|\sqrt{d_n n}\,T_{n,d_n n}-R_n\|
\ge
\frac{\sqrt{\log2}}{2\sqrt2}>0.
}
\tag{8}
\]

Thus the obstruction from `NB-327` is not confined to the lattice `m=d(n-1)`. The neighboring lattice `m=dn=d(n-1)+d` carries the same logarithmic operator-norm obstruction with opposite matrix-coefficient phase. The statement remains source-side and does not imply target occupation, finite-section excess, a Nyman approximation rate, or RH.

## 1. Rescaling on the neighboring lattice

For the standard reciprocal profile

\[
F_{g_j}(t)=\left\{\frac tj\right\}-\frac1j\{t\},
\]

the `\{t\}` terms cancel in (1), giving

\[
F_{u_n}(t)
=
\left\{\frac tn\right\}
-
\frac{n-1}{n}
\left\{\frac{t}{n-1}\right\}.
\tag{9}
\]

Its reciprocal mean is

\[
\mu(u_n)
=
\frac{n-1}{2n}
-
\frac{n-1}{n}\frac{n-2}{2(n-1)}
=
\frac1{2n}.
\tag{10}
\]

Hence the centered profile is

\[
\widetilde F_n(t)
=
\left\{\frac tn\right\}
-
\frac{n-1}{n}
\left\{\frac{t}{n-1}\right\}
-
\frac1{2n}.
\tag{11}
\]

`NB-327` scaled this profile by `n-1`, because `m=d(n-1)` made the `g_2` selector cell-aligned. For the off-lattice choice `m=dn`, scale instead by `n`:

\[
h_n(y):=\widetilde F_n(ny).
\tag{12}
\]

The function `h_n` is `(n-1)`-periodic. If

\[
y=k+r,
\qquad
0\le k\le n-2,
\qquad
0\le r<1,
\]

then direct fractional-part algebra gives

\[
\boxed{
h_n(k+r)
=
\frac{n-1}{n}
\mathbf1_{\{r\ge(n-1-k)/n\}}
-
\frac{k+1/2}{n}.
}
\tag{13}
\]

This is the reflected companion of the pulse formula used in `NB-327`: the positive jump now sits near the **right** edge of each unit cell rather than near the left edge.

By the exact rank-one-error identity from `NB-314`,

\[
\mathcal E^+_{n,d}
=
\int_0^\infty
F_{g_2}(t)\widetilde F_n(dnt)
\frac{dt}{t^2}.
\tag{14}
\]

Changing variables `y=dt` gives

\[
\boxed{
\mathcal E^+_{n,d}
=
d\int_0^\infty
s_d(y)h_n(y)\frac{dy}{y^2},
\qquad
s_d(y):=F_{g_2}(y/d).
}
\tag{15}
\]

Because `d` is an integer, the selector is again constant on every unit cell:

\[
s_d(y)=
\begin{cases}
0,&y\in[2jd,(2j+1)d),\\[1mm]
1/2,&y\in[(2j+1)d,(2j+2)d),
\end{cases}
\qquad j\ge0.
\tag{16}
\]

Thus `m=dn` is genuinely off the `NB-327` lattice, but after the natural neighboring rescaling it has an equally exact cell decomposition.

## 2. Every selected first-period cell contributes the opposite sign

Fix a selected unit cell `[k,k+1)` with `1<=k<=n-2`. Put

\[
\theta_k:=\frac{n-1-k}{n},
\qquad
c_k:=\frac{k+1/2}{n}.
\]

Using (13),

\[
\begin{aligned}
\int_k^{k+1}\frac{h_n(y)}{y^2}\,dy
&=
\frac{n-1}{n}
\int_{k+\theta_k}^{k+1}\frac{dy}{y^2}
-c_k\int_k^{k+1}\frac{dy}{y^2}\\[1mm]
&=
\frac1{n(k+1)}
-
\frac{k+1/2}{n\,k(k+1)}\\[1mm]
&=
\boxed{-\frac1{2n\,k(k+1)}}.
\end{aligned}
\tag{17}
\]

The selector contributes the extra factor `1/2`. Therefore the complete first profile period is

\[
I^{(0),+}_{n,d}
=
-\frac{d}{4n}
\sum_{\substack{1\le k<n-1\\ \lfloor k/d\rfloor\ \mathrm{odd}}}
\frac1{k(k+1)}.
\tag{18}
\]

As in `NB-327`, the infinite selected-cell sum telescopes block by block:

\[
d
\sum_{\substack{k\ge1\\ \lfloor k/d\rfloor\ \mathrm{odd}}}
\frac1{k(k+1)}
=
\log2.
\tag{19}
\]

The omitted terms have `k>=n-1`, hence

\[
0\le
\frac{\log2}{d}
-
\sum_{\substack{1\le k<n-1\\ \lfloor k/d\rfloor\ \mathrm{odd}}}
\frac1{k(k+1)}
\le
\frac1{n-1}.
\tag{20}
\]

It follows that

\[
\boxed{
\left|
I^{(0),+}_{n,d}+\frac{\log2}{4n}
\right|
\le
\frac{d}{4n(n-1)}.
}
\tag{21}
\]

The sign reversal is therefore already complete inside the first `(n-1)` cells. It is not produced by a remote tail or by a delicate common-period argument.

## 3. Cellwise centering still suppresses the infinite tail

For a global cell `[K,K+1)` with `K>=n-1`, put

\[
k:=K\bmod(n-1).
\]

The unweighted mean of (13) over that cell is

\[
\begin{aligned}
b_k
&:=\int_0^1h_n(k+r)\,dr\\
&=
\frac{n-1}{n}\frac{k+1}{n}
-
\frac{k+1/2}{n}\\
&=
\boxed{\frac{n/2-k-1}{n^2}}.
\end{aligned}
\tag{22}
\]

Therefore

\[
|b_k|\le\frac1{2n}.
\tag{23}
\]

Set `q_k(r):=h_n(k+r)-b_k`. Then `int_0^1 q_k(r)dr=0`, while `|h_n|<1` and `|q_k|<3/2`. With `w_K(r)=(K+r)^{-2}`, the zero-mean part satisfies

\[
\left|
\int_0^1q_k(r)w_K(r)\,dr
\right|
\le
\frac3{K^3},
\tag{24}
\]

because `|w_K(r)-w_K(0)|<=2/K^3`. The mean part obeys

\[
\left|
b_k\int_0^1w_K(r)\,dr\right|
\le
\frac1{2nK(K+1)}.
\tag{25}
\]

Since `s_d` is constant on each unit cell and `|s_d|<=1/2`, the tail beginning after the first profile period satisfies

\[
\begin{aligned}
|\mathcal T^+_{n,d}|
&\le
\frac d2
\sum_{K=n-1}^\infty
\left(
\frac3{K^3}
+
\frac1{2nK(K+1)}
\right)\\[1mm]
&\le
\boxed{\frac{7d}{4(n-1)^2}}.
\end{aligned}
\tag{26}
\]

Here we used, for `n>=3`,

\[
\sum_{K=n-1}^\infty K^{-3}\le(n-1)^{-2},
\qquad
\sum_{K=n-1}^\infty\frac1{K(K+1)}=\frac1{n-1}.
\tag{27}
\]

Combining (21) and (26) gives

\[
\left|
\mathcal E^+_{n,d}+\frac{\log2}{4n}
\right|
\le
\frac{d}{4n(n-1)}
+
\frac{7d}{4(n-1)^2}
\le
\frac{2d}{(n-1)^2},
\]

which proves (4).

## 4. A one-cell drift is a phase flip, not a mixing mechanism

If `d_n=o(n)`, (4) yields (5). Dividing by the physical norms of `g_2` and `u_n` gives (8), exactly the same logarithmic lower obstruction as on the `m=d(n-1)` lattice of `NB-327`.

The comparison is particularly sharp because

\[
m^+_{n,d}-m^-_{n,d}=d,
\qquad
\frac{m^+_{n,d}-m^-_{n,d}}{m^-_{n,d}}
=\frac1{n-1}.
\tag{28}
\]

Thus a relative perturbation of only `1/(n-1)` changes this explicit matrix coefficient from

\[
+\frac{\log2}{4n}+o(n^{-1})
\quad\text{to}\quad
-\frac{\log2}{4n}+o(n^{-1}),
\tag{29}
\]

while its operator-norm obstruction remains of order `1/sqrt(log n)` at both endpoints.

This narrows the source-side frontier left by `NB-327`. Merely leaving the integer-multiple lattice `d(n-1)`, or even accumulating one complete unit cell of selector drift across the first adjacent period, is not enough to force mixing below quadratic scale. The unresolved question is now the **intermediate drift phase** between these two resonant lattices: for

\[
m=d(n-1)+r,
\qquad
0<r<d,
\tag{30}
\]

does the adjacent channel pass through a genuine cancellation window, and if so is that cancellation stable in operator norm or merely a zero of this one signed matrix coefficient? Resolving that distinction is necessary before off-lattice drift can serve as a mechanism for uniform moving-`n` mixing.

For every fixed `1<=alpha<2`, taking `d_n=max{1,floor(n^(alpha-1))}` gives `d_n=o(n)` and

\[
m^+_{n,d_n}=n^{\alpha+o(1)},
\]

so the obstruction persists on this off-`NB-327` lattice at every subquadratic power scale.

## 5. Prior-art boundary and adversarial checks

A fresh literature audit again places the result next to the discrete integer-dilation strengthening of Báez-Duarte, multiplicative fractional-part autocorrelation, and modern Gram-geometry work on Nyman-Beurling systems. Those sources establish the broader dilation/Gram setting, but the present proof uses no external theorem beyond the repository's already established identities. The audit did not locate this finite-section neighboring-lattice sign-reversal statement; no bibliographic novelty claim is made from that absence, and `SOURCES.md` therefore needs no new load-bearing entry.

The proof was stress-tested at the points most likely to hide an indexing or scaling error:

- the mean in (10) is recomputed directly from the known reciprocal means of `g_n` and `g_{n-1}`;
- the period of `h_n` is `n-1`, not `n`, because the original adjacent profile has period `n(n-1)` and is rescaled by `n`;
- the threshold in (13) is `(n-1-k)/n`; inserting it into the weighted cell integral gives the exact negative sign in (17);
- the singular endpoint `y=0` is harmless because `s_d=0` on `[0,d)`;
- the tail estimate uses only cellwise zero-mean cancellation and the `O(1/n)` cell mean, so it does not assume a common global period of `s_d h_n`;
- the asymptotic claim is restricted to `d=o(n)`; the finite bound (4) itself remains valid for arbitrary integer `d>=1`.

No target-aware conclusion is inferred from the source-side matrix coefficient.