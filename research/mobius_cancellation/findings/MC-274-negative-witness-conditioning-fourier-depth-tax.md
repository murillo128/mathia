# MC-274 — Negative-witness conditioning spends an atom-scale Fourier-depth tax

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the flat Christoffel source of `MC-268`–`MC-273`. Order the lower-prime coordinates as

\[
\mathcal P_y=\{p_1,\dots,p_k\},
\qquad
x_i(T):=\sigma_{p_i}(T)\in\{-1,+1\},
\]

and write

\[
g_m(x)
:=
\sum_{\substack{S\subseteq[k]\\|S|\le m}}x_S,
\qquad
x_S:=\prod_{i\in S}x_i.
\tag{1}
\]

`MC-273` showed that once a negative witness `x_j=-1` is known, the row value in `(1)` collapses to a homogeneous degree-`m` shell after deleting that coordinate. A natural next move is therefore to choose a negative witness adaptively and partition the target rows according to the first witness found.

That rowwise simplification is **not free at the ensemble level**. Exact conditioning on a witness consumes Fourier/source depth, and at the single-atom scale it consumes parametrically more depth than the original Christoffel detector.

Consider any deterministic coordinate-query procedure which queries distinct lower-prime signs and stops when it sees a negative sign. Along a leaf reached after `j` queries with `j-1` positive answers followed by the negative witness `i_j`, the leaf indicator is

\[
I_j(x)
=
2^{-j}(1-x_{i_j})
\prod_{r=1}^{j-1}(1+x_{i_r}).
\tag{2}
\]

On that leaf, `MC-273` gives

\[
g_m(x)=e_m(x_{\widehat{i_j}}),
\tag{3}
\]

where `e_m` is the degree-`m` elementary symmetric polynomial in all coordinates except the witness. Hence the exact conditioned energy is

\[
I_j(x)g_m(x)^2
=
I_j(x)e_m(x_{\widehat{i_j}})^2.
\tag{4}
\]

Whenever `k-j\ge2m`, the multilinear Walsh degree of `(4)` is **exactly**

\[
\boxed{\deg_{\mathrm W}\big(I_jg_m^2\big)=2m+j.}
\tag{5}
\]

Indeed, choose any `2m` unqueried coordinates `U`. The coefficient of `x_U` in `e_m^2` is `\binom{2m}{m}`, while the coefficient of the product of all `j` queried coordinates in `I_j` is `-2^{-j}`. Therefore the coefficient of the degree-`2m+j` monomial

\[
x_{\{i_1,\dots,i_j\}\cup U}
\]

is exactly

\[
\boxed{-2^{-j}\binom{2m}{m}\ne0.}
\tag{6}
\]

Since a Walsh monomial of degree `d` is precisely a lower-prime source product supported on `d` primes, `(5)` is an exact source-depth statement, not merely abstract Boolean complexity.

The same tax survives summing all witness leaves through a fixed query depth. Along the all-positive path let `i_1,\dots,i_J` be the first `J` queried coordinates and put

\[
R_J(x)
:=
2^{-J}\prod_{r=1}^J(1+x_{i_r}).
\tag{7}
\]

Then

\[
1-R_J(x)=\sum_{j=1}^J I_j(x)
\tag{8}
\]

is exactly the indicator that a negative witness was found by depth `J`, while `R_J` is the unresolved all-positive subcube. Consequently

\[
\sum_{j=1}^J I_j(x)g_m(x)^2
=(1-R_J(x))g_m(x)^2,
\tag{9}
\]

and, if `k-J\ge2m`,

\[
\boxed{
\deg_{\mathrm W}\big((1-R_J)g_m^2\big)=2m+J.
}
\tag{10}
\]

Thus even after the witness cells are recombined, the conditioning depth does not cancel. The unconditioned Christoffel energy has source degree `2m`; exact witness conditioning through depth `J` raises that to `2m+J` and also breaks the radial source symmetry used in `MC-267`–`MC-269`.

There is a second quantitative obstruction. Under the uniform Boolean comparator underlying the binomial/Krawtchouk model,

\[
\mathbb E R_J=2^{-J}.
\tag{11}
\]

If

\[
C=\binom{N_y}{t}
\]

is the number of target-shell rows, then the natural independent-sign comparator leaves

\[
C2^{-J}
\tag{12}
\]

rows unresolved after `J` positive queries. Therefore even an ideal natural-scale estimate

