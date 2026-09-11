# NB-053 — after Blaschke deflation repair defect is purely off-grid semigroup leakage

**Status:** `EXACT-DERIVED + CORRECTED-HARDY-DOMAIN + LITERATURE-BOUNDED + DISCRETE-SEMIGROUP-INVARIANCE + TWO-GENERATOR-CONTINUOUS-HULL + LARGE-SHIFT-LEAKAGE-DECAY + NEGATIVE/METHOD-BOUNDARY`.

`NB-052` removes Burnol's common Blaschke factor from the weighted-repair comparison and leaves the target defect

\[
\Delta_*=B(1)^2\delta_{\rm def}^2,
\qquad
\delta_{\rm def}=\operatorname{dist}(k_1,\mathcal A_{\rm nat}),
\qquad
k_1(s)=\frac1s,
\tag{1}
\]

inside

\[
\mathcal H^2=H^2(\Re s>1/2),
\qquad
\mathcal A_{\rm nat}=\overline{\operatorname{span}}\{\phi_{1/n}:n\ge2\},
\tag{2}
\]

where

\[
\phi_\theta(s)=\frac{1}{B(s)}\widehat{\rho_\theta}(s)
=O(s)\frac{\theta-\theta^s}{s-1},
\qquad
O(s)=\frac{s-1}{s}\frac{\zeta(s)}{B(s)}.
\tag{3}
\]

The durable content of this finding is the semigroup structure of the **actual Hardy vectors** `phi_theta` and of the orthogonal defect. Let

\[
(U_tF)(s)=e^{-t(s-1/2)}F(s),\qquad t\ge0.
\tag{4}
\]

Then:

\[
\boxed{U_{\log m}\mathcal A_{\rm nat}\subseteq\mathcal A_{\rm nat}\qquad(m\ge2),}
\tag{5}
\]

while two multiplicatively independent natural generators already have full continuous-shift hull,

\[
\boxed{\overline{\operatorname{span}}\{U_t\phi_{1/2},U_t\phi_{1/3}:t\ge0\}=\mathcal H^2.}
\tag{6}
\]

Consequently, if `P=P_(A_nat)` and `h in A_nat^perp`, then

\[
\boxed{P U_{\log n}^*h=0\qquad(n\ge1),}
\tag{7}
\]

and for every fixed such `h`,

\[
\boxed{\sup_{t\ge T}\|P U_t^*h\|\longrightarrow0\qquad(T\to\infty).}
\tag{8}
\]

If `h!=0`, however, (6) forces `P U_t^*h!=0` for at least one off-grid `t`. Thus the deflated closure defect is invisible on the logarithmic integer grid, visible somewhere off that grid, and asymptotically invisible at large shifts **for each fixed witness**. The result is vectorwise; it is not the false operator-norm assertion `||P U_t^*P_(A_nat^perp)||->0`.

A correction is load-bearing here. An earlier version of this finding also asserted that `O in H^2` and used that premise to claim `phi_(e^-a)/a -> O` in `H^2`. That premise is false: Burnol's Hardy function is the additionally regularized factor `O(s)/s`, while `O` itself has critical-line magnitude comparable to `|zeta(1/2+it)|` and is not square-integrable. Those small-shift statements are withdrawn. `NB-055` gives the correct `H^2` regularization and replaces the dependent tail argument.

## 1. Integer-log invariance is exact

For `n>=2` write

\[
q_n(s)=\frac{n^{-1}-n^{-s}}{s-1},\qquad \phi_{1/n}=Oq_n.
\tag{9}
\]

For integers `m,n>=2`,

\[
q_{mn}(s)=n^{-1}q_m(s)+m^{-s}q_n(s).
\tag{10}
\]

Multiplying by `O` and using `U_(log m)F=m^(1/2-s)F` gives

\[
\boxed{U_{\log m}\phi_{1/n}=\sqrt m\left(\phi_{1/(mn)}-n^{-1}\phi_{1/m}\right).}
\tag{11}
\]

The right side is in the algebraic natural span. Density and boundedness of `U_(log m)` prove (5). This is the deflated form of the classical multiplicative-semigroup covariance; no novelty is claimed for the covariance itself.

## 2. Two natural generators have full continuous hull

Because `O` is outer in Burnol's factorization, the inner divisor of `phi_(1/n)=Oq_n` is the inner divisor of `q_n`. Away from the removable point `s=1`,

\[
q_n(s)=0
\iff n^{-(s-1)}=1,
\tag{12}
\]

so

\[
Z(q_n)=\left\{1+\frac{2\pi i k}{\log n}:k\in\mathbb Z\setminus\{0\}\right\}.
\tag{13}
\]

The functions `q_2` and `q_3` have no common zero: a common zero would make `log 2/log 3` rational and hence force `2^a=3^b` for nonzero integers `a,b`. They also have no common singular or exponential inner divisor. The Beurling--Lax theorem therefore makes their greatest common inner divisor constant and yields (6).

