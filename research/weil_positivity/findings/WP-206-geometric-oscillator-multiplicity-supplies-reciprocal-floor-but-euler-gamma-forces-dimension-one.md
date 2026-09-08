# WP-206 — Geometric oscillator multiplicity supplies the reciprocal floor, but exact Euler-Gamma divisor forces dimension one

**Status:** `DERIVED + EXACT + ARCHIMEDEAN-GAMMA + BARNES-MULTIPLE-ZETA + POSITIVE-ROUGH-BATH + RECIPROCAL-FLOOR + DIVISOR-RIGIDITY + SIGNED-CANCELLATION-BOUNDARY + MATCHED-CONTROL + PRIOR-ART-AUDITED + DECISIVE-NARROWING + NOT-A-WEIL-BRIDGE`.

`WP-205` leaves a very specific source-forcing problem. At every allowed higher spectral-shift order `n=4k`, identical fractional Gamma channels can supply the `WP-202` reciprocal Fourier floor only at

\[
M=n-1,
\qquad
s=\frac1{n-1},
\]

but neither the Gamma determinant nor the extension theorem selects `n` or explains why the critical roughness should be implemented by `n-1` copies of a fractional channel.

There is a natural way to remove that artificial-looking multiplicity: replace one one-dimensional number operator by a `d`-mode additive number operator. Its spectral multiplicities automatically create the same critical roughness with an **ordinary inverse**, with no fractional functional calculus. For `d=n-1`, the resulting positive compact bath lies in `S^n\setminus S^{n-1}` and has the uniform reciprocal Fourier floor required by `WP-202`.

That escape is real analytically but fails the exact Riemann archimedean normalization. The determinant of the `d`-mode operator is governed by the equal-period Barnes multiple zeta/gamma hierarchy. Its singularity at the `m`th Gamma lattice point has multiplicity

\[
g_d(m)=\binom{m+d-1}{d-1}.
\]

A finite **positive** direct sum of such determinant channels can equal the Euler-Gamma relative determinant only if every channel has `d=1`; higher-dimensional multiplicities cannot cancel because all determinant exponents are nonnegative. The classical Barnes finite-difference recurrence does reduce dimension back to Euler Gamma, but it does so by ratios/alternating differences, i.e. by a signed virtual determinant rather than a positive direct sum.

Thus geometric dimension can source-force the missing reciprocal-floor roughness, or a positive determinant architecture can retain the exact Euler Gamma divisor, but this Barnes class cannot do both at once:

\[
\boxed{
\text{dimension-forced critical roughness}
\quad\Longrightarrow\quad
\text{Barnes multiplicity},
\qquad
\text{exact Euler-Gamma divisor + positive determinant weights}
\quad\Longrightarrow\quad
 d=1.
}
\]

This does not rule out a genuinely cohomological construction in which an intrinsic grading supplies the necessary alternating Barnes cancellation and a separate Hodge/intersection theorem controls the final sign. It does rule out treating higher oscillator dimension itself as the missing positive archimedean completion of `WP-205`.

## 1. The `d`-mode Gamma source is the equal-period Barnes zeta operator

Let `N_1,...,N_d` be commuting copies of the nonnegative number operator and define

\[
N^{(d)}=N_1+\cdots+N_d,
\qquad
L_{d,q}=\frac{N^{(d)}+q}{\pi},
\qquad \Re q>0.
\tag{1}
\]

The eigenspace of `N^{(d)}` with eigenvalue `m` is indexed by weak compositions

\[
\alpha_1+\cdots+\alpha_d=m,
\qquad \alpha_j\in\mathbb N_0,
\]

so its multiplicity is exactly

\[
\boxed{
 g_d(m)=\binom{m+d-1}{d-1}.
}
\tag{2}
\]

Hence, initially for `Re w>d`,

\[
\begin{aligned}
\zeta_{L_{d,q}}(w)
&=\operatorname{Tr}(L_{d,q}^{-w})\\
&=\pi^w\sum_{m=0}^{\infty}g_d(m)(m+q)^{-w}\\
&=\pi^w\zeta_d(w,q),
\end{aligned}
\tag{3}
\]

where `zeta_d` is the equal-period Barnes multiple zeta function. For `d=1`, `g_1(m)=1` and (3) is exactly the Hurwitz-zeta source used in `WP-203`.

Thus increasing the oscillator dimension is not a new Gamma representation in disguise: it moves canonically from the Euler/Hurwitz level to the Barnes multiple-gamma hierarchy.

## 2. Dimension alone produces the critical Schatten roughness

Fix `a>0` and use the ordinary positive inverse

\[
V_{d,a}=L_{d,a}^{-1}\succeq0.
\tag{4}
\]

