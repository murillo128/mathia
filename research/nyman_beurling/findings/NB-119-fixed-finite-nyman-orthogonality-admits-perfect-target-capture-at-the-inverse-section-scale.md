# NB-119 — fixed finite Nyman orthogonality admits perfect target capture at the inverse-section scale

**Status:** `EXACT-DERIVED + MATCHED-CONTROL + NB-118-SHARP-ORDER + PERIODIC-TAIL-GRAM + PERFECT-VISIBLE-TARGET-CAPTURE + REPRESENTATION-AUDIT`.

`NB-118` shows that every finite packet of actual zeta-zero powers with target capture above a fixed finite Nyman baseline must hide all but `O_M(1/R)` of its continuum norm in the first `R` natural cells. That estimate uses only the fixed source equations

\[
\langle f,g_b\rangle=0,
\qquad 2\le b\le M.
\tag{1}
\]

The natural next question is whether those same equations can force a smaller visible fraction, for example `o(1/R)`, once the target alignment is very strong. They cannot. For every fixed `M`, the finite source equations themselves admit an exact matched control whose visible part is **exactly the target** and whose retained fraction is asymptotic to a positive constant times `1/R`.

More precisely, let

\[
V_M=\operatorname{span}\{g_2,\ldots,g_M\},
\qquad
\mathcal E_R=\operatorname{span}\{\psi_n:1\le n<R\},
\qquad
Q_R=P_{\mathcal E_R},
\qquad
e_R=Q_Re,
\tag{2}
\]

and put `L_R=||e_R||^2=1-1/R` as in `NB-118`. For every fixed `M>=2`, there are vectors `f_(M,R) in V_M^perp` for all sufficiently large `R` such that

\[
Q_Rf_{M,R}=e_R,
\qquad
q_R(f_{M,R})=1,
\tag{3}
\]

while

\[
\boxed{
\frac{\|Q_Rf_{M,R}\|^2}{\|f_{M,R}\|^2}
=
\frac{1}{\kappa_M R}+O_M(R^{-2}),
}
\tag{4}
\]

for an explicit constant `kappa_M>0`. The tail used to enforce `(1)` is the unique minimum-norm repair of the perfect visible target and has squared norm

\[
\boxed{
\|(I-Q_R)f_{M,R}\|^2
=
\kappa_M R+O_M(1).
}
\tag{5}
\]

Thus the inverse-section scale in `NB-118` is sharp in order under fixed finite Nyman orthogonality alone. Any theorem excluding actual zero-power rescue at that scale must use information not shared by this matched control: the confluent zero-power form from `NB-117`, source coherence that grows with `M`, simultaneous information across cutoffs, or another genuinely source-specific constraint.

## 1. The tail Gram matrix has an exact periodic first-order law

On the `n`th natural cell, `NB-118` uses

\[
\langle g_b,\psi_n\rangle
=
\frac{\{n/b\}}{\sqrt{n(n+1)}}.
\tag{6}
\]

Write

\[
h_{b,R}:=(I-Q_R)g_b,
\qquad 2\le b\le M,
\tag{7}
\]

and let `Gamma_(M,R)` be their tail Gram matrix,

\[
\Gamma_{M,R}(i,j)
=
\langle h_{i,R},h_{j,R}\rangle
=
\sum_{n\ge R}
\frac{\{n/i\}\{n/j\}}{n(n+1)}.
\tag{8}
\]

Let

\[
L=\operatorname{lcm}(2,\ldots,M)
\tag{9}
\]

and define the periodic mean Gram matrix

\[
C_M(i,j)
:=
\frac1L\sum_{r=1}^{L}
\{r/i\}\{r/j\},
\qquad 2\le i,j\le M.
\tag{10}
\]

For any fixed periodic sequence `u_n` of mean `mu`, bounded partial sums of `u_n-mu` and summation by parts give

