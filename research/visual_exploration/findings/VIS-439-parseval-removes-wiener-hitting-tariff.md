# VIS-439 — Parseval removes the Wiener charge from buffered hitting variance

## Claim

For a finite nonzero Wang Laurent shell `F_N` on its base-prime torus with Haar probability `m_H`, let `S_N=||F_N||_infinity`, `X_N=|F_N|^2/S_N^2 in [0,1]`, and let `q:[0,1]->[0,1]` be a real polynomial of degree at most `d`. Define `Q=q(X_N)`, `qbar=int Q dm_H` and the symmetric occupation `L_(q,rho)(z)=int_(-rho)^rho Q(z tau(u))du` for `rho>0`. Let `delta^*_(N,d)` be the `VIS-425` structural mixed divisor: the minimum nonzero frequency magnitude among sums of at most `d` original shell-frequency differences (with `+infinity` when there are none).

Writing `c_m` for Fourier coefficients of `Q` and `lambda_m=<m,(log p)_p>`, the exact occupation variance satisfies

`Var_H(L_(q,rho)) = 4 sum_(m!=0)|c_m|^2 sin^2(rho lambda_m)/lambda_m^2`

` <= 4 min(rho^2,(delta^*_(N,d))^(-2)) Var_H(Q)`

` <= 4 qbar(1-qbar) min(rho^2,(delta^*_(N,d))^(-2))`

` <= min(rho^2,(delta^*_(N,d))^(-2)).`

For a strict near-band Wang dyadic shell of arithmetic height `Y_N`, the `VIS-425` product-ratio floor `delta^*_(N,d)>=(2Y_N)^(-2d)` yields

`Var_H(L_(q,rho)) <= min(rho^2,(2Y_N)^(4d)).`

For the thresholded Bernstein/Chernoff separator `q=q_(d,M)` of `VIS-433` with `0<a<b<1`, target mass `mu_b=m_H{X_N>=b}`, leakage `epsilon=exp(-d I(theta;a,b))`, `m_0=(1-epsilon)mu_b`, and positive margin `D=m_0-epsilon>0`, the symmetric hitting time `H_a` of `{X_N>=a}` obeys, with `B=min(rho^2,(delta^*_(N,d))^(-2))`,

`m_H{H_a>rho} <= B m_0(1-m_0)/(B m_0(1-m_0)+rho^2 D^2) <= B/(B+4rho^2 D^2).`

The first inequality retains the target-mass floor inside the joint Cantelli mean/variance ratio. It is stronger whenever `m_0` differs from `1/2`; no new Wiener tariff is introduced.

**No Wiener `l^1` coefficient factor enters this bounded-separator Haar second-moment certificate.** The previous `4 A_(d,M)(W_N^2)^2/(delta^*)^2` bound in `VIS-437` and `VIS-438`'s optimization of its exponent remain correct but unnecessary for this particular `l^2` route.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL PARSEVAL/PLANCHEREL AND CANTELLI + REPRESENTATION-TARIFF SHARPENING + NO-NOVELTY-CLAIM`.

## Derivation

The torus normalization gives `0<=X_N<=1`, hence `0<=Q<=1`. A nonconstant character of `q(X_N)` is a sum of at most `d` shell-frequency differences; its nonzero flow frequency has magnitude at least `delta^*_(N,d)` regardless of power-basis coefficient cancellation or Wiener growth.

By `VIS-430`, integration of each nonzero character over `[-rho,rho]` multiplies it by `2 sin(rho lambda_m)/lambda_m`. Haar character orthogonality yields the exact variance identity. The inequality `|sin(rho lambda_m)/lambda_m|<=min(rho,1/|lambda_m|)` then yields the first upper bound.

Crucially, apply Parseval **before** summing absolute coefficient values:

`sum_(m!=0)|c_m|^2 = int Q^2 dm_H-qbar^2 = Var_H(Q).`

Since `0<=Q<=1`, `Q^2<=Q` and therefore `Var_H(Q)<=qbar(1-qbar)<=1/4`. The constant `4` in the variance identity cancels the universal `1/4` bound. If `Q` is constant, the nonzero Fourier sum vanishes and the claimed bound is immediate. Inserting the `VIS-425` structural floor proves the explicit strict near-band bound.

For the thresholded Bernstein separator, `VIS-433` proves `Q<=epsilon` on `{X_N<=a}` and `Q>=1-epsilon` on `{X_N>=b}`. Write `v=qbar`; the latter inequality gives `v>=m_0=(1-epsilon)mu_b>epsilon`. Avoidance `H_a>rho` implies `L_(q,rho)<=2rho epsilon`. Retaining the **actual** mean `E_H[L]=2rho v` and its matching Parseval variance inside Cantelli gives

