---
title: "WP-431: Critical prime-coherent semigroup field has a sharp KMS domain collapse"
type: research-finding
status: verified
research_question: "Can the arithmetic semigroup shifts themselves provide the source-canonical cross-frequency coherent selector left open by WP-430 at the critical Bost--Connes half-density?"
claim_strength: exact_infinite_domain_no_go_for_one_sided_prime_semigroup_field
scope: standard positive-energy Bost--Connes/Hardy representation on l2(N); one-sided prime-coherent formal sums and their finite-prime cutoffs; no claim for bidirectional, nonlinear, rigged-space, or archimedean completions
finding_id: WP-431
related_findings:
  - WP-209
  - WP-227
  - WP-268
  - WP-296
  - WP-429
  - WP-430
related_clues:
  - CLUE-bost-connes-affiliation-conditioning-boundary
created: 2026-09-24
updated: 2026-09-24
tags:
  - weil-positivity
  - bost-connes
  - hardy-dirichlet
  - coherent-selector
  - kms-criticality
  - domain
  - no-go
---

# WP-431: Critical prime-coherent semigroup field has a sharp KMS domain collapse

## Executive summary

`WP-430` leaves one narrow finite-control escape: use **additional arithmetic source structure**, rather than the bare Gibbs pair, to select a nonzero-Bohr coherent mixer. The most direct Bost--Connes candidate is already present in the source: its canonical multiplicative isometries

`mu_p e_n = e_{pn}`

on `l2(N)`, with Hamiltonian `H e_n=(log n)e_n`. A prime-coherent selector would therefore begin with a formal field

`T_a = sum_p a_p mu_p`.

There is an exact Hilbert-domain obstruction. Give this formal sum its maximal coefficientwise domain

`D(T_a)={f in l2(N): T_a f in l2(N)}`.

Then

`D(T_a)={0}` **whenever** `sum_p |a_p|^2=infinity`, while finitely supported vectors lie in `D(T_a)` whenever `a in l2(P)`. Thus square summability is the sharp threshold for a nontrivial dense domain in this one-sided prime field.

For the canonical thermal family

`a_p(beta)=p^(-beta/2)`,

this threshold is exactly

`beta>1`.

At the critical Bost--Connes boundary `beta=1`, the half-density coefficients `p^(-1/2)` satisfy `sum_p 1/p=infinity`, so the maximal formal operator has **trivial domain**. If the logarithmic Weil weight is put directly into the coherent field, `a_p=(log p)/sqrt(p)`, the obstruction is stronger still. If instead the `log p` is intended to come from the source Hamiltonian through `[H,mu_p]=(log p)mu_p`, the underlying half-density field has already collapsed before that derivative can be used.

Consequently the simplest source-canonical answer to the `WP-430` gap -- coherently summing the arithmetic semigroup shifts with the critical KMS amplitudes -- does not define a densely defined Hilbert-space selector at all. Finite-prime versions exist, but their norm on the vacuum diverges, and any scalar normalization that keeps them uniformly bounded erases every fixed prime amplitude in the limit.

This is a no-go for the **one-sided analytic semigroup field**, not for the full Bost--Connes source and not for global Weil positivity. A surviving mechanism must use genuinely different structure: for example a bidirectional or cancellation-bearing correspondence, a quadratic/form-level construction not represented by this multiplier, a rigorously justified rigged/distributional completion, or another source geometry. It must still recover the exact prime-power coefficients together with the Gamma and polar sectors.

## Exact theorem: sharp domain threshold

Let `P` be the primes and let `mu_p` act on `l2(N)` by

`mu_p e_n=e_{pn}`.

For a complex coefficient family `a=(a_p)_{p in P}`, define the formal coefficientwise operator

`T_a=sum_p a_p mu_p`.

Every individual output coefficient is a finite sum, explicitly

`(T_a f)(m)=sum_{p|m} a_p f(m/p)`,

so the formal action is unambiguous on arbitrary sequences. Give it the maximal Hilbert domain

`D(T_a)={f in l2(N): ((T_a f)(m))_m in l2(N)}`.

Then:

1. If `a notin l2(P)`, then `D(T_a)={0}`.
2. If `a in l2(P)`, every finitely supported vector belongs to `D(T_a)`, so `D(T_a)` is dense in `l2(N)`.

