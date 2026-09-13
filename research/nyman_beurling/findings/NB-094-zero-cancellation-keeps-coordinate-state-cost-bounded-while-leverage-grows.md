# NB-094 — zero cancellation keeps coordinate-state cost bounded while leverage grows

**Status:** `EXACT-DERIVED + ACTUAL-NYMAN-SOURCE + SINGLE-OFF-CRITICAL-ZERO + GROWING-DEPTH + UNIFORM-COORDINATE-SUPPRESSION + EXACT-LEVERAGE-CELL-FORMULA + NORMALIZED-CORRELATION-BRIDGE-CLOSED + NEGATIVE-ENTROPY-EXCESS`.

`NB-093` reduces the one-zero diagonal-normalization problem to the exact identity

\[
-\log\det\mathcal R_{m,R}^{(\rho)}
+\log\det\widetilde{\mathcal R}_{m,R}
=
\sum_{j=m}^{R-1}\log(1+\nu_{j,R})
-
\log(1+\tau_{m,R}),
\tag{1}
\]

where `rho=beta+i gamma` is an actual zeta zero with `beta>1/2`,

\[
a:=\beta-\frac12>0,
\qquad
\lambda:=\rho-\frac12,
\tag{2}
\]

`nu_(j,R)=|s_(j,R)|^2/(A_R)_(jj)` is the coordinatewise inflation of the one-state causal update, and

\[
\tau_{m,R}=s_R^*A_R^{-1}s_R
\tag{3}
\]

is its inverse-Gram leverage on the consecutive band `I_(m,R)={m,...,R-1}`. `NB-093` proves the lower bound `tau_(m,mq) >= q^(2a+o(1))` but leaves open whether the coordinate bill in `(1)` can absorb that gain.

For the actual Nyman raw innovations it cannot. The zeta-zero condition itself suppresses **every individual state coordinate** to the finite-cutoff scale `R^(-1/2)`, uniformly over the entire growing band, while the same state has polynomial inverse-Gram leverage because the raw band becomes nearly singular in a coherent Möbius direction.

More precisely, there is a constant `C_rho<infinity` such that for every integer `R>=2` and every `1<=j<R`,

\[
\boxed{
|s_{j,R}|\le C_\rho R^{-1/2}.
}
\tag{4}
\]

Since the raw visible diagonal always obeys

\[
(A_R)_{jj}=\|J_R\widetilde D_j\|_2^2
\ge \frac{j}{j+1}\ge\frac12,
\tag{5}
\]

it follows uniformly for every consecutive band that

\[
\boxed{
\sum_{j=m}^{R-1}\log(1+\nu_{j,R})=O_\rho(1).
}
\tag{6}
\]

At the same time the leverage has an exact orthogonal-cell representation:

\[
\boxed{
\tau_{m,R}
=
\frac{2a}{|\rho|^2}R^{2a}
\sum_{n=m}^{R-1}
 n(n+1)
\left|n^{-\rho}-(n+1)^{-\rho}\right|^2.
}
\tag{7}
\]

Putting `R=mq`, equations `(7)` and the Möbius-annulus lower bound of `NB-093` give two-sided growth

\[
\boxed{
 c_\rho q^{2a}
\le 1+\tau_{m,mq}
\le C_\rho q^{2a}
}
\qquad(m\ge1,\ q\ge2).
\tag{8}
\]

Therefore the exact normalized bridge `(1)` closes with the full zero-frontier exponent:

\[
\boxed{
\log\frac{\det\mathcal R_{m,mq}^{(\rho)}}
          {\det\widetilde{\mathcal R}_{m,mq}}
=(2\beta-1)\log q+O_\rho(1),
}
\tag{9}
\]

or equivalently

\[
\boxed{
-\log\det\mathcal R_{m,mq}^{(\rho)}
+
\log\det\widetilde{\mathcal R}_{m,mq}
=-(2\beta-1)\log q+O_\rho(1).
}
\tag{10}
\]

