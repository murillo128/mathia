# MI-025 — Regular sampling separates aliasing, joint coupling, label resolution, mixed degree, and observation count

**Evidence level:** supported by the exact phase-pushforward classifications AF-279--AF-281 and the finite-prefix separation/stability/sparsification theorems AF-282--AF-284 on the stated known-support ordinary-Dirichlet coefficient class.

For

\[
F(s)=\sum_n a_n n^{-s},\qquad \sum_n|a_n|n^{-c}<\infty,
\]

a single regular vertical lattice retains the phase `n -> e^{-ih log n}`, not `log n` itself. With

\[
R_h=\{r\in\mathbb Q_{>0}:h\log r\in2\pi\mathbb Z\},
\]

AF-279 gives exact coefficient fidelity for the complete bilateral lattice iff `R_h={1}`. AF-280 shows that finitely many **separate lattice marginals** cannot generally repair individually resonant quotients on the unrestricted weighted `ell^1` source class, even when the tuple of phase labels is injective. AF-281 gives the complementary classification for genuinely **joint mixed samples**: exact fidelity is equivalent to joint phase injectivity, `cap_j R_(h_j)={1}`.

For the concrete two-prime repair

\[
h_2=2\pi/\log2,\qquad h_3=2\pi/\log3,
\]

AF-282 proves that the joint nodes of the known prefix `1,...,N` have minimum spacing `Theta(1/N)`. AF-283 then prices the coefficient-stability degree. If mixed indices range over `{0,...,L-1}^2`, a two-point test forces instability for `L=o(N)`, while the full square with `L=30N` has a breadth-uniform least-squares inverse under per-sample absolute noise. Thus the sharp coordinatewise mixed-degree scale is

\[
L=\Theta(N).
\]

AF-284 separates this degree bill from scalar observation count. The dense square has `900N^2` rows, but its frame lower bound and equal row norms allow classical matrix Chernoff sparsification. There exists an **unweighted subset of distinct raw mixed indices** with

\[
|\Omega_N|=O(N\log N)
\]

whose least-squares inverse remains breadth-uniform; with per-sample adversarial error at most `epsilon`, one explicit construction gives

\[
\|\widehat b-b\|_2<\frac{20}{9}\epsilon.
\]

No repeated measurements or acquisition weights are used. Randomness proves existence only. The finite-prefix sample-count gap is therefore now `Omega(N)` by rank versus `O(N log N)` by raw unweighted sparsification. Whether the logarithm can be removed in this acquisition model is open; weighted linear-size spectral sparsification is a different measurement/noise model and does not settle it.

The reusable separation is therefore: **phase-fiber aliasing, retention of joint coupling, finite-prefix label spacing, stable mixed degree, raw scalar observation count, timing geometry, and target-norm conversion are different resources**. Exact injectivity does not imply stable recovery; stable linear degree does not force quadratic acquisition; and near-linear sample count does not by itself control time horizon, unknown support, source weighting, or the unrestricted infinite-source near-collision obstruction.

**Boundary.** AF-284 is an existential sparse-sampling theorem on the known prefix `1,...,N`. It is not an explicit deterministic sampling formula, an `O(N)` unweighted theorem, an unknown-support super-resolution result, or a breadth-uniform inverse for the unrestricted infinite weighted `ell^1` source.