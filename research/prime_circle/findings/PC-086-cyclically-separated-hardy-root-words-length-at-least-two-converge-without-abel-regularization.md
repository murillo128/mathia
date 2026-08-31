# PC-086 — cyclically separated Hardy root words of length at least two converge without Abel regularization

**Status:** `EXACT-DERIVED` + `CORRECTION` + `NOVELTY-CORRECTION` + `PRIOR-ART-REDIRECTION`. This finding replaces the withdrawn PC-083 after adversarial review exposed a missing length hypothesis. The corrected ordinary-trace theorem is exact for cyclically separated root words of length `k>=2`; the scalar finite-section formula also converges for a separated one-letter channel, but that operator is not trace class and therefore has no ordinary operator trace. No theorem-level historical novelty is claimed.

PC-082 represented cyclically separated Hardy root-channel traces by a radial/Abel limit and treated that prescription as essential because the associated critical cone series is not absolutely convergent. The substantive correction survives, but only once the operator word contains at least two factors:

\[
\boxed{
\text{cyclic separation + }k\ge2
\Longrightarrow
\text{ordinary trace-class Hardy word and ordinary finite-section convergence}.
}
\]

For `k=1`, cyclotomic oscillation can make the **scalar diagonal finite sections** converge, but it does not make the Hilbert channel trace class. That distinction is the exact boundary missed by PC-083.

## 1. Corrected root-channel theorem

For a unit complex number `alpha`, define

\[
(\mathcal H_\alpha)_{jk}
=\frac{\alpha^{j+k+1}}{j+k+1},
\qquad j,k\ge0.
\]

Let

\[
k\ge2,
\qquad
|\alpha_i|=1,
\qquad
\alpha_i\alpha_{i+1}\neq1
\quad(i\bmod k).
\]

If `P_N` is the orthogonal projection onto `span{e_0,...,e_N}`, then

\[
\boxed{
\left\|
P_N\mathcal H_{\alpha_1}P_N\cdots
P_N\mathcal H_{\alpha_k}P_N
-
\mathcal H_{\alpha_1}\cdots\mathcal H_{\alpha_k}
\right\|_{\mathcal S_1}
\longrightarrow0.
}
\]

Consequently the ordinary traces exist and

\[
\boxed{
\lim_{N\to\infty}
\operatorname{Tr}
\bigl(P_N\mathcal H_{\alpha_1}P_N\cdots
P_N\mathcal H_{\alpha_k}P_N\bigr)
=
\operatorname{Tr}
\bigl(\mathcal H_{\alpha_1}\cdots\mathcal H_{\alpha_k}\bigr).
}
\]

Their common value is the same cyclotomic cube period used in PC-082:

\[
\boxed{
\left(\prod_{i=1}^k\alpha_i\right)
\int_{[0,1]^k}
\prod_{i=1}^k
\frac{dx_1\cdots dx_k}
{1-\alpha_i\alpha_{i+1}x_ix_{i+1}}.
}
\]

Thus Abel damping is not needed to define the separated **multi-factor** operator trace.

## 2. Why `k>=2` supplies an ordinary trace

Write

\[
A_i=\mathcal H_{\alpha_i}.
\]

Cyclic separation gives in particular

\[
\alpha_1\alpha_2\neq1.
\]

PC-080 proves that a separated root pair satisfies

\[
A_1A_2\in\mathcal S_1,
\]

and PC-084 strengthens this at the natural Hardy cutoff to

\[
\boxed{
\|P_NA_1P_NA_2P_N-A_1A_2\|_1\to0.
}
\]

Every `A_i` is bounded. The remaining compressed factors converge strong-* to their limiting factors and are uniformly bounded. The standard two-sided ideal continuity of `S_1` therefore gives

\[
P_NA_1P_NA_2P_NA_3P_N\cdots A_kP_N
\longrightarrow
A_1A_2\cdots A_k
\]

in trace norm. In particular,

\[
\boxed{A_1\cdots A_k\in\mathcal S_1.}
\]

This supplies the operator-theoretic bridge that the original PC-083 statement lacked at `k=1`. It also shows that the corrected theorem does not rely merely on convergence of a scalar multiple series: the limiting multi-factor operator itself is trace class.

The argument only needs one separated adjacent pair to create the nuclear core. Full cyclic separation is retained here because it is exactly the hypothesis needed for the root-wise cube-period formula below.

## 3. Exact finite-section cube formula

Put

\[
A=\prod_{i=1}^k\alpha_i,
\qquad
\delta_i=\alpha_{i-1}\alpha_i
\quad(i\bmod k).
\]

The cyclic-separation condition is

\[
\delta_i\neq1
\qquad\text{for every }i.
\]

Expanding the finite trace gives

\[
S_N
:=
\operatorname{Tr}
\bigl(P_N\mathcal H_{\alpha_1}P_N\cdots
      P_N\mathcal H_{\alpha_k}P_N\bigr)
=
\sum_{0\le j_1,\ldots,j_k\le N}
\prod_{i=1}^k
\frac{\alpha_i^{j_i+j_{i+1}+1}}
{j_i+j_{i+1}+1}.
\]