Thus diagonal normalization does **not** erase the polynomial single-zero Gram repair found in `NB-092`. It preserves its entire logarithmic exponent. The sign is also determined: one off-critical zero decreases the raw centered correlation entropy by `(2 beta-1) log q+O(1)` rather than adding a positive entropy charge.

## 1. The zeta-zero identity cancels the only large coordinate term

The raw Paley--Wiener innovation is

\[
\widetilde d_j(t)
=e^{-t/2}
\left[
 j\left\lfloor\frac{e^t}{j}\right\rfloor
-(j+1)\left\lfloor\frac{e^t}{j+1}\right\rfloor
\right].
\tag{11}
\]

From `NB-093`, the one-zero state at cutoff `R` is

\[
s_{j,R}
=
\sqrt{2a}
\int_0^{\log R}
 e^{\lambda(\log R-v)}\widetilde d_j(v)\,dv.
\tag{12}
\]

For `Re rho>0`, define

\[
F_\rho(y)
:=
\int_1^y\lfloor u\rfloor u^{-\rho-1}\,du,
\qquad
E_\rho(y)
:=
\int_y^\infty\{u\}u^{-\rho-1}\,du.
\tag{13}
\]

The classical fractional-part representation, valid in the strip `Re rho>0`, is

\[
\zeta(\rho)
=
\frac{\rho}{\rho-1}
-
\rho\int_1^\infty\{u\}u^{-\rho-1}\,du.
\tag{14}
\]

Because `rho` is an **actual zero**, `(14)` gives

\[
\int_1^\infty\{u\}u^{-\rho-1}\,du
=
\frac1{\rho-1}.
\tag{15}
\]

Using `floor u=u-{u}` in `(13)`, the constant term cancels exactly and one obtains

\[
\boxed{
F_\rho(y)
=
\frac{y^{1-\rho}}{1-\rho}
+E_\rho(y).
}
\tag{16}
\]

For the single floor component

\[
h_k(t):=e^{-t/2}k\left\lfloor\frac{e^t}{k}\right\rfloor,
\tag{17}
\]

a change of variables gives

\[
\int_0^{\log R}e^{-\lambda v}h_k(v)\,dv
=
k^{1-\rho}F_\rho(R/k)
=
\frac{R^{1-\rho}}{1-\rho}
+k^{1-\rho}E_\rho(R/k).
\tag{18}
\]

The first term in `(18)` is independent of `k`. Since `widetilde d_j=h_j-h_(j+1)`, it disappears from every innovation. Hence, with

\[
g_R(x):=x^{1-\rho}E_\rho(R/x),
\tag{19}
\]

we have the exact state formula

\[
\boxed{
\frac{s_{j,R}}{\sqrt{2a}\,R^\lambda}
=g_R(j)-g_R(j+1).
}
\tag{20}
\]

This is the source-specific cancellation that the abstract rank-one control in `NB-093` does not possess.

Now `beta=Re rho>1/2`, so

\[
|E_\rho(y)|
\le
\int_y^\infty u^{-\beta-1}\,du
=
\frac{y^{-\beta}}{\beta}.
\tag{21}
\]

The function `g_R` is absolutely continuous away from harmless integer breakpoints, and almost everywhere

\[
g_R'(x)
=
(1-\rho)x^{-\rho}E_\rho(R/x)
+
\{R/x\}R^{-\rho}.
\tag{22}
\]

Equations `(21)`--`(22)` give the uniform bound

\[
|g_R'(x)|
\le
\left(1+\frac{|1-\rho|}{\beta}\right)R^{-\beta},
\qquad 1\le x\le R.
\tag{23}
\]

Therefore `(20)` yields

\[
|s_{j,R}|
\ll_\rho
R^{\beta-1/2}R^{-\beta}
=R^{-1/2},
\tag{24}
\]

which proves `(4)`.

