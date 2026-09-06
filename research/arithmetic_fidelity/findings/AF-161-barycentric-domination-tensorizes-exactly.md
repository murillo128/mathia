# AF-161 — Barycentric domination tensorizes into an exact local-to-global recovery-complexity budget

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `QUANTITATIVE-FIDELITY`, `COMPOSITION-LAW`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-159 identifies the barycentric domination radius

\[
\Lambda_{\rm bar}(\mathcal E)
\]

as the likelihood-complexity factor that makes a propagated barycentric Pearson loss quantitatively comparable with **optimal** common recovery. AF-160 then rewrites that radius as a finite maximin game on Shtarkov likelihood rays and separates it into unrestricted Shtarkov complexity and a convex-hull penalty.

For independent product experiments, all three quantities tensorize **exactly**. This gives a sharp composition law and exposes a strong limitation of the full-family calibration route.

Let

\[
\mathcal E=(P_i)_{i\in I}
\quad\text{on }X,
\qquad
\mathcal F=(Q_j)_{j\in J}
\quad\text{on }Y
\]

be finite statistical experiments. Their full Cartesian product experiment is

\[
\mathcal E\otimes\mathcal F
:=
(P_i\otimes Q_j)_{(i,j)\in I\times J}
\quad\text{on }X\times Y.
\tag{1}
\]

Write

\[
s_{\mathcal E}(x)=\max_iP_i(x),
\qquad
C(\mathcal E)=\sum_xs_{\mathcal E}(x),
\tag{2}
\]

and likewise for `F`, and let

\[
G_{\rm hull}(\mathcal E)
:=
\frac{\Lambda_{\rm bar}(\mathcal E)}{C(\mathcal E)}
=
\exp d_{\rm hull}(\mathcal E)
\tag{3}
\]

be AF-160's multiplicative convex-hull penalty. Then

\[
\boxed{
C(\mathcal E\otimes\mathcal F)
=
C(\mathcal E)C(\mathcal F),
}
\tag{4}
\]

\[
\boxed{
\Lambda_{\rm bar}(\mathcal E\otimes\mathcal F)
=
\Lambda_{\rm bar}(\mathcal E)\Lambda_{\rm bar}(\mathcal F),
}
\tag{5}
\]

and therefore

\[
\boxed{
G_{\rm hull}(\mathcal E\otimes\mathcal F)
=
G_{\rm hull}(\mathcal E)G_{\rm hull}(\mathcal F),
\qquad
 d_{\rm hull}(\mathcal E\otimes\mathcal F)
=
 d_{\rm hull}(\mathcal E)+d_{\rm hull}(\mathcal F).
}
\tag{6}
\]

The result is stronger than observing that product barycentric references give an upper bound. The convex hull of the product experiment allows **arbitrary correlated mixtures** of the pairs `(i,j)`. Equation `(5)` says such correlations cannot beat the product of the optimal one-factor barycentric domination radii.

For a finite sequence of product factors,

\[
\mathcal E^{(1)}\otimes\cdots\otimes\mathcal E^{(n)},
\]

one gets

\[
\boxed{
\log\Lambda_{\rm bar}
=
\sum_{k=1}^n\log\Lambda_{\rm bar}(\mathcal E^{(k)}),
\quad
\log C
=
\sum_{k=1}^n\log C(\mathcal E^{(k)}),
\quad
 d_{\rm hull}
=
\sum_{k=1}^n d_{\rm hull}(\mathcal E^{(k)}).
}
\tag{7}
\]

Thus AF-160's source complexity has an exact **local-to-global additive budget after taking logarithms**.

The decisive obstruction is the tensor-power case. If `E` is nontrivial, meaning that at least two of its member laws are distinct, then

\[
\Lambda_{\rm bar}(\mathcal E)>1.
\tag{8}
\]

Hence

\[
\boxed{
\Lambda_{\rm bar}(\mathcal E^{\otimes n})
=
\Lambda_{\rm bar}(\mathcal E)^n
\longrightarrow\infty
}
\tag{9}
\]

exponentially. In particular, the uniform bounded-likelihood-complexity hypothesis used in AF-159 cannot hold for growing full Cartesian tensor powers of any nontrivial finite experiment.

