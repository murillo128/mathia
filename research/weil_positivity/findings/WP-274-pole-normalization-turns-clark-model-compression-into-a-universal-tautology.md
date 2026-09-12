---
id: WP-274
title: Pole normalization turns Clark-model compression into a universal tautology
branch: weil_positivity
status: supported
kind: source-side-model-space-classification
claim_strength: exact unconditional normalization plus classical Clark and de Branges inverse realizations with universality no-go
created: 2026-09-12
related: [WP-222, WP-269, WP-270, WP-272, WP-273]
prior_art:
  - D. N. Clark, One dimensional perturbations of restricted shifts, Journal d'Analyse Mathematique 25 (1972), 169-191, DOI 10.1007/BF02790036
  - A. Poltoratski and D. Sarason, Aleksandrov-Clark measures, in Recent Advances in Operator-Related Function Theory, Contemporary Mathematics 393 (2006), 1-14
  - Louis de Branges, Hilbert Spaces of Entire Functions, Prentice-Hall, 1968
  - Jonathan Eckhardt and Aleksey Kostenko, Trace formulas and inverse spectral theory for generalized indefinite strings, Inventiones Mathematicae 238 (2024), 391-502, DOI 10.1007/s00222-024-01287-9
---

# WP-274 — Pole normalization turns Clark-model compression into a universal tautology

## Claim

`WP-273` leaves one broad escape from the local-cutoff obstruction: a genuinely nonlocal analytic/model-space compression whose norm is controlled by the prime-power samples. For the canonical pole-completed carrier

\[
T_{\rm pole}
=\nu_{1/2}-\cosh(x/2)\,dx,
\qquad
\nu_{1/2}
=\frac12\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\bigl(\delta_{\log n}+\delta_{-\log n}\bigr),
\tag{1}
\]

there is an exact and unconditional normalization that puts this escape directly into classical Aleksandrov--Clark theory.

Let

\[
w(x)=\cosh(x/2),
\qquad
g(x)=w(x)^{1/2}f(x).
\tag{2}
\]

Since

\[
w(\log n)=\cosh\!\left(\frac{\log n}{2}\right)
=\frac{n+1}{2\sqrt n},
\tag{3}
\]

the quadratic form of `WP-273` becomes exactly

\[
Q(f)
=\sum_{n\ge2}\frac{\Lambda(n)}{n+1}
\left(|g(\log n)|^2+|g(-\log n)|^2\right)
-\int_{\mathbb R}|g(x)|^2\,dx.
\tag{4}
\]

Thus the pole background canonically normalizes the critical Mangoldt half-density to the positive discrete measure

\[
\sigma_\Lambda
:=\sum_{n\ge2}\frac{\Lambda(n)}{n+1}
\bigl(\delta_{\log n}+\delta_{-\log n}\bigr).
\tag{5}
\]

This measure is Herglotz-admissible without RH:

\[
\int_{\mathbb R}\frac{d\sigma_\Lambda(t)}{1+t^2}
=2\sum_{n\ge2}
\frac{\Lambda(n)}{(n+1)(1+(\log n)^2)}
<\infty.
\tag{6}
\]

Because `sigma_Lambda` is positive, singular, and locally discrete, classical Herglotz--Clark theory therefore produces a meromorphic inner function `Theta_Lambda` for which `sigma_Lambda` is a Clark measure, after one fixed universal Hardy/Clark normalization convention. The Clark operator identifies the corresponding model space `K_{Theta_Lambda}` unitarily with `L^2(sigma_Lambda)`. Consequently its boundary functions satisfy

\[
\int_{\mathbb R}|g(x)|^2\,dx
=\int_{\mathbb R}|g(t)|^2\,d\sigma_\Lambda(t),
\tag{7}
\]

in that fixed convention, and the weighted pullback

\[
\mathcal R_\Lambda
:=\left\{f:\;w^{1/2}f
\text{ is the boundary value of some }g\in K_{\Theta_\Lambda}\right\}
\tag{8}
\]

