# MI-011 — Finite-start dephasing has a worst-spacing baseline and a sharper weighted-collision currency

**Evidence level:** exact deterministic weighted-Hilbert and same-sign gap-fiber reduction through VIS-197, literature-backed sieve closures VIS-198--VIS-199, and the uniform finite-window baseline [VIS-212](../../findings/VIS-212-prime-ratio-spacing-quantifies-finite-start-dephasing.md). Pointwise worst-start cancellation, the critical-scale transition and optimal finite-window length remain open.

VIS-192--VIS-195 reduce deterministic finite-start dephasing to the coefficient-weighted local-spacing resource `D_v` and make `D_v=o(y^2)` equivalent to vanishing taper-energy mass on every fixed normalized top-scale collision family. VIS-196 removes the opposite-sign branch at subquadratic cost and writes each dangerous same-sign collision as a one-parameter affine prime-gap fiber. VIS-197 shows that local congruence geometry is not the power-scale obstruction: outside an explicit finite conductor, the four-form system has only polylogarithmic local-product inflation.

VIS-198 closes every polynomially growing strictly subcritical corridor, while VIS-199 pushes the weighted route deep into the subpolynomial regime by retaining all four primality conditions and moving the sieve/taper split. These results show that global minimum spacing is often too pessimistic: coefficient mass on near-collisions, not the closest formal pair alone, controls the useful averaging cost.

VIS-212 supplies the complementary unconditional baseline. The symmetric prime-ratio frequencies `+/- log(q/p)` are globally separated by at least `y^-2`, because two distinct reduced ratios satisfy `|qr-ps|>=1`. Montgomery--Vaughan therefore gives, uniformly in the position `T_0` of the averaging interval,

`L^(-1) int_(T_0)^(T_0+L) |M_v(y;H,T)-1|^2 dT = R_v(y,H)[1+O(y^2/L)]`.

Hence `L>=c y^2` already yields `O(R_v)` mean square in **every** sliding start window, and when `H->infinity` this gives density-one cancellation inside every such window. Infinite Cesaro averaging is not essential.

The two conclusions use different currencies and should not be conflated. The quadratic scale comes from worst deterministic separation of bounded rational ratios and ignores coefficient weights. The `D_v` theory can beat that baseline by proving that dangerous small determinants carry little normalized mass, but it requires more arithmetic input and currently has its own slow-horizon restrictions. Neither statement is pointwise in `T`.

The next finite-window theorem should therefore quantify the weighted distribution of small cross-determinants `|qr-ps|` strongly enough to replace the crude `delta^-1<=y^2` cost by the coefficient-weighted scale relevant to the taper. Separately, a worst-start theorem must rule out or classify rare coherent phases that can survive every mean-square statement. Shortening the averaging interval and proving pointwise cancellation are not the same problem.

**Boundary.** VIS-212 proves a sufficient quadratic window, not necessity. VIS-198--VIS-199 do not establish arbitrary-slow or critical-scale control, and none of these results excludes exceptional individual starts. The exact pair-difference cancellation taxonomy is independent of this averaging-horizon question.
