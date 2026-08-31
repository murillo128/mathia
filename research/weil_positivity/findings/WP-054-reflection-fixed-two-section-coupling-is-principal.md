# WP-054 — the reflection-fixed two-section coupling is principal before Hodge positivity

**Status:** `EXACT-DERIVED + CLASSICAL-CYCLOTOMIC-IDENTITIES + DECISIVE-NEGATIVE`. `WP-048` identified the anchored reflection `z -> conjugate(z)` as an intrinsic Prime-Circle selector of the order-two pair `{+1,-1}` and showed that its even radial field `Log(1-z^2)` carries the real Riemann Gamma/digamma channel after Mellin transformation. `WP-050` and `PC-076` independently found that the same two endpoints produce, respectively, the positive sum and signed difference of the two cyclotomic endpoint masses. The most direct attempt to couple those finite and archimedean facts *before* positivity is therefore to use the two reflection-fixed sections of `P^1_Z` as one arithmetic divisor geometry.

That coupling is exact, but class-trivial. Let

\[
X=\mathbf P^1_{\mathbf Z},
\qquad
A_+=V(T-1),
\qquad
A_-=V(T+1),
\qquad
A_\infty=\{\infty\},
\]

and let

\[
D_n=V(\Phi_n(T)),\qquad n>2,
\]

be the primitive Prime-Circle shell divisor from `WP-052`. Then the finite intersection degrees are

\[
\widehat{\deg}_{\rm fin}(D_n\cdot A_+)=\log\Phi_n(1)=\Lambda(n),
\]

\[
\widehat{\deg}_{\rm fin}(D_n\cdot A_-)=\log\Phi_n(-1)
=\mathbf 1_{2\mid n}\Lambda(n/2).
\]

Consequently the reflection-even and reflection-odd endpoint combinations reproduce *exactly* the two previously discovered arithmetic readouts:

\[
\boxed{
\widehat{\deg}_{\rm fin}\bigl(D_n\cdot(A_++A_-)\bigr)
=\Lambda(n)+\mathbf1_{2\mid n}\Lambda(n/2)
=E_n^{\rm cur}
}
\tag{1}
\]

from `WP-050`, and

\[
\boxed{
\widehat{\deg}_{\rm fin}\bigl(D_n\cdot(A_+-A_-)\bigr)
=\Lambda(n)-\mathbf1_{2\mid n}\Lambda(n/2)
=2\operatorname{Tr}T_n
}
\tag{2}
\]

from `PC-076`.

However, the very two combinations selected by reflection are principal after the unavoidable degree normalization:

\[
\boxed{
A_+-A_-
=\operatorname{div}\!\left(\frac{T-1}{T+1}\right),
}
\tag{3}
\]

and

\[
\boxed{
A_++A_--2A_\infty
=\operatorname{div}(T^2-1).
}
\tag{4}
\]

The even function in (4) is precisely the algebraic divisor underlying the `q=2` field of `WP-048`, since on the affine complex chart

\[
\operatorname{Re}\Log(1-z^2)=\log|1-z^2|
\]

has zeros at the same reflection-fixed pair `{+1,-1}`; changing `1-z^2` to `z^2-1` changes only a constant phase. Thus the most canonical finite-dimensional object that puts the finite endpoint arithmetic and the intrinsically selected `q=2` archimedean field into the **same geometry** is already a principal divisor on `P^1_Z`.

With the canonical Arakelov metric of a principal rational function, the archimedean Green/log-norm contribution cancels its finite intersection contribution by the product formula. Hence no nonzero arithmetic Chow/Picard class remains on which a Hodge/intersection sign theorem could act. Keeping the unnormalized even divisor `A_++A_-` only retains the universal degree-two class; its nonconstant `q=2` content is exactly the principal correction (4). The direct two-section route therefore cannot be the missing nonprincipal finite--archimedean Weil pairing.

This does **not** rule out using the principal potential before passing to divisor classes, equipping it with a noncanonical/nonprincipal metric forced by another Mathia construction, coupling it nonseparably to shell/boundary degrees of freedom, or replacing `P^1` by a space with genuine primitive cohomology. It rules out the narrow but highest-leverage candidate in which the reflection-fixed pair itself is treated as an ordinary arithmetic-divisor/Hodge object.

## 1. The anchored reflection already chooses the two sections

`WP-048` starts from the Prime-Circle anchor `1`. Among Euclidean reflections preserving the unit circle and fixing that anchor, the canonical one is complex conjugation,

\[
j(z)=\bar z.
\]

Its fixed points on the circle are

\[
\{+1,-1\}=\mu_2.
\]

