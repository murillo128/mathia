# MI-001 — Farey occupation has a deterministic critical host, subpower packet amplification, and a below-critical localization barrier

**Evidence level:** supported by exact source/occupation reductions through FD-060; no positive global occupation theorem is claimed.

The cumulative Farey obstruction is controlled by the physical shell source

\[
c(n)=\Delta\mathcal H(n)=\sum_{dm=n}\frac{\mu(m)}d.
\]

Signed multiplicative rays are not coercive, while quadratic occupation admits additive transfer. FD-054--FD-058 separate deterministic transfer, strong short-interval cancellation, sparse represented-start sampling, and maximal ambient-window localization.

FD-059 identifies the natural host scale. Put `A_X=|\mathcal H(X)|` and `Q_X=X/A_X`. A favorable squarefree host at `q\asymp Q_X` has a nonsquarefree neighbor whose quotient point keeps a fixed positive fraction of the spike. Along a false-RH spike `A_X=X^{\Theta+o(1)}`, this already reaches

\[
q=T^{\alpha_\Theta+o(1)},
\qquad
\alpha_\Theta=\frac{1-\Theta}{2-\Theta},
\]

for every `\Theta>1/2` without a short-interval theorem.

FD-060 shows that subpower slack above `Q_X` can be spent on **multiplicity**, not only on making one twin more accurate. There are `K_X\to\infty`, with `K_X\le\log\log Q_X`, and squarefree hosts

\[
2K_XQ_X\le q\le(2K_X+1)Q_X
\]

such that every `q+d`, `1\le d\le K_X`, is nonsquarefree. For `T=qX`, bounded increments give every packet row

\[
|\mathcal H(\lfloor T/(q+d)\rfloor)|\ge A_X/2-1,
\]

hence for every fixed Schur head `D`,

\[
U_{T,D}\ge \frac{K_X}{\zeta(2)}\left(\frac{A_X}{2}-1\right)^2.
\]

If `J_q(T)=w(q)A_X^2` is the selected squarefree host-row energy, then `w(q)\le1` and

\[
\frac{U_{T,D}}{J_q(T)}\ge \frac{K_X}{4\zeta(2)}(1-o(1))\to\infty.
\]

Because `K_X=X^{o(1)}`, this growing packet still sits at the same zero-frontier **power exponent** `\alpha_\Theta`. The exponent therefore hides a genuine subpower distinction: `qA_X/X\asymp1` guarantees only bounded deterministic multiplicity, while `qA_X/X\to\infty` can support a packet whose local nonsquarefree occupation grows without bound relative to its selected host row.

The deterministic barrier is correspondingly sharp. Preserving a fixed fraction of one spike over `K` consecutive offsets by the one-Lipschitz law alone requires, at this mechanism level,

\[
K\lesssim \frac{qA_X}{X}.
\]

Thus a growing packet cannot be forced at a genuinely constant critical ratio without additional source cancellation. For `q=o(X/A_X)`, even one fixed-fraction transfer leaves the bounded-increment regime and the short-interval/maximal-localization machinery becomes load-bearing.

**Boundary.** The packet only proves an unbounded ratio against the chosen host row, not a fixed lower bound for the global occupation ratio `U_{T,D}/E_{T,D}`. Other low rows may contribute much more to `E_{T,D}`. The remaining global gate is therefore not “produce more transferred rows” in isolation, but compare the packet scale `K_XA_X^2` with the aggregate competing low-row energy, or find a different mechanism that controls that denominator.
