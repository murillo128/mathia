# MC-310 — Reciprocal endpoint Page-cheap subspaces obey a 2-adic rank law

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact endpoint-partition setup of `MC-293`–`MC-309`, and specialize to the reciprocal one-defect extremizer from `MC-295`–`MC-296`. Thus

\[
L=\langle\lambda_1,\ldots,\lambda_R\rangle\cong\mathbf F_2^R,
\tag{1}
\]

and the defect sets form an exact partition with equal masses

\[
d_{\lambda_1}=\cdots=d_{\lambda_R}=\frac1R.
\tag{2}
\]

For a mask `a=(a_1,\ldots,a_R)\in\mathbf F_2^R`, write

\[
\lambda_a=\sum_{i=1}^R a_i\lambda_i,
\qquad
j(a)=|a|.
\tag{3}
\]

`MC-296` gives the exact shell bias

\[
\boxed{
 x_{\lambda_a}
 =(-1)^{j(a)}\left(1-\frac{2j(a)}R\right).
}
\tag{4}
\]

Use the Page source scale and balance error from `MC-293`,

\[
D_y=\exp\!\left(\kappa\frac{\log y}{\log\log y}\right),
\qquad
\varepsilon_y=O((\log y)^{-2}),
\tag{5}
\]

so that among all nonzero shell functionals with `\mathcal Q(\lambda)\le D_y`, at most one Page-exceptional functional `\lambda_*(y)` can have

\[
|x_\lambda|>\varepsilon_y.
\tag{6}
\]

Call a subspace

\[
C\le L,
\qquad \dim C=t,
\tag{7}
\]

**uniformly Page-cheap** when every nonzero `\lambda\in C` satisfies

\[
\mathcal Q(\lambda)\le D_y.
\tag{8}
\]

Assume the reciprocal rank is in the discrete-resolution range

\[
\boxed{R\varepsilon_y<1.}
\tag{9}
\]

This includes the critical endpoint regime `R\asymp\log\log y` considered in `MC-242`, `MC-295`, and `MC-306`.

Then every uniformly Page-cheap subspace obeys the unconditional 2-adic rank bound

\[
\boxed{
 t\le \nu_2(R)+1,
}
\tag{10}
\]

where `\nu_2(R)` is the exponent of `2` dividing `R`.

More precisely:

1. **No exceptional mode in `C`.** If `\lambda_*\notin C` (or if no Page-exceptional mode exists), then
   \[
   \boxed{2^t\mid R,\qquad t\le\nu_2(R).}
   \tag{11}
   \]

2. **One exceptional mode in `C`.** If `\lambda_*\in C`, write uniquely
   \[
   \lambda_*=\lambda_{a_*},
   \qquad j_*=j(a_*).
   \tag{12}
   \]
   Then
   \[
   \boxed{
   2^{t-1}\mid j_*,
   \qquad
   2^{t-1}\mid (R-j_*),
   }
   \tag{13}
   \]
   and therefore
   \[
   \boxed{
   2^{t-1}\mid\gcd(R,j_*),
   \qquad
   t\le1+\min\{\nu_2(R),\nu_2(j_*)\}.
   }
   \tag{14}
   \]

In particular, if `R\equiv2\pmod4`, every uniformly Page-cheap subspace has dimension at most `2`, and one of dimension `2` must contain the unique Page-exceptional mode. If the exceptional mode is absent, the maximum dimension is `1`.

Equivalently, define the Page-cheap subspace rank inside the reciprocal endpoint span by

\[
r_{\mathrm{cheap}}(y)
:=
\max\left\{\dim C:
C\le L,
\ \mathcal Q(\lambda)\le D_y
\text{ for every }0\ne\lambda\in C
\right\}.
\tag{15}
\]

Then `(9)` implies

\[
\boxed{
r_{\mathrm{cheap}}(y)\le\nu_2(R)+1.}
\tag{16}
\]

Thus the reciprocal endpoint extremizer cannot hide a large low-source linear sector merely by arranging its low-cost frequencies near the middle Hamming layer. `MC-309` gave a general half-occupancy barrier for low-product source cuts. The reciprocal equal-mass model is much more rigid: the exact `1/R` Fourier lattice snaps every nonexceptional cheap frequency **exactly** onto Hamming weight `R/2`, and linear closure then forces a one-weight-code divisibility law. Except when `R` has unusually large 2-adic valuation, the entire Page-cheap sector has only constant or very small dimension.

No estimate for `M(x)` follows. The surviving route is still to prove that the actual arithmetic source geometry must create a sufficiently large uniformly cheap subspace, or otherwise exploit the complementary fact that most independent endpoint directions necessarily live above the Page source scale.

## 1. Page balance becomes exact middle-layer membership

Let `0\ne\lambda_a\in C` be nonexceptional. By `(6)` and `(8)`,

