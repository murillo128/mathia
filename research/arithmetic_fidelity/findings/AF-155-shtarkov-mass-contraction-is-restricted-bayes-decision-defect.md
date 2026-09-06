# AF-155 — Shtarkov mass contraction is a restricted Bayes decision defect

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `EXACT-DERIVED`, `QUANTITATIVE-FIDELITY`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-150 identifies the logarithm of the Shtarkov mass as maximal leakage, while AF-154 shows that stochastic compression acts on the max-normalized likelihood ray by conditional averaging and that the resulting radial retreat is strictly weaker than full experiment loss. The radial quantity itself has an exact decision-theoretic meaning: it is the Bayes risk of one particular source-induced gain/loss problem on the likelihood ray.

Let

\[
\mathcal E=(P_i)_{i=1}^m
\]

be a finite statistical experiment on a finite set `X`. Define

\[
s(x):=\max_iP_i(x),
\qquad
C_X:=\sum_xs(x),
\qquad
M(x):=\frac{s(x)}{C_X},
\tag{1}
\]

and on the union of the experiment supports let

\[
U_i(x):=\frac{P_i(x)}{s(x)}.
\tag{2}
\]

Thus `0<=U_i<=1` and `max_i U_i(x)=1` at every source point. Let

\[
K:X\rightsquigarrow Y
\]

be a stochastic compression, put `Q_i=P_iK`, `q=MK`, and write

\[
V_i(y):=\mathbb E_M[U_i(X)\mid Y=y].
\tag{3}
\]

As in AF-154,

\[
\|V(y)\|_\infty
=\frac{\max_iQ_i(y)}{C_Xq(y)}
=\frac1{\kappa(y)}.
\tag{4}
\]

Now give the decision maker the finite action set `{1,...,m}` and the **envelope loss**

\[
\boxed{
\ell(i,x):=1-U_i(x).
}
\tag{5}
\]

With the source point `X` itself observed, the optimal loss is identically zero: choose any experiment member attaining the pointwise envelope. With only the compressed observation `Y=y`, the conditional Bayes risk is

\[
\begin{aligned}
r_{\rm env}(y)
&:=\min_i\mathbb E_M[\ell(i,X)\mid Y=y]\\
&=1-\max_iV_i(y)\\
&=1-\|V(y)\|_\infty\\
&=1-\frac1{\kappa(y)}.
\end{aligned}
\tag{6}
\]

Therefore the global Bayes-risk penalty is exactly

\[
\boxed{
R_{\rm env}(K;\mathcal E)
:=\mathbb E_q r_{\rm env}(Y)
=1-\frac{C_Y}{C_X},
}
\tag{7}
\]

where

\[
C_Y:=\sum_y\max_iQ_i(y).
\]

Equivalently, if

\[
\Delta_\infty
:=\log\frac{C_X}{C_Y}
\tag{8}
\]

is the maximal-leakage drop from AF-150, then

\[
\boxed{
R_{\rm env}=1-e^{-\Delta_\infty}.
}
\tag{9}
\]

Thus Shtarkov-mass contraction is not merely a scalar complexity change: after the source Shtarkov normalization it is exactly the loss of performance for **one declared finite decision problem**. This interpretation is classical gain-based decision theory / quantitative information flow specialized to the source-induced gain `g(i,x)=U_i(x)`; no novelty is claimed for that general framework.

The zero set is correspondingly weaker than experiment sufficiency. For every output with `q(y)>0`,

\[
\boxed{
r_{\rm env}(y)=0
\iff
\exists i_y\text{ such that }U_{i_y}(X)=1
\quad M(\cdot\mid Y=y)\text{-a.s.}
}
\tag{10}
\]

In finite support language, all source points feeding that output share at least one common pointwise-envelope winner. Hence

\[
\boxed{
R_{\rm env}=0
\iff
\kappa(Y)=1\quad q\text{-a.s.}
\iff
C_Y=C_X.
}
\tag{11}
\]

