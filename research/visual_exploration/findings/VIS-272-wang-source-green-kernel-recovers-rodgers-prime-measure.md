# VIS-272 — Wang source diagonal is a Green potential of the Rodgers prime-power measure

## Claim

The source-scale mismatch isolated in `VIS-271` has an exact representation-level resolution, although not yet a theorem-level asymptotic transfer.

Biao Wang's short-interval explicit formula uses

`D_x(t)=sum_(n>=2) a_n(x)n^(-it)`

with

`a_n(x)=Lambda(n)/sqrt(n) min(n/x,x/n)`.

Introduce the logarithmic source coordinate

`q = log(x)/(2*pi)`

and, for every integer `n>=2`, the fixed frequency

`xi_n = log(n)/(2*pi)`.

Then exactly

`a_n(e^(2*pi*q)) = Lambda(n)/sqrt(n) exp(-2*pi |q-xi_n|)`.

Thus Wang's moving source profile becomes, in the `q` coordinate, a translation-invariant exponential kernel centered at the same fixed prime-power frequencies `xi_(p^m)=m log(p)/(2*pi)` that occur in the Rodgers lower-order carrier.

The bridge is stronger at the diagonal-energy level. Define

`A(q)=sum_(n>=2) a_n(e^(2*pi*q))^2`

and the positive prime-power atomic measure

`mu = sum_(p,m>=1) (log p)^2 p^(-m) delta_(m log(p)/(2*pi))`.

Since `Lambda(n)` vanishes away from prime powers,

`A(q)=int exp(-4*pi |q-xi|) dmu(xi)`.

The kernel is the one-dimensional Green kernel for `16*pi^2-d_q^2` up to normalization:

`(16*pi^2-d_q^2) exp(-4*pi|q-xi|)=8*pi delta_xi`

in the sense of distributions. Consequently

`mu = (16*pi^2-d_q^2)A/(8*pi)`.

Therefore the exact prime-power measure sampled by Rodgers' quadratic arithmetic term can be recovered from Wang's source **diagonal energy as a function of logarithmic source position** by one fixed second-order differential operator.

For a sufficiently smooth decaying test function `g`, the prime-power part of the Rodgers coefficient already audited in the preceding visual findings is

`C_2^pp(g)=-(1/(8*pi^4)) int g''(q) dmu(q)`.

Substituting the Green inversion gives the equivalent exact pairing

`C_2^pp(g)=-(1/(64*pi^5)) int A(q) [16*pi^2 g''(q)-g''''(q)] dq`.

So the Wang and Rodgers source descriptions are not intrinsically incompatible: their prime labels coincide after the natural logarithmic rescaling of Wang's source variable, and the Rodgers quadratic carrier is an explicit differential functional of the resulting Wang diagonal-energy field.

**Evidence/status:** `EXACT-DERIVED + REPRESENTATION/TRANSFORM BRIDGE + CLASSICAL GREEN-KERNEL INVERSION + NO-NOVELTY-CLAIM`.

This does **not** transfer Wang's short-interval asymptotic into Rodgers' lower-order coefficient. Wang's theorem is formulated on fixed `alpha` scales with `x=T^alpha`, whereas a fixed `q` neighborhood corresponds to `alpha=2*pi*q/log(T)` and therefore shrinks toward `0`. Uniform control on that moving test/source regime is an additional analytic requirement not supplied by the identity above.

## 1. The logarithmic source coordinate fixes the prime labels

Write `x=e^u`. Wang's coefficient becomes

`a_n(e^u)`
` = Lambda(n)/sqrt(n) min(exp(log n-u),exp(u-log n))`
` = Lambda(n)/sqrt(n) exp(-|u-log n|)`.

Now put

`q=u/(2*pi)`

and

`xi_n=log(n)/(2*pi)`.

Then

`|u-log n|=2*pi |q-xi_n|`,

so

`a_n(e^(2*pi*q))=Lambda(n)/sqrt(n) exp(-2*pi|q-xi_n|)`.

This is an exact change of variables, with no asymptotic approximation. The center attached to `n=p^m` is

