# MI-001 — Farey occupation has full counting exponent; compatible accumulation is now the bottleneck

**Evidence level:** supported by the exact source/occupation reductions through FD-083 and the persisted Pintz inputs. Full polynomial counting exponent of constant-strength occupied horizons is proved, but no positive density, compatible integer-ratio chain, transport inequality, or RH criterion is claimed.

FD-071--FD-081 build a strict ladder from causal record protection and frontier-near abundance through physical-energy weighting, logarithmic annular recurrence and subpower pointwise first passage. FD-082 then identifies the exact information contained in first passage alone: `log g_(n+1)/log g_n -> 1` is compatible with only `(log log X)^2` good horizons, so a fixed gain per hit need not accumulate to a power saving.

FD-083 imports the missing physical anti-concentration information rather than strengthening first passage abstractly. If

`a_H = log((H+1)/H) E_(H,D)`,

then the zero-frontier envelope gives `a_H << H^(2 sigma-1)` for every `sigma>Theta`, while every fixed power annulus has total energy `Y^(2Theta+o(1))`. A constant energy-weighted nonsquarefree occupation therefore cannot be concentrated on a sparse set of physical horizons: a fixed positive fraction of the annular energy requires `Y^(1-o(1))` distinct atoms.

Consequently, for every fixed `epsilon>0` and every admissible occupation threshold `eta`, the actual good set satisfies

`# {H : X < H <= X^(1+epsilon), nu_(H,D)>eta} = X^(1+epsilon-o(1))`,

in logarithmic-exponent form, and cumulatively `N_eta(X)=X^(1-o(1))`. The cardinality obstruction isolated by FD-082 is therefore absent for the physical Schur/Jordan occupation set. FD-082 remains the correct control showing that this density does not follow from recurrence alone; FD-083 is precisely the extra source-specific atom cap that rules out the sparse control.

The remaining Farey obstruction is **compatibility, not scarcity**. A set of `X^(1-o(1))` occupied integers need not contain the multiplicative or integer-ratio geometry required by the existing GCD/Schur transport steps, and favorable projective gains at unrelated horizons cannot simply be multiplied. Nor does exponent-one counting imply positive natural or logarithmic density.

The next useful theorem must therefore convert full-counting occupation into a scale geometry that the RH-facing accumulation mechanism can consume: for example a compatible chain, a transport inequality across many occupied horizons, a gap-sensitive gain, or a genuinely nonlocal estimate that couples occupied and intervening scales. Reproving abundance in another counting norm without solving that compatibility step does not address the current bottleneck.

**Boundary.** FD-083 uses the physical per-horizon energy envelope and annular total-energy exponent; it does not upgrade arbitrary power-syndetic sets. Its count is `X^(1-o(1))`, not positive density. No statement is made that the good horizons form a suitable divisor chain or that the fixed gains of earlier local inequalities compose across them.
