# MI-001 — Farey transfer is governed by causal protection plus the recurrence geometry of frontier-sized source blocks

**Evidence level:** supported by the exact source/occupation reductions through FD-076 and the persisted Pintz local-Mertens input; no bounded multiplicative-gap, logarithmic-density, or RH criterion is claimed.

FD-071 shows why arbitrary-later persistence does not improve normalization: a later source spike can dominate the same-horizon denominator and dilute an earlier episode. FD-072 gives the complementary positive mechanism. At a `sigma`-record `X`, `sigma>1/2`, the causal choice `T=4X`, `D=3` confines every reciprocal quotient to the record-controlled prefix while row `4` samples the record exactly, forcing a fixed positive nonsquarefree occupation.

FD-073 thickens this point mechanism. Since the physical source `H` is one-Lipschitz, a record of amplitude `A=|H(X)|` protects an additive block of radius comparable to `A`; every point in that block remains a quantitative near-record after recentering its causal horizon. FD-074 constrains strict record centers by `phi(rad X)>sigma|H(X)|` and aligns the sign with `mu(rad X)` once the amplitude is large. FD-075 then forces aligned coefficient mass throughout backward subwindows and, on amplitude scale, at least `>> A^2/X` same-parity hosts with radical `>> A`.

FD-076 supplies the first genuinely global spacing information. Combining Pintz's fixed-power-window maximal-order theorem for the ordinary Mertens function with the exact inverse floor-harmonic transform gives, for every fixed `lambda in (0,1)`,

`max_(X^(1-lambda)<=n<=X) |H(n)| = X^(Theta+o(1))`,

where `Theta` is the rightmost zeta-zero frontier. Consequently, for every `0<sigma<Theta`, the running normalized maximum satisfies

`P_sigma(X)=X^(Theta-sigma+o(1))`,

and every sufficiently large power window `[X^(1-lambda),X]` contains a strict `sigma`-record. If `X_j` are consecutive strict records, then

`log X_(j+1) / log X_j -> 1`,

and `|H(X_j)|=X_j^(Theta+o(1))`.

Under a false-RH frontier `Theta>1/2`, the protected blocks therefore have radius `X_j^(Theta+o(1))`, and FD-075's local cloud sharpens to

`|Q_j| >= X_j^(2Theta-1-o(1))`,

with `rad n >= X_j^(Theta-o(1))` for its selected hosts. The source cannot hide frontier-sized protected episodes behind any fixed power gap, and it cannot lower their amplitudes below the actual zero-frontier exponent.

The remaining gap is now **subpower recurrence** rather than arbitrary multiplicative sparsity. The relation `X_(j+1)=X_j^(1+o(1))` still allows `X_(j+1)/X_j -> infinity`, while a protected block has relative width `X_j^(Theta-1+o(1))`. To force a global same-horizon occupation statement, the exact coefficient law must improve this power-scale recurrence to enough ordinary/logarithmic recurrence, or another argument must aggregate the power-dense local swarms without requiring overlap.

**Boundary.** FD-076 rules out fixed power gaps but does not prove bounded multiplicative gaps, positive logarithmic density, overlap of protected blocks, or positive global occupation. At `Theta=1/2` the polynomial cloud exponent vanishes, so the supercritical swarm argument does not remove the critical logarithmic loss.