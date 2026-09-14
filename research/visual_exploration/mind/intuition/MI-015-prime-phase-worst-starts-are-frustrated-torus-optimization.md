# MI-015 — Prime-phase worst starts are constant-factor equivalent to the full correlation SDP

**Evidence level:** exact finite-dimensional reduction from VIS-213, exact holonomy and fractional cycle-packing certificates from VIS-214--VIS-215, normalized magnetic-ground-state certificate from VIS-216, exact relaxation lower bound from VIS-217, prime-graph asymptotics in VIS-218, destination pricing in VIS-219, universal simple-cycle packing ceiling in [VIS-220](../../findings/VIS-220-simple-cycle-packing-universal-envelope-ceiling.md), exact SDP hierarchy/stress certification in [VIS-221](../../findings/VIS-221-sdp-stress-certificate-retains-torus-interactions.md), and the classical complex symmetric-Grothendieck comparison specialized in [VIS-222](../../findings/VIS-222-symmetric-grothendieck-constant-factor-sdp-torus-equivalence.md). No prime-specific asymptotic SDP estimate, recurrence-time theorem or RH consequence is claimed.

For fixed `y,H`, VIS-213 identifies the worst start exactly with the unit-modulus quadratic optimum

`M_abs(A_(y,H)) = max_(|z_p|=1) |z^*A_(y,H)z|`.

Kronecker density settles equality of the one-parameter supremum with this finite torus optimum; it does not determine its size or the time required to approach a near-maximizer.

VIS-214 identifies cycle holonomy as the gauge-invariant obstruction to exact coefficient-envelope attainment. VIS-215 turns that obstruction into weighted fractional cycle-packing certificates. VIS-216 adds a normalized magnetic-Laplacian relaxation. VIS-217--VIS-218 prove that this spectral certificate misses Haar-RMS scale by a diverging factor in the strictly subcritical prime regime, and VIS-219--VIS-220 show that simple-cycle packing also remains on the coefficient-envelope scale.

VIS-221 moves to the full correlation SDP

`U_abs(A)=max_(X>=0, diag(X)=1) |Tr(A X)|`.

The old magnetic certificate is one restricted degree-proportional dual stress inside this SDP. A stationary torus candidate `z` with

`S_z = Diag(conj(z_i)(Az)_i) - A >= 0`

is a certified global maximizer and gives rank-one SDP tightness; conversely an optimal rank-one SDP solution has this stress certificate.

VIS-222 removes the remaining objective-scale ambiguity. Friedland--Lim's complex symmetric Grothendieck inequality identifies `U_abs` and `M_abs` with the corresponding symmetric Grothendieck seminorms and gives the dimension-free comparison

`M_abs(A) <= U_abs(A) <= K_gamma^C M_abs(A)`,

with `K_gamma^C <= 8/pi - 1 < 1.547`.

Therefore high rank can obstruct exact optimizer recovery but **cannot create an unbounded multiplicative relaxation gap in the objective value**. For the canonical prime matrices,

`U_abs/K_gamma^C <= sup_T |M_v(y;H,T)-1| <= U_abs`.

After normalization by the exact Haar scale `sqrt(R_v)`, boundedness or divergence of the SDP ratio is equivalent to boundedness or divergence of the exact torus/worst-start ratio. The live static problem is therefore simply to determine the asymptotic scale of `U_abs(A_(y,H))/sqrt(R_v(y,H))`. If it is `O(1)`, the exact worst-start amplitude is at RMS scale; if it diverges, the exact worst-start amplitude diverges relative to RMS as well, up to the same universal constant.

Rank-one stress remains useful for exact finite optimizers and values, but it is no longer required for asymptotic scale transfer. Likewise, failure of the magnetic or cycle certificates says nothing by itself about the SDP scale, while a large **optimal** SDP value now has direct lower-bound content for the exact torus optimum.

**Boundary.** VIS-222 does not determine the prime-specific SDP scale, SDP rank, exact finite relaxation gap, maximizing phase assignment or one-parameter access time. The symmetric-Grothendieck comparison is multiplicative and static; quantitative recurrence along the prime-log orbit remains a separate simultaneous-Diophantine problem.