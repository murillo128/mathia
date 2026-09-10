# AF-255 — Keiper height couples growth and cancellation scales

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `LI-DOMINANT-MODE-CONTROL`, `DIOPHANTINE-FIDELITY`, `TARGET-METRIC`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

For a hypothetical off-critical zero

\[
\rho=\beta+i\gamma,
\qquad \frac12<\beta<1,
\qquad \gamma>0,
\tag{1}
\]

the Keiper conformal image

\[
a_\rho=1-\frac1\rho
=r_\rho e^{i\theta_\rho},
\qquad 0<r_\rho<1,
\qquad q_\rho=r_\rho^{-1}>1,
\tag{2}
\]

does not carry an independent radial growth rate and angular cancellation frequency. Both are rigid functions of the same zero coordinates. In fact

\[
\boxed{
r_\rho^2
=1-\frac{2\beta-1}{\beta^2+\gamma^2}
}
\tag{3}
\]

and

\[
\boxed{
\theta_\rho
=
\arctan\frac{\beta}{\gamma}
+
\arctan\frac{1-\beta}{\gamma}.
}
\tag{4}
\]

Writing

\[
\delta=\beta-\frac12>0,
\tag{5}
\]

gives the exact useful bounds

\[
\boxed{
\frac{\delta}{\beta^2+\gamma^2}
\le \log q_\rho
\le
\frac{\delta}{(1-\beta)^2+\gamma^2}
}
\tag{6}
\]

and

\[
\boxed{
\frac{\gamma}{\gamma^2+1}
\le \theta_\rho
\le \frac1\gamma.
}
\tag{7}
\]

Consequently, for fixed `beta` and `gamma -> infinity`,

\[
\theta_\rho
=\frac1\gamma+O_\beta(\gamma^{-3}),
\qquad
\log q_\rho
=\frac{\delta}{\gamma^2}+O_\beta(\gamma^{-4}),
\tag{8}
\]

so

\[
\boxed{
\frac{\log q_\rho}{\theta_\rho^2}
\longrightarrow
\beta-\frac12.
}
\tag{9}
\]

This coupling changes the relevant fidelity target from an absolute cancellation condition to a **growth-normalized cancellation margin**.

For one conjugate dominant pair of multiplicity `m`, the normalized angular mode is

\[
F_\rho(n)=-2m\cos(n\theta_\rho).
\tag{10}
\]

Assume `alpha_rho=theta_rho/pi` is irrational and let `S subset N` be unbounded. Define, as in AF-249,

\[
\tau_\rho(S)
=
\liminf_{\substack{n\to\infty\\n\in S}}
\frac{-\log\operatorname{dist}
(n\alpha_\rho,\mathbb Z+\tfrac12)}{n}.
\tag{11}
\]

Then AF-249 and `(2)` give the exact pair-level root rate

\[
\boxed{
\limsup_{\substack{n\to\infty\\n\in S}}
\left|q_\rho^nF_\rho(n)\right|^{1/n}
=
\exp\!\left(\log q_\rho-\tau_\rho(S)\right).
}
\tag{12}
\]

Therefore the off-critical pair remains superunit at the RH root-rate threshold exactly when

\[
\boxed{
\tau_\rho(S)<\log q_\rho,
}
\tag{13}
\]

while the pair can be reduced to unit root rate or below when

\[
\tau_\rho(S)\ge\log q_\rho.
\tag{14}
\]

Full-rate fidelity `q_rho` still requires `tau_rho(S)=0`, but **mere detectability of the pair is a weaker, source-scaled condition**. By `(6)`, its critical cancellation exponent is only of order

\[
\frac{\beta-1/2}{\gamma^2}.
\tag{15}
\]

Thus high off-critical zeros close to the critical line are intrinsically ill-conditioned for sparse root-rate observation: the radial exponential excess above one is quadratic in inverse height, whereas the angular step is only linear in inverse height.

There is also a finite-horizon separation. For every fixed `0<c<pi/2`,

\[
1\le n\le c\gamma
\quad\Longrightarrow\quad
|F_\rho(n)|\ge 2m\cos c,
\tag{16}
\]

because `(7)` gives `n theta_rho <= c`. On the same range, `(6)` gives

\[
1\le q_\rho^n
\le
\exp\!\left(\frac{c\delta}{\gamma}\right).
\tag{17}
\]

So height buys a linear prefix free of phase cancellation precisely in a regime where essentially no radial exponential amplification has accumulated. The angular timescale is `Theta(gamma)`, while one radial e-fold is `Theta(gamma^2/delta)`.

