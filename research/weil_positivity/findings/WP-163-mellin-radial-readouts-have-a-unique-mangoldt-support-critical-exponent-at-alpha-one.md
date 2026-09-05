# WP-163 — Mellin radial readouts have a unique Mangoldt-support critical exponent at alpha one

**Status:** `EXACT-DERIVED + DECISIVE-NARROWING + PRIME-CIRCLE-BRIDGE + NONLOCAL-RADIAL-MELLIN-CLASSIFICATION + CRITICAL-EXPONENT + MANGOLDT-SUPPORT-RIGIDITY + POSITIVITY-SUPPORT-TRADEOFF + MATCHED-CONTROLS + PRIOR-ART-CLASSICALIZATION`.

`WP-162` shows that the canonical inward cyclotomic radial flux

\[
\rho_n(s)
:=-\frac{d}{ds}\log\Phi_n(e^{-s}),
\qquad n>1,
\tag{1}
\]

has total mass `Lambda(n)`, is pointwise positive exactly on prime-power shells, and necessarily changes sign on every mixed-prime shell. It therefore leaves open a narrower question than ordinary positive bulk scalarization: can a **canonical nonlocal radial weighting** preserve the prime-power cancellation while producing a more usable positive response?

The exact dilation-homogeneous family can be classified completely. For real `alpha>0`, define the Mellin radial readout

\[
\boxed{
M_n(\alpha)
:=
\int_0^\infty
s^{\alpha-1}\rho_n(s)\,ds.
}
\tag{2}
\]

The integral is ordinary and convergent for every `alpha>0`. Its exact value is

\[
\boxed{
M_n(\alpha)
=
-\Gamma(\alpha)\zeta(\alpha)\,
 n^{1-\alpha}
\prod_{p\mid n}\left(1-p^{\alpha-1}\right),
}
\tag{3}
\]

where the apparent singularity at `alpha=1` is removable. At that critical exponent,

\[
\boxed{M_n(1)=\Lambda(n).}
\tag{4}
\]

More strongly, for every real `alpha>0`,

\[
\boxed{
M_n(\alpha)=0
\quad\Longleftrightarrow\quad
\alpha=1
\text{ and }n\text{ has at least two distinct prime divisors}.
}
\tag{5}
\]

Thus `alpha=1` is the **unique positive Mellin homogeneity exponent** in this source-forced radial family that retains the Mangoldt prime-power support. Moving to either side destroys the sparse selector in opposite ways:

\[
\boxed{
0<\alpha<1
\quad\Longrightarrow\quad
M_n(\alpha)>0
\text{ for every }n>1,
}
\tag{6}
\]

whereas for `alpha>1`,

\[
\boxed{
\operatorname{sgn}M_n(\alpha)
=(-1)^{\omega(n)+1},
}
\tag{7}
\]

so every shell again has nonzero mass and mixed-prime shells acquire parity signs.

This is a sharp extension of the exponential-damping control in `WP-162`. Positive subcritical Mellin weighting can indeed turn the signed flux into a positive scalar on **all** shells, but precisely by filling in every Mangoldt zero. The sparse arithmetic selector survives only at the critical exponent where a zeta pole is cancelled by a zero of the generalized Jordan factor. Consequently the canonical scale-homogeneous radial family cannot simultaneously manufacture a positive bulk response and preserve the finite Weil support.

The result is not a Weil-positive form and does not use zero data. Its value is a rigidity statement about the exact Mathia-native radial object: any surviving finite--archimedean construction must use more than a scalar dilation eigenkernel applied shell by shell.

## 1. The Mellin family is intrinsic and needs no regularization

From `WP-162`,

\[
\rho_n(s)
=-\sum_{d\mid n}
\mu(n/d)\frac{d}{e^{ds}-1}
=-\sum_{m\ge1}c_n(m)e^{-ms}.
\tag{8}
\]

The same finding gives the finite boundary limit

\[
\rho_n(0^+)=\frac{\varphi(n)}2
\tag{9}
\]

and exponential decay as `s\to\infty`. Therefore, for complex `z` with `Re z>0`,

\[
M_n(z):=
\int_0^\infty s^{z-1}\rho_n(s)\,ds
\tag{10}
\]

