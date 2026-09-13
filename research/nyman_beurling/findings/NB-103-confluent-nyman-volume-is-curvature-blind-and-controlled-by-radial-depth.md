# NB-103 — confluent Nyman volume is curvature-blind and controlled by radial depth

**Status:** `EXACT-DERIVED + NYMAN-FINITE-WINDOW-GRAM + CONFLUENT-VOLUME-CONTINUATION + CURVATURE-BLIND + LAGUERRE-MOMENT-LAW + RADIAL-DEPTH-GATE`.

`NB-098`--`NB-102` show that canonical **spectral conditioning** of three nearby right-half-plane zero states can be violently sensitive to local geometry: after canonical deflation the pivots remain one, yet transverse confluence produces collective shear, and for an arbitrary sufficiently local triple the condition number is governed by dimensionless Menger curvature. That leaves an important ambiguity in the fixed-family volume law of `NB-095`--`NB-096`. Does the same curvature singularity destroy the sharp determinant coefficient when distinct states coalesce, or is it only a coordinate-conditioning effect?

At fixed multiplicity the determinant answer is much more rigid. The normalized finite-window volume coefficient of `NB-096` has a **removable, path-independent confluence singularity**. After taking the large-cell limit, that continuation forgets the collision geometry completely. It depends only on the multiplicity `d` and the radial depth

\[
x=2\,\Re\lambda_*\,\log q.
\]

The universal coefficient is a truncated Laguerre moment determinant

\[
\boxed{
\Delta_d(x)
=
\frac{
\det\!\left[\gamma(r+s+1,x)\right]_{r,s=0}^{d-1}
}{
\displaystyle\prod_{j=0}^{d-1}(j!)^2
},
}
\tag{1}
\]

where

\[
\gamma(k,x)=\int_0^x u^{k-1}e^{-u}\,du
\]

is the lower incomplete gamma function. Thus high Menger curvature can make the canonical state coordinates arbitrarily ill-conditioned while leaving the fixed-cardinality **normalized volume** coefficient unchanged in the confluence limit. Curvature is a spectral resource, not a fixed-multiplicity determinant resource.

The distinction matters for the frontier. To preserve the sharp coefficient `1` in a confluent fixed family, the relevant continuum condition is not bounded curvature but

\[
\boxed{\Re\lambda_*\,\log q\to\infty.}
\tag{2}
\]

Near the critical boundary the opposite regime has a precise collapse law:

\[
\boxed{
\Delta_d(x)
=c_d x^{d^2}(1+O_d(x)),
\qquad
c_d=
\frac{\displaystyle\prod_{j=0}^{d-1}(j!)^2}
     {\displaystyle\prod_{j=0}^{2d-1}j!}.
}
\tag{3}
\]

This does **not** solve the repeated-zero state problem, the growing-`d` problem, diagonal correlation normalization, or target conversion. It isolates which singularity survives at the determinant-volume level.

## 1. Strip the coordinate factors before taking confluence

Keep the notation of `NB-095`--`NB-096`. For a fixed distinct family

\[
F=(\lambda_1,\ldots,\lambda_d),
\qquad
\Re\lambda_r=a_r>0,
\]

let

\[
M_{m,q}=S_{mq}^*A_{m,mq}^{-1}S_{mq}
\]

be the interacting state leverage matrix on the band `m <= n < mq`. `NB-096` proves the exact identity

\[
\boxed{
q^{-2A_F}\det M_{m,q}
=
\frac{\det C_{m,q}(F)}{\det G_F(\infty)},
\qquad
A_F=\sum_{r=1}^d a_r.
}
\tag{4}
\]

Both matrices on the right contain the row/column normalization `2 sqrt(a_r a_s)`. Those factors cancel **exactly** in the determinant quotient, so they should be removed before any confluence argument. Introduce independent complex variables `z,w` and the stripped kernels

