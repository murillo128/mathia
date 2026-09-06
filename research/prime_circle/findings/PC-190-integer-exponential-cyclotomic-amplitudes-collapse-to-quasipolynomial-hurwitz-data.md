# PC-190 — integer-exponential cyclotomic amplitudes collapse to quasipolynomial Hurwitz data

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for fixed integer exponentials/Laurent polynomials of the local cyclotomic log-potential, followed by one Mellin scalarization. This closes a canonical infinite-Taylor-depth loophole left explicitly open by PC-189, but it does not classify arbitrary analytic/non-polynomial functions of the local field, conductor-dependent nonlinearities, or genuinely nonlocal/global couplings.

PC-189 classified every fixed finite polynomial in local cyclotomic jets as a finite root-of-unity-colored Mordell--Tornheim/conical Dirichlet family, while leaving non-polynomial or infinite-degree nonlinearities open. The most intrinsic such repair is not an arbitrary analytic function: exponentiating the actual local potential

\[
F_n(x):=\log\Phi_n(e^{-x})
\]

recovers the cyclotomic amplitude itself. Negative integer exponentials `exp(-mF_n)` have infinitely many Taylor coefficients in `F_n`, so they genuinely lie outside the finite-polynomial theorem. Nevertheless cyclotomic algebra makes the entire family rational, and its Mellin data reduce to finite Hurwitz-zeta combinations with rational shifts.

## 1. Reciprocal integer exponentials are rational with one cyclotomic denominator

Put `z=e^{-x}` and, for an integer `m>=1`, define

\[
A_{n,m}(x):=e^{-mF_n(x)}=\Phi_n(z)^{-m}.
\tag{1}
\]

Since `Phi_n(z)` divides `1-z^n`,

\[
Q_n(z):=\frac{1-z^n}{\Phi_n(z)}\in\mathbb Z[z],
\qquad
\deg Q_n=n-\varphi(n)<n.
\tag{2}
\]

Hence

\[
\boxed{
\Phi_n(z)^{-m}=\frac{Q_n(z)^m}{(1-z^n)^m}.
}
\tag{3}
\]

Write

\[
Q_n(z)^m=\sum_{r=0}^{D}a_rz^r,
\qquad D=m(n-\varphi(n)).
\tag{4}
\]

Using

\[
(1-z^n)^{-m}
=\sum_{q\ge0}\binom{q+m-1}{m-1}z^{nq},
\tag{5}
\]

we obtain an exact coefficient formula. If

\[
\Phi_n(z)^{-m}=\sum_{k\ge0}b_kz^k,
\]

then

\[
\boxed{
b_k=
\sum_{\substack{0\le r\le\min(k,D)\\r\equiv k\pmod n}}
a_r
\binom{(k-r)/n+m-1}{m-1}.
}
\tag{6}
\]

For each residue class modulo `n`, once `k` is larger than `D`, the right side is a fixed polynomial of degree at most `m-1` in `(k-r)/n`. Therefore:

\[
\boxed{
(b_k)_{k\ge0}\text{ is eventually quasipolynomial of degree }\le m-1
\text{ and period dividing }n.
}
\tag{7}
\]

The first reciprocal is even more rigid. For `m=1`, `deg Q_n<n`, so every residue class receives at most one numerator coefficient and

\[
\boxed{
[b_k]\text{ for }\Phi_n(z)^{-1}\text{ is exactly periodic from }k=0,
\text{ with period dividing }n.
}
\tag{8}
\]

Thus the simplest infinite-degree nonlinear escape from PC-189 is already finite-state in the angular/refinement label.

## 2. Mellinization gives only finite rational-shift Hurwitz-zeta data

Normalize away the constant value at infinity:

\[
G_{n,m}(x):=\Phi_n(e^{-x})^{-m}-1
=\sum_{k\ge1}b_ke^{-kx}.
\tag{9}
\]

It decays exponentially as `x->infinity` and is bounded at `0+`, so

\[
\mathcal G_{n,m}(s)
:=\int_0^\infty G_{n,m}(x)x^{s-1}\,dx
\tag{10}
\]

