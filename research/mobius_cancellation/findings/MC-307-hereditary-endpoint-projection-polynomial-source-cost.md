# MC-307 — Endpoint projections force hereditary polynomial source cost

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `FRONTIER-REFINEMENT` · `NEGATIVE/OBSTRUCTION` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact endpoint-partition setup of `MC-296`, the source-cost definition of `MC-293`, and the Brun--Titchmarsh coset argument of `MC-305`. Let

\[
\mathcal R_y
=\{r:y<r\le2y,\ r\text{ prime},\ r\equiv1\pmod4\},
\qquad N=|\mathcal R_y|,
\]

and let

\[
\lambda_1,\ldots,\lambda_R
\]

be linearly independent shell functionals whose defect sets form an exact partition of `mathcal R_y`: every shell prime has value `+1` for exactly one selected functional and value `-1` for the other `R-1` functionals.

For each `i`, choose a minimum lower-prime product representative of `lambda_i` in the sense of `MC-293`, and write

\[
Q_i:=\mathcal Q(\lambda_i)
=\prod_{p\in V_i}p,
\]

with `V_i` a set of odd primes at most `y`. For a nonempty index set `I subsetneq [R]`, put

\[
k=|I|,
\qquad
P_I:=\prod_{p\in\cup_{i\in I}V_i}p.
\]

Thus `P_I` is the common squarefree support radical of the chosen minimum representatives, and

\[
P_I\le\prod_{i\in I}Q_i.
\tag{1}
\]

Then every proper `k`-coordinate projection of the endpoint partition satisfies the unconditional hereditary radical bound

\[
\boxed{
\log\frac{y}{P_I}
\le
(2+o(1))\frac{(k+1)\log y}{2^k}+O(1).
}
\tag{2}
\]

Equivalently,

\[
\boxed{
P_I
\ge
y^{\,1-(2+o(1))(k+1)/2^k}\,e^{-O(1)}.
}
\tag{3}
\]

The new point relative to `MC-305` is that the same support-capacity argument applies **hereditarily to every subfamily**, not only to the full `R`-dimensional quotient. A `k`-coordinate projection of a one-defect endpoint does not occupy `2^k` sign cells: it occupies only the `k` one-defect cells plus the all-minus cell. This turns small projected source radicals into an immediate Brun--Titchmarsh contradiction.

Combining `(1)` and `(3)` gives a source-cost consequence that is much stronger than the quasi-subpower Landau--Page threshold of `MC-293`--`MC-296`:

\[
\boxed{
\prod_{i\in I}Q_i
\ge
y^{\,1-(2+o(1))(k+1)/2^k}e^{-O(1)}
}
\tag{4}
\]

for **every** proper `k`-subset `I`.

A fixed six-coordinate projection already gives a polynomial barrier. For `k=6`,

\[
1-\frac{2(k+1)}{2^k}
=1-\frac{14}{64}
=\frac{25}{32},
\]

so for every six-element `I` and all sufficiently large `y`, provided `R\ge7`,

\[
\boxed{
\prod_{i\in I}Q_i
\ge y^{25/32-o(1)}.
}
\tag{5}
\]

Order the selected source costs as

\[
Q_{(1)}\le Q_{(2)}\le\cdots\le Q_{(R)}.
\]

Applying `(5)` to the six cheapest selected directions gives

\[
Q_{(6)}^6
\ge
\prod_{j=1}^6Q_{(j)}
\ge y^{25/32-o(1)},
\]

hence

\[
\boxed{
Q_{(6)}\ge y^{25/192-o(1)}.
}
\tag{6}
\]

Therefore an exact endpoint partition forces **all but at most five** selected basis directions to have minimum lower-prime source cost at least

\[
\boxed{
y^{25/192-o(1)}.}
\tag{7}
\]

Among fixed projection dimensions, the exponent obtained from this direct argument,

\[
c_k=\frac{1-2(k+1)/2^k}{k},
\]

is maximized at `k=6`; the fixed-six conclusion is therefore the strongest polynomial per-direction bound furnished by this unweighted projected Brun--Titchmarsh calculation.

There is also a flexible hereditary form. If `k=k(y)<R` and

