# MI-009 — Bidirectional scalar survival is killed by accumulated pant loss

**Evidence level:** supported by the exact scalar pant decomposition PF-298, intrinsic prime-coordinate accumulation PF-299--PF-301, and the variational lower accumulation theorem PF-302; no full `P/H` mixed-response extinction theorem is claimed.

Each tight one-cusp pant has a constant-channel matrix

\[
M_n=c_n\begin{pmatrix}1&-1\\-1&1\end{pmatrix}
+\operatorname{diag}(\kappa_{n,L},\kappa_{n,R}),
\]

with directional relative killings `r_{n,\pm}=\kappa_{n,\pm}/c_n`. PF-298 shows each `r_{n,\pm}=O(s_n)`, so every individual pant is asymptotically almost conservative. PF-301 shows that one directional infinite product survives exactly when the corresponding bounded intrinsic attenuation density has finite `L^1` mass.

PF-302 supplies the missing lower accumulation law for the **sum of the two orientations**. A distance-cutoff trial bounds the antisymmetric pant energy by `E_{-,n}\lesssim L_n/s_n`, while the equal-sign energy has a uniform positive floor. Consequently

\[
r_{n,L}+r_{n,R}\gtrsim\frac{s_n}{L_n}.
\]

The exact ordered-prime mesh then gives

\[
\sum_{n\le M}\frac{s_n}{L_n}\gtrsim\log\log p_M-O(1),
\]

so

\[
\sum_n(r_{n,L}+r_{n,R})=\infty.
\]

Therefore the product of the two directional scalar transmissions vanishes. **Local near-conservativity does not imply global bidirectional survival when the small losses accumulate in the intrinsic source coordinate.** Arbitrary oscillation of the directional coefficients cannot make both scalar attenuation masses finite.

This is stronger than a generic statement that some local leakage exists, but weaker than a one-way theorem. The divergent mass may concentrate predominantly in one orientation; PF-302 proves only that at least one directional product vanishes and that scalar round trips are extinguished.

**Boundary.** The constant channel is not known to be invariant under the complete boundary Schur problem. Nonconstant modes can screen or redistribute scalar attenuation, and the actual source-weighted mixed Riesz response still requires the full `P/H` return/reassembly equation. PF-302 therefore closes a scalar escape hatch; it does not by itself prove the physical global response decays.