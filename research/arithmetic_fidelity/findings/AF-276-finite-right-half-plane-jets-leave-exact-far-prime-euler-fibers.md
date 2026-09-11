# AF-276 — Finite right-half-plane jets leave exact far-prime Euler fibers

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `ARITHMETIC-FIDELITY`, `EULER-GLOBAL`, `FINITE-JETS`, `PRIME-BREADTH`, `POINT-FIBER`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-275 proves that finitely many exact values in `Re(s)>1` do not identify the degree-one rational-prime Euler source: coordinated perturbations of finitely many arbitrarily large prime-local factors can leave all retained values unchanged. Replacing each sampled value by an arbitrary **finite analytic jet** still does not repair that loss.

Fix distinct real sample points

\[
1<\sigma_1<\cdots<\sigma_m,
\tag{1}
\]

nonnegative jet orders

\[
r_1,\ldots,r_m\ge 0,
\qquad
M:=\sum_{j=1}^m(r_j+1),
\tag{2}
\]

and an arbitrary prime cutoff `P_0`. Then there exist

\[
N=M+1
\tag{3}
\]

distinct rational primes

\[
q_1,\ldots,q_N>P_0
\tag{4}
\]

such that, for parameters `a=(a_1,\ldots,a_N)` near

\[
\mathbf1=(1,\ldots,1),
\tag{5}
\]

and

\[
Z_a(s)
:=\zeta(s)
\prod_{\ell=1}^{N}
\frac{1-q_\ell^{-s}}
{1-a_\ell q_\ell^{-s}},
\tag{6}
\]

the simultaneous finite-jet constraints

\[
\boxed{
Z_a^{(k)}(\sigma_j)=\zeta^{(k)}(\sigma_j)
\quad
(1\le j\le m,\ 0\le k\le r_j)
}
\tag{7}
\]

have a nontrivial smooth local solution manifold through `\mathbf1`. With `N=M+1` this manifold has dimension one; with any `N>M` containing an `M`-prime full-rank block, its local dimension is `N-M`.

The primes in `(4)` can be chosen beyond every prescribed cutoff. After shrinking the parameter neighborhood, every `a_\ell` remains positive and below `q_\ell`, so every modified local factor stays degree one and holomorphic/nonzero on `Re(s)>1`. Every nontrivial point of the fiber changes at least one rational-prime Euler coefficient and therefore defines an analytic function distinct from `\zeta`.

Hence no compression consisting of **finitely many values and finitely many derivatives at finitely many right-half-plane points** is locally faithful to the exact prime-local coefficient law in this Euler-product category.

## Exact derivation

### 1. Ordinary jets are equivalent to logarithmic-ratio jets

For `a` in a sufficiently small positive neighborhood of `\mathbf1`, define

\[
H_a(s):=\log\frac{Z_a(s)}{\zeta(s)}
=\sum_{\ell=1}^{N}
\left[
\log(1-q_\ell^{-s})
-\log(1-a_\ell q_\ell^{-s})
\right]
\tag{8}
\]

on `Re(s)>1`, using the real logarithm on the real sample points and its local holomorphic branch nearby. At `a=\mathbf1`, `H_{\mathbf1}\equiv0`.

For a fixed sample `\sigma_j`, the conditions

\[
\partial_s^k H_a(\sigma_j)=0
\qquad(0\le k\le r_j)
\tag{9}
\]

mean that `H_a` has a zero of order at least `r_j+1` at `\sigma_j`. Since

\[
\frac{Z_a}{\zeta}=e^{H_a},
\tag{10}
\]

this is equivalent to

\[
\frac{Z_a(s)}{\zeta(s)}-1
=O((s-\sigma_j)^{r_j+1}),
\tag{11}
\]

and because `\zeta(\sigma_j)\ne0`, `(11)` is equivalent to the ordinary jet equalities `(7)`. Thus it is enough to study the finite map whose coordinates are the logarithmic-ratio jets `(9)`.

Define

\[
F:U\subset\mathbb R^N\longrightarrow\mathbb R^M,
\qquad
F_{j,k}(a):=
\left.\partial_s^k H_a(s)\right|_{s=\sigma_j},
\tag{12}
\]

for `1\le j\le m` and `0\le k\le r_j`. Then `F(\mathbf1)=0`.

### 2. The Jacobian consists of differentiated Euler responses

Differentiating first in the local parameter gives

\[
\left.
\frac{\partial H_a(s)}{\partial a_\ell}
\right|_{a=\mathbf1}
=
\frac{q_\ell^{-s}}{1-q_\ell^{-s}}
=
\frac1{q_\ell^s-1}.
\tag{13}
\]

Therefore

\[
\frac{\partial F_{j,k}}
{\partial a_\ell}(\mathbf1)
=
\left.
\partial_s^k\frac1{q_\ell^s-1}
\right|_{s=\sigma_j}.
\tag{14}
\]

For a prime `q`, put

