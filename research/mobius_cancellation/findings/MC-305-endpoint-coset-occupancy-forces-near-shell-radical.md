# MC-305 — Endpoint coset occupancy forces the common radical near the shell scale

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact endpoint-partition setup of `MC-296` and the fixed common-radical realization of `MC-304`. Let

\[
\mathcal R_y=\{r:y<r\le 2y,\ r\text{ prime},\ r\equiv1\pmod4\},
\qquad N=|\mathcal R_y|,
\]

and let

\[
\chi_1,\ldots,\chi_R
\]

be linearly independent quadratic source characters generated from lower odd primes, with common squarefree support radical

\[
P=\prod_{p\in U}p.
\]

Induce every selected character to modulus `P`, as in `MC-304`. Suppose their defect sets form an exact endpoint partition of the shell: for every `r in mathcal R_y`, exactly one selected character takes its defect value `+1`, while the other `R-1` characters take the preferred value `-1`.

Then the shell primes occupy only `R` cosets of the common kernel of the selected character family. More precisely, if

\[
\Theta:(\mathbb Z/P\mathbb Z)^\times\longrightarrow\{\pm1\}^R,
\qquad
\Theta(a)=(\chi_1(a),\ldots,\chi_R(a)),
\]

then `Theta` is onto, every fiber has `phi(P)/2^R` reduced residue classes, and

\[
\Theta(\mathcal R_y)
\subseteq
\{(-1,\ldots,-1,+1,-1,\ldots,-1):1\le i\le R\}.
\tag{1}
\]

Consequently, after also imposing `r=1 mod 4`, the whole shell is contained in exactly

\[
\boxed{
\frac{R\varphi(P)}{2^R}
}
\tag{2}
\]

reduced residue classes modulo `4P`.

Applying the arbitrary-interval Brun--Titchmarsh bound already audited in `MC-249` gives the following unconditional necessary condition:

\[
\boxed{
\log\frac{y}{P}
\le
(2+o(1))\frac{R\log y}{2^R}+O(1).
}
\tag{3}
\]

Equivalently,

\[
\boxed{
P
\ge
y\exp\!\left(
-(2+o(1))\frac{R\log y}{2^R}-O(1)
\right).
}
\tag{4}
\]

The statement is nontrivial only when `P<y`; if `P>=y/4`, `(3)` is already automatic up to the displayed `O(1)` term. When `4P<y`, the stronger explicit form follows from Yamada's constant:

\[
\boxed{
\log\frac{y}{4P}+0.8601
\le
(2+o(1))\frac{R\log y}{2^R}.
}
\tag{5}
\]

At the live critical-rank scale, this is much stronger than merely saying that the individual source conductors exceed a quasi-subpower Page threshold. For example, if

\[
\frac{2^R}{\log y}\to\kappa\in(0,\infty),
\]

then `R=(\log\log y)/(\log2)+O(1)` and `(4)` becomes

\[
\boxed{
P
\ge
\frac{y}{(\log y)^{\,2/(\kappa\log2)+o(1)}}.
}
\tag{6}
\]

In the balanced normalization `2^R~log y`, the exponent is `2/log 2 = 2.88539...`.

Thus the first escape branch left by `MC-304` cannot be realized by an arbitrarily small common radical even when `phi(P)/P` is large enough to absorb the large-sieve energy. The endpoint partition itself forces the selected quadratic family to have a common ramification radical within a polylogarithmic factor of the shell scale at critical rank.

This still does **not** contradict the endpoint model: a radical of size `y/(log y)^{O(1)}` or larger remains possible, and no theorem here controls whether the required `R` sign cells are actually occupied with the endpoint multiplicities. No estimate for `M(x)` follows.

## 1. Endpoint partition is a support statement in the quotient, not only an energy statement

Let

\[
X=\langle\chi_1,\ldots,\chi_R\rangle.
\]

`MC-304` verifies that the characters remain independent after induction to modulus `P`, so

\[
|X|=2^R.
\]

Duality therefore makes `Theta` onto. Its kernel

\[
K=\bigcap_{i=1}^R\ker\chi_i
\]

has index `2^R` in `(Z/PZ)^*`, hence every sign vector has exactly

\[
|K|=\frac{\varphi(P)}{2^R}
\]

preimages among the reduced residue classes modulo `P`.

For a shell prime `r`, membership in the defect set of `chi_i` is exactly the condition `chi_i(r)=+1`. Because the defect sets partition the shell, exactly one coordinate of `Theta(r)` equals `+1`. This proves `(1)` and shows that the shell lies in the union of `R` fibers of `Theta`, containing exactly the number of residue classes in `(2)` modulo `P`.

The shell also imposes `r=1 mod 4`. The radical `P` is odd in the present Legendre-source realization, so the Chinese remainder theorem identifies each reduced class modulo `P` with exactly one reduced class modulo `4P` satisfying `a=1 mod 4`. Therefore `(2)` is also the exact number of admissible classes modulo `4P`.

