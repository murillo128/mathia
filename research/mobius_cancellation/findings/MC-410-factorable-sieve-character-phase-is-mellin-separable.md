# MC-410 — Factorable sieve character phase is Mellin-separable before dispersion

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The well-factorable upper-sieve representation of `MC-409` supplies genuine coefficient structure, but **it does not by itself create a nonseparable source-character phase**.

For a Dirichlet character `chi`, write the character twist of an arithmetic function `f` as

\[
T_\chi f(n):=\chi(n)f(n).
\]

Because `chi` is completely multiplicative, twisting is an exact endomorphism of the Dirichlet-convolution algebra:

\[
\boxed{
T_\chi(f*g)=(T_\chi f)*(T_\chi g).
}
\tag{1}
\]

For one factorable component of the upper-sieve coefficient,

\[
\lambda=\alpha*\beta,
\qquad
w=\lambda*1,
\]

this gives

\[
\boxed{
T_\chi w=(\alpha\chi)*(\beta\chi)*\chi.
}
\tag{2}
\]

Consequently the `MC-409` off-diagonal is exactly

\[
\boxed{
S_\chi(N)
=\sum_{uvm\le N}
\alpha_u\beta_v\chi(u)\chi(v)\chi(m).
}
\tag{3}
\]

The three-variable appearance in `(3)` therefore contains no intrinsic bilinear oscillation of the form that makes sums such as `chi(uv+a)` or Kloosterman phases nontrivial: the source phase itself is the tensor product `chi(u)chi(v)chi(m)`.

This remains true after the natural archimedean coupling is localized. On a rectangular box with separate cutoffs in `u,v,m`, the sum factors **exactly** into three one-dimensional twisted sums. More generally, if `V` is a smooth compactly supported function on the positive reals and

\[
S_{\chi,V}(N)
:=\sum_{u,v,m}
\alpha_u\beta_v\chi(uvm)
V\!\left(\frac{uvm}{N}\right),
\]

then Mellin inversion on any line `Re(s)=c>1` gives

\[
\boxed{
S_{\chi,V}(N)
=\frac{1}{2\pi i}\int_{(c)}
\widetilde V(s)N^s
A_\chi(s)B_\chi(s)L(s,\chi)\,ds,
}
\tag{4}
\]

where

\[
A_\chi(s)=\sum_u \alpha_u\chi(u)u^{-s},
\qquad
B_\chi(s)=\sum_v \beta_v\chi(v)v^{-s}.
\]

Thus the moving product boundary `uvm\asymp N` is Mellin-diagonal: it couples the factors only through one scalar transform parameter `s`, not through a new arithmetic relation among `u,v,m`.

For a finite linear combination of well-factorable components, `(2)`--`(4)` hold termwise. Therefore **well-factorability alone does not provide the retained arithmetic variable sought in the source-depth clue**. It remains potentially useful, but only if a subsequent operation creates or exposes arithmetic geometry not present in the raw product character phase—for example a congruence, additive shift, reciprocal/Kloosterman phase, modulus average, or another nonseparable relation produced by dispersion, Poisson, or a comparable transformation before absolute values destroy the coefficient structure.

This narrows, but does not kill, the `MC-409` route. A Type I/II or dispersion argument may still exploit the support and norm structure of `alpha,beta`; what is ruled out is crediting the bare factorization `lambda=alpha*beta` and the phase `chi(uvm)` as an additional oscillatory dimension.

No estimate for `M(x)` follows.

## 1. Character twisting commutes with Dirichlet convolution

For arbitrary arithmetic functions `f,g`, complete multiplicativity gives

\[
\begin{aligned}
((T_\chi f)*(T_\chi g))(n)
&=\sum_{d\mid n}f(d)\chi(d)g(n/d)\chi(n/d)\\
&=\chi(n)\sum_{d\mid n}f(d)g(n/d)\\
&=T_\chi(f*g)(n).
\end{aligned}
\tag{5}
\]

The identity also covers non-units modulo the conductor: if `chi(n)=0`, then for every factorization `n=d(n/d)` at least one character factor vanishes, so both sides of `(5)` are zero.

Now `w=lambda*1` and `lambda=alpha*beta`, so `(1)` gives `(2)`. Summing `(2)` through `N` yields `(3)` directly.

This is stronger than the observation in `MC-409` that `chi(uvm)` is multiplicatively separable during an `m`-only differencing step. It shows that the entire factorable upper-sieve coefficient sits inside the same convolution algebra on which the source character acts diagonally.

## 2. Rectangular localization has no bilinear source phase

Let `F,G,H` be arbitrary finitely supported weights. Then

\[
\begin{aligned}
&\sum_{u,v,m}
\alpha_u\beta_v\chi(uvm)F(u)G(v)H(m)\\
&\qquad=
\left(\sum_u\alpha_u\chi(u)F(u)\right)
\left(\sum_v\beta_v\chi(v)G(v)\right)
\left(\sum_m\chi(m)H(m)\right).
\end{aligned}
\tag{6}
\]

So after ordinary dyadic localization, any box lying wholly inside the hyperbola contains no cross-variable character oscillation at all. The only remaining coupling in `(3)` is the archimedean product boundary.

Equation `(4)` shows that a smooth version of that boundary also does not generate arithmetic coupling. With

\[
\widetilde V(s)=\int_0^\infty V(x)x^{s-1}\,dx,
\]

Mellin inversion gives

\[
V(uvm/N)
=\frac{1}{2\pi i}\int_{(c)}
\widetilde V(s)N^s(uvm)^{-s}\,ds.
\]

Because `alpha,beta` have finite support and `L(s,chi)` converges absolutely for `c>1`, sums and integral may be interchanged, proving `(4)` without analytic continuation or a zero-free hypothesis.

