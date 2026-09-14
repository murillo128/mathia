# MC-281 — Empirical Christoffel leverage gives an exact blind-count certificate on the arithmetic image

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the fixed-weight shell matrix of `MC-269`–`MC-280`. Let

\[
\mathcal B_m=\{S\subseteq\mathcal P_y:|S|\le m\},
\qquad
Z=|\mathcal B_m|,
\]

\[
\mathcal T_t=\{T\subseteq\mathcal R_y:|T|=t\},
\qquad
C=|\mathcal T_t|,
\]

and form the real sign matrix

\[
\mathbf A=(A_{T,S})_{T\in\mathcal T_t,S\in\mathcal B_m},
\qquad
A_{T,S}=\chi_T(q_S)\in\{-1,+1\}.
\tag{1}
\]

Write

\[
v:=\mathbf1_Z.
\tag{2}
\]

A row `T` is blind exactly when its complete degree-`m` feature row equals `v^*`. Let `A_y(t)` denote the number of blind rows, as in `MC-268`.

Instead of demanding a scalar decoder that is uniformly accurate on the entire Boolean cube, optimize directly on the **actual arithmetic row image**. Define the counting-measure empirical Christoffel value at the virtual blind endpoint by

\[
\boxed{
\mathfrak C_{m,y}(t)
:=
\inf_{a\in\mathbb C^Z\,:\,v^*a=1}
\|\mathbf A a\|_2^2.
}
\tag{3}
\]

Equivalently, if

\[
p_a(x)=\sum_{S\in\mathcal B_m}a_Sx_S,
\tag{4}
\]

then `(3)` is

\[
\mathfrak C_{m,y}(t)
=
\inf_{\deg p\le m\,:\,p(1^k)=1}
\sum_{T\in\mathcal T_t}|p(x(T))|^2.
\tag{5}
\]

Every blind row contributes exactly `1` to `(5)` for every admissible polynomial. Therefore

\[
\boxed{
A_y(t)\le \mathfrak C_{m,y}(t).
}
\tag{6}
\]

In particular,

\[
\boxed{
\mathfrak C_{m,y}(t)<1
\quad\Longrightarrow\quad
A_y(t)=0.
}
\tag{7}
\]

This is a strictly more adaptive positive certificate than the flat Christoffel energy of `MC-268`–`MC-269`. The flat coefficient vector

\[
a_{\rm flat}=\frac vZ
\tag{8}
\]

is admissible in `(3)`, hence

\[
\boxed{
\mathfrak C_{m,y}(t)
\le
\left\|\mathbf A\frac vZ\right\|_2^2
=
\mathcal E_{m,y}(t).
}
\tag{9}
\]

Thus the existing Christoffel detector is one feasible polynomial inside a larger endpoint-normalized optimization over the same degree-`m` source features. No additional source depth is introduced.

The dual formulation exposes the signed cross-row structure left open by `MC-280`. Define

\[
\boxed{
\Lambda_{m,y}(t)
:=
\inf\left\{
\|c\|_2^2:
\mathbf A^*c=v
\right\},
}
\tag{10}
\]

with `\Lambda_{m,y}(t)=+\infty` if the moment-matching equation is infeasible. Then exactly

\[
\boxed{
\mathfrak C_{m,y}(t)=\frac1{\Lambda_{m,y}(t)},
}
\tag{11}
\]

with the convention `1/(+\infty)=0`.

The constraint in `(10)` says that a signed measure `c` on the target shell has total mass one and matches **every available source moment** of the blind endpoint:

\[
\sum_{T\in\mathcal T_t}c_T\chi_T(q_S)=1
\qquad(S\in\mathcal B_m).
\tag{12}
\]

The empty support `S=\varnothing` already gives `\sum_Tc_T=1`. Therefore `(10)` is not another pointwise row decoder: it asks how cheaply the virtual blind endpoint can be synthesized by a signed combination of the **actual target rows** at the current source depth.

If there are `B=A_y(t)>=1` blind rows, averaging their coordinate vectors gives a feasible `c` with squared norm `1/B`. Hence

\[
\Lambda_{m,y}(t)\le\frac1{A_y(t)},
\qquad
A_y(t)\le\frac1{\Lambda_{m,y}(t)},
\tag{13}
\]

