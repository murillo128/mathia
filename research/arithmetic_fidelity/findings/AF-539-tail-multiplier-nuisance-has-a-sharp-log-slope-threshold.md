# AF-539 — Tail-multiplier nuisance has a sharp log-slope threshold

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DIRICHLET-SOURCE` · `OUTWARD-TRANSPORT` · `CARRIER-SHAPE` · `NUISANCE-QUOTIENT` · `SOURCE-FORCED-TRANSVERSALITY` · `RECOVERY-BOUNDARY` · `NO-NOVELTY-CLAIM`

## Claim

Keep the exact anchored outward-tail carrier used in AF-525–AF-530,

\[
D_{X,C}(t)
=
\frac{(C^{1+t}-1)B_0(X,t)}{P(1+t)},
\qquad
B_0(X,t)=\sum_{p\le X}p^{-1-t},
\]

and compare a cutoff `A` with the power-separated cutoff

\[
B_A=\lfloor A^\theta\rfloor,
\qquad 0<\theta<1,
\]

using arbitrary integer tail multipliers `C_A,\widetilde C_A\ge2`. Put

\[
L_A=\log A,
\qquad
H_A=\log L_A,
\]

and define the exact projective carrier ratio

\[
R_A(t)
=
\frac{D_{B_A,\widetilde C_A}(t)}{D_{A,C_A}(t)}
=
\frac{\widetilde C_A^{1+t}-1}{C_A^{1+t}-1}
\frac{B_0(B_A,t)}{B_0(A,t)}.
\]

The common prime-zeta factor cancels, so `R_A` extends smoothly to `t=0`. Define

\[
g(C)=\frac{C\log C}{C-1}
\]

and the normalized multiplier drift

\[
\lambda_A
=
\frac{H_A}{L_A}
\bigl(g(\widetilde C_A)-g(C_A)\bigr).
\]

Then the exact derivative decomposition and the classical prime Mertens estimates imply

\[
\boxed{
\frac{H_A}{L_A}(\log R_A)'(0)
=
1-\theta+\lambda_A+o(1).
}
\tag{1}
\]

Consequently:

1. if `\lambda_A\to0`, the boundary log-slope still recovers the hidden anchor exponent,

\[
\frac{H_A}{L_A}(\log R_A)'(0)\longrightarrow1-\theta;
\tag{2}
\]

2. the simple sufficient condition

\[
\log C_A+\log\widetilde C_A
=o\!\left(\frac{L_A}{H_A}\right)
\tag{3}
\]

forces `\lambda_A\to0`;

3. in particular, **every pair of AF-525-admissible tail multipliers** satisfies (3). If

\[
\frac{C_AH_A}{L_A}\to0,
\qquad
\frac{\widetilde C_AH_B}{L_B}\to0,
\qquad
L_B=\log B_A,
\quad H_B=\log L_B,
\tag{4}
\]

then the multiplier nuisance is asymptotically invisible at the normalized log-slope scale;

4. this scale is sharp for the exact carrier family: to change the leading limit in (1), the multiplier contribution must itself reach logarithmic size `L_A/H_A`. For example, taking `\widetilde C_A=2` and

\[
C_A
=
\left\lfloor
\exp\!\left((1-\theta)\frac{L_A}{H_A}\right)
\right\rfloor
\]

gives `\lambda_A\to-(1-\theta)` and hence

\[
\frac{H_A}{L_A}(\log R_A)'(0)\to0.
\tag{5}
\]

Thus the arbitrary multiplier nuisance has a precise asymptotic boundary. Inside the entire AF-525 transport regime it cannot imitate the anchor direction in first projective boundary shape; erasing that direction requires multipliers whose **logarithms** live on the same `L_A/H_A` scale as the arithmetic anchor signal, far outside AF-525 admissibility.

This is a source-forced transversality statement for the exact carrier, not a rational-prime uniqueness theorem.

## Derivation

Write

\[
S(X)=\sum_{p\le X}\frac1p,
\qquad
M_1(X)=\sum_{p\le X}\frac{\log p}{p},
\qquad
\mu_X=\frac{M_1(X)}{S(X)}.
\]

Exact differentiation at `t=0` gives

\[
\partial_t\log(C^{1+t}-1)\big|_{t=0}
=
\frac{C\log C}{C-1}=g(C),
\]

and

\[
\partial_t\log B_0(X,t)\big|_{t=0}
=-\mu_X.
\]

Therefore

\[
(\log R_A)'(0)
=
g(\widetilde C_A)-g(C_A)
+\mu_A-\mu_{B_A}.
\tag{6}
\]

The second term is independent of the multiplier choice. The classical Mertens estimates

\[
S(X)=\log\log X+B_1+O\!\left(\frac1{\log X}\right),
\qquad
M_1(X)=\log X+O(1)
\tag{7}
\]

combined with

\[
\log B_A=\theta L_A+o(1),
\qquad
\log\log B_A=H_A+\log\theta+o(1)
\tag{8}
\]

give, exactly as in AF-528,

\[
\frac{H_A}{L_A}
\bigl(\mu_A-\mu_{B_A}\bigr)
\longrightarrow1-\theta.
\tag{9}
\]

Multiplying (6) by `H_A/L_A` and inserting the definition of `\lambda_A` proves (1).

### Subcritical multiplier scale

For every integer `C\ge2`,

\[
g(C)
=
\frac{\log C}{1-C^{-1}}
\le2\log C.
\tag{10}
\]

Hence

\[
|\lambda_A|
\le
2\frac{H_A}{L_A}
\bigl(\log C_A+\log\widetilde C_A\bigr).
\tag{11}
\]

Condition (3) therefore implies `\lambda_A\to0` and proves (2).

Now assume the AF-525 admissibility conditions (4). Since `B_A=A^\theta+O(1)`, one has `L_B\sim\theta L_A` and `H_B\sim H_A`. Eventually,

\[
C_A\le\frac{L_A}{H_A},
\qquad
\widetilde C_A\le\frac{L_B}{H_B}
\ll\frac{L_A}{H_A},
\]

so

\[
\log C_A+\log\widetilde C_A=O(H_A).
\tag{12}
\]

Because

\[
\frac{H_A^2}{L_A}\to0,
\]

(11) and (12) show `\lambda_A\to0`. This closes the multiplier-family boundary left open in AF-528: its recovery mechanism is not special to the co-tuned choice `C_A,\widetilde C_A\asymp e^{\sqrt{H_A}}`; it survives throughout the much larger multiplier class in which AF-525 derived the first curvature carrier.

### Critical multiplier scale and cancellation

Equation (1) also identifies the only way multiplier freedom can contaminate the leading target signal. If

\[
\lambda_A\to\lambda,
\]

then

\[
\frac{H_A}{L_A}(\log R_A)'(0)
\longrightarrow1-\theta+\lambda.
\tag{13}
\]

Thus a nonzero leading distortion requires

\[
|g(\widetilde C_A)-g(C_A)|
=\Omega\!\left(\frac{L_A}{H_A}\right).
\tag{14}
\]

Since `g(C)=\log C+O((\log C)/C)`, this can be realized by multiplier logarithms of order `L_A/H_A`. With `\widetilde C_A=2` and the exponentially large `C_A` in the claim,

\[
g(C_A)
=(1-\theta)\frac{L_A}{H_A}+o\!\left(\frac{L_A}{H_A}\right),
\]

while `g(2)=O(1)`. Therefore `\lambda_A\to-(1-\theta)`, proving (5).

This cancellation example is deliberately outside AF-525 admissibility: indeed `C_AH_A/L_A` then diverges extremely rapidly. It marks the boundary of the exact-carrier observation class rather than contradicting the source-constrained recovery result.

## Fidelity / representation audit

The natural object is the two-source-parameter map

\[
(\theta,C)\longmapsto [\log D_{A^\theta,C}(t)]
\]

viewed projectively, so constant amplitude is discarded and first boundary shape is retained. The target parameter is the hidden anchor exponent `\theta`; the transport multiplier is nuisance.

In the normalized first-shape coordinate, the arithmetic target tangent has scale `L_A/H_A`, whereas every AF-525-admissible multiplier contributes only `O(H_A)`. Their relative scale is therefore

\[
O\!\left(\frac{H_A^2}{L_A}\right)\to0.
\]

This is the deterministic source-specific analogue of the nuisance-transverse viewpoint developed abstractly in AF-533 and AF-538: the source constraints themselves force the nuisance direction to become asymptotically negligible in the retained target coordinate. The representation classification is therefore `useful-reframing`, not a claim of a new general semiparametric theorem.

The nearest falsifier is also explicit. If the transport family is enlarged so that `\log C` may reach `L_A/H_A`, multiplier and anchor directions enter the same asymptotic scale and exact cancellation becomes possible. The transversality is thus forced by the admissible source family, not by the carrier representation alone.

## Falsification and matched-control audit

The theorem survives arbitrary changes of the AF-527 amplitude co-tuning because no amplitude matching assumption is used. It is therefore stronger than a statement about one specially engineered pair of controls.

It does **not** isolate rational primes. The target term in (9) comes only from the first two classical Mertens prime moments. A generalized-prime or other matched source reproducing the same reciprocal and logarithmically weighted reciprocal asymptotics can reproduce the same `1-\theta` boundary-shape signal. Such systems remain valid controls against any primality-specific interpretation.

The critical-scale cancellation above is the relevant nuisance falsifier: once source constraints allow multiplier logarithms of order `L_A/H_A`, the first-shape observable ceases to be intrinsically anchor-faithful. Any later theorem claiming robustness under a broader transport family must therefore control this drift or add an independent observable that separates it.

## Boundaries

1. **Exact carrier, not curvature derivative.** The result concerns the exact carrier ratio `R_A`. AF-525 gives value-level asymptotics between this carrier and the normalized curvature defect, but those estimates do not provide the derivative-level error control needed to transfer the theorem automatically to the curvature-defect log-slope.

2. **Fixed power separation.** The statement is written for fixed `\theta\in(0,1)`. Uniformity for `\theta` in a compact subset of `(0,1)` should follow from uniform versions of the same Mertens estimates, but is not claimed here.

3. **Coarse anchor parameter only.** The recovered target is `\theta`, not the exact cutoff `B_A`, the rational-prime set, or a zero-sensitive invariant.

4. **Threshold for this observable.** The `L_A/H_A` log-multiplier threshold is sharp for contamination of this first projective log-slope. It is not asserted to be the threshold for every higher jet, full-profile, noisy, or alternative compression.

5. **No practical stability conclusion beyond existing conditioning results.** AF-529–AF-532 already show that exact shape separation can coexist with severe finite-resolution/noise conditioning. The present theorem identifies nuisance transversality at the asymptotic target scale; it does not improve those sampling thresholds.

## Prior-art / source audit

The number-theoretic input is classical. Terence Tao's expository note *Mertens' theorems* (11 December 2013), https://terrytao.wordpress.com/2013/12/11/mertens-theorems/ , records both

\[
\sum_{p\le x}\frac{\log p}{p}=\log x+O(1)
\]

and

\[
\sum_{p\le x}\frac1p=\log\log x+O(1),
\]

and discusses the standard sharper variants obtainable from prime-number-theorem input. AF-527/AF-528 already audited and used the refined reciprocal-prime form needed here.

The interpretation in terms of a target direction transverse to nuisance is standard statistical geometry: efficient scores are obtained by removing nuisance-tangent components, and AF-533/AF-538 already specialize that language to Arithmetic Fidelity. No novelty is claimed for nuisance projection, for the Mertens estimates, or for the elementary bound `g(C)\le2\log C`.

The durable contribution recorded here is the source-specific threshold classification supplied by the exact carrier identity (6): AF-525 admissibility forces the multiplier nuisance below the arithmetic log-slope scale, while multiplier logarithms of order `L_A/H_A` can already cancel that signal. This is retained as a Mathia fidelity result, not as a new theorem of prime-number theory or semiparametric statistics.

## Consequence

AF-528's first-shape recovery is structurally more robust than its original co-tuned example suggested. Within the complete outward-tail multiplier regime for which AF-525 derived the first anchor carrier, multiplier freedom can destroy scalar amplitude information but cannot erase the normalized first projective boundary shape. The first nuisance scale capable of doing so is parametrically larger and explicitly identifiable.

For the broader Arithmetic Fidelity program, this is a concrete instance of a source-forced fidelity subspace: admissible nuisance motion exists, but its image in the retained coordinate is asymptotically lower order than the target motion. Future arithmetic applications should seek this stronger property—**source constraints that force target/nuisance separation after compression**—rather than merely selecting observables that separate one hand-picked pair of controls.