Finally, this conditioning cannot be repaired by **coarse zero location alone**. For every finite height threshold `H>0`, there exists a symmetry-compatible off-critical quartet with `beta=3/4`, `gamma>H`, and a super-Liouville Keiper phase for which a periodically complete retained set has `tau_rho(S)=+infinity`. Hence the pair contribution in `(12)` has restricted root rate zero despite `q_rho>1`. More generally, any right-edge exclusion of the form

\[
\beta>1-\eta(\gamma),
\qquad \eta(\gamma)\longrightarrow0,
\tag{18}
\]

still admits these controls at sufficiently large height because `beta=3/4 <= 1-eta(gamma)` eventually. A finite verified-height cutoff or a shrinking right-edge zero-free region therefore cannot, by itself, supply the Diophantine fidelity demanded by `(13)`.

## Why it matters

AF-244--AF-250 separated sparse output sampling from the source depth needed to form Li coefficients and identified exponential phase cancellation as the exact output-side obstruction. AF-249 then gave the one-pair invariant `tau`, while AF-253--AF-254 generalized the cancellation geometry to affine multimode fibers. Those results deliberately treated the angular cancellation problem after the dominant radial rate `q` had already been isolated.

The present result puts those two pieces back together for an actual Keiper image. The radial distance from the unit circle and the phase step are not independent adversarial parameters. Equation `(9)` shows the exact high-zero scaling: an off-line displacement `delta` produces a radial log-growth gap of order `delta theta^2`. Consequently, the amount of exponential cancellation needed merely to hide the **existence** of an off-RH pair becomes smaller as its height increases or as it approaches the critical line.

This exposes a uniformity requirement that was easy to miss when asking only whether `tau=0` generically. A source theorem giving a fixed positive upper bound on cancellation exponents is not enough uniformly over hypothetical off-RH zeros, because `log q_rho` can approach zero. A family-level detector needs either the strongest condition `tau_rho(S)=0` or a genuinely source-coupled estimate of the form

\[
\tau_\rho(S)
<\log q_\rho
\asymp
\frac{\beta-1/2}{\gamma^2}
\tag{19}
\]

for every relevant dominant pair. This is a quantitative conditioning statement, not merely a genericity question.

## Exact derivation

### 1. The radial excess is the off-line displacement divided by height squared

From `(2)`,

\[
a_\rho
=\frac{\rho-1}{\rho}.
\tag{20}
\]

Therefore

\[
r_\rho^2
=\frac{(1-\beta)^2+\gamma^2}{\beta^2+\gamma^2}
=1-\frac{2\beta-1}{\beta^2+\gamma^2},
\tag{21}
\]

which proves `(3)` and also `r_rho<1` for `beta>1/2`.

Put

\[
x=\frac{2\beta-1}{\beta^2+\gamma^2}\in(0,1).
\tag{22}
\]

Then

\[
\log q_\rho
=-\log r_\rho
=-\frac12\log(1-x).
\tag{23}
\]

The elementary bounds

\[
x\le-\log(1-x)\le\frac{x}{1-x}
\tag{24}
\]

give

\[
\frac{2\beta-1}{2(\beta^2+\gamma^2)}
\le\log q_\rho
\le
\frac{2\beta-1}
{2((1-\beta)^2+\gamma^2)},
\tag{25}
\]

which is `(6)`.

### 2. The phase is a sum of the two endpoint angles

For `gamma>0`,

\[
\arg(\rho)
=\frac\pi2-\arctan\frac{\beta}{\gamma},
\tag{26}
\]

whereas

\[
\arg(\rho-1)
=\frac\pi2+\arctan\frac{1-\beta}{\gamma}.
\tag{27}
\]

Subtracting gives `(4)`. Since for `x>=0`

\[
\frac{x}{1+x^2}\le\arctan x\le x,
\tag{28}
\]

we obtain

\[
\theta_\rho
\le
\frac{\beta}{\gamma}
+
\frac{1-\beta}{\gamma}
=\frac1\gamma.
\tag{29}
\]

For the lower bound, each denominator in `(28)` is at most `1+1/gamma^2`, so

\[
\theta_\rho
\ge
\frac{1/\gamma}{1+1/\gamma^2}
=\frac{\gamma}{\gamma^2+1}.
\tag{30}
\]

This proves `(7)`. Taylor expansion of `(4)` and `(23)` gives `(8)` and hence `(9)`.

### 3. The correct pair-level conditioning parameter is relative to `log q`

AF-249 proves for irrational `alpha_rho` that

\[
\limsup_{\substack{n\to\infty\\n\in S}}
|F_\rho(n)|^{1/n}
=e^{-\tau_\rho(S)}.
\tag{31}
\]

Multiplication by the fixed exponential factor `q_rho^n` gives `(12)` immediately. The RH root-rate boundary is one, so the pair's contribution remains strictly superunit exactly when