which is `(6)` through `(11)`. Thus either of the following is an exact blind-exclusion certificate:

\[
\boxed{
\mathbf1_Z\notin\operatorname{ran}(\mathbf A^*)
}
\tag{14}
\]

or, when the endpoint is in the row span,

\[
\boxed{
\Lambda_{m,y}(t)>1.
}
\tag{15}
\]

The first alternative is equivalent to the rank increment

\[
\operatorname{rank}
\begin{pmatrix}
\mathbf A\\
v^*
\end{pmatrix}
=
\operatorname{rank}(\mathbf A)+1.
\tag{16}
\]

It also has an explicit degree-`m` separating polynomial. If

\[
n=P_{\ker\mathbf A}v\ne0,
\tag{17}
\]

then

\[
a=\frac{n}{\|n\|_2^2}
\tag{18}
\]

satisfies

\[
\mathbf A a=0,
\qquad
v^*a=1.
\tag{19}
\]

So `(14)` makes the empirical Christoffel value exactly zero.

When `v\in\operatorname{ran}(\mathbf A^*)`, put `G=\mathbf A^*\mathbf A`. Standard Moore–Penrose theory gives

\[
\boxed{
\Lambda_{m,y}(t)=v^*G^+v,
\qquad
\mathfrak C_{m,y}(t)=\frac1{v^*G^+v}.
}
\tag{20}
\]

The quantity `v^*G^+v` is the same inverse-Gram quadratic form that defines statistical leverage, here evaluated at the virtual blind feature row. Hence the surviving arithmetic question can be stated sharply: **does tight shell localization force the blind endpoint either outside the actual degree-`m` row span, or to have virtual leverage greater than one?**

This does not prove either alternative. It converts the arithmetic-image-only escape left open by `MC-280` into a precise directional rank/inverse-Gram problem and shows exactly why coefficient-uniform large-sieve bounds still cannot solve it.

## 1. The blind-count inequality is pointwise and exact

For any admissible `a` in `(3)`, a blind row has row vector `v^*`, so

\[
(\mathbf A a)_T=v^*a=1.
\tag{21}
\]

If there are `A_y(t)` blind rows, their contribution alone gives

\[
\|\mathbf A a\|_2^2\ge A_y(t).
\tag{22}
\]

Taking the infimum over all endpoint-normalized degree-`m` coefficient vectors proves `(6)`. No distributional model, positivity assumption on the coefficients, or arithmetic estimate enters this step.

Equation `(9)` follows because the flat vector `(8)` is exactly the coefficient vector of the Christoffel polynomial already isolated in `MC-269`:

\[
(\mathbf A a_{\rm flat})_T
=\frac1Z\sum_{S\in\mathcal B_m}\chi_T(q_S)
=P_m(b_y(T);k_y).
\tag{23}
\]

Therefore the empirical optimization never performs worse than the previous positive endpoint detector at the same feature depth.

## 2. Signed shell synthesis is the exact Hilbert-space dual

Assume first that `(10)` is feasible and let `c_0` be its minimum-norm solution. For every admissible `a`,

\[
1
=v^*a
=(\mathbf A^*c_0)^*a
=c_0^*\mathbf A a.
\tag{24}
\]

Cauchy–Schwarz gives

\[
1\le\|c_0\|_2\,\|\mathbf A a\|_2,
\tag{25}
\]

hence

\[
\mathfrak C_{m,y}(t)\ge\frac1{\|c_0\|_2^2}
=\frac1{\Lambda_{m,y}(t)}.
\tag{26}
\]

Since `v\in\operatorname{ran}(\mathbf A^*)=\operatorname{ran}(G)`, the minimum-norm synthesis has

\[
c_0=\mathbf A G^+v,
\tag{27}
\]

and

\[
\|c_0\|_2^2=v^*G^+v.
\tag{28}
\]

The normalized vector

\[
a_0=\frac{G^+v}{v^*G^+v}
\tag{29}
\]

satisfies `v^*a_0=1` and attains

\[
\|\mathbf A a_0\|_2^2
=\frac1{v^*G^+v},
\tag{30}
\]