\[
\sum_{n\ge R}\frac{u_n}{n(n+1)}
=
\frac{\mu}{R}+O_u(R^{-2}).
\tag{11}
\]

Applying `(11)` entrywise to `(8)` yields

\[
\boxed{
\Gamma_{M,R}
=
\frac{C_M}{R}+O_M(R^{-2}).
}
\tag{12}
\]

The matrix `C_M` is positive definite. Indeed, suppose

\[
\sum_{b=2}^{M}c_b\{n/b\}=0
\tag{13}
\]

for every residue `n mod L`. Put `A=sum_(b=2)^M c_b/b`. Taking the first difference of `(13)` gives

\[
A-
\sum_{\substack{2\le b\le M\\ b\mid n}}c_b
=0
\tag{14}
\]

for every integer `n`. At `n=1`, `(14)` gives `A=0`. At `n=2` it gives `c_2=0`, and induction on `n=3,...,M` then gives `c_n=0`, because every proper divisor coefficient has already vanished. Hence the periodic functions `{n/b}`, `2<=b<=M`, are linearly independent, so

\[
C_M>0.
\tag{15}
\]

Consequently `Gamma_(M,R)` is invertible for all sufficiently large `R`, with

\[
\Gamma_{M,R}^{-1}
=
R C_M^{-1}+O_M(1).
\tag{16}
\]

## 2. Perfect visible target alignment has an exact minimum-norm tail repair

Define the finite head correlation vector

\[
a_{M,R}(b):=\langle e_R,g_b\rangle,
\qquad 2\le b\le M.
\tag{17}
\]

The classical target correlation already used throughout the Nyman line is

\[
\langle e,g_b\rangle=\frac{\log b}{b}.
\tag{18}
\]

Since the omitted cell tail in `(17)` is `O_M(1/R)`, if

\[
a_M:=\left(\frac{\log b}{b}\right)_{b=2}^{M},
\tag{19}
\]

then

\[
a_{M,R}=a_M+O_M(R^{-1}).
\tag{20}
\]

Let

\[
\lambda_{M,R}:=\Gamma_{M,R}^{-1}a_{M,R},
\qquad
y_{M,R}:=-\sum_{b=2}^{M}\lambda_{M,R}(b)h_{b,R},
\tag{21}
\]

and set

\[
f_{M,R}:=e_R+y_{M,R}.
\tag{22}
\]

The vector `y_(M,R)` lives entirely beyond the cutoff. For each `2<=i<=M`, equations `(17)` and `(21)` give

\[
\langle f_{M,R},g_i\rangle
=
\langle e_R,g_i\rangle
+
\langle y_{M,R},h_{i,R}\rangle
=0.
\tag{23}
\]

Thus `f_(M,R) in V_M^perp`, while its visible part is untouched:

\[
Q_Rf_{M,R}=e_R.
\tag{24}
\]

In particular the `NB-118` target angle is exactly maximal,

\[
q_R(f_{M,R})=1.
\tag{25}
\]

Moreover `(21)` is not merely one possible repair. Among all tail vectors `y in (I-Q_R)H` satisfying

\[
\langle y,h_{b,R}\rangle=-a_{M,R}(b),
\qquad2\le b\le M,
\tag{26}
\]

it is the unique minimum-norm solution in the span of the tail generators, and every additional component orthogonal to that span only increases the norm. Therefore

\[
\boxed{
\|y_{M,R}\|^2
=
a_{M,R}^{*}\Gamma_{M,R}^{-1}a_{M,R}.
}
\tag{27}
\]

Define the positive constant

\[
\boxed{
\kappa_M:=a_M^{*}C_M^{-1}a_M>0.
}
\tag{28}
\]

Using `(16)` and `(20)` in `(27)` gives

\[
\|y_{M,R}\|^2
=
\kappa_M R+O_M(1).
\tag{29}
\]

Because the head and tail are orthogonal and `||e_R||^2=L_R`, equations `(24)` and `(29)` now give

