# WP-219 — Shift-invariant test-space restrictions preserve the Bost–Connes Weil defect

**Status:** `EXACT-DERIVED + BOST-CONNES-CRITICAL-GRAM + BEURLING-INVARIANT-SUBSPACE + TOEPLITZ-COMPRESSION-RIGIDITY + TEST-SPACE-NO-GO + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-218` leaves one qualitatively different escape from its compact-perturbation obstruction: perhaps the Bost–Connes source itself selects a proper admissible test space on which the negative Weyl packets of the prime-axis Weil defect are absent. For the most natural source-compatible version of that idea—requiring the admissible prime-power space to remain invariant under the Bost–Connes prime shift—this escape is impossible in an exact way.

Fix a prime `p`, put `r=p^{-1/2}`, and realize the prime-power ray on

\[
H^2(\mathbb T)\simeq \ell^2(\mathbb N_0),
\qquad
S f(z)=z f(z).
\]

As in `WP-218`, the critical Bost–Connes finite-Weil defect is the self-adjoint Toeplitz operator

\[
W_p=T(w_p),
\qquad
w_p(\theta)=\log p\left(1-P_r(\theta)\right),
\]

whose symbol has a nonempty open negative region around `theta=0`.

Let `M` be any nonzero closed subspace of the prime ray satisfying the source covariance

\[
S M\subseteq M.
\]

Beurling's theorem gives

\[
M=\Theta H^2
\]

for an inner function `Theta`. Multiplication by `Theta` is a unitary map

\[
U_\Theta:H^2\longrightarrow M.
\]

For every `f,g in H^2`, using `|Theta|=1` almost everywhere on the circle,

\[
\begin{aligned}
\langle U_\Theta f,\,T(w_p)U_\Theta g\rangle
&=\int_{\mathbb T}w_p\,\overline{\Theta f}\,\Theta g\,dm\\
&=\int_{\mathbb T}w_p\,\overline f g\,dm\\
&=\langle f,T(w_p)g\rangle.
\end{aligned}
\]

Hence the compression of the Weil defect to **every** nonzero shift-invariant admissible subspace is exactly unitarily equivalent to the original defect:

\[
\boxed{
U_\Theta^*\bigl(P_M W_p|_M\bigr)U_\Theta=W_p.
}
\]

Therefore no such restriction removes even one aspect of the sign problem. In particular,

\[
\boxed{
P_MW_p|_M\not\succeq0
}
\]

for every nonzero closed `S`-invariant `M`, and its spectrum and essential spectrum are the same as those of `W_p`.

This closes a natural part of the test-space escape left open by `WP-218`. A source-derived admissibility condition cannot rescue the critical Bost–Connes prime ray merely by selecting a nonzero submodule for the same prime-power semigroup action. Any surviving restriction must **break the one-prime shift covariance, couple prime rays before the restriction is formed, or otherwise destroy the scalar multiplicity-one Hardy module itself**. That is a substantially stronger requirement than merely being noncompact.

## 1. Exact source dictionary

`WP-216` constructs the critical Bost–Connes conditional Gram on the `p`-power ray,

\[
G_{1,p}(a,b)=r^{|a-b|},
\qquad r=p^{-1/2},
\tag{1}
\]

and identifies the desired finite-Weil orientation as

\[
W_p=\log p\,(I-G_{1,p}).
\tag{2}
\]

Under the Hardy identification `e_a <-> z^a`, the Bost–Connes prime isometry acts by the unilateral shift

\[
S z^a=z^{a+1}.
\tag{3}
\]

`WP-218` then writes

\[
G_{1,p}=T(P_r),
\qquad
W_p=T(w_p),
\tag{4}
\]

with

\[
P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2},
\qquad
w_p=\log p\,(1-P_r).
\tag{5}
\]

The symbol satisfies

\[
w_p(0)=-\frac{2(\log p)r}{1-r}<0,
\tag{6}
\]

