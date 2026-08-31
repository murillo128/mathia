# WP-052 — Prime-Circle resultant intersections recover finite Weil rays but their canonical Arakelov completion is principal

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the most direct arithmetic-intersection upgrade of the Prime-Circle chord/resultant kernel. The primitive cyclotomic shells of `PC-001`--`PC-004` admit a literal realization as horizontal divisors on the arithmetic surface `P^1_Z`; their finite intersections have arithmetic degree

\[
\log|\operatorname{Res}(\Phi_m,\Phi_n)|,
\]

so the normalized intersection recovers the same critical prime-ray coefficient `(log p)p^{-k/2}` already found geometrically by Prime Circle. However, the corresponding degree-zero shell divisors are principal, and the same resultant is the norm of a principal element in the cyclotomic shell field. Its canonical Arakelov completion therefore adds an archimedean log-norm term that cancels the finite resultant exactly by the product formula. The resulting arithmetic class is zero before any Hodge/intersection positivity can act.

Thus the route

```text
Prime-Circle primitive shells
    -> horizontal cyclotomic divisors
    -> arithmetic intersection / Arakelov completion
    -> class-level Hodge positivity
    -> global Weil positivity
```

fails in its canonical form. The failure is not that the finite arithmetic coefficient disappears before globalization: it is present exactly as an intersection multiplicity. The failure is that ordinary principal-divisor completion identifies that finite interaction with its compensating archimedean norm, rather than producing the independent Riemann `Gamma_R`/digamma sector needed by the explicit formula.

This finding does **not** rule out a nonprincipal metric forced by another Mathia geometry, a higher-dimensional correspondence, a quotient/compression before passage to divisor classes, or a noncommutative/cohomological enlargement. It rules out treating the ordinary principal Arakelov completion of the cyclotomic shell/resultant geometry as the missing positive global object.

## 1. Primitive Prime-Circle shells are horizontal cyclotomic divisors

Let

\[
X=\mathbf P^1_{\mathbf Z}
\]

with affine coordinate `T`. For `n>1`, define the horizontal divisor

\[
D_n:=V(\Phi_n(T))\subset X.
\tag{1}
\]

Because `Phi_n` is monic and

\[
\mathbf Z[T]/(\Phi_n)\cong\mathbf Z[\zeta_n]
=\mathcal O_{\mathbf Q(\zeta_n)},
\]

this horizontal shell is canonically

\[
D_n\cong\operatorname{Spec}\mathcal O_{K_n},
\qquad K_n=\mathbf Q(\zeta_n).
\tag{2}
\]

Put

\[
d_n=\deg\Phi_n=\varphi(n).
\]

Let `infinity` denote the section at infinity and let

\[
A:=V(T-1)
\]

be the horizontal section corresponding to the common Prime-Circle anchor `1`. On `X`,

\[
\operatorname{div}_X(\Phi_n(T))
=D_n-d_n\,\infty,
\tag{3}
\]

while

\[
\operatorname{div}_X(T-1)=A-\infty.
\tag{4}
\]

Consequently

\[
\boxed{
D_n-d_nA
=
\operatorname{div}_X\!\left(
\frac{\Phi_n(T)}{(T-1)^{d_n}}
\right)
}
\tag{5}
\]

and likewise `D_n-d_n infinity` is principal.

Equation (5) is already a warning for any direct Hodge-index interpretation of the shell classes: after the canonical degree-zero normalization relative to either distinguished section, every primitive shell is the zero class in the ordinary Picard/Chow group of `P^1_Z`. Any class-level bilinear or quadratic form therefore vanishes on these normalized shell directions.

This is the pairwise Prime-Circle analogue of the class-triviality obstruction in `WP-006`, but now the finite data being globalized is the actual cyclotomic interaction kernel rather than an integer exponent vector.

## 2. The Prime-Circle chord resultant is literally finite arithmetic intersection

Take distinct `m,n>1`. The horizontal divisors `D_m` and `D_n` have disjoint generic fibers because `Phi_m` and `Phi_n` are distinct irreducible polynomials. Their scheme-theoretic intersection is therefore vertical and finite.

