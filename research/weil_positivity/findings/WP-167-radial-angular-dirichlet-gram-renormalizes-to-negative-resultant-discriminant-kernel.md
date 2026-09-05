# WP-167 — the canonical radial-angular Dirichlet Gram is positive only before boundary renormalization; its finite part is the negative cyclotomic resultant/discriminant kernel

**Status:** `EXACT-DERIVED + DECISIVE-NARROWING + RADIAL-ANGULAR-CYCLOTOMIC + POSITIVE-DIRICHLET-GRAM + BOUNDARY-DIVERGENCE + RESULTANT-DISCRIMINANT-CLASSICALIZATION + RENORMALIZED-SIGN-LOSS + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-166` leaves one especially canonical way to escape the pure-gauge obstruction for one-dimensional radial connections: use a second base direction that is already present in the same cyclotomic source. For `n>1`, instead of sampling only the positive radial ray, retain the angular coordinate of the same point in the unit disk and define

\[
H_n(s,t):=\log\left|\Phi_n\!\left(e^{-s+it}\right)\right|,
\qquad s>0,
\quad t\in\mathbb R/2\pi\mathbb Z.
\tag{1}
\]

This gives an intrinsic two-dimensional radial-angular field without importing a new arithmetic kernel. The most direct geometric positivity is then the Dirichlet Gram of the gradients of these fields. At every cutoff `epsilon>0` that Gram is genuinely positive semidefinite. However, the exact boundary limit exposes a sharp obstruction: the diagonal energies diverge, and after subtracting only their forced logarithmic self-divergence, the complete finite Gram is the **negative** of the classical cyclotomic resultant/discriminant kernel already isolated in `WP-156`.

More precisely, with

\[
E_{m,n}(\varepsilon)
:=
\int_{\varepsilon}^{\infty}\!\int_0^{2\pi}
\bigl(
\partial_s H_m\,\partial_s H_n
+
\partial_t H_m\,\partial_t H_n
\bigr)\,dt\,ds,
\tag{2}
\]

one has for every finite real amplitude vector `(a_n)`

\[
\sum_{m,n}a_ma_nE_{m,n}(\varepsilon)
=
\int_{\varepsilon}^{\infty}\!\int_0^{2\pi}
\left|\nabla\sum_n a_nH_n\right|^2dt\,ds
\ge0.
\tag{3}
\]

Nevertheless, for distinct shells,

\[
\boxed{
\lim_{\varepsilon\downarrow0}E_{m,n}(\varepsilon)
=-\pi\log\left|\operatorname{Res}(\Phi_m,\Phi_n)\right|,
\qquad m\ne n,
}
\tag{4}
\]

while on the diagonal

\[
\boxed{
E_{n,n}(\varepsilon)
=
-\pi\varphi(n)\log\!\left(1-e^{-2\varepsilon}\right)
-\pi\log\left|\operatorname{Disc}\Phi_n\right|
+o(1).
}
\tag{5}
\]

Thus the canonical self-energy finite part is

\[
\boxed{
\operatorname{FP}E_{n,n}
:=
\lim_{\varepsilon\downarrow0}
\left[
E_{n,n}(\varepsilon)
+\pi\varphi(n)\log\!\left(1-e^{-2\varepsilon}\right)
\right]
=-\pi\log\left|\operatorname{Disc}\Phi_n\right|.
}
\tag{6}
\]

For an indicator vector of a finite shell set `S`, equations (4)--(6) give exactly minus `pi` times the block log-discriminant of the product `prod_{n in S} Phi_n` from `WP-156`. The second base direction therefore creates no new global positive geometry: **before** renormalization the source has infinite Dirichlet norm at the arithmetic boundary, while **after** the forced subtraction the finite form loses positivity and classicalizes to the already-known resultant/discriminant arithmetic.

A matched control makes the information loss especially explicit. For every odd prime `p`,

\[
\Phi_{2p}(z)=\Phi_p(-z),
\tag{7}
\]

so

\[
H_{2p}(s,t)=H_p(s,t+\pi).
\tag{8}
\]

Any full-circle rotationally invariant scalar Dirichlet energy therefore gives

\[
\boxed{
E_{2p,2p}(\varepsilon)=E_{p,p}(\varepsilon)
\quad\text{for every }\varepsilon>0,
}
\tag{9}
\]

even though

