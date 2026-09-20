---
id: WP-387
title: Beurling--Deny jump selectors collapse to unit-cell invisibility
branch: weil_positivity
status: supported
kind: pointed-boundary-jump-killing-classification
claim_strength: exact RH-independent classification showing that every positive pure-jump Dirichlet energy on the WP-384 boundary profiles which annihilates all mixed-prime shells must have its jump measure supported within the canonical unit cells of the floor coordinate, where every arithmetic profile is constant; hence the jump sector annihilates all shells, and adding the Beurling--Deny killing sector recovers at most the rank-one Mangoldt ray of WP-386
created: 2026-09-20
related: [WP-009, WP-168, WP-381, WP-382, WP-383, WP-384, WP-385, WP-386]
clues: [CLUE-weil-positivity-noncharacter-finite-archimedean-incidence]
prior_art:
  - classical Beurling--Deny decomposition of regular symmetric Dirichlet forms into strongly local, jump, and killing parts
  - Schilling--Uemura pure-jump Dirichlet-form framework already recorded in SOURCES.md
  - classical identity mu * log = Lambda
---

# WP-387 — Beurling--Deny jump selectors collapse to unit-cell invisibility

## Claim

`WP-386` left genuinely nonlocal/off-diagonal positive boundary couplings as a live escape. The first canonical nonlocal positive class is not an arbitrary positive-definite kernel but a **pure-jump Dirichlet energy**, the jump sector of the classical Beurling--Deny decomposition.

For the `WP-384` boundary profiles

\[
h_m(x)=\frac1{\sqrt m}\sum_{d\mid m}\mu(m/d)
\left(H_{\lfloor x/d\rfloor}-\log(x/d)-\gamma\right),
\qquad m>1,
\tag{1}
\]

set

\[
I_0=(0,1),\qquad I_n=[n,n+1)\quad(n\ge1).
\tag{2}
\]

Let `J` be any positive symmetric Borel measure on
`(0,\infty)^2\setminus\mathrm{diag}` for which all `h_m` have finite energy, and define

\[
\mathcal E_J(f,g)
:=\frac12\iint
(f(x)-f(y))\overline{(g(x)-g(y))}\,dJ(x,y).
\tag{3}
\]

Then

\[
\boxed{
\mathcal E_J(h_m)=0
\text{ for every mixed-prime }m
\iff
J\!\left(
(0,\infty)^2\setminus\bigcup_{n\ge0} I_n\times I_n
\right)=0.
}
\tag{4}
\]

Moreover, whenever (4) holds,

\[
\boxed{
\mathcal E_J(h_m,h_n)=0
\qquad\text{for every }m,n>1.
}
\tag{5}
\]

Thus the pure-jump escape is sharper than the pointwise-local one. A jump geometry can remain nontrivial inside each unit cell, but exact mixed-shell nullity forces it to become **arithmetically invisible to every shell**, including prime powers.

Combining this with `WP-386` classifies the jump-plus-killing sector. For a positive measure `nu`, define

\[
\mathcal E_{J,\nu}(f,g)
:=\mathcal E_J(f,g)+\int f(x)\overline{g(x)}\,d\nu(x).
\tag{6}
\]

Under the same domain assumption, exact mixed-shell nullity is equivalent to

\[
\nu([1,\infty))=0
\quad\text{and}\quad
J\text{ is supported on }\bigcup_{n\ge0}I_n^2.
\tag{7}
\]

Consequently

\[
\boxed{
\mathcal E_{J,\nu}(h_m,h_n)
=\nu((0,1))\,
\frac{\Lambda(m)\Lambda(n)}{\sqrt{mn}}
\qquad(m,n>1).
}
\tag{8}
\]

The entire nonlocal jump sector disappears from the arithmetic Gram; the only surviving positive finite-place response is exactly the rank-one Mangoldt ray already found in `WP-386`.

**Classification:** `EXACT-DERIVED + RH-INDEPENDENT + FRESH-PRIME-BOUNDARY + PURE-JUMP-DIRICHLET-CLASSIFICATION + BEURLING-DENY-JUMP-KILLING-SECTOR + UNIT-CELL-RIGIDITY + JUMP-ARITHMETIC-BLINDNESS + MANGOLDT-RANK-ONE-REMAINDER + MATCHED-CONTROLS + DECISIVE-NEGATIVE + NOT-A-WEIL-BRIDGE`.

## 1. Every arithmetic boundary profile is exactly unit-cell constant

For `m>1`, expand (1). Since

\[
\sum_{d\mid m}\mu(m/d)=0
\quad\text{and}\quad
\sum_{d\mid m}\mu(m/d)\log d=\Lambda(m),
\tag{9}
\]