\[
g_{\sigma,k}(q)
:=
\left.
\partial_s^k\frac1{q^s-1}
\right|_{s=\sigma}.
\tag{15}
\]

Since for `\sigma>1`

\[
\frac1{q^s-1}
=\sum_{n\ge1}q^{-ns},
\tag{16}
\]

termwise differentiation gives the exact expansion

\[
g_{\sigma,k}(q)
=(-\log q)^k
\sum_{n\ge1}n^k q^{-n\sigma}.
\tag{17}
\]

For every fixed `\sigma>1` and `k\ge0`, as `q\to\infty`,

\[
g_{\sigma,k}(q)
=(-\log q)^kq^{-\sigma}
+O_{\sigma,k}\!\left((\log q)^kq^{-2\sigma}\right).
\tag{18}
\]

Thus the rows of the Jacobian carry a lexicographic asymptotic signature: first by decay exponent `\sigma`, then by polynomial degree in `\log q`.

### 3. All finitely many jet-response functions are independent on every prime tail

Consider the `M` functions

\[
\mathcal G
:=
\{g_{\sigma_j,k}:1\le j\le m,\ 0\le k\le r_j\}
\tag{19}
\]

restricted to primes `q>P_0`. Suppose there were a nontrivial relation

\[
\sum_{j=1}^m
\sum_{k=0}^{r_j}
 c_{j,k}g_{\sigma_j,k}(q)=0
\tag{20}
\]

for every prime `q>P_0`.

Choose the smallest `\sigma_*` among sample points having a nonzero coefficient, and among the coefficients at that `\sigma_*` choose the largest derivative order `k_*` with nonzero coefficient `c_{*,k_*}`. Multiply `(20)` by

\[
\frac{q^{\sigma_*}}
{(-\log q)^{k_*}}
\tag{21}
\]

and let `q\to\infty` through the primes. By `(18)`:

- the selected term tends to `c_{*,k_*}`;
- terms at the same `\sigma_*` with smaller derivative order vanish by powers of `1/\log q`;
- terms at larger sample exponents vanish exponentially relative to `q^{-\sigma_*}`, even after multiplication by any fixed power of `\log q`.

The scaled left side must remain zero, so its limit is zero, contradicting `c_{*,k_*}\ne0`. Therefore the `M` functions in `(19)` are linearly independent on **every** prime tail.

As in AF-275, the elementary evaluation lemma now applies: linearly independent real-valued functions on a set have evaluation vectors spanning their coefficient space. Hence there exist `M` distinct primes

\[
q_1,\ldots,q_M>P_0
\tag{22}
\]

for which the square matrix

\[
\left[
 g_{\sigma_j,k}(q_\ell)
\right]_{
 (j,k),\ell
}
\tag{23}
\]

is invertible. Choose one more distinct prime `q_{M+1}>P_0`. The full `M\times(M+1)` Jacobian of `F` at `\mathbf1` has rank `M`.

No quantitative theorem on prime gaps or prime distribution is required. Infinitude of the rational primes is enough because the rank separation comes from the asymptotic hierarchy in `(18)`.

### 4. The regular-level-set theorem gives an exact finite-jet collision fiber

Full row rank at `\mathbf1` makes `F` a submersion there. The regular-level-set / implicit-function theorem therefore gives

\[
F^{-1}(0)
\tag{24}
\]

as a smooth local submanifold of dimension

\[
N-M=1
\tag{25}
\]

through `\mathbf1`. It contains nontrivial parameters arbitrarily close to `\mathbf1`. By the equivalence in `(9)`–`(11)`, every such parameter satisfies the full collection of ordinary jet equalities `(7)` exactly.

The same argument works with any `N>M` selected primes as soon as the set includes an `M`-prime full-rank block; the local collision fiber then has dimension `N-M`.

Finally, if `a\ne\mathbf1`, choose any selected prime `q_*` with `a_*>1` or `a_*<1`. The coefficient of `q_*^{-s}` in the absolutely convergent Dirichlet series of `Z_a` is `a_*` rather than `1`. Hence `Z_a` and `\zeta` are genuinely different analytic Euler sources despite having identical retained finite jets.

## What this adds to AF-275

AF-275 rules out finite **value** sampling. A natural escape is to retain local analytic shape as well: at each sample point keep `Z`, `Z'`, `Z''`, and as many higher derivatives as desired. AF-276 closes every such escape of **fixed finite order**.

The obstruction is not that an individual scalar value is too weak. It is the finite dimensionality of the retained local analytic data compared with the independently perturbable prime-local directions. Derivatives increase the number of constraints, but each finite derivative budget merely replaces the AF-275 response family

\[
q\mapsto(q^\sigma-1)^{-1}
\tag{26}
\]

by finitely many differentiated responses whose distinct `q^{-\sigma}(\log q)^k` asymptotics still furnish a full-row-rank finite observation map and therefore still leave a positive-dimensional fiber once one more prime coordinate is exposed.

This sharpens the hierarchy

