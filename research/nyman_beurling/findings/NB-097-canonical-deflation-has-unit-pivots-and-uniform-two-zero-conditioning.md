# NB-097 — canonical deflation has unit pivots and uniform two-zero conditioning

**Status:** `EXACT-DERIVED + ACTUAL-NYMAN-SOURCE + FINITE-DISTINCT-OFF-CRITICAL-DIVISOR + HALF-LINE-STATE-GEOMETRY + UNIT-CHOLESKY-PIVOTS + UNIFORM-TWO-ZERO-CONDITIONING`.

`NB-096` proves that for every fixed finite ordered set of distinct right-half zeta zeros, the determinant collapse of the raw Cauchy state Gram is cancelled exactly by the determinant growth of the canonical triangular Blaschke-deflation coordinates. That leaves open whether the same zero crowding can reappear immediately as a small singular value after the determinant cancellation.

At the half-line limiting level the canonical coordinates have more structure than their determinant alone records. Every **leading principal pivot is exactly one**. In particular, for two distinct zero states the entire canonically transformed Gram can be written as a unit triangular shear whose shear coefficient has modulus at most `2`. Hence its spectrum is bounded by absolute constants, uniformly over the zero locations and uniformly through an arbitrarily close distinct-zero collision.

For the notation of `NB-095`--`NB-096`, let

\[
F=(\rho_1,\ldots,\rho_d),
\qquad
\lambda_r=\rho_r-\frac12,
\qquad
a_r=\Re\lambda_r>0,
\]

let

\[
G_F(\infty)_{rs}
=\frac{2\sqrt{a_ra_s}}
{\lambda_r+\overline{\lambda_s}},
\]

and let `T_F` be the exact upper-triangular canonical-deflation matrix satisfying `S_R=U_RT_F`. Define the limiting interacting-state matrix

\[
\boxed{
C_F:=T_F^*G_F(\infty)T_F.
}
\tag{1}
\]

Then:

1. every leading principal minor of `C_F` equals `1`;
2. equivalently, the Cholesky factorization has the form

\[
\boxed{
C_F=R_F^*R_F,
\qquad
R_F\ \text{upper triangular},
\qquad
(R_F)_{kk}=1;
}
\tag{2}
\]

3. if `d=2`, then

\[
\boxed{
(3-2\sqrt2)I
\preceq C_F
\preceq
(3+2\sqrt2)I,
}
\tag{3}
\]

and therefore

\[
\boxed{
\kappa_2(C_F)
\le
\frac{3+2\sqrt2}{3-2\sqrt2}
=(3+2\sqrt2)^2
=17+12\sqrt2.
}
\tag{4}
\]

Thus isolated pairwise crowding does **not** create an unbounded spectral-conditioning penalty after canonical deflation. Any unbounded conditioning in a growing zero divisor must be genuinely collective -- growth of the unit-triangular shear with dimension -- or must enter through the finite-window/discretization and diagonal-normalization layers that are absent from `(1)`.

## 1. Prefix cancellation forces every canonical pivot to equal one

Fix the deflation order and write

\[
F_k=(\rho_1,\ldots,\rho_k).
\]

Because `T_F` is upper triangular and the `k`th causal state uses only the first `k` raw zero states, the upper-left `k x k` block of `T_F` is exactly the canonical matrix `T_(F_k)` obtained by stopping the same deflation after `k` factors. Likewise, the upper-left block of `G_F(infinity)` is `G_(F_k)(infinity)`. Hence

\[
(C_F)_{1:k,1:k}
=
T_{F_k}^*G_{F_k}(\infty)T_{F_k}.
\tag{5}
\]

`NB-096` applies to every prefix and gives

\[
|\det T_{F_k}|^2\det G_{F_k}(\infty)=1.
\]

Therefore

\[
\boxed{
\det (C_F)_{1:k,1:k}=1
\qquad(1\le k\le d).
}
\tag{6}
\]

Since `C_F` is positive definite, its unpivoted `LDL^*` pivots are the ratios of consecutive leading principal minors. Equation `(6)` gives

\[
D_{kk}
=
\frac{
\det(C_F)_{1:k,1:k}
}{
\det(C_F)_{1:k-1,1:k-1}
}
=1.
\tag{7}
\]

