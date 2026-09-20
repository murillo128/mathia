---
id: WP-389
title: Logarithmic interface current classicalizes to Ramanujan orthogonality
branch: weil_positivity
status: supported
kind: pointed-boundary-interface-ramanujan-classicalization
claim_strength: exact RH-independent identification of the WP-384 integer-interface current with normalized Ramanujan sums, together with a positive mean-square/logarithmic interface Gram that orthogonalizes all shell indices with weight phi(m)/m; every mixed-prime shell therefore retains positive interface energy and any prime-power projection would have to be added as a separate arithmetic multiplier rather than follow from the interface geometry
created: 2026-09-21
related: [WP-161, WP-162, WP-384, WP-386, WP-387, WP-388]
clues: [CLUE-weil-positivity-noncharacter-finite-archimedean-incidence]
prior_art:
  - classical Ramanujan sums and the divisor formula c_m(k)=sum_{d|(m,k)} d mu(m/d)
  - classical mean orthogonality of Ramanujan sums
  - classical cyclotomic/Ramanujan-sum relations
---

# WP-389 — Logarithmic interface current classicalizes to Ramanujan orthogonality

## Claim

`WP-388` leaves an interface-sensitive boundary geometry with extra degrees of freedom as one possible escape from the strongly-local domain obstruction. On the exact `WP-384` carrier, however, the most immediate source-native interface observable already has a classical arithmetic identity.

For

\[
h_m(x)=\frac1{\sqrt m}\left(
\Lambda(m)+\sum_{d\mid m}\mu(m/d)H_{\lfloor x/d\rfloor}
\right),
\qquad m>1,
\tag{1}
\]

write

\[
\Delta_k h_m:=h_m(k+0)-h_m(k-0),
\qquad k\ge1.
\tag{2}
\]

Then the logarithmically scale-normalized interface current is exactly a Ramanujan sum:

\[
\boxed{
 j_m(k):=k\,\Delta_k h_m
 =\frac{c_m(k)}{\sqrt m},
}
\tag{3}
\]

where

\[
c_m(k)
:=\sum_{d\mid (m,k)}d\,\mu(m/d)
=\sum_{\substack{1\le a\le m\\(a,m)=1}}
 e^{2\pi iak/m}
\tag{4}
\]

is the classical Ramanujan sum.

Consequently the ordinary mean-square geometry of the interface currents is diagonal in the shell index:

\[
\boxed{
\lim_{X\to\infty}\frac1X
\sum_{k\le X}j_m(k)\overline{j_n(k)}
=\delta_{m,n}\frac{\varphi(m)}m.
}
\tag{5}
\]

The same Gram is obtained by the first scale-covariant nearest-neighbor interface energy. For any finite shell combination

\[
f=\sum_{m\in F}\alpha_m h_m,
\tag{6}
\]

define

\[
\mathcal E_X(f)
:=\sum_{k\le X}k\,|\Delta_k f|^2.
\tag{7}
\]

Then

\[
\boxed{
\lim_{X\to\infty}
\frac{\mathcal E_X(f)}{\log X}
=\sum_{m\in F}|\alpha_m|^2\frac{\varphi(m)}m.
}
\tag{8}
\]

In particular every nonzero finite shell combination has positive logarithmic interface-energy density, while its unnormalized energy grows like a positive constant times `log X`.

Thus the interface route does produce a genuine positive geometry that sees the integer jumps excluded from a strongly-local diffusion, but it immediately classicalizes to Ramanujan harmonic analysis. It does **not** recover the Weil finite-place selector. Every mixed-prime shell has strictly positive norm, and

\[
\frac{\varphi(m)}m
=\prod_{p\mid m}\left(1-\frac1p\right)
\tag{9}
\]

depends only on the radical of `m`. Prime-power exponent data and the Mangoldt weight are absent.

**Classification:** `EXACT-DERIVED + RH-INDEPENDENT + INTERFACE-CURRENT + RAMANUJAN-SUM-IDENTIFICATION + CLASSICAL-ORTHOGONALITY + POSITIVE-INTERFACE-GRAM + MIXED-SHELL-POSITIVE-CONTROL + RADICAL-ONLY-DIAGONAL + PRIOR-ART-CLASSICALIZATION + DECISIVE-NEGATIVE-FOR-MEAN-SQUARE-INTERFACE-POSITIVITY + NOT-A-WEIL-BRIDGE`.

## 1. The exact jump is the Ramanujan divisor formula

Crossing the integer `k`, the term `H_{floor(x/d)}` changes only when `d|k`. In that case the index increases from `k/d-1` to `k/d`, so the harmonic-number jump is

\[
H_{k/d}-H_{k/d-1}=\frac d k.
\tag{10}
\]

Applying this to (1) gives

