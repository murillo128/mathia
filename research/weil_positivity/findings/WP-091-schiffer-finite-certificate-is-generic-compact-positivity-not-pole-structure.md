# WP-091 — The finite Schiffer certificate is generic compact positivity, not a shadow of the pole expansion

**Status:** `EXACT-DERIVED + CLUE-RESOLUTION + PRIOR-ART-CLASSICALIZATION + MATCHED-CONTROL`.

The clue `CLUE-finite-local-certificates-schiffer-obstruction` asks whether the global Mittag--Leffler proof of the `WP-014` Schiffer obstruction and the finite fifth-order sine certificate exposed by its Lean formalization are manifestations of a deeper equivalence. There is a precise answer, but it is mostly a classicalization rather than a new Mathia mechanism.

For the concrete Schiffer inequality, the finite proof can be reconstructed exactly without using any pole data. More generally, once a real analytic inequality has only finite-order zeros and is strictly positive after those zeros are factored, compact polynomial approximation plus the classical Lukács theorem gives a finite polynomial positivity certificate in principle. Validated Taylor-model methods are the constructive numerical version of the same principle. Conversely, a positive pole/tail representation does not impose any uniform bound on the local jet order needed to see strict positivity.

Thus the coexistence of the two `WP-014` proofs is not evidence that the global meromorphic pole structure has collapsed into a new finite geometric invariant. It is an instance of a broad one-dimensional fact: **strict compact positivity with finite-order contact is finitely certifiable after the contact is factored**. The unusually low fifth order in the Schiffer case is a useful proof simplification, but not a new Weil-positive structure.

## 1. The `WP-014` inequality has an exact pole-free fifth-order certificate

Write

\[
g(t)=\csc^2 t-\frac1{t^2}-\frac13,
\qquad 0<|t|<\frac\pi2.
\tag{1}
\]

`WP-014` proves `g(t)>0` by the global Mittag--Leffler expansion of `csc^2`. To remove the poles and denominators from the sign question, multiply by the positive factor `t^2 sin^2 t` and put

\[
Q(t)
:=t^2-\sin^2 t-\frac13t^2\sin^2 t.
\tag{2}
\]

Then

\[
\boxed{
g(t)>0\iff Q(t)>0}
\qquad(0<|t|<\pi/2).
\tag{3}
\]

By evenness it is enough to take `0<t<pi/2<2`. The alternating Taylor bound gives

\[
0<\sin t
<t-\frac{t^3}{6}+\frac{t^5}{120}.
\tag{4}
\]

Set

\[
u=t^2,
\qquad
S(u)=1-\frac u6+\frac{u^2}{120}.
\tag{5}
\]

Since `0<u<4`, direct rational algebra gives

\[
\begin{aligned}
3-(3+u)S(u)^2
&=\frac{u^2}{14400}
\left(2880-520u+37u^2-u^3\right)\\
&>\frac{736}{14400}u^2
>0.
\end{aligned}
\tag{6}
\]

The crude lower bound in the second line is already enough: for `0<u<4`,

\[
2880-520u+37u^2-u^3
>2880-520\cdot4-4^3
=736.
\tag{7}
\]

Equations (4)--(6) imply

\[
\sin^2 t
<t^2S(u)^2
<\frac{3t^2}{3+t^2},
\tag{8}
\]

which is exactly equivalent to

\[
\frac1{\sin^2 t}>\frac1{t^2}+\frac13.
\tag{9}
\]

So the decisive `2 x 2` Schiffer determinant obstruction of `WP-014` has a completely finite proof using only a fifth-order Taylor upper bound and one polynomial inequality. The Mittag--Leffler poles are not logically needed for this sign.

This reconstruction is important because it isolates exactly what the formalization discovered: a short certificate for the scalar inequality, not a second geometric source of the sign.

## 2. Why finite certificates are generic after finite-order contact is removed

The relevant general statement is elementary.