Its nonzero singular values are

\[
\frac{\pi}{m+a}
\quad\text{with multiplicity }g_d(m).
\tag{5}
\]

For any `r>0`,

\[
\operatorname{Tr}(V_{d,a}^r)
=\pi^r\sum_{m=0}^{\infty}
\frac{g_d(m)}{(m+a)^r}.
\tag{6}
\]

Since

\[
g_d(m)\sim\frac{m^{d-1}}{(d-1)!},
\tag{7}
\]

the series in (6) converges exactly when

\[
\boxed{r>d.}
\tag{8}
\]

Now fix an allowed Weil-cone spectral-shift order

\[
n=4k\ge4
\tag{9}
\]

and choose

\[
\boxed{d=n-1.}
\tag{10}
\]

Then

\[
\boxed{
V_{n-1,a}\in\mathcal S^n
\setminus\mathcal S^{n-1}.
}
\tag{11}
\]

This is exactly the critical Schatten boundary that `WP-205` obtained from `n-1` identical one-dimensional fractional channels with exponent `1/(n-1)`, but here it comes from one additive `n-1`-mode source and the ordinary inverse power `s=1`.

The mechanism is transparent: ordering all eigenvalues with multiplicity gives an effective singular-value decay `j^{-1/d}`. Geometric degeneracy replaces the fractional exponent.

## 3. The same dimension also supplies the `WP-202` reciprocal Fourier floor

Let `F_b` denote the centered scalar order-`n` multiplier from `WP-202`,

\[
F_b(\xi)
=
\frac1{(n-3)!\,\xi^2}
\int_0^b
(1-\cos(t\xi))(b-t)^{n-3}\,dt.
\tag{12}
\]

For the bath (4), direct-sum additivity gives

\[
F_{d,a}(\xi)
=
\sum_{m=0}^{\infty}
 g_d(m)
 F_{\pi/(m+a)}(\xi).
\tag{13}
\]

Take `|xi|` large. If

\[
m+a\ge\pi|\xi|,
\tag{14}
\]

then `b=pi/(m+a)` satisfies `b|xi|<=1`. On `|u|<=1`,

\[
1-\cos u\ge\frac{u^2}{4}.
\tag{15}
\]

Substituting (15) into (12) and evaluating the beta integral gives

\[
F_b(\xi)
\ge
\frac{b^n}{2n!}
\qquad
(b|\xi|\le1).
\tag{16}
\]

Therefore, with `d=n-1`,

\[
F_{n-1,a}(\xi)
\ge
\frac{\pi^n}{2n!}
\sum_{m+a\ge\pi|\xi|}
\frac{g_{n-1}(m)}{(m+a)^n}.
\tag{17}
\]

For large `m`,

\[
g_{n-1}(m)
=\binom{m+n-2}{n-2}
\ge\frac{m^{n-2}}{(n-2)!},
\tag{18}
\]

and `(m+a)^n` differs from `m^n` only by a fixed multiplicative constant. The tail in (17) therefore dominates a positive multiple of

\[
\sum_{m\ge C|\xi|}\frac1{m^2}
\asymp\frac1{|\xi|}.
\tag{19}
\]

Consequently

\[
\boxed{
\liminf_{|\xi|\to\infty}
|\xi|F_{n-1,a}(\xi)>0.
}
\tag{20}
\]

By `WP-202`, the single higher-dimensional ordinary-inverse bath is therefore a universal centered-bath stabilizer for finite positive payloads at order `n` after finite amplification.

This is a genuine improvement in source forcing relative to `WP-205`: the critical roughness no longer has to be chosen as a fractional exponent. It is forced by an integer geometric multiplicity `d=n-1`.

It is also a matched-control warning. Equations (1)--(20) hold for every `a>0` and contain no primes, Mangoldt selector, pole term, or zeta-zero data.

## 4. Exact Euler Gamma sees the Barnes multiplicity and forces `d=1`

The obstruction is already visible at the divisor level, before any asymptotic normalization is considered.

For `d=1`, `WP-203` proves

\[
\frac{\det_\zeta L_{1,a}}
     {\det_\zeta L_{1,a+z}}
=
\pi^{-z}\frac{\Gamma(a+z)}{\Gamma(a)}.
\tag{21}
\]

The right-hand side has one simple Gamma pole at each

\[
z=-a-m,
\qquad m=0,1,2,\ldots.
\tag{22}
\]

For general `d`, the zeta determinant of `L_{d,q}` is a Barnes multiple-gamma determinant. At `q=-m`, exactly the level-`m` eigenspace of (1) vanishes, with multiplicity `g_d(m)`. Equivalently, the regularized determinant has a zero of order `g_d(m)` there, while the inverse relative determinant has local logarithmic pole coefficient

