---
id: CLUE-prime-flute-positive-width-transition-schur-complement
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-342-sharp-physical-cutoff-forces-order-one-direct-angle-correlation.md
  - research/prime_flute/findings/PF-343-uniformly-small-physical-hard-sector-gaps-force-order-one-direct-angle-correlation.md
  - research/prime_flute/findings/PF-344-positive-width-transition-shorting-removes-the-leading-corridor-cost.md
  - research/prime_flute/findings/PF-345-growing-exterior-edge-strips-have-exponentially-small-shorted-trace.md
  - research/prime_flute/findings/PF-346-corridor-gram-shorting-preserves-correlations-but-is-unstable-to-subleading-energy.md
---

# Can a positive-width transition band absorb the collapsing-corridor mode after exact Schur elimination?

## Observation

PF-342 shows that the canonical sharp fixed physical \`L/H\` split has order-one low/high canonical correlation. PF-343 strengthens the mechanism: the direct hard-sector angle is still noncompact whenever opposite sectors contain bounded physical Fourier modes separated by at most one sufficiently small fixed physical distance.

Therefore moving the hard cutoff or inserting only a narrow direct gap does not address the obstruction. The first representation change not covered by the argument is a genuine three-sector decomposition

\[
\mathcal H=L\oplus T\oplus H
\]

in which the transition band \`T\` has a physical width bounded below independently of the cuff period and is **retained in the full positive boundary form** before being eliminated.

Schur-complement realizations of Dirichlet-to-Neumann operators are classical. PF-344 proves that exact positive shorting cancels the leading raw corridor-scale matrix element on bounded edge witnesses. Its strengthened binomial compensation (equation (27)) gives a relative (O(e^{-\gamma L_n})) edge rate, while individual arbitrary bounded-frequency cosine modes still have only the qualitative (o(D_n)) result. PF-345 extends the relative exponential upper bound to two positive-width exterior edge strips of dimension Θ(L_n), with a positive-compression trace estimate. The surviving issue is the **diagonally normalized** effective angle and its global singular-value scale.

## Research question

Let

\[
M_n=Q_n+\Lambda_{E,n}>0
\]

be the raw completed positive boundary form on one tail module. Choose bounded physical cutoffs

\[
0<\kappa_-<\kappa_+
\]

with fixed separation \`\eta=\kappa_+-\kappa_->0\`, and decompose Fourier modes into

\[
L_n=\{|\xi|\le\kappa_-\},
\qquad
T_n=\{\kappa_-<|\xi|<\kappa_+\},
\qquad
H_n=\{|\xi|\ge\kappa_+\}.
\]

Form the exact positive shorted/Schur-complement form on \`L_n\oplus H_n\`,

\[
M_n^{/T}
=
M_{LH,LH}
-
M_{LH,T}M_{TT}^{-1}M_{T,LH},
\]

with the appropriate quadratic-form interpretation if an inverse must be taken on the supported transition range.

After normalizing by the \`L\` and \`H\` diagonal blocks of \`M_n^{/T}\`, does the resulting effective low/high canonical-correlation operator become compact, Hilbert--Schmidt, or weak trace class at the scale needed by the Prime-Flute endpoint?

Equivalently: **does the fixed-width transition band absorb the leading collapsing-corridor response, or does an order-one canonical correlation survive the Schur complement?**

## Why it may matter

PF-343 removes cosmetic versions of cutoff smoothing. A positive answer here would be the first direct-angle representation in which low and high are genuinely separated at finite physical scale while all intermediate boundary degrees of freedom are still accounted for exactly.

A negative answer would close a much larger family of completed-angle architectures: not only hard binary cutoffs, but also the natural finite-width transition-band repair suggested by PF-342/PF-343.

The test is also structurally clean. It asks whether the leading thin-corridor response is carried by a transition subspace that can be shorted out, rather than asking for another absolute estimate on the same obstructed binary angle.

## Decisive test

PF-344 settles the first raw-corridor-scale obstruction, but not the completed endpoint. In strictly positive canonical finite sections, form the exact three-sector positive shorted precision

\[
\widehat M_{LH}
=M_{LH}-M_{LT}M_{TT}^{-1}M_{TH}
\]

with a fixed positive-width physical transition sector. PF-344 supplies the actual bound that its bounded-frequency *matrix entries* are \(o(D_n)\), and the strengthened edge rate \(O(D_n e^{-\gamma L_n})\) from growing binomial compensators, by explicit variational trials. Do not ask for the same raw leading-order cancellation again or reinterpret it as normalized angle decay.

Now determine the shorted diagonal energies \(\widehat M_{LL},\widehat M_{HH}\) on these witnesses and estimate

\[
\widehat Z_{LH}
=
\widehat M_{LL}^{-1/2}
\widehat M_{LH}
\widehat M_{HH}^{-1/2}
\]

in the actual finite-section spectral currency. A lower bound on the normalized correlation along infinitely many separated modules would refute this architecture. A positive endpoint requires quantitative decay after normalization, control of all high frequencies, and the PF-318/PF-320 weak-trace reassembly, not merely small unnormalized entries.

PF-346 supplies an exact control for this test. The weighted cosine Gram matrix in PF-344 is diagonally scaled Cauchy, and its transition Schur complement is another diagonal congruence of the retained Gram block. Hence **all its retained low/high canonical correlations survive shorting**, despite exponentially small raw residual energies. Yet a positive `o(D_n)` perturbation of that raw model can make the residual correlation vanish. This rules out deciding the actual angle from the weighted leading kernel and raw-scale error alone; it does not decide the flute operator.

The approximation-cost gate remains the tradeoff in PF-344's trial bound

\[
D_n\left\|f+\sum_j a_j\cos(\xi_j\cdot)\right\|_
{L^2(\operatorname{sech}t\,dt)}^2
+C\left(1+\sum_j|a_j|\right)^2.
\]

PF-344 controls the coefficient tradeoff at the two edges; PF-345's negative-binomial extrapolator controls a **positive physical-width strip** at each edge and obtains a relative exponential trace bound on its positive compressed shorted form. Arbitrary bounded exterior packets still lack a uniform coefficient-cost bound. Obtain two-sided bounds on the shorted diagonal energies and the normalized mixed response (including beyond-strip modes), then either prove a small completed angle or construct a surviving normalized witness. Keep the full growing transition block, not a fixed-rank surrogate.

In particular, quantify the nonsingular pant/seam terms and intermodule elimination **relative to the shorted diagonal energies**. PF-346 (18)–(19) gives a sufficient residual-scale comparison for transferring its model witness; that comparison is unproved. A positive compactness route must instead establish how the actual remainder changes the normalized model correlation, while retaining uniform global finite-section control.

## Evidence boundary

PF-344 proves a **partial positive** result: a fixed positive physical transition band removes the raw \(D_n\)-scale edge correlation after exact positive Schur shorting; all individual bounded-frequency cosine matrix entries are \(o(D_n)\). These are variational upper bounds on the unnormalized shorted form, not a claim about its normalized low/high canonical-correlation angle.

PF-345 strengthens the relative unnormalized control to a growing-rank edge-strip compression, but no spectral bound **after division by the shorted diagonal energies**, no uniform approximation-conditioning rate **for the whole exterior band**, no control of the unbounded high sector, and no compactness or weak-\(\mathcal S_1\) endpoint is established. General DtN/Schur theory and weighted-exponential completeness are classical; neither supplies these missing quantitative Prime-Flute estimates.

PF-346's exact correlation preservation and instability control concern the corridor **Gram model only**. PF-344's one-sided geometric trial estimate does not supply a two-sided comparison at the much smaller shorted scale. The model is therefore neither proof nor refutation of the actual transition-band architecture.

## Research disposition

Status: accepted. PF-344 removes the raw \(D_n\) term on bounded edge witnesses, and PF-345 extends relative exponential suppression to two physically positive-width edge strips of dimension \(\Theta(L_n)\) in the positive unnormalized shorted compression. The clue remains active for the materially different question of the **completed, diagonally normalized and globally reassembled** effective low/high angle. Its decisive test is now a **beyond-strip** approximation-cost/conditioning estimate **together with two-sided diagonal normalization**, or a normalized counter-witness. See [[research/prime_flute/findings/PF-344-positive-width-transition-shorting-removes-the-leading-corridor-cost.md]] and [[research/prime_flute/findings/PF-345-growing-exterior-edge-strips-have-exponentially-small-shorted-trace.md]].

[[research/prime_flute/findings/PF-346-corridor-gram-shorting-preserves-correlations-but-is-unstable-to-subleading-energy.md]] sharpens the required comparison: the leading corridor Gram model retains its normalized correlations, and `o(D_n)` raw error is insufficient to transfer that answer. The remaining actual-PDE question must control the remainder at the residual-energy scale or demonstrate its effect on the normalized angle directly. The clue stays accepted and unresolved.
