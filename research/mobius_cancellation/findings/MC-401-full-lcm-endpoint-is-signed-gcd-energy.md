# MC-401 — Full twisted lcm endpoint is a classical signed gcd/divisor energy

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact Selberg/lcm setup of `MC-398`--`MC-400`. Let

\[
C_g(\ell)
=\sum_{\substack{d,e\le B\\[d,e]=\ell}}g(d)g(e),
\qquad
A_\chi(X)=\sum_{\ell\le X}C_g(\ell)\chi(\ell),
\tag{1}
\]

where `g` is supported on `d\le B` and `\chi=\chi_I` is one quadratic source-mode Dirichlet character modulo the common source radical `P`.

Because every lcm `[d,e]` in `(1)` is at most `B^2`, the **full lcm endpoint** has the exact form

\[
A_\chi(B^2)
=\sum_{d,e\le B}g(d)g(e)\chi([d,e]).
\tag{2}
\]

Define

\[
b(d):=g(d)\chi(d)
\tag{3}
\]

and let

\[
\eta_\chi:=\mu *_D \chi
\tag{4}
\]

be the ordinary Dirichlet-convolution Möbius transform of the arithmetic function `\chi`. Then

\[
\boxed{
A_\chi(B^2)
=\sum_{d,e\le B}b(d)b(e)\chi((d,e))
=\sum_{k\le B}\eta_\chi(k)
\left(\sum_{\substack{d\le B\\k\mid d}}b(d)\right)^2.
}
\tag{5}
\]

Thus the complete twisted lcm coefficient is not an unexplained new lcm statistic. It is a classical meet/GCD-matrix quadratic form, diagonalized by divisor incidence and Möbius inversion. For the current quadratic source modes the diagonal weights are explicit. If `p\nmid P`,

\[
\eta_\chi(p^a)
=\chi(p)^a-\chi(p)^{a-1}
=\begin{cases}
0,&\chi(p)=+1,\\
2(-1)^a,&\chi(p)=-1,
\end{cases}
\tag{6}
\]

while for `p\mid P` one has `\eta_\chi(p)=-1` and `\eta_\chi(p^a)=0` for `a\ge2`; those modulus-prime terms make no contribution to `(5)` because `b(d)=0` whenever `(d,P)>1`.

In particular, when the Selberg coefficient is squarefree-supported, only squarefree `k` contribute and, on the unit part,

\[
\eta_\chi(k)=(-2)^{\omega(k)}
\tag{7}
\]

exactly when every prime `p\mid k` has `\chi(p)=-1`, and it vanishes otherwise.

This exact diagonalization **does not provide cancellation or positivity**. The local lcm kernel is already indefinite at a single unit prime with `\chi(p)=-1`: on the indices `{1,p}` it is

\[
\begin{pmatrix}
1&-1\\
-1&-1
\end{pmatrix},
\tag{8}
\]

whose eigenvalues are `\pm\sqrt2`. Conversely, if `\chi(p)=+1` for every unit prime `p\le B`, then `\chi(d)=1` for every unit `d\le B` and `(5)` collapses to

\[
A_\chi(B^2)
=\left(\sum_{\substack{d\le B\\(d,P)=1}}g(d)\right)^2,
\tag{9}
\]

again with no oscillatory gain.

Therefore the **complete endpoint** `A_\chi(B^2)` cannot by itself be the independent lcm-side mechanism sought after `MC-400`. The surviving lcm branch must use additional information about the actual Selberg weight `g`, a genuinely truncated endpoint `A_\chi(X)` with `X<B^2` where the condition `[d,e]\le X` destroys the complete meet-matrix factorization, source-signature distribution beyond the full quadratic form, or another collective estimate not implied by `(5)`. The alternative pre-quadratic retained-variable branch also remains open.

No estimate for `M(x)` follows.

## 1. Lcm-to-gcd conversion for a quadratic source mode

For any pair `d,e`, if either integer is not coprime to `P`, then both sides of

\[
\chi([d,e])=\chi(d)\chi(e)\chi((d,e))
\tag{10}
\]

vanish. If both are units modulo `P`, the identity follows from

\[
de=[d,e](d,e)
\]

and `\chi((d,e))^2=1`, since the source-mode character is quadratic on the unit group. Multiplying `(10)` by `g(d)g(e)` and summing proves the first equality in `(5)`.

The point is that the lcm kernel at the complete endpoint is semimultiplicatively equivalent to the meet/GCD kernel. The source character has not created a new two-variable arithmetic object; it has conjugated a GCD matrix by the diagonal coefficient vector `g(d)\chi(d)`.

## 2. Divisor-incidence diagonalization

By definition of `(4)`, ordinary Möbius inversion gives

\[
\chi(n)=\sum_{k\mid n}\eta_\chi(k).
\tag{11}
\]

Apply `(11)` at `n=(d,e)` in the first form of `(5)`:

\[
\begin{aligned}
A_\chi(B^2)
&=\sum_{d,e\le B}b(d)b(e)
  \sum_{k\mid d,\,k\mid e}\eta_\chi(k)\\
&=\sum_{k\le B}\eta_\chi(k)
  \left(\sum_{\substack{d\le B\\k\mid d}}b(d)\right)
  \left(\sum_{\substack{e\le B\\k\mid e}}b(e)\right),
\end{aligned}
\tag{12}
\]

which is the second equality in `(5)`.

