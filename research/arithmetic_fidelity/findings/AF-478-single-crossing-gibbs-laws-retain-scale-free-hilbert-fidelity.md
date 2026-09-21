# AF-478 — Single-crossing Gibbs laws retain scale-free Hilbert fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `SOURCE-LAW`, `QUANTITATIVE-FIDELITY`, `MONOTONE-LIKELIHOOD-RATIO`, `MATCHED-CONTROL`, `NO-NOVELTY-CLAIM`

## Claim

AF-473--AF-476 show that tail mass or a tail-decay envelope alone does not give scale-free Hilbert fidelity on an infinite alphabet: a full soft-tail class can hide arbitrarily large Hamming cubes in small residual mass. That obstruction is not inherited by every narrow infinite-support source law satisfying the same tail bound.

There is an exact positive counterpoint for one-parameter Gibbs families. Let

\[
E_0<E_1<E_2<\cdots\to\infty,
\qquad a_n>0,
\]

and fix `sigma_0` such that

\[
Z(\sigma_0)=\sum_{n\ge0}a_n e^{-\sigma_0 E_n}<\infty
\]

and

\[
m_0
:=
\frac{\sum_{n\ge0}E_n a_n e^{-\sigma_0 E_n}}
     {Z(\sigma_0)}
<\infty.
\tag{1}
\]

For `sigma>=sigma_0`, define the probability law

\[
\mu_\sigma(n)
=
\frac{a_n e^{-\sigma E_n}}{Z(\sigma)}.
\tag{2}
\]

Put

\[
N_0=\#\{n:E_n<m_0\}.
\tag{3}
\]

Because the energies are strictly increasing and unbounded, `N_0<\infty`; because every state has positive mass and there is more than one state, `N_0>=1`.

Then the canonical coordinate Hilbert encoding

\[
H(\mu)=\sqrt2\,(\mu(n))_{n\ge0}\in\ell^2
\tag{4}
\]

is globally bi-Lipschitz on the whole infinite-support family `\{\mu_\sigma:\sigma>=\sigma_0\}` for the total-variation/`ell^1` source metric:

\[
\boxed{
\frac{1}{\sqrt{2N_0}}\,
\|\mu_\sigma-\mu_\tau\|_1
\le
\|H(\mu_\sigma)-H(\mu_\tau)\|_2
\le
\|\mu_\sigma-\mu_\tau\|_1
}
\tag{5}
\]

for every `sigma,tau>=sigma_0`.

Thus an infinite tail of positive mass does **not** by itself force the AF-473/AF-476 Hamming-cube obstruction. What matters is the geometry of the **actually realizable secants**. In this Gibbs family every pairwise secant has a one-crossing sign pattern, and the positive Jordan part is uniformly confined to at most `N_0` low-energy coordinates. That bounded sign complexity is enough to give a resolution-independent Hilbert conditioning constant even though every source has infinite support.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{tail amplitude/profile is not a complete source-complexity invariant: a rigid single-crossing secant law can retain scale-free Hilbert fidelity on an infinite alphabet.}
}
\tag{6}
\]

This identifies a concrete escape hatch from the broad profile-envelope obstruction: prove structure on the admissible secant carrier itself, rather than only an approximation rate for individual sources.

## Exact derivation

Assume without loss of generality that `tau>sigma>=sigma_0`. From `(2)`,

\[
\frac{\mu_\tau(n)}{\mu_\sigma(n)}
=
\frac{Z(\sigma)}{Z(\tau)}
\exp\!\bigl(-(\tau-\sigma)E_n\bigr).
\tag{7}
\]

Because `E_n` is strictly increasing, the likelihood ratio in `(7)` is strictly decreasing in `n`. Therefore

\[
d_n:=\mu_\tau(n)-\mu_\sigma(n)
\tag{8}
\]

can change sign at most once: its positive coordinates form an initial energy block, its negative coordinates a terminal block, with at most one zero coordinate at the crossing.

The positive condition is

\[
\frac{\mu_\tau(n)}{\mu_\sigma(n)}>1
\iff
E_n<c_{\sigma,\tau},
\tag{9}
\]

where

\[
c_{\sigma,\tau}
=
\frac{\log Z(\sigma)-\log Z(\tau)}{\tau-\sigma}.
\tag{10}
\]

Let

\[
m(u)=\sum_n E_n\mu_u(n).
\tag{11}
\]

The first-moment assumption at `sigma_0` gives the needed right-half-line differentiability by dominated convergence. The standard log-partition identities are

\[
(\log Z)'(u)=-m(u)
\tag{12}
\]

and, wherever the second moment is finite,

\[
m'(u)=-\operatorname{Var}_{\mu_u}(E)\le0.
\tag{13}
\]

For the monotonicity used below, a second-moment hypothesis is unnecessary: `(7)` itself gives monotone-likelihood-ratio ordering, hence `m(u)` is nonincreasing whenever the first moment is finite. Equivalently one may differentiate on `u>sigma_0` and pass to the endpoint by monotone/dominated limits.

Using `(12)`,

