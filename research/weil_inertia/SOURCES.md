# Weil-inertia literature anchors

This file records durable sources that support or constrain findings in `research/weil_inertia/`. It is not a reading log. Claims from recent unrefereed preprints are explicitly separated from the established baseline.

## Primary theorem and formal verification

- Levent Alpöge and Ralph Furman, **More than two thirds of the zeros of the Riemann zeta function are simple and on the critical line**, arXiv:2608.13637v2 (2026), https://arxiv.org/abs/2608.13637. Role: primary source for the unconditional `2/3` theorem, the Montgomery--Taylor constant `0.672500703679...`, the rank--trace/Weil-form proof, the explicit equality configurations, the bandwidth-one ceiling, and the higher-moment arithmetic barrier.
- Anthropic, **formal-math**, `zeta23/`, https://github.com/anthropics/formal-math. Role: public Lean 4 formalization of the Alpöge--Furman headline theorems. The repository documents its pinned Lean/Mathlib environment and comparator checks. The separate numerical enclosure used for the bandwidth-one ceiling is explicitly not part of the kernel-checked headline theorem.

## Classical and unconditional pair-correlation inputs

- H. L. Montgomery, **The pair correlation of zeros of the zeta function**, in *Analytic Number Theory* (St. Louis, 1972), Proc. Sympos. Pure Math. 24, AMS (1973), 181--193. Role: original pair-correlation framework and the RH-conditional `2/3` simplicity deduction whose prime-side second moment is made unconditional in the modern argument.
- Farzad Aryan, **On an extension of the Landau--Gonek formula**, *Journal of Number Theory* 233 (2022), 389--404; arXiv:1902.05473. Role: unconditional Fejér-kernel/pair-correlation second-moment input and an earlier `2/3` simplicity consequence under an additional zero-density hypothesis.
- S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya and C. L. Turnage-Butterbaugh, **An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function**, *Acta Arithmetica* 214 (2024), 357--376; arXiv:2306.04799. Role: unconditional pointwise Montgomery form-factor input over all complex zeros used by Alpöge--Furman.
- E. Bombieri, **Remarks on Weil's quadratic functional in the theory of prime numbers, I**, *Atti Accad. Naz. Lincei Rend. Lincei Mat. Appl.* 11 (2000), 183--233. Role: prior art for interpreting the negative index of finite truncations of Weil's form in terms of off-critical zero pairs.

## Optimization, multiplicity, and support barriers

- Emanuel Carneiro, Vorrapan Chandee, Friedrich Littmann and Micah B. Milinovich, **Hilbert spaces and the pair correlation of zeros of the Riemann zeta-function**, *J. Reine Angew. Math.* 725 (2017), 143--182; arXiv:1406.5462. Role: extremal-function/Hilbert-space optimization underlying the optimality of the Montgomery--Taylor window among single-window certificates of the form `2-R(psi)`.
- J. B. Conrey, A. Ghosh and S. M. Gonek, **Simple zeros of the Riemann zeta-function**, *Proc. London Math. Soc.* (3) 76 (1998), 497--522. Role: classical multiplicity-integrality inequalities mirrored by the rank--trace regrouping.
- Z. Rudnick and P. Sarnak, **Zeros of principal L-functions and random matrix theory**, *Duke Math. J.* 81 (1996), 269--322. Role: higher-correlation/support range used to locate the arithmetic obstruction to obtaining higher trace moments at the `X \asymp T` bandwidth of the unconditional proof.

## Horizontal multiplicity and conditional defect-to-zero routes

- Daniel A. Goldston, Junghun Lee, Jordan Schettler and Ade Irma Suriajaya, **Pair Correlation Conjecture for the Zeros of the Riemann Zeta-function I: Simple and Critical Zeros**, arXiv:2503.15449. Role: establishes that full pair correlation, without assuming RH, implies that asymptotically `100%` of zeta zeros are both simple and on the critical line; this is an existing conditional defect-to-zero mechanism based on horizontal multiplicity.
- Daniel A. Goldston and Ade Irma Suriajaya, **Zeta zeros on the critical line**, arXiv:2511.20059; and **Zeta zeros in a narrow vertical box**, arXiv:2603.28104. Role: isolate horizontal-distribution/near-line hypotheses under which the Montgomery constants can be recovered before the unconditional inertia argument removes that hypothesis.

## Direct follow-up claim requiring independent audit

- Michael Devine, **An Unconditional 67.3399% Bound and Conditional Advances Beyond 67.92% for Simple Critical Zeros of the Riemann Zeta Function**, Zenodo record 22066689, version 1.0.3, published 23 Aug 2026, DOI 10.5281/zenodo.22066689. **Status here: `NEEDS-AUDIT`, not established evidence.** The deposit metadata claims an unconditional `0.673399` bound using several admissible bandlimited profiles and nonnegative pair interactions, slightly above the single-window Montgomery--Taylor value but below the broader Alpöge--Furman bandwidth-one ceiling. This line must not use the claimed theorem until its analytic reductions, interval certificates, and public artifacts have been independently checked.