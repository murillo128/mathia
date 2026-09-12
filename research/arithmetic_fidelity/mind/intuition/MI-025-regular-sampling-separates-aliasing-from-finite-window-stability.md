# MI-025 — Regular sampling separates aliasing, joint coupling, phase-label resolution, and coefficient stability

**Evidence level:** supported by the exact phase-pushforward classifications AF-279--AF-281 and the finite-prefix separation theorem AF-282 on the stated absolutely convergent ordinary-Dirichlet coefficient class.

For

\[
F(s)=\sum_n a_n n^{-s},\qquad \sum_n|a_n|n^{-c}<\infty,
\]

a single regular vertical lattice retains the phase `n -> e^{-ih log n}`, not `log n` itself. With

\[
R_h=\{r\in\mathbb Q_{>0}:h\log r\in2\pi\mathbb Z\},
\]

AF-279 gives exact coefficient fidelity for the complete bilateral lattice iff `R_h={1}`.

AF-280 classifies a finite family observed as **separate lattice marginals**: it is faithful on the unrestricted weighted `ell^1` source class iff at least one cadence is individually nonresonant. If every cadence resonates, a finite group-algebra interaction lies in the common kernel. An injective tuple of phase labels is not enough when acquisition discards mixed moments.

AF-281 gives the complementary classification for genuinely **joint mixed samples** `F(c+i(k\cdot h))`. They are all Fourier coefficients of the joint torus pushforward, so exact fidelity is equivalent to joint phase injectivity; for ordinary Dirichlet frequencies this is precisely

\[
\bigcap_j R_{h_j}=\{1\}.
\]

Thus coupling can repair exact aliases that no separate marginal repairs. If all individual cadences resonate, strict repair requires their generated time subgroup to be dense rather than one discrete lattice, so complete exact recovery pays unbounded mixed integer-combination complexity.

AF-282 prices a different finite-breadth resource for the concrete two-prime repair

\[
h_2=2\pi/\log2,\qquad h_3=2\pi/\log3.
\]

For the joint phase nodes

\[
z_n=(e^{-2\pi i\log n/\log2},e^{-2\pi i\log n/\log3}),
\qquad 1\le n\le N,
\]

the minimum coordinatewise chord separation satisfies

\[
\frac{4}{3^{1/4}\log6}\frac1N
\le \delta_N
\le \frac{2\pi}{\log2}\frac1{N-1}.
\]

So the finite prefix's **labels themselves** separate at order `1/N`: direct noisy label identification needs `O(1/N)` phase accuracy, equivalently only `O(\log N)` bits of absolute resolution. Exact joint alias repair therefore does not hide an exponentially collapsing pairwise node spacing on the ordinary prefix.

This does **not** price arbitrary coefficient recovery. Interpolating an unknown amplitude vector from mixed Fourier moments still pays mixed-mode degree, collective node geometry, observation design, and the inverse condition number of the resulting moment/Vandermonde system. On the unrestricted infinite source every fixed mixed-index box still has remote near-collisions and no source-breadth-independent inverse modulus.

The useful separation is therefore fourfold: **phase-fiber aliasing, retention of joint coupling, finite-prefix label resolution, and coefficient-recovery conditioning**. AF-282 removes pairwise phase-label collapse as the explanation for severe finite-prefix instability in the `log2/log3` channel; any stronger bill must enter through the moment budget, coefficient inversion, noise model, or a broader source category.

**Boundary.** These statements concern declared ordinary Dirichlet frequencies and weighted `ell^1` amplitudes. Narrow Euler, automorphic, positive, sparse, or otherwise structured source categories can alter both the exact kernel and the conditioning problem. The `Theta(1/N)` result is pairwise joint-node separation, not a lower singular-value estimate for a multivariate interpolation matrix.
