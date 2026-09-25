# VIS-434 — Chernoff geometry identifies the intrinsic small-buffer coordinate

## Claim

Fix an interior Bernoulli parameter `p in (0,1)` and let `delta>0` with `p+delta<1`. Let `C_Ber(p,p+delta)` be the optimized Bernoulli Chernoff information from `VIS-433`, equivalently

`C_Ber(p,p+delta)=D(theta_*||p)=D(theta_*||p+delta)`,

where

`theta_* = log((1-p)/(1-p-delta)) / log((p+delta)(1-p)/(p(1-p-delta)))`.

As `delta->0` with `p` fixed,

`theta_* = p + delta/2 + O_p(delta^2)`

and

`C_Ber(p,p+delta) = delta^2/[8p(1-p)] + O_p(delta^3)`.

Thus the optimized separator is locally governed by the Bernoulli Fisher metric

`ds_F^2 = dp^2/[p(1-p)]`:

`C_Ber(p,p+delta) = (1/8) ds_F^2 + O_p(delta^3)`

for the infinitesimal displacement `dp=delta`.

Equivalently, in the intrinsic arcsine coordinate

`phi(p)=arcsin(sqrt(p))`,

for which `ds_F^2=4 dphi^2`,

`C_Ber(p,p+delta) = (1/2) [phi(p+delta)-phi(p)]^2 + O_p(delta^3)`.

For the Wang squared-amplitude thresholds used in `VIS-431`--`VIS-433`,

`p=t^2,qquad p+delta=(t+eta)^2`,

with fixed `t in (0,1)` and `eta->0+`, this becomes

`C_Ber(t^2,(t+eta)^2) = eta^2/[2(1-t^2)] + O_t(eta^3)`.

Consequently the optimized sufficient Bernstein depth from `VIS-433` has local leading coefficient

`d > [2(1-t^2)/eta^2 + O_t(eta^(-1))] log((1+mu_b)/mu_b)`,

whereas the universal Hoeffding certificate of `VIS-432` has leading coefficient

`d > [1/(2t^2 eta^2) + O_t(eta^(-1))] log((1+mu_b)/mu_b)`.

Their leading-coefficient ratio is

`4t^2(1-t^2)<=1`,

with equality only at `t^2=1/2`. Hence the apparent `t^(-2)` penalty produced by measuring a small amplitude buffer through the raw squared-amplitude gap `(t+eta)^2-t^2` is not intrinsic to the Chernoff-balanced separator. At fixed interior `t`, the natural local buffer coordinate is `arcsin(t)), and the remaining divergence is still quadratic in the amplitude gap `eta`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL INFORMATION-GEOMETRIC INTERPRETATION + REPRESENTATION-CERTIFIED + LOCAL ASYMPTOTIC + NO-NOVELTY-CLAIM`.

No endpoint-uniform asymptotic, new Chernoff theorem, new Fisher-information theorem, Wang selector anomaly, hitting-time asymptotic, or RH consequence is claimed.

## 1. The Chernoff balance point is locally the midpoint

Write

`A(delta)=log((1-p)/(1-p-delta))`

and

`B(delta)=log((p+delta)(1-p)/(p(1-p-delta)))`.

For fixed interior `p`, Taylor expansion gives

`A(delta)=delta/(1-p)+delta^2/[2(1-p)^2]+O_p(delta^3)`

and

`B(delta)=delta/[p(1-p)] + (2p-1)delta^2/[2p^2(1-p)^2] + O_p(delta^3)`.

Dividing the two series yields

`theta_*=A(delta)/B(delta)=p+delta/2+O_p(delta^2)`.

Thus the optimal threshold from `VIS-433` is asymptotically the ordinary midpoint in probability space, but its error exponent is not Euclidean in that coordinate.

## 2. Relative entropy exposes the local metric

For `h->0` at fixed `p in (0,1)`,

`D(p+h||p)=h^2/[2p(1-p)] + O_p(h^3)`.

Substituting

`h=theta_*-p=delta/2+O_p(delta^2)`

gives

`D(theta_*||p)=delta^2/[8p(1-p)] + O_p(delta^3)`.

By the defining balance relation from `VIS-433`, this is exactly the same leading expansion as `D(theta_*||p+delta)`, so it is the local expansion of `C_Ber(p,p+delta)`.

The coefficient `1/[p(1-p)]` is the Fisher information of the Bernoulli family. With

