# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price retained information jointly with the admissible source class

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`, `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`, `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`, `MI-052-finite-positivity-must-be-gauge-invariant-to-track-zero-geometry`.

The fidelity results separate exact discriminator survival from finite observation, source freedom, conditioning and source-category rigidity. AF-406 shows why the representation must be named: finite coefficient-sequence Pólya-frequency positivity can change under an exponential tilt that preserves the entire zero divisor, whereas the normalized translation-kernel Toda hierarchy is invariant under the corresponding affine exponential profile gauge. AF-407 adds that the native bilateral-Laplace convergence half-plane of the Euler-log profile is zero-free; the nontrivial zeta divisor enters only after meromorphic continuation. Source identification, representation gauge, native analytic domain, admissible continuation and zero selection are therefore separate gates.

## Treat determinant order, source position and derivative depth as separate scaling coordinates

**Linked intuitions:** `MI-043-support-scale-interaction-components-bound-effective-relational-arity` through `MI-055-derivative-depth-is-a-second-left-tail-scaling-coordinate`.

AF-403--AF-405 reduce fixed-order strict translation positivity to the complete confluent flag and the Toda recursion. AF-408--AF-410 make the first possible order-five failure compact: with `A_4=4q-(log R_4)''`, one has `A_4>0` for `t<=-14` and `t>=4`.

AF-411--AF-412 then show that every **fixed** confluent order is eventually positive in both tails, so any escaping negative sequence must have order tending to infinity. AF-413 locates the first nontrivial left-tail diagonal at `m e^t=Theta(1)`. AF-414 shows that fixed excess partition sectors survive there with alternating Plancherel weights, and AF-415 resums the complete exceptional-`1` double-block sector to the positive Cauchy factor `exp(-c^2/(4pi^2))`.

AF-416 closes the remaining fixed-shift diagonal loopholes. For `m=n+3` and `e^t=c/n`, the **full** normalized determinant converges locally uniformly on compact `c>0` intervals to the same positive Cauchy exponential. Exponent sets omitting `1`, one-singular-block sectors and the zero-singular-block sector are negligible at that scale. Thus `n e^t=Theta(1)` is a genuine competition scale but not a fixed-shift sign obstruction. Any large-order left-tail failure must leave every compact `n e^t` corridor or introduce another moving parameter.

AF-417 identifies derivative depth as that extra parameter: for fixed excess degree `d`, `s_n/n -> sigma` multiplies the limiting Cauchy coefficient by `e^(sigma d)`. AF-418 shows that this fixed-degree compression is not uniform over the complete partition ensemble. For each fixed-width full-height rectangle `lambda=(r^n)`, with `a=c^2/(4pi^2)`,

`(1/n) log C_(n,r) = r((s_n/n)-2) log n + r log a - (s_n/n) log(r!) + o(1)`.

Hence every such rectangle is superexponentially negligible for `sigma<2`, while for `sigma>2` it diverges in absolute value for every fixed `a>0`; no AF-415-style absolute domination can control the full tail there. At the critical ratio `sigma=2`, the coarse variable `s_n/n` is itself insufficient: if `tau_n=((s_n/n)-2)log n -> tau`, then `(C_(n,r))^(1/n) -> e^(r tau)a^r/(r!)^2`. In particular, for `s_n=2n` the single column `(1^n)` already grows exponentially when `c>2pi`.

The live question is therefore regime-dependent. For `sigma<2`, can one prove a shape-uniform absolute majorant over the complete partition family and then recheck the omitted determinant sectors? For `sigma>=2`, any survival of the fixed-degree candidate `exp(-e^sigma c^2/(4pi^2))` must come from a genuinely signed global cancellation or resummation mechanism; fixed-degree convergence and absolute Schur domination cannot establish it. At `sigma=2`, any such statement must track at least the finer critical variable `tau_n`, because AF-418 proves that growing sectors retain information erased by the limit `s_n/n -> 2`.

## Match physical locality to source-density and certificate scales

AF-400--AF-402 remain the locality gate. Ordinary regular variation is insufficient when the physical wall shrinks; current short-interval input gives all-prime-start control for `h_N=p_N^(-beta)` with `beta<13/30` and a density-one route for every fixed `beta<13/15`. These are technology boundaries of the source theorem, not intrinsic detector constants.

A useful continuation must therefore declare the physical sampling wall, confluent order, derivative depth when it moves, and the source theorem used to populate that wall. Uniformity in one of these coordinates cannot be silently promoted to uniformity in the others, and no conclusion about zero geometry follows without an independent continuation/selection theorem.