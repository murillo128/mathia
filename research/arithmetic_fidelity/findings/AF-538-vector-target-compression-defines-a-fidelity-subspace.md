# AF-538 — Vector-target compression defines a fidelity subspace

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `CLASSICAL-INGREDIENTS` · `ARITHMETIC-FIDELITY` · `SEMIPARAMETRIC` · `VECTOR-TARGET` · `LOEWNER-ORDER` · `FIDELITY-SUBSPACE` · `MARKOV-COMPOSITION` · `NO-NOVELTY-CLAIM`

## Claim

AF-537 gives an exact three-part loss budget for one scalar target direction propagated through a chain of parameter-independent Markov channels with possibly enlarging nuisance spaces. For a finite-dimensional target, the same geometry is matrix-valued and yields more than monotonicity: it identifies exactly **which linear combinations of the target survive**.

At stage `j`, let

\[
H_j=L_0^2(P_j)
\]

be the tangent Hilbert space, let `\Lambda_j\subset H_j` be the closed nuisance tangent space, and let the target parameter have dimension `d`. Write the target score vector as

\[
s_j=(s_{j,1},\ldots,s_{j,d}).
\]

Project each component away from nuisance and package the resulting efficient scores into the linear score operator

\[
\mathcal E_j:\mathbb R^d\to H_j,
\qquad
\mathcal E_j a
=
\sum_{r=1}^d a_r (I-\Pi_{\Lambda_j})s_{j,r}.
\tag{1}
\]

The efficient information matrix is the Gram operator

\[
J_j=\mathcal E_j^*\mathcal E_j.
\tag{2}
\]

Let a parameter-independent Markov kernel send stage `j` to stage `j+1`, with score contraction

\[
C_j:H_j\to H_{j+1},
\qquad
C_j f=\mathbb E[f(X_j)\mid X_{j+1}].
\tag{3}
\]

Assume the downstream target score vector is obtained componentwise by `C_j`, and that the actual downstream nuisance space contains the pushed-forward upstream nuisance:

\[
N_{j+1}:=\overline{C_j\Lambda_j}
\subseteq
\Lambda_{j+1}.
\tag{4}
\]

Write the orthogonal nuisance increment as

\[
D_{j+1}:=\Lambda_{j+1}\cap N_{j+1}^{\perp},
\qquad
\Lambda_{j+1}=N_{j+1}\oplus D_{j+1}.
\tag{5}
\]

Then the efficient-score operator propagates exactly as

\[
\boxed{
\mathcal E_{j+1}
=(I-\Pi_{\Lambda_{j+1}})C_j\mathcal E_j.
}
\tag{6}
\]

Moreover, the efficient-information loss is the positive-semidefinite matrix identity

\[
\boxed{
J_j-J_{j+1}=A_j+B_j+Q_j,
}
\tag{7}
\]

where

\[
A_j
=
\mathcal E_j^*(I-C_j^*C_j)\mathcal E_j,
\tag{8}
\]

\[
B_j
=
\mathcal E_j^*C_j^*\Pi_{N_{j+1}}C_j\mathcal E_j,
\tag{9}
\]

and

\[
Q_j
=
\mathcal E_j^*C_j^*\Pi_{D_{j+1}}C_j\mathcal E_j.
\tag{10}
\]

All three matrices are positive semidefinite. They are respectively the vector-target forms of direct channel erasure, pushed-nuisance recontamination, and new-nuisance reclassification.

For every target direction `a\in\mathbb R^d`, the scalar information loss is exactly

\[
a^*(J_j-J_{j+1})a
=
a^*A_ja+a^*B_ja+a^*Q_ja,
\tag{11}
\]

so AF-537 is recovered by restricting to any one-dimensional target submodel.

The important extra object is the **fidelity subspace**

\[
\boxed{
\mathcal F_j:=\ker(J_j-J_{j+1}).
}
\tag{12}
\]

It is exactly the set of target combinations whose efficient information survives that stage. Under the conditional-expectation realization,

\[
\boxed{
a\in\mathcal F_j
\iff
\begin{cases}
\mathcal E_j a\text{ is measurable with respect to }X_{j+1},\\
C_j\mathcal E_j a\perp D_{j+1}.
\end{cases}
}
\tag{13}
\]

