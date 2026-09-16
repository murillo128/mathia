# AF-389 — Multiscale solid PF3 excludes every finite-order PF2-boundary contact

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `TARGET-FIDELITY` · `TOTAL-POSITIVITY` · `PF3` · `TOEPLITZ` · `MULTISCALE` · `BOUNDARY-RIGIDITY` · `NO-NOVELTY-CLAIM`

## Claim

AF-388 proves that shrinking solid order-two/order-three Toeplitz tests exclude a nondegenerate quadratic zero of the logarithmic curvature. In fact the same multiscale certificate excludes **every finite-order contact** with the `PF_2` boundary.

Let

\[
f:\mathbb R\to(0,\infty)
\]

be `C^\infty`, let `h_\nu>0` with `h_\nu\to0`, and suppose that for every `\nu` and every integer `d`,

\[
C_{2,\nu}(d)
:=
\det\!\left(f((d+i-j)h_\nu)\right)_{i,j=0}^{1}
\ge0
\tag{1}
\]

and

\[
C_{3,\nu}(d)
:=
\det\!\left(f((d+i-j)h_\nu)\right)_{i,j=0}^{2}
\ge0.
\tag{2}
\]

Write

\[
g=\log f,
\qquad
q=-g''.
\tag{3}
\]

Then `q\ge0`, and every zero of `q` is infinitely flat:

\[
q(x_0)=0
\quad\Longrightarrow\quad
q^{(k)}(x_0)=0
\qquad(k=0,1,2,\ldots).
\tag{4}
\]

Equivalently, no point can satisfy

\[
q(x_0+y)=c y^{2m}+o(y^{2m})
\qquad(c>0,\;m\ge1).
\tag{5}
\]

Thus the fixed-lattice alias of AF-387 becomes much more rigid under one-profile vanishing-mesh consistency: not only quadratic but **all finite-order lower-order degeneracies are forbidden**. Any remaining smooth boundary alias must live on an infinitely-flat stratum.

A useful analytic corollary is immediate. If `f` is positive real-analytic on `\mathbb R`, then either

\[
q(x)>0\quad\text{for every }x,
\tag{6}
\]

or `q\equiv0`, hence

\[
f(x)=e^{ax+b}.
\tag{7}
\]

So in the analytic category the multiscale solid certificate leaves no nontrivial finite or infinite flat boundary contact: the only non-strict alternative is the globally affine logarithm.

## Step 1: order two gives nonnegative logarithmic curvature

As in AF-388, define for a real center `x` and mesh `h`

\[
D_2(x,h)
=
\det
\begin{pmatrix}
f(x)&f(x-h)\\
f(x+h)&f(x)
\end{pmatrix}.
\tag{8}
\]

The local expansion

\[
\frac{D_2(x,h)}{f(x)^2}
=-g''(x)h^2+o(h^2)
=q(x)h^2+o(h^2)
\tag{9}
\]

combined with nearest-grid centers shows from `(1)` that

\[
q(x)\ge0
\qquad\text{for every }x.
\tag{10}
\]

Consequently, if a zero `x_0` of `q` is not infinitely flat, its first nonzero derivative has even order. Thus for some `m\ge1` and `c>0`,

\[
q(x_0+y)=c y^{2m}+o(y^{2m}).
\tag{11}
\]

It remains to show that `(11)` contradicts the shrinking solid order-three inequalities.

## Step 2: integrate the finite-order contact into the logarithm

Put

\[
n=2m+2.
\tag{12}
\]

Since `g''=-q`, integrating `(11)` twice gives constants `\alpha,\beta` such that

\[
g(x_0+y)
=
\alpha+\beta y
-\lambda y^n
+o(y^n),
\qquad
\lambda=\frac{c}{n(n-1)}>0.
\tag{13}
\]

For each mesh choose an integer `d_\nu` nearest to `x_0/h_\nu` and write

\[
x_\nu=d_\nu h_\nu,
\qquad
r_\nu=\frac{x_\nu-x_0}{h_\nu},
\qquad
|r_\nu|\le\frac12.
\tag{14}
\]

