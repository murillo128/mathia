# AF-133 — Restricted witness composition requires quotient-compatible recovery

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `RESTRICTED-WITNESS`, `QUOTIENT-COMPATIBILITY`, `COMPOSITION-GATE`, `PROFILE-CALCULUS`, `NO-NOVELTY-CLAIM`

## Claim

AF-129 shows that a symmetric restricted witness class induces a quotient seminorm on recovery residuals. AF-131--AF-132 show, in the nondegenerate metric-local/Wasserstein case, that quantitative recovery errors compose only after retaining the transport regularity of the intermediate inverse.

There is a more basic gate before that regularity calculus can even be finite: **an intermediate recovery must descend through the invisible quotient of the downstream witness class.** If it turns a downstream-invisible residual into an upstream-visible one, its cross-category contraction coefficient is infinite, and stagewise zero restricted defects need not compose to zero.

For a finite set `X`, let

\[
H_X:=\left\{\mu\in\mathbb R^X:\sum_x\mu(x)=0\right\}
\tag{1}
\]

be the zero-mass residual space. Let

\[
A_X\subset H_X^*
\]

be a nonempty compact convex centrally symmetric witness body containing `0`, understood after the parameterwise-constant gauge reduction of AF-129. It induces the seminorm

\[
\|\mu\|_{A_X}
:=
\max_{f\in A_X}\langle \mu,f\rangle.
\tag{2}
\]

For another finite set `Y` with witness body `A_Y`, a Markov recovery kernel

\[
R:Y\rightsquigarrow X
\]

induces

\[
R_*:H_Y\to H_X,
\qquad
\nu\mapsto \nu R,
\tag{3}
\]

and the dual pullback

\[
R^*:H_X^*\to H_Y^*.
\tag{4}
\]

Define the **witness-transport coefficient**

\[
\kappa_{X\leftarrow Y}(R)
:=
\inf\left\{
\kappa\ge0:
R^*A_X\subseteq \kappa A_Y
\right\},
\tag{5}
\]

with value `+infinity` if no finite dilation works.

Then:

1. `\kappa` is exactly the induced operator seminorm:
   \[
   \boxed{
   \kappa_{X\leftarrow Y}(R)
   =
   \inf\left\{
   \kappa\ge0:
   \|\nu R\|_{A_X}
   \le
   \kappa\|\nu\|_{A_Y}
   \ \forall\nu\in H_Y
   \right\}.
   }
   \tag{6}
   \]
2. In finite dimensions, `\kappa_{X\leftarrow Y}(R)<\infty` if and only if the recovery respects the invisible quotient:
   \[
   \boxed{
   R_*\ker\|\cdot\|_{A_Y}
   \subseteq
   \ker\|\cdot\|_{A_X}.
   }
   \tag{7}
   \]
   Equivalently, `R_*` descends to a linear map
   \[
   H_Y/\ker\|\cdot\|_{A_Y}
   \longrightarrow
   H_X/\ker\|\cdot\|_{A_X}.
   \tag{8}
   \]
3. For compatible kernels
   \[
   T:Z\rightsquigarrow Y,
   \qquad
   R:Y\rightsquigarrow X,
   \]
   the coefficients compose submultiplicatively:
   \[
   \boxed{
   \kappa_{X\leftarrow Z}(TR)
   \le
   \kappa_{X\leftarrow Y}(R)
   \kappa_{Y\leftarrow Z}(T).
   }
   \tag{9}
   \]
4. Let experiments
   \[
   \mathcal A=(P_\theta)_\theta,
   \quad
   \mathcal B=(Q_\theta)_\theta,
   \quad
   \mathcal C=(S_\theta)_\theta
   \]
   live on `X,Y,Z`. For a recovery `R:Y\rightsquigarrow X`, define
   \[
   e_{\mathcal A\mid\mathcal B}(R)
   :=
   \max_\theta
   \|P_\theta-Q_\theta R\|_{A_X}.
   \tag{10}
   \]
   Then every compatible pair `R,T` obeys
   \[
   \boxed{
   e_{\mathcal A\mid\mathcal C}(TR)
   \le
   e_{\mathcal A\mid\mathcal B}(R)
   +
   \kappa_{X\leftarrow Y}(R)
   e_{\mathcal B\mid\mathcal C}(T).
   }
   \tag{11}
   \]
