# PL-117 — Compatible l-adic Frobenius data keep the cross-prime gauge; local purity does not localize Riemann zeros

## Claim

`PL-116` explicitly leaves l-adic representations open because they can have infinite image and need not factor through finite Galois quotients. That enlargement is real, but the direct compatible-system repair still does not supply the missing operator-valued coupling between prime coordinates.

Let `E` be a number field and let

`{rho_lambda : G_Q -> GL_n(E_lambda)}_lambda`

be a Serre compatible system, unramified outside a finite set `S`. At every good rational prime `p`, the canonical local spectral datum is

`P_p(T)=det(I-rho_lambda(Frob_p)T) in E[T]`,

and compatibility says that this polynomial is independent of `lambda` wherever both members are unramified.

This removes the finite-image limitation of `PL-116`, but not the conjugacy gauge from `PL-115`: `Frob_p` is intrinsically a conjugacy class. Replacing a representative `g_p` by `h_p g_p h_p^(-1)` conjugates `rho_lambda(g_p)`. Raw products or eigenspace comparisons involving representatives at distinct rational primes therefore require extra choices; the local Frobenius classes themselves do not provide a canonical relative frame.

The ordinary representative-independent local readouts are scalar invariants such as `P_p`, its coefficients, and power traces. Their standard global assembly is the scalar Euler product

`L^S(s,rho)=prod_(p notin S) P_p(p^(-s))^(-1)`

in its convergence domain. Infinite monodromy can make the polynomials much richer, but it does not by itself create a noncommutative cross-prime Riemann-zeta channel.

The tempting extra ingredient, **purity**, does not repair this direct route. Even assuming a compatible system is pure in the usual Frobenius sense, purity controls the absolute values of the roots of each individual `P_p`. The rank-one trivial system is already exactly pure of weight zero:

`rho_lambda(Frob_p)=1`, `P_p(T)=1-T`,

while

`L(s,rho_triv)=prod_p (1-p^(-s))^(-1)=zeta(s)`

