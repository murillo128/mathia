---
id: CLUE-prime-flute-shift-clone-sharp-schatten-threshold
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-107-shift-clone-cuff-defect-is-l2-not-l1.md
  - research/prime_flute/findings/PF-109-shift-clone-preserves-canonical-separator-pinching-multiplicatively.md
  - research/prime_flute/findings/PF-112-first-relative-resolvent-is-not-trace-class.md
  - research/prime_flute/findings/PF-125-shift-clone-has-compact-relative-resolvent.md
  - research/prime_flute/findings/PF-126-shift-clone-metric-defect-is-Lp-above-one.md
  - research/prime_flute/findings/PF-127-collapsing-canonical-collar-is-schatten-benign-above-trace-endpoint.md
  - research/prime_flute/findings/PF-130-lambert-shift-metric-defect-is-strong-L1-summable.md
  - research/prime_flute/findings/PF-147-square-resolvent-S1-forces-first-resolvent-S2.md
  - research/prime_flute/findings/PF-150-square-resolvent-S1-is-sharp-at-S2-without-geometry.md
  - research/prime_flute/findings/PF-169-all-margulis-short-central-squared-resolvent-blocks-are-trace-summable.md
  - research/prime_flute/findings/PF-171-all-margulis-short-central-first-resolvent-blocks-have-sharp-Sr-threshold.md
  - research/prime_flute/findings/PF-172-finite-collar-recoupling-is-trace-class-but-zero-mode-budget-does-not-collapse.md
  - research/prime_flute/findings/PF-173-relative-central-recoupling-is-trace-summable.md
---

# Does the prime/shift relative resolvent have the sharp Schatten threshold `S_r`, `r>1`?

## Observation

PF-112 fixes the unavoidable local endpoint for any genuinely different two-dimensional metric pair: the first relative resolvent is locally of critical order `-2`, so `S_1` is impossible while every exponent `r>1` remains compatible with microlocal order. PF-125 proves global compact relative resolvent for the exact prime flute versus the exact all-composite shift clone, and PF-126 places the transported coefficient defect in weak `L^1` and every `L^r`, `r>1`.

The closed-thin central geometry is now substantially exhausted as a possible obstruction. PF-127 proves on one fixed central Dirichlet collar that the first relative resolvent lies in every `S_r`, `r>1`, with

\[
\|A_{L,L_+}^{(R)}\|_{\mathcal S_r}^r
\le C_{R,r}|\log(L_+/L)|^rL^{2r-1},
\]

while remaining outside `S_1` whenever `L_+ != L`. PF-169 sums the corresponding **squared** relative-resolvent blocks over every Margulis-short core and obtains trace class. PF-171 performs the sharper first-resolvent summation itself and proves

\[
\bigoplus_{\eta\in\mathcal S}A_\eta
\in\mathcal S_r\quad\text{for every }r>1,
\qquad
\bigoplus_{\eta\in\mathcal S}A_\eta\notin\mathcal S_1.
\]

PF-172 then separates local boundary order from infinite assembly. Restoring transmission across any finite smooth cut family is trace class in dimension two, but on an exact collapsing collar the **absolute** central recoupling trace norm has an `L`-independent zero-mode contribution. Thus one cannot prove the infinite result by separately summing prime and clone gluing norms.

PF-173 now carries out the relative cancellation that PF-172 left open on the exact central-cut model. If

\[
G_L=(\Delta_L+1)^{-1}-(\Delta_L^{\rm cut}+1)^{-1},
\qquad L_+=e^tL,
\]

then

\[
\boxed{
G_{L_+}-G_L\in\mathcal S_1,
\qquad
\|G_{L_+}-G_L\|_1\le C_R|t|L^2.
}
\]

The common angular zero mode cancels exactly. Using PF-109's `t=O(P^{-3})` matching and PF-138's complete `O(P^{0.525})` short-core count, PF-173 further proves that the orthogonal direct sum of these **relative central-cut recoupling corrections over every Margulis-short tail core is trace class**.

Thus zero systole, short-core multiplicity, the complete central metric blocks, finite boundary pseudodifferential order, and the shrinking-core transmission zero mode are no longer candidates for an `S_r`, `r>1`, failure. The remaining operator burden is body-loaded and nonlocal.

PF-130 independently shows that the isolated Lambert body comparison has summable strong-`L^1` metric/density mass. PF-147 says a future global squared-resolvent `S_1` result would force the full first relative resolvent into `S_2`, while PF-150 proves that this abstract implication cannot by itself cross below `2`. PF-171 is therefore informative precisely because actual collar geometry does cross below `2`; PF-173 shows that the corresponding central-cut transmission correction crosses all the way to `S_1` after source/clone cancellation.

## Research question

For the common-manifold Laplacians associated with the PF-125 marking, does

\[
A
:=
(\Delta_{g_+}+1)^{-1}
-
(\Delta_g+1)^{-1}
\]

satisfy

\[
\boxed{
A\in\mathcal S_r\quad\text{for every }r>1,
\qquad
A\notin\mathcal S_1?
}
\]

