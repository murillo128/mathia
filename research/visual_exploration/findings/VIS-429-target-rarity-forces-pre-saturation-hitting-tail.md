# VIS-429 — rare superlevel targets force long Haar pre-saturation hitting tails

## Claim

Let `(X,m)` be a probability space with a measure-preserving real flow `tau(u)`, and let

`A:X->[0,1]`

be an observable whose restriction to every flow orbit is uniformly `B`-Lipschitz:

`|A(x tau(u))-A(x tau(v))| <= B |u-v|`.

For `t in [0,1]`, define the closed superlevel target

`E_t={x:A(x)>=t}`,

its Haar/probability mass

`mu(t)=m(E_t)`,

and the two-sided hitting time

`H_t(x)=inf{|u|:x tau(u) in E_t}`,

with `H_t=+infinity` if the target is never hit.

Fix `t in [0,1)`, `eta in (0,1-t]`, and assume `B>0`. Then for every `rho>=0`,

`m{H_(t+eta)<=rho} <= min(1,(1+rho B/eta) mu(t))`,

hence

`m{H_(t+eta)>rho} >= max(0,1-(1+rho B/eta) mu(t))`.

If every point eventually hits `E_(t+eta)` and

`R(t+eta)=sup_x H_(t+eta)(x)`,

then whenever `0<mu(t)<1`,

`R(t+eta) >= (eta/B)(1/mu(t)-1)`.

For the fixed strict near-band Wang shells of `VIS-425`, the normalized amplitude satisfies the orbit-Lipschitz bound

`B_N <= Omega_N < log 2`.

Writing

`mu_N(t)=m_H{z:A_N(z)>=t}`,

one therefore has the source-independent fixed-shell tariff

`m_H{H_(N,t+eta)>rho}`
` >= max(0,1-(1+rho Omega_N/eta) mu_N(t))`,

and, when `0<mu_N(t)<1`,

`R_N(t+eta) >= (eta/Omega_N)(1/mu_N(t)-1)`.

Thus a rare high-amplitude target **necessarily produces a long pre-saturation hitting tail under the exact Haar self-null**. A large cover radius or a long quiet window is not by itself evidence that an arithmetic selector is atypical; target rarity already forces such behavior before any selector information is used.

