# WP-037 — Prime-Circle Weil birth form is a singular profinite-Haar tangent

**Status:** `EXACT-DERIVED + CLASSICAL-HARMONIC-ANALYSIS + NEGATIVE/OBSTRUCTION` for the attempt to rescue the positive radial Prime-Circle family of `WP-036` by normalizing its escaped spectral mass to the profinite-Haar probability limit of `PC-061` and then taking an ordinary positive/statistical tangent there. The normalized radial measure does converge weakly to Haar, and its **first scaled Gram-moment variation recovers exactly the renormalized boundary birth operator `C` of `WP-034`**, including the interior Weil coefficients `-Lambda(p^k)/sqrt(p^k)`. However, the underlying first variation is only a cylindrical linear functional on locally constant profinite observables: its Fourier coefficients grow like `log q` with conductor `q`, so it is not a finite signed measure, not an `L^1` or `L^2` Haar density, and in particular not a Fisher/score tangent to the Haar probability geometry. The arithmetic operator therefore lives precisely in the singular first-order departure from the positive Haar limit, not inside the positive probability geometry itself.

This does **not** rule out a distributional/Sobolev completion, growing-conductor boundary theory, or a nonseparable finite--archimedean compression chosen by an intrinsic Prime-Circle construction. It does rule out claiming that the canonical probability normalization plus an ordinary Haar-space tangent supplies the missing global Weil positivity.

## 1. The positive primitive Gram family is an expectation under the PC-061 log-series law

`WP-036` writes the primitive-shell-normalized exact radial Gram matrix as

\[
\widehat G_x
=\sum_{r\ge1}\frac{x^r}{r}\,u(r)u(r)^*,
\qquad 0<x<1,
\tag{1}
\]

with Ramanujan feature coordinates

\[
\boxed{
 u_n(r)=\frac{c_n(r)}{\sqrt{\varphi(n)}}.
}
\tag{2}
\]

`PC-061` identifies the total radial mass

\[
L(x):=-\log(1-x)=\sum_{r\ge1}\frac{x^r}{r}
\tag{3}
\]

and the corresponding probability measure on the embedded positive integers in the profinite completion `\widehat{\mathbb Z}`,

\[
\boxed{
\bar\nu_x
=\frac1{L(x)}\sum_{r\ge1}\frac{x^r}{r}\,\delta_r.
}
\tag{4}
\]

Consequently, on every finite shell set `S`, equation (1) is exactly the second-moment matrix

\[
\boxed{
\frac{\widehat G_{x,S}}{L(x)}
=\int_{\widehat{\mathbb Z}}
 u_S(y)u_S(y)^*\,d\bar\nu_x(y).
}
\tag{5}
\]

No zeta zero, explicit formula, or analytic continuation appears in this identity. It is a direct reorganization of the exact Prime-Circle harmonic energy.

## 2. Profinite Haar makes the normalized Ramanujan features orthonormal

Each `c_n` is periodic modulo `n`, hence extends canonically to a locally constant function on `\widehat{\mathbb Z}`. For positive integers `m,n`, averaging over a common period gives the classical Ramanujan orthogonality relation

\[
\frac1{\operatorname{lcm}(m,n)}
\sum_{r=1}^{\operatorname{lcm}(m,n)}
 c_m(r)c_n(r)
=
\begin{cases}
\varphi(n),&m=n,\\
0,&m\ne n.
\end{cases}
\tag{6}
\]

Since Haar integration of a locally constant function is exactly uniform averaging on any finite quotient through which it factors,

\[
\boxed{
\int_{\widehat{\mathbb Z}}
 u_m(y)u_n(y)\,dm_H(y)
=\delta_{mn},
}
\tag{7}
\]

where `m_H` is normalized profinite Haar measure.

Thus `PC-061`'s weak convergence

\[
\bar\nu_x\Longrightarrow m_H
\qquad(x\to1^-)
\tag{8}
\]

has an exact Gram interpretation:

\[
\frac{\widehat G_{x,S}}{L(x)}\longrightarrow I_S
\tag{9}
\]

for every fixed finite shell set. The universal collision term `L(x)I` in `WP-034` is therefore not merely a scalar divergence: after probability normalization it is precisely the **Haar covariance/Gram vacuum** of the Ramanujan feature system.

## 3. The finite birth operator is the first scaled Gram variation away from Haar

`WP-034` gives on every fixed finite divisor-closed box

\[
\boxed{
\widehat G_x=L(x)I+C+o(1)
\qquad(x\to1^-).
}
\tag{10}
\]