\[
\begin{aligned}
\mathscr C_{m,q}(z,w)
:={}&
\frac{m^{z+w}}
     {(z+\tfrac12)(w+\tfrac12)}
\sum_{n=m}^{mq-1} n(n+1)\\
&\times
\left(n^{-z-1/2}-(n+1)^{-z-1/2}\right)
\left(n^{-w-1/2}-(n+1)^{-w-1/2}\right),
\end{aligned}
\tag{5}
\]

and

\[
\mathscr G_q(z,w)
=
\frac{1-q^{-(z+w)}}{z+w},
\qquad
\mathscr G_\infty(z,w)
=
\frac1{z+w}.
\tag{6}
\]

Then `(4)` is equivalently

\[
\boxed{
q^{-2A_F}\det M_{m,q}
=
\frac{
\det[\mathscr C_{m,q}(\lambda_r,\overline{\lambda_s})]_{r,s=1}^d
}{
\det[\mathscr G_\infty(\lambda_r,\overline{\lambda_s})]_{r,s=1}^d
}.
}
\tag{7}
\]

For fixed `m,q`, both stripped kernels are holomorphic in a neighborhood of any point `(lambda_*, overline(lambda_*))` with `Re(lambda_*)>0`. The apparent singularity when the `lambda_r` collide therefore belongs entirely to the two determinants, not to the kernels themselves.

## 2. The determinant quotient has a path-independent confluent continuation

The needed confluence fact is elementary. Let `K(z,w)` be holomorphic near `(z_*,w_*)`. For pairwise distinct nodes `z_1,...,z_d` and `w_1,...,w_d`, successive divided differences in rows and columns give

\[
\frac{\det[K(z_i,w_j)]}
     {V(z_1,\ldots,z_d)V(w_1,\ldots,w_d)}
\longrightarrow
\det\left[
\frac{\partial_z^r\partial_w^s K(z_*,w_*)}{r!s!}
\right]_{r,s=0}^{d-1},
\tag{8}
\]

as all row nodes tend to `z_*` and all column nodes tend to `w_*`, where `V` is the Vandermonde product. No comparability of the pairwise gaps and no prescribed collision tree is required.

Apply `(8)` to the numerator and denominator of `(7)`, with `w_j=overline(lambda_j)`. The same factor `|V(lambda_1,...,lambda_d)|^2` occurs on both sides and cancels. Since the denominator derivative matrix is the Gram matrix of the linearly independent functions

\[
t^r e^{-\lambda_*t},
\qquad 0\le r<d,
\]

on `[0,infinity)`, its determinant is positive. Hence `(7)` has a removable confluence singularity. Define its continuation by

\[
\boxed{
\mathcal V^{\mathrm{conf}}_{d,m,q}(\lambda_*)
:=
\frac{
\det[\partial_z^r\partial_w^s\mathscr C_{m,q}
      (\lambda_*,\overline{\lambda_*})]_{r,s=0}^{d-1}
}{
\det[\partial_z^r\partial_w^s\mathscr G_\infty
      (\lambda_*,\overline{\lambda_*})]_{r,s=0}^{d-1}
}.
}
\tag{9}
\]

The omitted factorial row/column factors from `(8)` cancel between numerator and denominator. Equation `(9)` is **path-independent**: transverse, tangential, hierarchical, or otherwise irregular distinct-node collisions all have the same determinant limit once their center and multiplicity agree.

This is already enough to separate volume from conditioning. `NB-102` can assign radically different condition numbers to two collision paths with the same center, while `(9)` assigns them the same confluent determinant coefficient.

## 3. The discrete kernel converges with all fixed derivatives, uniformly in depth

`NB-095` proved entrywise that `C_(m,q)` converges to the finite-window exponential Gram uniformly for integer `q>=2`. For confluence one needs the same statement for the finite number of derivatives appearing in `(9)`. The original sum-integral argument upgrades directly because the stripped kernel is holomorphic.

Fix a small closed polydisc around

\[
(\lambda_*,\overline{\lambda_*}),
\qquad a:=\Re\lambda_*>0,
\]

