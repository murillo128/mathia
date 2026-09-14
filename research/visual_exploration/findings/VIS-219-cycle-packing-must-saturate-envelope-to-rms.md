# VIS-219 — RMS certification requires cycle-packing saturation, not positive density

## Claim

Keep the finite Hermitian zero-diagonal setup of `VIS-215`. Write

`G(z)=2 sum_e w_e cos(delta_e)`,

`B(A)=2 sum_e w_e`,

and let `P_+`, `P_-` be the optimal positive- and negative-envelope fractional cycle-packing certificates from `VIS-215`. Put

`P(A)=min(P_+,P_-)`.

Then the packing certificate is

`max_z |G(z)| <= U_pack(A):=B(A)-P(A)`.

Also put

`R(A)=2 sum_e w_e^2`

and

`N_eff(A)=(sum_e w_e)^2/(sum_e w_e^2)`.

Since

`B(A)/sqrt(R(A))=sqrt(2 N_eff(A))`,

the normalized packing certificate satisfies the exact identity

`U_pack(A)/sqrt(R(A))`
` = sqrt(2 N_eff(A)) [1-P(A)/B(A)]`.

Therefore this cycle-packing route can certify a Haar-RMS-scale worst-start bound

`max_z |G(z)|=O(sqrt(R(A)))`

only when its *certificate deficit* obeys

`B(A)-P(A)=O(sqrt(R(A)))`,

or equivalently

`1-P(A)/B(A)=O(N_eff(A)^(-1/2))`.

A merely positive packing density or any fixed-fraction bound

`P(A)>=c B(A)`, with fixed `c<1`,

is not enough when `N_eff(A)->infinity`: the resulting upper certificate remains larger than the RMS scale by a factor of order `sqrt(N_eff)`.

For the strictly subcritical prime-phase matrices `A_(y,H)` of `VIS-218`,

`N_eff asymp_(alpha,v) y^2/[H (log y)^2]`.

Hence an RMS-scale certificate from `VIS-215` would require

`1-P(A_(y,H))/B(A_(y,H))`
` = O_(alpha,v)(sqrt(H) log y / y)`,

which tends to zero under `H log y/y ->0`. The cycle packing must therefore asymptotically **saturate the absolute envelope** to increasing relative precision; extensive cycle count or a nonzero macroscopic fraction of weighted frustration is not by itself the relevant threshold.

Finally, the raw normalization `P(A)/|E|` proposed in the current magnetic-frustration clue is not intrinsic to this objective. Under uniform coefficient rescaling `w_e -> c w_e`, `P`, `B`, and `sqrt(R)` all scale by `c`, while `|E|` is unchanged. Thus `P/|E|` changes by `c` whereas both `P/B` and `(B-P)/sqrt(R)` are invariant. The scale-free quantity relevant to the desired RMS bound is the residual envelope `(B-P)/sqrt(R)`, not packing reward per combinatorial edge.

**Evidence/status:** `EXACT-DERIVED + NORMALIZATION CORRECTION + NEGATIVE CERTIFICATE THRESHOLD + NO-NOVELTY-CLAIM`.

This finding does **not** prove that the exact torus optimum is larger than the Haar RMS scale, and failure of the packing certificate to saturate does not refute stronger fixed-modulus mechanisms. It identifies the exact strength that the `VIS-215` certificate itself must reach.

## 1. The packed cycle bound has an exact normalized form

`VIS-215` proves, for every torus point,

`-B(A)+P_- <= G(z) <= B(A)-P_+`,

and therefore

`max_z |G(z)| <= B(A)-min(P_+,P_-)`.

Set `P=min(P_+,P_-)`. With

`W_1=sum_e w_e`, `W_2=sum_e w_e^2`,

one has

`B=2W_1`, `R=2W_2`, `N_eff=W_1^2/W_2`.

Consequently

`B/sqrt(R)`
` = 2W_1/sqrt(2W_2)`
` = sqrt(2N_eff)`.

Multiplying by the relative residual `1-P/B` gives

`(B-P)/sqrt(R)`
` = sqrt(2N_eff)(1-P/B)`.

Nothing asymptotic or probabilistic enters this identity.

The packing rewards are automatically on the same weighted scale as `B`. Indeed `P_+<=E_+(z)` and `P_-<=E_-(z)` for every `z`; Haar averaging gives `E E_+=E E_-=B` because `E G=0`, hence `0<=P_+,P_-<=B`.

## 2. Positive fraction is not the RMS threshold

Suppose for illustration that one proves a uniform lower bound