for `Re(s)>1`. Thus the Riemann channel has perfectly rigid prime-local Frobenius eigenvalues before the global nontrivial-zero problem is addressed. Local purity is not the missing mechanism that singles out `Re(s)=1/2`; one still needs an additional global cohomological, trace, duality, positivity, or target-relative structure that turns the global zero divisor into spectral data.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION` for the direct route

`infinite-image compatible l-adic system + standard local Frobenius spectral invariants/purity -> canonical operator-valued prime coupling -> RH rigidity`.

No novelty is claimed for compatible systems, Frobenius characteristic polynomials, weights/purity, or Galois `L`-functions. The durable contribution is the line-specific closure of the simplest non-archimedean escape left open by `PL-116`.

## 1. Infinite image is not a canonical cross-prime frame

An l-adic representation can have infinite compact image, so the finite-quotient argument for complex Artin representations cannot be repeated. Nevertheless, at an unramified prime one only has a Frobenius conjugacy class. If `g_p` is a representative then

`g_p -> h_p g_p h_p^(-1)`

induces

`rho_lambda(g_p) -> rho_lambda(h_p)rho_lambda(g_p)rho_lambda(h_p)^(-1)`.

For distinct `p,q`, an expression such as `rho_lambda(g_p)rho_lambda(g_q)` or an entry comparing their eigenvectors changes with these representative choices unless further transport/frame data are specified. All matrices act on the same abstract representation space, but that fact does not canonically choose representatives of the two conjugacy classes.

This is exactly the gauge obstruction of `PL-115` surviving a change of coefficient field. Infinite monodromy supplies more matrices, not a canonical alignment of prime directions.

## 2. Compatibility is coherence across coefficient places, not transport across arithmetic primes

Hui's formulation of a Serre compatible system makes the distinction explicit. For a good finite place `v`,

`P_(v,rho_lambda)(T)=det(I-rho_lambda(Frob_v)T)`

lies in one number field and agrees for different coefficient places `lambda`. Specialized to `Q`, one obtains a fixed polynomial `P_p` for each good rational prime.

This is genuine arithmetic coherence, but it is coherence **across `lambda` for a fixed `p`**. It does not supply a connection from the local eigenspaces at `p` to those at `q`. In exponent-lattice language, the basis direction `e_p` is enriched by a canonical scalar polynomial, but the compatibility axiom does not create an edge or noncommuting operator between `e_p` and `e_q`.

This is not an information-poverty claim. Dokchitser--Dokchitser show that Frobenius-semisimple local Weil representations can be recovered from Euler factors over finite extensions. The obstruction is specifically the absence of a canonical **cross-prime** coupling in the standard local data.

## 3. The standard global readout remains scalar

The usual unramified global readout is

`L^S(s,rho)=prod_(p notin S) det(I-rho_lambda(Frob_p)p^(-s))^(-1)`.

Where this Euler product converges absolutely it is an ordinary scalar holomorphic function. If continuation and a functional equation are known, they come from additional global arithmetic or automorphic input; they are not obtained by continuing the product termwise into the critical strip.

Thus the direct chain remains

`prime coordinate -> Frobenius class -> lambda-independent P_p -> scalar L-function`.

A construction only becomes a new RH mechanism if it adds an independent global relation that constrains the continued divisor rather than merely repackaging it.

## 4. Purity is already exact on the zeta channel

Deligne's theory of weights supplies the decisive finite-field precedent: a cohomological Frobenius plus purity and a trace/determinant realization produces zero-location theorems for zeta functions over finite fields. The load-bearing point is the **global cohomological realization**, not the word purity by itself.

For a pure number-field compatible system, the roots of `P_p` have prescribed complex modulus `p^(w/2)`. The trivial compatible system gives the cheapest adversarial control. Its only Frobenius eigenvalue is `1` at every good prime, so it is exactly weight-zero pure, while its scalar Euler product is Riemann zeta.

Consequently prime-local purity is already fully present on the target Riemann channel. What is missing over `Spec Z` is an analogue of the finite-field global Frobenius/cohomology mechanism in which the **nontrivial global zeros themselves** become eigenvalues whose weights can constrain their location.

## 5. Prior-art and novelty audit

The ingredients are standard.

- **Chun Yin Hui**, “Monodromy of subrepresentations and irreducibility of low degree automorphic Galois representations,” *Journal of the London Mathematical Society* **108** (2023), 838–902, DOI `10.1112/jlms.12811`. Section 2.4 explicitly defines `E`-rational and Serre compatible systems through good-prime Frobenius characteristic polynomials and their independence of the coefficient place.
- **Richard Taylor**, “Galois representations,” *Annales de la Faculté des sciences de Toulouse: Mathématiques* (6) **13**(1) (2004), 73–119, DOI `10.5802/afst.1065`. Survey anchor for number-field Galois representations and their global `L`-function/automorphic setting.
- **Pierre Deligne**, “La conjecture de Weil : II,” *Publications Mathématiques de l'IHES* **52** (1980), 137–252, DOI `10.1007/BF02684780`. Primary purity/weights anchor for the finite-field cohomological paradigm.
- **Tim Dokchitser, Vladimir Dokchitser**, “Euler factors determine local Weil representations,” *Journal fur die reine und angewandte Mathematik* **2016**(717), 35–46, DOI `10.1515/crelle-2014-0013`. Adversarial control showing that scalar Euler factors can retain rich local representation data.

No theorem was found phrased in the present `prime_lattice` language. The conclusion is therefore a route classification synthesized from standard structures, not a new theorem in Galois representation theory.

## 6. Adversarial boundaries

1. **Only the direct local-data escape is ruled out.** Global cohomology, correspondence algebras, trace formulas, deformation spaces, motives, automorphic reciprocity, or target-relative Hilbert spaces can introduce genuine cross-prime structure.
2. **The claim does not say `P_p` exhausts all global Galois information.** It says the standard prime-local spectral data are conjugacy-invariant and do not themselves choose relative Frobenius frames.
3. **Purity is not asserted for arbitrary l-adic representations.** The negative test applies when purity is available; the trivial system gives an exact weight-zero control.
4. **No Euler product is continued termwise.** Euler-product identities are used only in their convergence domain; continuation requires separate global input.
5. **Finite ramified sets do not create an infinite cross-prime matrix coupling.** More elaborate ramified or local data can matter globally but need their own mechanism.
6. **A genuine cohomological Hilbert--Polya construction remains outside the no-go.** If a global operator independently realizes completed zeta and has a positivity/self-adjointness theorem, local weights may become part of the explanation.

## Consequence for the research line

`PL-115` scalarized fixed finite Galois Frobenius labels; `PL-116` showed that a profinite tower with canonical central harmonic analysis is still block-scalar but left l-adic representations open. The direct l-adic repair now narrows to

`infinite-image compatible system -> lambda-independent local P_p -> scalar global L-function`,

with local purity already exact on the trivial system whose `L`-function is zeta.

A viable Galois/cohomological continuation must therefore specify **what globally couples the prime directions** and why that global structure turns nontrivial zeta zeros into spectral data with a positivity or duality constraint. Merely replacing complex Artin representations by richer l-adic matrices, or invoking local Frobenius purity, does not supply that missing step.