\[
\boxed{g_d(m).}
\tag{23}
\]

The scale by `pi` and any zeta-regularization normalization can multiply the determinant by an entire nonvanishing elementary factor, but cannot change these local multiplicities.

Now take any finite positive direct sum of common-anchor Barnes channels with positive determinant exponents

\[
\mathcal D(z)
=
\prod_{r=1}^R
\left(
\frac{\det_\zeta L_{d_r,a}}
     {\det_\zeta L_{d_r,a+z}}
\right)^{\beta_r},
\qquad
\beta_r>0.
\tag{24}
\]

Fractional powers are included because

\[
\log\det_\zeta(L^{\beta_r})
=\beta_r\log\det_\zeta L.
\tag{25}
\]

At the lattice point (22), the local logarithmic pole coefficient of (24) is

\[
c_m
=
\sum_{r=1}^R
\beta_r g_{d_r}(m).
\tag{26}
\]

If (24) is to equal the exact Euler-Gamma factor (21), including as a single-valued meromorphic function after the elementary `pi` normalization, then necessarily

\[
\boxed{c_m=1\quad\text{for every }m\ge0.}
\tag{27}
\]

But

\[
g_1(m)=1,
\qquad
 g_d(m)\longrightarrow\infty
\quad(d\ge2).
\tag{28}
\]

All coefficients in (26) are nonnegative. Hence any channel with `d_r>=2` and `beta_r>0` makes `c_m` grow without bound, contradicting (27). Therefore

\[
\boxed{
\mathcal D(z)=\pi^{-z}\frac{\Gamma(a+z)}{\Gamma(a)}
\quad\Longrightarrow\quad
 d_r=1\ \text{for every positive channel},
\qquad
\sum_r\beta_r=1.
}
\tag{29}
\]

The last equality follows from (27) once every `g_{d_r}` is identically one.

This is stronger than merely saying that the higher-dimensional determinant is a different special function. The **simple Euler-Gamma divisor itself** forbids every positive higher-dimensional Barnes contribution.

The same conclusion is stable under the obvious shifted-channel repair. A nonintegral shift creates singularities off the Euler-Gamma lattice. A negative integral shift creates extra singularities before `-a`. A positive integral shift contributes additional nonnegative multiplicity only from some later lattice point onward; matching the first pole already exhausts coefficient one, so no such positive shifted channel can subsequently be added without making a later multiplicity exceed one.

## 5. Barnes finite differences explain exactly why the repair is signed

The equal-period Barnes zeta has the elementary recurrence

\[
\boxed{
\zeta_d(w,q)-\zeta_d(w,q+1)
=\zeta_{d-1}(w,q).
}
\tag{30}
\]

It follows directly by separating one lattice coordinate, and the corresponding multiple-gamma hierarchy is classical. At the level of spectral multiplicities, the same recurrence is just Pascal's identity:

\[
g_d(m)-g_d(m-1)=g_{d-1}(m),
\qquad g_d(-1)=0.
\tag{31}
\]

Iterating `d-1` finite differences reduces the growing polynomial multiplicity to

\[
\Delta^{d-1}g_d(m)=g_1(m)=1.
\tag{32}
\]

So there **is** a canonical algebraic operation that turns the Barnes divisor into the Euler-Gamma divisor. But expanding `Delta^{d-1}` gives alternating binomial coefficients. On determinants it is a product of some shifted determinants divided by others; on logarithms it is an alternating sum.

Therefore the exact classical repair is not a positive direct-sum completion. It is a virtual/superdeterminantal construction:

\[
\boxed{
\text{Barnes dimension}
\xrightarrow{\text{finite differences}}
\text{Euler Gamma}
\quad\text{requires signed cancellation.}
}
\tag{33}
\]

This is precisely the type of category change the Weil-positivity mandate treats cautiously. A genuine cohomological or graded Mathia object could in principle make the alternating structure intrinsic and then obtain a sign from a separate Hodge/intersection theorem. But the positivity would have to be proved for that assembled graded object; it is not inherited from the positive bath (4) or from a positive determinant product.

## 6. Aggressive falsification and exact scope

**Could the Riemann shift `a=1/4` select the dimension?** No. The Schatten threshold (8), reciprocal-floor proof (14)--(20), and Barnes multiplicity (2) hold for every `a>0`. The special Riemann value fixes the Euler-Gamma anchor only after one asks for (21).

**Could dimension select the higher spectral-shift order?** Only conditionally. Requiring the ordinary inverse to sit at the critical Schatten boundary gives `d=n-1`; but every allowed `n=4k` still gives a candidate dimension `d=4k-1`. Thus geometric dimension trades the `WP-205` channel ladder for an equally infinite dimension ladder unless another Mathia structure selects one `d`.

