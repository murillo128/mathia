# FD-305 — Common-window correlation crowding forces a Möbius Fourier fourth-moment spike

- **Date:** 2026-09-24
- **Status:** proved deterministic Fourier compression of the FD-304 common-window correlation family
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** block-Mertens field / common-window correlations / exact autocorrelation / Fourier fourth moment / additive spectral concentration / capacity obstruction
- **Depends on:** FD-300, FD-303, FD-304
- **Classification:** `RH-CONDITIONAL-INPUT + EXACT-FOURIER-COMPRESSION + FOURTH-MOMENT-INFLATION + ADDITIVE-SPECTRAL-SPIKE + CAPACITY-BOUNDARY + ROUTE-REDUCTION`

## Claim

Continue with

\[
U_N(q)=M(Nq)-M(N(q-1)),
\qquad
G_N(d)=\sum_{q\mid d}U_N(q),
\tag{1}
\]

\[
L_N(x)=\sum_{x<d\le2x}|G_N(d)|,
\qquad
c:=1-\log_2(3/2)=0.4150374992\ldots,
\tag{2}
\]

and the near-capacity premise

\[
L_N(x)\ge N^{1/2}x^{1+c-o(1)}.
\tag{3}
\]

Assume RH and a fixed polynomial-depth regime

\[
x=N^{\lambda+o(1)}.
\tag{4}
\]

For

\[
\lambda>\frac{3}{10c}=0.7228262519\ldots,
\tag{5}
\]

FD-304 gives a capacity-bearing dyadic shell `Q<q<=2Q`, with

\[
Q\ge x^{2c-o(1)},
\qquad
X:=NQ,
\tag{6}
\]

and a set `\mathcal H\subset[1,N)` of distinct shifts satisfying

\[
|\mathcal H|
\ge
N^{-1/2}x^{3c-o(1)}
\tag{7}
\]

and

\[
C_h^0(X)
:=
\sum_{X\le n<2X}\mu(n)\mu(n+h)
\ge
Q N^{-1/2}x^{3c-o(1)}
\tag{8}
\]

for every `h\in\mathcal H`.

Define the compactly supported Möbius block

\[
f_X(n):=\mu(n)\mathbf 1_{[X,2X)}(n)
\tag{9}
\]

and its additive Fourier transform

\[
F_X(\alpha)
:=
\sum_{n\in\mathbb Z}f_X(n)e(n\alpha)
=
\sum_{X\le n<2X}\mu(n)e(n\alpha),
\qquad
e(t):=e^{2\pi i t}.
\tag{10}
\]

Then the common-window family (7)--(8) forces

\[
\boxed{
\int_0^1|F_X(\alpha)|^4\,d\alpha
\ge
Q^2N^{-3/2}x^{9c-o(1)}.
}
\tag{11}
\]

Equivalently, relative to the natural `X^2` fourth-moment scale,

\[
\boxed{
\frac{1}{X^2}
\int_0^1|F_X(\alpha)|^4\,d\alpha
\ge
N^{-7/2}x^{9c-o(1)}.
}
\tag{12}
\]

Hence, once

\[
\boxed{
\lambda>
\frac{7}{18c}
=0.9369969932\ldots,
}
\tag{13}
\]

the near-capacity premise forces a power-sized fourth-moment inflation above `X^2`.

Parseval also gives

\[
\int_0^1|F_X(\alpha)|^2\,d\alpha
=
\sum_{X\le n<2X}\mu(n)^2
\le X.
\tag{14}
\]

Therefore (11) forces at least one source-selected frequency `\alpha_*\in[0,1)` with

\[
\boxed{
|F_X(\alpha_*)|
\ge
Q^{1/2}N^{-5/4}x^{9c/2-o(1)}.
}
\tag{15}
\]

Relative to square-root size,

\[
\boxed{
\frac{|F_X(\alpha_*)|}{X^{1/2}}
\ge
N^{-7/4}x^{9c/2-o(1)}.
}
\tag{16}
\]

Thus the same threshold (13) makes the forced additive Fourier coefficient a fixed power larger than `X^{1/2}`. The many-shift common-window Chowla-type obstruction of FD-304 can therefore be compressed into one exact additive-spectral obstruction.

At balanced depth `\lambda=1`,

\[
9c-\frac72
=
0.2353374935\ldots,
\tag{17}
\]

so

\[
\int_0^1|F_X(\alpha)|^4\,d\alpha
\ge
X^2N^{0.2353374935\ldots-o(1)},
\tag{18}
\]

and

\[
\frac{|F_X(\alpha_*)|}{X^{1/2}}
\ge
N^{0.1176687467\ldots-o(1)}.
\tag{19}
\]

The conclusion is one-way. It does not localize `\alpha_*`, does not prove a contradiction with known Möbius exponential-sum bounds, and does not claim that every large Fourier coefficient reconstructs the FD-304 correlation family.

