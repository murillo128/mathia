---
id: WP-305
title: Canonical reflected Mangoldt Herglotz has the wrong next-order Gamma curvature
branch: weil_positivity
status: supported
kind: subleading-herglotz-gamma-curvature-obstruction
claim_strength: exact first-subleading real asymptotic for the WP-304 pole-normalized Mangoldt Herglotz response, exact positivity of its curvature coefficient, and an exact opposite-sign comparison with the Riemann digamma/Gamma curvature; rules out source-alone reflection, additive real renormalization, and positive spectral dilation as an exact Gamma completion
created: 2026-09-14
related: [WP-117, WP-273, WP-275, WP-303, WP-304]
prior_art:
  - Tom M. Apostol, Introduction to Analytic Number Theory, Springer, 1976, for classical weighted Mertens/von-Mangoldt estimates
  - NIST Digital Library of Mathematical Functions, Section 25.2, especially Eq. 25.2.4, for the Laurent expansion of zeta in Stieltjes constants
  - NIST Digital Library of Mathematical Functions, Section 5.11, especially Eq. 5.11.2, for the asymptotic expansion of the digamma function
  - Fritz Gesztesy and Eduard Tsekanovskii, On Matrix-Valued Herglotz Functions, Mathematische Nachrichten 218 (2000), 61-138, DOI 10.1002/1522-2616(200010)218:1<61::AID-MANA61>3.0.CO;2-D, for the classical Herglotz/Nevanlinna framework
---

# WP-305 — Canonical reflected Mangoldt Herglotz has the wrong next-order Gamma curvature

## Claim

`WP-304` left open whether the one-sided, pole-normalized positive Mangoldt measure

\[
\mu_+=\sum_{n\ge2}\frac{\Lambda(n)}{n+1}\,\delta_{\log n}
\tag{1}
\]

could acquire the exact Riemann archimedean profile after choosing the reflected orientation that gives the correct sign of the leading logarithm. That route can be falsified at the first nonconstant real correction.

Let

\[
M(R)=\mu_+([0,R])=\sum_{n\le e^R}\frac{\Lambda(n)}{n+1}.
\tag{2}
\]

Then

\[
M(R)=R+C_++\varepsilon(R),\qquad \varepsilon(R)\to0,
\tag{3}
\]

with

\[
C_+=-\gamma-\sum_{n\ge2}\frac{\Lambda(n)}{n(n+1)}.
\tag{4}
\]

The PNT zero-free-region error makes `epsilon` integrable, and its zeroth moment is exactly

\[
\boxed{
A_0:=\int_0^\infty\varepsilon(E)\,dE
=\gamma^2+2\gamma_1+\sum_{n\ge2}\frac{\Lambda(n)\log n}{n(n+1)}>0,
}
\tag{5}
\]

where `gamma_1` is the first Stieltjes constant in the convention

\[
\zeta(1+s)=\frac1s+\gamma-\gamma_1s+O(s^2).
\tag{6}
\]

For the regularized Herglotz response of `WP-304`,

\[
m_+(z)=\int_0^\infty\left(\frac1{E-z}-\frac{E}{1+E^2}\right)d\mu_+(E),
\qquad \operatorname{Im}z>0,
\tag{7}
\]

one has along `z=iy`

\[
m_+(iy)=-\log y+B-\frac{A_0}{y^2}+o(y^{-2})
+i\left(\frac\pi2+\frac{C_+}{y}+o(y^{-1})\right).
\tag{8}
\]

Reflecting the same positive measure to the negative half-line gives

\[
m_-(iy)=-\overline{m_+(iy)},
\tag{9}
\]

hence

\[
\operatorname{Re}m_-(iy)=\log y-B+\frac{A_0}{y^2}+o(y^{-2}).
\tag{10}
\]

This reflection repairs the sign of the leading logarithm, but fixes the next real coefficient to be positive. By contrast, the Riemann archimedean digamma term satisfies

\[
\operatorname{Re}\psi\!\left(\frac14+\frac{iy}{2}\right)
=\log\frac y2-\frac1{24y^2}+O(y^{-4}).
\tag{11}
\]

Thus the canonical reflected `WP-304` source and the actual Riemann Gamma sector have opposite first subleading real curvature:

\[
\boxed{+\frac{A_0}{y^2}\quad\text{versus}\quad-\frac1{24y^2},\qquad A_0>0.}
\tag{12}
\]

Consequently, the exact `WP-304` source cannot become the Riemann Gamma term by reflection/orientation plus additive real renormalization, nor after a positive spectral dilation. A surviving completion must introduce additional Mathia-forced structure before the exact Gamma comparison.

## 1. Exact offset of the source counting law

Use

\[
\frac1{n+1}=\frac1n-\frac1{n(n+1)}.
\tag{13}
\]

