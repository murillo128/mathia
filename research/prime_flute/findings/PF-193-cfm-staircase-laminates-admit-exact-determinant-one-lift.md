# PF-193 — CFM staircase laminates admit an exact determinant-one lift

**Status:** `LITERATURE+DERIVED + EXACT-ALGEBRA + ROUTE-BOUNDARY`. PF-192 shows that generic strong-`L^1` geometric rigidity fails at the endpoint, but leaves open whether the exact-area constraint present in the PF-184 collar germ could by itself remove the bad laminate mechanism. At the level of finite-order laminates, it does not. The Conti--Faraco--Maggi staircase can be transported split-by-split into `SL(2,R)` by an explicit product-of-shears map that preserves every horizontal/vertical rank-one split and its barycenter. The resulting determinant-one laminates retain an arbitrarily large ratio between distance from every single rotation and integrated pointwise distance to `SO(2)`, even while their support is forced into an arbitrarily small neighborhood of the identity. This is a matrix/laminate statement, **not yet a map-level incompressible counterexample**: realizing the transported laminate by gradients with `det Du=1` while preserving the quantitative ratio remains a separate constrained-convex-integration gate.

## Claim

Write

\[
G_{\alpha,\beta}
=
\begin{pmatrix}
0&\alpha\\
\beta&0
\end{pmatrix}.
\tag{1}
\]

Conti--Faraco--Maggi construct finite-order laminates `nu_n` supported on multiples of the symmetric and antisymmetric matrices

\[
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\tag{2}
\]

with

\[
\int G\,d\nu_n(G)=G_{1,1},
\qquad
\int |\operatorname{sym}G|\,d\nu_n(G)=|G_{1,1}|,
\qquad
M_n:=\int|G|\,d\nu_n(G)\longrightarrow\infty.
\tag{3}
\]

For `epsilon>0` define on the `(alpha,beta)` parametrization

\[
\boxed{
\Phi_\varepsilon(\alpha,\beta)
=
\begin{pmatrix}
1+\varepsilon^2\alpha\beta&\varepsilon\alpha\\
\varepsilon\beta&1
\end{pmatrix}
=
\begin{pmatrix}1&\varepsilon\alpha\\0&1\end{pmatrix}
\begin{pmatrix}1&0\\\varepsilon\beta&1\end{pmatrix}.
}
\tag{4}
\]

Then:

1. `det Phi_epsilon(alpha,beta)=1` exactly;
2. `Phi_epsilon` is affine separately in `alpha` and `beta`;
3. every constant-`alpha` or constant-`beta` rank-one split used in the CFM staircase is sent to a rank-one split with the **same weights and exact barycenter**;
4. therefore

\[
\mu_{n,\varepsilon}:=(\Phi_\varepsilon)_\#\nu_n
\tag{5}
\]

is a finite-order laminate supported in `SL(2,R)`, with barycenter `Phi_epsilon(1,1)`.

Moreover, for every `K>0` and every neighborhood `U` of the identity in `SL(2,R)`, there are `n` and sufficiently small `epsilon` such that `supp(mu_{n,epsilon}) subset U` and

\[
\boxed{
\inf_{Q\in SO(2)}
\int |A-Q|\,d\mu_{n,\varepsilon}(A)
>
K
\int \operatorname{dist}(A,SO(2))\,d\mu_{n,\varepsilon}(A).
}
\tag{6}
\]

Thus no uniform strong-`L^1` rigidity inequality of the form (6) with the opposite inequality and a fixed constant can hold for **finite-order laminate measures supported in determinant one**, even arbitrarily close to the identity.

## 1. The determinant-one lift preserves the complete CFM lamination tree

The exact determinant statement in (4) is immediate either by expansion or by the shear factorization. More importantly, for fixed `beta`,