\[
c_{\sigma,\tau}
=
\frac1{\tau-\sigma}
\int_\sigma^\tau m(u)\,du
\le m(\sigma)
\le m_0.
\tag{14}
\]

Consequently every positive coordinate of `d` lies in the fixed finite set

\[
\{n:E_n<m_0\},
\tag{15}
\]

so

\[
|\operatorname{supp} d_+|\le N_0.
\tag{16}
\]

Because `d` has total mass zero,

\[
\|d_+\|_1=\|d_-\|_1=\frac12\|d\|_1.
\tag{17}
\]

Cauchy--Schwarz on the positive support gives

\[
\|d_+\|_2
\ge
\frac{\|d_+\|_1}{\sqrt{N_0}}
=
\frac{\|d\|_1}{2\sqrt{N_0}}.
\tag{18}
\]

Hence

\[
\sqrt2\,\|d\|_2
\ge
\sqrt2\,\|d_+\|_2
\ge
\frac{\|d\|_1}{\sqrt{2N_0}},
\tag{19}
\]

which is the lower bound in `(5)`.

For the upper bound, `(17)` and `\|x\|_2\le\|x\|_1` on nonnegative vectors give

\[
\|d\|_2^2
=
\|d_+\|_2^2+\|d_-\|_2^2
\le
\|d_+\|_1^2+\|d_-\|_1^2
=
\frac12\|d\|_1^2.
\tag{20}
\]

Multiplying by `\sqrt2` proves the upper bound in `(5)`.

The constant is global: it is independent of `sigma`, `tau`, their separation, the requested source resolution, and the number of tail coordinates carrying nonzero probability.

## The actual resource is bounded secant sign complexity

The Gibbs formula is one sufficient mechanism, but the proof exposes the smaller reusable invariant. Let `\mathcal C` be any class of probability vectors on a countable alphabet such that for every distinct `\mu,\nu\in\mathcal C`, after orienting the difference one of the Jordan parts of `\mu-\nu` has support size at most `N`. Then the same argument gives

\[
\frac1{\sqrt{2N}}\|\mu-\nu\|_1
\le
\sqrt2\|\mu-\nu\|_2
\le
\|\mu-\nu\|_1.
\tag{21}
\]

So the positive theorem does not come from parametric dimension by itself. It comes from a uniform combinatorial restriction on the sign pattern of **pairwise source secants**.

This distinction matters because AF-461 already rules out the naive inference

\[
\text{finite-dimensional nonlinear source law}
\Longrightarrow
\text{good Hilbert fidelity}.
\]

Regular finite-dimensional source-law fibers may locally realize large tangent-kernel families and inherit zero cube defect. The Gibbs curve is much more rigid: its likelihood ratios are totally ordered, every secant is single-crossing, and the crossing rank is uniformly bounded on the half-line `sigma>=sigma_0` by `(14)`.

## Prime specialization

Take the alphabet to be the rational primes, with

\[
E_p=\log p,
\qquad a_p=1.
\]

For real `sigma>1`, the partition function is the classical prime zeta function

\[
P(\sigma)=\sum_p p^{-\sigma},
\tag{22}
\]

and the normalized prime Gibbs law is

\[
\mu_\sigma(p)=\frac{p^{-\sigma}}{P(\sigma)}.
\tag{23}
\]

Fix any `sigma_0>1`. Absolute convergence permits termwise differentiation and gives

