---
id: WP-362
title: Canonical Eisenstein Hecke Euler completion is a modulus square; its Mangoldt readout imports the zeta divisor
branch: weil_positivity
status: supported
kind: hecke-euler-completion-obstruction
claim_strength: exact Hecke Dirichlet-series completion, central modulus-square positivity, and logarithmic-derivative divisor obstruction
created: 2026-09-18
related: [WP-243, WP-269, WP-270, WP-345, WP-352, WP-361]
clues: [CLUE-maass-selberg-remainder-sign-interface]
prior_art:
  - Henryk Iwaniec, Spectral Methods of Automorphic Forms, 2nd ed., AMS, 2002
  - W. Duke, O. Imamoglu, and A. Toth, Geometric invariants for real quadratic fields, Annals of Mathematics 184 (2016), 949-990, especially the Eisenstein Hecke L-function in Remark after Eq. (5.9)
  - Tian An Wong, Explicit formulas for the spectral side of the trace formula of SL(2), Acta Arithmetica 195 (2020), 149-175, DOI 10.4064/aa190115-9-10, arXiv:1608.02296
  - classical Euler product and logarithmic derivative of the Riemann zeta function
---

# WP-362 — Canonical Eisenstein Hecke Euler completion is a modulus square; its Mangoldt readout imports the zeta divisor

## Claim

`WP-361` leaves a precise escape after the ordinary critical all-prime Hecke packet fails to converge: perhaps the divergent prime packet should not be completed by an arbitrary summation rule at all, but by the **canonical Hecke Euler series already attached to the Eisenstein eigenline**. This is the strongest source-defined scalar completion of that route, and it does something genuinely attractive: it assembles every finite prime and, after completion, the archimedean Gamma factors in one global automorphic object.

That completion exists, but it separates the desired ingredients in the wrong way for Weil positivity.

For

\[
E_r(z):=E\!\left(z,\frac12+ir\right),
\qquad r\in\mathbb R,
\]

retain the normalized level-one Hecke eigenvalues from `WP-361`,

\[
\lambda_r(n)
=\sum_{d\mid n}\left(\frac{n}{d^2}\right)^{ir}
=n^{ir}\sigma_{-2ir}(n).
\tag{1}
\]

The associated Hecke Dirichlet series is, for `Re s>1`,

\[
\boxed{
D(s,r)
:=\sum_{n\ge1}\frac{\lambda_r(n)}{n^s}
=\zeta(s+ir)\zeta(s-ir).
}
\tag{2}
\]

Thus the canonical Euler completion of the all-Hecke packet is not a new unknown global object: it is exactly the classical Eisenstein Hecke `L`-function. Its completed form

\[
\boxed{
\mathcal D(s,r)
:=\pi^{-s}
\Gamma\!\left(\frac{s+ir}{2}\right)
\Gamma\!\left(\frac{s-ir}{2}\right)
\zeta(s+ir)\zeta(s-ir)
}
\tag{3}
\]

satisfies

\[
\mathcal D(s,r)=\mathcal D(1-s,r).
\tag{4}
\]

For real `sigma` and `r`, away from poles,

\[
D(\sigma,r)=|\zeta(\sigma+ir)|^2\ge0,
\tag{5}
\]

and likewise

\[
\boxed{
\mathcal D\!\left(\frac12,r\right)
=\pi^{-1/2}
\left|
\Gamma\!\left(\frac{1/2+ir}{2}\right)
\zeta\!\left(\frac12+ir\right)
\right|^2
\ge0.
}
\tag{6}
\]

So this canonical completion really does supply an unconditional positive scalar containing both the finite Euler product and the archimedean factor. But the positivity is only **conjugate-product positivity**. It is true for every possible off-critical zero pattern and therefore cannot imply Weil positivity or RH. Off-line zeros do not have to move, disappear, or change the sign of (6).

The operation that recovers the desired linear prime-power weights is the logarithmic derivative. In the absolutely convergent half-plane,