After passing to a subsequence,

\[
r_\nu\to r
\qquad\text{for some }|r|\le\frac12.
\tag{15}
\]

At the nine arguments entering the solid `3\times3` determinant,

\[
x_\nu+(i-j)h_\nu
=x_0+h_\nu(r_\nu+i-j),
\qquad 0\le i,j\le2.
\tag{16}
\]

The Taylor remainder in `(13)` is uniform for these bounded scaled arguments. Therefore

\[
f\!\left(x_\nu+(i-j)h_\nu\right)
=
\exp\!\left(
\alpha+\beta h_\nu(r_\nu+i-j)
-\lambda h_\nu^n(r_\nu+i-j)^n
+o(h_\nu^n)
\right).
\tag{17}
\]

The affine part `\alpha+\beta y` contributes only a positive common factor together with positive row and column factors, so it cannot change the determinant sign. Hence the sign of the solid order-three minor is the sign of the determinant of

\[
M_\nu(i,j)
=
\exp\!\left(
-\lambda h_\nu^n(r_\nu+i-j)^n
+o(h_\nu^n)
\right).
\tag{18}
\]

## Step 3: the universal leading determinant

Let

\[
p(z)=z^n,
\qquad
\varepsilon_\nu=h_\nu^n.
\tag{19}
\]

Then

\[
M_\nu(i,j)
=1-\lambda\varepsilon_\nu p(r_\nu+i-j)+o(\varepsilon_\nu).
\tag{20}
\]

Because the constant `3\times3` all-ones matrix has rank one, its determinant and first variation both vanish. The first possible term is quadratic in the perturbation. Subtract row zero from rows one and two and then column zero from columns one and two. The coefficient is

\[
\det M_\nu
=
\lambda^2\varepsilon_\nu^2 K_n(r_\nu)
+o(\varepsilon_\nu^2),
\tag{21}
\]

where

\[
K_n(r)=\det B(r)
\tag{22}
\]

and, for `a,b\in\{1,2\}`,

\[
B_{ab}(r)
=
p(r+a-b)-p(r-b)-p(r+a)+p(r).
\tag{23}
\]

The important point is that this coefficient can be signed for **every** even `n\ge4` without computing an ever-growing Taylor expansion.

Since

\[
p''(z)=n(n-1)z^{2m},
\tag{24}
\]

two applications of the fundamental theorem of calculus give

\[
B_{ab}(r)
=-n(n-1)
\int_0^a\!\int_0^b
(r+s-t)^{2m}\,dt\,ds.
\tag{25}
\]

Define

\[
A_m(u)
:=
\int_0^1\!\int_0^1
(u+s-t)^{2m}\,dt\,ds.
\tag{26}
\]

Splitting the rectangles in `(25)` into unit squares yields

\[
H(r):=
\left(
\int_0^a\!\int_0^b(r+s-t)^{2m}\,dt\,ds
\right)_{a,b=1}^{2}
=
\begin{pmatrix}
A_m(r) & A_m(r)+A_m(r-1)\\
A_m(r)+A_m(r+1) & 2A_m(r)+A_m(r-1)+A_m(r+1)
\end{pmatrix}.
\tag{27}
\]

Therefore

\[
K_n(r)
=[n(n-1)]^2\det H(r)
\tag{28}
\]

with

\[
\det H(r)
=A_m(r)^2-A_m(r-1)A_m(r+1).
\tag{29}
\]

Combining `\lambda=c/[n(n-1)]` with `(21)` and `(28)`, the leading term simplifies to

\[
\det M_\nu
=
c^2 h_\nu^{2n}
\Bigl[
A_m(r_\nu)^2
-A_m(r_\nu-1)A_m(r_\nu+1)
\Bigr]
+o(h_\nu^{2n}).
\tag{30}
\]

This formula is the all-orders replacement for the `h^8` boundary calculation in AF-388.

## Step 4: the coefficient is strictly negative in the nearest-cell window

The function `A_m` is even. Indeed, swapping `s` and `t` in `(26)` gives

