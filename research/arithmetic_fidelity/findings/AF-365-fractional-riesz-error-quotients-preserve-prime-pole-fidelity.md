# AF-365 — fractional Riesz error quotients preserve prime-pole fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-BRIDGE`, `ARITHMETIC-FIDELITY`, `QUANTITATIVE-FIDELITY`, `ZERO-SENSITIVE-SOURCE`, `TARGET-METRIC-CALIBRATION`, `NO-NOVELTY-CLAIM`

## Claim

AF-350 proves that an integer-order Riesz profile observed modulo `O(X^theta)` still preserves every Dirichlet singularity strictly to the right of `Re(s)=theta`. The current small-order program AF-351--AF-364 uses instead a real order `delta -> 0`, so AF-350's own boundary note leaves a genuine audit gap: the integer polynomial inverse of the beta factor is no longer available.

The gap closes exactly. Let `delta>=0` be any fixed real number and, for a coefficient sequence `c=(c_n)`, define

\[
\mathcal R_\delta[c](X)
:=
\sum_{n\le X}c_n\left(1-\frac nX\right)^\delta,
\qquad X>0.
\tag{1}
\]

Suppose the Dirichlet series

\[
C(s):=\sum_{n\ge1}c_n n^{-s}
\tag{2}
\]

converges absolutely in some right half-plane, and let `theta>=0`. If

\[
\boxed{\mathcal R_\delta[c](X)=O(X^\theta)}
\qquad (X\to\infty),
\tag{3}
\]

then `C` has a holomorphic continuation to

\[
\boxed{\Re s>\theta},
\tag{4}
\]

there given by

\[
\boxed{
C(s)=
\frac{\Gamma(s+\delta+1)}
{\Gamma(s)\Gamma(\delta+1)}
\int_1^\infty
\mathcal R_\delta[c](X)X^{-s-1}\,dX.
}
\tag{5}
\]

The key point is not merely that the Mellin multiplier is invertible for one order. For every real `delta>=0`,

\[
B(s,\delta+1)
=
\frac{\Gamma(s)\Gamma(\delta+1)}
{\Gamma(s+\delta+1)}
\tag{6}
\]

is holomorphic and **zero-free** throughout `Re(s)>0`; its reciprocal in `(5)` is holomorphic there as well. Thus changing the positive Riesz order cannot create or cancel a Dirichlet pole in the positive half-plane.

Consequently, if two sources `a,b` have meromorphic Dirichlet transforms `A,B` on `Re(s)>theta`, then

\[
\mathcal R_\delta[a](X)-\mathcal R_\delta[b](X)=O(X^\theta)
\tag{7}
\]

forces

\[
\boxed{A-B\in\operatorname{Hol}(\Re s>\theta)}.
\tag{8}
\]

So the fractional-order quotient

\[
Q_{\delta,\theta}(a)
:=
\mathcal R_\delta[a]\bmod O(X^\theta)
\tag{9}
\]

is faithful to the complete meromorphic principal-part discriminator above the error line, exactly as in AF-350. The surviving discriminator is independent of whether `delta` is integer, fractional, large, or arbitrarily small but positive.

This has a rational-prime specialization that connects the present Riesz-conditioning sequence back to arithmetic specificity. Let

\[
p(n):=
\begin{cases}
\log q,&n=q\text{ prime},\\
0,&\text{otherwise},
\end{cases}
\tag{10}
\]

and define the centered prime-only source

\[
g(1):=0,
\qquad
g(n):=p(n)-1\quad(n\ge2).
\tag{11}
\]

Its Dirichlet transform is the AF-341 function

\[
G(s)=\sum_{n\ge1}g(n)n^{-s}
=A(s)-\bigl(\zeta(s)-1\bigr),
\qquad
A(s)=\sum_q(\log q)q^{-s}.
\tag{12}
\]

AF-341 proves that `G` is meromorphic on `Re(s)>1/2`, regular at `s=1`, and has a pole of residue `-m` at every zeta zero `rho` of multiplicity `m` with `Re(rho)>1/2`. Therefore, for every fixed real `delta>=0` and every `0<=theta<1`,

\[
\boxed{
\mathcal R_\delta[g](X)=O(X^\theta)
\Longrightarrow
\zeta(s)\ne0
\quad\text{for }\Re s>\max\{\theta,\tfrac12\}.
}
\tag{13}
\]

In particular,

\[
\boxed{
\mathcal R_\delta[g](X)
=O_\varepsilon(X^{1/2+\varepsilon})
\text{ for every }\varepsilon>0
\Longrightarrow \mathrm{RH}.
}
\tag{14}
\]

The same conclusion holds with the full centered Mangoldt source `c_n=Lambda(n)-1`; there AF-350's stronger singularity description applies throughout the positive half-plane, and `(5)` shows that its error-exponent gate is unchanged for every real `delta>=0`.

The resulting Arithmetic Fidelity separation is exact:

\[
\boxed{
\text{fractional Riesz smoothing}
\text{ preserves the prime/zero pole discriminator exactly,}
}
\tag{15}
\]