is holomorphic for `Re(s)>0`. In the absolute termwise region `Re(s)>m`,

\[
\boxed{
\mathcal G_{n,m}(s)=\Gamma(s)\sum_{k\ge1}\frac{b_k}{k^s}.
}
\tag{11}
\]

By (7), for every residue `a mod n`, the tail has the form `b_{nq+a}=P_a(q)` with `deg P_a<=m-1`. Expanding each power of `q=((nq+a)-a)/n` gives

\[
\boxed{
\sum_{k\ge1}\frac{b_k}{k^s}
=D_{n,m}(s)
+\sum_{a=1}^{n}\sum_{j=0}^{m-1}
C_{a,j}\,n^{\,j-s}\,
\zeta\!\left(s-j,\frac{a}{n}+q_a\right),
}
\tag{12}
\]

for explicit rational/integer coefficients `C_{a,j}`, finite starting offsets `q_a>=0`, and a finite Dirichlet polynomial `D_{n,m}` accounting for the initial exceptional coefficients. Shifting the Hurwitz argument reduces (12), if desired, to rational shifts in `(0,1]` plus another finite Dirichlet polynomial.

Equation (12) is the decisive classicalization: fixed reciprocal integer exponentials do not generate a new shell-dependent spectral function. They generate finite combinations of ordinary Hurwitz zeta functions with rational colors and finitely many shifted weights. The equivalent binomial-multiplicity packaging lies in the classical Barnes-zeta framework.

Positive integer exponentials are simpler still. For `r>=1`,

\[
e^{rF_n(x)}-1=\Phi_n(e^{-x})^r-1
\tag{13}
\]

is a finite polynomial in `e^{-x}`, so its Mellin transform is `Gamma(s)` times a finite Dirichlet polynomial. Consequently every **fixed Laurent polynomial in `e^{F_n}`** lies, after one Mellin readout, in a finite span of rational-shift Hurwitz/Barnes zeta data and finite Dirichlet polynomials.

## 3. The prime-power selector survives only as endpoint data

The common-vertex value remains exact. For `n>1`,

\[
\Phi_n(1)=
\begin{cases}
p,&n=p^a,\\1,&n\text{ is not a prime power}.
\end{cases}
\tag{14}
\]

Therefore

\[
\boxed{
G_{n,m}(0+)=
\begin{cases}
p^{-m}-1,&n=p^a,\\0,&n\text{ is not a prime power}.
\end{cases}}
\tag{15}
\]

So exponentiation has not manufactured a new interior selector: it merely applies a fixed nonlinear function to the already classical cyclotomic endpoint `Phi_n(1)`.

The matched mixed-prime control `n=6` makes the distinction explicit. Since

\[
\Phi_6(r)=1-r+r^2<1
\qquad(0<r<1),
\]

we have, for every `m>=1`,

\[
\boxed{G_{6,m}(x)>0\qquad(x>0),}
\tag{16}
\]

although `G_{6,m}(0+)=0`. Thus any positive radial weighting of this reciprocal-amplitude interior is nonzero on the mixed-prime shell `6`; the exact prime-power nullspace again lives only at the boundary. This agrees with the positivity obstruction of PC-182/PC-183 rather than escaping it.

## 4. The `n=2` control exposes the classical zeta factor immediately

For `n=2,m=1`, `Phi_2(z)=1+z`, so

\[
G_{2,1}(x)=\frac1{1+e^{-x}}-1=-\frac1{e^x+1}.
\tag{17}
\]

Hence, for `Re(s)>0`,

\[
\boxed{
\mathcal G_{2,1}(s)
=-\Gamma(s)\eta(s)
=-\Gamma(s)(1-2^{1-s})\zeta(s).
}
\tag{18}
\]

Thus the first and cleanest reciprocal exponential does display the nontrivial zeros of zeta, but only through the standard Fermi--Dirac/Dirichlet-eta Mellin integral. This is a matched falsification control against interpreting zeros produced by (12) as a new Prime-Circle spectral mechanism.

## 5. Prior art and novelty audit

No novelty is claimed for the ingredients on the right side of (3), (7), or (12).

