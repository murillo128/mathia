# AF-111 — Regularized determinants have a sharp integer summability fidelity threshold

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-REGULARIZED-FREDHOLM`, `SCHATTEN-SUMMABILITY-THRESHOLD`, `REGULARIZATION-LOSS`, `ZERO-FREE-FACTOR-FIDELITY`, `NO-NOVELTY-CLAIM`

## Claim

Let `H` be a complex separable Hilbert space, let

\[
1\le p<\infty,
\]

and let `(A_i)` be a net of operators in the Schatten class `\mathcal S_p(H)` such that

\[
\sup_i \|A_i\|_p\le C<\infty,
\qquad
\|A_i\|\longrightarrow0,
\tag{1}
\]

where `\|\cdot\|` is the operator norm. Let `r\in\mathbb N` be an integer with `r\ge p`, so that `A_i\in\mathcal S_r(H)` and the `r`-regularized Fredholm determinant

\[
\det_r(I+zA_i)
\]

is defined.

AF-110 treated the trace-class case `p=1`: an infinitesimal trace-class cloud can leave one first-order trace channel in the ordinary determinant, while `\det_2` removes that channel. The general Schatten picture has a sharp discrete feature because the determinant regularization order is integral.

### 1. Every supercritical regularization collapses to one

If

\[
r>p,
\tag{2}
\]

then

\[
\boxed{
\det_r(I+zA_i)\longrightarrow1
\quad\text{locally uniformly on }\mathbb C.
}
\tag{3}
\]

Thus a bounded amount of `\mathcal S_p` mass may remain while the complete value-level `r`-regularized determinant becomes asymptotically trivial.

In particular, if `p` is not an integer and

\[
r=\lceil p\rceil,
\tag{4}
\]

then the **smallest admissible integer regularization already lies strictly above the summability exponent**, and (3) is automatic under (1).

### 2. At an integer critical order, exactly one moment may survive

Suppose instead that

\[
p=r=m\in\mathbb N.
\tag{5}
\]

Then for every fixed `R>0`,

\[
\boxed{
\sup_{|z|\le R}
\left|
\log\det_m(I+zA_i)
-
\frac{(-1)^{m+1}}{m}z^m\operatorname{Tr}(A_i^m)
\right|
\longrightarrow0.
}
\tag{6}
\]

Consequently, if

\[
\operatorname{Tr}(A_i^m)\longrightarrow\tau\in\mathbb C,
\tag{7}
\]

then

\[
\boxed{
\det_m(I+zA_i)
\longrightarrow
\exp\!\left(
\frac{(-1)^{m+1}}{m}\tau z^m
\right)
}
\tag{8}
\]

locally uniformly on `\mathbb C`.

All trace moments of order `>m` disappear under (1); only the critical `m`-th moment can remain at order one. The limit (8) is zero-free, so passing further to the zero divisor erases this surviving channel completely.

### 3. One additional regularization always erases the critical channel

Under (5), the standard regularizations satisfy the exact identity

\[
\det_{m+1}(I+zA)
=
\det_m(I+zA)
\exp\!\left(
\frac{(-1)^m}{m}z^m\operatorname{Tr}(A^m)
\right),
\tag{9}
\]

and therefore

\[
\boxed{
\det_{m+1}(I+zA_i)\longrightarrow1
}
\tag{10}
\]

locally uniformly. Thus the step

\[
\det_m \longrightarrow \det_{m+1}
\]

is not a harmless normalization in this regime: it quotients out the only aggregate spectral moment not already forced to zero by infinitesimal operator scale.

AF-110 is exactly the endpoint `m=1`: ordinary Fredholm determinants may converge to `e^{\tau z}`, while `\det_2` converges to `1`.

### 4. The threshold is attained by positive finite-rank clouds

Let `(e_j)` be an orthonormal basis, let `Q_n` be the projection onto

\[
\operatorname{span}\{e_1,\ldots,e_n\},
\]

and for an integer `m\ge1` define

\[
A_n=n^{-1/m}Q_n.
\tag{11}
\]

Then

\[
A_n\ge0,
\qquad
\|A_n\|=n^{-1/m}\to0,
\qquad
\|A_n\|_m^m=1,
\qquad
\operatorname{Tr}(A_n^m)=1.
\tag{12}
\]

Therefore

\[
\det_m(I+zA_n)
\longrightarrow
\exp\!\left(\frac{(-1)^{m+1}}{m}z^m\right),
\tag{13}
\]

while

\[
\det_{m+1}(I+zA_n)\longrightarrow1.
\tag{14}
\]

So the critical residual in (8) is not an artifact of the estimate. An order-one amount of Schatten resource can survive exactly in the first trace moment not removed by the regularization.

### 5. Noninteger summability has no critical determinant channel

Let `p\notin\mathbb N`, set `r=\lceil p\rceil`, and define

\[
B_n=n^{-1/p}Q_n.
\tag{15}
\]

Then

\[
\|B_n\|_p^p=1,
\qquad
\|B_n\|=n^{-1/p}\to0,
\tag{16}
\]

but for the first admissible regularization order `r>p`,

\[
\det_r(I+zB_n)\longrightarrow1.
\tag{17}
\]

Equivalently,

\[
\operatorname{Tr}(B_n^r)
=
n^{1-r/p}
\longrightarrow0.
\tag{18}
\]

Hence the integer lattice of regularization orders creates a genuine threshold effect: diffuse `\mathcal S_p` mass can leave a determinant-scale residue only when the summability exponent itself lands exactly on an integer regularization order.

## Derivation

### 1. A single Schatten estimate controls every surviving trace moment

Fix an integer `r\ge p` and an integer `k\ge r`. Since `p\le r\le k`, the inclusions of Schatten ideals give

\[
A_i\in\mathcal S_p
\subseteq
\mathcal S_r
\subseteq
\mathcal S_k.
\tag{19}
\]

Schatten Hölder with `r` copies of `A_i` gives

\[
\|A_i^r\|_1
\le
\|A_i\|_r^r.
\tag{20}
\]

If `(s_j(A_i))` are the singular values, then

\[
\|A_i\|_r^r
=
\sum_j s_j(A_i)^r
\le
\|A_i\|^{\,r-p}
\sum_j s_j(A_i)^p
=
\|A_i\|^{\,r-p}\|A_i\|_p^p.
\tag{21}
\]

Using the ideal property for the remaining `k-r` factors,

\[
\|A_i^k\|_1
\le
\|A_i\|^{\,k-r}\|A_i^r\|_1
\le
\|A_i\|^{\,k-p}\|A_i\|_p^p.
\tag{22}
\]

Therefore

\[
\boxed{
|\operatorname{Tr}(A_i^k)|
\le
C^p\|A_i\|^{\,k-p}
\qquad(k\ge r).
}
\tag{23}
\]

This is the resource estimate behind the threshold. The exponent `k-p` is positive for every available determinant term when `r>p`, but becomes zero at exactly one possible index when `r=p=m` is integral.

### 2. The regularized trace-log starts at the regularization order

For `A\in\mathcal S_r`, the standard `r`-regularized determinant cancels the first `r-1` terms of the ordinary Fredholm logarithm. On any disk where `|z|\|A\|<1`,

\[
\log\det_r(I+zA)
=
\sum_{k=r}^{\infty}
\frac{(-1)^{k+1}}{k}
z^k\operatorname{Tr}(A^k),
\tag{24}
\]

with the logarithm normalized to vanish at `z=0`.

Fix `R>0`. By (1), eventually

\[
R\|A_i\|<1.
\tag{25}
\]

Combining (23) and (24), and discarding the harmless factor `1/k`, gives

\[
\begin{aligned}
\sup_{|z|\le R}
|\log\det_r(I+zA_i)|
&\le
C^p
\sum_{k=r}^{\infty}
R^k\|A_i\|^{\,k-p}
\\
&=
\frac{
C^p R^r \|A_i\|^{\,r-p}
}{
1-R\|A_i\|
}.
\end{aligned}
\tag{26}
\]

If `r>p`, the right-hand side tends to zero. Exponentiating proves (3).

### 3. The critical integer term is the unique nonvanishing order

Now take `p=r=m\in\mathbb N`. Separate the `k=m` term in (24):

\[
\log\det_m(I+zA_i)
=
\frac{(-1)^{m+1}}{m}
z^m\operatorname{Tr}(A_i^m)
+
\mathcal R_i(z).
\tag{27}
\]

For `|z|\le R`, (23) gives

\[
|\mathcal R_i(z)|
\le
C^m
\sum_{k=m+1}^{\infty}
R^k\|A_i\|^{\,k-m}
=
\frac{
C^m R^{m+1}\|A_i\|
}{
1-R\|A_i\|
}.
\tag{28}
\]

The right-hand side tends to zero, proving (6). Equation (8) follows from (7) by exponentiation.

Taking regularization order `m+1` puts the problem back in the supercritical case `r>p`, proving (10).

### 4. The projection clouds realize both sides sharply

For (11), the nonzero singular values are `n` copies of `n^{-1/m}`. Thus

\[
\|A_n\|_m^m
=
n(n^{-1/m})^m
=1,
\]

and

\[
A_n^m=n^{-1}Q_n,
\qquad
\operatorname{Tr}(A_n^m)=1.
\]

Equation (13) follows from the critical theorem. Equivalently, it follows directly by cancelling the first `m-1` scalar Taylor terms in

\[
n\log(1+zn^{-1/m}).
\]

For (15),

\[
\|B_n\|_p^p
=
n(n^{-1/p})^p
=1,
\]

while for every integer `k>p`,

\[
\operatorname{Tr}(B_n^k)
=
n^{1-k/p}\to0.
\]

The first admissible regularization begins at `r=\lceil p\rceil>p`, so every term in its trace-log vanishes and (17) follows.

## Exact controls and failure modes

### Bounded `\mathcal S_p` mass is not the same as determinant fidelity

The hypotheses (1) permit

\[
\|A_i\|_p
\not\longrightarrow0.
\]

The examples (11) and (15) keep the `\mathcal S_p` mass exactly equal to one. Thus the collapse of `\det_r` is not caused by disappearance of the underlying Schatten resource. It is caused by the interaction between diffuse mass, operator-scale collapse, and the order at which the regularized trace-log starts observing moments.

### The integer threshold belongs to the chosen determinant category

There is no claim that noninteger `p` is intrinsically less informative. The threshold arises because the standard regularized Fredholm determinant is indexed by an **integer** `r` and is defined by cancelling all trace powers below `r`.

Another observable not restricted to integer polynomial moments could retain information from the same `\mathcal S_p` cloud. Therefore (3) is a no-go for this determinant compression, not a universal no-go for every possible functional of `\mathcal S_p`.

### Positivity identifies the critical coefficient with resource mass

If `p=m\in\mathbb N` and `A_i\ge0`, then

\[
\operatorname{Tr}(A_i^m)
=
\|A_i\|_m^m.
\tag{29}
\]

Hence the coefficient surviving in (8) is exactly the limiting `m`-Schatten resource mass whenever that norm power converges.

For self-adjoint operators the same identity holds automatically when `m` is even. When `m` is odd, positive and negative eigenvalues can cancel in `\operatorname{Tr}(A_i^m)` while the Schatten mass remains nonzero. For general normal operators, complex phases can likewise cancel. Thus critical-order determinant fidelity may still lose total variation unless the operator category independently controls sign or phase.

### The zero divisor always loses the critical residue

Every limiting function in (8) is of the form

\[
e^{c z^m},
\]

which is entire and zero-free. Therefore the divisor compression

\[
\det_m(I+zA_i)
\longrightarrow
\{\text{zeros with multiplicity}\}
\]

cannot retain the critical coefficient `c` in the limit. As in AF-017 and AF-110, a zero-free analytic factor is a genuine possible carrier of provenance and cannot be dismissed merely because it does not alter zeros.

### Higher regularization is a quotient with explicit information semantics

The relation between `\det_m` and `\det_{m+1}` removes the `m`-th trace term by construction. In the critical regime that is exactly the only term whose aggregate size is not forced to zero.

Therefore choosing a higher regularization order than necessary can erase a surviving structural channel even when it improves analytic convenience. Any RH-oriented use of a regularized determinant must justify not only that the regularization exists, but that the moments it subtracts are independently known to be irrelevant to the intended arithmetic discriminator.

### Operator-scale collapse is essential

A bounded `\mathcal S_p` family without `\|A_i\|\to0` can retain arbitrarily rich `\det_r` behavior. The theorem is specifically about **infinitesimal clouds**: every individual singular scale vanishes while aggregate `p`-mass may remain.

This condition is the analogue of a Lindeberg-style small-atom regime for the determinant expansion. Removing it changes the information geometry and invalidates the threshold conclusion.

## Prior art and novelty assessment

The determinant definitions, Schatten ideal inclusions, Hölder estimates, and trace-log expansions are classical. **No theorem-level novelty is claimed.**

- Barry Simon, ***Trace Ideals and Their Applications***, 2nd ed., Mathematical Surveys and Monographs 120, American Mathematical Society (2005), DOI `10.1090/surv/120`. Role: standard source for Schatten ideals, ordinary and regularized Fredholm determinants, trace-ideal estimates, and determinant expansions.
- Thomas Britz, Alan Carey, Fritz Gesztesy, Roger Nichols, Fedor Sukochev, and Dmitriy Zanin, **“The product formula for regularized Fredholm determinants,”** *Proceedings of the American Mathematical Society, Series B* 8 (2021), 42–51, DOI `10.1090/bproc/70`; arXiv:`2007.12834`. Role: modern source explicitly placing the higher regularized determinant `\det_k(I-A)` on the Schatten class `\mathcal S_k` and recording the standard higher-order regularization framework.
- Nikolaos Koutsonikos-Kouloumpis and Matthias Lesch, **“The product formula for regularized Fredholm determinants: two new proofs,”** arXiv:`2202.12923` (2022). Role: direct modern statement that for an `m`-summable operator the higher regularized determinant `\det_m(I+A)` is the natural holomorphic determinant and a generalization of the ordinary Fredholm determinant.
- Luiz Hartmann and Matthias Lesch, **“Zeta and Fredholm determinants of self-adjoint operators,”** *Journal of Functional Analysis* 283 (2022), 109491, DOI `10.1016/j.jfa.2022.109491`; arXiv:`2106.02444`. Role: explicit relation between a `p`-regularized Fredholm determinant and a zeta determinant through a separate exponential polynomial of the lower-order coefficients; useful prior-art confirmation that the low-order polynomial/exponential terms removed by regularization are mathematically distinct data rather than automatically disposable normalization.

The threshold statements above are elementary consequences of this classical machinery. The durable Arithmetic Fidelity content is the information-loss classification: **an infinitesimal bounded `\mathcal S_p` cloud leaves a regularized-determinant residue only at the exact integer critical order `r=p`; every strictly supercritical integer regularization collapses to one, and one extra regularization deletes the critical residue.**

## Consequences for Arithmetic Fidelity

AF-108 through AF-111 now give a four-level hierarchy for operator-to-determinant compression.

A uniform Schatten budget can preserve the operator ideal while weak assembly loses observables. Exact Schatten-norm conservation upgrades weak assembly to full ideal-norm fidelity. If the individual operator scale collapses, an ordinary or regularized determinant retains only trace moments at or above its declared regularization order. AF-111 identifies the sharp boundary inside that final step: only an integer critical moment can survive a bounded diffuse `\mathcal S_p` cloud, and any strictly higher regularization erases it.

This supplies a reusable audit for determinant-based RH proposals. The relevant questions are not only whether the approximants are trace/Schatten class and whether a determinant converges. One must identify the actual summability exponent, the smallest integer regularization used, whether the construction sits at an integer critical threshold, whether sign or phase lets the critical moment cancel, and whether a later divisor or higher regularization removes the residual zero-free factor.

The theorem also sharpens the line's composition principle. In this regime the information flow is

\[
\text{diffuse }\mathcal S_p\text{ mass}
\longrightarrow
\text{integer regularized determinant}
\longrightarrow
\text{zero-free critical exponential or }1
\longrightarrow
\text{zero divisor}.
\]

When `p` is noninteger, the first determinant arrow already sends the diffuse cloud to `1`. When `p=m` is integral, `\det_m` can retain one `m`-th-moment coefficient, but `\det_{m+1}` or the zero divisor erases it. No downstream operation on that final compressed object can reconstruct the lost resource without importing additional structure.