`P>=cB`

with some fixed `0<c<1`. Then the `VIS-215` certificate gives

`U_pack<= (1-c)B`.

But measured in Haar-RMS units its *certificate value* is

`U_pack/sqrt(R)`
` = sqrt(2N_eff)(1-P/B)`.

A lower bound `P>=cB` alone permits the right-hand side to be as large as `(1-c)sqrt(2N_eff)`. Thus when `N_eff` diverges, a fixed positive fraction does not place the certificate on the RMS scale. To force

`U_pack/sqrt(R)<=C`

for a fixed constant `C`, one needs exactly

`1-P/B <= C/sqrt(2N_eff)`.

This is a statement about the **strength required of the certificate**, not a lower bound on the true torus optimum. A weak certificate may coexist with a much smaller exact optimum.

## 3. The subcritical prime graph requires near-total saturation

`VIS-218` proves in the strictly subcritical regime

`W_1 asymp y/(H log y)`,

`W_2 asymp 1/H`,

and therefore

`N_eff asymp y^2/[H(log y)^2]`.

Substitution into the exact threshold gives

`N_eff^(-1/2) asymp sqrt(H) log y/y`.

Because `H log y/y ->0`, this quantity tends to zero. Hence a useful cycle-packing certificate cannot merely occupy a positive density of cycles or recover a fixed percentage of the absolute envelope. It must leave only an `O(sqrt(R))` residual, equivalently an asymptotically vanishing relative fraction of `B`.

The conclusion sharpens the research consequence of `VIS-218`. That finding left the fractional cycle-packing route open because it is stronger than the normalized spectral relaxation. The present result does not close it, but it identifies its actual quantitative target: **near-saturation, not extensivity**.

## 4. Why raw edge density is the wrong normalization

The current proposed clue asks whether a cycle-packing optimum can be `Omega(|E|)` and tracks `P_G/|E|`. The packing objective, however, is a weighted energy:

`P_± = max_lambda sum_C lambda_C |1-H_±(C)|^2/R(C)`.

Uniformly rescale all edge weights by `c>0`. Then every harmonic cycle reward scales by `c`, so

`P_± -> cP_±`, `B->cB`, `sqrt(R)->c sqrt(R)`.

The support graph and therefore `|E|` do not change. Thus `P/|E|` is not invariant under a harmless change of coefficient units. In contrast,

`P/B`

and

`(B-P)/sqrt(R)`

are invariant and are directly tied to the desired envelope bound.

This is enough to reject the proposed raw edge-density criterion even before solving a finite packing LP.

## 5. Prior-art and novelty boundary

The general `U(1)` synchronization, magnetic-frustration, holonomy, and connection-Laplacian setting is already source-audited in `VIS-215`, including the Bandeira--Singer--Spielman and Lange--Liu--Peyerimhoff--Post references and the 2026 cycle-holonomy literature noted there. `VIS-215` explicitly makes no novelty claim for the general fractional cycle-packing inequality.

`VIS-218` already source-audits the prime/Fourier localization and effective-count asymptotics used here. The present finding adds no external graph theorem or arithmetic theorem: it is the exact normalization consequence obtained by composing the `VIS-215` packing certificate with the `VIS-218` RMS/effective-edge scale. Novelty is therefore not claimed.

## Boundaries and falsification

The statement concerns what the specific `VIS-215` packing lower bound must accomplish in order to certify an RMS-scale worst-start upper bound. It does not say that `P` cannot saturate `B`, does not say that the exact torus optimum is large when `P` fails to saturate, and does not address finite-time access of the one-parameter prime-log orbit.

The subcritical asymptotic specialization inherits the fixed `alpha`, taper, and `H->infinity`, `H log y/y->0` hypotheses of `VIS-218`.

Falsify this finding by locating an error in the exact identity `B/sqrt(R)=sqrt(2N_eff)`, the `VIS-215` bound `max|G|<=B-P`, the rescaling behavior of `P`, or the substitution of the `VIS-218` effective-count asymptotic.

## Research consequence

The proposed `macroscopic-magnetic-frustration-density` clue is mis-normalized as written. The next legitimate question is sharper: can the canonical prime-phase graph force **both** signed cycle-packing certificates to saturate `B` so that

`[B-min(P_+,P_-)]/sqrt(R)`

stays bounded, or can one prove that this normalized deficit diverges and thereby close this particular packing certificate route?

That is a new coherent research question. It should be tested directly in the weighted normalization before any attempt to interpret raw cycle density or combinatorial edge count.