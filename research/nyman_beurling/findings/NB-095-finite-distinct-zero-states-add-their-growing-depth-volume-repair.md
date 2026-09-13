# NB-095 — finite distinct zero states add their growing-depth volume repair

**Status:** `EXACT-DERIVED + ACTUAL-NYMAN-SOURCE + FINITE-DISTINCT-OFF-CRITICAL-DIVISOR + GROWING-DEPTH + INTERACTING-STATE-LAW + ADDITIVE-HORIZONTAL-MASS + NORMALIZED-VOLUME-REPAIR`.

`NB-094` closes the growing-depth correlation-volume law for one actual off-critical zero. The remaining finite-family difficulty is genuine: after one Blaschke factor is removed, the next causal state is evaluated on a partially deflated source, not on the raw innovation, so single-zero estimates cannot simply be added factor by factor.

For any **fixed finite set of pairwise distinct actual zeta zeros** in the right half of the critical strip, that interaction can nevertheless be eliminated exactly. The successive causal states are related by a fixed invertible triangular transformation to the raw single-zero state vectors of `NB-094`. On a band `m <= j < R=mq`, the inverse-raw-Gram matrix of those raw states has, after the natural anisotropic scaling by `q^(rho-1/2)`, a uniformly positive Cauchy/model-space limit. Consequently every selected zero contributes its own horizontal exponent to the finite-state determinant, while the total diagonal-normalization bill stays bounded.

Let

\[
F=\{\rho_1,\ldots,\rho_d\},
\qquad
\rho_r=\beta_r+i\gamma_r,
\qquad
\beta_r>\frac12,
\tag{1}
\]

be pairwise distinct actual zeros of `zeta`, and put

\[
\lambda_r:=\rho_r-\frac12,
\qquad
a_r:=\Re\lambda_r=\beta_r-\frac12>0,
\qquad
A_F:=\sum_{r=1}^d a_r.
\tag{2}
\]

Use the elementary factors

\[
b_r(z)=\frac{z-\lambda_r}{z+\overline{\lambda_r}},
\qquad
B_F=\prod_{r=1}^d b_r.
\tag{3}
\]

For the raw innovations

\[
\widetilde D_j(s)
=\frac{\zeta(s)}s\bigl(j^{1-s}-(j+1)^{1-s}\bigr),
\tag{4}
\]

define

\[
D_j^{[F]}:=\frac{\widetilde D_j}{B_F}.
\tag{5}
\]

For integers `m>=1`, `q>=2`, set `R=mq` and use the consecutive band

\[
I_{m,R}=\{m,m+1,\ldots,R-1\}.
\tag{6}
\]

Let `A_(m,R)` be the visible Gram of `J_R widetilde D_j` on this band, `K_(m,R)^[F]` the visible Gram of `J_R D_j^[F]`, and let `widetilde mathcal R_(m,R)` and `mathcal R_(m,R)^[F]` be their diagonal correlation normalizations.

Then there are constants

\[
m_F\in\mathbb N,
\qquad
0<c_F\le C_F<\infty,
\tag{7}
\]

depending only on the fixed zero set `F`, such that for every `m>=m_F` and every integer `q>=2`,

\[
\boxed{
 c_F q^{2A_F}
 \le
 \frac{\det\mathcal R_{m,mq}^{[F]}}
      {\det\widetilde{\mathcal R}_{m,mq}}
 \le
 C_F q^{2A_F}.
}
\tag{8}
\]

Equivalently,

\[
\boxed{
\log\frac{\det\mathcal R_{m,mq}^{[F]}}
          {\det\widetilde{\mathcal R}_{m,mq}}
=
2\sum_{r=1}^d\left(\beta_r-\frac12\right)\log q
+O_F(1).
}
\tag{9}
\]

Thus the one-zero law of `NB-094` is not destroyed by finite state interaction. For distinct factors the growing-depth normalized volume-repair exponents are **additive**. In centered-entropy form,

\[
\boxed{
-\log\det\mathcal R_{m,mq}^{[F]}
+
\log\det\widetilde{\mathcal R}_{m,mq}
=
-2A_F\log q+O_F(1).
}
\tag{10}
\]

The finite-family sign is therefore the same as the single-zero sign: a fixed right-half Blaschke divisor creates a correlation-volume repair, not a positive correlation-entropy charge.

## 1. Successive deflation states are a triangular transform of raw zero states

For each selected zero define the raw one-zero state vector on the band by

\[
u^{(r)}_{j,R}
:=
\sqrt{2a_r}
\int_0^{\log R}
 e^{\lambda_r(\log R-v)}\widetilde d_j(v)\,dv,
\qquad j\in I_{m,R}.
\tag{11}
\]

