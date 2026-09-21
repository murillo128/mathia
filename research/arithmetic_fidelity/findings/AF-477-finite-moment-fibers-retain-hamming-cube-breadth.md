# AF-477 — Finite-moment fibers retain Hamming-cube breadth

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `SOURCE-LAW`, `MOMENT-FIBER`, `SUPPORT-BUDGET`, `NONLINEAR-TARGET`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-460 shows that finitely many bounded linear source constraints cannot make the normalized signed kernel cube-poor, but it leaves two important escape routes open: positivity/support restrictions may stop those signed directions from being physically completable, and its target conclusion is affine. AF-464 removes the affine restriction once an actual source-point Hamming cube is present, while AF-476 makes that obstruction scale-aware for a full soft-compressibility envelope.

For finite generalized-moment fibers, the actual positive source-point cube can be constructed exactly. Finite-dimensional affine side information can reduce the available cube dimension only by a constant factor proportional to its affine rank; it cannot suppress growing metric-cube breadth uniformly over source-law fibers as the support budget grows.

Let `X` be a set and let

\[
\Psi:X\to\mathbb R^q
\]

be any finite-valued feature map. Write

\[
d=\dim\operatorname{aff}\Psi(X)\le q.
\tag{1}
\]

For an integer support budget `r` and a source-law value `u`, define the positive moment fiber

\[
\mathcal F_{r,u}(\Psi)
=
\left\{
\mu\in\operatorname{Prob}_{\mathrm{fin}}(X):
|\operatorname{supp}\mu|\le r,
\ \int\Psi\,d\mu=u
\right\},
\tag{2}
\]

with total-variation / `ell^1` distance

\[
d_1(\mu,\nu)=\|\mu-\nu\|_1.
\]

Fix `k>=1`. If

\[
|X|\ge k(d+2)
\qquad\text{and}\qquad
r\ge k(d+1),
\tag{3}
\]

then there exists a moment value `u_k` for which `\mathcal F_{r,u_k}(\Psi)` contains an exact scaled isometric copy of the `k`-dimensional Hamming cube:

\[
\boxed{
 d_1(\mu_\varepsilon,\mu_\eta)
 =\frac{2}{k}d_H(\varepsilon,\eta),
 \qquad
 \varepsilon,\eta\in\{-1,+1\}^k.
}
\tag{4}
\]

In particular, every cube edge has length `2/k` and every antipodal pair has distance `2`.

Let `Y` have Enflo type `p in [1,2]` with constant `T_p^E(Y)` in the normalization used in AF-464. For any map

\[
F:\mathcal F_{r,u_k}(\Psi)\to Y
\]

with finite upper TV-Lipschitz modulus `L(F)`, at least one antipodal pair of the cube satisfies

\[
\boxed{
 d_Y(F\mu_\varepsilon,F\mu_{-\varepsilon})
 \le
 2T_p^E(Y)L(F)k^{1/p-1}.
}
\tag{5}
\]

Hence for any resolution threshold `0<delta<=2`, the lower modulus

\[
\kappa_\delta(F)
=
\inf_{d_1(\mu,\nu)\ge\delta}
\frac{d_Y(F\mu,F\nu)}{d_1(\mu,\nu)}
\tag{6}
\]

obeys

\[
\boxed{
\kappa_\delta(F)
\le
T_p^E(Y)L(F)k^{1/p-1}.
}
\tag{7}
\]

For Hilbert targets, `p=2` and `T_2^E=1`, so every bi-Lipschitz representation of this fiber satisfies

\[
\boxed{
\frac{L(F)}{\kappa_\delta(F)}\ge\sqrt{k}.
}
\tag{8}
\]

Taking

\[
k=\left\lfloor\frac{r}{d+1}\right\rfloor
\tag{9}
\]

when `X` has enough atoms gives a worst-fiber lower bound. To state it without representation-dependent notation, define

\[
\operatorname{Dist}_{H,\delta}(S)
=
\inf_F\frac{L(F)}{\kappa_\delta(F)},
\tag{10}
\]

where the infimum runs over Hilbert-valued maps with `0<kappa_delta(F)<=L(F)<infinity`, and set the value to `infinity` if no such map exists. Then

\[
\boxed{
\sup_{u:\mathcal F_{r,u}(\Psi)\ne\varnothing}
\operatorname{Dist}_{H,\delta}\bigl(\mathcal F_{r,u}(\Psi)\bigr)
\ge
\sqrt{\left\lfloor\frac{r}{d+1}\right\rfloor}.
}
\tag{11}
\]