## 1. Trim the common-window family to exact autocorrelations

The fixed-window correlations in FD-304 are not quite Fourier coefficients of `|F_X|^2`, because their upper endpoint does not shrink with the shift. Introduce instead the exact autocorrelation

\[
R_h(X)
:=
\sum_{n\in\mathbb Z}f_X(n)f_X(n+h).
\tag{20}
\]

For `1\le h<N`, compact support gives

\[
R_h(X)
=
\sum_{X\le n<2X-h}\mu(n)\mu(n+h).
\tag{21}
\]

Comparing with (8), only the terminal interval of length `h` is removed. Since `|\mu|\le1`,

\[
|C_h^0(X)-R_h(X)|\le h\le N.
\tag{22}
\]

Write the FD-304 correlation amplitude as

\[
A_Q:=Q N^{-1/2}x^{3c-o(1)}.
\tag{23}
\]

By the RH shell floor in (6),

\[
\frac{A_Q}{N}
\ge
N^{-3/2}x^{5c-o(1)}.
\tag{24}
\]

Using `x=N^{\lambda+o(1)}`,

\[
N^{-3/2}x^{5c-o(1)}
=
N^{5c\lambda-3/2-o(1)}.
\tag{25}
\]

The exponent in (25) is positive exactly under (5). Hence

\[
N=o(A_Q),
\tag{26}
\]

and every selected shift from FD-304 satisfies

\[
R_h(X)
\ge
A_Q(1-o(1)).
\tag{27}
\]

This boundary check is essential. Without (5), the common-window correlations cannot simply be inserted into the Fourier identity below, because the terminal strip can be comparable with the forced correlation scale. No new threshold is paid here: (5) is exactly the same depth condition already required by FD-304 to remove the earlier moving-start freedom.

## 2. The correlation family is an exact Fourier fourth moment

Expanding (10),

\[
|F_X(\alpha)|^2
=
\sum_{m,n}f_X(m)f_X(n)e((m-n)\alpha).
\tag{28}
\]

Therefore its `h`-th Fourier coefficient is the compact autocorrelation:

\[
\int_0^1|F_X(\alpha)|^2e(-h\alpha)\,d\alpha
=
R_h(X),
\tag{29}
\]

up to the immaterial choice of sign convention for `h`. Parseval applied to `|F_X|^2` gives the exact Wiener identity

\[
\boxed{
\int_0^1|F_X(\alpha)|^4\,d\alpha
=
\sum_{h\in\mathbb Z}|R_h(X)|^2.
}
\tag{30}
\]

FD-304 already counts distinct shifts, so no multiplicity correction is needed. Combining (7), (27), and (30),

\[
\begin{aligned}
\int_0^1|F_X(\alpha)|^4\,d\alpha
&\ge
\sum_{h\in\mathcal H}|R_h(X)|^2\\
&\ge
|\mathcal H|A_Q^2x^{-o(1)}\\
&\ge
\left(N^{-1/2}x^{3c-o(1)}\right)
\left(Q^2N^{-1}x^{6c-o(1)}\right)\\
&=
Q^2N^{-3/2}x^{9c-o(1)}.
\end{aligned}
\tag{31}
\]

This proves (11). Since `X=NQ`, division by `X^2=N^2Q^2` yields

\[
\frac{1}{X^2}
\int_0^1|F_X(\alpha)|^4\,d\alpha
\ge
N^{-7/2}x^{9c-o(1)}.
\tag{32}
\]

Under (4), the right-hand side is

\[
N^{9c\lambda-7/2-o(1)}.
\tag{33}
\]

It grows by a fixed power precisely when

\[
9c\lambda-\frac72>0,
\tag{34}
\]

which is the threshold (13).

The lower bound (11) itself is valid throughout the wider FD-304 regime (5). What changes at (13) is its interpretation: below that second threshold it need not exceed `X^2` by a power, while above it the fourth moment is forced into a genuinely inflated regime.

## 3. A fourth-moment inflation forces one additive spectral spike

The second moment is exact:

\[
\int_0^1|F_X(\alpha)|^2\,d\alpha
=
\sum_n|f_X(n)|^2
\le X.
\tag{35}
\]

Since

\[
|F_X(\alpha)|^4
\le
\|F_X\|_\infty^2|F_X(\alpha)|^2,
\tag{36}
\]

integration gives

\[
\|F_X\|_\infty^2
\ge
\frac{
\int_0^1|F_X(\alpha)|^4\,d\alpha
}{
\int_0^1|F_X(\alpha)|^2\,d\alpha
}.
\tag{37}
\]

Substituting (11) and (35),

\[
\|F_X\|_\infty^2
\ge
Q N^{-5/2}x^{9c-o(1)},
\tag{38}
\]

which proves (15). Dividing its square root by

