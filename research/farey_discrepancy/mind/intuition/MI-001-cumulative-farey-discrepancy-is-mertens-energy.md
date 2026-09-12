# MI-001 — Farey occupation has a deterministic critical host, packet amplification, and an explicit global loss exponent

**Evidence level:** supported by exact source/occupation reductions through FD-061; no positive global occupation theorem is claimed.

The cumulative Farey obstruction is controlled by the physical shell source

\[
c(n)=\Delta\mathcal H(n)=\sum_{dm=n}\frac{\mu(m)}d.
\]

FD-054--FD-058 separate deterministic transfer, strong short-interval cancellation, sparse represented-start sampling, and maximal ambient-window localization. Signed multiplicative rays are not coercive, while quadratic occupation admits additive transfer.

FD-059 identifies the natural host scale. Put `A_X=|\mathcal H(X)|` and `Q_X=X/A_X`. A favorable squarefree host at `q\asymp Q_X` has a nonsquarefree neighbor whose quotient point keeps a fixed positive fraction of the spike. FD-060 shows that subpower slack above `Q_X` can instead be spent on multiplicity: there are `K_X\to\infty`, `K_X=X^{o(1)}`, and hosts `q\asymp K_XQ_X` carrying a packet of `K_X` nonsquarefree rows, each with source amplitude at least `A_X/2-1`.

FD-061 now measures how much of that packet survives the **global** denominator. Along a false-RH zero-frontier spike

\[
A_X=X^{\Theta+o(1)},\qquad \frac12<\Theta<1,
\]

the packet horizon is

\[
T_X=X^{2-\Theta+o(1)},
\]

and for every fixed Schur head `D` and every `eta>0`,

\[
T_X^{\beta_\Theta+\eta}\nu_{T_X,D}\to\infty,
\qquad
\beta_\Theta=\frac{2\Theta(1-\Theta)}{2-\Theta}.
\]

The all-horizon FD-049 estimate contributes exponent `2\Theta-1`; on packet horizons the stronger available exponent is their minimum. Since

\[
\beta_\Theta-(2\Theta-1)=\frac{2-3\Theta}{2-\Theta},
\]

the CRT packet improves the global polynomial-loss barrier exactly for `\Theta>2/3`.

The growing packet factor itself does not buy an additional power. Enlarging `K_X` also enlarges `T_X`, and after division by the global energy envelope its contribution is only subpower. Packet multiplicity, host-relative amplification, and normalized global occupation are therefore distinct currencies.

The deterministic transfer barrier remains sharp. Preserving a fixed fraction over `K` offsets by bounded increments alone requires `K\lesssim qA_X/X`; below `q=o(X/A_X)` new source localization is still load-bearing. On the global side, improving FD-061 requires a denominator estimate sharper than the generic zero-frontier envelope **on the same packet horizons**, or a transfer construction that reaches many nonsquarefree rows with less horizon displacement.

**Boundary.** FD-061 gives a source-selected lower-rate theorem for `U/E`, not `\liminf U/E>0`, an asymptotic formula, or monotonicity. It does not solve the below-critical source-localization problem. The exponent crossover at `2/3` records which proved mechanism gives the stronger polynomial barrier, not a new zero-free region.