\[
q_\rho e^{-\tau_\rho(S)}>1,
\tag{32}
\]

which is equivalent to `(13)`. This distinguishes two targets that should not be conflated:

- preserving the exact dominant rate `q_rho` requires `tau_rho(S)=0`;
- preserving only an off-RH superunit witness requires the weaker `tau_rho(S)<log q_rho`.

If a full Li decomposition has remainder root rate `eta<q_rho`, then `(12)` transfers unchanged to the full sequence whenever `q_rho e^{-tau_rho(S)}>eta`; in that case the pair still dominates on a subsequence realizing its root limsup. If the remainder has root rate at least that large, `(12)` alone is only a statement about the pair contribution and no whole-sequence conclusion is justified.

### 4. A high zero has a safe angular prefix but essentially no growth on it

Fix `0<c<pi/2`. If `n<=c gamma`, equation `(29)` gives

\[
0<n\theta_\rho\le c<\frac\pi2,
\tag{33}
\]

and therefore

\[
|\cos(n\theta_\rho)|\ge\cos c.
\tag{34}
\]

This proves `(16)`. The upper bound in `(6)` and `n<=c gamma` give

\[
n\log q_\rho
\le
\frac{c\gamma\delta}{\gamma^2+(1-\beta)^2}
\le
\frac{c\delta}{\gamma},
\tag{35}
\]

which proves `(17)`.

Thus the first `Theta(gamma)` angular window is robust against cancellation, but its radial amplification tends to one as `gamma` grows. Conversely the radial e-fold scale satisfies

\[
(\log q_\rho)^{-1}
=\Theta_\beta(\gamma^2/\delta),
\tag{36}
\]

while `theta_rho^{-1}=Theta(gamma)`. For fixed `beta>1/2`, the number of angular oscillations occurring before one radial e-fold therefore grows linearly with `gamma`.

### 5. Arbitrarily high location-admissible controls can still be maximally cancellation-prone

The AF-248 nested odd-denominator construction can be localized inside any nonempty interval `(0,epsilon)`: enumerate every residue condition `(q,r)` infinitely often, choose increasingly large `n_j congruent r (mod q)`, and choose odd numerators `p_j` so that

\[
\alpha_j=\frac{p_j}{2n_j}
\tag{37}
\]

increase inside the chosen interval while the future tail is bounded by

\[
0<\alpha-\alpha_j
\le
\frac{e^{-n_j^2}}{16n_j}.
\tag{38}
\]

Exactly as in AF-248, the limit `alpha` is irrational, `S={n_j}` is periodically complete, and

\[
\operatorname{dist}
(n_j\alpha,\mathbb Z+\tfrac12)
\le\frac1{16}e^{-n_j^2},
\tag{39}
\]

so `tau_alpha(S)=+infinity`.

Now fix `beta=3/4`, put `theta=pi alpha`, and choose `alpha<1/2`. For a point `rho=3/4+i gamma`, direct expansion of `(20)` gives

\[
\tan\theta
=\frac{\gamma}{\gamma^2-3/16}.
\tag{40}
\]

Conversely, for every sufficiently small positive `theta`, setting

\[
\gamma(\theta)
=
\frac{1+\sqrt{1+\tfrac34\tan^2\theta}}
{2\tan\theta}
\tag{41}
\]

solves `(40)` with `gamma>0`; moreover

\[
\gamma(\theta)>\frac1{\tan\theta}
\longrightarrow\infty
\qquad(\theta\downarrow0).
\tag{42}
\]

Hence the interval in the localized AF-248 construction can be chosen small enough that `gamma(theta)>H` for any prescribed finite `H`. The resulting quartet

\[
\rho,\ \bar\rho,\ 1-\rho,\ 1-\bar\rho
\tag{43}
\]

has the elementary zeta symmetries, lies off the critical line, has arbitrarily large ordinate, and has exactly the super-Liouville normalized phase used in `(39)`. Equation `(12)` then gives restricted pair root rate zero.

Finally, if `eta(gamma)->0`, choose the same control at sufficiently large `gamma` that `eta(gamma)<1/4`. Then

\[
\beta=\frac34<1-\eta(\gamma),
\tag{44}
\]

so any exclusion confined to the shrinking right edge `(18)` leaves the control admissible. The argument uses no numerical value of a known zero-free-region constant.

## Prior-art audit

