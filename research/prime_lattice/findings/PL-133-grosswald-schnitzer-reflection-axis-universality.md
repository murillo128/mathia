# PL-133 — Grosswald–Schnitzer phase rigidity persists on every positive reflection axis

## Claim

`PL-127`, `PL-131`, and `PL-132` identified an unexpectedly rigid critical-line observable inside the Grosswald–Schnitzer zero-preserving deformation class. For

`Z_q(s)=phi_q(s) zeta(s)`,  with  `p_n <= q_n <= p_(n+1)`, 

Grosswald and Schnitzer prove that

`phi_q(s)=prod_n (1-p_n^(-s))/(1-q_n^(-s))`

is analytic and nonvanishing throughout `Re(s)>0`. The previous findings used the Riemann reflection `s -> 1-s` and the cocycle

`R_q(s)=phi_q(s)/phi_q(1-s)`.

The apparent special role of the critical line in that mechanism is not intrinsic. Fix **any** real `c>0` and define, in the strip `0<Re(s)<c`,

`R_(q,c)(s)=phi_q(s)/phi_q(c-s)`.

Then the entire rigidity chain survives with the self-dual axis moved from `Re(s)=1/2` to `Re(s)=c/2`:

1. `|R_(q,c)(c/2+i t)|=1` for every real `t`;
2. the central phase slope is a positive additive prime-deformation functional;
3. for integer Grosswald–Schnitzer controls, a sufficiently small slope certifies exact agreement with the rational primes below any prescribed finite cutoff;
4. equality of the phase on any subset of `Re(s)=c/2` with a finite accumulation point forces equality of the entire Grosswald–Schnitzer generator sequence, even for real controls;
5. for integer controls and any fixed finite prefix, finitely many exact phase samples on any nondegenerate compact interval of the axis separate all distinct prefixes uniformly over arbitrary admissible tails.

Thus the phase-rigidity geometry of `PL-127`/`PL-131`/`PL-132` does **not** select `1/2`. It selects the fixed line of whichever affine reflection `s -> c-s` is supplied. The value `1/2` enters those results only because the actual Riemann functional equation externally supplies the particular reflection `s -> 1-s`.

**Evidence/status:** `EXACT-DERIVED + DECISIVE-NEGATIVE/AXIS-CONTROL + PRIOR-ART-DELIMITED`.

This does not weaken the genuine arithmetic significance of the Riemann functional equation. For `c != 1`, `R_(q,c)` is a synthetic reflection quotient, not a functional-equation defect for `zeta`. The negative result is narrower and useful: no argument based only on the Grosswald–Schnitzer quotient, unit-modulus self-dual phase, positive phase slope, or the associated inverse-rigidity statements can claim to explain why the Riemann critical line is `Re(s)=1/2`. A separate global structure must first force `c=1`.

## 1. Every positive reflection axis carries unit-modulus phase

Let `c>0`. Both arguments `s` and `c-s` lie in the Grosswald–Schnitzer continuation half-plane precisely when

`0<Re(s)<c`,

so `R_(q,c)` is analytic and nonzero there. No Euler product is being continued term by term into this strip: the quotient `phi_q` is the analytic nonvanishing function supplied by the Grosswald–Schnitzer theorem.

Because all generators are real,

`phi_q(conj(s))=conj(phi_q(s))`.

On the fixed line `s=c/2+i t`,

`c-s=c/2-i t=conj(s)`,

and therefore

`R_(q,c)(c/2+i t)=phi_q(c/2+i t)/conj(phi_q(c/2+i t))`.

Hence

`|R_(q,c)(c/2+i t)|=1`

for every real `t`. The unit-circle phase phenomenon used at `1/2` in `PL-127` is therefore a generic Schwarz-reflection fact for **every** positive affine reflection axis.

## 2. Positive central slope persists for every `c>0`

Define

`D_c(q)=(1/2) (d/ds log R_(q,c)(s))|_(s=c/2)`.

Since

`d/ds log R_(q,c)(s)
 = phi_q'(s)/phi_q(s) + phi_q'(c-s)/phi_q(c-s)`,

we obtain at the fixed point

`D_c(q)=phi_q'(c/2)/phi_q(c/2)`.

Grosswald–Schnitzer's locally uniform logarithmic product allows termwise differentiation in `Re(s)>0`. For a real `x>1`,

`d/ds log(1-x^(-s))=log(x)/(x^s-1)`,

so

`D_c(q)=sum_n [g_c(p_n)-g_c(q_n)]`,

