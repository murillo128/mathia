# PL-158 — Fixed-step Suzuki sampling has exact off-line aliasing controls

## Claim

The fixed geometric sampling left open by `PL-157` has a sharp matched-control obstruction. For every sampling step

`h>0`,

there is an entire function with the same two basic completion symmetries as `xi`, with all four of its zeros strictly inside `0<Re(s)<1` but off `Re(s)=1/2`, whose finite Suzuki zero-screw is nevertheless **bounded above on every sample `t=n h`**.

More explicitly, choose

`0<theta<1/2`

and an integer `m>=1` large enough that

`tau=2 pi m/h > theta`.

Put `u=s-1/2` and define

`X_(theta,tau)(s)=((u-theta)^2+tau^2)((u+theta)^2+tau^2)`.

Then

`X(s)=X(1-s)=conjugate(X(conjugate(s)))`,

and its zeros are

`1/2 +/- theta +/- i tau`.

Thus the analogue of RH is false for this completed polynomial. If `Gamma={+/-tau +/- i theta}` is the corresponding zero set of `X(1/2-i z)`, define the exact finite zero-screw

`Psi_X(t)=sum_(gamma in Gamma) (1-exp(i gamma t))/gamma^2`.

For real `t`, quartet symmetry gives

`Psi_X(t)=4 Re[(1-cos((tau+i theta)t))/(tau+i theta)^2]`.

At the fixed samples `t=n h`, the choice `tau h=2 pi m` freezes the oscillatory phase and yields

`Psi_X(n h)`
` = 4 (tau^2-theta^2)/(tau^2+theta^2)^2 * (1-cosh(theta n h))`
` <= 0`

for every `n>=0`, with `Psi_X(n h)->-infinity`. Hence

`sup_(n>=0) Psi_X(n h)=0`

despite the off-critical zero quartet.

The control is not merely a formal zero list. For `Im(z)>theta`, direct integration gives the exact Suzuki-type transform

`integral_0^infinity Psi_X(t) exp(i z t) dt`
` = -(1/z^2) X'/X(1/2-i z)`.

