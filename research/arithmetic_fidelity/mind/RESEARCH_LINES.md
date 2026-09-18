# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price retained information jointly with the admissible source class

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`, `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`, `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`, `MI-052-finite-positivity-must-be-gauge-invariant-to-track-zero-geometry`.

The fidelity results separate exact discriminator survival from finite observation, source freedom, conditioning and source-category rigidity. Recovering `zeta` inside a rigid source class can identify the analytic object without selecting its nontrivial zeros, while small observations can become complete only after the admissible source fibre has already been restricted enough. Any useful compression must therefore state the source class and retained analytic layer before counting coordinates.

AF-406 sharpens the quotient test while separating two positivity representations that must not be conflated. For `xi_1(z)=xi(sqrt(z)+1/2)`, Katkova's finite-order theorem gives, for every fixed `m`, sufficiently large `n` with `e^{nz}xi_1(z) in PF_m`, while multiplication by `e^{nz}` preserves the complete zero divisor. Fixed finite **coefficient-sequence** Pólya-frequency positivity therefore does not descend to the zero-divisor quotient.

The translation-kernel Toda hierarchy behaves differently under the corresponding affine exponential profile gauge. For `f(t)->e^{at+b}f(t)`, every translation determinant is multiplied only by a positive row/column factor, `H_r` scales by `e^{r(at+b)}`, and the normalized quantities `R_r=H_r/f^r` and `q=-(log f)''` are invariant. Thus AF-406 does not turn the order-five Toda gate into a gauge artifact. The correct fidelity rule is representation-specific: compute the gauge action on the exact positivity object before inferring anything about zero geometry.

AF-407 adds a second separation inside the same analytic representation. For the affine-tilted Euler-log profile the bilateral Laplace transform is zero-free throughout its genuine convergence half-plane; nontrivial zeta zeros enter only through meromorphic continuation beyond that wall. The offset of those continued zeros from the convergence wall is gauge-invariant. All-order Pólya-frequency theory can exploit them because Schoenberg supplies a reciprocal-entire continuation theorem, but finite-order translation positivity has no such continuation principle for free. Native transform data, admissible continuation, and zero selection must therefore be priced separately.

## Match physical locality to source-density and confluent-certificate scales

**Linked intuitions:** `MI-043-support-scale-interaction-components-bound-effective-relational-arity` through `MI-053-first-harmonic-perturbation-makes-the-order-five-right-tail-effective`.

AF-387--AF-394 identify the smooth order-three translation-kernel structure. For a positive `C^4` profile, the local analytic `TN_3` condition is controlled by logarithmic curvature `q=-(log f)''`; under the shrinking solid hierarchy the remaining global datum is connectedness of `{q>0}`. AF-395--AF-399 then show that a fixed successor stencil can miss that global topology and that physical logarithmic reach, not raw successor count, is the invariant resource.

AF-400 proves that ordinary regular variation is insufficient when the physical wall itself shrinks. AF-401 supplies an all-prime-start conversion from uniform short-interval PNT: for `h_N=p_N^(-beta)` with `beta<13/30`, `B_N(h_N)~N h_N` for every sufficiently large prime index. AF-402 gives a distinct density-one route: exceptional-set inertia plus Brun--Titchmarsh packing transfers an almost-all ambient theorem to relative density one of prime starts, reaching every fixed `beta<13/15` with the current input.

AF-403 settles the placement question in the strict interior. For a smooth translation kernel, positivity of the complete initial confluent flag `H_m(t)>0` for every `m<=r` globalizes by extended-complete-Chebyshev theory to strict total positivity of every minor of order at most `r`. Thus fixed-order strict positivity needs no additional placement/topology datum once the whole flag is positive; topology re-enters on degenerate/nonstrict strata where a confluent minor vanishes.

AF-404 shows that the flag entries are recursively coupled by the classical Toda/Hankel identity

`H_(m+1) H_(m-1) = -H_m^2 (log H_m)''`.

With `q=-(log f)''` and `R_m=H_m/f^m`, the normalized recursion is `R_(m+1)R_(m-1)=R_m^2(mq-(log R_m)'')`. AF-405 closes the full-Euler order-four gate exactly: `H_1,...,H_4>0` everywhere, so the Euler-log translation kernel is strictly totally positive through order four. A finite signed source with at most three ordered sign changes cannot annihilate four distinct positive real samples, while AF-217 still forces failure at some later finite order. The first possible bad order is therefore at least five.

AF-408 localizes the order-five gate. Since `R_3,R_4>0`, write `A_4(t)=4q(t)-(log R_4(t))''`, so `H_5` has the sign of `A_4`. It proves `A_4(t)=(24/5)e^(2t)(1+o(1))` as `t->-infinity` and `A_4(t)=4e^t(1+o(1))` as `t->+infinity`.

AF-409 makes the right tail effective. With `x=e^t`, exact first-harmonic matrix factorization plus exponentially small higher-harmonic perturbation gives `A_4(t)>4e^t-3>0` whenever `e^t>=50`, hence throughout `t>=4`.

AF-410 now makes the left tail effective by a complementary singular-germ argument. Writing `u=-t`, `x=e^t`, and `f(t)=u+h(x)` with `h` analytic at the origin, multilinearity gives `H_4=u a(x)+b(x)`. The curvature numerator `N_4=(H_4')^2-H_4H_4''` is therefore quadratic in `u` with analytic coefficient germs. Explicit coefficient and Cauchy-remainder bounds show that the exponentially small `x=e^{-u}` beats every polynomial factor in `u`, yielding `N_4(t)>0.533e^{8t}>0` for every `t<=-14`. Since `H_4>0`, `A_4>0` there.

Both semi-infinite tails are therefore rigorously closed. The entire unresolved order-five sign problem is the compact interval `[-14,4]`. If `A_4>0` is certified there, AF-403/AF-404 globalize strict total positivity through order five and move the first possible bad order to at least six.

AF-409--AF-410 also give a reusable proof pattern: use an exactly invertible dominant harmonic where one term controls the tail, but separate an unbounded logarithmic singularity from its analytic remainder where the opposite tail is governed by a germ. There is no reason to force both asymptotic regimes into the same representation.

The live locality problem remains layered. First declare the physical wall, sampling regime and same-scale source theorem needed to inspect the profile. Then establish the confluent certificate on that physical source scale. Finally propagate one order at a time through the Toda/log-concavity gate. The `13/30` all-start and `13/15` density-one boundaries remain technology boundaries, not intrinsic detector constants.

## Separate source identification from zero selection

Hamburger-type rigidity can identify the zeta source without forcing RH. AF-406 strengthens the same separation while showing why the representation must be named: a finite coefficient positivity certificate may change while the entire zero divisor is held fixed, whereas the affine-exponential profile gauge leaves the normalized translation-kernel Toda hierarchy unchanged. AF-407 adds that even within one transform representation the native convergence domain can be zero-free while its meromorphic continuation carries the zeta divisor.

AF-408--AF-410 sharpen a different separation inside the finite translation hierarchy. The order-five sign is now explicitly settled outside `[-14,4]` without any appeal to continued zeta zeros. Tail positivity is therefore not evidence that the finite certificate has acquired access to the zero divisor; the remaining compact gate is still a finite translation-positivity problem for the Euler-log profile.

Future fidelity arguments must keep source identification, representation gauge, native analytic domain, admissible continuation, stable recovery, source-specific relational structure and zero selection as separate gates rather than transferring a gauge or zero verdict across them. A source-coordinate count or finite positivity level has mathematical meaning only after those choices are fixed.
