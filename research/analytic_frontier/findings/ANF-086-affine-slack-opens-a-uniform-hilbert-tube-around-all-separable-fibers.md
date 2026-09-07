# ANF-086 — affine slack opens a uniform Hilbert tube around all separable fibers

**Status:** `EXACT-DERIVED + CENTRAL-NOTCH + ALL-HEIGHTS + QUANTITATIVE-NONSEPARABILITY-GATE + UNIFORM-SEPARABLE-CONE-TUBE + STRICT-MONTGOMERY-TAYLOR-IMPROVEMENT`. `ANF-081` supplies one fixed central-notch spectrum with a strict normalization margin on every finite real multiset. `ANF-083` uses part of that margin to open one fixed small-height complex tube around the real locus, and `ANF-085` proves that every exactly separable center-height occupation pattern is safe at arbitrary height. The remaining frontier can be sharpened quantitatively: a counterexample cannot merely have rank at least two. It must stay a fixed positive distance, in the **actual target Hilbert norm**, from every compatible all-height separable carrier.

Fix the spectrum and real constant from `ANF-081`,

\[
J_s=J_{\rm MT}-s\phi_\eta\ge0,
\qquad F_s=\widehat J_s,
\qquad q_s>0,
\tag{1}
\]

and abbreviate

\[
\rho_s:=\frac{C(J_s)}{C_{\rm MT}}.
\tag{2}
\]

The strict objective gap of `ANF-081` is exactly

\[
\boxed{0<\rho_s<q_s.}
\tag{3}
\]

For a finite conjugation-invariant multiset `Z`, put

\[
L(Z):=2|Z|-\sigma(Z),
\tag{4}
\]

where `sigma(Z)` counts simple real sites, and write

\[
S_Z(\alpha):=\sum_{z\in Z}e^{-2\pi i\alpha z},
\qquad
\|f\|_s^2:=\int_{-1}^{1}J_s(\alpha)|f(\alpha)|^2\,d\alpha.
\tag{5}
\]

Let `P` be any product/separable multiset covered by `ANF-085`, with `|P|=|W|`. Define its relative destination-norm defect from an arbitrary conjugation-invariant multiset `W` by

\[
\delta_s(W\mid P)
:=
\frac{\|S_W-S_P\|_s}{\|S_P\|_s}.
\tag{6}
\]

Then the exact perturbative lower bound is

\[
\boxed{
E_{F_s}(W)
\ge
q_s\bigl(1-\delta_s(W\mid P)\bigr)_+^2 L(P).
}
\tag{7}
\]

Consequently, if `sigma(P)<=sigma(W)`, then `L(P)>=L(W)` and every

\[
\boxed{
\delta_s(W\mid P)<
\kappa_{\rm crit}
:=1-\sqrt{\rho_s/q_s}
}
\tag{8}
\]

forces

\[
\frac{E_{F_s}(W)}{L(W)}>\rho_s.
\tag{9}
\]

Thus no configuration capable of destroying the strict Montgomery--Taylor improvement can lie inside this fixed relative Hilbert neighborhood of the all-height separable cone. The radius `kappa_crit` is positive and depends only on the single central-notch certificate, not on cardinality, pair count, horizontal geometry, vertical height, collisions, multiplicities, or matrix rank.

## 1. The perturbation theorem is an exact affine-weighted comparison

`ANF-085` proves for every separable product multiset `P`

\[
\|S_P\|_s^2
=E_{F_s}(P)
\ge q_sL(P).
\tag{10}
\]

In particular `||S_P||_s>0` for every nonempty `P`, so (6) is well-defined. The reverse triangle inequality gives

\[
\begin{aligned}
\|S_W\|_s
&\ge
\bigl(\|S_P\|_s-\|S_W-S_P\|_s\bigr)_+\\
&=
\bigl(1-\delta_s(W\mid P)\bigr)_+\|S_P\|_s.
\end{aligned}
\tag{11}
\]

Squaring and inserting (10) proves (7). No spatial sign statement for `F_s` is used.

It is useful to retain the simple-real bookkeeping rather than hide it inside a rank condition. For arbitrary `P` of the same cardinality as `W`, equation (7) gives the exact effective affine constant

\[
\boxed{
q_{\rm eff}(W\mid P)
:=
q_s\bigl(1-\delta_s(W\mid P)\bigr)_+^2
\frac{L(P)}{L(W)}.
}
\tag{12}
\]

Whenever

\[
q_{\rm eff}(W\mid P)>\rho_s,
\tag{13}
\]

the configuration `W` is individually screened at a normalization that still beats Montgomery--Taylor. Condition (8) is the uniform corollary obtained when `L(P)>=L(W)`.

