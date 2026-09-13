# MI-023 — Blindness survives rowwise; normalization and aggregation are the expensive steps

**Evidence level:** proved for the current flat Christoffel source by [MC-273](../../findings/MC-273-christoffel-negative-witness-homogeneous-collapse.md)--[MC-277](../../findings/MC-277-christoffel-endpoint-margin-conditioning.md). No signed arithmetic cancellation theorem or blind-support exclusion is claimed.

MC-273 gives an exact rowwise simplification after any negative lower-prime witness, and MC-275 shows that using **all** such witnesses simultaneously is cheap. With `b(x)` the number of negative coordinates,

`U_m(x)=b(x)g_m(x)=1/2[(k-m)e_m-(m+1)e_(m+1)]`,

so overlap itself costs only one extra Walsh/source degree. MC-274 shows that selecting witnesses atom by atom can still be expensive, but first-witness search is not intrinsically required.

The first obstruction is normalization. Exact normalization to one unit per nonblind row reconstructs Boolean OR and has full degree `k`; uniform approximation costs `Theta(sqrt(k log(1/epsilon)))` on the generic cube. MC-276 closes the natural distributional relaxation: if a degree-`m` selector is forced to vanish at the blind point, its L2 classification loss subtracts the blind mass exactly. On the arithmetic shell,

`empirical L2 error = (E_(m,y)(t)-A_y(t))/C`.

Distributional normalization is therefore cheap precisely because its objective is allowed to forget the target atom.

MC-277 identifies what survives before that loss. For the normalized Christoffel scalar `P_m=g_m/Z_m`, the blind point has value `1`, every nonblind point has value at most

`h=binom(k-1,m)/Z_m`,

and one-negative vectors attain `h`. The exact rowwise gap is

`delta_(k,m)=1-h = 2 sum_(s=0)^(m-1) binom(k-1,s)/Z_m ~ 2m/k`.

A scalar decoder is uniformly robust to additive error exactly below `delta_(k,m)/2`, and its optimal Lipschitz condition number is `1/delta_(k,m)`. At the support-matched arithmetic scale this margin is of order `log y log log y/y`, while a single target-row mass is exponentially smaller in `log y log log y`. Hence the low-depth row representation has **not** erased the blind bit. The difficult one-exception problem is created when `C` row identities are aggregated and the exceptional provenance is discarded.

The unresolved object is still the signed linear residual, but its role is now more precise. A successful theorem must either control each relevant Christoffel scalar to its natural `delta_(k,m)` margin before aggregation, or prove signed cross-row cancellation while retaining enough information that an integer blind contribution cannot be hidden by the nonblind rows. Replacing the row scalar by another generic classifier is not the missing step.

The reusable distinction is **representation / conditioning / normalization / aggregation**. A representation may encode the exact bit with a shrinking margin; a stable decoder then costs the reciprocal margin; a normalization may delete the bit from its objective; and an aggregate may make one exceptional row invisible even when every row is individually decodable. These losses should not be conflated.

**Boundary.** The margin theorem is deterministic on the full Boolean cube and is not arithmetic specificity. It does not show that the actual row scalars can be estimated to the required accuracy, and it does not control the aggregate signed phase. The cube approximate-degree obstruction remains relevant to polynomial normalization, while the localized arithmetic cross-row theorem remains open.
