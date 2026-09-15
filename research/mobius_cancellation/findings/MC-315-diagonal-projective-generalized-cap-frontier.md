# MC-315 — The exact source-code endpoint is a diagonal projective generalized-cap problem

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `FRONTIER-REFINEMENT` · `NEGATIVE/OBSTRUCTION` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact-natural-scale endpoint isolated in `MC-314`. Let

\[
t_R:=\left\lceil 2\log_2(R+1)\right\rceil
\]

and suppose the source-incidence code is a full-length binary `[2R,R]` code `C` satisfying

\[
d_{t_R}(C)\ge R-2.
\tag{1}
\]

The generator columns of `C` define a spanning multiset `\mathcal M` of `2R` points in the projective space `PG(R-1,2)`. The standard geometric formula for generalized Hamming weights is

\[
2R-d_t(C)
=
\max_{U:\,\operatorname{codim}U=t}\mathcal M(U).
\tag{2}
\]

Hence `(1)` is exactly the incidence constraint

\[
\boxed{
\max_{U:\,\operatorname{codim}U=t_R}\mathcal M(U)\le R+2.
}
\tag{3}
\]

Thus the unresolved generic-code question in `MC-314` is not merely an informal near-capacity list-decoding question. It is a standard finite-geometric extremal problem: can `2R` spanning projective points in `PG(R-1,2)` have every codimension-`t_R` subspace contain at most `R+2` of them?

D'haeseleer and Kurz (2026) define `n_q(r,h,f;s)` as the maximum size of a projective `(h,f)-(n,r,s)_q` system. In the linear case `h=1`, their object is precisely a multiset of projective points controlled by codimension-`f` incidences, and they record the coding identity `s=n-d_f`. Equivalently, in the notation of Kurz--Landjev--Rousseva (2026), the same geometry is an `(n,w)^(R-t_R-1)` multiarc in `PG(R-1,2)` with `w\le R+2`.

To avoid the harmless convention that those extremal functions record an attained maximum occupancy, define the monotone cap envelope

\[
\mathcal N_R
:=
\max_{0\le s\le R+2} n_2(R,1,t_R;s).
\tag{4}
\]

Then, using the paper's faithful-replacement observation for projective systems, the existence of a generic full-length `[2R,R]` control satisfying `(1)` is equivalent, for all sufficiently large `R`, to

\[
\boxed{\mathcal N_R\ge 2R.}
\tag{5}
\]

This turns the next generic coding kill into a single diagonal asymptotic question:

\[
\boxed{
\text{prove }\mathcal N_R<2R\text{ eventually, or construct systems showing }\mathcal N_R\ge2R.
}
\tag{6}
\]

The strongest immediately available general incidence bound in the new projective-system framework does **not** resolve `(6)`. Lemma 4.2 of D'haeseleer--Kurz gives

\[
n_q(r,h,f;s)
\le
\frac{{r\brack f}_q}{{r-h\brack f}_q}s.
\tag{7}
\]

For `q=2`, `r=R`, `h=1`, `f=t_R`, the Gaussian-binomial ratio telescopes to

\[
\frac{{R\brack t_R}_2}{{R-1\brack t_R}_2}
=
\frac{2^R-1}{2^{R-t_R}-1}.
\tag{8}
\]

Therefore

\[
\mathcal N_R
\le
\frac{2^R-1}{2^{R-t_R}-1}(R+2)
=
O(R^3),
\tag{9}
\]

because `2^{t_R}=\Theta(R^2)`. The endpoint only asks for length `2R`, so `(9)` misses the relevant scale by two powers of `R`.

Together with `MC-313`, this eliminates another broad generic route: generalized Singleton/Griesmer collapse at this `t_R`, while the natural projective incidence average is also far too weak. A generic contradiction, if one exists, needs a genuinely sharper **diagonal** estimate for projective generalized caps/multiarcs in the regime

\[
q=2,
\qquad
r=R\to\infty,
\qquad
f\sim2\log_2 R,
\qquad
s\sim R,
\qquad
n\sim2R.
\tag{10}
\]

No estimate for `M(x)` follows.

## 1. Exact code-to-geometry dictionary

Let `G` be an `R\times2R` full-rank generator matrix for `C`. Full length means no column is zero, so its columns determine a spanning projective multiset `\mathcal M` in `PG(R-1,2)`.

For every `1\le t\le R`, the classical generalized-weight/projective-system correspondence gives `(2)`: a `t`-dimensional subcode with small support is dual to a codimension-`t` projective subspace containing many generator columns. D'haeseleer--Kurz state this as

\[
n-d_f(C)=\max\{\mathcal M(U):\operatorname{codim}U=f\}.
\tag{11}
\]

Putting `n=2R`, `f=t_R`, and using `d_{t_R}\ge R-2` gives `(3)` immediately.

Conversely, a spanning multiset of `2R` nonzero projective points satisfying `(3)` gives a full-length `[2R,R]` code and `(11)` returns `d_{t_R}\ge R-2`. Thus no coding information is lost in passing from `(1)` to `(3)`.

