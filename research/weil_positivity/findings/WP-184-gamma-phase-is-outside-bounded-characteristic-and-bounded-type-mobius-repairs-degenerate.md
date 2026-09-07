# WP-184 — The Gamma phase is outside bounded characteristic, and bounded-type Möbius repairs degenerate

**Status:** `EXACT-DERIVED + NEVANLINNA-BOUNDED-CHARACTERISTIC-NO-GO + LINEAR-FRACTIONAL-CLOSURE + DECISIVE-NARROWING + MATCHED-INNER-CONTROL + PRIOR-ART-CLASSICALIZATION + NOT-WEIL-POSITIVITY`.

`WP-169` isolates the exact real-place relative phase

\[
R_\infty(z)
=\pi^{iz}
\frac{\Gamma(\tfrac14-\tfrac{iz}{2})}
     {\Gamma(\tfrac14+\tfrac{iz}{2})},
\tag{1}
\]

whose real boundary values are unimodular. `WP-170` proves that its upper-half-plane continuation is analytic but not Schur: its zeros

\[
z_n=i\left(2n+\frac12\right),\qquad n\ge0,
\tag{2}
\]

violate the Blaschke condition. `WP-183` then shows that no bounded analytic **linear** channel mixer can retain a nonzero `R_infty` component while producing bounded analytic outputs, and explicitly leaves linear-fractional/nonlinear and larger Smirnov/Nevanlinna categories open.

The first of those nonlinear escapes can be closed exactly, and the obstruction is stronger than boundedness. The phase (1) is not a function of **bounded characteristic** in the upper half-plane at all. Consequently no nondegenerate linear-fractional transformation with bounded-characteristic coefficients can turn it into a bounded-characteristic output. In particular, no bounded analytic, Smirnov-class, or ordinary Nevanlinna bounded-type Möbius/Cayley/feedback regularization can retain the exact Gamma phase after the quotient has been formed.

Let `N_bc(H)` denote the meromorphic field of functions of bounded characteristic on the upper half-plane `H`, equivalently quotients of two bounded analytic functions. This is the classical Nevanlinna bounded-type class; it is **not** the same terminology as the Herglotz--Nevanlinna positive-imaginary-part class used for Weyl functions elsewhere in this line.

Then

\[
\boxed{R_\infty\notin N_{bc}(\mathbb H).}
\tag{3}
\]

More strongly, let

\[
a,b,c,d\in N_{bc}(\mathbb H),
\qquad
\Delta:=ad-bc\not\equiv0,
\tag{4}
\]

and suppose a meromorphic function `S` satisfies the linear-fractional relation

\[
S(c+dR_\infty)=a+bR_\infty.
\tag{5}
\]

Then

\[
\boxed{S\notin N_{bc}(\mathbb H).}
\tag{6}
\]

Thus every bounded-characteristic linear-fractional transform of `R_infty` that lands back in bounded characteristic must be **degenerate**, `ad-bc=0`; pointwise as a projective map it then carries no recoverable `R_infty` dependence. Any genuine post-quotient cancellation of the Gamma divisor must therefore leave bounded characteristic itself or use an operation not rationally invertible at linear-fractional level.

This is still not a Weil positivity theorem. It is a category obstruction on the strongest exact archimedean phase found by the line. Its value is that an escape explicitly left open by `WP-183` is no longer available: replacing bounded linear mixing by ordinary stable Möbius/Cayley/feedback algebra does not help.

## 1. The Gamma phase is not of bounded characteristic

A nonzero analytic function of bounded characteristic in the upper half-plane has a canonical factorization whose zero divisor is a Blaschke divisor. In particular, if its zeros are `w_j`, counted with multiplicity, then necessarily

\[
\sum_j\frac{\operatorname{Im}w_j}{1+|w_j|^2}<\infty.
\tag{7}
\]

For (1), `WP-170` derives the exact zeros (2). Hence

