# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price retained information jointly with the admissible source class

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`, `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`, `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`, `MI-052-finite-positivity-must-be-gauge-invariant-to-track-zero-geometry`.

The fidelity results separate exact discriminator survival from finite observation, source freedom, conditioning and source-category rigidity. AF-406 shows why the representation must be named: finite coefficient-sequence Pólya-frequency positivity can change under an exponential tilt that preserves the entire zero divisor, whereas the normalized translation-kernel Toda hierarchy is invariant under the corresponding affine exponential-profile gauge. AF-407 adds that the native bilateral-Laplace convergence half-plane of the Euler-log profile is zero-free; the nontrivial zeta divisor enters only after meromorphic continuation. Source identification, representation gauge, native analytic domain, admissible continuation and zero selection are therefore separate gates.

## Resolve square-transition cancellation beyond the explicit first detuning coordinate

**Linked intuitions:** `MI-043-support-scale-interaction-components-bound-effective-relational-arity` through `MI-055-derivative-depth-is-a-second-left-tail-scaling-coordinate`.

AF-417--AF-420 show that derivative depth is an independent moving coordinate. In the critical window `s_n=2n+d_n`, `d_n=o(n)`, source amplitude and derivative depth combine through

`b_n(a)=a n^(d_n/n)`.

AF-421 resolves the finite-window signed organization into full-column packets with exponential rates `L_r(b)=b^r/(r!)^2`. Away from square values `b=m^2`, one packet dominates and every nonsquare superthreshold `b>1` genuinely diverges. At `b=m^2`, exactly the adjacent packets `r=m-1,m` tie and a nested cancellation problem begins.

AF-422 identifies the rectangle-scale coordinate

`Xi_(n,m)=log n+n log(b_n/m^2)-d_n log m`,

with adjacent rectangle ratio `F_(n,m)=K_m exp(Xi_(n,m))(1+o(1))`. AF-423 then shows that rectangle balance is still too coarse: the complete residual packets contribute a deterministic inverse-`n` drift, so first complete-packet cancellation requires `n log F_(n,m)->-2ae^2` on the odd square fiber.

AF-424 makes that condition explicit in the original square-fiber coordinates. Writing `alpha_n=d_n/n`, it proves

`log F_(n,m)=Xi_(n,m)+log K_m+m alpha_n+[-m^2+m-1-(m^2/2)alpha_n]/n+O(n^-2)`

and

`log(G_(n,m)/G_(n,m-1))=a e^(2+alpha_n)(2+alpha_n)/n+O(n^-2)`.

Hence, with `Omega_(n,m)=Xi_(n,m)+log K_m+m alpha_n`, the first complete cancellation condition is equivalently

`n(Xi_(n,m)+log K_m)+m d_n -> m^2-m+1-2ae^2`.

The new retained coordinate is the derivative-offset term `m alpha_n`. When `a!=m^2`, the square condition normally makes it order `1/log n`, so replacing `alpha_n` by its limit zero before expanding loses a correction larger than `1/n`. AF-424 also proves that the first shape-sensitive content correction cancels only after the complete Schur packet is summed by partition conjugation; this is a derived cancellation, not an assumption.

The live finite-window problem is now one scale deeper. For `m>=2`, satisfying the displayed condition removes only the first polynomial mismatch while the common saddle still grows exponentially. Determine whether the next complete-packet term already forbids admissible tuning, or whether polynomial cancellation can continue until a lower-saddle, tall-column or other beyond-all-orders residual becomes load-bearing. The exact square path, parity, admissible behavior of `d_n`, and the distinction between packetwise and complete-family cancellation must remain explicit throughout.

The genuinely supercritical regime `s_n/n>2`, where `b_n->infinity`, remains a separate moving-saddle problem and should not be extrapolated from the fixed-square hierarchy.

## Match physical locality to source-density and certificate scales

AF-400--AF-402 remain the locality gate. Ordinary regular variation is insufficient when the physical wall shrinks; current short-interval input gives all-prime-start control for `h_N=p_N^(-beta)` with `beta<13/30` and a density-one route for every fixed `beta<13/15`. These are technology boundaries of the source theorem, not intrinsic detector constants.

A useful continuation must therefore declare the physical sampling wall, confluent order, derivative depth when it moves, the critical amplitude coordinate when relevant, and the source theorem used to populate that wall. Uniformity in one coordinate cannot be silently promoted to uniformity in the others, and no conclusion about zero geometry follows without an independent continuation or selection theorem.