5. If `\mathcal R_{AB}^{\rm comp}` denotes the recoveries with finite coefficient, define the compatible recovery profile
   \[
   \Phi_{\mathcal A\mid\mathcal B}(t)
   :=
   \min_{R\in\mathcal R_{AB}^{\rm comp}}
   \left[
   e_{\mathcal A\mid\mathcal B}(R)
   +t\kappa_{X\leftarrow Y}(R)
   \right],
   \qquad t\ge0.
   \tag{12}
   \]
   The compatible recovery set is nonempty and compact, the minimum is attained, and the profile is finite, nondecreasing, concave, and continuous. Moreover
   \[
   \boxed{
   \Phi_{\mathcal A\mid\mathcal C}(t)
   \le
   \Phi_{\mathcal A\mid\mathcal B}
   \!\left(
   \Phi_{\mathcal B\mid\mathcal C}(t)
   \right).
   }
   \tag{13}
   \]

The intercept now has a load-bearing interpretation:

\[
\Phi_{\mathcal A\mid\mathcal B}(0)
=
\min_{R:\,\kappa(R)<\infty}
 e_{\mathcal A\mid\mathcal B}(R).
\tag{14}
\]

It need not equal the ordinary restricted recovery defect

\[
\delta_{A_X}(\mathcal A\mid\mathcal B)
:=
\min_R e_{\mathcal A\mid\mathcal B}(R).
\tag{15}
\]

Thus a representation can be exactly recoverable relative to its own stagewise witness class and still be unusable in a compositional pipeline because every exact inverse resurrects structure that the intermediate quotient had declared invisible.

## Derivation

### Dual witness inclusion is exactly the induced seminorm coefficient

For `\nu\in H_Y`,

\[
\begin{aligned}
\|\nu R\|_{A_X}
&=
\max_{f\in A_X}
\langle \nu R,f\rangle\\
&=
\max_{f\in A_X}
\langle \nu,R^*f\rangle\\
&=
 h_{R^*A_X}(\nu),
\end{aligned}
\tag{16}
\]

where `h_K` is the support function of a compact convex set `K`. Likewise

\[
\|\nu\|_{A_Y}=h_{A_Y}(\nu).
\tag{17}
\]

For compact convex sets containing the origin, support-function domination

\[
h_{R^*A_X}\le \kappa h_{A_Y}
\tag{18}
\]

is equivalent to the set inclusion

\[
R^*A_X\subseteq \kappa A_Y.
\tag{19}
\]

Equations `(16)`--`(19)` prove `(6)` and identify `(5)` as the exact category-specific contraction/expansion coefficient. No special metric structure is required.

### Finite coefficient is exactly quotient descent

Necessity of `(7)` is immediate. If

\[
\|\nu\|_{A_Y}=0
\]

and `(6)` holds with finite `\kappa`, then

\[
\|\nu R\|_{A_X}=0.
\tag{20}
\]

Conversely assume `(7)`. Then `R_*` induces a linear map between the quotient spaces in `(8)`. Each quotient carries the genuine norm induced by its original seminorm. The spaces are finite-dimensional, so every linear map between them is bounded. Hence a finite constant in `(6)` exists.

This is the exact obstruction hidden by stagewise restricted deficiency. A recovery may be perfectly valid as a stochastic inverse on the raw sample spaces while failing to define any map between the information quotients actually represented by the declared witness categories.

### Composition is ordinary operator-seminorm calculus after the quotient gate

For compatible `R` and `T`, take `\eta\in H_Z`. Then

\[
\|\eta T R\|_{A_X}
\le
\kappa_{X\leftarrow Y}(R)
\|\eta T\|_{A_Y}
\le
\kappa_{X\leftarrow Y}(R)
\kappa_{Y\leftarrow Z}(T)
\|\eta\|_{A_Z},
\tag{21}
\]

which proves `(9)`.

For the recovery error, decompose

\[
P_\theta-S_\theta T R
=
(P_\theta-Q_\theta R)
+
(Q_\theta-S_\theta T)R.
\tag{22}
\]

The triangle inequality for `\|\cdot\|_{A_X}` and `(6)` give

