# MI-028 — Uniform state boundedness collapses the first-prime gate

**Evidence level:** conditional exact synthesis from [PL-329](../../findings/PL-329-source-amplitude-gate-for-first-prime-reflection.md) through [PL-336](../../findings/PL-336-uniform-linfty-closes-first-prime-source-gate.md).

PL-329 expresses the moving first-prime sign problem through the endpoint-source amplitude `S_delta`, the selected critical coefficient `C_delta`, and the half-log scale `L_delta`. PL-336 shows that these apparently separate quantities become controlled together under one concrete state-space hypothesis: a uniform `L^infty` bound on the normalized simple odd eigenbranch as `delta->0`.

Assuming

`sup_(0<=delta<=delta_0) ||u_delta||_infty < infinity`,

the exact completed-Weil eigen-equation gives `S_delta=O(1)`. The source equation then supplies the family-uniform half-log boundary envelope and the uniform endpoint remainder required by PL-329 and PL-332. Norm-resolvent/`L^2` transport identifies `C_delta->C_0`, while PL-335's odd reflected Hopf mechanism gives `C_0>0` on the lowest odd threshold branch.

Consequently

`(1+S_delta)/(|C_delta| sqrt(L_delta)) -> 0`,

which is exactly the PL-329 source-amplitude gate. Under the uniform state bound, the favorable first-prime reflected sign therefore follows without separately estimating a growing source norm and endpoint coefficient.

The reusable lesson is that a moving-boundary forcing problem can sometimes be reduced to a norm of the **state that generates the forcing**, rather than controlled by independent source/remainder estimates. When the equation maps a uniform state bound directly to a uniform source bound and the limiting state has a noncollapsed boundary coefficient, the moving-scale tariff can collapse to one concentration estimate.

**Boundary.** No result here proves the required uniform `L^infty` bound. Existing `L^2`, graph-topology and every fixed logarithmic Fourier-seminorm control do not supply it, and the compressed first-prime translation is precisely where concentration could occur. The statement is a conditional reduction, not an RH proof, a branch-existence theorem, or a claim of a positivity-preserving completed semigroup.