> **Finite compact-certificate principle.** Let `I=[-a,a]`, and suppose a real-valued function `G` on `I` factors as
> \[
> G(t)=t^{2m}H(t),
> \tag{10}
> \]
> where `m>=0`, `H` is continuous on `I`, and
> \[
> H(t)>0\qquad(t\in I).
> \tag{11}
> \]
> Then the strict sign of `G` away from its prescribed zero at `0` admits a finite polynomial surrogate certificate: there is a polynomial `P` and `eta>0` such that
> \[
> H(t)\ge P(t)-\eta>0
> \qquad(t\in I),
> \tag{12}
> \]
> and the polynomial positivity in (12) has a finite one-variable sum-of-squares certificate on `I`.

Indeed, compactness gives

\[
m_H:=\min_I H>0.
\tag{13}
\]

By the Weierstrass approximation theorem choose a polynomial `P` with

\[
\|H-P\|_\infty<\frac{m_H}{4}.
\tag{14}
\]

Then

\[
P(t)-\frac{m_H}{2}>\frac{m_H}{4}>0,
\tag{15}
\]

and

\[
H(t)>P(t)-\frac{m_H}{4}>0.
\tag{16}
\]

The classical Lukács theorem says that a univariate polynomial nonnegative on a compact interval has an exact representation by polynomial squares with the interval factors `(t+a)` and `(a-t)` (equivalently, after affine rescaling, by the standard `[-1,1]` formulas). Thus the polynomial part of the certificate is finite and exact.

This is an **existence** statement, not an algorithmic claim that the degree is known in advance. To make (14) constructive one needs a rigorous approximation-error bound. That is standard validated numerics: Taylor-model methods represent a function by a finite Taylor polynomial plus a rigorous interval enclosure of the remainder. Berz--Makino's classical Taylor-model framework is precisely of this form. Positive polynomial approximation based on the Lukács representation is likewise established approximation theory.

Therefore a finite polynomial proof of a strict one-dimensional analytic inequality on a compact interval is not, by itself, evidence for the global analytic representation that happened to furnish another proof.

## 3. The Schiffer function satisfies the finite-contact hypothesis exactly

The denominator-cleared function (2) has a sixth-order zero at the origin. Expanding only far enough to identify the removable contact,

\[
\sin^2t
=t^2-\frac{t^4}{3}+\frac{2t^6}{45}+O(t^8),
\tag{17}
\]

so

\[
Q(t)=\frac{t^6}{15}+O(t^8).
\tag{18}
\]

Hence

\[
H(t):=\frac{Q(t)}{t^6}
\tag{19}
\]

extends real analytically through `t=0` with

\[
\boxed{H(0)=\frac1{15}>0.}
\tag{20}
\]

`WP-014` proves `Q(t)>0` for every nonzero `|t|<pi/2`; at the other endpoint,

\[
Q(\pi/2)=\frac{\pi^2}{6}-1>0.
\tag{21}
\]

Thus the factored profile has exactly the compact strict-positivity structure of Section 2. The explicit fifth-order proof of Section 1 is much sharper than the abstract approximation argument, but its **existence is not mysterious** once the finite-order contact is recognized.

The finite formal proof therefore reveals a useful proof normal form:

\[
\boxed{
\text{clear positive denominators}
\to
\text{factor the finite-order zero}
\to
\text{certify a positive compact remainder}.
}
\tag{22}
\]

What it does not reveal is a new global pairing or a hidden pole-to-geometry equivalence.

## 4. Positive pole tails do not give a uniform bounded jet order

The strongest version of the clue would be that positive global pole/tail structure forces some bounded local certificate order. That is false even in a trivial meromorphic family.

For every integer `m>=1`, define on `|t|<1`

\[
G_m(t)
:=t^{2m}\left(\frac1{1-t}+\frac1{1+t}\right)
=\frac{2t^{2m}}{1-t^2}.
\tag{23}
\]

This has the explicit positive-tail expansion

\[
\boxed{
G_m(t)=2\sum_{j=m}^{\infty}t^{2j}>0
\qquad(0<|t|<1),
}
\tag{24}
\]

and a fixed symmetric pole pair at `t=+-1`. Nevertheless,

\[
G_m^{(j)}(0)=0
\qquad(0\le j<2m).
\tag{25}
\]

Thus the positive pole/tail representation places **no uniform bound** on the local Taylor-jet order at which strict positivity first becomes visible. Given any proposed fixed jet order `d`, choose `m>d/2`; the entire `d`-jet is zero even though the global positive-tail proof is immediate.

