# MC-508 — Fixed conductor phase leaves finite lower-prime first-exit mask coordinates programmable

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `MATCHED-ARITHMETIC-CONTROL`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`, `NON-RH`.

## Claim

`MC-506` reduces a varying-profile conductor bias to concentration of the physical sum coordinate `t=x+j`, while `MC-507` shows that abstract row/column marginals do not control that concentration. The surviving possibility is therefore genuinely source-coupled: the conductor start and the lower-prime hard-mask profile may fail to vary independently because both come from the same first-exit prime `q`.

The first natural version of that escape is nevertheless too weak. **At fixed conductor phase, every finite projection of the moving lower-prime hard mask is arithmetically programmable once tight localization of `q` is removed.**

Fix a prime conductor `p`, a nonzero shift `h` with `p\nmid h`, and a conductor residue

\[
a\in(\mathbb Z/p\mathbb Z)^\times.
\tag{1}
\]

Let `S` be any finite set of primes `\ell` satisfying

\[
\ell\ne p,
\qquad
\ell\nmid h,
\tag{2}
\]

and prescribe arbitrary nonzero residues

\[
\rho_\ell\in(\mathbb Z/\ell\mathbb Z)^\times
\qquad(\ell\in S).
\tag{3}
\]

Then there exist infinitely many primes `q`, larger than every prime in `S` and larger than any prescribed finite threshold, such that simultaneously

\[
\boxed{
q\equiv a\pmod p,
\qquad
-hq^{-1}\equiv\rho_\ell\pmod\ell
\quad(\ell\in S).
}
\tag{4}
\]

For the root `q\mid n`, these are exactly the two pieces of row data isolated in `MC-489`: the conductor character shift

\[
hq^{-1}\pmod p
\tag{5}
\]

is fixed by `(1)`, while at each lower active prime `\ell<q` the moving sieve root

\[
-hq^{-1}\pmod\ell
\tag{6}
\]

can be prescribed arbitrarily on the chosen finite set `S`.

Equivalently, for every fixed `a`, the map

\[
q
\longmapsto
\bigl(-hq^{-1}\bmod\ell\bigr)_{\ell\in S}
\tag{7}
\]

from primes `q\equiv a\pmod p` onto

\[
\prod_{\ell\in S}(\mathbb Z/\ell\mathbb Z)^\times
\tag{8}
\]

is surjective, with every fiber containing infinitely many primes, once no narrow size condition is imposed on `q`.

The same statement holds for the translated root `q\mid n+h`, with the corresponding sign convention for the moving lower-prime root.

This gives a precise matched-arithmetic obstruction to a tempting reading of the post-`MC-507` frontier:

\[
\boxed{
\text{fixed conductor phase}
+
\text{finitely many local first-exit mask coordinates}
\not\Rightarrow
\text{source/profile rigidity}.
}
\tag{9}
\]

Thus no argument can obtain the required anti-diagonal control merely from a bounded or fixed finite collection of congruence coordinates of the `q`-dependent hard mask. The load-bearing dependence, if it exists, must use information destroyed by `(4)`: the **full moving profile** over all lower primes `\ell<q`, the cutoff/order encoded by `q` itself, tight localization of `q` in its actual source range, the archimedean start/endpoints and reconstruction weights, or quantitative simultaneous distribution when the number of prescribed coordinates grows with the scale.

This does **not** show that the complete first-exit profile is arbitrary, does not place `q` in a dyadic or source-selected interval, does not control the anti-diagonal collision statistic of `MC-506`, and gives no estimate for `M(X)` or the zeta zero set.

## 1. CRT programs the finite mask projection while fixing conductor phase

For every `\ell\in S`, condition `(4)` is equivalent to

\[
q\equiv -h\rho_\ell^{-1}\pmod\ell.
\tag{10}
\]

Put

\[
M:=p\prod_{\ell\in S}\ell.
\tag{11}
\]

The moduli in `(11)` are pairwise coprime. The Chinese remainder theorem therefore gives a unique residue class

\[
A\pmod M
\tag{12}
\]

satisfying

\[
A\equiv a\pmod p,
\qquad
A\equiv-h\rho_\ell^{-1}\pmod\ell
\quad(\ell\in S).
\tag{13}
\]

Every component in `(13)` is nonzero: `a` is a unit modulo `p`, while `\ell\nmid h` and `\rho_\ell` is a unit modulo `\ell`. Hence

\[
(A,M)=1.
\tag{14}
\]

Dirichlet's theorem on primes in arithmetic progressions now supplies infinitely many primes

\[
q\equiv A\pmod M.
\tag{15}
\]

Choose one above `\max S` and above any additional finite exclusion threshold. Reducing `(15)` modulo `p` fixes the conductor residue `q\equiv a`; reducing modulo each `\ell\in S` gives `(10)`, hence the prescribed moving root `(4)`.

Nothing deeper is hidden in the proof. Its point is exactly that the finite local profile data left by the first-exit dilation are ordinary congruence coordinates of the same prime `q`, and CRT can decouple any fixed finite collection of them from the conductor coordinate.

## 2. What remains genuinely coupled after the finite projection is removed

The conclusion is intentionally finite-dimensional. In the actual first-exit row of `MC-489`, the sieve product is

\[
P(q)=\prod_{\substack{\ell<q\\ \ell\ \mathrm{active}}}\ell,
\tag{16}
\]

so the number of lower-prime mask coordinates grows with `q`. The construction above fixes only a finite set `S`; all other coordinates remain whatever the chosen prime supplies. Asking to prescribe the **entire** profile up to `q` would require a modulus whose logarithm grows with the source scale, and the qualitative Dirichlet argument gives no prime at a useful comparable height.

That distinction is the same kind of localization boundary already exposed elsewhere in the line: algebraic congruence programmability is cheap when the realizing prime may escape arbitrarily far, but it says nothing about realization inside the narrow moving range where the analytic estimate lives.

The physical source geometry also contains non-congruence data that `(4)` never touches. In the incomplete row sums, the starting points and lengths inherited from the original `n`-interval depend on `q` through quotients such as `X/q`; reconstruction coefficients and first-exit ownership depend on the exact source partition. These are plausible carriers of the start/profile dependence required by `MC-506`--`MC-507` precisely because they cannot be frozen or programmed by a fixed finite CRT prescription.

Therefore the post-`MC-507` search should not spend effort proving dependence from a bounded list of local mask residues. A viable theorem has to be genuinely **scale-growing or archimedean**.

## 3. Relation to the existing localization no-go results

This is not a new prescribed-residue theorem. Its closest local precedents are `MC-252` and `MC-256`.

`MC-252` proves that after removing tight shell localization, arbitrary finite binary matrices can be realized exactly as Legendre-symbol matrices by CRT, Dirichlet and quadratic reciprocity. Its durable lesson is that quadratic reciprocity plus primality does not force useful code rigidity unless the realizing primes are required to lie in the active moving shell.

`MC-256` extends the same exclusion to every fixed tame prime residue order via Kummer theory and Chebotarev: arbitrary finite residue-character matrices are again realizable when the prime columns may escape the active scale.

The present result specializes that principle to the **exact moving hard-mask coordinates of the current first-exit route**. No reciprocity law or auxiliary character family is needed: both the conductor phase and the lower-prime mask roots are direct congruence functions of `q`. The new research delta is therefore a frontier exclusion, not new number theory: `MC-507` leaves physical start/profile dependence as the live mechanism, and `(4)` shows that fixed finite local projections of that profile cannot supply it.

The only external ingredient beyond CRT is the classical existence of infinitely many primes in a reduced residue class. The line already records the standard fixed-modulus prime-in-progressions reference as `MC-S15` in `SOURCES.md`; no stronger quantitative distribution theorem is invoked.

## 4. Falsification checks and boundaries

- **Prime-divisor-of-h boundary.** If `\ell\mid h`, the two local sieve roots in `MC-489` coalesce and the moving root is `0`; arbitrary nonzero prescription is false there. This is why `(2)` excludes those primes.
- **Conductor boundary.** The conductor coordinate is meaningful only for `q\not\equiv0\pmod p`; `(1)` fixes a unit class and therefore avoids `q=p`.
- **Lower-prime boundary.** The theorem chooses `q>\max S`, so every prescribed `\ell` genuinely lies in the lower-prime profile of the resulting row. It does not prescribe every lower prime below `q`.
- **Localization boundary.** Dirichlet's theorem is qualitative. No claim is made that a realizing `q` lies in `[Q,2Q]`, in a first-exit source block, or even within a polynomial factor of the CRT modulus.
- **Growing-coordinate boundary.** The theorem is for fixed finite `S`. If `|S|` grows with the analytic scale, the modulus in `(11)` grows too, and the required quantitative prime-distribution problem is exactly what this argument does not solve.
- **Archimedean boundary.** The source start, interval length, quotient fibers, and reconstruction weights are not congruence coordinates and are not matched by this control.
- **Collision boundary.** Surjectivity of finite mask projections neither proves nor disproves concentration of the physical sum coordinate `t=x+j` from `MC-506`; it only removes one proposed source of rigidity.
- **RH boundary.** No zero-free region, reciprocal-zeta continuation, improved Mertens estimate, or RH-scale cancellation is used or obtained.

## Updated frontier

`MC-506` identifies excess anti-diagonal collisions as the exact currency of a varying-profile conductor bias. `MC-507` then rules out abstract marginal control. The remaining source-coupling question can now be narrowed once more:

\[
\boxed{
\text{the useful dependence, if any, must survive arbitrary finite local mask reprogramming.}
}
\tag{17}
\]

A decisive next test is therefore to keep the **actual localized prime `q` and its entire growing first-exit profile** and ask whether the induced physical start/profile pushforward has subcritical anti-diagonal collision excess. Equivalently, one should seek a theorem that fails for the nonlocalized CRT controls above because it uses the moving cutoff, the full nested lower-prime mask, or the archimedean quotient geometry. Another theorem about finitely many local congruence coordinates cannot cross the present frontier.