\[
\frac{k}{2^k}\to0,
\]

then every `k`-subfamily obeys

\[
P_I\ge y^{1-o(1)},
\qquad
\prod_{i\in I}Q_i\ge y^{1-o(1)}.
\tag{8}
\]

Summing the logarithmic version of `(4)` over all `k`-subsets gives

\[
\boxed{
\sum_{i=1}^R\log Q_i
\ge
\frac{R}{k}
\left(1-(2+o(1))\frac{k+1}{2^k}\right)\log y-O(R/k).
}
\tag{9}
\]

Thus the endpoint condition imposes not merely one near-shell common radical but a **hereditary source-complexity profile**: every moderately sized selected subfamily must already collectively see essentially the whole shell scale.

This kills the explicit disjoint-singleton matched profile of `MC-306` as a possible realization of the actual endpoint localization. In that model, with

\[
z=y^{1/R},
\qquad
p_i\in[z,2z],
\]

one has for every `k`-subset

\[
P_I=\prod_{i\in I}p_i
\le (2z)^k=2^k y^{k/R}.
\tag{10}
\]

At the critical rank `2^R\asymp\log y`, take for example `k=6` once `R` is large. Equation `(10)` gives `P_I=y^{o(1)}`, whereas `(3)` requires `P_I\ge y^{25/32-o(1)}`. More generally any fixed `k\ge4` with positive exponent in `(3)` contradicts the disjoint-singleton profile.

The endpoint model itself is **not** ruled out. A surviving arithmetic realization must instead use strongly overlapping or individually expensive lower-prime source representatives so that even small coordinate projections acquire polynomial-size common radical. No estimate for `M(x)` follows.

## 1. Every projected endpoint occupies only `k+1` sign cells

Fix a nonempty proper subset

\[
I=\{i_1,\ldots,i_k\}\subsetneq[R].
\]

For each selected minimum source representative define the corresponding quadratic character on integers coprime to `P_I` by

\[
\chi_i(n)=\prod_{p\in V_i}\left(\frac np\right),
\qquad i\in I.
\tag{11}
\]

On shell primes `r\equiv1 mod4`, quadratic reciprocity identifies this with the lower-prime source value used to represent `lambda_i`:

\[
\chi_i(r)
=\prod_{p\in V_i}\left(\frac rp\right)
=\prod_{p\in V_i}\left(\frac pr\right)
=(-1)^{\lambda_i(s(r))}.
\tag{12}
\]

The characters `chi_i`, `i in I`, are linearly independent after induction to modulus `P_I`. Indeed, if a nonempty product of them were principal modulo `P_I`, its value would be `+1` on every shell prime, contradicting linear independence of the corresponding shell functionals.

Hence

\[
\Theta_I:(\mathbb Z/P_I\mathbb Z)^\times\to\{\pm1\}^k,
\qquad
\Theta_I(a)=(\chi_i(a))_{i\in I},
\tag{13}
\]

is onto, and every sign cell has exactly

\[
\frac{\varphi(P_I)}{2^k}
\tag{14}
\]

reduced residue classes modulo `P_I`.

Now use the exact endpoint partition. If the unique defect of a shell prime `r` occurs at an index `i in I`, then `Theta_I(r)` has one `+1` coordinate and `k-1` coordinates equal to `-1`. If the unique defect occurs outside `I`, then all `k` projected coordinates equal `-1`. Therefore

\[
\Theta_I(\mathcal R_y)
\subseteq
\{(-1,\ldots,-1)\}
\cup
\{\text{the `k` one-defect sign vectors}\}.
\tag{15}
\]

So the projected shell occupies at most

\[
\boxed{
\frac{(k+1)\varphi(P_I)}{2^k}
}
\tag{16}
\]

reduced residue classes modulo `P_I`.

Because `P_I` is odd and the shell already imposes `r=1 mod4`, the Chinese remainder theorem turns `(16)` into the same number of admissible reduced classes modulo `4P_I`.

This projection step is the information absent from the scalar capacity package of `MC-301`--`MC-306`. The full endpoint may pay for a near-shell radical, but every proper projection retains an exponentially sparse sign support: only `k+1` cells survive out of `2^k`.

