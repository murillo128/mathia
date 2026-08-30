# WP-036 — Prime-Circle radial Mellin response is positive-real and contains the Riemann digamma

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + CANDIDATE-BRIDGE + DECISIVE-BOUNDARY` for the attempt to use the exact radial Prime-Circle Dirichlet Gram family as a single intrinsic source of both the archimedean Gamma response and the finite-prime Weil coefficients. The same geometric family does contain both pieces algebraically: its Mellin response is an operator-valued positive-real/Stieltjes family and the full-root `n=2` diagonal gives the exact `psi(s/2)` scale of the Riemann Gamma factor; after Möbius primitive-shell normalization, the high-Mellin finite part is exactly the boundary birth operator `C` of `PC-057`/`WP-034`, whose interior prime-ray entries are `-Lambda(p^k)/sqrt(p^k)`. However, these two readouts do not yet form one positive Weil pairing. The finite arithmetic term appears only after subtracting the universal positive collision background, and the resulting `C` is unbounded below. The Gamma readout likewise requires affine subtraction from the positive-real `n=2` response. Thus the discovery is a genuine same-geometry finite/archimedean bridge, but the geometric positivity lives before the renormalizations that isolate the Weil pieces.

This finding does **not** rule out a larger compression, quotient, boundary construction, or nonseparable finite–archimedean coupling built from this Mellin family. It does rule out claiming that the bare positive-real Mellin response itself is already the global Weil-positive form.

## 1. Exact positive harmonic decomposition of the full-root Gram

For a finite set of scale indices `S`, retain the full-root Prime-Circle fields from `PC-056`,

\[
V_n(z)=\Log(1-z^n),
\qquad 0<x<1,
\]

with exact Dirichlet Gram matrix

\[
G^{\rm full}_{m,n}(x)
=-\gcd(m,n)\log\!\left(1-x^{\operatorname{lcm}(m,n)}\right).
\tag{1}
\]

Write

\[
F_x(q)=-\log(1-x^q)=\sum_{k\ge1}\frac{x^{qk}}k.
\]

If `r=k lcm(m,n)`, then

\[
\frac{\gcd(m,n)}k
=\frac{\gcd(m,n)\operatorname{lcm}(m,n)}r
=\frac{mn}{r}.
\]

Therefore (1) has the exact coefficientwise decomposition

\[
\boxed{
G^{\rm full}(x)
=\sum_{r\ge1}\frac{x^r}{r}\,b_rb_r^{\!*},
}
\tag{2}
\]

where, on `S`,

\[
\boxed{
(b_r)_m=m\,\mathbf 1_{m\mid r}.
}
\tag{3}
\]

Every coefficient in (2) is rank-one positive semidefinite. This is stronger than positivity of `G^{full}(x)` at each radius: the entire radial power series lies coefficientwise in the PSD cone. It is simply the common-Fourier-mode calculation behind `PC-056`, reorganized by physical harmonic mode `r`; no zeta zeros, continuation, or spectral fitting enter.

## 2. Mellin transform gives an operator-valued positive-real family

For

\[
s=\sigma+it,
\qquad \sigma>0,
\]

define

\[
\mathcal M_S(s)
:=\int_0^1 x^{s-1}G^{\rm full}_S(x)\,dx.
\tag{4}
\]

Termwise integration of (2) is absolutely convergent and gives

\[
\boxed{
\mathcal M_S(s)
=\sum_{r\ge1}\frac{b_rb_r^{\!*}}{r(r+s)}.
}
\tag{5}
\]

Hence

\[
\boxed{
\operatorname{Re}\mathcal M_S(\sigma+it)
=\sum_{r\ge1}
\frac{r+\sigma}{r((r+\sigma)^2+t^2)}
\,b_rb_r^{\!*}
\succeq0,
}
\tag{6}
\]

and, more strongly for the Gamma readout,

\[
\boxed{
\operatorname{Re}[s\mathcal M_S(s)]
=\sum_{r\ge1}
\frac{\sigma(r+\sigma)+t^2}{r((r+\sigma)^2+t^2)}
\,b_rb_r^{\!*}
\succeq0.
}
\tag{7}
\]

Thus the Prime-Circle radial Dirichlet family has a canonical operator-valued positive-real response throughout `Re s>0`, including the Riemann critical vertical line `s=1/2+it`. This positivity is geometric and independent of RH.

Calling (5) a Stieltjes/positive-real family is standard operator theory. The Mathia-specific content is the exact feature system (3) forced by the Prime-Circle common-mode geometry.

## 3. Every full-root diagonal gives a digamma scale

On the diagonal `m=n=q`, equation (1) reads

\[
G^{\rm full}_{q,q}(x)=qF_x(q).
\]

Therefore

\[
\begin{aligned}
\mathcal M_{q,q}(s)
&=q\int_0^1x^{s-1}[-\log(1-x^q)]\,dx\\
&=q\sum_{k\ge1}\frac1{k(s+qk)}.
\end{aligned}
\tag{8}
\]

Using the classical digamma series

\[
\psi(1+z)+\gamma
=\sum_{k\ge1}\frac{z}{k(k+z)},
\]

one obtains exactly

\[
\boxed{
\mathcal M_{q,q}(s)
=\frac{q}{s}
\left[\psi\!\left(1+\frac{s}{q}\right)+\gamma\right].
}
\tag{9}
\]

By `psi(1+z)=psi(z)+1/z`,

\[
\boxed{
\psi\!\left(\frac{s}{q}\right)
=\frac{s}{q}\mathcal M_{q,q}(s)-\gamma-\frac{q}{s}.
}
\tag{10}
\]

So a Gamma-type function is not inserted after the fact: it is already present in the Mellin response of the exact two-dimensional Dirichlet Gram family.

## 4. The `q=2` channel contains the exact Riemann archimedean scale

For the Riemann completed zeta function, the archimedean logarithmic derivative is

\[
A_\infty(s)
:=\frac{d}{ds}\log\!\left(\pi^{-s/2}\Gamma(s/2)\right)
=-\frac12\log\pi+\frac12\psi(s/2).
\tag{11}
\]

Setting `q=2` in (10) gives

\[
\boxed{
A_\infty(s)
=\frac{s}{4}\mathcal M_{2,2}(s)
-\frac\gamma2
-\frac1s
-\frac12\log\pi.
}
\tag{12}
\]

This is an exact scale match: the full-root two-level Prime-Circle radial field produces the `Gamma(s/2)` digamma, including the `1/s` recurrence term, by an intrinsic Mellin transform.

The adversarial control is immediate and important. Equation (10) holds for **every** integer `q>=1`, producing `psi(s/q)`. Therefore the Mellin mechanism itself does not single out `q=2` as the infinite place. The fact that `q=2` matches the Riemann Gamma factor is exact and potentially useful, but it is not yet an independent geometric explanation of why the real place should be the two-level channel. Any future use of (12) must supply that selector intrinsically rather than choose `q=2` because the target is already known.

## 5. Primitive-shell normalization exposes a positive Ramanujan feature system

Pass to the Möbius primitive-shell coordinates used by `PC-056`, `PC-057`, and `WP-034`. On a finite divisor-closed set let

\[
T=D_\varphi^{-1/2}M,
\qquad
\widehat G_x=T G^{\rm full}_xT^{\!*}.
\tag{13}
\]

Applying `T` coefficientwise to (2),

\[
\boxed{
\widehat G_x
=\sum_{r\ge1}\frac{x^r}{r}\,u_ru_r^{\!*},
\qquad
u_r:=Tb_r.
}
\tag{14}
\]

For shell `n`,

\[
\begin{aligned}
(u_r)_n
&=\frac1{\sqrt{\varphi(n)}}
\sum_{d\mid n}\mu(n/d)d\,\mathbf1_{d\mid r}\\
&=\boxed{\frac{c_n(r)}{\sqrt{\varphi(n)}}},
\end{aligned}
\tag{15}
\]

where `c_n(r)` is the classical Ramanujan sum in divisor form. Thus the exact primitive radial geometry has the positive feature map

\[
\boxed{
r\longmapsto
\left(\frac{c_n(r)}{\sqrt{\varphi(n)}}\right)_n.
}
\tag{16}
\]

Its Mellin response is

\[
\boxed{
\widehat{\mathcal M}(s)
=\sum_{r\ge1}\frac{u_ru_r^{\!*}}{r(r+s)},
}
\tag{17}
\]

and obeys the same positive-real identities (6)--(7). This gives an exact bridge between the primitive divisor geometry and positive harmonic features; it is compatible with the divisor-Haar descriptions of `PC-058`/`PC-059` but does not depend on reading zeros into that spectrum.

## 6. The Weil-signed boundary operator is the high-Mellin finite part

`PC-057` gives, on every fixed finite divisor box,

\[
\boxed{
\widehat G_x
=\Lambda_xI+C+o(1),
\qquad
\Lambda_x=-\log(1-x),
\qquad x\to1^-.
}
\tag{18}
\]

For real `a>0`, the density `a x^{a-1}dx` concentrates at `x=1`, while

\[
\boxed{
a\int_0^1x^{a-1}\Lambda_x\,dx
=\psi(a+1)+\gamma.
}
\tag{19}
\]

Applying this approximate identity to the bounded remainder in (18) yields

\[
\boxed{
\lim_{a\to+\infty}
\left[
a\widehat{\mathcal M}(a)
-(\psi(a+1)+\gamma)I
\right]
=C.
}
\tag{20}
\]

So the `WP-034` boundary birth operator is a renormalized high-Mellin finite part of the **same positive family**.

On every interior prime-power ray, `WP-034` proves

\[
\boxed{
C_{dp^k,d}
=-\frac{\log p}{p^{k/2}}
=-\frac{\Lambda(p^k)}{\sqrt{p^k}}
\qquad(p\mid d).
}
\tag{21}
\]

The common parent geometry can therefore be summarized as

```text
exact radial Dirichlet Gram G_x >= 0
    |
    +-- Mellin response at complex s
    |      -> positive-real operator family
    |      -> q=2 diagonal contains psi(s/2)
    |
    +-- primitive-shell normalization + boundary/high-Mellin finite part
           -> C
           -> exact -Lambda(p^k)/sqrt(p^k) interior ray weights