Because `rho_r` is an actual zero, `NB-094` proves the source-specific uniform cancellation

\[
\boxed{
|u^{(r)}_{j,R}|\ll_{\rho_r}R^{-1/2}
}
\qquad(1\le j<R).
\tag{12}
\]

Collect these columns in

\[
U_R=[u^{(1)}_R\ \cdots\ u^{(d)}_R].
\tag{13}
\]

Now remove the factors in any fixed order. Write

\[
B_{k-1}=\prod_{r<k}b_r,
\qquad
x_{k-1,j}:=\frac{\widetilde D_j}{B_{k-1}},
\tag{14}
\]

so the `k`th rank-one update removes `b_k` from `x_(k-1,j)`. Let `s^(k)_R` be that update's causal state vector. Iterating the exact one-factor identity of `NB-093` gives

\[
K_{m,R}^{[F]}
=A_{m,R}+S_RS_R^*,
\qquad
S_R=[s_R^{(1)}\ \cdots\ s_R^{(d)}].
\tag{15}
\]

The apparent problem is that `s^(k)` is built from `x_(k-1)`, not from the raw source. Distinctness of the selected zeros removes that problem algebraically. Since

\[
\frac1{B_{k-1}(z)}
=1+\sum_{r<k}\frac{c_{kr}}{z-\lambda_r}
\tag{16}
\]

for constants `c_(kr)` depending only on `F`, the inverse-filter time representation is

\[
x_{k-1,j}(t)
=
\widetilde d_j(t)
+
\sum_{r<k}c_{kr}
\int_0^t e^{\lambda_r(t-v)}\widetilde d_j(v)\,dv.
\tag{17}
\]

For

\[
Y_{j,T}(w):=\int_T^\infty e^{-wv}\widetilde d_j(v)\,dv,
\qquad T=\log R,
\tag{18}
\]

the zero identity `widetilde D_j(rho_r)=0` rewrites each convolution in `(17)` as

\[
\int_0^t e^{\lambda_r(t-v)}\widetilde d_j(v)\,dv
=-e^{\lambda_rt}Y_{j,t}(\lambda_r).
\tag{19}
\]

For `r<k`, direct Fubini gives

\[
\int_T^\infty
 e^{-(\lambda_k-\lambda_r)t}Y_{j,t}(\lambda_r)\,dt
=
\frac{
 e^{-(\lambda_k-\lambda_r)T}Y_{j,T}(\lambda_r)
 -Y_{j,T}(\lambda_k)
}{\lambda_k-\lambda_r}.
\tag{20}
\]

The `k`th state is the scaled missing tail of `x_(k-1,j)` at `lambda_k`. Combining `(16)`--`(20)` therefore yields

\[
s_R^{(k)}
=
\frac1{B_{k-1}(\lambda_k)}u_R^{(k)}
+
\sum_{r<k}t_{rk}u_R^{(r)},
\tag{21}
\]

where every `t_(rk)` is a constant depending only on the selected zeros. In particular,

\[
\boxed{
S_R=U_RT_F
}
\tag{22}
\]

for a fixed triangular matrix `T_F` with

\[
(T_F)_{kk}=B_{k-1}(\lambda_k)^{-1}\ne0.
\tag{23}
\]

Hence `T_F` is invertible. This is the exact interaction law missing from the one-zero calculation: finite distinct zero states can mix, but their mixing is an `R`-independent change of coordinates. It cannot change a power of the multiplicative depth.

## 2. The raw inverse-Gram interaction converges to a positive exponential Gram

Set

\[
H_{m,R}:=U_R^*A_{m,R}^{-1}U_R.
\tag{24}
\]

`NB-094` identifies the raw visible innovations on `I_(m,R)` with a basis of the complete orthogonal integer-cell space

\[
\mathcal E_{m,R}
=
\operatorname{span}\left\{
\phi_n(t)=e^{-t/2}\mathbf1_{[\log n,\log(n+1))}(t):m\le n<R
\right\}.
\tag{25}
\]

Therefore the cross-leverage entries, not only the diagonal ones, can be evaluated in that orthogonal basis. Put

\[
\Delta_r(n):=n^{-\rho_r}-(n+1)^{-\rho_r}.
\tag{26}
\]

Since

\[
L_{r,R}(\phi_n)
=
\frac{\sqrt{2a_r}}{\rho_r}
 R^{\lambda_r}\Delta_r(n),
\qquad
\|\phi_n\|_2^2=\frac1{n(n+1)},
\tag{27}
\]

we obtain the exact matrix identity

\[
\boxed{
(H_{m,R})_{rs}
=
\frac{2\sqrt{a_ra_s}}{\rho_r\overline{\rho_s}}
R^{\lambda_r+\overline{\lambda_s}}
\sum_{n=m}^{R-1}
 n(n+1)\Delta_r(n)\overline{\Delta_s(n)}.
}
\tag{28}
\]

