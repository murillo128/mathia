# MI-001 — Prime-specific spectral information lives in relative multi-gap geometry, not in an individual cuff

**Evidence level:** proved

## Core intuition

A distinguished cuff length is a faithful arithmetic encoding of one prime gap, but hyperbolically it is only the standard length parameter of a cylinder. Prime-specific spectral information appears only after **relative contrasts among several nearby cuffs/gaps** survive the universal local geometry and become genuine moduli of finite subsurfaces.

## Strongest justified claim

For the prime flute, every invariant depending only on a single cuff germ is a universal function of `ell_n`; the collar width is exactly the standard `w(ell_n)`, and microlocal wave/DtN/cylinder data near that cuff add no independent information. By contrast, for a finite prime pattern with gaps `d_i`, separating multi-gap geodesics satisfy exact cross-ratio laws such as

` sinh^2(L_k/4) = (d_1+...+d_{k-1})/d_k `,

so common divergence in the cuffs cancels and the remaining contrasts become moduli of a finite punctured-sphere tangent.

PF-032 and PF-037 kill the single-cuff interpretation. PF-029/PF-034 establish the finite cusp-side tangent. PF-047, PF-054 and PF-056 show that its small spectrum, weighted-path reduction and exact collar capacities depend on the relative gap profile. PF-074/PF-076 sharpen the first nontrivial case: for the four-punctured tangent, the unordered adjacent-gap contrast determines the global systole and exact Cheeger constant.

## Failure modes

Not every multi-gap observable is new: sojourn-time differences can merely reproduce a classical shear coordinate (PF-031), and the unmarked small spectrum of a longer weighted path is not inverse-unique in general (PF-048). The useful invariant must survive geometric quotienting without being a disguised coordinate readout.

## Status / novelty

The geometric identities and local-impossibility statements are exact. Spectral graph limits are classical machinery specialized to prime-derived moduli. Novelty, if any, lies in the composition from exact prime-circle cross-ratios to genuine spectral data.

## Falsification criterion

A canonical single-cuff spectral observable carrying information not determined by `ell_n` would falsify the first half. A proof that all finite prime-derived tangents of fixed topology are isospectral would falsify the positive half.

## Most informative next move

Prefer fixed-topology tangents where moduli vary and seek minimally marked spectral data that distinguish them.

## Lean-formalizable core

- Exact collar-width/cuff identity.
- Exact multi-gap cross-ratio-to-length formula.
- Algebraic conversion from cuff contrasts to gap ratios.