where

`g_c(x)=log(x)/(x^(c/2)-1)`.

For every fixed `c>0`, `g_c` is strictly decreasing. Put `y=x^(c/2)>1`; then

`g_c(x)=(2/c) log(y)/(y-1)`.

The derivative of `log(y)/(y-1)` has numerator

`1-1/y-log(y)`,

which is zero at `y=1` and strictly decreasing thereafter because its derivative is `(1-y)/y^2<0`. Hence `g_c'(x)<0` for every `x>1`.

The one-sided Grosswald–Schnitzer ordering `p_n<=q_n` therefore gives

`D_c(q)>=0`,

with equality if and only if `q_n=p_n` for every `n`. If the controls are integers, define for a fixed cutoff `X`

`delta_c(X)=min_{p prime, p<=X} [g_c(p)-g_c(p+1)] > 0`.

Any altered generator with `p_n<=X` satisfies `q_n>=p_n+1` and contributes at least `delta_c(X)`. Consequently

`D_c(q)<delta_c(X)`

forces exact agreement `q_n=p_n` for every prime `p_n<=X`.

Thus both the positivity and the finite-scale integer certificate of `PL-127` occur on every positive reflection axis. They cannot by themselves distinguish `c=1` from any other positive value.

## 3. Phase-arc injectivity also moves to every positive axis

Let `q` and `r` be two admissible **real** Grosswald–Schnitzer sequences, and put

`psi(s)=phi_q(s)/phi_r(s)`.

Suppose

`R_(q,c)(c/2+i t)=R_(r,c)(c/2+i t)`

for heights `t` in any set with a finite accumulation point. On the strip `0<Re(s)<c`, this says that the analytic function

`psi(s)-psi(c-s)`

vanishes on a set accumulating inside the strip. The identity theorem gives

`psi(s)=psi(c-s)`

throughout `0<Re(s)<c`.

Exactly as in `PL-131`, this symmetry glues the original zero-free `psi` on `Re(s)>0` to the function `psi(c-s)` on `Re(s)<c`. The two definitions agree on their overlap, and their domains cover the whole plane. Thus `psi` extends to a zero-free entire function satisfying

`psi(s)=psi(c-s)`.

The growth estimate needed for Hadamard rigidity works for every `c>0`. For

`H_s(x)=log(1-x^(-s))`

and `Re(s)>=c/2`,

`|partial_x H_s(x)|
 <= C_c |s| x^(-1-c/2)`,

where `C_c=(1-2^(-c/2))^(-1)`. If `d_n=p_(n+1)-p_n`, the interval condition gives

`|H_s(p_n)-H_s(q_n)|
 <= C_c |s| d_n p_n^(-1-c/2)`.

The majorant is summable. Bertrand's postulate gives `p_(n+1)<2p_n`; on each interval `[p_n,p_(n+1)]`, comparison with `x^(-1-c/2)` yields

`d_n p_n^(-1-c/2)
 <= 2^(1+c/2) integral_(p_n)^(p_(n+1)) x^(-1-c/2) dx`,

and the adjacent integrals telescope to a finite tail because `c>0`. Therefore

`|log psi(s)|<=C |s|`,  for `Re(s)>=c/2`.

The reflection identity transfers the same exponential-type bound to the other half-plane. Hence `psi` is a zero-free entire function of order at most one, so classical Hadamard factorization gives

`psi(s)=exp(a s+b)`.

The symmetry `psi(s)=psi(c-s)` forces `a=0`. Finally, the Grosswald–Schnitzer Euler normalization on the positive real axis gives `psi(sigma)->1` as `sigma->+infinity`, so `psi` is identically one. Thus `phi_q=phi_r`.

The first-differing-frequency argument from `PL-131`, used only back in the absolutely convergent half-plane, then forces

`q_n=r_n` for every `n`.

Therefore **any accumulating exact reflection-phase data on any axis `Re(s)=c/2`, `c>0`, determine the complete admissible Grosswald–Schnitzer sequence**. The special value `c=1` is not used anywhere in this rigidity proof.

## 4. Finite integer fingerprints are likewise axis-universal

Restrict now to integer controls

`q_n in A_n := Z intersect [p_n,p_(n+1)]`.

As in `PL-132`, the control space

`Q_Z=prod_(n>=1) A_n`

is compact in the product topology, and for any fixed finite prime cutoff `X` it has only finitely many clopen prefix classes.

Fix a nondegenerate compact height interval `I`. Define