The same finding shows independently, from the cycle Laplacian, that the unique maximal nontrivial mode is the order-two character. The resulting full-root radial field is

\[
V_2(z)=\Log(1-z^2)=\Log(1-z)+\Log(1+z),
\tag{5}
\]

and its Mellin response yields the `q=2` digamma entering the real Riemann Gamma factor after the explicit affine/polar subtraction recorded there.

Equation (5) is important here only at the level of geometric support: the q=2 field is not an externally chosen second endpoint. It is exactly the **reflection-even sum of the anchor and antipode**. Thus if one asks for the smallest algebraic object that might couple the finite Prime-Circle shell arithmetic to the archimedean selector before invoking positivity, the pair of sections `A_+`,`A_-` is forced by the existing Mathia geometry.

## 2. Shell intersection with `+1` gives the ordinary Mangoldt endpoint

For `n>2`, the generic fibers of `D_n` and `A_+` are disjoint, and their scheme-theoretic intersection is finite. Restricting the defining equation `Phi_n(T)` to the section `T=1` gives

\[
D_n\cap A_+
\cong\operatorname{Spec}\bigl(\mathbf Z/(\Phi_n(1))\bigr).
\]

Therefore

\[
\widehat{\deg}_{\rm fin}(D_n\cdot A_+)
=\log|\Phi_n(1)|.
\tag{6}
\]

The classical cyclotomic endpoint identity used throughout Prime Circle is

\[
\Phi_n(1)=
\begin{cases}
p,&n=p^k,\\
1,&n>1\text{ is not a prime power},
\end{cases}
\]

hence

\[
\boxed{
\widehat{\deg}_{\rm fin}(D_n\cdot A_+)=\Lambda(n).
}
\tag{7}
\]

This is the anchor/resultant intersection already present in `WP-052`, now retained as one half of the reflection-fixed pair.

## 3. Shell intersection with `-1` is exactly the dyadic Mangoldt shadow

Likewise, for `n>2`, `Phi_n(-1)` is nonzero and

\[
D_n\cap A_-
\cong\operatorname{Spec}\bigl(\mathbf Z/(\Phi_n(-1))\bigr),
\]

so

\[
\widehat{\deg}_{\rm fin}(D_n\cdot A_-)
=\log|\Phi_n(-1)|.
\tag{8}
\]

The standard cyclotomic parity identities give exactly the classification derived internally in `WP-050` and `PC-076`:

\[
\boxed{
\log\Phi_n(-1)
=\mathbf1_{2\mid n}\Lambda(n/2),
\qquad n>2,
}
\tag{9}
\]

with `Lambda(1)=0`.

Concrete controls are

\[
\begin{array}{c|c|c}
n&\log\Phi_n(1)&\log\Phi_n(-1)\\ \hline
3&\log3&0\\
4&\log2&\log2\\
6&0&\log3\\
9&\log3&0\\
10&0&\log5\\
12&0&0.
\end{array}
\tag{10}
\]

Thus the antipodal mass is not an arbitrary correction. It is the exact false-support term that appears when the canonical reflection-odd cycle current is made positive in `WP-050`.

## 4. Even and odd section combinations recover the two operator formulas exactly

By bilinearity of finite intersection degree, equations (7)--(9) give

\[
\widehat{\deg}_{\rm fin}\bigl(D_n\cdot(A_++A_-)\bigr)
=\Lambda(n)+\mathbf1_{2\mid n}\Lambda(n/2).
\tag{11}
\]

But `WP-050` proved independently that the positive current energy

\[
E_n^{\rm cur}
:=\frac12\log\det(4D^2|_{H_n})
\]

has exactly the right-hand side of (11). Hence

\[
\boxed{
E_n^{\rm cur}
=\widehat{\deg}_{\rm fin}\bigl(D_n\cdot(A_++A_-)\bigr).
}
\tag{12}
\]

Similarly,

\[
\widehat{\deg}_{\rm fin}\bigl(D_n\cdot(A_+-A_-)\bigr)
=\Lambda(n)-\mathbf1_{2\mid n}\Lambda(n/2).
\tag{13}
\]

`PC-076` proved that its canonical Hardy/Hilbert trace-class remainder satisfies

\[
\operatorname{Tr}T_n
=\frac12\left(\Lambda(n)-\mathbf1_{2\mid n}\Lambda(n/2)\right),
\]

therefore

\[
\boxed{
2\operatorname{Tr}T_n
=\widehat{\deg}_{\rm fin}\bigl(D_n\cdot(A_+-A_-)\bigr).
}
\tag{14}
\]

The positive current determinant and the signed Hardy relative trace are therefore not merely analogous endpoint formulas. They are the **even and odd finite intersection channels of the same reflection-fixed two-section divisor algebra**.

