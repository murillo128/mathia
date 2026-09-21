# MI-064 — Primorial primitive boundary support is exactly the rough-number wheel

**Evidence level:** exact support-level synthesis from [PC-388](../../findings/PC-388-primorial-boundary-windows-are-rough-number-sieves.md), extending the scalar primitive-shell classicalization in PC-386--PC-387. Primorial wheels, rough numbers, Buchstab asymptotics, and the least-prime-factor threshold are classical; the line-specific content is the exact identification of the retained prime-circle boundary support and the resulting no-go for support-only novelty.

For the primorial shell `N_x=prod_(p<=x) p`, the primitive boundary indices

`R_x(H)={1<=a<=H:(a,N_x)=1}`

are exactly `1` together with the `x`-rough integers. Before the first rough composite enters,

`H<p_+(x)^2  =>  R_x(H)={1} union {p:x<p<=H, p prime}`.

Thus the first nontrivial boundary scale is `H asymp log N_x`, while the first rough composite appears only around `H asymp (log N_x)^2`. Beyond that threshold the support passes through the ordinary rough almost-prime hierarchy governed by the classical sieve.

Retaining the point cloud instead of scalarizing does preserve fine arithmetic information, but at support level that information is already the primorial wheel. On polylogarithmic windows a line-forced chord kernel also locally Euclideanizes, so a matrix restricted to the surviving points is simply a difference kernel evaluated on the classical prime/rough-number set. Prime detection caused only by which vertices survive is therefore information inserted by the primitive mask, not a new geometric discriminator.

The non-scalar branch is not closed by this observation. A forced interaction law, cross-level transport, phase-sensitive operator, or other invariant may still contain mathematics not reconstructible from the support set alone. The burden is now explicit: subtract the rough-number support contribution first and exhibit the additional source-forced interaction that survives.

**Boundary.** The exact rough-number description uses primorial shells and a boundary window anchored in exponent coordinates. It does not classify arbitrary squarefree shells, nonlocal selections, or spectra of all operators on the retained points. The conclusion is only that support selection itself is classical sieve data.