This does **not** say that approximate recovery itself becomes impossible, nor that every destination-relative fidelity metric must deteriorate exponentially. It says something narrower and exact: AF-159's route from a single barycentric-reference Pearson defect to an `n`-independent two-sided modulus for **optimal recovery of the whole product family** cannot retain a uniformly bounded source constant under repeated nontrivial independent products. A scalable arithmetic application therefore needs at least one of the following to change: the recovered family, the destination witness class, the loss, or the product structure being modeled.

## Derivation

### Shtarkov envelopes and centers factor pointwise

For nonnegative product probabilities,

\[
\begin{aligned}
s_{\mathcal E\otimes\mathcal F}(x,y)
&=
\max_{i,j}P_i(x)Q_j(y)\\
&=
\left(\max_iP_i(x)\right)
\left(\max_jQ_j(y)\right)\\
&=
s_{\mathcal E}(x)s_{\mathcal F}(y).
\end{aligned}
\tag{10}
\]

Summing over `X x Y` proves `(4)`. Consequently the normalized Shtarkov/NML reference factorizes as well:

\[
M_{\rm Sh}^{\mathcal E\otimes\mathcal F}
=
M_{\rm Sh}^{\mathcal E}\otimes M_{\rm Sh}^{\mathcal F}.
\tag{11}
\]

This is the elementary product form of the classical Shtarkov/NML construction.

Define AF-160's max-normalized likelihood rays

\[
U_i(x)=\frac{P_i(x)}{s_{\mathcal E}(x)},
\qquad
V_j(y)=\frac{Q_j(y)}{s_{\mathcal F}(y)}
\tag{12}
\]

on their positive envelope supports. Equation `(10)` gives

\[
U_{ij}(x,y)
=
U_i(x)V_j(y).
\tag{13}
\]

Thus the finite game controlling barycentric domination is itself a nonnegative tensor-product game.

### The maximin value tensorizes despite correlated mixtures

AF-160 gives

\[
v(\mathcal E)
:=
\frac1{\Lambda_{\rm bar}(\mathcal E)}
=
\max_{\pi\in\Delta_I}
\min_x
\sum_i\pi_iU_i(x)
=
\min_{\nu\in\Delta(X_s)}
\max_i
\sum_x\nu(x)U_i(x).
\tag{14}
\]

Define `v(F)` analogously. Because the spaces are finite, optimal mixed strategies exist.

Choose optimal row strategies `pi_*` for `E` and `sigma_*` for `F`. Their product is an admissible — though not necessarily uniquely optimal — mixture over the full pair index set. For every `(x,y)`,

\[
\begin{aligned}
\sum_{i,j}\pi_*(i)\sigma_*(j)U_i(x)V_j(y)
&=
\left(\sum_i\pi_*(i)U_i(x)\right)
\left(\sum_j\sigma_*(j)V_j(y)\right)\\
&\ge
v(\mathcal E)v(\mathcal F).
\end{aligned}
\tag{15}
\]

Therefore

\[
v(\mathcal E\otimes\mathcal F)
\ge
v(\mathcal E)v(\mathcal F).
\tag{16}
\]

For the reverse inequality, choose optimal dual point strategies `nu_*` and `mu_*` in `(14)`. Under their product distribution, every pure pair `(i,j)` has expected payoff

\[
\begin{aligned}
\mathbb E_{\nu_*\otimes\mu_*}[U_i(X)V_j(Y)]
&=
\mathbb E_{\nu_*}U_i(X)\,
\mathbb E_{\mu_*}V_j(Y)\\
&\le
v(\mathcal E)v(\mathcal F),
\end{aligned}
\tag{17}
\]

because the dual optimality conditions give

\[
\mathbb E_{\nu_*}U_i\le v(\mathcal E)
\quad\forall i,
\qquad
\mathbb E_{\mu_*}V_j\le v(\mathcal F)
\quad\forall j.
\]

The entries are nonnegative, so multiplication preserves these inequalities. Equation `(17)` supplies an admissible dual strategy proving

\[
v(\mathcal E\otimes\mathcal F)
\le
v(\mathcal E)v(\mathcal F).
\tag{18}
\]

Combining `(16)` and `(18)` gives

\[
\boxed{
v(\mathcal E\otimes\mathcal F)
=
v(\mathcal E)v(\mathcal F),
}
\tag{19}
\]

and inversion proves `(5)`.

The proof is important for the interpretation. Merely taking a product of optimal barycentric references would prove only

