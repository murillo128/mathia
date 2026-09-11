# VIS-166 — anchored Haar collision moments are finite exactly below support dimension

## Claim

Keep the anchored held-out-prime Haar control from `VIS-164`. Let

`X=(X_1,...,X_d)` and `Y`

be independent Haar-uniform coordinates on `T^d` and `T`, and define

`R(X)=sqrt(sum_(j=1)^d sin^2(pi X_j))`,

`N(Y)=|sin(pi Y)|`,

`C=N(Y)/R(X)`

away from the Haar-null set `R(X)=0`, with any value assigned on that null set.

Then for every real `s>0`,

`E[C^s] < infinity` if and only if `s<d`.

At the critical order `s=d` the divergence is logarithmic, while for `s>d` it is polynomial. More precisely, if

`M_s(B)=E[min(C,B)^s]`,

then, with the tail constant `c_d` from `VIS-164`,

- for `0<s<d`, `M_s(B)` converges to `E[C^s]` and

  `E[C^s]-M_s(B) ~ [s c_d/(d-s)] B^(s-d)`;
- for `s=d`,

  `M_d(B) ~ d c_d log B`;
- for `s>d`,

  `M_s(B) ~ [s c_d/(s-d)] B^(s-d)`.

Moreover, for every fixed cap `B<infinity`, the anchored prime-log sequence from `VIS-164` obeys

`lim_(Q->infinity) Q^(-1) sum_(q<=Q) min(C_q,B)^s = M_s(B)`.

Thus the matched held-out-prime null has an exact **moment threshold at the retained support dimension**. Raw collision moments of order `s>=d` are intrinsically dominated by the generic near-return singularity and are not stable population statistics even before any zeta-specific effect is introduced.

