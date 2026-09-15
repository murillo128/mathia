# MC-317 — Random linear erasure list recovery plus constant-dimensional augmentation closes the generic half-rate endpoint

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `MATCHED-CONTROL` · `FRONTIER-CLOSURE` · `NEGATIVE/OBSTRUCTION` · `PRIOR-ART-AUDITED` · `NON-RH`.

## Claim

Let

\[
t_R:=\left\lceil 2\log_2(R+1)\right\rceil.
\]

For all sufficiently large integers `R`, there exists a full-length binary linear code

\[
C_R\le \mathbf F_2^{2R},\qquad \dim C_R=R,
\]

such that

\[
\boxed{d_{t_R}(C_R)\ge R-2.}
\tag{1}
\]

Equivalently, by the exact erasure/generalized-weight dictionary of `MC-313`, every erasure set of size `R-3` leaves at most `t_R-1` dimensions of ambiguity, so every received unerased word has at most

\[
2^{t_R-1}< (R+1)^2
\]

compatible codewords.

Consequently the generic matched-control question isolated in `MC-315` and `MC-316` has an affirmative existence answer: the diagonal projective generalized-cap envelope eventually satisfies `N_R\ge 2R`, and there exist systematic matrices `P_R\in\mathbf F_2^{R\times R}` for which every actual `(g+3)\times g` submatrix has rank at least `g-t_R+1` for all `t_R\le g\le R-3`.

This does **not** prove that the arithmetic source-incidence codes arising in the Möbius program attain `(1)`. It proves the opposite kind of statement needed by the matched-control discipline: **generic binary coding/projective incidence alone cannot rule out the exact natural-scale source regime.** Any future obstruction must use additional arithmetic structure of the source matrices rather than only their length, dimension, generalized weights, projective occupancy, or systematic submatrix-rank profile.

No estimate for `M(x)` follows.

## 1. Finite-blocklength random-linear input

Dean Doron, Jonathan Mosheiff, Nicolas Resch and João Ribeiro, *List-Recovery of Random Linear Codes over Small Fields*, APPROX/RANDOM 2025, LIPIcs 353, article 57, DOI `10.4230/LIPIcs.APPROX/RANDOM.2025.57`, arXiv `2505.05935`, prove a finite-blocklength erasure list-recovery theorem for random linear codes over prime fields. Their Theorem 25 states, in the notation needed here, that for prime `q`, list input size `\ell\le q-1`, erasure fraction `\alpha`, and `\varepsilon>0`, a random linear code of rate

\[
1-\alpha-(1-\alpha)\log_q\ell-\varepsilon
\tag{2}
\]

is list-recoverable from `\alpha n` erasures with list size

\[
L=\frac{C_{q,\ell,\alpha}}{\varepsilon},
\tag{3}
\]

with probability at least `1-q^{-n}`, provided `n\ge L`. For `\ell\le(2/3)q` they give an explicit bound

\[
C_{q,\ell,\alpha}
\le q^{C\log q\,((1-\alpha)\ell+1)}
\tag{4}
\]

for a universal constant `C`.

Specialize to

\[
q=2,\qquad \ell=1,
\qquad n=2R,
\qquad \alpha_R=\frac{R-3}{2R}.
\tag{5}
\]

Because `q=2` and `\ell=1` are fixed and

\[
(1-\alpha_R)\ell+1<2,
\]

equation `(4)` gives an absolute constant `K` such that

\[
C_{2,1,\alpha_R}\le K
\tag{6}
\]

uniformly in `R`.

Choose once and for all an integer

\[
B\ge\max\{K,2\},
\tag{7}
\]

and put

\[
\varepsilon_R=\frac BR.
\tag{8}
\]

For sufficiently large `R`, `0<\varepsilon_R<1`. The rate in `(2)` becomes

\[
\frac{R+3}{2R}-\frac BR
=
\frac{R+3-2B}{2R},
\]

so the random code has the integral dimension

\[
k_0=R+3-2B.
\tag{9}
\]

