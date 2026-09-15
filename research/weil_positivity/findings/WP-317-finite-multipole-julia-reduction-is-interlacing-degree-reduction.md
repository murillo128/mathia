---
id: WP-317
title: Finite multipole Julia reduction is interlacing degree reduction, not a new positivity mechanism
branch: weil_positivity
status: supported
kind: finite-multipole-julia-interlacing-degree-reduction
claim_strength: exact classification of the canonically normalized regular-node Julia transform of every finite positive atomic scalar Herglotz function with no surviving affine imaginary channel; N positive atoms are removed and replaced by exactly N-1 positive atoms interlacing the original support, so finite clusters are classical rational Herglotz continued-fraction data and repeated regular reductions collapse them to a real constant rather than producing a persistent finite-prime/archimedean sign mechanism
created: 2026-09-15
related: [WP-304, WP-312, WP-315, WP-316]
prior_art:
  - Jim Agler and N. J. Young, Boundary Nevanlinna-Pick interpolation via reduction and augmentation, Mathematische Zeitschrift 268 (2011), 791-817, DOI 10.1007/s00209-010-0696-3, arXiv:0905.4759, for classical Julia-Nevanlinna reduction/augmentation and Pick-class preservation
  - Jonathan Eckhardt, Continued fraction expansions of Herglotz-Nevanlinna functions and generalized indefinite strings of Stieltjes type, Bulletin of the London Mathematical Society 54 (2022), 737-759, DOI 10.1112/blms.12598, for the classical continued-fraction classification of rational Herglotz-Nevanlinna functions
---

# WP-317 — Finite multipole Julia reduction is interlacing degree reduction, not a new positivity mechanism

## Claim

`WP-316` proves that a support-side scalar Julia tangent becomes trivial whenever one focal Mangoldt pole asymptotically dominates the positive boundary derivative. It leaves genuinely multipole local geometry open. The first remaining case is a finite cluster of positive atoms that all survive at comparable scale.

That case is exactly classifiable, and the result is classical rational Herglotz geometry rather than a new arithmetic sign mechanism.

Let

\[
f(z)=c-\sum_{j=1}^{N}\frac{a_j}{z-x_j},
\qquad
x_1<\cdots<x_N,
\qquad
a_j>0,
\qquad c\in\mathbb R,
\tag{1}
\]

and choose any regular real Julia node

\[
t\in\mathbb R\setminus\{x_1,\ldots,x_N\}.
\tag{2}
\]

Put

\[
w=f(t),
\qquad
d=f'(t)=\sum_{j=1}^{N}\frac{a_j}{(t-x_j)^2}>0.
\tag{3}
\]

Use the same normalized scalar Julia response as in `WP-312` and `WP-316`,

\[
\mathcal J_t[f](z)
=
\frac{d(z-t)(f(z)-w)}{d(z-t)-(f(z)-w)}+\beta,
\qquad \beta\in\mathbb R.
\tag{4}
\]

Define

\[
Q_t(z):=
\sum_{j=1}^{N}
\frac{a_j}{(t-x_j)(z-x_j)},
\qquad
R_t(z):=
\sum_{j=1}^{N}
\frac{a_j}{(t-x_j)^2(z-x_j)}.
\tag{5}
\]

Then the transform has the exact rational normal form

\[
\boxed{
\mathcal J_t[f](z)-\beta
=d\,\frac{Q_t(z)}{R_t(z)}.
}
\tag{6}
\]

Every original pole `x_j` is removable in (6). If `N>=2`, the denominator `R_t` has exactly one simple real zero

\[
y_k\in(x_k,x_{k+1}),
\qquad k=1,\ldots,N-1,
\tag{7}
\]

and no other real zeros. At each such zero,

\[
Q_t(y_k)=d,
\tag{8}
\]

so