The polynomial has no real zeros, so the shifted logarithmic derivative has no real-axis poles, exactly the analytic feature used by the continuous one-sign Landau argument in `PL-153`. The continuous `Psi_X` is in fact unbounded in both signs. The failure occurs only after fixed-step sampling: an off-line oscillatory exponential is aliased into a one-sign real exponential mode.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + MATCHED-CONTROL + DECISIVE-NEGATIVE/STRUCTURAL-BOUNDARY`. Suzuki's zero series and one-sided Fourier-Laplace transform are peer-reviewed inputs. The quartet construction and sampled formula are exact elementary deductions. Equispaced aliasing of exponential modes is classical sampling theory, so no novelty claim is made. A targeted search around Suzuki's screw function, arithmetic-progression/fixed-step sampling, and the recent prime-power checkpoint literature did not locate this exact control; absence from that search is not treated as novelty evidence.

## Suzuki's zero expansion exposes the sampling map

Suzuki proves unconditionally that his completed zeta function `Psi` satisfies, for every real `t>=0`,

`Psi(t)=sum_gamma (1-exp(i gamma t))/gamma^2`,

where `gamma` ranges over the zeros of `xi(1/2-i z)`, with multiplicity. If

`rho=beta+i T`

is a zero of `xi`, then the associated zero parameter is

`gamma=i(rho-1/2)=-T+i(beta-1/2)`.

Thus horizontal displacement of a zeta zero from the critical line becomes the imaginary part of the screw frequency. Under sampling at `t=n h`, each zero mode becomes

`exp(i gamma n h)=(exp(i gamma h))^n`.

Writing `gamma=a+i b`, the discrete multiplier has

`|exp(i gamma h)|=exp(-b h)`.

So the horizontal zero displacement is retained as a radial expansion/contraction factor, while the ordinate is observed only through the phase

`a h mod 2 pi`.

That quotient is the fixed-step aliasing channel. Continuous time distinguishes all real frequencies `a`; the sequence `{n h}` identifies frequencies differing by integer multiples of `2 pi/h`.

For the actual exponent lattice, a fixed one-prime ray `k e_p` has exactly this form with

`h=log p`,  `t_k=k log p`.

Therefore any argument that tries to transfer the continuous one-sided criterion of `PL-153` to a single prime ray must confront this phase quotient. The issue is not the radial encoding of `beta-1/2`; that survives sampling. The issue is that the oscillation which forces both signs in continuous time can disappear on the sampled ray.

## Exact symmetric quartet control

Let

`X(s)=((s-1/2-theta)^2+tau^2)((s-1/2+theta)^2+tau^2)`.

Because replacing `s` by `1-s` sends `u=s-1/2` to `-u` and swaps the two factors,

`X(1-s)=X(s)`.

The coefficients are real, so Schwarz symmetry also holds. The zero set consists of

`rho_(eps,delta)=1/2+eps theta+i delta tau`,

with `eps,delta in {+1,-1}`. Choosing `theta<1/2` puts all four zeros in the open critical strip, while `theta>0` places all four off the critical line.

The zeros of `z -> X(1/2-i z)` are the quartet

`Gamma={tau+i theta, tau-i theta, -tau+i theta, -tau-i theta}`

up to the irrelevant ordering/sign convention inherited from `rho -> i(rho-1/2)`. Because the set is closed under sign and conjugation,

`Psi_X(t)=sum_(gamma in Gamma)(1-exp(i gamma t))/gamma^2`

is real and even. Pairing `gamma` with `-gamma` and then conjugates gives

`Psi_X(t)=4 Re[(1-cos((tau+i theta)t))/(tau+i theta)^2]`.

Expanding the real part makes the continuous oscillation explicit:

`Psi_X(t)`
` = 4/(tau^2+theta^2)^2 * [`
`     2 tau theta sin(tau t) sinh(theta t)`
`     -(tau^2-theta^2)(cos(tau t) cosh(theta t)-1)`
`   ].`

The coefficient of the leading `exp(theta t)` term is a nonzero sinusoid. Hence `Psi_X(t)` has arbitrarily large positive and negative excursions on the continuum. This is exactly what the continuous Landau obstruction predicts for a completed object with nonreal shifted logarithmic-derivative poles and no real ones.

Now impose

`tau h=2 pi m`.

At `t=n h`,

`sin(tau n h)=0`,  `cos(tau n h)=1`,

so

`Psi_X(n h)`
` = 4 (tau^2-theta^2)/(tau^2+theta^2)^2 (1-cosh(theta n h)).`

When `tau>theta`, this is nonpositive for every sample and tends exponentially to negative infinity. For every prescribed `h>0` one can first fix, say, `theta=1/4`, and then take `m` large enough that `2 pi m/h>1/4`. Thus the obstruction applies to **every** fixed step, including every one-prime lattice axis `h=log p`.

## The same transform survives, but the Landau boundary moves onto the real sampled axis

The control also preserves the relevant transform structure. Since the zero set is finite and symmetric, for `Im(z)>theta` termwise integration is legitimate:

`integral_0^infinity (1-exp(i gamma t)) exp(i z t) dt`
` = i/z-i/(z+gamma)`.

Summing over the sign-symmetric quartet and using `sum_gamma 1/gamma=0` gives

`integral_0^infinity Psi_X(t) exp(i z t) dt`
` = -(1/z^2) X'/X(1/2-i z)`.

Thus the fixed-step failure is not caused by dropping the completed logarithmic-derivative relation. It is caused by replacing a continuous transform with a sampled sequence.

The ordinary generating function makes this loss especially transparent. Set

`A=4 (tau^2-theta^2)/(tau^2+theta^2)^2 >0`,

`r=exp(theta h)>1`.

Then

`Psi_X(n h)=A[1-(r^n+r^(-n))/2]`,

so, in its disk of convergence,

`sum_(n>=0) Psi_X(n h) z^n`
` = A[1/(1-z)-1/(2(1-r z))-1/(2(1-r^(-1) z))].`

Its nearest singularity is the **positive real pole**

`z=r^(-1)=exp(-theta h)`.

This explains why a discrete Pringsheim/Landau argument cannot reproduce `PL-153`: after resonance, the off-line quartet has been folded onto the positive real boundary singularity that a one-signed sequence is allowed, indeed required, to possess. In continuous time the same quartet produces nonreal poles and therefore cannot remain one-signed.

## Prior art and novelty audit

The theorem-level source is:

