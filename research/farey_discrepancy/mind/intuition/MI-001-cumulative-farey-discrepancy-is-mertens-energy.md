# MI-001 — Farey occupation has a deterministic critical host, subcritical packet transfer, and a same-horizon denominator bottleneck

**Evidence level:** supported by exact source/occupation reductions through FD-062 plus the cited short-interval Möbius theorem; no positive global occupation theorem is claimed.

The cumulative Farey obstruction is controlled by the physical shell source

\[
c(n)=\Delta\mathcal H(n)=\sum_{dm=n}\frac{\mu(m)}d.
\]

FD-054--FD-058 separate deterministic transfer, strong short-interval cancellation, sparse represented-start sampling, and maximal ambient-window localization. Signed multiplicative rays are not coercive, while quadratic occupation admits additive transfer.

FD-059 identifies the natural deterministic host scale. Put `A_X=|\mathcal H(X)|` and `Q_X=X/A_X`. A favorable squarefree host at `q\asymp Q_X` has a nonsquarefree neighbor whose quotient point keeps a fixed positive fraction of the spike. FD-060 shows that subpower slack above `Q_X` can instead be spent on multiplicity, producing `K_X\to\infty` nonsquarefree rows.

FD-062 shows that genuine source cancellation changes this geometry qualitatively. If

\[
A_X(\log X)^B\ge X^\vartheta,\qquad \vartheta>0.55,
\]

and `B+\kappa<1/3`, the same spike supports a growing CRT packet with `K_X\le(\log X)^\kappa` while

\[
\frac{qA_X}{X}\asymp(\log X)^{-B}\to0.
\]

Every packet quotient samples `\mathcal H(X)+o(A_X)`. Thus the deterministic barrier `q\asymp X/A_X` is sharp only for bounded-increment transfer; it is not an intrinsic barrier once short-interval Möbius cancellation is admitted. The current logarithmic saving acts as a quantitative currency: one part moves the host below the deterministic scale and the rest can be spent on packet width, with the proved budget `B+\kappa<1/3`.

The global occupation problem remains separate. FD-061 gives a source-selected polynomial lower-rate theorem for `U/E`; FD-062 improves the local geometry and lowers the packet horizon, but the available generic denominator estimate still contains uncontrolled subpower losses. Even a packet whose local mass beats its selected host by a factor `K_X\to\infty` does not imply `\liminf U/E>0`.

The live obstruction has therefore moved. In the range `\vartheta>0.55`, packet existence below the critical host is no longer the issue; the next theorem must sharpen the **same-horizon energy denominator** or exploit a transfer whose global row-count/horizon balance survives normalization. Separately, the present all-short-interval input leaves the `\Theta\le0.55` localization range unresolved.

**Boundary.** FD-062 is conditional on the stated source amplitude and the available all-short-interval Möbius range. Its `B+\kappa<1/3` budget is not claimed optimal. It proves neither positive normalized occupation nor any new zero-free region.