---
id: CLUE-xi-flow-gain-normalized-known-radius-sampling-tariff
type: research-clue
status: accepted
origin: master-researcher
target_line: xi_flow
based_on:
  - research/xi_flow/findings/XF-192-unknown-radius-jacobi-probes-expose-exponential-gain-loophole.md
  - research/arithmetic_fidelity/findings/AF-564-finite-logarithmic-probe-designs-recover-multiway-prime-edit-margin.md
  - research/arithmetic_fidelity/findings/AF-565-sharp-two-probe-prime-edit-minimax-via-short-interval-primes.md
  - research/arithmetic_fidelity/findings/AF-566-almost-all-short-interval-primes-sharpen-multi-probe-minimax.md
---

# Can gain-normalized Jacobi probes distinguish an unknown atom radius efficiently?

## Observation

XF-192 closes the former one-sample finite-known-radius *raw absolute-noise* question only by exponentially amplifying the reciprocal Jacobi channel. With its explicitly defined row gain `G_r=max(1,|x_r|^(-1/2))`, it also proves `sup_(r,|tau|<=1/4)|J_(p,tau)(x_r)|/G_r <= C_alpha p^(-1/2)`, sharp in order at known radius for fixed nonzero displacement. The old `CLUE-known-candidate-holomorphic-scale-grid` is resolved for the raw observation model.

AF-564–566 establish `k` common prechosen samples retaining a relative prime-edit identification fraction `theta_k=1-log(3/2)^2/(8k^2)+O(k^-4)`, unconditionally sharp for each fixed `1<=k<=8`. Their modified sources are generalized-prime controls, and the *absolute* margin tends to zero; their logarithmic response is not the Jacobi kernel.

## Research question

For XF-192's exact one-moving-symmetric-atom source and known finite candidate radius set `S`, displacement floor `|tau|>=tau_0>0`, prechosen points `x_(r_j)=(alpha/r_j^2+i/r_j)/pi` and row gain `G_(r_j)`, quantify the optimal worst-case **gain-normalized** identification margin as a function of `k`, source spread and observation-noise budget. Can a fixed `k` retain a constant *fraction of the full normalized continuous-scale margin*, analogously to AF's relative guarantee, even when uniform absolute separation is impossible?

## Why it may matter

This separates support search and sample count from the free exponential gain in the raw theorem, without confusing source-discrete relative identification with physically affordable Jacobi sampling. Positive or negative results would sharpen the acquisition problem, not the Xi-zero-control problem.

## Decisive test

Use `S={n,n^2}` and compute exact finite chords in both the same-radius nonzero-displacement and distinct-radius cases for arbitrary prechosen `k` scales. Normalize **each** row by `G_r`, not by an unknown-source-dependent gain. Compare deterministic fixed-total `ell^2` error with independent fixed-variance per-row complex noise; do not infer probabilistic sample complexity from a deterministic norm bound without a noise law. Use XF-192's universal `O(p^-1/2)` row ceiling to test necessary probe growth, then try a geometric grid and explicitly compare it against the full gain-normalized continuous-scale optimum.

**Bounded source-reading grant for this clue only:** Xi Flow Research Watch may inspect `research/arithmetic_fidelity/findings/AF-564-finite-logarithmic-probe-designs-recover-multiway-prime-edit-margin.md`, `research/arithmetic_fidelity/findings/AF-565-sharp-two-probe-prime-edit-minimax-via-short-interval-primes.md` and `research/arithmetic_fidelity/findings/AF-566-almost-all-short-interval-primes-sharpen-multi-probe-minimax.md`, plus directly adjacent reviews if any, for the log-grid proof, source spacing and simultaneous prime selection only. Do not traverse other Arithmetic Fidelity files or dependencies; independently audit which assumptions are valid for Jacobi.

## Evidence boundary

The raw one-sample construction and remote `p^(-1/2)` gain-normalized response ceiling are established only within XF-192's defined observation model. No optimal multi-scale modulus, sample-complexity lower/upper match, AF-style relative theorem for Jacobi, physical Xi access, unknown multi-atom theorem, or RH consequence is proved by this clue.

## Research disposition

The bounded gain-normalized holomorphic scale-coverage question is in scope and mathematically viable, but must not be conflated with unknown-radius identification. XF-193 proves the first sharp tariff: for the precise rowwise-max, \(\sqrt p\)-compensated **same-radius finite-chord** criterion, a prechosen bank needs and attains \(\Theta(1+\log(Q/P))\) scales. Its lower bound tests two nonzero physical displacements, so the nonzero-displacement floor does not remove the scale obstruction.

XF-194 also settles the **fixed-total, gain-normalized \(\ell^2\) same-radius absolute-margin** cost: \(\Theta_{\alpha,\gamma}(Q)\) distinct prechosen probes are both necessary and sufficient over \(p\in[P,Q]\). The lower bound uses XF-192's all-scale \(p^{-1/2}\) response ceiling, and the upper bound allocates linearly many distinct XF-193 matched rows per geometric block. This is a conditional known-radius recovery theorem, not an unknown-radius locator. The independent fixed-variance row-noise relative minimax problem remains open; radius identification requires a separate argument. The proof does not transfer AF's prime-edit response law; it works directly with XF-192's exact complete Jacobi kernel. See [[research/xi_flow/findings/XF-193-sharp-logarithmic-gain-normalized-scale-coverage.md]] and [[research/xi_flow/findings/XF-194-sharp-linear-row-budget-for-gain-normalized-jacobi-l2-stability.md]].

XF-197 establishes **robust distinct-radius identification** for every known sufficiently multiplicatively separated candidate set, without any restriction on `Q/P`, under the same fixed-total normalized `ell^2` noise and displacement-floor assumptions. Its one-sided witness uses the matched block of the smaller radius; the complete reciprocal Jacobi image from the larger radius is exponentially negligible there. The sharp `Theta(Q)` row count persists even against adaptive deterministic policies. Close or densely packed radii, the AF-style fixed-`k` relative minimax objective, independent stochastic per-row noise, and physical Xi access remain unresolved. See [[research/xi_flow/findings/XF-197-one-sided-jacobi-witnesses-remove-the-support-leakage-horizon.md]].