This is a useful synthesis because it identifies the smallest shared geometric carrier of three previously separate observations:

```text
q=2 Riemann-Gamma selector (WP-048):   A_+ + A_-  at the potential/support level
positive cycle-current endpoint sum:  D_n · (A_+ + A_-)
signed Hardy endpoint difference:     D_n · (A_+ - A_-)
```

The next question is whether this carrier has any nontrivial class on which positivity could act.

## 5. Both nonconstant reflection channels are principal on `P^1_Z`

The answer is no for ordinary divisor/intersection geometry. On `P^1_Z`, the rational functions

\[
f_-(T)=\frac{T-1}{T+1},
\qquad
f_+(T)=T^2-1
\]

have divisors

\[
\operatorname{div}(f_-)=A_+-A_-,
\tag{15}
\]

and

\[
\operatorname{div}(f_+)=A_++A_--2A_\infty.
\tag{16}
\]

Thus the reflection-odd direction is exactly zero in the divisor class group, while the reflection-even pair differs from the universal degree-two class `2A_infinity` by a principal divisor.

Equivalently, the only ordinary Picard information retained by

\[
aA_+ + bA_-
\]

is its total degree `a+b`. The genuinely reflection-sensitive direction `a=-b` is principal, and after removing the universal degree from the even direction `a=b`, that direction is principal as well. This is the explicit two-point manifestation of the genus-zero fact behind `WP-052` and `WP-053`: `P^1` has no primitive/Jacobian degree-zero divisor class in which the endpoint contrast could live.

This is stronger than merely observing that `A_+` and `A_-` are linearly equivalent. It says that **both exact arithmetic combinations already found by the Mathia operators occupy principal directions** once one removes the universal degree.

## 6. The q=2 field is the same principal even direction, not a new Hodge class

Equation (5) gives

\[
V_2(z)=\Log(1-z^2).
\]

The rational function in (16) is `T^2-1=-(1-T^2)`. Therefore, on the complex affine chart away from its zeros,

\[
\operatorname{Re}V_2(z)=\log|1-z^2|
=\log|z^2-1|.
\tag{17}
\]

So the exact two-point support whose radial/Mellin response selects the real Gamma channel in `WP-048` is the archimedean logarithmic potential of the same principal even divisor (16).

This does **not** mean that the Mellin digamma formula of `WP-048` is itself an arithmetic intersection number. It means something narrower and more useful for the present audit: promoting the q=2 endpoint pair to an ordinary global divisor class supplies no new primitive class. The divisor whose complex logarithmic potential underlies that channel is already principal.

Under the canonical Arakelov completion of a principal rational function, one adjoins precisely its archimedean log-norm/Green component. The principal arithmetic divisor is zero in the arithmetic Chow/Picard group, and its arithmetic degree/intersection with a completed class vanishes by the product formula. This is the same mechanism audited in `WP-006` and `WP-052`.

Hence, for the odd channel, the finite value (13) is canceled by the archimedean contribution of `f_-`; for the normalized even channel, the finite value associated with (16) is canceled by that of `f_+`. Ordinary Hodge/intersection positivity sees the resulting class as zero.

The cancellation should not be confused with the Riemann Gamma term. The canonical principal Green metric is forced by the rational function/product formula, whereas `WP-048` obtains the Riemann digamma by a Mellin transform plus explicit affine/polar subtraction. Merely declaring the principal Arakelov Green term to be the desired Gamma sector would therefore be another repackaging, not a derived Weil bridge.

## 7. Matched controls and attempts to rescue the route

### Keep the even divisor without degree normalization

One can avoid (16) by keeping `A_++A_-` itself. But then its class is just

\[
[A_++A_-]=2[A_\infty].
\]

Any ordinary class-level intersection/Hodge readout sees only this universal degree-two class and forgets which two points were selected. The reflection/q=2 content resides in the principal difference (16), exactly the part discarded by passage to the class.

### Use the odd divisor directly

The odd combination has degree zero from the start, so there is no universal class to retain:

\[
[A_+-A_-]=0.
\]

Its nonzero finite shell intersection (13) is representative-level data and is canceled in canonical arithmetic intersection. This is the same type of warning as `WP-053`: finite special-fiber collisions can be real while the ordinary global class carrying them is null.

### Add the critical half-density `n^{-1/2}`

Multiplying the shell readout by `n^{-1/2}` produces the desired critical attenuation on the finite coefficients, but a scalar normalization cannot turn the zero divisor class (15) or (16) into a nonzero Hodge direction. The class-triviality obstruction survives unchanged.

### Replace canonical metrics by a special metric