on which `Re(z+w)` stays bounded below by a positive constant. Uniformly on a slightly larger polydisc,

\[
\frac{n(n+1)}
     {(z+\tfrac12)(w+\tfrac12)}
\left(n^{-z-1/2}-(n+1)^{-z-1/2}\right)
\left(n^{-w-1/2}-(n+1)^{-w-1/2}\right)
=
n^{-1-z-w}
+O_{\lambda_*}(n^{-2-\Re(z+w)}).
\tag{10}
\]

Multiplying by `m^(z+w)` and summing from `m` to `mq-1`, the remainder contributes `O_(lambda_*)(m^-1)` uniformly for every integer `q>=2`. The main sum satisfies the same uniform sum-integral estimate,

\[
m^{z+w}\sum_{n=m}^{mq-1}n^{-1-z-w}
=
\frac{1-q^{-(z+w)}}{z+w}
+O_{\lambda_*}(m^{-1}).
\tag{11}
\]

Thus

\[
\boxed{
\mathscr C_{m,q}(z,w)
=
\mathscr G_q(z,w)+O_{\lambda_*}(m^{-1})
}
\tag{12}
\]

uniformly on the polydisc and uniformly in integer `q>=2`. Cauchy's derivative estimates applied on nested polydiscs then give, for every fixed `0<=r,s<d`,

\[
\partial_z^r\partial_w^s\mathscr C_{m,q}
=
\partial_z^r\partial_w^s\mathscr G_q
+O_{d,\lambda_*}(m^{-1}),
\tag{13}
\]

again uniformly in `q>=2`.

Because the denominator of `(9)` is fixed and nonzero, determinant continuity now yields the uniform fixed-multiplicity law

\[
\boxed{
\mathcal V^{\mathrm{conf}}_{d,m,q}(\lambda_*)
=
\frac{
\det[\partial_z^r\partial_w^s\mathscr G_q
      (\lambda_*,\overline{\lambda_*})]_{r,s=0}^{d-1}
}{
\det[\partial_z^r\partial_w^s\mathscr G_\infty
      (\lambda_*,\overline{\lambda_*})]_{r,s=0}^{d-1}
}
+O_{d,\lambda_*}(m^{-1}).
}
\tag{14}
\]

The error constant is uniform in `q`, but it is **not** claimed uniform as `a -> 0` or as `d -> infinity`.

## 4. The continuum coefficient is exactly a Laguerre moment determinant

Let

\[
L=\log q,
\qquad
x=2aL.
\tag{15}
\]

The finite-window kernel has the integral form

\[
\mathscr G_q(z,w)
=
\int_0^L e^{-(z+w)t}\,dt.
\tag{16}
\]

Therefore at the confluent center,

\[
\partial_z^r\partial_w^s\mathscr G_q
(\lambda_*,\overline{\lambda_*})
=
(-1)^{r+s}
\int_0^L t^{r+s}e^{-2at}\,dt.
\tag{17}
\]

The corresponding half-line derivative matrix replaces `L` by `infinity`. Scaling `u=2at` cancels all row and column powers of `2a` in the determinant quotient. Since

\[
\int_0^x u^{r+s}e^{-u}\,du
=
\gamma(r+s+1,x)
\]

and

\[
\det[(r+s)!]_{r,s=0}^{d-1}
=
\prod_{j=0}^{d-1}(j!)^2,
\tag{18}
\]

`(14)` becomes

\[
\boxed{
\mathcal V^{\mathrm{conf}}_{d,m,q}(\lambda_*)
=
\Delta_d(2a\log q)
+O_{d,\lambda_*}(m^{-1}),
}
\tag{19}
\]

uniformly in integer `q>=2`, with `Delta_d` given by `(1)`.

The moment interpretation immediately gives

\[
0<\Delta_d(x)<1
\qquad(x>0),
\tag{20}
\]

strict monotonicity in `x`, and

\[
\Delta_d(x)\longrightarrow1
\qquad(x\to\infty).
\tag{21}
\]