`xi_(p^m)=m log(p)/(2*pi)`,

which is exactly the fixed prime-power frequency coordinate appearing in Rodgers' arithmetic sampler.

This clarifies the negative result in `VIS-271`. At fixed Wang parameter `alpha`, the logarithmic source position is

`q_T=alpha log(T)/(2*pi)`,

which drifts to infinity and therefore tracks growing prime powers. A fixed prime label `xi_p` is recovered only when

`alpha_T=log(p)/log(T)`.

The mismatch was therefore a mismatch between the fixed-`alpha` theorem scale and the fixed-`q` arithmetic scale, not a mismatch between the underlying source coordinates themselves.

## 2. Wang's diagonal energy is an exponential potential of the prime-power measure

Squaring the exact coefficient gives

`a_n(e^(2*pi*q))^2 = Lambda(n)^2/n * exp(-4*pi|q-xi_n|)`.

Hence

`A(q)=sum_(n>=2) Lambda(n)^2/n exp(-4*pi|q-xi_n|)`.

Because `Lambda(p^m)=log p` and `Lambda(n)=0` otherwise,

`A(q)=sum_(p,m>=1) (log p)^2 p^(-m) exp(-4*pi|q-m log(p)/(2*pi))`.

Introduce

`mu=sum_(p,m>=1) (log p)^2 p^(-m) delta_(m log(p)/(2*pi))`.

Then simply

`A(q)=int exp(-4*pi|q-xi|) dmu(xi)`.

The series is locally well behaved: on a compact `q` interval, the exponential kernel contributes an additional factor comparable to `n^(-2)` for sufficiently large `n`, so the prime-power tail converges absolutely there. Thus the following distributional differentiation can be performed locally without assigning an illicit pointwise derivative at the kernel cusps.

## 3. A second-order operator recovers the atomic measure exactly

For `a>0`, the elementary distribution identity

`(a^2-d_s^2) exp(-a|s|)=2a delta_0`

follows from the derivative jump at `s=0`. Taking `a=4*pi` and translating to each `xi` gives

`(16*pi^2-d_q^2) exp(-4*pi|q-xi|)=8*pi delta_xi`.

Applying this termwise in the distributional representation of `A` yields

`(16*pi^2-d_q^2)A=8*pi mu`,

or equivalently

`mu=(16*pi^2-d_q^2)A/(8*pi)`.

This is the exact representation bridge missing from `VIS-271`: the full fixed prime-power atomic measure is already encoded in Wang's diagonal coefficient field before any large-`T` averaging. The exponential source profile smooths that measure, and a fixed local differential operator inverts that smoothing distributionally.

The identity concerns the source coefficient geometry. It does not say that Wang's presently proved pair-correlation theorem observes `A(q)` with the uniform accuracy needed to apply this inverse operator on a fixed `q` scale.

## 4. Rodgers' quadratic carrier is a differential functional of the Wang diagonal

The Rodgers quadratic prime-power carrier established in the preceding visual chain has the form

`C_2^pp(g)`
` = -(1/(8*pi^4)) sum_(p,m>=1) (log p)^2 p^(-m) g''(m log(p)/(2*pi))`
` = -(1/(8*pi^4)) <mu,g''>`.

For a smooth test function with enough decay to justify the distributional pairing, substitute

`mu=(16*pi^2-d_q^2)A/(8*pi)`.

Since `16*pi^2-d_q^2` is formally self-adjoint,

`<mu,g''>`
` = (1/(8*pi)) <A,(16*pi^2-d_q^2)g''>`
` = (1/(8*pi)) int A(q)[16*pi^2 g''(q)-g''''(q)]dq`.

Therefore

`C_2^pp(g)`
` = -(1/(64*pi^5)) int A(q)[16*pi^2 g''(q)-g''''(q)]dq`.

This does not manufacture the Rodgers arithmetic term from a universal kernel. All arithmetic remains in `A`, equivalently in `mu`; the Green operator only supplies an exact dictionary between two representations of the same weighted prime-power atoms.

## 5. What this resolves and what it does not

