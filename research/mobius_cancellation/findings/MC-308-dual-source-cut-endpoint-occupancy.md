# MC-308 — Dual source-cut occupancy exposes where endpoint sparsity first becomes visible

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `NEGATIVE/OBSTRUCTION` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact one-defect Legendre-shell endpoint of `MC-307`. Fix linearly independent shell functionals

\[
\lambda_1,\ldots,\lambda_k
\]

and choose lower-prime product representatives

\[
V_i\subseteq\{p\le y:p\text{ odd prime}\},
\qquad
\prod_{p\in V_i}\left(\frac pr\right)=(-1)^{\lambda_i(s(r))}
\]

on the shell `\mathcal R_y`. For source-cost applications one may take the minimum representatives used in `MC-307`, but the finite statement below holds for any fixed representatives.

Let

\[
U=\bigcup_{i=1}^kV_i
\]

and attach to every source prime `p\in U` its incidence column

\[
a_p=(\mathbf 1_{p\in V_1},\ldots,\mathbf 1_{p\in V_k})\in\mathbf F_2^k.
\]

The columns span `\mathbf F_2^k`: otherwise a nonzero row relation among the chosen representatives would give a nontrivial linear relation among the independent shell functionals.

Now choose an arbitrary source subset `J\subseteq U`, put

\[
P_J:=\prod_{p\in J}p,
\qquad
B_J:=\operatorname{span}\{a_p:p\in U\setminus J\},
\]

and write

\[
W_J:=\mathbf F_2^k/B_J,
\qquad
t_J:=\dim W_J.
\]

Let `q_J:\mathbf F_2^k\to W_J` be the quotient map and define the **quotient-simplex size**

\[
h_J
:=
\left|\{0,q_J(e_1),\ldots,q_J(e_k)\}\right|,
\tag{1}
\]

where `e_1,\ldots,e_k` is the coordinate basis determined by the chosen endpoint functionals.

Then the exact one-defect endpoint condition restricts the shell, modulo `P_J`, to at most

\[
\boxed{
\frac{h_J}{2^{t_J}}\,\varphi(P_J)
}
\tag{2}
\]

reduced residue classes. More precisely, `(2)` is the exact number of reduced residue classes modulo `P_J` that are compatible with the endpoint constraint after the complementary source coordinates `U\setminus J` are allowed to vary freely.

Consequently the same arbitrary-interval Brun--Titchmarsh input used in `MC-307` gives

\[
\boxed{
\log\frac{y}{P_J}
\le
(2+o(1))\frac{h_J}{2^{t_J}}\log y+O(1),
}
\tag{3}
\]

and hence

\[
\boxed{
P_J
\ge
 y^{\,1-(2+o(1))h_J/2^{t_J}}e^{-O(1)}.
}
\tag{4}
\]

The exponent is useful precisely when the endpoint image in the source cut occupies less than half of the quotient states.

This is the source-coordinate dual of `MC-307`. Taking `J=U` gives `B_J=0`, `t_J=k`, `h_J=k+1`, so `(4)` becomes exactly

\[
P_U\ge y^{1-(2+o(1))(k+1)/2^k}e^{-O(1)},
\]

the hereditary endpoint radical bound of `MC-307`.

The new information appears for **proper source cuts**. It identifies the exact invariant controlling whether a low-product subset of source primes can already see the endpoint sparsity: not merely the number of source primes removed, but the rank loss `t_J` and the number `h_J` of distinct one-defect directions surviving in that quotient.

## 1. Exact source-cut counting

For every shell prime `r`, encode the lower-prime Legendre signs by bits

\[
z_p(r)\in\mathbf F_2,
\qquad
\left(\frac pr\right)=(-1)^{z_p(r)}.
\]

Let

\[
A:\mathbf F_2^U\longrightarrow\mathbf F_2^k,
\qquad
Az=\sum_{p\in U}z_pa_p.
\tag{5}
\]

With the convention `-1\leftrightarrow1`, the exact one-defect endpoint says that the selected sign vector belongs to the affine simplex

\[
E
=
\{\mathbf 1,\mathbf 1+e_1,\ldots,\mathbf 1+e_k\}
\subseteq\mathbf F_2^k.
\tag{6}
\]

Split `z=(z_J,z_{J^c})`. A prescribed source-sign assignment `z_J\in\mathbf F_2^J` is compatible with some complementary assignment if and only if

\[
A_Jz_J+A_{J^c}z_{J^c}\in E
\]

for some `z_{J^c}`. After quotienting by `B_J=\operatorname{im}A_{J^c}`, this is exactly

\[
q_J(A_Jz_J)\in q_J(E).
\tag{7}
\]

Because the full column family spans `\mathbf F_2^k`, the quotient map

