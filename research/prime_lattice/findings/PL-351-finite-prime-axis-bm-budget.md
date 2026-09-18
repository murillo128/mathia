# PL-351 — Finite prime-axis sources have an exact BM budget, and natural energy cutoffs must grow only logarithmically to avoid form-core collapse

**Evidence:** `EXACT-DERIVED + CLASSICAL-BM + CLASSICAL-PNT + DECISIVE-BOUNDARY`

**Status:** `FINITE-UNION-OF-PRIME-AXES-HAS-ADDITIVE-FINITE-BM-DENSITY + CROSS-DIRECTION-GEOMETRY-NEED-NOT-COLLAPSE-WITHOUT-MULTIPLICATIVE-CLOSURE + LINEAR-ENERGY-CUTOFFS-STILL-BECOME-FORM-CORES`

## Precise claim

`PL-350` showed that multiplicative closure is fatal to the finite-Beurling--Malliavin escape of `PL-349`: once a multiplicatively closed source retains two independent exponent directions, the energy projection produces quadratically many distinct log frequencies and the source becomes a form core on every finite aperture. That leaves an important structural question: does merely retaining several genuine prime directions already force the same collapse, or was cross-direction multiplication the decisive step?

For a finite set of distinct primes `P`, retain each coordinate ray but no mixed exponent vectors:

\[
\Lambda_P^{\rm axes}
:=\bigcup_{p\in P}\{k\log p:k\in\mathbb N_0\}.
\tag{PL351-1}
\]

This is exactly the energy image of the union of exponent-coordinate rays `\{k e_p:k\ge0\}`. Then

\[
\boxed{
D_{BM}^*(\Lambda_P^{\rm axes})
=\sum_{p\in P}\frac1{\log p}.
}
\tag{PL351-2}
\]

Consequently, by the completeness-radius/form-core theorem of `PL-349`,

\[
\boxed{
A_{\rm core}(P)
=\pi\sum_{p\in P}\frac1{\log p}.
}
\tag{PL351-3}
\]

As in `PL-349`, this is a supremal aperture statement; no assertion is made about completeness exactly at the critical aperture.

Thus **multiple independent prime directions do not by themselves force infinite BM density**. The collapse in `PL-350` is caused specifically by allowing cross-direction additive closure in exponent space, equivalently multiplication of integers drawn from different rays.

There is nevertheless a second collapse for the most natural growing axis selection. Let

\[
P_B:=\{p:\log p\le B\}=\{p:p\le e^B\}.
\tag{PL351-4}
\]

The prime number theorem gives

\[
D(B):=\sum_{p\in P_B}\frac1{\log p}
\sim \frac{e^B}{B^2},
\qquad B\to\infty,
\tag{PL351-5}
\]

and therefore

\[
A_{\rm core}(B)
\sim \pi\frac{e^B}{B^2}.
\tag{PL351-6}
\]

Hence any prime-energy window growing linearly with the physical aperture, for example `B(A)=cA` with fixed `c>0`, becomes overwhelmingly complete:

\[
\frac{A_{\rm core}(B(A))}{A}\longrightarrow\infty.
\tag{PL351-7}
\]

To avoid automatic form-core collapse at aperture `A`, a source of this particular axis-cutoff type must stay at or below the logarithmic scale

\[
B(A)\lesssim \log A+2\log\log A+O(1).
\tag{PL351-8}
\]

The balance `A_{\rm core}(B)\asymp A` occurs more precisely at

\[
B=\log A+2\log\log A-\log\pi+o(1).
\tag{PL351-9}
\]

This produces a concrete source-selection boundary after `PL-349`/`PL-350`: a finite collection of unmixed prime axes is genuinely multi-directional and has finite BM budget, but allowing the prime-energy cutoff to track aperture at any linear rate already restores full local Weil information.

## 1. Exact BM density of finitely many prime axes

For distinct primes `p\ne q`, the positive rays in (PL351-1) do not intersect. Indeed,

\[
k\log p=\ell\log q
\]

with positive integers `k,\ell` would imply `p^k=q^\ell`, impossible by unique factorization. The only common point is the origin.

Put

\[
D(P):=\sum_{p\in P}\frac1{\log p}.
\tag{PL351-10}
\]

For every interval `I=(x,y]\subset[0,\infty)`, each ray contributes

\[
\#\bigl((\log p)\mathbb N_0\cap I\bigr)
=\frac{|I|}{\log p}+O(1),
\]

with an absolute `O(1)` independent of `x,y`. Summing over the fixed finite set `P` gives the uniform discrepancy estimate

\[
\boxed{
\#(\Lambda_P^{\rm axes}\cap I)
=D(P)|I|+O(|P|).
}
\tag{PL351-11}
\]

In particular the ordinary asymptotic density is `D(P)`, so the exterior/effective BM density cannot be smaller than `D(P)`. Conversely, (PL351-11) gives upper uniform density `D(P)`: for every `epsilon>0`, an interval on which the local density exceeds `D(P)+epsilon` must have length `O_P(1/epsilon)`. Such uniformly bounded intervals cannot form a BM-long family, because for pairwise disjoint intervals `I_j` of bounded length,

\[
\sum_j\frac{|I_j|^2}{1+\operatorname{dist}(0,I_j)^2}<\infty.
\]

Therefore the long-interval definition of exterior BM density cannot exceed `D(P)`. This proves (PL351-2). Equivalently, one may sandwich the BM density between the asymptotic density and the upper uniform density, which coincide here because of the bounded-discrepancy estimate.

The analytic input after this counting lemma is entirely classical. Source 104 and `PL-349` give

\[
R_2(\Lambda)=2\pi D_{BM}^*(\Lambda),
\qquad
A_{\rm core}(\Lambda)=\pi D_{BM}^*(\Lambda),
\]