\[
\|P_\theta-S_\theta T R\|_{A_X}
\le
\|P_\theta-Q_\theta R\|_{A_X}
+
\kappa_{X\leftarrow Y}(R)
\|Q_\theta-S_\theta T\|_{A_Y}.
\tag{23}
\]

Taking the worst parameter gives `(11)`.

Compatibility is closed under composition by `(7)`, and constant-row recovery kernels always have coefficient `0` because they annihilate every zero-mass residual. Hence every compatible-recovery set is nonempty. The quotient-descent condition is a finite collection of linear conditions on the kernel, so it is closed inside the compact Markov-kernel polytope. On that closed set `\kappa` is the ordinary induced norm of a finite-dimensional quotient operator and is continuous. This gives attainment and the elementary profile properties in `(12)`.

Combining `(11)` and `(9)` exactly as in AF-132 gives `(13)`.

## Exact stagewise fidelity can fail to compose across incompatible quotients

The quotient gate is not a technical refinement. A three-state example gives

\[
\delta_{A_X}(\mathcal A\mid\mathcal B)=0,
\qquad
\delta_{A_Y}(\mathcal B\mid\mathcal C)=0,
\qquad
\delta_{A_X}(\mathcal A\mid\mathcal C)=\frac12.
\tag{24}
\]

Let

\[
X=\{0,1,2\}
\]

and give `H_X` the total-variation norm

\[
\|\mu\|_{A_X}=\frac12\|\mu\|_1.
\tag{25}
\]

Let

\[
Y=\{a,b,c\}
\]

and use the nontrivial but degenerate witness seminorm

\[
\|\nu\|_{A_Y}=|\nu(c)|.
\tag{26}
\]

This witness category sees how much zero-mass residual crosses between the block `{a,b}` and `c`, but it deliberately forgets redistribution inside `{a,b}`. In particular

\[
\|\delta_a-\delta_b\|_{A_Y}=0.
\tag{27}
\]

Take `Theta={0,1,2}` and

\[
P_0=\delta_0,
\quad
P_1=\delta_1,
\quad
P_2=\delta_2,
\tag{28}
\]

while

\[
Q_0=\delta_a,
\quad
Q_1=\delta_b,
\quad
Q_2=\delta_c.
\tag{29}
\]

The raw inverse

\[
R_a=\delta_0,
\qquad
R_b=\delta_1,
\qquad
R_c=\delta_2
\tag{30}
\]

recovers `\mathcal A` exactly, so the ordinary stagewise defect is zero. But `(27)` and

\[
\|R_a-R_b\|_{A_X}
=
\|\delta_0-\delta_1\|_{TV}
=1
\tag{31}
\]

show that this inverse has infinite witness-transport coefficient.

Every compatible recovery must satisfy

\[
R_a=R_b,
\tag{32}
\]

because total variation has no nonzero blind directions. Therefore

\[
1
=
\|\delta_0-\delta_1\|_{TV}
\le
\|\delta_0-R_a\|_{TV}
+
\|R_b-\delta_1\|_{TV},
\tag{33}
\]

so every compatible recovery has worst error at least `1/2`. Equality is obtained by

\[
R_a=R_b=\frac12(\delta_0+\delta_1),
\qquad
R_c=\delta_2.
\tag{34}
\]

Hence

\[
\Phi_{\mathcal A\mid\mathcal B}(0)=\frac12
\quad\text{while}\quad
\delta_{A_X}(\mathcal A\mid\mathcal B)=0.
\tag{35}
\]

Now let

\[
Z=\{u,v\}
\]

with total-variation witness geometry, and define the final experiment

\[
S_0=S_1=\delta_u,
\qquad
S_2=\delta_v.
\tag{36}
\]

Recover `Y` by

\[
T_u=\delta_a,
\qquad
T_v=\delta_c.
\tag{37}
\]

For parameter `1`, the only residual is `\delta_b-\delta_a`, which is invisible under `(26)`. Therefore

\[
e_{\mathcal B\mid\mathcal C}(T)=0,
\tag{38}
\]

and `T` is compatible because the source witness seminorm on `Z` is a norm. Thus the second stage also has exact restricted fidelity.

