# AF-018 — Order-one reflection rigidity reduces a zero-divisor fiber to scale

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`

## Claim

Let `c in C`, and let `f` and `g` be nonzero entire functions of finite order at most one with the same zero divisor, including multiplicities.

Hadamard factorization implies that there exist `a,b in C` such that

\[
\boxed{g(s)=e^{as+b}f(s).}
\]

Thus, inside the class of entire functions of order at most one, the zero divisor leaves exactly an exponential-linear zero-free ambiguity.

If both functions additionally satisfy the same reflection equation

\[
f(s)=f(c-s),\qquad g(s)=g(c-s),
\]

then necessarily `a=0`, so

\[
\boxed{g(s)=C f(s),\qquad C\in\mathbb C^*.}
\]

Finally, if one nonzero normalization value is retained at any point `s_0` outside the common zero divisor,

\[
f(s_0)=g(s_0)\ne0,
\]

then `C=1` and hence

\[
\boxed{f=g.}
\]

The hierarchy is sharp in this admissible category:

1. the divisor plus the order bound alone cannot remove the `e^{as+b}` freedom;
2. one point normalization without reflection still leaves the nonconstant family `e^{a(s-s_0)}f(s)`;
3. reflection without normalization still leaves arbitrary nonzero constant multiples;
4. reflection plus one nonzero normalization value determines the exact function.

Therefore a zero divisor that is non-faithful in a broad meromorphic category can become faithful after adding independently justified global constraints. The relevant lift is not another collection of zeros: it is the admissible analytic class itself.

## Derivation

### Hadamard factorization identifies the complete zero-free fiber

Hadamard's factorization theorem states that a nonzero entire function of finite order `rho` is a canonical product over its zeros multiplied by `e^{Q(s)}`, where `Q` is a polynomial of degree at most `rho`.

Because `f` and `g` have the same zeros with the same multiplicities, choose the same canonical product `P(s)` for both. Since both orders are at most one,

\[
f(s)=e^{Q_f(s)}P(s),\qquad
 g(s)=e^{Q_g(s)}P(s),
\]

with `Q_f` and `Q_g` polynomials of degree at most one. Hence

\[
\frac{g(s)}{f(s)}
=e^{Q_g(s)-Q_f(s)}
=e^{as+b}
\]

for suitable constants `a,b`.

This is stronger than merely saying that two same-zero entire functions differ by a nonvanishing entire factor. The finite-order assumption rigidifies the full zero-free fiber to a finite-dimensional exponential gauge.

It is also sharp. For any entire `f` of order at most one and any `a,b in C`,

\[
g(s)=e^{as+b}f(s)
\]

has exactly the same zero divisor and remains of order at most one. Thus the divisor alone cannot distinguish any of these functions inside the declared class.

### Reflection symmetry kills the linear exponential slope

Assume now

\[
f(s)=f(c-s),\qquad g(s)=g(c-s).
\]

For the quotient

\[
h(s)=\frac{g(s)}{f(s)}=e^{as+b},
\]

the common reflection law gives

\[
h(s)=h(c-s).
\]

Therefore

\[
e^{as+b}=e^{a(c-s)+b},
\]

so

\[
e^{a(2s-c)}=1
\]

for every complex `s`. Differentiating this identity yields

\[
2a\,e^{a(2s-c)}=0,
\]

and hence `a=0`. Thus `h` is constant and

\[
g=Cf
\]

for some `C != 0`.

The surviving constant is unavoidable. Multiplying any reflection-symmetric `f` by a nonzero scalar preserves its zero divisor, order, and reflection equation.

### One normalization kills the remaining scale

Let `s_0` be any point outside the common zero divisor and suppose

\[
f(s_0)=g(s_0)\ne0.
\]

Since `g=Cf`, evaluation at `s_0` gives

\[
C f(s_0)=f(s_0),
\]

so `C=1` and `g=f` identically.

This final datum is minimal at the level of cardinality of the residual gauge: after reflection, the entire ambiguity is one nonzero complex scalar, so one independently fixed nonzero value suffices to remove it.

### Why normalization alone is not an alternative to reflection

Fix `s_0` with `f(s_0) != 0`. For every `a in C`, define

\[
g_a(s)=e^{a(s-s_0)}f(s).
\]

Then `g_a` has the same zero divisor as `f`, has order at most one, and satisfies

\[
g_a(s_0)=f(s_0).
\]

Unless `a=0`, it is a different function. Thus a single scalar normalization does not by itself recover an order-one entire function from its zeros. Reflection is doing genuine structural work: it removes the linear part of the zero-free exponential factor before the scalar normalization removes the constant part.

## Riemann xi application

Riemann's completed xi-function is

\[
\xi(s)=\frac12 s(s-1)\Gamma\!\left(\frac{s}{2}\right)\pi^{-s/2}\zeta(s).
\]

Classically, `xi` is an entire function of order one and satisfies

\[
\xi(s)=\xi(1-s).
\]

Its zeros are exactly the nontrivial zeros of the Riemann zeta function, with multiplicity. Therefore, in the declared admissible class

\[
\mathcal A=
\{F:\ F\text{ entire of order }\le1,\ F(s)=F(1-s)\},
\]

the nontrivial zeta zero divisor determines `xi` up to one nonzero scalar. Retaining one normalization such as

\[
\xi(0)=\frac12
\]

fixes that scalar and determines the exact completed function.

Once the exact `xi` function and its fixed completion convention are known, the Riemann zeta function is recovered meromorphically by

\[
\zeta(s)
=
\frac{2\,\pi^{s/2}\xi(s)}{s(s-1)\Gamma(s/2)}.
\]

In `Re(s)>1`, AF-017 then applies: the exact Euler-product function determines the prime Dirichlet sum by Möbius inversion and hence determines the unordered rational-prime norm multiset.

So, under this full chain of admitted structure,

\[
\begin{aligned}
&\text{nontrivial zero divisor}
+\text{order-one entire class}
+\text{reflection }s\leftrightarrow1-s\\
&\qquad+\text{one normalization}
+\text{fixed completion convention}\\
&\qquad\Longrightarrow \xi
\Longrightarrow \zeta
\Longrightarrow \{p:p\text{ rational prime}\}\text{ as a norm multiset}.
\end{aligned}
\]

This is a **constraint-assisted recovery theorem**, not a statement that the zero set alone contains all prime information in an unrestricted category.

## Relation to AF-017 and Arithmetic Fidelity

AF-017 showed that two adjacent representations have opposite fidelity behavior:

\[
\text{exact Euler-product values}
\longrightarrow
\text{zero/pole divisor}.
\]

The exact Euler-product function retains the generator-norm multiset, whereas the divisor does not: Grosswald--Schnitzer can change the Euler-product generators while preserving the zeta zero divisor in their continuation domain, with the change absorbed by a holomorphic nonvanishing factor.

The present finding identifies what happens after declaring a much narrower analytic category. For entire functions of order at most one, Hadamard factorization reduces the arbitrary zero-free factor to `e^{as+b}`. A common reflection equation removes `a`; one normalization removes `b` modulo the exponential, leaving no residual freedom.

This gives a precise Arithmetic Fidelity lesson:

> A compression fiber must be computed **inside the actual admissible category**. The same raw retained datum can be non-faithful in a broad category and faithful in a rigid subcategory whose independently supplied global constraints cut the fiber down to a point.

This does not violate AF-001's irreversibility principle. Reflection, finite-order growth, the completion convention, and normalization are extra retained or externally justified structure; they are not downstream functions of an already discarded divisor. If those constraints are not independently available at the loss point, they cannot be inferred merely because the final target is `xi` or `zeta`.

It also sharpens AF-016. Merely observing that a candidate factor happens to respect a symmetry would be insufficient without a completeness theorem. Here Hadamard factorization supplies that completeness theorem: it explicitly classifies **all** same-divisor functions in the order-one entire category, after which reflection and normalization can be proved to exhaust the remaining ambiguity.

## Prior art and novelty assessment

All analytic ingredients are classical.

Hadamard's factorization theorem gives the canonical-product representation of finite-order entire functions and bounds the degree of the exponential polynomial by the order. The fact that two order-at-most-one entire functions with the same zero divisor differ by `e^{as+b}` is an immediate corollary.

The order-one entire character of Riemann's `xi` function, its functional equation `xi(s)=xi(1-s)`, and its Hadamard product over the nontrivial zeta zeros are classical parts of the analytic theory of the zeta function. Standard references include the NIST Digital Library of Mathematical Functions, the *Encyclopedia of Mathematics*, and Titchmarsh's treatment of the Riemann zeta function.

No novelty is claimed for reconstruction of `xi` from its zeros once the functional equation, growth class, and normalization are imposed. The Arithmetic Fidelity contribution is the **fiber placement and sharp lift ladder** immediately after AF-017: divisor-only compression leaves a zero-free ambiguity; order-one growth makes that ambiguity finite-dimensional; reflection removes exactly the linear exponential degree of freedom; one scalar normalization removes exactly the remaining scale.

## Boundaries and failure modes

- The same-zero conclusion `g/f=e^{as+b}` uses the finite-order-at-most-one hypothesis. For broader classes of entire or meromorphic functions, the zero-free quotient can be much less rigid.
- The two functions must have the same zero divisor **with multiplicities**, not merely the same set of distinct zero locations.
- A reflection equation is useful only when it is independently part of the admitted structure. Imposing `F(s)=F(c-s)` solely because it forces the desired object into a narrow fiber would be circular.
- The reflection laws must use the same center and normalization convention. A changed completion can move structure between the function and its prefactors.
- Reflection alone leaves the scalar ambiguity `C f`; it does not determine residues, normalization, or exact values.
- One point normalization is decisive only after the slope ambiguity has been removed and only at a point where the common function is nonzero.
- Grosswald--Schnitzer controls from AF-017 are not contradicted. Their modified Euler products preserve the relevant zero divisor but generally do not belong to the same fixed completed order-one reflection class as Riemann `xi`. The present theorem explains exactly why adding that global structure changes the fidelity category.
- Recovering the rational-prime norm multiset from exact `zeta` values does not recover every richer arithmetic provenance or prove that a given spectral/geometric construction intrinsically supplies the completion data.
- This finding has no implication for the truth of RH. It is a reconstruction/fidelity statement conditional only on classical analytic properties that hold regardless of whether the nontrivial zeros lie on the critical line.

## Decisive audit test

For a proposed RH-relevant representation whose retained data are a zero divisor or spectrum:

1. state the full admissible analytic/operator category rather than only the zero set;
2. classify the complete zero-free or isospectral fiber inside that category;
3. identify each independent global constraint claimed to shrink the fiber -- growth/order, reflection, normalization, completion factors, boundary data, markings, or another structure;
4. prove which residual degrees of freedom each constraint removes and exhibit surviving counterexamples when a constraint is omitted;
5. only after the fiber is reduced to the intended equivalence class ask whether the resulting exact object distinguishes rational primes from matched generalized-prime or arithmetic-equivalent controls.

If the admissible category still contains a nontrivial same-destination family with different prime-specific upstream data, the proposed compression remains non-faithful. If a completeness theorem classifies the full fiber and independently justified constraints reduce it to one point, exact recovery is established in that narrower category.

## Consequence for the line

Promote **fiber rigidity under independently justified global constraints** as the positive counterpart to same-destination matched controls.

The category-indexed audit is now:

\[
\text{retained datum}
\longrightarrow
\text{full fiber in the admitted category}
\longrightarrow
\text{independent constraints}
\longrightarrow
\text{residual gauge}
\longrightarrow
\text{exact recovery or surviving control}.
\]

AF-017 supplies a strong negative example at the bare divisor layer; AF-018 supplies a sharp positive example after order-one reflection rigidity and normalization. Future Arithmetic Fidelity work should seek similarly explicit fiber classifications for spectral, positive, quotient, and asymptotic compressions rather than treating either information loss or symmetry breaking as a category-independent yes/no property.