## 2. Brun--Titchmarsh forces every projected radical toward the shell

Assume first that

\[
4P_I<y.
\]

The explicit arbitrary-interval Brun--Titchmarsh theorem used and audited in `MC-249` and `MC-305` gives, for every reduced class `a mod 4P_I`,

\[
\pi(2y;4P_I,a)-\pi(y;4P_I,a)
<
\frac{2y}
{\varphi(4P_I)\{\log(y/(4P_I))+0.8601\}}.
\tag{17}
\]

Since `P_I` is odd,

\[
\varphi(4P_I)=2\varphi(P_I).
\]

Summing `(17)` over the at most `(k+1)phi(P_I)/2^k` classes in `(16)` yields

\[
N
<
\frac{(k+1)y}
{2^k\{\log(y/(4P_I))+0.8601\}}.
\tag{18}
\]

The prime number theorem in the fixed progression `1 mod4` gives

\[
N=\left(\frac12+o(1)\right)\frac{y}{\log y}.
\tag{19}
\]

Combining `(18)` and `(19)` gives

\[
\log\frac{y}{4P_I}+0.8601
\le
(2+o(1))\frac{(k+1)\log y}{2^k}.
\tag{20}
\]

If instead `4P_I\ge y`, then `log(y/P_I)<=log4`, so the unified bound `(2)` follows after absorbing an absolute constant. Exponentiation gives `(3)`.

No equidistribution assumption appears. The argument only counts how many progression classes are *available* to the projected endpoint and applies an upper bound separately to each class.

## 3. Minimum source cost converts projected radical pressure into a polynomial barrier

For every `i`, the representative `V_i` was chosen to attain the minimum source cost `Q_i`. Since `P_I` is the radical of the union of these sources,

\[
P_I
=\prod_{p\in\cup_{i\in I}V_i}p
\le
\prod_{i\in I}\prod_{p\in V_i}p
=\prod_{i\in I}Q_i.
\tag{21}
\]

Combining `(21)` with `(3)` proves `(4)`.

For fixed `k`, define

\[
\gamma_k
:=
1-\frac{2(k+1)}{2^k}.
\tag{22}
\]

Whenever `gamma_k>0`, every `k`-subset satisfies

\[
\prod_{i\in I}Q_i\ge y^{\gamma_k-o(1)}.
\tag{23}
\]

The first positive case is `k=4`. Dividing the exponent by `k` to obtain a bound on the `k`-th order statistic gives

\[
c_k=\frac{\gamma_k}{k}.
\tag{24}
\]

Direct comparison of the fixed integers `k>=4` shows

\[
c_4=\frac3{32},
\quad
c_5=\frac18,
\quad
c_6=\frac{25}{192},
\quad
c_7=\frac18,
\]

and `c_k` decreases for `k>=7`. Thus `k=6` gives the strongest fixed-dimensional exponent from this exact unweighted argument, proving `(5)`--`(7)`.

The contrast with the Page threshold is large. `MC-293`--`MC-296` forced all but at most one relevant direction above

\[
D_y=\exp\!\left(\kappa\frac{\log y}{\log\log y}\right)=y^{o(1)}.
\]

The exact endpoint support condition now forces all but at most five selected basis directions above the fixed power `y^(25/192-o(1))`. This is not a stronger zero-free theorem; it comes from using the **joint sparse support of the endpoint partition** rather than only the bias of one character at a time.

## 4. The hereditary form identifies the missing arithmetic structure

The full-radical theorem `MC-305` says that at critical rank the union of all selected source supports must be almost shell-sized. `MC-306` then showed that this scalar requirement, together with totient density and family-energy capacity, can be matched by `R` disjoint singleton sources near `y^(1/R)`.

The present theorem separates those two situations. A single full radical can be large because many cheap disjoint sources accumulate. But the endpoint partition demands much more: after forgetting almost all coordinates, the remaining projected sign law is still concentrated on only `k+1` cells. Brun--Titchmarsh therefore forces the *projected* common radical to remain large as well.

Consequently, the surviving source geometry cannot be a collection of cheap nearly independent coordinates. It must have one or both of the following properties:

