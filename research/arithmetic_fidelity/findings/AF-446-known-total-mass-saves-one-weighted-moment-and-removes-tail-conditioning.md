# AF-446 — Known total mass saves one weighted moment and removes the lost-boundary factor

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `MASS-CONSTRAINED-MOMENT-THRESHOLD`, `TARGET-PURE-FIBER`, `UNSHIFTED-HANKEL-CERTIFICATE`, `UNIFORM-TAIL-SEPARATION`, `CLASSICAL-TRUNCATED-MOMENT/PRONY`, `NO-NOVELTY-CLAIM`

## Claim

AF-445 shows that when both support locations and positive weights are unknown, a `K`-atomic nuisance source can hide one additional positive atom from the first `2K` **positive** moments, while moment `2K+1` supplies the first global shifted-Hankel certificate. A single source law changes that threshold sharply.

Let

\[
\mu=\sum_{i=1}^r a_i\delta_{x_i},
\qquad a_i>0,\quad x_i>0,
\]

and write

\[
m_n(\mu)=\int t^n\,d\mu(t)=\sum_i a_i x_i^n,
\qquad n\ge0.
\]

Fix a total mass `M>0` and restrict every admissible source to

\[
m_0(\mu)=M.
\tag{1}
\]

The scalar `M` is a source constraint known independently of the retained positive moments; it is not a target label.

Fix `K>=1`.

### Positive side: `2K` positive moments now suffice globally

If `\mu` has at most `K` distinct positive support points, `\nu` has exactly `K+1` distinct positive support points, and

\[
m_0(\mu)=m_0(\nu)=M,
\]

then

\[
\boxed{
(m_1(\mu),\ldots,m_{2K}(\mu))
\ne
(m_1(\nu),\ldots,m_{2K}(\nu)).
}
\tag{2}
\]

The separating invariant is the **unshifted** Hankel determinant

\[
\Delta_K(m)
:=
\det [m_{i+j}]_{i,j=0}^{K}.
\tag{3}
\]

Because `m_0=M` is already supplied by the source law, `(3)` is a polynomial function of only the retained positive moments `m_1,...,m_{2K}`. It vanishes on every source with at most `K` atoms and is strictly positive on every positive `(K+1)`-atomic source with distinct support.

### Negative side: `2K-1` positive moments can still fail

Let

\[
\mu_0=\sum_{i=1}^{K}a_i^0\delta_{x_i^0}
\]

have distinct positive supports, positive weights, and total mass `M`. Fix any target location `y>0` different from the `x_i^0`. Then there is `\varepsilon>0` such that for every target weight

\[
0<c<\varepsilon
\]

there exists another positive `K`-atomic measure

\[
\widetilde\mu_c
=
\sum_{i=1}^{K}\widetilde a_i(c)\delta_{\widetilde x_i(c)}
\]

with supports and weights arbitrarily close to those of `\mu_0` and satisfying

\[
\boxed{
m_n(\mu_0)
=
m_n(\widetilde\mu_c+c\delta_y),
\qquad n=0,1,\ldots,2K-1.
}
\tag{4}
\]

In particular both sides of `(4)` have total mass `M`, while the first `2K-1` positive moments are identical even though the second source has the additional distinct atom at `y`. Moreover, for fixed `y`,

\[
\max_i\left(
|\widetilde a_i(c)-a_i^0|
+
|\widetilde x_i(c)-x_i^0|
\right)=O(c).
\tag{5}
\]

Thus on the positive weighted atomic class with known total mass the worst-case threshold is sharp:

\[
\boxed{
2K-1\text{ positive moments can fail,}
\qquad
2K\text{ positive moments always separate.}
}
\tag{6}
\]

Relative to AF-445, the conserved scalar `m_0=M` saves exactly one transmitted positive moment.

## Local collision below the threshold

Parameterize a labeled `K`-atomic measure by

\[
\theta=(a_1,\ldots,a_K,x_1,\ldots,x_K)
\]

