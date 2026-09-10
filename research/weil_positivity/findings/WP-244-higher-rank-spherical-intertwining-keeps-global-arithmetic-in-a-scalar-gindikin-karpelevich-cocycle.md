# WP-244 — Higher-rank spherical intertwining keeps global arithmetic in a scalar Gindikin–Karpelevich cocycle

**Status:** `LITERATURE+EXACT-DERIVED + HIGHER-RANK-SPHERICAL-CONTROL + GINDIKIN-KARPELEVICH-SCALARIZATION + A2-WEYL-MATCHED-CONTROL + NORMALIZED-INTERTWINER-ARITHMETIC-REMOVAL + DECISIVE-NEGATIVE-FOR-SPHERICAL-OPERATOR-ESCAPE + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-243` leaves two live ways for the Maaß–Selberg/scattering direction to escape the scalar-normalizer obstruction: a source-defined coupling across primitive congruence oldclasses, or a genuinely vector-valued/higher-rank scattering system whose global arithmetic remains irreducibly operator-valued before positivity. The most canonical version of the second possibility is to replace rank-one `SL(2)` by a split higher-rank arithmetic quotient and use spherical minimal-parabolic Eisenstein series. The Weyl group then has many chambers and the spectral parameter is multidimensional, so it is natural to ask whether the larger scattering system itself turns the completed zeta data into matrix arithmetic.

For the **spherical minimal-parabolic channel**, it does not. The Gindikin–Karpelevich formula shows that every standard intertwining operator acts on the unique spherical line by a scalar product of completed-zeta ratios, one scalar factor for each root in the relevant inversion set. After the standard normalization those same intertwiners send normalized spherical vector to normalized spherical vector: the arithmetic normalizer has been divided out. If the Weyl orbit is bundled into a finite-dimensional vector space, the raw operators become zeta-weighted monomial/permutation matrices, while the normalized operators become the corresponding arithmetic-free Weyl permutations. Higher rank adds noncommutative **Weyl combinatorics**, but not irreducibly operator-valued Riemann arithmetic on the spherical sector.

This is already decisive for the direct higher-rank spherical escape suggested after `WP-243`. The standard source of unitarity/positive Hilbert structure applies to normalized intertwining operators, but on the spherical line those operators retain no completed-zeta scalar. Keeping the raw scalar factor retains the arithmetic phase, yet unitarity gives only reality of its logarithmic phase derivative, not a sign. Positive Gram readouts instead see a modulus square and lose the linear logarithmic-derivative information used by explicit formulas. Thus merely passing from rank one to higher rank does not create the missing independently positive Weil form.

The result is deliberately narrower than a no-go for higher-rank Maaß–Selberg theory as a whole. Differentiating a multidimensional scalar normalizer produces canonical root-direction tensors, and non-spherical inducing data can support genuinely nontrivial normalized intertwiners. Those are category changes that require separate tests. What is closed here is the tempting claim that **spherical higher rank by itself** supplies irreducible operator-valued arithmetic before scalarization.

## 1. The spherical global normalizer is scalar in every rank

Let `G` be a split connected reductive group over `Q`, `B=TN` a minimal parabolic, `lambda` a complex spectral parameter, and

\[
f^0_{\lambda,v}\in I_v(\lambda)
\tag{1}
\]

be the normalized `K_v`-fixed vector in the local unramified principal series. For a Weyl element `w`, the standard local intertwining operator satisfies the Gindikin–Karpelevich formula

\[
M_v(w,\lambda)f^0_{\lambda,v}
=
J_v(w,\lambda)f^0_{w^{-1}\lambda,v},
\tag{2}
\]

with

\[
J_v(w,\lambda)
=
\prod_{\substack{\alpha>0\\w^{-1}\alpha<0}}
\frac{\zeta_{v}(\langle\lambda,\alpha^\vee\rangle)}
{\zeta_{v}(\langle\lambda,\alpha^\vee\rangle+1)}
\tag{3}
\]

for the split `Q` case, in the usual normalized convention. Gurevich--Segal state the corresponding formula for a general split reductive setting and explicitly note that the global Gindikin–Karpelevich factor is the product over all places and hence a ratio of products of complete zeta functions.

Writing

\[
\Lambda_{\mathbb Q}(s)
=\pi^{-s/2}\Gamma(s/2)\zeta(s)
\tag{4}
\]

for the completed Dedekind zeta factor (with its usual poles), the global spherical coefficient can therefore be written

