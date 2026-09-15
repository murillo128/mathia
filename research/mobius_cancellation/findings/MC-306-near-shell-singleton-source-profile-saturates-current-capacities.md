# MC-306 — A near-shell singleton-source profile simultaneously saturates the current endpoint capacity constraints

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-REFINEMENT` · `MATCHED-CONTROL` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the reciprocal endpoint frontier of `MC-296` and `MC-301`–`MC-305`. The surviving necessary conditions are not algebraically contradictory at the critical rank. There is an explicit matched source profile in which the rank, primitive-conductor scale, common radical, totient density, multiquadratic discriminant, endpoint Fourier energy, and quotient-cell capacity all occupy the ranges allowed by the existing theorems.

Fix a constant `kappa>0`. For each sufficiently large integer `R`, put

\[
y=\exp(2^R/\kappa),
\qquad
z=y^{1/R}.
\tag{1}
\]

Thus

\[
2^R=\kappa\log y,
\qquad
R=\frac{\log\log y}{\log2}+O(1),
\qquad
\log z=(\log2+o(1))\frac{\log y}{\log\log y}.
\tag{2}
\]

Choose `R` distinct odd primes

\[
p_1,\ldots,p_R\in[z,2z]
\tag{3}
\]

and define independent primitive quadratic characters

\[
\chi_i(n)=\left(\frac n{p_i}\right),
\qquad
X=\langle\chi_1,\ldots,\chi_R\rangle,
\qquad
P=\prod_{i=1}^R p_i.
\tag{4}
\]

Such a choice exists for all sufficiently large `R` by the prime number theorem, because `z/log z` grows much faster than `R`.

Then the following hold simultaneously.

First, the common squarefree radical is already at the shell scale but no larger than a logarithmic factor beyond it:

\[
\boxed{
y\le P\le 2^R y=\kappa y\log y.
\ }
\tag{5}
\]

Moreover the radical is maximally totient-rough in the asymptotic sense

\[
\boxed{
\frac{\varphi(P)}P
=\prod_{i=1}^R\left(1-\frac1{p_i}\right)
=1-o(1).
}
\tag{6}
\]

Second, every nontrivial product character

\[
\chi_I=\prod_{i\in I}\chi_i,
\qquad \varnothing\ne I\subseteq[R],
\]

is primitive of conductor

\[
q_I=\prod_{i\in I}p_i\ge z.
\tag{7}
\]

Hence, after shrinking the absolute Page constant in `MC-293` if necessary so that its `kappa_0<log 2`, the complete nontrivial character subgroup lies above the Page source scale at the level of primitive conductors:

\[
\boxed{
q_I>
D_y:=\exp\!\left(\kappa_0\frac{\log y}{\log\log y}\right)
\qquad(I\ne\varnothing)
}
\tag{8}
\]

for all sufficiently large `R`.

Third, the conductor-discriminant identity of `MC-304` gives exactly

\[
\boxed{|D_K|=P^{2^{R-1}}.}
\tag{9}
\]

Thus the multiquadratic discriminant can be enormous while its entire finite ramification support remains concentrated in a radical of size `y^{1+o(1)}`.

Fourth, impose only the **abstract reciprocal endpoint law** on the selected quotient: give equal mass `1/R` to the `R` sign vectors having exactly one `+1` coordinate. Its selected Fourier energy is exactly the value already computed in `MC-301`,

\[
E_X=\frac{2^R}{R}
=\frac{\kappa\log y}{R}.
\tag{10}
\]

But the fixed-radical large-sieve capacity from `MC-304` has first term

\[
\log y\,\frac{\varphi(P)}P
=(1-o(1))\log y.
\tag{11}
\]

Therefore the endpoint energy fits inside that capacity with an asymptotic factor `R/kappa` of slack. Equivalently, the totient-density escape branch in `MC-304` is satisfied very comfortably:

\[
\frac{\varphi(P)}P
\gg
\frac{2^R}{R\log y}
=\frac\kappa R.
\tag{12}
\]

Finally, the exact quotient map

\[
\Theta:(\mathbb Z/P\mathbb Z)^\times\to\{\pm1\}^R,
\qquad
\Theta(a)=(\chi_1(a),\ldots,\chi_R(a))
\tag{13}
\]

is onto. Every sign cell therefore contains exactly `phi(P)/2^R` reduced residue classes modulo `P`, and the `R` endpoint cells contain

\[
\frac{R\varphi(P)}{2^R}
=(1-o(1))\frac{RP}{\kappa\log y}
\tag{14}
\]

classes. In particular, `(5)` automatically satisfies the near-shell radical requirement of `MC-305`. At the purely residue-class level there is also ample room for balanced endpoint multiplicities: one endpoint cell contains

\[
\frac{\varphi(P)}{2^R}
=(1-o(1))\frac{P}{\kappa\log y}
\ge
(1-o(1))\frac{y}{\kappa\log y}
\tag{15}
\]

classes, whereas a balanced shell partition would ask for only

\[
\frac NR
\sim
\frac{y}{2R\log y}
\tag{16}
\]

shell primes in that cell. The class count exceeds the requested multiplicity by a factor at least `(2/kappa+o(1))R`.

Equations `(5)`–`(16)` prove a precise negative statement about the present frontier: **the scalar source/radical/energy/coset-capacity conditions accumulated in `MC-296` and `MC-301`–`MC-305` admit a common critical-rank model.** They cannot be closed merely by combining their current inequalities more efficiently.

What remains unmodelled is exactly the arithmetic localization step: actual primes in `(y,2y]`, `1 mod 4`, would have to occupy the prescribed one-defect Legendre sign cells for a modulus `P=y^{1+o(1)}`. The construction above proves that the source-side parameters and residue-class cardinalities do not themselves forbid this; it does **not** prove that such shell primes exist.

No estimate for `M(x)` follows.

## 1. Construction of the source profile

With `y,z` as in `(1)`, one has `z->infinity` superpolynomially in `R`. The prime number theorem therefore supplies far more than `R` primes in `[z,2z]`; choose any `R` distinct ones and define `(4)`.

Because the prime conductors are distinct, the `chi_i` are linearly independent as quadratic Dirichlet characters. Every subset product has squarefree primitive conductor `(7)`, and the union of the supports is exactly the radical `P`.

Taking products of the inequalities `z<=p_i<=2z` gives

\[
z^R\le P\le(2z)^R.
\]

Since `z^R=y` and `2^R=kappa log y`, this is `(5)`.

For `(6)`, use

\[
0\le1-\frac{\varphi(P)}P
\le\sum_{i=1}^R\frac1{p_i}
\le\frac Rz
=o(1).
\tag{17}
\]

Thus the radical can simultaneously be near the shell scale and avoid the small-prime harmonic mass that would make `phi(P)/P` small.

## 2. The Page source scale fits inside one singleton conductor

Equation `(2)` gives

\[
\log z
=\frac{\log y}{R}
=(\log2+o(1))\frac{\log y}{\log\log y}.
\tag{18}
\]

The constant in the Landau--Page threshold of `MC-293` was explicitly chosen only to be a sufficiently small positive absolute constant. Replacing it by a smaller constant preserves that theorem. Choose once and for all

\[
0<\kappa_0<\log2.
\tag{19}
\]

Then `(18)` implies `z>D_y` eventually, and every nontrivial subset conductor is at least `z`. This proves `(8)`.

This comparison is intentionally about the **primitive conductor profile of the matched source family**. In the actual `MC-293` shell, the source cost `Q(lambda)` is a minimum over *all* lower-prime representatives that agree on the finite shell. An additional ambient prime could in principle give a cheaper representative of the same shell functional. The present construction does not rule that out and does not replace the actual source-cost map by primitive conductor. Rather, it shows that the conductor/radical side of the persisted necessary conditions has a completely consistent critical-scale model. Any future use of unexpectedly cheap alternative representatives would be genuinely additional arithmetic information.

## 3. Endpoint energy does not exhaust the fixed-radical capacity

For the equal one-defect measure, `MC-296` gives

\[
x_I=(-1)^{|I|}\left(1-\frac{2|I|}{R}\right),
\]

and `MC-301` sums its squares to `(10)`.

The first capacity term in `MC-304` depends only on the reduced-residue density of the common radical. By `(6)` it is asymptotic to `log y`. Thus

\[
\frac{E_X}{\log y\,\varphi(P)/P}
=\frac{\kappa+o(1)}R
\longrightarrow0.
\tag{20}
\]

This identifies an explicit extremal geometry behind the factor-`R` near miss in `MC-301`: a critical-rank endpoint spectrum can coexist with an almost-full-density radical. No sharpening that still pays the entire generic `log y * phi(P)/P` term can exclude this profile.

## 4. Quotient support is algebraically sparse but not cardinality-impossible

Because the characters in `(4)` are independent, finite character duality makes `(13)` onto and gives exactly `phi(P)/2^R` classes per sign vector. The abstract endpoint support uses only `R` of those sign vectors, hence `(14)`.

This realizes the **algebraic** endpoint quotient without requiring a target prime theorem: the required sign cells are nonempty and in fact contain many reduced residue classes. Combining `(15)` with the prime-number-theorem shell size

\[
N\sim\frac{y}{2\log y}
\]

shows that even balanced endpoint multiplicities do not fail for lack of residue classes.

This is not a distribution statement. When `P>=y`, a residue class modulo `4P` may have no representative at all in the short interval `(y,2y]`, much less a prime representative. The missing theorem is precisely about localization of primes into these simultaneous quadratic-sign cells near the conductor scale.

## 5. Prior art and novelty boundary

No new prime-distribution theorem is claimed. The construction uses only the prime number theorem, quadratic-character independence, the Chinese remainder theorem/finite-character duality, and the already-audited inequalities in `MC-293`–`MC-305`.

A targeted literature check found Brandon Hanson, Robert C. Vaughan and Ruixiang Zhang, *The least number with prescribed Legendre symbols and representation by binary quadratic forms of small discriminant*, Journal of Number Theory **179** (2017), 3–16, DOI `10.1016/j.jnt.2017.03.004`. That work studies prescribed vectors of Legendre signs for small **integers**, confirming that simultaneous prescribed-symbol problems are classical; it does not provide the prime-in-a-dyadic-shell statement at modulus `P=y^{1+o(1)}` needed here.

Barnabas Szabo, *On the existence of products of primes in arithmetic progressions*, Bulletin of the London Mathematical Society **56** (2024), 1826–1843, DOI `10.1112/blms.12990`, works explicitly with multiplicative cosets and proves strong coverage results for products of a few primes. Its single-prime input remains Linnik/Brun--Titchmarsh type and likewise does not imply that a dyadic prime shell at `x=P^{1+o(1)}` must visit sign cells omitted by the endpoint support.

Accordingly, **no standalone novelty claim is made** for the ingredients or for prescribed Legendre-symbol language. The durable result is the matched critical-scale compatibility calculation: it identifies exactly which current currencies can coexist and therefore which missing arithmetic coupling cannot be replaced by further algebra on the existing inequalities.

## Boundaries and falsification tests

- **This is a matched source profile, not an arithmetic endpoint realization.** The source primes and characters are genuine, and the quotient sign cells are genuine residue classes, but no claim is made that primes in `(y,2y]` occupy only the one-defect cells.
- **Primitive conductor is not the full shell source cost.** Equation `(8)` concerns the constructed characters themselves. The actual minimum `Q(lambda)` from `MC-293` could be smaller if another lower-prime product agrees on the finite shell. That possibility is outside the matched model and is a legitimate place for new arithmetic rigidity.
- **The radical may sit slightly above the shell.** Equation `(5)` gives `P` between `y` and `kappa y log y`; this is still `y^{1+o(1)}` and lies safely inside the surviving regime of `MC-305`. The construction does not claim the lower bound `(6)` of `MC-305` is sharp in its polylogarithmic exponent.
- **Residue-class capacity is not prime occupancy.** Equation `(15)` only counts available reduced classes. It gives no lower bound for how many of those classes contain a prime in the target shell.
- **The fixed-modulus capacity remains an upper bound.** Showing that `(10)` fits below `(11)` does not assert that the large-sieve bound is attained by actual shell primes.
- **No exceptional-zero assumption is used.** The Page threshold is used only as a comparison scale for primitive conductors; no zero is postulated and no zero-free region is imported into the construction.
- **The no-go is scoped to the persisted scalar package.** A theorem exploiting target-prime localization, the full ambient source-minimization map, finer conductor correlations, or another invariant not present in `(5)`–`(16)` may still kill the endpoint model. That is exactly the remaining research obligation.
- **No estimate for the Mertens function follows.** The finding narrows the next useful theorem surface rather than advancing the final cancellation exponent directly.