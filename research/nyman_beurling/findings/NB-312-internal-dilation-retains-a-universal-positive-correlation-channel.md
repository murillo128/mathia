# NB-312 — internal dilation retains a universal positive correlation channel

- **Date:** 2026-09-23
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-290, NB-303, NB-306, NB-311
- **Classification:** `EXACT-DERIVED + CANONICAL-NYMAN-SOURCE + RECIPROCAL-SHELLS + PROJECTED-DILATION + INTERNAL-DILATION + EXPLICIT-CORRELATION-CHANNEL + UNIVERSAL-POSITIVE-FLOOR + ASYMPTOTIC-CONSTANT + NON-TARGET-AWARE + PRIOR-ART-AUDITED`

## Claim

Let

\[
U_N:=\operatorname{span}\{g_2,\ldots,g_N\},
\qquad
T_{N,m}:=P_{U_N}A_m|_{U_N},
\qquad
\beta_{N+1}(m):=\|T_{N,m}\|,
\]

where `A_m` is the normalized integer dilation from `NB-290`. For every integer pair

\[
2\le m\le N,
\]

define the anchored correlation coefficient

\[
\rho_m:=
\frac{\langle A_m g_2,g_m\rangle}
{\|g_2\|_2\,\|g_m\|_2}.
\]

Then

\[
\boxed{\beta_{N+1}(m)\ge \rho_m>0.}
\tag{1}
\]

Moreover the channel is uniformly non-degenerate. A completely explicit bound is

\[
\boxed{
\rho_m\ge
c_0:=
\frac{1}
{24\sqrt{\log 2\,\left(1+\pi^2/6\right)}}
>0.0307
\qquad (m\ge2).
}
\tag{2}
\]

The correlation has the sharper asymptotic

\[
\boxed{
\rho_m\longrightarrow
\rho_\infty:=
\frac{\log\pi-\gamma}
{2\sqrt{\log 2\,(\log(2\pi)-\gamma)}}
=
0.303553\ldots
}
\tag{3}
\]

as `m -> infinity`, where `gamma` is Euler's constant. Consequently, for every moving family with

\[
2\le m_X\le N_X,
\qquad
m_X\to\infty,
\]

one has

\[
\boxed{
\liminf_{X\to\infty}\beta_{N_X+1}(m_X)
\ge \rho_\infty.
}
\tag{4}
\]

Thus projected-dilation overlap cannot vanish anywhere in the entire **internal-dilation region** `m <= N`. The exact unit plateau of `NB-306` still ends at `2m=N`, and `NB-311` still controls how slowly the top singular value initially leaves `1`; the new statement is different: even deeper in the first linear strip, where near-isometry is unresolved, a fixed low generator `g_2` keeps a macroscopic correlation channel into the in-section generator `g_m`.

## 1. The anchored channel

The reciprocal-shell formula used throughout this line is

\[
g_j|_{I_k}=\frac{k\bmod j}{j},
\qquad
I_k:=\left(\frac1{k+1},\frac1k\right].
\tag{5}
\]

The exact covariance from `NB-290` gives

\[
A_m g_2
=
\sqrt m\left(g_{2m}-\frac12g_m\right).
\tag{6}
\]

Write

\[
k=qm+r,
\qquad
0\le r<m.
\]

Then

\[
g_m|_{I_k}=\frac rm,
\tag{7}
\]

while (6) and the remainder pattern modulo `2m` give the exact two-block rule

\[
(A_m g_2)|_{I_k}
=
\begin{cases}
0, & q\ \text{even},\\[1mm]
\sqrt m/2, & q\ \text{odd}.
\end{cases}
\tag{8}
\]

Every nonzero term in the shell expansion of
`\langle A_m g_2,g_m\rangle` is therefore positive.

Because `g_2,g_m\in U_N` whenever `m<=N`,

\[
\begin{aligned}
\beta_{N+1}(m)
&\ge
\frac{\|P_{U_N}A_mg_2\|_2}{\|g_2\|_2}\\
&\ge
\frac{|\langle A_mg_2,g_m\rangle|}
{\|g_2\|_2\|g_m\|_2}
=
\rho_m.
\end{aligned}
\tag{9}
\]

