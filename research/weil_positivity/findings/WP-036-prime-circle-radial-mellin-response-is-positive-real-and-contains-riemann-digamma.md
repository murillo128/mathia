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

where, on the finite index set `S`,

\[
\boxed{
(b_r)_m=m\,\mathbf 1_{m\mid r}.
}
\tag{3}
\]

Every coefficient in (2) is rank-one positive semidefinite. This is stronger than positivity of `G^{full}(x)` at each radius: the entire radial power series lies coefficientwise in the PSD cone.

The decomposition is just the common-Fourier-mode calculation behind `PC-056`, reorganized by the actual harmonic mode `r`. No zeta zeros, continuation, or spectral fitting enter.

## 2. Mellin transform gives an operator-valued positive-real family

For

\[
s=\sigma+it,
\qquad \sigma>0,
\]

define the finite-dimensional Mellin response

\[
\mathcal M_S(s)
:=\int_0^1 x^{s-1}G^{\rm full}_S(x)\,dx.
\tag{4}
\]

Termwise integration of (2) is absolutely convergent and gives

\[
\boxed{
\mathcal M_S(s)
=\sum_{r\ge1}
\frac{b_rb_r^{\!*}}{r(r+s)}.
}
\tag{5}
\]

Taking Hermitian real parts,

\[
\boxed{
\operatorname{Re}\mathcal M_S(\sigma+it)
=\sum_{r\ge1}
\frac{r+\sigma}
{r\bigl((r+\sigma)^2+t^2\bigr)}
\,b_rb_r^{\!*}
\succeq0.
}
\tag{6}
\]

There is a second positivity which will be more relevant for the Gamma factor:

\[
\boxed{
\operatorname{Re}\bigl[s\mathcal M_S(s)\bigr]
=\sum_{r\ge1}
\frac{\sigma(r+\sigma)+t^2}
{r\bigl((r+\sigma)^2+t^2\bigr)}
\,b_rb_r^{\!*}
\succeq0.
}
\tag{7}
\]

Thus the Prime-Circle radial Dirichlet family has a canonical operator-valued positive-real response throughout the half-plane `Re s>0`, including the Riemann critical vertical line `s=1/2+it`. This positivity follows directly from the harmonic Gram decomposition and is independent of RH.

Calling (5) a Stieltjes/positive-real family is standard operator theory; the Mathia-specific content is the exact coefficient vectors (3) forced by the Prime-Circle common-mode geometry.

## 3. The full-root diagonal gives a whole digamma family

On the diagonal `m=n=q`, equation (1) reads

\[
G^{\rm full}_{q,q}(x)=qF_x(q).
\]

Hence

\[
\begin{aligned}
\mathcal M_{q,q}(s)
&=q\int_0^1 x^{s-1}[-\log(1-x^q)]\,dx\\
&=q\sum_{k\ge1}\frac1{k(s+qk)}.
\end{aligned}
\tag{8}
\]

Using the classical digamma series

\[
\psi(1+z)+\gamma
=\sum_{k\ge1}\frac{z}{k(k+z)},
\]

or simply comparing the two absolutely convergent series, one gets the exact identity

\[
\boxed{
\mathcal M_{q,q}(s)
=\frac{q}{s}
\left[
\psi\!\left(1+\frac{s}{q}\right)+\gamma
\right].
}
\tag{9}
\]

Equivalently, by the recurrence `psi(1+z)=psi(z)+1/z`,

\[
\boxed{
\psi\!\left(\frac{s}{q}\right)
=\frac{s}{q}\mathcal M_{q,q}(s)-\gamma-\frac{q}{s}.
}
\tag{10}
\]

So the appearance of a Gamma-type function is not a post-hoc zeta insertion: it is already present in the Mellin response of the exact two-dimensional Dirichlet Gram family.

## 4. The `q=2` channel contains the exact Riemann archimedean scale

For the Riemann completed zeta function, the archimedean logarithmic derivative is

\[
A_\infty(s)
:=\frac{d}{ds}
\log\!\left(\pi^{-s/2}\Gamma(s/2)\right)
=-\frac12\log\pi+\frac12\psi(s/2).
\tag{11}
\]

Setting `q=2` in (10) gives

\[
\boxed{
A_\infty(s)
=
\frac{s}{4}\mathcal M_{2,2}(s)
-\frac\gamma2
-\frac1s
-\frac12\log\pi.
}
\tag{12}
\]