Now put `R=mq` and

\[
D_q:=\operatorname{diag}(q^{\lambda_1},\ldots,q^{\lambda_d}).
\tag{29}
\]

Then

\[
H_{m,mq}=D_q C_{m,q}D_q^*,
\tag{30}
\]

where `(28)` gives `C_(m,q)` explicitly. For

\[
\eta_{rs}:=\lambda_r+\overline{\lambda_s},
\qquad \Re\eta_{rs}=a_r+a_s>0,
\tag{31}
\]

the elementary expansion

\[
\frac{n(n+1)}{\rho_r\overline{\rho_s}}
\Delta_r(n)\overline{\Delta_s(n)}
=
n^{-1-\eta_{rs}}+O_F(n^{-2-\Re\eta_{rs}})
\tag{32}
\]

and a sum-integral comparison give, uniformly for every `q>=2`,

\[
\boxed{
(C_{m,q})_{rs}
=
2\sqrt{a_ra_s}
\frac{1-q^{-\eta_{rs}}}{\eta_{rs}}
+O_F(m^{-1}).
}
\tag{33}
\]

The leading matrix has an immediate Gram representation. Define

\[
G_F(q)_{rs}
:=
2\sqrt{a_ra_s}
\frac{1-q^{-(\lambda_r+\overline{\lambda_s})}}
     {\lambda_r+\overline{\lambda_s}}.
\tag{34}
\]

Then

\[
G_F(q)_{rs}
=
\int_0^{\log q}
\sqrt{2a_r}\,e^{-\lambda_rt}
\overline{\sqrt{2a_s}\,e^{-\lambda_st}}\,dt.
\tag{35}
\]

Because the `lambda_r` are pairwise distinct, the exponentials in `(35)` are linearly independent on every nontrivial interval. Thus `G_F(2)>0`. Moreover `G_F(q)` increases in Loewner order with `q` and is bounded above by

\[
G_F(\infty)_{rs}
=
\frac{2\sqrt{a_ra_s}}
      {\lambda_r+\overline{\lambda_s}},
\tag{36}
\]

the classical positive Cauchy/model-space Gram on the half-line. Hence there are constants depending only on `F` such that

\[
c_F I\preceq G_F(q)\preceq C_F I
\qquad(q\ge2).
\tag{37}
\]

Equation `(33)` now implies that after choosing `m_F` sufficiently large,

\[
\boxed{
c_F'I\preceq C_{m,q}\preceq C_F'I}
\qquad(m\ge m_F,\ q\ge2).
\tag{38}
\]

Consequently

\[
\det H_{m,mq}
=q^{2A_F}\det C_{m,q}
\asymp_F q^{2A_F},
\tag{39}
\]

and, writing `a_min=min_r a_r>0`,

\[
\lambda_{\min}(H_{m,mq})\gg_F q^{2a_{\min}}.
\tag{40}
\]

This is the source of additivity. The growing band turns the raw zero states into anisotropically amplified copies of a fixed positive model-space Gram; distinct state directions do not collapse into one maximal-zero mode.

## 3. The interacting finite-state determinant has the additive exponent

From `(22)`,

\[
S_R^*A_{m,R}^{-1}S_R
=T_F^*H_{m,R}T_F.
\tag{41}
\]

The matrix determinant lemma applied to `(15)` gives

\[
\frac{\det K_{m,R}^{[F]}}{\det A_{m,R}}
=
\det\left(I_d+T_F^*H_{m,R}T_F\right).
\tag{42}
\]

Because `T_F` is fixed and invertible, `(39)`--`(40)` imply

\[
\det(T_F^*H_{m,mq}T_F)
\asymp_F q^{2A_F},
\qquad
\lambda_{\min}(T_F^*H_{m,mq}T_F)\gg_F q^{2a_{\min}}.
\tag{43}
\]

Since `q>=2`, replacing this positive matrix by `I` plus the matrix changes its determinant only by another `F`-dependent multiplicative constant. Hence

\[
\boxed{
\frac{\det K_{m,mq}^{[F]}}{\det A_{m,mq}}
\asymp_F
q^{2A_F}
}
\qquad(m\ge m_F,\ q\ge2).
\tag{44}
\]

So the unnormalized finite-family state interaction already has the exact sum of the single-zero horizontal exponents. The result is stronger than a monotonicity lower bound from the zero with largest real part: no selected distinct zero is lost at the determinant level.

## 4. Diagonal normalization costs only a fixed constant

The remaining issue is precisely the one that blocked `NB-092`: correlation normalization divides out every diagonal. Here the triangular state law and `NB-094` make the total bill harmless.

