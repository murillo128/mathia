# NB-091 — fixed-ratio Nyman bands are source-silent after universal Gram calibration

**Status:** `EXACT-DERIVED + CONDITIONAL-ACTUAL-NYMAN-SOURCE + FIXED-RATIO-BANDS + EXACT-RAW-DETERMINANT + UNIVERSAL-CORRELATION-BASELINE + SUMMABLE-HORIZONTAL-ZERO-MASS + BOUNDED-EXCESS + NEGATIVE-METHOD-BOUNDARY`.

`NB-090` shows that under summable horizontal off-critical zero mass, the complete **dyadic** terminal Gram determinant remains bounded. A natural escape is to widen the terminal window: perhaps a fixed deeper ratio `q>=3` sees enough nonterminal structure that the same determinant becomes source-sensitive.

It does become much larger, but for a universal reason already present on the raw zeta side. After subtracting that baseline, every **fixed** ratio remains silent under the same summable-mass hypothesis.

Let

\[
A:=\sum_{\Re\rho>1/2}\left(\Re\rho-\frac12\right)<\infty,
\tag{1}
\]

fix an integer `q>=2`, and put

\[
m_R:=\left\lceil\frac Rq\right\rceil,
\qquad
I_{R,q}:=\{m_R,\ldots,R-1\}.
\tag{2}
\]

For the raw innovations

\[
\widetilde D_j:=BD_j
=\frac{\zeta(s)}s\bigl(j^{1-s}-(j+1)^{1-s}\bigr),
\tag{3}
\]

and the actual Blaschke-deflated innovations `D_j`, define the visible Gram matrices

\[
\widetilde K_{R,q}
:=\bigl(\langle J_R\widetilde D_i,J_R\widetilde D_j\rangle\bigr)_{i,j\in I_{R,q}},
\qquad
K_{R,q}
:=\bigl(\langle J_RD_i,J_RD_j\rangle\bigr)_{i,j\in I_{R,q}}.
\tag{4}
\]

Let `\widetilde{\mathcal R}_{R,q}` and `\mathcal R_{R,q}` be their diagonal normalizations. Then:

1. for every pair of integers `1<=m<R`, not only for fixed-ratio bands,

\[
\boxed{
\det \widetilde K_{m,R}=\frac mR,
}
\tag{5}
\]

where `\widetilde K_{m,R}` is the raw Gram on indices `m,...,R-1`;

2. for each fixed `q` there is `c_q>0` such that

\[
\boxed{
\widetilde K_{R,q}\succeq c_q I
}
\tag{6}
\]

uniformly in `R`;

3. if `H_k=sum_{r<=k}1/r` and

\[
\Phi_q
:=
\sum_{k=1}^{q-1}
\frac{\log H_k}{k(k+1)},
\tag{7}
\]

then the raw normalized correlation entropy satisfies

\[
\boxed{
-\log\det\widetilde{\mathcal R}_{R,q}
=R\Phi_q+O_q(1).
}
\tag{8}
\]

Here `Phi_2=0`, while `Phi_q>0` for every `q>=3`;

4. under `(1)`, the actual and raw normalized determinant entropies differ by only a bounded amount,

\[
\boxed{
\left|
-\log\det\mathcal R_{R,q}
+\log\det\widetilde{\mathcal R}_{R,q}
\right|
=O_{A,q}(1).
}
\tag{9}
\]

Consequently, for every fixed `q>=3`,

\[
\boxed{
-\log\det\mathcal R_{R,q}
=R\Phi_q+O_{A,q}(1),
}
\tag{10}
\]

but the entire linear term is already present when `B=1`. The divergence of the uncentered fixed-ratio determinant is therefore **not an off-critical obstruction**. For `q=2`, `NB-090` supplies the sharper bounded dyadic calibration.

The fixed-ratio escape from `NB-090` is thus closed under `(1)`: source-specific information can only appear in a genuinely growing ratio `q=q(R)`, in an explicitly centered excess beyond the raw baseline with nonuniform depth, or in structure outside these visible contiguous-band Gram determinants.

## 1. The raw visible Gram has determinant exactly `m/R`

The Paley--Wiener representative from `NB-088` is

\[
\widetilde d_j(t)
=e^{-t/2}
\left[
 j\left\lfloor\frac{e^t}{j}\right\rfloor
-(j+1)\left\lfloor\frac{e^t}{j+1}\right\rfloor
\right].
\tag{11}
\]

Set `x=e^t`. On every integer cell `x in [n,n+1)`, define