Thus a multidimensional compression need not be classified only as faithful or unfaithful. It can be faithful on a precise linear subspace of target directions and lossy on its complement.

For a chain of `m` stages,

\[
\boxed{
J_0-J_m
=
\sum_{j=0}^{m-1}(A_j+B_j+Q_j),
}
\tag{14}
\]

and because every summand is positive semidefinite,

\[
\boxed{
\ker(J_0-J_m)
=
\bigcap_{j=0}^{m-1}\mathcal F_j.
}
\tag{15}
\]

So exact survival through a chain is an intersection law: a target combination survives end to end if and only if it loses no efficient information at **every** stage. A direction damaged at one stage cannot be restored by later parameter-independent post-processing.

When `J_0` is positive definite, the normalized endpoint operator

\[
\Phi_{0\to m}
:=
J_0^{-1/2}J_mJ_0^{-1/2}
\tag{16}
\]

satisfies

\[
0\preceq\Phi_{0\to m}\preceq I.
\tag{17}
\]

Its eigenvalues give a coordinate-free first-order **fidelity spectrum** relative to the source efficient-information metric. Eigenvalue `1` directions are precisely the fully preserved target combinations after whitening; values in `(0,1)` quantify partial retention; eigenvalue `0` marks complete first-order loss.

## Representation declaration

This finding uses a local regular statistical representation as a controlled model of property survival under compression.

- **Source object:** a finite-dimensional target direction together with a possibly infinite-dimensional nuisance tangent space.
- **Target carrier:** the efficient-score operator `\mathcal E_j`, not the raw score vector.
- **Forward operation:** a parameter-independent Markov channel acting componentwise on scores by conditional expectation.
- **Equivalence:** nuisance tangent directions are quotiented out by orthogonal projection.
- **Additional semantic quotient:** `D_{j+1}` records downstream nuisance directions not generated by the upstream nuisance family.
- **Fidelity object:** the efficient-information matrix `J_j` and, more finely, the nullspace of its stagewise loss.

The statistical representation is not asserted to be intrinsic to any arithmetic construction. An arithmetic application must independently identify a finite family of target perturbations, admissible nuisance/control perturbations, and a legitimate compression channel.

## Derivation

### 1. Efficient-score propagation is operator-valued

Let `\mathcal S_j:\mathbb R^d\to H_j` denote the raw target-score operator,

\[
\mathcal S_j a=\sum_r a_rs_{j,r}.
\tag{18}
\]

Componentwise nuisance projection gives

\[
\mathcal E_j=(I-\Pi_{\Lambda_j})\mathcal S_j.
\tag{19}
\]

Write

\[
\mathcal S_j=\mathcal E_j+\mathcal V_j,
\qquad
\operatorname{ran}(\mathcal V_j)\subseteq\Lambda_j.
\tag{20}
\]

The downstream raw target-score operator is

\[
\mathcal S_{j+1}=C_j\mathcal S_j.
\tag{21}
\]

Because `C_j\operatorname{ran}(\mathcal V_j)\subseteq N_{j+1}\subseteq\Lambda_{j+1}`,

\[
\begin{aligned}
\mathcal E_{j+1}
&=(I-\Pi_{\Lambda_{j+1}})\mathcal S_{j+1}\\
&=(I-\Pi_{\Lambda_{j+1}})C_j(\mathcal E_j+\mathcal V_j)\\
&=(I-\Pi_{\Lambda_{j+1}})C_j\mathcal E_j,
\end{aligned}
\tag{22}
\]

which proves (6).

### 2. The loss is a sum of three positive-semidefinite Gram defects

Using (2) and (6),

\[
\begin{aligned}
J_{j+1}
&=\mathcal E_j^*C_j^*(I-\Pi_{\Lambda_{j+1}})C_j\mathcal E_j\\
&=\mathcal E_j^*C_j^*C_j\mathcal E_j
-\mathcal E_j^*C_j^*\Pi_{\Lambda_{j+1}}C_j\mathcal E_j.
\end{aligned}
\tag{23}
\]