\[
A_m(-u)=A_m(u).
\tag{31}
\]

It is also strictly increasing as a function of `|u|` away from zero. If `S,T` are independent uniform variables on `[0,1]` and `X=S-T`, then `X` has a symmetric distribution and

\[
A_m(u)=\mathbb E(u+X)^{2m}.
\tag{32}
\]

Expanding the even moments,

\[
A_m(u)
=
\sum_{j=0}^{m}
\binom{2m}{2j}
 u^{2m-2j}\,\mathbb E X^{2j}.
\tag{33}
\]

Every coefficient is nonnegative and the leading one is positive, so

\[
0\le u<v
\quad\Longrightarrow\quad
A_m(u)<A_m(v).
\tag{34}
\]

For `|r|\le1/2`,

\[
|r-1|\ge|r|,
\qquad
|r+1|\ge|r|,
\tag{35}
\]

and at least one inequality is strict. By `(31)` and `(34)`,

\[
A_m(r-1)A_m(r+1)>A_m(r)^2.
\tag{36}
\]

Hence

\[
K_n(r)<0
\qquad\text{for every }|r|\le\frac12.
\tag{37}
\]

The inequality is strict on a compact interval, so its negative margin is uniform there.

Returning to the convergent subsequence `(15)`, `(30)` and `(37)` imply

\[
C_{3,\nu}(d_\nu)<0
\tag{38}
\]

for all sufficiently large `\nu`, contradicting `(2)`. Thus `(11)` is impossible for every finite `m`, proving `(4)`.

## Recovery interpretation

AF-387 shows that one fixed lattice can hide a non-solid negative order-three minor behind a lower-order degenerate stratum even when support is connected and the full `PF_2` target holds. AF-388 shows that a quadratic version of that stratum cannot persist when the same continuous source must satisfy the solid certificate on arbitrarily fine lattices.

AF-389 identifies the stronger resource precisely: **cross-scale compatibility remembers the order of contact with the compressed lower-order boundary**. Every finite-order contact produces, after rescaling by its own natural exponent, the same kind of rank-one perturbation problem. The resulting coefficient is a `2\times2` determinant of integrated even-power kernels, and nearest-grid uncertainty is defeated by the strict monotonicity in `(34)`.

This is a genuine minimal-lift refinement. One fixed lattice retains too little placement information, while an unbounded hierarchy of compatible lattice scales recovers enough infinitesimal information to eliminate every finite-order boundary alias. The surviving gap is now much narrower: only infinitely-flat smooth contacts remain possible.

## Analytic corollary

Assume additionally that `f` is positive real-analytic on `\mathbb R`. Then `g=\log f` and `q=-g''` are real-analytic. If `q(x_0)=0`, `(4)` says that every derivative of `q` vanishes at `x_0`, so analyticity forces `q` to vanish identically on the connected real line. Therefore either `q>0` everywhere or `q\equiv0`.

In the latter case `g''=0`, so `g(x)=ax+b` and `(7)` follows. In particular, if one additionally requires `f` to be integrable and positive on all of `\mathbb R`, the exponential alternative is impossible and the multiscale solid certificate forces

\[
-(\log f)''>0
\qquad\text{everywhere}.
\tag{39}
\]

This is still a conclusion about the lower-order boundary, not a proof of continuum `PF_3` or `TN_3`.

## What remains open

The theorem closes the finite-order branch left explicitly open by AF-388, but it does not establish full continuum order-three total nonnegativity from the sampled solid hierarchy.

For merely smooth sources, a nonnegative `q` can vanish to infinite order without vanishing identically. The remaining boundary question is therefore sharply localized:

> Can an infinitely-flat zero of `q=-(\log f)''` coexist with nonnegative solid order-two/order-three Toeplitz minors on a vanishing mesh sequence while some arbitrary-placement continuum order-three minor is negative?

A negative answer would remove the last smooth lower-order boundary stratum and make the strict-interior recognition route effectively complete under multiscale compatibility. A positive example would identify the exact residual information that even infinitely many compatible solid samples fail to retain.

