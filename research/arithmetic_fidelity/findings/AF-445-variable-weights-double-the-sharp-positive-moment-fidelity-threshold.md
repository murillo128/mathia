# AF-445 — Variable weights double the sharp positive-moment fidelity threshold

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `SHARP-WEIGHTED-MOMENT-THRESHOLD`, `TARGET-PURE-FIBER`, `HANKEL-RANK-CERTIFICATE`, `CONDITIONING-DECAY`, `CLASSICAL-STIELTJES/PRONY`, `NO-NOVELTY-CLAIM`

## Claim

AF-444 shows that for positive **unit-weight** atoms, `K` latent support coordinates can hide a remote added atom from `K` moments, while one surplus consecutive moment gives a global Newton-Girard certificate. Allowing the nuisance atoms to carry unknown positive weights doubles their local degrees of freedom. The corresponding exact-fidelity threshold doubles as well.

For a positive finite atomic measure

\[
\mu=\sum_{i=1}^r a_i\delta_{x_i},
\qquad a_i>0,\quad x_i>0,
\]

write its positive power moments as

\[
m_n(\mu)=\int t^n\,d\mu(t)=\sum_{i=1}^r a_i x_i^n,
\qquad n\ge1.
\tag{1}
\]

Fix `K>=1`.

### Negative side: `2K` moments can still hide one remote atom

Choose any base `K`-atomic measure

\[
\mu_0=\sum_{i=1}^K a_i^0\delta_{x_i^0}
\]

with distinct positive support points and positive weights, and fix a target weight `c>0`. Then for every sufficiently small `y>0` there is another `K`-atomic positive measure

\[
\widetilde\mu_y=\sum_{i=1}^K \widetilde a_i(y)\delta_{\widetilde x_i(y)}
\]

arbitrarily close to `\mu_0` in its labeled weight/support parameters such that

\[
\boxed{
 m_n(\mu_0)
 =m_n(\widetilde\mu_y+c\delta_y),
 \qquad n=1,\ldots,2K.
}
\tag{2}
\]

Moreover

\[
\max_i\Bigl(
|\widetilde a_i(y)-a_i^0|
+|\widetilde x_i(y)-x_i^0|
\Bigr)=O(y).
\tag{3}
\]

Thus a fixed family of the first `2K` positive moments can be exactly target-impure even though the source carrying the target has `K+1` distinct positive atoms.

### Positive side: moment `2K+1` gives a global certificate

If `\mu` has at most `K` distinct positive support points, while `\nu` has exactly `K+1` distinct positive support points with positive weights, then

\[
\boxed{
(m_1(\mu),\ldots,m_{2K+1}(\mu))
\ne
(m_1(\nu),\ldots,m_{2K+1}(\nu)).
}
\tag{4}
\]

The separating invariant is the shifted Hankel determinant

\[
D_K(m)
:=
\det\bigl[m_{i+j+1}\bigr]_{i,j=0}^{K}.
\tag{5}
\]

For every measure with at most `K` distinct atoms,

\[
D_K=0,
\tag{6}
\]

whereas for

\[
\nu=\sum_{j=1}^{K+1} b_j\delta_{z_j},
\qquad b_j>0,
\qquad z_j>0\text{ distinct},
\]

one has the exact factorization

\[
\boxed{
D_K(\nu)
=
\left(\prod_{j=1}^{K+1} b_j z_j\right)
\left(\prod_{1\le i<j\le K+1}(z_j-z_i)^2\right)
>0.
}
\tag{7}
\]

Consequently the first `2K+1` consecutive positive moments are globally target-pure for the distinction

\[
\text{at most `K` positive atoms}
\quad\text{versus}\quad
\text{`K+1` distinct positive atoms},
\]

while `2K` moments are not sufficient in the worst case.

For this precise weighted-atomic source class the threshold is therefore sharp:

\[
\boxed{
2K\text{ positive moments can fail,}
\qquad
2K+1\text{ positive moments always separate.}
}
\tag{8}
\]

This is the weighted analogue of AF-443/AF-444. The extra nuisance amplitudes change the source dimension from `K` to `2K`, and a **source-law certificate** again appears exactly one observation beyond that local dimension.

## Why the first `2K` moments remain locally programmable

Parameterize a labeled `K`-atomic measure by

\[
\theta=(a_1,\ldots,a_K,x_1,\ldots,x_K)
\]

inside the open set where all weights are positive and all support points are positive and distinct. Define

\[
F(\theta)
=
(m_1,\ldots,m_{2K})
\in\mathbb R^{2K}.
\tag{9}
\]

At a base point `\theta_0`, the Jacobian columns associated with the weights and supports are

\[
\frac{\partial m_n}{\partial a_i}=x_i^n,
\qquad
\frac{\partial m_n}{\partial x_i}=n a_i x_i^{n-1},
\qquad
n=1,\ldots,2K.
\tag{10}
\]