```

This is the strongest same-geometry finite/archimedean bridge found so far in the `weil_positivity` line.

## 7. Why this is still not a global Weil positivity theorem

The bridge passes an algebraic matching test but not the required sign theorem.

First, positivity belongs to the **unrenormalized** response. For every real `a>0`,

\[
a\widehat{\mathcal M}(a)\succeq0.
\]

But extracting the arithmetic finite part requires the scalar subtraction in (20). `WP-034` proves that the resulting `C` is not merely indefinite: along `1,p,...,p^A`, its lowest eigenvalue is exactly `-A log p`, and on a divisor box `D(N)` its lowest eigenvalue is `-log N`. The positive collision background is precisely what kept the full Dirichlet Gram positive.

Second, the exact Gamma identity (12) is itself an affine finite-part extraction from a positive-real quantity. Equation (7) gives

\[
\operatorname{Re}[s\mathcal M(s)]\succeq0,
\]

but `A_infty(s)` appears only after subtracting `gamma/2`, `1/s`, and `(1/2)log pi`. Hence positivity of the Mellin response does not transfer termwise to the standard Gamma contribution.

Third, the two extractions use the Mellin parameter differently. Equation (12) treats `s` as the complex spectral variable on `Re s>0`; equation (20) obtains the arithmetic finite part from a **real high-Mellin limit** `a->+infinity`. Nothing derived here identifies those two operations with one canonical quadratic form on Weil test functions.

Consequently the result does not evade `WP-005`, `WP-028`, or `WP-034`. In particular, a scalar/finite-dimensional Gamma readout cannot repair the infinite negative index of the finite-prime translation comb. A successful use of this bridge must lift the positive-real radial response to an infinite-dimensional archimedean compression or coupling that interacts with the finite birth sector **before** the subtraction producing `C`.

## 8. Adversarial controls and falsification tests

### 8.1 Replace `2` by arbitrary `q`

Equation (10) produces `psi(s/q)` for every level. Therefore `q=2` is a target match, not yet an intrinsically selected real place.

### 8.2 Keep only the positive-real Mellin response

Then positivity is unconditional, but (5) is a Stieltjes transform of ordinary harmonic modes. Its analytic singularities are at negative integers `s=-r`; no prime-log translation comb appears inside the positive measure itself. This is Gamma/harmonic-mode structure, not the finite Weil term.

### 8.3 Subtract the collision background

Equation (20) then recovers `C`, but `WP-034` proves that `C` is unbounded below under cofinal prime-power refinement. The subtraction is not sign-preserving.

### 8.4 Use the Ramanujan feature representation as the positivity theorem

Equation (17) is genuinely positive-real, but the exact Weil coefficients occur only in its boundary finite part, not as nonnegative Stieltjes weights. Changing basis does not remove the sign boundary.

### 8.5 Declare the digamma identity itself to be the solution

The identity is classical special-function algebra. `WP-013` already records the Gamma/digamma component of the completed zeta logarithmic derivative, and `SOURCES.md` records Connes–Consani's genuine archimedean Weil positivity through operator compression. No novelty is claimed for digamma formulas, Stieltjes theory, or Ramanujan sums.

The claim can be falsified directly at finite level by checking four identities independently:

1. expand (1) and verify the coefficient matrix at harmonic `r` is `b_rb_r^*/r`;
2. apply the Möbius/totient congruence and verify `(u_r)_n=c_n(r)/sqrt(phi(n))`;
3. compare the diagonal Mellin series with (9);
4. numerically or symbolically evaluate (20) on a finite divisor box and compare with the `PC-057` finite boundary matrix.

## 9. Prior-art and novelty boundary

The ambient ingredients are classical: the digamma series and recurrence, matrix-valued Stieltjes/Herglotz positivity, and Ramanujan sums. The relevant Weil and archimedean-compression prior art is already anchored in `SOURCES.md`; `WP-013` gives the canonical Gamma term and the failure of direct positive Hankel completion.

The durable Mathia-specific statement is the exact three-way identification

\[
\boxed{
\text{Prime-Circle radial Gram}
\longrightarrow
\begin{cases}
\text{positive-real Mellin response},\\
\text{Riemann-scale digamma in the }q=2\text{ full-root diagonal},\\
\text{critical finite Weil ray weights in the renormalized primitive boundary part}.
\end{cases}
}
\tag{22}
\]

No previous `WP` finding established that one intrinsic Mathia family contains both the exact Riemann archimedean scale and the exact critical finite-ray bridge.

## 10. Consequence for the search

It is no longer accurate to say that Prime Circle lacks an intrinsic archimedean structure connected to its finite Weil bridge. The radial Dirichlet Gram already contains a canonical positive-real Mellin response whose two-level channel has the exact `Gamma(s/2)` scale.

What remains missing is more specific:

\[
\boxed{
\text{derive one global compression/quotient/coupling in which}
\quad
\text{the finite-part subtraction and archimedean response occur together,}
\quad
\text{while positivity survives as an independent theorem.}
}
\]

The next falsifiable target is therefore an **infinite-dimensional coupled finite–archimedean response built before renormalization**, with `G_x`/`mathcal M(s)` as the common parent. It must explain intrinsically why `q=2` is the real place, reproduce the endpoint correction omitted by the interior-ray identity (21), and survive the infinite-negative-index obstruction of `WP-028` without importing zero data or a known RH-equivalent Weil functional.