By contrast, AF-154's full Shtarkov Pearson loss

\[
\mathcal L_*(K;\mathcal E)
=C_X^2\,
\mathbb E_q\|U(X)-V(Y)\|_2^2
\tag{12}
\]

vanishes exactly when the whole experiment is sufficient. In decision language, the normalized quantity

\[
R_{\rm ray}(K;\mathcal E)
:=\frac{\mathcal L_*}{C_X^2}
\tag{13}
\]

is the minimum squared-error Bayes risk for reconstructing the **entire likelihood ray** `U` from `Y`, because `V=E[U|Y]` is the Bayes estimator. Consequently

\[
\boxed{
R_{\rm env}=0
\not\Rightarrow
R_{\rm ray}=0,
}
\tag{14}
\]

and the distinction in AF-154 is exactly a distinction between decision classes: preserving the best envelope action is weaker than preserving the full minimal-sufficient likelihood ray.

The two risks obey the universal bound

\[
\boxed{
R_{\rm env}
\le
\sqrt{R_{\rm ray}}
=\frac{\sqrt{\mathcal L_*}}{C_X}.
}
\tag{15}
\]

This follows because the distance from `V(y)` to the positive `ell_infinity` unit boundary is `r_env(y)`, while every conditional value `U(X)` lies on that boundary. AF-154 gives the corresponding conditional squared-distance lower bound; averaging and Jensen yield `(15)`.

Finally, when the pointwise envelope winner is unique with a uniform normalized margin, radial loss becomes quantitatively equivalent to recovering that winner label. Let

\[
A(x):=\operatorname*{argmax}_iU_i(x)
\]

be unique and assume

\[
\boxed{
\gamma
:=\inf_x\left[
1-\max_{j\ne A(x)}U_j(x)
\right]>0.
}
\tag{16}
\]

Let

\[
e_A(Y)
:=\mathbb E_q\left[
1-\max_i\mathbb P_M(A(X)=i\mid Y)
\right]
\tag{17}
\]

be the Bayes classification error for the winner label. Then

\[
\boxed{
\gamma e_A(Y)
\le
R_{\rm env}(K;\mathcal E)
\le
e_A(Y).
}
\tag{18}
\]

The margin hypothesis is essential. Without it, the winning label can be badly scrambled while the radial Shtarkov loss tends to zero, because near-tied likelihood rays can cross the envelope face under an arbitrarily small perturbation.

The resulting hierarchy is precise:

\[
\text{winner-label recovery with margin}
\quad\leftrightarrow_{\gamma}\quad
\text{radial / Shtarkov-mass fidelity}
\quad\ll\quad
\text{full likelihood-ray fidelity}
\quad\leftrightarrow\quad
\text{experiment sufficiency}.
\tag{19}
\]

This gives a decision-relative interpretation of the current Arithmetic Fidelity frontier. A scalar leakage or canonical-center budget is useful only after identifying the decision class it controls. If the downstream theorem depends on non-maximal likelihood coordinates, provenance, or another tangential direction, zero radial loss is not a preservation theorem for that target.

## Derivation

### Envelope loss turns radial retreat into Bayes risk

Under `M`, the conditional expected loss of action `i` is

\[
\begin{aligned}
\mathbb E_M[\ell(i,X)\mid Y=y]
&=\mathbb E_M[1-U_i(X)\mid Y=y]\\
&=1-V_i(y).
\end{aligned}
\tag{20}
\]

Minimizing over `i` gives

\[
r_{\rm env}(y)
=1-\max_iV_i(y)
=1-\|V(y)\|_\infty,
\]

which is `(6)`. AF-154 gives

\[
\frac{C_Y}{C_X}
=\mathbb E_q\|V(Y)\|_\infty.
\tag{21}
\]

Therefore

