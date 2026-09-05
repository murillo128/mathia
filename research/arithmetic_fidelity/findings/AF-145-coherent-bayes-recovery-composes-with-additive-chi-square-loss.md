# AF-145 — Coherent Bayes recovery composes with additive chi-square loss

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-BAYES-COMPOSITION`, `EXACT-CHAIN-DECOMPOSITION`, `QUANTITATIVE-FIDELITY`, `NO-NOVELTY-CLAIM`

## Claim

AF-133--AF-134 show that generic stagewise recovery is not automatically compositional: an inverse may resurrect information declared invisible by the next-stage quotient, and the minimal witness repair can be as large as the discarded structure. AF-144 identifies a special whole-experiment recovery certificate in the finite statistical category: common-reference Pearson chi-square loss controls one Bayes/Petz reverse kernel.

For this special recovery the composition obstruction disappears **provided the reference is propagated coherently through the entire chain**. The stagewise Bayes reverses compose exactly to the Bayes reverse of the composite channel, while the corresponding chi-square losses telescope exactly. Thus there is no additional recovery penalty caused merely by staging the compression.

Let

\[
X_0\xrightarrow{K_1}X_1\xrightarrow{K_2}\cdots\xrightarrow{K_n}X_n
\tag{1}
\]

be finite stochastic channels, and let

\[
\mathcal E_0=(P_{\theta,0})_{\theta\in\Theta}
\]

be a finite experiment on `X_0`. Choose one full-support prior

\[
\lambda\in\Delta^\circ(\Theta)
\]

and define recursively

\[
P_{\theta,j}=P_{\theta,j-1}K_j,
\qquad
M_j=\sum_\theta\lambda_\theta P_{\theta,j}=M_{j-1}K_j.
\tag{2}
\]

Restrict each `X_j` to the support of `M_j`. Define the stage-`j` Bayes reverse

\[
R_j(x_{j-1}\mid x_j)
:=
\frac{M_{j-1}(x_{j-1})K_j(x_j\mid x_{j-1})}{M_j(x_j)}.
\tag{3}
\]

For each parameter and stage define the Pearson chi-square loss

\[
\varepsilon_{\theta,j}(\lambda)
:=
\chi^2(P_{\theta,j-1}\|M_{j-1})
-
\chi^2(P_{\theta,j}\|M_j)
\ge0.
\tag{4}
\]

Then:

1. if
   \[
   K_{1:n}:=K_1K_2\cdots K_n,
   \]
   the Bayes reverse of `K_{1:n}` at the common reference `M_0` is exactly
   \[
   \boxed{
   R_{1:n}=R_nR_{n-1}\cdots R_1;
   }
   \tag{5}
   \]
2. the common-reference chi-square loss of the composite is exactly additive:
   \[
   \boxed{
   \chi^2(P_{\theta,0}\|M_0)
   -
   \chi^2(P_{\theta,n}\|M_n)
   =
   \sum_{j=1}^n\varepsilon_{\theta,j}(\lambda);
   }
   \tag{6}
   \]
3. applying AF-144 once to the composite channel therefore gives the **single-kernel chain recovery bound**
   \[
   \boxed{
   4\,
   \left\|
   P_{\theta,0}
   -P_{\theta,n}R_n\cdots R_1
   \right\|_{\rm TV}^2
   \le
   \sum_{j=1}^n\varepsilon_{\theta,j}(\lambda)
   }
   \tag{7}
   \]
   simultaneously for every `theta`;
4. consequently the whole-experiment recovery deficiency obeys
   \[
   \boxed{
   \delta_{\rm rec}(K_{1:n};\mathcal E_0)
   \le
   \frac12
   \sqrt{
   \max_\theta
   \sum_{j=1}^n\varepsilon_{\theta,j}(\lambda)
   };
   }
   \tag{8}
   \]
5. defining the coherent path profile
   \[
   \Gamma_{\rm path}(K_{1:n};\mathcal E_0)
   :=
   \inf_{\lambda\in\Delta^\circ(\Theta)}
   \max_\theta
   \sum_{j=1}^n\varepsilon_{\theta,j}(\lambda),
   \tag{9}
   \]
   one has exactly
   \[
   \boxed{
   \Gamma_{\rm path}(K_{1:n};\mathcal E_0)
   =
   \Gamma_{\chi^2}(K_{1:n};\mathcal E_0),
   }
   \tag{10}
   \]
   where `Gamma_chi2` is the endpoint profile from AF-144. Hence
   \[
   4\delta_{\rm rec}(K_{1:n};\mathcal E_0)^2
   \le
   \Gamma_{\rm path}(K_{1:n};\mathcal E_0).
   \tag{11}
   \]

The important point is not a new scalar inequality at the endpoint: `(10)` says the path profile is exactly the already-known endpoint chi-square certificate. The new organizational information is the **canonical stage attribution** `(4)--(6)` together with the fact that the corresponding reverse channel also factors stage by stage. A coherent reference therefore supplies both sides of a compositional fidelity certificate: additive loss accounting forward and an exactly compatible inverse backward.

## Derivation

### Bayes reverses compose when the prior is propagated

It is enough to prove the two-stage statement. Let

\[
X\xrightarrow{K}Y\xrightarrow{L}Z,
\]

let `M` be the reference law on `X`, and put

\[
N=MK,
\qquad
O=NL.
\]

The two Bayes reverses are

\[
R_K(x\mid y)=\frac{M(x)K(y\mid x)}{N(y)},
\qquad
R_L(y\mid z)=\frac{N(y)L(z\mid y)}{O(z)}.
\tag{12}
\]

Their composite is

\[
\begin{aligned}
(R_LR_K)(x\mid z)
&=
\sum_y
\frac{N(y)L(z\mid y)}{O(z)}
\frac{M(x)K(y\mid x)}{N(y)}\\
&=
\frac{M(x)}{O(z)}
\sum_y K(y\mid x)L(z\mid y)\\
&=
\frac{M(x)(KL)(z\mid x)}{O(z)}.
\end{aligned}
\tag{13}
\]

The last expression is exactly the Bayes reverse of the composite channel `KL` at reference `M`. Induction proves `(5)`.

The dependence on the propagated reference is load-bearing. The inverse of the second stage is taken at `M_1=M_0K_1`, not at an independently selected law on `X_1`. This is the finite stochastic version of the standard compositional Bayes rule.

### Chi-square loss telescopes along the same reference chain

Equation `(6)` follows algebraically from `(4)`:

\[
\begin{aligned}
\sum_{j=1}^n\varepsilon_{\theta,j}(\lambda)
&=
\sum_{j=1}^n
\left[
\chi^2(P_{\theta,j-1}\|M_{j-1})
-
\chi^2(P_{\theta,j}\|M_j)
\right]\\
&=
\chi^2(P_{\theta,0}\|M_0)
-
\chi^2(P_{\theta,n}\|M_n).
\end{aligned}
\tag{14}
\]

There is also an exact conditional-expectation interpretation of every term. Under the reference joint law

\[
M_0(x_0)
K_1(x_1\mid x_0)\cdots K_n(x_n\mid x_{n-1}),
\tag{15}
\]

define

\[
h_{\theta,j}(x_j)
:=
\frac{P_{\theta,j}(x_j)}{M_j(x_j)}-1.
\tag{16}
\]

Bayes' rule gives

\[
h_{\theta,j}(X_j)
=
\mathbb E[
 h_{\theta,j-1}(X_{j-1})
 \mid X_j
].
\tag{17}
\]

Therefore

\[
\boxed{
\varepsilon_{\theta,j}(\lambda)
=
\mathbb E
\left[
\left(
 h_{\theta,j-1}(X_{j-1})
 -h_{\theta,j}(X_j)
\right)^2
\right].
}
\tag{18}
\]

Indeed the conditional-expectation orthogonality identity turns the right-hand side into

\[
\|h_{\theta,j-1}\|_{L^2(M_{j-1})}^2
-
\|h_{\theta,j}\|_{L^2(M_j)}^2,
\]

which is exactly `(4)`. Thus each stage loss is a genuine nonnegative `L^2` projection defect, not an arbitrary allocation of the endpoint discrepancy.

For `j<k`, the stage-`j` residual in `(18)` has conditional mean zero given `X_j`'s output `X_j`, and all later variables are downstream of that state. The usual Markov/conditional-expectation orthogonality therefore makes distinct stage innovations orthogonal in the reference path space. Equation `(6)` is consequently also a Pythagorean decomposition of the total common-reference likelihood-ratio loss into stage innovations.

### One composite recovery bound is stronger than chaining stagewise TV bounds

AF-144 applied independently at each stage would give

\[
2\,
\|P_{\theta,j-1}-P_{\theta,j}R_j\|_{\rm TV}
\le
\sqrt{\varepsilon_{\theta,j}}.
\tag{19}
\]

A naive triangle-inequality propagation would then pay a sum of square roots and would additionally need to control how intermediate recovery kernels transport earlier errors. That is exactly the kind of regularity burden exposed abstractly by AF-131--AF-133.

Here it is unnecessary. Equation `(5)` identifies the stagewise inverse product with the **single Bayes inverse of the composite channel**, so AF-144 can be applied once at the endpoint. Together with `(6)` this yields `(7)` directly with the square root of the total additive chi-square defect rather than a stagewise accumulation of separate reconstruction errors.

This does not contradict AF-133. The present chain is a special coherent family of inverses generated by one reference law and the actual forward channels. Generic recovery kernels do not possess this functorial structure.

## Prior art and novelty assessment

No theorem-level novelty is claimed.

- Dylan Braithwaite, Jules Hedges, and Toby St Clere Smithe, **“The Compositional Structure of Bayesian Inference,”** in *48th International Symposium on Mathematical Foundations of Computer Science (MFCS 2023)*, LIPIcs 272, Article 24, 24:1--24:15 (2023), DOI `10.4230/LIPIcs.MFCS.2023.24`, arXiv:`2305.06112`. They explicitly formulate Bayesian inversion of a composite kernel as composition of the component Bayesian inverses with the intermediate prior propagated by the preceding forward kernel, and develop the construction functorially in Markov categories. This is direct stronger prior art for `(5)`.
- Li Gao, Haojian Li, Iman Marvian, and Cambyse Rouzé, **“Sufficient Statistic and Recoverability via Quantum Fisher Information,”** *Communications in Mathematical Physics* 405, article 180 (2024), DOI `10.1007/s00220-024-05053-z`, arXiv:`2302.02341`. AF-144 specializes their chi-square/Petz recoverability mechanism to the finite classical common-mixture setting used here.
- Classical conditional-expectation projection theory supplies `(17)--(18)`, and the telescoping identity `(6)` is elementary once the same reference is propagated. These pieces should not be cited as a new martingale or information-decomposition theorem.

The Arithmetic Fidelity contribution is the synthesis relevant to its live composition obstruction: **the common-reference certificate from AF-144 is not merely family-wide at one stage; it is coherently compositional across an entire finite Markov pipeline.** The source of this favorable behavior is exact and auditable: one propagated reference simultaneously determines the forward chi-square defect decomposition and the backward Bayes/Petz chain.

## Boundary conditions and falsification tests

1. **One coherent prior is required.** Every `M_j` must be the forward image of the same initial mixture `M_0`. Picking an independently optimized reference at each stage can produce different reverse kernels that do not compose to the Bayes inverse of the whole chain.

2. **Do not infer false subadditivity after independent optimization.** For fixed `lambda`,
   \[
   \max_\theta\sum_j\varepsilon_{\theta,j}(\lambda)
   \le
   \sum_j\max_\theta\varepsilon_{\theta,j}(\lambda).
   \]
   But taking a separate infimum over `lambda` in each summand does not justify
   \[
   \Gamma_{\rm path}
   \le
   \sum_j\Gamma_j.
   \]
   The stagewise minimizers may be incompatible. Any scalar stage budget must retain the common reference or another compatibility certificate.

3. **Different parameters may lose information at different stages.** The worst `theta` of the total sum need not be the worst `theta` at every individual stage. Replacing `max_theta sum_j` by a sum of stagewise maxima is a valid upper bound but can be substantially loose.

4. **The decomposition localizes loss but does not identify an arithmetic discriminator.** A small stage loss only says that the declared finite experiment is nearly recoverable relative to the chosen common mixture. An RH application still has to justify the experiment/control family and prove that it contains the rational-prime-specific distinction that matters.

5. **The prior remains auxiliary unless independently canonical.** Optimizing `(9)` removes the arbitrary prior from the endpoint scalar, but the minimizing prior need not have an intrinsic arithmetic meaning. If a concrete pipeline claims that its stage attribution is canonical, the source mathematics must select the reference or prove reference-robust conclusions.

6. **Support and category matter.** Equations `(3)` and `(13)` are stated after restricting to the supports of the propagated reference laws. The finite classical proof does not automatically extend to arbitrary measurable kernels, singular measures, noncommutative channels, or unbounded operator settings without their own domain/support theory.

7. **This does not make arbitrary approximate inverses compositional.** The favorable rule is specific to Bayes/Petz reverses tied to the actual forward channel and one propagated reference. AF-133--AF-134 remain the relevant gate for independently proposed recoveries and restricted witness categories.

8. **The path profile is not a new endpoint invariant.** By `(10)` it is exactly AF-144's composite common-reference chi-square profile. Its value is the exact stage decomposition and compatible reverse factorization, not a claim of discovering another numerical measure of information.

## Consequence for the current frontier

AF-143 showed that local Fisher geometry and pairwise distinguishability do not assemble themselves into one reverse experiment. AF-144 supplied a common-reference finite-displacement profile that does. AF-145 now shows the next structural fact: **that common reverse experiment can be transported through a chain without inventing a new compatibility layer at every stage.**

This sharpens the future arithmetic test. For a proposed compression pipeline, it is not enough to show that each stage separately retains some preferred statistic. A positive route should seek a source-natural reference/control geometry whose finite-displacement losses remain small under the actual forward maps and whose induced reverse maps are coherently compositional. If no such common geometry exists, the generic AF-133/AF-134 witness-saturation obstruction returns.