inside the open set where every weight is positive and the support points are positive and distinct. Consider the full prefix map

\[
F(\theta)
=
(m_0,m_1,\ldots,m_{2K-1})
\in\mathbb R^{2K}.
\tag{7}
\]

Its Jacobian columns are

\[
\frac{\partial m_n}{\partial a_i}=x_i^n,
\qquad
\frac{\partial m_n}{\partial x_i}=n a_i x_i^{n-1},
\qquad n=0,\ldots,2K-1.
\tag{8}
\]

This square Jacobian is nonsingular whenever the support points are distinct and the weights are nonzero. Indeed, suppose a row vector `\lambda=(\lambda_0,\ldots,\lambda_{2K-1})` annihilates all columns and set

\[
P(t)=\sum_{n=0}^{2K-1}\lambda_n t^n.
\]

The weight columns give `P(x_i)=0`, while the support columns give `a_iP'(x_i)=0`, hence `P'(x_i)=0`. Every `x_i` is therefore a double root of `P`. A nonzero polynomial of degree at most `2K-1` cannot have `K` distinct double roots, so `P\equiv0`. Hence the Jacobian is invertible.

The inverse-function theorem gives a neighborhood of `F(\theta_0)` filled by nearby `K`-atomic sources. The target atom contributes

\[
c(1,y,y^2,\ldots,y^{2K-1}).
\tag{9}
\]

For fixed `y` this vector tends to zero with `c`. Therefore, for sufficiently small `c`, there is a unique nearby parameter vector `\widetilde\theta(c)` with

\[
F(\widetilde\theta(c))
=
F(\theta_0)
-
c(1,y,\ldots,y^{2K-1}).
\tag{10}
\]

Adding `c\delta_y` gives `(4)`. Shrinking the parameter neighborhood preserves positivity and support distinctness and keeps the nuisance supports away from the fixed target point. Differentiability of the local inverse gives `(5)`.

The zeroth coordinate in `(9)` is decisive. Under the mass constraint, inserting target mass `c` forces the nuisance source to surrender the same amount of mass somewhere else. The target perturbation is therefore not allowed to disappear merely because `y` approaches zero.

## Unshifted Hankel rank gives the global certificate

Given `m_0=M` and the positive moments through order `2K`, form

\[
H_K(\mu)
=
[m_{i+j}(\mu)]_{i,j=0}^{K}.
\tag{11}
\]

For

\[
\mu=\sum_{j=1}^{r}a_j\delta_{x_j}
\]

let

\[
V_{ij}=x_j^i,
\qquad 0\le i\le K.
\]

Then

\[
\boxed{
H_K(\mu)=V\,\operatorname{diag}(a_1,\ldots,a_r)\,V^T.
}
\tag{12}
\]

If `r<=K`, the rank is at most `K`, hence

\[
\Delta_K(\mu)=0.
\tag{13}
\]

If `r=K+1`, the support points are distinct, and every weight is positive, then `V` is an invertible square Vandermonde matrix and

\[
\boxed{
\Delta_K(\mu)
=
\left(\prod_{j=1}^{K+1}a_j\right)
\left(\prod_{1\le i<j\le K+1}(x_j-x_i)^2\right)
>0.
}
\tag{14}
\]

Equations `(13)` and `(14)` prove `(2)` globally. No local regularity, ordering, or reconstruction algorithm is needed.

This is the same finite-atomic rank mechanism that appears in classical truncated moment and Prony theory, but the source-law comparison with AF-445 is exact. Without `m_0`, the first available `(K+1)x(K+1)` Hankel certificate must be shifted and therefore reaches through `m_{2K+1}`. Once total mass is known, the unshifted certificate is available one order earlier and reaches only through `m_{2K}`.

## The conserved scalar also changes conditioning

The difference between shifted and unshifted Hankel certificates is not only one observation count. It changes which boundary controls the separation margin.

Consider a compact target-present class

\[
\nu
=
\sum_{i=1}^{K} b_i\delta_{z_i}
+c\delta_y
\tag{15}
\]