Hence `a in l2(P)` is the exact threshold between a densely defined one-sided prime field and complete domain collapse.

Under the Bohr transform, `l2(N)` is the Hardy--Dirichlet space `H^2`, equivalently the `H^2` geometry of the infinite prime polytorus/polydisc, and `mu_p` is multiplication by the prime coordinate `z_p`. The theorem therefore says that the formal linear symbol

`A(z)=sum_p a_p z_p`

has a nontrivial maximal multiplication domain on this `H^2` exactly when its degree-one coefficient vector belongs to `l2(P)`.

## Proof

Decompose `l2(N)` by total prime degree

`l2(N)=direct_sum_{d>=0} H_d`,

where `H_d` is spanned by `e_n` with `Omega(n)=d`, counting prime factors with multiplicity. Every `mu_p` raises degree by one, so `T_a` maps formal degree `d` coefficients only into degree `d+1`.

Assume `f!=0` and choose any degree `d` for which the homogeneous component of `f` is nonzero. Pick `n` with `Omega(n)=d` and

`c:=f(n)!=0`.

Let `S` be the finite set of primes dividing `n`. For every prime `p notin S`, inspect the output coefficient at `np`. The prime divisors of `np` are `p` and the primes in `S`, hence

`(T_a f)(np)=a_p c + r_p`,

where

`r_p=sum_{q in S} a_q f(np/q)`.

The sequence `(r_p)_{p notin S}` belongs to `l2(P)`. Indeed, for each fixed `q in S`, the integers `np/q` are distinct as `p` varies, so

`sum_{p notin S} |f(np/q)|^2 <= ||f||_2^2`.

There are only finitely many `q in S`, and the fixed coefficients `a_q` therefore preserve square summability under the finite sum defining `r_p`.

If `a notin l2(P)`, deleting the finite set `S` does not restore square summability, so `(c a_p)_{p notin S}` is not in `l2(P)`. An `l2` sequence cannot cancel a non-`l2` sequence into `l2`; therefore

`((T_a f)(np))_{p notin S}`

is not square summable. It is a subsequence of the degree-`d+1` output, so `T_a f notin l2(N)`. Since this holds for every nonzero `f`, the maximal domain is exactly `{0}`.

Conversely, suppose `a in l2(P)`. For every basis vector,

`T_a e_n=sum_p a_p e_{pn}`

and the vectors `e_{pn}` are orthonormal as `p` varies, giving

`||T_a e_n||_2^2=sum_p |a_p|^2<infinity`.

Every finitely supported vector is a finite linear combination of basis vectors, so its image is a finite sum of `l2` vectors. Thus all finitely supported vectors lie in `D(T_a)`, proving density. This also shows that the threshold above is sharp rather than merely a necessary condition.

## Critical Bost--Connes specialization

In the standard positive-energy representation of the Bost--Connes multiplicative skeleton,

`H e_n=(log n)e_n`

and

`[H,mu_p]=(log p)mu_p`.

Consider first the canonical KMS half-density family

`T_beta=sum_p p^(-beta/2) mu_p`.

Its coefficient square norm is the prime-zeta sum

`sum_p |p^(-beta/2)|^2=sum_p p^(-beta)`.

This converges exactly for `beta>1` and diverges for `beta<=1`. Therefore

`D(T_beta)` is dense for `beta>1`,

while

`D(T_beta)={0}` for `beta<=1`.

The Hilbert-domain transition lands exactly at the Bost--Connes critical inverse temperature `beta=1`. In particular the critical source half-density

`T_1=sum_p p^(-1/2) mu_p`

is not an unbounded densely defined operator: its maximal Hilbert domain is trivial.

There are two direct ways one might try to obtain the finite Weil one-prime coefficient `(log p)/sqrt(p)` from this source field. One is to use the Hamiltonian generator, since commuting with `H` supplies the factor `log p`; the other is to put the logarithm directly into the coefficient. The first route fails because `T_1` itself has no nonzero Hilbert domain. The second route has coefficients

`a_p=(log p)/sqrt(p)`

and

`sum_p |a_p|^2=sum_p (log p)^2/p=infinity`,

so it also has trivial maximal domain by the theorem.