\[
J(w,\lambda)
=
\prod_{\alpha\in I(w)}
\frac{\Lambda_{\mathbb Q}(\langle\lambda,\alpha^\vee\rangle)}
{\Lambda_{\mathbb Q}(\langle\lambda,\alpha^\vee\rangle+1)},
\qquad
I(w)=\{\alpha>0:w^{-1}\alpha<0\}.
\tag{5}
\]

The important structural fact is not the precise shift convention but the type of object in (5): **one scalar meromorphic function on the spherical line**. It already contains both the finite-prime Euler factors and the archimedean Gamma factor, but it contains them inside the same completed scalar normalizer.

Define the normalized intertwiner by

\[
N(w,\lambda)=J(w,\lambda)^{-1}M(w,\lambda)
\tag{6}
\]

where regular. Then

\[
N(w,\lambda)f^0_\lambda=f^0_{w^{-1}\lambda}.
\tag{7}
\]

Equation (7) is the key control. The standard normalization that gives the well-behaved/unitary intertwining family removes exactly the global scalar in which the zeta arithmetic sits. This is not peculiar to `SL(2)` and is not repaired by increasing the semisimple rank.

## 2. Exact rank-two control: six Weyl chambers still give only weighted permutations

Take `G=SL(3)` over `Q`. Write

\[
\lambda=(\lambda_1,\lambda_2,\lambda_3),
\qquad
\lambda_1+\lambda_2+\lambda_3=0,
\tag{8}
\]

and choose positive roots

\[
\alpha_1=e_1-e_2,
\qquad
\alpha_2=e_2-e_3,
\qquad
\alpha_1+\alpha_2=e_1-e_3.
\tag{9}
\]

The Weyl group is `S_3`, so the minimal-parabolic constant term has six Weyl contributions rather than two. For the longest Weyl element `w_0`, all three positive roots lie in the inversion set and (5) becomes

\[
J(w_0,\lambda)
=c(\lambda_1-\lambda_2)
 c(\lambda_2-\lambda_3)
 c(\lambda_1-\lambda_3),
\tag{10}
\]

where

\[
c(u)=\frac{\Lambda_{\mathbb Q}(u)}{\Lambda_{\mathbb Q}(u+1)}.
\tag{11}
\]

For a simple reflection there is one such root factor; for every other Weyl element the coefficient is the product over its inversion set. The increase from two to six constant-term channels is therefore real, but the global analytic coefficient attached to each channel is still scalar.

This remains true if one deliberately packages all Weyl chambers as one vector space. For regular `lambda`, let

\[
\mathscr S_\lambda
=
\bigoplus_{w\in W} L_{w\lambda},
\qquad
L_{w\lambda}=\mathbb C f^0_{w\lambda}.
\tag{12}
\]

In the canonical spherical basis `e_w=f^0_{w lambda}`, a simple-reflection intertwiner has the form

\[
M_i(\lambda)e_w
=j_i(w\lambda)e_{s_iw}
\tag{13}
\]

up to the harmless choice of left/right Weyl convention. Thus its matrix has exactly one nonzero entry in each relevant row and column: it is a **weighted permutation**. After Gindikin–Karpelevich normalization,

\[
N_i(\lambda)e_w=e_{s_iw}.
\tag{14}
\]

The six-dimensional matrix presentation can therefore look nontrivial without introducing any nonabelian arithmetic coupling. The noncommutativity in (14) is the fixed `S_3` Weyl action. The zeta dependence in (13) remains a scalar weight attached to each Weyl edge and disappears under the canonical normalization.

This is the matched control that the `WP-243` escape requires. Rank two really supplies more channels and a noncommutative Weyl group, so the negative result is not obtained by suppressing the new geometry. What fails is specifically the hoped-for conversion of the Riemann data into an irreducible operator coefficient.

## 3. Logarithmic derivatives remain rootwise scalar even though parameter tensors can appear

Maaß–Selberg relations and trace formulas often involve logarithmic derivatives of intertwining operators rather than the operators themselves. Higher rank could therefore appear to evade the preceding argument through the multidimensional parameter `lambda`.

Let

\[
h(u)=\log\Lambda_{\mathbb Q}(u)-\log\Lambda_{\mathbb Q}(u+1).
\tag{15}
\]

For a tangent direction `v` in spectral-parameter space, differentiating (5) gives

\[
D_v\log J(w,\lambda)
=
\sum_{\alpha\in I(w)}
\langle v,\alpha^\vee\rangle
h'(\langle\lambda,\alpha^\vee\rangle).
\tag{16}
\]