Every `j_i` occurs once with `alpha_{i-1}` and once with `alpha_i`, so

\[
\prod_i\alpha_i^{j_i+j_{i+1}+1}
=A\prod_i\delta_i^{j_i}.
\]

Using

\[
\frac1{j_i+j_{i+1}+1}
=
\int_0^1x_i^{j_i+j_{i+1}}\,dx_i,
\]

we obtain the exact identity

\[
\boxed{
S_N
=
A\int_{[0,1]^k}
\prod_{i=1}^k
\left(
\sum_{j=0}^N
(\delta_i x_{i-1}x_i)^j
\right)
\,dx_1\cdots dx_k.
}
\]

For a fixed unit `delta!=1`,

\[
c_\delta
:=
\min_{0\le t\le1}|1-\delta t|>0
\]

and therefore

\[
\left|
\sum_{j=0}^N(\delta t)^j
\right|
\le\frac2{c_\delta}
\qquad(0\le t\le1),
\]

uniformly in `N`. Away from a measure-zero union of boundary faces,

\[
(\delta_i x_{i-1}x_i)^{N+1}\to0.
\]

Dominated convergence yields

\[
\boxed{
\lim_{N\to\infty}S_N
=
A\int_{[0,1]^k}
\prod_{i=1}^k
\frac{dx_1\cdots dx_k}
{1-\delta_i x_{i-1}x_i}.
}
\]

Relabeling the cyclic indices gives the PC-082 cube period in Section 1. Because Section 2 independently proves that the limiting word is trace class and that the compressed words converge to it in `S_1`, this scalar limit is indeed its **ordinary operator trace**.

The same dominated-convergence argument works for rectangular cutoffs `0<=j_i<=N_i` with every `N_i->infinity`. Thus the separated multi-index series has genuine Pringsheim/rectangular convergence, not merely Abel summability.

## 4. The one-letter counterexample and exact boundary

For `k=1`, the formal cyclic-separation condition becomes

\[
\alpha^2\neq1.
\]

The finite diagonal sums are

\[
S_N^{(1)}
=
\operatorname{Tr}(P_N\mathcal H_\alpha P_N)
=
\sum_{j=0}^N
\frac{\alpha^{2j+1}}{2j+1}.
\]

If `alpha^2!=1`, bounded geometric partial sums give ordinary conditional convergence, equivalently

\[
\boxed{
S_N^{(1)}
\longrightarrow
\alpha\int_0^1\frac{dx}{1-\alpha^2x^2}.
}
\]

But

\[
\mathcal H_\alpha
=\alpha D_\alpha H D_\alpha,
\qquad
D_\alpha e_j=\alpha^j e_j,
\]

where

\[
H_{jk}=\frac1{j+k+1}
\]

is the classical Hilbert matrix. The outer diagonal operators are unitary, so `mathcal H_alpha` has exactly the same singular values as `H`. The Hilbert matrix is the classical bounded non-compact Hankel operator with continuous spectrum reaching `[0,pi]`; in particular it is not compact and hence cannot be trace class. Therefore

\[
\boxed{
\alpha^2\neq1,\ k=1:
\quad
\text{the scalar finite-section limit exists, but }
\operatorname{Tr}(\mathcal H_\alpha)
\text{ is not an ordinary operator trace}.
}
\]

This is not a merely terminological issue. It separates two genuinely different statements:

\[
\boxed{
\text{conditional convergence of selected diagonal sums}
\not\Rightarrow
\text{trace-classness of the operator}.
}
\]

For `alpha=1` or `alpha=-1`, even the scalar finite diagonal sums diverge logarithmically, so there is no missing separated one-letter case there.

## 5. Completed primitive shells remain covered in their intended domain

Recall

\[
\Gamma_n
=-\sum_{\alpha\in P_n^*}\mathcal H_\alpha.
\]

Let `k>=2` and suppose shell orders `n_1,...,n_k` are cyclically adjacent and distinct. For every choice

\[
\alpha_i\in P_{n_i}^*,
\]

reciprocity `alpha_{i+1}=alpha_i^{-1}` would force equal exact orders, so

\[
\alpha_i\alpha_{i+1}\neq1.
\]

There are only finitely many primitive roots in each shell. Summing the corrected root theorem over those choices gives

\[
\boxed{
\operatorname{Tr}
\bigl(P_N\Gamma_{n_1}P_N\cdots
      P_N\Gamma_{n_k}P_N\bigr)
\longrightarrow
\operatorname{Tr}
\bigl(\Gamma_{n_1}\cdots\Gamma_{n_k}\bigr).
}
\]

Thus the multi-shell applications intended by the withdrawn PC-083 are unchanged. At `k=2`, this recovers the PC-080 resultant trace without a radial limit. PC-084 then goes further: after complete shells are assembled, every finite **nonconstant** mixed-shell word converges in trace norm under the same natural finite sections, even if a root-wise cyclic separation condition fails at a repeated-shell junction.

No one-shell ordinary trace is asserted here.

