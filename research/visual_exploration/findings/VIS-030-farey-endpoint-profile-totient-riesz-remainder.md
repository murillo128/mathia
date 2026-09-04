# VIS-030 — the full fixed-`nx` Farey endpoint profile is a normalized-totient Riesz remainder

## Claim

Let

`K(y) = sum_(a<=y) phi(a) (1/a - 1/y)`

be the fixed-`nx` endpoint rank profile from `VIS-029`, and put

`c = 3/pi^2`.

Then for every real `y>=1`, `K` has three exact arithmetic representations.

First, with

`b(a)=phi(a)/a`,

one has

`K(y) = sum_(a<=y) b(a) (1-a/y)`.

Thus the entire bounded-numerator endpoint hierarchy is exactly the first-order Riesz/Cesaro mean of the normalized totient sequence `phi(a)/a`, not an independent geometric decoration of the Farey endpoint.

Second, if

`Phi(t)=sum_(a<=t) phi(a)`,

then finite interchange gives

`K(y) = integral_1^y Phi(t)/t^2 dt`.

Writing

`E_phi(t)=Phi(t)-c t^2`,

and recalling the scaled endpoint discrepancy from `VIS-029`,

`H(y)=y-(pi^2/3)K(y)=y-K(y)/c`,

one obtains the exact identity

`H(y) = 1 - (pi^2/3) integral_1^y E_phi(t)/t^2 dt`.

So the limiting endpoint shape is precisely an integrated summatory-totient remainder.

Third, using

`phi(a)/a = sum_(d|a) mu(d)/d`,

let `theta_d={y/d}` be the fractional part. Then

`K(y)`
` = (y/2) sum_(d<=y) mu(d)/d^2`
`   - (1/2) sum_(d<=y) mu(d)/d`
`   + (1/(2y)) sum_(d<=y) mu(d) theta_d(1-theta_d)`.

The endpoint profile therefore has an exact finite Möbius decomposition.

Finally, for `Re(s)>1`, absolute convergence and the same divisor identity give the Dirichlet series

`sum_(a>=1) [phi(a)/a] a^(-s) = zeta(s)/zeta(s+1)`.

The `c y` main term in `K(y)` is consistent with the pole at `s=1`: the residue of `zeta(s)/zeta(s+1)` is `1/zeta(2)=6/pi^2`, and first-order Riesz smoothing contributes the factor `1/2`, giving `c=3/pi^2`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL ARITHMETIC/RIESZ REPRESENTATION + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No asymptotic estimate for `H(y)` as `y->infinity`, RH equivalence, new totient theorem, or new Farey rank theorem is claimed.

## 1. The endpoint layers are one Riesz mean

`VIS-029` obtained

`K(y)=sum_(a<=y) phi(a)(1/a-1/y)`

by counting reduced fractions `a/q<=y/n` for bounded numerator `a` as `n->infinity` with fixed `y`. Factoring `phi(a)/a` gives immediately

`K(y)=sum_(a<=y) [phi(a)/a](1-a/y)`.

This identity changes the interpretation of the successive integer layers. The break at `y=m` is still the exact admission of numerator `m`, but the collection of all admitted layers up to `y` is already a classical smoothed arithmetic sum. The endpoint geometry and the normalized-totient arithmetic are the same data in this scaling.

For every fixed cutoff `Y`, this remains a finite, explicit control exactly as used in `VIS-029`: only finitely many numerator classes contribute. The new issue appears when one tries to make the endpoint null progressively more aggressive by letting the cutoff itself explore larger arithmetic scales.

## 2. Exact summatory-totient remainder

For each `a<=y`,

`1/a - 1/y = integral_a^y t^(-2) dt`.

Because the sum is finite,

`K(y)`
` = sum_(a<=y) phi(a) integral_a^y t^(-2) dt`
` = integral_1^y [sum_(a<=t) phi(a)] t^(-2) dt`
` = integral_1^y Phi(t)/t^2 dt`.

Now substitute

`Phi(t)=c t^2 + E_phi(t)`.

Then

`K(y)=c(y-1)+integral_1^y E_phi(t)/t^2 dt`.

Since `H(y)=y-K(y)/c`, this is equivalent to

`H(y)=1-c^(-1) integral_1^y E_phi(t)/t^2 dt`
`    =1-(pi^2/3) integral_1^y E_phi(t)/t^2 dt`.

Thus the entire continuum profile that generated the deterministic endpoint energy in `VIS-029` can be read as an accumulated totient-discrepancy signal. This is an exact identity, not an asymptotic fit to the plotted endpoint layers.

## 3. Exact Möbius decomposition

The standard divisor identity

`phi(a)/a = product_(p|a)(1-1/p) = sum_(d|a) mu(d)/d`

turns the Riesz sum into

`K(y)=sum_(d<=y) mu(d)/d sum_(m<=y/d) (1-dm/y)`.