Thus the arithmetic logarithmic derivative is still an additive sum of **scalar completed-zeta logarithmic derivatives**. Each `h'` keeps the finite primes, Gamma factor and polar contribution tied together inside the same completed function. The root system supplies geometric coefficients and several arguments, but no matrix-valued global `L`-normalizer appears on the spherical line.

A second derivative does produce a canonical tensor,

\[
D^2\log J(w,\lambda)
=
\sum_{\alpha\in I(w)}
h''(\langle\lambda,\alpha^\vee\rangle)
\,\alpha^\vee\otimes\alpha^\vee.
\tag{17}
\]

Equation (17) is an important falsification control against overstating the result. Higher-rank spherical theory **can** turn scalar arithmetic into a root-space Hessian after differentiating with respect to parameters. However, that tensor is derived from the scalar normalizer after the fact; its coefficients remain independent scalar root factors. This finding does not prove that a full higher-rank Maaß–Selberg chamber identity could never give a useful sign to a particular tensor combination. Such a sign theorem, if source-defined and valid for the full Weil test class, would be a distinct mechanism and must be audited separately.

What (16)--(17) do rule out is calling the mere existence of several spectral coordinates an irreducibly operator-valued scattering normalizer. The operator-valued object is in parameter geometry, not in the arithmetic action of the spherical intertwiner itself.

## 4. The inherited unitary structure and the arithmetic information separate

The line mandate requires a sign theorem supplied independently by geometry. Standard normalized intertwining theory does provide a canonical unitary structure on unitary inducing data. But on the spherical line, (7) shows that the normalized operator on which this clean unitary theorem acts is arithmetically trivial after the source-defined normalization.

Conversely, keep the raw spherical scalar `J`. On a regular unitary spectral line it is a scattering phase in the standard normalization. A direct positive Gram readout sees

\[
\|M(w,\lambda)f^0_\lambda\|^2
=|J(w,\lambda)|^2\,\|f^0_{w^{-1}\lambda}\|^2,
\tag{18}
\]

which on the unitary axis is normalized to the same unit norm. Even away from a convention in which the modulus is literally one, a Gram form sees `|J|^2`: a nonlinear magnitude, not the linear logarithmic derivative entering an explicit formula.

The phase derivative does retain arithmetic. Formally along a real unitary parameter `t`,

\[
A(t)=-iJ(t)^{-1}\frac{dJ(t)}{dt}
\tag{19}
\]

is real whenever `|J(t)|=1`. But this is only a self-adjointness/reality statement. For a scalar unitary phase `J(t)=e^{i\theta(t)}`,

\[
A(t)=\theta'(t),
\tag{20}
\]

and unitarity places no sign restriction on `theta'(t)`. Hence the standard scattering theorem supplies exactly the wrong strength for the Weil objective: Gram positivity erases the phase derivative, while keeping the phase derivative loses positivity.

Increasing the Weyl rank does not change this dichotomy. In the packaged space (12), normalized intertwiners contribute fixed unitary Weyl permutations; raw intertwiners multiply those permutations by scalar arithmetic weights. Neither operation produces an independently positive linear form in the completed-zeta logarithmic derivative.

## 5. Aggressive controls and surviving escapes

### Control A — rank one versus rank two

For `SL(2)`, the nontrivial Weyl coefficient is one scalar completed-zeta ratio. For `SL(3)`, there are six Weyl channels and the longest coefficient has three root factors. Equations (10)--(14) show that the additional channels change the Weyl combinatorics but not the scalar nature of the arithmetic. The obstruction therefore survives the first genuinely higher-rank matched control.

### Control B — a dense change of Weyl basis

Conjugating the weighted-permutation matrices by a generic fixed unitary basis change can make them dense. That does not create invariant cross-root arithmetic: returning to the canonical spherical lines recovers (13), and the normalized family recovers the arithmetic-free Weyl action (14). A dense matrix obtained only by basis change is representation, not new coupling.

### Control C — differentiate before normalizing

Equation (16) retains the zeta/Gamma/polar package, but only as rootwise scalar logarithmic derivatives. Equation (17) can create root-space cross terms after evaluating a quadratic form in parameter directions, so the present result deliberately leaves a higher-rank truncation/Hessian mechanism open. To qualify, that route must derive its parameter-space form and its sign from the Maaß–Selberg geometry itself, not choose a tangent direction or root combination after inspecting the desired zeta divisor.

