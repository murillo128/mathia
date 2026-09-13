# NB-090 — summable horizontal zero mass bounds full dyadic terminal Gram entropy

**Status:** `EXACT-DERIVED + CONDITIONAL-ACTUAL-NYMAN-SOURCE + SUMMABLE-HORIZONTAL-ZERO-MASS + FULL-TERMINAL-GRAM + BOUNDED-CORRELATION-ENTROPY + NEGATIVE-METHOD-BOUNDARY`.

`NB-089` closes the scalar average-direction continuation of `NB-087` under the conditional hypothesis

\[
A:=\sum_{\Re\rho>1/2}\left(\Re\rho-\frac12\right)<\infty.
\tag{1}
\]

It leaves open the natural escape explicitly identified there: perhaps the sibling-contrast and cross-block directions discarded by the scalar compression still make the **full** terminal determinant obstruction of `NB-086` diverge.

They do not. Under (1), for the dyadic terminal block

\[
I_R:=I_{R,2}
=\left\{\left\lceil\frac R2\right\rceil,\ldots,R-1\right\},
\qquad
m_R:=|I_R|=\left\lfloor\frac R2\right\rfloor,
\tag{2}
\]

let

\[
K_R:=\bigl(\langle J_RD_i,J_RD_j\rangle\bigr)_{i,j\in I_R},
\qquad
\mathcal R_R:=\Delta_R^{-1/2}K_R\Delta_R^{-1/2},
\tag{3}
\]

where `Delta_R` is the diagonal of `K_R`. Then

\[
\boxed{
-\log\det\mathcal R_R=O_A(1).
}
\tag{4}
\]

More explicitly, every off-diagonal normalized terminal correlation satisfies

\[
\boxed{
|\rho_{ij}^{(R,2)}|\ll_A R^{-1}
\qquad(i\ne j,\ i,j\in I_R),
}
\tag{5}
\]

so

\[
\boxed{
\|\mathcal R_R-I\|_F^2
=\sum_{i\ne j}|\rho_{ij}^{(R,2)}|^2
=O_A(1).
}
\tag{6}
\]

At the same time the spectrum of `mathcal R_R` stays uniformly away from zero. Consequently no hidden near-singular collective mode can turn the bounded pair energy in (6) into a divergent logarithmic determinant.

Thus the entire current-window matrix obstruction from `NB-086`, not merely the scalar test of `NB-087`, is silent on the false-RH-compatible regime (1). A terminal-Gram route must first exclude summable horizontal off-critical mass, or move to structure not contained in the terminal visible block.

## 1. The raw zeta terminal Gram is exactly a rank-one perturbation of the identity

Use the raw innovations restored in `NB-088`,

\[
\widetilde D_j:=BD_j
=\frac{\zeta(s)}s\bigl(j^{1-s}-(j+1)^{1-s}\bigr),
\tag{7}
\]

with Paley--Wiener representative

\[
\widetilde d_j(t)
=e^{-t/2}
\left[
 j\left\lfloor\frac{e^t}{j}\right\rfloor
-(j+1)\left\lfloor\frac{e^t}{j+1}\right\rfloor
\right].
\tag{8}
\]

For every `j in I_R`, one has `j+1<=R<=2j` once the trivial final endpoint is interpreted in the usual empty-tail way. `NB-088` therefore gives

\[
\|J_R\widetilde D_j\|^2=1-\frac1R.
\tag{9}
\]

There is also an exact off-diagonal formula. If `i<j` are both in `I_R`, then `R<=2i`, so by the same terminal two-state floor formula, `\widetilde d_i(t)=-e^{-t/2}` throughout the support of `\widetilde d_j` after `log j`. Hence

\[
\begin{aligned}
\langle J_R\widetilde D_i,J_R\widetilde D_j\rangle
&=
-j\int_{\log j}^{\log(j+1)}e^{-t}\,dt
+
\int_{\log(j+1)}^{\log R}e^{-t}\,dt\\
&=-\frac1{j+1}
+\left(\frac1{j+1}-\frac1R\right)\\
&=
\boxed{-\frac1R}.
\end{aligned}
\tag{10}
\]

Therefore the complete raw terminal Gram matrix is

\[
\boxed{
\widetilde K_R
=I_{m_R}-\frac1R\mathbf1\mathbf1^*.
}
\tag{11}
\]

Its eigenvalues are `1` with multiplicity `m_R-1` and

\[
1-\frac{m_R}{R}\ge\frac12
\tag{12}
\]

in the constant direction. In particular the raw terminal family is uniformly well conditioned.

After diagonal normalization, every off-diagonal raw correlation equals

\[
\widetilde\rho_{ij}^{(R,2)}=-\frac1{R-1}.
\tag{13}
\]

The raw normalized determinant is therefore exact:

