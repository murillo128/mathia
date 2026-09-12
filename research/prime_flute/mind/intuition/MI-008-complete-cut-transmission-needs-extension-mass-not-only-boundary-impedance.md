# MI-008 — The flute mixed-response gate has an exact intrinsic attenuation-density reduction

**Evidence level:** proved local operator/source-space and scalar accumulation boundaries through PF-301; the factorization of the complete physical mixed response remains open.

For the fixed physical high-pass spaces, PF-292 gives a diverging local frequency floor. PF-296 proves that the canonical fixed-axis synthesis is uniformly bounded from the explicit weighted source space `ell^1(q)` into positive Sobolev regularity. A complete normalized response with uniformly bounded `sum_i q_i|a_i|`, controlled transport, and negligible residual therefore cannot sustain the PF-290 local high-band shorting deficit.

PF-297 identifies the exact behavior of one repeated local factor. Every fixed-axis Robin inverse is nonexpansive in the same `ell^1(q)` currency. Finite Galerkin sections are strictly contractive only because `q`-mass leaks into omitted rows; the complete positive inverse preserves `q`-mass.

PF-298 removes a second possible uniform discount. On constant boundary data a tight one-cusp pant has response

\[
c_n\begin{pmatrix}1&-1\\-1&1\end{pmatrix}+\operatorname{diag}(\kappa_{n,L},\kappa_{n,R}),
\]

with `c_n\gtrsim s_n^{-1}` and bounded nonnegative killing. Writing

\[
r_n=\frac{\kappa_n}{c_n},\qquad \theta_n=(1+r_n)^{-1},
\]

one has `0\le r_n\le Cs_n`.

PF-299 identifies the coarse endpoint: `sum s_n=infinity` while `sum s_n^q<infinity` for every `q>1`. PF-300 resolves monotone slowly varying refinements in the intrinsic coordinate `t_n=F(p_n)`. PF-301 removes the remaining monotonicity restriction for the **actual bounded pant coefficient sequence**.

Put

\[
b_n=\frac{r_n}{s_n}=\frac{\kappa_n}{c_ns_n},
\]

and let `\psi_n` be the triangular hat at the exact intrinsic mesh point `t_n`, so that `\int\psi_n=s_n`. The piecewise-linear attenuation field

\[
B_N(t)=\sum_{n\ge N}b_n\psi_n(t)
\]

then satisfies the exact identity

\[
\boxed{
\int_{t_{N-1}}^\infty B_N(t)\,dt
=\sum_{n\ge N}r_n.
}
\]

No smoothness, monotonicity, or independence from the prime gaps is needed. Because PF-298 gives bounded `b_n` and PF-299 gives `\sum s_n^2<\infty`, one also has `\sum r_n^2<\infty`, so

\[
\boxed{
\prod_{n\ge N}\theta_n>0
\iff B_N\in L^1(t_{N-1},\infty),
}
\]

and, up to one finite positive multiplicative renormalization,

\[
\prod_{n=N}^M\theta_n
=C_N\exp\!\left(-\int_{t_{N-1}}^{t_M}B_N(t)\,dt\right)(1+o(1)).
\]

Thus prime-gap-correlated oscillation of the local killing is no longer an accumulation loophole. The symmetric seam weights are exactly the mass-lumped areas of the intrinsic hat basis, so the discrete scalar chain has a canonical continuous attenuation density for **every** bounded nonnegative coefficient sequence.

The scalar live quantity is now sharply localized: determine whether the actual directional densities

\[
b_{n,\pm}=\frac{\kappa_{n,\pm}}{c_ns_n}
\]

have finite or infinite intrinsic mass, or obtain enough block/integral control to decide it. A monotone pointwise model is unnecessary. Raw relative killing and exact loss differ only by finite intrinsic mass, so either density gives the same survival/extinction classification.

This remains only one compression of the physical problem. The PF-298 constant channel is not proved invariant under the complete `P/H` Schur return. The full gate is still the normalized mixed return/reassembly map, where accumulated nonconstant-mode damping, support loss, source-specific forcing/cancellation, physical-high remainders, or a change of coefficient currency may dominate the scalar chain.

**Boundary.** PF-301 is an exact scalar accumulation reduction, not a calculation of the actual density and not a full mixed-response factorization. It gives no finite/infinite answer for `\int B_\pm`, and it does not justify replacing the complete `P/H` dynamics by the constant channel.