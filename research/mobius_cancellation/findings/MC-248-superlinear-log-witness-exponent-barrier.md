# MC-248 — Superlinear log-conductor witness bounds cannot close blind shell generation

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the shell-square blind-character setting of `MC-238`--`MC-247`. Let

\[
S\subset\{r\text{ prime}:y<r\le 2y\},
\qquad n=|S|\asymp \frac{y}{\log y},
\]

and let a nonprincipal blind character have active shell support `T(χ)` of size `k`. By `MC-239`, after deleting principal local components its active conductor is

\[
q_\chi=\prod_{r\in T(\chi)}r,
\qquad
\log q_\chi\le k\log(2y).
\tag{1}
\]

Every prime `p\le y` lies in `ker χ`. Thus any theorem of the following generic least-witness form

\[
\boxed{
\text{every proper subgroup }K<(\mathbb Z/m\mathbb Z)^\times
\text{ has a prime }\ell\nmid m,\ \ell\notin K,
\ \ell\le C(\log m)^A
}
\tag{2}
\]

with fixed `C>0` and `A\ge1`, forces

\[
\boxed{
 k
 >
 C^{-1/A}\frac{y^{1/A}}{\log(2y)}.
}
\tag{3}
\]

For every fixed `A>1`, this support floor is parametrically smaller than the shell dimension:

\[
\frac{k}{n}\gg y^{1/A-1}=o(1).
\tag{4}
\]

Consequently **no improvement that stays within a generic `O((log m)^A)` witness theorem with exponent `A>1` can close the small-prime generation gate `H=G` merely by excluding low-support blind characters**. Constants and lower-order logarithms can strengthen the floor but cannot remove the power deficit.

The same obstruction is exact for the quadratic blind code. If a witness theorem of exponent `A>1` yields minimum distance

\[
d\gg \frac{y^{1/A}}{\log y}
\tag{5}
\]

for a binary kernel of length `n\asymp y/\log y`, then abstract binary linear codes exist with that minimum-distance scale and parity-check rank only

\[
\boxed{
r=O\!\left(d\log\frac nd\right)=O(y^{1/A})=o(n).
}
\tag{6}
\]

Thus minimum support at the scale supplied by any fixed `A>1` is compatible with a kernel of dimension `n-o(n)`. The information type itself is insufficient to force full rank.

`MC-247` is exactly the `A=2` instance, obtained from the ERH/GRH small-subgroup-witness theorem. Modern GRH improvements to the constant in front of `(log q)^2` do not change this conclusion.

The first generic witness scale that even reaches **linear shell support** is `O(log m)`. Even that does not by itself force triviality: a constant-fraction minimum distance is compatible with nonzero linear codes, and the constant in the witness theorem would still matter. Moreover, a generic uniform `O(log m)` theorem across all moduli is impossible already in the quadratic prime-modulus subfamily: Graham--Ringrose proved that the least quadratic nonresidue is infinitely often `\gg \log p\,\log\log\log p`.

Hence the `H=G` exit of `MC-246` cannot plausibly be completed by successively sharpening a **generic** least-witness theorem. A successful generation proof must use special simultaneous arithmetic of the moving shell family, while the alternative exit remains direct signed cancellation in the source-selected rough Möbius coset.

No RH/GRH consequence is proved here. Equation `(3)` is a deterministic implication from the hypothetical witness bound `(2)`; the GRH literature supplies the important `A=2` example.

## 1. Blindness converts any generic witness theorem into a support floor

Let

\[
K_\chi=\ker\chi_T<(\mathbb Z/q_\chi\mathbb Z)^\times.
\]

Because `χ` is blind to every small-prime generator,

\[
\chi_T(p)=1
\qquad(p\le y\text{ prime}).
\tag{7}
\]

All conductor primes of `q_χ` lie in `(y,2y]`, so every prime `p\le y` is a reduced residue modulo `q_χ`. Therefore the least prime outside `K_χ` is strictly larger than `y`.

Applying `(2)` to `K_χ` gives

\[
y<C(\log q_\chi)^A.
\tag{8}
\]

Using `(1)`,

\[
y<Ck^A\log^A(2y),
\]

which is exactly `(3)`.

If `A>1` and `n\asymp y/\log y`, then

\[
\frac{y^{1/A}/\log y}{y/\log y}
=y^{1/A-1}\to0,
\]

proving `(4)`. This is independent of the constant `C`.

The same calculation also locates the scale transition. A hypothetical bound

\[
W(m)\ll \log m\,L(\log m)
\tag{9}
\]

with an unbounded slowly varying factor `L` yields at best a support floor smaller than shell size by the corresponding factor. For example, a bound of the often-conjectured quadratic-nonresidue shape

\[
W(m)\ll \log m\,\log\log m
\tag{10}
\]

would give only

\[
k\gg \frac{y}{\log^2 y}
=o\!\left(\frac y{\log y}\right)
\tag{11}
\]

when used solely through this support argument. Equation `(10)` is used here only as a scale comparison; no such uniform theorem for the present shell subgroups is assumed.

## 2. Minimum-distance information at this scale cannot force quadratic full rank

The insufficiency in `(4)` is not merely a weakness of the Hamming lower bound used in `MC-247`. There are abstract binary linear kernels showing that the same information type is compatible with very low parity-check rank.

Fix length `n` and target minimum distance `d=o(n)`. Choose an `r\times n` binary matrix `B` uniformly at random. For any fixed nonzero vector `v`,

\[
\Pr(Bv=0)=2^{-r}.
\]

Hence the expected number of nonzero kernel vectors of weight below `d` is

