# VIS-180 — bounded prime gaps make the linear-support variance boundary genuinely nonuniform

## Claim

Keep the notation of `VIS-179`. There exists a fixed even integer `d>=2` and an infinite sequence of consecutive prime pairs

`p_j < q_j = p_j + d`

with `p_j -> infinity`. For each pair, set

`y_j=q_j`, `P_(y_j)={p_j,q_j}`, `w_(p_j)=w_(q_j)=1`, `H_j=p_j`, `T=0`.

Then

`y_j/H_j -> 1`

but the deterministic continuous-window variance does **not** converge to the matched Haar value:

`H_j^(-1) int_0^(H_j) S_(y_j)(t)^2 dt`
` -> 1/8 + (1/8) sin(d)/d != 1/8`.

Therefore the uniform arbitrary-subset/arbitrary-positive-weight variance null from `VIS-179` cannot be extended from `y=o(H)` to the full linear boundary `y asymp H` with an `o(1)` error. The `O(y/H)` scale in `VIS-179` is genuinely non-vanishing at linear support for the class it controls.

This does **not** produce zeta-specific evidence. The surviving term is an explicit two-frequency clock effect created by a bounded prime-log separation. It is a matched-control obstruction showing that linear-support variance separation can arise before any new source information enters.

**Evidence/status:** `CLASSICAL BOUNDED-PRIME-GAP THEOREM + EXACT TWO-FREQUENCY AVERAGE + SHARPNESS/NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No claim is made that the same non-Haar limit occurs for the full prime set, for prime-power weights on all primes, for every linear-support sequence, for higher moments, or for zeta itself.

## 1. Bounded prime gaps supply a fixed close-frequency subsequence

Maynard's bounded-gap theorem proves unconditionally that

`liminf_n (p_(n+1)-p_n) <= 600`.

Hence there are infinitely many consecutive prime pairs with gap at most `600`. Only finitely many positive integer gaps are available in that range, so by the pigeonhole principle at least one fixed gap `d` occurs infinitely often. Apart from the isolated pair `(2,3)`, consecutive prime gaps are even, so the recurrent `d` may be taken even and positive.

Fix an infinite subsequence

`q_j-p_j=d`.

No identification of the recurrent gap is needed below; only that `d` is fixed and nonzero.

## 2. The two-prime field has one persistent low beat frequency

For the support `{p,q}` with equal weights,

`Q_y=2`

and

`S_y(t)=-(1/(2 sqrt(2))) [cos(t log p)+cos(t log q)]`.

Put

`delta=log(q/p)>0`.

Expanding exactly gives

`S_y(t)^2`
` = 1/8 + (1/8) cos(delta t)`
`   + (1/16) cos(2t log p)`
`   + (1/8) cos(t log(pq))`
`   + (1/16) cos(2t log q)`.

The first oscillatory term is the beat between the two close prime-log frequencies. The other three frequencies are of size `Theta(log p)` and are therefore rapidly averaged when the window length is of order `p`.

## 3. At `H=p`, the beat survives with constant amplitude

Take `H=p` and average on `[0,H]`. For every nonzero `lambda`,

`H^(-1) int_0^H cos(lambda t) dt = sin(H lambda)/(H lambda)`.

Since `q=p+d` with fixed `d`,

`delta=log(1+d/p)=d/p+O_d(p^-2)`,

so

`H delta = p log(1+d/p) -> d`.

Consequently

`H^(-1) int_0^H cos(delta t) dt -> sin(d)/d`.

Meanwhile

`H log p -> infinity`, `H log q -> infinity`, `H log(pq) -> infinity`,

so the remaining oscillatory averages tend to zero. Therefore

`H^(-1) int_0^H S_y(t)^2 dt`
` -> 1/8 + (1/8) sin(d)/d`.

The correction is nonzero: if `sin(d)=0` for a positive integer `d`, then `d` would be a nonzero integer multiple of `pi`, impossible because `pi` is irrational.

Finally, with `y=q=p+d`,

`y/H=(p+d)/p -> 1`.

Thus the failure occurs exactly at a linear support/window ratio, not by taking `y/H` to infinity.

## 4. What this sharpens in `VIS-179`

`VIS-179` proves the uniform estimate

`|time variance - 1/8| <= C y/H`

for arbitrary positive weights and arbitrary prime subsets. The present construction shows that no uniform replacement whose right-hand side tends to zero merely from `y/H -> 1` can hold on that same class.

The mechanism also explains why the boundary is delicate. In the sublinear regime `y=o(H)`, even the closest possible prime-log frequencies accumulate many beat periods across the averaging window. At `y~H`, a bounded additive prime gap produces

`H log(q/p)=Theta(1)`,

so one low beat mode can retain constant memory of the deterministic orbit.

This is a representation/sampling effect, not an arithmetic-source discriminator. Any visual statistic that interprets a linear-support second-moment discrepancy as zeta-specific must first rule out exactly this close-frequency crowding mechanism in its matched control.

## 5. Prior art and novelty boundary

James Maynard, **Small gaps between primes**, *Annals of Mathematics* 181:1 (2015), 383–413, DOI `10.4007/annals.2015.181.1.7`, proves in particular `liminf_n (p_(n+1)-p_n)<=600`. That theorem is the sole non-elementary input needed to produce an infinite fixed-gap subsequence.

The averaging calculation after choosing such a pair is elementary Fourier algebra. No novelty is claimed for bounded gaps, beat frequencies, Dirichlet-polynomial averaging, or the general observation that near frequencies mix slowly. The Mathia-specific content is the exact boundary audit for the active `VIS-179` matched-control class: its uniform sublinear variance null has a concrete classical obstruction at `y~H` even before any zeta-specific source term is introduced.

A targeted literature search did not identify this exact two-prime consequence as a named theorem; that absence is not used as a novelty claim.

## 6. Boundaries and falsification

The result is existential within the arbitrary-subset class. It does not show that a natural full-support prime sum has a persistent variance defect at `y~H`, because diffuse coefficients may average the bounded-gap pairs away.

Equal weights on exactly two primes are admissible under `VIS-179` but are deliberately adversarial. The conclusion is therefore that the **uniform theorem class** has a sharp linear-support obstruction, not that every natural zeta-facing weighting exhibits one.

The interval starts at `T=0`. Since a putative extension of `VIS-179` would be uniform in `T`, one valid sequence of starts already rules out such a uniform `o(1)` extension. No statement is made about a typical translated interval.

Falsify the finding by finding an error in the bounded-gap pigeonhole step, the exact expansion of `S_y^2`, the limit `p log(1+d/p)->d`, or the claim that the remaining frequencies average to zero on a window of length `p`.

## Research consequence

Crossing from `y=o(H)` to `y~H` is a genuine control transition, but **not automatically a source-sensitive opportunity**. A global quadratic statistic at linear support must distinguish a source effect from deterministic slow beating among close prime-log frequencies.

For the accepted prime-phase recursive-geometry clue, a linear-support variance residual is therefore admissible only after a matched control preserves the relevant local prime-frequency crowding, or after a theorem shows that the chosen full-support coefficient profile suppresses this bounded-gap channel. The next useful question is no longer whether `VIS-179` can be extended uniformly to `y~H`; this finding shows that it cannot on its stated arbitrary-subset class.