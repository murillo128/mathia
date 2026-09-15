# AF-352 — every positive Riesz order crosses the critical boundary-conditioning threshold

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `ARITHMETIC-FIDELITY`, `QUANTITATIVE-FIDELITY`, `ZERO-SENSITIVE-SOURCE`, `TARGET-METRIC-CALIBRATION`, `BOUNDARY-CLARIFICATION`, `NO-NOVELTY-CLAIM`

## Claim

Let

\[
c_n:=\Lambda(n)-1
\]

and, for a fixed real `delta>=0`, define the Riesz profile

\[
\mathcal R_\delta[c](X)
:=
\sum_{n\le X}c_n\left(1-\frac nX\right)^\delta,
\qquad X\ge2.
\tag{1}
\]

AF-351 proved the critical-boundary equivalence for every fixed integer order `r>=1` and left fractional orders open. The actual threshold is sharper:

\[
\boxed{
\text{for every fixed real }\delta>0,
\qquad
\mathrm{RH}
\iff
\mathcal R_\delta[\Lambda-1](X)=O_\delta(X^{1/2}).
}
\tag{2}
\]

At the endpoint `delta=0`, the same sharp norm is impossible:

\[
\mathcal R_0[\Lambda-1](X)
=
\psi(X)-\lfloor X\rfloor
\ne O(X^{1/2}).
\tag{3}
\]

Thus there is no smallest positive Riesz order at which the critical boundary becomes well conditioned. **Every positive amount of Riesz smoothing is enough, while zero smoothing is not.** The phase boundary is the open endpoint `delta=0`.

The mechanism is exact. A nontrivial zero `rho` is transmitted through the smoothing with multiplier

\[
B(\rho,\delta+1)
=
\frac{\Gamma(\rho)\Gamma(\delta+1)}
     {\Gamma(\rho+\delta+1)}.
\tag{4}
\]

On the critical line this has size `|gamma|^{-1-delta}`. Since the number of zeros up to height `T` is `O(T log T)`, the critical zero coefficients are absolutely summable for every `delta>0`, but the endpoint decay `1/|gamma|` at `delta=0` is not absolutely summable and the classical prime error actually exceeds the sharp `sqrt(X)` norm along suitable sequences.

This is not a new RH criterion. It is a refinement of AF-351's fidelity interpretation: **arbitrarily weak positive smoothing can regularize the target-relevant boundary signal without erasing the off-critical singularity discriminator.**

## Derivation

### 1. The Mellin multiplier is valid for every real positive order

For `delta>-1`, `Re(s)>0`, and `n>0`, the change of variable `u=n/X` gives

\[
\int_n^\infty
\left(1-\frac nX\right)^\delta X^{-s-1}\,dX
=
n^{-s}B(s,\delta+1),
\tag{5}
\]

where

\[
B(s,\delta+1)
=
\frac{\Gamma(s)\Gamma(\delta+1)}
     {\Gamma(s+\delta+1)}.
\tag{6}
\]

Hence, initially in any half-plane where the Dirichlet series

\[
C(s):=\sum_{n\ge1}\frac{c_n}{n^s}
\tag{7}
\]

converges absolutely, termwise integration yields

\[
\int_1^\infty
\mathcal R_\delta[c](X)X^{-s-1}\,dX
=
B(s,\delta+1)C(s).
\tag{8}
\]

For `c_n=Lambda(n)-1`,

