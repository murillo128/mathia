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

For the thresholded Bernstein/Chernoff separator `q=q_(d,M)` of `VIS-433` with `0<a<b<1`, target mass `mu_b=m_H{X_N>=b}`, leakage `epsilon=exp(-d I(theta;a,b))` and positive margin `D=(1-epsilon)mu_b-epsilon>0`, the symmetric hitting time `H_a` of `{X_N>=a}` obeys, with `B=min(rho^2,(delta^*_(N,d))^(-2))`,

`m_H{H_a>rho} <= B/(B+4rho^2 D^2).`

**No Wiener `l^1` coefficient factor enters this bounded-separator Haar second-moment certificate.** The previous `4 A_(d,M)(W_N^2)^2/(delta^*)^2` bound in `VIS-437` and `VIS-438`'s optimization of its exponent remain correct but unnecessary for this particular `l^2` route.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL PARSEVAL/PLANCHEREL AND CANTELLI + REPRESENTATION-TARIFF SHARPENING + NO-NOVELTY-CLAIM`.

## Derivation

The torus normalization gives `0<=X_N<=1`, hence `0<=Q<=1`. A nonconstant character of `q(X_N)` is a sum of at most `d` shell-frequency differences; its nonzero flow frequency has magnitude at least `delta^*_(N,d)` regardless of power-basis coefficient cancellation or Wiener growth.

By `VIS-430`, integration of each nonzero character over `[-rho,rho]` multiplies it by `2 sin(rho lambda_m)/lambda_m`. Haar character orthogonality yields the exact variance identity. The inequality `|sin(rho lambda_m)/lambda_m|<=min(rho,1/|lambda_m|)` then yields the first upper bound.

Crucially, apply Parseval **before** summing absolute coefficient values:

`sum_(m!=0)|c_m|^2 = int Q^2 dm_H-qbar^2 = Var_H(Q).`

Since `0<=Q<=1`, `Q^2<=Q` and therefore `Var_H(Q)<=qbar(1-qbar)<=1/4`. The constant `4` in the variance identity cancels the universal `1/4` bound. If `Q` is constant, the nonzero Fourier sum vanishes and the claimed bound is immediate. Inserting the `VIS-425` structural floor proves the explicit strict near-band bound.

For the thresholded Bernstein separator, `VIS-433` proves `Q<=epsilon` on `{X_N<=a}` and `Q>=1-epsilon` on `{X_N>=b}`. Avoidance `H_a>rho` implies `L_(q,rho)<=2rho epsilon`, while `E_H[L_(q,rho)]-2rho epsilon>=2rho D`. Cantelli's one-sided lower-tail bound therefore gives `Var(L)/(Var(L)+4rho^2 D^2)`. The fraction is increasing in `Var(L)`, so substitution of the new bound gives the stated hitting inequality. No independence, mixing, or new approximation assumption is used.

## Consequence and boundary

`VIS-437` computes a correct weighted Wiener upper bound for the thresholded polynomial, and `VIS-438` correctly optimizes that inflated bound's exponential rate with the Chernoff leakage. Parseval detects cancellation in the **final bounded separator** and removes their coefficient-space surcharge from this specific second moment. The frequency floor and the degree `d` remain essential.

When `rho delta^*<=1`, the estimate only gives `B=rho^2` and is usually weak. For a small certified avoidance tail through the divisor regime one needs `rho delta^* D>>1`; the coarse strict near-band sufficient scale is `rho D>>(2Y_N)^(2d)`. If `mu_b` tends to zero or the buffer shrinks, `VIS-433` still makes the necessary certified degree grow as `log(1/mu_b)/C_Ber(a,b)`, so the small divisor may become severe. This is not a cover-time law or evidence of an arithmetic height-selector anomaly.

The Wiener tariffs of `VIS-423`–`VIS-425` remain relevant for **Gram-block versus Haar comparison**, and the degree restriction is unavailable for a hard target indicator without smoothing. The present result neither verifies the actual transported Wang coefficients against the Gram/Haar null nor implies anything about RH.

## Prior art, representation audit and falsification

Parseval/Plancherel for Fourier series is classical; see Elias M. Stein and Rami Shakarchi, *Fourier Analysis: An Introduction*, Princeton Lectures in Analysis I (2003). The `[0,1]` variance bound is elementary, and Cantelli is the classical hitting step already used in `VIS-431`. There is no new general Fourier theorem, hitting-time theorem, small-divisor estimate or RH implication. The Mathia contribution is exposing a **material avoidable loss** in its active Wang occupation certificate.

This is an intrinsic torus argument, insensitive to relabelling base-prime coordinates, a common source-phase translation, plotting scales or color choices. No finite raster evidence or post-hoc parameter search is used. A genuine falsifier would violate the bounded separator range, the depth-`d` frequency support, nonresonance of nonzero prime-log characters, Parseval, or Cantelli. An arbitrary unbounded-range polynomial loses the `1/4` energy bound; a nonpolynomial hard indicator need not have finite-depth Fourier support.

## Dependencies and research consequence

`VIS-425` supplies the mixed-frequency divisor; `VIS-430` the exact occupation identity; `VIS-431` and `VIS-433` the bounded buffered separator, leakage and positive mass margin; `VIS-437`–`VIS-438` the valid but unnecessarily charged Wiener alternative. For a selected quiet interval, first compare `VIS-429`'s Haar rarity lower tail with this Wiener-free upper-tail certificate at the **same** threshold, buffer and radius. An inconclusive sufficient upper bound is not evidence of a selector anomaly; the remaining growing Fourier resource is the depth-priced small divisor (or a sharper actual weighted Fourier variance).
