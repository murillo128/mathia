# AF-028 — Accumulating double-positive modulation tests are finite-scale norm-faithful

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`

## Claim

Fix numbers

\[
0<B<A
\]

and choose a nonnegative real bump

\[
\phi\in C_c^\infty((-A/2,A/2))
\]

which is strictly positive on `(-B/2,B/2)` and vanishes outside `[-B/2,B/2]`. Put

\[
K(x)
=
\frac{(\phi*\widetilde\phi)(x)}{(\phi*\widetilde\phi)(0)},
\qquad
\widetilde\phi(x)=\phi(-x).
\]

Then

\[
K\in C_c^\infty((-A,A)),
\qquad
K(-x)=K(x),
\qquad
K(0)=1,
\]

and, crucially,

\[
K(x)>0\quad (|x|<B),
\qquad
K(x)\ge0,
\qquad
\widehat K(\xi)\ge0.
\]

Fix `0<\varepsilon<1` and define, for every real frequency `\xi`,

\[
\boxed{
F_\xi(x)
=
\frac{K(x)(1+\varepsilon\cos(\xi x))}{1+\varepsilon}.
}
\]

Every `F_\xi` belongs to the double-positive compact test class of AF-027:

\[
\mathcal D_A
=
\left\{
F\in C_c^\infty((-A,A);\mathbb R):
F(-x)=F(x),\ F(0)=1,\ F\ge0,\ \widehat F\ge0
\right\}.
\]

Let `\Lambda\subset\mathbb R` have a finite accumulation point. Then the infinite family

\[
\boxed{\{F_\xi:\xi\in\Lambda\}}
\]

is an exact determining family for finite signed measures on the visible positive interval `(0,B)`:

> If `\mu` and `\nu` are finite signed Radon measures supported in `(0,B)` and
> \[
> \int F_\xi\,d\mu
> =
> \int F_\xi\,d\nu
> \qquad(\xi\in\Lambda),
> \]
> then
> \[
> \boxed{\mu=\nu.}
> \]

More generally, if `\mu,\nu` are finite signed measures on `(0,\infty)` whose restrictions to `(0,B)` are finite, equality of all these test values implies

\[
\boxed{
\mu|_{(0,B)}=\nu|_{(0,B)}
}
\]

provided the measures have no contribution in the support of `K` outside `(0,B)`; in the prime-power application below this is enforced simply by comparing the restrictions of the measures to `(0,B)`.

For generalized-prime systems `Q` and `R` satisfying the local-finiteness hypotheses of AF-020, let

\[
\omega_Q
=
\sum_j\sum_{m\ge1}
\ell_j e^{-m\ell_j/2}\delta_{m\ell_j},
\qquad
\ell_j=\log q_j,
\]

and similarly for `R`. If

\[
\boxed{
W_Q(F_\xi)=W_R(F_\xi)
\qquad\text{for every }\xi\in\Lambda,
}
\]

then

\[
\boxed{
\omega_Q|_{(0,B)}=\omega_R|_{(0,B)}
}
\]

and AF-020's dilation-Möbius inversion gives

\[
\boxed{
Q_{<e^B}=R_{<e^B}
\quad\text{as generator-norm multisets.}
}
\]

Thus a **countably infinite** family already suffices: for example one may take

\[
\Lambda=\{1/n:n\ge1\}.
\]

This creates a sharp fidelity boundary with AF-022, AF-023, and AF-027. Every finite collection of scalar tests remains vulnerable to finite-dimensional Beurling collision mechanisms, and the entire double-positive cone has full-dimensional finite response jets. Yet one fixed source-independent one-parameter modulation template, sampled at infinitely many frequencies with a finite accumulation point, determines the complete visible prime-power measure and hence all generator norms below one exact support horizon.

The recovery mechanism is **analytic coupling across the infinite test family**, not positivity by itself and not a finite-order local singularity.

## The modulation family stays inside the double-positive cone

The autocorrelation seed satisfies

\[
\widehat K(\omega)
=
\frac{|\widehat\phi(\omega)|^2}{(\phi*\widetilde\phi)(0)}
\ge0.
\]

Because `\phi` is nonnegative and positive throughout `(-B/2,B/2)`, the overlap integral defining the autocorrelation is strictly positive for every translation of magnitude `<B`. Hence

\[
K(x)>0
\qquad(|x|<B).
\]

For `0<\varepsilon<1`,

\[
1+\varepsilon\cos(\xi x)
\ge1-\varepsilon>0,
\]

so `F_\xi\ge0`. Its normalization is exact:

\[
F_\xi(0)=1.
\]

Fourier transformation gives

\[
\widehat F_\xi(\omega)
=
\frac{1}{1+\varepsilon}
\left[
\widehat K(\omega)
+
\frac{\varepsilon}{2}\widehat K(\omega-\xi)
+
\frac{\varepsilon}{2}\widehat K(\omega+\xi)
\right]
\ge0.
\]

Therefore

\[
F_\xi\in\mathcal D_A
\qquad\text{for every real }\xi.
\]

This is exactly the same classical positive-positive-definite modulation family used in AF-027. The new issue is not admissibility but what happens when the **whole analytically linked family** is retained instead of finitely many of its values or finitely many local jets.

## Accumulating frequency samples determine the weighted measure

Let

\[
\delta=\mu-\nu.
\]

Assume first that `\delta` is a finite signed Radon measure supported in `(0,B)`, and define for complex `z`

\[
H(z)
=
\int F_z(x)\,d\delta(x),
\]

where

\[
F_z(x)
=
\frac{K(x)(1+\varepsilon\cos(zx))}{1+\varepsilon}.
\]

The function `F_z` need not be an admissible positive test for non-real `z`; complexifying the parameter is only an analytic continuation device. Since `K\delta` has compact support, differentiation under the integral is legitimate on compact subsets of the complex plane and

\[
H:\mathbb C\to\mathbb C
\]

is entire.

Write

\[
c=\int K(x)\,d\delta(x)
\]

and

\[
C(z)=\int K(x)\cos(zx)\,d\delta(x).
\]

Then

\[
H(z)=\frac{c+\varepsilon C(z)}{1+\varepsilon}.
\]

Equality of the retained test values says

\[
H(\xi)=0
\qquad(\xi\in\Lambda).
\]

Because `\Lambda` has a finite accumulation point and `H` is entire, the identity theorem forces

\[
\boxed{H\equiv0.}
\]

At `z=0`, `F_0=K`, so

\[
0=H(0)=c.
\]

Consequently

\[
\boxed{C(z)\equiv0.}
\]

Thus the cosine transform of the finite signed measure

\[
d\eta(x)=K(x)\,d\delta(x)
\]

vanishes identically.

## Cosine-transform uniqueness on the positive interval

There are several classical ways to finish the argument. One transparent route is to reflect `\eta` evenly.

Let `\eta^-` be the reflected measure on `(-B,0)` and define the finite signed measure

\[
\eta_e=\eta+\eta^-.
\]

Its Fourier-Stieltjes transform is

\[
\widehat{\eta_e}(t)
=
2\int_0^B\cos(tx)\,d\eta(x)
=2C(t)
=0
\qquad(t\in\mathbb R).
\]

Uniqueness of the Fourier transform of finite measures gives

\[
\eta_e=0.
\]

The positive and negative supports are disjoint, so

\[
\eta=0.
\]

Equivalently, differentiating the entire cosine transform at the origin gives all even moments

\[
\int x^{2n}\,d\eta(x)=0,
\qquad n\ge0,
\]

and compact-interval moment determinacy reaches the same conclusion because `x\mapsto x^2` is one-to-one on the positive half-line.

Finally, `K(x)>0` for every `x\in(0,B)`. Multiplication by `K` is therefore injective on finite signed measures supported there. For example, on every compact subinterval

\[
[1/n,B-1/n]\subset(0,B)
\]

the function `1/K` is bounded and continuous, so `K\delta=0` implies `\delta=0` on that compact set. Exhausting `(0,B)` gives

\[
\boxed{\delta=0.}
\]

Hence the accumulating modulation family determines the entire visible measure.

The proof exposes exactly where each hypothesis enters:

- compact support gives an entire transform in the modulation parameter;
- an accumulating exact sample set invokes the identity theorem;
- positivity of `K` on the visible interval prevents the window from erasing any local mass;
- cosine/Fourier uniqueness converts transform equality back to measure equality.

Pointwise or Fourier positivity of the tests does **not** itself perform the recovery. Those conditions show that the determining family remains inside a strongly constrained admissible cone while analytic coupling supplies the missing rigidity.

## Prime-power recovery and the support horizon

For a generalized-prime system `Q`, AF-020 identifies the positive Weil measure

\[
\omega_Q
=
\sum_j\sum_{m\ge1}
\ell_j e^{-m\ell_j/2}\delta_{m\ell_j}.
\]

On every bounded positive interval it is finite. Because each `F_\xi` is supported in `[-B,B]`, the positive-side pairing depends only on

\[
\omega_Q|_{(0,B)}.
\]

Thus if two generalized-prime systems have the same values for every `F_\xi`, `\xi\in\Lambda`, the measure theorem gives

\[
\omega_Q|_{(0,B)}
=
\omega_R|_{(0,B)}.
\]

AF-020 then removes the prime-power collisions exactly. If

\[
b_Q(x)
=
\frac{e^{x/2}\omega_Q(\{x\})}{x},
\]

and `n_Q(y)` is the multiplicity of `y` as a generator logarithm, then

\[
b_Q(x)
=
\sum_{m\ge1}\frac1m n_Q(x/m)
\]

and dilation-Möbius inversion yields

\[
\boxed{
n_Q(x)
=
\sum_{m\ge1}\frac{\mu(m)}m b_Q(x/m).
}
\]

For `x<B`, every argument `x/m` also lies below `B`. Hence the restricted prime-power measure determines every generator log below `B`, including multiplicity. Exponentiating gives

\[
Q_{<e^B}=R_{<e^B}.
\]

The result therefore retains AF-020's exact arithmetic horizon. It does not recover any generator whose logarithm lies at or beyond `B`, because no test in the family sees that region.

For the rational primes, the conclusion is concrete:

\[
W_{\mathbb P}(F_\xi)=W_R(F_\xi)
\quad\forall\xi\in\Lambda
\]

forces every generalized-prime control `R` to have exactly the same generator norms as the rational primes below `e^B`. This is exact finite-scale rational-prime norm fidelity inside a countable double-positive test family.

## Finite versus infinite family is the actual boundary

AF-022 proves that for any **finite** collection of real compactly supported tests there are exact arbitrarily local collisions inside genuine generalized-prime deformation chambers. AF-023 strengthens this at regular points: with more perturbable generator coordinates than retained scalar outputs, the rational-prime point itself lies on a positive-dimensional exact same-test fiber whenever the finite-test Jacobian has full row rank.

AF-027 then shows that imposing both

\[
F\ge0
\qquad\text{and}\qquad
\widehat F\ge0
\]

still leaves full-dimensional freedom in every finite off-origin jet and every finite nonresonant Weil-response jet. Therefore no universal finite-order singular relation is forced merely by double positivity.

The present result does not contradict any of those no-go theorems. Its destination is no longer finite-dimensional. The sequence

\[
\left(W_Q(F_\xi)\right)_{\xi\in\Lambda}
\]

contains infinitely many exact scalar values tied together as samples of one entire function. A set with a finite accumulation point uniquely determines that entire function, so the infinite family recovers information that every finite truncation loses.

This gives the exact hierarchy

\[
\boxed{
\text{finite double-positive test set}
\;\not\Rightarrow\;
\text{local norm fidelity}
}
\]

at the matched generalized-prime level of AF-022/AF-023, while

\[
\boxed{
\text{accumulating double-positive modulation family}
\;\Longrightarrow\;
\text{exact norm fidelity below }e^B.
}
\]

The lesson is not that infinitely many tests are always sufficient. The decisive property here is an **analytic uniqueness structure** linking them. Nor does a one-dimensional parameter imply a one-dimensional information destination: infinitely many exact evaluations of an analytic transform can encode a full compactly supported measure.

## Prior art and novelty assessment

Every ingredient in the recovery argument is classical.

- Alexandr Borisov, **“Positive positive-definite functions and measures on locally compact abelian groups,”** arXiv:`math/9906126` (1999), and Philippe Jaming, Máté Matolcsi, Szilárd G. Révész, **“On the Extremal Rays of the Cone of Positive, Positive Definite Functions,”** *Journal of Fourier Analysis and Applications* 15(4) (2009), 561–582, DOI `10.1007/s00041-008-9057-6`, are direct prior art for the cone of functions that are simultaneously pointwise nonnegative and positive definite.
- The fact that the Fourier-Laplace transform of a compactly supported finite measure extends to an entire function is a basic Paley–Wiener phenomenon; in the present bounded-support setting it also follows directly by differentiating the integral of `e^{izx}` or `\cos(zx)` under the sign of integration.
- The identity theorem for holomorphic functions is classical complex analysis: exact values on any set with an interior accumulation point determine an entire function uniquely.
- Walter Rudin, ***Fourier Analysis on Groups***, Interscience/Wiley (1962), supplies the classical uniqueness framework for Fourier-Stieltjes transforms of finite measures on locally compact abelian groups.
- Compact-interval moment determinacy is the classical Hausdorff moment phenomenon and gives an alternative proof after taking all even derivatives of the cosine transform at zero.
- AF-020 already established the dilation-Möbius reconstruction from the complete visible prime-power measure to the generator-norm multiset.

No novelty is claimed for the double-positive cone, autocorrelation kernels, cosine modulation, Fourier shifts, Paley–Wiener analyticity, the complex identity theorem, Fourier-transform uniqueness, Hausdorff moment determinacy, or Möbius inversion.

A targeted literature audit did not identify a standard theorem stated as the exact combination used here: a single compactly supported **double-positive normalized modulation template**, sampled on an arbitrary frequency set with a finite accumulation point, as a determining family for the visible Weil prime-power measure and hence for generalized-prime norms below the corresponding support horizon. Absence of such a statement is not evidence of novelty.

The Arithmetic Fidelity contribution is therefore deliberately narrower: it identifies a reusable **category boundary** by combining classical analytic uniqueness with the matched-control results AF-020/AF-022/AF-023/AF-027. Double positivity leaves every finite response layer flexible, but an infinitely and analytically coupled subfamily inside that same cone becomes exact and measure-determining.

## Boundaries and failure modes

- **Exact fidelity is not stable recovery.** Analytic continuation from clustered samples is generally severely ill-conditioned. Arbitrarily small errors in the values `W_Q(F_\xi)` can produce large uncertainty away from the sampled frequencies. This theorem is a zero-error identifiability result, not a numerical reconstruction guarantee.
- The theorem needs infinitely many exact test values. Every finite truncation falls back under the finite-test obstructions of AF-022/AF-023.
- A frequency set with no finite accumulation point is not covered by the identity-theorem proof. Some such sets may be uniqueness or sampling sets for an appropriate Paley–Wiener class, but that requires density/type hypotheses not established here.
- The family is source-independent once `A,B,\phi,\varepsilon,\Lambda` are fixed. The proof does not tune the tests to the rational primes or to a competing generalized-prime source.
- The theorem does not say that one canonical test is faithful. The information lives in the complete accumulating family.
- The support horizon is strict. The construction determines the measure on `(0,B)` and generator norms `<e^B`; it says nothing about atoms at the boundary where the window may vanish or about generators above the window.
- Recovery of the prime-power measure gives the unordered generator-norm multiset, not prime labels, additive structure of the integers, splitting provenance, or richer upstream arithmetic relations.
- The argument uses a finite signed-measure difference on the visible interval. General distributional sources of higher order require a separate uniqueness statement, although compactly supported distributions also have entire Fourier-Laplace transforms.
- Evenness is harmless here because the unknown measure lives on the positive half-line. On a source class containing independent positive and negative locations, a cosine-only family would identify only the even symmetrization unless additional odd/phase data were retained.
- Nothing here constrains the location, multiplicity, or simplicity of zeta zeros and nothing here is evidence for RH.

## Decisive audit test

For a proposed RH or explicit-formula route that claims an infinite constrained test family restores information lost by all finite probes:

1. identify the exact source measure or structured object and the finite-scale support horizon;
2. express the retained infinite family as samples of a transform or other rigid function class of the source;
3. prove the required uniqueness-set theorem for the **actual** parameter set, not merely for an ideal continuum of tests;
4. prove that any fixed window/kernel multiplying the source is nonvanishing on the region claimed to be recovered;
5. invert all structural collisions in the source representation, such as the prime-power overlap removed here by dilation-Möbius inversion;
6. compare against matched generalized-prime or other controls at the same retained destination;
7. separate exact uniqueness from stability: if the mechanism needs robustness rather than zero-error identifiability, establish a quantitative sampling/reconstruction bound independently;
8. only then interpret the infinite family as carrying rational-prime-specific information into a downstream spectral, positivity, or asymptotic step.

A finite list of tests cannot inherit the present theorem merely because it was selected from the same analytic family.

## Consequence for the line

The local Weil-programming obstruction now has an explicit escape that is both constrained and exact.

The relevant hierarchy is no longer simply

\[
\text{unconstrained tests}
\supset
\text{positive tests}
\supset
\text{double-positive tests}.
\]

AF-027 shows that every one of those broad classes can remain finite-jet flexible. The decisive axis is instead

\[
\boxed{
\text{finite retained evaluations}
\quad\longrightarrow\quad
\text{infinite analytically coupled evaluations}.
}
\]

For the modulation family above, crossing that axis converts local finite-dimensional non-identifiability into exact measure recovery on the visible interval.

This supplies a concrete answer to one part of the line's global-fidelity question: a genuinely global constraint need not make each individual test rigid. It may instead impose **cross-test analytic coherence** strong enough that the whole family is a uniqueness set for the source transform.

The next boundary is therefore sharper. For RH-relevant mechanisms, ask not only whether the admissible tests are positive, canonical, or infinite, but whether the retained family forms a source-independent uniqueness/sampling set in the actual analytic category, whether the recovery is stable enough for the intended downstream operation, and whether the support horizon or later compression discards the recovered prime-norm information again.