**Could a fractional power of a higher-dimensional source repair the determinant?** No within the positive determinant class. Replacing `L_{d,q}` by `L_{d,q}^s`, `s>0`, multiplies the local coefficient (23) by `s` but leaves its growth in `m`; `s g_d(m)` cannot equal one for all `m` when `d>=2`.

**Could several higher-dimensional channels cancel their multiplicities?** Not with positive determinant exponents. Equation (26) is a positive sum. Cancellation requires negative coefficients, exactly as in the finite-difference recurrence (30)--(33).

**Could zeta regularization hide the divisor multiplicity?** No. Regularization changes global normalization and entire counterterms, not the local order of a determinant zero caused by a finite-dimensional eigenspace crossing zero. The classical Barnes functions exhibit the same multiplicities explicitly; for `d=2`, the Barnes `G` product already has increasing zero multiplicities at the nonpositive integers.

**Does the reciprocal floor prove Weil positivity?** No. `WP-202` classifies a generic stabilization resource. The bath here is independent of finite-prime arithmetic and can stabilize arbitrary finite positive payloads. No finite Mangoldt sector or polar term is generated, and no global finite--archimedean identity has been obtained.

**Does (29) rule out all archimedean geometric completions?** No. It rules out finite positive products/direct sums of additive Barnes number-operator determinant channels as a way to combine dimension-forced roughness with the exact Euler-Gamma divisor. Coupled non-diagonal geometries, graded complexes with an independently proved Hodge sign, non-determinantal boundary responses, or genuinely finite--archimedean constructions remain outside the theorem.

## 7. Prior art and novelty boundary

Barnes multiple zeta and gamma functions are classical. S. N. M. Ruijsenaars, *On Barnes' multiple zeta and gamma functions*, Advances in Mathematics **156** (2000), 107--132, develops the Barnes multiple-zeta/gamma hierarchy and its difference equations. V. S. Adamchik, *Multiple Gamma Function and Its Application to Computation of Series*, arXiv:`math/0308074` (2003), gives the equal-period multiple zeta explicitly as

\[
\zeta_d(w,q)
=\sum_{k_1,\ldots,k_d\ge0}
(q+k_1+\cdots+k_d)^{-w}
\]

and reviews the multiple-gamma recurrence hierarchy. NIST DLMF §5.17 records the first nontrivial case, the Barnes `G` function, with `G(z+1)=Gamma(z)G(z)` and the canonical product whose increasing powers display the growing zero multiplicities.

No novelty is claimed for the Barnes hierarchy, Pascal multiplicities, Schatten summability of polynomially degenerate resolvents, or the finite-difference recurrence. The Mathia-specific result is the conjunction of these classical facts with the exact `WP-202` Fourier-floor criterion and the `WP-203` Euler-Gamma determinant normalization:

1. `d=n-1` geometric multiplicity gives the missing reciprocal floor using an ordinary positive inverse;
2. the exact Euler-Gamma divisor forces every positive Barnes determinant channel back to `d=1`;
3. the only classical route from higher Barnes dimension back to Euler Gamma is alternating finite difference, which forfeits direct positivity inheritance.

A targeted audit found the Barnes multiple-gamma hierarchy and its recurrences but no independent theorem converting the resulting alternating determinant into the zeta Weil positivity form. Search absence is not a novelty claim; any such cohomological conversion would be a category exit from the positive Barnes direct-sum class proved here.

## 8. Consequence for the research line

`WP-205` left open whether its fractional critical bath was an artifact of choosing functional calculus before geometry. `WP-206` answers that question in both directions.

The favorable part is exact: **critical roughness can be forced by integer geometric multiplicity.** One `d=n-1` additive oscillator with its ordinary positive inverse already supplies the same reciprocal-frequency resource.

The unfavorable part is equally exact: **the Riemann Gamma divisor rejects that multiplicity in every positive Barnes determinant assembly.** Exact Euler Gamma collapses the positive determinant source back to dimension one, where the ordinary inverse is too smooth by `WP-203`--`WP-204`. Recovering Euler Gamma from the successful higher-dimensional bath requires an intrinsic alternating/graded operation before any final positivity theorem.

The live frontier is therefore narrower. A successful Mathia geometry must not merely choose a rough archimedean bath; it must explain why the signed operation that reduces a richer archimedean multiplicity to the simple Euler-Gamma divisor is itself part of a global finite--archimedean object with an independent sign theorem. Until such a graded/global bridge is produced, Barnes dimension is a sharp matched control rather than a Weil-positivity mechanism.
