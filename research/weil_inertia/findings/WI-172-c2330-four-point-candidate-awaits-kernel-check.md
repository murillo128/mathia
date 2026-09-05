# WI-172 — The `c=2330/10^6` four-point candidate is a concrete kernel-checkable source improvement, not yet a theorem

**Status:** `LITERATURE+COMPUTATIONAL-CANDIDATE`, `EXACT-CONDITIONAL-DERIVED`, `PRIOR-ART-REDIRECT`, `NEEDS-KERNEL-CHECK`, `NO-NOVELTY-CLAIM`

## Claim

The accepted source-constrained four-point question now has a much narrower first test than a new optimization campaign. A public `teal-sea/zeta-lab` artifact already contains a generated candidate proof for the genuine Montgomery--Taylor four-point functional at

\[
n=4,\qquad c=\frac{2330}{10^6},\qquad p=2500,
\]

strictly above the established Lean-checked value

\[
c_0=\frac{2310}{10^6}.
\]

The candidate is **not established evidence**: its complete Lean build was canceled before any candidate proof module ran. What is established from the public record is only that the exact-rational search reported closure and a separate emitted-source preflight reported zero coverage problems. The candidate therefore remains a bounded formal-verification target, not an unconditional zeta theorem.

If the preserved generated proof at the pinned candidate commit passes a complete Lean kernel check with the repository's intended trust footprint, then the existing `n_point_bound` bridge at the valid block size `m=432` gives the exact conditional lower bound

\[
\boxed{
\liminf_{T\to\infty}
\frac{N_0^s(T,2T)}{N(T,2T)}
\ge
\frac{14400000H_{\rm MT}-17240}{14366681}
}
\tag{1}
\]

with numerical value

\[
0.6728603588388666595002053005\ldots .
\tag{2}
\]

This would strictly exceed Mathia's current exact four-point bound from WI-036,

\[
B_{36}
=
\frac{1609375H_{\rm MT}-1920}{1605679}
=
0.6728529301211843197511878001\ldots .
\tag{3}
\]

The comparison does not rely on decimal arithmetic. Exactly,

\[
\frac{14400000H-17240}{14366681}
-
\frac{1609375H-1920}{1605679}
=
\frac{400365625H-97878440}{23068277981399}.
\tag{4}
\]

The numerator is positive already for

\[
H>\frac{97878440}{400365625}=0.2444726\ldots ,
\]

so in particular it is positive for the established Montgomery--Taylor constant `H_MT>2/3`. At the actual value of `H_MT`, the conditional gain over WI-036 is

\[
7.428717682339749\ldots\times10^{-6}.
\tag{5}
\]

Thus a successful kernel replay would not merely reproduce a weaker historical candidate: it would give a strict certified-proportion improvement over the current Mathia exact frontier using the actual MT source functional and no new prime-side moment.

## Evidence and proof provenance

The load-bearing external artifacts are both in `teal-sea/zeta-lab`.

1. The current archival record `hunts/four_point_pressure/RUNS.md` on main commit
   `4d0d431d9da567b5967eca38085ebc94d9270cea` records the candidate parameters
   `n=4`, `c=2330/10^6`, `p=2500`, `m=432`, the exact bridge expression in (1),
   and the terminal verification status. It reports:

   - exact search-tree closure;
   - emitted-source preflight with `1516` cell lemmas, `11863` leaves, `220`
     chunks, `13` boxes, `64` dispatch cases, and zero problems;
   - GitHub Actions run `33987435968` at candidate commit
     `d28df5f992479cd32751cb90c8c88551550582a3`;
   - successful toolchain installation and Mathlib-cache steps, followed by
     cancellation during the dependency build;
   - every candidate proof step, including `FourPoint.Base`, generated cells,
     chunks, `FourPoint.Main`, and the final axiom audit, **skipped**.

   The archival record explicitly concludes that no new proved bound was
   produced.

2. The preserved generated source at commit
   `d28df5f992479cd32751cb90c8c88551550582a3`,
   `hunts/ainta_seven_point/lean-four-point/FourPoint/Main.lean`, contains the
   intended declarations

   \[
   \texttt{four\_point\_cert}:
   \frac{2330}{10^6}\le F_4(2500;g)
   \quad(g_i\ge0),
   \]

   together with the exact `Phi_four` identity at `m=432` and the downstream
   bound source. The existence of theorem-shaped Lean source is **not** a proof
   that those declarations compile; the canceled build never reached them.

The earlier `FOUR-POINT.md` in the same repository had already measured the
`c=2330/10^6` frontier and tabulated the parameter. Therefore neither the
constant nor the candidate is a Mathia discovery.

## The block-size correction is load-bearing