- **Masatoshi Suzuki**, “Aspects of the screw function corresponding to the Riemann zeta-function,” *Journal of the London Mathematical Society* **108**(4) (2023), 1448–1487, DOI `10.1112/jlms.12785`. Theorem 1.1 gives both the exact zero representation `Psi(t)=sum_gamma (1-exp(i gamma t))/gamma^2` for all real `t>=0` and the one-sided transform `-z^(-2) xi'/xi(1/2-i z)` in its initial half-plane. These are the only zeta-specific inputs needed for the control.

The aliasing identity itself is classical: equispaced sampling maps an exponential frequency `gamma` to the discrete multiplier `exp(i gamma h)`, so real frequencies differing by `2 pi/h` are indistinguishable. Modern Prony/exponential-sum sampling literature treats precisely this equispaced exponential representation. That general fact is prior art, not a discovery of the prime-lattice program.

A targeted current search combined Suzuki's screw function with `sampling`, `arithmetic progression`, `fixed step`, and the August 2026 prime-power-checkpoint literature. The checkpoint work found in the audit emphasizes exact prime-power event intervals and explicitly distinguishes complete interval certification from a numerical sampling grid. No source located in the bounded search stated the exact symmetric off-line quartet control above. This absence does not support a novelty claim: once Suzuki's zero series is viewed as a sampled exponential sum, the construction is elementary aliasing.

The finding therefore records a **structural negative** rather than a proposed new theorem about zeta.

## Adversarial boundaries

1. **This is not a counterexample to a zeta-specific fixed-axis criterion.** `X` is a finite completed polynomial, not the Riemann `xi`, not an Euler product, and not a Dirichlet series generated by the rational primes. The result proves that functional-equation symmetry, Schwarz symmetry, off-line zero geometry, the zero-screw representation, and the completed logarithmic-derivative transform are insufficient by themselves to make fixed-step one-sided sampling an RH discriminator.

2. **The result specifically kills the generic upper-one-sided transfer.** The constructed samples are bounded above and unbounded below. It does not prove that lower boundedness or two-sided boundedness on the actual one-prime zeta samples fails to imply RH. Those would require additional arguments.

3. **Exact resonance is deliberately adversarial.** For a fixed zeta zero ordinate there is no reason to expect `T log p/(2 pi)` to be an integer. The point is methodological: a proof based only on the ambient completed zero-series structure cannot exclude such a resonance. Any successful one-prime theorem must use a zeta-specific anti-aliasing statement, a second incommensurable scale, or another arithmetic constraint.

4. **This does not affect `PL-156` or `PL-157`.** Ordinary-prime and sub-`3/4` meshes have logarithmic gaps tending to zero and recover the continuum by deterministic interpolation. A fixed ray `p^n` has constant logarithmic spacing `log p`, equivalently multiplicative gaps of order the scale itself (`kappa=1`), so it lies exactly outside that no-aliasing interpolation regime.

5. **It also does not affect `PL-155`.** A two-prime face uses the dense difference group `Z log p+Z log q`; kernel positivity there extends by continuity to the whole real line. A single ray has difference group `Z log p`, which is discrete and admits the aliasing control above.

6. **No Euler product is being continued.** Every identity for the matched control is a finite exact calculation. For zeta, the only imported identities are Suzuki's already-completed zero series and transform in their stated domains.

A falsification would require an algebraic error in the quartet pairing, failure of `X(1-s)=X(s)`/Schwarz symmetry, failure of the resonance identity `cos((tau+i theta)n h)=cosh(theta n h)` when `tau h in 2 pi Z`, or failure of the elementary finite-term transform calculation.

## Consequence for the research line

`PL-157` left a fixed one-prime axis as a logically separate sampling problem. This finding explains why it is separate. The continuum one-sided Landau mechanism does **not** survive fixed logarithmic sampling in any purely formal way: the zero ordinate is quotiented modulo `2 pi/h`, and an off-critical expanding mode can become a one-sign sampled mode.

Accordingly, do not pursue

`{Psi(n log p) bounded above} -> RH`

by simply discretizing the `PL-153` transform/Landau proof or by treating the radial factor `exp((beta-1/2) log p)` as sufficient information. A viable fixed-axis argument must add a genuinely arithmetic anti-aliasing mechanism. Natural surviving discriminators are interactions between two multiplicatively independent prime scales, mixed-face positivity as in `PL-155`, or a theorem tying actual zeta zero ordinates to the rational-prime frequency module strongly enough to prevent resonant one-sign folding. Merely observing that off-line zeros have radial multiplier different from one is not enough.