## 6. Critical homogeneity still survives

For `k>=2`, the absolute value of each root-word series term is

\[
\prod_{i=1}^k\frac1{j_i+j_{i+1}+1}.
\]

On the dyadic block

\[
R\le j_i<2R
\qquad\text{for every }i,
\]

there are `R^k` lattice points and each denominator factor is at most `4R+1`. Hence

\[
\sum_{R\le j_i<2R}
\prod_i\frac1{j_i+j_{i+1}+1}
\ge
\frac{R^k}{(4R+1)^k},
\]

which is bounded below by a positive constant along disjoint dyadic blocks. Therefore

\[
\boxed{
\sum_{j_1,\ldots,j_k\ge0}
\left|
\prod_i
\frac{\alpha_i^{j_i+j_{i+1}+1}}
{j_i+j_{i+1}+1}
\right|
=\infty.
}
\]

The corrected result does not remove the criticality detected in PC-082. It says instead that nontrivial root-of-unity characters provide enough multidimensional Dirichlet cancellation to make the natural operator ordering converge when an ordinary trace-class word exists.

## 7. Prior-art and novelty audit

Nothing in this correction supports a theorem-level novelty claim.

1. The classical Hilbert matrix is a standard non-compact Hankel operator; its continuous/absolutely continuous spectrum `[0,pi]` and explicit spectral theory are classical. This is the decisive prior-art fact behind the `k=1` counterexample.
2. Trace class as a two-sided ideal, finite-rank approximation in `S_1`, and strong-* continuity around a fixed trace-class core are standard trace-ideal facts. PC-084 already uses exactly this mechanism for completed mixed-shell words.
3. Root-of-unity Dirichlet cancellation and conditional cyclotomic multiple sums are classical. Terasoma's rational-cone reduction, already anchored in `SOURCES.md`, assumes absolute convergence in the relevant general theorem and therefore does not by itself identify the present critical conditional values.
4. The surrounding multichannel Hankel localization literature already anchored for PC-080/PC-084 makes trace-class separation between distinct oscillatory singular channels unsurprising. The Prime-Circle specialization is an exact bookkeeping result, not evidence of historical novelty.
5. A targeted literature check of the Hilbert matrix confirms that non-compactness, rather than any subtle arithmetic feature, is the entire obstruction in the one-letter channel. No special trace notion is introduced here to rescue `k=1`.

The durable result is therefore a corrected **scope classification**: separated finite Hardy words of length at least two have canonical ordinary traces selected by the Prime-Circle Hardy cutoff, whereas a separated one-letter scalar diagonal limit is only a conditional summation value.

## 8. RH relevance

The correction weakens rather than strengthens the RH interpretation. In the separated finite-word sector, Abel regularization supplies no intrinsic complex spectral parameter, gamma factor, functional equation, or critical-line symmetry. The natural Hardy cutoff already determines the multi-factor trace, while the one-factor channel shows that conditional finite-section summability alone is too weak to define an operator-theoretic spectral invariant.

The finite mixed Hardy algebra can still contain information beyond pairwise cyclotomic resultants, as PC-082/PC-084 demonstrate, but any route to zeta must come from additional cross-level/infinite-shell structure rather than from mistaking conditional diagonal convergence for an ordinary trace.

## Falsification surface

The corrected theorem has seven direct audit points.

1. The operator-trace claim must always include `k>=2`.
2. Cyclic separation must imply at least one adjacent pair `alpha_i alpha_{i+1}!=1`, giving an `S_1` core.
3. The PC-084 separated-pair finite-section estimate must converge in trace norm.
4. The exact finite trace expansion must carry `delta_i^{j_i}` with `delta_i=alpha_{i-1}alpha_i` and factor into the geometric sums above.
5. For every `delta_i!=1`, `min_{0<=t<=1}|1-delta_i t|` must be positive, giving the uniform dominated-convergence bound.
6. For `k=1` and `alpha^2!=1`, the scalar diagonal sequence must converge while `mathcal H_alpha` remains non-compact/not trace class.
7. Absolute convergence must fail on dyadic boxes for the multi-factor series, so the result may not be upgraded to an order-independent absolutely convergent conical zeta value.

Failure of points 1--6 invalidates the corrected operator statement. Failure of point 7 would alter the prior-art classification but not the trace-norm convergence theorem.

## Research consequence

The exact correction to the Hardy branch is

\[
\boxed{
\begin{array}{ll}
\text{cyclically separated root words, }k\ge2
&\to\text{ordinary trace-class finite-section limits},\\[3pt]
\text{separated one-letter root channel}
&\to\text{conditional scalar finite-section limit only},\\[3pt]
\text{finite nonconstant completed-shell words}
&\to\text{ordinary trace-norm limits by PC-084},\\[3pt]
\text{pure same-shell words}
&\to\text{no mixed trace-class core supplied here}.
\end{array}
}
\]

Accordingly, Abel damping remains a safe representation but is not necessary for the separated multi-factor trace. The one-letter exception is an operator-domain boundary, not a new arithmetic mechanism.