\[
\text{full analytic function}
\quad\text{versus}\quad
\text{finite local analytic data}.
\tag{27}
\]

An arbitrarily high but finite Taylor budget at finitely many points remains on the non-faithful side. The identity theorem becomes relevant only when the retained data cease to be finite in this sense—for example, a full germ at one point or values on a set with an interior accumulation point determine the analytic function in the connected domain.

## Prior art and novelty assessment

The proof deliberately uses classical ingredients.

- NIST DLMF §27.4 records the standard Euler-product/Dirichlet-series correspondence for multiplicative and completely multiplicative coefficient laws in an absolute-convergence region: https://dlmf.nist.gov/27.4 .
- The derivative constraints are a Hermite/confluent interpolation pattern. Confluent Vandermonde systems and Hermite interpolation are classical; for one representative reference see Hao Lu, *A Generalized Hilbert Matrix Problem and Confluent Chebyshev--Vandermonde Systems*, SIAM J. Matrix Anal. Appl. 19 (1998), 253–276, DOI `10.1137/S0895479896307221`.
- The asymptotic functions `x^k e^{-\sigma x}` appearing after `x=\log q` belong to the classical generalized-exponential / Chebyshev-system landscape; see Samuel Karlin and William J. Studden, *Tchebycheff Systems: With Applications in Analysis and Statistics*, Interscience, 1966. The argument above does not need the full theory because the lexicographic tail limit proves precisely the required independence.
- The conversion of full Jacobian rank into an exact positive-dimensional level set is the standard regular-level-set / implicit-function theorem, already used and sourced in AF-007, AF-023, and AF-275.
- Helson-zeta literature demonstrates much broader flexibility of prime-local phases under analytic continuation—for example I. Bochkov, *Helson zeta functions for characters with finitely many values*, Bull. London Math. Soc. 55 (2023), 2233–2241, DOI `10.1112/blms.12847`—but that literature is not needed for the present finite-jet theorem and should not be read as its source.

A targeted search did not expose a standard named theorem whose statement is exactly the source-specific boundary above: arbitrary finite right-half-plane jets of a finitely perturbed, degree-one Euler product at the zeta source fail to recover the exact rational-prime local coefficients, with the perturbation block movable beyond every prime cutoff. No broad novelty is claimed. The interpolation, generalized-exponential independence, Euler-product algebra, and differential-topology mechanisms are classical; the Mathia contribution is the explicit **fidelity boundary** obtained by combining them with AF-275's prime-breadth question.

## Boundaries and failure modes

- The theorem concerns finitely many **real** sample points `\sigma_j>1` and finite derivative orders. It does not claim the same rank statement for arbitrary complex sampling configurations, although analogous complex versions may be accessible.
- The local parameters are real and positive near `1`. Prime locations remain the ordinary rational primes and all local factors remain degree one, but the deformation does not preserve `|a_p|=1`, automorphy, a functional equation, analytic continuation to the critical strip, or another rigid global `L`-function category.
- The theorem is exact, not uniformly conditioned. The full-rank determinant can become very small as the chosen perturbation primes move outward. Finite-precision recoverability is a separate problem.
- A full infinite jet at one point is outside the theorem. For analytic functions it determines the local germ and, by continuation in a connected domain, the whole function. The result therefore does not contradict analytic uniqueness.
- The theorem does not say that finitely many zeros, spectral invariants, explicit-formula observables, nonlinear moments, or other destination categories have the same Jacobian. Each requires its own fidelity audit.
- The perturbations change finitely many Euler factors. No infinite-tail perturbation is constructed.
- The theorem has no direct implication for the truth or falsity of RH.

## Decisive audit test

For an RH-facing proposal that claims to preserve exact arithmetic information using finitely many local analytic measurements of an Euler/L-function, count the effective real jet constraints and expose more independently admissible prime-local coordinates than that count. Then compute the prime-response Jacobian rather than assuming derivatives restore provenance.

In the degree-one family `(6)`, the rows are exactly `(14)`, and `(18)` proves that every finite collection is independent on every sufficiently remote prime tail. Thus the Jacobian can be made full row rank while retaining one or more extra prime coordinates, forcing an exact collision manifold.

Any proposed route that evades AF-276 must therefore identify an additional global relation that removes these independent local directions, retain genuinely infinite analytic information, or use a destination whose structure is not reducible to finitely many jets.

## Consequence for the research line

AF-274 removes unbounded **local prime-power depth** when Euler degree is bounded. AF-275 then shows that finitely many global values do not remove **prime breadth**. AF-276 strengthens that boundary: no fixed finite amount of Taylor data at finitely many right-half-plane points removes prime breadth either.

The live gate remains cross-prime rigidity, but its formulation is now harder to evade by enriching scalar samples locally. A candidate finite-dimensional compression must do more than retain values plus derivatives; it must impose or preserve a theorem-level coupling among prime-local coordinates strong enough to destroy the exact far-prime fibers constructed here.