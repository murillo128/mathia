---
id: WP-273
title: Pole-completed positive compressions require nonlocal prime-power sampling
branch: weil_positivity
status: supported
kind: source-side-compression-obstruction
claim_strength: exact RH-independent Krein reduction plus localizable-subspace no-go
created: 2026-09-12
related: [WP-005, WP-063, WP-132, WP-219, WP-222, WP-269, WP-270, WP-271, WP-272]
prior_art:
  - A. Kamuda, S. Kuzhel, and V. Sudilovskaya, On Dual Definite Subspaces in Krein Space, Complex Analysis and Operator Theory 13 (2019), 1011-1032, DOI 10.1007/s11785-018-0838-x
  - M. Suzuki, On the Hilbert space derived from the Weil distribution, Canadian Journal of Mathematics (2025), DOI 10.4153/S0008414X25101739
  - M. Suzuki, Weil's quadratic form via the screw function, arXiv:2606.09096
---

# WP-273 — Pole-completed positive compressions require nonlocal prime-power sampling

## Claim

`WP-272` rules out continuous scalar spectral multipliers as a way to orient the canonical pole-completed critical carrier

\[
T_{\rm pole}
=\nu_{1/2}-\cosh(x/2)\,dx,
\qquad
\nu_{1/2}
=\frac12\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\bigl(\delta_{\log n}+\delta_{-\log n}\bigr).
\tag{1}
\]

A broader escape is to abandon scalar multiplication and compress the signed carrier to a proper test space. At the level of the two positive measures already present in (1), this route has an exact structural description.

Put

\[
H_+=L^2(\nu_{1/2}),
\qquad
H_-=L^2\!\left(\cosh(x/2)\,dx\right),
\tag{2}
\]

and equip

\[
\mathcal K=H_+\oplus H_-
\tag{3}
\]

with the fundamental Krein form

\[
[(u,v),(u',v')]
=\langle u,u'\rangle_{H_+}-\langle v,v'\rangle_{H_-}.
\tag{4}
\]

Every nonnegative linear subspace `M` of `K` is the graph of a contraction over its arithmetic projection: if `D=P_+M`, then there is a uniquely defined linear map

\[
C:D\to H_-,
\qquad \|Cx\|_{H_-}\le\|x\|_{H_+},
\tag{5}
\]

such that

\[
M=\{x\oplus Cx:x\in D\}.
\tag{6}
\]

For a compression coming from actual functions `f`, equations (5)--(6) say something concrete: positivity is exactly a **weighted prime-power sampling inequality**. On every domain on which both sides are finite,

\[
Q(f):=\langle T_{\rm pole},|f|^2\rangle
=\frac12\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\left(|f(\log n)|^2+|f(-\log n)|^2\right)
-\int_{\mathbb R}\cosh(x/2)|f(x)|^2\,dx.
\tag{7}
\]

Thus `Q>=0` on a linear test space `R` means that the continuum component of every `f in R` must be contractively reconstructible from its values on the Mangoldt support.

This already gives a decisive local no-go. Let

\[
S=\{\pm\log(p^k):p\text{ prime},\ k\ge1\}.
\tag{8}
\]

If a nonzero linear space

\[
R\subset C(\mathbb R)\cap H_+\cap H_-
\tag{9}
\]

is stable under multiplication by compactly supported smooth cutoffs,

\[
f\in R,\ \phi\in C_c^\infty(\mathbb R)
\quad\Longrightarrow\quad
\phi f\in R,
\tag{10}
\]

then `Q` cannot be nonnegative on `R`. In fact, every nonzero continuous `f` has a nonzero localization inside an atom-free interval, and on such a localization the positive arithmetic term in (7) vanishes while the continuous pole term is strictly negative.

More quantitatively, if `I` is bounded and contains exactly `N` points of `S`, then every linear subspace of continuous functions supported in `I` on which `Q>=0` has algebraic dimension at most `N`. In an atom-free interval that dimension is zero.

Therefore a positive compression of the canonical source carrier cannot be a localizable geometric test space. Any surviving compression must be genuinely **global and nonlocal**: an analytic/model/de Branges-type space, a distributional space already tied to `S`, or another source-derived interpolation structure in which local cutoffs are not admissible. Merely saying that the construction "mixes frequencies" is no longer enough. It must canonically produce a contraction from weighted prime-power samples to the pole continuum before the desired sign is inspected.