The sharp cutoff in `(3)` is still an exact summatory Dirichlet convolution by `(2)`. Smoothing is used only to expose the multiplicative diagonalization transparently; no claim depends on moving the Mellin contour.

## 3. What Cauchy can and cannot gain before new geometry appears

Suppose one opens `(3)` in the `u` variable:

\[
S_\chi(N)=\sum_u\alpha_u\chi(u)H_u,
\qquad
H_u:=\sum_{vm\le N/u}\beta_v\chi(vm).
\tag{7}
\]

A direct Cauchy step in `u` removes the scalar phase `chi(u)`:

\[
|S_\chi(N)|^2
\le
\left(\sum_u|\alpha_u|^2\right)
\left(\sum_u|H_u|^2\right).
\tag{8}
\]

The same occurs if `v` is the outer factor. Therefore factorability does not automatically alter the Cauchy diagonal in the way the retained arithmetic variable does in Stadlmann's modified `q`-van der Corput argument. To obtain a new diagonal/off-diagonal geometry, one must first arrange that the inner object depends arithmetically on the outer variable—not merely through the scalar factor `chi(u)` and the endpoint `N/u`.

This is exactly the distinction between the current form and the well-factorable prime-distribution theorems cited in `MC-409`. In Maynard's theorem, the factorable coefficient weights a **progression modulus** inside a prime-distribution error. Dispersion and subsequent transformations act on that congruence geometry. The theorem is not a bound for a bare product phase `chi(uv)`; importing its gain into `(3)` requires first exhibiting the corresponding nonseparable arithmetic relation.

## 4. Consequence for candidate bilinear estimates

A proposed estimate for `MC-409` now has a sharper admission test.

It is not enough to say that `(u,v)` are two variables and invoke a generic bilinear-character-sum heuristic. For a fixed source character, the raw phase `chi(uv)` equals `chi(u)chi(v)`, so any theorem whose only oscillatory input is that phase reduces to one-dimensional character information after localization.

A legitimate surviving route must identify the first step at which this separability is broken or augmented. Examples include:

- a dispersion identity that compares two different products and leaves a genuine congruence between factor variables;
- Poisson/completion producing reciprocal or Kloosterman-type phases;
- a family average whose covariance couples source character and factor variables in a way not already collapsed by `MC-397`;
- a translated multiplicative-character phase such as `chi(uv+a)` generated intrinsically by the argument;
- another arithmetic constraint whose post-Cauchy diagonal count is strictly smaller than the one obtained from the collapsed coefficient sequence.

The resulting transformed form must then be checked against the actual source modulus, support lengths, common-radical cost, and source-depth bookkeeping. If the proof never produces such a relation, the well-factorable decomposition is a useful coefficient normal form but not a new cancellation mechanism.

## Prior art and novelty boundary

No novelty is claimed for `(1)`, Dirichlet convolution, complete multiplicativity of Dirichlet characters, or the product rule for Dirichlet series. These are classical; a standard reference is Tom M. Apostol, *Introduction to Analytic Number Theory* (Springer, 1976), especially Chapter 2 on Dirichlet multiplication, Chapter 6 on characters, and §11.4 on multiplication of Dirichlet series. Apostol's Theorem 11.5 identifies multiplication of absolutely convergent Dirichlet series with Dirichlet convolution.

The well-factorable comparison remains the literature boundary already audited in `MC-409`: Iwaniec's factorable linear-sieve weights and Maynard's well-factorable prime-distribution theorem exploit coefficient factorization in a modulus/progression problem. Maynard's main result averages prime-distribution errors over moduli with well-factorable weights; it does not estimate the fixed-source product-character form `(3)`.

A targeted literature check also confirms the expected distinction in the terminology of bilinear multiplicative-character sums: nontrivial double-character estimates are attached to genuinely nonseparable phases such as `chi(ab+lambda)`, whereas `chi(ab)` factorizes identically. The present finding is therefore a Mathia frontier classification of `MC-409`, not a new theorem about character sums.

## Boundaries and falsification tests

- **Factorability is not declared useless.** The support, boundedness, and flexible convolution scales of `alpha,beta` may enable a Type I/II, dispersion, or family estimate after a suitable transformation. The finding rules out only a gain attributed to the raw multiplicative source phase.
- **Mellin separation is not a bound.** Equation `(4)` is an exact representation on `Re(s)>1`; taking absolute values there may be far too costly. It is used to classify coupling, not to estimate `S_chi`.
- **No contour shift is used.** The argument does not assume analytic continuation, a zero-free region, RH, or any bound for `L(s,chi)` in the critical strip.
- **Source-family structure remains a separate possibility.** `MC-397` classifies naive source-mode averaging as a signature projector, but a transformed hybrid family estimate could still be new information. This finding does not rule out such a theorem.
- **The sharp hyperbola remains potentially useful.** Its endpoint variation may be exploited by a method that creates arithmetic coupling. The claim is only that the product cutoff itself is archimedean and becomes scalar under Mellin transform.
- **Finite linear combinations are covered termwise.** Iwaniec's upper-sieve coefficient may be represented as a bounded finite linear combination of well-factorable components; the separability statement applies to each component and hence to their sum.

## Consequence for the research line

`MC-409` correctly opens a representation outside the quadratic Selberg/lcm bottleneck. The present finding identifies its first exact obstruction: **coefficient factorization survives, but source-phase entanglement does not**.

The next useful step is therefore not to seek a generic bilinear bound for `chi(uv)`. It is to perform one concrete dispersion/Poisson/family transformation on the actual factorable upper-sieve form and write the resulting kernel before estimating it. The route advances only if that transformed kernel contains a genuinely nonseparable arithmetic variable and the resulting diagonal/off-diagonal accounting beats the existing modewise source-depth cost.