is an ordinary Mellin transform, holomorphic in the half-plane `Re z>0`. In particular, the critical value `z=1` does **not** require zeta regularization or analytic continuation of the defining integral:

\[
M_n(1)=\int_0^\infty\rho_n(s)\,ds=\Lambda(n)
\tag{11}
\]

by the boundary-to-origin conservation law of `WP-162`.

The monomials `s^{z-1}` are the standard Mellin eigenkernels for radial dilation. Thus (10) tests the simplest canonical nonlocal family after the unweighted total flux, without choosing a kernel from the desired arithmetic answer.

## 2. Exact evaluation by the cyclotomic divisor decomposition

For `Re z>1`, each divisor term in (8) is individually Mellin integrable. The standard Bose integral gives

\[
\int_0^\infty
s^{z-1}\frac{d}{e^{ds}-1}\,ds
=
 d^{1-z}\Gamma(z)\zeta(z).
\tag{12}
\]

Hence

\[
M_n(z)
=
-\Gamma(z)\zeta(z)
\sum_{d\mid n}\mu(n/d)d^{1-z}.
\tag{13}
\]

The finite divisor sum is the generalized Jordan-totient factor

\[
\boxed{
D_n(z)
:=
\sum_{d\mid n}\mu(n/d)d^{1-z}
=
 n^{1-z}
\prod_{p\mid n}
\left(1-p^{z-1}\right).
}
\tag{14}
\]

For `n>1`, `D_n(1)=0`. Its zero at `z=1` cancels the unique pole of `zeta(z)` in `Re z>0`, while `Gamma(z)` is holomorphic there. Thus the right-hand side of (13) has a removable singularity at `z=1` and is holomorphic throughout `Re z>0` after removal.

Since both sides are holomorphic on `Re z>0` and agree on the nonempty open set `Re z>1`, the identity theorem extends (13) to the whole half-plane. This proves (3) as an identity of ordinary Mellin transforms, not as a definition by continuation.

Equivalently, for `Re z>1`, (13) is the classical fixed-modulus Ramanujan-sum Dirichlet series

\[
\sum_{m\ge1}\frac{c_n(m)}{m^z}
=
\zeta(z)
\sum_{d\mid n}\mu(n/d)d^{1-z},
\tag{15}
\]

multiplied by `-Gamma(z)`. The Mathia content is therefore not a new special-function identity; it is what that identity implies for the exact radial geometry singled out by `WP-161` and `WP-162`.

## 3. The Mangoldt selector is the critical pole-zero cancellation

Let

\[
r:=\omega(n)
\tag{16}
\]

be the number of distinct prime divisors of `n`, and write `z=1+epsilon`. Equation (14) gives

\[
D_n(1+\epsilon)
=
 n^{-\epsilon}
\prod_{p\mid n}(1-p^\epsilon).
\tag{17}
\]

Since

\[
1-p^\epsilon
=-\epsilon\log p+O(\epsilon^2),
\tag{18}
\]

we have

\[
D_n(1+\epsilon)
=
(-\epsilon)^r
\prod_{p\mid n}\log p
+O(\epsilon^{r+1}).
\tag{19}
\]

At the same time,

\[
\zeta(1+\epsilon)
=\frac1\epsilon+O(1),
\qquad
\Gamma(1+\epsilon)=1+O(\epsilon).
\tag{20}
\]

If `r=1`, so `n=p^a`, equations (13), (19), and (20) give

\[
\lim_{\alpha\to1}M_{p^a}(\alpha)
=\log p.
\tag{21}
\]

If `r\ge2`, the Jordan zero has order at least two, so one power survives after cancelling the zeta pole and

\[
\lim_{\alpha\to1}M_n(\alpha)=0.
\tag{22}
\]

Therefore

\[
\boxed{
M_n(1)
=
\begin{cases}
\log p,&n=p^a,\\
0,&\omega(n)\ge2,
\end{cases}
=
\Lambda(n).
}
\tag{23}
\]

This identifies the exact mechanism behind the sparse boundary mass. The prime-power selector is not stable under generic radial smoothing: within the whole Mellin family it occurs at a single critical exponent, through the collision of the universal simple zeta pole with a shell-dependent Jordan zero whose order is `omega(n)`.

## 4. Subcritical Mellin weighting makes every shell positive