**Evidence/status:** `EXACT-DERIVED + REPRESENTATION-CERTIFIED + QUANTITATIVE NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This is a one-sided lower bound on generic hitting difficulty. It gives no upper bound on the cover radius, no mixing theorem, no selector anomaly, no asymptotic law for the changing Wang family, and no RH consequence.

## 1. A hit of the higher target forces a block of lower-target occupation

Put

`h=eta/B`.

Suppose `H_(t+eta)(x)<=rho`. Because the higher target is closed, take a hitting time `u_0` with

`|u_0|<=rho`

and

`A(x tau(u_0))>=t+eta`.

For every `u` with `|u-u_0|<=h`, orbit-Lipschitz continuity gives

`A(x tau(u))`
` >= A(x tau(u_0))-B|u-u_0|`
` >= t+eta-Bh`
` = t`.

Therefore the lower target `E_t` is occupied for the whole interval

`[u_0-h,u_0+h]`,

which has length `2h` and lies inside

`[-rho-h,rho+h]`.

Consequently, with

`L_(rho,h)(x)=int_(-rho-h)^(rho+h) 1_(E_t)(x tau(u)) du`,

one has the pointwise implication

`H_(t+eta)(x)<=rho  =>  L_(rho,h)(x)>=2h`.

The threshold buffer `eta` is essential here. A single hit of `{A>=t}` need not contain a positive-length interval on which `{A>=t}` remains true, whereas a hit of `{A>=t+eta}` creates exactly such an interval by the orbit-Lipschitz bound.

## 2. Haar invariance turns occupation length into a finite-time hitting bound

Integrate the previous inequality over `X`. Markov's inequality gives

`2h m{H_(t+eta)<=rho}`
` <= int_X L_(rho,h)(x) dm(x)`.

By Tonelli and invariance of `m` under the flow,

`int_X L_(rho,h)(x) dm(x)`
` = int_(-rho-h)^(rho+h) m(E_t) du`
` = 2(rho+h) mu(t)`.

Dividing by `2h` and using `h=eta/B` yields

`m{H_(t+eta)<=rho}`
` <= ((rho+h)/h) mu(t)`
` = (1+rho B/eta) mu(t)`.

Taking complements gives the displayed lower bound for the hitting-time tail.

No independence, mixing, decorrelation, Diophantine rate, or shrinking-target theorem enters this estimate. It uses only a measure-preserving flow, a nested pair of amplitude targets, and the orbit-Lipschitz certificate.

## 3. Target rarity forces a cover-time lower bound

Assume now that every starting point eventually hits `E_(t+eta)`, as `VIS-428` proves for every fixed nonzero Wang shell and every fixed `t+eta<1`.

If

`rho < (eta/B)(1/mu(t)-1)`,

then

`(1+rho B/eta) mu(t) < 1`.

The hitting probability by radius `rho` is therefore strictly below one, so some starting point satisfies

`H_(t+eta)(x)>rho`.

Hence `R(t+eta)>rho`. Letting `rho` increase to the displayed boundary gives

`R(t+eta) >= (eta/B)(1/mu(t)-1)`.

This lower bound is deliberately one-sided. Compact minimality in `VIS-428` proves that `R_N(t+eta)` is finite for each fixed shell; the present argument proves that it cannot be too small when a nearby lower superlevel set has small Haar mass. The two statements bracket different sides of the same pre-saturation problem but do not determine its scale sharply.

## 4. Wang specialization

For the strict near-band Wang shells, `VIS-425` proves that along the prime-log orbit

`u -> F_N(z tau_N(u))/S_N`

the normalized amplitude is `Omega_N`-Lipschitz, with

`Omega_N<log 2`.

Applying the general occupation argument with

`A=A_N`, `B=Omega_N`, `m=m_H`

gives

`m_H{H_(N,t+eta)>rho}`
` >= max(0,1-(1+rho Omega_N/eta) mu_N(t))`.

Because `Omega_N<log 2`, the weaker shell-uniform form

`m_H{H_(N,t+eta)>rho}`
` >= max(0,1-(1+rho log(2)/eta) mu_N(t))`

is also valid.

If `Omega_N=0`, the along-flow amplitude is constant; density of the prime-log orbit and continuity then make `A_N` constant on the torus, and normalization forces `A_N==1`. That degenerate shell has no rare sub-maximal target and is outside the nontrivial rarity regime.

The important new control is therefore not another random-phase model. It is an exact implication inside the shell's own Haar translation null: **before attributing a long quiet interval to an arithmetic selector, price how rare the corresponding high-amplitude target already is under Haar.**

## 5. Prior art and novelty audit

The recurrence principle surrounding inverse target measure is classical. Mark Kac's recurrence lemma originates in Mark Kac, **On the notion of recurrence in discrete stochastic processes**, *Bulletin of the American Mathematical Society* 53 (1947), 1002--1010, DOI `10.1090/S0002-9904-1947-08927-8`. Kac's theorem concerns mean return times and is not being claimed here as the source of the displayed finite-window inequality.

Modern shrinking-target and hitting-time laws often recover inverse-measure scales under substantially stronger dynamical hypotheses. Stefano Galatolo, **Hitting time in regular sets and logarithm law for rapidly mixing dynamical systems**, *Proceedings of the American Mathematical Society* 138 (2010), 2477--2487, arXiv `0906.3416`, treats regular targets under rapid mixing. Bassam Fayad, **Mixing in the absence of the shrinking target property**, *Bulletin of the London Mathematical Society* 38 (2006), 829--838, shows how delicate shrinking-target behavior can be for toral dynamics and records the Diophantine sensitivity of translation examples.

Those sharper theories are deliberately not imported into the Wang claim. The prime-log flow is a quasiperiodic torus translation, not a rapidly mixing system. The Mathia result is the elementary occupation estimate above, specialized using the already-proved Wang orbit-Lipschitz bound. No novelty is claimed for general recurrence, occupation-time arguments, Markov/Tonelli, or inverse-target-measure heuristics.

## 6. Representation audit, boundaries, and falsification

The statement is invariant under torus-coordinate relabelling and starting-phase translation. It depends only on the intrinsic normalized amplitude along the actual shell flow, the Haar mass of its superlevel target, and the certified orbit-Lipschitz scale. No plotted geometry, colormap, discretization, or arbitrary random-phase surrogate enters the claim.

The buffer `eta` cannot simply be dropped. The argument controls hits of `E_(t+eta)` through occupation of `E_t`; it does not assert

`m{H_t<=rho} <= (1+rho B/eta) mu(t)`

with `eta=0`. Likewise, small `mu(t)` yields a lower bound on generic hitting difficulty, not an upper bound and not a complete hitting-time law. A selected phase lying beyond this lower-bound scale may still be entirely typical under the exact Haar tail.

For a changing family, the bound becomes informative only after the shell-dependent quantities `Omega_N`, `mu_N(t)`, `eta`, and `rho_N` are specified consistently. If `t=t_N` approaches one, the buffer and target masses must be frozen as part of the shrinking-target test rather than chosen after seeing the selected trajectory.

Falsify the derivation by finding a hit of `E_(t+eta)` that does not force an `eta/B` neighborhood inside `E_t`, a failure of Haar invariance/Tonelli for the stated finite occupation integral, or a Wang shell violating the `VIS-425` orbit-Lipschitz bound used in the specialization.

## Dependencies

- `VIS-419`: fixed Wang shells live on the base-prime torus and Haar is the exact translation self-null.
- `VIS-425`: strict near-band Wang shells have orbit-Lipschitz normalized amplitude with `Omega_N<log 2`.
- `VIS-428`: every fixed nonzero shell reaches every fixed sub-maximal target from every starting phase within a finite shell-specific radius.

## Research consequence

The pre-saturation branch in `CLUE-wang-phase-anchored-small-values` now has a compulsory **target-rarity control**. Before treating a large `H_(N,t)` or `R_N(t)` as evidence of an arithmetic selector effect, estimate the exact-shell Haar superlevel mass at a nearby buffered threshold and compare the observed radius with the scale forced by the inequality above.

When

`(1+rho_N Omega_N/eta) mu_N(t) << 1`,

most Haar phases are guaranteed not to have hit `E_(t+eta)` by radius `rho_N`; a quiet selected phase at that radius is therefore generically expected, not anomalous. Only after this inexpensive one-sided control fails to explain the observation is it worth estimating the full same-shell hitting-time tail or pursuing sharper Diophantine/shrinking-target structure.