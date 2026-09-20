# MI-056 — Bounded Hilbert marks pay a sharp square-root sparse-mixture TV tariff

**Evidence level:** exact synthesis from [AF-456](../../findings/AF-456-full-simplex-tv-fidelity-requires-l1-geometry.md) and [AF-457](../../findings/AF-457-bounded-hilbert-marks-have-sharp-sqrt-k-sparse-mixture-tv-fidelity.md). The statement is geometric and barycentric; no prime-specific source-law conclusion is claimed.

AF-456 separates atomwise distinguishability from mixture stability. On a countably infinite alphabet, uniform TV fidelity for the full probability simplex is exactly bounded-below control on `l1_0`, so a target must contain an isomorphic copy of `l1`. Hilbert space can therefore keep infinitely many atoms uniformly separated while still having zero full-simplex TV gain.

AF-457 makes the finite-complexity Hilbert boundary sharp. Let `phi:A->H` be any bounded Hilbert marking with `sup_a ||phi(a)||<=M`, extend it barycentrically to probability laws, and restrict to laws supported on at most `k` atoms. With the convention `||mu-nu||_TV=||mu-nu||_1`, its worst-case conditioning modulus satisfies

`kappa_k^TV(phi) <= M/sqrt(2k)`.

The orthogonal one-hot marking `phi(a)=M e_a` attains equality. Hence the familiar `k^{-1/2}` degradation is not a weakness of one-hot coding: it is the optimal worst-case law for every bounded Hilbert-valued barycentric representation on an infinite alphabet. More Hilbert dimensions, better atomwise separation and orthogonality cannot improve the exponent or constant.

The source-law qualifier is load-bearing. The upper bound is witnessed by balanced disjoint sparse mixtures available in the unrestricted `k`-sparse simplex. A physical arithmetic source may forbid those secants or couple their coefficients. Therefore AF-457 does not prove that an arithmetic model must realize the sharp obstruction; it says exactly what must be excluded before a stronger Hilbert fidelity claim is possible.

The reusable audit is: **first identify the completed admissible secants, then compare their mixture complexity with the target geometry**. If the source contains growing balanced sparse secants of the AF-457 type, bounded Hilbert TV conditioning necessarily decays at the square-root rate. If it does not, the mathematically meaningful resource is the source constraint that removes those secants, not extra Hilbert dimension.

**Boundary.** The theorem is for bounded affine/barycentric Hilbert observations and worst-case TV on sparse probability mixtures. Non-Hilbert targets, nonlinear observations, different source metrics, or stricter arithmetic mixture laws are different categories and require separate lower-gain analysis.
