# PL-436 — Correct-order scalar variance lower bounds are known, but they do not close the oriented mod-5 cone

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + MATRIX-INFORMATION-GAP`.

**Parent findings:** `PL-421`, `PL-428`, `PL-431`, `PL-432`, `PL-435`.

## Claim

`PL-435` isolates a genuine quantitative gap between current almost-all Hardy--Littlewood pair-correlation theorems and a full Selberg-variance asymptotic at the scale needed by the local-factor route. But a full asymptotic is **stronger than the actual positivity gate requires**. The `p=5` image-cone condition of `PL-421` only asks for a fixed lower spectral margin,

\[
S_X\succeq \frac14 D_X,
\qquad
D_X:=\operatorname{Diag}(S_X),
\tag{1}
\]

or equivalently, on the positive diagonal support,

\[
C_X:=D_X^{-1/2}S_XD_X^{-1/2}\succeq \frac14 I.
\tag{2}
\]

There is already substantial classical and modern prior art proving **one-sided lower bounds at the conjectured short-interval variance scale** by positivity/explicit-formula methods. In particular, de la Bretèche--Fiorilli prove weighted second-moment lower bounds with the Montgomery--Soundararajan main scale for all admissible large scales under RH, and unconditionally along an unbounded sequence of scales. Related arithmetic-progression work gives lower bounds for residue-averaged moments or individual progressions under GRH, while unconditional lower-bound theorems are available after averaging over moduli or in growing-modulus/omega regimes.

Thus the live problem should not be stated merely as “obtain a scalar Selberg-variance asymptotic” or even “obtain a scalar lower bound of the right order.” Those mechanisms already exist in forms much closer to the needed scale than `PL-435`'s MRSTT comparison suggests.

However, they still do **not** close the Mathia gate. The required statement is a matrix coercivity theorem for **every complex residue/character direction**, whereas the established lower bounds are scalar, trace-like, diagonal, averaged, subsequential, or conditional on RH/GRH. The exact surviving target is therefore a non-circular, scale-appropriate, complex-polarized fixed-mod-5 lower-frame estimate such as

\[
\boxed{
 z^*S_X(t)z
 \ge
 \frac14\,z^*D_X(t)z-o\!\left(z^*D_X(t)z\right)
 \quad\text{uniformly for }z\in\mathbb C^4,
}
\tag{3}
\]

at the source parameters required by `PL-431`--`PL-432`, or any quantitatively equivalent statement forcing the normalized covariance spectral floor. This is weaker than a full matrix asymptotic but strictly stronger than the currently audited scalar variance lower bounds.

## 1. Why `PL-421` needs coercivity, not an asymptotic

Let the four reduced residue channels modulo `5` form a centered vector signal

\[
R_X(y,t)\in\mathbb C^4,
\]

and let the relevant integrated covariance be

\[
S_X(t)=\int R_X(y,t)R_X(y,t)^*\,d\mu_X(y)\succeq0.
\tag{4}
\]

The exact local-factor calculation in `PL-421` does not ask for a formula for every entry of `S_X(t)`. It asks whether `S_X(t)` lies in the positive image of the `p=5` dephasing map. This is exactly (1), or equivalently (2).

Hence an asymptotic of the form

\[
S_X(t)=L_XD_X(t)+o(L_XD_X(t))
\tag{5}
\]

in operator norm would certainly suffice after normalization, but it contains much more information than necessary. Any direct theorem proving the lower quadratic-form bound

\[
z^*S_X(t)z\ge c\,z^*D_X(t)z
\tag{6}
\]

with `c>1/4` eventually, or `c=1/4` with a controlled favorable remainder, would already pass the cone gate.

This matters because one-sided variance lower bounds have a substantially stronger unconditional and conditional literature than full short-interval variance asymptotics. The correct literature comparison is therefore not only with pair-correlation asymptotics, but also with explicit-formula positivity methods designed specifically to prove lower bounds.

## 2. Scalar correct-order lower bounds are established prior art

De la Bretèche and Fiorilli study the Montgomery--Soundararajan conjecture for weighted moments of primes in short intervals. For the second moment their theorem supplies a lower bound with the predicted principal scale and secondary structure throughout the stated range under RH. More importantly for route calibration, they also obtain the corresponding lower bound **unconditionally on an unbounded sequence of scales**. Their argument deliberately exploits positivity in the explicit formula rather than requiring a full pair-correlation asymptotic.

This shows that the factor-`H/L_X` first-order gap identified in `PL-435` is not a universal obstruction to obtaining a one-sided variance estimate: one can bypass absolute control of the entire triangular Hardy--Littlewood error and prove a lower bound more directly.

The arithmetic-progression analogue is also well developed. De la Bretèche--Fiorilli study moments of prime counts in reduced residue classes and prove unconditional omega/lower-bound results in ranges where the modulus varies, together with stronger all-modulus/all-scale statements under GRH and linear-independence hypotheses for more precise conclusions. Goldston--Yildirim prove, under GRH, correct-order lower bounds for the second moment in an individual arithmetic progression. Harper--Soundararajan give unconditional lower bounds for von Mangoldt variance after averaging over moduli in suitable large-modulus ranges.

These results materially narrow the missing ingredient: **one-sided second-order positivity is not itself new or unavailable technology**. What remains special to the present line is the oriented fixed-modulus matrix inequality (1)--(3).

## 3. Residue-averaged second moments control a trace, not the spectral floor

For a real centered residue vector `R(y)\in\mathbb R^4`, write

\[
S=\int R(y)R(y)^T\,d\mu(y).
\tag{7}
\]

A residue-averaged second moment of the usual form

\[
\frac14\sum_{a\in(\mathbb Z/5\mathbb Z)^\times}
\int |R_a(y)|^2\,d\mu(y)
\tag{8}
\]

is exactly `\tfrac14\operatorname{tr}S`. Passing to the normalized character basis by the unitary `C_4` Fourier matrix changes neither the trace nor the total quadratic energy. Thus a theorem for the total variance over residue classes gives a **trace lower bound**, even if it has the correct conjectural order.

Trace control cannot imply (2). An exact matched family is

\[
C_\rho=(1-\rho)I_4+\rho\mathbf1\mathbf1^T,
\qquad -\frac13\le\rho\le1.
\tag{9}
\]

Every `C_\rho` is a correlation matrix with

\[
\operatorname{diag}(C_\rho)=(1,1,1,1),
\qquad
\operatorname{tr}C_\rho=4,
\tag{10}
\]

but

\[
\operatorname{spec}(C_\rho)
=
\{1+3\rho,1-\rho,1-\rho,1-\rho\}.
\tag{11}
\]

Taking, for example, `\rho=0.9` preserves positivity, all four diagonal variances, and the total trace, while

\[
\lambda_{\min}(C_{0.9})=0.1<\frac14.
\tag{12}
\]

So even exact correct-order lower bounds for the total residue variance, or separate correct-order lower bounds for each diagonal variance, do not force local-factor image admission.

This is not a constant-factor technicality. The gate is a lower-frame condition: it asks that **no linear combination of the four residue directions nearly collapses** after normalization.

## 4. Even all real scalar probes are not enough for the oriented mod-5 gate

`PL-428` gives a stronger information obstruction. In the character basis the admissible Hermitian covariance has ten real degrees of freedom, while scalar variances of every real linear combination determine only its real symmetric part. The three invisible mod-5 directions can be represented by

\[
\Im K_{01},\qquad \Im K_{21},\qquad \Im K_{13}.
\tag{13}
\]

There are positive-semidefinite matched controls that agree on **every real quadratic probe** yet have opposite `PL-421` cone verdicts. Thus enlarging a scalar variance theorem from the principal channel to every ordinary product of Dirichlet `L`-functions still cannot recover the missing oriented covariance.

The correct coercivity target is genuinely complex-polarized:

\[
\inf_{z\ne0}
\frac{z^*S_X(t)z}{z^*D_X(t)z}
\ge\frac14+o(1),
\tag{14}
\]

with `z\in\mathbb C^4`. Equivalently, one needs the smallest generalized eigenvalue of `(S_X(t),D_X(t))`, not the trace, not the four diagonal energies, and not merely the quadratic form on `\mathbb R^4`.

`PL-431` and `PL-432` explain why the orientation is not decorative: the dyadic quarter-turn vertical displacement supplies the quadrature needed to expose the complex coherences, and the Abel--Stieltjes transport identity controls how that displacement changes the source. A useful lower-bound theorem must therefore either preserve this oriented information directly or provide another non-circular mechanism that reconstructs it.

## 5. Exact limitation of the existing lower-bound theorems

The audited literature falls short for several independent reasons.

First, the all-scale scalar lower bounds in the de la Bretèche--Fiorilli short-interval theorem use RH. For the present program the principal channel is precisely ordinary zeta, so importing RH there would be circular. Their unconditional result on an unbounded sequence of scales is genuine evidence that the expected lower magnitude occurs infinitely often, but it does not directly establish the eventual/scale-uniform cone admission pursued here. No claim is made that a cleverly redesigned RH criterion could never exploit a subsequence; only that this theorem does not supply the current gate.

Second, the arithmetic-progression lower-bound literature usually scalarizes before the estimate. Residue-averaged moments sum squared deviations over classes, hence control total energy. Individual-progression results control one coordinate. Neither object contains the mixed complex coherences needed by (14).

Third, the strongest individual-progression all-scale lower bounds in the classical Goldston--Yildirim direction are GRH-conditional. This is again unsuitable as an independent bridge when the principal character contains the Riemann zeta factor.

Fourth, the unconditional arithmetic-progression results closest to this method generally average over moduli, select a positive proportion of moduli/scales, or let the modulus grow with the main parameter. They therefore do not give a theorem specifically for the fixed modulus `5` at every sufficiently large scale.

These limitations are logically separate. Removing only the conditional hypothesis would still leave the matrix-information gap; proving only a matrix theorem on a sparse sequence would still leave the scale issue; and obtaining only the trace at fixed `5` would still leave the lower-frame issue.

## 6. Prior-art and novelty audit

The relevant prior art is:

- Régis de la Bretèche, Daniel Fiorilli, **“On a conjecture of Montgomery and Soundararajan,”** *Mathematische Annalen* **381** (2021), 575--591. DOI: https://doi.org/10.1007/s00208-021-02179-6; arXiv: https://arxiv.org/abs/2009.05760. This is the main scalar lower-bound calibration: weighted even-moment lower bounds at the Montgomery--Soundararajan scale, all admissible scales under RH and an unconditional unbounded sequence of scales.
- Régis de la Bretèche, Daniel Fiorilli, **“Moments of moments of primes in arithmetic progressions,”** *Proceedings of the London Mathematical Society* **127** (2023), 165--220. DOI: https://doi.org/10.1112/plms.12542; arXiv: https://arxiv.org/abs/2010.05944. This is the closest residue-class positivity analogue: it studies moments averaged over reduced residue classes for individual moduli, obtains unconditional omega/lower-bound phenomena in growing-modulus ranges, and gives stronger conclusions under GRH/linear-independence assumptions.
- D. A. Goldston, C. Y. Yildirim, **“On the second moment for primes in an arithmetic progression,”** *Acta Arithmetica* **100** (2001), 85--104. DOI: https://doi.org/10.4064/aa100-1-8; arXiv: https://arxiv.org/abs/math/0004149. Under GRH it gives a correct-order lower bound for an individual arithmetic progression, showing that diagonal scalar coercivity has classical conditional precedent.
- Adam J. Harper, Kannan Soundararajan, **“Lower bounds for the variance of sequences in arithmetic progressions: primes and divisor functions,”** *Quarterly Journal of Mathematics* **68** (2017), 97--123. DOI: https://doi.org/10.1093/qmath/haw005; arXiv: https://arxiv.org/abs/1602.01984. This supplies unconditional lower-bound technology after averaging over moduli and is a matched control against treating one-sided variance positivity itself as a novel mechanism.

The positivity method, Parseval/character orthogonality, correlation matrices, trace versus smallest-eigenvalue separation, and the example (9) are elementary or classical. No novelty is claimed for them.

Targeted searches of the current short-interval/AP variance and Dirichlet-character literature did not locate a theorem giving the specific unconditional, fixed-mod-5, arbitrary-complex-direction coercivity (14), nor the quarter-turn-oriented analogue required by `PL-431`--`PL-432`. That search result is only a novelty audit, not proof that no equivalent theorem exists.

The durable line-specific delta is the **theorem-strength comparison**: once the exact `PL-421` image cone and the `PL-428` blind sector are imposed, existing correct-order scalar variance lower bounds are seen to be simultaneously stronger than necessary in asymptotic precision and weaker than necessary in directional information.

## 7. Adversarial audit

1. **A full covariance asymptotic is not being smuggled back in.** Equation (14) is one-sided. It deliberately asks only for the generalized smallest-eigenvalue margin required by `PL-421`.

2. **Trace and diagonal counterexamples are admissible PSD controls.** The family (9) is positive semidefinite exactly for `-1/3<=rho<=1`; choosing `rho=0.9` is therefore a legitimate covariance geometry. It proves information insufficiency, not that the actual prime covariance behaves this way.

3. **The unconditional subsequence theorem is not dismissed as useless.** It is a genuine second-order result of the correct magnitude. It simply does not, by itself, imply scale-uniform cone admission. A different criterion built to use a subsequence would require a separate proof.

4. **Conditional results are not evidence against the desired inequality.** RH/GRH-based lower bounds show compatibility and provide technique, but they cannot serve as the independent arithmetic premise of an RH proof through the principal zeta channel.

5. **Growing-modulus theorems are not silently specialized to `q=5`.** Their role here is prior-art calibration of the positivity method. Fixed `q=5` is a distinct regime and remains part of the live target.

6. **Real scalar polarization remains insufficient even if every such scalar variance were known perfectly.** This is the exact representation obstruction of `PL-428`; the missing complex coherences can change the cone verdict while all real quadratic data remain fixed.

7. **No method impossibility is claimed.** The de la Bretèche--Fiorilli positivity architecture, an explicit-formula matrix inequality, or another arithmetic argument could conceivably be upgraded to complex-polarized coercivity. The present result redirects what such an upgrade must prove.

8. **`PL-435` remains correct.** Its claim is that MRSTT's published leading-order pair-correlation theorem does not yield the full triangular second-order residual at Selberg scale. The present finding changes the strategic target: the line need not insist on reconstructing that entire residual if a direct one-sided matrix lower bound can be proved.

## Consequence for the line

The analytic frontier is now sharper. Searching for yet another scalar short-interval variance asymptotic or scalar correct-order lower bound is not enough. The useful target is

\[
\boxed{
S_X(t)\succeq \frac14 D_X(t)
\quad\text{in the full complex mod-5 residue space,}
}
\tag{15}
\]

up to the quantitatively harmless remainder allowed by the `PL-421` margin, with the orientation/vertical shift required by `PL-431`--`PL-432` and without assuming RH/GRH.

This admits several possible proof architectures -- direct matrix explicit-formula positivity, a lower-frame inequality for the four residue vectors, or a complex-polarized variance theorem -- but they are now judged by one exact criterion. Scalar trace, diagonal, or real-polarized theorems are controls, not solutions.
