# MC-249 — Brun–Titchmarsh shell occupancy squeezes the blind quotient torsion spectrum

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the shell-square smooth-dilation setting of `MC-238`–`MC-248`. Write

\[
G=(\mathbb Z/Q_S\mathbb Z)^\times,
\qquad
H=H_y(Q_S)=\langle p\bmod Q_S:p\le y\text{ prime}\rangle,
\qquad
\mathcal Q:=G/H.
\tag{1}
\]

By `MC-239`, the square-lift kernel already lies in `H`, every local shell projection is onto for sufficiently large `y`, and every blind character factors through

\[
\prod_{r\in S}(\mathbb Z/r\mathbb Z)^\times,
\qquad y<r\le2y.
\tag{2}
\]

The support lower bounds of `MC-242`, `MC-247`, and the generic witness calculation of `MC-248` can therefore be combined with a second piece of information that those findings did not use: a character of a prescribed prime-power order can live only on shell primes in one arithmetic progression.

Let

\[
d=\ell^a
\]

be any prime power dividing the exponent `exp(mathcal Q)`. Then, for all sufficiently large `y`,

\[
\boxed{
L_y
\le
\#\{r\in S:r\equiv1\pmod d\}
\le
\pi(2y;d,1)-\pi(y;d,1),
}
\tag{3}
\]

where `L_y` is **any valid lower bound for the active support of a nonprincipal blind character** at this shell scale.

Using the explicit arbitrary-interval Brun–Titchmarsh bound

\[
\pi(2y;d,1)-\pi(y;d,1)
<
\frac{2y}{\varphi(d)\{\log(y/d)+0.8601\}}
\qquad(d<y),
\tag{4}
\]

and `phi(ell^a)>=d/2`, one obtains the uniform occupancy inequality

\[
\boxed{
L_y
<
\frac{4z}{\log z+0.8601},
\qquad z:=\frac yd.
}
\tag{5}
\]

for every prime-power divisor `d` of `exp(mathcal Q)` once `y` is large. This converts support information into **torsion-order information**.

### Unconditional consequence

`MC-242` gives

\[
L_y
=
\left(\frac1{\log2}-o(1)\right)\log\log y.
\tag{6}
\]

Inverting `(5)` gives

\[
\boxed{
\ell^a
\le
(4\log2+o(1))
\frac{y}{\log\log y\,\log\log\log y}
}
\tag{7}
\]

for **every** prime power `ell^a | exp(mathcal Q)`. In particular the largest prime divisor satisfies the sharper prime-modulus form

\[
\boxed{
P^+(|\mathcal Q|)
\le
(2\log2+o(1))
\frac{y}{\log\log y\,\log\log\log y}.
}
\tag{8}
\]

Thus the unconditional double-log support theorem does more than rule out sparse blind characters: it forces every surviving cross-shell quotient relation into progressively lower-order torsion. This strengthens the elementary `ell<=y/2` exclusion in `MC-239` by a diverging factor.

### ERH consequence

Under the ERH hypothesis used in `MC-247`,

\[
L_y
=
\left(\frac1{\sqrt2}-o(1)\right)
\frac{\sqrt y}{\log y}.
\tag{9}
\]

Equation `(5)` then yields

\[
\boxed{
\ell^a
\le
(8\sqrt2+o(1))\sqrt y
}
\tag{10}
\]

for every prime power dividing `exp(mathcal Q)`, and the prime-divisor version improves to

\[
\boxed{
P^+(|\mathcal Q|)
\le
(4\sqrt2+o(1))\sqrt y.
}
\tag{11}
\]

So the generic ERH least-witness theorem still does not prove `H=G`, as `MC-247`–`MC-248` already showed, but after shell occupancy is imposed it does force the entire blind quotient to have only square-root-scale prime-power torsion.

More generally, if a witness theorem of the schematic `MC-248` form

\[
W(m)\le C(\log m)^A,
\qquad A>1,
\tag{12}
\]

is available, then `(3)`–`(5)` sharpen its support-only consequence to

\[
\boxed{
\ell^a
\le
(4A C^{1/A}+o(1))\,y^{1-1/A}
}
\tag{13}
\]

for every prime-power divisor of the quotient exponent; for prime divisors the leading factor `4A` becomes `2A`. At the formally critical scale `A=1`, the same calculation would force the quotient exponent to be bounded in terms of `C` rather than merely forcing linear support.

