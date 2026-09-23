# NB-304 — scaled adjacent cancellations make quadratic shell localization power-sharp

**Date:** 2026-09-23

**Status:** `EXACT-DERIVED + SOURCE-SIDE + MOVING-CUTOFF + SHARPNESS-CONTROL + METHOD-BOUNDARY + NON-TARGET-AWARE`.

`NB-303` proves the uniform source-localization estimate

\[
\Lambda_N(m)
:=
\sup_{0\ne u\in U_N}
\frac{\|1_{(0,1/m]}u\|_2^2}{\|u\|_2^2}
\le
\min\left\{
1,
\frac{10N^2}{m}+
\frac{20N^4}{3m^2}
\right\},
\qquad
U_N:=\operatorname{span}\{g_2,\ldots,g_N\},
\]

and hence `m/N^2 -> infinity` forces `Lambda_N(m)->0`. The exponent `2` is not merely an artifact of the separated-frequency large-sieve proof. It is **power-sharp for every argument that first tries to make the whole old source section small on `(0,1/m]`**.

For `N>=3`, define the scaled adjacent cancellation

\[
\boxed{
 u_N
 :=
 g_N-rac{N-1}{N}g_{N-1}.
}
\tag{1}
\]

On the reciprocal shell `I_k=(1/(k+1),1/k]`, this vector has the exact value

\[
\boxed{
 u_{N,k}
 =
 \frac{N-1}{N}
 \left\lfloor\frac{k}{N-1}\right\rfloor
 -
 \left\lfloor\frac{k}{N}\right\rfloor.
}
\tag{2}
\]

The linear `k/N` part has cancelled completely. The remaining floor defect is periodic with period

\[
L_N=N(N-1),
\]

and its energy is spread logarithmically across shell blocks from depth `N` out to depth `N^2`.

The resulting quantitative obstruction is:

\[
\boxed{
\text{for every fixed }0<\eta<1,
\quad
m_N:=\lceil N^{2-\eta}\rceil
\quad\Longrightarrow\quad
\liminf_{N\to\infty}\Lambda_N(m_N)
\ge
\frac{\eta}{8}.
}
\tag{3}
\]

Consequently, for every exponent `p<2`, there are cutoffs `m_N` with

\[
\frac{m_N}{N^p}\to\infty
\]

but

\[
\Lambda_N(m_N)\not\to0.
\]

Thus no universal tail-support theorem of the form

\[
m/N^p\to\infty
\Longrightarrow
\sup_{u\in U_N\setminus\{0\}}
\frac{\|1_{(0,1/m]}u\|_2}{\|u\|_2}	o0
\]

can hold for any fixed `p<2`.

The same witness also shows that the `N^2` separated-frequency frame scale in `NB-303` cannot be replaced by a smaller fixed power. If `Q_N(u)` denotes its Cesaro shell energy, then

\[
\boxed{
\liminf_{N\to\infty}
\frac{\log N}{N^2}
\sup_{0\ne u\in U_N}
\frac{Q_N(u)}{\|u\|_2^2}
\ge
\frac1{12}.
}
\tag{4}
\]

So the large-sieve upper bound `Q_N(u)=O(N^2||u||^2)` is power-sharp, with only a logarithmic gap left by this explicit two-generator witness.

This does **not** prove that the projected-dilation overlap `beta_(N+1)(m)` itself has a quadratic threshold. `NB-303` bounds `beta` by source-tail concentration, but the reverse implication need not hold because projection onto `U_N` can destroy a large supported tail. The result is therefore a sharp boundary for the *generic support-localization route*, not an optimality theorem for projected dilation, first-free sampling, or the Nyman distance.

## 1. Exact shell formula for the scaled adjacent defect

Use the canonical Bagchi generators

\[
g_j(x)
=
\left\{\frac1{jx}\right\}
-
\frac1j\left\{\frac1x\right\}.
\]

As in `NB-301`--`NB-303`, on `I_k` one has

\[
g_j|_{I_k}=r_j(k),
\qquad
r_j(k)=\frac{k\bmod j}{j}
=
\frac{k}{j}-\left\lfloor\frac{k}{j}\right\rfloor.
\tag{5}
\]

Insert (5) into (1):

\[
\begin{aligned}
u_{N,k}
&=
\frac{k}{N}
-
\left\lfloor\frac{k}{N}\right\rfloor
-
\frac{N-1}{N}
\left(
\frac{k}{N-1}
-
\left\lfloor\frac{k}{N-1}\right\rfloor
\right)\\
&=
\frac{N-1}{N}
\left\lfloor\frac{k}{N-1}\right\rfloor
-
\left\lfloor\frac{k}{N}\right\rfloor,
\end{aligned}
\]

