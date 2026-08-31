# WP-057 — Prym discriminant is torsion-invisible to real quadratic positivity

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT` for the most direct attempt to turn the `WP-056` Prym polarization discriminant into a genuine positive quadratic form. `WP-056` shows that the old-prime cover `C_{pn}->C_n` stores `log p` canonically in the finite polarization kernel of its Prym. The exact obstruction below is that this carrier is torsion: every real-valued biadditive pairing on it vanishes, every real quadratic form compatible with multiplication vanishes, and the Néron--Tate positive height pairing kills it even when it is paired against arbitrary non-torsion points. The intrinsic nondegenerate pairing that *does* survive on the polarization kernel is the theta-group commutator pairing, which is alternating and root-of-unity-valued rather than ordered and positive.

The finite carrier can be promoted to the canonical finite-Heisenberg representation, but there `p` survives only through the representation dimension `sqrt(|K|)`. Recovering `log p` therefore again requires a nonlinear logarithm of a counting invariant. Thus the route

```text
Prym polarization discriminant
    -> finite polarization kernel
    -> canonical real quadratic / height pairing
    -> positive local Weil coefficient
```

is closed. Any surviving Prym route must make the torsion kernel act on a larger non-torsion space **before** the positive pairing is formed; evaluating a positive quadratic form on the discriminant carrier itself cannot work.

## 1. The `WP-056` carrier is a finite torsion group

Keep the old-prime setup of `WP-055` and `WP-056`. Let

\[
f:C_{pn}\longrightarrow C_n,
\qquad (x,y)\longmapsto(x^p,y),
\]

with `p|n`, and assume the base genus

\[
g_n=\frac{\varphi(n)-2}{2}
\]

is positive. Let

\[
P_{n,p}=\operatorname{Prym}(C_{pn}/C_n)
\]

and let

\[
\lambda_{n,p}:P_{n,p}\longrightarrow P_{n,p}^{\vee}
\]

be the polarization induced from the principal polarization of `J(C_{pn})`.

By the cyclic-cover polarization type used in `WP-056`, the elementary divisor `p` occurs exactly `g_n` times. Over characteristic zero this gives

\[
\boxed{
K_{n,p}:=\ker\lambda_{n,p}
\cong (\mathbf Z/p\mathbf Z)^{2g_n}
}
\tag{1}
\]

on geometric points, and hence

\[
|K_{n,p}|=p^{2g_n}.
\tag{2}
\]

Consequently the exact Prime-Circle arithmetic scale is

\[
\boxed{
\log p
=\frac{1}{2g_n}\log|K_{n,p}|.
}
\tag{3}
\]

This is the strongest local carrier found so far in the Prym branch: unlike the normalized Hodge norm of `WP-055`, the integral polarization remembers the prime itself.

The question tested here is whether the same carrier can support the missing **real positive quadratic form** rather than merely a logarithmic cardinality readout.

## 2. A finite torsion group admits no nonzero real biadditive pairing

There is a general algebraic obstruction independent of Pryms.

Let `G` be a finite abelian group and let

\[
B:G\times G\longrightarrow \mathbf R
\]

be biadditive. If `x` has order `m`, then for every `y`,

\[
mB(x,y)=B(mx,y)=B(0,y)=0.
\]

Since the additive group of `R` is torsion-free,

\[
B(x,y)=0.
\]

Thus

\[
\boxed{
B\equiv0
}
\tag{4}
\]

for every real-valued biadditive form on a finite abelian group.

The same statement holds directly for a real quadratic form compatible with the group multiplication law. If

\[
q:G\longrightarrow\mathbf R,
\qquad
q(rx)=r^2q(x)
\tag{5}
\]

for integers `r`, then for an element of order `m`,

\[
0=q(0)=q(mx)=m^2q(x),
\]

so

\[
\boxed{q(x)=0.}
\tag{6}
\]

Therefore **no nonzero real positive-semidefinite quadratic form can descend to `K_{n,p}` while respecting its additive group structure**. This is stronger than saying that a particular candidate height fails: the target category itself is incompatible with finite torsion.

The statement is deliberately narrow. A finite group certainly admits nonconstant positive functions, graph energies on functions *over* the group, unitary representations, and finite quadratic refinements valued in groups such as `Q/Z`. What it cannot carry nontrivially is an ordered real quadratic form on the torsion group itself.

## 3. Néron--Tate positivity annihilates exactly the discriminant carrier

The most canonical arithmetic-positive repair is the Néron--Tate height.

Let `M` be any symmetric ample line bundle on `P_{n,p}`; one may take a symmetric ample representative associated with the Prym polarization, or a symmetric ample multiple of it. Its canonical height satisfies the exact quadratic law

\[
\widehat h_M([r]x)=r^2\widehat h_M(x).
\tag{7}
\]

For an ample symmetric bundle over a number field, the resulting quadratic form is nonnegative and positive definite after quotienting by torsion. In particular, (7) alone already gives

\[
\boxed{
\widehat h_M(x)=0
\qquad (x\in P_{n,p}(\overline{\mathbf Q})_{\rm tors}).
}
\tag{8}
\]

Since `K_{n,p}` is finite torsion,

\[
\boxed{
\widehat h_M|_{K_{n,p}}\equiv0.
}
\tag{9}
\]

The associated Néron--Tate bilinear pairing

\[
\langle x,y\rangle_M
=\frac12\bigl(
\widehat h_M(x+y)-\widehat h_M(x)-\widehat h_M(y)
\bigr)
\tag{10}
\]

is biadditive. Hence the torsion argument is stronger still: if `x in K_{n,p}` has order `m`, then

\[
m\langle x,y\rangle_M
=\langle mx,y\rangle_M=0
\]

for **every** `y` in the ambient abelian variety. Therefore

\[
\boxed{
\langle K_{n,p},P_{n,p}(\overline{\mathbf Q})\rangle_M=0.
}
\tag{11}
\]

So the carrier of `log p` is not merely null when paired with itself. It lies in the radical of the canonical arithmetic height pairing against every possible non-torsion direction.

This blocks a natural finite--archimedean repair of `WP-056`. Global Néron--Tate height is precisely a canonical arithmetic quadratic object assembled from local data, but its passage to a positive real quadratic space quotients out the finite torsion on which (3) lives. Keeping an individual local-height term cannot inherit the global positive-definite theorem automatically; the globally positive object has already erased the carrier.

## 4. The polarization does retain a perfect pairing, but only as phase data

The previous section does **not** mean that `K_{n,p}` has no intrinsic pairing. Classical theta-group theory identifies exactly what survives.

Let `L` be an ample line bundle inducing the Prym polarization over an algebraic closure. Its theta group fits into the central extension

\[
1\longrightarrow \mathbf G_m
\longrightarrow \mathcal G(L)
\longrightarrow K(L)
\longrightarrow 1,
\tag{12}
\]

where

\[
K(L)=\ker\phi_L=K_{n,p}.
\]

Taking commutators gives the canonical pairing

\[
\boxed{
e_L:K_{n,p}\times K_{n,p}\longrightarrow\mathbf G_m,
}
\tag{13}
\]

which is alternating and bilinear; for a nondegenerate line bundle it is nondegenerate.

For `x` of finite order `m`, bilinearity gives

\[
e_L(x,y)^m=e_L(mx,y)=1.
\tag{14}
\]

Thus over `C`, every value of `e_L` is a root of unity. In particular,

\[
|e_L(x,y)|=1,
\qquad
-\log|e_L(x,y)|=0.
\tag{15}
\]

The nontrivial datum therefore lives in a phase, equivalently in a circle-valued or torsion-valued symplectic form. Choosing an argument lifts it only to `R/Z`; there is no canonical order on that target from which a positive-semidefinite real quadratic form follows.

This gives an intrinsic geometric explanation for the category mismatch in (4)--(11): the positive Hermitian/Riemann geometry lives **upstairs** on the real/complex vector space and integral lattice of the polarized abelian variety. Passing to the finite discriminant quotient preserves the integral index and a mod-one symplectic shadow, but an ordered real bilinear form cannot descend to the quotient.

## 5. The canonical Heisenberg representation exports `p` only as dimension

Theta-group theory supplies the strongest natural escape from the torsion obstruction: instead of trying to pair points of `K_{n,p}`, let the finite theta group act on a genuine vector space.

For a nondegenerate theta group of separable type over an algebraically closed characteristic-zero field, the finite Stone--von Neumann theorem gives a unique irreducible representation of weight one, up to isomorphism. If its space is `V_{n,p}`, then

\[
\boxed{
(\dim V_{n,p})^2=|K_{n,p}|.
}
\tag{16}
\]

Using (2),

\[
\dim V_{n,p}=p^{g_n},
\]

and hence

\[
\boxed{
\log p
=\frac1{g_n}\log\dim V_{n,p}.
}
\tag{17}
\]

So the polarization kernel *can* be promoted canonically, up to representation isomorphism, into a linear object without losing the prime. But (17) shows exactly where the arithmetic scale lives: in the **logarithm of the representation dimension**, another counting/discriminant invariant.

A Hermitian norm on the representation gives ordinary quadratic positivity, but after normalization its value on a unit vector is independent of `p`; the prime scale is not forced as a quadratic expectation. One can of course manufacture the scalar positive operator

\[
\frac1{g_n}\log(\dim V_{n,p})\,I
=(\log p)I,
\tag{18}
\]

but this merely wraps the nonlinear dimension extraction (17) in a positive operator. It does not derive `log p` from the operator's positivity.

This is the same structural warning as `WP-043`: positive linear geometry may carry an arithmetic integer in its determinant/dimension, while the desired logarithm appears only after a nonlinear readout.

## 6. Canonicalizing the `p^k` relative increment still leaves only torsion

`WP-056` observes that the direct degree-`p^k` cover stores

\[
\frac1{2g_n}\log\deg\lambda_{F^{(k)}}
=k\log p,
\tag{19}
\]

so recovering the Mangoldt value `log p` requires a one-step invariant or a relative increment.

At the level of the fixed base Jacobian there is a completely canonical torsion filtration that realizes such an increment. Put

\[
J=J(C_n).
\]

In characteristic zero,

\[
0\longrightarrow J[p^{k-1}]
\longrightarrow J[p^k]
\xrightarrow{[p^{k-1}]}
J[p]
\longrightarrow0
\tag{20}
\]

is exact. Consequently

\[
J[p^k]/J[p^{k-1}]\cong J[p]
\]

and

\[
\boxed{
\frac1{2g_n}
\log\left|J[p^k]/J[p^{k-1}]\right|
=\log p.
}
\tag{21}
\]

Thus the relative extraction need not be viewed as an arbitrary subtraction of two real numbers: the same increment exists as the logarithmic order of a canonical finite quotient in the base torsion tower.

But this sharpening does **not** rescue positivity. Every group in (20), and every quotient in (21), is finite torsion. Equations (4)--(11) therefore apply at every level. The canonical-height pairing sees

\[
\widehat h_M(J[p^k])=0
\]

for all `k`, and the relative quotient still admits no nonzero real biadditive form.

So even the best intrinsic version of the `p^k` relative increment remains a **cardinality invariant of torsion**, not a positive quadratic energy.

## 7. Matched controls and limits of the no-go

The obstruction is universal rather than Riemann-specific. For any polarized abelian variety over characteristic zero, the kernel of a polarization is finite torsion; every real biadditive pairing on that kernel vanishes, Néron--Tate height annihilates it, and the theta-group commutator pairing is multiplicative/phase-valued. The argument therefore survives replacing the cyclotomic cover by the matched arbitrary cyclic covers already used in `WP-056`.

The genus-zero boundary of `WP-056` remains even stronger: when `g_n=0`, the polarization kernel carrying (3) is trivial, so there is no discriminant datum to start from despite the nonzero Mangoldt coefficient.

Two important escape routes are **not** ruled out:

1. A nonlinear invariant such as group order, determinant, entropy, or representation dimension can retain `p`; equations (3), (17), and (21) are examples. But its positivity is not the positivity of a quadratic Weil form.
2. The torsion kernel may act on a larger non-torsion Hilbert/cohomological/correspondence space. A positive form on that larger space need not vanish merely because the acting symmetry is finite. The theta representation in section 5 is the canonical local example. What remains missing is a Mathia-forced operator or pairing on such an enlarged space whose sign theorem produces the assembled finite and archimedean Weil form, rather than a logarithm of its dimension.

Likewise, nontrivial finite quadratic/discriminant forms valued in `Q/Z` or roots of unity are not contradicted by section 2: their codomain has torsion and no compatible real order. They are potential phase/cohomological data, not direct PSD forms.

## 8. Prior-art and novelty boundary

Néron's canonical-height theory and the fact that Néron--Tate heights are quadratic and vanish on torsion are classical. Theta groups, their alternating commutator pairings, and the unique irreducible weight-one representation with dimension squared equal to the order of the finite kernel are also standard abelian-variety theory; the preliminary *Abelian Varieties* manuscript of van der Geer and Moonen gives an audit-friendly formulation in Chapter VIII.

No historical novelty is claimed for any of those ingredients.

The Mathia-specific consequence is their collision with `WP-056`: **the exact finite carrier that stores `log p` through the Prym polarization discriminant is precisely a carrier that every ordered real quadratic height kills**. The only canonical structures that retain the prime after passage to the discriminant are finite cardinality, phase-valued theta pairing, and Heisenberg representation dimension. None makes `log p` the value of an independently positive quadratic pairing.

This is distinct from the previous obstructions:

- `WP-043` shows that a positive cycle Laplacian recovers Mangoldt only through a shell log-determinant;
- `WP-052` shows that ordinary Arakelov completion makes the cyclotomic resultant class principal and cancels its finite degree by the product formula;
- `WP-055` shows that normalized Hodge pull-push is degree-flat;
- `WP-056` finds the missing degree information in the integral Prym discriminant.

The present result identifies why the natural next move -- applying a canonical positive real quadratic/height pairing to that discriminant carrier -- cannot convert the new information into Weil positivity.

## 9. Consequence for the Weil-positivity search

The surviving Prym mechanism must therefore have the schematic form

\[
\boxed{
K_{n,p}\ \text{(torsion/index data)}
\longrightarrow
\text{action or extension on a non-torsion global space}
\longrightarrow
\text{one assembled positive pairing},
}
\tag{22}
\]

not

\[
K_{n,p}
\longrightarrow
\text{positive real quadratic form on }K_{n,p}.
\]

Such an enlargement would still have to solve every global requirement left open by `WP-056`: cross-prime coupling, the `p^{-k/2}` transfer normalization without hand multiplication, the Riemann `Gamma_R`/digamma sector, the polar counterterms, and an independent sign theorem. Merely taking `log |K|`, `log dim V`, a theta phase, or a Néron--Tate height does not supply that structure.