\[
C(s)
=-\frac{\zeta'(s)}{\zeta(s)}-\zeta(s)
\qquad(\Re s>1).
\tag{9}
\]

The pole at `s=1` cancels in `(9)`, while every nontrivial zero of zeta remains a pole of `C`.

### 2. The critical bound still detects every zero to the right

Assume for one fixed `delta>0` that

\[
\mathcal R_\delta[\Lambda-1](X)=O_\delta(X^{1/2}).
\tag{10}
\]

Then the left side of `(8)` is holomorphic for `Re(s)>1/2`. In this region `B(s,delta+1)` is finite and nonzero: Gamma has no zeros, and the poles of the denominator Gamma factor only create zeros of `B` at points lying to the left of this half-plane.

Equation `(8)`, first valid for `Re(s)>1` and then continued by identity, therefore makes `C(s)` holomorphic throughout

\[
\Re(s)>\frac12.
\tag{11}
\]

By `(9)`, zeta has no nontrivial zero there. The functional equation reflects every nontrivial zero `rho` to `1-rho`, so the absence of zeros strictly to the right of `1/2` also excludes zeros strictly to the left. Consequently

\[
\mathcal R_\delta[\Lambda-1](X)=O_\delta(X^{1/2})
\quad\Longrightarrow\quad
\mathrm{RH}
\tag{12}
\]

for every fixed `delta>0`.

This is the real-order version of AF-350's singularity-preservation argument; no integer-order factorization of the beta function is needed.

### 3. Under RH, every positive order makes the critical zero tail absolutely summable

For fixed real `delta>0`, the classical Riesz explicit-formula contour gives

\[
\mathcal R_\delta[\Lambda](X)
=
\frac{X}{\delta+1}
-
\sum_\rho m_\rho B(\rho,\delta+1)X^\rho
+
O_\delta(1),
\qquad X\ge2,
\tag{13}
\]

where the bounded remainder collects the `s=0` contribution and the trivial-zero terms. At a collision between a trivial zero and a Gamma pole the residue may contain `X^{-2m}\log X`; such terms are still bounded for `X>=2` and do not affect the critical scale.

For the dense unit source, the kernel `u -> (1-u)^delta` is bounded and monotone on `[0,1]`. A sum-integral comparison therefore gives

\[
\mathcal R_\delta[1](X)
=
\frac{X}{\delta+1}+O_\delta(1).
\tag{14}
\]

Subtracting `(14)` from `(13)` yields

\[
\mathcal R_\delta[\Lambda-1](X)
=
-
\sum_\rho m_\rho B(\rho,\delta+1)X^\rho
+
O_\delta(1).
\tag{15}
\]

Now assume RH, so `rho=1/2+i gamma`. The standard Gamma-ratio form of Stirling's formula gives

\[
|B(\tfrac12+i\gamma,\delta+1)|
\ll_\delta
(1+|\gamma|)^{-1-\delta}.
\tag{16}
\]

The Riemann--von Mangoldt count gives `N(T)=O(T log T)`. Thus the zeros with

\[
2^j<|\gamma|\le2^{j+1}
\]

contribute at most

\[
O_\delta\!\left(j\,2^{-j\delta}\right)
\tag{17}
\]

to the absolute coefficient sum. Since

\[
\sum_{j\ge0}j\,2^{-j\delta}<\infty
\qquad(\delta>0),
\tag{18}
\]

we obtain

\[
\sum_\rho m_\rho
|B(\rho,\delta+1)|<\infty.
\tag{19}
\]

Therefore the zero series in `(15)`, divided by `X^{1/2}`, converges absolutely and uniformly in `log X`, and

\[
\left|
\sum_\rho m_\rho B(\rho,\delta+1)X^\rho
\right|
\le
X^{1/2}
\sum_\rho m_\rho |B(\rho,\delta+1)|
=
O_\delta(X^{1/2}).
\tag{20}
\]

Together with `(15)`, this proves

\[
\mathrm{RH}
\quad\Longrightarrow\quad
\mathcal R_\delta[\Lambda-1](X)=O_\delta(X^{1/2})
\qquad(\delta>0).
\tag{21}
\]

Combining `(21)` and `(12)` proves `(2)`.

### 4. The endpoint failure is genuine, not a proof artifact

At `delta=0`, equation `(1)` reduces to

\[
\mathcal R_0[\Lambda-1](X)
=
\psi(X)-\lfloor X\rfloor.
\tag{22}
\]

Hardy--Littlewood's classical oscillation theorem gives

\[
\psi(X)-X
=
\Omega_\pm\!\left(
X^{1/2}\log\log\log X
\right).
\tag{23}
\]

The bounded floor correction cannot remove this oscillation, so `(3)` follows. In particular, the endpoint is not excluded merely because the absolute-convergence estimate `(18)` fails; the actual arithmetic source violates the target norm there.

For `delta>0`, by contrast, the extra factor `|gamma|^{-delta}` is arbitrarily weak but enough to cross the summability threshold against zero density. Hence the conditioning transition is genuinely located at

\[
\boxed{\delta=0.}
\tag{24}
\]

The transition is one-sided: every fixed positive order lies on the well-conditioned side, while the endpoint itself does not.

## Prior art and novelty assessment

No novelty claim is made for the constituent analytic-number-theory statements.

- G. H. Hardy and J. E. Littlewood, **“Contributions to the Theory of the Riemann Zeta-Function and the Theory of the Distribution of Primes,”** *Acta Mathematica* 41, 119--196 (1916), DOI `10.1007/BF02422942`, is classical prior art for generalized Riesz means of the von Mangoldt function, their Mellin/Gamma kernel, the zero-sensitive explicit formula, and the oscillation input at the unsmoothed endpoint.
- G. H. Hardy and Marcel Riesz, ***The General Theory of Dirichlet's Series***, Cambridge Tracts in Mathematics and Mathematical Physics 18, Cambridge University Press (1915), is classical background for Riesz typical means and Mellin/Dirichlet-series continuation arguments.
- E. C. Titchmarsh, revised by D. R. Heath-Brown, ***The Theory of the Riemann Zeta-function***, 2nd ed., Clarendon Press, Oxford (1986), is the standard source for zero counting, the functional equation, and the explicit-formula framework used here.

A targeted literature check found the arbitrary-real-order Riesz transform and zero formula as standard material, but did not justify treating the exact statement `(2)` as a new theorem. AF-352 therefore records it as a derived synthesis of classical ingredients. The line-specific contribution is the **conditioning interpretation and the sharpening of AF-351 from the first positive integer order to the open real interval `delta>0`**.

## Boundaries and failure modes

### `delta` is fixed

The implied constants may depend strongly on `delta`. Nothing here is uniform as `delta -> 0+`, and no claim is made for an order `delta=delta(X)` tending to zero with `X`. The dyadic majorant in `(18)` already shows why deterioration near the endpoint is unavoidable at the level of this absolute-convergence argument, but AF-352 does not assert an optimal blow-up rate.

### Positive smoothing does not recover the source

Equation `(2)` concerns the terminal critical `C^0` scale only. It does not imply recovery of `Lambda(n)-1`, prime support, gaps, signs, or other local arithmetic data. AF-349 showed that full coefficient recovery lives in a much stronger destination metric.

### The theorem is about preserving one discriminator while improving its conditioning

Riesz smoothing still suppresses high-frequency zero modes by the multiplier `(4)`. Fidelity here does not mean isometry or losslessness. It means that the transformation simultaneously:

1. leaves every off-critical zero visible as a Mellin singularity obstruction to `(10)`; and
2. attenuates the critical-line tail enough that, under RH, the exact boundary norm becomes finite.

This is target-relative fidelity, not global information preservation.

### No assertion is made for negative order or other kernels

For `delta<0` the endpoint kernel is singular and the present sum-integral and absolute-tail argument changes category. Likewise a different smoothing kernel must be audited through its own Mellin multiplier and high-frequency decay; the result is not a generic statement that any nonzero smoothing suffices.

### This remains equivalent to RH, not progress toward proving it

For every fixed `delta>0`, proving the bound in `(2)` for the actual prime source is already strong enough to force RH. The smoothing creates a better-conditioned representation of the discriminator; it does not supply the missing arithmetic estimate.

## Consequence for Arithmetic Fidelity

AF-351 suggested that one Riesz order was the first boundary-conditioning threshold because integer orders were the declared category there. AF-352 removes that discretization artifact. The governing quantity is not the integer order itself but the **high-zero decay exponent of the compression multiplier**.

At `delta=0`, the zero multiplier is asymptotically `|gamma|^{-1}`. For every `delta>0`, however small, it becomes `|gamma|^{-1-delta}`. Against zero density `N(T)=O(T log T)`, that infinitesimal exponent gain is exactly enough to turn the critical coefficient tail from non-absolutely-summable to absolutely summable, while the Mellin multiplier remains nonzero in the half-plane where off-critical zeros must be detected.

This supplies a sharper reusable design principle for the line:

\[
\boxed{
\text{a useful compression threshold is set by the interaction of}
\\
\text{target-mode density with multiplier decay, not by nominal transform order.}
}
\tag{25}
\]

For future conditioning questions, the relevant audit is therefore quantitative: estimate the density of target-relevant modes, estimate the decay imposed by the compression, and locate the summability/regularity boundary. Only after that should one ask whether the same multiplier has introduced zeros or quotient identifications that destroy the discriminator itself.