\[
\boxed{
\det\widetilde{\mathcal R}_R
=
\left(\frac R{R-1}\right)^{m_R-1}
\frac{R-m_R}{R-1}.
}
\tag{14}
\]

In particular,

\[
-\log\det\widetilde{\mathcal R}_R
\longrightarrow
\log2-\frac12.
\tag{15}
\]

This is the correct `B=1` zeta calibration. Unlike the memory-free `O=1` control of `NB-086`, the raw zeta terminal innovations are not orthogonal; they carry a finite rank-one correlation-volume cost even on the RH branch.

## 2. Summable horizontal mass perturbs every terminal Gram entry by only `O_A(R^-1)`

The proof of `NB-089` gives more than the diagonal norm estimate recorded in its statement. After translating the support origin of the `j`th innovation to `log j`, on the fixed relative horizon `0<=u<=log2` one has

\[
D_j(\log j+u)
=
y_j(u)+r_j(u),
\tag{16}
\]

where `y_j` is the raw terminal profile from `NB-088`,

\[
y_j(u)=
\begin{cases}
\sqrt j\,e^{-u/2},&0\le u<\log(1+1/j),\\
-j^{-1/2}e^{-u/2},&\log(1+1/j)\le u\le\log2,
\end{cases}
\tag{17}
\]

and the infinite-product Volterra estimate under (1) gives

\[
\boxed{
\|r_j\|_{L^\infty(0,\log2)}\ll_A j^{-1/2}.
}
\tag{18}
\]

The same calculation in `NB-089` gives

\[
\|y_j\|_{L^1(0,\log2)}\ll j^{-1/2}.
\tag{19}
\]

Causality makes both the raw and deflated innovation vanish before `log j`, so (16) may be used directly on the global terminal window. For `i,j in I_R`, all indices are comparable to `R`. Expanding one terminal pairing and using (18)--(19),

\[
\begin{aligned}
&\left|
\langle J_RD_i,J_RD_j\rangle
-
\langle J_R\widetilde D_i,J_R\widetilde D_j\rangle
\right|\\
&\quad\le
\|r_i\|_\infty\|y_j\|_1
+\|r_j\|_\infty\|y_i\|_1
+(\log2)\|r_i\|_\infty\|r_j\|_\infty\\
&\quad\ll_A R^{-1}.
\end{aligned}
\tag{20}
\]

The estimate is uniform in both terminal indices. Combining (10) and (20),

\[
\boxed{
(K_R)_{ij}=O_A(R^{-1})
\qquad(i\ne j).
}
\tag{21}
\]

For the diagonal, `NB-089` already gives

\[
(K_R)_{jj}
=1-\frac1R+O_A(R^{-1})
=1+O_A(R^{-1}),
\tag{22}
\]

while the exact causal delay identity of `NB-088` gives the useful one-sided bound

\[
(K_R)_{jj}\ge1-\frac1R.
\tag{23}
\]

Hence normalization changes (21) only by another bounded factor, proving (5). Since `m_R asymp R`, summing `O_A(R^-2)` over `O(R^2)` off-diagonal entries proves (6).

This is precisely the matrix information absent from `NB-089`: sibling contrasts and correlations between different dyadic sibling blocks are all included in (20)--(21), not merely the average branching direction.

## 3. Inner causality prevents a hidden exponentially small eigenvalue

Bounded Frobenius correlation energy alone would not prove (4). A single eigenvalue tending to zero exponentially could leave `||mathcal R_R-I||_F` bounded while making `-log det mathcal R_R` diverge. The actual Nyman factorization excludes that failure mode by a one-sided Gram comparison.

Multiplication by the Blaschke inner factor `B` is a causal isometry and

\[
M_BD_j=\widetilde D_j.
\tag{24}
\]

Causality gives

\[
J_RM_B(I-J_R)=0,
\]

so for every coefficient vector `c=(c_j)_(j in I_R)`,

\[
J_RM_BJ_R\sum_jc_jD_j
=
J_R\sum_jc_j\widetilde D_j.
\tag{25}
\]

Because `J_RM_BJ_R` is a contraction,

\[
\left\|
J_R\sum_jc_j\widetilde D_j
\right\|
\le
\left\|
J_R\sum_jc_jD_j
\right\|.
\tag{26}
\]

Equivalently,

\[
\boxed{
K_R\succeq\widetilde K_R
\succeq\frac12 I.
}
\tag{27}
\]

Let `Delta_R` be the diagonal of `K_R`. From (22),

\[
\|\Delta_R\|_{\rm op}
\le1+C_A/R
\tag{28}
\]

for large `R`. Therefore

\[
\mathcal R_R
=\Delta_R^{-1/2}K_R\Delta_R^{-1/2}
\succeq
\frac{1}{2(1+C_A/R)}I.
\tag{29}
\]

