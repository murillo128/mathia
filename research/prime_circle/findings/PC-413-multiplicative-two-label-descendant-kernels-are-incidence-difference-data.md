# PC-413 — multiplicative two-label descendant kernels are incidence-difference data

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for source-independent descendant couplings whose two conductor labels may be used separately but whose kernel is multiplicative prime by prime. This strictly enlarges the kernel classes treated in PC-410--PC-412: the local weight may be an arbitrary function of the pair of prime exponents `(v_p(m),v_p(k))`, rather than only of their join, meet, or a fixed power of `gcd/lcm`, and the two Mellin frequencies may be distinct. At every fresh prime, however, the Prime-Circle descendant cocycle acts on that arbitrary two-label kernel only through its two-dimensional incidence difference. Under absolute convergence the global coupling is therefore an Euler product determined entirely by the externally chosen conductor kernel and the universal descendant law. A matched arbitrary base profile reproduces it. Consequently this whole multiplicative conductor-only family cannot by itself provide a source-specific RH mechanism.

This does **not** cover kernels coupling different rational primes to one another, source-derived angular/chord/old-new data that is not measurable from conductor valuations, nonlinear state changes, or interaction rank/depth growing with conductor outside a fixed prime-local kernel. Those are the surviving boundaries.

## 1. Universal fresh-prime cocycle at two Mellin frequencies

Keep the PC-405/PC-407 descendant law for a fixed parent shell `n>1`,

\[
\widehat{h_{nm}}(t)=c_{n,m}(t)\widehat h_n(t),
\]

with multiplicative coefficients and prime-power factors

\[
c_{n,p^a}(t)=
\begin{cases}
1,&a=0,\\[1mm]
p^{iat},&a\ge1,\ p\mid n,\\[1mm]
p^{i(a-1)t}(p^{it}-1),&a\ge1,\ p\nmid n.
\end{cases}
\tag{1}
\]

Fix real Mellin frequencies `t,u`. At a fresh prime `p\nmid n` put

\[
A=p^{it},\qquad C=p^{-iu}.
\tag{2}
\]

The two local descendant sequences are

\[
e_0=1,\qquad e_a=A^a-A^{a-1}\quad(a\ge1),
\tag{3}
\]

and

\[
f_0=1,\qquad f_b=C^b-C^{b-1}\quad(b\ge1).
\tag{4}
\]

PC-410 used the telescoping cumulative sums of (3) to prove cancellation when the weight depends only on `max(a,b)`. PC-412 showed that changing the two Mellin frequencies prevents that special max-shell cancellation, but its reciprocal-lcm kernel still classicalizes to a universal zeta dephasing factor. The natural remaining question is whether a genuinely arbitrary **two-label conductor kernel** can retain more source information.

## 2. Arbitrary prime-local two-label kernels

Let the conductor kernel be multiplicative in the pair `(m,k)`:

\[
\boxed{
W(m,k;t,u)=\prod_p w_p\bigl(v_p(m),v_p(k);t,u\bigr),
\qquad w_p(0,0;t,u)=1.
}
\tag{5}
\]

The local arrays `w_p(a,b;t,u)` may otherwise be arbitrary and may depend on the spectral parameters. The important restrictions are only that they are selected independently of the Prime-Circle source profile and that different rational primes are not coupled inside one local factor.

Whenever the resulting double series is absolutely convergent, define

\[
\boxed{
K_{n,W}(t,u)
:=
\sum_{m,k\ge1}
W(m,k;t,u)c_{n,m}(t)\overline{c_{n,k}(u)}.
}
\tag{6}
\]

A sufficient local hypothesis for the algebra below is `w_p\in\ell^1(\mathbb N_0^2)` for every `p`, together with the usual summability of the deviations of the local factors from `1`; finite-support arrays need no limiting argument. More general conditionally convergent kernels are deliberately not claimed here.

At a fresh prime, the local factor of (6) is

\[
F_p(A,C)
=
\sum_{a,b\ge0}e_a f_b\,w_p(a,b).
\tag{7}
\]