This proves (1). Notice that no conditioning estimate, canonical pivot, or target datum enters the argument.

## 2. A uniform positive floor

The exact norm of the anchor is already implicit in the first canonical pivot used in `NB-311`:

\[
\|g_2\|_2^2=\frac{\log2}{4}.
\tag{10}
\]

For general `m`, split the norm into reciprocal-shell blocks `k=qm+r`. On the initial block `q=0`,

\[
\sum_{r=1}^{m-1}
\frac{(r/m)^2}{r(r+1)}
\le \frac1m.
\]

For `q>=1`, use `0<=g_m<=1` and `k>=qm` to obtain

\[
\sum_{r=0}^{m-1}
\frac{|g_m(k)|^2}{k(k+1)}
\le
\frac{1}{q^2m}.
\]

Hence

\[
\boxed{
\|g_m\|_2^2
\le
\frac{1+\pi^2/6}{m}.
}
\tag{11}
\]

Now retain only the `q=1` block in the positive correlation sum and only the residues

\[
\lceil m/2\rceil\le r\le m-1.
\]

There are `floor(m/2) >= m/3` such residues. On them, (7)--(8) give

\[
(A_mg_2)(k)=\frac{\sqrt m}{2},
\qquad
g_m(k)\ge\frac12,
\]

and

\[
\frac1{k(k+1)}
\ge \frac1{4m^2}.
\]

Therefore

\[
\boxed{
\langle A_mg_2,g_m\rangle
\ge
\frac{1}{48\sqrt m}.
}
\tag{12}
\]

Combining (10)--(12) gives exactly (2). The constant is deliberately crude; its role is only to show that the internal channel is uniformly positive for every integer `m>=2`.

## 3. Exact asymptotic strength of the channel

The same shell formulas identify the limiting constant. First,

\[
\|g_m\|_2^2
=
\sum_{r=1}^{m-1}
\frac{(r/m)^2}{r(r+1)}
+
\sum_{q\ge1}\sum_{r=0}^{m-1}
\frac{(r/m)^2}
{(qm+r)(qm+r+1)}.
\tag{13}
\]

Put `x=r/m`, and define the missing `r=0` summand in the `q=0` block to be `0`. Multiplying by `m`, each fixed `q` block is then a Riemann sum:

\[
m\sum_{r=0}^{m-1}
\frac{(r/m)^2}
{(qm+r)(qm+r+1)}
=
\frac1m\sum_{r=0}^{m-1}
\frac{x^2}{(q+x)(q+x+1/m)}.
\tag{14}
\]

For `q=0` the summand is bounded by `1`; for `q>=1` it is bounded by `1/q^2`. Dominated convergence over the block index therefore gives

\[
m\|g_m\|_2^2
\longrightarrow
\sum_{q\ge0}
\int_0^1\frac{x^2}{(q+x)^2}\,dx.
\tag{15}
\]

The `q=0` integral is `1`, and for `q>=1`

\[
\int_0^1\frac{x^2}{(q+x)^2}\,dx
=
2-\frac1{q+1}-2q\log\left(1+\frac1q\right).
\tag{16}
\]

Summing (16) to `Q`, then using Stirling's formula and
`H_Q=log Q+gamma+o(1)`, yields

\[
\boxed{
m\|g_m\|_2^2
\longrightarrow
\log(2\pi)-\gamma.
}
\tag{17}
\]

For the correlation

\[
C_m:=\langle A_mg_2,g_m\rangle,
\]

only odd `q` blocks survive by (8). Thus

\[
C_m
=
\frac{\sqrt m}{2}
\sum_{\substack{q\ge1\\q\ {\rm odd}}}
\sum_{r=0}^{m-1}
\frac{r/m}
{(qm+r)(qm+r+1)}.
\tag{18}
\]

Again dominated convergence gives

\[
\sqrt m\,C_m
\longrightarrow
\frac12
\sum_{\substack{q\ge1\\q\ {\rm odd}}}
\int_0^1\frac{x}{(q+x)^2}\,dx.
\tag{19}
\]

For each `q>=1`,

\[
\int_0^1\frac{x}{(q+x)^2}\,dx
=
\log\left(1+\frac1q\right)-\frac1{q+1}.
\tag{20}
\]

