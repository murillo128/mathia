# PL-260 — Bombieri finite-defect stabilization removes finite-total sparsity from the Weil observability gap

**Evidence:** `LITERATURE+DERIVED`

**Status:** `PRIOR-ART-REDIRECT + SHARP-BOUNDARY + NEGATIVE/OBSTRUCTION`

## Claim

A possible overreading of `PL-259` is now ruled out by classical prior art. Alpöge--Furman and Lamzouri show that the particular first/second-moment mechanism used for their positive-proportion theorem is insensitive to `o(N)` off-line zeros, so those aggregate moments cannot by themselves exclude a finite or zero-density exceptional set. However, this does **not** mean that finite-dimensional Weil truncations are intrinsically unable to see finite sparse violations of RH.

Bombieri proved in 2000 that, **under the hypothesis that RH is false but only finitely many nontrivial zeros lie off the critical line**, the finite truncations of the Fourier-side quadratic form associated with Weil's functional eventually have

\[
 n_-(Q_M)=\frac12 N_{\mathrm{off}}
\]

for all sufficiently large truncation level `M`, where `N_off` is the total number of nontrivial zeros failing RH, counted in Bombieri's formulation, and `n_-(Q_M)` denotes the number of negative eigenvalues. Thus every finite-total off-line defect is eventually visible in the negative index of the full truncation family.

For `prime_lattice`, this creates an important distinction:

- **moment observability:** asymptotic trace/second-moment data such as that used in `PL-259` can average away `o(N)` exceptional zeros;
- **form observability:** a sufficiently rich cofinal family of finite Weil forms can, at least in Bombieri's finite-total-defect regime, retain enough information for its negative index to count the entire off-line defect.

The theorem is classical prior art, not a Mathia novelty claim. The line-specific consequence is a redirect of the surviving target after `PL-259`: it is too strong to demand an individually localized per-zero detector as the only possible escape from sparse-exception blindness. A global **negative-index stabilization/completeness theorem** is already a valid mechanism for finite-total defects. What remains unresolved for an RH route is to obtain unconditional/cofinal control strong enough to rule out negative directions in the general case, in particular without assuming that the off-line divisor is finite.

## 1. What Bombieri's theorem actually removes

Weil's quadratic functional is positive semidefinite if and only if RH holds. Bombieri studies the Fourier transform of this functional as a quadratic form in infinitely many variables, together with finite truncations and their eigenvalues. His abstract states the sharp finite-defect theorem: if RH is false but only finitely many nontrivial zeros are off the critical line, then, once the truncation is large enough, the number of negative eigenvalues is precisely one-half the number of zeros failing RH.

The factor `1/2` is consistent with the functional-equation/conjugation pairing emphasized in `PL-259`: an off-line zero configuration is not an isolated scalar defect but comes with the corresponding symmetry partners, while an indefinite Hermitian block contributes a negative direction. For the present finding, however, the exact stabilization statement is cited from Bombieri rather than rederived from the rank-one model in `PL-259`; the two truncation constructions should not be silently identified.

The immediate logical consequence is exact:

\[
\boxed{
\text{finite total off-line zero set}
\quad\Longrightarrow\quad
\text{eventual nonzero finite Weil negative index}
}
\]

under Bombieri's stated hypothesis and truncation scheme.

Therefore the blanket claim

\[
\text{``a finite-dimensional Weil form necessarily averages away finitely many off-line zeros''}
\]

is false. The averaging loss belongs to specific compressed statistics, not to finite-dimensionality as such.

## 2. Relation to the `PL-259` two-moment mechanism

`PL-259` records an unconditional and genuinely positive result: a source-determined finite compression of Weil's Hermitian form plus first/second-moment arithmetic estimates forces more than two thirds of zeros to be simple and on the critical line. It also records the authors' sharp limitation that those aggregate inputs are insensitive to `o(N)` exceptional zeros.

There is no contradiction. The objects retain more information than the particular two moments extracted from them. Passing from a Hermitian matrix `Q_M` to quantities such as

\[
\operatorname{tr}Q_M,
\qquad
\|Q_M\|_{\mathrm{HS}}^2
\]

is a severe compression. A perturbation affecting only `o(N)` spectral directions can disappear from normalized first/second moments while still changing the exact negative index by an integer amount. Bombieri's theorem shows that, in the finite-total-defect regime, the latter information eventually survives.

This distinction sharpens the falsification test suggested by `PL-259`. A proposed successor observable need not identify each bad zero separately. It is enough, in principle, to prove a cofinal sign theorem of the form

\[
\text{any off-line divisor}
\Longrightarrow
\exists M_0\ \forall M\ge M_0:\ n_-(Q_M)>0,
\]

or an appropriate asymptotic variant. Bombieri establishes exactly this type of conclusion when the total off-line set is finite; extending such control beyond that hypothesis is the substantive missing problem.

## 3. Prime-exponent interpretation

The arithmetic input of Weil's completed explicit formula remains the same axis-ray projection already audited in `PL-013` and `PL-259`. Writing

\[
n=\prod_p p^{v_p(n)},
\qquad
E(v(n))=\langle v(n),(\log p)_p\rangle=\log n,
\]

one has

\[
\Lambda(n)\ne0
\quad\Longleftrightarrow\quad
v(n)=r e_p
\]

for some prime `p` and integer `r>=1`. Hence the non-archimedean source of the Weil form is supported on the prime-power coordinate rays, with frequencies `r log p` and weights derived from the von Mangoldt function.