\[
\sum_{|T|=t}R_J(x(T))
\le
L_y C2^{-J}
\tag{13}
\]

can prove that no unresolved row remains only if

\[
\boxed{J>\log_2 C+\log_2 L_y.}
\tag{14}
\]

At the live Christoffel scale

\[
t=\left(\frac1{\log2}+o(1)\right)\log\log y,
\qquad
m=t+1,
\qquad
N_y\sim\frac y{\log y},
\tag{15}
\]

Stirling gives

\[
\log C
=t\log\frac{N_y}{t}+O(t)
=\left(\frac1{\log2}+o(1)\right)
\log y\,\log\log y.
\tag{16}
\]

Hence, for every loss with

\[
\log L_y=o(\log y\,\log\log y),
\]

the atom-scale query depth forced by `(14)` is

\[
\boxed{
J_{\mathrm{atom}}
=
\left(\frac1{(\log2)^2}+o(1)\right)
\log y\,\log\log y.
}
\tag{17}
\]

By comparison,

\[
2m
=
\left(\frac2{\log2}+o(1)\right)\log\log y.
\tag{18}
\]

Thus a witness partition deep enough even for its **ideal independent-sign residual baseline** to fall below one row requires

\[
\boxed{
\frac{2m+J_{\mathrm{atom}}}{2m}
=
\left(\frac1{2\log2}+o(1)\right)\log y,
}
\tag{19}
\]

times the source degree of the original Christoffel energy.

The exact full decision tree is worse still: the all-positive input cannot be certified blind until every coordinate has been queried, and

\[
R_k(x)=2^{-k}\prod_{i=1}^k(1+x_i)
\tag{20}
\]

is exactly the blind-point indicator. Pushing witness conditioning all the way to exact completeness therefore reconstructs the original degree-`k` endpoint projector rather than providing a lower-depth escape.

The durable conclusion is that the adaptive witness suggestion left open by `MC-273` cannot be inserted into the existing support-matched `2m` hierarchy as a free homogeneous-shell reduction. A viable witness-based argument must supply **new anisotropic arithmetic information for conditioned cells directly**, or another mechanism that avoids paying the decision-path depth. Merely expanding the witness conditions back into lower-prime characters loses the low-depth advantage before the atom scale is reached.

No blind relation is excluded, no Christoffel flat-energy estimate is proved, and no new bound for `M(X)` follows.

## 1. The conditioning degree is exact, not an upper-bound artifact

The leaf indicator `(2)` is a conjunction of `j` queried signs. Its Walsh expansion contains every subset of those queried coordinates, and its degree-`j` coefficient is nonzero. This is the standard subcube-indicator representation on the Boolean cube.

The homogeneous shell in `(3)` has

\[
e_m(x_{\widehat{i_j}})
=
\sum_{\substack{S\subseteq[k]\setminus\{i_j\}\\|S|=m}}x_S.
\tag{21}
\]

After multilinearization, the coefficient of `x_U` in `e_m^2` for every `|U|=2m` is `\binom{2m}{m}`: the two size-`m` supports must be disjoint and partition `U`, and there are exactly `\binom{2m}{m}` ordered choices for the first support. Choosing `U` disjoint from all queried coordinates makes the degree-`2m+j` coefficient in `(6)` unique, so no lower-degree cancellation can remove it.

The same argument with the top monomial of `R_J` proves `(10)`. In particular, the degree increase is not caused by bounding the leaf indicators separately; it remains after all first-witness leaves through depth `J` are summed exactly.

## 2. Conditioning also destroys the radial Krawtchouk compression

`MC-267` showed that the unconditioned source hierarchy through degree `2m` is radial: permutation-symmetric source coefficients reduce to the Krawtchouk aggregates `H_{s,y}(t)`, equivalently to the shell histogram of the Hamming weight `b_y(T)`.

The leaf observable `(4)` is not permutation-symmetric in the lower-prime coordinates. It singles out the queried set and the witness coordinate. Its Walsh expansion therefore requires character sums resolved at least by their relation to that specific queried set, not only by total support size.

This gives a second cost beyond `(5)`: the conditioned energy is not determined by the scalar radial data

\[
\{H_{s,y}(t)\}_{s\le2m+j}
\]

through universal Krawtchouk algebra alone. A coordinate permutation preserves every radial `H_s` but moves the fixed witness leaf. Any recovery of `(4)` from actual arithmetic must therefore use a prefix-/support-refined family of character sums or a direct conditional theorem.