while AF-361--AF-364 show simultaneously that recovering detailed endpoint coordinates through the same small-order channel can have an inverse-noise cost of `e^u`, `e^{u+v}`, or the critical `e^{u+v}/\sqrt v` scale depending on the target profile. **Arithmetic specificity can therefore survive perfectly even when stable coordinate recovery is badly conditioned.** Information survival and recovery cost are genuinely different currencies in the current Riesz example.

## Derivation

### 1. The Mellin multiplier is the beta function for every real Riesz order

Assume first that `Re(s)=sigma>0` lies in a half-plane where `(2)` converges absolutely. For one coefficient, the substitution `u=n/X` gives

\[
\begin{aligned}
\int_n^\infty
\left(1-\frac nX\right)^\delta X^{-s-1}\,dX
&=n^{-s}\int_0^1(1-u)^\delta u^{s-1}\,du\\
&=n^{-s}B(s,\delta+1).
\end{aligned}
\tag{16}
\]

Because `delta>=0` and the Dirichlet series is absolutely convergent, Tonelli/Fubini applies after taking absolute values in the common right half-plane. Summing `(16)` gives

\[
\int_1^\infty
\mathcal R_\delta[c](X)X^{-s-1}\,dX
=B(s,\delta+1)C(s).
\tag{17}
\]

This is the same beta multiplier already appearing in the zero coefficients of AF-356--AF-364. No integrality assumption on `delta` enters the calculation.

### 2. The fractional beta multiplier has no positive-half-plane kernel

For real `delta>=0`, `(6)` and the classical analytic structure of the gamma function imply that on `Re(s)>0` all three gamma arguments `s`, `delta+1`, and `s+delta+1` avoid the nonpositive integers. The gamma function has no zeros anywhere and no poles in this region. Hence

\[
B(s,\delta+1)\ne0
\qquad(\Re s>0),
\tag{18}
\]

and

\[
B(s,\delta+1)^{-1}
=
\frac{\Gamma(s+\delta+1)}
{\Gamma(s)\Gamma(\delta+1)}
\tag{19}
\]

is holomorphic there.

Now assume `(3)`. Then

\[
I(s):=\int_1^\infty
\mathcal R_\delta[c](X)X^{-s-1}\,dX
\tag{20}
\]

converges absolutely and locally uniformly on `Re(s)>theta`, so `I` is holomorphic in that half-plane. Since `theta>=0`, `(19)I(s)` is holomorphic there too. On the original half-plane of absolute convergence it equals `C(s)` by `(17)`, and uniqueness of analytic continuation proves `(4)`--`(5)`.

This is exactly the audit that was unnecessary at integer order in AF-350 because `B(s,r+1)^{-1}` reduced to a polynomial. At fractional order the inverse is no longer polynomial, but its gamma quotient remains zero-free and holomorphic in the entire positive half-plane relevant to the arithmetic discriminator.

### 3. Pairwise `O(X^theta)` equivalence preserves principal parts

Apply the previous argument to `c=a-b`. Equation `(7)` gives a holomorphic continuation of the initial Dirichlet difference `A-B` to `Re(s)>theta` through `(5)`. If `A` and `B` already have meromorphic continuations there, uniqueness forces their meromorphic difference to coincide with this holomorphic function. Every pole and every principal-part coefficient therefore cancels, proving `(8)`.

This is a matched-control statement at the same information layer. A non-arithmetic control may imitate local support, counts, signs, or even large parts of the Riesz profile, but if its Dirichlet transform has a different pole divisor above the declared error line, it cannot be `O(X^theta)`-equivalent to the arithmetic source after any fixed real Riesz order `delta>=0`.

Conversely, equality of principal parts is not enough to guarantee `(7)`. As in AF-350, the theorem is deliberately one-way: the holomorphic remainder may still be too large in vertical growth or inverse Mellin size. The result identifies a discriminator that must survive the quotient, not a complete classification of its fibers.

### 4. The prime layer supplies an independently specified arithmetic discriminator

AF-341 decomposes