**Evidence/status:** `EXACT-DERIVED + HAAR-NULL CONSEQUENCE + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This is not a theorem about uncapped empirical moments along the deterministic prime-log orbit, a jointly growing cap `B=B(Q)`, an extreme-value law, growing support, zeta, or RH.

## 1. Haar factorization reduces the moment question to one inverse radial integral

Because `X` and `Y` are independent,

`E[C^s] = E[N(Y)^s] E[R(X)^(-s)]`

whenever the right-hand side is finite; for nonnegative variables the same factorization also identifies divergence through Tonelli.

The numerator is harmless for every `s>0`:

`E[N(Y)^s] = int_0^1 |sin(pi y)|^s dy`
` = Gamma((s+1)/2)/(sqrt(pi) Gamma((s+2)/2))`.

It is finite and strictly positive. Therefore the entire integrability threshold comes from the retained-phase denominator `R(X)`.

## 2. The inverse radial moment is finite exactly for `s<d`

The zero set of `R` on `T^d` is the torus origin. In signed local coordinates `u` around that point,

`sin(pi u_j)=pi u_j+O(u_j^3)`,

so

`R(u)=pi ||u||_2 (1+O(||u||_2^2))`.

Away from a sufficiently small neighborhood of the origin, `R` is bounded below by a positive constant and contributes no integrability problem. Near the origin, the inverse moment is therefore comparable to

`int_0^epsilon r^(d-1-s) dr`.

This integral is finite exactly when `s<d`. At `s=d` it diverges like `log(1/r)`, and for `s>d` it has a power divergence.

This local calculation is the moment-side form of the support-dimension tail in `VIS-164`: after one retained prime is anchored exactly, the remaining `d` retained phases must approach a `d`-dimensional small ball to generate a large collision score.

## 3. The tail law gives the exact capped-moment growth

For every nonnegative random variable and every `s,B>0`, the layer-cake identity gives

`E[min(C,B)^s] = s int_0^B t^(s-1) P(C>t) dt`.

`VIS-164` proves

`P(C>t)=mu_d(t) ~ c_d t^(-d)`.

For `s>d`, Karamata integration of this regularly varying tail — or direct comparison with the displayed power law — yields

`M_s(B) ~ [s c_d/(s-d)] B^(s-d)`.

At the boundary `s=d`, the integrand is asymptotic to `d c_d/t`, hence

`M_d(B) ~ d c_d log B`.

For `0<s<d`, the full moment is finite and the missing tail satisfies

`E[C^s]-M_s(B)`
` = s int_B^infinity t^(s-1) P(C>t) dt`
` ~ [s c_d/(d-s)] B^(s-d)`.

So the tail exponent from `VIS-164` and the local radial calculation give the same threshold independently.

## 4. Fixed caps transfer to the anchored deterministic orbit

For fixed `B`, define on `T^(d+1)`

`f_(s,B)(x,y)=min(|sin(pi y)|/sqrt(sum_j sin^2(pi x_j)), B)^s`,

with an arbitrary value at the simultaneous zero where the quotient is undefined.

This function is bounded. Its only possible discontinuity from the quotient singularity is contained in a Haar-null set, so it is Riemann integrable. The rational independence proved in `VIS-164` and discrete Kronecker--Weyl equidistribution therefore give

`Q^(-1) sum_(q<=Q) f_(s,B)(q alpha_1,...,q alpha_d,q beta)`
` -> int_(T^(d+1)) f_(s,B) = M_s(B)`.

Equivalently,

`Q^(-1) sum_(q<=Q) min(C_q,B)^s -> M_s(B)`

for every fixed cap.

The cap is essential to this immediate argument. Ordinary equidistribution of bounded Riemann-integrable observables does not justify removing `B` after `Q->infinity`, nor does it control a cap that grows with `Q`.

## 5. Consequence for collision statistics

The dimension-coded null now constrains not only exceedance tails but the choice of summary statistic. At retained support dimension `d`, a raw `s`-th collision moment with `s>=d` has no finite Haar population target. Increasing sample size can therefore expose ever larger generic near-return contributions even when the data are exactly behaving like the matched omitted-prime control.

A source-sensitive zeta comparison should not interpret growth of such raw high moments as evidence. Safer predeclared statistics include fixed quantiles, exceedance probabilities at controlled thresholds, bounded/capped losses, or fractional moments with `s<d`; if a growing cap or a high-order moment is used, its dimension-dependent Haar growth must be included explicitly in the null.

This strengthens the same methodological boundary as `VIS-164` and `VIS-165`: support dimension is part of the null model, not a cosmetic parameter. Changing retained support can change both the collision-tail exponent and which moments even exist.

## 6. Prior art and novelty boundary

The probability facts used here are classical. The layer-cake representation of positive moments is standard, and the conversion of a regularly varying tail into truncated-moment asymptotics is a direct instance of Karamata integration. A standard reference for regular variation and Karamata theory is N. H. Bingham, C. M. Goldie, and J. L. Teugels, **Regular Variation**, Cambridge University Press, 1987, DOI `10.1017/CBO9780511721434`.

No novelty is claimed for moment-tail identities, Karamata theory, local Euclidean integrability, or Kronecker--Weyl averaging of bounded observables. The Mathia-specific content is the specialization to the canonical collision control already derived in `VIS-164`: its support-dimension exponent is exactly the boundary between finite and divergent collision moments, giving a concrete null-design rule for later source-sensitive tests.

## 7. Boundaries and falsification

The statement concerns the fixed finite-support Haar control and fixed caps when transferring back to anchor indices. It does not establish convergence of the uncapped empirical average

`Q^(-1) sum_(q<=Q) C_q^s`

even when `s<d`; that requires a uniform-integrability or shrinking-target argument beyond ordinary equidistribution. It also does not determine the finite-`Q` growth of divergent empirical moments for `s>=d`.

`VIS-165` supplies quantitative discrepancy for collision exceedance sets and therefore suggests that some growing-cap regimes may be accessible, but deriving the optimal joint `B(Q),Q` moment law is a separate question and is not imported here.

Falsify the threshold by finding a neighborhood of the denominator zero whose Haar volume is not `d`-dimensional to first order, or by showing that the `VIS-164` tail is incompatible with the displayed layer-cake asymptotics. Either would contradict the established local geometry or tail calculation.

## Research consequence

The held-out-prime control has a sharp statistic-design boundary: collision moments exist exactly below order `d=|P|-1`. Any proposed zeta-facing moment statistic should therefore be chosen relative to support dimension before data inspection, and high-order or growing-cap statistics must be normalized against the corresponding heavy-tail null rather than treated as intrinsically more sensitive evidence.