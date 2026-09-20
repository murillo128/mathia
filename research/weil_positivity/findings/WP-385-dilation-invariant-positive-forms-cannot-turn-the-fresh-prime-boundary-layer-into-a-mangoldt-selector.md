---
id: WP-385
title: Dilation-invariant positive forms cannot turn the fresh-prime boundary layer into a Mangoldt selector
branch: weil_positivity
status: supported
kind: pointed-boundary-dilation-positive-form-obstruction
claim_strength: exact RH-independent no-go showing that every closed positive form on the WP-384 fresh-prime boundary space that is invariant under the source scaling action sees each fixed-base boundary profile as boundedly equivalent to the prime profile through an everywhere-invertible finite Euler multiplier; hence no nonzero such form can give positive prime energy while nulling even one mixed-prime base, and arbitrary fixed nonnegative Mellin reweighting cannot create prime-power support or the missing Weil completion
created: 2026-09-20
related: [WP-168, WP-374, WP-375, WP-383, WP-384]
clues: [CLUE-weil-positivity-noncharacter-finite-archimedean-incidence]
prior_art:
  - classical Mellin-Plancherel diagonalization of the unitary dilation group on L2(R_+,dx)
  - classical spectral theorem/commutant description of closed positive forms invariant under a multiplicity-one unitary translation or dilation representation
  - Nyman--Beurling/Muentz Mellin geometry already audited in WP-168 and SOURCES.md
  - WP-384 finite Euler/Jordan multiplier c_m(tau)=m^{-i tau} product_{p|m}(1-p^{-1/2+i tau})
---

# WP-385 — Dilation-invariant positive forms cannot turn the fresh-prime boundary layer into a Mangoldt selector

## Claim

`WP-384` found the first canonical boundary layer that genuinely escapes the compact-open collapse of `WP-383`. For a fixed base `m` and a fresh prime `q`, the critically normalized cyclotomic shell has a nonzero boundary limit represented by

\[
h_m(x)=\frac1{\sqrt m}\sum_{d\mid m}\mu(m/d)a(x/d),
\qquad h_1=a,
\tag{1}
\]

and Mellin transform

\[
\widehat h_m(\tau)=c_m(\tau)\widehat h_1(\tau),
\qquad
c_m(\tau)=m^{-i\tau}\prod_{p\mid m}
\left(1-p^{-1/2+i\tau}\right).
\tag{2}
\]

`WP-384` tested the intrinsic pointed `D_1` norm and found a finite-Euler-weighted Nyman Gram. A natural remaining escape is to keep the same source-forced boundary profiles but replace `D_1` by some other positive geometry that is still stationary under the underlying scale action. That whole class can be closed exactly.

Let

\[
H=L^2(\mathbb R_+,dx),
\qquad
(D_r f)(x)=r^{-1/2}f(x/r),
\quad r>0,
\tag{3}
\]

and let `Q` be a densely defined closed positive-semidefinite quadratic form on `H` whose form domain is invariant under every `D_r` and satisfies

\[
Q(D_r f)=Q(f).
\tag{4}
\]

Assume the prime boundary profile `h_1` has finite `Q`-energy. Then for every integer `m>=1`, `h_m` also belongs to the form domain and

\[
\boxed{
\alpha_m^2 Q(h_1)
\le Q(h_m)\le
\beta_m^2 Q(h_1),
}
\tag{5}
\]

where

\[
\alpha_m:=\prod_{p\mid m}(1-p^{-1/2})>0,
\qquad
\beta_m:=\prod_{p\mid m}(1+p^{-1/2}).
\tag{6}
\]

The converse domain implication also holds: `h_m` has finite `Q`-energy if and only if `h_1` does.

Consequently a nonzero dilation-invariant positive boundary geometry cannot implement the required arithmetic support. If `Q(h_1)>0`, then

\[
\boxed{Q(h_m)>0\quad\text{for every }m>1.}
\tag{7}
\]

But for every fixed `m>1` and every fresh prime `q`, the prelimit shell `mq` has at least two distinct prime divisors and therefore

\[
\Lambda(mq)=0.
\tag{8}
\]