\[
2^{-r}\sum_{j=1}^{d-1}\binom nj.
\tag{12}
\]

Taking

\[
r>
\log_2\!\left(\sum_{j=1}^{d-1}\binom nj\right)
\tag{13}
\]

makes this expectation smaller than one, so some matrix `B` has no such kernel vector. Therefore there exists a binary linear code with minimum distance at least `d` and parity-check rank at most

\[
r
=O\!\left(d\log\frac nd\right).
\tag{14}
\]

For the witness-induced scale `(5)`,

\[
\frac nd\asymp y^{1-1/A},
\]

up to constants, and therefore

\[
d\log(n/d)
=O(y^{1/A}),
\]

which proves `(6)`.

This gives an exact matched coding control: for every fixed `A>1`, a support theorem of the form supplied by `(2)` is compatible with rank `o(n)`, not merely rank less than `n`. Any route from blind-character support to full Legendre rank must therefore add arithmetic constraints on the shell columns or simultaneous relations that generic coding theory does not see.

## 3. The GRH literature improves constants but remains on the same exponent side of the barrier

Eric Bach's 1990 ERH theorem, used in `MC-247`, gives the classical `(log q)^2` subgroup-witness scale. Lamzouri, Li and Soundararajan subsequently sharpened this under GRH for a general proper subgroup `H<(\mathbb Z/q\mathbb Z)^\times`. Their Theorems 1.1--1.3 keep the least prime outside `H` at

\[
(\alpha([G:H])+o(1))(\log q)^2
\]

with improved constants, reaching `1/4+o(1)+O(1/\log [G:H])` for large index. These are real improvements to the generic witness theorem, but in `(3)` they alter only the constant in a `\sqrt y/\log y` support floor.

Recent Fourier-optimization work continues to improve GRH constants for least nonresidues while retaining the quadratic `\log^2 q` exponent. This confirms that the gap isolated here is not a missed constant optimization: the shell needs a change in information scale or shell-specific simultaneous structure.

The relevant primary references are:

- Eric Bach, *Explicit Bounds for Primality Testing and Related Problems*, Mathematics of Computation **55** (1990), 355--380, DOI `10.2307/2008811`.
- Youness Lamzouri, Xiannan Li and Kannan Soundararajan, *Conditional bounds for the least quadratic non-residue and related problems*, Mathematics of Computation **84** (2015), 2391--2412, DOI `10.1090/S0025-5718-2015-02925-1`, arXiv `1309.3595`.

## 4. Generic linear-log witnesses are themselves blocked by classical lower bounds

The calculation above says that `A=1` is the first pure power of `log m` that is not automatically `o(n)` after translation to shell support. It does **not** say an `O(log m)` witness theorem would automatically prove `H=G`; constants and simultaneous structure would remain.

More importantly, such a bound cannot hold uniformly for generic proper subgroups. In the special case of the quadratic-residue subgroup modulo a prime `p`, S. W. Graham and C. J. Ringrose proved that the least quadratic nonresidue is, for infinitely many primes,

\[
\gg \log p\,\log\log\log p.
\tag{15}
\]

Thus even the broad class of quadratic subgroups forbids a universal `O(log p)` witness bound. The source is:

- S. W. Graham and C. J. Ringrose, *Lower Bounds for Least Quadratic Non-Residues*, in *Analytic Number Theory*, Progress in Mathematics **85** (1990), 269--309, DOI `10.1007/978-1-4612-3464-7_18`.

This lower bound is not asserted for the special shell conductors `q_χ`. Its role is adversarial: it rules out the hope that a sufficiently strong **generic all-moduli** witness theorem will eventually supply the missing generation argument. Any improvement beyond the exponent barrier must use structure special to these shell moduli/subgroups.

## 5. Prior-art and novelty audit

Least character nonresidues, least primes outside multiplicative subgroups, GRH `(log q)^2` witnesses, and the coding-theoretic probabilistic construction are classical mechanisms. No novelty is claimed for them.

The durable mathematical delta is a frontier classification internal to the Mathia shell route: combining the exact blind-support/conductor dictionary of `MC-239`--`MC-247` with a symbolic witness exponent shows that **every fixed superlinear log-conductor exponent `A>1` remains parametrically incapable of closing shell generation through support or minimum-distance information alone**. The random parity-check construction verifies that this is an information-type obstruction, not merely a loose use of the Hamming bound.

This sharpens the route-selection consequence of `MC-247`: improving Bach/GRH constants, or even replacing `log^2 q` by `log^{1+\delta}q` for fixed `\delta>0`, cannot close the shell by the same mechanism. The next mathematical step must instead attack simultaneous shell generation directly or the signed rough-coset amplitude from `MC-246`.

## 6. Boundaries and falsification tests

- Equation `(2)` is a schematic hypothesis used to classify witness exponents. Only specific instances supported by literature may be treated as theorems.
- The GRH/ERH `A=2` application remains conditional and is already isolated in `MC-247`; this finding does not strengthen it arithmetically.
- The coding construction is an abstract matched control. It proves insufficiency of minimum-distance information alone, not the existence of an arithmetic blind code with those parameters.
- The Graham--Ringrose lower bound concerns quadratic characters modulo primes. It blocks a generic all-moduli `O(log q)` theorem but does not rule out stronger witness bounds specialized to the moving shell conductor family.
- Linear-scale minimum distance does not imply a zero-dimensional kernel. Reaching `A=1` would remove the present power deficit, not finish the generation proof.
- None of these witness bounds controls the signed rough Möbius coset in `MC-246`; that remains a logically separate exit.
- No contour shift, reciprocal-`L` continuation, or zero-free region is used in `(1)`--`(14)`.