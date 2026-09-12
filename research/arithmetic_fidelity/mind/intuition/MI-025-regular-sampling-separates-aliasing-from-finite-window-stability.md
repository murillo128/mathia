# MI-025 — Regular sampling separates aliasing, coupling, degree, sample count, and timing provenance

**Evidence level:** supported by exact phase-pushforward classifications AF-279--AF-281 and finite-prefix separation/stability/timing theorems AF-282--AF-287 on the stated known-support ordinary-Dirichlet coefficient class.

For

\[
F(s)=\sum_n a_n n^{-s},\qquad \sum_n|a_n|n^{-c}<\infty,
\]

a single regular vertical lattice retains the phase `n -> e^{-ih log n}`, not `log n` itself. With

\[
R_h=\{r\in\mathbb Q_{>0}:h\log r\in2\pi\mathbb Z\},
\]

AF-279 gives exact coefficient fidelity for the complete bilateral lattice iff `R_h={1}`. AF-280 shows that finitely many **separate lattice marginals** cannot generally repair individually resonant quotients on the unrestricted weighted `ell^1` source class, even when their phase-label tuple is injective. AF-281 gives the complementary classification for genuinely **joint mixed samples**: exact fidelity is equivalent to joint phase injectivity, `cap_j R_(h_j)={1}`.

For the concrete two-prime repair

\[
h_2=2\pi/\log2,\qquad h_3=2\pi/\log3,
\]

AF-282 proves that the joint nodes of the known prefix `1,...,N` have minimum spacing `Theta(1/N)`. AF-283 prices coefficient stability: if mixed indices range over `{0,...,L-1}^2`, a two-point test forces instability for `L=o(N)`, while `L=30N` admits a breadth-uniform stable inverse. AF-284--AF-285 separate degree from observation count: deterministic subset selection gives an unweighted linear-size family of raw complex mixed moments and rank forces at least `N` complex observations.

AF-286 shows that **timing error itself splits into different information classes**. If every requested time has the same unknown offset `tau`, the observation matrix factors exactly as

\[
\widetilde y=A D_\tau b,
\qquad
D_\tau=\operatorname{diag}(n^{-i\tau})_{n\le N}.
\]

The nominal exact decoder therefore returns `D_tau b`. For an arbitrary complex source class, `(b,tau)` is identifiable only modulo the gauge `(b,\tau)\sim(D_\epsilon b,\tau-\epsilon)`. Fixed relative coefficient distortion has the sharp common-clock scale `T=Theta(1/log N)`.

AF-287 closes the apparent extra cost for arbitrary independent rowwise jitter. Starting from the uniformly conditioned complete two-prime Vandermonde frame, classical Kadison--Singer/frame sparsification yields an **unweighted `O(N)` raw subframe with condition number bounded independently of `N`**. For rowwise offsets `|tau_j|<=T`, the exact expansion

\[
\widetilde A-A
=\sum_{k\ge1}\frac{(-i)^k}{k!}D_{\tau^k}A\Lambda^k,
\qquad \Lambda=\operatorname{diag}(\log1,\ldots,\log N),
\]

gives

\[
\|\widetilde A-A\|
\le\|A\|\bigl(e^{T\log N}-1\bigr).
\]

Hence the nominal decoder has relative `ell^2` error at most `K(e^{T\log N}-1)` for an absolute frame-condition constant `K`. The common-offset subclass supplies the matching lower-order obstruction, so

\[
T_{\rm independent\ jitter}(N)=\Theta(1/\log N).
\]

The earlier `sqrt(N)` loss came from passing through an `ell^1` source estimate after controlling only one side of the frame spectrum; it is not an intrinsic jitter information bill.

The reusable separation is therefore: **phase-fiber aliasing, retention of joint coupling, finite-prefix label spacing, stable mixed degree, raw sample count, frame conditioning, common-clock gauge, independent jitter, time horizon, and target norm are distinct resources**. Exact injectivity does not imply stable recovery; linear stable degree does not imply dense `N^2` acquisition; and a common-mode error that is an exact source symmetry should be quotiented or externally marked rather than priced as generic noise.

The remaining timing question is target-relative rather than frame-relative. A downstream functional invariant under `b -> D_tau b` needs no external clock-origin lift, while full coefficient recovery pays the inverse-log scale. Unknown support, infinite Dirichlet sources, different coefficient norms, drift/rate error, and source constraints remain separate problems.

**Boundary.** AF-282--AF-287 are finite known-support theorems. The frame-sparsification subset is existential and its constants are not optimized. The gauge nonidentifiability assumes arbitrary complex coefficients; constrained sources can break it. None of these results supplies analytic continuation, zero-location information, or infinite-source stability.