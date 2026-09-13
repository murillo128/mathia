# MI-023 — Generic witness normalization is either expensive or blind to the blind atom

**Evidence level:** proved for the current flat Christoffel source by [MC-273](../../findings/MC-273-christoffel-negative-witness-homogeneous-collapse.md), [MC-274](../../findings/MC-274-negative-witness-conditioning-fourier-depth-tax.md), [MC-275](../../findings/MC-275-witness-normalization-approximate-degree-barrier.md) and [MC-276](../../findings/MC-276-distributional-witness-normalization-christoffel-collapse.md). No signed arithmetic cancellation theorem or blind-support exclusion is claimed.

MC-273 gives an exact rowwise simplification after any negative lower-prime witness, and MC-275 shows that using **all** such witnesses simultaneously is cheap. With `b(x)` the number of negative coordinates,

`U_m(x)=b(x)g_m(x)=1/2[(k-m)e_m-(m+1)e_(m+1)]`,

so overlap itself costs only one extra Walsh/source degree. MC-274 shows that selecting witnesses atom by atom can still be expensive, but first-witness search is not intrinsically required.

The obstruction is normalization. Exact normalization to one unit per nonblind row reconstructs Boolean OR and has full degree `k`; uniform approximation costs `Theta(sqrt(k log(1/epsilon)))` on the generic cube. MC-276 now closes the most natural weaker escape. If a degree-`m` selector `Q` is constrained by `Q(x_*)=0` at the blind point and `P=1-Q`, then under any measure `rho` with blind mass `a`,

`||Q-NB||_(L2(rho))^2 = ||P||_(L2(rho))^2-a`.

Under the uniform cube the optimum is exactly the existing Christoffel kernel `P_m=g_m/Z_m`, with minimum error `1/Z_m-2^(-k)`. On the actual arithmetic shell,

`empirical L2 error = (E_(m,y)(t)-A_y(t))/C`.

Thus distributional least-squares normalization is cheap precisely because the loss **subtracts the blind mass one is trying to exclude**. It can be perfect when every sampled row is blind. This is not a softer route to the endpoint; it is an information-losing reformulation of the old positive Christoffel energy.

MC-276 also shows that support-respecting signed witness allocation is not the missing complexity. The radial optimizer factors as `Q_m(b)=b h_m(b)`, so signed weights `phi_i=n_i h_m(b)` have degree at most `m`, vanish when witness `i` is absent, and sum exactly to `Q_m`.

The unresolved object is therefore the **signed linear residual**, not another classifier:

`A_y(t)-L_(m,y)(t)=sum_T (Q_m(T)-NB(T))`,

where `L_(m,y)` uses source depth only `m`. A useful theorem must prevent nonblind arithmetic phase from cancelling an integer blind contribution, or control the uncentered Christoffel energy strongly enough to retain the atom. Pointwise OR approximation and L2 classification have now failed for opposite reasons: one is too expensive, the other deletes the target.

**Boundary.** The cube approximate-degree obstruction is worst-case; MC-276 does not compute the best polynomial for the empirical arithmetic measure. The independent-sign fluctuation scale is only a matched control, not arithmetic evidence. Signed cancellation on the localized Legendre shell remains open.