# NB-313 — external dilation retains a square-root anchored correlation channel

- **Date:** 2026-09-23
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-290, NB-303, NB-312
- **Classification:** `EXACT-DERIVED + CANONICAL-NYMAN-SOURCE + PROJECTED-DILATION + EXTERNAL-DILATION + EXPLICIT-CORRELATION-CHANNEL + SQUARE-ROOT-FLOOR + FIXED-RATIO-ASYMPTOTIC + NON-TARGET-AWARE + PRIOR-ART-AUDITED`

## Claim

Let

\[
U_N:=\operatorname{span}\{g_2,\ldots,g_N\},
\qquad
T_{N,m}:=P_{U_N}A_m|_{U_N},
\qquad
\beta_{N+1}(m):=\|T_{N,m}\|,
\]

with the normalized integer dilation `A_m` from `NB-290`. Put

\[
C_*:=1+\frac{\pi^2}{6},
\qquad
c_{\rm ext}:=
\frac{1}{32\sqrt{\log 2\,C_*}}
=0.0230796\ldots.
\]

Then for every integer pair

\[
N\ge32,
\qquad
m\ge N,
\]

one has the explicit external-dilation lower bound

\[
\boxed{
\beta_{N+1}(m)
\ge
c_{\rm ext}\sqrt{\frac Nm}.
}
\tag{1}
\]

Consequently, for every moving family with `N_X -> infinity`,

\[
\boxed{
\beta_{N_X+1}(m_X)\to0
\quad\Longrightarrow\quad
\frac{m_X}{N_X}\to\infty.
}
\tag{2}
\]

Indeed `NB-312` already prevents decay when `m_X<=N_X`, while (1) prevents decay on every bounded external linear strip `N_X<m_X<=L N_X`.

There is also a sharper fixed-ratio profile. If

\[
N\to\infty,
\qquad
\frac{m_N}{N}\to\lambda\in[1,\infty),
\]

define

\[
J(\lambda)
:=
\int_0^1 g_2(y)
\left\{\frac{\lambda}{y}\right\}\,dy.
\tag{3}
\]

Then `J(lambda)>0`, in fact `J(lambda)>=1/32`, and

\[
\boxed{
\liminf_{N\to\infty}\beta_{N+1}(m_N)
\ge
B(\lambda)
:=
\frac{2J(\lambda)}
{\sqrt{\lambda\log2\,(\log(2\pi)-\gamma)}}
>0.
}
\tag{4}
\]

At `lambda=1`, this anchored profile recovers the limiting constant from `NB-312`.

## 1. Move the external correlation back to the unit interval

For the canonical generator

\[
g_j(x)
=
\left\{\frac{1}{jx}\right\}
-\frac1j\left\{\frac1x\right\},
\tag{5}
\]

the normalized dilation is

\[
(A_m f)(x)
=
\begin{cases}
\sqrt m\,f(mx), & 0<x\le1/m,\\
0, & 1/m<x\le1.
\end{cases}
\tag{6}
\]

Take the fixed source anchor `g_2` and, even when `m>N`, test its dilate against the **edge generator** `g_N`, which remains available in `U_N`. A change of variable `y=mx` gives

\[
\sqrt m\,\langle A_mg_2,g_N\rangle
=
\int_0^1 g_2(y)\,g_N(y/m)\,dy.
\tag{7}
\]

Writing

\[
\lambda:=\frac mN\ge1,
\]

equation (5) yields the exact decomposition

\[
g_N(y/m)
=
\left\{\frac{\lambda}{y}\right\}
-\frac1N\left\{\frac{m}{y}\right\}.
\tag{8}
\]

Thus

\[
\sqrt m\,\langle A_mg_2,g_N\rangle
=
\int_0^1
g_2(y)\left\{\frac{\lambda}{y}\right\}\,dy
-
\frac1N
\int_0^1
g_2(y)\left\{\frac{m}{y}\right\}\,dy.
\tag{9}
\]

The first term is the macroscopic channel. The second is only the finite-`N` correction coming from the canonical neutralization term in `g_N`.

## 2. The first reciprocal shell already gives a universal floor