Thus **even one exact mixed-base nullity condition `Q(h_m)=0` forces `Q(h_1)=0`**. Requiring all mixed shells to be null does not leave a small prime-power sector: it kills the prime boundary carrier itself.

This obstruction is stronger than the particular `D_1` calculation in `WP-384`. Any fixed nonnegative Mellin spectral reweighting, including an unbounded one defining a closed form, leaves the finite Euler factors in (2) boundedly invertible. Such a weight may change the metric, but it cannot turn the boundary packet into Mangoldt support. Nor can the arithmetic packet generate a Gamma or polar term through this operation: those contributions would have to be inserted entirely into the common spectral weight, while the finite arithmetic part would still satisfy (5).

The route closed here is therefore

\[
\boxed{
\text{fresh-prime boundary escape}
+\text{one closed scale-stationary positive form}
\not\Rightarrow
\text{prime-power selection or global Weil positivity}.
}
\tag{9}
\]

A surviving boundary construction must break at least one ingredient used above: it must be genuinely nonstationary/off-diagonal in scale, retain the finite-`q` prelimit before taking the positive scalar, use an indefinite intermediate coupling, or couple finite and archimedean data before the boundary profiles are reduced to the common Mellin multiplier class.

**Classification:** `EXACT-DERIVED + RH-INDEPENDENT + FRESH-PRIME-BOUNDARY + CLOSED-POSITIVE-FORM + DILATION-COVARIANCE + MELLIN-SPECTRAL-CLASSIFICATION + FINITE-EULER-BOUNDED-INVERTIBILITY + MIXED-SHELL-NULLITY-NO-GO + NYMAN-CLASSICALIZATION + MATCHED-CONTROL + NO-ZERO-DATA + NOT-A-WEIL-PROOF`.

## 1. The finite Euler multiplier has no critical-line zeros

The only arithmetic fact needed beyond `WP-384` is the elementary pointwise bound in (2). For real `tau`,

\[
|m^{-i\tau}|=1
\tag{10}
\]

and, for each prime `p|m`,

\[
1-p^{-1/2}
\le
\left|1-p^{-1/2+i\tau}\right|
\le
1+p^{-1/2}.
\tag{11}
\]

Multiplying (11) over the finitely many prime divisors of `m` gives

\[
\boxed{
0<\alpha_m\le |c_m(\tau)|\le\beta_m<\infty
\qquad(\tau\in\mathbb R).
}
\tag{12}
\]

So `c_m` is not merely nonzero almost everywhere. It is a boundedly invertible multiplier on the entire real Mellin axis. This is the decisive distinction from a factor whose zeros might allow a positive spectral form to annihilate selected arithmetic sectors.

The estimate is insensitive to prime-power exponents except for the harmless phase `m^{-i tau}`. The diagonal multiplier modulus depends only on `rad(m)`, exactly matching the information loss already visible in `WP-384`.

## 2. Every closed dilation-invariant positive form is a Mellin weight

Use the unitary Mellin transform

\[
(\mathcal Mf)(\tau)
=\int_0^\infty f(x)x^{-1/2-i\tau}\,dx
\tag{13}
\]

with the usual Plancherel normalization. Under (3),

\[
\mathcal M(D_r f)(\tau)
=r^{-i\tau}(\mathcal Mf)(\tau).
\tag{14}
\]

Let `A>=0` be the nonnegative self-adjoint operator associated with the closed form `Q`, so

\[
Q(f)=\|A^{1/2}f\|_2^2.
\tag{15}
\]

Form invariance (4) implies that `A` strongly commutes with the dilation group. After Mellin transform, that group is the multiplicity-one family of multiplication operators `r^{-i tau}`. Its commutant is the scalar multiplication algebra. Hence `A` is multiplication by a measurable function `w(tau)>=0`, possibly unbounded, and

\[
\boxed{
Q(f)=\frac1{2\pi}\int_{-\infty}^{\infty}
 w(\tau)|\widehat f(\tau)|^2\,d\tau,
}
\tag{16}
\]

with form domain

\[
\mathcal D(Q)
=\left\{f\in H:
\int w(\tau)|\widehat f(\tau)|^2d\tau<\infty
\right\}.
\tag{17}
\]