**Classification:** `EXACT-DERIVED + RH-INDEPENDENT + KREIN-GRAPH-REDUCTION + PRIME-POWER-SAMPLING-INEQUALITY + LOCAL-CUTOFF-NO-GO + FINITE-WINDOW-DIMENSION-BOUND + NONLOCALITY-GATE + PRIOR-ART-AUDITED + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. The signed carrier has a canonical positive-minus-positive Hilbert realization

Equation (1) is always a locally finite signed Radon measure, independently of RH. The atomic part is locally finite because every bounded logarithmic interval contains only finitely many prime powers, and the smooth density `cosh(x/2)` has finite mass on compact intervals. Hence (2) makes sense as a pair of ordinary Hilbert spaces even when `WP-270` says that the signed difference itself is not tempered.

The decomposition (4) is not a proposed new geometry. It is simply the canonical fundamental decomposition attached to the Jordan decomposition of (1). For every compactly supported smooth `f`, define

\[
Jf=(f|_S,f)\in H_+\oplus H_-.
\tag{11}
\]

Then

\[
[Jf,Jf]=Q(f).
\tag{12}
\]

So any proposed source-side test-space compression on which the pole-completed carrier is positive gives a nonnegative subspace `J(R)` of this fixed Krein space.

This formulation deliberately keeps the two obligations separate. `H_+` remembers the exact critical Mangoldt half-density already forced in `WP-256` and isolated in `WP-269`; `H_-` is the independently forced pole background of `WP-270`. Positivity is not built into either identification. It is the additional statement that their difference is nonnegative on the selected range.

## 2. Every positive range is a graph contraction

Let `M subset K` be a linear subspace satisfying

\[
[m,m]\ge0
\qquad(m\in M).
\tag{13}
\]

The projection `P_+|_M` is injective. Indeed, if `m=0\oplus y` lies in `M`, then

\[
0\le[m,m]=-\|y\|_{H_-}^2,
\tag{14}
\]

so `y=0`.

Set `D=P_+M`. For `x in D`, there is therefore a unique `m=x\oplus y in M`; define `Cx=y`. Equation (13) gives

\[
0\le\|x\|_{H_+}^2-\|Cx\|_{H_-}^2,
\tag{15}
\]

hence `C` is contractive on its domain and (6) follows. Conversely, the graph of any contraction satisfies (13).

This is the standard angular-operator description of positive subspaces in Krein-space theory; Kamuda--Kuzhel--Sudilovskaya give a modern reference in the setting of definite subspaces. No novelty is claimed for the graph theorem itself. Its use here is to identify exactly what a positive compression of (1) would have to encode.

If `M=J(R)`, then the arithmetic projection is the weighted sample vector

\[
E(f)=\left(
\sqrt{\frac{\Lambda(n)}{2\sqrt n}}\,f(\log n),
\sqrt{\frac{\Lambda(n)}{2\sqrt n}}\,f(-\log n)
\right)_{n\ge2,\ \Lambda(n)>0},
\tag{16}
\]

with repetitions omitted in the obvious way. The continuum component is the class of `f` in `H_-`. Thus (15) is exactly

\[
\boxed{
\int_{\mathbb R}\cosh(x/2)|f(x)|^2\,dx
\le
\frac12\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\left(|f(\log n)|^2+|f(-\log n)|^2\right).
}
\tag{17}
\]

The missing sign theorem has therefore become an interpolation/sampling theorem with a fixed arithmetic sampling set and a fixed continuum norm. An arbitrary contraction can always manufacture a nonnegative graph; what matters for Mathia is whether Prime Circle, Prime Flute, Prime Lattice, or another intrinsic construction forces the contraction before the Weil sign is read.

## 3. Cutoff stability is incompatible with positivity

Assume (9)--(10), `R != {0}`, and `Q(f)>=0` for all `f in R`. Choose `0 != f in R` and a point `x_0` with `f(x_0) != 0`. By continuity, `f` is nonzero on some open neighborhood `U` of `x_0`.

The set `S` in (8) is locally discrete. Hence `U` contains a point `y notin S` and, after shrinking, an open interval

\[
J\Subset U,
\qquad J\cap S=\varnothing.
\tag{18}
\]

Choose a nonzero `phi in C_c^infty(J)` supported where `f` does not vanish. By (10), `g=phi f` belongs to `R`, and `g != 0`. But every arithmetic sample of `g` is zero, so (7) becomes

\[
Q(g)
=-\int_J\cosh(x/2)|g(x)|^2\,dx
<0,
\tag{19}
\]

contradicting positivity.

Therefore

\[
\boxed{
R\ne\{0\},\ C_c^\infty\text{-cutoff stability}
\quad\Longrightarrow\quad
Q|_R\not\ge0.
}
\tag{20}
\]

This excludes much more than scalar spectral filtering. Any ordinary local energy domain that remains closed under spatial/spectral cutoffs can isolate an atom-free patch of the negative background and therefore cannot inherit positivity from the pole-completed carrier.

The conclusion is not that no positive compression exists. It is that a positive one must destroy this localization principle. Analytic and model spaces are the canonical examples of spaces in which multiplying by an arbitrary compactly supported cutoff leaves the space, so they sit exactly on the surviving side of (20).

## 4. Finite windows have an exact dimension bound

Let `I` be a bounded interval and write

\[
S\cap I=\{s_1,\ldots,s_N\}.
\tag{21}
\]

Let `R_I` be any linear subspace of continuous functions supported in `I` for which `Q>=0`. Consider the evaluation map

\[
\mathcal E_I:R_I\to\mathbb C^N,
\qquad
f\mapsto(f(s_1),\ldots,f(s_N)).
\tag{22}
\]

If `f` lies in its kernel, then the atomic part of (7) vanishes and

\[
0\le Q(f)
=-\int_I\cosh(x/2)|f(x)|^2\,dx.
\tag{23}
\]

Hence `f=0` almost everywhere and, by continuity, identically. Therefore `E_I` is injective and

\[
\boxed{\dim R_I\le N.}
\tag{24}
\]

For every atom-free interval, `N=0`, so no nonzero continuous positive direction can be supported there. This is the finite-window version of the contraction picture: positive directions have at most the number of arithmetic sampling degrees of freedom available in the window.

No asymptotic prime theorem enters this result. It depends only on the exact local support and signs in (1).

## 5. Aggressive falsification and matched controls

The theorem does not prove RH and does not produce a candidate positive space. The graph construction goes in both directions: **every** contraction `C` produces a nonnegative subspace. Without an independent source law selecting `C`, the mechanism is fully sign-programmable. This is the continuous-source analogue of the warning in `WP-222`, where coinvariant quotients of the same Bost--Connes defect can be tuned to either sign.

The result is also deliberately generic. Replace `S` by any locally discrete set, give its atoms positive weights, and replace `cosh(x/2)` by any strictly positive continuous density. The same graph theorem, cutoff obstruction, and dimension bound hold. Consequently they provide an architectural exclusion, not arithmetic specificity. A successful Riemann construction still has to explain why its nonlocal sampling law is the canonical one and why it simultaneously produces the Gamma and polar terms of the completed Weil form.

Nor does (20) rule out a de Branges, model-space, or other analytic completion. Such spaces are intrinsically nonlocal and can possess discrete sampling formulas. Suzuki's Hilbert space derived from the Weil distribution is an important control: under RH it is isomorphic to a de Branges space, so nonlocal Hilbert geometry and discrete sampling are entirely compatible with the **zero-side Weil form**. But that construction begins with the Weil distribution/RH-equivalent positivity and does not provide an independent source-side map from the Mangoldt samples in (16) to the pole continuum. Importing it here would therefore fail the branch's independence requirement.

Likewise, allowing generalized functions supported directly on `S` evades the continuity hypothesis, but then the source-support selection has already been inserted into the state space. Such a route is admissible only if Mathia's geometry independently forces that distributional boundary law; otherwise it is the same support coding exposed by the discontinuous control in `WP-272`.

Finally, the theorem does not assume that `T_pole` is tempered. `WP-270` proves that global temperedness of the signed difference is equivalent to RH, but the two Hilbert measures in (2), the compactly supported test form (7), and the local no-go (20) are all defined unconditionally. Thus the present restriction does not smuggle the RH-equivalent category descent into its hypotheses.

## 6. Prior-art and novelty audit

The positive-subspace/graph-contraction theorem is classical Krein-space theory. Kamuda, Kuzhel, and Sudilovskaya provide a modern formulation in which positive and uniformly positive subspaces are represented by contractive angular operators. The finite-window injectivity argument is elementary measure theory. No claim of novelty is made for either ingredient.

The closest substantive zeta-side control located in the bounded audit is Suzuki's 2025 construction of the Hilbert space obtained from the Weil distribution under RH and its identification with a de Branges space, together with his 2026 screw-function/operator realization of the Weil quadratic form. These works confirm that nonlocal analytic test spaces are a natural destination, but they do not turn (17) into an unconditional source-derived sampling theorem. The direction of construction is crucial: a Hilbert space whose positivity is already equivalent to RH cannot be reused as the independent geometry demanded here.

Within Mathia, `WP-219`--`WP-222` study a different restriction problem for the Bost--Connes Toeplitz defect: source-shift-invariant Hardy submodules are sign-inert, whereas coinvariant quotients can program either sign. `WP-272` studies scalar multiplication of the present pole-completed source measure. The new content here is the intermediate structural boundary: **even after arbitrary linear compression is allowed, every localizable continuous positive range is impossible, and every surviving positive range is necessarily a nonlocal contraction from arithmetic samples to the continuous pole sector.**

A directed search around Krein positive subspaces, de Branges realizations of the Weil form, and zeta sampling/interpolation found the classical graph theorem and the Weil/de Branges constructions above, but no independent theorem deriving the particular source-side contraction (17) from Prime Circle, Prime Flute, Prime Lattice, or equivalent prime geometry. This negative search is not evidence that such a theorem cannot exist; it only fixes the novelty boundary for the present result.

## Consequence

`WP-269`--`WP-273` now separate four increasingly strong requirements. The critical Mangoldt carrier itself needs an exponential-growth host; canonical pole subtraction reaches the tempered category exactly on RH; finite-order conditional positivity and continuous scalar filtering cannot repair the sign; and **localizable test-space compression cannot repair it either**.

The remaining source-side compression problem is therefore sharply nonlocal. A viable Mathia construction must derive, from independent geometry, a global interpolation/sampling law that maps the exact weighted prime-power data (16) contractively into the pole/archimedean continuum, while also supplying the missing Gamma and polar structure and surviving generalized-prime or matched controls. Choosing a convenient contraction after seeing the target sign is not a bridge; deriving the contraction is now the bridge.