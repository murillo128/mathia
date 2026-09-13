# MI-017 — Zero-order shift transport needs BV structure, not merely spectral stability

**Evidence level:** supported by [PL-297](../../findings/PL-297-renormalized-hadamard-stress-hhalf-decoupling.md)--[PL-300](../../findings/PL-300-norm-small-perturbation-bv-shift-transport-obstruction.md). The needed source-structured compactness for the actual completed-Weil eigenbranch remains open.

PL-297 separates two singular resources in the small-order fractional control. The renormalized boundary stress has a finite nonzero limit while the zero extensions satisfy

`||E u_s||_(H^(1/2)) -> infinity`.

So a finite Hadamard stress does not imply the critical Fourier first moment used by routine absolute differentiation. PL-298 nevertheless shows that every fixed `s>0` has a `C^1` translation autocorrelation through physical-space `W^(1,1) cap L^infty` regularity.

PL-299 closes the `s->0+` passage for the pure principal branch by a different compactness currency. On the centered interval the positive principal eigenfunctions are even and decreasing; uniform `L^infty` control gives a uniform BV bound, while the small-order theory gives uniform convergence `u_s->u_0`. Uniform convergence plus uniform BV transports the derivative measures through convolution and yields

`C_s -> C_0 in C^1(R)`.

Thus failure of the half-Sobolev route is not evidence that the zero-order prime-shift derivative is singular. The load-bearing property is finite-measure derivative compactness, not an absolute Fourier first moment.

PL-300 shows just as sharply what does **not** imply that property. One can add self-adjoint perturbations of rank at most two with `||B_j||->0`, preserve a unique simple isolated ground branch and uniform convergence of the eigenstates to `u_0`, yet force both `TV(v_j)->infinity` and `|C'_(v_j)(h_0)|->infinity` at any prescribed nonzero lag. The high-frequency contamination is cheap in the logarithmic graph norm, `O(log K)`, but expensive in variation and shift derivative, `O(K)`.

Therefore Kato tracking, norm-resolvent convergence, a persistent spectral gap, bounded perturbation size and even uniform `C_0` convergence are not substitutes for the exact destination regularity. A proof for the completed-Weil branch must exploit a structural property of its **actual rational-prime/completion remainder** that the PL-300 finite-rank controls lack: for example a uniform BV mapping/coercive estimate, variation diminution, a source-specific order law, or a direct compactness equation for the derivative measures.

The reusable distinction is between Hilbert-space spectral stability and **stronger geometric regularity of the tracked state**. The former can identify which eigenvector is being followed while remaining completely insensitive to oscillations of tiny amplitude and huge variation. If the endpoint differentiates translations, the proof has to price precisely that stronger regularity.

**Boundary.** PL-300 is a matched adversarial perturbation, not a model of Suzuki's remainder, and does not prove that the actual completed-Weil branch loses BV. PL-299 remains a valid transport theorem once uniform BV/derivative-measure compactness is established. The independent sign gate and the renormalized Hadamard-trace problem are not resolved by either result.