\[
\begin{aligned}
R_{\rm env}
&=\mathbb E_q[1-\|V(Y)\|_\infty]\\
&=1-\frac{C_Y}{C_X},
\end{aligned}
\]

proving `(7)`. Equation `(9)` follows immediately from `(8)`.

This is also the exact gain-based information-flow form. With secret/source state `X`, prior `M`, action set `{1,...,m}`, and gain

\[
g(i,x):=U_i(x),
\tag{22}
\]

the vulnerability with full observation of `X` is one, while the posterior vulnerability after observing `Y` is

\[
\mathbb E_q\max_i\mathbb E_M[g(i,X)\mid Y]
=\frac{C_Y}{C_X}.
\tag{23}
\]

Thus `(7)` is the corresponding additive vulnerability loss. The Shtarkov construction selects the prior and gain from the statistical experiment itself rather than introducing them independently.

### Zero radial risk means a common winner, not a constant likelihood ray

Fix `y` with `q(y)>0`. Since `0<=U_i<=1`,

\[
V_i(y)=\mathbb E_M[U_i(X)\mid Y=y]=1
\]

holds if and only if

\[
U_i(X)=1
\quad M(\cdot\mid Y=y)\text{-a.s.}
\tag{24}
\]

Therefore `max_i V_i(y)=1` exactly when at least one index wins the pointwise envelope throughout the posterior support of that output. This proves `(10)`.

The requirement is much weaker than constancy of `U`. The winning coordinate may remain identically one while every non-maximal coordinate varies across the fiber. Those variations are invisible to `(5)` but contribute positive conditional variance to `(12)`. This recovers AF-154's tangential-loss mechanism in decision-theoretic terms.

### Full likelihood-ray loss is the squared-error Bayes risk

For any `Y`-measurable estimator `g(Y) in R^m`, the conditional-expectation Pythagorean identity from AF-009 gives

\[
\mathbb E_M\|U-g(Y)\|_2^2
=
\mathbb E_M\|U-V(Y)\|_2^2
+
\mathbb E_q\|V(Y)-g(Y)\|_2^2.
\tag{25}
\]

Hence

\[
\inf_g\mathbb E_M\|U-g(Y)\|_2^2
=
R_{\rm ray}.
\tag{26}
\]

At each `y`, every conditional source ray lies on

\[
B:=\{u\in[0,1]^m:\|u\|_\infty=1\}.
\]

The Euclidean distance from `V(y)` to `B` is

\[
1-\|V(y)\|_\infty=r_{\rm env}(y).
\]

Therefore

\[
\mathbb E_M[\|U-V(y)\|_2^2\mid Y=y]
\ge r_{\rm env}(y)^2.
\tag{27}
\]

Average `(27)` and use Jensen:

\[
R_{\rm ray}
\ge\mathbb E_q r_{\rm env}(Y)^2
\ge R_{\rm env}^2,
\]

which proves `(15)`.

### A winner margin calibrates radial loss to classification error

Assume `(16)`. For any action `i` and source point `x`, if `A(x)=i` then `U_i(x)=1` and

\[
1-U_i(x)=0.
\]

If `A(x)\ne i`, uniqueness and the margin give

\[
\gamma\le1-U_i(x)\le1.
\]

Thus pointwise

\[
\gamma\,\mathbf 1_{\{A\ne i\}}
\le
1-U_i
\le
\mathbf 1_{\{A\ne i\}}.
\tag{28}
\]

Condition on `Y=y` and minimize over `i`:

\[
\gamma\left(1-\max_i\mathbb P(A=i\mid y)\right)
\le r_{\rm env}(y)
\le
1-\max_i\mathbb P(A=i\mid y).
\tag{29}
\]

Averaging proves `(18)`.

## Matched control: near ties destroy winner-label stability

The margin in `(18)` cannot be removed. For `0<epsilon<1`, take a two-member experiment on `X={a,b}` with

