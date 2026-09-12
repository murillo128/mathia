# MI-025 — Regular sampling separates aliasing, joint coupling, label resolution, mixed degree, and raw sample count

**Evidence level:** supported by the exact phase-pushforward classifications AF-279--AF-281 and the finite-prefix separation/stability/subset-selection theorems AF-282--AF-285 on the stated known-support ordinary-Dirichlet coefficient class.

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

AF-282 proves that the joint nodes of the known prefix `1,...,N` have minimum spacing `Theta(1/N)`. AF-283 then prices coefficient stability. If mixed indices range over `{0,...,L-1}^2`, a two-point test forces instability for `L=o(N)`, while the full square with `L=30N` has a breadth-uniform least-squares inverse under per-sample absolute noise. Thus the sharp coordinatewise mixed-degree scale is

\[
L=\Theta(N).
\]

AF-284 separates degree from observation count by extracting an unweighted raw subset of `O(N log N)` samples from the dense frame. AF-285 closes that order gap. Realify the same `L=30N` complex frame, apply deterministic column subset selection to its transpose, and then close each selected real component under its complete source complex observation. The resulting set `Omega_N` uses no weights, repeats, or averaging and satisfies

\[
|\Omega_N|\le8N,
\qquad
\|\widehat b-b\|_2<\frac{64\sqrt2}{27}\epsilon<3.36\epsilon
\]

for arbitrary samplewise errors `|eta_nu|<=epsilon`. Since injectivity on `C^N` requires at least `N` complex observations,

\[
\boxed{q_{\mathrm{stable,raw}}(N)=\Theta(N).}
\]

The reusable separation is therefore sharper: **phase-fiber aliasing, retention of joint coupling, finite-prefix label spacing, stable mixed degree, raw scalar observation count, timing geometry, and target-norm conversion are different resources even when two of them happen to have the same linear order**. Exact injectivity does not imply stable recovery; linear stable degree does not imply a dense `N^2` acquisition; and linear sample count does not control time horizon, unknown support, source weighting, or the unrestricted infinite-source near-collision obstruction.

**Boundary.** AF-285 is still a finite known-support theorem. It gives an existential/deterministically constructible linear-size subset but no simple arithmetic sampling formula; selected indices still lie inside a coordinatewise horizon `L=30N`. Timing perturbations, relative/correlated noise, unknown support, conversion from `b_n=a_n n^{-c}` to another target norm, and infinite-source stability remain separate. The old `N` versus `N log N` raw-sample gap is no longer open.