This is an exact scale match: the full-root two-level Prime-Circle radial field produces the `Gamma(s/2)` digamma, including the `1/s` recurrence term, by an intrinsic Mellin transform.

There is an important adversarial control. Equation (10) holds for **every** integer `q>=1`, producing `psi(s/q)`. Therefore the Mellin mechanism itself does not single out `q=2` as an infinite place. The fact that `q=2` matches the Riemann Gamma factor is exact and potentially useful, but it is not yet an independent geometric explanation of why the real place should be the two-level channel. Any future use of (12) must supply that selector intrinsically rather than choose `q=2` because the target is known.

## 5. Primitive-shell normalization preserves the positive-real representation

Now pass to the Möbius primitive-shell coordinates used by `PC-056`, `PC-057`, and `WP-034`. On a finite divisor-closed set, let

\[
T=D_\varphi^{-1/2}M,
\qquad
\widehat G_x=T G^{\rm full}_xT^{\!*}.
\tag{13}
\]

Applying `T` to each coefficient vector in (2),

\[
\widehat G_x
=\sum_{r\ge1}\frac{x^r}{r}\,u_ru_r^{\!*},
\qquad
u_r:=Tb_r.
\tag{14}
\]

For shell `n`,

\[
\begin{aligned}
(u_r)_n
&=\frac1{\sqrt{\varphi(n)}}
\sum_{d\mid n}\mu(n/d)d\,\mathbf1_{d\mid r}\\
&=\boxed{
\frac{c_n(r)}{\sqrt{\varphi(n)}}
},
\end{aligned}
\tag{15}
\]

where `c_n(r)` is the classical Ramanujan sum in its divisor formula. Thus the exact primitive radial geometry has the positive feature map

\[
\boxed{
r\longmapsto
\left(
\frac{c_n(r)}{\sqrt{\varphi(n)}}
\right)_n.
}
\tag{16}
\]

Its Mellin response is correspondingly

\[
\boxed{
\widehat{\mathcal M}(s)
=\sum_{r\ge1}
\frac{u_ru_r^{\!*}}{r(r+s)},
}
\tag{17}
\]

and satisfies the same positive-real identities (6)--(7). This is a useful exact synthesis with `PC-058`/`PC-059`: the divisor-Haar geometry can be represented either by its finite common eigenbasis or by the positive Ramanujan feature measure over physical Fourier modes `r`.

## 6. The Weil-signed boundary operator is the high-Mellin finite part

The decisive connection to `WP-034` is obtained by taking the Mellin parameter large, not by analytic continuation. `PC-057` gives on every fixed finite divisor box

\[
\boxed{
\widehat G_x
=\Lambda_x I+C+o(1),
\qquad
\Lambda_x=-\log(1-x),
\qquad x\to1^-.
}
\tag{18}
\]

For real `a>0`, the probability density `a x^{a-1}dx` concentrates at `x=1`. The universal collision term has the exact Mellin average

\[
\boxed{
a\int_0^1x^{a-1}\Lambda_x\,dx
=\psi(a+1)+\gamma.
}
\tag{19}
\]

Applying the approximate-identity limit to the bounded remainder in (18) gives

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

This identifies the `WP-034` boundary birth operator as a **renormalized high-Mellin finite part of the same positive family**.

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

Thus one intrinsic Prime-Circle Gram family really does reach both sides that had previously appeared disconnected:

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

## 7. Why this still does not give global Weil positivity

The bridge passes an algebraic matching test but fails the current sign theorem test.

First, the positivity theorem belongs to the **unrenormalized** response. For every real `a>0`,

\[
a\widehat{\mathcal M}(a)\succeq0.
\]

But extracting the arithmetic finite part requires the scalar subtraction in (20). `WP-034` proves that the resulting operator `C` is not merely indefinite: along a prime-power cutoff `1,p,...,p^A`, its lowest eigenvalue is exactly

\[
-A\log p,
\]

and on a divisor box `D(N)` its lowest eigenvalue is `-log N`. The positive collision background is precisely what had kept the full Dirichlet Gram positive.

Second, the exact Gamma identity (12) is also an affine **finite-part extraction** from a positive-real quantity. The theorem (7) says

\[
\operatorname{Re}[s\mathcal M(s)]\succeq0,
\]