Its erasure list bound satisfies

\[
L_0
=\frac{C_{2,1,\alpha_R}}{\varepsilon_R}
\le \frac{KR}{B}
\le R,
\tag{10}
\]

and hence the theorem's finite-length condition `n\ge L_0` is automatic because `n=2R`.

Therefore, for every sufficiently large `R`, with positive probability a binary linear `[2R,R+3-2B]` code `C_0` has the following uniform property:

> after **any** `R-3` erasures, every unerased word has at most `R` compatible codewords in `C_0`.

The fact that `\varepsilon_R` is of order `1/R`, rather than a fixed constant, is the decisive point. Earlier fixed-gap erasure-capacity results do not by themselves reach the constant-dimensional deficit needed at the `MC-315` endpoint.

## 2. The random code may simultaneously be chosen full length

The projective formulation of `MC-315` requires that no coordinate be identically zero. This does not cost the existence argument.

For a uniformly random `k_0`-dimensional subspace of `\mathbf F_2^{2R}`, the probability that the entire code lies in one prescribed coordinate hyperplane equals

\[
\frac{{2R-1\brack k_0}_2}{{2R\brack k_0}_2}
=
\frac{2^{2R-k_0}-1}{2^{2R}-1}
=O(2^{-k_0}).
\tag{11}
\]

A union bound over the `2R` coordinates therefore gives

\[
\Pr(C_0\text{ is not full length})
=O(R2^{-k_0})=o(1).
\tag{12}
\]

The erasure theorem fails with probability at most `2^{-2R}`. Hence for all sufficiently large `R` the two good events intersect: one may choose `C_0` both erasure-good and full length.

## 3. Constant-dimensional augmentation reaches exact half rate

The code `C_0` is only a constant number of dimensions below `R`. Define

\[
D:=R-k_0=2B-3,
\tag{13}
\]

which is independent of `R`, and extend `C_0` to any `R`-dimensional supercode

\[
C_0\subset C_R\le\mathbf F_2^{2R}.
\tag{14}
\]

The quotient `C_R/C_0` has exactly `2^D` cosets. Fix an erasure set `E` of size `R-3` and a word on the unerased coordinates. Inside any one coset `v+C_0`, translating by `v` converts the compatibility condition into one for `C_0`, so there are at most `L_0\le R` compatible codewords in that coset. Summing over the cosets gives the exact uniform bound

\[
L(C_R,E)\le 2^D R.
\tag{15}
\]

Full length is preserved because `C_0\subset C_R`.

Now

\[
2^{t_R-1}
\ge \frac{(R+1)^2}{2}.
\tag{16}
\]

Since `D` is an absolute constant, `(16)` implies

\[
2^D R\le 2^{t_R-1}
\tag{17}
\]

for all sufficiently large `R`. Thus every erasure set of size `R-3` leaves list size at most `2^{t_R-1}` in `C_R`.

For a linear code, the list size after erasing `E` is exactly

\[
2^{\dim C_R(E)},
\]

where `C_R(E)` is the shortened subcode supported inside `E`. Hence `(17)` gives

\[
\dim C_R(E)\le t_R-1
\qquad (|E|=R-3).
\tag{18}
\]

By the definition of generalized Hamming weight,

\[
d_{t_R}(C_R)>R-3,
\]

which is the claimed integer inequality `(1)`.

## 4. Translation to the projective and systematic frontiers

`MC-315` proved, for a full `[2R,R]` binary code, that

\[
2R-d_t(C)
=
\max_{\operatorname{codim}U=t} M(U),
\tag{19}
\]

where `M(U)` counts generator columns lying in the codimension-`t` projective subspace `U`. Applying `(1)` at `t=t_R` gives

\[
\max_{\operatorname{codim}U=t_R}M(U)\le R+2.
\tag{20}
\]

Thus the diagonal generalized-cap target of `MC-315` is compatible with `2R` points for all sufficiently large `R`.