This is information that the energy estimate of `MC-304` deliberately compresses away: the reciprocal/endpoint model does not merely have large selected Fourier energy; its support in the selected quotient is concentrated on only `R` of the `2^R` available sign cells.

## 2. Brun--Titchmarsh turns quotient support concentration into a radical lower bound

Assume first that

\[
4P<y.
\]

For every reduced residue class `a mod 4P`, Yamada's arbitrary-interval Brun--Titchmarsh inequality, already recorded and audited in `MC-249`, gives

\[
\pi(2y;4P,a)-\pi(y;4P,a)
<
\frac{2y}{\varphi(4P)\{\log(y/(4P))+0.8601\}}.
\tag{7}
\]

Because `P` is odd,

\[
\varphi(4P)=2\varphi(P).
\]

Summing `(7)` over the `R phi(P)/2^R` admissible classes from `(2)` therefore yields

\[
N
<
\frac{Ry}{2^R\{\log(y/(4P))+0.8601\}}.
\tag{8}
\]

On the other hand, the prime number theorem in the fixed progression `1 mod 4` gives

\[
N
=\left(\frac12+o(1)\right)\frac{y}{\log y}.
\tag{9}
\]

Combining `(8)` and `(9)` proves `(5)`.

If `4P>=y`, then `log(y/P)<=log 4`, so `(3)` holds trivially after enlarging the absolute `O(1)` term. This proves the unified statements `(3)` and `(4)`.

## 3. Critical rank converts the bound into polylogarithmic proximity to the shell

Suppose

\[
2^R=(\kappa+o(1))\log y
\]

for fixed `kappa>0`. Then

\[
R
=\frac{\log\log y}{\log2}+O(1),
\]

and the main term on the right of `(3)` is

\[
(2+o(1))\frac{R}{\kappa}
=
\left(\frac{2}{\kappa\log2}+o(1)\right)\log\log y.
\]

Exponentiating gives `(6)`.

The point is not the numerical constant `2/log 2`; it is the change of scale. `MC-293`--`MC-300` forced most selected modes beyond quasi-subpower individual source thresholds. `MC-304` then packaged those modes into one exact radical but left a totient-density branch in which the fixed-modulus large sieve did not itself force `P` to be large. The present support calculation shows that the exact endpoint partition pays an additional collective price: at critical rank, the common radical must already be nearly of shell size before any energy/totient argument is invoked.

## 4. Prior art and novelty boundary

The analytic input is classical. The arbitrary-interval Brun--Titchmarsh inequality used in `(7)` is Tomohiro Yamada's explicit theorem, already audited in `MC-249`; no novelty is claimed for that estimate, the Chinese remainder theorem, or finite-character duality.

A targeted literature check also finds established work where concentration of primes in a small union of cosets of a subgroup of `(Z/qZ)^*` is converted into character bias or sieve obstructions. In particular, modern work on products of primes in arithmetic progressions uses precisely this broad subgroup/coset language. That literature confirms that **prime support in few multiplicative cosets is a standard analytic-number-theory object**, not a Mathia invention.

No source located in this audit states the endpoint-specific composition used here: the exact one-defect sign support from `MC-296`, the common lower-prime radical from `MC-304`, and the resulting short-shell bound `(3)`. No standalone novelty claim is made. The durable delta is the explicit capacity inequality for the current endpoint model.

## Boundaries and falsification tests

- **Exact endpoint partition is load-bearing.** If shell points can have zero, two, or more simultaneous defects, the image of `Theta(mathcal R_y)` can occupy more than `R` sign cells and `(2)` must be replaced by the actual occupied-cell count.
- **Equal defect weights are not needed.** The proof uses only that the defect sets partition the shell, not `d_i=1/R`. The reciprocal equal-weight model is therefore a special case.
- **The common radical is the exact `MC-304` radical.** No new modulus is introduced. Every selected character is induced from its primitive conductor to `P`, and shell primes are coprime to `P`.
- **The `1 mod 4` restriction is used, not discarded.** Passing to modulus `4P` improves the elementary class-counting constant by a factor two compared with summing only modulo `P`.
- **Brun--Titchmarsh is only an upper bound.** The result does not assert equidistribution across the selected cosets, nor does it prove that any actual arithmetic endpoint partition exists.
- **Large radical is not large discriminant.** `MC-303` and `MC-304` keep these currencies distinct; `(3)` constrains `P` directly and does not infer a field-discriminant theorem.
- **The result does not kill the totient branch of `MC-304`.** It narrows it to near-shell radicals. A further theorem must still show that the required sign-cell concentration or totient density is impossible, or extract additional energy/rank from it.
- **No zero-free region is imported.** Apart from the fixed-progression prime number theorem for modulus `4`, the argument uses only the unconditional sieve upper bound `(7)` and exact finite character structure.
- **No estimate for the Mertens function follows.** This is a necessary-condition theorem for one arithmetic realization of the endpoint obstruction.