Combine (5), (7), and (10). For every pair of shell indices `m,n`,

\[
\begin{aligned}
&L(x)\left[
\int u_m u_n\,d\bar\nu_x
-
\int u_m u_n\,dm_H
\right]\\
&\qquad=
(\widehat G_x)_{mn}-L(x)\delta_{mn}
\longrightarrow C_{mn}.
\end{aligned}
\tag{11}
\]

Define the scaled signed functionals

\[
\boxed{
\eta_x:=L(x)(\bar\nu_x-m_H).
}
\tag{12}
\]

Then equation (11) becomes

\[
\boxed{
C_{mn}=\lim_{x\to1^-}\eta_x(u_mu_n).
}
\tag{13}
\]

This identifies the entire finite Prime-Circle birth matrix as a first-order moment response of the normalized positive radial law at its Haar boundary.

In particular, the exact arithmetic bridge of `WP-034` is now a statement about that tangent. Whenever `n=dp^k` with `p\mid d`,

\[
\boxed{
\lim_{x\to1^-}\eta_x(u_{dp^k}u_d)
=C_{dp^k,d}
=-\frac{\log p}{p^{k/2}}
=-\frac{\Lambda(p^k)}{\sqrt{p^k}}.
}
\tag{14}
\]

The valuation-zero first-birth anomaly of `WP-034` remains present; the tangent does not turn `C` into a translation-invariant Weil comb.

A minimal audit witness is already visible at `(m,n)=(2,1)`. Since `u_1=1`, `u_2(r)=(-1)^r`, and the Haar mean of `u_2` is zero,

\[
\eta_x(u_2)
=\sum_{r\ge1}\frac{x^r(-1)^r}{r}
=-\log(1+x)
\longrightarrow-\log2,
\tag{15}
\]

exactly matching `C_{2,1}=-\log2`.

## 4. The first measure variation exists on every fixed finite quotient

Let `\mathcal A_{\rm lc}` denote the algebra of complex locally constant functions on `\widehat{\mathbb Z}`. Equivalently, it is the union over `q` of the finite-dimensional spaces of functions factoring through `\mathbb Z/q\mathbb Z`.

For a finite-conductor additive character

\[
\chi_\zeta(r)=\zeta^r,
\qquad \zeta^q=1,
\tag{16}
\]

`PC-061` gives

\[
\int\chi_\zeta\,d\bar\nu_x
=
\frac{-\Log(1-x\zeta)}{L(x)}.
\tag{17}
\]

For the trivial character `\zeta=1`, both probability measures in (12) have mass one, so

\[
\eta_x(1)=0.
\tag{18}
\]

For every nontrivial root of unity, Haar has zero Fourier coefficient and therefore

\[
\boxed{
\eta_x(\chi_\zeta)
=-\Log(1-x\zeta)
\longrightarrow
-\Log(1-\zeta).
}
\tag{19}
\]

Every locally constant function has a finite Fourier expansion on some finite quotient. Hence the limit

\[
\boxed{
\eta(f):=\lim_{x\to1^-}\eta_x(f)
}
\tag{20}
\]

exists for every `f\in\mathcal A_{\rm lc}`, with Fourier data

\[
\widehat\eta(1)=0,
\qquad
\widehat\eta(\chi_\zeta)=-\Log(1-\zeta)
\quad(\zeta\ne1).
\tag{21}
\]

So the first-order object is canonical at the **cylindrical** level: no choice of subsequence or regularization is required on any fixed finite conductor.

## 5. The cylindrical tangent is not a finite measure

The conductor dependence in (21) is decisive. Let

\[
\zeta_q=e^{2\pi i/q},
\qquad q\ge2.
\]

Then

\[
|1-\zeta_q|=2\sin\frac\pi q
\sim\frac{2\pi}{q},
\tag{22}
\]

and therefore

\[
\operatorname{Re}\bigl[-\Log(1-\zeta_q)\bigr]
=-\log|1-\zeta_q|
=\log q-\log(2\pi)+o(1).
\tag{23}
\]

Hence

\[
\boxed{
\sup_{\chi\in\widehat{\widehat{\mathbb Z}}}
|\widehat\eta(\chi)|=\infty.
}
\tag{24}
\]

But the Fourier--Stieltjes coefficients of any finite complex Borel measure `\mu` on a compact group satisfy the elementary bound

\[
|\widehat\mu(\chi)|
\le\|\mu\|_{\rm TV}
\tag{25}
\]

for every character. Equations (24)--(25) prove