with total mass `M`, where the nuisance supports lie in pairwise separated compact cells inside

\[
[\alpha,\beta]\Subset(0,\infty),
\]

all nuisance weights are bounded below by `w_->0`, the target weight satisfies `c>=c_->0`, and

\[
0<y\le y_0<\alpha/2.
\]

Equation `(14)` becomes

\[
\Delta_K(\nu)
=
c
\left(\prod_{i=1}^{K}b_i\right)
\left(\prod_{1\le i<j\le K}(z_j-z_i)^2\right)
\left(\prod_{i=1}^{K}(z_i-y)^2\right).
\tag{16}
\]

Every factor in `(16)` is bounded uniformly away from zero on the declared class. In particular there is **no multiplicative factor `y`**. Hence

\[
\Delta_K(\nu)\ge A>0
\tag{17}
\]

uniformly as `y\downarrow0`.

On the corresponding at-most-`K`-atomic mass-`M` class, `\Delta_K` is identically zero. Since `m_0=M` is fixed, `\Delta_K` is a polynomial in the retained vector `(m_1,\ldots,m_{2K})`. Its gradient is bounded on any compact convex set containing the two observation classes and their joining segments. The mean-value inequality therefore gives

\[
\operatorname{dist}
\bigl(T_{2K}(\mathcal C_{\le K}),
T_{2K}(\mathcal C_{K+1}(y))\bigr)
\ge A/L>0
\tag{18}
\]

with a constant independent of small `y`. Compactness supplies a finite upper bound, so for a nonempty compact family satisfying the stated uniform hypotheses the class separation is

\[
\boxed{\Theta(1)\quad\text{as }y\downarrow0.}
\tag{19}
\]

This contrasts directly with AF-445. There the shifted determinant contains the factor `c y`, so after exact fidelity is restored its class margin still collapses linearly in the disappearing support coordinate. Here the known mass activates the unshifted determinant, and a fixed positive target weight remains visible even when its support moves toward the positive-moment blind boundary `y=0`.

The mechanism is relational rather than magical recovery of the lost coordinate: conservation of total mass couples appearance of the target atom to a compensating mass change in the rest of the source. The positive-moment observation can detect that coupled redistribution even when the target atom's own positive powers become tiny.

If the target weight `c` is allowed to tend to zero, `(16)` shows that the determinant certificate again weakens proportionally to `c` under the same compact support assumptions. Thus the conserved source law transfers the relevant conditioning parameter from the target **location** to the target **mass**.

## A one-atom sanity check

For `K=1`, a fixed-mass one-atomic source is `M\delta_x`. Its first moment alone does not distinguish it from every two-atomic probability/mass distribution with the same weighted mean. This is the `2K-1=1` collision side.

With the second moment retained, however,

\[
\Delta_1
=
\det\begin{bmatrix}M&m_1\\m_1&m_2\end{bmatrix}
=
Mm_2-m_1^2.
\]

It vanishes for a one-point source and is strictly positive for any positive two-point source with distinct locations. This is exactly the usual zero-versus-positive variance distinction, and it is the `K=1` instance of `(14)`.

## Prior-art and novelty audit

The mathematical core is classical moment theory. Konrad Schmüdgen, *The Moment Problem*, Graduate Texts in Mathematics 277, Springer (2017), DOI `10.1007/978-3-319-64546-9`, treats the one-dimensional truncated Hamburger and Stieltjes moment problems in Chapters 9–10 and Hankel/moment-matrix methods more generally. The factorization `(12)` and rank/cardinality relation are standard finite-atomic moment facts.

Raul E. Curto and Lawrence A. Fialkow, **“Flat Extensions of Positive Moment Matrices: Recursively Generated Relations,”** *Memoirs of the American Mathematical Society* 136(648) (1998), DOI `10.1090/memo/0648`, develop the finite-rank/flat-extension theory of positive moment matrices and minimal finitely atomic representing measures. Their framework is substantially more general than the elementary one-dimensional determinant argument used here.

