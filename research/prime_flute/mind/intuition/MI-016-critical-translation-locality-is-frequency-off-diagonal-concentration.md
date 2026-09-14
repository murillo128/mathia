# MI-016 — Critical translation locality is a seam-normalized raw Fourier-coupling test

**Evidence level:** exact necessary-condition reduction from [PF-337](../../findings/PF-337-critical-translations-expose-the-frequency-off-diagonal-mass-of-the-normalized-pant-insertion.md)--[PF-339](../../findings/PF-339-half-cuff-invariance-forces-raw-symmetric-pant-fourier-coupling-below-seam-width.md). No raw pant-energy lower bound, concentration theorem or direct-angle endpoint is claimed.

PF-336 reduces completed polar translation transport to the Hilbert--Schmidt commutator of the normalized pant insertion `K=Q_L^(-1/2) Lambda_LL Q_L^(-1/2)`. PF-337 diagonalizes the translation action:

`||[K,tau_t]||_(S2)^2 = sum_(j,k) 4 sin^2((xi_j-xi_k)t/2) |K_(jk)|^2`.

Averaging over the positive-length critical interval turns locality into a positive frequency-mixing statement. PF-338 then makes the finite-boundary subsequence much stronger: when `r_n=h_(n+1)/h_n -> 0`, the whole retained odd-offset sector is controlled by half-cuff translation `H_n=tau_(ell_n/2)`, so the route requires

`||[K_n,H_n]||_(S2)=o(1)`,

equivalently vanishing cross-parity mass `||P_(n,+)K_nP_(n,-)||_(S2)=o(1)`.

PF-339 removes most of the normalized-operator bookkeeping from the obstruction side. In the symmetric seam-parity channel, PF-326 gives for every fixed nonzero Fourier mode

`q_(n,+)(k)=w_n(1+o(1))`,

with seam half-width `w_n asy P_n^(-1)`. Hence for every fixed odd-offset pair `j-k`,

`(K_n)_(jk)=lambda_(n;jk)^(+)/w_n (1+o(1))`.

The half-cuff gate therefore forces the **raw** pant DtN coupling

`lambda_(n;jk)^(+) = o(w_n) = o(P_n^(-1))`.

This is a much cheaper falsifier than estimating a large matrix. The fixed pair of modes `1,2` already suffices: if their raw symmetric-channel coupling is merely comparable to seam width, the entire PF-336 translation route fails on the finite-boundary subsequence.

PF-339 also gives a basis-free two-mode witness. For explicit normalized cosine combinations `f_(n,+),f_(n,-)` exchanged by half-cuff translation, the route requires

`|E_n^(+)(f_(n,+))-E_n^(+)(f_(n,-))| = o(w_n)`.

The pair is geometrically aligned with the common-perpendicular corridor: one profile is nonzero at the corridor foot while its half-cuff mate vanishes quadratically there. But corridor asymmetry is only motivation until the **total** one-cusp-pant energy contrast is bounded below at seam-width scale.

The live PDE problem is therefore scalar and quantitative: prove that one explicit symmetric-parity two-mode energy contrast has nonzero limsup after division by `w_n`. Only if this test is `o(w_n)` is it useful to return to higher odd modes, surviving even-offset/fixed-physical-separation mass, or a positive full-commutator estimate.

This remains separate from physical concentration of a completed reference packet. Translation compatibility does not localize a packet in space because spatial cutoffs need not commute with `Q`.

**Boundary.** PF-337--PF-339 give necessary conditions only. PF-338--PF-339 apply on the source-realized finite-boundary subsequence and retained physical-low space. PF-339 does not prove the raw energy contrast is large; the unresolved calculation is exactly whether the actual one-cusp-pant DtN response can satisfy the unusually small `o(w_n)` threshold.