\[
q_JA_J:\mathbf F_2^J\to W_J
\]

is surjective. Every quotient state therefore has exactly `2^{|J|-t_J}` preimages. Translation by `q_J(\mathbf1)` does not affect cardinality, so

\[
|q_J(E)|
=
\left|\{0,q_J(e_1),\ldots,q_J(e_k)\}\right|
=h_J.
\tag{8}
\]

Hence the number of compatible Legendre-sign assignments on `J` is exactly

\[
2^{|J|-t_J}h_J.
\tag{9}
\]

For square-free odd `P_J`, the Chinese remainder theorem gives exactly

\[
\frac{\varphi(P_J)}{2^{|J|}}
\]

reduced residue classes for each prescribed vector of Legendre signs. Multiplying by `(9)` proves `(2)`.

This calculation distinguishes two notions that were conflated by a tempting next attack after `MC-307`: the full endpoint is exponentially sparse in the **joint** source-sign space, while a small source projection can be completely nonsparse.

## 2. Brun--Titchmarsh converts source-cut sparsity into a product cost

Impose also `r\equiv1\pmod4`, as throughout the localized shell. Every compatible class modulo `P_J` determines one reduced class modulo `4P_J` with residue `1 mod 4`, so the number of admissible classes modulo `4P_J` is still the quantity in `(2)`.

If `4P_J<y`, Yamada's explicit arbitrary-interval Brun--Titchmarsh bound, already used in `MC-307`, gives for each admissible class `a mod 4P_J`

\[
\pi(2y;4P_J,a)-\pi(y;4P_J,a)
<
\frac{2y}{\varphi(4P_J)\{\log(y/(4P_J))+0.8601\}}.
\tag{10}
\]

Since `\varphi(4P_J)=2\varphi(P_J)`, summing `(10)` over `(2)` admissible classes yields

\[
N
<
\frac{h_J}{2^{t_J}}
\frac{y}{\log(y/(4P_J))+0.8601}.
\tag{11}
\]

The fixed-progression prime number theorem gives

\[
N\sim\frac{y}{2\log y}.
\tag{12}
\]

Combining `(11)` and `(12)` proves `(3)`. If `4P_J\ge y`, then `\log(y/P_J)\le\log4`, so `(3)` remains true after the displayed `O(1)` adjustment. Exponentiating proves `(4)`.

The analytic step therefore adds no new zero information. The new content is the exact finite source-cut occupancy ratio `h_J/2^{t_J}` that tells us which composite source moduli are worth feeding into the same Brun--Titchmarsh mechanism.

## 3. Individual source primes are completely blind to the endpoint

The quotient images `q_J(e_i)` span `W_J`, because the coordinate vectors `e_i` span `\mathbf F_2^k`. Therefore

\[
h_J\ge t_J+1.
\tag{13}
\]

Now take a singleton source cut `J=\{p\}`. Removing one column can reduce rank by at most one, so `t_J\in\{0,1\}`.

- If `t_J=0`, then `h_J=1`.
- If `t_J=1`, at least one `q_J(e_i)` is the unique nonzero quotient vector, so `h_J=2`.

In both cases

\[
\boxed{h_J=2^{t_J}.}
\tag{14}
\]

Thus `(2)` equals `\varphi(p)`: **every nonzero residue class modulo each individual source prime is compatible with the exact endpoint condition.** The same is true modulo every prime power `p^a`: the endpoint constraint depends only on the Legendre sign modulo `p`, and both signs remain compatible, so it excludes no unit class modulo `p^a`.

This gives a clean no-go for a natural proposed strengthening of `MC-307`. Gallagher's classical larger sieve aggregates restrictions expressed through the number of occupied classes modulo prime powers. At every individual source prime power the endpoint contributes **no extra residue-class deletion at all** beyond ordinary coprimality. A direct per-prime larger-sieve application therefore cannot recover the exponentially sparse joint endpoint profile. The endpoint information lives in correlations across source primes and first becomes visible only on suitable composite source cuts.

This does **not** rule out a composite-modulus or correlation-sensitive sieve. It says precisely why replacing the composite Brun--Titchmarsh count of `MC-307` by a black-box prime-by-prime larger sieve loses the decisive information.

## 4. Rank loss must reach at least four before dimension alone can force a polynomial cost

Inequality `(13)` gives a representation-independent lower bound on the quotient-simplex size for fixed rank loss. Substituting it into `(4)` shows what can be obtained from `t_J` alone.

For `t_J\le3`,

\[
\frac{2h_J}{2^{t_J}}
\ge
\frac{2(t_J+1)}{2^{t_J}}
\ge1.
\tag{15}
\]