\[
\frac{\|Q_Rf_{M,R}\|^2}{\|f_{M,R}\|^2}
=
\frac{L_R}{L_R+\|y_{M,R}\|^2}
=
\frac1{\kappa_M R}+O_M(R^{-2}),
\tag{30}
\]

which proves `(4)`--`(5)`.

## 3. The first source equation already saturates the scale explicitly

For `M=2`, the periodic sequence `{n/2}` alternates between `1/2` and `0`, so

\[
C_2=\frac18,
\qquad
a_2=\frac{\log2}{2}.
\tag{31}
\]

Hence

\[
\boxed{
\kappa_2=2(\log2)^2\approx0.960906,
}
\tag{32}
\]

and the matched control obeys

\[
R\,
\frac{\|Q_Rf_{2,R}\|^2}{\|f_{2,R}\|^2}
\longrightarrow
\frac1{2(\log2)^2}
\approx1.040684.
\tag{33}
\]

So even the single exact parity/Nyman equation from `NB-118` permits perfect visible target alignment at precisely inverse-section retention. Adding any fixed number of further Nyman equations changes the constant `kappa_M`, but not the `1/R` exponent.

As a regression check, direct finite-cell evaluation for `M=2,3,5` converges to `(29)`--`(30)`, and the periodic matrices `C_M` are numerically positive definite for the tested range `2<=M<=10`. These computations are not used in the proof; `(11)` and `(13)`--`(15)` give the exact fixed-`M` argument.

## 4. Representation audit: fixed finite source truth is saturated

The carrier here is the natural-cell split already used by `NB-117`--`NB-118`. No new arithmetic source information is inserted. The matched control preserves exactly the finite source facts that powered `NB-118`, namely

\[
f\perp V_M,
\tag{34}
\]

and it does so while achieving the strongest possible visible target alignment `Q_Rf=e_R`.

This is the relevant kill test. If one forgets that an actual zero packet must be a confluent zero-power sum and retains only the first `M-1` Nyman annihilation equations, then the tail Gram geometry itself manufactures a perfect target-rescue witness with optimal repair cost `Theta_M(R)`. Therefore no argument depending only on a fixed finite family of equations `(1)` can upgrade `NB-118` from `O_M(1/R)` to `o_M(1/R)` uniformly over that source-equation class.

The result does **not** construct an actual packet of zeta zeros. The witness need not be a finite exponential polynomial in `log n`, need not satisfy the Nyman equations for `b>M`, and is rebuilt for each cutoff `R`. It also does not identify the sharp constant in the `NB-118` upper bound for actual zero packets. What it proves is the sharpness of the **retention exponent** under exactly the fixed finite source information used there.

This separation is important. The finite source equations are genuine arithmetic facts about actual zeros, but after compression they are not source-complete. Their orthogonal complement still contains target-perfect matched controls at the critical inverse-section scale. The missing information is therefore coherence, not another fixed finite constraint.

## 5. Prior-art and next theorem boundary

The derivation is elementary once the natural-cell coefficients and exact Nyman orthogonality from `NB-118` are available. A prior-art audit of finite-dimensional Nyman--Beurling/Gram formulations did not supply a load-bearing theorem for the periodic tail-Gram repair `(12)`--`(30)`, and no external novelty claim is needed here. `SOURCES.md` therefore requires no new dependency.

The live theorem is now more specific. To exclude strong high-zero target rescue, one must distinguish the actual zero-power interpolation class from the matched controls above. Natural routes are to combine the `NB-117` confluent power-sum form with `O(1/R)` retention, make a growing family of Nyman equations coercive without assuming the Nyman distance conclusion, impose cross-cutoff coherence so the witness cannot be rebuilt independently for every `R`, or find another actual-zero identity that survives the matched-control test.

`NB-118` localized the escape to inverse-section modes. `NB-119` shows that **fixed finite Nyman orthogonality cannot close that escape, even at perfect target angle**. The next gain has to come from the source class itself.