- most selected shell functionals are individually expensive at a fixed polynomial scale, as `(7)` already forces; and/or
- minimum source representatives overlap so heavily that even small subfamilies cover a large lower-prime radical.

This is a genuinely different invariant from the scalar quantities exhausted in `MC-301`--`MC-306`. Total Fourier energy, full radical size, field discriminant, and `phi(P)/P` do not record whether source complexity survives projection. The endpoint localization problem therefore acquires a new necessary arithmetic datum: **hereditary projected source cost**.

What remains open is whether the actual lower-prime Legendre system permits an independent endpoint family with this hereditary polynomial source profile. The present argument does not exclude such a family and does not convert `(7)` into global Möbius cancellation.

## 5. Prior art and novelty boundary

The analytic input is classical. Equation `(17)` is exactly the arbitrary-interval Brun--Titchmarsh inequality of Tomohiro Yamada, *Explicit improvements of the Brun-Titchmarsh theorem for arbitrary intervals*, arXiv:2312.16090, already audited in `MC-249` and reused in `MC-305`. Finite-character duality, quadratic reciprocity, the Chinese remainder theorem, and the fixed-modulus prime number theorem are standard.

A targeted literature check also found the established neighboring theme in which primes confined to a small union of multiplicative cosets force character bias or obstruct products of primes; for example, Máté Szabó, *On the existence of products of primes in arithmetic progressions*, Bulletin of the London Mathematical Society 56 (2024), 805–816, DOI `10.1112/blms.12990`, works explicitly with prime sets contained in unions of subgroup cosets and character consequences. Hanson--Vaughan--Zhang's work on least integers with prescribed Legendre symbols, already noted at the `MC-306` frontier, is another adjacent prescribed-sign literature.

Those sources establish that neither few-coset prime support nor prescribed Legendre signs are new mechanisms. No source located in this audit states the endpoint-specific hereditary composition `(2)`--`(7)`: project an exact one-defect shell partition to arbitrary coordinate subfamilies, count the surviving `k+1` sign cells, and apply Brun--Titchmarsh to the minimum-source radical. **No standalone novelty claim is made.** The durable delta is a new internal necessary-condition theorem for the current endpoint model and the resulting elimination of the `MC-306` disjoint-singleton profile as an arithmetic realization.

## Boundaries and falsification tests

- **Exact endpoint partition is load-bearing.** The `k+1` support count in `(15)` uses that every shell prime has exactly one defect. If defects overlap or a positive set has no defect, the projected image can occupy additional sign cells and the exponent in `(3)` must be recomputed from the actual projected support size.
- **The subfamily must be proper for the `k+1` count.** For `I=[R]`, the all-minus cell is absent and the sharper `R`-cell theorem of `MC-305` applies instead.
- **Minimum representatives are chosen independently but remain character-independent.** A nonempty product becoming principal modulo `P_I` would be principal on the shell and would contradict linear independence of the corresponding `lambda_i`. No hidden independence assumption beyond the endpoint setup is added.
- **Overlap only helps the obstruction.** Repeated lower-prime factors among different minimum representatives shrink `P_I` relative to `prod Q_i`; inequality `(21)` is in the safe direction.
- **Large projected radical is not a distribution theorem.** The result proves a necessary source-complexity condition; it does not assert equidistribution of shell primes among any of the occupied cells.
- **The polynomial source-cost bound is basis-local.** Equation `(7)` concerns the selected independent endpoint directions and their minimum lower-prime product representatives. It does not assert the same lower bound for every nonzero functional in their span.
- **`MC-306` is not retracted.** Its matched profile remains a valid witness that the earlier scalar package is jointly satisfiable. The present theorem shows precisely why that matched profile cannot also satisfy the omitted endpoint localization requirement.
- **No zero-free region or reciprocal-`L` continuation is imported.** The proof uses only exact finite character structure, the fixed progression `1 mod4`, and the Brun--Titchmarsh upper bound already present in the line.
- **No RH or Mertens conclusion follows.** A true endpoint realization may survive by paying the hereditary polynomial source cost; ruling that out requires new arithmetic information.