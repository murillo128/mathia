# MC-032 — Huxley–Watt Fourier modes localize the separate-residual burden to the finite-cutoff product annulus

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/BOUNDARY`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

The Fourier route left open by `MC-031` can be localized more sharply before any new exponential-sum estimate is attempted. For

\[
Q_h(N)
=
\sum_{m,n\le N}
\mu(m)\mu(n)
\sin\!\left(\frac{2\pi hN^2}{mn}\right),
\]

define the finite-cutoff convolution coefficient

\[
c_N(q)
:=
\sum_{\substack{mn=q\\m,n\le N}}
\mu(m)\mu(n).
\]

Then, exactly,

\[
Q_h(N)
=
\sum_{q\le N^2}
c_N(q)
\sin\!\left(\frac{2\pi hN^2}{q}\right).
\tag{1}
\]

Thus an individual Fourier mode already factors through the total product `q=mn`: it does **not** retain the individual factor labels once written in its natural one-dimensional coefficient form. What survives the product quotient is the finite-cutoff coefficient `c_N(q)`.

On the low-product interior `q\le N`, the cutoff is inactive, so

\[
c_N(q)=(\mu*\mu)(q)=:\mu_2(q).
\tag{2}
\]

Moreover the entire contribution of this interior to the **weighted truncated Fourier aggregate** from Huxley–Watt is automatically at the RH-compatible square-scale size. If

\[
\mathcal F_H(N)
:=
\sum_{1\le h\le H}\frac{Q_h(N)}{\pi h},
\qquad 1\le H\le N,
\]

and `\mathcal F_H^{\rm int}(N)` denotes the part with `q\le N`, then uniformly in `H`,

\[
\boxed{
\mathcal F_H^{\rm int}(N)=O(N\log N).
}
\tag{3}
\]

The proof uses no cancellation of Möbius signs. Consequently, for every fixed `\varepsilon>0`,

\[
\mathcal F_H^{\rm int}(N)=O_\varepsilon(N^{1+\varepsilon}),
\]

which is already within the separate-residual target at horizon `N^2` used in `MC-031`.

Therefore the unresolved Fourier burden is localized to the finite-cutoff annulus

\[
N<q\le N^2.
\tag{4}
\]

Any termwise or joint-`h` Fourier mechanism that improves the Huxley–Watt residual must obtain its nontrivial arithmetic gain from the annular truncated convolution

\[
\sum_{N<q\le N^2}
c_N(q)
\sin\!\left(\frac{2\pi hN^2}{q}\right),
\tag{5}
\]

or from cancellation between that annular contribution and other terms in the unsplit identity. The low-product convolution interior cannot be the missing source of a power gain because it is already cheap by absolute counting.

This also identifies precisely what product information the Fourier route still preserves relative to `MC-028` and `MC-029`: factor labels are gone, but the **cutoff defect** of the convolution remains. The only potentially useful pre-collapse datum in (5) is the interaction between that finite-cutoff annular coefficient and the reciprocal phase. If a proposed continuation subsequently removes this interaction by the auxiliary convolution or by the full source-prescribed product recombination, the exact Möbius-reflection obstructions of `MC-028`/`MC-029` apply.

## 1. Exact product grouping of each reciprocal Fourier mode

Huxley and Watt's Fourier decomposition of the sawtooth residual uses matrices

\[
Z(h)_{mn}
=
\sin\!\left(\frac{2\pi hN^2}{mn}\right),
\]

so that `Q_h(N)=\mathbf m^{\rm T}Z(h)\mathbf m` for `\mathbf m=(\mu(1),\ldots,\mu(N))^{\rm T}`. The phase depends on `(m,n)` only through `mn`. Grouping terms with the same product gives (1) immediately.

This grouping is an exact quotient of the two factor coordinates. It is important not to describe the scalar `Q_h` as retaining arbitrary factor provenance: after the summation defining the quadratic form, all pairs with the same product are represented only through `c_N(q)`.

For `q\le N`, every factorization `q=mn` automatically has `m,n\le N`; hence

\[
\begin{aligned}
c_N(q)
&=\sum_{mn=q}\mu(m)\mu(n)\\
&=(\mu*\mu)(q),
\end{aligned}
\]

proving (2).

For `N<q\le N^2`, write

\[
e_N(q):=c_N(q)-\mu_2(q).
\tag{6}
\]

Because two divisors in a factor pair cannot both exceed `N` when their product is at most `N^2`, the excluded ordered pairs are disjoint and occur in the two orientations. Therefore

\[
\boxed{
e_N(q)
=-2\sum_{\substack{d\mid q\\d>N}}
\mu(d)\mu(q/d)
\qquad(N<q\le N^2).
}
\tag{7}
\]

Equation (7) is the same finite-cutoff defect studied from the auxiliary-convolution side in `MC-028`. It makes the surviving information layer explicit: ordinary convolution in the interior, cutoff-sensitive divisor structure in the annulus.

## 2. The low-product interior is uniformly cheap for the full retained Fourier aggregate

Exchange the finite `h`- and `q`-sums and define

\[
S_H(x)
:=
\sum_{h=1}^H\frac{\sin(2\pi h x)}{\pi h}.
\tag{8}
\]

The classical partial harmonic sine sums are uniformly bounded:

\[
\sup_{H\ge1}\sup_{x\in\mathbb R}|S_H(x)|<\infty.
\tag{9}
\]

Thus the interior contribution is

\[
\mathcal F_H^{\rm int}(N)
=
\sum_{q\le N}\mu_2(q)S_H(N^2/q),
\tag{10}
\]

and hence

\[
|\mathcal F_H^{\rm int}(N)|
\ll
\sum_{q\le N}|\mu_2(q)|.
\tag{11}
\]

Using only `|\mu|\le1`,

\[
\begin{aligned}
\sum_{q\le N}|\mu_2(q)|
&\le
\sum_{ab\le N}|\mu(a)\mu(b)|\\
&\le
\sum_{a\le N}\left\lfloor\frac Na\right\rfloor\\
&=O(N\log N).
\end{aligned}
\tag{12}
\]

Equations (10)–(12) prove (3), uniformly for every `H` for which the finite Fourier sum is formed. In particular there is no exceptional-set, zero-free-region, random-walk, or sign-cancellation input hidden in this estimate.

A weaker termwise statement follows as well:

\[
\left|
\sum_{q\le N}\mu_2(q)
\sin\!\left(\frac{2\pi hN^2}{q}\right)
\right|
=O(N\log N)
\tag{13}
\]

uniformly in `h`. But (3) is the more relevant boundary for `MC-031`: even after the `1/h` Fourier weights are combined, the whole interior is already below `N^{1+\varepsilon}` for every fixed positive `\varepsilon`.

## 3. The hard Fourier object is the annular truncated convolution, not generic factor geometry

Combining (1) and (2), write

\[
Q_h(N)
=
Q_h^{\rm int}(N)+Q_h^{\rm ann}(N),
\]

where

\[
Q_h^{\rm ann}(N)
=
\sum_{N<q\le N^2}
c_N(q)
\sin\!\left(\frac{2\pi hN^2}{q}\right).
\tag{14}
\]

The source remainder audited in `MC-031` can be made `O_\varepsilon(N^{1+\varepsilon})` for each fixed target `\varepsilon` by choosing an `\varepsilon`-dependent sublinear polynomial cutoff `H`. Equation (3) now removes the low-product interior from the arithmetic budget at the same target scale. The remaining retained-mode problem is therefore (14), jointly over the required `h`-range.

This narrows two possible interpretations of the Fourier escape:

1. **Factor-coordinate geometry is not retained by `Q_h` itself.** Any estimate depending only on the scalar mode sees `(m,n)` through `q=mn` and `c_N(q)`.
2. **Total-product collapse is not yet fatal at this stage.** Unlike the fully recombined coefficient in `MC-029`, `c_N(q)` on the annulus is not pointwise equal to `\pm\mu(q)`. Its cutoff defect remains coupled to the reciprocal oscillatory weight. That coupling is exactly what must be exploited before any later operation erases it.

So the useful frontier is neither "keep arbitrary two-dimensional factor data" nor "study an arbitrary one-dimensional Möbius transform." It is the specific annular object (14), with its finite-cutoff divisor coefficient and reciprocal phase both intact.

## 4. Relation to the exact reflection obstructions

`MC-028` proves that after the source-natural auxiliary convolution with `1`, the degree-two cutoff defect satisfies

\[
(e_N*1)(q)=-2\mu(q)
\qquad(N<q\le N^2).
\tag{15}
\]

`MC-029` extends the same lesson to arbitrary Huxley–Watt cutoffs and all source-prescribed correction degrees: after full product recombination, the upper new block becomes exactly `-\mu(q)`.

Equation (14) sits strictly before those operations. It retains the phase `\sin(2\pi hN^2/q)` against the truncated coefficient itself rather than convolving the coefficient with the auxiliary factor. Hence (15) does not by itself estimate or kill (14).

But it gives a sharp falsification boundary. If a proposed Fourier estimate first averages, convolves, or recombines `c_N` in a way that reduces the annulus to the coefficients from `MC-028` or `MC-029`, then the target Möbius cancellation has been reconstructed rather than weakened. A viable estimate must exploit reciprocal-phase cancellation **before** that collapse, or prove signed cancellation of the full Huxley–Watt identity without separating the annular mode.

## 5. Prior art and novelty assessment

The matrix `Z`, its sawtooth Fourier expansion, the mode matrices `Z(h)`, and the truncated formula

\[
\mathbf m^{\rm T}Z\mathbf m
=
\sum_{h\le H}\frac{Q_h(N)}{\pi h}
+O\!\left(\frac{N^2(\log N)^2\log H}{H}\right)
\]

are from M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the Möbius function*, Chebyshevskii Sbornik 19(3) (2018), 20–34, DOI `10.22405/2226-8383-2018-19-3-20-34`, arXiv `1807.05890`; see `MC-S24`. The source itself presents Fourier truncation as one possible way to use the residual matrix and states that proper use of the truncation remained to be explored.

Grouping a product-dependent double sum by `q=mn`, identifying the inactive-cutoff interior with Dirichlet convolution, and bounding the divisor-counting mass in (12) are elementary classical mechanisms. A targeted search around the Huxley–Watt formula and truncated Möbius convolution literature did not justify a novelty claim for this reorganization, and none is made here.

The durable contribution is the line-specific **mechanism localization** relative to the current frontier: after `MC-031` quantifies how much Fourier resolution is needed, equations (1)–(14) show that the retained Fourier aggregate already pays no critical-scale cost on `q\le N`. Its unresolved arithmetic content is concentrated in the cutoff annulus, where the truncated convolution has not yet undergone the auxiliary operation that `MC-028` proves reconstructs Möbius.

## 6. Boundary conditions and falsification

This result does not prove any nontrivial estimate for `Q_h^{\rm ann}(N)`, either individually or jointly in `h`. It does not show that the annulus is easier than `M(N^2)`, and it does not transfer random-phase heuristics to deterministic Möbius signs.

The `O(N\log N)` interior estimate is an upper bound, not an asymptotic, and its usefulness is specific to the square-scale residual target `O_\varepsilon(N^{1+\varepsilon})`. It says only that the low-product portion cannot be the obstruction in a proof that treats the Huxley–Watt Fourier residual separately.

The decisive continuation is now concrete. A candidate must establish a power-relevant estimate for the annular family (14), or for its weighted joint-`h` sum, using information that is independently weaker than RH-scale Mertens cancellation. It should be killed if the estimate can be transformed through the exact identities of `MC-028`/`MC-029` into a bound for the next Möbius block with no independently controlled intermediate quantity.

## Consequence for the research line

`MC-031` left four broad Fourier/spectral escapes. This result sharpens the Fourier one: the ordinary convolution interior and arbitrary factor-label interpretation can be discarded. The remaining Fourier target is the reciprocal-phase interaction with the **finite-cutoff annular convolution coefficient**.

That is a smaller and more falsifiable object. A useful next attack can now focus on whether the annular coefficient has exploitable cancellation against the reciprocal phases jointly in `h`, whether its cutoff defect admits a source-natural bilinear estimate before auxiliary convolution, or whether any such estimate inevitably collapses back to the Möbius reflection already exposed by `MC-028` and `MC-029`.