Take real `0<alpha<1`. Then

\[
\Gamma(\alpha)>0,
\qquad
\zeta(\alpha)<0.
\tag{24}
\]

For every prime divisor `p\mid n`,

\[
p^{\alpha-1}<1,
\qquad
1-p^{\alpha-1}>0,
\tag{25}
\]

so `D_n(alpha)>0`. Equation (3) therefore gives

\[
\boxed{M_n(\alpha)>0\qquad(n>1).}
\tag{26}
\]

This is a useful matched falsification of a tempting idea. The kernel `s^{alpha-1}` is positive on the radial half-line, and for subcritical exponents its nonlocal averaging overcomes the sign changes of every mixed-prime flux strongly enough to yield a positive number. But that positivity has **full shell support**. In particular,

\[
M_6(\alpha)>0
\qquad(0<\alpha<1),
\tag{27}
\]

although

\[
\Lambda(6)=0.
\tag{28}
\]

Thus gaining shellwise positivity in this canonical family does exactly what the pointwise norms of `WP-162` did: it destroys the arithmetic sparsity needed by the finite explicit-formula coefficient.

The distinction is important. Equation (26) is nonlocal and is not covered by `WP-162`'s pointwise-positive-density argument. It is a genuinely stronger control: even a natural positive kernel acting on the **signed** flux produces false positive mass on mixed shells as soon as its homogeneity is moved below the critical value.

## 5. Supercritical weighting exposes parity rather than Mangoldt support

For real `alpha>1`, `Gamma(alpha)` and `zeta(alpha)` are positive, while every prime factor in (14) is negative:

\[
1-p^{\alpha-1}<0.
\tag{29}
\]

Hence

\[
\boxed{
\operatorname{sgn}D_n(\alpha)=(-1)^{\omega(n)},
\qquad
\operatorname{sgn}M_n(\alpha)=(-1)^{\omega(n)+1}.
}
\tag{30}
\]

No shell vanishes. For the smallest mixed-prime control `n=6`, equation (3) at `alpha=2` gives the exact value

\[
D_6(2)
=6^{-1}(1-2)(1-3)
=\frac13,
\tag{31}
\]

and therefore

\[
\boxed{
M_6(2)
=-\zeta(2)D_6(2)
=-\frac{\pi^2}{18}<0.
}
\tag{32}
\]

Thus the same shell that has positive subcritical Mellin mass and zero critical mass becomes negative immediately in the simplest supercritical test. More generally, the supercritical family reads only the parity of the number of distinct prime factors at the sign level, not prime-power support.

Combining the three regimes proves the rigidity statement (5): for positive real `alpha\ne1`, `Gamma(alpha)` and `zeta(alpha)` are nonzero and every factor `1-p^{alpha-1}` is nonzero, so `M_n(alpha)` cannot vanish. At `alpha=1`, equations (21)--(23) give precisely the Mangoldt zeros.

## 6. What this closes, and what it does not

`WP-162` showed that unweighted total radial flux preserves `Lambda(n)` only through signed cancellation, and that a simple positive exponential damping already contaminates `n=6`. The present calculation closes a broader and more canonical escape: **exact radial dilation eigenweights**.

Within this Mellin family there is no nearby deformation that keeps the finite selector while improving positivity:

\[
\boxed{
\begin{array}{ccl}
0<\alpha<1&:&\text{positive on every shell, but full support},\\
\alpha=1&:&\text{exact Mangoldt support, via signed critical cancellation},\\
\alpha>1&:&\text{full support with }(-1)^{\omega(n)+1}\text{ signs}.
\end{array}
}
\tag{33}
\]

This does **not** rule out an arbitrary nonlocal kernel. More importantly, it does not rule out the mechanism demanded by the research mandate: an operator that keeps the signed finite flux as input, couples shells to each other and to the archimedean sector before scalarization, and then obtains nonnegativity from an independent geometric theorem.

The result also does not turn the factor `zeta(alpha)` in (3) into a hidden Riemann-zero construction. Here it is the elementary Mellin transform of `1/(e^s-1)`, evaluated on a real homogeneity parameter. No zeta zeros, spectral data, explicit-formula kernel, or RH-equivalent positivity criterion is inserted.