\[
a_j(n)
:=
 j\left\lfloor\frac nj\right\rfloor
-(j+1)\left\lfloor\frac n{j+1}\right\rfloor.
\tag{12}
\]

Since

\[
\int_{\log n}^{\log(n+1)}e^{-t}\,dt
=\frac1{n(n+1)},
\tag{13}
\]

the raw Gram on `j=m,...,R-1` factors exactly as

\[
\widetilde K_{m,R}=A_{m,R}^*W_{m,R}A_{m,R},
\tag{14}
\]

where

\[
(A_{m,R})_{n,j}=a_j(n),
\qquad
W_{m,R}=\operatorname{diag}_{m\le n<R}\frac1{n(n+1)}.
\tag{15}
\]

The matrix `A_(m,R)` is lower triangular. Indeed `a_j(n)=0` for `n<j`, while

\[
a_j(j)=j.
\tag{16}
\]

Therefore

\[
\begin{aligned}
\det\widetilde K_{m,R}
&=
\left(\prod_{j=m}^{R-1}j^2\right)
\left(\prod_{n=m}^{R-1}\frac1{n(n+1)}\right)\\
&=
\prod_{n=m}^{R-1}\frac n{n+1}
=
\boxed{\frac mR}.
\end{aligned}
\tag{17}
\]

This identity is independent of zeta zeros and independent of any asymptotic approximation. It is a finite exact consequence of the natural integer-cell innovation flag.

## 2. Fixed-ratio raw bands are uniformly invertible

The constant determinant in `(17)` is not enough by itself: one could still hide a very small eigenvalue behind compensating large ones. For fixed ratio, the triangular arithmetic matrix admits a direct uniform inverse estimate.

For a coefficient vector `c=(c_j)_(m<=j<R)`, write

\[
F_n:=\sum_{j=m}^{n}c_j a_j(n),
\qquad m\le n<R.
\tag{18}
\]

Then

\[
\|F\|_W^2
:=
\sum_{n=m}^{R-1}\frac{|F_n|^2}{n(n+1)}
=c^*\widetilde K_{m,R}c.
\tag{19}
\]

Put

\[
b_m=c_m,
\qquad
b_k=c_k-c_{k-1}\quad(k>m).
\tag{20}
\]

If `h_k(n)=k floor(n/k)`, the telescoping relation `a_j=h_j-h_(j+1)` gives

\[
F_n=\sum_{k=m}^{n} k b_k\left\lfloor\frac nk\right\rfloor.
\tag{21}
\]

Hence, with `F_(m-1)=0`,

\[
G_n:=F_n-F_{n-1}
=
\sum_{\substack{k\mid n\\k\ge m}} k b_k.
\tag{22}
\]

Möbius inversion yields

\[
n b_n
=
\sum_{\substack{d\mid n\\n/d\ge m}}
\mu(d)G_{n/d},
\tag{23}
\]

and therefore

\[
c_j
=
\sum_{d\le j/m}\frac{\mu(d)}d
\sum_{r=m}^{\lfloor j/d\rfloor}
\frac{F_r-F_{r-1}}r.
\tag{24}
\]

The inner sum has the exact Abel form

\[
\sum_{r=m}^{M}\frac{F_r-F_{r-1}}r
=
\frac{F_M}{M}
+
\sum_{r=m}^{M-1}\frac{F_r}{r(r+1)}.
\tag{25}
\]

Now specialize to `m=m_R=ceil(R/q)`. In `(24)` only `d<=q` can occur. For each fixed `d`, the endpoint sequence `F_(floor(j/d))/floor(j/d)` has `ell^2` norm at most `C_d||F||_W`, because each index is repeated at most `d` times and `r^-2` is comparable with `[r(r+1)]^-1`. The second term in `(25)` obeys

\[
\left|
\sum_{r=m}^{M-1}\frac{F_r}{r(r+1)}
\right|
\le
\|F\|_W
\left(
\sum_{r=m}^{\infty}\frac1{r(r+1)}
\right)^{1/2}
=
\frac{\|F\|_W}{\sqrt m}.
\tag{26}
\]

There are fewer than `R` output indices and `R/m<=q`, so the `ell^2` norm of these tail terms is also `O_q(||F||_W)`. Summing the finitely many `d<=q` in `(24)` gives

\[
\|c\|_2\le C_q\|F\|_W.
\tag{27}
\]

Together with `(19)`, this proves `(6)` with `c_q=C_q^-2`.

This spectral floor is the fixed-ratio analogue of the explicit `1/2` floor found in `NB-090`. It is essential below: the exact determinant `(17)` alone would not control a perturbation determinant.