\[
\operatorname*{Res}_{z=y_k}
\mathcal J_t[f](z)
=
\frac{d^2}{R_t'(y_k)}<0.
\tag{9}
\]

Consequently there is a real constant `c_t` such that

\[
\boxed{
\mathcal J_t[f](z)
=c_t-
\sum_{k=1}^{N-1}\frac{A_k}{z-y_k},
\qquad
A_k:=
\frac{d^2}
{\displaystyle\sum_{j=1}^{N}
\frac{a_j}{(t-x_j)^2(y_k-x_j)^2}}
>0.
}
\tag{10}
\]

Thus a regular scalar Julia step sends an `N`-atom positive Herglotz function to an `(N-1)`-atom positive Herglotz function. The new support strictly interlaces the old support. It does **not** preserve the original prime-power poles as a finite arithmetic carrier; it replaces them by gap poles whose positivity is forced for every positive atomic input.

Iterating regular reductions therefore gives the exact finite chain

\[
N\ \text{atoms}
\longrightarrow N-1
\longrightarrow\cdots\longrightarrow1
\longrightarrow0,
\tag{11}
\]

where the last one-pole step is the constant collapse already obtained in `WP-316`. Reversing the process is precisely classical Julia augmentation/continued-fraction reconstruction, so keeping the node/augmentation data merely recodes the original finite rational Herglotz function.

For the `weil_positivity` program this closes only the **bounded finite-multipole scalar Julia sign mechanism**. It does not rule out a support-side tangent with unbounded/infinite local multiplicity, a surviving continuous background, a matrix/operator-valued boundary response, or a genuinely nonseparable finite--archimedean construction. Combined with `WP-315`, however, it sharpens the remaining scalar route: prime clustering can force increasing local multiplicity, and any route that remains within classical scalar Julia geometry must exploit that genuinely unbounded collective limit rather than a fixed finite cluster.

**Classification:** `EXACT-DERIVED + CLASSICAL-RATIONAL-HERGLOTZ + NEGATIVE/OBSTRUCTION + SUPPORT-SIDE-JULIA + FINITE-MULTIPOLE + INTERLACING-POLE-RELOCATION + DEGREE-REDUCTION + POSITIVE-ATOMIC-MATCHED-CONTROL + NOT-WEIL-POSITIVITY`.

## 1. Exact reduction to a quotient of two Cauchy transforms

From (1),

\[
\begin{aligned}
f(z)-f(t)
&=-\sum_j a_j
\left(\frac1{z-x_j}-\frac1{t-x_j}\right)\\
&=(z-t)
\sum_j\frac{a_j}{(t-x_j)(z-x_j)}\\
&=(z-t)Q_t(z).
\end{aligned}
\tag{12}
\]

Also

\[
\begin{aligned}
d-Q_t(z)
&=\sum_j a_j
\left(
\frac1{(t-x_j)^2}
-
\frac1{(t-x_j)(z-x_j)}
\right)\\
&=(z-t)
\sum_j\frac{a_j}{(t-x_j)^2(z-x_j)}\\
&=(z-t)R_t(z).
\end{aligned}
\tag{13}
\]

Substituting (12)-(13) into (4), the two factors `(z-t)^2` cancel and give (6). This cancellation is exact; no asymptotic or prime-distribution input is involved.

Near an original pole `x_j`, the singular terms in `Q_t` and `R_t` have ratio

\[
\frac{a_j/(t-x_j)}{a_j/(t-x_j)^2}
=t-x_j,
\tag{14}
\]

so every `x_j` is removable and

\[
\mathcal J_t[f](x_j)-\beta=d(t-x_j).
\tag{15}
\]

The Julia step therefore does not retain any original atom as a pole.

## 2. Positivity forces exact interlacing

Set

\[
b_j:=\frac{a_j}{(t-x_j)^2}>0.
\tag{16}
\]

Then

\[
R_t(z)=\sum_j\frac{b_j}{z-x_j}.
\tag{17}
\]

For real `x` away from the poles,

\[
R_t'(x)
=-\sum_j\frac{b_j}{(x-x_j)^2}<0.
\tag{18}
\]

On each interval `(x_k,x_{k+1})`, `R_t(x)` decreases continuously from `+infinity` to `-infinity`. Hence it has exactly one simple zero `y_k` there. For `x<x_1`, every denominator in (17) is negative, so `R_t(x)<0`; for `x>x_N`, every denominator is positive, so `R_t(x)>0`. Therefore there are no exterior zeros. This proves (7).

The numerator is tied to the same positive weights:

\[
\begin{aligned}
Q_t(z)
&=\sum_j\frac{b_j(t-x_j)}{z-x_j}\\
&=(t-z)R_t(z)+\sum_j b_j\\
&=(t-z)R_t(z)+d.
\end{aligned}
\tag{19}
\]

At a zero `y_k` of `R_t`, equation (19) gives `Q_t(y_k)=d`. Since `R_t'(y_k)<0`, equations (6) and (19) give the negative residue (9), hence the positive atomic mass in (10).

This is the entire sign theorem for the finite cluster: positivity of the input residues makes `R_t` a strictly decreasing real Cauchy transform, and the Julia output inherits positive residues at the interlacing zeros. No property specific to primes, prime powers, the Mangoldt weights, or the Gamma factor enters.

## 3. The two-pole case is already the decisive matched control

For `N=2`, let

\[
b_i=\frac{a_i}{(t-x_i)^2}.
\tag{20}
\]

There is one output pole,

\[
\boxed{
y=
\frac{b_1x_2+b_2x_1}{b_1+b_2}
\in(x_1,x_2),}
\tag{21}
\]

with mass

\[
\boxed{
A=
\frac{b_1b_2}{b_1+b_2}(x_2-x_1)^2>0.
}
\tag{22}
\]

Nothing arithmetic remains in the mechanism. Arbitrary positive locations and arbitrary positive residues obey the same formulas. Replacing a two-prime local chart by a synthetic two-atom Herglotz control changes only the numerical values of `y` and `A`, not the positivity theorem or the degree drop.

The same matched-control statement holds for every fixed `N`: the interlacing pattern and signs depend only on positivity of the atomic measure. Therefore finite-multipole Julia positivity cannot by itself be the independent arithmetic/geometric theorem sought by the line mandate.

## 4. Finite clusters are continued-fraction data, not a persistent completion

Classical Julia--Nevanlinna reduction and augmentation preserve the Pick class. Independently, rational Herglotz--Nevanlinna functions admit finite continued-fraction descriptions with positive coefficients. Equations (6)-(10) identify the exact specialization relevant here: one regular Julia step lowers the positive atomic degree by one, while augmentation restores the removed degree together with the boundary-node data.

Accordingly, the finite chain (11) is not a new cohomology, intersection form, or global positivity theorem. If all reduction/augmentation parameters are retained, the construction is reversible classical encoding of the original rational function. If they are discarded, the original prime-power support is progressively lost. Neither branch generates the missing archimedean Gamma contribution or global counterterms.

The novelty claim is therefore deliberately narrow. The interlacing/continued-fraction phenomenon is classical function theory. The Mathia-specific result is the **obstruction it imposes on the live support-side escape after `WP-315`--`WP-316`**: a bounded finite multipole cluster does not evade the scalar Julia closure merely because more than one Mangoldt atom survives.

## 5. Boundary of the obstruction

The proof uses a finite pure atomic Herglotz tangent with no surviving affine imaginary channel or continuous measure at the local scale. It therefore does not cover a limit in which the number of relevant atoms tends to infinity, an absolutely/singular-continuous component survives, or an affine Herglotz term remains order one. Those are genuine category changes because the rational degree argument no longer terminates.

It also does not rule out using a finite cluster as input to some **different** non-Julia, non-scalar global construction. The conclusion is only that classical scalar Julia positivity on such a cluster is generic interlacing degree reduction, not an independently source-specific Weil sign mechanism.

This boundary matters because `WP-315` supplies exactly the phenomenon capable of leaving the finite-degree regime: bounded prime clusters of arbitrarily large cardinality collapse under the canonical Mangoldt atom-mass scale. A remaining scalar support-side program must therefore control an unbounded/infinite collective positive measure and show that its limiting geometry is both locally compact enough to exist and source-specific enough to distinguish the Gamma target. Otherwise the route must leave scalar Julia geometry altogether.

## Prior-art and novelty audit

Agler--Young supplies the classical boundary Julia--Nevanlinna reduction/augmentation framework and Pick-class preservation already used by `WP-312` and `WP-316`. Eckhardt's continued-fraction work makes explicit that rational Herglotz--Nevanlinna functions belong to a classical finite continued-fraction category with positive coefficients. The exact quotient (6), interlacing zeros (7), and residue formula (10) are derived directly here as the specialization to a finite positive atomic tangent.

No novelty is claimed for rational Herglotz interlacing or continued fractions. The durable contribution is the line-specific closure: **fixed finite multipole support is not the missing escape from isolated-pole trivialization**. Any surviving scalar Julia route must use an unbounded/infinite collective limit (or another non-rational component) before positivity is interpreted arithmetically.

## Consequence for the research line

The support-side scalar frontier is now sharper:

\[
\text{one asymptotically isolated pole}
\Rightarrow\text{constant Julia tangent},
\tag{23}
\]

by `WP-316`, while

\[
\text{fixed finite multipole tangent}
\Rightarrow\text{finite interlacing degree reduction}
\Rightarrow\text{constant after finitely many Julia steps}.
\tag{24}
\]

Thus “make the local chart multipole” is insufficient unless the collectivity itself grows without bound or leaves the pure finite-atomic scalar category. The next scalar question is not another fixed `N` cluster computation; it is whether the reflected Mangoldt source forces a canonical **infinite collective** support-side tangent whose positivity survives matched positive-measure controls and whose same structure can generate the archimedean/global terms required by Weil positivity.