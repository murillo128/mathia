# AF-235 — the subexponential Li quotient is RH-sufficient

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `CLASSICAL-CRITERION-SPECIALIZATION`, `RH-SUFFICIENT-QUOTIENT`, `TARGET-METRIC`, `ROBUSTNESS`, `COMPOSITION-LAW`, `NO-NOVELTY-CLAIM`

## Claim

Let `(lambda_n)_{n>=1}` be Li's coefficients for the Riemann xi function, normalized by

\[
F(z):=\frac{d}{dz}\log \Xi\!\left(\frac1{1-z}\right)
     =\sum_{n\ge 1}\lambda_n z^{n-1}.
\tag{1}
\]

For a complex sequence `a=(a_n)`, define its exponential root rate

\[
r(a):=\limsup_{n\to\infty}|a_n|^{1/n}
\tag{2}
\]

and the subexponential class

\[
\mathcal S:=\{a:r(a)\le 1\}.
\tag{3}
\]

Then `S` is a complex vector subspace of `C^N`, and

\[
\boxed{\mathrm{RH}\iff \lambda\in\mathcal S.}
\tag{4}
\]

Equivalently,

\[
\boxed{\mathrm{RH}\iff [\lambda]=0
\quad\text{in}\quad
\mathbb C^{\mathbb N}/\mathcal S.}
\tag{5}
\]

Thus the entire subexponential part of the Li sequence can be quotiented away without losing the truth value of RH. More strongly, if `e in S` is any additive approximation error, then

\[
\boxed{
\mathrm{RH}
\iff
\lambda+e\in\mathcal S.
}
\tag{6}
\]

If RH is false, the error cannot even change the dominant exponential root rate:

\[
r(\lambda+e)=r(\lambda)>1.
\tag{7}
\]

This endpoint is strictly coarser than the AF-234 Li-trend quotient. If

\[
\mathcal N_{\rm tr}:=\{e:e_n=o(n\log n)\},
\tag{8}
\]

then

\[
\mathcal N_{\rm tr}\subsetneq\mathcal S;
\tag{9}
\]

for example `e_n=exp(sqrt(n))` lies in `S` but not in `N_tr`. AF-234 therefore identifies a quotient that preserves the precise RH trend, while AF-235 identifies a much larger quotient that preserves only the binary RH discriminator.

## Derivation

### The Cayley image of the zero set fixes the coefficient radius

The singularities of `F` in `(1)` come from zeros `rho` of `Xi`. Under

\[
s=\frac1{1-z},
\]

a zero `rho` maps to

\[
z_\rho=1-\frac1\rho.
\tag{10}
\]

For `rho=beta+i gamma`,

\[
|z_\rho|^2
=\frac{(\beta-1)^2+\gamma^2}{\beta^2+\gamma^2}.
\tag{11}
\]

Hence

\[
|z_\rho|=1\iff\beta=\frac12,
\tag{12}
\]

while `beta>1/2` gives `|z_rho|<1`. The functional equation pairs every off-critical zero with a reflected zero, so if RH is false there is a mapped zero strictly inside the unit disk.

The logarithmic derivative `Xi'/Xi` has a genuine pole at every zero, with multiplicity as residue; composition with `(10)` does not cancel it. Therefore:

- under RH, no zero-induced pole lies inside the unit disk and mapped zeros lie on its boundary, so the Taylor series `(1)` has radius exactly `R=1`;
- if RH is false, at least one pole lies at `|z_rho|<1`, so its radius is some `R<1`.

Cauchy-Hadamard applied to `(1)` gives

\[
R^{-1}
=\limsup_{n\to\infty}|\lambda_{n+1}|^{1/n}
=r(\lambda).
\tag{13}
\]

Thus `R=1` exactly under RH and `R<1`, equivalently `r(lambda)>1`, when RH is false. This proves `(4)`.

This is the same classical analytic dichotomy made explicit by Keiper's generating-function formulation and by Voros's sharpened asymptotics. Voros gives, when RH is false, Darboux contributions from poles inside the unit disk with exponentially growing modulus; under RH he obtains `lambda_n=o(e^{epsilon n})` for every `epsilon>0`, and more precisely the familiar `n log n` asymptotic. No novelty is claimed for that criterion.

### Subexponential errors form exactly the harmless additive class

For arbitrary sequences `a,b`,

\[
r(a+b)\le\max\{r(a),r(b)\}.
\tag{14}
\]

Indeed, any common eventual exponential bound above the two root rates also bounds the sum, while the factor `2` disappears after taking `n`th roots. Scalar multiplication does not change the root rate for a nonzero scalar. Therefore `S` is a vector subspace.

If RH holds, both `lambda` and any `e in S` belong to `S`, hence `lambda+e in S`. Conversely, suppose RH is false and put `q=r(lambda)>1`. From `(14)`,

\[
r(\lambda+e)\le q.
\]

But

\[
\lambda=(\lambda+e)-e
\]

also gives

\[
q\le\max\{r(\lambda+e),r(e)\}.
\]

Since `r(e)<=1<q`, necessarily

\[
r(\lambda+e)\ge q.
\]

This proves `(7)` and hence `(6)`.

