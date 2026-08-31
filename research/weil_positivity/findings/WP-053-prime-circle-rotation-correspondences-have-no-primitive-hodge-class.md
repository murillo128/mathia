# WP-053 — Prime-Circle rotation correspondences isolate Mangoldt vertically but have no primitive Hodge class

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the most direct higher-dimensional correspondence escape left open by `WP-052`. Primitive Prime-Circle rotations do admit a literal correspondence model on `P^1 x P^1`: summing the graphs of multiplication by primitive `n`-th roots of unity gives a Galois-invariant divisor whose intersection with the diagonal contains an exact vertical residual supported precisely when `n` is a prime power. Its logarithmic local weight is `Lambda(n)`. However, the same correspondence has no primitive divisor/Hodge class: its class is exactly `phi(n)` times the diagonal, and after subtracting that universal class the correspondence is principal. More sharply, the prime-power residual on the diagonal is itself the **whole vertical fiber** `div(p)`, hence exactly the null/principal direction identified by `WP-011`.

Thus the naive function-field-style upgrade

```text
Prime-Circle primitive rotations
    -> graphs on P^1 x P^1
    -> diagonal intersection
    -> Hodge/intersection positivity
    -> Weil positivity
```

fails even though the diagonal intersection really does remember prime powers. The arithmetic survives only as special-fiber collision data of a genus-zero correspondence; ordinary class-level intersection forgets it. This does **not** rule out a higher-genus or noncommutative/cohomological correspondence canonically forced by Mathia, a secondary/height pairing sensitive to representative-level data, or an infinite-dimensional finite--archimedean coupling with an independent sign theorem.

## 1. The canonical primitive rotation correspondence

Work on the arithmetic threefold

\[
X:=\mathbf P^1_{\mathbf Z}\times_{\mathbf Z}\mathbf P^1_{\mathbf Z}
\]

with homogeneous coordinates `[X_0:X_1]` and `[Y_0:Y_1]`, and affine coordinates

\[
x=X_1/X_0,\qquad y=Y_1/Y_0.
\]

For `n>1`, put

\[
d_n:=\varphi(n).
\]

Over `Qbar`, every primitive `n`-th root `zeta` defines the scalar automorphism

\[
\rho_\zeta:\mathbf P^1\longrightarrow\mathbf P^1,
\qquad x\longmapsto\zeta x,
\]

whose graph is

\[
\Gamma_\zeta:
Y_1X_0-\zeta X_1Y_0=0.
\tag{1}
\]

The Galois-invariant sum of the primitive graphs is cut out over `Z` by the bihomogeneous cyclotomic product

\[
\boxed{
F_n(X,Y)
:=\prod_{\operatorname{ord}(\zeta)=n}
(Y_1X_0-\zeta X_1Y_0)
=(X_1Y_0)^{d_n}
\Phi_n\!\left(\frac{Y_1X_0}{X_1Y_0}\right).
}
\tag{2}
\]

Because `Phi_n` is monic integral, (2) is a primitive integral bihomogeneous polynomial of bidegree `(d_n,d_n)`. Let

\[
Z_n:=V(F_n)\subset X.
\tag{3}
\]

Its generic fiber is exactly

\[
(Z_n)_{\overline{\mathbf Q}}
=\sum_{\operatorname{ord}(\zeta)=n}\Gamma_\zeta.
\tag{4}
\]

This is the most literal way to turn the embedded Prime-Circle primitive shell into a global algebraic correspondence without first collapsing it to the scalar `Phi_n(1)` or to a zeta transform.

## 2. Every primitive rotation graph has the diagonal class

Let `Delta` be the diagonal, with equation

\[
D(X,Y):=Y_1X_0-X_1Y_0=0.
\tag{5}
\]

Both `F_n` and `D^{d_n}` are sections of the same line bundle `O(d_n,d_n)`. Therefore their quotient is a rational function on `X`, and

\[
\boxed{
\operatorname{div}_X\!\left(\frac{F_n}{D^{d_n}}\right)
=Z_n-d_n\Delta.
}
\tag{6}
\]

Consequently

\[
\boxed{[Z_n]=d_n[\Delta]}
\tag{7}
\]