The key point is that (7) has an exact normal form for **every** such array.

## 3. Exact two-dimensional incidence-difference identity

Define the forward mixed difference

\[
\boxed{
(\Delta_1\Delta_2 w)(a,b)
:=w(a,b)-w(a+1,b)-w(a,b+1)+w(a+1,b+1).
}
\tag{8}
\]

Then direct reindexing of (7) gives

\[
\boxed{
F_p(A,C)
=
\sum_{a,b\ge0}
A^aC^b(\Delta_1\Delta_2w_p)(a,b).
}
\tag{9}
\]

For finite-support `w`, (9) is a finite identity. Indeed

\[
e_a=A^a-\mathbf 1_{a\ge1}A^{a-1},
\qquad
f_b=C^b-\mathbf 1_{b\ge1}C^{b-1},
\]

so expanding the product and shifting the second term in each coordinate yields (8) coefficient by coefficient. For `w\in\ell^1(\mathbb N_0^2)`, the same identity follows by truncation because shifts preserve `\ell^1` and `|A|=|C|=1`.

Thus the universal descendant cocycle does not inspect an arbitrary two-label conductor kernel directly. It applies the product-chain Möbius operator to it and then takes the bidisk Fourier generating function of the result. Equivalently, **only the mixed incidence curvature `\Delta_1\Delta_2 w_p` survives at a fresh prime**.

This is the two-label analogue of the one-dimensional telescoping behind PC-410. The special max-shell cancellation there is not the fundamental operation; it is one degenerate outcome of the more general difference transform (9).

## 4. Parent primes are finite local corrections

If `p\mid n`, equation (1) contains no fresh-prime first difference. The local factor is simply

\[
\boxed{
G_p(A,C)
=
\sum_{a,b\ge0}A^aC^b w_p(a,b).
}
\tag{10}
\]

Hence, whenever absolute convergence justifies Euler factorization,

\[
\boxed{
K_{n,W}(t,u)
=
\prod_{p\mid n}G_p(p^{it},p^{-iu})
\prod_{p\nmid n}F_p(p^{it},p^{-iu}).
}
\tag{11}
\]

The parent dependence therefore changes only finitely many local factors. The entire infinite fresh-prime product is determined by the fixed family of conductor arrays `w_p` through (9). No chord location, root angle, cyclotomic value, old/new incidence matrix, or other Prime-Circle source datum enters those fresh factors.

This distinction matters for RH-oriented use. One can certainly choose `w_p` so that (11) contains Riemann or Dirichlet `L` factors. But such factors are then properties of the **chosen kernel**. Equation (9) gives no route by which the roots-of-unity geometry independently forces them.

## 5. PC-410--PC-412 are exact special cases

Several previous branches become transparent inside (9).

For a join-only local weight

\[
w_p(a,b)=\omega_p(\max(a,b)),
\tag{12}
\]

and equal frequencies `t=u`, summing (9) by max shells reproduces PC-410: every positive fresh shell cancels and `F_p=\omega_p(0)`. With the reciprocal-lcm choice and `t\ne u`, the same formula gives the cross-frequency local factors studied in PC-412.

For the meet-plus-join kernel of PC-411,

\[
w_p(a,b)=x^{\max(a,b)}y^{\min(a,b)},
\tag{13}
\]

(9) is exactly the incidence form underlying its universal zeta rectangle. Thus adding the meet changes the mixed difference but does not change the source-identifiability problem.

A useful independent check is the completely separable array

\[
w_p(a,b)=x^a y^b,
\qquad |x|,|y|<1.
\tag{14}
\]

Here

\[
\Delta_1\Delta_2w_p(a,b)
=(1-x)(1-y)x^ay^b,
\]

and (9) gives

\[
\boxed{
F_p(A,C)
=
\frac{1-x}{1-Ax}\,
\frac{1-y}{1-Cy}.
}
\tag{15}
\]

Taking `x` and `y` to be powers of `p^{-1}` globalizes (15) into ordinary shifted zeta ratios. This is the cleanest possible example of the obstruction: an apparently rich two-label coupling produces all-prime analytic structure, but that structure is completely specified before the Prime-Circle source profile is supplied.