Subtracting from `J_j=\mathcal E_j^*\mathcal E_j` gives

\[
J_j-J_{j+1}
=
\mathcal E_j^*(I-C_j^*C_j)\mathcal E_j
+
\mathcal E_j^*C_j^*\Pi_{\Lambda_{j+1}}C_j\mathcal E_j.
\tag{24}
\]

Since `C_j` is a contraction, `I-C_j^*C_j\succeq0`, hence `A_j\succeq0`. Since (5) is an orthogonal direct sum,

\[
\Pi_{\Lambda_{j+1}}
=
\Pi_{N_{j+1}}+\Pi_{D_{j+1}},
\tag{25}
\]

which splits the second term of (24) into `B_j+Q_j`. Each is a Gram matrix of projected score components and is therefore positive semidefinite. This proves (7).

Under a joint realization of the channel, the direct term also has the concrete covariance form

\[
A_j
=
\mathbb E\!\left[
\operatorname{Cov}(e_j(X_j)\mid X_{j+1})
\right],
\tag{26}
\]

where `e_j` is the `d`-vector of efficient-score components. Equation (26) makes the Loewner positivity of direct erasure transparent.

### 3. The kernel is the exact preserved-direction space

Fix `a\in\mathbb R^d`. Applying (7) to `a` gives

\[
a^*(J_j-J_{j+1})a
=
\|\mathcal E_ja\|^2
-\|C_j\mathcal E_ja\|^2
+
\|\Pi_{N_{j+1}}C_j\mathcal E_ja\|^2
+
\|\Pi_{D_{j+1}}C_j\mathcal E_ja\|^2.
\tag{27}
\]

Every term is nonnegative. Therefore the quadratic form vanishes exactly when each relevant term vanishes.

Equality in the conditional-expectation contraction holds exactly when the scalar random variable `\mathcal E_ja` is already measurable with respect to the downstream observation. In that case, for every `\lambda\in\Lambda_j`,

\[
\langle C_j\mathcal E_ja,C_j\lambda\rangle_{H_{j+1}}
=
\langle \mathcal E_ja,\lambda\rangle_{H_j}
=0,
\tag{28}
\]

so orthogonality to `N_{j+1}=\overline{C_j\Lambda_j}` follows automatically. The only additional equality condition is orthogonality to `D_{j+1}`. This proves (13).

Because `J_j-J_{j+1}` is positive semidefinite, the zero set of its quadratic form is its ordinary linear kernel. Hence the preserved target combinations form a genuine linear subspace rather than merely a collection of isolated directions.

### 4. Sequential survival is intersection, not compensation

Summing (7) over stages telescopes the information matrices and gives (14). For positive-semidefinite matrices `L_0,\ldots,L_{m-1}`,

\[
\ker\!\left(\sum_jL_j\right)
=
\bigcap_j\ker L_j,
\tag{29}
\]

because

\[
a^*\!\left(\sum_jL_j\right)a=0
\iff
a^*L_ja=0\text{ for every }j.
\tag{30}
\]

Taking `L_j=A_j+B_j+Q_j` proves (15). There is therefore no matrix-level cancellation by which one stage can lose a target combination and a later stage can restore its original first-order information through post-processing.

### 5. Normalization separates target coordinates from fidelity

If `J_0\succ0`, equation (14) gives `0\preceq J_m\preceq J_0`. Congruence by `J_0^{-1/2}` yields (17). If target coordinates are changed by an invertible linear map, the pair `(J_0,J_m)` changes by congruence while the generalized eigenvalues of

\[
J_mv=\lambda J_0v
\tag{31}
\]

are unchanged. These generalized eigenvalues are precisely the spectrum of `\Phi_{0\to m}`. Thus the fidelity spectrum does not depend on an arbitrary linear parametrization of the target.

The multiplicity of `\lambda=1` is the dimension of the end-to-end fidelity subspace. It records exact survival, while the remaining eigenvalues quantify directional weakening without turning the matrix inequality into a single scalar determinant or trace that could hide which target combinations were lost.

## Matched controls: identical endpoint information, different loss mechanisms

A two-dimensional Gaussian pair shows why the decomposition carries information that the endpoint matrix alone does not.

