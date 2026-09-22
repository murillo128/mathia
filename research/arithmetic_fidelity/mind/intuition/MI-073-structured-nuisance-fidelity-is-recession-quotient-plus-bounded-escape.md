# MI-073 — Structured nuisance fidelity is recession quotient plus bounded escape

**Evidence level:** exact finite-dimensional convex-geometry synthesis from [AF-491](../../findings/AF-491-bounded-nuisance-sets-restore-depth-through-difference-set-modulus.md) and [AF-492](../../findings/AF-492-convex-nuisance-recession-quotient-bounded-residual.md), sharpening the linear-nuisance quotient of MI-070--MI-072.

Nuisance geometry has two mathematically different parts. For a bounded nuisance set `K`, distinguishability of a displacement `delta s` is governed exactly by its distance from the difference set `K-K`. The nuisance can mask only a bounded amount of motion, so sufficiently deep motion eventually escapes. In particular, bounded unknown amplitude restores an absolute-depth law after a finite crossover even though unrestricted amplitude removes common depth completely.

For a closed convex symmetric nuisance set `C`, AF-492 identifies the general decomposition. Its recession cone `V=rec(C)` is a linear subspace, and after quotienting by `V` the residual set `B=q(C)` is bounded. The exact identity

`dist_Y(x,C)=dist_(Y/V)(q(x),B)`

shows that permanent invisibility is carried only by recession directions. If `a=dist(s,V)>0`, the separation modulus grows linearly in `delta a` up to the bounded residual radius; if `s in V`, the displacement remains invisible at every depth.

This gives a sharper fidelity ledger than either raw observation depth or nuisance dimension. **First quotient the directions in which nuisance can drift without bound; only then price the bounded residual freedom.** A moving window helps only through the component transverse to the recession space. Sample count, absolute location and nominal parameter depth are not resources until this quotient has been taken.

The principle also clarifies why compact and linear nuisance models behave differently without contradiction. Compact nuisance has trivial recession and therefore cannot erase arbitrarily large displacement; a linear nuisance space is pure recession and can erase its own directions forever. Intermediate convex nuisance classes interpolate between those cases through the pair `(rec(C), q(C))`.

**Boundary.** AF-491--AF-492 are finite-dimensional deterministic results for the stated bounded or closed convex symmetric nuisance classes. They do not classify nonconvex, stochastic or infinite-dimensional nuisance, do not provide uniform conditioning for deep arithmetic sources, and do not identify a rational-prime discriminator. Arithmetic provenance remains a separate gate: the quotient geometry determines what the observation can resolve, not whether the resolved feature is specific to the rational primes.