\[
\sum_{n\ge0}
\frac{\operatorname{Im}z_n}{1+|z_n|^2}
=
\sum_{n\ge0}
\frac{2n+\tfrac12}{1+(2n+\tfrac12)^2}
=\infty,
\tag{8}
\]

because the summand is asymptotic to `1/(2n)`. Therefore the analytic function `R_infty` cannot belong to `N_bc(H)`, proving (3).

This strengthens the `H^infinity` statement in `WP-170`--`WP-183`. The obstruction is not merely that `R_infty` grows too much to be bounded. It cannot even be represented meromorphically as a quotient of bounded analytic functions in the upper half-plane.

An immediate field-theoretic corollary extends the multiplier result of `WP-183`. If

\[
m\in N_{bc}(\mathbb H),\qquad m\not\equiv0,
\tag{9}
\]

then

\[
\boxed{mR_\infty\notin N_{bc}(\mathbb H).}
\tag{10}
\]

Indeed, if both `m` and `mR_infty` were of bounded characteristic, their quotient would put `R_infty` in the same field, contradicting (3). Thus even a meromorphic bounded-type multiplier cannot provide the infinite divisor compensation required by `WP-170`. Any multiplier capable of doing so must itself lie outside bounded characteristic.

The same argument gives the affine version: if `a,b,f in N_bc(H)` and

\[
f=a+bR_\infty,
\tag{11}
\]

then `b` must vanish identically. Otherwise `(f-a)/b=R_infty` would belong to `N_bc(H)`. Equation (11) is the bounded-characteristic extension of the `H^infinity` channel theorem in `WP-183`.

## 2. Nondegenerate bounded-type linear-fractional regularization is impossible

Assume (4)--(5) and suppose, toward contradiction, that

\[
S\in N_{bc}(\mathbb H).
\tag{12}
\]

Cross-multiplying (5) gives the meromorphic identity

\[
(Sd-b)R_\infty=a-Sc.
\tag{13}
\]

Every coefficient in (13) belongs to the field `N_bc(H)`. There are now only two cases.

If

\[
Sd-b\not\equiv0,
\tag{14}
\]

then

\[
R_\infty
=\frac{a-Sc}{Sd-b}
\in N_{bc}(\mathbb H),
\tag{15}
\]

contradicting (3).

If instead

\[
Sd-b\equiv0,
\tag{16}
\]

then (13) forces `a-Sc=0` as well. Hence

\[
b=Sd,
\qquad
a=Sc,
\tag{17}
\]

and therefore

\[
\Delta
=ad-bc
=(Sc)d-(Sd)c
=0,
\tag{18}
\]

contradicting the nondegeneracy assumption in (4).

Thus (12) is impossible and (6) follows.

No contractivity or positivity hypothesis was used. The coefficients may already be meromorphic functions of bounded characteristic, and `S` need only be of bounded characteristic, not Schur. Consequently the no-go contains as special cases:

- constant Möbius transforms of the exact Gamma phase;
- bounded analytic linear-fractional filters;
- Smirnov-class linear-fractional regularizations, since the Smirnov class lies inside bounded characteristic;
- finite cascades of bounded-type Möbius/Cayley stages whose overall projective matrix has nonzero determinant.

For a finite cascade, the coefficient matrices multiply. Their entries remain in `N_bc(H)` and the determinant is the product of the stage determinants. Hence a cascade that is nondegenerate overall is again covered by (4)--(6).

## 3. What degeneration means: bounded output is possible only after projective erasure

The determinant condition is not a technical inconvenience. For fixed `z`, the projective map

\[
r\longmapsto\frac{a(z)+b(z)r}{c(z)+d(z)r}
\tag{19}
\]

has derivative

\[
\frac{bc-ad}{(c+dr)^2}.
\tag{20}
\]

When `ad-bc=0`, it is constant in the projective variable wherever defined. Its value may still vary with `z` through the coefficient functions, but that variation is supplied by the coefficients, not by `R_infty`. Thus the only bounded-type Möbius outputs allowed by the theorem are exactly the algebraically nonfaithful ones.

