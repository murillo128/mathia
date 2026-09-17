# AF-401 — Prime short-interval fidelity pushes shrinking locality to 17/30 successor depth

## Status

`LITERATURE+DERIVED` · `EXACT-DERIVED` · `ARITHMETIC-FIDELITY` · `SHORT-INTERVALS` · `MOVING-SCALE` · `QUANTITATIVE-SAMPLING` · `LOCAL-TO-GLOBAL` · `NO-NOVELTY-CLAIM`

## Claim

AF-400 showed that a shrinking logarithmic locality wall for the rational-prime source must be paid for with source information at the same moving scale. The current unconditional uniform short-interval prime number theorem supplies that information far below the polylogarithmic walls obtained there from a global PNT remainder.

For the prime source define

\[
B_N(h)=\max\left\{R\ge 0:\log\frac{p_{N+R}}{p_N}\le h\right\}
      =\pi(e^h p_N)-N.
\tag{1}
\]

Fix `epsilon` with

\[
0<\varepsilon<\frac{13}{30}.
\]

If

\[
h_N\to0,
\qquad
h_N\ge p_N^{-13/30+\varepsilon}
\tag{2}
\]

for all sufficiently large `N`, then

\[
\boxed{
B_N(h_N)\sim N h_N.
}
\tag{3}
\]

In particular, for every fixed

\[
0<\beta<\frac{13}{30},
\tag{4}
\]

the polynomially shrinking wall

\[
h_N=p_N^{-\beta}
\tag{5}
\]

obeys

\[
\boxed{
B_N(p_N^{-\beta})
\sim Np_N^{-\beta}
= N^{1-\beta}(\log N)^{-\beta}(1+o(1)).
}
\tag{6}
\]

Thus at the current uniform short-interval boundary, taking

\[
h_N=p_N^{-13/30+\varepsilon}
\]

costs

\[
B_N(h_N)=N^{17/30+\varepsilon+o(1)}.
\tag{7}
\]

The exponent `17/30` is therefore a present unconditional **all-starting-primes conversion boundary** for this physical-to-successor locality law, up to fixed epsilon slack. It is not claimed to be sharp or intrinsic.

## Short-interval input

Larry Guth and James Maynard prove in Corollary 1.3 of **“New large value estimates for Dirichlet polynomials,”** *Annals of Mathematics* **203**(2), 623--675 (2026), DOI `10.4007/annals.2026.203.2.6`, that for every fixed `eta>0`, uniformly for

\[
x^{17/30+\eta}\le y\le x^{0.99},
\tag{8}
\]

one has a prime-number-theorem asymptotic

\[
\pi(x+y)-\pi(x)
=\frac{y}{\log x}(1+o(1)).
\tag{9}
\]

Their published abstract records the consequence as asymptotics for primes in intervals of length `x^{17/30+o(1)}`; the paper's Corollary 1.3 gives the fixed-epsilon uniform formulation used here. The result follows from their new Dirichlet-polynomial large-value and zeta zero-density estimates. No part of that analytic-number-theory theorem is new here.

## Derivation

Put

\[
x=p_N,
\qquad
\Delta_N=x(e^{h_N}-1).
\tag{10}
\]

Then `(1)` becomes exactly

\[
B_N(h_N)=\pi(x+\Delta_N)-\pi(x).
\tag{11}
\]

Because `h_N\to0`,

\[
\Delta_N=xh_N(1+o(1))=o(x),
\tag{12}
\]

while `(2)` gives

\[
\Delta_N\ge xh_N\ge x^{17/30+\varepsilon}.
\tag{13}
\]

If `Delta_N<=x^0.99`, Guth--Maynard applies directly with `eta=epsilon`.

If `Delta_N>x^0.99`, partition `[x,x+Delta_N]` into `m=ceil(Delta_N/x^0.99)` adjacent intervals of equal length `L=Delta_N/m`. Then

\[
\frac12 x^{0.99}\le L\le x^{0.99}.
\tag{14}
\]

Every starting point `x_j` in the partition satisfies `x_j=x(1+o(1))` because `Delta_N=o(x)`. Hence, for all sufficiently large `N`,

\[
x_j^{17/30+\varepsilon/2}\le L\le x_j^{0.99}.
\tag{15}
\]

Applying `(9)` with `eta=epsilon/2` on every piece and summing yields

\[
\pi(x+\Delta_N)-\pi(x)
=\frac{\Delta_N}{\log x}(1+o(1)).
\tag{16}
\]