The cancellation in `(16)` is load-bearing. For a generic point `w` in the strip with `zeta(w) != 0`, the same calculation contains the extra term

\[
F_w(y)
=
\frac{y^{1-w}}{1-w}
+
\frac{\zeta(w)}w
+E_w(y),
\tag{25}
\]

so `(18)` retains a nonzero multiple of `k^(1-w)`. The uniform `R^(-1/2)` coordinate suppression does not follow. Thus `(4)` is not a generic all-pass or finite-section effect; it uses the arithmetic zero condition at exactly the point where it is needed.

## 2. The diagonal-normalization bill is uniformly bounded

On the first visible cell of the `j`th raw innovation, `x in [j,j+1)`, the coefficient in `(11)` is exactly `j`. Therefore

\[
\begin{aligned}
(A_R)_{jj}
&=\|J_R\widetilde D_j\|_2^2\\
&\ge
j^2\int_{\log j}^{\log(j+1)}e^{-t}\,dt\\
&=
\frac{j}{j+1},
\end{aligned}
\tag{26}
\]

which is `(5)`. Combining `(4)` and `(26)`,

\[
\nu_{j,R}
=
\frac{|s_{j,R}|^2}{(A_R)_{jj}}
\ll_\rho \frac1R.
\tag{27}
\]

There are fewer than `R` coordinates in any band `m<=j<R`. Since `log(1+x)<=x` for `x>=0`,

\[
\sum_{j=m}^{R-1}\log(1+\nu_{j,R})
\le
\sum_{j=m}^{R-1}\nu_{j,R}
=O_\rho(1),
\tag{28}
\]

uniformly in both `m` and the multiplicative depth `R/m`. This proves `(6)`.

The point is geometric rather than merely quantitative. The state is tiny in every generator coordinate, but `NB-093` already shows that the raw inverse Gram can amplify the coherent vector by a polynomial factor. Growing-depth source sensitivity is therefore genuinely a **collective near-kernel effect**, not rowwise energy growth.

## 3. The leverage is the exact Riesz norm on the integer-cell space

The raw visible innovations on `j=m,...,R-1` form a basis of the complete integer-cell space

\[
\mathcal E_{m,R}
:=
\operatorname{span}
\left\{
\phi_n(t):=
 e^{-t/2}\mathbf1_{[\log n,\log(n+1))}(t)
:
 m\le n<R
\right\}.
\tag{29}
\]

Indeed `NB-091` factors the raw Gram through the square lower-triangular coefficient matrix

\[
a_j(n)
=j\left\lfloor\frac nj\right\rfloor
-(j+1)\left\lfloor\frac n{j+1}\right\rfloor,
\qquad a_j(j)=j,
\tag{30}
\]

so that matrix is invertible.

Let the state functional on the cell space be

\[
L_{\rho,R}(f)
:=
\sqrt{2a}\int_0^{\log R}
 e^{\lambda(\log R-v)}f(v)\,dv.
\tag{31}
\]

Its values on the orthogonal cell basis are explicit:

\[
L_{\rho,R}(\phi_n)
=
\frac{\sqrt{2a}}\rho
R^\lambda
\left(n^{-\rho}-(n+1)^{-\rho}\right),
\tag{32}
\]

while

\[
\|\phi_n\|_2^2
=
\frac1{n(n+1)}.
\tag{33}
\]

The quantity `tau_(m,R)=s_R^*A_R^(-1)s_R` is basis invariant: it is exactly the squared Riesz norm of `L_(rho,R)` restricted to `E_(m,R)`. Using the orthogonal basis `(29)` therefore gives `(7)` immediately.

This also supplies the missing upper bound on the leverage. Since

\[
n^{-\rho}-(n+1)^{-\rho}
=
\rho\int_n^{n+1}x^{-\rho-1}\,dx,
\tag{34}
\]

we have

\[
\left|n^{-\rho}-(n+1)^{-\rho}\right|
\le
|\rho|n^{-\beta-1}.
\tag{35}
\]