`Phi_(c,I)(q)(t)=R_(q,c)(c/2+i t)`.

The same derivative estimate from the preceding section, now uniform for `t in I`, gives a summable tail majorant of order

`d_n p_n^(-1-c/2)`.

Hence `Phi_(c,I):Q_Z -> C(I)` is continuous in the uniform norm without freezing or truncating the arbitrary tail. Section 3 makes it injective.

Distinct compact prefix cylinders therefore have disjoint compact images in `C(I)` and hence positive mutual distance. Since there are only finitely many prefix classes, their minimum separation is positive. Compactness of the full image gives uniform equicontinuity, so a sufficiently fine finite grid of heights preserves a positive fraction of that separation.

Consequently, for every `c>0`, finite cutoff `X`, and nondegenerate compact `I`, there exist heights

`t_1,...,t_m in I`

and `eta=eta(c,X,I)>0` such that

`P_X(q)!=P_X(r)`

implies

`max_k |R_(q,c)(c/2+i t_k)-R_(r,c)(c/2+i t_k)| >= eta`

uniformly over all admissible integer tails. As in `PL-132`, this is an existence/stability theorem, not an effective sample-complexity bound.

Thus the finite-fingerprint consequence of integer prime-lattice discreteness is also independent of the Riemann value `c=1`.

## 5. Adversarial interpretation: the phase mechanism is axis-blind

The result gives a direct matched control for claims that `PL-127`--`PL-132` explain the critical line. Replace the Riemann reflection by any

`s -> c-s`,  `c>0`.

Without changing the Grosswald–Schnitzer deformation class or its exponent-lattice arithmetic, one obtains the same qualitative package on `Re(s)=c/2`: unitary phase, positive noncancelling slope, integer low-prime certification, complete arc injectivity, and finite tail-uniform integer fingerprints.

Therefore the implication

`self-dual phase rigidity => the distinguished axis is Re(s)=1/2`

is false for this mechanism. The phase geometry only detects the fixed set of a reflection already supplied to it.

This does **not** say that the true zeta reflection may be shifted arbitrarily. The actual completed zeta function has a specific functional equation, and `PL-014` already records that adelic/Fourier self-duality naturally produces the axis `Re(s)=1/2`. The present finding instead separates two logical jobs that must not be conflated:

- deriving the **specific global reflection** `s -> 1-s`, including its archimedean/gamma normalization and arithmetic origin;
- exploiting the resulting fixed axis once that reflection is already known.

The Grosswald–Schnitzer reflection-phase machinery performs the second job but not the first. Any RH-relevant extension must obtain `c=1` from an independent global structure and then add a positivity/unitarity/Hodge mechanism capable of localizing the zero divisor there. Merely observing phase rigidity on the fixed line is insufficient.

## Prior-art and novelty audit

No new external theorem is needed. Grosswald–Schnitzer's 1978 theorem supplies the analytic nonvanishing quotient on `Re(s)>0`; classical Hadamard factorization supplies the zero-free order-one rigidity already audited in `PL-128`; Bertrand's postulate and compactness/equicontinuity are elementary ingredients already used in `PL-131` and `PL-132`.

A targeted search around Grosswald–Schnitzer modified zeta functions, functional-equation/reflection phases, shifted reflection axes, inverse recovery, and phase rigidity located the original deformation literature and generic functional-equation/entire-function tools but no source stating this `c>0` axis-parametric version of the `PL-127`--`PL-132` chain. No broad novelty claim is made from that absence. The durable result is the adversarial control: the exact proofs already present in this line have a free positive reflection parameter, so they cannot be used as intrinsic evidence that the exponent lattice singles out the Riemann critical line.

No `SOURCES.md` update is required because all external ingredients were already audited and recorded by `PL-125`--`PL-132`.

## Consequence for the prime-lattice line

The Grosswald–Schnitzer control has now separated arithmetic identifiability from critical-axis selection. Integer discreteness genuinely improves finite observability of the prime generator sequence, but the phase observables that achieve that recovery are compatible with **every** positive self-dual axis.

Future work should therefore reject any candidate whose only reason for privileging `1/2` is that a quotient becomes unit-modulus, positive-slope, or phase-rigid on the fixed line of an assumed reflection. A useful RH mechanism must explain why the global arithmetic completion supplies exactly `s -> 1-s` and must then impose an additional zero-localizing constraint that does not survive arbitrary reflection-axis replacement or matched generalized-prime controls.