Before deflation the same statement reads

\[
\overline{\operatorname{span}}\{U_t\widehat{\rho_{1/2}},U_t\widehat{\rho_{1/3}}:t\ge0\}=B\mathcal H^2,
\tag{14}
\]

so after the common zeta-zero obstruction is divided out there is no second common inner obstruction hidden in the natural family. The remaining difference from the continuous Nyman closure is in the available shift times, not in a further shared spectral factor.

## 3. Orthogonal defects are blind on `log N` and decay off-grid vectorwise

Take `h in A_nat^perp`. Integer-log invariance gives

\[
U_{\log n}^*h\in\mathcal A_{\rm nat}^\perp,
\tag{15}
\]

which is (7). For large `t`, put

\[
n=\lfloor e^t\rfloor,
\qquad a=\log n,
\qquad \delta=t-a.
\tag{16}
\]

Then

\[
0\le\delta<\log\left(1+\frac1n\right).
\tag{17}
\]

Since `P U_a^*h=0`, the semigroup property and contractivity give

\[
\|P U_t^*h\|
\le\|U_\delta^*h-h\|.
\tag{18}
\]

For the fixed vector `h`, define

\[
\omega_h(r)=\sup_{0\le u\le r}\|U_u^*h-h\|.
\tag{19}
\]

Strong continuity gives `omega_h(r)->0`. Hence

\[
\sup_{t\ge T}\|P U_t^*h\|
\le
\omega_h\!\left(\log\left(1+\frac1{\lfloor e^T\rfloor}\right)\right)
\longrightarrow0,
\tag{20}
\]

proving (8). This argument is deliberately not uniform on the unit sphere; the right-shift semigroup is not norm-continuous at zero.

If a nonzero `h in A_nat^perp` also obeyed `P U_t^*h=0` for every `t>=0`, it would be orthogonal to the continuous invariant hull of `A_nat`. Equation (6) makes that hull all of `H^2`, so `h=0`, a contradiction. Every nonzero defect must therefore be detected at some finite off-grid shift.

For the canonical target residual

\[
h_*=k_1-Pk_1,
\qquad \|h_*\|=\delta_{\rm def},
\tag{21}
\]

this shows that a nonzero `NB-052` repair defect is a finite/moderate-scale off-grid co-invariance defect. Merely pushing a fixed probe to larger and larger dilation scales cannot reveal it persistently.

## 4. Hardy-domain correction and surviving finite-section bridge

The former small-shift argument used

\[
O(s)=\frac{s-1}{s}\frac{\zeta(s)}{B(s)}
\tag{22}
\]

as though `O` were a vector of `H^2`. It is not. On the critical boundary `|B|=1` almost everywhere and `|(s-1)/s|` tends to one, while the classical second moment of `zeta(1/2+it)` diverges like `T log T`. Thus `O` has infinite Hardy boundary norm. In particular, the previous assertions

\[
\phi_{e^{-a}}/a\to O\quad\text{in }H^2
\tag{23}
\]

and the interpretation that the first off-grid finite-grid column converges to an `H^2` outer seed are invalid and are withdrawn.

This correction does **not** affect Sections 1--3: they use `phi_(1/n)`, `q_n`, and fixed vectors `h in H^2`, not `O` as an ambient Hardy vector. It does affect any argument that Bochner-integrates the orbit `U_tO` or invokes a norm-continuity modulus for that orbit. `NB-055` repairs exactly that domain error by replacing `O` with

\[
E(s)=\frac{O(s)}s=\frac{s-1}{s^2}\frac{\zeta(s)}{B(s)}\in H^2,
\tag{24}
\]

and derives the correct logarithmic-cell recurrence and finite-grid raw-tail bounds.

The live finite-section question therefore remains scale-coupled. Canonical finite residuals are orthogonal only to their own finite section, not to `A_nat`; (20) cannot be transferred to them without a quantitative correction term. A useful theorem must control moderate/off-grid finite-section geometry from source-visible data without inserting the unknown full projector, `d_N`, or an equivalent RH-sensitive oracle.

## 5. Prior-art boundary

Burnol's Mellin formula, Blaschke/outer factorization, and Beurling--Lax description of the continuous closure are classical and remain the load-bearing external inputs. Bagchi and the classical Nyman--Báez-Duarte formulation provide the multiplicative-semigroup viewpoint. Work on orthogonality and shift invariance of natural Nyman spaces also makes clear that semigroup invariance itself is not a new mechanism.

The line-local contribution retained here is narrower: after the exact deflation in `NB-052`, the natural space is exactly invariant at integer-log times, two multiplicatively independent natural generators already recover the full continuous hull, and every fixed orthogonal defect is forced into the off-grid finite/moderate-scale channel with large-shift leakage tending to zero. No estimate of `delta_def`, `Delta_*`, or `d_N` follows, and no RH implication is asserted.