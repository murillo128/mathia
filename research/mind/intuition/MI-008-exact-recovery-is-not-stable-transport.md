# MI-008 — Exact recovery, quotient geometry, source-normalized response, and accumulated local loss are different resources

**Evidence level:** supported by the specified inverse, sampling, timing, and scalar propagation/Green models through AF-289 and PF-304; no common universal condition number, target modulus, or full mixed-response theorem is claimed.

Dirichlet acquisition separates phase fibers from coupling. AF-279--AF-281 classify one-lattice aliasing, failure of separate resonant marginals, and exact recovery from genuinely joint mixed samples. AF-282--AF-285 then price the known-prefix `log2/log3` repair: joint phase spacing is `Theta(1/N)`, stable mixed degree is `Theta(N)`, and raw acquisition can be reduced to `Theta(N)` observations.

AF-286--AF-287 add timing provenance. A common clock-origin offset factors exactly as a coefficient gauge `b -> D_tau b`, while independent rowwise jitter is a genuine operator perturbation. A bounded-condition unweighted `O(N)` raw subframe removes the apparent extra `sqrt(N)` penalty, leaving the same sharp ambient coefficient-recovery scale `Theta(1/log N)`.

AF-288 shows that this coefficient scale is not automatically a target scale. The common gauge is vertical translation `F(s)->F(s+i tau)`, so it preserves every zero real part and therefore the RH yes/no predicate. For horizontal zero geometry, the clock origin should be quotiented rather than reconstructed. Exact source anchors can instead identify the gauge without providing a global robust inverse modulus.

AF-289 makes the quotient quantitative for an arbitrary rowwise timing vector. With

\[
r(\tau)=\inf_\sigma\max_j|\tau_j-\sigma|
=\frac{\operatorname{osc}(\tau)}2,
\]

one has the exact decomposition of the perturbed frame into a common coefficient gauge plus residual differential jitter. For condition number at most `K`,

\[
\inf_\sigma
\frac{\|\widehat b-G_\sigma b\|_2}{\|b\|_2}
\le K\left(e^{r(\tau)\log N}-1\right).
\]

Thus an arbitrarily large common timing center is free for a common-clock-invariant target, while the differential diameter remains a real stability resource. The target still needs its own modulus on the quotient before coefficient-orbit control becomes a target theorem.

Prime Flute supplies a complementary source-normalized phenomenon. PF-297--PF-302 show that scalar directional losses accumulate in the intrinsic seam coordinate and force scalar round-trip extinction. PF-303 then identifies the finite scalar Robin killing vector `d` as the exact Green-potential currency:

\[
H_N\mathbf1=d,
\qquad
G_Nd=\mathbf1.
\]

PF-304 strengthens this to a full norm statement. With `D_N=diag(d)` and

\[
P_N=G_ND_N,
\]

`P_N` is a reversible Markov kernel, hence

\[
\|G_Nf\|_{\ell^p(d)}
\le
\|D_N^{-1}f\|_{\ell^p(d)},
\qquad1\le p\le\infty.
\]

The absence of a depth-uniform scalar spectral gap is therefore not itself a forced-response obstruction. Once the source is measured in the killing currency, the scalar Green response is nonamplifying even while local returns approach conservativity. The unresolved burden is the physical map from the true `P/H` forcing and reassembly into these source-adapted norms.

The cross-line lesson is concrete: **price perturbation and response only after removing exact nuisance symmetries and identifying the source measure against which the operator is normalized**. AF-289 replaces ambient timing radius by distance to the common-clock orbit. PF-304 replaces a bare spectral-gap demand by a killing-weighted source/response norm. In both cases a worst-case ambient cost can disappear because it lies in the wrong geometry; what remains is the residual direction actually seen by the target or source.

This does not imply that quotienting or reweighting always helps. Differential jitter survives the AF gauge, and nonconstant `P/H` modes may escape the PF scalar killing currency. The gain is a sharper question: identify the exact residual geometry before asking for a bound.

**Boundary.** AF-289 is finite known-support and coefficient-orbit `ell^2`; it supplies no target-specific quotient modulus. PF-303--PF-304 are finite scalar constant-mode statements and do not prove that the complete boundary response factors through their Markov normalization. Neither mechanism transfers automatically to another measurement, source, or global response category.