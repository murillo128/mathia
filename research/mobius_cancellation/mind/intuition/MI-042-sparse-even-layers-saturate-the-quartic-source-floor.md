# MI-042 — Quartic source saturation forces actual columns into the half-loaded band

**Evidence level:** proved for the reciprocal-endpoint common-source architecture by [MC-323](../../findings/MC-323-varying-modulus-prime-halasz-montgomery-obstruction.md) through [MC-327](../../findings/MC-327-quartic-saturation-forces-half-loaded-source-mass.md); the individual conductor input and Plotkin mechanism are literature-backed/classical, and no RH consequence is claimed.

The universal loading problem is already minimax-sharp. For any nonempty family of nonzero modes `a in F_2^R` with nonnegative weights, some nonzero abstract source column carries asymptotically at least one half of the total mode weight. Thus no universal nonnegative mode selection can improve the quartic common-radical floor obtained from independent near-quadratic conductor bills.

MC-327 now removes the main ambiguity left by that abstract minimax statement. For the **actual** common source package, let `a_p` be the number of generators using source prime `p`, let `nu_p=log p/log P`, and define

`B_R = sum_p nu_p ((2a_p-R)/R)^2`.

The weighted pair-distance identity is exact:

`sum_(i<j) log m_ij = (R^2/4)(1-B_R) log P`.

Combined with the varying-modulus conductor obstruction, this gives

`liminf (1-B_R) log P/log y >= 4`.

Hence quartic saturation `log P/log y=4+o(1)` forces `B_R->0`: for every fixed `epsilon>0`, asymptotically all logarithmic source mass lies on columns with `|a_p/R-1/2|<epsilon`. Persistent imbalance `B_R>=beta>0` costs a strictly larger source exponent, at least `4/(1-beta)` in the limit. Under quartic saturation, almost all generator and pair package costs are also pinned in density to exponent two.

So the surviving actual-source question is no longer whether economical arithmetic columns can avoid the high-loading region. **They cannot.** At the quartic frontier the source is forced into the maximally pair-loaded Hamming band. What remains unresolved is structure *inside* that band: there are exponentially many near-half-loaded columns, and the present positive incidence accounting does not distinguish the arithmetic subset among them.

The genuine escapes are therefore sharper: prove an arithmetic restriction within the half-loaded band that interacts with a destination theorem, derive a joint or signed conductor relation not reducible to positive independent bills, improve the individual conductor horizon, or change the endpoint/source representation. Merely enlarging or reweighting the mode family, or hoping the actual source avoids half loading while keeping quartic cost, is closed.
