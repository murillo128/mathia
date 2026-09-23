# MC-485 — Complete q-shift frame identifies the coefficient-blind L2 ceiling

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `CLASSICAL-CORRELATION+DERIVED-APPLICATION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NON-RH`.

## Claim

`MC-484` leaves a genuinely two-dimensional first-exit family in which the same prime variable `q` moves both the residual pair-sieve condition and the translated-ratio character phase. This finding isolates the character part and asks whether the motion

\[
\delta_q\equiv hq^{-1}\pmod p
\]

already supplies useful `q`-averaging before the moving sieve mask is used.

For an odd prime `p`, a nonprincipal multiplicative character `chi` modulo `p`, and `h not\equiv0 (mod p)`, extend `chi` by `chi(0)=0` and define, for `q,m in F_p^*`,

\[
K_q(m):=\chi(m+hq^{-1})\overline{\chi(m)}.
\tag{1}
\]

Let `G` be the Gram matrix of the complete `q`-family,

\[
G_{m,n}:=\sum_{q\in\mathbf F_p^*}K_q(m)\overline{K_q(n)}.
\tag{2}
\]

If `J` is the all-ones matrix and `v_m=\overline{\chi(m)}`, then

\[
\boxed{G=pI-J-vv^*.}
\tag{3}
\]

Consequently, for every coefficient vector `b=(b_m)_{m\in F_p^*}`,

\[
\boxed{
\sum_{q\in\mathbf F_p^*}
\left|\sum_{m\in\mathbf F_p^*}b_mK_q(m)\right|^2
=
p\sum_m|b_m|^2
-
\left|\sum_m b_m\right|^2
-
\left|\sum_m b_m\overline{\chi(m)}\right|^2.
}
\tag{4}
\]

The spectrum is therefore exactly

\[
1,\ 1,\ \underbrace{p,\ldots,p}_{p-3\ \mathrm{times}},
\tag{5}
\]

with the two eigenvalue-`1` directions spanned by the constant vector and the character vector `v`. Thus the moving translated-ratio phases form an almost-tight frame: apart from two explicit low-rank directions, the complete source-shift family preserves coefficient `L^2` energy at scale `p` rather than creating an extra saving.

This gives a precise no-go for a natural simplification of the `MC-484` route. If the `q`-dependent residual sieve/interval data are frozen or majorized to a common coefficient vector and one then relies only on the motion `h/q` for a coefficient-blind `L^2` gain, the complete-family operator norm is `sqrt(p)`. For any subset `Q subset F_p^*`,

\[
\left|
\sum_{q\in Q}\sum_m b_mK_q(m)
\right|
\le
\sqrt{|Q|p}\,\|b\|_2.
\tag{6}
\]

If `b` is supported on `M` points with `|b_m|<=1`, this becomes

\[
\left|
\sum_{q\in Q}\sum_m b_mK_q(m)
\right|
\le
\sqrt{|Q|pM}.
\tag{7}
\]

On a first-exit rectangle with `|Q|M asymp H`, the generic frame bound is therefore `sqrt(pH)`. At the subconductor scale `H<=p`, this does not improve the trivial size `H`. The conclusion is deliberately narrow: **bare inverse-shift motion does not by itself furnish a uniform subconductor saving for arbitrary common coefficients.** Any surviving route must exploit either special concentration of the coefficient vector in the two exceptional modes, cancellation specific to an incomplete `q`-set, or — most importantly for `MC-484` — the joint `q`-dependence of the residual pair-sieve mask and source interval.

## 1. Exact Gram calculation

Because inversion permutes `F_p^*`, write `x=q^{-1}` in `(2)`. Then

\[
G_{m,n}
=
\overline{\chi(m)}\chi(n)
\sum_{x\in\mathbf F_p^*}
\chi(m+hx)\overline{\chi(n+hx)}.
\tag{8}
\]

For `m=n`, exactly one nonzero value of `x`, namely `x=-m/h`, makes the character argument vanish. Hence

\[
G_{m,m}=p-2.
\tag{9}
\]

Now assume `m!=n`. First sum over all `x in F_p`. The exceptional point `x=-n/h` contributes zero, and on its complement the fractional-linear map

\[
y=\frac{m+hx}{n+hx}
\tag{10}
\]

is a bijection from `F_p\setminus{-n/h}` onto `F_p\setminus{1}`. Therefore

\[
\sum_{x\in\mathbf F_p}
\chi(m+hx)\overline{\chi(n+hx)}
=
\sum_{y\in\mathbf F_p\setminus\{1\}}\chi(y)
=-1,
\tag{11}
\]

because `chi` is nonprincipal and `sum_y chi(y)=0`. Removing the `x=0` term yields

\[
\sum_{x\in\mathbf F_p^*}
\chi(m+hx)\overline{\chi(n+hx)}
=
-1-\chi(m)\overline{\chi(n)}.
\tag{12}
\]

Substitution into `(8)` gives

\[
G_{m,n}=-1-\overline{\chi(m)}\chi(n),
\qquad m\ne n.
\tag{13}
\]

Equations `(9)` and `(13)` are exactly `(3)`: on the diagonal, `pI-J-vv^*` equals `p-2`, and off the diagonal it equals `-1-v_m\overline{v_n}`.

## 2. Spectrum and exact frame identity

The constant vector `mathbf 1` and `v` are orthogonal because `chi` is nonprincipal, and both have squared norm `p-1`. Hence