No smoothness, boundedness, locality, differential order, or particular formula for `w` is assumed. The only structural input is one common closed positive geometry invariant under the source dilation action.

Substituting (2) into (16) gives

\[
Q(h_m)=\frac1{2\pi}\int
w(\tau)|c_m(\tau)|^2
|\widehat h_1(\tau)|^2d\tau.
\tag{18}
\]

The uniform bounds (12) immediately imply (5). They also show that multiplication by `c_m` and by `c_m^{-1}` preserve the weighted form domain, proving the domain equivalence.

This proof does not use RH, a zero expansion, a regularization, a fitted kernel, or a special choice of spectral weight.

## 3. Exact mixed-shell nullity is impossible in this class

The intended arithmetic selector distinguishes the fresh-prime base `m=1` from every `m>1`: the shell `q` is a prime power, while `mq` with `q` fresh and `m>1` is not. In the boundary limit, however, the passage from `h_1` to `h_m` is multiplication by the invertible function `c_m`.

Therefore (5) gives the dichotomy

\[
Q(h_1)=0
\quad\Longleftrightarrow\quad
Q(h_m)=0
\qquad(m>=1).
\tag{19}
\]

For an explicit matched control take `m=6`. Then

\[
|c_6(\tau)|^2
\ge
(1-2^{-1/2})^2(1-3^{-1/2})^2>0,
\tag{20}
\]

so every nonzero `Q`-energy on the prime boundary packet forces strictly positive energy on the `6q` boundary packet, even though `Lambda(6q)=0` for every fresh prime `q`.

This is not a finite-truncation artifact. At any finite collection of test vectors one can manufacture positive forms with prescribed finite nullspaces. What prevents the desired selector here is the exact source identity (2) together with a **single scale-stationary form on the limiting boundary space**: all fixed-base packets lie in the same boundedly invertible Mellin orbit.

The theorem also explains why changing the positive scale metric cannot repair `WP-384`. If one replaces the pointed norm by any fixed positive multiplier `w`, the Gram becomes

\[
Q(h_m,h_n)
=\frac1{2\pi}\int
w(\tau)c_m(\tau)\overline{c_n(\tau)}
|\widehat h_1(\tau)|^2d\tau.
\tag{21}
\]

The arithmetic dependence is still only the finite Euler packet `c_m overline{c_n}` multiplying the same Nyman carrier. A common positive spectral weight can reweight that carrier but cannot create the missing prime-power support.

## 4. Relation to the earlier no-go results

This result is not a restatement of `WP-374` or `WP-375`. Those findings start from the inward cyclotomic radial flux `rho_n`, use the exact coboundary relation after logarithmic radial projection, and show that imposing mixed-shell zero energy collapses stationary or closable positive radial forms. `WP-385` starts from the different boundary layer that deliberately escaped the compact-open and radial-`L2` mechanisms: the `WP-384` profiles survive at the pointed boundary with nonzero energy.

The new obstruction is correspondingly different and simpler. It does not use density of spectator-prime translations, Mazur convexification, or closure of the mixed-shell span. The fixed-base boundary profiles are already spectrally equivalent by the boundedly invertible Euler multiplier (12). Thus even an exotic unbounded but closed dilation-invariant positive form cannot separate the prime packet from a mixed packet.

Nor is the claim merely `WP-168` again. `WP-168` identifies the base scaling limit as the classical Nyman modulus-square carrier. `WP-384` derives the exact finite-Euler deformation produced by adjoining a fixed base before a fresh prime. `WP-385` uses the fact that those finite Euler deformations are uniformly invertible on the critical line to classify **all closed positive dilation-invariant reweightings of that boundary space** with respect to the selector question.

## 5. Representation audit

### Intrinsic/source representation

The objects are the source-forced critical fresh-prime boundary profiles obtained from cyclotomic shells in `WP-384`. No zeta zero, explicit-formula kernel, Gamma factor, or Mangoldt support mask is inserted. The symmetry tested is the same continuous dilation action that becomes translation on logarithmic scale and is already intrinsic to the scaling limit.

### Transform representation

