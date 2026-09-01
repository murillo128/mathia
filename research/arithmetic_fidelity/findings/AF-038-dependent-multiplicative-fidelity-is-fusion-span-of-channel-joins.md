# AF-038 — Dependent multiplicative fidelity is the fusion span of bounded channel joins

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `NEGATIVE/OBSTRUCTION`

## Claim

Let

\[
(\Omega,\mathcal F,\mathbb P)
\]

be an arbitrary probability space and let

\[
\mathcal F_1,\ldots,\mathcal F_m\subseteq\mathcal F
\]

be completed sub-`\sigma`-fields. No independence, product structure, coordinate representation, or commuting-projection hypothesis is assumed.

For `I\subseteq[m]`, write

\[
\mathcal F_I=\bigvee_{j\in I}\mathcal F_j,
\qquad
V_I=L^2(\mathcal F_I),
\qquad
P_I f=\mathbb E[f\mid\mathcal F_I],
\]

with `\mathcal F_\varnothing` the trivial completed `\sigma`-field. For `0\le r\le m`, define the bounded multiplicative channel-degree space

\[
W_r
=
\overline{\operatorname{span}}^{\,L^2(\mathbb P)}
\left\{
\prod_{\ell=1}^{k} f_\ell:
0\le k\le r,\;
f_\ell\in L^\infty(\mathcal F_{j_\ell})
\right\}.
\]

Repeated channel indices are allowed, but they do not add degree: a product of bounded functions from one `\mathcal F_j` is again a bounded `\mathcal F_j`-measurable function.

Then:

1. **Arbitrary-source degree is exactly the closed fusion span of at most `r`-way channel joins.**
   \[
   \boxed{
   W_r
   =
   \overline{
   \sum_{\substack{I\subseteq[m]\\ |I|\le r}}
   V_I
   }^{\,L^2(\mathbb P)}.
   }
   \]
   Thus the correct source-dependent replacement for AF-037's product-space set-cover filtration is the family of actual join subspaces `L^2(\bigvee_{j\in I}\mathcal F_j)`. No Hoeffding decomposition is needed.

2. **The invisible directions are the common conditional-expectation kernel.**
   \[
   \boxed{
   W_r^\perp
   =
   \bigcap_{\substack{I\subseteq[m]\\ |I|\le r}}
   \ker P_I.
   }
   \]
   Hence a target direction `g\in L^2(\mathbb P)` is completely invisible to every degree-`r` upstream channel combination exactly when
   \[
   \mathbb E[g\mid\mathcal F_I]=0
   \qquad
   \text{for every }|I|\le r.
   \]

3. **A positive fusion operator gives the exact support projection without requiring commuting projections.** Define
   \[
   S_r
   =
   \sum_{\substack{I\subseteq[m]\\ |I|\le r}}P_I.
   \]
   Then
   \[
   \boxed{
   \ker S_r=W_r^\perp,
   \qquad
   \overline{\operatorname{Ran}S_r}=W_r.
   }
   \]
   If `E_r=\mathbf 1_{(0,\infty)}(S_r)` denotes the support projection of the bounded positive operator `S_r`, then
   \[
   \boxed{E_r=P_{W_r}.}
   \]
   Consequently
   \[
   \boxed{
   \operatorname{dist}(g,W_r)^2
   =
   \|(I-E_r)g\|_2^2.
   }
   \]
   This is the dependent-source analogue of AF-037's explicit missing-Hoeffding-energy formula.

4. **Exact recoverability and stable recoverability separate.** The finite family of join subspaces is a fusion frame for `W_r` precisely when there is an `A_r>0` such that
   \[
   \boxed{
   A_r\|h\|_2^2
   \le
   \sum_{\substack{I\subseteq[m]\\ |I|\le r}}
   \|P_Ih\|_2^2
   \qquad(h\in W_r).
   }
   \]
   Equivalently, `S_r|_{W_r}` is bounded below. In that case the retained `r`-way channel projections provide stable reconstruction on `W_r`. The support identity above remains valid even when no such positive lower bound exists, so **zero-error structural fidelity does not by itself imply numerically stable recovery**. In finite-dimensional `W_r`, the lower bound is automatic.