On the first reciprocal shell

\[
\frac12<y\le1,
\]

one has `g_2(y)=1/2`. Therefore, with `t=1/y`,

\[
\begin{aligned}
J(\lambda)
&:=
\int_0^1
g_2(y)\left\{\frac{\lambda}{y}\right\}\,dy\\
&\ge
\frac12
\int_{1/2}^{1}
\left\{\frac{\lambda}{y}\right\}\,dy\\
&=
\frac12
\int_1^2
\frac{\{\lambda t\}}{t^2}\,dt\\
&\ge
\frac18
\int_1^2
\{\lambda t\}\,dt\\
&=
\frac{1}{8\lambda}
\int_\lambda^{2\lambda}
\{u\}\,du.
\end{aligned}
\tag{10}
\]

For any interval of length `L>=1`, periodicity of the fractional-part function gives

\[
\int_a^{a+L}\{u\}\,du
\ge
\frac{\lfloor L\rfloor}{2}
\ge
\frac L4.
\tag{11}
\]

The first inequality simply retains `floor(L)` consecutive unit-length pieces, each of integral `1/2`, and discards the nonnegative remainder. The second uses `floor(L)>=L/2` for `L>=1`. Applying (11) with `L=lambda` gives

\[
\boxed{
J(\lambda)\ge\frac1{32}
\qquad(\lambda\ge1).
}
\tag{12}
\]

For the correction term in (9), use `0<=g_2<=1/2` and the fact that every fractional part lies in `[0,1)`:

\[
0
\le
\frac1N
\int_0^1
g_2(y)\left\{\frac{m}{y}\right\}\,dy
\le
\frac1{2N}.
\tag{13}
\]

Hence

\[
\boxed{
\sqrt m\,\langle A_mg_2,g_N\rangle
\ge
\frac1{32}-\frac1{2N}
\ge
\frac1{64}
}
\tag{14}
\]

whenever `N>=32` and `m>=N`. In particular this cross-correlation is positive throughout the external region, even though the natural in-section probe `g_m` used by `NB-312` has already left `U_N`.

## 3. Normalize by the edge-generator scale

`NB-312` records the exact anchor norm

\[
\|g_2\|_2^2=\frac{\log2}{4}
\tag{15}
\]

and the elementary uniform generator bound

\[
\|g_N\|_2^2
\le
\frac{1+\pi^2/6}{N}
=
\frac{C_*}{N}.
\tag{16}
\]

Since \(g_2,g_N\in U_N\),

\[
\begin{aligned}
\beta_{N+1}(m)
&\ge
\frac{\|P_{U_N}A_mg_2\|_2}{\|g_2\|_2}\\
&\ge
\frac{|\langle A_mg_2,g_N\rangle|}
{\|g_2\|_2\,\|g_N\|_2}.
\end{aligned}
\tag{17}
\]

Combining (14)--(17) gives

\[
\beta_{N+1}(m)
\ge
\frac{1}{32\sqrt{\log2\,C_*}}
\sqrt{\frac Nm},
\]

which is (1).

This is deliberately a one-channel lower certificate, not an estimate of the full singular spectrum. Its importance is the scaling: **external dilation cannot erase all finite-section overlap while `m/N` remains bounded**.

## 4. Fixed linear ratios have a positive limiting channel

Let `m_N/N -> lambda>=1`. Equation (9) gives

\[
\sqrt{m_N}\,
\langle A_{m_N}g_2,g_N\rangle
=
\int_0^1
g_2(y)
\left\{\frac{m_N/N}{y}\right\}\,dy
+o(1).
\tag{18}
\]

For almost every `y`, the fractional part in (18) converges to `{lambda/y}`; the exceptional points `y=lambda/k` are countable. Dominated convergence therefore yields

\[
\boxed{
\sqrt{m_N}\,
\langle A_{m_N}g_2,g_N\rangle
\longrightarrow
J(\lambda).
}
\tag{19}
\]

The generator norm asymptotic already derived in `NB-312` is

\[
N\|g_N\|_2^2
\longrightarrow
\log(2\pi)-\gamma.
\tag{20}
\]

