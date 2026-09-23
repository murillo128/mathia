# VIS-405 — a fixed Lipschitz quantile budget is exactly a uniform mass floor

## Claim

Continue in the fixed-`m_1` rank-one qutrit setting of `VIS-388`--`VIS-404`, where the normalized positive spectrum is parameterized by one residual coordinate on a compact interval

`I=[a,b]`, with length `ell=b-a`.

Let `nu` be a Borel probability law on `I`, let

`F(x)=nu((-∞,x])`,

and let `Q=F^{-1}` denote its generalized quantile, extended by `Q(0)=a`, `Q(1)=b`. If `U~Uniform(0,1)`, then `Q(U)~nu`.

Fix a numerical decoder budget `L>0` **before** inspecting `nu`. The following are equivalent:

1. the monotone quantile decoder `Q:[0,1]->I` is `L`-Lipschitz;
2. for every `a<=x<y<=b`,

   `F(y)-F(x) >= (y-x)/L`;
3. as measures on `I`,

   `nu >= (1/L) Leb_I`;
4. necessarily `L>=ell`, and when `L>ell` there is a probability law `eta` on `I` such that

   `nu = (1/L) Leb_I + (1-ell/L) eta`.

   At the sharp boundary `L=ell`, the only admissible law is the uniform law `Leb_I/ell`.

Thus `VIS-404` has a precise quantitative boundary. A fixed latent prior plus merely qualitative monotonicity or a target-dependent finite Lipschitz constant is universal, but a **pre-specified numerical Lipschitz budget is genuinely falsifiable**. Its entire restriction is an explicit absolutely-continuous floor: every interval of residual width `delta` must carry at least `delta/L` probability mass.

Equivalently, after rescaling the residual interval to `[0,1]`, the `L`-Lipschitz monotone-decoder family is exactly

`nu = (1/L) Leb_[0,1] + (1-1/L) eta`, `L>=1`.

The remaining mass `eta` is arbitrary. So a fixed Lipschitz budget does not impose Gaussianity, unimodality, moment closure, or a particular copula; it imposes one specific capacity constraint and nothing stronger.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL MONOTONE-TRANSPORT CHARACTERIZATION + CONTROL/CAPACITY BOUNDARY + NO-NOVELTY-CLAIM`.

No Wang-derived numerical value of `L`, source anomaly, arithmetic gain, zeta-zero statement, or RH consequence is claimed.

## 1. Lipschitz quantile implies the CDF slope floor

Assume `Q` is nondecreasing and `L`-Lipschitz. Since it is continuous, its image is the whole interval `I`; in particular the pushforward law has no support gap inside `I`.

For `x<y` in `I`, let `r_x` be the right end of the level set `{p:Q(p)=x}` and `r_y` the right end of `{p:Q(p)=y}`. The standard quantile/CDF correspondence gives

`r_x=F(x)`, `r_y=F(y)`.

Therefore

`y-x = Q(r_y)-Q(r_x) <= L(r_y-r_x) = L(F(y)-F(x))`,

hence

`F(y)-F(x) >= (y-x)/L`.

This already gives a direct falsification rule: if any interval `(x,y]` carries mass smaller than `(y-x)/L`, no monotone `L`-Lipschitz decoder from the fixed uniform latent can generate the target law.

## 2. The CDF floor implies an `L`-Lipschitz quantile

Conversely assume

`F(y)-F(x) >= (y-x)/L`

for every `x<y` in `I`. Let `0<=p<q<=1`, and set

`x=Q(p)`, `y=Q(q)`.

If `x=y` there is nothing to prove. Suppose `x<y`. For every `epsilon>0` small enough, `y-epsilon>x`; by the defining generalized-inverse property,

`F(y-epsilon)<q`, while `F(x)>=p`.

Hence

`q-p > F(y-epsilon)-F(x) >= (y-epsilon-x)/L`.

Letting `epsilon` decrease to zero gives

`Q(q)-Q(p)=y-x <= L(q-p)`.

Thus `Q` is `L`-Lipschitz.

The argument allows atoms. Flat pieces of `Q` create atoms in `nu`; they do not violate the upper derivative bound. What is forbidden is the opposite phenomenon: a support gap or a region with too little target mass, because that would force the quantile to traverse output distance too quickly.

## 3. Measure domination and the contamination form

The increment inequality is exactly

`nu((x,y]) >= (1/L) Leb((x,y])`

for every half-open interval inside `I`. These intervals generate the Borel sigma-algebra, so equivalently

`nu >= (1/L) Leb_I`

as finite measures.

Taking total mass gives the necessary capacity condition

`1 = nu(I) >= ell/L`,

so `L>=ell`.

When `L>ell`, the positive measure

`rho = nu - (1/L) Leb_I`

has total mass

`rho(I)=1-ell/L`.

Normalizing it gives a probability law `eta=rho/(1-ell/L)` and hence

`nu = (1/L) Leb_I + (1-ell/L) eta`.

Conversely every law of this form dominates `(1/L)Leb_I`, so its generalized quantile is `L`-Lipschitz by the previous section.

At `L=ell`, the residual mass is zero and the uniform law is forced. As `L` grows, the mandatory uniform floor weakens and the admissible family approaches the unrestricted class from `VIS-404`.

## 4. Consequence for the qutrit nuisance frontier

`VIS-404` showed that fixing `U~Uniform(0,1)` and allowing an arbitrary monotone quantile decoder leaves every Borel residual law admissible. It also noted that saying only “the decoder has some finite Lipschitz constant” is still target-dependent and therefore non-diagnostic.

The present result identifies exactly what changes once a **numerical** constant is frozen independently. A proposed source-free null of the form

`u=Q(U)`, `Lip(Q)<=L`

is no longer universal. It predicts the explicit interval-mass floor

`nu((x,y]) >= (y-x)/L`.

This is a valid capacity test, but it is not yet a Wang control merely because it is mathematically falsifiable. The number `L` must still come from the source-packet mechanism, an independently fixed coefficient/basis budget, a packet incidence rule, or another pre-candidate admissibility argument. Choosing `L` after looking at the target simply recreates the `VIS-404` escape in quantitative form.

The exact contamination representation also prevents over-interpreting rejection or acceptance. Passing the `L`-budget test says only that the residual contains the required uniform floor; the excess law `eta` can still be arbitrary. Failing it rejects that frozen decoder family, not the full class of source-free mechanisms.

## 5. Prior art and novelty audit

The underlying probability/transport facts are classical. Sergey Bobkov and Michel Ledoux, *One-Dimensional Empirical Measures, Order Statistics, and Kantorovich Transport Distances*, Memoirs of the American Mathematical Society 261 (2019), no. 1259, DOI `10.1090/memo/1259`, Appendix A.6, Proposition A.24, characterize monotone Lipschitz transports through inverse-distribution/I-function bounds. For a uniform source, their criterion specializes to a quantitative lower bound on the target distribution's inverse-density/I-function, equivalently an upper Lipschitz bound on the quantile. The generalized-quantile pushforward itself is the classical inversion construction already audited in `VIS-404`.

Reference manuscript used for the exact Appendix A.6 statement:

`https://perso.math.univ-toulouse.fr/ledoux/files/2016/12/MEMO.pdf`