This square Jacobian is nonsingular. A short dual proof avoids writing a confluent Vandermonde determinant explicitly. Suppose a row vector `\lambda=(\lambda_1,\ldots,\lambda_{2K})` annihilates every column and form

\[
P(t)=\sum_{n=1}^{2K}\lambda_n t^n.
\tag{11}
\]

The weight columns give

\[
P(x_i)=0,
\]

and the support columns give

\[
a_iP'(x_i)=0,
\]

hence

\[
P'(x_i)=0
\qquad(i=1,\ldots,K).
\tag{12}
\]

So every `x_i` is a double root of `P`. Because `(11)` has no constant term, `0` is another root. The `K` distinct positive double roots together with `0` give at least `2K+1` roots counted with multiplicity, but `\deg P\le2K`. Therefore `P\equiv0`, hence `\lambda=0`, and the Jacobian is invertible.

The inverse-function theorem now gives a neighborhood `U` of `\theta_0` whose moment image contains a neighborhood of `F(\theta_0)`. For the target atom `c\delta_y`, define

\[
v_{2K}(y)
=(y,y^2,\ldots,y^{2K}).
\tag{13}
\]

Since

\[
c\,v_{2K}(y)\longrightarrow0
\qquad(y\downarrow0),
\]

for all sufficiently small `y` there is a unique nearby parameter vector `\widetilde\theta(y)` satisfying

\[
F(\widetilde\theta(y))
=F(\theta_0)-c\,v_{2K}(y).
\tag{14}
\]

Adding `c\delta_y` to the corresponding nuisance measure yields `(2)` exactly. Shrinking `U` if necessary preserves positivity, distinctness, and any preassigned small disjoint cells around the base nuisance supports. Taking `y` below all of those cells also makes the target atom distinct from every nuisance atom.

Because the local inverse is differentiable and

\[
\|v_{2K}(y)\|=O(y),
\]

one obtains `(3)`. The collision is therefore not only exact; the nuisance adjustment needed to hide the target vanishes linearly with the disappearing target coordinate.

## Shifted Hankel rank gives the surplus-observation certificate

Given moments through order `2K+1`, form the shifted Hankel matrix

\[
H_K^+(\mu)
=
\bigl[m_{i+j+1}(\mu)\bigr]_{i,j=0}^{K}.
\tag{15}
\]

For

\[
\mu=\sum_{j=1}^{r}a_j\delta_{x_j},
\]

let

\[
V_{ij}=x_j^i,
\qquad 0\le i\le K,
\qquad 1\le j\le r.
\]

Then

\[
\boxed{
H_K^+(\mu)
=
V\,\operatorname{diag}(a_1x_1,\ldots,a_rx_r)\,V^T.
}
\tag{16}
\]

If `r\le K`, this matrix has rank at most `K`, so its determinant vanishes. If `r=K+1` and the positive support points are distinct, `V` is a square nonsingular Vandermonde matrix while the diagonal matrix in `(16)` is positive definite. Hence `H_K^+(\mu)` is positive definite and

\[
\det H_K^+(\mu)
=
(\det V)^2\prod_j a_jx_j,
\]

which is exactly `(7)`.

This proves `(4)` globally. Unlike the negative result, it is not a local rank argument. The determinant is a polynomial function of the retained moments and vanishes on the entire `K`-atomic observation class while remaining strictly positive on every `(K+1)`-distinct-atom positive source.

The **shift** in `(15)` matters. The observation begins at `m_1`, not at total mass `m_0`. Algebraically, the shifted factorization weights each atom by the additional factor `x_j`; geometrically, this is why an atom approaching the lost boundary `x=0` becomes increasingly difficult to distinguish even after exact identifiability has been restored.

## Quantitative class separation

The Hankel certificate also separates exact fidelity from conditioning.

Let the `K` nuisance supports range in pairwise disjoint compact intervals contained in

\[
[\alpha,\beta]\Subset(0,\infty),
\]

with a uniform pairwise separation at least `\delta>0`. Let nuisance weights lie in

\[
[w_-,w_+],
\qquad w_->0,
\]

and let the target weight satisfy `c\in[c_-,c_+]` with `c_->0`. Restrict

\[
0<y\le y_0<\alpha/2.
\]

Write `\mathcal C_0` for the first-`2K+1`-moment image of the nuisance-only class and `\mathcal C_1(y)` for the image after adjoining `c\delta_y`, allowing the nuisance parameters to vary independently on the two sides.

On `\mathcal C_0`, the determinant polynomial `D_K` is identically zero. On `\mathcal C_1(y)`, `(7)` gives

