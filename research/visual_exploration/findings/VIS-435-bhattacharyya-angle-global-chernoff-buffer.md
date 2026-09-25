# VIS-435 — Bhattacharyya angle gives a global Chernoff buffer certificate

## Claim

Let `0<=a<b<=1` and let `C_Ber(a,b)` denote the Bernoulli Chernoff information from `VIS-433`, extended to the endpoints by its standard Chernoff definition. Put

`phi(x)=arcsin(sqrt(x))`,

`Delta=phi(b)-phi(a)`.

Then

`C_Ber(a,b) >= -log[sqrt(ab)+sqrt((1-a)(1-b))] = -log cos(Delta) >= Delta^2/2`.

For the Wang amplitude thresholds `a=t^2`, `b=(t+eta)^2`, `0<=t<t+eta<=1`,

`Delta=arcsin(t+eta)-arcsin(t)>=eta`,

so globally

`C_Ber(t^2,(t+eta)^2) >= -log cos(eta) >= eta^2/2`.

Hence, whenever `mu_b=m{Y>=b}>0`, the thresholded-Bernstein separator of `VIS-433` may safely use

`d > log((1+mu_b)/mu_b)/[-log cos(Delta)]`,

or the simpler threshold-uniform certificate

`d > (2/eta^2) log((1+mu_b)/mu_b)`.

Exact Bernoulli endpoints are nonsingular. For `a=0<b<1`, take `q_d(x)=1-(1-x)^d`; its lower leakage is zero and upper leakage is at most `(1-b)^d`. For `0<a<1=b`, take `q_d(x)=x^d`; its upper leakage is zero and lower leakage is at most `a^d`. Their monomial `l^1` norms are at most `2^d` and `1`, so the existing `3^d` Wang Wiener bound remains valid.

Thus endpoint motion does not create an additional scalar approximation tariff. The scalar cost is controlled by the actual amplitude buffer and target mass; the surviving Wang question is whether the growing-depth Wiener/small-divisor tariff remains useful.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL BHATTACHARYYA/CHERNOFF INPUT + REPRESENTATION-CERTIFIED + GLOBAL ENDPOINT-UNIFORM BOUND + NO-NOVELTY-CLAIM`.

No new Chernoff-information, Bhattacharyya-distance, information-geometry, hitting-time, Wang-selector, or RH theorem is claimed.

## 1. Chernoff dominates the symmetric Bhattacharyya slice

For Bernoulli laws the Chernoff affinity is

`rho_s(a,b)=a^s b^(1-s)+(1-a)^s(1-b)^(1-s)`.

Since `C_Ber=-log inf_s rho_s`, evaluating at `s=1/2` gives

`C_Ber(a,b)>=-log[sqrt(ab)+sqrt((1-a)(1-b))]`.

This is the ordinary Bhattacharyya distance between the two Bernoulli laws.

## 2. The affinity is exactly an angular cosine

Write `a=sin^2(alpha)` and `b=sin^2(beta)` with `0<=alpha<beta<=pi/2`. Then

`sqrt(ab)+sqrt((1-a)(1-b))`
` = sin(alpha)sin(beta)+cos(alpha)cos(beta)`
` = cos(beta-alpha)`.

Hence the symmetric Bhattacharyya distance is exactly `-log cos(Delta)` in the square-root/arcsine coordinate. This identity is global and requires no fixed-interior Taylor expansion.

Moreover, for `0<=x<pi/2`,

`-log cos(x)>=x^2/2`,

because the derivative of the difference is `tan(x)-x>=0`. Therefore `C_Ber>=Delta^2/2`.

## 3. Wang amplitude buffers have a threshold-uniform price

For `a=t^2`, `b=(t+eta)^2`,

`Delta=arcsin(t+eta)-arcsin(t)`.

Since `(arcsin x)'=1/sqrt(1-x^2)>=1`, one has `Delta>=eta`. Therefore

`C_Ber(t^2,(t+eta)^2)>=eta^2/2`

uniformly in `t`. The local expansion from `VIS-434`, `C_Ber=eta^2/[2(1-t^2)]+O_t(eta^3)`, remains sharper for fixed interior `t`, but its nonuniform remainder is no longer needed for a valid global certificate.

When `a=0`, the direct polynomial `1-(1-x)^d` has exact exponent `-log(1-b)=C_Ber(0,b)`. When `b=1`, `x^d` has exact exponent `-log a=C_Ber(a,1)`. Thus the endpoint parameterization itself is not an obstruction.

## 4. Prior art, audit, and falsification

A. Bhattacharyya, **On a measure of divergence between two statistical populations defined by their probability distributions**, *Bulletin of the Calcutta Mathematical Society* 35 (1943), 99--109, MR0010358, is the classical source of the Bhattacharyya coefficient/distance. Chernoff's 1952 testing-exponent paper and the information-geometric source already cited for `VIS-433`--`VIS-434` delimit the remaining background.

No novelty is claimed for the Bhattacharyya coefficient, Chernoff information, square-root probability embedding, statistical angle, or `-log cos(x)>=x^2/2`. The Mathia delta is the exact specialization to the persisted Wang hitting certificate: the `s=1/2` Chernoff slice removes the fixed-interior caveat left by `VIS-434`.

Falsify the result by finding a failure of the Chernoff-versus-Bhattacharyya inequality, the cosine identity, the global `-log cos` bound, `Delta>=eta`, or the endpoint polynomial/Wiener-depth statements.

## Dependencies

- `VIS-425`: depth-`d` Wang structural divisor.
- `VIS-430`: occupation variance turns finite Fourier control into a hitting upper bound.
- `VIS-433`: Chernoff-balanced thresholded-Bernstein separator.
- `VIS-434`: local Fisher/arcsine small-buffer geometry.

## Research consequence

For buffered Wang hitting, price the scalar separator in the intrinsic arcsine amplitude coordinate. A changing threshold `t_N` is not itself a surviving representation escape. After target mass and amplitude buffer are paid, any failure must lie in the growing-depth Wang coefficient/small-divisor geometry or in a different source-sensitive observable.