This sharpens the interpretation of `WP-183`. There, bounded analytic **linear** outputs could exist only after the `R_infty` column was killed. Here, bounded-characteristic **linear-fractional** outputs can exist only after the projective dependence on `R_infty` is killed.

The distinction is important for feedback and scattering models. A Cayley or Redheffer-style scalar feedback formula often appears to have more freedom than a linear mixer because a denominator can cancel unwanted growth. Equations (13)--(18) show that ordinary bounded-type denominator freedom is still insufficient for this exact phase. If the output remains in bounded characteristic and the transform is nondegenerate, the denominator makes `R_infty` recoverable as a bounded-type quotient, which is impossible.

## 4. Matched controls

The obstruction is specific to the non-Blaschke Gamma divisor, not to Möbius transforms themselves.

Let `B` be any ordinary scalar inner function in the upper half-plane and let `alpha` lie in the unit disk. The disk automorphism

\[
S_B(z)
=\frac{B(z)-\alpha}{1-\overline\alpha B(z)}
\tag{21}
\]

is again inner and therefore belongs to `H^infinity subset N_bc`. Its coefficient matrix has determinant `1-|alpha|^2`, so the transform is nondegenerate. Thus exactly the same projective operation that fails for `R_infty` works perfectly for a genuine passive inner phase.

There is also a boundary-only control. Because `|R_infty(t)|=1` for real `t`, the same Möbius formula applied pointwise to the boundary values gives another unimodular measurable function whenever `|alpha|<1`. Nothing in the theorem forbids that boundary identity. What fails is the claim that this nondegenerate transformed phase is the boundary trace of a bounded-characteristic analytic output obtained by the same post-quotient formula in the upper half-plane.

Finally, determinant-zero transforms are allowed and give the expected trivial control. Choosing coefficients with `a=Sc` and `b=Sd` makes (5) hold identically for any prescribed bounded-type `S`, but the apparent output has been put into the coefficients in advance and is independent of the phase variable. This is precisely the sort of target insertion that cannot count as a geometric explanation.

## 5. Aggressive falsification and exact scope

The theorem closes only a specific post-quotient analytic category.

**It does not rule out coupling before the quotient.** `R_infty` appears in `WP-169` only after dividing two canonical spectral factors. A source-derived operation acting on those unnormalized factors may alter the divisor before any projective ratio is formed. That remains the most relevant surviving architecture for the line mandate.

**It does not classify arbitrary nonlinear maps.** A genuinely nonlinear, non-rationally-recoverable operation on `R_infty` need not preserve enough information for the field argument (13)--(15). Such an operation would need its own canonicity, domain, positivity, and target-fitting audit. Merely applying a nonlinear function chosen to tame the known Gamma factor would still fail the mandate's no-hand-picked-regularization gate.

**It does not rule out coefficients outside bounded characteristic.** An infinite meromorphic compensation with a non-Blaschke pole divisor can in principle cancel the zeros (2). The result says exactly that such compensation cannot come from the usual bounded-type/Smirnov stable analytic algebra. The compensator must carry analytic singularity of comparable severity and therefore needs an independent Mathia-native origin and coercivity theorem.

**It does not classify indefinite or changing-domain operator geometry.** Generalized Nevanlinna/Pontryagin systems, singular relation limits, nonclosable boundary maps, and other category changes may produce scalar observables outside `N_bc`. Their positivity cannot be inherited merely from the bounded-type algebra ruled out here.

**It creates no finite-prime or polar term.** This is an archimedean architecture obstruction. It does not generate Mangoldt support, the critical finite coefficient, mixed-prime incidence, or the polar counterterms required by the full Weil form.

The decisive falsification test for the present claim is exact: exhibit `a,b,c,d,S` of bounded characteristic satisfying (4)--(5) with `ad-bc` nonzero. Equations (13)--(18) show that such an example would contradict the standard field property or the established non-Blaschke zero divisor (2); there is no numerical or RH-dependent step in the argument.