so (PL351-3) follows immediately.

This distinction from `PL-350` is structural. The union of axes retains arbitrarily high powers along each selected prime coordinate, but it deliberately excludes mixed vectors such as `k e_p+\ell e_q`. Those mixed vectors were exactly what produced the two-dimensional triangular count `\gg R^2` in `PL-350`. Without them, the energy projection is only a finite union of one-dimensional half-lattices and its frequency budget remains linear.

## 2. Prime-energy truncation has exponentially growing BM budget

Now choose the finite axis set canonically by the same energy used throughout the Prime-Lattice representation:

\[
P_B=\{p:\log p\le B\}.
\]

Then (PL351-2) becomes

\[
D(B)=\sum_{p\le e^B}\frac1{\log p}.
\tag{PL351-12}
\]

Writing `x=e^B` and applying partial summation to the prime number theorem `\pi(x)\sim x/\log x`,

\[
\sum_{p\le x}\frac1{\log p}
=
\frac{\pi(x)}{\log x}
+
\int_2^x\frac{\pi(t)}{t(\log t)^2}\,dt
\sim \frac{x}{(\log x)^2}.
\tag{PL351-13}
\]

The integral is lower order, of size `O(x/(\log x)^3)` at the asymptotic level supplied by the prime number theorem. Substituting `x=e^B` proves (PL351-5), and `PL-349` gives (PL351-6).

This growth is much faster than the aperture itself under any linear energy schedule. If `B(A)=cA`, then

\[
A_{\rm core}(B(A))
\sim \pi\frac{e^{cA}}{c^2A^2},
\]

which proves (PL351-7). Solving the transition relation

\[
\pi\frac{e^B}{B^2}\asymp A
\]

for `B` gives the logarithmic scale (PL351-8), with the asymptotic equality (PL351-9). Thus a natural energy cutoff on prime coordinates can remain genuinely incomplete at growing aperture only if the coordinate budget grows extremely slowly compared with the physical/logarithmic window being tested.

## 3. Prior-art and novelty audit

The mathematical ingredients are classical. The exact conversion from BM density to completeness/form-core aperture is source 104 through `PL-349`; the density computation for a finite union of prime rays is an elementary bounded-discrepancy count; and (PL351-5) is a routine consequence of the prime number theorem by partial summation.

A targeted literature audit on 18 September 2026 searched for Beurling--Malliavin density/completeness results specifically for prime logarithms, prime powers, finite unions of logarithmic prime-power rays, and the corresponding completeness radius. It located general literature relating BM density to asymptotic density but did not locate this exact Prime-Lattice axis-selection statement or the aperture-versus-prime-energy threshold above. That absence is **not** treated as evidence of novelty. The durable contribution is the route boundary relative to `PL-350`: cross-direction multiplicative closure, not multidirectionality alone, is what forces immediate infinite-BM collapse; however, the canonical growing energy cutoff still collapses unless it is logarithmically sparse in the aperture.

Nothing here is a new RH criterion. The calculation uses no zeta zeros, functional equation, or continuation. Its relevance is solely to constrain which source-selected modulation families can plausibly remain intermediate coordinates for the completed Weil form rather than silently reconstructing the full criterion.

## 4. Adversarial boundaries

1. **Finite `P` is not a zeta source by itself.** It omits infinitely many prime coordinates and cannot recover the full explicit-formula prime source without an additional limiting or coupling theorem.

2. **The result concerns the union of coordinate rays, not their multiplicative closure.** Adding mixed exponent vectors immediately returns to the rank-at-least-two obstruction of `PL-350` and infinite BM density.

3. **The all-prime union is already terminal.** Taking every prime at once contains the prime-log set `\{\log p\}`, which `PL-348`/`PL-349` already showed has infinite completeness radius. The useful regime is necessarily aperture-dependent or otherwise thinned.

4. **A cutoff schedule is not a mechanism.** Choosing `B(A)` by hand below the threshold only prevents automatic form-core collapse. To become RH-relevant, the schedule must be forced by arithmetic or operator structure and must control the missing directions by something stronger than density.

5. **Weights do not rescue frequency completeness.** Prime coefficients such as `\log p`, von Mangoldt weights, or other nonzero scalar weights on the same modulation support do not change the unconstrained linear span. A viable weighted proposal must impose coefficient relations or another nontrivial coupling, not merely rescale basis vectors.

6. **No statement is made at the BM critical aperture.** As in `PL-349`, only strict inside/outside completeness and the supremal core radius are asserted.

7. **No arithmetic selectivity follows from BM density itself.** The exact density formula is explained by a finite union of uniformly distributed half-lattices. A generic set with the same frequency geometry has the same completeness behavior; rational-prime specificity enters only through the source-derived spacings `\log p` and the PNT growth of the number of available axes.

## Research consequence

The intermediate-sufficiency route now has a sharper source-selection map. Requiring genuine multidirectionality is compatible with finite BM density provided cross-direction multiplication is withheld: finitely many complete prime coordinate rays give the exact finite budget (PL351-2). This is the first non-rank-one multi-direction family left open by the `PL-350` obstruction.

However, the most canonical way to enlarge that family, by admitting every prime coordinate with `\log p\le B`, has BM budget `\asymp e^B/B^2`. If the cutoff follows the aperture at any linear scale, the family rapidly becomes a form core and restricted Gram positivity again degenerates to full Weil positivity in redundant coordinates. A genuinely intermediate growing prime-axis proposal must therefore either derive a roughly logarithmic-in-aperture coordinate cutoff from the arithmetic source, impose cross-axis coefficient/coupling laws that survive unrestricted span, or leave the frequency-only endpoint-modulation framework.