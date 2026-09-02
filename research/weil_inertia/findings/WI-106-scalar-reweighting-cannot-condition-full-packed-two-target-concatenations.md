# WI-106 — Scalar reweighting cannot condition full-packed two-target concatenations

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion and does not certify or repair the Yang--Yang one-sided fourth-moment candidate. It sharpens the obstruction in WI-105 from principal angles to the actual concatenated cross-Gram operator: along the WI-105 simultaneous full-packing family, **no choice of one scalar weight per target block can give a uniformly conditioned full-source-rank concatenation**.

More precisely, let

\[
G_i=(U_p^{(N)})^*U_{q_i}^{(N)},
\qquad
K_i=\ker G_i^*\subset\mathbf C^{p-1}
\qquad(i=1,2),
\tag{1}
\]

be any two finite full-packed positive-defect interactions from WI-104, and let `theta` be the smallest principal angle between `K_1` and `K_2`. For arbitrary complex scalars `a_1,a_2`, form the horizontally concatenated weighted operator

\[
B_{a_1,a_2}=[\,a_1G_1\;\;a_2G_2\,].
\tag{2}
\]

If both weights are nonzero, WI-104 gives full source row rank and hence a finite rectangular two-norm condition number

\[
\kappa_2(B_{a_1,a_2})
:=\frac{\sigma_{\max}(B_{a_1,a_2})}
        {\sigma_{\min}(B_{a_1,a_2})}.
\tag{3}
\]

Then the following weight-independent inequality holds:

\[
\boxed{
\kappa_2(B_{a_1,a_2})\ge \csc\theta.
}
\tag{4}
\]

If either scalar weight vanishes, the remaining block has a nontrivial left kernel, so the concatenation loses full source row rank; interpreting its condition number as infinite, (4) remains valid in the extended sense.

Applying (4) to the infinite arithmetic family of WI-105, where

\[
t_i=2p-q_i,
\qquad
\Delta=q_2-q_1,
\qquad
\sin^2\theta\le\frac{\Delta}{t_1},
\tag{5}
\]

gives

\[
\boxed{
\kappa_2(B_{a_1,a_2})
\ge
\sqrt{\frac{t_1}{\Delta}}.
}
\tag{6}
\]

WI-105 constructs infinitely many such configurations with `t_1>2p/3` and `Delta=O(log p)`. Therefore, **uniformly over every choice of nonzero scalar target weights**, including weights that depend arbitrarily on `p,q_1,q_2,N`,

\[
\boxed{
\kappa_2(B_{a_1,a_2})
=\Omega\!\left(\sqrt{\frac{p}{\log p}}\right)
\longrightarrow\infty.
}
\tag{7}
\]

Equivalently,

\[
\boxed{
\inf_{a_1a_2\ne0}
\frac{\sigma_{\min}([a_1G_1\;a_2G_2])}
     {\sigma_{\max}([a_1G_1\;a_2G_2])}
\le
\sqrt{\frac{\Delta}{t_1}}
\longrightarrow0.
}
\tag{8}
\]

Thus the exact full-rank restoration of WI-104 is not merely non-uniform at the level of kernel incidence: it is asymptotically ill-conditioned **after optimal scalar balancing of the two target blocks**.

## 1. A general two-block angle-to-conditioning lemma

The operator statement is elementary and does not use Ramanujan structure. Let `A_1:H_1 -> H` and `A_2:H_2 -> H` be finite-dimensional operators with nontrivial left kernels

\[
K_i=\ker A_i^*\subset H.
\tag{9}
\]

Assume `K_1 cap K_2={0}` and let `theta` be their smallest principal angle. For scalars `a_i`, put

\[
B=[a_1A_1\;a_2A_2],
\qquad
b_i=|a_i|\,\|A_i\|_2.
\tag{10}
\]

Assume first that `a_1a_2 != 0`, so in the present application `B` has full row rank. Without loss of generality suppose

\[
b_1\ge b_2.
\tag{11}
\]

Choose a unit principal vector `x in K_1` realizing the smallest angle to `K_2`. If `P_2` is the orthogonal projection onto `K_2`, then

\[
\|x-P_2x\|=\sin\theta.
\tag{12}
\]

Because `A_1^*x=0` and `A_2^*P_2x=0`,

\[
\begin{aligned}
\|B^*x\|^2
&=|a_1|^2\|A_1^*x\|^2
 +|a_2|^2\|A_2^*x\|^2\\
&=|a_2|^2\|A_2^*(x-P_2x)\|^2\\
&\le b_2^2\sin^2\theta.
\end{aligned}
\tag{13}
\]

The variational characterization of the smallest singular value therefore gives

\[
\sigma_{\min}(B)\le b_2\sin\theta.
\tag{14}
\]

On the other hand the largest singular value of the concatenation dominates that of either block:

\[
\sigma_{\max}(B)=\|B\|_2\ge b_1.
\tag{15}
\]

Using (11),

\[
\frac{\sigma_{\min}(B)}{\sigma_{\max}(B)}
\le
\frac{b_2}{b_1}\sin\theta
\le\sin\theta,
\tag{16}
\]

which is (4). If `b_2>=b_1`, interchange the two blocks and use a principal vector in `K_2`. Thus **arbitrary scalar rebalancing cannot improve the relative gap past the sine of the kernel angle**. In fact an imbalanced choice only strengthens the upper bound through the extra factor `min(b_1,b_2)/max(b_1,b_2)`.

A useful normalized corollary is obtained by choosing

\[
a_i=\|A_i\|_2^{-1}.
\tag{17}
\]

Even after each target block has unit operator norm,

\[
\boxed{
\frac{\sigma_{\min}([A_1/\|A_1\|\;A_2/\|A_2\|])}
     {\sigma_{\max}([A_1/\|A_1\|\;A_2/\|A_2\|])}
\le\sin\theta.
}
\tag{18}
\]

