# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price retained information jointly with the admissible source class

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`, `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`, `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`, `MI-052-finite-positivity-must-be-gauge-invariant-to-track-zero-geometry`.

The fidelity results separate exact discriminator survival from finite observation, source freedom, conditioning and source-category rigidity. AF-406 shows why the representation must be named: finite coefficient-sequence Pólya-frequency positivity can change under an exponential tilt that preserves the entire zero divisor, whereas the normalized translation-kernel Toda hierarchy is invariant under the corresponding affine exponential profile gauge. AF-407 adds that the native bilateral-Laplace convergence half-plane of the Euler-log profile is zero-free; the nontrivial zeta divisor enters only after meromorphic continuation. Source identification, representation gauge, native analytic domain, admissible continuation and zero selection are therefore separate gates.

## Move from fixed-order tail closure to the increasing-order diagonal

**Linked intuitions:** `MI-043-support-scale-interaction-components-bound-effective-relational-arity` through `MI-054-signed-plancherel-sectors-make-reciprocal-order-tail-genuinely-nonuniform`.

AF-403--AF-405 reduce fixed-order strict translation positivity to the complete confluent flag and the Toda recursion. For the Euler-log kernel the flag is strictly positive through order four, so the first possible failure is at order five. AF-408--AF-410 made that first gate effective: with `A_4=4q-(log R_4)''`, one has `A_4>0` for `t<=-14` and for `t>=4`; the order-five problem is therefore compact on `[-14,4]`.

AF-411--AF-412 change the larger frontier. The first-harmonic factorization on the right and the logarithmic-germ expansion on the left extend beyond `m=5`: **for every fixed confluent order `m`, `H_m(t)` is eventually positive in both tails**. Consequently any sequence of negative determinants with `|t|->infinity` must also have `m->infinity`. Escaping-tail failure is no longer a fixed-order phenomenon.

AF-413 identifies the first nontrivial scale of that variable-order problem on the left. The exact leading coefficient of the left-tail determinant has Barnes-`G`/zeta structure and its root-normalized size is asymptotic to `m e^t/(pi e^(3/2))`, so the natural diagonal is `m e^t=Theta(1)`.

AF-414 proves that this is a **genuine competition scale**, not merely a dimensional balance of the leading term. Inside the same double-rank-two Cauchy--Binet sector, every fixed excess partition `lambda` has a nonzero diagonal limit, with sign `(-1)^|lambda|` and Plancherel/hook weighting. The first competitor is already opposite-signed and remains order one relative to the AF-412 leading monomial. Summing each fixed excess degree gives the coefficients of the formal exponential `exp(-c^2/(4pi^2))`, but no uniform summation over growing partition degree is yet justified.

The accepted clue `CLUE-left-tail-diagonal-order-drift-scale` therefore now asks a sharper question. Control the growing partition tail, exponent families omitting the exceptional exponent `1`, and determinant sectors using fewer than two singular-block entries on `x=c/n`; only then can the full diagonal determinant asymptotic or sign be decided. A fixed-degree Plancherel limit is not a full determinant theorem.

The fixed-order and variable-order questions should remain separate. Certifying `A_4>0` on `[-14,4]` would move the first bad order above five, but it would not address the diagonal `m->infinity`, `e^t->0` regime. Conversely, a diagonal obstruction would not invalidate the fixed-order tail theorems.

## Match physical locality to source-density and certificate scales

AF-400--AF-402 remain the locality gate. Ordinary regular variation is insufficient when the physical wall shrinks; current short-interval input gives all-prime-start control for `h_N=p_N^(-beta)` with `beta<13/30` and a density-one route for every fixed `beta<13/15`. These are technology boundaries of the source theorem, not intrinsic detector constants.

A useful continuation must therefore declare three scales independently: the physical sampling wall, the confluent order, and the source theorem used to populate that wall. The new tail results make this especially important: fixed-order positivity can be uniform in `t` outside a compact set while the first unresolved behavior migrates to an order-dependent spatial scale. No conclusion about zero geometry should be transferred from that migration unless the representation supplies an independent continuation/selection theorem.