in the ordinary Picard/Chow class group. On the generic surface `P^1 x P^1` this is also immediate from bidegree: every graph of a projective-line automorphism has class `(1,1)`, the same as the diagonal.

Equation (6) is the decisive class-level obstruction. Any ordinary bilinear intersection or Hodge-index form that factors through divisor classes sees `Z_n` only through the scalar `phi(n)`. The normalized correspondence

\[
Z_n-\varphi(n)\Delta
\tag{8}
\]

is not merely isotropic or numerically trivial; it is principal. Thus the cyclotomic distinction between prime powers and other integers cannot live in the primitive Hodge class of this genus-zero correspondence.

This is a genuinely stronger test than the horizontal-divisor obstruction in `WP-052`: the object is now a bona fide correspondence on a product, as in the function-field Weil argument, yet its class still collapses before a sign theorem can see the arithmetic.

## 3. The diagonal intersection nevertheless contains exact Mangoldt support

The loss of class information does **not** mean that the correspondence forgot the prime-power arithmetic as a scheme. Restrict (2) to the diagonal by setting `Y=X`. Every factor becomes

\[
Y_1X_0-\zeta X_1Y_0
=(1-\zeta)X_0X_1.
\]

Hence on `Delta \simeq P^1_Z`,

\[
\boxed{
F_n|_\Delta
=\Phi_n(1)(X_0X_1)^{d_n}.
}
\tag{9}
\]

Because `n>1`, the diagonal is not a component of `Z_n`, so this gives the exact Cartier intersection divisor

\[
\boxed{
Z_n|_\Delta
=d_n[0]+d_n[\infty]
+\sum_p v_p(\Phi_n(1))F_p,
}
\tag{10}
\]

where `F_p` is the whole vertical fiber of `Delta=P^1_Z` above `p`.

The first two terms are universal fixed points of every nontrivial scalar automorphism of `P^1`: `0` and `infinity`. The residual

\[
R_n
:=Z_n|_\Delta-d_n([0]+[\infty])
\tag{11}
\]

is therefore purely arithmetic. The classical cyclotomic identity

\[
\Phi_n(1)=
\begin{cases}
p,&n=p^k,\\
1,&n>1\text{ is not a prime power}
\end{cases}
\tag{12}
\]

gives

\[
\boxed{
R_n=
\begin{cases}
F_p,&n=p^k,\\
0,&\text{otherwise}.
\end{cases}
}
\tag{13}
\]

and therefore its standard logarithmic local weight is

\[
\boxed{
\sum_p v_p(\Phi_n(1))\log p
=\log\Phi_n(1)
=\Lambda(n).
}
\tag{14}
\]

So Prime Circle has produced something closer to the Frobenius-graph picture than `WP-052` alone revealed: **prime-power support appears as the excess intersection of a canonical correspondence with the diagonal after removing universal geometric fixed points.** No zeta zeros, analytic continuation, or hand-picked prime selector are used in (9)--(14).

## 4. The Mangoldt residual is exactly the whole-fiber null direction

The positive-looking correspondence route fails at the next step for an exact reason. On

\[
\Delta\simeq\mathbf P^1_{\mathbf Z},
\]

the residual (11) is itself principal:

\[
\boxed{
R_n
=\operatorname{div}_\Delta(\Phi_n(1)).
}
\tag{15}
\]

In the prime-power case this says simply

\[
\boxed{F_p=\operatorname{div}_\Delta(p).}
\tag{16}
\]

Thus the exact arithmetic term isolated by the diagonal intersection lands in the same whole-fiber direction studied in `WP-011`. That direction is the radical of vertical intersection: for every irreducible component `Gamma` of the fiber,

\[
F_p\cdot\Gamma=0,
\qquad
F_p^2=0.
\tag{17}
\]

On `P^1_Z` the fiber is itself irreducible, so there is not even a nontrivial component-difference quotient behind it. Multiplying its local contribution by `log p` does not change the zero intersection class.

The obstruction is therefore a two-stage collapse:

```text
primitive rotation correspondence Z_n
    |
    +-- generic divisor class
    |      Z_n - phi(n) Delta = principal
    |      -> no primitive Hodge direction
    |
    +-- diagonal excess intersection
           R_n = F_p exactly on n=p^k
           -> Lambda(n) support
           -> whole vertical fiber = div(p)
           -> null/principal for surface intersection
```