\[
|x_{\lambda_a}|\le\varepsilon_y.
\tag{17}
\]

Using the reciprocal endpoint formula `(4)`,

\[
|R-2j(a)|
=R|x_{\lambda_a}|
\le R\varepsilon_y<1.
\tag{18}
\]

The left side is an integer. Hence it is zero:

\[
\boxed{j(a)=R/2.}
\tag{19}
\]

So every nonzero mask in the coefficient subspace corresponding to `C`, except possibly the single mask `a_*` of the Page-exceptional mode, has exactly half of the `R` endpoint coordinates switched on.

This is stronger than the antichain conclusion in `MC-296`. There, Page theory forced low-cost subset sums into an `O(\varepsilon_y)` window around defect mass `1/2`. Reciprocal equal weights make that window discrete. Once `R\varepsilon_y<1`, there is no room for a neighboring Hamming layer.

## 2. Walsh inversion classifies the cheap coefficient subspace

Identify `C` with `\mathbf F_2^t`. Because the `\lambda_i` are independent, every element of `C` has a unique coefficient mask in `\mathbf F_2^R`. Choose a basis of `C` and place those masks as the rows of a binary generator matrix

\[
G\in\mathbf F_2^{t\times R}.
\tag{20}
\]

Let its `i`-th column be

\[
g_i\in\mathbf F_2^t,
\tag{21}
\]

and for each column type `v\in\mathbf F_2^t` let

\[
m(v):=\#\{i:g_i=v\}.
\tag{22}
\]

Thus

\[
\sum_{v\in\mathbf F_2^t}m(v)=R.
\tag{23}
\]

For `u\in\mathbf F_2^t`, the corresponding coefficient mask is `uG`, and

\[
R-2|uG|
=
\sum_{i=1}^R(-1)^{u\cdot g_i}
=
\sum_{v\in\mathbf F_2^t}m(v)(-1)^{u\cdot v}
=:\widehat m(u).
\tag{24}
\]

Thus the deviation of a codeword from middle Hamming weight is exactly the Walsh transform of the column-multiplicity function.

If the exceptional mode is absent from `C`, equation `(19)` gives

\[
\widehat m(u)=0
\qquad(u\ne0),
\tag{25}
\]

while `\widehat m(0)=R`. Fourier inversion on `\mathbf F_2^t` therefore gives

\[
\boxed{
 m(v)=\frac{R}{2^t}
 \qquad(v\in\mathbf F_2^t).
}
\tag{26}
\]

All `2^t` column types occur with the same multiplicity, including the zero column. Integrality proves `2^t\mid R`, hence `(11)`.

This is the finite-code form of the obstruction: after puncturing the zero columns, the resulting binary linear code is a repeated simplex/one-weight code.

## 3. One Page exception gives exactly two column multiplicities

Now suppose the unique Page-exceptional mode belongs to `C`. Let `u_*\in\mathbf F_2^t\setminus\{0\}` be its coordinate vector in the chosen basis, so

\[
u_*G=a_*,
\qquad |u_*G|=j_*.
\tag{27}
\]

Every other nonzero `u` is nonexceptional and therefore has weight `R/2`. Hence

\[
\widehat m(u)=0
\qquad(u\ne0,u_*),
\tag{28}
\]

while

\[
\widehat m(0)=R,
\qquad
\widehat m(u_*)=R-2j_*=:B.
\tag{29}
\]

Walsh inversion is now exact:

\[
\boxed{
 m(v)
 =2^{-t}\left(R+B(-1)^{u_*\cdot v}\right).
}
\tag{30}
\]

Therefore the two affine half-spaces of column types have constant multiplicities

\[
\boxed{
 u_*\cdot v=0:
 \quad
 m(v)=\frac{R-j_*}{2^{t-1}},
}
\tag{31}
\]

and

\[
\boxed{
 u_*\cdot v=1:
 \quad
 m(v)=\frac{j_*}{2^{t-1}}.
}
\tag{32}
\]

Both are nonnegative integers. Equations `(13)` and `(14)` follow immediately.

So the possible Page exception does not merely cost one uncontrolled Fourier coefficient, as in the generic support estimate `MC-309`. In the reciprocal endpoint model, linear closure propagates that one exceptional coefficient into a complete two-level classification of the source-subspace coordinate geometry.

## 4. Relation to the source-cut frontier

The new statement is basis-invariant at the level of the endpoint span. It controls **any** subspace `C\le L` all of whose nonzero functionals have individual source cost at most `D_y`; it does not require that the low-cost representatives share one fixed source-prime set.

Hence it also applies to every low-product source cut from `MC-308`–`MC-309`: if a cut `J` with `P_J\le D_y` exposes a quotient-frequency subspace of dimension `t`, every nonzero frequency has `\mathcal Q(\lambda)\le P_J\le D_y`, so `(10)` applies. In the reciprocal model,