obeys

\[
\boxed{Q(f)=0\qquad(f\in\mathcal R_\Lambda).}
\tag{9}
\]

So the nonlocal escape left open by `WP-273` is **nonempty**: an analytic model-space compression can evade every compact-cutoff localization argument and make the pole-completed source form nonnegative.

But the same construction works for essentially every positive-minus-positive carrier whose normalized singular sampling measure satisfies the elementary Herglotz growth condition. The inner function in (7) is reconstructed *from the desired sampling measure itself*. Hence Clark realization supplies no independent Riemann sign theorem. It is a universal representation theorem that can manufacture a null positive compression from the Jordan data one started with.

The same verdict survives the apparently more geometric canonical-system reformulation. Once a Herglotz function is built from `sigma_Lambda`, de Branges inverse spectral theory produces a positive trace-normalized Hamiltonian having that Herglotz function as Weyl coefficient; after trace normalization the Hamiltonian is determined almost everywhere. Thus inverse canonical-system geometry does not add an independently selected positive object: it is another universal reconstruction of the target measure.

The consequence is a sharper gate than `WP-273`: **nonlocal analytic sampling is necessary as a possible escape from localization, but neither a Clark model nor a canonical system counts as evidence for Weil positivity when it is reconstructed from the target carrier.** A viable model/de Branges route must derive its inner function, Hamiltonian, boundary law, or equivalent analytic space independently from Mathia/source geometry and only then show that its pre-existing sampling or Weyl law reproduces the Mangoldt, Gamma, and polar terms with the correct Weil orientation.