Indeed, the numerator is the Gram determinant of `1,u,...,u^(d-1)` in `L^2([0,x],e^{-u}du)`, while the denominator is the same Gram determinant on the whole half-line. Enlarging a nontrivial interval adds a positive-definite polynomial Gram increment.

At the other endpoint,

\[
\gamma(r+s+1,x)
=
\frac{x^{r+s+1}}{r+s+1}
+O_d(x^{r+s+2}).
\tag{22}
\]

Extracting the row and column powers of `x` leaves the classical Hilbert determinant. This gives exactly `(3)`, with exponent `d^2`. Thus a fixed confluent packet does not lose volume because its nodes are close; it loses normalized finite-window volume only when the available radial depth `2a log q` is too small.

For three states the universal coefficient is explicit:

\[
\boxed{
\begin{aligned}
\Delta_3(x)={}&1-
\left(\frac{x^4}{4}-x^3+3x^2+3\right)e^{-x}\\
&+\left(\frac{x^4}{4}+x^3+3x^2+3\right)e^{-2x}
-e^{-3x},
\end{aligned}
}
\tag{23}
\]

and

\[
\boxed{
\Delta_3(x)=\frac{x^9}{8640}+O(x^{10}).
}
\tag{24}
\]

## 5. Matched controls: the curvature blow-up disappears from volume

Take the transverse family from `NB-098`, after vertical gauge normalization,

\[
\lambda_1=a+i\varepsilon,
\qquad
\lambda_2=a+c\varepsilon,
\qquad
\lambda_3=a-i\varepsilon,
\qquad c\ne0.
\tag{25}
\]

`NB-102` gives dimensionless Menger curvature `Theta(a/epsilon)` and hence

\[
\kappa_2(C)=\Theta(\varepsilon^{-4}).
\tag{26}
\]

Nevertheless `(8)`--`(19)` force its normalized Nyman volume coefficient to converge, after the fixed-`m` confluence continuation and then `m -> infinity`, to

\[
\Delta_3(2a\log q).
\tag{27}
\]

Now compare a tangent family such as

\[
\lambda_1=a+i\varepsilon,
\qquad
\lambda_2=a+c\varepsilon^2,
\qquad
\lambda_3=a-i\varepsilon.
\tag{28}
\]

Its dimensionless Menger curvature stays bounded and its canonical three-state condition number stays bounded by `NB-100`--`NB-102`, but its volume limit is **the same** `(27)`. A hierarchical family with one pair at scale `epsilon^m` and the third state at scale `epsilon` also has the same determinant continuation. The collision path can change the spectrum by arbitrarily large factors without changing the limiting determinant coefficient at all.

This is not paradoxical. `NB-096` already proved that canonical deflation cancels raw Cauchy crowding **in determinant volume**. `NB-098`--`NB-102` then showed that the cancellation can hide a huge unit-triangular shear. `NB-103` identifies the exact confluent limit of what remains after that volume cancellation. The two observables answer different questions.

## 6. The surviving fixed-multiplicity gate is radial, not angular

For fixed `a>0`, `(21)` shows that

\[
\Delta_d(2a\log q)\to1
\qquad(q\to\infty).
\tag{29}
\]

So the sharp coefficient `1` from `NB-096` survives arbitrary fixed-multiplicity confluence once the multiplicative depth is large enough. No bounded-curvature hypothesis is required at the determinant level.

If one subsequently lets the center approach the critical boundary, the continuum law exposes the relevant dimensionless parameter. Writing

\[
x=2a\log q,
\]

there are three regimes:

- if `x -> infinity`, the normalized confluent volume coefficient tends to `1`;
- if `x -> x_0 in (0,infinity)`, it tends to the fixed number `Delta_d(x_0)` in `(0,1)`;
- if `x -> 0`, it collapses like `c_d x^(d^2)`.

