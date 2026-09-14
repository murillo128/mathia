# MI-016 — Critical translation locality is frequency-off-diagonal concentration

**Evidence level:** exact necessary-condition reduction from [PF-337](../../findings/PF-337-critical-translations-expose-the-frequency-off-diagonal-mass-of-the-normalized-pant-insertion.md), using the completed transport reductions of PF-336 and the critical packet interval of PF-328. No pant-matrix lower bound, concentration theorem or direct-angle endpoint is claimed.

PF-336 reduces completed polar translation transport to the Hilbert--Schmidt commutator of the normalized pant insertion `K=Q_L^(-1/2) Lambda_LL Q_L^(-1/2)`. PF-337 diagonalizes the translation action and identifies exactly what this commutator measures. In the physical Fourier basis,

`||[K,tau_t]||_(S2)^2 = sum_(j,k) 4 sin^2((xi_j-xi_k)t/2) |K_(jk)|^2`.

Averaging over the positive-length PF-328 critical interval produces a nonnegative weight on every Fourier matrix coefficient. Any fixed physical-frequency separation receives a uniform positive weight, so an `o(1)` translation commutator forces the entire Hilbert--Schmidt mass away from an arbitrarily thin frequency diagonal to vanish.

The arithmetic finite-boundary subsequence makes the test sharper. There the critical translations are asymptotically half-cuff translations. For every fixed odd Fourier offset `m`, the averaged weight tends to `4`, hence the translation route requires `sum_k |K_(k+m,k)|^2=o(1)`. The nearest odd band `m=1` is therefore a minimal concrete falsification target for the actual one-cusp-pant insertion.

The reusable point is that “quasilocality” is no longer an abstract operator property here. At the critical packet scale it is a **positive frequency-off-diagonal mass statement**. A persistent fixed-separated tail, or just one persistent odd Fourier diagonal on the finite-boundary subsequence, kills the route before square-root or polar analysis enters.

This also separates two remaining currencies. Frequency-diagonal concentration is necessary for translation compatibility of the completed polar rotation, but it does not by itself give spatial concentration of a completed reference packet. The latter still needs an independent localized profile or cutoff/off-diagonal theorem.

**Boundary.** PF-337 gives necessary conditions, not sufficiency. Even if every tested fixed odd band vanishes, the full uniform-in-translation commutator may still fail through frequency separations shrinking with the geometry, and even a successful commutator does not establish the final low/high correlation estimate.