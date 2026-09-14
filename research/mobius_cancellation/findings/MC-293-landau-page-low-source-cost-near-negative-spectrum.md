# MC-293 — Landau–Page collapses the low-source-cost near-negative shell spectrum to one mode

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`

## Claim

Continue the localized Legendre-shell setup of `MC-281`--`MC-292`. Let

\[
\mathcal R_y
=
\{r:y<r\le 2y,\ r\text{ prime},\ r\equiv1\pmod4\},
\qquad
N=|\mathcal R_y|,
\tag{1}
\]

and encode each shell prime by its lower-prime Legendre signs. Let `S` be the distinct occupied sign cells, `H=\langle S\rangle` their generated binary span, and for `\lambda\in H^*` write

\[
A_\lambda
=
\sum_{r\in\mathcal R_y}(-1)^{\lambda(s(r))},
\qquad
x_\lambda=\frac{A_\lambda}{N},
\qquad
 d_\lambda=\frac{1+x_\lambda}{2}.
\tag{2}
\]

Thus `d_lambda` is the shell proportion on which the preferred `-1` sign fails, exactly as in `MC-291`--`MC-292`.

For a nonzero shell functional define its **source cost**

\[
\mathcal Q(\lambda)
:=
\min
\left\{
\prod_{p\in V}p:
V\subseteq\{p\le y:p\text{ odd prime}\},
\ \prod_{p\in V}\left(\frac pr\right)
=(-1)^{\lambda(s(r))}
\ \forall r\in\mathcal R_y
\right\}.
\tag{3}
\]

The minimum is over ambient lower-prime product-character representatives of the same functional on the actual shell. Every functional arising in `MC-289`--`MC-292` has such a representative. Source cost is deliberately not the rank, cardinality, or entropy cost from those findings.

There is an absolute `\kappa>0` such that, with

\[
D_y
:=
\exp\!\left(\kappa\frac{\log y}{\log\log y}\right),
\tag{4}
\]

the following holds for all sufficiently large `y`.

There is **at most one** nonzero shell functional `\lambda_*(y)` with `\mathcal Q(\lambda_*)\le D_y` for which the shell bias is not negligible. More precisely, after choosing `\kappa` sufficiently small,

\[
\boxed{
\sup_{\substack{\lambda\ne0,\ \mathcal Q(\lambda)\le D_y\\
                 \lambda\ne\lambda_*}}
|x_\lambda|
\ll
(\log y)^{-2},
}
\tag{5}
\]

where the exceptional functional is omitted if no Landau--Page exceptional primitive character exists at level `4D_y` or if that character does not induce a nontrivial shell functional.

Consequently, for every `\tau=\tau(y)` satisfying

\[
(\log y)^{-2}=o\!\left(\frac12-\tau\right),
\qquad 0\le\tau<\frac12,
\tag{6}
\]

the low-source-cost near-negative spectrum

\[
\mathcal E_{\tau,D_y}
:=
\{\lambda\ne0:\mathcal Q(\lambda)\le D_y,\ d_\lambda\le\tau\}
\tag{7}
\]

obeys

\[
\boxed{|\mathcal E_{\tau,D_y}|\le1.}
\tag{8}
\]

This applies far inside the live `MC-291`--`MC-292` regime `tau=c/t` with `t\asymp\log\log y`: a family of two or more independently near-negative modes cannot be built entirely from source characters of quasi-subpower cost `(4)`.

The possible singleton is much more rigid than an arbitrary analytic exception. If `d_{\lambda_*}\le\tau\le1/4`, then one of its two parity-equivalent ambient representatives is the unique exceptional primitive real character `\chi_*` at level `4D_y`, with real zero `\beta_*=1-\delta_*`, and

\[
\boxed{
\delta_*
\ll
\frac{\tau+(\log y)^{-2}}{\log y}.
}
\tag{9}
\]

In particular, at the near-affine scale `tau\asymp1/t` with `t\asymp\log\log y`,

\[
\boxed{
1-\beta_*
\ll
\frac1{\log y\,\log\log y}.
}
\tag{10}
\]

Thus the low-source-cost part of the endpoint obstruction has collapsed to a single classical object: an exceptionally close Landau--Siegel zero. Every additional independent near-negative mode required by a future argument must have source cost exceeding `(4)`.

No estimate for `M(x)` follows. The theorem does not rule out the singleton exceptional mode and says nothing comparable about generated characters above the source-cost threshold.

## 1. A low-cost shell functional gives two low-conductor real characters

Choose `V` attaining `(3)` and put

\[
m_V=\prod_{p\in V}p,
\qquad
\chi_V(n)=\prod_{p\in V}\left(\frac np\right).
\tag{11}
\]

Because the prime moduli are distinct, `chi_V` is a primitive real character of odd conductor `m_V`. Its parity twist `chi_4 chi_V` is primitive of conductor `4m_V`.

For every odd prime `r\equiv1\pmod4`, quadratic reciprocity gives

\[
\chi_V(r)
=
\prod_{p\in V}\left(\frac rp\right)
=
\prod_{p\in V}\left(\frac pr\right)
=(-1)^{\lambda(s(r))}.
\tag{12}
\]

Hence

\[
A_\lambda
=
\sum_{r\in\mathcal R_y}\chi_V(r).
\tag{13}
\]

Using the parity projector on odd primes,

\[
\mathbf1_{r\equiv1\ (4)}=\frac{1+\chi_4(r)}2,
\tag{14}
\]

the weighted shell sum is

\[
T_\lambda(y)
:=
\sum_{r\in\mathcal R_y}\chi_V(r)\log r
=
\frac12
\sum_{y<r\le2y\atop r\text{ prime}}
\bigl(\chi_V(r)+(\chi_4\chi_V)(r)\bigr)\log r.
\tag{15}
\]

Therefore a source-cost bound `m_V\le D_y` places both characters in conductor at most `4D_y`. This is the exact reason for applying Landau--Page at level `4D_y`, rather than separately to each lower-prime coordinate.

## 2. Every nonexceptional low-cost functional is balanced on the shell

Ruzsa and Sanders, *Difference sets and the primes* (Acta Arith. 131 (2008), arXiv `0710.0644`), Corollary 4.3 and Theorem 4.5, record the classical Landau--Page dichotomy in a growing-level form. At level `D` there is at most one exceptional primitive character, and every nonprincipal character of modulus at most `D` not induced by that exception satisfies

\[
\psi(x,\chi)
\ll
x\exp\!\left(
-\frac{c\log x}{\sqrt{\log x}+\log D}
\right)(\log D)^2
\tag{16}
\]

for an absolute `c>0`. The same input was already audited for the different positive-feedback object in `MC-069`.

Take `D=4D_y`. For `x\asymp y`, after shrinking the absolute `kappa` in `(4)` one may make the right side of `(16)` at most

\[
O\!\left(\frac{x}{(\log x)^4}\right).
\tag{17}
\]

Indeed `log D \ll kappa log y/log log y`, so the exponential in `(16)` becomes an arbitrarily strong fixed negative power of `log y` once `kappa` is chosen sufficiently small. Removing prime powers is negligible on this scale.

If neither `chi_V` nor `chi_4 chi_V` is induced by the exceptional primitive character, `(15)` therefore gives

\[
T_\lambda(y)
\ll
\frac{y}{(\log y)^4}.
\tag{18}
\]

Partial summation on `[y,2y]` converts `(18)` and the corresponding uniform bound for intermediate endpoints into

\[
A_\lambda
\ll
\frac{y}{(\log y)^5}.
\tag{19}
\]

The prime number theorem in the fixed progression `1 mod 4` gives

\[
N\sim\frac{y}{2\log y}.
\tag{20}
\]

Thus

\[
|x_\lambda|
\ll
(\log y)^{-4},
\tag{21}
\]

which is stronger than the deliberately relaxed display `(5)`.

No GRH or zero-density hypothesis enters. The only zero information is the unconditional classical exceptional-character dichotomy.

## 3. Page uniqueness becomes uniqueness of the shell functional

Suppose a low-cost `lambda` violates the nonexceptional estimate. Then one of the pair

\[
\chi_V,
\qquad
\chi_4\chi_V
\tag{22}
\]

must be induced by the unique exceptional primitive character `chi_*` at level `4D_y`.

At first sight the parity pair might appear to permit two exceptional shell modes. It does not. On the shell `r\equiv1 mod4`,

\[
\chi_4(r)=1,
\tag{23}
\]

so `chi_*` and `chi_4 chi_*` have exactly the same values. They therefore induce the same functional on every occupied shell cell and hence the same element of `H^*`.

Consequently the unique Landau--Page primitive exception produces at most one nontrivial shell functional. This proves `(5)` and `(8)`. Notice that this is stronger than a rank statement: the entire low-cost near-negative set has cardinality at most one.

The quotient nature of `H^*` causes no loophole. A shell functional may have several ambient product-character representatives, but if **any** representative of source cost at most `D_y` were nonexceptional in both parity forms, `(21)` would force the shell functional itself to be balanced. Hence every genuinely biased low-cost representative must point to the same exceptional shell functional.

## 4. Near-affinity forces an exceptionally close real zero

Assume now that the exceptional shell functional exists and

\[
d_{\lambda_*}\le\tau\le\frac14.
\tag{24}
\]

Let

\[
N_+=\#\{r\in\mathcal R_y:\chi_V(r)=+1\},
\qquad
W_+=\sum_{r\in\mathcal R_y\atop\chi_V(r)=+1}\log r,
\tag{25}
\]

and

\[
W=\sum_{r\in\mathcal R_y}\log r.
\tag{26}
\]

Since `N_+/N=d_{lambda_*}` and `log r` varies only from `log y` to `log(2y)`,

\[
\frac{W_+}{W}
\le
\tau\frac{\log(2y)}{\log y}.
\tag{27}
\]

Therefore

\[
\frac{T_{\lambda_*}(y)}{W}
=
2\frac{W_+}{W}-1
\le
-1+2\tau\left(1+O\!\left(\frac1{\log y}\right)\right).
\tag{28}
\]

Let `beta_*=1-delta_*` be the exceptional zero. Ruzsa--Sanders Theorem 4.5 gives the exceptional main term, and the parity partner in `(15)` is nonexceptional. Hence

\[
T_{\lambda_*}(y)
=
-\frac12
\frac{(2y)^{\beta_*}-y^{\beta_*}}{\beta_*}
+O\!\left(\frac{y}{(\log y)^4}\right).
\tag{29}
\]

Also

\[
W=\frac y2+O\!\left(\frac{y}{(\log y)^4}\right)
\tag{30}
\]

after harmlessly weakening the fixed-modulus prime-number-theorem error. Combining `(28)`--`(30)` gives

\[
\frac1y
\frac{(2y)^{\beta_*}-y^{\beta_*}}{\beta_*}
\ge
1-O\!left(\tau+(\log y)^{-4}\right).
\tag{31}
\]

The left side has the exact integral form

\[
\frac1y
\frac{(2y)^{\beta_*}-y^{\beta_*}}{\beta_*}
=
\frac1y\int_y^{2y}t^{-\delta_*}\,dt
=
y^{-\delta_*}\int_1^2u^{-\delta_*}\,du
\le
y^{-\delta_*}.
\tag{32}
\]

Thus

\[
y^{-\delta_*}
\ge
1-O\!\left(\tau+(\log y)^{-4}\right).
\tag{33}
\]

For `tau<=1/4` and sufficiently large `y`, taking logarithms proves the stronger form

\[
\delta_*
\ll
\frac{\tau+(\log y)^{-4}}{\log y},
\tag{34}
\]

and hence `(9)`--`(10)`.

This implication is one-way. A very close exceptional zero creates the correct negative prime bias direction, but `(34)` does not assert that every such zero forces the exact shell defect `tau` under arbitrary source conventions.

## 5. Interaction with the entropy/rank frontier

`MC-292` showed that linearly independent near-negative modes pay the entropy budget

\[
\sum_i\bigl(1-h_2(d_i)\bigr)
\le
\log_2(1/\eta),
\tag{35}
\]

but that inequality by itself does not know anything about conductor or source complexity. The present result supplies exactly one arithmetic axis that the finite-geometric argument lacked.

If

\[
\lambda_1,\ldots,\lambda_R
\tag{36}
\]

are linearly independent and all obey `d_{lambda_i}<=tau` in the regime `(6)`, then

\[
\boxed{
\#\{i:\mathcal Q(\lambda_i)\le D_y\}\le1.
}
\tag{37}
\]

Hence at least `R-1` independent near-negative directions must satisfy

\[
\boxed{
\mathcal Q(\lambda_i)>D_y.
}
\tag{38}
\]

The exceptional-spectrum escape has therefore acquired a genuine source-complexity cost: entropy limits how many independent biased directions can exist at all, while Landau--Page says that all but possibly one of those directions must live beyond a quasi-subpower lower-prime product conductor.

This does not yet combine into a contradiction. `MC-292` supplies an upper rank budget, not a lower rank requirement, and high-source-cost characters are not controlled here. The arithmetic frontier is narrowed rather than closed.

## 6. Prior art and novelty audit

The analytic theorem is classical. Landau's uniqueness of an exceptional primitive real character and the prime-number theorem for nonexceptional Dirichlet characters are standard; Ruzsa--Sanders Corollary 4.3 and Theorem 4.5 provide the growing-level formulation used in `(16)`. Their statements ultimately cite Davenport's *Multiplicative Number Theory*. `MC-069` already used the same theorem to collapse a different family of prime-conductor positive-feedback comparators.

`MC-284` used Page/Siegel technology in the present Legendre-shell setting, but only up to the smaller stretched-exponential **joint coordinate conductor** needed to prove every prescribed sign cell nonempty. The present statement asks a weaker marginal question -- whether an individual generated shell character can have order-one negative bias -- and therefore reaches the larger quasi-subpower **individual source-cost** range inherited from the pointwise character prime-number theorem.

A targeted literature search through 14 September 2026 recovered the standard exceptional-character theory and modern work using the same Landau--Page dichotomy, but no reason to treat `(5)`, `(8)`, or `(9)` as new general analytic-number-theory theorems. They are direct specializations and compositions of established character-PNT facts with the current shell quotient and defect variables. No standalone novelty is claimed.

The durable line-specific delta is the frontier separation: the low-cost sector of the `MC-291`--`MC-292` near-negative spectrum is not a large unresolved family. It consists of at most one Landau--Page mode, and near-affinity of that mode quantitatively forces its zero to lie within `O(tau/log y)` of `1`.

## Boundaries and falsification tests

- The shell restriction `r\equiv1 mod4` is load-bearing for the clean parity identification `(23)`. Without it, `chi_*` and `chi_4 chi_*` need not define the same shell functional.
- Source cost `mathcal Q(lambda)` is the **minimum product of lower-prime coordinates representing the functional on the actual shell**. It is not raw support size, dual rank, primitive conductor, or the joint conductor of a whole exceptional family.
- The theorem controls each low-cost mode individually. It does not say that the union of the coordinate supports of many high-cost modes has any particular structure.
- The quasi-subpower range `(4)` depends on choosing a sufficiently small absolute `kappa`, exactly as in `MC-069`. No claim is made for every `D=y^{o(1)}`.
- The quantitative decay power in `(5)` is inessential. Shrinking `kappa` trades source-cost range for a stronger fixed logarithmic error; the durable content is uniform `o(1)` bias outside the unique exceptional mode.
- The zero-closeness statement `(9)` is conditional on observing near-affinity of the exceptional shell mode. It neither proves existence of a Landau--Siegel zero nor excludes one.
- A high-conductor generated character may still have extreme shell bias. Burgess/Pólya--Vinogradov bounds for complete or integer character sums do not automatically control this prime-shell regime at the needed moving conductor scale.
- Nothing here supplies a lower bound on the participation ratio `eta`, forces many independent near-negative modes, or improves `M(x)`.
- No RH, GRH, reciprocal-zeta continuation, random-character heuristic, or unproved character-sum estimate is used.

## Consequence for the research line

The arithmetic bottleneck after `MC-292` is now split by source complexity. Below `exp(kappa log y/log log y)`, there is no broad exceptional spectrum to control: every generated shell character is asymptotically balanced except possibly the unique Landau--Page mode, and an almost-affine bias in that mode would require a zero at distance only `O(1/(log y log log y))` from `1` at the live defect scale.

Accordingly, further progress on the near-negative spectrum should not spend effort improving generic finite-geometric rank estimates in the low-cost sector. The remaining live targets are: rule out or exploit the single exceptional mode using additional arithmetic structure, force high source cost to interact with multiplicity/participation, or obtain arithmetic control for the high-cost generated family. Those are genuinely different from the classical entropy and odd-girth mechanisms already exhausted by `MC-288`--`MC-292`.
