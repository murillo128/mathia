---
id: WP-378
title: Cyclotomic Hardy positivity factorizes primewise while the Mangoldt selector is an unbounded boundary trace
branch: weil_positivity
status: supported
kind: prime-circle-cyclotomic-hardy-gram-boundary-trace-obstruction
claim_strength: exact RH-independent classification of the canonical Hardy H2 pairing of Prime-Circle cyclotomic logarithmic potentials; its positive Gram kernel has an explicit Euler-factorized Ramanujan-sum formula with full composite support and prime-power diagonal energy independent of the exponent, while the exact Mangoldt selector occurs only as boundary evaluation at z=1, which is unbounded in H2 even on the shell family
created: 2026-09-19
related: [WP-155, WP-157, WP-158, WP-161, WP-162, WP-374, WP-377]
clues: [CLUE-weil-positivity-noncharacter-finite-archimedean-incidence]
prior_art:
  - Ramanujan 1918, On certain trigonometrical sums and their applications in the theory of numbers
  - C. A. Nicol 1962, Some Formulas Involving Ramanujan Sums, Canadian Journal of Mathematics 14, 284-286
  - standard Hardy H2 coefficient norm and reproducing-kernel evaluation on the unit disk
  - classical cyclotomic identity Phi_n(1)=p for n a prime power and 1 otherwise
---

# WP-378 — Cyclotomic Hardy positivity factorizes primewise while the Mangoldt selector is an unbounded boundary trace

## Claim

Prime Circle has a canonical genuinely two-dimensional positive Hilbert geometry that had not been tested in the `WP-161`--`WP-377` radial chain: put the primitive-shell logarithmic potential itself in the Hardy space of the unit disk.

For `n>1`, let

\[
F_n(z):=\log\Phi_n(z),\qquad |z|<1,
\]

with the unique analytic branch satisfying `F_n(0)=0`. Then `F_n\in H^2(\mathbb D)`, and the intrinsic Hardy Gram form

\[
K(m,n):=\langle F_m,F_n\rangle_{H^2}
\]

is positive semidefinite by construction. It is not empty: different prime shells have nonzero cross terms. Nevertheless it does **not** create the missing irreducible finite-prime incidence or a Weil finite term.

Writing `a=v_p(m)` and `b=v_p(n)`, one has the exact Euler factorization

\[
\boxed{
K(m,n)=\zeta(2)\prod_p L_p(a,b),
}
\tag{1}
\]

where all but finitely many factors are `1` and

\[
L_p(a,b)=
\begin{cases}
1,&a=b=0,\\
-(p-1)p^{-a},&a>0,\ b=0,\\
-(p-1)p^{-b},&a=0,\ b>0,\\
2(p-1)/p,&a=b>0,\\
-(p-1)^2p^{-|a-b|-1},&a,b>0,\ a\ne b.
\end{cases}
\tag{2}
\]

In particular,

\[
\boxed{
\|F_n\|_{H^2}^2
=\zeta(2)\prod_{p\mid n}2\left(1-\frac1p\right),
}
\tag{3}
\]

so the positive diagonal energy depends only on `rad(n)`, not on the prime-power exponents. For every `a>=1`,

\[
\|F_{p^a}\|_{H^2}^2
=2\zeta(2)\left(1-\frac1p\right),
\tag{4}
\]

whereas the finite Weil coefficient at critical half-density is proportional to

\[
\frac{\Lambda(p^a)}{\sqrt{p^a}}
=\frac{\log p}{p^{a/2}}.
\tag{5}
\]

Even after the natural shell scaling `F_n\mapsto n^{-1/4}F_n`, the Hardy diagonal gives

\[
\frac{\zeta(2)}{\sqrt n}
\prod_{p\mid n}2\left(1-\frac1p\right),
\tag{6}
\]

with the wrong support and no `log p`. The smallest exact mixed-prime control is already decisive:

\[
\Lambda(6)=0,
\qquad
\|F_6\|_{H^2}^2=\frac43\zeta(2)>0.
\tag{7}
\]

The exact Mangoldt selector is present in the same analytic family, but at a different topological level:

\[
\boxed{
\lim_{r\uparrow1}F_n(r)
=\log\Phi_n(1)
=\Lambda(n).
}
\tag{8}
\]

Boundary evaluation at `1` is not a bounded functional on `H^2`. More sharply, it is already unbounded on the cyclotomic shell family itself, because (4) is uniformly bounded in `p` while

\[
F_{p^a}(1)=\log p\to\infty.
\tag{9}
\]

