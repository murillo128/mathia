---
id: WP-341
title: Cross-prime stationary Hilbert transport controls logarithmic variance only by containing the arithmetic log-square
branch: weil_positivity
status: supported
kind: cross-prime-negative-type-transport-rigidity
claim_strength: exact classification on the full prime-exponent displacement group; a translation-invariant squared-Hilbert/CND transport cost can dominate the quadratic arithmetic logarithmic displacement required by the WP-338--WP-340 defect mechanism if and only if its classical quadratic Levy-Khinchin component already contains that logarithm as a bounded rank-one Hilbert direction; the spectral/jump component cannot create the missing cross-prime control
created: 2026-09-17
related: [WP-039, WP-115, WP-296, WP-338, WP-339, WP-340]
prior_art:
  - Christian Berg, Jens Peter Reus Christensen, and Paul Ressel, Harmonic Analysis on Semigroups, Graduate Texts in Mathematics 100, Springer, 1984, especially the Levy-Khinchin representation for negative-definite functions on abelian groups
  - Cedric Arhancet and Christoph Kriegler, Riesz Transforms, Hodge-Dirac Operators and Functional Calculus for Multipliers, Lecture Notes in Mathematics 2304, Springer, 2022, DOI 10.1007/978-3-030-99011-4, formula (1.22) and the quadratic-part limit on discrete abelian groups
  - I. J. Schoenberg, Metric Spaces and Positive Definite Functions, Transactions of the American Mathematical Society 44 (1938), 522-536, DOI 10.2307/1989894
---

# WP-341 — Cross-prime stationary Hilbert transport controls logarithmic variance only by containing the arithmetic log-square

## Claim

`WP-340` closed the stationary Hilbertian escape on a single prime-power ray but deliberately left **cross-prime coupling** open. The strongest scalar stationary version of that escape can also be classified exactly.

Let

\[
\Gamma:=\bigoplus_{p\ \mathrm{prime}}\mathbb Z e_p
\tag{1}
\]

be the finite-support prime-exponent displacement group and let

\[
L(\alpha):=\sum_p \alpha_p\log p
\tag{2}
\]

be the arithmetic logarithm homomorphism. A translation-invariant squared-Hilbert displacement cost on the exponent lattice is equivalently a symmetric conditionally negative-definite function

\[
\psi:\Gamma\to[0,\infty),
\qquad \psi(0)=0,
\tag{3}
\]

with cost `c(alpha,beta)=psi(alpha-beta)`.

For a discrete abelian group the classical Levy--Khinchin decomposition gives

\[
\boxed{
\psi(\alpha)
=q(\alpha)
+\int_{\widehat\Gamma\setminus\{1\}}
\bigl(1-\operatorname{Re}\chi(\alpha)\bigr)\,d\mu(\chi),
}
\tag{4}
\]

where `q>=0` is a quadratic form on `Gamma`, `mu` is a positive symmetric measure with the pointwise integrability required by (4), and

\[
\boxed{
q(\alpha)=\lim_{m\to\infty}\frac{\psi(m\alpha)}{m^2}.
}
\tag{5}
\]

The integral in (4) is nonnegative, so `psi>=q` pointwise.

Fix `a>0`. The following are equivalent:

1. there is `R>=0` such that
   \[
   \psi(\alpha)\ge a\,L(\alpha)^2
   \qquad\text{whenever }|L(\alpha)|\ge R;
   \tag{6}
   \]
2. the quadratic Levy--Khinchin component itself satisfies
   \[
   \boxed{q(\alpha)\ge a\,L(\alpha)^2\qquad(\alpha\in\Gamma);}
   \tag{7}
   \]
3. if `D:Gamma->H_q` is the canonical Hilbert realization of `q`,
   \[
   q(\alpha)=\|D\alpha\|^2,
   \tag{8}
   \]
   then the arithmetic logarithm is already a bounded Hilbert covector of that quadratic sector: there exists `w in H_q` with
   \[
   \boxed{
   L(\alpha)=\langle D\alpha,w\rangle
   \quad\text{for every }\alpha,
   \qquad
   \|w\|\le a^{-1/2}.
   }
   \tag{9}
   \]

Thus a stationary cross-prime Hilbert geometry cannot obtain the quadratic logarithmic control needed by `WP-338`--`WP-340` from a richer spectral/jump coupling. **If it controls `L^2`, the arithmetic logarithm was already present in its Gaussian/quadratic sector as a positive rank-one direction.**

On every finite prime set `P`, write `ell_P=((log p))_{p in P}` and represent `q` by a positive-semidefinite Gram matrix `G_P`. Then (7) is exactly