The finite arithmetic information is real, but it lives precisely in data that ordinary class-level intersection quotients out.

## 5. Why this differs from the successful function-field Frobenius argument

The classical function-field comparison in `WP-011` uses a curve `C/F_q` and correspondences on `C x C`: the diagonal and graphs of powers of Frobenius. Their intersections encode point counts, while the Hodge index theorem controls a nontrivial primitive correspondence class.

For the Prime-Circle carrier the generic curve is `P^1`, and its cohomological middle piece is absent:

\[
H^1(\mathbf P^1)=0.
\tag{18}
\]

Accordingly, the Neron--Severi group of `P^1 x P^1` contains only the two ruling directions, and every scalar-automorphism graph has the same `(1,1)` class as the diagonal. Equation (6) is the explicit divisor-level manifestation of this genus-zero collapse.

This does not say that correspondences are the wrong idea. It says that **the Mathia-native correspondence supplied by the existing Prime-Circle carrier is cohomologically too thin for the usual Weil/Hodge mechanism**. A successful correspondence route would need Mathia itself to force an additional nontrivial cohomological direction rather than importing a higher-genus curve solely because Frobenius proofs are known to work there.

## 6. Matched control: power-map correspondences escape the rotation class but lose Mangoldt

There is another canonical correspondence already present in the abstract cyclotomic tower: the power map

\[
f_q(x)=x^q,
\qquad q\ge2.
\tag{19}
\]

Its graph is defined over `Z` and has nontrivial degree class, so it does not satisfy the automorphism identity (7). However, its diagonal intersections are the generic fixed points of a degree-`q` map:

\[
x^q=x.
\]

On `G_m` this gives `q-1` roots of unity; after compactification to `P^1`, the fixed points `0` and `infinity` give total intersection number

\[
\boxed{\Gamma_{f_q}\cdot\Delta=q+1.}
\tag{20}
\]

For the `r`-th iterate the same count is `q^r+1`. These are degree/fixed-point counts, not the sparse Mangoldt law.

Moreover, `PC-010` already identifies the roots-of-unity tower together with the maps `z -> z^q` as the classical Bost--Connes cyclotomic semigroup. Passing from the rotation graphs to the power-map graphs therefore trades the exact Prime-Circle prime-power collision (13) for the already-known abstract refinement dynamics. Recovering `log p` or `Lambda` from that semigroup requires additional logarithmic/Euler-product structure of the type already audited in `WP-012`, not a new Hodge sign theorem coming from the graph itself.

This gives a useful matched dichotomy:

\[
\boxed{
\begin{array}{ll}
\text{primitive rotations:}&
\text{exact Mangoldt collision, but primitive graph class }0,\\
\text{power maps:}&
\text{nontrivial degree graph, but generic fixed-point counts and Bost--Connes prior art.}
\end{array}
}
\tag{21}
\]

Neither is the number-field analogue of a Frobenius correspondence whose own intersection geometry both carries the correct arithmetic and supplies the global sign.

## 7. Adversarial controls

### 7.1 Keep the raw effective class instead of subtracting the diagonal

Then (7) says all arithmetic dependence visible to ordinary intersection is reduced to `phi(n)`. For example, every class pairing with a fixed divisor is proportional to `phi(n)`. The prime-power selector in (13) is invisible at that level.

### 7.2 Remove the compactification points `0` and `infinity`

On `G_m`, a nontrivial scalar rotation `x -> zeta x` has no generic fixed point at all. This removes the universal horizontal terms in (10), but it does not create a new primitive class. The arithmetic collision still occurs only in special fibers where primitive roots reduce toward `1`; it remains representative/integral-model data rather than a generic Hodge class.

### 7.3 Blow up the special intersections

Blowing up can convert the collision into exceptional components with nontrivial intersection matrices, but the result depends on extra birational choices unless the Prime-Circle geometry canonically forces a specific resolution. The total transformed fiber remains constrained by the same whole-fiber null relation. Arbitrary blowups therefore manufacture the missing geometry rather than derive it.