A principal divisor equipped with a deliberately changed metric can define nonzero arithmetic data. That is outside this no-go. For such a rescue to count, however, the metric must be forced independently by Mathia geometry and must derive both the finite and Riemann archimedean terms with an independent sign theorem. Choosing a metric to insert the known Gamma factor would violate the research mandate.

### General anchored-circle control

The two-section principal identities (15)--(16) are not arithmetic-specific. Any two marked rational points on `P^1` differ by a principal degree-zero divisor, and any degree-two pair differs from `2 infinity` by a principal divisor. Thus the q=2 reflection carrier remains class-trivial in matched genus-zero controls. The arithmetic content enters through the cyclotomic shell intersections, not through a special nonprincipal endpoint class.

## 8. Prior-art and novelty audit

No theorem-level novelty is claimed for any external ingredient. The endpoint values `Phi_n(1)` and `Phi_n(-1)` are classical cyclotomic identities; `Pic(P^1)` being degree-generated and degree-zero divisors being principal is standard algebraic geometry; and canonical arithmetic principal divisors/product-formula cancellation is standard Arakelov theory already anchored in `SOURCES.md` (Freixas i Montplet; Burgos Gil--Kramer--Kuehn). `WP-052` already established the broader warning that normalized Prime-Circle shell divisors are principal, and `WP-053` established the analogous failure for genus-zero rotation correspondences.

The durable new content is the **Mathia-internal identification and falsification of a specific remaining bridge**: the same intrinsically selected `{+1,-1}` pair simultaneously carries

1. the `q=2` archimedean potential support of `WP-048`,
2. the positive endpoint sum of `WP-050`, and
3. the signed endpoint difference of `PC-076`,

yet both of its reflection-sensitive divisor channels are principal before any ordinary Hodge/intersection positivity can act.

Targeted literature searches for the exact Prime-Circle synthesis of the two cyclotomic endpoint readouts with a q=2 reflection-fixed Arakelov/Hodge coupling did not identify an authoritative source asserting this specialization. That absence is **not** treated as evidence of mathematical novelty; the finding is retained as an internal structural obstruction and portfolio-narrowing result.

## 9. Falsification surface

The claim has six direct failure points.

1. For `n>2`, the finite intersections with `A_+` and `A_-` must have arithmetic degrees `log Phi_n(1)` and `log Phi_n(-1)` with no missing multiplicity.
2. The classical endpoint identities must give `Lambda(n)` and `1_{2|n}Lambda(n/2)` with the stated convention.
3. `WP-050` must use the endpoint **sum** with exactly the normalization in (12).
4. `PC-076` must use one half of the endpoint **difference**, as in (14).
5. The divisor identities (15)--(16) must hold on `P^1_Z`; they are immediate from the rational functions displayed.
6. The scope must remain class-level: a pre-quotient secondary functional or a noncanonical metric is not ruled out by principal-divisor triviality.

The exceptional shell `n=2` is deliberately excluded from the intersection formulas above because `D_2=A_-`, so the `-1` intersection becomes improper/self-intersection rather than the finite endpoint calculation used for `n>2`. This does not affect the obstruction: order two is the fixed endpoint/archimedean selector itself, while the question is whether higher primitive shells acquire a nontrivial global class through that selector.

## Research consequence

The most obvious attempt to realize the current portfolio target — **couple the finite Mangoldt selector and the intrinsically selected q=2 archimedean channel before positivity** — now has an exact genus-zero obstruction:

\[
\boxed{
\begin{array}{c}
\text{reflection-fixed pair }\{+1,-1\}\\
\Downarrow\\
\text{finite even/odd shell intersections}
=\Lambda(n)\pm\mathbf1_{2\mid n}\Lambda(n/2)\\
\Downarrow\\
A_+-A_-\text{ and }A_++A_--2A_\infty\text{ are principal}\\
\Downarrow\\
\text{canonical Arakelov/Hodge class}=0.
\end{array}
}
\]

So the coincidence exposed by `WP-048`, `WP-050`, and `PC-076` is real and geometrically unified, but **ordinary two-section divisor geometry is too small to turn it into global Weil positivity**.

A viable continuation must leave this principal genus-zero category before the sign theorem is invoked. The remaining credible forms include a nonprincipal metric forced by another Mathia structure, a higher-genus/higher-dimensional correspondence with genuine primitive cohomology, a representative-sensitive secondary/height pairing prior to Chow quotient, a noncommutative/cohomological enlargement, or an infinite-dimensional/nonseparable finite--archimedean boundary coupling. Any such route must still derive the Riemann Gamma/polar terms and the finite `Lambda(p^k)/sqrt(p^k)` structure from the same object rather than insert them after the fact.