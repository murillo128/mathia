# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price retained information jointly with the admissible source class

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`, `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`, `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`, `MI-052-finite-positivity-must-be-gauge-invariant-to-track-zero-geometry`.

The fidelity results separate exact discriminator survival from finite observation, source freedom, conditioning and source-category rigidity. AF-406 shows why the representation must be named: finite coefficient-sequence Pólya-frequency positivity can change under an exponential tilt that preserves the entire zero divisor, whereas the normalized translation-kernel Toda hierarchy is invariant under the corresponding affine exponential profile gauge. AF-407 adds that the native bilateral-Laplace convergence half-plane of the Euler-log profile is zero-free; the nontrivial zeta divisor enters only after meromorphic continuation. Source identification, representation gauge, native analytic domain, admissible continuation and zero selection are therefore separate gates.

## Resolve the packet-level tuned square-transition fibers of the critical derivative window

**Linked intuitions:** `MI-043-support-scale-interaction-components-bound-effective-relational-arity` through `MI-055-derivative-depth-is-a-second-left-tail-scaling-coordinate`.

AF-403--AF-405 reduce fixed-order strict translation positivity to the complete confluent flag and the Toda recursion. AF-408--AF-410 make the first possible order-five failure compact, while AF-411--AF-416 show that every fixed confluent order is eventually positive in both tails and close the full fixed-shift left-tail determinant on the `e^t~1/n` diagonal.

AF-417 identifies derivative depth as a second moving coordinate: fixed partition sectors see `s_n/n->sigma` by renormalizing the Cauchy parameter by `e^sigma`. AF-418 shows that growing full-height partitions detect the finer critical window `tau_n=((s_n/n)-2)log n`, and AF-419 proves that `limsup s_n/n<2` is completely controlled by a shape-uniform absolute majorant.

AF-420 then identifies the joint critical coordinate

`b_n(a)=a n^(s_n/n-2)=a e^(tau_n)`, with `a=c^2/(4pi^2)`.

For `b<1`, the complete exceptional-`1` sector remains absolutely resummable to the fixed-degree exponential. AF-421 resolves the signed finite-window organization beyond that boundary. If `b_n->b in (0,infinity)`, the exponentially leading partition families are full-column packets around `(r^n)` with rates

`L_r(b)=b^r/(r!)^2`.

Away from `b=m^2`, one packet with `r=floor(sqrt(b))` dominates, so every nonsquare superthreshold `b>1` gives genuine signed divergence rather than hidden cancellation. At each square transition `b=m^2`, exactly the adjacent packets `r=m-1,m` tie exponentially.

AF-422 resolves the next rectangle scale. With `s_n=2n+d_n`, `d_n=o(n)`, and `b_n->m^2`, define

`Xi_(n,m)=log n+n log(b_n/m^2)-d_n log m`.

The adjacent rectangular packet ratio is `F_(n,m)=K_m exp(Xi_(n,m))(1+o(1))`, with explicit `K_m>0`. Even `n` cannot cancel because the packet signs agree. For odd `n`, leading rectangular cancellation is possible only when `Xi_(n,m)->-log K_m`; the exact square path is untuned.

AF-423 now resolves the first complete-packet correction that was previously the live interface. If `G_(n,r)` denotes the residual Schur--Cauchy factor around the `r`-column rectangle, then

`log(G_(n,m)/G_(n,m-1)) = 2 a e^2/n + o(1/n)`.

Thus `F_(n,m)->1` is still insufficient. The complete adjacent ratio obeys

`log Q_(n,m)=log F_(n,m)+2 a e^2/n+o(1/n)`,

so first packet-level cancellation on the odd square fiber additionally requires

`n log F_(n,m) -> -2 a e^2`.

For `m>=2`, any surviving order-`1/n` mismatch is only polynomially smaller than an exponentially growing tied saddle and still diverges exponentially. The finite-window frontier has therefore moved one scale deeper: under the new inverse-`n` tuning, derive the next term of the complete packet ratio together with the matching finer expansion of `F_(n,m)`, and compare the resulting residual against the lower saddle packets. AF-423 does not show that this stronger tuning is sufficient for boundedness or recovery of the fixed-partition exponential.

The genuinely supercritical regime `s_n/n>2`, where `b_n->infinity`, remains a separate moving-saddle problem and should not be extrapolated from the finite-window hierarchy.

## Match physical locality to source-density and certificate scales

AF-400--AF-402 remain the locality gate. Ordinary regular variation is insufficient when the physical wall shrinks; current short-interval input gives all-prime-start control for `h_N=p_N^(-beta)` with `beta<13/30` and a density-one route for every fixed `beta<13/15`. These are technology boundaries of the source theorem, not intrinsic detector constants.

A useful continuation must therefore declare the physical sampling wall, confluent order, derivative depth when it moves, the critical amplitude coordinate when relevant, and the source theorem used to populate that wall. Uniformity in one coordinate cannot be silently promoted to uniformity in the others, and no conclusion about zero geometry follows without an independent continuation/selection theorem.