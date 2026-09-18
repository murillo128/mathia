# PL-357 — Complete multiplicativity collapses the Bohr `H^2` family to reproducing kernels

**Evidence:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE`.

**Parent finding:** `PL-356`.

`PL-356` leaves genuinely infinite nonlinear relations, including cross-degree/Euler-product compatibility, as one plausible way to restore arithmetic rigidity after finite linear repairs fail. The most canonical exact version of that proposal is complete multiplicativity. In the standard Hardy space of Dirichlet series it is not an intermediate family: it collapses exactly to the reproducing-kernel family and is automatically zero-free everywhere that `\mathscr H^2` can evaluate it.

Let

\[
F(s)=\sum_{n\ge1} a_n n^{-s}\in\mathscr H^2,
\qquad
\sum_{n\ge1}|a_n|^2<\infty,
\tag{1}
\]

with `a_1=1` and

\[
a_{mn}=a_ma_n\qquad(m,n\ge1).
\tag{2}
\]

Write `\alpha_p=a_p`. Then

\[
a_n=\prod_p \alpha_p^{v_p(n)}.
\tag{3}
\]

The exact conclusions are:

\[
\boxed{
\mathcal BF(z)
=
\prod_p(1-\alpha_p z_p)^{-1}
=
K_{\bar\alpha}(z),
}
\tag{4}
\]

where `K_{\bar\alpha}` is the standard reproducing kernel of `H^2(\mathbb T^\infty)` at the point `\bar\alpha=(\overline{\alpha_p})_p`, and

\[
\boxed{F(s)\ne0\qquad(\Re s>1/2).}
\tag{5}
\]

Equivalently, complete multiplicativity makes the coefficient vector a simultaneous eigenvector of every backward prime shift. Thus the strongest naive cross-degree compatibility suggested after `PL-356` produces a coherent point-evaluation state, not a zero-sensitive critical-strip family.

## 1. `\ell^2` plus complete multiplicativity forces an interior polydisk point

For a fixed prime `p`, all prime powers occur in (1), so

\[
\sum_{k\ge0}|a_{p^k}|^2
=
\sum_{k\ge0}|\alpha_p|^{2k}
<\infty.
\tag{6}
\]

Hence

\[
|\alpha_p|<1
\qquad\text{for every }p.
\tag{7}
\]

Also the prime terms alone give

\[
\sum_p|\alpha_p|^2<\infty.
\tag{8}
\]

More precisely, monotone convergence over finite sets of primes gives the exact tensor-product norm identity

\[
\|F\|_{\mathscr H^2}^2
=
\sum_n|a_n|^2
=
\prod_p\left(1-|\alpha_p|^2\right)^{-1}<\infty.
\tag{9}
\]

Thus `\alpha` lies in the standard point-evaluation domain `\mathbb D^\infty\cap\ell^2` of the infinite-polydisk Hardy space.

Under the Bohr lift, (3) gives

\[
\begin{aligned}
\mathcal BF(z)
&=
\sum_{\nu\in\mathbb N_0^{(\mathcal P)}}
\left(\prod_p\alpha_p^{\nu_p}\right)z^\nu\\
&=
\prod_p\left(\sum_{k\ge0}(\alpha_pz_p)^k\right)\\
&=
\prod_p(1-\alpha_pz_p)^{-1}.
\end{aligned}
\tag{10}
\]

For `w\in\mathbb D^\infty\cap\ell^2`, the standard Hardy kernel is

\[
K_w(z)=\prod_p(1-\overline{w_p}z_p)^{-1}.
\tag{11}
\]

Taking `w_p=\overline{\alpha_p}` proves (4). This is standard infinite-polydisk RKHS structure under the classical Bohr correspondence; no novelty is claimed for the kernel identity itself.

There is an equivalent operator statement. Let the prime shifts on the Dirichlet basis be

\[
S_p e_n=e_{pn}.
\tag{12}
\]

Then

\[
(S_p^*a)_n=a_{pn}=a_pa_n,
\]

so

\[
\boxed{S_p^*F=\alpha_pF\qquad\text{for every prime }p.}
\tag{13}
\]

The completely multiplicative vectors are therefore precisely the normalized joint backward-shift eigenvectors, i.e. the reproducing kernels parametrized by admissible prime coordinates. This is the vector-level counterpart of the shift-commutant rigidity already isolated in `PL-023`.

## 2. The whole native `\mathscr H^2` evaluation half-plane is zero-free

Fix `s=\sigma+it` with `\sigma>1/2`. Cauchy--Schwarz gives absolute convergence:

\[
\sum_{n\ge1}|a_n|n^{-\sigma}
\le
\left(\sum_n|a_n|^2\right)^{1/2}
\left(\sum_n n^{-2\sigma}\right)^{1/2}
<\infty.
\tag{14}
\]

Complete multiplicativity therefore permits the ordinary Euler-product rearrangement in this region:

\[
F(s)
=
\prod_p\left(1-\alpha_pp^{-s}\right)^{-1}.
\tag{15}
\]

This is not a formal continuation of an Euler product. Equation (15) is used only where (14) proves absolute convergence.

The product cannot vanish. Indeed,

\[
\sum_p |\alpha_p|p^{-\sigma}
\le
\left(\sum_p|\alpha_p|^2\right)^{1/2}
\left(\sum_p p^{-2\sigma}\right)^{1/2}
<\infty,
\tag{16}
\]

while every factor in (15) is finite and nonzero because

\[
|\alpha_pp^{-s}|=|\alpha_p|p^{-\sigma}<1.
\tag{17}
\]

Hence the absolutely convergent product has a finite nonzero value, proving (5).

The same conclusion is geometrically immediate from (4): along the Bohr curve

\[
z(s)=(p^{-s})_p,
\]

both `\bar\alpha` and `z(s)` are interior `\ell^2` points for `\sigma>1/2`, and a product Szegő kernel has no zeros there.

## 3. Why this does not transport zeta's zeros into the Bohr Hilbert geometry

The rational-prime zeta family appears as a special radial subfamily of these kernels only after a positive shift. If

\[
a_n=n^{-\delta},\qquad \delta>1/2,
\tag{18}
\]

then `a` is completely multiplicative and square-summable, and

\[
F(s)=\zeta(s+\delta).
\tag{19}
\]

But the native evaluation region `\Re s>1/2` maps to

\[
\Re(s+\delta)>1.
\tag{20}
\]

Thus the kernel model sees precisely the absolutely convergent, zero-free Euler-product side of zeta. To remove the shift and recover the actual coefficients `a_n=1` would leave `\ell^2` altogether.

This gives a sharp negative control on one tempting interpretation of the `1/2` Hilbert boundary. The boundary does not become RH-sensitive merely by imposing the exact nonlinear arithmetic law `a_{mn}=a_ma_n`; inside the standard Bohr `\mathscr H^2` topology, that law forces the family into kernels whose visible analytic region lies entirely on the zero-free side of its Euler products.

## 4. Prior-art and novelty audit

The ambient ingredients are classical. Hedenmalm--Lindqvist--Seip identify `\mathscr H^2` with the square-summable coefficient space and, via Bohr's correspondence, with Hardy `H^2` on the infinite prime torus. Cole--Gamelin identify the natural point-evaluation domain of the infinite-polydisk Hardy space as `\mathbb D^\infty\cap\ell^2`; its kernel is the product of one-variable Szegő kernels. These are already recorded in `research/prime_lattice/SOURCES.md` as the baseline anchors for `PL-001` and the infinite-polydisk evaluation boundary.

A targeted literature audit on 18 September 2026 searched Hardy spaces of Dirichlet series, completely multiplicative coefficient sequences, Euler products, and reproducing kernels. It found the standard Bohr/infinite-polydisk kernel framework and modern work on Hardy-Dirichlet multipliers, but no reason to present (4)--(5) as a new theorem. They are elementary consequences of the classical RKHS/tensor-product structure. **No novelty claim is made.** The durable contribution is the route restriction relative to `PL-356`: exact complete multiplicativity is not the sought source-forced intermediate family because it over-rigidifies the completed space all the way to zero-free kernel vectors.

## 5. Adversarial boundaries

1. **Complete multiplicativity is much stronger than a generic Euler product.** Ordinary multiplicative coefficients may have non-geometric local factors `\sum_{k\ge0}a_{p^k}z^k`; those factors can carry zeros. This finding rules out the canonical geometric local law (2), not every possible nonlinear cross-degree relation.

2. **The conclusion is confined to the native `\mathscr H^2` evaluation domain.** Nothing here proves zero-freeness on `\Re s=1/2`, below it, or in a meromorphic continuation obtained by additional structure.

3. **The Hilbert topology is load-bearing.** The step (14) is exactly what makes the Euler product legitimate for every `\sigma>1/2`. A critical renormalized space, a weighted coefficient space, or a target-relative Mellin/Nyman topology need not have this property.

4. **There is no functional equation or archimedean coupling.** The product kernel is purely prime-local. Its zero-freeness does not explain the Riemann zero divisor; it avoids it.

5. **The zero vector is irrelevant.** With the standard nontrivial completely multiplicative normalization `a_1=1`, (3)--(17) apply. The identically zero sequence is excluded from the statement.

## Research consequence

The nonlinear escape left by `PL-356` is now narrower. Requiring the most exact prime-power compatibility

\[
a_{p^k}=a_p^k
\]

at every coordinate, together with cross-prime multiplicativity, does remove the boundary-zero flexibility of `PL-355`; however it removes too much. The resulting family is exactly the point-kernel manifold of the Bohr Hardy space and has no zeros anywhere in `\Re s>1/2`.

A surviving source-selected family must therefore sit strictly between the two extremes already classified:

\[
\text{free completed coefficients with large zero-set nullspaces}
\quad\text{and}\quad
\text{completely multiplicative kernel vectors with no native zeros}.
\]

The useful next target is an infinite, genuinely nonlinear arithmetic relation that is weaker than complete multiplicativity but stronger than finitely many Hilbert-visible constraints, and whose effect survives a valid continuation or target-relative coupling. Merely asking for the strongest naive Euler-product compatibility cannot provide that mechanism.