\[
\boxed{
G_P\succeq a\,\ell_P\ell_P^{\mathsf T}.
}
\tag{10}
\]

So the successful cross-prime stationary geometry literally contains a PSD arithmetic log-square summand; the remaining CND spectral part may change lower-order distances but cannot be the source of the required second-moment control.

**Classification:** `EXACT-DERIVED + CLASSICAL-ABELIAN-LEVY-KHINTCHINE + FULL-PRIME-EXPONENT-LATTICE + CROSS-PRIME-STATIONARY-HILBERTIAN + QUADRATIC-PART-EXTRACTION + BOUNDED-COVECTOR-FACTORIZATION + MATCHED-CONTROL + DECISIVE-NEGATIVE-FOR-STATIONARY-SCALAR-CROSS-PRIME-REPAIR + NOT-WEIL-POSITIVITY`.

## 1. The exact object is the prime-exponent displacement group

Prime Lattice supplies canonical exponent coordinates. An integer or rational multiplicative displacement has finite-support exponent vector

\[
\alpha=(\alpha_p)_p\in\Gamma.
\tag{11}
\]

Its logarithmic displacement is not an additional arbitrary coordinate:

\[
L(\alpha)=\log\left(\prod_p p^{\alpha_p}\right).
\tag{12}
\]

Unique factorization implies

\[
L(\alpha)=0\iff \alpha=0.
\tag{13}
\]

The relevant scalar observable in the `WP-332`--`WP-340` UCP chain is precisely this logarithmic coordinate. `WP-338` and `WP-339` showed that controlling its Kadison/variance defect requires quadratic control of long logarithmic displacements. `WP-340` then proved on one ray that a stationary squared-Hilbert metric supplies such control only through Euclidean drift.

A genuinely cross-prime stationary scalar repair therefore asks whether a CND cost on the **whole** displacement group `Gamma` can use interactions among prime coordinates to generate the missing `L(alpha)^2` control even when no such direction is explicitly present.

Equation (4) is the exact classical classification of that candidate class.

## 2. Scaling kills the spectral/jump escape

Assume (6). Fix any `alpha in Gamma`.

If `alpha=0`, (7) is trivial. If `alpha!=0`, then by (13)

\[
L(\alpha)\ne0.
\tag{14}
\]

Hence for all sufficiently large positive integers `m`,

\[
|L(m\alpha)|=m|L(\alpha)|\ge R.
\tag{15}
\]

Applying (6) to `m alpha` gives

\[
\frac{\psi(m\alpha)}{m^2}
\ge
 a\,L(\alpha)^2.
\tag{16}
\]

Taking `m->infinity` and using the classical extraction formula (5),

\[
\boxed{
q(\alpha)\ge a\,L(\alpha)^2.
}
\tag{17}
\]

This proves `(6) => (7)`.

Conversely, the Levy--Khinchin remainder in (4) is nonnegative, so

\[
\psi(\alpha)\ge q(\alpha).
\tag{18}
\]

Therefore (7) implies

\[
\psi(\alpha)\ge aL(\alpha)^2
\tag{19}
\]

for **every** `alpha`, stronger than the eventual condition (6). Thus `(7) => (6)` with `R=0`.

This is the key cross-prime rigidity. The spectral measure in (4) may couple every prime coordinate and may be infinite, anisotropic, or highly nonlocal. None of that matters to the quadratic tail: dilation along each arithmetic displacement extracts `q` exactly. If the full cost eventually dominates the logarithmic square, the quadratic component already did so before the spectral/jump term was added.

## 3. The arithmetic logarithm must already be a Hilbert direction

A nonnegative quadratic form on an abelian group has a canonical Hilbert realization. Quotient `Gamma` by the nullspace of `q` and define on the quotient

\[
\langle D\alpha,D\beta\rangle_q
:=
\frac14\bigl(q(\alpha+\beta)-q(\alpha-\beta)\bigr).
\tag{20}
\]

Complete to a real Hilbert space `H_q`. Then

\[
q(\alpha)=\|D\alpha\|^2.
\tag{21}
\]

If (7) holds, then `D alpha=0` implies `L(alpha)=0`, so `L` descends to the range of `D`. Moreover,

\[
|L(\alpha)|
\le a^{-1/2}\|D\alpha\|.
\tag{22}
\]

Thus the functional

\[
D\alpha\longmapsto L(\alpha)
\tag{23}
\]

is bounded on `D(Gamma)` and extends continuously to `H_q`. The Riesz representation theorem supplies `w in H_q` with

\[
L(\alpha)=\langle D\alpha,w\rangle,
\qquad
\|w\|\le a^{-1/2},
\tag{24}
\]