5. **The filtration remains exact but loses a source-independent combinatorial grading.**
   \[
   W_0\subseteq W_1\subseteq\cdots\subseteq W_m
   =
   L^2\!\left(\bigvee_{j=1}^m\mathcal F_j\right).
   \]
   Define
   \[
   \mathcal G_r=W_r\ominus W_{r-1},
   \qquad r\ge1.
   \]
   Then
   \[
   \boxed{
   E_r-E_{r-1}
   \text{ is the orthogonal projector onto }\mathcal G_r.
   }
   \]
   The grade `\mathcal G_r` is therefore intrinsic to the actual source law and retained channel fields. Under dependence it need not correspond to an `r`-coordinate interaction face or a hypergraph cover number.

6. **AF-037 is recovered exactly in the independent product-coordinate case.** If
   \[
   \mathbb P=Q=\bigotimes_{i=1}^d q_i,
   \qquad
   \mathcal F_j=\sigma(X_i:i\in A_j),
   \]
   then the Hoeffding spaces `\mathcal H_S` of AF-034 diagonalize every `P_I`. On `\mathcal H_S`,
   \[
   S_r
   =
   N_r(S)\,I,
   \]
   where
   \[
   N_r(S)
   =
   \#\left\{
   I\subseteq[m]:
   |I|\le r,\;
   S\subseteq\bigcup_{j\in I}A_j
   \right\}.
   \]
   Therefore
   \[
   N_r(S)>0
   \iff
   \kappa_{\mathcal A}(S)\le r,
   \]
   and
   \[
   \boxed{
   W_r
   =
   \bigoplus_{\kappa_{\mathcal A}(S)\le r}\mathcal H_S,
   }
   \]
   exactly AF-037. With unit weights the positive eigenvalues are positive integers, so the fusion lower bound on `W_r` is at least `1`.

7. **Dependence can collapse the apparent set-cover degree all the way to one.** Let `X_1,X_2` be independent Rademacher variables and set
   \[
   X_3=X_1X_2.
   \]
   Put `\mathcal F_j=\sigma(X_j)`. Then
   \[
   V_j=\operatorname{span}\{1,X_j\},
   \]
   while
   \[
   \{1,X_1,X_2,X_3\}
   =
   \{1,X_1,X_2,X_1X_2\}
   \]
   is an orthogonal basis of the four-dimensional `L^2(\mathbb P)`. Hence
   \[
   \boxed{
   W_1
   =
   V_1+V_2+V_3
   =
   L^2(\mathbb P).
   }
   \]
   No individual channel is the full `\sigma`-field, but the source relation has moved the nominal three-way product interaction into the linear span of the singleton channels. For three independent coordinates with the same singleton channel hypergraph, AF-037 instead has a genuine degree-three component. Therefore **channel cover number is a theorem of the product source model, not an invariant of the channel hypergraph alone**.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{multiplicative fidelity degree is determined by actual source join subspaces; product set cover is only their independent-coordinate normal form.}
}
\]

This both extends and limits AF-037. Its exact cover-number filtration is correct under the product hypotheses, but those combinatorial grades cannot be transported into a dependent arithmetic source merely because the same channel labels or overlaps remain visible.

## Derivation

### Products from `r` channels cannot leave their joined `\sigma`-field

Take a generator

\[
F=\prod_{\ell=1}^k f_\ell,
\qquad k\le r,
\qquad
f_\ell\in L^\infty(\mathcal F_{j_\ell}).
\]

Let `I` be the set of distinct channel indices appearing among the factors. Then `|I|\le r`, and `F` is measurable with respect to

\[
\mathcal F_I=\bigvee_{j\in I}\mathcal F_j.
\]

Thus

\[
F\in V_I.
\]

Taking linear spans and `L^2` closure gives

\[
W_r
\subseteq
\overline{\sum_{|I|\le r}V_I}.
\]

Nothing here uses independence.

### Every `L^2` function of an `r`-way join is approximable by bounded channel products

Fix `I\subseteq[m]` with `|I|\le r`. Consider the class

\[
\Pi_I
=
\left\{
\bigcap_{j\in I}A_j:
A_j\in\mathcal F_j
\right\},
\]

allowing `A_j=\Omega`. This is a `\pi`-system and

\[
\sigma(\Pi_I)=\mathcal F_I.
\]

For every `A=\bigcap_{j\in I}A_j\in\Pi_I`,

\[
\mathbf 1_A
=
\prod_{j\in I}\mathbf 1_{A_j},
\]

so `\mathbf 1_A\in W_r`.

Let

\[
\mathcal D
=
\{A\in\mathcal F_I:\mathbf 1_A\in W_r\}.
\]