For a whole class one can keep one fixed normalization. Set, for example,

\[
q_\diamond:=\frac{q_s+\rho_s}{2},
\qquad
\kappa_\diamond
:=1-\sqrt{q_\diamond/q_s}>0.
\tag{14}
\]

Every `W` admitting a same-cardinality separable `P` with

\[
\sigma(P)\le\sigma(W),
\qquad
\delta_s(W\mid P)\le\kappa_\diamond
\tag{15}
\]

satisfies the **same** affine certificate

\[
\boxed{
E_{F_s}(W)\ge q_\diamond L(W),
\qquad
\frac{C(J_s)}{q_\diamond}<C_{\rm MT}.
}
\tag{16}
\]

This is a genuine all-cardinality, all-height open neighborhood of the product class rather than a configuration-by-configuration choice of normalization.

## 2. The radius is exactly paid by the central-notch normalization slack

`ANF-081` writes

\[
q_s=1-sG_s
\tag{17}
\]

and

\[
C(J_s)
=C_{\rm MT}
-sb_\eta\left(1+\frac{\eta^2}{3}\right),
\tag{18}
\]

with

\[
G_s<
\frac{b_\eta}{C_{\rm MT}}
\left(1+\frac{\eta^2}{3}\right).
\tag{19}
\]

Define the positive slack coefficient

\[
\Delta_s
:=
\frac{b_\eta}{C_{\rm MT}}
\left(1+\frac{\eta^2}{3}\right)-G_s>0.
\tag{20}
\]

Then

\[
q_s-\rho_s=s\Delta_s
\tag{21}
\]

and the critical tube radius can be written exactly as

\[
\boxed{
\kappa_{\rm crit}
=1-\sqrt{1-\frac{s\Delta_s}{q_s}}.
}
\tag{22}
\]

In particular,

\[
\boxed{
\kappa_{\rm crit}
\ge
\frac{s\Delta_s}{2q_s}>0,
}
\tag{23}
\]

because `1-sqrt(1-x)=x/(1+sqrt(1-x))>=x/2` for `0<x<1`. The protected thickness is therefore not a qualitative continuity statement. It is exactly the unused affine normalization margin of the fixed notch, converted into a relative Hilbert-distance budget.

This also explains why the target norm matters. A coefficient-space or matrix-rank perturbation can be tiny while a high vertical level multiplies it by a large Fourier--Laplace factor. Equation (22) measures nonseparability only after the same spectral weighting that enters the zeta-side certificate; no height-dependent comparison constant is inserted afterward.

## 3. An intrinsic nonseparability obstruction

Let `Sep(W)` denote the set of nonempty product multisets `P` covered by `ANF-085` such that

\[
|P|=|W|,
\qquad
\sigma(P)\le\sigma(W).
\tag{24}
\]

This comparison class is never empty: the real-part collapse of `W` is a real multiset of the same cardinality, is a degenerate product fiber with vertical profile `{0}`, and cannot have more simple real sites than `W`.

Define

\[
\boxed{
d_{\rm sep}(W)
:=
\inf_{P\in\operatorname{Sep}(W)}
\delta_s(W\mid P).
}
\tag{25}
\]

If

\[
\frac{E_{F_s}(W)}{L(W)}\le\rho_s,
\tag{26}
\]

then (7)--(8) force

\[
\boxed{
d_{\rm sep}(W)\ge\kappa_{\rm crit}>0.}
\tag{27}
\]

Equation (27) is the sharpened frontier. `ANF-085` only showed that an obstruction must have nonseparable center-height occupation, equivalently rank at least two after empty rows and columns are removed. That algebraic condition is now far too weak: a fatal configuration must be **uniformly separated from the entire separable class in the destination Hilbert geometry**.

The theorem does not assert that the infimum in (25) is attained. It does not need to be. If `d_sep(W)<kappa_crit`, there exists a comparator with relative defect strictly below `kappa_crit`, contradicting (26).

## 4. The same obstruction is simultaneously Montgomery--Taylor near-extremal

There is a second independent necessary condition. Since

\[
J_s\ge(1-s)J_{\rm MT},
\tag{28}
\]

one has

\[
E_{F_s}(W)
\ge(1-s)E_{F_{\rm MT}}(W).
\tag{29}
\]

Therefore every fatal configuration satisfying (26) must also obey

\[
\boxed{
\frac{E_{F_{\rm MT}}(W)}{L(W)}
\le
\frac{\rho_s}{1-s}.
}
\tag{30}
\]