### Control D — non-spherical inducing data

The conclusion is **not** extended to general `K`-types, non-spherical automorphic inducing representations, or Braverman--Kazhdan/Langlands--Shahidi type normalized operators on their full representation spaces. Those settings can support genuinely nontrivial normalized intertwiners. Indeed Braverman and Kazhdan construct explicit unitary transforms between `L^2(G/[P,P])` spaces using dual-group nilpotent structure, while Henry Kim's Langlands--Shahidi analysis makes explicit the scalar `L`-functions used to normalize more general global intertwining operators. Whether any such operator retains Riemann arithmetic in a noncentral positive channel is a separate question.

### Control E — hand-built off-diagonal Weyl kernels

One can always put the six scalar functions `J(w,lambda)` into a dense matrix by choosing extra off-diagonal entries, or select a linear combination of their logarithmic derivatives intended to cancel Gamma/polar pieces. Unless the extra kernel is forced by the source geometry before the target sign is examined, this is exactly the hand-picked-kernel/repackaging move excluded by the `weil_positivity` mandate.

## 6. Prior-art and novelty audit

The spherical scalarization used here is classical, not a Mathia discovery.

- Nadya Gurevich and Avner Segal, *Poles of the Standard L-function of G2 and the Rallis–Schiffmann Lift*, Canadian Journal of Mathematics 71 (2019), 1127--1161, DOI `10.4153/CJM-2018-019-7`, Section 3.1. Their displayed Gindikin–Karpelevich formula gives (2)--(3) for normalized spherical vectors and states explicitly that the global factor is a ratio of products of complete zeta functions.
- Daniel Bump and Maki Nakasuji, *Integration on p-adic groups and crystal bases*, Proceedings of the American Mathematical Society 138 (2010), 1595--1605, DOI `10.1090/S0002-9939-09-10206-X`. This is a direct local spherical Gindikin–Karpelevich anchor: the standard spherical-vector integral is a product over positive roots.
- Henry H. Kim, *On Local L-Functions and Normalized Intertwining Operators*, Canadian Journal of Mathematics 57 (2005), 535--597, DOI `10.4153/CJM-2005-023-x`. It makes explicit the `L`-functions that occur as **scalar normalizing factors** of global intertwining operators in the Langlands--Shahidi setting and is a useful prior-art boundary against treating the separation `M=rN` as new.
- Alexander Braverman and David Kazhdan, *Normalized intertwining operators and nilpotent elements in the Langlands dual group*, Moscow Mathematical Journal 2 (2002), 533--553, DOI `10.17323/1609-4514-2002-2-3-533-553`, arXiv `math/0206119`. This is a deliberate escape-control reference: genuinely operator-valued unitary normalized transforms exist on larger spaces and therefore must not be ruled out by the spherical-line argument.

A bounded literature search combining `Weil positivity`, `Maaß--Selberg`, `higher rank`, `spherical Eisenstein`, `Gindikin--Karpelevich`, and `normalized intertwining` found the classical scattering/normalization theory above and the existing Connes--Consani trace/Weil program, but no source in the audited set where **mere spherical higher-rank Weyl multiplicity** converts the completed Riemann factor into an irreducible positive operator proving the global Weil sign. This absence is not a completeness claim. The novelty here is only the line-specific obstruction: the explicit higher-rank escape left by `WP-243` collapses, in its spherical minimal-parabolic form, to a scalar arithmetic cocycle around an arithmetic-free normalized Weyl action.

## 7. Research consequence

The direct candidate

\[
\text{spherical higher-rank Eisenstein scattering}
\longrightarrow
\text{irreducibly operator-valued zeta arithmetic}
\longrightarrow
\text{independent positivity}
\tag{21}
\]

fails at its first arrow. Higher rank intrinsically supplies Weyl combinatorics and multidimensional truncation geometry, but the standard spherical intertwining arithmetic remains scalar and is removed by canonical normalization.

The remaining Maaß–Selberg/scattering search is therefore narrower. A viable continuation must exhibit at least one of the following genuinely new ingredients: a source-defined coupling across primitive oldclasses; non-spherical/vector-valued inducing data for which the **normalized operator itself** carries relevant noncentral arithmetic; or a higher-rank truncation/parameter-space form whose sign is independently forced and whose rootwise scalar normalizers combine into the exact Weil functional without target-chosen projections. `WP-244` supplies no such construction and proves no case of RH. It converts the most immediate spherical higher-rank escape into a matched negative control.