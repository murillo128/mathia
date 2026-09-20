# AF-463 — Convex boundaries do not improve pairwise local linear fidelity beyond their affine hull

**Status:** `EXACT-DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `SOURCE-LAW`, `PAIRWISE-FIDELITY`, `PARATINGENT-GEOMETRY`, `NO-NOVELTY-CLAIM`

## Claim

For a convex source class, moving two nearby source points symmetrizes every one-sided boundary restriction. The exact local object for pairwise linear fidelity is therefore not the ordinary anchored tangent cone but the **paratingent cone**, and for a convex set that cone is the closed linear direction space of its affine hull.

Let `X` be a real normed space, let `C subset X` be convex with at least two points, and fix `x_bar in C`. Write

\[
L_C:=\overline{\operatorname{span}}(C-C).
\tag{1}
\]

Define the Bouligand paratingent cone through moving secants by

\[
T_C^P(x_{\rm bar})
:=
\left\{
v:\ \exists x_n,y_n\in C,\ x_n\to x_{\rm bar},\ y_n\to x_{\rm bar},\ t_n\downarrow0,
\ \frac{y_n-x_n}{t_n}\to v
\right\}.
\tag{2}
\]

Then

\[
\boxed{T_C^P(x_{\rm bar})=L_C.}
\tag{3}
\]

In particular, the paratingent cone is independent of the chosen base point inside the convex source class. Boundary faces can shrink the one-sided contingent cone, but they do not shrink the moving-secant geometry relevant to arbitrary nearby pairs.

Now let `F:X->Y` be a bounded linear map into a normed space `Y`. For any relative neighborhood `W` of `x_bar` in `C`, define the local pairwise lower gain

\[
\kappa_W(F;C)
:=
\inf_{\substack{x,y\in W\\x\ne y}}
\frac{\|F(x-y)\|}{\|x-y\|}.
\tag{4}
\]

Then

\[
\boxed{
\kappa_W(F;C)
=
\inf_{0\ne v\in L_C}\frac{\|Fv\|}{\|v\|}.
}
\tag{5}
\]

Thus every local pairwise lower-Lipschitz question for a bounded linear compression of a convex source class is already determined by the compression on the closed affine direction space `L_C`. Positivity, active faces, finite support at the anchor, and other one-sided convex-boundary information can improve **anchored** fidelity, but cannot improve pairwise local linear fidelity beyond what the affine hull already permits.

For the countable probability simplex

\[
\Delta(A)=\left\{\mu\in\ell^1(A):\mu\ge0,\ \sum_a\mu(a)=1\right\},
\tag{6}
\]

one has

\[
L_{\Delta(A)}
=
\left\{h\in\ell^1(A):\sum_a h(a)=0\right\}.
\tag{7}
\]

For the canonical linear inclusion `J:ell^1(A)->ell^2(A)`,

\[
\boxed{
\inf_{\substack{0\ne h\in L_{\Delta(A)}}}
\frac{\|h\|_2}{\|h\|_1}=0.
}
\tag{8}
\]

Consequently the pairwise collapse proved at the finite-support anchor in AF-462 is not specific to that anchor: every relative neighborhood of **every** point of the infinite simplex has zero pairwise `ell^1`-to-`ell^2` lower gain under `J`.

## Exact derivation

### Convex moving secants fill the affine direction space

Every element of `T_C^P(x_bar)` is a limit of vectors `(y_n-x_n)/t_n` with `x_n,y_n in C`. Each such vector lies in `span(C-C)`, hence

\[
T_C^P(x_{\rm bar})\subseteq L_C.
\tag{9}
\]

For the reverse inclusion, first take `w in span(C-C)`. Any finite linear combination of differences can be rewritten as one positive scalar multiple of one difference. Indeed, after swapping endpoints when a coefficient is negative, write

\[
w=\sum_{j=1}^m\lambda_j(a_j-b_j),\qquad \lambda_j\ge0.
\]

If `alpha=sum_j lambda_j>0`, convexity gives

\[
a=\sum_j\frac{\lambda_j}{\alpha}a_j\in C,
\qquad
b=\sum_j\frac{\lambda_j}{\alpha}b_j\in C,
\]

and therefore

\[
w=\alpha(a-b).
\tag{10}
\]

Choose `epsilon_n downarrow 0` and set

\[
x_n=(1-\epsilon_n)x_{\rm bar}+\epsilon_n b,
\qquad
y_n=(1-\epsilon_n)x_{\rm bar}+\epsilon_n a.
\tag{11}
\]

Both points lie in `C`, both converge to `x_bar`, and with `t_n=epsilon_n/alpha`,

\[
\frac{y_n-x_n}{t_n}=w.
\tag{12}
\]

Hence `span(C-C) subset T_C^P(x_bar)`. The paratingent cone is closed by its sequential outer-limit definition; equivalently, a diagonalization of `(11)` for an approximating sequence in `span(C-C)` gives every vector in `L_C`. This proves `(3)`.

The distinction from the anchored tangent cone is exact. At a boundary point, the ordinary tangent cone uses secants from the fixed anchor and can remain one-sided. The paratingent permits the base point to move with the comparison pair; convexity then realizes both signs of every affine direction arbitrarily close to the anchor.

### Local pairwise gain equals the affine-hull minimum modulus

Every difference `x-y` of points in `C` belongs to `L_C`, so `(4)` immediately gives

\[
\kappa_W(F;C)
\ge
m_{L_C}(F)
:=
\inf_{0\ne v\in L_C}\frac{\|Fv\|}{\|v\|}.
\tag{13}
\]

For the reverse inequality, take any nonzero `w in span(C-C)` and write it as `w=alpha(a-b)` as in `(10)`. Because `W` is a relative neighborhood of `x_bar`, the points in `(11)` belong to `W` for all sufficiently small `epsilon_n`. Their difference is `epsilon_n(a-b)`, so linearity gives the scale-invariant identity

\[
\frac{\|F(y_n-x_n)\|}{\|y_n-x_n\|}
=
\frac{\|F(a-b)\|}{\|a-b\|}
=
\frac{\|Fw\|}{\|w\|}.
\tag{14}
\]

Thus the local infimum is at most the minimum modulus over `span(C-C)`. Normalized vectors from this span are dense in the unit sphere of `L_C`; boundedness of `F` passes the quotient continuously along normalized approximants. Therefore

\[
\kappa_W(F;C)\le m_{L_C}(F),
\tag{15}
\]

and `(5)` follows.

This proves something stronger than a tangent-cone necessary condition: for convex sources and bounded linear destinations, the affine direction space gives the **exact** pairwise local fidelity constant in every relative neighborhood.

### Infinite probability simplex

If `h in ell^1(A)` has zero total mass and `h != 0`, then its positive and negative parts have the same mass

\[
m=\|h_+\|_1=\|h_-\|_1>0.
\]

The normalized laws `p=h_+/m` and `q=h_-/m` belong to `Delta(A)`, and

\[
h=m(p-q).
\tag{16}
\]

So `(7)` follows directly, with no closure defect.

Choose `2N` distinct atoms and define

\[
h_N
=
\frac1{2N}\sum_{j=1}^N\delta_{a_j}
-
\frac1{2N}\sum_{j=1}^N\delta_{b_j}.
\tag{17}
\]

Then

\[
\sum_a h_N(a)=0,
\qquad
\|h_N\|_1=1,
\qquad
\|h_N\|_2=\frac1{\sqrt{2N}}\to0.
\tag{18}
\]

This proves `(8)`. Combining `(5)` and `(8)` gives zero local pairwise gain around every source law in the countably infinite simplex, including boundary laws with finite support.

## What this adds to AF-462

AF-462 showed by an explicit construction that a finite-support simplex boundary has two sharply different behaviors. Its anchored radial carrier retains a one-sided support constraint and the canonical Hilbert marking has exact anchored TV gain `1/sqrt(s)`. Yet arbitrary nearby pairs have zero lower gain because they can share the same depletion of the anchor and differ only by diffuse fresh-support mass.

The present result identifies the reusable geometry behind that split. The anchored carrier is a section of the ordinary feasible tangent cone; the pairwise carrier is controlled by the paratingent cone. **Convexity itself forces the latter to forget every active-face inequality and recover the whole affine direction space.** The fresh-support example of AF-462 is therefore one witness of a general convex symmetrization theorem, not an isolated pathology of the simplex.

This also sharpens the next-source-law gate. A convex restriction can protect an anchored discriminator through one-sided provenance, but it cannot create a stronger pairwise linear modulus unless its affine hull is already small enough for the destination map to be bounded below. To escape that conclusion one must change at least one load-bearing hypothesis: use a genuinely nonconvex/singular source class with a smaller paratingent geometry, retain a distinguished anchor rather than arbitrary pairs, change the source metric, or use a nonlinear/relational destination whose pairwise behavior is not captured by one bounded linear map on `L_C`.

## Prior-art and novelty audit

The mathematical language is classical, and this finding makes **no novelty claim** for paratingent cones, convex tangent geometry, strict/two-point differentiability, or minimum-modulus arguments.

- Szymon Dolecki and Gabriele H. Greco, **“Tangency vis-à-vis Differentiability by Peano, Severi and Guareschi,”** *Journal of Convex Analysis* 18(2) (2011), 301–339; arXiv:`1003.1332`. They document the Severi–Bouligand paratangent/paratingent tradition and its role in strict, two-point differential behavior, which is exactly the conceptual distinction needed between anchored and moving-secant fidelity.
- Matúš Benko and Patrick Mehlitz, **“Isolated Calmness of Perturbation Mappings and Superlinear Convergence of Newton-Type Methods,”** *Journal of Optimization Theory and Applications* 203 (2024), 1587–1621, DOI `10.1007/s10957-024-02522-2`. Their variational-analysis setup defines tangent, limiting-tangent, and paratingent cones by moving base points and explicitly notes that the inclusions can be strict even for convex polyhedral sets; for `R_-^2` at the origin the ordinary tangent cone is `R_-^2` while the paratingent cone is all of `R^2`.
- Jean-Pierre Aubin and Hélène Frankowska, *Set-Valued Analysis*, Birkhäuser (1990), is standard background for contingent/paratingent constructions and set-valued local geometry.

The exact equality `(3)` for a convex source and the minimum-modulus identity `(5)` are elementary consequences of convexity and bounded linearity and are presented here as derived specializations, not as new variational-analysis theorems. Their value inside Arithmetic Fidelity is the resulting **classification rule**: convex one-sided boundary information is invisible to pairwise local linear fidelity once moving comparisons are allowed.

## Boundary and falsification audit

- **Convexity is load-bearing.** For a nonconvex or singular source class, local moving secants need not fill the affine direction space. Such classes are precisely where a smaller paratingent cone may provide genuine pairwise protection.
- **Linearity is load-bearing for `(5)`.** A nonlinear destination can distinguish nearby pairs through state-dependent derivatives or higher-order structure. Equation `(3)` still constrains source directions, but the exact minimum-modulus reduction need not survive.
- **This is pairwise, not anchored.** The result does not weaken AF-462's anchored modulus. It explains why that modulus cannot be promoted to arbitrary pairs merely from convex positivity.
- **Affine-hull reduction is not automatically a failure.** If `F` is bounded below on `L_C`, then pairwise fidelity is positive. The theorem says only that convex boundary geometry contributes no extra pairwise improvement beyond that fact.
- **Closure matters in infinite dimensions.** The source direction space is `overline(span(C-C))`; omitting the closure can miss limiting pairwise directions relevant to the lower modulus.
- **The source metric is the ambient norm.** A different intrinsic metric may alter which secants are normalized and can evade `(5)` only after its relation to the ambient linear structure is stated explicitly.
- **No prime conclusion follows from convexity alone.** A rational-prime application must identify the actual admissible source family and whether its downstream theorem needs anchored discrimination or arbitrary pairwise stability.

## Arithmetic specialization

This gives a concrete warning for any prime-derived construction that convexifies or mixture-closes its admissible source family before applying a bounded linear statistic, feature map, moment map, trace readout, or Hilbert embedding. Once the relevant source class is convex, pairwise local fidelity is controlled entirely by the closed affine direction space. Active positivity faces, sparse support of one distinguished arithmetic source, or one-sided provenance at that source cannot improve the pairwise modulus.

Therefore a proposed RH mechanism that needs stable distinction between **arbitrary nearby admissible arithmetic controls** cannot cite convex positivity or an anchored support constraint as the missing discriminator. It must instead prove one of the sharper alternatives exposed above: the actual arithmetic family is nonconvex in a way that restricts its paratingent cone; the theorem only consumes an anchored comparison; the retained metric encodes additional provenance; or the destination carries nonlinear/relational information not reducible to a bounded linear map on the affine hull.

For Arithmetic Fidelity this separates two future searches cleanly. Boundary geometry remains a viable carrier for source-anchored provenance, while pairwise protection should now be sought in **nonconvex/singular completed-secant geometry or richer destination structure**, not in stronger convex boundary inequalities alone.