# MI-001 — Nyman target geometry remembers absolute scale, but source normal equations can expose that mismatch early

**Evidence level:** exact augmented-Gram, semigroup, full-defect, and residual-localization results through NB-009

## Core intuition

The Nyman approximation problem is not determined by generator geometry among itself. The fixed target supplies a separate coordinate, and canonical multiplicative self-similarity can preserve every local Gram relation while losing relevance to that target.

The newer evidence adds a constructive counterpoint. Although generic finite semigroup probes can alias the target and periodicity localizes residual mismatch only at exponential lcm scale, the **actual best residual is not generic**. Its projection normal equations force visible target mismatch at polylogarithmic index. Source optimality can therefore recover useful absolute-scale information much earlier than representation geometry alone suggests.

## Strongest justified principle

NB-001 gives `d_N^2=1-b_N^*G_N^+b_N` and Gram-preserving controls with different target distances. NB-002 realizes the loss inside the canonical semigroup: a scale-`m` copy preserves the generator Gram block while target pairings shrink by `m^{-1/2}` and projection energy by `1/m`.

NB-004--NB-006 show that finitely many target-character probes and every finite harmonic cutoff remain vulnerable to Mellin aliasing; exact full-semigroup identification is not finite coercivity. NB-007 closes the infinite boundary: the full harmonic `ell^2` defect is finite exactly on the target line, and every fixed non-target vector pays logarithmic cumulative defect, but the coefficient has no uniform lower bound on the target-orthogonal unit sphere.

NB-008 locates a witness for each canonical finite residual using common periodicity, but only by index `lcm(2,...,N)+1`, with exponentially small guaranteed amplitude. NB-009 shows that this cost is not intrinsic. The single orthogonality equation against `g_2` forces a tail-average witness by `O(d_N^{-2})` with gauge at least a constant times `d_N^6`; the known Nyman distance lower bound converts this to index `O(log N)` and amplitude `Omega((log N)^{-3})`.

## Program consequence

The next target-aware theorem should exploit the finite best-residual equations, not generic semigroup character. A promising surface is to aggregate the polylogarithmic tail-average witness into unavoidable truncated harmonic energy or a dual certificate strong enough to improve control of `d_N`.

Absolute scale remains load-bearing, but NB-009 shows that it can be recovered from source optimality without scanning to the common period. Additional normal equations should be valued by the quantitative coercivity they force, not by probe count alone.

## Counterevidence / boundary

NB-009 does not improve the known Nyman distance bound; it uses that bound to express its residual-localization scale in `N`. One early tail-average mismatch may still carry too little total energy to constrain `d_N` beyond known results, and generic scale-dependent aliases remain valid controls outside the best-residual source class.

## Epistemic status

**Exact target-information boundary plus exact source-selected polylogarithmic witness localization; no improved Nyman approximation rate or RH consequence is established.**

## Falsification criterion

Produce a canonical best residual violating the NB-009 localization bound, or show that its forced early witness can be made arbitrarily irrelevant to every admissible finite semigroup/dual certificate. A positive continuation should quantify how the projection equations convert early mismatch into target-distance coercivity.