\[
\Lambda_{\rm bar}(\mathcal E\otimes\mathcal F)
\le
\Lambda_{\rm bar}(\mathcal E)\Lambda_{\rm bar}(\mathcal F).
\]

The dual product strategy proves that **no correlated barycentric mixture over `(i,j)` lowers the radius further**.

### The convex-hull mismatch is additive in logarithmic scale

Divide `(5)` by `(4)` to obtain the first identity in `(6)`. Since every `G_hull>=1`, taking logarithms gives the additive directed-hull mismatch.

Equivalently, AF-160's decomposition

\[
\Lambda_{\rm bar}=C e^{d_{\rm hull}}
\tag{20}
\]

separates into two independently additive logarithmic source costs under Cartesian products:

\[
\log\Lambda_{\rm bar}
=
\log C+d_{\rm hull}.
\tag{21}
\]

The first is the unrestricted Shtarkov/NML envelope complexity; the second is the extra cost of requiring the reference to lie in the experiment convex hull so that whole-family recovery automatically recovers the reference.

### Nontrivial tensor powers necessarily leave the uniformly bounded regime

For every experiment,

\[
\Lambda_{\rm bar}\ge1.
\]

If equality holds, some barycentric probability law `M` satisfies

\[
s(x)\le M(x)\qquad\forall x.
\tag{22}
\]

Since every member `P_i<=s` pointwise and both `P_i` and `M` have total mass one, `(22)` forces `s=M=P_i` for every `i`. Thus