Using (15), (17), (19), and (20) gives (4). The lower bound (12) makes positivity completely explicit.

For `lambda=1`, one has

\[
J(1)=\frac{\log\pi-\gamma}{4},
\]

so (4) becomes exactly the asymptotic anchored coefficient of `NB-312`,

\[
\frac{\log\pi-\gamma}
{2\sqrt{\log2\,(\log(2\pi)-\gamma)}}.
\]

Thus `NB-312` is the boundary value of a whole family of nonvanishing anchored channels extending outside the finite section.

## 5. What this changes in the source-side transition

Before this finding, the current source-side picture was

\[
m\le N
\quad\Longrightarrow\quad
\beta_{N+1}(m)\not\to0
\]

from `NB-312`, while `NB-303` only forced

\[
\frac{m}{N^2}\to\infty
\quad\Longrightarrow\quad
\beta_{N+1}(m)\to0.
\]

The external region beginning immediately at `m>N` was therefore open even at a fixed ratio such as `m=2N`.

Equation (1) removes that possibility. If a moving family with `N->infinity` has `beta->0` and `m/N` does **not** tend to infinity, then some subsequence has `m/N<=L`. On the internal part `m<=N`, `NB-312` gives a fixed positive floor. On the external part `N<m<=LN`, (1) gives

\[
\beta_{N+1}(m)
\ge
\frac{c_{\rm ext}}{\sqrt L}>0,
\]

again a contradiction. Hence (2).

The source-side decay frontier is therefore no longer merely "external versus internal." A vanishing projected-dilation norm requires a **genuinely superlinear dilation scale**

\[
N\ll m.
\]

The sufficient theorem from `NB-303` remains genuinely superquadratic,

\[
N^2\ll m
\quad\Longrightarrow\quad
\beta_{N+1}(m)\to0.
\]

So the unresolved source-side decay transition is now squeezed between the necessary superlinear condition and the sufficient superquadratic condition. The quantitative floor (1) also survives into that window, but decays like `sqrt(N/m)` and therefore does not by itself rule out `beta->0` once `m/N->infinity`.

## 6. Boundary, target caveat, and prior-art audit

This remains a **source-side operator statement**. It does not say that the top singular vector is occupied by the moving first-free Ford datum, does not improve the ordinary Nyman distance directly, and does not address off-critical sample conditioning. The accepted target-aware and visible-semigroup-defect clues remain untouched.

A fresh prior-art audit checked the nearby integer-dilation, multiplicative-autocorrelation, and Gram literature represented by Báez-Duarte, Balazard--Martin, Ehm, Alouges--Darses--Hillion, and Carvill. The reviewed material contains the classical integer-dilation framework, fractional-part autocorrelation machinery, and Nyman--Beurling Gram structure, but did not expose this exact finite-section external certificate

\[
\beta_{N+1}(m)\gtrsim\sqrt{N/m}
\]

obtained from the fixed source anchor `g_2` and moving edge probe `g_N`. This is an audit result, not a novelty claim.

No external quantitative theorem is load-bearing. The proof uses the canonical generator identity and dilation setup already established internally, plus periodicity of the fractional-part function and the generator norm bound from `NB-312`. No `SOURCES.md` update is required.

## Validation

- The lower bound `J(lambda)>=1/32` was derived without asymptotics from only the first reciprocal shell and the unit-period integral of the fractional-part function.
- The finite-`N` correction in (9) is uniformly at most `1/(2N)`, so the sign and `m^{-1/2}` scale in (14) are stable throughout all `m>=N` once `N>=32`.
- Direct truncated reciprocal-shell evaluation for representative pairs `(N,m)=(32,32),(32,39),(32,64),(50,250),(100,500)` is positive and comfortably above the crude bound in (14).
- The fixed-ratio limit was checked numerically for several ratios `lambda=1,1.1,1.5,2,3,5,10`; the scaled correlation converges to the positive integral `J(lambda)`.
- The result is compatible with `NB-303`: when `m/N^2->infinity`, the lower floor `sqrt(N/m)` itself tends to zero.
- No clue is consumed, and no target-aware claim is made.
