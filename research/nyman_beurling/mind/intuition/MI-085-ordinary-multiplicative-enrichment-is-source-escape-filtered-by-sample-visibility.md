# MI-085 — Ordinary multiplicative enrichment is source escape filtered by sample visibility

**Evidence level:** exact canonical finite-section identities from [NB-297](../../findings/NB-297-projected-dilation-escape-gives-baseline-free-ordinary-enrichment-certificate.md), following the baseline obstruction in NB-296.

Let `U=V_(n-1,Z)` be an old Blaschke-deflated Nyman section, `S=S_m` the canonical dilation and `V^+=V_(mn-1,Z)`. The projected dilated copy

`R_(m,n,Z)=(U+SU)\ominus U = ran((I-P_U)SU)`

lies inside the genuine ordinary increment from `U` to `V^+`. Its first-free sampling Gram

`Xi_(m,n,Z)=L P_R L^*`

therefore satisfies `0 <= Xi <= K_(mn-1,Z)-K_(n-1,Z)`. Unlike the multiplicative band of NB-292--NB-295, this is a baseline-free certificate against the actual undilated old section.

Choose an isometric synthesis `E` onto `U` and write `X=LE`, `T=E^*SE`, `Q=I-T^*T` and `Y=DX-XT`. NB-297 gives the exact factorization

`Xi = Y Q^+ Y^*`.

Here `Q=E^*S^*(I-P_U)SE` measures source escape, while `Y=L(I-P_U)SE` measures how much of that escape remains visible to the first-free zero sampler. The canonical source has abundant escape: `rank Q=n-1-q_(m,n)` with `q_(m,n)=max(1,floor((n-1)/m))`, so every `m>=2` ejects at least about half the old source dimensions. But that rank statement alone says nothing about ordinary approximation gain because the entire escaping block may lie in the sampling kernel, equivalently `Y=0` and `Xi=0`.

The reusable principle is that **source-side principal-angle motion is only a potential resource; the ordinary destination sees the intertwining defect**. The correct positive object is not `Q` or its rank by itself but the sample-weighted Schur block `YQ^+Y^*`, and target gain is then priced relative to the old Gram. This exactly diagnoses the saturation control of NB-296: the dilated-baseline band can be strongly coercive while `U^perp` is sample-null, making the ordinary escape certificate vanish.

For a target datum `y`, NB-297 turns the same block into a genuine ordinary decrement lower bound after whitening by `K_(n-1,Z)`. Thus a closing theorem no longer needs to invent a bridge from the multiplicative dilation to the ordinary nested sections; that bridge exists canonically. It must instead prove quantitative lower control of `YQ^+Y^*` in the actual moving Ford regime, or at least enough target-aligned mass for the relevant datum.

**Boundary.** Large rank of `Q` does not imply a principal-angle lower bound, large rank of `Y`, or target occupation. NB-297 gives an exact positive sub-block of ordinary enrichment, not an equality with the whole increment and not an asymptotic rate. Any uniform coercivity claim must still be proved for the actual Nyman packet rather than inferred from dimension.