In particular there is a constant `c_A>0`, and in fact any fixed constant below `1/2` works eventually, such that

\[
\boxed{
\lambda_{\min}(\mathcal R_R)\ge c_A>0.
}
\tag{30}
\]

This spectral floor is stronger than entrywise perturbation alone. It uses the direction of the causal inner deformation: deflating by `B` can increase the finite-prefix Gram quadratic form relative to the raw zeta prefix, but cannot collapse it below the raw rank-one matrix (11).

## 4. The complete terminal determinant entropy is uniformly bounded

Let `lambda_1,...,lambda_(m_R)` be the eigenvalues of `mathcal R_R`. Since it is a correlation matrix,

\[
\sum_{a=1}^{m_R}\lambda_a=m_R.
\tag{31}
\]

Hence

\[
-\log\det\mathcal R_R
=
\sum_a
\bigl(\lambda_a-1-\log\lambda_a\bigr).
\tag{32}
\]

By (30), all eigenvalues lie in `[c_A,m_R]`. On `[c_A,infinity)` there is a finite constant `C_A'` such that

\[
x-1-\log x
\le C_A'(x-1)^2.
\tag{33}
\]

Using (6),

\[
\begin{aligned}
-\log\det\mathcal R_R
&\le
C_A'\sum_a(\lambda_a-1)^2\\
&=
C_A'\|\mathcal R_R-I\|_F^2\\
&=
O_A(1),
\end{aligned}
\tag{34}
\]

which proves (4). Equivalently,

\[
\boxed{
\det\mathcal R_R\ge e^{-C_A}>0
}
\tag{35}
\]

uniformly for all sufficiently large dyadic terminal windows.

Combining with `NB-086`, the necessary finite-window obstruction

\[
\mathfrak S_{R,2}
\ge
-\log\det\mathcal R_R
\tag{36}
\]

cannot be made divergent under (1). This conclusion is strictly stronger than `NB-089`: it controls every direction in the terminal visible correlation matrix, including the sibling-contrast and cross-block sectors that survived the scalar reduction of `NB-087`.

## 5. Method boundary and what remains live

Equation (34) does **not** prove that the dyadic radial charge `mathfrak S_(R,2)` is bounded. The determinant in `NB-086` is only a lower bound for that charge. Earlier indices, the mismatch between the visible prediction errors and the positive aliased Szegő floors, and nonterminal/inter-scale correlations can still carry an obstruction. Nor does (34) say that the Nyman distance vanishes under (1); the hypothesis is compatible with false RH by construction.

What is ruled out is a whole proposed rescue of the current terminal route. After `NB-089`, one could still hope that the scalar average direction was accidentally blind while the discarded matrix directions forced

\[
-\log\det\mathcal R_R\to\infty.
\]

Under summable horizontal zero mass this is impossible. The full terminal matrix remains uniformly nondegenerate and has only bounded correlation-volume charge.

The new falsification boundary is therefore source-specific and clean. Any proof that tries to kill fixed-`q=2` radial screening through the `NB-086` current-window determinant must establish a condition stronger than mere nontriviality or infinitude of the off-critical Blaschke factor; in particular it must exclude (1). Otherwise the next live carriers are outside the terminal Gram block: nonterminal scale coupling, the detailed aliased floor excess, or a genuinely stronger zero-mass statistic than the unweighted horizontal sum.

## 6. Prior-art and stress-test boundary

The exact raw matrix (11) is an elementary consequence of the terminal floor profile already derived in `NB-088`; the determinant argument uses only standard Gram order, Hadamard normalization and the elementary convex function `x-1-log x`. No novelty is claimed for those ingredients. The targeted literature audit rechecked Burnol's Blaschke formulation, Ziad's finite Blaschke/Gram-spectral decomposition, and Carvill's Mellin-smoothed ladder Gram decay and block-compressibility. Those works do not supply the present finite-window statement that summable **unweighted horizontal zero mass** keeps the full canonical dyadic terminal correlation determinant uniformly away from zero. No priority claim is made.

No new specialized external theorem is load-bearing, so `SOURCES.md` requires no new anchor.

The main adversarial checks are built into the proof. First, entrywise `O(R^-1)` control alone is deliberately not used to infer a determinant bound; the causal contraction (27) supplies the missing uniform spectral floor. Second, the hypothesis (1) remains conditional and substantially stronger than the ordinary half-plane Blaschke condition. Third, the `O_A(R^-1)` pair estimate uses the fixed relative terminal horizon `log2`; no global inverse bound for `1/B` is asserted. Fourth, the exact raw entropy in (15) is positive, so boundedness of the terminal determinant charge is not confused with asymptotic orthogonality. Finally, (34) is a negative statement about the `NB-086` lower-bound channel only and is not promoted to boundedness of the complete radial prediction charge.