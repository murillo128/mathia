# MI-003 — Analytic nonmasking is weaker than absolute convolution inversion

**Evidence level:** supported by MC-007--MC-008 and exact Euler-factor calculations

## Core intuition

When a multiplicative comparator differs from Möbius only beyond the prime layer, coefficientwise absolute inversion can be much stronger than what RH sensitivity actually needs. The relevant analytic gate is whether the comparator transfer factor can **mask a hypothetical zeta zero in the open critical half-strip**, not whether its Dirichlet inverse has absolutely summable coefficients at every exponent above `1/2`.

This distinction creates a legitimate comparator architecture, but not a free RH proof: one still needs an independently established square-root-scale bound for the comparator, and the nonmasking statement must be proved without importing the zeta zero divisor through analytic continuation.

## Strongest justified principle

MC-007 classifies all `1`-bounded multiplicative comparators with the exact prime values `g(p)=-1=mu(p)`. Writing `g=mu*h`, the transfer kernel `h` has no prime layer and is supported on squarefull integers; its absolute Dirichlet series converges for `Re s>1/2`. Hence every Mertens exponent `alpha>1/2` transfers forward to every such comparator.

For the reverse absolute transfer, all large-prime local factors are automatically zero-free in the relevant disk: only the Euler factors at `2` and `3` can obstruct absolute inversion above `1/2`. This already shows that changing higher prime-power values does not create a new large-prime threshold.

MC-008 then separates absolute inversion from analytic sensitivity sharply. An explicit comparator `g_2` differs from Möbius only through the `2`-adic prime-power factor. Its inverse transfer coefficients grow exponentially, so the absolute reverse threshold is `1`; nevertheless

`RH <=> sum_{n<=x} g_2(n)=O_epsilon(x^(1/2+epsilon))`.

Its Dirichlet series satisfies `F_2(s)=A_2(s)/zeta(s)` with

`A_2(s)=(1-2^(1-s))/(1-2^(-s))^2`,

and `A_2` is holomorphic and zero-free throughout `1/2<Re s<1`. Thus a square-root bound for the comparator forces holomorphy of `F_2` there and excludes any zeta zero in that half-strip even though coefficientwise inversion is unavailable. The obstruction to absolute inversion lives on the boundary `Re s=1`, not at hypothetical nontrivial zeros.

## What remains possible

A serious comparator program should search for multiplicative functions whose partial sums admit an independently provable improvement and whose exact transfer factor is holomorphic and zero-free on the critical half-strip for arithmetic reasons visible before any zeta continuation is invoked. Signed or oscillatory reverse transforms, finite local modifications, and other squarefull kernels are admissible if the nonmasking theorem is source-independent.

The key adversarial test is circularity. Writing a transfer factor as a continued expression involving `zeta'/zeta`, `1/zeta`, or another object whose poles/zeros are the target does not establish nonmasking. The zero-free property of the auxiliary factor must come from its own local or elementary analytic structure.

## Status / novelty

The convolution factorization, multiplication-operator algebra, Dirichlet-series continuation from summatory bounds, and finite Euler-factor calculations are classical. The persisted synthesis is the comparator gate: **absolute invertibility is a sufficient but nonessential transfer condition; analytic nonmasking is the weaker condition relevant to zero detection**.

## Falsification criterion

Construct a same-prime comparator whose transfer factor is holomorphic and zero-free on `1/2<Re s<1` and whose summatory function has an independently proved RH-scale bound without already implying the corresponding Möbius estimate by a known route; or show that every such nonmasking comparator bound is automatically equivalent to an equally hard zeta-zero statement before any new arithmetic estimate enters.
