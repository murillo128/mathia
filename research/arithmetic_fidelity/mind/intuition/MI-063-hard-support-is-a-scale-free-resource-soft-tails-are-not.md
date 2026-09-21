# MI-063 — Hard support is a scale-free Hilbert resource; a positive diffuse tail is not

**Evidence level:** exact metric-embedding synthesis from [AF-472](../../findings/AF-472-hard-support-budgets-have-exact-square-root-hilbert-distortion.md) and [AF-473](../../findings/AF-473-any-positive-tail-budget-destroys-scale-free-hilbert-fidelity.md). Sparse `ell^1`/`ell^2` comparison and Hamming-cube Hilbert distortion are classical; the line-specific content is the sharp source-relative boundary for TV fidelity.

For the full probability simplex with support size at most `s`, the original TV/`ell^1` metric has exact Hilbert distortion

`c_2(Delta_s(A),d_1)=sqrt(s)`.

The coordinate inclusion already attains this cost, while the paired-support `s`-cube supplies the matching lower bound. A hard support cap therefore changes the admissible secant geometry strongly enough to give a genuine positive fidelity theorem, with the resource priced exactly by the square root of simultaneous support complexity.

AF-473 shows that this positive result has a singular all-scales boundary. If one replaces the hard cap by the softer requirement that at least `1-epsilon` of the mass lie on `s` atoms, then every fixed `epsilon>0` on an infinite alphabet permits arbitrarily high-dimensional Hamming cubes inside the residual tail. Their absolute diameter is only `O(epsilon)`, but multiplicative distortion is scale invariant, so

`c_2(Delta_(s,epsilon)^soft(A),d_1)=infinity`.

Thus **small tail mass and small structural complexity are different resources**. A source restriction supports scale-free multiplicative Hilbert fidelity only if it controls the number of independently variable directions at every nonzero scale consumed by the downstream theorem. Approximate sparsity can still support additive-error, finite-resolution, anchored or otherwise scale-aware guarantees, but those are different fidelity claims and must price the ignored tail scale explicitly.

**Boundary.** The infinite-distortion statement uses an infinite ambient supply and the full soft-sparse family. Finite alphabets give finite quantitative cube bounds, and narrower arithmetic subclasses may forbid independent tail switches. The result does not supply a rational-prime discriminator or show that any physical arithmetic source has a fixed hard support budget; those remain source-specific obligations.