Bombieri's finite-defect stabilization therefore supplies a genuine example in which **prime-axis explicit-formula data plus the completed zero-side geometry can preserve an integer-valued sparse defect that normalized moment statistics lose**. It does not show that the full mixed-prime exponent lattice is needed, and it does not create a new operator from the bare Bohr torus. The mechanism still depends on the completed Weil functional, including the archimedean and pole contributions.

This matters for the research mandate because it changes what kind of spectral information is worth seeking. The target is not another generic matrix whose low moments reproduce known zero statistics; it is a source-forced family whose **inertia is complete enough** that an exceptional zero configuration cannot hide in the truncation limit.

## 4. What remains open after the finite-defect theorem

Bombieri's theorem is conditional on the off-line zero set being finite. It does not, as quoted here, establish a general stabilization law for an infinite zero-density off-line divisor. That distinction is essential: a hypothetical RH failure could involve infinitely many off-line zeros while still contributing zero density among all zeros, precisely the regime that normalized two-moment arguments cannot exclude.

The present audit therefore leaves a narrower and more falsifiable target:

\[
\boxed{
\text{control the negative-index growth/completeness of a cofinal source-forced Weil truncation family}
}
\]

without assuming finiteness of the off-line divisor. A useful theorem could take several forms: monotone/cofinal detection of every negative Weil direction, a quantitative lower bound on negative index from off-line zeros in growing height ranges, or a completeness theorem showing that the chosen finite test spaces eventually approximate every negative vector of the global Weil form strongly enough to preserve sign.

None of those statements is proved here. In particular, the finite-total theorem cannot simply be passed to an infinite sparse zero set by taking limits: negative directions may drift with the truncation scale, and uniform approximation/sign margins would have to be controlled.

## 5. Analytic-continuation and source audit

No Euler product is continued into the critical strip in this finding. The relevant object is Weil's **completed explicit formula and quadratic functional**, which already incorporate the meromorphic continuation, the archimedean contribution, the pole terms, and the nontrivial zero divisor. The von Mangoldt expansion is used only to identify the non-archimedean source with prime-power axis rays, an identity valid in the classical explicit-formula framework.

This also prevents a generic-geometry misreading. The negative-index theorem is not a property of an arbitrary Hermitian truncation built from frequencies `log p`; it belongs to a specific quadratic form forced by the completed zeta explicit formula. Matched Beurling or Helson systems can reproduce broad prime-frequency or continuation phenomena, but Bombieri's theorem here is a statement about the ordinary Riemann-zeta Weil functional and its actual zero divisor.

## 6. Prior art and novelty audit

Primary source:

- **Enrico Bombieri**, “Remarks on Weil’s quadratic functional in the theory of prime numbers, I,” *Atti Accad. Naz. Lincei Rend. Lincei Mat. Appl.* **11**(3) (2000), 183--233. This is already recorded in `research/prime_lattice/SOURCES.md` entry 26. Its abstract explicitly states both the Weil positivity equivalence and the finite-defect negative-index stabilization used here.

The theorem itself is entirely Bombieri's. `PL-259` already cites Bombieri as prior art for the negative-index viewpoint, so this finding does not claim discovery of inertia as a mechanism. The durable addition is the **sharp logical boundary** that was not made explicit there: sparse blindness of the Alpöge--Furman/Lamzouri first-two-moment argument does not extend to the full cofinal truncation family in the finite-total-defect case.

A targeted repository audit found no earlier `PL-*` finding whose main claim is Bombieri's exact finite-defect stabilization or this moment-observability/form-observability split. The nearest stored findings are `PL-013` (Weil finite spectral route and unresolved limit), `PL-066` (moving-band rightmost-zero certificate), and `PL-259` (unconditional positive-proportion localization and its sparse-exception limit). Search absence is not evidence of originality; the theorem is explicitly classified as classical prior art.

## 7. Adversarial boundaries

1. **This does not prove RH or density one.** The theorem is conditional on there being only finitely many off-line zeros and says how the truncation inertia behaves in that counterfactual regime.

2. **It does not identify the locations of the off-line zeros.** The stabilized negative index counts a defect; it is not a divisor-complete spectral reconstruction.

3. **Do not transfer the theorem automatically to another Galerkin family.** Bombieri's finite truncations, the Connes--Consani--Moscovici truncations of `PL-013`, and the Alpöge--Furman compression of `PL-259` are related through Weil's form but are not asserted here to have identical inertia at equal finite parameters.

4. **Moment blindness remains valid.** A finite number of negative directions contributes `o(N)` to normalized bulk statistics as `N->infinity`; Bombieri's theorem does not rescue an argument that only ever keeps those moments.

5. **The infinite sparse case is not obtained by compactness for free.** A sequence of finite subsets of off-line zeros does not by itself produce uniform sign margins or stable negative directions in a prescribed cofinal truncation.

6. **The full exponent lattice is still not the primitive source.** The non-archimedean Weil channel sees prime powers, hence axis rays. Any claim that mixed-prime geometry solves the remaining inertia-completeness problem requires an additional theorem showing how those interior lattice points enter the completed form.

## Consequence for the research line

`PL-259` should be read as a boundary on **aggregate moment methods**, not on finite-dimensional Weil observability itself. Classical prior art already proves that the full finite-truncation family can detect every finite-total RH defect through eventual negative index.

The next viable direction is therefore broader and sharper than an individually localized per-zero certificate: study whether a canonical cofinal truncation of the completed Weil form has a negative-index completeness/stability law strong enough for arbitrary sparse off-line divisors. Such a theorem would still need arithmetic control of the source-forced form; merely computing more moments, inventing another self-adjoint matrix, or observing numerical negative eigenvalues without a sign-stability theorem would not cross the boundary.