Nor does the critical pole in (3) supply the missing archimedean term. It explains why the **finite shell selector** is rigid inside this radial family. A global Weil mechanism would still have to produce the Gamma/polar contribution and the test-function autocorrelation in the same positive geometry rather than attach them afterward.

## 7. Relation to the current Mathia frontier

`WP-161` classified the local radial jet: the zero-order boundary value is Mangoldt while every positive local curvature coefficient has full Jordan-totient support. `WP-162` then showed that the complete nonlocal radial path recovers Mangoldt exactly as net signed flux. `WP-163` now classifies the natural Mellin deformation of that entire path and shows that the sparse selector is a **critical, isolated homogeneity** rather than a robust positive radial observable.

This sharpens the surviving category in the accepted finite--archimedean incidence direction. Merely replacing local differentiation by a source-independent scale-homogeneous radial average is not enough. The next viable operation must mix additional data before the scalar sign is taken: cross-shell incidence, a genuinely global boundary operator, or finite--archimedean coupling whose positivity theorem acts on the assembled object.

The same result also matches the recurring operator-category warning in this line. A family of positive scalar numbers `M_n(alpha)` for `0<alpha<1` is not a positive semidefinite quadratic form on Weil test functions. Conversely, exact recovery of `Lambda(n)` at `alpha=1` remains only the finite coefficient side. Neither property alone bridges to global Weil positivity.

## 8. Prior-art and novelty audit

No theorem-level novelty is claimed for equations (12)--(15). The fixed-modulus Ramanujan-sum Dirichlet series

\[
\sum_{m\ge1}\frac{c_n(m)}{m^z}
=
\zeta(z)
\sum_{d\mid n}\mu(n/d)d^{1-z}
\tag{34}
\]

is classical; standard accounts of Ramanujan sums record it, and the divisor factor is the generalized Jordan-totient/Möbius convolution. László Tóth, *Some remarks on Ramanujan sums and cyclotomic polynomials*, Bulletin Mathématique de la Société des Sciences Mathématiques de Roumanie 53 (2010), 277--292, is neighboring literature already relevant to the cyclotomic/Ramanujan interface. The product formula for generalized Jordan totients is likewise classical.

The novelty audit therefore classicalizes the analytic identity rather than presenting it as a new arithmetic theorem. The durable contribution is the **Mathia-specific classification of the surviving radial route**: starting from the exact cyclotomic flux forced by `WP-162`, the full positive-real Mellin family has a unique exponent with Mangoldt support, and that exponent is exactly the undeformed signed-flux value `alpha=1`. Subcritical positivity and supercritical parity are both exact false controls for the desired Weil coefficient.

A targeted literature search around cyclotomic logarithmic derivatives, Ramanujan sums, their Dirichlet generating series, and generalized Jordan factors found the ingredients as classical identities but did not supply a distinct geometric theorem that converts this shellwise Mellin family into a Weil-positive quadratic form. This finding therefore makes no historical priority claim beyond its role as a project-specific narrowing of the Mathia construction.

## 9. Falsification surface and research consequence

The core result has four direct checks:

1. verify the endpoint regularity of `rho_n` from `WP-162`, which gives ordinary Mellin convergence for `Re z>0`;
2. for `Re z>1`, apply (12) term by term to the finite divisor decomposition (8), obtaining (13);
3. factor the finite divisor sum as (14) and remove the `z=1` singularity using (17)--(20);
4. check the three real regimes from the signs of `zeta(alpha)` and `1-p^{alpha-1}`, with `n=6`, `alpha=2` giving the exact matched value `-pi^2/18`.

Failure of any one of these identities would invalidate the corresponding classification. No numerical fitting or zero input is required.

The resulting boundary for the radial route is

\[
\boxed{
\text{Mellin positivity away from }\alpha=1
\ \Longrightarrow\ 
\text{loss of Mangoldt sparsity},
}
\tag{35}
\]

while

\[
\boxed{
\text{Mangoldt sparsity}
\ \Longleftrightarrow\ 
\text{the critical unweighted signed-flux exponent }\alpha=1
}
\tag{36}
\]

inside the entire positive-real Mellin family. The next credible Weil-positivity attempt must therefore move beyond shellwise scale-homogeneous radial scalarization and force its sign only after a genuinely global finite--archimedean assembly.