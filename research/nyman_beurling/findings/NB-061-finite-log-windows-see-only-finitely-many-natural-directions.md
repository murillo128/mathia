# NB-061 — finite log windows see only finitely many natural directions

**Status:** `EXACT-DERIVED + WINDOW-TRUNCATION + FINITE-RANK + FIRST-DYADIC-KERNEL-NONTRIVIAL + TARGET-TAIL-REDUCTION + FLAT-CONTROL + METHOD-ADVANCE`.

`NB-058` identifies the collective late quotient with the orthogonal complement of compact-time arithmetic defects, and `NB-060` reduces the existence of any such defect to the first dyadic kernel

\[
\mathcal K_2=\ker\!\left(U_{\log 2}^*\big|_{\mathcal D}\right),
\qquad
\mathcal D=\mathcal A^\perp.
\]

The remaining existence question looked genuinely arithmetic: perhaps the actual deflated natural span imposed infinitely many independent constraints even on the first finite Paley--Wiener window. It does not. The exact integer-log cocycle from `NB-053` forces all sufficiently large natural generators to become proportional after restriction to any fixed integer-log window.

For every integer `R>=2`, let

\[
\mathcal E_R:=\ker U_{\log R}^*,
\qquad
J_R:=P_{\mathcal E_R}.
\]

Under Paley--Wiener, `E_R` is exactly `L^2([0,log R])` embedded in `L^2(0,infinity)`, and `J_R` is time truncation to that interval. With

\[
F_n:=F_{\log n}=Oq_{\log n},
\qquad
\mathcal A=\overline{\operatorname{span}}\{F_n:n\ge2\},
\]

define the visible finite-window natural space

\[
\mathcal G_R:=J_R\mathcal A\subseteq\mathcal E_R.
\]

Then

\[
\boxed{
\mathcal G_R
=
\operatorname{span}\{J_RF_n:2\le n\le R\}.
}
\tag{1}
\]

In particular,

\[
\boxed{
\dim\mathcal G_R\le R-1,
\qquad
\mathcal K_R
=
\mathcal E_R\ominus\mathcal G_R.
}
\tag{2}
\]

Since `E_R` is infinite-dimensional, every finite-time arithmetic defect sector is infinite-dimensional. In particular

\[
\boxed{
\mathcal K_2
=
\mathcal E_2\ominus\operatorname{span}\{J_2F_2\}
}
\tag{3}
\]

has codimension at most one in `E_2`, so `K_2` is certainly nonzero and in fact infinite-dimensional. Thus the zero-kernel branch left open in `NB-060` is impossible: **compact-time defects exist abundantly already in the first dyadic window**.

The target problem nevertheless does not collapse. For any `h in D`,

\[
\boxed{
\operatorname{dist}(h,\mathcal K_R)^2
=
\|(I-J_R)h\|^2
+
\|P_{\mathcal G_R}J_Rh\|^2.
}
\tag{4}
\]

Applied to the canonical residual `h_*=Qe`, `NB-058` becomes

\[
\boxed{
\|P_{\mathcal T_R}h_*\|^2
=
\|(I-J_R)h_*\|^2
+
\|P_{\mathcal G_R}J_Rh_*\|^2.
}
\tag{5}
\]

The ordinary time tail in the first term tends to zero automatically. Hence the whole generalized-kernel question is reduced to one finite-dimensional, target-aware quantity:

\[
\boxed{
h_*\in\mathcal K_{\rm fin}
\iff
\|P_{\mathcal G_R}J_Rh_*\|\longrightarrow0.
}
\tag{6}
\]

So `NB-060`'s first theorem is now settled positively; the live obstruction is not existence of localized defects, but whether the finite family of natural directions visible in each growing window continues to capture a nonvanishing component of the truncated canonical residual.

## 1. Integer-log covariance collapses the high-index restrictions

Retain the exact cocycle from `NB-053` / `NB-058`. For integers `m,n>=2`,

\[
F_{mn}
=
\frac1nF_m
+
m^{-1/2}U_{\log m}F_n.
\tag{7}
\]

Fix an integer `R>=2` and take any `n>=R`. Using `(m,n)=(R,n)` gives

\[
F_{Rn}
=
\frac1nF_R
+
R^{-1/2}U_{\log R}F_n.
\tag{8}
\]

Because `J_R` truncates to `[0,log R]`, every right shift by `log R` or more disappears after applying `J_R`. Thus

