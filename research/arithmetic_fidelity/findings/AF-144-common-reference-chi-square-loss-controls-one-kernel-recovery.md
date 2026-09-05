# AF-144 — Common-reference chi-square loss controls one-kernel experiment recovery

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-COMMUTATIVE-SPECIALIZATION`, `QUANTITATIVE-FIDELITY`, `RECOVERY-UPPER-BOUND`, `NO-NOVELTY-CLAIM`

## Claim

AF-126 identifies one-sided Le Cam recovery deficiency as the finite whole-experiment notion of approximate fidelity. AF-143 then shows why local Fisher near-isometry, global injectivity, and even uniform pairwise total-variation separation still do not certify small deficiency: those conditions need not produce one reverse channel that works for the whole family.

In the finite statistical category there is, however, a direct positive certificate of exactly that missing type. A family of Pearson chi-square data-processing losses measured against **one common reference mixture** controls the error of **one common Bayes/Petz reverse channel**.

Let

\[
\mathcal E=(P_\theta)_{\theta\in\Theta}
\]

be a finite statistical experiment on a finite sample space `X`, let

\[
K:X\rightsquigarrow Y
\]

be a stochastic compression, and write

\[
Q_\theta=P_\theta K.
\]

Choose any full-support prior

\[
\lambda\in\Delta^\circ(\Theta),
\qquad \lambda_\theta>0,
\]

and define the common source and output mixtures

\[
M_\lambda=\sum_\theta\lambda_\theta P_\theta,
\qquad
N_\lambda=M_\lambda K
=\sum_\theta\lambda_\theta Q_\theta.
\tag{1}
\]

Restrict `X` and `Y` to the supports of `M_lambda` and `N_lambda`; this loses no member of the experiment because `lambda_theta>0` makes `M_lambda` dominate every `P_theta`.

For distributions `P << M`, use the Pearson divergence

\[
\chi^2(P\|M)
:=
\sum_x M(x)
\left(\frac{P(x)}{M(x)}-1\right)^2.
\tag{2}
\]

Define the common-reference chi-square loss of member `theta` by

\[
\varepsilon_\theta(\lambda)
:=
\chi^2(P_\theta\|M_\lambda)
-
\chi^2(Q_\theta\|N_\lambda)
\ge0.
\tag{3}
\]

The Bayes reverse channel associated with the same reference mixture is

\[
R_\lambda(x\mid y)
:=
\frac{M_\lambda(x)K(y\mid x)}{N_\lambda(y)}
\qquad(N_\lambda(y)>0).
\tag{4}
\]

Then:

1. `R_lambda` exactly recovers the reference mixture,
   \[
   N_\lambda R_\lambda=M_\lambda;
   \tag{5}
   \]
2. the **same** reverse channel satisfies, simultaneously for every `theta`,
   \[
   \boxed{
   4\,
   \|P_\theta-Q_\theta R_\lambda\|_{\rm TV}^{2}
   \le
   \varepsilon_\theta(\lambda);
   }
   \tag{6}
   \]
3. therefore the whole-experiment recovery deficiency from AF-126 obeys
   \[
   \boxed{
   \delta_{\rm rec}(K;\mathcal E)
   \le
   \frac12
   \sqrt{\max_{\theta}\varepsilon_\theta(\lambda)}.
   }
   \tag{7}
   \]
4. optimizing away the arbitrary prior by
   \[
   \Gamma_{\chi^2}(K;\mathcal E)
   :=
   \inf_{\lambda\in\Delta^\circ(\Theta)}
   \max_\theta\varepsilon_\theta(\lambda)
   \tag{8}
   \]
   gives the reference-optimized certificate
   \[
   \boxed{
   4\,\delta_{\rm rec}(K;\mathcal E)^2
   \le
   \Gamma_{\chi^2}(K;\mathcal E).
   }
   \tag{9}
   \]
5. the zero boundary is exact:
   \[
   \boxed{
   \Gamma_{\chi^2}(K;\mathcal E)=0
   \iff
   \delta_{\rm rec}(K;\mathcal E)=0
   \iff
   K\text{ is sufficient for the finite experiment.}
   }
   \tag{10}
   \]
   More strongly, if one full-support `lambda` has `varepsilon_theta(lambda)=0` for every `theta`, then its single Bayes reverse `R_lambda` already recovers every experiment member exactly.

Thus the positive target left by AF-143 exists in the finite statistical category: **simultaneous finite-displacement chi-square retention relative to one common reference gives a deficiency-dominating profile and an explicit common reconstruction kernel.** This is categorically stronger than checking tangent Fisher geometry or unrelated pairwise distances.

The underlying recoverability inequality is established prior art. In Gao--Li--Marvian--Rouzé, Theorem 1.5 gives a quantum chi-square data-processing-loss bound by squared trace-norm error of the Petz recovery map; the authors state explicitly that it reduces to the classical chi-square result in the commutative setting. Equations `(6)`--`(9)` are the finite classical/common-mixture packaging of that theorem, with the elementary Hilbert-space proof included below. No theorem-level novelty is claimed.

## Derivation

### The common Bayes reverse is the classical Petz map

Fix `lambda` and abbreviate

\[
M=M_\lambda,
\qquad
N=N_\lambda.
\]

Under the joint reference law

\[
J(x,y)=M(x)K(y\mid x),
\tag{11}
\]

the kernel `(4)` is exactly the conditional law of `X` given `Y`. Hence

\[
(NR_\lambda)(x)
=
\sum_y N(y)
\frac{M(x)K(y\mid x)}{N(y)}
=M(x),
\]

which proves `(5)`. The important family-level point is that `R_lambda` depends only on the declared experiment through the single mixture `M` and on the channel `K`; it does **not** depend on `theta`.

### Compression and reverse recovery form an `L^2` contraction

Let

\[
A:L^2(N)\to L^2(M)
\]

be the Markov operator

\[
(Af)(x)=\sum_y K(y\mid x)f(y).
\tag{12}
\]

Its Hilbert adjoint is conditional expectation under `(11)`:

\[
(A^*h)(y)
=
\sum_x R_\lambda(x\mid y)h(x)
=
\mathbb E_M[h(X)\mid Y=y].
\tag{13}
\]

Both are contractions. Therefore

\[
B:=AA^*:L^2(M)\to L^2(M)
\tag{14}
\]

is self-adjoint, positive, and satisfies

\[
0\preceq B\preceq I,
\qquad
B\mathbf 1=\mathbf 1.
\tag{15}
\]

For each member define its centered likelihood ratio relative to the common mixture,

\[
h_\theta(x)
:=
\frac{P_\theta(x)}{M(x)}-1.
\tag{16}
\]

The output likelihood-ratio residual is exactly

\[
A^*h_\theta(y)
=
\frac{Q_\theta(y)}{N(y)}-1.
\tag{17}
\]

Consequently the chi-square data-processing loss is

\[
\begin{aligned}
\varepsilon_\theta(\lambda)
&=\|h_\theta\|_{L^2(M)}^2
-\|A^*h_\theta\|_{L^2(N)}^2\\
&=\langle h_\theta,(I-B)h_\theta\rangle_{L^2(M)}.
\end{aligned}
\tag{18}
\]

This is the finite-displacement analogue of the conditional-score projection defect in AF-141, but now the displacement is the complete likelihood ratio from one common reference rather than only a tangent score at one parameter value.

### The same defect bounds the actual recovered distribution

The density of the recovered distribution `Q_theta R_lambda` relative to `M` is

\[
1+Bh_\theta.
\tag{19}
\]

Therefore the source-versus-recovered density difference is

\[
h_\theta-Bh_\theta
=(I-B)h_\theta.
\tag{20}
\]

Since `0 <= B <= I`, functional calculus gives

\[
(I-B)^2\preceq I-B.
\tag{21}
\]

Hence

\[
\begin{aligned}
\left\|h_\theta-Bh_\theta\right\|_{L^2(M)}^2
&=\langle h_\theta,(I-B)^2h_\theta\rangle\\
&\le
\langle h_\theta,(I-B)h_\theta\rangle\\
&=\varepsilon_\theta(\lambda).
\end{aligned}
\tag{22}
\]

Finally, Cauchy--Schwarz under the probability law `M` gives

\[
\begin{aligned}
2\|P_\theta-Q_\theta R_\lambda\|_{\rm TV}
&=\|h_\theta-Bh_\theta\|_{L^1(M)}\\
&\le
\|h_\theta-Bh_\theta\|_{L^2(M)}\\
&\le
\sqrt{\varepsilon_\theta(\lambda)},
\end{aligned}
\tag{23}
\]

which proves `(6)`. Taking the supremum over `theta` and then the infimum over all possible reverse channels proves `(7)`. Since `(7)` holds for every full-support `lambda`, taking the infimum over `lambda` proves `(9)`.

This is exactly the commutative mechanism behind the Petz recoverability inequality: the same conditional-expectation operator that contracts chi-square divergence determines the canonical reverse kernel, and positivity of `AA^*` converts divergence loss into reconstruction error.

### Exact zero loss is exactly finite-experiment sufficiency

Equation `(9)` immediately implies

\[
\Gamma_{\chi^2}=0
\Longrightarrow
\delta_{\rm rec}=0.
\tag{24}
\]

For the converse, suppose `delta_rec=0`. By AF-126 there exists one reverse channel `S` satisfying

\[
Q_\theta S=P_\theta
\qquad\forall\theta.
\tag{25}
\]

For every prior `lambda`, linearity gives

\[
N_\lambda S=M_\lambda.
\tag{26}
\]

Apply chi-square data processing first through `K` and then through `S`:

\[
\chi^2(P_\theta\|M_\lambda)
\ge
\chi^2(Q_\theta\|N_\lambda)
\ge
\chi^2(Q_\theta S\|N_\lambda S)
=
\chi^2(P_\theta\|M_\lambda).
\tag{27}
\]

Both inequalities are equalities, so every `varepsilon_theta(lambda)` vanishes. Thus `Gamma_chi2=0`, proving `(10)`.

This also connects directly to AF-013. Exact finite-experiment fidelity there is retention of the full vector of likelihood ratios relative to one reference. AF-144 supplies a quantitative finite-displacement relaxation: common-reference quadratic likelihood-ratio loss controls the actual error of one common reconstruction channel.

## Prior art and novelty assessment

The recovery mechanism is established mathematics; the present finding should not be cited as a new chi-square or Petz theorem.

- Li Gao, Haojian Li, Iman Marvian, and Cambyse Rouzé, **“Sufficient Statistic and Recoverability via Quantum Fisher Information,”** *Communications in Mathematical Physics* 405, article 180 (2024), DOI `10.1007/s00220-024-05053-z`, arXiv:`2302.02341`. Their Theorem 1.5 proves the universal quantum bound
  \[
  \chi_{1/2}^2(\rho,\sigma)
  -\chi_{1/2}^2(\Phi(\rho),\Phi(\sigma))
  \ge
  \|\rho-\mathcal R_{\sigma,\Phi}\Phi(\rho)\|_1^2
  \]
  for the Petz recovery map, and explicitly notes that the result applies to the classical setting because the quantum chi-square divergences reduce to classical chi-square divergence for commuting states. This is direct stronger prior art for `(6)`.
- Dénes Petz, **“Sufficient subalgebras and the relative entropy of states of a von Neumann algebra,”** *Communications in Mathematical Physics* 105(1), 123–131 (1986), and **“Sufficiency of channels over von Neumann algebras,”** *Quarterly Journal of Mathematics* 39(1), 97–108 (1988). Role: canonical recovery-map and exact-sufficiency background. In the finite commutative case the Petz map is precisely the Bayes reverse `(4)`.
- AF-012 and AF-013 already record the classical conditional-Jensen and likelihood-ratio exact-sufficiency boundary for binary and finite experiments. AF-126 supplies the whole-experiment deficiency that `(7)` bounds. AF-141--AF-143 establish why tangent Fisher retention and pairwise geometry alone are weaker than this common-reference finite-displacement condition.

The literature therefore changes the novelty classification decisively: the inequality is not a new Arithmetic Fidelity theorem. The durable contribution is the **family-level organization** needed by this line: choosing one common reference mixture makes the same classical/Petz reverse map valid for every matched control simultaneously, and the resulting profile directly upper-bounds the exact recovery defect that AF-143 left unresolved.

## Boundary conditions and falsification tests

1. **The common reference is essential.** Pairwise chi-square losses computed with unrelated reference distributions may each come with different reverse kernels and therefore do not establish whole-experiment recoverability. Equations `(6)`--`(7)` work because every member is compared to the same `M_lambda` and uses the same `R_lambda`.

2. **The prior is auxiliary structure.** Any full-support prior gives a valid certificate, and `(8)` removes it from the scalar profile by optimization. But an arithmetic application cannot claim that a particular prior or mixture is intrinsic unless the source mathematics justifies it. Optimization supplies a category-level audit quantity, not automatically a canonical arithmetic construction.

3. **Small chi-square loss is sufficient, not quantitatively necessary with the same modulus.** Equation `(9)` is one-sided. Exact zero agrees with sufficiency, but the ratio between `Gamma_chi2` and `delta_rec^2` may be large. Do not treat `(9)` as an equivalence of quantitative geometries without additional hypotheses.

4. **This is stronger than local Fisher retention.** AF-141 measures tangent score loss at a parameter value. The common-reference chi-square profile measures finite likelihood-ratio displacement from `M_lambda`. AF-142/AF-143 are therefore not contradicted: their local or pairwise gates can look good while `(3)` remains large enough to obstruct recovery.

5. **Pairwise metric preservation does not bypass the profile.** AF-126 notes an AF-012 example where a selected pairwise total-variation discrimination score is preserved while exact sufficiency fails. By `(10)`, every valid reference-optimized common chi-square profile remains strictly positive in such an example. The profile is detecting common-kernel compatibility rather than one scalar pairwise distance.

6. **The channel must be a genuine parameter-independent compression.** If the observation rule depends on `theta`, it can inject source information and the common Markov/Petz interpretation no longer represents pure downstream compression.

7. **The finite-support proof is deliberate.** Extensions to dominated infinite experiments require measurable-kernel and `L^2` domain care. The quantum theorem supplies substantially broader operator-algebraic prior art, but this finding claims only the finite classical consequence needed to connect AF-126 to AF-143.

8. **There is still no arithmetic conclusion.** To use `(7)` in an RH-facing line one must derive a source-natural finite experiment/control family and compression, then prove that the relevant common-reference chi-square losses are small. Introducing an artificial statistical family whose mixture already encodes the desired discriminator would merely move the answer into the source model.

## Consequences for Arithmetic Fidelity

The generic positive question left at the end of AF-143 is now narrowed. In finite statistical experiments, a deficiency-dominating divergence profile with a proved common-recovery converse does exist: common-reference chi-square data-processing loss controls the Bayes/Petz reconstruction error through `(7)`.

This sharpens the next research gate. It is no longer enough to ask abstractly for another metric stronger than Fisher or pairwise total variation. For a concrete arithmetic compression, the useful questions are now:

- can the source force a non-artificial finite experiment or matched-control family;
- can one justify a common reference mixture or an equivalent intrinsic reference object;
- does the arithmetic discriminator have uniformly small finite-displacement chi-square loss under the proposed compression;
- and is that certificate materially smaller than retaining the full likelihood-ratio data already identified by AF-013?

A failure at the last point matters. The Bayes/Petz certificate is mathematically valid even if evaluating its chi-square profile requires almost all the discarded information. Arithmetic usefulness therefore still requires a **compression gain**, not merely a correct recovery theorem.