This does **not** prove `mathcal Q=1`. Bounded or very smooth exponent is not bounded quotient size: an elementary abelian group `(Z/2Z)^m` has exponent `2` and arbitrarily large rank. The live generation problem therefore changes shape but does not disappear. After `(7)`, the surviving obstruction is concentrated in many-coordinate relations of comparatively low order; after a hypothetical linear-log shell witness theorem it would reduce to finitely many bounded-order torsion ranks.

No estimate for the rough Möbius coset of `MC-246`, no proof of `H=G`, and no consequence for `M(X)` or the zeta zero set is proved here.

## 1. Prime-power torsion produces a blind order-`ell` character on an `r=1 mod ell^a` sub-shell

Finite abelian duality identifies the annihilator

\[
A=H^\perp
\]

with the character group of `mathcal Q`; in particular `A` and `mathcal Q` have the same exponent. If `d=ell^a` divides that exponent, choose

\[
\eta\in A
\]

of exact order `ell^a` and put

\[
\chi:=\eta^{\ell^{a-1}}.
\tag{14}
\]

Then `chi` is a nonprincipal blind character of exact order `ell`.

By `MC-239`, `eta` factors through the squarefree shell radical, so write

\[
\eta=\prod_{r\in S}\eta_r,
\qquad
\eta_r\in\widehat{(\mathbb Z/r\mathbb Z)^\times}.
\tag{15}
\]

If the local `ell`-primary order of `eta_r` is `ell^{b_r}`, then `0<=b_r<=a`, and the local component of `(14)` is nonprincipal exactly when `b_r=a`. Every such coordinate satisfies

\[
\ell^a\mid r-1,
\tag{16}
\]

because `(Z/rZ)^*` has order `r-1`. Hence

\[
\operatorname{supp}(\chi)
\subseteq
\{r\in S:r\equiv1\pmod{\ell^a}\}.
\tag{17}
\]

Any lower bound `L_y` valid for the support of nonprincipal blind characters therefore implies `(3)`.

This prime-power reduction is stronger than applying the argument only to prime divisors of `|mathcal Q|`: it constrains the **exponent** of every primary component. Raising `eta` in `(14)` deliberately deletes all local coordinates whose `ell`-power order is below the maximal `ell^a` level, so the remaining support really lies on the thinner progression `(16)`.

## 2. Brun–Titchmarsh converts shell occupancy into an order cutoff

Tomohiro Yamada's explicit arbitrary-interval Brun–Titchmarsh theorem gives, for coprime positive integers `k,a` and interval length `Y>k`,

\[
\pi(x+Y;k,a)-\pi(x;k,a)
<
\frac{2Y}{\varphi(k)\{\log(Y/k)+0.8601\}}.
\tag{18}
\]

Apply `(18)` with `x=Y=y`, `k=d`, and `a=1`. Since the support lower bounds used here tend to infinity, `(3)` first implies `d<y` for all sufficiently large `y`; otherwise the interval `(y,2y]` contains at most one integer congruent to `1 mod d`. Thus `(18)` applies.

For a prime power `d=ell^a`,

\[
\varphi(d)=d(1-1/\ell)\ge d/2.
\tag{19}
\]

Writing `z=y/d` gives `(5)`. Since the right side of `(5)` must tend to infinity in both `(6)` and `(9)`, one also has `z->infinity`, so the elementary inversion of `z/log z` is legitimate.

For prime `d=ell->infinity`, `(19)` improves to `phi(ell)/ell=1+o(1)`, replacing the factor `4` in `(5)` by `2+o(1)`. This gives the sharper prime-divisor constants in `(8)` and `(11)`.

## 3. Inverting the occupancy inequality

Put

\[
L=\log\log y,
\qquad
L_2=\log\log\log y.
\]

Under `(6)`, equation `(5)` requires

\[
\frac{4z}{\log z}
\ge
\left(\frac1{\log2}-o(1)\right)L.
\tag{20}
\]

The function `z/log z` is increasing for `z>e`. Evaluating `(20)` at `z=cLL_2` and using

\[
\log(cLL_2)=(1+o(1))L_2
\]

shows that necessarily

\[
z
\ge
\left(\frac1{4\log2}-o(1)\right)LL_2,
\tag{21}
\]

which is `(7)`. Repeating the same calculation with the prime-modulus coefficient `2+o(1)` gives `(8)`.

Under ERH, combine `(5)` and `(9).` At `z=c\sqrt y`,

\[
\log z=(\tfrac12+o(1))\log y,
\]

so

\[
\frac{4z}{\log z}
=
(8c+o(1))\frac{\sqrt y}{\log y}.
\]

