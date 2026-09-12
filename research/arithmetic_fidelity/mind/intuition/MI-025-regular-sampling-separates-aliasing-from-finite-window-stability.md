# MI-025 — Regular sampling separates aliasing, joint coupling, label resolution, mixed degree, and observation count

**Evidence level:** supported by the exact phase-pushforward classifications AF-279--AF-281 and the finite-prefix separation/stability theorems AF-282--AF-283 on the stated known-support ordinary-Dirichlet coefficient class.

For

\[
F(s)=\sum_n a_n n^{-s},\qquad \sum_n|a_n|n^{-c}<\infty,
\]

a single regular vertical lattice retains the phase `n -> e^{-ih log n}`, not `log n` itself. With

\[
R_h=\{r\in\mathbb Q_{>0}:h\log r\in2\pi\mathbb Z\},
\]

AF-279 gives exact coefficient fidelity for the complete bilateral lattice iff `R_h={1}`. AF-280 shows that finitely many **separate lattice marginals** cannot generally repair individually resonant quotients on the unrestricted weighted `ell^1` source class, even when the tuple of phase labels is injective.

AF-281 gives the complementary classification for genuinely **joint mixed samples** `F(c+i(k\cdot h))`: they are the Fourier coefficients of the joint torus pushforward, so exact fidelity is equivalent to joint phase injectivity, namely `cap_j R_(h_j)={1}` for ordinary Dirichlet frequencies. Coupling can therefore repair exact aliases that separate marginals lose.

For the concrete two-prime repair

\[
h_2=2\pi/\log2,\qquad h_3=2\pi/\log3,
\]

AF-282 proves that the joint nodes of the known prefix `1,...,N` have minimum spacing `Theta(1/N)`. Direct label discrimination therefore needs inverse-breadth phase accuracy, not exponentially fine resolution.

AF-283 then prices the coefficient-stability degree itself. If mixed indices range over `{0,...,L-1}^2`, a two-point adjacent-coefficient test gives

\[
\kappa_\infty(N,L)\ge
\frac{(N-1)\log2}{4\pi(L-1)},
\]

so `L=o(N)` cannot have a breadth-uniform inverse modulus. Conversely the full square with `L=30N` is uniformly stable: the arithmetic node separation and the multivariate Vandermonde theorem give `sigma_min>0.9L`, hence per-sample error `||eta||_infty<=epsilon` yields least-squares coefficient error `||\hat b-b||_2<10epsilon/9` for `b_n=a_n n^{-c}`. Thus the sharp coordinatewise mixed-degree scale is

\[
L=\Theta(N).
\]

This closes a conditioning question but not the acquisition bill. The sufficient square contains `L^2=Theta(N^2)` scalar moments, while arbitrary recovery of `N` coefficients needs at least `N` scalar observations. Nothing in AF-283 decides whether a sparse arithmetic mixed-index family can achieve comparable stability with near-linear sample count. Nor does it remove the separate costs of timing precision, known support, the weighting `b_n=a_nn^{-c}`, or the unrestricted infinite-source near-collision obstruction.

The reusable separation is therefore: **phase-fiber aliasing, retention of joint coupling, finite-prefix label spacing, stable mixed degree, scalar observation count, and target-norm conversion are different resources**. In this arithmetic channel the first four are now explicitly priced; the live finite-prefix uncertainty has moved to sparse observation design and target-sensitive recovery, not hidden exponential Vandermonde conditioning.

**Boundary.** The stable theorem assumes the known prefix `1,...,N` and the dense rectangular mixed-moment set. It is not an unknown-support super-resolution result, a sparse-sampling theorem, or a breadth-uniform inverse for the unrestricted infinite weighted `ell^1` source.