So the witness reduction trades one rowwise simplification for two ensemble-level requirements:

1. extra source degree equal to the decision depth;
2. anisotropic information that the existing radial hierarchy intentionally discarded.

Neither requirement is supplied by the homogeneous-shell identity itself.

## 3. The atom-scale depth is much larger than the Christoffel depth

The residual `(7)` is the indicator of a codimension-`J` subcube. Under independent unbiased signs its mass is exactly `2^{-J}`; no approximation theorem is needed for `(11)`.

Equation `(14)` is only a **method threshold**. It does not assert that the actual arithmetic residual count equals `C2^{-J}` or is nonzero when `C2^{-J}\gg1`. It says that a proof comparing the actual residual with its natural independent-sign scale, with multiplicative loss `L_y`, cannot force the integer count below one until the right side itself is below one.

The asymptotic `(17)` then shows why the first-negative route is poorly matched to the current detector budget. The Christoffel polynomial reaches the one-atom binomial scale using all low-degree source monomials—`Z_m(k)` of them—while a single decision path reduces uniform mass only by one factor `1/2` per queried coordinate. Reaching the same atom scale by sequential coordinate conditioning costs order `\log_2 C`, not order `m`.

This remains true for an adaptive query order. Along the all-positive path all previous answers are identical, so the next queried coordinate is fixed by the procedure; after `J` positive answers the unresolved set is still exactly one codimension-`J` subcube with uniform mass `2^{-J}`. No ordering of the coordinates changes `(11)`–`(17)`.

## 4. Prior-art and novelty boundary

Subcube indicators, conjunction expansions, Fourier analysis on the Boolean cube, and the relationship between decision trees and Fourier representations are classical. Ryan O'Donnell's *Analysis of Boolean Functions* (Cambridge University Press, 2014; corrected arXiv edition 2105.10386) is a standard reference for the Walsh/Fourier framework. Eyal Kushilevitz and Yishay Mansour, *Learning Decision Trees Using the Fourier Spectrum*, SIAM Journal on Computing 22 (1993), 1331–1348, DOI `10.1137/0222080`, is classical decision-tree/Fourier prior art. No novelty is claimed for the fact that a depth-`j` leaf is a degree-`j` conjunction or for the exact expansion of a subcube indicator.

A targeted literature check through 13 September 2026 found no basis for treating those Boolean facts as new. The durable Mathia delta claimed here is only their exact specialization to the `MC-273` negative-witness collapse, together with the source-support identity `(5)`–`(6)` and the live atom-scale comparison `(17)`–`(19)`.

## Boundaries

- **Not a universal no-go for conditional arithmetic.** A theorem that estimates first-witness cells directly, without expanding their indicators into the current low-support character hierarchy, lies outside this obstruction.
- **Not a lower bound for the actual residual count.** The comparator calculation `C2^{-J}` is a natural-scale benchmark, not a statement that the arithmetic sign vectors are independent.
- **Not a no-go for non-coordinate selectors.** A genuinely global arithmetic certificate of nonblindness need not be representable as sequential queries of individual `x_i`.
- **Not a contradiction to MC-273.** The rowwise homogeneous-shell identity remains exact and potentially useful; the present result identifies the ensemble-level information cost of making the witness choice explicit.
- **No claim that degree alone measures theorem difficulty.** The point is exact compatibility with the existing source-support hierarchy, whose degree has a concrete arithmetic meaning.
- **No Möbius/RH consequence.** Nothing here rules out blind support or improves `M(X)`.

## Consequence for the research line

`MC-273` narrowed the phase-sensitive frontier to the arithmetic cost of having no negative witness or to an adaptive witness partition. The second option now splits sharply.

If the witness partition is implemented by ordinary lower-prime sign queries and then reduced to the existing character hierarchy, it is not a lower-complexity reformulation: conditioning through depth `J` raises the exact source degree from `2m` to `2m+J`, destroys radial Krawtchouk compression, and requires `J\asymp\log_2 C\asymp\log y\log\log y` before even the independent-sign residual baseline reaches the one-row scale.

The surviving witness route must therefore exploit arithmetic conditioning **before Fourier expansion**—for example, a direct theorem about localized Legendre-sign cells—or replace coordinate witnessing with a global phase-sensitive statistic. Otherwise the `MC-273` collapse merely moves the missing information from the mixed-degree source vector into the conditioning event.