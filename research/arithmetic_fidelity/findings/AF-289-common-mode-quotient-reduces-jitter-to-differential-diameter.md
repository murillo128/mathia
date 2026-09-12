# AF-289 — Common-mode quotient reduces rowwise jitter to differential timing diameter

**Status:** `EXACT-DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `JOINT-SAMPLING`, `TIMING`, `GAUGE-QUOTIENT`, `TARGET-RELATIVE`, `STABILITY`, `NO-NOVELTY-CLAIM`

## Claim

AF-287 proves stable recovery of a known Dirichlet prefix from an unweighted `O(N)` two-prime sampling frame when every row timing error obeys an absolute bound `|tau_j| <= T`. AF-288 then shows that a **common** timing offset is a gauge: it acts on coefficients by

\[
G_\sigma b=(b_n n^{-i\sigma})_{n=1}^N,
\]

and some downstream targets, including horizontal zero geometry of an exact vertically translated analytic carrier, are invariant under that gauge.

The two statements combine into a sharper target-relative timing law. For an arbitrary rowwise timing-error vector

\[
\tau=(\tau_1,\ldots,\tau_q)\in\mathbb R^q,
\]

define its common-mode quotient radius

\[
r(\tau)
:=\inf_{\sigma\in\mathbb R}\max_j|\tau_j-\sigma|
=\frac{\max_j\tau_j-\min_j\tau_j}{2}.
\]

Let `A` be any nominal sampling matrix with full column rank and condition number `kappa(A)<=K`, and let

\[
\widetilde A(\tau)_{j,n}
=A_{j,n}e^{-i\tau_j\log n}.
\]

Then, with the nominal decoder

\[
\widehat b=A^\dagger\widetilde A(\tau)b,
\]

the coefficient vector is recovered **modulo common clock gauge** with the bound

\[
\boxed{
\inf_{\sigma\in\mathbb R}
\frac{\|\widehat b-G_\sigma b\|_2}{\|b\|_2}
\le
K\left(e^{r(\tau)\log N}-1\right)
}
\]

for every nonzero `b`.

Consequently, to guarantee quotient-relative coefficient distortion at most `rho>0`, it is sufficient that

\[
\boxed{
\operatorname{osc}(\tau)
:=\max_j\tau_j-\min_j\tau_j
\le
\frac{2\log(1+\rho/K)}{\log N}.
}
\]

There is **no bound at all on the absolute common timing component**. All offsets may be translated together by an arbitrarily large amount without changing the quotient error. The timing resource seen by a common-clock-invariant target is therefore the differential jitter diameter, not the distance of the timing vector from the nominal origin.

The same quotient radius controls frame injectivity. If

\[
K\left(e^{r(\tau)\log N}-1\right)<1,
\]

then `\widetilde A(\tau)` remains full column rank. Thus an arbitrarily large common offset does not degrade the singular values; only the residual offsets after removing the best common mode do.

This is a target-relative refinement of AF-287, not a stronger full-coefficient recovery theorem. If the downstream target depends on absolute coefficient phase or absolute imaginary origin, AF-286's common-clock calibration cost remains relevant. If the target descends to the common-clock quotient, that cost disappears exactly and only the differential timing component remains to be controlled.

## Exact quotient decomposition

For any chosen `sigma in R`, write

\[
\tau_j=\sigma+\varepsilon_j.
\]

Then row by row,

\[
\begin{aligned}
\widetilde A(\tau)_{j,n}
&=A_{j,n}e^{-i(\sigma+\varepsilon_j)\log n}\\
&=A_{j,n}e^{-i\varepsilon_j\log n}e^{-i\sigma\log n}.
\end{aligned}
\]

Therefore

\[
\boxed{
\widetilde A(\tau)=\widetilde A(\varepsilon)G_\sigma.
}
\]

This factorization is exact. It separates rowwise timing error into:

- a right-unitary coefficient gauge `G_sigma`, common to every row; and
- a residual timing vector `epsilon`, which is the genuinely differential perturbation of the acquisition frame.

The best `ell^infinity` residual is obtained by minimizing

\[
\max_j|\tau_j-\sigma|.
\]

Let

\[
m=\min_j\tau_j,
\qquad
M=\max_j\tau_j.
\]

For every `sigma`,

\[
M-m
\le |M-\sigma|+|\sigma-m|
\le 2\max_j|\tau_j-\sigma|,
\]

so

\[
\max_j|\tau_j-\sigma|\ge\frac{M-m}{2}.
\]

The midpoint

\[
\sigma_*=\frac{M+m}{2}
\]

attains equality. Hence

\[
\boxed{
r(\tau)=\frac{\operatorname{osc}(\tau)}2.
}
\]

This is the exact `ell^infinity` quotient distance from the timing vector to the one-dimensional common-clock subspace.

## Quotient recovery bound

Choose the optimal common mode `sigma_*` and put

\[
\varepsilon_j=\tau_j-\sigma_*.
\]

Then

\[
\|\varepsilon\|_\infty=r(\tau).
\]

Set

\[
c=G_{\sigma_*}b.
\]

Because `G_{sigma_*}` is unitary,

\[
\|c\|_2=\|b\|_2.
\]

The observed samples satisfy

\[
\widetilde A(\tau)b
=\widetilde A(\varepsilon)c.
\]

AF-287's matrix-level perturbation argument applies to the residual timing vector and gives

\[
\|\widetilde A(\varepsilon)-A\|_{2\to2}
\le
\|A\|_{2\to2}
\left(e^{r(\tau)\log N}-1\right).
\]

The nominal decoder therefore obeys

\[
\begin{aligned}
\|\widehat b-c\|_2
&=\|A^\dagger(\widetilde A(\varepsilon)-A)c\|_2\\
&\le
\|A^\dagger\|\,\|A\|
\left(e^{r(\tau)\log N}-1\right)\|c\|_2\\
&\le
K\left(e^{r(\tau)\log N}-1\right)\|b\|_2.
\end{aligned}
\]

Since `c=G_{sigma_*}b` belongs to the common-clock orbit of `b`, minimizing over the whole orbit can only improve this estimate. Thus

\[
\inf_{\sigma\in\mathbb R}
\frac{\|\widehat b-G_\sigma b\|_2}{\|b\|_2}
\le
K\left(e^{r(\tau)\log N}-1\right).
\]

The right side depends on the **diameter of the timing-error cloud** and is completely independent of its center.

## Frame stability also lives on the timing quotient

The exact factorization

\[
\widetilde A(\tau)=\widetilde A(\varepsilon)G_{\sigma_*}
\]

shows immediately that

\[
\sigma_k(\widetilde A(\tau))
=\sigma_k(\widetilde A(\varepsilon))
\]

for every singular value. An arbitrary common offset is therefore spectrally invisible to the acquisition matrix.

By Weyl's inequality and AF-287's perturbation estimate,

\[
\begin{aligned}
\sigma_{\min}(\widetilde A(\tau))
&\ge
\sigma_{\min}(A)
-\|A\|\left(e^{r(\tau)\log N}-1\right)\\
&\ge
\sigma_{\min}(A)
\left[1-K\left(e^{r(\tau)\log N}-1\right)\right].
\end{aligned}
\]

Hence

\[
K\left(e^{r(\tau)\log N}-1\right)<1
\]

is a sufficient quotient-relative injectivity condition. The frame may be centered at any absolute timing origin; only its residual row-to-row timing spread enters.

## Target-relative interpretation

Define the coefficient orbit pseudometric

\[
d_G(b,b')
:=
\inf_{\sigma\in\mathbb R}
\frac{\|b'-G_\sigma b\|_2}{\|b\|_2},
\qquad b\ne0.
\]

AF-289 proves a bound on this quotient error, not on ordinary coefficient error. Therefore the correct downstream implication depends on the target.

If a target `Phi` satisfies

\[
\Phi(G_\sigma b)=\Phi(b)
\qquad\text{for all }\sigma,
\]

then common timing origin is nuisance provenance rather than target information. If, in addition, the target has a quantitative stability modulus on the quotient, for example

\[
d_{\mathcal T}(\Phi(b),\Phi(b'))
\le
\omega(d_G(b,b')),
\]

then

\[
d_{\mathcal T}(\Phi(b),\Phi(\widehat b))
\le
\omega\!\left(
K(e^{r(\tau)\log N}-1)
\right).
\]

The theorem does not assert that every interesting arithmetic target has such a modulus. It says that **the common timing mode must be quotiented before pricing timing precision whenever the target itself is gauge-invariant**.

AF-288 supplies the canonical motivating example at the analytic-carrier level. For an exact Dirichlet-series object, common timing offset corresponds to vertical translation `F(s)->F(s+i sigma)`, and horizontal zero geometry is unchanged. In that setting the RH yes/no predicate is constant on the common-clock orbit. AF-289 does not convert finite-prefix coefficient recovery into analytic continuation or a zero-location theorem; it only identifies which part of rowwise timing uncertainty is relevant after the target's exact gauge symmetry has been recognized.

## Prior art and novelty assessment

No novelty is claimed for subtracting a common mode, quotienting a nuisance group action, orbit recovery, sampling-jitter perturbation analysis, or the midpoint formula for the smallest enclosing interval.

Recovery only up to a group action is a standard formulation in orbit-recovery and invariant-estimation problems, and timing jitter is classically analyzed through frequency-sensitive phase perturbations in sampled signals. The present theorem does not introduce either idea. Its retained Arithmetic Fidelity content is the exact bridge between the two already-established local results: AF-287's bounded-condition Dirichlet frame estimate is naturally a statement about **distance to the common-clock orbit**, while AF-288 identifies when that orbit is invisible to the downstream target.

The useful distinction is therefore not a new general theorem of invariant theory. It is a resource correction inside this arithmetic channel: an absolute constraint `max_j|tau_j|<=T` overprices timing precision for gauge-invariant targets. The intrinsic `ell^infinity` resource is instead

\[
\inf_\sigma\max_j|\tau_j-\sigma|
=\frac{\operatorname{osc}(\tau)}2.
\]

## Boundaries and failure modes

- The source support remains the known finite prefix `1,...,N`; unknown support and infinite Dirichlet sources are not covered.
- The decoder is the nominal least-squares decoder for a bounded-condition frame of the type supplied by AF-287. No claim is made for arbitrary acquisition designs.
- The displayed differential-jitter bound is **sufficient**, not proved sharp. AF-287's common-offset lower bound disappears after quotienting, so it cannot provide a matching lower bound in this target-relative geometry.
- The half-range formula is exact only for the declared `ell^infinity` timing metric. Other stochastic, weighted, or quadratic timing models have different quotient radii.
- A target must genuinely be invariant under the common-clock action before the absolute timing mode can be discarded. Absolute coefficient phases, exact zero ordinates, fixed-height windows, and canonical completed-function normalizations generally retain that provenance.
- Exact invariance does not imply quantitative stability under residual jitter. A discontinuous or badly conditioned quotient target may still require substantially stronger control than the coefficient-orbit estimate alone suggests.
- AF-288's RH observation concerns an exact analytic carrier up to vertical translation. AF-289 does not establish that finitely many noisy samples determine that carrier, its analytic continuation, or its zero divisor.
- No new zero-free region, zero-density estimate, critical-line proportion, or proof of RH follows.

## Decisive audit test

When a proposed arithmetic acquisition mechanism assigns a timing-precision cost from rowwise errors `tau_j`, first identify the nuisance symmetry of the final target.

If common clock translation is target-invariant, replace the absolute timing radius

\[
\max_j|\tau_j|
\]

by the quotient radius

\[
\inf_\sigma\max_j|\tau_j-\sigma|
=\frac{\max_j\tau_j-\min_j\tau_j}{2}.
\]

Only the latter measures timing information that survives the common-mode quotient. A claimed calibration obstruction based solely on a large absolute clock offset is therefore spurious for such a target. Any stronger obstruction must arise from residual row-to-row timing spread, target instability on the quotient, source uncertainty, or another non-gauge acquisition defect.

## Consequence for the research line

The finite-prefix timing picture now separates cleanly into three layers.

1. AF-286 prices common-clock uncertainty for full coefficient recovery: `Theta(1/log N)` absolute calibration is required when absolute phase matters.
2. AF-287 shows arbitrary independent rowwise jitter has the same `Theta(1/log N)` order for full coefficient recovery on a bounded-condition `O(N)` frame.
3. AF-288 and AF-289 show that a common component is free whenever the target descends through vertical translation; after that quotient, the relevant acquisition resource is only the differential timing diameter.

The remaining timing frontier is therefore no longer “how accurately must the absolute clock origin be known?” for every target. It is to determine, target by target, which non-common timing perturbations remain visible after quotienting all exact nuisance symmetries and what stability modulus those downstream arithmetic targets possess on the resulting quotient geometry.
