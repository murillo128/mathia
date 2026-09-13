# NB-104 — boundary confluence has an ordinate-delay Laguerre law

**Status:** `EXACT-DERIVED + NYMAN-FINITE-WINDOW-GRAM + BOUNDARY-DOUBLE-SCALING + ORDINATE-DELAY + INTERVAL-LAGUERRE-LAW + FIXED-MULTIPLICITY`.

`NB-103` identifies the fixed-multiplicity confluent Nyman volume coefficient, for a fixed interior center `lambda_*=a+i Gamma`, with the Laguerre moment determinant

\[
\Delta_d(2a\log q)
\]

up to a discrete error whose constant is allowed to depend on `lambda_*`. It explicitly leaves open the boundary regime `a -> 0`, where that error estimate is not uniform. The boundary limit has an additional scale that is invisible in the continuum half-line geometry: the zero ordinate compared with the discrete-cell scale.

Let

\[
\lambda_j=a_j+i\Gamma_j,
\qquad a_j\downarrow0,
\]

with fixed multiplicity `d`, integers `m_j>=1`, `q_j>=2`, and suppose

\[
x_j:=2a_j\log q_j\longrightarrow x\in(0,\infty).
\tag{1}
\]

Define the **ordinate delay**

\[
y_j:=2a_j\log^+\!\left(\frac{|\Gamma_j|}{m_j}\right),
\qquad
\log^+ t:=\max(\log t,0),
\tag{2}
\]

and assume `y_j -> y` in `[0,infinity]`. Then the analytic confluent continuation of the normalized finite-window state volume from `NB-103` satisfies

\[
\boxed{
\mathcal V^{\mathrm{conf}}_{d,m_j,q_j}(\lambda_j)
\longrightarrow
\begin{cases}
 e^{-dy}\,\Delta_d(x-y),&0\le y<x,\\[2mm]
 0,&y\ge x.
\end{cases}
}
\tag{3}
\]

Thus `x=2a log q` is the total available radial depth, while `y=2a log^+(|Gamma|/m)` is a discrete **dead depth** consumed before the logarithmic cells resolve the oscillation `t^{-i Gamma}`. The `NB-103` law is recovered exactly when

\[
2a\log^+(|\Gamma|/m)\to0,
\tag{4}
\]

which allows `|Gamma|/m` to grow, but only subexponentially on the `1/a` scale. If `m<|Gamma|<mq`, the surviving depth is

\[
x-y
=
2a\log\frac{mq}{|\Gamma|}+o(1).
\tag{5}
\]

This is a discretization effect, not a contradiction with `NB-099`: absolute ordinate remains an exact gauge variable for the continuum half-line canonical Gram and deflation geometry. It re-enters only because a finite logarithmic cell cannot reproduce a rapidly rotating Mellin phase until the cell index reaches the ordinate scale.

## 1. The confluent derivative matrix is an exact cell Gram matrix

Keep the stripped finite-window kernel of `NB-103`,

\[
\begin{aligned}
\mathscr C_{m,q}(z,w)
:={}&
\frac{m^{z+w}}
     {(z+\tfrac12)(w+\tfrac12)}
\sum_{n=m}^{mq-1} n(n+1)\\
&\times
\left(n^{-z-1/2}-(n+1)^{-z-1/2}\right)
\left(n^{-w-1/2}-(n+1)^{-w-1/2}\right).
\end{aligned}
\tag{6}
\]

The elementary identity

\[
\frac{n^{-z-1/2}-(n+1)^{-z-1/2}}{z+1/2}
=
\int_n^{n+1}t^{-z-3/2}\,dt
\tag{7}
\]

makes the boundary scaling transparent. For `lambda=a+i Gamma`, define

\[
\Phi_{r,n}
:=
m^\lambda
\int_n^{n+1}
\bigl(2a\log(t/m)\bigr)^r
t^{-\lambda-3/2}\,dt,
\qquad 0\le r<d.
\tag{8}
\]