Therefore the Brun--Titchmarsh exponent in `(4)` cannot be positive solely from knowing a source cut loses at most three ranks. The first potentially useful rank loss is

\[
t_J=4,
\]

where the smallest possible quotient-simplex size is `h_J=5`, giving

\[
P_J\ge y^{3/8-o(1)}
\tag{16}
\]

when that minimum is attained. More generally, a useful polynomial lower bound requires

\[
\boxed{h_J<2^{t_J-1}.}
\tag{17}
\]

This exposes a second structural requirement beyond high rank loss: the images of the coordinate one-defect directions must remain sufficiently collapsed in the quotient. A high-rank source cut whose quotient sees almost all `2^{t_J}` states does not create a strong residue-class restriction.

The full-radical case of `MC-307` is extremal in the favorable direction: `t_J=k` and `h_J=k+1`, so the quotient retains only the affine-simplex number of states rather than an exponential fraction.

## 5. Prior art and novelty boundary

All ingredients are classical separately.

- The Legendre-sign count per square-free modulus is ordinary quadratic-residue counting plus the Chinese remainder theorem.
- The quotient calculation `(7)`--`(9)` is elementary finite linear algebra; in coding/matroid language it is a puncturing/deletion rank calculation.
- The analytic conversion `(10)`--`(12)` is exactly the arbitrary-interval Brun--Titchmarsh input already audited in `MC-307`: Tomohiro Yamada, *Explicit improvements of the Brun-Titchmarsh theorem for arbitrary intervals*, arXiv:2312.16090 (2023).
- The larger-sieve comparison uses P. X. Gallagher, *A larger sieve*, Acta Arithmetica **18** (1971), 77--81, DOI `10.4064/aa-18-1-77-81`. Gallagher's theorem is designed to exploit small occupied-class counts modulo prime powers; the present singleton calculation shows that the endpoint supplies no such local deletion on its source primes.

A targeted literature search on 15 September 2026 for larger-sieve treatments of prescribed Legendre patterns, punctured binary simplex/source matrices, and composite-modulus quadratic-sign restrictions found the classical ingredients and adjacent prescribed-Legendre-symbol literature, but not this Mathia-specific source-cut composition. **No standalone novelty claim is made.** The durable delta is the exact dual occupancy formula `(2)` and the identification of `(t_J,h_J,P_J)` as the missing source-side profile behind the hereditary radical obstruction.

## Boundaries and falsification tests

- **Allowed classes are not claimed to be occupied.** Equation `(2)` counts residue classes compatible with the endpoint constraint after forgotten source coordinates may vary. The actual shell may occupy fewer; that only strengthens the Brun--Titchmarsh upper bound.
- **The source-cut profile depends on the chosen representatives.** Different product-character representatives of the same shell functionals can change the incidence columns, `P_J`, `t_J`, and `h_J`. The theorem is valid for every fixed choice; an invariant application must optimize or otherwise justify the chosen representatives. Minimum representatives from `MC-307` are natural for source-cost questions but need not be unique.
- **High rank loss is not enough.** The useful condition is `(17)`, not merely large `t_J`. The quotient images of the endpoint coordinate directions also control occupancy.
- **No low-product high-rank cut is proved to exist.** The theorem turns such a cut into a contradiction pressure; it does not supply the cut. A source system may evade the result by making every cut with favorable `(t_J,h_J)` have product near the shell scale.
- **The larger-sieve no-go is deliberately narrow.** It applies to direct prime-by-prime/prime-power occupancy input. A sieve or dispersion theorem that genuinely retains composite-modulus correlations is not covered by the obstruction.
- **Exact one-defect structure is load-bearing.** A different endpoint support replaces the affine simplex `E` in `(6)` by its own support, and `h_J` must be recomputed from that image.
- **No Möbius or RH estimate follows.** This is a source-structure theorem inside the localized endpoint program. It neither excludes the endpoint family nor moves a zero-free boundary.

## Consequence for the research line

`MC-307` showed that every proper collection of endpoint directions must already see a large common source radical. The obvious next hope was that a sieve combining many individual lower-prime restrictions might amplify that fact. The source-cut calculation shows why the simplest version cannot work: **the endpoint is jointly sparse but one-source-wise completely uniform.** Every individual source prime forgets the endpoint constraint exactly.

The next source-side target is therefore sharper. One must understand the weighted cut profile of the minimum-representative incidence matrix: find, force, or rule out subsets `J` for which a relatively small product `P_J` causes a large rank drop `t_J` while keeping the quotient-simplex image `h_J` sub-half as in `(17)`. Any such cut immediately incurs the polynomial source-cost bound `(4)`. Conversely, an endpoint realization that survives must hide its sparsity in genuinely high-order composite source correlations, not in per-prime residue exclusions.