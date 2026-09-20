# VIS-348 — higher Wang moments inherit the same phase-entropy gate after exact lower-order cancellation

## Claim

Let Wang's exact summatory-remainder multiplier be

`m(xi)=4(1+i xi)/(4+xi^2)`.

For each large `X`, consider a finite translated-dilate bank

`M_X(xi)=sum_j c_(j,X) exp(-i b_(j,X) xi) m(a_(j,X) xi)`,

with `a_(j,X)>0` and frequency-independent complex coefficients. Write the exact high-frequency coefficients from `VIS-343` as

`beta_(2n+1)=4 i (-4)^n`,
`beta_(2n+2)=4 (-4)^n`.

Fix an integer `q>=1`. For each translation `b`, define the `q`th inverse-scale moment

`S_(b,q,X)=sum_(j:b_(j,X)=b) c_(j,X) a_(j,X)^(-q)`,

and the corresponding exponential polynomial

`P_(q,X)(xi)=sum_b S_(b,q,X) exp(-i b xi)`.

Assume that all lower moment polynomials vanish identically,

`P_(k,X) == 0`, `k=1,...,q-1`,

and that on an interval `J_X subset [X,2X]` of length `ell_X>0`,

`sup_(xi in J_X) |M_X(xi)| <= C_0 X^(-(q+1))`.

Put

`T_(q+1,X)=sum_j |c_(j,X)| a_(j,X)^(-(q+1))`.

There is a finite constant `C_q`, depending only on `q`, such that with

`D_(q,X)=[2^q C_0 + C_q T_(q+1,X)]/|beta_q|`,

one necessarily has

`sup_(xi in J_X)|P_(q,X)(xi)| <= D_(q,X)/X`.

Let `B_(q,X)` be the number of translations with `S_(b,q,X) != 0`. If `B_(q,X)=0`, the `q`th moment is also cancelled exactly and the first unresolved order moves to `q+1`. If `B_(q,X)=1`, then

`X ||S_(q,X)||_2 <= D_(q,X)`.

If `B_(q,X)>=2`, let

`Delta_(q,X)=min_(b!=b') |b-b'|`

among the active `q`th-moment phases, and put

`L_(q,X)=4(B_(q,X)-1)/Delta_(q,X)`,
`e_(q,X)=min(ell_X,L_(q,X))`.

Then the same measurable Turán--Nazarov constant `A` used in `VIS-346` and `VIS-347` gives the necessary budget

`(B_(q,X)-1) log(A L_(q,X)/e_(q,X))`
` >= log( X ||S_(q,X)||_2 / (sqrt(2) D_(q,X)) )`.

Therefore exact cancellation of the first `q-1` Wang tail moments does **not** make the next surviving moment locally cheap. Once the first nonzero moment is reached, hiding it on a window costs the same one-power `X` concentration budget, with the relevant phase count, phase spacing and conditioning evaluated at that moment order.

In particular, if

`D_(q,X)/||S_(q,X)||_2 = X^(o(1))`,

then the phase-entropy term must be `(1-o(1)) log X`. For fixed `B>=2`, power-law windows and phase gaps

`ell_X=X^(-alpha+o(1))`,
`Delta_(q,X)=X^(-beta+o(1))`

again require

`(B-1)(alpha+beta)>=1`.

For macroscopic windows and uniformly separated active `q`th-moment phases, one again needs

`B_(q,X) log B_(q,X) >= (1-o(1)) log X`,

up to constants. The threshold is independent of how many lower inverse-frequency orders were already cancelled exactly.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL TURAN-NAZAROV PROPAGATION + HIGHER-MOMENT NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

The result is conditional on exact cancellation of the lower moment polynomials. It does not classify local cancellation produced by interaction among several nonzero asymptotic orders, frequency/source-dependent coefficients, infinite expansions, or signed arithmetic cancellation in `G`.

## 1. Uniform remainder after any fixed Wang tail order