\[
D_K
=
cy
\left(\prod_{i=1}^{K}b_i z_i\right)
\left(\prod_{1\le i<j\le K}(z_j-z_i)^2\right)
\left(\prod_{i=1}^{K}(z_i-y)^2\right).
\tag{17}
\]

All factors except `y` are bounded uniformly away from zero on the declared compact source class. Therefore

\[
D_K\ge A y
\tag{18}
\]

for some `A>0` independent of small `y`.

The determinant is a polynomial in the retained moment vector. On one compact convex set containing all relevant observation vectors and their joining segments, its gradient is bounded by some `L<\infty`. Hence for every `q\in\mathcal C_0` and `q'\in\mathcal C_1(y)`, the mean-value inequality gives

\[
Ay
\le
|D_K(q')-D_K(q)|
\le
L\|q'-q\|.
\tag{19}
\]

Thus

\[
\operatorname{dist}(\mathcal C_0,\mathcal C_1(y))
\ge
(A/L)y.
\tag{20}
\]

For the reverse bound choose identical nuisance parameters on both sides. Their observation vectors then differ only by

\[
c(y,y^2,\ldots,y^{2K+1}),
\]

whose norm is `O(y)` uniformly for bounded `c`. Therefore

\[
\boxed{
\operatorname{dist}(\mathcal C_0,\mathcal C_1(y))
=\Theta(y).
}
\tag{21}
\]

If the target weight itself is allowed to decay, the same factorization shows the natural first-order certificate scale is `cy`, provided the remaining compact separation assumptions stay uniform.

So allowing unknown nuisance amplitudes changes the **number of observations required for exact target purity**, but once that threshold is crossed the disappearing-target conditioning scale is still linear in the target coordinate.

## Reciprocal-square shell specialization

In the AF-442 through AF-444 shell model, put

\[
x_i=r_{j_i}^{-2}
\]

for `K` earlier nuisance shells and let the target reciprocal coordinate be

\[
y=r_m^{-2}.
\]

Now allow each earlier occupied shell to carry an unknown positive amplitude as well as an unknown support location inside its retained cell. The nuisance class has `2K` local continuous parameters: `K` weights and `K` realized supports.

Equation `(2)` shows that the first `2K` reciprocal-power moments can still hide a sufficiently remote target occupancy of fixed positive weight by perturbing only those earlier amplitudes and supports inside arbitrarily small neighborhoods. Shell/cell provenance by itself does not prevent the collision.

If one retains the first `2K+1` reciprocal-power moments, however, the shifted Hankel determinant forbids the collision whenever the target reciprocal coordinate is distinct from the nuisance coordinates. For a remote shell this distinctness is automatic. On fixed separated earlier cells with target weight bounded away from zero,

\[
y=\Theta(m^{-2}),
\]

so `(21)` gives

\[
\boxed{
\operatorname{dist}(\mathcal C_0,\mathcal C_1(m))
=\Theta(m^{-2}).
}
\tag{22}
\]

Thus the weighted source law has a clean two-resource accounting:

\[
\boxed{
\text{exact-fidelity threshold: }2K+1\text{ moments},
\qquad
\text{remote-target margin: }\Theta(m^{-2}).
}
\tag{23}
\]

The first quantity prices latent source freedom; the second prices downstream robustness after that freedom has been eliminated from the target fiber.

## Relation to AF-443 and AF-444

AF-443 established the negative local principle for **unit weights**: `K` independently movable supports can absorb a remote added unit atom from `K` moment equations.

AF-444 then showed that one surplus consecutive moment is sufficient globally because unit weights impose a cardinality law visible through the top Newton coefficient. Its sharp threshold is therefore `K+1` positive moments.

The present result changes only one source law: the nuisance weights are now unknown positive variables. That apparently small relaxation changes the local parameter count from `K` to `2K` and destroys the `K+1`-moment Newton certificate as a universal separator. The matching replacement is the shifted Hankel rank law: a `K`-atomic positive measure has shifted Hankel rank at most `K`, while a `(K+1)`-distinct-atomic positive measure has rank `K+1`.

This produces a stronger structural lesson than raw dimension counting alone:

\[
\boxed{
\text{observation surplus is useful only when a source law converts it into a target-sensitive invariant.}
}
\tag{24}
\]

For unit atoms that invariant was an elementary symmetric coefficient. For arbitrary positive weights it is a Hankel determinant. In both cases the first globally decisive observation lies one step beyond the dimension of the nuisance parameterization.

## Prior-art and novelty audit

All algebraic ingredients are classical, and no novelty is claimed for finite-atomic moment recovery, Prony reconstruction, Hankel rank, Vandermonde factorization, confluent-Vandermonde nonsingularity, or the inverse-function theorem.

Konrad Schmüdgen, ***The Moment Problem***, Graduate Texts in Mathematics 277, Springer (2017), DOI `10.1007/978-3-319-64546-9`, gives a unified treatment of the one-dimensional full and truncated Hamburger/Stieltjes moment problems. Chapter 9 develops Hankel matrices, Hankel rank, finitely atomic representing measures, and the truncated one-dimensional moment problem. The factorization `(16)` is the elementary finite-atomic specialization of this classical moment-matrix framework.

Gerlind Plonka and Manfred Tasche, **“Prony methods for recovery of structured functions,”** *GAMM-Mitteilungen* 37(2), 239–258 (2014), DOI `10.1002/gamm.201410011`, surveys classical Prony recovery of finitely supported exponential/atomic structures from moment-like samples, including the central role of Hankel matrices and annihilating polynomials.

Dmitry Batenkov, Gil Goldman, Yehonatan Salman, and Yosef Yomdin, **“Algebraic Geometry of Error Amplification: the Prony leaves,”** arXiv:`1702.05338` (2017), studies equi-moment surfaces in node/amplitude parameter space. It is direct prior art for the local geometry behind the `2K`-moment collision side.

The Arithmetic Fidelity contribution recorded here is the **paired sharp boundary needed by the current source-law frontier**: with `K` unknown supports and `K` unknown positive nuisance weights, the first `2K` positive moments admit exact remote-target collisions, while moment `2K+1` supplies a global source-derived shifted-Hankel certificate. The same certificate quantifies the surviving margin and shows that exact recovery and conditioning remain distinct resources.

No claim is made that this threshold, the Hankel determinant formula, or Prony identifiability is new mathematics in isolation.

## Boundaries and falsification checks

- The positive theorem distinguishes **effective support cardinality**. If the added target lands exactly on an existing nuisance support, its weight can merge with that atom and the `(K+1)`-distinct-support hypothesis fails. No positive-moment statistic can recover a label that the source model itself identifies with a weight change at the same point.
- Strict positivity of weights and support points is used in the sign certificate. Signed or complex amplitudes require a different audit; the determinant can lose positivity even when the Vandermonde rank remains full.
- The sharp threshold concerns the consecutive positive moments `m_1,...,m_{2K+1}`. It is not a theorem for arbitrary sparse sets of `2K+1` moment orders.
- The negative construction is local and requires the target coordinate to be sufficiently small so that its moment vector lies in the local image of the nuisance moment map. It does not say that every target location can be hidden from `2K` moments.
- The `Theta(y)` class-margin statement requires nuisance weights bounded away from zero, nuisance supports bounded away from zero and from each other, and the target separated from those nuisance supports. If weights vanish or supports collide, the Vandermonde/Hankel certificate becomes ill-conditioned at exactly the rates visible in `(17)`.
- The result uses labeled local nuisance coordinates for the inverse-function argument. Distinct disjoint support neighborhoods remove permutation ambiguity; the final moment collision is a statement about the unlabeled measures themselves.
- Total mass `m_0` is deliberately not retained. Including `m_0` changes the observation model: a fixed-weight atom approaching `y=0` still contributes a nonvanishing amount to total mass, so the remote-target attenuation studied here disappears at order zero.
- The theorem separates one added positive atom from a source with at most `K` effective atoms. Multiple coordinated target changes or a nuisance class with more atoms require a new rank/source-law audit.
- Nothing here distinguishes rational primes, constrains the Riemann zero divisor, or implies RH. It classifies one precise compression boundary that any Euler-style finite-moment representation must respect when amplitudes as well as support positions are latent.

A direct falsification of the positive half would require a `K`-atomic and a `(K+1)`-distinct-atomic positive measure with equal moments through order `2K+1`; their common shifted Hankel matrix would have determinant simultaneously zero by the first representation and strictly positive by `(7)`. A falsification of the negative half would require failure of local reachability despite the square Jacobian `(10)` being nonsingular; the polynomial root argument proves that nonsingularity exactly under the stated hypotheses.

## Consequence for the research line

The source-law classification can now distinguish two exact thresholds rather than treating “finite moments” as one undifferentiated representation class:

- unit weights: `K` nuisance parameters, sharp threshold `K+1` consecutive positive moments (AF-444);
- unknown positive weights: `2K` nuisance parameters, sharp threshold `2K+1` consecutive positive moments (this finding).

Both cases obey the same pattern: **local nuisance dimension sets the collision budget, but a specific algebraic source law—not dimension count alone—must supply the first globally separating invariant beyond that budget.**

The next useful frontier is therefore not to add more generic moments blindly. It is to classify which further source constraints—known weight sums, coupled amplitudes, multiplicative relations, repeated/structured weights, or relational support laws—reduce the effective nuisance dimension and, crucially, which explicit invariant converts the resulting surplus into target purity. Only after such a certificate is identified should conditioning, Padé/Prony algorithms, or downstream arithmetic transport be compared.