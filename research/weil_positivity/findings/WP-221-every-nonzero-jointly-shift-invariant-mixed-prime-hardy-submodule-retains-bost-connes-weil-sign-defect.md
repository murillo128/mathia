# WP-221 — Every nonzero jointly shift-invariant mixed-prime Hardy submodule retains the Bost–Connes Weil sign defect

**Status:** `EXACT-DERIVED + BOST-CONNES-CRITICAL-GRAM + FINITE-MIXED-PRIME + HARDY-SUBMODULE-LOCALIZATION + TOEPLITZ-NUMERICAL-RANGE + ADMISSIBLE-SUBSPACE-NO-GO + PASSIVE-MULTIPLICITY-NO-GO + DECISIVE-NARROWING + PRIOR-ART-CLASSICAL-TOOLS + NOT-A-WEIL-BRIDGE`.

`WP-220` closes the finite mixed-prime restriction escape when the compressed source shifts remain pairwise doubly commuting: Mandrekar–Seto then forces a scalar-inner Beurling submodule and the entire Toeplitz compression is unitarily equivalent to the unrestricted defect. Joint shift invariance without double commutation was left open because general polydisc submodules are much richer.

For the sign question, however, no invariant-subspace classification is needed. A nonzero Hardy function cannot have boundary mass missing from an open torus patch, while coordinate-shift invariance lets analytic peak polynomials localize that mass near any prescribed boundary point. Consequently every nonzero jointly shift-invariant submodule still sees the full scalar-symbol numerical range.

More precisely, let `E` be a Hilbert space, let

\[
0\ne M\subset H^2_E(\mathbb D^d)
\]

be a closed subspace invariant under every scalar coordinate multiplier `M_{z_j}`, and let `w\in C(\mathbb T^d,\mathbb R)`. Then

\[
\boxed{
\overline{W\!\left(P_M(T(w)\otimes I_E)|_M\right)}
=
[\min_{\mathbb T^d}w,\max_{\mathbb T^d}w].
}
\]

Thus if `w` changes sign, **every** nonzero jointly shift-invariant submodule has both positive and negative Rayleigh quotients. No double-commutation hypothesis is required, and merely adding passive source multiplicity does not help as long as the defect remains the same scalar Toeplitz symbol tensored with the identity.

Applying this to the critical Bost–Connes finite-prime defect from `WP-220`,

\[
W_F=T(w_F),
\qquad
w_F(\theta)=\sum_{p\in F}(\log p)\bigl(1-P_{p^{-1/2}}(\theta_p)\bigr),
\]

gives the exact interval

\[
\boxed{
\overline{W(P_M(W_F\otimes I_E)|_M)}
=
\left[
-2\sum_{p\in F}\frac{(\log p)p^{-1/2}}{1-p^{-1/2}},
\;
2\sum_{p\in F}\frac{(\log p)p^{-1/2}}{1+p^{-1/2}}
\right].
}
\]

Both endpoints have strict opposite signs for every nonempty finite `F`. Hence **no nonzero source-covariant Hardy submodule can make the finite critical Bost–Connes Weil defect positive**, even when the submodule is non-Beurling, genuinely mixed-prime, non-doubly-commuting, or lives in a passive vector-valued multiplicity.

This strictly narrows the admissible-test-space escape left by `WP-218`--`WP-220`. A surviving restriction must break joint source-shift invariance itself, pass to a genuinely different quotient/coinvariant geometry, or change the scalar Toeplitz defect before compression through a nontrivial operator-valued, finite--archimedean, or other global coupling. Increasing multiplicity without changing the symbol is not enough.

## 1. General localization theorem for Hardy submodules

Let `E` be a Hilbert space and write

\[
\mathcal H=H^2_E(\mathbb D^d)
\simeq H^2(\mathbb D^d)\otimes E.
\tag{1}
\]

Let `M` be a nonzero closed subspace satisfying

\[
M_{z_j}M\subseteq M,
\qquad j=1,\ldots,d.
\tag{2}
\]

For real `w\in C(\mathbb T^d)`, define the scalar vector-valued Toeplitz operator