\[
\boxed{
\eta\text{ does not extend to a finite signed/complex Borel measure on }\widehat{\mathbb Z}.
}
\tag{26}
\]

Equivalently, although every `\eta_x` is a finite signed measure, its total-variation norm necessarily escapes to infinity along the boundary scaling. The finite-conductor limits do not assemble into a bounded functional on `C(\widehat{\mathbb Z})`.

This is an exact topology obstruction, not a numerical divergence and not a statement about zeta continuation.

## 6. There is no ordinary Haar `L^2` score or Fisher tangent carrying `C`

An ordinary differentiable statistical tangent at Haar would be represented by a score density `h`, at minimum in a suitable `L^1(m_H)` class and in Fisher geometry in `L^2(m_H)`, so that

\[
\eta(f)=\int f h\,dm_H
\tag{27}
\]

on the test algebra.

Equation (26) already excludes `L^1`, because `h\,dm_H` would be a finite signed measure. It excludes `L^2` a fortiori. Directly, Plancherel would require the Fourier coefficients of an `L^2` density to form an `\ell^2` family on the discrete dual, whereas the subsequence (23) is unbounded.

There is an even more elementary geometric warning from `PC-061`: for every `x<1`, `\bar\nu_x` is supported on the embedded countable integers while Haar gives that set measure zero. Thus

\[
\bar\nu_x\perp m_H
\qquad\text{for every }x<1.
\tag{28}
\]

The weakly convergent radial path never enters the Haar measure class before reaching the endpoint. There is no Radon--Nikodym score along the ordinary interior path whose square could inherit Fisher positivity.

Consequently the tempting chain

```text
positive Prime-Circle radial Gram
    -> normalize to probability
    -> profinite Haar boundary
    -> ordinary positive/Fisher tangent at Haar
    -> Weil-signed birth operator C
```

breaks at the tangent step. `C` is carried by a singular first variation, not by an ordinary positive tangent Hilbert space.

## 7. Positivity disappears exactly when the arithmetic first variation is isolated

The result sharpens the sign boundary in `WP-034` and `WP-036`.

For each `x<1`, equation (5) is a genuine positive Gram matrix because it is an expectation of rank-one positive matrices under a probability measure. In the limit, Haar orthogonality gives the positive identity matrix. But subtracting that zeroth-order Haar vacuum and magnifying the first correction yields

\[
C=\eta(uu^*),
\tag{29}
\]

and `WP-034` proves that `C` is unbounded below on the canonical arithmetic exhaustion.

There is no paradox. A first derivative of a curve inside the positive cone need not itself be positive. Here the failure is stronger: the derivative does not even live in the ordinary finite-measure or `L^2` tangent category at the limiting Haar point.

Also note that `\eta(1)=0` while `\eta(u_2)=-\log2\ne0`. Any positive bounded linear functional on a unital `C^*`-algebra with value zero on the identity is identically zero. Thus the nontrivial tangent cannot itself be a positive Haar functional even before invoking the explicit negative spectrum of `C`.

This gives a precise answer to one natural escape left by `WP-036`: probability normalization does not move the arithmetic finite part into a hidden positive boundary score. It moves the zeroth-order mass to Haar and leaves the arithmetic in a singular, signed next-order term.

## 8. Relation to the archimedean readout

`WP-036` also derives the exact Riemann digamma scale from a diagonal Mellin response of the **same pre-renormalized radial geometry**. The present Haar tangent does not merge that archimedean readout with the finite birth term.

The operations remain different:

```text
radial positive Gram family
    |
    +-- Mellin diagonal q=2
    |      -> psi(s/2) after affine subtraction
    |
    +-- probability normalization x -> 1
           -> Haar vacuum
           -> singular cylindrical first variation eta
           -> C and its interior -Lambda(p^k)/sqrt(p^k) entries.
```

Thus the same-parent observation of `WP-036` survives and becomes more structural, but still not global-positive. A successful finite--archimedean mechanism would have to couple the Mellin and profinite boundary sectors **before** extracting the signed singular tangent, and prove a sign theorem for that coupled object independently of RH.

## 9. Matched controls and adversarial escape tests

### 9.1 Keep only the weak Haar limit

Then all nontrivial finite-conductor Fourier coefficients vanish by `PC-061`, and equation (9) leaves only the identity Gram. The arithmetic birth operator disappears.

### 9.2 Keep the first scaled correction

Then equations (19)--(26) force an unbounded-conductor cylindrical functional, not a finite measure or ordinary Haar `L^2` tangent. The exact arithmetic survives, but ordinary probability/Hilbert positivity does not.

