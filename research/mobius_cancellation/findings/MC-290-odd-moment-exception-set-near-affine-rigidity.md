# MC-290 — Odd moments force a small exceptional character family toward an affine halfspace

**Status:** `EXACT-DERIVED` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`

## Claim

Continue the collision-rich odd-shell setup and notation of `MC-289`. Thus

\[
S\subset H\cong \mathbf F_2^r,
\qquad |H|=2^r=:q,
\]

has no odd zero-sum subset of cardinality at most the odd target weight `t>=3`; the shell multiplicities are `n_s>=1`; and

\[
N=\sum_{s\in S}n_s,
\qquad
E_2=\sum_{s\in S}n_s^2,
\qquad
\eta=\frac{N^2}{qE_2}.
\tag{1}
\]

For `lambda in H^*`, write

\[
A_\lambda=\sum_{s\in S}n_s(-1)^{\lambda(s)}.
\tag{2}
\]

`MC-289` proves, for every odd `m<=t`,

\[
\sum_{\lambda\ne0} A_\lambda^m=-N^m,
\qquad
\sum_{\lambda\ne0} A_\lambda^2
=N^2\left(\frac1\eta-1\right).
\tag{3}
\]

Fix an odd `m` with `3<=m<=t` and a one-sided tolerance `0<delta<1`. Let

\[
E\subset H^*\setminus\{0\}
\tag{4}
\]

be a set of `J=|E|` exceptional characters such that every character outside `E` obeys

\[
\frac{A_\lambda}{N}\ge-\delta.
\tag{5}
\]

There is no loss in taking every member of `E` to have `A_lambda<0`, since a nonnegative coefficient already satisfies `(5)`. Put

\[
a_\lambda=-\frac{A_\lambda}{N}\in(0,1]
\qquad(\lambda\in E).
\tag{6}
\]

Then the exceptional family must carry almost all of the forbidden odd moment:

\[
\boxed{
1-\sum_{\lambda\in E}a_\lambda^m
\le
\delta^{m-2}
\left(
\frac1\eta-1-\sum_{\lambda\in E}a_\lambda^2
\right).
}
\tag{7}
\]

In particular, with

\[
\varepsilon_m
:=
\delta^{m-2}\left(\frac1\eta-1\right),
\tag{8}
\]

one has

\[
\boxed{
\sum_{\lambda\in E}a_\lambda^m\ge1-\varepsilon_m.
}
\tag{9}
\]

If `J>=1` and `varepsilon_m<1`, some exceptional character therefore satisfies

\[
\boxed{
-
\frac{A_\lambda}{N}
\ge
\left(\frac{1-\varepsilon_m}{J}\right)^{1/m}.
}
\tag{10}
\]

This has a direct weighted-affine interpretation. For the character supplied by `(10)`, let

\[
N_+(\lambda)
:=
\sum_{\substack{s\in S\\\lambda(s)=0}}n_s
\tag{11}
\]

be the shell mass on the `+1` side of its sign. Since

\[
A_\lambda=2N_+(\lambda)-N,
\tag{12}
\]

`(10)` gives

\[
\boxed{
\frac{N_+(\lambda)}N
\le
\frac12
\left[
1-
\left(\frac{1-\varepsilon_m}{J}\right)^{1/m}
\right].
}
\tag{13}
\]

Thus a theorem that controls **all but a small exceptional set** of generated quadratic characters cannot leave the remaining modes arbitrary. If

\[
\varepsilon_m=o(1),
\qquad
\log J=o(m),
\tag{14}
\]

then one exceptional generated character is `-1` on a `1-o(1)` fraction of the shell multiplicity. The collision-rich non-affine escape is forced toward a weighted affine hyperplane.

The one-exception case is especially rigid. If `J=1`, write `a=-A_{\lambda_*}/N`. Then

\[
1-a^m
\le
\delta^{m-2}
\left(\frac1\eta-1-a^2\right)
\le\varepsilon_m.
\tag{15}
\]

Consequently

\[
\frac{N_+(\lambda_*)}{N}
\le
\frac{1-(1-\varepsilon_m)^{1/m}}2.
\tag{16}
\]

When `varepsilon_m<=1/2`, the elementary factorization of `1-u^m` yields the explicit bound

\[
\boxed{
\frac{N_+(\lambda_*)}{N}
\le
\frac{\varepsilon_m}{2m(1-\varepsilon_m)}
\le
\frac{\varepsilon_m}{m}.
}
\tag{17}
\]

At the sharp Geelen-scale effective occupancy

\[
\eta\asymp t2^{-t},
\qquad m=t,
\tag{18}
\]

a one-exception bound with `delta=1/2` already gives

\[
\varepsilon_t=O(t^{-1}),
\qquad
\frac{N_+(\lambda_*)}{N}=O(t^{-2}).
\tag{19}
\]

For any fixed `delta<1/2`, `varepsilon_t` is exponentially small in `t`, so the allowed `+1` shell mass is exponentially smaller still up to the factor `1/t`.

This strictly refines the scalar conclusion of `MC-289`. There, the odd-moment stack forced at least one substantially negative generated character whenever `eta` was not too small. Here, if analytic input permits only a small number of badly negative modes, the same moments force those modes to absorb essentially the entire odd-moment deficit, which pushes at least one of them toward the exact affine endpoint `A_lambda=-N`.

No bound for `M(x)` is improved. The theorem is an exact interface between the finite odd-girth mechanism and any arithmetic result that supplies a one-sided character bound with a controlled exceptional set.

## 1. Remove the exceptional modes from the exact odd moment

Normalize

\[
x_\lambda:=\frac{A_\lambda}{N}.
\tag{20}
\]

For every odd `m<=t`, `(3)` becomes

\[
\sum_{\lambda\ne0}x_\lambda^m=-1,
\qquad
\sum_{\lambda\ne0}x_\lambda^2=\frac1\eta-1.
\tag{21}
\]

For `lambda notin E`, condition `(5)` says `x_lambda>=-delta`. Because `m` is odd,

\[
x_\lambda^m
\ge
-\delta^{m-2}x_\lambda^2.
\tag{22}
\]

Indeed `(22)` is automatic for `x_lambda>=0`; for `-delta<=x_lambda<0` it is just `|x_lambda|^{m-2}<=delta^{m-2}`.

The exact residual odd moment is

\[
\sum_{\lambda\notin E,\lambda\ne0}x_\lambda^m
=
-1-\sum_{\lambda\in E}x_\lambda^m
=
-1+\sum_{\lambda\in E}a_\lambda^m.
\tag{23}
\]

Applying `(22)` to the same residual family gives

\[
-1+\sum_{\lambda\in E}a_\lambda^m
\ge
-\delta^{m-2}
\sum_{\lambda\notin E,\lambda\ne0}x_\lambda^2.
\tag{24}
\]

By the second identity in `(21)`,

\[
\sum_{\lambda\notin E,\lambda\ne0}x_\lambda^2
=
\frac1\eta-1-
\sum_{\lambda\in E}a_\lambda^2.
\tag{25}
\]

Substituting `(25)` into `(24)` proves `(7)`. Dropping the nonnegative correction `delta^{m-2} sum_{E} a_lambda^2` proves `(9)`.

The argument uses no graph approximation and no asymptotic step. It is simply the exact odd Fourier moment from the forbidden short relations plus a one-sided truncation of the residual spectrum.

## 2. A small exceptional family must contain a nearly constant-negative mode

If `J>=1`, `(9)` and the definition

\[
a_{\max}:=\max_{\lambda\in E}a_\lambda
\tag{26}
\]

give

\[
J a_{\max}^m
\ge
\sum_{\lambda\in E}a_\lambda^m
\ge1-\varepsilon_m.
\tag{27}
\]

This is exactly `(10)`. Combining with `(12)` proves `(13)`.

The asymptotic condition `(14)` now has a transparent meaning. Taking logarithms in `(10)`,

\[
\log a_{\max}
\ge
-\frac{\log J}{m}
+
\frac{\log(1-\varepsilon_m)}m.
\tag{28}
\]

If `log J=o(m)` and `varepsilon_m=o(1)`, the right side is `o(1)`, so `a_max=1-o(1)`. The weighted shell therefore concentrates asymptotically on the affine halfspace `lambda(s)=1` for that exceptional functional.

For `J=1`, `(15)` is the exact specialization of `(7)`. From `a^m>=1-varepsilon_m`,

\[
1-a
\le
1-(1-\varepsilon_m)^{1/m}.
\tag{29}
\]

Writing `u=(1-varepsilon_m)^{1/m}` and using

\[
1-u
=
\frac{1-u^m}{1+u+\cdots+u^{m-1}}
\le
\frac{\varepsilon_m}{m u^{m-1}}
\le
\frac{\varepsilon_m}{m(1-\varepsilon_m)}
\tag{30}
\]

proves `(17)`.

The endpoint `a=1` is exactly the affine obstruction from `MC-286` and `MC-288`: `lambda(s)=1` on every occupied cell. Thus `(13)` is a quantitative weighted interpolation between the non-affine branch and that exact obstruction.

## 3. The Geelen scale has a sharp half-bias transition

Take `m=t` and suppose

\[
\eta\asymp t2^{-t}.
\tag{31}
\]

Then

\[
\varepsilon_t
=
\delta^{t-2}\left(\frac1\eta-1\right)
\asymp
\frac{4}{t}(2\delta)^{t-2}
\tag{32}
\]

up to fixed multiplicative constants coming from `(31)`.

This exposes a threshold already latent in `MC-289` but not visible from its single-minimum formulation.

If `delta<1/2` is fixed, `(32)` decays exponentially, so even one permitted exceptional mode must be exponentially close to the exact constant-negative affine character. If `delta=1/2`, `(32)` is only `O(1/t)`, but `(17)` still forces the exceptional character's positive-side shell mass down to `O(1/t^2)`. If `delta>1/2`, the residual family can absorb the odd moment at this density scale and the argument ceases to force near-affinity.

Thus `1/2` is the natural one-sided family-cancellation threshold for the Geelen-scale occupancy `eta~t2^{-t}`. This matches the order-one bias forced by `MC-289` but sharpens its interpretation: **a family theorem beating negative bias `1/2` outside a tiny exceptional set does not merely identify an exceptional character; it forces an almost affine shell concentration.**

## 4. Arithmetic interface: exceptional-character theorems become concentration theorems

For the Legendre shell of `MC-281`--`MC-289`, every `A_lambda` is an actual generated quadratic product-character sum

\[
A_\lambda
=
\sum_{\rho\in\mathcal R_y}\chi_\lambda(\rho).
\tag{33}
\]

Therefore `(7)`--`(13)` can consume analytic statements of the following form directly:

> outside at most `J` generated quadratic characters, every shell sum has negative relative bias at most `delta`.

The output is no longer merely another character-sum bound. If `delta^{t-2}(eta^{-1}-1)` is small, the exceptional family must contain a character whose `-1` level set carries almost all shell multiplicity.

The Page--Siegel mechanism audited in `MC-284` is the cleanest classical example of an analytic theorem with a one-character exception in a bounded conductor range. In that exact moderate-total-conductor regime, `MC-284` already proves the stronger statement of full Legendre-cell coverage, so the present result is **not** a new conductor improvement and should not be used to repackage `MC-284`.

Its value is as a composable interface when later arithmetic information controls a broad generated family while allowing a small exceptional subfamily, without giving the simultaneous full-cell theorem required by `MC-284`. In such a setting, the residual arithmetic escape is not generic character bias: it is weighted near-affine concentration around one of the exceptional modes.

This also separates two future proof obligations cleanly:

1. obtain an independent lower bound on `eta` strong enough that `varepsilon_t` is small for the available family threshold `delta`; and
2. exclude, or exploit, the resulting near-affine exceptional character by arithmetic information not already equivalent to the desired Mertens bound.

Neither obligation is discharged here.

## 5. Prior art and novelty audit

The spectral mechanism is classical. Vanishing odd closed-walk counts give vanishing odd spectral moments, and high odd girth is routinely translated into restrictions on the negative spectrum. Aida Abiad, Vladislav Taranchuk and Thijs van Veluw, *On the sum of the largest and smallest eigenvalues of odd-cycle free graphs*, Electronic Journal of Combinatorics 33 (2026), P2.31, DOI `10.37236/14427`, use this high-odd-girth/least-eigenvalue viewpoint. Fredy Yip, *On the sum of the largest and smallest eigenvalues of graphs with high odd girth*, Linear Algebra and its Applications 736 (2026), DOI `10.1016/j.laa.2026.01.027`, explicitly formulates the vanishing of traces of odd polynomials below the odd-girth threshold and combines those identities with even spectral control.

A targeted literature search found these and adjacent least-eigenvalue/near-bipartiteness results, but no reason to treat `(7)` as a new general spectral theorem. It is an elementary exceptional-set truncation of the exact odd moments already derived in `MC-289`. No novelty is claimed for odd trace identities, Fourier diagonalization, least-eigenvalue methods, or Page exceptional-character theory.

The durable research contribution recorded here is the exact specialization needed by the current shell frontier: a **small family of analytically uncontrolled generated characters must absorb the full forbidden odd-moment deficit**, and at the Geelen occupancy scale this forces a quantitative near-affine concentration rather than merely one moderately negative character.

## Boundaries and falsification tests

- The no-short-odd-relation hypothesis inherited from `MC-288` is essential. Without it the exact odd moments `(3)` do not vanish in the required range.
- `eta` is the weighted participation ratio from `MC-289`, not raw support density. If multiplicities drive `eta` far below the Geelen support density, `varepsilon_m` can be at least one and the conclusion becomes vacuous.
- The family input is one-sided. A theorem controlling only positive character bias does not supply `(5)`.
- The exceptional set must be counted among **distinct characters on `H`**. Different ambient presentations of the same functional do not create multiple exceptions.
- The conclusion is weighted near-affinity, not support containment. A small number of shell primes may remain on the `+1` side even when `(13)` is strong.
- A large exceptional family can absorb the odd moment without any one coefficient approaching `-N`; the condition `log J=o(m)` in `(14)` is therefore substantive.
- Page uniqueness applies only inside its conductor/height range and after passing to primitive inducing characters. Nothing here bounds the conductors of the generated characters, so Page cannot be applied globally by fiat.
- The result does not prove that an exceptional Landau--Siegel character exists, nor that such a character can or cannot produce the required shell concentration.
- No RH, GRH, reciprocal-zeta continuation, random-walk model, or probabilistic independence assumption is used.

## Consequence for the research line

`MC-289` reduced the collision-rich odd-girth escape to either tiny effective occupancy or one substantially negative generated quadratic character. The present result makes that reduction robust to realistic analytic family theorems with exceptions. If all but a small exceptional family enjoy one-sided cancellation beyond the `1/2` threshold at Geelen-scale occupancy, the exceptions cannot merely be somewhat biased: one must become almost the exact affine obstruction already isolated in `MC-286`.

The frontier is therefore narrower. A useful arithmetic attack may now target **near-affine exceptional concentration** rather than uniform cancellation of every generated character. Conversely, any proposed small-exception family estimate that does not control `eta` cannot close the route; the participation-ratio escape remains genuine.