**Classification:** `EXACT-DERIVED + RH-INDEPENDENT + CANONICAL-POLE-NORMALIZATION + POISSON-FINITE-MANGOLDT-MEASURE + CLASSICAL-CLARK-REALIZATION + DE-BRANGES-INVERSE-SPECTRAL-REALIZATION + NONLOCAL-NULL-COMPRESSION + GENERIC-JORDAN-PAIR-TAUTOLOGY + MATCHED-CONTROL-STABLE + PRIOR-ART-AUDITED + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. The pole density removes the critical square root exactly

For compactly supported continuous `f`, `WP-273` writes

\[
Q(f)
=\frac12\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\left(|f(\log n)|^2+|f(-\log n)|^2\right)
-\int_{\mathbb R}w(x)|f(x)|^2\,dx.
\tag{10}
\]

Multiplication by `w^{1/2}` is an isometry from the negative Hilbert component `L^2(w(x)dx)` to ordinary `L^2(dx)`. At an arithmetic atom, (3) gives

\[
\frac{\frac12\Lambda(n)n^{-1/2}}{w(\log n)}
=\frac{\Lambda(n)}{n+1}.
\tag{11}
\]

The same holds at `-log n` because `w` is even. Equations (4)--(5) follow with no limiting argument, analytic continuation, or zero information.

This normalization is more rigid than choosing a convenient sampling weight after the fact. Both factors in (11) are already fixed by (1): the numerator is the critical Mangoldt half-density and the denominator is the canonical pole continuum. Their ratio is forced.

It is nevertheless only a normalization of the signed source carrier. No Gamma term has appeared, and no sign theorem has yet been proved.

## 2. The normalized Mangoldt measure satisfies the Herglotz growth condition unconditionally

The support

\[
S=\{\pm\log(p^k):p\text{ prime},\ k\ge1\}
\tag{12}
\]

is locally finite, so `sigma_Lambda` is a locally finite positive pure-point measure. It remains to check the one growth condition required by the upper-half-plane Herglotz representation.

For `x>=3`, set

\[
h(x)=\frac{1}{x(1+(\log x)^2)}.
\tag{13}
\]

Since `n+1>=n`, the positive half of (6) is bounded by

\[
\sum_{n\ge3}\Lambda(n)h(n).
\tag{14}
\]

Write `psi(X)=sum_{n<=X} Lambda(n)`. Chebyshev's elementary bound `psi(X)=O(X)` is enough. Partial summation gives

\[
\sum_{3\le n\le X}\Lambda(n)h(n)
=\psi(X)h(X)-\psi(3^-)h(3)
-\int_3^X\psi(t)h'(t)\,dt.
\tag{15}
\]

Here `psi(X)h(X)=O((1+(log X)^2)^{-1})`, while

\[
|h'(t)|
\ll\frac{1}{t^2(\log t)^2}
\qquad(t\to\infty).
\tag{16}
\]

Therefore

\[
\int_3^\infty\psi(t)|h'(t)|\,dt
\ll\int_3^\infty\frac{dt}{t(\log t)^2}
<\infty,
\tag{17}
\]

proving (6). This uses neither the prime number theorem nor RH.

The point of (6) is categorical, not asymptotic. The normalized source measure lies exactly in the ordinary one-variable Herglotz/Nevanlinna measure class; no generalized distribution space is needed to construct the associated analytic function.

## 3. Classical Clark theory manufactures a nonlocal null range

Fix once and for all an upper-half-plane Hardy-space normalization in which the boundary norm is

\[
\|g\|_{H^2}^2=\int_{\mathbb R}|g(x)|^2\,dx,
\tag{18}
\]

and normalize Clark measures with the corresponding universal Poisson-kernel constant. Changing to the more common `1/(2pi)` Hardy convention merely rescales every Clark measure by the same fixed constant and changes none of the argument below.

By (6), the regularized Herglotz integral of `sigma_Lambda` defines a holomorphic Herglotz function on the upper half-plane. Choose zero linear term and any fixed real additive normalization. Its Cayley transform is an inner function `Theta_Lambda`; because the representing measure is pure point with locally discrete support, this is a meromorphic inner function. In the chosen Clark normalization, `sigma_Lambda` is one of its Aleksandrov--Clark measures.

Clark's theorem then gives a unitary spectral/boundary map

\[
K_{\Theta_\Lambda}\longrightarrow L^2(\sigma_\Lambda),
\tag{19}
\]

whose action on the natural dense class is boundary evaluation at the Clark support. Consequently

\[
\|g\|_{H^2}^2
=\sum_{n\ge2}\frac{\Lambda(n)}{n+1}
\left(|g(\log n)|^2+|g(-\log n)|^2\right).
\tag{20}
\]

Equations (4), (18), and (20) give (9).

This does exactly what the local no-go in `WP-273` says a surviving range must do. `K_{Theta_Lambda}` is an analytic space and is not stable under arbitrary compactly supported smooth cutoffs. Its continuum boundary norm is reconstructed globally from discrete samples, so an atom-free local interval cannot be varied independently.

The construction is a **boundary model-space realization for `g`**, not a claim that the original weighted variable `f=w^{-1/2}g` is itself an ordinary unweighted de Branges/model space. The weight in (2) is part of the exact pullback from the pole carrier and must be retained.

## 4. Aggressive falsification: the construction is universal for Poisson-finite Jordan pairs

The preceding success does not survive the branch's independence test. Consider any signed carrier

\[
T=\mu_+-w(x)\,dx,
\tag{21}
\]

where `w>0` is continuous and `mu_+` is a positive singular locally finite measure. Put

\[
d\sigma=w^{-1}\,d\mu_+.
\tag{22}
\]

Whenever

\[
\int_{\mathbb R}\frac{d\sigma(t)}{1+t^2}<\infty,
\tag{23}
\]

the same change of variable `g=w^{1/2}f` gives

\[
\langle T,|f|^2\rangle
=\int|g|^2\,d\sigma-\int|g|^2\,dx.
\tag{24}
\]

Herglotz--Clark theory can then construct an inner function from `sigma` itself and a corresponding model-space range on which the two norms in (24) are equal. Thus

\[
\boxed{
\text{Poisson-finite normalized singular Jordan data}
\Longrightarrow
\text{a Clark-manufactured nonlocal null compression.}
}
\tag{25}
\]

No primes, Euler product, functional equation, Gamma factor, or Riemann-specific relation enters this implication.

This gives a strong matched control. Replace the prime-power support in (5) by any locally finite weighted discrete set whose normalized measure satisfies (23). The same analytic construction succeeds. Even the locations and weights can be arbitrary. The model space simply changes so that its Clark measure becomes the prescribed data.

Accordingly, the construction reverses the explanatory direction required by this research line. The desired sample law is fed into Herglotz representation; the inner function is recovered from it; Clark's theorem then returns the same sample law as an isometric boundary representation. The resulting nonnegativity is mathematically genuine but **representation-theoretically tautological**.

This is the infinite-dimensional analytic analogue of the sign-programmability warning in `WP-222`. There, changing a finite-Blaschke coinvariant quotient can program the sign of a fixed source defect. Here, choosing the inner function whose Clark measure is the target normalized carrier programs an exact null range. In both cases, positivity becomes relevant only after an independent source law selects the quotient/model object.

Two apparent escapes do not change that diagnosis:

- the real additive constant in the Herglotz function changes the inner-function normalization but does not create an arithmetic sign theorem;
- imposing the even symmetry of (5) can choose a symmetric representative, but symmetry is shared by arbitrary symmetric matched controls and does not select the Riemann arithmetic.

Nor does (9) supply the missing completed Weil form. It accounts only for the positive Mangoldt atoms against the pole continuum in (1). The Gamma contribution, exact polar normalization in the full explicit formula, and the required Weil autocorrelation/test-function structure remain separate obligations.

## 5. De Branges inversion manufactures a positive Hamiltonian from the same target measure

The Clark tautology does not disappear if the model space is replaced by a canonical system whose Hamiltonian is itself positive. Fix the same universal Herglotz normalization for every candidate measure satisfying (23): choose one real constant `a_0`, set the nonnegative linear coefficient to zero, and define

\[
m_\sigma(z)
=a_0+\int_{\mathbb R}
\left(\frac{1}{t-z}-\frac{t}{1+t^2}\right)d\sigma(t).
\tag{25a}
\]

This is a Herglotz--Nevanlinna function. De Branges' inverse spectral theorem for two-dimensional canonical systems says that every Herglotz--Nevanlinna function occurs as the Weyl--Titchmarsh function of a Hamiltonian, and that the Weyl function determines the Hamiltonian almost everywhere up to reparametrization. With the standard trace normalization, the ambiguity disappears: there is a unique almost-everywhere Hamiltonian `H_sigma` with

\[
H_\sigma(x)\succeq0,
\qquad
\operatorname{tr}H_\sigma(x)=1
\quad\text{for a.e. }x,
\tag{25b}
\]

whose canonical system, in one standard sign convention,

\[
JY'(x)=zH_\sigma(x)Y(x),
\qquad
J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\tag{25c}
\]

has Weyl function `m_sigma`. The Herglotz representing measure of that Weyl function is exactly the input `sigma` in (25a).

Applying this to `sigma=sigma_Lambda` gives a positive trace-normalized Hamiltonian `H_Lambda` **unconditionally**. But it does not provide the independent geometric positivity required by the branch mandate. Once (5) is used to define `m_Lambda`, the inverse theorem deterministically reconstructs `H_Lambda`; after trace normalization there is no further geometric degree of freedom from which an arithmetic sign theorem could emerge.

The matched control is exact and broad. Every positive measure satisfying (23), including an arbitrary locally finite weighted discrete set unrelated to primes, yields by the same fixed prescription a Herglotz function and therefore a positive trace-normalized Hamiltonian. The positivity of `H_sigma` is a theorem of the representation class, not a discriminator for the Riemann carrier.

Nor do the scalar freedoms in the Herglotz representation rescue the route. Allowing a different real additive constant or a nonnegative linear term changes the reconstructed canonical system, but unless those parameters are fixed by source geometry they are additional programmable inputs. Fixing them once and uniformly, as in (25a), removes that freedom and leaves the universality argument intact.

Therefore the implication

\[
\text{target sampling measure}
\longrightarrow
\text{Herglotz Weyl function}
\longrightarrow
\text{positive trace-normalized Hamiltonian}
\tag{25d}
\]

is an **inverse-spectral encoding** of the target data, not an independently derived Mathia geometry. The only live canonical-system route is the reverse causal direction: first derive a Hamiltonian or equivalent boundary geometry from Mathia without using the Mangoldt carrier, then prove that its already-fixed Weyl/sampling law reproduces the finite-prime data and that the same construction supplies the Gamma and polar terms with the required Weil sign.

## 6. Prior-art and novelty audit

The analytic machinery in this finding is classical. Clark's 1972 theorem identifies the spectral measures of one-dimensional unitary perturbations of the restricted shift and gives the model-space/measure unitary picture. Aleksandrov--Clark theory and later expositions, including Poltoratski--Sarason, make the measure/function correspondence and boundary transforms standard. The Herglotz--Nevanlinna representation used in (6) is older classical analysis.

The canonical-system extension is equally classical. De Branges' inverse spectral theorem gives the correspondence between suitably normalized positive-semidefinite Hamiltonians and Nevanlinna/Weyl functions. Eckhardt--Kostenko's 2024 Appendix D gives an audit-friendly modern statement: the Weyl--Titchmarsh function determines a Hamiltonian up to reparametrization, uniquely determines a trace-normalized Hamiltonian, and every Herglotz--Nevanlinna function arises from a Hamiltonian.

No novelty is claimed for constructing an inner function from a positive singular Herglotz measure, for the Clark isometry, for model-space sampling, or for reconstructing a positive canonical Hamiltonian from a Herglotz function. The durable content for this line is instead the exact source-side normalization (11) and the resulting falsification boundary: **the immediate analytic escapes suggested by `WP-273` can be manufactured from the signed carrier itself and therefore cannot count as independent Mathia positivity mechanisms.**

This does not rule out de Branges, model-space, canonical-system, or other analytic geometry. It rules out the inferences

\[
\text{target sampling measure}
\xrightarrow{\text{Herglotz/Clark inversion}}
\text{analytic model space}
\xrightarrow{\text{Clark isometry}}
\text{target positivity}
\tag{26}
\]

and (25d) as explanations of the Weil sign. A successful route must reverse that causal order.

## Consequence

`WP-273` showed that any positive compression of the canonical pole-completed carrier must abandon local cutoff freedom and behave as a global sampling/interpolation law. `WP-274` now shows that **global analytic sampling and inverse canonical-system positivity are both too weak as selection principles**. Classical inverse theory can manufacture them from the normalized Mangoldt carrier, and equally from arbitrary matched positive singular carriers.

The remaining analytic route has a sharper obligation. Mathia must independently force an inner function, canonical system, de Branges Hamiltonian, boundary correspondence, or equivalent nonlocal object from its intrinsic geometry **before** the target carrier is used to define that object. Only then is it meaningful to ask whether the object's pre-existing positive norm, Hamiltonian, or intersection form reproduces the finite-prime term and, in the same construction, the Gamma and polar sectors of the completed Weil functional.

So the live bridge is no longer merely "find a nonlocal positive compression." It is:

\[
\boxed{
\text{source geometry}
\Longrightarrow
\text{canonical nonlocal analytic object}
\Longrightarrow
\text{independent norm/sign theorem}
\Longrightarrow
\text{Weil arithmetic decomposition}.
}
\tag{27}
\]

Constructing the middle object by inverting the last line of data is a representation of the answer, not an explanation of it.
