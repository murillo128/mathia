# MC-426 — Bounded additive factor summaries have subpolynomial state volume

**Evidence:** `EXACT-DERIVED · NEGATIVE/OBSTRUCTION · CLASSICAL-INGREDIENTS · FRONTIER-ADVANCE`

## Claim

Let `n<=X` be squarefree and write `r=omega(n)`. Consider all ordered active factorizations

\[
n=u_1\cdots u_d,
\qquad
1\le d\le r,
\qquad
u_j>1.
\]

Fix integers `m>=1` and `B>=0`, independent of `X`. Give each prime `p|n` a bounded additive increment

\[
a(p)\in\mathbf Z^m,
\qquad
\|a(p)\|_\infty\le B,
\]

and retain each factor only through

\[
S(u)=\sum_{p\mid u} a(p).
\]

Then the number of distinct retained words

\[
\bigl(S(u_1),\ldots,S(u_d)\bigr)
\]

obtainable across **all active depths** is

\[
\exp\!\bigl(O_{B,m}(r)\bigr)=X^{o(1)}.
\]

Thus growing factor depth does not create polynomially many source states when each factor is compressed to a fixed-dimensional bounded additive statistic. More quantitatively, with fixed `B`, a family of such summaries carrying at least `X^delta` distinct states for some fixed `delta>0` requires the retained dimension to grow at least on the order of `log log X`.

## Exact derivation

First replace each signed coordinate of `a(p)` by its positive and negative parts. Recording the resulting pair is a refinement of the original summary, so it can only increase the number of distinguishable words. It is therefore enough to count `2m` nonnegative integer coordinates, each prime contributing at most `B` to each coordinate.

For one such coordinate `ell`, set

\[
A_\ell=\sum_{p\mid n}a_\ell(p),
\qquad
0\le A_\ell\le Br.
\]

At active depth `d`, every factorization produces a nonnegative sequence

\[
\bigl(S_\ell(u_1),\ldots,S_\ell(u_d)\bigr)
\]

whose entries sum to `A_ell`. Forgetting the requirement that every factor block contain a prime only enlarges the state set, so stars-and-bars gives at most

\[
\binom{A_\ell+d-1}{d-1}
\le
2^{(B+1)r}
\]

possible sequences for that coordinate, since `A_ell<=Br` and `d<=r`. Across the `2m` nonnegative coordinates there are therefore at most

\[
2^{2m(B+1)r}
\]

summary words at a fixed depth. Summing over the at most `r` active depths yields

\[
N(n)\le r\,2^{2m(B+1)r}=\exp\!\bigl(O_{B,m}(r)\bigr).
\]

Because `n` is squarefree with `r` distinct prime factors,

\[
n\ge \prod_{j=1}^{r}p_j\ge (r+1)!,
\]

so `n<=X` and Stirling's formula give

\[
r=O\!\left(\frac{\log X}{\log\log X}\right).
\]

Consequently

\[
N(n)
\le
\exp\!\left(O_{B,m}\!\left(\frac{\log X}{\log\log X}\right)\right)
=X^{o(1)}.
\]

The same calculation quantifies the dimension escape. For fixed `B`,

\[
\log N(n)=O_B(mr+\log r).
\]

If `N(n)>=X^delta` for fixed `delta>0`, then necessarily

\[
m=\Omega_{B,\delta}(\log\log X)
\]

along a sequence with `X` tending to infinity. Thus a bounded additive channel needs a growing number of independent retained coordinates before polynomial state capacity is even combinatorially possible.

There is also a direct shell version. If a shell contains at most `Delta` distinct product values `n<=X` and the state records the product value together with its additive-summary word, then the total shell state count is at most

\[
\Delta\,X^{o(1)}.
\]

So fixed-dimensional bounded additive summaries cannot amplify the shell-state exponent inherited from the number of product values.

## Relation to the current frontier

`MC-423` bounded the raw tangent multiplicity of exact product fibers at fixed depth. `MC-424` showed that fixed depth cannot amplify a shell-state exponent and quantified how rapidly raw factor depth would have to grow before polynomial multiplicity becomes possible. `MC-425` then closed the simplest growing-depth loophole: retaining only one Möbius sign bit per factor still leaves only `X^{o(1)}` source states.

The present result closes a substantially larger quotient class. A factor coordinate may now retain an alphabet whose size grows with `omega(n)` — for example `omega(u_j)` itself or a fixed list of prime-incidence counts — yet conservation of a bounded additive mass in fixed dimension still collapses the full growing-depth factorization family to `X^{o(1)}` states.

Examples covered include a fixed finite vector of counts of prime divisors lying in predetermined classes, bounded per-prime feature counts, and any fixed-dimensional integer statistic obtained by summing bounded prime-local increments. The obstruction is not that each factor has only finitely many possible labels; it is that a fixed amount of additive coordinate structure is redistributed among at most `omega(n)` active blocks.

A surviving factor-lift mechanism must therefore retain information outside this class: unbounded or increasingly precise weights, a dimension growing with `X`, exact prime/factor identities, growing-modulus residue or character data, or genuinely non-additive relations between coordinates.

## Prior-art and novelty boundary

The combinatorial ingredients are classical. Ordered nontrivial factorizations of squarefree integers reduce to partitions of their distinct prime factors into ordered blocks; R. D. James, *The Factors of a Square-Free Integer*, Canadian Mathematical Bulletin 11 (1968), 733–735, studies this raw factorization count. Stars-and-bars gives the weak-composition bound, and the maximal size of `omega(n)` follows elementarily from the primorial lower bound and Stirling's formula.

No novelty is claimed for any of those ingredients or for counting bounded additive functions. The additional result is the mechanism-specific quotient/no-go statement: **even when growing-depth squarefree factorization has large raw multiplicity, every fixed-dimensional bounded additive projection of the factor blocks has only subpolynomial state volume**. A targeted prior-art search found the classical raw-factorization and additive-counting ingredients but did not identify this exact Möbius-factor-channel obstruction as a named theorem.

## Limits and decisive test

This is an information-capacity obstruction, not an improved estimate for `M(x)`. It does not show that `X^{o(1)}` states cannot have strong analytic consequences, and it does not rule out exact logarithmic sizes, exact residues with growing modulus, characters of growing conductor, prime identities, or other data whose precision/range grows with `X`. Those violate the fixed-`B`, fixed-`m` hypotheses and must be analyzed separately.

The squarefree restriction is intrinsic to the nonzero Möbius support used here. Unit factors must also be deleted before measuring active depth: arbitrary labeled `1`-slots would create coordinate padding rather than new arithmetic source information.

A proposed growing-depth factor lift now has a sharper first-kill test than the sign-only projection of `MC-425`: express the retained per-factor data as prime-local increments. If those increments are uniformly bounded and live in a fixed-dimensional additive space, the entire factorization channel has only `X^{o(1)}` states. A survivor must identify exactly which hypothesis it escapes and why that extra structure is canonical and cancellation-relevant.
