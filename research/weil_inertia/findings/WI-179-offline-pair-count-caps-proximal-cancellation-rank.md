# WI-179 — off-line pair count caps the proximal cancellation rank

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + BOOTSTRAP-INTERFACE`. WI-178 shows that Lamzouri's exceptional-population slack contains the entire clipped Gram defect of the simple-real sector after allowing the off-line odd block to act as an arbitrary positive-semidefinite subtractor. That relaxation discards one exact piece of source information: the subtractor is a sum of one rank-one operator per **distinct off-line conjugate pair**. If there are `k` such pairs, its rank is at most `k`.

Keeping this rank constraint gives an exact strengthening. Let `M_0=V\ominus U` be Lamzouri's simple-real quotient, let

\[
S=\sum_{x\in R_1} b_x\otimes b_x,
\qquad b_x=P_{M_0}f_x,
\]

and let `B` be the Gram matrix of the `b_x`. Write the eigenvalues of `S` (equivalently of `B`) in decreasing order as `lambda_1>=...>=lambda_n>0`, and define

\[
\mathcal T_k(S)
:=\sum_{j>k}(\lambda_j-2)_+^2.
\tag{1}
\]

Then the exact Lamzouri budget strengthens to

\[
\boxed{
Q-N\ge
O+2M+\operatorname{tr}\Psi(G_s)+\mathcal T_k(S),
}
\tag{A}
\]

where `G_s` is the full Gram matrix of the simple real vectors, `O` is the multiplicity-weighted non-real population, `M=N-D` is total multiplicity excess, and

\[
\Psi(t)=
\begin{cases}
(t-1)^2,&0\le t\le2,\\
2t-3,&t\ge2.
\end{cases}
\]

Thus **one distinct off-line pair can remove at most one supercritical quotient mode from the quadratic Gram penalty**. If the simple-real quotient has more than `k` eigenvalues above `2`, the excess modes pay an unavoidable squared tail even after the exceptional odd sector is optimized adversarially. This is a genuinely joint exceptional-block constraint absent from the scalar budget of WI-170 and from the unrestricted proximal relaxation of WI-178.

No unconditional simple-critical-zero percentage changes in this finding. The new term becomes numerically useful only after a source theorem forces enough quotient eigenvalues above `2` by a controlled margin.

## 1. Exact source interface from WI-178

The primary finite source remains Proposition 2.1 of Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1 (2 September 2026). WI-137 rewrites Lamzouri's Hilbert-space proof as an exact operator slack identity; WI-170 separates that slack into off-line mass, multiplicity excess, and a nonnegative remainder; WI-178 compresses the remainder to the simple-real quotient.

For every simple real point `x`, write

\[
a_x=P_Uf_x,
\qquad
b_x=P_{M_0}f_x,
\qquad M_0=V\ominus U.
\tag{2}
\]

Set

\[
S:=\sum_{x\in R_1}b_x\otimes b_x
\tag{3}
\]

on `M_0`. The projected vectors are linearly independent by WI-126, so `S` is positive definite on the `n`-dimensional quotient. Their Gram matrix `B` has the same positive eigenvalues as `S`.

The full simple-real Gram is

\[
G_s=B+A,
\qquad
A=(\langle a_x,a_y\rangle)\succeq0,
\qquad
\operatorname{tr}A=S_1.
\tag{4}
\]

The off-line odd sector enters the `M_0` compression through

\[
C:=2\sum_{z\in Z_+}m_z
(P_{M_0}h_z)\otimes(P_{M_0}h_z)\succeq0.
\tag{5}
\]

If

\[
k:=|Z_+|
\tag{6}
\]

is the number of distinct non-real conjugate pairs, then (5) immediately gives the load-bearing source constraint

\[
\boxed{\operatorname{rank}C\le k.}
\tag{7}
\]

Multiplicity does not increase this rank: repeating the same off-line frequency only rescales the same rank-one term.

WI-178 proves from the exact Lamzouri remainder `R` that

\[
\boxed{
R\ge
\|S-I-C\|_{\rm HS}^2
+2\operatorname{tr}C
+2S_1.
}
\tag{8}
\]

Its published strengthening then minimizes the first two terms over **all** `C\succeq0`, obtaining `tr Psi(S)`. The present step repeats that minimization without discarding (7).

## 2. Rank-constrained proximal minimization

For a fixed positive-semidefinite `S`, put

\[
X:=S-2I,
\qquad
X_+:=(S-2I)_+.
\tag{9}
\]

For every `C\succeq0`,

\[
\begin{aligned}
\|S-I-C\|_{\rm HS}^2+2\operatorname{tr}C
&=\|S-I\|_{\rm HS}^2
  +\|C\|_{\rm HS}^2
  -2\operatorname{tr}(XC).
\end{aligned}
\tag{10}
\]

Since `X_+-X\succeq0` and `C\succeq0`,

\[
\operatorname{tr}(XC)\le\operatorname{tr}(X_+C).
\tag{11}
\]

Hence

\[
\begin{aligned}
\|S-I-C\|_{\rm HS}^2+2\operatorname{tr}C
&\ge
\|S-I\|_{\rm HS}^2
-\|X_+\|_{\rm HS}^2
+\|C-X_+\|_{\rm HS}^2.
\end{aligned}
\tag{12}
\]

The first two terms are exactly the clipped spectral defect:

\[
\|S-I\|_{\rm HS}^2-\|X_+\|_{\rm HS}^2
=\operatorname{tr}\Psi(S).
\tag{13}
\]

Now impose `rank C<=k`. The classical Eckart--Young low-rank approximation theorem applied to the positive-semidefinite matrix `X_+` gives

\[
\min_{\substack{C\succeq0\\\operatorname{rank}C\le k}}
\|C-X_+\|_{\rm HS}^2
=
\sum_{j>k}(\lambda_j(S)-2)_+^2
=\mathcal T_k(S).
\tag{14}
\]

The PSD constraint does not change the classical minimum because the spectral truncation of `X_+` to its `k` largest eigenvalues is itself PSD. Equality in (11)--(14) is attained in the relaxed matrix problem by taking `C` to be precisely that top-`k` spectral truncation. Therefore the relaxation is exact:

\[
\boxed{
\min_{\substack{C\succeq0\\\operatorname{rank}C\le k}}
\left(
\|S-I-C\|_{\rm HS}^2+2\operatorname{tr}C
\right)
=
\operatorname{tr}\Psi(S)+\mathcal T_k(S).
}
\tag{15}
\]

This is not a claim that every optimizing rank-`k` PSD matrix is realizable by Lamzouri odd vectors. The actual source class is smaller. Equation (15) minimizes over a larger class containing every source-realizable `C`, so it is a valid lower bound and any additional realizability restriction can only strengthen it.

## 3. Restore the full simple-real Gram without losing the rank tail

Insert (15) into (8):

\[
R\ge
\operatorname{tr}\Psi(S)
+\mathcal T_k(S)
+2S_1.
\tag{16}
\]

Because `S` and `B` have the same positive spectrum,

\[
\operatorname{tr}\Psi(S)=\operatorname{tr}\Psi(B),
\qquad
\mathcal T_k(S)=\mathcal T_k(B).
\tag{17}
\]

WI-178 already proves, using `G_s=B+A`, Weyl monotonicity, and the global `2`-Lipschitz bound for `Psi`, that

\[
\operatorname{tr}\Psi(G_s)
\le
\operatorname{tr}\Psi(B)+2\operatorname{tr}A
=
\operatorname{tr}\Psi(S)+2S_1.
\tag{18}
\]

Combining (16) and (18) gives

\[
\boxed{
R\ge
\operatorname{tr}\Psi(G_s)+\mathcal T_k(S).
}
\tag{19}
\]

Finally WI-170's exact population identity

\[
Q-N=O+2M+R
\tag{20}
\]

turns (19) into the announced joint budget (A).

The tail must remain attached to the **projected** Gram `B`/frame `S`. Since `G_s=B+A` with `A\succeq0`, the supercritical eigenvalues of `G_s` can be larger than those of `B`; replacing `\mathcal T_k(S)` by the corresponding tail of `G_s` would go in the wrong direction and is not justified by this argument.

## 4. Threshold form: each pair screens at most one supercritical mode

For `epsilon>0`, define

\[
q_\epsilon(S)
:=\#\{j:\lambda_j(S)\ge2+\epsilon\}.
\tag{21}
\]

If `q_epsilon(S)>k`, every one of the `q_epsilon-k` uncancelled modes contributes at least `epsilon^2` to (1). Therefore

\[
\boxed{
\mathcal T_k(S)
\ge
\bigl(q_\epsilon(S)-k\bigr)_+\epsilon^2.
}
\tag{22}
\]

Thus (A) implies

\[
\boxed{
Q-N\ge
O+2M+\operatorname{tr}\Psi(G_s)
+\bigl(q_\epsilon(S)-k\bigr)_+\epsilon^2.
}
\tag{23}
\]

Since every distinct off-line pair contributes at least two non-real labels counted with multiplicity,

\[
O=2\sum_{z\in Z_+}m_z\ge2k,
\tag{24}
\]

and hence also

\[
\boxed{
Q-N\ge
O+2M+\operatorname{tr}\Psi(G_s)
+\left(q_\epsilon(S)-\frac O2\right)_+\epsilon^2.
}
\tag{25}
\]

Equation (25) is a nonlinear coupling between the off-line population and the spectrum of the simple-real quotient. It is precisely the kind of joint constraint that is outside WI-177's affine-vector cancellation theorem: the number of exceptional pairs controls the **rank of the admissible proximal response**, rather than merely contributing an additive scalar tax.

A useful near-equality formulation is obtained by defining the residual after the WI-178 budget,

\[
\Xi:=Q-N-O-2M-\operatorname{tr}\Psi(G_s)\ge0.
\tag{26}
\]

Then

\[
\boxed{
q_\epsilon(S)
\le k+\frac{\Xi}{\epsilon^2}.
}
\tag{27}
\]

So a near-extremizer cannot have many more uniformly supercritical simple-real quotient modes than it has distinct off-line pairs. The exceptional block has one rank degree of freedom per pair and no more.

## 5. Controls and equality cases

The rank constraint behaves correctly on the line's canonical controls.

If there are no off-line pairs, `k=0` and `C=0`. Equation (15) reduces to

\[
\|S-I\|_{\rm HS}^2
=\operatorname{tr}\Psi(S)+\sum_j(\lambda_j(S)-2)_+^2,
\]

so all supercritical excess is charged quadratically. This is exactly the original objective before the off-line subtractor was introduced.

For one off-line conjugate pair, `k=1`. The odd sector may remove the quadratic excess of at most one eigenmode above `2`; a second mode above `2+epsilon` costs at least `epsilon^2`. This does not contradict the isolated-pair confluence example of WI-140, which has no requirement that the simple-real quotient carry two such supercritical modes.

If `S` has at most `k` eigenvalues above `2`, then `mathcal T_k(S)=0` and the result reduces exactly to WI-178. Hence the new term does not manufacture a gain when the off-line rank budget is already large enough to realize the unrestricted proximal clipping at the level of this relaxation.

Critical-line doubles remain separated. They contribute to `M` but not to `k`, and they do not create odd rank-one subtractors in (5). Off-line multiplicity increases `O` and `M` but still does not enlarge `rank C` beyond the number of distinct conjugate pairs. Pure proof/operator slack remains in `R`; it is not relabelled as off-line mass.

No commutativity between `S` and the actual source operator `C` is assumed. Inequality (11) and the Frobenius low-rank approximation step treat arbitrary PSD `C`. The minimizing spectral truncation is used only to solve the relaxed optimization problem.

## 6. Relation to the existing inertia and confluence barriers

WI-138 proves that the negative index of the full Lamzouri tensor is exactly `k`, one negative direction per distinct off-line pair. WI-139 shows that near saturation forces those negative directions to align with the horizontal quotient `W\ominus V`. The present result is different: it controls how many **supercritical simple-real quotient modes** the projected odd sector can cancel before the Lamzouri remainder is evaluated.

The common integer `k` therefore appears on both sides of the signed geometry. The full tensor has exactly `k` negative directions, and its projected odd correction has rank at most `k`. This does not give a spectral gap: all `k` negative directions may still collapse under confluence, and if the simple-real quotient has at most `k` supercritical modes then the new tail vanishes. WI-140 and the fixed-bandwidth confluence barriers therefore remain valid.

The result also does not contradict WI-177. That barrier closes finite-dimensional additive states whose eventual global use is affine/support-functional on the same period-33 source witness. Here the exceptional population changes the **feasible set** of a matrix minimization through a rank constraint. The term `T_k(S)` is nonlinear in the joint state `(S,k)` and cannot be obtained by assigning an independent affine tax to `S` and `k` after the minimization has already forgotten their coupling.

This distinction identifies the next decisive source question. To turn (A) into a stricter zeta theorem one needs an independently justified lower bound on `q_epsilon(S)` or directly on `T_k(S)` that cannot be satisfied by choosing `k` off-line pairs. A theorem forcing an extensive family of quotient eigenvalues above `2+epsilon`, for example, would immediately consume exceptional-pair budget through (23). Conversely, a source-compatible near-extremizer with at most `k` supercritical quotient modes would show that this rank coupling alone cannot bootstrap further.

## 7. Prior-art and novelty audit

The source-side ingredients are literature-backed by Lamzouri's Proposition 2.1 and by the Alpöge--Furman/Weil-form context already recorded in `SOURCES.md`. The exact operator, population, inertia, and Gram-defect interfaces used here are Mathia findings WI-137, WI-138, WI-170, and WI-178.

The matrix optimization in (14)--(15) is classical low-rank approximation. Carl Eckart and Gale Young, *The approximation of one matrix by another of lower rank*, **Psychometrika** 1 (1936), 211--218, DOI `10.1007/BF02288367`, gives the foundational Frobenius low-rank theorem; the PSD specialization used here is immediate because the target `X_+` is PSD and its spectral truncation remains PSD. Generalized rank-constrained Frobenius approximation has a large subsequent literature. No novelty is claimed for Eckart--Young, spectral truncation, positive/negative parts, or the rank inequality for sums of rank-one operators.

A targeted audit of Lamzouri's current preprint, the local WI-137--WI-178 chain, and the current local clue set found exact negative-index counting, eigenspace orientation, Schur-collapse barriers, and the unrestricted proximal clipping of WI-178, but not the rank-capped proximal tail (A)/(15). Absence from that bounded audit is not evidence of priority, and no priority claim is made. The durable line-specific content is the observation that Lamzouri's **off-line pair count is exactly the rank budget of the exceptional proximal cancellation**, plus the resulting joint inequalities (A), (23), and (27).

## 8. Research implication

WI-178 showed that Gram defect is not merely a proof remainder: it subtracts from the same reservoir available to off-line mass and multiplicity. WI-179 makes that coupling finer. The off-line sector cannot spend arbitrary PSD cancellation power against the simple-real quotient; with `k` distinct pairs it can spend at most `k` spectral directions.

This yields a concrete bootstrap interface rather than a percentage claim. A future zeta-source theorem that forces more than `k` robustly supercritical quotient modes immediately creates extra remainder by (22), reducing the exceptional budget and potentially feeding back on `k`. The route is falsified if the actual source can always concentrate all quotient supercriticality into at most the available off-line pair count. The next useful attack should therefore target the **spectral multiplicity of supercritical quotient modes**, not another scalar lower bound for `tr Psi(G_s)` alone.