For two monic polynomials with no common generic root, the standard resultant/intersection identity gives

\[
\boxed{
\widehat{\deg}_{\rm fin}(D_m\cdot D_n)
=\sum_p i_p(D_m,D_n)\log p
=\log|\operatorname{Res}(\Phi_m,\Phi_n)|.
}
\tag{6}
\]

The right-hand side is exactly the Prime-Circle scalar from `PC-002`:

\[
I_{m,n}
:=
\sum_{\zeta\in P_m^*}
\sum_{\eta\in P_n^*}
\log|\zeta-\eta|
=\log|\operatorname{Res}(\Phi_m,\Phi_n)|.
\tag{7}
\]

So the Euclidean chord interaction was not merely analogous to an arithmetic intersection. It is the logarithmic arithmetic degree of the finite intersection of the corresponding horizontal cyclotomic shells.

The anchor case is the same mechanism. Since `Phi_1(T)=T-1`,

\[
\log|\operatorname{Res}(\Phi_1,\Phi_n)|
=\log|\Phi_n(1)|
=\Lambda(n),
\qquad n>1,
\tag{8}
\]

which is precisely `PC-001`.

## 3. Hilbert normalization recovers the finite Weil ray coefficient

Prime Circle normalizes shell interactions by their populations. In the divisor model this means

\[
J_{m,n}
:=
\frac{\widehat{\deg}_{\rm fin}(D_m\cdot D_n)}
{\sqrt{d_md_n}}
=
\frac{\log|\operatorname{Res}(\Phi_m,\Phi_n)|}
{\sqrt{\varphi(m)\varphi(n)}}.
\tag{9}
\]

Suppose

\[
n=mp^k,
\qquad k\ge1.
\]

The classical cyclotomic resultant theorem used in `PC-002`/`PC-004` gives

\[
\log|\operatorname{Res}(\Phi_m,\Phi_{mp^k})|
=\varphi(m)\log p.
\tag{10}
\]

Hence

\[
J_{m,mp^k}
=(\log p)
\sqrt{\frac{\varphi(m)}{\varphi(mp^k)}}.
\tag{11}
\]

If `p|m`, then

\[
\varphi(mp^k)=p^k\varphi(m),
\]

and therefore

\[
\boxed{
J_{m,mp^k}
=\frac{\log p}{p^{k/2}}
=\frac{\Lambda(p^k)}{\sqrt{p^k}}.
}
\tag{12}
\]

Thus the arithmetic-surface interpretation preserves exactly the critical finite Weil coefficient on every interior prime-power ray. No zeta transform, zero data, or analytic continuation is needed.

The known first-birth anomaly also survives exactly. If `p` does not divide `m`, then

\[
\varphi(mp^k)
=p^{k-1}(p-1)\varphi(m),
\]

so

\[
\boxed{
J_{m,mp^k}
=
\sqrt{\frac p{p-1}}
\frac{\log p}{p^{k/2}}.
}
\tag{13}
\]

This matches the endpoint defect isolated later in `WP-034`: the arithmetic intersection realization neither invents nor repairs that boundary normalization.

## 4. The same resultant is the norm of a principal cyclotomic element

Fix `n>1` and a distinct `m`. In the shell field

\[
K_n=\mathbf Q(\zeta_n),
\]

consider the algebraic integer

\[
\alpha_{m,n}:=\Phi_m(\zeta_n)\in\mathcal O_{K_n}.
\tag{14}
\]

Because the embeddings of `K_n` send `zeta_n` through the primitive `n`-th roots,

\[
\begin{aligned}
|N_{K_n/\mathbf Q}(\alpha_{m,n})|
&=
\prod_{\operatorname{ord}(\eta)=n}|\Phi_m(\eta)|\\
&=|\operatorname{Res}(\Phi_n,\Phi_m)|\\
&=|\operatorname{Res}(\Phi_m,\Phi_n)|.
\end{aligned}
\tag{15}
\]

Therefore the finite intersection scalar also has the exact norm descriptions

\[
\boxed{
I_{m,n}
=\sum_{\mathfrak p}
\operatorname{ord}_{\mathfrak p}(\alpha_{m,n})
\log N\mathfrak p
=\log|N_{K_n/\mathbf Q}\alpha_{m,n}|.
}
\tag{16}
\]