### Control A: observation erasure

Let

\[
X\sim N(\theta,I_2),
\qquad
\theta=(\theta_1,\theta_2),
\tag{32}
\]

with no nuisance. At `\theta=0`,

\[
\mathcal E_0(a_1,a_2)=a_1X_1+a_2X_2,
\qquad
J_0=I_2.
\tag{33}
\]

Compress to `Y=X_1`. Then

\[
J_1=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
A_0=
\begin{pmatrix}
0&0\\
0&1
\end{pmatrix},
\qquad
B_0=Q_0=0.
\tag{34}
\]

The fidelity subspace is `\operatorname{span}\{(1,0)\}`: the `\theta_1` direction survives and the `\theta_2` direction is deleted by the observation channel.

### Control B: semantic reclassification with no observation loss

Keep the same full observation `X` and the same target `\theta`, but enlarge the downstream model with a nuisance parameter `\zeta` in the second mean direction:

\[
X\sim N(\theta_1e_1+\theta_2e_2+\zeta e_2,I_2).
\tag{35}
\]

The channel is the identity, so `A_0=0`, and there was no upstream nuisance, so `B_0=0`. The new nuisance increment is generated by score `X_2`, giving

\[
Q_0=
\begin{pmatrix}
0&0\\
0&1
\end{pmatrix}.
\tag{36}
\]

Nevertheless the endpoint efficient-information matrix is again

\[
J_1=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}.
\tag{37}
\]

The two controls therefore have **identical source and endpoint efficient-information matrices and the same fidelity subspace**, but the cause of loss is different: Control A forgets an observation direction, whereas Control B keeps all observations and changes which target variation is declared distinguishable from nuisance.

This is a useful diagnostic for arithmetic representations. Comparing only source and destination invariants can show that information was lost but not **where or why**. A stagewise decomposition is required to distinguish carrier destruction from an enlargement of the destination equivalence relation.

## Minimal lifts for selected target subspaces

Let `U\subseteq\mathbb R^d` be a declared target subspace and suppose there is no fixed downstream semantic obstruction on `U`, meaning the surviving efficient scores for `U` are orthogonal to `D_{j+1}`. Among observation sigma-fields extending the existing output, exact preservation of efficient information on every direction in `U` requires measurability of

\[
\{\mathcal E_ja:a\in U\}.
\tag{38}
\]

Hence the minimal first-order observation lift is generated by the downstream observation together with any basis of the efficient-score image `\mathcal E_jU`.

For `U=\mathbb R^d`, this reduces to adjoining the full efficient-score vector, the vector analogue of AF-535. For a proper `U`, only the score combinations spanning `\mathcal E_jU` are required. Thus the fidelity subspace also tells which target-relative marks are unnecessary: already preserved directions need no repair, while semantically reclassified directions cannot be repaired by observation enrichment alone.

## Prior art and novelty assessment

The underlying statistical facts are classical, and no theorem-level novelty is claimed.

- Abram Kagan and C. Radhakrishna Rao, **“Some properties and applications of the efficient Fisher score,”** *Journal of Statistical Planning and Inference* 116(2), 343–352 (2003), DOI `10.1016/S0378-3758(02)00351-8`. The paper explicitly studies monotonicity and superadditivity of the **efficient Fisher information matrix**; it is direct prior art for the Loewner monotonicity used here.
- Rachel M. Fewster and Peter E. Jupp, **“Information on parameters of interest decreases under transformations,”** *Journal of Multivariate Analysis* 120, 34–39 (2013), DOI `10.1016/j.jmva.2013.05.010`. It proves transformation monotonicity for information on parameters of interest using partitioned positive-definite matrices and Schur complements; this directly covers the classical matrix-order background.
- Janet M. Begun, W. J. Hall, Wei-Min Huang, and Jon A. Wellner, **“Information and Asymptotic Efficiency in Parametric-Nonparametric Models,”** *The Annals of Statistics* 11(2), 432–452 (1983), DOI `10.1214/aos/1176346151`. This supplies the classical tangent-space and efficient-information setting behind the operator formulation.
- Peter J. Bickel, Chris A. J. Klaassen, Ya'acov Ritov, and Jon A. Wellner, ***Efficient and Adaptive Estimation for Semiparametric Models***, Johns Hopkins University Press (1993; Springer reprint 1998). This is standard background for vector parameters of interest, nuisance tangent spaces, efficient scores, and efficient information.
- Pablo Zegers, **“Fisher Information Properties,”** *Entropy* 17(7), 4918–4939 (2015), DOI `10.3390/e17074918`. This gives ordinary Fisher-information data processing along Markov chains and helps separate the generic Markov monotonicity ingredient from the nuisance-relative refinement.