The Keiper conformal map `z=1-1/s`, the correspondence between off-critical zeros and singularities inside the unit disk, and the resulting non-tempered oscillatory Li asymptotics are classical. André Voros, **“Sharpenings of Li's Criterion for the Riemann Hypothesis,”** *Mathematical Physics, Analysis and Geometry* 9 (2006), 53--63, DOI `10.1007/s11040-005-9002-8`, is the principal source already used in AF-244 and AF-248--AF-250. Juan Arias de Reyna, **“Asymptotics of Keiper-Li coefficients,”** *Functiones et Approximatio Commentarii Mathematici* 45(1) (2011), 7--21, DOI `10.7169/facm/1317045228`, is neighboring asymptotic Li-coefficient literature. No novelty is claimed for the conformal map, Li criterion, or the elementary identities `(3)`--`(8)` in isolation.

The exponential Diophantine scale in `(11)` is the AF-249 specialization of Jonathan Sondow's irrationality-base framework; Sondow, **“Irrationality Measures, Irrationality Bases, and a Theorem of Jarnik,”** arXiv:`math/0406300` (2004), supplies the classical exponential rational-approximation language. AF-248 already supplies the super-Liouville matched-control construction used in localized form above.

Modern Vinogradov--Korobov zero-free regions are examples of right-edge exclusions of the abstract type `(18)`. For context, Michael J. Mossinghoff, Timothy S. Trudgian, and Andrew Yang, **“Explicit zero-free regions for the Riemann zeta-function,”** *Research in Number Theory* 10, 11 (2024), DOI `10.1007/s40993-023-00498-y`, prove explicit regions whose width from `Re(s)=1` tends to zero with height. The present result proves no new zero-free region; it shows structurally why such one-zero location information cannot by itself control the exponential Diophantine phase condition required by sparse Li sampling.

A targeted search across Keiper--Li asymptotics, off-critical zero singularities, zero-free regions, and exponential Diophantine approximation did not locate a standard statement organizing the same zero's radial excess and angular phase into the threshold `(13)` or the high-height scale separation `(9)`, `(15)`--`(17)`. This is not an exhaustive novelty proof. The durable contribution is the narrow Arithmetic Fidelity synthesis: **the cancellation budget must be compared to the radial off-RH growth gap generated by the same zero, and that gap degenerates like `(beta-1/2)/gamma^2`.**

## Boundaries

**Single conjugate pair.** The exact threshold `(13)` concerns one dominant conjugate pair. Several co-dominant pairs produce the multimode/fiber geometry of AF-250--AF-254. The likely analogue is to compare the relevant fiber-collapse exponent with the common radial `log q`, but that statement is not proved here.

**Pair-level versus whole Li sequence.** If cancellation lowers this pair below unit rate, another off-critical pole family may still reveal RH failure. Conversely, transfer of `(12)` to the full Li sequence requires the separated remainder to have smaller root rate than the surviving pair contribution. The finding does not silently replace that domination check.

**Location is not arithmetic provenance.** The high-ordinate quartet in `(43)` is a symmetry- and location-admissible control, not a claim about an actual Riemann zero. Actual zeta zeros obey global analytic relations not encoded by one point's strip position, height, and functional-equation orbit. The result says those coarse one-zero constraints cannot be the missing fidelity theorem.

**Finite safe horizon is not asymptotic fidelity.** Equation `(16)` only protects an initial window of length proportional to `gamma`. It does not prevent much later exponentially accurate returns to the cosine zero set.

**Near-critical zeros are more ill-conditioned.** As `beta downarrow1/2`, `log q_rho` shrinks even at fixed height. Any family-level detection theorem that allows hypothetical zeros arbitrarily close to the critical line must track this radial gap, not only height.

**Rational phases remain a separate exact-alias regime.** AF-249 assumes irrational phase to isolate near-cancellation. Rational normalized phases can have exact periodic zeros and fall under the earlier aliasing analysis.

## Research consequence

For sparse Li output, the source-side target is now quantitatively sharper. It is not enough to prove that actual zero-derived phases are non-generic, irrational, or even that their cancellation exponent is bounded by some source-independent positive constant. For each relevant off-critical dominant pair, the useful inequality is

\[
\boxed{
\tau_\rho(S)
<
-\log\left|1-\frac1\rho\right|
}
\tag{45}
\]

if the goal is merely to keep that pair above the RH unit-root boundary, and `tau_rho(S)=0` if the goal is to preserve its full dominant rate.

Because the right side can degenerate like `(beta-1/2)/gamma^2`, a uniform RH-facing argument needs a **source-coupled Diophantine estimate at exactly that scale**, or a stronger zero-exponent theorem. The high-height matched control shows that strip position, finite-height verification, functional-equation symmetry, and ordinary right-edge zero-free information do not provide it.

For the multimode affine frontier of AF-253--AF-254, the natural next theorem is therefore not another genericity statement. It is a growth-normalized version of the fiber problem: identify the actual zeta-forced phase constraints and compare their quotient fiber-collapse exponent against the radial `log q` of the same dominant Keiper shell, with enough uniformity as height increases and the shell approaches the unit circle.