Mellin transform is used only to diagonalize that intrinsic dilation symmetry. In this representation, the arithmetic transition `h_1 -> h_m` is the finite Euler multiplier `c_m`, while a common closed positive dilation-invariant geometry is a nonnegative multiplier `w`. The no-go is the pointwise inequality (12), not a numerical fit.

### What scalarization forgets

Once positivity is imposed by a stationary Mellin weight, `c_m` cannot create a null sector because it never vanishes. On the diagonal, prime-power exponents survive only in a unit-modulus phase and are therefore invisible. This is precisely the wrong direction for a Weil bridge: the form keeps unconditional positive size while losing the arithmetic support distinction that the finite explicit-formula term needs.

### Surviving representations

The theorem does not rule out a non-dilation-invariant boundary operator, a form with genuine off-diagonal coupling between Mellin frequencies, a `q`-dependent/prelimit response before `q -> infinity`, a source-forced topology outside the closed-form setting, or an indefinite finite--archimedean incidence whose sign is taken only after global assembly. Those possibilities must be tested separately and cannot claim support from (5).

## 6. Adversarial and matched controls

**Control: arbitrary positive spectral weight.** Equation (16) allows any measurable `w>=0`, including unbounded weights and weights vanishing on large sets. Because `c_m` has a strictly positive pointwise lower bound, no such weight can make `h_m` null while leaving `h_1` nonnull.

**Control: one mixed base is enough.** The obstruction does not rely on nulling an infinite family. The single exact control `m=6` already forces the contradiction through (20).

**Control: fixed archimedean reweighting.** Multiplying by a fixed nonnegative real-place spectral density changes `w` but leaves (5) unchanged. Therefore a fixed Gamma-shaped positive multiplier cannot by itself turn the finite boundary packet into Mangoldt support. This does not rule out a nonpositive or off-diagonal archimedean coupling before the final sign theorem.

**Control: finite prelimit.** The theorem concerns the canonical fresh-prime boundary limit. It does not claim that every finite-`q` operator has this rigidity. A genuinely `q`-dependent construction that uses terms discarded by the limit remains outside the theorem; it must show that those terms survive globally rather than being a finite-cutoff interpolation artifact.

**Control: dropping dilation covariance.** If (4) is removed, the spectral multiplier classification no longer applies. This is a real escape, not a technical loophole. It moves the burden to deriving a nonstationary or cross-frequency operator from the source geometry and then matching its finite and archimedean coefficients.

## 7. Prior-art and novelty audit

The abstract ingredients are classical. Mellin-Plancherel diagonalizes positive dilations; the spectral theorem identifies a closed positive form commuting with this multiplicity-one group with multiplication by a nonnegative measurable weight. The Nyman--Beurling/Muentz interpretation of the base carrier is also classical and is already recorded in `SOURCES.md` through Bagchi and Burnol, with the related Baez-Duarte literature checked again for this pass.

The Mathia-specific content is narrower: combining the exact `WP-384` fresh-prime boundary packet with the elementary critical-line bound (12) shows that **every** closed scale-stationary positive metric sees all fixed bases as mutually boundedly equivalent. The external audit found the expected classical Nyman/Mellin machinery but no source in the checked literature asserting this particular finite-Euler bounded-invertibility no-go for the Mathia packet. Accordingly this finding does not claim a new abstract spectral theorem or a new RH criterion; it records a branch-specific exact obstruction.

This also separates the result from known RH-equivalent Nyman projection criteria. No density/totality assertion, zero-defined projection, or conditional positivity is used. The conclusion is negative and unconditional.

## 8. Implication for the research line

`WP-384` showed that reaching the boundary is necessary but not sufficient. `WP-385` now removes the most natural attempt to repair that boundary escape by choosing a better positive scale-stationary metric. The finite Euler factors produced by the intrinsic fixed-base incidence are too weak: on the critical line they are units, so positive dilation-invariant geometry cannot convert them into arithmetic support.

The next viable test should therefore happen **before stationary positive scalarization**. In particular, a candidate should exhibit either a source-forced cross-frequency/nonstationary boundary response or a finite--archimedean coupling in which the mixed-prime channel remains signed until the archimedean and polar pieces have interacted. Merely replacing the `D_1` norm by another positive Mellin weight is now closed.
