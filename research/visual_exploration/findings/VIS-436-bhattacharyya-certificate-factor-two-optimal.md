# VIS-436 — Bhattacharyya angular depth is globally factor-two optimal inside the Chernoff separator family

## Claim

For probability laws `P,Q`, define `rho_s(P,Q)=int p^s q^(1-s) dmu`, `0<=s<=1`, the Bhattacharyya coefficient `B_c=rho_(1/2)`, Bhattacharyya distance `B=-log B_c`, and Chernoff information `C=-log inf_s rho_s`.

Then

`B(P,Q) <= C(P,Q) <= 2 B(P,Q)`.

Both constants are sharp. For Bernoulli laws with parameters `a,b`, `VIS-435` identifies

`B(a,b)=-log cos(Delta)`,  `Delta=arcsin(sqrt(b))-arcsin(sqrt(a))`.

Hence the exact Bernoulli Chernoff information obeys the sharp global sandwich

`-log cos(Delta) <= C_Ber(a,b) <= -2 log cos(Delta)`.

If `L_mu=log((1+mu_b)/mu_b)`, the exact real degree price from `VIS-433`, `d_C=L_mu/C_Ber`, and the symmetric angular price from `VIS-435`, `d_B=L_mu/[-log cos(Delta)]`, satisfy

`d_C <= d_B <= 2 d_C`.

Thus the intrinsic Bhattacharyya/arcsine separator is globally within a factor two of the optimal thresholded-Bernstein Chernoff degree, and factor two is the best uniform constant.

For Wang thresholds `a=t^2`, `b=(t+eta)^2`, the comparison applies to the intrinsic angular certificate. The coarser fallback `2/eta^2` from `VIS-435` is only a simpler sufficient bound and is not claimed to share the same factor-two optimality near endpoints.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL CHERNOFF/BHATTACHARYYA INPUT + REPRESENTATION-CERTIFIED + SHARP GLOBAL COMPARISON + NO-NOVELTY-CLAIM`.

No new general Chernoff theorem, Bhattacharyya theorem, Wang selector theorem, hitting-time law, or RH consequence is claimed.

## 1. Universal factor-two comparison

Hölder gives `0<=rho_s<=1`. Cauchy--Schwarz applied to

`sqrt(pq)=[p^(s/2)q^((1-s)/2)][p^((1-s)/2)q^(s/2)]`

gives

`B_c^2 <= rho_s rho_(1-s)`.

Because `rho_(1-s)<=1`, one gets `rho_s>=B_c^2` for every `s`. Therefore `inf_s rho_s>=B_c^2`, hence `C<=2B`.

Conversely `inf_s rho_s<=rho_(1/2)=B_c`, so `C>=B`.

## 2. Sharpness

For Bernoulli parameters `a=0`, `0<b<1`,

`C_Ber(0,b)=-log(1-b)=2[-log sqrt(1-b)]=2B(0,b)`.

So the upper factor two is attained.

For `0<a<1/2` and `b=1-a`, the affinity satisfies `rho_s(a,1-a)=rho_(1-s)(a,1-a)`. Since `log rho_s` is convex and symmetric about `1/2`, its minimum is at `s=1/2`. Thus `C_Ber(a,1-a)=B(a,1-a)`, attaining the lower constant.

## 3. Consequence for the Wang separator

`VIS-433` prices the optimized thresholded-Bernstein separator by `L_mu/C_Ber`. `VIS-435` prices the symmetric angular separator by `L_mu/B`. Since `B<=C_Ber<=2B`,

`1 <= d_B/d_C = C_Ber/B <= 2`.

Integer rounding changes only an additive `O(1)` degree. No Wang coefficient, divisor, or source arithmetic enters this comparison.

Near a fixed interior small buffer, `VIS-434` implies `C_Ber/B -> 1`, so the symmetric angular certificate is locally asymptotically optimal. The factor-two loss is an endpoint phenomenon and is genuinely sharp there.

## 4. Prior art, representation audit, and falsification

Bhattacharyya's 1943 coefficient/distance and Chernoff's 1952 optimized testing exponent are classical, and the sources already recorded for `VIS-433`--`VIS-435` delimit that background. The inequality here is an elementary consequence of Cauchy--Schwarz, Hölder, and the standard affinity definitions; no novelty is claimed for it as a general statistical-divergence inequality.

The Mathia delta is the representation audit: the explicit arcsine/Bhattacharyya coordinate from `VIS-435` is certified to be globally constant-factor optimal relative to the fully optimized thresholded-Bernstein Chernoff separator.

Falsify the result by violating the Cauchy--Schwarz product inequality, Hölder's `rho_s<=1` bound, either sharpness example, the `VIS-435` cosine identity, or the algebraic conversion from exponent to degree.

## Dependencies

- `VIS-433`: exact optimized Bernoulli Chernoff degree.
- `VIS-434`: local Fisher/arcsine small-buffer geometry.
- `VIS-435`: global Bhattacharyya-angle certificate.

## Research consequence

For buffered Wang hitting, there is no large scalar gain left to extract merely by optimizing the Chernoff skew. Any materially stronger route must improve the growing-depth Wang Wiener/small-divisor tariff, exploit source-specific cancellation, change the destination observable, or leave the thresholded-Bernstein representation family.