The literature above means neither matrix monotonicity nor efficient-information projection is claimed as new. AF-538's line-local contribution is the organization needed for Arithmetic Fidelity: lift AF-537's three loss mechanisms to positive-semidefinite operators, identify the kernel of the loss as the exact **target-direction fidelity subspace**, prove its intersection law under sequential compression, and separate endpoint-equivalent observation loss from semantic reclassification by matched controls.

## Boundary conditions and falsification tests

1. **Finite target dimension is assumed.** The operator formulas suggest an infinite-dimensional target analogue, but closed ranges, domains, trace notions, and generalized spectral statements then require additional functional analysis and are not asserted here.

2. **The nuisance inclusion remains essential.** The recursion assumes `\overline{C_j\Lambda_j}\subseteq\Lambda_{j+1}`. If valid upstream nuisance paths disappear from the destination model, the target problem itself has changed in another way and (6) must be re-derived.

3. **The channel is parameter-independent.** A parameter-dependent observation mechanism contributes its own score terms and is outside this identity.

4. **The result is local and first-order.** `\mathcal F_j` classifies target combinations preserving efficient Fisher information at the chosen baseline. It does not imply Blackwell equivalence, global identifiability, finite-sample sufficiency, or exact recovery of the underlying source object.

5. **The fidelity spectrum requires `J_0\succ0`.** If source target directions are already nonidentifiable, one should first quotient by `\ker J_0` or work with a pseudoinverse-supported version; blindly applying `J_0^{-1/2}` is invalid.

6. **Eigenvalues in `(0,1)` are not probabilities.** They are generalized directional information-retention factors in the source information metric. They do not by themselves identify a stochastic recovery map.

7. **A unit generalized eigenvalue is an exact first-order equality statement.** Small loss eigenvalues give approximate information preservation but do not automatically provide a uniform reconstruction modulus for arbitrary observables.

8. **The decomposition depends on the declared path.** Two routes with the same endpoint information matrix can allocate loss differently across `A_j`, `B_j`, and `Q_j`, as the matched controls show. This is a feature when auditing representations, but it prevents treating the three terms as endpoint invariants.

9. **Semantic loss needs independent justification.** Declaring any target direction nuisance can manufacture a desired fidelity subspace. Arithmetic applications must derive admissible controls, gauge directions, or equivalence classes independently of the claimed discriminator.

10. **Minimal lifts are target-relative.** Adjoining efficient-score combinations is minimal only in the local observation-sigma-field order for the declared target subspace and fixed nuisance semantics. It is not automatically source-natural or arithmetically canonical.

## Consequence for Arithmetic Fidelity

The scalar question “did the discriminator survive?” is too coarse when a representation carries several candidate discriminator directions. AF-538 replaces it with a linear object:

\[
\text{target space}
\supseteq
\mathcal F_j
=
\text{directions preserved by stage }j.
\tag{39}
\]

For a chain, these spaces can only intersect; they cannot regain a direction lost earlier. The normalized information spectrum further records how strongly the remaining directions are attenuated without hiding them inside one aggregate scalar.

For later arithmetic use, this suggests a sharper audit of multi-feature encodings. Rather than asking whether a spectrum, trace, quotient, average, or positive form preserves “the arithmetic information” as one indivisible object, specify a finite family of target perturbations and compute which linear combinations remain visible after each transformation. The resulting fidelity subspace separates exact survivors from collapsed combinations, while the `A/B/Q` budget identifies whether the loss came from forgetting the carrier, mixing it with existing controls, or enlarging the destination equivalence relation.