which is (9).

Conversely, if (9) holds, Cauchy--Schwarz gives

\[
L(\alpha)^2
\le \|w\|^2q(\alpha).
\tag{25}
\]

Hence any `a<=||w||^{-2}` gives (7). This proves the factorization equivalence.

In particular, on generators,

\[
\boxed{
\log p=\langle De_p,w\rangle
\qquad\text{for every prime }p.
}
\tag{26}
\]

The prime weights are therefore not being synthesized by the spectral part of the stationary geometry. They are already coordinates of one bounded covector in its quadratic Hilbert sector.

## 4. Finite prime windows make the rank-one content explicit

Restrict to a finite set of primes

\[
P=\{p_1,\ldots,p_d\}.
\tag{27}
\]

Write

\[
q(n)=n^{\mathsf T}G_Pn,
\qquad
\ell_P=(\log p_1,\ldots,\log p_d)^{\mathsf T}.
\tag{28}
\]

Then

\[
L(n)^2=n^{\mathsf T}\ell_P\ell_P^{\mathsf T}n.
\tag{29}
\]

Condition (7) is therefore exactly the Loewner inequality (10), so

\[
G_P-a\ell_P\ell_P^{\mathsf T}\succeq0.
\tag{30}
\]

This gives a particularly transparent audit test for any proposed finite cross-prime stationary metric: compute or derive its quadratic Levy--Khinchin matrix. If that matrix does not already contain the rank-one arithmetic log direction, no amount of spectral/jump CND structure can repair the missing quadratic logarithmic control.

The result does **not** require the quadratic sector to be rank one. Extra positive drift directions are allowed. It says only that a successful metric must dominate, and hence contain, the rank-one `L^2` direction as a PSD summand.

## 5. Failure of the quadratic sector produces arbitrarily cheap large logarithmic displacements

Suppose there is no `a>0` for which (7) holds. Equivalently,

\[
\inf_{\alpha\ne0}
\frac{q(\alpha)}{L(\alpha)^2}=0.
\tag{31}
\]

Choose `alpha_j` with the ratio in (31) tending to zero. For each fixed `alpha_j`, (5) gives

\[
\frac{\psi(m\alpha_j)}{m^2L(\alpha_j)^2}
\longrightarrow
\frac{q(\alpha_j)}{L(\alpha_j)^2}.
\tag{32}
\]

Choosing `m_j` sufficiently large produces displacements

\[
\beta_j=m_j\alpha_j
\tag{33}
\]

with

\[
|L(\beta_j)|\to\infty,
\qquad
\frac{\psi(\beta_j)}{L(\beta_j)^2}\to0.
\tag{34}
\]

So the failure is not merely a matrix-comparison nicety. The stationary Hilbert geometry then has genuinely long arithmetic-log displacements whose transport cost is asymptotically negligible compared with the second moment they can carry.

On the full exponent lattice, the same symmetric three-point construction used in `WP-339` can be placed on

\[
0,\quad \beta_j,\quad 2\beta_j,
\tag{35}
\]

because `L` is linear. With rare symmetric jumps from the middle point, one can preserve the `L` barycenter exactly while the logarithmic variance is normalized to stay fixed and the `psi`-transport cost tends to zero by (34). This is the full-lattice matched-control witness.

This witness is **not** asserted to lie inside the Mangoldt prime-power support. That distinction is part of the boundary below.

## 6. Relation to WP-340 and the cross-prime escape

`WP-340` proved the one-generator statement on `Z`: a stationary Hilbertian cost on a prime-power ray has a quadratic tail if and only if its cocycle contains invariant Euclidean drift. It explicitly left cross-prime coupling open.

The present theorem closes the direct scalar stationary version of that escape. Passing from one generator to the full free abelian exponent group does permit nontrivial cross-prime CND interactions, but the classical abelian Levy--Khinchin decomposition separates them into:

\[
\text{quadratic/Gaussian sector }q
\quad+\quad
\text{positive spectral/jump sector}.
\tag{36}
\]

Only the first sector can survive quadratic dilation. If the metric controls the arithmetic logarithmic second moment, its quadratic sector already contains `L^2` in the precise factorization sense (9)--(10).

Thus cross-prime stationarity does not reveal a hidden arithmetic mechanism inside the spectral remainder. It only enlarges the possible PSD quadratic drift matrix. The arithmetic burden is moved to an independent theorem that would have to explain why Mathia canonically selects a drift sector containing the covector

\[
e_p\longmapsto\log p.
\tag{37}
\]

No such theorem is supplied here.

## 7. Matched controls remove arithmetic selectivity