so continuity gives an open arc on which `w_p<0`.

The present question is not whether an arbitrary hand-picked subspace can delete that arc. It is whether the source semigroup can impose an admissibility condition while preserving its own prime-power action. On the multiplicity-one prime ray, that means precisely a nonzero closed `S`-invariant subspace.

## 2. Beurling rigidity makes every covariant restriction isometric

Let

\[
0\ne M\subset H^2
\]

be closed and invariant under `S`. Beurling's invariant-subspace theorem states that there is an inner function `Theta`, unique up to a unimodular scalar, such that

\[
M=\Theta H^2.
\tag{7}
\]

Define

\[
U_\Theta f=\Theta f.
\tag{8}
\]

Since the boundary values of an inner function satisfy `|Theta|=1` almost everywhere, `U_Theta` is unitary from `H^2` onto `M`.

For any bounded real symbol `w` and `f,g in H^2`,

\[
\begin{aligned}
\langle U_\Theta f,T(w)U_\Theta g\rangle_{H^2}
&=\langle \Theta f,P_+(w\Theta g)\rangle_{L^2}\\
&=\langle \Theta f,w\Theta g\rangle_{L^2}\\
&=\langle f,wg\rangle_{L^2}\\
&=\langle f,T(w)g\rangle_{H^2}.
\end{aligned}
\tag{9}
\]

The second equality uses that `Theta f` already lies in `H^2`; the third uses `|Theta|=1` almost everywhere. Since testing against vectors in `M` makes the outer projection `P_M` invisible in the quadratic pairing, (9) is equivalently the operator identity

\[
\boxed{
U_\Theta^*\bigl(P_MT(w)|_M\bigr)U_\Theta=T(w).
}
\tag{10}
\]

Equation (10) is stronger than preservation of essential spectrum. The **entire compressed Toeplitz form is unchanged up to unitary equivalence**. It holds for every bounded symbol `w`, not only the Poisson defect.

Applying (10) to `w=w_p` gives

\[
\sigma(P_MW_p|_M)=\sigma(W_p)
\tag{11}
\]

and

\[
\sigma_{\rm ess}(P_MW_p|_M)=\sigma_{\rm ess}(W_p).
\tag{12}
\]

By `WP-218`, the latter contains the interval

\[
\left[
-\frac{2(\log p)r}{1-r},
\frac{2(\log p)r}{1+r}
\right],
\tag{13}
\]

so positivity is impossible on `M`.

## 3. Algebraic difference and augmentation constraints also fail

The same argument covers the obvious algebraic attempts to encode a source-derived constraint by finite differences along the prime-power ray.

Let `q` be any nonzero bounded analytic multiplier and consider the range

\[
q(S)H^2=qH^2.
\tag{14}
\]

Write the inner–outer factorization

\[
q=\Theta O.
\tag{15}
\]

The outer factor has dense range, hence

\[
\overline{qH^2}=\Theta H^2.
\tag{16}
\]

By (10), the restriction of the Toeplitz quadratic form to the closure (16) is exactly the original form. Because the form is bounded and `qH^2` is dense in that closure, a negative vector in `Theta H^2` is approximated by vectors in the actual algebraic range `qH^2`; eventually their Rayleigh quotients are negative as well.

Thus no nonzero analytic shift filter can remove the bad sign. In particular, the elementary difference/augmentation channel

\[
(I-S)H^2=(1-z)H^2
\tag{17}
\]

is not a rescue: `1-z` is outer, so its range is dense in all of `H^2`. Finite polynomial difference constraints and finite products of such source-covariant filters fall under the same argument.

This matters for the Bost–Connes interpretation. A constraint generated solely from repeated application of the same prime isometry and then closed in the natural Hardy norm remains within the Beurling class. It can rearrange representatives but cannot change the Toeplitz sign geometry seen by the Weil defect.

## 4. Relation to the compact-completion obstruction