`m_H{H_a>rho} <= B v(1-v)/(B v(1-v)+rho^2(v-epsilon)^2).`

The right side is nonincreasing in `v`: the inverse-signal ratio `g(v)=(v-epsilon)^2/[v(1-v)]` has derivative

`g'(v)=(v-epsilon)[v(1-2epsilon)+epsilon]/[v^2(1-v)^2]>0`

for `epsilon<v<1`. Indeed `m_0>epsilon` and `m_0<=1-epsilon` force `epsilon<1/2`; `v=1` follows by continuity (the variance is zero). Thus the worst admissible mean is `v=m_0`, proving the mass-aware claim. **Substitution occurs in the joint Cantelli ratio, not in the variance alone**: the lower bound `v>=m_0` does not independently imply `Var(Q)<=m_0(1-m_0)`. Finally `m_0(1-m_0)<=1/4` recovers the previous universal bound. No independence, mixing, or new approximation assumption is used.

## Consequence and boundary

`VIS-437` computes a correct weighted Wiener upper bound for the thresholded polynomial, and `VIS-438` correctly optimizes that inflated bound's exponential rate with the Chernoff leakage. Parseval detects cancellation in the **final bounded separator** and removes their coefficient-space surcharge from this specific second moment. The frequency floor and the degree `d` remain essential.

When `rho delta^*<=1`, the estimate only gives `B=rho^2` and is usually weak. In the divisor regime `rho delta^*>=1`, the mass-aware certificate tends to zero when `rho delta^* D >> sqrt(m_0(1-m_0))`. For rare targets `mu_b->0` with prescribed leakage `epsilon<=c mu_b`, where fixed `c<1`, one has `m_0~mu_b` and `D>=(1-c-o(1))mu_b`. Thus the sufficient radius scale improves from the universal `rho delta^*>>mu_b^(-1)` to `rho delta^*>>mu_b^(-1/2)`. The strict near-band divisor floor yields the coarse sufficient scale `rho>>(2Y_N)^(2d) mu_b^(-1/2)`, with constants depending on `c`. If the buffer shrinks, `VIS-433` still makes the certified degree grow as `log(1/mu_b)/C_Ber(a,b)`, so the small divisor can remain severe. This is not a cover-time law or evidence of an arithmetic height-selector anomaly.

The Wiener tariffs of `VIS-423`–`VIS-425` remain relevant for **Gram-block versus Haar comparison**, and the degree restriction is unavailable for a hard target indicator without smoothing. The present result neither verifies the actual transported Wang coefficients against the Gram/Haar null nor implies anything about RH.

## Prior art, representation audit and falsification

Parseval/Plancherel for Fourier series is classical; see Elias M. Stein and Rami Shakarchi, *Fourier Analysis: An Introduction*, Princeton Lectures in Analysis I (2003). The `[0,1]` variance bound is elementary, and Cantelli is the classical hitting step already used in `VIS-431`. Retaining the same mean in the variance and in Cantelli's denominator is an algebraic sharpening of those classical inputs, not a new general probability inequality. There is no new general Fourier theorem, hitting-time theorem, small-divisor estimate or RH implication. The Mathia contribution is exposing a **material avoidable loss** in its active Wang occupation certificate.

This is an intrinsic torus argument, insensitive to relabelling base-prime coordinates, a common source-phase translation, plotting scales or color choices. No finite raster evidence or post-hoc parameter search is used. A genuine falsifier would violate the bounded separator range, the depth-`d` frequency support, nonresonance of nonzero prime-log characters, Parseval, or Cantelli. An arbitrary unbounded-range polynomial loses the `1/4` energy bound; a nonpolynomial hard indicator need not have finite-depth Fourier support.

## Dependencies and research consequence

`VIS-425` supplies the mixed-frequency divisor; `VIS-430` the exact occupation identity; `VIS-431` and `VIS-433` the bounded buffered separator, leakage and positive mass margin; `VIS-437`–`VIS-438` the valid but unnecessarily charged Wiener alternative. For a selected quiet interval, first compare `VIS-429`'s Haar rarity lower tail with this **mass-aware**, Wiener-free upper-tail certificate at the same threshold, buffer and radius. The certified rare-target radius penalty is square-root rather than inverse target mass when leakage is proportional to mass, but an inconclusive sufficient upper bound is not evidence of a selector anomaly; the remaining growing Fourier resource is the depth-priced small divisor (or a sharper actual weighted Fourier variance).