\[
m_0
=
\frac{\sum_p(\log p)p^{-\sigma_0}}{P(\sigma_0)}
=
-\frac{P'(\sigma_0)}{P(\sigma_0)}.
\tag{24}
\]

Therefore one may take

\[
N_0
=
\#\left\{p:
\log p< -\frac{P'(\sigma_0)}{P(\sigma_0)}
\right\}.
\tag{25}
\]

Equations `(5)` and `(25)` give a completely explicit, scale-free TV-to-Hilbert conditioning bound for the entire prime family `\{\mu_\sigma:\sigma>=sigma_0\}`.

This is **not evidence for rational-prime selectivity**. The proof uses only the ordered energy sequence and the one-parameter exponential-family law. Replacing `\log p` by any strictly increasing non-prime energy sequence satisfying `(1)` gives the same theorem. The matched non-prime control therefore passes exactly.

The prime specialization is useful for a different reason: it demonstrates on an actual infinite prime-derived source that the generic soft-tail obstruction can disappear once the admissible source law forbids independent private-tail switches. What survives here is the one-dimensional monotone-likelihood geometry, not a specifically arithmetic discriminator.

## Relation to AF-473--AF-477

AF-473 proves infinite Hilbert distortion for the **full** soft-sparse envelope because an arbitrarily small tail can independently choose among indefinitely many disjoint atom pairs. AF-474 and AF-475 replace impossible all-scale multiplicative control by additive/resolution-dependent guarantees from best-`s` tail mass. AF-476 proves that, for the full profile class `\mathcal C_\phi`, those guarantees are essentially forced whenever the profile admits the corresponding private-tail cubes. AF-477 shows that finitely many moment constraints also leave large exact cube families when the source fiber is broad enough.

AF-478 establishes the complementary boundary: **the profile of individual sources is not enough to predict the conditioning of a narrow source manifold.** The Gibbs family has an infinite tail, and its tail may obey exactly the same decay envelope used to define a much larger `\mathcal C_\phi`, but the source family does not realize the independent tail switches that make AF-476 sharp. Its pairwise secants instead satisfy `(16)`.

Accordingly, an arithmetic source restriction should now be audited with two separate quantities:

1. an approximation profile, measuring how much mass/energy lies outside the best finite truncation; and
2. a realizable-secant complexity, measuring which sign patterns, cubes, or independent switches actually occur between admissible sources.

The first controls additive truncation error. The second controls whether generic metric-embedding lower bounds are physically realizable inside the source law. Neither quantity determines the other.

## Prior art and novelty audit

The structural ingredients are classical, and this finding makes **no novelty claim** for exponential families, monotone likelihood ratios, prime zeta, or the elementary norm inequalities.

- Samuel Karlin and Herman Rubin, **“The Theory of Decision Procedures for Distributions with Monotone Likelihood Ratio,”** *The Annals of Mathematical Statistics* 27(2), 272--299 (1956), DOI `10.1214/aoms/1177728259`. One-parameter exponential families and monotone likelihood ratios are classical statistical structure; the threshold/single-crossing behavior used in `(7)`--`(10)` is exactly in that orbit of ideas.
- Samuel Karlin and Herman Rubin, **“Distributions Possessing a Monotone Likelihood Ratio,”** *Journal of the American Statistical Association* 51(276), 637--643 (1956), DOI `10.1080/01621459.1956.10501355`. Direct classical source for the monotone-likelihood-ratio property and its consequences for ordered families.
- C.-E. Fröberg, **“On the Prime Zeta Function,”** *BIT* 8, 187--202 (1968), DOI `10.1007/BF01933420`. Classical source for the prime zeta function. On the real half-line `sigma>1`, `(22)` and its differentiated series are in the elementary absolute-convergence regime.

A targeted prior-art search found the monotone-likelihood-ratio and exponential-family mechanism as standard mathematics, but did not justify treating the particular inequality `(5)` as a new theorem of statistics or metric geometry. The durable Arithmetic Fidelity contribution is therefore the **boundary synthesis**: AF-473--AF-477 diagnose broad source classes by the tail switches their envelopes permit, whereas `(5)` exhibits an explicit infinite-support source law whose ordered secant geometry forbids those switches and restores a uniform Hilbert margin.

## Boundaries and falsification audit

- **The parameter half-line is load-bearing.** The uniform constant uses the fixed anchor `sigma_0` and the bound `c_{sigma,tau}<=m_0`. If the family is enlarged toward a parameter value where the first energy moment diverges, `N_0` need not remain finite and this proof gives no scale-free constant.
- **Strict energy ordering is a convenient sufficient hypothesis.** Ties can be grouped into energy shells. Then the relevant bound is the number of coordinates, or shell multiplicity, below the maximal crossing energy; unbounded degeneracy can destroy the stated finite `N_0` bound.
- **Positive base weights and common support matter.** They make the base factor `a_n` cancel from the likelihood ratio. Parameter-dependent supports or weights require a separate secant audit.
- **The result concerns this source family, not its tail envelope or convex hull.** Closing under arbitrary mixtures, independent tail perturbations, or moment-fiber completion can reintroduce Hamming cubes and invalidate the constant.
- **The canonical embedding is linear in the probability vector.** The theorem proves existence of one uniformly faithful Hilbert representation; it does not assert optimal distortion or characterize all Hilbert embeddings.
- **The bound may be conservative.** `N_0` controls the largest possible positive support over the entire parameter half-line. Pair-specific crossings can occur much earlier, yielding stronger local constants.
- **No arithmetic discriminator has been certified.** Every matched non-prime Gibbs family with the same ordered-energy hypotheses enjoys the same mechanism. Any RH-facing application would still need an independently justified property that distinguishes rational primes from those controls and survives the downstream transformation.
- **Finite parametric dimension is not the explanation.** AF-461 is the falsification control: other regular finite-dimensional source laws can retain arbitrarily bad secant directions. The load-bearing property here is the global single-crossing order.

## Research consequence

The current source-restriction program should not ask only whether a prime-derived family has fast tail decay. AF-478 shows that this can miss the decisive structure in both directions. A broad class with an excellent tail profile may still carry private-tail Hamming cubes, while a narrow infinite-support family can have constant Hilbert conditioning because its secants obey a rigid sign law.

For future arithmetic instantiations, the sharper gate is therefore:

\[
\boxed{
\text{identify the realizable secant/sign complexity of the exact arithmetic source class before importing lower bounds from a larger approximation envelope.}
}
\tag{26}
\]

The prime Gibbs example clears that geometric gate but fails the arithmetic-selectivity gate: its good conditioning is reproduced by non-prime controls. That separates two questions which the earlier profile results could not separate cleanly -- **can the source restriction defeat generic compression obstructions, and is the restriction itself specifically arithmetic?** Here the answers are respectively yes and no.