Thus a fixed finite number of affine source statistics does not turn large-support positive moment fibers into uniformly Hilbert-thin objects. To keep the worst-fiber condition number bounded as `r` grows, the effective affine rank must itself grow on the support-complexity scale, or the physical source family must impose additional nonconvex, singular, boundary, provenance, or other restrictions that invalidate the full moment-fiber model.

## Exact source-point cube construction

Choose `k` pairwise disjoint blocks

\[
B_j=\{x_{j,1},\ldots,x_{j,d+2}\}
\subset X,
\qquad j=1,\ldots,k.
\tag{12}
\]

All `Psi(B_j)` lie in an affine space of dimension at most `d`. Radon's theorem therefore gives, for each block, two disjoint nonempty parts whose convex hulls intersect. Equivalently, there are mutually singular probability measures `alpha_j` and `beta_j`, both supported inside `B_j`, such that

\[
\int\Psi\,d\alpha_j
=
\int\Psi\,d\beta_j
=:v_j.
\tag{13}
\]

Because the two Radon parts are nonempty and together use at most `d+2` latent atoms,

\[
|\operatorname{supp}\alpha_j|\le d+1,
\qquad
|\operatorname{supp}\beta_j|\le d+1.
\tag{14}
\]

For a sign vector `epsilon in {-1,+1}^k`, set

\[
\gamma_j^{\varepsilon}
=
\begin{cases}
\alpha_j,&\varepsilon_j=+1,\\
\beta_j,&\varepsilon_j=-1,
\end{cases}
\qquad
\mu_\varepsilon
=
\frac1k\sum_{j=1}^k\gamma_j^{\varepsilon}.
\tag{15}
\]

Every `mu_epsilon` is a probability measure. Equations `(13)` and `(15)` give the same source law for every orientation:

\[
\int\Psi\,d\mu_\varepsilon
=
\frac1k\sum_{j=1}^k v_j
=:u_k.
\tag{16}
\]

Equation `(14)` gives

\[
|\operatorname{supp}\mu_\varepsilon|
\le k(d+1)
\le r,
\tag{17}
\]

so all `2^k` vertices are genuine positive members of one fixed moment fiber.

Now let `D` be the set of coordinates on which `epsilon` and `eta` differ. Since the latent blocks are disjoint, and within each block `alpha_j` and `beta_j` are mutually singular,

\[
\begin{aligned}
\|\mu_\varepsilon-\mu_\eta\|_1
&=
\frac1k\sum_{j\in D}
\|\alpha_j-\beta_j\|_1\\
&=
\frac1k\sum_{j\in D}2
=
\frac{2}{k}|D|.
\end{aligned}
\tag{18}
\]

This proves `(4)` exactly. No signed completion, compactness, boundedness of `Psi`, tangent approximation, or limiting argument is involved.

Repeated feature values cause no problem: if two distinct latent atoms in a block have the same `Psi` value, they already supply a singleton-versus-singleton Radon collision. Otherwise the ordinary affine Radon partition applies.

## Enflo-type consequence

Set

\[
f(\varepsilon)=F(\mu_\varepsilon).
\]

A one-coordinate sign flip has source distance `2/k`, so

\[
d_Y(f(\varepsilon),f(\varepsilon^{(j)}))
\le\frac{2L(F)}{k}.
\tag{19}
\]

With

\[
D_jf(\varepsilon)
=\frac{f(\varepsilon)-f(\varepsilon^{(j)})}{2},
\]

we have

\[
\|D_jf(\varepsilon)\|
\le\frac{L(F)}{k}.
\tag{20}
\]

The Enflo-type inequality used in AF-464 gives

\[
\mathbb E_\varepsilon
\left\|
\frac{f(\varepsilon)-f(-\varepsilon)}2
\right\|^p
\le
T_p^E(Y)^p
\sum_{j=1}^k
\mathbb E_\varepsilon\|D_jf(\varepsilon)\|^p
\le
T_p^E(Y)^pL(F)^pk^{1-p}.
\tag{21}
\]

Therefore some antipodal pair satisfies `(5)`. Its source distance is exactly `2`, so it belongs to every lower-modulus test `(6)` with `delta<=2`; dividing `(5)` by `2` proves `(7)`.