### 7.4 Add an Arakelov metric

The canonical completion of the principal residual (15) returns to the product-formula cancellation already established in `WP-052`/`WP-006`. A nonprincipal metric could change the arithmetic Chow class, but then its canonical origin and its relation to the independently selected `q=2` Gamma channel of `WP-048` are exactly the new mathematics that still need to be proved.

### 7.5 Replace `P^1` by a higher-genus carrier

This can create a genuine `H^1` correspondence sector, so it lies outside the obstruction. But no current Prime-Circle construction canonically supplies such a curve. A higher-genus replacement is therefore an escape only if it is derived from Mathia's intrinsic geometry and survives matched controls, not if it is inserted merely to imitate the function-field proof.

## 8. Prior-art and novelty audit

No historical novelty is claimed for the algebraic ingredients.

- The factorization of `Phi_n`, the identity `Phi_n(1)=exp(Lambda(n))`, and scalar root-of-unity rotations are classical and already anchored by `PC-001`--`PC-004`.
- `Pic(P^1 x P^1)=Z^2`, the `(1,1)` class of an automorphism graph, and `H^1(P^1)=0` are standard algebraic geometry. Equation (6) gives the required class collapse directly, so no new general theorem is being claimed.
- The whole-fiber radical/null relation is the standard arithmetic-surface fact already anchored in `SOURCES.md` through Qing Liu and used in `WP-011`.
- The successful function-field Hodge/correspondence comparison is already anchored through Kedlaya in `SOURCES.md` and `WP-011`.
- The power-map/refinement semigroup is already bounded by Bost--Connes and endomotive prior art in `PC-010`, `WP-012`, and `SOURCES.md`.

A directed search for cyclotomic/root-of-unity graph correspondences did not justify any broader novelty claim. The durable Mathia-specific content is the exact synthesis (9)--(17): the most literal correspondence built from the embedded Prime-Circle primitive rotations **does** convert the cyclotomic selector into a diagonal special-fiber collision, but the resulting Mangoldt residual is exactly a principal whole fiber while the generic primitive graph class is already zero.

## 9. Boundary of the obstruction and consequence for the search

This finding rules out the direct chain

```text
primitive root rotations on P^1
    -> ordinary graph correspondences on P^1 x P^1
    -> subtract universal diagonal/fixed-point background
    -> Hodge/intersection positivity.
```

It does **not** rule out:

- a higher-genus or otherwise nontrivial cohomological carrier canonically constructed from Prime Circle, Prime Flute, or Prime Lattice;
- a secondary height/regulator pairing that is deliberately sensitive to principal representative data and has an independent positivity theorem;
- a noncommutative/endomotive enlargement whose relevant cohomology is not ordinary `Pic/NS` of `P^1 x P^1`;
- an infinite-dimensional boundary or singular quotient in which the whole-fiber residual is coupled to the `WP-036`/`WP-048` archimedean response **before** class quotient or finite-part subtraction;
- a genuinely nonseparable finite--archimedean correspondence with its own sign theorem.

The new constraint is sharper than “find a correspondence.” The correspondence must possess a **nontrivial primitive global class or replacement thereof that still retains the special-fiber Mangoldt collision**. The existing genus-zero Prime-Circle rotation geometry has the arithmetic and the correspondence separately, but the ordinary Hodge quotient places them on opposite sides of the same principal/null boundary.

## 10. Exact falsification tests

The core claim is independently checkable by five short calculations.

1. Multiply the primitive graph equations (1) and recover the integral bihomogeneous polynomial (2).
2. Compare bidegrees with `D^{phi(n)}` and verify the principal divisor identity (6).
3. Restrict (2) to the diagonal and verify (9), hence the decomposition (10).
4. Insert the classical values of `Phi_n(1)` and verify that the residual is exactly one whole fiber for every prime power and zero otherwise.
5. On `Delta=P^1_Z`, verify `F_p=div(p)` and the whole-fiber intersection null relation from `WP-011`.

Failure of any of these identities would invalidate the obstruction. Their validity still leaves the escape routes above open, but it prevents treating the obvious primitive rotation graphs on `P^1 x P^1` as the missing Weil-positive correspondence.