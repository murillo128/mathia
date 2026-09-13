# MC-261 — Blind shell generation is a logarithmic-smooth all-class representation problem

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the descended shell-radical setting of `MC-257`--`MC-260`. Let

\[
y=c\log X,
\qquad
R=\prod_{y<r\le 2y\atop r\ {m prime}}r,
\qquad
G=(\mathbb Z/R\mathbb Z)^\times,
\qquad
H=\langle p\bmod R:p\le y\text{ prime}\rangle.
\tag{1}
\]

The generation exit `H=G` from `MC-246` has an exact reformulation in the classical language of smooth representatives. Put

\[
\mathcal S(y)=\{n\ge1:P^+(n)\le y\}.
\tag{2}
\]

Because every prime divisor of `R` is larger than `y`, every `n\in\mathcal S(y)` is a reduced residue modulo `R`. Moreover,

\[
\boxed{
\{n\bmod R:n\in\mathcal S(y)\}=H.
}
\tag{3}
\]

Consequently

\[
\boxed{
H=G
\iff
\text{every reduced residue class modulo }R
\text{ contains a }y\text{-smooth integer}.
}
\tag{4}
\]

The shell is at the extreme logarithmic-smoothness endpoint. The prime number theorem gives

\[
\log R=\vartheta(2y)-\vartheta(y)=y+o(y),
\tag{5}
\]

so

\[
\boxed{y=(1+o(1))\log R.}
\tag{6}
\]

Thus the generation alternative left by `MC-246` is not merely a generic smooth-modulus problem. It asks whether primes only up to about `log R` generate the full reduced residue group modulo the very special squarefree shell modulus `R`.

A direct prior-art audit shows a genuine scale mismatch. Harper's theorem on smooth numbers in arithmetic progressions gives all-class asymptotic equidistribution for moduli `q<=z^A` in the fixed-`A` range `A<4 sqrt(e)`. Banks--Shparlinski extend the fixed-`A` statement to every fixed `A>0` for a large class of sufficiently smooth moduli satisfying, in particular,

\[
P^+(q)^{Q_A}<q\le z^A.
\tag{7}
\]

For the present `q=R` and smoothness cutoff `z=y`, the smooth-modulus condition is exceptionally favorable:

\[
P^+(R)\le2y,
\qquad
(2y)^{Q_A}<R
\tag{8}
\]

for every fixed `Q_A` once `y` is large. But the decisive size condition fails for every fixed `A`:

\[
R=\exp((1+o(1))y)\gg y^A.
\tag{9}
\]

Equivalently, forcing `R<=y^A` at the shell scale would require

\[
\boxed{
A\ge \frac{\log R}{\log y}
=(1+o(1))\frac{y}{\log y}\to\infty,
}
\tag{10}
\]

whereas the cited theorems are fixed-`A` results. Their smooth-modulus technology therefore cannot be extrapolated to `(4)` by choosing a large constant `A`.

The all-class product-of-primes literature has the same qualitative gap from the opposite direction. Matomäki--Teräväinen prove that for every sufficiently large cube-free modulus `q`, every reduced residue class is a product of three primes at most `q`; since `R` is squarefree, this gives a strong simultaneous generation theorem for `R`, but with prime generators at scale `R`, not `log R`. Their paper notes that the factor range can be reduced to `q^{1-\alpha}` for some fixed `\alpha>0` in the cube-free setting, still polynomial in `q`. For prime moduli, Munsch--Shparlinski prove all-class squarefree representatives whose prime factors are at most

\[
p^{1/(4\sqrt e)+o(1)},
\tag{11}
\]

again a fixed positive power of the modulus rather than logarithmic size.

Hence two different established languages -- equidistribution of smooth numbers and bounded products of primes -- currently reach **polynomial-size generators**, while the Mathia shell asks for **logarithmic-size generators**. This is an exponential scale gap in the generator cutoff.

The consequence for the active frontier is negative but useful: the `H=G` exit in `MC-246` should not be treated as a routine consequence of the fact that `R` is a very smooth modulus. Current smooth-number theorems exploit that smoothness only after the allowed prime-factor cutoff is at least a fixed power of the modulus (or an equivalent fixed-`A` regime). Closing `H=G` at `(6)` needs either a theorem genuinely specialized to the simultaneous shell structure, with strength far beyond the fixed-`A` smooth-representative theory, or a different mechanism. The alternative exit from `MC-259`--`MC-260` -- signed cancellation in the source-selected rough Möbius coset / its single surviving blind pretender -- remains logically separate.