Thus the canonical positive interior Hardy geometry and the exact Mangoldt boundary selector do not coexist as one bounded positive Hilbert readout. The positive Gram form is Euler-factorized and full-support; the arithmetic selector survives only as a singular boundary trace.

**Classification:** `EXACT-DERIVED + RH-INDEPENDENT + PRIME-CIRCLE-INTRINSIC + HARDY-H2-POSITIVE-GRAM + RAMANUJAN-COEFFICIENTS + EXACT-EULER-FACTORIZATION + NONZERO-CROSS-PRIME-GRAM + RADICAL-ONLY-DIAGONAL + FULL-COMPOSITE-SUPPORT + UNBOUNDED-MANGOLDT-BOUNDARY-TRACE + MATCHED-N6-CONTROL + CLASSICAL-INGREDIENTS + NO-ZERO-DATA + NOT-A-GLOBAL-WEIL-POSITIVITY-PROOF`.

## 1. The cyclotomic logarithms are canonical Hardy vectors

For `n>1`, `Phi_n` has no zero in the open unit disk and `Phi_n(0)=1`, so `F_n=log Phi_n` has a canonical analytic branch there. The cyclotomic product formula gives

\[
\Phi_n(z)=\prod_{d\mid n}(1-z^d)^{\mu(n/d)}.
\tag{10}
\]

Expanding the logarithm for `|z|<1`,

\[
F_n(z)
=-\sum_{k\ge1}\frac{c_n(k)}{k}z^k,
\tag{11}
\]

where

\[
c_n(k)=\sum_{d\mid(n,k)}d\,\mu(n/d)
\tag{12}
\]

is the classical Ramanujan sum. Since `|c_n(k)|<=phi(n)` for fixed `n`,

\[
\sum_{k\ge1}\frac{|c_n(k)|^2}{k^2}<\infty,
\]

so `F_n\in H^2(D)` exactly, with no regularization.

This is source-native Prime-Circle geometry: the vector is the analytic logarithmic potential of the primitive root layer itself, and the positive form is the standard Hilbert norm of analytic functions on the same disk. No zeta zeros, test kernel, or prime-dependent weighting has been inserted.

## 2. The positive Gram kernel has an exact primewise factorization

Parseval applied to (11) gives

\[
K(m,n)
=\sum_{k\ge1}\frac{c_m(k)c_n(k)}{k^2}.
\tag{13}
\]

Insert (12) twice. Absolute convergence permits rearrangement:

\[
\begin{aligned}
K(m,n)
&=\sum_{d\mid m}\sum_{e\mid n}
 d e\,\mu(m/d)\mu(n/e)
 \sum_{\operatorname{lcm}(d,e)\mid k}\frac1{k^2}\\
&=\zeta(2)
\sum_{d\mid m}\sum_{e\mid n}
\mu(m/d)\mu(n/e)
\frac{\gcd(d,e)^2}{de}.
\end{aligned}
\tag{14}
\]

The finite divisor sum is multiplicative in the pair `(m,n)`, which yields (1). Because each Mobius factor restricts a local divisor exponent to `a` or `a-1` (and similarly for `b`), the four local terms evaluate directly to (2).

This also gives a useful adversarial control. For distinct primes `p!=q`,

\[
K(p,q)
=\zeta(2)\frac{(p-1)(q-1)}{pq}>0.
\tag{15}
\]

So the Hardy pairing really does see two different prime shells simultaneously; the negative conclusion is not caused by orthogonality or by throwing away the interaction. The problem is stronger: the interaction itself is an Euler product of independent local factors. It is therefore a positive multiplicative completion of prime-primary data, not the irreducible finite-prime incidence sought by the accepted clue.

Taking `m=n` in (2) proves (3). The disappearance of every exponent `v_p(n)` from the diagonal is exact.

## 3. The Weil coefficient fails before any archimedean completion

Equation (3) gives positive energy to every `n>1`. It therefore fails the first finite-place support test: mixed shells do not disappear. Equation (4) gives an independent failure on the desired support: even restricted to prime powers, the energy does not know the exponent and has no logarithmic prime factor.

The critical scaling control in (6) prevents a normalization ambiguity from hiding the problem. Multiplying each shell by `n^{-1/4}` supplies the desired `n^{-1/2}` quadratic scale, but the remaining coefficient is still

\[
\zeta(2)\prod_{p\mid n}2(1-p^{-1}),
\]

not `Lambda(n)`. Inserting `sqrt(log p)` by hand on a prime shell would repair one local coefficient only by importing the target arithmetic weight; it is not forced by the Hardy geometry and is excluded by the line mandate.

