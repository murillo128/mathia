# MI-028 — Dyadic screening forces a uniform archimedean reserve before any nonpositive one-signed Weil test

**Evidence level:** exact structural consequence from [WI-301](../../findings/WI-301-screened-prime-ladders-force-a-uniform-archimedean-reserve.md), combining the rearrangement inequalities of [WI-298](../../findings/WI-298-rearrangement-collapses-complete-one-signed-screening-to-first-prime-aperture.md) with the independently replayed compact-window floor of [WI-300](../../findings/WI-300-l08-compact-window-certificate-would-kill-complete-one-signed-screening.md)

Let `f` be a nonzero real compactly supported Weil test with one global sign, normalized so `f>=0`. If every power-of-two autocorrelation vanishes,

`C_f(k log 2)=0` for all `k>=1`,

then nonnegativity turns screening into measurable disjointness: the positivity set and all its `log 2` translates are pairwise disjoint. Hence its measure is at most `log 2`.

Symmetric decreasing rearrangement preserves the `L^2` norm and compresses the support into radius `(log 2)/2`, while the source-side inequalities of WI-298 make the prime-deleted archimedean form nonincreasing. The rearranged test therefore lies inside the independently certified `0.8` window, where WI-300 gives the uniform floor

`Q_W(f^*) >= c_0 ||f||_2^2`,  `c_0=8.9e-18`.

Because every prime-power translation of the rearranged test vanishes, this lower bound is purely archimedean and transfers back:

`q_arch(f) >= c_0 ||f||_2^2`.

Consequently any one-signed dyadically screened test with `Q_W(f)<=0` must carry an **unscreened arithmetic reserve** of at least the same size:

`P(f) >= c_0 ||f||_2^2`.

If all active prime-power autocorrelations are screened, then `P(f)=0` and the inequality is impossible. Complete one-signed screening is therefore incompatible with nonpositivity at **every aperture**, not just at a first crossing.

The reusable mechanism is a defect-to-unscreening principle. Screening the first-prime ladder is not a way to remove the arithmetic source for free: in the one-signed class it forces geometric packing, packing permits rearrangement into a certified compact window, and compact-window positivity creates a quantitative archimedean reserve that any nonpositive test must pay back through unscreened odd-prime interactions.

This is stronger than a spectral-bottom statement because it no longer uses a null equation, first-crossing minimality or a bound on the original support radius. It also explains why the first prime is special: dyadic screening compresses below the first arithmetic shift, so all prime terms vanish after rearrangement. Screening a later prime ladder alone does not have the same consequence because smaller prime shifts may still overlap.

**Boundary.** One-sign is essential both for turning zero autocorrelation into disjointness and for the rearrangement inequalities. Sign-changing functions can screen by cancellation. The reserve does not identify which odd-prime lag supplies the missing mass and does not imply unrestricted Weil positivity or RH.