\[
\Delta_k h_m
=\frac1{k\sqrt m}
\sum_{\substack{d\mid m\\d\mid k}}
 d\,\mu(m/d).
\tag{11}
\]

The divisor sum in (11) is exactly the standard Kluyver/von-Sterneck formula for the Ramanujan sum `c_m(k)`. Hence (3) is an identity, with no limiting process, zero data, RH assumption, fitted kernel, or regularization.

This also sharpens the interface statement in `WP-388`. There it was enough to note that a squarefree mixed shell `pq` has a nonzero jump at every integer. Equation (3) identifies the **entire jump sequence** for every shell: the boundary interfaces carry the classical primitive-root Fourier moments indexed by `m`.

The factor `k` is not selected to manufacture the orthogonality below. It is the Euler/logarithmic scaling factor converting a jump at physical scale `x=k` into the dimensionless interface current associated with `x d/dx`. The unscaled jump already contains the forced `1/k` factor in (11).

## 2. Classical Ramanujan orthogonality gives the full positive Gram

For fixed `m,n`, the product `c_m(k)c_n(k)` is periodic with period

\[
L=\operatorname{lcm}(m,n).
\tag{12}
\]

Its mean over one period is the classical Ramanujan orthogonality relation

\[
\frac1L\sum_{k=1}^L c_m(k)c_n(k)
=\delta_{m,n}\varphi(m).
\tag{13}
\]

For completeness, (13) follows directly from the primitive-root representation in (4). Expanding both sums and averaging over `k` leaves only pairs of reduced fractions whose phases cancel. For `m,n>1`, cancellation requires

\[
\frac a m+\frac b n=1.
\tag{14}
\]

Reducedness then forces `m=n` and `b=m-a`, giving exactly `phi(m)` surviving pairs. This proves (13) without importing any analytic number theory.

Dividing by `sqrt(mn)` gives (5). By polarization, for every finite combination (6),

\[
\lim_{X\to\infty}\frac1X
\sum_{k\le X}
\left|k\Delta_k f\right|^2
=\sum_{m\in F}|\alpha_m|^2\frac{\varphi(m)}m.
\tag{15}
\]

So the interface current does not merely have a positive diagonal. Distinct arithmetic shells are mutually orthogonal in its canonical mean-square completion.

## 3. The logarithmic nearest-neighbor energy has the same limit

The positive truncated energy (7) can be rewritten using (3) as

\[
\mathcal E_X(h_m,h_n)
=\frac1{\sqrt{mn}}
\sum_{k\le X}\frac{c_m(k)c_n(k)}k.
\tag{16}
\]

If `a(k)` is periodic with mean `A`, then elementary summation over residue classes gives

\[
\sum_{k\le X}\frac{a(k)}k
=A\log X+O_a(1).
\tag{17}
\]

Apply (17) to `a(k)=c_m(k)c_n(k)` and use (13):

\[
\mathcal E_X(h_m,h_n)
=\delta_{m,n}\frac{\varphi(m)}m\log X+O_{m,n}(1).
\tag{18}
\]

Equation (8) follows for finite combinations.

This is the scale-compatible control suggested by the floor partition itself. On the logarithmic coordinate `t=log x`, adjacent large integer interfaces are separated at scale `1/k`; a first-order nearest-neighbor conductance therefore has scale `k`. More importantly, the conclusion is not an artifact of this particular averaging convention: the direct counting mean of the logarithmic currents in (5) gives exactly the same shell Gram. Any positive averaging whose normalized mass becomes equidistributed among residue classes modulo each fixed period likewise recovers (13).

The infinite unnormalized graph energy is therefore not a finite shell form: every nonzero finite shell combination has `E_X(f)~C_f log X` with `C_f>0`. Dividing by `log X` produces an intensive energy density, not a hidden finite-energy completion.

## 4. Matched controls kill the prime-power-selector interpretation

The smallest mixed control is `m=6`. Its Ramanujan current is periodic,

\[
c_6(k)=1,-1,-2,-1,1,2,\ldots,
\tag{19}
\]

and its period mean square is `phi(6)=2`. Hence

\[
\lim_{X\to\infty}\frac1X\sum_{k\le X}|j_6(k)|^2
=\frac{\varphi(6)}6=\frac13>0,
\tag{20}
\]

even though `Lambda(6)=0`. The interface mean-square therefore fails the exact mixed-shell control in the strongest possible way: the mixed shell is an orthogonal positive direction rather than a null direction.

For a prime power `m=p^a`,

\[
\frac{\varphi(p^a)}{p^a}=1-\frac1p,
\tag{21}
\]

independent of `a`. Thus the positive interface diagonal forgets the prime-power exponent. For a squarefree mixed shell `pq`,

