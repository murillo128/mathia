# MI-024 — Dirichlet-gap tent variance has an explicit half-circle overlap formula

**Evidence level:** exact-derived calibration from [VIS-242](../../findings/VIS-242-dirichlet-gap-tent-variance-overlap-classes.md), sharpened by the complement-symmetry closure [VIS-243](../../findings/VIS-243-complement-symmetry-closes-cyclic-overlap-multiplicities.md), building on the fixed-count Dirichlet null of VIS-240 and endpoint-phase quotient of VIS-241.

Normalize the circle to length `1`, let cyclic gaps `X` have the symmetric `Dirichlet(alpha,...,alpha)` law, and let `S_(i,r)` be the mass of the oriented arc of `r` consecutive gaps starting at `i`. For the cut-averaged tent statistic the pair kernel obeys `q_u(s)=q_u(1-s)`.

VIS-243 uses that symmetry pointwise. Put `R_m={1,...,floor(m/2)}` and let `w_r=1`, except `w_(m/2)=1/2` when `m` is even. Then

`bar T = sum_(r in R_m) w_r sum_i q_u(S_(i,r))`.

For `r,s in R_m`, set `a=min(r,s)` and `b=max(r,s)`. Because `r+s<=m`, the number of cyclic displacements giving overlap size `k` is exactly

`N_(r,s,0)=m-r-s+1`,

`N_(r,s,a)=b-a+1`,

`N_(r,s,k)=2` for `1<=k<a`.

If `C_(r,s,k)=M_(r,s,k)-mu_r mu_s` denotes the low-dimensional Dirichlet covariance from VIS-242, then

`Var_G(bar T)=m sum_(r,s in R_m) w_r w_s[(m-r-s+1)C_(r,s,0)+(b-a+1)C_(r,s,a)+2 sum_(k=1)^(a-1) C_(r,s,k)]`.

Thus the null variance no longer contains an unresolved displacement sum. Complementary arc lengths disappear, every interior overlap size has multiplicity two, and each `M_(r,s,k)` still reduces by Dirichlet aggregation to at most four components. The probability-integral dimension and the deterministic combinatorics are both explicit.

At `alpha=1`, rotated symmetric Dirichlet gaps are exactly spacings of iid uniform circle points and the independent audit remains

`Var(bar T)=binom(m,2)[2u/3-4u^2/3+11u^3/15-u^4/9]`.

The substantive consequence is procedural but mathematical: once `alpha` and endpoint semantics are fixed independently, a prime residual cannot be blamed on unknown covariance or cyclic-displacement bookkeeping. Any residual is a separate source/point-process question.

**Boundary.** The half-circle reduction depends on the complement-symmetric endpoint-quotiented kernel and should not be transferred to oriented or endpoint-sensitive statistics. The Dirichlet family remains a chosen null rather than a theorem about prime gaps, and an anomaly against it is not an RH mechanism until it survives stronger controls and is connected back to the signed prime-phase channel.