\[
\Phi_\varepsilon(\alpha,\beta)
-
\Phi_\varepsilon(\alpha',\beta)
=
(\alpha-\alpha')
\begin{pmatrix}
\varepsilon^2\beta&\varepsilon\\
0&0
\end{pmatrix},
\tag{7}
\]

which has rank one. For fixed `alpha`,

\[
\Phi_\varepsilon(\alpha,\beta)
-
\Phi_\varepsilon(\alpha,\beta')
=
(\beta-\beta')
\begin{pmatrix}
\varepsilon^2\alpha&0\\
\varepsilon&0
\end{pmatrix},
\tag{8}
\]

which also has rank one.

Because (4) is separately affine, if a CFM node is split along one of these directions, for example

\[
(\alpha,\beta)
=\lambda(\alpha_1,\beta)
+(1-\lambda)(\alpha_2,\beta),
\tag{9}
\]

then

\[
\Phi_\varepsilon(\alpha,\beta)
=\lambda\Phi_\varepsilon(\alpha_1,\beta)
+(1-\lambda)\Phi_\varepsilon(\alpha_2,\beta)
\tag{10}
\]

with exactly the same `lambda`. The identical statement holds for a vertical split. Induction on the finite lamination order therefore transports the whole staircase, not merely its terminal support. In particular the determinant constraint introduces no barycentric incompatibility: every node and every leaf lies in `SL(2,R)` and the root is `Phi_epsilon(1,1)`, also of determinant one.

This is stronger than simply projecting terminal matrices onto `SL(2)`. Projection would generally destroy the rank-one tree and hence the laminate structure. Equation (4) preserves the exact splitting geometry that drives the CFM endpoint construction.

## 2. The large strong-`L^1` ratio survives the nonlinear lift

For a matrix in the original support, abbreviate

\[
B(G_{\alpha,\beta})=\alpha\beta E_{11}.
\tag{11}
\]

Then

\[
\Phi_\varepsilon(\alpha,\beta)
=I+\varepsilon G_{\alpha,\beta}
+\varepsilon^2 B(G_{\alpha,\beta}).
\tag{12}
\]

Fix `n`. Its support is finite, so all moments and the maximum of `|G|+|B(G)|` are finite. CFM use the local Taylor estimate

\[
\operatorname{dist}(I+F,SO(2))
\le
|\operatorname{sym}F|+c|F|^2
\tag{13}
\]

for small `F`. Applying it to (12), integrating against `nu_n`, and using (3) gives

\[
D_{n,\varepsilon}
:=
\int\operatorname{dist}(A,SO(2))\,d\mu_{n,\varepsilon}(A)
\le
\varepsilon |G_{1,1}|+C_n\varepsilon^2.
\tag{14}
\]

The numerator has a complementary lower bound. For any `Q in SO(2)` put

\[
F_Q=\frac{Q-I}{\varepsilon}.
\tag{15}
\]

Then by (12) and the triangle inequality,

\[
\int |A-Q|\,d\mu_{n,\varepsilon}(A)
\ge
\varepsilon
\int|G-F_Q|\,d\nu_n(G)
-
\varepsilon^2 B_n,
\tag{16}
\]

where `B_n=int |B(G)| dnu_n<infinity`. Hence

\[
N_{n,\varepsilon}
:=
\inf_{Q\in SO(2)}\int |A-Q|\,d\mu_{n,\varepsilon}(A)
\ge
\varepsilon A_n-\varepsilon^2B_n,
\tag{17}
\]

with

\[
A_n:=\inf_{F\in\mathbb R^{2\times2}}
\int|G-F|\,d\nu_n(G).
\tag{18}
\]

The CFM growth of `M_n` forces `A_n` to diverge. Indeed the fixed barycenter in (3) gives, for every `F`,

\[
|F-G_{1,1}|
\le
\int|F-G|\,d\nu_n(G),
\tag{19}
\]

and therefore

\[
M_n
\le
\int|G-F|\,d\nu_n+|F|
\le
2\int|G-F|\,d\nu_n+|G_{1,1}|.
\tag{20}
\]

Thus

\[
\boxed{
A_n\ge\frac{M_n-|G_{1,1}|}{2}\longrightarrow\infty.
}
\tag{21}
\]

For fixed `n`, sending `epsilon` to zero in (14)--(17) makes the quadratic errors negligible, while (21) allows the leading numerator coefficient to be arbitrarily larger than the fixed leading denominator coefficient. Choosing `n` first and then `epsilon` proves (6). The same small-`epsilon` choice puts the finite support of `mu_{n,epsilon}` inside any prescribed neighborhood of `I`.

## 3. What this does and does not say about the PF endpoint splice

PF-192 left several possible ways in which the prime-flute's additional structure might evade generic strong-`L^1` failure. PF-193 removes one tempting explanation at the **laminate geometry** level: exact determinant one does not delete the CFM staircase, does not break its rank-one splits, and does not bound its strong-`L^1` rigidity ratio. Incompressibility alone therefore supplies no matrix-space reason for a generic strong endpoint estimate.

This matters because PF-184 already makes the canonical collar germ exact area-preserving. A future proof of a strong endpoint PF-183 splice cannot plausibly cite `det dH=1` by itself as the missing coercive ingredient. It must use further structure absent from the lifted laminate, such as the PF-142 reflection marking, zero annular flux/exactness beyond pointwise determinant, fixed-germ target confinement, boundary behavior, or special regularity of the canonical PF-179--PF-184 map. The alternative weak/Lorentz endpoint route remains naturally aligned with CFM's surviving weak-`L^1` rigidity remark and with PF-189's weak-trace operator endpoint.

There is, however, a genuine gate between this finding and a map-level no-go theorem. A finite-order laminate measure supported in `SL(2)` is not automatically the gradient distribution of a globally admissible exact-area annulus diffeomorphism with the PF marking. Standard unconstrained laminate realization permits small transition regions that need not remain in `SL(2)`. The determinant constraint must be preserved during realization, not merely on the ideal laminate leaves.

## Prior art and novelty assessment

**S. Conti, D. Faraco, F. Maggi**, *A new approach to counterexamples to `L^1` estimates: Korn's inequality, geometric rigidity, and regularity for gradients of separately convex functions*, Archive for Rational Mechanics and Analysis **175** (2005), 287--300. DOI `10.1007/s00205-004-0350-5`. Their Lemmas 2--3 provide the staircase laminates and the fixed symmetric-mass/diverging total-mass properties used in (3); their nonlinear argument also supplies the local Taylor estimate (13). PF-193 does not claim novelty for those ingredients.

**W. Pompe**, *Explicit Construction of Piecewise Affine Mappings with Constraints*, Bulletin of the Polish Academy of Sciences. Mathematics **58** (2010), 209--220. DOI `10.4064/ba58-3-4`. Pompe develops explicit piecewise-affine convex-integration constructions with constraints and explains a determinant-one modification producing maps with `det Du=1`. This is important nearby prior art, but the present audit did **not** establish that a theorem there realizes the specific lifted CFM staircase while preserving the quantitative ratio (6). PF-193 therefore does not import a map-realization conclusion from Pompe.

A targeted search did not locate an authoritative source stating the exact split-preserving lift (4) for the CFM staircase or the quantitative laminate conclusion (6). That absence is not a novelty claim. The shear factorization and split transport are elementary exact algebra; the project-specific contribution is to isolate their consequence for the live PF endpoint gate without conflating laminate compatibility with realization by the canonical collar maps.

## Falsification and boundary checks

PF-193 would be overclaimed if read as any of the following, none of which is asserted:

- there already exists a Lipschitz or smooth `u` on the PF collar with `det Du=1` that violates strong-`L^1` geometric rigidity;
- the lifted laminate can be realized with identity boundary data, PF reflection marking, zero flux, or fixed target confinement;
- the actual PF-179--PF-184 germ contains CFM-type oscillations;
- strong `W^{1,1}` rigidity is impossible on the **canonical** PF map class;
- weak-`L^1` geometric control is sufficient by itself for the exact-symplectic cutoff or global weak-`S_1` resolvent reassembly.

A decisive strengthening would prove a determinant-preserving realization theorem for `mu_{n,epsilon}` with transition error small enough that (6) survives; that would turn the laminate obstruction into an exact-area map-level counterexample. Conversely, a theorem showing that the additional PF marking/exact-flux/canonical-germ conditions forbid every such realization would identify precisely which extra structure rescues the strong endpoint route.

## Consequences for the research line

The endpoint conservative-splice problem is now separated into a sharper hierarchy. **Pointwise exact area is not enough at the rank-one/laminate level.** Any strong-`L^1` PF-specific estimate must use structure beyond determinant one, while the weak/Lorentz endpoint remains the generic surviving scale. This does not settle the PF-183 splice, but it prevents the current program from treating incompressibility as an automatic cure for PF-192 and provides a concrete falsifier for any future endpoint proof that uses only local determinant-one strain geometry.