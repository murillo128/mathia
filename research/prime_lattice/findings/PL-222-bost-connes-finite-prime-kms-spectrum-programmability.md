# PL-222 — Finite prime-channel KMS correlation weights are independently programmable

## Claim

The bounded Bost–Connes correlation channel left open by `PL-220` has no finite-dimensional arithmetic rigidity in its prime-frequency weights. Fix any inverse temperature `beta>0` for which a Bost–Connes `KMS_beta` state `phi_beta` exists, any finite set of distinct primes `F`, and arbitrary nonnegative target weights

\[
(w_p)_{p\in F}.
\]

Let `mu_p` be the canonical Bost–Connes isometry of gauge degree `p`, so

\[
\sigma_t(\mu_p)=p^{it}\mu_p,
\qquad
\mu_p^*\mu_p=1.
\]

Then the bounded self-adjoint observable

\[
X_F=\sum_{p\in F}
\left(\sqrt{w_p}\,\mu_p+\sqrt{w_p}\,\mu_p^*\right)
\]

has equilibrium autocorrelation

\[
\boxed{
C_{X_F}(t)
=
\phi_\beta\!\left(X_F\sigma_t(X_F)\right)
=
\sum_{p\in F}w_p
\left(p^{it}+p^{-\beta}p^{-it}\right).
}
\]

Equivalently, in the notation of `PL-220`,

\[
\boxed{
c_p=w_p,
\qquad
c_{p^{-1}}=p^{-\beta}w_p,
\qquad p\in F,}
\]

with no cross-prime terms. Thus the positive-frequency masses on any finite collection of prime directions can be chosen independently; the opposite masses are then fixed only by the generic KMS detailed-balance factor.

This freedom survives a **positive-contraction** requirement. If `B>=||X_F||` and

\[
Y_F=\frac12\left(1+\frac{X_F}{B}\right),
\]

then `0<=Y_F<=1`, while for every `p in F`

\[
\boxed{
c_p(Y_F,Y_F)=\frac{w_p}{4B^2},
\qquad
c_{p^{-1}}(Y_F,Y_F)=p^{-\beta}\frac{w_p}{4B^2}.}
\]

Hence positivity and a norm-one budget preserve arbitrary **relative** finite prime-channel weights, up to one common scale. More strongly, any prescribed finite vector of sufficiently small absolute weights is realized exactly: taking coefficients `2 sqrt(w_p)` gives the desired `c_p=w_p` whenever, for example, the sufficient triangle-norm condition

\[
4\sum_{p\in F}\sqrt{w_p}\le1
\]

holds.

