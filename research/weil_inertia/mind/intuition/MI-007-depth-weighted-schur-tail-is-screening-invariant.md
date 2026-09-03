# MI-007 — Density-scale screening requires a macroscopic depth-matched Schur near-null sector

**Evidence level:** supported by WI-126, WI-127, and WI-132--WI-134; the zeta-scale localization input is literature-backed through the persisted zero-density audit

## Core intuition

The normalized odd Schur complement is the right quotient for horizontal screening, but its single smallest eigenvalue is not the right quantitative invariant. An endpoint-tapered modulation block can create one arbitrarily soft collective mode while every individual odd direction remains uniformly transverse and the actual horizontal remainder stays extensive.

True density-scale screening must instead align a density-scale amount of horizontal depth with a **macroscopic lower spectral tail** of the Schur quotient. The relevant object is the joint distribution of depth weights and Schur eigenvalues, not one weakest mode.

## Strongest justified principle

WI-126 identifies Lamzouri's exact horizontal remainder as a sum of squared odd distances. WI-132 normalizes each odd divided difference by its horizontal depth and defines `S=U^*(I-P_V)U`, obtaining the useful but coarse bound `H>=lambda_min(S) D_2`.

WI-133 gives the decisive counterexample to treating `lambda_min(S)` as the screening invariant. On a fixed-depth conjugate lattice with any fixed admissible compactly supported taper, `lambda_min(S_M)=O(1/M)` although the fixed-period theorem of WI-127 keeps every diagonal distance uniformly positive and hence makes the total horizontal charge `Omega(M)`. The soft mode is an endpoint-concentration artifact rather than a screened off-line population.

WI-134 retains the whole spectrum and depth weights. After expanding multiplicities, let `0<=s_1<=...<=s_K` be the eigenvalues of the normalized Schur matrix and let the depth squares be rearranged decreasingly. Then

`H = Tr(Y^2 S) >= sum_i s_i w_i^down`.

With depth truncation `D_{2,A}=sum min(y_i^2,A^2)` and `r_a=#{i:s_i<a}`, this gives

`H >= a(D_{2,A}-A^2 r_a)_+`.

Therefore a near-sharp configuration carrying `D_{2,A}>=delta N` must have `r_a/N>=delta/A^2-o(1)` for every fixed `a>0`. At fixed equal depth, essentially the entire Schur spectrum of the off-line population must collapse toward zero. One or finitely many accidental near-null modes cannot screen macroscopic charge.

Combined with the persisted near-line zero-density localization, a positive-density off-line near-extremizer must either collapse horizontally toward the critical line on the normalized `1/log T` scale or exhibit a macroscopic normalized-Schur near-null sector. Multiplicity-generated duplicate modes and slack in other parts of Lamzouri's inequality remain separate exceptions.

## What remains possible

A useful source theorem should control a positive spectral quantile, depth-weighted spectral distribution, or equivalent frame/coercivity quantity for the actual zeta configuration. It need not give a uniform lower bound on every Schur eigenvalue. Conversely, a decisive negative would construct source-admissible zeta-scale configurations with macroscopic bounded depth whose required lower spectral sector genuinely collapses while all known counting and moment constraints remain satisfied.

## Status / novelty

Schur complements, trace rearrangement, majorization, spectral quantiles, and weighted Fourier concentration are classical. The Mathia synthesis is the screening criterion: **density-scale horizontal hiding requires density-scale collapse in the depth-matched quotient spectrum; a single soft direction is not evidence of screening**.

## Falsification criterion

Produce a sequence with macroscopic truncated square depth and `H=o(N)` but only `o(N)` Schur eigenvalues below some fixed positive threshold, contradicting the WI-134 rearrangement bound. Or derive an unconditional zeta theorem excluding the required macroscopic lower-tail collapse and thereby obtain quantitative Lamzouri slack.

## Lean-formalizable core

- Expanded-multiplicity Schur Gram construction.
- Endpoint-taper counterexample to scalar minimum coercivity.
- Trace rearrangement `Tr(Y^2S)>=sum s_i w_i^down`.
- Threshold bound `H>=a(D_{2,A}-A^2r_a)_+`.
- Near-sharpness implication to positive-density lower spectral collapse.
