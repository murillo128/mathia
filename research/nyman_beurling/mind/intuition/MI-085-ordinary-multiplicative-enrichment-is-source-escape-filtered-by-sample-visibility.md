# MI-085 — Ordinary multiplicative enrichment is a subblock of pre-existing sample-visible tail

**Evidence level:** exact canonical finite-section identities from [NB-297](../../findings/NB-297-projected-dilation-escape-gives-baseline-free-ordinary-enrichment-certificate.md) and [NB-298](../../findings/NB-298-projected-dilation-escape-is-a-parseval-subblock-of-finite-section-excess.md), following the baseline obstruction in NB-296.

Let `U=V_(n-1,Z)` be an old Blaschke-deflated Nyman section, `S=S_m` the canonical dilation and `V^+=V_(mn-1,Z)`. The projected dilated copy

`R_(m,n,Z)=(U+SU)\ominus U = ran((I-P_U)SU)`

lies inside the genuine ordinary increment from `U` to `V^+`. Its first-free sampling Gram

`Xi_(m,n,Z)=L P_R L^*`

therefore gives a baseline-free positive certificate against the actual undilated old section. NB-298 sharpens where that certificate lives. In the closed quotient-source space, if `T=H\ominus U` is the full future source tail and

`E=L P_T L^*=K_infinity-K_(n-1,Z)`,

then `R subseteq T` and exactly

`E=Xi+Omega`, with `Omega>=0`.

Hence `0<=Xi<=E`: the projected dilation does not create a second source of ordinary coercivity. It selects a finite-dimensional subblock from the same future representer tail that already controls the ordinary finite-section excess.

Choose an isometric synthesis `E_U` onto `U`, set `F=(I-P_U)S E_U`, `Q=F^*F` and `Y=LF`. NB-297 gives `Xi=YQ^+Y^*`. NB-298 resolves the role of `Q` more sharply through the polar decomposition `F=JQ^(1/2)`:

`YQ^+Y^*=LJJ^*L^*=L P_R L^*`.

Thus the **nonzero magnitudes** of the principal-angle defect eigenvalues cancel after the escaping directions are normalized. Their kernel still controls which source directions escape, but beyond rank the quantitative sample mass is determined by the orientation of the normalized subspace `R` under `L`, not by how large the positive eigenvalues of `Q` are. A theorem that the dilation makes many large principal angles is therefore not by itself a first-free sampling theorem.

The target-side identity is equally exact. If `D_U=U cap ker L`, `R_U` is the minimum-norm right inverse of `L|_U`, and `N_R=(I-R_UL)R`, then

`(U+R) cap ker L = D_U direct_sum N_R`

orthogonally. For the old minimum-norm interpolant `h_U=R_U y`, the ordinary gain is

`C_U(y)-C_(U+R)(y)=||P_(N_R)h_U||^2`.

The full finite-section excess is `A_U(y)=||P_(D_infinity\ominus D_U)h_U||^2`, and `N_R subseteq D_infinity\ominus D_U`, so the dilation gain is exactly one Parseval subblock of the pre-existing excess and the remainder is another orthogonal nonnegative tail.

For a **fixed zero packet**, this closes the idea that a growing multiplicative dilation can rescue late finite sections. Since `||E_(n-1,Z)||->0`, NB-298 gives

`sup_(m>=2)||Xi_(m,n,Z)|| <= ||E_(n-1,Z)|| -> 0`,

and for every fixed datum `y` the corresponding ordinary gain is uniformly bounded by `A_(n-1,Z)(y)->0`. This remains true even though the source escape rank from NB-297 can stay macroscopic. Increasing `m` does not manufacture sample-visible mass after the entire future tail has already collapsed.

The live quantity is therefore a **moving-packet occupation fraction**, not source escape strength in isolation. On the support of `E`, define

`Theta_R=E^(+/2) Xi E^(+/2)`, so `0<=Theta_R<=P_(ran E)` and `Xi=E^(1/2) Theta_R E^(1/2)`.

A surviving Ford-scale theorem must show simultaneously that the moving packet leaves a nonvanishing target-relevant future tail `E` and that the normalized projected dilation escape occupies a nonnegligible part of that tail through `Theta_R` (or the equivalent nullspace Parseval block). Source rank, nonzero principal-angle magnitudes, multiplicative-band coercivity and determinant pressure cannot substitute for this occupation statement.

**Boundary.** NB-298 proves a fixed-packet uniform no-go and an exact subblock decomposition; it does not show that the moving Ford packet has `E->0`, that every moving `Theta_R` degenerates, or that the projected dilation captures no useful target mass before the fixed-packet limit. The cancellation of principal-angle magnitudes concerns the normalized block `YQ^+Y^*`; the kernel/rank of `Q` still matters. No RH consequence or moving-packet lower/upper bound is obtained.