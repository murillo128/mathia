# VIS-285 — Wang's fixed-source diagonal profile is regular at the q=0 source boundary

## Claim

Keep the fixed-source diagonal profile isolated in `VIS-283`–`VIS-284`,

`Q_gamma(x)=S_D(x)+C_Lambda/x^2`,

where

`S_D(x)=sum_(n>=2) [Lambda(n)^2/n] min(n/x,x/n)^2`

and

`C_Lambda=sum_(n>=2) Lambda(n)^2/n^3`.

Wang's source parameter satisfies `x>=1`; the physical-source coordinate used by this line is

`x=e^(2*pi*q)`, `q>=0`.

For every `1<=x<=2`, all integers carrying von Mangoldt mass satisfy `n>=2>=x`, so

`min(n/x,x/n)=x/n`.

Hence exactly

`S_D(x)=C_Lambda x^2`

and therefore

`Q_gamma(x)=C_Lambda(x^2+x^-2)`.

Equivalently, for

`0<=q<=log(2)/(2*pi)`, 

one has the exact source-boundary formula

`Q_gamma(e^(2*pi*q))=2 C_Lambda cosh(4*pi*q)`.

In particular the coefficient-scale arithmetic profile has no singularity, threshold amplification, or linear cusp as `q->0+`. It reaches the finite value

`Q_gamma(1)=2 C_Lambda`,

has right derivative zero there, and admits the expansion

`Q_gamma(e^(2*pi*q)) = 2 C_Lambda + 16*pi^2 C_Lambda q^2 + O(q^4)`.

Thus the `q=0` escape left open by `VIS-284` is closed **for the source observable `Q_gamma` itself**. Any divergent or linearly amplified packet signal obtained while a family approaches `q=0` must come from packet normalization, another factor in the Wang representation, or an error term whose uniformity deteriorates there; it cannot be attributed to a singularity of this diagonal source profile.

**Evidence/status:** `EXACT-DERIVED + SOURCE-BOUNDARY NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No moving-packet theorem, uniform boundary asymptotic for the complete pair statistic, new pair-correlation theorem, new prime-power invariant, or RH implication is claimed.

## 1. Exact first source cell

Wang's coefficient sequence is

`a_n(x)=Lambda(n)/sqrt(n) min(n/x,x/n)`

for `x>=1`. The fixed-source Dirichlet energy from `VIS-282` is

`S_D(x)=sum_(n>=2) a_n(x)^2`.

For `1<=x<=2`, every `n` with `Lambda(n) != 0` satisfies `n>=2>=x`. At `x=2`, equality for `n=2` gives the same value from either branch. Thus throughout this whole first source cell,

`a_n(x)=x Lambda(n)n^(-3/2)`,

and absolute convergence gives

`S_D(x)=x^2 sum_(n>=2) Lambda(n)^2/n^3=C_Lambda x^2`.

There is no approximation here. The first possible change of formula occurs only when the source crosses the first von-Mangoldt support point `x=2`, equivalently

`q_2=log(2)/(2*pi)`.

This identifies an actual open neighborhood of the `q=0` boundary on which the source observable has a closed form rather than merely a compact-interior bound.

## 2. Boundary regularity in the physical-source coordinate

Substituting `x=e^(2*pi*q)` gives

`Q_gamma(e^(2*pi*q))`
` = C_Lambda[e^(4*pi*q)+e^(-4*pi*q)]`
` = 2 C_Lambda cosh(4*pi*q)`

for `0<=q<=q_2`.

The right-hand side is the restriction of an even entire function of `q`. Therefore the right limit at the Wang boundary `q=0` is finite and equals `2 C_Lambda`, while

`d/dq Q_gamma(e^(2*pi*q)) |_(q=0+) = 0`.

Since `C_Lambda>0`, the boundary is in fact a strict local minimum of the continued profile. Expanding `cosh` gives

`2 C_Lambda cosh(4*pi*q)`
` = 2 C_Lambda + 16*pi^2 C_Lambda q^2 + O(q^4)`.

The diagonal source layer therefore becomes *flatter*, not singular, at the left endpoint. A response proportional to `q^-a`, `|q|`, or another nonanalytic first-order boundary feature cannot come from `Q_gamma`.

## 3. Consequence for source-boundary packet searches

`VIS-284` deliberately excluded packets whose support approaches `q=0`, because its compact interval was contained in `(0,infinity)` and its uniform asymptotic remainder was only established there. That exclusion remains correct for the **complete packet theorem**: the present calculation does not manufacture uniformity of the other terms at the boundary.

What it does remove is one candidate mechanism. The isolated coefficient-scale profile itself cannot generate a source-threshold enhancement at `q=0`; on the first source cell it is explicitly bounded and analytic. Therefore any packet family claiming extra gain while approaching `q=0` must charge separately:

- growth of its total variation or other normalization;
- loss of uniformity in the fixed-source remainder;
- another source-boundary factor outside `Q_gamma`;
- or a genuinely different scaling in which the fixed-source decomposition no longer applies.

If none of those supplies a new term, approaching `q=0` only samples the finite baseline `2 C_Lambda` plus a quadratic source variation.

This does not close the other boundaries isolated by the accepted clue. In particular, source escape `q->infinity`, growing/moving support, and singularly normalized packets remain outside the present result.

## 4. Prior art and novelty boundary

The primary external source is Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026). Wang's equation (2.8) defines

`a_n=Lambda(n)n^(-1/2) min(n/x,x/n)`

for `x>=1`, and Lemma 2.5 records the standard global estimate for `sum a_n^2`. The present first-cell identity is the elementary exact specialization of those coefficients below the first support point `n=2`; no new theorem about Wang's coefficients or von Mangoldt sums is claimed.

Repository search found no existing canonical statement of the exact `1<=x<=2` formula, the `2 C_Lambda cosh(4*pi*q)` boundary profile, or its quadratic `q=0` expansion. `VIS-282` supplies the exact diagonal profile `S_D`, `VIS-283` identifies `Q_gamma` after signed recombination, and `VIS-284` leaves the source boundary explicitly unresolved. The durable contribution here is therefore a regime-specific negative control at that stated boundary, not a novelty claim in analytic number theory.

No numerical fitting or visual salience is used.

## Dependencies

- `VIS-282`: exact fixed-source Dirichlet diagonal profile `S_D(x)` and its prime-power breakpoints.
- `VIS-283`: coefficient-scale positive diagonal profile `Q_gamma(x)=S_D(x)+C_Lambda/x^2`.
- `VIS-284`: bounded fixed-interior packet projection and the explicit exclusion of packets approaching `q=0`.

## Research consequence

The left source boundary is no longer a candidate singular mechanism **through `Q_gamma` itself**. Before the first source breakpoint at `q=log(2)/(2*pi)`, the profile is exactly `2 C_Lambda cosh(4*pi*q)` and departs from its boundary value only quadratically.

`CLUE-wang-fixed-source-packet-localization` should therefore remain open but narrower. A subsequent invocation should test either the uniformity/normalization of the full packet formula as support approaches `q=0`, or a genuinely off-compact regime such as `q->infinity`; it should not treat the already isolated diagonal source profile as a possible `q=0` singularity.