\[
P_1=\left(\frac1{2-\varepsilon},
          \frac{1-\varepsilon}{2-\varepsilon}\right),
\qquad
P_2=\left(\frac{1-\varepsilon}{2-\varepsilon},
          \frac1{2-\varepsilon}\right).
\tag{30}
\]

Then

\[
C_X=\frac2{2-\varepsilon},
\qquad
M=(1/2,1/2),
\]

and

\[
U(a)=(1,1-\varepsilon),
\qquad
U(b)=(1-\varepsilon,1).
\tag{31}
\]

Let `K` collapse `a,b` to one output. The winner label is balanced, so

\[
e_A=\frac12.
\tag{32}
\]

But

\[
V=(1-\varepsilon/2,1-\varepsilon/2),
\]

hence

\[
\boxed{
R_{\rm env}=\frac\varepsilon2\longrightarrow0
\quad\text{while}\quad
e_A=\frac12.
}
\tag{33}
\]

The normalized winner margin is exactly `gamma=epsilon`, and `(18)` is sharp on the lower side:

\[
R_{\rm env}=\gamma e_A.
\]

So a discrete "which model wins?" mark is not itself a robust retained discriminator near likelihood ties. The radial Shtarkov quantity correctly regards those flips as cheap when the rays lie arbitrarily close to the tie face.

## Exact arithmetic stress test: one Euler-factor truncation

AF-154 already supplies a concrete prime-power instance of tangential likelihood-ray loss. For the local `p=2` Euler-factor weights truncated to exponents `k=1,2,3`, compare

\[
P_1=\left(\frac47,\frac27,\frac17\right),
\qquad
P_2=\left(\frac{16}{21},\frac4{21},\frac1{21}\right),
\tag{34}
\]

corresponding to the normalized profiles at `sigma=1` and `sigma=2`. Their envelope and Shtarkov center are

\[
s=\left(\frac{16}{21},\frac6{21},\frac3{21}\right),
\qquad
C_X=\frac{25}{21},
\qquad
M=\left(\frac{16}{25},\frac6{25},\frac3{25}\right).
\tag{35}
\]

The likelihood rays are

\[
U(1)=\left(\frac34,1\right),
\qquad
U(2)=\left(1,\frac23\right),
\qquad
U(3)=\left(1,\frac13\right).
\tag{36}
\]

Let the compression retain `k=1` and merge `k=2,3` into one higher-power output. On the merged output the first experiment member is a common envelope winner because its first likelihood-ray coordinate is identically one across `k=2,3`. Consequently

\[
\kappa=1
\]

on both outputs and

\[
\boxed{
C_Y=C_X,
\qquad
R_{\rm env}=0.
}
\tag{37}
\]

Nevertheless the second likelihood coordinate varies from `2/3` to `1/3` inside the merged cell. Conditional on that output, the Shtarkov probabilities of `k=2,3` are `2/3,1/3`, so

\[
V_{\{2,3\}}
=\left(1,\frac59\right)
\]

and

\[
\operatorname{Var}(U_2\mid\{2,3\})
=\frac2{81}.
\tag{38}
\]

Since the merged output has `q`-mass `9/25`,

\[
R_{\rm ray}
=\frac{9}{25}\frac2{81}
=\frac2{225}>0,
\tag{39}
\]

and therefore

\[
\boxed{
\mathcal L_*
=C_X^2R_{\rm ray}
=\frac{50}{3969}>0.
}
\tag{40}
\]

This is the desired arithmetic separation in the new language: the compression preserves the Shtarkov envelope decision perfectly while destroying a non-maximal prime-power likelihood ratio. A downstream theorem that needs the full local profile cannot use zero maximal-leakage drop as a fidelity certificate.

## Prior art and novelty assessment

The decision-theoretic ingredients are classical and should not be relabeled as a new theory.