proving `(11)` and `(20)` in the feasible case.

If `(10)` is infeasible, then `v\notin\operatorname{ran}(\mathbf A^*)`, equivalently its orthogonal projection `n` onto `\ker\mathbf A` is nonzero. Since `v=n+r` with `r\perp\ker\mathbf A`,

\[
v^*n=\|n\|_2^2.
\tag{31}
\]

The vector `(18)` is therefore admissible and has zero empirical energy, proving `\mathfrak C=0=1/(+\infty)`.

This duality makes the open signed route concrete. Rather than bounding each row separately and then summing, `(10)` asks whether signed cancellation among the target rows can reproduce the blind low-degree moments with small Euclidean mass.

## 3. The operator-norm barrier reappears at exactly one

`MC-270` proved that every coefficient-uniform estimate

\[
\|\mathbf A a\|_2^2\le D\|a\|_2^2
\qquad(a\in\mathbb C^Z)
\tag{32}
\]

must have

\[
D\ge Z
\tag{33}
\]

because each row of `\mathbf A` has squared norm `Z`.

Suppose the synthesis equation `(10)` is feasible. Since `\|v\|_2^2=Z`,

\[
Z
=v^*v
=c^*\mathbf A v
\le
\|c\|_2\,\|\mathbf A v\|_2
\le
\|c\|_2\sqrt{DZ}.
\tag{34}
\]

Minimizing over feasible `c` yields only

\[
\boxed{
\Lambda_{m,y}(t)\ge\frac ZD.
}
\tag{35}
\]

But `(33)` makes the right-hand side at most one. Thus a coefficient-uniform operator-norm theorem can never force the strict leverage condition `(15)`. Nor can an operator norm prove the rank-increment alternative `(14)`.

This is the dual form of `MC-270`'s blind-atom threshold. The information missing from the ordinary large sieve is now identified as **directional endpoint geometry**: the position of `v` relative to the arithmetic row span and, conditional on membership, the minimum signed synthesis norm in that one direction.

At the live choice `m=t+1`, `MC-270` has

\[
\frac ZC\sim\frac{k_y}{t+1}\to\infty,
\tag{36}
\]

so the matrix is very wide and

\[
\dim\ker\mathbf A\ge Z-C.
\tag{37}
\]

However `(37)` alone proves nothing: a huge kernel may still be orthogonal to `v`. The decisive object is the **orientation** of that kernel relative to the blind endpoint, equivalently `(14)`–`(15)`, not rank deficiency by itself.

## 4. Why this is not contradicted by the full-cube decoder barriers

`MC-275`, `MC-278`, `MC-279`, and `MC-280` ask for endpoint discrimination under constraints that hold on the full Boolean cube. In particular, `MC-280` shows that a scalar polynomial which is atom-accurate at the blind point and uniformly tiny on **every** nonblind Boolean vector cannot place substantial coefficient mass at the available low depth.

The optimization `(3)` removes exactly that full-cube requirement. It constrains `p_a` only on the arithmetic image

\[
\{x(T):T\in\mathcal T_t\},
\tag{38}
\]

and at the virtual blind endpoint. Therefore it is not subject to the full-cube Parseval obstruction merely by definition. If the arithmetic image occupies a favorable low-dimensional position, a degree-`m` polynomial can vanish on every actual row while taking value one at `1^k`; `(17)`–`(19)` give the exact criterion.

That escape is also its principal weakness. Determining the arithmetic row span or the directional inverse Gram form may encode essentially the same exceptional-row information one hoped to prove. Thus `\mathfrak C<1` is a rigorous certificate, not yet an unconditional estimate or an algorithmically cheap surrogate for blindness.

The result nevertheless separates two questions that were conflated by full-cube decoding:

1. **representation depth:** the degree-`m` features already suffice to pose an exact arithmetic-image separation problem;
2. **arithmetic conditioning:** useful progress requires shell-specific control of the orientation or signed synthesis cost, not another generic full-cube approximation theorem.

## 5. Prior art and novelty boundary

