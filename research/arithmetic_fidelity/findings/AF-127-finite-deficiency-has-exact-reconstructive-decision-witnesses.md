# AF-127 — Finite recovery deficiency has exact reconstructive decision witnesses

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `QUANTITATIVE-FIDELITY`, `DECISION-WITNESS`, `NO-NOVELTY-CLAIM`

## Claim

AF-126 identifies the one-sided Le Cam recovery deficiency as the correct finite whole-experiment defect for approximate statistical fidelity. In finite spaces that defect has an exact dual interpretation: **every positive recovery deficiency is witnessed by one bounded reconstructive decision problem.**

Let

\[
\mathcal E=(P_\theta)_{\theta\in\Theta}
\]

be a statistical experiment on a finite sample space `X`, with finite parameter set `Theta`. Let

\[
K:X\rightsquigarrow Y
\]

be a stochastic compression and write

\[
Q_\theta=P_\theta K.
\]

Using normalized total variation,

\[
\|P-Q\|_{\rm TV}
:=\frac12\sum_x|P(x)-Q(x)|,
\]

define the recovery deficiency as in AF-126:

\[
\delta_{\rm rec}(K;\mathcal E)
:=
\inf_{R:Y\rightsquigarrow X}
\sup_{\theta\in\Theta}
\|P_\theta-Q_\theta R\|_{\rm TV}.
\tag{1}
\]

For a prior `lambda in Delta(Theta)` and a bounded payoff table

\[
u:\Theta\times X\to[-1,1],
\]

define the reward of the **identity reconstruction rule** on the original experiment by

\[
V_{\rm id}(\mathcal E;\lambda,u)
:=
\sum_{\theta,x}
\lambda_\theta P_\theta(x)u(\theta,x),
\tag{2}
\]

and the optimal reward obtainable from the compressed observation by

\[
V^*(\mathcal E K;\lambda,u)
:=
\sum_{y\in Y}
\max_{a\in X}
\sum_{\theta\in\Theta}
\lambda_\theta Q_\theta(y)u(\theta,a).
\tag{3}
\]

The action alphabet in `(3)` is a reconstructed symbol `a in X`. Randomized actions cannot improve `(3)` because the finite objective is linear in the action distribution.

Then

\[
\boxed{
2\,\delta_{\rm rec}(K;\mathcal E)
=
\max_{\lambda\in\Delta(\Theta)}
\max_{u\in[-1,1]^{\Theta\times X}}
\left[
V_{\rm id}(\mathcal E;\lambda,u)
-
V^*(\mathcal E K;\lambda,u)
\right].
}
\tag{4}
\]

Equivalently, write

\[
\ell(\theta,x)=\frac{1-u(\theta,x)}2\in[0,1]
\]

and define

\[
\mathcal R_{\rm id}(\mathcal E;\lambda,\ell)
:=
\sum_{\theta,x}
\lambda_\theta P_\theta(x)\ell(\theta,x),
\tag{5}
\]

while the optimal Bayes risk from compressed data is

\[
\mathcal R^*(\mathcal E K;\lambda,\ell)
:=
\sum_{y\in Y}
\min_{a\in X}
\sum_{\theta\in\Theta}
\lambda_\theta Q_\theta(y)\ell(\theta,a).
\tag{6}
\]

Then `(4)` is exactly

\[
\boxed{
\delta_{\rm rec}(K;\mathcal E)
=
\max_{\lambda\in\Delta(\Theta)}
\max_{\ell\in[0,1]^{\Theta\times X}}
\left[
\mathcal R^*(\mathcal E K;\lambda,\ell)
-
\mathcal R_{\rm id}(\mathcal E;\lambda,\ell)
\right].
}
\tag{7}
\]

Thus a compression is `epsilon`-recoverable for the entire finite experiment if and only if **no bounded reconstruction loss and no prior can force a Bayes-risk penalty larger than `epsilon` relative to observing and returning the original sample itself**.

In particular,

\[
\delta_{\rm rec}>0
\]