\[
\begin{aligned}
M(s,r)
&:=-\partial_s\log D(s,r)\\
&=-\frac{\zeta'}{\zeta}(s+ir)
  -\frac{\zeta'}{\zeta}(s-ir)\\
&=\sum_p\sum_{k\ge1}(\log p)
\left(p^{-k(s+ir)}+p^{-k(s-ir)}\right)\\
&=2\sum_p\sum_{k\ge1}
(\log p)p^{-ks}\cos(kr\log p).
\end{aligned}
\tag{7}
\]

At `s=1/2`, equation (7) has exactly the critical Mangoldt half-density

\[
(\log p)p^{-k/2}
\tag{8}
\]

on every prime power. This is the finite arithmetic normalization sought by the branch. However, the meromorphic continuation of `M` has poles precisely where `s+ir` or `s-ir` meets the zero/pole divisor of `zeta`. The divisor is therefore present **before** any positivity is read. Taking a modulus square of `M` restores a tautological positive quantity but squares the linear Weil carrier and its singularities; taking `M` linearly keeps the correct carrier but loses inherited positivity.

The source-defined Euler completion therefore exhibits a sharp bifurcation:

\[
\boxed{
\begin{array}{c}
\text{canonical completed Hecke }L\text{-value}
\end{array}
\Longrightarrow
\text{finite+archimedean global object and modulus-square positivity, but no Weil orientation},
}
\tag{9}
\]

whereas

\[
\boxed{
-\partial_s\log
\Longrightarrow
\text{exact critical Mangoldt prime-power carrier, but the zeta divisor is already encoded and positivity is gone}.
}
\tag{10}
\]

This closes the most direct **canonical Euler/analytic-continuation escape** left open by `WP-361` on the scalar level-one Eisenstein eigenline. The missing bridge cannot be merely “complete the divergent Hecke packet by its natural automorphic `L`-function.” A successful construction must add a genuinely non-scalar geometric sign theorem before or while the logarithmic/divisor readout is formed.

**Classification:** `CLASSICAL-EISENSTEIN-HECKE-L + EXACT-DERIVED + CANONICAL-EULER-COMPLETION + FINITE-ARCHIMEDEAN-ASSEMBLY + MODULUS-SQUARE-CONTROL + LOG-DERIVATIVE-DIVISOR-OBSTRUCTION + NEGATIVE/NARROWING + NO-NOVELTY-CLAIM-FOR-CLASSICAL-IDENTITIES`.

## 1. The all-Hecke Dirichlet series is forced and factors exactly

Starting from (1), write `n=dm`. Then

\[
\begin{aligned}
D(s,r)
&=\sum_{n\ge1}n^{-s+ir}
  \sum_{d\mid n}d^{-2ir}\\
&=\sum_{d,m\ge1}
  d^{-s-ir}m^{-s+ir}\\
&=\zeta(s+ir)\zeta(s-ir),
\end{aligned}
\tag{11}
\]

absolutely for `Re s>1`. No coefficient or regularizer has been fitted to the Weil target. The same Hecke eigenvalues that appear in the finite amplifiers of `WP-361` determine the series uniquely.

This is exactly the standard Hecke `L`-function of the level-one Eisenstein series. Duke--Imamoglu--Toth record the identical product and its completion (3), including the functional equation (4). Thus analytic continuation of this particular scalar all-prime packet is not speculative; it is classical automorphic structure.

This matters because `WP-361` only ruled out the ordinary increasing-prime limit of the critical coefficients. Equation (2) tests the most natural objection to that finding: perhaps the correct completion is supplied by the Hecke algebra itself through its Euler Dirichlet series. It is.

## 2. The canonical completion really does assemble finite and archimedean data

Equation (3) contains exactly the two sectors whose simultaneous source derivation has repeatedly been missing in more local Mathia constructions:

- the finite places enter through the Euler products of `zeta(s+ir)` and `zeta(s-ir)`;
- the archimedean place enters through the conjugate Gamma pair and the power of `pi`;
- meromorphic continuation and the functional equation are properties of the same completed object.

At the central value, complex conjugation gives

\[
\Gamma\!\left(\frac{1/2-ir}{2}\right)
=\overline{\Gamma\!\left(\frac{1/2+ir}{2}\right)},
\qquad
\zeta\!\left(\frac12-ir\right)
=\overline{\zeta\!\left(\frac12+ir\right)},
\tag{12}
\]

and hence (6). This is an honest unconditional sign statement for a global completed automorphic scalar.

But it is the wrong sign statement. It says only that an object times its complex conjugate is nonnegative. It is insensitive to whether nontrivial zeros also occur at `beta+i gamma` with `beta\ne1/2`. Such zeros change the meromorphic function away from the line but do not threaten (6). The same observation already holds before Gamma completion in (5) on **every** real vertical parameter `sigma` where the value is finite.

Thus even a canonical global completion that intrinsically includes the archimedean factor does not answer the research mandate merely by being positive. The positive structure must constrain the relevant divisor orientation, not only take a norm of a scalar carrying that divisor.

## 3. The exact Mangoldt carrier appears only after a logarithmic readout

The Euler product of (2) gives

\[
D(s,r)
=\prod_p
\frac1{(1-p^{-s-ir})(1-p^{-s+ir})}.
\tag{13}
\]

Taking `-partial_s log` yields (7). Since `n=p^k` has `Lambda(n)=log p`, this can be written

\[
M(s,r)
=2\sum_{n\ge2}
\frac{\Lambda(n)}{n^s}\cos(r\log n)
\qquad(\Re s>1).
\tag{14}
\]

Therefore the critical formal boundary is

\[
M\!\left(\frac12,r\right)
\sim
2\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}\cos(r\log n),
\tag{15}
\]

which is precisely the source arithmetic frequency/mass pair studied in `WP-269`--`WP-270`, now obtained from the Hecke-Eisenstein eigenline rather than inserted as an external prime measure.

The gain is canonicity of the finite carrier. The loss is decisive: the analytic continuation is

\[
M(s,r)
=-\frac{\zeta'}{\zeta}(s+ir)
 -\frac{\zeta'}{\zeta}(s-ir),
\tag{16}
\]

so each nontrivial zero `rho` produces poles on the two-variable divisors

\[
s+ir=\rho
\qquad\text{or}\qquad
s-ir=\rho.
\tag{17}
\]

In particular the restriction `s=1/2` meets every critical-line zero. Infinitely many such zeros are known unconditionally. The continuation that makes the divergent prime-power expression meaningful is therefore not a positive Hilbert completion of the critical packet; it is a meromorphic scalar whose singular divisor is the zeta divisor itself.

This does not make analytic continuation illegitimate. It establishes the logical order relevant to the mandate: **zero information enters through the meromorphic logarithmic derivative before any new positivity theorem appears**. A later square such as `|M|^2` cannot be counted as geometry forcing Weil positivity, because the divisor has already been encoded in the scalar being squared.

## 4. Completion at the center collapses the logarithmic derivative to the functional equation

The completed object makes the separation even clearer. Away from its zeros and poles,

\[
\partial_s\log\mathcal D(s,r)
=-\log\pi
+\frac12\psi\!\left(\frac{s+ir}{2}\right)
+\frac12\psi\!\left(\frac{s-ir}{2}\right)
+\frac{\zeta'}{\zeta}(s+ir)
+\frac{\zeta'}{\zeta}(s-ir),
\tag{18}
\]

where `psi=Gamma'/Gamma`. Since (4) is symmetric about `s=1/2`,

\[
\partial_s\log\mathcal D\!\left(\frac12,r\right)=0
\tag{19}
\]

whenever the logarithm is regular there. Consequently

\[
M\!\left(\frac12,r\right)
=-\log\pi
+\frac12\psi\!\left(\frac{1/2+ir}{2}\right)
+\frac12\psi\!\left(\frac{1/2-ir}{2}\right)
\tag{20}
\]

at every nonzero regular central value.

Equation (20) is not a new arithmetic identity; it is the differential form of the zeta functional equation on the critical line. At a critical-line zero the logarithmic derivative is singular instead. To turn those singularities into a zero sum one integrates against a test and shifts contours, i.e. one returns to the classical explicit-formula mechanism already audited in Wong/`PL-253` and `WP-270`.

Thus the completed Hecke function does not secretly provide an additional positive linear functional at the center. Its smooth logarithmic derivative is fixed by the archimedean functional equation between zeros, while the zero divisor appears as singularities. The nonnegative quantity (6) and the linear explicit-formula carrier (16) are different readouts with different sign behavior.

## 5. Aggressive falsification of nearby rescues

**Differentiate the positive scalar.** Positivity of `mathcal D(1/2,r)` does not imply a sign for its `s`-derivative; the completed first derivative is identically zero at regular central points by (19). Away from the center, derivatives of a positive-valued function need not have a fixed sign. No Weil inequality follows.

**Take the square of the logarithmic derivative.** `|M|^2` is nonnegative, but it is quadratic in the Mangoldt carrier and has squared singularities at the zeta divisor. The Weil explicit formula is linear in the prime-power distribution before the final positive-type test pairing. Squaring `M` changes the mathematical object rather than proving the required sign.

**Cancel the poles with zeta or xi factors.** Multiplying (16) by a factor designed to cancel its zero poles necessarily uses the same zeta/xi function whose divisor is being tested. Unless a separate source theorem derives that cancellation and a sign-preserving projection, this only hides the inserted divisor in the regularizer.

**Use Poincare--Lelong/Chern curvature of the scalar norm.** Applying `dd^c log|D|` can convert zeros into a positive divisor current in the complex parameter plane, but it is positive for zeros wherever they occur. It does not force support onto the critical line. This is the same structural failure already isolated for common scalar `L`-phases in `WP-352`.

**Use a different genuine automorphic `L`-channel as a matched control.** For a real primitive Dirichlet character `chi`, the analogous Eisenstein/Dirichlet channel has a central conjugate product built from `L(s+ir,chi)L(s-ir,chi)`, hence the same unconditional modulus-square positivity after the appropriate Gamma completion while its nontrivial zero divisor is different. This confirms that central conjugate-product positivity is a generic automorphic reality symmetry, not a selector of the Riemann divisor.

**Interpret analytic continuation as the missing Hilbert completion.** `WP-361` excluded the ordinary unrenormalized all-prime eigenline limit. Equation (16) gives a perfectly canonical meromorphic continuation, but meromorphic continuation of an eigenvalue is not convergence of vectors in the positive Maaß--Selberg Hilbert norm. The poles at the target divisor make that distinction concrete.

## 6. Relation to earlier branch obstructions

This finding does not duplicate `WP-269` or `WP-270`. `WP-269` starts from the already-derived critical Mangoldt positive measure and proves that its stationary Fourier covariance is too large for ordinary positive-definite distributions and Fourier hyperfunctions. `WP-270` then shows that subtracting the canonical zeta-pole background yields a tempered distribution exactly under RH.

Here the starting question is the different escape left explicitly open in `WP-361`: whether the divergent critical **Hecke amplifier** has a canonical Euler/automorphic continuation before one passes to generalized distributions. Equations (2)--(3) answer yes and identify it exactly. The new obstruction is the readout bifurcation: the canonical Hecke completion has unconditional norm-square positivity but no Weil-oriented linear carrier, while the canonical logarithmic operation that creates the linear critical Mangoldt carrier is exactly the zeta logarithmic derivative and therefore already carries the zero divisor.

Nor does this retract the Maaß--Selberg route. Wong's positive truncated spectral distribution remains a genuinely nonfactorizing Hilbert-space object. The result only says that **scalar Euler completion of the Hecke eigenvalue packet cannot be the missing projection** from that positive global distribution to the Weil zero form.

## 7. Prior-art and novelty audit

All analytic identities used above are classical. The Hecke eigenvalue formula and the factorization

\[
L(s;r)=\zeta(s+ir)\zeta(s-ir)
\]

are standard for the nonholomorphic Eisenstein series; Duke--Imamoglu--Toth state the product and completed functional equation explicitly, and Iwaniec gives the standard spectral/Hecke framework. The Euler-product logarithmic derivative (7) is the classical von Mangoldt expansion. Wong supplies the direct prior-art bridge from the logarithmic derivative of an automorphic normalizing factor to a Weil explicit formula and the associated positive Maaß--Selberg distribution.

No historical novelty is claimed for any of these ingredients, for central conjugate-product positivity, or for the fact that `zeta'/zeta` has poles at zeta zeros.

The line-specific substantive result is their exact combination against the `WP-361` escape: **the source-canonical all-Hecke continuation simultaneously solves the finite/global/archimedean assembly problem and demonstrates why that alone is insufficient. Its inherited positivity lives on the undifferentiated conjugate product, while the exact critical Mangoldt readout is obtained only by a logarithmic derivative whose meromorphic divisor is already the zeta divisor.** This is a decisive redirect rather than a new RH criterion.

## Consequence

The scalar level-one Eisenstein route is now narrower than “find a canonical renormalization of the divergent all-prime Hecke packet.” The most canonical one is already known and auditable: the Eisenstein Hecke `L`-function and its completion.

A surviving Weil-positivity mechanism must therefore act **before scalarization or beyond scalar modulus-square positivity**. It needs, for example, a genuinely operator-valued/multichannel truncation form, a cohomological/intersection structure, or another source-defined geometry in which the logarithmic/divisor operation itself is part of an independently positive theorem. Merely replacing the divergent prime cutoff of `WP-361` by its Euler/analytic continuation, even with the correct Gamma completion, produces classical zeta data plus tautological conjugate-product positivity rather than a geometric proof of the Weil sign.
