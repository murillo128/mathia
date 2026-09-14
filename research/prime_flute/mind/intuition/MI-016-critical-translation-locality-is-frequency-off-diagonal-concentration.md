# MI-016 — Critical translation locality is frequency-off-diagonal concentration

**Evidence level:** exact necessary-condition reduction from [PF-337](../../findings/PF-337-critical-translations-expose-the-frequency-off-diagonal-mass-of-the-normalized-pant-insertion.md), strengthened on the finite-boundary subsequence by [PF-338](../../findings/PF-338-finite-boundary-critical-translations-force-total-half-cuff-mixing-to-vanish.md). No pant-matrix lower bound, concentration theorem or direct-angle endpoint is claimed.

PF-336 reduces completed polar translation transport to the Hilbert--Schmidt commutator of the normalized pant insertion `K=Q_L^(-1/2) Lambda_LL Q_L^(-1/2)`. PF-337 diagonalizes the translation action and identifies exactly what this commutator measures:

`||[K,tau_t]||_(S2)^2 = sum_(j,k) 4 sin^2((xi_j-xi_k)t/2) |K_(jk)|^2`.

Averaging over the positive-length PF-328 critical interval produces a nonnegative weight on every Fourier matrix coefficient. Any fixed physical-frequency separation receives a uniform positive weight, so an `o(1)` translation commutator forces the Hilbert--Schmidt mass at every fixed nonzero physical-frequency separation to vanish.

PF-338 makes the finite-boundary test substantially stronger. Along `r_n=h_(n+1)/h_n -> 0`, every retained **odd** Fourier offset has a common positive lower weight, including offsets growing proportionally to the cuff length. If `H_n=tau_(ell_n/2)` is half-cuff translation, then the whole odd sector is exactly its cross-parity block and

`avg_(t in I_n) ||[K_n,tau_t]||_(S2)^2 >= (c_*/4)||[K_n,H_n]||_(S2)^2`.

Hence the translation route requires `||[K_n,H_n]||_(S2)=o(1)`, equivalently `||P_(n,+) K_n P_(n,-)||_(S2)=o(1)`. The old nearest-neighbor test is only one component of this stronger aggregate obstruction.

There is a basis-free falsifier. Because `H_n` is an involution, `||K_n-H_nK_nH_n||_(S2)=||[K_n,H_n]||_(S2)`. Thus one retained-low unit profile whose normalized pant energy differs by order one from the energy of its half-cuff translate kills the PF-336 translation route without resolving individual Fourier matrix entries.

The reusable point is that critical “quasilocality” is now a **positive frequency-mixing statement** with an especially cheap geometric test on the finite-boundary subsequence. The first obstruction target should be the aggregate half-cuff defect; only if it vanishes is it useful to resolve surviving even-offset/fixed-physical-separation mass.

This remains separate from physical concentration of a completed reference packet. Translation compatibility does not by itself localize a packet in space, because spatial cutoffs need not commute with `Q`.

**Boundary.** PF-337--PF-338 give necessary conditions, not sufficiency. PF-338 is restricted to the finite-boundary subsequence and fixed physical low band; even-offset mass and other translation defects can still survive after the half-cuff cross block vanishes. A successful commutator still does not establish the final low/high correlation estimate or reference-packet concentration.
