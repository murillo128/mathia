# MI-009 — Fixed-ratio visible Gram bands are source-silent after universal calibration

**Evidence level:** exact under the conditional source hypothesis `A=sum_(Re rho>1/2)(Re rho-1/2)<infinity` through NB-091. The statement covers every fixed multiplicative depth `q`, but not a growing ratio `q=q(R)`, the full radial charge, or genuinely inter-scale statistics.

NB-090 closed the complete dyadic terminal matrix: under `A<infinity`, its normalized determinant entropy is `O_A(1)`. NB-091 shows that widening the contiguous visible window to any other **fixed** ratio does not recover source sensitivity. For indices `m,...,R-1`, the raw Nyman innovation Gram has the exact determinant

`det K_tilde_(m,R)=m/R`.

For `m=ceil(R/q)` with fixed `q`, that raw Gram also has a uniform spectral floor `K_tilde_(R,q) >= c_q I`. After diagonal normalization its correlation entropy is

`-log det R_tilde_(R,q) = R Phi_q + O_q(1)`,

where `Phi_2=0` and `Phi_q>0` for every fixed `q>=3`. The apparent linear entropy gained by looking deeper is therefore already present in the raw `B=1` calibration; it is not arithmetic information from off-critical zeros.

The decisive comparison is the **centered excess** between the actual Blaschke-deflated Gram and that universal raw baseline. Causal inner order gives `K_(R,q)>=K_tilde_(R,q)`, while summable horizontal zero mass gives only `O_A,q(1)` total trace deformation on a fixed-ratio band. The spectral floor converts that trace budget into

`|-log det R_(R,q) + log det R_tilde_(R,q)| = O_A,q(1)`.

Thus all contiguous visible Gram determinants at fixed multiplicative depth are silent after calibration in the summable-horizontal-mass regime. The important lesson is stronger than “the terminal block is too small”: **fixed depth itself is the wrong asymptotic carrier**. Enlarging a window from `R/2` to `R/q` with constant `q` only exposes a universal correlation baseline.

What remains live is genuinely nonuniform in scale: prove that false-RH zero geometry forces a nonsummable effective horizontal statistic, let `q=q(R)->infinity` and control how the spectral/inverse/delay constants deteriorate, or construct an inter-scale statistic coupling different bands rather than taking one fixed-ratio determinant. Earlier indices help only if the depth actually grows or the statistic preserves coupling that a single band determinant discards.

**Boundary.** The `O_A,q(1)` calibration is conditional on `A<infinity` and keeps `q` fixed. It does not control any regime with `q=q(R)->infinity`, prove the radial charge bounded, prove false RH compatible with all Nyman obstructions, or imply RH.