On the other hand, summing over the complex embeddings gives

\[
\boxed{
\sum_{\sigma:K_n\hookrightarrow\mathbf C}
\log|\sigma(\alpha_{m,n})|
=\log|N_{K_n/\mathbf Q}\alpha_{m,n}|
=I_{m,n}.
}
\tag{17}
\]

Equations (16)--(17) are decisive for the attempted global completion. The finite intersection and the apparent archimedean chord norm are not two independent local sectors: they are two presentations of the **same principal norm**.

## 5. Canonical Arakelov completion cancels the finite interaction

For a number field `K`, the principal arithmetic divisor of a nonzero element `alpha` consists of its finite valuation divisor together with the negative logarithmic norms at the archimedean embeddings. In the squared-metric convention used by the Arakelov source already audited in `WP-006`, the infinite component is `-log|sigma alpha|^2`, with the corresponding standard half-weight in arithmetic degree. Either normalization gives the product-formula identity

\[
\boxed{
\widehat{\deg}\,\widehat{\operatorname{div}}(\alpha)=0.
}
\tag{18}
\]

Applying this to `alpha_{m,n}` and using (16)--(17), the finite contribution is exactly

\[
+I_{m,n},
\]

while the canonical archimedean principal contribution is exactly

\[
-I_{m,n}.
\]

Thus

\[
\boxed{
\widehat{\deg}\,\widehat{\operatorname{div}}(\alpha_{m,n})
=I_{m,n}-I_{m,n}=0.
}
\tag{19}
\]

Any real scalar normalization, including division by `sqrt(phi(m)phi(n))`, preserves zero. In particular, the operation that turns the finite intersection into the exact interior Weil ray coefficient (12) cannot turn this principal global object into a nonzero positive class.

This is stronger than saying that Arakelov theory is known prior art. It identifies what the canonical Arakelov completion does to the **specific Mathia interaction that already carries the correct critical finite coefficient**: it cancels it.

## 6. Why the cancelling archimedean norm is not the Riemann Gamma sector

It would be tempting to reinterpret the second half of (19) as the missing archimedean contribution. That identification is incorrect.

The archimedean term in (19) is forced only by the product formula for the cyclotomic element `alpha_{m,n}`. It is the negative of the same finite resultant norm and therefore depends on the chosen pair of cyclotomic shells. It supplies no independent `Gamma_R` response, no digamma kernel in the test variable, and no polar term.

Moreover, for `n>2`, the shell field `K_n` is totally complex: its archimedean data consists of the embeddings of a cyclotomic field, whereas the Riemann zeta explicit formula has the single real place of `Q` and its `Gamma(s/2)` factor. The multiplicity and local type are therefore wrong even before a positivity theorem is considered.

This contrasts sharply with `WP-036`/`WP-048`, where Prime Circle independently produced the exact `psi(s/2)` scale and intrinsically selected the order-two channel. The arithmetic intersection completion here does not couple to that structure; it merely performs principal-divisor cancellation.

## 7. Matched control: the obstruction is generic resultant geometry

The cancellation is not cyclotomic-specific. Let `f,g in Z[T]` be monic polynomials with no common generic root. Their horizontal divisors on `P^1_Z` have finite intersection degree

\[
\log|\operatorname{Res}(f,g)|.
\]

If `beta` is a root of `g`, then `f(beta)` has norm equal, up to the standard leading-coefficient convention, to the same resultant. The principal arithmetic divisor of `f(beta)` again has total arithmetic degree zero.

Cyclotomic arithmetic is special because Apostol's resultant theorem makes this generic intersection scalar sparse and produces prime-power support. But **principal globalization does not preserve that sparsity as a nontrivial class**: every such interaction becomes a product-formula zero class.

This is a useful matched control against overinterpreting the exact equality (12). The correct local Weil coefficient is genuinely encoded by the cyclotomic geometry, but the ordinary arithmetic-intersection completion mechanism is universal and does not turn that coefficient into global Weil positivity.