Because `W_r` is a closed linear subspace containing constants, `\mathcal D` is a Dynkin system: it contains `\Omega`, is closed under relative complements inside nested sets, and under countable disjoint unions because the partial indicator sums converge in `L^2`. Since `\Pi_I\subseteq\mathcal D`, the `\pi`-`\lambda` theorem gives

\[
\mathcal D=\mathcal F_I.
\]

Therefore every `\mathcal F_I`-measurable indicator belongs to `W_r`, hence every bounded simple `\mathcal F_I`-measurable function belongs to `W_r`, and density yields

\[
V_I=L^2(\mathcal F_I)\subseteq W_r.
\]

Summing over all `|I|\le r` gives the reverse inclusion and proves the main identity.

This is the precise point at which AF-037's tensor-product proof can be discarded. The general mechanism is not an interaction decomposition; it is ordinary measurable generation plus `L^2` closure.

### Common kernels and the fusion support operator

For every `I`, `P_I` is the orthogonal projection onto `V_I`. Therefore

\[
V_I^\perp=\ker P_I.
\]

For a finite family of subspaces,

\[
\left(
\overline{\sum_{|I|\le r}V_I}
\right)^\perp
=
\bigcap_{|I|\le r}V_I^\perp,
\]

which proves

\[
W_r^\perp
=
\bigcap_{|I|\le r}\ker P_I.
\]

Now `S_r` is bounded, positive, and self-adjoint. For every `h\in L^2(\mathbb P)`,

\[
\langle S_rh,h\rangle
=
\sum_{|I|\le r}\langle P_Ih,h\rangle
=
\sum_{|I|\le r}\|P_Ih\|_2^2.
\]

Hence

\[
S_rh=0
\iff
P_Ih=0\quad\text{for every }|I|\le r,
\]

so

\[
\ker S_r=W_r^\perp.
\]

For a bounded self-adjoint operator,

\[
\overline{\operatorname{Ran}S_r}
=
(\ker S_r)^\perp,
\]

therefore

\[
\overline{\operatorname{Ran}S_r}=W_r.
\]

The support projection of a positive operator is the orthogonal projection onto the closure of its range, proving `E_r=P_{W_r}`.

### Exact versus stable recovery

The support of `S_r` sees only whether a direction survives at all. Stability needs a spectral gap away from zero on that support.

Indeed,

\[
\langle S_rh,h\rangle
=
\sum_{|I|\le r}\|P_Ih\|_2^2.
\]

Thus a lower fusion-frame bound is exactly the operator inequality

\[
S_r\ge A_r E_r.
\]

When it holds, `S_r` has a bounded inverse on `W_r` and the standard frame-of-subspaces reconstruction machinery applies. When it fails, there are unit vectors `h_n\in W_r` for which all retained `r`-way projections become collectively arbitrarily small even though no nonzero direction is exactly annihilated.

This distinction matters for compression: a representation can be faithful in the exact factorization sense while becoming arbitrarily ill-conditioned under perturbation. AF-009 similarly separates exact zero defect from quantitative loss under stochastic garbling; here the same separation appears as the bottom of the fusion-operator spectrum.

## Minimal controls

### Product-source control reproduces AF-037

Under the independent product law of AF-034, each Hoeffding component `\mathcal H_S` is either fixed or killed by `P_I`:

\[
P_I|_{\mathcal H_S}
=
\begin{cases}
I,&S\subseteq\bigcup_{j\in I}A_j,\\
0,&\text{otherwise}.
\end{cases}
\]

Summing these selectors gives the integer multiplier `N_r(S)`. The support condition `N_r(S)>0` is exactly the set-cover condition `\kappa_{\mathcal A}(S)\le r`. Thus no part of AF-037 is contradicted; the present theorem identifies the hypothesis responsible for its combinatorial diagonalization.

### Dependent parity control kills the hypergraph interpretation

For the Rademacher example `X_3=X_1X_2`,

\[
S_1=P_\varnothing+P_1+P_2+P_3
\]

acts diagonally on the orthogonal basis `\{1,X_1,X_2,X_3\}` with eigenvalues

\[
4,1,1,1.
\]

So the support is already all of `L^2`, and the fusion lower bound is `1`.

The same three singleton labels under a product law would leave the three-way Hoeffding component invisible until degree three. The change is entirely in the source law. Any proposed "interaction order" or "channel-cover complexity" for a dependent source must therefore be derived from its actual join spaces or another justified decomposition, not copied from the product coordinate labels.

## Destination-category boundary

The theorem still concerns **upstream bounded observables** before they are separately compressed. It does not license multiplying scalar summaries, marginal laws, traces, spectra, or other already-compressed outputs.