`VIS-343` gives the asymptotic coefficients `beta_k` above. For fixed `q`, define

`R_q(z)=m(z)-sum_(k=1)^q beta_k z^(-k)`.

The function

`z^(q+1) R_q(z)`

is continuous for `z>0`. As `z->infinity`, it tends to the finite coefficient `beta_(q+1)`. As `z->0+`, multiplication by `z^(q+1)` kills both the bounded rational term `m(z)` and every retained inverse power `z^(-k)` with `k<=q`. Hence

`C_q=sup_(z>0) z^(q+1)|R_q(z)| < infinity`.

This gives the global bound

`|R_q(z)| <= C_q z^(-(q+1))`, `z>0`.

Substituting `z=a_(j,X) xi`, summing the bank, and grouping by moment order yields

`M_X(xi)`
` = sum_(k=1)^q beta_k xi^(-k) P_(k,X)(xi) + R_(bank,q,X)(xi)`,

with

`|R_(bank,q,X)(xi)| <= C_q xi^(-(q+1)) T_(q+1,X)`.

Unlike a bare asymptotic `O`-term, the dependence on coefficient size and dilation scale remains explicit through `T_(q+1,X)`.

## 2. Exact lower cancellations isolate the first surviving moment

Under

`P_(1,X)=...=P_(q-1,X)==0`,

the expansion reduces to

`M_X(xi)=beta_q xi^(-q) P_(q,X)(xi)+R_(bank,q,X)(xi)`.

For `xi in J_X subset [X,2X]`,

`|P_(q,X)(xi)|`
` <= xi^q |M_X(xi)|/|beta_q| + xi^q |R_(bank,q,X)(xi)|/|beta_q|`
` <= [2^q C_0 + C_q T_(q+1,X)]/(|beta_q| X)`
` = D_(q,X)/X`.

The important point is structural: after `q-1` exact tail moments have been removed, the next surviving moment is again forced down by a full extra factor `X^-1` if the bank claims one additional local smoothing order.

If only one translation carries the `q`th moment, `|P_(q,X)|` is identically `||S_(q,X)||_2`, giving the one-phase inequality immediately.

## 3. The phase geometry is the same at every moment order

For `B_(q,X)>=2`, `P_(q,X)` is a finite exponential polynomial in exactly the form used by `VIS-345`--`VIS-347`. The direct reference-frame estimate is pointwise in its coefficients and frequencies, so on an interval `I_X` of length

`L_(q,X)=4(B_(q,X)-1)/Delta_(q,X)`

containing a subinterval `E_X subset J_X` of length `e_(q,X)`, it gives

`sup_(I_X)|P_(q,X)| >= (1/sqrt(2)) ||S_(q,X)||_2`.

The measurable Turán--Nazarov inequality then gives

`sup_(I_X)|P_(q,X)|`
` <= (A L_(q,X)/e_(q,X))^(B_(q,X)-1) sup_(E_X)|P_(q,X)|`.

Combining the two displays and `E_X subset J_X` yields

`sup_(J_X)|P_(q,X)|`
` >= (1/sqrt(2)) ||S_(q,X)||_2`
`    (e_(q,X)/(A L_(q,X)))^(B_(q,X)-1)`.

The upper bound from Section 2 proves the claimed entropy inequality.

Nothing in this step depends on `q`: after lower orders vanish exactly, the surviving coefficient is again just an exponential polynomial. This is why the same phase-resolution cost reappears at every tail order.

## 4. Consequence for higher-order local smoothing claims

The fixed-bank theorem `VIS-344` says that uniform polynomial tail improvement requires fiberwise moment cancellation. `VIS-346` and `VIS-347` then show that the first moment cannot merely be hidden on an ordinary window without paying a Turán--Nazarov concentration cost.