## 8. Prior-art and novelty audit

No historical novelty is claimed for the algebraic ingredients.

- The cyclotomic resultant formula used in (10) is classical and already audited by `PC-002`/`PC-004`.
- Resultants as arithmetic intersection multiplicities of horizontal divisors are standard arithmetic-surface algebra.
- Principal arithmetic divisors, the product formula, and their zero class/zero arithmetic degree are standard Arakelov geometry; the relevant conventions and class-triviality mechanism are already anchored in `research/weil_positivity/SOURCES.md` through Freixas i Montplet and Burgos Gil--Kramer--Kuehn.
- `WP-006` already established the analogous principal-class collapse for Prime-Lattice integer vectors on `Spec Z`.

A directed audit of arithmetic-intersection/resultant literature did not provide a basis for claiming a new general theorem. The durable Mathia-specific result is the **bridge-and-failure synthesis**: the Prime-Circle normalized chord kernel is literally a finite arithmetic-intersection kernel, including its critical half-density on interior prime rays, but the canonical class-level arithmetic completion of exactly that kernel is principal and therefore supplies cancellation rather than an independent positive global pairing.

This also places the route close to the classical Weil-function-field analogy audited in `WP-011`: the successful function-field argument uses nontrivial global correspondences on a surface. Merely converting horizontal point/divisor data into principal classes on an arithmetic surface does not recreate that correspondence geometry.

## 9. Boundary of the obstruction

The result rules out the direct chain

```text
cyclotomic horizontal shells
    -> ordinary finite intersection
    -> principal Arakelov completion
    -> Picard/Chow-class Hodge positivity.
```

It does **not** rule out:

- a nonprincipal Hermitian/Green metric canonically forced by Prime-Circle radial geometry;
- a higher-dimensional cycle or correspondence whose class is not principal;
- a relative pairing evaluated before quotienting by principal divisors, provided a canonical gauge/quotient supplies invariance;
- a compression or cohomological quotient that couples the finite intersection kernel to the `q=2` archimedean channel of `WP-036`/`WP-048` before positivity is taken;
- an infinite-dimensional boundary sector or singular renormalization with its own independent sign theorem;
- an adelic, monoidal, or noncommutative enlargement of ordinary arithmetic Picard geometry.

These are genuine changes of object, not counterexamples to the obstruction. Any such escape must still derive the Riemann Gamma and polar terms from the same geometry and prove nonnegativity independently of RH or inserted zero data.

## 10. Falsification surface

The exact core has short independent checks.

1. Verify `div_X(Phi_n)=D_n-phi(n) infinity` and `div_X(T-1)=A-infinity`, giving the principal shell relation (5).
2. Verify that the local intersection lengths of `D_m,D_n` sum with `log p` weights to `log|Res(Phi_m,Phi_n)|`.
3. Verify the norm identity (15) for `alpha_{m,n}=Phi_m(zeta_n)`.
4. Apply the product formula to obtain the zero arithmetic degree (19).
5. On `n=mp^k`, apply the cyclotomic resultant theorem and the totient ratio to recover (12) when `p|m` and the endpoint factor (13) when `p` does not divide `m`.

Failure of items 1--4 would invalidate the principal-completion obstruction. Failure only of item 5 would invalidate the claimed exact bridge to the Prime-Circle finite Weil coefficient while leaving the generic principal cancellation intact.

## Research consequence

Prime Circle now has an exact arithmetic-surface interpretation at precisely the point where a Weil-style intersection argument would naturally be attempted:

\[
\boxed{
\text{normalized cyclotomic finite intersection}
\supset
\frac{\log p}{p^{k/2}}.
}
\]

But the canonical global arithmetic class containing that intersection is

\[
\boxed{
\text{principal finite resultant}
+\text{principal archimedean norm}
=0.
}
\]

Therefore the next viable intersection/cohomology route cannot simply globalize the primitive shells as ordinary Arakelov divisors. It must create a **nonprincipal global correspondence or relative/cohomological object before the sign theorem is applied**, and it must couple that object intrinsically to the independently discovered Prime-Circle real-place channel rather than identify product-formula cancellation with the Riemann Gamma term.