Thus `D=I`, proving `(2)`. The determinant cancellation of `NB-096` is therefore not only a final-volume identity: **no sequential Schur pivot loses volume at any finite prefix**. What can still become large is the shear in the unit-triangular factor `R_F`.

This distinction is important. Unit pivots alone do not bound a high-dimensional condition number: an arbitrary unit-triangular matrix may have very large off-diagonal entries. So `(2)` does not solve the growing-divisor problem. It does, however, identify the only half-line spectral resource that remains: collective shear rather than collapsing pivots.

## 2. The two-zero canonical matrix is an explicit unit shear

Now take `d=2`. Put

\[
\lambda_r=a_r+i\gamma_r,
\qquad
\Delta:=\lambda_2-\lambda_1,
\qquad
h:=\lambda_2+\overline{\lambda_1},
\qquad
r:=2\sqrt{a_1a_2}.
\tag{8}
\]

The raw half-line Gram is

\[
G_2(\infty)
=
\begin{pmatrix}
1 & r/\overline h\\
r/h & 1
\end{pmatrix}.
\tag{9}
\]

The second canonical state can be read directly from the one-factor inverse filter. Since

\[
\frac1{b_1(z)}
=1+\frac{2a_1}{z-\lambda_1},
\]

its time-domain input before removal of the second factor is

\[
x_{1,j}(t)
=
\widetilde d_j(t)
+2a_1\int_0^t
 e^{\lambda_1(t-v)}\widetilde d_j(v)\,dv.
\tag{10}
\]

For the finite-time state functional at `lambda_2`, Fubini on `0<=v<=t<=T` gives

\[
\int_v^T
 e^{\lambda_2(T-t)}e^{\lambda_1(t-v)}\,dt
=
\frac{
 e^{\lambda_2(T-v)}-e^{\lambda_1(T-v)}
}{\lambda_2-\lambda_1}.
\tag{11}
\]

Using the raw state normalizations from `NB-095`, `(11)` yields exactly

\[
s^{(2)}
=
-\frac{2\sqrt{a_1a_2}}{\lambda_2-\lambda_1}u^{(1)}
+
\frac{\lambda_2+\overline{\lambda_1}}
     {\lambda_2-\lambda_1}u^{(2)}.
\tag{12}
\]

Hence

\[
\boxed{
T_2=
\begin{pmatrix}
1 & -r/\Delta\\
0 & h/\Delta
\end{pmatrix}.
}
\tag{13}
\]

Multiplying `(9)` and `(13)`, the first canonical coordinate still has norm one and the off-diagonal entry is

\[
\chi
:=(C_2)_{12}
=
\frac{r(h-\overline h)}
{\Delta\,\overline h}
=
\frac{
4i\sqrt{a_1a_2}(\gamma_2-\gamma_1)
}{
(\lambda_2-\lambda_1)
(\lambda_1+\overline{\lambda_2})
}.
\tag{14}
\]

By `(6)`, `det C_2=1`. Therefore

\[
\boxed{
C_2
=
\begin{pmatrix}
1 & \chi\\
\overline\chi & 1+|\chi|^2
\end{pmatrix}
=
\begin{pmatrix}1&\chi\\0&1\end{pmatrix}^{\!*}
\begin{pmatrix}1&\chi\\0&1\end{pmatrix}.
}
\tag{15}
\]

So the entire two-zero conditioning question has reduced to one scalar shear.

## 3. The shear is universally bounded, even at distinct-zero collision

Let

\[
\omega:=\gamma_2-\gamma_1.
\]

Equation `(14)` gives

\[
|\chi|^2
=
\frac{
16a_1a_2\omega^2
}{
\bigl((a_2-a_1)^2+\omega^2\bigr)
\bigl((a_1+a_2)^2+\omega^2\bigr)
}.
\tag{16}
\]

The denominator satisfies

\[
\bigl((a_2-a_1)^2+\omega^2\bigr)
\bigl((a_1+a_2)^2+\omega^2\bigr)
\ge
\omega^2(a_1+a_2)^2
\ge
4a_1a_2\omega^2.
\]

Thus

\[
\boxed{|\chi|\le2.}
\tag{17}
\]