Writing the odd indices as `q=2k+1`, the partial sum through
`k=n-1` is

\[
\log\frac{4^n}{\binom{2n}{n}}
-\frac12H_n.
\tag{21}
\]

The central-binomial asymptotic and the harmonic-number asymptotic give

\[
\sum_{\substack{q\ge1\\q\ {\rm odd}}}
\left[
\log\left(1+\frac1q\right)-\frac1{q+1}
\right]
=
\frac{\log\pi-\gamma}{2}.
\tag{22}
\]

Therefore

\[
\boxed{
\sqrt m\,C_m
\longrightarrow
\frac{\log\pi-\gamma}{4}.
}
\tag{23}
\]

Combining (10), (17), and (23) proves (3), and (4) follows from (1).

## 4. What this changes in the source-side transition

`NB-306` gives the exact plateau

\[
\beta_{N+1}(m)=1
\qquad\Longleftrightarrow\qquad
2m\le N.
\]

`NB-311` then proves that in the first post-core strip,
`m=N/2+o(N)`, the top singular value is still asymptotic to `1`.
The present result covers a different question. If `m` grows anywhere inside

\[
2\le m\le N,
\]

then even after the exact core has disappeared and even if the endpoint near-isometry from `NB-311` no longer applies,

\[
\liminf\beta_{N+1}(m)\ge 0.303553\ldots
\]

along every moving internal-dilation family. Thus an order-one gap below `1` may still develop deeper in the first strip, but **collapse of the projected-dilation norm to zero cannot occur before the dilation index itself exits the finite section**.

This relocates the first possible vanishing-overlap regime to `m>N`. It does not identify the true decay threshold there. The current upper theorem `NB-303` only forces full decay when `m/N^2 -> infinity`, so the broad external-dilation region

\[
N<m\lesssim N^2
\]

remains unresolved.

The mechanism is also structurally transparent. The source vector `g_2` is dilated to an alternating sequence of zero and constant reciprocal-shell blocks, while the in-section probe `g_m` is the positive sawtooth on each `m`-block. Their positive overlap survives at order `m^{-1/2}`, exactly the same scale as `\|g_m\|_2`, leaving a nonzero normalized correlation.

## 5. Boundary and target caveat

This is a **source-side operator statement**. The vector `g_m` is available as an in-section probe only because `m<=N`; once `m>N`, this particular certificate disappears. The theorem neither gives an asymptotic formula for `beta`, nor proves that `beta` stays near `1` for a fixed positive fraction past `N/2`, nor supplies a lower bound on the first post-core gap.

Most importantly, it does not solve target occupation. A strong correlation channel between `A_mg_2` and `g_m` may lie in a direction that the moving first-free Ford datum barely occupies. The accepted target-aware and visible-semigroup-defect clues therefore remain untouched.

## 6. Prior-art audit and dependency boundary

A fresh audit checked the nearby integer-dilation and Gram literature represented by Balazard/de Roton, Ehm, Alouges--Darses--Hillion, and Carvill. Those works are directly adjacent to integer dilations of the fractional-part family and to Nyman--Beurling Gram structure, but the reviewed material did not expose this exact finite-section `g_2 -> g_m` correlation certificate or the limiting constant in (3). This is an audit result, not a novelty claim.

No external quantitative theorem is load-bearing here. Equations (5)--(8) are internal canonical identities already established in this research line, and the remaining argument uses elementary Riemann sums, harmonic asymptotics, Stirling, and the central-binomial asymptotic. No `SOURCES.md` update is required.

## Validation

- The `q=1` shell block makes `C_m>0` explicit for every `m>=2`.
- The crude bounds (11)--(12) were checked independently against the exact shell sums; they preserve the correct `m^{-1/2}` scaling needed for a uniform normalized floor.
- Direct shell summation for representative values `m=2,3,5,10,20,50,100,200,500` agrees with (17), (23), and the limit (3).
- The result does not conflict with `NB-303`: that theorem's full-decay regime has `m/N^2 -> infinity`, hence eventually `m>N`, exactly outside the anchored certificate here.
- The result does not extend the exact plateau from `NB-306`; it only prevents the operator norm from vanishing after the plateau.
- No clue is consumed, and no target-aware claim is made.