This is the standard incidence factorization of a meet matrix. It is important not to confuse `\eta_\chi=\mu *_D\chi` here with the pointwise function `\mu\chi` in `MC-400`. In `MC-400`, `\mu(n)\chi(n)` is the Dirichlet-convolution inverse of the completely multiplicative sequence `\chi`. Here `\mu *_D\chi` is instead the Möbius transform of the **meet-kernel value** `\chi(n)` used to expand `\chi((d,e))`. They are different arithmetic functions.

For a prime power, `(6)` follows immediately because only the divisors `1` and `p` survive in the convolution with `\mu`:

\[
\eta_\chi(p^a)=\chi(p^a)-\chi(p^{a-1}).
\tag{13}
\]

The squarefree specialization `(7)` then follows multiplicatively.

## 3. Why the diagonal form does not solve the sign problem

Equation `(5)` is an exact decomposition into squares, but its coefficients `\eta_\chi(k)` are signed. It is therefore not a positivity theorem.

The smallest obstruction is `(8)`. Equivalently, restrict the quadratic form `(2)` to coefficients at `1` and a unit prime `p` with `\chi(p)=-1`. For a vector `(x,y)` the contribution is

\[
x^2-2xy-y^2,
\tag{14}
\]

which takes both signs. This is not a pathology introduced by a large modulus, a limiting argument, or a bad normalization; it is already present in one prime coordinate.

At the opposite extreme, if every available unit prime has positive character value, all contributing divisor blocks except `k=1` disappear and `(9)` is a perfect square. Hence neither sign pattern gives a generic cancellation principle: negative source primes produce an indefinite energy, while absence of negative source primes removes the oscillation altogether.

A useful theorem would therefore have to exploit the **specific vector** supplied by the actual Selberg coefficient `g`, or control a truncated/averaged family of such vectors, rather than rely on the lcm/GCD kernel alone.

## 4. Prior art and novelty boundary

Meet/GCD and join/LCM matrices, their incidence factorizations, determinants, inverses, and the role of Möbius inversion are classical. A direct primary prior-art anchor is:

- Ismo Korkee and Pentti Haukkanen, *On meet and join matrices associated with incidence functions*, Linear Algebra and its Applications 372 (2003), 127--153, DOI: https://doi.org/10.1016/S0024-3795(03)00497-X.

The paper treats meet matrices as abstract GCD matrices, join matrices as abstract LCM matrices, and develops incidence-function formulas on the corresponding semilattices. An earlier arithmetic-function GCD-matrix source is Keith Bourque and Steve Ligh, *Matrices associated with arithmetical functions*, Linear and Multilinear Algebra 34 (1993), 261--267, DOI: https://doi.org/10.1080/03081089308818225.

No novelty is claimed for the factorization `(11)`--`(12)` or for meet/join matrix theory. The Mathia-specific contribution is the **frontier specialization**: the exact full endpoint of the post-`MC-400` twisted Selberg lcm coefficient is a classical signed meet-matrix energy, and therefore generic appeals to the complete lcm coefficient as an unexplained independent source of cancellation are not a new mechanism.

The partial endpoint `X<B^2` is intentionally not classified by this result. The mask `[d,e]\le X` couples the pair to the truncation and prevents the immediate replacement of `(2)` by the complete divisor-incidence square sum `(5)`. Likewise, a theorem about the actual Selberg minimizer or source-signature statistics can supply genuinely additional information.

## Boundaries and falsification tests

- **Only the full lcm endpoint is diagonalized in this form.** The finding does not claim that every partial sum `A_\chi(X)` with `X<B^2` reduces to `(5)`.
- **No positivity is inferred from a sum of squares.** The weights `\eta_\chi(k)` are signed and the one-prime kernel `(8)` is indefinite whenever a negative unit prime exists.
- **No assumption that `g` is multiplicative is used.** The exact formula `(5)` holds for any finitely supported coefficient sequence `g`; squarefree support is used only for the simplification `(7)`.
- **The actual Selberg coefficient remains special.** A new theorem showing that its divisor-block vector lands in a favorable cone or exhibits cancellation is outside this obstruction.
- **Source-signature information is not declared useless.** A distribution theorem that is not already encoded by the single full quadratic form remains admissible.
- **Character zeros are handled exactly.** Modulus-prime divisibility kills both the lcm term and the corresponding incidence blocks.
- **No analytic continuation or RH input is used.** The result is finite divisor algebra plus classical meet-matrix structure.
- **No Möbius cancellation bound follows.** This is a representation/frontier classification only.

A proposed counterexample must either show an error in the exact identities `(2)`--`(13)` or supply additional structure not present in the complete lcm kernel itself. A theorem for truncated `A_\chi(X)`, for the actual Selberg `g`, or for a pre-quadratic retained variable is not a counterexample; it is precisely the surviving research direction.

## Consequence for the research line

`MC-400` left open an independent theorem for the twisted lcm coefficient `A_\chi(X)`. The present finding splits that obligation sharply. At the **complete endpoint** `X=B^2`, the object is already a classical signed GCD/divisor energy with explicit source-character weights, and the kernel supplies neither positivity nor generic cancellation. Therefore the generic full-endpoint lcm branch is closed as an independent mechanism.

The accepted retained-variable clue should now concentrate its lcm-side effort on one of three genuinely additional inputs: **truncation before `B^2`, special structure of the actual Selberg weight, or source-signature statistics beyond the complete quadratic form**. If none yields a strict source-depth gain, the remaining route is the genuinely nonseparable pre-quadratic variable already isolated after `MC-399`--`MC-400`.