For a Hilbert target the diagonal-versus-edges inequality has constant one, yielding `(8)`.

The obstruction is therefore genuinely nonlinear and genuinely physical: it acts on actual positive source points in one prescribed moment fiber, not merely on signed kernel directions or an affine observation map.

## Finite affine side information has a quantitative cost

The support budget in `(3)` makes the source/side-information tradeoff explicit. If `X` is infinite and `r` is large, a finite affine rank `d` leaves a cube of dimension

\[
k\asymp\frac{r}{d+1}
\tag{22}
\]

inside some `r`-sparse fiber. For Hilbert compression the resulting worst-fiber distortion is therefore at least

\[
\sqrt{\frac{r}{d+1}}
\]

up to the integer cutoff.

Equivalently, suppose one wants every nonempty `r`-sparse moment fiber to admit a Hilbert representation with condition number at most `D` at any fixed resolution `delta<=2`. If

\[
r\ge(d+1)(\lfloor D^2\rfloor+1),
\tag{23}
\]

then choosing `k=\lfloor D^2\rfloor+1` contradicts `(8)`. Hence a necessary condition for such a uniform guarantee is

\[
\boxed{
 r<(d+1)(\lfloor D^2\rfloor+1).
}
\tag{24}
\]

The exact integer form is less important than the structural law: **bounded Hilbert conditioning across all sparse moment fibers requires affine side-information dimension proportional to source support complexity.** A fixed finite list of moments cannot provide that protection as `r` grows.

For targets of Enflo type `p>1`, the same argument replaces `D^2` by the corresponding power `(D T_p^E(Y))^{p/(p-1)}`.

## Relation to AF-451, AF-460, AF-461, AF-464, and AF-476

AF-451 identifies fixed affine source-law fibers as the correct physical objects and shows why signed Radon cores must be completed by positive backgrounds before fiberwise conclusions are drawn. AF-460 later proves that finite-rank linear source laws have zero paired-cube defect in their normalized signed kernels, but explicitly leaves positivity, hard support budgets, and physical completion as possible escapes.

AF-477 closes those particular escapes for the **full positive finite-moment fiber**. Independent Radon blocks are not merely signed tangent directions: choosing one side of each block produces `2^k` actual positive laws with exactly the same source moment and a controlled hard support budget.

AF-461 proves a local analogous obstruction for regular finite-dimensional nonlinear source laws, but again through normalized secants and bounded affine downstream observations. AF-477 is different: the source law is affine, yet the target map may be completely nonlinear because the obstruction is an actual metric cube and AF-464 applies directly.

AF-464 is recovered when `d=0`: no source-law statistic is retained, every Radon block consists of two atoms, and `(4)` becomes the ordinary sparse-simplex cube. AF-477 therefore measures exactly how much a finite-dimensional affine source law can reduce that generic cube breadth: at worst it replaces one atom per switch by at most `d+1` atoms.

AF-476 shows that a soft tail envelope can itself force a resolution-dependent cube, but warns that a narrower arithmetic subclass may exclude the private-tail switches. AF-477 supplies a complementary exact certificate: if that subclass is **nothing more than a positive sparse moment fiber of finitely many affine statistics**, the required switches cannot all be excluded. Radon partitions manufacture them inside the physical fiber.

## Prior art and novelty audit

Every external ingredient is classical, and no theorem-level novelty is claimed for Radon's theorem, generalized moment sets, or Enflo-type cube inequalities.

- Johann Radon, **“Mengen konvexer Körper, die einen gemeinsamen Punkt enthalten,”** *Mathematische Annalen* 83 (1921), 113–115. Radon's theorem is exactly the finite-dimensional convex-geometric step behind `(13)`: `d+2` feature points admit two disjoint convex representations of one barycenter.
- Gerhard Winkler, **“Extreme Points of Moment Sets,”** *Mathematics of Operations Research* 13(4), 581–587 (1988), DOI `10.1287/moor.13.4.581`. This is classical prior art for probability-measure sets under finitely many generalized moment constraints and for the sparse affine-independence structure of their extreme points.
- Per Enflo, **“On the nonexistence of uniform homeomorphisms between `L_p`-spaces,”** *Arkiv för Matematik* 8 (1969), 103–105, DOI `10.1007/BF02589549`, and Paata Ivanisvili, Ramon van Handel, and Alexander Volberg, **“Rademacher type and Enflo type coincide,”** *Annals of Mathematics* 192(2), 665–678 (2020), DOI `10.4007/annals.2020.192.2.8`, supply the metric-cube obstruction already used in AF-464.