No claim is made here about orders `k>3`.

## Prior-art and novelty audit

The surrounding Pólya-frequency and total-positivity theory is classical and already contains much stronger full-target characterization machinery than the reduced certificate studied here.

- Samuel Karlin, ***Total Positivity, Vol. I***, Stanford University Press (1968). Role: classical Pólya-frequency/translation-kernel and total-positivity framework.
- H. F. Weinberger, **“A Characterization of the Polya Frequency Functions of Order 3,”** *Applicable Analysis* **15**(1--4) (1983), 53--69, DOI `10.1080/00036818308839439`. Role: direct classical characterization territory for full `PF_3`; AF-389 is not proposed as a new characterization of the `PF_3` class.
- M. Gasca and J. M. Peña, **“Characterizations and Decompositions of Almost Strictly Positive Matrices,”** *SIAM Journal on Matrix Analysis and Applications* **28**(1) (2006), 1--8, DOI `10.1137/050631203`. Role: boundary-minor recognition on structured nonstrict total-positivity strata, emphasizing that lower-order degeneracy carries information not present in naive reduced minor tests.
- S. Launois and T. H. Lenagan, **“Efficient Recognition of Totally Nonnegative Matrix Cells,”** *Foundations of Computational Mathematics* **14** (2014), 371--387, DOI `10.1007/s10208-013-9169-5`. Role: cell/zero-pattern-dependent reduced recognition for nonstrict total nonnegativity; closest matrix-level analogue of retaining boundary-stratum information.
- Christian Grussler and Tobias Damm, **“Efficient `k`-Sign Consistency Verification of Hankel Matrices via Schur Polynomials,”** arXiv:`2602.08122` (2026). Role: current structured-minor recognition theory, including extensions to Toeplitz settings, and the immediate finite-matrix context for AF-383--AF-388.

A targeted search across `PF_3`, smooth/log-concave translation kernels, finite-order boundary contact, and reduced total-nonnegativity recognition did not surface the exact implication `(4)` from **only the compatible shrinking solid order-two/order-three certificate**. No broad novelty claim is made. The durable result is the direct all-orders asymptotic reduction `(30)` and the exact elimination of every finite-order lower-order contact under this specific multiscale compression model.

## Riemann-facing boundary

This finding has no direct RH consequence and supplies no arithmetic signs. It is upstream theory about what a compressed determinant certificate retains when it is observed consistently across scales.

If a later prime-derived kernel intrinsically provides the required solid signs on a hierarchy `h_\nu\to0`, AF-389 says that its logarithmic curvature cannot touch zero at finite order. This may simplify a later recognition argument by replacing a large family of boundary degeneracies with one sharply defined infinitely-flat residual case. It must not be read backward as evidence that any prime-derived kernel has those signs.

## Boundaries and falsification checks

Strict positivity of `f` is required to form `g=\log f` and factor the affine logarithmic term. Kernels with zeros require a separate local analysis.

`C^\infty` is used only to state the compact conclusion `(4)`. For a fixed `m`, the contradiction to a contact `(11)` needs enough local differentiability to obtain `(13)` through order `2m+2`; a finite-regularity version can therefore be stated order by order.

The same continuous profile must be sampled on every mesh. Unrelated discrete sequences at different resolutions do not share the expansion `(13)` and remain subject to the fixed-grid obstruction of AF-387.

Both order-two and order-three solid inequalities are used. Order two supplies `q\ge0`, which forces the first nonzero derivative at a zero to have even order and positive coefficient. Order three supplies the contradiction.

The nearest-grid choice is essential only to keep `r_\nu` in `[-1/2,1/2]`. Formula `(37)` shows that the universal leading coefficient is strictly negative throughout this entire uncertainty window; no mesh point is required to hit `x_0` exactly.

Finally, infinite flatness is a necessary condition on a surviving smooth boundary alias, not evidence that such an alias exists. The theorem neither constructs one nor proves that the sampled solid hierarchy is sufficient for continuum `TN_3`.