Gerlind Plonka and Manfred Tasche, **“Prony Methods for Recovery of Structured Functions,”** *GAMM-Mitteilungen* 37(2), 239–258 (2014), DOI `10.1002/gamm.201410011`, surveys classical Prony recovery and its Hankel/annihilating-polynomial structure for finitely supported exponential or atomic data.

No novelty is claimed for finite-atomic Hankel factorization, moment-matrix rank, Vandermonde determinants, Prony reconstruction, the inverse-function theorem, or the fact that normalized probability measures have known zeroth moment.

The Arithmetic Fidelity contribution recorded here is the source-law comparison required by the frontier after AF-445: **one conserved scalar reduces the worst-case positive-moment fidelity threshold by exactly one and changes the disappearing-target conditioning law because it changes which Hankel minor is computable from the compressed representation.** This is a concrete example where a source constraint does more than reduce a parameter count; it supplies the missing algebraic certificate that turns rank surplus into global target purity.

## Boundaries and falsification checks

- The source law must supply the exact common total mass `m_0=M`. If total mass is unknown or may differ between the compared sources, the unshifted determinant cannot be evaluated from `(m_1,...,m_{2K})` alone, and AF-445's shifted threshold applies instead.
- The positive theorem distinguishes at most `K` atoms from exactly `K+1` **distinct** positive atoms with positive weights. Coalescing supports reduces effective cardinality and correctly makes the Vandermonde factor vanish.
- The negative theorem uses arbitrarily small positive target weight `c`. It proves sharpness in the worst case over the full positive-weight source class; it does not claim that `2K-1` moments fail for every prescribed lower bound on target mass.
- The target location in the local collision must be distinct from the base nuisance supports. This allows the nearby nuisance supports to remain separated from it.
- The uniform tail-margin statement requires nuisance supports and weights to remain in a compact nondegenerate region and the target weight to stay bounded away from zero. If nuisance weights vanish, nuisance supports collide, or `c\to0`, the determinant margin can collapse.
- Equation `(19)` concerns Euclidean separation of the declared finite observation classes, not an optimal statistical decoder or a noise model.
- The theorem uses a consecutive positive-moment prefix. Other measurement families may admit different certificates and thresholds.
- Knowing `M` is legitimate only when mass conservation is intrinsic to the source category. Adding `m_0` solely because it encodes the desired target would be a target-identity smuggling violation of the line mandate.
- Nothing here distinguishes rational primes, constrains the Riemann zero divisor, or implies RH.

A direct falsification of the positive half would require a mass-`M` measure with at most `K` atoms and a mass-`M` measure with `K+1` distinct positive atoms sharing moments through order `2K`; their common unshifted Hankel matrix would then have determinant both zero by rank and strictly positive by `(14)`. A falsification of the local negative half would require failure of local reachability despite the confluent Vandermonde Jacobian `(8)` being nonsingular.

## Consequence for the research line

AF-444 and AF-445 showed that the first globally separating moment arrives one observation beyond the locally programmable nuisance dimension, provided an algebraic source law supplies a certificate. This finding gives the first nontrivial comparison **between source laws**:

- unit weights: `K` nuisance parameters and threshold `K+1` positive moments;
- unknown positive weights: `2K` nuisance parameters and threshold `2K+1` positive moments;
- unknown positive weights with conserved total mass: `2K-1` effective nuisance parameters and threshold `2K` positive moments.

The third case also shows that constraint value cannot be judged from dimension reduction alone. The conserved scalar changes the certificate from shifted to unshifted Hankel rank and thereby removes the extra lost-boundary factor `y` from the separation margin.

The next useful source-law question is therefore whether other constraints listed by the live frontier—coupled/repeated weights, multiplicative relations, finite-alphabet amplitudes, or relational support laws—similarly expose a computable minor or annihilating relation at the first surplus observation, or whether some reduce local dimension without producing any global target-pure invariant. That distinction is the next place where Arithmetic Fidelity can separate mere parameter counting from genuine preservation.