1. Pieter Moree, *Inverse cyclotomic polynomials*, *Journal of Number Theory* **129** (2009), 667--680, studies the classical inverse-cyclotomic polynomial `Psi_n(x)=(x^n-1)/Phi_n(x)`. Up to the harmless sign convention, this is exactly the finite numerator `Q_n` used in (2)--(3).
2. Makoto Ishibashi and Shigeru Kanemitsu, *Dirichlet series with periodic coefficients*, *Results in Mathematics* **35** (1999), 70--88, DOI `10.1007/BF03322023`, treats the established periodic-coefficient Dirichlet-series framework. The `m=1` case of (11)--(12) lies directly in that class.
3. S. N. M. Ruijsenaars, *On Barnes' multiple zeta and gamma functions*, *Advances in Mathematics* **156** (2000), 107--132, DOI `10.1006/aima.2000.1946`, is a standard modern reference for the Barnes zeta/gamma framework that packages polynomial/binomial multiplicities such as those in (5).
4. The decomposition of an eventually quasipolynomial Dirichlet series into finitely many rational-shift Hurwitz zeta functions follows elementarily by splitting into residue classes and expanding the residue-class polynomials. No new special-function identity is being claimed here.

The durable contribution is the **Prime-Circle boundary theorem** (3)--(12): one of the most natural infinite-Taylor-depth nonlinearities left open by PC-189 is still forced by cyclotomic algebra into finite classical root-of-unity/Hurwitz data. The appearance of `zeta(s)` in the `n=2` control is explicitly classical rather than evidence for a new RH bridge.

## 6. What this rules out and what remains open

This finding rules out the claim that simply replacing a finite polynomial in `F_n` by a fixed integer exponential `exp(kF_n)`, or by any fixed Laurent polynomial in the cyclotomic amplitude `exp(F_n)=Phi_n(e^{-x})`, escapes the finite classicalization seen in PC-189. Negative powers have infinite Taylor depth in `F_n`, but their coefficient dynamics are only periodic/quasipolynomial because the denominator is `(1-z^n)^m`.

It does **not** classify arbitrary non-integer exponentials, arbitrary analytic functions of `F_n`, nonlinear degree/exponent growing with `n` or refinement depth, genuinely nonlocal two-depth/angular couplings, shell-dependent old/new operators, singular boundary domains, or all-shell/global limits. Those remain possible only if the geometry forces structure beyond a fixed rational cyclotomic amplitude before scalarization.

## 7. Falsification checks

The result can be audited without any RH assumption.

- For `m=1`, direct power-series division of `1/Phi_n(z)` must reproduce an exactly `n`-periodic coefficient sequence as predicted by (8).
- For `m>=2`, each residue subsequence `b_{nq+a}` must agree, after finitely many initial terms, with a polynomial in `q` of degree at most `m-1`; failure would falsify (6)--(7).
- For `n=2,m=2`, `(1+z)^{-2}=sum_{k>=0}(-1)^k(k+1)z^k`, giving a degree-one quasipolynomial of period two, the simplest nontrivial check of (7).
- For `n=6,m=1`, `1/Phi_6(z)` begins `1,1,0,-1,-1,0,...`, giving exact period six and independently checking (8).
- Numerical Mellin quadrature for `n=2,m=1` must agree with `-Gamma(s)eta(s)` in `Re(s)>0`.

## Research consequence

PC-189's phrase “non-polynomial or infinite-degree nonlinearities” was genuinely broader than its theorem. PC-190 now removes a canonical and geometrically forced subfamily from that frontier: **fixed integer exponentials and Laurent cyclotomic amplitudes add infinite Taylor depth but no new arithmetic carrier**. Their bulk Mellin data are finite Hurwitz/Barnes combinations, while the exact prime-power discriminator remains boundary data inherited from `Phi_n(1)`.

The surviving nonlinear frontier therefore has to be more than exponentiation of the same local source: conductor/refinement-dependent infinite depth, a second geometry-forced carrier, genuine nonlocal mixing before scalarization, or an all-shell/global operator construction.