The same applies to the simplest coherent sandwich perturbation `B=I+T_a`. If `Bf=f+T_af` belongs to `l2` for an `l2` vector `f`, then `T_af=Bf-f` belongs to `l2`; hence `D(I+T_a)=D(T_a)`. At the critical coefficients, adding the identity does not rescue the domain.

## Finite-prime cutoff control

For a finite prime set `F`, define

`T_{a,F}=sum_{p in F} a_p mu_p`.

This is a bounded source operator and is exactly the kind of finite arithmetic coherent mixer left available by `WP-430`. But the infinite critical limit is singular already on the vacuum:

`T_{a,F} e_1=sum_{p in F} a_p e_p`,

so

`||T_{a,F}|| >= ||T_{a,F}e_1|| = (sum_{p in F}|a_p|^2)^(1/2)`.

For `a_p=p^(-1/2)` or `a_p=(log p)/sqrt(p)`, this lower bound diverges as `F` exhausts the primes. Thus the finite source selectors do not converge to a uniformly bounded operator family.

There is also a matched normalization control. Suppose scalars `lambda_F` are chosen so that

`||T_{a,F}/lambda_F||`

stays uniformly bounded along an exhausting sequence of finite prime sets. The vacuum lower bound forces `|lambda_F| -> infinity`. For each fixed prime `p`, once `p in F` its normalized coefficient is `a_p/lambda_F`, which tends to zero. Therefore scalar normalization can keep the cutoff family bounded only by erasing every fixed critical prime amplitude. It cannot preserve the target local coefficient while producing a bounded infinite selector.

This control separates a genuine domain obstruction from a mere choice of cutoff convention.

## Relation to WP-429 and WP-430

`WP-429` shows that an arbitrary coherent sandwich on a finite faithful Gibbs system is too flexible: it can realize any faithful target state. `WP-430` then shows that a selector canonical from thermodynamics alone is too rigid: it lies in spectral functional calculus and has zero Bohr degree. The surviving possibility was therefore to let **arithmetic source data** pick a nonzero-Bohr mixer.

The prime isometries `mu_p` are the most immediate such source data. They are not target-programmed, they have the correct source Bohr frequencies `log p`, and their critical KMS half-density supplies the natural `p^(-1/2)` scale. The present theorem shows that their naive coherent all-prime sum crosses an exact Hilbert-domain wall at the same critical parameter where it would become relevant to the Weil coefficient.

This is stronger than saying that the candidate is not bounded. There is no dense unbounded-operator domain to close: the maximal coefficientwise domain is `{0}`. Thus the direct analytic semigroup sum does not furnish the source-canonical coherent selector required by the current research frontier.

## Evidence classification

**Result class:** unconditional coefficient/Hilbert-space theorem in the stated standard representation, plus an exact specialization to the critical prime coefficients.

**Hypothesis burden:** one-sided linear prime-semigroup field `sum_p a_p mu_p`; standard `l2(N)` positive-energy representation; maximal coefficientwise Hilbert domain. No zero data, RH assumption, desired sign, prime-power mask, Gamma term, or regularization is used.

**Proof dependence:** orthogonal prime-coordinate geometry, unique prime factorization, and the classical convergence threshold for `sum_p p^(-beta)`. The Bost--Connes interpretation uses only its standard multiplicative shifts and logarithmic Hamiltonian.

**Theorem debt:** substantial. The result does not classify bidirectional combinations involving `mu_p*`, nonlinear source correspondences, cancellation between positive and negative Bohr sectors, quadratic forms that are not represented by this multiplier, rigged/distributional completions, or global adelic/cohomological objects. It does not construct the archimedean Gamma term or polar normalization and is not a proof of global Weil positivity.

## Prior-art and novelty audit

The Hilbert/Bohr setting is classical. Hedenmalm--Lindqvist--Seip identify square-summable Dirichlet coefficients with the Hardy `H^2` geometry in infinitely many prime variables, and the Bost--Connes system supplies the multiplicative shifts and logarithmic Hamiltonian. Both anchors are already recorded in `research/weil_positivity/SOURCES.md`.