\[
A_w=T(w)\otimes I_E
\tag{3}
\]

and its compression

\[
A_{w,M}=P_MA_w|_M.
\tag{4}
\]

The claim is

\[
\boxed{
\overline{W(A_{w,M})}
=[\min w,\max w].
}
\tag{5}
\]

The upper inclusion is immediate. For every unit vector `g\in M`, boundary values give

\[
\langle g,A_{w,M}g\rangle
=
\langle g,A_wg\rangle
=
\int_{\mathbb T^d}w(\zeta)\,\|g^*(\zeta)\|_E^2\,dm(\zeta),
\tag{6}
\]

so

\[
\min w
\le
\langle g,A_{w,M}g\rangle
\le
\max w.
\tag{7}
\]

It remains to show that every boundary value `w(\zeta)` can be approached by Rayleigh quotients of vectors in `M`.

## 2. Every nonzero Hardy vector has boundary mass in every open patch

Fix `0\ne f\in M` and define the finite positive measure

\[
d\nu_f(\zeta)=\|f^*(\zeta)\|_E^2\,dm(\zeta).
\tag{8}
\]

Then

\[
\boxed{\operatorname{supp}\nu_f=\mathbb T^d.}
\tag{9}
\]

Indeed, suppose an open set `U\subset\mathbb T^d` had `\nu_f(U)=0`. It contains a product of nonempty arcs

\[
I_1\times\cdots\times I_d\subset U.
\tag{10}
\]

Hence `f^*=0` almost everywhere on that product. For every `u\in E`, the scalar Hardy function

\[
f_u(z)=\langle f(z),u\rangle_E
\tag{11}
\]

also has boundary values zero there. Iterating the one-variable Hardy boundary uniqueness theorem with Fubini proves `f_u\equiv0`: view the boundary function first as an `H^2(\mathbb D)` function in `z_1` for almost every remaining boundary parameter, conclude that every `z_1` coefficient vanishes on `I_2\times\cdots\times I_d`, and continue inductively. Since (11) vanishes for every `u`, `f\equiv0`, contradicting the choice of `f`.

Thus every nonzero Hardy vector supplies positive boundary mass in every neighborhood. This is the only uniqueness input needed below; no Beurling or Mandrekar–Seto classification enters the argument.

## 3. Coordinate invariance produces peak-localized test vectors inside the same submodule

Fix any `\zeta=(\zeta_1,\ldots,\zeta_d)\in\mathbb T^d` and put

\[
\phi_\zeta(z)
=
\prod_{j=1}^d\frac{1+\overline{\zeta_j}z_j}{2}.
\tag{12}
\]

On the distinguished boundary,

\[
|\phi_\zeta|\le1,
\qquad
|\phi_\zeta(\eta)|=1
\iff
\eta=\zeta.
\tag{13}
\]

Because `M` is invariant under every coordinate shift, it is invariant under every polynomial multiplier. Therefore

\[
h_n=\phi_\zeta^n f\in M.
\tag{14}
\]

These vectors are nonzero. Normalize them by

\[
g_n=\frac{h_n}{\|h_n\|}.
\tag{15}
\]

The probability measures

\[
d\mu_n
=
\frac{|\phi_\zeta|^{2n}\,d\nu_f}
{\int|\phi_\zeta|^{2n}\,d\nu_f}
\tag{16}
\]

concentrate at `\zeta`. To see this without any asymptotic theorem, let `V` be a neighborhood of `\zeta`. Since the maximum in (13) is unique,

\[
a:=\sup_{\mathbb T^d\setminus V}|\phi_\zeta|<1.
\tag{17}
\]

Choose a smaller neighborhood `U\subset V` and `b` with `a<b<1` such that

\[
|\phi_\zeta|>b
\quad\text{on }U.
\tag{18}
\]

By (9), `\nu_f(U)>0`. Hence

\[
\mu_n(\mathbb T^d\setminus V)
\le
\frac{a^{2n}\nu_f(\mathbb T^d)}
{b^{2n}\nu_f(U)}
\longrightarrow0.
\tag{19}
\]