Nothing in the proof uses primality beyond the choice of the homomorphism (2). Let

\[
\Gamma_I=\bigoplus_{j\in I}\mathbb Z e_j
\tag{38}
\]

and choose any nonzero real weights `omega_j`. Define

\[
L_\omega(\alpha)=\sum_j\alpha_j\omega_j.
\tag{39}
\]

The same proof gives

\[
\psi(\alpha)\gtrsim L_\omega(\alpha)^2
\quad\Longleftrightarrow\quad
q(\alpha)\gtrsim L_\omega(\alpha)^2
\quad\Longleftrightarrow\quad
L_\omega=\langle D(\cdot),w_\omega\rangle.
\tag{40}
\]

So even the surviving cross-prime quadratic mechanism is generic free-abelian Hilbert geometry. Replacing `log p` by arbitrary generator weights leaves the theorem unchanged. This sharply separates a useful analytic control from an arithmetic explanation of Weil positivity.

## 8. Prior-art and novelty audit

The harmonic-analysis theorem underlying (4)--(5) is classical and is **not** claimed as new. Berg--Christensen--Ressel give the general semigroup/abelian-group Levy--Khinchin theory for negative-definite functions. Arhancet--Kriegler state the discrete-abelian specialization explicitly: a conditionally negative length is the sum of a nonnegative quadratic form and a positive character integral, with the quadratic form recovered by the limit `q(s)=lim_n psi(ns)/n^2`. Schoenberg is the classical source for the squared-Hilbert/negative-type correspondence.

The Hilbert factorization (20)--(25) is elementary positive-quadratic-form theory. The finite-window matrix inequality (10) is the same statement in coordinates.

The Mathia-specific contribution is the synthesis with the live `WP-338`--`WP-340` obstruction:

- the intrinsic prime-exponent displacement group is the correct cross-prime stationary domain;
- its arithmetic observable is the canonical homomorphism `L(alpha)=sum alpha_p log p`;
- any stationary Hilbert/CND cost that supplies the needed global quadratic logarithmic control must already contain `L` in its quadratic Hilbert sector;
- the entire spectral/jump cross-prime coupling is powerless to create that missing direction;
- the conclusion survives arbitrary-weight matched controls, so this positivity remains non-arithmetic unless a separate Mathia theorem forces the specific logarithmic covector.

A bounded literature audit found the classical negative-definite/Levy--Khinchin decomposition and modern operator-theoretic restatements, but no arithmetic novelty is attributed to those ingredients.

## 9. Aggressive falsification and exact boundary

**This does not prove that all cross-prime geometry fails.** It classifies only scalar, translation-invariant squared-Hilbert/CND displacement costs on the full exponent group.

**Source-support-only geometries remain open.** The full-lattice witness (35) need not lie on the union of prime-power axes supporting the Mangoldt source. A geometry whose domain is intrinsically that sparse support, rather than a translation-invariant metric on all exponent displacements, is outside this theorem. `WP-340` still controls each individual prime-power ray.

**Nonstationary arithmetic metrics remain open.** If the metric depends on the base exponent vector rather than only on the displacement, there is no single CND function `psi(alpha-beta)` and the Levy--Khinchin scaling extraction does not apply.

**Operator-valued/noncommutative transport remains open.** A positive operator-valued correspondence, matrix-valued boundary response, or noncommutative coupling need not reduce to one scalar negative-type cost before positivity is taken.

**A canonical theorem forcing the quadratic sector would be genuine extra structure.** The result does not forbid Mathia from deriving a quadratic form `q` whose geometry independently forces (9). It says that such a theorem, not the stationary spectral/jump remainder, would carry the arithmetic content.

**The archimedean/global bridge is untouched.** Even a canonical `q` containing `L^2` would only close the logarithmic second-moment control problem. It would not generate the Gamma term, polar counterterms, the full Weil explicit-formula pairing, or an RH-independent theorem of positivity for that pairing.

## Consequence for the Weil-positivity search

The scalar stationary Hilbert route now has the same rigidity across primes that `WP-340` established on one ray:

\[
\boxed{
\text{stationary CND cross-prime geometry}
+\text{ quadratic control of arithmetic log}
\Longrightarrow
\text{arithmetic log-square already present in }q.
}
\tag{41}
\]

Cross-prime spectral richness does not manufacture the needed quadratic direction. A surviving Mathia-native mechanism must therefore obtain its arithmetic sign from a genuinely new input: a canonical theorem forcing the logarithmic quadratic sector, a nonstationary/source-support geometry, an operator-valued or cohomological coupling, or a finite--archimedean structure whose positivity is established before the explicit-formula identification.