Put

`u=y/d`, `M=floor(u)`, `theta={u}`.

The inner finite arithmetic progression satisfies exactly

`sum_(m<=u)(1-m/u)`
` = M - M(M+1)/(2u)`
` = u/2 - 1/2 + theta(1-theta)/(2u)`.

Substituting `u=y/d` yields

`K(y)`
` = (y/2) sum_(d<=y) mu(d)/d^2`
`   - (1/2) sum_(d<=y) mu(d)/d`
`   + (1/(2y)) sum_(d<=y) mu(d) {y/d}(1-{y/d})`.

This gives a concrete information-accounting boundary. Enlarging the endpoint window is not merely adding geometrically similar fans: it progressively includes explicit Möbius-weighted partial sums and a bounded fractional-part correction.

## 4. Dirichlet-series identity

From

`phi(a)/a=sum_(d|a) mu(d)/d`,

absolute convergence for `Re(s)>1` gives

`sum_(a>=1) [phi(a)/a] a^(-s)`
` = zeta(s) sum_(d>=1) mu(d) d^(-s-1)`
` = zeta(s)/zeta(s+1)`.

This is enough to show why an all-scale endpoint subtraction cannot be treated as an arithmetic-free preprocessing step. The generating Dirichlet series of the very profile being removed contains the same zeta/Möbius analytic structure that the broader Farey program is meant to understand.

The statement is deliberately weaker than an RH criterion. No contour shift, zero sum, or error exponent for `K(y)-cy` is used here.

## 5. Prior art and novelty boundary

The Farey endpoint/rank ingredients remain classical and are already anchored by Dress, Tomás, and García in `SOURCES.md`. The present identities use only finite summation, the standard divisor formula for Euler's totient, and its Dirichlet series.

Riesz means attached to Euler-totient arithmetic are established literature. A targeted structure-based search located Shota Inoue and Isao Kiuchi, **Riesz means of the Euler totient function**, *Functiones et Approximatio Commentarii Mathematici* 60:1 (2019), 31–40, DOI `10.7169/facm/1650`. This bounds any novelty claim based merely on recognizing a smoothed totient sum. The exact normalization and identities used above are derived independently here; no error term or RH-equivalence statement is imported from that paper.

There is also a useful internal cautionary analogue in `research/mobius_cancellation/findings/MC-019-path-energy-coarse-riesz-rh-equivalence.md`: in a different Möbius carrier, a seemingly coarse Riesz mode already contains an RH-equivalent obligation. That does **not** prove an analogous equivalence for `K`; it only reinforces the methodological rule that a smoothed arithmetic control must be audited before being declared innocuous.

The durable Mathia result is therefore a control classification, not a new theorem about totients: the bounded-numerator endpoint hierarchy of `VIS-029` becomes an explicitly zeta/Möbius-bearing Riesz channel as the cutoff is enlarged.

## 6. Boundary conditions and falsification

The fixed-`Y` conclusions of `VIS-029` are unchanged. For each pre-fixed finite `Y`, the endpoint window is a legitimate exact finite control, and the associated `C(Y)` and `r=Theta(n)` spectral contribution remain valid.

This finding does not prove that a cutoff `Y=Y(n)` is invalid. It says that such a control acquires arithmetic content that must be accounted for. A growing-cutoff argument may still be useful if it proves that the removed Riesz component is asymptotically negligible for the proposed residual statistic or if the matched null preserves exactly the same component without importing the target conclusion.

No claim is made that the complete Farey discrepancy is determined by `K`, that `H(y)` has a particular decay rate, or that estimating `H` at any stated scale is equivalent to RH. The formulas classify what information the endpoint profile contains; they do not solve its asymptotics.

The identities can be falsified directly by finite arithmetic evaluation. In particular, failure of the Riesz form, the integral representation, the Möbius decomposition, or the Dirichlet series would invalidate the claim. Each follows by finite rearrangement or absolutely convergent Dirichlet convolution in its stated domain.

## Research consequence

The cross-line clue

`research/farey_discrepancy/clues/CLUE-farey-gap-order-bridge-suppression.md`

needs one more control boundary. Pre-fixed finite endpoint cutoffs remain appropriate, but **“remove more and more endpoint layers until the residual stabilizes” is not automatically a neutral nuisance subtraction**. Once the cutoff itself grows, the removed profile is a normalized-totient Riesz mean with an explicit Möbius decomposition and zeta-ratio generating series.

The preferable next Farey test is therefore either to keep a pre-registered finite family of endpoint cutoffs and demand residual stability across them, or to construct a bulk statistic for which the full fixed-`nx` endpoint contribution can be proved negligible without assuming the arithmetic cancellation the experiment is trying to detect. Only then should a surviving spectral feature be attributed to denominator strata, mediant ancestry, long-range gap order, or another interior mechanism.