Therefore the caveat left in `PL-220` can be closed at finite prime support: neither the individual correlation weights, their positivity, nor KMS reciprocity supplies a source-forced relation among finitely many rational-prime channels. Any surviving arithmetic rigidity must be genuinely **global/infinite**, involve higher joint data not reducible to finitely many two-point masses, or use structure outside ordinary bounded same-state KMS correlations.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE/CONTROL + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`.

## 1. Exact Bost–Connes calculation

The standard rational Bost–Connes system has multiplicative isometries `mu_n` with

\[
\mu_m\mu_n=\mu_{mn},
\qquad
\mu_n^*\mu_n=1,
\qquad
\sigma_t(\mu_n)=n^{it}\mu_n.
\]

By `PL-219`, every KMS state is invariant under the full compact prime-gauge action. In particular the expectation of every nonzero gauge grade vanishes.

The KMS condition already fixes the range-projection weight of each prime isometry. With the convention

\[
\phi_\beta(ab)
=
\phi_\beta\!\left(b\,\sigma_{i\beta}(a)\right)
\]

for analytic `a,b`, set `a=mu_p^*` and `b=mu_p`. Since

\[
\sigma_{i\beta}(\mu_p^*)=p^\beta\mu_p^*,
\]

we get

\[
1
=
\phi_\beta(\mu_p^*\mu_p)
=
p^\beta\phi_\beta(\mu_p\mu_p^*),
\]

hence

\[
\boxed{\phi_\beta(\mu_p\mu_p^*)=p^{-\beta}.}
\]

Now write

\[
X_F=\sum_{p\in F}(a_p\mu_p+\overline{a_p}\mu_p^*),
\qquad |a_p|^2=w_p.
\]

For distinct primes `p!=q`, every mixed product occurring in

\[
\phi_\beta(X_F\sigma_t(X_F))
\]

has nonzero gauge degree: `pq`, `(pq)^{-1}`, `p/q`, or `q/p`. Gauge invariance kills all of them. The only neutral products are

\[
\mu_p^*\mu_p=1
\]

and

\[
\mu_p\mu_p^*,
\]

which gives the displayed autocorrelation formula exactly.

There is no use of an Euler product or analytic continuation here. The statement is entirely inside the real-temperature KMS theory of the Bost–Connes `C*`-system.

## 2. Positive contractions do not restore finite-channel rigidity

The self-adjoint `X_F` need not be positive. This does not provide an escape. Choose any `B>=||X_F||`; then `A_F=X_F/B` is a self-adjoint contraction and

\[
Y_F=(1+A_F)/2
\]

is a positive contraction.

The zero gauge component of `X_F` is zero, so

\[
E_1(Y_F)=1/2,
\qquad
E_p(Y_F)=\frac{a_p}{2B}\mu_p,
\qquad
E_{p^{-1}}(Y_F)=\frac{\overline{a_p}}{2B}\mu_p^*.
\]

Using the coefficient formula from `PL-220`,

\[
c_q(Y_F,Y_F)
=
\phi_\beta\!\left(E_q(Y_F)^*E_q(Y_F)\right),
\]

gives

\[
c_p=\frac{|a_p|^2}{4B^2},
\qquad
c_{p^{-1}}=p^{-\beta}\frac{|a_p|^2}{4B^2}.
\]

Thus the map from coefficient magnitudes `(|a_p|^2)` to the positive-frequency prime masses is diagonal and has no arithmetic coupling between different primes. The normalization needed to make the observable positive and contractive changes all nonzero prime masses by the same scalar only.

For an explicit absolute-budget version, choose `a_p=2 sqrt(w_p)` and take `B=1`. The triangle estimate

\[
\|X_F\|
\le
2\sum_{p\in F}|a_p|
=
4\sum_{p\in F}\sqrt{w_p}
\]

shows that `4 sum sqrt(w_p)<=1` is sufficient for `Y_F=(1+X_F)/2` to be a positive contraction with **exactly** `c_p=w_p` and `c_{p^{-1}}=p^{-beta}w_p`.

The inequality is only a convenient sufficient norm budget; no sharp norm claim is needed for the programmability conclusion.

## 3. Matched generic control

The mechanism is not specific to rational primes or to the arithmetic part of the Bost–Connes algebra. Let `(A,alpha)` be any `C*`-dynamical system with a `KMS_beta` state `phi` and isometries `V_j` satisfying

\[
\alpha_t(V_j)=e^{itE_j}V_j,
\qquad
V_j^*V_j=1,
\qquad E_j>0.
\]

The KMS identity forces

\[
\phi(V_jV_j^*)=e^{-\beta E_j}.
\]

If the finitely selected energies are distinct and their mixed sums/differences do not vanish, time invariance alone kills all mixed terms in the same construction. One obtains

\[
\phi\!\left(X\alpha_t(X)\right)
=
\sum_jw_j
\left(e^{itE_j}+e^{-\beta E_j}e^{-itE_j}\right).
\]

This is the ordinary eigen-isometry/KMS mechanism appearing broadly in semigroup and Nica–Toeplitz equilibrium theory. The rational Bost–Connes choice `E_p=log p` realizes it canonically, but does not add a finite-channel constraint beyond the energy labels themselves.

A targeted prior-art audit found this exact range-projection law as standard in the general theory of KMS states for semigroup `C*`-algebras; see, for example, Zahra Afsar, Nadia S. Larsen, and Sergey Neshveyev, “KMS States on Nica-Toeplitz C*-algebras,” *Communications in Mathematical Physics* **378** (2020), 1875–1929, DOI `10.1007/s00220-020-03711-6`, together with the classical Bost–Connes system already registered as source 5 in `research/prime_lattice/SOURCES.md`. No novelty is claimed for the KMS calculation or for the finite superposition argument.

The line-specific durable result is the **matched-control closure** of a live loophole from `PL-220`: even after keeping the canonical prime directions, exact KMS dynamics, self-adjointness, positivity, and a bounded norm budget, arbitrary finite relative prime-channel autocorrelation masses remain possible.

## 4. What this does and does not close

This finding closes only finite-support **two-point spectral-weight rigidity** for ordinary bounded same-state KMS correlations. It does not prove that an arbitrary infinite `ell^1` sequence of weights on `Q_+^times` can be realized by one bounded Bost–Connes observable. Passing from finite support to an infinite prescribed spectrum introduces convergence and norm constraints that are not addressed here.

It also does not program the full multi-time correlation hierarchy. Higher correlations can contain multiplicative neutrality relations among several grades, and a global invariant coupling infinitely many such coefficients remains logically possible. The finding says that any such invariant cannot be detected from a fixed finite collection of two-point prime masses alone.

The construction does not use analytic continuation of `zeta`, its zero divisor, the functional equation, or a completed archimedean factor. Consequently it provides no mechanism that can single out `beta=1/2`: the same construction works for every inverse temperature at which a KMS state exists, and the only reflection law is the generic factor `p^{-beta}`.

Nor does this affect unbounded affiliated observables, relative modular operators between genuinely noncommuting states, renormalized infinite traces, scattering constructions, or adelic/Weil positivity. Those remain outside the bounded finite-correlation control.

## 5. Falsification / audit tests

The finding would require correction or narrowing if any of the following failed:

1. the Bost–Connes generators `mu_p` were not isometries with `sigma_t(mu_p)=p^{it}mu_p`;
2. a Bost–Connes KMS state did not satisfy `phi_beta(mu_p mu_p^*)=p^{-beta}`;
3. gauge invariance did not annihilate mixed products of distinct nonzero prime grades;
4. the `p`-spectral component of the constructed `X_F` or `Y_F` contained contributions from another prime `q!=p`;
5. the positive-contraction affine normalization changed the relative nonzero prime weights by anything other than a common scalar; or
6. the same finite-weight construction failed in a generic KMS system with matched eigen-isometries and nonresonant energies.

All six tests are elementary consequences of the `C*` relations, KMS identity, and spectral grading and do not depend on RH.

## Consequence for the research line

`PL-219` removes noncommutativity from bounded one-point KMS readouts; `PL-220` shows that bounded two-point correlations have pure-point prime-gauge spectra and leaves possible rigidity in their weights; `PL-222` now removes **finite prime-support weight rigidity**, even under positivity and a norm budget.

The surviving Bost–Connes route must therefore cross a genuinely global threshold. A viable mechanism needs an infinite/source-forced compatibility among prime channels, a higher-order relation that cannot be reduced to arbitrary finite marginals, or an object outside ordinary bounded same-state correlations. Merely observing a special finite pattern of prime-frequency masses near `beta=1/2` cannot be evidence for an RH mechanism, because the same pattern can be inserted by hand inside the canonical Bost–Connes system itself.