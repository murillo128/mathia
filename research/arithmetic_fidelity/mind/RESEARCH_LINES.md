# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price retained information jointly with the admissible source class

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`, `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`, `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`, `MI-052-finite-positivity-must-be-gauge-invariant-to-track-zero-geometry`.

The fidelity results separate exact discriminator survival from finite observation, source freedom, conditioning and source-category rigidity. Recovering `zeta` inside a rigid source class can identify the analytic object without selecting its nontrivial zeros, while small observations can become complete only after the admissible source fibre has already been restricted enough. Any useful compression must therefore state the source class and retained analytic layer before counting coordinates.

AF-406 sharpens the quotient test while separating two positivity representations that must not be conflated. For `xi_1(z)=xi(sqrt(z)+1/2)`, Katkova's finite-order theorem gives, for every fixed `m`, sufficiently large `n` with `e^{nz}xi_1(z) in PF_m`, while multiplication by `e^{nz}` preserves the complete zero divisor. Fixed finite **coefficient-sequence** Pólya-frequency positivity therefore does not descend to the zero-divisor quotient.

The translation-kernel Toda hierarchy behaves differently under the corresponding affine exponential profile gauge. For `f(t)->e^{at+b}f(t)`, every translation determinant is multiplied only by a positive row/column factor, `H_r` scales by `e^{r(at+b)}`, and the normalized quantities `R_r=H_r/f^r` and `q=-(log f)''` are invariant. Thus AF-406 does not turn the order-five Toda gate into a gauge artifact. The correct fidelity rule is representation-specific: compute the gauge action on the exact positivity object before inferring anything about zero geometry.

## Match physical locality to source-density and confluent-certificate scales

**Linked intuitions:** `MI-043-support-scale-interaction-components-bound-effective-relational-arity` through `MI-052-finite-positivity-must-be-gauge-invariant-to-track-zero-geometry`.

AF-387--AF-394 identify the smooth order-three translation-kernel structure. For a positive `C^4` profile, the local analytic `TN_3` condition is controlled by logarithmic curvature `q=-(log f)''`; under the shrinking solid hierarchy the remaining global datum is connectedness of `{q>0}`. AF-395--AF-399 then show that a fixed successor stencil can miss that global topology and that physical logarithmic reach, not raw successor count, is the invariant resource.

AF-400 proves that ordinary regular variation is insufficient when the physical wall itself shrinks. AF-401 supplies an all-prime-start conversion from uniform short-interval PNT: for `h_N=p_N^(-beta)` with `beta<13/30`, `B_N(h_N)~N h_N` for every sufficiently large prime index. AF-402 gives a distinct density-one route: exceptional-set inertia plus Brun--Titchmarsh packing transfers an almost-all ambient theorem to relative density one of prime starts, reaching every fixed `beta<13/15` with the current input.

AF-403 settles the placement question in the strict interior. For a smooth translation kernel, positivity of the complete initial confluent flag `H_m(t)>0` for every `m<=r` globalizes by extended-complete-Chebyshev theory to strict total positivity of every minor of order at most `r`. Thus fixed-order strict positivity needs no additional placement/topology datum once the whole flag is positive; topology re-enters on degenerate/nonstrict strata where a confluent minor vanishes.

AF-404 shows that the flag entries are recursively coupled by the classical Toda/Hankel identity

`H_(m+1) H_(m-1) = -H_m^2 (log H_m)''`.

With `q=-(log f)''` and `R_m=H_m/f^m`, the normalized recursion is `R_(m+1)R_(m-1)=R_m^2(mq-(log R_m)'')`. AF-405 closes the full-Euler order-four gate exactly: `H_1,...,H_4>0` everywhere, so the Euler-log translation kernel is strictly totally positive through order four. A finite signed source with at most three ordered sign changes cannot annihilate four distinct positive real samples, while AF-217 still forces failure at some later finite order. The first possible bad order is therefore at least five.

The next local analytic frontier remains precise. Since `R_3,R_4>0`, order five is equivalent to `(log R_4)''<4q`; proving or refuting that scalar curvature inequality locates the next step of the finite-order hierarchy. AF-406 now removes one possible misinterpretation of this question: although coefficient `PF_m` can be manufactured along a zero-preserving exponential gauge, the normalized translation-kernel Toda quantities are invariant under affine exponential profile tilt. A positive fifth Toda gate would therefore be genuine gauge-invariant kernel structure under this natural freedom, though still not by itself a zero-selection theorem.

The live locality problem remains layered. First declare the physical wall, sampling regime and same-scale source theorem needed to inspect the profile. Then establish the confluent certificate on that physical source scale. Finally propagate one order at a time through the Toda/log-concavity gate. The `13/30` all-start and `13/15` density-one boundaries remain technology boundaries, not intrinsic detector constants; coefficient-PF gauge sensitivity and translation-kernel Toda invariance are separate representation facts.

## Separate source identification from zero selection

Hamburger-type rigidity can identify the zeta source without forcing RH. AF-406 strengthens the same separation while showing why the representation must be named: a finite coefficient positivity certificate may change while the entire zero divisor is held fixed, whereas the affine-exponential profile gauge leaves the normalized translation-kernel Toda hierarchy unchanged. Future fidelity arguments must therefore keep source identification, representation gauge, stable recovery, source-specific relational structure and zero selection as separate gates rather than transferring a gauge verdict from one positivity model to another.

For every proposed destination theorem state separately the observed data, admissible source/tail class, retained analytic layer, relation order, intrinsic physical source coordinate, sampling set, same-scale density theorem, exceptional-set transfer if needed, conditioning, residual gauge, positivity representation and final zero/sign discriminator. A source-coordinate count or finite positivity level has mathematical meaning only after those choices are fixed.