The classical weighted Mertens estimate gives

\[
\sum_{n\le x}\frac{\Lambda(n)}n=\log x-\gamma+o(1).
\tag{14}
\]

The correction

\[
D:=\sum_{n\ge2}\frac{\Lambda(n)}{n(n+1)}
\tag{15}
\]

converges absolutely and is positive. Therefore, with `x=e^R`,

\[
M(R)=R-\gamma-D+\varepsilon(R),
\tag{16}
\]

proving (4). A standard zero-free-region form of the prime number theorem gives an error decaying faster than any negative power of `R` after `x=e^R`; the tail of (15) is exponentially small up to a polynomial factor. Hence

\[
\int_0^\infty|\varepsilon(E)|\,dE<\infty,
\tag{17}
\]

and the moments needed below are finite.

## 2. The first Stieltjes correction is forced and positive

Take the Laplace transform

\[
F(s):=\int_0^\infty e^{-sE}\,d\mu_+(E)
=\sum_{n\ge2}\frac{\Lambda(n)}{n+1}n^{-s},\qquad s>0.
\tag{18}
\]

By (13),

\[
F(s)=-\frac{\zeta'(1+s)}{\zeta(1+s)}-D(s),
\qquad
D(s)=\sum_{n\ge2}\frac{\Lambda(n)n^{-s}}{n(n+1)}.
\tag{19}
\]

The Laurent expansion at the pole is

\[
-\frac{\zeta'(1+s)}{\zeta(1+s)}
=\frac1s-\gamma+(\gamma^2+2\gamma_1)s+O(s^2).
\tag{20}
\]

Since

\[
D'(0)=-\sum_{n\ge2}\frac{\Lambda(n)\log n}{n(n+1)},
\tag{21}
\]

(19) gives

\[
F(s)=\frac1s+C_++\left(\gamma^2+2\gamma_1+\sum_{n\ge2}\frac{\Lambda(n)\log n}{n(n+1)}\right)s+O(s^2).
\tag{22}
\]

On the other hand, Stieltjes integration by parts in (3) gives

\[
F(s)=s\int_0^\infty e^{-sE}M(E)\,dE
=\frac1s+C_++s\int_0^\infty e^{-sE}\varepsilon(E)\,dE.
\tag{23}
\]

Taking `s->0+` and using (17) proves (5). Moreover

\[
\gamma^2+2\gamma_1>0,
\tag{24}
\]

and every term in the series in (5) is nonnegative, with strict positivity, so `A_0>0`. No zero data, RH assumption, or fitted archimedean parameter enters this sign.

## 3. The Herglotz remainder has fixed `y^{-2}` curvature

Let

\[
\nu:=\mu_+-dE,\qquad N(E):=\nu([0,E])=C_++\varepsilon(E).
\tag{25}
\]

Subtracting the unit-density reference in (7) changes the regularized transform by a real normalization constant plus the conditionally convergent Cauchy transform

\[
h(y):=\int_0^\infty\frac{d\nu(E)}{E-iy}.
\tag{26}
\]

Stieltjes integration by parts yields

\[
h(y)=\int_0^\infty\frac{N(E)}{(E-iy)^2}\,dE.
\tag{27}
\]

The constant part is exact:

\[
C_+\int_0^\infty\frac{dE}{(E-iy)^2}=\frac{iC_+}{y}.
\tag{28}
\]

For the integrable remainder,

\[
\frac1{(E-iy)^2}=-\frac1{y^2}+O\!\left(\frac{E}{y^3}\right)
\tag{29}
\]

in the moment sense supplied by (17). Hence the real first correction is `-A_0/y^2`. The unit-density reference is exactly

\[
\int_0^\infty\left(\frac1{E-iy}-\frac{E}{1+E^2}\right)dE
=-\log y+\frac{i\pi}{2},
\tag{30}
\]

so (8) follows after absorbing the real subtraction difference into `B`. Reflection gives (9)-(10).

## 4. The Riemann Gamma curvature has the opposite sign

For the completed zeta factor, the relevant real archimedean variation contains

\[
H_\infty(y)=\operatorname{Re}\psi\!\left(\frac14+\frac{iy}{2}\right)-\psi(1/4),
\tag{31}
\]

up to an additive normalization independent of `y`. The standard digamma expansion is

\[
\psi(z)=\log z-\frac1{2z}-\frac1{12z^2}+O(z^{-4}).
\tag{32}
\]

At `z=1/4+iy/2`, the three contributions to the `y^{-2}` coefficient in the real part are respectively

\[
\frac18,\qquad-\frac12,\qquad\frac13,
\tag{33}
\]

whose sum is `-1/24`. This proves (11). The mismatch is therefore not a constant-normalization issue: it occurs at the first nonconstant even real correction after the logarithm.

## 5. Scope of the obstruction

An additive real renormalization `m(z)->m(z)+b` changes only `B` and cannot change (12). A positive spectral dilation `E->aE`, `a>0`, can rescale the magnitude of the `y^{-2}` term after the leading logarithm is normalized, but cannot change its sign. Thus reflection, additive normalization, and positive dilation cannot turn the exact `WP-304` source into the Riemann Gamma profile.

This does **not** exclude a Mathia-forced completion containing a nontrivial spectral translation, an additional archimedean/boundary sector, a quotient or compression that changes the source remainder, a genuinely nonlocal finite--archimedean coupling, or another nonlinear spectral observable already forced independently by the geometry. Such operations can alter the `y^{-2}` coefficient. They remain admissible only if Mathia derives them before the Gamma target is consulted; choosing one merely because it changes `+A_0` into `-1/24` is target programming.

## 6. Matched control and aggressive falsification

The sign in (5) is **not** a generic theorem for every positive unit-density measure. A synthetic positive measure can have a bounded counting remainder whose integral is negative. Hence the curvature obstruction is not a tautology of Herglotz positivity or asymptotic density one.

It is specific to the canonical arithmetic source already forced by `WP-273`/`WP-275` and inherited by `WP-304`: the exact weight `Lambda(n)/(n+1)` fixes (19), and therefore fixes (5). Altering those weights can evade the coefficient only by changing the Mathia-derived source and independently justifying a new law.

The complex `iC_+/y` term is deliberately not used as the obstruction because its interpretation is more convention-sensitive. The real `y^{-2}` coefficient is the cleaner matched invariant: reflection fixes the leading-log orientation but leaves the first even real curvature with the wrong sign.

Finally, retaining only the leading `log y` scale is not enough. `WP-304` already showed that this growth is unit-density universal. Exact Weil/Gamma matching begins precisely in the subleading structure that distinguishes the Riemann completion from that control.

## 7. Prior-art and novelty audit

All analytic ingredients are classical. Weighted Mertens estimates and the pole expansion of `-zeta'/zeta` are standard analytic-number-theory facts; the Stieltjes/Herglotz expansion is elementary once the counting remainder is integrable; DLMF records both the zeta Laurent expansion in Stieltjes constants and the digamma asymptotic used above.

A bounded literature/search audit over Herglotz/Nevanlinna formulations of the Riemann explicit formula, von-Mangoldt Stieltjes transforms, Gamma factors, and related resolvent language did not identify a source stating this exact comparison for the `WP-304` measure. No novelty is claimed for Herglotz theory, the digamma expansion, or the constants themselves.

The Mathia-specific content is the collision of two independently fixed objects: `WP-273`/`WP-275` force the positive pole-normalized source `Lambda(n)/(n+1)`, while `WP-303`/`WP-304` force examination of a nonlocal positive Herglotz/boundary response and leave reflection as the simplest orientation repair. For that already-fixed source and transform family, (5)-(12) show that the first Riemann-specific real correction has the wrong sign. This is a repository-level falsification of a live Mathia route, not a new classical theorem about zeta.

Relevant standard references:

- NIST DLMF 25.2.E4: https://dlmf.nist.gov/25.2.E4
- NIST DLMF 5.11.E2: https://dlmf.nist.gov/5.11.E2
- Apostol, *Introduction to Analytic Number Theory*, Springer, 1976.
- Gesztesy--Tsekanovskii, *On Matrix-Valued Herglotz Functions*, Math. Nachr. 218 (2000), 61--138.

## 8. Consequence for the research frontier

`WP-304` showed that logarithmic Herglotz growth is available but generic. `WP-305` sharpens that diagnosis: even after choosing the orientation that repairs the leading sign, the **first subleading real curvature already disagrees with the Riemann Gamma factor**.

The next useful test is therefore not another normalization of the same source transform. A viable construction must derive an additional operation that changes the arithmetic remainder before exact Gamma matching, while retaining an independent positivity theorem and surviving nonarithmetic controls. The missing structure must do mathematical work at the finite--archimedean interface; a reflected unit-density Herglotz tail plus constants is not enough.

## Conclusion

The canonical `WP-304` Mangoldt source contains more information than its universal leading logarithm, but that extra information points the wrong way for the Riemann Gamma sector. Its reflected Herglotz response has positive first real curvature `+A_0/y^2`, with `A_0` fixed explicitly and strictly positive, whereas the completed-zeta digamma term has `-1/(24y^2)`.

This rules out the simplest source-only completion by orientation, additive real renormalization, and positive dilation. Any surviving Mathia route must supply an independently forced boundary/coupling operation that changes this subleading structure rather than merely fitting the known Gamma target.