No novelty is claimed for generalized quantiles, monotone transport, Lipschitz inverse criteria, or measure domination. The Mathia-specific contribution is the explicit capacity interpretation for the current one-dimensional qutrit residual: a frozen Lipschitz decoder budget is neither vacuous nor a broad shape model; it is exactly a mandatory uniform mass floor plus arbitrary excess measure.

## Boundaries

- The theorem concerns the canonical monotone transport from a fixed uniform latent to the one-dimensional residual. It does not characterize higher-dimensional latent decoders or non-monotone maps.
- Atoms are allowed. A fixed Lipschitz budget forbids support gaps/insufficient interval mass, not atoms or arbitrary singular/atomic excess on top of the uniform floor.
- If the decoder budget is allowed to depend on the observed target, the test loses its force: any target with finite quantile Lipschitz constant can choose its own `L`, and arbitrary Borel laws remain covered by unrestricted monotone transport as in `VIS-404`.
- A fixed polynomial/basis/coefficient family may imply a Lipschitz budget, but can impose additional restrictions. This finding isolates only the consequences of the Lipschitz constant itself.
- No argument here derives a Wang/source-packet value of `L`. That remains the load-bearing step for `CLUE-wang-fixed-source-packet-localization`.
- No retained visualization is required because the result is an exact one-dimensional transport/capacity characterization.

## Dependencies

- `VIS-389`: the fixed-`m_1` generic rank-one qutrit spectrum has one residual coordinate.
- `VIS-403`: unrestricted finite-latent conditional-independence language is non-identifying.
- `VIS-404`: a fixed uniform latent with arbitrary monotone quantile decoder remains universal.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose admissible nuisance family must be fixed before target inspection.

## Research consequence

A numerical decoder regularity budget is now a concrete, testable object rather than a qualitative phrase. If a Wang/source-packet derivation proposes `Lip(Q)<=L`, the first exact check is the interval-mass floor `nu((x,y]) >= (y-x)/L`; after rescaling to `[0,1]`, this is the equivalent decomposition `nu=L^(-1)Leb+(1-L^(-1))eta`.

The next unresolved step is not to invent a better target-dependent decoder. It is to derive an independently fixed `L` (or a stronger joint decoder restriction) from Wang/source-packet mathematics and then test the actual residual against that predeclared boundary.