# MI-001 — Farey occupation has a deterministic critical host, a host-uniform subcritical packet, and a same-horizon denominator bottleneck

**Evidence level:** supported by exact source/occupation reductions through FD-063 plus the cited short-interval Möbius theorem; no positive global occupation theorem is claimed.

The cumulative Farey obstruction is controlled by the physical shell source

\[
c(n)=\Delta\mathcal H(n)=\sum_{dm=n}\frac{\mu(m)}d.
\]

FD-054--FD-058 separate deterministic transfer, strong short-interval cancellation, sparse represented-start sampling, and maximal ambient-window localization. Signed multiplicative rays are not coercive, while quadratic occupation admits additive transfer.

FD-059 identifies the natural deterministic host scale. Put `A_X=|\mathcal H(X)|` and `Q_X=X/A_X`. A favorable squarefree host at `q\asymp Q_X` has a nonsquarefree neighbor whose quotient point keeps a fixed positive fraction of the spike. FD-060 shows that subpower slack above `Q_X` can be spent on multiplicity.

FD-062 shows that genuine source cancellation changes this geometry qualitatively. If

\[
A_X(\log X)^B\ge X^\vartheta,\qquad \vartheta>0.55,
\]

and `B+\kappa<1/3`, the same spike supports a growing packet with `K_X\le(\log X)^\kappa` while `qA_X/X\asymp(\log X)^{-B}\to0`. The logarithmic saving is a quantitative currency: one part moves the host below the deterministic scale and the rest buys packet width.

FD-063 strengthens the quantifier without spending more analytic budget. With `R_X=A_X(\log X)^B`, `K_X=\lfloor(\log X)^\kappa\rfloor`, and `Y_X=X/(8R_X)`, source transfer is uniform for every host `Y_X\le q\le2Y_X`. Multiples of four among the next `K_X` rows give a deterministic nonsquarefree packet of density at least `1/4`, hence

\[
U_{qX,D}\ge\left(\frac1{4\zeta(2)}-o(1)\right)K_XA_X^2
\]

throughout the corridor. The earlier growing CRT modulus is therefore not intrinsic to packet occupation. Host entropy remains available for a later denominator estimate, averaging argument, or favorable-host selection.

The global occupation problem remains separate. Generic same-horizon denominator bounds still absorb the available subpower gains, and FD-063 does not improve the `\vartheta>0.55` short-interval threshold or the `B+\kappa<1/3` budget. The live theorem is now even more sharply identified: exploit the **host-uniform corridor** to control `E_{qX,D}`, or obtain stronger source localization below the current short-interval range.

**Boundary.** The corridor theorem is conditional on the stated source amplitude and all-short-interval Möbius input. It proves neither positive normalized occupation nor a new zero-free region. Its durable contribution is to separate packet availability from host selection: below the deterministic host scale, the packet can already be present uniformly while the denominator remains uncontrolled.