The error remains relative `o(1)` after summation because the short-interval estimate is uniform and the pieces have total length `Delta_N`; also `log x_j/log x ->1` uniformly across the partition.

Combining `(12)`, `(16)`, and the prime number theorem `p_N/log p_N~N` gives `(3)`. Equation `(6)` follows from

\[
p_N=N(\log N+\log\log N-1+o(1)),
\tag{17}
\]

and `(7)` is the corresponding exponent form at the Guth--Maynard scale.

## What this changes relative to AF-400

AF-400's global PNT remainder supplies `(3)` when the physical wall shrinks only slowly enough that the global counting error is negligible compared with the expected local count. That includes every fixed polylogarithmic wall `h_N=(log N)^{-A}`, but it does not reach a polynomial wall `p_N^{-beta}` with fixed `beta>0`.

The short-interval theorem changes the source resource rather than the downstream decoder: it controls prime density on an additive interval whose length is itself polynomially smaller than `p_N`. This lowers the proven physical scale from polylogarithmic shrinkage to

\[
h_N\ge p_N^{-13/30+\varepsilon},
\tag{18}
\]

and therefore lowers the corresponding successor breadth to approximately `N^{17/30+epsilon}` at the edge of the available uniform theorem.

This is exactly the moving-scale distinction identified in AF-400: the conversion coefficient remains `1`, but proving that it remains valid at a smaller wall consumes a stronger source theorem at that same locality scale.

## Prior-art and novelty audit

The `17/30` uniform exponent and the prime-count asymptotic are Guth--Maynard prior art. Their article was published online 1 March 2026 in *Annals of Mathematics* 203(2), after an earlier arXiv version `2405.20552`; the final arXiv revision is version 2 dated 7 April 2026. Their result improves the previous uniform `7/12` short-interval exponent due to Huxley.

Ayla Gafni and Terence Tao, **“On the number of exceptional intervals to the prime number theorem in short intervals,”** arXiv:`2505.24017` (2025), independently summarize the modern boundary relevant here: the PNT in every short interval is known for exponents greater than `17/30`, while an almost-all statement reaches exponents greater than `2/15`.

No novelty is claimed for short-interval prime counting, the `17/30` exponent, the zero-density input, or the standard asymptotic `p_N~N log N`. The Arithmetic Fidelity contribution is the composition with AF-400's exact physical-wall identity `(1)`: it translates the strongest uniform local prime-density scale into an explicit representation-resource law for how much successor depth is sufficient to realize a shrinking logarithmic discriminator.

## Boundaries and falsification

The fixed epsilon slack is essential. Guth--Maynard proves every exponent strictly above `17/30`; this finding does **not** assert the endpoint `17/30` itself.

Equation `(3)` is a sufficient scale law, not a lower bound proving that shallower successor information cannot work for another discriminator or another representation. Nor does the current `17/30` boundary establish optimality: any stronger uniform short-interval PNT would immediately improve `(2)` and `(7)` by the same composition.

The almost-all `2/15` exponent is deliberately not imported into `(3)`. An almost-all theorem over integer starting points does not automatically give the required statement along every prime starting point `p_N`; that transfer would need a separate exceptional-set argument.

The conclusion is also **not rational-prime identifying by itself**. Any matched source whose counting function satisfies the same uniform short-interval asymptotic obtains the same physical-to-successor conversion. In the language of the line mandate, `(3)` prices the information resource needed to retain a locality wall; it does not prove that the retained observable distinguishes rational primes from Beurling or other matched controls.

Finally, no RH consequence follows. The Guth--Maynard theorem is unconditional, and the derived law only describes fidelity of a prime-index representation under a declared shrinking-locality requirement.

## Consequences

The AF-399--AF-400 hierarchy now has a quantitative third regime:

- fixed logarithmic walls are priced by regular variation;
- arbitrary shrinking walls are not controlled by regular variation alone;
- for the rational primes, uniform short-interval density certifies every shrinking wall down to `p_N^{-13/30+epsilon}`, costing `N^{17/30+epsilon+o(1)}` successor depth at the boundary.

This makes the next resource question precise. A concrete downstream discriminator that needs a wall smaller than `(18)` cannot currently inherit its successor-depth law from the uniform Guth--Maynard theorem alone; it must either exploit stronger source structure, tolerate an exceptional set with a justified transfer to prime starts, or use a representation that does not reduce the required physical locality to raw successor breadth.