\[
J_RF_{Rn}=\frac1nJ_RF_R.
\tag{9}
\]

Now use the same cocycle with the factors interchanged:

\[
F_{nR}
=
\frac1R F_n
+
n^{-1/2}U_{\log n}F_R.
\tag{10}
\]

Since `n>=R`, the second shifted term also starts no earlier than `log R`, so

\[
J_RF_{nR}=\frac1R J_RF_n.
\tag{11}
\]

The left sides of (9) and (11) are identical. Therefore

\[
\boxed{
J_RF_n=\frac{R}{n}J_RF_R
\qquad(n\ge R).
}
\tag{12}
\]

This is the key rigidity. Once one looks only before time `log R`, **every natural generator with index at least `R` contributes the same direction**, differing only by the scalar `R/n`.

The generators with `2<=n<R` contribute at most `R-2` additional directions. Hence the truncated algebraic natural span lies in the finite-dimensional space on the right side of (1). Conversely each of those finitely many truncated generators is visibly in `J_R A`. Since `J_R` is bounded and the right side of (1) is finite-dimensional and therefore closed, taking the closure defining `A` proves (1) exactly.

No property of the arithmetic multiplier `O` beyond the already established semigroup covariance is used. In particular, there is no inversion of `O`, no assumption that `O` is bounded, and no regularity transfer from compact Paley--Wiener support to a disk local-Dirichlet class.

## 2. Every finite-time defect sector is automatically large

For `h in E_R` and `a in A`,

\[
\langle h,a\rangle
=
\langle h,J_Ra\rangle,
\tag{13}
\]

because `h` is supported in the first window and `(I-J_R)a` is supported after it. Therefore

\[
\begin{aligned}
\mathcal K_R
&=\mathcal D\cap\mathcal E_R\\
&=\{h\in\mathcal E_R:h\perp\mathcal A\}\\
&=\{h\in\mathcal E_R:h\perp J_R\mathcal A\}\\
&=\mathcal E_R\ominus\mathcal G_R,
\end{aligned}
\tag{14}
\]

which proves (2).

Since `E_R` is unitarily `L^2([0,log R])`, it is infinite-dimensional, whereas `G_R` has dimension at most `R-1`. Consequently

\[
\boxed{\dim\mathcal K_R=\infty\qquad(R\ge2).}
\tag{15}
\]

At the first dyadic scale there is only one visible natural direction:

\[
\mathcal G_2=\operatorname{span}\{J_2F_2\},
\tag{16}
\]

so (3) follows. Whether the vector `J_2F_2` itself vanishes is irrelevant for the nontriviality conclusion: `K_2` has codimension zero or one in an infinite-dimensional space. Thus

\[
\boxed{\ker B_2=\mathcal K_2\ne\{0\}.}
\tag{17}
\]

Combined with `NB-060`, this eliminates its sharp negative alternative `K_2={0}`, under which every collective late quotient would equal the whole defect space. The generalized root tower

\[
\mathcal K_{2^k}=\ker B_2^k
\]

now begins from an infinite-dimensional seed rather than from an unresolved existence question.

This conclusion should not be confused with RH or with density of `A`. The deflated natural space here is the target-approximation space of `NB-052`--`NB-060`; its orthogonal complement can be large even when only one distinguished target-membership question matters. Equation (15) says that compact-time orthogonal defects exist, not that the canonical residual belongs to their closed union.

## 3. The remaining target question is a finite-window leakage problem

Because `K_R subset E_R` and `E_R=K_R direct-sum G_R`, every `h in D` has the orthogonal decomposition relevant to approximation by `K_R`:

\[
h
=
P_{\mathcal K_R}J_Rh
+
P_{\mathcal G_R}J_Rh
+
(I-J_R)h.
\tag{18}
\]

The last term is orthogonal to `E_R`, while the first two are orthogonal inside `E_R`. Therefore

\[
\operatorname{dist}(h,\mathcal K_R)^2
=
\|P_{\mathcal G_R}J_Rh\|^2
+
\|(I-J_R)h\|^2,
\tag{19}
\]

which is (4).

Taking `h=h_*` and using `NB-058`,

\[
\|P_{\mathcal T_R}h_*\|^2
=
\operatorname{dist}(h_*,\mathcal K_R)^2,
\]

proves (5). Strong convergence `J_R -> I` gives

\[
\|(I-J_R)h_*\|\to0.
\tag{20}
\]

Since the increasing spaces `K_R` converge to `K_fin` in the usual closed-union sense, (5) and (20) yield