PF-112 proves the second statement for the full non-isometric pair. The positive side is now localized more sharply than before: the complete decoupled central metric family already has the desired threshold by PF-171, and the complete relative central-**cut recoupling** family is even trace class by PF-173.

What remains is not another isolated short-core calculation. It is whether the **actual outer collar/body transmission**, complementary body pieces, localization commutators, and repeated interactions created by removing the global Dirichlet decomposition preserve the `S_r`, `r>1`, threshold under one common prime/shift interface calculus.

## Why it may matter

A positive answer would finish the natural operator-ideal classification between PF-112 and PF-125 and show that even the sharp first-resolvent ideal scale is compatible with an exact all-composite control. It would also place the pair in the `S_2` regime relevant to regularized determinant and second-order spectral-shift machinery while ordinary trace-class first-resolvent constructions remain excluded. None of that would be prime-specific by itself.

A negative answer for some `r>1` is now highly localized conceptually. It would have to identify a genuinely global amplification mechanism absent from every isolated and collectively summed central short-collar metric block and absent from the relative shrinking-core recoupling family. The obstruction must be carried by body-dependent boundary response, nonorthogonal overlap, repeated propagation, or another full-surface assembly channel.

## Decisive test

A positive resolution must control the **uncut full operator under one common prime/shift outer-interface calculus**. PF-172 and PF-173 show why the order of operations matters: separate absolute gluing norms retain an order-one zero-mode budget, whereas subtracting matched transmission problems first can expose trace-summable relative decay.

The next useful calculation should therefore cut prime and clone along the same fixed outer collar/body interfaces, write compatible Krein/Schur-complement or Dirichlet-to-Neumann formulas, and subtract those formulas algebraically before taking Schatten norms. Unlike PF-173's central-cut model, the boundary operators must include the **actual complementary-body Dirichlet-to-Neumann response**. The required estimate must remain uniform across the complete zero-systole tail and through repeated head-tail interaction.

A schematic target is to control the source/clone difference of terms of the form

\[
\mathcal P(z)\,\mathcal M(z)^{-1}\mathcal P(\bar z)^*,
\]

where `P` and `M` are the Poisson and boundary transmission operators for the full cut surface, not just the isolated collar. The central collar contributions supplied by PF-171 and PF-173 should appear as already-controlled pieces rather than being re-estimated from scratch.

The squared-resolvent route remains complementary. Proving the global squared-resolvent difference is `S_1` would, through PF-147, settle `r>=2`; PF-150 shows that additional surface-specific estimates would still be required for `1<r<2`. A direct first-resolvent outer-transmission estimate is therefore the natural test of whether PF-171's sharp threshold survives the actual infinite assembly.

A decisive negative resolution must produce an actual singular-value lower bound in a channel excluded from PF-171--PF-173. Concentration solely in fixed-central Margulis-short collars, finite-interface pseudodifferential order, the nondecaying **absolute** recoupling norm of one surface, or the matched central-cut transmission family is no longer enough.

## Evidence boundary

PF-171 is a theorem about the **Dirichlet-decoupled fixed-central collar direct sum**. It does not estimate the full uncut Laplacian, outer collar pieces, body terms, or the operators created when the outer Dirichlet interfaces are removed. PF-130 is likewise a coefficient estimate on an explicit body comparison rather than a global Schatten theorem.

PF-172 proves finite transmission trace class and an absolute zero-mode lower bound for one exact collapsing-collar cut. PF-173 subtracts the two matched versions of that same **central-cut** problem and proves trace-class summability over the complete short-core family. Neither finding contains the actual complementary-body Dirichlet-to-Neumann maps or restores the collar's outer interfaces to the infinite flute. Consequently PF-173 is evidence that relative cancellation works in the canonical local transmission model, not a proof of full-surface trace-class transmission.

PF-147 remains conditional on the still-open full-surface squared-resolvent `S_1` gate, and PF-150 is only an abstract limitation of functional calculus. Standard compact/bounded-geometry pseudodifferential theorems cannot simply be globalized across this zero-systole infinite-type surface. The Güneysu--Thalmaier criterion is useful for wave operators but is not a Schatten theorem, while the Behrndt--Langer--Lotoreichik/Grubb boundary results control finite smooth boundary-condition changes rather than the infinite body-loaded prime/shift transmission difference.

## Research disposition

The clue remains `accepted`, but its live interface target is now **outer and body-loaded**. The entire closed-thin central metric sector already satisfies the conjectured sharp `S_r`, `r>1`, classification, and the complete matched central-cut recoupling family is trace class after source/clone cancellation.

Future work should therefore not spend another cycle proving local central transmission smoothing. The next decisive operator calculation is the relative full-surface Krein/Schur-complement difference on common outer collar/body interfaces: retain the actual body response, cancel source/clone transmission before norms, and test whether the remaining nonlocal defect is `S_r`-summable for every `r>1`. The clue will be resolved only when those body-loaded uncut terms either preserve the sharp threshold globally or yield a genuine operator-level counterexample for some `r>1`.