\[
\boxed{
 t_J\le\nu_2(R)+1,
}
\tag{33}
\]

whenever `(9)` holds.

This can be far stronger than the generic `MC-309` consequence `2^{t_J-1}\le h_J\le R+1`, which only yields `t_J\le1+\log_2(R+1)`. For example, if `R\equiv2\pmod4`, `(33)` gives `t_J\le2` regardless of how large `R` is.

The gain is specific to the reciprocal defect partition. It comes from combining three ingredients that were previously separate:

- exact endpoint subset-sum biases from `MC-296`;
- Page uniqueness and `O((\log y)^{-2})` balance from `MC-293`;
- linear closure of the cheap/source-cut frequency family from `MC-294` and `MC-308`.

The resulting obstruction is therefore a sharper answer to the current hereditary-source-complexity question: a reciprocal endpoint family can place at most `\nu_2(R)+1` independent directions inside the full Page-cheap spectral sector.

## 5. Prior art and novelty audit

The coding-theory component is classical in spirit and no new coding theorem is claimed.

Arrigo Bonisoli, *Every equidistant linear code is a sequence of dual Hamming codes*, Ars Combinatoria 18 (1984), 181–186, classifies linear one-weight/equidistant codes by repeated simplex (dual Hamming) structure. The University of Modena record summarizes the theorem as saying that every equidistant linear code can be brought, after column permutation, to a sequence of Hamming parity-check matrices. This is exactly adjacent to `(26)`: after puncturing the zero columns, the nonexceptional case is a repeated binary simplex code.

R. Calderbank and W. M. Kantor, *The Geometry of Two-Weight Codes*, Bulletin of the London Mathematical Society 18 (1986), 97–122, DOI `10.1112/blms/18.2.97`, surveys the broader relation between two-weight linear codes, projective point sets, and strongly regular graphs. The one-Page-exception case `(30)`–`(32)` is an extremely special two-weight situation. Its two-level column-multiplicity formula follows directly here from finite Walsh inversion; no novelty is claimed for the underlying few-weight-code phenomenon.

Victor K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory 37 (1991), 1412–1418, DOI `10.1109/18.133259`, established the standard subcode-support hierarchy. That language is relevant if one rephrases `(16)` as a lower bound on the dimension of subcodes supportable below a source-product budget, but the present finding does not claim a new general bound in coding theory.

The line-specific derived content is the arithmetic bridge: Landau–Page balance at the source threshold `D_y`, when inserted into the exact reciprocal endpoint Fourier profile, forces every uniformly cheap subspace into this one-weight/one-exception code class and therefore exposes the 2-adic rank obstruction `(10)`–`(16)`. A fresh search found the classical one-weight/two-weight/generalized-weight literature above but no source asserting this Möbius/Legendre-shell specialization. Because the finite-code classification is classical and the arithmetic construction is highly specialized, the result is recorded as a frontier refinement with **no standalone novelty claim**.

## 6. Boundaries and falsification tests

The conclusion is intentionally narrow.

- **Exact reciprocal masses are essential.** For unequal defect weights `d_i`, the Page window need not snap to one exact Hamming layer, and the Walsh classification above does not apply as stated.
- **The discrete-resolution condition is essential.** If `R\varepsilon_y\ge1`, neighboring Hamming layers may fit inside the Page balance window. In the critical regime `R\asymp\log\log y`, however, `(9)` is automatic for large `y` because `\varepsilon_y\ll(\log y)^{-2}`.
- **Uniform cheapness is stronger than cheap generators.** It is not enough that a basis of `C` have source cost at most `D_y`; every nonzero combination must satisfy `(8)`. A common source-prime cut of product at most `D_y` is a sufficient way to guarantee this.
- **The possible Page exception matters.** It is exactly why `(10)` has `+1`. If independent arithmetic input removes the exceptional character from the subspace, the stronger divisibility `(11)` applies.
- **Large 2-adic rank remains an escape.** If `R` is highly divisible by powers of two, the bound can be as large as `O(\log R)` and approaches the generic occupancy scale. The theorem does not rule out such endpoint ranks.
- **No common source set is inferred.** `r_cheap(y)` concerns individual minimum source costs for every member of a subspace. It does not assert that their minimizing representatives are simultaneously realizable inside one fixed radical.
- **No zeta zero-free improvement follows.** Landau–Page is used only in its already established range from `MC-293`; the argument neither enlarges `D_y` nor converts the source-complexity obstruction into a bound for `M(x)`.

The next non-circular question is therefore sharper than after `MC-309`: can the actual Legendre source geometry force a Page-cheap subspace whose dimension exceeds `\nu_2(R)+1`, or force reciprocal endpoint ranks with bounded `\nu_2(R)` while independently requiring a larger cheap quotient dimension? Either route would contradict the reciprocal endpoint extremizer without asking for stronger character cancellation first.