`VIS-271` ruled out a naive identification of a fixed Wang `alpha` with a fixed Rodgers prime frequency. The present identity explains why: fixed `alpha` means

`q=alpha log(T)/(2*pi)`,

so the source center moves through the fixed `q`-axis as `T` grows. The correct comparison variable is `q`, not `alpha` itself.

At the coefficient level this completely aligns the source labels. At the theorem level, however, the difficult step remains. A fixed-width window around one Rodgers frequency `q=xi_p` becomes an `alpha` window of width `O(1/log T)` centered at `alpha_T=log(p)/log(T)`. Wang's current fixed-support asymptotic does not by itself provide the uniform shrinking-scale error control needed to resolve `A(q)`, differentiate it twice, or pair it against the fourth-order test functional above.

In particular, this finding does not establish that the lower-order Rodgers coefficient is present in Wang's short-interval statistic, does not improve Wang's `O(H)` remainder, does not prove a new pair-correlation asymptotic, and has no direct RH implication.

The concrete theorem-transfer question is now sharper: can Wang's explicit-formula/mean-square analysis be made uniform on `alpha=O(1/log T)` families strongly enough to recover a fixed-`q` functional of `A`, with an error stable under the Green inversion or its integrated adjoint form? If not, the exact representation bridge remains a useful explanation of why the two arithmetic formulas share atoms without yielding an asymptotic transfer.

## 6. Prior-art and novelty boundary

Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026), is the source of the coefficient

`a_n(x)=Lambda(n)/sqrt(n) min(n/x,x/n)`

and the fixed-`alpha` short-interval framework used in `VIS-271`. The present finding changes variables in that exact coefficient; it does not alter Wang's theorem or claim that Wang stated the `q`-space interpretation.

Brad Rodgers, **Macroscopic Pair Correlation of the Riemann Zeroes for Smooth Test Functions**, *Quarterly Journal of Mathematics* 64:4 (2013), 1197--1219, arXiv:1203.3275, is the source underlying the fixed prime-power lower-order carrier previously audited in the visual line. The present finding uses the already persisted coefficient identity and identifies its atomic measure with the Green inverse of Wang's diagonal source field.

A targeted literature search for this exact Wang-to-Rodgers logarithmic-source Green-kernel dictionary did not locate an existing statement. That is not a novelty proof: explicit-formula literature routinely relates zero statistics to weighted prime-power sums, and the identity

`(a^2-d^2/dq^2)e^(-a|q|)=2a delta_0`

is classical elementary distribution theory. Accordingly, no novelty is claimed for the kernel inversion, the logarithmic coordinate, or prime-power atomic measures. The durable content is the exact repository-level bridge between two already persisted formulas and the resulting clarification of the remaining uniformity barrier.

## Boundaries and falsification

The Green inversion is a distributional identity for the coefficient field, not an instruction to differentiate Wang's asymptotic error term. Any theorem-level use must establish the required uniformity independently.

The normalization is falsifiable directly: the source kernel has exponent `2*pi` at amplitude level and `4*pi` after squaring, so its Green operator is respectively `4*pi^2-d_q^2` with delta factor `4*pi`, or `16*pi^2-d_q^2` with delta factor `8*pi`. A different normalization of the frequency coordinate must transform both constants consistently.

The Rodgers pairing is falsified if the previously audited quadratic coefficient does not in fact use the measure `sum_(p,m) (log p)^2 p^(-m) delta_(m log p/(2*pi))`; in that case the last identification must be withdrawn even though the Wang-side Green identity survives.

No untouched confirmation-zero data are used.

## Research consequence

The next useful work is no longer to search abstractly for a transform between a moving Wang prime scale and fixed Rodgers labels. The transform at the coefficient level is explicit: use logarithmic source position and invert the exponential Green smoothing.

The live mathematical bottleneck is whether the **short-interval asymptotic** can be controlled in the shrinking `alpha=O(1/log T)` regime, or in an integrated formulation that avoids unstable differentiation, strongly enough for the exact source-level dictionary to survive averaging. That is a distinct theorem question and should be pursued separately rather than folded into this finding.