A fresh literature search also checked current work on the facial geometry of generalized moment problems and modern work on Hamming-cube embedding obstructions. That literature reinforces the two classical sides of the argument—finite moment constraints have well-developed convex/extreme-point theory, and Hamming cubes have classical type-based nonembedding theory—but did not justify treating their combination here as a new general theorem. AF-477 is therefore recorded as a line-specific derived no-go result.

One conceptual distinction is nevertheless important for this research line. Classical moment theory says that extreme points under `d` finite moment constraints are sparse. AF-477 shows that **sparse extreme points do not imply a metrically thin fiber**: by combining independent Radon ambiguities, the same fiber family can contain Hamming cubes whose dimension grows linearly with the allowed support budget. Approximation sparsity and realizable relational breadth are different resources.

No additional external theorem is required beyond the literature already audited by the cited canonical findings; the new content is the exact Radon-block assembly inside one positive support-bounded fiber and its metric-type consequence.

## Boundary and falsification audit

- **Worst-fiber, not every-fiber.** The value `u_k` is constructed from the chosen Radon blocks and may depend on `k`. Some special moment fibers can be singletons or live on low-dimensional boundary faces. AF-477 rules out a uniform guarantee over all fibers; it does not say every prescribed arithmetic fiber contains growing cubes.
- **Full moment-fiber model is substantive.** The theorem assumes every finitely supported positive law satisfying the declared moment and support constraints is admissible. A thinner arithmetic subclass may forbid the convex mixtures in `(15)` through ordering, integrality, provenance, multiplicative compatibility, or another non-moment relation.
- **Finite affine rank is substantive.** If the retained source law has dimension growing with `r`, or is genuinely infinite-dimensional, `(22)` does not force growing cube dimension.
- **No boundedness assumption on `Psi` is needed.** Each Radon step uses only finitely many feature values. This is stronger in that respect than AF-460's compactness argument for bounded finite-rank operators.
- **Hard support is already accounted for.** Every cube vertex uses at most `k(d+1)` atoms. Thus support restriction alone does not remove the obstruction unless the budget is comparable to the source-law dimension or the allowed supports have additional structure.
- **Target upper sensitivity remains load-bearing.** As in AF-464, `(7)` is a stable-fidelity statement. It does not forbid injective encodings with arbitrarily growing or discontinuous sensitivity.
- **TV / `ell^1` geometry is substantive.** The exact Hamming metric in `(18)` uses mutual singularity of the Radon sides and disjoint latent blocks. Another source metric needs its own cube calculation.
- **The affine dimension `d`, not the ambient coordinate count `q`, is the intrinsic parameter.** Redundant source statistics cannot buy fidelity merely by increasing the number of reported coordinates.
- **No prime discriminator is produced.** The theorem says when finite moment side information is insufficient to make the source family compression-friendly. It does not identify a relation that distinguishes rational primes from matched non-prime controls.

## Arithmetic-fidelity consequence

Take `X` to be the rational primes and let `Psi(p)` collect any fixed finite list of real-valued prime marks or generalized moments. If the proposed arithmetic source model is the full class of `r`-sparse probability laws on primes with a prescribed value of those moments, then for every growing support budget there are source-law values whose fibers retain Hamming-cube dimension of order

\[
\frac{r}{\dim\operatorname{aff}\Psi(\mathbb P)+1}.
\]

No arbitrary Lipschitz nonlinear Hilbert representation can preserve TV distinctions on all such fibers with complexity-independent condition number.

This sharpens the current source-side question. A rational-prime discriminator cannot be protected merely by saying that the source also satisfies finitely many affine arithmetic statistics. The protection has to come from structure that makes the **actual prime-derived class thinner than its moment fiber**: a special fixed boundary fiber, nonconvex compatibility across primes, ordering or provenance, an infinite-dimensional/unbounded source law, or another relation that prevents independent Radon switches from being combined.

That gives the local Mind frontier a concrete negative half. The upper approximation profile of an arithmetic class is not enough, but neither can finite moment constraints be invoked abstractly as the missing rigidity. Before such constraints count as an escape from AF-476, one must show exactly which additional arithmetic rule destroys the Radon-block cube inside the actual source class.