\[
\frac{\varphi(pq)}{pq}
=\left(1-\frac1p\right)
 \left(1-\frac1q\right)>0.
\tag{22}
\]

The contrast with the source boundary value is exact. On `(0,1)`, `WP-386` has

\[
h_m=\frac{\Lambda(m)}{\sqrt m},
\tag{23}
\]

which has the desired prime-power support but only one rank-one coordinate. Passing to the full first-order interface current does create infinitely many orthogonal coordinates, yet those coordinates are Ramanujan modes and the canonical positive mean-square weights every shell rather than selecting prime powers.

One can of course define an operator on the orthogonal Ramanujan shell basis whose eigenvalue is zero on mixed `m` and nonzero on prime powers. But after (5) that is precisely an **additional arithmetic spectral multiplier**. Positivity alone places no restriction preventing such programming, and the floor/interface geometry does not force that projector. Inserting it would therefore restate the desired selector rather than explain its sign.

## 5. Prior-art and novelty audit

The number-theoretic ingredients are classical. Ramanujan introduced the sums now denoted `c_m(k)` in *On Certain Trigonometrical Sums and Their Applications in the Theory of Numbers*, Transactions of the Cambridge Philosophical Society 22 (1918), 259--276. The divisor formula in (4) is standard; an audit-friendly source is C. A. Nicol, *Some Formulas Involving Ramanujan Sums*, Canadian Journal of Mathematics 14 (1962), 284--286, DOI `10.4153/CJM-1962-019-8`. Product/orthogonality identities are part of the classical Ramanujan-sum literature; see for example L. Toth, *Sums of products of Ramanujan sums*, Annali dell'Universita di Ferrara 58 (2012), 183--197, DOI `10.1007/s11565-011-0143-3`, arXiv `1104.1906`.

Cyclotomic/Ramanujan relations are themselves classical, so no novelty is claimed for identifying a new general Ramanujan-sum theorem. A bounded search around Ramanujan sums, cyclotomic logarithmic derivatives, Nyman--Beurling geometry, and harmonic-floor formulas found the expected classical Ramanujan/cyclotomic harmonic analysis rather than an independent Weil-positivity mechanism.

The line-specific contribution is narrower: the exact integer-jump trace of the `WP-384` **critical primitive-cyclotomic boundary layer** is the normalized Ramanujan basis, and the two immediate scale-neutral positive interface averages, (5) and (8), therefore classicalize to the totient diagonal. This closes the most direct interface-current interpretation left after `WP-388`; it is not a new RH criterion.

## 6. Boundary of the obstruction

The theorem does not rule out an arbitrary non-Markov off-diagonal form on the interface-current space. Ramanujan orthogonality actually makes clear why such a form needs an additional source-forced principle: once the shell directions are orthogonal, a general positive operator can be assigned essentially arbitrary nonnegative spectral data on those directions. A useful candidate must explain why its kernel or multiplier is forced **before** the prime-power answer is known.

Nor does the result rule out retaining the finite-`q` prelimit structure discarded in `WP-384`, or an indefinite finite--archimedean coupling in which mixed-shell terms remain alive until a final assembled sign theorem. Those mechanisms do not require a standalone positive interface energy to be the finite-place selector.

What is ruled out is the natural first-order completion suggested by the discontinuities themselves: take the scale-normalized integer-interface current and its ordinary positive mean-square/nearest-neighbor geometry. That construction has a complete exact answer, and the answer is the classical Ramanujan Hilbert geometry with positive mass on every shell.

## Consequence for the research line

`WP-388` showed that continuous strongly-local diffusion cannot read the integer interfaces while admitting the shell steps. `WP-389` now reads those interfaces explicitly. The extra boundary degrees of freedom are real, but their first-order source trace is not a hidden Mangoldt selector: it is the Ramanujan basis.

The canonical positive mean-square sign is therefore too easy. It orthogonalizes all arithmetic shells and assigns `phi(m)/m>0` to every one of them, including every mixed-prime shell. Recovering sparse Weil support would require a further geometrically forced non-diagonal operation, a finite-prelimit mechanism, or a genuinely global finite--archimedean assembly; a projector chosen in the Ramanujan basis does not count.

## Conclusion

The integer discontinuities of the `WP-384` boundary layer have an exact classical identity:

\[
k\Delta_k h_m=\frac{c_m(k)}{\sqrt m}.
\]

Thus the obvious interface completion does not reveal a new positivity mechanism. Its positive Hilbert geometry is Ramanujan orthogonality, with shell norm `phi(m)/m`; mixed shells remain positive, prime-power exponents are forgotten, and no Gamma or polar term appears.

The interface survives the strongly-local obstruction only to classicalize. Any remaining interface-based Weil route must add genuinely new, source-forced structure beyond positive mean-square geometry of the jumps.