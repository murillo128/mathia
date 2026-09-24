# AF-541 — Two-point weighted contrast cancels arbitrary tail-multiplier drift

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DIRICHLET-SOURCE` · `OUTWARD-TRANSPORT` · `CARRIER-SHAPE` · `NUISANCE-ANNIHILATION` · `FINITE-RESOLUTION` · `MINIMAL-LIFT` · `CONDITIONING` · `NO-NOVELTY-CLAIM`

## Claim

Keep the exact anchored outward-tail carrier of AF-525–AF-540,

\[
D_{X,C}(t)
=
\frac{(C^{1+t}-1)B_0(X,t)}{P(1+t)},
\qquad
B_0(X,t)=\sum_{p\le X}p^{-1-t},
\]

and compare the power-separated cutoffs

\[
B_A=\lfloor A^\theta\rfloor,
\qquad 0<\theta<1,
\]

through

\[
R_A(t)
=
\frac{D_{B_A,\widetilde C_A}(t)}{D_{A,C_A}(t)}
=
\frac{\widetilde C_A^{1+t}-1}{C_A^{1+t}-1}
\frac{B_0(B_A,t)}{B_0(A,t)},
\]

where the integer multiplier sequences `C_A,\widetilde C_A\ge2` are completely arbitrary. Write

\[
L_A=\log A,
\qquad
H_A=\log L_A.
\]

AF-540 showed that the second log-jet removes the arbitrary-multiplier obstruction because every multiplier derivative of order at least two is uniformly bounded. Finite resolution can do better: the exact multiplier representation has only one **unbounded** point-sample direction, and a weighted two-point contrast already annihilates it.

For `0<h\le A^{-1}`, define

\[
\mathcal Q_{A,h}
:=
\log R_A(h)-(1+h)\log R_A(0).
\tag{1}
\]

Then

\[
\boxed{
\sup_{C_A,\widetilde C_A\ge2}
\sup_{0<h\le A^{-1}}
\left|
\frac{H_A}{hL_A}\mathcal Q_{A,h}-(1-\theta)
\right|
\longrightarrow0.
}
\tag{2}
\]

Thus **two finite samples** of the exact carrier recover the hidden anchor exponent uniformly over arbitrary tail multipliers. No derivative oracle, multiplier growth restriction, or co-tuning is required.

At the largest boundary-layer separation `h=A^{-1}`,

\[
\boxed{
\mathcal Q_{A,A^{-1}}
\sim
(1-\theta)\frac{L_A}{A H_A}.
}
\tag{3}
\]

Consequently, if the two observed log-values have deterministic additive errors bounded by `\varepsilon_A`, the decoder based on `(1)` is consistent whenever

\[
\boxed{
\varepsilon_A=o\!\left(\frac{L_A}{A H_A}\right).
}
\tag{4}
\]

This is the **same finite-resolution signal order** as AF-529's co-tuned endpoint secant, despite allowing completely arbitrary multipliers.

There is also a precise minimality statement for the declared observation class. Among nonzero **linear point-sample contrasts** whose response to `\log(C^{1+t}-1)` must remain uniformly bounded as `C\to\infty`, one point never suffices. On the two nodes `0,h`, the unique annihilator of the unbounded multiplier direction, up to overall scale, has weights proportional to

\[
(-(1+h),1),
\]

which is exactly `(1)`. This is a minimality theorem for linear point-sample nuisance annihilation, not for arbitrary nonlinear decoders.

## Derivation

### 1. The arbitrary multiplier has one unbounded shape direction

Put

\[
\phi_C(t)=\log(C^{1+t}-1),
\qquad a=\log C.
\]

The exact decomposition used in AF-540 is

\[
\phi_C(t)
=(1+t)a+r_C(t),
\qquad
r_C(t)=\log\!\left(1-C^{-(1+t)}\right).
\tag{5}
\]

The entire unbounded dependence on `C` is the one-dimensional function `(1+t)a`. The remainder is uniformly controlled on `t\ge0`. Indeed,

\[
|r_C(0)|\le\log2,
\tag{6}
\]

and

\[
r_C'(t)
=
\frac{\log C}{C^{1+t}-1},
\qquad
0\le r_C'(t)\le\log2
\tag{7}
\]

for every `C\ge2` and `t\ge0`.

Apply the two-point functional

\[
Q_h f=f(h)-(1+h)f(0).
\tag{8}
\]

It kills the unbounded direction exactly:

\[
Q_h[(1+t)a]=0.
\tag{9}
\]

For the bounded remainder,

\[
Q_h r_C
=r_C(h)-r_C(0)-h r_C(0),
\]

so `(6)`–`(7)` give

\[
|Q_h r_C|
\le2h\log2.
\tag{10}
\]

Therefore, uniformly over arbitrary `C,\widetilde C\ge2`,

\[
\boxed{
\left|
Q_h\bigl(\phi_{\widetilde C}-\phi_C\bigr)
\right|
\le4h\log2.
}
\tag{11}
\]

After the target normalization `H_A/(hL_A)`, the entire multiplier contribution is at most

\[
4\log2\,\frac{H_A}{L_A}\longrightarrow0.
\tag{12}
\]

This is stronger at finite resolution than replacing the first derivative by a generic second difference: it uses the exact nuisance representation rather than annihilating the whole two-dimensional affine space.

### 2. The source contribution retains the first-shape signal

Let

\[
\psi_X(t)=\log B_0(X,t),
\qquad
S(X)=B_0(X,0)=\sum_{p\le X}\frac1p,
\]

and

\[
\mu_X(t)
=
\frac{\sum_{p\le X}(\log p)p^{-1-t}}
{\sum_{p\le X}p^{-1-t}}.
\]

Since

\[
\psi_X'(t)=-\mu_X(t),
\]

we have the exact identity

\[
\frac{Q_h\psi_X}{h}
=
-\frac1h\int_0^h\mu_X(t)\,dt
-\log S(X).
\tag{13}
\]

Hence for the source ratio,

\[
\frac1hQ_h\bigl(\psi_{B_A}-\psi_A\bigr)
=
\frac1h\int_0^h
\bigl(\mu_A(t)-\mu_{B_A}(t)\bigr)\,dt
+
\log\frac{S(A)}{S(B_A)}.
\tag{14}
\]

The Mertens-moment estimates already used in AF-529 give, uniformly for `0\le t\le A^{-1}`,

\[
\frac{H_A}{L_A}
\bigl(\mu_A(t)-\mu_{B_A}(t)\bigr)
\longrightarrow1-\theta.
\tag{15}
\]

For completeness, the required perturbation from `t=0` is elementary: with

\[
M_j(X,t)=\sum_{p\le X}(\log p)^j p^{-1-t},
\]

one has for `t\ge0`

\[
|M_j(X,t)-M_j(X,0)|
\le t M_{j+1}(X,0),
\tag{16}
\]

while classical partial summation from Mertens' first theorem gives the needed logarithmic moment orders. Because `t\le A^{-1}`, these perturbations are negligible for both `X=A` and `X=B_A`.

Also,

\[
S(A)=H_A+B_1+O(L_A^{-1}),
\]

and

\[
S(B_A)=H_A+\log\theta+B_1+o(1),
\tag{17}
\]

so

\[
\frac{H_A}{L_A}
\log\frac{S(A)}{S(B_A)}
\longrightarrow0.
\tag{18}
\]

Averaging `(15)` over any `0<h\le A^{-1}` and using `(18)` yields

\[
\sup_{0<h\le A^{-1}}
\left|
\frac{H_A}{hL_A}
Q_h\bigl(\psi_{B_A}-\psi_A\bigr)
-(1-\theta)
\right|
\longrightarrow0.
\tag{19}
\]

Combining `(11)`–`(12)` with `(19)` proves `(2)`.

### 3. Finite-resolution decoder and deterministic noise scale

With exact data, define

\[
\widehat\theta_{A,h}
=
1-
\frac{H_A}{hL_A}\mathcal Q_{A,h}.
\tag{20}
\]

Equation `(2)` gives `\widehat\theta_{A,h}\to\theta` uniformly over arbitrary multiplier choices and uniformly over `0<h\le A^{-1}`.

Now suppose the observed log-values are

\[
Y_0=\log R_A(0)+e_0,
\qquad
Y_h=\log R_A(h)+e_h,
\qquad
|e_0|,|e_h|\le\varepsilon_A.
\]

The observed contrast

\[
\widehat{\mathcal Q}_{A,h}
=Y_h-(1+h)Y_0
\]

satisfies

\[
|\widehat{\mathcal Q}_{A,h}-\mathcal Q_{A,h}|
\le(2+h)\varepsilon_A.
\tag{21}
\]

Thus a sufficient condition for consistency is

\[
\varepsilon_A=o\!\left(\frac{hL_A}{H_A}\right).
\tag{22}
\]

The largest permitted boundary step `h=A^{-1}` maximizes this deterministic error budget and gives `(3)`–`(4)`.

AF-529 found exactly the same order `L_A/(A H_A)` for a first secant after co-tuning the multiplier amplitude. The present contrast reaches that order with **no multiplier restriction at all** because the dangerous multiplier direction is removed algebraically before the asymptotic normalization.

### 4. Two samples are minimal for linear point-sample annihilation

For every fixed `t\ge0`, `(5)` gives

\[
\phi_C(t)=(1+t)\log C+O(1)
\qquad(C\to\infty),
\tag{23}
\]

with the `O(1)` uniform over `C\ge2`. Therefore any nonzero one-point linear functional

\[
L(f)=w f(t_0),
\qquad w\ne0,
\]

has

\[
|L(\phi_C)|\to\infty.
\]

So one point cannot produce a nonzero linear observable with uniformly bounded arbitrary-multiplier nuisance.

For two distinct nodes `t_0,t_1`, a contrast

\[
L(f)=w_0f(t_0)+w_1f(t_1)
\]

cancels the unbounded multiplier direction exactly iff

\[
w_0(1+t_0)+w_1(1+t_1)=0.
\tag{24}
\]

This is a one-dimensional nullspace. At `t_0=0,t_1=h`, `(24)` gives the weights `(-(1+h),1)` up to scale, proving the stated minimality and uniqueness.

The distinction from AF-195 is load-bearing. A **generic affine nuisance** `a+bt` has two independent coefficients and requires three samples for a nonzero linear annihilator. Here the exact tail-multiplier family has only one unbounded affine direction, `(1+t)\log C`; its remaining nonlinear part is uniformly `O(h)` under the two-point functional. Exploiting this representation-specific rank reduction saves one sample and one order of finite-resolution conditioning.

## Prior-art / novelty audit

The generic mathematics of removing nuisance directions by projection or differencing is classical.

- D. R. Cox and N. Reid, **“Parameter Orthogonality and Approximate Conditional Inference,”** *Journal of the Royal Statistical Society: Series B* 49(1), 1–39 (1987), DOI `10.1111/j.2517-6161.1987.tb01422.x`, is classical prior art for orthogonalizing a target against nuisance parameters.
- Yongchang Hu and Geert Leus, **“On a unified framework for linear nuisance parameters,”** *EURASIP Journal on Advances in Signal Processing* 2017, article 4 (2017), DOI `10.1186/s13634-016-0438-8`, explicitly treats projection and reference differencing as standard ways to remove deterministic linear nuisance parameters.
- Carl de Boor, **“Divided Differences,”** *Surveys in Approximation Theory* 1, 46–69 (2005), arXiv:`math/0502036`, and Bengt Fornberg, **“Generation of Finite Difference Formulas on Arbitrarily Spaced Grids,”** *Mathematics of Computation* 51(184), 699–706 (1988), DOI `10.1090/S0025-5718-1988-0935077-0`, provide classical interpolation/finite-difference background. AF-195 already records the exact moment-annihilator statement for generic polynomial nuisance.
- Rick Chartrand, **“Numerical Differentiation of Noisy, Nonsmooth Data,”** *ISRN Applied Mathematics* 2011, article 164564, DOI `10.5402/2011/164564`, is representative prior art for the classical noise amplification inherent in numerical differentiation and the need to account for conditioning when derivative-like observables are formed from noisy values.

No novelty is claimed for linear nuisance projection, reference differencing, divided differences, finite-difference weights, or deterministic error propagation.

The durable Arithmetic Fidelity content is the exact specialization of those ideas to the AF-525 tail carrier: the multiplier family appears unbounded at the first log-slope level (AF-539), yet its exact value-level representation has only one unbounded direction. The unique two-sample annihilator of that direction retains the arithmetic anchor signal at order `hL_A/H_A`, while the entire arbitrary-multiplier remainder is uniformly only `O(h)`. At `h=A^{-1}` this restores the AF-529 signal scale without co-tuning and avoids the extra finite-resolution loss that a generic second-difference realization of AF-540 would incur.

Targeted prior-art searches located the general nuisance-projection, differencing, interpolation, and noisy-differentiation frameworks above; no broad novelty claim is made for the arithmetic specialization merely because the exact formula was not found in those literatures.

## Fidelity / representation audit

This result is a direct instance of the line's central distinction between **how much information is present** and **which representation makes the target survive nuisance compression**.

At a single point, arbitrary multiplier growth dominates the source: `\phi_C(t)` carries an unbounded `(1+t)\log C` component. Passing mechanically to the first derivative does not solve the problem because the derivative of that component remains `\log C`, producing AF-539's threshold. Passing to the second derivative solves it, as AF-540 showed, but asks for a stronger infinitesimal observable.

The two-point functional `(8)` instead uses the exact nuisance geometry. It quotients the one-dimensional unbounded span generated by `1+t` while retaining a target component of order `hL_A/H_A`. The bounded multiplier remainder survives the quotient, but only at order `h`, smaller by the factor `H_A/L_A` after target normalization.

In Arithmetic Fidelity language, the useful lift is therefore not “retain more derivatives” in general. It is “retain enough relational information to form an annihilator of the actual nuisance image.” The required sample count is controlled by the dimension and shape of the dangerous nuisance subspace, not by the nominal polynomial degree of a generic local model.

## Falsification and matched-control audit

1. **Arbitrary multiplier growth is genuinely included.** Bounds `(6)`–`(12)` are uniform over every integer `C_A,\widetilde C_A\ge2`; no hidden AF-525 admissibility or co-tuning condition enters.

2. **The exact multiplier law is essential.** The two-point cancellation uses the decomposition `\phi_C(t)=(1+t)\log C+r_C(t)`. Enlarging the nuisance family to two independent affine coefficients `a+bt`, or to a family whose residual has slope growing with the nuisance parameter, invalidates the two-sample conclusion. AF-195 then supplies the appropriate generic polynomial-annihilator baseline.

3. **Matched non-prime controls remain.** The source limit uses only reciprocal-prime and logarithmically weighted reciprocal-prime asymptotics. A generalized-prime or other matched source reproducing those moment laws can reproduce the same anchor signal. Nothing here isolates rational-prime identity.

4. **The theorem concerns the exact carrier ratio.** AF-525's value-level approximation from normalized curvature defect to this carrier does not automatically transfer the two-point log-contrast at the shrinking `h=A^{-1}` scale. That would require error control strong enough after differencing and logarithmization.

## Boundaries

1. **Coarse anchor exponent only.** The recovered target is fixed `\theta\in(0,1)`, not the exact cutoff, the prime set, the zeta zeros, or RH.

2. **Boundary-layer sampling.** Equation `(2)` is proved for `0<h\le A^{-1}`. Larger windows may have different source asymptotics and are not claimed.

3. **Linear point-sample minimality only.** The one-versus-two sample statement concerns nonzero linear functionals of point values with uniformly bounded arbitrary-multiplier response. It does not rule out a nonlinear one-sample decoder under extra restrictions or side information.

4. **Log-value error model.** Equation `(4)` concerns deterministic additive error in the two observed log-values. Relative/multiplicative error before logarithmization, stochastic sampling noise, correlated error, or quantization can give different thresholds.

5. **Sufficient conditioning threshold.** The `o(L_A/(A H_A))` requirement is sufficient for this contrast decoder. No global minimax lower bound over every possible two-sample decoder with arbitrary nuisance is asserted.

6. **No rational-prime uniqueness.** As in AF-539–AF-540, the theorem is a carrier-fidelity statement inside a source class, not evidence that the carrier distinguishes the rational primes from all matched arithmetic controls.

## Consequence

AF-539's first-derivative obstruction and AF-540's higher-jet escape do not mean that arbitrary multiplier nuisance forces a curvature-level finite observation. The obstruction is representation-dependent: the raw first slope keeps the multiplier's unbounded affine direction, while the weighted two-point value contrast quotients that direction exactly.

For the broader Arithmetic Fidelity program this is a sharper minimal-lift lesson. **Before adding derivative order or extra samples, identify the actual unbounded nuisance image and annihilate that image as economically as possible.** Generic compression-resistant lifts can be strictly more expensive than representation-specific ones, both in sample count and in conditioning.