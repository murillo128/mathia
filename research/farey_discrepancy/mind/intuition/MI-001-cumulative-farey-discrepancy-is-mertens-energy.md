# MI-001 — Farey transfer has a critical host budget, a polynomial-packet tradeoff, and a two-thirds normalization barrier

**Evidence level:** supported by exact source/occupation reductions through FD-065 plus the cited all-short-interval Möbius theorem; no positive global occupation theorem is claimed.

The cumulative Farey obstruction is controlled by the physical shell source

\[
c(n)=\Delta\mathcal H(n)=\sum_{dm=n}\frac{\mu(m)}d.
\]

FD-054--FD-058 separate deterministic transfer, genuine short-interval cancellation, sparse represented-start sampling, and maximal ambient-window localization. FD-059 identifies the deterministic critical host scale `Q_X=X/A_X`, where `A_X=|\mathcal H(X)|`: favorable squarefree hosts at `q\asymp Q_X` force a nearby nonsquarefree row that retains a fixed fraction of the spike. FD-060 shows that subpower slack can be spent on packet multiplicity.

FD-062--FD-063 show that physical short-interval cancellation changes the geometry and removes combinatorial host scarcity. FD-064 then classifies the larger power-gap family. On a zero-frontier spike `A_X=X^{\Theta+o(1)}`, hosts `q\asymp X^\lambda` can support polynomial packets, but after paying the later horizon the optimized loss exponent is

\[
b_\Theta(\lambda)
=\frac{1-\Theta+(2\Theta-1)\lambda}{1+\lambda},
\qquad
b_\Theta'(\lambda)=\frac{3\Theta-2}{(1+\lambda)^2}.
\]

Hence `\Theta=2/3` is invariant across the direct power-gap family. If `\Theta>2/3`, moving away from the critical host worsens the exponent; if `1/2<\Theta<2/3`, the all-horizon estimate remains stronger; at `\Theta=2/3`, all admissible hosts have the same `1/3` loss. Polynomial packet multiplicity does not beat the barrier because its gain is exactly offset by horizon cost.

FD-065 shows that **moving the Schur head cannot repair this ledger either**. Let the head grow as `D=X^{\delta+o(1)}`. The zero-frontier denominator becomes smaller by the apparent factor `D^{2\Theta-1}`, but the scalar leverage satisfies

\[
C_T-C_D\asymp D^{-1}.
\]

Their product pays `D^{-2(1-\Theta)}`. Equivalently, both the packet and deterministic terminal scalar loss exponents acquire the same positive penalty

\[
\frac{2\delta(1-\Theta)}{1+\lambda}.
\]

The common penalty cancels when the two obstructions are compared, so the `\Theta=2/3` crossover survives unchanged, and each scalar obstruction is optimized at fixed/subpower head. A shorter physical tail can improve a raw occupation lower bound while worsening the final scalar quantity.

FD-064 also identifies a geometric phase boundary. The packet rows have `r=T^{\lambda/(1+\lambda)+o(1)}`. A direct all-short-interval theorem available only above square-root scale keeps these rows strictly inside the cube-root Jordan core. Reaching `r\asymp T^{1/3}` is equivalent to source transfer at square-root interval scale.

The durable separation is therefore sharper: **local packet capacity, host entropy, head truncation, Schur leverage, and normalized occupation are different currencies**. Progress must change a load-bearing ingredient rather than optimize one of the already priced internal knobs. The surviving possibilities are a source-coupled denominator, an averaging/selection theorem that uses correlations across the host corridor, source cancellation at/below square-root scale, or another row interaction that does not pay the direct-transfer horizon ledger.

**Boundary.** FD-064--FD-065 classify the current direct transfer combined with the generic zero-frontier denominator and Schur scalarization. They do not rule out source-coupled denominator estimates, almost-all/maximal interval theorems usable on adaptive hosts, stronger row interactions, or other global normalizations. No new zero-free region or positive global occupation theorem follows.