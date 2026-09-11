# MC-211 — Lowest-shell two-scale principal energy is RH-equivalent under prefix stability

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `LITERATURE+DERIVED`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-210` leaves one potentially non-circular escape for the principal part of the square-modulus variance route: although pointwise critical control of

\[
R_{qd}(U):=\sum_{\substack{n\le U\\(n,qd)=1}}\mu(n)
\]

is Mertens-complete at fixed-power resolution, an **aggregate** estimate for

\[
P_D(U)
=\sum_{D<d\le2D}
 d\mu^2(d)\frac{|R_{qd}(U)|^2}{\varphi(d^2)^2}
\]

might conceivably be weaker. At the lowest square-defect shell, however, this escape has a sharp stability boundary.

Fix

\[
y=c\log X,\qquad 0<c<\frac12,
\qquad q=\prod_{\ell\le y}\ell,
\]

as in `MC-208`--`MC-210`. For large `X`, every square-free `y`-rough integer `d` with

\[
y<d\le2y
\]

is a prime `p`. Hence the principal energy on the lowest shell is exactly the prime family

\[
P_y(U)
:=\sum_{y<p\le2y}w_p|R_{qp}(U)|^2,
\qquad
w_p:=\frac{p}{\varphi(p^2)^2}
=\frac1{p(p-1)^2}.
\tag{1}
\]

Introduce its one-prime rescaled companion

\[
P_y^{\downarrow}(U)
:=\sum_{y<p\le2y}w_p|R_{qp}(U/p)|^2
\tag{2}
\]

and

\[
\mathcal E_y(U):=P_y(U)+P_y^{\downarrow}(U).
\tag{3}
\]

Then for every `p>y` there is the exact one-prime deletion identity

\[
\boxed{
R_q(U)=R_{qp}(U)-R_{qp}(U/p).
}
\tag{4}
\]

Consequently, if

\[
S_y:=\sum_{y<p\le2y}w_p,
\]

then

\[
\boxed{
S_y|R_q(U)|^2\le2\mathcal E_y(U).
}
\tag{5}
\]

The prime number theorem gives

\[
\boxed{
S_y\asymp\frac1{y^2\log y}.
}
\tag{6}
\]

Since `y=c log X`, the inverse loss `S_y^{-1}` is only polylogarithmic.

This makes a very weak prefix-stable version of aggregate principal control already equivalent to RH. More precisely, for fixed `c in (0,1/2)`, the following condition implies

\[
M(X)=O_\varepsilon(X^{1/2+\varepsilon})
\]

for every `epsilon>0`:

\[
\boxed{
\max_{\substack{e\mid q\\e\le X}}
\mathcal E_y(X/e)
\ll_{c,\varepsilon}X^{1+\varepsilon}.
}
\tag{7}
\]

Conversely RH implies `(7)`. Thus `(7)` is an RH-equivalent **aggregate two-scale principal-energy criterion** up to the usual arbitrary `X^epsilon` loss.

The implication is elementary but consequential for the live `MC-209`--`MC-210` branch. A theorem that controls the lowest-shell principal energy only at the single terminal prefix `U=T` may still be genuinely weaker than Mertens. But once that aggregate control is stable under the one-prime deletion scale `U -> U/p` and under the `q`-divisor prefix family needed by the exact rough/smooth inverse, the supposed averaging escape closes: no pointwise control in `p` is needed to recover the critical Mertens exponent.

Therefore a successful **separate-principal-mode** proof of the raw square-modulus energy must exploit at least one of the following asymmetries: terminal-prefix specificity, failure of one-prime rescaling stability, or interference with the centered transverse term that is destroyed when the principal mode is estimated separately. Generic uniform-in-prefix mean-square machinery is already too strong at the bottom shell.

No bound of the form `(7)` is proved here, and no new proof of RH or improved estimate for `M(X)` is claimed.

## Derivation

### 1. The bottom square-defect shell is a prime shell

The square-free principal energy from `MC-210` keeps only `d` with `mu^2(d)=1`, `(d,q)=1`, and `d>y`. If `y<d<=2y` were composite, every prime factor of `d` would exceed `y`; for `y>2` this would force

\[
d>y^2>2y,
\]

a contradiction. Thus `d=p` is prime and `y<p<=2y`. Since `y=c log X`, one also has `p^2<X` for large `X`, so the square-modulus cutoff does not remove this shell.

For such a prime,

\[
\varphi(p^2)=p(p-1),
\]

which gives the weight in `(1)`.

### 2. Deleting one new prime gives an exact two-scale decoder

Split the `q`-rough prefix according to divisibility by `p`:

\[
R_q(U)
=R_{qp}(U)
+\sum_{\substack{n\le U\\(n,q)=1\\p\mid n}}\mu(n).
\]

Write `n=pm`. Terms with `p|m` vanish because `mu(pm)=0`; for the remaining terms `mu(pm)=-mu(m)`. Since `p` does not divide `q`, the divisible part is

\[
-\sum_{\substack{m\le U/p\\(m,qp)=1}}\mu(m)
=-R_{qp}(U/p),
\]

proving `(4)`.

Now

\[
|R_q(U)|^2
\le2|R_{qp}(U)|^2+2|R_{qp}(U/p)|^2.
\]

Multiplying by `w_p`, summing over `y<p<=2y`, and using that the left side is independent of `p` proves `(5)`.

For `(6)`, throughout the dyadic prime interval `p asy y`, one has `w_p asy y^{-3}`, while the prime number theorem gives `pi(2y)-pi(y) asy y/log y`. Hence

\[
S_y\asymp y^{-3}\frac{y}{\log y}
=\frac1{y^2\log y}.
\]

### 3. Prefix-stable aggregate control recovers the rough zero mode

Assume `(7)`. For every divisor `e|q`, put `U=X/e`. Equation `(5)` and `(6)` give

\[
|R_q(X/e)|
\ll_{c,\varepsilon}
X^{1/2+\varepsilon/2}\,y\sqrt{\log y}.
\tag{8}
\]

The important point is that `(8)` was obtained from a weighted **average over the new primes `p`**, not from a pointwise estimate for any individual `R_{qp}`.

The exact inverse transform from `MC-210`, specialized to `Q=q`, is

\[
M(X)=\sum_{e\mid q}\mu(e)R_q(X/e).
\tag{9}
\]

There are only

\[
\tau(q)=2^{\pi(y)}=X^{o(1)}
\]

divisors because `y=c log X`. Combining this with `(8)` already yields

\[
M(X)\ll X^{1/2+\varepsilon/2+o(1)}.
\]

A slightly sharper bookkeeping keeps the natural `e^{-1/2}` scale if `(7)` is stated with `U` rather than `X` on the right. It is not needed here: even the deliberately weak common budget `X^{1+epsilon}` across the subpower-size divisor-prefix family recovers the RH exponent. Since `epsilon` is arbitrary, the classical Mertens criterion gives RH.

### 4. RH gives the two-scale aggregate bound back

Assume RH. Then for every fixed `delta>0`,

\[
M(V)\ll_\delta V^{1/2+\delta}.
\tag{10}
\]

The exact forward rough/smooth transform used in `MC-210` gives, for `Q=qp`,

\[
R_Q(V)
=\sum_{\substack{r\le V\\r\in\mathcal S_Q}}M(V/r).
\tag{11}
\]

Using `(10)` in `(11)` and extending the resulting positive majorant over the full semigroup,

\[
|R_Q(V)|
\ll_\delta
V^{1/2+\delta}
\prod_{\ell\mid Q}
\left(1-\ell^{-1/2-\delta}\right)^{-1}.
\tag{12}
\]

Uniformly for `p in (y,2y]`, the logarithm of the Euler product in `(12)` is

\[
O\!\left(\sum_{\ell\le y}\ell^{-1/2-\delta}+y^{-1/2-\delta}\right)
=O(\sqrt y)
=o(\log X),
\]

so the product is `X^{o(1)}`. Therefore

\[
R_{qp}(V)\ll_\delta V^{1/2+\delta}X^{o(1)}
\tag{13}
\]

uniformly in the prime shell. Substituting `(13)` at `V=U` and `V=U/p` into `(3)`, and using `sum_p w_p=S_y<=1`, gives

\[
\mathcal E_y(U)
\ll_\delta U^{1+2\delta}X^{o(1)}.
\]

For `U=X/e` with `e|q`, one has `U<=X`, so choosing `delta` sufficiently small relative to `epsilon` proves `(7)`.

This establishes the asserted RH equivalence.

## Why it matters

`MC-210` deliberately left aggregate control of

\[
P_D=\sum_d d\mu^2(d)\frac{|R_{qd}(T)|^2}{\varphi(d^2)^2}
\]

as a legitimate possible escape from the pointwise principal-mode barrier. `MC-211` shows exactly how narrow that escape is at the first shell. The common rough prefix `R_q(U)` can be decoded from every `qp`-rough prefix by comparing only two scales, `U` and `U/p`; averaging those identities over the entire prime shell preserves the decoder with only the polylogarithmic conditioning factor `S_y^{-1}`.

Thus the obstacle is not merely that each principal character individually contains Mertens information. Even a positive quadratic **average over many principal characters** becomes Mertens-complete as soon as the estimate survives the natural one-prime rescaling and the finite `q`-divisor prefix family. A future BDH/large-sieve style argument must therefore be audited for prefix stability, not only for whether it avoids pointwise character bounds.

This also explains why terminal-only information remains a meaningful loophole. Equation `(4)` needs both `R_{qp}(U)` and the shorter prefix `R_{qp}(U/p)`. A theorem proved only at one terminal `U`, with no compatible information at the rescaled prefix, does not trigger the decoder. Likewise the raw prescribed-residue energy from `MC-209` may still exploit cross terms between principal and centered modes that disappear in the separated positive energy `(3)`.

## Boundary / conditions

- The equivalence is for the **two-scale** aggregate energy `(3)` on the lowest shell, not for `P_y(U)` alone. No lower bound for the one-scale principal energy is asserted.
- The prefix family in `(7)` is exactly what is needed to invert the logarithmic primorial pre-sieve through `(9)`. A single terminal estimate at `U=T` is not claimed to imply RH.
- The common right side `X^{1+epsilon}` in `(7)` is intentionally weak. Replacing it by a natural local scale `U^{1+epsilon}` only strengthens the hypothesis.
- The argument uses the logarithmic sieve level `y=c log X`, fixed `0<c<1/2`, and the resulting subpower divisor complexity. It is not asserted unchanged for substantially larger primorial cutoffs.
- No cancellation between the principal and centered residue pieces is retained in `mathcal E_y`. Therefore this obstruction does not rule out a direct proof of the raw energy `W_D` from `MC-210`.
- No probabilistic independence, zero-free region, contour shift, or assumed pointwise Mertens estimate enters the forward implication `(7) -> RH`.

## Prior-art audit

The one-prime identity `(4)` is an elementary coprimality decomposition, and the rough/smooth transforms `(9)` and `(11)` are the same classical local Euler-factor mechanism already audited in `MC-181` and `MC-210`. No novelty is claimed for those identities or for the classical equivalence between RH and `M(X)=O_epsilon(X^(1/2+epsilon))`.

Adam J. Harper, *Simple Barban--Davenport--Halberstam type asymptotics for general sequences*, Journal of the London Mathematical Society 112 (2025), e70293, DOI `10.1112/jlms.70293`, studies centered arithmetic-progression variance for general complex sequences. Its variance subtracts the average over each gcd class before squaring. As already noted in `MC-210`, such centering removes the principal mode rather than controlling the two-scale quantity `(3)`.

Baier and Zhao's sparse-modulus Barban--Davenport--Halberstam/Bombieri--Vinogradov theory and the square-modulus large-sieve literature audited in `MC-209` show that averaging over square moduli is a classical analytic mechanism. Those results do not supply `(7)`: the new obstruction here is the exact decoder created by the common logarithmic primorial core and the coupled prefixes `U` and `U/p`.

No source located in the existing line audit or the targeted literature check was used as evidence for a published theorem asserting the line-specific equivalence `(7)`. This is not a literature-absence or novelty claim. The durable contribution is the exact frontier refinement: **aggregate principal-mode control is a genuine escape only while it remains unstable under the natural one-prime and primorial-prefix dilations.**