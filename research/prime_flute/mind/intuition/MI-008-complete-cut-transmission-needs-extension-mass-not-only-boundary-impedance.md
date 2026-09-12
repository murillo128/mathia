# MI-008 — The flute mixed-response gate has an intrinsic logarithmic accumulated-loss threshold

**Evidence level:** proved local operator/source-space and scalar accumulation boundaries through PF-300; the factorization of the complete physical mixed response remains open.

For the fixed physical high-pass spaces, PF-292 gives a diverging local frequency floor. PF-296 proves that the canonical fixed-axis synthesis is uniformly bounded from the explicit weighted source space `ell^1(q)` into positive Sobolev regularity. A complete normalized response with uniformly bounded `sum_i q_i|a_i|`, controlled transport, and negligible residual therefore cannot sustain the PF-290 local high-band shorting deficit.

PF-297 identifies the exact behavior of one repeated local factor. Every fixed-axis Robin inverse is nonexpansive in the same `ell^1(q)` currency. Finite Galerkin sections are strictly contractive only because `q`-mass leaks into omitted rows; the complete positive inverse preserves `q`-mass.

PF-298 removes a second possible uniform discount. On constant boundary data a tight one-cusp pant has response

\[
c_n\begin{pmatrix}1&-1\\-1&1\end{pmatrix}+\operatorname{diag}(\kappa_{n,L},\kappa_{n,R}),
\]

with `c_n\gtrsim s_n^{-1}` and bounded nonnegative killing, so the isolated scalar loss satisfies `epsilon_n=O(s_n)`.

PF-299 identifies the coarse endpoint: `sum s_n=infinity` while `sum s_n^q<infinity` for every `q>1`. PF-300 resolves the logarithmic refinements by using the intrinsic coordinate

\[
t_n=F(p_n),\qquad s_n=\frac{(t_n-t_{n-1})+(t_{n+1}-t_n)}2.
\]

For every nonnegative decreasing `phi`, the seam sum `sum s_n phi(t_n)` has the same convergence behavior as `int phi(t)dt`. Hence

\[
\sum_n\frac{s_n}{(1+F(p_n))^\beta}
\]

diverges exactly for `0<=\beta<=1` and converges for `\beta>1`. Prime-gap irregularity is absorbed into the exact mesh; no average-gap replacement is needed.

The scalar live quantity is consequently the relative killing **inside this quadrature currency**. If `epsilon_n\lesssim s_n(1+F(p_n))^{-\beta}` with `\beta>1`, the scalar transmission product stays positive. If `epsilon_n\gtrsim s_n(1+F(p_n))^{-\beta}` with `\beta<=1`, it vanishes. At the critical law

\[
\epsilon_n\sim a\frac{s_n}{1+F(p_n)},
\]

PF-300 gives the sharper prediction

\[
\prod_{k\le n}(1-\epsilon_k)=(\log p_n)^{-a+o(1)}.
\]

Thus “`epsilon_n=o(s_n)`” is still not a meaningful global criterion; the actual slowly varying factor decides accumulation.

This remains only one compression of the physical problem. The PF-298 constant channel is not proved invariant under the complete `P/H` Schur return. The full gate is still the normalized mixed return/reassembly map, where accumulated nonconstant-mode damping, support loss, source-specific forcing/cancellation, or a change of coefficient currency may dominate the scalar chain.

**Boundary.** PF-300 proves an intrinsic quadrature/integral test for monotone scalar weights, not the asymptotic of the actual pant killing and not a full mixed-response factorization. Highly oscillatory source-dependent weights require additional control.