No claim that `H\ne G` is made. The result classifies the exact representation problem and the scale at which current prior art stops.

## 1. The smooth-representative image is exactly `H`

Every `y`-smooth integer is a product of primes at most `y`, so its residue modulo `R` belongs to `H`. This proves one inclusion in `(3)`.

Conversely, an element of `H` is a finite product of integer powers of the residues of primes `p<=y`. Negative powers cause no problem. Since `G` is finite, if `o_R(p)` is the order of `p mod R`, then

\[
p^{-1}\equiv p^{o_R(p)-1}\pmod R.
\tag{12}
\]

Replacing every negative exponent by a nonnegative exponent modulo the corresponding order produces a positive integer with no prime factor larger than `y` representing the same element of `H`. Thus the multiplicative monoid generated by the small-prime residues is already the subgroup they generate, proving `(3)` and `(4)`.

This equivalence does not impose a useful size bound on the representing integer. Any theorem giving, for some finite `x`,

\[
\Psi(x,y;R,a)>0
\qquad\text{for every }a\in G
\tag{13}
\]

would prove `H=G`, but the group-theoretic equivalence itself only asks for existence somewhere in the infinite `y`-smooth semigroup.

## 2. Fixed-`A` smooth-number distribution misses the shell exponentially

Adam Harper, *On a paper of K. Soundararajan on smooth numbers in arithmetic progressions*, Journal of Number Theory **132** (2012), 182--199, DOI `10.1016/j.jnt.2011.07.005`, arXiv `1103.2106`, proves Soundararajan's conjectured equidistribution in the range `q<=z^A` for fixed `A<4 sqrt(e)`, with the additional `z` restrictions from the earlier result removed.

William Banks and Igor Shparlinski, *On a conjecture of Soundararajan*, Bulletin of the London Mathematical Society **54** (2022), 301--317, DOI `10.1112/blms.12524`, arXiv `2009.06800`, prove for every fixed `A>0` an all-class asymptotic when

\[
P^+(q)^{Q_A}<q\le z^A
\tag{14}
\]

for a constant `Q_A` depending on `A`, as `log x/log q -> infinity`. Their theorem is particularly relevant because the shell radical is itself extremely smooth.

But substituting `q=R` and `z=y` leaves `(14)` split in two very different ways. The first inequality holds overwhelmingly by `(5)` and `P^+(R)<=2y`; the second becomes the impossible fixed-`A` inequality `(9)`. The obstruction is therefore not failure of modulus smoothness. It is that the **allowed prime factors of the representing integers are too small relative to the modulus**.

Equation `(10)` is the exact scale ledger. Reaching `z=(1+o(1))log q` through a condition `q<=z^A` requires `A` to grow like `log q/log log q`. Fixed-`A` statements, no matter how large the chosen constant, do not approach this endpoint asymptotically. Their constants and exceptional-character analysis are not uniform data that can be silently promoted to such a growing-`A` theorem.

Recent average-distribution results for smooth numbers at large moduli do not change this all-class fixed-modulus conclusion automatically: an average over moduli or residue classes cannot certify `(13)` for the exact moving shell radical and every reduced class without an additional uniform argument.

## 3. Product-of-primes theorems confirm that the missing scale is the generator size

Kaisa Matomäki and Joni Teräväinen, *Products of primes in arithmetic progressions*, Journal für die reine und angewandte Mathematik **808** (2024), DOI `10.1515/crelle-2023-0096`, arXiv `2301.07679`, prove that for every sufficiently large cube-free `q`, every reduced residue class modulo `q` is a product of three primes `p_1,p_2,p_3<=q`. Their discussion also records that their method can yield `E_3(q^{1-\alpha})=G` for some fixed small `\alpha>0` in the cube-free case.

Since `R` is squarefree, this literature already proves a very strong simultaneous multiplicative covering statement for the same ambient group `G`. It therefore rules out the vague diagnosis that "simultaneous generation of every residue class is itself out of reach." The difficulty specific to `(4)` is the much shorter generating set:

\[
 p\le y=(1+o(1))\log R
\qquad\text{instead of}\qquad
 p\le R^{\delta}
\tag{15}
\]

for a fixed positive exponent `delta` (or `p<=R` in the clean published theorem).

A closer smooth-representative comparison exists already for prime moduli. Marc Munsch and Igor Shparlinski, *On smooth square-free numbers in arithmetic progressions*, Journal of the London Mathematical Society **101** (2020), 1041--1067, DOI `10.1112/jlms.12297`, arXiv `1710.04705`, prove that every class modulo a large prime `p` has a squarefree representative `s<=p^{2+o(1)}` all of whose prime factors are at most `p^{1/(4 sqrt(e))+o(1)}`. This is a genuine all-class smoothness theorem, but its prime-factor threshold remains polynomial in the modulus.

These comparisons are not used as lower bounds or impossibility theorems. They identify the prior-art scale that a proposed `H=G` proof must actually beat.

## 4. Relationship to the current blind-pretender frontier

`MC-248` showed that generic least-witness bounds of size `O((log q)^A)` with fixed `A>1` cannot close shell generation merely by forcing blind characters to have large support. The present finding attacks the complementary **simultaneous-generation** formulation rather than the least-witness formulation.

The two barriers are consistent but logically different:

- the least-witness route asks how early one can force a single nonprincipal character to differ from `1`;
- the smooth-representative route asks whether products of the entire small-prime set cover every residue class.

Classical smooth-number and product-set theorems are designed for the second question, but their generator cutoff is polynomial in the modulus. Thus replacing witness bounds by a black-box global equidistribution theorem does not currently close the gap exposed by `MC-248`.

This narrows the generation exit from `MC-246`: a useful next theorem cannot merely say that smooth numbers equidistribute for smooth moduli. It must exploit the special contiguous shell

\[
R=\prod_{y<r\le2y}r
\tag{16}
\]

strongly enough to push the generator threshold from a fixed power of `R` all the way down to `(1+o(1))log R`, or derive the same generation conclusion by another shell-specific simultaneous mechanism.

## 5. Prior-art and novelty assessment

The equality between a finite subgroup generated by residues and the image of the corresponding positive multiplicative semigroup is elementary group theory. Smooth numbers in arithmetic progressions, products of primes in arithmetic progressions, and smooth squarefree representatives are established literatures. **No novelty is claimed for those mechanisms or the cited theorems.**

The durable delta is the exact frontier dictionary and scale audit for the current Mathia shell: `H=G` is precisely an all-class `log R`-smooth representation problem, the shell modulus satisfies the strongest smoothness side of existing fixed-`A` theorems while violating their modulus-versus-smoothness side exponentially, and known simultaneous product-covering results operate at polynomial generator scale. This prevents the smoothness of `R` from being mistaken for an already available generation theorem.

A targeted search through September 2026 for smooth representatives, smooth-number distribution in arithmetic progressions, and products of small primes found no all-class theorem at a `P^+(n)=O(log q)` generator cutoff for this shell family. This is a prior-art boundary, not a proof that such a theorem is impossible.

## 6. Boundaries and falsification tests

- `H=G` is **not** disproved. The special shell radical may satisfy a much stronger generation theorem than generic moduli.
- Equation `(4)` allows arbitrarily large `y`-smooth representatives. The cited quantitative theorems are used only to audit known sufficient routes to all-class coverage.
- The Banks--Shparlinski theorem is a fixed-`A` statement. Letting `A` grow as in `(10)` without uniform control is outside its theorem.
- Average distribution over moduli cannot by itself establish coverage for the exact shell radical `R`; an exceptional-modulus issue must be eliminated rather than averaged away.
- Matomäki--Teräväinen and Munsch--Shparlinski use different modulus classes and quantitative targets. They are scale comparators, not theorems directly specialized to `(4)`.
- A theorem proving that primes up to `R^delta` generate `G` for any fixed `delta>0` still misses `(4)` by an exponential factor in the generator cutoff.
- Conversely, an all-class theorem for the exact shell with prime factors bounded by `C log R`, or any direct proof that the residues of primes `p<=y` generate `G`, would falsify the present route-level pessimism and close the generation exit immediately.
- Nothing here gives signed cancellation for the rough Möbius coset in `MC-259`; the surviving blind-pretender problem remains open.