Differentiating `(6)` under the finite sum gives exactly

\[
\boxed{
K_{rs}^{(m,q,\lambda)}
:=
(2a)^{r+s+1}(-1)^{r+s}
\partial_z^r\partial_w^s
\mathscr C_{m,q}(\lambda,\overline\lambda)
=
2a\sum_{n=m}^{mq-1}
 n(n+1)\Phi_{r,n}\overline{\Phi_{s,n}}.
}
\tag{9}
\]

Hence `K` is a positive semidefinite Gram matrix. Apply the same row/column scaling to the half-line kernel

\[
\mathscr G_\infty(z,w)=\frac1{z+w}.
\]

Its confluent derivative matrix becomes

\[
K^\infty_{rs}=(r+s)!,
\tag{10}
\]

so

\[
\det K^\infty
=
\prod_{r=0}^{d-1}(r!)^2.
\tag{11}
\]

The row and column scalings in `(9)` cancel between numerator and denominator of the `NB-103` determinant quotient. Therefore

\[
\boxed{
\mathcal V^{\mathrm{conf}}_{d,m,q}(\lambda)
=
\frac{\det K^{(m,q,\lambda)}}
     {\prod_{r=0}^{d-1}(r!)^2}.
}
\tag{12}
\]

No fixed-interior `m -> infinity` approximation has been used in `(9)`--`(12)`.

## 2. Boundary scaling turns the logarithmic cells into a fine radial mesh

Write each cell as

\[
t=ne^v,
\qquad
0\le v\le h_n:=\log(1+1/n),
\]

and set

\[
u_n:=2a\log(n/m).
\tag{13}
\]

Then `(8)` is exactly

\[
\Phi_{r,n}
=
m^\lambda n^{-\lambda-1/2}
\int_0^{h_n}
 (u_n+2av)^r
 e^{-(a+1/2+i\Gamma)v}\,dv.
\tag{14}
\]

The radial mesh width of the `n`th cell is

\[
\Delta u_n
=2a h_n.
\tag{15}
\]

As `a -> 0`,

\[
\max_{n\ge1}\Delta u_n
\le2a\log2
\longrightarrow0.
\tag{16}
\]

Thus the boundary limit itself makes the logarithmic mesh fine; no separate assumption `m -> infinity` is needed. The cells in `m<=n<mq` fill `[0,x]` in the `u` coordinate up to a terminal mesh error tending to zero.

The only nonuniform factor in `(14)` is the phase `e^{-i Gamma v}`. Since `h_n\asymp1/n`, it changes behavior when `n` crosses `|Gamma|`. In the `u` coordinate that transition occurs at

\[
2a\log(|\Gamma|/m),
\tag{17}
\]

which is exactly the delay `(2)` when the ordinate lies beyond the first cell scale.

## 3. Cells below the ordinate threshold vanish, cells above it recover the Laguerre density

Fix `delta>0`. Consider first cells satisfying

\[
u_n\le y-\delta.
\tag{18}
\]

Along the sequence in the claim,

\[
\frac{|\Gamma|}{n}
=
\exp\!\left(\frac{y_j-u_n+o(1)}{2a}\right)
\longrightarrow\infty
\tag{19}
\]

uniformly on this region. Integration by parts in `(14)` gives, for fixed `r<d`, a bound by the corresponding nonoscillatory cell size multiplied by `O_d(n/|Gamma|)`. After inserting the two factors into the Gram sum `(9)`, the entire region `(18)` is therefore killed by an exponentially small factor. Its contribution to every `K_{rs}` tends to zero.

Now take

\[
u_n\ge y+\delta.
\tag{20}
\]

Then `|Gamma|/n -> 0` exponentially uniformly on this region. Also `n -> infinity` uniformly after excluding the vanishing initial `u`-band when `y=0`. Consequently

\[
e^{-i\Gamma v}=1+o(1),
\qquad
u_n+2av=u_n+o(1),
\qquad
(n+1)h_n=1+o(1)
\tag{21}
\]