A bounded literature audit also checked the modern multiplier classification of Tomas Fernandez Vidal, Daniel Galicer and Pablo Sevilla-Peris, *Multipliers for Hardy spaces of Dirichlet series*, Annales de l'Institut Fourier 75 (2025), 541--577, DOI `10.5802/aif.3658`. That work characterizes bounded Hardy--Dirichlet multiplier classes and studies their associated multiplication operators. The present finding does not claim a new general multiplier theorem in the literature; its durable novelty claim is the repository-level **source-critical application** and the elementary sharp maximal-domain calculation for the pure prime degree-one field relevant after `WP-430`.

Internally, the claim is not a restatement of the earlier obstructions. `WP-209` rules out exact critical Mangoldt mass inside bounded Bost--Connes equilibrium autocorrelations; it leaves open an unbounded source selector. `WP-227` shows that a different frequency-matched positive completion requires infinite auxiliary trace, but the positive block can still be written formally. `WP-268` concerns a different free-Fock boundary row and identifies a rigged-space escape. `WP-296` classifies multiplicative-shift-equivariant linear maps as Dirichlet convolution but does not prove this Hilbert-domain collapse for the prime kernel. `WP-429` and `WP-430` are finite canonicity controls and explicitly leave the infinite critical source-selector problem open.

The new delta is therefore exact and narrow: **for the first source-derived coherent mixer suggested by the WP-430 frontier, the critical KMS half-density is precisely the point at which the natural one-sided semigroup field loses every nonzero Hilbert-domain vector.**

## Falsification and audit controls

The theorem has a direct finite-support audit. Pick any nonzero `f`, any coefficient `f(n)!=0`, and inspect only the fresh-prime outputs `np` with `p` not dividing `n`. All possible competing terms use the finitely many old prime divisors of `n`; those terms form an `l2` sequence in the fresh prime `p`. They therefore cannot cancel a non-`l2` prime coefficient row. A counterexample would have to exhibit such an impossible `l2` cancellation.

The sharpness control is `a in l2(P)`: then the vacuum and every finitely supported vector are in the domain. Hence the proof is not silently showing that infinite prime sums are always pathological.

The thermal control is `beta>1`, where `sum_p p^(-beta)<infinity`; the same formal field regains a dense domain. The collapse at `beta=1` is therefore tied to the critical exponent rather than to an arbitrary representation cutoff.

The target-independence control removes all Weil information: replace the critical coefficients by any non-square-summable prime family and the same domain theorem holds. Thus the no-go is source/operator-theoretic rather than a disguised use of zero data or the desired Weil sign.

## Implication

The accepted Bost--Connes conditioning clue remains open, but its live coherent-selector branch narrows again. Extra arithmetic source structure is indeed necessary after `WP-430`; however, simply summing the canonical prime isometries at the critical half-density does not supply a legitimate Hilbert-space mixer. The critical family has already left the densely defined operator category.

A next viable candidate must therefore explain both **where its cross-frequency cancellation comes from** and **why its critical infinite limit has a nontrivial canonical domain**. Bidirectional correspondences, genuinely form-level constructions, or independently motivated rigged/cohomological completions remain logically open, but none can inherit positivity merely from the failed one-sided field. Any survivor must still pass the mandate's independent-sign, finite/archimedean assembly, polar normalization, and matched-control gates.

## References

- `research/weil_positivity/findings/WP-209-bost-connes-critical-kms-midpoint-forces-half-density-but-bounded-correlations-cannot-carry-mangoldt-mass.md`
- `research/weil_positivity/findings/WP-227-frequency-matched-positive-completion-requires-infinite-critical-auxiliary-trace.md`
- `research/weil_positivity/findings/WP-268-critical-fock-boundary-row-lies-beyond-every-finite-hamiltonian-hilbert-scale.md`
- `research/weil_positivity/findings/WP-296-multiplicative-shift-equivariant-nonlocal-couplings-are-dirichlet-convolution.md`
- `research/weil_positivity/findings/WP-429-coherent-kms-sandwiches-are-state-universal-on-finite-gibbs-truncations.md`
- `research/weil_positivity/findings/WP-430-thermodynamic-naturality-forces-finite-gibbs-selectors-into-spectral-functional-calculus.md`
- `research/weil_positivity/clues/CLUE-bost-connes-affiliation-conditioning-boundary.md`
- `research/weil_positivity/SOURCES.md`