Lamzouri's global conjugation Hilbert inequality, recorded in `ANF-002`, gives the corresponding Montgomery--Taylor floor

\[
E_{F_{\rm MT}}(W)\ge L(W).
\tag{31}
\]

Hence the unresolved complex frontier is no longer arbitrary rank-two geometry. A genuine obstruction must lie in the intersection of two constraints:

\[
1\le
\frac{E_{F_{\rm MT}}(W)}{L(W)}
\le
\frac{\rho_s}{1-s},
\tag{32}
\]

whenever the upper endpoint is at least one, **and simultaneously** satisfy the fixed separation (27) from every compatible all-height product carrier. If `rho_s<1-s`, the crude spectral comparison (28)--(31) would already rule out (26) altogether; otherwise (32) is a quantitative near-extremizer gate.

This intersection is the natural next object. Proving that Montgomery--Taylor near-extremizers must approach the separable cone closely enough would close the remaining pairwise complex branch. Conversely, a useful negative result must construct a near-extremal Montgomery--Taylor configuration whose destination-norm distance from every product carrier stays above `kappa_crit`.

## 5. Adversarial audit and failure modes

The derivation has five load-bearing checks. First, the comparator is required to have the same cardinality as `W`; otherwise the affine quantity `L` cannot be transferred by (12). Second, the uniform radius (8) uses `sigma(P)<=sigma(W)` only to ensure `L(P)>=L(W)`; when that inequality fails, the exact ratio in (12) must be retained instead of silently dropping simple-point bookkeeping. Third, the sign gate is handled by `(1-delta)_+` before squaring, so no lower bound is inferred from a negative reverse-triangle expression. Fourth, `||S_P||_s` cannot vanish because the all-height separable theorem supplies the positive floor (10). Fifth, the proof is entirely in `L^2(J_s d alpha)` and therefore does not assume that `F_s=widehat J_s` is pointwise nonnegative.

Two negative controls prevent overstatement. Merely having occupation-matrix rank two does not imply the lower bound (27); rank is discontinuous as a quantitative invariant and an arbitrarily small algebraic perturbation can raise rank. Conversely, small Frobenius or entrywise distance from a product occupation matrix does not by itself imply small `delta_s` uniformly at unbounded height, because the Fourier--Laplace factors `cosh(2 pi alpha y)` can amplify a small high-level defect. The theorem deliberately identifies the norm in which a quantitative rank-one-plus-defect statement is actually sufficient, but it does not yet provide a purely combinatorial upper bound for that norm.

Taking `P` to be the real-part collapse specializes the mechanism to the neighborhood used in `ANF-083`; that finding supplies a geometric small-height condition implying small destination-norm defect. Taking `P=W` for an exactly separable configuration gives `delta_s=0` and recovers `ANF-085`. The present result is the interpolation between those endpoints: arbitrary heights and genuine rank at least two are allowed as long as the configuration remains inside a fixed spectral neighborhood of some safe product carrier.

## 6. Prior art and evidence boundary

The reverse triangle inequality and stability of a quadratic Hilbert norm under relative perturbation are classical and no novelty is claimed for them. Buescu--Paixão--Symeonides provide the classical Fourier--Laplace/positive-definite strip framework already recorded in `SOURCES.md`, while Carneiro--Chandee--Littmann--Milinovich and Lamzouri anchor the pair-correlation Hilbert geometry and Montgomery--Taylor normalization used by the line. A targeted search of positive-definite strip kernels, Hilbert-space perturbation bounds, and rank-one/separable-cone stability did not identify a theorem supplying the line-specific affine threshold (22), the all-height product comparison (12), or the double obstruction (27)+(30). No new external result is load-bearing, so `SOURCES.md` is unchanged.

The result is an auxiliary structural reduction inside the Mathia/BGSST support-one program. It does **not** prove that every finite conjugation-invariant multiset lies in the protected tube, provide a combinatorial estimate for `d_sep`, improve the unconditional simple-critical proportion by itself, or prove RH. It also does not claim theorem-level novelty for generic Hilbert perturbation theory.

## Research consequence

The next pairwise-complex gate should no longer be phrased as “find a rank-two center-height pattern.” Rank two is necessary but not remotely sufficient. A surviving obstruction must be both Montgomery--Taylor near-extremal and at least `kappa_crit` away, in the exact `J_s`-weighted Hilbert geometry, from **every** same-cardinality separable carrier with no worse simple-real count. The decisive next test is therefore a quantitative rigidity statement relating Montgomery--Taylor excess to `d_sep(W)`, or an explicit family violating such a relation. Higher-order carriers should remain deferred until that intersection has been tested.