D'haeseleer--Kurz allow projective systems with lower-dimensional elements but explicitly note that such a system can be replaced by a faithful system with the same length and no larger incidence cap. This is why the monotone envelope `(4)` is sufficient for the exact existence test `(5)`: if an extremal system has more than `2R` points, retain a spanning `R`-point subset and any further points up to length `2R`; deleting points cannot increase the codimension-`t_R` occupancy.

## 2. The current general incidence bound is quantitatively non-coercive

Equation `(7)` is the elementary double-counting bound in the modern projective-system language. For `h=1`, the Gaussian-coefficient identity

\[
\frac{{R\brack t}_2}{{R-1\brack t}_2}
=
\frac{2^R-1}{2^{R-t}-1}
\tag{12}
\]

is exact. Since `t_R=o(R)`, the ratio is `(1+o(1))2^{t_R}`. By definition of `t_R`,

\[
(R+1)^2\le2^{t_R}<2(R+1)^2,
\tag{13}
\]

so `(9)` follows.

This is not a small numerical loss. The average-incidence bound permits `\Theta(R^3)` points while the source-code endpoint asks whether `2R` points are possible. Therefore no refinement that merely reuses the same first-moment incidence count can rule out the exact-natural-scale source code.

The multiarc formulation of Kurz--Landjev--Rousseva gives the same target. Writing `w_j` for the maximum occupancy of a projective `j`-subspace, their identity

\[
w_j+d_{R-j-1}=n
\tag{14}
\]

sets `j=R-t_R-1`, so `(1)` becomes `w_j\le R+2`. Their 2026 paper develops generalized Griesmer bounds and exact small-dimension tables, but its general Griesmer inequality is precisely the bound already shown in `MC-313` to collapse to generalized Singleton in this regime.

## 3. Prior-art boundary

The geometric translation itself is classical. D'haeseleer and Kurz explicitly say that the special cases `h=1` or `f=1` have been extensively studied, and their paper is a modern unifying treatment of generalized Hamming weights and projective systems. `MC-S53` records that source. `MC-S51` already records the neighboring generalized-weight multiarc formulation of Kurz--Landjev--Rousseva.

A targeted literature check on 15 September 2026 found these exact finite-geometric formulations, generalized Griesmer bounds, small-dimension optimal tables, and the fixed-gap erasure-list literature already recorded in `MC-S50`--`MC-S52`. It did not locate a theorem settling the diagonal regime `(10)`. This is not a bibliographic-completeness claim.

No novelty is claimed for projective systems, generalized caps, multiarcs, the identity `(11)`, or the double-counting bound `(7)`. The durable Mathia delta is the **parameter identification**: the unresolved exact-source-scale escape of `MC-314` is the diagonal extremal question `(6)`, and the currently audited general projective-system bound specializes to `O(R^3)` rather than the needed `<2R` threshold.

## Boundaries and falsification tests

- **This is a generic-code boundary, not an arithmetic realization.** A projective system satisfying `(3)` need not arise from lower-prime Legendre source columns. Constructing one would only show that generic binary/projective geometry does not kill the source endpoint.
- **The exact-natural-scale source cap remains hypothetical.** `MC-314` does not prove `Z\le y^{1/R}`; it proves what that hypothesis would force.
- **The envelope `(4)` is intentional.** The literature parameters usually record an attained maximum occupancy. The source condition only supplies an upper cap `s\le R+2`; maximizing over `s` avoids an artificial equality convention.
- **The `O(R^3)` bound is only a failure certificate for first-moment incidence counting.** It does not imply that systems of length `2R` actually exist.
- **Generalized caps in other affine/projective senses are not automatically the same problem.** Results forbidding small subsets in low-dimensional flats must be translated to the exact codimension-`t_R` occupancy condition before use.
- **Small fixed-dimension tables do not control the diagonal limit.** Here both ambient dimension and the controlled codimension grow.
- **No RH or Mertens estimate follows.** This only sharpens the generic coding branch of the reciprocal endpoint program.

## Consequence for the research line

`MC-314` ended with the instruction to seek either second-order arithmetic source control or a stronger coding/realizability obstruction. The generic coding half can now be stated without ambiguity: determine the asymptotic projective generalized-cap parameter `(4)` in regime `(10)` well enough to decide the threshold `2R`.

If one proves `\mathcal N_R<2R` eventually, the exact-natural-scale rate-one-half source code is impossible before any arithmetic column restriction is used. If instead one constructs `\mathcal N_R\ge2R`, generic coding geometry is decisively cleared and any further obstruction must use the arithmetic realizability of the lower-prime source columns or a stronger joint-weight/source-cost law.

Until one side of `(6)` is resolved, further use of generalized Singleton, generalized Griesmer, fixed-gap erasure capacity, or the raw incidence average cannot by itself move this endpoint.