`MC-316` proved that the same generalized-weight inequality is equivalent, after putting a parity-check matrix in systematic form `[I_R\mid P_R]`, to

\[
\operatorname{rank}Q\ge g-t_R+1
\tag{21}
\]

for every actual `(g+3)\times g` submatrix `Q` of `P_R` and every

\[
t_R\le g\le R-3.
\]

Therefore the matrices whose existence was left open in `MC-316` do exist for all sufficiently large `R`. No explicit deterministic construction is supplied here; the existence is inherited from the random-linear theorem plus the constant-dimensional augmentation.

## Prior-art and novelty boundary

The random-linear erasure theorem is entirely literature input. No novelty is claimed for random codes approaching erasure list-decoding capacity, generalized Hamming weights, or their erasure interpretation. In particular, `MC-313` already recorded Ding–Jin–Xing's fixed-positive-gap random-linear erasure result and Guruswami's classical generalized-weight/list-decoding framework.

The new durable Mathia step is the **parameter specialization and augmentation at the exact diagonal matched-control frontier** defined by `MC-313`–`MC-316`. The 2025 theorem remains effective when the gap from erasure capacity is chosen as `\varepsilon_R=B/R`; because its binary `\ell=1` constant is uniform in `\alpha_R`, it yields a code only `D=O(1)` dimensions below half rate with list size `O(R)`. Adding those `D` dimensions costs only a constant list-size factor, while the target permits a quadratic list. This closes the generic existence question left open by `MC-315` and `MC-316`.

This materially strengthens the earlier elementary control in `MC-313`. That union bound reached only

\[
d_{t_R}(C)\ge R-O(R/\log R),
\]

whereas the literature-assisted argument reaches the exact constant-defect target `R-2`.

## Boundaries and falsification tests

- **Asymptotic existence only.** The argument gives an unspecified sufficiently-large threshold depending on the universal constant in the random-linear theorem. It does not identify the smallest admissible `R`.
- **No explicit code family.** Existence is probabilistic; no efficiently constructible deterministic `P_R` is produced.
- **No arithmetic realizability.** The source-incidence codes generated by reciprocal-prime subsets are highly structured. Nothing here shows that they sample the generic code ensemble or can realize the constructed controls.
- **No independence heuristic is used.** The argument uses a proved finite-blocklength random-linear theorem, then exact linear-algebraic augmentation. It does not model Möbius signs as independent random variables.
- **The list blow-up is accounted for.** Adding `D` dimensions can increase every erasure list by at most `2^D`; the target list `2^{t_R-1}` is quadratic in `R`, so this fixed factor is eventually harmless.
- **The finite-length hypothesis is checked.** Choosing `B\ge K` makes `L_0\le R<2R=n`, so the theorem is not being extrapolated outside its stated `n\ge L` regime.
- **Full length is not assumed for free.** Equation `(12)` verifies that the random erasure-good code can also avoid zero coordinates with positive probability.
- **No RH-scale cancellation follows.** This finding closes a generic coding obstruction route; it does not prove the source cap that motivated the code dictionary and does not yield a bound for `M(x)`.

## Consequence for the research line

The generic-code branch is now settled in the permissive direction. `MC-313` showed that generalized Griesmer was too weak; `MC-315` isolated the exact diagonal projective occupancy problem; `MC-316` showed that systematic rank and Wei-dual reformulations add no extra coercivity. The present finding supplies the missing existence theorem.

Accordingly, further attempts to rule out the exact natural-scale source regime using only **generic** generalized-weight inequalities, half-rate erasure capacity, projective occupancy, systematic submatrix ranks, or ordinary primal/dual code constraints should be treated as exhausted unless they introduce a genuinely stronger invariant not already satisfied by these random-linear matched controls.

The live question moves back to **arithmetic realizability**: identify a property forced specifically by the reciprocal-prime/source-incidence construction that generic `[2R,R]` binary codes need not satisfy, and test whether that property is strong enough to forbid the otherwise feasible endpoint `(1)`.