The current archival record uses `m=432`. This is forced by the side condition
of the generic bridge,

\[
c\bigl(m-(n-1)\bigr)\le1.
\tag{6}
\]

For `n=4` and `c=2330/10^6`,

\[
\frac{2330}{10^6}(432-3)
=
\frac{999570}{10^6}<1,
\]

whereas the older exploratory table's nearby `m=433` entry would give

\[
\frac{2330}{10^6}(433-3)
=
\frac{1001900}{10^6}>1.
\]

So `m=433` cannot be used in the theorem bridge at this `c`; the exact
conditional comparison in this finding uses only the corrected admissible
`m=432` value from the archival record.

## Relation to the source-constrained positive-cover frontier

WI-166 proves sharpness only after relaxing the four-point problem to arbitrary
nonnegative pair weights and a common pressure ledger at the established local
constant `2310/10^6`. WI-171 then shows that generic PSD/Toeplitz/Gram
realizability does not eliminate that relaxed saturation witness. The accepted
`CLUE-kernel-constrained-positive-cover-escape` therefore isolates the actual
Montgomery--Taylor kernel-value relation tied to ordered additive gaps as the
remaining source-specific information.

The candidate here tests exactly that surviving interface: its local functional
is the genuine `wfun`/Montgomery--Taylor four-point functional, not the arbitrary
weight relaxation. If `four_point_cert` kernel-checks at `2330/10^6`, then the
actual source functional has a strict uniform local margin of at least

\[
\frac{20}{10^6}=2\times10^{-5}
\]

above the WI-009/WI-166 certified constant. Because the generic bridge already
propagates that stronger local certificate to (1), no new global assembly lemma
is needed to turn this particular local surplus into a strict theorem-level
proportion improvement.

This would **not** resolve the larger accepted clue. It would establish one
strict source-specific escape from the exact relaxed saturation point, but it
would not determine the optimal MT-constrained infimum, show an extensive
surplus for arbitrary positive-cover architectures, defeat WI-026's
single-profile pressure-family ceiling, or constrain the exceptional off-line
block strongly enough to imply RH.

## Adversarial audit

Several weaker readings are excluded.

- **Generated Lean source is not formal verification.** The only attempted
  complete build was canceled before the candidate modules ran. No theorem from
  the `c=2330/10^6` source is imported as evidence here.
- **Search closure is not kernel closure.** The preflight checks the emitted
  exact-rational partition/coverage bookkeeping; it does not replace Lean's
  elaboration, dependency checking, kernel checking, no-`sorry` audit, or axiom
  inspection.
- **The old `m=433` arithmetic is inadmissible.** Equation (6) rules it out
  exactly; the corrected `m=432` is used throughout.
- **A successful replay would improve only the certified simple-critical
  proportion.** It does not identify the complementary mass as off-line zeros
  and does not remove multiple critical-line zeros or pure proof slack.
- **A failed build need not refute the mathematics.** A theorem/cell failure
  after successful dependency setup is material evidence about the generated
  candidate; timeout, cancellation, missing resources, or unrelated tooling
  failure is only inconclusive execution evidence.

## Prior-art and novelty audit

The `c=2330/10^6` parameter, its generated candidate proof tree, and the
conditional decimal in (2) are public prior art in `teal-sea/zeta-lab`.
Mathia makes no priority claim for them. The durable contribution of this
finding is narrower: it classifies the current proof status correctly, checks
the bridge side condition and the corrected `m=432` value, derives the exact
conditional comparison with the stronger WI-036 bound rather than only the
older registered four-point theorem, and identifies a bounded kernel replay as
the first decisive test for the accepted source-constrained clue.

A local duplication audit found no existing `weil_inertia` finding that records
this current archival disposition or the exact comparison (4) against WI-036.
WI-009 records the proved `2310/10^6` certificate; WI-025/WI-036 optimize its
assembly; WI-166/WI-171 isolate the source-specific escape question. The
present result is therefore a prior-art redirect and evidence-status finding,
not a rediscovery of those results.

## Decisive next test

Run exactly one bounded replay of the preserved candidate at commit
`d28df5f992479cd32751cb90c8c88551550582a3` in its pinned repository
environment:

1. reproduce the existing emitted-source preflight and require the recorded
   zero-problem counts;
2. compile the complete relevant Lean package so the candidate proof modules
   themselves run;
3. inspect `four_point_cert`, `Phi_four`, the downstream bound declarations,
   no-`sorry` status, and their axiom footprint;
4. classify resource/cancellation failures separately from proof failures.

Do not sweep `c`, regenerate a new proof tree, or redesign the certificate
before this replay. The candidate is already precise enough that the next
information gain is formal verification, not another numerical search.