always has a finite certificate consisting of one prior `lambda` and one bounded loss table `ell`. This certificate can exist even when a selected pairwise discrimination score is preserved exactly. Therefore the zero pairwise-TV lower bound exhibited in AF-126 does not mean that the positive whole-experiment defect is witnessless; it means only that the chosen scalar decision family is too small.

The minimax/randomization mathematics behind `(4)`–`(7)` is classical finite statistical decision theory and Le Cam deficiency. No novelty is claimed for that theory. The Arithmetic Fidelity use is to turn AF-126's abstract reverse-simulation distance into an exact **task witness**: loss of family-level fidelity is equivalent to the existence of a bounded decision problem that exposes precisely that loss.

## Derivation

### Total variation turns the worst reconstruction error into a bilinear game

For any fixed reverse channel `R`, finite total-variation duality gives

\[
\|P_\theta-Q_\theta R\|_{\rm TV}
=
\frac12
\max_{|h_\theta(x)|\le1}
\sum_x
\left(P_\theta(x)-(Q_\theta R)(x)\right)h_\theta(x).
\tag{8}
\]

The maximum over `theta` can itself be written as a maximum over a prior concentrated on any worst parameter. It is convenient to absorb the prior into the test functions. Define the compact convex set

\[
\mathcal C
:=
\left\{(\lambda,r):
\lambda_\theta\ge0,
\ \sum_\theta\lambda_\theta=1,
\ |r_{\theta x}|\le\lambda_\theta
\right\}.
\tag{9}
\]

For every reverse channel `R`,

\[
\sup_\theta
\|P_\theta-Q_\theta R\|_{\rm TV}
=
\max_{(\lambda,r)\in\mathcal C}
\Phi(R,\lambda,r),
\tag{10}
\]

where

\[
\Phi(R,\lambda,r)
:=
\frac12
\left[
\sum_{\theta,x}P_\theta(x)r_{\theta x}
-
\sum_{\theta,y,x}
Q_\theta(y)R(x\mid y)r_{\theta x}
\right].
\tag{11}
\]

To see the `<=` direction of `(10)`, whenever `lambda_theta>0` set

\[
h_\theta(x)=r_{\theta x}/\lambda_\theta.
\]

Then `|h_theta(x)|<=1`, so each weighted term is at most `lambda_theta` times the corresponding total variation, and their sum is at most the largest total variation. Terms with `lambda_theta=0` vanish.

For the reverse inequality, choose a parameter attaining the finite maximum in `(10)`, put all prior mass on it, and choose a sign function attaining the `l^1` dual in `(8)`. Hence `(10)` is exact rather than merely a lower bound.

### Finite minimax exchanges recovery and witness selection

The set of stochastic matrices `R:Y\rightsquigarrow X` is a compact convex product of simplices. The set `C` is also compact and convex, and `Phi` is continuous and bilinear. Finite-dimensional minimax therefore yields

\[
\begin{aligned}
\delta_{\rm rec}(K;\mathcal E)
&=
\min_R\max_{(\lambda,r)\in\mathcal C}
\Phi(R,\lambda,r)\\
&=
\max_{(\lambda,r)\in\mathcal C}
\min_R
\Phi(R,\lambda,r).
\end{aligned}
\tag{12}
\]

For fixed `(lambda,r)`, define

\[
c_{yx}:=
\sum_\theta Q_\theta(y)r_{\theta x}.
\tag{13}
\]

The rows of `R` separate. Since each row is a probability vector,

\[
\max_{R(\cdot\mid y)}
\sum_x R(x\mid y)c_{yx}
=
\max_x c_{yx}.
\tag{14}
\]

Consequently

\[
\boxed{
\delta_{\rm rec}
=
\frac12
\max_{(\lambda,r)\in\mathcal C}
\left[
\sum_{\theta,x}P_\theta(x)r_{\theta x}
-
\sum_y\max_x
\sum_\theta Q_\theta(y)r_{\theta x}
\right].
}
\tag{15}
\]

This formula already exhibits the dual witness. The first term scores the true source symbol. The second asks how well any reconstruction from the compressed symbol can score against the same table.

### Rescaling the dual variables gives the decision problem

For every `theta` with `lambda_theta>0`, write