This is a **continuum fixed-multiplicity classification**. Equation `(19)` gives its discrete Nyman realization for each fixed interior center and fixed `d`; it does not claim a two-parameter error estimate uniform as `a -> 0`. Establishing such a boundary-uniform discretization would be a separate theorem.

For a zeta zero `rho=beta+i gamma`, `a=beta-1/2`. Hence the new volume-scale quantity is

\[
\boxed{
(\beta-\tfrac12)\log q,
}
\tag{30}
\]

not the local Menger curvature. This does **not** say that curvature is irrelevant to Nyman approximation. It says only that curvature cannot be invoked as the obstruction to the fixed-cardinality determinant law. Curvature remains potentially decisive for coordinate stability, spectral lower bounds, growing families, and any target-aware argument that needs more than determinant volume.

## 7. Prior-art boundary and falsification conditions

The confluence mechanism in `(8)` is standard analytic determinant geometry: confluent Cauchy matrices and divided-difference limits are classical, and no novelty is claimed for them. Likewise the determinant in `(1)` is a classical Laguerre Hankel determinant. For `alpha=0`, its normalization is exactly the finite-`d` Laguerre unitary ensemble probability that all eigenvalues lie in `(0,x)`, i.e. the largest-eigenvalue distribution. A direct comparator is S. Lyu and Y. Chen, *The largest eigenvalue distribution of the Laguerre unitary ensemble*, Acta Math. Sci. 37 (2017), 439--462, DOI `10.1016/S0252-9602(17)30013-9`, also circulated as arXiv `1511.00795`. More general Laguerre Hankel determinant ratios as eigenvalue gap probabilities are standard in that literature.

The line-local contribution is therefore **not** the incomplete-gamma determinant itself. It is the identification of the `NB-096` normalized finite-window Nyman state-volume coefficient with this universal confluent law, together with the consequence that the Menger-curvature singularity discovered in `NB-098`--`NB-102` is absent from fixed-multiplicity determinant volume and is replaced by the radial-depth parameter `(30)`. No external theorem is load-bearing in `(4)`--`(24)`, so `SOURCES.md` does not require a new dependency.

Several boundaries are essential. First, `(9)` is an analytic continuation of the **distinct-state determinant coefficient**. It is not a derivation of the correct causal state realization for a genuine multiple zeta zero. Exact multiplicity still requires the confluent/Jordan state system already separated in `NB-098`--`NB-102`.

Second, `d` is fixed. Nothing here gives uniform control as the number of selected zeros grows. A large packet may accumulate shear, derivative orders, discretization losses, or diagonal-normalization cost in ways invisible to every fixed-`d` statement.

Third, this finding concerns the unnormalized state determinant `det M` after the exact `q^(2A_F)` scaling from `NB-096`. The bounded diagonal-correlation normalization bill of `NB-095` was proved only with constants depending on the fixed distinct family; confluence-uniform correlation normalization is not established here.

Finally, determinant volume is still not target distance. `NB-001`, `NB-004`, and the target-aware branch remain binding: a spectacularly well-behaved volume coefficient cannot by itself prove or disprove Nyman approximation.

## Consequence

`NB-102` left a tempting source question: perhaps actual off-critical zeta triples must have bounded dimensionless Menger curvature in order for the finite-state Nyman mechanism to remain usable. `NB-103` shows that this requirement is **too strong for the determinant-volume branch**. At fixed multiplicity, even arbitrarily high-curvature confluence has a canonical path-independent volume limit.

The fixed-family determinant frontier therefore moves from local angular geometry to radial depth:

\[
\boxed{
q^{-2A_F}\det M
\quad\xrightarrow[\text{confluence},\ m\to\infty]{}\quad
\Delta_d\!\left(2(\beta-\tfrac12)\log q\right).
}
\tag{31}
\]

If the next argument needs only volume, it should attack uniformity in `(beta-1/2) log q`, growing multiplicity, or diagonal normalization rather than zero-triple curvature. If it needs spectral inversion or stable target coordinates, the Menger-curvature obstruction of `NB-102` remains fully active. The two branches are now cleanly separated.