For a matrix of the form `(15)`, the eigenvalues are

\[
\lambda_\pm
=
1+\frac{|\chi|^2}{2}
\pm
\frac12\sqrt{|\chi|^2(|\chi|^2+4)},
\qquad
\lambda_+\lambda_-=1.
\tag{18}
\]

They are monotone in `|chi|`, so `(17)` gives `(3)`--`(4)`.

The bound passes the relevant edge tests sharply. If the two zeros have the same ordinate, `omega=0`, then `chi=0` and

\[
C_2=I
\tag{19}
\]

**exactly**, no matter how close their real parts are. For a tangential near-collision with `a_1=a_2=a` and nonzero `omega->0`,

\[
|\chi|^2
=
\frac{16a^2}{4a^2+\omega^2}
\longrightarrow4,
\]

so

\[
\lambda_\pm\longrightarrow3\pm2\sqrt2.
\tag{20}
\]

Thus the constant in `(3)` is the correct universal two-state endpoint. At large vertical separation, `|chi|->0` and the canonical states again approach orthogonality.

This also shows why the determinant-only warning in `NB-096` was necessary but not yet sharp. Canonical deflation is generally **not** the Takenaka--Malmquist orthogonalizing transform: `chi` need not vanish. Nevertheless, the possible two-state nonorthogonality is uniformly limited; the reciprocal Cauchy determinant blow-up in `T_2` cancels not only at volume level but strongly enough to prevent a small spectral mode.

## 4. What remains for a growing divisor

The prefix identity `(6)` rules out a second possible failure mode. The growing-family problem cannot be explained by a sequence of vanishing canonical Schur pivots. Every pivot is identically one. And `(17)` rules out an isolated close pair as a source of unbounded half-line condition number.

The remaining half-line question is therefore genuinely many-body:

\[
\boxed{
\text{control the unit-triangular shear }R_F
\text{ as }|F|\to\infty.
}
\tag{21}
\]

A dimension-dependent bound on `||R_F||` and `||R_F^{-1}||` that is insensitive to pseudo-hyperbolic separation would remove raw zero crowding from the spectral frontier entirely; a counterexample would have to exhibit collective amplification involving at least three states. Even such a bound would still leave the other nonuniformities already isolated by `NB-096`: replacing the half-line Gram by the finite-window `G_F(q)`, making the `O_F(m^-1)` discretization uniform, controlling the accumulated diagonal-normalization cost, and finally converting generator-state geometry into a target-relevant Nyman obstruction.

The exact multiple-zero/confluent case also remains separate. The distinct two-zero matrix has bounded but path-dependent collision limits -- `(19)` and `(20)` are already different -- so one cannot infer the repeated-factor state law merely by taking `lambda_2->lambda_1`. A genuine multiple zeta zero requires the confluent/Jordan causal system and the corresponding source derivative cancellations.

## 5. Prior-art boundary

The surrounding Hardy-space geometry is classical. Takenaka--Malmquist systems arise by Gram--Schmidt orthogonalization of shifted Cauchy/Szego kernels and admit closed forms involving finite Blaschke products; a targeted audit found this standard boundary again in the modern Malmquist--Takenaka literature. That classical orthogonalization explains why normalized kernel crowding is naturally paired with Blaschke factors, but it does not identify the canonical Nyman causal-deflation coordinates `T_F`, which are generally not the orthogonalizing coordinates as `(14)`--`(15)` make explicit.

No external estimate is used in `(6)` or `(12)`--`(20)`: they follow from the exact interaction law of `NB-095`, the exact determinant cancellation of `NB-096`, and elementary two-state algebra. The contemporary Nyman/Blaschke prior-art boundary recorded in `SOURCES.md` therefore remains sufficient; no new source is load-bearing.

The line-level consequence is a sharper spectral frontier. `NB-096` removed raw Cauchy **volume** crowding. `NB-097` now shows that canonical half-line deflation also has no pivot collapse and no unbounded **two-state** crowding penalty. If spectral conditioning is where the growing-divisor argument breaks, it must appear through collective unit-triangular shear, finite-window resolution, or one of the later normalization/target-conversion layers -- not through the raw separation of a single pair.