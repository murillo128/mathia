# MI-004 — Mean-absolute Mertens control is RH-complete, and sub-L1 moments do not transport the needed excursion mass

**Evidence level:** exact Mellin/checkpoint results, literature-backed Pintz lower bound, and exact matched-control barriers through MC-121

## Core intuition

The mean-absolute endpoint is RH-complete, but statistics below `L^1` forget exactly the rare coherent amplitude that the endpoint consumes. MC-117--MC-120 show that this is not repaired merely by imposing square-free support, multiplicativity, uniform control across a polynomial window, or even one fixed multiplicative function recurring on infinitely many such windows.

MC-121 removes a different apparent obstacle: **the RH-strength mean-absolute output does not need to be controlled on a dense scale mesh**. Pintz's 1987 theorem says any fixed off-critical zero forces excessive mean-absolute Mertens mass at every sufficiently large scale. Therefore square-root-scale control of the actual `D_M(X)` along any unbounded checkpoint sequence already excludes all off-critical zeros.

The surviving difficulty is consequently information content, not physical-scale interpolation of the final endpoint. A successful source theorem must recover first-absolute excursion amplitude for Möbius on some rigorously produced unbounded scales from genuinely weaker arithmetic information. Dense-scale or correlation coherence may be useful ways to achieve that recovery, but density of the resulting `D_M` checkpoints is no longer itself a necessary gate.

## Strongest justified principle

MC-115 proves directly that square-root-scale mean-absolute Mertens control continues `1/zeta(s)` into every half-plane `Re s>1/2+epsilon`, giving the exact RH equivalence. MC-116 shows that subpower-dense deterministic checkpoints suffice to manufacture the corresponding all-scale bound by monotone interpolation, and its exponent-loss statement for lacunary checkpoints remains correct for that interpolation mechanism.

MC-121 uses a different classical bridge. Pintz's 1987 lower bound states that an off-critical zero `beta_0+i gamma_0` forces

`D_M(Y) > Y^(beta_0)/gamma_0^5`

for every sufficiently large `Y`. Hence for **any** unbounded sequence `X_j`, the bounds `D_M(X_j)=O_epsilon(X_j^(1/2+epsilon))` for all `epsilon>0` are equivalent to RH. Equivalently, RH is characterized by the liminf exponent of the actual Möbius mean being at most `1/2`.

For every `0<p<1`, MC-117 quantifies the information gap from a fractional moment to the first absolute mean. MC-118 realizes the missing excursion using balanced prime blocks inside a multiplicative square-free-supported comparator. MC-119 keeps the weak moment controlled throughout a polynomial window, and MC-120 removes the moving-comparator objection by using one fixed multiplicative function on infinitely many windows.

These controls still matter after MC-121: they show that a weak moment or generic multiplicative structure does not automatically upgrade to `D_M`. What disappears is the claim that the final RH-scale `D_M` estimate itself must arrive on subpower-dense scales.

## Counterevidence / boundary

Pintz's theorem is Möbius/zeta-specific and runs from a hypothetical zero to a lower bound for the actual Mertens mean. Generic balanced-block comparators do not inherit it, so MC-121 does not invalidate MC-117--MC-120 or turn sub-`L^1` control into an endpoint theorem.

MC-121 also does not improve any unconditional upper bound for `D_M`, construct a local-to-global transfer, or show how to choose useful checkpoints from weaker arithmetic information. MC-116 remains the correct theorem when one wants an all-scale physical bound by interpolation without invoking the zero-to-arithmetic lower bound.

## Epistemic status

**Proved/literature-backed endpoint reduction and matched-control obstruction; open Möbius-specific source mechanism.** The 1987 Pintz lower bound used by MC-121 is audited prior art; stronger separate Pintz-profile claims retained elsewhere remain subject to their own evidence status.

## Falsification criterion

Derive the RH-scale first absolute mean on some unbounded sequence from a source condition genuinely weaker than that conclusion and satisfied by Möbius, while showing why the MC-117--MC-120 coherent-excursion comparators cannot satisfy it. Conversely, a proof that such a checkpoint estimate still requires subpower-density despite Pintz's every-large-scale lower bound would contradict the persisted MC-121 reduction.