\[
-\frac{\zeta'(s)}{\zeta(s)}=A(s)+R(s),
\tag{21}
\]

where the higher-prime-power tail `R` is holomorphic on `Re(s)>1/2`. Consequently

\[
G(s)
=-\frac{\zeta'(s)}{\zeta(s)}-R(s)-\zeta(s)+1
\tag{22}
\]

on that half-plane. The pole at `s=1` cancels, while a zeta zero `rho` with `Re(rho)>1/2` and multiplicity `m` contributes the principal part

\[
-\frac{m}{s-\rho}.
\tag{23}
\]

If `(13)`'s Riesz error bound holds, `(5)` makes `G` holomorphic on `Re(s)>theta`. Intersecting this with the independently known representation `(22)` excludes every zero satisfying both `Re(rho)>theta` and `Re(rho)>1/2`, which is precisely `(13)`.

For `(14)`, suppose a zero had real part `beta_0>1/2`. Choose `epsilon` with `0<epsilon<beta_0-1/2`. Applying `(13)` at `theta=1/2+epsilon` excludes that zero. Thus there is no zero to the right of the critical line, and the functional-equation symmetry `rho -> 1-rho` gives RH.

This arithmetic discriminator is specified before the Riesz channel: the source is the ordinary rational-prime layer `(10)`, and the relevant pole divisor comes from its classical Dirichlet transform. No target is chosen to cancel the multiplier after seeing `delta`. The only channel fact used is that its Mellin multiplier is zero-free where the discriminator lives.

## Relation to AF-350 and AF-361--AF-364

AF-350 already establishes the error-exponent singularity gate for integer order and explicitly leaves noninteger order to a separate gamma-factor audit. AF-365 closes that boundary exactly where the current program needs it: the small-order channel `delta downarrow 0` of AF-351--AF-364.

The combined picture now separates three logically different questions.

First, **discriminator survival**: at the full Mellin/principal-part level, every fixed real `delta>=0` transmits the prime/zero pole discriminator because `B(s,delta+1)` is zero-free in `Re(s)>0`.

Second, **destination resolution**: observing the Riesz profile only modulo `O(X^theta)` retains precisely enough Mellin information to protect singularities above `theta`, while potentially erasing coefficient provenance and all holomorphic differences.

Third, **stable inversion**: AF-361--AF-364 show that finite-band coordinate recovery under Hilbert noise can still become exponentially expensive as `delta -> 0` and the physical frequency band grows. That instability does not contradict `(15)`: a zero-free multiplier can be injective and pole-faithful while having very small modulus on the modes used by a stronger reconstruction task.

This is the concrete separation requested by the current Arithmetic Fidelity frontier. The rational-prime discriminator is not being manufactured after compression; it survives the fractional Riesz stage exactly. What remains difficult is to identify destination observables and error budgets that consume that surviving discriminator without requiring an unstable reconstruction of substantially more source detail.

## Boundaries and falsification

- `delta` is fixed while the Mellin continuation argument is applied. A variable order `delta=delta(X)` inside the cutoff kernel does not factor as one beta multiplier and is not covered by this theorem.
- The theorem uses `theta>=0`, so the continuation domain lies inside the positive half-plane where the beta multiplier and its reciprocal are manifestly holomorphic and nonzero. Extending the statement across nonpositive real parts requires auditing the gamma poles/zeros and is irrelevant to the present zeta discriminator.
- The Riesz bound is a global eventual `C^0` estimate. Sparse samples, mean-square bounds, subsequence bounds, or local-window estimates do not automatically give the Mellin integral `(20)`.
- Principal-part fidelity is not coefficient or support fidelity. Matched controls whose Dirichlet transforms differ only by a holomorphic function on `Re(s)>theta` are not separated by this theorem.
- For the prime-only source, AF-341's elementary higher-prime-power decomposition identifies the zeta-zero poles only in the open half-plane `Re(s)>1/2`. Equation `(13)` deliberately makes no claim about a boundary zero at `Re(s)=1/2` from the prime-layer representation alone.
- Equation `(14)` is an implication, not a converse and not a new RH criterion. Classical Chebyshev-error formulations already make prime-distribution error exponents equivalent or closely related to zero-free regions under suitable conventions.
- The result does not improve the AF-361--AF-364 noise condition numbers. It proves that the arithmetic singularity is still present in the exact/coarse Mellin representation; it does not provide a cheap algorithm for extracting it from noisy finite data.

A direct falsification would require either failure of the beta identity `(17)` in its absolute-convergence domain or a zero/pole of `B(s,delta+1)` in `Re(s)>0`. The former is an elementary change-of-variables calculation, while the latter is excluded by the classical zero-free meromorphic structure of the gamma function.

## Prior art and novelty assessment

No novelty is claimed for fractional Riesz means, beta/gamma Mellin multipliers, or RH criteria from prime-counting error exponents.

Hardy and Riesz, *The General Theory of Dirichlet's Series* (1915), is classical prior art for typical Riesz means of Dirichlet series. AF-350 already uses that framework and Hardy--Littlewood's 1916 Riesz treatment of the von Mangoldt coefficients. Bruce C. Berndt, **“Identities involving the coefficients of a class of Dirichlet series. VII,”** *Transactions of the American Mathematical Society* **201** (1975), 247--261, DOI `10.1090/S0002-9947-1975-0352018-5`, explicitly studies Riesz sums `A_rho(x)=sum_{n<=x}a(n)(x-n)^rho` for nonintegral order in the broader Dirichlet-series setting. NIST DLMF §5.2 records the decisive analytic fact used in `(18)`--`(19)`: `Gamma(z)` is meromorphic with no zeros, and `1/Gamma(z)` is entire with zeros only at the nonpositive integers.

AF-341 already audits the prime-only Dirichlet transform against Titchmarsh and the classical Chebyshev/prime-zeta literature. The present finding does not claim a new prime-number-theory theorem. Its durable Arithmetic Fidelity contribution is the cross-layer statement that the **same fractional Riesz channel whose small-order inverse becomes badly conditioned in AF-361--AF-364 nevertheless preserves the independently specified rational-prime pole discriminator exactly at every fixed positive order**. That separates arithmetic specificity from target conditioning in one concrete transformation rather than leaving the distinction as an abstract warning.