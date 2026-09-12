# MI-025 — Regular sampling separates aliasing, coupling, degree, sample count, and timing provenance

**Evidence level:** supported by exact phase-pushforward classifications AF-279--AF-281 and finite-prefix separation/stability/timing theorems AF-282--AF-286 on the stated known-support ordinary-Dirichlet coefficient class.

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

AF-282 proves that the joint nodes of the known prefix `1,...,N` have minimum spacing `Theta(1/N)`. AF-283 prices coefficient stability: if mixed indices range over `{0,...,L-1}^2`, a two-point test forces instability for `L=o(N)`, while `L=30N` admits a breadth-uniform stable inverse. AF-284--AF-285 then separate degree from observation count: deterministic subset selection yields an unweighted set of at most `8N` raw complex mixed moments with a breadth-uniform least-squares inverse under samplewise absolute noise. Rank forces at least `N` complex observations, hence

\[
q_{\mathrm{stable,raw}}(N)=\Theta(N).
\]

AF-286 shows that **timing error itself splits into different information classes**. If every requested time has the same unknown offset `tau`, the observation matrix does not suffer arbitrary rowwise noise:

\[
\widetilde y=A D_\tau b,
\qquad
D_\tau=\operatorname{diag}(n^{-i\tau})_{n\le N}.
\]

The nominal exact decoder therefore returns exactly `D_tau b`. For an arbitrary complex source class, `(b,tau)` is identifiable only modulo the gauge

\[
(b,\tau)\sim(D_\epsilon b,\tau-\epsilon).
\]

The exact worst-case relative coefficient displacement is

\[
R_N(T)=
\begin{cases}
2\sin(T\log N/2),&0\le T\le\pi/\log N,\\
2,&T\ge\pi/\log N,
\end{cases}
\]

so fixed relative distortion requires and suffices to have `T=Theta(1/log N)`, equivalently only `Theta(log log N)` fractional clock bits in a fixed time unit. This is a **provenance/gauge bill**, not a condition-number bill and not an observation-count bill.

Independent per-sample jitter is different. AF-286 only gives the elementary sufficient relative scale `T=O(1/(sqrt(N) log N))` from AF-285 plus `ell^1` control, while the common-offset subclass proves the necessary scale can be no better than `O(1/log N)`. The remaining `sqrt(N)` gap is therefore specifically a rowwise timing-jitter/derivative-frame question.

The reusable separation is now: **phase-fiber aliasing, retention of joint coupling, finite-prefix label spacing, stable mixed degree, raw sample count, common-clock gauge, independent jitter, time horizon, and target norm are distinct resources**. Exact injectivity does not imply stable recovery; linear stable degree does not imply dense `N^2` acquisition; linear sample count does not calibrate a clock; and an error mode that is an exact source symmetry should be quotiented or externally marked rather than priced as generic additive noise.

**Boundary.** AF-286 is still a finite known-support theorem and its exact gauge nonidentifiability assumes arbitrary complex coefficients. Source constraints can break the gauge. The independent-jitter upper bound may be nonsharp, and none of AF-282--AF-286 settles unknown support, conversion from `b_n=a_n n^{-c}` to another target norm, or unrestricted infinite-source stability.