The exact object retained at degree `r` is

\[
W_r
=
\overline{\sum_{|I|\le r}L^2(\mathcal F_I)},
\]

where each `\mathcal F_I` is an actual upstream joined information field. If a destination gives only values of some functionals on the individual channels, then access to `P_I`, `V_I`, or products of channel observables must itself be proved to factor through that destination.

This preserves the AF-030/AF-031/AF-036 warning:

\[
\text{upstream multiplicative closure}
\ne
\text{post-compression nonlinear processing}
\]

without an independent factorization theorem.

## Prior art and novelty assessment

No novelty is claimed for the `\pi`-`\lambda` / monotone-class generation argument, conditional expectation as an `L^2` orthogonal projection, sums of measurable-function subspaces, frames of subspaces/fusion frames, or dependent-input functional decompositions.

- Olav Kallenberg, ***Foundations of Modern Probability***, 3rd ed., Probability Theory and Stochastic Modelling 99, Springer (2021), DOI `10.1007/978-3-030-61871-1`. Role: authoritative measure-theoretic probability source for generated `\sigma`-fields, monotone-class arguments, and conditional expectation as the standard projection machinery underlying the proof.
- L. Rüschendorf and W. Thomsen, **“Closedness of Sum Spaces and the Generalized Schrödinger Problem,”** *Theory of Probability and Its Applications* 42(3), 483–494 (1998), DOI `10.1137/S0040585X97976301`; original Russian publication 42(3), 576–590 (1997). Role: direct prior art on closedness of sums of measurable-function spaces, with applications to multivariate marginals and additive statistical models; it prevents treating closed-sum geometry of the `V_I` as a new phenomenon.
- Peter G. Casazza and Gitta Kutyniok, **“Frames of Subspaces,”** *Contemporary Mathematics* 345, 87–113 (2004), DOI `10.1090/conm/345/06242`, arXiv:`math/0311384`. Role: foundational frames-of-subspaces language, including analysis, synthesis, frame operators, completeness, minimality, exactness, and stable reconstruction from subspaces.
- Peter G. Casazza, Gitta Kutyniok, and Shidong Li, **“Fusion Frames and Distributed Processing,”** *Applied and Computational Harmonic Analysis* 25(1), 114–132 (2008), DOI `10.1016/j.acha.2007.10.001`, arXiv:`math/0605374`. Role: standard fusion-frame formulation and robust reconstruction from overlapping weighted subspaces; it supplies the established stability language for the lower bound on `S_r`.
- Marouane Il Idrissi, Nicolas Bousquet, Fabrice Gamboa, Bertrand Iooss, and Jean-Michel Loubes, **“Hoeffding decomposition of black-box models with dependent inputs,”** arXiv:`2310.06567` (2023). Role: close modern prior art showing that dependent inputs do not inherit the classical independent Hoeffding decomposition for free and that a dependent decomposition requires additional structure, including oblique projections under explicit assumptions.

The individual ingredients are classical. The Arithmetic Fidelity contribution is the **boundary theorem organization relative to AF-037**: bounded multiplicative degree for an arbitrary source is exactly the fusion span of its actual `r`-way joined information fields; the independent-product channel-cover filtration is one diagonal normal form of that operator statement, not a source-free combinatorial invariant. The parity control gives an exact falsifier for transporting product interaction degree into a dependent source.

## Relation to the current Arithmetic Fidelity frontier

AF-035 showed that the Boolean meet law

\[
P_AP_B=P_{A\cap B}
\]

for raw coordinate conditional expectations is itself equivalent to the relevant conditional-independence structure, and that the full Boolean law characterizes product independence. AF-036 then separated linear Hilbert joins from generated measurable joins under the product model, while AF-037 graded the latter by channel-cover degree.

The present result removes the product hypothesis from the multiplicative-degree question without pretending that a dependent Hoeffding basis survives. The exact replacement is:

\[
\boxed{
\text{product interaction faces/set cover}
\quad\longrightarrow\quad
\text{source-dependent join subspaces/fusion support}.
}
\]

This advances the master frontier from "extend target-relative interaction fidelity to dependent settings" to a sharper next question: for a concrete arithmetic or explicit-formula source, identify the genuinely available channel `\sigma`-fields or closed observable subspaces and determine the support and small-spectrum behavior of the corresponding fusion operator. Only after that audit is it legitimate to attach a combinatorial interaction grading, a stable reconstruction claim, or an RH-relevant discriminator to the retained channel architecture.