\[
\Lambda(p)=\log p,
\qquad
\Lambda(2p)=0.
\tag{10}
\]

For the smallest example, `Phi_6(z)=Phi_3(-z)`, both shells have `phi=2` and discriminant magnitude `3`, hence identical truncated and renormalized self-energy, whereas their Mangoldt boundary values are `log 3` and `0`. This infinite control family shows that the rotationally invariant positive bulk energy erases exactly the distinguished angular basepoint that carries the prime-power selector.

The obstruction is specific but decisive. It does **not** rule out every two-dimensional, boundary, matrix-valued, or cohomological construction. It rules out the canonical same-source scalar radial-angular Dirichlet/Chern route as the higher-dimensional escape from `WP-166`. A surviving construction must retain a marked boundary section before positivity, introduce genuinely nontrivial matrix curvature or a zero-order coupling not reducible to this scalar harmonic field, or couple the finite and archimedean sectors nonseparably with an independent sign theorem. Merely changing to a conformally equivalent metric does not help, because two-dimensional Dirichlet energy is conformally invariant.

## 1. The angular direction is canonical but the interior field is harmonic

All roots of `Phi_n` lie on the unit circle and `Phi_n(0)=1` for `n>1`. Therefore `Phi_n` is nonvanishing on the open unit disk, a holomorphic logarithm exists there, and `H_n` is the real part of a holomorphic function. Hence

\[
(\partial_s^2+\partial_t^2)H_n=0
\qquad(s>0).
\tag{11}
\]

So the obvious scalar Chern/Laplacian curvature built from `log|Phi_n|` vanishes identically in the interior. Distributionally across the unit circle, the Poincare--Lelong current is supported at the primitive `n`th roots with total divisor multiplicity `phi(n)`. That charge is not the Mangoldt selector: it is nonzero on every shell `n>1`, including mixed composites.

The useful question is therefore not whether local scalar curvature sees `Lambda(n)`--it does not--but whether the positive **gradient energy** of the two-dimensional field can retain the selector after the arithmetic boundary is reached.

## 2. Exact Fourier form of the positive cutoff Gram

The Ramanujan-sum expansion already underlying `WP-162` extends angularly as

\[
H_n(s,t)
=-\sum_{k\ge1}\frac{c_n(k)}k e^{-ks}\cos(kt),
\tag{12}
\]

where `c_n(k)` is the Ramanujan sum. Therefore

\[
\partial_sH_n
=\sum_{k\ge1}c_n(k)e^{-ks}\cos(kt),
\qquad
\partial_tH_n
=\sum_{k\ge1}c_n(k)e^{-ks}\sin(kt).
\tag{13}
\]

Using Fourier orthogonality on the circle and then integrating in `s` gives the exact kernel

\[
\boxed{
E_{m,n}(\varepsilon)
=\pi\sum_{k\ge1}
\frac{c_m(k)c_n(k)}k e^{-2k\varepsilon}.
}
\tag{14}
\]

Equation (3) proves positivity independently of any zeta zero data, Weil kernel, or RH assumption. Thus this candidate passes the local sign gate in the strongest possible way: it is literally a Gram matrix of gradients.

The difficulty appears only at the required arithmetic boundary `epsilon -> 0`, where the logarithmic singularities of the cyclotomic roots enter.

## 3. Root products identify the boundary Gram exactly

Put `r=e^{-epsilon}` and let `P_n` be the primitive `n`th roots of unity. Since

\[
c_n(k)=\sum_{\zeta\in P_n}\zeta^k
=\sum_{\zeta\in P_n}\overline\zeta^{\,k},
\tag{15}
\]

we may rewrite (14) using `-sum_{k>=1}x^k/k=log(1-x)` as

\[
\frac1\pi E_{m,n}(\varepsilon)
=
-\sum_{\zeta\in P_m}\sum_{\eta\in P_n}
\log\left|1-r^2\zeta\overline\eta\right|.
\tag{16}
\]

If `m != n`, the primitive-root sets are disjoint, so every factor has a nonzero limit. Because `|eta|=1`,

\[
|1-\zeta\overline\eta|=|\eta-\zeta|,
\tag{17}
\]

and hence

\[
\prod_{\zeta\in P_m,\eta\in P_n}
|1-\zeta\overline\eta|
=
|\operatorname{Res}(\Phi_m,\Phi_n)|.
\tag{18}
\]

Equations (16)--(18) prove (4).