which proves (2). Since the two original shell sequences have coprime periods `N` and `N-1`, `u_(N,k)` is `L_N=N(N-1)` periodic.

Inside the first period, write

\[
k=aN+r,
\qquad
0\le a\le N-2,
\qquad
0\le r<N.
\tag{6}
\]

Then

\[
\left\lfloor\frac{k}{N}\right\rfloor=a
\]

and

\[
\left\lfloor\frac{k}{N-1}\right\rfloor
=
 a+
 \mathbf 1_{\{r\ge N-1-a\}}.
\]

Therefore

\[
\boxed{
 u_{N,aN+r}
 =
 \begin{cases}
 -a/N,&0\le r<N-1-a,\\[2mm]
 (N-1-a)/N,&N-1-a\le r<N.
 \end{cases}
}
\tag{7}
\]

The second branch contains exactly `a+1` shells. These are the sparse order-one spikes that transport source norm through the whole interval of reciprocal depths `N << k << N^2`.

## 2. The witness has only logarithmic-over-quadratic total norm

The exact Nyman source norm is

\[
\|u_N\|_2^2
=
\sum_{k\ge1}
\frac{|u_{N,k}|^2}{k(k+1)}.
\tag{8}
\]

For a block `a>=1`, let

\[
S_a
:=
\sum_{r=0}^{N-1}
|u_{N,aN+r}|^2.
\]

Equation (7) gives

\[
S_a
=
\frac{
(N-1-a)a^2
+(a+1)(N-1-a)^2
}{N^2}.
\tag{9}
\]

A direct simplification shows

\[
(a+1)-S_a
=
\frac{
(N-2)a^2+(4N-3)a+(2N-1)
}{N^2}
>0,
\]

hence

\[
\boxed{S_a\le a+1.}
\tag{10}
\]

For `k` in the `a`-th block, `k>=aN`, so

\[
\sum_{r=0}^{N-1}
\frac{|u_{N,aN+r}|^2}
{(aN+r)(aN+r+1)}
\le
\frac{a+1}{a^2N^2}
\le
\frac2{aN^2}.
\tag{11}
\]

The block `a=0` has only one nonzero shell, at `k=N-1`, and contributes

\[
\frac{N-1}{N^3}
\le
\frac1{N^2}.
\tag{12}
\]

Thus the first full period contributes at most

\[
\frac{1+2H_{N-2}}{N^2}.
\tag{13}
\]

The later periods are harmless. Let `Q_N(u_N)` be the mean square over one period. Each complete period contains square mass `L_N Q_N(u_N)`. For the period with index `q>=1`, every shell has `k>qL_N`, so its weighted contribution is at most

\[
\frac{Q_N(u_N)}{q^2L_N}.
\]

Summing in `q`, using `Q_N(u_N)<=1/6` below and `L_N>=N^2/2`, gives

\[
\sum_{k>L_N}
\frac{|u_{N,k}|^2}{k(k+1)}
\le
\frac{\pi^2}{18N^2}.
\tag{14}
\]

Combining (13) and (14),

\[
\boxed{
\|u_N\|_2^2
\le
\frac{
2H_{N-2}+1+\pi^2/18
}{N^2}.
}
\tag{15}
\]

This is consistent with the adjacent-cancellation phenomenon isolated in `NB-025`, but (7) gives the additional information needed here: the small norm is not concentrated near the first active shell. Its spike contribution is distributed harmonically over the whole first `N(N-1)`-period.

## 3. Subquadratic cutoffs retain a fixed fraction of the source norm

Fix `0<eta<1` and set

\[
m_N=\lceil N^{2-\eta}\rceil,
\qquad
A_N=\left\lceil\frac{m_N}{N}\right\rceil,
\qquad
B_N=\left\lfloor\frac{N-2}{2}\right\rfloor.
\tag{16}
\]

For all sufficiently large `N`, `A_N<=B_N`. Consider a block

\[
A_N\le a\le B_N.
\]

Every shell in that block lies beyond the cutoff because `aN>=m_N`. In the upper branch of (7) there are `a+1` shells and

\[
\frac{N-1-a}{N}
\ge
\frac12.
\tag{17}
\]

Those shells also satisfy