\[
J\mathbf1=(p-1)\mathbf1,
\qquad
vv^*v=(p-1)v,
\tag{14}
\]

while each rank-one operator kills the other vector. Thus `(3)` acts by eigenvalue `1` on `span{mathbf1,v}` and by eigenvalue `p` on its orthogonal complement. This proves `(5)`.

Taking the quadratic form of `(3)` against `b` gives `(4)` exactly. In particular,

\[
\sum_q\left|\sum_m b_mK_q(m)\right|^2
\le p\|b\|_2^2,
\tag{15}
\]

and the constant `p` is attained on every nonzero vector orthogonal to both exceptional modes. So `sqrt(p)` is the exact norm of the complete analysis operator, not an artifact of Cauchy-Schwarz.

For a subset `Q`, applying Cauchy-Schwarz in `q` and then enlarging the energy to the complete family gives `(6)`. The argument is intentionally coefficient-blind: it assumes no structure of `b` beyond its `L^2` norm.

## 3. What this kills and what remains live

The finding kills a specific shortcut suggested by the new source variable in `MC-484`:

- freeze the first-exit pair-sieve mask after reparameterization;
- replace the `q`-dependent shortened intervals by one common coefficient profile;
- average only the translated character phases `K_{h/q}`;
- expect the inverse motion of the shift to supply a new conductor-power saving automatically.

That shortcut has no generic subconductor gain through the complete-family `L^2` mechanism. The character rows are not becoming mutually orthogonal enough to lower the operator norm below `sqrt(p)`; on a codimension-two subspace they are exactly tight at that scale.

The result does **not** kill the actual `MC-484` family. There the coefficients are not common:

\[
b_{q,m}
=
\mathbf1_{m\ \mathrm{in\ the\ q\text{-}dependent\ interval}}
\mathbf1_{(m(m+\delta_q),P(q))=1}
\tag{16}
\]

up to the two first-exit branches and harmless affine changes. Both the cutoff `P(q)` and the translated roughness shift depend on the same `q` that moves the character phase. Equation `(4)` says that discarding this dependence before dispersion throws away the only source-variable structure not already exhausted by the bare character frame.

There are two narrower escape hatches even with common coefficients. First, a particular `b` may be unusually concentrated in `span{mathbf1,v}`, where the frame eigenvalue is `1` rather than `p`. Such concentration must be proved from the arithmetic coefficients; it cannot be assumed from the character motion. Second, an incomplete set of source primes may possess additional cancellation not visible in the complete-family norm. This finding does not rule out an incomplete-prime estimate of that kind.

## 4. Adversarial boundaries

The hypotheses `h not\equiv0 (mod p)` and nonprincipal `chi` are essential. If `h=0`, the translated-ratio phase degenerates. If `chi` is principal, the rank structure changes and there is no character oscillation to analyze.

The exact frame uses all nonzero residue classes `q mod p`, each once. The first-exit variable in `MC-484` runs over actual primes in an interval. When those primes occupy only a subset of residues, `(6)` is a valid coarse completion bound after identifying distinct residue classes, but `(3)` is not an exact Gram law for the prime subset. If source primes repeat residue classes modulo `p`, multiplicity weights must be retained and are outside the unweighted statement above.

Likewise, `(7)` is not a lower bound and does not assert that every common coefficient vector has size `sqrt(pH)`. It identifies the sharp **uniform operator-norm ceiling** of this proof architecture. Special coefficients or specially distributed incomplete source sets can do better.

Finally, no statement here controls the actual `q`-dependent pair-sieve mask. That dependence is precisely what remains to be exploited or killed next.

## 5. Prior-art and novelty audit

The complete shifted multiplicative-character correlation used in `(11)` is classical finite-field/Jacobi-sum orthogonality. No novelty is claimed for that identity or for complete rational-character sum technology. The line already records Cochrane--Pinner (`MC-S55`) as a classical anchor for complete multiplicative-character sums of bounded-complexity rational functions, and the standard Jacobi-sum formalism contains the same inverse-character `-1` phenomenon after an affine/fractional-linear change of variables.

The line-specific contribution here is the exact Gram organization `(3)` for the inverse-shift family forced by `MC-484`, its two exceptional modes, and the resulting quantitative audit of the proposed source-variable averaging route. A targeted search found standard Jacobi-sum/shifted-correlation literature and broader shifted-character-sum results, but no reason to regard the `MC-484` application itself as an existing theorem. Accordingly this finding is classified as a derived application of a classical correlation identity, not as a new finite-field theorem.

## 6. Relation to the current frontier

`MC-471` identifies the translated-ratio kernel as the base hard pair-sieve object. `MC-477` shows why denominator-free completion is attractive, while `MC-484` is the first accepted route that removes the selector obstruction without destroying the source factor variable. The present finding now separates that new resource into two pieces:

1. the bare moving character shift, whose complete-family coefficient-blind `L^2` behavior is exhausted by `(3)`--`(7)`; and
2. the genuinely coupled `q`-dependent mask/source geometry, which remains unresolved.

Therefore the next decisive object should not be another unweighted average of `K_{h/q}`. It should be a **weighted Gram/dispersion form with the first-exit pair-sieve mask still inside the `q,m` sum**. A power saving there would use information absent from `(3)`; a no-go showing that the moving mask still leaves the norm at the same scale would close the surviving branch more decisively.