The present result joins those two mechanisms. For a finite bank, inspect the moment polynomials in order. If `P_1` is nonzero, `VIS-347` already applies. If `P_1` vanishes exactly, move to `P_2`; if that also vanishes exactly, move again. At the **first surviving moment `q`**, any claimed extra local inverse-frequency order faces the same phase-entropy/conditioning gate stated above.

Thus exact moment cancellation and short-window concentration are complementary resources rather than interchangeable labels. A proposed higher-order local mechanism must say which lower moments are genuinely zero and which first surviving moment is only being made small on the observation window. It cannot credit exact Vandermonde cancellation at low orders and then treat the next oscillatory coefficient as free because the target is local rather than uniform.

This still leaves a real escape. Several nonzero asymptotic orders might interact on a finite window in a way not captured by the conditional isolation above; coefficients may depend on frequency or directly on the source `G`; or an infinite/source-adaptive construction may prove a signed arithmetic estimate rather than multiplier smallness. Those routes require a different argument rather than a stronger interpretation of this theorem.

## Prior-art audit

The two ingredients are classical and already independently anchored in the preceding findings.

F. L. Nazarov, **Local estimates for exponential polynomials and their applications to inequalities of the uncertainty principle type**, *Algebra i Analiz* 5:4 (1993), 3--66; English translation *St. Petersburg Mathematical Journal* 5:4 (1994), 663--717, gives the local Turán-type estimates for exponential polynomials used in `VIS-346`--`VIS-347`.

Omer Friedland and Yosef Yomdin, **An observation on the Turán--Nazarov inequality**, *Studia Mathematica* 218:1 (2013), 27--39, DOI `10.4064/sm218-1-2`, treats the measurable-set form and metric-entropy refinements. The exponent equal to the number of exponential terms minus one is classical.

Cancellation of successive asymptotic powers by scale mixtures is likewise classical Richardson/Vandermonde extrapolation; `VIS-343` records Avram Sidi, **The Richardson Extrapolation Process with a Harmonic Sequence of Collocation Points**, *SIAM Journal on Numerical Analysis* 37:5 (2000), 1729--1746, DOI `10.1137/S0036142998340137`, as the explicit prior-art anchor.

No novelty is claimed for Turán--Nazarov concentration, asymptotic expansion, Richardson extrapolation, or Vandermonde moment cancellation. The Mathia-specific statement is only their higher-moment coupling for Wang's exact rational multiplier: after exact lower moment cancellation, the first surviving translated moment inherits the same local phase-entropy gate as the first moment.

A targeted literature search by the combined mechanism did not identify a standard theorem stated for Wang's multiplier or this exact tail-moment hierarchy. That absence is not used as a novelty claim.

## Dependencies

- `VIS-333`: exact Wang multiplier and one-order log-frequency smoothing.
- `VIS-343`: nonzero Wang tail coefficients and pure-dilate moment cancellation.
- `VIS-344`: translation-fiber moment polynomials and exact uniform cancellation hierarchy.
- `VIS-345`: resolving-interval lower bound for finite exponential polynomials.
- `VIS-346`: fixed-bank Turán--Nazarov short-window obstruction.
- `VIS-347`: variable first-moment phase-entropy budget.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue narrowed here.

## Research consequence

The finite translated-dilate branch is narrower than the first-moment statement alone suggests. **At whatever inverse-frequency order the exact fiberwise cancellations stop, the first surviving moment must pay the same phase-entropy and conditioning cost to be hidden on a window.**

A future finite-bank proposal should therefore expose its moment ledger before being credited with local smoothing: exact zeros for the cancelled orders, followed by the phase geometry and conditioning of the first nonzero order. If that order cannot pass the displayed budget, the proposal is already excluded without invoking any arithmetic property of `G`.

The accepted Wang clue remains open only beyond this scalar hierarchy: genuinely interacting nonzero orders on finite windows, frequency/source-dependent coefficients, infinite expansions, or signed arithmetic information in `G` that survives the downstream derivative-repayment audit.