uniformly in the cells of `(20)`. Substituting `(14)` into `(9)` therefore gives the cell asymptotic

\[
K_{rs}[n]
=
e^{-u_n}u_n^{r+s}\,\Delta u_n\,(1+o(1)).
\tag{22}
\]

By `(16)`, these cells form a Riemann sum, so

\[
\sum_{u_n\ge y+\delta}K_{rs}[n]
\longrightarrow
\int_{y+\delta}^{x}u^{r+s}e^{-u}\,du
\tag{23}
\]

when `y+delta<x`, and vanish otherwise.

It remains only the transition strip `|u_n-y|<=delta` (or `[0,delta]` when `y=0`). Cauchy--Schwarz in `(14)`, together with `(n+1)h_n=O(1)` for all `n`, gives the uniform majorant

\[
|K_{rs}[n]|
\le
C_d\,e^{-u_n}(1+u_n)^{2d}\,\Delta u_n.
\tag{24}
\]

Hence the total transition contribution is `O_d(delta)` uniformly in `Gamma`, `m`, and `q` in the stated scaling window. Letting first `j -> infinity` and then `delta -> 0` proves

\[
\boxed{
K_{rs}^{(m_j,q_j,\lambda_j)}
\longrightarrow
\begin{cases}
\displaystyle\int_y^x u^{r+s}e^{-u}\,du,&y<x,\\[3mm]
0,&y\ge x.
\end{cases}
}
\tag{25}
\]

for every fixed `0<=r,s<d`. This also covers `y=0`: any finitely resolved initial cells occupy radial width `o(1)` and disappear into the transition strip.

## 4. The delayed moment determinant is exactly a shifted Laguerre coefficient

For `0<=y<x`, let

\[
M_d(y,x)
=
\left[
\int_y^x u^{r+s}e^{-u}\,du
\right]_{r,s=0}^{d-1}.
\tag{26}
\]

Put `u=y+v`. In the polynomial basis, translation from `v^r` to `(y+v)^r` is represented by a unit triangular matrix, hence has determinant one. The weight contributes one common factor `e^{-y}` to the Gram form. Therefore

\[
\det M_d(y,x)
=
e^{-dy}
\det M_d(0,x-y).
\tag{27}
\]

Using the definition of `Delta_d` from `NB-103`,

\[
\frac{\det M_d(0,L)}
     {\prod_{r=0}^{d-1}(r!)^2}
=
\Delta_d(L).
\tag{28}
\]

Equations `(12)`, `(25)`, `(27)`, and determinant continuity now give `(3)`.

For a one-state packet the law reduces to the transparent control

\[
\mathcal V^{\mathrm{conf}}_{1,m_j,q_j}
\longrightarrow
\begin{cases}
 e^{-y}-e^{-x},&y<x,\\
 0,&y\ge x.
\end{cases}
\tag{29}
\]

For general fixed `d`, the factor `e^{-dy}` records the radial weight already lost before the cells resolve the oscillation, while `Delta_d(x-y)` records the remaining polynomial-volume budget.

## 5. Relation to the half-line gauge and to the `NB-103` radial law

`NB-099` proves exact invariance of the canonical half-line Gram, deflation matrix, and transformed conditioning under a common vertical translation. The present result does not alter that statement. The continuum state `e^{-(a+i Gamma)t}` can remove its common phase by a unitary modulation, so absolute height is invisible there.

The finite Nyman window is different because `(7)` averages the Mellin state over the arithmetic cells `[n,n+1]`. On such a cell, the phase rotates by approximately `Gamma/n`. When `n<<|Gamma|`, the average is suppressed; when `n>>|Gamma|`, the phase is nearly constant. The boundary radial coordinate multiplies logarithmic scale by `2a`, so the physical threshold `n\asymp|Gamma|` becomes the finite delay `(2)`.

