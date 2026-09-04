# WI-146 — two-point Lamzouri tests admit an arbitrarily small remote positive spectral repair

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`. WI-145 proved that every normalized even scalar kernel `H` entering a universal Lamzouri-form inequality

\[
 s(\mathcal Z)\ge 2|\mathcal Z|-\sum_{z,w\in\mathcal Z}H(z-w)
\tag{1}
\]

must satisfy `H(iy)>=1` on every imaginary gap, and therefore cannot have a genuine eventually non-positive outer Fourier profile with negative mass farther out than all positive mass. A natural strengthening would be to hope that the complete two-point tests already force Fourier positivity, or at least forbid any negative profile mass.

That strengthening is false. The two-point tests are exactly

\[
\boxed{H(x)\ge0\quad(x\in\mathbb R),\qquad H(iy)\ge1\quad(y\in\mathbb R),}
\tag{2}
\]

and there are explicit normalized real-even **signed** Fourier profiles with a fixed negative intermediate band that satisfy both conditions. For every prescribed negative mass `A>0` and every `epsilon>0`, one can put an arbitrarily small positive mass `<epsilon` sufficiently farther out in frequency so that its hyperbolic growth repairs the imaginary-axis condition while leaving the real-axis kernel nonnegative. The construction can be smoothed to a compactly supported `C_c^infinity` profile without losing either inequality.

Thus the outer-tail hypothesis in WI-145 is load-bearing: one conjugate pair detects an uncompensated negative outer tail, but it cannot rule out a negative band protected by farther-out positive spectral mass. Any stronger universal scalar obstruction must use at least multi-point configurations or an independent arithmetic/analytic bound on the cost of the remote repair. No new zeta-zero proportion is claimed.

## 1. The complete two-element necessary tests

Assume `H` is even, `H(0)=1`, is real on the real and imaginary axes, and that (1) holds for every finite conjugation-invariant multiset. There are only three nontrivial types of conjugation-invariant multisets of cardinality at most two.

For two distinct simple real points, translate to

\[
\mathcal Z=\{0,x\},\qquad x\in\mathbb R\setminus\{0\}.
\]

Then `s(Z)=2` and

\[
\sum_{z,w\in\mathcal Z}H(z-w)=2+2H(x),
\]

so (1) gives

\[
2\ge4-(2+2H(x))=2-2H(x),
\]

hence

\[
\boxed{H(x)\ge0.}
\tag{3}
\]

For one non-real conjugate pair,

\[
\mathcal Z=\{iy/2,-iy/2\},\qquad y\ne0,
\]

we have `s(Z)=0` and the same calculation on the imaginary gap gives WI-145's condition

\[
\boxed{H(iy)\ge1.}
\tag{4}
\]

A doubled real point has `s=0` and pair sum `4H(0)=4`, so (1) is an equality and adds no condition. A singleton is necessarily real and again gives equality from `H(0)=1`. Therefore (3)--(4), together with normalization, are the **complete necessary conditions visible to all multisets of cardinality at most two**.

This observation is independent of any Gram representation or zeta asymptotic. It concerns only the finite zero-side inequality that a proposed scalar replacement would have to satisfy.

## 2. An exact atomic signed repair

Fix

\[
A>0,\qquad 0<a<R,
\]

and define

\[
B:=A\left(\frac aR\right)^2.
\tag{5}
\]

Consider the normalized even signed probability measure

\[
\mu=(1+A-B)\delta_0
-\frac A2(\delta_a+\delta_{-a})
+\frac B2(\delta_R+\delta_{-R}).
\tag{6}
\]

Its total mass is exactly one. It contains fixed negative mass `A` at the intermediate frequencies `+-a`, compensated in total mass mostly at the origin and by only `B` positive mass at the more remote frequencies `+-R`.

With Fourier convention

\[
H_\mu(z)=\int_{\mathbb R}e^{-2\pi i z u}\,d\mu(u),
\tag{7}
\]

we have on the real axis

\[
H_\mu(x)
=1+A\bigl(1-\cos(2\pi a x)\bigr)
-B\bigl(1-\cos(2\pi R x)\bigr).
\tag{8}
\]

The `A` term is nonnegative and `0<=1-cos(theta)<=2`, so

\[
\boxed{H_\mu(x)\ge1-2B.}
\tag{9}
\]

Consequently `B<1/2` implies strict real-axis positivity for every `x`.

On the imaginary axis,

\[
H_\mu(iy)
=1-A\bigl(\cosh(2\pi a y)-1\bigr)
+B\bigl(\cosh(2\pi R y)-1\bigr).
\tag{10}
\]

For `0<a<R`, monotonicity of `sinh(t)/t` on `(0,infinity)` gives, for every real `y`,

\[
\sinh(\pi a|y|)
\le \frac aR\sinh(\pi R|y|).
\tag{11}
\]

Squaring and using `cosh(2t)-1=2sinh^2(t)` yields

\[
\cosh(2\pi a y)-1
\le
\left(\frac aR\right)^2
\bigl(\cosh(2\pi R y)-1\bigr).
\tag{12}
\]

By the definition (5) of `B`, (10)--(12) imply

\[
\boxed{H_\mu(iy)\ge1\qquad(y\in\mathbb R).}
\tag{13}
\]

The amount of remote repair can be made arbitrarily small while the intermediate negative mass stays fixed. Given any `epsilon>0`, choose

\[
R>a\sqrt{A/\epsilon}.
\]

Then `B<epsilon`; increasing `R` further if necessary also gives `B<1/2`, so both (9) and (13) hold. This is the central exact counterexample to the hoped-for strengthening of WI-145.

The mechanism is simple but asymmetric. Oscillation makes a remote mass cost at most `2B` on the real Fourier axis, whereas on the imaginary axis its bilateral-Laplace contribution grows at scale `cosh(2 pi R y)`. Choosing `B` only quadratically small in `R` is already enough to dominate the intermediate negative contribution uniformly for every imaginary gap.

## 3. Smooth compactly supported realization

The atomic example is not an artifact of distributions. Let `r in C_c^infinity(R)` be real and nonnegative with

\[
\int_{\mathbb R}r(u)\,du=1,
\]

put `r_tilde(u)=r(-u)`, and set

\[
\rho=r*r_{\rm tilde}.
\tag{14}
\]

Then `rho` is real, even, nonnegative, smooth, compactly supported, and has total mass one. Its Fourier transform obeys

\[
\widehat\rho(x)=|\widehat r(x)|^2\ge0
\qquad(x\in\mathbb R),
\tag{15}
\]

while evenness and nonnegativity give

\[
\widehat\rho(iy)
=\int_{\mathbb R}\rho(u)\cosh(2\pi yu)\,du
\ge1
\qquad(y\in\mathbb R).
\tag{16}
\]

Now define the signed smooth profile

\[
\phi:=\mu*\rho.
\tag{17}
\]

It is real-even, belongs to `C_c^infinity(R)`, and has integral one. Its entire Fourier transform factors as

\[
\widehat\phi(z)=H_\mu(z)\widehat\rho(z).
\tag{18}
\]

Equations (9), (13), (15), and (16) therefore give

\[
\boxed{\widehat\phi(x)\ge0\quad(x\in\mathbb R),\qquad
\widehat\phi(iy)\ge1\quad(y\in\mathbb R)}
\tag{19}
\]

whenever `B<1/2`.

Choose the support radius of `rho` smaller than both `a` and `R-a`. Then the five translates in (17) are disjoint. Around `+-a`, the profile is exactly `-(A/2)rho` and hence has genuine negative intermediate bands of total negative mass `A`; around `+-R` it has positive remote bands of total mass `B`. Since `B` can be made smaller than any prescribed `epsilon`, (19) is compatible with a fixed amount of sign-indefinite spectral mass and an arbitrarily small farther-out repair.

One may additionally choose `a>1` and the smoothing radius below `a-1`, placing the negative band entirely outside the usual support-one arithmetic region and the positive repair still farther out. This is only a structural observation. It does **not** make such a profile usable in the unconditional zeta argument: controlling the prime side at those larger Fourier radii is precisely an additional arithmetic problem.

## 4. What WI-145 does and does not force

WI-145 remains correct without modification. Its hypothesis was stronger than mere sign change: after some radius, the Fourier profile was assumed to contain no positive mass while retaining genuine negative mass farther out. Under that ordering, bilateral-Laplace growth forces `H(iy)->-infinity`, contradicting a single conjugate pair.

The present construction shows that this radial ordering is essential. If any positive repair is allowed at a larger radius than the negative band, hyperbolic growth can reverse the conclusion. In particular,

\[
\boxed{\text{the complete two-point Lamzouri tests do not force Fourier positivity.}}
\tag{20}
\]

They do not even impose a quantitative upper bound on the total intermediate negative mass: `A` is arbitrary, while the repair mass `B=A(a/R)^2` can be driven to zero by moving it outward.

This also explains why replacing the fixed-kernel conclusion of WI-145 by a naive compactness argument is unsafe. Small total variation at very large spectral radius is cheap on the real axis but is not small for imaginary gaps. Any `T`-dependent proposal that sends positive repair to radii `R=R(T)` therefore needs a **uniform prime-side and off-line analysis**; total spectral mass alone is not the correct control parameter.

## 5. Prior-art audit and novelty boundary

The primary finite-inequality source remains Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1, Proposition 2.1. Chirre--Gonçalves--de Laat, *Pair Correlation Estimates for the Zeros of the Zeta Function via Semidefinite Programming*, Advances in Mathematics 361 (2020), 106926, arXiv:1810.08843v2, remains the relevant source for RH-conditional test functions with a favorable negative outer Fourier region. WI-143--WI-145 already audited why their mechanism does not pass directly through Lamzouri's positive-Hilbert zero-side certificate.

The current `weil_inertia` corpus was searched for the two-point conditions, signed spectral repairs, remote positive compensation, and `T`-dependent signed kernels. The closest stored result is WI-145 itself, which explicitly leaves profiles with positive mass farther out outside its theorem. The public `teal-sea/zeta-lab` interaction-control audit likewise emphasizes that a scalar/global census can miss signed on/off interactions and calls for richer incidence information; it does not supply the construction (6) or the exact uniform inequalities (9), (13).

Broader searches around Fourier sign uncertainty, positive-definite kernels, idempotent/trigonometric-polynomial concentration, and the CGdL/Lamzouri mechanisms did not locate a published formulation of this exact remote-repair counterexample. No priority claim is made. Classical ingredients used here include monotonicity of `sinh(t)/t`, Fourier transforms of signed measures, autocorrelation smoothing, and the elementary classification of two-element conjugation-invariant multisets.

The Mathia contribution recorded here is therefore deliberately narrow: **WI-145 cannot be strengthened from “no uncompensated negative outer tail” to “no signed spectral profile” using only one- and two-element zero configurations.** The explicit family (6) proves the failure and quantifies how cheaply a remote positive repair can evade those tests.

## Research consequence

The weak route “use pair tests to force Fourier positivity of every universal Lamzouri-form scalar kernel” should be treated as closed. A sign-changing scalar profile is not excluded merely by real-axis nonnegativity plus the single-conjugate-pair condition.

There are two materially different next gates. On the zero side, one must use multisets with at least three elements, where the kernel values are coupled by nontrivial trigonometric-polynomial/incidence constraints rather than tested one gap at a time. On the arithmetic side, one can try to prove that moving the compensating positive mass to a large radius has a source-specific cost that cannot remain negligible in the explicit formula. Either route retains information that the complete two-point audit provably discards.

This is a structural redirect and a decisive negative result for a proposed strengthening of WI-145, not a new unconditional percentage and not a proof that the constructed signed profile satisfies the full universal inequality (1). Passing every two-element necessary test is only a necessary-filter result; multi-point configurations may still rule the profile out.