For `m=n`, separate the ordered root pairs into `zeta=eta` and `zeta!=eta`. The diagonal pairs contribute exactly

\[
-\pi\varphi(n)\log(1-r^2),
\tag{19}
\]

while the off-diagonal product tends

\[
\prod_{\substack{\zeta,\eta\in P_n\\\zeta\ne\eta}}
|\zeta-\eta|
=
|\operatorname{Disc}\Phi_n|.
\tag{20}
\]

This proves (5) and (6) without an arbitrary regularization choice: the divergent coefficient and the finite remainder are forced by the exact root-product decomposition.

For a finite amplitude vector `a`, subtracting only the shellwise self-divergences yields

\[
\operatorname{FP}Q(a)
=
-\pi\left[
\sum_n a_n^2\log|\operatorname{Disc}\Phi_n|
+2\sum_{m<n}a_ma_n
\log|\operatorname{Res}(\Phi_m,\Phi_n)|
\right].
\tag{21}
\]

When every `a_n` is `0` or `1`, the bracket is the standard product-discriminant identity

\[
\log\left|\operatorname{Disc}\prod_{n\in S}\Phi_n\right|
=
\sum_{n\in S}\log|\operatorname{Disc}\Phi_n|
+2\sum_{m<n}\log|\operatorname{Res}(\Phi_m,\Phi_n)|.
\tag{22}
\]

This is exactly the block arithmetic already identified in `WP-156`. In particular, whenever `|Disc Phi_n|>1`,

\[
\operatorname{FP}Q(e_n)
=-\pi\log|\operatorname{Disc}\Phi_n|<0,
\tag{23}
\]

so the positive cutoff form does not pass its sign to the canonical finite part.

## 4. Boundary divergence is not an archimedean completion

Without subtraction, every shell with nonzero `phi(n)` has logarithmically divergent Dirichlet energy as `epsilon -> 0`. The arithmetic boundary fields therefore do not lie in the finite-energy completion of this bulk Dirichlet form. The coefficient of the divergence is `phi(n)`, not `Lambda(n)`, and is present for mixed composites.

Subtracting (19) is canonical as a local self-energy finite part, but it does not solve the sign problem: equations (21)--(23) show that it produces a generally negative quadratic form whose entries are classical finite cyclotomic discriminants and resultants. Adding further finite counterterms specifically to reverse that sign or manufacture the Gamma/pole terms would be a new structure and must be independently forced; it cannot be credited to the positivity of (3).

Nor can a conformal change of the two-dimensional metric rescue the route. For scalar functions in real dimension two, the Dirichlet integral is conformally invariant. A hyperbolic-disk or conformally rescaled cylinder presentation therefore has the same energy mechanism and the same boundary obstruction. A repair must change the operator, boundary architecture, coefficient bundle, or coupling, not merely the conformal metric.

## 5. Matched prime/mixed-composite control

For every odd prime `p`, the cyclotomic identity (7) gives an exact half-turn relation between the two disk fields. Rotational invariance of the full-circle energy then gives (9), pointwise in the cutoff parameter. The control preserves not only the asymptotic divergence but the **entire positive energy curve**.

At `p=3`,

\[
\Phi_3(z)=z^2+z+1,
\qquad
\Phi_6(z)=z^2-z+1=\Phi_3(-z),
\tag{24}
\]

and therefore

\[
E_{3,3}(\varepsilon)=E_{6,6}(\varepsilon)
\quad\text{for every }\varepsilon>0.
\tag{25}
\]

Both have `phi=2` and discriminant magnitude `3`, so their canonical finite parts also agree. Yet

\[
\Lambda(3)=\log3,
\qquad
\Lambda(6)=0.
\tag{26}
\]

Thus the full rotationally invariant Dirichlet geometry cannot distinguish the prime-power shell from its mixed-composite half-turn clone even though the marked boundary value at `z=1` distinguishes them exactly. This is a stronger control than comparing only one asymptotic coefficient.

The conclusion is **not** that the point `z=1` is arbitrary. `WP-161` shows that this distinguished boundary evaluation is precisely where the cyclotomic field carries `Lambda(n)`. The conclusion is that integrating over the whole angular orbit before extracting positivity discards that marked-point information. A surviving boundary construction may retain the marked section before scalarization, but then its nonnegativity requires a new theorem; it is not inherited from the rotationally invariant bulk Gram.