\[
k<(a+1)N,
\]

so

\[
\frac1{k(k+1)}
>
\frac1{(a+1)^2N^2}.
\tag{18}
\]

Therefore the contribution of just the upper branch of block `a` to the tail norm is at least

\[
(a+1)
\frac14
\frac1{(a+1)^2N^2}
=
\frac1{4(a+1)N^2}.
\tag{19}
\]

Summing (19),

\[
\boxed{
\|1_{(0,1/m_N]}u_N\|_2^2
\ge
\frac1{4N^2}
\sum_{a=A_N}^{B_N}
\frac1{a+1}.
}
\tag{20}
\]

Now

\[
\sum_{a=A_N}^{B_N}\frac1{a+1}
=
\eta\log N+O(1),
\tag{21}
\]

whereas

\[
2H_{N-2}+1+\pi^2/18
=
2\log N+O(1).
\tag{22}
\]

Dividing (20) by (15) yields

\[
\liminf_{N\to\infty}
\frac{
\|1_{(0,1/m_N]}u_N\|_2^2
}{
\|u_N\|_2^2
}
\ge
\frac{\eta}{8}.
\tag{23}
\]

Since `u_N in U_N`, (23) proves (3).

To state the power-sharpness consequence explicitly, suppose `p<2`. Choose any `q` with

\[
p<q<2
\]

and put `m_N=ceil(N^q)`. Then

\[
\frac{m_N}{N^p}\to\infty,
\]

while (3), with `eta=2-q`, gives

\[
\liminf_{N\to\infty}\Lambda_N(m_N)
\ge
\frac{2-q}{8}>0.
\tag{24}
\]

So no fixed exponent below `2` can replace the quadratic scale in a universal support-localization criterion.

The argument deliberately leaves open logarithmic improvements at the quadratic endpoint. For example, this witness alone does not rule out a threshold such as `N^2/log N`, nor any other `N^(2-o(1))` refinement. Its conclusion is exactly power-sharpness, not full asymptotic optimality.

## 4. The same vector nearly saturates the `N^2` shell-frame scale

The exact Cesaro shell energy of `u_N` can be computed without estimates. Over the period `L_N`, the residues modulo `N` and `N-1` are independent because the moduli are coprime. For

\[
r_j(k)=\frac{k\bmod j}{j},
\]

one has

\[
\mathbb E r_j
=
\frac{j-1}{2j},
\qquad
\mathbb E r_j^2
=
\frac{(j-1)(2j-1)}{6j^2}.
\tag{25}
\]

Since

\[
u_N=r_N-\frac{N-1}{N}r_{N-1},
\]

independence over the complete period gives

\[
\boxed{
Q_N(u_N)
=
\frac{N^2-N+1}{6N^2}.
}
\tag{26}
\]

In particular `Q_N(u_N)->1/6`. Combining (26) with (15),

\[
\frac{Q_N(u_N)}{\|u_N\|_2^2}
\ge
\frac{N^2-N+1}
{6\left(2H_{N-2}+1+\pi^2/18\right)}.
\tag{27}
\]

Hence

\[
\boxed{
\liminf_{N\to\infty}
\frac{\log N}{N^2}
\frac{Q_N(u_N)}{\|u_N\|_2^2}
\ge
\frac1{12},
}
\tag{28}
\]

which proves (4). Thus the `O(N^2)` source-frame constant obtained from Farey separation in `NB-303` is already correct at the level of polynomial exponent. Improving it to `O(N^(2-epsilon))` for any fixed `epsilon>0` is impossible for the full canonical section.

This also explains why the Farey `N^{-2}` separation in `NB-303` was not merely an unnecessarily pessimistic generic-frequency scale. The canonical Nyman section contains a two-generator vector whose shell mean-square remains order one while its weighted Hilbert norm is only logarithmic-over-quadratic.

## 5. What this does and does not sharpen after NB-303

The implication of `NB-303`

\[
\Lambda_N(m)\to0
\quad\Longrightarrow\quad
\beta_{N+1}(m)\to0
\]

uses only the support of the normalized dilation: `S_m v` is contained in `(0,1/m]`. `NB-304` shows that this first step cannot be improved to a subquadratic fixed power uniformly over `U_N`. A continuation that still tries to prove

\[
\sup_{u\in U_N}
\|1_{(0,1/m]}u\|/\|u\|
\to0
\]

must therefore remain at the quadratic endpoint, perhaps gaining logarithms but not a smaller power.