For continuous `w`, equations (16)--(19) imply

\[
\langle g_n,A_{w,M}g_n\rangle
=
\int w\,d\mu_n
\longrightarrow
w(\zeta).
\tag{20}
\]

Since `\zeta` was arbitrary, the closure of the numerical range contains `w(\mathbb T^d)`, in particular `\min w` and `\max w`. Combined with (7), this proves (5).

The theorem is deliberately only a numerical-range statement. For arbitrary non-doubly-commuting submodules it does **not** claim the unitary equivalence, spectral equality, or essential-spectral equality obtained in the narrower Mandrekar–Seto class of `WP-220`.

## 4. Exact application to the finite critical Bost–Connes defect

Let `F` be a nonempty finite set of primes. As in `WP-220`, put

\[
r_p=p^{-1/2}
\tag{21}
\]

and

\[
P_{r_p}(\theta)
=
\frac{1-r_p^2}{1-2r_p\cos\theta+r_p^2}.
\tag{22}
\]

The finite-prime critical defect is

\[
W_F=T(w_F),
\qquad
w_F(\theta)
=
\sum_{p\in F}(\log p)\bigl(1-P_{r_p}(\theta_p)\bigr).
\tag{23}
\]

Each summand is minimized at `\theta_p=0` and maximized at `\theta_p=\pi`, with

\[
1-P_r(0)=-\frac{2r}{1-r},
\qquad
1-P_r(\pi)=\frac{2r}{1+r}.
\tag{24}
\]

Because the coordinates separate, the extrema of (23) are

\[
\min w_F
=
-2\sum_{p\in F}\frac{(\log p)r_p}{1-r_p}<0,
\tag{25}
\]

and

\[
\max w_F
=
2\sum_{p\in F}\frac{(\log p)r_p}{1+r_p}>0.
\tag{26}
\]

Therefore for every Hilbert multiplicity `E` and every nonzero closed `M\subset H^2_E(\mathbb D^{|F|})` invariant under all source coordinate shifts,

\[
\boxed{
\overline{W(P_M(W_F\otimes I_E)|_M)}
=
[\min w_F,\max w_F].
}
\tag{27}
\]

In particular

\[
\boxed{P_M(W_F\otimes I_E)|_M\not\succeq0.}
\tag{28}
\]

This closes the exact gap left in `WP-220`: failure of double commutation can make the submodule geometrically complicated, but it cannot hide any open part of a scalar continuous Toeplitz symbol from the quadratic form while source-shift covariance remains available for localization.

## 5. Passive higher multiplicity is not an escape

The vector-valued formulation matters for the Bost–Connes completion question. One possible response to `WP-220` was to increase Hardy-module multiplicity before imposing the admissibility condition. Equation (27) shows that this does nothing by itself.

If the source completion merely replaces

\[
W_F
\quad\text{by}\quad
W_F\otimes I_E
\tag{29}
\]

and then selects a nonzero joint submodule, the same boundary localization survives. The fiber `E` may be infinite-dimensional and the submodule may mix the prime variables with the fiber; the scalar peak multiplier still stays inside `M`, and the defect still attains both orientations in the closure of its numerical range.

Thus a multiplicity-based survivor must make the additional sector **active** before the sign test. It must change (29) to an operator-valued symbol, alter the form/domain, couple the finite places to the real place, or otherwise modify the source operation itself. Merely tensoring with extra degrees of freedom and compressing cannot supply the missing Weil sign.

## 6. Matched controls

The localization theorem contains no arithmetic input. For arbitrary parameters

\[
0<r_j<1,
\qquad
c_j>0,
\tag{30}
\]

set

\[
w(\theta)
=
\sum_{j=1}^d c_j\bigl(1-P_{r_j}(\theta_j)\bigr).
\tag{31}
\]

Then every nonzero jointly shift-invariant submodule of `H^2_E(\mathbb D^d)` has compressed numerical-range closure