\[
r_{\theta x}=\lambda_\theta u(\theta,x),
\qquad
|u(\theta,x)|\le1.
\tag{16}
\]

When `lambda_theta=0`, the corresponding values of `u` are irrelevant and may be chosen arbitrarily in `[-1,1]`.

Substituting `(16)` into `(15)` gives

\[
\delta_{\rm rec}
=
\frac12
\max_{\lambda,u}
\left[
\sum_{\theta,x}\lambda_\theta P_\theta(x)u(\theta,x)
-
\sum_y\max_x
\sum_\theta\lambda_\theta Q_\theta(y)u(\theta,x)
\right],
\tag{17}
\]

which is exactly `(4)`.

The maximization over `x` in the compressed term is the optimal deterministic decision after seeing `y`. A randomized reconstruction is merely a convex combination of those action scores and therefore cannot exceed the best deterministic action for that `y`.

### Payoffs and losses differ only by an affine normalization

Set

\[
u=1-2\ell.
\tag{18}
\]

Because every `P_theta`, `Q_theta`, and prior `lambda` is normalized,

\[
V_{\rm id}
=1-2\mathcal R_{\rm id},
\tag{19}
\]

and

\[
V^*
=1-2\mathcal R^*.
\tag{20}
\]

Therefore

\[
V_{\rm id}-V^*
=2(\mathcal R^*-\mathcal R_{\rm id}),
\tag{21}
\]

and `(7)` follows from `(4)`.

The sign is important. The original-data benchmark in `(5)` is not the Bayes-optimal rule for an arbitrary decision problem. It is the **identity reconstruction rule**, because deficiency `(1)` asks whether compressed data can regenerate the original experiment. The theorem therefore compares the best reconstruction-based action from `Y` with the specific action `a=x` available when the original observation `x` is known.

## Why pairwise discrimination can miss the exact witness

AF-126 derives the pairwise total-variation lower bound