Substitution into `(7)` yields

\[
\tau_{m,R}
\ll_a
R^{2a}
\sum_{n=m}^{\infty}n^{-2\beta}
\ll_a
\left(\frac Rm\right)^{2a}.
\tag{36}
\]

For `R=mq`, `NB-093` gives the complementary exact variational lower bound

\[
\tau_{m,mq}
\ge
\frac{2a}{|\rho|^2}
\frac{|q^\lambda-q^{-1/2}|^2}{1-1/q}
\gg_\rho q^{2a}.
\tag{37}
\]

Together `(36)`--`(37)` prove `(8)` and hence

\[
\log(1+\tau_{m,mq})
=(2\beta-1)\log q+O_\rho(1).
\tag{38}
\]

Combining `(28)` and `(38)` with the exact bridge `(1)` proves `(9)`--`(10)`.

## 4. Consequence for the growing-depth frontier

The ambiguity left by `NB-093` is resolved for a single actual off-critical zero. The large generalized eigenvalue is **not** paid for by diagonal inflation: each row sees only `O(R^-1)` relative state energy, while the inverse raw Gram coherently aggregates those tiny coordinates into `q^(2 beta-1)` leverage. The normalized determinant therefore retains the entire zero exponent.

This also fixes the sign. Relative to the universal raw correlation baseline, removing one actual off-critical Blaschke factor makes the visible correlation volume polynomially **larger**, so its centered correlation entropy is lower by

\[
(2\beta-1)\log q+O_\rho(1).
\tag{39}
\]

Accordingly, a strategy that expected false RH to create a positive centered correlation-entropy excess has the sign backwards at the one-zero level. A viable radial obstruction can still use this information, but it must be formulated as a calibrated volume **repair/deficit**, an inter-scale effect, or a statistic whose sign matches the one-zero geometry.

The result does **not** yet settle the full Burnol product. Successive factors act on intermediate partially deflated sources, and diagonal normalization is not monotone under adding further state directions. What is now closed is the single-zero bridge: no additional estimate is needed to know whether normalization erases the `NB-092` exponent; it does not.

## 5. Prior-art and falsification boundary

A targeted search again found the nearest Nyman-specific boundaries to be Burnol's Hardy/Blaschke decomposition already anchored in `SOURCES.md`, Ziad's 2026 finite Blaschke versus arithmetic Gram split, and Carvill's smoothed multiscale Gram analysis. None of those sources located in the audit states the natural consecutive-cell Riesz identity `(7)`, the zero-driven uniform coordinate cancellation `(4)`, or the normalized determinant asymptotic `(9)`. No priority claim is made.

The proof uses no new specialized external estimate. The only analytic identity beyond the line's existing Hardy setup is the standard fractional-part representation `(14)`, which is re-derived into the exact cancellation needed here; the remaining steps are the explicit raw integer-cell factorization from `NB-091`, the one-state identity from `NB-093`, and elementary integral bounds. `SOURCES.md` therefore needs no expansion.

The main adversarial boundaries are strict. First, `rho` must be an **actual** zeta zero; replacing it by a generic right-half-plane parameter restores the `zeta(w) k^(1-w)/w` coordinate term in `(25)`. Second, `(9)` concerns the one-zero partially deflated source `widetilde D_j/b_lambda`, not the complete infinite Blaschke-deflated Nyman family. Third, the result determines the centered correlation determinant, not by itself the sign of every radial Szego charge from `NB-085`--`NB-086`. Fourth, the estimate is uniform in the base scale `m`, so the effect cannot be dismissed as a small-`m` endpoint artifact.

The durable delta is therefore quantitative and source-specific: **an actual off-critical zeta zero creates a state that is `O(R^-1/2)` in every visible Nyman coordinate but `q^(beta-1/2)` in inverse-Gram norm, so diagonal normalization preserves the full `q^(2 beta-1)` determinant repair rather than cancelling it**.