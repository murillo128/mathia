# MI-028 — Sparse midpoint rigidity comes from cross-coordinate multiplicativity, not coefficient fidelity

**Evidence level:** exact synthesis from [FD-170](../../findings/FD-170-consecutive-midpoint-history-inverts-the-entire-source.md) through [FD-176](../../findings/FD-176-geometric-midpoint-null-sources-survive-growing-rank-multiplicative-fidelity.md).

The midpoint sequence is a changing linear observation of the source. Consecutive horizons invert it exactly, while FD-172--FD-174 show that geometric sparse horizons certify Möbius inside a squarefree multiplicative cone. It is tempting to attribute that recovery to coefficient sparsity, the ternary Möbius alphabet, correct prime signs, or agreement on many low multiplicative-rank layers. FD-175--FD-176 separate those effects.

A counterexample can keep `a(n)` in `{0,mu(n)}`, preserve every prime coefficient and any prescribed finite prefix, and agree with Möbius at every horizon `B^m`. FD-176 strengthens this from fixed rank to a growing rank window. For `B>=3` and every

`rho < beta_B := 1-log_B(1+floor(B/2))`,

one can preserve every coefficient with

`omega(n) <= rho log n/log log n`

while still constructing a permanent geometric-midpoint null source. Thus even a positive fraction of the natural extremal squarefree rank scale can remain correct without sparse target-rigidity.

The reusable geometric mechanism is a **balanced-row dilation plus fresh-shell repair**. If the midpoint row at `h` is already balanced, then at `Bh` the leading scaled part cancels and each old modified coordinate contributes only the bounded rounding defect

`|W_(Bh)(d)-B W_h(d)| <= floor(B/2)`.

The fresh half-shell `(Bh/2,Bh]` contains many squarefree coefficients of either Möbius sign. By forcing repair coordinates to lie above the protected rank threshold, the shell can pay the old-support debt while leaving a growing low-rank cone untouched. What fails is not local coefficient fidelity but the global product rule tying those fresh high-rank composites to prime coordinates already fixed earlier.

The lesson is broader than this midpoint formula. Sparse observation can look coercive after imposing increasingly large coordinatewise source restrictions and still fail if the admissible class lacks **cross-coordinate compatibility** strong enough to stop fresh degrees of freedom from repairing each new row. In the present line, full multiplicativity is one such compatibility; FD-176 shows that any weaker substitute must control ranks at least near the extremal `log n/log log n` scale, or couple low and high ranks in some different way.

**Boundary.** The theorem gives a sufficient non-rigidity range `rho<beta_B` for `B>=3`; it does not identify the sharp growing-rank threshold, settle the dyadic `B=2` growing-rank analogue, give pairwise sparse inversion, or improve the Franel--Landau destination estimate. The next structural target is a quantitative compatibility condition between large-but-incomplete multiplicative fidelity and full product coupling that makes recursive shell repair impossible.