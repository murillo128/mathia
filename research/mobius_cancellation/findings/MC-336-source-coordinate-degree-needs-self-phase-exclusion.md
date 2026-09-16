# MC-336 — Source-coordinate degree needs self-phase exclusion

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-335` proves that low Walsh degree in the **standard mode coordinates** `a_1,...,a_R` blocks approximate dephasing at the reciprocal endpoint. That restriction is genuine, but it is not invariant under changing to the endpoint's own source-phase coordinates. In the most obvious source coordinates, degree alone immediately collapses.

Continue the reciprocal endpoint notation

\[
G=\mathbf F_2^R,
\qquad
\Xi=G\setminus\{0\},
\qquad
S=\{s_i:=\mathbf1+e_i:1\le i\le R\},
\]

and define the source-phase variables

\[
x_i(a):=(-1)^{a\cdot s_i}.
\tag{1}
\]

A prime `r` in source cell `s_i` has `\chi_a(r)=x_i(a)`. If one declares a coefficient family "low degree" merely because each row entry is a low-degree polynomial in the source phases `x_1,...,x_R`, then the matched filter from `MC-332` has degree **one**:

\[
w_{a,r}=x_i(a)
\qquad(r\text{ in cell }s_i).
\tag{2}
\]

Consequently

\[
w_{a,r}\chi_a(r)=x_i(a)^2=1
\]

for every mode and every prime, so the normalized endpoint output is identically one. Thus

\[
\boxed{\text{source-phase polynomial degree by itself does not constrain dephasing at all.}}
\tag{3}
\]

This exposes the exact loophole: the coefficient attached to source cell `i` is allowed to read the same phase `x_i` that the character factor contributes, and can cancel it locally before any family estimate acts.

There is, however, a sharp finite repair. Impose **self-phase exclusion**: for a prime in cell `s_i`, its coefficient may depend on the other source phases but not on `x_i`. For even `R`, also impose source-polynomial degree at most `d`. Then the entire normalized output space is exactly

\[
\boxed{
\mathcal L_d
=
\operatorname{span}\left\{
 x_K:=\prod_{j\in K}x_j:
 1\le |K|\le d+1
\right\}.
}
\tag{4}
\]

Write `N=2^R`, `m=N-1`, and

\[
q_d:=\sum_{k=d+2}^{R}\binom Rk.
\tag{5}
\]

For `0\le d\le R-2`, the best possible approximation to exact all-nonprincipal dephasing then satisfies

\[
\boxed{
\inf_{F\in\mathcal L_d}
\sum_{a\in\Xi}|F(a)-1|^2
=
\frac{Nq_d}{q_d+1}.
}
\tag{6}
\]

Hence any genuinely low-degree self-phase-excluded source architecture, in particular `d=o(R)`, has normalized RMS error tending to one. Even at `d=R-2`, where every source monomial except the top one is available, the normalized squared error is

\[
\frac{N}{2(N-1)}=\frac12+o(1).
\tag{7}
\]

Exact punctured-cube dephasing first becomes possible at

\[
d=R-1.
\tag{8}
\]

Therefore the useful source-natural restriction is not "low degree" alone. It is **low degree after forbidding direct access to the phase of the source coordinate being weighted**. This separates two notions that `MC-335` could otherwise be read as conflating: low degree in an externally fixed mode basis is anti-programmable, while low degree in the endpoint evaluation variables is completely programmable unless self-phase leakage is excluded.

No estimate for `M(x)` follows.

## 1. Why source-coordinate degree one already contains the matched filter

For every source cell `i`, equation `(1)` is exactly the character evaluation on that cell. Taking the coefficient in `(2)` gives

\[
F(a)
:=
\frac1A\sum_{r\in\mathcal A}w_{a,r}\chi_a(r)
=
\frac1A\sum_{r\in\mathcal A}1
=1.
\tag{9}
\]

No rank, energy, asymptotic, or approximation argument is involved. The coefficient is one source variable, so it has multilinear degree one in the `x`-coordinates. This works for every `R` and does not require the `x_i` to be independent coordinates.

The contrast with `MC-335` is exact. In the standard `a`-coordinates,

\[
x_i(a)=(-1)^{a\cdot s_i}
\]

is the Walsh character indexed by `s_i=\mathbf1+e_i`, whose Hamming weight is `R-1`. The same matched filter is therefore degree `R-1` in `a` but degree `1` in `x`.

So Fourier degree is not a coordinate-free complexity measure here. A linear change of `\mathbf F_2` coordinates preserves the character group but can move a frequency from Hamming weight `R-1` to weight `1`. Any source-natural coefficient class must specify **which variables are admissible inputs and which local phase is forbidden**, not merely quote a degree bound.

## 2. Even `R` makes the endpoint source phases independent coordinates

For the repaired theorem, assume `R` is even. Let `M` be the `R\times R` binary matrix whose columns are the source vectors `s_i`. Then

\[
M=I+J
\tag{10}
\]

over `\mathbf F_2`, where `J` is the all-ones matrix.

If `Mc=0`, writing `t=\sum_i c_i` gives

\[
c=t\mathbf1.
\tag{11}
\]

Summing the coordinates of `(11)` yields `t=Rt`. For even `R`, this forces `t=0`, hence `c=0`. Therefore

\[
\boxed{M\text{ is invertible when }R\text{ is even}.}
\tag{12}
\]

It follows that

\[
a\longmapsto (x_1(a),\ldots,x_R(a))
\tag{13}
\]

is a bijection from `G` to `\{\pm1\}^R`. In this parity regime the `x_i` are honest independent Walsh coordinates, so ordinary multilinear degree in the source variables is unambiguous.

This parity restriction is only needed for the exact repaired-space calculation. The degree-one collapse `(2)`--`(3)` holds for odd `R` as well.

## 3. Self-phase exclusion gives an exact reachable subspace

Fix a prime `r` in cell `s_i`. Assume its coefficient has the form

\[
w_{a,r}=g_r(x_1(a),\ldots,\widehat{x_i(a)},\ldots,x_R(a)),
\tag{14}
\]

where the hat denotes omission and `g_r` is a multilinear polynomial of degree at most `d`.

Multiplying by the character phase contributes one factor `x_i`, so every monomial produced by this prime is

\[
x_i x_T=x_{T\cup\{i\}},
\qquad
i\notin T,
\qquad
|T|\le d.
\tag{15}
\]

Hence every output lies in the right-hand side of `(4)`: its Fourier support contains only nonconstant source monomials of degree at most `d+1`.

Conversely, take any nonempty `K\subseteq[R]` with `|K|\le d+1`. Choose `i\in K` and one endpoint prime `r` from cell `s_i`. Setting all other coefficients to zero and choosing

\[
g_r=A\,x_{K\setminus\{i\}}
\tag{16}
\]

realizes the normalized output `x_K`. Every source cell occurs at the reciprocal endpoint, so all such monomials are realizable. This proves the exact equality `(4)`.

The missing constant mode is the algebraic expression of self-phase exclusion. Without the restriction, choosing `g_r=x_i` makes `(15)` the constant `x_i^2=1`, which is precisely the matched-filter collapse.

## 4. Exact punctured-cube error and the sharp threshold

Because `(13)` is a coordinate bijection for even `R`, the source monomials `x_K` are the ordinary Walsh basis. The allowed frequencies are all subsets of sizes `1,...,D`, where

\[
D=d+1.
\]

The missing frequency set consists of the constant mode together with every subset of size greater than `D`. Thus there are `q_d+1` missing characters, with `q_d` as in `(5)`.

The punctured target is the function equal to one at every nonprincipal mode while the principal value is unpenalized. Exactly as in the inverse-Gram calculation of `MC-335`, restrictions of any `q_d+1` distinct Walsh characters to the punctured cube have Gram matrix

\[
N I_{q_d+1}-\mathbf1\mathbf1^*.
\tag{17}
\]

Minimizing over the free principal value therefore gives

\[
\inf_{F\in\mathcal L_d}
\sum_{a\ne0}|F(a)-1|^2
=
\frac{Nq_d}{q_d+1},
\tag{18}
\]

which proves `(6)`.

Several thresholds follow immediately.

If `d=o(R)`, then `q_d/N\to1`, so

\[
\frac1{N-1}
\inf_{F\in\mathcal L_d}
\sum_{a\ne0}|F(a)-1|^2
\to1.
\tag{19}
\]

If `d=R-2`, only the top monomial `x_{[R]}` remains missing besides the constant, so `q_d=1` and `(7)` follows.

At `d=R-1`, every nonconstant source character is available. The function

\[
F_*(x)=-\sum_{\varnothing\ne K\subseteq[R]}x_K
\tag{20}
\]

satisfies

\[
F_*(x)=1
\quad\text{for }x\ne(1,\ldots,1),
\qquad
F_*(1,\ldots,1)=-(N-1),
\tag{21}
\]

because `\sum_K x_K=\prod_i(1+x_i)`. Therefore exact nonprincipal dephasing is possible at `d=R-1`, proving the sharp threshold `(8)`.

## 5. What changed relative to `MC-335`

`MC-335` remains correct: bounded degree in the standard mode bits `a_i` excludes the matched filter because each endpoint source phase is a high-degree Walsh character in that basis. The new point is that calling this restriction "source-natural" requires care.

The endpoint itself presents the evaluations `x_i=\chi_a(s_i)` as especially natural observables. In those coordinates the dangerous matched filter is the simplest possible nonconstant function. Thus a generic statement such as "coefficients depend polynomially and at low degree on source character data" is **not** an admissible replacement for the `a`-coordinate degree condition.

Self-phase exclusion repairs the problem for a precise reason: the weight attached to source `i` cannot read the exact bit that multiplication by `\chi_a(r)` will expose. The coefficient can use cross-source information, but it cannot locally invert its own observation. The resulting reachable space loses the constant mode and, at low degree, most high-order source modes as well.

This gives a sharper admission test for the live frontier. A proposed analytic joint coefficient class should be checked in this order:

1. identify the actual source variables available to each prime coefficient;
2. test whether the coefficient can read its own character phase or an algebraically equivalent local decoder;
3. only after that leakage test, measure degree, energy, variation, rank, or conditioning.

A low degree bound without step 2 can certify the matched filter itself.

## 6. Prior art and novelty boundary

The harmonic analysis used here is classical. Walsh characters are the characters of `\mathbf F_2^R`; every function on the Boolean cube has a multilinear Fourier expansion; Fourier degree is the largest monomial size with nonzero coefficient. Ryan O'Donnell, *Analysis of Boolean Functions* (Cambridge University Press, 2014; DOI `10.1017/CBO9781139814782`, author PDF available from Carnegie Mellon) is a standard reference and was already used as the Boolean-Fourier prior-art boundary in `MC-335`.

The dependence of Hamming-weight degree on a chosen coordinate basis is also elementary: an invertible linear change of `\mathbf F_2^R` permutes Fourier characters but need not preserve the Hamming weight of their frequency labels. No novelty is claimed for this fact, for leave-one-coordinate functional dependence, or for the punctured-cube projection calculation.

A targeted literature search on 16 September 2026 found the standard Boolean-Fourier framework and low-degree function literature, but no external theorem is required for `(2)`--`(21)`. The durable Mathia delta is the endpoint-specific **self-phase leakage diagnosis** and the exact self-phase-excluded reachable-space threshold. It narrows what a "source-natural low-complexity" coefficient class can mean after `MC-332`--`MC-335`; it is not presented as a new theorem in Boolean analysis.

## Boundaries and falsification tests

- **The degree-one collapse is unconditional in `R`.** It uses only `x_i^2=1` and therefore survives the odd-`R` dependency among source phases.
- **The exact repaired theorem is stated only for even `R`.** Then the one-defect vectors `s_i` form a basis. For odd `R`, `\sum_i s_i=0`, equivalently `\prod_i x_i=1`, and source monomials must be treated on the resulting quotient; `(4)`--`(8)` are not asserted there.
- **Self-phase exclusion is syntactic unless justified by an analytic architecture.** This finding proves what the restriction buys; it does not prove that an arithmetic theorem naturally supplies coefficients with this locality property.
- **Algebraic leakage counts as self-phase access.** A class that omits `x_i` by name but can reconstruct it from other admitted data is not covered. The relevant condition is measurability/function dependence, not notation.
- **No norm constraint is imposed.** Coefficients can be arbitrarily large. The obstruction comes from missing Fourier modes, so energy and variation remain independent resources exactly as in `MC-333`--`MC-335`.
- **The target is the spread all-nonprincipal dephasing vector.** Sparse mode targets or different endpoint geometries require a new capacity calculation.
- **The theorem is finite and endpoint-specific.** It does not itself provide a prime-family analytic estimate or transfer to `M(x)`.
- **No zero-free information or RH-equivalent bound is imported.** The argument is finite linear algebra and Walsh analysis.

## Consequence for the research line

The live frontier is narrower than `MC-335` alone suggests. There are now two distinct degree models:

- low degree in fixed mode bits `a_i`, which genuinely blocks endpoint dephasing;
- low degree in source evaluation phases `x_i`, which fails already at degree one unless own-phase access is forbidden.

The next useful analytic coefficient architecture should therefore expose a **non-circular locality rule**—ideally one forced by how the coefficient is constructed from prime/source data—under which own-phase or equivalent matched-filter leakage is impossible. Only then do low degree, energy, cross-mode variation, and conditioning become meaningful capacity budgets rather than coordinate artifacts.

That requirement is stronger but more concrete: the research program no longer needs merely a low-complexity joint coefficient family; it needs one whose information flow prevents each source from cancelling its own character observation.