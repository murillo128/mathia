# VIS-407 — the qutrit source-invariant chart is boundary-singular

## Claim

Continue in the normalized rank-one qutrit setting of `VIS-388`--`VIS-393`. Let

`E in Herm_0(3)`, `tr(E^2)=1`,

and let the intrinsic source-subspace invariant be

`x = tr(E^3)^2 in [0,1/6]`.

After unitary conjugacy, permutation of eigenvalues, and the generator sign quotient `E ~ -E`, choose the standard Weyl-chamber representative

`lambda_k(theta) = sqrt(2/3) cos(theta + 2 pi k/3)`, `k=0,1,2`,

with

`0 <= theta <= pi/6`.

Then

`tr(E^3) = cos(3 theta)/sqrt(6)`,

so

`x(theta) = (1/6) cos^2(3 theta)`.

The three squared root gaps of the commutator Laplacian are, up to ordering,

`q_1(theta)=2 sin^2(theta)`,

`q_2(theta)=2 sin^2(pi/3-theta)`,

`q_3(theta)=2 sin^2(pi/3+theta)`.

The chamber coordinate `theta` is intrinsically regular: along this normalized diagonal representative,

`sum_k (d lambda_k/d theta)^2 = 1`,

so `theta` is Hilbert-Schmidt arc length. Each `q_i(theta)` has bounded derivative, in fact `|dq_i/dtheta|<=2`.

By contrast, the scalar invariant chart `x=t^2` is metrically singular at both symmetry-enhanced boundaries because

`dx/dtheta = -(1/2) sin(6 theta)`

vanishes at `theta=0` and `theta=pi/6`. The inverse root-spectrum map has square-root boundary splitting. Writing

`delta_+ = 1/6-x`,

near `x=1/6` the two roots meeting at `3/2` satisfy

`q_{2,3} = 3/2 +/- sqrt(2 delta_+) + O(delta_+)`.

Near `x=0`, the two roots meeting at `1/2` satisfy

`q_{1,2} = 1/2 +/- sqrt(2x) + O(x)`

up to ordering of the `+/-` branches.

Therefore the source support is smooth and Lipschitz in intrinsic Hilbert-Schmidt arc length, while its representation as a function of `x=tr(E^3)^2` is only `1/2`-Holder at the Weyl-chamber boundaries. A numerical Lipschitz or derivative budget imposed in the `x` coordinate is consequently **not an intrinsic source-complexity budget**: it can diverge solely because of the scalar chart even when the underlying source path and root spectrum remain geometrically regular.

Combined with `VIS-393`, which proves that source-stabilizer symmetry allows an arbitrary Borel law for the residual qutrit weight coordinate at fixed source, this rules out **source conjugacy/support geometry plus stabilizer symmetry alone** as the missing target-independent decoder restriction required by `VIS-405`--`VIS-406`. Any genuine Wang/source-packet decoder-capacity bound must use additional structure coupling the source to the tangent, response, packet architecture, or another independently fixed admissibility resource.