## 3. The raw correlation entropy has a universal linear rate for `q>=3`

The diagonal norms can also be read directly from the integer cells. Let

\[
k=\left\lfloor\frac{R-1}{j}\right\rfloor.
\tag{28}
\]

For all but at most one `j` for each fixed `k`, the cutoff `R` lies after the short `k`th spike, equivalently `R>=k(j+1)`. An elementary summation of the two values of `a_j(n)` on each quotient cell then gives

\[
\boxed{
\|J_R\widetilde D_j\|^2
=H_k-\frac{k^2}{R}.
}
\tag{29}
\]

The exceptional set has `O_q(1)` indices on `I_(R,q)`. By `(6)` all raw diagonal norms are uniformly bounded below there, so the exceptional logarithmic contribution is also `O_q(1)`.

For `1<=k<=q-1`, the number of indices in the regular part with `(28)` is

\[
\#\left\{j\in I_{R,q}:
\left\lfloor\frac{R-1}{j}\right\rfloor=k
\right\}
=
\frac{R}{k(k+1)}+O_q(1).
\tag{30}
\]

Since `k` is fixed,

\[
\log\left(H_k-\frac{k^2}{R}\right)
=
\log H_k+O_q(R^{-1}).
\tag{31}
\]

Thus

\[
\sum_{j\in I_{R,q}}
\log\|J_R\widetilde D_j\|^2
=
R\Phi_q+O_q(1),
\tag{32}
\]

with `Phi_q` from `(7)`. Using `(17)` with `m=m_R`,

\[
\log\det\widetilde K_{R,q}
=
\log\frac{m_R}{R}
=O_q(1).
\tag{33}
\]

Since diagonal normalization gives

\[
-\log\det\widetilde{\mathcal R}_{R,q}
=
-\log\det\widetilde K_{R,q}
+
\sum_{j\in I_{R,q}}
\log\|J_R\widetilde D_j\|^2,
\tag{34}
\]

equations `(32)`--`(33)` prove `(8)`.

For `q=2`, only `k=1` occurs and `H_1=1`, so `Phi_2=0`; `NB-090` computes the sharper finite limit `log 2-1/2`. For every `q>=3`, the `k=2` term alone has `log H_2>0`, hence

\[
\Phi_q>0.
\tag{35}
\]

Therefore widening from the dyadic band creates **linear normalized Gram entropy even on the raw `B=1` branch**. Any use of that divergence as an off-critical signal must first subtract this universal baseline.

## 4. Summable horizontal zero mass changes a fixed-ratio band by only bounded determinant excess

The Volterra estimate in `NB-089` was written on the dyadic relative horizon `log 2`, but its proof is uniform on every **fixed** horizon. Here every `j in I_(R,q)` satisfies

\[
0\le \log(R/j)\le\log q+o(1).
\tag{36}
\]

On the physical variable `x=e^t`, the raw profile `(11)` has

\[
\|J_R\widetilde D_j\|_{L^1(dt)}
=
\int_j^R
|a_j(x)|x^{-3/2}\,dx
\ll_q j^{-1/2}.
\tag{37}
\]

Indeed, on `x<=qj` the two floors in `(12)` differ by at most one for large `j`. Away from their `O_q(1)` short mismatch intervals, `a_j(x)=O_q(1)`; the mismatch intervals have total physical length `O_q(1)` and amplitude `O(j)`. Both contributions to `(37)` are `O_q(j^-1/2)`.

For one off-critical Blaschke zero `lambda` with `a=Re lambda>0`, finite-horizon division is the same causal Volterra operator as in `NB-089`,

\[
T_\lambda f(u)
=
f(u)+2a\int_0^u e^{\lambda(u-v)}f(v)\,dv.
\tag{38}
\]

Repeating the `NB-089` iteration with `L=log q+1` and total mass `(1)` gives, uniformly for `j in I_(R,q)`,

\[
D_j=\widetilde D_j+r_j
\quad\text{on the visible prefix},
\qquad
\|r_j\|_\infty
\ll_{A,q}j^{-1/2}.
\tag{39}
\]

Together with `(37)`, this implies for all `i,j in I_(R,q)`

\[
\boxed{
\left|
(K_{R,q})_{ij}-(\widetilde K_{R,q})_{ij}
\right|
\ll_{A,q}R^{-1}.
}
\tag{40}
\]

Causal inner multiplication supplies more than entrywise control. Since

\[
M_BD_j=\widetilde D_j
\tag{41}
\]