\[
\left[
-2\sum_j\frac{c_jr_j}{1-r_j},
\;
2\sum_j\frac{c_jr_j}{1+r_j}
\right].
\tag{32}
\]

The obstruction therefore survives generalized-prime, arbitrary-generator, and passive-multiplicity controls preserving the same Hardy-module architecture. This is appropriate for a no-go theorem: the failure comes from the operator category, not from a disguised RH input.

Conversely, a positive proposal cannot count mere failure of these controls as arithmetic specificity. It must explain what source-forced global relation changes the scalar-module architecture and why that same relation also produces the finite Mangoldt orientation, the Gamma contribution, the polar/global counterterms, and an independent sign theorem.

## 7. Prior-art and novelty audit

The ingredients of the proof are classical Hardy and Toeplitz theory.

- Boundary values and uniqueness for Hardy functions on the polydisc are standard several-complex-variables function theory; the product-arc uniqueness needed here was also derived explicitly in Section 2 by iterating the one-variable theorem.
- Analytic polynomials peaking at a distinguished-boundary point are elementary, and (12) gives the exact peak family used here.
- Toeplitz quadratic forms with scalar real symbol are ordinary boundary integrals. `WP-220` already records the stronger classical Beurling/Mandrekar–Seto rigidity available when the restricted shifts doubly commute.
- The Hardy-polydisc/submodule literature contains substantially more complicated non-Beurling submodules and quotient modules, so double commutation genuinely was an extra hypothesis rather than an automatic property. A targeted audit of Toeplitz/submodule and numerical-range literature found neighboring results on Toeplitz characterizations, special Beurling quotients, compressed multipliers, and numerical ranges, but no source was used as an independent theorem asserting the exact blanket sign conclusion (27).

No novelty is claimed for Hardy boundary uniqueness, peak localization, numerical ranges, Toeplitz quantization, the Bost–Connes system, or the Mandrekar–Seto theorem. The durable Mathia contribution is the exact reduction of the remaining source-covariant mixed-prime restriction family to the localization lemma above, and the observation that the same proof also eliminates passive vector-valued multiplicity.

This result does not subsume `WP-220`. In the doubly commuting scalar class, `WP-220` proves the stronger operator identity that the whole compression is unitarily equivalent to `W_F`. The present theorem gives less structural information but applies to every nonzero jointly invariant submodule and is exactly strong enough to settle positivity.

## 8. Boundary of the no-go

Three hypotheses are load-bearing.

First, the admissible space is a **submodule** for the same finite-prime coordinate shifts. A non-invariant global test space, a coinvariant/quotient construction, or a relation imposed only after coupling to the real place is not covered.

Second, the finite defect is the same **scalar continuous Toeplitz symbol** on that module. An operator-valued symbol or a non-Toeplitz form produced by genuine finite--archimedean or mixed-prime incidence can evade the localization theorem because its Rayleigh quotient is no longer the scalar average (6).

Third, the theorem is finite-prime at the operator level. It does not by itself construct or exclude a completed infinite-prime domain, the Gamma sector, polar normalization, or an unbounded global form. Any use in such a setting requires an audited passage from its finite cylinders to the declared completed operator.

Within those hypotheses there is no remaining admissible-submodule sign escape. Outside them, positivity is still a new theorem to be proved rather than inherited from the critical Gram.

## 9. Research disposition

This passes the substantive-finding gate as a decisive strengthening of the current Bost–Connes restriction boundary.

The previously open implication

\[
\text{joint source-shift covariance}
+\text{non-doubly-commuting mixed-prime submodule}
\stackrel{?}{\Longrightarrow}
\text{removal of the finite Weil sign defect}
\]

is false. In fact the compressed scalar defect has the same **closed numerical range** as the full symbol for every nonzero joint submodule, independently of double commutation and passive multiplicity.

The accepted Bost–Connes completion question remains unresolved, but its admissible-space branch is now materially sharper. A survivor cannot be obtained by choosing any nonzero joint Hardy submodule of the unchanged finite critical defect. It must instead change covariance, quotient geometry, symbol/operator category, or finite--archimedean coupling before positivity is invoked.