but `A_infty(s)` is obtained only after subtracting `gamma/2`, `1/s`, and `(1/2)log pi`. Therefore the sign of the positive-real Mellin response does not transfer termwise to the standard Gamma contribution.

Third, the two extractions use the Mellin parameter in different roles. Equation (12) treats `s` as the complex spectral variable on `Re s>0`. Equation (20) obtains the arithmetic finite part from a **real high-Mellin limit** `a->+infinity`. Nothing derived here identifies those two operations as one canonical global quadratic form on Weil test functions.

So the present result does not evade `WP-005`, `WP-028`, or `WP-034`. In particular, a scalar/finite-dimensional Gamma readout cannot repair the infinite negative index of the finite-prime translation comb. A successful use of this bridge would have to lift the positive-real radial response to an infinite-dimensional archimedean operator/compression that couples to the finite birth sector *before* the subtraction producing `C`.

## 8. Adversarial controls

### 8.1 Replace `2` by an arbitrary level `q`

Equation (10) produces `psi(s/q)` for every `q`. Therefore `q=2` cannot be advertised as an intrinsic real-place theorem without an additional geometric characterization unique to the two-level channel.

### 8.2 Keep only the positive-real Mellin response

Then positivity is unconditional, but the object is a Stieltjes transform of the ordinary harmonic-mode measure in (5). Its analytic singularities occur at negative integers `s=-r`, and it contains no prime-log translation support by itself. This is Gamma/harmonic-mode structure, not the finite Weil comb.

### 8.3 Subtract the collision background to expose prime arithmetic

This recovers `C` exactly by (20), but `WP-034` already proves that `C` is unbounded below under cofinal prime-power refinement. The subtraction is therefore not a harmless normalization preserving the geometric sign.

### 8.4 Use the primitive Ramanujan feature representation as the positivity theorem

Equation (17) is genuinely positive-real, but it is still a positive transform of rank-one harmonic features. The exact Weil weights appear only in the boundary finite part, not as nonnegative weights of the Stieltjes measure. This is the same sign boundary in a different basis.

### 8.5 Declare the digamma identity itself to be the solution

The identity is classical special-function algebra. Moreover, `WP-013` already records the Gamma/digamma component of the completed zeta logarithmic derivative, and Connes–Consani provide genuine prior art for archimedean Weil positivity through operator compression. The novelty here is only the Mathia-specific derivation of that digamma scale from the exact Prime-Circle radial Gram and its simultaneous connection to `C`; it is not a new Gamma-function formula or an RH criterion.

## 9. Prior-art and novelty boundary

The classical ingredients are deliberately separated from the project-specific content.

- The digamma series, recurrence, and integral representations are standard Gamma-function identities; they can be checked directly from the convergent series used in (8)--(10).
- Matrix/operator-valued Stieltjes and Herglotz/Nevanlinna positive-real representations are classical. Equations (6)--(7) are proved directly here, so no novelty is claimed for the abstract theory.
- Ramanujan sums and the divisor identity in (15) are classical.
- `SOURCES.md` already records the relevant Weil target and the Connes–Consani archimedean compression mechanism. `WP-013` records the canonical Gamma term in the completed logarithmic derivative and warns that direct positive Hankel completion fails.

The durable Mathia-specific statement is instead the exact three-way identification

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

No previous `WP` finding established that one intrinsic Mathia family contains both the exact Riemann archimedean scale and the exact critical finite-ray coefficient bridge.

## 10. Consequence for the search

The search frontier changes in a useful way. It is no longer accurate to say that Prime Circle lacks any intrinsic archimedean structure related to the finite Weil bridge. The radial Dirichlet Gram already contains a canonical positive-real Mellin response whose two-level channel has the exact `Gamma(s/2)` scale.

What remains missing is more specific and harder:

\[
\boxed{
\text{derive one global compression/quotient/coupling in which}
\quad
\text{the finite-part subtraction and the archimedean response occur together,}
\quad
\text{while positivity survives as an independent theorem.}
}
\]

The next falsifiable target is therefore not another zeta or determinant. It is an **infinite-dimensional coupled finite–archimedean response built before renormalization**, with `G_x`/`mathcal M(s)` as the common parent object. Such a construction must explain intrinsically why the `q=2` channel is the real place, reproduce the endpoint correction omitted by the interior-ray identity (21), and survive the infinite-negative-index obstruction of `WP-028` without importing zero data or a known RH-equivalent Weil functional.