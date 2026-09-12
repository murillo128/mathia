# MI-025 — Regular sampling separates marginal aliasing, joint coupling, and finite-budget stability

**Evidence level:** supported by the exact phase-pushforward classifications AF-279--AF-281 on the stated absolutely convergent ordinary-Dirichlet coefficient class.

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

Thus coupling can repair exact aliases that no separate marginal repairs.

The cost of that repair is geometrically explicit. The subgroup `sum_j Z h_j` is either one discrete lattice or dense in `R`. If all individual cadences resonate, strict repair cannot occur in the discrete case; it requires the dense case and therefore arbitrarily fine mixed times or unbounded integer combinations. On a known `M`-frequency truncation, mixed polynomials of degree at most `M-1` can interpolate distinct joint phase nodes, but on the unrestricted infinite source every fixed mixed-index box has no uniform inverse modulus because remote frequencies recur near the same joint phase.

Hence three currencies remain independent: **fiber aliasing, retention of joint coupling, and finite acquisition stability**. Joint moments solve the second and can solve exact aliasing, but they do not make unbounded source breadth a finite-budget problem.

**Boundary.** These statements concern declared ordinary Dirichlet frequencies and weighted `ell^1` amplitudes. Narrow Euler, automorphic, positive, sparse, or otherwise structured source categories can alter both the exact kernel and the conditioning problem.