This closes the most immediate normalization loophole left explicitly open in WI-105.

## 2. Specialization to the WI-105 arithmetic family

WI-105 gives an infinite sequence of simultaneous full-packed triples `(p,q_1,q_2,N)` with

\[
p<q_1<q_2<\frac{4p}{3},
\qquad
\Delta=q_2-q_1=O(\log p),
\tag{19}
\]

and positive-defect source kernels `K_i` satisfying both

\[
K_1\cap K_2=\{0\}
\tag{20}
\]

and

\[
\cos\theta
\ge\sqrt{\frac{t_2}{t_1}},
\qquad
 t_i=2p-q_i.
\tag{21}
\]

Since `t_1-t_2=Delta`,

\[
\sin^2\theta
\le1-\frac{t_2}{t_1}
=\frac{\Delta}{t_1}.
\tag{22}
\]

Substitution into the general lemma gives (6). Because `q_1<4p/3`,

\[
t_1=2p-q_1>\frac{2p}{3},
\tag{23}
\]

so

\[
\boxed{
\kappa_2(B_{a_1,a_2})
\ge
\sqrt{\frac{2p}{3\Delta}}.
}
\tag{24}
\]

The fixed-modulus-three prime-selection argument in WI-105 supplies `Delta=O(log p)`, proving (7). No estimate for the individual nonzero singular values of either cross Gram is needed; the result follows solely from the exact kernels plus the operator variational principle.

This is stronger than merely saying that the left kernels become nearly parallel. The concatenation itself remains full source row rank for every finite member, but its **best possible scalar-balanced relative singular gap goes to zero**.

## 3. Stress tests and equality boundaries

The proof has only three possible places where slack can occur: the chosen principal vector may fail to be a top right singular direction for the restriction of `A_2^*` to `K_2^perp`; the larger weighted block norm in (15) may exceed the actual contribution relevant to the minimizing source vector; and the WI-105 character witness provides an upper bound on `sin(theta)` rather than necessarily the exact principal angle. None of these affects the obstruction because every step goes in the direction needed for an **upper** bound on the relative smallest singular value.

The scalar-weight quantifier is also exact. If one weighted block dominates in operator norm, the factor `min(b_1,b_2)/max(b_1,b_2)` in (16) only makes the relative gap smaller. The most favorable scalar balancing permitted by this proof is therefore `b_1=b_2`; even there the `csc(theta)` condition-number barrier remains.

As a falsification check, the general lemma was tested on finite random matrices constructed with prescribed nontrivial left kernels and widely imbalanced scalar weights. The numerical inequalities agreed in every tested instance, but this computation is not evidence for the theorem and is not used in the derivation above.

The result does **not** imply

\[
\sigma_{\min}([G_1\;G_2])\to0
\tag{25}
\]

in absolute, unnormalized units. WI-105 correctly left that stronger statement open: the operator norms may grow with the arithmetic scale. What is now ruled out is a uniform **relative** spectral gap, even after arbitrary scalar target reweighting.

## 4. Prior art and novelty boundary

Principal angles and their computation through singular values are classical; WI-105 already cited A. Björck and G. H. Golub, **Numerical methods for computing angles between linear subspaces**, *Mathematics of Computation* 27:123 (1973), 579--594, DOI `10.1090/S0025-5718-1973-0348991-3`.

The broader inverse relationship between small subspace angles and matrix conditioning is also classical. In particular, J. W. Demmel, **The Condition Number of Equivalence Transformations That Block Diagonalize Matrix Pencils**, *SIAM Journal on Numerical Analysis* 20:3 (1983), 599--610, DOI `10.1137/0720040`, shows in a block-diagonalization setting that the best achievable conditioning is governed, up to the formulation-specific constants, by the cosecant of the smallest angle between the prescribed subspaces. That paper is prior art for the general `csc(theta)` conditioning phenomenon, not for the Ramanujan/full-packing specialization here.

A targeted search around principal angles, Friedrichs angles, null spaces, concatenated operators, and smallest singular values located the classical conditioning literature but did not locate the specific weighted-concatenation statement (4) attached to finite-window Ramanujan cross Grams, nor the arithmetic divergence (6)--(7). This negative search is **not** a claim of priority. The durable contribution here is the self-contained elementary lemma and its exact specialization to the already-established WI-105 arithmetic family.

## 5. Program consequence and evidence boundary

WI-105 listed singular-value/operator weights and coefficient-weighted target aggregation among possible ways to extract quantitative information beyond bare kernel incidence. The present result separates that frontier more sharply.

A route that keeps each target cross Gram intact and changes only one scalar coefficient per target cannot obtain a uniform coercivity estimate of the form

\[
\sigma_{\min}([a_1G_1\;a_2G_2])
\ge c\,\sigma_{\max}([a_1G_1\;a_2G_2])
\tag{26}
\]

with a fixed `c>0` over the full-packed arithmetic family. Equation (7) rules this out for **every** scalar weighting rule, including arithmetic-dependent rules chosen after seeing the moduli.

This does not close genuinely operator-sensitive escapes. A future Yang or multi-target covariance argument may still exploit non-scalar diagonal/internal weights inside a target block, detailed singular-vector alignment, absolute rather than relative scale together with an independent normalization from the analytic problem, positive-slack layers away from full packing, or simultaneous coupling of three or more targets. Those mechanisms carry information absent from the two-subspace scalar-balancing problem.

The decisive falsification test for a proposed quantitative use of WI-104 is therefore stronger than in WI-105: if the claimed uniform gain survives only by rescaling whole target blocks, evaluate its normalized concatenation on the WI-105 modulus-three family. Any fixed relative singular gap contradicts (6)--(8).