After clearing the positive denominator, the exact polynomial numerator is simply `2t^{2m}`, whose degree likewise grows without bound. This does not say that each member lacks a finite certificate -- each has the trivial square certificate -- but it rules out the structural claim that the existence of a positive pole tail itself forces one universal bounded certificate order.

## 5. Matched controls remove the pole interpretation

The converse diagnostic also fails. Entire functions with no meromorphic pole structure have the same finite-certificate behavior. For example,

\[
E_m(t)=t^{2m}(1+t^2)
\tag{26}
\]

is entire, positive for every `t!=0`, and after factoring its finite-order zero has the manifestly positive remainder `1+t^2`.

So the two properties separate cleanly:

\[
\begin{array}{ccl}
\text{global positive pole/tail representation}
&\not\Rightarrow&
\text{uniform bounded local certificate order},\\[1mm]
\text{finite local polynomial certificate}
&\not\Rightarrow&
\text{global pole structure}.
\end{array}
\tag{27}
\]

The `csc^2` Schiffer profile happens to possess both, but neither one characterizes the other.

## 6. Prior-art and novelty audit

All general ingredients are classical.

- Weierstrass uniform approximation already implies that a strictly positive continuous function on a compact interval can be approximated closely enough by a polynomial while preserving a strict margin. Positive Bernstein approximation is a standard constructive refinement of the same fact.
- The one-dimensional Lukács theorem gives exact sum-of-squares representations for polynomials nonnegative on an interval. Campos-Pinto, Charles, and Després, *Algorithms For Positive Polynomial Approximation*, SIAM Journal on Numerical Analysis 57 (2019), 148--172, DOI `10.1137/17M1131891`, explicitly uses these Lukács representations for positive polynomial approximation.
- Martin Berz and Kyoko Makino, *Verified Integration of ODEs and Flows Using Differential Algebraic Methods on High-Order Taylor Models*, Reliable Computing 4 (1998), 361--369, DOI `10.1023/A:1024467732637`, is a standard source for the finite Taylor-polynomial plus rigorous remainder-enclosure paradigm.

A targeted search across positive polynomial approximation, Lukács interval certificates, validated Taylor models, and analytic inequality certification found no reason to treat the coexistence of the two `WP-014` proofs as a special Schiffer or Weil phenomenon. No novelty is claimed for the approximation/certificate principle.

The Mathia-specific durable content is narrower: the exact `WP-014` scalar obstruction admits the explicit pole-free certificate (4)--(9), and the formalization-generated clue therefore classicalizes rather than opening a new global positivity mechanism.

## 7. Scope boundary

This result does **not** say that alternative formal proofs are mathematically uninteresting. A low-order certificate can expose a better normalization, a hidden finite-order contact, or a route amenable to automation. Nor does the compact argument produce a useful degree bound without quantitative information on the positive margin and approximation error.

It also does not rule out a genuinely structural theorem connecting a special-function pole measure to a particular finite certificate family with quantitative degree/control estimates. Such a theorem would need data absent from the generic principle above -- for example, a canonical relation between pole locations/residues and the certificate coefficients, or a uniform degree bound derived from that global data. The current `WP-014` fifth-order certificate alone supplies neither.

Most importantly for the line mandate, none of the finite-certificate machinery creates a Mathia-native positive quadratic form, an archimedean completion, or a finite-prime/Weil local-to-global decomposition. It only reproves a scalar inequality already used to show that the raw Schiffer kernel is **indefinite**.

## Consequence for the Weil-positivity search

The clue is resolved as `classical` rather than promoted as a new mechanism. The correct interpretation is

\[
\boxed{
\text{Mittag--Leffler proof}
\quad\text{and}\quad
\text{finite Taylor/polynomial proof}
\text{ certify the same scalar sign for different classical reasons.}
}
\tag{28}
\]

Their coexistence does not supply the missing geometric positivity sought by this research line. The Prime-Flute frontier therefore remains where `WP-014` placed it: any successful route must introduce a genuinely new singular, dynamical, quotient/cohomological, or boundary-response construction whose positivity is independent, rather than extracting further significance from the existence of a finite proof of the already-negative Schiffer test.