The optimization `(5)` is a classical empirical Christoffel-function construction for a finite counting measure. Jean-Bernard Lasserre and Edouard Pauwels, *The empirical Christoffel function with applications in data analysis*, Advances in Computational Mathematics 45 (2019), 1439–1468, DOI `10.1007/s10444-019-09673-1`, studies the empirical Christoffel function associated with a counting measure on a finite point cloud and its use for support, outlier, and novelty detection. No novelty is claimed for the finite-sample Christoffel variational principle.

The inverse-Gram quantity in `(20)` is likewise classical leverage geometry. Edouard Pauwels, Francis Bach and Jean-Philippe Vert, *Relating Leverage Scores and Density using Regularized Christoffel Functions*, NeurIPS 31 (2018), 1670–1679, arXiv `1805.07943`, develops the Christoffel/leverage variational connection in a regularized kernel setting. Moore–Penrose formulas, minimum-norm moment matching, row-space projection, and rank-increment tests are standard linear algebra.

A targeted literature search through 14 September 2026 found these general Christoffel/leverage mechanisms but did not identify a theorem applying the virtual-endpoint criterion `(3)`–`(20)` to this fixed-weight shell-product quadratic-character matrix. That search boundary is not a novelty claim.

The durable Mathia-specific content is the exact insertion of this classical mechanism into the current arithmetic object: the flat detector of `MC-269` admits an image-adaptive Christoffel improvement at the same source depth; its dual is a signed target-shell moment-matching problem; blind multiplicity is bounded exactly by the empirical Christoffel value; and `MC-270`'s uniform large-sieve floor becomes the sharp statement that generic operator control cannot force virtual leverage above one.

## Boundaries and falsification tests

- **Sufficient, not necessary.** `\mathfrak C<1`, `\Lambda>1`, or infeasibility of `(10)` excludes blindness. Their failure does not produce a blind row. There may be no blind row even when `v` lies in the row span and `\Lambda\le1`.
- **No gain from dimension counting alone.** The live inequality `Z>C` creates a large nullspace but does not imply `P_{\ker\mathbf A}v\ne0`.
- **No hidden source-depth gain.** Every column in `(1)` still has support at most `m`; optimization changes coefficients and uses the actual row image but introduces no deeper Walsh feature.
- **No unconditional arithmetic estimate.** Evaluating or bounding `G^+` or proving `(14)` may be as difficult as the original shell problem. The finding supplies an exact target, not a proof of its favorable value.
- **No generic-code specificity.** The separated-prime universality control of `MC-252` must be applied to any proposed theorem for `(14)` or `(15)`. A bound that survives arbitrary separated-prime Legendre realizations does not yet exploit the tight shell localization that the live problem requires.
- **No operator-norm shortcut.** Any argument that replaces the virtual direction by a coefficient-uniform norm before the decisive step falls back to `(35)` and cannot certify `\Lambda>1`.
- **Normalization check.** `\mathfrak C` uses the unnormalized counting measure on target rows. Under the probability-normalized empirical measure it is divided by `C`; all blind-count statements must be rescaled accordingly.

A direct falsification of the algebra would be an admissible `a` with empirical energy below the number of blind rows, or a feasible `c` violating the reciprocal minimization `(11)`. Equations `(21)`–`(31)` exclude both.

## Consequence for the research line

The full-cube signed-decoder route closed by `MC-280` does not close arithmetic-image-only decoding. At the current low source depth there is an exact surviving criterion, but it is no longer a generic approximation problem. It is the shell-specific directional question

\[
\boxed{
\mathbf1_Z\notin\operatorname{ran}(\mathbf A^*)
\quad\text{or}\quad
\mathbf1_Z^*(\mathbf A^*\mathbf A)^+\mathbf1_Z>1.
}
\tag{39}
\]

The first alternative asks for a genuine rank increment of the virtual blind row; the second asks for a lower bound on its signed synthesis cost. Both preserve row identity and phase across the target shell and both evade the coefficient-uniform operator relaxation that `MC-270` proved insufficient.

Accordingly, the next useful arithmetic theorem should target this directional geometry directly: exploit tight shell localization, reciprocity, or another source-coupled identity to control the projection of the blind endpoint onto the actual row span or the corresponding inverse-Gram quadratic form. A proof that only improves average row orthogonality or a uniform large-sieve constant cannot cross the new certificate threshold.