# MC-338 — Source-observation leakage controls dephasing energy

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-336` and `MC-337` show that a source coefficient must not merely omit its own phase syntactically: what matters is whether that phase can be reconstructed from the information the coefficient is allowed to observe. There is a coordinate-invariant quantitative form of that requirement, and it couples directly to the Frobenius-energy currency of `MC-333`.

Work at the exact reciprocal endpoint. Let

\[
G=\mathbf F_2^R,
\qquad
\Xi=G\setminus\{0\},
\qquad
m=|\Xi|=2^R-1,
\]

and write

\[
x_i(a)=(-1)^{a\cdot s_i},
\qquad
s_i=\mathbf1+e_i.
\tag{1}
\]

Assume the `A` shell primes are equally distributed among the `R` source cells. For a prime `r` in source cell `i`, let the mode-dependent coefficient `w_{a,r}` belong, as a function of `a\in\Xi`, to a closed admissible subspace

\[
\mathcal H_i\subset L^2(\Xi),
\tag{2}
\]

where `L^2(\Xi)` uses the uniform probability measure on the nonprincipal modes. Define normalized coefficient energy

\[
\mathcal E(W)
:=\frac1A\sum_{r\in\mathcal A}\|w_{\cdot,r}\|_{L^2(\Xi)}^2
=\frac{\|W\|_F^2}{A m}.
\tag{3}
\]

Thus the unrestricted matched filter from `MC-332` has `\mathcal E(W)=1`.

Let `P_i` be orthogonal projection onto `\mathcal H_i`, and define the **own-phase leakage**

\[
\rho_i:=\|P_i\overline{x_i}\|_{L^2(\Xi)},
\qquad
\rho^2:=\frac1R\sum_{i=1}^R\rho_i^2.
\tag{4}
\]

For the normalized endpoint output

\[
F_W(a):=\frac1A\sum_{r\in\mathcal A}w_{a,r}\chi_a(r),
\tag{5}
\]

write its all-nonprincipal RMS dephasing error as

\[
\delta(W):=\|F_W-1\|_{L^2(\Xi)}.
\tag{6}
\]

Then every admissible coefficient family satisfies the exact information-energy obstruction

\[
\boxed{
\delta(W)\ge
\bigl(1-\rho\sqrt{\mathcal E(W)}\bigr)_+.
}
\tag{7}
\]

Equivalently, whenever `\rho>0`,

\[
\boxed{
\mathcal E(W)\ge
\frac{(1-\delta(W))_+^2}{\rho^2}.
}
\tag{8}
\]

In particular, exact all-mode dephasing requires

\[
\boxed{
\mathcal E(W)\ge\rho^{-2}.
}
\tag{9}
\]

This makes own-phase access an invariant resource rather than a coordinate convention. If `\mathcal H_i=L^2(\sigma(Y_i))` for some source observation `Y_i`, then

\[
P_i\overline{x_i}
=\mathbf E[\overline{x_i}\mid Y_i],
\tag{10}
\]

so `\rho_i` is exactly the `L^2` predictability of the omitted phase from the admitted observation. Any invertible re-encoding of `Y_i` leaves `(10)` unchanged.

For quotient observations there is an exact dichotomy. Suppose `Y_i` records the coset in `G/K_i`, with `k_i:=|K_i|\ge2`, restricted to `\Xi`. Then

\[
\boxed{
\rho_i^2=
\begin{cases}
1, & x_i|_{K_i}\equiv1,\\[2mm]
\displaystyle\frac1{m(k_i-1)}, & x_i|_{K_i}\not\equiv1.
\end{cases}
}
\tag{11}
\]

Thus if the own phase really factors through the observation, the matched filter is present. If it does not, deleting the principal mode creates only a tiny leakage through the single punctured identity fiber.

The even/odd distinction of `MC-336`--`MC-337` becomes quantitative immediately. For even `R`, observing **all other source phases** leaves a two-point hidden fiber and does not determine `x_i`; hence

\[
\rho_i^2=\frac1m
\quad\text{for every }i,
\tag{12}
\]

and exact punctured dephasing under self-phase exclusion costs

\[
\boxed{\mathcal E(W)\ge m=2^R-1.}
\tag{13}
\]

So the exact degree-`R-1` escape constructed in `MC-336` is necessarily exponentially ill-conditioned in normalized coefficient energy, even though it is algebraically realizable.

For odd `R`, `MC-337` gives

\[
x_i=\prod_{j\ne i}x_j,
\tag{14}
\]

so all-other-phase observation determines the own phase exactly: `\rho_i=1`. The ordinary matched filter then has `\mathcal E(W)=1` and attains exact dephasing, saturating `(9)`. The parity transition is therefore not only a degree threshold; it is an **information-conditioning transition from leakage `m^{-1/2}` to leakage `1`**.

No estimate for `M(x)` follows. The result is a finite endpoint admission theorem for future source-natural joint coefficient classes.

## 1. Cell averaging reduces the coefficient matrix to source observations without lowering the obstruction

For source cell `i`, define the cell-averaged coefficient

\[
g_i(a):=\frac{R}{A}
\sum_{r\text{ in cell }i}w_{a,r}.
\tag{15}
\]

Because `\mathcal H_i` is linear and every coefficient in that source cell lies in `\mathcal H_i`, we have `g_i\in\mathcal H_i`. Every prime in the cell has character value `x_i(a)`, so `(5)` becomes

\[
F_W(a)=\frac1R\sum_{i=1}^R x_i(a)g_i(a).
\tag{16}
\]

Jensen's inequality inside each equally populated cell gives

\[
\frac1R\sum_i\|g_i\|_2^2
\le
\frac1A\sum_r\|w_{\cdot,r}\|_2^2
=\mathcal E(W).
\tag{17}
\]

Hence it is enough to bound the energy of the `R` source-level functions. This step is important: `(7)` is not restricted to coefficient matrices that are literally constant within a source cell. Arbitrary prime-by-prime variation can only increase the quadratic cost relative to the cell average relevant to the endpoint output.

## 2. The mean target detects exactly the projected own phase

Use the normalized inner product

\[
\langle f,h\rangle_\Xi
:=\frac1m\sum_{a\in\Xi}f(a)\overline{h(a)}.
\tag{18}
\]

Taking the mean of `(16)` gives

\[
\mathbf E_\Xi F_W
=\frac1R\sum_i
\langle g_i,\overline{x_i}\rangle_\Xi.
\tag{19}
\]

Since `g_i\in\mathcal H_i`, only the projection of the own phase onto the admissible information can contribute:

\[
\langle g_i,\overline{x_i}\rangle
=\langle g_i,P_i\overline{x_i}\rangle.
\tag{20}
\]

Cauchy--Schwarz first within each source and then across the `R` sources yields

\[
\begin{aligned}
|\mathbf E_\Xi F_W|
&\le
\frac1R\sum_i\|g_i\|_2\rho_i\\
&\le
\left(\frac1R\sum_i\|g_i\|_2^2\right)^{1/2}
\left(\frac1R\sum_i\rho_i^2\right)^{1/2}\\
&\le \rho\sqrt{\mathcal E(W)}.
\end{aligned}
\tag{21}
\]

On the other hand, if `F_W` is within RMS error `\delta` of the constant target `1`, then

\[
|\mathbf E_\Xi F_W|
\ge
1-|\mathbf E_\Xi(F_W-1)|
\ge 1-\delta.
\tag{22}
\]

Combining `(21)` and `(22)` proves `(7)`--`(9)`.

The key point is that the argument never asks which coordinates were used to describe `\mathcal H_i`. It asks only how much of the inverse source character survives orthogonal projection onto the information actually available to the coefficient. A source model cannot evade the test by renaming variables or replacing them with an invertible encoding.

## 3. For observation sigma-algebras, leakage is conditional predictability

If the admissible coefficient functions are exactly all square-integrable functions of an observation `Y_i`, then

\[
\mathcal H_i=L^2(\sigma(Y_i)).
\]

Conditional expectation is the orthogonal projection from `L^2` onto this closed subspace, giving `(10)`. Consequently

\[
\rho_i^2
=\mathbf E_\Xi
\left|
\mathbf E_\Xi[\overline{x_i}\mid Y_i]
\right|^2.
\tag{23}
\]

For a unit-modulus phase this quantity lies in `[0,1]`. It is zero when the admitted observation carries no linear `L^2` predictability of the phase and one exactly when the phase is measurable from that observation. Intermediate values measure partial leakage.

This is the appropriate invariant replacement for the syntactic phrase "does not depend on `x_i`". Two coordinate descriptions generating the same sigma-algebra have the same `\rho_i`; conversely an algebraic decoder hidden inside apparently different variables is automatically counted because it makes the conditional expectation nonzero or exact.

## 4. Quotient observations have an exact puncture-leakage formula

Let `Y_i(a)=a+K_i` for a subgroup `K_i\le G` of size `k_i\ge2`. First suppose `x_i` is nontrivial on `K_i`. On the full group, the average of the character over every coset vanishes:

\[
\sum_{u\in a+K_i}x_i(u)=0.
\tag{24}
\]

Passing to `\Xi` changes only the identity coset `K_i`, because the principal point `0` is deleted. On every nonidentity coset the conditional mean remains zero. On the punctured identity coset,

\[
\sum_{u\in K_i\setminus\{0\}}x_i(u)=-1,
\]

and therefore

\[
\mathbf E_\Xi[x_i\mid Y_i=K_i]
=-\frac1{k_i-1}.
\tag{25}
\]

That fiber has probability `(k_i-1)/m` under the uniform measure on `\Xi`. Hence

\[
\rho_i^2
=\frac{k_i-1}{m}\frac1{(k_i-1)^2}
=\frac1{m(k_i-1)},
\tag{26}
\]

which is the second case of `(11)`.

If instead `x_i|_{K_i}\equiv1`, then `x_i` is constant on quotient fibers and is itself a function of `Y_i`. Thus its conditional expectation is `x_i`, proving the first case of `(11)`.

This formula separates two effects that were mixed together in the degree language of `MC-336`. **Intrinsic quotient access is all-or-nothing on the full group.** When access is absent, the nonprincipal puncture creates only the precisely quantified leakage `(26)`. Exact target reconstruction can exploit that tiny leak, but `(9)` says doing so requires its reciprocal quadratic energy.

If every source has a nontrivial hidden kernel, `(9)` becomes

\[
\mathcal E(W)
\ge
\frac{R m}
{\displaystyle\sum_{i=1}^R\frac1{k_i-1}}.
\tag{27}
\]

For equal kernel size `k`, this is

\[
\boxed{\mathcal E(W)\ge m(k-1).}
\tag{28}
\]

Larger hidden fibers therefore make puncture-driven dephasing more expensive rather than easier.

## 5. Even-rank source degree has an exact leakage profile

For even `R`, the source phases `x_1,\ldots,x_R` are independent Walsh coordinates on the full cube by `MC-336`. Consider the self-phase-excluded degree-`d` space

\[
\mathcal H_{i,d}
=
\operatorname{span}\{x_T:i\notin T,\ |T|\le d\}
\quad\text{on }\Xi,
\tag{29}
\]

and write

\[
K_d:=\sum_{j=0}^{d}\binom{R-1}{j}.
\tag{30}
\]

Every allowed character has punctured inner product `-1/m` with `x_i`. The Gram matrix of the `K_d` allowed characters on `\Xi` is

\[
\frac1m\left(2^R I_{K_d}-\mathbf1\mathbf1^*\right).
\tag{31}
\]

An elementary inverse-Gram calculation therefore gives

\[
\boxed{
\rho_{i,d}^2
=\frac{K_d}{m(2^R-K_d)}.
}
\tag{32}
\]

Consequently

\[
\boxed{
\delta(W)
\ge
\left(
1-\sqrt{\mathcal E(W)}
\sqrt{\frac{K_d}{m(2^R-K_d)}}
\right)_+.
}
\tag{33}
\]

At maximal self-phase-excluded degree `d=R-1`, `K_d=2^{R-1}` and `(32)` reduces exactly to `\rho^2=1/m`, recovering `(12)`--`(13)`. At lower degree the leakage is smaller still. Thus the degree obstruction of `MC-336` has a separate conditioning interpretation: even before invoking its exact reachable-space theorem, any source-degree architecture with bounded normalized coefficient energy has vanishing ability to create the constant all-mode target.

`MC-336` remains stronger where it proves exact non-reachability for `d<R-1`; `(33)` contributes a different resource statement. At the first degree where exact dephasing becomes algebraically possible, its coefficient cost is already forced to be exponential.

## 6. Odd rank turns the information barrier off exactly when parity reconstructs the phase

For odd `R`, the source phases obey

\[
\prod_{j=1}^R x_j=1.
\]

Therefore

\[
x_i=\prod_{j\ne i}x_j,
\]

so the observation consisting of the other `R-1` source phases determines `x_i` pointwise. In the language of `(23)`,

\[
\rho_i=1.
\tag{34}
\]

Choosing `g_i=\overline{x_i}` for every source gives

\[
F_W=1,
\qquad
\mathcal E(W)=1,
\tag{35}
\]

so the lower bound `(9)` is sharp in this regime.

This exactly identifies what changes between `MC-336` and `MC-337`. For even `R`, the omitted own phase is genuinely hidden on the full source cube and only the deleted principal mode leaks it at size `m^{-1/2}`. For odd `R`, the global parity relation makes the phase fully observable from the other sources. The final-degree collapse is therefore not a coordinate artifact: it is a discontinuous change in the observation sigma-algebra's ability to predict the phase.

## 7. Prior art and novelty boundary

The mechanism behind `(10)` and `(23)` is classical. Conditional expectation is the orthogonal projection from `L^2` onto the closed subspace of functions measurable with respect to a sub-sigma-algebra; standard modern references include Olav Kallenberg, *Foundations of Modern Probability*, 3rd ed., Springer (2021), DOI `10.1007/978-3-030-61871-1`. Quantifying dependence through conditional means and correlation ratios belongs to the classical dependence-measure literature going back to Alfréd Rényi, *On measures of dependence*, Acta Mathematica Academiae Scientiarum Hungaricae **10** (1959), 441--451, DOI `10.1007/BF02024507`.

The finite-group ingredients are equally standard: character averages vanish on a subgroup unless the character is trivial there, and characters factoring through `G/K` are exactly those trivial on `K`. The Walsh-cube specializations and punctured-character Gram matrices are elementary finite Fourier analysis; Ryan O'Donnell, *Analysis of Boolean Functions*, Cambridge University Press (2014), DOI `10.1017/CBO9781139814782`, is a standard reference for the Boolean Fourier language already used in `MC-335`--`MC-337`.

A targeted literature audit on 16 September 2026 found these general projection, dependence, and finite-character frameworks. No novelty is claimed for conditional expectation as projection, correlation-ratio-type predictability, quotient-character factorization, Cauchy--Schwarz, or the inverse-Gram calculation. The durable Mathia delta is their **exact reciprocal-endpoint specialization**: the source-observation leakage `\rho` gives the direct dephasing-energy inequality `(7)`, quotient observations expose the puncture-only leakage `(11)`, and the even/odd source-parity transition becomes an exponential-versus-unit conditioning dichotomy.

## Boundaries and falsification tests

- **The theorem is an endpoint calibration, not a Möbius bound.** It constrains coefficient architectures on the finite reciprocal character family and does not improve `M(x)`.
- **The admissible information class must be fixed independently of the target.** Taking `\mathcal H_i` to contain the own inverse phase by design gives `\rho_i=1` and correctly recovers the unrestricted matched-filter collapse of `MC-332`.
- **Linearity is load-bearing for the projection formulation.** Observation sigma-algebras give a canonical linear space of all measurable coefficient functions. A nonlinear coefficient family not closed under averaging needs its own information-capacity analysis rather than being silently replaced by `(2)`.
- **Equal source-cell populations are used in `(15)`--`(17)`.** Unequal populations give a weighted source average and a corresponding weighted leakage parameter.
- **Energy is measured on the actual nonprincipal family.** Unlike an argument that completes the cube and charges an unobserved principal row, `(3)` uses exactly the Frobenius energy of the coefficient matrix on `\Xi`. The exponential cost in `(13)` is therefore not an artifact of charging the missing mode.
- **The puncture is essential to the small nonzero quotient leakage.** On the full group a nontrivial hidden quotient character has projection exactly zero. Removing the principal point changes only one quotient fiber and produces `(26)`.
- **Small leakage does not prove an arithmetic estimate exists.** A future analytic theorem must still show that its naturally generated coefficient functions lie in, or are well approximated by, a class with controlled `\rho` and controlled energy.
- **The degree profile `(32)` is stated for even `R`.** It uses independent source Walsh coordinates. Odd `R` has the quotient relation of `MC-337` and must not be inserted into the same Gram formula.
- **The lower bound need not be optimal for every admissible subspace.** It uses only the scalar mean of the target. Additional geometry may force larger energy or outright non-reachability, as `MC-336` already does below maximal degree.
- **No zero-free region, explicit formula, or RH-equivalent estimate is used.** The proof is finite Hilbert-space projection and character orthogonality.

## Consequence for the research line

The source-natural joint-coefficient frontier can now be stated without referring to a preferred coordinate system. A candidate architecture must expose an observation class whose **own-phase leakage `\rho` is small for a structural arithmetic reason**, while keeping coefficient energy near the analytic scale at which a useful family theorem could operate. If `\rho` is order one, the matched-filter loophole remains. If `\rho` is exponentially small but the architecture permits reciprocal-exponential energy inflation, the loophole also remains through conditioning.

For the exact reciprocal endpoint, the most natural all-other-source observation already exhibits the full dichotomy: even source rank has only puncture leakage and requires at least `2^R-1` times the matched-filter energy for exact dephasing; odd source rank reconstructs the phase and dephases at baseline energy. The next useful analytic proposal should therefore justify both sides of the budget simultaneously—**limited phase predictability and limited coefficient conditioning**—rather than relying on low rank, low degree, or syntactic variable omission alone.