`phi=arcsin(sqrt(p))`,

one has

`dphi/dp=1/[2sqrt(p(1-p))]`

and therefore

`dp^2/[p(1-p)]=4dphi^2`.

This makes the small-buffer Chernoff cost locally Euclidean in `phi` rather than in raw `p`.

## 3. Squared Wang amplitude hides that local geometry

The hitting construction uses the normalized squared amplitude `Y=X_N=A_N^2`, so an amplitude buffer from `t` to `t+eta` appears in probability space as

`delta=(t+eta)^2-t^2=2t eta+eta^2`.

For fixed `t in (0,1)`,

`p(1-p)=t^2(1-t^2)`.

Substituting these into the Fisher expansion cancels the leading `t^2` from the squaring map:

`C_Ber(t^2,(t+eta)^2)`
` = (2t eta+eta^2)^2/[8t^2(1-t^2)] + O_t(eta^3)`
` = eta^2/[2(1-t^2)] + O_t(eta^3)`.

The same fact is immediate from the intrinsic coordinate because

`phi(t^2)=arcsin(t)`

for `t in [0,1]`, and hence

`phi((t+eta)^2)-phi(t^2)=eta/sqrt(1-t^2)+O_t(eta^2)`.

Therefore the low-threshold `t^(-2)` blow-up in the coarse Hoeffding/Pinsker coefficient is a coordinate-level looseness of that universal bound, not a necessary cost of the optimized separator.

## 4. Comparison with the universal Hoeffding certificate

From `VIS-432`, with

`g=(t+eta)^2-t^2=2t eta+eta^2`,

the sufficient degree has leading coefficient

`2/g^2 = 1/[2t^2 eta^2] + O_t(eta^(-1))`.

From `VIS-433` and the expansion above,

`1/C_Ber = 2(1-t^2)/eta^2 + O_t(eta^(-1))`.

The ratio of the optimized to universal leading coefficients is therefore

`4t^2(1-t^2)`.

It never exceeds one, as required by the global Pinsker comparison in `VIS-433`, and equals one only at `t^2=1/2`. Away from that central squared-amplitude level, the local Chernoff geometry gives a strictly smaller leading depth requirement.

This does **not** remove the `eta^(-2)` shrinking-buffer cost. It removes only the extra coordinate-dependent low-`t` penalty in the universal certificate.

## 5. Prior art, representation audit, and falsification

Frank Nielsen, **An Information-Geometric Characterization of Chernoff Information**, *IEEE Signal Processing Letters* 20:3 (2013), 269--272, DOI `10.1109/LSP.2013.2243726`, gives an information-geometric characterization of Chernoff information for exponential families, including multinomial families. The Fisher metric of the Bernoulli family and the arcsine/square-root coordinate are classical information geometry.

No novelty is claimed for Chernoff information, Fisher information, the Bernoulli statistical manifold, or the local quadratic expansion of relative entropy. The Mathia contribution is the representation audit of the already persisted Wang hitting certificate: after `VIS-433` optimizes the separator, translate its local information geometry back through the squared-amplitude map and identify which part of the apparent shrinking-buffer tariff was introduced by the coarse coordinate-level bound.

The statement is local for fixed `t in (0,1)`. It is not uniform as `t->0` or `t->1`; any regime coupling `t=t_N` to `eta_N` needs a separate endpoint analysis. That nonuniformity is part of the evidence boundary rather than evidence for a Wang anomaly.

Falsify the finding by finding an error in the expansion of `theta_*`, the second-order Bernoulli-KL expansion, the Fisher/arcsine coordinate identity, or the substitution `p=t^2`, `delta=(t+eta)^2-t^2`.

## Dependencies

- `VIS-432`: universal Hoeffding depth certificate in the raw squared-amplitude gap.
- `VIS-433`: Chernoff-balanced separator and exact optimized degree coefficient.

## Research consequence

For a fixed interior amplitude threshold and a small pre-registered buffer, price the scalar-separator depth with the exact Chernoff information, or locally with the arcsine-amplitude gap, rather than interpreting the raw squared-amplitude Hoeffding coefficient as intrinsic.

The live arithmetic obstruction is unchanged: the Wang Wiener/small-divisor machinery must remain useful at the resulting growing depth. A separate question begins only when the amplitude threshold itself approaches an endpoint together with the shrinking buffer, because the present local expansion is then nonuniform.