and `J_R M_B J_R` is a contraction,

\[
\boxed{
K_{R,q}\succeq\widetilde K_{R,q}.
}
\tag{42}
\]

Set `E_(R,q)=K_(R,q)-\widetilde K_(R,q)`. Equations `(40)` and `(42)` give

\[
E_{R,q}\succeq0,
\qquad
\operatorname{tr}E_{R,q}=O_{A,q}(1).
\tag{43}
\]

Using the spectral floor `(6)`, put

\[
H_{R,q}
:=
\widetilde K_{R,q}^{-1/2}
E_{R,q}
\widetilde K_{R,q}^{-1/2}
\succeq0.
\tag{44}
\]

Then

\[
\begin{aligned}
0
&\le
\log\det K_{R,q}-\log\det\widetilde K_{R,q}\\
&=
\log\det(I+H_{R,q})\\
&\le
\operatorname{tr}H_{R,q}
\le
c_q^{-1}\operatorname{tr}E_{R,q}
=O_{A,q}(1).
\end{aligned}
\tag{45}
\]

The same argument on the diagonal is simpler. From `(40)`, `(42)` and `(6)`,

\[
0\le
\sum_{j\in I_{R,q}}
\log\frac{(K_{R,q})_{jj}}{(\widetilde K_{R,q})_{jj}}
=O_{A,q}(1).
\tag{46}
\]

Subtracting the log-determinant change `(45)` from the diagonal-normalization change `(46)` proves `(9)`.

The crucial point is that the perturbation may affect `O(R^2)` Gram entries, yet positivity and the `O(1)` **trace** budget reduce its total determinant effect to `O(1)`. No entrywise determinant expansion is being used.

## 5. Consequence: fixed depth is the wrong asymptotic carrier

For `q=2`, `NB-090` already shows that the full terminal determinant entropy is bounded under `(1)`. For every fixed `q>=3`, `(10)` shows linear divergence, but `(8)` proves that exactly the same leading term occurs on the raw RH calibration `B=1`. Thus moving from depth `2` to any other fixed multiplicative depth does not recover source discrimination.

Equivalently, the centered quantity

\[
\mathcal E_{R,q}
:=
-\log\det\mathcal R_{R,q}
+
\log\det\widetilde{\mathcal R}_{R,q}
\tag{47}
\]

obeys

\[
\boxed{
|\mathcal E_{R,q}|=O_{A,q}(1)
}
\tag{48}
\]

for every fixed `q`. A proof strategy based on these contiguous visible Gram bands must therefore leave the fixed-ratio regime if it wants an unbounded off-critical signal under summable horizontal mass.

This identifies a sharper live target than the generic "use nonterminal scales" left by `NB-090`: one must either let `q=q(R)` grow and control the loss of the constants in `(6)`, `(37)` and `(39)`, or build an inter-scale statistic that does not reduce to a single fixed-ratio band determinant. The first option asks for a genuinely **nonuniform horizon** estimate for the Blaschke delay; the second asks for coupling between bands rather than more information inside one band.

## 6. Prior-art and adversarial boundary

The determinant identity `(17)`, the fixed-ratio inverse estimate `(27)`, and the calibrated entropy conclusion `(48)` are derived directly from the canonical Nyman innovation flag. No specialized external theorem is load-bearing. The literature audit rechecked recent Gram-structure work including Hugh Carvill's Mellin-smoothed multiplicative ladder and Alouges--Darses--Hillion's generalized Nyman--Beurling Gram structures. Those objects use different families or smoothing/randomization and do not supply the exact natural consecutive-band factorization `(14)`--`(17)` or the fixed-ratio calibrated conclusion above. No priority claim is made.

The main stress tests are explicit. First, `(1)` is conditional and substantially stronger than the ordinary half-plane Blaschke condition; the finding does not assert it under false RH. Second, `q` is fixed throughout. Every useful constant may deteriorate with `q`, so `(48)` gives no control when `q=q(R)->infinity`; that is precisely the remaining frontier. Third, the linear entropy in `(10)` is **not** claimed as arithmetic information: it is the universal diagonal-normalization cost `(32)` already present for `B=1`. Fourth, the exact determinant `(17)` is an unnormalized Gram identity and must not be confused with a correlation determinant. Fifth, the spectral floor `(6)` is proved separately because a bounded determinant alone would not exclude a hidden near-kernel direction. Finally, the Volterra argument is confined to the finite relative horizon `log q`; it does not assert a global inverse bound for `1/B` on Hardy space.
