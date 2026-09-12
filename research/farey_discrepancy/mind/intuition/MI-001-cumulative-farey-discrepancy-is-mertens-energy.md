# MI-001 — Farey transfer has reached subpower pointwise recurrence, but not yet a power-saving accumulation law

**Evidence level:** supported by the exact source/occupation reductions through FD-082 and the persisted Pintz inputs. No eventual pointwise occupation bound, logarithmic density lower bound, bounded logarithmic horizon entropy, or RH criterion is claimed.

FD-071--FD-081 build a strict ladder: causal record protection, abundant frontier-near values, physical-energy weighting, logarithmic annular recurrence, subpower annular first passage, and finally a good physical horizon in every sufficiently late fixed-power window. For every fixed `eta<c_q`, the first good horizon satisfies `log sigma_eta(X)/log X -> 1`.

FD-082 identifies the exact counting content of this endpoint. If the good horizons are `g_n`, then the first-passage law is equivalent to

`log g_(n+1)/log g_n -> 1`,

or equivalently `log log g_(n+1)-log log g_n -> 0`. This forces `N_eta(X)/log log X -> infinity`, but no fixed positive power of `log X`. An explicit integer-ratio control with `g_n=2^(ceil(exp(sqrt n)))` has the same first-passage geometry while `N(X)~(log log X)^2` and its logarithmic horizon entropy diverges.

That control exposes the accumulation mismatch. If a downstream proof earns only a fixed favorable factor `kappa<1` at each good horizon, the recurrence information alone permits total gain

`kappa^(N(X)) = X^(-o(1))`,

which cannot change a power exponent. Power-syndeticity is therefore a recurrence statement, not yet the scale-density currency needed by a fixed-per-hit proof architecture.

The residual Farey problem is now precise. One must either strengthen pointwise occupation enough to produce roughly logarithmically many usable scales, prove anti-concentration that converts annular energy recurrence into many distinct witnesses, extract a gain that grows with the gaps or horizon energies, or use a nonlocal estimate that also consumes the bad intervals. Merely iterating the existing first-passage theorem with a bounded reward per hit cannot reach the RH-facing power threshold.

**Boundary.** FD-082 is an information-sufficiency obstruction, not a theorem that the actual good set is as sparse as the control sequence. The physical set may be much denser. What is proved is that such density does not follow from FD-081 alone, so any argument requiring it must import additional arithmetic or energy-distribution information.