Nor does (1) contain an archimedean completion in disguise. Its only universal analytic constant is `zeta(2)`, while every dependence on `(m,n)` is the finite Euler product (2). There is no Gamma/digamma or polar counterterm generated by this pairing. Positivity is intrinsic, but it is positivity of the wrong object.

## 4. Mangoldt survives exactly as a singular boundary trace

The classical cyclotomic value at `1` is

\[
\Phi_n(1)=
\begin{cases}
p,&n=p^a,\\
1,&n>1\text{ has at least two distinct prime factors}.
\end{cases}
\tag{16}
\]

Hence (8) is exactly the von Mangoldt selector already seen radially in `WP-161` and as total signed flux in `WP-162`.

The Hardy realization explains a different obstruction. For `0<r<1`, evaluation is bounded and represented by the Szego kernel

\[
k_r(z)=\frac1{1-rz},
\qquad
\|k_r\|_{H^2}^2=\frac1{1-r^2}.
\tag{17}
\]

As `r\uparrow1`, the representing-vector norm diverges. Therefore the limit in (8) does not define a bounded `H^2` functional. Equation (9) proves the same failure without appealing to general Hardy theory: the shell vectors `F_{p^a}` stay in a fixed bounded `H^2` ball while their desired readout tends to infinity.

This blocks the most direct finite--archimedean rescue of the Hardy pairing. A fixed finite-energy background vector `b in H^2` can contribute only the bounded cross term `2 Re <F_n,b>` to a positive square `||F_n+b||^2`; it cannot equal `Lambda(n)` on all prime-power shells. Using `k_r` and sending `r` to `1` restores the selector only while the background energy `||k_r||^2` diverges. Subtracting or renormalizing that divergence would require an additional source-derived theorem; Hardy positivity alone does not supply one, and positivity of the renormalized difference is not automatic.

## 5. Matched controls and scope

A finite shell panel can hide the obstruction. On any finite-dimensional span, the values `F_n(1)` define a bounded linear functional, so one can construct a finite representing vector that reproduces the Mangoldt labels exactly. Such interpolation is not evidence for a global mechanism. The obstruction is the uniform infinite family (9).

The result is also deliberately narrower than a no-go for analytic or two-dimensional geometry. It rules out the **canonical unweighted `H^2` Gram pairing of the cyclotomic logarithmic potentials**, and any attempt to obtain the exact Mangoldt coefficient from a fixed bounded `H^2` background cross term. It does not rule out a source-forced weighted Hardy/Bergman/Dirichlet geometry, an indefinite intermediate pairing, a genuinely finite--archimedean boundary condition, or a construction that keeps mixed shells active until after a different global assembly. Any such variant must derive its weight/domain from Prime Circle rather than choose it to insert `Lambda`.

## 6. Prior-art and novelty audit

The ingredients are classical. Ramanujan introduced the sums `c_n(k)` in 1918, and Nicol's 1962 paper records direct cyclotomic/Ramanujan identities. The coefficient realization of `H^2`, the Szego reproducing kernel, and the unboundedness of boundary evaluation are standard Hardy-space facts. The cyclotomic value (16) is classical.

A bounded literature search for the structural combination used here did not locate a source presenting the exact pairwise kernel (1)--(2) as a Weil-positivity mechanism. No novelty claim is made for the underlying identities: (1)--(2) are an elementary consequence of classical Ramanujan-sum formulas and Parseval. The Mathia-specific contribution is the falsification result: the first canonical non-radial positive Hilbert pairing of the Prime-Circle logarithmic potentials has genuine cross-prime terms but still factorizes primewise, loses prime-power exponent information on the diagonal, and separates positivity from the singular boundary operation that recovers `Lambda`.

This is distinct from classical Weil positivity, Frobenius/cohomology, Hilbert--Polya, Connes/trace, Sonin/localization, and intersection-form programs: it supplies none of their global sign theorems or zero data. It is a negative classification of one Mathia-native candidate, not an alternative proof of their criteria.

## Consequence for the research line

The accepted non-character-incidence clue can now discard one natural two-dimensional escape from the radial no-go chain. Passing from the radial profile to the full analytic cyclotomic potential and using its canonical Hardy positivity does create nonzero cross-prime Gram coefficients, but those coefficients are still completely primewise after Euler factorization. More importantly, the exact `Lambda` selector sits at the singular boundary of that positive topology.

A surviving analytic-disk route must therefore explain, from the source geometry itself, why a different positive topology has a bounded boundary object with the linear Weil coefficient **and** how the same construction produces the archimedean/polar terms. Merely replacing the radial `L^2` norm by the canonical interior `H^2` norm does not do it.