\[
\delta_{\rm rec}(K;\mathcal E)
\ge
\frac12
\left[
\|P_\theta-P_{\theta'}\|_{\rm TV}
-
\|Q_\theta-Q_{\theta'}\|_{\rm TV}
\right]
\tag{22}
\]

for every pair of hypotheses. That bound uses a very restricted class of witnesses: one pair of parameters and one binary discrimination geometry.

AF-012 supplies a binary compression for which total variation between the two hypotheses is preserved exactly even though the compression is not sufficient. AF-126 then implies

\[
\delta_{\rm rec}>0
\]

while every instance of `(22)` available in that binary experiment is zero.

Equation `(7)` closes the apparent gap. Because the finite maximum is attained, there must exist a prior and a bounded `X`-valued reconstruction loss for which

\[
\mathcal R^*(\mathcal E K;\lambda,\ell)
-
\mathcal R_{\rm id}(\mathcal E;\lambda,\ell)
=
\delta_{\rm rec}>0.
\tag{23}
\]

So preservation of one divergence or one pairwise discrimination score does not imply absence of a decision-theoretic witness. It says only that the witness may require a richer loss geometry than that selected scalar statistic exposes.

## Relationship to AF-013 and AF-126

AF-013 gives the exact zero-loss structural criterion for a finite experiment: one reverse channel reconstructs all hypotheses exactly if and only if the full vector of reference-relative likelihood ratios survives the compression.

AF-126 relaxes that boundary quantitatively by measuring the smallest worst-case total-variation error of one common reverse channel. It also shows that selected pairwise total-variation losses lower-bound but do not determine the whole-experiment defect.

AF-127 supplies the exact finite dual of that defect. The three statements fit together as

\[
\text{likelihood-ratio sufficiency}
\Longleftrightarrow
\delta_{\rm rec}=0
\Longleftrightarrow
\text{no positive bounded reconstructive decision gap},
\tag{24}
\]

while for approximate fidelity

\[
\delta_{\rm rec}
=
\text{largest bounded reconstructive Bayes-risk gap}.
\tag{25}
\]

This is a stronger audit principle than preserving a selected scalar observable: either exhibit a reverse channel giving a uniform upper bound on the entire experiment, or search for an admissible decision witness giving a lower bound. In the unrestricted finite decision class the two sides meet exactly by minimax.

## Prior art and novelty assessment

The underlying comparison-of-experiments framework is classical.

- David Blackwell, **“Equivalent Comparisons of Experiments,”** *The Annals of Mathematical Statistics* 24(2), 265–272 (1953), DOI `10.1214/aoms/1177729032`. Role: exact comparison/randomization boundary underlying zero deficiency and sufficiency.
- Lucien Le Cam, **“Sufficiency and Approximate Sufficiency,”** *The Annals of Mathematical Statistics* 35(4), 1419–1455 (1964), DOI `10.1214/AOMS/1177700372`. Role: foundational approximate-sufficiency and deficiency framework.
- Erik Torgersen, ***Comparison of Statistical Experiments***, Cambridge University Press (1991), Chapter 6, **“Deficiencies,”** DOI `10.1017/CBO9780511666353.007`. Role: systematic treatment of deficiencies through randomizations, risks, Bayes risks, performance functions, and restricted classes of decision problems.

Equation `(7)` should therefore be read as a finite reconstructive specialization and direct minimax/linear-programming derivation of classical deficiency duality, not as a new theorem of statistical decision theory. The Mathia-specific value is organizational: it identifies the exact witness language that complements AF-126's reverse-channel metric and prevents a preserved scalar divergence from being mistaken for approximate fidelity of the whole declared control family.

## Boundary conditions and falsification checks

The theorem has several important boundaries.

1. **Finite spaces are essential to this proof as written.** Compactness, attainment, rowwise optimization, and the minimax exchange are immediate in finite dimensions. Infinite experiments require measurable decision rules and appropriate topological or domination hypotheses and belong to the full Le Cam theory.

2. **The action alphabet is deliberately `X`.** This is enough because the reverse channel in `(1)` is itself an `X`-valued randomized decision rule. The theorem is about reconstructing the original observation, not about claiming that every general statistical decision problem literally has action space `X`.

3. **The benchmark rule on the original experiment is the identity rule.** Replacing `R_id` by the Bayes-optimal risk over all original-data decision rules changes the statement into a broader comparison-of-experiments theorem and should be justified separately rather than inferred from `(7)`.

4. **The full bounded loss class matters.** Restricting `ell` to pairwise tests, one divergence family, linear scores, or another structured subclass can lower the maximum and may miss positive deficiency. Such restricted witness classes are mathematically interesting only after their admissibility and completeness are stated explicitly.

5. **No efficient large-scale algorithm is claimed.** Equation `(15)` is an exact finite convex/minimax certificate. Computational tractability for large `Theta`, `X`, or `Y` is a separate question.

6. **The witness does not create lost information.** It certifies a gap already present in the reverse-simulation problem. Downstream post-processing without a new side channel cannot erase that positive deficiency by AF-126.

A direct falsification test for `(4)` or `(7)` on any finite instance is to formulate `(1)` as a linear program and independently formulate `(15)` as its dual. Any mismatch in optimum values would refute the claimed normalization or minimax derivation.

## Consequences for Arithmetic Fidelity

The result gives a practical two-sided language for approximate finite fidelity. A proposed compression may be supported from above by constructing one reverse channel with small worst-case error, while failure may be certified from below by one bounded decision witness. This is more informative than monitoring a convenient divergence whose equality or near-equality may fail to control the whole declared family.

For later arithmetic applications with finite matched-control panels, the same distinction should be enforced. A claim that a prime discriminator approximately survives a compression is strong only if it concerns the declared control family and an admissible recovery category; preservation of a selected moment, divergence, spectrum statistic, or pairwise score is not automatically a whole-family guarantee.

The next structural question is therefore not whether deficiency already has a decision interpretation—it does, classically—but **which decision witnesses remain admissible after imposing the naturality, symmetry, locality, positivity, spectral, or arithmetic constraints of a concrete mathematical compression.** That restricted-witness problem is where a genuinely line-specific fidelity boundary could remain after the classical Le Cam theory is accounted for.