### 9.3 Renormalize `eta` by an additional scalar tending to zero

That can bound the Fourier coefficients only by weakening or killing fixed-conductor values such as (15). It changes the normalization that recovers `C` and therefore cannot retain the exact `WP-034` finite coefficient scale without additional structure.

### 9.4 Restrict to bounded conductor

On every fixed finite quotient, `eta` is a perfectly finite signed functional. This does not solve the global problem: the norm grows with the conductor, so the family has no uniform finite-measure completion. A bounded-conductor theorem is a localization statement, not global Weil positivity.

### 9.5 Choose a weighted Sobolev/distribution topology

This is a genuine escape and is not ruled out. Since the bad coefficient growth is only logarithmic along primitive characters, many weighted Fourier topologies can make `eta` continuous. But the choice of weight/topology must be forced by Mathia's geometry and must carry an independent positivity theorem. Selecting a Sobolev weight merely because it absorbs `log q` would be an external regularization, not an explanation.

### 9.6 Use a growing conductor coupled to `x`

Also open. `PC-061` only controls each fixed conductor before the limit. A canonical joint scaling could retain extra information, but it must be derived from the original two-dimensional geometry rather than hand-picked to preserve desired arithmetic modes.

### 9.7 Treat the cylindrical functional itself as the Weil form

This fails the branch target twice: `eta` is signed/unbounded in the natural sup-norm topology, and its Gram moment `C` is already known from `WP-034` to be unbounded below. Calling the singular first variation a distribution does not create the missing positivity theorem.

## 10. Prior-art and novelty audit

The ambient ingredients are classical and are not claimed as discoveries:

- Ramanujan sums and their mean orthogonality are standard harmonic/arithmetic analysis; Richard Bellman's *Ramanujan sums and the average value of arithmetic functions*, Duke Mathematical Journal 17 (1950), is an early systematic reference, and later Ramanujan-expansion literature treats the normalized sums as an orthogonal system.
- Profinite completion, normalized Haar measure, finite-quotient averaging, and the relation between arithmetic density and Haar measure are classical. A close modern reference is Luca Demangos and Ignazio Longhi, *Densities on Dedekind domains, completions and Haar measure*, Mathematische Zeitschrift 306 (2024), DOI `10.1007/s00209-023-03415-2`, already used by `PC-061` as its density/Haar boundary control.
- Bounded Fourier--Stieltjes coefficients of finite measures and Plancherel theory on compact abelian groups are standard; Walter Rudin's *Fourier Analysis on Groups* is a classical reference.
- A literature search by the combined structures `Ramanujan sums + profinite Haar + logarithmic/Abel density + first variation` did not identify a pre-existing theorem asserting the project-specific identity (13) for this Prime-Circle Gram family. No historical novelty is claimed merely from that search.

The Mathia-specific content is the exact synthesis of three already-persisted constructions: the `WP-036` Ramanujan feature decomposition, the `PC-061` log-series-to-Haar boundary, and the `WP-034` renormalized birth matrix. Together they force

\[
\boxed{
\text{positive radial Gram}
\to
\text{Haar Gram vacuum}
\to
\text{singular first variation}
\to
C
\to
-\Lambda(p^k)/\sqrt{p^k}\text{ on interior prime rays}.
}
\tag{30}
\]

That identity and the Fourier-coefficient obstruction (24)--(26) are the substantive result recorded here.

## 11. Consequence for the Weil-positivity search

The canonical normalized boundary route is now sharply classified.

Prime Circle does supply a positive family whose probability-normalized boundary is canonical Haar, and the **next-order departure from Haar contains the correct critical finite arithmetic coefficients**. This is stronger than merely saying that the coefficients arise after an arbitrary subtraction. But it simultaneously explains why the positivity has not transferred: the arithmetic is not in the Haar vacuum; it is in an unbounded signed cylindrical tangent outside the ordinary measure/Fisher Hilbert category.

Therefore a surviving route cannot be

\[
\boxed{
\text{positive radial probability geometry}
+\text{ordinary Haar tangent positivity}
\Longrightarrow
\text{Weil positivity}.
}
\]

The remaining possibilities are more structured: an intrinsically weighted distribution space, a growing-conductor semilocal limit, an infinite-dimensional compression/quotient, or a nonseparable finite--archimedean coupling that acts before the singular first variation is isolated. Any such proposal must still explain the Gamma/polar terms and derive its sign independently of RH rather than inherit the signed operator `C` unchanged.