# MI-016 — Source-aligned shifts face a defect-or-Mertens dichotomy

**Evidence level:** supported

## Core intuition

Preserving source order is necessary but not sufficient for a useful Möbius escape. The first source-aligned shift observables split into two unfavorable classes. If they probe shifted squarefree support, their new information lives only on sparse defect sites and can be small for purely combinatorial reasons. If they densify the probe with logarithmic prime incidence, the prime-power-completed observable becomes an invertible Volterra transform of the rough Mertens prefix; deleting the completion leaves repeated-prime-power defects.

The surviving arithmetic channel must therefore be both relational and **source-cheaper**: it must retain dense ordered information without becoming a disguised principal sum after the natural completion.

## Strongest justified claim

MC-206 specializes the mixed sign/support shift of MC-205 to the actual logarithmic-primorial Möbius source. After the old principal/support terms are removed, the genuinely new shift contribution is exactly a signed sample of squarefree holes. Mean-zero off-diagonal filters can therefore be small without any Möbius sign cancellation, simply because the defect set is sparse.

MC-207 replaces that binary support field by log-weighted prime incidence. Its prime-power completion is `sum g_y(n) log(n+R)`, and exact partial summation gives a two-way Volterra transform between this quantity and the rough Mertens prefix. The two have the same fixed-power exponent up to logarithms. The difference between completed and distinct-prime incidence is supported only on repeated prime powers.

MC-208 then audits the primitive square-defect branch. The shifted residue classes are all reduced and the primorial pre-sieve can be removed with only subpower multiplicity, so those are not the main obstructions. The decisive loss is the square modulus: control up to ordinary modulus `Q=X^alpha` only reaches square divisors `d<=X^(alpha/2)`, leaving an absolute tail `X^(1-alpha/2)+sqrt(X)`. Classical square-root-level progression ranges therefore stop near `X^(3/4)`. The remaining large-divisor tail has an exact dual expression as Möbius parity on the cubic family `d(md^2-q)`.

## Synthesis of evidence

MC-205 proves that source-relative ordering can survive where permutation-invariant enrichment fails. MC-206--MC-208 show what must be added to that criterion. A useful relation needs a dense nonprincipal signal, must not become principal-equivalent after completion, and must avoid a modulus transformation that consumes the entire target exponent before cancellation technology begins.

This gives a sharper admission test for future observables than “is it source-aligned?”: identify the defect support, compute the natural completion, price any modulus inflation, and only then ask whether the remaining relation is genuinely cheaper.

## Counterevidence / boundary cases

The square-defect level-doubling theorem concerns this specific shifted support expansion. Other source-aligned observables need not introduce square moduli. Likewise the Volterra equivalence is for logarithmic incidence and its natural prime-power completion; a different dense weighting could retain useful nonprincipal information.

MC-208 does not prove that the cubic polynomial tail is as hard as Mertens. It isolates it as the remaining quantitative object after the obvious progression route loses too much exponent.

## Epistemic status

**Supported route-narrowing:** the first actual-source shift escapes preserve ordering but either collapse to sparse defects, become Mertens-equivalent after completion, or pay a square-modulus level-doubling tax. Any surviving relational observable must cross all three gates.

## Novelty/prior-art status

The underlying partial summation, progression decomposition, and polynomial-parity mechanisms are classical; the persisted findings make no broad novelty claim. This intuition only synthesizes their role in the current Möbius line.

## Falsification criterion

Produce within the MC-206--MC-208 constructions a dense nonprincipal component that survives completion without allowing recovery of the rough Mertens prefix and whose required progression range stays at or below the ordinary square-root level, or prove an RH-scale bound for the cubic tail using information already present in the current construction. Either would reopen the classified branch.