## 6. Prior art and novelty audit

No novelty is claimed for functions of bounded characteristic, their quotient representation, Blaschke zero condition, field closure, or linear-fractional algebra. These are classical one-variable function theory. A standard half-plane factorization reference is Louis de Branges, *Hilbert Spaces of Entire Functions* (Prentice-Hall, 1968), Chapter 1, §9, where bounded-type functions in a half-plane are factored into a Blaschke product and zero-free exponential factors. John B. Garnett, *Bounded Analytic Functions* (Springer GTM 236, 2007), is the standard Hardy/Blaschke reference already used in `WP-170`.

A targeted literature search by bounded characteristic, Nevanlinna class, linear-fractional transformations, and Gamma ratios found the expected classical factorization/quotient theory and unrelated bounded-type Gamma-ratio families, but no separate theorem is needed here. Absence of wording matching (6) is not evidence of novelty.

The substantive Mathia-specific delta is the application of those classical facts to the exact source-derived divisor of `R_infty`, together with the projective algebra (13)--(18). `WP-183` explicitly left linear-fractional transforms and larger Smirnov/Nevanlinna categories outside its theorem. The present result closes their ordinary bounded-characteristic overlap:

\[
\boxed{
R_\infty\notin N_{bc}
\quad\Longrightarrow\quad
\text{nondegenerate }N_{bc}\text{-Möbius repair cannot land in }N_{bc}.
}
\tag{22}
\]

This is a project-specific no-go derived from classical factorization, not a new theorem of Nevanlinna theory and not a claim of Weil positivity.

## 7. Consequence for the Weil-positivity search

The post-quotient archimedean route is now narrower than after `WP-183`. The exact Gamma phase cannot be stabilized by bounded analytic linear mixing; it is not even of bounded characteristic; multiplying it by any nonzero bounded-type factor cannot bring it into that class; and a nondegenerate bounded-type Möbius/Cayley/feedback transformation cannot do so either.

Therefore an ordinary stable analytic completion cannot obtain the `WP-182` positive Schur geometry by first isolating `R_infty` and then hiding its divisor in a denominator. A genuine repair must instead do at least one of three things: act **before** the Nyman/Gamma quotient is formed; introduce a source-forced compensating object outside bounded characteristic; or move to a genuinely different nonlinear/domain/indefinite category with its own independent positivity theorem.

For the research mandate the first option remains the structurally preferred one. The missing object is still not another regularization of a known Gamma factor, but a single finite--archimedean construction in which the arithmetic selector, real-place contribution, and sign theorem arise before scalar quotienting destroys the geometry.

## Dependencies

- `research/weil_positivity/findings/WP-169-pointed-nyman-relative-phase-is-exact-archimedean-scattering.md`
- `research/weil_positivity/findings/WP-170-archimedean-phase-is-not-a-passive-inner-boundary-response.md`
- `research/weil_positivity/findings/WP-176-nevanlinna-relation-valued-passive-limits-cayley-back-to-schur.md`
- `research/weil_positivity/findings/WP-182-pythagorean-defect-completion-cancels-dissipative-pole-but-controls-total-phase.md`
- `research/weil_positivity/findings/WP-183-gamma-relative-phase-cannot-survive-bounded-analytic-linear-channel-mixing.md`

## Bottom line

The exact Gamma phase found by the pointed/Nyman bridge has a stronger analytic obstruction than non-Schur behavior: its non-Blaschke zero divisor puts it outside the entire field of meromorphic bounded-characteristic functions. Field closure then turns every nondegenerate bounded-type linear-fractional regularization into a contradiction, because a bounded-type output would algebraically recover `R_infty` as a bounded-type quotient. Degenerate transforms are the only bounded-type escape, and they erase the phase projectively.

So the obvious nonlinear continuation of `WP-183` fails. If the Gamma divisor is to participate in a positive global Weil geometry, its compensation must already be present upstream in the Mathia source construction or must come from a genuinely more singular analytic category whose positivity is independently justified.