## 6. Matched-control falsification is exact

Let `h` be an arbitrary Mellin-tame nonarithmetic base profile and propagate it by the same universal descendant operators used in PC-405,

\[
\widehat{h_m}(t)=c_{n,m}(t)\widehat h(t).
\tag{16}
\]

For any bilinear construction using the same conductor kernel (5), the frequencywise descendant factor is still exactly `K_{n,W}(t,u)`. The actual source appears only through the outer factor

\[
\widehat h(t)\overline{\widehat h(u)}.
\tag{17}
\]

Replacing the cyclotomic parent profile by a matched arbitrary profile therefore preserves every fresh-prime factor in (11), including any zeta or `L` divisor generated by the chosen `w_p`. The kernel can be spectrally nontrivial while remaining **source blind** in precisely the sense required by the research mandate.

This control is stronger than saying that a particular zeta identity is classical. It shows that, within the hypotheses of (5)--(6), no manipulation of the two conductor labels can make the all-prime analytic factor evidence for a Prime-Circle-specific mechanism: the same factor survives after removing the roots-of-unity source.

## 7. Prior-art and novelty audit

No novelty is claimed for the algebraic ingredients of (8)--(11). Möbius inversion and finite differences on chains, and their products on locally finite posets, are standard incidence-algebra operations. Likewise, multiplicative kernels on the divisibility lattice and their meet/join specializations sit in the classical GCD/LCM matrix literature already anchored for this line. In particular, Korkee and Haukkanen, *On a general form of join matrices associated with incidence functions*, Aequationes Math. 75 (2008), doi:10.1007/s00010-007-2922-6, and Mattila and Haukkanen, *On the positive definiteness and eigenvalues of meet and join matrices*, Discrete Math. 326 (2014), 9--19, doi:10.1016/j.disc.2014.02.014, provide the relevant incidence-matrix background used in PC-410/PC-411.

The novelty audit therefore downgrades the ambient transform immediately: (9) is a product-chain summation-by-parts identity, not a new arithmetic structure. The project-specific result is the obstruction obtained by combining that classical transform with the exact PC-405 descendant cocycle. It closes a substantially larger natural branch than PC-410/PC-411: **separate dependence on the two conductor labels is not enough if that dependence remains source-independent and primewise multiplicative.**

Nor does (11) provide a functional equation, gamma factor, critical-line selector, or new zero-generating operator. Any such structure obtained solely by tuning `w_p` is an externally imposed spectral wrapper under the canonical Prime-Circle contract.

## 8. Falsification tests and surviving boundary

The local theorem is easy to falsify independently of any Euler product. Choose arbitrary finite-support complex data `w(a,b)`, arbitrary unit complex numbers `A,C`, and compute both sides of

\[
\sum_{a,b\ge0}
\bigl(A^a-\mathbf1_{a\ge1}A^{a-1}\bigr)
\bigl(C^b-\mathbf1_{b\ge1}C^{b-1}\bigr)w(a,b)
=
\sum_{a,b\ge0}A^aC^b\Delta_1\Delta_2w(a,b).
\tag{18}
\]

A single counterexample disproves the core claim. Random finite arrays provide a direct numerical stress test, but (18) is already an exact finite reindexing identity.

The negative result is intentionally narrower than "all two-label kernels." It leaves four qualitatively different routes open:

1. a kernel that couples valuations at **different rational primes**, so it does not factor as (5);
2. a kernel derived from angular/chord/old-new geometry before quotienting to conductor valuations;
3. a nonlinear interaction that changes the descendant state or product law rather than merely weighting pairs of labels;
4. a family whose rank, depth, or interaction complexity grows with the conductor and therefore is not represented by a fixed prime-local array.

These are now the meaningful ways to interpret the two-label escape left by PC-412. Merely replacing `gcd`, `lcm`, or a separable conductor weight by a more elaborate primewise function of `(v_p(m),v_p(k))` cannot overcome the matched-control obstruction.