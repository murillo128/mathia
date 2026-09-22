# MC-456 — Triply-well-factorable dispersion provides a factor-specific quotient-breaking template

**Status:** `LITERATURE+DERIVED` · `FRONTIER-ADVANCE` · `TRANSFER-CRITERION` · `PRE-QUADRATIC-DISPERSION` · `PRODUCT-QUOTIENT-BREAKING` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-454` and `MC-455` isolated a structural obstruction in the current well-factorable/source-frame branch. Writing a coefficient as a convolution does not create new source states when the source kernel depends only on the product variables, and standard source-only `q`-van der Corput operations preserve that product quotient when their parameters are chosen independently of the internal factor representative.

Modern dispersion arguments for triply-well-factorable weights supply a concrete classical template for how that quotient can actually be broken **before positive closure**. The relevant mechanism is not factorability by itself. It is that the factor variables of the weight are also factors of the arithmetic-progressions modulus, and Linnik dispersion plus completion assigns those factors asymmetrical roles in the transformed oscillatory kernel.

Pascadi's triply-well-factorable setup starts from

\[
q=q_1q_2q_3,
\qquad
\lambda_q
=
\sum_{q_1q_2q_3=q}
\alpha_{q_1}\beta_{q_2}\gamma_{q_3},
\tag{1}
\]

with the three factor ranges selectable subject to `Q_1Q_2Q_3=Q`. In the critical prime-distribution form, the congruence is itself modulo `q_1q_2q_3`. Pascadi's proof outline then applies Cauchy--Schwarz in one factor block and a source variable, duplicates the remaining factor blocks, completes a source sum, and reaches a Kloosterman-fraction sum of the form

\[
\sum_{c\sim Q}\sum_{d\sim x/Q}
\left|
\sum_{\ell\sim Q^2/x}v_\ell
\sum_{h\sim Q^2/x}
 e\!\left(h\frac{\overline{\ell d}}{c}\right)
\right|.
\tag{2}
\]

In the prime case Pascadi identifies, schematically,

\[
(c,d,\ell)
\longleftrightarrow
(nq_2'q_3',\;n'q_3,\;q_2).
\tag{3}
\]

Thus the transformed phase retains **which factor occupied which block**. Two representations having the same total product `q=q_1q_2q_3` need not give the same `c,d,\ell` and hence need not give the same reciprocal phase in `(2)`. The transformed family is therefore not a pullback through the multiplication quotient ` (q_1,q_2,q_3)\mapsto q ` in the sense of `MC-455`.

This is the missing qualitative feature of the Mathia escape condition: a legitimate analytic operation can make internal factor labels observable when those labels enter distinct arithmetic roles *before* Cauchy/completion has scalarized them. The gain in the classical theorem then comes from estimating the resulting structured Kloosterman family, not from counting more convolution representations of the same modulus.

Yang's 2026 convolution-type Bombieri--Vinogradov theorem gives an especially relevant two-factor-to-three-factor bridge. Yang starts with an ordinary well-factorable modulus weight

\[
\lambda_q=\sum_{q_2q_3=q}\lambda_2(q_2)\lambda_3(q_3)
\tag{4}
\]

in a convolution form carrying an additional arithmetic variable and explicitly applies Pascadi's triply-well-factorable estimate after choosing the factor ranges. For the complementary regime Yang uses truncated Poisson summation and Pascadi's incomplete-Kloosterman estimate; the latter contains phases of the model form

\[
e\!\left(\pm n\frac{\overline{rd}}{sc}\right),
\tag{5}
\]

where the factor blocks `r,s,c,d` remain separately visible. This shows that the quotient-breaking pattern is not merely a formal decomposition of a weight: it is an operational ingredient of current beyond-square-root distribution technology.

However, this prior art **does not transfer automatically** to the present Möbius translated-character source frame. In `MC-413`--`MC-455`, the well-factorable variables parameterize divisor products `(d,e)` and their CRT/lcm translation data, while the multiplicative-character conductor is a separate fixed source modulus. Once the source kernel has become a function only of `(d,e)`, source-side conductor splitting is fiber-independent and `MC-455` applies. Pascadi/Yang succeed in a different incidence geometry: the factorable variable is itself inside the congruence modulus and remains there through the first dispersion/completion step.

Therefore the live transfer problem has a sharper criterion:

> A well-factorable decomposition can evade the `MC-454`/`MC-455` product-quotient obstruction only if a justified pre-positive transform makes different internal factor representatives of the same product occupy analytically different source/modulus roles, or supplies an equivalent factor-specific oscillatory kernel. Merely possessing a convolution decomposition, or separately factoring an external character conductor, is insufficient.

No such transform has yet been derived for the current Möbius source kernel. No improvement for `M(x)`, no new character-sum exponent, and no RH consequence follows.

## 1. Exact classical quotient breaking

Pascadi defines triply-well-factorable weights precisely by `(1)`. In the prime arithmetic-progression problem the basic weighted error contains

\[
\mathbf 1_{mn\equiv 1\pmod{q_1q_2q_3}}
-
\frac{\mathbf 1_{(mn,q_1q_2q_3)=1}}
     {\varphi(q_1q_2q_3)}.
\tag{6}
\]

The factor variables are therefore not auxiliary labels attached only to a coefficient: they are visible in the constraint satisfied by the source variables.

Pascadi's overview states that dispersion begins with Cauchy--Schwarz in `q_1` and a source variable. After expanding the square, the `q_2,q_3` variables are duplicated. Fourier completion of the remaining source sum introduces a short frequency `h`, after which complementary-divisor substitutions reduce the problem to `(2)`. In the prime branch, the explicit correspondence `(3)` records separate appearances of `q_2`, `q_3`, and their primed copies.

This gives a direct fiber test. Let

\[
\Pi(q_1,q_2,q_3)=q_1q_2q_3.
\tag{7}
\]

A transformed kernel `K` factors through `\Pi` only if

\[
\Pi(z)=\Pi(z')\implies K_z=K_{z'}.
\tag{8}
\]

But the reciprocal fraction in `(2)` depends on the ordered block data entering `(3)`, not merely on their total product. Changing a factor allocation while preserving the total modulus can alter `\ell`, `c`, or `d`, and hence alter `\overline{\ell d}/c`. The post-dispersion family therefore fails `(8)` generically.

That is the exact structural distinction from `MC-455`. There the initial translated-character family already satisfies `K_z=\widetilde K_{\Pi(z)}`, and every source-only transform has fiber-independent parameters, so pullback stability follows tautologically. Pascadi starts the nontrivial analytic step while the internal modulus factors still occur in separate congruence roles; the pullback hypothesis has not formed.

## 2. The analytic gain is not representation multiplicity

It would be wrong to interpret the classical result as saying that a modulus with many factorizations supplies many independent observations. The useful object is the **structured transformed sum** produced after dispersion.

Pascadi reduces both the triply-well-factorable prime problem and a smooth-number convolution problem to the same Kloosterman-fraction architecture. After another Cauchy--Schwarz step, the off-diagonal variable has additive structure

\[
n=h\ell-h'\ell',
\tag{9}
\]

while the reciprocal phase retains multiplicative/modular structure. The resulting bounds use large-sieve estimates for structured coefficient sequences and Kloosterman sums. The diagonal `h\ell=h'\ell'` is explicitly part of the budget rather than being wished away by factor counting.

Yang's 2026 theorem reinforces the same point. His current version states that the key input is the `x^{5/8-o(1)}` triply-well-factorable prime-distribution theorem together with incomplete Kloosterman estimates. In the small-convolution regime Yang writes the ordinary well-factorable coefficient as `lambda=lambda_2*lambda_3` and applies the three-factor estimate using the additional convolution structure of the source problem. In the larger-convolution regime truncated Poisson exposes the reciprocal phases to which Pascadi's incomplete-Kloosterman theorem applies.

So the reusable lesson is not

\[
\text{more factor labels}\Rightarrow\text{more occupancy}.
\tag{10}
\]

It is

\[
\text{factor labels inside the arithmetic constraint}
\xrightarrow{\text{dispersion/completion}}
\text{factor-specific reciprocal phase}
\xrightarrow{\text{structured estimate}}
\text{analytic gain}.
\tag{11}
\]

This is exactly compatible with `MC-453`: if the factor components are first separated and then each closed by a positive quadratic norm, only a bounded splitting factor is available. The classical method instead keeps the variables coupled through a nontrivial off-diagonal kernel before invoking the decisive positive estimate.

## 3. Transfer criterion for the current Möbius branch

For the translated-character family of `MC-413`, a genuine transfer of the Pascadi/Yang mechanism must produce, before full recombination, a kernel that distinguishes internal representatives such as

\[
(r_1,r_2,r_1',r_2')
\quad\text{with}\quad
r_1r_2=d,
\qquad
r_1'r_2'=e.
\tag{12}
\]

A sufficient structural certificate would be a legitimate transformation giving a phase or congruence of the schematic form

\[
\mathcal K(r_1,r_2,r_1',r_2';\xi)
\tag{13}
\]

for which there exist two tuples `z,z'` satisfying `\Pi(z)=\Pi(z')=(d,e)` but

\[
\mathcal K(z;\xi)\ne\mathcal K(z';\xi)
\tag{14}
\]

on a non-negligible set of source/dual variables, with the distinction surviving the later Cauchy/Poisson/completion bookkeeping. Equation `(14)` is only a structural admission test; one must still prove a quantitative estimate whose diagonal, exceptional set, and completion losses beat the current source budget.

The classical analogy suggests three places to look, all before product collapse:

1. a dispersion ordering in which internal factor blocks enter different congruence moduli before Cauchy;
2. a reciprocity/Poisson step in which different factor blocks enter numerator and denominator of a reciprocal phase separately;
3. an auxiliary convolution variable, analogous to Yang's convolution form, that turns ordinary well-factorability into a genuinely multi-block modulus geometry.

By contrast, the following remain excluded by `MC-454`--`MC-455`: duplicating factor labels while keeping the source kernel product-level; choosing the external conductor split independently of those labels; or applying source-only `A/B` operations after the product quotient has formed.

## 4. Prior art and novelty boundary

The quotient-breaking analytic mechanism is classical/current prior art, not a Mathia invention.

Alexandru Pascadi, *On the exponents of distribution of primes and smooth numbers*, arXiv:2505.00653v2 (29 June 2025), https://arxiv.org/abs/2505.00653. Definition 1.1 gives triply-well-factorable weights; Theorem 1.3 reaches exponent `5/8-epsilon` for primes with such weights. Section 2.1 explicitly describes the dispersion reduction from separately factorized modulus variables to Kloosterman fractions and identifies the factor blocks appearing in the transformed variables.

Zhiyuan Yang, *Convolution-type Bombieri-Vinogradov theorem with well-factorable weights, and its applications*, arXiv:2608.13299v2 (3 September 2026), https://arxiv.org/abs/2608.13299. The current version states that the proof uses Pascadi's `5/8-o(1)` triply-well-factorable result and incomplete Kloosterman estimates. In the proof Yang explicitly writes an ordinary well-factorable weight as `lambda=lambda_2*lambda_3` before applying Pascadi's three-factor convolution estimate, and records the incomplete reciprocal-phase estimate inherited from Pascadi.

Bombieri--Friedlander--Iwaniec, Maynard, Lichtman, Deshouillers--Iwaniec, and the large-sieve/Kloosterman literature are the historical framework behind these results. The present finding makes no novelty claim for well-factorability, Linnik dispersion, Poisson completion, reciprocal/Kloosterman phases, or the exponents of distribution.

The Mathia-specific durable contribution is only the **transfer classification** relative to `MC-453`--`MC-455`: there is established prior art where internal factor variables really do survive into a non-fiber-constant oscillatory kernel, and the decisive property is that they enter the arithmetic modulus geometry before positive closure. This both validates the structural escape condition and sharply limits what can be imported into the current fixed-conductor translated-character setting.

A targeted prior-art audit on 22 September 2026 used the current arXiv versions above. Yang's v2 postdates the initial formulation of this Mathia branch and is therefore especially relevant as a modern worked example, but it is evidence about a neighboring analytic architecture, not evidence that the Möbius transfer succeeds.

## Boundaries and falsification tests

- **No automatic theorem transfer.** Pascadi/Yang estimate primes or convolution sequences in arithmetic progressions whose factorable variable is the modulus. The current Möbius source frame has a fixed external character conductor and coefficient divisors controlling translations/CRT data. A dictionary between the two settings must be derived, not asserted.
- **Factor-specific notation is insufficient.** The decisive test is `(14)`: the transformed kernel must genuinely vary inside a multiplication fiber and that variation must survive later recombination.
- **Quotient breaking is not yet a saving.** Even if `(14)` holds, diagonal terms or completion losses may consume the entire gain. The full source-depth/common-radical budget must still improve strictly.
- **Yang uses extra convolution structure.** The reduction from ordinary well-factorability to Pascadi's stronger three-block estimate is available only for the special convolution form in Yang's theorem. It is not a generic statement that every well-factorable coefficient enjoys triply-well-factorable distribution.
- **The fixed conductor may be a genuine mismatch.** If every legitimate transformation of the `MC-413` source kernel keeps the internal divisor factors outside the oscillatory modulus, then this classical template cannot repair the branch even though it succeeds for arithmetic progressions.
- **No circular zeta input is used.** The literature mechanism is unconditional analytic number theory; this finding does not use a zero-free region near the critical line or `1/zeta` continuation.
- **No global Möbius bound is asserted.** The result is a mechanism/transfer classification only.

The strongest falsification of the live transfer is therefore concrete: prove that, for the exact pre-recombination `MC-413` well-factorable source form, every admissible dispersion/Poisson/reciprocity ordering still factors through `(d,e)` (or another already-classified product/lcm quotient). Conversely, a positive continuation must exhibit the first exact formula that violates that statement and then quantify its diagonal.

## Consequence for the research line

`MC-455` ended with two possibilities: source-only conductor improvement, or factor/conductor coupling before the product quotient. The modern well-factorable literature now resolves an ambiguity in the second phrase. **Factor/conductor coupling is a real analytic mechanism in successful neighboring theorems, but it works because the factorable coefficient variable is itself part of the modulus seen by dispersion and completion.**

The next useful calculation should therefore stop asking whether factorability *in the abstract* can help. It should take the exact pre-positive form underlying `MC-413`/`MC-409`, expose one genuine well-factorable component, and test whether any legal reordering of dispersion, reciprocity, or completion places separate internal divisor factors into separate source/modulus slots before they recombine. If no such placement exists because the character conductor remains external, the Pascadi/Yang escape is structurally unavailable to this branch; if it does exist, the resulting reciprocal phase and its true diagonal become the next quantitative object.