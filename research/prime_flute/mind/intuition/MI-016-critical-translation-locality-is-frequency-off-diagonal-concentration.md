# MI-016 — Critical translation locality is a seam-normalized two-pant Fourier-coupling test

**Evidence level:** exact necessary-condition reduction from [PF-337](../../findings/PF-337-critical-translations-expose-the-frequency-off-diagonal-mass-of-the-normalized-pant-insertion.md)--[PF-340](../../findings/PF-340-symmetric-seam-parity-averages-two-adjacent-pant-self-responses.md). No two-pant no-cancellation theorem, raw energy lower bound, concentration theorem or direct-angle endpoint is claimed.

PF-336 reduces completed polar translation transport to the Hilbert--Schmidt commutator of the normalized pant insertion `K=Q_L^(-1/2) Lambda_LL Q_L^(-1/2)`. PF-337 diagonalizes the translation action:

`||[K,tau_t]||_(S2)^2 = sum_(j,k) 4 sin^2((xi_j-xi_k)t/2) |K_(jk)|^2`.

Averaging over the positive-length critical interval turns locality into a positive frequency-mixing statement. PF-338 then makes the finite-boundary subsequence much stronger: when `r_n=h_(n+1)/h_n -> 0`, the whole retained odd-offset sector is controlled by half-cuff translation `H_n=tau_(ell_n/2)`, so the route requires

`||[K_n,H_n]||_(S2)=o(1)`,

equivalently vanishing cross-parity mass `||P_(n,+)K_nP_(n,-)||_(S2)=o(1)`.

PF-339 removes most of the normalized-operator bookkeeping from the obstruction side. In the symmetric seam-parity channel, every fixed nonzero Fourier mode has seam energy

`q_(n,+)(k)=w_n(1+o(1))`,

with seam half-width `w_n asy P_n^(-1)`. Hence every fixed odd-offset raw symmetric-channel Fourier coupling must be `o(w_n)`.

PF-340 identifies the exact raw object hidden by that symmetric channel. After the simultaneous seam cut, the two faces of cuff module `n` belong to different adjacent pant cores. If `A_n^-` and `A_n^+` are the left and right self-DtN blocks, then

`Lambda_n^(+) = (A_n^- + A_n^+)/2`.

Thus a fixed Fourier matrix element and the two-mode energy witness are **averages of two adjacent pant responses**, not one-pant quantities. For the explicit half-cuff-exchanged cosine pair, if `Delta_n^-` and `Delta_n^+` are the left/right pant contrasts, then

`Delta_n^sym = (Delta_n^- + Delta_n^+)/2`.

The PF-336 translation route therefore requires

`Delta_n^- + Delta_n^+ = o(w_n)`

along the `r_n->0` subsequence. A right-pant lower bound `|Delta_n^+| gtrsim w_n` is not by itself a contradiction because the left pant can in principle cancel it. The arithmetic regime controls `h_(n+1)/h_n` and therefore the right pant geometry, but says nothing comparable about `h_(n-1)/h_n`.

The cheapest obstruction-side PDE theorem is consequently still scalar, but it is a **two-pant no-cancellation test**. It suffices to prove one of three mathematically distinct statements: the two contrasts have a common eventual sign, one dominates the other with a seam-scale lower bound, or their sum can be estimated directly and has nonzero seam-normalized limsup. Only if the actual sum is `o(w_n)` is it useful to return to higher odd modes, surviving even-offset/fixed-physical-separation mass, or a positive full-commutator estimate.

This remains separate from physical concentration of a completed reference packet. Translation compatibility does not localize a packet in space because spatial cutoffs need not commute with `Q`.

**Boundary.** PF-337--PF-340 give necessary conditions only. PF-340 proves the exact decomposition and exposes a cancellation channel; it does not assert that cancellation occurs or that the two pant contrasts have opposite signs. Zero twist aligns the test profiles but does not equalize the adjacent self-responses. A one-sided corridor calculation remains useful input, but it is not a completed falsifier until the other side is controlled.