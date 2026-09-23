# VIS-403 — unrestricted finite-latent conditional independence is vacuous for the qutrit residual

## Claim

Continue in the generic rank-one qutrit setting of `VIS-388`--`VIS-402`. Fix the positive support

`0 < q_1 < q_2 < q_3`

and a first moment

`m_1=sum_i q_i w_i=x`

for which the admissible simplex slice is parameterized affinely by the residual coordinate `u` from `VIS-389`:

`w=w(u)=(w_1(u),w_2(u),w_3(u))`.

Let `nu` be **any** Borel probability law on the admissible residual interval. Then there is a one-dimensional latent variable `L` and conditionally independent sector amplitudes whose normalized squared energies have exactly residual law `nu`.

Take

`L ~ nu`

and, for any fixed `T>0`, define deterministic conditional amplitudes

`S_i = sqrt(T w_i(L))`.

Then

`Y_i=S_i^2=T w_i(L)`

and therefore

`W_i=Y_i/(Y_1+Y_2+Y_3)=w_i(L)`.

The first moment is identically `x`, and the residual coordinate of `W` is exactly `L`, hence has law `nu`.

Conditional on `L`, each `S_i` is deterministic. Degenerate random variables are mutually independent, so the three sector amplitudes are conditionally independent given this **one-dimensional** latent state.

More generally, for any finite random vector `S=(S_1,...,S_k)`, taking the latent state to be `L=S` makes the coordinates conditionally independent given `L`: the conditional joint law is the point mass `delta_L`, which factors as the product of its coordinate point masses.

Therefore **the bare existence of a finite-dimensional latent state that restores conditional independence is not an intrinsic restriction on a finite-dimensional Wang residual**. In the qutrit fixed-`m_1` problem, even one latent scalar is enough to reproduce an arbitrary residual law if its law and decoder are allowed to be chosen from the target distribution.

The useful statistical/mathematical content must consequently lie in restrictions imposed **before inspecting the candidate**: a fixed latent law, fixed decoder/loadings, restricted interaction family, independently justified packet mechanism, source-free physical semantics, complexity bound with testable consequences, or a Wang admissibility theorem that narrows the family. Conditional independence after an unrestricted latent representation is not itself evidence or a falsification criterion.

**Evidence/status:** `EXACT-DERIVED + DEGENERATE-LATENT REPRESENTATION + NEGATIVE IDENTIFIABILITY/CONTROL RESULT + CLASSICAL CONDITIONAL-INDEPENDENCE TAUTOLOGY + NO-NOVELTY-CLAIM`.

No Wang anomaly, arithmetic source signal, destination gain, zeta-zero statement, or RH consequence is claimed.

## 1. Conditional independence becomes automatic when the latent contains the observation

Let `S=(S_1,...,S_k)` be any finite random vector and set `L=S`.

For bounded measurable functions `phi_i`, every `phi_i(S_i)` is measurable with respect to `sigma(L)`. Hence

`E[prod_i phi_i(S_i) | L] = prod_i phi_i(S_i)`

while separately

`E[phi_i(S_i) | L] = phi_i(S_i)`.

Thus

`E[prod_i phi_i(S_i) | L] = prod_i E[phi_i(S_i) | L]`,

which is exactly mutual conditional independence of the coordinates given `L`.

Equivalently, at a realized latent value `l=(s_1,...,s_k)`, the conditional law is

`delta_l = delta_(s_1) x ... x delta_(s_k)`.

This argument uses no Gaussianity, Gamma structure, additive factorization, moment assumptions, density assumptions, or smoothness. It is a statement about what happens when the latent representation itself is unrestricted.

## 2. The qutrit residual needs only one latent scalar

The general `L=S` construction uses a latent with the dimension of the full sector vector. The fixed-`m_1` qutrit problem is even more restrictive geometrically: `VIS-389` shows that the admissible normalized spectral slice is one-dimensional.

Let `U` have any target residual law `nu` and set `L=U`. The affine map `w(U)` already reconstructs all three normalized sector weights. Choosing any fixed total energy `T>0` and

`S_i=sqrt(T w_i(U))`