From `(12)` and `(22)`, for every row of `S_R`,

\[
\|(S_R)_{j,*}\|^2
\le
\|T_F\|^2\sum_{r=1}^d|u^{(r)}_{j,R}|^2
\ll_F R^{-1}.
\tag{45}
\]

Since `(15)` gives

\[
(K_{m,R}^{[F]})_{jj}
=(A_{m,R})_{jj}+\|(S_R)_{j,*}\|^2,
\tag{46}
\]

and `NB-094` gives the source-uniform lower bound

\[
(A_{m,R})_{jj}\ge\frac{j}{j+1}\ge\frac12,
\tag{47}
\]

we have

\[
0\le
\sum_{j=m}^{R-1}
\log\frac{(K_{m,R}^{[F]})_{jj}}{(A_{m,R})_{jj}}
\ll_F
\frac{R-m}{R}
\ll_F1.
\tag{48}
\]

Finally,

\[
\log\frac{\det\mathcal R_{m,R}^{[F]}}
          {\det\widetilde{\mathcal R}_{m,R}}
=
\log\frac{\det K_{m,R}^{[F]}}
          {\det A_{m,R}}
-
\sum_{j=m}^{R-1}
\log\frac{(K_{m,R}^{[F]})_{jj}}{(A_{m,R})_{jj}}.
\tag{49}
\]

Combining `(44)` and `(48)` proves `(8)`--`(10)`.

The mechanism is worth separating into its two resources. Actual zeta-zero cancellation makes **every raw zero state rowwise cheap**, so a fixed collection still costs only `O_F(1)` under diagonal normalization. At the same time the integer-cell inverse Gram sees those states collectively as a positive finite-dimensional exponential system whose determinant expands by `q^(2A_F)`. Finite interaction changes only the constant basis matrix `T_F`; it cannot erase the depth exponent.

## 5. Prior-art boundary, controls, and remaining obstruction

Burnol's Hardy-space result already identifies the global Nyman projection with the full right-half-plane Blaschke product and gives the familiar multiplicative contribution of off-critical zeros to the infinite-space target projection. That is a different observable from `(8)`: the present statement concerns a **finite growing-depth visible correlation determinant** of consecutive Nyman innovations. No novelty is claimed for finite Blaschke model spaces, their finite state dimension, the Cauchy Gram `(36)`, or the fact that distinct exponentials are linearly independent.

The closest contemporary Nyman-specific boundary remains T. A. Ziad's 2026 finite Blaschke/arithmetic Gram split, already recorded in `SOURCES.md`. The targeted literature audit did not locate the band law `(8)`, the triangular raw-state reduction `(22)`, or the additive growing-depth exponent `(9)` for the canonical Nyman innovations. Hugh Carvill's multiscale Gram work concerns smoothed unconditional generator geometry rather than this Blaschke-state finite-horizon determinant. No priority claim is made. All load-bearing analytic input in this finding is either derived above or already contained in `NB-093`--`NB-094`, so `SOURCES.md` needs no new dependency.

Several boundaries are essential.

First, `F` is fixed and consists of pairwise distinct zeros. Repeated copies of a multiple zero require confluent partial fractions and are not covered by `(22)`--`(38)`. The theorem may always select one factor from each distinct off-critical zero, but it does not state the multiplicity law.

Second, the constants are not uniform as the number or geometry of selected zeros changes. In particular, `(8)` cannot be passed to the full infinite Burnol product by taking `d` to infinity. The triangular matrix can become poorly conditioned, the Cauchy Gram can lose quantitative separation, and diagonal normalization is not monotone when further states are added.

Third, the uniform Cauchy comparison is asserted only once the band base satisfies `m>=m_F`. This is an asymptotic growing-section statement, not a claim about every small finite section.

Fourth, correlation volume is still generator geometry. `NB-001` and the line mandate prohibit treating a Gram-only statistic as target distance. Equation `(9)` proves a sharp source-sensitive signature of a fixed finite off-critical divisor; it does **not** by itself provide a Nyman approximation lower bound or prove RH.

Fifth, actual zero identities are load-bearing twice: they make every deflation legal in `H^2`, and through `NB-094` they give the `R^(-1/2)` coordinate suppression used in `(45)`. A synthetic rational all-pass family with the same finite state dimension but without the zeta-zero cancellation need not have a bounded normalization bill.

The durable frontier after `NB-094` is therefore narrower. **Finite interaction among distinct off-critical zero states is no longer an obstruction: its normalized growing-depth exponent is exactly additive in their horizontal masses.** What remains is genuinely infinite-family or target-facing: control the constants/effective state rank as the selected divisor grows, handle possible multiplicities if needed, or convert the calibrated volume repair into a target-relevant Nyman obstruction without re-importing RH.