## 6. Prior-art and novelty audit

The analytic ingredients are classical. Harmonic logarithmic potentials of holomorphic functions, the Dirichlet integral and its conformal invariance, and the Poincare--Lelong description of divisor currents are standard complex/potential theory. A standard reference for Dirichlet-space energy is Omar El-Fallah, Karim Kellay, Javad Mashreghi, and Thomas Ransford, *A Primer on the Dirichlet Space*, Cambridge University Press, 2014, DOI `10.1017/CBO9781107239425`. A standard source for Poincare--Lelong and divisor currents is Jean-Pierre Demailly, *Complex Analytic and Differential Geometry*.

Cyclotomic resultants and discriminants are likewise classical arithmetic; the pairwise resultant classification goes back in particular to T. M. Apostol, “Resultants of cyclotomic polynomials,” *Proceedings of the American Mathematical Society* 24 (1970), 457--462. Within this research line, `WP-145`--`WP-156` already audit the resultant/discriminant mechanism and show that it remains finite-prime local algebraic data rather than a global Weil-positive completion.

Accordingly, no novelty is claimed for equations (11), (16)--(20), or the general Dirichlet-space facts in isolation. The Mathia-specific contribution is the exact **classicalization obstruction**: testing the most canonical higher-dimensional escape left by `WP-166` produces a genuine source-native positive Gram at finite cutoff, but its arithmetic boundary either has infinite norm or, under the forced self-energy finite part, becomes exactly the negative of the already-classified cyclotomic resultant/discriminant kernel. The `p` versus `2p` family additionally proves that full angular averaging erases the Mangoldt selector at every cutoff.

This is not a reformulation of classical Weil positivity, a zero-defined spectrum, or an RH-equivalent kernel. It is a falsification upstream of those constructions.

## 7. Research consequence

The route now closed is

\[
\boxed{
\text{cyclotomic radial selector}
+\text{canonical angular direction}
+\text{scalar harmonic field}
+\text{Dirichlet-Gram positivity}
\not\Rightarrow
\text{global Weil positivity}.
}
\tag{27}
\]

The failure has two independent faces. Analytically, the arithmetic boundary sources have infinite positive energy and canonical finite-part subtraction destroys the sign. Arithmetically, the resulting finite kernel is not new: it is precisely the resultant/discriminant geometry already known to be local, while the matched `p`/`2p` control shows that rotational invariance has forgotten the marked boundary selector.

The surviving frontier is therefore narrower than “add a second dimension.” A higher-dimensional construction must retain source-specific finite information in a form not annihilated by angular symmetry, and it must produce its finite-prime and archimedean/global pieces through one intrinsic coupling before the sign theorem is applied. Plausible categories still include a marked-boundary response with independent coercivity, a genuinely matrix-valued curvature with source-forced noncommuting directions, or a nonseparable finite--archimedean/cohomological object. None receives positivity for free from the scalar Dirichlet energy tested here.

## Evidence and dependencies

- `research/weil_positivity/findings/WP-145-*.md` through `WP-156-*`: local cyclotomic resultant/discriminant audit, especially `WP-156`.
- `research/weil_positivity/findings/WP-161-radial-cyclotomic-boundary-value-is-mangoldt-but-its-differential-jet-is-jordan-totient.md`.
- `research/weil_positivity/findings/WP-162-cyclotomic-inward-radial-flux-is-positive-exactly-on-prime-powers.md`.
- `research/weil_positivity/findings/WP-165-cyclotomic-radial-flux-is-pure-gauge-as-a-scalar-connection.md`.
- `research/weil_positivity/findings/WP-166-off-diagonal-radial-incidence-is-still-pure-gauge-as-a-matrix-connection.md`.
- Exact derivation in (11)--(23); no zeta-zero data, RH assumption, or imported Weil kernel enters.

## Bottom line

The angular coordinate supplies exactly the kind of second base direction that `WP-166` leaves open, and its truncated Dirichlet Gram has an impeccable independent positivity theorem. But the arithmetic boundary defeats that route: the positive energy diverges with `phi(n)` self-charge, while its canonical finite part is the negative cyclotomic resultant/discriminant kernel and loses positivity. Full angular invariance also identifies every odd-prime shell `p` with the mixed shell `2p` although their Mangoldt boundary values differ. The canonical scalar radial-angular completion therefore does not produce the missing global Weil-positive form.