**Evidence/status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + SOURCE-LOCALIZATION + CLASSICAL SU(3) PARAMETERIZATION + NO-NOVELTY-CLAIM`.

No claim is made that the full Wang construction cannot provide a decoder budget. The result excludes only a budget attributed to rank-one qutrit source conjugacy/support geometry or source-stabilizer symmetry by themselves.

## 1. Weyl-chamber arc length and the cubic invariant

For

`lambda_k(theta)=sqrt(2/3) cos(theta+2 pi k/3)`,

the three shifted cosines sum to zero and their squared sum is `3/2`, hence

`sum_k lambda_k = 0`,

`sum_k lambda_k^2 = 1`.

The identity

`sum_(k=0)^2 cos^3(theta+2 pi k/3) = (3/4) cos(3 theta)`

gives

`tr(E^3)=sum_k lambda_k^3=cos(3 theta)/sqrt(6)`.

Thus the intrinsic sign-quotiented source coordinate from `VIS-388` is exactly

`x(theta)=(1/6)cos^2(3 theta)`.

The chamber interval `0<=theta<=pi/6` maps monotonically from `x=1/6` to `x=0`; its endpoints are precisely the two repeated-root boundaries already identified in `VIS-388`.

Differentiate the eigenvalue vector. Since the shifted sine squares also sum to `3/2`,

`sum_k (d lambda_k/dtheta)^2`
` = (2/3) sum_k sin^2(theta+2 pi k/3)`
` = 1`.

The normalized diagonal representative therefore moves at unit Hilbert-Schmidt speed. This gives a natural intrinsic metric coordinate on the one-dimensional conjugacy quotient, independent of how its remaining scalar invariant is algebraically encoded.

## 2. Root support is regular in the intrinsic coordinate

Taking pairwise differences of the three eigenvalues gives the squared gaps

`2 sin^2(theta)`,

`2 sin^2(pi/3-theta)`,

`2 sin^2(pi/3+theta)`.

These reproduce the endpoint spectra of `VIS-388`:

- at `theta=0`, the support is `{0,3/2,3/2}` and `x=1/6`;
- at `theta=pi/6`, the support is `{1/2,1/2,2}` and `x=0`.

For every branch,

`|d[2 sin^2(a+/-theta)]/dtheta| <= 2`.

Hence the complete ordered root-support path is globally Lipschitz in `theta` away from the harmless relabeling at coincident roots, and the unordered spectrum is continuous through both endpoints.

There is no geometric blow-up in the normalized source orbit itself.

## 3. The invariant chart creates square-root singularities

Differentiate

`x(theta)=(1/6)cos^2(3theta)`

to obtain

`dx/dtheta=-(1/2)sin(6theta)`.

At `theta=0`, Taylor expansion gives

`1/6-x = (3/2) theta^2 + O(theta^4)`.

The two root branches meeting at `3/2` split linearly:

`q_3-q_2 = sqrt(3) sin(2theta) = 2 sqrt(3) theta + O(theta^3)`.

Thus each branch differs from the common value `3/2` by

`sqrt(3) theta + O(theta^2) = sqrt(2(1/6-x)) + O(1/6-x)`

up to sign.

At the other boundary put `epsilon=pi/6-theta`. Then

`x=(3/2)epsilon^2+O(epsilon^4)`,

while the two branches meeting at `1/2` split with first derivative magnitude `sqrt(3)`. Hence

`q_{1,2}=1/2 +/- sqrt(2x)+O(x)`

up to ordering.

The scalar source invariant `x` is therefore an excellent algebraic classifier but a bad global metric chart: the inverse spectrum map has the ordinary square-root behavior of a discriminant coordinate at repeated roots.

## 4. Consequence for decoder-capacity restrictions

`VIS-405` and `VIS-406` establish a useful generic fact: once a numerical decoder Lipschitz/representation budget is fixed independently, it produces a falsifiable uniform-mass floor for the residual law. The open Wang clue asks whether the source/packet mechanism supplies such a target-independent budget rather than fitting it to the observed residual.

The present calculation removes one tempting source of that budget. If decoder regularity is measured against the scalar source coordinate `x=t^2`, even the **intrinsic root spectrum itself** has unbounded `dq/dx` at the source-symmetry boundaries. Reparameterizing the same source orbit by its Hilbert-Schmidt arc length `theta` removes the blow-up. A bound stated only as regularity with respect to `x` therefore depends on the chosen invariant chart and cannot be credited as source-derived complexity without an additional reason that makes `x` the operational input metric.

This coordinate obstruction joins the probability obstruction in `VIS-393`. At a fixed generic qutrit source, source-stabilizer invariance alone permits every Borel law on the residual coordinate `u`. Varying the source conjugacy class supplies only the regular one-dimensional support path above. Neither fact independently restricts the residual decoder family.

Accordingly, a non-vacuous source-derived budget must come from structure not contained in the source conjugacy class itself: for example an explicit Wang map from source packets to tangent sectors, a fixed finite response basis with coefficients controlled by packet resources, a source-response differential estimate in an intrinsic metric, or another mechanism-specific admissibility constraint fixed before the residual is inspected.

## Prior-art and novelty audit

The mathematical ingredients are classical. `VIS-388` already records the standard `SU(3)` root-space description and the fact that a normalized traceless Hermitian `3 x 3` generator has one remaining cubic invariant. It cites Thomas L. Curtright and Cosmas K. Zachos, **Elementary Results for the Fundamental Representation of SU(3)**, *Reports on Mathematical Physics* 76:3 (2015), 401--404, DOI `10.1016/S0034-4877(15)30040-9`, arXiv `1508.00868`, for the Cayley-Hamilton/cubic-invariant background.

The trigonometric Weyl-chamber parameterization, repeated-root discriminant behavior, and square-root splitting derived above are elementary consequences of that classical one-parameter conjugacy geometry. No novelty is claimed for them, for eigenvalue perturbation at a double root, or for using arc length as a regular coordinate.

The Mathia-specific result is the negative control for the current Wang decoder-capacity branch: it identifies an explicit representation dependence that prevents `t^2`-Lipschitzness from serving, by itself, as the independently justified source complexity demanded by `VIS-405`--`VIS-406`, and combines it with the already-persisted `VIS-393` symmetry no-go to localize the remaining restriction to mechanism-specific source-response coupling.

## Boundaries

- The exact calculation is for normalized rank-one qutrit sources. Higher matrix dimension or source rank has a larger conjugacy/subspace geometry and is not classified here.
- `x=t^2` remains a complete algebraic source-shape invariant in this test bed. The result concerns its metric conditioning, not its classification power.
- The square-root singularity does not invalidate a Lipschitz budget if an independent Wang mechanism genuinely uses `x` with that metric and supplies a finite numerical bound on the relevant restricted domain. It shows only that such a bound does not follow from source geometry alone.
- `VIS-393` realizes arbitrary invariant residual laws abstractly; it does not prove that every such law is Wang-admissible. Additional Wang admissibility is exactly the unresolved layer.
- The result does not rule out a decoder budget derived from source--tangent coupling, packet incidence, fixed response bases, finite resources, or destination-side analytic constraints.
- No retained visualization is needed because the obstruction is exact and representation-independent once the two source coordinates are compared.
- No arithmetic anomaly, destination gain, zeta-zero statement, or RH consequence is established.