one gets the exact formula

\[
\boxed{
h_m(x)
=\frac1{\sqrt m}
\left(
\Lambda(m)
+\sum_{d\mid m}\mu(m/d)H_{\lfloor x/d\rfloor}
\right).
}
\tag{10}
\]

If `x` moves inside one half-open unit cell `I_n`, then for every integer divisor `d`, `floor(x/d)` is constant: its only possible jumps occur at integer multiples of `d`, hence at integer cell boundaries. Therefore every `h_m`, not only the mixed-shell profiles, is constant on each `I_n`.

This step-function structure was implicit in the harmonic-floor carrier of `WP-384`, but it matters differently here. A jump form only sees differences `h_m(x)-h_m(y)`. It is therefore blind to all arithmetic profiles on pairs of points lying in the same unit cell.

## 2. Fresh mixed shells separate every pair of distinct cells

The converse rigidity comes from exactly the fresh-large-prime control used in `WP-386`. Fix `X>0` and choose distinct primes `p,q>X`. Since `pq` has two distinct prime divisors, `Lambda(pq)=0`. For every `0<x\le X`, the scaled arguments `x/p`, `x/q`, and `x/(pq)` lie in `(0,1)`. Equation (10), or the direct squarefree expansion, gives

\[
\boxed{
h_{pq}(x)=\frac{H_{\lfloor x\rfloor}}{\sqrt{pq}}
\qquad(0<x\le X),
}
\tag{11}
\]

where `H_0=0`.

The sequence `H_n` is strictly increasing. Hence on `(0,X]`,

\[
h_{pq}(x)=h_{pq}(y)
\iff
\lfloor x\rfloor=\lfloor y\rfloor.
\tag{12}
\]

Now suppose every mixed shell has zero jump energy. In particular,

\[
0=\mathcal E_J(h_{pq})
=\frac12\iint |h_{pq}(x)-h_{pq}(y)|^2\,dJ(x,y).
\tag{13}
\]

The integrand is nonnegative, so it vanishes `J`-almost everywhere. Restricting to `(0,X]^2` and using (12) shows that `J` gives zero mass there to every pair in different unit cells. Exhausting `(0,\infty)^2` by such bounded squares proves the forward implication in (4).

Conversely, if `J` is supported on same-cell pairs, equation (10) makes every difference `h_m(x)-h_m(y)` vanish on the support of `J`. This proves both the reverse implication in (4) and the stronger conclusion (5).

The theorem therefore identifies the exact equivalence relation seen by all mixed shells:

\[
\boxed{x\sim y\iff\lfloor x\rfloor=\lfloor y\rfloor.}
\tag{14}
\]

The mixed family separates the unit cells globally but cannot resolve geometry inside them.

## 3. Adding the killing sector leaves only the Mangoldt ray

The Beurling--Deny jump and killing contributions are separately nonnegative. Therefore, if their sum (6) has zero energy on every mixed shell, then each contribution has zero energy on every mixed shell.

The jump conclusion is (4). For the killing term, `WP-386` proves exactly that

\[
\int |h_m|^2\,d\nu=0
\text{ for every mixed-prime }m
\iff
\nu([1,\infty))=0.
\tag{15}
\]

On `(0,1)`, the same source identity gives

\[
h_m(x)=\frac{\Lambda(m)}{\sqrt m}.
\tag{16}
\]

The domain assumption for any prime profile forces `nu((0,1))<\infty`. Since the jump part vanishes on **all** shell pairs once (4) holds, polarization yields (8).

This also kills a possible finite--archimedean use of the jump sector. For any admissible anchor `g`,

\[
\mathcal E_J(h_m,g)=0
\qquad(m>1),
\tag{17}
\]

because `h_m(x)-h_m(y)=0` on the support of `J`. Any shell dependence in a jump-plus-killing coupling to `g` therefore comes only from the killing term, where `WP-386` already shows it is proportional to `Lambda(m)/sqrt(m)`.

So a source-native pure-jump geometry does not supply the missing second arithmetic/global coordinate. Its only way to respect exact mixed-shell nullity is to move all nonlocal conductance into directions that the entire arithmetic family cannot see.

## 4. Matched controls and falsification

The theorem is sharp. A nonzero jump measure supported, for example, inside `I_1\times I_1` gives a genuinely nonlocal positive energy on general functions, yet equation (5) says it is zero on every arithmetic shell. Thus the result is not claiming that the geometric jump form itself must vanish.

The opposite control is equally direct. Put any positive jump mass between `(0,1)` and `[1,2)`. For fresh primes `p,q>2`, equation (11) gives value `0` on the first cell and `1/sqrt(pq)` on the second, so the mixed shell `pq` has strictly positive jump energy. Cross-cell conductance and exact mixed-shell nullity cannot coexist.