Consequently the `NB-103` coefficient `Delta_d(x)` is boundary-uniform precisely in the regime `(4)`. More generally there are three fixed-`d` regimes:

- `y=0`: the full `NB-103` coefficient `Delta_d(x)` survives;
- `0<y<x`: only the delayed coefficient `e^{-dy}Delta_d(x-y)` survives;
- `y>=x`: the entire normalized confluent volume disappears before the cells reach a resolvable scale.

This is a stronger classification than a generic statement that the fixed-interior error constant deteriorates as `a -> 0`: it identifies the missing dimensionless variable and computes its exact limiting effect.

For a hypothetical zeta zero `rho=beta+i gamma`, the two scales are

\[
x=2(\beta-\tfrac12)\log q,
\qquad
y=2(\beta-\tfrac12)\log^+\!\frac{|\gamma|}{m}.
\tag{30}
\]

If `m<|gamma|<mq`, the determinant sees the residual depth

\[
2(\beta-\tfrac12)\log\frac{mq}{|\gamma|}
\tag{31}
\]

rather than the nominal depth `2(beta-1/2) log q` alone. This does not itself constrain actual zeta zeros: one may move the band start `m`, and doing so can remove the delay. It instead identifies the exact synchronization cost that any source-to-finite-section application has to pay.

## 6. Prior-art boundary, controls, and limitations

The ingredients of the derivation are classical. The Nyman--Beurling/Baez--Duarte criterion and Burnol's zero-sensitive quantitative approximation boundary are already anchored in `SOURCES.md`. Truncated and interval Laguerre moment determinants are standard Hankel/orthogonal-polynomial objects, including their interpretation as finite Laguerre-unitary-ensemble gap probabilities. No novelty is claimed for those determinant identities, for oscillatory cell averaging, or for the abstract fact that high frequencies require a sufficiently fine mesh.

A targeted prior-art search across Nyman--Beurling finite sections, Mellin/Blaschke formulations, logarithmic oscillatory discretization, and Laguerre Hankel determinants did not identify the specific boundary double-scaling law `(3)` for the `NB-103` finite-window confluent coefficient. The line-local contribution is therefore narrower: the exact reduction of the discrete Nyman cell Gram to an **ordinate-delayed Laguerre interval**, and the resulting scale coupling `(30)`. No external theorem is load-bearing in the proof, so no new `SOURCES.md` dependency is required.

Several boundaries remain essential. First, `d` is fixed; `(3)` gives no uniform control when multiplicity or the selected packet size grows. Second, the object is the analytic confluent continuation of the distinct-state determinant from `NB-103`, not the causal Jordan realization of a genuine repeated zeta zero. Third, determinant volume is not spectral conditioning: the Menger-curvature obstruction of `NB-102` remains independent. Fourth, determinant volume is not Nyman target distance; the target-aware finite-section and dual-certificate branch remains binding.

Finally, `(3)` does not say that large ordinate is intrinsically harmful. If the band begins at `m` comparable to or above `|Gamma|`, then `y=0` and the full radial coefficient is restored. The new gate is therefore not absolute height but **height relative to the arithmetic resolution scale available at the start of the finite window**.

## Consequence

`NB-103` left boundary uniformity as an unspecified two-parameter problem. It is now explicit at fixed multiplicity. In the critical-boundary scaling `a -> 0` with finite nominal depth `x=2a log q`, the finite Nyman state volume does not depend on `x` alone. The discrete cells subtract the ordinate delay

\[
\boxed{
y=2a\log^+(|\Gamma|/m)}
\]

before the continuum Laguerre volume law starts.

The next source-facing question is therefore sharper. If a later Nyman argument needs this determinant volume for zeros approaching the critical line, it must either synchronize the band start with their ordinates so that `y=o(1)`, or explicitly pay the delayed coefficient in `(3)`. If the argument instead needs stable coordinate inversion or target conversion, this volume theorem does not remove the separate conditioning and target-alignment gates.