There is also a sharp algebraic sense in which the error class cannot be enlarged uniformly while retaining this exact membership decoder. If an additive error space contains some `v notin S`, then the non-subexponential signal `lambda=v` can be annihilated by the allowed error `e=-v`, producing `lambda+e=0 in S`. Thus `S` is the maximal vector subspace of additive perturbations under which membership in `S` is invariant for every sequence.

## Relationship to AF-234

AF-234 deliberately priced the stronger target

\[
\frac{\lambda_n}{n\log n}\longrightarrow\frac12,
\]

which needs additive distortion `o(n log n)`. AF-235 asks only for the weakest large-scale discriminator visible directly from the Li generating function: whether its coefficient radius is `1` or strictly smaller than `1`.

The resulting information budget changes drastically. A perturbation may dominate the RH main term by an arbitrarily large subexponential factor — for example `exp(sqrt(n))` — and still be harmless for the radius/RH endpoint. What matters is not absolute approximation quality but whether the distortion crosses the same exponential scale that separates the two hypotheses.

This supplies a concrete instance of the Arithmetic Fidelity principle that compression must be priced against the declared endpoint. Recovering the Li trend, Li signs, individual zeros, or prime provenance is far stronger than recovering the single radius class needed by `(4)`.

## Arithmetic-facing consequence

Suppose an upstream prime-side or explicit-formula construction produces a sequence `L=(L_n)` together with an unconditional estimate

\[
\lambda-L\in\mathcal S.
\tag{15}
\]

Then immediately

\[
\boxed{\mathrm{RH}\iff L\in\mathcal S.}
\tag{16}
\]

No `o(n log n)` approximation and no recovery of exact Li coefficients is required. The admissible error may be as large as `exp(o(n))`.

This does **not** solve RH or make `(15)` easy. A proof that the remainder is subexponential must be independent of RH; if it already excludes the pole structure corresponding to off-critical zeros, the argument is circular. The useful change is the target: an upstream representation need only preserve the exponential growth class, not the full Li sequence or its precise trend.

The next arithmetic test is therefore sharply falsifiable: identify a natural prime-side decomposition `lambda=L+E` in which `E in S` is provable unconditionally and `L` is structurally simpler than `lambda`, or prove that the known arithmetic decompositions cannot isolate such a remainder without importing zero-free information equivalent to the desired radius bound.

## Matched controls and boundaries

1. **Subexponential masking control.** Add `e_n=exp(sqrt(n))`, or any sequence with `r(e)<=1`. It can completely destroy the `n log n` trend and all eventual sign information, but it cannot change the RH decision in `(4)`.

2. **Exponential cancellation boundary.** If an allowed error contains a component with root rate `q>1`, exact cancellation of a false-RH exponential component becomes possible. The subexponential error budget is therefore not merely convenient; it is the maximal linear noise class for a uniform quotient decoder.

3. **Finite-prefix control.** Arbitrary changes to finitely many coefficients leave `r(a)` unchanged. The endpoint is intrinsically tail-only and cannot certify RH from any finite computation.

4. **Same-divisor provenance control.** As in AF-017 and AF-234, changing arithmetic provenance while preserving the relevant zero divisor does not refute this endpoint: the radius discriminator intentionally forgets that provenance. It is sufficient for RH truth, not faithful to the rational-prime source.

## Prior art and novelty assessment

- Jerry B. Keiper, **“Power Series Expansions of Riemann's xi Function,”** *Mathematics of Computation* 58(198), 765–773 (1992), DOI `10.1090/S0025-5718-1992-1122072-5`. Keiper introduced the relevant power-series coefficients and already connected RH to the unit-disk convergence boundary.
- Enrico Bombieri and Jeffrey C. Lagarias, **“Complements to Li's Criterion for the Riemann Hypothesis,”** *Journal of Number Theory* 77(2), 274–287 (1999), DOI `10.1006/jnth.1999.2392`. This supplies the classical general Li-criterion/conformal-mapping framework and arithmetic formulas.
- André Voros, **“Sharpenings of Li's Criterion for the Riemann Hypothesis,”** *Mathematical Physics, Analysis and Geometry* 9, 53–63 (2006), DOI `10.1007/s11040-005-9002-8`, arXiv:`math/0506326`. Voros proves the sharp asymptotic alternative: RH gives tempered `n log n` growth, whereas false RH produces exponentially growing oscillatory contributions from mapped poles inside the unit disk.

The radius criterion, Cauchy-Hadamard step, and Li/Voros asymptotic dichotomy are classical or immediate consequences of classical analysis. No novelty is claimed for them. The Arithmetic Fidelity contribution is the **target-relative quotient statement**: the subexponential sequence space is exactly a maximal linear additive error class that can be erased while preserving the binary RH discriminator, and it is strictly larger than the `o(n log n)` trend-null class isolated in AF-234.

## Evidence boundary

`(4)`–`(7)` are exact consequences of the classical Li generating function, the Cayley geometry of zeta zeros, Cauchy-Hadamard, and elementary root-rate inequalities. The literature establishes the underlying RH/growth dichotomy; the quotient and robustness language is a derived organization of that criterion, not a new RH theorem.

The finding establishes only an endpoint tolerance theorem. It does not provide a prime-side construction satisfying `(15)`, does not show that subexponential remainder control is easier than RH, and does not recover prime provenance, individual zeros, Li positivity, or the AF-234 leading asymptotic. Any claimed RH route using AF-235 must still prove the subexponential error bound without smuggling in the missing zero-free information.