But `S_0=S_1`, so direct recovery of `P_0=\delta_0` and `P_1=\delta_1` from the same final observation has minimum worst total-variation error `1/2`. This proves `(24)`.

The failure is exact: the intermediate category declared `a` versus `b` irrelevant, while the first inverse needed precisely that distinction to reconstruct `0` versus `1`. The two zero-defect statements therefore refer to incompatible quotients and cannot be chained.

## Relationship to AF-129--AF-132

AF-129 identifies the blind quotient created by a restricted symmetric witness body. AF-133 adds the missing cross-stage rule: **a recovery is compositional only when it descends through that quotient.** The finite coefficient `(5)` is the exact certificate of this descent.

AF-130's metric-local witness body has no blind directions on a genuine finite metric space, so the quotient gate is automatic there. AF-131 then identifies the remaining quantitative obstruction: the finite coefficient need not be at most one and is exactly the Wasserstein Lipschitz coefficient. AF-132 packages reconstruction error and that coefficient into a compositional profile.

Thus the hierarchy is now sharper:

\[
\text{restricted witness category}
\;\Longrightarrow\;
\text{invisible quotient}
\;\Longrightarrow\;
\text{quotient-compatible recovery}
\;\Longrightarrow\;
\text{finite expansion coefficient}
\;\Longrightarrow\;
\text{error/regularity profile}.
\tag{39}
\]

Total variation is the special case in which the witness seminorm is a norm and every Markov kernel is universally nonexpansive. Wasserstein is the special case in which the witness seminorm is again a norm but the expansion coefficient depends on metric regularity. A genuinely degenerate restricted class adds an earlier categorical obstruction: some stochastic inverses have infinite coefficient because they do not define maps on the retained information quotient at all.

For Arithmetic Fidelity this matters whenever successive compressions are audited using different admissible observables. A claim that each stage is individually faithful is insufficient. The retained quotient at one stage must be compatible with the inverse needed by the preceding stage, or later analysis may silently discard a distinction that an earlier reconstruction depended on.

## Prior art and novelty assessment

The ingredients are classical and no novelty claim is made for the functional-analytic theorem.

- Alfred Müller, **“Integral Probability Metrics and Their Generating Classes of Functions,”** *Advances in Applied Probability* 29(2), 429--443 (1997), DOI `10.2307/1428011`. Role: classical generating-function description of integral probability metrics; equations `(2)` and `(16)` are finite symmetric IPM/support-function geometry.
- Stéphane Gaubert and Zheng Qu, **“Dobrushin's Ergodicity Coefficient for Markov Operators on Cones,”** *Integral Equations and Operator Theory* 81, 127--150 (2015), DOI `10.1007/s00020-014-2193-2`. Role: general contraction coefficients for Markov operators and their dual seminorm descriptions; places `(5)`--`(9)` inside established ergodicity-coefficient/operator-seminorm theory.
- Giulia De Pasquale, Kevin D. Smith, Francesco Bullo, and Maria Elena Valcher, **“Dual Seminorms, Ergodic Coefficients and Semicontraction Theory,”** *IEEE Transactions on Automatic Control* 69(5), 3040--3053 (2024), DOI `10.1109/TAC.2023.3302788`. Role: modern explicit treatment of induced matrix seminorms, their kernels/quotients, and dual contraction coefficients.
- Erik Torgersen, ***Comparison of Statistical Experiments***, Cambridge University Press (1991), Chapter 6, DOI `10.1017/CBO9780511666353.007`. Role: authoritative deficiency and restricted-decision framework behind AF-126--AF-129.

The derived Arithmetic Fidelity value is the explicit alignment of these classical pieces with the line's staged-compression question. AF-129's witness quotient and AF-132's recovery profile are not separate phenomena: the profile calculus is well-defined across categories only after the recovery respects the invisible quotient. The exact three-stage counterexample makes that compatibility requirement falsifiable rather than rhetorical.

The next useful question is therefore category-specific rather than another abstract scalarization: for a natural admissible witness family, characterize which Markov recoveries satisfy

\[
R^*A_X\subseteq \kappa A_Y
\]

with small finite `\kappa`, and determine whether the resulting quotient-compatible recovery class is rich enough to retain the discriminator of interest.