\[
\boxed{
\Lambda_{\rm bar}(\mathcal E)=1
\iff
P_i=P_{i'}\text{ for all }i,i'.
}
\tag{23}
\]

Any genuinely discriminating finite experiment therefore has `Lambda_bar>1`, and `(9)` follows from `(5)` by induction.

For nonidentical factors, `(7)` gives the exact boundedness criterion

\[
\sup_n
\Lambda_{\rm bar}
\left(\bigotimes_{k=1}^n\mathcal E^{(k)}\right)
<\infty
\iff
\sum_{k=1}^\infty
\log\Lambda_{\rm bar}(\mathcal E^{(k)})
<\infty.
\tag{24}
\]

Likewise the extra convex-hull penalty stays uniformly bounded exactly when

\[
\sum_k d_{\rm hull}(\mathcal E^{(k)})<\infty.
\tag{25}
\]

These are exact complexity budgets, not asymptotic estimates.

## Exact arithmetic/analytic stress test: tensor powers of the local `p=2` Euler-factor family

AF-157--AF-159 use a two-member family derived from one rational-prime Euler factor. On exponent states `k=1,2,3`,

\[
P_1=\left(\frac47,\frac27,\frac17\right),
\qquad
P_2=\left(\frac{16}{21},\frac4{21},\frac1{21}\right).
\tag{26}
\]

AF-157 computes its Shtarkov envelope and mass as

\[
s=\left(\frac{16}{21},\frac27,\frac17\right),
\qquad
C=\frac{25}{21},
\tag{27}
\]

while AF-159 computes

\[
\Lambda_{\rm bar}=\frac{11}{9}.
\tag{28}
\]

Therefore AF-160's convex-hull penalty is exactly

\[
G_{\rm hull}
=
\frac{11/9}{25/21}
=
\frac{77}{75}.
\tag{29}
\]

For the declared **Cartesian tensor power** of this arithmetic-derived finite experiment, AF-161 gives

\[
\boxed{
C_n=\left(\frac{25}{21}\right)^n,
\qquad
\Lambda_{{\rm bar},n}
=\left(\frac{11}{9}\right)^n,
\qquad
G_{{\rm hull},n}
=\left(\frac{77}{75}\right)^n.
}
\tag{30}
\]

Two different multiplicative effects are visible. Even the modest local hull mismatch `77/75` accumulates exponentially. More fundamentally, the total barycentric domination radius grows as `(11/9)^n`, so AF-159's bounded-`Lambda_bar` sufficient condition for uniform two-sided Pearson/optimal-recovery calibration fails under repeated independent copies.

This is a genuine arithmetic/analytic stress test of the abstract theorem because the one-factor laws come from the local Euler-factor construction already audited in this line. It is **not** a claim that the global rational-prime Euler product is this tensor power. Distinct rational primes, multiplicative constraints, the target analytic observable, and the global arithmetic family may define a diagonal, dependent, quotient, or otherwise much smaller source class. Equation `(30)` says exactly what happens only when the admitted family contains the full independent Cartesian product.

That boundary is itself informative: before importing AF-159 as a scalable local-to-global recovery theorem, an arithmetic application must specify whether its admissible alternatives really multiply independently. If they do, full-family recovery pays the exact product complexity above. If they do not, the structure that forbids arbitrary combinations is part of the surviving arithmetic provenance and must be retained explicitly rather than discarded as irrelevant labeling.

## Prior-art and novelty audit

The ingredients are classical.

- Yu. M. Shtarkov, **“Universal Sequential Coding of Single Messages,”** *Problems of Information Transmission* 23(3), 175–186 in the English translation (1987), introduced the normalized maximum-likelihood/Shtarkov minimax-regret construction. Product factorization of `(10)` is immediate from the pointwise envelope definition; no novelty is claimed for NML product complexity itself.
- John von Neumann, **“Zur Theorie der Gesellschaftsspiele,”** *Mathematische Annalen* 100, 295–320 (1928), DOI `10.1007/BF01448847`, is the classical finite minimax source underlying AF-160's game dual and the two product-strategy bounds `(15)--(18)`.
- Ibrahim Issa, Aaron B. Wagner, and Sudeep Kamath, **“An Operational Approach to Information Leakage,”** *IEEE Transactions on Information Theory* 66(3), 1625–1657 (2020), DOI `10.1109/TIT.2019.2962804`, identify maximal leakage with order-infinity Sibson information and establish additivity over independent pairs. This is close prior art for the additive `log C` / unrestricted-envelope side of `(21)`.

A targeted search did not identify a source that states AF-160's **convex-hull-restricted barycentric domination radius** and its exact tensorization in this notation. That is not a novelty claim: `(5)` is an elementary consequence of AF-160's finite minimax representation plus product strategies, and closely related multiplicativity facts may exist in matrix-game, fractional-covering, universal-coding, or information-radius language.

The durable contribution here is the **fidelity boundary** obtained by combining those classical ingredients with AF-159/AF-160: the source complexity required by the barycentric Pearson-to-optimal-recovery calibration has an exact multiplicative composition law, and therefore escapes every uniform bound under nontrivial full Cartesian tensor powers.

## Boundaries and counterarguments

1. **Full Cartesian family is essential.** If the admissible pair indices form only a diagonal or constrained subset of `I x J`, the envelope need not factor as `(10)` and the game need not be a tensor product. Equation `(5)` must not be transferred to correlated or arithmetic-constrained families without rederivation.

2. **This is a calibration obstruction, not an impossibility of recovery.** Divergence of `Lambda_bar` shows that AF-159's source-only continuity constant cannot remain uniformly bounded. It does not lower-bound the actual recovery deficiency and does not rule out another destination-relative metric with better scaling.

3. **The product barycentric optimizer need not be unique.** Product optimal strategies always attain the product value, but correlated optimal mixtures may coexist. The theorem classifies the value, not the complete optimizer set.

4. **Hull mismatch and total complexity are different.** `G_hull=1` means the Shtarkov center is barycentric, but a nontrivial experiment still has `C=Lambda_bar>1`. Eliminating the convex-hull penalty alone therefore does not make whole-family tensor-power calibration uniformly bounded.

5. **No RH consequence is established.** The arithmetic stress test is finite and local. Any use for rational primes must first identify the actual product/constrained-family structure and the downstream witness or decision class that needs recovery.

## Consequence for the line

AF-159's live question was whether one could control barycentric likelihood complexity for arithmetic source families. AF-161 gives a decisive negative answer for one broad compositional regime: **uniform control is impossible for repeated full independent products of any nontrivial finite source experiment**, because the exact optimal radius tensorizes.

This redirects the scalable problem away from searching for a globally bounded whole-family barycentric reference in product-like models. A viable local-to-global application must instead exploit genuine arithmetic dependence or restrict the destination requirement — for example to a target-relative witness family whose effective complexity does not contain every independent local alternative.

The key new test for an arithmetic compression is therefore not merely whether each local factor has a small fidelity defect. It is whether the downstream target consumes the full Cartesian product experiment or only a structurally constrained quotient of it. That distinction determines whether local information-loss certificates compose with a finite global budget or accumulate exponentially.