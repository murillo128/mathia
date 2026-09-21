# MI-049 — Parity dilation moves exact-omission conditioning from support to paired coefficients

**Evidence level:** exact support-embedding synthesis from [FD-252](../../findings/FD-252-parity-dilation-embeds-arbitrary-divisor-conditioning-into-exact-omission-supports.md), interpreted with the weighted incidence inverse of FD-248 and the ordered-factorization ceiling of FD-251.

For every finite divisor support `D subset [1,N]`, parity dilation produces a genuine exact-omission response with omission set `E=2D` and increment support

`D' = supp(Delta Y) = 2D union (2D+1)`.

Every divisibility interval between embedded even nodes survives unchanged: `mu_(D')(2q,2d)=mu_D(q,d)`. Since the weights also satisfy `(2q)/(2d)=q/d`, the support norm obeys

`kappa(D') >= kappa(D)`.

Hence the bare support constraint `supp(Delta Y) subset E union (E+1)` cannot improve the worst-case power-law conditioning relative to arbitrary induced divisor supports, even with the same omission cardinality up to a constant dilation of the horizon. Any response-side improvement beyond FD-251 must use information that parity dilation does not preserve as free support data.

That missing information is coefficient-level. Isolated omissions force adjacent increments `Delta Y(2d)=+Y(2d)` and `Delta Y(2d+1)=-Y(2d)`; overlapping omissions telescope similarly. The large row defining `kappa(D')` is allowed to choose arbitrary signs and amplitudes and need not align with this paired subspace. The next relevant norm must therefore keep the linear map `Y|_E -> Delta Y` inside the weighted divisibility inversion instead of replacing it by free coordinates on `supp(Delta Y)`.

**Boundary.** FD-252 does not construct an exact omission whose paired amplitudes attain `kappa(D')`, does not invalidate the FD-251 coercive range, and says nothing about positivity, prime-reservoir capacity or squarefree source realization. It closes only support-combinatorial attempts to improve the response norm.