\[
X^{1/2}=N^{1/2}Q^{1/2}
\tag{39}
\]

gives (16). In the polynomial-depth scaling,

\[
\frac{\|F_X\|_\infty}{X^{1/2}}
\ge
N^{(9c\lambda/2)-7/4-o(1)}.
\tag{40}
\]

Thus (13) is simultaneously the threshold at which the fourth moment becomes power-larger than `X^2` and the threshold at which a Möbius additive Fourier coefficient is forced power-larger than square-root size.

At `\lambda=1`, the two excess exponents are respectively

\[
9c-\frac72
=0.2353374935\ldots
\tag{41}
\]

and

\[
\frac{9c}{2}-\frac74
=0.1176687467\ldots .
\tag{42}
\]

This additive-frequency formulation is strictly more compressed than retaining the entire family of shifts: a capacity-scale Farey obstruction now implies the existence of one frequency at which a single length-`X` Möbius exponential sum is anomalously large relative to square-root scale in the range (13).

## 4. Prior-art boundary and adversarial review

A fresh prior-art check included averaged Chowla results of Matomäki--Radziwiłł--Tao, short-interval multiplicative-function work, and classical Möbius exponential-sum bounds. None is imported as a load-bearing theorem here. The present statement is a deterministic Fourier consequence of the already-proved FD-304 family: once the common-window correlations are available, (22), (29), and Parseval give the compression exactly. Therefore no new `SOURCES.md` entry is required.

This finding also does **not** contradict Davenport-type uniform estimates for

\[
\sum_{n\le X}\mu(n)e(n\alpha).
\tag{43}
\]

Bounds of size `X(log X)^{-A}` for arbitrary fixed `A` remain much larger than the power-above-square-root coefficient forced by (15) in the current parameter range. The useful change is structural, not a contradiction with known linear exponential-sum technology: the Farey route has been reduced from many positive correlations to a single source-selected additive frequency.

The adversarial checks are as follows. First, the fixed-window-to-compact-autocorrelation trim costs at most `h<=N`, and (5) makes that cost polynomially negligible compared with every selected correlation by (24)--(26). Second, FD-304 already supplies distinct shifts, so (31) does not double-count one autocorrelation. Third, the Fourier identity is exact and uses one fixed compact vector `f_X`; there is no hidden moving endpoint after (21). Fourth, the claim of power-sized fourth-moment inflation is made only above (13), not throughout the wider regime (5). Fifth, `\alpha_*` is unrestricted and may depend on `(N,x,Q)`; no major-arc, minor-arc, rational-denominator, or stability statement is asserted. Sixth, RH enters only through the FD-304 input and shell floor; the Fourier compression itself is deterministic. Finally, the implication is one-way: a large fourth moment or a large Fourier coefficient by itself does not recover the population, positivity, or common-window structure of the FD-304 correlations.

## 5. Consequence for the Farey route

FD-300 converted near-capacity divisor-convolved variation into a high-energy block-Mertens shell. FD-303 converted that shell into many positive untwisted Möbius correlations, and FD-304 removed their moving-start freedom under RH. The present finding removes another degree of freedom: **the whole common-window family must leave a detectable fourth-moment footprint in one fixed Möbius block, and above (13) it must generate an additive Fourier coefficient power-larger than square-root scale.**

This changes the next obstruction test. Instead of attacking all selected shifts independently, one may try to rule out the forced spectral concentration by controlling

\[
\int_0^1
\left|
\sum_{X\le n<2X}\mu(n)e(n\alpha)
\right|^4d\alpha
\tag{44}
\]

at the source-selected scales `X=NQ`, or by proving a sufficiently strong uniform pointwise bound for the same block Fourier transform. Either route would kill the entire common-window family at once.

The required estimates are substantially stronger than the classical logarithmic savings currently used for linear Möbius exponential sums. Thus FD-305 is a route reduction rather than a closure: it identifies a compact additive-spectral certificate whose exclusion would rule out near-capacity block-Mertens variation, but it does not yet exclude that certificate.

## Bottom line

Under RH, once `lambda>3/(10c)`, the capacity-scale Farey route of FD-304 forces the exact fourth-moment lower bound

\[
\int_0^1|F_X(\alpha)|^4\,d\alpha
\ge
Q^2N^{-3/2}x^{9c-o(1)}.
\tag{45}
\]

Above

\[
\lambda>\frac{7}{18c}=0.9369969932\ldots,
\tag{46}
\]

this is a power above `X^2`, and one additive Möbius Fourier coefficient is consequently a power above `X^{1/2}`. At balanced depth `lambda=1`, the forced excess exponents are `0.2353374935...` in the fourth moment and `0.1176687467...` in the maximal Fourier coefficient relative to square-root scale. The surviving frontier is therefore no longer only a many-shift Chowla-type family: it has an equivalent one-block additive-spectral certificate that can be targeted globally.