Comparison with `(9)` forces `c>=1/(8sqrt2)+o(1)`, proving `(10)`; the prime-modulus coefficient gives `(11)`.

The same inversion with the `MC-248` support floor

\[
L_y>C^{-1/A}\frac{y^{1/A}}{\log(2y)}
\]

gives `(13)` because `log(y^{1/A})=(1/A)log y`.

## 4. What this changes — and what it does not

`MC-248` proved that a generic witness exponent `A>1` cannot close shell generation if its only use is to force a minimum support: abstract codes can have that minimum distance and still retain a huge kernel. The present finding shows that the same support theorem has a second, genuinely shell-specific consequence because the local factor orders are `r-1` and the shell primes occupy only a Brun–Titchmarsh-sized progression slice.

The information hierarchy is therefore now:

- **support:** every blind relation must involve many shell coordinates;
- **torsion order:** every prime-power order surviving in the quotient must occur in at least that many values of `r-1`, forcing `(7)` or `(10)`;
- **rank/index:** still uncontrolled by those two facts alone;
- **source amplitude:** the rough Möbius coset of `MC-246` remains completely separate.

This prevents two opposite mistakes. One should not dismiss the witness route as giving *only* minimum distance: after shell occupancy it also squeezes the quotient's torsion spectrum. But one should not mistake a smooth or even bounded exponent for generation: high-rank low-order quotients remain algebraically possible, with the quadratic blind code as the first concrete example.

A sharper next target on the generation side is therefore no longer a generic least-witness constant. It is control of the **low-order simultaneous character ranks** left after `(7)`: for fixed or moderately growing `ell^a`, determine whether the vectors of local `ell^a`-power residue characters across the shell can have a nontrivial relation on every prime `p<=y`. This is a different information type from minimum support and is not closed by `MC-248`.

## 5. Prior art and novelty audit

All external mechanisms used here are classical or established. Finite-abelian duality, primary decomposition of characters, and the divisibility of local character order by `r-1` are standard. `MC-239` already supplies the shell-specific reduction to tame cross-prime characters; `MC-242`, `MC-247`, and `MC-248` supply the support lower bounds and witness-exponent dictionary.

The new literature input used for the occupancy step is:

- Tomohiro Yamada, *Explicit improvements of the Brun-Titchmarsh theorem for arbitrary intervals*, arXiv:2312.16090 (26 December 2023). The paper proves the explicit arbitrary-interval inequality `(18)` for every `Y>k`. It is an arXiv preprint and is used here only for that displayed prime-counting upper bound.

The classical Brun–Titchmarsh principle already makes the qualitative mechanism standard: primes `r` for which a prescribed order divides `r-1` lie in the progression `1 mod d` and cannot occupy an interval more densely than the sieve bound allows. A targeted search found adjacent literature on shifted primes and large factors of `p-1`, but no source asserting the exact shell-annihilator exponent consequences `(7)`–`(13)`. No novelty is claimed for Brun–Titchmarsh, character primary decomposition, or inversion of `z/log z`.

The durable Mathia delta is the composition of those standard mechanisms with the exact shell blind quotient: **support pressure plus progression occupancy localizes the possible torsion orders even though support pressure alone cannot force generation**. This is a frontier reduction, not a new theorem of analytic number theory.

## 6. Boundaries and falsification tests

- The unconditional bounds `(7)`–`(8)` depend on the `MC-242` growing-support theorem and inherit its asymptotic regime; they do not assert that a nontrivial quotient actually survives.
- The ERH bounds `(10)`–`(11)` are conditional on exactly the ERH input already isolated in `MC-247` and must not be reported as unconditional arithmetic progress.
- Equation `(13)` is a deterministic consequence of the schematic witness hypothesis `(12)`; it is not a claim that such a theorem exists for arbitrary `A`.
- The quotient exponent and quotient order are different invariants. Neither `(7)` nor `(10)` bounds the rank of a low-order primary component, and neither implies `H=G`.
- The use of `(18)` counts all primes in the progression `1 mod d`, not only those belonging to the selected shell subset `S`; it is therefore a safe upper bound and may be far from sharp for a sparse `S`.
- No distributional independence between the conditions `r in S` and `r=1 mod d` is assumed.
- No contour shift, reciprocal-`L` continuation, or zero-free region enters the unconditional derivation.
- None of these torsion bounds estimates the signed rough Möbius source term of `MC-246`; that remains the independent amplitude exit.