`WP-218` shows that adding a compact self-adjoint correction cannot remove the negative essential interval of `W_p`. The present theorem attacks the other side of the same escape surface: **restricting the test space while preserving the prime shift cannot remove it either**.

These are logically distinct no-go statements. A shift-invariant subspace can have infinite codimension, so it need not be obtainable by deleting finitely many GNS directions or by a compact perturbation. Nevertheless its compressed Toeplitz form is still exactly the original one because Beurling's inner multiplier is unimodular on the boundary.

Conversely, an arbitrary non-shift-invariant restriction is not covered here. A global constraint could in principle correlate prime rays so strongly that its intersection with an individual prime-axis Hardy module is zero or is not invariant under the prime shift. Such a construction would evade (10), but it would also have to explain why breaking the source semigroup covariance is canonical and how the resulting global space still carries the finite Mangoldt coefficients, the Gamma term, the polar term, and an independent positivity theorem.

## 5. Matched controls and arithmetic specificity

The rigidity theorem uses no arithmetic property of `p`. For any `0<r<1` and any real bounded Toeplitz symbol `w`, every nonzero shift-invariant Hardy subspace has the same compressed quadratic form as `T(w)` up to unitary equivalence.

Therefore the obstruction survives arbitrary-generator and generalized-prime controls preserving the multiplicity-one shift architecture. This is appropriate for a negative classification result: it says that **semigroup covariance itself is too weak to select a favorable Weil test space**.

A positive construction would need extra global structure that is absent from those controls. Merely replacing the ordinary primes by their Bost–Connes provenance does not change the invariant-subspace theorem.

## 6. Prior-art and novelty audit

The functional analysis used here is classical. Arne Beurling's theorem classifies every nonzero closed invariant subspace of the unilateral shift on `H^2` as `Theta H^2` for an inner function `Theta`: A. Beurling, **“On two problems concerning linear transformations in Hilbert space,”** *Acta Mathematica* **81** (1949), 239–255, DOI `10.1007/BF02395019`. The inner–outer factorization and density of outer multiples in `H^2` are likewise standard Hardy-space theory. `WP-218` already supplies the classical Toeplitz/Calkin side and the exact Bost–Connes prime-axis defect.

A targeted literature search for Bost–Connes/Toeplitz invariant-subspace restrictions and for Beurling-type restrictions of Weil positivity found no source asserting the specific reduction above. No novelty is claimed for Beurling's theorem, Toeplitz compression, inner–outer factorization, or the Bost–Connes system. The Mathia contribution is the exact application to the remaining `WP-218` test-space escape: source-covariant prime-axis restrictions are sign-inert because the relevant Toeplitz form is unchanged under every inner-module embedding.

This must not be confused with Nyman–Beurling or Connes–Consani compression prior art. Nyman–Beurling totality is an RH-equivalent closure problem with its own zero-sensitive global subspace, while Connes–Consani use nontrivial phase-space cutoff/compression at the archimedean place. Neither is a claim that a nonzero `S`-invariant submodule of this Bost–Connes prime-axis Hardy space makes `W_p` positive. In particular, the present theorem is **not** a no-go for arbitrary non-invariant, semilocal, adelic, Sonin, or trace-formula test spaces.

## 7. Research disposition

This passes the substantive-finding gate as a decisive negative for an explicit surviving class named by `WP-218`.

The excluded implication is now

\[
\boxed{
\text{critical Bost--Connes Weil defect}
+\text{nonzero prime-shift-invariant admissible subspace}
\not\Rightarrow
\text{positive Weil form}.
}
\]

Together, `WP-218` and `WP-219` show that neither compact completion nor a covariant submodule restriction can repair the local critical orientation while leaving the one-prime Hardy module intact. A surviving Bost–Connes route must therefore act **noncompactly and nontrivially across the module structure**: it must couple primes or the real place before restriction, break the scalar prime-shift invariant channel in a source-forced way, and still recover the full completed Weil coefficients with an independent sign theorem.