\[
\operatorname{dist}(h_*,\mathcal K_{\rm fin})^2
=
\lim_{R\to\infty}
\|P_{\mathcal G_R}J_Rh_*\|^2.
\tag{21}
\]

This proves (6).

The reduction is useful because `G_R` is no longer an unknown infinite-dimensional quotient object. It is the finite span of at most `R-1` explicit truncated natural generators. But finite rank by itself gives no decay: a one-dimensional subspace can retain a fixed component of a target forever. A useful next theorem therefore needs a quantitative estimate for

\[
\|P_{\mathcal G_R}J_Rh_*\|,
\tag{22}
\]

or an equivalent source-controlled dual certificate. This is precisely where target moments and conditioning can still matter.

## 4. Flat calibration and falsification boundary

For the `O=1` control of `NB-056`--`NB-058`, `E_R` decomposes into the first `R-1` logarithmic cells and `G_R` is exactly the direct sum of their coarse one-dimensional directions

\[
\operatorname{span}\{e^{t/2}\mathbf1_{I_j}:1\le j<R\}.
\tag{23}
\]

Hence

\[
\dim\mathcal G_R^{(0)}=R-1,
\]

showing that the general rank bound in (2) is sharp. Its orthogonal complement is exactly the early-cell detail space already identified in `NB-058`, so the present theorem recovers that calibration without assuming the arithmetic factor is flat.

For the canonical flat target, the second term in (5) vanishes at the cubic rate encoded by the cell-detail calculation, ultimately giving

\[
\|P_{\mathcal T_R^{(0)}}Q_0e\|^2
=
\frac1{36R^3}+O(R^{-4}).
\tag{24}
\]

But this behavior is target-specific. The finite-rank theorem alone does not reproduce (24) for the actual arithmetic factor and does not imply that the generalized kernels are dense in `D`. A generic vector in `D` may have nondecaying leakage into the moving spaces `G_R`; equation (21) is exactly the quantity that must rule that out for `h_*`.

This is also the correct falsification control against the withdrawn `NB-059` route. The present argument proves nontrivial compact-time defects directly from the exact half-plane semigroup and truncation geometry. It makes no claim that compact support places those defects in a local Dirichlet class after a disk conjugacy. Therefore it neither invokes nor conflicts with the point-specific local-Dirichlet rigidity theorem recorded in `SOURCES.md`.

## 5. Consequence for the accepted early-cell adjoint clue

`CLUE-early-cell-adjoint-duals-certify-target-tail` had two logically distinct difficulties: first, whether any nonzero compact-time arithmetic defect exists; second, whether such defects can approximate the canonical residual with a useful rate. `NB-060` isolated the first question at `R=2`. Equations (3) and (17) now settle that existence gate positively and strongly: there is an infinite-dimensional first-window defect sector.

What remains of the clue is the genuinely target-aware half. Constructing one `h_R in K_R` is no longer the issue. The useful certificate must choose localized defects so that the remainder to `h_*` tends to zero, equivalently so that the finite-window leakage (22) tends to zero. Any proposed adjoint lift should therefore be judged by whether it controls this projection, not merely by whether it manufactures a compactly supported annihilator.

## 6. Prior-art boundary

The ingredients used above are individually standard or already anchored in this line: Paley--Wiener turns the Hardy shift into a right translation; truncation before a right shift annihilates it; orthogonal complements inside a finite window are elementary Hilbert-space geometry; and the integer-dilation covariance of the Nyman family is classical and was persisted in `NB-053`.

The closest line-level prior art remains the Hardy-space orthogonality and shift-invariance work of Calderaro--Manzur--Noor--Santos already recorded in `SOURCES.md`. A targeted search for Nyman--Beurling orthogonal complements, compact support / Paley--Wiener localization, and shift-invariant formulations did not locate the specific finite-window identity (1), the consequent infinite-dimensionality (15) of every compact-time defect sector in the Blaschke-deflated natural space, or the target leakage formula (21). No priority claim is made.

No new specialized external estimate is load-bearing, so `SOURCES.md` remains unchanged.

The durable line-local delta is that the compact-time existence problem is finished: **every integer-log window contains infinitely many arithmetic defects, and the first dyadic window already does so**. The live problem after `NB-060` is solely whether those abundant localized defects can approximate the distinguished canonical residual; equivalently, whether its projection onto the finite-dimensional visible natural space `G_R` vanishes as the window grows.