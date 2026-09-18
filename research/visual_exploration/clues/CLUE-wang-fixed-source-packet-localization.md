---
id: CLUE-visual-wang-fixed-source-packet-localization
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-283-wang-fixed-source-cross-frequency-separation.md
  - research/visual_exploration/findings/VIS-284-wang-fixed-source-packet-projection-bound.md
  - research/visual_exploration/findings/VIS-285-wang-q-zero-source-observable-analytic.md
  - research/visual_exploration/findings/VIS-286-wang-large-source-diagonal-linearizes.md
---

# Does Wang packet localization preserve the fixed-source diagonal profile without manufacturing strip gain?

## Observation

`VIS-283` isolates the fixed-source coefficient-scale field energy after the exact gamma baseline is retained. On compact fixed physical-source windows, the signed prime/source cross is power-small after packet normalization, while the surviving `L^-2` arithmetic profile before packet projection is the positive diagonal quantity

`Q_gamma(x)=S_D(x)+C_Lambda/x^2`,

with `x=e^(2*pi*q)`.

`VIS-284` resolves the fixed-interior packet interface. For every uniformly `L^1`-bounded packet family supported inside one fixed compact physical-source interval, the coefficient-scale contribution is a bounded linear projection of `Q_gamma(e^(2*pi*q))`. If the packet also annihilates the universal fixed-source Laplace mode `e^(-4*pi q)`, shrinking its support with bounded total variation makes the arithmetic projection vanish at least linearly in the support diameter. Retaining a nonzero response under such localization forces inverse-width growth of the packet total variation.

`VIS-285` closes one explicit left-boundary mechanism. On the entire first source cell `1<=x<=2`, equivalently `0<=q<=log(2)/(2*pi)`, the diagonal profile is exactly

`Q_gamma(e^(2*pi*q))=2 C_Lambda cosh(4*pi*q)`.

It is finite at `q=0`, has zero first derivative there, and departs from its boundary value only quadratically. Thus approaching `q=0` cannot create a threshold or blow-up through `Q_gamma` itself.

`VIS-286` closes the opposite isolated-profile escape. Classical prime-number-theorem partial summation sharpens Wang's exact square sum to

`Q_gamma(x)=log x+o(1)`,

so in physical-source coordinates

`Q_gamma(e^(2*pi*q))=2*pi*q+o(1)` as `q->infinity`.

After subtracting that forced linear baseline, every uniformly `L^1`-bounded packet whose entire support escapes to `q->infinity` has vanishing response to the isolated diagonal residual. Even the prime-power derivative jumps flatten, with `q`-derivative jump `-8*pi Lambda(m)^2/m -> 0` at escaping prime powers.

The unresolved interface is therefore no longer a hidden singularity of `Q_gamma` at either source end. It is the behavior of the **complete moving-source Wang formula** when packet support reaches a boundary, source grows with `T`, or packet normalization itself becomes singular.

## Research question

For a predeclared moving packet family with `x=x(T)=e^(2*pi q_T)` remaining inside Wang's allowed range but leaving every fixed compact source interval, can the complete pair statistic still separate genuine new source-scale information from the universal `2*pi*q` diagonal baseline, source-dependent theorem remainders, other field sectors, and packet conditioning?

Likewise, for support approaching `q=0`, can the remaining terms in the complete formula be controlled uniformly strongly enough that any residual signal survives after the exact regular baseline from `VIS-285` and the packet norm are charged?

A positive mechanism now has to live outside the isolated diagonal profile itself.

## Why it may matter

The fixed-source analysis has eliminated the easiest representation artifacts at both ends. Ordinary fixed-interior localization is only a bounded projection and pays an inverse-width conditioning cost; the left endpoint of the isolated source profile is analytic; the large-source endpoint is only a universal linear baseline plus a vanishing arithmetic residual.

This sharply separates source geometry from theorem uniformity. A large response from a moving packet is interesting only if it cannot be reproduced by the explicit `2*pi*q` baseline, by growth of the packet norm, or by deterioration of source-dependent error terms. Conversely, a uniform moving-source asymptotic that survives those charges would identify genuinely new information not visible in the compact-source model.

## Decisive test

Choose one growth regime before inspecting the resulting signal. Record the packet center and width, `L^1` norm, the corresponding `x(T)=e^(2*pi q_T)`, and its relation to Wang's admissible `x<=T^lambda` range.

For an escaping family, subtract the exact asymptotic diagonal baseline `2*pi*q` first. Then return to Wang's complete source representation and propagate the chosen `x(T)` through every load-bearing remainder rather than importing compact-source `O_K` notation. In particular, quantify the localization error of Lemma 2.4, the mean-value remainder in the `D_x` sector, the `B_x+E_x` sector, and every normalization factor after packet integration. Require the resulting total error, multiplied by the packet norm, to be smaller than the proposed residual signal.

For a family approaching `q=0`, insert the exact first-cell identity from `VIS-285` before estimating the remaining sectors and prove a boundary-uniform error strong enough to survive the same conditioning audit.

Kill the direction if the claimed enhancement is reproduced by `2*pi*q`, by the regular `q=0` source baseline, by packet-norm amplification, or by loss of uniformity in an existing theorem remainder. A surviving effect must require a term absent from the established diagonal projection and remain controlled under one explicit moving-source budget.

## Evidence boundary

`VIS-283` establishes the fixed-source diagonal profile and the negligibility of the signed cross sector in its stated compact regime. `VIS-284` establishes the bounded packet projection there and the inverse-width conditioning cost for localized Laplace-null packets. `VIS-285` establishes that `Q_gamma` is exactly regular at `q=0`. `VIS-286` establishes that `Q_gamma(e^(2*pi*q))-2*pi*q -> 0` as `q->infinity` and that bounded-total-variation translating packets cannot preserve that isolated residual.

None of these findings gives a moving-source asymptotic for the **complete** Wang statistic, a boundary-uniform theorem for all remaining sectors, or control for packet families whose total variation diverges. No source-threshold theorem for the full statistic, off-critical-strip gain, new pair-correlation theorem, RH criterion, or new arithmetic invariant is established here.

## Research disposition

Outcome so far: **narrowed**.

The fixed-interior mechanism and both obvious endpoint singularities of the isolated diagonal profile are closed. Continued investigation is justified only at the coupled moving-source interface: source-dependent remainders and other sectors under an explicit `x(T)` growth law, or deliberately singular packet conditioning whose amplification is quantitatively charged. A later invocation should choose one such growth regime and derive the complete error budget rather than repeat fixed-source packet tests or reinterpret `Q_gamma` itself as the missing source-threshold mechanism.