There are nevertheless three major escape routes, none closed here. First, `beta` is a *projected dilation* norm, not a tail-support norm. Large mass of `u_N` beyond shell `m` need not correlate with any vector of the form `S_m v` strongly enough to survive projection back to `U_N`. Second, the first-free compression matrix `Xi` also contains the off-critical sample multiplier and destination sampling geometry. Third, the Ford target may occupy only a much smaller part of any surviving source sector.

Accordingly, (3) is not a lower bound for `beta`, `Xi`, the target gain, the finite-section excess, or the Nyman distance. It does not challenge the super-quadratic no-go region already proved by `NB-303`; it says that **generic source support alone cannot push that region below quadratic power**.

The clean next question is therefore not another universal shell-tail estimate with exponent `<2`. It is whether the extra structure discarded by the Cauchy--Schwarz support step—especially the actual correlation

\[
\langle u,S_mv\rangle
\]

and the first-free sample map—produces additional cancellation in the near/sub-quadratic regime. That is a genuinely stronger object than source localization.

## 6. Adversarial checks

The witness is an actual two-generator vector of the canonical discrete Nyman section; no enlarged periodic model or arbitrary Farey polynomial is introduced. The coefficient `(N-1)/N` is essential only because it cancels the linear shell drift exactly and exposes the floor defect (2).

The lower tail estimate uses the actual weighted `L^2(0,1)` norm, not coefficient norm, Cesaro norm, or an unweighted shell count. Every retained block lies beyond the declared moving cutoff and every lower bound is taken on explicit shells of the exact source vector.

The periodic tail after `L_N` is used only for the **upper** bound on total norm. Omitting it would make the denominator too small and could invalidate the tail fraction. Equation (14) accounts for all later periods.

The constant `eta/8` is intentionally nonoptimal. Only a positive cutoff-uniform fraction matters. The proof is stable under harmless endpoint rounding in `m_N`, `A_N`, and `B_N`.

The result does not reverse the support estimate used in `NB-303`. A large value of `Lambda_N(m)` does not force large projected-dilation overlap. Treating (3) as a lower bound for `beta` would be an invalid converse and is explicitly excluded.

Finally, no zeta-zero information, RH assumption, target coefficient, or first-free interpolation hypothesis enters the construction. This is a source-side sharpness control only.

## 7. Prior-art boundary

The local closeness of neighboring fractional-part dilations is classical territory. Báez-Duarte--Balazard--Landreau--Saias study the multiplicative fractional-part structure underlying Nyman--Beurling, Balazard--Martin (`arXiv:1305.4395`) analyze local regularity of the multiplicative autocorrelation, and Ehm (`arXiv:2405.06349`) gives modern exact Gram formulae and decompositions. `NB-025` already records this literature boundary and derives an explicit adjacent canonical near-null mode with norm `O(log n/n^2)` and vanishing target angle. No novelty is claimed for adjacent-generator closeness itself.

The line-local delta here is different and narrower: the scaled adjacent vector (1) has the exact shell floor form (2), which exposes a logarithmically distributed sequence of order-one spike blocks through reciprocal depth `N^2`. Equations (3) and (24) turn that distribution into a **power-sharpness theorem for the universal shell-localization step used by `NB-303`**, while (28) gives a matching polynomial lower scale for its Cesaro shell-frame constant. A targeted search of the adjacent-autocorrelation, Gram-formula, and recent Nyman Gram-compressibility literature did not locate this exact moving-cutoff tail-retention statement. Search absence is not a priority claim.

No specialized external estimate is load-bearing in the proof. The argument uses only the canonical shell identity, elementary harmonic summation, coprime-period averaging, and the definitions already established in the local line. `SOURCES.md` therefore requires no update.

## Research consequence

`NB-300`--`NB-303` progressively moved the generic projected-dilation source-compression sufficient scale from exponential to cubic, five-halves, and finally quadratic. `NB-304` supplies the missing adversarial control on that progression: **quadratic is the first exponent that a universal source-support argument can possibly reach.**

This does not certify that the true projected-dilation threshold is quadratic. Instead it separates two questions that were still conflated after `NB-303`. The support-localization problem is now power-sharp and should not be attacked by another fixed-power improvement. Any further polynomial gain must exploit structure beyond support—projected correlation, destination sampling, target occupation, or another source relation not dominated by `Lambda_N(m)`.

That narrows the live near/sub-quadratic frontier without making a target-aware claim: the next useful estimate has to see more than where the old source section stores its norm.