The global quantifier over mixed shells is essential. A finite panel can leave accidental equal-value classes between several unit cells and hence admit cross-cell jump measures invisible to that panel. The fresh-prime family removes those accidents at arbitrarily large scale; finite numerical separation is therefore not evidence against the global obstruction.

The domain hypothesis is also substantive rather than cosmetic. If a proposed Dirichlet form does not contain the source profiles whose arithmetic response it is meant to evaluate, it is not a candidate selector for this boundary layer. No closure or regularization is being used to insert otherwise inadmissible shells.

## 5. Beurling--Deny scope and the remaining escape

The classical Beurling--Deny decomposition writes a regular symmetric Dirichlet form as a sum of a strongly local part, a jump part, and a killing part. `SOURCES.md` already records Schilling--Uemura as the standard pure-jump comparison class used earlier in this line.

The present theorem classifies **only the jump and killing sectors** on the exact `WP-384` arithmetic profiles. It does not claim to classify a strongly local diffusion/interface contribution, and it does not cover an arbitrary positive-definite integral kernel that lacks the Markov/difference structure (3).

This distinction matters. If a full regular Dirichlet form contains all `h_m` and makes every mixed shell zero-energy, nonnegativity of the Beurling--Deny components forces its jump and killing pieces individually into (7). Hence any additional prime-power response must come from the strongly local/interface component. Alternatively, an escape must leave the Beurling--Deny/Markov class, retain finite-`q` structure discarded by the `WP-384` continuum limit, or postpone mixed-shell nullity until after a finite--archimedean interaction.

Those are genuinely different mechanisms. Simply replacing the pointwise weight of `WP-386` by a positive nonlocal conductance kernel of Dirichlet-jump type is now closed.

## 6. Prior-art and novelty audit

No novelty is claimed for pure-jump Dirichlet forms or the Beurling--Deny decomposition. The jump energy (3), its positive jump measure, and the separation of jump and killing terms are standard potential-theoretic machinery. Schilling--Uemura's 2012 treatment is already a durable literature anchor in `SOURCES.md`, and `WP-009` previously used the same general framework to test a very different translation-jump construction on the Prime-Lattice axis.

A targeted literature search for Nyman--Beurling/cyclotomic harmonic-floor profiles combined with Beurling--Deny jump forms found only the general Dirichlet-form framework, not this source-specific unit-cell classification. The durable claim is therefore deliberately narrow: **for the exact `WP-384` boundary family**, fresh mixed shells identify the floor-cell partition, and the Markovian jump sector becomes completely arithmetic-blind once mixed-shell nullity is imposed.

This is not a new general theorem about Nyman--Beurling geometry, nor a new positivity criterion for RH. In fact it is a negative result: another canonical independently positive geometry fails before any global Weil comparison is reached.

## Consequence for the research line

`WP-386` showed that arbitrary positive pointwise-local reweighting can preserve prime-power support only by collapsing to one Mangoldt ray. `WP-387` now handles the first canonical genuinely nonlocal positive continuation. Pure-jump Dirichlet conductances can evade pointwise locality, but exact mixed-shell nullity forces all conductance to stay within floor cells, and the arithmetic boundary profiles are constant on precisely those cells. The jump contribution therefore vanishes on every shell.

The combined jump-plus-killing sector has no more arithmetic freedom than `WP-386`: its complete shell Gram is the rank-one form (8). It cannot manufacture an independent archimedean Gamma/polar channel, a nontrivial test-function family, or a global Weil sign theorem.

The next boundary candidate should therefore not be another positive Markov jump kernel on the same continuum carrier. The live tests are now a source-forced strongly local/interface form whose domain genuinely contains the shell steps, a non-Markov positive off-diagonal geometry with an independent canonical reason for its kernel, a finite-`q` prelimit term lost in `WP-384`, or an indefinite finite--archimedean coupling whose final positivity appears only after assembly.

## Conclusion

The `WP-384` boundary profiles carry a hidden exact discretization: every shell is constant on the unit cells of the floor coordinate, while fresh mixed-prime shells separate those cells. That makes the nonlocal jump problem rigid. A positive Dirichlet jump energy annihilates every mixed shell **if and only if** its conductance never crosses a unit-cell boundary; under that condition it annihilates every prime-power shell as well.

Adding the positive killing sector restores only the already-known Mangoldt rank-one ray. Thus the Beurling--Deny jump-plus-killing escape does not provide the missing Mathia-native global Weil positivity structure, and any surviving boundary route must obtain its extra degrees of freedom from a genuinely different component rather than from another positive jump completion of the same continuum profiles.