- David Blackwell, **“Equivalent Comparisons of Experiments,”** *The Annals of Mathematical Statistics* 24(2), 265–272 (1953), DOI `10.1214/aoms/1177729032`. Blackwell comparison makes the central distinction used here: preservation for one decision problem is weaker than preservation of an experiment for the unrestricted decision class.
- Yuri M. Shtarkov, **“Universal Sequential Coding of Single Messages,”** *Problems of Information Transmission* 23(3), 175–186 (1987). The pointwise likelihood envelope, Shtarkov sum, and normalized maximum-likelihood law are classical minimax-regret objects.
- Ibrahim Issa, Aaron B. Wagner, and Sudeep Kamath, **“An Operational Approach to Information Leakage,”** *IEEE Transactions on Information Theory* 66(3), 1625–1657 (2020), DOI `10.1109/TIT.2019.2962804`, arXiv:`1807.07878`. They identify maximal leakage with Sibson mutual information of order infinity, derive the discrete `log sum_y max_x W(y|x)` formula, establish data processing, and explicitly connect the quantity to the Shtarkov sum.
- Mário S. Alvim, Konstantinos Chatzikokolakis, Annabelle McIver, Carroll Morgan, Catuscia Palamidessi, and Geoffrey Smith, **“An Axiomatization of Information Flow Measures,”** *Theoretical Computer Science* 777, 32–54 (2019), DOI `10.1016/j.tcs.2018.10.016`. Gain-based vulnerability formalizes exactly the general pattern of optimizing a declared action/gain function before and after observation; `(22)--(23)` are a source-induced specialization of that established framework.

Accordingly, `(6)--(9)` are best classified as an exact specialization/identification, not as a new decision-theory theorem. The useful Arithmetic Fidelity content is the resulting **boundary between decision classes**. AF-150's maximal-leakage scalar, AF-151's local conflict, and AF-154's full ray loss are no longer merely related diagnostics: the first two control one canonical envelope-choice task, while the full Pearson profile controls squared reconstruction of the minimal-sufficient ray. The near-tie and Euler-factor controls show exactly why those zero sets differ.

## Boundaries and falsification checks

- The loss `(5)` is induced by the chosen Shtarkov normalization. It is canonical for the finite experiment but it is still only one decision problem; preserving it is not Blackwell sufficiency.
- Ties are allowed in `(6)--(11)`. The winner-label comparison `(18)` requires a unique winner and a strictly positive normalized margin. Without that gate, a chosen tie-breaking label is not stable or canonical.
- `R_env` is an average under the Shtarkov reference. Rare outputs can have large local conflict while contributing little to the mean; AF-151's stronger moment/tail audits remain necessary when the downstream topology demands them.
- `R_ray` uses Euclidean squared loss on the likelihood-ray coordinates. Its zero set is coordinate-stable because it is exact sufficiency, but its numerical scale is not invariant under arbitrary nonlinear reparameterizations of the ray.
- The arithmetic example proves only a local prime-power information-loss mechanism. It does not establish an RH consequence, a global Euler-product theorem, or a privileged probability interpretation of the Riemann explicit formula.
- The gain-based/QIF interpretation prevents a novelty claim for the abstract Bayes-risk construction. Its role is to identify exactly which source-induced decision task the Shtarkov scalar can and cannot certify.

## Consequence for the line

When a future compression is summarized by a scalar monotone quantity, the first question should be **which decision class has that scalar as its exact Bayes-risk defect?** For the Shtarkov mass the answer is now explicit: it controls only the envelope-choice gain on the normalized likelihood ray.

A downstream route that needs only a robust envelope winner may legitimately use radial conflict, preferably with a margin or tail condition appropriate to its topology. A route that needs non-maximal likelihood ratios, signed provenance, or another tangential component must instead control a richer witness family such as the full likelihood ray. This turns the current radial-versus-tangential distinction into a reusable stopping rule: do not promote a scalar data-processing equality to structural fidelity until the target theorem has been shown to factor through the corresponding decision class.