produces the exact desired normalized spectrum after squaring. Boundary points with `w_i=0` simply produce a zero deterministic amplitude in that sector.

Thus latent dimension is not a useful complexity discriminator here. An arbitrary qutrit residual law can be hidden in one scalar latent variable unless the law of that latent and the map from latent state to sector amplitudes are independently restricted.

The same conclusion holds if deterministic signs are attached to the square roots, or if a separate independently specified positive radial variable multiplies all sector amplitudes: radial normalization removes that common scale and leaves the residual law unchanged.

## 3. Relation to the calibrated packet ladder

`VIS-394`--`VIS-402` progressively enlarge **mechanistically specified** source-free nulls. Their force comes from the fact that packet counts, rate/amplitude laws, incidence architecture, loadings, latent law and other nuisance choices are fixed independently of the Wang residual being judged. Under those restrictions, the induced simplex/residual law is a real prediction and can falsify a candidate mechanism.

The present result does not weaken those controls. It marks the opposite boundary: once the latent representation is allowed to absorb the observed residual itself, conditional independence can always be manufactured and the null loses falsifiability.

This also sharpens the distinction exposed by `VIS-393`. Source-stabilizer symmetry alone can realize arbitrary qutrit weight laws. `VIS-403` shows independently that **unrestricted latent conditional-independence language has the same identifiability failure**: the condition is only informative relative to a pre-declared latent/decoder family.

## 4. Consequence for the Wang packet-localization clue

`VIS-402` left open interactions that do not reduce to conditionally independent sector amplitudes after conditioning on an admitted finite latent state. That wording is useful only if “admitted” carries an independently fixed mechanistic restriction.

Without such a restriction there is no invariant notion of “still dependent after every finite latent state”: the latent can simply encode the residual coordinate, or the whole sector vector, and make the conditional distribution degenerate and factorized.

The next coherent Wang test therefore must **first derive or pre-register the allowed latent/interaction family** from mathematics external to the candidate residual. Only then can failure of conditional independence, violation of an induced inequality, support restriction, moment relation, phase constraint, or other consequence count as source information.

A proposed source-free control should be killed as vacuous if its latent law or decoder is chosen after looking at the candidate, if its admitted family can encode an arbitrary law on `u`, or if increasing latent freedom removes every falsifiable prediction.

## Prior-art and novelty audit

The mathematical ingredients are elementary classical probability. Conditional independence is defined relative to a conditioning sigma-algebra; when the conditioned variables are measurable with respect to that sigma-algebra, the factorization above is immediate. Latent-variable and local-independence models are informative only because they restrict the latent state and observation kernels rather than allowing the latent to encode the full observation.

No new theorem about latent-variable models, conditional independence, disintegration, identifiability, or compositional probability is claimed. The Mathia-specific result is the exact qutrit-Wang boundary: **finite-latent conditional independence cannot serve as a representation-independent escape criterion unless the admissible latent mechanism is fixed independently of the residual; one latent scalar can otherwise reproduce any fixed-`m_1` residual law**.

## Boundaries

- The exact one-dimensional construction uses degenerate conditional amplitudes. It proves non-identifiability of the unrestricted latent criterion; it does not say that every restricted smooth/noisy latent family can represent every residual law exactly.
- Requiring absolutely continuous idiosyncratic noise, fixed decoder regularity, bounded parameter complexity, prescribed latent dimension together with a prescribed decoder family, or another independently justified mechanism can restore testable restrictions. Those restrictions must be stated before inspecting the candidate.
- The result does not invalidate `VIS-394`--`VIS-402`, because those findings study specific independently frozen source-free mechanisms rather than arbitrary fitted latent representations.
- A source-derived Wang theorem may legitimately force a special latent/interaction architecture. Such a theorem would create new mathematics precisely because it narrows the otherwise vacuous representation class.
- The finding does not establish which restricted latent family Wang admissibility actually selects, whether the real source residual violates it, or whether any surviving effect yields a destination gain.
- No retained visualization is required because the result is an exact representation/identifiability statement once the one-dimensional qutrit residual parameterization is fixed.
